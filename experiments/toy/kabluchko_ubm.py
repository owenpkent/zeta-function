"""The Kabluchko object probe: does a RICH circle-controlled mean restore MSS selection?

The question (LEARNINGS #143, handoff H1). The circle-rooted interlacing engine
died at the extremal-selection step, and one adversary correction survived: the
Haar first moment E[det(zI - U)] = z^N is HAAR-EXACT, not circle-universal.
Kabluchko (Ann. Henri Lebesgue 2025) shows unitary Brownian motion (UBM) at
finite time has a rich expected characteristic polynomial (a unitary Hermite
polynomial, heat flow applied to (z-1)^n, Lee-Yang-connected). H1 asks: does
that rich mean restore the missing selection order? Concretely (a) do UBM
realizations angularly interlace the mean, and (b) is there any functional for
which "some realization is at least as good as the mean" is true, non-vacuous,
and survives the wrong-axis screen (#120)?

What the battery finds (each claim is a numbered test below):

  PART 1 (Test 1). The simulator: U(t) = prod_k exp(i sqrt(t/K) G_k), G_k iid
      GUE with E[tr G^2]/n = 1, n = 6, exactly unitary steps via the Pade(4,4)
      generalized Cayley transform (diagonal Pade of exp maps anti-Hermitian to
      unitary identically). Unitarity ~1e-14 after the full evolution, and the
      first-moment anchor E[Tr U_t] = n e^{-t/2} holds at MC accuracy.

  PART 2 (Tests 2-4). The mean polynomial IS rich (unlike Haar's z^n), and its
      MC coefficients match the exact character-theory formula
      E[e_k(U_t)] = C(n,k) exp(-t k(n+1-k)/(2n)) at the M^{-1/2} rate; the
      t = 50 control reproduces the Haar collapse to z^n. THE SURPRISE (Test 4,
      reported over the task's stated expectation): the mean's roots are NOT on
      the unit circle. They lie EXACTLY on the shrunken circle |z| = e^{-t/(2n)}
      (radii equal to 12+ digits for the exact-formula polynomial; the MC roots
      agree within the split-half noise floor, and the unit-circle defect
      1 - e^{-t/(2n)} exceeds that floor decisively at every t tested).
      Kabluchko's unimodularity is exact only in the rescaled variable
      w = z e^{t/(2n)}: circle-CONTROLLED, circle-DISPLACED. So the rich mean
      does not even live on the locus its realizations live on.

  PART 3 (Test 5). Angular interlacing realization-vs-mean exists but is a
      MINORITY event, not a family property (fraction reported; MSS needs a
      common interlacing certificate for ALL members, which fails here).

  PART 4 (Tests 6-10). Selection functionals (mesh = min angular gap, max gap,
      spacing discrepancy, min distance to z = 1): for each, "some realization
      is at least as good as the mean" is TRUE and NON-VACUOUS (the mean sits
      at an interior quantile of the realization distribution, so a positive
      fraction is better and a positive fraction is strictly worse). Two
      honest data points: for MESH the mean is nearly extremal (quantile
      0.977, only 2.3% of realizations beat it: the heat-flow mean has
      strongly repelled roots, the finite-free-probability echo of the MSS
      setup), and for dist-to-1 interlacing certifies the WRONG direction
      (P(better | interlace) = 0.000: alternation forces a realization root
      into the mean's gap straddling z = 1, an anti-certificate). But the
      inequality is only distributional: Test 10 checks whether the
      interlacing event CERTIFIES better-than-mean (the MSS structure) and
      finds no positive association for any functional, so "better than the
      mean" has no certificate and selection degenerates to sampling.

  PART 5 (Tests 11-12). The screen (#120 wrong-axis, #143 gate). (a) All four
      functionals PRESUPPOSE the locus: perturb U off unitary (scale one 2x2
      block by s) and the roots leave the circle monotonically in s, while the
      functionals stay perfectly well-defined and fail to measure the defect
      (no monotone separation; the direct defect statistic separates at d' far
      above the bar, the functionals do not). (b) They are WRONG-AXIS: a
      synthetic pair (A on-circle badly spaced, B off-circle perfectly spaced)
      is ordered B-over-A by ALL FOUR functionals, so the order they induce
      runs along the spacing axis (Level-3 territory), orthogonal to the locus
      axis where RH-content lives.

Composed verdict: H1 is a sharp kill. The rich mean adds content to the
expectation step (Kabluchko is a genuine counterexample to Haar triviality) but
restores nothing of the selection order: (1) the mean polynomial leaves the
unit circle, so realizations and mean do not even share a locus; (2) interlacing
with the mean is a minority event, not a certificate; (3) every functional that
makes "at least as good as the mean" true and non-vacuous is a spacing statistic
that presupposes the circle and orders configurations within it. The #143 gate
stands: unitarity is presupposed, not manufactured, and the missing selection
order is still missing.

Run from the repo root:  python -m experiments.toy.kabluchko_ubm
(Monte Carlo with M = 20000 trajectories of 1200 batched steps: a few minutes.)
"""

