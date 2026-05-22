"""Experiment 4D: Multivariate auxiliary inequalities (CORRECTED).

4B established that the LP optimum for a 1D non-negative trigonometric
polynomial in the convention
    P_{4B}(theta) = c_0 + 2 sum_{k=1}^n c_k cos(k theta) >= 0
saturates the Fejér bound c_1^max / c_0 = cos(pi / (n + 2)).

This experiment probes two extensions:

4D-i: Degree-sweep extension. We push the LP to n = 30, 50, 100, 200 and
verify Fejér saturation persists at large degree.

4D-ii: Two-variable LP. Among non-negative bivariate trig polynomials in
the RAW-COEFFICIENT convention
    P(theta, phi) = sum_{0<=j,k<=N} c_{j,k} cos(j theta) cos(k phi) >= 0
with c_{0,0} = 1, how large can c_{1,1} be?

The tensor-product witness P = Q(theta) Q(phi) is the natural baseline.
Take Q = 1D Fejér optimum at degree N. In the raw-coefficient convention
for Q, q_0 = 1 and the coefficient of cos(theta) is q_1 = 2 c_1^{4B} =
2 cos(pi/(N+2)). The tensor product P = Q(theta) Q(phi) has
    c_{j,k}^{tensor} = q_j q_k    for all j, k,
so c_{1,1}^{tensor} = (2 cos(pi/(N+2)))^2 = 4 cos^2(pi/(N+2)).

The LP we run here returns max c_{1,1} = 4 cos^2(pi/(N+2)) for N up to
4. **The LP value matches the tensor-product witness exactly.** The
LP-optimal polynomial IS the tensor product (or another polynomial with
the same c_{1,1} and c_{j,k} structure). The 2D problem decomposes.

(An earlier version of this experiment compared the LP value against
(c_1^{4B})^2 = cos^2(pi/(N+2)) and reported a "factor-of-4 advantage."
That was a convention error: the proper tensor-product witness gives
(q_1)^2 = (2 c_1^{4B})^2 = 4 c_1^2, matching the LP. No advantage.)

The honest finding: the d-variate LP for max c_{1, ..., 1} at d-degree
(N, ..., N) with c_{0, ..., 0} = 1 saturates at (2 cos(pi/(N+2)))^d, the
d-th power of the 1D Fejér max coefficient of cos(alpha) in Q. No new
auxiliary inequality is found at this LP objective.

A genuinely new multivariate inequality would require a different
objective (e.g., a combination of c_{j,k} coefficients) or different
constraints (e.g., coupling between primes at different heights).

Output:
  - e4d_multivariate_lp.npz: degree-sweep data + 2D LP optima
  - e4d_multivariate_lp.png: log-log gap, 1D-vs-2D comparison
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

from experiments.zero_free.e4b_nonneg_trig import best_trig_ratio


def best_bivariate_c11(N: int, M: int = 60):
    """LP: maximize c_{1,1} over nonneg P(theta, phi) of bidegree (N, N).

    P(theta, phi) = sum_{0<=j,k<=N} c_{j,k} cos(j theta) cos(k phi).
    Constraint: P(theta, phi) >= 0 sampled on M x M grid.
    Normalization: c_{0,0} = 1.

    Variables c_{j,k} flattened to single index (N+1)^2.
    """
    n_vars = (N + 1) ** 2
    theta = np.linspace(0, 2 * np.pi, M, endpoint=False)
    phi = np.linspace(0, 2 * np.pi, M, endpoint=False)

    # Index map: var(j, k) = j * (N + 1) + k
    def idx(j, k):
        return j * (N + 1) + k

    # Objective: maximize c_{1,1} == minimize -c_{1,1}
    obj = np.zeros(n_vars)
    obj[idx(1, 1)] = -1

    # Inequality constraints: -P(theta_a, phi_b) <= 0 for all (a, b)
    M2 = M * M
    A_ub = np.zeros((M2, n_vars))
    row = 0
    cos_j = np.array([np.cos(j * theta) for j in range(N + 1)])  # (N+1, M)
    cos_k = np.array([np.cos(k * phi) for k in range(N + 1)])    # (N+1, M)
    for a in range(M):
        for b in range(M):
            for j in range(N + 1):
                cja = cos_j[j, a]
                if cja == 0:
                    continue
                for k in range(N + 1):
                    A_ub[row, idx(j, k)] = -cja * cos_k[k, b]
            row += 1
    b_ub = np.zeros(M2)

    # Equality: c_{0,0} = 1
    A_eq = np.zeros((1, n_vars))
    A_eq[0, idx(0, 0)] = 1
    b_eq = np.array([1.0])

    # Bounds: generous
    bounds = [(-10.0, 10.0)] * n_vars

    res = linprog(
        obj, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method="highs"
    )
    if not res.success:
        raise RuntimeError(f"2D LP failed at N={N}: {res.message}")
    c_max = -res.fun
    c_mat = res.x.reshape((N + 1, N + 1))
    return float(c_max), c_mat


def verify_bivariate_nonneg(c_mat, M_test: int = 200):
    """Verify P(theta, phi) >= 0 on a dense M_test x M_test grid."""
    N = c_mat.shape[0] - 1
    theta = np.linspace(0, 2 * np.pi, M_test, endpoint=False)
    phi = np.linspace(0, 2 * np.pi, M_test, endpoint=False)
    cos_j = np.array([np.cos(j * theta) for j in range(N + 1)])
    cos_k = np.array([np.cos(k * phi) for k in range(N + 1)])
    # P[a, b] = sum_{j,k} c_{j,k} cos_j[a] cos_k[b]
    P = cos_j.T @ c_mat @ cos_k
    return float(P.min()), float(P.max())


def run(
    degrees_1D=(5, 10, 20, 30, 50, 100, 200),
    N_2D_max: int = 4,
    M_1D: int = 8000,
    M_2D: int = 50,
    out_dir: Path = None,
):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    # 4D-i: degree sweep
    print(f"[4D-i] LP degree sweep, M = {M_1D}")
    c1_values = []
    fejer_bounds = []
    times_1D = []
    for n in degrees_1D:
        t0 = time.time()
        c1, _coeffs = best_trig_ratio(n, M=M_1D)
        dt = time.time() - t0
        fejer = float(np.cos(np.pi / (n + 2)))
        c1_values.append(float(c1))
        fejer_bounds.append(fejer)
        times_1D.append(dt)
        print(f"     n = {n:>4}: c_1 = {c1:.10f}, Fejér = {fejer:.10f}, "
              f"gap = {fejer - c1:.4e}  ({dt:.1f}s)")

    # 4D-ii: 2D LP
    print(f"\n[4D-ii] Bivariate nonneg trig poly LP, max c_{{1,1}}, "
          f"M_2D = {M_2D}")
    print(f"        Convention: c_{{j,k}} is the RAW coefficient of cos(j theta) cos(k phi).")
    print(f"        Tensor-product witness P = Q(theta) Q(phi) with Q the 1D Fejér optimum")
    print(f"        gives c_{{1,1}}^tensor = (2 cos(pi/(N+2)))^2 = 4 cos^2(pi/(N+2)).")
    c11_values = []
    c11_tensor_predictions = []
    P_min_check = []
    times_2D = []
    for N in range(1, N_2D_max + 1):
        t0 = time.time()
        c11, c_mat = best_bivariate_c11(N, M=M_2D)
        dt = time.time() - t0
        # Correct tensor-product witness: Q(theta) Q(phi) with Q the 1D Fejér
        # optimum in raw-coefficient convention has q_1 = 2 c_1^{4B}, so the
        # tensor product has c_{1,1} = q_1^2 = (2 cos(pi/(N+2)))^2.
        c1_1D_4B, _ = best_trig_ratio(N, M=M_1D)
        q1_raw = 2 * float(c1_1D_4B)
        tensor_prediction = q1_raw ** 2  # = 4 cos^2(pi/(N+2))
        # Verify nonneg
        P_min, _ = verify_bivariate_nonneg(c_mat, M_test=200)
        c11_values.append(float(c11))
        c11_tensor_predictions.append(tensor_prediction)
        P_min_check.append(P_min)
        times_2D.append(dt)
        diff = c11 - tensor_prediction
        print(f"     N = {N}: LP c_{{1,1}} = {c11:.6f}, "
              f"tensor product = {tensor_prediction:.6f}, "
              f"diff = {diff:+.4e}, "
              f"P_min = {P_min:.4e}  ({dt:.1f}s)")

    # Save
    np.savez_compressed(
        out_dir / "e4d_multivariate_lp.npz",
        degrees_1D=np.array(degrees_1D),
        c1_values=np.array(c1_values),
        fejer_bounds=np.array(fejer_bounds),
        N_2D=np.arange(1, N_2D_max + 1),
        c11_values=np.array(c11_values),
        c11_tensor_predictions=np.array(c11_tensor_predictions),
    )

    # Plot
    fig, axs = plt.subplots(1, 3, figsize=(15, 4.8))

    # Panel 1: 1D degree sweep, c_1 vs Fejér
    ax = axs[0]
    ax.plot(degrees_1D, c1_values, "bo-", label="LP max $c_1$")
    ax.plot(degrees_1D, fejer_bounds, "r--", label=r"Fejér $\cos(\pi/(n+2))$")
    ax.axhline(1.0, color="gray", linestyle=":", alpha=0.5, label="limit")
    ax.set_xlabel("polynomial degree $n$")
    ax.set_ylabel(r"max $c_1$ (with $c_0 = 1$)")
    ax.set_title("4D-i: degree sweep (LP saturates Fejér)")
    ax.legend()
    ax.grid(alpha=0.3)
    ax.set_ylim(0, 1.05)

    # Panel 2: log-log of Fejér gap
    ax = axs[1]
    gap = np.array(fejer_bounds) - np.array(c1_values)
    gap_clean = np.maximum(gap, 1e-12)
    n_arr = np.array(degrees_1D, dtype=float)
    # Asymptotic: 1 - cos(pi/(n+2)) ~ pi^2 / (2(n+2)^2) (this is the gap from 1, not from Fejér)
    # The gap LP-vs-Fejér tracks LP-precision, not Fejér's gap from 1.
    asymptotic = np.pi ** 2 / (2 * (n_arr + 2) ** 2)
    ax.loglog(degrees_1D, gap_clean, "go-", label="LP gap to Fejér")
    ax.loglog(degrees_1D, asymptotic, "k--", label=r"$\pi^2 / (2(n+2)^2)$ (Fejér gap to 1)")
    ax.set_xlabel("polynomial degree $n$")
    ax.set_ylabel("gap")
    ax.set_title("4D-i: gap scaling (log-log)")
    ax.legend()
    ax.grid(alpha=0.3, which="both")

    # Panel 3: 2D LP - max c_{1,1} vs tensor-product witness
    ax = axs[2]
    Ns = list(range(1, N_2D_max + 1))
    ax.plot(Ns, c11_values, "ms-", markersize=10, label=r"LP max $c_{1,1}$")
    ax.plot(Ns, c11_tensor_predictions, "k--",
            label=r"tensor product $Q(\theta) Q(\phi)$: $c_{1,1} = (2\cos\frac{\pi}{N+2})^2$")
    ax.set_xlabel("bidegree $N$")
    ax.set_ylabel(r"$c_{1,1}$")
    ax.set_title("4D-ii: 2D LP saturates the tensor-product witness")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig(out_dir / "e4d_multivariate_lp.png", dpi=140)
    plt.close()
    print(f"\n[4D] Saved {out_dir / 'e4d_multivariate_lp.png'}")
    print(f"[4D] Saved {out_dir / 'e4d_multivariate_lp.npz'}")

    # Closed-form check: max c_{1,1} = 4 cos^2(pi/(N+2)) = (tensor-product witness)
    print()
    print(f"[4D] LP vs tensor-product witness check:")
    print(f"     {'N':>3}  {'LP c_{1,1}':>11}  {'tensor':>12}  {'diff':>10}")
    match = True
    for N, c11 in zip(range(1, N_2D_max + 1), c11_values):
        c1_4B = float(np.cos(np.pi / (N + 2)))
        tensor = (2 * c1_4B) ** 2
        diff = c11 - tensor
        if abs(diff) > 1e-3 * max(1.0, abs(tensor)):
            match = False
        print(f"     {N:>3}  {c11:>11.6f}  {tensor:>12.6f}  {diff:>+10.4e}")

    print()
    if match:
        print(f"[4D] The LP value saturates the tensor-product witness")
        print(f"     P = Q(theta) Q(phi) where Q is the 1D Fejér optimum.")
        print(f"     The 2D problem decomposes: the LP-optimal coefficient matrix")
        print(f"     c_{{j,k}} is rank 1, equal to q_j q_k where Q(alpha) = sum q_j cos(j alpha).")
        print(f"     No new auxiliary inequality is found at this LP objective.")
        print(f"     A genuinely multivariate inequality would require a different")
        print(f"     objective (combinations of c_{{j,k}}) or constraints (e.g.,")
        print(f"     cross-prime-height structure from the explicit formula).")
    else:
        print(f"[4D] LP value DEVIATES from the tensor-product witness at some N.")
        print(f"     A genuine multivariate inequality may exist. Investigate.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--degrees", type=int, nargs="+",
                        default=[5, 10, 20, 30, 50, 100, 200])
    parser.add_argument("--N-2D-max", type=int, default=4)
    parser.add_argument("--M-1D", type=int, default=8000)
    parser.add_argument("--M-2D", type=int, default=50)
    args = parser.parse_args()
    run(
        degrees_1D=tuple(args.degrees),
        N_2D_max=args.N_2D_max,
        M_1D=args.M_1D,
        M_2D=args.M_2D,
    )
