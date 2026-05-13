"""E2: Fit the Fyodorov-Hiary-Keating second-order constant.

Hypothesis:
    E[ max_{|h| <= 1/2} log|zeta(1/2 + i(T+h))| ] = log log T - (3/4) log log log T + c.

For each height T_k = 10^k (k = 4..6 by default to keep runtime tractable),
sample many random centers t_k = T_k + xi with xi uniform on [-DELTA, DELTA],
compute the discrete window max, and average. Fit the affine model.

This experiment is slow and modest: at T = 10^8 with several centers and
2048-point windows each, expect tens of minutes. The cache helps if you
re-run with the same parameters.

Run:
    python experiments/multifractal/e2_fhk_max_fit.py
"""

from __future__ import annotations

import math
import sys
import time
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(THIS_DIR))

from zeta_sampling import window_max  # noqa: E402


# Defaults: 3 heights, 4 centers each. Bump up for a serious run.
LOG10_T = [4, 5, 6]
N_CENTERS = 4
DELTA = 1000.0
WINDOW = 1.0
WINDOW_POINTS = 2048
PREC = 30


def run_height(log10T, n_centers=N_CENTERS, seed=42):
    rng = np.random.default_rng(seed + log10T)
    T = 10.0 ** log10T
    offsets = rng.uniform(-DELTA, DELTA, size=n_centers)
    maxes = []
    for k, off in enumerate(offsets):
        t0 = time.time()
        m = window_max(
            T_center=T + off,
            window=WINDOW,
            num_points=WINDOW_POINTS,
            prec=PREC,
        )
        maxes.append(m)
        print(f"    center {k+1}/{n_centers}: T+off = {T+off:.4e}, "
              f"max = {m:+.4f}  ({time.time() - t0:.1f}s)")
    arr = np.array(maxes, dtype=float)
    return T, arr.mean(), arr.std(ddof=1) if arr.size > 1 else 0.0


def main():
    print("E2: FHK second-order fit")
    results = []
    for k in LOG10_T:
        print(f"  height 10^{k}:")
        T, mean_max, std_max = run_height(k)
        results.append((T, mean_max, std_max))

    Ts = np.array([r[0] for r in results])
    means = np.array([r[1] for r in results])
    stds = np.array([r[2] for r in results])

    L = np.log(np.log(Ts))            # log log T
    LL = np.log(np.log(np.log(Ts)))   # log log log T

    # Fit means = a * L + b * LL + c. FHK predicts a = 1, b = -3/4.
    A = np.column_stack([L, LL, np.ones_like(L)])
    coef, *_ = np.linalg.lstsq(A, means, rcond=None)
    a, b, c = coef
    print("\nLeast-squares fit  E[max] = a * log log T + b * log log log T + c")
    print(f"  a = {a:+.4f}  (FHK prediction: 1)")
    print(f"  b = {b:+.4f}  (FHK prediction: -0.75)")
    print(f"  c = {c:+.4f}")

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.errorbar(L, means, yerr=stds / max(1, math.sqrt(N_CENTERS)),
                fmt="o", color="C0", capsize=4, label="data (mean +/- sem)")
    L_fine = np.linspace(L.min() - 0.2, L.max() + 0.2, 200)
    # L = log log T, so log log log T = log L.
    LL_fine = np.log(L_fine)
    ax.plot(L_fine, a * L_fine + b * LL_fine + c, "-", color="C0",
            label=f"fit: {a:+.3f}*LL {b:+.3f}*LLL {c:+.3f}")
    ax.plot(L_fine, L_fine - 0.75 * LL_fine + c, "--", color="C3",
            label="FHK: LL - 0.75*LLL + c")
    ax.set_xlabel("L = log log T")
    ax.set_ylabel("mean window max of log|zeta(1/2 + it)|")
    ax.set_title("E2: FHK second-order fit")
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()

    out = THIS_DIR / "e2_fhk_max_fit.png"
    fig.savefig(out, dpi=130)
    print(f"saved {out}")


if __name__ == "__main__":
    main()
