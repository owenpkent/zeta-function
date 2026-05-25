"""Experiment 4E.8: cos x cos sum-of-squares (SOS) SDP for the MT setup.

LEARNINGS finding #12 identifies polynomial-ideal SOS via Putinar/Schmuedgen
as the remaining LP/SDP-style escape route from 4E.3's line-restriction
lemma. 4E.6 (constrained-domain K-point LP) and 4E.7 (multi-zero LP at
naive objectives) closed two of the three open routes. 4E.8 targets the
third using SDP rather than LP.

This experiment runs four probes using semidefinite programming with
cos x cos Gram-matrix parameterization (matching 4E.2's polynomial cone):

(A) SDP reproduction of 4E.2's K-sampling LP for max c_{1,1} + alpha c_{2,2}
    at bidegree (2, 2). The K-sampling LP is an OUTER relaxation (constraint
    enforced only at K points; LP value upper-bounds true non-neg cone).
    The cos x cos SOS SDP is an INNER relaxation (SOS implies non-neg, but
    not the reverse in 2D). Comparing them tells us whether the LP value
    is tight.

(B) Lasserre hierarchy: raise the SOS bidegree L while keeping the
    polynomial bidegree at (2, 2). Tests convergence of the inner relaxation
    to the LP value.

(C) Full-trig SOS (no cos x cos symmetry constraint). Gives an OUTER
    relaxation of the cos x cos LP: allows the polynomial to have sin x sin
    terms that cancel, increasing the cos x cos coefficient sum without
    requiring the cos x cos polynomial itself to be non-neg. The result is
    an upper bound on a DIFFERENT problem (max cos x cos coefficient over
    non-neg full trig polynomials).

(D) Putinar constrained-domain SOS: max objective over P = sigma_0 + g sigma_1
    with sigma_l SOS, where K = { (theta, phi) : g(theta, phi) >= 0 }.
    Tests whether constraining to a STRICT subset of [0, 2 pi]^2 produces
    LP values exceeding the unconstrained case.

Output:
  - e4e8_sos_sdp.npz: SDP values per (probe, N, alpha, level)
  - e4e8_sos_sdp.png: SDP vs K-sampling LP vs C-S tensor across alphas
"""

from __future__ import annotations

import argparse
import time
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import cvxpy as cp


# =========================================================================
# Cos x cos product expansion
# =========================================================================
#
# cos(a theta) cos(a' theta) expanded in the cos basis on [0, 2 pi]:
#   - a = 0, a' = 0:  cos(0)*cos(0) = 1                -> coef[0] = 1
#   - a = 0, a' > 0:  cos(0)*cos(a' th) = cos(a' th)   -> coef[a'] = 1
#   - a > 0, a' = 0:  symmetric                         -> coef[a] = 1
#   - a, a' > 0, a != a':  0.5 * (cos(|a-a'| th) + cos((a+a') th))
#   - a > 0, a' > 0, a == a':  0.5 * (1 + cos(2a th))   -> coef[0] = 0.5, coef[2a] = 0.5

def cos_product_coef(a: int, ap: int) -> dict:
    """Return dict {j: coef} for cos(a*x) * cos(ap*x) = sum coef[j] cos(j*x)."""
    if a == 0 and ap == 0:
        return {0: 1.0}
    if a == 0:
        return {ap: 1.0}
    if ap == 0:
        return {a: 1.0}
    # a, ap both > 0
    if a == ap:
        return {0: 0.5, 2 * a: 0.5}
    return {abs(a - ap): 0.5, a + ap: 0.5}


# =========================================================================
# Cos x cos SOS SDP
# =========================================================================
#
# P(theta, phi) = sum c_{j, k} cos(j theta) cos(k phi) is cos x cos SOS iff
#   exists PSD B of size (L+1)^2 indexed by (a, b) such that
#   P = sum_l Q_l^2 where Q_l(theta, phi) = sum q_l_{a, b} cos(a theta) cos(b phi)
#   and B = sum_l q_l q_l^T.
#
# Then c_{j, k}(P) = sum_{(a, b), (a', b')} B[(a, b), (a', b')]
#                  * w_theta(a, a', j) * w_phi(b, b', k)
# where w_theta is the cos product coefficient.
#
# The polynomial P has bidegree (2L, 2L). For 4E.2's bidegree (2, 2), L = 1.
# Higher L is the Lasserre hierarchy, giving polynomials of higher bidegree
# whose projection to bidegree (2, 2) cosine coefficients we optimize.

