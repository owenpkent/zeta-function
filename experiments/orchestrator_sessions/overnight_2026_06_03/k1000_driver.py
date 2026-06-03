"""Overnight slow-compute: de Branges Q to K=1000 (does the ~6% failure density stabilize?).

Reuses the VERIFIED e2db2 machinery (xi, Q_at, dps_for_gamma). Saves to a SEPARATE npz so it
cannot clobber the canonical K=500 data. Deterministic; the main agent re-derives a sample before
trusting it. Answers the digest's open question A1: whether the de Branges (3.1) pointwise-failure
density (~6% at K=500, with a (400,500]:11 uptick) stabilizes / tracks the zero density, or drifts.

Run: python -m experiments.orchestrator_sessions.overnight_2026_06_03.k1000_driver
"""
from __future__ import annotations
import functools, time
from pathlib import Path
import mpmath as mp
import numpy as np
from experiments.arithmetic_geometric.e2db2_debranges_k500 import xi, Q_at, dps_for_gamma  # noqa: F401

print = functools.partial(print, flush=True)  # noqa: A001
HERE = Path(__file__).resolve().parent
NPZ = HERE / "k1000.npz"
K = 1000


def main():
    gammas, logsQ, signs, neg, dps_used = [], [], [], [], []
    t0 = time.time(); last = t0
    for k in range(1, K + 1):
        mp.mp.dps = 60
        rho = mp.zetazero(k)
        gamma = float(rho.imag)
        mp.mp.dps = dps_for_gamma(gamma)
        rho = mp.zetazero(k)
        qk, lq, sg, _, _ = Q_at(rho)
        gammas.append(gamma); logsQ.append(float(lq)); signs.append(sg); dps_used.append(mp.mp.dps)
        if sg < 0:
            neg.append(k)
        now = time.time()
        if k % 25 == 0 or k == K:
            print(f"  k={k:4d} gamma={gamma:10.3f} dps={mp.mp.dps:5d} neg_so_far={len(neg)} [{now-t0:7.1f}s]")
            # checkpoint save so a kill/timeout still leaves partial data
            np.savez(NPZ, K=k, gamma=np.array(gammas), logQ=np.array(logsQ),
                     sign=np.array(signs, int), dps_used=np.array(dps_used, int),
                     neg_indices=np.array(neg, int))
            last = now
    # density per 100-window
    print(f"\nK={K} done in {time.time()-t0:.0f}s. negatives = {len(neg)} ({100*len(neg)/K:.1f}%)")
    print("per-100 windows:", [sum(1 for x in neg if lo < x <= lo+100) for lo in range(0, K, 100)])
    print("neg set:", neg)


if __name__ == "__main__":
    main()
