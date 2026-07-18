"""E1Q: the theta/Poisson wrap-collapse rung -- the form-side S4 probe,
the form-side half of the post-corridor pivot.

WHY THIS EXPERIMENT EXISTS
==========================
The CCM corridor closed as a proof home on 2026-07-17 (LEARNINGS #163/#164).
docs/03_research/ccm_corridor_frame_audit.md named the next move explicitly:
e1m proved the Hamburger pin's proof engine IS Poisson/theta duality, and
that construction pays the #152 lattice clause BY CONSTRUCTION, so the S4
spec's identity clause (docs/03_research/s4_carrier_audit.md Section 4 item
5 / e1o_s4_carrier.md Q4) should next be attempted on the theta/modular-
interpolation side rather than re-entering the closed CCM Sonin space. This
probe is that attempt, built per docs/03_research/theta_s4_build_spec.md.

THE OBJECT
==========
A finite Poisson-summation (Jacobi-theta) kernel: the periodized (wrapped)
Gaussian on a window of period L(lambda) = 2 log(lambda) (e1o's own carrier
convention, horizon p <= lambda^2 <=> log p <= L):
    Theta_t^L(y) = sum_{n=-Nwrap}^{Nwrap} exp(-pi (y - n L)^2 / t)
This is the direct period-L rescaling of e1m's own T1b shifted-Poisson
identity (verified there to <1e-25, measured ~1.5e-36), with dual (Poisson)
representation
    Theta_t^L(y) = (sqrt(t)/L) sum_k exp(-pi k^2 t / L^2) cos(2 pi k y / L).
Gram matrices G_jk(t) = Theta_t^L(x_j - x_k) on X_lambda = {log p : p <=
lambda^2} are compared against the wrap-free control G0_jk(t) = exp(-pi
(x_j-x_k)^2/t) (the n=0 term alone, a generic Gaussian kernel carrying no
lattice input): G - G0 is the part attributable specifically to the
periodization sum sum_{n != 0}, i.e. specifically to the additive lattice
L*Z. This isolates the lattice-sourced wrap term from dimension-generic
kernel smoothness, per the S4 spec's condition (2) (cheap multiplicity: a
lambda-uniform, well-conditioned rank collapse of the evaluation matrix at
{k log p}).

WHAT THIS BUILDS (test battery)
================================
PHASE 0 THE ANCHOR: re-verify the rescaled dual identity to e1m's own T1a/
   T1b tolerance class (<1e-25) at each tested lambda, at (y,t) pairs
   rescaled directly from e1m's own tested (x,t) pairs, with Nwrap=Kwrap=80
   fixed (matching e1m's own truncation). Both sides of the wrap sum
   converge comfortably at N=K=80 whenever t/L^2 stays in the O(0.3-2)
   range e1m actually tested (the "self-dual" balance point is t/L^2=1,
   where primal and dual decay at the identical rate e^{-pi n^2}); this is
   why Phase 0 is anchored there rather than at Phase 1's extreme small-t
   cells (see the comment above theta_primal_mp/theta_dual_mp below, and
   the companion .md's closing deviations section, for the full reasoning:
   at Phase 1's smallest t, the DUAL sum alone would need Kwrap in the
   hundreds to hit 1e-25, breaking the <=80 cap, while the PRIMAL form
   used for the actual Gram matrices stays safe at Nwrap=80 across the
   entire Phase-1 range because t <= L^2 there always).
PHASE 1 THE COLLAPSE TEST (the S4 question itself), zeta side: for each
   lambda in {2.2, 3.0, sqrt(13), 6.0} and t swept geometrically from the
   minimum pairwise gap^2 in X_lambda up to L(lambda)^2 (9 points),
   numeric rank of G(t) and G0(t) at e1o's own T4c threshold convention
   (relative singular value > 1e-8), rho = rank(G)/M, rho0 = rank(G0)/M,
   Delta_rho = rho0 - rho, plus the conditioning pair (sigma_r/sigma_1,
   sigma_{r+1}/sigma_1) at the declared rank r of G(t) (e1o's own
   "min sv" discipline, built to catch the superresolution mirage e1o's
   own adversary round already found once in a near-commensurate
   decimation family).
PHASE 2 THE DISCIPLINES, in the same run: (a) the Beurling twin's node set
   X_lambda^B through the IDENTICAL true kernel, at matched (lambda,t)
   cells (the e1o-T3-style twin: same code, different input); (b) the
   fake's OWN wrap-sum/dual identity (Z replaced by BeurlingSystem's
   generalized integers: the direct analogue of e1m's T5a, reproducing
   its construction verbatim, predicted defect order 0.1-1 by direct
   analogy to T5's measured 0.37); (c) D-H, cited unposable (AX-FORM: no
   Euler product means no privileged prime-power sublattice to test the
   kernel against; type exclusion: e1m's T2 conductor mismatch), no new
   D-H computation; (d) K1: source scan + runtime guards on the zero
   scanners (installed, never tripped) + the consume() ledger.

GRADING (spec Section (d), four tiers)
=======================================
1 LATTICE-GENUINE COLLAPSE: wrap-attributable (Delta_rho>=0.1) AND
  well-conditioned (genuine sv gap, not a smooth tail) AND lambda-uniform
  (non-shrinking across the two largest lambda) AND Beurling-separating
  (twin's Delta_rho <= half of zeta's at matched cells). All four required.
2 MEASURED BUT PARTIAL: a gap clears some but not all four.
3 BLIND / MIRAGE / FAIL: no gap anywhere, or a gap that fails the
  conditioning gate, or Phase 0 fails to generalize to L(lambda).
4 SYSTEM-GENERIC: a gap that clears conditioning + uniformity but
  reproduces at matched strength on the Beurling twin (the DMV-kill trap,
  a distinct failure mode from 3, tested only in Phase 2). Reported even
  though it is nominally a "positive" rank result.

RESULT (measured, full run, 25/25 self-tests post-ADVERSARY;
        16/16 at the original BUILDER pass, see _e1q_adversary.md)
==============================================
Phase 0 PASSED cleanly: the rescaled dual identity holds to worst-case
relative defect ~1.5e-36 at every tested lambda (Nwrap=Kwrap=80), the same
tolerance class as e1m's own T1a/T1b. [ADVERSARY, precision-floor note: the
~1e-36 figure is the mp.mp.dps=35 WORKING-PRECISION rounding floor, not the
identity's true mathematical tightness -- re-run at dps=50/80/120 the
measured defect drops to ~1e-51/1e-81/1e-121 (scaling linearly with dps),
while the Nwrap=Kwrap=80 TRUNCATION error alone is independently bounded at
~1e-8952 (see theta_wrap_np's docstring). The identity is not merely
"verified to 1e-36"; it is verified to whatever precision one chooses to
spend, the quoted number is a precision-budget choice (matching e1m's own
dps=35), not a ceiling on the identity's accuracy. This does not change the
Phase 0 pass/fail (either reading clears the 1e-25 bar by many orders of
magnitude).] Phase 1 landed on the PRE-REGISTERED
WALL, tier 3 (MIRAGE), not tier 3's plainer BLIND sub-case: three cells (at
the two largest tested lambda, sqrt(13) and 6.0, all at the top of the t
sweep near L^2) show a raw Delta_rho up to 0.182, but every one fails the
conditioning gate outright (sig_r ~ 1e-6 to 1e-8, three to six orders of
magnitude below the 1e-3 bar). [ADVERSARY, mirage grading, Attack 2 --
corrected characterization: a plot-free consecutive-singular-value-ratio
audit (P1g) at ALL THREE flagged cells, not just the one the original text
showed, finds the ratio sv[r]/sv[r-1] AT the declared-rank boundary is 3+
orders of magnitude below the MEDIAN consecutive ratio elsewhere in the
same spectrum at every one of the three cells: i.e. there IS a
disproportionate step exactly at the boundary in all three cases, not
"smooth monotone decay with no clean gap" as originally and imprecisely
stated. This does not change the verdict: the step is between two already-
negligible values (sig_r itself is only 1.7e-6 to 9.9e-6 relative to the
top singular value, still three to six orders of magnitude below the 1e-3
floor), so it is a boundary between noise and deeper noise, not signal
falling off a cliff into noise. This is exactly the behavior expected of a
Gaussian/RBF kernel's well-known super-exponential eigenvalue decay, which
can show a locally sharp RATIO step at essentially any index purely from
smoothness, with no arithmetic content -- which is precisely why
is_discovery_candidate gates on the ABSOLUTE scale of sig_r (>1e-3) and not
on local spectral shape: shape alone cannot distinguish a genuine
structural collapse from generic smooth-kernel tail behavior.] Confirming
this is the
same conditioning mirage e1o's own adversary round caught once already in
a near-commensurate decimation family, not a structural rank drop. Phase 2
reinforces the mirage reading rather than complicating it: the Beurling
twin shows a comparably sized (if anything slightly larger, 0.231 vs 0.182)
raw fluctuation at the same cells, consistent with the effect being a
generic property of smooth-kernel SVD tails at large t/L^2, not specific to
zeta's arithmetic; the fake's own dual/Poisson identity breaks at relative
defect 0.368, reproducing e1m's T5a number (0.37) essentially exactly,
which is also a useful fidelity check on the port. D-H unposable (cited);
K1 guards never tripped.

[ADVERSARY, lambda extension, Attack 1] The original grid tops out at
M=pi(lambda^2)=11 (lambda=6), a statistically thin base for a rank-collapse
verdict. Re-running the identical Phase 1 battery at lambda in
{10,14,20,30} (M=25,44,78,154, M ~ 100+) finds the SAME wall, and it
HARDENS: the per-lambda max raw Delta_rho shrinks monotonically
(0.120->0.068->0.038->0.020), never exceeds the original grid's own 0.182
ceiling, and at M>=44 does not even reach the 0.1 magnitude bar at all; no
cell at any tested M clears the conditioning gate. The Beurling twin's own
raw-gap cells (both grids) are now directly confirmed, not just asserted,
to fail the identical sig_r/sig_r1 gate. Full record: _e1q_adversary.md.

HONEST SCOPE
============
This probe proves nothing about RH by itself. The measured wall (tier 3,
MIRAGE) is the pre-registered outcome: the wrap-around correction to a
generic Gaussian kernel is either Gaussian-suppressed wherever G0 is still
well-conditioned (the small/mid-t cells, Delta_rho exactly 0.000 throughout
the grid), or, at large t where a raw rank-count difference does appear, it
tracks a smooth SVD tail rather than a genuine gap. The honest reading,
per the project's stance on negative results as coordinates: a construction
that PROVABLY consumes the additive lattice (unlike KNS's density
criterion, unlike raw trig decimation, unlike the closed majorant route)
still cannot produce a well-conditioned collapse at {k log p} using the
simplest available lattice-consuming device -- a narrowing, not a dead end
(see the spec's own closing section for the next-rung reading:
Cohn-Elkies/Viazovska/Radchenko-Viazovska modular interpolation, genuine
modular forms and Hecke structure, not a bare theta function). A genuine
tier-1 finding would feed BRIDGE-H (landau_one_sided.md Section 3): cheap
multiplicity at {k log p} is exactly what lets the Stepanov pairing run
linearly instead of quadratically, deleting the sieve's level-halving 2.

Run:
  python -m experiments.spectral.e1q_s4_theta_wrap_rung           # full
  python -m experiments.spectral.e1q_s4_theta_wrap_rung --quick   # reduced grids
Outputs:
  experiments/spectral/e1q_s4_theta_wrap_rung.npz  (+ .md companion)
  (--quick does NOT write the npz: the tracked artifact is the full run's,
   matching e1o's own convention.)
"""

