"""GPU variant of the segmented-sieve streaming engine.

Same algorithm and the same output dict as primestream.stream(); the CPU
version stays the reference implementation and is untouched. This module
exists because a 10^13 pass is ~4.4 days on the CPU, of which roughly half
is the sieve marking itself.

WHERE THE SPEED COMES FROM. Marking is a scatter of ~1.5e9 byte-writes per
5e8 segment. On the CPU that runs at about 58M integers/s, far below memory
bandwidth, because for primes larger than a cache line every write pulls a
fresh 64-byte line to store one byte. A GPU hides that latency across
thousands of threads. One batched kernel marks every multiple of every base
prime in a segment (thread -> (prime, multiple) by binary search over a
prefix-sum of counts), measured at 14.4x the CPU loop and bit-identical.
The remaining per-segment work is ordinary array reductions, which move to
the GPU too; only the race bookkeeping, which is inherently sequential,
comes back to the host, and that costs about 0.02 s a segment.

CORRECTNESS. This is a performance variant of code whose exact counts are
the whole point, so it is not trusted, it is checked: test_primes.py runs
both engines and requires every integer accumulator to be bit-identical and
every float accumulator to agree to 1e-12 (float sums differ in their last
bits because the GPU reduces in a different order).

Usage:
    from experiments.primes.primestream_gpu import stream_gpu, gpu_available
    res = stream_gpu(10**12)          # same dict as primestream.stream
"""
from __future__ import annotations

import sys
import time
from math import isqrt, log10
from pathlib import Path

import numpy as np

from experiments.primes.primestream import (
    BASES, CACHE_DIR, CONSTELLATIONS, DECADE_EDGES, DECADE_TRANS_BASES, GAP_HIST,
    GP, MAXOFF, NDEC, OFFSETS, RACE_MODULI, RACE_SAMPLES, SEGMENT, TRIPLE_BASE,
    _ALIAS, _digit_lut, _save, flat_primes, units,
)

_MARK_KERNEL = r'''
extern "C" __global__
void mark(bool* seg, const long long* p, const long long* start,
          const long long* cnt, const long long* off,
          long long nprimes, long long lo, long long total) {
  long long gid = blockDim.x * (long long)blockIdx.x + threadIdx.x;
  if (gid >= total) return;
  long long a = 0, b = nprimes - 1, i = 0;      // which prime owns this thread
  while (a <= b) {
    long long m = (a + b) / 2;
    if (off[m] <= gid) { i = m; a = m + 1; } else { b = m - 1; }
  }
  long long k = gid - off[i];
  if (k < cnt[i]) seg[start[i] - lo + k * p[i]] = false;
}
'''


def gpu_available() -> bool:
    try:
        import cupy as cp
        cp.cuda.runtime.getDeviceCount()
        return True
    except Exception:
        return False


