"""Acceptance tests for the executable falsifier oracle (increment 1).

Run: python -m experiments.lemma_db.test_oracle

Covers the five disqualifier branches and the two integration facts that make
the oracle worth having: the canonical soft detector (Li) is blind to D-H and is
killed by the flip test, and the only separating detector is circular and is
killed by K1. Together they are the marginal-positivity wall, executable.

Style mirrors experiments/_shared/smoke_test.py (plain runnable module, no
pytest dependency).
"""

from __future__ import annotations

from experiments.lemma_db.oracle import (
    Candidate, run_oracle,
    level_classifier, k1_noncircular, dh_buildable_compute, flip_test,
    li_min_detector, offline_zero_detector,
    realization_construction, signature_construction,
    KILL, PARK, PASS, UNTESTABLE,
    EXAMPLE_CANDIDATES,
)
from experiments._shared import zeta_L, DavenportHeilbronn


def check(label, ok, info=""):
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {label}{(' - ' + info) if info else ''}")
    return ok


def test_level_classifier():
    print("Test 1: level classifier (Level-3 kill)")
    stat = Candidate("t-stat", "statistical", False, frozenset())
    pos = Candidate("t-pos", "positivity", True, frozenset())
    tr = Candidate("t-tr", "trace", False, frozenset())
    return (
        check("statistical + no RH-equiv => KILL", level_classifier(stat).result == KILL)
        and check("positivity => PASS", level_classifier(pos).result == PASS)
        and check("trace + no RH-equiv => PARK (realization-only)", level_classifier(tr).result == PARK)
    )


def test_k1_noncircular():
    print("Test 2: K1 non-circularity tripwire")
    circ = Candidate("t-circ", "positivity", True, frozenset({"zero_locations"}))
    clean = Candidate("t-clean", "positivity", True, frozenset({"polarization"}))
    return (
        check("positivity reading zero_locations => KILL", k1_noncircular(circ).result == KILL)
        and check("positivity from a polarization => PASS", k1_noncircular(clean).result == PASS)
    )


def test_dh_buildable_compute():
    print("Test 3: computed dh_buildable (replaces the hand-set flag)")
    realiz = Candidate("t-realiz", "trace", False, frozenset(), construction=realization_construction)
    sig = Candidate("t-sig", "positivity", True, frozenset({"polarization"}), construction=signature_construction)
    abstract = Candidate("t-abs", "positivity", True, frozenset(), construction=None)
    v_realiz = dh_buildable_compute(realiz)
    v_sig = dh_buildable_compute(sig)
    v_abs = dh_buildable_compute(abstract)
    return (
        check("realization construction => dh_buildable='true' (PARK)",
              v_realiz.evidence.get("dh_buildable") == "true" and v_realiz.result == PARK)
        and check("signature construction raises NoEulerProduct => 'false' (PASS)",
                  v_sig.evidence.get("dh_buildable") == "false" and v_sig.result == PASS)
        and check("abstract construction => 'N/A' (UNTESTABLE)",
                  v_abs.evidence.get("dh_buildable") == "N/A" and v_abs.result == UNTESTABLE)
    )


def test_flip_test_separating():
    print("Test 4: flip test PASSES a genuinely separating detector")
    sep = Candidate("t-sep", "positivity", True, frozenset({"polarization"}), detector=offline_zero_detector)
    v = flip_test(sep)
    return check("offline-zero detector separates D-H => PASS",
                 v.result == PASS, f"zeta={v.evidence['zeta']}, dh={v.evidence['dh']}")


def test_flip_test_blind_li():
    print("Test 5: flip test KILLS the blind Li detector (the load-bearing test)")
    # The substantive computation: min_n lambda_n is non-negative on BOTH zeta and
    # D-H, so the canonical soft positivity functional cannot separate the
    # counterexample. If this ever stops being a KILL, either the oracle broke or
    # someone found a soft detector that separates D-H (which would be major).
    d_zeta = li_min_detector(zeta_L)
    d_dh = li_min_detector(DavenportHeilbronn())
    blind = Candidate("t-li", "positivity", True, frozenset({"polarization"}), detector=li_min_detector)
    v = flip_test(blind)
    return (
        check("li_min(zeta) >= 0", d_zeta >= 0, f"{d_zeta:.5f}")
        and check("li_min(D-H) >= 0 (Li is BLIND to the off-line zeros)", d_dh >= 0, f"{d_dh:.5f}")
        and check("flip test => KILL", v.result == KILL)
    )


def test_pipeline_two_move_wall():
    print("Test 6: full pipeline reproduces the two-move wall")
    soft = run_oracle(EXAMPLE_CANDIDATES["soft-li"])
    reader = run_oracle(EXAMPLE_CANDIDATES["zero-reader"])
    abstract = run_oracle(EXAMPLE_CANDIDATES["abstract-honest"])
    realiz = run_oracle(EXAMPLE_CANDIDATES["realization"])
    return (
        check("soft-li: KILL by flip_test (blindness)",
              soft.overall == KILL and soft.killed_by == "flip_test")
        and check("zero-reader: KILL by k1 (circularity), flip never runs",
                  reader.overall == KILL and reader.killed_by == "k1_noncircular"
                  and "flip_test" not in reader.verdicts)
        and check("abstract-honest: overall PASS (== not yet killed, not valid)",
                  abstract.overall == PASS and abstract.killed_by is None)
        and check("realization: PARK with computed dh_buildable='true'",
                  realiz.overall == PARK and realiz.dh_buildable == "true")
    )


def main():
    results = [
        test_level_classifier(),
        test_k1_noncircular(),
        test_dh_buildable_compute(),
        test_flip_test_separating(),
        test_flip_test_blind_li(),
        test_pipeline_two_move_wall(),
    ]
    print()
    n_pass = sum(results)
    print(f"Oracle acceptance: {n_pass}/{len(results)} passed")
    return 0 if n_pass == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