from __future__ import annotations

import argparse
import math
import time
import warnings
from pathlib import Path

import numpy as np
import mpmath as mp

from experiments._shared.beurling import BeurlingSystem, _primes_upto
import experiments._shared.davenport_heilbronn as _dhmod

warnings.filterwarnings("ignore")

OUT = Path(__file__).with_suffix(".npz")
CHECKS: list = []
LEDGER: dict = {}

LAMBDA_GRID = (2.2, 3.0, math.sqrt(13.0), 6.0)   # e1o's own T4c grid, verbatim
NWRAP = 80          # matches e1m's own truncation (T1a/T1b)
RANK_THRESH = 1e-8  # e1o's own T4c convention, exactly

# [ADVERSARY, lambda extension] LAMBDA_GRID tops out at M=pi(lambda^2)=11
# (lambda=6): an 11x11 rank-collapse verdict carries limited statistical
# weight (one rank unit is Delta_rho ~ 0.09, right at the 0.1 threshold).
# Extend to M ~ 100+ with the IDENTICAL Phase 1 machinery (same helpers, no
# reimplementation): M = 25, 44, 78, 154 at lambda = 10, 14, 20, 30.
LAMBDA_EXT = (10.0, 14.0, 20.0, 30.0)


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    tag = "PASS" if ok else "FAIL"
    print(f"  [{tag}] {name}" + (f"  ({detail})" if detail else ""))


def consume(test, *inputs):
    LEDGER.setdefault(test, []).extend(inputs)


# ==========================================================================
# The object: node sets, the periodized kernel, the wrap-free control.
# ==========================================================================
def node_set_zeta(lam):
    """X_lambda = {log p : p prime, p <= lambda^2}, e1o's exact log-prime
    comb. The +1e-9 dodges float boundary noise at lam = sqrt(13) (lam*lam
    may round a hair below 13.0)."""
    bound = int(math.ceil(lam * lam)) + 2
    primes = [p for p in _primes_upto(bound) if p <= lam * lam + 1e-9]
    return np.array([math.log(p) for p in primes], dtype=float)


def node_set_beurling(lam, eps=0.25, seed=149):
    """X_lambda^B: BeurlingSystem(...).logs restricted to <= log(lambda^2),
    the repo default fake (e1m T5 / e2ak precedent). The +15 prime_bound
    margin covers primes whose jittered log could cross the lambda^2
    boundary from either side (eps <= 0.25 moves log p by at most 0.25)."""
    bound = int(math.ceil(lam * lam)) + 15
    B = BeurlingSystem(prime_bound=bound, eps=eps, seed=seed)
    cap = math.log(lam * lam) + 1e-9
    return np.array([lv for lv in B.logs if lv <= cap], dtype=float)


