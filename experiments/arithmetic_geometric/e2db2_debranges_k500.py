"""2DB.2 -- de Branges / Conrey-Li cross-term Q(rho) extended to K=500 (density revision of 2DB.1).

Slow-compute extension of 2DB.1 (e2db_debranges_crossterm.py). Same convention, NO new claims
about the mathematics: a deterministic data-gathering run that REVISES one empirical reading of
2DB.1. 2DB.1 ran k=1..50 and found a SINGLE negative (k=34, the Conrey-Li anchor), which read as
"sporadic." Pushed to K=500, the de Branges pointwise positivity (Conrey-Li (3.1)) fails at
POSITIVE DENSITY (~6%, 32 of 500), not once, while RH holds. The mathematical lesson is unchanged
and only sharpened: the RH-equivalent signed pairing must be a global SUM (the Li coefficients
lambda_n), NOT the pointwise Hermite-Biehler cross-term Q.

CONVENTION (identical to 2DB.1; reproduces Conrey-Li, arXiv:math/9812166):
    xi(s) = s(s-1) pi^{-s/2} Gamma(s/2) zeta(s)      (the NO-1/2 normalization)
    Q(rho) = -Re{ xi'(rho) xi(1 + rho) }             (de Branges positivity (3.1) consequence)
    xi'(rho) via mp.diff.

PRECISION. |Q| ~ 10^{-(pi/2) gamma / ln10}; gamma_500 ~ 811 so |Q| ~ 10^{-553} at the deepest
zeros. dps is scaled with gamma (dps_for_gamma) so the SIGN of Q and log10|Q| stay reliable with a
comfortable guard band against the cancellation in -Re{...}.

RESULTS (verified: the anchor reproduces Conrey-Li, and an independent re-derivation of sampled
indices matched the negative set; see experiments/orchestrator_sessions/overnight_2026_06_03/DIGEST.md):
    - negative-Q index set (32): {34, 71, 106, 127, 144, 173, 184, 186, 196, 233, 257, 265, 282,
      289, 298, 315, 334, 363, 368, 380, 394, 401, 409, 423, 436, 453, 462, 477, 483, 485, 492, 497}
    - density ~6%, tracking the zero density (per-100 windows: 2,7,6,6,11); no strong clustering.
    - anchor Q(rho_34) = -5.389101e-69, ratio 1.000000 to Conrey-Li.
    - slope log10|Q| vs gamma: full -0.6768, tail -0.6785, -> -(pi/2)/ln10 = -0.68219 (one-sided).
    - two-factor decomposition -0.3385 + -0.3381 ~ the double-Gamma law (each ~ -(pi/4)/ln10).

K=1000 FOLLOW-UP (data in e2db2_debranges_k1000.npz; verified independently). The density does NOT
stabilize at the K=500 ~6%: it drifts UPWARD to 80/1000 = 8.0%, per-100 windows [2,7,6,6,11,8,10,8,
13,9] (rising from ~5% at low zeros to ~9-13% higher). So the de Branges pointwise (3.1) failure is a
generic, mildly-increasing positive-density phenomenon; the "~6%" of the K=500 sample was a low-zero
undercount. Reproduce with `ZETA_K=1000 python -m experiments.arithmetic_geometric.e2db2_debranges_k500`
(writes e2db2_debranges_k1000.npz; ~4.4h, precision scaled with gamma up to dps~1028 at gamma~1419).

HONEST SCOPE. A COMPUTED coordinate, not a proof. It refines the empirical negative-index set and
the asymptotic slope of 2DB.1; the reading (de Branges (3.1) is strictly-stronger-than-RH and fails
for zeta; the pointwise cross-term is the WRONG positivity) is unchanged. Does NOT touch the M3
signature gap. The K2 (D-H) control was not re-run at K=500 (inherited from 2DB.1, T<=90).

Run:  python -m experiments.arithmetic_geometric.e2db2_debranges_k500            (full K=500, slow)
      python -m experiments.arithmetic_geometric.e2db2_debranges_k500 --report   (summary from npz)
      ZETA_K=50 python -m experiments.arithmetic_geometric.e2db2_debranges_k500   (quick K=50 check)
"""

from __future__ import annotations

import functools
import os
import sys
import time
from pathlib import Path