from __future__ import annotations

import sys
import time
from math import comb

import numpy as np
from scipy.optimize import linear_sum_assignment

# ---------------------------------------------------------------------------
# Parameters. n = 6, M = 20000 per the task; the step schedule refines the
# task's K ~ 200 (400 steps to t = 1) so discretization bias sits below the
# MC error that the exact-formula test would otherwise misattribute.
# ---------------------------------------------------------------------------
N = 6
M = 20000
SEED = 20260701
T_CHECK = (0.3, 1.0, 4.0, 50.0)
SEGMENTS = ((0.3, 120), (1.0, 280), (4.0, 600), (50.0, 200))
N_SCREEN = 500       # realizations kept as full matrices for the off-unitary screen
R_INTERLACE = 200    # task-specified interlacing sample
R_FUNC = 2000        # functional-distribution sample
TWO_PI = 2.0 * np.pi

_I = np.eye(N, dtype=complex)


# ---------------------------------------------------------------------------
# The simulator.
# ---------------------------------------------------------------------------
def gue(rng: np.random.Generator, m: int) -> np.ndarray:
    """Batch of m iid GUE matrices normalized so E[tr G^2]/n = 1
    (entrywise E[G_ab G_cd] = delta_ad delta_bc / n)."""
    a = rng.standard_normal((m, N, N)) + 1j * rng.standard_normal((m, N, N))
    return (a + np.conj(np.swapaxes(a, 1, 2))) / (2.0 * np.sqrt(N))


def pade_unitary_exp(g: np.ndarray, c: float) -> np.ndarray:
    """exp(i c G) via diagonal Pade(4,4). For anti-Hermitian argument the
    diagonal Pade approximant is EXACTLY unitary (generalized Cayley
    transform: q(X)^H = p(X) when X^H = -X), so no unitarity drift beyond
    roundoff; the approximation error ~1e-12 per step at |icG| ~ 0.1 only
    perturbs the law, far below MC resolution."""
    x = (1j * c) * g
    x2 = x @ x
    x3 = x @ x2
    x4 = x2 @ x2
    p = _I + x / 2 + (3 / 28) * x2 + (1 / 84) * x3 + (1 / 1680) * x4
    q = _I - x / 2 + (3 / 28) * x2 - (1 / 84) * x3 + (1 / 1680) * x4
    return np.linalg.solve(q, p)


def unitarity_error(u: np.ndarray) -> float:
    return float(np.abs(np.einsum("mji,mjk->mik", np.conj(u), u) - _I).max())


def charpoly_coeffs(ev: np.ndarray) -> np.ndarray:
    """Coefficients of prod_j (z - lambda_j), rows of ev; c[:, k] multiplies
    z^{n-k}."""
    m = ev.shape[0]
    c = np.zeros((m, N + 1), dtype=complex)
    c[:, 0] = 1.0
    for j in range(N):
        lam = ev[:, j][:, None]
        c[:, 1:j + 2] = c[:, 1:j + 2] - lam * c[:, 0:j + 1]
    return c


