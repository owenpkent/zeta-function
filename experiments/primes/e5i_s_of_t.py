"""e5i: S(T), the argument of zeta on the critical line, measured in bulk.

WHY. S(T) = (1/pi) arg zeta(1/2 + iT) is the fluctuating term of the zero
count, N(T) = theta(T)/pi + 1 + S(T). It is the quantitative companion of
the hiding law from PRIME_PATTERNS: a counterexample pair of off-line zeros
at height T0 would force S to jump by 2 at T0 and hold that offset until the
partner heights, so the measured smallness of S across certified ranges IS
what "an off-line zero has nowhere to hide below these heights" means as a
number. This probe computes S at (and between) every zero of three certified
data regimes: the locally recomputed low range [0, 2e7] gated against the
e5f certified counts, and the three LMFDB/Platt rigorous windows at heights
3.7e8 / 3.3e9 / 3.06e10 (DATASETS.md section 18). Per window it reports
max |S| with location and the second moment of S against the Selberg/Ghosh
scale log log T / (2 pi^2).

PRE-REGISTRATION (recorded in e5i_s_of_t.md before the full run started):
max |S| < 3 in every window.

METHOD. At the n-th zero gamma_n (1-based), S jumps by +1 (all zeros in the
covered ranges are simple, per the certifications), so the one-sided values
are S(gamma_n^+) = n - theta(gamma_n)/pi - 1 and S(gamma_n^-) = S(gamma_n^+) - 1.
max |S| over a window is the max over both one-sided values. Between zeros
S(t) = n - theta(t)/pi - 1 exactly, so the time-averaged second moment
(1/L) int S^2 dt is computed per gap by Simpson (endpoints + midpoint), which
is essentially exact here because theta is nearly linear across one gap. A
plain average of the midpoint samples is reported as the secondary version.
theta is the Riemann-Siegel theta asymptotic in float64 (rsz.theta), whose
error at these heights is < 1e-4 absolute, i.e. < 4e-5 in S: ample against
max |S| ~ 1-3. It is validated against mpmath.siegeltheta in the self-test.

DATA. Platt windows: exact block-structured binary (2^-101 absolute precision,
md5-verified, every_millionth cross-checked; decoder convention: a block's
Nt0/Nt1 are COUNTS, its zeros carry ranks Nt0+1..Nt1). The low range has no
stored zero locations (e5f certifies counts, not positions), so it is
recomputed with the same Riemann-Siegel engine e5f used (rsz.zed, k=1),
via a chunked sign-change scan plus a close-pair rescue pass (grid |Z| dips
without an adjacent sign change get a 64x finer rescan), and the assembled
count is HARD-GATED against the e5f certified totals at 1e7 and 2e7: sign
changes can only undercount per interval, so total equality with the
certified count forces per-interval equality, i.e. every rank n is exact.

NAMING. The TODO's candidate label for this probe was "e5g", but e5g is
already taken (e5g_race_from_zeros.py); e5i is the next free letter after
e5h. See the provenance section of e5i_s_of_t.md.

Usage:
    python -m experiments.primes.e5i_s_of_t             # quick self-checks (N/N passed)
    python -m experiments.primes.e5i_s_of_t --full      # full overnight run
    python -m experiments.primes.e5i_s_of_t --full --tlow=1e7 --workers=4
"""
from __future__ import annotations

import os
import struct
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

import numpy as np

from experiments.primes import platt_reader as pr
from experiments.primes.rsz import theta, zed

PI = np.pi
CACHE = Path(__file__).resolve().parent / "_cache"
RESULTS_NPZ = CACHE / "e5i_results.npz"
LOWRANGE_NPY = CACHE / "e5i_lowrange_gammas.npy"

# The three Platt windows (DATASETS.md section 18). Expected first ranks are
# the every_millionth-anchored values derived and cross-checked there; the
# self-test re-asserts them against each file's own block-0 header.
PLATT_WINDOWS = [
    ("w1_3.7e8", "zeros_370046000.dat", 994804897),
    ("w2_3.3e9", "zeros_3293246000.dat", 9999087291),
    ("w3_3.06e10", "zeros_30607946000.dat", 103793332901),
]

