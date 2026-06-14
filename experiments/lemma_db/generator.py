"""The move-library generator (Generative Engine, 6a) + quality-diversity archive (6c).

Spec: `docs/03_research/generative_engine.md` sections 3, 5, 6. The first organ that
PROPOSES. It applies structure-preserving moves to a seed formulation, emits the
variants, and runs each through the evaluate stack (the committed oracle's static
disqualifiers + the function-field shadow of `fq_shadow.py`). Survivors are
RH-consistent reformulations; the killed branches reproduce the project's
disciplines. A MAP-Elites archive bins every variant by its failure cell, so the
loop maps the space of distinct outcomes instead of climbing one hill.

HONEST SCOPE: this proposes reformulations and prunes them. It does not find new
proofs. A SURVIVE verdict means "not pruned by the cheap disciplines," never
"closer to M4" (the blind-spot invariant, generative_engine.md section 7).
"""

from __future__ import annotations

from dataclasses import dataclass, field, replace

from experiments.lemma_db.oracle import (
    Candidate, level_classifier, k1_noncircular, KILL,
)
from experiments.lemma_db.fq_shadow import (
    elliptic_eigenvalues, fq_shadow_check, SHADOW_KILL, SHADOW_NA,
)

# Outcome labels (the cells of the quality-diversity archive).
SURVIVE = "SURVIVE"            # passed every cheap discipline (an RH-consistent reformulation)
KILL_LEVEL = "kill:level"     # dropped to Level-3 statistics
KILL_K1 = "kill:k1"           # reads the zeros (circular)
KILL_FQ = "kill:fq_shadow"    # breaks the proven F_q theorem (off-circle)
VACUOUS = "vacuous:firewall"  # no Euler product: the positivity cannot be stated (AX-FORM)
UNTESTABLE = "untestable"     # abstract (q -> 1 limit): no cheap evaluation


@dataclass
class Formulation:
    name: str
    base: str                          # 'F_q' | 'abstract'
    p: "int | None"                    # the field size for an F_q instance
    eigenvalues: tuple                 # Frobenius eigenvalues, () if abstract
    has_euler: bool
    claim_type: str = "positivity"
    claims_rh_equivalent: bool = True
    inputs: frozenset = frozenset({"polarization"})
    lineage: tuple = ()                # the moves applied to reach this formulation


def seed() -> Formulation:
    """The Weil positivity on a real elliptic curve over F_5: the on-circle,
    Euler-bearing, Level-4, non-circular starting point."""
    return Formulation("Weil/F_5", "F_q", 5, elliptic_eigenvalues(5, 1), has_euler=True)


# ---------------------------------------------------------------------------
# The move library: structure-preserving rewrites, Formulation -> Formulation.
# Each is a standard mathematician's move; together they exercise every discipline.
# ---------------------------------------------------------------------------

def base_change(f: Formulation) -> Formulation:
    return replace(f, name="base-change->F_11", p=11, eigenvalues=elliptic_eigenvalues(11, 3),
                   lineage=f.lineage + ("base_change",))


def raise_q(f: Formulation) -> Formulation:
    return replace(f, name="raise-q->F_13", p=13, eigenvalues=elliptic_eigenvalues(13, 4),
                   lineage=f.lineage + ("raise_q",))


def dualize(f: Formulation) -> Formulation:
    return replace(f, name="dualize", lineage=f.lineage + ("dualize",))


def perturb_offline(f: Formulation) -> Formulation:
    e = f.eigenvalues
    pushed = (e[0] * 1.3,) + tuple(e[1:]) if e else e
    return replace(f, name="perturb-offline", eigenvalues=pushed,
                   lineage=f.lineage + ("perturb_offline",))


def drop_euler(f: Formulation) -> Formulation:
    return replace(f, name="drop-euler", has_euler=False, lineage=f.lineage + ("drop_euler",))


def degenerate_q1(f: Formulation) -> Formulation:
    return replace(f, name="degenerate-q1", base="abstract", p=None, eigenvalues=(),
                   lineage=f.lineage + ("degenerate_q1",))


def read_zeros(f: Formulation) -> Formulation:
    return replace(f, name="read-zeros", inputs=f.inputs | {"zero_locations"},
                   lineage=f.lineage + ("read_zeros",))


def go_statistical(f: Formulation) -> Formulation:
    return replace(f, name="go-statistical", claim_type="statistical",
                   claims_rh_equivalent=False, lineage=f.lineage + ("go_statistical",))


MOVES = [base_change, raise_q, dualize, perturb_offline, drop_euler,
         degenerate_q1, read_zeros, go_statistical]


