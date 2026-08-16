"""Smoke test for the RH toy sandbox. Run: python -m experiments.toy.test_toy

Verifies the toy's ground truth and that the grader has teeth:
  - every positive instance is on-circle, every negative is off-circle;
  - moments are real (the spectrum is conjugation- and inversion-closed);
  - the reference candidate (e2xx moment matrix) scores ALL GREEN;
  - the second reference (Cohn 1922 + Schur-Cohn, LEARNINGS #143) scores ALL GREEN,
    with the Schur-Cohn convention validated against brute-force root location;
  - a soft candidate (identity) FAILS rejects_fakes;
  - the D-H instance is correctly unbuildable (the firewall);
  - the spectral toy: self-adjoint => on-line, non-self-adjoint => off-line.
"""

from __future__ import annotations

import numpy as np

from experiments.toy.instances import POSITIVE_BATTERY, NEGATIVE_BATTERY, FULL_BATTERY, ToyData
from experiments.toy.grader import (
    grade,
    is_psd,
    moment_matrix_candidate,
    schur_cohn_candidate,
    schur_cohn_matrix,
    identity_candidate,
    diag_moment_candidate,
)
from experiments.toy import axiom_census, selberg
from experiments.toy import ihara
from experiments.toy import interlacing
from experiments.toy import alon_boppana
from experiments.toy import archimedean_place
from experiments.toy.ihara_grader import (
    grade as grade_graph,
    moment_localizing_candidate,
    hamburger_only_candidate,
    POSITIVE_GRAPHS,
    NEGATIVE_GRAPHS,
)


def test_ground_truth():
    for inst in POSITIVE_BATTERY:
        assert inst.rh_true and inst.has_euler
        assert inst.circle_defect() < 1e-9, f"positive {inst.name} not on circle"
    for inst in NEGATIVE_BATTERY:
        assert not inst.rh_true
        if inst.has_euler:
            assert inst.circle_defect() > 1e-3, f"negative {inst.name} unexpectedly on circle"


def test_moments_real():
    for inst in FULL_BATTERY:
        if not inst.has_euler:
            continue
        for n in range(7):
            val = sum(u ** n for u in inst.eigenvalues_u)
            assert abs(val.imag) < 1e-9, f"{inst.name} moment c_{n} not real"


def test_reference_all_green():
    sc = grade(moment_matrix_candidate, "reference")
    assert sc.reproduces_weil, "reference must reproduce Weil on RH-true instances"
    assert sc.rejects_fakes, "reference must reject the off-line fakes"
    assert sc.dh_immune, "reference must be unbuildable for D-H"
    assert sc.k1_clean
    assert sc.all_green


def test_soft_candidates_fail():
    for cand, name in [(identity_candidate, "identity"), (diag_moment_candidate, "diag c_0")]:
        sc = grade(cand, name)
        assert sc.reproduces_weil, f"{name} should still certify the true curves"
        assert not sc.rejects_fakes, f"{name} should FAIL to reject the fakes (soft positivity)"
        assert not sc.all_green


def test_dh_unbuildable():
    dh = [i for i in NEGATIVE_BATTERY if i.kind == "dh"][0]
    assert moment_matrix_candidate(dh.to_data(6)) is None
    assert schur_cohn_candidate(dh.to_data(6)) is None


