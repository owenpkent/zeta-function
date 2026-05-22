"""Experiment 4E.4: Trivariate balanced-sum LP, extending 4E.2 to d = 3.

4E.2 found that the bivariate LP for max c_{1,1} + alpha c_{2,2} at
bidegree (2, 2) exceeds the Cauchy-Schwarz tensor bound by +25% at
alpha = 3, with clean rational LP-optimal coefficients. 4E.3 showed
that this 2D C-S gap does NOT translate into an improved Mossinghoff-
Trudgian zero-free region constant (single-zero, single-prime case
is bounded by 1D Fejer at matched effective degree).

The structural lemma of 4E.3 applies to any dimension d, so the
trivariate LP also cannot beat 1D Fejer for the MT framework. But
the structural question of whether the d-variate C-S gap grows or
shrinks with d is independent of that conclusion and worth measuring.

This experiment computes:

(a) For tridegree (2, 2, 2), the LP

      max c_{1,1,1} + alpha c_{2,2,2}
      subject to P(theta, phi, psi) = sum_{j,k,l} c_{j,k,l} cos(j theta)
                                       cos(k phi) cos(l psi) >= 0,
      c_{0,0,0} = 1.

(b) The symmetric tensor bound

      sup_Q (q_1^3 + alpha q_2^3) over 1D nonneg deg-N polys Q with
      q_0 = 1,

    obtained by 1D angle sweep on a sphere (q_1, q_2) → 1D LP.

(c) For each alpha in the sweep grid, the LP value, symmetric tensor
    bound, and the relative gap. Find the alpha that maximizes the
    relative gap, characterize the peak polynomial, and compare to
    the 4E.2 peak (alpha = 3, N = 2, gap = +25%).

The hypothesis (to be tested): the trivariate balanced-sum LP at
tridegree (2, 2, 2) has a peak gap at some alpha; either the gap
is larger than 25% (the higher-dimensional structure compounds the
2D non-decomposition), or it is smaller (the higher-dimensional
tensor bound is tighter).

Output:
  - e4e4_trivariate_sum.npz: alpha grid, LP/tensor values, peak
    coefficient tensor, M-convergence diagnostic
  - e4e4_trivariate_sum.png: LP-vs-tensor curves, gap vs alpha
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

from experiments.zero_free.e4e_offdiag_lp import best_1D_linear_obj


def best_trivariate_diag_sum(
    N: int, alpha: float, M: int = 30, bounds_abs: float = 20.0
):
    """LP: max c_{1,1,1} + alpha c_{2,2,2} over nonneg trivariate trig polys.

    P(theta, phi, psi) = sum_{0<=j,k,l<=N} c_{j,k,l} cos(j theta)
                          cos(k phi) cos(l psi) >= 0
    sampled on M x M x M uniform grid in [0, 2pi)^3, c_{0,0,0} = 1.

    Returns (LP value, coefficient tensor of shape (N+1)^3).
    """
    n_vars = (N + 1) ** 3
    theta = np.linspace(0, 2 * np.pi, M, endpoint=False)
    phi = np.linspace(0, 2 * np.pi, M, endpoint=False)
    psi = np.linspace(0, 2 * np.pi, M, endpoint=False)

    def idx(j, k, l):
        return j * (N + 1) ** 2 + k * (N + 1) + l

    obj = np.zeros(n_vars)
    obj[idx(1, 1, 1)] = -1.0
    if alpha != 0.0:
        obj[idx(2, 2, 2)] = -float(alpha)

    cos_j = np.array([np.cos(j * theta) for j in range(N + 1)])
    cos_k = np.array([np.cos(k * phi) for k in range(N + 1)])
    cos_l = np.array([np.cos(l * psi) for l in range(N + 1)])

    # Vectorized constraint construction (M^3 x n_vars)
    M3 = M ** 3
    A_ub = np.zeros((M3, n_vars))
    for j in range(N + 1):
        for k in range(N + 1):
            for l in range(N + 1):
                # Tensor outer product over the 3 directions
                outer = (
                    cos_j[j][:, None, None]
                    * cos_k[k][None, :, None]
                    * cos_l[l][None, None, :]
                ).flatten()
                A_ub[:, idx(j, k, l)] = -outer
    b_ub = np.zeros(M3)

    A_eq = np.zeros((1, n_vars))
    A_eq[0, idx(0, 0, 0)] = 1.0
    b_eq = np.array([1.0])

    bounds = [(-bounds_abs, bounds_abs)] * n_vars

    res = linprog(
        obj, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method="highs"
    )
    if not res.success:
        raise RuntimeError(f"3D LP failed at N={N}, alpha={alpha}: {res.message}")
    c_tensor = res.x.reshape((N + 1, N + 1, N + 1))
    return float(-res.fun), c_tensor


def verify_trivariate_nonneg(c_tensor, M_test: int = 60):
    """Verify P(theta, phi, psi) >= 0 on a fine grid.

    Returns (P_min, location of min).
    """
    N = c_tensor.shape[0] - 1
    theta = np.linspace(0, 2 * np.pi, M_test, endpoint=False)
    phi = np.linspace(0, 2 * np.pi, M_test, endpoint=False)
    psi = np.linspace(0, 2 * np.pi, M_test, endpoint=False)
    cos_j = np.array([np.cos(j * theta) for j in range(N + 1)])
    cos_k = np.array([np.cos(k * phi) for k in range(N + 1)])
    cos_l = np.array([np.cos(l * psi) for l in range(N + 1)])

    # Evaluate P via einsum
    P = np.einsum("jkl,ja,kb,lc->abc", c_tensor, cos_j, cos_k, cos_l)
    idx_min = np.unravel_index(np.argmin(P), P.shape)
    return float(P.min()), idx_min


def symmetric_tensor_bound_diag(
    N: int, alpha: float, M: int = 4000, M_angle: int = 720
):
    """Max_Q (q_1^3 + alpha q_2^3) over 1D nonneg deg-N polys with q_0 = 1.

    Parameterize via angle theta in [0, 2pi): max linear objective
        cos(theta) * q_1 + sin(theta) * cube_root(alpha) * q_2
    via 1D LP, return ((LP value)^3) but cube is harder; instead use:
    parameterize trade-off explicitly.

    For each angle theta, compute the 1D LP max cos(theta) q_1 +
    sin(theta) q_2 via 1D linear-obj LP. Then evaluate q_1^3 +
    alpha q_2^3 at the optimum and track the max.

    NOTE: this is an UPPER bound on the symmetric tensor bound
    (since the angle-parameterized optimum maximizes a linear
    combination, not the cube objective directly). But since q_1^3
    + alpha q_2^3 is non-convex (cubic), the max over Q is attained
    at a boundary q of the feasible polytope, and the linear-obj
    angle sweep covers all vertices.
    """
    if alpha == 0.0:
        # max q_1^3: at q_1 = q_1^max, so bound = (q_1^max)^3
        q1_obj = np.zeros(N + 1)
        q1_obj[1] = 1.0
        q1_max, _ = best_1D_linear_obj(N, q1_obj, M=M)
        return q1_max ** 3, (q1_max, 0)
    angles = np.linspace(0, 2 * np.pi, M_angle, endpoint=False)
    best = -np.inf
    best_q = None
    for theta in angles:
        obj_w = np.zeros(N + 1)
        obj_w[1] = np.cos(theta)
        obj_w[2] = np.sin(theta)
        val, qv = best_1D_linear_obj(N, obj_w, M=M)
        if qv is None:
            continue
        q1, q2 = qv[1], qv[2]
        cube_val = q1 ** 3 + alpha * q2 ** 3
        if cube_val > best:
            best = cube_val
            best_q = (q1, q2)
    return best, best_q


def tensor_witness_trivariate(q_vec, N):
    """Build coefficient tensor c_{j,k,l} = q_j q_k q_l."""
    c = np.zeros((N + 1, N + 1, N + 1))
    for j in range(N + 1):
        for k in range(N + 1):
            for l in range(N + 1):
                c[j, k, l] = q_vec[j] * q_vec[k] * q_vec[l]
    return c


def run(
    N: int = 2,
    alpha_grid=None,
    M_3D: int = 40,
    M_1D: int = 4000,
    M_angle: int = 720,
    M_verify: int = 60,
    out_dir: Path = None,
):
    if alpha_grid is None:
        # Denser around expected peak (between 0 and 10)
        alpha_grid = np.array(
            [0.0, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 7.0, 10.0]
        )

    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 78)
    print(f"[4E.4] Trivariate balanced-sum LP: max c_{{1,1,1}} + alpha c_{{2,2,2}}")
    print("=" * 78)
    print(f"  N = {N} (tridegree ({N},{N},{N})), M_3D = {M_3D} "
          f"({M_3D**3:,} constraints)")
    print(f"  M_1D = {M_1D}, M_angle = {M_angle}, M_verify = {M_verify}")
    print()

    results = []
    print(f"  {'alpha':>6}  {'LP':>10}  {'tensor':>10}  {'gap':>11}  "
          f"{'rel gap':>9}  {'P_min':>10}  {'time':>5}")
    for alpha in alpha_grid:
        t0 = time.time()
        lp_val, c_tensor = best_trivariate_diag_sum(
            N, float(alpha), M=M_3D
        )
        tensor_bound, q_best = symmetric_tensor_bound_diag(
            N, float(alpha), M=M_1D, M_angle=M_angle
        )
        P_min, _ = verify_trivariate_nonneg(c_tensor, M_test=M_verify)
        gap = lp_val - tensor_bound
        rel_gap = gap / tensor_bound if tensor_bound != 0 else 0.0
        dt = time.time() - t0
        results.append({
            "alpha": float(alpha),
            "lp_val": lp_val,
            "tensor_bound": tensor_bound,
            "q_best": q_best,
            "gap": gap,
            "rel_gap": rel_gap,
            "P_min": P_min,
            "c_tensor": c_tensor,
        })
        print(f"  {alpha:>6.2f}  {lp_val:>10.4f}  {tensor_bound:>10.4f}  "
              f"{gap:>+11.3e}  {rel_gap:>+9.4f}  {P_min:>10.3e}  {dt:>3.1f}s")

    # Find peak gap
    peak_idx = int(np.argmax([r["rel_gap"] for r in results]))
    peak = results[peak_idx]
    print()
    print(f"  Peak relative gap: +{peak['rel_gap']*100:.2f}% at alpha = "
          f"{peak['alpha']:.3f}")
    print(f"  LP value at peak: {peak['lp_val']:.4f}")
    print(f"  Tensor bound at peak: {peak['tensor_bound']:.4f}")
    print(f"  Best 1D Q at peak (q_1, q_2): {peak['q_best']}")

    # Verify peak polynomial more aggressively
    P_min_fine, _ = verify_trivariate_nonneg(peak["c_tensor"], M_test=M_verify * 2)
    print(f"  Peak P_min on {M_verify*2}^3 grid: {P_min_fine:.3e}")
    print(f"  Peak LP-feasibility / convergence diagnostic")

    # Compare to 4E.2 (d = 2 case): peak at alpha = 3 was +25.00%
    print()
    print(f"  Comparison to 4E.2 (bivariate at bidegree ({N},{N})):")
    print(f"    d = 2 peak gap (4E.2): +25.00% at alpha = 3")
    print(f"    d = 3 peak gap (4E.4): +{peak['rel_gap']*100:.2f}% at alpha = "
          f"{peak['alpha']:.2f}")
    if peak['rel_gap'] > 0.25:
        print(f"    ==> trivariate gap EXCEEDS bivariate gap "
              f"({peak['rel_gap']/0.25:.2f}x)")
    else:
        print(f"    ==> trivariate gap is {0.25/peak['rel_gap']:.2f}x SMALLER "
              f"than bivariate gap")

    # Examine peak coefficient tensor structure
    print()
    print(f"  Peak coefficient tensor (alpha = {peak['alpha']:.3f}) structure:")
    c_t = peak["c_tensor"]
    # Show large coefficients
    large = []
    for j in range(N + 1):
        for k in range(N + 1):
            for l in range(N + 1):
                if abs(c_t[j, k, l]) > 1e-3:
                    large.append((j, k, l, c_t[j, k, l]))
    large.sort(key=lambda x: -abs(x[3]))
    print(f"    {'(j,k,l)':>10}  {'c_{j,k,l}':>10}  {'ratio to c_{0,0,0}':>16}")
    for j, k, l, c in large[:15]:
        print(f"    {str((j,k,l)):>10}  {c:>+10.4f}  {c/c_t[0,0,0]:>16.4f}")

    # Save
    np.savez_compressed(
        out_dir / "e4e4_trivariate_sum.npz",
        N=N,
        alpha_grid=np.array(alpha_grid),
        lp_vals=np.array([r["lp_val"] for r in results]),
        tensor_bounds=np.array([r["tensor_bound"] for r in results]),
        gaps=np.array([r["gap"] for r in results]),
        rel_gaps=np.array([r["rel_gap"] for r in results]),
        P_mins=np.array([r["P_min"] for r in results]),
        peak_alpha=peak["alpha"],
        peak_rel_gap=peak["rel_gap"],
        peak_c_tensor=peak["c_tensor"],
        peak_q_best=np.array(peak["q_best"]),
    )

    # Plot
    fig, axs = plt.subplots(1, 2, figsize=(13, 5))
    alphas = [r["alpha"] for r in results]
    lps = [r["lp_val"] for r in results]
    tensors = [r["tensor_bound"] for r in results]
    rel_gaps = [r["rel_gap"] * 100 for r in results]

    ax = axs[0]
    ax.plot(alphas, lps, "bo-", label="LP value")
    ax.plot(alphas, tensors, "r--", label="symmetric tensor bound")
    ax.set_xlabel(r"$\alpha$ in $c_{1,1,1} + \alpha c_{2,2,2}$")
    ax.set_ylabel(f"value at $N = {N}$")
    ax.set_title(f"4E.4: trivariate LP at tridegree ({N},{N},{N})")
    ax.legend()
    ax.grid(alpha=0.3)

    ax = axs[1]
    ax.plot(alphas, rel_gaps, "go-", label="d = 3 (trivariate)")
    # Also overlay the d = 2 result (4E.2) for comparison
    alpha_4e2 = [0, 0.5, 1, 2, 2.75, 3, 3.5, 4, 5, 7, 10]
    rel_gap_4e2 = [0, 6.2, 12.1, 21.4, 24.8, 25.0, 24.0, 20.8, 14.1, 8, 3.9]
    ax.plot(alpha_4e2, rel_gap_4e2, "ms--", alpha=0.6, label="d = 2 (4E.2)")
    ax.axvline(peak["alpha"], color="green", linestyle=":", alpha=0.5,
               label=f"d=3 peak at α={peak['alpha']:.2f}\n+{peak['rel_gap']*100:.2f}%")
    ax.set_xlabel(r"$\alpha$")
    ax.set_ylabel("relative gap (% of tensor bound)")
    ax.set_title(f"4E.4: relative LP-vs-tensor gap, d=3 vs d=2")
    ax.legend()
    ax.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig(out_dir / "e4e4_trivariate_sum.png", dpi=140)
    plt.close()
    print()
    print(f"  Saved {out_dir / 'e4e4_trivariate_sum.png'}")
    print(f"  Saved {out_dir / 'e4e4_trivariate_sum.npz'}")

    print()
    print("=" * 78)
    print("[4E.4] Summary")
    print("=" * 78)
    print(f"Trivariate balanced-sum LP at tridegree ({N},{N},{N}):")
    print(f"  Peak relative gap: +{peak['rel_gap']*100:.2f}% at alpha = "
          f"{peak['alpha']:.3f}")
    print(f"  Bivariate analog (4E.2): +25.00% at alpha = 3")
    if peak['rel_gap'] > 0.25:
        ratio = peak['rel_gap'] / 0.25
        print(f"  ==> trivariate gap is {ratio:.2f}x LARGER than bivariate.")
    else:
        ratio = 0.25 / peak['rel_gap']
        print(f"  ==> trivariate gap is {ratio:.2f}x SMALLER than bivariate.")
    print()
    print(f"Caveat: per 4E.3 structural lemma, the C-S gap does NOT translate")
    print(f"into an improved zero-free region constant via 1D restriction.")
    print(f"This experiment characterizes the d-variate auxiliary inequality")
    print(f"structure independently of its applicability to RH.")

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, default=2)
    parser.add_argument("--M-3D", type=int, default=40)
    parser.add_argument("--M-1D", type=int, default=4000)
    parser.add_argument("--M-angle", type=int, default=720)
    parser.add_argument("--M-verify", type=int, default=60)
    args = parser.parse_args()
    run(
        N=args.N,
        M_3D=args.M_3D,
        M_1D=args.M_1D,
        M_angle=args.M_angle,
        M_verify=args.M_verify,
    )
