# Draft outline (P4): the flagship survey

> Status: **outline / skeleton**, 2026-06-16. Registry entry: [`../PUBLICATIONS.md`](../PUBLICATIONS.md) P4.
> This is the project's flagship expository contribution. It absorbs the research-tier coordinates
> (P3, P5, P7, P8) that the lit-checks showed are strongest bundled, not standalone. Read the
> "What makes this more than a catalog" and "Go/no-go" sections first.

## Working title

"All roads to one signature: the marginal-positivity compass and the Spec(ℤ) polarization gap."

(Alternatives: "Why every approach to the Riemann Hypothesis stops at the same step"; "The signature
is the gap: a structural survey of approaches to RH.")

## One-paragraph thesis

Every serious framework for the Riemann Hypothesis (spectral / Hilbert-Pólya, arithmetic-geometric /
Deninger-$\mathbb{F}_1$, direct positivity / Weil-Li, analytic / zero-free, and the newer
prismatic-cohomology and THH/TC programs) succeeds at *realizing* $\zeta$ as a determinant or a trace
of some operator or correspondence, and then stops at the *same* missing step: supplying a
**polarization** (an RH-equivalent positivity / Hodge-index signature) on that realization. We make
this convergence precise with a scorecard of candidate cohomologies for $\mathrm{Spec}(\mathbb{Z})$
graded against one requirement (does the candidate carry an RH-equivalent polarization?), and we argue
that the reason the gap is universal is **marginal positivity**: $\zeta$'s Weil-form positivity is a
near-zero cancellation residue with no buffer, so no soft or structure-blind method can close it. The
Davenport-Heilbronn discipline (the standard non-example) is the operational test that keeps the
classification honest. The survey's posture is that this is a **compass, not a verdict**: knowing the
gap is a single, precisely-located polarization tells the field where the proof must live.

## What makes this more than a catalog (positioning, load-bearing)

There are excellent existing surveys; the paper must say clearly what it adds beyond them.

- **Conrey, *The Riemann Hypothesis*** (Notices AMS 2003): a broad, classic catalog of approaches and
  evidence. Cataloging; not a convergence thesis.
- **Bombieri, *Problems of the Millennium: The Riemann Hypothesis*** (Clay): the authoritative problem
  statement, includes the D-H / Euler-product point. Foundational, not a survey of the modern
  cohomological programs.
- **Connes, *The Riemann Hypothesis: Past, Present and a Letter Through Time***
  ([arXiv:2602.04022](https://arxiv.org/abs/2602.04022), 2026): the closest competitor, a recent
  wide-angle survey culminating in the constructive Weil-positivity program. We **must** position
  against it explicitly. Our distinctive angle: Connes argues *from* one program (the trace formula /
  spectral realization) toward RH; we argue *across* programs that they all reach the same polarization
  gap, and we make the gap the organizing object via the scorecard. The project's own assessment of
  2602.04022 (the constructive $\eta_x$ manufactures on-line zeros for any admissible form, so the RH
  content is the unproven convergence = our $(N_\mathrm{off}, N_\mathrm{off})$ obstruction) is a data
  point in our favor and belongs in the survey.

**The distinctive contribution is the convergence claim, operationalized.** Not "here are the
approaches," but "here is the single step they all miss, here is a scorecard that locates it in each,
and here is the quantitative evidence (marginal positivity) for why it is hard." That is a thesis a
catalog does not make.

## The three pillars

### Pillar 1: all roads realize $\zeta$, RH is the signature

- Source: [`docs/03_research/all_roads_to_the_signature.md`](../docs/03_research/all_roads_to_the_signature.md)
  (LEARNINGS #30), [`docs/03_research/research_directions/08A_rosati_standard_conjecture.md`](../docs/03_research/research_directions/08A_rosati_standard_conjecture.md).
- Content: each framework produces $\zeta$ as $\det$ or $\mathrm{Tr}$ (Hesselholt's
  $\zeta = \det_\infty(s - \Theta \mid \mathrm{TP})$ over $\mathbb{F}_q$; the Weil explicit formula;
  the Connes trace; Deninger's regularized determinant). RH is not the realization but the
  *polarization / Hodge-index signature* on it. The function-field case is the theorem-side mirror
  (Weil's proof = the Hodge index on $C \times C$); over $\mathbb{Z}$ the same object's positivity is
  open and IS the arithmetic Hodge standard conjecture.

### Pillar 2: the Spec(ℤ) cohomology scorecard (the operationalization)

- Source: [`docs/03_research/spec_z_cohomology_landscape.md`](../docs/03_research/spec_z_cohomology_landscape.md)
  (LEARNINGS #73), the primitive-system / lemma-DB confirmation.
- Content: a table of candidate cohomologies (Deninger foliated, Connes/Connes-Consani,
  prismatic/WCart/Gurney, Hesselholt THH/TC, Arakelov/Faltings-Hriljac, $\mathbb{F}_1$, AHK) against
  the columns (i) realizes-$\zeta$-as-trace, (ii) FE-duality / perfectness, (iii) RH-equivalent
  polarization. The finding: every candidate has (i) and most have (ii); **none** has (iii), and (iii)
  is the conjunction of four proven-droppable properties (global $\wedge$ carries-trace $\wedge$
  RH-equivalent $\wedge$ noncircular). An object with all four proves RH. This is the survey's central
  figure.

### Pillar 3: marginal positivity is why the gap is universal (the compass)

- Source: [`docs/03_research/soft_detector_wall.md`](../docs/03_research/soft_detector_wall.md)
  (the frozen 5 load-bearing facts: #46 prime-block K2, #52 $e^{-4\pi x}$ wall, #56 370× cancellation,
  #61 cup-is-polarization, #63 $e^\gamma$ resolution cost), the four-level framing.
- Content: $\zeta$'s positivity collapses doubly-exponentially ($\varepsilon(x) \sim e^{-4\pi x}$) and
  is a $\sim$370× cancellation residue, so it sits exactly at the boundary; any structure-blind
  (Level-3) method is compatible with a world where some zero has $\beta = 0.51$. This is the
  quantitative reason the polarization cannot be supplied softly, and the stance is directional: it
  tells the field the proof must engage Level-4 / the exact structure of $\zeta$.

## How the research-tier coordinates fold in (P3, P5, P7, P8)

These are the evidence base, presented as sharp exhibits inside the pillars, not as separate claims:

- **P3 (D-H discipline, operationalized)** → the methodology that keeps Pillar 2 honest. The Schur
  counting law `schur_neg = #off-line heights` + the Epstein generalization = a quantitative sharpening
  of the Selberg-class / Bombieri-Conrey point. Goes in the "how we score" methods section.
- **P5 (no soft escape in zero-free methods)** → Pillar 3 evidence: "Architecture 4 maps its own
  ceiling." The line-restriction lemma + the V-K $2/3$-after-BDG context show the analytic soft method
  cannot close RH.
- **P7 (RH is $\Pi^0_1$)** → a short framing subsection: undecidability is a back door to truth, and
  the need for ever-sharper effective bounds at highly-composite $n$ is the logic-layer shadow of
  marginal positivity.
- **P8 (stealth window quantified)** → Pillar 3's quantitative core (the $e^{-4\pi x}$ rate, the
  D-H-aware defect $D(\gamma) = |1 - 2\beta|$), positioned against Connes' $\varepsilon(\lambda)$.

## Proposed structure

1. Introduction: RH as a target; the convergence thesis in one figure.
2. The four-level framing and why RH is Level 4 (positivity), not Level 3.
3. The realizations: each framework as a trace/determinant (Pillar 1).
4. The scorecard: candidate Spec(ℤ) cohomologies vs the polarization requirement (Pillar 2); the
   methods subsection with the D-H discipline (P3).
5. Marginal positivity: the quantitative compass (Pillar 3); the soft-method ceilings (P5); the
   stealth window (P8).
6. Logical status (P7) and the honest stance (compass, not verdict).
7. Conclusion: the proof must supply one precisely-located polarization; where to look (Rosati / Hodge
   standard conjecture, the M-ladder).

## Source material in-repo

- Spine: `all_roads_to_the_signature.md`, `08A_rosati_standard_conjecture.md`,
  `spec_z_cohomology_landscape.md`, `soft_detector_wall.md`, `researcher_mindset.md`.
- The four-level framing: `docs/02_graduate/log_correlated_fields_intro.md` §6.
- D-H: `experiments/_shared/davenport_heilbronn.py`, the lemma-DB CI gate.
- Connes assessment: `docs/03_research/connes_2602_letter_to_riemann.md`.
- LEARNINGS: #30, #46, #52, #56, #61, #63, #73 (and the P3/P5/P8 finding clusters).

## Lit-check (2026-06-16: thesis CONFIRMED distinctive after a deep read of the main competitor)

The strongest competitor was read in depth; the result is decisively in P4's favor.

**Connes, [arXiv:2602.04022](https://arxiv.org/abs/2602.04022)** (2026), a 165-year overview + a
"Letter to Riemann" original contribution (the prolate-spheroidal / Weil-quadratic-form method). The
deep read found that all three of P4's distinctive moves are **absent** there:

1. **No convergence thesis.** Connes acknowledges multiple approaches but argues *from* one program
   (noncommutative geometry / trace formula) toward RH. He does not claim the approaches converge on a
   single missing ingredient. P4's "all roads $\to$ one polarization gap" is not his framing.
2. **No Spec($\mathbb{Z}$) scorecard.** He discusses cohomology theories (étale, de Rham, crystalline,
   motives) but does **not** rank them against an RH-equivalent-polarization requirement. P4's central
   figure has no analogue there.
3. **Weil positivity is "one equivalent reformulation among many,"** not framed as THE universal
   polarization every approach lacks. And the **Davenport-Heilbronn discipline is not mentioned.**

   Note: Connes' "Letter to Riemann" uses exactly the prolate-spheroidal method that P4's Pillar 3 / P8
   engages with, so cite 2602.04022 as both the competitor survey *and* the source of that method (the
   repo's own assessment is [`connes_2602_letter_to_riemann.md`](../docs/03_research/connes_2602_letter_to_riemann.md)).

**"A Brief Survey on the RH and Some Attempts to Prove It"**, MDPI *Symmetry* 17(2):225 (2025): a brief
flat catalog of attempts (confirmed at abstract level; full text paywalled). No convergence thesis, no
scorecard. Lower-tier venue. Not a competitor on thesis.

Noise: several crank / AI-generated "proofs of RH". Not credible, but the noisy space *raises* the bar
for a credible new survey, which the scorecard + D-H discipline help clear.

**Verdict:** P4's distinctive thesis (all roads $\to$ one polarization gap, located by the
Spec($\mathbb{Z}$) scorecard, explained by marginal positivity, disciplined by D-H) is **confirmed
distinctive** against the strongest competitor. The survey is worth writing. One prerequisite remains:
an expert reader for the scorecard's (iii) polarization column.

## Prerequisites before writing the paper (not the outline)

- **Full reads of the two competitors** (Connes 2602.04022 and the MDPI Symmetry 2025 survey) plus a
  deeper pass on the recent prismatic / THH-over-$\mathbb{Z}$ program surveys and Deninger's program,
  to lock the positioning and confirm the convergence thesis is genuinely unstated elsewhere.
- **An expert reader** for the arithmetic-geometry pillar (the scorecard's (iii) column makes precise
  claims about what each cohomology does and does not supply).

## Go/no-go

**Honest read.** A survey lives or dies on whether the organizing thesis is genuinely new and useful.
Here the thesis (all roads → one polarization gap, located by a scorecard, explained by marginal
positivity) is **distinctive**: it is not a catalog, and its central figure (the Spec(ℤ) scorecard
against the polarization requirement) is the project's own and does not appear, as far as the
lit-checks show, in existing surveys. The risks: (a) Connes 2602.04022 occupies adjacent ground and is
recent, so positioning must be crisp; (b) the arithmetic-geometry claims in the scorecard need expert
vetting to survive refereeing; (c) it is the **long pole**, the most writing-intensive item in the
portfolio.

**Recommendation.** This is the right flagship. But sequence it **after** the two READY Mathlib PRs
(P1, P2) ship and **after** the full survey lit-check, because the survey's credibility is helped by
landing the concrete formal contributions first, and because the lit-check may reshape the thesis.
Treat this outline as the spec; do not start prose until the lit-check and an expert reader are lined
up.
