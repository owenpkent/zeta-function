"""Python 3 reader for the LMFDB/Platt rigorous zeta-zero binary archive.

Ports `experiments/primes/_cache/datasets/lmfdb/platt/platt_zeros.py` (Jonathan
Bober, Python 2, upstream at beta.lmfdb.org/riemann-zeta-zeros/examples/
every_millionth_zero/platt_zeros.py) to Python 3, without the sqlite
`index.db` that script uses to jump between files: this module only needs
to decode files whose names are already known (see acquisition report), so
every lookup is a sequential scan of the one open file.

FORMAT OF A `.dat` FILE.

    offset 0:  uint64 LE            number_of_blocks
    then `number_of_blocks` blocks back to back, each:
        32-byte header:  t0, t1 (float64 LE), Nt0, Nt1 (uint64 LE)
            t0, t1:   the height range [t0, t1) this block covers
            Nt0, Nt1: the zero-index range [Nt0, Nt1) this block covers
                      (Nt1 - Nt0 zeros in the block)
        (Nt1 - Nt0) entries of 13 bytes each: uint64 LE, uint32 LE, uint8.
            The three fields concatenate (little-endian) into a 104-bit
            unsigned integer delta. Z accumulates deltas from 0 at the
            start of the block; the k-th zero in the block has height
            t0 + Z_k * 2**-101 exactly, where Z_k is the running sum of
            the first k deltas and 2**-101 is the archive's stated
            absolute precision (EPS_BITS below).

Filenames encode the block grid: `zeros_<T0>.dat`, T0 = int(t0) of the
file's first block. Established by decoding md5sum.log's 14,580 filenames
and cross-checking against downloaded files, not assumed: ordinary files
span 2,100,000 in height (1000 blocks of 2100 each); a short run of early
files (heights below 2.3e5) and the archive's final file are shorter. See
the acquisition report for the derivation.

EXACT ARITHMETIC, NOT mpmath. t0 is an exact float64 and Z*2**-101 is an
exact dyadic fraction, so a zero's height is an EXACT rational with no
rounding at all if the arithmetic is done in Python's `fractions.Fraction`
rather than fixed-precision mpmath. That makes reproducing a reference
file's printed decimal digits a correctly-rounded truncation with no
rounding-mode ambiguity to chase, so this module has no mpmath dependency.

A NOTED UPSTREAM QUIRK. Bober's original comments that "at least one of
the files has some sort of garbage at the end", which is why the decoder
stops at the declared `number_of_blocks` rather than reading to EOF. This
module does the same, and separately reports any trailing bytes rather
than treating them as a hard validation failure.

Usage:
    python -m experiments.primes.platt_reader                    # validate every .dat in data/
    python -m experiments.primes.platt_reader path/to/zeros_X.dat  # validate specific file(s)
"""
from __future__ import annotations

import hashlib
import os
import struct
import sys
from dataclasses import dataclass
from fractions import Fraction
from math import log, pi
from pathlib import Path

import numpy as np

PLATT_DIR = Path(__file__).resolve().parent / "_cache" / "datasets" / "lmfdb" / "platt"
DATA_DIR = PLATT_DIR / "data"
MD5LOG_PATH = PLATT_DIR / "md5sum.log"
EVERY_MILLIONTH_PATH = PLATT_DIR / "every_millionth"

EPS_BITS = 101
EPS = Fraction(1, 1 << EPS_BITS)   # 2**-101, the archive's stated absolute precision

FILE_HEADER_FMT = "<Q"
FILE_HEADER_SIZE = struct.calcsize(FILE_HEADER_FMT)     # 8

BLOCK_HEADER_FMT = "<ddQQ"
BLOCK_HEADER_SIZE = struct.calcsize(BLOCK_HEADER_FMT)   # 32

# Packed (no padding: checked against calcsize('<QIB') == 13) little-endian
# view of one 13-byte entry, so a whole block's payload decodes in one call.
ENTRY_DTYPE = np.dtype([("lo", "<u8"), ("mid", "<u4"), ("hi", "u1")])
ENTRY_SIZE = ENTRY_DTYPE.itemsize                       # 13