def test_schur_cohn_formula():
    """Brute-force validation of the Schur-Cohn convention (the formula is the risk;
    the root locations are the arbiter): on random polynomials (mixed real/complex
    coefficients, degrees 1..6, roots planted inside / outside / on the circle,
    random non-monic scale), PSD must match "all roots in the closed unit disk" in
    every case, and off the boundary the number of negative eigenvalues must equal
    the number of roots outside the disk."""
    rng = np.random.default_rng(20260701)
    psd_checked = sig_checked = 0
    for _ in range(400):
        m = int(rng.integers(1, 7))
        real_coeffs = bool(rng.integers(0, 2))
        roots = []
        while len(roots) < m:
            kind = int(rng.integers(0, 3))  # 0 inside, 1 outside, 2 on the circle
            r = (rng.uniform(0.05, 0.9), rng.uniform(1.1, 2.5), 1.0)[kind]
            if real_coeffs and m - len(roots) >= 2 and rng.random() < 0.5:
                z = r * np.exp(1j * rng.uniform(0.1, np.pi - 0.1))
                roots += [z, np.conj(z)]  # conjugate pair keeps the coefficients real
            elif real_coeffs:
                roots.append(complex(r * (1.0 if rng.random() < 0.5 else -1.0)))
            else:
                roots.append(r * np.exp(1j * rng.uniform(0.0, 2.0 * np.pi)))
        roots = np.array(roots, dtype=complex)
        coeffs = np.poly(roots)
        if real_coeffs:
            coeffs = np.real(coeffs)
        scale = rng.uniform(0.5, 2.0)
        if not real_coeffs:
            scale = scale * np.exp(1j * rng.uniform(0.0, 2.0 * np.pi))
        S = schur_cohn_matrix(coeffs * scale)
        w = np.linalg.eigvalsh(S)
        tol = 1e-8 * (1.0 + float(np.abs(S).max()))
        radii = np.abs(roots)
        all_closed = bool(np.all(radii <= 1.0 + 1e-9))
        assert (float(w.min()) >= -tol) == all_closed, (radii, w)
        psd_checked += 1
        if np.all(np.abs(radii - 1.0) > 1e-3):
            assert int(np.sum(w < -tol)) == int(np.sum(radii > 1.0)), (radii, w)
            sig_checked += 1
    assert psd_checked == 400 and sig_checked >= 80
    # the hand-checkable genus-1 anchor: phi' = 2z - t/sqrt(p) gives S = [4 - t^2/p]
    t, p = 3.0, 7.0
    S1 = np.real(schur_cohn_matrix(np.array([2.0, -t / np.sqrt(p)])))
    assert abs(float(S1[0, 0]) - (4.0 - t * t / p)) < 1e-12


def test_schur_cohn_all_green():
    """The second reference (Cohn 1922 + Schur-Cohn, LEARNINGS #143) must score ALL
    GREEN: an independent classical theorem lands the same verdicts as the
    Caratheodory-Toeplitz moment route."""
    sc = grade(schur_cohn_candidate, "schur-cohn")
    assert sc.reproduces_weil, "Schur-Cohn must certify every RH-true instance"
    assert sc.rejects_fakes, "Schur-Cohn must reject every off-circle fake"
    assert sc.dh_immune, "no Euler product => no moments => unbuildable"
    assert sc.k1_clean
    assert sc.all_green
    # the supersingular boundary t^2 = 4q (u = 1 double root): the matrix is
    # PSD-SINGULAR (min eigenvalue exactly 0) and the grader tolerance accepts it,
    # with no loosening of the global PSD_TOL
    ss = ToyData(q=4, genus=1, moments=(2.0, 2.0, 2.0), has_euler=True)
    M = schur_cohn_candidate(ss)
    assert M is not None
    assert abs(float(np.linalg.eigvalsh(M).min())) < 1e-12
    assert is_psd(M)


def test_spectral_toy():
    A = selberg.random_self_adjoint(6, lo=0.25, seed=1)
    assert selberg.critical_line_verdict(np.linalg.eigvalsh(A)).on_line
    B = selberg.break_self_adjointness(A, eps=0.4, seed=2)
    assert not selberg.critical_line_verdict(np.linalg.eigvals(B)).on_line


def test_ihara_theorem():
    """The graph-RH theorem: Ramanujan <=> all nontrivial Ihara poles on |u| = 1/sqrt(q)."""
    for inst in POSITIVE_GRAPHS:
        v = ihara.graph_rh_verdict(inst.adjacency)
        assert v.is_ramanujan and v.on_line, f"{inst.name} should be Ramanujan and on-line"
    for inst in NEGATIVE_GRAPHS:
        v = ihara.graph_rh_verdict(inst.adjacency)
        assert (not v.is_ramanujan) and (not v.on_line), \
            f"{inst.name} should be the native D-H (non-Ramanujan, off-line)"
        assert v.max_offline_defect > 1e-3


