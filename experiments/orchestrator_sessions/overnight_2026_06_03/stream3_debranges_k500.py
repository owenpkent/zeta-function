"""STREAM 3b (overnight 2026-06-03) -- de Branges / Conrey-Li cross-term Q(rho) to K=500.

Slow-compute extension of 2DB.1 (experiments/arithmetic_geometric/e2db_debranges_crossterm.py).
Same convention, NO new claims: this is a deterministic data-gathering run.

CONVENTION (identical to 2DB.1, reproduces Conrey-Li, arXiv:math/9812166):
    xi(s) = s(s-1) pi^{-s/2} Gamma(s/2) zeta(s)      (the NO-1/2 normalization)
    Q(rho) = -Re{ xi'(rho) xi(1 + rho) }             (de Branges positivity (3.1) consequence)
    xi'(rho) computed via mp.diff.

WHAT WE PUSH. 2DB.1 ran k=1..50 at dps=80 and found:
    - negative-Q index set = {34} (exactly one), the Conrey-Li anchor.
    - finite-size slope of log10|Q| vs gamma = -0.655, target -(pi/2)/ln10 = -0.68224.
This script pushes K toward 500. Because |Q| ~ 10^{-(pi/2 gamma)/ln10} and gamma_500 ~ 811,
the deepest zeros have |Q| ~ 10^{-553}; dps is scaled with gamma so the sign of Q (the negative
set) and log10|Q| stay reliable (the catastrophic cancellation in -Re{...} loses a few digits,
so we keep a comfortable guard band).

HONEST SCOPE. This is a COMPUTED coordinate, not a proof. It refines the empirical negative-index
set and the asymptotic slope. The mathematical reading (de Branges (3.1) is strictly-stronger-than-
RH and fails for zeta; the pointwise cross-term is the WRONG positivity) is unchanged from 2DB.1.

Run: python -m experiments.orchestrator_sessions.overnight_2026_06_03.stream3_debranges_k500
  optional: set ZETA_K env var to override the target K (default 500).
"""

from __future__ import annotations

import functools
import os
import sys
import time
from pathlib import Path

import mpmath as mp

# Unbuffered prints so a long background run shows incremental progress in the log.
print = functools.partial(print, flush=True)  # noqa: A001

HERE = Path(__file__).resolve().parent
PUBLISHED_34 = mp.mpf("-5.389100507182945e-69")   # Conrey-Li anchor


# ----------------------------------------------------------------------------- precision policy
def dps_for_gamma(gamma: float) -> int:
    """Working precision needed so log10|Q| and sign(Q) survive.

    |Q| ~ 10^{-(pi/2) gamma / ln10}. The two xi factors plus the diff plus the cancellation in
    -Re{xi'(rho) xi(1+rho)} cost roughly another constant. We set dps to cover the magnitude of
    the SMALLER of the two factors and add a fixed guard band, then floor at 80 (the 2DB.1 value).
    """
    # exponent magnitude of |Q| in decimal digits, doubled headroom for the cancellation + diff.
    mag = (mp.pi / 2) * gamma / float(mp.log(10))
    return max(80, int(mag) + 60)


# ----------------------------------------------------------------------------- xi / Q
def xi(s):
    """Completed zeta, Conrey-Li normalization (no 1/2 factor)."""
    s = mp.mpc(s)
    return s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def Q_at(rho):
    """Q(rho) = -Re{xi'(rho) xi(1+rho)}.  Returns (Q, log10|Q|, sign, |xi'|, |xi(1+rho)|)."""
    xip = mp.diff(xi, rho)
    x1 = xi(1 + rho)
    qk = -mp.re(xip * x1)
    return qk, mp.log10(abs(qk)), int(mp.sign(qk)), abs(xip), abs(x1)


# ----------------------------------------------------------------------------- statistics
def _slope(gammas, logabsQ):
    """OLS slope of log10|Q| vs gamma."""
    n = len(gammas)
    if n < 3:
        return float("nan")
    mx = sum(gammas) / n
    my = sum(logabsQ) / n
    sxx = sum((x - mx) ** 2 for x in gammas)
    if sxx == 0:
        return float("nan")
    return sum((x - mx) * (y - my) for x, y in zip(gammas, logabsQ)) / sxx