# e5f certified count anchors (counts of zeros with gamma <= height).
CERT_ANCHORS = [
    ("1e7", CACHE / "e5f_rh_verified_10000000_certified.npz"),
    ("2e7", CACHE / "e5f_rh_verified_20000000_certified.npz"),
]

LANDMARKS = np.array([
    14.134725142, 21.022039639, 25.010857580, 30.424876126, 32.935061588,
    37.586178159, 40.918719012, 43.327073281, 48.005150881, 49.773832478,
])


# ----------------------------------------------------------------------
# Platt window decoding (vectorized float64; exactness is not needed for S,
# see the error budget in the module docstring)
# ----------------------------------------------------------------------

def decode_platt(path: Path, max_blocks: int | None = None):
    """Decode a Platt .dat file to (n_first, n_last, gammas) in float64.

    Per block: deltas are exact 104-bit integers in units of 2^-101; we
    convert each 13-byte entry to float64 as lo*2^-101 + mid*2^-37 + hi*2^-5
    (each scaling is a power of two, so per-entry error is one rounding at
    2^-53 relative) and cumulative-sum within the block. Accumulated float64
    error over one block (~7500 entries spanning 2100 in height) is < 1e-8,
    far below the 1e-5 height accuracy S needs.
    """
    gs = []
    n_first = None
    prev_t1 = prev_Nt1 = None
    with open(path, "rb") as fh:
        (nb,) = struct.unpack("<Q", fh.read(8))
        if max_blocks is not None:
            nb = min(nb, max_blocks)
        for i in range(nb):
            t0, t1, Nt0, Nt1 = struct.unpack("<ddQQ", fh.read(32))
            if i == 0:
                n_first = Nt0 + 1
            elif t0 != prev_t1 or Nt0 != prev_Nt1:
                raise ValueError(f"{path}: block {i} does not chain")
            prev_t1, prev_Nt1 = t1, Nt1
            nz = Nt1 - Nt0
            e = np.frombuffer(fh.read(nz * pr.ENTRY_SIZE), dtype=pr.ENTRY_DTYPE)
            d = (e["lo"].astype(np.float64) * 2.0 ** -101
                 + e["mid"].astype(np.float64) * 2.0 ** -37
                 + e["hi"].astype(np.float64) * 2.0 ** -5)
            gs.append(t0 + np.cumsum(d))
    return n_first, prev_Nt1, np.concatenate(gs)


# ----------------------------------------------------------------------
# S statistics
# ----------------------------------------------------------------------

def theta_over_pi(t: np.ndarray, chunk: int = 4_000_000) -> np.ndarray:
    out = np.empty(t.size)
    for i in range(0, t.size, chunk):
        out[i:i + chunk] = theta(t[i:i + chunk]) / PI
    return out


def sigma2_theory(T: float) -> float:
    """The Selberg/Ghosh leading-order variance of S: log log T / (2 pi^2)."""
    return float(np.log(np.log(T)) / (2.0 * PI ** 2))


