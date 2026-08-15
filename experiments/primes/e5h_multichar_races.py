"""E5H: races mod 8 and mod 12, where several characters share the work.

E5G predicted the mod-3 and mod-4 races from L-function zeros. Those are the
easy cases: one non-principal character each, so one set of zeros drives
everything. Mod 8 and mod 12 have THREE non-principal characters apiece, and
the race between two classes hears a different combination of them depending
on which classes are racing. That makes this a real generalization rather
than a rerun, and it predicts things the single-character case cannot, such
as races with no bias at all.

THE FORMULA. For a race between classes a and b mod q,

    psi(x;q,a) - psi(x;q,b) = (1/phi(q)) sum_{chi != chi0} (chi(a)-chi(b)) psi(x,chi)

and psi(x,chi) = -sum_rho x^rho/rho over the zeros of L(s,chi). Prime squares
land in the class of squares, contributing the systematic bias. Undoing that
and passing to pi leaves, under GRH,

    E(x) := (log x / sqrt x) [pi(x;q,a) - pi(x;q,b)]
          = [nu(b) - nu(a)]/phi(q)
            + (1/phi(q)) sum_{chi != chi0} (chi(b) - chi(a)) osc_chi(x),

    osc_chi(x) = 2 sum_{gamma_chi > 0} Re[ x^{i gamma} / (1/2 + i gamma) ],

where nu(s) counts the square roots of s in (Z/q)*. For q = 8 and 12 every
unit squares to 1, so nu(1) = phi(q) and nu = 0 elsewhere: a race against
class 1 carries bias exactly 1, and a race between two non-square classes
carries NO bias. Those unbiased races are the interesting prediction, since
they should sit around zero and change sign constantly rather than favouring
anyone (Rubinstein-Sarnak: density 1/2).

IMPRIMITIVE CHARACTERS. Some characters mod q are induced from a smaller
conductor (mod 8 borrows one from mod 4; mod 12 borrows from both mod 3 and
mod 4). L(s,chi) then differs from L(s,chi*) only by finitely many Euler
factors, which move psi by O(log^2 x), far below anything here. So the zeros
of the primitive inducing character are used, which is also the only option:
Oliveira e Silva tabulated 10,000 zeros for primitive characters and just 10
for the rest.
"""
from __future__ import annotations

import gzip
import re
import sys
from math import gcd
from pathlib import Path

import numpy as np

from experiments.primes.primestream import CACHE_DIR, stream, units
from experiments.primes.e5g_race_from_zeros import E_predicted, excursions, tail_rms

TOS = CACHE_DIR / "datasets" / "tos" / "zeta"


def _parse(path: Path) -> tuple[int, dict[int, int], np.ndarray]:
    """(modulus, chi on the units, zero ordinates) from a TOS zeros file."""
    mod, listed, vals = None, {}, []
    with gzip.open(path, "rt") as f:
        for line in f:
            s = line.strip()
            if s.startswith("#"):
                m = re.search(r"character modulus:\s*(\d+)", s)
                if m:
                    mod = int(m.group(1))
                m = re.match(r"#\s*(\d+)\s+(-?\d+(?:/\d+)?)$", s)
                if m:                       # log(chi(n))/(2 pi i), a rational
                    num = m.group(2)
                    v = eval(num) if "/" in num else float(num)   # 0 or 1/2 here
                    listed[int(m.group(1))] = 1 if v == 0 else -1
            elif s:
                vals.append(float(s))
    u = units(mod)
    chi = {k: v for k, v in listed.items() if k in u}
    for _ in range(4):                      # extend multiplicatively
        for a in u:
            for b in u:
                if a in chi and b in chi and (a * b) % mod not in chi:
                    chi[(a * b) % mod] = chi[a] * chi[b]
    return mod, chi, np.asarray(vals)


_REG: list | None = None
_CHARS: dict[int, list] = {}


def registry() -> list[tuple[int, dict[int, int], np.ndarray, Path]]:
    """All TOS character files, parsed once (each parse walks 10,000-line gzips)."""
    global _REG
    if _REG is not None:
        return _REG
    if not TOS.exists():
        raise FileNotFoundError(f"{TOS} missing; see experiments/primes/DATASETS.md")
    out = []
    for p in sorted(TOS.glob("zeros_*.txt.gz")):
        mod, chi, vals = _parse(p)
        if mod:
            out.append((mod, chi, vals, p))
    _REG = out
    return out


