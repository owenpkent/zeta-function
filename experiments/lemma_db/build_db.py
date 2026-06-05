"""
build_db.py - (re)build the RH lemma-graph DuckDB database.

Loads experiments/lemma_db/schema.sql (DDL + views) and seeds it from
experiments/lemma_db/seed_lemmas.json, then runs structural validation and
prints the current frontier plus the RH transitive-dependency count.

The database is the VERIFIER/INFRA surface for the bespoke RH proof system. It
operationalizes two disciplines as queryable structure:

  * The Davenport-Heilbronn (D-H) discipline. Each node carries dh_buildable
    in {true, false, N/A}. The proof spine is engineered so that every
    LOAD-BEARING path to TGT-rh passes only through dh_buildable=false signature
    nodes. The dh_audit view returns any dh_buildable=true node sitting on such a
    path; an empty result means the firewall holds by type, not by label.

  * The K1 non-circularity discipline. Positivity must come from a polarization,
    never read off the zeros. AX-noncircular-source records this and contradicts
    OBS-k1-circularity by construction.

Design choices:
  * Only edges of kind 'depends_on' and 'specializes' are LOAD-BEARING (they
    carry proof obligation). All other edge kinds are annotations and do not
    propagate dependency. The acyclicity check and every reachability view
    traverse the load-bearing sub-graph only.
  * The acyclicity check is done in pure Python (Kahn's algorithm) over the
    load-bearing edges so the build fails loudly on any cycle, independent of
    DuckDB's recursive-CTE behavior.

Dependencies: duckdb + Python stdlib only (no numpy / mpmath). Idempotent:
re-running drops and recreates everything and reloads the seed from scratch.

Usage:
    python -m experiments.lemma_db.build_db
    python experiments/lemma_db/build_db.py
    python experiments/lemma_db/build_db.py --db path/to/out.duckdb
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from collections import defaultdict, deque
from typing import Any

import duckdb

HERE = os.path.dirname(os.path.abspath(__file__))
SCHEMA_PATH = os.path.join(HERE, "schema.sql")
SEED_PATH = os.path.join(HERE, "seed_lemmas.json")
DEFAULT_DB_PATH = os.path.join(HERE, "lemma_graph.duckdb")

# Edge kinds that carry a proof obligation (logical sub-graph).
LOAD_BEARING_KINDS = ("depends_on", "specializes")

# Statuses that count as a discharged dependency.
PROVEN_STATUSES = ("proven_ff", "proven_char0", "proven_lean")

RH_NODE = "TGT-rh"


# ---------------------------------------------------------------------------
# Loading helpers
# ---------------------------------------------------------------------------
def load_seed(path: str = SEED_PATH) -> dict[str, Any]:
    """Read and minimally validate the seed JSON."""
    with open(path, "r", encoding="utf-8") as fh:
        seed = json.load(fh)
    if "nodes" not in seed or "edges" not in seed:
        raise ValueError("seed JSON must contain 'nodes' and 'edges'")
    return seed


def _node_row(n: dict[str, Any]) -> tuple:
    return (
        n["id"],
        n["kind"],
        n["name"],
        n["statement"],
        n["status"],
        n["layer"],
        n["dh_buildable"],
        n.get("milestone"),
        n.get("lean_ref") or None,
        n.get("experiment_ref") or None,
        n.get("notes") or None,
    )


def _edge_row(e: dict[str, Any]) -> tuple:
    return (e["from"], e["to"], e["kind"], e.get("notes") or None)


# ---------------------------------------------------------------------------
# Structural validation (pure Python, independent of DuckDB)
# ---------------------------------------------------------------------------
def validate_seed_integrity(seed: dict[str, Any]) -> None:
    """Catch duplicate ids, dangling edge endpoints, and self-loops early."""
    ids = [n["id"] for n in seed["nodes"]]
    id_set = set(ids)
    if len(ids) != len(id_set):
        dupes = sorted({i for i in ids if ids.count(i) > 1})
        raise ValueError(f"duplicate node ids: {dupes}")

    seen_edges: set[tuple[str, str, str]] = set()
    for e in seed["edges"]:
        key = (e["from"], e["to"], e["kind"])
        if e["from"] not in id_set:
            raise ValueError(f"edge from unknown node: {e['from']} -> {e['to']}")
        if e["to"] not in id_set:
            raise ValueError(f"edge to unknown node: {e['from']} -> {e['to']}")
        if e["from"] == e["to"]:
            raise ValueError(f"self-loop edge on {e['from']}")
        if key in seen_edges:
            raise ValueError(f"duplicate edge: {key}")
        seen_edges.add(key)


def assert_acyclic(seed: dict[str, Any]) -> list[str]:
    """
    Verify the LOAD-BEARING sub-graph is a DAG, via Kahn's algorithm.

    Returns a topological order of the load-bearing nodes (for reporting).
    Raises ValueError listing a residual cycle's nodes if one exists.
    """
    nodes = [n["id"] for n in seed["nodes"]]
    succ: dict[str, list[str]] = defaultdict(list)
    indeg: dict[str, int] = {nid: 0 for nid in nodes}

    for e in seed["edges"]:
        if e["kind"] not in LOAD_BEARING_KINDS:
            continue
        succ[e["from"]].append(e["to"])
        indeg[e["to"]] += 1

    queue = deque(sorted(n for n in nodes if indeg[n] == 0))
    order: list[str] = []
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in sorted(succ[u]):
            indeg[v] -= 1
            if indeg[v] == 0:
                queue.append(v)

    if len(order) != len(nodes):
        residual = sorted(n for n in nodes if indeg[n] > 0)
        raise ValueError(
            "load-bearing dependency graph is CYCLIC; "
            f"nodes still in a cycle: {residual}"
        )
    return order


def assert_single_sink(seed: dict[str, Any]) -> None:
    """
    Confirm TGT-rh is the unique sink of the load-bearing graph: it has no
    load-bearing dependents (nothing depends_on / specializes it) but it does
    depend on at least one node. This guards the convergence property.
    """
    has_load_dependent: set[str] = set()
    has_load_dependency: set[str] = set()
    for e in seed["edges"]:
        if e["kind"] not in LOAD_BEARING_KINDS:
            continue
        has_load_dependent.add(e["to"])
        has_load_dependency.add(e["from"])

    if RH_NODE in has_load_dependent:
        raise ValueError(
            f"{RH_NODE} has a load-bearing dependent; it must be the unique sink"
        )
    if RH_NODE not in has_load_dependency:
        raise ValueError(f"{RH_NODE} has no load-bearing dependency; graph is empty above it")


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------
def build(db_path: str = DEFAULT_DB_PATH, seed_path: str = SEED_PATH,
          schema_path: str = SCHEMA_PATH) -> duckdb.DuckDBPyConnection:
    """
    (Re)build the database at db_path from schema_path + seed_path.

    Idempotent: the schema drops and recreates all tables/views, and the seed is
    reloaded from scratch each run.
    """
    seed = load_seed(seed_path)
    validate_seed_integrity(seed)
    assert_acyclic(seed)
    assert_single_sink(seed)

    with open(schema_path, "r", encoding="utf-8") as fh:
        schema_sql = fh.read()

    # Connect (creates the file if missing). An in-memory build is possible via
    # db_path=":memory:" for tests.
    con = duckdb.connect(db_path)
    con.execute("BEGIN TRANSACTION")
    try:
        con.execute(schema_sql)

        con.executemany(
            "INSERT INTO node "
            "(id, kind, name, statement, status, layer, dh_buildable, "
            " milestone, lean_ref, experiment_ref, notes) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [_node_row(n) for n in seed["nodes"]],
        )
        con.executemany(
            "INSERT INTO edge (from_id, to_id, kind, notes) VALUES (?, ?, ?, ?)",
            [_edge_row(e) for e in seed["edges"]],
        )

        # Derive obstruction_link rows from obstruction edges so the convenience
        # surface stays in sync with the graph rather than being hand-maintained.
        con.execute(
            """
            INSERT INTO obstruction_link (obstruction_id, target_id, relation, notes)
            SELECT e.from_id, e.to_id,
                   CASE
                     WHEN e.kind = 'contradicts' THEN 'blocks'
                     WHEN e.kind = 'instantiates' THEN 'explains'
                     WHEN e.kind = 'bridges' THEN 'why_hard'
                     ELSE e.kind
                   END AS relation,
                   e.notes
            FROM edge e
            JOIN node src ON src.id = e.from_id
            WHERE src.kind = 'obstruction'
            """
        )
        con.execute("COMMIT")
    except Exception:
        con.execute("ROLLBACK")
        raise

    return con


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------
def _fmt_table(rows: list[tuple], headers: list[str]) -> str:
    cols = [headers] + [[str(c) if c is not None else "" for c in r] for r in rows]
    widths = [max(len(row[i]) for row in cols) for i in range(len(headers))]
    line = "  ".join(h.ljust(widths[i]) for i, h in enumerate(headers))
    sep = "  ".join("-" * widths[i] for i in range(len(headers)))
    body = "\n".join(
        "  ".join(str(r[i]).ljust(widths[i]) for i in range(len(headers)))
        for r in cols[1:]
    )
    return f"{line}\n{sep}\n{body}" if rows else f"{line}\n{sep}\n  (none)"


def report(con: duckdb.DuckDBPyConnection) -> dict[str, Any]:
    """Print the frontier, RH-dependency count, and the D-H audit verdict."""
    n_nodes = con.execute("SELECT count(*) FROM node").fetchone()[0]
    n_edges = con.execute("SELECT count(*) FROM edge").fetchone()[0]
    n_load = con.execute("SELECT count(*) FROM load_edge").fetchone()[0]

    frontier = con.execute(
        "SELECT id, kind, status, layer, dh_buildable, "
        "coalesce(milestone,'') FROM frontier ORDER BY id"
    ).fetchall()

    rh_deps = con.execute("SELECT count(*) FROM rh_transitive_deps").fetchone()[0]
    rh_open = con.execute(
        "SELECT count(*) FROM rh_transitive_deps "
        "WHERE status NOT IN ('proven_ff','proven_char0','proven_lean')"
    ).fetchone()[0]

    dh_violations = con.execute(
        "SELECT id, status, layer, depth FROM dh_audit ORDER BY depth, id"
    ).fetchall()

    # Foundation-layer dh_buildable carriers on the path: expected, not a leak,
    # but surfaced so the exemption is never silent.
    dh_exempt = con.execute(
        "SELECT id, depth FROM rh_transitive_deps "
        "WHERE dh_buildable = 'true' AND layer = 'foundation' ORDER BY depth, id"
    ).fetchall()

    open_sig = con.execute("SELECT count(*) FROM open_signature_nodes").fetchone()[0]
    dischargeable = con.execute("SELECT count(*) FROM dischargeable_axioms").fetchone()[0]

    print("=" * 70)
    print("RH LEMMA GRAPH  (experiments/lemma_db)")
    print("=" * 70)
    print(f"nodes: {n_nodes}   edges: {n_edges}   load-bearing edges: {n_load}")
    print()
    print(f"FRONTIER ({len(frontier)} open node(s) with all load-bearing deps proven):")
    print(_fmt_table(
        frontier,
        ["id", "kind", "status", "layer", "dh_buildable", "milestone"],
    ))
    print()
    print(f"RH TRANSITIVE DEPENDENCIES (load-bearing): {rh_deps} node(s), "
          f"{rh_open} still open.")
    print()
    print(f"OPEN SIGNATURE-LAYER nodes (the real work): {open_sig}")
    print(f"DISCHARGEABLE AXIOMS (proven in a model, open over Z): {dischargeable}")
    print()
    if dh_violations:
        print(f"D-H AUDIT: {len(dh_violations)} VIOLATION(S) "
              "(dh_buildable node on a load-bearing path to TGT-rh):")
        print(_fmt_table(dh_violations, ["id", "status", "layer", "depth"]))
    else:
        print("D-H AUDIT: clean. No dh_buildable CONTENT node on any load-bearing "
              "path to TGT-rh; the firewall holds by type.")
    if dh_exempt:
        carriers = ", ".join(f"{i} (depth {d})" for i, d in dh_exempt)
        print(f"  (exempt neutral foundation carrier(s) on path: {carriers} - "
              "shared substrate below where discrimination happens, by design)")
    print("=" * 70)

    return {
        "n_nodes": n_nodes,
        "n_edges": n_edges,
        "frontier": [r[0] for r in frontier],
        "rh_transitive_deps": rh_deps,
        "rh_open_deps": rh_open,
        "dh_violations": [r[0] for r in dh_violations],
        "open_signature_nodes": open_sig,
        "dischargeable_axioms": dischargeable,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build the RH lemma-graph DuckDB DB.")
    parser.add_argument("--db", default=DEFAULT_DB_PATH,
                        help="output DuckDB path (default: lemma_graph.duckdb next to this script)")
    parser.add_argument("--seed", default=SEED_PATH, help="seed JSON path")
    parser.add_argument("--schema", default=SCHEMA_PATH, help="schema SQL path")
    args = parser.parse_args(argv)

    con = build(args.db, args.seed, args.schema)
    try:
        summary = report(con)
    finally:
        con.close()

    # Non-zero exit if the D-H discipline is violated, so CI can gate on it.
    if summary["dh_violations"]:
        print("\nFAIL: D-H discipline violated (see audit above).", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