def window_L(lam):
    return 2.0 * math.log(lam)


def theta_wrap_np(diff, L, t, nwrap=NWRAP):
    """Primal periodized Gaussian, float64/numpy, vectorized over diff (any
    shape). Nwrap=80 is safe (overkill) across the whole Phase-1 t-range
    t <= L^2: the dropped-tail exponent -pi(n L)^2/t is then at least
    -pi n^2, e.g. n=81 gives ~2e-8952 [ADVERSARY: the original comment said
    "~1e-2800", a hand-arithmetic slip; exp(-pi*81^2) independently verified
    at mpmath dps=50], far below the 1e-12 spec bar. Directly confirmed too:
    Nwrap=80 vs Nwrap=400 agree to <1e-50 relative (mpmath dps=50) and to
    float64 machine precision (the theta_wrap_np path itself) at every
    tested Phase-1 (lambda, t, node-diff) triple, smallest AND largest t."""
    ns = np.arange(-nwrap, nwrap + 1, dtype=float)
    d = diff[..., None] - ns * L
    return np.sum(np.exp(-np.pi * d * d / t), axis=-1)


def gram_matrices(X, L, t):
    """G = the wrapped kernel (consumes the L*Z lattice via the n != 0
    terms); G0 = the n=0-only wrap-free control (a generic Gaussian Gram
    matrix, no lattice input at all). G - G0 isolates the lattice term."""
    diff = X[:, None] - X[None, :]
    G = theta_wrap_np(diff, L, t)
    G0 = np.exp(-np.pi * diff * diff / t)
    return G, G0


def numeric_rank(mat, thresh=RANK_THRESH):
    sv = np.linalg.svd(mat, compute_uv=False)
    rank = int(np.sum(sv > thresh * sv[0]))
    return rank, sv


def is_discovery_candidate(cell):
    """Section (b)'s own bar for a cell worth taking seriously: wrap-
    attributable (Delta_rho>=0.1) AND a genuine sv gap at the declared rank
    (sig_r>1e-3, sig_r+1<1e-6). A raw Delta_rho>=0.1 alone is NOT enough: a
    smooth SVD tail (both G and G0 decaying gradually through the 1e-8
    threshold at slightly different steps) can produce a nonzero rank-count
    difference with no structural gap at all -- exactly the conditioning
    mirage e1o's own adversary round caught once already in a
    near-commensurate decimation family (e1o_s4_carrier.md Adversarial test
    case 2b). This helper is the single source of truth for that gate,
    shared by P1c, P2a, and grade_and_report so the three cannot drift."""
    return (cell["drho"] >= 0.1 and not math.isnan(cell["sig_r1"])
            and cell["sig_r"] > 1e-3 and cell["sig_r1"] < 1e-6)


def t_grid_for(X, L, npts=9):
    """Geometric sweep from the minimum pairwise gap^2 in X up to L^2."""
    gaps = np.diff(np.sort(X))
    t_lo = float(np.min(gaps)) ** 2
    t_hi = L * L
    return np.geomspace(t_lo, t_hi, npts)


# --------------------------------------------------------------------------
# mpmath high-precision primal/dual forms, for Phase 0's identity check only
# (Phase 1/2's Gram matrices use the float64 form above: the rank threshold
# is 1e-8 relative, so double precision is far more than sufficient there,
# and mpmath at the extreme small-t Phase-1 cells would need Kwrap >> 80 to
# hit 1e-25 on the DUAL side -- see the honest-deviation note in main()).
# --------------------------------------------------------------------------
def theta_primal_mp(y, t, L, nwrap=NWRAP):
    y, t, L = mp.mpf(y), mp.mpf(t), mp.mpf(L)
    return mp.nsum(lambda n: mp.e ** (-mp.pi * (y - n * L) ** 2 / t), [-nwrap, nwrap])


def theta_dual_mp(y, t, L, kwrap=NWRAP):
    y, t, L = mp.mpf(y), mp.mpf(t), mp.mpf(L)
    return (mp.sqrt(t) / L) * mp.nsum(
        lambda k: mp.e ** (-mp.pi * k * k * t / (L * L)) * mp.cos(2 * mp.pi * k * y / L),
        [-kwrap, kwrap])


# ==========================================================================
# PHASE 0: the anchor. Rescale e1m's own T1b (x,t) pairs by (y=x*L, t=tf*L^2)
# so the tested t/L^2 ratio matches e1m's actually-verified range (~0.3-2.0,
# where primal and dual both converge fast at Nwrap=Kwrap=80).
# ==========================================================================
PHASE0_PAIRS = [(0.3, 1.1), (0.45, 0.6), (0.1, 0.31), (0.2, 2.0)]


def run_phase0(results, quick):
    print("\n[PHASE 0] THE ANCHOR: generalize e1m's T1b Poisson identity to "
          "period L(lambda), re-verify")
    consume("PHASE0", "Z lattice (wrap index n, primal and dual forms)",
            "window L(lambda) = 2 log lambda (carrier geometry, no arithmetic)")
    lam_list = LAMBDA_GRID[:2] if quick else LAMBDA_GRID
    pairs = PHASE0_PAIRS[:2] if quick else PHASE0_PAIRS
    prev = mp.mp.dps
    mp.mp.dps = 35
    worst_rows = []
    try:
        for lam in lam_list:
            Lm = 2 * mp.log(mp.mpf(lam))
            worst = mp.mpf(0)
            for yf, tf in pairs:
                y = yf * Lm
                t = tf * Lm * Lm
                lhs = theta_primal_mp(y, t, Lm)
                rhs = theta_dual_mp(y, t, Lm)
                d = abs(lhs - rhs) / abs(lhs)
                worst = max(worst, d)
            worst_f = float(worst)
            worst_rows.append((lam, worst_f))
            check(f"P0 dual identity holds at lambda={lam:.4f} (L={float(Lm):.4f}, "
                  f"{len(pairs)} (y,t) pairs)", worst_f < 1e-25, f"max rel defect {worst_f:.2e}")
        check(f"P0 truncation within the e1m cap (Nwrap=Kwrap={NWRAP} <= 80)",
              NWRAP <= 80, f"fixed at N=K={NWRAP} for every cell, every phase")
    finally:
        mp.mp.dps = prev
    results["p0_lambda"] = np.array([r[0] for r in worst_rows])
    results["p0_worst_defect"] = np.array([r[1] for r in worst_rows])
    return worst_rows


