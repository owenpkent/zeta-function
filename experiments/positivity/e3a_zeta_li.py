"""Experiment 3A: zeta Li coefficients up to n_max.

Li (1997): RH is equivalent to lambda_n >= 0 for all n >= 1, where
    lambda_n = sum_rho [1 - (1 - 1/rho)^n]
and the sum runs over non-trivial zeros rho, paired with conjugates.

Bombieri-Lagarias (1999): under RH,
    lambda_n = (n/2)(log n + 1 - gamma_E - log(2 pi)) + O(sqrt(n) log n)
The oscillating remainder of order sqrt(n) log n carries arithmetic
information (it is a sum over zeros with rapidly oscillating phases).

Algorithm: incremental product. For each zero rho compute
    w_rho = 1 - 1/rho
which lies on the unit circle for rho on the critical line. We maintain
power[k] = w_{rho_k}^n and update by multiplication, so total work is
O(n_max * |zeros|) multiplications rather than O(n_max * |zeros|) complex
powers from scratch.

Truncation: missing tail (zeros with gamma > T) contributes about
n^2 (log T)/T. For our defaults, this is small relative to lambda_n at
moderate n. The truncation will be visible at very small n (where
lambda_n itself is small) and is the dominant source of error there.

Outputs:
  - e3a_zeta_li.npz: arrays of n, lambda_n, predicted, residual
  - e3a_zeta_li.png: lambda_n vs n, residual, log-log
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

from experiments._shared import zeta_L


GAMMA_E = 0.5772156649015329
ASYMP_CONST = 0.5 * (1 - GAMMA_E - np.log(2 * np.pi))  # ~ -0.7075


def bombieri_lagarias_prediction(n_array):
    """Leading-order RH asymptotic: lambda_n ~ (n/2) log n + ASYMP_CONST * n."""
    return 0.5 * n_array * np.log(np.maximum(n_array, 1)) + ASYMP_CONST * n_array


def compute_li_coefficients(rhos, n_max: int, prec: int = 30):
    """Incremental Li coefficients up to n_max.

    Each rho in rhos should be an mp.mpc with positive imaginary part.
    Pairs with conjugates implicitly via 2 * Re.

    Returns (lambdas, w_magnitudes) where lambdas is a list of mp.mpf
    values and w_magnitudes is the list of |1 - 1/rho| (diagnostic).
    """
    mp.mp.dps = prec
    one = mp.mpf(1)
    w = [one - one / rho for rho in rhos]
    w_mag = [float(abs(wi)) for wi in w]
    power = list(w)
    lambdas = []
    for n in range(1, n_max + 1):
        s = mp.mpf(0)
        for pk in power:
            s += (one - pk).real
        lambdas.append(2 * s)
        if n < n_max:
            for k in range(len(power)):
                power[k] = power[k] * w[k]
    return lambdas, w_mag


def run(n_max: int = 200, T_max: float = 500.0, prec: int = 30, out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"[3A] Loading zeta zeros up to T = {T_max} at {prec} dps...")
    t0 = time.time()
    rhos = zeta_L.zeros(T_max=T_max, prec=prec)
    t_zeros = time.time() - t0
    print(f"     Got {len(rhos)} zeros in {t_zeros:.1f}s")

    print(f"[3A] Computing Li coefficients up to n = {n_max} ...")
    t0 = time.time()
    lambdas_mp, w_mag = compute_li_coefficients(rhos, n_max, prec=prec)
    t_li = time.time() - t0
    print(f"     Computed in {t_li:.1f}s")
    print(f"     |1 - 1/rho| range: [{min(w_mag):.15f}, {max(w_mag):.15f}] (expect ~1.0)")

    lambdas = np.array([float(li) for li in lambdas_mp])
    ns = np.arange(1, n_max + 1, dtype=float)
    predicted = bombieri_lagarias_prediction(ns)
    residual = lambdas - predicted

    # Positivity check
    neg_mask = lambdas < 0
    n_neg = int(neg_mask.sum())
    print(f"[3A] Positivity: {n_neg} of {n_max} negative ({100*n_neg/n_max:.2f}%)")
    if n_neg == 0:
        print("     All lambda_n >= 0  (consistent with RH)")
    else:
        first_neg = int(np.argmax(neg_mask))
        print(f"     First negative at n = {first_neg + 1}: lambda = {lambdas[first_neg]:.6e}")
        print(f"     (Expected at very small n as a truncation artifact when T is small.)")

    # First few values
    print("[3A] First 10 lambda_n:")
    for k in range(min(10, n_max)):
        print(f"     lambda_{k+1:>3} = {lambdas[k]:+.6e}   predicted = {predicted[k]:+.6e}")

    # Linear fit to lambda_n / n vs log n to extract the asymptotic constant
    # lambda_n / n ~ (1/2) log n + c  =>  fit slope ~ 0.5 and intercept ~ c
    if n_max >= 50:
        mask_fit = ns >= max(20, n_max // 4)  # use upper portion for asymptotic
        x_fit = np.log(ns[mask_fit])
        y_fit = lambdas[mask_fit] / ns[mask_fit]
        slope, intercept = np.polyfit(x_fit, y_fit, 1)
        print(f"[3A] Asymptotic fit (n >= {int(ns[mask_fit][0])}): "
              f"lambda_n / n ~ {slope:.4f} * log n + {intercept:+.4f}")
        print(f"     Expected: slope = 0.5, intercept = {ASYMP_CONST:+.4f}")
        print(f"     Slope error: {(slope - 0.5):+.4f}; "
              f"intercept error: {(intercept - ASYMP_CONST):+.4f}")

    np.savez_compressed(
        out_dir / "e3a_zeta_li.npz",
        n=ns.astype(int),
        lambda_=lambdas,
        predicted=predicted,
        residual=residual,
        T_max=T_max,
        prec=prec,
        n_zeros=len(rhos),
    )

    fig, axs = plt.subplots(1, 3, figsize=(15, 4.5))

    axs[0].plot(ns, lambdas, "b-", label="lambda_n (computed)")
    axs[0].plot(ns, predicted, "r--", label="B-L leading order")
    axs[0].axhline(0, color="k", linewidth=0.5)
    axs[0].set_xlabel("n")
    axs[0].set_ylabel("lambda_n")
    axs[0].set_title(f"Zeta Li coefficients\n(T_max={T_max:.0f}, |zeros|={len(rhos)})")
    axs[0].legend()
    axs[0].grid(alpha=0.3)

    axs[1].plot(ns, residual, "g-")
    axs[1].axhline(0, color="k", linewidth=0.5)
    axs[1].set_xlabel("n")
    axs[1].set_ylabel("lambda_n - prediction")
    axs[1].set_title("Residual vs leading order\n(should be O(sqrt(n) log n))")
    axs[1].grid(alpha=0.3)

    pos_mask = lambdas > 0
    if pos_mask.any():
        axs[2].loglog(ns[pos_mask], lambdas[pos_mask], "b-", label="lambda_n")
        axs[2].loglog(ns, 0.5 * ns * np.log(np.maximum(ns, 2)), "r--",
                      label="(n/2) log n")
    axs[2].set_xlabel("n")
    axs[2].set_ylabel("lambda_n")
    axs[2].set_title("Log-log growth")
    axs[2].legend()
    axs[2].grid(alpha=0.3, which="both")

    plt.tight_layout()
    plt.savefig(out_dir / "e3a_zeta_li.png", dpi=140)
    plt.close()
    print(f"[3A] Saved {out_dir / 'e3a_zeta_li.png'}")
    print(f"[3A] Saved {out_dir / 'e3a_zeta_li.npz'}")

    return lambdas, predicted, residual


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-max", type=int, default=200)
    parser.add_argument("--T-max", type=float, default=500.0)
    parser.add_argument("--prec", type=int, default=30)
    args = parser.parse_args()
    run(n_max=args.n_max, T_max=args.T_max, prec=args.prec)
