# A Proof Program for the Riemann Hypothesis

> Operational follow-on to [`PROOF_ARCHITECTURES_PLAN.md`](../../experiments/PROOF_ARCHITECTURES_PLAN.md) (which tests the four architectures) and [`2A_path_forward.md`](../../experiments/arithmetic_geometric/2A_path_forward.md) (which sketches the strategic plan). This document is the operational program: what would actually be done, in what order, with what falsifiability criteria, by whom, on what timeline, with what abandonment conditions.
>
> **Premise**: the four-architecture analysis identifies Architecture 2's geometric route (intersection theory + Hodge index theorem on a constructed arithmetic surface) as the unique direction capable of escaping the K1 wall (per R3.5 no-shortcut theorem). Architectures 1, 3, 4 are structurally capped at the project level. So a proof program must execute Architecture 2.
>
> **Execution modality: AI-augmented research.** The phases below are scoped around what AI assistants (Claude Code with `mpmath` / `numpy` / `cvxpy` / `sympy`, plus current and future generations of mathematical-reasoning AI) can do versus what requires expert human researchers. The project's experimental thread (this repo) demonstrates AI's capabilities on the mapping side: scorecards, R-series structural analyses, high-precision computational witnesses, cross-literature synthesis. The construction-grade work (Hodge index theorem, foliated dynamical system, the Lambda-blueprint surface) remains human-led, with AI in a sub-tool role. See [§ AI division of labor across phases](#ai-division-of-labor-across-phases) for the per-phase breakdown. The timelines below assume AI-augmented execution; they would be substantially longer for pre-AI research methodology.
>
> **Honesty up front**: this is a multi-decade research program with success probability under 1%. It cannot be executed by one person in one year. Most milestones are independently publishable as partial results even if the final goal is not reached. The plan is structured so that each phase produces a deliverable that is valuable on its own.
>
> **See also**: [`proof_program_ai_only.md`](proof_program_ai_only.md) is the speculative sibling document describing what an AI-only execution variant would look like (no human in the critical path). The AI-only variant has LOWER success probability (~0.2-0.5% vs ~0.8% for AI-augmented) under current AI capabilities, because Phase 4's Hodge index theorem requires mathematical creativity that AI does not yet demonstrate at this depth. The AI-only variant becomes a viable target design if AI mathematical creativity improves substantially over the next 5-10 years.

---

## 0. Strategic premise

The project's experimental thread (six commits of recent work plus prior sessions) established three findings that pin down the strategy:

1. **Only Architecture 2 can in principle close RH.** R3.5's no-shortcut theorem rules out all NCG-only approaches. Architectures 3 and 4 hit walls (analytic circularity, V-K 2/3 stagnation, LP/SDP family saturation) consistent with the marginal-positivity thesis.

2. **The unique escape route is intersection-theoretic positivity.** A Hodge index theorem on a constructed arithmetic surface gives positivity from the SIGNATURE of an intersection form. Structurally different from trace-formula positivity. Not subject to R3.5.

3. **The construction is research-grade.** Six existing F_1 candidates (Deitmar, Lorscheid, Borger, Connes, Connes-Consani, Deninger) and Arakelov-Soule together provide most ingredients but not the Hodge index slot. No candidate has even a partial yes on constraints (xi)-(xiii).

The proof program executes the construction.

## 1. Goal hierarchy

In order of decreasing tractability, increasing significance:

| Tier | Goal | Estimated effort | Probability if pursued seriously |
|---|---|---|---|
| G1 | Develop R2.5 Lambda-blueprints rigorously (categorical definitions, fiber products, scorecard verification) | 1-2 years | 70-80% |
| G2 | Apply prismatic cohomology to the Lambda-blueprint analog of Spec(W(Z)); verify R5 questions Q1-Q5 | 2-3 years | 50-60% |
| G3 | Verify 2D-M3 prismatic foliation hypothesis (Lefschetz trace formula, Poincare duality, Kunneth on the foliated prismatic site) | 2-4 years | 40-50% |
| G4 | Define an arithmetic intersection theory on the constructed surface (cycle classes, intersection product, basic properties) | 4-6 years | 20-35% |
| G5 | Prove a Hodge index theorem giving positivity for the relevant intersection form | 7-12 years | 5-15% |
| G6 | Assemble the Weil-template proof: Lefschetz + Poincare duality + Hodge index on the constructed surface | 10-15 years | 3-10% |
| G7 | Verify D-H discipline, Weil specialization, and K1 escape; publish | 12-20 years | 2-8% |

G1-G3 are publishable independently. G4 is a major contribution even without G5. G5 is the central open problem. G6-G7 are the proof.

## 1.5. AI division of labor across phases

The phases below run on different mixes of AI and human work. AI accelerates the surveyable, mechanical, and structurally-mappable parts; human researchers remain primary for the construction-grade and novel-creativity parts. This table is the per-phase scoping:

| Phase | AI primary | Human primary | Both required | AI acceleration vs traditional research |
|---|:---:|:---:|:---:|---|
| 0 Foundation | ✓ | | | ~5x (literature synthesis, scorecard work in weeks not months) |
| 1 Lambda-blueprints | | | ✓ | ~2-3x (AI handles fiber-product calculations + categorical checks; human handles definitions) |
| 2 Prismatic cohomology | | | ✓ | ~2x (AI assists with Q1-Q5 verification; human constructs cohomology) |
| 3 Intersection theory | | ✓ | | ~1.5x (mostly construction work; AI as bookkeeping aid) |
| 4 Hodge index | | ✓ | | ~1.2x (deeply creative work; AI assists with computation and verification) |
| 5 Assembly | | | ✓ | ~2x (verification-heavy, where AI shines; integration is human-judgment) |
| 6 Peer review | | ✓ | | ~1x (community process; AI does not accelerate) |

**What AI does in each phase**:

- **Phase 0**: substantially AI-led. Literature deep-dive across F_1, Arakelov, prismatic, NCG. Independent scorecard verification. Structural pinning-down of R3.5 (already done in the project). Identification of expert correspondents (human-led). The 12-month estimate is realistic for an AI-augmented Phase 0; without AI, this is more like 2-3 years.

- **Phase 1**: collaborative. AI articulates the categorical structure of Lambda-Blpr, verifies the basic axioms (composition, identity, full faithfulness of embeddings), and computes the fiber product Spec(Z) x_F1 Spec(Z) once human-defined Fermat-Frobenius is in place. AI maintains the 17-constraint scorecard consistently. Human researcher defines Fermat-Frobenius, judges categorical taste, decides which structural choices to make.

- **Phase 2**: collaborative, with AI heavier on the verification side. AI applies prismatic cohomology machinery to Spec(W(Z)) and verifies the R5 Q1-Q5 properties as theorems. The actual construction of the prismatic site and the foliation requires human researchers with deep p-adic Hodge theory expertise. AI provides infrastructure (e.g., 2D-M3 explicit specification, error checking).

- **Phase 3**: human-led construction work. Defining a Chow-style intersection product on the Lambda-blueprint surface requires creativity AI does not have. AI assists with: bookkeeping (tracking which constraints are satisfied), verifying basic properties (bilinearity, projection formula) once constructions are proposed, and comparing to function-field analogs.

- **Phase 4**: the central open problem. This is where AI is least helpful: the Hodge index theorem requires genuinely novel mathematical creativity. AI's role: (a) cross-survey of related Hodge index theorems (Adiprasito-Huh-Katz tropical, Faltings arithmetic, classical algebraic-geometric); (b) computational verification of candidate proofs once proposed; (c) maintaining the K1 / K2 / K3 verification framework. The actual creative leap is human.

- **Phase 5**: collaborative. Assembling the Weil-template proof from Phases 1-4 is integration work. AI verifies each step against K1-K4 and writes the cross-referenced exposition. Human researchers make integration choices and judge the overall structure.

- **Phase 6**: peer review is a human community process. AI may be used by reviewers to verify computational claims and check structural arguments, but the judgment process is community-driven.

**What this means for the program structure**:

- Phase 0 and 1 are AI-tractable enough that a small group (1 human + AI sessions) can produce them in 1-2 calendar years. This is dramatically faster than pre-AI norms.
- Phases 2-3 require a small research group (2-3 humans + AI) and 2-3 years each.
- Phase 4 is the central open problem; AI offers limited acceleration. 5-10 calendar years of human-led work is realistic.
- Phase 5-6 are collaborative integration and community process. 5-7 calendar years cumulatively.

Total calendar time under AI-augmented execution: 12-18 years. Traditional research methodology would be 20-30 years for the same program.

**What AI cannot accelerate**: the Hodge index theorem itself. The marginal-positivity thesis says RH is barely true; the proof must use exact zeta structure. No amount of computation or literature synthesis substitutes for the creative leap of constructing the right surface, the right cohomology, and the right positivity argument together. This is what makes the program hard, and it is the part AI cannot do alone.

## 2. Phase structure

### Phase 0: Foundation (months 1-12)

**Goal**: get the prerequisite frameworks rigorously in place.

**Tasks**:
- 0.1 Read the relevant primary literature in depth: Borger 2009+, Lorscheid 2010+, BMS 2018+, Connes-Consani 2008+, Deninger 1991+, Bost-Connes 1995. Estimated 3-6 months for a strong PhD-level mathematician.
- 0.2 Identify expert collaborators or correspondents: at least one in each of (a) noncommutative geometry / Connes program, (b) arithmetic geometry / F_1 / blueprints, (c) prismatic cohomology / p-adic Hodge theory.
- 0.3 Reproduce the 2A scorecards independently: verify the constraint analysis for the six candidates. Disagreements with the existing scorecards refine the framework.
- 0.4 Identify the precise version of R3.5 that applies and pin down what "intersection-theoretic positivity" means formally. Settle whether tropical Hodge index theorems (Adiprasito-Huh-Katz 2018) provide a usable template.

**Milestone**: a 20-30 page survey of the landscape with the candidate frameworks scorecards verified, expert correspondents identified, and the precise statement of R3.5 in the framework's language. Independently publishable as an expository article.

**Falsifiability**: if Phase 0 reveals that R3.5 is too narrow (some NCG approach can escape K1) OR that the 17-constraint scorecard is structurally wrong (some candidate IS at a yes on (xi)-(xiii)), the entire strategy needs rethink.

### Phase 1: Lambda-blueprints (year 1-2)

**Goal**: G1. Make R2.5 ([`2A_R2_5_lambda_blueprints.md`](../../experiments/arithmetic_geometric/2A_R2_5_lambda_blueprints.md)) rigorous.

**Tasks**:
- 1.1 Define a Lambda-blueprint as a triple (B, B-bullet, {psi_p}) precisely. Verify the Fermat-Frobenius compatibility psi_p(x) ≡ x^p mod blueprint relations.
- 1.2 Show that the category Lambda-Blpr has F_1 as initial object, Z as canonical next level (with psi_p = id), and contains both Lambda-Rings and Blpr as full subcategories.
- 1.3 Compute the fiber product Spec(Z) x_F1 Spec(Z) in Lambda-Blpr. Compare to Borger's W(Z) and Lorscheid's blueprint surface.
- 1.4 Verify the 17-constraint scorecard for Lambda-Blpr. Predicted: 8 yes / 4 partial / 5 open. Confirm or revise.
- 1.5 Verify D-H exclusion (K2) for Lambda-Blpr.

**Milestone**: a 30-50 page paper "Lambda-blueprints and the F_1 geometry of Spec(Z)", publishable in Compositio or JAMS.

**Falsifiability**: if Lambda-Blpr does not admit fiber products, or if the predicted scorecard is wrong by more than 2 constraints, the framework is not the right hybrid and the program needs a different surface candidate (likely back to Lorscheid pure-blueprint or Borger pure-Lambda).

### Phase 2: Prismatic cohomology on the constructed surface (years 2-4)

**Goal**: G2 + G3. Apply BMS prismatic cohomology to the Lambda-blueprint surface and verify the prismatic foliation hypothesis.

**Tasks**:
- 2.1 Show that prismatic cohomology of Spec(W(Z)) (Borger) extends to the Lambda-blueprint analog. Verify R5 questions Q1-Q5.
- 2.2 Define the foliation F on the prismatic site of the Lambda-blueprint surface. Use the R4 multiplicative-completion bridge Phi_t = prod_p U_{log p}^{t/log p}.
- 2.3 Verify the prismatic foliation hypothesis (2D-M3): finiteness of H^*_{F,pr}, Poincare duality, Kunneth, Lefschetz trace formula recovering at least the Euler-product piece of zeta(s).
- 2.4 Compute the cohomology explicitly in low-degree cases. Verify against known function-field cases (zeta_C for C/F_q).

**Milestone**: a 40-60 page paper "Prismatic foliations and the zeta function of Spec(Z)", publishable in Inventiones or Ann. of Math. This closes (iv)-(vii) and partially (viii)-(ix) of the 17 constraints.

**Falsifiability**: if R5 questions don't have positive answers (e.g., prismatic cohomology of W(Z) is not finite-dimensional in the relevant sense), or if the foliation does not give a Lefschetz trace formula recovering zeta's Euler product, the framework is missing a key compatibility. The fix may be to use a different cohomology (Hochschild, motivic) or a different Frobenius substitute.

### Phase 3: Arithmetic intersection theory (years 3-7)

**Goal**: G4. Define and develop intersection theory on the constructed surface.

**Tasks**:
- 3.1 Define cycle classes on the Lambda-blueprint surface (analog of Chow groups). Use either (a) algebraic cycles modulo rational equivalence, or (b) prismatic-cohomology-derived cycle classes, or (c) a hybrid.
- 3.2 Define the intersection product. Verify basic properties: bilinearity, projection formula, compatibility with Frobenius (psi_p).
- 3.3 Compute intersection numbers in low-degree cases. Verify against function-field Chow theory for C x C.
- 3.4 (If R3.6.3 machinery becomes available) Test whether hyperring-valued cycle classes on the Connes-Consani arithmetic site provide an alternative intersection theory. This is R3.6.3.b operationalized.

**Milestone**: a 50-80 page paper "Arithmetic intersection theory on Spec(Z) x_F1 Spec(Z)", publishable in Ann. of Math. This is a MAJOR contribution even if the rest of the program does not succeed.

**Falsifiability**: if the intersection product is not bilinear, or does not satisfy the projection formula, or does not specialize correctly to Chow theory in the function-field limit, the framework's intersection theory is wrong. Three years of attempted construction without a working candidate is signal to fundamentally rethink (possibly abandon).

### Phase 4: The Hodge index attempt (years 4-10)

**Goal**: G5. The central open problem.

This is where the program might succeed or fail. Three a priori distinct attack angles:

**4.A Tropical-arithmetic Hodge bridge** (R3.6.3.c). Adapt the Adiprasito-Huh-Katz tropical Hodge index theorem to the characteristic-one limit of the Connes-Consani arithmetic site. Verify whether the tropical Hodge index, suitably reinterpreted, gives Hodge index on the Lambda-blueprint surface.

**4.B Connes-Consani topos-theoretic Hodge** (R3.6.3.a). Develop a sheaf-theoretic Hodge index in the hyperring-sheaf topos. This is highly speculative; no published work points in this direction directly.

**4.C Direct algebraic-geometric construction**. Forget the F_1 / hyperring machinery and ask: on the Lambda-blueprint surface, equipped with prismatic cohomology, is there a direct algebraic-geometric argument for Hodge index? This is the most conservative approach and most likely to succeed if the surface is "geometric enough".

Each of 4.A, 4.B, 4.C is a multi-year sub-program. They are not mutually exclusive; ideally all three are pursued in parallel by different groups.

**Milestones (per sub-program)**:
- 4.A: a paper "Tropical Hodge index in characteristic-one arithmetic", 60-100 pages.
- 4.B: a paper "Sheaf-theoretic positivity on the arithmetic site", 60-100 pages.
- 4.C: a paper "Algebraic-geometric Hodge index for the Lambda-blueprint surface of Spec(Z)", 80-120 pages. The most direct path to RH if it works.

**Falsifiability**: 5 years of attempted Hodge index without progress is signal that the structure isn't there. Two options at that point: (i) abandon Architecture 2's geometric route and accept that RH may require fundamentally new mathematics outside the four-architecture framework; (ii) try Bombieri variational SOS as a non-LP/SDP escape from the marginal-positivity thesis.

### Phase 5: Assembly and verification (years 8-15)

**Goal**: G6. Combine the pieces into a proof.

**Tasks**:
- 5.1 Write the Weil-template proof: Lefschetz fixed-point formula + Poincare duality + Hodge index on the Lambda-blueprint surface.
- 5.2 Verify the D-H discipline rigorously: the proof must not "prove RH" for D-H. K2 is satisfied by construction (Phase 1), but the assembled proof must transparently use the Euler product / cohomological structure that D-H lacks.
- 5.3 Verify the Weil specialization: the assembled proof, restricted to a function-field instance, must recover Weil's 1948 proof for curves over F_q. This is the K3 check.
- 5.4 Verify K1 escape: the assembled positivity must come from the SIGNATURE of an intersection form, not from a trace identity. This is what R3.5 demanded.

**Milestone**: a 100-200 page paper "A proof of the Riemann Hypothesis via arithmetic geometry on Spec(Z) x_F1 Spec(Z)". Publishable in Annals after expert review. Submission to the Clay Mathematics Institute for the Millennium Prize.

### Phase 6: Peer review and possible refutation (years 12-20)

The community will spend years verifying or refuting the proof. Examples of what to expect:

- 6.1 Initial reaction: skepticism, often with concrete technical objections. The proof team must respond to each.
- 6.2 Counterexample-hunting: experts will try to find a gap. Common gap locations: implicit assumptions in the F_1 framework, definitional issues with the intersection theory, subtle errors in the Hodge index argument.
- 6.3 Independent verification: ideally, a separate group reproduces the proof using slightly different machinery. If they succeed, the proof is robust.
- 6.4 Possible outcome: the proof is correct as stated, OR a gap is found and the proof is repaired, OR a gap is found that cannot be repaired and the program is back to Phase 4 or earlier.

Historical reference: Wiles's proof of Fermat's Last Theorem took 18 months between announcement and confirmation; the first version had a gap that was repaired with help from Richard Taylor. RH proof verification will likely be similar or longer.

## 3. Personnel and expertise needed

This is not a solo project. Required human expertise:

- **Algebraic geometry** (arithmetic surfaces, Chow theory, Hodge theory): primary contributor to Phases 1, 3, 4.C, 5.
- **Noncommutative geometry** (Connes program, adèle class space, trace formulas): primary contributor to Phases 0, 4.B; consultant throughout.
- **p-adic Hodge theory and prismatic cohomology** (BMS, Bhatt-Scholze, perfectoid spaces): primary contributor to Phase 2; consultant for Phases 3, 4.
- **F_1 / blueprint geometry** (Lorscheid, Borger, Toen-Vaquie): primary contributor to Phase 1; consultant for Phases 2, 3.
- **Tropical / characteristic-one geometry** (Adiprasito-Huh-Katz, Mikhalkin, Connes-Consani): primary contributor to Phase 4.A.
- **Analytic number theory** (zeta function, Selberg class, D-H): consultant throughout for the validation checks (K2, K3) and the explicit-formula side.

### AI as a collaborator type

AI assistants (Claude Code with mathematical libraries, plus current and future generations of mathematical-reasoning AI) are an effective collaborator across all phases, with role varying per the [§ AI division of labor across phases](#15-ai-division-of-labor-across-phases) table. Specifically:

- **Phase 0**: AI is the primary executor for literature synthesis, scorecard verification, R-series structural analysis. A small group (1 human + AI) can complete Phase 0 in 12 months.
- **Phases 1-2**: AI is a working collaborator: handles categorical / formal verifications, maintains the 17-constraint scorecard, computes explicit fiber products and cohomology classes. Human researcher leads the definitions and structural choices.
- **Phases 3-4**: AI is a sub-tool: assists with bookkeeping, computational verification of candidate proofs, K1/K2/K3 verification framework. Human researchers lead the creative construction.
- **Phase 5**: AI is a verification-and-exposition partner: checks each step against kill criteria, writes cross-referenced documentation, computes against the function-field benchmark.
- **Phase 6**: AI may be used by individual reviewers but does not lead the community process.

**What AI changes**:

1. **The bottleneck shifts from literature synthesis to mathematical creativity.** Phase 0 was traditionally a 2-3 year sub-program (deep reading of multiple research areas, building a unified picture); AI compresses this to 6-12 months. The savings get reinvested in Phase 4, the central open problem.

2. **The scorecard is maintained consistently across years.** Pre-AI, multi-year programs lost institutional memory: contributors changed, scorecards drifted, conventions shifted. AI keeps the 17-constraint framework consistent across sessions and across years, which sharpens the verification of every phase's deliverables.

3. **Reproducibility is enforced.** Every AI-executed experiment leaves code + data + writeup artifacts. Future sessions and reviewers can re-run any check. This is a structural advantage over hand-computed results.

4. **The headcount estimate reduces.** A traditional program would need 5-8 mathematicians plus graduate students; an AI-augmented program can run with 3-5 mathematicians plus AI. The savings come primarily from Phase 0 (the literature-survey roles) and the routine verification roles in Phases 1-2.

### Funding and staffing

Realistic minimum: a research group of 3-5 mathematicians at the postdoc-or-faculty level, with collaborators in adjacent areas, plus AI assistants throughout. Funding: NSF / Simons / ERC grants over the 12-18 year AI-augmented timeline. Total budget ~$5-15M, lower than a traditional 20-30 year program of similar scope.

This is a large undertaking. It cannot be staffed by hobbyists or by a single PhD student, even with AI assistance. The creative parts (Phases 3-4) require expert human judgment and long-horizon focus that AI does not provide.

## 4. Falsifiability and abandonment criteria

The program should be abandoned (or fundamentally restructured) if:

- **Phase 0 reveals R3.5 is too narrow.** If some NCG approach can in fact escape K1, the project's structural picture is wrong and the strategic premise needs revision. New plan needed.
- **Phase 1 fails at Lambda-Blpr fiber products.** Indicates the blueprint+Lambda hybrid is not the right surface candidate. Try pure Borger (Witt scheme) or pure Lorscheid alternatives.
- **Phase 2 fails at the prismatic foliation hypothesis.** Indicates prismatic cohomology is not compatible with Deninger-style foliations on the constructed surface. Try alternative cohomology theories (Hochschild, motivic, cyclic).
- **Phase 3 fails at the intersection product.** Indicates the surface candidate is not "geometric enough" to host arithmetic intersection theory. May require fundamentally new categorical setting.
- **Phase 4 fails after 5 years.** Indicates the Hodge index gap is not closable by the current machinery. Two options: abandon, OR pivot to Bombieri variational SOS.

These are HARD abandonment criteria. The program should not be stretched beyond them.

## 5. Probability assessment

Honest estimates based on 30+ years of partial progress on each phase by senior mathematicians, ADJUSTED for AI-augmented execution:

| Phase | Trad. probability | AI-augmented probability | Cumulative (AI) |
|---|---|---|---|
| 0 | 70% | 85% | 85% |
| 1 | 60% | 75% | 64% |
| 2 | 40% | 55% | 35% |
| 3 | 25% | 30% | 11% |
| 4 | 10% | 12% | 1.3% |
| 5 | 60% (given 4) | 75% (given 4) | 1.0% |
| 6 | 70% (given 5) | 80% (given 5) | 0.8% |

**Overall probability of a verified RH proof via this program: under 1%, AI-augmented or not.**

AI primarily accelerates the SURVEYABLE and VERIFIABLE work, raising Phase 0 / 1 / 5 probabilities by ~10-15 percentage points each. AI does NOT meaningfully accelerate the CREATIVE work in Phases 3-4, where the probability bottleneck lies. So the cumulative probability moves from ~0.4% (traditional) to ~0.8% (AI-augmented). A factor of 2 improvement, not an order of magnitude.

This estimate assumes the program is well-staffed and executed seriously. It is much higher than the base rate of "someone proves RH in the next 20 years" (which is also under 1%) because the program is structurally well-chosen: Architecture 2 is the unique route that can in principle close RH.

The MAJORITY of the program's value is in Phases 1-3, which produce significant partial results regardless of whether the full proof is reached. A working arithmetic intersection theory on Spec(Z) x_F1 Spec(Z) would be a major contribution to mathematics independent of RH. Similarly, the prismatic foliation hypothesis verification would close several long-standing open questions.

**What AI changes about the probability picture**:
- Phase 0 probability rises substantially: AI does the literature synthesis faster, more thoroughly, and more consistently than humans alone.
- Phase 1-2 probabilities rise moderately: AI handles the formal-verification overhead, letting human researchers focus on creative choices.
- Phase 3 probability rises slightly: AI helps with bookkeeping but the construction is still creative.
- Phase 4 probability barely changes: the Hodge index theorem requires creative leap; AI offers limited acceleration.
- Phases 5-6 probabilities rise: AI helps with verification and exposition.

The asymmetry (AI helps mapping more than construction) is structural to current AI capabilities and may shift as AI mathematical reasoning improves. If future AI can autonomously discover novel positivity arguments or construct new mathematical objects, the probability picture changes. As of 2026, this is speculative; the estimates above assume current AI capabilities.

## 6. What this project (the experimental thread) has already contributed

The experimental thread is AI-augmented Phase 0 work. As of 2026-05-25, it has produced:

- **The 17-constraint scorecard methodology** ([`2A_candidate_evaluation.md`](../../experiments/arithmetic_geometric/2A_candidate_evaluation.md)): the framework Phase 0.3 builds on. Six candidates scored.
- **The R-series structural analyses**: R1 (D-H exclusion universal), R2 (fiber product in Borger / Lorscheid), R2.5 (Lambda-blueprints hybrid proposal), R3 (Connes-Consani K1 verdict), R3.5 (no-shortcut theorem), R3.6 + R3.6.3 (arithmetic site deep dive + infrastructure follow-ups), R4 (Borger+Connes hybrid analysis), R5 (prismatic cohomology connection).
- **The 2A path forward synthesis** ([`2A_path_forward.md`](../../experiments/arithmetic_geometric/2A_path_forward.md)): the strategic plan above this operational program.
- **The 2C F_1 / Arakelov survey** ([`f1_arakelov_survey_2025.md`](f1_arakelov_survey_2025.md)): landscape mapping as of 2025.
- **The 2D Deninger micro-target** ([`2D_deninger_micro_target.md`](../../experiments/arithmetic_geometric/2D_deninger_micro_target.md)): identification of M3 (prismatic foliation hypothesis) as the smallest open conjecture.
- **The Davenport-Heilbronn discipline** (codified in [`_shared/davenport_heilbronn.py`](../../experiments/_shared/davenport_heilbronn.py)): the K2 unit test for the assembled proof.
- **The Bombieri explicit formula implementation** ([`e3f_weil_form_zeta.py`](../../experiments/positivity/e3f_weil_form_zeta.py)): the validation tool for Phase 2 Lefschetz trace formula recovery.
- **15 cross-architecture findings** ([`LEARNINGS.md`](../../experiments/LEARNINGS.md)): the cumulative structural picture.
- **Documented out-of-scope directions** ([`research_directions/`](research_directions/)): 8 research-grade follow-ups, each with operational specification.

This is approximately **50-70% of Phase 0** under traditional research methodology. The remaining Phase 0 work (independent expert verification, expert correspondent identification) requires human researchers.

**What the AI thread cannot do**: the actual research-grade construction work in Phases 1-5. The Lambda-blueprint rigorous development, the prismatic foliation hypothesis verification, the intersection theory definition, and the Hodge index theorem proof all require expert mathematicians operating over years. AI can SUPPORT each of these as documented in [§ AI division of labor across phases](#15-ai-division-of-labor-across-phases), but cannot LEAD them.

## 7. Recommended near-term action

For someone wanting to actually pursue this program, building on the AI-augmented Phase 0 already done in this repo:

**Step A** (1-3 months, AI-assisted): read the existing project documents, focusing on [`2A_path_forward.md`](../../experiments/arithmetic_geometric/2A_path_forward.md), [`f1_arakelov_survey_2025.md`](f1_arakelov_survey_2025.md), [`research_directions/`](research_directions/), and the [`PROOF_ARCHITECTURES_PLAN.md`](../../experiments/PROOF_ARCHITECTURES_PLAN.md) "Why this plan exists" section. AI can do the surface reading in a few sessions; human reader internalizes and judges.

**Step B** (1-3 months, AI-assisted): cross-check the 17-constraint scorecards against the primary literature. Identify any disagreements with the AI-produced analyses. AI helps with the cross-referencing; human researcher renders the expert verdict.

**Step C** (3-6 months, human-led with AI support): pick one of (i) R2.5 Lambda-blueprints (Direction 1), (ii) R4 Borger+Connes hybrid (Direction 2), or (iii) another candidate. Make the choice based on Step B's findings. AI can model the scorecard implications of each choice.

**Step D** (3-6 months, human-led): identify expert collaborators in the chosen direction's adjacent areas. This is a human relationship-building task.

**Step E** (6-12 months, collaborative): begin Phase 1 of the chosen direction. AI handles the formal infrastructure; human researchers handle the creative work.

Total time to begin Phase 1: 12-24 months from a serious start. Faster than pre-AI norms (which would be 24-36 months) because Steps A and B are AI-augmented.

If Steps A-D conclude the program is not viable as currently structured (e.g., the scorecards disagree with primary literature in a fundamental way, or no expert collaborators are available), that itself is a valuable Phase 0.5 negative result worth publishing.

## 8. Cross-cuts to project documents

This program builds on:
- [`PROOF_ARCHITECTURES_PLAN.md`](../../experiments/PROOF_ARCHITECTURES_PLAN.md): test plan with status table, "Why this plan exists" section.
- [`LEARNINGS.md`](../../experiments/LEARNINGS.md): 15 cross-architecture findings.
- [`2A_path_forward.md`](../../experiments/arithmetic_geometric/2A_path_forward.md): strategic plan (the level above this program).
- [`2A_candidate_evaluation.md`](../../experiments/arithmetic_geometric/2A_candidate_evaluation.md): 17-constraint scorecard methodology.
- [`2D_deninger_micro_target.md`](../../experiments/arithmetic_geometric/2D_deninger_micro_target.md): the M3 prismatic foliation hypothesis is Phase 2's central target.
- [`2A_R3_6_3_cc_infrastructure.md`](../../experiments/arithmetic_geometric/2A_R3_6_3_cc_infrastructure.md): infrastructure analysis for the Hodge index attempt.
- [`f1_arakelov_survey_2025.md`](f1_arakelov_survey_2025.md): the survey of frameworks Phase 0 builds on.

## 9. Honest closing

The marginal-positivity thesis says RH is true only at the margin. That is a precise instruction, not a discouragement: the proof must use the exact structure of zeta and produce positivity from a specific geometric source that does not yet exist in any current framework. The Hodge index theorem on a constructed surface below Z is the unique known candidate source. The program above is the best operational plan to build it, and building it is the work. It is hard, the odds are long, and it is worth attempting.

The plan is honest about its < 1% success probability and the multi-decade timeline. Most participants in the program would publish partial results without ever reaching the full proof. That is fine: each phase's deliverable is independently valuable. Even if RH is never proved by this program, the byproducts (Lambda-blueprint geometry, arithmetic intersection theory on Spec(Z) x_F1 Spec(Z), prismatic foliations, hyperring intersection theory) would substantially advance arithmetic geometry.

**The AI-augmentation angle**: this program is the first major-mathematics research program designed from the outset around AI as a collaborator type. The Phase 0 work done in this repo is a proof of concept: an AI assistant + a focused human owner can produce in months what traditional research methodology would do in 2-3 years. The acceleration is real and structural. But the acceleration is on the MAPPING side, not the CONSTRUCTION side. The Hodge index theorem remains as hard as it ever was; AI does not make it easier, only the surrounding infrastructure faster.

The project (this repo) has done what AI-augmented Phase 0 can do: identified the architectural picture, sharpened the scorecards, surfaced the central open problem (Hodge index in some constructible setting), and documented the strategic plan. Execution of Phases 1-5 requires research-grade mathematicians collaborating with AI over 12-18 calendar years. We can hand the program off; we cannot execute it ourselves.

**The bet**: a serious AI-augmented attempt has roughly twice the success probability of a pre-AI attempt of similar scope. From ~0.4% to ~0.8%. Still under 1%, but enough that the program is worth running for the partial results alone. Even if RH stays open, the byproducts move arithmetic geometry forward.
