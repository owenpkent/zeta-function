"""H2 (LEARNINGS #143 handoff): is there an interlacing-family engine for MESH?

Mesh = the minimum circular gap between consecutive zeros of a polynomial with
all zeros on the unit circle. It is the one natively ORDERED quantity on the
circle locus (#143 killed the location version: the circle has no one-sided
order for root LOCATION, so the MSS selection step dies there). This module
asks the follow-up at the spacing axis: Suffridge's class S_n (degree n, all
zeros on |z| = 1, consecutive gaps >= 2pi/(n+1)) is closed under the binomial
Schur-Szego composition (Suffridge 1976; Lamprecht 2016; Leake-Ryder 2020
connect it to the q-multiplicative finite free convolution at q on the unit
circle), and POPUC supplies a circle interlacing order, so two of the three
MSS organs exist at the mesh axis too. Does the third (averaging + extremal
selection) run?

HONEST LABEL UP FRONT. Mesh is a spacing statistic (Level-3-adjacent, the #120
wrong-axis screen) and is undefined off the circle (it presupposes the locus),
so NOTHING here is an M4 route. The prize is smaller and publishable either
way: a first circle-side interlacing-family-shaped statement about spacing, or
the sharp reason none exists.

CONVENTION CORRECTION (recorded, load-bearing). The task spec said "mesh >=
2pi/n" for degree n; that class is empty of interest: n circular gaps sum to
2pi, so mesh <= 2pi/n always, with equality exactly at rotated roots-of-unity
polynomials. The literature class (Suffridge) is gaps >= 2pi/(n+1), which is
what this module implements. Likewise the task's suggested identity z^n - 1
FAILS validation as the composition identity (Test 5): the true identity of
the Schur-Szego composition (f*g)_k = f_k g_k / binom(n,k) is (1+z)^n, and
z^n - 1 is instead the PROJECTOR onto the equal-spacing extremal point
(f * (z^n - 1) = f_n z^n - f_0 exactly).

What the battery finds (all numbers from the tests below):

  Test 1-2. The POPUC pencil B(z; beta) is circle-rooted with pairwise
      interlacing zeros, and the circle Hermite-Biehler question splits by a
      PHASE GAUGE: the naive real convex combination lam B1 + (1-lam) B2 exits
      the circle at EVERY interior lam (provably: it equals z Phi - c Phi*
      with |c| < 1, and the degree-n Blaschke argument pulls all n roots
      strictly inside the disk), while the phase-ALIGNED combination (each
      member rotated to self-inversive phase -1) stays exactly circle-rooted:
      it IS the POPUC arc, beta_eff = D/conj(D) unimodular. Averaging on the
      chord leaves the locus; averaging on the arc is the only legal mean.
      The #143 lesson (linear averaging is the gate) at the pencil level.

  Test 3. Circle Hermite-Biehler dichotomy beyond POPUC: phase-aligned
      STRICTLY INTERLACING pairs have all convex combinations circle-rooted
      (provable by the cyclic sign-alternation argument on the real trig
      restriction i e^{-in t/2} p(e^{it})); a phase-aligned NON-interlacing
      control pair loses the circle at interior lam. Interlacing is exactly
      the convex-stability condition, as on the line.

  Test 4. Mesh along the aligned pencil: the naive intermediate-value bound
      mesh(lam) >= min(mesh(0), mesh(1)) FAILS (staggered zero speeds let a
      gap dip below both endpoint values mid-path), but the merged-endpoint
      FLOOR holds: mesh(lam) >= min gap between consecutive travel cells
      (each zero rides monotonically inside the cell cut out by its lam = 0
      and lam = 1 positions). The floor is the correct pencil statement.

  Test 5-7. The Suffridge convolution: identity validated ((1+z)^n exact),
      z^n - 1 = equal-spacing projector, S_n closure verified on random pairs
      (circle-rooted + mesh >= 2pi/(n+1)), and circle-rootedness of the
      composition holds UNCONDITIONALLY for arbitrary circle-rooted inputs
      (Grace-Szego disk bound + self-inversiveness pins the locus; no mesh
      hypothesis needed for the locus). The teeth question came back SPLIT:
      a SINGLE sub-threshold gap is repaired above the bound by one
      composition, 300/300 times (the composition is strongly smoothing),
      so the naive "preservation fails below threshold" expectation is
      wrong for single violations; the teeth live at CLUSTERED violations
      (whole-cluster inputs with mesh eps compose to mesh ~ 1.36 eps, far
      below the bound: the class below threshold is NOT closed). In every
      tested pair, including all adversarial shapes, the output mesh is
      >= min(mesh f, mesh g): composition never creates a tighter gap than
      its inputs (mesh min-monotonicity, CONJECTURE; Suffridge closure is
      its threshold case).

  Test 8. THE ENGINE TEST. The three averaging modes: (a) the raw
      coefficient mean is off the locus, and the phase-ALIGNED mean of 40
      Suffridge members is (surprise) circle-rooted at machine precision,
      but only by class RIGIDITY (every member is a perturbation of
      c cos(nt/2 + phi), and 40 random phases rarely cancel the leading
      term): pairwise it is exactly the HB dichotomy (non-alternating
      in-class pairs exit the circle, defect up to ~0.8), and the aligned
      mean of 40 ARBITRARY circle-rooted members is far off the locus
      (defect ~0.5). (c) the z^n - 1 kernel mode collapses to
      z^n - mean(unimodular), roots on a SHRUNKEN circle (literally the
      #143 collapse). (b) the Suffridge composition stays on the locus and
      in S_n, BUT it is a CONTRACTION onto the equal-spacing extremal point
      (middle normalized coefficients are products of moduli < 1; after 40
      compositions max middle |A_k| ~ 1e-68), so the MSS selection
      inequality "some member has mesh >= mesh(average)" is decisively
      FALSE: the average out-meshes every member (and so does the aligned
      linear mean) and FORGETS the family. Alternation is common across the
      rigid family (~76% of pairs) but not universal: no common
      interlacing. The MSS shape does not exist at the mesh axis: every
      locus-keeping average is mesh-dominant (selection is pointless and
      false), and the average a selection step would need is either
      locus-breaking or interlacing-gated.

  Test 9. The screens. (a) Presupposes-the-locus: mesh is computed from
      angles only, so it is RADIALLY BLIND: moving a root to radius 1.3 at
      the same angle leaves "mesh" unchanged while circle-rootedness is
      destroyed. Mesh orders configurations WITHIN the locus; it cannot
      certify TOWARD it. (b) Wrong axis (#120): mesh is spacing, not
      location; any theorem here is a circle-side spacing result, not M4.

Run from the repo root:  python -m experiments.toy.suffridge_mesh
"""