def s_stats(n0: int, g: np.ndarray) -> dict:
    """All S statistics for zeros of ranks n0..n0+len(g)-1 at heights g.

    Second moments: 'sm2_time' is the gap-weighted Simpson time average of
    S^2 over [g[0], g[-1]] (primary, the version the Selberg theorem is
    about); 'sm2_mid' is the plain average of the midpoint samples
    (secondary); 'sm2_zero_plus' averages S(gamma_n^+)^2 (zero-sampled).
    """
    N = g.size
    n = n0 + np.arange(N, dtype=np.float64)      # exact: n0 + N < 2^53
    S_plus = n - theta_over_pi(g) - 1.0
    ap = np.abs(S_plus)
    am = np.abs(S_plus - 1.0)
    ip = int(np.argmax(ap))
    im = int(np.argmax(am))
    if ap[ip] >= am[im]:
        i_max, side, S_max = ip, "+", float(S_plus[ip])
    else:
        i_max, side, S_max = im, "-", float(S_plus[im] - 1.0)

    mids = 0.5 * (g[:-1] + g[1:])
    S_mid = n[:-1] - theta_over_pi(mids) - 1.0
    gaps = np.diff(g)
    fl = S_plus[:-1] ** 2
    fr = (S_plus[1:] - 1.0) ** 2
    fm = S_mid ** 2
    sm2_time = float(np.sum(gaps * (fl + 4.0 * fm + fr)) / 6.0 / (g[-1] - g[0]))
    sm2_mid = float(np.mean(fm))
    sm2_zero = float(np.mean(S_plus ** 2))

    hist, edges = np.histogram(S_mid, bins=240, range=(-3.0, 3.0))
    n_outside = int(S_mid.size - hist.sum())

    # top-20 |S| one-sided extremes: (gamma, n, S_signed, side +1/-1)
    kk = min(20, N)
    cand = np.unique(np.concatenate([
        np.argpartition(ap, -kk)[-kk:], np.argpartition(am, -kk)[-kk:]]))
    rows = []
    for i in cand:
        rows.append((g[i], n[i], S_plus[i], 1.0))
        rows.append((g[i], n[i], S_plus[i] - 1.0, -1.0))
    rows.sort(key=lambda r: -abs(r[2]))
    top20 = np.array(rows[:kk], dtype=np.float64)

    return dict(
        count=N, n_first=int(n0), n_last=int(n0 + N - 1),
        g_first=float(g[0]), g_last=float(g[-1]),
        max_abs_S=abs(S_max), S_at_max=S_max, side_at_max=side,
        gamma_at_max=float(g[i_max]), n_at_max=int(n0 + i_max),
        sm2_time=sm2_time, sm2_mid=sm2_mid, sm2_zero_plus=sm2_zero,
        hist=hist, hist_edges=edges, hist_outside=n_outside, top20=top20,
    )


def report_line(label: str, s: dict) -> str:
    T_mid = 0.5 * (s["g_first"] + s["g_last"])
    th = sigma2_theory(T_mid)
    return (f"{label:12s} n=[{s['n_first']:,}..{s['n_last']:,}] "
            f"T=[{s['g_first']:.3f}..{s['g_last']:.3f}]\n"
            f"{'':12s} max|S| = {s['max_abs_S']:.6f} (S = {s['S_at_max']:+.6f} "
            f"side {s['side_at_max']} at gamma = {s['gamma_at_max']:.6f}, "
            f"n = {s['n_at_max']:,})\n"
            f"{'':12s} <S^2>_time = {s['sm2_time']:.6f}  <S^2>_mid = {s['sm2_mid']:.6f}  "
            f"<S^2>_zero+ = {s['sm2_zero_plus']:.6f}\n"
            f"{'':12s} Selberg/Ghosh loglogT/(2pi^2) at T_mid = {th:.6f}  "
            f"ratio time/theory = {s['sm2_time'] / th:.4f}\n"
            f"{'':12s} pre-registration max|S| < 3: "
            f"{'PASS' if s['max_abs_S'] < 3.0 else 'FAIL'}")


# ----------------------------------------------------------------------
# Low-range zero scan (recomputation gated against e5f certified counts)
# ----------------------------------------------------------------------

def _bisect(lo: np.ndarray, hi: np.ndarray, slo: np.ndarray, k: int,
            iters: int = 22) -> np.ndarray:
    lo = lo.copy()
    hi = hi.copy()
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        same = np.signbit(zed(mid, k=k)) == slo
        lo = np.where(same, mid, lo)
        hi = np.where(same, hi, mid)
    return 0.5 * (lo + hi)