def test_ihara_reference_all_green():
    sc = grade_graph(moment_localizing_candidate, "reference")
    assert sc.reproduces_ramanujan and sc.rejects_nonramanujan and sc.all_green


def test_ihara_hamburger_fails():
    """Self-adjointness alone (the Hamburger block) reproduces but cannot reject the native
    D-H: real spectrum is free, the spectral gap is the content."""
    sc = grade_graph(hamburger_only_candidate, "hamburger only")
    assert sc.reproduces_ramanujan
    assert not sc.rejects_nonramanujan
    assert not sc.all_green


def test_interlacing_source_and_faultline():
    """MSS interlacing sources the sqrt(q) bound with no variety (Godsil-Gutman, real-rooted
    matching poly, a good signing exists), but the arithmetic L-polynomial is not real-rooted,
    so the engine cannot transfer."""
    edges, n = interlacing.k33_edges()
    d = interlacing.degree(edges, n)
    bound = 2.0 * np.sqrt(d - 1)
    mu = interlacing.matching_polynomial(edges, n)
    exp = interlacing.expected_char_poly(edges, n)
    assert np.max(np.abs(mu - exp)) < 1e-9, "Godsil-Gutman: avg char poly = matching poly"
    roots = np.roots(mu)
    assert np.max(np.abs(roots.imag)) < 1e-9, "Heilmann-Lieb: matching poly is real-rooted"
    assert np.max(np.abs(roots.real)) <= bound + 1e-9, "matching roots within the Ramanujan window"
    assert interlacing.min_max_root_over_signings(edges, n) <= bound + 1e-9, "a good signing exists"
    # the fault line: arithmetic L-polynomial roots are complex (not real-rooted)
    from experiments.toy.instances import POSITIVE_BATTERY
    max_imag = max(
        float(np.max(np.abs(np.array(inst.eigenvalues_u, dtype=complex).imag)))
        for inst in POSITIVE_BATTERY)
    assert max_imag > 0.5, "arithmetic Frobenius eigenvalues are genuinely complex (not real-rooted)"


def test_alon_boppana_marginal():
    """Marginal positivity as a theorem: the cycle margin to 2 sqrt(q) shrinks toward zero
    (no buffer), the bound is the Kesten-McKay tree edge, and non-Ramanujan graphs sit above
    it while random regular graphs concentrate at it."""
    margins = [2.0 - 2.0 * np.cos(2.0 * np.pi / n) for n in (16, 64, 256)]
    assert margins[0] > margins[1] > margins[2], "cycle margin must shrink toward the bound"
    assert margins[2] < 1e-3, "the margin has no fixed buffer (approaches zero)"
    assert abs(alon_boppana.kesten_mckay_edge(3) - 2.0 * np.sqrt(2)) < 1e-12
    # the native D-H sits ABOVE the bound; a random regular graph concentrates AT it
    v = ihara.graph_rh_verdict(ihara.two_clique_bridge(5))
    assert v.max_nontrivial_abs_lambda > v.ramanujan_bound
    A = alon_boppana.random_regular(300, 3, seed=1)
    assert abs(alon_boppana.spectral_radius_nontrivial(A) - 2.0 * np.sqrt(2)) < 0.25


