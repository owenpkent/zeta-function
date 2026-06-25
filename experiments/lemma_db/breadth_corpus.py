"""The breadth corpus engine (the Breadth Program's operational organ).

Spec: `docs/03_research/breadth_program.md`. The human-readable atlas is
`breadth_corpus.md`. This module scales the Generative-Engine transfer search
(`transfer_search.py`, 6b) from "the lemma DB" to "all of mathematics", indexed by
the FIELD-AGNOSTIC M4 skeleton (S1-S7) so the corpus is queryable by STRUCTURE,
not by field name.

WHAT THIS IS AND IS NOT
-----------------------
RETRIEVAL + SCREENING, not a verdict. It (a) scores a structured corpus of
positivity/signature/polarization phenomena against the M4 skeleton, (b) runs the
disqualifier battery to screen a candidate, and (c) reads the disqualifier-complement
aim off the active kills (where to look next). It never certifies a transfer; that
stays a human/LLM judgement on the shortlist (the builder -> adversary loop).

THE MASTER DISCRIMINATOR is S6, POLARITY. Almost every positivity theorem in
mathematics is S1-S5 with UNCONDITIONAL polarity (Kahler/matroid/convex/Lorentzian
Hodge-Riemann): a (1, n-1) signature for every valid input, so it can never flip to
flag a violation. M4 needs CONTINGENT polarity: the Weil/Rosati form flips
PSD -> indefinite exactly when a zero leaves the line. The first question to any
candidate is "does your signature flip, and on what?".

Run:
  python -m experiments.lemma_db.breadth_corpus
"""

from __future__ import annotations

from dataclasses import dataclass, field as _field


# ---------------------------------------------------------------------------
# The field-agnostic M4 skeleton (the query keys). See breadth_program.md sec 1.
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class Skeleton:
    lefschetz: bool        # S1 a Lefschetz operator (hard-Lefschetz)
    primitive: bool        # S2 a primitive decomposition
    duality: bool          # S3 a perfect pairing (the functional equation)
    t_slot: bool           # S4 a slot for the trace datum t (the Frobenius eigenvalue)
    signature: bool        # S5 a primitive-definite signature exists (a polarization)
    polarity: str          # S6 'contingent' (right) | 'unconditional' (wrong) | 'na'  <- THE DISCRIMINATOR
    noncircular: bool      # S7 proved without inputting the answer
    # context axes
    produces: str          # 'signature' | 'perfectness' | 'realization'
    dh_engages: bool       # engages the Euler product (distinguishes zeta from Davenport-Heilbronn)
    regime: str            # 'all-heights' | 'L-value' | 'Level-3' | 'na'
    root_half: str         # 'complex' | 'real' | 'na'  (the #119 discriminant axis: t^2-4q vs 0)


@dataclass
class Entry:
    phenomenon: str
    field: str
    skel: Skeleton
    verdict: str           # TRANSFER-CANDIDATE | COMPONENT | WATCH | DISQUALIFIED | TARGET
    rule: str              # the disqualifier rule (if DISQUALIFIED), else ''
    note: str = ""


# The M4 target, as a skeleton (everything true, contingent polarity, complex-root half).
M4 = Skeleton(
    lefschetz=True, primitive=True, duality=True, t_slot=True, signature=True,
    polarity="contingent", noncircular=True,
    produces="signature", dh_engages=True, regime="all-heights", root_half="complex",
)


def _S(lef, pri, dua, tsl, sig, pol, ncirc, prod, dh, reg, root):
    return Skeleton(lef, pri, dua, tsl, sig, pol, ncirc, prod, dh, reg, root)


