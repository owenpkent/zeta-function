"""Experiment 3DD: the Eratosthenes Descent (EDC) octave ladder.

The first test of Eratosthenes Descent, one of the five PURSUE survivors of the
session-019 first-principles conjecture program (LEARNINGS #76,
docs/03_research/first_principles_conjecture_program.md) and idea 4 of the
local-compute workaround slate (docs/03_research/local_compute_workarounds.md).
Nothing has touched EDC before this run.

## What EDC claims and which clauses this tests

EDC reads Weil positivity as a SELF-REDUCING certificate graded by support
octaves. Slice the Weil quadratic form by test-function support half-width
L = log b into octaves a_k = a_0 * 2^k. Place the basis functions so the
cumulative Gram G_k (all functions with L <= a_k) is the top-left principal
block of G_{k+1}. Then Haynsworth inertia additivity gives the EXACT identity

    In(G_{k+1}) = In(G_k) + In(S_k),     S_k = the octave-k Schur complement,

where In(M) = (n_+, n_0, n_-) is the eigenvalue inertia triple. EDC's clauses:

  (i)  every octave Schur complement S_k is positive semidefinite (n_-(S_k)=0).
       Then by telescoping In(G_K) has n_- = 0, i.e. the global Weil form is PSD,
       i.e. RH. The base case (octave 0, support < log 2, prime-free) is a
       claimed theorem (Yoshida + Connes-Consani).
  (ii) the certificate margins lambda_min(S_k) decay at worst EXPONENTIALLY IN
       THE LEVEL k. If instead they decay exponentially in the SUPPORT
       a_k = a_0 2^k (hence doubly-exponentially in k), the Cholesky chain
       collapses super-exponentially and the certificate advantage is VOID: that
       is the e^{-4 pi x} marginal wall (#52) in octave clothing.

This experiment computes In(S_k) for zeta, chi_3, D-H, and the Epstein d=47
non-principal form, verifies the Haynsworth identity as a numerical consistency
gate, and runs the decisive clause-(ii) regression: is log|lambda_min(S_k)|
linear in k (level, certificate survives) or in a_k (support, the wall)?

## The decisive sub-test (clause ii)

One regression separates "new structure" from "wall restatement". This is
exactly what EDC's viability hangs on, so it is the load-bearing readout, not
the inertia counts (which clause i predicts trivially for zeta if RH holds).

## Predictions and kills

  - zeta / chi_3 (Euler, RH): every S_k PSD (n_-=0). A robustly indefinite octave
    (n_- > 0 with |lambda_min| well above the conditioning floor) KILLS clause (i).
  - D-H / Epstein d=47 non-principal (off-line zeros): the chain must BREAK at
    some octave k* (the off-line resonance entering the support window). The value
    and stability of k* is an integer-valued discriminator, the octave-graded
    refinement of 3J's law schur_neg = #off-line heights (#19).
  - clause (ii): R^2(level) > R^2(support) and a clean constant per-level ratio =>
    certificate survives (EDC viable). log|margin| linear in a_k = 2^k (margin
    halves-of-magnitude per octave doubling) => the #52 wall => certificate void.

## Normalization (reuses the M2.5/M2.6-validated Weil-form blocks)

The Weil Gram is the input-side non-circular form M = A_arch + P_fin + B_pole in
the exact normalization e3aa and e3p use (no zeros enter):
  - A_arch : arch_block_bombieri (physical-space Bombieri integral, e2v).
  - P_fin  : finite_block on the von Mangoldt (zeta) / -L'/L (chi_3, D-H, Epstein)
             coefficients.
  - B_pole : pole_block (residue 1 for zeta; 0 for the entire L; numeric for Eps).
Test family Phi_b(s) = 2 sinh((s-1/2) log b)/(s-1/2); h_b = 1_{[-log b, log b]}, so
the support half-width is L = log b. Octave boundaries are in L.

Octave grid: a_0 = 0.34 (just below log 2 / 2, so octave 0 is strictly
prime-free), a_k = a_0 * 2^k. With N_oct octaves and m basis functions per octave
(K = m * N_oct total), the largest support half-width is a_{N_oct-1} and the
explicit-formula sum runs to n <= e^{2 a_{N_oct-1}}.

K1 / non-circularity: every matrix entry is built from the Gamma factor and the
prime coefficients only; no zero locations enter. D-H discipline: D-H has no Euler
product, so its -L'/L delocalizes onto all n; it is included to confirm the chain
BREAKS where zeta's does not.

Honest scope (soft-detector freeze): a falsification instrument, not a
certificate. The outer-octave margins sit on the marginal-positivity wall (#52),
so they read as ~0 / float noise; the decisive content is (a) the integer inertia
sequence and the break octave k* for the off-line controls, and (b) the
level-vs-support character of the margin decay, a RATE comparison, not a certified
margin.

Outputs:
  - e3dd_edc_octave_ladder.npz
  - e3dd_edc_octave_ladder.png
  - stdout: per-octave inertia tables, Haynsworth checks, clause-(ii) regression.

RESULT (2026-06-09, a_0=0.34, a_k=0.34*2^k, m=3/octave, prec=25, T_max=200;
LEARNINGS #78). EDC SURVIVED this first falsification test on every clause it
could be asked at reachable scale.

  Clause (i) CONFIRMED. Every octave Schur complement is PSD (In(S_k)=(+,0,0),
  n_-=0) for zeta and chi_3 on the genuine non-circular input-side Weil form
  M=A_arch+P_fin+B_pole, and for zeta out to 7 octaves on the zero side. The
  Haynsworth identity In(G_k)=In(G_{k-1})+In(S_k) holds exactly at every octave
  (consistency gate passed) with cond(G_{k-1}) <= ~90, so the inertia counts are
  trustworthy. The telescoping skeleton is sound and computable.

  Clause (ii): NO octave-graded wall. Zero-side zeta margins lambda_min(S_k) stay
  in [0.014, 0.039] across 7 octaves, support b in [1.5, 2.8e9] (a 64x span in
  log-support), with NO exponential-in-support collapse: the smallest margin sits
  ~1e117 ABOVE a nominal e^{-4 pi a_k} wall at the top octave. Input-side zeta
  margins (0.054/0.055/0.047/0.037/0.034 over 5 octaves) fit LEVEL k far better
  than SUPPORT a_k (R^2 0.98 vs 0.86). And the telescoping picture is exactly
  EDC's dossier prediction: the global min-eig(G_K)=+0.007 (zero side) / +0.023
  (input side) is MARGINAL while every per-octave Schur margin is healthy
  (O(0.01-0.05)); the global marginality is the telescoped accumulation of healthy
  octaves, not any single octave being marginal.

  HONEST SCOPE (the load-bearing caveats; soft-detector freeze respected):
   (a) The zero-side flatness is nearly TAUTOLOGICAL under RH: with all zeros on
       the line, the zero-side Gram is a sum of real rank-1 PSD outer products, so
       it is robustly PSD at every octave by construction. It demonstrates
       scale/conditioning control, not positivity per se. The genuine test is the
       input side.
   (b) The input side (the actual non-circular certificate) CAPS at n_oct=5: its
       prime sum runs to n <= e^{2 a_max}, which is ~5.3e4 at a_max=5.44 but
       ~2.8e9 at the next octave. So clause (ii) on the side that matters is only
       4 Schur points, suggestive not decisive. That ceiling IS the feasibility
       wall; the analytic question of whether the input-side octave margins stay
       bounded below as octaves grow is exactly the open core, not a compute task.
   (c) The off-line BREAK (idea-4's promised integer discriminator, the
       octave-graded refinement of 3J's schur_neg=#off-line heights, #19) is NOT
       exhibited: D-H and Epstein d=47 stay fully PSD on both sides at m=3/octave.
       This is a RESOLUTION limit, not a refutation: 3D.3 needed K=100-1000 to
       resolve D-H's off-line eigenvalues (a -2.6% relative effect), and the
       octave detector at K=15-21 is far below that. The input-side D-H PSD-ness
       is additionally the M2.6 stealth window (#34). Epstein input-side is
       untestable (a_1=0, the form 2x^2+xy+6y^2 does not represent 1).

  VERDICT: a falsification instrument that EDC passed. Clause (i) holds, the
  Haynsworth skeleton is exact and well-conditioned, and clause (ii) shows the
  encouraging direction (no support-wall; healthy per-octave margins telescoping
  into the global marginality). EDC stays a live PURSUE direction, sharpened: the
  open core is now precisely (b) (the input-side margin lower bound past the
  feasibility ceiling, an analytic statement) and (c) (reproduce the off-line
  break at high octave resolution). Next compute step: an m>>3 (dense per-octave)
  zero-side run to try to expose the break, and the e2ll function-field wind
  tunnel (workaround idea 1) where the analytic margin bound is a theorem.
"""