from __future__ import annotations

import itertools
import math
import sys
from functools import reduce

import numpy as np

from experiments.toy.circle_interlacing import (
    para_orthogonal,
    poly_zeros_ascending,
    szego_phi,
    szego_step,
)

TWO_PI = 2.0 * np.pi
N = 8                                  # working degree for the POPUC/Suffridge tests
THRESH = TWO_PI / (N + 1)              # the Suffridge mesh bound 2pi/(n+1)
MAX_MESH = TWO_PI / N                  # unreachable-above ceiling (gaps sum to 2pi)


# ---------------------------------------------------------------------------
# Helpers: mesh, phases, the Schur-Szego composition, samplers.
# ---------------------------------------------------------------------------
def circle_defect(zs) -> float:
    return float(np.max(np.abs(np.abs(zs) - 1.0)))


def sorted_angles(zs) -> np.ndarray:
    return np.sort(np.mod(np.angle(zs), TWO_PI))


def circular_gaps_from_angles(angles) -> np.ndarray:
    a = np.sort(np.mod(np.asarray(angles, dtype=float), TWO_PI))
    return np.mod(np.roll(a, -1) - a, TWO_PI)


def mesh_angles(angles) -> float:
    """Min circular gap of an angle configuration. NOTE: angles only; this
    functional never sees the radius (Test 9 makes that blindness explicit)."""
    return float(np.min(circular_gaps_from_angles(angles)))


def mesh(zs) -> float:
    return mesh_angles(np.angle(zs))


def si_star(p: np.ndarray) -> np.ndarray:
    """p*(z) = z^n conj(p(1/conj z)) on ascending coefficient arrays."""
    return np.conj(p[::-1])


def si_phase(p: np.ndarray, tol: float = 1e-8):
    """If p is self-inversive up to phase (p* = w p, |w| = 1) return w, else None."""
    k = int(np.argmax(np.abs(p)))
    if abs(p[k]) == 0.0:
        return None
    w = si_star(p)[k] / p[k]
    if np.max(np.abs(si_star(p) - w * p)) > tol * np.max(np.abs(p)):
        return None
    return complex(w)


def align_phase(p: np.ndarray) -> np.ndarray:
    """Rotate by a unimodular constant so that (u p)* = -(u p) (phase -1 gauge)."""
    w = si_phase(p)
    if w is None:
        raise ValueError("polynomial is not self-inversive up to phase")
    u = np.exp(0.5j * np.angle(-w))
    q = u * p
    if np.max(np.abs(si_star(q) + q)) > 1e-8 * np.max(np.abs(q)):
        raise AssertionError("phase alignment failed")
    return q


def schur_szego(f: np.ndarray, g: np.ndarray) -> np.ndarray:
    """(f * g)_k = f_k g_k / binom(n, k) on ascending degree-n arrays: the
    binomial Schur-Szego composition underlying Grace-Szego / Suffridge."""
    n = len(f) - 1
    if len(g) != n + 1:
        raise ValueError("degree mismatch")
    b = np.array([math.comb(n, k) for k in range(n + 1)], dtype=float)
    return np.asarray(f, dtype=complex) * np.asarray(g, dtype=complex) / b


def poly_from_angles(angles) -> np.ndarray:
    """Monic ascending coefficients of prod (z - e^{i a_j})."""
    return np.poly(np.exp(1j * np.asarray(angles, dtype=float)))[::-1].astype(complex)


def verblunsky(n: int, seed: int = 20260701) -> np.ndarray:
    rng = np.random.default_rng(seed)
    r = 0.8 * np.sqrt(rng.uniform(size=n - 1))
    th = rng.uniform(0.0, TWO_PI, size=n - 1)
    return r * np.exp(1j * th)


def suffridge_angles(n: int, rng: np.random.Generator) -> np.ndarray:
    """Random member of S_n: all n circular gaps >= 2pi/(n+1); the slack
    2pi/(n+1) is spread randomly, then the configuration is randomly rotated."""
    lo = TWO_PI / (n + 1)
    slack = rng.random(n)
    slack = slack / slack.sum() * (TWO_PI - n * lo)
    gaps = lo + slack
    start = rng.uniform(0.0, TWO_PI)
    return np.mod(start + np.concatenate(([0.0], np.cumsum(gaps[:-1]))), TWO_PI)


def violating_angles(n: int, rng: np.random.Generator, tight: float) -> np.ndarray:
    """Circle-rooted but NOT in S_n: one gap = tight < 2pi/(n+1), the others
    >= 2pi/(n+1). The mesh is exactly `tight`."""
    lo = TWO_PI / (n + 1)
    if not 0.0 < tight < lo:
        raise ValueError("tight must violate the Suffridge bound")
    rest = TWO_PI - tight - (n - 1) * lo          # = 2 lo - tight > 0
    slack = rng.random(n - 1)
    slack = slack / slack.sum() * rest
    gaps = np.concatenate(([tight], lo + slack))
    start = rng.uniform(0.0, TWO_PI)
    return np.mod(start + np.concatenate(([0.0], np.cumsum(gaps[:-1]))), TWO_PI)


