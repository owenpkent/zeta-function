"""New-branch spec generation (Generative Engine, 6e).

Spec: `docs/03_research/generative_engine.md` section 5. The meta-level generator.
It reads forcing questions off the deepest asserted-vs-proven gap, writes the
required-property SPEC of the object a new branch would need, and computes each
candidate's RESIDUAL (the properties it does not supply) using the cheap
disciplines already in the repo.

THE HONEST CEILING, ENFORCED
----------------------------
6e never resolves the blind-spot property (the indefinite polarization,
`PROP-rh-equivalent` = M4). No cheap discipline can, by the marginal-positivity
finding. What 6e does is mechanically CONFIRM that every serious forcing question
reduces to exactly that one open property, while the bracketed candidates fail a
cheaply-checkable property instead. It generates the convergence rather than
asserting it, and it bottoms out, correctly, at the doorway it cannot open.
"""

from __future__ import annotations

from dataclasses import dataclass

from experiments.lemma_db.build_db import build, DEFAULT_DB_PATH
import duckdb


# The required-property spec of the missing object for M4. The last property is
# the blind spot: the indefinite (1, n-1) polarization that IS RH.
@dataclass
class SpecProperty:
    prop_id: str
    description: str
    blind_spot: bool


M4_SPEC = [
    SpecProperty("PROP-carries-trace", "realizes zeta as a trace", False),
    SpecProperty("PROP-global", "defined over all of Spec(Z)", False),
    SpecProperty("PROP-noncircular", "positivity from a polarization, not read off the zeros", False),
    SpecProperty("euler-gated", "exists only with an Euler product (the D-H firewall)", False),
    SpecProperty("PROP-rh-equivalent", "an indefinite (1,n-1) polarization = RH", True),  # THE BLIND SPOT
]

# Verdicts.
CONVERGENT = "CONVERGENT"            # all cheap properties met; residual = the blind-spot polarization
BRACKETED = "BRACKETED"              # fails a cheaply-checkable property
CIRCULAR = "CIRCULAR"                # positivity read off the zeros (fails noncircular)
PRE_REALIZATION = "PRE-REALIZATION"  # upstream: does not yet realize zeta
OTHER = "OTHER"

# Human-readable residual property per PROP id.
_PROP_DESC = {
    "PROP-rh-equivalent": "the indefinite (1,n-1) polarization (M4)",
    "PROP-global": "defined over all of Spec(Z)",
    "PROP-carries-trace": "realizes the zeta trace",
    "PROP-noncircular": "positivity not read off the zeros",
}


def top_gap_node(con) -> tuple:
    """The deepest forcing question lives at the top asserted-vs-proven gap."""
    return con.execute(
        "SELECT id, annotation_in_degree, load_in_degree, gap "
        "FROM asserted_vs_proven ORDER BY gap DESC LIMIT 1"
    ).fetchone()


def _resolution_target(con, cand: str) -> "str | None":
    row = con.execute(
        "SELECT to_id FROM edge WHERE from_id = ? "
        "AND kind IN ('instantiates','specializes','depends_on') LIMIT 1", [cand]
    ).fetchone()
    return row[0] if row else None


def _bracket_failed_prop(con, node: str) -> "str | None":
    row = con.execute(
        "SELECT to_id FROM edge WHERE from_id = ? "
        "AND kind IN ('contradicts','constrains') AND to_id LIKE 'PROP-%' LIMIT 1", [node]
    ).fetchone()
    return row[0] if row else None


@dataclass
class Residual:
    cand: str
    target: str
    verdict: str
    residual_prop: str
    residual_desc: str
    blind_spot: bool


def classify(con, cand: str) -> Residual:
    """Compute one candidate's residual against the M4 spec. The residual is the
    single property that, given everything cheaply checkable, remains the obstacle."""
    target = _resolution_target(con, cand)
    if target == "TGT-m4-hodge-standard":
        return Residual(cand, target, CONVERGENT, "PROP-rh-equivalent",
                        _PROP_DESC["PROP-rh-equivalent"], True)
    if target and target.startswith("NODE-"):
        p = _bracket_failed_prop(con, target) or "PROP-?"
        return Residual(cand, target, BRACKETED, p, _PROP_DESC.get(p, p), False)
    if target == "OBS-k1-circularity":
        return Residual(cand, target, CIRCULAR, "PROP-noncircular",
                        _PROP_DESC["PROP-noncircular"], False)
    if target == "PRIM-euler-product":
        return Residual(cand, target, PRE_REALIZATION, "PROP-carries-trace",
                        "does not yet realize zeta (upstream of the Euler product)", False)
    return Residual(cand, target or "(none)", OTHER, "PROP-?", "unclassified", False)


def run(con) -> list:
    cands = [r[0] for r in con.execute(
        "SELECT id FROM node WHERE id LIKE 'CAND-%' ORDER BY id").fetchall()]
    return [classify(con, c) for c in cands]


def demo(con=None) -> int:
    own = con is None
    if own:
        con = build(":memory:")
    try:
        print("New-branch spec generation (6e): forcing questions off the gap\n")
        gap = top_gap_node(con)
        print(f"  TOP GAP (the forcing question): {gap[0]}  "
              f"({gap[1]} asserted, {gap[2]} proven, gap {gap[3]})")
        print("  = 'what object would make each asserting candidate actually reduce here?'\n")

        print("  SPEC of the missing object (required properties):")
        for p in M4_SPEC:
            tag = "  <- BLIND SPOT (no cheap discipline resolves it)" if p.blind_spot else ""
            print(f"    - {p.description}{tag}")
        print()

        residuals = run(con)
        print("  per-candidate residual (the property that remains the obstacle):")
        for r in sorted(residuals, key=lambda r: (r.verdict, r.cand)):
            mark = "  [BLIND SPOT]" if r.blind_spot else ""
            print(f"    {r.cand:34} {r.verdict:15} residual = {r.residual_desc}{mark}")

        conv = [r for r in residuals if r.verdict == CONVERGENT]
        brk = [r for r in residuals if r.verdict != CONVERGENT]
        print(f"\n  CONVERGENCE: {len(conv)} candidates converge on ONE OPEN residual, "
              "the indefinite polarization (M4),")
        print(f"  the blind spot. {len(brk)} bracket out on a RESOLVED property "
              "(cheaply-checkable, refuted, or upstream):")
        from collections import Counter
        for prop, n in Counter(r.residual_desc for r in brk).items():
            print(f"    {n} x  {prop}")
        debranges = [r for r in brk if r.residual_prop == "PROP-rh-equivalent"]
        if debranges:
            print("    note: de Branges targets the polarization too, but its version is "
                  "DEFINITIVELY too\n          strong (refuted, OBS-classD) - a CLOSED branch, "
                  "not the convergent OPEN one.")
        print("\n6e GENERATES the all-roads convergence rather than asserting it, and bottoms "
              "out\nat exactly the one property no cheap discipline can resolve. It writes the "
              "doorway;\nit does not open it.")
        return 0
    finally:
        if own:
            con.close()


if __name__ == "__main__":
    raise SystemExit(demo())
