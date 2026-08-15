"""Segmented-sieve streaming engine for the primes thread (e5a-e5f).

Streams every prime up to N with O(segment) memory, accumulating in one pass
every statistic the digit, constellation and gap experiments need:

- last-digit counts per base (equidistribution among the phi(b) unit digits)
- consecutive-prime last-digit transition matrices per base, per-decade for
  bases 3 and 10, plus the base-10 transition TENSOR over digit triples
  (the Lemke Oliver-Soundararajan bias and its slow decay, to second order)
- the Chebyshev races mod 4 and mod 3, with first sign change, extremes and
  where they occur, and a log-spaced sampled lead curve
- Hardy-Littlewood constellations: (p,p+2), (p,p+4), (p,p+6), the two prime
  triplets (0,2,6) and (0,4,6), and the quadruplet (0,2,6,8), per decade
- the consecutive-gap histogram per decade, and the joint distribution of
  ADJACENT gap pairs (g_n, g_{n+1}): does one gap predict the next
- the slow sums: sum 1/p per decade (Mertens) and the Brun partial sum

Constellation membership is read straight off the sieve bitmap: each segment
is sieved with a MAXOFF overhang, so p + off is always inside the current
segment's array and no cross-segment carry is needed. Every accumulator is
segment-size invariant by construction; test_primes.py checks that against
two different segment sizes.

Scale on the research box: N = 10^8 in ~2 s, N = 10^11 in ~45 min,
N = 10^12 overnight. Checkpoints land every 20 segments, so a partial run
is still readable.
"""
from __future__ import annotations

import sys
import time
from math import gcd, isqrt, log10
from pathlib import Path

import numpy as np

CACHE_DIR = Path(__file__).resolve().parent / "_cache"
CACHE_VERSION = "v3"

BASES = (3, 4, 10, 12, 30)          # base 2 is degenerate: every odd prime ends in 1
DECADE_TRANS_BASES = (3, 10)        # per-decade transition matrices kept for these
TRIPLE_BASE = 10                    # digit-triple tensor kept for this base

# Admissible patterns. Membership of p + off is a bitmap lookup, so the whole
# family costs four gathers per segment (one per distinct offset).
CONSTELLATIONS = {
    "twin":        (0, 2),
    "cousin":      (0, 4),
    "sexy":        (0, 6),
    "triplet_026": (0, 2, 6),
    "triplet_046": (0, 4, 6),
    "quad":        (0, 2, 6, 8),
}
OFFSETS = (2, 4, 6, 8)
MAXOFF = 8

RACE_MODULI = (3, 4, 8, 12)         # per-class counts sampled across x (multi-way races)
GAP_HIST = 1024                     # consecutive-gap histogram bins (top bin = overflow)
GP = 32                             # adjacent-gap joint histogram, indexed by g//2
SEGMENT = 5 * 10**8
RACE_SAMPLES = 4000
NDEC = 14                           # decades [10^k, 10^{k+1}) for k = 0..13
DECADE_EDGES = 10 ** np.arange(1, NDEC + 1, dtype=np.int64)

GAPS = (2, 4, 6)                    # legacy aliases written as pair{d}_dec
_ALIAS = {2: "twin", 4: "cousin", 6: "sexy"}


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