def characters_for(q: int) -> list[tuple[dict[int, int], np.ndarray, str]]:
    """Non-principal characters mod q, each with the best zero list available.

    An imprimitive character mod q is matched to the primitive one that
    induces it, by agreeing on every unit mod q after lifting.
    """
    if q in _CHARS:
        return _CHARS[q]
    reg = registry()
    u = units(q)
    out = []
    for mod, chi, vals, p in reg:
        if mod != q or all(chi[x] == 1 for x in u):
            continue                                    # not mod q, or principal
        best, best_name = vals, p.name
        if vals.size < 100:                             # imprimitive: borrow zeros
            for m2, chi2, v2, p2 in reg:
                if m2 in (1, q) or q % m2 or v2.size < 100:
                    continue                            # must be a proper divisor
                if all(chi2.get(x % m2) == chi[x] for x in u):
                    best, best_name = v2, p2.name
                    break
        out.append((chi, best, best_name))
    _CHARS[q] = out
    return out


def nu(q: int, s: int) -> int:
    """Number of square roots of s in (Z/q)*."""
    return sum(1 for x in units(q) if (x * x) % q == s % q)


def E_race(logx: np.ndarray, q: int, a: int, b: int) -> tuple[np.ndarray, float]:
    """Predicted E(x) for the race of class a against class b, and its bias."""
    phi = len(units(q))
    bias = (nu(q, b) - nu(q, a)) / phi
    total = np.full(logx.size, bias, dtype=np.float64)
    for chi, gammas, _ in characters_for(q):
        w = (chi[b % q] - chi[a % q]) / phi
        if w:
            total += w * (E_predicted(logx, gammas) - 1.0)   # strip E_predicted's own bias
    return total, bias


def E_measured(q: int, a: int, b: int, res: dict) -> tuple[np.ndarray, np.ndarray]:
    """Measured E(x) from our own stream's pi(x; q, class) samples."""
    u = units(q)
    samp = res[f"ap{q}_samp"]
    x = res["race_thresholds"][: samp.shape[0]].astype(float)
    ca, cb = samp[:, u.index(a)].astype(float), samp[:, u.index(b)].astype(float)
    keep = x > 1e4
    x = x[keep]
    return x, (ca - cb)[keep] * np.log(x) / np.sqrt(x)


def biggest_stream() -> tuple[int, dict]:
    """The deepest prime pass already on disk.

    Never triggers a recomputation: a missing cache for a big N would silently
    start a multi-hour sieve, which is exactly the trap this avoids.
    """
    for n in (10**13, 10**12, 10**11, 10**10, 10**9, 10**8):
        for tag in ("", "_bench", "_benchgpu"):
            if (CACHE_DIR / f"stream_{n}{tag}_v3.npz").exists():
                return n, stream(n, cache_tag=tag)
    raise SystemExit("no prime-stream cache found; run e5a first")


def main(q: int = 8) -> None:
    print(f"E5H: predicting the mod-{q} races from L-function zeros")
    chars = characters_for(q)
    print(f"  non-principal characters: {len(chars)}")
    for chi, g, name in chars:
        print(f"    chi on {units(q)} = {[chi[x] for x in units(q)]}  "
              f"<- {name} ({g.size:,} zeros, first {g[0]:.4f})")

    N, res = biggest_stream()
    u = units(q)
    saved = {}
    print(f"\n[A] Every pairwise race, prediction vs our prime stream to {N:.0e}")
    print("    a  vs  b   bias   corr    mean E (meas / pred)   RMS diff")
    for i, a in enumerate(u):
        for b in u[i + 1 :]:
            x, Em = E_measured(q, a, b, res)
            Ep, bias = E_race(np.log(x), q, a, b)
            band = x > 1e5
            corr = float(np.corrcoef(Em[band], Ep[band])[0, 1])
            saved[f"pred_{a}_{b}"], saved[f"meas_{a}_{b}"] = Ep, Em
            print(f"    {a:>2}  vs {b:>2}   {bias:+.2f}  {corr:+.4f}   "
                  f"{Em[band].mean():+.4f} / {Ep[band].mean():+.4f}      "
                  f"{float(np.sqrt(np.mean((Em[band]-Ep[band])**2))):.4f}")

    print(f"\n[B] The unbiased races: no square-root bias, so no favourite")
    for i, a in enumerate(u):
        for b in u[i + 1 :]:
            if nu(q, a) != nu(q, b):
                continue
            x, Em = E_measured(q, a, b, res)
            band = x > 1e5
            flips = int(np.count_nonzero(np.diff(np.signbit(Em[band]))))
            print(f"    {a:>2} vs {b:>2}: measured lead changes sign {flips} times over "
                  f"{int(band.sum())} samples, mean E {Em[band].mean():+.4f}")
    print("    (a biased race flips rarely: mod-4's 3 vs 1 took until x = 26,861,")
    print("     and mod-3's 2 vs 1 until 6.09e11. With no bias there is nothing to")
    print("     overcome, so the lead should change hands constantly.)")

    np.savez_compressed(CACHE_DIR / f"e5h_race{q}.npz", **saved)
    print(f"\nsaved to {CACHE_DIR / f'e5h_race{q}.npz'}")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 8)