# ---------------------------------------------------------------------------
# The corpus (seeded from breadth_corpus.md: the eight-angle + four-area sweeps,
# the cohomology landscape, the transfer shortlist). Append-only, deduplicated.
# ---------------------------------------------------------------------------
CORPUS = [
    Entry("Weil/Rosati form on a surface /F_q", "algebraic geometry",
          _S(1,1,1,1,1,"contingent",1,"signature",1,"all-heights","complex"),
          "TRANSFER-CANDIDATE", "", "the master column = function-field RH = lever B; the template"),
    Entry("Faltings-Hriljac arithmetic Hodge index", "Arakelov geometry",
          _S(1,1,1,0,1,"contingent",1,"signature",1,"all-heights","complex"),
          "TARGET", "", "proven, single surface; needs the PRODUCT Spec(Z)^2 + Frobenius Gamma_S"),
    Entry("CCM semilocal prolate W_{lambda,S}", "NCG / metaplectic",
          _S(1,1,1,1,1,"contingent",1,"signature",1,"all-heights","complex"),
          "TARGET", "", "door ajar = M4 at core; the un-eliminated metaplectic route"),
    Entry("Adiprasito-Huh-Katz (matroids)", "combinatorics",
          _S(1,1,1,0,1,"unconditional",1,"signature",0,"na","na"),
          "TARGET", "", "09A AHK lattice: needs a t-carrying Lefschetz element; sign source, wrong polarity bare"),
    Entry("Ihara zeta / Ramanujan graphs", "spectral graph theory",
          _S(1,0,1,1,1,"contingent",1,"signature",1,"all-heights","complex"),
          "COMPONENT", "", "the function-field RH shadow in graph clothing (lever B)"),
    Entry("Connes-Consani archimedean Weil positivity", "NCG",
          _S(1,1,1,0,1,"contingent",1,"signature",0,"all-heights","complex"),
          "COMPONENT", "", "proves the sign can be GEOMETRIC (rho=1 jump); K2-blind, Gamma-factor half"),
    Entry("Hirzebruch signature operator", "index theory",
          _S(1,1,1,0,1,"na",1,"realization",0,"all-heights","na"),
          "DISQUALIFIED", "supertrace/grading split (#119)",
          "realizes the integer sigma but presupposes Hodge-Riemann; its grading IS the polarization"),
    Entry("Hodge-Riemann (Kahler)", "complex geometry",
          _S(1,1,1,0,1,"unconditional",1,"signature",0,"na","na"),
          "DISQUALIFIED", "e3r polarity (#48)", "the canonical wrong-polarity source"),
    Entry("Alexandrov-Fenchel / mixed volumes", "convex geometry",
          _S(1,1,1,0,1,"unconditional",1,"signature",0,"na","real"),
          "DISQUALIFIED", "e3r polarity (#48) + discriminant (#119)", "transfer-shortlist; wrong polarity"),
    Entry("Lorentzian / log-concave polynomials", "combinatorics/optimization",
          _S(1,1,1,0,1,"unconditional",1,"signature",0,"na","real"),
          "DISQUALIFIED", "discriminant screen (#119)", "real-rooted: the wrong half of t^2-4q"),
    Entry("Tropical / Berkovich Hodge-Riemann", "tropical geometry",
          _S(1,1,1,0,1,"unconditional",1,"signature",0,"na","real"),
          "DISQUALIFIED", "discriminant (#119) + #97", "same family, real-root half"),
    Entry("Lee-Yang circle theorem", "statistical mechanics",
          _S(0,0,1,0,1,"unconditional",1,"signature",0,"na","real"),
          "DISQUALIFIED", "discriminant (#119) + #95", "all-positive on a circle; real-root half"),
    Entry("Boucksom-Jonsson NA Monge-Ampere", "non-archimedean geometry",
          _S(0,0,1,0,1,"unconditional",0,"signature",0,"na","real"),
          "DISQUALIFIED", "#97", "valuative single place, archimedean-blind, no t-slot"),
    Entry("Connes 1999 adele trace formula", "NCG / operator algebras",
          _S(1,0,1,1,0,"na",0,"realization",1,"all-heights","na"),
          "DISQUALIFIED", "R3.5 / K1 wall", "spectrum=zeros => positivity <=> RH, no content (paradigm K1)"),
    Entry("Bost-Connes / KMS type III_1", "operator algebras",
          _S(0,0,1,0,0,"na",1,"realization",1,"Re(s)>1","na"),
          "DISQUALIFIED", "K1 + Buchholz-Longo (#119)", "blind to the strip; graded-KMS modulus ~ ungraded"),
    Entry("SUSY Witten index Tr(-1)^F", "physics / index theory",
          _S(1,1,1,0,0,"na",1,"realization",0,"L-value","na"),
          "DISQUALIFIED", "supertrace/grading split (#119) + L-value (#113)",
          "= Euler characteristic; the SIGNATURE grading is a different index theorem = M4"),
    Entry("Eta-invariant / APS signature defect", "index theory",
          _S(1,1,1,0,1,"na",1,"realization",0,"L-value","na"),
          "DISQUALIFIED", "L-value rule (#113, #119)", "eta = Shimizu L-value; special-value regime"),
    Entry("Kudla arithmetic theta lift", "automorphic forms",
          _S(1,1,1,1,1,"contingent",1,"realization",1,"L-value","complex"),
          "DISQUALIFIED", "L-value rule (#113)", "native output a central L-derivative (BSD/Gross-Zagier)"),
    Entry("de Branges / Conrey-Li pairing", "analysis",
          _S(0,0,1,0,1,"contingent",1,"signature",1,"all-heights","complex"),
          "DISQUALIFIED", "#43 (strictly stronger than RH)", "fails for zeta at k=34; must be RH-EQUIVALENT"),
    Entry("Metaplectic / Weil rep over F_p (e1i)", "rep theory / harmonic analysis",
          _S(0,0,1,0,0,"na",1,"realization",0,"na","na"),
          "DISQUALIFIED", "finite-local sign cancels (#118)", "the Weil index is a phase the measure discards"),
    Entry("Tang prismatic Poincare duality", "p-adic Hodge theory",
          _S(0,0,1,0,0,"na",1,"perfectness",0,"na","na"),
          "DISQUALIFIED", "perfectness-not-sign (#71)", "duality proven, polarization absent"),
    Entry("Condensed/analytic 6-functors + norm-stack", "condensed mathematics",
          _S(0,0,1,0,0,"na",1,"perfectness",0,"na","na"),
          "WATCH", "perfectness-not-sign (#71/#119)",
          "best archimedean-inclusive substrate; gated on an archimedean Deligne-Illusie"),
    Entry("Bhatt-Lurie prismatic / WCart", "p-adic Hodge theory",
          _S(1,0,1,1,0,"na",1,"perfectness",0,"na","na"),
          "COMPONENT", "", "duality proven, no positivity; a substrate"),
    Entry("Hesselholt THH/TP/TC", "algebraic K-theory",
          _S(0,0,1,0,0,"na",1,"realization",0,"na","na"),
          "COMPONENT", "", "zeta = det_inf /F_q; needs a Z-flow + negative-definite cup"),
]


