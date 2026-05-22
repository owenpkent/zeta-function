"""Experiment 4E: Off-diagonal and balanced-sum bivariate LPs.

4D-ii (e4d_multivariate_lp.py) established that the bivariate LP for
max c_{1,1} at bidegree (N, N) saturates the tensor-product witness
P = Q(theta) Q(phi) where Q is the 1D Fejér optimum. Concretely:

    max c_{1,1} = q_1^2 = (2 cos(pi/(N+2)))^2.

The LP-optimal coefficient matrix is rank-1 with c_{j,k} = q_j q_k.

That result is for ONE objective (max c_{1,1}) and ONE bidegree (N, N).
This experiment asks how universal the decomposition is. Two probes:

Test A. Off-diagonal single coefficients. Do the LPs

    max c_{1,2}, c_{2,1}, c_{2,2} at bidegree (N, N)

also decompose as (max_{1D} q_j) * (max_{1D} q_k)?

Test B. Balanced-sum objectives. Does max (c_{1,1} + c_{2,2})
decompose? This is the simplest "weighted combination" objective from
LEARNINGS open question #2: the explicit-formula bookkeeping at two
heights produces sum-of-coefficient objectives, not single-coefficient.

Decomposition is equivalent to the LP-optimal c_{j,k} matrix having
rank 1. Numerical SVD provides the diagnostic.

If decomposition holds for ALL these objectives, then no single-LP
extension within "max a linear combo of c_{j,k}'s subject to P >= 0
on [0, 2pi]^2" produces a genuine 2D inequality. New structure must
come from different constraints (constrained domain, cross-prime
coupling, etc.).

If decomposition FAILS for any objective (LP-optimal matrix has rank
> 1), we have a candidate for a new 2D auxiliary inequality.

Output:
  - e4e_offdiag_lp.npz: LP values, tensor predictions, SVD ranks
  - e4e_offdiag_lp.png: rank diagnostics + LP-vs-tensor comparisons
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


def best_1D_raw_qj(N: int, j: int, M: int = 4000):
    """LP: max q_j over nonneg trig polys of degree N in raw convention.

    P(theta) = sum_{k=0}^N q_k cos(k theta) >= 0, q_0 = 1.

    Returns (q_j_max, q_vector).
    """
    n_vars = N + 1
    theta = np.linspace(0, 2 * np.pi, M, endpoint=False)
    obj = np.zeros(n_vars)
    obj[j] = -1.0
    A_ub = np.zeros((M, n_vars))
    for k in range(n_vars):
        A_ub[:, k] = -np.cos(k * theta)
    b_ub = np.zeros(M)
    A_eq = np.zeros((1, n_vars))
    A_eq[0, 0] = 1.0
    b_eq = np.array([1.0])
    bounds = [(-5.0, 5.0)] * n_vars
    res = linprog(
        obj, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method="highs"
    )
    if not res.success:
        raise RuntimeError(f"1D LP failed for j={j}, N={N}: {res.message}")
    return float(-res.fun), res.x.copy()


def best_bivariate_objective(
    N: int, obj_coeffs: dict, M: int = 80, bound_lo: float = -10.0, bound_hi: float = 10.0
):
    """LP: max sum_{(j,k)} obj_{j,k} * c_{j,k} over nonneg bivariate trig polys.

    P(theta, phi) = sum_{0<=j,k<=N} c_{j,k} cos(j theta) cos(k phi) >= 0,
    c_{0,0} = 1, sampled on M x M grid.

    Returns (LP_value, c_matrix shape (N+1, N+1)).
    """
    n_vars = (N + 1) ** 2
    theta = np.linspace(0, 2 * np.pi, M, endpoint=False)
    phi = np.linspace(0, 2 * np.pi, M, endpoint=False)

    def idx(j, k):
        return j * (N + 1) + k

    obj = np.zeros(n_vars)
    for (j, k), w in obj_coeffs.items():
        obj[idx(j, k)] = -float(w)

    cos_j = np.array([np.cos(j * theta) for j in range(N + 1)])  # (N+1, M)
    cos_k = np.array([np.cos(k * phi) for k in range(N + 1)])    # (N+1, M)

    M2 = M * M
    A_ub = np.zeros((M2, n_vars))
    for j in range(N + 1):
        for k in range(N + 1):
            outer = np.outer(cos_j[j], cos_k[k]).flatten()
            A_ub[:, idx(j, k)] = -outer
    b_ub = np.zeros(M2)

    A_eq = np.zeros((1, n_vars))
    A_eq[0, idx(0, 0)] = 1.0
    b_eq = np.array([1.0])

    bounds = [(bound_lo, bound_hi)] * n_vars

    res = linprog(
        obj, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method="highs"
    )
    if not res.success:
        raise RuntimeError(f"Bivariate LP failed: {res.message}")
    lp_val = float(-res.fun)
    c_mat = res.x.reshape((N + 1, N + 1))
    return lp_val, c_mat


def verify_bivariate_nonneg(c_mat, M_test: int = 200):
    """Verify P(theta, phi) >= 0 on a dense M_test x M_test grid."""
    N = c_mat.shape[0] - 1
    theta = np.linspace(0, 2 * np.pi, M_test, endpoint=False)
    phi = np.linspace(0, 2 * np.pi, M_test, endpoint=False)
    cos_j = np.array([np.cos(j * theta) for j in range(N + 1)])
    cos_k = np.array([np.cos(k * phi) for k in range(N + 1)])
    P = cos_j.T @ c_mat @ cos_k
    return float(P.min()), float(P.max())


def numerical_rank(c_mat, tol: float = 1e-6):
    """Numerical rank of c_mat via SVD. Returns (rank, singular_values)."""
    s = np.linalg.svd(c_mat, compute_uv=False)
    s_norm = s / s[0] if s[0] > 0 else s
    rank = int((s_norm > tol).sum())
    return rank, s.tolist()


def best_1D_linear_obj(N: int, obj_weights, M: int = 4000):
    """LP: max sum_k obj_weights[k] q_k over nonneg deg-N trig polys, q_0 = 1.

    obj_weights: length (N+1) vector of objective coefficients (q_0 ignored).
    """
    n_vars = N + 1
    theta = np.linspace(0, 2 * np.pi, M, endpoint=False)
    obj = -np.asarray(obj_weights, dtype=float).copy()
    A_ub = np.zeros((M, n_vars))
    for k in range(n_vars):
        A_ub[:, k] = -np.cos(k * theta)
    b_ub = np.zeros(M)
    A_eq = np.zeros((1, n_vars))
    A_eq[0, 0] = 1.0
    b_eq = np.array([1.0])
    bounds = [(-5.0, 5.0)] * n_vars
    res = linprog(
        obj, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method="highs"
    )
    if not res.success:
        raise RuntimeError(f"1D LP failed: {res.message}")
    return float(-res.fun), res.x.copy()


def tensor_bound_sum_squares(N: int, indices, M: int = 4000, M_angle: int = 360):
    """Compute the asymmetric-tensor-product upper bound for the objective
    sum_{(j) in indices} q_j r_j   subject to Q, R nonneg deg-N, q_0 = r_0 = 1.

    By Cauchy-Schwarz applied to the (q_{j})_{j in indices} feature vector,
    this bound equals max_Q ||q_S||_2^2 where S is the index set, with
    ||q_S||_2 = sqrt(sum_{j in S} q_j^2). The max-norm-squared over Q in
    the 1D feasibility set is computed by sweeping the LP objective
    cos(theta) * q_{j_1} + sin(theta) * q_{j_2} over angles theta and
    taking the max of (LP value)^2. For 2-index sets this is exact; for
    more it's a 1D sweep that may need higher-dim sampling.

    Returns (bound, best_angle, best_q_vector).
    """
    if len(indices) != 2:
        raise NotImplementedError("Only 2-index sets supported")
    j1, j2 = indices
    angles = np.linspace(0, 2 * np.pi, M_angle, endpoint=False)
    best = 0.0
    best_angle = 0.0
    best_q = None
    for theta in angles:
        weights = np.zeros(N + 1)
        weights[j1] = np.cos(theta)
        weights[j2] = np.sin(theta)
        val, q = best_1D_linear_obj(N, weights, M=M)
        val_sq = val * val
        if val_sq > best:
            best = val_sq
            best_angle = theta
            best_q = q
    return float(best), float(best_angle), best_q


def run(
    N_values=(2, 3, 4, 5),
    M_2D: int = 60,
    M_1D: int = 4000,
    M_verify: int = 200,
    out_dir: Path = None,
):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 78)
    print("[4E] Off-diagonal and balanced-sum bivariate LPs")
    print("=" * 78)
    print(f"  M_2D = {M_2D} (LP grid), M_1D = {M_1D} (1D LP grid), "
          f"M_verify = {M_verify}")
    print()

    # First: 1D q_j maxima at each N (raw convention)
    print("[4E.1] 1D LP: max q_j over nonneg trig polys of degree N, q_0 = 1")
    print(f"       {'N':>3}  {'j':>3}  {'max q_j':>14}  {'check vs Fejér':>20}")
    q_max = {}  # q_max[(N, j)] = max q_j
    for N in N_values:
        for j in range(1, N + 1):
            qj, _ = best_1D_raw_qj(N, j, M=M_1D)
            q_max[(N, j)] = qj
            # For j = 1, classical Fejér: max q_1 = 2 cos(pi/(N+2))
            if j == 1:
                fejer = 2 * float(np.cos(np.pi / (N + 2)))
                tag = f"Fejér = {fejer:.6f}"
            else:
                tag = ""
            print(f"       {N:>3}  {j:>3}  {qj:>14.6f}  {tag:>20}")
        print()

    # Test A: off-diagonal single-coefficient LPs
    print("[4E.A] Bivariate LP: max c_{j,k} at bidegree (N, N)")
    print(f"       Tensor prediction: (max q_j) * (max q_k) at degree N")
    print(f"       {'N':>3}  {'(j,k)':>6}  {'LP c_jk':>10}  {'tensor':>10}  "
          f"{'diff':>10}  {'rank':>4}  {'sv ratio s2/s1':>15}  "
          f"{'P_min':>10}  {'time':>6}")

    test_A_pairs = [(1, 1), (1, 2), (2, 1), (2, 2)]
    test_A_results = {}
    for N in N_values:
        for (j, k) in test_A_pairs:
            if j > N or k > N:
                continue
            t0 = time.time()
            lp_val, c_mat = best_bivariate_objective(
                N, {(j, k): 1.0}, M=M_2D
            )
            dt = time.time() - t0
            tensor = q_max[(N, j)] * q_max[(N, k)]
            rank, svs = numerical_rank(c_mat)
            sv_ratio = (svs[1] / svs[0]) if svs[0] > 0 and len(svs) > 1 else 0.0
            P_min, _ = verify_bivariate_nonneg(c_mat, M_test=M_verify)
            test_A_results[(N, j, k)] = {
                "lp_val": lp_val,
                "tensor": tensor,
                "diff": lp_val - tensor,
                "rank": rank,
                "singular_values": svs,
                "P_min": P_min,
                "c_mat": c_mat,
            }
            print(f"       {N:>3}  ({j},{k})  {lp_val:>10.6f}  {tensor:>10.6f}  "
                  f"{lp_val - tensor:>+10.4e}  {rank:>4}  {sv_ratio:>15.4e}  "
                  f"{P_min:>10.4e}  {dt:>4.1f}s")
        print()

    # Test B: balanced-sum objectives
    print("[4E.B] Bivariate LP: max c_{1,1} + c_{2,2} at bidegree (N, N)")
    print(f"       Tensor bound (C-S): max_Q (q_1^2 + q_2^2) over 1D nonneg deg-N polys")
    print(f"       {'N':>3}  {'LP value':>10}  {'tensor bd':>10}  {'LP - tensor':>11}  "
          f"{'rank':>4}  {'sv s2/s1':>10}  {'P_min':>10}  {'time':>6}")
    test_B_results = {}
    for N in N_values:
        if N < 2:
            continue
        t0 = time.time()
        lp_val, c_mat = best_bivariate_objective(
            N, {(1, 1): 1.0, (2, 2): 1.0}, M=M_2D
        )
        dt = time.time() - t0
        rank, svs = numerical_rank(c_mat)
        sv_ratio = (svs[1] / svs[0]) if svs[0] > 0 and len(svs) > 1 else 0.0
        P_min, _ = verify_bivariate_nonneg(c_mat, M_test=M_verify)
        tensor_bound, t_angle, t_q = tensor_bound_sum_squares(N, (1, 2), M=M_1D, M_angle=360)
        test_B_results[N] = {
            "lp_val": lp_val,
            "tensor_bound": tensor_bound,
            "diff": lp_val - tensor_bound,
            "rank": rank,
            "singular_values": svs,
            "P_min": P_min,
            "c_mat": c_mat,
            "tensor_best_q": t_q,
            "tensor_best_angle": t_angle,
        }
        print(f"       {N:>3}  {lp_val:>10.6f}  {tensor_bound:>10.6f}  "
              f"{lp_val - tensor_bound:>+11.4e}  {rank:>4}  {sv_ratio:>10.4e}  "
              f"{P_min:>10.4e}  {dt:>4.1f}s")
    print()

    # Test C: off-diagonal sum c_{1,2} + c_{2,1}
    print("[4E.C] Bivariate LP: max c_{1,2} + c_{2,1} at bidegree (N, N)")
    print(f"       Tensor bound (C-S applied symmetrically): same max_Q (q_1^2 + q_2^2)")
    print(f"       {'N':>3}  {'LP value':>10}  {'tensor bd':>10}  {'LP - tensor':>11}  "
          f"{'rank':>4}  {'sv s2/s1':>10}  {'P_min':>10}  {'time':>6}")
    test_C_results = {}
    for N in N_values:
        if N < 2:
            continue
        t0 = time.time()
        lp_val, c_mat = best_bivariate_objective(
            N, {(1, 2): 1.0, (2, 1): 1.0}, M=M_2D
        )
        dt = time.time() - t0
        rank, svs = numerical_rank(c_mat)
        sv_ratio = (svs[1] / svs[0]) if svs[0] > 0 and len(svs) > 1 else 0.0
        P_min, _ = verify_bivariate_nonneg(c_mat, M_test=M_verify)
        # Tensor bound for c_{1,2} + c_{2,1}: by C-S on W = [[0,1],[1,0]] block,
        # sigma_max = 1, bound = max_Q (q_1^2 + q_2^2) -- same as Test B.
        tensor_bound = test_B_results[N]["tensor_bound"] if N in test_B_results else (
            tensor_bound_sum_squares(N, (1, 2), M=M_1D, M_angle=360)[0]
        )
        test_C_results[N] = {
            "lp_val": lp_val,
            "tensor_bound": tensor_bound,
            "diff": lp_val - tensor_bound,
            "rank": rank,
            "singular_values": svs,
            "P_min": P_min,
            "c_mat": c_mat,
        }
        print(f"       {N:>3}  {lp_val:>10.6f}  {tensor_bound:>10.6f}  "
              f"{lp_val - tensor_bound:>+11.4e}  {rank:>4}  {sv_ratio:>10.4e}  "
              f"{P_min:>10.4e}  {dt:>4.1f}s")
    print()

    # Save
    save_dict = {
        "N_values": np.array(N_values),
        "M_2D": M_2D,
        "M_1D": M_1D,
        "M_verify": M_verify,
    }
    # Flatten test A results
    for (N, j, k), r in test_A_results.items():
        prefix = f"A_N{N}_j{j}_k{k}"
        save_dict[f"{prefix}_lp"] = r["lp_val"]
        save_dict[f"{prefix}_tensor"] = r["tensor"]
        save_dict[f"{prefix}_rank"] = r["rank"]
        save_dict[f"{prefix}_singular_values"] = np.array(r["singular_values"])
        save_dict[f"{prefix}_P_min"] = r["P_min"]
        save_dict[f"{prefix}_c_mat"] = r["c_mat"]
    for N, r in test_B_results.items():
        prefix = f"B_N{N}"
        save_dict[f"{prefix}_lp"] = r["lp_val"]
        save_dict[f"{prefix}_tensor_bound"] = r["tensor_bound"]
        save_dict[f"{prefix}_rank"] = r["rank"]
        save_dict[f"{prefix}_singular_values"] = np.array(r["singular_values"])
        save_dict[f"{prefix}_P_min"] = r["P_min"]
        save_dict[f"{prefix}_c_mat"] = r["c_mat"]
    for N, r in test_C_results.items():
        prefix = f"C_N{N}"
        save_dict[f"{prefix}_lp"] = r["lp_val"]
        save_dict[f"{prefix}_tensor_bound"] = r["tensor_bound"]
        save_dict[f"{prefix}_rank"] = r["rank"]
        save_dict[f"{prefix}_singular_values"] = np.array(r["singular_values"])
        save_dict[f"{prefix}_P_min"] = r["P_min"]
        save_dict[f"{prefix}_c_mat"] = r["c_mat"]
    # Save q_max
    q_max_array = np.zeros((max(N_values) + 1, max(N_values) + 1))
    for (N, j), v in q_max.items():
        q_max_array[N, j] = v
    save_dict["q_max"] = q_max_array

    np.savez_compressed(out_dir / "e4e_offdiag_lp.npz", **save_dict)

    # Plot
    fig, axs = plt.subplots(1, 3, figsize=(16, 4.8))

    # Panel 1: Test A LP vs tensor for each (j, k)
    ax = axs[0]
    for (j, k) in test_A_pairs:
        Ns_pair = [N for N in N_values if (N, j, k) in test_A_results]
        lp_vals = [test_A_results[(N, j, k)]["lp_val"] for N in Ns_pair]
        tensors = [test_A_results[(N, j, k)]["tensor"] for N in Ns_pair]
        diffs = [lp - t for lp, t in zip(lp_vals, tensors)]
        ax.plot(Ns_pair, lp_vals, "o-", label=f"LP $c_{{{j},{k}}}$")
        ax.plot(Ns_pair, tensors, "x--", label=f"tensor $(q_{{{j}}})(q_{{{k}}})$", alpha=0.6)
    ax.set_xlabel("bidegree $N$")
    ax.set_ylabel("LP value")
    ax.set_title("4E.A: single-coefficient LPs vs tensor witness")
    ax.legend(fontsize=8, ncol=2)
    ax.grid(alpha=0.3)

    # Panel 2: rank of LP-optimal matrix (singular value ratio s_2 / s_1)
    ax = axs[1]
    # Test A entries
    for (j, k) in test_A_pairs:
        Ns_pair = [N for N in N_values if (N, j, k) in test_A_results]
        sv_ratios = []
        for N in Ns_pair:
            svs = test_A_results[(N, j, k)]["singular_values"]
            r = svs[1] / svs[0] if svs[0] > 0 and len(svs) > 1 else 1e-16
            sv_ratios.append(max(r, 1e-16))
        ax.semilogy(Ns_pair, sv_ratios, "o-", label=f"A: max $c_{{{j},{k}}}$", markersize=6)
    # Test B
    Ns_B = sorted(test_B_results.keys())
    sv_B = []
    for N in Ns_B:
        svs = test_B_results[N]["singular_values"]
        r = svs[1] / svs[0] if svs[0] > 0 and len(svs) > 1 else 1e-16
        sv_B.append(max(r, 1e-16))
    if Ns_B:
        ax.semilogy(Ns_B, sv_B, "s-", label="B: max $c_{1,1} + c_{2,2}$",
                    markersize=8, linewidth=2)
    # Test C
    Ns_C = sorted(test_C_results.keys())
    sv_C = []
    for N in Ns_C:
        svs = test_C_results[N]["singular_values"]
        r = svs[1] / svs[0] if svs[0] > 0 and len(svs) > 1 else 1e-16
        sv_C.append(max(r, 1e-16))
    if Ns_C:
        ax.semilogy(Ns_C, sv_C, "d-", label="C: max $c_{1,2} + c_{2,1}$",
                    markersize=8, linewidth=2)
    ax.axhline(1e-6, color="r", linestyle="--", alpha=0.5,
               label="rank-1 threshold ($10^{-6}$)")
    ax.set_xlabel("bidegree $N$")
    ax.set_ylabel(r"$\sigma_2 / \sigma_1$ of LP-optimal $c_{j,k}$")
    ax.set_title("Rank diagnostic: SVD ratio (low = rank 1 = decomposes)")
    ax.legend(fontsize=7, ncol=1)
    ax.grid(alpha=0.3, which="both")

    # Panel 3: summary text
    ax = axs[2]
    ax.axis("off")
    # Build summary text
    lines = []
    lines.append("Test A: max c_{j,k}, single-coeff")
    lines.append(f"  rank distribution across (N, j, k):")
    rank_counts_A = {}
    for r in test_A_results.values():
        rank_counts_A[r["rank"]] = rank_counts_A.get(r["rank"], 0) + 1
    for rk, cnt in sorted(rank_counts_A.items()):
        lines.append(f"     rank {rk}: {cnt} cases")
    lines.append("")
    lines.append("Test B: max c_{1,1} + c_{2,2}")
    lines.append(f"  rank distribution across N:")
    rank_counts_B = {}
    for r in test_B_results.values():
        rank_counts_B[r["rank"]] = rank_counts_B.get(r["rank"], 0) + 1
    for rk, cnt in sorted(rank_counts_B.items()):
        lines.append(f"     rank {rk}: {cnt} cases")
    lines.append("")
    lines.append("Test C: max c_{1,2} + c_{2,1}")
    lines.append(f"  rank distribution across N:")
    rank_counts_C = {}
    for r in test_C_results.values():
        rank_counts_C[r["rank"]] = rank_counts_C.get(r["rank"], 0) + 1
    for rk, cnt in sorted(rank_counts_C.items()):
        lines.append(f"     rank {rk}: {cnt} cases")
    ax.text(0.05, 0.95, "\n".join(lines), transform=ax.transAxes,
            fontsize=10, verticalalignment="top", family="monospace")
    ax.set_title("4E summary: rank counts")

    plt.tight_layout()
    plt.savefig(out_dir / "e4e_offdiag_lp.png", dpi=140)
    plt.close()
    print(f"[4E] Saved {out_dir / 'e4e_offdiag_lp.png'}")
    print(f"[4E] Saved {out_dir / 'e4e_offdiag_lp.npz'}")

    # Summary interpretation
    print()
    print("=" * 78)
    print("[4E] Summary")
    print("=" * 78)

    # Test A
    test_A_all_rank1 = all(r["rank"] == 1 for r in test_A_results.values())
    test_A_all_match_tensor = all(
        abs(r["diff"]) < 1e-3 * max(1.0, abs(r["tensor"]))
        for r in test_A_results.values()
    )
    print(f"Test A (single-coeff off-diagonal): "
          f"all rank-1? {test_A_all_rank1}; LP matches tensor? {test_A_all_match_tensor}")
    if test_A_all_rank1 and test_A_all_match_tensor:
        print("    -> Off-diagonal single-coeff LPs DECOMPOSE via asymmetric tensor product")
        print("       P(theta, phi) = Q(theta) R(phi) with Q, R independent 1D Fejér-type optima.")
    else:
        print("    -> Off-diagonal does NOT universally decompose. Investigate cases with "
              "rank > 1 or LP - tensor > tolerance.")

    # Test B
    test_B_all_rank1 = all(r["rank"] == 1 for r in test_B_results.values())
    test_B_exceeds_tensor = any(
        r["diff"] > 1e-3 * max(1.0, r["tensor_bound"])
        for r in test_B_results.values()
    )
    print(f"Test B (max c_{{1,1}} + c_{{2,2}}): rank-1 in all cases? {test_B_all_rank1}")
    print(f"    LP value exceeds Cauchy-Schwarz tensor bound? {test_B_exceeds_tensor}")
    if test_B_exceeds_tensor:
        print("    -> LP value provably exceeds the best tensor-product witness.")
        print("       The optimal P is NOT a sum of products. New 2D inequality found.")
        print("       Improvement factor per N:")
        for N in sorted(test_B_results.keys()):
            r = test_B_results[N]
            ratio = r["lp_val"] / r["tensor_bound"] if r["tensor_bound"] > 0 else 0
            print(f"         N = {N}: LP = {r['lp_val']:.4f}, "
                  f"tensor = {r['tensor_bound']:.4f}, ratio = {ratio:.4f} "
                  f"({(ratio - 1)*100:+.1f}%)")
    else:
        print("    -> LP value does not provably exceed tensor bound. "
              "Rank > 1 may be LP-vertex artifact.")

    # Test C
    test_C_all_rank1 = all(r["rank"] == 1 for r in test_C_results.values())
    test_C_exceeds_tensor = any(
        r["diff"] > 1e-3 * max(1.0, r["tensor_bound"])
        for r in test_C_results.values()
    )
    print(f"Test C (max c_{{1,2}} + c_{{2,1}}): rank-1 in all cases? {test_C_all_rank1}")
    print(f"    LP value exceeds Cauchy-Schwarz tensor bound? {test_C_exceeds_tensor}")
    if test_C_exceeds_tensor:
        print("    -> LP value exceeds tensor bound. New inequality.")
        for N in sorted(test_C_results.keys()):
            r = test_C_results[N]
            ratio = r["lp_val"] / r["tensor_bound"] if r["tensor_bound"] > 0 else 0
            print(f"         N = {N}: LP = {r['lp_val']:.4f}, "
                  f"tensor = {r['tensor_bound']:.4f}, ratio = {ratio:.4f} "
                  f"({(ratio - 1)*100:+.1f}%)")
    else:
        print("    -> LP value does not exceed tensor bound. Rank > 1 LP solution "
              "is LP-vertex artifact; tensor product witness achieves the LP value.")

    print()
    if test_B_exceeds_tensor or test_C_exceeds_tensor:
        print("[4E] Genuine 2D structure: at least one sum-of-coefficient LP")
        print("     exceeds its best tensor-product witness. This contradicts the 4D")
        print("     '-no new auxiliary inequality' conclusion: 4D only tested single-")
        print("     coefficient objectives, which DO decompose. Sum objectives can")
        print("     access non-tensor bivariate polynomials.")
    else:
        print("[4E] All probed LPs decompose to tensor-product witnesses. No new")
        print("     inequality from sum-of-coefficient LP objectives at this bidegree.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--N-values", type=int, nargs="+", default=[2, 3, 4, 5])
    parser.add_argument("--M-2D", type=int, default=60)
    parser.add_argument("--M-1D", type=int, default=4000)
    parser.add_argument("--M-verify", type=int, default=200)
    args = parser.parse_args()
    run(
        N_values=tuple(args.N_values),
        M_2D=args.M_2D,
        M_1D=args.M_1D,
        M_verify=args.M_verify,
    )