@dataclass
class BlockHeader:
    index: int      # block number within the file, 0-based
    offset: int     # byte offset of this block's 32-byte header
    t0: float
    t1: float
    Nt0: int
    Nt1: int

    @property
    def n_zeros(self) -> int:
        return self.Nt1 - self.Nt0


@dataclass
class FileReport:
    path: str
    size_bytes: int
    n_blocks: int
    n_first: int            # rank of the first decoded zero (inclusive)
    n_last: int             # rank of the last decoded zero (inclusive)
    t_first: float          # header t0 of the first block
    t_last: float           # header t1 of the last block
    gamma_first: Fraction
    gamma_last: Fraction
    strictly_increasing: bool
    bad_deltas: int          # entries with a zero (non-positive) delta
    chaining_ok: bool         # every block's (t0, Nt0) matches the previous (t1, Nt1)
    index_count_ok: bool      # sum of per-block (Nt1-Nt0) equals n_last - n_first
    trailing_bytes: int       # bytes in the file past the declared blocks (see module docstring)
    density_ratio: float      # observed zeros-per-height over the RvM prediction at the midpoint
    n_checked: int            # every_millionth indices inside this window
    n_matched: int            # of those, how many matched to all printed digits
    mismatches: list          # [(n, ours, theirs), ...]


def iter_block_headers(path: str | Path):
    """Yield a BlockHeader for every block, seeking past entry payloads.

    Cheap: never reads the (Nt1 - Nt0) * 13 bytes of zero data in a block it
    is only passing over, so this is the fast way to index a large file.
    """
    with open(path, "rb") as fh:
        (n_blocks,) = struct.unpack(FILE_HEADER_FMT, fh.read(FILE_HEADER_SIZE))
        for i in range(n_blocks):
            offset = fh.tell()
            raw = fh.read(BLOCK_HEADER_SIZE)
            if len(raw) < BLOCK_HEADER_SIZE:
                raise ValueError(f"{path}: truncated block header at block {i}/{n_blocks}")
            t0, t1, Nt0, Nt1 = struct.unpack(BLOCK_HEADER_FMT, raw)
            header = BlockHeader(i, offset, t0, t1, Nt0, Nt1)
            yield header
            fh.seek(header.n_zeros * ENTRY_SIZE, os.SEEK_CUR)


def zero_height(t0: float, Z: int) -> Fraction:
    """Exact height of a zero: t0 (exact as a float64) plus Z * 2**-101."""
    return Fraction(t0) + Z * EPS


def decimal_str(x: Fraction, decimals: int) -> str:
    """Correctly-rounded fixed-point decimal string of a non-negative Fraction."""
    if x < 0:
        raise ValueError("decimal_str expects a non-negative Fraction (zero heights are)")
    n, d = x.numerator, x.denominator
    q, r = divmod(n * 10**decimals, d)
    if 2 * r >= d:          # round half away from zero; exact ties are not
        q += 1              # expected in ~40 significant digits of a zero height
    s = str(q).rjust(decimals + 1, "0")
    return s if decimals == 0 else f"{s[:-decimals]}.{s[-decimals:]}"


def zero_at_index(path: str | Path, target_N: int) -> tuple[int, Fraction]:
    """The exact (N, height) of the zero at index target_N in this file.

    Nt0 is a COUNT (the number of zeros below t0), not a label, so the
    block's own zeros carry ranks Nt0+1 .. Nt1 inclusive: the first entry
    consumed from a block is rank Nt0+1. Getting this backwards (using
    Nt0 as if it were the first rank) reads one entry too many and returns
    the next zero instead, which is wrong by about one local zero spacing
    and was caught exactly that way, against every_millionth, before this
    comment was written.

    Scans block headers (cheap) to find the enclosing block, then decodes
    only that block's deltas up through target_N with a plain Python loop
    (at most a few thousand entries, so this is fast).
    """
    with open(path, "rb") as fh:
        (n_blocks,) = struct.unpack(FILE_HEADER_FMT, fh.read(FILE_HEADER_SIZE))
        for i in range(n_blocks):
            t0, t1, Nt0, Nt1 = struct.unpack(BLOCK_HEADER_FMT, fh.read(BLOCK_HEADER_SIZE))
            n_zeros = Nt1 - Nt0
            if not (Nt0 < target_N <= Nt1):
                fh.seek(n_zeros * ENTRY_SIZE, os.SEEK_CUR)
                continue
            need = target_N - Nt0
            raw = fh.read(need * ENTRY_SIZE)
            entries = np.frombuffer(raw, dtype=ENTRY_DTYPE)
            Z = 0
            for lo, mid, hi in zip(entries["lo"].tolist(), entries["mid"].tolist(),
                                    entries["hi"].tolist()):
                Z += lo + (mid << 64) + (hi << 96)
            return target_N, zero_height(t0, Z)
    raise KeyError(f"index {target_N} not found in {path}")