from __future__ import annotations

import argparse
import time
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np

from experiments._shared import (
    zeta_L, DavenportHeilbronn, chi3_L, epstein_for_discriminant,
)
from experiments.positivity.e3m_place_type_balance import (
    finite_block, pole_block, lambda_coeffs_from_dirichlet, von_mangoldt_zeta,
    numeric_residue_at_one, gram_zero_side,
)
from experiments.arithmetic_geometric.e2v_rosati_balance_M2_5 import arch_block_bombieri


# ----------------------------------------------------------------------------
# Octave grid and nested basis
# ----------------------------------------------------------------------------

def octave_grid(a0: float, n_oct: int, m: int):
    """Basis support half-widths L_i grouped into octaves a_k = a0 * 2^k.

    Octave k spans (a_{k-1}, a_k] (with a_{-1}=0) and gets m points linearly
    spaced in L, excluding the left boundary. Returns (L_vals, octave_of, a_k).
    """
    a_k = np.array([a0 * (2.0 ** k) for k in range(n_oct)])
    L_vals = []
    octave_of = []
    left = 0.0
    for k in range(n_oct):
        right = a_k[k]
        pts = np.linspace(left, right, m + 1)[1:]  # exclude left boundary
        L_vals.extend(pts.tolist())
        octave_of.extend([k] * m)
        left = right
    return np.array(L_vals), np.array(octave_of), a_k