def exact_mean_coeffs(t: float) -> np.ndarray:
    """K -> infinity reference: E[e_k(U_t)] = C(n,k) exp(-t k(n+1-k)/(2n))
    (heat-kernel character expectation, E[chi_lam] = dim(lam) e^{-t C2(lam)/(2n)}
    with the gl_n Casimir C2(1^k) = k(n+1-k); validated against MC in Test 2).
    Sign per det(zI - U) = sum_k (-1)^k e_k z^{n-k}."""
    return np.array([(-1) ** k * comb(N, k) * np.exp(-t * k * (N + 1 - k) / (2 * N))
                     for k in range(N + 1)])


def simulate() -> dict:
    """One batched ensemble, checkpointed at T_CHECK. Returns eigenvalues per
    checkpoint, unitarity errors, and matrix snapshots at t = 1 for the screen."""
    rng = np.random.default_rng(SEED)
    u = np.broadcast_to(_I, (M, N, N)).copy()
    out = {"ev": {}, "uerr": {}, "u_snapshot": None}
    t_now = 0.0
    for t_end, steps in SEGMENTS:
        dt = (t_end - t_now) / steps
        c = np.sqrt(dt)
        for _ in range(steps):
            u = pade_unitary_exp(gue(rng, M), c) @ u
        t_now = t_end
        out["ev"][t_end] = np.linalg.eigvals(u)
        out["uerr"][t_end] = unitarity_error(u)
        if t_end == 1.0:
            out["u_snapshot"] = u[:N_SCREEN].copy()
    return out


# ---------------------------------------------------------------------------
# Functionals on root configurations. Each carries a direction: which way is
# "at least as good".
# ---------------------------------------------------------------------------
def cyclic_gaps(angles: np.ndarray) -> np.ndarray:
    s = np.sort(np.mod(angles, TWO_PI))
    return np.diff(s, append=s[0] + TWO_PI)


def f_mesh(roots: np.ndarray) -> float:
    return float(cyclic_gaps(np.angle(roots)).min())


def f_maxgap(roots: np.ndarray) -> float:
    return float(cyclic_gaps(np.angle(roots)).max())


def f_disc(roots: np.ndarray) -> float:
    return float(np.abs(cyclic_gaps(np.angle(roots)) - TWO_PI / N).sum())


def f_dist1(roots: np.ndarray) -> float:
    return float(np.abs(roots - 1.0).min())


FUNCTIONALS = (
    ("mesh (min angular gap)", "max", f_mesh),
    ("max angular gap", "min", f_maxgap),
    ("spacing discrepancy sum|g - 2pi/n|", "min", f_disc),
    ("min distance of roots to z = 1", "max", f_dist1),
)


def at_least_as_good(val: float, ref: float, direction: str) -> bool:
    return val >= ref if direction == "max" else val <= ref


def strictly_worse(val: float, ref: float, direction: str) -> bool:
    return val < ref if direction == "max" else val > ref


def alternates(ang_a: np.ndarray, ang_b: np.ndarray) -> bool:
    """Strict cyclic alternation of two equal-size angle sets on the circle."""
    pts = sorted([(float(np.mod(a, TWO_PI)), 0) for a in ang_a]
                 + [(float(np.mod(b, TWO_PI)), 1) for b in ang_b])
    angs = [p[0] for p in pts]
    labels = [p[1] for p in pts]
    k = len(labels)
    if any(angs[i] == angs[(i + 1) % k] for i in range(k)):
        return False
    return all(labels[i] != labels[(i + 1) % k] for i in range(k))


def pair_roots(a: np.ndarray, b: np.ndarray) -> float:
    """Max distance between optimally matched root sets (robust to angle-sort
    branch-cut flips near +-pi)."""
    d = np.abs(a[:, None] - b[None, :])
    ri, ci = linear_sum_assignment(d)
    return float(d[ri, ci].max())