# ----------------------------------------------------------------------------- main run
def run(K: int):
    target = -float(mp.pi / 2 / mp.log(10))   # -0.68224...
    half = -float(mp.pi / 4 / mp.log(10))      # -0.34112... (single-Gamma)

    print("=" * 80)
    print(f"STREAM 3b -- de Branges/Conrey-Li cross-term Q(rho) to K={K}")
    print(f"  xi(s)=s(s-1)pi^(-s/2)Gamma(s/2)zeta(s) [no-1/2]; Q=-Re(xi'(rho)xi(1+rho))")
    print(f"  target asymptotic slope log10|Q| vs gamma = -(pi/2)/ln10 = {target:.5f}")
    print("=" * 80)

    gammas, logsQ, signs = [], [], []
    sub_xip, sub_x1, dps_used = [], [], []
    neg = []
    q34 = None
    t0 = time.time()
    last_report = t0

    for k in range(1, K + 1):
        # zetazero precision: needs enough to place rho, modest relative to the Q precision.
        # locate the zero first at a safe precision, then refine working dps for the Q evaluation.
        mp.mp.dps = 60
        rho = mp.zetazero(k)
        gamma = float(rho.imag)

        mp.mp.dps = dps_for_gamma(gamma)
        # re-fetch rho at the higher precision so xi' is accurate to working dps
        rho = mp.zetazero(k)

        qk, lq, sg, axip, ax1 = Q_at(rho)
        if k == 34:
            q34 = qk
        if sg < 0:
            neg.append(k)

        gammas.append(gamma)
        logsQ.append(float(lq))
        signs.append(sg)
        sub_xip.append(float(mp.log10(axip)))
        sub_x1.append(float(mp.log10(ax1)))
        dps_used.append(mp.mp.dps)

        now = time.time()
        if k <= 5 or k % 25 == 0 or now - last_report > 20 or k == K:
            elapsed = now - t0
            print(f"  k={k:4d}  gamma={gamma:11.4f}  dps={mp.mp.dps:5d}  "
                  f"sign={sg:+d}  log10|Q|={float(lq):10.3f}  [{elapsed:7.1f}s]")
            last_report = now

    mp.mp.dps = 80
    print("-" * 80)

    # anchor check
    if q34 is not None:
        ratio = q34 / PUBLISHED_34
        print(f"ANCHOR  Q(rho_34) = {mp.nstr(q34, 13)}   /Conrey-Li ratio = {mp.nstr(ratio, 8)}")

    # negative set
    print(f"\nNEGATIVE-Q INDEX SET (k where de Branges (3.1) fails pointwise):")
    print(f"  {neg}")
    print(f"  count = {len(neg)} of {K}")
    # gaps between consecutive negatives (cluster check)
    if len(neg) >= 2:
        gaps = [neg[i + 1] - neg[i] for i in range(len(neg) - 1)]
        print(f"  gaps between consecutive negatives: {gaps}")
        print(f"  min gap = {min(gaps)}, max gap = {max(gaps)}, mean gap = {sum(gaps)/len(gaps):.1f}")

    # slope over growing windows: test convergence to -(pi/2)/ln10
    print(f"\nSLOPE of log10|Q| vs gamma over growing windows (target {target:.5f}):")
    windows = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
    windows = [w for w in windows if w <= K]
    if K not in windows:
        windows.append(K)
    print(f"  {'k<=W':>8}  {'slope(1..W)':>12}  {'slope tail(W/2..W)':>20}")
    for W in windows:
        s_full = _slope(gammas[:W], logsQ[:W])
        h = W // 2
        s_tail = _slope(gammas[h:W], logsQ[h:W])
        print(f"  {W:>8}  {s_full:>12.5f}  {s_tail:>20.5f}")

    s_all = _slope(gammas, logsQ)
    s_xip = _slope(gammas, sub_xip)
    s_x1 = _slope(gammas, sub_x1)
    # tail-only (drop first 20% to suppress finite-size curvature)
    cut = K // 5
    s_tail_global = _slope(gammas[cut:], logsQ[cut:])
    print(f"\nFULL slope k=1..{K}            = {s_all:.5f}")
    print(f"TAIL slope k={cut+1}..{K}        = {s_tail_global:.5f}   (drops first 20%)")
    print(f"target -(pi/2)/ln10            = {target:.5f}")
    print(f"TWO-FACTOR: slope[log|xi'(rho)|]={s_xip:.5f}, slope[log|xi(1+rho)|]={s_x1:.5f}")
    print(f"            each ~ {half:.5f} (single-Gamma); sum = {s_xip + s_x1:.5f}")

    elapsed = time.time() - t0
    print(f"\nTotal wall time: {elapsed:.1f}s for K={K}")

    _save(K, gammas, logsQ, signs, sub_xip, sub_x1, dps_used, neg, q34,
          s_all, s_tail_global, target)
    return dict(K=K, gammas=gammas, logsQ=logsQ, signs=signs, neg=neg,
                slope_all=s_all, slope_tail=s_tail_global, q34=q34)