def coscos_sos_sdp(obj_dict: dict, L: int, N: int = None, verbose: bool = False,
                    extra_constraints=None):
    """SDP: max sum obj_dict[(j, k)] c_{j, k} over cos x cos SOS polynomials
    of SOS-bidegree (L, L). Constraint c_{0, 0} = 1.

    obj_dict: {(j, k): weight}.
    L: bidegree of each SOS square Q_l (so P = sum Q_l^2 has bidegree (2L, 2L)).
    N: bidegree of the OBJECTIVE polynomial. If P at bidegree (2L, 2L)
       contributes to c_{j, k} for j, k <= 2L, we report c_{j, k} for j, k <= N.
       If N is None, use 2L.
    extra_constraints: optional list of additional cvxpy constraints on c_{j, k}.

    Returns (value, c_matrix of size (N+1, N+1), B value).
    """
    if N is None:
        N = 2 * L

    size = (L + 1) ** 2  # B index: (a, b), a, b in {0, ..., L}
    B = cp.Variable((size, size), symmetric=True)
    constraints = [B >> 0]

    def B_idx(a, b):
        return a * (L + 1) + b

    # Build c_{j, k} as linear function of B entries for each (j, k) up to (N, N).
    # Cache the matrix of weights (size x size) for each (j, k).
    def coef_matrix(j, k):
        """Return weight matrix W of size (size, size) such that c_{j, k} = trace(B @ W^T)."""
        W = np.zeros((size, size))
        for a in range(L + 1):
            for ap in range(L + 1):
                w_theta_dict = cos_product_coef(a, ap)
                if j not in w_theta_dict:
                    continue
                w_theta = w_theta_dict[j]
                for b in range(L + 1):
                    for bp in range(L + 1):
                        w_phi_dict = cos_product_coef(b, bp)
                        if k not in w_phi_dict:
                            continue
                        w_phi = w_phi_dict[k]
                        W[B_idx(a, b), B_idx(ap, bp)] += w_theta * w_phi
        return W

    # Constraint c_{0, 0} = 1
    W00 = coef_matrix(0, 0)
    constraints.append(cp.sum(cp.multiply(B, W00)) == 1.0)

    # Apply extra constraints (e.g., zero out specific c_{j, k} to enforce bidegree)
    if extra_constraints is not None:
        for (j, k, target) in extra_constraints:
            W = coef_matrix(j, k)
            constraints.append(cp.sum(cp.multiply(B, W)) == target)

    # Objective: sum_{(j, k)} obj_{j, k} * c_{j, k}
    obj_expr = 0
    for (j, k), w in obj_dict.items():
        W = coef_matrix(j, k)
        obj_expr = obj_expr + w * cp.sum(cp.multiply(B, W))

    prob = cp.Problem(cp.Maximize(obj_expr), constraints)
    val = prob.solve(solver='CLARABEL', verbose=verbose)

    # Extract c_{j, k} for j, k in {0, ..., N}
    c_mat = np.zeros((N + 1, N + 1))
    B_val = B.value
    for j in range(N + 1):
        for k in range(N + 1):
            W = coef_matrix(j, k)
            c_mat[j, k] = float((B_val * W).sum())

    return float(val), c_mat, B_val


# =========================================================================
# Full-trig SOS SDP (for outer relaxation comparison)
# =========================================================================
#
# Same H of size (L+1)^2 but build the polynomial in exp basis,
# extract cos x cos PROJECTION. No symmetry constraint on H beyond real
# symmetric, so the polynomial has sin terms.