def stream_gpu(N: int, segment: int = SEGMENT, log=None, cache_tag: str = "") -> dict:
    """GPU port of primestream.stream. Identical output, identical cache names."""
    import cupy as cp

    cache = CACHE_DIR / f"stream_{N}{cache_tag}_v3.npz"
    if cache.exists():
        return dict(np.load(cache))
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    say = log or (lambda *_: None)
    kern = cp.RawKernel(_MARK_KERNEL, "mark")

    bps = flat_primes(isqrt(N + MAXOFF) + 1)
    bps_g = cp.asarray(bps)
    edges = cp.asarray(DECADE_EDGES)
    luts = {b: cp.asarray(_digit_lut(b)) for b in BASES}
    nb = {b: len(units(b)) for b in BASES}
    ntb = nb[TRIPLE_BASE]

    def decades(v):
        return cp.searchsorted(edges, v, side="right")

    acc = {
        "pi_dec": cp.zeros(NDEC, dtype=cp.int64),
        "recip_dec": cp.zeros(NDEC, dtype=cp.float64),
        "gap_hist_dec": cp.zeros((NDEC, GAP_HIST), dtype=cp.int64),
        "gap_joint": cp.zeros((GP, GP), dtype=cp.int64),
        f"tri_b{TRIPLE_BASE}": cp.zeros((ntb, ntb, ntb), dtype=cp.int64),
    }
    for b in BASES:
        acc[f"counts_b{b}"] = cp.zeros(nb[b], dtype=cp.int64)
        acc[f"trans_b{b}"] = cp.zeros((nb[b], nb[b]), dtype=cp.int64)
    for b in DECADE_TRANS_BASES:
        acc[f"transdec_b{b}"] = cp.zeros((NDEC, nb[b], nb[b]), dtype=cp.int64)
    for name in CONSTELLATIONS:
        acc[f"cons_{name}_dec"] = cp.zeros(NDEC, dtype=cp.int64)

    prev_idx = {b: -1 for b in BASES}
    prev_dec = {b: -1 for b in BASES}
    prev_tri = cp.empty(0, dtype=cp.int64)
    prev_last = -1
    prev_gap = -1
    brun_partial = 0.0
    neg_runs = {n: [] for n in ("race4", "race3")}
    neg_open = {n: None for n in ("race4", "race3")}

    thresholds = np.unique(np.round(np.logspace(2, log10(N), RACE_SAMPLES))).astype(np.int64)
    thr_g = cp.asarray(thresholds)
    ap_lut = {q: cp.asarray(_digit_lut(q)) for q in RACE_MODULI}
    ap_samp = {q: cp.zeros((len(thresholds), len(units(q))), dtype=cp.int64)
               for q in RACE_MODULI}
    ap_cum = {q: cp.zeros(len(units(q)), dtype=cp.int64) for q in RACE_MODULI}
    ap_done = 0
    race = {}
    for name, mod in (("race4", 4), ("race3", 3)):
        race[name] = dict(mod=mod, carry=0, first_cross=0, min_lead=0, max_lead=0,
                          min_lead_x=0, max_lead_x=0, n_pos=0, n_neg=0, n_zero=0,
                          sample_lead=np.zeros(len(thresholds), dtype=np.int64),
                          sample_done=0)

    t0 = time.time()
    n_segments = (N + segment) // segment
    for si in range(n_segments):
        lo = si * segment
        hi = min(lo + segment, N + 1)
        if lo >= hi:
            break
        size = hi - lo + MAXOFF
        top = hi + MAXOFF
        seg = cp.ones(size, dtype=cp.bool_)
        if lo == 0:
            seg[:2] = False

        pp = bps[bps * bps < top].astype(np.int64)
        if pp.size:
            start = np.maximum(pp * pp, ((lo + pp - 1) // pp) * pp)
            cnt = np.maximum((top - start + pp - 1) // pp, 0)
            off = np.concatenate(([0], np.cumsum(cnt)))[:-1]
            total = int(cnt.sum())
            if total:
                threads = 256
                blocks = (total + threads - 1) // threads
                kern((blocks,), (threads,),
                     (seg, cp.asarray(pp), cp.asarray(start), cp.asarray(cnt),
                      cp.asarray(off), np.int64(pp.size), np.int64(lo),
                      np.int64(total)))

        primes = cp.flatnonzero(seg[: hi - lo]).astype(cp.int64) + lo
        if primes.size == 0:
            del seg
            continue

        dec = decades(primes)
        acc["pi_dec"] += cp.bincount(dec, minlength=NDEC)
        acc["recip_dec"] += cp.bincount(dec, weights=1.0 / primes, minlength=NDEC)

        rel = primes - lo
        member = {o: seg[rel + o] for o in OFFSETS}
        for name, H in CONSTELLATIONS.items():
            ok = member[H[1]].copy()
            for o in H[2:]:
                ok &= member[o]
            ok &= primes <= N - H[-1]
            if bool(ok.any()):
                p_ok = primes[ok]
                acc[f"cons_{name}_dec"] += cp.bincount(decades(p_ok), minlength=NDEC)
                if name == "twin":
                    brun_partial += float(cp.sum(1.0 / p_ok + 1.0 / (p_ok + 2)))
        del seg, member

        for b in BASES:
            mask = primes > b
            all_ok = bool(mask.all())
            p_b = primes if all_ok else primes[mask]
            if p_b.size == 0:
                continue
            idx = luts[b][p_b % b]
            acc[f"counts_b{b}"] += cp.bincount(idx, minlength=nb[b])
            d_b = dec if all_ok else dec[mask]
            if prev_idx[b] >= 0:
                idx_f = cp.concatenate((cp.asarray([prev_idx[b]], dtype=cp.int64), idx))
                dec_f = cp.concatenate((cp.asarray([prev_dec[b]], dtype=cp.int64), d_b))
            else:
                idx_f, dec_f = idx, d_b
            a, c = idx_f[:-1], idx_f[1:]
            acc[f"trans_b{b}"] += cp.bincount(
                a * nb[b] + c, minlength=nb[b] ** 2).reshape(nb[b], nb[b])
            if b in DECADE_TRANS_BASES:
                flat = (dec_f[:-1] * nb[b] + a) * nb[b] + c
                acc[f"transdec_b{b}"] += cp.bincount(
                    flat, minlength=NDEC * nb[b] ** 2).reshape(NDEC, nb[b], nb[b])
            if b == TRIPLE_BASE:
                full = cp.concatenate((prev_tri, idx)) if prev_tri.size else idx
                if full.size >= 3:
                    tflat = (full[:-2] * ntb + full[1:-1]) * ntb + full[2:]
                    acc[f"tri_b{b}"] += cp.bincount(
                        tflat, minlength=ntb ** 3).reshape(ntb, ntb, ntb)
                prev_tri = full[-2:].copy()
            prev_idx[b] = int(idx[-1])
            prev_dec[b] = int(d_b[-1])

        # -- races: vectorized on the GPU, sequential bookkeeping on the host
        for name in ("race4", "race3"):
            r = race[name]
            mod = r["mod"]
            resid = primes % mod
            keep = resid != 0 if mod == 3 else (resid == 1) | (resid == 3)
            p_r_g = primes[keep]
            if p_r_g.size == 0:
                continue
            hi_res = 2 if mod == 3 else 3
            step = cp.where(resid[keep] == hi_res, 1, -1).astype(cp.int64)
            lead_g = r["carry"] + cp.cumsum(step)
            lead = cp.asnumpy(lead_g)
            p_r = cp.asnumpy(p_r_g)

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

            neg = lead < 0
            if neg.any():
                idx_n = np.flatnonzero(neg)
                brk = np.flatnonzero(np.diff(idx_n) > 1)
                starts = np.concatenate(([idx_n[0]], idx_n[brk + 1]))
                ends = np.concatenate((idx_n[brk], [idx_n[-1]]))
                for s_i, e_i in zip(starts, ends):
                    seg_lead = lead[s_i : e_i + 1]
                    j = int(np.argmin(seg_lead))
                    run = [int(p_r[s_i]), int(p_r[e_i]), int(seg_lead[j]),
                           int(p_r[s_i + j])]
                    if s_i == 0 and neg_open[name] is not None:
                        prev = neg_open[name]
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

        # -- pi(x; q, a) on the shared log-spaced grid
        j1 = ap_done + int(np.searchsorted(thresholds[ap_done:], hi))
        thr = thr_g[ap_done:j1]
        for q in RACE_MODULI:
            idx_q = ap_lut[q][primes % q]
            for c in range(ap_samp[q].shape[1]):
                pc = primes[idx_q == c]
                if thr.size:
                    ap_samp[q][ap_done:j1, c] = ap_cum[q][c] + cp.searchsorted(
                        pc, thr, side="right")
                ap_cum[q][c] += pc.size
        ap_done = j1

        smaller = primes[:-1]
        g = cp.clip(cp.diff(primes), 0, GAP_HIST - 1)
        if prev_last > 0:
            smaller = cp.concatenate((cp.asarray([prev_last], dtype=cp.int64), smaller))
            g = cp.concatenate((cp.asarray(
                [min(int(primes[0]) - prev_last, GAP_HIST - 1)], dtype=cp.int64), g))
        if smaller.size:
            flat = decades(smaller) * GAP_HIST + g
            acc["gap_hist_dec"] += cp.bincount(
                flat, minlength=NDEC * GAP_HIST).reshape(NDEC, GAP_HIST)
        gg = cp.concatenate((cp.asarray([prev_gap], dtype=cp.int64), g)) if prev_gap > 0 else g
        if gg.size >= 2:
            a = cp.clip(gg[:-1] // 2, 0, GP - 1)
            c = cp.clip(gg[1:] // 2, 0, GP - 1)
            acc["gap_joint"] += cp.bincount(a * GP + c, minlength=GP * GP).reshape(GP, GP)
        if g.size:
            prev_gap = int(g[-1])
        prev_last = int(primes[-1])

        if log and (si % 10 == 9 or si == n_segments - 1):
            say(f"  segment {si+1}/{n_segments}  x <= {hi-1:.3e}  "
                f"pi = {int(acc['pi_dec'].sum())}  ({time.time()-t0:.0f}s)")
        if si % 20 == 19 and si != n_segments - 1:
            _save(cache.with_suffix(".part.npz"), hi - 1,
                  _to_host(acc, ap_samp, neg_runs, neg_open),
                  brun_partial, thresholds, race, time.time() - t0)

    for r in race.values():
        r["sample_lead"][r["sample_done"]:] = r["carry"]
        r["sample_done"] = len(thresholds)
    for q in RACE_MODULI:
        ap_samp[q][ap_done:, :] = ap_cum[q]   # thresholds past the last prime

    _save(cache, N, _to_host(acc, ap_samp, neg_runs, neg_open),
          brun_partial, thresholds, race, time.time() - t0)
    cache.with_suffix(".part.npz").unlink(missing_ok=True)
    return dict(np.load(cache))


def _to_host(acc, ap_samp, neg_runs, neg_open) -> dict:
    import cupy as cp

    out = {k: cp.asnumpy(v) for k, v in acc.items()}
    for q, v in ap_samp.items():
        out[f"ap{q}_samp"] = cp.asnumpy(v)
    for name in neg_runs:
        runs = neg_runs[name] + ([neg_open[name]] if neg_open[name] else [])
        out[f"{name}_neg_runs"] = (np.asarray(runs, dtype=np.int64) if runs
                                   else np.zeros((0, 4), dtype=np.int64))
    return out


if __name__ == "__main__":
    N = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**8
    seg = int(float(sys.argv[2])) if len(sys.argv) > 2 else SEGMENT
    if not gpu_available():
        raise SystemExit("no CUDA device available")
    print(f"streaming primes to N = {N:.2e} on the GPU (segment {seg:.1e})")
    res = stream_gpu(N, segment=seg, log=print)
    print(f"pi({N:.0e}) = {int(res['pi_dec'].sum())}   "
          f"elapsed {float(res['elapsed']):.1f}s")
