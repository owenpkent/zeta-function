# PUBLICATIONS — publishable-discovery registry and evaluation

> Tracks every candidate publishable discovery across formal (Mathlib) and expository/research
> (arXiv) output, with an evaluation gate that decides tier and venue. Living document.
> Maintained alongside [`PHASE_STATE.md`](PHASE_STATE.md) and [`experiments/LEARNINGS.md`](experiments/LEARNINGS.md).

This file answers two questions: **what is publishable right now**, and **how do we decide** whether
a new finding clears the bar. `LEARNINGS.md` is the firehose of every finding; this file is the much
smaller subset that could leave the repo as a contribution, scored honestly.

A discovery and a paper are not the same thing. Each row below is a *discovery* (a `P#` id); a paper
may bundle several. The "Venue / bundle" field records the intended container.

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
- **Standalone-publishable as a formalization artifact:** P6 (the Lean function-field RH chain; novelty
  is the development, not the classical math). **Lit-check confirmed viable (2026-06-16):** the
  Hasse-Weil bound is absent from every proof assistant and is an explicit Mathlib future goal, so this
  is genuine territory. The one candidate that survived its lit-check intact.
- **One survey that absorbs the rest:** P4, bundling P3, P5, P7, P8 as operationalized coordinates.

Lit-check every research candidate before drafting it. The scorecard so far: P3 and P5 moved STRONG →
DEVELOPING (pre-empted theses); P6 confirmed viable. The pattern: the *positivity/analytic*
"discoveries" are operationalized folklore (fold into P4); the *formal* contributions (P1, P2, P6) are
the real standalone output.

---

## Registry

