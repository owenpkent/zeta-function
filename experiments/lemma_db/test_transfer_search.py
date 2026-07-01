"""Acceptance tests for transfer-search (Generative Engine, 6b).

Encodes the three success criteria from generative_engine.md: validation
(rediscover the known transfers, find the Hodge-index family), the Lee-Yang gate
(demote the all-positive theorem), and a fresh high-match (the novelty surface).

Run: python -m experiments.lemma_db.test_transfer_search
"""

from __future__ import annotations

from experiments.lemma_db.transfer_search import (
    rank, match_score, Features, CORPUS, M4_RESIDUAL,
)


def check(label, ok, info=""):
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {label}{(' - ' + info) if info else ''}")
    return ok


def _scores():
    return {t.name: s for t, s in rank()}


def test_templates_top():
    print("Test 1: the templates (the right shape) rank at the top")
    ranked = rank()
    top3 = {t.name for t, _ in ranked[:3]}
    return (
        check("Weil positivity is the top match", ranked[0][0].name.startswith("Weil"))
        and check("Hodge index theorem is in the top 3",
                  any("Hodge index" in n for n in top3))
    )


def test_lee_yang_gate():
    print("Test 2: the Lee-Yang gate (an all-positive theorem cannot match)")
    s = _scores()
    indefinite_min = min(
        s[t.name] for t in CORPUS if t.features.positivity_kind == "indefinite")
    return (
        check("Lee-Yang scores below every indefinite-family theorem",
              s["Lee-Yang circle theorem"] < indefinite_min,
              f"Lee-Yang={s['Lee-Yang circle theorem']}, indefinite-min={indefinite_min}")
        and check("a definite theorem scores 0 on the positivity_kind axis",
                  match_score(Features("definite", "cohomology", "polarization", True, True))
                  < match_score(Features("indefinite", "cohomology", "polarization", True, True)))
    )


def test_validation_bost_connes():
    print("Test 3: validation - the hand-found Bost-Connes import is rediscovered")
    s = _scores()
    return (
        check("Bost-Connes scores high (>= 6), the pinning import surfaced",
              s["Bost-Connes KMS uniqueness"] >= 6, f"score {s['Bost-Connes KMS uniqueness']}")
        and check("Bost-Connes >> Lee-Yang (validation beats the demoted all-positive shape)",
                  s["Bost-Connes KMS uniqueness"] > s["Lee-Yang circle theorem"])
        and check("Curto-Fialkow ranks below Bost-Connes (no continuous component)",
                  s["Curto-Fialkow flat extension"] < s["Bost-Connes KMS uniqueness"])
    )


def test_novelty_surface():
    print("Test 4: a fresh (not template/imported/candidate) theorem scores high")
    ranked = rank()
    fresh_indef = [(t, sc) for t, sc in ranked
                   if t.role == "fresh" and t.features.positivity_kind == "indefinite"]
    return (
        check("at least one fresh indefinite-Hodge-index sibling is surfaced",
              len(fresh_indef) >= 1,
              ", ".join(f"{t.name}={sc}" for t, sc in fresh_indef))
        and check("its score reaches the high tier (>= 7)", fresh_indef[0][1] >= 7)
    )


def test_brackets_low():
    print("Test 5: bracketed candidates (definite / too-strong / local) rank low")
    s = _scores()
    return (
        check("de Branges (too strong) is low", s["de Branges spaces positivity"] <= 1)
        and check("Faltings-Hriljac height (definite, local) is low",
                  s["Neron-Tate / Faltings-Hriljac height"] <= 1)
    )


def test_killed_node_demoted():
    print("Test 6: a killed corpus node stays in-corpus but ranks low and never reads as live")
    s = _scores()
    bj = "Boucksom-Jonsson non-archimedean Monge-Ampere / K-stability"
    in_corpus = next((t for t in CORPUS if t.name == bj), None)
    fresh_indef = [t for t, _ in rank()
                   if t.role == "fresh" and t.features.positivity_kind == "indefinite"]
    return (
        check("Boucksom-Jonsson is present in the corpus (not lost)", in_corpus is not None)
        and check("it is flagged role='killed' (never re-proposed as live)",
                  in_corpus is not None and in_corpus.role == "killed")
        and check("it ranks below every fresh indefinite-Hodge-index sibling (demoted)",
                  bool(fresh_indef) and all(s[bj] < s[t.name] for t in fresh_indef),
                  f"Boucksom-Jonsson={s[bj]}")
    )


def test_mss_r1_node():
    print("Test 7: the MSS interlacing node (a non-variety R1 source) is present and demoted")
    s = _scores()
    mss = "Marcus-Spielman-Srivastava interlacing families"
    node = next((t for t in CORPUS if t.name == mss), None)
    indefinite_min = min(
        s[t.name] for t in CORPUS if t.features.positivity_kind == "indefinite")
    return (
        check("MSS is present in the corpus", node is not None)
        and check("MSS is flagged role='killed' (an R1 source, not an M4 transfer)",
                  node is not None and node.role == "killed")
        and check("MSS scores below every indefinite-family theorem (wrong signature for M4)",
                  s[mss] < indefinite_min, f"MSS={s[mss]}, indefinite-min={indefinite_min}")
    )


def test_circle_engine_node():
    print("Test 8: the circle-rooted interlacing node (the #143 circle-side kill) is present and demoted")
    s = _scores()
    ce = "Circle-rooted interlacing engine (Suffridge / POPUC / Schur-Cohn)"
    node = next((t for t in CORPUS if t.name == ce), None)
    indefinite_min = min(
        s[t.name] for t in CORPUS if t.features.positivity_kind == "indefinite")
    return (
        check("circle-engine node is present in the corpus", node is not None)
        and check("it is flagged role='killed' (the engine does not exist circle-rooted)",
                  node is not None and node.role == "killed")
        and check("it scores below every indefinite-family theorem (definite Schur-Cohn shape)",
                  s[ce] < indefinite_min, f"circle-engine={s[ce]}, indefinite-min={indefinite_min}")
    )


def main():
    results = [
        test_templates_top(),
        test_lee_yang_gate(),
        test_validation_bost_connes(),
        test_novelty_surface(),
        test_brackets_low(),
        test_killed_node_demoted(),
        test_mss_r1_node(),
        test_circle_engine_node(),
    ]
    print()
    n_pass = sum(results)
    print(f"Transfer-search (6b) acceptance: {n_pass}/{len(results)} passed")
    return 0 if n_pass == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
