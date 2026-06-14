"""Reduction Engine loop driver (increment 4).

Spec: `docs/03_research/reduction_engine.md` section 6. Runs one cycle of the
engine over a single candidate:

    INGEST -> FALSIFY (oracle) -> ROUTE -> SCORE (frontier ranking + the
    asserted-vs-proven gap) -> REPORT (kernel + next move + anti-theater counts)
    -> PERSIST (append to a monotone JSONL log).

Plus the construction-registry handoff: recompute `dh_buildable` for nodes that
carry a registered construction and cross-check against the seed's hand-set flag.
No real seed node carries a construction yet (the increment-1-to-4 handoff), so
the registry below uses formation-rule STAND-INS to exercise the cross-check; the
comment on each entry says exactly what is being stood in for.

Nothing here validates. The oracle kills or parks; the Lean hook is the only
positive floor, and it promotes nothing on its own.
"""

from __future__ import annotations

import datetime
import json
import os

import duckdb

from experiments.lemma_db.oracle import (
    Candidate, run_oracle, dh_buildable_compute, EXAMPLE_CANDIDATES,
    realization_construction, signature_construction,
    KILL, PARK, PASS,
)
from experiments.lemma_db.build_db import build, DEFAULT_DB_PATH
from experiments.lemma_db import lean_hook

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE_DIR = os.path.join(HERE, "_cache")
LOG_PATH = os.path.join(CACHE_DIR, "engine_log.jsonl")

# Construction registry: node_id -> construction callable. STAND-INS until real
# constructions are attached on ingest. Each entry is honest about what it models:
#   - signature_construction encodes the Euler-product formation gate (AX-FORM):
#     it raises NoEulerProduct on D-H, so dh_buildable computes 'false'. That is
#     exactly why AX-polarization's seed flag is 'false'.
#   - realization_construction returns a finite value on any L-function (D-H
#     included), so dh_buildable computes 'true', matching a realization node.
CONSTRUCTION_REGISTRY = {
    "AX-polarization": signature_construction,             # signature/Euler-gated => 'false'
    "CAND-connes-1999-adele-trace": realization_construction,  # realization => 'true'
}


def open_con(db_path: str = DEFAULT_DB_PATH, rebuild: bool = True) -> duckdb.DuckDBPyConnection:
    return build(db_path) if rebuild else duckdb.connect(db_path)


def current_kernel(con) -> tuple:
    """Return (top frontier rows, headline gap row, named kernel row).
    Frontier is ranked by depth + PROVEN support; the named kernel is the deepest
    frontier node that carries a milestone tag (today: AX-polarization, M4)."""
    rows = con.execute(
        "SELECT id, layer, coalesce(milestone,''), rh_depth, load_in_degree, "
        "asserted_minus_proven FROM frontier_ranked LIMIT 5"
    ).fetchall()
    gap = con.execute(
        "SELECT id, annotation_in_degree, load_in_degree, gap "
        "FROM asserted_vs_proven ORDER BY gap DESC LIMIT 1"
    ).fetchone()
    kernel = con.execute(
        "SELECT id, milestone, rh_depth FROM frontier_ranked "
        "WHERE milestone <> '' ORDER BY rh_depth DESC LIMIT 1"
    ).fetchone()
    return rows, gap, kernel


def read_log(log_path: str = LOG_PATH) -> list:
    if not os.path.exists(log_path):
        return []
    out = []
    with open(log_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                out.append(json.loads(line))
    return out


def _append_log(rec: dict, log_path: str = LOG_PATH) -> None:
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec) + "\n")