# ---------------------------------------------------------------------------
# Evaluate: compose the committed oracle's static disqualifiers + the F_q shadow.
# Cheapest first: level -> k1 (static, reuse oracle) -> firewall -> F_q shadow.
# ---------------------------------------------------------------------------

@dataclass
class GenVerdict:
    formulation: str
    outcome: str                 # one of the cell labels above
    defect: "float | None"       # F_q circle defect when applicable
    cell: tuple                  # MAP-Elites cell: (base, has_euler, outcome)


def _candidate(f: Formulation) -> Candidate:
    return Candidate(f.name, f.claim_type, f.claims_rh_equivalent, frozenset(f.inputs))


def evaluate(f: Formulation) -> GenVerdict:
    c = _candidate(f)
    if level_classifier(c).result == KILL:
        return GenVerdict(f.name, KILL_LEVEL, None, (f.base, f.has_euler, KILL_LEVEL))
    if k1_noncircular(c).result == KILL:
        return GenVerdict(f.name, KILL_K1, None, (f.base, f.has_euler, KILL_K1))
    if not f.has_euler:
        return GenVerdict(f.name, VACUOUS, None, (f.base, f.has_euler, VACUOUS))
    shadow, defect = fq_shadow_check(f.eigenvalues, f.p)
    if shadow == SHADOW_NA:
        return GenVerdict(f.name, UNTESTABLE, None, (f.base, f.has_euler, UNTESTABLE))
    if shadow == SHADOW_KILL:
        return GenVerdict(f.name, KILL_FQ, defect, (f.base, f.has_euler, KILL_FQ))
    return GenVerdict(f.name, SURVIVE, defect, (f.base, f.has_euler, SURVIVE))


# ---------------------------------------------------------------------------
# The generation loop + the MAP-Elites archive.
# ---------------------------------------------------------------------------

def generate(start: Formulation, depth: int = 2) -> tuple:
    """Apply moves from the seed (and from survivors) up to `depth` rounds.
    Returns (all_verdicts, archive). The archive keeps one representative per cell,
    the quality-diversity map of distinct outcomes."""
    frontier = [start]
    seen = {start.name}
    verdicts = [evaluate(start)]
    archive: dict = {verdicts[0].cell: verdicts[0]}
    for _ in range(depth):
        nxt = []
        survivors = [f for f in frontier]
        for f in survivors:
            for move in MOVES:
                g = move(f)
                if g.name in seen:
                    continue
                seen.add(g.name)
                v = evaluate(g)
                verdicts.append(v)
                archive.setdefault(v.cell, v)        # first to fill the cell keeps it
                if v.outcome == SURVIVE:
                    nxt.append(g)                    # only survivors spawn the next round
        frontier = nxt
        if not frontier:
            break
    return verdicts, archive


def anti_theater(verdicts) -> dict:
    """Kills (and prunes) by discipline: the number that justifies the generator."""
    counts: dict = {}
    for v in verdicts:
        if v.outcome not in (SURVIVE, UNTESTABLE):
            counts[v.outcome] = counts.get(v.outcome, 0) + 1
    return counts


def demo() -> None:
    print("Move-library generator (6a) + quality-diversity archive (6c)\n")
    s = seed()
    verdicts, archive = generate(s, depth=2)
    print(f"  seed: {s.name}  (on-circle, Euler, Level-4, non-circular)\n")
    print("  proposed variants and their verdicts:")
    for v in verdicts:
        extra = f"  defect={v.defect:.2e}" if v.defect is not None else ""
        print(f"    {v.formulation:18} -> {v.outcome}{extra}")
    print(f"\n  ANTI-THEATER: {len(verdicts)} proposed, "
          f"{sum(anti_theater(verdicts).values())} pruned {dict(sorted(anti_theater(verdicts).items()))}")
    print(f"\n  QUALITY-DIVERSITY ARCHIVE: {len(archive)} distinct cell(s) filled")
    for cell, v in sorted(archive.items(), key=lambda kv: kv[0][2]):
        base, euler, outcome = cell
        print(f"    cell(base={base}, euler={euler}, {outcome:16}) <- {v.formulation}")
    print("\nThe generator PROPOSES; the disciplines PRUNE. drop-euler is vacuous "
          "(no Euler =\nno positivity to state), perturb-offline breaks the F_q theorem, "
          "read-zeros is\ncircular, go-statistical is Level-3. SURVIVE = not pruned, never "
          "'closer to M4'.")


if __name__ == "__main__":
    demo()
