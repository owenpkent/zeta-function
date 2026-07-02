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
mathematics is S1-S5 with UNCONDITIONAL polarity. M4 needs CONTINGENT polarity.
But the first aimed acquisition batch (acq1, the #119 disqualifier-complement)
found that CONTINGENT + complex-root is NECESSARY but NOT SUFFICIENT: the complement
is occupied by four distinct flavors of "contingent but still wrong", each giving a
screen. Together they form a near necessary-and-sufficient FINGERPRINT of M4's
polarity (a polarization = Weil/Rosati form):

  contingent  AND  complex-root half (#119, discriminant: t^2-4q < 0)
              AND  line axis        (not vertical spacing / central rank / strip width)
              AND  output-indefinite (a signature of the zeros, not a definite condition
                                      on the input measure-class)
              AND  prohibitive flip on a FIXED locus (failure forbidden; not curative,
                                      where the locus relocates and the zeros track it).

THE SELECTION-ORDER SCREEN (#143, from the circle-rooted interlacing kill) is the
mechanism form of the #119 discriminant screen: an averaging-plus-selection engine
(MSS-style interlacing families) certifies via a one-sided bound on an ORDERED
quantity; an exact locus (all roots ON a circle or line) has no native one-sided
order; so a candidate whose certifying step requires above-or-below-average selection
on the target locus itself presupposes either an operator realization (self-adjoint
or unitary, which manufactures the order as a real spectrum) or a positivity of the
Lee-Yang class (already graded wrong-polarity by #95/#119). See toy/circle_interlacing.py
and the killed circle-engine node in transfer_search.py.

THE MODULUS-ONLY-CONSUMER SCREEN (#146, ADVERSARY-passed 2026-07-02) is the
consumer-side dual of the #148 producer finding: a technology whose Weil/Deligne
contact is only through SIGN-FREE corollaries -- the modulus tier (|S| <= 2 sqrt p,
|alpha| <= q^{i/2}) or the angle/monodromy tier (weights in all degrees, monodromy
classifications, equidistribution laws such as vertical Sato-Tate) -- imports nothing
that varies under flipping the polarizing form Q -> -Q, and no geometric carrier
(cycle lattice + ample cone) crosses the border; so no signature can be re-emitted
downstream and the family (Kloostermania, exponential-sum technology, trace-function
machinery, the sieve parity-breakers) is generically retired as an M4 SOURCE while
staying fully alive as a purity (R1) consumer. 'Sign' means the S5 signature (which
class pairs positively), NOT eigenvalue phases (Gauss-sum signs, root numbers = S3
data) and NOT proof-internal oscillation (Kloosterman sign changes are Kuznetsov /
operator-sourced, the #143 branch). Tagging discipline (the Ihara boundary call): tag
the candidate's CLAIMED ROUTE to a signature, not the historical construction of its
examples (graph-RH's sign is operator-sourced even though LPS graphs consume Deligne).
Falsifier: an analytic argument importing the Hodge-index inequality itself. See
docs/03_research/parity_vs_polarization.md (the #146 dossier + ADVERSARY resolution).

Run:
  python -m experiments.lemma_db.breadth_corpus
"""

from __future__ import annotations

from dataclasses import dataclass


# ---------------------------------------------------------------------------
# The field-agnostic M4 skeleton (the query keys). See breadth_program.md sec 1.
# The last three axes (axis / flip / positivity_side) are the acq1 fingerprint
# dimensions; they default to 'na' so older rows need not set them.
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class Skeleton:
    lefschetz: bool        # S1 a Lefschetz operator (hard-Lefschetz)
    primitive: bool        # S2 a primitive decomposition
    duality: bool          # S3 a perfect pairing (the functional equation)
    t_slot: bool           # S4 a slot for the trace datum t (the Frobenius eigenvalue)
    signature: bool        # S5 a primitive-definite signature exists (a polarization)
    polarity: str          # S6 'contingent' (right) | 'unconditional' (wrong) | 'na'  <- DISCRIMINATOR
    noncircular: bool      # S7 proved without inputting the answer
    # context axes
    produces: str          # 'signature' | 'perfectness' | 'realization'
    dh_engages: bool       # engages the Euler product (distinguishes zeta from Davenport-Heilbronn)
    regime: str            # 'all-heights' | 'L-value' | 'Level-3' | 'na'
    root_half: str         # 'complex' | 'real' | 'na'  (#119 discriminant: t^2-4q vs 0)
    # acq1 fingerprint dimensions (why a CONTINGENT positivity can still be wrong)
    axis: str = "na"           # 'line' (RH) | 'spacing' | 'central-rank' | 'strip-width' |
                               # 'level' (of distribution, the sieve theta axis, #146) | 'na'
    flip: str = "na"           # 'prohibitive' (fixed locus) | 'curative' (locus relocates) | 'na'
    side: str = "na"           # 'output-indefinite' (RH) | 'input-definite' (measure-class) | 'na'
    # #143 mechanism dimension: where does the certifying step's ORDER come from?
    order_source: str = "na"   # 'selection' (above/below-average selection on an ordered
                               # quantity, MSS-style: the order is presupposed) |
                               # 'operator' (a self-adjoint/unitary realization the
                               # phenomenon carries natively manufactures the order) | 'na'
    # #146 dimension: how the candidate touches the Weil/Deligne (polarization) input.
    weil_consumption: str = "na"   # 'sign-free' (only sign-blind corollaries: eigenvalue
                                   # moduli/purity, dimensions, monodromy + angle-
                                   # equidistribution laws; invariant under Q -> -Q,
                                   # no carrier crosses the border) |
                                   # 'signature' (consumes the (1,n-1) sign itself,
                                   # Weil's Hodge-index route) |
                                   # 'producer' (produces purity with no polarization,
                                   # the Weil I engine, #148) | 'na'


@dataclass
class Entry:
    phenomenon: str
    field: str
    skel: Skeleton
    verdict: str           # TRANSFER-CANDIDATE | COMPONENT | WATCH | DISQUALIFIED | TARGET
    rule: str              # the disqualifier rule (if DISQUALIFIED), else ''
    note: str = ""


# The M4 target, fully fingerprinted.
M4 = Skeleton(
    lefschetz=True, primitive=True, duality=True, t_slot=True, signature=True,
    polarity="contingent", noncircular=True,
    produces="signature", dh_engages=True, regime="all-heights", root_half="complex",
    axis="line", flip="prohibitive", side="output-indefinite",
)


def _S(lef, pri, dua, tsl, sig, pol, ncirc, prod, dh, reg, root,
       axis="na", flip="na", side="na", order_source="na", weil_consumption="na"):
    return Skeleton(lef, pri, dua, tsl, sig, pol, ncirc, prod, dh, reg, root,
                    axis, flip, side, order_source, weil_consumption)


# ---------------------------------------------------------------------------
# The corpus. Append-only, deduplicated. Seeded from the eight-angle + four-area
# sweeps, the cohomology landscape, the transfer shortlist, and the acq1 batch.
# ---------------------------------------------------------------------------
CORPUS = [
    # --- transfer candidates / targets (the contingent, fully-fingerprinted rows) ---
    Entry("Weil/Rosati form on a surface /F_q", "algebraic geometry",
          _S(1,1,1,1,1,"contingent",1,"signature",1,"all-heights","complex",
             "line","prohibitive","output-indefinite", weil_consumption="signature"),
          "TRANSFER-CANDIDATE", "", "the master column = function-field RH = lever B; the template; "
          "consumes the S5 sign itself (Hodge index), the direction #146 never fires on"),
    Entry("Faltings-Hriljac arithmetic Hodge index", "Arakelov geometry",
          _S(1,1,1,0,1,"contingent",1,"signature",1,"all-heights","complex",
             "line","prohibitive","output-indefinite"),
          "TARGET", "", "proven, single surface; needs the PRODUCT Spec(Z)^2 + Frobenius Gamma_S"),
    Entry("CCM semilocal prolate W_{lambda,S}", "NCG / metaplectic",
          _S(1,1,1,1,1,"contingent",1,"signature",1,"all-heights","complex",
             "line","prohibitive","output-indefinite"),
          "TARGET", "", "door ajar = M4 at core; the un-eliminated metaplectic route"),
    Entry("Ihara zeta / Ramanujan graphs", "spectral graph theory",
          _S(1,0,1,1,1,"contingent",1,"signature",1,"all-heights","complex",
             "line","prohibitive","output-indefinite"),
          "COMPONENT", "", "the function-field RH shadow in graph clothing (lever B)"),
    Entry("Connes-Consani archimedean Weil positivity", "NCG",
          _S(1,1,1,0,1,"contingent",1,"signature",0,"all-heights","complex",
             "line","prohibitive","output-indefinite"),
          "COMPONENT", "", "proves the sign can be GEOMETRIC (rho=1 jump); K2-blind, Gamma-factor half"),
    Entry("Adiprasito-Huh-Katz (matroids)", "combinatorics",
          _S(1,1,1,0,1,"unconditional",1,"signature",0,"na","na"),
          "TARGET", "", "09A AHK lattice: needs a t-carrying Lefschetz element; sign source, wrong polarity bare"),
    # --- the wrong-polarity convex/log-concave engine (real-root half) ---
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
    Entry("Lee-Yang circle theorem (+ failure regime)", "statistical mechanics",
          _S(0,0,1,0,1,"contingent",1,"signature",0,"na","real","na","na","input-definite"),
          "DISQUALIFIED", "input/output split (#120) + discriminant (#119) + #95",
          "acq1: failure = measure leaves Laguerre-Polya class (input-definite, Euler-blind, Dobner S^#)"),
    Entry("Boucksom-Jonsson NA Monge-Ampere", "non-archimedean geometry",
          _S(0,0,1,0,1,"unconditional",0,"signature",0,"na","real"),
          "DISQUALIFIED", "#97", "valuative single place, archimedean-blind, no t-slot"),
    # --- acq1 batch: the #119 complement, occupied by four flavors of 'contingent but wrong' ---
    Entry("Riemann-Hilbert / equilibrium-measure transitions", "integrable systems / RMT",
          _S(0,0,1,0,1,"contingent",0,"realization",0,"Level-3","complex","na","curative","na"),
          "DISQUALIFIED", "curative-flip screen (#120)",
          "acq1: S-curves on the complex-root half, but the flip RELOCATES the band (curative), "
          "underlying energy convexity unconditional; K1 made concrete (locus solved-for)"),
    Entry("Transfer operator / Ruelle / Selberg dynamical zeta", "thermodynamic formalism",
          _S(1,0,1,1,1,"contingent",1,"realization",1,"all-heights","complex","strip-width","na","na",
             order_source="operator"),
          "DISQUALIFIED", "spectral-gap=zero-free-region screen (#120) + K1",
          "acq1: the gap is contingent but controls a STRIP WIDTH (Arch 4), not the line; Selberg-RH "
          "reaches the line by self-adjointness but has no zeta; zeta's zeros are SCATTERING RESONANCES "
          "off the self-adjoint axis (the absorption sign = M4's polarization sign)"),
    Entry("Berry-Tabor / GUE level-statistics transition", "quantum chaos",
          _S(0,0,0,0,0,"contingent",1,"realization",0,"Level-3","na","spacing","na","na"),
          "DISQUALIFIED", "wrong-axis screen (#120) + Level-3 (#1)",
          "acq1: level repulsion flips on the VERTICAL spacing law, orthogonal to the line; "
          "compatible with beta=0.51"),
    Entry("Katz-Sarnak symmetry type (low-lying zeros)", "automorphic / RMT",
          _S(1,1,1,1,1,"contingent",1,"realization",1,"L-value","complex","central-rank","na","na",
             weil_consumption="sign-free"),
          "DISQUALIFIED", "wrong-axis (#120) + L-value (#113) + circular (S7) + modulus-only (#146)",
          "acq1: arithmetic, but governs the CENTRAL POINT (rank); a corollary of RH where proven; "
          "its engine (Deligne-Katz equidistribution) is a tier-2 sign-free Weil consumption"),
    # --- acq2 batch (#121): the full-fingerprint test; the closest non-AG near-misses ---
    Entry("Bridgeland stability + support-property form", "derived categories / stability",
          _S(1,1,1,0,1,"unconditional",1,"realization",0,"na","na","na","curative","output-selection"),
          "DISQUALIFIED", "selection-not-sign (#121) + curative-flip (#120) + e3r (#48)",
          "acq2: a fixed indefinite Q on a fixed Mukai lattice (the rare ingredient), but Q's signature "
          "(2,n-2) NEVER flips -- class-MEMBERSHIP flips (selection), wall-crossing is curative; Q IS the "
          "WEIGHT-2 Hodge-Riemann polarization, one weight above Weil's weight-1 (1,n-1)"),
    Entry("Frobenius manifolds / Dubrovin connection", "GW theory / integrable systems",
          _S(0,0,1,0,0,"na",1,"realization",0,"na","na","na","curative","na"),
          "DISQUALIFIED", "curative-flip (#120) + D-H",
          "acq2: the static skeleton (fixed indefinite eta + spectral-parameter connection) but NO "
          "contingent polarization; the contingency is semisimplicity (eigenvalue collision), curative"),
    Entry("Gamma conjecture / Apery (quantum-cohomology zeta-values)", "GW theory / Hodge",
          _S(0,0,1,0,0,"na",1,"realization",0,"special-value","na","na","na","na"),
          "DISQUALIFIED", "special-value/period regime (#121)",
          "acq2: zeta VALUES zeta(k), k>=2, in the convergent half-plane where zeta has NO zeros; "
          "structurally deep (the Gamma-hat integral lattice) but one tier beyond #113"),
    Entry("Scattering / Eisenstein resonance sign (modular surface)", "automorphic spectral theory",
          _S(1,1,1,1,1,"unconditional",1,"realization",1,"all-heights","complex","line","curative","na"),
          "DISQUALIFIED", "K1 + de Branges #43 (Lax-Phillips = de Branges space of xi)",
          "acq2: F3 line-axis HIT (the one improvement over acq1 strip-width), but the positivity is a "
          "half-plane dissipativity bound (unconditional), not a line signature; resonances sit in the "
          "continuous spectrum where self-adjointness is inert; closes onto Connes/CCM/de Branges"),
    # --- #143: the selection-order kill (averaging-plus-selection engines) ---
    Entry("MSS interlacing families (averaging + extremal selection)",
          "polynomial method / spectral graph theory",
          _S(0,0,0,0,0,"na",1,"realization",0,"na","real","na","na","na",
             order_source="selection"),
          "DISQUALIFIED", "selection-order screen (#143) + discriminant (#119)",
          "#140/#143: sources sqrt(q) with NO variety, but the certifying step selects "
          "above/below average on an ORDERED real spectrum, so the order (= real-rootedness "
          "= self-adjointness) is presupposed; the circle-rooted variant does not exist "
          "(killed node in transfer_search.py, toy/circle_interlacing.py 11/11); the classical "
          "circle certificate (Schur-Cohn 1922) is instead FE + Hermitian PSD = the M4 shape"),
    # --- #146: the modulus-only-consumer kill (the sieve parity corpus; ADVERSARY-passed 2026-07-02) ---
    Entry("Sieve parity barrier / bilinear parity-breakers (Vinogradov Type I/II, "
          "Bombieri-Vinogradov, Deshouillers-Iwaniec, Friedlander-Iwaniec x^2+y^4, "
          "Zhang Type III, Sawin-Shusterman /F_q[T])", "analytic number theory (sieve)",
          _S(0,0,0,0,0,"na",1,"realization",1,"Level-3","real",
             "level","curative","input-definite", weil_consumption="sign-free"),
          "DISQUALIFIED", "modulus-only-consumer (#146) + wrong-axis: level (#146 flavor of #120) + "
          "input/output (#120) + curative (#120) + discriminant (#119)",
          "#146: every power-saving parity-break consumes Weil/Deligne purity through sign-free "
          "corollaries (moduli, or the FKM / Sawin-Shusterman angle/monodromy tier) and discards "
          "the S5 sign at the border: parity = the consumer-side shadow of R1, not M4; the mu-sign "
          "is an INPUT-side ambiguity (#120); Type II ranges are solved-for per problem (curative); "
          "Kloostermania's sign changes are Kuznetsov/operator-sourced (#143 branch); D-H is exempt "
          "by type (no Euler product = nothing to sieve), so dh_engages=1 records the structural "
          "precondition, not discrimination leverage; yields the sharpened R1 WATCH trigger "
          "(variety-free power-saving bilinear mu cancellation near sqrt x)"),
    # --- realization / K1 / perfectness rows (earlier sweeps) ---
    Entry("Hirzebruch signature operator", "index theory",
          _S(1,1,1,0,1,"na",1,"realization",0,"all-heights","na"),
          "DISQUALIFIED", "supertrace/grading split (#119)",
          "realizes the integer sigma but presupposes Hodge-Riemann; its grading IS the polarization"),
    Entry("Eta-invariant / APS signature defect", "index theory",
          _S(1,1,1,0,1,"na",1,"realization",0,"L-value","na"),
          "DISQUALIFIED", "L-value rule (#113, #119)", "eta = Shimizu L-value; special-value regime"),
    Entry("SUSY Witten index Tr(-1)^F", "physics / index theory",
          _S(1,1,1,0,0,"na",1,"realization",0,"L-value","na"),
          "DISQUALIFIED", "supertrace/grading split (#119) + L-value (#113)",
          "= Euler characteristic; the SIGNATURE grading is a different index theorem = M4"),
    Entry("Kudla arithmetic theta lift", "automorphic forms",
          _S(1,1,1,1,1,"contingent",1,"realization",1,"L-value","complex"),
          "DISQUALIFIED", "L-value rule (#113)", "native output a central L-derivative (BSD/Gross-Zagier)"),
    Entry("de Branges / Conrey-Li pairing", "analysis",
          _S(0,0,1,0,1,"contingent",1,"signature",1,"all-heights","complex",
             "line","prohibitive","output-indefinite"),
          "DISQUALIFIED", "#43 (strictly stronger than RH)", "fails for zeta at k=34; must be RH-EQUIVALENT"),
    Entry("Connes 1999 adele trace formula", "NCG / operator algebras",
          _S(1,0,1,1,0,"na",0,"realization",1,"all-heights","na"),
          "DISQUALIFIED", "R3.5 / K1 wall", "spectrum=zeros => positivity <=> RH, no content (paradigm K1)"),
    Entry("Bost-Connes / KMS type III_1", "operator algebras",
          _S(0,0,1,0,0,"na",1,"realization",1,"Re(s)>1","na"),
          "DISQUALIFIED", "K1 + Buchholz-Longo (#119)", "blind to the strip; graded-KMS modulus ~ ungraded"),
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
# Skeleton match score. POLARITY is the hard gate; the acq1 fingerprint dimensions
# (axis/flip/side) reward the M4 profile and penalize the wrong-but-contingent ones.
# ---------------------------------------------------------------------------
def match_score(s: Skeleton, target: Skeleton = M4) -> int:
    score = 0
    if s.polarity == "contingent":
        score += 6
    elif s.polarity == "unconditional":
        score -= 4
    score += {"signature": 4, "perfectness": 1, "realization": 0}.get(s.produces, 0)
    score += sum([s.lefschetz, s.primitive, s.duality, s.signature])
    if s.t_slot and target.t_slot:
        score += 2
    if s.noncircular:
        score += 1
    score += {"all-heights": 2, "Re(s)>1": 0, "na": 0,
              "Level-3": -2, "L-value": -3, "special-value": -3}.get(s.regime, 0)
    if s.dh_engages:
        score += 1
    if s.root_half == "complex":
        score += 1
    elif s.root_half == "real":
        score -= 2
    # acq1 fingerprint dimensions
    if s.axis == "line":
        score += 2
    elif s.axis in ("spacing", "central-rank", "strip-width", "level"):
        score -= 2
    if s.flip == "prohibitive":
        score += 2
    elif s.flip == "curative":
        score -= 2
    if s.side == "output-indefinite":
        score += 2
    elif s.side in ("input-definite", "output-selection"):
        score -= 2
    # #143: a certifying step that presupposes the order it selects on is a transfer debit
    if s.order_source == "selection":
        score -= 2
    # #146: a sign-free Weil/Deligne import can never source the signature
    if s.weil_consumption == "sign-free":
        score -= 2
    return score


# ---------------------------------------------------------------------------
# The disqualifier battery (EVALUATE). Structurally-encodable members. K1, the
# cheap-spectral pair, and the supertrace/grading split need a human/LLM read and
# are applied as entry tags. The acq1 batch added four screens (the fingerprint).
# ---------------------------------------------------------------------------
def battery(s: Skeleton) -> list:
    """Return the disqualifier rules that fire on this skeleton (empty = survives)."""
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
    # acq1 fingerprint screens (the #120 batch; 'level' = the fourth shadow flavor, #146)
    if s.axis in ("spacing", "central-rank", "strip-width", "level"):
        fired.append(f"wrong-axis screen #120 (flips on the {s.axis} axis, not the line"
                     + ("; level-of-distribution flavor #146" if s.axis == "level" else "") + ")")
    if s.flip == "curative":
        fired.append("curative-flip screen #120 (locus relocates and zeros track it; K1 made concrete)")
    if s.side == "input-definite":
        fired.append("input/output split #120 (definite on the input measure-class; Euler-blind)")
    # acq2 refinements (#121)
    if s.side == "output-selection":
        fired.append("selection-not-sign screen #121 (indefinite form present, but class-MEMBERSHIP "
                     "flips while the SIGNATURE stays fixed; selection = realization, the Bridgeland miss)")
    if s.regime == "special-value":
        fired.append("special-value/period regime #121 (zeta VALUES at k>=2 / periods, not zero-LOCATION; "
                     "one tier beyond the #113 central-value/BSD regime)")
    # #143 mechanism screen (the circle-rooted interlacing kill)
    if s.order_source == "selection":
        fired.append("selection-order screen #143 (averaging-plus-selection certifies via a one-sided "
                     "bound on an ORDERED quantity; an exact locus, all roots ON a circle or line, has "
                     "no native one-sided order, so the order is presupposed: an operator realization "
                     "(self-adjoint/unitary) or a Lee-Yang-class positivity, wrong polarity per #95/#119)")
    # #146 provenance screen (the modulus-only-consumer kill; ADVERSARY-passed 2026-07-02)
    if s.weil_consumption == "sign-free":
        fired.append("modulus-only-consumer screen #146 (the Weil/Deligne import is sign-free: moduli, "
                     "dimensions, monodromy/angle-equidistribution only, invariant under Q -> -Q; the S5 "
                     "signature never crosses the border and cannot be re-emitted, so the technology is "
                     "not an M4 SOURCE; it stays alive as a purity/R1 consumer, and as an ingredient in "
                     "assemblies whose sign is sourced elsewhere, per the #143 operator branch)")
    return fired


def screen(s: Skeleton) -> dict:
    """Screen a candidate: its score, the rules that fire, and whether it survives to a
    TRANSFER-CANDIDATE (the full M4 fingerprint + survives the battery)."""
    fired = battery(s)
    is_candidate = (s.polarity == "contingent" and s.t_slot and s.duality
                    and s.produces == "signature" and not fired)
    return {"score": match_score(s), "disqualifiers": fired, "transfer_candidate": is_candidate}


# ---------------------------------------------------------------------------
# The skeleton query (GENERATE) and ranking.
# ---------------------------------------------------------------------------
def query_transfer_candidates(corpus=CORPUS) -> list:
    hits = [e for e in corpus
            if e.skel.polarity == "contingent" and e.skel.t_slot and e.skel.duality
            and e.skel.produces == "signature" and not battery(e.skel)]
    return sorted(hits, key=lambda e: -match_score(e.skel))


def rank(corpus=CORPUS) -> list:
    return sorted(corpus, key=lambda e: (-match_score(e.skel), e.phenomenon))


# ---------------------------------------------------------------------------
# The M4 polarity FINGERPRINT (the acq1 yield): the near necessary-and-sufficient
# profile a contingent positivity must have to be a transfer candidate for M4.
# ---------------------------------------------------------------------------
FINGERPRINT = {
    "polarity": ("contingent", "the signature flips when a zero moves (not unconditional)"),
    "root_half": ("complex", "#119: t^2-4q < 0 (not the real-root convex/log-concave half)"),
    "axis": ("line", "#120: flips on the Re=1/2 LINE (not vertical spacing, central rank, or strip width)"),
    "side": ("output-indefinite", "#120/#121: an indefinite signature of the OUTPUT zeros whose SIGN "
             "FLIPS (not a definite INPUT-class condition #120, and not class-MEMBERSHIP selection on a "
             "fixed-signature form #121 -- the Bridgeland near-miss)"),
    "flip": ("prohibitive", "#120: failure is forbidden on a FIXED locus (not curative, where the locus "
             "relocates and the zeros track it)"),
}


def aim() -> dict:
    """Read the next aimed acquisition off the active disqualifiers. After acq2 the breadth search
    has CONVERGED: the fixed-indefinite-form space outside algebraic geometry is mapped (Bridgeland =
    the closest near-miss) and shown INSUFFICIENT. The fingerprint is now so tight that the residual
    profile IS M4 itself, so the productive next move is the construction, not more breadth draws."""
    return {
        "status": "CONVERGED (acq2): the full fingerprint is essentially 'a weight-1 (1,n-1) polarization "
                   "with a Frobenius t-slot whose SIGN flips, prohibitive on a fixed locus' = M4.",
        "what_acq2_showed": "Bridgeland supplies a fixed indefinite form but its SIGNATURE never flips "
                            "(selection, not sign; weight-2 not weight-1); the scattering sign is line-axis "
                            "but unconditional (a half-plane bound, not a line signature); Frobenius gives "
                            "the static skeleton with no contingent polarization. The rare ingredient "
                            "(a fixed indefinite form) exists in several fields; the SIGN-FLIP + the "
                            "Frobenius t-slot do not, outside arithmetic geometry.",
        "pivot": "breadth has done its compression job. The productive work is now the M4 CONSTRUCTION "
                 "(09A AHK arithmetic lattice; Faltings-Hriljac product + Gamma_S; the lever-B Spec(Z) "
                 "lift) and the R3_5.lean VERIFIER target (a discrete-vs-continuous predicate separating "
                 "the Selberg operator-exists case from the zeta scattering-resonance case).",
        "residual_breadth_draws": [
            "weight-1 sign-flipping forms with a Frobenius t-slot: the limiting MHS / Sen non-"
            "semisimplicity where the polarization DEGENERATES contingently (08D) -- but likely already "
            "on file; a genuinely new orbit point is required to justify another draw",
            "the BUILDER toy model: the self-inversive Schur-Cohn / Bezoutian form (acq1 Lee-Yang "
            "Reading B) -- a finite contingent (1,n-1) sign-flip to test arguments before the lift",
        ],
    }


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------
def demo() -> int:
    print("=" * 88)
    print("THE BREADTH CORPUS: positivity/signature phenomena indexed by the M4 skeleton")
    print("  master discriminator = S6 POLARITY; refined by the acq1 fingerprint (axis/flip/side)")
    print("=" * 88)
    print(f"\n  corpus: {len(CORPUS)} phenomena.  M4 target match_score = {match_score(M4)}\n")

    print("  THE M4 POLARITY FINGERPRINT (the acq1 yield; a contingent positivity must hit ALL):")
    for k, (v, why) in FINGERPRINT.items():
        print(f"    {k:11} = {v:18}  {why}")

    print("\n  RANKED by skeleton match:")
    for e in rank():
        print(f"   {match_score(e.skel):>3}  [{e.verdict:18}] {e.phenomenon}")

    print("\n  TRANSFER-CANDIDATES (full fingerprint + survive the battery):")
    for e in query_transfer_candidates():
        print(f"     - {e.phenomenon}  ({e.field})")

    print("\n  ACQ1 SCREENS demo (each #119-complement near-miss fails a distinct fingerprint axis):")
    for nm, sk in [
        ("Riemann-Hilbert (curative)", _S(0,0,1,0,1,"contingent",0,"realization",0,"Level-3","complex","na","curative","na")),
        ("transfer-operator (strip)", _S(1,0,1,1,1,"contingent",1,"realization",1,"all-heights","complex","strip-width","na","na")),
        ("Berry-Tabor (spacing)", _S(0,0,0,0,0,"contingent",1,"realization",0,"Level-3","na","spacing","na","na")),
        ("Lee-Yang failure (input)", _S(0,0,1,0,1,"contingent",1,"signature",0,"na","real","na","na","input-definite")),
    ]:
        fired = battery(sk)
        print(f"     {nm:30} -> {fired[0] if fired else 'survives'}")

    print("\n  #143 SELECTION-ORDER screen demo (MSS-style engines vs operator carriers):")
    for nm, sk in [
        ("MSS averaging+selection (no operator)",
         _S(0,0,0,0,0,"na",1,"realization",1,"na","na", order_source="selection")),
        ("Selberg/Laplacian (carries its operator)",
         _S(1,0,1,1,1,"contingent",1,"realization",1,"all-heights","complex","strip-width",
            "na","na", order_source="operator")),
    ]:
        sel = [r for r in battery(sk) if "selection-order" in r]
        print(f"     {nm:42} -> {sel[0][:60] + '...' if sel else 'selection-order screen does not fire'}")

    print("\n  #146 MODULUS-ONLY-CONSUMER screen demo (sign-free import vs the signed route):")
    for nm, sk in [
        ("Kloostermania / trace-function import (sign-free)",
         _S(0,0,0,0,0,"na",1,"realization",1,"na","na", weil_consumption="sign-free")),
        ("Weil/Rosati route (consumes the S5 sign itself)",
         _S(1,1,1,1,1,"contingent",1,"signature",1,"all-heights","complex",
            "line","prohibitive","output-indefinite", weil_consumption="signature")),
    ]:
        moc = [r for r in battery(sk) if "modulus-only" in r]
        print(f"     {nm:50} -> {moc[0][:56] + '...' if moc else 'modulus-only screen does not fire'}")

    print("\n  AIM (post-acq2: the breadth search has CONVERGED):")
    a = aim()
    print(f"     status: {a['status']}")
    print(f"     pivot:  {a['pivot']}")

    print("\n  HONEST NOTE: RETRIEVAL + SCREENING, a prior + a filter, not a transfer certificate.")
    print("  The scored output is the growth of the disqualifier battery (now ~15 screens; 4 from")
    print("  acq1, 2 from acq2, 1 from #143 selection-order, 1 from #146 modulus-only-consumer,")
    print("  ADVERSARY-passed 2026-07-02), not the count of areas surveyed. Every new row passes")
    print("  a builder->adversary + D-H/polarity control before entry.")
    print("  AIM: CONVERGED (see above).")
    print("=" * 88)
    return 0


if __name__ == "__main__":
    raise SystemExit(demo())