def alternates(angles_a, angles_b) -> bool:
    """Strict cyclic alternation of two angle sets around the circle."""
    pts = [(float(np.mod(a, TWO_PI)), 0) for a in np.atleast_1d(angles_a)]
    pts += [(float(np.mod(b, TWO_PI)), 1) for b in np.atleast_1d(angles_b)]
    pts.sort()
    labels = [lab for _, lab in pts]
    return all(labels[i] != labels[(i + 1) % len(labels)] for i in range(len(labels)))


# ---------------------------------------------------------------------------
# Test 1  The known circle interlacing family (POPUC beta-pencil).
# ---------------------------------------------------------------------------
def test_1_popuc_pencil() -> bool:
    print("Test 1  POPUC beta-pencil: circle-rooted on a beta grid + pairwise interlacing")
    alphas = verblunsky(N)
    betas = np.exp(1j * (0.25 + TWO_PI * np.arange(6) / 6))
    zero_sets, defects, phase_errs = [], [], []
    for b in betas:
        B = para_orthogonal(alphas, b)
        z = poly_zeros_ascending(B)
        zero_sets.append(sorted_angles(z))
        defects.append(circle_defect(z))
        w = si_phase(B)
        phase_errs.append(abs(w + b) if w is not None else np.inf)
    n_pairs, n_alt = 0, 0
    for i, j in itertools.combinations(range(len(betas)), 2):
        n_pairs += 1
        n_alt += int(alternates(zero_sets[i], zero_sets[j]))
    print(f"    6 betas on the unit circle, n = {N}, seeded Verblunsky (|alpha| <= 0.8)")
    print(f"    circle defect max over betas      = {max(defects):.2e}")
    print(f"    phase lemma B* = -beta B, max err = {max(phase_errs):.2e}")
    print(f"    pairwise interlacing              = {n_alt}/{n_pairs} pairs alternate")
    return max(defects) < 1e-7 and max(phase_errs) < 1e-7 and n_alt == n_pairs


# ---------------------------------------------------------------------------
# Test 2  The pencil-combination test (the circle Hermite-Biehler question).
# ---------------------------------------------------------------------------
def test_2_pencil_combination() -> bool:
    print("Test 2  Convex combinations of interlacing POPUC members: the phase gauge")
    alphas = verblunsky(N)
    phi = szego_phi(alphas)
    b1, b2 = np.exp(0.9j), np.exp(2.7j)
    B1, B2 = para_orthogonal(alphas, b1), para_orthogonal(alphas, b2)
    z1, z2 = poly_zeros_ascending(B1), poly_zeros_ascending(B2)
    inter = alternates(sorted_angles(z1), sorted_angles(z2))
    print(f"    endpoints interlace strictly: {inter}")

    # (a) NAIVE real convex combination: provably exits the circle at every
    # interior lam. Identity: lam B1 + (1-lam) B2 = z Phi - c Phi* with
    # c = lam conj(b1) + (1-lam) conj(b2), |c| < 1, and the degree-n Blaschke
    # b(z) = z Phi / Phi* solves b = c only strictly inside the disk.
    ident_ok, margins, cmods = True, [], []
    for lam in np.arange(0.1, 0.91, 0.1):
        P = lam * B1 + (1.0 - lam) * B2
        c = lam * np.conj(b1) + (1.0 - lam) * np.conj(b2)
        ident_ok = ident_ok and bool(np.allclose(P, szego_step(phi, np.conj(c)), atol=1e-10))
        z = poly_zeros_ascending(P)
        margins.append(1.0 - float(np.max(np.abs(z))))
        cmods.append(abs(c))
    print(f"    naive lam B1 + (1-lam) B2 == z Phi - c Phi* (identity check): {ident_ok}")
    print(f"    |c| over interior lam in [{min(cmods):.4f}, {max(cmods):.4f}]  (< 1: Blaschke)")
    print("    inside margin 1 - max|root| at lam = 0.1 .. 0.9:")
    print("      " + "  ".join(f"{m:.4f}" for m in margins))
    naive_exits = min(margins) > 1e-4
    print(f"    -> ALL roots strictly inside at EVERY interior lam: {naive_exits}")
    print("       (the expected circle Hermite-Biehler positive FAILS in naive form;")
    print("        linear averaging leaves the locus, the #143 mechanism)")

    # (b) PHASE-ALIGNED combination: rotate each member to phase -1; the same
    # real combination is then D * B(.; D/conj(D)) with D on a chord and
    # beta_eff = D/conj(D) unimodular: the pencil is the POPUC ARC.
    u1, u2 = np.exp(0.5j * np.angle(b1)), np.exp(0.5j * np.angle(b2))
    gauge_ok = (np.max(np.abs(si_star(u1 * B1) + u1 * B1)) < 1e-9
                and np.max(np.abs(si_star(u2 * B2) + u2 * B2)) < 1e-9)
    arc_ok, aligned_defects = True, []
    for lam in np.linspace(0.0, 1.0, 21):
        D = lam * u1 + (1.0 - lam) * u2
        P = lam * u1 * B1 + (1.0 - lam) * u2 * B2
        beta_eff = D / np.conj(D)
        arc_ok = arc_ok and bool(np.allclose(P, D * para_orthogonal(alphas, beta_eff),
                                             atol=1e-9))
        aligned_defects.append(circle_defect(poly_zeros_ascending(P)))
    print(f"    aligned gauge (u B)* = -(u B) for both members: {gauge_ok}")
    print(f"    aligned combo == D * B(.; D/conj(D)), beta_eff unimodular: {arc_ok}")
    print(f"    aligned circle defect, max over lam in [0,1]: {max(aligned_defects):.2e}")
    print("    -> the correct circle Hermite-Biehler pencil is the ARC (gauge-fixed),")
    print("       not the chord: convexity happens in beta on the circle.")
    return inter and ident_ok and naive_exits and gauge_ok and arc_ok \
        and max(aligned_defects) < 1e-7