def stream(N: int, segment: int = SEGMENT, log=None, cache_tag: str = "") -> dict:
    """Run (or load) the one-pass accumulation up to N. Returns a dict of arrays."""
    cache = CACHE_DIR / f"stream_{N}{cache_tag}_{CACHE_VERSION}.npz"
    if cache.exists():
        return dict(np.load(cache))
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    say = log or (lambda *_: None)

    bps = flat_primes(isqrt(N + MAXOFF) + 1)
    luts = {b: _digit_lut(b) for b in BASES}
    nb = {b: len(units(b)) for b in BASES}
    ntb = nb[TRIPLE_BASE]

    acc = {
        "pi_dec": np.zeros(NDEC, dtype=np.int64),
        "recip_dec": np.zeros(NDEC, dtype=np.float64),
        "gap_hist_dec": np.zeros((NDEC, GAP_HIST), dtype=np.int64),
        "gap_joint": np.zeros((GP, GP), dtype=np.int64),
        f"tri_b{TRIPLE_BASE}": np.zeros((ntb, ntb, ntb), dtype=np.int64),
    }
    for b in BASES:
        acc[f"counts_b{b}"] = np.zeros(nb[b], dtype=np.int64)
        acc[f"trans_b{b}"] = np.zeros((nb[b], nb[b]), dtype=np.int64)
    for b in DECADE_TRANS_BASES:
        acc[f"transdec_b{b}"] = np.zeros((NDEC, nb[b], nb[b]), dtype=np.int64)
    for name in CONSTELLATIONS:
        acc[f"cons_{name}_dec"] = np.zeros(NDEC, dtype=np.int64)

    prev_idx = {b: -1 for b in BASES}      # previous prime's unit index, per base
    prev_dec = {b: -1 for b in BASES}
    prev_tri = np.empty(0, dtype=np.int64)  # up to 2 trailing base-10 digit indices
    prev_last = -1                          # last prime seen (boundary gap)
    prev_gap = -1                           # gap ending at prev_last (boundary gap pair)
    brun_partial = 0.0

    # Every maximal stretch where a race lead is negative, as
    # (x_first, x_last, min_lead, x_of_min). The sampled lead curve is too
    # coarse to catch these (they can be narrower than the sample spacing),
    # and first_cross/min_lead alone record only the earliest and the deepest.
    # Added after the v3 caches were built, so older .npz files lack it;
    # consumers should treat it as optional.
    neg_runs = {name: [] for name in ("race4", "race3")}
    neg_open = {name: None for name in ("race4", "race3")}

    thresholds = np.unique(np.round(np.logspace(2, log10(N), RACE_SAMPLES))).astype(np.int64)
    ap_lut = {q: _digit_lut(q) for q in RACE_MODULI}
    ap_samp = {q: np.zeros((len(thresholds), len(units(q))), dtype=np.int64)
               for q in RACE_MODULI}
    ap_cum = {q: np.zeros(len(units(q)), dtype=np.int64) for q in RACE_MODULI}
    ap_done = 0
    race = {}
    for name, mod in (("race4", 4), ("race3", 3)):
        race[name] = dict(
            mod=mod, carry=0, first_cross=0, min_lead=0, max_lead=0,
            min_lead_x=0, max_lead_x=0, n_pos=0, n_neg=0, n_zero=0,
            sample_lead=np.zeros(len(thresholds), dtype=np.int64), sample_done=0,
        )

    t0 = time.time()
    n_segments = (N + segment) // segment
    for si in range(n_segments):
        lo = si * segment
        hi = min(lo + segment, N + 1)
        if lo >= hi:
            break
        # Sieve [lo, hi + MAXOFF): the overhang makes p + off a local lookup.
        seg = np.ones(hi - lo + MAXOFF, dtype=bool)
        if lo == 0:
            seg[:2] = False
        top = hi + MAXOFF
        for p in bps:
            p = int(p)
            if p * p >= top:
                break
            start = max(p * p, ((lo + p - 1) // p) * p)
            seg[start - lo :: p] = False
        primes = np.flatnonzero(seg[: hi - lo]).astype(np.int64) + lo
        if primes.size == 0:
            del seg
            continue

        dec = _decades_of(primes)
        acc["pi_dec"] += np.bincount(dec, minlength=NDEC)
        acc["recip_dec"] += np.bincount(dec, weights=1.0 / primes, minlength=NDEC)

        # -- constellations: one gather per distinct offset, then boolean ANDs
        rel = primes - lo
        member = {off: seg[rel + off] for off in OFFSETS}
        for name, H in CONSTELLATIONS.items():
            ok = member[H[1]].copy()
            for off in H[2:]:
                ok &= member[off]
            ok &= primes <= N - H[-1]      # count tuples lying entirely below N
            if ok.any():
                p_ok = primes[ok]
                acc[f"cons_{name}_dec"] += np.bincount(_decades_of(p_ok), minlength=NDEC)
                if name == "twin":
                    brun_partial += float(np.sum(1.0 / p_ok + 1.0 / (p_ok + 2)))
        del seg, member

        # -- digit statistics per base ------------------------------------
        for b in BASES:
            mask = primes > b
            p_b = primes[mask] if not mask.all() else primes
            if p_b.size == 0:
                continue
            idx = luts[b][p_b % b]
            acc[f"counts_b{b}"] += np.bincount(idx, minlength=nb[b])
            d_b = dec[mask] if not mask.all() else dec
            if prev_idx[b] >= 0:
                idx_f = np.concatenate(([prev_idx[b]], idx))
                dec_f = np.concatenate(([prev_dec[b]], d_b))
            else:
                idx_f, dec_f = idx, d_b
            a, c = idx_f[:-1], idx_f[1:]
            acc[f"trans_b{b}"] += np.bincount(a * nb[b] + c,
                                              minlength=nb[b] ** 2).reshape(nb[b], nb[b])
            if b in DECADE_TRANS_BASES:
                flat = (dec_f[:-1] * nb[b] + a) * nb[b] + c
                acc[f"transdec_b{b}"] += np.bincount(
                    flat, minlength=NDEC * nb[b] ** 2).reshape(NDEC, nb[b], nb[b])
            if b == TRIPLE_BASE:
                full = np.concatenate((prev_tri, idx)) if prev_tri.size else idx
                if full.size >= 3:
                    tflat = (full[:-2] * ntb + full[1:-1]) * ntb + full[2:]
                    acc[f"tri_b{b}"] += np.bincount(
                        tflat, minlength=ntb ** 3).reshape(ntb, ntb, ntb)
                prev_tri = full[-2:].copy()
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
            hi_res = 2 if mod == 3 else 3
            step = np.where(res[keep] == hi_res, 1, -1).astype(np.int64)
            lead = r["carry"] + np.cumsum(step)
            lo_i, hi_i = int(np.argmin(lead)), int(np.argmax(lead))
            if r["first_cross"] == 0 and lead[lo_i] < 0:
                r["first_cross"] = int(p_r[int(np.argmax(lead < 0))])
            if int(lead[lo_i]) < r["min_lead"]:
                r["min_lead"], r["min_lead_x"] = int(lead[lo_i]), int(p_r[lo_i])
            if int(lead[hi_i]) > r["max_lead"]:
                r["max_lead"], r["max_lead_x"] = int(lead[hi_i]), int(p_r[hi_i])
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
            # -- catalogue the negative excursions, stitching across segments
            neg = lead < 0
            if neg.any():
                idx = np.flatnonzero(neg)
                brk = np.flatnonzero(np.diff(idx) > 1)
                starts = np.concatenate(([idx[0]], idx[brk + 1]))
                ends = np.concatenate((idx[brk], [idx[-1]]))
                for s_i, e_i in zip(starts, ends):
                    seg_lead = lead[s_i : e_i + 1]
                    j = int(np.argmin(seg_lead))
                    run = [int(p_r[s_i]), int(p_r[e_i]),
                           int(seg_lead[j]), int(p_r[s_i + j])]
                    if s_i == 0 and neg_open[name] is not None:
                        prev = neg_open[name]          # continues from last segment
                        prev[1] = run[1]
                        if run[2] < prev[2]:
                            prev[2], prev[3] = run[2], run[3]
                    else:
                        if neg_open[name] is not None:
                            neg_runs[name].append(neg_open[name])
                        neg_open[name] = run
                if not neg[-1]:
                    neg_runs[name].append(neg_open[name])
                    neg_open[name] = None
            elif neg_open[name] is not None:
                neg_runs[name].append(neg_open[name])
                neg_open[name] = None

            r["carry"] = int(lead[-1])

        # -- pi(x; q, a) sampled on the shared log-spaced grid -------------
        j1 = ap_done + int(np.searchsorted(thresholds[ap_done:], hi))
        thr = thresholds[ap_done:j1]
        for q in RACE_MODULI:
            idx_q = ap_lut[q][primes % q]
            for c in range(ap_samp[q].shape[1]):
                pc = primes[idx_q == c]
                if thr.size:
                    ap_samp[q][ap_done:j1, c] = ap_cum[q][c] + np.searchsorted(
                        pc, thr, side="right")
                ap_cum[q][c] += pc.size
        ap_done = j1

        # -- consecutive gaps, and the joint law of adjacent gaps ----------
        smaller = primes[:-1]
        g = np.clip(np.diff(primes), 0, GAP_HIST - 1)
        if prev_last > 0:
            smaller = np.concatenate(([prev_last], smaller))
            g = np.concatenate(([min(int(primes[0]) - prev_last, GAP_HIST - 1)], g))
        if smaller.size:
            flat = _decades_of(smaller) * GAP_HIST + g
            acc["gap_hist_dec"] += np.bincount(
                flat, minlength=NDEC * GAP_HIST).reshape(NDEC, GAP_HIST)
        gg = np.concatenate(([prev_gap], g)) if prev_gap > 0 else g
        if gg.size >= 2:
            a = np.clip(gg[:-1] // 2, 0, GP - 1)
            c = np.clip(gg[1:] // 2, 0, GP - 1)
            acc["gap_joint"] += np.bincount(a * GP + c, minlength=GP * GP).reshape(GP, GP)
        if g.size:
            prev_gap = int(g[-1])
        prev_last = int(primes[-1])

        if log and (si % 10 == 9 or si == n_segments - 1):
            say(f"  segment {si+1}/{n_segments}  x <= {hi-1:.3e}  "
                f"pi = {int(acc['pi_dec'].sum())}  ({time.time()-t0:.0f}s)")
        if si % 20 == 19 and si != n_segments - 1:
            _save(cache.with_suffix(".part.npz"), hi - 1, dict(acc, **{
                f"ap{q}_samp": ap_samp[q] for q in RACE_MODULI}),
                brun_partial, thresholds, race, time.time() - t0)

    # A trailing segment with no primes leaves its thresholds unconsumed; the
    # lead there is exactly the final carry, so flush rather than leave zeros.
    for r in race.values():
        r["sample_lead"][r["sample_done"]:] = r["carry"]
        r["sample_done"] = len(thresholds)
    for q in RACE_MODULI:
        ap_samp[q][ap_done:, :] = ap_cum[q]
        acc[f"ap{q}_samp"] = ap_samp[q]
    for name in neg_runs:
        runs = neg_runs[name] + ([neg_open[name]] if neg_open[name] else [])
        acc[f"{name}_neg_runs"] = (np.asarray(runs, dtype=np.int64) if runs
                                   else np.zeros((0, 4), dtype=np.int64))

    _save(cache, N, acc, brun_partial, thresholds, race, time.time() - t0)
    cache.with_suffix(".part.npz").unlink(missing_ok=True)
    return dict(np.load(cache))


def _save(path, N, acc, brun_partial, thresholds, race, elapsed):
    out = dict(acc)
    out["N"] = np.int64(N)
    out["elapsed"] = np.float64(elapsed)
    out["brun_partial"] = np.float64(brun_partial)
    out["race_thresholds"] = thresholds
    for d, name in _ALIAS.items():
        out[f"pair{d}_dec"] = acc[f"cons_{name}_dec"]
    for name, r in race.items():
        for k in ("first_cross", "min_lead", "max_lead", "min_lead_x", "max_lead_x",
                  "n_pos", "n_neg", "n_zero"):
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
    seg = int(float(sys.argv[2])) if len(sys.argv) > 2 else SEGMENT
    print(f"streaming primes to N = {N:.2e} (segment {seg:.1e})")
    res = stream(N, segment=seg, log=print)
    print(f"pi({N:.0e}) = {int(res['pi_dec'].sum())}   elapsed {float(res['elapsed']):.1f}s")
