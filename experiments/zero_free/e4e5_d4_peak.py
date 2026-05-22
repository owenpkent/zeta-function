"""Experiment 4E.5: d = 4 balanced-sum LP, testing the (d-1) x 25% pattern.

4E (d=2): peak gap +25.00% at alpha = 3, N = 2.
4E.4 (d=3): peak gap +51.29% at alpha = 3.25, N = 2 (M-corrected: ~[50%, 51%]).

The pattern (d-1) x 25% predicts:
  d = 4: ~75% (predicted)
  d = 5: ~100%
  ...

This experiment tests d = 4. We solve

    max c_{1,1,1,1} + alpha c_{2,2,2,2}
    subject to P(theta_1, theta_2, theta_3, theta_4) = sum c_{j,k,l,m}
                cos(j theta_1) cos(k theta_2) cos(l theta_3) cos(m theta_4) >= 0,
    c_{0,0,0,0} = 1

at quad-degree (N, N, N, N) for N = 2. The symmetric tensor bound is
max_Q (q_1^4 + alpha q_2^4) over 1D nonneg deg-N polys with q_0 = 1.

Computational cost: (N+1)^4 = 81 variables, M_4D^4 constraints. At
M_4D = 25 we have 390K constraints; at M_4D = 35 we have 1.5M. We
use M_4D = 25 for the sweep and verify peak at M_4D = 35.

Output:
  - e4e5_d4_peak.npz: alpha grid, LP/tensor values
  - e4e5_d4_peak.png: gap vs alpha
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


def best_quadvariate_diag_sum(
    N: int, alpha: float, M: int = 25, bounds_abs: float = 20.0
):
    """LP: max c_{1,1,1,1} + alpha c_{2,2,2,2} over nonneg quadvariate trig polys.

    P(t_1, t_2, t_3, t_4) = sum_{j,k,l,m} c_{j,k,l,m}
                              cos(j t_1) cos(k t_2) cos(l t_3) cos(m t_4) >= 0
    sampled on M^4 uniform grid, c_{0,0,0,0} = 1.
    """
    n_vars = (N + 1) ** 4
    theta = np.linspace(0, 2 * np.pi, M, endpoint=False)

    def idx(j, k, l, m):
        return ((j * (N + 1) + k) * (N + 1) + l) * (N + 1) + m

    obj = np.zeros(n_vars)
    obj[idx(1, 1, 1, 1)] = -1.0
    if alpha != 0.0:
        obj[idx(2, 2, 2, 2)] = -float(alpha)

    cos_arr = np.array([np.cos(j * theta) for j in range(N + 1)])  # (N+1, M)

    M4 = M ** 4
    A_ub = np.zeros((M4, n_vars))
    for j in range(N + 1):
        for k in range(N + 1):
            for l in range(N + 1):
                for m in range(N + 1):
                    outer = (
                        cos_arr[j][:, None, None, None]
                        * cos_arr[k][None, :, None, None]
                        * cos_arr[l][None, None, :, None]
                        * cos_arr[m][None, None, None, :]
                    ).flatten()
                    A_ub[:, idx(j, k, l, m)] = -outer
    b_ub = np.zeros(M4)

    A_eq = np.zeros((1, n_vars))
    A_eq[0, idx(0, 0, 0, 0)] = 1.0
    b_eq = np.array([1.0])

    bounds = [(-bounds_abs, bounds_abs)] * n_vars

    res = linprog(
        obj, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method="highs"
    )
    if not res.success:
        raise RuntimeError(f"4D LP failed at N={N}, alpha={alpha}: {res.message}")
    c_tensor = res.x.reshape((N + 1, N + 1, N + 1, N + 1))
    return float(-res.fun), c_tensor


def verify_quadvariate_nonneg(c_tensor, M_test: int = 30):
    """Verify P >= 0 on M_test^4 grid via einsum."""
    N = c_tensor.shape[0] - 1
    theta = np.linspace(0, 2 * np.pi, M_test, endpoint=False)
    cos_arr = np.array([np.cos(j * theta) for j in range(N + 1)])
    P = np.einsum("jklm,ja,kb,lc,md->abcd",
                  c_tensor, cos_arr, cos_arr, cos_arr, cos_arr)
    return float(P.min())


def symmetric_tensor_bound_d4_diag(
    N: int, alpha: float, M: int = 4000, M_angle: int = 720
):
    """Max_Q (q_1^4 + alpha q_2^4) over 1D nonneg deg-N polys with q_0 = 1.

    Same angle-sweep strategy as e4e4 but with 4th power.
    """
    if alpha == 0.0:
        q1_obj = np.zeros(N + 1)
        q1_obj[1] = 1.0
        q1_max, _ = best_1D_linear_obj(N, q1_obj, M=M)
        return q1_max ** 4, (q1_max, 0)
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
        quart_val = q1 ** 4 + alpha * q2 ** 4
        if quart_val > best:
            best = quart_val
            best_q = (q1, q2)
    return best, best_q


def run(
    N: int = 2,
    alpha_grid=None,
    M_4D: int = 25,
    M_1D: int = 4000,
    M_angle: int = 720,
    M_verify: int = 30,
    out_dir: Path = None,
):
    if alpha_grid is None:
        # Focus on the expected peak region (around alpha = 3-4)
        alpha_grid = np.array([0.0, 1.0, 2.0, 3.0, 3.5, 4.0, 4.5, 5.0, 7.0, 10.0])

    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 78)
    print(f"[4E.5] d=4 balanced-sum LP: max c_{{1,1,1,1}} + alpha c_{{2,2,2,2}}")
    print("=" * 78)
    print(f"  N = {N} (quad-degree ({N},{N},{N},{N})), M_4D = {M_4D} "
          f"({M_4D**4:,} constraints)")
    print(f"  Variables: {(N+1)**4}")
    print()

    results = []
    print(f"  {'alpha':>6}  {'LP':>10}  {'tensor':>10}  {'gap':>11}  "
          f"{'rel gap':>9}  {'P_min':>10}  {'time':>5}")
    for alpha in alpha_grid:
        t0 = time.time()
        lp_val, c_tensor = best_quadvariate_diag_sum(N, float(alpha), M=M_4D)
        tensor_bound, q_best = symmetric_tensor_bound_d4_diag(
            N, float(alpha), M=M_1D, M_angle=M_angle
        )
        P_min = verify_quadvariate_nonneg(c_tensor, M_test=M_verify)
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
              f"{gap:>+11.3e}  {rel_gap:>+9.4f}  {P_min:>10.3e}  {dt:>5.1f}s")

    peak_idx = int(np.argmax([r["rel_gap"] for r in results]))
    peak = results[peak_idx]
    print()
    print(f"  Peak relative gap: +{peak['rel_gap']*100:.2f}% at alpha = "
          f"{peak['alpha']:.3f}")
    print(f"  LP value at peak: {peak['lp_val']:.4f}")
    print(f"  Tensor bound at peak: {peak['tensor_bound']:.4f}")
    print(f"  P_min on verify grid: {peak['P_min']:.3e}")

    # M-corrected lower bracket
    lower = peak['lp_val'] / (1 + max(0, -peak['P_min']))
    lower_gap = (lower - peak['tensor_bound']) / peak['tensor_bound']
    print(f"  Lower bracket (LP/(1+|P_min|)): {lower:.4f}")
    print(f"  Gap interval: [{lower_gap*100:+.2f}%, {peak['rel_gap']*100:+.2f}%]")

    print()
    print(f"  Pattern test:")
    print(f"    d = 2 peak gap (4E.2): +25.00% at alpha = 3.00")
    print(f"    d = 3 peak gap (4E.4): +51.29% at alpha = 3.25 (M-corrected ~50%)")
    print(f"    d = 4 peak gap (4E.5): +{peak['rel_gap']*100:.2f}% at alpha = "
          f"{peak['alpha']:.2f}")
    print(f"    Predicted by (d-1) x 25%: d=4 -> +75%")
    if abs(peak['rel_gap'] - 0.75) < 0.10:
        print(f"    ==> Pattern (d-1) x 25% holds approximately")
    elif peak['rel_gap'] > 0.75:
        print(f"    ==> d = 4 gap EXCEEDS prediction; pattern may grow faster")
    else:
        print(f"    ==> d = 4 gap is BELOW prediction; pattern saturates")

    np.savez_compressed(
        out_dir / "e4e5_d4_peak.npz",
        N=N,
        M_4D=M_4D,
        alpha_grid=np.array(alpha_grid),
        lp_vals=np.array([r["lp_val"] for r in results]),
        tensor_bounds=np.array([r["tensor_bound"] for r in results]),
        gaps=np.array([r["gap"] for r in results]),
        rel_gaps=np.array([r["rel_gap"] for r in results]),
        P_mins=np.array([r["P_min"] for r in results]),
        peak_alpha=peak["alpha"],
        peak_rel_gap=peak["rel_gap"],
        peak_c_tensor=peak["c_tensor"],
    )

    fig, axs = plt.subplots(1, 2, figsize=(13, 5))
    alphas = [r["alpha"] for r in results]
    lps = [r["lp_val"] for r in results]
    tensors = [r["tensor_bound"] for r in results]
    rel_gaps = [r["rel_gap"] * 100 for r in results]

    ax = axs[0]
    ax.plot(alphas, lps, "bo-", label="LP value")
    ax.plot(alphas, tensors, "r--", label="symmetric tensor bound")
    ax.set_xlabel(r"$\alpha$ in $c_{1,1,1,1} + \alpha c_{2,2,2,2}$")
    ax.set_ylabel(f"value at $N = {N}, d = 4$")
    ax.set_title(f"4E.5: 4-variate LP at quad-degree ({N},{N},{N},{N})")
    ax.legend()
    ax.grid(alpha=0.3)

    ax = axs[1]
    ax.plot(alphas, rel_gaps, "go-", label="d = 4 (4E.5)")
    # Overlay d=2, d=3 for reference
    alpha_4e2 = [0, 0.5, 1, 2, 2.75, 3, 3.5, 4, 5, 10]
    rel_gap_4e2 = [0, 6.2, 12.1, 21.4, 24.8, 25.0, 24.0, 20.8, 14.1, 3.9]
    ax.plot(alpha_4e2, rel_gap_4e2, "ms--", alpha=0.5, label="d = 2 (4E.2)")
    alpha_4e4 = [0.25, 0.5, 1, 2, 2.5, 3, 3.25, 3.5, 4, 5, 10]
    rel_gap_4e4 = [4.33, 8.48, 16.5, 32.9, 41.0, 48.1, 51.3, 50.8, 41.4, 30.1, 9.7]
    ax.plot(alpha_4e4, rel_gap_4e4, "c^--", alpha=0.5, label="d = 3 (4E.4)")
    ax.axhline(75, color="gray", linestyle=":", alpha=0.5,
               label="(d-1) x 25% prediction at d = 4")
    ax.set_xlabel(r"$\alpha$")
    ax.set_ylabel("relative gap (% of tensor bound)")
    ax.set_title(f"4E.5: relative LP-vs-tensor gap across d")
    ax.legend()
    ax.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig(out_dir / "e4e5_d4_peak.png", dpi=140)
    plt.close()
    print()
    print(f"  Saved {out_dir / 'e4e5_d4_peak.png'}")
    print(f"  Saved {out_dir / 'e4e5_d4_peak.npz'}")

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, default=2)
    parser.add_argument("--M-4D", type=int, default=25)
    parser.add_argument("--M-verify", type=int, default=30)
    args = parser.parse_args()
    run(N=args.N, M_4D=args.M_4D, M_verify=args.M_verify)
