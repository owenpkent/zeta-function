# ADVERSARY review of the publication-tracking system

> Hostile review of `PUBLICATIONS.md` and the P4/P5/P6 dossiers, 2026-06-16. Severity-ranked.
> "PASS" means a claim survived this attack, not that it is correct. Cross-checked against
> `experiments/LEARNINGS.md`, `docs/03_research/soft_detector_wall.md`,
> `docs/03_research/spec_z_cohomology_landscape.md`, `docs/03_research/all_roads_to_the_signature.md`,
> `experiments/zero_free/README.md` + the e4e8/e4e9 sources, the Mathlib v4.30 source cache, and the
> upstream PR bodies. Method: D-H discipline lens + the project's own K1 circularity test + direct
> falsification against sources.

The work is, on the whole, unusually honest: the lit-checks did real demotions (P3, P5 STRONG -> DEVELOPING)
and the dossiers carry explicit caveats. My job is the residue. The single most important correction is
HIGH-1 (the P4 "distinctive" verdict is over-claimed AND, more seriously, the thesis is partly circular by
the project's own standard). The rest are MED/LOW.

---

## HIGH-1. P4's "convergence thesis is distinctive" is over-claimed, and the thesis's mathematical core is the folklore the project's own P3 lit-check demoted

**Severity: HIGH.** This is the load-bearing claim for the flagship paper, and it has two compounding problems.

**(a) "CONFIRMED distinctive" rests on ONE competitor read.** PUBLICATIONS.md line 194-202, the P4 outline
"Verdict," and the changelog all upgrade P4 from "evaluated" to "thesis CONFIRMED distinctive" on the
strength of a single deep read (Connes arXiv:2602.04022) plus an abstract-level skim of one MDPI survey.
The outline's own "Prerequisites" section (lines 161-168) simultaneously says full reads of BOTH competitors
plus "a deeper pass on the recent prismatic / THH-over-Z program surveys and Deninger's program" are still
required. You cannot be both "CONFIRMED distinctive" and "still need to read the adjacent programs to confirm
the thesis is genuinely unstated elsewhere." The word CONFIRMED is doing work the evidence does not support.
A survey thesis is exactly the kind of claim that dies to ONE prior paper you have not read; Deninger's
program papers (which the spine doc itself credits with the "regularized-determinant realization +
missing-positivity" framing) are the obvious unchecked source.

**(b) The mathematical core of the thesis is folklore, by the project's own ruling.** Strip the
operationalization (scorecard + D-H) and the residual convergence claim is: "every framework realizes zeta as
a determinant/trace, and RH is the missing polarization = the arithmetic Hodge standard conjecture / arithmetic
Rosati positivity." That equation is stated as classical in the project's own spine: `all_roads_to_the_signature.md`
line 38 calls it "the arithmetic analogue of Grothendieck's Hodge standard conjecture," and `soft_detector_wall.md`
demotes the scalar identity at its center to "write-down-not-research." This is precisely the move the P3
lit-check used to demote P3: "the thesis is the canonical Selberg-class folklore." P4 applies the SAME kind of
canonical framing (RH = a standard-conjecture positivity, Deninger/Connes/Grothendieck) and is NOT held to the
same standard. The genuinely novel residue of P4 is the same shape as P3's: an *operationalization* (the
Spec(Z) scorecard as a figure + the D-H discipline as a method), not the convergence claim.

**Fix.** Demote the verdict from "CONFIRMED distinctive" to "provisionally distinctive on operationalization;
convergence claim is known folklore, novelty is the scorecard + D-H method." Do the Deninger read and at least
one prismatic/THH-survey read BEFORE any "confirmed" language. Reframe the paper's contribution explicitly as
"we operationalize a known convergence intuition" (scorecard + discipline), mirroring exactly how P3 was honestly
reframed. This is not fatal to P4 (an operationalized survey can be a real contribution), but the current framing
over-sells the thesis as new mathematics when the project's own docs call it restated folklore.

**D-H lens.** The thesis itself passes the D-H discipline as a *statement* (it correctly says the polarization is
unbuildable for D-H, all_roads line 32-34). But "passes D-H as a statement" is necessary-not-sufficient for
"novel," and that is the gap here.

---

## HIGH-2. P5 mis-cites its load-bearing Heath-Brown SDP result to the wrong LEARNINGS entry; and that result lacks an `.md` writeup, unlike every sibling

**Severity: HIGH** (for a publication: a wrong citation on a result claimed as a paper's novel residue is a
referee-killer and a self-consistency failure).

PUBLICATIONS.md P5 (line 218) and `P5_zero_free_ceiling.md` (table row, line 76) attribute the Heath-Brown
multi-zero SDP closure ("best ratio <= 1, rank-2 certificate") to **LEARNINGS #21**. But the canonical
`### 21.` header in LEARNINGS.md (line 646) is the **function-field Hodge index** (e2g intersection signature),
a completely different result. The Heath-Brown SDP is actually documented as an *embedded* "**Finding #21**"
sub-label at LEARNINGS.md line 1256, inside a later cluster. So LEARNINGS.md has a genuine **numbering
collision**: two different results both labeled "#21." P5's citation resolves to the wrong one under the
document's own canonical numbering.

I verified the *substance* of the 4E.9 claim against the raw data (`e4e9_heath_brown_sdp.npz`): best ratio
1.0000 (rank-2 certificate at N=4, g=0.6), so the underlying result is real. The problem is purely the citation
and the source-document collision, but for a paper that is a precision failure.

Secondary: 4E.9 is the ONLY experiment in the P5 escape-route list with no `.md` writeup (only `.py/.png/.npz`),
and the public `experiments/zero_free/README.md` documents the thread only through 4A+4C and still lists 4E.8 as
"the remaining open computational direction" (README line 501) and 4E.8/4E.9 are NOT in the README at all.
So a reader following the cited README would conclude the SDP/SOS closures P5 leans on are unfinished. The
results exist in LEARNINGS + the e4e8 `.md`, but the README that P5 cites as "Source material in-repo" is stale.

**Fix.** (1) Renumber the embedded "Finding #21/#22/..." cluster in LEARNINGS.md to unique ids (they collide with
the top-level `### 8..#73` scheme); cite the corrected id in P5. (2) Add the 4E.8/4E.9 sections to
`experiments/zero_free/README.md` (or write `e4e9_heath_brown_sdp.md`) so the cited source actually documents the
closures. Until then, P5 cannot be drafted with a straight face: it cites a README that contradicts it.

---

## MED-3. P6's "no cheap unconditional path / route (b1)(ii) needs the resultant API" verdict under-investigated Mathlib: the resultant API it says is "needed" is already substantially present

**Severity: MED.** Does not overturn the "multi-month" bottom line, but the scoping mischaracterizes the route
(b1)(ii) availability and the verdict is stated more pessimistically than the source supports.

`P6_hasse_bound_scope.md` (line 95-100, the "Verdict") frames route (b1)(ii), the elementary resultant route, as
"PLAUSIBLE but substantial... needing the resultant API + careful multiplicity bookkeeping... Weeks, not days,"
and the Mathlib audit (line 54-77) lists only divisor theory under "Absent (the real work)," never checking
whether the resultant primitive exists. I grepped the v4.30 cache: Mathlib **has**
`Mathlib/RingTheory/Polynomial/Resultant/Basic.lean` including `resultant_eq_prod_roots_sub` (line 404) and
`resultant_eq_prod_eval` (line 476), i.e. the resultant-as-product-over-roots lemmas, plus
`Mathlib/Algebra/Polynomial/Roots.lean` (`card_roots`). These are exactly the primitives the scope doc says
route (b1)(ii) "needs" for the "#affine zeros = degree of the resultant" step. The audit did not find them.

This matters because the whole point of the M-b1.3 probe was to locate the precise blocker, and it reported
the blocker as "no divisor theory" while route (ii) explicitly avoids divisor theory and routes through the
resultant, which IS present. The honest verdict for (b1)(ii) is "the degree-count primitive is borrowable
(resultant API present); the real work is the multiplicity bookkeeping at infinity and at branch points,"
which is a meaningfully smaller and better-located task than "weeks of resultant API + bookkeeping."

**Fix.** Re-run the M-b1.3(ii) probe against `RingTheory/Polynomial/Resultant` and `Algebra/Polynomial/Roots`,
and restate the (b1)(ii) blocker as the pole/branch multiplicity bookkeeping specifically, not "the resultant
API." The "both paths multi-month" conclusion may still hold, but it should be derived from what is actually
missing, not from an audit that overlooked present API.

---

## MED-4. P4 draft §3 risks the exact overclaim its own drafting note forbids: "none reaches the polarization" contradicts the scorecard's two PROVEN (partial) polarizations

**Severity: MED.** The draft note (line 196) explicitly says "Do not upgrade any 'realization' to a
'polarization' claim." The complementary error is live and not guarded against: the draft repeatedly says
NO framework reaches the polarization (§1 line 39, §3 line 90 "the polarization is not," abstract "None of them
supplies"). But the source scorecard (`spec_z_cohomology_landscape.md` line 48, 54, and the whole "two proven
signatures that bracket the gap" section) marks **Faltings-Hriljac** and **Adiprasito-Huh-Katz** with **(iii) =
proven polarization** (the symbol is partial, and FH is "a real, proven polarization... reproduced end-to-end,"
AHK is "the Kahler package including Hodge-Riemann positivity... holds on any matroid"). They miss RH for
*other* reasons (too-local, too-blind), not for lack of a polarization.

The draft's blanket "none reaches the polarization" is therefore false as stated against the project's own
landscape. The precise claim is: "none reaches a polarization that is simultaneously global, carries the
Frobenius trace, and is RH-equivalent" (the conjunction of four proven-droppable properties, LEARNINGS #73).
That conjunction is the actual thesis; the slogan drops the qualifiers and becomes wrong.

**Fix.** Replace every "none reaches the polarization" with the qualified form ("none reaches a polarization
that is global AND trace-carrying AND RH-equivalent AND noncircular"). §4 (the stub) already states the
conjunction correctly; §3 and §1 and the abstract must be made consistent with §4 BEFORE drafting, or a
referee who knows Faltings-Hriljac/AHK will reject the framing on sight.

---

## MED-5. The evaluation gate has a blind spot: it has no circularity / K1 test, the project's primary RH-specific filter

**Severity: MED.** The 6-question gate (PUBLICATIONS.md lines 22-40) tests completeness, verification,
novelty, D-H soundness, honest-framing, and venue. It has **no K1 circularity check** ("does the claim
provably imply RH and does RH provably imply it?"), which is the project's stated primary adversarial filter
(R3.5 trace-formula trap) and is co-equal with D-H in the ADVERSARY role spec. This is a real gap: a
candidate that is a *restatement of RH* (a reformulation whose positivity is RH-equivalent) would pass all 6
gate questions. It is D-H-sound (correctly fails for D-H, because it IS RH), novel-looking, honestly framed,
and completable. The gate would wave it through, then it would die in refereeing as "you reformulated RH."

This is not hypothetical: P4's own thesis (HIGH-1), P8's "cup-is-a-polarization," and the parked de Branges /
Pólya-kernel items are all circularity-adjacent. The gate caught the parked items via novelty, but only because
someone happened to know the pre-emption. A K1 line would catch them structurally.

The D-H criterion's scoping (exempting Arch 2 and "pure formal results") is otherwise **correct**: Arch 2
genuinely requires the Euler product D-H lacks, and a true theorem about zeta (P1 `riemannZeta_conj`) is not an
RH-method. No objection there.

**Fix.** Add gate question 4b: "K1 circularity. Does the discovery provably imply RH, and does RH provably imply
it? If both, it is a reformulation of RH, not a step; it is publishable only as an explicitly-labeled
equivalence, never as 'progress toward RH.'" Apply it retroactively to P4 (the convergence thesis is a
reformulation by construction) and P8.

---

## MED-6. P6's standalone-publishable status rests on "the development, not the math," but the development is conditional on an unbuilt hypothesis (existence of A) the dossier admits is FLT-adjacent

**Severity: MED.** The Portfolio read (PUBLICATIONS.md line 79-81) lists P6 as "Standalone-publishable as a
formalization artifact." The dossier (line 252-253) is honest that everything is "conditional on the existence
of A," which is "Mathlib-absent, FLT-adjacent." The tension: a formalization paper whose headline is
"function-field RH for elliptic curves" but whose actual content is "the linear-algebra half downstream of an
unconstructed Frobenius-Tate-module representation" is a weaker artifact than the Portfolio framing implies. The
honest title (dossier line 268, "a conditional Lean formalization... reduced to the existence of A") is correct;
the Portfolio one-liner ("the Lean function-field RH chain") oversells it by dropping "conditional."

A referee will ask: what is the mathematical content of formalizing the eigenvalue extraction from a matrix A
whose existence (the only hard part) is assumed? The answer is "real but modest" (the dossier says so). The
Portfolio summary should carry that qualifier, because "standalone-publishable" in a venue like ITP requires the
artifact to be self-contained, and "conditional on an FLT-adjacent unbuilt object" is the opposite of
self-contained for the headline claim.

**Fix.** In the Portfolio read, change "P6 (the Lean function-field RH chain)" to "P6 (the CONDITIONAL Lean
reduction of function-field RH to the existence of A)." Keep the honesty that is already in the dossier body;
just propagate it to the one-line summary that an ORCHESTRATOR reads.

---

## LOW-7. P4 draft internal inconsistency: framework count ("five") and candidate count ("17") do not match the enumerations

**Severity: LOW** (cosmetic, but referee-visible).

- Draft §6 (line 167) says "across five independent frameworks." The abstract (line 13-16) enumerates SIX
  (spectral, arithmetic-geometric, direct positivity, analytic zero-free, prismatic, THH). §3 has THREE headers
  (function field, spectral, arithmetic-geometric). Pick one count and make the enumerations consistent.
- The outline (line 72) and the §4 stub (line 114) say "candidate cohomologies" and list 7 names, while the
  thesis and PUBLICATIONS say "17 candidate cohomologies" (LEARNINGS #73) and the source scorecard table has 18
  rows. The "17" vs "18 rows" vs "7 named in the figure" should be reconciled (some rows are sub-variants;
  state the counting rule).

**Fix.** One framework list, one candidate count with an explicit counting rule, used everywhere.

---

## LOW-8. P8's "delta vs Connes" is still an open action, yet P8 is carried as an evaluated dossier with a novelty claim

**Severity: LOW.** P8 (PUBLICATIONS.md line 316-323) states its own novelty is "Open action: lit check vs.
Connes" and that the e^{-4πx} rate + D-H-aware defect "are candidates" for the new delta. So P8's novelty is
explicitly unestablished, yet the registry lists it as "evaluated" with verification "Numerical + prolate
(semi-rigorous)." That is fine as a parked-pending item, but the Portfolio read folds P8 into P4 as "Pillar 3's
quantitative core" without flagging that its standalone novelty vs Connes is unchecked. If the Connes lit-check
finds the exp(-4πx) rate is already in Connes sec 6.4 (the soft_detector doc and LEARNINGS #52 both say Connes'
Figure 1 IS the exp(-4π·) law and the project recovered HIS constant), then P8 has NO standalone novelty and is
purely expository synthesis of Connes. That is a real risk the dossier half-acknowledges ("the project's stealth
window = Connes' ε(λ) near-radical").

**Fix.** Run the P8-vs-Connes lit check before P8 is cited as a "quantitative core." Likely outcome: the rate is
Connes', the D-H-aware defect D(γ)=|1-2β| is the genuine project residue. Frame P8 accordingly (rate = cited
from Connes, defect = new), or it overclaims the rate as project-novel.

---

## Verifications that PASSED (attacked, survived)

These I tried to break and could not, on the evidence checked:

- **Marginal-positivity numbers in P4 §5** (norms 55/69/123 -> 0.33, ~370x cancellation, A_arch indefinite,
  ε ~ e^{-4πx}, crosses float64 by x≈3, ~1e-71 at x=13, D(γ)=|1-2β| with 0.617 spike at γ≈85.7, e^γ≈1e37).
  All check out exactly against LEARNINGS #56, #52, #63 and soft_detector_wall.md. The draft's
  "verified 2026-06-16 against soft_detector_wall.md" note is accurate. **PASS.** (Caveat: these are
  computational findings about truncated forms, not theorems; the draft says so. The "~370x" and the indefinite
  A_arch correct a prior false docstring, which is a point in the project's favor.)

- **P5 line-restriction lemma + SDP/SOS closures** (4E.3 lemma; 4E.8 SOS saturates-not-exceeds; 4E.9 ratio<=1).
  The lemma is elementary and correct; the SDP/SOS data (`e4e8_sos_sdp.md`, `e4e9_heath_brown_sdp.npz`) confirm
  saturation without violation. The 1D-pre-emption honesty (Mossinghoff-Trudgian) is correct. **PASS on substance**
  (the citation/README problems are HIGH-2, separate).

- **P1/P2 Mathlib novelty against the v4.30 source cache.** `Complex.digamma` exists (`Digamma.lean`) with the
  recurrence (`digamma_apply_add_one`) and both special values, so P2's "those three pre-empted, reflection/
  iterated-recurrence/duplication remain" is accurate. `Complex.cot` exists (`cot_eq_cos_div_sin`,
  Complex/Trigonometric.lean), so P2's "reflection RHS-form resolved" holds. **PASS.**

- **P6 core absence claim.** No RiemannRoch, no AlgebraicGeometry divisor, no WeilDivisor/CartierDivisor in
  v4.30; `EllipticCurve/LFunction.lean` exists but carries no Hasse bound; no Weil-conjecture-for-curves anywhere.
  "Absent from every proof assistant" survives the Mathlib-side check. **PASS** (the resultant-API
  over-pessimism is MED-3, separate).

- **D-H control is live.** `python -m experiments._shared.smoke_test` = 9/9, including the first off-line zero
  at 0.8085 + 85.70i and the Li-detector-blind-to-D-H flip test. The "operational test" P4 leans on is not vapor.
  **PASS.**

- **Gate's D-H scoping** (exempting Arch 2 + pure formal). Correct, as argued in MED-5.

---

## Severity-ranked summary

| # | Severity | Claim attacked | Verdict |
|---|----------|----------------|---------|
| HIGH-1 | HIGH | P4 thesis "CONFIRMED distinctive" | over-claimed (one read) + core is project-admitted folklore; novelty is operationalization only |
| HIGH-2 | HIGH | P5 cites Heath-Brown SDP to LEARNINGS #21 | wrong entry (#21 is function-field Hodge index); LEARNINGS has a #21 collision; cited README is stale |
| MED-3 | MED | P6 (b1)(ii) "needs resultant API / weeks" | resultant API already present in v4.30 (audit missed it); blocker is mislocated |
| MED-4 | MED | P4 §3 "none reaches the polarization" | false vs scorecard's two proven (partial) polarizations (FH, AHK); needs the four-property qualifier |
| MED-5 | MED | Evaluation gate completeness | no K1 circularity question; a reformulation-of-RH passes all 6 |
| MED-6 | MED | P6 "standalone-publishable" one-liner | drops "conditional on unbuilt A"; oversells a modest artifact |
| LOW-7 | LOW | P4 framework/candidate counts | five vs six vs three; 17 vs 18 vs 7 |
| LOW-8 | LOW | P8 novelty vs Connes | rate is likely Connes', not project-novel; lit-check still open |

**No FAIL verdicts** (nothing is provably broken mathematics). The findings are over-claims, a wrong citation,
a stale cross-reference, a mislocated Mathlib blocker, and a gate gap. The portfolio's bones are sound; the
framing runs ahead of the evidence in exactly the places (P4 novelty, P5 citation) that a referee hits first.

**Single most important correction:** HIGH-1. The P4 "CONFIRMED distinctive" verdict must be downgraded and the
thesis reframed as "operationalized known convergence intuition" (its real, defensible novelty = scorecard +
D-H method), held to the same standard the project already applied when it honestly demoted P3 for being the
same kind of folklore. Do the Deninger + prismatic/THH reads before any "confirmed" language ships.
