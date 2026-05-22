"""Experiment 4E.2: alpha-sweep and extended-diagonal-sum probes.

4E (e4e_offdiag_lp.py) found that the LP for max c_{1,1} + c_{2,2} at
bidegree (N, N) exceeds the Cauchy-Schwarz tensor-product bound, with
the largest gap (+12.1%) at N = 2. 4E.2 probes two follow-up questions:

(a) Alpha sweep at N = 2. The objective max c_{1,1} + alpha * c_{2,2}
    decomposes (LP = tensor) at alpha = 0 (pure c_{1,1}) and at alpha
    = infinity (pure c_{2,2}). At alpha = 1 the relative gap is 12.1%.
    Where does the relative gap peak as alpha varies?

(b) Extended diagonal sum at N = 3. Compare max c_{1,1} + c_{2,2} +
    c_{3,3} at bidegree (3, 3) against the 2-term variant. Does adding
    a third diagonal term enlarge the gap?

These extend the 4E "balanced sum" study by widening the LP objective
family and verifying that the non-decomposition is robust to the
specific coefficient weights.

Output:
  - e4e2_sum_sweep.npz: alpha grid, LP/tensor values, 3-term result
  - e4e2_sum_sweep.png: gap-vs-alpha at N=2 plus 3-term bar chart
"""

from __future__ import annotations

import argparse
import time
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from experiments.zero_free.e4e_offdiag_lp import (
    best_1D_linear_obj,
    best_1D_raw_qj,
    best_bivariate_objective,
    numerical_rank,
    verify_bivariate_nonneg,
)


def tensor_bound_diag_weighted(N: int, weights: dict, M: int = 4000,
                               M_angle: int = 360):
    """Compute max_Q sum_j w_j q_j^2 over 1D nonneg deg-N polys with q_0 = 1.

    weights: dict {j: w_j} for indices j >= 1.

    Uses sphere-direction sweep: max sum w_j q_j^2 = max_{||c|| = 1}
    (max_Q sum_j c_j sqrt(w_j) q_j)^2, the inner max being a 1D LP.

    Returns (bound, best_direction, best_q_vector).
    """
    indices = sorted(weights.keys())
    K = len(indices)
    sqrt_w = {j: float(np.sqrt(weights[j])) for j in indices}

    if K == 1:
        j = indices[0]
        max_qj, qv = best_1D_raw_qj(N, j, M=M)
        return weights[j] * max_qj * max_qj, [1.0], qv

    if K == 2:
        j1, j2 = indices
        angles = np.linspace(0, 2 * np.pi, M_angle, endpoint=False)
        best = 0.0
        best_dir = None
        best_q = None
        for theta in angles:
            obj_w = np.zeros(N + 1)
            obj_w[j1] = np.cos(theta) * sqrt_w[j1]
            obj_w[j2] = np.sin(theta) * sqrt_w[j2]
            val, qv = best_1D_linear_obj(N, obj_w, M=M)
            if val * val > best:
                best = val * val
                best_dir = [np.cos(theta), np.sin(theta)]
                best_q = qv
        return best, best_dir, best_q

    if K == 3:
        j1, j2, j3 = indices
        n_theta = M_angle
        n_phi = M_angle // 2
        thetas = np.linspace(0, 2 * np.pi, n_theta, endpoint=False)
        phis = np.linspace(0, np.pi, n_phi)
        best = 0.0
        best_dir = None
        best_q = None
        for phi in phis:
            sp, cp = np.sin(phi), np.cos(phi)
            for theta in thetas:
                ct, st = np.cos(theta), np.sin(theta)
                c1, c2, c3 = sp * ct, sp * st, cp
                obj_w = np.zeros(N + 1)
                obj_w[j1] = c1 * sqrt_w[j1]
                obj_w[j2] = c2 * sqrt_w[j2]
                obj_w[j3] = c3 * sqrt_w[j3]
                val, qv = best_1D_linear_obj(N, obj_w, M=M)
                if val * val > best:
                    best = val * val
                    best_dir = [c1, c2, c3]
                    best_q = qv
        return best, best_dir, best_q

    raise NotImplementedError(f"K = {K} sphere sweep not implemented")


