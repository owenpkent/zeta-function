"""Smoke test for the RH toy sandbox. Run: python -m experiments.toy.test_toy

Verifies the toy's ground truth and that the grader has teeth:
  - every positive instance is on-circle, every negative is off-circle;
  - moments are real (the spectrum is conjugation- and inversion-closed);
  - the reference candidate (e2xx moment matrix) scores ALL GREEN;
  - a soft candidate (identity) FAILS rejects_fakes;
  - the D-H instance is correctly unbuildable (the firewall);
  - the spectral toy: self-adjoint => on-line, non-self-adjoint => off-line.
"""

from __future__ import annotations

import numpy as np

from experiments.toy.instances import POSITIVE_BATTERY, NEGATIVE_BATTERY, FULL_BATTERY
from experiments.toy.grader import (
    grade,
    moment_matrix_candidate,
    identity_candidate,
    diag_moment_candidate,
)
from experiments.toy import selberg


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


def test_spectral_toy():
    A = selberg.random_self_adjoint(6, lo=0.25, seed=1)
    assert selberg.critical_line_verdict(np.linalg.eigvalsh(A)).on_line
    B = selberg.break_self_adjointness(A, eps=0.4, seed=2)
    assert not selberg.critical_line_verdict(np.linalg.eigvals(B)).on_line


def main() -> None:
    tests = [
        test_ground_truth,
        test_moments_real,
        test_reference_all_green,
        test_soft_candidates_fail,
        test_dh_unbuildable,
        test_spectral_toy,
    ]
    passed = 0
    for t in tests:
        t()
        passed += 1
        print(f"  [ok] {t.__name__}")
    print(f"\n{passed}/{len(tests)} toy sandbox tests passed.")


if __name__ == "__main__":
    main()