import mpmath as mp

print = functools.partial(print, flush=True)  # noqa: A001

HERE = Path(__file__).resolve().parent
NPZ = HERE / "e2db2_debranges_k500.npz"
PUBLISHED_34 = mp.mpf("-5.389100507182945e-69")   # Conrey-Li anchor


def dps_for_gamma(gamma: float) -> int:
    """Working precision so log10|Q| and sign(Q) survive: |Q| ~ 10^{-(pi/2) gamma/ln10}, plus
    a fixed guard band for the cancellation in -Re{...} and the numerical derivative; floor 80."""
    mag = (mp.pi / 2) * gamma / float(mp.log(10))
    return max(80, int(mag) + 60)


def xi(s):
    """Completed zeta, Conrey-Li normalization (no 1/2 factor)."""
    s = mp.mpc(s)
    return s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def Q_at(rho):
    """Q(rho) = -Re{xi'(rho) xi(1+rho)}. Returns (Q, log10|Q|, sign, |xi'|, |xi(1+rho)|)."""
    xip = mp.diff(xi, rho)
    x1 = xi(1 + rho)
    qk = -mp.re(xip * x1)
    return qk, mp.log10(abs(qk)), int(mp.sign(qk)), abs(xip), abs(x1)


def _slope(gammas, logabsQ):
    n = len(gammas)
    if n < 3:
        return float("nan")
    mx = sum(gammas) / n
    my = sum(logabsQ) / n
    sxx = sum((x - mx) ** 2 for x in gammas)
    if sxx == 0:
        return float("nan")
    return sum((x - mx) * (y - my) for x, y in zip(gammas, logabsQ)) / sxx


def run(K: int):
    target = -float(mp.pi / 2 / mp.log(10))
    half = -float(mp.pi / 4 / mp.log(10))
    print("=" * 80)
    print(f"2DB.2 -- de Branges/Conrey-Li cross-term Q(rho) to K={K}")
    print(f"  xi(s)=s(s-1)pi^(-s/2)Gamma(s/2)zeta(s) [no-1/2]; Q=-Re(xi'(rho)xi(1+rho))")
    print(f"  target asymptotic slope log10|Q| vs gamma = -(pi/2)/ln10 = {target:.5f}")
    print("=" * 80)

    gammas, logsQ, signs, sub_xip, sub_x1, dps_used, neg = [], [], [], [], [], [], []
    q34 = None
    t0 = time.time(); last = t0
    for k in range(1, K + 1):
        mp.mp.dps = 60
        rho = mp.zetazero(k)
        gamma = float(rho.imag)
        mp.mp.dps = dps_for_gamma(gamma)
        rho = mp.zetazero(k)
        qk, lq, sg, axip, ax1 = Q_at(rho)
        if k == 34:
            q34 = qk
        if sg < 0:
            neg.append(k)
        gammas.append(gamma); logsQ.append(float(lq)); signs.append(sg)
        sub_xip.append(float(mp.log10(axip))); sub_x1.append(float(mp.log10(ax1)))
        dps_used.append(mp.mp.dps)
        now = time.time()
        if k <= 5 or k % 25 == 0 or now - last > 20 or k == K:
            print(f"  k={k:4d}  gamma={gamma:11.4f}  dps={mp.mp.dps:5d}  sign={sg:+d}  "
                  f"log10|Q|={float(lq):10.3f}  [{now-t0:7.1f}s]")
            last = now

    mp.mp.dps = 80
    print("-" * 80)
    if q34 is not None:
        print(f"ANCHOR  Q(rho_34) = {mp.nstr(q34, 13)}   /Conrey-Li ratio = {mp.nstr(q34/PUBLISHED_34, 8)}")
    print(f"\nNEGATIVE-Q INDEX SET (de Branges (3.1) fails pointwise):\n  {neg}\n  count = {len(neg)} of {K}")
    if len(neg) >= 2:
        gaps = [neg[i + 1] - neg[i] for i in range(len(neg) - 1)]
        print(f"  gaps min/mean/max = {min(gaps)} / {sum(gaps)/len(gaps):.1f} / {max(gaps)}")
    s_all = _slope(gammas, logsQ)
    cut = K // 5
    s_tail = _slope(gammas[cut:], logsQ[cut:])
    print(f"\nFULL slope k=1..{K} = {s_all:.5f}   TAIL k={cut+1}..{K} = {s_tail:.5f}   target = {target:.5f}")
    print(f"TWO-FACTOR: slope[log|xi'(rho)|]={_slope(gammas, sub_xip):.5f}, "
          f"slope[log|xi(1+rho)|]={_slope(gammas, sub_x1):.5f}  (each ~ {half:.5f})")
    print(f"\nTotal wall time: {time.time()-t0:.1f}s for K={K}")
    _save(K, gammas, logsQ, signs, sub_xip, sub_x1, dps_used, neg, q34, s_all, s_tail, target)
    return dict(K=K, neg=neg, slope_all=s_all, slope_tail=s_tail, q34=q34)