# ---------------------------------------------------------------------------
# Test 3  Interlacing vs non-interlacing control (aligned gauge for both).
# ---------------------------------------------------------------------------
def _aligned_combo_defects(f: np.ndarray, g: np.ndarray, grid: int = 81):
    defects = []
    for lam in np.linspace(0.0, 1.0, grid):
        P = lam * f + (1.0 - lam) * g
        if abs(P[-1]) < 1e-8:            # degree drop; skip the degenerate point
            continue
        defects.append((float(lam), circle_defect(poly_zeros_ascending(P))))
    return defects


def test_3_noninterlacing_control() -> bool:
    print("Test 3  Control: aligned convex combos, interlacing vs NON-interlacing pair")
    # non-interlacing pair: two antipodal 3-clusters each.
    fa = np.array([0.0, 0.12, 0.24, 3.0, 3.12, 3.24])
    ga = np.array([1.5, 1.62, 1.74, 4.5, 4.62, 4.74])
    non_inter = not alternates(fa, ga)
    f = align_phase(poly_from_angles(fa))
    g = align_phase(poly_from_angles(ga))
    dn = _aligned_combo_defects(f, g)
    lam_bad, worst = max(dn, key=lambda t: t[1])
    print(f"    non-interlacing pair (two 3-clusters each): alternation = {not non_inter}")
    print(f"    worst circle defect along lam: {worst:.4f} at lam = {lam_bad:.3f}")
    control_fails = worst > 1e-3

    # interlacing pair (NOT from a POPUC pencil): evens/odds of 12 random angles.
    rng = np.random.default_rng(7)
    merged = np.sort(rng.uniform(0.0, TWO_PI, 12))
    fa2, ga2 = merged[0::2], merged[1::2]
    inter = alternates(fa2, ga2)
    f2 = align_phase(poly_from_angles(fa2))
    g2 = align_phase(poly_from_angles(ga2))
    di = _aligned_combo_defects(f2, g2)
    worst_i = max(d for _, d in di)
    print(f"    interlacing pair (evens/odds of 12 random angles): alternation = {inter}")
    print(f"    worst circle defect along lam: {worst_i:.2e}")
    hb_holds = worst_i < 1e-6
    print("    -> circle Hermite-Biehler dichotomy (aligned gauge): interlacing =>")
    print("       convex-stable on the locus; non-interlacing => the combination")
    print("       can leave the circle. Same shape as the line (Obreschkoff).")
    return non_inter and control_fails and inter and hb_holds


# ---------------------------------------------------------------------------
# Test 4  Mesh along the aligned pencil: IVT fails, the cell floor holds.
# ---------------------------------------------------------------------------
def _matched_ahead(a_from: np.ndarray, a_to: np.ndarray) -> np.ndarray:
    out = []
    for x in a_from:
        d = np.mod(a_to - x, TWO_PI)
        d[d < 1e-12] = TWO_PI
        out.append(a_to[int(np.argmin(d))])
    return np.array(out)


def _matched_behind(a_from: np.ndarray, a_to: np.ndarray) -> np.ndarray:
    out = []
    for x in a_from:
        d = np.mod(x - a_to, TWO_PI)
        d[d < 1e-12] = TWO_PI
        out.append(a_to[int(np.argmin(d))])
    return np.array(out)


def pencil_floor(z_start, z_end, direction: int) -> float:
    """Merged-endpoint floor: each zero travels monotonically inside the cell
    cut out by its lam = 0 and lam = 1 positions (zero monotonicity in arg
    beta + interlacing), so mesh(lam) >= min gap between consecutive cells."""
    a0, a1 = sorted_angles(z_start), sorted_angles(z_end)
    if direction > 0:
        partner = _matched_ahead(a0, a1)         # cell_j = [a0_j, partner_j]
        gaps = np.mod(np.roll(a0, -1) - partner, TWO_PI)
    else:
        partner = _matched_behind(a0, a1)        # cell_j = [partner_j, a0_j]
        gaps = np.mod(partner - np.roll(a0, 1), TWO_PI)
    return float(np.min(gaps))


def _motion_direction(z_a, z_b) -> int:
    aa, ab = sorted_angles(z_a), sorted_angles(z_b)
    moves = []
    for x in aa:
        d = np.mod(ab - x + np.pi, TWO_PI) - np.pi
        moves.append(d[int(np.argmin(np.abs(d)))])
    return 1 if float(np.median(moves)) > 0 else -1