def rvm_density(T: float) -> float:
    """Riemann-von Mangoldt zero density log(T/2pi)/(2pi) at height T."""
    return log(T / (2.0 * pi)) / (2.0 * pi)


def load_every_millionth(path: str | Path) -> dict[int, str]:
    """{index: gamma-as-printed} for every row of the every_millionth file."""
    table: dict[int, str] = {}
    with open(path) as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            n_str, gamma_str = line.split()
            table[int(n_str)] = gamma_str
    return table


def load_md5log(path: str | Path) -> dict[str, str]:
    """{filename: expected md5} from the upstream md5sum.log."""
    table: dict[str, str] = {}
    with open(path) as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            digest, name = line.split(" *", 1)
            table[name] = digest
    return table


def file_md5(path: str | Path, chunk_size: int = 1 << 20) -> str:
    h = hashlib.md5()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(chunk_size), b""):
            h.update(chunk)
    return h.hexdigest()


def validate_file(path: str | Path, every_millionth: dict[int, str] | None = None) -> FileReport:
    """Decode a whole .dat file once, checking every structural invariant.

    Strict monotonicity is checked WITHOUT converting every zero to a
    height: since eps > 0 and Z only accumulates within a block, the
    decoded sequence is strictly increasing iff every entry's 104-bit
    delta is nonzero, which is a fully vectorized numpy comparison per
    block. Full-precision Fraction heights are only computed for the
    first and last zero of the file (for the report) and for whichever
    every_millionth indices fall in this file's range.

    Rank convention: Nt0/Nt1 are COUNTS (zeros strictly below t0/t1), so a
    block's own zeros carry ranks Nt0+1 .. Nt1 inclusive (see
    zero_at_index). n_first/n_last below follow that convention.
    """
    path = str(path)
    size = os.path.getsize(path)
    every_millionth = every_millionth or {}

    n_first = n_last = None
    t_first = t_last = None
    prev_t1 = prev_Nt1 = None
    chaining_ok = True
    bad_deltas = 0
    total_entries = 0
    gamma_first = gamma_last = None

    with open(path, "rb") as fh:
        (n_blocks,) = struct.unpack(FILE_HEADER_FMT, fh.read(FILE_HEADER_SIZE))
        for i in range(n_blocks):
            t0, t1, Nt0, Nt1 = struct.unpack(BLOCK_HEADER_FMT, fh.read(BLOCK_HEADER_SIZE))
            if i == 0:
                n_first, t_first = Nt0 + 1, t0
            elif t0 != prev_t1 or Nt0 != prev_Nt1:
                chaining_ok = False
            prev_t1, prev_Nt1 = t1, Nt1
            n_last, t_last = Nt1, t1

            n_zeros = Nt1 - Nt0
            total_entries += n_zeros
            raw = fh.read(n_zeros * ENTRY_SIZE)
            entries = np.frombuffer(raw, dtype=ENTRY_DTYPE)
            nonzero = (entries["lo"] != 0) | (entries["mid"] != 0) | (entries["hi"] != 0)
            bad_deltas += n_zeros - int(nonzero.sum())

            if i == 0:
                Z0 = int(entries["lo"][0]) + (int(entries["mid"][0]) << 64) + (int(entries["hi"][0]) << 96)
                gamma_first = zero_height(t0, Z0)
            if i == n_blocks - 1:
                Z = 0
                for lo, mid, hi in zip(entries["lo"].tolist(), entries["mid"].tolist(),
                                        entries["hi"].tolist()):
                    Z += lo + (mid << 64) + (hi << 96)
                gamma_last = zero_height(t0, Z)

        trailing_bytes = len(fh.read())

    index_count_ok = total_entries == (n_last - n_first + 1)
    strictly_increasing = bad_deltas == 0 and chaining_ok
    density_ratio = ((n_last - n_first + 1) / (t_last - t_first)) / rvm_density((t_first + t_last) / 2.0)

    checked = matched = 0
    mismatches = []
    for n in sorted(every_millionth):
        if n_first <= n <= n_last:
            checked += 1
            _, gamma = zero_at_index(path, n)
            expected = every_millionth[n]
            decimals = len(expected.split(".")[1])
            ours = decimal_str(gamma, decimals)
            if ours == expected:
                matched += 1
            else:
                mismatches.append((n, ours, expected))

    return FileReport(
        path=path, size_bytes=size, n_blocks=n_blocks,
        n_first=n_first, n_last=n_last, t_first=t_first, t_last=t_last,
        gamma_first=gamma_first, gamma_last=gamma_last,
        strictly_increasing=strictly_increasing, bad_deltas=bad_deltas,
        chaining_ok=chaining_ok, index_count_ok=index_count_ok,
        trailing_bytes=trailing_bytes, density_ratio=density_ratio,
        n_checked=checked, n_matched=matched, mismatches=mismatches,
    )


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    paths = [Path(p) for p in argv] if argv else sorted(DATA_DIR.glob("*.dat"))
    if not paths:
        print(f"no .dat files given and none found in {DATA_DIR}")
        return 1

    md5_map = load_md5log(MD5LOG_PATH) if MD5LOG_PATH.exists() else {}
    every_millionth = load_every_millionth(EVERY_MILLIONTH_PATH) if EVERY_MILLIONTH_PATH.exists() else {}
    if not md5_map:
        print(f"warning: no md5sum.log at {MD5LOG_PATH}, skipping md5 checks")
    if not every_millionth:
        print(f"warning: no every_millionth at {EVERY_MILLIONTH_PATH}, skipping cross-checks")

    all_ok = True
    for path in paths:
        print(f"=== {path.name} ===")
        print(f"  bytes: {path.stat().st_size:,}")

        if path.name in md5_map:
            digest = file_md5(path)
            ok = digest == md5_map[path.name]
            all_ok &= ok
            print(f"  md5: {digest} {'OK' if ok else 'MISMATCH, expected ' + md5_map[path.name]}")

        r = validate_file(path, every_millionth)
        print(f"  blocks: {r.n_blocks}")
        print(f"  index range: [{r.n_first:,}, {r.n_last:,}]  ({r.n_last - r.n_first + 1:,} zeros)")
        print(f"  height range: [{r.t_first!r}, {r.t_last!r})")
        print(f"  gamma_first = {decimal_str(r.gamma_first, 20)}")
        print(f"  gamma_last  = {decimal_str(r.gamma_last, 20)}")
        print(f"  strictly increasing: {r.strictly_increasing} (bad deltas: {r.bad_deltas})")
        print(f"  block chaining ok: {r.chaining_ok}")
        print(f"  index count ok (sum of block sizes == n_last - n_first + 1): {r.index_count_ok}")
        if r.trailing_bytes:
            print(f"  NOTE: {r.trailing_bytes} trailing bytes past the declared blocks "
                  "(the known upstream quirk, see module docstring)")
        print(f"  density ratio (observed / Riemann-von Mangoldt): {r.density_ratio:.6f}")
        if r.n_checked:
            print(f"  every_millionth cross-check: {r.n_matched}/{r.n_checked} matched")
            for n, ours, expected in r.mismatches:
                print(f"    MISMATCH n={n}: ours={ours} expected={expected}")
        else:
            print("  every_millionth cross-check: no indices in range")

        all_ok &= r.strictly_increasing and r.index_count_ok
        all_ok &= r.n_checked == 0 or r.n_matched == r.n_checked

    print("ALL OK" if all_ok else "VALIDATION FAILED")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