def _save(K, gammas, logsQ, signs, sub_xip, sub_x1, dps_used, neg, q34, slope_all, slope_tail, target):
    try:
        import numpy as np
    except Exception as exc:  # pragma: no cover
        print(f"(npz skipped: {exc})"); return
    out = HERE / f"e2db2_debranges_k{K}.npz"   # K-dependent so K=500 and K=1000 coexist
    np.savez(out, K=K, gamma=np.array(gammas, float), logQ=np.array(logsQ, float),
             sign=np.array(signs, int), sub_xip=np.array(sub_xip, float), sub_x1=np.array(sub_x1, float),
             dps_used=np.array(dps_used, int), neg_indices=np.array(neg, int),
             q34=float(q34) if q34 is not None else float("nan"),
             slope_all=slope_all, slope_tail=slope_tail, target_slope=target)
    print(f"Saved: {out}")


def report_from_npz():
    """Reprint the summary from the saved npz (the canonical K=500 run; the npz is ground truth)."""
    import numpy as np
    d = np.load(NPZ)
    K = int(d["K"]); g = d["gamma"]; lq = d["logQ"]
    sub_xip = d["sub_xip"]; sub_x1 = d["sub_x1"]; dps_used = d["dps_used"]
    neg = d["neg_indices"].tolist(); q34 = float(d["q34"])
    target = -float(mp.pi / 2 / mp.log(10)); half = -float(mp.pi / 4 / mp.log(10))

    def slope(x, y):
        x = np.asarray(x, float); y = np.asarray(y, float)
        return float(np.polyfit(x, y, 1)[0]) if len(x) >= 3 else float("nan")

    print("=" * 80)
    print(f"2DB.2 -- de Branges/Conrey-Li cross-term Q(rho) to K={K}  [report from npz]")
    print("=" * 80)
    print(f"  max gamma = {g.max():.4f}   dps range {int(dps_used.min())}..{int(dps_used.max())}")
    margin = dps_used - np.abs(lq)
    print(f"  precision guard band min (dps-|log10|Q||) = {margin.min():.1f} at k={int(np.argmin(margin)+1)}")
    print(f"ANCHOR  Q(rho_34) = {q34:.6e}   /Conrey-Li ratio = {q34/float(PUBLISHED_34):.6f}")
    print(f"\nNEGATIVE-Q INDEX SET ({len(neg)} of {K}):\n  {neg}")
    if len(neg) >= 2:
        gaps = [neg[i + 1] - neg[i] for i in range(len(neg) - 1)]
        print(f"  gaps min/mean/max = {min(gaps)} / {sum(gaps)/len(gaps):.1f} / {max(gaps)}")
    print(f"  negatives per 100-index window:")
    for lo in range(0, K, 100):
        print(f"    k in ({lo},{lo+100}]: {sum(1 for k in neg if lo < k <= lo + 100)}")
    print(f"\nFULL slope k=1..{K} = {slope(g, lq):.5f}   TAIL k={K//5+1}..{K} = {slope(g[K//5:], lq[K//5:]):.5f}"
          f"   target = {target:.5f}")
    print(f"TWO-FACTOR: slope[log|xi'(rho)|]={slope(g, sub_xip):.5f}, slope[log|xi(1+rho)|]={slope(g, sub_x1):.5f}"
          f"  (each ~ {half:.5f})")


if __name__ == "__main__":
    if "--report" in sys.argv:
        report_from_npz()
    else:
        run(int(os.environ.get("ZETA_K", "500")))