# ==========================================================================
# PHASE 1: the collapse test, zeta side.
# ==========================================================================
def run_phase1(results, quick):
    print("\n[PHASE 1] THE COLLAPSE TEST (S4 condition 2), zeta side: "
          "G (wrapped) vs G0 (wrap-free control)")
    consume("PHASE1", "prime logs {log p <= lambda^2} (Euler-product data, X_lambda)",
            "t scale grid (free parameter, no arithmetic)")
    lam_list = list(LAMBDA_GRID[:2]) if quick else list(LAMBDA_GRID)
    npts = 5 if quick else 9
    zeta_cells = []
    t_grid_by_lambda = {}
    print(f"    {'lam':>8} {'t':>10} {'M':>3} {'rk(G)':>5} {'rk(G0)':>6} {'rho':>6} "
          f"{'rho0':>6} {'drho':>7} {'sig_r':>10} {'sig_r+1':>10}")
    for lam in lam_list:
        L = window_L(lam)
        X = node_set_zeta(lam)
        M = len(X)
        tg = t_grid_for(X, L, npts)
        t_grid_by_lambda[lam] = tg
        for t in tg:
            t = float(t)
            G, G0 = gram_matrices(X, L, t)
            rG, svG = numeric_rank(G)
            rG0, svG0 = numeric_rank(G0)
            rho, rho0 = rG / M, rG0 / M
            drho = rho0 - rho
            r = rG
            sig_r = float(svG[r - 1] / svG[0]) if r >= 1 else float("nan")
            sig_r1 = float(svG[r] / svG[0]) if r < M else float("nan")
            cell = dict(lam=lam, t=t, M=M, rG=rG, rG0=rG0, rho=rho, rho0=rho0,
                        drho=drho, sig_r=sig_r, sig_r1=sig_r1)
            zeta_cells.append(cell)
            print(f"    {lam:8.4f} {t:10.4g} {M:3d} {rG:5d} {rG0:6d} {rho:6.3f} "
                  f"{rho0:6.3f} {drho:+7.3f} {sig_r:10.2e} {sig_r1:10.2e}")

    ok_sane = all(0 <= c["rG"] <= c["M"] and 0 <= c["rG0"] <= c["M"]
                  and math.isfinite(c["rho"]) and math.isfinite(c["rho0"]) for c in zeta_cells)
    check("P1a construction sane: ranks in [0,M], rho/rho0 finite at every cell",
          ok_sane, f"{len(zeta_cells)} cells checked")

    # [ADVERSARY, falsifiability spot-check] periodization invariant: the
    # wrap-free control G0 is never LESS full-rank than the wrapped kernel G
    # (rho0 >= rho, i.e. Delta_rho >= 0) at every tested cell. Confirmed
    # empirically at 100+ cells across every system tested in this module
    # (zeta original + extended grid + Beurling twin, both grids); the
    # plausible reason is that periodization (folding/aliasing distant
    # copies back onto the fundamental domain) can only destroy resolving
    # power relative to the free-space kernel, never create it. This is
    # also a structural regression guard: a scratch-copy corruption that
    # swaps gram_matrices' (G, G0) return order (tested during this
    # ADVERSARY round) silently passes P1a/P1c/P1d (ranks stay in [0,M],
    # and a globally negated Delta_rho never crosses the +0.1 discovery
    # bar either) but is caught immediately here (Delta_rho < 0 uniformly).
    neg_drho = [c for c in zeta_cells if c["drho"] < -1e-9]
    check("P1a2 [ADVERSARY] periodization invariant: Delta_rho = rho0-rho >= 0 "
          "at every cell (G0 never less full-rank than G; also guards against "
          "a G/G0 mislabeling bug)",
          not neg_drho,
          f"{len(zeta_cells)} cells, min Delta_rho = {min(c['drho'] for c in zeta_cells):.4f}"
          if not neg_drho else f"{len(neg_drho)} cell(s) VIOLATE the invariant")

    small_t_rho0 = {}
    for lam in lam_list:
        cs = [c for c in zeta_cells if c["lam"] == lam]
        c0 = min(cs, key=lambda c: c["t"])
        small_t_rho0[lam] = c0["rho0"]
    check("P1b wrap-free control G0 at (or near) full rank at the tightest tested bandwidth",
          all(v >= 1.0 - 1e-9 for v in small_t_rho0.values()),
          "; ".join(f"lam={lam:.3f}: rho0={v:.3f}" for lam, v in small_t_rho0.items()))

    max_drho = max(c["drho"] for c in zeta_cells)
    argmax_cell = max(zeta_cells, key=lambda c: c["drho"])
    raw_gap_cells = [c for c in zeta_cells if c["drho"] >= 0.1]
    discovery_cells = [c for c in zeta_cells if is_discovery_candidate(c)]
    check("P1c collapse measurement: no WELL-CONDITIONED cell reaches the S4 discovery bar "
          "(Delta_rho>=0.1 AND a genuine sv gap, sig_r>1e-3 AND sig_r+1<1e-6)",
          not discovery_cells,
          f"max Delta_rho = {max_drho:.4f} at lambda={argmax_cell['lam']:.4f}, "
          f"t={argmax_cell['t']:.4g} (sig_r={argmax_cell['sig_r']:.2e}, "
          f"sig_r+1={argmax_cell['sig_r1']:.2e}); {len(raw_gap_cells)} cell(s) with raw "
          f"Delta_rho>=0.1, {len(discovery_cells)} pass the conditioning gate too "
          f"(a raw gap alone is a known mirage mode, not a discovery: see is_discovery_candidate)")

    # [ADVERSARY, mirage grading] the .md's prose illustrates the mirage with
    # ONE spectrum (lambda=6, t=4.743) and describes it as "smooth monotone
    # decay, no clean gap" -- true for that cell, but NOT a fair description
    # of the other two raw-gap cells, which independently checked here show
    # a SHARP cliff (a genuine ratio-sense gap) at the declared-rank
    # boundary. Print the full spectrum + consecutive-ratio sequence for
    # EVERY raw-gap cell (not just one), and confirm numerically that the
    # rejection reason is uniform regardless of local shape: sig_r fails the
    # absolute 1e-3 scale bar at all of them, smooth-decay or sharp-cliff.
    if raw_gap_cells:
        print("    [ADVERSARY, mirage grading] full spectrum + consecutive-ratio audit "
              "at every raw-gap cell (plot-free numeric criterion):")
    sig_r_all_small = True
    for c in raw_gap_cells:
        Gc, G0c = gram_matrices(node_set_zeta(c["lam"]), window_L(c["lam"]), c["t"])
        svGc = np.linalg.svd(Gc, compute_uv=False)
        ratios = svGc[1:] / np.where(svGc[:-1] > 0, svGc[:-1], np.nan)
        boundary_idx = c["rG"] - 1
        boundary_ratio = float(ratios[boundary_idx]) if boundary_idx < len(ratios) else float("nan")
        others = np.delete(ratios, boundary_idx) if len(ratios) > 1 else ratios
        med_other = float(np.nanmedian(others)) if others.size else float("nan")
        is_cliff = math.isfinite(boundary_ratio) and math.isfinite(med_other) and med_other > 0 \
            and boundary_ratio < 0.1 * med_other
        print(f"      lambda={c['lam']:.4f} t={c['t']:.4g}: sv(G)/sv0 = "
              + " ".join(f"{v/svGc[0]:.2e}" for v in svGc))
        print(f"        boundary ratio sv[r]/sv[r-1] = {boundary_ratio:.2e} vs median "
              f"other consecutive ratio {med_other:.2e}  -> "
              f"{'SHARP CLIFF at the rank boundary' if is_cliff else 'gradual/smooth decay'} "
              f"(shape is NOT what the gate keys on: sig_r={c['sig_r']:.2e} vs 1e-3 is)")
        if c["sig_r"] >= 1e-3:
            sig_r_all_small = False
    check("P1g [ADVERSARY, mirage grading] every raw-gap cell is rejected on absolute scale "
          "(sig_r < 1e-3) independent of local spectral shape (both smooth-decay and "
          "sharp-cliff shapes occur among the 3 flagged cells)",
          sig_r_all_small,
          f"{len(raw_gap_cells)} raw-gap cell(s) audited; max sig_r among them = "
          f"{max((c['sig_r'] for c in raw_gap_cells), default=float('nan')):.2e}"
          if raw_gap_cells else "no raw-gap cells this run (nothing to audit)")

    lam_sorted = sorted(set(lam_list))
    if len(lam_sorted) >= 2:
        lam_a, lam_b = lam_sorted[-2], lam_sorted[-1]
        drho_a = [c["drho"] for c in zeta_cells if c["lam"] == lam_a]
        drho_b = [c["drho"] for c in zeta_cells if c["lam"] == lam_b]
        max_a, max_b = max(drho_a), max(drho_b)
        shrinking = (max_b < 0.5 * max_a) if max_a > 1e-6 else False
        uni_detail = (f"lambda {lam_a:.4f}: max drho {max_a:.4f}; "
                       f"lambda {lam_b:.4f}: max drho {max_b:.4f}; "
                       f"{'SHRINKING' if shrinking else 'not shrinking (consistent with both nil)'}")
    else:
        uni_detail = "single lambda tested (quick mode): uniformity check not applicable"
    check("P1d lambda-uniformity read across the two largest tested lambda", True, uni_detail)

    results["p1_lam"] = np.array([c["lam"] for c in zeta_cells])
    results["p1_t"] = np.array([c["t"] for c in zeta_cells])
    results["p1_M"] = np.array([c["M"] for c in zeta_cells])
    results["p1_rho"] = np.array([c["rho"] for c in zeta_cells])
    results["p1_rho0"] = np.array([c["rho0"] for c in zeta_cells])
    results["p1_drho"] = np.array([c["drho"] for c in zeta_cells])
    results["p1_sig_r"] = np.array([c["sig_r"] for c in zeta_cells])
    results["p1_sig_r1"] = np.array([c["sig_r1"] for c in zeta_cells])
    return zeta_cells, t_grid_by_lambda, lam_list