def run_cycle(candidate: Candidate, con, persist: bool = True, log_path: str = LOG_PATH) -> dict:
    """One engine cycle. Returns a record dict; appends it to the monotone log
    when persist=True."""
    ov = run_oracle(candidate)                                  # FALSIFY
    rows, gap, kernel = current_kernel(con)                     # SCORE
    prior = read_log(log_path)
    rec = {                                                     # ROUTE + REPORT payload
        "cycle": len(prior) + 1,
        "ts": datetime.datetime.now().isoformat(timespec="seconds"),
        "node_id": candidate.node_id,
        "overall": ov.overall,
        "killed_by": ov.killed_by,
        "dh_buildable": ov.dh_buildable,
        "kernel": kernel[0] if kernel else None,
        "kernel_milestone": kernel[1] if kernel else None,
        "kernel_gap_node": gap[0] if gap else None,
        "kernel_gap": gap[3] if gap else None,
    }
    if persist:                                                # PERSIST (monotone)
        _append_log(rec, log_path)
    return rec


def anti_theater(history: list) -> dict:
    """Cumulative kills by disqualifier across a history of cycle records. This is
    the number that justifies the engine: if it stays zero across many cycles, the
    engine is overhead."""
    counts: dict = {}
    for r in history:
        if r.get("overall") == KILL and r.get("killed_by"):
            counts[r["killed_by"]] = counts.get(r["killed_by"], 0) + 1
    return counts


def audit_dh_flags(con, registry: dict = CONSTRUCTION_REGISTRY) -> list:
    """Cross-check: for each registered node, compute dh_buildable and compare to
    the seed's stored flag. A mismatch means a hand-set flag the computation
    contradicts (a leak the engine should surface). Returns (id, stored, computed,
    match) per registered node."""
    out = []
    for nid, cons in registry.items():
        row = con.execute("SELECT dh_buildable FROM node WHERE id = ?", [nid]).fetchone()
        stored = row[0] if row else "(not-in-seed)"
        cand = Candidate(nid, "other", False, frozenset(), construction=cons)
        computed = dh_buildable_compute(cand).evidence.get("dh_buildable")
        match = (stored == computed) if row else None
        out.append((nid, stored, computed, match))
    return out


def demo() -> int:
    con = open_con()
    try:
        print("Reduction Engine loop driver (increment 4)\n")
        history = []
        for key in ("level3", "zero-reader", "soft-li", "realization", "abstract-honest"):
            rec = run_cycle(EXAMPLE_CANDIDATES[key], con, persist=True)
            history.append(rec)
            tail = (f"killed_by={rec['killed_by']}" if rec["killed_by"]
                    else f"dh_buildable={rec['dh_buildable']}")
            print(f"  cycle {rec['cycle']:>3}  {key:>16}  ->  {rec['overall']:4}  {tail}")

        kernel = history[-1]
        print(f"\nCURRENT KERNEL: {kernel['kernel']} ({kernel['kernel_milestone']})  |  "
              f"headline gap: {kernel['kernel_gap_node']} = {kernel['kernel_gap']} "
              "(asserted minus proven)")

        at = anti_theater(history)
        print(f"ANTI-THEATER (this session): {sum(at.values())} kill(s) "
              f"{dict(sorted(at.items()))}")

        print("\nDH-FLAG CROSS-CHECK (computed vs seed's hand-set flag):")
        for nid, stored, computed, match in audit_dh_flags(con):
            mark = "MATCH" if match else ("MISMATCH" if match is False else "n/a")
            print(f"  {nid:<32} stored={stored:<12} computed={computed:<5} [{mark}]")

        print("\nLEAN FLOOR (textual audit; run_build=True for authoritative):")
        checks = lean_hook.audit_lean_refs(_seed(), run_build=False)
        sev = {"ERROR": 0, "WARN": 0, "INFO": 0, "OK": 0}
        for c in checks:
            sev[c.severity] += 1
        print(f"  {len(checks)} lean_ref node(s): {sev['ERROR']} ERROR, {sev['WARN']} WARN, "
              f"{sev['INFO']} INFO, {sev['OK']} OK")
        print(f"\nmonotone log: {os.path.relpath(LOG_PATH, os.path.dirname(os.path.dirname(HERE)))} "
              f"({len(read_log())} cycle(s) total)")
        return 0
    finally:
        con.close()


def _seed() -> dict:
    return lean_hook._load_seed()


if __name__ == "__main__":
    raise SystemExit(demo())
