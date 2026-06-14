"""Acceptance tests for new-branch spec generation (Generative Engine, 6e).

Run: python -m experiments.lemma_db.test_branch_specs
"""

from __future__ import annotations

from experiments.lemma_db.build_db import build
from experiments.lemma_db.branch_specs import (
    top_gap_node, classify, run, M4_SPEC,
    CONVERGENT, BRACKETED, CIRCULAR, PRE_REALIZATION,
)


def check(label, ok, info=""):
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {label}{(' - ' + info) if info else ''}")
    return ok


def test_spec_has_one_blind_spot():
    print("Test 1: the M4 spec has exactly one blind-spot property (the polarization)")
    blind = [p for p in M4_SPEC if p.blind_spot]
    return (
        check("exactly one blind-spot property", len(blind) == 1)
        and check("it is PROP-rh-equivalent (the indefinite polarization)",
                  blind[0].prop_id == "PROP-rh-equivalent")
    )


def test_forcing_question_is_the_gap():
    print("Test 2: the forcing question is read off the top gap")
    con = build(":memory:")
    try:
        gap = top_gap_node(con)
        return check("top gap is TGT-m4-hodge-standard with gap 16",
                     gap[0] == "TGT-m4-hodge-standard" and gap[3] == 16,
                     f"{gap[0]} gap {gap[3]}")
    finally:
        con.close()


def test_classification():
    print("Test 3: candidates classify to the right residual")
    con = build(":memory:")
    try:
        c = {r.cand: r for r in run(con)}
        return (
            check("Deninger-foliated CONVERGENT, residual = the polarization (blind spot)",
                  c["CAND-deninger-foliated"].verdict == CONVERGENT
                  and c["CAND-deninger-foliated"].blind_spot)
            and check("Connes-1999 CIRCULAR (positivity read off the zeros)",
                      c["CAND-connes-1999-adele-trace"].verdict == CIRCULAR)
            and check("Faltings-Hriljac BRACKETED on 'global'",
                      c["CAND-faltings-hriljac"].verdict == BRACKETED
                      and c["CAND-faltings-hriljac"].residual_prop == "PROP-global")
            and check("AHK BRACKETED on 'carries-trace'",
                      c["CAND-adiprasito-huh-katz"].verdict == BRACKETED
                      and c["CAND-adiprasito-huh-katz"].residual_prop == "PROP-carries-trace")
            and check("Deitmar PRE-REALIZATION (upstream)",
                      c["CAND-deitmar-monoid-schemes"].verdict == PRE_REALIZATION)
        )
    finally:
        con.close()


def test_convergence_is_generated():
    print("Test 4: the convergence is generated and bottoms out at the blind spot")
    con = build(":memory:")
    try:
        residuals = run(con)
        conv = [r for r in residuals if r.verdict == CONVERGENT]
        return (
            check("at least 9 candidates converge", len(conv) >= 9, f"{len(conv)} convergent")
            and check("every convergent residual is the blind-spot polarization",
                      all(r.blind_spot and r.residual_prop == "PROP-rh-equivalent" for r in conv))
            and check("the brackets do NOT carry the blind-spot flag",
                      all(not r.blind_spot for r in residuals if r.verdict != CONVERGENT))
        )
    finally:
        con.close()


def main():
    results = [
        test_spec_has_one_blind_spot(),
        test_forcing_question_is_the_gap(),
        test_classification(),
        test_convergence_is_generated(),
    ]
    print()
    n_pass = sum(results)
    print(f"Branch-spec (6e) acceptance: {n_pass}/{len(results)} passed")
    return 0 if n_pass == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