def test_4_mesh_along_pencil() -> bool:
    print("Test 4  mesh(lam) along the aligned pencil: IVT vs the cell floor")
    n_seeds, grid = 12, 101
    ivt_viols, floor_ok_all, consistency = [], True, True
    worst_ivt, worst_seed = 0.0, -1
    for seed in range(n_seeds):
        alphas = verblunsky(N, seed=1000 + seed)
        rng = np.random.default_rng(500 + seed)
        tb = rng.uniform(0.0, TWO_PI, 2)
        b1, b2 = np.exp(1j * tb[0]), np.exp(1j * tb[1])
        B1, B2 = para_orthogonal(alphas, b1), para_orthogonal(alphas, b2)
        u1, u2 = np.exp(0.5j * tb[0]), np.exp(0.5j * tb[1])
        path_zeros, path_mesh = [], []
        for lam in np.linspace(0.0, 1.0, grid):
            D = lam * u1 + (1.0 - lam) * u2
            if abs(D) < 1e-6:
                continue
            P = lam * u1 * B1 + (1.0 - lam) * u2 * B2
            z = poly_zeros_ascending(P)
            consistency = consistency and circle_defect(z) < 1e-6
            path_zeros.append(z)
            path_mesh.append(mesh(z))
        m0, m1 = path_mesh[0], path_mesh[-1]
        m_min = min(path_mesh)
        deficit = m_min - min(m0, m1)            # < 0 means the IVT bound fails
        direction = _motion_direction(path_zeros[0], path_zeros[1])
        F = pencil_floor(path_zeros[0], path_zeros[-1], direction)
        floor_ok = m_min >= F - 1e-7
        floor_ok_all = floor_ok_all and floor_ok
        if deficit < -1e-9:
            ivt_viols.append(seed)
        if deficit < worst_ivt:
            worst_ivt, worst_seed = deficit, seed
        print(f"    seed {seed:2d}: mesh ends ({m0:.4f}, {m1:.4f})  min path {m_min:.4f}"
              f"  IVT deficit {deficit:+.4f}  floor {F:.4f}"
              f"  floor holds {floor_ok}")
    decisive = worst_ivt < -1e-6 or len(ivt_viols) == 0
    print(f"    IVT bound mesh(lam) >= min(endpoints): FAILS on {len(ivt_viols)}/{n_seeds}"
          f" paths (worst deficit {worst_ivt:+.4f}, seed {worst_seed})")
    print(f"    cell floor mesh(lam) >= merged-endpoint gap: holds on {n_seeds}/{n_seeds}"
          f" = {floor_ok_all}")
    print("    -> quasi-concavity of mesh along the pencil is FALSE; the correct")
    print("       statement is the cell floor (provable from zero monotonicity +")
    print("       interlacing). Candidate small theorem, spacing-axis only.")
    return consistency and floor_ok_all and decisive and len(ivt_viols) > 0


# ---------------------------------------------------------------------------
# Test 5  Convolution convention: the identity is (1+z)^n; z^n - 1 projects.
# ---------------------------------------------------------------------------
def test_5_convention() -> bool:
    print("Test 5  Schur-Szego convention: identity element and the z^n - 1 projector")
    rng = np.random.default_rng(11)
    f = poly_from_angles(suffridge_angles(N, rng))
    one = np.array([math.comb(N, k) for k in range(N + 1)], dtype=complex)   # (1+z)^n
    runity = np.zeros(N + 1, dtype=complex)
    runity[0], runity[N] = -1.0, 1.0                                          # z^n - 1
    id_err = float(np.max(np.abs(schur_szego(f, one) - f)))
    not_id_err = float(np.max(np.abs(schur_szego(f, runity) - f)))
    h = schur_szego(f, runity)
    pred = np.zeros(N + 1, dtype=complex)
    pred[0], pred[N] = -f[0], f[N]
    proj_err = float(np.max(np.abs(h - pred)))
    zh = poly_zeros_ascending(h)
    print(f"    f * (1+z)^n = f exactly:      max err = {id_err:.2e}  (the identity)")
    print(f"    f * (z^n - 1) = f ?           max err = {not_id_err:.3f}  (NOT an identity:")
    print("      the task-suggested convention check FAILS; convention corrected)")
    print(f"    f * (z^n - 1) = f_n z^n - f_0: max err = {proj_err:.2e}")
    print(f"    its zeros: circle defect = {circle_defect(zh):.2e},"
          f" mesh = {mesh(zh):.6f} vs 2pi/n = {MAX_MESH:.6f}")
    print("    -> z^n - 1 is the PROJECTOR onto the equal-spacing extremal point.")
    return id_err < 1e-12 and not_id_err > 0.5 and proj_err < 1e-12 \
        and circle_defect(zh) < 1e-9 and abs(mesh(zh) - MAX_MESH) < 1e-9


# ---------------------------------------------------------------------------
# Test 6  Suffridge preservation + unconditional locus preservation.
# ---------------------------------------------------------------------------
def test_6_preservation() -> bool:
    print("Test 6  Composition preserves S_n (Suffridge) and the locus unconditionally")
    rng = np.random.default_rng(20260630)
    n_pairs = 60
    worst_def, worst_mesh, ge_max = 0.0, np.inf, 0
    for _ in range(n_pairs):
        af, ag = suffridge_angles(N, rng), suffridge_angles(N, rng)
        h = schur_szego(poly_from_angles(af), poly_from_angles(ag))
        zh = poly_zeros_ascending(h)
        worst_def = max(worst_def, circle_defect(zh))
        mh = mesh(zh)
        worst_mesh = min(worst_mesh, mh)
        ge_max += int(mh >= max(mesh_angles(af), mesh_angles(ag)) - 1e-9)
    suff_ok = worst_def < 1e-6 and worst_mesh >= THRESH - 1e-7
    print(f"    {n_pairs} random S_{N} pairs: max circle defect = {worst_def:.2e},")
    print(f"    min output mesh = {worst_mesh:.6f} >= 2pi/(n+1) = {THRESH:.6f}: {suff_ok}")
    print(f"    output mesh >= max(input meshes) on {ge_max}/{n_pairs} pairs")

    worst_def_u = 0.0
    for _ in range(n_pairs):
        af = np.sort(rng.uniform(0.0, TWO_PI, N))
        ag = np.sort(rng.uniform(0.0, TWO_PI, N))
        h = schur_szego(poly_from_angles(af), poly_from_angles(ag))
        worst_def_u = max(worst_def_u, circle_defect(poly_zeros_ascending(h)))
    print(f"    {n_pairs} ARBITRARY circle-rooted pairs (no mesh bound): max defect"
          f" = {worst_def_u:.2e}")
    print("    -> the LOCUS is preserved unconditionally (Grace-Szego keeps the")
    print("       closed disk; self-inversiveness of the composition then forbids")
    print("       interior roots). The mesh hypothesis is not about the locus.")
    return suff_ok and worst_def_u < 1e-5


