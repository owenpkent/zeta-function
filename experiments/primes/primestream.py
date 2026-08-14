"""Segmented-sieve streaming engine for the primes thread (e5a/e5b).

Streams every prime up to N with O(segment) memory, accumulating in one pass
all the statistics the digit-pattern and gap experiments need:

- last-digit counts per base (equidistribution among the phi(b) unit digits)
- consecutive-prime last-digit transition matrices per base, and for bases
  3 and 10 the per-decade breakdown (the Lemke Oliver-Soundararajan bias
  and its slow decay)
- the Chebyshev races mod 4 (pi(x;4,3) vs pi(x;4,1)) and mod 3, with first
  sign change, extremes, and a log-spaced sampled lead curve
- small even gaps d = 2, 4, 6 per decade (twins, cousins, sexy primes)
- the slow sums: sum 1/p per decade (Mertens) and the Brun partial sum

One pass serves both e5a and e5b. Results are cached per N as an .npz under
_cache/ so the analysis modules re-read without re-sieving. The engine is
numpy-only (the research box venv carries numpy + mpmath and nothing else).

Scale: N = 10^8 streams in seconds; N = 10^11 (4.1e9 primes) is an
hour-class background run on the always-on box. Checkpoints land every 20
segments so a partial run is still usable.
"""
from __future__ import annotations

import sys
import time
from math import gcd, isqrt, log10
from pathlib import Path

import numpy as np

CACHE_DIR = Path(__file__).resolve().parent / "_cache"

BASES = (3, 4, 10, 12, 30)          # base 2 is degenerate: every odd prime ends in 1
DECADE_TRANS_BASES = (3, 10)        # per-decade transition tensors kept for these
GAPS = (2, 4, 6)                    # twin, cousin, sexy
GAP_HIST = 1024                     # consecutive-gap histogram bins (top bin = overflow)
SEGMENT = 10**8
RACE_SAMPLES = 4000
NDEC = 12                           # decades [10^k, 10^{k+1}) for k = 0..11
DECADE_EDGES = 10 ** np.arange(1, NDEC + 1, dtype=np.int64)


def flat_primes(limit: int) -> np.ndarray:
    """All primes <= limit via a flat sieve. Fine up to ~10^9 on this box."""
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p :: p] = False
    return np.flatnonzero(sieve).astype(np.int64)


def units(b: int) -> list[int]:
    return [d for d in range(b) if gcd(d, b) == 1]


def _digit_lut(b: int) -> np.ndarray:
    """Map last digit -> unit index (or -1). Primes > b only hit units."""
    lut = np.full(b, -1, dtype=np.int64)
    for i, d in enumerate(units(b)):
        lut[d] = i
    return lut


def _decades_of(values: np.ndarray) -> np.ndarray:
    return np.searchsorted(DECADE_EDGES, values, side="right")


