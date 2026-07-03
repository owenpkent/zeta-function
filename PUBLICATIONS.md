# PUBLICATIONS — publishable-discovery registry and evaluation

> Tracks every candidate publishable discovery across formal (Mathlib) and expository/research
> (arXiv) output, with an evaluation gate that decides tier and venue. Living document.
> Maintained alongside [`PHASE_STATE.md`](PHASE_STATE.md) and [`experiments/LEARNINGS.md`](experiments/LEARNINGS.md).

This file answers two questions: **what is publishable right now**, and **how do we decide** whether
a new finding clears the bar. `LEARNINGS.md` is the firehose of every finding; this file is the much
smaller subset that could leave the repo as a contribution, scored honestly.

A discovery and a paper are not the same thing. Each row below is a *discovery* (a `P#` id); a paper
may bundle several. The "Venue / bundle" field records the intended container.

**How to use this system:** [`publications/README.md`](publications/README.md) (the workflow guide).
**Adversarial review of this system:** [`publications/ADVERSARY_REVIEW.md`](publications/ADVERSARY_REVIEW.md)
(its findings are folded into the dossiers below, tagged "adversary HIGH/MED/LOW-n").

---

## Evaluation gate

Run this for every candidate before it earns a tier. It is the publication-side analogue of the
[Davenport-Heilbronn discipline](experiments/_shared/davenport_heilbronn.py): a structural sanity
check that catches the things that *feel* publishable but are not.

1. **Is the discovery itself complete?** A finding can be publishable while RH stays open, as long as
   the finding it claims is finished. Separate "the result is done" from "RH is done." (This is the
   RH-independence axis below, not a disqualifier.)
2. **Verification status.** One of: kernel-verified Lean (sorry-free + `#print axioms` clean) /
   rigorous proof / numerically validated (state precision + controls) / conjectural. Anything below
   "rigorous" needs the gap named explicitly in the dossier.
3. **Novelty / literature check.** Is this absent from the target corpus (Mathlib for formal; the
   published record for math)? Name the nearest prior work. If it is pre-empted, it goes to
   **Parked / pre-empted**, not the registry, with the reference that pre-empts it.
4. **D-H soundness (for any Arch 1/3/4 positivity, spectral, or zero-free claim).** Does the result
   respect the wrong-approach discipline, i.e. does it correctly NOT prove the analogous false
   statement for Davenport-Heilbronn? A method that "works" for D-H is wrong and is not publishable
   as an RH advance. Architecture 2 (arithmetic-geometric) and pure formal results are exempt.