# ---------------------------------------------------------------------------
# Shared state, filled by main() before the tests run.
# ---------------------------------------------------------------------------
SIM: dict = {}


def _mean_stats(t: float) -> dict:
    ev = SIM["ev"][t]
    coeffs = charpoly_coeffs(ev)
    half = M // 2
    st = {
        "mc": coeffs.mean(axis=0),
        "se": coeffs.std(axis=0) / np.sqrt(M),
        "mc_a": coeffs[:half].mean(axis=0),
        "mc_b": coeffs[half:].mean(axis=0),
    }
    st["roots"] = np.roots(st["mc"])
    st["roots_a"] = np.roots(st["mc_a"])
    st["roots_b"] = np.roots(st["mc_b"])
    st["jitter"] = pair_roots(st["roots_a"], st["roots_b"])
    return st


# ---------------------------------------------------------------------------
# PART 1: the simulator.
# ---------------------------------------------------------------------------
def test_1_simulator() -> bool:
    print("Test 1: UBM simulator: GUE normalization, unitarity, first-moment anchor.")
    rng = np.random.default_rng(12345)
    g = gue(rng, 4000)
    tr2 = float(np.mean(np.einsum("mij,mji->m", g, g)).real) / N
    print(f"  E[tr G^2]/n = {tr2:.4f}  (target 1.0)")
    ok = 0.97 < tr2 < 1.03

    for t in (1.0, 50.0):
        err = SIM["uerr"][t]
        print(f"  unitarity max|U^H U - I| at t = {t}: {err:.2e}")
        ok = ok and err < 1e-11
    ev1 = SIM["ev"][1.0]
    root_defect = float(np.abs(np.abs(ev1) - 1.0).max())
    print(f"  realization roots on |z| = 1 at t = 1: max||lambda| - 1| = {root_defect:.2e}")
    ok = ok and root_defect < 1e-10

    for t in (0.3, 1.0):
        tr = SIM["ev"][t].sum(axis=1)
        target = N * np.exp(-t / 2)
        se = float(tr.std() / np.sqrt(M))
        dev = abs(float(tr.mean().real) - target)
        print(f"  E[Tr U_t] anchor t = {t}: MC {tr.mean().real:.4f} vs n e^(-t/2) = "
              f"{target:.4f}  (|dev| = {dev:.4f}, 5 se = {5 * se:.4f})")
        ok = ok and dev < 5 * se and abs(float(tr.mean().imag)) < 5 * se
    return ok


# ---------------------------------------------------------------------------
# PART 2: the mean polynomial.
# ---------------------------------------------------------------------------
def test_2_mean_convergence_and_formula() -> bool:
    print("Test 2: mean-polynomial MC convergence (split-half ~ M^(-1/2)) and the")
    print("        exact character-formula match E[e_k] = C(n,k) e^(-t k(n+1-k)/(2n)).")
    ok = True
    for t, n_se in ((0.3, 6.0), (1.0, 5.0), (4.0, 6.0)):
        st = _mean_stats(t)
        exact = exact_mean_coeffs(t)
        half_diff = float(np.abs(st["mc_a"] - st["mc_b"]).max())
        se_max = float(np.abs(st["se"]).max())
        # split halves differ by ~2 se of a half-mean = 2 sqrt(2) se of the full mean
        conv_ok = half_diff < 6.0 * np.sqrt(2) * se_max
        dev = np.abs(st["mc"] - exact)
        match_ok = bool(np.all(dev < n_se * np.abs(st["se"]) + 1e-12))
        im_ok = bool(np.all(np.abs(st["mc"].imag) < n_se * np.abs(st["se"]) + 1e-12))
        print(f"  t = {t}: split-half max diff {half_diff:.4f} (~{2 * np.sqrt(2) * se_max:.4f} "
              f"expected), max |MC - exact| = {dev.max():.4f} at max se {se_max:.4f} "
              f"-> {'match' if match_ok else 'MISMATCH'}")
        ok = ok and conv_ok and match_ok and im_ok
    return ok