# ---------------------------------------------------------------------------
# Test 7  Boundary and teeth: sub-threshold inputs, min-monotonicity probe.
# ---------------------------------------------------------------------------
def test_7_boundary_and_teeth() -> bool:
    print("Test 7  Boundary members, sub-threshold teeth, mesh min-monotonicity")
    rng = np.random.default_rng(31)

    # boundary member: seven gaps exactly 2pi/(n+1), one gap 2 * 2pi/(n+1).
    gaps = np.array([THRESH] * (N - 1) + [2.0 * THRESH])
    ab = np.mod(0.4 + np.concatenate(([0.0], np.cumsum(gaps[:-1]))), TWO_PI)
    fb = poly_from_angles(ab)
    hb = schur_szego(fb, fb)
    zb = poly_zeros_ascending(hb)
    print(f"    boundary member (mesh exactly {THRESH:.6f}): f*f mesh = {mesh(zb):.6f},"
          f" defect = {circle_defect(zb):.2e}")
    boundary_ok = circle_defect(zb) < 1e-7 and mesh(zb) >= THRESH - 1e-7

    # roots of unity compose to roots of unity: (z^n - 1) * (z^n - 1) = z^n + 1.
    runity = np.zeros(N + 1, dtype=complex)
    runity[0], runity[N] = -1.0, 1.0
    hru = schur_szego(runity, runity)
    ru_ok = np.allclose(hru, np.array([1.0] + [0.0] * (N - 1) + [1.0]), atol=1e-12)
    print(f"    (z^n - 1) * (z^n - 1) = z^n + 1 exactly: {ru_ok}  (max-mesh fixed shape)")

    # sub-threshold probe A: ONE violating gap per input. SURPRISE: a single
    # sub-threshold gap is REPAIRED above the bound by one composition, every
    # time (the composition is strongly smoothing).
    n_trials = 300
    below_out, min_deficit, min_out_mesh = 0, np.inf, np.inf
    worst_def = 0.0
    for _ in range(n_trials):
        tf = rng.uniform(0.1, 0.9) * THRESH
        tg = rng.uniform(0.1, 0.9) * THRESH
        af, ag = violating_angles(N, rng, tf), violating_angles(N, rng, tg)
        h = schur_szego(poly_from_angles(af), poly_from_angles(ag))
        zh = poly_zeros_ascending(h)
        worst_def = max(worst_def, circle_defect(zh))
        mh = mesh(zh)
        min_out_mesh = min(min_out_mesh, mh)
        below_out += int(mh < THRESH - 1e-9)
        min_deficit = min(min_deficit, mh - min(mesh_angles(af), mesh_angles(ag)))
    singles_repaired = below_out == 0
    print(f"    {n_trials} single-violating-gap pairs (one gap in (0.1, 0.9) * 2pi/(n+1)):")
    print(f"      output below the Suffridge bound on {below_out}/{n_trials} pairs;"
          f" min output mesh = {min_out_mesh:.4f}")
    print("      SURPRISE: one composition REPAIRS any single sub-threshold gap")
    print(f"      (expected 'preservation can fail' did not occur here);"
          f" max defect = {worst_def:.2e}")

    # sub-threshold probe B: CLUSTERED violations. Here the teeth show: the
    # output stays far below the bound (class below threshold is NOT closed).
    cluster_rows, cluster_teeth = [], False
    for e in (0.02, 0.05, 0.1, 0.2):             # whole-cluster inputs, mesh = e
        ac = np.arange(N) * e
        bc = np.arange(N) * e + 2.0
        h = schur_szego(poly_from_angles(ac), poly_from_angles(bc))
        mo = mesh(poly_zeros_ascending(h))
        cluster_rows.append((e, mo))
        cluster_teeth = cluster_teeth or mo < THRESH - 1e-6
        min_deficit = min(min_deficit, mo - e)
    print("    whole-cluster pairs (all 8 roots in an arc, input mesh = eps):")
    print("      " + "  ".join(f"eps={e:.2f} -> {m:.4f} (x{m / e:.2f})"
                               for e, m in cluster_rows))
    print(f"      TEETH: output mesh stays below the bound {THRESH:.4f} (class not")
    print("      closed below threshold), yet grows by a stable factor ~1.36.")

    # multi-tight-gap search (2 to 4 violating gaps per input).
    worst_multi = np.inf
    for _ in range(200):
        k = int(rng.integers(2, 5))
        tight = rng.uniform(0.02, 0.3, k)
        rest = TWO_PI - tight.sum() - (N - k) * THRESH
        if rest <= 0:
            continue
        sl = rng.random(N - k)
        gaps = np.concatenate([tight, THRESH + sl / sl.sum() * rest])
        rng.shuffle(gaps)
        af = np.mod(np.concatenate(([0.0], np.cumsum(gaps[:-1]))), TWO_PI)
        ag = np.mod(rng.uniform(0, TWO_PI)
                    + np.concatenate(([0.0], np.cumsum(np.roll(gaps, 3)[:-1]))), TWO_PI)
        h = schur_szego(poly_from_angles(af), poly_from_angles(ag))
        mo = mesh(poly_zeros_ascending(h))
        worst_multi = min(worst_multi, mo)
        min_deficit = min(min_deficit, mo - min(mesh_angles(af), mesh_angles(ag)))
    print(f"    multi-tight-gap search (200 pairs, 2-4 violating gaps): min output"
          f" mesh = {worst_multi:.4f} (teeth again)")

    # iterated self-composition of a violator: escapes the violation geometrically.
    av = violating_angles(N, np.random.default_rng(3), 0.2)
    fv = poly_from_angles(av)
    traj, h = [mesh_angles(av)], fv
    for _ in range(6):
        h = schur_szego(h, fv)
        traj.append(mesh(poly_zeros_ascending(h)))
    print("    iterated f^(*k), f a 0.2-gap violator: mesh trajectory")
    print("      " + " -> ".join(f"{m:.4f}" for m in traj))
    mono_supported = min_deficit > -1e-6
    print(f"    min-monotonicity deficit mesh(f*g) - min(mesh f, mesh g), global"
          f" min = {min_deficit:+.4f}")
    print(f"    -> mesh min-monotonicity: "
          f"{'SUPPORTED, no counterexample found' if mono_supported else 'FALSE, counterexample above'}"
          f" (conjecture; Suffridge closure is the threshold case)")
    return boundary_ok and ru_ok and singles_repaired and cluster_teeth \
        and worst_multi < THRESH - 1e-3 and worst_def < 1e-5 and mono_supported


