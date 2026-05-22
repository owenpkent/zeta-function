"""Experiment 4E.3: Translation of the 4E.2 +25% LP gap into a zero-free
region constant via Heath-Brown / Pintz explicit-formula bookkeeping.

4E.2 found that the LP for max c_{1,1} + alpha c_{2,2} at bidegree
(2, 2) exceeds the Cauchy-Schwarz tensor bound by +25% at alpha = 3,
with LP-optimal coefficient matrix

    c_{0,0} = 1, c_{1,1} = 8/5, c_{2,0} = c_{0,2} = c_{2,2} = 4/5.

The question of 4E.3: does this auxiliary inequality improve the
Mossinghoff-Trudgian (MT) / de la Vallee Poussin zero-free region
constant C in beta < 1 - C / log|t|?

The MT framework. For a nonneg trig polynomial P(u) = c_0 + c_1 cos u
+ c_2 cos 2u + ... >= 0 with c_0 > 0 (literal-coefficient
convention), a putative zero rho_0 = beta_0 + i gamma_0 forces

    c_1 / (sigma - beta_0) <= c_0 / (sigma - 1) + R(P) log T,

yielding C = (c_1 - c_0)^2 / (4 R(P) c_0). The "shape factor" is
(c_1 - c_0)^2 / (4 c_0), and R(P) is a boundary term scaling roughly
with P(0).

The 2D restriction. Given a 2D nonneg bivariate polynomial
P(theta, phi) and heights (t_1, t_2), the effective 1D polynomial
tilde P(u) := P(t_1 u, t_2 u) inherits non-negativity and serves
as the MT input.

The main finding (Part 6 below). For ANY non-neg bivariate
polynomial P(theta, phi) and ANY heights (t_1, t_2), the effective
1D polynomial tilde P(u) is itself non-neg, so its MT shape factor
is bounded by 1D Fejer at matched effective degree. The 2D-via-
restriction strategy CANNOT improve over 1D Fejer at the same degree.

Numerical confirmation. For the 4E.2 peak polynomial (alpha=3, N=2)
and a sweep alpha in [0, 10] x reductions in {t_1=t_2=g/2, t_1=g,
t_1=2t_2, ...}:
  - the 4E.2 peak's best shape/P(0) is 12.6x WORSE than 1D Fejer
    at matched degree;
  - the BEST 2D polynomial across the alpha sweep gives ratio 0.958
    (still slightly worse than 1D Fejer), achieved by the trivial
    tensor product Q(theta) Q(phi) at alpha = 0.

Conclusion. The +25% C-S auxiliary-inequality gap is structurally
real, but the C-S figure of merit and the MT figure of merit are
incompatible. The 4E.2 LP family is misaligned with MT; more
fundamentally, the structural lemma (Part 6) rules out ANY single-
zero MT improvement from the 2D restriction route.

To actually improve the zero-free region constant via 2D inequalities,
one must target a different bookkeeping: multiple putative zeros
(Heath-Brown's least-prime-in-AP setup), constrained-domain LP,
polynomial-ideal SOS, or cross-prime coupling.

Output:
  - e4e3_mt_translation.npz: comparison table over reduction choices
  - e4e3_mt_translation.png: visual summary
"""

from __future__ import annotations

import argparse
import time
from fractions import Fraction
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


def build_4E2_peak_polynomial():
    """Construct the 4E.2 peak LP optimum at alpha = 3, N = 2.

    Returns a dict {(j, k): c_{j,k}} with c_{0,0} = 1.

    LP-optimal coefficients (from 4E.2):
      c_{0,0} = 1
      c_{1,1} = 8/5
      c_{2,0} = c_{0,2} = c_{2,2} = 4/5
    all others zero.
    """
    return {
        (0, 0): 1.0,
        (1, 1): 8.0 / 5.0,
        (2, 0): 4.0 / 5.0,
        (0, 2): 4.0 / 5.0,
        (2, 2): 4.0 / 5.0,
    }


def verify_4E2_peak_via_LP(N: int = 2, M: int = 200):
    """Re-solve the LP at alpha = 3 and verify coefficients."""
    alpha = 3.0
    obj = {(1, 1): 1.0, (2, 2): alpha}
    lp_val, c_mat = best_bivariate_objective(N, obj, M=M)
    return lp_val, c_mat