def scan_chunk(a: float, b: float, h: float = 0.02, tau: float = 0.25,
               sub: int = 64, k: int = 1, pad: float = 0.5,
               refine: int = 22) -> np.ndarray:
    """All zeros of Z in [a, b), by grid sign changes plus close-pair rescue.

    Rescue pass: a pair of zeros closer than the grid step shows up not as a
    sign change but as a grid point where |Z| dips near 0 with the SAME sign
    on both neighbors (crossing both zeros flips the sign twice). Every
    interior local minimum of |Z| with no adjacent sign change and |Z| < tau
    gets a (sub)x finer rescan over +-1.5h. tau = 0.25 is ~3x above the worst
    dip magnitude a missed pair can leave at this step (|Z''|/2 * (h/2)^2
    with generous amplitude), and the certified-count gate in low_range_scan
    is the hard backstop behind this heuristic.
    """
    lo_edge = max(10.0, a - pad)
    grid = np.arange(lo_edge, b + pad + h, h)
    z = zed(grid, k=k)
    sb = np.signbit(z)
    ch = np.flatnonzero(sb[:-1] != sb[1:])
    zeros = (_bisect(grid[ch], grid[ch + 1], sb[ch], k, refine)
             if ch.size else np.empty(0))

    if tau > 0.0 and grid.size >= 3:
        az = np.abs(z)
        interior = ((az[1:-1] <= az[:-2]) & (az[1:-1] <= az[2:])
                    & (az[1:-1] < tau)
                    & (sb[1:-1] == sb[:-2]) & (sb[1:-1] == sb[2:]))
        js = np.flatnonzero(interior) + 1
        if js.size:
            wlo, whi = grid[js] - 1.5 * h, grid[js] + 1.5 * h
            merged = []
            cl, cr = wlo[0], whi[0]
            for l, r in zip(wlo[1:], whi[1:]):
                if l <= cr:
                    cr = r
                else:
                    merged.append((cl, cr))
                    cl, cr = l, r
            merged.append((cl, cr))
            fh_ = h / sub
            segs = [np.arange(l, r + fh_, fh_) for l, r in merged]
            fg = np.concatenate(segs)
            fsb = np.signbit(zed(fg, k=k))
            chs, off = [], 0
            for seg in segs:
                L = seg.size
                c = np.flatnonzero(fsb[off:off + L - 1] != fsb[off + 1:off + L])
                chs.append(c + off)
                off += L
            chs = np.concatenate(chs)
            if chs.size:
                extra = _bisect(fg[chs], fg[chs + 1], fsb[chs], k, refine)
                zeros = np.concatenate([zeros, extra])

    zeros = np.sort(zeros)
    if zeros.size > 1:
        # dedupe base-vs-rescue refinds (separation ~1e-7); true gaps at
        # these heights never get below ~3e-4, so 1e-5 cannot merge real pairs
        zeros = zeros[np.concatenate([[True], np.diff(zeros) > 1e-5])]
    return zeros[(zeros >= a) & (zeros < b)]


def _job(args):
    i, a, b, h, tau, sub, k = args
    return i, scan_chunk(a, b, h=h, tau=tau, sub=sub, k=k)


def _run_pass(chunks, h, tau, sub, k, workers, log):
    jobs = [(i, a, b, h, tau, sub, k) for i, (a, b) in enumerate(chunks)]
    results = [None] * len(jobs)
    # cost model ~ integral sqrt(t) dt per chunk, for the ETA line
    w = np.array([b ** 1.5 - a ** 1.5 for a, b in chunks])
    w_total, w_done = float(w.sum()), 0.0
    t0 = time.time()
    ex = ProcessPoolExecutor(max_workers=workers)
    try:
        futs = {ex.submit(_job, j): j[0] for j in jobs}
        n_done = 0
        for fut in as_completed(futs):
            i, zs = fut.result()
            results[i] = zs
            n_done += 1
            w_done += float(w[i])
            if n_done % 20 == 0 or n_done == len(jobs):
                el = time.time() - t0
                eta = el * (w_total / max(w_done, 1e-9) - 1.0)
                log(f"  pass tau={tau}: {n_done}/{len(jobs)} chunks, "
                    f"elapsed {el / 60:.1f} min, ETA {eta / 60:.1f} min")
    finally:
        ex.shutdown()
    return np.concatenate(results)


