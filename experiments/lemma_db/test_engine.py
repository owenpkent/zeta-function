"""Acceptance tests for the loop driver (increment 4) and the Lean hook
(increment 5).

Run: python -m experiments.lemma_db.test_engine

Uses an in-memory DB build and a throwaway log path so the tests are
deterministic and never touch the persisted engine log.
"""

from __future__ import annotations

import os
import tempfile

from experiments.lemma_db.build_db import build
from experiments.lemma_db.engine import (
    run_cycle, anti_theater, audit_dh_flags, CONSTRUCTION_REGISTRY,
)
from experiments.lemma_db.oracle import EXAMPLE_CANDIDATES, KILL, PASS, PARK
from experiments.lemma_db import lean_hook

_NO_LOG = os.path.join(tempfile.gettempdir(), "re_engine_test_nonexistent.jsonl")


def check(label, ok, info=""):
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {label}{(' - ' + info) if info else ''}")
    return ok


def test_run_cycle_kills_and_scores():
    print("Test 1: run_cycle kills the soft detector and scores the kernel")
    con = build(":memory:")
    try:
        rec = run_cycle(EXAMPLE_CANDIDATES["soft-li"], con, persist=False, log_path=_NO_LOG)
        return (
            check("soft-li overall KILL by flip_test",
                  rec["overall"] == KILL and rec["killed_by"] == "flip_test")
            and check("kernel is AX-polarization (M4)",
                      rec["kernel"] == "AX-polarization" and rec["kernel_milestone"] == "M4")
            and check("headline gap = TGT-m4-hodge-standard, 16",
                      rec["kernel_gap_node"] == "TGT-m4-hodge-standard" and rec["kernel_gap"] == 16)
            and check("deterministic cycle index = 1 (throwaway log)", rec["cycle"] == 1)
        )
    finally:
        con.close()


def test_pass_and_park_paths():
    print("Test 2: run_cycle reports PASS and PARK without killing")
    con = build(":memory:")
    try:
        passed = run_cycle(EXAMPLE_CANDIDATES["abstract-honest"], con, persist=False, log_path=_NO_LOG)
        parked = run_cycle(EXAMPLE_CANDIDATES["realization"], con, persist=False, log_path=_NO_LOG)
        return (
            check("abstract-honest => PASS (not yet killed)", passed["overall"] == PASS)
            and check("realization => PARK, dh_buildable computed 'true'",
                      parked["overall"] == PARK and parked["dh_buildable"] == "true")
        )
    finally:
        con.close()


def test_anti_theater_tally():
    print("Test 3: anti-theater tally counts kills by disqualifier")
    history = [
        {"overall": KILL, "killed_by": "level"},
        {"overall": KILL, "killed_by": "flip_test"},
        {"overall": KILL, "killed_by": "level"},
        {"overall": PASS, "killed_by": None},
    ]
    at = anti_theater(history)
    return (
        check("two level kills, one flip_test kill",
              at.get("level") == 2 and at.get("flip_test") == 1)
        and check("PASS does not count as a kill", sum(at.values()) == 3)
    )


def test_dh_flag_cross_check():
    print("Test 4: construction-registry cross-check confirms hand-set flags")
    con = build(":memory:")
    try:
        rows = {nid: (stored, computed, match) for nid, stored, computed, match in audit_dh_flags(con)}
        return (
            check("AX-polarization: computed 'false' matches seed",
                  rows["AX-polarization"] == ("false", "false", True))
            and check("CAND-connes-1999-adele-trace: computed 'true' matches seed",
                      rows["CAND-connes-1999-adele-trace"] == ("true", "true", True))
        )
    finally:
        con.close()


def test_lean_hook():
    print("Test 5: Lean closability hook (dangling detection + real audit)")
    # A dangling ref must be an ERROR.
    fake = {"id": "EX-dangling", "status": "proven_lean", "lean_ref": "lean/ZetaRH/NoSuchFile.lean"}
    dang = lean_hook.check_node_lean(fake)
    # A known sorry-free proven_lean node must be OK/CONSISTENT.
    real = {"id": "PRIM-l-function", "status": "proven_lean", "lean_ref": "lean/ZetaRH/Basic.lean"}
    good = lean_hook.check_node_lean(real)
    # The real seed audit must have no dangling refs / overclaims.
    seed = lean_hook._load_seed()
    audit = lean_hook.audit_lean_refs(seed, run_build=False)
    n_err = sum(1 for c in audit if c.severity == "ERROR")
    return (
        check("dangling lean_ref => DANGLING/ERROR",
              dang.verdict == lean_hook.DANGLING and dang.severity == "ERROR")
        and check("PRIM-l-function (Basic.lean) => CONSISTENT/OK",
                  good.verdict == lean_hook.CONSISTENT and good.severity == "OK")
        and check("real seed: 0 ERROR rows (no dangling refs / overclaims)", n_err == 0,
                  f"{len(audit)} lean_ref nodes audited")
    )


def main():
    results = [
        test_run_cycle_kills_and_scores(),
        test_pass_and_park_paths(),
        test_anti_theater_tally(),
        test_dh_flag_cross_check(),
        test_lean_hook(),
    ]
    print()
    n_pass = sum(results)
    print(f"Engine + Lean-hook acceptance: {n_pass}/{len(results)} passed")
    return 0 if n_pass == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