def _save(K, gammas, logsQ, signs, sub_xip, sub_x1, dps_used, neg, q34,
          slope_all, slope_tail, target):
    try:
        import numpy as np
    except Exception as exc:  # pragma: no cover
        print(f"(npz skipped: {exc})")
        return
    np.savez(
        HERE / "stream3_debranges_k500.npz",
        K=K,
        gamma=np.array(gammas, dtype=float),
        logQ=np.array(logsQ, dtype=float),
        sign=np.array(signs, dtype=int),
        sub_xip=np.array(sub_xip, dtype=float),
        sub_x1=np.array(sub_x1, dtype=float),
        dps_used=np.array(dps_used, dtype=int),
        neg_indices=np.array(neg, dtype=int),
        q34=float(q34) if q34 is not None else float("nan"),
        slope_all=slope_all,
        slope_tail=slope_tail,
        target_slope=target,
    )
    print(f"Saved: {HERE / 'stream3_debranges_k500.npz'}")


def report_from_npz():
    """Reprint the full report from the saved npz (the canonical K=500 run used a
    fully-buffered stdout that was lost on the background harness; the npz is the
    ground truth and this reproduces the formatted summary deterministically)."""
    import numpy as np
    d = np.load(HERE / "stream3_debranges_k500.npz")
    K = int(d["K"])
    g = d["gamma"]; lq = d["logQ"]; sg = d["sign"]
    sub_xip = d["sub_xip"]; sub_x1 = d["sub_x1"]; dps_used = d["dps_used"]
    neg = d["neg_indices"].tolist()
    q34 = float(d["q34"])
    target = -float(mp.pi / 2 / mp.log(10))
    half = -float(mp.pi / 4 / mp.log(10))

    def slope(x, y):
        x = np.asarray(x, float); y = np.asarray(y, float)
        return float(np.polyfit(x, y, 1)[0]) if len(x) >= 3 else float("nan")

    print("=" * 80)
    print(f"STREAM 3b -- de Branges/Conrey-Li cross-term Q(rho) to K={K}  [report from npz]")
    print(f"  xi(s)=s(s-1)pi^(-s/2)Gamma(s/2)zeta(s) [no-1/2]; Q=-Re(xi'(rho)xi(1+rho))")
    print(f"  target asymptotic slope log10|Q| vs gamma = -(pi/2)/ln10 = {target:.5f}")
    print("=" * 80)
    print(f"  max gamma = {g.max():.4f}   dps range {int(dps_used.min())}..{int(dps_used.max())}")
    print(f"  log10|Q| range {lq.min():.3f} .. {lq.max():.3f}")
    margin = dps_used - np.abs(lq)
    print(f"  precision guard band min (dps-|log10|Q||) = {margin.min():.1f} at k={int(np.argmin(margin)+1)}")
    print("-" * 80)
    ratio = q34 / float(PUBLISHED_34)
    print(f"ANCHOR  Q(rho_34) = {q34:.6e}   /Conrey-Li ratio = {ratio:.6f}")
    print(f"\nNEGATIVE-Q INDEX SET (k where de Branges (3.1) fails pointwise):")
    print(f"  {neg}")
    print(f"  count = {len(neg)} of {K}")
    if len(neg) >= 2:
        gaps = [neg[i + 1] - neg[i] for i in range(len(neg) - 1)]
        print(f"  gaps: {gaps}")
        print(f"  min/mean/max gap = {min(gaps)} / {sum(gaps)/len(gaps):.1f} / {max(gaps)}")
    print(f"\n  negatives per 100-index window:")
    for lo in range(0, K, 100):
        c = sum(1 for k in neg if lo < k <= lo + 100)
        print(f"    k in ({lo},{lo+100}]: {c}")
    print(f"\nSLOPE log10|Q| vs gamma over growing windows (target {target:.5f}):")
    print(f"  {'k<=W':>6}  {'full(1..W)':>12}  {'tail(W/2..W)':>14}")
    for W in [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]:
        if W > K:
            continue
        print(f"  {W:>6}  {slope(g[:W], lq[:W]):>12.5f}  {slope(g[W//2:W], lq[W//2:W]):>14.5f}")
    cut = K // 5
    print(f"\nFULL slope k=1..{K}      = {slope(g, lq):.5f}")
    print(f"TAIL slope k={cut+1}..{K}    = {slope(g[cut:], lq[cut:]):.5f}  (drops first 20%)")
    print(f"target -(pi/2)/ln10      = {target:.5f}")
    print(f"TWO-FACTOR: slope[log|xi'(rho)|]={slope(g, sub_xip):.5f}, "
          f"slope[log|xi(1+rho)|]={slope(g, sub_x1):.5f}  (each ~ {half:.5f})")


if __name__ == "__main__":
    if "--report" in sys.argv:
        report_from_npz()
    else:
        K = int(os.environ.get("ZETA_K", "500"))
        run(K)