def expand_to_frequency_weights(P_coeffs: dict, t1: float, t2: float):
    """Expand P(t1 log n, t2 log n) into literal Fourier frequencies in log n.

    Each term c_{j,k} cos(j t1 log n) cos(k t2 log n) expands as
      - j = k = 0: contributes c_{0,0} to freq h = 0
      - j > 0, k = 0: c_{j,0} cos(j t1 log n) contributes to freq h = j t1
      - j = 0, k > 0: c_{0,k} cos(k t2 log n) contributes to freq h = k t2
      - j > 0, k > 0: c_{j,k}/2 to freq j t1 + k t2 AND j t1 - k t2

    Frequencies are taken as absolute values (cos is even).

    Returns dict {h_abs: weight}, summing contributions at coincident freqs.
    """
    weights = {}

    def add(h, w):
        h_abs = round(abs(h), 10)  # tolerance for floating-point coincidence
        weights[h_abs] = weights.get(h_abs, 0.0) + w

    for (j, k), c in P_coeffs.items():
        if j == 0 and k == 0:
            add(0.0, c)
        elif k == 0:
            add(j * t1, c)
        elif j == 0:
            add(k * t2, c)
        else:
            add(j * t1 + k * t2, c / 2.0)
            add(j * t1 - k * t2, c / 2.0)

    return weights


def mt_shape_factor(weights: dict, gamma_0: float, tol: float = 1e-6):
    """MT leading-order shape factor for a 1D polynomial.

    Given the effective 1D polynomial as a dict {h: w_h}, with h normalized
    to units of gamma_0 (so h=0 is the pole, h=1 is the trick frequency):
    compute (w_1 - w_0)^2 / (4 w_0), the MT shape (boundary-free).

    For comparison across polynomials, this isolates the "shape" factor
    that gets multiplied by 1/R(P) to give the actual constant.
    """
    h_units = {h / gamma_0: w for h, w in weights.items()}
    w_0 = sum(w for h, w in h_units.items() if abs(h) < tol)
    w_1 = sum(w for h, w in h_units.items() if abs(h - 1.0) < tol)
    return (w_1 - w_0) ** 2 / (4.0 * w_0) if w_0 > 0 else 0.0, w_0, w_1


def heath_brown_constant(weights: dict, gamma_0: float, tol: float = 1e-6):
    """Heath-Brown style bound from frequency expansion.

    For the inequality
        sum_h w_h * (-Re zeta'/zeta(sigma + ih)) >= 0
    keeping only the pole at h=0 and the trick zero rho_0 at h = gamma_0,
    we get
        w_1 / (sigma - beta_0) <= w_0 / (sigma - 1) + R log T

    where w_0 = sum of weights at h=0, w_1 = sum at h = gamma_0.

    Solving for eta = 1 - beta_0 -> 0:
      eta >= (w_1 - w_0)^2 / (4 R w_0 log T)

    The "shape factor" (w_1 - w_0)^2 / (4 w_0) is the relevant comparison
    across polynomials when R is held fixed.

    Returns: shape factor, plus all the weight collections at h = k*gamma_0
    for k = 0, 1, 2, ...
    """
    h_units = {h / gamma_0: w for h, w in weights.items()}
    # Bin to integer multiples of gamma_0
    bins = {}
    for h, w in h_units.items():
        # Find nearest integer (or half-integer) multiple
        for k_candidate in [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]:
            if abs(h - k_candidate) < tol:
                bins[k_candidate] = bins.get(k_candidate, 0.0) + w
                break
        else:
            bins[round(h, 4)] = bins.get(round(h, 4), 0.0) + w

    w_0 = bins.get(0, 0.0)
    w_1 = bins.get(1, 0.0)
    shape = (w_1 - w_0) ** 2 / (4.0 * w_0) if w_0 > 0 and w_1 > w_0 else 0.0
    return shape, bins