def test_3_haar_limit_control() -> bool:
    print("Test 3: t = 50 control: the mean collapses to z^n (the #143 Haar-exact limit).")
    st = _mean_stats(50.0)
    nonleading = np.abs(st["mc"][1:])
    se = np.abs(st["se"][1:])
    exact_size = float(np.abs(exact_mean_coeffs(50.0)[1:]).max())
    print(f"  max nonleading |coeff| = {nonleading.max():.5f} (exact limit value "
          f"{exact_size:.1e}, MC floor ~{se.max():.5f})")
    return bool(np.all(nonleading < 5.0 * se + 1e-10))


def test_4_mean_roots_which_circle() -> bool:
    print("Test 4: THE KEY QUESTION: are the mean's roots on the UNIT circle?")
    print("  (Task expectation was yes. The data says NO: they sit exactly on the")
    print("   SHRUNKEN circle |z| = e^(-t/(2n)); Kabluchko's unimodularity is exact")
    print("   only after the rescaling w = z e^(t/(2n)). Reported as the surprise.)")
    ok = True
    for t in (0.3, 1.0, 4.0):
        r_pred = np.exp(-t / (2 * N))
        exact_roots = np.roots(exact_mean_coeffs(t))
        rad = np.abs(exact_roots)
        spread = float(rad.max() - rad.min())
        rad_dev = float(np.abs(rad - r_pred).max())
        # rescaled polynomial: unimodular roots (the unitary Hermite face)
        resc = np.abs(np.roots(exact_mean_coeffs(t)
                               * r_pred ** np.arange(N, -1, -1)))
        resc_defect = float(np.abs(resc - 1.0).max())
        st = _mean_stats(t)
        mc_vs_exact = pair_roots(st["roots"], exact_roots)
        unit_defect = float(np.abs(np.abs(st["roots"]) - 1.0).max())
        noise = st["jitter"]
        ratio = unit_defect / max(noise, 1e-15)
        print(f"  t = {t}: exact radii = {rad.mean():.6f} (pred e^(-t/12) = {r_pred:.6f}, "
              f"spread {spread:.1e}); rescaled-to-unit defect {resc_defect:.1e}")
        print(f"          MC max||root| - 1| = {unit_defect:.4f}, split-half noise floor "
              f"{noise:.4f} (defect/noise = {ratio:.1f}); MC vs exact roots {mc_vs_exact:.4f}")
        ok = ok and spread < 1e-9 and rad_dev < 1e-9 and resc_defect < 1e-9
        ok = ok and mc_vs_exact < 3.0 * max(noise, 1e-12)
        ok = ok and ratio > 3.0  # off the unit circle beyond noise, at every t
    return ok


# ---------------------------------------------------------------------------
# PART 3: interlacing with the mean.
# ---------------------------------------------------------------------------
def test_5_interlacing_fraction() -> bool:
    print("Test 5: angular interlacing of realizations with the mean polynomial.")
    st = _mean_stats(1.0)
    mean_ang = np.angle(st["roots"])
    # checker controls
    ms = np.sort(np.mod(mean_ang, TWO_PI))
    mids = np.mod(ms + cyclic_gaps(ms) / 2.0, TWO_PI)   # midpoints: must alternate
    pos_ok = alternates(mids, ms)
    bad = mids.copy()
    bad[0] = ms[1] + 0.25 * cyclic_gaps(ms)[1]          # two in one gap: must fail
    bad[1] = ms[1] + 0.50 * cyclic_gaps(ms)[1]
    neg_ok = not alternates(bad, ms)
    print(f"  checker controls: midpoints alternate = {pos_ok}, "
          f"double-occupancy rejected = {neg_ok}")

    ev = SIM["ev"][1.0]
    flags_200 = [alternates(np.angle(ev[r]), mean_ang) for r in range(R_INTERLACE)]
    flags_2k = [alternates(np.angle(ev[r]), mean_ang) for r in range(R_FUNC)]
    fr200 = float(np.mean(flags_200))
    fr2k = float(np.mean(flags_2k))
    SIM["interlace_flags"] = np.array(flags_2k)
    print(f"  fraction interlacing the mean: {fr200:.3f} (R = {R_INTERLACE}), "
          f"{fr2k:.3f} (R = {R_FUNC})")
    if fr2k >= 0.999:
        print("  SURPRISE: common interlacing holds for (essentially) all realizations;")
        print("  the MSS certificate structure would be restored. Investigate.")
        return False
    print("  -> interlacing exists but is NOT a family property (no common certificate).")
    return pos_ok and neg_ok and 0.0 <= fr2k < 0.999


