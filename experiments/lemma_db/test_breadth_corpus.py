"""Tests for the breadth corpus engine (docs/03_research/breadth_program.md)."""

from __future__ import annotations

from experiments.lemma_db.breadth_corpus import (
    M4, CORPUS, Skeleton, match_score, battery, screen,
    query_transfer_candidates, rank, aim, FINGERPRINT, _S,
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


def test_aim_converged_after_acq2():
    """After acq2 the breadth search has converged: aim() reports the status + the pivot to construction."""
    a = aim()
    assert "CONVERGED" in a["status"]
    assert "pivot" in a
    assert "M4" in a["status"] or "polarization" in a["status"]


def test_acq2_selection_not_sign_screen():
    """The Bridgeland near-miss (indefinite form, but membership flips not the sign) fires the #121 screen."""
    bridgeland = _S(1,1,1,0,1,"unconditional",1,"realization",0,"na","na","na","curative","output-selection")
    assert any("selection-not-sign" in r for r in battery(bridgeland))


def test_acq2_special_value_regime_screen():
    """The Gamma-conjecture near-miss (zeta values at k>=2) fires the special-value/period screen."""
    gamma = _S(0,0,1,0,0,"na",1,"realization",0,"special-value","na")
    assert any("special-value" in r for r in battery(gamma))


def test_acq1_wrong_axis_screen():
    """A contingency that flips on the vertical-spacing or strip-width axis fires the wrong-axis screen."""
    spacing = _S(0,0,0,0,0,"contingent",1,"realization",1,"na","complex","spacing","na","na")
    strip = _S(1,0,1,1,1,"contingent",1,"realization",1,"all-heights","complex","strip-width","na","na")
    assert any("wrong-axis" in r for r in battery(spacing))
    assert any("wrong-axis" in r for r in battery(strip))


def test_acq1_curative_flip_screen():
    """A curative flip (locus relocates) fires the curative-flip screen even when complex-root + contingent."""
    rh = _S(0,0,1,0,1,"contingent",1,"realization",1,"all-heights","complex","line","curative","na")
    assert any("curative" in r for r in battery(rh))


def test_acq1_input_output_screen():
    """An input-definite (measure-class) positivity fires the input/output split screen."""
    leeyang = _S(0,0,1,0,1,"contingent",1,"signature",1,"all-heights","complex","line","prohibitive","input-definite")
    assert any("input/output" in r for r in battery(leeyang))


def test_selection_order_screen_fires_on_mss():
    """#143: an averaging-plus-selection engine (MSS-style interlacing families) certifies via
    a one-sided bound on an ORDERED quantity; an exact locus (roots ON a circle or line) has no
    native one-sided order, so the order is presupposed. The screen must fire."""
    mss = _S(0, 0, 0, 0, 0, "na", 1, "realization", 1, "na", "na", order_source="selection")
    fired = battery(mss)
    assert any("selection-order" in r for r in fired)
    assert screen(mss)["transfer_candidate"] is False


def test_selection_order_screen_spares_operator_carrier():
    """#143: a phenomenon that carries its own operator (the Selberg/Laplacian case: the order
    IS the real spectrum, manufactured by self-adjointness) must NOT fire the selection-order
    screen; it dies elsewhere (strip-width axis, K1), not by presupposing the order."""
    selberg = _S(1, 0, 1, 1, 1, "contingent", 1, "realization", 1, "all-heights", "complex",
                 "strip-width", "na", "na", order_source="operator")
    assert not any("selection-order" in r for r in battery(selberg))


def test_mss_corpus_row_disqualified():
    """The #143 kill is on file: the MSS row is DISQUALIFIED by the selection-order screen and
    stays below the M4 target in rank (the killed circle-engine node lives in transfer_search.py)."""
    mss = next(e for e in CORPUS if "MSS interlacing" in e.phenomenon)
    assert mss.verdict == "DISQUALIFIED"
    assert "#143" in mss.rule
    assert mss.skel.order_source == "selection"
    assert any("selection-order" in r for r in battery(mss.skel))
    assert match_score(mss.skel) < match_score(M4)


def test_m4_has_full_fingerprint():
    """The M4 target must carry every fingerprint value (it is the ideal profile)."""
    assert M4.axis == "line"
    assert M4.flip == "prohibitive"
    assert M4.side == "output-indefinite"
    for key in FINGERPRINT:
        assert hasattr(M4, key)


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