def low_range_scan(T: float, h: float = 0.02, chunk_len: float = 25000.0,
                   workers: int = 7, k: int = 1, log=print):
    """Scan [10, T] for all zeros, gate the count against e5f certified totals.

    Returns (gammas_trimmed_to_top_anchor, gate_status_string, anchor_info).
    """
    edges = np.arange(10.0, T, chunk_len)
    chunks = [(float(a), float(min(a + chunk_len, T))) for a in edges]
    log(f"low range: [10, {T:.0f}], {len(chunks)} chunks of {chunk_len:.0f}, "
        f"h={h}, workers={workers}")
    zs = _run_pass(chunks, h, 0.25, 64, k, workers, log)
    assert np.all(np.diff(zs) > 0), "assembled zeros not strictly increasing"

    anchors = []
    for name, path in CERT_ANCHORS:
        d = np.load(path)
        h_cert, found = float(d["height"]), int(d["found"])
        if h_cert <= T:
            anchors.append((name, h_cert, found))
    gate = "PASS"
    for name, h_cert, found in anchors:
        cnt = int(np.searchsorted(zs, h_cert + 1e-6, side="right"))
        log(f"  gate {name}: found {cnt:,} zeros <= {h_cert:.6f}, "
            f"certified {found:,} -> {'OK' if cnt == found else 'MISMATCH'}")
    if any(int(np.searchsorted(zs, hc + 1e-6, side="right")) != fd
           for _, hc, fd in anchors):
        log("  count mismatch: escalation pass (tau=1.0, sub=128) over all chunks")
        zs = _run_pass(chunks, h, 1.0, 128, k, workers, log)
        assert np.all(np.diff(zs) > 0)
        for name, h_cert, found in anchors:
            cnt = int(np.searchsorted(zs, h_cert + 1e-6, side="right"))
            ok = cnt == found
            log(f"  gate {name} (after escalation): {cnt:,} vs {found:,} "
                f"-> {'OK' if ok else 'MISMATCH'}")
            if not ok:
                gate = f"FAILED at {name}: {cnt} vs {found}"
    if gate == "PASS":
        log("  certified-count gate: PASS (per-interval completeness forced, "
            "ranks exact)")
    # trim to the top anchor height so every reported rank is certified-gated
    top_h = max(hc for _, hc, _ in anchors)
    zs = zs[zs <= top_h + 1e-6]
    return zs, gate, anchors


# ----------------------------------------------------------------------
# Full run
# ----------------------------------------------------------------------

def _flat(prefix: str, s: dict, out: dict):
    for key, val in s.items():
        out[f"{prefix}_{key}"] = val


def run_full(T_low: float = 2e7, workers: int = 7):
    log = lambda *a: print(*a, flush=True)
    out: dict = {"pre_registration": "max |S| < 3 in every window",
                 "started_utc": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())}
    log("e5i S(T) probe, full run")
    log("PRE-REGISTERED (see e5i_s_of_t.md, written before this run): "
        "max |S| < 3 in every window")
    log(f"started {out['started_utc']} UTC\n")

    # Stage A: the three Platt windows (fast, do first so results land early)
    log("=== Stage A: Platt windows ===")
    for label, fname, n_exp in PLATT_WINDOWS:
        t0 = time.time()
        path = pr.DATA_DIR / fname
        n_first, n_last, g = decode_platt(path)
        assert n_first == n_exp, f"{fname}: n_first {n_first} != expected {n_exp}"
        s = s_stats(n_first, g)
        assert s["count"] == n_last - n_first + 1
        _flat(label, s, out)
        log(f"[{time.time() - t0:6.1f}s] {report_line(label, s)}\n")
        np.savez_compressed(RESULTS_NPZ, **out)   # partial save per window
    log(f"partial results saved to {RESULTS_NPZ}")

    # Stage B: low range, recomputed and count-gated
    log("\n=== Stage B: low range ===")
    t0 = time.time()
    zs, gate, anchors = low_range_scan(T_low, workers=workers, log=log)
    log(f"low-range scan done in {(time.time() - t0) / 3600:.2f} h, "
        f"{zs.size:,} zeros, gate: {gate}")
    out["low_gate"] = gate
    out["low_anchors"] = np.array([(hc, fd) for _, hc, fd in anchors])
    try:
        np.save(LOWRANGE_NPY, zs)
        log(f"low-range gammas cached at {LOWRANGE_NPY}")
    except OSError as e:
        log(f"could not cache low-range gammas: {e}")

    s = s_stats(1, zs)
    _flat("low_all", s, out)
    log("\n" + report_line("low_all", s) + "\n")

    band_edges = [10.0, 1e3, 1e4, 1e5, 1e6, 1e7, float(zs[-1])]
    for i in range(len(band_edges) - 1):
        lo, hi = band_edges[i], band_edges[i + 1]
        i0, i1 = np.searchsorted(zs, lo), np.searchsorted(zs, hi, side="right")
        if i1 - i0 < 10:
            continue
        sb_ = s_stats(1 + i0, zs[i0:i1])
        _flat(f"low_band{i}", sb_, out)
        log(report_line(f"band[{lo:.0e},{hi:.0e}]", sb_) + "\n")

    out["finished_utc"] = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    np.savez_compressed(RESULTS_NPZ, **out)
    log(f"all results saved to {RESULTS_NPZ}")
    log(f"finished {out['finished_utc']} UTC")

    # Final verdict table
    log("\n=== VERDICT vs pre-registration (max |S| < 3) ===")
    for label in [w[0] for w in PLATT_WINDOWS] + ["low_all"]:
        m = out[f"{label}_max_abs_S"]
        log(f"  {label:12s} max|S| = {m:.6f}  "
            f"{'PASS' if m < 3.0 else 'FAIL'}")
    if gate != "PASS":
        log(f"  WARNING: low-range certified-count gate: {gate} "
            "(low-range ranks not fully certified; windows unaffected)")