| ID | Discovery | Type | Verification | Tier | Venue / bundle | Status |
|----|-----------|------|--------------|------|----------------|--------|
| [P1](#p1) | `riemannZeta_conj`: conjugation symmetry of ζ | Formal (positive) | Lean, axiom-clean | 🟢 READY | Mathlib PR | ready |
| [P2](#p2) | Digamma reflection / iterated recurrence / duplication | Formal (positive) | Lean, axiom-clean | 🟢 READY | Mathlib PR | ready |
| [P3](#p3) | The Davenport-Heilbronn discipline, operationalized (Schur counting law + Epstein) | Methodology | Numerical (validated) + rigorous Li at n=336k | 🟡 DEVELOPING | Fold into P4 | lit-checked |
| [P4](#p4) | All-roads convergence + marginal-positivity thesis + Spec(ℤ) scorecard | Survey | Synthesis | 🟡 DEVELOPING | Expository / arXiv | evaluated |
| [P5](#p5) | No higher-dimensional / SDP / SOS escape for the single-zero zero-free constant | Negative (closed branch) | Rigorous (line-restriction lemma) + SDP/LP certificates | 🟡 DEVELOPING | arXiv math.NT note / fold into P4 | lit-checked |
| [P6](#p6) | Lean formalization of function-field RH for elliptic curves (deg = det route) | Formalization (positive) | Lean, axiom-clean (conditional on existence of A) | 🟡 DEVELOPING | Formalization venue | lit-checked ✓ viable |
| [P7](#p7) | RH is Π⁰₁ + the Lean kernel witness | Expository note | Lean anchors; logical fact classical | 🟡 DEVELOPING | Note / bundle into P4 | evaluated |
| [P8](#p8) | The stealth window quantified (e^{-4πx} wall, 370× cancellation, D-H-aware defect) | Analytic note | Numerical + prolate analysis | 🟡 DEVELOPING | Section of P4 | evaluated |

---

## Candidate dossiers

Each dossier carries the six gate fields. `LEARNINGS #n` cross-references
[`experiments/LEARNINGS.md`](experiments/LEARNINGS.md).

### P1 {#p1}
**`riemannZeta_conj`: conjugation symmetry of the Riemann zeta function.** 🟢 READY

- **Claim.** `ζ(conj s) = conj (ζ s)` for `s ≠ 1`, and the corollary that the zeros are
  conjugation-symmetric. The natural companion to Mathlib's `riemannZeta_one_sub`; together they
  generate the quadruple symmetry `{ρ, 1−ρ, conj ρ, 1−conj ρ}`.
- **Verification.** [`lean/ZetaRH/RiemannZetaConj.lean`](lean/ZetaRH/RiemannZetaConj.lean), sorry-free,
  `#print axioms` = `[propext, Classical.choice, Quot.sound]` against Lean/Mathlib v4.30.0,
  imports only Mathlib.
- **Novelty.** Absent from current Mathlib (lit-checked against the RiemannZeta API).
- **D-H soundness.** N/A (a true theorem about ζ, not an RH-method).
- **RH-independence.** Fully independent of the open content.
- **Venue / next.** Mathlib PR; body ready at [`lean/upstream/riemann_zeta_conj_pr_body.md`](lean/upstream/riemann_zeta_conj_pr_body.md).
  **Next:** the human GitHub/CLA/fork/rebase steps (Owen); submit after P2 per the upstream README order.

### P2 {#p2}
**Digamma reflection, iterated recurrence, duplication.** 🟢 READY

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
- **Venue / next.** Mathlib PR; body at [`lean/upstream/digamma_pr_body.md`](lean/upstream/digamma_pr_body.md).
  **Next:** submit FIRST (staged longest, only open question now resolved). Human GitHub steps.

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
  17 candidate cohomologies collapse onto one gap node, an RH-equivalent polarization that none
  supplies (LEARNINGS #73).
- **Verification.** Synthesis of validated experiments + literature survey. The framing is the
  contribution; individual facts are mostly established.
- **Novelty.** The synthesis and the "all roads → one signature" framing are the novel part. This is
  expository/landscape work, valuable precisely as a map.
- **D-H soundness.** The thesis is built on the discipline (P3 is a sub-section).
- **RH-independence.** Surveys the open problem; self-contained as a survey.
- **Venue / next.** Expository (arXiv math.HO/NT survey or an expository journal). Outline written:
  [`publications/P4_survey_outline.md`](publications/P4_survey_outline.md). Scope decided: it **bundles
  P3, P5, P7, P8** as evidence inside the three pillars. **Survey lit-check (2026-06-16, deep read of the
  main competitor): thesis CONFIRMED distinctive.** A deep read of Connes [2602.04022](https://arxiv.org/abs/2602.04022)
  (the strongest competitor) found all three distinctive moves absent there: no convergence thesis (he
  argues from NCG), no Spec(ℤ) scorecard, Weil positivity treated as one reformulation among many, D-H
  not used as a discipline. The MDPI *Symmetry* 2025 survey is a flat catalog. **Remaining prerequisite:**
  an expert reader for the scorecard's (iii) polarization column. Then prose. Still the long pole, but
  de-risked: the thesis is novel against the field's best recent survey.

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
  Heath-Brown multi-zero SDP (4E.9, best ratio ≤ 1, rank-2 certificate, LEARNINGS #21), and
  Putinar/Schmüdgen SOS (4E.8, LEARNINGS #15).
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
  **no curve divisor theory at all**, so M-b1.3 ("#zeros = #poles") cannot be borrowed; it needs either
  general curve divisor theory (blocked) or an elementary resultant build (weeks). **Both P6 paths are
  multi-month** (path (a) needs the Tate module / deg-as-quadratic-form, FLT-adjacent; path (b1) needs
  the resultant build). The only finished, citable artifact is the path-(a) **conditional reduction**.
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
- **Novelty.** Overlaps Connes' constructive Weil positivity (the project's stealth window =
  Connes' ε(λ) near-radical; see the assessment of arXiv:2602.04022 in
  [`docs/03_research/connes_2602_letter_to_riemann.md`](docs/03_research/connes_2602_letter_to_riemann.md)).
  **Open action: lit check vs. Connes** to find the genuinely-new delta (the explicit exp(−4πx) rate +
  the D-H-aware defect are candidates).
- **D-H soundness.** The whole point is the D-H-aware defect.
- **RH-independence.** Self-contained as an analytic benchmark.
- **Venue / next.** A section of P4, or a standalone analytic note if the delta vs. Connes survives.
  **Next:** the Connes lit check.

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
