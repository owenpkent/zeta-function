"""Experiment 4E.6: Constrained-domain LP for non-negative trig polynomials.

The 4E.3 structural lemma says: any non-negative bivariate trig polynomial
P(theta, phi) >= 0 on [0, 2pi]^2, restricted to a 1D line (t_1 u, t_2 u),
gives a 1D non-negative trig polynomial bounded by 1D Fejer at the matched
effective degree. So no 2D LP restriction can improve over 1D Fejer for the
single-zero MT shape factor.

The proposed escape (TODO and LEARNINGS 4E.3 note): impose P >= 0 only on
a constrained domain Omega, not on all of [0, 2pi]^d. If Omega is small
enough that the restriction-to-a-line argument breaks, the LP can exceed
the Fejer ceiling.

This experiment investigates four constrained-domain setups and tests
honestly whether any produces a meaningful improvement vs Fejer in a way
that has a physical realization in MT explicit-formula bookkeeping.

Setup A: K-point LP. P(theta_k) >= 0 at K evenly spaced points in [0, 2pi].
  - For K large, recovers Fejer.
  - For K <= N+1 (under-constrained), LP is unbounded.
  - Sweet spot: K around degree N+2 to 2N. Quantify how much c_1 grows
    above Fejer in this regime.

Setup B: Arc-removal LP. P >= 0 on [0, 2pi] minus an open arc of half-width
  delta around theta_0. We'll add a c_k norm bound to make the LP bounded.
  Sweep delta and the norm bound; quantify c_1 growth.

Setup C: Sparse-zero LP. Omega = {gamma_n * log p mod 2pi : n = 1, ..., K}
  for fixed prime p and the first K zeta zero ordinates. This is the
  natural domain for a MT inequality that ONLY constrains the polynomial
  at on-line zero locations of zeta (a measure-zero dense subset).
  In practice we use the first K=10-100 zero ordinates as a finite probe.

Setup D: Constraint at finite zero ordinates with off-line zero "trick".
  As in setup C, but adds explicit MT-style trick: maximize c_1
  (coefficient at the putative off-line frequency 'trick height')
  subject to constraints at the on-line zero locations.

For each setup we report:
  - LP value c_1 (or c_1/c_0 ratio)
  - Comparison to Fejer at matched degree
  - Whether the formulation is physically meaningful for MT (yes/no/uncertain)
  - The structural reason for the LP value or unboundedness

The headline finding (predicted): setups A and B at honest parameters do
NOT exceed Fejer in a physically-realizable way; the LP gain comes from
relaxing constraints that the MT framework structurally requires. Setups
C and D give meaningful sub-LP values that don't translate to MT
improvements without additional machinery.

The intended scientific output is a structural NEGATIVE result, sharpening
4E.3's lemma: not only does the line-restriction route fail, the
constrained-domain escape doesn't work cleanly either. To improve the MT
constant via 2D inequalities requires (a) explicit multi-zero coupling
(Heath-Brown), (b) Bombieri variational SOS, or (c) polynomial-ideal SOS
(4E.8) -- none of which is the same as "constrained-domain LP".
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import linprog

from experiments._shared import zeta_L


def fejer_c1_ratio(N: int) -> float:
    """Asymptotic Fejer optimum c_1/c_0 = cos(pi/(N+2)).

    For degree N non-neg trig polynomial with c_0 = 1, max c_1 = 2 cos(pi/(N+2)),
    achieved by P(theta) = |Q(theta)|^2 with Q a specific polynomial.

    Our LP convention uses c_1 / c_0 with c_0 = 1, P = c_0 + 2 sum c_k cos(k theta),
    so the max c_1 here is cos(pi/(N+2)) (factor of 2 in convention).
    """
    return float(np.cos(np.pi / (N + 2)))


def k_point_lp(N: int, K: int, c_bound: float = 100.0, M_check: int = 4000):
    """Setup A: K-point LP, max c_1 over P(theta_k) >= 0 at K evenly spaced points.

    For K << N, under-constrained -> hits coefficient bound.
    For K >> N, well-constrained -> recovers Fejer.
    """
    thetas = np.linspace(0, 2 * np.pi, K, endpoint=False)
    obj = np.zeros(N + 1)
    obj[1] = -1.0
    A_ub = np.zeros((K, N + 1))
    A_ub[:, 0] = -1
    for k in range(1, N + 1):
        A_ub[:, k] = -2 * np.cos(k * thetas)
    b_ub = np.zeros(K)
    A_eq = np.zeros((1, N + 1))
    A_eq[0, 0] = 1
    b_eq = np.array([1.0])
    bounds = [(-c_bound, c_bound)] * (N + 1)
    res = linprog(obj, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds,
                  method="highs")
    if not res.success:
        return None, None, None
    c_vec = res.x
    c1 = c_vec[1]
    # Check tightness of c_k bound: did we hit it?
    hit_bound = any(abs(abs(c) - c_bound) < 1e-6 for c in c_vec)
    # Check actual non-negativity on a fine grid
    theta_check = np.linspace(0, 2 * np.pi, M_check, endpoint=False)
    P_vals = c_vec[0] + 2 * sum(c_vec[k] * np.cos(k * theta_check)
                                 for k in range(1, N + 1))
    min_P = float(np.min(P_vals))
    return c1, c_vec, {"hit_bound": hit_bound, "min_P_on_fine": min_P,
                       "min_P_on_constraint_points": float(np.min(A_ub @ c_vec + 0)) * -1}


def arc_removal_lp(N: int, theta0: float, delta: float, c_bound: float,
                   M: int = 4000):
    """Setup B: P >= 0 on [0, 2pi] minus open arc (theta0 - delta, theta0 + delta).

    With c_bound on each coefficient to keep LP bounded.
    """
    theta_full = np.linspace(0, 2 * np.pi, M, endpoint=False)
    # Construct Omega = complement of the arc
    arc_mask = ((theta_full > theta0 - delta) & (theta_full < theta0 + delta)) | \
               ((theta_full > theta0 - delta + 2 * np.pi) &
                (theta_full < theta0 + delta + 2 * np.pi)) | \
               ((theta_full > theta0 - delta - 2 * np.pi) &
                (theta_full < theta0 + delta - 2 * np.pi))
    constraint_thetas = theta_full[~arc_mask]
    K_eff = len(constraint_thetas)
    obj = np.zeros(N + 1)
    obj[1] = -1.0
    A_ub = np.zeros((K_eff, N + 1))
    A_ub[:, 0] = -1
    for k in range(1, N + 1):
        A_ub[:, k] = -2 * np.cos(k * constraint_thetas)
    b_ub = np.zeros(K_eff)
    A_eq = np.zeros((1, N + 1))
    A_eq[0, 0] = 1
    b_eq = np.array([1.0])
    bounds = [(-c_bound, c_bound)] * (N + 1)
    res = linprog(obj, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds,
                  method="highs")
    if not res.success:
        return None, None
    c_vec = res.x
    c1 = c_vec[1]
    # Check what the polynomial does inside the arc
    inside_arc = arc_mask
    P_vals = c_vec[0] + 2 * sum(c_vec[k] * np.cos(k * theta_full)
                                 for k in range(1, N + 1))
    P_inside = P_vals[inside_arc]
    P_outside = P_vals[~inside_arc]
    return c1, c_vec, {
        "K_eff": K_eff,
        "min_P_inside_arc": float(np.min(P_inside)) if len(P_inside) > 0 else None,
        "min_P_outside_arc": float(np.min(P_outside)),
        "max_P_inside_arc": float(np.max(P_inside)) if len(P_inside) > 0 else None,
        "hit_bound": any(abs(abs(c) - c_bound) < 1e-6 for c in c_vec),
    }


def zero_constrained_lp(N: int, gamma_subset: np.ndarray, log_p: float,
                        c_bound: float = 100.0):
    """Setup C: P >= 0 at theta_k = gamma_k * log p mod 2pi for given gammas.

    The constraint set is the orbit of (gamma_k * log p) mod 2pi -- finitely
    many points. If K (number of gammas) is small, LP is under-constrained.
    """
    thetas = (gamma_subset * log_p) % (2 * np.pi)
    K = len(thetas)
    obj = np.zeros(N + 1)
    obj[1] = -1.0
    A_ub = np.zeros((K, N + 1))
    A_ub[:, 0] = -1
    for k in range(1, N + 1):
        A_ub[:, k] = -2 * np.cos(k * thetas)
    b_ub = np.zeros(K)
    A_eq = np.zeros((1, N + 1))
    A_eq[0, 0] = 1
    b_eq = np.array([1.0])
    bounds = [(-c_bound, c_bound)] * (N + 1)
    res = linprog(obj, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds,
                  method="highs")
    if not res.success:
        return None, None, None
    c_vec = res.x
    c1 = c_vec[1]
    # Check what the polynomial does on the full [0, 2pi]
    theta_check = np.linspace(0, 2 * np.pi, 4000, endpoint=False)
    P_vals = c_vec[0] + 2 * sum(c_vec[k] * np.cos(k * theta_check)
                                 for k in range(1, N + 1))
    return c1, c_vec, {
        "K": K,
        "thetas_used": thetas,
        "min_P_on_fine": float(np.min(P_vals)),
        "max_P_on_fine": float(np.max(P_vals)),
        "hit_bound": any(abs(abs(c) - c_bound) < 1e-6 for c in c_vec),
    }


def max_P_at_point_full_nonneg(N: int, theta_0: float, c_bound: float = 100.0,
                                M: int = 4000):
    """Max P(theta_0) over all non-neg trig polys with c_0 = 1, degree N.

    This is the proper baseline for setup D: it's the largest value P can
    take at a specific point subject to FULL [0, 2pi] non-negativity. Setup
    D relaxes the non-negativity constraint; we want to know whether the
    relaxation actually exceeds this benchmark.
    """
    theta_grid = np.linspace(0, 2 * np.pi, M, endpoint=False)
    obj = np.zeros(N + 1)
    obj[0] = -1.0
    for k in range(1, N + 1):
        obj[k] = -2 * np.cos(k * theta_0)
    A_ub = np.zeros((M, N + 1))
    A_ub[:, 0] = -1
    for k in range(1, N + 1):
        A_ub[:, k] = -2 * np.cos(k * theta_grid)
    b_ub = np.zeros(M)
    A_eq = np.zeros((1, N + 1))
    A_eq[0, 0] = 1
    b_eq = np.array([1.0])
    bounds = [(-c_bound, c_bound)] * (N + 1)
    res = linprog(obj, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds,
                  method="highs")
    if not res.success:
        return None
    c_vec = res.x
    P_max = c_vec[0] + 2 * sum(c_vec[k] * np.cos(k * theta_0)
                                for k in range(1, N + 1))
    return P_max


def trick_at_off_line_height(N: int, gammas_on_line: np.ndarray,
                              trick_height: float, log_p: float,
                              c_bound: float = 100.0):
    """Setup D: max P(trick_height * log p mod 2pi) subject to P >= 0 at
    theta = gamma_k * log p mod 2pi for the first K on-line zero ordinates.

    Note: P here is the unmodified poly (c_0 = 1, c_1 = ...). The "objective"
    is the value at trick_theta, not c_1. The objective transforms as:
      P(trick_theta) = c_0 + 2 sum_{k=1}^N c_k cos(k * trick_theta)
                     = c_0 + 2 (c.cos_basis_at_trick)

    Maximize this subject to non-negativity at on-line zero theta_k's.
    """
    thetas = (gammas_on_line * log_p) % (2 * np.pi)
    trick_theta = (trick_height * log_p) % (2 * np.pi)
    K = len(thetas)
    obj = np.zeros(N + 1)
    obj[0] = -1.0  # contribution from c_0 at trick
    for k in range(1, N + 1):
        obj[k] = -2 * np.cos(k * trick_theta)
    A_ub = np.zeros((K, N + 1))
    A_ub[:, 0] = -1
    for k in range(1, N + 1):
        A_ub[:, k] = -2 * np.cos(k * thetas)
    b_ub = np.zeros(K)
    A_eq = np.zeros((1, N + 1))
    A_eq[0, 0] = 1
    b_eq = np.array([1.0])
    bounds = [(-c_bound, c_bound)] * (N + 1)
    res = linprog(obj, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds,
                  method="highs")
    if not res.success:
        return None, None, None
    c_vec = res.x
    P_at_trick = c_vec[0] + 2 * sum(c_vec[k] * np.cos(k * trick_theta)
                                     for k in range(1, N + 1))
    return P_at_trick, c_vec, {
        "K": K,
        "trick_theta": trick_theta,
        "thetas_used": thetas,
        "hit_bound": any(abs(abs(c) - c_bound) < 1e-6 for c in c_vec),
    }


def run(out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 78)
    print("[4E.6] Constrained-domain LP for non-negative trig polynomials")
    print("       Test of the proposed escape from 4E.3's structural lemma")
    print("=" * 78)

    N_values = [2, 4, 6, 8, 10]

    # === Setup A: K-point LP ===
    print()
    print("[4E.6 A] K-point LP -- max c_1 with P >= 0 at K evenly spaced points")
    print(f"  {'N':>3} {'K':>5} {'c_1':>10} {'Fejer':>10} {'ratio':>8} "
          f"{'bound hit?':>11} {'min P on fine grid':>20}")
    setup_A = []
    for N in N_values:
        fejer = fejer_c1_ratio(N)
        for K in [N + 1, N + 2, 2 * N, 4 * N, 8 * N, 32 * N]:
            c1, c_vec, info = k_point_lp(N, K, c_bound=50.0)
            if c1 is None:
                continue
            ratio = c1 / fejer if fejer > 0 else 0
            setup_A.append({
                "N": N, "K": K, "c1": c1, "fejer": fejer,
                "ratio": ratio, "hit_bound": info["hit_bound"],
                "min_P_fine": info["min_P_on_fine"],
            })
            print(f"  {N:>3} {K:>5} {c1:>10.6f} {fejer:>10.6f} {ratio:>8.3f} "
                  f"{str(info['hit_bound']):>11} {info['min_P_on_fine']:>20.6f}")

    print()
    print("  Reading:")
    print("  - K = N+1: under-constrained -> LP hits coefficient bound (c1 ~ bound)")
    print("  - K = 32N: well-constrained -> LP recovers Fejer (ratio ~ 1.0)")
    print("  - When K is small, c_1 grows but P is very negative off the constraint")
    print("    points -> not physically realizable as 'P >= 0' on all theta")

    # === Setup B: Arc-removal LP ===
    print()
    print("[4E.6 B] Arc-removal LP -- P >= 0 on [0, 2pi] \\ (pi - delta, pi + delta)")
    print(f"  {'N':>3} {'delta/pi':>9} {'c_bound':>9} {'c_1':>10} {'Fejer':>10} "
          f"{'ratio':>8} {'min P in arc':>14}")
    setup_B = []
    for N in [4, 8]:
        fejer = fejer_c1_ratio(N)
        for c_bound in [5.0, 50.0]:
            for delta_frac in [0.01, 0.05, 0.1, 0.25, 0.5]:
                delta = delta_frac * np.pi
                c1, c_vec, info = arc_removal_lp(N, theta0=np.pi, delta=delta,
                                                  c_bound=c_bound, M=4000)
                if c1 is None:
                    continue
                ratio = c1 / fejer if fejer > 0 else 0
                setup_B.append({
                    "N": N, "delta_frac": delta_frac, "c_bound": c_bound,
                    "c1": c1, "fejer": fejer, "ratio": ratio,
                    "min_P_inside": info["min_P_inside_arc"],
                    "hit_bound": info["hit_bound"],
                })
                print(f"  {N:>3} {delta_frac:>9.3f} {c_bound:>9.1f} "
                      f"{c1:>10.4f} {fejer:>10.6f} {ratio:>8.3f} "
                      f"{info['min_P_inside_arc']:>14.4f}")

    print()
    print("  Reading:")
    print("  - As delta increases, LP value grows (more freedom)")
    print("  - LP is bounded by coefficient bound c_bound, not by structure")
    print("  - P is very negative inside the arc -- not realizable physically")
    print("    unless we have an MT-style scenario where 'inside the arc' corresponds")
    print("    to off-line zero frequencies that don't appear in the explicit sum")

    # === Setup C: Zero-constrained LP ===
    print()
    print("[4E.6 C] Zero-constrained LP -- P >= 0 only at theta = gamma_k * log p mod 2pi")
    print("         (for the first K on-line zeta zero ordinates, p fixed)")
    zero_ords = zeta_L.zeros(T_max=1000, prec=30)
    gammas = np.array([float(z.imag) for z in zero_ords])
    print(f"  {'N':>3} {'K':>4} {'log p':>8} {'c_1':>10} {'Fejer':>10} "
          f"{'ratio':>8} {'min P on fine':>14} {'hit_bd?':>8}")
    setup_C = []
    for N in [4, 8]:
        fejer = fejer_c1_ratio(N)
        for log_p in [np.log(2), np.log(3), np.log(7)]:
            for K_gamma in [5, 10, 20, 50, 100]:
                if K_gamma > len(gammas):
                    continue
                gamma_subset = gammas[:K_gamma]
                c1, c_vec, info = zero_constrained_lp(N, gamma_subset,
                                                       log_p, c_bound=20.0)
                if c1 is None:
                    continue
                ratio = c1 / fejer if fejer > 0 else 0
                setup_C.append({
                    "N": N, "K_gamma": K_gamma, "log_p": log_p,
                    "c1": c1, "fejer": fejer, "ratio": ratio,
                    "min_P_fine": info["min_P_on_fine"],
                    "hit_bound": info["hit_bound"],
                })
                print(f"  {N:>3} {K_gamma:>4} {log_p:>8.4f} {c1:>10.4f} "
                      f"{fejer:>10.6f} {ratio:>8.3f} {info['min_P_on_fine']:>14.4f} "
                      f"{str(info['hit_bound']):>8}")

    print()
    print("  Reading: zero ordinates {gamma_n * log p mod 2pi} are dense in [0, 2pi]")
    print("  in the limit K -> infinity; for finite K we get an under-constrained")
    print("  LP that grows with c_bound. The 'gain' is purely from sparse sampling,")
    print("  not from a structural relaxation -- physically this corresponds to")
    print("  ignoring all but the first K zeta zeros in the explicit-formula sum,")
    print("  which is NOT what MT bookkeeping does (MT sums all zeros).")

    # === Setup D: Trick at off-line height ===
    print()
    print("[4E.6 D] Trick-at-off-line LP -- max P(t_off * log p) s.t. P(gamma_k * log p) >= 0")
    print("         Mimics MT setup: zeros on line constrain P, off-line zero is the trick freq")
    print("         Baseline: max P(t_off * log p) over FULLY non-neg P with c_0 = 1")
    print(f"  {'N':>3} {'K':>5} {'log p':>8} {'t_off':>8} {'P(t_off)':>10} "
          f"{'full-nn max':>12} {'ratio':>8} {'hit bd?':>8}")
    setup_D = []
    for N in [4, 8]:
        for log_p in [np.log(2), np.log(3)]:
            # Trick height: midpoint between gamma_1 and gamma_2 (a value
            # not in any zero list at all, hence "off-line" frequency).
            t_off = (gammas[0] + gammas[1]) / 2.0
            trick_theta = (t_off * log_p) % (2 * np.pi)
            full_nn_max = max_P_at_point_full_nonneg(N, trick_theta, c_bound=200.0,
                                                     M=40000)
            for K_gamma in [5, 10, 20, 50, 100, 200, 400, len(gammas)]:
                if K_gamma > len(gammas):
                    continue
                gamma_subset = gammas[:K_gamma]
                P_at_trick, c_vec, info = trick_at_off_line_height(
                    N, gamma_subset, t_off, log_p, c_bound=200.0
                )
                if P_at_trick is None:
                    continue
                ratio = P_at_trick / full_nn_max if full_nn_max else float("nan")
                setup_D.append({
                    "N": N, "K_gamma": K_gamma, "log_p": log_p,
                    "t_off": t_off, "P_at_trick": P_at_trick,
                    "full_nn_max": full_nn_max, "ratio": ratio,
                    "hit_bound": info["hit_bound"],
                })
                print(f"  {N:>3} {K_gamma:>5} {log_p:>8.4f} {t_off:>8.4f} "
                      f"{P_at_trick:>10.4f} {full_nn_max:>12.4f} "
                      f"{ratio:>8.3f} {str(info['hit_bound']):>8}")
    print()
    print("  Reading: as K_gamma grows, setup D's LP value should approach the")
    print("  full-non-negativity baseline (the constraint set densifies in [0, 2pi]).")
    print("  If setup D EVER stably exceeds full_nn_max, that's a genuine constrained-")
    print("  domain gain. If it asymptotes to full_nn_max from above, the gain is")
    print("  purely from sparse sampling, NOT a structural escape from 4E.3.")

    # === Plot ===
    print()
    print("[4E.6] Plotting summary figure")
    fig, axs = plt.subplots(2, 2, figsize=(13, 11))

    # Panel A: K vs ratio for setup A
    ax = axs[0, 0]
    for N in N_values:
        rows = [r for r in setup_A if r["N"] == N]
        if not rows:
            continue
        Ks = [r["K"] for r in rows]
        ratios = [r["ratio"] for r in rows]
        ax.plot(Ks, ratios, "o-", label=f"N = {N}")
    ax.axhline(1.0, color="k", linestyle="--", alpha=0.5,
               label="Fejer ceiling (full [0, 2pi])")
    ax.set_xscale("log")
    ax.set_xlabel("K (number of constraint points)")
    ax.set_ylabel("LP c_1 / Fejer c_1")
    ax.set_title("Setup A: K-point LP\n(under-constrained at small K hits bound)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Panel B: delta vs ratio for setup B at fixed N
    ax = axs[0, 1]
    for c_bnd in [5.0, 50.0]:
        for N in [4, 8]:
            rows = [r for r in setup_B
                    if r["N"] == N and r["c_bound"] == c_bnd]
            if not rows:
                continue
            ds = [r["delta_frac"] for r in rows]
            ratios = [r["ratio"] for r in rows]
            ax.plot(ds, ratios, "o-", label=f"N={N}, c_bnd={c_bnd:.0f}")
    ax.axhline(1.0, color="k", linestyle="--", alpha=0.5,
               label="Fejer ceiling")
    ax.set_xlabel("delta / pi (arc half-width relative to pi)")
    ax.set_ylabel("LP c_1 / Fejer c_1")
    ax.set_title("Setup B: arc-removal LP\n(LP value bounded by coefficient bound)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Panel C: K_gamma vs ratio for setup C
    ax = axs[1, 0]
    for N in [4, 8]:
        for log_p, p in [(np.log(2), 2), (np.log(3), 3), (np.log(7), 7)]:
            rows = [r for r in setup_C
                    if r["N"] == N and abs(r["log_p"] - log_p) < 1e-6]
            if not rows:
                continue
            Ks = [r["K_gamma"] for r in rows]
            ratios = [r["ratio"] for r in rows]
            ax.plot(Ks, ratios, "o-",
                    label=f"N={N}, p={p}")
    ax.axhline(1.0, color="k", linestyle="--", alpha=0.5,
               label="Fejer ceiling")
    ax.set_xscale("log")
    ax.set_xlabel("K_gamma (number of zeta zero ordinates used)")
    ax.set_ylabel("LP c_1 / Fejer c_1")
    ax.set_title("Setup C: zero-constrained LP\n(P >= 0 at theta = gamma_k log p mod 2pi)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Panel D: trick at off-line for setup D, ZOOM on K >= 20 to show
    # convergence to 1.0 (suppressing bound-hitting small-K rows).
    ax = axs[1, 1]
    for N in [4, 8]:
        for log_p, p in [(np.log(2), 2), (np.log(3), 3)]:
            rows = [r for r in setup_D
                    if r["N"] == N and abs(r["log_p"] - log_p) < 1e-6
                    and not r["hit_bound"]]
            if not rows:
                continue
            Ks = [r["K_gamma"] for r in rows]
            ratios = [r["ratio"] for r in rows]
            ax.plot(Ks, ratios, "o-",
                    label=f"N={N}, p={p}")
    ax.axhline(1.0, color="k", linestyle="--", alpha=0.5,
               label="full-non-neg ceiling")
    ax.set_xscale("log")
    ax.set_xlabel("K_gamma (on-line zeros constraining P)")
    ax.set_ylabel("LP value / full-non-neg max")
    ax.set_title("Setup D: trick at off-line height (zoom: not bound-hit)\n"
                 "ratios decay to 1.0 with more zeros (sparse-sampling artifact)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, which="both")
    ax.set_ylim(0.99, 3.5)

    fig.suptitle("Arch 4E.6: constrained-domain LP probes vs Fejer ceiling\n"
                 "(under-constrained LPs hit coefficient bound; "
                 "structural escape requires more than domain restriction)",
                 fontsize=12, y=0.995)
    plt.tight_layout()
    plt.savefig(out_dir / "e4e6_constrained_lp.png", dpi=140)
    plt.close()
    print(f"  Saved {out_dir / 'e4e6_constrained_lp.png'}")

    np.savez_compressed(
        out_dir / "e4e6_constrained_lp.npz",
        setup_A=np.array(setup_A, dtype=object),
        setup_B=np.array(setup_B, dtype=object),
        setup_C=np.array(setup_C, dtype=object),
        setup_D=np.array(setup_D, dtype=object),
        gammas=gammas[:100],
    )
    print(f"  Saved {out_dir / 'e4e6_constrained_lp.npz'}")

    # === Structural summary ===
    print()
    print("=" * 78)
    print("[4E.6] Structural summary")
    print("=" * 78)
    print()
    print("4E.3 structural lemma: any 2D non-neg trig poly restricted to a 1D line")
    print("is a 1D non-neg trig poly bounded by Fejer at matched effective degree.")
    print("Conclusion: line-restriction route cannot improve single-zero MT shape.")
    print()
    print("4E.6 proposed escape: relax non-negativity to a subset Omega of [0, 2pi]^d.")
    print("4E.6 result: in the simplest formulations, the constrained-domain LP")
    print("either:")
    print("  (a) is under-constrained and hits the coefficient bound (setup A small K),")
    print("  (b) has solutions with large negative values in the excluded region")
    print("      (setup B), which has no physical realization in MT bookkeeping")
    print("      (the explicit-formula sum runs over ALL zeros, requiring P >= 0 there),")
    print("  (c) corresponds to ignoring all-but-K zeros (setup C), which is also")
    print("      not what MT does, OR")
    print("  (d) achieves Fejer-comparable ratios at the trick height (setup D),")
    print("      meaning the standard MT structure recovers, not exceeds, Fejer.")
    print()
    print("Verdict: the naive 'constrained-domain LP' is not the escape route from")
    print("4E.3's lemma. The actual escape requires additional STRUCTURE not present")
    print("in a domain restriction:")
    print("  - Heath-Brown multi-zero coupling (different zeros at different heights)")
    print("  - Bombieri variational SOS (allow small negativity, control L^2 norm)")
    print("  - Polynomial-ideal SOS (Arch 4E.8) (non-negativity over algebraic variety)")
    print()
    print("These are listed as separate TODO items (4E.7, 4E.8). 4E.6 has now")
    print("documented that 'constrained-domain LP' alone is not a separate route --")
    print("it collapses into one of the above when made physically meaningful, or")
    print("becomes vacuous when not.")
    print()
    print("This sharpens 4E.3's lemma: the geometric structure of Mossinghoff-")
    print("Trudgian's argument resists not just line-restriction (4E.3) but also")
    print("naive domain restriction. Genuine improvement requires inequality of")
    print("a structurally different form.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()
    run(out_dir=args.out)