def test_archimedean_flat_vs_continuous():
    """The archimedean place = atomic-flat (function-field) vs continuous-never-flat (the
    universal cover). Petersen's atomic Hankel goes flat at its atom count; the Kesten-McKay
    Hankel never does; growing finite graphs converge to the continuous measure."""
    ap = archimedean_place
    vals = ap.nontrivial_eigs(ihara.petersen_graph())     # 2 distinct atoms
    m = ap.atom_moments(vals, 12)
    assert ap.min_eig(ap.hankel(m, 1)) > 1e-6, "rank 2 measure: order-1 Hankel is full"
    assert ap.min_eig(ap.hankel(m, 2)) < 1e-10, "atomic measure goes FLAT at its atom count"
    # continuous Kesten-McKay: never flat, and m_2 = d
    mkm = ap.kesten_mckay_moments(3, 12)
    assert abs(mkm[2] - 3.0) < 1e-2, "Kesten-McKay second moment = d"
    assert ap.min_eig(ap.hankel(mkm, 6)) > 1e-3, "continuous measure Hankel never flattens"
    # the passage: finite empirical moments converge to Kesten-McKay
    edge = ap.kesten_mckay_edge(3)
    mkm_norm = np.array([mkm[k] / edge ** k for k in range(9)])
    d30 = np.linalg.norm(ap.atom_moments(ap.nontrivial_eigs(ap.random_regular(30, 3, 1)) / edge, 8)[2:] - mkm_norm[2:])
    d300 = np.linalg.norm(ap.atom_moments(ap.nontrivial_eigs(ap.random_regular(300, 3, 3)) / edge, 8)[2:] - mkm_norm[2:])
    assert d300 < d30, "finite spectra converge to the continuous universal-cover measure"


def test_axiom_census_gap():
    """FE + integrality + Euler-product positivity do NOT force RH.

    The three axioms confine the inverse roots only to |alpha| <= q, the trivial
    region Re(s) <= 1 that the Euler product supplies for free; RH is Re(s) = 1/2.
    Genus 1 pins the permitted range exactly; genus 2 shows the RH-violating
    fraction growing with q. This is why "all Weil cohomologies are the same"
    cannot deliver the polarization: positivity is not among the axioms that the
    sameness pins down."""
    ac = axiom_census
    ps = ac.power_sums([3, 5], 8)
    ref = [2, -3]
    for n in range(2, 9):
        ref.append(-3 * ref[-1] - 5 * ref[-2])
    assert ps[:9] == ref[:9], "Newton identities disagree with the genus-1 recursion"
    assert ac.power_sums([0, 4, 0, 4], 4)[:5] == [4, 0, -8, 0, 16], "genus-2 power sums"

    for q in (5, 7, 9, 13):
        ok, weil = ac.genus1_range(q)
        assert min(ok) == -(q + 1) and max(ok) == q, f"axiom range wrong at q={q}"
        assert any(a * a > 4 * q for a in ok), f"no RH violator at q={q}"

    q, c = ac.REPO_FAKE           # LEARNINGS #123
    assert c[2] == q * c[0] and c[3] == q * q, "#123 must satisfy the functional equation"
    assert ac.euler_ok(q, c) and ac.tail_is_safe(q, c), "#123 must have an Euler product"
    assert not ac.rh_ok(q, c), "#123 must violate RH"
    assert ac.point_counts(q, c, 4)[1:5] == [2, 40, 182, 660], "#123 point counts"

    small, big = ac.genus2_census(2), ac.genus2_census(9)
    assert small["violate"] == 0, "q=2 is small enough that the axioms do force RH"
    assert big["violate"] > big["rh"], "by q=9 most axiom-satisfying models violate RH"
    assert big["worst"] > 2.9, "worst violation should approach sqrt(q) = 3"


def main() -> None:
    tests = [
        test_ground_truth,
        test_moments_real,
        test_reference_all_green,
        test_soft_candidates_fail,
        test_dh_unbuildable,
        test_schur_cohn_formula,
        test_schur_cohn_all_green,
        test_spectral_toy,
        test_ihara_theorem,
        test_ihara_reference_all_green,
        test_ihara_hamburger_fails,
        test_interlacing_source_and_faultline,
        test_alon_boppana_marginal,
        test_archimedean_flat_vs_continuous,
        test_axiom_census_gap,
    ]
    passed = 0
    for t in tests:
        t()
        passed += 1
        print(f"  [ok] {t.__name__}")
    print(f"\n{passed}/{len(tests)} toy sandbox tests passed.")


if __name__ == "__main__":
    main()
