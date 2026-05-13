"""E3: MFDFA on the normalized Chebyshev fluctuation Y(u) = (psi(e^u) - e^u)/e^(u/2).

This is the fastest of the three experiments and the one closest to the
question "is the multifractal structure on the critical line just a
representation of the primes?". If Y(u) shows multifractal scaling similar
to log|zeta(1/2+it)| on a unit window, the answer is "yes, by the explicit
formula." If not, the duality is more subtle than the heuristics suggest.

Run:
    python experiments/multifractal/e3_psi_mfdfa.py

Output:
    e3_psi_mfdfa.png    plots
    stdout              numerical summary
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(THIS_DIR))

from mfdfa import mfdfa, hurst_summary  # noqa: E402
from prime_data import normalized_psi_fluctuation  # noqa: E402


def main(x_max=10**7, num_points=8192, order=3, x_min=100.0):
    print(f"E3: MFDFA on (psi(x) - x)/sqrt(x), x in [{x_min:g}, {x_max:g}], "
          f"{num_points} log-uniform samples, detrend order={order}")

    us, Y = normalized_psi_fluctuation(
        x_max=x_max, num_points=num_points, x_min=x_min,
    )
    print(f"  series length N = {Y.size}")
    print(f"  mean = {Y.mean():+.4f}, std = {Y.std():.4f}, "
          f"range = [{Y.min():+.4f}, {Y.max():+.4f}]")

    scales = np.unique(np.logspace(np.log10(16), np.log10(Y.size // 4), 24).astype(int))
    q_values = np.linspace(-4.0, 4.0, 17)
    result = mfdfa(Y, scales=scales, q_values=q_values, order=order)

    print("  " + hurst_summary(result))

    fig, axes = plt.subplots(2, 2, figsize=(12, 9))

    ax = axes[0, 0]
    ax.plot(us, Y, lw=0.7)
    ax.set_xlabel("u = log x")
    ax.set_ylabel(r"$(\psi(e^u) - e^u)/e^{u/2}$")
    ax.set_title("Normalized Chebyshev fluctuation")
    ax.grid(True, alpha=0.3)

    ax = axes[0, 1]
    q_idx_show = [0, 4, 8, 12, 16]
    for j in q_idx_show:
        ax.loglog(result["scales"], result["F"][:, j], "o-", ms=4,
                  label=f"q = {result['q'][j]:+.1f}")
    ax.set_xlabel("scale s (samples)")
    ax.set_ylabel(r"$F_q(s)$")
    ax.set_title("Fluctuation function")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3, which="both")

    ax = axes[1, 0]
    ax.plot(result["q"], result["h"], "o-", color="C2")
    ax.axhline(0.5, color="k", ls="--", lw=0.8, alpha=0.6,
               label="monofractal H = 0.5")
    ax.set_xlabel("q")
    ax.set_ylabel("h(q)")
    ax.set_title("Generalized Hurst exponent")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    ax = axes[1, 1]
    ax.plot(result["alpha"], result["D_alpha"], "o-", color="C3")
    ax.set_xlabel(r"$\alpha$")
    ax.set_ylabel(r"$D(\alpha)$")
    ax.set_title("Singularity spectrum")
    ax.grid(True, alpha=0.3)

    fig.suptitle(
        f"E3: MFDFA on Chebyshev fluctuation  (x up to {x_max:g}, N={Y.size})",
        fontsize=12,
    )
    fig.tight_layout()

    out = THIS_DIR / "e3_psi_mfdfa.png"
    fig.savefig(out, dpi=130)
    print(f"  saved {out}")

    print("\n  h(q):")
    for q, h in zip(result["q"], result["h"]):
        print(f"    h({q:+.1f}) = {h:.4f}")


if __name__ == "__main__":
    main()
