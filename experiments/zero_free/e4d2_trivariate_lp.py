"""Experiment 4D.2: Trivariate LP, testing the d-dimensional pattern (CORRECTED).

4D-ii found (in the corrected interpretation) that the bivariate LP at
bidegree (N, N) with c_{0,0} = 1 saturates the tensor-product witness
P = Q(theta) Q(phi) where Q is the 1D Fejér optimum:

    max c_{1,1} = (q_1)^2 = (2 cos(pi/(N+2)))^2 = 4 cos^2(pi/(N+2))

with q_1 = 2 c_1^{4B} the raw coefficient of cos(alpha) in Q. The bivariate
LP's coefficient matrix c_{j,k} is rank 1, equal to q_j q_k.

This experiment extends to d = 3 to confirm the same decomposition holds:

    max c_{1,1,1} =? (q_1)^3 = 8 cos^3(pi/(N+2))

over non-negative trivariate trig polynomials of tridegree (N, N, N) with
c_{0,0,0} = 1 in the basis
    P(theta, phi, psi) = sum_{0<=j,k,l<=N} c_{j,k,l}
                          cos(j theta) cos(k phi) cos(l psi) >= 0.

We expect the trivariate LP to also saturate at the tensor product
P = Q(theta) Q(phi) Q(psi). If so, the d-variate problem decomposes for
this objective: no new auxiliary inequality from this LP family.

(An earlier version of this experiment compared to (c_1^{4B})^3 and
reported a "factor-of-8 advantage." That was a convention error; the
proper tensor-product witness gives q_1^3 = (2 c_1^{4B})^3, matching
the LP value.)

Output:
  - e4d2_trivariate_lp.npz: per-N LP optimum and verification
  - e4d2_trivariate_lp.png: LP vs tensor product, M-convergence
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


def best_trivariate_c111(N: int, M: int = 30, bounds_abs: float = 20.0):
    """LP: maximize c_{1,1,1} over nonneg P(theta,phi,psi) of tridegree (N,N,N).

    P(theta, phi, psi) = sum_{0<=j,k,l<=N} c_{j,k,l}
                          cos(j theta) cos(k phi) cos(l psi) >= 0
    sampled on M x M x M uniform grid. c_{0,0,0} = 1.

    Variables flattened to (N+1)^3.
    """
    n_vars = (N + 1) ** 3
    theta = np.linspace(0, 2 * np.pi, M, endpoint=False)
    phi = np.linspace(0, 2 * np.pi, M, endpoint=False)
    psi = np.linspace(0, 2 * np.pi, M, endpoint=False)

    def idx(j, k, l):
        return j * (N + 1) ** 2 + k * (N + 1) + l

    # Objective: maximize c_{1,1,1}
    obj = np.zeros(n_vars)
    obj[idx(1, 1, 1)] = -1

    # Inequality constraint: -P(theta_a, phi_b, psi_c) <= 0 for all (a, b, c).
    # That's M^3 constraints.
    M3 = M ** 3
    A_ub = np.zeros((M3, n_vars))

    cos_j = np.array([np.cos(j * theta) for j in range(N + 1)])  # (N+1, M)
    cos_k = np.array([np.cos(k * phi) for k in range(N + 1)])
    cos_l = np.array([np.cos(l * psi) for l in range(N + 1)])

    # Build constraint matrix
    row = 0
    for a in range(M):
        for b in range(M):
            for c in range(M):
                # P(theta_a, phi_b, psi_c) = sum_{j,k,l} c_{j,k,l} * cos_j[j,a] * cos_k[k,b] * cos_l[l,c]
                for j in range(N + 1):
                    cja = cos_j[j, a]
                    if cja == 0:
                        continue
                    for k in range(N + 1):
                        ckb_cja = cja * cos_k[k, b]
                        if ckb_cja == 0:
                            continue
                        for l in range(N + 1):
                            A_ub[row, idx(j, k, l)] = -ckb_cja * cos_l[l, c]
                row += 1
    b_ub = np.zeros(M3)

    A_eq = np.zeros((1, n_vars))
    A_eq[0, idx(0, 0, 0)] = 1
    b_eq = np.array([1.0])

    bounds = [(-bounds_abs, bounds_abs)] * n_vars

    res = linprog(
        obj, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method="highs"
    )
    if not res.success:
        raise RuntimeError(f"3D LP failed at N={N}: {res.message}")
    c_max = -res.fun
    c_tensor = res.x.reshape((N + 1, N + 1, N + 1))
    return float(c_max), c_tensor


def verify_trivariate_nonneg(c_tensor, M_test: int = 80):
    """Verify P(theta, phi, psi) >= 0 on M_test^3 grid via tensor contraction."""
    N = c_tensor.shape[0] - 1
    theta = np.linspace(0, 2 * np.pi, M_test, endpoint=False)
    phi = np.linspace(0, 2 * np.pi, M_test, endpoint=False)
    psi = np.linspace(0, 2 * np.pi, M_test, endpoint=False)
    cos_j = np.array([np.cos(j * theta) for j in range(N + 1)])  # (N+1, M)
    cos_k = np.array([np.cos(k * phi) for k in range(N + 1)])
    cos_l = np.array([np.cos(l * psi) for l in range(N + 1)])
    # P[a, b, c] = sum_{j,k,l} c_tensor[j,k,l] cos_j[j,a] cos_k[k,b] cos_l[l,c]
    # einsum: 'jkl,ja,kb,lc -> abc'
    P = np.einsum("jkl,ja,kb,lc->abc", c_tensor, cos_j, cos_k, cos_l)
    return float(P.min()), float(P.max())


def run(
    N_max: int = 3,
    M_3D: int = 30,
    M_verify: int = 80,
    out_dir: Path = None,
):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"[4D.2] Trivariate LP at tridegree (N, N, N), M = {M_3D}, M_verify = {M_verify}")
    print(f"       Testing conjecture max c_{{1,1,1}} = 8 cos^3(pi/(N+2))")
    print()

    results = []
    for N in range(1, N_max + 1):
        t0 = time.time()
        c111, c_tensor = best_trivariate_c111(N, M=M_3D)
        dt_lp = time.time() - t0
        t0 = time.time()
        P_min, P_max = verify_trivariate_nonneg(c_tensor, M_test=M_verify)
        dt_verify = time.time() - t0

        c1_4B = float(np.cos(np.pi / (N + 2)))
        q1_raw = 2 * c1_4B  # raw coefficient of cos(alpha) in 1D Fejér optimum Q
        tensor_prediction = q1_raw ** 3  # = 8 cos^3(pi/(N+2))
        diff_from_tensor = c111 - tensor_prediction

        results.append({
            "N": N, "c111": c111, "c_tensor": c_tensor,
            "tensor_prediction": tensor_prediction,
            "diff": diff_from_tensor,
            "P_min": P_min, "P_max": P_max,
            "dt_lp": dt_lp, "dt_verify": dt_verify,
        })

        print(f"   N = {N}:")
        print(f"     LP max c_{{1,1,1}} = {c111:.10f}     (lp {dt_lp:.1f}s)")
        print(f"     tensor product Q(theta) Q(phi) Q(psi):  c_{{1,1,1}} = (2 cos(pi/{N+2}))^3 = {tensor_prediction:.10f}")
        print(f"     diff = LP - tensor              = {diff_from_tensor:+.4e}")
        print(f"     P_min on {M_verify}^3 verify grid: {P_min:.4e}  (P_max: {P_max:.2f})")
        print()

    # M-convergence study at N = 2
    print(f"[4D.2] M-convergence study at N = 2:")
    print(f"       M_3D   |  LP value   |  LP - tensor  |  P_min on M_verify")
    convergence_Ms = [20, 30, 50, 70]
    conv_c111 = []
    conv_excess = []
    conv_Pmin = []
    N_conv = 2
    tensor_N2 = (2 * np.cos(np.pi / (N_conv + 2))) ** 3
    for Mc in convergence_Ms:
        c111c, c_tensorc = best_trivariate_c111(N_conv, M=Mc)
        Pminc, _ = verify_trivariate_nonneg(c_tensorc, M_test=M_verify)
        excess = c111c - tensor_N2
        conv_c111.append(c111c)
        conv_excess.append(excess)
        conv_Pmin.append(Pminc)
        print(f"       {Mc:>5}  |  {c111c:.10f}  |  {excess:+.4e}  |  {Pminc:+.4e}")

    # Save
    save_dict = {
        "Ns": np.array([r["N"] for r in results]),
        "c111_values": np.array([r["c111"] for r in results]),
        "tensor_predictions": np.array([r["tensor_prediction"] for r in results]),
        "P_min_verify": np.array([r["P_min"] for r in results]),
        "M_3D": M_3D,
        "M_verify": M_verify,
        "convergence_Ms": np.array(convergence_Ms),
        "convergence_c111_N2": np.array(conv_c111),
        "convergence_excess_N2": np.array(conv_excess),
        "convergence_Pmin_N2": np.array(conv_Pmin),
        "convergence_tensor_N2": tensor_N2,
    }
    for r in results:
        save_dict[f"c_tensor_N{r['N']}"] = r["c_tensor"]
    np.savez_compressed(out_dir / "e4d2_trivariate_lp.npz", **save_dict)

    # Plot
    fig, axs = plt.subplots(1, 3, figsize=(15, 4.5))
    Ns = [r["N"] for r in results]

    ax = axs[0]
    ax.plot(Ns, [r["c111"] for r in results], "mo-", markersize=10, label="LP max $c_{1,1,1}$")
    ax.plot(Ns, [r["tensor_prediction"] for r in results], "k--",
            label=r"tensor product $Q(\theta)Q(\phi)Q(\psi)$: $(2\cos\frac{\pi}{N+2})^3$")
    ax.set_xlabel("tridegree $N$")
    ax.set_ylabel(r"$c_{1,1,1}$")
    ax.set_title("4D.2: 3D LP saturates the tensor-product witness")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    ax = axs[1]
    diffs = [abs(r["diff"]) for r in results]
    diffs_floor = [max(d, 1e-16) for d in diffs]
    ax.semilogy(Ns, diffs_floor, "ro-", markersize=10, label="|LP - tensor|")
    Pmin_abs = [max(abs(r["P_min"]), 1e-16) for r in results]
    ax.semilogy(Ns, Pmin_abs, "bs-", markersize=10, label="|P_min| (LP relaxation gap)")
    ax.axhline(1e-10, color="k", linestyle="--", alpha=0.4, label="$10^{-10}$ floor")
    ax.set_xlabel("tridegree $N$")
    ax.set_ylabel("magnitude")
    ax.set_title(f"Per-N: LP - tensor vs LP grid violation\n(M_3D = {M_3D})")
    ax.legend()
    ax.grid(alpha=0.3, which="both")

    ax = axs[2]
    ax.semilogy(convergence_Ms, [abs(x) for x in conv_excess], "ro-",
                label="|LP - tensor| at N=2")
    ax.semilogy(convergence_Ms, [abs(x) for x in conv_Pmin], "bs-",
                label="|P_min| at N=2")
    # Reference slope 1/M
    Ms_arr = np.array(convergence_Ms, dtype=float)
    ref_1overM = 1.0 / Ms_arr * abs(conv_excess[0]) * Ms_arr[0]
    ax.semilogy(Ms_arr, ref_1overM, "k:", alpha=0.5, label="$\\propto 1/M$")
    ax.set_xlabel("M_3D")
    ax.set_ylabel("magnitude")
    ax.set_title("M-convergence at N=2")
    ax.legend()
    ax.grid(alpha=0.3, which="both")

    plt.tight_layout()
    plt.savefig(out_dir / "e4d2_trivariate_lp.png", dpi=140)
    plt.close()
    print(f"[4D.2] Saved {out_dir / 'e4d2_trivariate_lp.png'}")
    print(f"[4D.2] Saved {out_dir / 'e4d2_trivariate_lp.npz'}")

    # Verdict using interval bounds: true_max in [LP / (1 + |P_min|), LP].
    print()
    print(f"[4D.2] Verdict (corrected interpretation):")
    print(f"       LP at finite M is a relaxation: LP value upper-bounds the")
    print(f"       true continuum max. Projecting the LP polynomial to feasibility")
    print(f"       gives lower bound LP / (1 + |P_min|). So true max lies in")
    print(f"       [LP / (1 + |P_min|), LP], which should bracket the tensor-product")
    print(f"       prediction (2 cos(pi/(N+2)))^3.")
    print()
    print(f"       Per-N interval bounds at M_3D = {M_3D}:")
    bracket_holds = True
    for r in results:
        viol = abs(r["P_min"]) if r["P_min"] < 0 else 0.0
        lower = r["c111"] / (1 + viol)
        upper = r["c111"]
        in_bracket = lower - 1e-12 <= r["tensor_prediction"] <= upper + 1e-12
        if not in_bracket:
            bracket_holds = False
        print(f"         N = {r['N']}: true in [{lower:.6f}, {upper:.6f}], "
              f"tensor = {r['tensor_prediction']:.6f}, in bracket? {in_bracket}")
    print()

    if bracket_holds:
        print()
        print(f"       => The 3D LP saturates the tensor-product witness P = ")
        print(f"          Q(theta) Q(phi) Q(psi) where Q is the 1D Fejér optimum.")
        print(f"          The d-variate problem decomposes at d = 1, 2, 3:")
        print(f"             max c_{{1, ..., 1}} = q_1^d = (2 cos(pi/(N+2)))^d")
        print(f"          where q_1 is the raw coefficient of cos(alpha) in Q.")
        print(f"          No new auxiliary inequality is found at this LP family;")
        print(f"          the d-variate inequality is just the d-th power of the")
        print(f"          1D Fejér inequality.")
    else:
        print()
        print(f"       => Tensor product prediction falls outside the LP bracket.")
        print(f"          The d=3 problem may NOT decompose. Investigate.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--N-max", type=int, default=3)
    parser.add_argument("--M-3D", type=int, default=30)
    parser.add_argument("--M-verify", type=int, default=80)
    args = parser.parse_args()
    run(N_max=args.N_max, M_3D=args.M_3D, M_verify=args.M_verify)