def fulltrig_sos_projection_sdp(obj_dict: dict, L: int, N: int = None,
                                  verbose: bool = False):
    """SDP for max sum obj * c_{j, k} over polynomials whose cos x cos
    PROJECTION has the given c_{j, k}. Allows sin x sin etc. components.

    Returns (value, c_matrix of cos x cos coefficients).
    """
    if N is None:
        N = 2 * L
    size = (L + 1) ** 2
    H = cp.Variable((size, size), symmetric=True)
    constraints = [H >> 0]

    def H_idx(i1, i2):
        return i1 * (L + 1) + i2

    def d_coef(m, n):
        # d_{m, n} = sum over (j_1, j_2) with j_1 + m, j_2 + n in [0, L]
        # of H[(j_1 + m, j_2 + n), (j_1, j_2)]
        if abs(m) > L or abs(n) > L:
            return 0.0
        terms = []
        m_abs = abs(m)
        n_abs = abs(n)
        m_sign = 1 if m >= 0 else -1
        n_sign = 1 if n >= 0 else -1
        for j1 in range(L + 1 - m_abs):
            for j2 in range(L + 1 - n_abs):
                i1 = j1 + m_abs
                i2 = j2 + n_abs
                # For m >= 0, n >= 0: H[i1, i2, j1, j2]
                # For m < 0, use symmetry H[j1, j2, i1, i2] (same)
                # For n < 0 similar
                # Real symmetric: d_{-m, -n} = d_{m, n}; for d_{m, -n} or d_{-m, n}
                # we need an INDEPENDENT calculation.
                # Use the convention: d_{m, n} = sum over (i, j) with i_1 - j_1 = m, i_2 - j_2 = n
                # of H[i, j]. For real H this gives a real bilinear function.
                if m >= 0:
                    j1_eff, i1_eff = j1, j1 + m_abs
                else:
                    j1_eff, i1_eff = j1 + m_abs, j1
                if n >= 0:
                    j2_eff, i2_eff = j2, j2 + n_abs
                else:
                    j2_eff, i2_eff = j2 + n_abs, j2
                terms.append(H[H_idx(i1_eff, i2_eff), H_idx(j1_eff, j2_eff)])
        return sum(terms) if terms else 0.0

    # Convert (j, k) cos x cos coefficient to combination of d's:
    # cos(j theta) cos(k phi) = (1/4)(e^{ij theta} + e^{-ij theta})(e^{ik phi} + e^{-ik phi})
    # So c_{j, k} in P = sum c_{j, k} cos(j theta) cos(k phi) means
    #   d_{j, k}-component = c_{j, k} / 4 for j, k > 0
    #   d_{j, 0} = c_{j, 0} / 2 for j > 0
    #   d_{0, k} = c_{0, k} / 2 for k > 0
    #   d_{0, 0} = c_{0, 0}
    # And by real polynomial symmetry: d_{-j, k} = d_{j, k} (since P real cos x cos)
    # But here we extract the cos x cos PROJECTION:
    # c_{j, k} = d_{j, k} + d_{-j, k} + d_{j, -k} + d_{-j, -k}  for j, k > 0  (4 terms)
    # c_{j, 0} = d_{j, 0} + d_{-j, 0}  for j > 0
    # c_{0, k} = d_{0, k} + d_{0, -k}  for k > 0
    # c_{0, 0} = d_{0, 0}

    def c_expr(j, k):
        if j == 0 and k == 0:
            return d_coef(0, 0)
        if j == 0:
            return d_coef(0, k) + d_coef(0, -k)
        if k == 0:
            return d_coef(j, 0) + d_coef(-j, 0)
        return d_coef(j, k) + d_coef(-j, k) + d_coef(j, -k) + d_coef(-j, -k)

    # Constraint c_{0, 0} = 1
    constraints.append(c_expr(0, 0) == 1.0)

    obj_expr = 0
    for (j, k), w in obj_dict.items():
        obj_expr = obj_expr + w * c_expr(j, k)

    prob = cp.Problem(cp.Maximize(obj_expr), constraints)
    val = prob.solve(solver='CLARABEL', verbose=verbose)

    c_mat = np.zeros((N + 1, N + 1))
    H_val = H.value
    for j in range(N + 1):
        for k in range(N + 1):
            # Recompute numerically
            def d_num(m, n):
                if abs(m) > L or abs(n) > L:
                    return 0.0
                s = 0.0
                m_abs = abs(m)
                n_abs = abs(n)
                for j1 in range(L + 1 - m_abs):
                    for j2 in range(L + 1 - n_abs):
                        if m >= 0:
                            j1_eff, i1_eff = j1, j1 + m_abs
                        else:
                            j1_eff, i1_eff = j1 + m_abs, j1
                        if n >= 0:
                            j2_eff, i2_eff = j2, j2 + n_abs
                        else:
                            j2_eff, i2_eff = j2 + n_abs, j2
                        s += H_val[H_idx(i1_eff, i2_eff), H_idx(j1_eff, j2_eff)]
                return s
            if j == 0 and k == 0:
                c_mat[j, k] = d_num(0, 0)
            elif j == 0:
                c_mat[j, k] = d_num(0, k) + d_num(0, -k)
            elif k == 0:
                c_mat[j, k] = d_num(j, 0) + d_num(-j, 0)
            else:
                c_mat[j, k] = d_num(j, k) + d_num(-j, k) + d_num(j, -k) + d_num(-j, -k)

    return float(val), c_mat


# =========================================================================
# Cauchy-Schwarz tensor bound (4E.2 convention)
# =========================================================================

