"""Acceptance tests for the function-field shadow (6d) and the move-library
generator + quality-diversity archive (6a, 6c).

Run: python -m experiments.lemma_db.test_generator
"""

from __future__ import annotations

from experiments.lemma_db.fq_shadow import (
    FQ_CONTROLS, FQ_FORGERY, fq_shadow_check, SHADOW_PASS, SHADOW_KILL,
)
from experiments.lemma_db.generator import (
    seed, evaluate, generate, anti_theater,
    base_change, perturb_offline, drop_euler, degenerate_q1, read_zeros, go_statistical,
    SURVIVE, KILL_FQ, KILL_K1, KILL_LEVEL, VACUOUS, UNTESTABLE,
)


def check(label, ok, info=""):
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {label}{(' - ' + info) if info else ''}")
    return ok


def test_fq_shadow():
    print("Test 1: function-field shadow (positive control)")
    controls_ok = all(fq_shadow_check(c.eigenvalues, c.q)[0] == SHADOW_PASS for c in FQ_CONTROLS)
    fv, fd = fq_shadow_check(FQ_FORGERY.eigenvalues, FQ_FORGERY.q)
    return (
        check("all genuine F_q curves reproduce Weil (SHADOW_PASS)", controls_ok)
        and check("off-line forgery is killed (SHADOW_KILL, defect > 0.1)",
                  fv == SHADOW_KILL and fd > 0.1, f"defect={fd:.3f}")
    )


def test_seed_survives():
    print("Test 2: the seed (Weil/F_q) survives the disciplines")
    v = evaluate(seed())
    return check("seed -> SURVIVE (on-circle, Euler, Level-4, non-circular)",
                 v.outcome == SURVIVE)


def test_each_move_hits_its_discipline():
    print("Test 3: each pruning move is caught by the right discipline")
    s = seed()
    cases = [
        (perturb_offline, KILL_FQ, "off-circle breaks the F_q theorem"),
        (drop_euler, VACUOUS, "no Euler product => no positivity to state (firewall)"),
        (read_zeros, KILL_K1, "reads the zeros => circular"),
        (go_statistical, KILL_LEVEL, "drops to Level-3 statistics"),
        (degenerate_q1, UNTESTABLE, "q->1 abstract => no cheap evaluation"),
        (base_change, SURVIVE, "another valid F_q curve => survives"),
    ]
    ok = True
    for move, expected, why in cases:
        got = evaluate(move(s)).outcome
        ok = check(f"{move.__name__} -> {expected} ({why})", got == expected, f"got {got}") and ok
    return ok


def test_perturb_defect_positive():
    print("Test 4: perturb-offline produces a measurable circle defect")
    v = evaluate(perturb_offline(seed()))
    return check("defect > 0.1", v.defect is not None and v.defect > 0.1,
                 f"defect={v.defect}")


def test_quality_diversity_archive():
    print("Test 5: generation fills distinct cells and the anti-theater tally is real")
    verdicts, archive = generate(seed(), depth=2)
    at = anti_theater(verdicts)
    outcomes = {v.outcome for v in verdicts}
    return (
        check("archive fills >= 5 distinct cells", len(archive) >= 5, f"{len(archive)} cells")
        and check("all four kill disciplines fire",
                  {KILL_FQ, KILL_K1, KILL_LEVEL, VACUOUS} <= set(at.keys()))
        and check("at least one SURVIVE and one UNTESTABLE present",
                  SURVIVE in outcomes and UNTESTABLE in outcomes)
    )


def main():
    results = [
        test_fq_shadow(),
        test_seed_survives(),
        test_each_move_hits_its_discipline(),
        test_perturb_defect_positive(),
        test_quality_diversity_archive(),
    ]
    print()
    n_pass = sum(results)
    print(f"Generator + F_q-shadow acceptance: {n_pass}/{len(results)} passed")
    return 0 if n_pass == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
