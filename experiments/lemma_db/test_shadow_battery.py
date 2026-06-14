"""Acceptance tests for the proven-case shadow battery (Generative Engine, 6f).

Encodes the design goals: the battery is self-validating (each checkpoint passes
its own proven witness), it scores a genuine M4-shape candidate FULL, and it is a
real graded gradient that discriminates the known failure modes along the
project's three axes (carries-t / indefinite-vs-definite / euler-gated).

Run: python -m experiments.lemma_db.test_shadow_battery
"""

from __future__ import annotations

from experiments.lemma_db.shadow_battery import (
    CHECKPOINTS, EXAMPLE_CANDIDATES, score,
    CP_PASS, FULL, PARTIAL, BROKEN,
)


def check(label, ok, info=""):
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {label}{(' - ' + info) if info else ''}")
    return ok


def test_checkpoints_nonvacuous():
    print("Test 1: every checkpoint passes its own proven witness (non-vacuous)")
    ok = True
    for cp in CHECKPOINTS:
        v, _ = cp.verify(cp.witness)
        ok = check(f"{cp.cid} ({cp.facet}) passes its witness", v == CP_PASS) and ok
    return ok


def test_genuine_full():
    print("Test 2: a genuine M4-shape candidate reproduces every proven case")
    s = score(EXAMPLE_CANDIDATES["genuine-m4"])
    return (
        check("genuine-m4 is FULL", s.verdict == FULL)
        and check("it covers all 5 checkpoints", s.passed == len(CHECKPOINTS),
                  f"{s.passed}/{len(CHECKPOINTS)}")
        and check("the D-H firewall holds (euler-gated)", s.firewall == "HOLDS")
    )


def test_arithmetic_blind_is_t_blind():
    print("Test 3: the #40 arithmetic-blind failure breaks F_q while passing the convex cases")
    s = score(EXAMPLE_CANDIDATES["arithmetic-blind"])
    return (
        check("arithmetic-blind is BROKEN", s.verdict == BROKEN)
        and check("the break is exactly CP-fq (t-blind: wrong modulus)", "CP-fq" in s.killed)
        and check("yet it reproduced the convex/combinatorial signatures",
                  s.per_cp["CP-hodge"][0] == CP_PASS
                  and s.per_cp["CP-ahk"][0] == CP_PASS
                  and s.per_cp["CP-af"][0] == CP_PASS)
        and check("and the firewall fails (no Euler product)", s.firewall == "FAILS")
    )


def test_too_strong_wrong_signature():
    print("Test 4: the de Branges / too-strong failure breaks the indefinite signature")
    s = score(EXAMPLE_CANDIDATES["too-strong"])
    return (
        check("too-strong is BROKEN", s.verdict == BROKEN)
        and check("the break is CP-hodge (definite, not (1, n-1))", "CP-hodge" in s.killed)
    )


def test_forgery_broken():
    print("Test 5: the off-line forgery breaks the function-field checkpoint")
    s = score(EXAMPLE_CANDIDATES["off-line-forgery"])
    return (
        check("off-line-forgery is BROKEN", s.verdict == BROKEN)
        and check("the break is CP-fq", "CP-fq" in s.killed)
    )


def test_gradient_discriminates():
    print("Test 6: the battery is a real graded gradient (a clean PARTIAL middle exists)")
    g = score(EXAMPLE_CANDIDATES["genuine-m4"])
    c = score(EXAMPLE_CANDIDATES["convex-only"])
    return (
        check("convex-only is PARTIAL (breaks nothing; firewall fails)",
              c.verdict == PARTIAL and not c.killed)
        and check("coverage strictly orders genuine > convex-only",
                  g.coverage > c.coverage, f"{g.coverage:.2f} > {c.coverage:.2f}")
        and check("the middle is genuinely intermediate (0 < coverage < 1)",
                  0.0 < c.coverage < 1.0, f"coverage={c.coverage:.2f}")
    )


def main():
    results = [
        test_checkpoints_nonvacuous(),
        test_genuine_full(),
        test_arithmetic_blind_is_t_blind(),
        test_too_strong_wrong_signature(),
        test_forgery_broken(),
        test_gradient_discriminates(),
    ]
    print()
    n = sum(results)
    print(f"Shadow battery (6f) acceptance: {n}/{len(results)} passed")
    return 0 if n == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