# ==========================================================================
# PHASE 1-EXT [ADVERSARY, lambda extension]: the small-M triviality attack.
# LAMBDA_GRID tops out at M=11 (lambda=6): re-run the IDENTICAL Phase 1
# battery (same node_set_zeta/gram_matrices/numeric_rank/is_discovery_
# candidate helpers, no reimplementation) at M ~ 100+, to see whether the
# wall holds once there is real statistical weight behind the measurement.
# ==========================================================================
def run_phase1_ext(results, quick, zeta_cells):
    print("\n[PHASE 1-EXT, ADVERSARY] SMALL-M TRIVIALITY: identical battery at "
          "lambda in {10, 14, 20, 30} (M = 25, 44, 78, 154), M ~ 100+")
    consume("PHASE1EXT", "prime logs {log p <= lambda^2} (Euler-product data, extended lambda)",
            "t scale grid (free parameter, no arithmetic)")
    lam_list = list(LAMBDA_EXT[:1]) if quick else list(LAMBDA_EXT)
    npts = 5 if quick else 9
    ext_cells = []
    print(f"    {'lam':>8} {'t':>10} {'M':>4} {'rk(G)':>5} {'rk(G0)':>6} {'rho':>6} "
          f"{'rho0':>6} {'drho':>7} {'sig_r':>10} {'sig_r+1':>10}")
    for lam in lam_list:
        L = window_L(lam)
        X = node_set_zeta(lam)
        M = len(X)
        tg = t_grid_for(X, L, npts)
        for t in tg:
            t = float(t)
            G, G0 = gram_matrices(X, L, t)
            rG, svG = numeric_rank(G)
            rG0, svG0 = numeric_rank(G0)
            rho, rho0 = rG / M, rG0 / M
            drho = rho0 - rho
            r = rG
            sig_r = float(svG[r - 1] / svG[0]) if r >= 1 else float("nan")
            sig_r1 = float(svG[r] / svG[0]) if r < M else float("nan")
            cell = dict(lam=lam, t=t, M=M, rG=rG, rG0=rG0, rho=rho, rho0=rho0,
                        drho=drho, sig_r=sig_r, sig_r1=sig_r1)
            ext_cells.append(cell)
            print(f"    {lam:8.4f} {t:10.4g} {M:4d} {rG:5d} {rG0:6d} {rho:6.3f} "
                  f"{rho0:6.3f} {drho:+7.3f} {sig_r:10.2e} {sig_r1:10.2e}")

    max_drho = max(c["drho"] for c in ext_cells)
    argmax_cell = max(ext_cells, key=lambda c: c["drho"])
    raw_gap_cells = [c for c in ext_cells if c["drho"] >= 0.1]
    discovery_cells = [c for c in ext_cells if is_discovery_candidate(c)]
    check("P1e [ADVERSARY, lambda extension] small-M triviality closed: no "
          "WELL-CONDITIONED cell at M in {25,44,78,154} (M ~ 100+) reaches "
          "the S4 discovery bar",
          not discovery_cells,
          f"max Delta_rho = {max_drho:.4f} at lambda={argmax_cell['lam']:.4f}, "
          f"M={argmax_cell['M']}, t={argmax_cell['t']:.4g} (sig_r={argmax_cell['sig_r']:.2e}, "
          f"sig_r+1={argmax_cell['sig_r1']:.2e}); {len(raw_gap_cells)} cell(s) with raw "
          f"Delta_rho>=0.1, {len(discovery_cells)} pass the conditioning gate too")

    neg_drho_ext = [c for c in ext_cells if c["drho"] < -1e-9]
    check("P1e2 [ADVERSARY] periodization invariant holds at the extended grid too "
          "(Delta_rho >= 0 at every extended cell)",
          not neg_drho_ext, f"{len(ext_cells)} extended cells checked")

    orig_max = max(c["drho"] for c in zeta_cells)
    lam_sorted = sorted({c["lam"] for c in ext_cells})
    if len(lam_sorted) >= 2:
        per_lam_max = [(lm, max(c["drho"] for c in ext_cells if c["lam"] == lm)) for lm in lam_sorted]
        non_increasing = all(per_lam_max[i][1] >= per_lam_max[i + 1][1] - 1e-9
                              for i in range(len(per_lam_max) - 1))
        detail = "; ".join(f"lambda={lm:.0f}: max drho={mx:.4f}" for lm, mx in per_lam_max)
        detail += f"; non-increasing across the extended grid = {non_increasing}"
    else:
        non_increasing = True
        detail = "single lambda tested (quick mode): hardening-trend check not applicable"
    # [ADVERSARY, quick/full parity fix] comparing against the ORIGINAL
    # grid's max is only a fair, meaningful bound in FULL mode: quick mode's
    # own Phase 1 grid (lambda in {2.2, 3.0} only) never reaches lambda=6,
    # the cell where the original grid's own raw gaps actually live, so
    # orig_max in quick mode is a vacuous 0.0000 and the comparison would
    # spuriously fail (caught by this round's own quick/full parity check:
    # an earlier version of this check ran unconditionally and correctly
    # FAILED under --quick for exactly this reason, a real self-inflicted
    # bug this ADVERSARY round found and fixed, not a construction flaw).
    if quick:
        orig_bounded = True
        detail += (f"; original-grid bound check skipped in quick mode (quick's own Phase 1 "
                   f"grid, lambda in {{2.2,3.0}}, does not include lambda=6 where the original "
                   f"grid's own gaps occur, so orig_max={orig_max:.4f} is not a fair reference "
                   f"here); extended max for the record: {max_drho:.4f}")
    else:
        orig_bounded = max_drho <= orig_max + 1e-9
        detail += f"; extended max {max_drho:.4f} <= original grid max {orig_max:.4f} = {orig_bounded}"
    check("P1f [ADVERSARY, lambda extension] the wall HARDENS with M: max raw Delta_rho "
          "across the extended grid never exceeds the original grid's own max (full mode), "
          "and (when more than one extended lambda is tested) is non-increasing in M",
          non_increasing and orig_bounded, detail)

    results["p1ext_lam"] = np.array([c["lam"] for c in ext_cells])
    results["p1ext_t"] = np.array([c["t"] for c in ext_cells])
    results["p1ext_M"] = np.array([c["M"] for c in ext_cells])
    results["p1ext_drho"] = np.array([c["drho"] for c in ext_cells])
    results["p1ext_sig_r"] = np.array([c["sig_r"] for c in ext_cells])
    results["p1ext_sig_r1"] = np.array([c["sig_r1"] for c in ext_cells])
    return ext_cells, lam_list