# ---------------------------------------------------------------------------
# Test 8  THE ENGINE TEST: three averaging modes on a Suffridge family.
# ---------------------------------------------------------------------------
def test_8_engine() -> bool:
    print("Test 8  The MSS-shape question at the mesh axis (R = 40 Suffridge members)")
    R = 40
    rng = np.random.default_rng(20260701)
    angle_sets = [suffridge_angles(N, rng) for _ in range(R)]
    polys = [poly_from_angles(a) for a in angle_sets]
    member_mesh = np.array([mesh_angles(a) for a in angle_sets])
    print(f"    member meshes: min {member_mesh.min():.4f}  max {member_mesh.max():.4f}"
          f"  (band [{THRESH:.4f}, {MAX_MESH:.4f}))")

    # (iii) common interlacing across the family?
    n_pairs, n_alt = 0, 0
    for i, j in itertools.combinations(range(R), 2):
        n_pairs += 1
        n_alt += int(alternates(angle_sets[i], angle_sets[j]))
    print(f"    (iii) pairwise alternation: {n_alt}/{n_pairs} pairs"
          f" (fraction {n_alt / n_pairs:.3f}): the class is RIGID (every member")
    print("        is a jittered rotated roots-of-unity set) so alternation is")
    print("        common, but not universal: no common interlacing across the family")

    # Mode A: coefficient mean, raw and phase-aligned.
    mean_raw = np.mean(polys, axis=0)
    def_raw = circle_defect(poly_zeros_ascending(mean_raw))
    aligned = [align_phase(p) for p in polys]
    mean_al = np.mean(aligned, axis=0)
    z_al = poly_zeros_ascending(mean_al)
    def_al = circle_defect(z_al)
    mesh_al = mesh(z_al)
    n_ge_al = int(np.sum(member_mesh >= mesh_al))
    print(f"    (A) coefficient mean: raw defect = {def_raw:.4f} (off the locus);")
    print(f"        phase-ALIGNED mean defect = {def_al:.2e}: SURPRISE, circle-rooted")
    print(f"        at machine precision, mesh = {mesh_al:.4f}; members with mesh >=")
    print(f"        mesh(aligned mean): {n_ge_al}/{R} (selection reversed here too)")
    # the surprise is probabilistic rigidity, not a theorem: pairwise it is
    # exactly the HB dichotomy, and outside the Suffridge class it dies.
    worst_pair_non, n_non, n_non_fail = 0.0, 0, 0
    rng_p = np.random.default_rng(123)
    for _ in range(150):
        a, b = suffridge_angles(N, rng_p), suffridge_angles(N, rng_p)
        if alternates(a, b):
            continue
        n_non += 1
        f2, g2 = align_phase(poly_from_angles(a)), align_phase(poly_from_angles(b))
        wd = 0.0
        for lam in np.linspace(0.0, 1.0, 41):
            P = lam * f2 + (1.0 - lam) * g2
            if abs(P[-1]) < 1e-9:
                continue
            wd = max(wd, circle_defect(poly_zeros_ascending(P)))
        n_non_fail += int(wd > 1e-6)
        worst_pair_non = max(worst_pair_non, wd)
    rng_u = np.random.default_rng(10)
    mean_arb = np.mean([align_phase(poly_from_angles(
        np.sort(rng_u.uniform(0.0, TWO_PI, N)))) for _ in range(R)], axis=0)
    def_arb = circle_defect(poly_zeros_ascending(mean_arb))
    print(f"        but NOT a theorem: of {n_non} non-alternating in-class pairs,")
    print(f"        {n_non_fail} exit the circle under aligned convex combination")
    print(f"        (worst defect {worst_pair_non:.2f}; most are convex-stable anyway,")
    print("        the rigidity again), and the aligned mean of 40 ARBITRARY")
    print(f"        circle-rooted members has defect {def_arb:.2f}:")
    print("        the 40-member stability is probabilistic rigidity of S_n")
    print("        (members are perturbations of c cos(nt/2 + phi); random phases")
    print("        rarely cancel the leading term), not an engine ingredient.")
    mode_a = (def_raw > 1e-3 and def_al < 1e-9 and worst_pair_non > 1e-2
              and def_arb > 1e-2 and n_ge_al == 0)

    # Mode B: iterated Suffridge composition (associative, order-free).
    comp = reduce(schur_szego, polys)
    zc = poly_zeros_ascending(comp)
    def_b, mesh_b = circle_defect(zc), mesh(zc)
    binom = np.array([math.comb(N, k) for k in range(N + 1)], dtype=float)
    mid = np.max(np.abs((comp / binom)[1:N]))
    traj = []
    for k in (2, 5, 10, 20, 40):
        ck = reduce(schur_szego, polys[:k])
        traj.append((k, mesh(poly_zeros_ascending(ck))))
    print(f"    (B) iterated composition: defect = {def_b:.2e}, mesh = {mesh_b:.6f}"
          f" (2pi/n = {MAX_MESH:.6f})")
    print(f"        max middle |A_k| after 40 compositions = {mid:.2e} (contraction)")
    print("        mesh after k compositions: "
          + "  ".join(f"k={k}: {m:.4f}" for k, m in traj))
    n_ge = int(np.sum(member_mesh >= mesh_b))
    n_below = int(np.sum(member_mesh < mesh_b))
    print(f"        selection test 'exists member with mesh >= mesh(average)':"
          f" {n_ge}/{R} members qualify")
    print(f"        (non-vacuous: {n_below}/{R} strictly below; the average"
          f" out-meshes EVERY member)")
    mode_b_ok = def_b < 1e-6 and mesh_b >= THRESH - 1e-9
    selection_reversed = n_ge == 0 and n_below == R

    # Mode C: smooth each member with the z^n - 1 kernel, then coefficient-mean.
    runity = np.zeros(N + 1, dtype=complex)
    runity[0], runity[N] = -1.0, 1.0
    smoothed = [schur_szego(p, runity) for p in polys]
    proj_err = max(float(np.max(np.abs(s - np.concatenate(([-p[0]], np.zeros(N - 1), [p[N]])))))
                   for s, p in zip(smoothed, polys))
    mean_c = np.mean(smoothed, axis=0)
    cval = -mean_c[0]
    radius = abs(cval) ** (1.0 / N)
    def_c = circle_defect(poly_zeros_ascending(mean_c))
    print(f"    (C) z^n - 1 kernel: each smoothed member = f_n z^n - f_0 exactly"
          f" (err {proj_err:.1e});")
    print(f"        mean = z^n - c with |c| = {abs(cval):.4f} < 1: roots on radius"
          f" {radius:.4f}, defect = {def_c:.4f}")
    print("        -> literally the #143 collapse: the kernel projects onto the")
    print("        extremal point and the linear mean of unimodular constants")
    print("        pulls inside the disk. Locus lost.")
    mode_c_off = abs(cval) < 1.0 - 1e-3 and def_c > 1e-3

    print("    ENGINE VERDICT: the guaranteed locus-preserving average (B) is a")
    print("    CONTRACTION toward equal spacing: it out-meshes every member and")
    print("    forgets the family; the aligned linear mean stays on the locus only")
    print("    by class rigidity (pairwise it needs interlacing) and ALSO out-meshes")
    print("    every member; raw and kernel means leave the locus. In every mode the")
    print("    MSS selection inequality is false or unavailable: no MSS-shape engine")
    print("    exists at the mesh axis.")
    return mode_a and mode_b_ok and selection_reversed and mode_c_off \
        and proj_err < 1e-12 and 0 < n_alt < n_pairs