def run(
    N_alpha: int = 2,
    alpha_grid=None,
    M_2D: int = 200,
    M_1D: int = 4000,
    M_angle: int = 360,
    M_angle_3D: int = 90,
    out_dir: Path = None,
):
    if alpha_grid is None:
        alpha_grid = np.concatenate(
            [
                np.linspace(0.0, 1.0, 11),
                np.linspace(1.0, 4.0, 13)[1:],
                np.array([5.0, 7.0, 10.0]),
            ]
        )

    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 78)
    print("[4E.2] Alpha-sweep + extended-diagonal-sum bivariate LP probes")
    print("=" * 78)
    print(f"  N (alpha sweep) = {N_alpha}, M_2D = {M_2D}, M_1D = {M_1D}, "
          f"M_angle = {M_angle}")
    print(f"  alpha grid: {len(alpha_grid)} values from {alpha_grid[0]:.2f} "
          f"to {alpha_grid[-1]:.2f}")
    print()

    # Part (a): alpha sweep at N = 2
    print(f"[4E.2.a] Alpha sweep: max c_{{1,1}} + alpha * c_{{2,2}} at bidegree "
          f"({N_alpha}, {N_alpha})")
    print(f"         {'alpha':>7}  {'LP':>10}  {'tensor':>10}  {'gap':>11}  "
          f"{'gap/tensor':>10}  {'rank':>4}  {'P_min':>10}  {'time':>5}")

    alpha_results = []
    for alpha in alpha_grid:
        t0 = time.time()
        if alpha == 0.0:
            obj = {(1, 1): 1.0}
        else:
            obj = {(1, 1): 1.0, (2, 2): float(alpha)}
        lp_val, c_mat = best_bivariate_objective(N_alpha, obj, M=M_2D)
        rank, svs = numerical_rank(c_mat)
        P_min, _ = verify_bivariate_nonneg(c_mat, M_test=200)

        if alpha == 0.0:
            # Pure c_{1,1}: tensor bound = (max q_1)^2
            q1, _ = best_1D_raw_qj(N_alpha, 1, M=M_1D)
            tensor_bound = q1 * q1
        else:
            tensor_bound, _, _ = tensor_bound_diag_weighted(
                N_alpha, {1: 1.0, 2: float(alpha)},
                M=M_1D, M_angle=M_angle
            )
        gap = lp_val - tensor_bound
        rel_gap = gap / tensor_bound if tensor_bound > 0 else 0
        dt = time.time() - t0
        alpha_results.append(
            {
                "alpha": float(alpha),
                "lp_val": lp_val,
                "tensor": tensor_bound,
                "gap": gap,
                "rel_gap": rel_gap,
                "rank": rank,
                "P_min": P_min,
            }
        )
        print(f"         {alpha:>7.3f}  {lp_val:>10.6f}  {tensor_bound:>10.6f}  "
              f"{gap:>+11.4e}  {rel_gap:>+10.4f}  {rank:>4}  "
              f"{P_min:>10.3e}  {dt:>3.1f}s")

    best_alpha_idx = int(np.argmax([r["rel_gap"] for r in alpha_results]))
    best_alpha = alpha_results[best_alpha_idx]
    print()
    print(f"  Peak relative gap at alpha = {best_alpha['alpha']:.3f}: "
          f"+{best_alpha['rel_gap']*100:.2f}% "
          f"(LP {best_alpha['lp_val']:.4f}, tensor {best_alpha['tensor']:.4f})")
    print()

    # Part (b): 3-term diagonal at N = 3
    print(f"[4E.2.b] Extended diagonal: max c_{{1,1}} + c_{{2,2}} + c_{{3,3}} at "
          f"bidegree (3, 3)")
    print(f"         compared to max c_{{1,1}} + c_{{2,2}} at bidegree (3, 3)")
    print(f"         M_angle_3D = {M_angle_3D} (sphere sweep)")

    t0 = time.time()
    # 3-term LP
    lp_3term, c_mat_3 = best_bivariate_objective(
        3, {(1, 1): 1.0, (2, 2): 1.0, (3, 3): 1.0}, M=M_2D
    )
    rank_3, svs_3 = numerical_rank(c_mat_3)
    P_min_3, _ = verify_bivariate_nonneg(c_mat_3, M_test=200)
    dt_lp_3 = time.time() - t0

    t0 = time.time()
    tensor_3term, _, _ = tensor_bound_diag_weighted(
        3, {1: 1.0, 2: 1.0, 3: 1.0}, M=M_1D, M_angle=M_angle_3D
    )
    dt_tensor_3 = time.time() - t0
    gap_3 = lp_3term - tensor_3term
    rel_3 = gap_3 / tensor_3term if tensor_3term > 0 else 0

    print(f"         3-term LP @ N=3: {lp_3term:.6f}, tensor = {tensor_3term:.6f}, "
          f"gap = {gap_3:+.4e} ({rel_3*100:+.2f}%)")
    print(f"         3-term rank = {rank_3}, sv ratios = "
          f"{[svs_3[i]/svs_3[0] for i in range(min(3, len(svs_3)))]}")
    print(f"         P_min = {P_min_3:.4e}, LP time {dt_lp_3:.1f}s, "
          f"tensor time {dt_tensor_3:.1f}s")
    print()

    # 2-term reference at N=3
    lp_2term_N3 = None
    tensor_2term_N3 = None
    for r in alpha_results:
        if r["alpha"] == 1.0 and N_alpha == 3:
            lp_2term_N3 = r["lp_val"]
            tensor_2term_N3 = r["tensor"]
    if lp_2term_N3 is None:
        # Compute fresh
        lp_2term_N3, _ = best_bivariate_objective(
            3, {(1, 1): 1.0, (2, 2): 1.0}, M=M_2D
        )
        tensor_2term_N3, _, _ = tensor_bound_diag_weighted(
            3, {1: 1.0, 2: 1.0}, M=M_1D, M_angle=M_angle
        )
    rel_2 = (lp_2term_N3 - tensor_2term_N3) / tensor_2term_N3
    print(f"  Reference: 2-term LP @ N=3: {lp_2term_N3:.4f}, tensor = "
          f"{tensor_2term_N3:.4f}, gap = {rel_2*100:+.2f}%")
    print()

    # Save
    np.savez_compressed(
        out_dir / "e4e2_sum_sweep.npz",
        N_alpha=N_alpha,
        alpha_grid=np.array(alpha_grid),
        lp_vals=np.array([r["lp_val"] for r in alpha_results]),
        tensor_bounds=np.array([r["tensor"] for r in alpha_results]),
        gaps=np.array([r["gap"] for r in alpha_results]),
        rel_gaps=np.array([r["rel_gap"] for r in alpha_results]),
        ranks=np.array([r["rank"] for r in alpha_results]),
        P_mins=np.array([r["P_min"] for r in alpha_results]),
        best_alpha=best_alpha["alpha"],
        best_alpha_rel_gap=best_alpha["rel_gap"],
        lp_3term=lp_3term,
        tensor_3term=tensor_3term,
        gap_3term=gap_3,
        rel_3term=rel_3,
        c_mat_3term=c_mat_3,
        rank_3term=rank_3,
        singular_values_3term=np.array(svs_3),
        lp_2term_N3=lp_2term_N3,
        tensor_2term_N3=tensor_2term_N3,
        rel_2term_N3=rel_2,
    )

    # Plot
    fig, axs = plt.subplots(1, 3, figsize=(16, 4.8))

    # Panel 1: alpha sweep - LP and tensor curves
    ax = axs[0]
    alphas = [r["alpha"] for r in alpha_results]
    lps = [r["lp_val"] for r in alpha_results]
    tensors = [r["tensor"] for r in alpha_results]
    ax.plot(alphas, lps, "bo-", label="LP value")
    ax.plot(alphas, tensors, "r--", label="tensor bound (C-S)")
    ax.set_xlabel(r"$\alpha$ in objective $c_{1,1} + \alpha\, c_{2,2}$")
    ax.set_ylabel("value at $N = 2$")
    ax.set_title(r"4E.2.a: alpha sweep at $N = 2$")
    ax.legend()
    ax.grid(alpha=0.3)

    # Panel 2: relative gap
    ax = axs[1]
    rel_gaps = [r["rel_gap"] * 100 for r in alpha_results]
    ax.plot(alphas, rel_gaps, "go-")
    ax.axhline(0, color="k", linestyle=":", alpha=0.5)
    ax.axvline(best_alpha["alpha"], color="purple", linestyle="--", alpha=0.7,
               label=f"peak at $\\alpha = {best_alpha['alpha']:.2f}$\n"
                     f"+{best_alpha['rel_gap']*100:.1f}%")
    ax.set_xlabel(r"$\alpha$")
    ax.set_ylabel("LP - tensor (% of tensor)")
    ax.set_title(r"4E.2.a: relative gap vs $\alpha$")
    ax.legend()
    ax.grid(alpha=0.3)

    # Panel 3: 2-term vs 3-term at N=3
    ax = axs[2]
    labels = ["2-term\n(N=3)", "3-term\n(N=3)"]
    lp_vals_panel = [lp_2term_N3, lp_3term]
    tensor_vals_panel = [tensor_2term_N3, tensor_3term]
    x = np.arange(2)
    width = 0.35
    ax.bar(x - width / 2, lp_vals_panel, width, label="LP value", color="blue", alpha=0.7)
    ax.bar(x + width / 2, tensor_vals_panel, width, label="tensor bound",
           color="red", alpha=0.7)
    for i, (lp, t) in enumerate(zip(lp_vals_panel, tensor_vals_panel)):
        rel = (lp - t) / t * 100
        ax.annotate(f"+{rel:.2f}%", xy=(i, max(lp, t) + 0.1),
                    ha="center", fontsize=10)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("value")
    ax.set_title("4E.2.b: 2-term vs 3-term diagonal sum at $N = 3$")
    ax.legend()
    ax.grid(alpha=0.3, axis="y")

    plt.tight_layout()
    plt.savefig(out_dir / "e4e2_sum_sweep.png", dpi=140)
    plt.close()
    print(f"[4E.2] Saved {out_dir / 'e4e2_sum_sweep.png'}")
    print(f"[4E.2] Saved {out_dir / 'e4e2_sum_sweep.npz'}")

    # Summary
    print()
    print("=" * 78)
    print("[4E.2] Summary")
    print("=" * 78)
    print(f"Part (a): alpha sweep at N = {N_alpha}")
    print(f"  Peak LP-vs-tensor gap: +{best_alpha['rel_gap']*100:.2f}% at "
          f"alpha = {best_alpha['alpha']:.3f}")
    print(f"  Gap at alpha = 0: {alpha_results[0]['rel_gap']*100:+.4f}% "
          f"(should be ~0; single-coefficient LP)")
    print(f"  Gap at alpha = 10: {alpha_results[-1]['rel_gap']*100:+.4f}% "
          f"(approaches single-c_{{2,2}}; should shrink)")
    print()
    print(f"Part (b): 3-term sum at N = 3")
    print(f"  2-term (c_{{1,1}} + c_{{2,2}}) at N=3: +{rel_2*100:.2f}%")
    print(f"  3-term (+ c_{{3,3}}) at N=3: +{rel_3*100:.2f}%")
    if rel_3 > rel_2:
        print(f"  Adding c_{{3,3}} ENLARGES the gap by a factor of "
              f"{rel_3/rel_2 if rel_2 > 0 else float('inf'):.2f}x")
    else:
        print(f"  Adding c_{{3,3}} does NOT enlarge the gap.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--N-alpha", type=int, default=2)
    parser.add_argument("--M-2D", type=int, default=200)
    parser.add_argument("--M-1D", type=int, default=4000)
    parser.add_argument("--M-angle", type=int, default=360)
    parser.add_argument("--M-angle-3D", type=int, default=90)
    args = parser.parse_args()
    run(
        N_alpha=args.N_alpha,
        M_2D=args.M_2D,
        M_1D=args.M_1D,
        M_angle=args.M_angle,
        M_angle_3D=args.M_angle_3D,
    )