4b. **K1 circularity (the project's primary RH-specific filter).** Does the discovery provably imply RH
   *and* does RH provably imply it? If both, it is a reformulation of RH, not a step toward it: it is
   publishable only as an explicitly-labeled equivalence, never as "progress toward RH." A
   reformulation passes 1-4 and 5-6 cleanly (it is D-H-sound because it *is* RH), so this question is
   what catches it. Applies to P4's convergence thesis and P8 by construction; both must be framed as
   operationalizations/equivalences, not new content.
5. **Honest framing (negative results).** A closed branch is first-class publishable when stating it
   saves the community effort: it must be a *provable* ceiling/no-go/blindness, not a failure to
   find. Frame as a coordinate, keep the math exactly as rigorous as it is.
6. **Venue fit + effort.** Pick the container (below) and the distance to submission.

Output of the gate: a **tier**, a **venue/bundle**, and the **one thing that has to happen next**.

### Venues

| Venue | For |
|-------|-----|
| **Mathlib PR** | Kernel-verified Lean absent from Mathlib. Workflow: [`lean/upstream/README.md`](lean/upstream/README.md). |
| **arXiv math.NT** | Research / methodology / negative-result notes and the survey. |
| **Formalization venue** (ITP / CPP / JAR) | A Lean development worth a paper in its own right (e.g. the function-field RH chain). |
| **Expository** | The flagship landscape/survey; possibly a journal expository slot. |

### Tiers

| Tier | Meaning |
|------|---------|
| 🟢 **READY** | Verified, novel, submittable now. Only mechanical/human steps remain. |
| 🔵 **STRONG** | Genuinely novel and rigorous; needs drafting, not new mathematics. |
| 🟡 **DEVELOPING** | Real contribution but needs more work, a lit check, or a bundle decision. |
| ⚪ **PARKED** | Not currently publishable as new (pre-empted, or a reformulation that detects the wrong thing). Kept for the record. |

### Pipeline status

`candidate → evaluated → drafting → ready → submitted → published` (or `withdrawn`).

---

## Portfolio read (what is actually standalone-publishable)

After lit-checking P5 and P3 (2026-06-16), a pattern is clear and worth stating up front: **the
research-tier "discoveries" are mostly sharp operationalizations of known ideas, not new theorems.**
P3's thesis is the Selberg-class folklore (Bombieri/Conrey); P5's 1D core is the Mossinghoff-Trudgian
program. Their novel residues are real but thin (a quantitative instrument; an elementary
line-restriction lemma), and each is strongest **bundled into the survey P4**, where "the soft methods
provably map their own ceiling" is exactly the evidence the survey is built on.

So the honest portfolio is:

- **Standalone-publishable, math finished:** P1, P2 (Mathlib PRs).
- **Standalone-publishable as a formalization artifact:** P6 (the **conditional** Lean reduction of
  function-field RH to the existence of `A`; novelty is the development, not the classical math).
  **Lit-check confirmed viable (2026-06-16):** the Hasse-Weil bound is absent from every proof assistant
  and is an explicit Mathlib future goal, so this is genuine territory. The one candidate that survived
  its lit-check intact. Caveat (adversary MED-6): the *finished* artifact is the linear-algebra half
  downstream of an unconstructed, FLT-adjacent `A`, so "standalone" means the conditional reduction, a
  real-but-modest formalization, not the unconditional Hasse bound.
- **One survey that absorbs the rest:** P4, bundling P3, P5, P7, P8 as operationalized coordinates.

Lit-check every research candidate before drafting it. The scorecard so far: P3 and P5 moved STRONG →
DEVELOPING (pre-empted theses); P6 confirmed viable. The pattern: the *positivity/analytic*
"discoveries" are operationalized folklore (fold into P4); the *formal* contributions (P1, P2, P6) are
the real standalone output.

---

## Registry

| ID | Discovery | Type | Verification | Tier | Venue / bundle | Status |
|----|-----------|------|--------------|------|----------------|--------|
| [P1](#p1) | `riemannZeta_conj`: conjugation symmetry of ζ | Formal (positive) | Lean, axiom-clean | 🟢 SUBMITTED | Mathlib PR | [mathlib4#41133](https://github.com/leanprover-community/mathlib4/pull/41133) |
| [P2](#p2) | Digamma reflection / iterated recurrence / duplication | Formal (positive) | Lean, axiom-clean | 🟢 SUBMITTED | Mathlib PR | [mathlib4#41132](https://github.com/leanprover-community/mathlib4/pull/41132) |
| [P3](#p3) | The Davenport-Heilbronn discipline, operationalized (Schur counting law + Epstein) | Methodology | Numerical (validated) + rigorous Li at n=336k | 🟡 DEVELOPING | Fold into P4 | lit-checked |
| [P4](#p4) | All-roads convergence + marginal-positivity thesis + Spec(ℤ) scorecard | Survey | Synthesis | 🟡 DEVELOPING | Expository / arXiv | draft written ([`publications/obstruction_map/`](publications/obstruction_map/)) |
| [P5](#p5) | No higher-dimensional / SDP / SOS / **variational** escape for the single-zero zero-free constant | Negative (closed branch) | Rigorous (line-restriction lemma) + SDP/LP certificates + variational QP (4F) | 🟡 DEVELOPING | arXiv math.NT note / fold into P4 | lit-checked |
| [P6](#p6) | Lean formalization of function-field RH for elliptic curves (deg = det route) | Formalization (positive) | Lean, axiom-clean (conditional on existence of A) | 🟡 DEVELOPING | Formalization venue | lit-checked ✓ viable |
| [P7](#p7) | RH is Π⁰₁ + the Lean kernel witness | Expository note | Lean anchors; logical fact classical | 🟡 DEVELOPING | Note / bundle into P4 | evaluated |
| [P8](#p8) | The stealth window quantified (e^{-4πx} wall, 370× cancellation, D-H-aware defect) | Analytic note | Numerical + prolate analysis | 🟡 DEVELOPING | Fold into P4 (no standalone) | lit-checked: rate is prior (Fuchs+Connes) |
| [P9](#p9) | Paired-subtorus circle-rootedness: E over conjugate-paired phases of det(zI−DU), U unitary, is circle-rooted (all m) | Theorem (positive) | Elementary proof, every step numerically verified (50-digit) | 🟡 DEVELOPING | arXiv math.CV note (4-6 pp), cross-list math.CO/math.PR | novelty-passed; **draft written** ([`publications/paired_subtorus/`](publications/paired_subtorus/), 5 pp, compiles); gate: checker verdicts + MathSciNet (human) + citation pins |
| [P10](#p10) | The Gauss-lemma height floor: minimal log-height of a prime-forced integer vanisher = ψ(x) exactly (the vF disc model has no Siegel-lemma slot); multiplicity rational-root floor absent from Mathlib | Negative (closed branch) + Formal | Lean, axiom-clean (#GF-1..#GF-5) + integer-exact Python; uniqueness clause numerics-only (#GF-6 candidate) | 🟡 DEVELOPING | Mathlib PR (generalized multiplicity rational-root floor); exposition folds into P4 counting-roads; no standalone note | novelty-passed 2026-07-02 |

---

## Candidate dossiers

Each dossier carries the six gate fields. `LEARNINGS #n` cross-references
[`experiments/LEARNINGS.md`](experiments/LEARNINGS.md).

### P1 {#p1}
**`riemannZeta_conj`: conjugation symmetry of the Riemann zeta function.** 🟢 SUBMITTED

- **Claim.** `ζ(conj s) = conj (ζ s)` for `s ≠ 1`, and the corollary that the zeros are
  conjugation-symmetric. The natural companion to Mathlib's `riemannZeta_one_sub`; together they
  generate the quadruple symmetry `{ρ, 1−ρ, conj ρ, 1−conj ρ}`.
- **Verification.** [`lean/ZetaRH/RiemannZetaConj.lean`](lean/ZetaRH/RiemannZetaConj.lean), sorry-free,
  `#print axioms` = `[propext, Classical.choice, Quot.sound]` against Lean/Mathlib v4.30.0,
  imports only Mathlib.
- **Novelty.** Absent from current Mathlib (lit-checked against the RiemannZeta API).
- **D-H soundness.** N/A (a true theorem about ζ, not an RH-method).
- **RH-independence.** Fully independent of the open content.
- **Venue / next.** **SUBMITTED 2026-06-28 as [mathlib4#41133](https://github.com/leanprover-community/mathlib4/pull/41133)**: ported to current master (v4.32.0-rc1, new module system), builds green, `#print axioms` clean, CI green (Build + Lint style), AI-use disclosed per Mathlib policy. Body archived at [`lean/upstream/riemann_zeta_conj_pr_body.md`](lean/upstream/riemann_zeta_conj_pr_body.md). **Next:** Owen engages the review in his own words (Mathlib AI policy forbids LLM-written review comments).

### P2 {#p2}
**Digamma reflection, iterated recurrence, duplication.** 🟢 SUBMITTED

- **Claim.** Three digamma identities absent from Mathlib: reflection (via `Complex.cot`), iterated
  recurrence, duplication.
- **Verification.** [`lean/ZetaRH/DigammaExtras.lean`](lean/ZetaRH/DigammaExtras.lean), axiom-clean,
  v4.30.0.
- **Novelty.** Of the six identities originally staged, Mathlib master now ships `Complex.digamma`
  with the recurrence and both special values (`ψ(1) = −γ`, `ψ(1/2) = −γ − 2 log 2`), so those three
  are pre-empted. The reflection, iterated-recurrence, and duplication formulas remain novel upstream
  candidates. The reflection RHS-form question is resolved (`Complex.cot` exists in v4.30.0).
- **D-H soundness.** N/A.
- **RH-independence.** Fully independent.
- **Venue / next.** **SUBMITTED 2026-06-28 as [mathlib4#41132](https://github.com/leanprover-community/mathlib4/pull/41132)**: ported to current master (the reflection uses the `Complex.cot` RHS), builds green, `#print axioms` clean, CI fully green, AI-use disclosed. Body archived at [`lean/upstream/digamma_pr_body.md`](lean/upstream/digamma_pr_body.md). **Next:** Owen engages the review in his own words.

### P3 {#p3}
**The Davenport-Heilbronn discipline, operationalized.** 🟡 DEVELOPING

> Reframed after the lit-check (2026-06-16). The *thesis* is canonical folklore; the defensible residue
> is the quantitative instrument (the Schur counting law + the Epstein generalization).

- **Claim (defensible core).** A quantitative, cross-architecture instrument for the Davenport-Heilbronn
  discipline: the Schur-complement two-clock decomposition of the Weil-form Gram matrix isolates an
  off-line obstruction ~30× sharper than the raw spectrum, with the exact counting law
  `schur_neg = #off-line heights`, `schur_dim = 2 × #off-line heights` (LEARNINGS #10, #18); the
  instrument **generalizes beyond D-H** to a structurally independent control (Epstein zeta of disc
  −47, LEARNINGS #19 / Arch 3L) with the same counting law; and it is wired as a build-time discipline
  (the lemma-DB CI gate, LEARNINGS #73).
- **Verification.** Numerical, high-precision, with controls; the Li-criterion leg is rigorous (D-H
  λ_n < 0 at n = 336,000; Epstein λ_n < 0 from n = 110,000; Selberg controls rigorously positive,
  LEARNINGS #3). These are computational findings about a truncated Gram matrix, not theorems.
- **Novelty (post-lit-check, honest).** The **thesis is NOT novel.** "Any RH-style argument that does
  not use the Euler product is suspect because D-H has a functional equation but off-line zeros" is the
  canonical Selberg-class philosophy, stated explicitly in Bombieri's Clay problem description, Conrey's
  *The Riemann Hypothesis* (Notices AMS 2003), and the Selberg-class literature (Selberg 1992;
  Conrey-Ghosh 1993). D-H is *the* textbook non-example. The **candidate-novel residue** is the specific
  quantitative instrument (the Schur counting law + the Epstein cross-validation + the CI-gate
  operationalization), which I did not find in the literature, but which is an operationalization of a
  known idea rather than a new theorem.
- **D-H soundness.** It *is* the discipline.
- **RH-independence.** Fully independent; a meta-instrument about methods.
- **Venue / next.** **Fold into P4** as the "operationalizing the Selberg-class discipline" section
  (its strongest home: the quantitative instrument is a sharp exhibit inside the survey, not a
  standalone paper). **Next:** write the counting-law statement + the Epstein generalization as a P4
  subsection, positioned as a sharpening of Bombieri-Conrey, not a new thesis.

### P4 {#p4}
**All-roads convergence + the marginal-positivity thesis + the Spec(ℤ) cohomology scorecard.** 🟡 DEVELOPING

- **Claim.** The flagship narrative. (i) Every candidate framework (spectral, arithmetic-geometric,
  positivity, prismatic/THH) realizes ζ as a determinant or trace; RH is the **signature/positivity**,
  the same object in every framework, and that is the irreducible content (LEARNINGS #30). (ii) The
  **marginal-positivity thesis**: RH is just barely true; the Weil-form minimal eigenvalue is a
  cancellation residue with no buffer for soft proofs, so any proof must engage the exact structure of
  ζ (LEARNINGS #52, #56). (iii) The **Spec(ℤ) cohomology scorecard**
  ([`docs/03_research/spec_z_cohomology_landscape.md`](docs/03_research/spec_z_cohomology_landscape.md)):
  ~17 candidate cohomologies collapse onto one gap node: a polarization that is global AND
  trace-carrying AND RH-equivalent AND noncircular, the conjunction of four proven-droppable properties
  that no candidate has all of (LEARNINGS #73). Note: two *partial* polarizations are proven
  (Faltings-Hriljac, AHK); they miss the conjunction (too-local / arithmetic-blind), so the claim is
  "none has all four," not "none has a polarization."
- **Verification.** Synthesis of validated experiments + literature survey. The framing is the
  contribution; individual facts are mostly established.
- **Novelty (adversary HIGH-1, honest).** The bare convergence claim (RH = the missing polarization =
  the arithmetic Hodge standard conjecture / Rosati positivity) is **known folklore** the project's own
  spine calls "the arithmetic analogue of Grothendieck's Hodge standard conjecture" and
  `soft_detector_wall.md` demotes to "write-down-not-research." So P4 is held to the same standard P3
  was: the defensible novelty is the **operationalization** (the Spec(ℤ) scorecard as a figure + the
  D-H discipline as a method), not the convergence thesis.
- **K1 circularity.** The convergence thesis is RH-equivalent by construction (the missing polarization
  IS RH), so it must be framed as an organizing equivalence, never as "progress toward RH."
- **D-H soundness.** The thesis is built on the discipline (P3 is a sub-section).
- **RH-independence.** Surveys the open problem; self-contained as a survey.
- **Venue / next.** Expository (arXiv math.HO/NT survey or an expository journal). Outline + first prose
  pass written ([`publications/P4_survey_outline.md`](publications/P4_survey_outline.md),
  [`publications/P4_survey_draft.md`](publications/P4_survey_draft.md); §4 scorecard is a stub). It
  **bundles P3, P5, P7, P8** as evidence. **Survey lit-check (2026-06-16): provisionally distinctive on
  the OPERATIONALIZATION, not the convergence claim.** A deep read of Connes
  [2602.04022](https://arxiv.org/abs/2602.04022) found the scorecard + the convergence-as-organizing-
  principle + the D-H discipline absent there (he argues from NCG; the MDPI *Symmetry* 2025 survey is a
  flat catalog). But "provisionally" not "confirmed": this rests on one competitor read.
  **Prerequisites before any 'confirmed' / prose-finalization:** (1) read Deninger's program + at least
  one prismatic/THH survey (the obvious unchecked sources for the convergence framing); (2) an expert
  reader for the scorecard's polarization column.

### P5 {#p5}
**No higher-dimensional / SDP / SOS escape for the single-zero zero-free constant.** 🟡 DEVELOPING

> Reframed after the lit-check (2026-06-16). The original headline ("the LP/SDP/SOS family is capped
> at the Fejér ceiling") had its 1D half pre-empted; the defensible core is the negative closure of
> the *higher-dimensional escape routes*. Draft skeleton: [`publications/P5_zero_free_ceiling.md`](publications/P5_zero_free_ceiling.md).

- **Claim (defensible core).** The natural generalizations of the nonnegative-cosine-polynomial method
  do not improve the single-zero de la Vallée Poussin / Mossinghoff-Trudgian zero-free-region shape
  factor, all unified by an elementary line-restriction obstruction (4E.3, LEARNINGS #8, #9): any
  nonnegative multivariate trig polynomial restricted to a line through the origin is a 1D nonnegative
  trig polynomial, hence bounded by the 1D optimum at matched effective degree. The escape routes that
  fail: multivariate balanced-sum LPs (4E/4E.2/4E.4/4E.5, where a +25%/+51%/+62% Cauchy-Schwarz gap is
  real but does NOT transfer), constrained-domain LPs (4E.6), naive multi-zero couplings (4E.7),
  Heath-Brown multi-zero SDP (4E.9 / `e4e9_heath_brown_sdp`, best ratio ≤ 1, rank-2 certificate;
  verified ratio = 1.0000 in the `.npz`), Putinar/Schmüdgen SOS (4E.8 / `e4e8_sos_sdp`, LEARNINGS
  #15), and now the **Bombieri variational SOS** (4F / `e4f_variational_sos`, LEARNINGS #136), the one
  escape route *outside* the LP/SDP non-negative-cone family: relaxing non-negativity with an L²
  penalty `‖P₋‖²` on the negative part also fails to beat Fejér, and razor-sharply — `‖P₋‖² = 0` for
  every target `c₁/c₀ ≤ 2cos(π/8) = 1.8478` and positive precisely above it (2.7e-6 at 1.86 → 6.7e-4
  at 1.96). This is the strongest form of the closure: the wall survives the relaxation specifically
  designed to escape it, so the line-restriction obstruction is not an artifact of the cone
  relaxation. Cite escape routes by **experiment ID**, not LEARNINGS number: the adversary (HIGH-2) found
  4E.9 was mis-cited to "LEARNINGS #21", which under the doc's canonical numbering is the function-field
  Hodge index (`### 21.` / e2g). **Both repo-hygiene fixes are now DONE (2026-06-16):** the LEARNINGS.md
  Session-003 cluster carries a disambiguation banner (cite by experiment ID; the `**Finding #N**`
  labels are session-local and collide with the canonical `### N.` headers), and
  `experiments/zero_free/README.md` now documents 4E.8 and 4E.9 (no longer lists 4E.8 as "open"). P5 can
  now cite a consistent source.
- **Verification.** The line-restriction lemma is rigorous and elementary; the escape-route closures
  carry LP/SDP optimality certificates (cvxpy + CLARABEL/SCS). Self-contained.
- **Novelty (post-lit-check, honest).** The **1D part is NOT novel**: the cosine-polynomial method, the
  Fejér constraint `2cos(π/(n+2))`, and the optimization of the zero-free constant V = inf V_n are the
  established Mossinghoff-Trudgian program ([1410.3926](https://arxiv.org/abs/1410.3926)),
  Mossinghoff-Trudgian-Yang ([2212.06867](https://arxiv.org/abs/2212.06867)), and the 2024 "Optimal
  Cosine Polynomials" ([2411.01385](https://arxiv.org/abs/2411.01385), which computes V₇, V₈ exactly).
  4B reproduces this framework. The **candidate-novel residue** is the systematic *negative* closure of
  the higher-dimensional / multi-zero / SDP / SOS escape routes via the line-restriction lemma, which
  I did not find stated in the published record. Caveats baked into the framing: the lemma is
  folklore-adjacent; the multi-zero machinery genuinely helps *finite-range* problems
  (least-prime-in-AP, Siegel zeros, Heath-Brown/Pintz), so the no-go is specifically about the
  *asymptotic single-zero* constant; the V-K 2/3 ceiling (4A/4C, BDG 2016) is expository synthesis, not
  a new theorem.
- **D-H soundness.** The method is D-H-blind by construction (no Euler product enters the trig-poly
  inequality), and that blindness is part of why it cannot reach the discriminating structure.
- **RH-independence.** Fully independent (a theorem about an optimization family).
- **Venue / next.** A short arXiv math.NT note **or** folded into P4's Architecture-4 section (likely
  the better home, given the residue is narrow). **Next:** finish the [draft skeleton](publications/P5_zero_free_ceiling.md);
  decide standalone-note vs fold-into-survey once the line-restriction lemma is written out as the
  centerpiece and positioned against the prior work above.

### P6 {#p6}
**Lean formalization of function-field RH for elliptic curves (the deg = det route).** 🟡 DEVELOPING

- **Claim.** A sorry-free Lean chain from "Frobenius is a rank-2 integer matrix A with deg = det" to
  function-field RH for the curve: `negDef_iff_hasseWeil`; the symplectic determinant law on the
  abstract Tate module (`det_transform`, [`lean/ZetaRH/TateModule.lean`](lean/ZetaRH/TateModule.lean));
  the Hasse bound DERIVED from degree-positivity
  ([`lean/ZetaRH/IsogenyDegree.lean`](lean/ZetaRH/IsogenyDegree.lean)); the endpoint
  `functionfield_RH_elliptic_of_matrix` ([`lean/ZetaRH/FunctionFieldRH.lean`](lean/ZetaRH/FunctionFieldRH.lean)).
- **Verification.** Kernel-verified, axiom-clean, conditional on the single explicit hypothesis: the
  **existence of A** (the scheme-theoretic Frobenius-on-Tate-module construction, Mathlib-absent,
  FLT-adjacent). Everything downstream of A is machine-checked.
- **Novelty (lit-checked 2026-06-16, CONFIRMED viable).** Function-field RH for elliptic curves is
  classical math (Hasse 1936), but it is **absent from every proof assistant**, so the formalization is
  genuine: Mathlib has the Weierstrass group law (Angdinata-Xu, ITP 2023,
  [arXiv:2302.10640](https://arxiv.org/abs/2302.10640)) and basic elliptic-curve definitions, but the
  Hasse-Weil bound / Weil conjectures are an explicit *future goal*, not a completed result; the FLT
  project ([blueprint](https://imperialcollegelondon.github.io/FLT/blueprint/sect0001.html)) builds
  Tate modules / Weil pairings as infrastructure toward modularity but does **not** target
  function-field RH; and no Lean/Isabelle/Coq formalization of the Weil conjectures for curves exists.
  Note the rank-2 symplectic determinant law is **not** itself a Mathlib gap (Mathlib has the general
  `LinearMap.det` / `AlternatingMap` version; see [`lean/upstream/README.md`](lean/upstream/README.md)
  "Not staged"). Unlike P3/P5, this candidate survived its lit-check intact.
- **D-H soundness.** Arch 2; exempt by construction (it requires the Euler product D-H lacks).
- **RH-independence.** Self-contained as a conditional formalization; the open input is geometric, not RH.
- **Venue / next.** A formalization venue (ITP/CPP/JAR) as "a conditional Lean formalization of
  function-field RH, reduced to the existence of the Frobenius Tate-module representation `A`." Two
  honest paths, with a strategic fork:
  - **(a) Publish the conditional reduction now.** The chain downstream of `A` is sorry-free and
    axiom-clean (done). Modest but real: it formalizes the linear-algebra/eigenvalue half and isolates
    `A` (the scheme-theoretic Frobenius-on-Tate-module + deg≥0) as the one open input. Coordinate with
    FLT, which may supply that infrastructure.
  - **(b) Aim for the unconditional Hasse bound via the elementary route.** The Stepanov-Bombieri proof
    avoids the Tate module entirely and could yield an *unconditional* Lean Hasse bound (a stronger,
    cleaner artifact, and a natural Mathlib target) without waiting on `A`. A different formalization
    effort, not an extension of the current chain.

  **Next:** scoping + M-b1.3 probe DONE ([`publications/P6_hasse_bound_scope.md`](publications/P6_hasse_bound_scope.md),
  probed against the Mathlib v4.30 source). **Verdict: no cheap unconditional path.** Mathlib has the
  EC development (Affine/Projective/Jacobian/Weierstrass/DivisionPolynomial/LFunction/Reduction) but
  **no curve divisor theory at all**, so M-b1.3 ("#zeros = #poles") cannot be borrowed via divisors.
  Correction (adversary MED-3): the elementary resultant route (b1)(ii) is better-located than first
  stated. The **resultant API is already present** in v4.30 (`RingTheory/Polynomial/Resultant/Basic`:
  `resultant_eq_prod_roots_sub`, `resultant_eq_prod_eval`; `Algebra/Polynomial/Roots`: `card_roots`),
  so the degree-count primitive is borrowable; the real residual work is the **multiplicity bookkeeping
  at infinity and at branch points**, not the resultant API. **Both P6 paths are still multi-month**
  (path (a) needs the Tate module / deg-as-quadratic-form, FLT-adjacent; path (b1)(ii) needs the
  multiplicity bookkeeping), but the (b1)(ii) blocker is smaller and sharper than "build divisor
  theory." The only finished, citable artifact is the path-(a) **conditional reduction**.
  Decision: ship the conditional reduction now (modest, honest) and/or budget an unconditional build as
  a real multi-month project (route (b1)(ii), M-b1.3 first), Owen-gated.

### P7 {#p7}
**RH is Π⁰₁, and the Lean kernel witness.** 🟡 DEVELOPING

- **Claim.** RH is a Π⁰₁ sentence, so independence from ZFC would itself prove it true (undecidability
  is a back door to truth, not an escape, LEARNINGS #64). Formalized: the Π⁰₁ kernel witness `RH_arith`
  plus 8 sorry-free anchors ([`lean/ZetaRH/RHEquivalences.lean`](lean/ZetaRH/RHEquivalences.lean)),
  including Lagarias at n = 1, 2, 3 and the Σ⁰₁ refutability structure.
- **Verification.** Kernel-verified anchors. The logical-status fact itself is classical (via Lagarias
  / Robin-type criteria).
- **Novelty.** **Low as mathematics** (the Π⁰₁ classification is folklore). Modest as a formalization
  note. Most valuable bundled into P4 or as a short Lean note.
- **D-H soundness.** N/A.
- **RH-independence.** It is a statement *about* RH's logical form.
- **Venue / next.** Short note, or a subsection of P4. **Next:** bundle decision.

### P8 {#p8}
**The stealth window, quantified.** 🟡 DEVELOPING

- **Claim.** The Weil-form minimal eigenvalue collapses doubly-exponentially, ε(x) ~ exp(−4πx) in the
  prime cutoff x, via Slepian prolate concentration (LEARNINGS #52 / Arch 3V); positivity for ζ is a
  ~370× cancellation residue, not cushion-plus-perturbation, and A_arch is itself indefinite
  (LEARNINGS #56 / Arch 3Y); the exact duality-vs-polarization defect D(γ) = |1 − 2β| is D-H-AWARE
  (0 for ζ, a 0.617 spike at D-H's off-line height), and the stealth window is a *resolution cost*
  (primes to e^γ), not intrinsic blindness (LEARNINGS #63).
- **Verification.** Numerical + the prolate-concentration analysis (semi-rigorous). The collapse rate
  is archimedean (shared with D-H); the floor is the discriminator.
- **Novelty (lit-checked 2026-06-16, LOW-8 RESOLVED): the rate is doubly prior, not project-novel.**
  (i) The exponential collapse of prolate concentration eigenvalues, `1 − λ ~ e^{−πs}`, is **classical
  analysis** (Fuchs 1964, *On the eigenvalues of an integral equation arising in the theory of
  band-limited signals*; Slepian 1965; Widom), decades before any RH application. (ii) Connes
  2602.04022 applies the same **Slepian-Pollak-Landau** prolate operator to the truncated Weil form,
  and his **Figure 1** plots the smallest eigenvalue tracking `1 − χ₂ ~ e^{−4π e^L}` (his "near radical
  of the Weil form"); the project's `e3v` is an **independent re-measurement** of exactly this (the
  project's own dossier:
  [`connes_2602_letter_to_riemann.md`](docs/03_research/connes_2602_letter_to_riemann.md) §3, "two
  instruments, one wall"). So the `e^{−4πx}` rate must be cited to **Fuchs/Slepian + Connes' Figure 1**,
  never as project-novel. The scalar defect `D(γ) = |1 − 2β|` is itself trivial (the project's own
  #61/#63 demotion: `|1 − 2Re(ρ)| = 0` is a tautology). **P8's only project-specific residue** is the
  **quantitative anatomy of the marginal cancellation** (e3y/#56: the 55/69/123 → 0.33 three-block
  decomposition, A_arch indefinite, correcting the old "cushion" claim) plus the **D-H-awareness** of
  the reading (Connes never uses D-H, confirmed absent from 2602.04022). Those are computational
  exhibits, not theorems.
- **Verdict: NO standalone novelty. Fold into P4 Pillar 3.** Carry the citations: the rate to Fuchs
  1964 + Connes Figure 1; the stealth-window/near-radical equivalence to Connes' ε(λ); the project's
  exhibits (cancellation anatomy + D-H-awareness) as the one new framing.
- **Caveat:** the live re-fetch of 2602.04022 did not independently re-surface Figure 1 (arXiv-HTML
  figures/equations render poorly to the fetch tool); the citation rests on the project's careful
  internal dossier. A human should eyeball Connes' Figure 1 / §6.x to fix the exact figure/equation
  number before submission.
- **D-H soundness.** The whole point is the D-H-aware defect.
- **RH-independence.** Self-contained as an analytic benchmark.
- **Venue / next.** **Fold into P4 Pillar 3 (decided; the Connes lit-check is done).** No standalone
  note. **Next:** carry the Fuchs-1964 + Connes-Figure-1 citation into the P4 §5 prose (done), and have
  a human pin Connes' exact figure/equation number before submission.

---

### P9 — Paired-subtorus circle-rootedness theorem

- **Statement.** For $U \in U(2m)$ and conjugate-paired phases $D(\theta) = \mathrm{diag}(e^{i\theta_1}, e^{-i\theta_1}, \ldots, e^{i\theta_m}, e^{-i\theta_m})$, the expected characteristic polynomial $\mathbb{E}_\theta[\det(zI - D(\theta)U)]$ has all roots on $|z| = 1$. Equivalent finite form: the torus average equals the $2^m$ block-sign average. Corollaries: contraction version (Schur-stable roots), and the interpolation trivial-subgroup (char poly) / paired subtorus (nontrivial, circle-rooted) / full torus (trivial $z^n$).
- **Provenance.** Emerged from the #143 adversary round (the A2 correlated-phase vector), proven in full generality in the H3 probe (LEARNINGS #144; [`experiments/toy/paired_subtorus.md`](experiments/toy/paired_subtorus.md), proof + 12/12 numerical verification incl. 50-digit).
- **Novelty pass (2026-07-01, done; second-pass gate checks done same day).** Statement APPARENTLY NOVEL (not found in MSS/finite-free, Hall-Puder-Sawin, RMT torus reductions, OPUC, or minor-generating-polynomial literature; arXiv:2606.15003 read: coefficientwise q-convolution, real-rooted, CLEAN; Ruelle Grace-like read: CLEAN). Proof machinery CLASSICAL AND NAMED: Lemma E is the **Asano contraction** (Asano 1970 / Ruelle PRL 1971; unit-bidisk form verbatim in COSW 2004, Remark after Prop. 4.19), equivalently a special case of Hinkkanen's Schur-Hadamard theorem (statement confirmed verbatim via COSW p.35); the proof pattern (contraction + unimodular pinning) is the standard Lee-Yang pattern. The note credits all of this explicitly; the contribution is the assembled orbit-average statement.
- **D-H soundness.** Not applicable: a standalone geometry-of-polynomials theorem, no RH claim. Its project role (why averaging over the paired subtorus retains circle content = conjugate pairing, per the #143 gate) is context, not a claim of the note.
- **RH-independence.** Fully standalone.
- **Venue / next.** arXiv math.CV note (4-6 pp), cross-list math.CO/math.PR. **Gate before submission:** read arXiv:2606.15003 in full; sweep Ruelle's Grace-like / Lee-Yang graph-counting papers; a MathSciNet session (the pass was web-only). Then draft.

### P10 {#p10}

**The Gauss-lemma height floor (the vF disc model's empty Siegel slot).**

- **Statement.** Any nonzero $f \in \mathbb{Z}[z]$ vanishing at $1/p$ with multiplicity $\ge m_p$ for
  each prime $p \in P$ has $(pz-1)^{m_p} \mid f$ in $\mathbb{Z}[z]$, hence
  $\log|\mathrm{lead}(f)| \ge \sum_P m_p \log p$. With van Frankenhuijsen's multiplicities
  $m_p = \lfloor \log_p x \rfloor$ the floor is exactly Chebyshev $\psi(x)$
  ($\prod p^{m_p} = \mathrm{lcm}(1..x) = e^{\psi(x)}$, integer-exact), attained by
  $\prod_{p \le x}(pz-1)^{m_p}$; at the minimal degree the extremal vanisher is unique up to sign.
  No-go meaning: the S3 (Siegel-lemma) slot of vF's 2008 disc model is provably empty; the model's
  only open slot is the S4/R1 cheap-multiplicity operator.
- **Provenance.** The "smallest checkable sub-question" of the vF deep read (reading note Section 8),
  executed as e2ah (LEARNINGS #149; [`experiments/arithmetic_geometric/e2ah_gauss_floor.md`](experiments/arithmetic_geometric/e2ah_gauss_floor.md),
  [`lean/ZetaRH/GaussFloor.lean`](lean/ZetaRH/GaussFloor.lean), sorry-free, axiom-clean; Python probe
  integer-exact, all PASS incl. a complete no-cheaper-vanisher certificate at minimal degree).
- **Novelty pass (2026-07-02, done).** Assembled statement APPARENTLY NOVEL (not found in the vF paper
  itself: Section 4 re-read from the PDF this session, no lower bound / Gauss lemma / lcm appears; not
  found in the G-S / integer-Chebyshev / lcm literatures; no direct-statement hit). Mechanism FOLKLORE
  AND NAMED: the rational root theorem with multiplicity via Gauss descent (single-point case textbook
  and already in Mathlib as `den_dvd_of_is_root`); nearest published relatives are the same
  lcm-vs-polynomial trade in reverse (Gelfond-Schnirelman 1936; Nair, Amer. Math. Monthly 1982;
  Pritsker, Canad. J. Math. 2005) and the integer-Chebyshev critical-factor divisibility
  (Aparicio; Borwein-Erdelyi 1996; Pritsker 2005). MATH AXIS: parked as new mathematics (below the
  standalone bar; expository home = P4 counting-roads). FORMAL AXIS: viable; Mathlib has the identity
  side (`Chebyshev.lcmUpto`, `psi_eq_log_lcmUpto`, `factorization_lcmUpto`) but NOT the multiplicity
  or multi-point rational-root floor (pinned-copy grep; master unchecked). Full report:
  `scratchpad/counting_roads_followup/01_surveyor_gauss_floor_novelty.md` (untracked).
- **Verification.** #GF-1..#GF-5 kernel-verified ([propext, Classical.choice, Quot.sound]); Python
  integer-exact with an adversarial interpolation half. The uniqueness-at-minimal-degree gap is now
  CLOSED: #GF-6 machine-checked 2026-07-02 (`gauss_floor_rank_one` + `canonical_dvd_of_vanishing` +
  `canonical_natDegree` in [`GaussFloor.lean`](lean/ZetaRH/GaussFloor.lean)), so the full P10 statement
  (floor + equality + uniqueness) is kernel-verified.
- **D-H soundness.** Exempt (Arch 2 + pure formal/elementary; no zeta content at all).
- **RH-independence / K1.** Fully unconditional and RH-independent; no zeros of zeta appear; neither
  implies nor is implied by RH. A no-go coordinate about a model's proof-slot, not a reformulation.
- **Venue / next.** Mathlib PR for the generalized floor (extend `RingTheory/Polynomial/RationalRoot.lean`
  with `den^rootMultiplicity ∣ leadingCoeff` + the coprime-product version; optional `lcmUpto`
  corollary). **Progress (2026-07-02, both preconditions DONE):** (a) prior-art check against master +
  open PRs + Zulip: CLEAR-TO-PR (master has only the m = 1 case `den_dvd_of_is_root`/`num_dvd_of_is_root`;
  Loogle certifies no declaration joins `den` with `rootMultiplicity`; nearest PR #24172 closed unmerged,
  multiplicity-free; note: `scratchpad/counting_roads_followup/02_surveyor_mathlib_prior_art.md`, untracked);
  (b) the generalization is machine-checked in FULL Mathlib generality (UFD $A$, fraction field $K$, the
  exact typeclass context of `RationalRoot.lean`): #RR-1 `den_pow_rootMultiplicity_dvd_leadingCoeff` +
  #RR-2 `prod_den_pow_rootMultiplicity_dvd_leadingCoeff` + PR-worthy supporting lemmas (`isPrimitive_pow`,
  `isPrimitive_prod`, one-sided `dvd_of_fraction_map_dvd`) in
  [`lean/ZetaRH/RationalRootFloor.lean`](lean/ZetaRH/RationalRootFloor.lean), sorry-free, axiom-clean,
  build green. **Next:** open the mathlib4 PR (port to master, naming review expected) after P1/P2 review
  bandwidth clears; optional `lcmUpto` corollary.

---

## Parked / pre-empted

Kept so they are not re-proposed as novel.

- **de Bruijn-Newman / Pólya kernel positivity `Φ ≥ 0`** (LEARNINGS #38). Verified correct but
  **pre-empted**: Dobner 2020 (the class S# including D-H), Newman-Wu 2019, Michalowski 2026. It is
  orthogonal to RH (D-H passes it identically to ζ). A confirmed coordinate, not new mathematics.
- **Reformulation-trap detectors** (Rankin loglog c_F, LEARNINGS #53; Bost-Connes multiplicativity
  defect, #55; Li log-concavity, #27). Each detects **non-Euler-ness, not RH-failure** (the
  necessary-not-sufficient K2 firewall). Not standalone publishable; they belong in P3/P4 as the
  "here is what a soft detector actually measures" exhibit.

---

## How to add a candidate

1. Run the **Evaluation gate** (top of file). Be honest about verification and novelty.
2. If it survives, add a row to the **Registry** and a dossier with the six gate fields.
3. If it is pre-empted or a reformulation trap, add it to **Parked / pre-empted** with the reference.
4. Record the **one next action** in the dossier so the file is operational, not just an archive.

## Changelog

- 2026-06-16: file created. Seeded P1-P8 + the parked list from `LEARNINGS.md`, the
  `lean/upstream/` staging, and the research docs. Two items READY (P1, P2, Mathlib PR bodies in
  hand); the rest evaluated and awaiting drafting/lit-checks.
- 2026-06-16: **P5 lit-checked and reframed.** The 1D headline is pre-empted (Mossinghoff-Trudgian
  [1410.3926](https://arxiv.org/abs/1410.3926) / [2212.06867](https://arxiv.org/abs/2212.06867) /
  Optimal Cosine Polynomials [2411.01385](https://arxiv.org/abs/2411.01385)); P5 dropped 🔵 STRONG →
  🟡 DEVELOPING and reframed to the negative closure of the higher-dimensional / SDP / SOS escape
  routes (the 4E.3 line-restriction lemma). Draft skeleton written:
  [`publications/P5_zero_free_ceiling.md`](publications/P5_zero_free_ceiling.md); recommendation is to
  fold into P4's Architecture-4 section rather than submit standalone.
- 2026-06-16: **P3 lit-checked and reframed.** The thesis (D-H as the wrong-approach discipline) is the
  canonical Selberg-class folklore (Bombieri Clay, Conrey Notices AMS 2003, Selberg 1992 /
  Conrey-Ghosh 1993); P3 dropped 🔵 STRONG → 🟡 DEVELOPING, residue narrowed to the quantitative
  instrument (Schur counting law + Epstein generalization + CI gate), recommended home P4. Added the
  **Portfolio read** section: standalone-publishable = {P1, P2, P6}; everything else folds into the
  survey P4.
- 2026-06-16: **P4 outline written** ([`publications/P4_survey_outline.md`](publications/P4_survey_outline.md)).
  Scope decided (bundles P3, P5, P7, P8 as evidence in three pillars: all-roads realization /
  Spec(ℤ) scorecard / marginal positivity). Distinctive thesis vs existing surveys = the convergence
  claim operationalized by the scorecard. Sequenced after P1/P2 ship + a full survey lit-check + an
  expert reader.
- 2026-06-16: **P6 lit-checked, CONFIRMED viable.** The Hasse-Weil bound / Weil conjectures for curves
  are absent from every proof assistant (Mathlib has only the Weierstrass group law + basic defs, the
  bound is an explicit future goal; the FLT project does not target it). P6 stays 🟡 DEVELOPING but is
  the one research/formalization candidate that survived its lit-check intact. Strategic fork recorded:
  (a) publish the conditional reduction now, vs (b) aim for the unconditional Hasse bound via the
  elementary Stepanov-Bombieri route (recommended; Mathlib-bound, no FLT dependency).
- 2026-06-16: **P6 path (b) scoped** ([`publications/P6_hasse_bound_scope.md`](publications/P6_hasse_bound_scope.md))
  and **P4 survey lit-checked (provisional, survives).** P6 scoping: general Stepanov-Bombieri hits the
  Riemann-Roch wall, but the elliptic-curve specialization dodges it (explicit Weierstrass $R_n$);
  recommend gating (b1) on a one-week M-b1.3 feasibility probe (#zeros = #poles without scheme
  cohomology). P4 lit-check: thesis not pre-empted by Connes 2602.04022 or the MDPI Symmetry 2025
  brief survey; full reads + expert reader still required before prose.
- 2026-06-16: **P6 M-b1.3 probe resolved against the Mathlib v4.30 source.** Mathlib has **no curve
  divisor theory** (no Weil/Cartier divisor, degree, Picard, or Riemann-Roch; the EC dev avoids
  divisors), so M-b1.3 needs either curve divisor theory (blocked) or an elementary resultant build
  (weeks). **Both P6 paths are multi-month**; the only finished artifact is the path-(a) conditional
  reduction. Recommendation: ship the conditional reduction now and/or budget an unconditional build
  (route (b1)(ii)) as a real project. The probe did its job: killed the cheap-win hope, located the
  exact blocker.
- 2026-06-16: **P4 thesis CONFIRMED distinctive** via a deep read of the main competitor (Connes
  2602.04022): no convergence thesis there, no Spec(ℤ) scorecard, Weil positivity is one reformulation
  among many, D-H not used as a discipline. P4's convergence-plus-scorecard-plus-D-H framing is novel
  against the field's best recent survey. The only remaining prerequisite before prose is an expert
  reader for the scorecard's polarization column. Positioning recorded in the P4 outline.
- 2026-06-16: **P4 first prose pass written** ([`publications/P4_survey_draft.md`](publications/P4_survey_draft.md)):
  the gate-free sections (§1 intro, §2 four-level framing, §3 realizations, §5 marginal positivity, §6
  logical status, conclusion) are drafted; §4 (the Spec(ℤ) scorecard) is a stub pending the expert
  reader. Numbers in §5 flagged for re-verification against the experiments before submission.
- 2026-06-16: **usage guide written** ([`publications/README.md`](publications/README.md)).
- 2026-06-16: **ADVERSARY review run and folded in** ([`publications/ADVERSARY_REVIEW.md`](publications/ADVERSARY_REVIEW.md);
  no FAIL verdicts, the bones are sound). Fixes applied: **HIGH-1** P4 "CONFIRMED distinctive" downgraded
  to "provisionally distinctive on the operationalization" (the convergence claim is project-admitted
  folklore; novelty = scorecard + D-H method; read Deninger + a prismatic/THH survey before "confirmed").
  **HIGH-2** P5 cite-by-experiment-ID (4E.9 was mis-cited to LEARNINGS #21, a numbering collision; stale
  `zero_free/README.md` flagged). **MED-3** P6: the resultant API *is* present in v4.30, so the (b1)(ii)
  blocker is multiplicity bookkeeping, not the resultant. **MED-4** P4 §3 "none reaches the polarization"
  to be qualified by the four properties (FH/AHK are proven partial polarizations). **MED-5** added the
  K1 circularity question (4b) to the gate. **MED-6** P6 Portfolio one-liner marked "conditional."
  **LOW-7** P4 count inconsistencies. **LOW-8** P8's exp(−4πx) rate is Connes', not project-novel.
  What PASSED the attack: the §5 marginal-positivity numbers, the P1/P2 Mathlib novelty, the P6 core
  absence claim, the live D-H control (smoke test 9/9).
- 2026-06-16: **P8 rate-vs-Connes lit-check DONE (adversary LOW-8 resolved).** The `e^{−4πx}` collapse
  rate is doubly prior: classical prolate asymptotics (Fuchs 1964, Slepian 1965, Widom, `1−λ~e^{−πs}`)
  + Connes' Figure 1 (`1−χ₂~e^{−4π e^L}`, his "near radical"; the prolate operator is
  Slepian-Pollak-Landau). The scalar defect `D(γ)=|1−2β|` is trivial (project's own #61/#63 demotion).
  P8's only residue = the cancellation anatomy (e3y) + D-H-awareness (Connes uses no D-H). Verdict: **no
  standalone novelty; fold into P4 Pillar 3** with the rate cited to Fuchs + Connes. Citations carried
  into the P4 §5 draft. (A human should pin Connes' exact figure number; the arXiv-HTML fetch could not
  re-surface it.)
- 2026-06-16: **adversary HIGH-2 repo-hygiene fixes landed.** Disambiguated the LEARNINGS.md #21
  numbering collision (a banner on the Session-003 cluster: the `**Finding #N**` labels are
  session-local and collide with the canonical `### N.` headers; cite by experiment ID). Refreshed
  `experiments/zero_free/README.md`: added the 4E.8 (SOS) and 4E.9 (Heath-Brown multi-zero SDP) sections
  and corrected the stale "4E.8 is the remaining open direction" to "the LP/SDP/SOS family is fully
  closed." P5's cited source is now consistent.
- 2026-06-30: **three session findings folded in.** (i) **P5 strengthened** with the Bombieri
  variational SOS (4F / `e4f_variational_sos`, LEARNINGS #136): the one escape route *outside* the
  LP/SDP cone family (L²-penalized negativity) also fails to beat Fejér, razor-sharply at the cone
  boundary, so the negative closure now covers the variational relaxation built to escape it. Registry
  row and dossier updated. (ii) **P4 / the obstruction-map survey strengthened** with the most concrete
  face of the marginal-positivity discipline (LEARNINGS #135, `e2w2_loglog_arch_coupling`): ζ's
  non-circular Rosati positivity is a +0.035 margin from two norm-44 blocks, and the one named probe to
  inject multiplicativity into the signature (c_F on A_arch) destroys it for every control including
  RH-true ζ — there is no margin to inject into. Added to the survey's marginal-positivity section. (iii)
  **The D4 meta-level gradient-descent thread** (LEARNINGS #134, `experiments/gradient_descent/`) was
  evaluated and deliberately NOT given a registry row: its publishable content (the kernel cliff =
  marginal positivity restated) is already P4, and the rest is tooling (a verifier-grounded RL rehearsal
  on the closed function-field case). Honest call per gate item 4b (it would be a reformulation/tooling
  note, not new content). It stays a repo artifact, citable from P4 as a methodology demonstration.
- 2026-07-02: **P10 registered (the Gauss-lemma height floor, LEARNINGS #149).** Gate run on a fresh
  SURVEYOR novelty pass: the assembled statement is apparently novel (vF 2008 Section 4 re-read from
  the PDF: the setting and the psi(x) value are there, no lower bound anywhere; no direct-statement hit
  in the Gelfond-Schnirelman / Nair / Pritsker / integer-Chebyshev literatures, which run the same
  lcm-vs-polynomial trade in reverse), while the mechanism is folklore (the rational root theorem with
  multiplicity; the m = 1 case is already Mathlib's `den_dvd_of_is_root`). Split verdict: math axis
  parked-as-new-math (expository home = P4 counting-roads), formal axis carries the row (Mathlib has
  `Chebyshev.lcmUpto` + `psi_eq_log_lcmUpto` but no multiplicity or multi-point rational-root floor).
  Tier 🟡 DEVELOPING; next = generalize #GF-2/#GF-5 to the `RationalRoot.lean` idiom + a Mathlib
  master/open-PR/Zulip check; optional #GF-6 (the uniqueness clause, currently Python-only) first.