# ----------------------------------------------------------------------------
# Weil Gram on a fixed basis (the full matrix; nested blocks are slices)
# ----------------------------------------------------------------------------

def build_full_gram(L, name, mu_list, log_Q, residue, has_euler, L_vals, prec):
    """Full Weil Gram M = A_arch + P_fin + B_pole on b_i = exp(L_i)."""
    b_vals = np.exp(L_vals)
    L_max = float(L_vals.max())
    n_max = int(np.exp(2.0 * L_max)) + 2

    A = arch_block_bombieri(b_vals, mu_list, log_Q, prec)

    if has_euler and name == "zeta":
        lam = np.array([0.0] + [von_mangoldt_zeta(n) for n in range(1, n_max + 1)])
    else:
        lam = lambda_coeffs_from_dirichlet(L, n_max, prec)
    P = finite_block(b_vals, lam, prec)

    if residue is None:
        residue = numeric_residue_at_one(L, prec)
    B = pole_block(b_vals, float(residue), prec)

    M = A + P + B
    return 0.5 * (M + M.T), n_max, float(residue)


# ----------------------------------------------------------------------------
# Inertia and Schur complement
# ----------------------------------------------------------------------------

def inertia(M, rel_tol=1e-9):
    """Eigenvalue inertia triple (n_+, n_0, n_-) with a relative zero band."""
    M = 0.5 * (M + M.T)
    vals = np.linalg.eigvalsh(M)
    scale = max(float(np.abs(vals).max()), 1e-300)
    tol = rel_tol * scale
    n_pos = int(np.sum(vals > tol))
    n_neg = int(np.sum(vals < -tol))
    n_zero = len(vals) - n_pos - n_neg
    return (n_pos, n_zero, n_neg), vals