def stream(N: int, segment: int = SEGMENT, log=None) -> dict:
    """Run (or load) the one-pass accumulation up to N. Returns a dict of arrays."""
    cache = CACHE_DIR / f"stream_{N}_v2.npz"
    if cache.exists():
        return dict(np.load(cache))
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    say = log or (lambda *_: None)

    bps = flat_primes(isqrt(N))
    luts = {b: _digit_lut(b) for b in BASES}
    nb = {b: len(units(b)) for b in BASES}

    counts = {b: np.zeros(nb[b], dtype=np.int64) for b in BASES}
    trans = {b: np.zeros((nb[b], nb[b]), dtype=np.int64) for b in BASES}
    trans_dec = {b: np.zeros((NDEC, nb[b], nb[b]), dtype=np.int64) for b in DECADE_TRANS_BASES}
    prev_idx = {b: -1 for b in BASES}   # unit index of the previous prime (> b)
    prev_dec = {b: -1 for b in BASES}

    pair_dec = {d: np.zeros(NDEC, dtype=np.int64) for d in GAPS}
    gap_hist_dec = np.zeros((NDEC, GAP_HIST), dtype=np.int64)
    pi_dec = np.zeros(NDEC, dtype=np.int64)
    recip_dec = np.zeros(NDEC, dtype=np.float64)
    brun_partial = 0.0
    pair_carry = np.empty(0, dtype=np.int64)  # primes within 7 of the segment top
    prev_last = -1                            # last prime seen (boundary gap)

    thresholds = np.unique(np.round(np.logspace(2, log10(N), RACE_SAMPLES))).astype(np.int64)
    race = {}
    for name, mod in (("race4", 4), ("race3", 3)):
        race[name] = dict(
            mod=mod, carry=0, first_cross=0, min_lead=0, max_lead=0,
            n_pos=0, n_neg=0, n_zero=0,
            sample_lead=np.zeros(len(thresholds), dtype=np.int64), sample_done=0,
        )

    t0 = time.time()
    n_segments = (N + segment - 1) // segment
    for si in range(n_segments):
        lo = si * segment
        hi = min(lo + segment, N + 1)
        seg = np.ones(hi - lo, dtype=bool)
        if lo == 0:
            seg[:2] = False
        for p in bps:
            p = int(p)
            if p * p >= hi:
                break
            start = max(p * p, ((lo + p - 1) // p) * p)
            seg[start - lo :: p] = False
        primes = (np.flatnonzero(seg) + lo).astype(np.int64)
        del seg
        if primes.size == 0:
            continue

        dec = _decades_of(primes)
        pi_dec += np.bincount(dec, minlength=NDEC)
        recip_dec += np.bincount(dec, weights=1.0 / primes, minlength=NDEC)

        # -- digit statistics per base ------------------------------------
        for b in BASES:
            mask = primes > b
            p_b = primes[mask] if not mask.all() else primes
            if p_b.size == 0:
                continue
            idx = luts[b][p_b % b]
            counts[b] += np.bincount(idx, minlength=nb[b])
            d_b = dec[mask] if not mask.all() else dec
            if prev_idx[b] >= 0:
                idx_full = np.concatenate(([prev_idx[b]], idx))
                dec_full = np.concatenate(([prev_dec[b]], d_b))
            else:
                idx_full, dec_full = idx, d_b
            a, c = idx_full[:-1], idx_full[1:]
            trans[b] += np.bincount(a * nb[b] + c, minlength=nb[b] ** 2).reshape(nb[b], nb[b])
            if b in trans_dec:
                flat = (dec_full[:-1] * nb[b] + a) * nb[b] + c
                trans_dec[b] += np.bincount(flat, minlength=NDEC * nb[b] ** 2).reshape(
                    NDEC, nb[b], nb[b])
            prev_idx[b] = int(idx[-1])
            prev_dec[b] = int(d_b[-1])

        # -- Chebyshev races ----------------------------------------------
        for name in ("race4", "race3"):
            r = race[name]
            mod = r["mod"]
            res = primes % mod
            keep = res != 0 if mod == 3 else (res == 1) | (res == 3)
            p_r = primes[keep]
            if p_r.size == 0:
                continue
            # lead = #(nonresidue class) - #(residue class 1)
            hi_res = 2 if mod == 3 else 3
            step = np.where(res[keep] == hi_res, 1, -1).astype(np.int64)
            lead = r["carry"] + np.cumsum(step)
            if r["first_cross"] == 0 and lead.min() < 0:
                r["first_cross"] = int(p_r[int(np.argmax(lead < 0))])
            r["min_lead"] = min(r["min_lead"], int(lead.min()))
            r["max_lead"] = max(r["max_lead"], int(lead.max()))
            r["n_pos"] += int((lead > 0).sum())
            r["n_neg"] += int((lead < 0).sum())
            r["n_zero"] += int((lead == 0).sum())
            j0 = r["sample_done"]
            j1 = j0 + int(np.searchsorted(thresholds[j0:], hi))
            if j1 > j0:
                pos = np.searchsorted(p_r, thresholds[j0:j1], side="right")
                lead_full = np.concatenate(([r["carry"]], lead))
                r["sample_lead"][j0:j1] = lead_full[pos]
                r["sample_done"] = j1
            r["carry"] = int(lead[-1])

        # -- consecutive-gap histogram: within-segment pairs plus the single
        #    boundary pair, so every consecutive pair lands exactly once -----
        smaller = primes[:-1]
        g = np.clip(np.diff(primes), 0, GAP_HIST - 1)
        if prev_last > 0:
            smaller = np.concatenate(([prev_last], smaller))
            g = np.concatenate(([min(int(primes[0]) - prev_last, GAP_HIST - 1)], g))
        if smaller.size:
            flat = _decades_of(smaller) * GAP_HIST + g
            gap_hist_dec += np.bincount(flat, minlength=NDEC * GAP_HIST).reshape(
                NDEC, GAP_HIST)
        prev_last = int(primes[-1])

        # -- (p, p+d) pair counts, d = 2, 4, 6: BOTH members prime, p+d not
        #    necessarily the next prime (a sexy pair can bracket another
        #    prime). Attribution window [prev_hi-7, hi-7) makes each p count
        #    exactly once across segments; the carry supplies membership. ----
        P = np.concatenate((pair_carry, primes))
        attr = P if hi == N + 1 else P[P < hi - 7]
        for d in GAPS:
            q = attr + d
            pos = np.searchsorted(P, q)
            pos[pos >= P.size] = P.size - 1
            p_ok = attr[P[pos] == q]
            if p_ok.size:
                pair_dec[d] += np.bincount(_decades_of(p_ok), minlength=NDEC)
                if d == 2:
                    brun_partial += float(np.sum(1.0 / p_ok + 1.0 / (p_ok + d)))
        pair_carry = primes[primes >= hi - 7]

        if log and (si % 10 == 9 or si == n_segments - 1):
            done = hi - 1
            say(f"  segment {si+1}/{n_segments}  x <= {done:.2e}  "
                f"pi = {int(pi_dec.sum())}  ({time.time()-t0:.0f}s)")
        if si % 20 == 19 and si != n_segments - 1:
            _save(cache.with_suffix(".part.npz"), hi - 1, counts, trans, trans_dec,
                  pair_dec, gap_hist_dec, pi_dec, recip_dec, brun_partial,
                  thresholds, race, time.time() - t0)

    _save(cache, N, counts, trans, trans_dec, pair_dec, gap_hist_dec, pi_dec,
          recip_dec, brun_partial, thresholds, race, time.time() - t0)
    cache.with_suffix(".part.npz").unlink(missing_ok=True)
    return dict(np.load(cache))


def _save(path, N, counts, trans, trans_dec, pair_dec, gap_hist_dec, pi_dec,
          recip_dec, brun_partial, thresholds, race, elapsed):
    out = {
        "N": np.int64(N), "elapsed": np.float64(elapsed),
        "pi_dec": pi_dec, "recip_dec": recip_dec,
        "brun_partial": np.float64(brun_partial),
        "race_thresholds": thresholds,
        "gap_hist_dec": gap_hist_dec,
    }
    for b in BASES:
        out[f"counts_b{b}"] = counts[b]
        out[f"trans_b{b}"] = trans[b]
    for b in trans_dec:
        out[f"transdec_b{b}"] = trans_dec[b]
    for d in pair_dec:
        out[f"pair{d}_dec"] = pair_dec[d]
    for name, r in race.items():
        for k in ("first_cross", "min_lead", "max_lead", "n_pos", "n_neg", "n_zero"):
            out[f"{name}_{k}"] = np.int64(r[k])
        out[f"{name}_sample_lead"] = r["sample_lead"]
        out[f"{name}_sample_done"] = np.int64(r["sample_done"])
    tmp = path.with_name(path.name + ".tmp.npz")
    np.savez_compressed(tmp, **out)
    tmp.replace(path)


def load_or_stream(N: int, log=None) -> dict:
    return stream(N, log=log)


if __name__ == "__main__":
    N = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**8
    print(f"streaming primes to N = {N:.2e}")
    res = stream(N, log=print)
    print(f"pi({N:.0e}) = {int(res['pi_dec'].sum())}   elapsed {float(res['elapsed']):.1f}s")