def run_phase2_ext(results, ext_cells, lam_list_ext, quick):
    print("\n[PHASE 2-EXT, ADVERSARY] Beurling twin at the extended (M ~ 100+) lambda grid")
    consume("PHASE2EXT", "Beurling fake logs at extended lambda (b_p = p e^eps, seed 149)")
    twin_ext_cells = []
    print(f"    {'lam':>8} {'t':>10} {'Mb':>4} {'rho_B':>6} {'rho0_B':>6} {'drho_B':>7}  "
          f"vs zeta drho")
    for lam in lam_list_ext:
        L = window_L(lam)
        Xb = node_set_beurling(lam)
        Mb = len(Xb)
        cs = [c for c in ext_cells if c["lam"] == lam]
        for c in cs:
            t = c["t"]
            if Mb >= 2:
                G, G0 = gram_matrices(Xb, L, t)
                rG, _ = numeric_rank(G)
                rG0, _ = numeric_rank(G0)
                rho, rho0 = rG / Mb, rG0 / Mb
            else:
                rho = rho0 = float("nan")
            drho = rho0 - rho
            twin_ext_cells.append(dict(lam=lam, t=t, M=Mb, drho=drho))
            print(f"    {lam:8.4f} {t:10.4g} {Mb:4d} {rho:6.3f} {rho0:6.3f} {drho:+7.3f}   "
                  f"{c['drho']:+.3f}")

    finite_twin = [c["drho"] for c in twin_ext_cells if math.isfinite(c["drho"])]
    max_twin = max(finite_twin) if finite_twin else float("nan")
    max_zeta_ext = max(c["drho"] for c in ext_cells)
    disc_ext = [c for c in ext_cells if is_discovery_candidate(c)]
    if disc_ext:
        twin_lookup_ext = {(c["lam"], c["t"]): c for c in twin_ext_cells}
        comparable = [(c, twin_lookup_ext[(c["lam"], c["t"])]) for c in disc_ext]
        sep_ok = all(math.isfinite(tc["drho"]) and tc["drho"] <= 0.5 * zc["drho"] + 1e-9
                      for zc, tc in comparable)
        detail = (f"{len(comparable)} discovery-candidate cell(s) at extended lambda: "
                  f"twin <= half of zeta at all = {sep_ok}")
    else:
        sep_ok = True
        detail = (f"no extended-lambda zeta cell clears the discovery bar (consistent with "
                  f"P1e): raw max Delta_rho for the record: zeta {max_zeta_ext:.4f}, "
                  f"twin {max_twin:.4f}")
    check("P2h [ADVERSARY, lambda extension] Beurling twin at M ~ 100+ also shows no "
          "well-conditioned gap; comparable raw fluctuation to zeta's",
          sep_ok, detail)

    neg_drho_twin_ext = [c for c in twin_ext_cells if math.isfinite(c["drho"]) and c["drho"] < -1e-9]
    check("P2h2 [ADVERSARY] periodization invariant holds for the twin at the extended grid too",
          not neg_drho_twin_ext, f"{len(twin_ext_cells)} extended twin cells checked")

    results["p2ext_twin_lam"] = np.array([c["lam"] for c in twin_ext_cells])
    results["p2ext_twin_t"] = np.array([c["t"] for c in twin_ext_cells])
    results["p2ext_twin_M"] = np.array([c["M"] for c in twin_ext_cells])
    results["p2ext_twin_drho"] = np.array([c["drho"] for c in twin_ext_cells])
    return twin_ext_cells


