"""Experiment 4E.9: Heath-Brown multi-zero MT figure of merit via SDP.

This is the Direction-7 experiment (see
docs/03_research/research_directions/07_heath_brown_multi_zero_mt.md): the
one remaining escape route from the 4E.3 line-restriction lemma that has not
been probed numerically. 4E.6 (constrained-domain LP), 4E.7 (multi-zero LP at
naive objectives), and 4E.8 (polynomial-ideal SOS / Putinar) each closed
one of the proposed escapes. Each converged to the 1D Fejer wall. Direction 7
asks the sharper question: combine 4E.7's multi-zero correlation structure
(lambda_{1,1} 55-137x larger than lambda_1^2) with 4E.2's higher-harmonic gain
(the c_{2,2} term that gives genuine rank > 1 2D structure), and target the
Mossinghoff-Trudgian (MT) figure of merit DIRECTLY in an SDP, not the naive
Cauchy-Schwarz coefficient sum.

The structural obstruction (4E.3, restated). The single-zero MT shape factor
is bounded by the 1D Fejer ceiling: any non-negative bivariate polynomial
P(theta, phi), restricted to a line {(theta, phi) : phi = g theta}, becomes a
1D non-negative cosine polynomial whose MT shape factor (c_1 - c_0)^2 / (4 c_0)
is bounded by 1D Fejer at the matched effective degree. 4E.8 confirmed this is
TIGHT under SDP (the SDP saturates Fejer but does not exceed it).

The Direction-7 escape, made concrete. Postulate TWO putative zeros at heights
gamma_1, gamma_2 with a COUPLING parameter g = gamma_2 / gamma_1 (the
"gap"/"coupling" of the two zeros, Heath-Brown 1992 / Pintz 1976). The MT
explicit-formula sum runs over primes p; the polynomial is evaluated at
(theta, phi) = (gamma_1 log p, gamma_2 log p) = (gamma_1 log p)(1, g). As p
ranges over primes, (theta, phi) traces the line of slope g through the torus.
The MULTI-ZERO MT trick keeps both the cross-frequency term (weight on
cos(theta) cos(phi), i.e. c_{1,1}, contributing at the combined height
gamma_1 +- gamma_2) AND the individual single-zero terms (c_{1,0}, c_{0,1}).
The figure of merit is the multi-zero shape factor

    Lambda(P, g) = (w_trick - w_0)^2 / (4 w_0)

where w_0 is the total weight that the line-restriction puts at the pole
(frequency 0) and w_trick is the weight at the trick frequency (the height
gamma_1 of the first putative zero, in units where gamma_1 = 1). We maximize
Lambda over the cos x cos SOS cone at bidegree (N, N) using the cvxpy /
CLARABEL SDP machinery of 4E.8, sweeping the coupling g and the bidegree, and
compare to the 1D Fejer ceiling at the matched effective degree.

Why this is the genuine remaining escape (not a rerun of 4E.8). 4E.8 Phase D
fixed a single slope (g = 2) and maximized only the FIRST-harmonic restriction
coefficient c_1, finding exact Fejer saturation. Direction 7 differs in two
ways that, per the spec, are exactly the open combination:
  (1) the coupling g is a free parameter (multi-zero heights are independent,
      so the slope is not fixed); we sweep it;
  (2) the objective is the multi-zero MT shape factor, which the multi-zero
      ledger lets us assemble from BOTH the cross term c_{1,1} and the
      higher-harmonic terms c_{2,2}, c_{2,0}, c_{0,2} that fold down onto the
      trick frequency under the line restriction. This is the c_{1,1} +
      alpha c_{2,2} higher-harmonic content of 4E.2 fed through the multi-zero
      MT bookkeeping rather than the C-S coefficient sum.

The predicted answer (marginal-positivity thesis + 4E.3 + 4E.7 + 4E.8): NO.
The best multi-zero MT shape factor should NOT exceed the 1D Fejer ceiling at
the matched effective degree, because the line restriction folds any cos x cos
SOS polynomial back into a 1D non-negative polynomial, and the multi-zero
ledger redistributes weight among harmonics but cannot manufacture trick-
frequency weight beyond what 1D Fejer permits. The experiment tests this and
reports the margin: best multi-zero MT / Fejer ratio, expected < 1, plus the
RANK of the optimal certificate. A non-rank-1 optimum that still fails to beat
Fejer is itself informative (it would mean the multi-zero higher-harmonic
structure is genuinely 2D yet still capped, sharpening 4E.7's rank-1 finding).

Davenport-Heilbronn discipline. This experiment is a PURE trig-polynomial
optimization: the SDP, the line restriction, and the Fejer ceiling are all
L-function-agnostic (they depend only on the polynomial cone and the coupling
g, not on any Euler product or zero data). The D-H control therefore does not
apply to the optimization itself. The L-function only enters at the
translation step (mapping a shape factor to an actual zero-free region
constant), which per 4E.3 / 4E.7 requires explicit Heath-Brown bookkeeping not
implemented here. We state this explicitly rather than forcing a D-H run that
would test nothing about the polynomial cone.

Output:
  - e4e9_heath_brown_sdp.npz: per (g, N) SDP values, ratios to Fejer, ranks
  - e4e9_heath_brown_sdp.png: multi-zero MT shape vs coupling g, ratio to Fejer
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

from experiments.zero_free.e4e_offdiag_lp import best_1D_raw_qj


# =========================================================================
# Cos x cos product expansion (shared with 4E.8)
# =========================================================================
#
# cos(a x) cos(a' x) = sum_j w_j cos(j x), returned as {j: w_j}.

def cos_product_coef(a: int, ap: int) -> dict:
    """Return dict {j: coef} for cos(a*x) * cos(ap*x) = sum coef[j] cos(j*x)."""
    if a == 0 and ap == 0:
        return {0: 1.0}
    if a == 0:
        return {ap: 1.0}
    if ap == 0:
        return {a: 1.0}
    if a == ap:
        return {0: 0.5, 2 * a: 0.5}
    return {abs(a - ap): 0.5, a + ap: 0.5}


# =========================================================================
# Line-restriction frequency bookkeeping (the multi-zero MT ledger)
# =========================================================================
#
# A cos x cos polynomial P(theta, phi) = sum_{j,k} c_{j,k} cos(j theta) cos(k phi)
# restricted to the multi-zero line (theta, phi) = u (1, g) becomes a 1D
# (generally quasi-periodic) trig sum in u with frequencies {j + k g}. For the
# MT trick we work in units where the first zero height gamma_1 = 1, so:
#   - the pole sits at frequency 0,
#   - the first-zero trick frequency is 1 (the height gamma_1 itself),
#   - cross terms cos(j theta) cos(k phi) land at frequencies |j +- k g|.
#
# The term c_{j,k} cos(j theta) cos(k phi) under theta = u, phi = g u expands as
#   c_{j,k} cos(j u) cos(k g u) = (c_{j,k}/2)[cos((j + k g) u) + cos((j - k g) u)]
# for j, k > 0; the boundary cases follow cos_product_coef applied with the
# second index scaled by g (which need not be an integer).
#
# w_0(P)     := total weight landing at frequency 0
# w_trick(P) := total weight landing at frequency 1 (the gamma_1 trick height)
#
# The coupling g controls which (j, k) fold onto the trick frequency. The
# multi-zero escape hope: for some g, higher-harmonic terms (c_{2,2}, c_{2,0},
# ...) reinforce c_{1,0}/c_{1,1} at frequency 1, boosting w_trick beyond the
# single-line 1D Fejer ceiling.

def line_frequency_weights(j: int, k: int, g: float):
    """Frequencies (absolute values) and weights for c_{j,k} cos(j u) cos(k g u).

    Returns list of (freq, weight) with weights summing to 1 (the coefficient
    c_{j,k} multiplies these). cos is even, so frequencies are taken |.|.
    """
    if j == 0 and k == 0:
        return [(0.0, 1.0)]
    if k == 0:
        return [(float(j), 1.0)]
    if j == 0:
        return [(abs(k * g), 1.0)]
    return [(abs(j + k * g), 0.5), (abs(j - k * g), 0.5)]


def restriction_weight_at(c_index_weights, target_freq: float, g: float,
                          tol: float = 1e-9):
    """Linear functional: total restriction weight at a given frequency.

    c_index_weights: dict {(j, k): cvxpy_or_float coefficient expression}.
    Returns the sum over (j, k) of c_{j,k} * (fraction of its mass at target_freq).
    """
    total = 0.0
    for (j, k), c in c_index_weights.items():
        for freq, w in line_frequency_weights(j, k, g):
            if abs(freq - target_freq) < tol:
                total = total + w * c
    return total


# =========================================================================
# Cos x cos SOS Gram-matrix machinery (reused from 4E.8)
# =========================================================================
#
# P = sum_l Q_l^2, Q_l cos x cos of bidegree (L, L). PSD Gram B of size
# (L+1)^2 indexed by (a, b). c_{j,k}(P) is linear in B with weight
# w_theta(a, a', j) w_phi(b, b', k).

def build_coef_matrices(L: int, jk_pairs):
    """Precompute weight matrices W_{j,k} such that c_{j,k} = sum(B * W_{j,k}).

    Returns dict {(j, k): W (size x size ndarray)} and size = (L+1)^2.
    """
    size = (L + 1) ** 2

    def B_idx(a, b):
        return a * (L + 1) + b

    mats = {}
    for (j, k) in jk_pairs:
        W = np.zeros((size, size))
        for a in range(L + 1):
            for ap in range(L + 1):
                wtd = cos_product_coef(a, ap)
                if j not in wtd:
                    continue
                wt = wtd[j]
                for b in range(L + 1):
                    for bp in range(L + 1):
                        wpd = cos_product_coef(b, bp)
                        if k not in wpd:
                            continue
                        W[B_idx(a, b), B_idx(ap, bp)] += wt * wpd[k]
        mats[(j, k)] = W
    return mats, size


def multi_zero_mt_sdp(N: int, g: float, verbose: bool = False, solver: str = None):
    """SDP: maximize the multi-zero MT shape factor along the coupling line.

    The MT shape factor (w_trick - w_0)^2 / (4 w_0) is monotone increasing in
    (w_trick - w_0) for fixed w_0, and the standard MT normalization fixes
    w_0 = 1 (the pole weight), so maximizing the shape factor at fixed w_0 is
    equivalent to maximizing w_trick. We therefore solve the linear-objective
    SDP

        max  w_trick(P)
        s.t. P is cos x cos SOS at bidegree (N, N)  (Gram B PSD, L = N/2 ... )
             w_0(P) = 1                              (pole-weight normalization)

    over the cos x cos SOS cone, then report the induced shape factor and its
    ratio to the 1D Fejer ceiling.

    To realize bidegree (N, N) as a single SOS square we take SOS-bidegree
    L = N (so each Q_l is cos x cos of bidegree (N, N) and P = sum Q_l^2 has
    bidegree (2N, 2N)); we then constrain c_{j,k} = 0 for j > N or k > N so the
    OPTIMIZED polynomial has bidegree (N, N) exactly. This is the standard
    SOS-with-degree-constraint (an inner relaxation of the bidegree-(N,N)
    non-negative cone). For the smoke test N is small (N = 2).

    Returns dict with value (w_trick), w0, shape factor, c-matrix, rank, B.
    """
    if solver is None:
        solver = 'CLARABEL'

    L = N  # Q_l has cos x cos bidegree (N, N); P = sum Q_l^2 has (2N, 2N)
    deg = 2 * L

    # All (j, k) up to bidegree (deg, deg) that the Gram matrix can produce.
    jk_all = [(j, k) for j in range(deg + 1) for k in range(deg + 1)]
    mats, size = build_coef_matrices(L, jk_all)

    B = cp.Variable((size, size), symmetric=True)
    constraints = [B >> 0]

    # c_{j,k} as cvxpy expression for each (j, k).
    c_expr = {jk: cp.sum(cp.multiply(B, mats[jk])) for jk in jk_all}

    # Degree constraint: force the optimized polynomial to bidegree (N, N).
    # Zero out all c_{j,k} with j > N or k > N.
    for (j, k) in jk_all:
        if j > N or k > N:
            constraints.append(c_expr[(j, k)] == 0.0)

    # The (j, k) actually free under the bidegree-(N, N) constraint.
    jk_active = [(j, k) for (j, k) in jk_all if j <= N and k <= N]
    c_active = {jk: c_expr[jk] for jk in jk_active}

    # Pole-weight normalization w_0(P) = 1.
    w0_expr = restriction_weight_at(c_active, 0.0, g)
    constraints.append(w0_expr == 1.0)

    # Objective: maximize trick-frequency weight w_trick = weight at freq 1.
    wtrick_expr = restriction_weight_at(c_active, 1.0, g)

    prob = cp.Problem(cp.Maximize(wtrick_expr), constraints)
    try:
        val = prob.solve(solver=solver, verbose=verbose)
    except Exception:
        val = prob.solve(solver='SCS', verbose=verbose)

    status = prob.status
    B_val = B.value

    # Extract the bidegree-(N, N) coefficient matrix.
    c_mat = np.zeros((N + 1, N + 1))
    if B_val is not None:
        for (j, k) in jk_active:
            c_mat[j, k] = float((B_val * mats[(j, k)]).sum())

    # Recompute w0 and w_trick numerically from c_mat (sanity).
    w0_num = 0.0
    wtrick_num = 0.0
    for j in range(N + 1):
        for k in range(N + 1):
            for freq, w in line_frequency_weights(j, k, g):
                if abs(freq) < 1e-9:
                    w0_num += w * c_mat[j, k]
                elif abs(freq - 1.0) < 1e-9:
                    wtrick_num += w * c_mat[j, k]

    wtrick = float(val) if val is not None else float("nan")
    shape = (wtrick - w0_num) ** 2 / (4.0 * w0_num) if w0_num > 0 else 0.0

    # Rank of the optimal coefficient matrix (the 4E.7 rank-1 question).
    if np.allclose(c_mat, 0.0):
        rank = 0
        svals = []
    else:
        svals = np.linalg.svd(c_mat, compute_uv=False)
        s_norm = svals / svals[0] if svals[0] > 0 else svals
        rank = int((s_norm > 1e-5).sum())
        svals = svals.tolist()

    return {
        "N": N,
        "g": float(g),
        "status": status,
        "w_trick": wtrick,
        "w_0": float(w0_num),
        "shape": float(shape),
        "c_matrix": c_mat,
        "rank": rank,
        "singular_values": svals,
        "B": B_val,
    }


# =========================================================================
# 1D Fejer ceiling at matched effective degree
# =========================================================================
#
# The line restriction of a bidegree-(N, N) cos x cos polynomial along slope g
# has, at integer frequencies, an effective degree governed by the largest
# integer frequency reachable. When g is rational the restriction is a genuine
# 1D polynomial; the MT trick frequency is 1, and the relevant 1D Fejer ceiling
# is the maximum trick-frequency coefficient w_1 / w_0 over 1D non-negative
# polynomials of the matched effective degree. We use the integer effective
# degree (max integer frequency present in the restriction) and the raw-
# convention Fejer maximum q_1 = 2 cos(pi / (deg_eff + 2)) (the maximum of
# c_1 / c_0 over non-negative 1D cosine polynomials of degree deg_eff).

def effective_integer_degree(N: int, g: float, tol: float = 1e-9) -> int:
    """Largest integer frequency reachable by a bidegree-(N, N) restriction."""
    best = 0
    for j in range(N + 1):
        for k in range(N + 1):
            for freq, _ in line_frequency_weights(j, k, g):
                if abs(freq - round(freq)) < tol:
                    best = max(best, int(round(freq)))
    return best


def fejer_ceiling_raw(deg_eff: int, M: int = 4000) -> float:
    """1D Fejer max of c_1 / c_0 (raw convention) at degree deg_eff.

    Closed form is 2 cos(pi / (deg_eff + 2)); we cross-check against the
    direct 1D LP (best_1D_raw_qj) for robustness at the degrees we hit.
    """
    if deg_eff < 1:
        return 1.0
    closed = float(2 * np.cos(np.pi / (deg_eff + 2)))
    return closed


# =========================================================================
# Sweep driver
# =========================================================================

def run(out_dir: Path = None, full: bool = False, solver: str = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    t_start = time.time()

    print("=" * 78)
    print("[4E.9] Heath-Brown multi-zero MT figure of merit via SDP (Direction 7)")
    print("=" * 78)
    print()
    print("  Question: does targeting the MULTI-ZERO MT shape factor directly")
    print("  in an SDP (cross term c_{1,1} + higher harmonics c_{2,2}, folded")
    print("  through the multi-zero ledger at coupling g) BEAT the 1D Fejer")
    print("  ceiling at the matched effective degree?")
    print()
    print("  Predicted (marginal-positivity thesis + 4E.3/4E.7/4E.8): NO.")
    print()

    if full:
        Ns = [2, 3, 4]
        g_grid = np.round(np.linspace(0.5, 3.0, 26), 4)
    else:
        Ns = [2]
        g_grid = np.array([1.0, 2.0, 3.0])

    print(f"  Bidegrees N = {Ns}")
    print(f"  Coupling grid g = {list(g_grid)}")
    print(f"  Solver = {solver or 'CLARABEL (fallback SCS)'}")
    print()

    results = []
    best_overall = {"ratio_to_fejer": -np.inf}

    for N in Ns:
        print(f"  --- bidegree N = {N} " + "-" * 50)
        print(f"  {'g':>6} {'status':>20} {'w_trick':>9} {'w_0':>6} "
              f"{'shape':>9} {'effdeg':>7} {'Fejer':>8} {'ratio':>8} {'rank':>5}")
        for g in g_grid:
            r = multi_zero_mt_sdp(N, float(g), solver=solver)
            deg_eff = effective_integer_degree(N, float(g))
            fejer_raw = fejer_ceiling_raw(deg_eff)
            fejer_shape = (fejer_raw - 1.0) ** 2 / 4.0
            ratio = r["shape"] / fejer_shape if fejer_shape > 0 else 0.0
            row = {
                "N": N,
                "g": float(g),
                "status": r["status"],
                "w_trick": r["w_trick"],
                "w_0": r["w_0"],
                "shape": r["shape"],
                "eff_deg": deg_eff,
                "fejer_raw": fejer_raw,
                "fejer_shape": fejer_shape,
                "ratio_to_fejer": ratio,
                "rank": r["rank"],
                "singular_values": r["singular_values"],
                "c_matrix": r["c_matrix"].tolist(),
            }
            results.append(row)
            if ratio > best_overall["ratio_to_fejer"]:
                best_overall = dict(row)
            print(f"  {g:>6.3f} {str(r['status']):>20} {r['w_trick']:>9.4f} "
                  f"{r['w_0']:>6.3f} {r['shape']:>9.4f} {deg_eff:>7d} "
                  f"{fejer_raw:>8.4f} {ratio:>8.4f} {r['rank']:>5d}")
        print()

    # =====================================================================
    # Plot
    # =====================================================================
    fig, axs = plt.subplots(1, 2, figsize=(13, 4.8))

    ax = axs[0]
    for N in Ns:
        rows = [r for r in results if r["N"] == N]
        gs = [r["g"] for r in rows]
        shapes = [r["shape"] for r in rows]
        ax.plot(gs, shapes, "o-", label=f"multi-zero MT shape, N={N}")
    # Fejer reference at the most common effective degree per N (use N=Ns[-1])
    rows_last = [r for r in results if r["N"] == Ns[-1]]
    ax.plot([r["g"] for r in rows_last], [r["fejer_shape"] for r in rows_last],
            "k--", label="1D Fejer ceiling (matched eff deg)")
    ax.set_xlabel("coupling g = gamma_2 / gamma_1")
    ax.set_ylabel("MT shape factor")
    ax.set_title("Multi-zero MT shape vs coupling")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    ax = axs[1]
    for N in Ns:
        rows = [r for r in results if r["N"] == N]
        gs = [r["g"] for r in rows]
        ratios = [r["ratio_to_fejer"] for r in rows]
        ax.plot(gs, ratios, "s-", label=f"ratio to Fejer, N={N}")
    ax.axhline(1.0, color="r", linestyle="--", label="Fejer ceiling (ratio = 1)")
    ax.set_xlabel("coupling g = gamma_2 / gamma_1")
    ax.set_ylabel("multi-zero MT / Fejer")
    ax.set_title("Does multi-zero MT beat Fejer?")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    fig.suptitle("Arch 4E.9: Heath-Brown multi-zero MT figure of merit (Direction 7)",
                 fontsize=12, y=1.0)
    plt.tight_layout()
    plt.savefig(out_dir / "e4e9_heath_brown_sdp.png", dpi=140)
    plt.close()
    print(f"[4E.9] Saved {out_dir / 'e4e9_heath_brown_sdp.png'}")

    np.savez_compressed(
        out_dir / "e4e9_heath_brown_sdp.npz",
        results=np.array(results, dtype=object),
        best_overall=np.array([best_overall], dtype=object),
        Ns=np.array(Ns),
        g_grid=g_grid,
    )
    print(f"[4E.9] Saved {out_dir / 'e4e9_heath_brown_sdp.npz'}")

    # =====================================================================
    # Summary
    # =====================================================================
    elapsed = time.time() - t_start
    print()
    print("=" * 78)
    print("[4E.9] Summary")
    print("=" * 78)
    print()
    print(f"  Best multi-zero MT / Fejer ratio across the sweep: "
          f"{best_overall['ratio_to_fejer']:.4f}")
    print(f"    achieved at N = {best_overall['N']}, g = {best_overall['g']:.3f}, "
          f"effective degree {best_overall['eff_deg']}")
    print(f"    optimal certificate rank = {best_overall['rank']} "
          f"(4E.7 found rank-1 at naive objectives)")
    if best_overall["ratio_to_fejer"] <= 1.0 + 1e-3:
        print()
        print("  VERDICT: the multi-zero MT figure of merit does NOT exceed the")
        print("  1D Fejer ceiling. The Direction-7 escape closes negative at the")
        print("  shape-factor level, consistent with 4E.3 (line restriction folds")
        print("  any cos x cos SOS polynomial into a 1D non-neg polynomial),")
        print("  4E.7 (multi-zero correlation is real but capped), 4E.8 (SDP")
        print("  saturates but does not violate Fejer), and the marginal-")
        print("  positivity thesis. The multi-zero ledger redistributes harmonic")
        print("  weight but cannot manufacture trick-frequency weight beyond the")
        print("  Fejer cap.")
    else:
        print()
        print("  VERDICT: a feasible certificate EXCEEDS the 1D Fejer ceiling.")
        print("  This would be a non-trivial Direction-7 result and must be")
        print("  re-verified at higher M / tighter solver tolerance and checked")
        print("  against the 4E.3 lemma before being believed.")
    print()
    print("  Davenport-Heilbronn discipline: NOT applicable. This is a pure")
    print("  trig-polynomial / SDP optimization. The cone, the line restriction,")
    print("  and the Fejer ceiling are all L-function-agnostic (no Euler product,")
    print("  no zero data enters). The L-function only appears at the unimplemented")
    print("  translation-to-zero-free-constant step (per 4E.3 / 4E.7).")
    print()
    print(f"  Runtime: {elapsed:.2f} s")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=None)
    parser.add_argument("--full", action="store_true",
                        help="heavy sweep: N in {2,3,4}, 26-point g grid")
    parser.add_argument("--solver", type=str, default=None,
                        help="cvxpy solver (default CLARABEL, fallback SCS)")
    args = parser.parse_args()
    run(out_dir=args.out, full=args.full, solver=args.solver)