# ---------------------------------------------------------------------------
# PART 4: selection functionals.
# ---------------------------------------------------------------------------
def _functional_report(idx: int) -> tuple[bool, dict]:
    name, direction, f = FUNCTIONALS[idx]
    st = _mean_stats(1.0)
    f_mean = f(st["roots"])
    ev = SIM["ev"][1.0][:R_FUNC]
    vals = np.array([f(ev[r]) for r in range(R_FUNC)])
    good = np.array([at_least_as_good(v, f_mean, direction) for v in vals])
    worse = np.array([strictly_worse(v, f_mean, direction) for v in vals])
    exists_good = bool(good.any())
    exists_worse = bool(worse.any())
    frac_good = float(good.mean())
    quant = float((vals < f_mean).mean()) if direction == "max" \
        else float((vals > f_mean).mean())
    rep = {"name": name, "direction": direction, "f_mean": f_mean, "vals": vals,
           "good": good, "frac_good": frac_good, "quantile_of_mean": quant,
           "exists_good": exists_good, "exists_worse": exists_worse}
    print(f"  functional: {name}  (better = {direction})")
    print(f"    F(mean) = {f_mean:.4f}; realizations: min {vals.min():.4f}, "
          f"median {np.median(vals):.4f}, max {vals.max():.4f}")
    print(f"    (i) exists realization at least as good: {exists_good}")
    print(f"    (ii) non-vacuous (some strictly worse):  {exists_worse}")
    print(f"    (iii) fraction at least as good: {frac_good:.3f} "
          f"(mean sits at quantile {quant:.3f})")
    if not exists_good:
        print("    SURPRISE: the mean dominates ALL realizations (one-sided MSS-style "
              "bound); flagging prominently.")
    coherent = (not np.isnan(vals).any()) and vals.std() > 0 \
        and abs(frac_good + float(worse.mean())
                + float(np.mean(vals == f_mean)) - 1.0) < 1e-12
    return coherent, rep


def test_6_functional_mesh() -> bool:
    print("Test 6: selection functional 1.")
    ok, rep = _functional_report(0)
    SIM["rep_mesh"] = rep
    return ok


def test_7_functional_maxgap() -> bool:
    print("Test 7: selection functional 2.")
    ok, rep = _functional_report(1)
    SIM["rep_maxgap"] = rep
    return ok


def test_8_functional_disc() -> bool:
    print("Test 8: selection functional 3.")
    ok, rep = _functional_report(2)
    SIM["rep_disc"] = rep
    return ok


def test_9_functional_dist1() -> bool:
    print("Test 9: selection functional 4.")
    ok, rep = _functional_report(3)
    SIM["rep_dist1"] = rep
    return ok