# ==========================================================================
# PHASE 2: the disciplines, in the same run.
# ==========================================================================
def run_phase2(results, zeta_cells, t_grid_by_lambda, lam_list, quick, guards):
    print("\n[PHASE 2] THE DISCIPLINES: Beurling twin (both ways), D-H citation, K1 ledger")
    consume("PHASE2", "Beurling fake logs (b_p = p e^eps, eps ~ U[-0.25,0.25], seed 149)",
            "Beurling generalized integers (gen_integers: the fake's own wrap-sum analogue)",
            "D-H sign-change / type-exclusion numbers, CITED from e1o T5a and e1m T2 "
            "(no new D-H computation)")

    # ---- 2(a): the twin's node set through the TRUE kernel, matched cells ----
    twin_cells = []
    twin_lookup = {}
    print(f"    {'lam':>8} {'t':>10} {'Mb':>3} {'rho_B':>6} {'rho0_B':>6} {'drho_B':>7}  "
          f"vs zeta drho")
    for lam in lam_list:
        L = window_L(lam)
        Xb = node_set_beurling(lam)
        Mb = len(Xb)
        for t in t_grid_by_lambda[lam]:
            t = float(t)
            if Mb >= 2:
                G, G0 = gram_matrices(Xb, L, t)
                rG, svG = numeric_rank(G)
                rG0, _ = numeric_rank(G0)
                rho, rho0 = rG / Mb, rG0 / Mb
                # [ADVERSARY, twin fairness] capture the twin's OWN conditioning
                # pair too (previously discarded: the code only ever compared
                # drho, never checked whether the twin's raw fluctuation is
                # itself mirage-graded by the SAME sig_r/sig_r1 gate zeta's
                # cells are held to -- see the new P2a2 check below).
                r = rG
                sig_r = float(svG[r - 1] / svG[0]) if r >= 1 else float("nan")
                sig_r1 = float(svG[r] / svG[0]) if r < Mb else float("nan")
            else:
                rho = rho0 = float("nan")
                sig_r = sig_r1 = float("nan")
            drho = rho0 - rho
            cell = dict(lam=lam, t=t, M=Mb, rho=rho, rho0=rho0, drho=drho,
                        sig_r=sig_r, sig_r1=sig_r1)
            twin_cells.append(cell)
            twin_lookup[(lam, t)] = cell
            zc = next(c for c in zeta_cells if c["lam"] == lam and abs(c["t"] - t) < 1e-9)
            print(f"    {lam:8.4f} {t:10.4g} {Mb:3d} {rho:6.3f} {rho0:6.3f} {drho:+7.3f}   "
                  f"{zc['drho']:+.3f}")

    # The Section (c)(ii) separation bar only binds on cells that are actual
    # discovery CANDIDATES on the zeta side (is_discovery_candidate: raw
    # Delta_rho alone is a known mirage mode, see P1c). Per the spec's own
    # table (Section (b)): "twin tracks zeta if Phase 1 walls (both nil);
    # separates if Phase 1 finds a genuine gap" -- when Phase 1 has no
    # discovery candidate, "both nil" (or both mirage-level) IS the passing
    # row, not a stricter half-of-a-near-zero-signal bound. The raw,
    # mirage-level numbers are still printed above (nothing hidden).
    candidates = [c for c in zeta_cells if is_discovery_candidate(c)]
    if candidates:
        comparable = [(c, twin_lookup[(c["lam"], c["t"])]) for c in candidates]
        sep_ok = all(math.isfinite(tc["drho"]) and tc["drho"] <= 0.5 * zc["drho"] + 1e-9
                      for zc, tc in comparable)
        detail = (f"{len(comparable)} discovery-candidate cell(s): twin <= half of zeta "
                  f"at all of them = {sep_ok}")
    else:
        sep_ok = True
        max_zeta_drho = max(c["drho"] for c in zeta_cells)
        finite_twin = [c["drho"] for c in twin_cells if math.isfinite(c["drho"])]
        max_twin_drho = max(finite_twin) if finite_twin else float("nan")
        detail = (f"no zeta cell clears the discovery bar (Phase 1 walled/mirage-only): "
                  f"the spec's own 'both nil' row applies, not a discriminator here; "
                  f"raw max Delta_rho for the record: zeta {max_zeta_drho:.4f}, "
                  f"twin {max_twin_drho:.4f}")
    check("P2a Beurling twin (node-set swap through the TRUE kernel) at matched cells",
          sep_ok, detail)

    # [ADVERSARY, twin fairness] the .md's "generic SVD-tail noise, not an
    # arithmetic effect" reading for the twin's own larger raw fluctuation
    # (e.g. 0.231 at lambda=6, t=12.84) was previously asserted in PROSE
    # only: the code discarded the twin's singular values (`rG, _ =
    # numeric_rank(G)`) and never actually checked them against the same
    # is_discovery_candidate gate zeta's cells are held to. Now computed
    # (see the capture above): confirm every twin cell with a raw gap
    # (drho>=0.1) is ITSELF rejected by the identical numeric criterion,
    # so the "mirage, not arithmetic" reading is verified, not just argued.
    twin_raw_gap = [c for c in twin_cells if math.isfinite(c["drho"]) and c["drho"] >= 0.1]
    twin_discovery = [c for c in twin_raw_gap if is_discovery_candidate(c)]
    check("P2a2 [ADVERSARY, twin fairness] the twin's OWN raw-gap cells are mirage-graded "
          "by the IDENTICAL conditioning gate (sig_r>1e-3, sig_r1<1e-6), not merely asserted "
          "to be noise",
          not twin_discovery,
          f"{len(twin_raw_gap)} twin cell(s) with raw Delta_rho>=0.1, max sig_r among them = "
          f"{max((c['sig_r'] for c in twin_raw_gap), default=float('nan')):.2e} (all < 1e-3)"
          if twin_raw_gap else "no twin cell reaches raw Delta_rho>=0.1 this run")

    neg_drho_twin = [c for c in twin_cells if math.isfinite(c["drho"]) and c["drho"] < -1e-9]
    check("P2a3 [ADVERSARY] periodization invariant holds for the twin too "
          "(Delta_rho >= 0 at every twin cell)",
          not neg_drho_twin, f"{len(twin_cells)} twin cells checked")

    # ---- 2(b): the fake's OWN wrap-sum/dual identity (e1m T5a's construction, ----
    # ---- reproduced verbatim: Z -> B.gen_integers in the theta wrap sum) --------
    Bfe = BeurlingSystem(prime_bound=15000, eps=0.25, seed=149)
    small = [lv for lv in Bfe.gen_integers(40)]

    def theta_fake(u):
        return 1 + 2 * sum(math.exp(-math.pi * math.exp(2 * lv) * u) for lv in small if lv > 0)

    worst_fake = max(abs(theta_fake(1 / t) - math.sqrt(t) * theta_fake(t)) / theta_fake(1 / t)
                      for t in (0.7, 1.3, 2.0))
    check("P2b the fake's own dual/Poisson identity BREAKS (Z -> B.gen_integers in the wrap sum)",
          worst_fake > 1e-3,
          f"relative defect {worst_fake:.3f} (true Z gives <1e-25; predicted order 0.1-1, "
          f"cf. e1m T5a's 0.37 for the identical un-rescaled construction)")

    print("    D-H (cited, not recomputed): e1o T5a: 25 sign changes below n=60, negative")
    print("    excess exhibit -0.288 at (x=10,delta=2): no privileged prime-power sublattice")
    print("    (AX-FORM). e1m T2: own FE exact (~1e-30), Riemann-type FE fails at O(1)")
    print("    (defect 1.72), budget surplus ~20.7 zeros at T=85.699 (type exclusion).")
    check("P2c D-H unposable (AX-FORM + type exclusion, cited from e1o T5a / e1m T2)",
          True, "no new D-H computation; both arguments independent of Phase 1's outcome")

    src = Path(__file__).read_text(encoding="utf-8")
    forbidden = ["zeta" + "zero", "ZETA_" + "ZEROS", "DH_" + "ZEROS", ".zeros" + "("]
    # [ADVERSARY, K1 scanner hardening] the exemption used to be a bare
    # substring test ("K1-ALLOW" not in ln), which an injection test showed
    # is gameable: a line with a genuine, unguarded mp.zetazero(1) call was
    # silently exempted because its own comment happened to DISCUSS
    # K1-ALLOW ("...no K1-ALLOW") without actually marking one. Tightened to
    # require the marker to appear as an actual trailing-comment token
    # ("# K1-ALLOW", matching the two real guard-install lines below
    # verbatim), which closes that specific gap (independently verified: the
    # two legitimate exemptions still pass, the crafted injection is now
    # caught). This is a heuristic, not a proof: a line whose comment
    # contains the literal substring "# K1-ALLOW" without being a genuine
    # exemption would still slip past a purely textual scan -- which is why
    # the RUNTIME guard below (P2e), not this scan, is the load-bearing K1
    # enforcement; the scan is a fast first line, not the actual proof.
    scan = [ln for ln in src.splitlines()
            if not ln.strip().startswith("#") and "# K1-ALLOW" not in ln]
    hits = [tok for tok in forbidden if any(tok in ln for ln in scan)]
    check("P2d K1 source scan: no zero-list / zero-scanner access in the theta-wrap path",
          not hits, f"forbidden tokens: {hits}" if hits else "clean")
    check("P2e K1 runtime guards installed, never tripped",
          guards["installed"] and not guards["tripped"], "any call would have raised")
    print("    input ledger (what each phase consumed):")
    for test in sorted(LEDGER):
        for item in LEDGER[test]:
            print(f"      {test}: {item}")
    bad = [t for t, items in LEDGER.items()
           if any("zero" in i.lower() and "no zero" not in i.lower()
                  and "no new" not in i.lower() for i in items)]
    check("P2f ledger: no phase consumed a zero list", not bad, str(bad) if bad else "clean")

    results["p2_twin_lam"] = np.array([c["lam"] for c in twin_cells])
    results["p2_twin_t"] = np.array([c["t"] for c in twin_cells])
    results["p2_twin_M"] = np.array([c["M"] for c in twin_cells])
    results["p2_twin_drho"] = np.array([c["drho"] for c in twin_cells])
    results["p2_fake_defect"] = worst_fake
    return twin_cells, twin_lookup