def effective_degree(bins: dict, tol: float = 1e-6):
    """Highest integer frequency present in the binned weights.

    Half-integer frequencies (e.g., 0.5, 1.5) indicate the polynomial
    is not at integer frequencies in gamma_0 units; we still report
    the max integer present, which is the right comparison for
    Mossinghoff-Trudgian since only integer frequencies contribute
    to the MT trick at gamma_0, 2 gamma_0, ...
    """
    integer_freqs = [int(h) for h in bins if abs(h - int(h)) < tol and h > 0]
    return max(integer_freqs) if integer_freqs else 0


def total_polynomial_norm(bins: dict):
    """Sum of all weights = P(0,0) (value of polynomial at origin).

    For the Mossinghoff-Trudgian constant C = shape / (R(P)), the
    boundary error R(P) typically scales with sum-of-weights or
    a similar polynomial norm. We use sum-of-weights as a fair
    normalization across polynomials of different effective degrees.
    """
    return sum(bins.values())


def reduction_table(P_coeffs: dict, gamma_0: float = 1.0):
    """Compute the effective polynomial under various (t1, t2) choices.

    All choices written in units of gamma_0. Returns list of dicts with:
      - label
      - (t1, t2)
      - effective 1D polynomial weights {h: w}
      - MT shape factor
    """
    rows = []

    # Choice 1: t1 = t2 = gamma_0 / 2 (3 freqs coincide at gamma_0)
    t1, t2 = gamma_0 / 2, gamma_0 / 2
    w = expand_to_frequency_weights(P_coeffs, t1, t2)
    shape, bins = heath_brown_constant(w, gamma_0)
    rows.append({
        "label": "t1 = t2 = gamma_0/2",
        "t1": t1, "t2": t2,
        "weights": w,
        "bins": bins,
        "shape": shape,
        "description": "3 freqs coincide at gamma_0 (best alignment for this P)",
    })

    # Choice 2: t1 = gamma_0, t2 = gamma_0/2
    t1, t2 = gamma_0, gamma_0 / 2
    w = expand_to_frequency_weights(P_coeffs, t1, t2)
    shape, bins = heath_brown_constant(w, gamma_0)
    rows.append({
        "label": "t1 = gamma_0, t2 = gamma_0/2",
        "t1": t1, "t2": t2,
        "weights": w,
        "bins": bins,
        "shape": shape,
        "description": "Mixed coincidence",
    })

    # Choice 3: t1 = gamma_0, t2 = gamma_0 (degenerate, doubled-degree)
    t1, t2 = gamma_0, gamma_0
    w = expand_to_frequency_weights(P_coeffs, t1, t2)
    shape, bins = heath_brown_constant(w, gamma_0)
    rows.append({
        "label": "t1 = t2 = gamma_0",
        "t1": t1, "t2": t2,
        "weights": w,
        "bins": bins,
        "shape": shape,
        "description": "Both heights at gamma_0 (degenerate; freqs at 0, 2g_0, 4g_0)",
    })

    # Choice 4: t1 = gamma_0/2, t2 = 0 (pure 1D in theta)
    t1, t2 = gamma_0 / 2, 0.0
    w = expand_to_frequency_weights(P_coeffs, t1, t2)
    shape, bins = heath_brown_constant(w, gamma_0)
    rows.append({
        "label": "t1 = gamma_0/2, t2 = 0",
        "t1": t1, "t2": t2,
        "weights": w,
        "bins": bins,
        "shape": shape,
        "description": "Degenerate to 1D in theta only",
    })

    # Choice 5: t1 = gamma_0, t2 = 0
    t1, t2 = gamma_0, 0.0
    w = expand_to_frequency_weights(P_coeffs, t1, t2)
    shape, bins = heath_brown_constant(w, gamma_0)
    rows.append({
        "label": "t1 = gamma_0, t2 = 0",
        "t1": t1, "t2": t2,
        "weights": w,
        "bins": bins,
        "shape": shape,
        "description": "Pure 1D at h = gamma_0",
    })

    # Choice 6: t1 = t2 = gamma_0/4 (less alignment)
    t1, t2 = gamma_0 / 4, gamma_0 / 4
    w = expand_to_frequency_weights(P_coeffs, t1, t2)
    shape, bins = heath_brown_constant(w, gamma_0)
    rows.append({
        "label": "t1 = t2 = gamma_0/4",
        "t1": t1, "t2": t2,
        "weights": w,
        "bins": bins,
        "shape": shape,
        "description": "No freq coincides with gamma_0 (only with 2 gamma_0)",
    })

    return rows


