"""E1: MFDFA on log|zeta(1/2 + it)| in unit windows around several heights T.

For each T in HEIGHTS, sample log|zeta(1/2+it)| on [T - 1/2, T + 1/2] and run
MFDFA. The hypothesis (Fyodorov-Hiary-Keating + Saksman-Webb) is that this
series is a 1D log-correlated Gaussian field with a quadratic multifractal
spectrum.

This is the slow experiment. mpmath zeta evaluation dominates. The on-disk
cache in _cache/ avoids redoing the same window across runs.

Run:
    python experiments/multifractal/e1_zeta_mfdfa.py
"""

from __future__ import annotations

import sys
import time
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(THIS_DIR))

from mfdfa import mfdfa, hurst_summary  # noqa: E402
from zeta_sampling import sample_log_zeta_window  # noqa: E402


# Conservative defaults so a first run finishes in minutes, not hours.
HEIGHTS = [1.0e4, 1.0e6, 1.0e8]
NUM_POINTS = 2048
WINDOW = 1.0
PREC = 30


def run_one(T, num_points=NUM_POINTS, window=WINDOW, prec=PREC, order=2):
    t0 = time.time()
    ts, log_abs = sample_log_zeta_window(
        T_center=T, window=window, num_points=num_points, prec=prec,
    )
    dt = time.time() - t0
    print(f"  T = {T:.3g}: sampled {num_points} points in {dt:.1f}s "
          f"(mean log|zeta| = {log_abs.mean():+.4f}, std = {log_abs.std():.4f})")

    scales = np.unique(np.logspace(np.log10(16), np.log10(num_points // 4), 18).astype(int))
    q_values = np.linspace(-4.0, 4.0, 17)
    result = mfdfa(log_abs, scales=scales, q_values=q_values, order=order)
    print("    " + hurst_summary(result))
    return ts, log_abs, result


def main():
    print(f"E1: MFDFA on log|zeta(1/2 + it)| at heights {HEIGHTS}")
    runs = [run_one(T) for T in HEIGHTS]

    fig, axes = plt.subplots(2, 2, figsize=(13, 10))

    ax = axes[0, 0]
    for (ts, log_abs, _), T in zip(runs, HEIGHTS):
        ax.plot(ts - T, log_abs, lw=0.7, alpha=0.8, label=f"T = {T:.0g}")
    ax.set_xlabel(r"$h = t - T$")
    ax.set_ylabel(r"$\log|\zeta(1/2 + it)|$")
    ax.set_title("Window samples")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    ax = axes[0, 1]
    for (_, _, result), T in zip(runs, HEIGHTS):
        ax.loglog(result["scales"], result["F"][:, result["q"].size // 2 + 2],
                  "o-", ms=4, label=f"T = {T:.0g}")
    ax.set_xlabel("scale s (samples)")
    ax.set_ylabel(r"$F_q(s)$ at $q = 1$")
    ax.set_title("Fluctuation function")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3, which="both")

    ax = axes[1, 0]
    for (_, _, result), T in zip(runs, HEIGHTS):
        ax.plot(result["q"], result["h"], "o-", label=f"T = {T:.0g}")
    ax.axhline(0.5, color="k", ls="--", lw=0.8, alpha=0.6,
               label="monofractal H = 0.5")
    ax.set_xlabel("q")
    ax.set_ylabel("h(q)")
    ax.set_title("Generalized Hurst exponent")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    ax = axes[1, 1]
    for (_, _, result), T in zip(runs, HEIGHTS):
        ax.plot(result["alpha"], result["D_alpha"], "o-", label=f"T = {T:.0g}")
    ax.set_xlabel(r"$\alpha$")
    ax.set_ylabel(r"$D(\alpha)$")
    ax.set_title("Singularity spectrum")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    fig.suptitle(
        f"E1: MFDFA on log|zeta(1/2+it)| in unit windows (N={NUM_POINTS})",
        fontsize=12,
    )
    fig.tight_layout()

    out = THIS_DIR / "e1_zeta_mfdfa.png"
    fig.savefig(out, dpi=130)
    print(f"saved {out}")


if __name__ == "__main__":
    main()