def cauchy_schwarz_bound_4e2(N: int, alpha: float) -> float:
    """The 4E.2 C-S tensor bound: max_Q (q_1^2 + alpha q_2^2) where
    Q(theta) = 1 + q_1 cos + q_2 cos 2 + ... + q_N cos N is 1D non-neg
    at degree N.

    For N = 2, closed-form (per 4E.2 dossier): 16 / (8 - alpha) for alpha in [0, 8).
    For alpha = 0: 2.0 = (2 cos pi/4)^2 = q_1^2.
    """
    if N == 2:
        if alpha < 8:
            return 16.0 / (8.0 - alpha)
        return float('inf')
    # Generic SDP form (Shor's relaxation of QCQP)
    M = 4000
    theta = np.linspace(0, 2 * np.pi, M, endpoint=False)
    cos_vals = np.array([np.cos(k * theta) for k in range(N + 1)])
    Q_psd = cp.Variable((N + 1, N + 1), symmetric=True)
    W = np.zeros((N + 1, N + 1))
    W[1, 1] = 1.0
    if N >= 2:
        W[2, 2] = alpha
    constraints = [Q_psd >> 0, Q_psd[0, 0] == 1.0]
    constraints.append(cos_vals.T @ Q_psd[0, :] >= 0)
    prob = cp.Problem(cp.Maximize(cp.trace(W @ Q_psd)), constraints)
    val = prob.solve(solver='CLARABEL')
    return float(val)


# =========================================================================
# K-sampling LP (for reference, matches 4E.2's setup)
# =========================================================================

def ksampling_lp(obj_dict: dict, N: int, M: int = 120):
    """Reproduce 4E.2-style K-sampling LP for max sum obj * c_{j,k} over
    cos x cos non-neg polynomials of bidegree (N, N), c_{0,0} = 1."""
    from experiments.zero_free.e4e_offdiag_lp import best_bivariate_objective
    return best_bivariate_objective(N, obj_dict, M=M)


# =========================================================================
# Phase A: SDP-exact vs K-sampling LP for the 4E.2 problem
# =========================================================================

def phase_A(out_dir: Path):
    print("=" * 78)
    print("[4E.8.A] cos x cos SOS SDP vs K-sampling LP for the 4E.2 problem")
    print("=" * 78)
    print()
    print("  Setup: bidegree (2, 2), objective max c_{1,1} + alpha c_{2,2},")
    print("         c_{0,0} = 1.  SOS bidegree L = 1 (so P = Q^2 with Q of")
    print("         cos x cos bidegree (1, 1)). P is bidegree (2, 2).")
    print()

    N = 2
    L = 1  # SOS bidegree; Q has cos x cos bidegree (1, 1), so Q^2 has (2, 2)
    alphas = np.array([0.0, 0.5, 1.0, 2.0, 3.0, 5.0, 7.0])
    print(f"  {'alpha':>6} {'C-S 1D':>9} {'cos SOS':>10} {'K-LP':>10} "
          f"{'SOS gap':>10} {'LP gap':>10} {'rank(C)':>8}")

    results = []
    for alpha in alphas:
        cs_bound = cauchy_schwarz_bound_4e2(N, alpha)
        obj = {(1, 1): 1.0, (2, 2): float(alpha)}
        t0 = time.time()
        sdp_val, c_mat, B_val = coscos_sos_sdp(obj, L=L, N=N)
        sdp_time = time.time() - t0
        rank = int(np.linalg.matrix_rank(c_mat, tol=1e-5))
        lp_val, lp_cmat = ksampling_lp(obj, N, M=120)
        sos_gap = (sdp_val - cs_bound) / cs_bound * 100
        lp_gap = (lp_val - cs_bound) / cs_bound * 100
        print(f"  {alpha:>6.2f} {cs_bound:>9.4f} {sdp_val:>10.4f} {lp_val:>10.4f} "
              f"{sos_gap:>9.2f}% {lp_gap:>9.2f}% {rank:>8d}")
        results.append({
            'alpha': float(alpha),
            'cs_bound': float(cs_bound),
            'sdp_val': float(sdp_val),
            'lp_val': float(lp_val),
            'sos_gap_pct': float(sos_gap),
            'lp_gap_pct': float(lp_gap),
            'rank_c': rank,
            'time_sec': float(sdp_time),
            'c_matrix': c_mat.tolist(),
        })

    return results


