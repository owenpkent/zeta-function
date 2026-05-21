"""Experiment 3B: per-zero Li-contribution diagnostic for D-H vs zeta.

Asks: does the zero-sum Li-coefficient method distinguish zeta from
Davenport-Heilbronn at computationally reachable n?

Setup: same incremental product algorithm as 3A, applied to both zeta
and D-H, with the same n range and same T_max for fair comparison.

Structural fact: for rho on the critical line, |1 - 1/rho| = 1 exactly.
For off-line zero rho = beta + i*gamma:
    |1 - 1/rho|^2 - 1 = (1 - 2 beta) / (beta^2 + gamma^2)
First D-H off-line zero: rho_+ = 0.808 + 85.7 i gives
    |w|^2 - 1 ~ -8.4e-5  =>  |w| ~ 1 - 4.2e-5
Functional-equation partner rho_- = 0.192 + 85.7 i gives
    |w| ~ 1 + 4.2e-5
So |w|^n deviates from 1 by ~4e-5 at n=1 and ~4e-1 at n=10000. Off-line
contribution becomes order-1 only around n ~ 1/log(1+4e-5) ~ 25000.

Hypothesis (to verify): naive Li-positivity at n <= a few thousand does
NOT distinguish zeta from D-H. Both will show lambda_n > 0. This means
the small-n Li criterion is not a valid wrong-approach detector; we
need a structurally different diagnostic (the Weil quadratic form,
covered in 3C) or to reach much larger n via the xi-derivative formula.

Outputs:
  - e3b_dh_li.npz: side-by-side Li coefficients, |w| values
  - e3b_dh_li.png: 4-panel plot:
      (1) histogram of |w_rho| - 1 for zeta and D-H
      (2) lambda_n curves for both
      (3) cumulative partial sums vs zero count
      (4) per-zero contribution to lambda_n at fixed n (off-line zeros
          highlighted)
"""

from __future__ import annotations

import argparse
import time
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np

from experiments._shared import zeta_L, DavenportHeilbronn
from experiments.positivity.e3a_zeta_li import (
    compute_li_coefficients,
    bombieri_lagarias_prediction,
)


def crossover_estimate(w_offline):
    """Estimate n at which off-line contribution becomes order 1.

    For |w| = 1 + eps with eps small, |w|^n - 1 ~ n*eps. Order-1 when
    n ~ 1/eps.
    """
    if not w_offline:
        return None
    max_dev = max(float(abs(abs(w) - 1)) for w in w_offline)
    if max_dev <= 0:
        return None
    return 1.0 / max_dev


