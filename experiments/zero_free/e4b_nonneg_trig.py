"""Experiment 4B: Non-negative trigonometric polynomial optimization.

The classical Hadamard / de la Vallée Poussin zero-free region argument
uses the inequality

    3 + 4 cos(theta) + cos(2 theta) >= 0     for all theta

which is the polynomial (1 + cos(theta))^2 * 2 in disguise. Combined
with the explicit-formula identity

    -Re zeta'/zeta(sigma + it) = sum_n Lambda(n) n^{-sigma} cos(t log n)

it gives a zero-free region. The 'strength' of the inequality, i.e.,
how close to 1 we can push sigma, depends on the ratio c_1 / c_0 in
a non-negative trigonometric polynomial
    P(theta) = c_0 + 2 sum_{k=1}^n c_k cos(k theta) >= 0.

For the classical degree-2 polynomial 3 + 4 cos + cos 2, c_1 / c_0 =
4 / (2 * 3) = 2/3.

Question (Fejér, 1915 onward): how large can c_1 / c_0 be at degree n?
Answer (asymptotic): cos(pi / (n + 2)) as n -> infinity, so the limit
is 1 but the approach is slow.

We solve the LP

    maximize  c_1
    subject to  c_0 = 1
                c_0 + 2 sum_{k=1}^n c_k cos(k theta) >= 0 at M sampled theta

for degrees n = 1, ..., n_max and compare to the Fejér bound. We also
record the OPTIMAL polynomial at each degree.

Application to the zero-free region: the de la Vallée Poussin constant
in the bound sigma >= 1 - c / log|t| depends linearly on c_1 / c_0
through a known formula. So improving c_1 / c_0 improves c, although
the basic functional FORM of the bound is unchanged. The exponent in
Vinogradov-Korobov (2/3 vs 1) is a DIFFERENT story; that comes from
exponential-sum estimates, not from trig-polynomial improvements.
"""

from __future__ import annotations

import argparse
import time
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import linprog


def best_trig_ratio(n: int, M: int = 4000):
    """LP: maximize c_1 over non-neg trig polynomials of degree n with c_0 = 1.

    P(theta) = c_0 + 2 sum_{k=1}^n c_k cos(k theta) >= 0 sampled at
    M uniform theta in [0, 2 pi).

    Returns (c_1_max, coefficient_vector_c).
    """
    theta = np.linspace(0, 2 * np.pi, M, endpoint=False)
    # Objective: maximize c_1 == minimize -c_1
    obj = np.zeros(n + 1)
    obj[1] = -1
    # Inequality constraint: -P <= 0, i.e., -c_0 - 2 sum c_k cos(k theta) <= 0
    A_ub = np.zeros((M, n + 1))
    A_ub[:, 0] = -1
    for k in range(1, n + 1):
        A_ub[:, k] = -2 * np.cos(k * theta)
    b_ub = np.zeros(M)
    # Equality: c_0 = 1
    A_eq = np.zeros((1, n + 1))
    A_eq[0, 0] = 1
    b_eq = np.array([1.0])
    # Bounds: coefficients can range; bound them generously
    bounds = [(-5.0, 5.0)] * (n + 1)
    res = linprog(
        obj,
        A_ub=A_ub,
        b_ub=b_ub,
        A_eq=A_eq,
        b_eq=b_eq,
        bounds=bounds,
        method="highs",
    )
    if not res.success:
        raise RuntimeError(f"LP failed at n={n}: {res.message}")
    return -res.fun, res.x


def verify_nonneg(c, M_test: int = 100000):
    """Verify the polynomial is non-negative on a dense theta sampling."""
    theta = np.linspace(0, 2 * np.pi, M_test, endpoint=False)
    P = np.full_like(theta, c[0])
    for k in range(1, len(c)):
        P += 2 * c[k] * np.cos(k * theta)
    return float(P.min()), float(P.max())