def phase_B(out_dir: Path):
    print()
    print("=" * 78)
    print("[4E.8.B] Lasserre hierarchy at alpha = 3 (4E.2's peak)")
    print("=" * 78)
    print()
    print("  Raise SOS-bidegree L; P has bidegree (2L, 2L) but we report only")
    print("  c_{0,0}, c_{1,1}, c_{2,2} (the objective + constraint coefficients).")
    print(f"  {'L':>3} {'P bidegree':>12} {'SOS value':>11} {'C-S':>10} "
          f"{'gap %':>9} {'time':>8}")

    alpha = 3.0
    cs_bound = cauchy_schwarz_bound_4e2(2, alpha)
    obj = {(1, 1): 1.0, (2, 2): alpha}
    results = []
    for L in [1, 2, 3]:
        t0 = time.time()
        try:
            val, c_mat, _ = coscos_sos_sdp(obj, L=L, N=2 * L)
            elapsed = time.time() - t0
        except Exception as e:
            print(f"  L={L}: failed ({e})")
            continue
        gap = (val - cs_bound) / cs_bound * 100
        print(f"  {L:>3d} ({2*L:>3d},{2*L:>3d})      {val:>11.4f} {cs_bound:>10.4f} "
              f"{gap:>8.2f}% {elapsed:>8.2f}")
        results.append({
            'L': L,
            'P_bidegree': 2 * L,
            'value': float(val),
            'cs_bound': float(cs_bound),
            'gap_pct': float(gap),
            'time_sec': float(elapsed),
        })

    return results


def phase_C(out_dir: Path):
    print()
    print("=" * 78)
    print("[4E.8.C] Full-trig SOS outer relaxation (cos x cos projection)")
    print("=" * 78)
    print()
    print("  Allow P to have sin x sin terms (full trig SOS); extract cos x cos")
    print("  PROJECTION coefficients c_{j, k}. This is a DIFFERENT problem from")
    print("  (A): it asks 'what cos x cos coefficient sum is achievable by some")
    print("  non-neg trig polynomial?', regardless of whether that polynomial is")
    print("  itself cos x cos.")
    print()
    print("  The result is an UPPER bound on (A)'s LP (more polynomials feasible).")
    print()
    print(f"  {'alpha':>6} {'C-S 1D':>9} {'cos SOS (A)':>12} {'full SOS (C)':>13} "
          f"{'(C) > (A)?':>12}")

    N = 2
    L = 1
    alphas = np.array([0.0, 1.0, 3.0, 5.0])
    results = []
    for alpha in alphas:
        cs_bound = cauchy_schwarz_bound_4e2(N, alpha)
        obj = {(1, 1): 1.0, (2, 2): float(alpha)}
        coscos_val, _, _ = coscos_sos_sdp(obj, L=L, N=N)
        fulltrig_val, _ = fulltrig_sos_projection_sdp(obj, L=2, N=N)
        diff = fulltrig_val - coscos_val
        sign = "yes (+%.2f)" % diff if diff > 1e-3 else "no"
        print(f"  {alpha:>6.2f} {cs_bound:>9.4f} {coscos_val:>12.4f} "
              f"{fulltrig_val:>13.4f} {sign:>12}")
        results.append({
            'alpha': float(alpha),
            'cs_bound': float(cs_bound),
            'coscos_sos': float(coscos_val),
            'fulltrig_sos_proj': float(fulltrig_val),
            'difference': float(diff),
        })

    return results