def run(n_max: int = 300, T_max: float = 200.0, prec: int = 30,
        out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    dh = DavenportHeilbronn()

    print(f"[3B] Loading zeros up to T = {T_max} at {prec} dps for both L-functions...")
    t0 = time.time()
    zeta_rhos = zeta_L.zeros(T_max=T_max, prec=prec)
    print(f"     zeta: {len(zeta_rhos)} zeros in {time.time() - t0:.1f}s")
    t0 = time.time()
    dh_rhos = dh.zeros(T_max=T_max, prec=prec, scan_step=0.5)
    print(f"     D-H:  {len(dh_rhos)} zeros in {time.time() - t0:.1f}s")

    # |w_rho| diagnostic
    one = mp.mpf(1)
    zeta_w_dev = np.array([float(abs(one - one / r) - 1) for r in zeta_rhos])
    dh_w_dev = np.array([float(abs(one - one / r) - 1) for r in dh_rhos])
    dh_offline_mask = np.array([abs(float(r.real) - 0.5) > 0.01 for r in dh_rhos])
    print(f"[3B] |w| - 1 statistics:")
    print(f"     zeta: max |dev| = {np.max(np.abs(zeta_w_dev)):.2e} (expected 0; what we see is float noise)")
    print(f"     D-H:  max |dev| = {np.max(np.abs(dh_w_dev)):.2e} on {int(dh_offline_mask.sum())} off-line zeros")

    if dh_offline_mask.any():
        offline_w = [one - one / r for r in np.array(dh_rhos)[dh_offline_mask]]
        n_cross = crossover_estimate(offline_w)
        print(f"     D-H off-line |w| values: {[float(abs(w)) for w in offline_w]}")
        print(f"     Predicted crossover (off-line dominates): n ~ {n_cross:.0f}")

    # Li coefficients via zero sum
    print(f"[3B] Computing Li coefficients up to n = {n_max} ...")
    t0 = time.time()
    lambdas_zeta_mp, _ = compute_li_coefficients(zeta_rhos, n_max, prec=prec)
    print(f"     zeta in {time.time() - t0:.1f}s")
    t0 = time.time()
    lambdas_dh_mp, _ = compute_li_coefficients(dh_rhos, n_max, prec=prec)
    print(f"     D-H  in {time.time() - t0:.1f}s")

    lambdas_zeta = np.array([float(x) for x in lambdas_zeta_mp])
    lambdas_dh = np.array([float(x) for x in lambdas_dh_mp])
    ns = np.arange(1, n_max + 1, dtype=float)

    # Positivity report
    zeta_neg = int((lambdas_zeta < 0).sum())
    dh_neg = int((lambdas_dh < 0).sum())
    print(f"[3B] Positivity over n = 1..{n_max}:")
    print(f"     zeta: {zeta_neg}/{n_max} negative")
    print(f"     D-H:  {dh_neg}/{n_max} negative")
    if zeta_neg == 0 and dh_neg == 0:
        print("     KEY FINDING: both L-functions show all lambda_n >= 0 at small n.")
        print("     Li-positivity at small n is NOT a wrong-approach detector.")
        print("     The D-H off-line zero contribution scale (|w| - 1 ~ 4e-5) means")
        print("     visible negativity requires n ~ 1/(|w|-1) ~ 25000, beyond reach")
        print("     for the zero-sum method.")

    # Per-zero contributions at a sampled n
    n_sample = min(n_max, 100)
    contrib_zeta = []
    for rho in zeta_rhos:
        w = one - one / rho
        contrib_zeta.append(float((one - w ** n_sample).real * 2))
    contrib_dh = []
    for rho in dh_rhos:
        w = one - one / rho
        contrib_dh.append(float((one - w ** n_sample).real * 2))
    contrib_zeta = np.array(contrib_zeta)
    contrib_dh = np.array(contrib_dh)

    # Save
    np.savez_compressed(
        out_dir / "e3b_dh_li.npz",
        n=ns.astype(int),
        lambda_zeta=lambdas_zeta,
        lambda_dh=lambdas_dh,
        zeta_w_dev=zeta_w_dev,
        dh_w_dev=dh_w_dev,
        dh_offline_mask=dh_offline_mask,
        zeta_contrib_at_n=contrib_zeta,
        dh_contrib_at_n=contrib_dh,
        n_sample=n_sample,
        T_max=T_max,
        prec=prec,
    )

    # Plot
    fig, axs = plt.subplots(2, 2, figsize=(13, 9))

    # (1) |w| - 1 distribution
    ax = axs[0, 0]
    ax.scatter(range(len(zeta_w_dev)), zeta_w_dev, s=10, c="b", label="zeta", alpha=0.7)
    ax.scatter(range(len(dh_w_dev)), dh_w_dev, s=10, c="r", label="D-H", alpha=0.7)
    if dh_offline_mask.any():
        idx = np.where(dh_offline_mask)[0]
        ax.scatter(idx, dh_w_dev[dh_offline_mask], s=80, c="r", marker="x",
                   label="D-H off-line")
    ax.axhline(0, color="k", linewidth=0.5)
    ax.set_yscale("symlog", linthresh=1e-10)
    ax.set_xlabel("zero index (ordered by gamma)")
    ax.set_ylabel(r"$|w_\rho| - 1$")
    ax.set_title("|w| - 1: on-line zeros have |w|=1 exactly")
    ax.legend()
    ax.grid(alpha=0.3)

    # (2) lambda_n curves
    ax = axs[0, 1]
    ax.plot(ns, lambdas_zeta, "b-", label="zeta", linewidth=1.2)
    ax.plot(ns, lambdas_dh, "r-", label="D-H", linewidth=1.2)
    ax.axhline(0, color="k", linewidth=0.5)
    ax.set_xlabel("n")
    ax.set_ylabel(r"$\lambda_n$")
    ax.set_title(f"Li coefficients (both positive in n <= {n_max})")
    ax.legend()
    ax.grid(alpha=0.3)

    # (3) difference lambda_n^DH - lambda_n^zeta
    ax = axs[1, 0]
    diff = lambdas_dh - lambdas_zeta
    ax.plot(ns, diff, "g-", linewidth=1.2)
    ax.axhline(0, color="k", linewidth=0.5)
    ax.set_xlabel("n")
    ax.set_ylabel(r"$\lambda_n^{DH} - \lambda_n^{\zeta}$")
    ax.set_title("D-H - zeta: off-line contribution structure")
    ax.grid(alpha=0.3)

    # (4) per-zero contribution at n_sample (highlight off-line zeros)
    ax = axs[1, 1]
    zeta_gammas = np.array([float(r.imag) for r in zeta_rhos])
    dh_gammas = np.array([float(r.imag) for r in dh_rhos])
    ax.scatter(zeta_gammas, contrib_zeta, s=15, c="b", label="zeta", alpha=0.6)
    ax.scatter(dh_gammas, contrib_dh, s=15, c="r", label="D-H on-line", alpha=0.6)
    if dh_offline_mask.any():
        ax.scatter(dh_gammas[dh_offline_mask], contrib_dh[dh_offline_mask],
                   s=120, c="r", marker="x", linewidth=2, label="D-H off-line",
                   zorder=10)
    ax.axhline(0, color="k", linewidth=0.5)
    ax.set_xlabel(r"$\gamma$ (imaginary part of zero)")
    ax.set_ylabel(rf"contribution to $\lambda_{{{n_sample}}}$ per zero")
    ax.set_title(f"Per-zero contribution at n = {n_sample}")
    ax.legend()
    ax.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig(out_dir / "e3b_dh_li.png", dpi=140)
    plt.close()
    print(f"[3B] Saved {out_dir / 'e3b_dh_li.png'}")
    print(f"[3B] Saved {out_dir / 'e3b_dh_li.npz'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-max", type=int, default=300)
    parser.add_argument("--T-max", type=float, default=200.0)
    parser.add_argument("--prec", type=int, default=30)
    args = parser.parse_args()
    run(n_max=args.n_max, T_max=args.T_max, prec=args.prec)