# ---------------------------------------------------------------------------
# Skeleton match score. POLARITY is the hard gate (the e3r kill, encoded):
# an UNCONDITIONAL signature scores near zero however many S1-S5 it has, because
# it can never flag an off-line zero. CONTINGENT polarity is the prize.
# ---------------------------------------------------------------------------
def match_score(s: Skeleton, target: Skeleton = M4) -> int:
    score = 0
    # S6 polarity: the discriminator.
    if s.polarity == "contingent":
        score += 6
    elif s.polarity == "unconditional":
        score -= 4                       # wrong polarity: actively demoted (cannot flip)
    # what it produces
    score += {"signature": 4, "perfectness": 1, "realization": 0}.get(s.produces, 0)
    # S1-S5 structural presence
    score += sum([s.lefschetz, s.primitive, s.duality, s.signature])
    if s.t_slot and target.t_slot:       # S4 a place for the trace datum
        score += 2
    if s.noncircular:                    # S7
        score += 1
    # regime: all-heights is RH; L-value is BSD (disqualified); Level-3 is statistical
    score += {"all-heights": 2, "Re(s)>1": 0, "na": 0, "Level-3": -2, "L-value": -3}.get(s.regime, 0)
    if s.dh_engages:                     # engages the Euler product
        score += 1
    if s.root_half == "complex":         # the #119 discriminant half RH lives on
        score += 1
    elif s.root_half == "real":
        score -= 2
    return score


# ---------------------------------------------------------------------------
# The disqualifier battery (EVALUATE). Each predicate screens a NEW candidate's
# skeleton and returns the killing rule, or None if it survives that gate.
# These are the structurally-encodable members; K1, cheap-spectral and the
# supertrace/grading split need a human/LLM read and are applied as entry tags.
# ---------------------------------------------------------------------------
def battery(s: Skeleton) -> list:
    """Return the list of disqualifier rules that fire on this skeleton (empty = survives)."""
    fired = []
    if not s.dh_engages:
        fired.append("Davenport-Heilbronn (does not engage the Euler product)")
    if s.polarity == "unconditional":
        fired.append("e3r polarity #48 (unconditional signature cannot flag an off-line zero)")
    if s.root_half == "real":
        fired.append("discriminant screen #119 (real-root half; RH is on the complex-root half)")
    if s.regime == "L-value":
        fired.append("L-value/order-of-vanishing rule #113 (BSD/Gross-Zagier regime, not all-heights)")
    if s.regime == "Level-3":
        fired.append("Level-3 (statistical; compatible with a beta=0.51 zero)")
    return fired