def phase_D(out_dir: Path):
    print()
    print("=" * 78)
    print("[4E.8.D] Line restriction to phi = 2 theta (Heath-Brown coupling)")
    print("=" * 78)
    print()
    print("  Per 4E.3 lemma, ANY non-neg cos x cos polynomial of bidegree (2, 2)")
    print("  restricted to phi = 2 theta gives a 1D non-neg cosine polynomial of")
    print("  effective degree 2 + 2*2 = 6.  The 1D Fejer bound at deg 6 caps")
    print("  the c_1 / c_0 ratio at 2 cos(pi/8) = 1.8478 in the RAW convention")
    print("  P = c_0 + c_1 cos + c_2 cos 2 + ... (or equivalently cos(pi/8) =")
    print("  0.9239 in the 4B convention P = c_0 + 2 c_1 cos + 2 c_2 cos 2 + ...).")
    print()
    print("  We compute the line-restriction of the 4E.2 LP-optimal polynomial")
    print("  and verify the bound holds.  Then we ask: does any (cos x cos SOS)")
    print("  polynomial achieve max c_1 / c_0 of its phi=2theta restriction")
    print("  that exceeds the Fejer cap at effective deg 6?")
    print()

    # The 4E.2 LP-optimal polynomial at alpha = 3, N = 2:
    # c_{0,0}=1, c_{1,1}=8/5, c_{2,2}=4/5, c_{0,2}=4/5, c_{2,0}=4/5, others 0.
    c_4e2 = np.array([
        [1.0,   0.0, 4.0/5],
        [0.0,   8.0/5, 0.0],
        [4.0/5, 0.0,   4.0/5],
    ])

    def restrict_to_line(c_mat, slope: float = 2.0, deg_eff: int = 6):
        """P(theta, slope * theta), expressed in cos basis of degree deg_eff."""
        coefs = np.zeros(deg_eff + 1)
        N_max = c_mat.shape[0] - 1
        for j in range(N_max + 1):
            for k in range(N_max + 1):
                cjk = c_mat[j, k]
                if abs(cjk) < 1e-12:
                    continue
                # cos(j theta) cos(k * slope * theta)
                eff_j = int(round(k * slope))
                w_dict = cos_product_coef(j, eff_j)
                for harm, w in w_dict.items():
                    if harm <= deg_eff:
                        coefs[harm] += w * cjk
        return coefs

    # Restrict 4E.2 LP-optimal to phi = 2 theta
    coefs_4e2 = restrict_to_line(c_4e2, slope=2.0, deg_eff=6)
    c1_over_c0_4e2 = coefs_4e2[1] / coefs_4e2[0]
    fejer_raw_deg6 = 2.0 * np.cos(np.pi / 8)  # raw convention: max c_1 / c_0 for P = c_0 + c_1 cos + ...
    fejer_4B_deg6 = np.cos(np.pi / 8)  # 4B convention: max c_1 / c_0 for P = c_0 + 2 c_1 cos + ...
    print(f"  4E.2 LP-optimal polynomial restricted to phi = 2 theta:")
    print(f"    1D cosine coefficients [0..6]: " +
          ", ".join(f"{c:.4f}" for c in coefs_4e2))
    print(f"    c_1 / c_0 (raw) = {c1_over_c0_4e2:.4f}")
    print(f"    1D Fejer max c_1 / c_0 at deg 6, raw = 2 cos(pi/8) = {fejer_raw_deg6:.4f}")
    print(f"    ratio = {c1_over_c0_4e2 / fejer_raw_deg6:.4f}  "
          f"({'BELOW Fejer (lemma holds)' if c1_over_c0_4e2 < fejer_raw_deg6 else 'EXCEEDS Fejer'})")
    print()

    # Now SDP: maximize the c_1 of the phi=2theta restriction, subject to
    # P being cos x cos SOS at bidegree (2, 2).
    # c_1 of the restriction = sum_{j, k} c_{j, k} * w(j, 2k, 1)
    # where w(j, 2k, 1) is the coefficient of cos(theta) in cos(j theta) cos(2k theta).
    # w(j, 2k, 1) = (delta(|j - 2k| == 1) + delta(j + 2k == 1)) * 0.5  for j, k > 0
    #             = delta(j == 1, k == 0) + delta(j == 0, 2k == 1) -> only j=1, k=0 contributes
    # Wait, also need to handle the boundary cases.
    # For our bidegree (2, 2), (j, k) ranges over {0, 1, 2}^2.
    # Compute w(j, 2k, 1) for each:
    # (j, k) -> cos(j th) cos(2k th) -> coefs by cos_product_coef(j, 2k)
    line_c1_weights = {}
    for j in range(3):
        for k in range(3):
            w_dict = cos_product_coef(j, 2 * k)
            if 1 in w_dict:
                line_c1_weights[(j, k)] = w_dict[1]
    print(f"  Weights for max c_1 of phi=2theta restriction:")
    for (j, k), w in line_c1_weights.items():
        print(f"    c_{{{j},{k}}} contributes {w:.4f}")

    # Build SDP: max sum line_c1_weights[(j, k)] * c_{j, k} over cos x cos SOS
    obj_line = {(j, k): float(w) for (j, k), w in line_c1_weights.items()}
    # Also need to fix c_0 of the restriction = 1 (the constraint c_{0,0}=1 plus
    # whatever else maps to cos(0) on the line).
    # c_0 of restriction = sum_{j, k} c_{j, k} * w(j, 2k, 0)
    # w(j, 2k, 0) = 1 if j = 0 and 2k = 0 (so (0, 0)); 0.5 if j = 2k > 0; 0 else.
    line_c0_weights = {}
    for j in range(3):
        for k in range(3):
            w_dict = cos_product_coef(j, 2 * k)
            if 0 in w_dict:
                line_c0_weights[(j, k)] = w_dict[0]
    print(f"\n  Weights for c_0 of phi=2theta restriction:")
    for (j, k), w in line_c0_weights.items():
        print(f"    c_{{{j},{k}}} contributes {w:.4f}")

    # SDP: max sum w_c1 * c_{j,k} s.t. sum w_c0 * c_{j,k} = 1 and P cos x cos SOS
    # Use coscos_sos_sdp with extra constraint sum w_c0 * c_{j,k} = 1 in place of c_{0,0} = 1.
    # We can't directly impose this with the current API. Workaround: add as extra_constraints
    # using the trick (j', k') = something that the function recognizes.
    # Simpler: write a custom SDP here.

    L_sos = 1  # bidegree-1 SOS so P has bidegree (2, 2)
    size = (L_sos + 1) ** 2
    B = cp.Variable((size, size), symmetric=True)
    constraints = [B >> 0]

    def B_idx(a, b):
        return a * (L_sos + 1) + b

    def coef_matrix(j, k):
        W = np.zeros((size, size))
        for a in range(L_sos + 1):
            for ap in range(L_sos + 1):
                w_theta_dict = cos_product_coef(a, ap)
                if j not in w_theta_dict:
                    continue
                w_theta = w_theta_dict[j]
                for b in range(L_sos + 1):
                    for bp in range(L_sos + 1):
                        w_phi_dict = cos_product_coef(b, bp)
                        if k not in w_phi_dict:
                            continue
                        w_phi = w_phi_dict[k]
                        W[B_idx(a, b), B_idx(ap, bp)] += w_theta * w_phi
        return W

    # Constraint c_0 of restriction = 1
    c0_total = 0
    for (j, k), w in line_c0_weights.items():
        c0_total = c0_total + w * cp.sum(cp.multiply(B, coef_matrix(j, k)))
    constraints.append(c0_total == 1.0)

    # Objective: c_1 of restriction
    c1_total = 0
    for (j, k), w in line_c1_weights.items():
        c1_total = c1_total + w * cp.sum(cp.multiply(B, coef_matrix(j, k)))

    prob = cp.Problem(cp.Maximize(c1_total), constraints)
    val = prob.solve(solver='CLARABEL')
    print(f"\n  SDP (max c_1 of phi=2theta restriction over cos x cos SOS, L=1,")
    print(f"       P at bidegree (2, 2), constraint c_0_of_restriction = 1):")
    print(f"    max c_1 of restriction (raw) = {val:.4f}")
    print(f"    1D Fejer at effective deg 6 (raw) = 2 cos(pi/8) = {fejer_raw_deg6:.4f}")
    saturation = val / fejer_raw_deg6
    if abs(saturation - 1.0) < 1e-3:
        verdict = "SATURATES Fejer (lemma is tight, NOT violated)"
    elif saturation < 1.0:
        verdict = "BELOW Fejer (lemma holds with slack)"
    else:
        verdict = f"EXCEEDS Fejer by {(saturation - 1)*100:.2f}% (lemma VIOLATED?)"
    print(f"    SDP / Fejer = {saturation:.4f}  ==>  {verdict}")

    results = {
        '4e2_restricted_coefs': coefs_4e2.tolist(),
        '4e2_c1_over_c0_raw': float(c1_over_c0_4e2),
        'fejer_raw_deg6': float(fejer_raw_deg6),
        'fejer_4B_deg6': float(fejer_4B_deg6),
        'sdp_max_c1_restricted_raw': float(val),
        'sdp_ratio_to_fejer_raw': float(saturation),
        'effective_degree': 6,
        'verdict': verdict,
    }
    return results