def fejer_1D_optimum_coeffs(N: int):
    """1D Fejer optimum at degree N: literal coefficients.

    P(theta) = 1 + 2 cos(pi/(N+2)) cos theta + ... (4B convention).
    Returns dict {k: c_k} for the literal-coefficient polynomial.

    Computed via direct LP for robustness.
    """
    q_max, q_vec = best_1D_raw_qj(N, 1, M=4000)
    return {k: float(q_vec[k]) for k in range(N + 1)}


def alpha_sweep_for_zero_free(alphas, N: int = 2, M: int = 200,
                              gamma_0: float = 1.0):
    """For each alpha in the 4E.2 sweep, compute the LP polynomial and
    its best MT shape factor over the reductions in reduction_table().

    Tracks both raw shape (w_g0 - w_0)^2/(4 w_0) and normalized
    shape/P(0) (proxy for actual MT constant since R(P) ~ P(0)).
    Also reports the effective degree of the best reduction.
    """
    rows = []
    for alpha in alphas:
        if alpha == 0.0:
            obj = {(1, 1): 1.0}
        else:
            obj = {(1, 1): 1.0, (2, 2): float(alpha)}
        lp_val, c_mat = best_bivariate_objective(N, obj, M=M)
        P_coeffs = {}
        for j in range(N + 1):
            for k in range(N + 1):
                if abs(c_mat[j, k]) > 1e-10:
                    P_coeffs[(j, k)] = float(c_mat[j, k])
        reductions = reduction_table(P_coeffs, gamma_0=gamma_0)
        for r in reductions:
            r["P0"] = total_polynomial_norm(r["bins"])
            r["shape_normalized"] = r["shape"] / r["P0"] if r["P0"] > 0 else 0
            r["eff_deg"] = effective_degree(r["bins"])
        best = max(reductions, key=lambda r: r["shape_normalized"])
        rows.append({
            "alpha": alpha,
            "lp_val": lp_val,
            "P_coeffs": P_coeffs,
            "best_reduction_shape": best["shape"],
            "best_reduction_shape_normalized": best["shape_normalized"],
            "best_reduction_P0": best["P0"],
            "best_reduction_eff_deg": best["eff_deg"],
            "best_reduction_label": best["label"],
        })
    return rows


