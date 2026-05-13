"""E0: Calibrate MFDFA against three synthetic series with known scaling.

  1. White noise (iid Gaussian).  Expected h(q) = 0.5 const.
  2. Fractional Gaussian noise, Hurst H = 0.7.  Expected h(q) = 0.7 const.
  3. p-binomial multiplicative cascade, p = 0.3.  Multifractal; h(q) varies.

For 1 and 2 the spread in h(q) measures pipeline noise: anything more than a
few hundredths is spurious multifractality from finite-sample effects, not
real structure. For 3 we overlay the closed-form theoretical h(q).

Run:
    python experiments/multifractal/e0_benchmarks.py

Output:
    e0_benchmarks.png    plot grid: series, F_q(s), h(q), D(alpha) for each
    stdout               summary table
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(THIS_DIR))

from benchmarks import (  # noqa: E402
    binomial_cascade,
    binomial_cascade_theory,
    fgn_spectral,
    white_noise,
)
from mfdfa import mfdfa  # noqa: E402


N_DEFAULT = 8192
ORDER = 3
SEED = 42

CASES = [
    ("white_noise", "white noise (iid)",   {}),
    ("fgn",         "fGn, H = 0.7",        {"H": 0.7}),
    ("cascade",     "binomial cascade, p = 0.3", {"p": 0.3}),
]


def make_series(name, N, rng, kwargs):
    if name == "white_noise":
        return white_noise(N, rng=rng)
    if name == "fgn":
        return fgn_spectral(N, H=kwargs["H"], rng=rng)
    if name == "cascade":
        levels = int(np.log2(N))
        return binomial_cascade(p=kwargs["p"], levels=levels, rng=rng)
    raise ValueError(name)


def main():
    rng = np.random.default_rng(SEED)
    q_values = np.linspace(-4.0, 4.0, 17)
    scales = np.unique(np.logspace(np.log10(16), np.log10(N_DEFAULT // 4), 24).astype(int))

    fig, axes = plt.subplots(len(CASES), 3, figsize=(13, 9))
    print(f"E0: MFDFA on synthetic benchmarks (N={N_DEFAULT}, order={ORDER})")
    print(f"{'case':30s}  {'h(q=2)':>9s}  {'alpha width':>12s}")
    print("-" * 60)

    for row, (name, label, kwargs) in enumerate(CASES):
        series = make_series(name, N_DEFAULT, rng, kwargs)
        result = mfdfa(series, scales=scales, q_values=q_values, order=ORDER)
        h_at_2 = float(np.interp(2.0, result["q"], result["h"]))
        a_width = float(result["alpha"].max() - result["alpha"].min())
        print(f"{label:30s}  {h_at_2:+9.4f}  {a_width:12.4f}")

        ax = axes[row, 0]
        ax.plot(series, lw=0.5)
        ax.set_title(label)
        ax.set_xlabel("index")
        ax.grid(True, alpha=0.3)

        ax = axes[row, 1]
        ax.plot(result["q"], result["h"], "o-", color="C0", label="MFDFA")
        if name == "white_noise":
            ax.axhline(0.5, color="k", ls="--", lw=0.8, label="theory: 0.5")
        elif name == "fgn":
            ax.axhline(kwargs["H"], color="k", ls="--", lw=0.8,
                       label=f"theory: H = {kwargs['H']}")
        elif name == "cascade":
            _, h_theory = binomial_cascade_theory(kwargs["p"], result["q"])
            ax.plot(result["q"], h_theory, "x--", color="k", lw=1.0,
                    label=f"theory: p = {kwargs['p']}")
        ax.set_xlabel("q")
        ax.set_ylabel("h(q)")
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3)

        ax = axes[row, 2]
        ax.plot(result["alpha"], result["D_alpha"], "o-", color="C3")
        ax.set_xlabel(r"$\alpha$")
        ax.set_ylabel(r"$D(\alpha)$")
        ax.grid(True, alpha=0.3)

    fig.suptitle("E0: MFDFA calibration on synthetic series", fontsize=12)
    fig.tight_layout()
    out = THIS_DIR / "e0_benchmarks.png"
    fig.savefig(out, dpi=130)
    print(f"\nsaved {out}")


if __name__ == "__main__":
    main()