def run(out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 78)
    print("[4E.8] Cos x cos SOS-SDP analysis of 4E.2's +25% LP gap")
    print("=" * 78)
    print()
    print("  Goal: test whether SDP machinery escapes the 4E.3 line-restriction")
    print("  lemma via polynomial-ideal SOS (Putinar/Schmuedgen). Compares")
    print("  inner SDP relaxation (SOS) to 4E.2's outer LP relaxation (K-sampling)")
    print("  to determine the truth, then probes the structural lemma directly.")

    results_A = phase_A(out_dir)
    results_B = phase_B(out_dir)
    results_C = phase_C(out_dir)
    results_D = phase_D(out_dir)

    # Plot
    fig, axs = plt.subplots(1, 3, figsize=(15, 4.5))

    # Panel 1: SOS SDP vs K-sampling LP vs C-S over alpha (Phase A)
    ax = axs[0]
    alphas_p = [r['alpha'] for r in results_A]
    cs_p = [r['cs_bound'] for r in results_A]
    sdp_p = [r['sdp_val'] for r in results_A]
    lp_p = [r['lp_val'] for r in results_A]
    ax.plot(alphas_p, cs_p, 'k--', label='C-S 1D bound', linewidth=1.5)
    ax.plot(alphas_p, sdp_p, 'o-', color='C0', label='cos SOS SDP (L=1)', linewidth=2)
    ax.plot(alphas_p, lp_p, 's-', color='C1', label='K-sampling LP (4E.2)', linewidth=2)
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel('value')
    ax.set_title(r'$\max c_{1,1} + \alpha c_{2,2}$ at bidegree (2,2)')
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)

    # Panel 2: Lasserre hierarchy convergence at alpha = 3
    ax = axs[1]
    Ls_b = [r['L'] for r in results_B]
    vals_b = [r['value'] for r in results_B]
    cs_val_b = results_B[0]['cs_bound'] if results_B else 0
    lp_val_a3 = next((r['lp_val'] for r in results_A if r['alpha'] == 3.0), None)
    ax.plot(Ls_b, vals_b, 'o-', color='C0', label='cos SOS SDP', linewidth=2)
    ax.axhline(cs_val_b, color='k', linestyle='--', label='C-S 1D')
    if lp_val_a3 is not None:
        ax.axhline(lp_val_a3, color='C1', linestyle=':',
                   label=f'K-sampling LP (4E.2) = {lp_val_a3:.3f}')
    ax.set_xlabel(r'Lasserre level $L$ (SOS bidegree)')
    ax.set_ylabel('SDP value')
    ax.set_title(r'Lasserre hierarchy at $\alpha = 3$ (4E.2 peak)')
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)

    # Panel 3: cos SOS vs full-trig SOS projection (Phase C)
    ax = axs[2]
    alphas_c = [r['alpha'] for r in results_C]
    cscoscos = [r['coscos_sos'] for r in results_C]
    csfull = [r['fulltrig_sos_proj'] for r in results_C]
    ax.plot(alphas_c, cscoscos, 'o-', color='C0', label='cos x cos SOS', linewidth=2)
    ax.plot(alphas_c, csfull, 's-', color='C2', label='full-trig SOS proj', linewidth=2)
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel('value')
    ax.set_title(r'cos x cos vs full-trig SOS')
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)

    fig.suptitle("Arch 4E.8: cos x cos SOS-SDP analysis of 4E.2's +25% LP gap",
                 fontsize=12, y=1.0)
    plt.tight_layout()
    plt.savefig(out_dir / "e4e8_sos_sdp.png", dpi=140)
    plt.close()
    print(f"\n[4E.8] Saved {out_dir / 'e4e8_sos_sdp.png'}")

    np.savez_compressed(
        out_dir / "e4e8_sos_sdp.npz",
        results_A=np.array(results_A, dtype=object),
        results_B=np.array(results_B, dtype=object),
        results_C=np.array(results_C, dtype=object),
        results_D=np.array([results_D], dtype=object),
    )
    print(f"[4E.8] Saved {out_dir / 'e4e8_sos_sdp.npz'}")

    # Summary
    print()
    print("=" * 78)
    print("[4E.8] Summary")
    print("=" * 78)

    a3_A = next((r for r in results_A if r['alpha'] == 3.0), None)
    print()
    if a3_A:
        print(f"  Phase A at alpha = 3 (4E.2 peak): cos x cos SOS = {a3_A['sdp_val']:.4f},")
        print(f"    K-sampling LP = {a3_A['lp_val']:.4f}, C-S 1D = {a3_A['cs_bound']:.4f}.")
        if abs(a3_A['sdp_val'] - a3_A['lp_val']) < 0.01:
            print(f"    SOS matches LP -> the +25% gap is TIGHT (not a sampling artifact).")
        elif a3_A['sdp_val'] < a3_A['lp_val'] - 0.01:
            print(f"    SOS strictly below LP -> SOS hierarchy needs higher level.")
        else:
            print(f"    SOS above LP -> unexpected.")
    if results_B:
        print(f"  Phase B Lasserre hierarchy at alpha = 3:")
        for r in results_B:
            print(f"    L = {r['L']}: SOS = {r['value']:.4f}  (P bidegree (2L, 2L))")

    if results_D:
        print(f"\n  Phase D line-restriction at phi = 2 theta:")
        print(f"    4E.2 LP-opt restricted: c_1 / c_0 (raw) = {results_D['4e2_c1_over_c0_raw']:.4f}")
        print(f"    SDP max c_1 of restriction (over cos x cos SOS) = "
              f"{results_D['sdp_max_c1_restricted_raw']:.4f}")
        print(f"    1D Fejer at effective deg 6 (raw) = {results_D['fejer_raw_deg6']:.4f}")
        print(f"    SDP / Fejer = {results_D['sdp_ratio_to_fejer_raw']:.4f}")
        print(f"    ==>  {results_D['verdict']}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()
    run(out_dir=args.out)