def screen(s: Skeleton) -> dict:
    """Screen a candidate: its score, the rules that fire, and whether it survives to a
    TRANSFER-CANDIDATE (contingent polarity + a t-slot + a duality + survives the battery)."""
    fired = battery(s)
    is_candidate = (s.polarity == "contingent" and s.t_slot and s.duality
                    and s.produces == "signature" and not fired)
    return {"score": match_score(s), "disqualifiers": fired, "transfer_candidate": is_candidate}


# ---------------------------------------------------------------------------
# The skeleton query (GENERATE): return contingent-polarity rows with a t-slot and
# a duality, ranked by match. The transfer shortlist, read by structure.
# ---------------------------------------------------------------------------
def query_transfer_candidates(corpus=CORPUS) -> list:
    hits = [e for e in corpus
            if e.skel.polarity == "contingent" and e.skel.t_slot and e.skel.duality
            and not battery(e.skel)]
    return sorted(hits, key=lambda e: -match_score(e.skel))


def rank(corpus=CORPUS) -> list:
    return sorted(corpus, key=lambda e: (-match_score(e.skel), e.phenomenon))


# ---------------------------------------------------------------------------
# Disqualifier-complement aim (Pillar 5.5): every kill names a HALF of the space;
# the productive next search is the complement. The discriminant screen kills the
# real-root half, so the aim is the contingent / complex-root / spectral-gap half.
# ---------------------------------------------------------------------------
COMPLEMENT_AIM = {
    "discriminant screen #119": {
        "kills": "the real-root half (t^2-4q >= 0): the convex/log-concave/Lee-Yang engine",
        "search": "CONTINGENT, complex-root, spectral-gap positivity (t^2-4q < 0)",
        "fields": [
            "Riemann-Hilbert / Plancherel-Rotach transitions (real roots becoming complex)",
            "the Lee-Yang FAILURE regime (zeros leaving the circle)",
            "transfer-operator / Ruelle spectral-gap positivity (contingent on the gap)",
            "the Berry-Tabor -> GUE transition (the contingency of level repulsion)",
        ],
    },
}


def aim() -> dict:
    """Read the next aimed acquisition off the active disqualifiers (the sharp draw)."""
    return COMPLEMENT_AIM


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------
def demo() -> int:
    print("=" * 84)
    print("THE BREADTH CORPUS: positivity/signature phenomena indexed by the M4 skeleton")
    print("  master discriminator = S6 POLARITY (contingent=right, unconditional=wrong)")
    print("=" * 84)
    print(f"\n  corpus: {len(CORPUS)} phenomena.  M4 target match_score = {match_score(M4)}\n")

    print("  RANKED by skeleton match (polarity-gated):")
    for e in rank():
        s = match_score(e.skel)
        print(f"   {s:>3}  [{e.verdict:18}] {e.phenomenon}  ({e.skel.polarity})")

    print("\n  TRANSFER-CANDIDATES (contingent polarity + t-slot + duality, survive the battery):")
    for e in query_transfer_candidates():
        print(f"     - {e.phenomenon}  ({e.field}) -- {e.note}")

    print("\n  DISQUALIFIER BATTERY demo (screening the wrong-polarity convex Hodge form):")
    convex = _S(1,1,1,0,1,"unconditional",1,"signature",0,"na","real")
    sc = screen(convex)
    print(f"     score={sc['score']}  transfer_candidate={sc['transfer_candidate']}")
    for r in sc["disqualifiers"]:
        print(f"       killed by: {r}")

    print("\n  DISQUALIFIER-COMPLEMENT AIM (the sharp next draw, off the #119 discriminant kill):")
    a = aim()["discriminant screen #119"]
    print(f"     kills:  {a['kills']}")
    print(f"     search: {a['search']}")
    for f in a["fields"]:
        print(f"       -> {f}")

    print("\n  HONEST NOTE: this is RETRIEVAL + SCREENING, a prior that says 'look here' and a")
    print("  filter that says 'not there'. It does not certify a transfer; the builder->adversary")
    print("  loop + a D-H/polarity control gate every new row. The scored output is the growth of")
    print("  the disqualifier battery, not the count of areas surveyed.")
    print("=" * 84)
    return 0


if __name__ == "__main__":
    raise SystemExit(demo())