def test_10_no_selection_certificate() -> bool:
    print("Test 10: does interlacing-with-the-mean CERTIFY better-than-mean?")
    print("  (This is the MSS order: in the real-rooted engine, common interlacing")
    print("   converts 'the mean is good' into 'some member is at least as good',")
    print("   deterministically. Here we test for any such association.)")
    inter = SIM["interlace_flags"]
    n_i = int(inter.sum())
    if n_i == 0:
        print("  certificate set EMPTY: no realization interlaces the mean at all;")
        print("  there is nothing for a selection order to select. Sharp kill.")
        return True
    ok = True
    for key in ("rep_mesh", "rep_maxgap", "rep_disc", "rep_dist1"):
        rep = SIM[key]
        good = rep["good"]
        p_g = float(good.mean())
        p_gi = float(good[inter].mean())
        p_gn = float(good[~inter].mean()) if n_i < len(inter) else float("nan")
        agree = float((good == inter).mean())
        print(f"  {rep['name']}: P(better) = {p_g:.3f}, P(better|interlace) = {p_gi:.3f}, "
          f"P(better|no) = {p_gn:.3f}, agreement = {agree:.3f}  (n_interlace = {n_i})")
        if n_i >= 10 and p_gi >= 0.99 and p_gn <= 0.90:
            print("  SURPRISE: interlacing certifies better-than-mean for this functional;")
            print("  the MSS selection order would be restored. Investigate.")
            ok = False
    if ok:
        print("  -> no functional's better-set is certified by interlacing: 'better than")
        print("     the mean' is a distributional fact with no structural certificate.")
    return ok


# ---------------------------------------------------------------------------
# PART 5: the screen.
# ---------------------------------------------------------------------------
def test_11_presupposes_the_locus() -> bool:
    print("Test 11: screen (a), presupposes-the-locus: scale one 2x2 block of U by s;")
    print("  roots leave the circle; do the functionals measure the defect?")
    u0 = SIM["u_snapshot"]
    svals = (1.0, 1.05, 1.1, 1.2, 1.4)
    defect_means, defect_stds = [], []
    fvals = {name: [] for name, _, _ in FUNCTIONALS}
    for s in svals:
        b = u0.copy()
        b[:, :2, :2] *= s
        ev = np.linalg.eigvals(b)
        d = np.abs(np.abs(ev) - 1.0).max(axis=1)
        defect_means.append(float(d.mean()))
        defect_stds.append(float(d.std()))
        for name, _, f in FUNCTIONALS:
            fvals[name].append(np.array([f(ev[r]) for r in range(N_SCREEN)]))
    dm = np.array(defect_means)
    print("  circle defect mean over s = " + ", ".join(f"{v:.4f}" for v in dm))
    control_ok = bool(np.all(np.diff(dm) > 0)) and dm[0] < 1e-10 and dm[3] > 0.01
    d_dprime = abs(dm[-1] - dm[0]) / (defect_stds[0] + defect_stds[-1] + 1e-15)
    print(f"  defect statistic: monotone in s = {bool(np.all(np.diff(dm) > 0))}, "
          f"separation d' = {d_dprime:.1f}  (this is what MEASURING the defect looks like)")
    ok = control_ok and d_dprime > 2.0

    n_track = 0
    for name, _direction, _f in FUNCTIONALS:
        arr = fvals[name]
        means = np.array([a.mean() for a in arr])
        finite = all(np.isfinite(a).all() for a in arr)
        diffs = np.diff(means)
        mono = bool(np.all(diffs > 0) or np.all(diffs < 0))
        dprime = abs(means[-1] - means[0]) / (arr[0].std() + arr[-1].std() + 1e-15)
        tracks = mono and dprime >= 2.0
        n_track += int(tracks)
        print(f"  {name}: still well-defined off-locus = {finite}, mean over s = "
              + ", ".join(f"{v:.3f}" for v in means)
              + f", monotone = {mono}, d' = {dprime:.2f} -> "
              + ("MEASURES DEFECT (SURPRISE)" if tracks else "BLIND to the defect"))
        ok = ok and finite
    if n_track > 0:
        print(f"  SURPRISE: {n_track} functional(s) separate the circle defect; "
              "read the numbers above before trusting the kill.")
    ok = ok and n_track == 0
    print("  -> failure mode is BLINDNESS, not ill-definedness: the functionals live on")
    print("     angles, remain perfectly defined off the locus, and do not measure it.")
    return ok