# ----------------------------------------------------------------------
# Quick self-checks
# ----------------------------------------------------------------------

def main() -> int:
    import mpmath as mp
    passed = failed = 0

    def check(name, ok, detail=""):
        nonlocal passed, failed
        passed += ok
        failed += not ok
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" ({detail})" if detail else ""))

    print("e5i S(T) probe: quick self-checks")

    # 1. float64 asymptotic theta vs mpmath.siegeltheta
    mp.mp.dps = 40
    heights = [1e3, 1e5, 1e7, 3.7e8, 3.06e10]
    rel = max(abs(float(theta(t)) - float(mp.siegeltheta(t)))
              / abs(float(mp.siegeltheta(t))) for t in heights)
    check("theta f8 vs mpmath.siegeltheta rel < 1e-8", rel < 1e-8, f"max rel {rel:.2e}")

    # 2. first ten zeros from the scan pipeline match the landmarks.
    #    Tolerance 5e-3: the RS k=1 truncation bound 0.053 t^-1.25 over |Z'|
    #    allows ~2.5e-3 of location error at t=14 (measured 2.47e-3); at the
    #    survey heights (t > 1e3) the same bound is < 1e-5.
    g10 = scan_chunk(10.0, 50.5)
    ok = g10.size == 10 and np.max(np.abs(g10 - LANDMARKS)) < 5e-3
    check("first 10 zeros match landmarks < 5e-3", ok,
          f"n={g10.size}, max dev {np.max(np.abs(g10 - LANDMARKS[:g10.size])) if g10.size else -1:.2e}")

    # 3. two-way S at t=100: zero-count formula vs mpmath arg continuation
    #    (S(t) = (1/pi) arg zeta(1/2+it), continued along the horizontal
    #    segment from sigma=3, where the principal branch is the right one)
    g110 = scan_chunk(10.0, 110.0)
    n_at = int(np.searchsorted(g110, 100.0))
    S_count = n_at - float(theta(100.0)) / PI - 1.0
    sigmas = np.arange(3.0, 0.5 - 1e-9, -0.025)
    zsv = [mp.zeta(mp.mpc(s_, 100.0)) for s_ in sigmas]
    arg_tot = mp.arg(zsv[0])
    for z1, z2 in zip(zsv[:-1], zsv[1:]):
        arg_tot += mp.arg(z2 / z1)
    S_arg = float(arg_tot) / PI
    ok = n_at == 29 and abs(S_count - S_arg) < 1e-6
    check("S(100) two ways: count formula vs arg-continuation", ok,
          f"N(100)={n_at}, count {S_count:+.8f}, arg {S_arg:+.8f}")

    # 4. close-pair rescue: the Lehmer pair at t ~ 7005.06/7005.10 with a
    #    step chosen so the base grid straddles the pair (no point between)
    fine = scan_chunk(7000.0, 7010.0, h=0.005)
    base_only = scan_chunk(7000.0, 7010.0, h=0.055, tau=0.0)
    rescued = scan_chunk(7000.0, 7010.0, h=0.055, tau=0.25)
    pair = rescued[(rescued > 7005.0) & (rescued < 7005.2)]
    ok = (base_only.size == fine.size - 2 and rescued.size == fine.size
          and pair.size == 2 and 0.02 < pair[1] - pair[0] < 0.05)
    check("Lehmer pair missed by base grid, recovered by rescue pass", ok,
          f"fine {fine.size}, base {base_only.size}, rescued {rescued.size}")

    # 5. vectorized Platt decoder vs platt_reader's exact Fraction path
    w1 = pr.DATA_DIR / PLATT_WINDOWS[0][1]
    n_first, n_last3, g3 = decode_platt(w1, max_blocks=3)
    devs = []
    for off in (0, 2000):
        _, exact = pr.zero_at_index(w1, n_first + off)
        devs.append(abs(g3[off] - float(exact)))
    check("decoder vs exact reference at n_first, n_first+2000 < 1e-6",
          max(devs) < 1e-6, f"max dev {max(devs):.2e}")

    # 6. every_millionth digit anchor at n = 1e9 (index anchoring is exact)
    em = pr.load_every_millionth(pr.EVERY_MILLIONTH_PATH)
    _, gamma_b = pr.zero_at_index(w1, 10 ** 9)
    expect = em[10 ** 9]
    ours = pr.decimal_str(gamma_b, len(expect.split(".")[1]))
    check("every_millionth anchor n=1e9 matches to all printed digits",
          ours == expect, f"{ours[:25]}...")

    # 7. window anchors: header rank matches the derived table, and S at the
    #    first zero of each window is small (the anchor-consistency assert)
    ok7, det = True, []
    for label, fname, n_exp in PLATT_WINDOWS:
        nf, _, gb = decode_platt(pr.DATA_DIR / fname, max_blocks=1)
        S_first = nf - float(theta(gb[0])) / PI - 1.0
        ok7 &= (nf == n_exp) and abs(S_first) < 3.0
        det.append(f"{label}: n_first={nf}, S={S_first:+.3f}")
    check("window anchors: n_first as derived, |S(first zero)| < 3", ok7,
          "; ".join(det))

    # 8. S internals on a window-1 slice: rank arithmetic vs searchsorted
    #    midpoint counting, the S- = S+ - 1 identity, and max|S| sane
    s = s_stats(n_first, g3)
    n_arr = n_first + np.arange(g3.size, dtype=np.float64)
    S_plus = n_arr - theta_over_pi(g3) - 1.0
    mids = 0.5 * (g3[:-1] + g3[1:])
    S_mid_a = n_arr[:-1] - theta_over_pi(mids) - 1.0
    S_mid_b = ((n_first - 1 + np.searchsorted(g3, mids, side="right"))
               - theta_over_pi(mids) - 1.0)
    ok = (np.array_equal(S_mid_a, S_mid_b)
          and s["count"] == g3.size and s["max_abs_S"] < 3.0
          and abs(s["S_at_max"]) == s["max_abs_S"])
    check("window-1 slice: midpoint S two ways identical, max|S| < 3", ok,
          f"count {s['count']}, max|S| {s['max_abs_S']:.3f}")

    # 9. certified anchors on disk and closed (the low-range gate inputs)
    ok9, det = True, []
    for name, path in CERT_ANCHORS:
        d = np.load(path)
        ok9 &= bool(d["verified"]) and bool(d["certified"]) and bool(d["turing_closed"])
        det.append(f"{name}: found={int(d['found']):,}")
    check("e5f certified anchors present, verified+certified+turing_closed",
          ok9, "; ".join(det))

    print(f"{passed}/{passed + failed} passed")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--full" in args:
        tlow = 2e7
        workers = max(1, min(7, (os.cpu_count() or 2) - 1))
        for a in args:
            if a.startswith("--tlow="):
                tlow = float(a.split("=")[1])
            if a.startswith("--workers="):
                workers = int(a.split("=")[1])
        run_full(T_low=tlow, workers=workers)
    else:
        raise SystemExit(main())