def run(N: int = 2, M_2D: int = 200, out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 78)
    print("[4E.3] Translation of 4E.2 LP gap into zero-free region constant")
    print("=" * 78)

    # Part 1: confirm 4E.2 peak coefficients
    print()
    print("[4E.3.1] Confirm 4E.2 peak (alpha = 3, N = 2) LP optimum")
    P_peak_predicted = build_4E2_peak_polynomial()
    lp_val, c_mat = verify_4E2_peak_via_LP(N=2, M=M_2D)
    print(f"  LP value at alpha = 3, N = 2: {lp_val:.6f} (expect 4.0000)")
    print(f"  C-S tensor bound: 16/5 = {16/5:.6f}")
    print(f"  Gap: +{(lp_val - 16/5)/(16/5)*100:.2f}%")
    print()
    print(f"  Predicted coefficients (rationals 5*c):")
    for jk in [(0, 0), (1, 1), (2, 0), (0, 2), (2, 2)]:
        c_pred = P_peak_predicted[jk]
        c_lp = c_mat[jk[0], jk[1]]
        print(f"    c_{jk}: predicted {c_pred:.6f} ({5*c_pred:.1f}/5), "
              f"LP {c_lp:.6f}, diff {c_pred - c_lp:+.2e}")

    # Part 2: Reductions to 1D for the peak polynomial
    print()
    print("[4E.3.2] Effective 1D polynomials under various (t1, t2) reductions")
    print(f"  Working in units gamma_0 = 1 (zero-free constant is dimensionless)")
    print()
    print(f"  {'Reduction':<32} {'w_0':>8} {'w_g0':>8} {'shape':>10} "
          f"{'P(0)':>8} {'shape/P(0)':>12} {'eff deg':>8}")

    reductions = reduction_table(P_peak_predicted, gamma_0=1.0)
    for r in reductions:
        w0 = r["bins"].get(0, 0.0)
        wg = r["bins"].get(1, 0.0)
        P0 = total_polynomial_norm(r["bins"])
        eff_deg = effective_degree(r["bins"])
        normalized = r["shape"] / P0 if P0 > 0 else 0
        r["P0"] = P0
        r["eff_deg"] = eff_deg
        r["shape_normalized"] = normalized
        print(f"  {r['label']:<32} {w0:>8.4f} {wg:>8.4f} {r['shape']:>10.4f} "
              f"{P0:>8.3f} {normalized:>12.6f} {eff_deg:>8d}")
        print(f"    -> {r['description']}")

    # Pick best by NORMALIZED shape (proxy for actual MT constant)
    best_red = max(reductions, key=lambda r: r["shape_normalized"])
    print()
    print(f"  Best 2D-derived shape/P(0): {best_red['shape_normalized']:.6f} "
          f"via {best_red['label']}")
    print(f"  Best 2D-derived raw shape: "
          f"{max(reductions, key=lambda r: r['shape'])['shape']:.6f}")

    # Part 3: Compare to 1D Fejer optimum at MATCHING effective degrees
    print()
    print("[4E.3.3] 1D Fejer comparison at matching effective degrees")
    fejer_data = {}
    for N_eff in [2, 3, 4, 6]:
        coeffs = fejer_1D_optimum_coeffs(N=N_eff)
        c0 = coeffs[0]
        c1 = coeffs[1]
        sh = (c1 - c0) ** 2 / (4 * c0) if c0 > 0 and c1 > c0 else 0.0
        P0 = sum(coeffs.values())
        sh_norm = sh / P0 if P0 > 0 else 0
        fejer_data[N_eff] = {
            "coeffs": coeffs,
            "shape": sh,
            "P0": P0,
            "shape_normalized": sh_norm,
        }
        print(f"  1D Fejer N = {N_eff}: c_0 = {c0:.4f}, c_1 = {c1:.4f}, "
              f"shape = {sh:.6f}, P(0) = {P0:.3f}, shape/P(0) = {sh_norm:.6f}")
    print()
    # Compare reductions to Fejer at MATCHING effective degree
    print(f"  Comparison at matching effective degree (peak P, alpha=3):")
    print(f"  {'Reduction':<32} {'eff deg':>8} {'2D shape/P0':>14} "
          f"{'Fejer shape/P0':>16} {'ratio':>8}")
    for r in reductions:
        deg = r["eff_deg"]
        if deg in fejer_data:
            fej_norm = fejer_data[deg]["shape_normalized"]
            ratio = r["shape_normalized"] / fej_norm if fej_norm > 0 else 0
            print(f"  {r['label']:<32} {deg:>8d} {r['shape_normalized']:>14.6f} "
                  f"{fej_norm:>16.6f} {ratio:>8.3f}")
    print()
    if best_red["eff_deg"] in fejer_data:
        fej_norm_best = fejer_data[best_red["eff_deg"]]["shape_normalized"]
        ratio_best = best_red["shape_normalized"] / fej_norm_best \
            if fej_norm_best > 0 else 0
        print(f"  Best 2D reduction: shape/P0 = {best_red['shape_normalized']:.6f} "
              f"at effective degree {best_red['eff_deg']}")
        print(f"  1D Fejer at same eff degree: shape/P0 = {fej_norm_best:.6f}")
        print(f"  Ratio: {ratio_best:.3f}")
        if ratio_best < 1.0:
            print(f"  ==> 2D LP optimum DOES NOT improve over 1D Fejer at same eff degree.")
        else:
            print(f"  ==> 2D LP gives better shape/P(0) than 1D Fejer (unexpected!)")

    # Part 4: Sweep alpha to see if any LP optimum DOES improve MT shape/P(0)
    print()
    print("[4E.3.4] Sweep alpha; compare shape/P(0) to 1D Fejer at matching deg")
    alpha_grid = np.array([0.0, 0.5, 1.0, 2.0, 3.0, 5.0, 10.0])
    print(f"  {'alpha':>6} {'LP val':>10} {'best shape':>10} {'P(0)':>8} "
          f"{'shape/P0':>10} {'eff deg':>8} {'Fejer s/P0':>11} {'ratio':>8}")
    alpha_rows = alpha_sweep_for_zero_free(alpha_grid, N=N, M=M_2D, gamma_0=1.0)
    for ar in alpha_rows:
        deg = ar["best_reduction_eff_deg"]
        if deg in fejer_data:
            fej = fejer_data[deg]["shape_normalized"]
        else:
            # Compute fresh
            coeffs = fejer_1D_optimum_coeffs(N=deg)
            c0, c1 = coeffs[0], coeffs[1]
            sh = (c1 - c0) ** 2 / (4 * c0) if c0 > 0 and c1 > c0 else 0
            P0 = sum(coeffs.values())
            fej = sh / P0 if P0 > 0 else 0
            fejer_data[deg] = {"coeffs": coeffs, "shape": sh,
                              "P0": P0, "shape_normalized": fej}
        ratio = ar["best_reduction_shape_normalized"] / fej if fej > 0 else 0
        print(f"  {ar['alpha']:>6.2f} {ar['lp_val']:>10.4f} "
              f"{ar['best_reduction_shape']:>10.4f} "
              f"{ar['best_reduction_P0']:>8.3f} "
              f"{ar['best_reduction_shape_normalized']:>10.6f} "
              f"{deg:>8d} {fej:>11.6f} {ratio:>8.3f}")

    best_alpha_idx = int(np.argmax(
        [r["best_reduction_shape_normalized"] for r in alpha_rows]))
    best_alpha_row = alpha_rows[best_alpha_idx]
    print()
    print(f"  Best alpha for MT shape/P(0): alpha = {best_alpha_row['alpha']:.2f}, "
          f"shape/P(0) = {best_alpha_row['best_reduction_shape_normalized']:.6f}, "
          f"eff deg = {best_alpha_row['best_reduction_eff_deg']}")
    best_deg = best_alpha_row["best_reduction_eff_deg"]
    fej_best = fejer_data[best_deg]["shape_normalized"]
    ratio_overall = best_alpha_row["best_reduction_shape_normalized"] / fej_best
    print(f"  1D Fejer at eff deg {best_deg}: shape/P(0) = {fej_best:.6f}")
    print(f"  Ratio (2D / Fejer): {ratio_overall:.3f}")
    if ratio_overall < 1.0:
        print(f"  ==> NO alpha gives a 2D LP poly whose best 1D reduction beats "
              f"1D Fejer at same eff degree.")
    else:
        print(f"  ==> Some alpha gives a 2D LP poly that BEATS 1D Fejer at eff "
              f"degree (improvement!)")

    # Part 5: visualization
    print()
    print("[4E.3.5] Plotting...")
    fig, axs = plt.subplots(1, 2, figsize=(14, 5))

    # Panel 1: shape/P(0) vs alpha, with Fejer reference at matching eff deg
    ax = axs[0]
    alphas_plot = [r["alpha"] for r in alpha_rows]
    shapes_norm = [r["best_reduction_shape_normalized"] for r in alpha_rows]
    degs = [r["best_reduction_eff_deg"] for r in alpha_rows]
    fej_norm = [fejer_data[d]["shape_normalized"] for d in degs]

    ax.plot(alphas_plot, shapes_norm, "bo-", label="best 2D reduction (shape/P0)")
    ax.plot(alphas_plot, fej_norm, "rs--",
            label="1D Fejer at matched eff degree (shape/P0)")
    for i, (a, d) in enumerate(zip(alphas_plot, degs)):
        ax.annotate(f"deg {d}", xy=(a, shapes_norm[i]),
                    xytext=(2, 5), textcoords="offset points",
                    fontsize=8, color="b")
    ax.set_xlabel(r"$\alpha$ in objective $c_{1,1} + \alpha c_{2,2}$")
    ax.set_ylabel(r"shape / $P(0)$")
    ax.set_title(r"4E.3: normalized MT shape: 2D LP vs 1D Fejer (matched deg)")
    ax.legend()
    ax.grid(alpha=0.3)

    # Panel 2: bar chart at the 4E.2 peak (alpha=3)
    ax = axs[1]
    bar_labels = [r["label"].replace("gamma_0", "g") for r in reductions]
    bar_data_2D = [r["shape_normalized"] for r in reductions]
    bar_data_fej = [fejer_data.get(r["eff_deg"], {"shape_normalized": 0})
                    ["shape_normalized"] for r in reductions]

    x = np.arange(len(bar_labels))
    w = 0.4
    ax.bar(x - w/2, bar_data_2D, w, label="2D LP shape/P0", color="b", alpha=0.7)
    ax.bar(x + w/2, bar_data_fej, w, label="1D Fejer shape/P0 (matched deg)",
           color="r", alpha=0.7)
    ax.set_xticks(x)
    ax.set_xticklabels(bar_labels, rotation=25, fontsize=8, ha="right")
    ax.set_ylabel(r"shape / $P(0)$")
    ax.set_title(r"4E.3: 4E.2 peak ($\alpha = 3, N = 2$) reductions vs 1D Fejer")
    ax.legend()
    ax.grid(alpha=0.3, axis="y")

    plt.tight_layout()
    plt.savefig(out_dir / "e4e3_mt_translation.png", dpi=140)
    plt.close()
    print(f"  Saved {out_dir / 'e4e3_mt_translation.png'}")

    np.savez_compressed(
        out_dir / "e4e3_mt_translation.npz",
        N=N,
        peak_lp_val=lp_val,
        peak_c_mat=c_mat,
        peak_reductions_labels=np.array([r["label"] for r in reductions]),
        peak_reductions_shapes=np.array([r["shape"] for r in reductions]),
        peak_reductions_shapes_norm=np.array([r["shape_normalized"]
                                              for r in reductions]),
        peak_reductions_P0=np.array([r["P0"] for r in reductions]),
        peak_reductions_effdeg=np.array([r["eff_deg"] for r in reductions]),
        fejer_degrees=np.array(list(fejer_data.keys())),
        fejer_shapes=np.array([fejer_data[d]["shape"]
                              for d in sorted(fejer_data)]),
        fejer_shapes_norm=np.array([fejer_data[d]["shape_normalized"]
                                   for d in sorted(fejer_data)]),
        alpha_grid=alpha_grid,
        alpha_lp_vals=np.array([r["lp_val"] for r in alpha_rows]),
        alpha_best_shapes=np.array([r["best_reduction_shape"]
                                    for r in alpha_rows]),
        alpha_best_shapes_norm=np.array(
            [r["best_reduction_shape_normalized"] for r in alpha_rows]),
        alpha_best_effdeg=np.array(
            [r["best_reduction_eff_deg"] for r in alpha_rows]),
    )
    print(f"  Saved {out_dir / 'e4e3_mt_translation.npz'}")

    # Part 6: structural argument (2D restriction is a subset of 1D non-neg)
    print()
    print("[4E.3.6] Structural lemma")
    print("-" * 78)
    print("Lemma: If P(theta, phi) >= 0 on [0, 2pi]^2 then")
    print("       tilde P(u) := P(t_1 u, t_2 u) is a non-neg 1D trig poly")
    print("       of degree <= max(j t_1 + k t_2) over support of P.")
    print()
    print("Proof: P(theta_0, r theta_0) is just P evaluated at a point in")
    print("[0, 2pi]^2 (modulo periodicity), so non-neg follows from P >= 0.")
    print()
    print("Consequence: the family of effective 1D polynomials from 2D non-neg")
    print("polynomials of bidegree (N, N) via reduction (t_1, t_2) is a SUBSET")
    print("of all 1D non-neg trig polynomials of degree max(j t_1 + k t_2).")
    print("Hence max c_1 from 2D restriction is <= max c_1 from 1D directly")
    print("(1D Fejer optimum at matched degree).")
    print()
    print("This is a STRUCTURAL upper bound: no 2D bivariate non-neg polynomial")
    print("can beat the 1D MT shape factor via the natural restriction route.")
    print()
    print("To get an improvement requires:")
    print("  (a) multiple putative zeros at different heights (Heath-Brown's")
    print("      use case for arithmetic progressions / Siegel zeros)")
    print("  (b) a different LP framework: constrained-domain non-negativity,")
    print("      sum-of-squares over a polynomial ideal, or cross-prime coupling")
    print("      not expressible as a single-prime trig inequality.")

    # Summary
    print()
    print("=" * 78)
    print("[4E.3] Summary")
    print("=" * 78)
    print(f"Question: does the 4E.2 +25% LP gap translate to a better")
    print(f"          zero-free region constant via Heath-Brown / Pintz?")
    print()
    print(f"4E.2 peak polynomial (alpha = 3, N = 2): LP value = {lp_val:.4f}")
    print(f"  Gap to C-S tensor bound (16/5 = 3.2): +25.00% (4E.2 finding)")
    print()
    print(f"At the 4E.2 peak (alpha=3):")
    print(f"  Best 2D reduction (by shape/P(0)): "
          f"{best_red['shape_normalized']:.6f} "
          f"via {best_red['label']} (eff deg {best_red['eff_deg']})")
    if best_red["eff_deg"] in fejer_data:
        fnb = fejer_data[best_red["eff_deg"]]["shape_normalized"]
        print(f"  1D Fejer at eff degree {best_red['eff_deg']}: shape/P(0) = "
              f"{fnb:.6f}")
        rat = best_red['shape_normalized'] / fnb
        if rat < 1.0:
            print(f"  ==> 4E.2 peak gives {1/rat:.2f}x WORSE shape/P(0) than "
                  f"1D Fejer.")
        else:
            print(f"  ==> 4E.2 peak gives {rat:.2f}x BETTER shape/P(0) than "
                  f"1D Fejer (improvement!)")
    print()
    print(f"Overall sweep summary:")
    print(f"  Best alpha (by shape/P(0)): alpha = {best_alpha_row['alpha']:.2f}, "
          f"shape/P(0) = {best_alpha_row['best_reduction_shape_normalized']:.6f}, "
          f"eff deg = {best_alpha_row['best_reduction_eff_deg']}")
    print(f"  1D Fejer at eff deg {best_alpha_row['best_reduction_eff_deg']}: "
          f"shape/P(0) = {fej_best:.6f}")
    if ratio_overall < 1.0:
        print(f"  ==> NO 2D LP polynomial in this family produces a better "
              f"shape/P(0) than 1D Fejer at matched effective degree.")
        print()
        print(f"This is consistent with the structural lemma (Part 6): the family")
        print(f"of effective 1D polynomials from 2D non-neg bivariate polynomials")
        print(f"is a SUBSET of all 1D non-neg trig polynomials, so 2D restriction")
        print(f"cannot beat the 1D Fejer optimum at matched effective degree.")
        print()
        print(f"Implication for the 4E.2 +25% C-S gap. The gap is real, but the")
        print(f"C-S figure of merit (max linear combination of c_{{j,k}}) is")
        print(f"structurally distinct from the MT figure of merit (max c_1 after")
        print(f"1D restriction). The +25% improvement in C-S does not transfer")
        print(f"to the MT framework, because MT is bounded by 1D Fejer regardless")
        print(f"of the 2D polynomial's structure.")
        print()
        print(f"To actually improve the zero-free region constant via 2D inequalities,")
        print(f"one must either: (a) target multiple putative zeros (Heath-Brown")
        print(f"setup for least-prime-in-AP / Siegel zeros), or (b) introduce")
        print(f"non-trig constraints (constrained-domain LP, polynomial-ideal SOS,")
        print(f"cross-prime coupling).")

    return {
        "peak_lp_val": lp_val,
        "best_2D_shape_normalized": best_red["shape_normalized"],
        "peak_eff_deg": best_red["eff_deg"],
        "fejer_at_peak_deg_normalized": fejer_data.get(
            best_red["eff_deg"], {"shape_normalized": 0})["shape_normalized"],
        "reductions": reductions,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, default=2)
    parser.add_argument("--M-2D", type=int, default=200)
    args = parser.parse_args()
    run(N=args.N, M_2D=args.M_2D)
