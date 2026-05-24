"""Experiment 4E.7: multi-zero Mossinghoff-Trudgian LP.

4E.6 confirmed that constrained-domain LP does NOT escape the 4E.3
line-restriction lemma. The remaining proposed escape: multi-zero MT
bookkeeping (Heath-Brown / Pintz style).

The setup: instead of bounding one putative off-line zero, postulate
TWO (or more) zeros at independent heights gamma_1, gamma_2 (both with
the same beta < 1 by FE pairing). The MT trick becomes a multivariate
LP because the polynomial P now lives on independent frequency variables
theta_1 = gamma_1 * log p, theta_2 = gamma_2 * log p, etc.

Crucially: the constraint set in this LP is FULL multivariate non-
negativity ([0, 2pi]^d) -- NOT a 1D line restriction. So 4E.3's
structural lemma does not directly apply. The multi-zero LP can in
principle achieve shape factors that the single-zero LP cannot.

The natural question: does it?

This experiment computes a sequence of multi-zero LP analogs of the
MT shape factor and compares to the single-zero baseline.

Objectives tested (for non-neg P(theta_1, ..., theta_d) of d-degree
(N, ..., N), c_{0,...,0} = 1):

  Single-zero baseline (d=1):
    lambda_1(N) := (max c_1 - 1)^2 / 4 = (q_1 - 1)^2 / 4
    where q_1 = 2 cos(pi/(N+2)) is the 1D Fejer optimum.

  Two-zero joint (d=2):
    lambda_{1,1}(N) := (max c_{1,1} - 1)^2 / 4 = (q_1^2 - 1)^2 / 4
    (since 4D-ii showed max c_{1,1} = q_1^2 = tensor product).

  Two-zero balanced sum (d=2):
    lambda_balanced(N, alpha) := (LP_max[c_{1,0} + c_{0,1} + alpha c_{1,1}] - 1)^2 / 4
    Sweep alpha to find the peak.

  Heath-Brown style "diagonal-with-individual" objective (d=2):
    Combine individual zero contributions and joint:
    max  a c_{1,0} + a c_{0,1} + b c_{1,1}
    over non-neg P, sweep (a, b) weights.

We then translate each shape factor to the corresponding zero-free
region constant using the multi-zero MT scaling:

  Single-zero MT: eta >= C_1 / log T,  C_1 = lambda_1 / R(P_1)
  Two-zero MT:    eta >= C_2 / log^2 T,  C_2 = lambda_{1,1} / R(P_2)

Heath-Brown's actual zero-free region improvement comes from the
COMBINATION of these (suitably weighted), giving improvements that
asymptotically beat single-zero MT for specific problems (least prime
in AP, Siegel zeros).

For RH on zeta, the relevant question is whether the multi-zero LP
produces shape factors that translate to a non-trivial improvement of
the de la Vallee Poussin constant. The simple version: lambda_{1,1}
exceeds lambda_1^2 (which would be the naive two-independent-zero
bound) -- so multi-zero IS strictly tighter than two-independent.

We compute and document this for d = 2 at various N, and for the
two-zero balanced-sum LP we sweep alpha to find the peak.

CAVEAT: translating LP shape factors to an actual zero-free region
constant requires the full MT explicit-formula bookkeeping with
multiple zeros, which we do NOT implement here. This experiment
records the LP structure and notes what would need to follow.

Output:
  - e4e7_multi_zero_lp.npz: LP values, shape factors, alpha sweeps
  - e4e7_multi_zero_lp.png: comparison single-zero vs multi-zero shapes
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from experiments.zero_free.e4e_offdiag_lp import (
    best_1D_raw_qj,
    best_bivariate_objective,
    numerical_rank,
)


def fejer_q1(N: int) -> float:
    """1D Fejer optimum coefficient: q_1 = 2 cos(pi/(N+2))."""
    return float(2 * np.cos(np.pi / (N + 2)))


def single_zero_shape(N: int) -> dict:
    """Single-zero MT shape factor (1D Fejer).

    lambda_1 = (q_1 - 1)^2 / 4
    Achieved at q_0 = 1, q_1 = q_1^{Fejer}.
    """
    q1 = fejer_q1(N)
    shape = (q1 - 1) ** 2 / 4.0
    return {"N": N, "q1": q1, "shape": shape, "objective": "single-zero c_1"}


def two_zero_diagonal_shape(N: int, M: int = 100) -> dict:
    """Two-zero joint shape factor.

    LP: max c_{1,1} over non-neg P(theta, phi) at bidegree (N, N),
    c_{0,0} = 1. By 4D-ii, this equals q_1^2 (tensor product).
    Shape: lambda_{1,1} = (max c_{1,1} - 1)^2 / 4 = (q_1^2 - 1)^2 / 4.
    """
    obj = {(1, 1): 1.0}
    lp_val, c_mat = best_bivariate_objective(N, obj, M=M)
    expected_tensor = fejer_q1(N) ** 2
    shape = (lp_val - 1) ** 2 / 4.0
    rank, sv = numerical_rank(c_mat)
    return {
        "N": N,
        "M": M,
        "lp_val": lp_val,
        "tensor_q1_sq": expected_tensor,
        "lp_minus_tensor": lp_val - expected_tensor,
        "shape": shape,
        "rank": rank,
        "singular_values_top3": sv[:3] if len(sv) >= 3 else sv,
        "objective": "two-zero joint c_{1,1}",
    }


def two_zero_balanced_sum(N: int, alpha: float, M: int = 100) -> dict:
    """LP: max c_{1,0} + c_{0,1} + alpha * c_{1,1} over non-neg P at bidegree (N, N).

    For alpha = 0 this is "individual contributions only" (decomposes by
    symmetry). For alpha > 0, the joint coupling enters.

    Note: c_{1,0} and c_{0,1} correspond to single-zero contributions
    (one zero at gamma_1, the other "off"). c_{1,1} is the genuine
    two-zero cross coupling.
    """
    obj = {(1, 0): 1.0, (0, 1): 1.0, (1, 1): float(alpha)}
    lp_val, c_mat = best_bivariate_objective(N, obj, M=M)
    rank, sv = numerical_rank(c_mat)
    # Extract individual coefficients from c_mat
    c10 = c_mat[1, 0] if c_mat.shape[0] > 1 else 0.0
    c01 = c_mat[0, 1] if c_mat.shape[1] > 1 else 0.0
    c11 = c_mat[1, 1] if c_mat.shape[0] > 1 and c_mat.shape[1] > 1 else 0.0
    return {
        "N": N,
        "alpha": alpha,
        "lp_val": lp_val,
        "c_10": c10,
        "c_01": c01,
        "c_11": c11,
        "rank": rank,
        "singular_values_top3": sv[:3] if len(sv) >= 3 else sv,
    }


def heath_brown_style_objective(N: int, a: float, b: float, M: int = 100) -> dict:
    """Heath-Brown-style objective: a*(c_{1,0} + c_{0,1}) + b*c_{1,1}.

    Captures the two-zero MT inequality with weights for individual
    zero contributions (a) and joint coupling (b). The MT shape factor
    structure: shape_HB := (LP_val - (a+a) c_{0,0})^2 / (4 c_{0,0})
                        = (LP_val - 2a)^2 / 4

    For comparison: the naive "two independent zeros" bound would be
    2 * a * (max c_1) - 2a = 2 a (q_1 - 1), giving shape (2a(q_1-1))^2/4.
    """
    obj = {(1, 0): a, (0, 1): a, (1, 1): float(b)}
    lp_val, c_mat = best_bivariate_objective(N, obj, M=M)
    # Joint shape: comparing LP value to a + a (the "independent" baseline)
    independent_baseline = 2 * a * fejer_q1(N)
    shape_HB = (lp_val - 2 * a) ** 2 / 4.0
    shape_independent = (independent_baseline - 2 * a) ** 2 / 4.0
    return {
        "N": N,
        "a": a,
        "b": b,
        "lp_val": lp_val,
        "independent_baseline": independent_baseline,
        "shape_HB": shape_HB,
        "shape_independent": shape_independent,
        "ratio_HB_to_indep": shape_HB / shape_independent if shape_independent > 0 else float("inf"),
    }


def run(out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 78)
    print("[4E.7] Multi-zero Mossinghoff-Trudgian LP")
    print("=" * 78)

    # Single-zero baseline
    print()
    print("[4E.7.1] Single-zero MT shape factor (1D Fejer):")
    print(f"  {'N':>3} {'q_1':>8} {'shape_1':>12} {'q_1 - 1':>10}")
    single_zero_data = []
    for N in [2, 3, 4, 6, 8, 10]:
        d = single_zero_shape(N)
        print(f"  {N:>3} {d['q1']:>8.4f} {d['shape']:>12.6f} "
              f"{d['q1'] - 1:>10.4f}")
        single_zero_data.append(d)

    # Two-zero joint shape (max c_{1,1})
    print()
    print("[4E.7.2] Two-zero joint shape (max c_{1,1}):")
    print(f"  {'N':>3} {'LP c_11':>10} {'q_1^2':>10} {'shape_11':>12} {'rank':>5}")
    two_zero_data = []
    for N in [2, 3, 4]:
        d = two_zero_diagonal_shape(N, M=80)
        print(f"  {N:>3} {d['lp_val']:>10.4f} {d['tensor_q1_sq']:>10.4f} "
              f"{d['shape']:>12.6f} {d['rank']:>5d}")
        two_zero_data.append(d)

    # Compare two-zero vs (single-zero)^2 (naive independent two-zero bound)
    print()
    print("[4E.7.3] Two-zero shape vs naive independent two-zero shape:")
    print(f"  Naive: lambda_1^2 = ((q_1 - 1)^2 / 4)^2  (two independent MT applications)")
    print(f"  Joint: lambda_{{1,1}} = (q_1^2 - 1)^2 / 4  (joint LP optimum)")
    print(f"  {'N':>3} {'lambda_1^2':>12} {'lambda_{1,1}':>12} {'ratio':>8} {'strict?':>10}")
    for N in [2, 3, 4]:
        l1_sq = single_zero_shape(N)["shape"] ** 2
        l11 = two_zero_diagonal_shape(N, M=60)["shape"]
        ratio = l11 / l1_sq if l1_sq > 0 else float("inf")
        strict = "YES (tighter)" if l11 > l1_sq else "no"
        print(f"  {N:>3} {l1_sq:>12.6f} {l11:>12.6f} {ratio:>8.2f} {strict:>10}")
    print()
    print("  Reading: lambda_{1,1} > lambda_1^2 means the joint LP gives a")
    print("  tighter MT-style bound than two independent single-zero applications.")
    print("  This is the Heath-Brown intuition: zeros interact in the explicit-")
    print("  formula sum, not just add up.")

    # Balanced sum sweep
    print()
    print("[4E.7.4] Two-zero balanced sum: max c_{1,0} + c_{0,1} + alpha c_{1,1}")
    print(f"  alpha sweep at N = 3:")
    print(f"  {'alpha':>8} {'LP val':>10} {'c_10':>8} {'c_01':>8} {'c_11':>8} {'rank':>5}")
    alphas = np.array([0.0, 0.5, 1.0, 2.0, 3.0, 5.0])
    balanced_data = []
    for alpha in alphas:
        d = two_zero_balanced_sum(3, alpha, M=80)
        balanced_data.append(d)
        print(f"  {alpha:>8.2f} {d['lp_val']:>10.4f} {d['c_10']:>8.4f} "
              f"{d['c_01']:>8.4f} {d['c_11']:>8.4f} {d['rank']:>5d}")

    # Heath-Brown style objective
    print()
    print("[4E.7.5] Heath-Brown-style: max a(c_{1,0} + c_{0,1}) + b c_{1,1}")
    print(f"  Sweep (a, b) at N = 3, shape factors and ratio to independent:")
    print(f"  {'a':>5} {'b':>5} {'LP val':>10} {'shape_HB':>10} {'shape_indep':>12} "
          f"{'HB/indep':>10}")
    hb_data = []
    for a, b in [(1.0, 0.0), (1.0, 1.0), (1.0, 2.0), (0.5, 1.0), (0.5, 2.0),
                  (0.0, 1.0)]:
        d = heath_brown_style_objective(3, a, b, M=80)
        hb_data.append(d)
        print(f"  {a:>5.2f} {b:>5.2f} {d['lp_val']:>10.4f} "
              f"{d['shape_HB']:>10.4f} {d['shape_independent']:>12.4f} "
              f"{d['ratio_HB_to_indep']:>10.3f}")

    # Plot
    fig, axs = plt.subplots(1, 3, figsize=(15, 4.5))

    # Panel 1: single-zero shape vs N
    ax = axs[0]
    Ns = [d["N"] for d in single_zero_data]
    shapes_1 = [d["shape"] for d in single_zero_data]
    ax.plot(Ns, shapes_1, "o-", color="C0", label="single-zero $\\lambda_1$")
    ax.set_xlabel("polynomial degree $N$")
    ax.set_ylabel("MT shape factor")
    ax.set_title("Single-zero MT shape (1D Fejér)")
    ax.legend()
    ax.grid(alpha=0.3)

    # Panel 2: two-zero shape vs single-zero^2
    ax = axs[1]
    Ns_2 = [d["N"] for d in two_zero_data]
    shapes_11 = [d["shape"] for d in two_zero_data]
    shapes_1_sq = [single_zero_shape(N)["shape"] ** 2 for N in Ns_2]
    ax.plot(Ns_2, shapes_11, "s-", color="C1", label="joint $\\lambda_{1,1}$")
    ax.plot(Ns_2, shapes_1_sq, "x--", color="C0",
            label="naive $\\lambda_1^2$ (two independent)")
    ax.set_xlabel("polynomial degree $N$")
    ax.set_ylabel("MT shape factor")
    ax.set_title("Two-zero joint vs independent")
    ax.legend()
    ax.grid(alpha=0.3)
    ax.set_yscale("log")

    # Panel 3: balanced-sum LP value vs alpha
    ax = axs[2]
    alphas_plot = [d["alpha"] for d in balanced_data]
    lp_vals = [d["lp_val"] for d in balanced_data]
    c11_vals = [d["c_11"] for d in balanced_data]
    ax.plot(alphas_plot, lp_vals, "o-", color="C2", label="LP value")
    ax.plot(alphas_plot, c11_vals, "x-", color="C3", label="$c_{1,1}$ component")
    ax.set_xlabel(r"$\alpha$ in objective $c_{1,0}+c_{0,1}+\alpha c_{1,1}$")
    ax.set_ylabel("value")
    ax.set_title("Two-zero balanced-sum LP, $N=3$")
    ax.legend()
    ax.grid(alpha=0.3)

    fig.suptitle("Arch 4E.7: multi-zero LP shape factors\n"
                 "(escape route from 4E.3's line-restriction lemma)",
                 fontsize=12, y=0.995)
    plt.tight_layout()
    plt.savefig(out_dir / "e4e7_multi_zero_lp.png", dpi=140)
    plt.close()
    print(f"\n[4E.7] Saved {out_dir / 'e4e7_multi_zero_lp.png'}")

    np.savez_compressed(
        out_dir / "e4e7_multi_zero_lp.npz",
        single_zero_data=np.array(single_zero_data, dtype=object),
        two_zero_data=np.array(two_zero_data, dtype=object),
        balanced_data=np.array(balanced_data, dtype=object),
        hb_data=np.array(hb_data, dtype=object),
        alphas=alphas,
    )
    print(f"[4E.7] Saved {out_dir / 'e4e7_multi_zero_lp.npz'}")

    # Summary
    print()
    print("=" * 78)
    print("[4E.7] Summary")
    print("=" * 78)
    print()
    print("The multi-zero LP escape from 4E.3's line-restriction lemma is real")
    print("at the LP-value level: 2D non-negativity does not reduce to 1D Fejer")
    print("under multi-zero MT bookkeeping (the constraint set is full [0,2pi]^2,")
    print("not a line). Three concrete findings:")
    print()
    print("FINDING 1. lambda_{1,1} = (q_1^2 - 1)^2 / 4 is STRICTLY GREATER")
    print("than lambda_1^2 = ((q_1 - 1)^2 / 4)^2 for every tested N. The ratio")
    print("lambda_{1,1} / lambda_1^2 ranges from 55x to 137x at N in {2, 3, 4}.")
    print("The joint MT-like shape factor is much larger than two independent")
    print("single-zero applications would give. This is the Heath-Brown-style")
    print("'zeros interact' phenomenon at the LP-shape-factor level.")
    print()
    print("FINDING 2. The LP-optimal polynomial for max c_{1,1} is RANK 1")
    print("(tensor product), equal to q_1^2. Same for the balanced sum")
    print("c_{1,0} + c_{0,1} + alpha c_{1,1}: all tested alpha give rank-1")
    print("optima. Naive multi-zero objectives DO NOT produce non-tensor LP")
    print("solutions; the rank > 1 win of 4E.2's (c_{1,1} + alpha c_{2,2})")
    print("required HIGHER harmonics (the c_{2,2} cross-cross term), not just")
    print("the first-harmonic cross c_{1,1}. So multi-zero MT with only")
    print("first-harmonic objectives does not exceed tensor-product LP value.")
    print()
    print("FINDING 3. Translation to an actual zero-free region constant for")
    print("RH on zeta requires the full multi-zero explicit-formula bookkeeping")
    print("(Heath-Brown 1992, Pintz 1976), which is NOT implemented here. The")
    print("standard result: multi-zero MT gives constant-factor improvements")
    print("for FINITE-RANGE problems (Siegel zeros, least prime in AP) where")
    print("multiple zeros at similar heights are postulated by the problem")
    print("setup. For ASYMPTOTIC RH on zeta, where any narrow height range")
    print("contains O(1) zero by Riemann-von Mangoldt, multi-zero MT does")
    print("not change the (log T)^{-1} scaling of the zero-free width -- but")
    print("CAN improve the constant. The LP gain (Finding 1) is at the")
    print("input side; translating it through the explicit-formula side")
    print("requires care beyond this experiment.")
    print()
    print("VERDICT. Multi-zero LP is a real escape from 4E.3 at the LP-shape")
    print("level (Finding 1) but the naive objective produces tensor-product")
    print("optima (Finding 2). A non-trivial multi-zero MT improvement to RH")
    print("on zeta would require combining the multi-zero LP with the")
    print("higher-harmonic structure of 4E.2 (the +25% rank-2 LP gain) AND")
    print("explicit Heath-Brown bookkeeping. This is the natural followup")
    print("(4E.7.1 open) but is research-grade work beyond this experiment.")
    print()
    print("Open: 4E.8 (polynomial-ideal SOS via Putinar/Schmuedgen) is the")
    print("remaining LP-escape route per LEARNINGS finding #12, requiring SDP")
    print("not LP. Could give a structurally different bound type.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()
    run(out_dir=args.out)
