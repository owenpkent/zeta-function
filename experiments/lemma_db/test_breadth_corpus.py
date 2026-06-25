"""Tests for the breadth corpus engine (docs/03_research/breadth_program.md)."""

from __future__ import annotations

from experiments.lemma_db.breadth_corpus import (
    M4, CORPUS, Skeleton, match_score, battery, screen,
    query_transfer_candidates, rank, aim, _S,
)


def test_m4_is_top_scoring():
    """The M4 target must outscore every corpus entry (it is the ideal)."""
    top_corpus = max(match_score(e.skel) for e in CORPUS)
    assert match_score(M4) >= top_corpus


def test_polarity_is_the_discriminator():
    """A contingent-polarity skeleton must outscore the SAME skeleton made unconditional."""
    base = dict(lefschetz=1, primitive=1, duality=1, t_slot=1, signature=1,
                noncircular=1, produces="signature", dh_engages=1,
                regime="all-heights", root_half="complex")
    contingent = Skeleton(polarity="contingent", **base)
    unconditional = Skeleton(polarity="unconditional", **base)
    assert match_score(contingent) > match_score(unconditional)


def test_battery_kills_convex_hodge():
    """Unconditional + real-root convex Hodge fires e3r AND the discriminant screen."""
    convex = _S(1, 1, 1, 0, 1, "unconditional", 1, "signature", 0, "na", "real")
    fired = battery(convex)
    assert any("e3r" in r for r in fired)
    assert any("discriminant" in r for r in fired)
    assert screen(convex)["transfer_candidate"] is False


def test_battery_kills_l_value_regime():
    """A central-L-value regime fires the #113 rule (Kudla-class)."""
    kudla = _S(1, 1, 1, 1, 1, "contingent", 1, "realization", 1, "L-value", "complex")
    fired = battery(kudla)
    assert any("L-value" in r for r in fired)


def test_dh_blind_is_killed():
    """A skeleton that does not engage the Euler product fires the D-H gate."""
    dh_blind = _S(1, 1, 1, 1, 1, "contingent", 1, "signature", 0, "all-heights", "complex")
    assert any("Davenport-Heilbronn" in r for r in battery(dh_blind))


def test_transfer_candidates_are_contingent_and_survive():
    """Every returned transfer candidate is contingent, has a t-slot + duality, survives the battery."""
    for e in query_transfer_candidates():
        assert e.skel.polarity == "contingent"
        assert e.skel.t_slot and e.skel.duality
        assert battery(e.skel) == []


def test_master_column_is_a_transfer_candidate():
    """The function-field Weil/Rosati form (the master template) must be retrieved."""
    names = [e.phenomenon for e in query_transfer_candidates()]
    assert any("Weil/Rosati" in n for n in names)


def test_unconditional_entries_never_transfer_candidates():
    """No unconditional-polarity entry can be a transfer candidate (the e3r kill)."""
    for e in CORPUS:
        if e.skel.polarity == "unconditional":
            assert screen(e.skel)["transfer_candidate"] is False


def test_complement_aim_points_at_complex_root_half():
    """The disqualifier-complement aim off the discriminant screen targets the complex-root half."""
    a = aim()["discriminant screen #119"]
    assert "complex-root" in a["search"]
    assert len(a["fields"]) >= 3


def test_rank_orders_targets_above_disqualified():
    """A TARGET/TRANSFER-CANDIDATE row should outrank a DISQUALIFIED wrong-polarity row."""
    ranked = rank()
    pos = {e.phenomenon: i for i, e in enumerate(ranked)}
    weil = next(e for e in CORPUS if "Weil/Rosati" in e.phenomenon)
    leeyang = next(e for e in CORPUS if "Lee-Yang" in e.phenomenon)
    assert pos[weil.phenomenon] < pos[leeyang.phenomenon]


if __name__ == "__main__":
    import sys
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    failed = 0
    for fn in fns:
        try:
            fn()
            print(f"  [PASS] {fn.__name__}")
        except AssertionError as e:
            failed += 1
            print(f"  [FAIL] {fn.__name__}: {e}")
    print(f"\n{len(fns) - failed}/{len(fns)} passed")
    sys.exit(1 if failed else 0)