# ==========================================================================
# GRADING: spec Section (d)'s four tiers.
# ==========================================================================
def grade_and_report(zeta_cells, twin_lookup):
    max_drho = max(c["drho"] for c in zeta_cells)
    raw_gap_cells = [c for c in zeta_cells if c["drho"] >= 0.1]
    if not raw_gap_cells:
        return 3, ("BLIND: no cell reaches Delta_rho >= 0.1 "
                    f"(max measured {max_drho:.4f}); both G and G0 track full rank together, "
                    "the wrap-around correction is Gaussian-suppressed wherever G0 is still "
                    "well-conditioned.")

    well_cond = [c for c in raw_gap_cells if is_discovery_candidate(c)]
    if not well_cond:
        return 3, (f"MIRAGE: {len(raw_gap_cells)} cell(s) reach Delta_rho >= 0.1 but none clear "
                    "the conditioning gate (sig_r>1e-3 and sig_r+1<1e-6): a smooth tail, not a "
                    "genuine rank drop.")

    lam_sorted = sorted({c["lam"] for c in zeta_cells})
    if len(lam_sorted) >= 2:
        lam_a, lam_b = lam_sorted[-2], lam_sorted[-1]
        a_max = max((c["drho"] for c in well_cond if c["lam"] == lam_a), default=0.0)
        b_max = max((c["drho"] for c in well_cond if c["lam"] == lam_b), default=0.0)
        uniform = (b_max >= 0.5 * a_max) if a_max > 0 else (b_max >= 0.1)
    else:
        uniform = True

    separators, non_separators = [], []
    for c in well_cond:
        tc = twin_lookup.get((c["lam"], c["t"]))
        if tc is not None and math.isfinite(tc["drho"]) and tc["drho"] <= 0.5 * c["drho"]:
            separators.append(c)
        else:
            non_separators.append(c)

    if uniform and separators and not non_separators:
        return 1, (f"LATTICE-GENUINE COLLAPSE: {len(separators)} cell(s) clear all four "
                    "conditions (wrap-attributable, well-conditioned, lambda-uniform, "
                    "Beurling-separating).")
    if separators:
        return 2, (f"MEASURED BUT PARTIAL: {len(separators)} well-conditioned, "
                    f"Beurling-separating cell(s), uniform={uniform}; "
                    f"{len(non_separators)} well-conditioned cell(s) did not separate.")
    if non_separators and uniform:
        return 4, (f"SYSTEM-GENERIC: {len(non_separators)} cell(s) clear conditioning + "
                    "uniformity but reproduce at matched strength on the Beurling twin: the "
                    "DMV-kill trap, reported as required even though nominally a positive "
                    "rank result.")
    return 2, (f"MEASURED BUT PARTIAL: {len(well_cond)} well-conditioned cell(s), "
               f"uniform={uniform}, none cleanly Beurling-separating.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true", help="reduced lambda/t grids")
    args = ap.parse_args()
    t0 = time.time()

    guards = {"installed": True, "tripped": False}

    def _forbid(*a, **k):
        guards["tripped"] = True
        raise RuntimeError("K1 guard: zero-list access attempted")
    mp.zetazero = _forbid                              # K1-ALLOW (guard install)
    _dhmod.davenport_heilbronn.zeros = _forbid          # K1-ALLOW (guard install)

    print("=" * 78)
    print("E1Q: theta/Poisson wrap-collapse rung (form-side S4 probe, post-corridor pivot)")
    print("=" * 78)

    results = {}
    run_phase0(results, args.quick)
    zeta_cells, t_grid_by_lambda, lam_list = run_phase1(results, args.quick)
    ext_cells, lam_list_ext = run_phase1_ext(results, args.quick, zeta_cells)
    run_phase2_ext(results, ext_cells, lam_list_ext, args.quick)
    twin_cells, twin_lookup = run_phase2(results, zeta_cells, t_grid_by_lambda, lam_list,
                                          args.quick, guards)

    tier, tier_detail = grade_and_report(zeta_cells, twin_lookup)
    tier_names = {1: "LATTICE-GENUINE COLLAPSE (the S4 bar met)",
                  2: "MEASURED BUT PARTIAL",
                  3: "BLIND / MIRAGE / WALL",
                  4: "SYSTEM-GENERIC (DMV-kill trap)"}
    check(f"GRADE: Section (d) tier = {tier} ({tier_names[tier]})", True, tier_detail)

    print("\n" + "=" * 78)
    print("STATUS")
    print("=" * 78)
    print(f"  tier = {tier} :: {tier_names[tier]}")
    print(f"  {tier_detail}")
    if tier == 3:
        print("  Reading: the wall is a coordinate, not a dead end (CLAUDE.md stance). A")
        print("  construction that provably consumes the additive lattice still could not")
        print("  produce a well-conditioned collapse at {k log p} with the simplest such")
        print("  device (a bare periodized Gaussian): the missing mechanism is narrowed to")
        print("  one that ties the lattice to the Euler-product structure nontrivially --")
        print("  the modular-interpolation corner (Cohn-Elkies/Viazovska/Radchenko-Viazovska)")
        print("  the spec names as the next rung.")
    elif tier == 4:
        print("  Reading: report plainly, do NOT claim an S4 discovery. The DMV kill applies:")
        print("  a mechanism indistinguishable from its Beurling twin is pre-killed at every")
        print("  exponent below 1 regardless of the collapse measurement.")
    else:
        print("  Reading: a genuine positive. Re-verify at higher mpmath precision and the")
        print("  conditioning gate before this is reported further (honesty clamp).")
    print("=" * 78)

    n_ok = sum(1 for _, ok in CHECKS if ok)
    print(f"\nSELF-TEST: {n_ok}/{len(CHECKS)} checks passed")
    for name, ok in CHECKS:
        if not ok:
            print(f"  FAILED: {name}")

    if args.quick:
        print("(--quick: npz NOT saved; the tracked artifact is the full run's)")
    else:
        np.savez_compressed(OUT, **results)
        print(f"Saved -> {OUT}")
    print(f"Total time {time.time() - t0:.1f}s")
    if n_ok != len(CHECKS):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
