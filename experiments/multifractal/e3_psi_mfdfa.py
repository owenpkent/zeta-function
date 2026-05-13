"""E3: MFDFA on the normalized Chebyshev fluctuation Y(u) = (psi(e^u) - e^u)/e^(u/2).

Two variants run side by side:
  - values:     MFDFA on Y(u) directly. (Earlier runs gave h(q) > 1 because
                 Y is a quasi-periodic sum of bounded oscillations whose
                 cumulative profile is too smooth.)
  - increments: MFDFA on Delta Y. This removes the slowly-varying envelope
                 and exposes the high-frequency content directly. Comparable
                 to E1 with one fewer integration.

If the increment spectrum width agrees with E1 (~ 2.05), the explicit-formula
duality is empirically supported: the multifractal "fractal" on the critical
line is the same object as the high-frequency fluctuations of the primes.

Run:
    python experiments/multifractal/e3_psi_mfdfa.py

Output:
    e3_psi_mfdfa.png    plots
    stdout              numerical summary
"""

from __future__ import annotations

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
    print(f"  Y: mean = {Y.mean():+.4f}, std = {Y.std():.4f}, "
          f"range = [{Y.min():+.4f}, {Y.max():+.4f}]")

    dY = np.diff(Y)
    print(f"  dY: mean = {dY.mean():+.4f}, std = {dY.std():.4f}, "
          f"range = [{dY.min():+.4f}, {dY.max():+.4f}]")

    scales = np.unique(np.logspace(np.log10(16), np.log10(Y.size // 4), 24).astype(int))
    q_values = np.linspace(-4.0, 4.0, 17)
    res_val = mfdfa(Y, scales=scales, q_values=q_values, order=order)
    res_inc = mfdfa(dY, scales=scales, q_values=q_values, order=order)

    print("  values:     " + hurst_summary(res_val))
    print("  increments: " + hurst_summary(res_inc))

    fig, axes = plt.subplots(2, 2, figsize=(13, 9))

    ax = axes[0, 0]
    ax.plot(us, Y, lw=0.7, label="Y(u)")
    ax2 = ax.twinx()
    ax2.plot(us[1:], dY, lw=0.5, color="C1", alpha=0.7, label=r"$\Delta Y$")
    ax.set_xlabel("u = log x")
    ax.set_ylabel(r"$Y(u) = (\psi(e^u) - e^u)/e^{u/2}$", color="C0")
    ax2.set_ylabel(r"$\Delta Y$", color="C1")
    ax.set_title("Normalized Chebyshev fluctuation and increments")
    ax.grid(True, alpha=0.3)

    ax = axes[0, 1]
    for j in [0, 4, 8, 12, 16]:
        ax.loglog(res_val["scales"], res_val["F"][:, j], "o-", ms=3,
                  alpha=0.6, label=f"values, q = {res_val['q'][j]:+.1f}")
    ax.set_xlabel("scale s")
    ax.set_ylabel(r"$F_q(s)$ on values")
    ax.set_title("Fluctuation function")
    ax.legend(fontsize=7, ncol=2)
    ax.grid(True, alpha=0.3, which="both")

    ax = axes[1, 0]
    ax.plot(res_val["q"], res_val["h"], "o-", color="C2", label="values")
    ax.plot(res_inc["q"], res_inc["h"], "s-", color="C4", label="increments")
    ax.axhline(0.5, color="k", ls="--", lw=0.8, alpha=0.6,
               label="monofractal H = 0.5")
    ax.set_xlabel("q")
    ax.set_ylabel("h(q)")
    ax.set_title("Generalized Hurst exponent")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    ax = axes[1, 1]
    ax.plot(res_val["alpha"], res_val["D_alpha"], "o-", color="C2",
            label="values")
    ax.plot(res_inc["alpha"], res_inc["D_alpha"], "s-", color="C4",
            label="increments")
    ax.set_xlabel(r"$\alpha$")
    ax.set_ylabel(r"$D(\alpha)$")
    ax.set_title("Singularity spectrum")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    fig.suptitle(
        f"E3: MFDFA on Chebyshev fluctuation, values vs increments  "
        f"(x in [{x_min:g}, {x_max:g}], N={Y.size})",
        fontsize=12,
    )
    fig.tight_layout()

    out = THIS_DIR / "e3_psi_mfdfa.png"
    fig.savefig(out, dpi=130)
    print(f"  saved {out}")

    print("\n  q     h_values   h_increments")
    for q, hv, hi in zip(res_val["q"], res_val["h"], res_inc["h"]):
        print(f"  {q:+.1f}    {hv:+.4f}    {hi:+.4f}")


if __name__ == "__main__":
    main()