# ---------------------------------------------------------------------------
# Test 9  The screens.
# ---------------------------------------------------------------------------
def test_9_screens() -> bool:
    print("Test 9  Screens: mesh presupposes the locus; wrong axis for M4")
    rng = np.random.default_rng(99)
    a = suffridge_angles(N, rng)
    z = np.exp(1j * a)
    m0 = mesh_angles(np.angle(z))
    z_pert = z.copy()
    z_pert[3] *= 1.3                              # radially off the circle, same angle
    p_pert = np.poly(z_pert)[::-1].astype(complex)
    d_pert = circle_defect(z_pert)
    m_pert = mesh_angles(np.angle(z_pert))
    si_lost = si_phase(p_pert) is None
    print(f"    (a) presupposes-the-locus: root 3 moved to radius 1.3 (same angle):")
    print(f"        circle defect {0.0:.1f} -> {d_pert:.2f};  angle-projected mesh"
          f" {m0:.6f} -> {m_pert:.6f} (unchanged: {abs(m0 - m_pert) < 1e-12})")
    print(f"        self-inversiveness lost: {si_lost}")
    print("        -> mesh is RADIALLY BLIND: it orders configurations WITHIN the")
    print("        circle locus and cannot certify TOWARD it. Any mesh theorem")
    print("        assumes what M4 must produce.")
    print("    (b) wrong-axis (#120): mesh is a SPACING statistic (Level-3-adjacent,")
    print("        the GUE/pair-correlation axis), not root LOCATION. An H2 theorem")
    print("        is a circle-side interlacing-family result about spacing; it is")
    print("        NOT an M4 route, by construction.")
    return abs(m0 - m_pert) < 1e-12 and d_pert > 0.29 and si_lost


# ---------------------------------------------------------------------------
# The battery.
# ---------------------------------------------------------------------------
TESTS = [
    test_1_popuc_pencil,
    test_2_pencil_combination,
    test_3_noninterlacing_control,
    test_4_mesh_along_pencil,
    test_5_convention,
    test_6_preservation,
    test_7_boundary_and_teeth,
    test_8_engine,
    test_9_screens,
]


def main() -> None:
    print("Suffridge-mesh engine probe (H2 from LEARNINGS #143)\n")
    passed, total = 0, 0
    for t in TESTS:
        total += 1
        ok = t()
        passed += int(ok)
        print(f"  -> {'PASS' if ok else 'FAIL'}\n")
    print("=" * 78)
    print("Verdict: two of the three MSS organs exist at the mesh axis (Suffridge")
    print("semigroup + POPUC interlacing order), but the engine does not assemble:")
    print("linear averaging exits the circle at every interior point (provably, via")
    print("the Blaschke pencil), the phase-aligned mean is the POPUC arc (interlacing")
    print("<=> convex stability, the circle Hermite-Biehler), and the only")
    print("locus-preserving average (the Suffridge composition) is a contraction onto")
    print("the equal-spacing extremal point that out-meshes every member, so the MSS")
    print("selection inequality is decisively reversed (the aligned linear mean, kept")
    print("on the locus only by class rigidity, reverses it too). Positive residue:")
    print("the pencil cell floor (Test 4), mesh min-monotonicity of the composition")
    print("(Test 7), and the one-composition repair of single sub-threshold gaps")
    print("(Test 7), all spacing-axis candidates, none an M4 route (Test 9).")
    print(f"\n{passed}/{total} suffridge_mesh tests passed.")
    if passed != total:
        sys.exit(1)


if __name__ == "__main__":
    main()