def run(n_max: int = 20, M: int = 4000, out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    degrees = list(range(1, n_max + 1))
    c1_values = []
    coeffs_by_degree = {}
    fejer_bounds = []

    print(f"[4B] Solving LPs for non-neg trig polynomials, degrees 1..{n_max}")
    print(f"     Sample count M = {M}")
    print(f"     {'degree':>6}   {'max c_1':>12}   {'Fejer bound':>12}   {'gap':>10}   "
          f"{'P_min':>12}   {'time':>6}")
    for n in degrees:
        t0 = time.time()
        c1, coeffs = best_trig_ratio(n, M=M)
        P_min, P_max = verify_nonneg(coeffs)
        fejer = np.cos(np.pi / (n + 2))
        c1_values.append(c1)
        coeffs_by_degree[n] = coeffs.copy()
        fejer_bounds.append(fejer)
        print(f"     {n:>6}   {c1:>12.8f}   {fejer:>12.8f}   {fejer - c1:>10.6f}   "
              f"{P_min:>12.4e}   {time.time() - t0:>4.1f}s")

    # Classical reference
    print("\n[4B] Classical comparison:")
    print(f"     3 + 4 cos + cos 2: P = 3 + 4 cos theta + 1 cos 2theta = 2(1 + cos theta)^2")
    print(f"     => c_0 = 3, c_1 = 2, c_2 = 1/2  (in the convention P = c_0 + 2 c_1 cos + 2 c_2 cos 2)")
    print(f"     Normalized to c_0 = 1: c_1 = 2/3 = {2/3:.8f}")
    print(f"     Our degree-2 LP result: c_1 = {c1_values[1]:.8f}")
    classical_match = abs(c1_values[1] - 2/3) < 1e-4
    print(f"     Match with classical: {classical_match}")

    np.savez_compressed(
        out_dir / "e4b_nonneg_trig.npz",
        degrees=np.array(degrees),
        c1_values=np.array(c1_values),
        fejer_bounds=np.array(fejer_bounds),
        M=M,
    )

    fig, axs = plt.subplots(1, 2, figsize=(13, 5))

    ax = axs[0]
    ax.plot(degrees, c1_values, "bo-", label=r"LP max $c_1$")
    ax.plot(degrees, fejer_bounds, "r--", label=r"Fejér bound $\cos(\pi/(n+2))$")
    ax.axhline(2 / 3, color="k", linestyle=":", label=r"classical $2/3$ at degree 2")
    ax.axhline(1.0, color="gray", linestyle=":", alpha=0.5, label="asymptotic limit")
    ax.set_xlabel("polynomial degree n")
    ax.set_ylabel(r"max $c_1$ (with $c_0 = 1$)")
    ax.set_title("Non-negative trig polynomial: max $c_1$ vs degree")
    ax.legend()
    ax.grid(alpha=0.3)
    ax.set_ylim(0, 1.05)

    ax = axs[1]
    gap = np.array(fejer_bounds) - np.array(c1_values)
    ax.semilogy(degrees, gap, "go-")
    ax.set_xlabel("polynomial degree n")
    ax.set_ylabel("Fejér bound - LP max (gap)")
    ax.set_title("LP saturates Fejér bound")
    ax.grid(alpha=0.3, which="both")

    plt.tight_layout()
    plt.savefig(out_dir / "e4b_nonneg_trig.png", dpi=140)
    plt.close()
    print(f"\n[4B] Saved {out_dir / 'e4b_nonneg_trig.png'}")
    print(f"[4B] Saved {out_dir / 'e4b_nonneg_trig.npz'}")

    # Print best polynomial at top degree
    n_best = n_max
    c_best = coeffs_by_degree[n_best]
    print(f"\n[4B] Best polynomial at degree {n_best} (c_0 = 1):")
    print(f"     c = {c_best}")
    print(f"     P(theta) = 1 + 2 * (" +
          " + ".join(f"{c_best[k]:+.5f} cos({k} theta)" for k in range(1, n_best + 1))
          + ")")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-max", type=int, default=20)
    parser.add_argument("--M", type=int, default=4000)
    args = parser.parse_args()
    run(n_max=args.n_max, M=args.M)