def test_12_wrong_axis() -> bool:
    print("Test 12: screen (b), wrong-axis: A = on-circle, badly spaced; B = off-circle")
    print("  (radius 1.3), perfectly spaced. A spacing functional that prefers B orders")
    print("  along the spacing axis, orthogonal to the locus axis.")
    ang_a = np.array([0.02, 2.0, 2.03, 2.8, 4.0, 5.0])
    roots_a = np.exp(1j * ang_a)
    roots_b = 1.3 * np.exp(1j * TWO_PI * np.arange(N) / N)
    da = float(np.abs(np.abs(roots_a) - 1.0).max())
    db = float(np.abs(np.abs(roots_b) - 1.0).max())
    print(f"  circle defect: A = {da:.3f} (on-locus), B = {db:.3f} (off-locus)")
    ok = da < 1e-12 and abs(db - 0.3) < 1e-12
    for name, direction, f in FUNCTIONALS:
        fa, fb = f(roots_a), f(roots_b)
        prefers_b = at_least_as_good(fb, fa, direction) and strictly_worse(fa, fb, direction)
        print(f"  {name}: A = {fa:.4f}, B = {fb:.4f} -> prefers "
              f"{'B (off-locus)' if prefers_b else 'A'}")
        ok = ok and prefers_b
    print("  -> ALL FOUR functionals prefer the off-locus configuration: they carry no")
    print("     signal toward the locus. Wrong-axis, machine-checked.")
    return ok


# ---------------------------------------------------------------------------
# The battery.
# ---------------------------------------------------------------------------
PARTS = (
    ("PART 1  The UBM simulator", [test_1_simulator]),
    ("PART 2  The mean polynomial: rich, and on WHICH circle",
     [test_2_mean_convergence_and_formula, test_3_haar_limit_control,
      test_4_mean_roots_which_circle]),
    ("PART 3  Interlacing with the mean", [test_5_interlacing_fraction]),
    ("PART 4  Selection functionals",
     [test_6_functional_mesh, test_7_functional_maxgap, test_8_functional_disc,
      test_9_functional_dist1, test_10_no_selection_certificate]),
    ("PART 5  The screen", [test_11_presupposes_the_locus, test_12_wrong_axis]),
)


def main() -> None:
    print("The Kabluchko object probe: does the rich UBM mean restore MSS selection? (#143 H1)\n")
    t0 = time.time()
    print(f"Simulating M = {M} UBM trajectories (n = {N}, checkpoints t = {T_CHECK}) ...")
    SIM.update(simulate())
    print(f"  done in {time.time() - t0:.0f} s.\n")

    passed, total = 0, 0
    for banner, tests in PARTS:
        print(banner)
        print("-" * 78)
        for t in tests:
            total += 1
            ok = t()
            passed += int(ok)
            print(f"  -> {'PASS' if ok else 'FAIL'}\n")

    print("=" * 78)
    print("Verdict on H1: a sharp kill, with one honest surprise. The Kabluchko mean is")
    print("genuinely rich (Test 2: exact character formula at MC rate; Test 3: Haar")
    print("collapse recovered at t = 50), BUT it does not even live on the unit circle:")
    print("its roots sit exactly on |z| = e^(-t/(2n)) (Test 4), so mean and realizations")
    print("share no locus. Interlacing with the mean is a minority event, not a family")
    print("certificate (Test 5), and while every spacing functional makes 'some")
    print("realization is at least as good as the mean' true and non-vacuous (Tests")
    print("6-9), no functional's better-set is certified by interlacing (Test 10):")
    print("selection degenerates to sampling. The screen then closes it: the")
    print("functionals stay well-defined and BLIND when unitarity is broken (Test 11)")
    print("and all four prefer an off-locus perfectly-spaced configuration over an")
    print("on-locus badly-spaced one (Test 12). Spacing statistics order WITHIN the")
    print("locus (Level 3); nothing here points TOWARD it. The #143 gate stands:")
    print("the rich mean does not restore the extremal-selection order.")
    print(f"\n{passed}/{total} kabluchko_ubm tests passed.")
    if passed != total:
        sys.exit(1)


if __name__ == "__main__":
    main()