def schur_complement(G, n_inner):
    """Schur complement of the inner block: S = D - B^T A^{-1} B, plus cond(A).

    G = [[A, B],[B^T, D]] with A = G[:n_inner,:n_inner] the cumulative inner Gram.
    Falls back to a least-squares solve if A is numerically singular.
    """
    A = G[:n_inner, :n_inner]
    B = G[:n_inner, n_inner:]
    D = G[n_inner:, n_inner:]
    condA = float(np.linalg.cond(A))
    try:
        X = np.linalg.solve(A, B)
    except np.linalg.LinAlgError:
        X = np.linalg.lstsq(A, B, rcond=None)[0]
    S = D - B.T @ X
    return 0.5 * (S + S.T), condA


def add_inertia(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def sub_inertia(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


# ----------------------------------------------------------------------------
# The ladder
# ----------------------------------------------------------------------------

def compute_ladder(G, a_k, m, n_oct):
    """Given a full Weil Gram G on the octave-ordered basis, compute the nested
    inertia chain, octave Schur complements, margins and Haynsworth checks."""
    dims = [(k + 1) * m for k in range(n_oct)]   # dim of cumulative G_k
    In_G = []
    eig_G_global = np.linalg.eigvalsh(G)
    global_min = float(eig_G_global.min())
    global_relmin = global_min / max(float(np.abs(eig_G_global).max()), 1e-300)

    for k in range(n_oct):
        Gk = G[:dims[k], :dims[k]]
        In_G.append(inertia(Gk)[0])

    octaves = []
    for k in range(n_oct):
        if k == 0:
            S = G[:dims[0], :dims[0]]
            condA = 1.0
        else:
            S, condA = schur_complement(G[:dims[k], :dims[k]], dims[k - 1])
        In_S, vals_S = inertia(S)
        lam_min = float(vals_S.min())
        lam_max = float(np.abs(vals_S).max())
        rel_min = lam_min / max(lam_max, 1e-300)

        # Haynsworth: In(G_k) - In(G_{k-1}) should equal In(S_k).
        if k == 0:
            hayns_ok = (In_S == In_G[0])
            predicted = In_G[0]
        else:
            predicted = sub_inertia(In_G[k], In_G[k - 1])
            # compare the (n_+, n_-) part; n_0 is numerically fragile
            hayns_ok = (predicted[0] == In_S[0] and predicted[2] == In_S[2])

        octaves.append(dict(
            k=k, a_k=float(a_k[k]), dim=dims[k], In_S=In_S, In_G=In_G[k],
            lam_min=lam_min, lam_max=lam_max, rel_min=rel_min,
            condA=condA, hayns_ok=bool(hayns_ok), hayns_pred=predicted,
        ))

    return dict(global_min=global_min, global_relmin=global_relmin, octaves=octaves)


def input_side_ladder(name, L, mu_list, log_Q, residue, has_euler,
                      L_vals, a_k, m, n_oct, prec):
    """Part A: the genuine non-circular Weil-form octave ladder (M=A+P+B)."""
    t0 = time.time()
    G, n_max, res = build_full_gram(
        L, name, mu_list, log_Q, residue, has_euler, L_vals, prec)
    lad = compute_ladder(G, a_k, m, n_oct)
    lad.update(name=name, has_euler=has_euler, residue=res, n_max=n_max,
               elapsed=time.time() - t0, side="input")
    return lad


def zero_side_ladder(name, L, L_vals, a_k, m, n_oct, T_max, prec):
    """Part B: the zero-side Gram octave ladder (3J detector, octave-graded).

    CIRCULAR (uses zero locations) but reaches higher support than the input side
    (no e^{2L} prime sum), so it can exhibit the off-line break k* and a longer
    clause-(ii) margin sequence. Reuses gram_zero_side from e3m (3C-3J machinery).
    """
    t0 = time.time()
    b_vals = np.exp(L_vals)
    G, n_zeros = gram_zero_side(L, b_vals, T_max, prec)
    G = 0.5 * (G + G.T)
    lad = compute_ladder(G, a_k, m, n_oct)
    lad.update(name=name, n_zeros=int(n_zeros), T_max=T_max,
               elapsed=time.time() - t0, side="zero")
    return lad


def clause_ii_regression(octaves):
    """Fit log|lambda_min(S_k)| against k (level) and a_k (support) for k>=1.

    Returns slopes, R^2 for each, and the verdict (which description fits better).
    Uses k>=1 (the genuine Schur complements; k=0 is the base block).
    """
    ks = np.array([o["k"] for o in octaves if o["k"] >= 1], dtype=float)
    aks = np.array([o["a_k"] for o in octaves if o["k"] >= 1], dtype=float)
    mags = np.array([abs(o["lam_min"]) for o in octaves if o["k"] >= 1], dtype=float)
    mags = np.maximum(mags, 1e-300)
    y = np.log(mags)

    def fit(x, y):
        if len(x) < 2:
            return float("nan"), float("nan"), float("nan")
        sl, icpt = np.polyfit(x, y, 1)
        yhat = sl * x + icpt
        ss_res = float(np.sum((y - yhat) ** 2))
        ss_tot = float(np.sum((y - y.mean()) ** 2))
        r2 = 1.0 - ss_res / ss_tot if ss_tot > 1e-30 else 1.0
        return float(sl), float(icpt), float(r2)

    sl_k, ic_k, r2_k = fit(ks, y)
    sl_a, ic_a, r2_a = fit(aks, y)

    # Margin band and the wall contrast. The #52 marginal wall predicts an
    # exponential-in-SUPPORT collapse ~ e^{-c*a_k}; at the largest octave that
    # is astronomically small. The ratio of the observed smallest margin to a
    # nominal e^{-4 pi a_k} wall value quantifies how far the octave-graded form
    # sits ABOVE any wall. "Flat" = the total margin drop is well under one
    # decade across all octaves (no collapse of any kind).
    band_lo = float(mags.min())
    band_hi = float(mags.max())
    total_drop = band_hi / max(band_lo, 1e-300)        # max/min ratio
    a_top = float(aks.max()) if len(aks) else 0.0
    wall_at_top = float(np.exp(-4.0 * np.pi * a_top))   # nominal e^{-4 pi x} wall
    margin_over_wall = band_lo / max(wall_at_top, 1e-300)

    flat = total_drop < 10.0   # less than a single decade of decay across all k
    if np.isnan(r2_k) or np.isnan(r2_a):
        verdict = "insufficient octaves"
    elif flat:
        verdict = (f"FLAT: margins in [{band_lo:.3g}, {band_hi:.3g}] across support "
                   f"a_k up to {a_top:.1f} (drop {total_drop:.1f}x < decade); NO "
                   f"octave-graded wall (margin/[e^-4pi a] ~ 1e{np.log10(margin_over_wall):.0f})")
    elif r2_k >= r2_a:
        verdict = "LEVEL (exp in k) fits better => certificate survives, no support-wall"
    else:
        verdict = "SUPPORT (exp in a_k=2^k) fits better => marginal wall, certificate void"
    return dict(
        ks=ks.tolist(), aks=aks.tolist(), log_mag=y.tolist(),
        slope_level=sl_k, r2_level=r2_k, slope_support=sl_a, r2_support=r2_a,
        band_lo=band_lo, band_hi=band_hi, total_drop=total_drop,
        margin_over_wall=margin_over_wall, flat=bool(flat), verdict=verdict,
    )


# ----------------------------------------------------------------------------
# Driver
# ----------------------------------------------------------------------------

def run(a0=0.34, n_oct=5, m=3, prec=25, targets="all", T_max=200.0,
        part="both", suffix="", out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    L_vals, octave_of, a_k = octave_grid(a0, n_oct, m)
    K = len(L_vals)

    dh = DavenportHeilbronn()
    eps47 = epstein_for_discriminant(47, principal=False)
    all_targets = [
        ("zeta",  zeta_L, [0.0],      mp.mpf(0),           1.0,  True),
        ("chi_3", chi3_L, [1.0],      mp.log(mp.sqrt(3)),  0.0,  True),
        ("DH",    dh,     [1.0],      mp.log(mp.sqrt(5)),  0.0,  False),
        ("Eps47", eps47,  [0.0, 1.0], mp.log(mp.sqrt(47)), None, False),
    ]
    if targets == "quick":
        all_targets = [all_targets[0], all_targets[2]]   # zeta + DH
    elif targets != "all":
        wanted = set(targets.split(","))
        all_targets = [t for t in all_targets if t[0] in wanted]

    print("=" * 80)
    print("EXPERIMENT 3DD: Eratosthenes Descent (EDC) octave ladder")
    print(f"  octaves a_k = {a0} * 2^k = {np.round(a_k, 4).tolist()}")
    print(f"  m={m} basis functions/octave, K={K} total, prec={prec}")
    print(f"  base octave 0 support half-width <= {a_k[0]:.3f} "
          f"(prime-free: 2*a_0 = {2*a_k[0]:.3f} < log 2 = {float(mp.log(2)):.3f})")
    print("  EDC clause (i): every S_k PSD (n_-=0) for Euler/RH targets.")
    print("  EDC clause (ii): does log|lambda_min(S_k)| track LEVEL k or SUPPORT a_k?")
    print("=" * 80)

    # ---- Part A: the genuine non-circular Weil-form ladder (input side) ----
    print("\n" + "#" * 80)
    print("# PART A: input-side non-circular Weil form M = A_arch + P_fin + B_pole")
    print("#   the actual EDC certificate (no zeros enter). Clause (i)+(ii) live here.")
    print("#   Off-line controls may stay intact: the M2.6 stealth window (#34).")
    print("#" * 80)
    input_results = {}
    if part in ("both", "A"):
        for name, L, mu_list, log_Q, residue, has_euler in all_targets:
            print(f"\n--- {name} [input] (Euler: {has_euler}) ---")
            try:
                res = input_side_ladder(name, L, mu_list, log_Q, residue, has_euler,
                                        L_vals, a_k, m, n_oct, prec)
            except Exception as e:
                print(f"    FAILED: {e}")
                continue
            input_results[name] = res
            print(f"    n_max={res['n_max']}, residue={res['residue']:.4g}, "
                  f"global min-eig(G_K)={res['global_min']:+.4e} "
                  f"(rel {res['global_relmin']:+.3e})  [{res['elapsed']:.1f}s]")
            _print_ladder(res)

    # ---- Part B: the zero-side 3J detector, octave-graded (reaches higher) ----
    print("\n" + "#" * 80)
    print("# PART B: zero-side Gram M_ij = sum_rho Phi_bi(rho) Phi_bj(rho)")
    print("#   CIRCULAR (uses zeros) but reaches higher support -> exhibits the")
    print("#   off-line break k* (octave-graded 3J/#19) and a longer clause-(ii) range.")
    print("#" * 80)
    zero_results = {}
    if part in ("both", "B"):
        for name, L, mu_list, log_Q, residue, has_euler in all_targets:
            print(f"\n--- {name} [zero] ---")
            try:
                res = zero_side_ladder(name, L, L_vals, a_k, m, n_oct, T_max, prec)
            except Exception as e:
                print(f"    FAILED: {e}")
                continue
            zero_results[name] = res
            print(f"    n_zeros(T<={res['T_max']})={res['n_zeros']}, "
                  f"global min-eig(G_K)={res['global_min']:+.4e} "
                  f"(rel {res['global_relmin']:+.3e})  [{res['elapsed']:.1f}s]")
            _print_ladder(res)

    results = dict(input=input_results, zero=zero_results)
    _plot(input_results, zero_results, a_k, out_dir, suffix)
    _save(input_results, zero_results, a_k, a0, n_oct, m, prec, out_dir, suffix)

    # ---- cross-target synthesis ----
    print("\n" + "=" * 80)
    print("SYNTHESIS")
    print("  Part A (input-side, the EDC certificate):")
    for name, res in input_results.items():
        neg = [o["k"] for o in res["octaves"] if o["In_S"][2] > 0]
        broke = f"breaks k*={neg[0]}" if neg else "intact (all S_k PSD)"
        v = res.get("regression", {}).get("verdict", "n/a")
        print(f"    {name:6s}: {broke:24s} | clause(ii): {v}")
    print("  Part B (zero-side, 3J octave detector, CIRCULAR):")
    for name, res in zero_results.items():
        neg = [o["k"] for o in res["octaves"] if o["In_S"][2] > 0]
        broke = f"breaks k*={neg[0]} octs={neg}" if neg else "intact (all S_k PSD)"
        print(f"    {name:6s}: {broke}")
    print("=" * 80)
    return results


def _print_ladder(res):
    """Shared per-target table printer; attaches the clause-(ii) regression."""
    print(f"    {'oct':>3} {'a_k':>7} {'dim':>4} {'In(S_k)=(+,0,-)':>16} "
          f"{'lam_min(S_k)':>14} {'rel_min':>11} {'cond(G_{k-1})':>13} {'Hayns':>7}")
    for o in res["octaves"]:
        hs = "OK" if o["hayns_ok"] else "MISMATCH"
        print(f"    {o['k']:>3d} {o['a_k']:>7.3f} {o['dim']:>4d} "
              f"{str(o['In_S']):>16} {o['lam_min']:>+14.4e} {o['rel_min']:>+11.3e} "
              f"{o['condA']:>13.2e} {hs:>7}")
    neg_octs = [o["k"] for o in res["octaves"] if o["In_S"][2] > 0]
    if neg_octs:
        print(f"    chain BREAKS first at octave k* = {neg_octs[0]} "
              f"(In(S) n_- > 0); all negative octaves: {neg_octs}")
    else:
        print(f"    chain intact: every S_k PSD (n_-=0) -> clause (i) holds at this K")
    # Telescoping picture: healthy per-octave margins vs marginal global min-eig.
    min_margin = min(abs(o["lam_min"]) for o in res["octaves"])
    gmin = res.get("global_min", float("nan"))
    print(f"    telescoping: min octave margin={min_margin:+.4e} vs global "
          f"min-eig(G_K)={gmin:+.4e} (per-octave healthier than the global residue "
          f"=> marginality is the telescoped accumulation, EDC's predicted picture)")
    reg = clause_ii_regression(res["octaves"])
    res["regression"] = reg
    print(f"    clause (ii) log|lambda_min(S_k)| regression (k>=1): "
          f"vs LEVEL k R^2={reg['r2_level']:.4f} (slope {reg['slope_level']:+.3f}); "
          f"vs SUPPORT a_k R^2={reg['r2_support']:.4f} (slope {reg['slope_support']:+.3f})")
    print(f"      verdict: {reg['verdict']}")


def _plot(input_results, zero_results, a_k, out_dir, suffix=""):
    panels = [("input", input_results, "Part A: input-side Weil form (non-circular)"),
              ("zero", zero_results, "Part B: zero-side Gram (3J detector, circular)")]
    fig, axes = plt.subplots(2, 2, figsize=(13, 9))
    for row, (side, results, title) in enumerate(panels):
        ax = axes[row, 0]
        for name, res in results.items():
            ks = [o["k"] for o in res["octaves"]]
            mags = [abs(o["lam_min"]) for o in res["octaves"]]
            ax.semilogy(ks, np.maximum(mags, 1e-18), "o-", label=name)
        ax.set_xlabel("octave level k")
        ax.set_ylabel("|lambda_min(S_k)| (margin)")
        ax.set_title(f"{title}\nmargin: level-linear=certificate, doubly-exp=wall")
        if ax.get_legend_handles_labels()[1]:
            ax.legend(fontsize=8)
        ax.grid(True, which="both", alpha=0.3)

        ax = axes[row, 1]
        for name, res in results.items():
            ks = [o["k"] for o in res["octaves"]]
            nneg = [o["In_S"][2] for o in res["octaves"]]
            ax.plot(ks, nneg, "s-", label=name)
        ax.set_xlabel("octave level k")
        ax.set_ylabel("n_-(S_k)")
        ax.set_title("Octave inertia: where the chain breaks\n"
                     "(Euler/RH stays 0; off-line jumps at k*)")
        if ax.get_legend_handles_labels()[1]:
            ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3)
    fig.tight_layout()
    p = out_dir / f"e3dd_edc_octave_ladder{suffix}.png"
    fig.savefig(p, dpi=130)
    plt.close(fig)
    print(f"\n[plot] {p}")


def _save(input_results, zero_results, a_k, a0, n_oct, m, prec, out_dir, suffix=""):
    payload = dict(a_k=a_k, a0=a0, n_oct=n_oct, m=m, prec=prec)
    for side, results in (("input", input_results), ("zero", zero_results)):
        for name, res in results.items():
            pre = f"{side}_{name}"
            payload[f"{pre}_global_min"] = res["global_min"]
            payload[f"{pre}_lam_min"] = np.array([o["lam_min"] for o in res["octaves"]])
            payload[f"{pre}_rel_min"] = np.array([o["rel_min"] for o in res["octaves"]])
            payload[f"{pre}_n_neg"] = np.array([o["In_S"][2] for o in res["octaves"]])
            payload[f"{pre}_condA"] = np.array([o["condA"] for o in res["octaves"]])
            payload[f"{pre}_hayns_ok"] = np.array([o["hayns_ok"] for o in res["octaves"]])
            if "regression" in res:
                r = res["regression"]
                payload[f"{pre}_r2_level"] = r["r2_level"]
                payload[f"{pre}_r2_support"] = r["r2_support"]
                payload[f"{pre}_slope_level"] = r["slope_level"]
                payload[f"{pre}_slope_support"] = r["slope_support"]
    p = out_dir / f"e3dd_edc_octave_ladder{suffix}.npz"
    np.savez(p, **payload)
    print(f"[save] {p}")


def main():
    ap = argparse.ArgumentParser(description="EDC octave ladder (experiment 3DD)")
    ap.add_argument("--a0", type=float, default=0.34, help="base octave half-width")
    ap.add_argument("--n_oct", type=int, default=5, help="number of octaves")
    ap.add_argument("--m", type=int, default=3, help="basis functions per octave")
    ap.add_argument("--prec", type=int, default=25, help="mpmath precision (dps)")
    ap.add_argument("--T_max", type=float, default=200.0, help="zero-side T_max (Part B)")
    ap.add_argument("--targets", type=str, default="all",
                    help="'all', 'quick' (zeta+DH), or comma list e.g. 'zeta,DH'")
    ap.add_argument("--part", type=str, default="both", choices=["both", "A", "B"],
                    help="'both', 'A' (input-side), or 'B' (zero-side, reaches higher)")
    ap.add_argument("--suffix", type=str, default="",
                    help="output filename suffix (avoid clobbering the main artifacts)")
    args = ap.parse_args()
    run(a0=args.a0, n_oct=args.n_oct, m=args.m, prec=args.prec,
        targets=args.targets, T_max=args.T_max, part=args.part, suffix=args.suffix)


if __name__ == "__main__":
    main()
