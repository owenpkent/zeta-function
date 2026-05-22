# 2A: Path Forward — Strategic Plan for Architecture 2

> Synthesis of the R1-R5 analyses. The evaluation framework is now substantially complete; this document maps the path forward, with specific milestones and the proposal to develop BOTH hybrid candidates in parallel and let intersection theory pick the winner.
>
> Companion to [2A_candidate_evaluation.md](2A_candidate_evaluation.md), the R1-R5 documents, and the dossiers.

## 1. State of the field (post R1-R5)

The Architecture 2 evaluation thread has produced:

**Six single-corner candidates** scored against 17 constraints (see [2A_candidate_evaluation.md](2A_candidate_evaluation.md) §III).

**Two hybrid candidates**:
- **Λ-blueprints (R2.5)**: blueprints with built-in Adams operations. Predicted scorecard ~8 ✅.
- **Borger + Connes (R4)**: Λ-rings unified with adèle class space via U_t = ∏_p U_{log p}^{t/log p}. Predicted scorecard ~8 ✅.

**Structural theorems**:
- **K2 universal (R1)**: all six candidates pass D-H exclusion by construction.
- **K1 universal failure for NCG (R3.5)**: every trace-formula NCG framework has positivity ⟺ RH. No NCG approach can reduce RH to a strictly weaker statement.

**Universal blocker**:
- **Hodge index slot (xi)-(xiii)**: fails in every candidate. K1-blocked for all NCG, geometry-not-yet-built for the geometric route.

**Infrastructure ready**:
- **Prismatic cohomology (R5)**: likely the right cohomology theory for Spec(W(ℤ)). Closes (iv)-(vii) when it applies.

## 2. The clear central conclusion

**Only the geometric route can break K1.** Every other path is structurally blocked:
- Classical analytic methods → circularity wall (Arch 3 finding 7, the prime sum cancellation tightness for ζ)
- Noncommutative geometric methods → R3.5 no-shortcut theorem (positivity ⟺ RH structurally)
- Spectral methods → L-function-blind constructions don't encode Euler product (Arch 1 finding)

**The geometric route requires**:
1. **A constructed surface**: Spec(ℤ) ×_{𝔽₁} Spec(ℤ) realized as a 2-dimensional proper smooth-or-formal scheme/stack/topos.
2. **Intersection theory on this surface**: Pic, cycle class map, intersection pairing.
3. **A Hodge index theorem**: signature of the intersection pairing has the right form.
4. **The Hodge index theorem proved WITHOUT RH input**: Castelnuovo-Severi or similar, using projectivity / properness rather than analytic / NCG inputs.

If all four are accomplished, the function-field Weil argument transfers and gives RH.

## 3. The hybrid question: Λ-blueprints vs Borger + Connes

Which hybrid candidate should be developed first? Each has different strengths for the geometric route.

### 3.1 Λ-blueprints argument

**For**:
- Lorscheid's blueprint structure is the cleanest "surface" of any candidate. Blueprints generalize ordinary schemes with explicit "addition relations," giving a direct way to build 2-dimensional objects.
- Intersection theory should be developable along familiar scheme-theoretic lines, just enriched with the blueprint structure.
- Constraint (ii) is cleanest in this hybrid: (ℤ × ℤ, doubled relations) is a 2-dim blueprint by Lorscheid's dimension theory.
- Compatibility with function fields is trivial (𝔽_q is a blueprint).

**Against**:
- Cohomology development for blueprints is less mature than for Witt vectors / prismatic.
- The L-function connection is less direct than in Borger + Connes.

### 3.2 Borger + Connes argument

**For**:
- Trace formula explicit (constraint ix ✅ inherited from Connes).
- L-function connection direct (Euler factors from Connes' adelic side, Adams operations from Borger's side, both naturally fitting).
- Functional analysis tools available (Hilbert space, traces, operators).
- Spec(W(ℤ)) with prismatic cohomology (R5) provides ready-made cohomological infrastructure.

**Against**:
- Surface structure heavier (Witt vectors are conceptually more complex than blueprints).
- Intersection theory has to be developed in the formal-scheme / Witt-vector setting, which has less precedent.
- The continuous-action / discrete-action bridge (R4's U_t = ∏_p U_{log p}^{t/log p}) needs rigorous foundations.

### 3.3 The proposal: develop BOTH in parallel

**Reasoning**: the two hybrids address the geometric route from different angles. Different teams / mathematicians with different backgrounds might prefer one over the other. Cross-fertilization is likely as both develop. And the central question (does the geometric route actually work?) is answered when EITHER yields to intersection theory + Hodge index, not when both do.

**Concrete plan**:
- **Track A (Λ-blueprints)**: developed by someone with strong scheme-theoretic / algebraic-geometric background. Goals: foundational definitions, categorical structure, intersection theory.
- **Track B (Borger + Connes)**: developed by someone with strong functional-analytic / noncommutative-geometric background. Goals: rigorous bridge construction, prismatic cohomology application, trace formula recovery.

The two tracks meet at the Hodge index question. Whichever gets there first wins (in the sense of providing the working framework); both contribute partial machinery to the eventual proof.

## 4. Milestones for each track

### Track A: Λ-blueprints (estimated 5-10 years to milestone)

**Milestone A1 (1-2 years)**: Rigorous definition.
- Define Λ-blueprints with precise Fermat-Frobenius condition.
- Verify categorical properties (limits, colimits, embeddings of parent categories).
- Compute the fiber product Spec(ℤ) ×_{𝔽₁} Spec(ℤ) in Λ-Blpr explicitly. Verify it gives the 2-dim object.
- Output: ~3 papers establishing the foundations.

**Milestone A2 (2-3 years)**: Cohomology theory.
- Define a cohomology theory for Λ-blueprint schemes.
- Investigate prismatic cohomology compatibility (R5).
- Establish basic structural properties: finiteness, Künneth, Poincaré duality.
- Output: ~2-3 papers establishing the cohomology.

**Milestone A3 (2-3 years)**: Intersection theory.
- Define Pic and cycle class map on the blueprint surface.
- Prove intersection pairing is bilinear, symmetric, non-degenerate.
- Compute the Picard rank (Néron-Severi analog).
- Output: ~2 papers establishing intersection theory.

**Milestone A4 (1-2 years)**: Hodge index theorem.
- Prove or refute: the intersection pairing on Pic(Λ-blueprint-surface) has signature (1, ρ - 1).
- If proved, derive RH via the standard Castelnuovo-Severi argument.
- If refuted, identify what's missing and either revise or abandon Track A.
- Output: ~1 paper.

**Total estimated time**: 5-10 years; ~7-9 papers.

### Track B: Borger + Connes hybrid (estimated 5-10 years to milestone)

**Milestone B1 (1-2 years)**: Rigorous bridge construction.
- Identify the right measure μ on W(ℤ).
- Prove the multiplicative-completion U_t = ∏_p U_{log p}^{t/log p} converges.
- Establish the bridge between Borger's Spec(W(ℤ)) and Connes' L²(X_ℚ).
- Output: ~2 papers.

**Milestone B2 (2-3 years)**: Prismatic cohomology application.
- Apply BMS prismatic cohomology to Spec(W(ℤ)) rigorously.
- Verify Adams operations ψ_p act on H*_prism with spectrum at zeta zeros (constraint viii).
- Establish trace formula on the hybrid framework.
- Output: ~2-3 papers.

**Milestone B3 (2-3 years)**: Intersection theory.
- Develop cycle class theory on Spec(W(ℤ)) (or its compactification).
- Establish intersection pairing on Pic.
- Output: ~2 papers.

**Milestone B4 (1-2 years)**: Hodge index theorem.
- Prove or refute on the Borger + Connes surface.
- Output: ~1 paper.

**Total estimated time**: similar to Track A.

### Joint synthesis milestone (after either A4 or B4)

If either track succeeds at its Hodge index step, the RH proof follows almost immediately by the standard Weil-style argument. **Estimated 1-2 years** to fully write up the proof, including verification of constraints (xiv)-(xvii) (which are easier in either hybrid).

**Total timeline**: 6-12 years from start to RH proof, IF the geometric route is actually viable. The "IF" is the key uncertainty.

## 5. What if the geometric route doesn't work?

If after 5-10 years of serious development, neither Track A nor Track B produces a Hodge index theorem, we'd know something deep about the limits of arithmetic geometry:

- Either: Spec(ℤ) ×_{𝔽₁} Spec(ℤ) doesn't admit the right kind of projectivity, OR
- A new mathematical idea is needed beyond Λ-blueprints + prismatic cohomology + intersection theory.

In that case, Architecture 2 itself would be ruled out as a path to RH, and the field would need entirely new approaches (perhaps in directions not foreseen by current programs).

**Honest assessment**: the geometric route is plausible but not guaranteed. R3.5 says NCG can't escape K1, but doesn't say the geometric route definitely works. Whether intersection theory + Hodge index can be made to work on a hypothetical Spec(ℤ)-surface is the deepest open question in arithmetic geometry.

## 6. The R3.6.3 connection

R3.6.3 surfaced the possibility that **Connes-Consani's categorical machinery (topos theory, hyperrings, characteristic-one geometry) might serve as INFRASTRUCTURE for the geometric route**, even though it doesn't directly provide K1-escaping positivity.

This is potentially relevant to either track:

**For Track A**: the topos-theoretic perspective on blueprints might be enriched by Connes-Consani's arithmetic site structure. Could a "blueprint topos" or "Λ-blueprint topos" be more powerful than ordinary blueprint schemes?

**For Track B**: the hyperring structure on the adèle class space might tie naturally to Witt vector formal schemes. The "Witt vector hyperring" formulation could be a hybrid object combining Borger's and Connes-Consani's frameworks.

So R3.6.3 is potentially relevant to BOTH tracks. Investigating it could provide cross-track infrastructure.

## 7. Sequencing recommendation

Given limited resources (mathematician-years, attention), the question becomes: which milestone should be pursued FIRST?

**My recommendation** (with appropriate humility):

**Phase 1 (Year 1-2): foundational pre-work for both tracks**:
- Develop the basic Λ-blueprint definition and properties (Milestone A1)
- Establish the basic Borger + Connes bridge (Milestone B1)
- Run R3.6.3 investigation (Connes-Consani machinery as infrastructure)
- Output: 4-6 foundational papers

**Phase 2 (Year 3-5): parallel cohomology development**:
- Track A cohomology (Milestone A2)
- Track B prismatic application (Milestone B2)
- Cross-fertilization: each track informs the other about what cohomology slot needs filling
- Output: 5-7 papers

**Phase 3 (Year 5-8): parallel intersection theory**:
- Track A intersection theory (Milestone A3)
- Track B intersection theory (Milestone B3)
- Output: 4 papers; the first to give a non-trivial intersection pairing wins

**Phase 4 (Year 8-10): Hodge index attack**:
- Whichever track has more developed intersection theory tackles Hodge index first
- The other track provides cross-reference / sanity check
- Output: 1-2 papers, possibly the RH proof

**Realistic outcome**: 10-year research program, succeeds with probability < 50%. The "fail mode" (no Hodge index theorem on either surface) is also a significant outcome — it would confirm that Architecture 2 is dead and force the field to look elsewhere.

## 8. Concrete next steps for the project

The Architecture 2 evaluation framework is now substantially complete at the meta-analysis level. The project's contributions to the field are:

1. **The 17-constraint specification** (2A_weil_proof_diff.md §5) provides a precise checklist for any candidate.
2. **The evaluation framework** (2A_candidate_evaluation.md) provides scoring methodology and kill criteria.
3. **The no-shortcut theorem** (R3.5) clarifies that only the geometric route can break K1.
4. **The hybrid proposals** (R2.5 Λ-blueprints, R4 Borger + Connes) identify the two natural directions for the geometric route.
5. **Per-candidate dossiers** provide deep-dives on Borger and Lorscheid (others could be added).

For the project to continue contributing, the natural next steps are:

**Project-level** (no expert collaboration required):
- Add dossiers for Connes, Deninger, Deitmar, Connes-Consani (one per candidate, following the existing Borger/Lorscheid template).
- Verify R3.5's specific application to each Connes-Consani positivity formulation (R3.6.1 follow-up).
- Investigate the triple hybrid (Λ-blueprints + Connes adelic side, R3.6.3 + R4 combined).

**Beyond-project** (requires expert collaboration or significant new work):
- Develop Track A or Track B foundationally.
- Investigate prismatic cohomology applied to Spec(W(ℤ)) (R5.1).
- Investigate Connes-Consani machinery as infrastructure (R3.6.3).

The project as currently configured (computational + literature analysis) can contribute to the project-level tasks but not to the beyond-project ones, which require multi-year specialist development.

## 9. The big-picture summary

**The Architecture 2 landscape after R1-R5**:

- 6 single-corner candidates, all ❌ on (xi)-(xiii).
- 2 hybrid candidates, both predicted ~8 ✅ but ❌ on (xi)-(xiii).
- 1 universal structural blocker: the K1 wall on NCG-style positivity (R3.5 theorem).
- 1 universal escape route: the geometric construction (intersection theory + Hodge index, not yet built).
- ~5-10 year, multi-paper research program to attempt the escape route, with success probability < 50%.

**The path forward**:
- Develop both hybrid candidates (Λ-blueprints and Borger + Connes) in parallel.
- Use prismatic cohomology (R5) as the cohomology theory for both.
- Investigate Connes-Consani machinery (R3.6.3) as cross-track infrastructure.
- Attack Hodge index on whichever track reaches it first.

**The honest verdict**: this is hard, multi-decade research. The evaluation framework clarifies what needs to be done and gives a structured way to evaluate progress. The actual development is beyond the scope of any single project.

## 10. What this project HAS achieved

Looking back at the session's R1-R5 outputs:

- **R1**: D-H exclusion sharpened across all six candidates. K2 universal.
- **R2**: Fiber products computed in Borger and Lorscheid. Complementary half-candidates identified.
- **R2.5**: Λ-blueprints proposed as the natural hybrid.
- **R3**: Connes-Consani positivity conjectures classified by K1 status.
- **R3.5**: Universal no-shortcut theorem for NCG approaches proved.
- **R3.6**: Arithmetic-site / hyperring / characteristic-one machinery analyzed; Connes-Consani sharpened to ❌ on positivity.
- **R4**: Borger + Connes hybrid analyzed; complementary to Λ-blueprints.
- **R5**: Prismatic cohomology identified as the right cohomology theory for both hybrids.

**The project's contribution to the RH literature**: a structured framework for evaluating Architecture 2 candidates that's more rigorous and explicit than the existing literature provides. Whether this framework helps actual progress toward RH depends on whether someone takes up the hybrid development tracks.

**The honest meta-conclusion**: Architecture 2 is the right place to look for an RH proof (per R3.5 ruling out other architectures), but the specific construction problem is hard enough that even the existing categorical machinery (Λ-rings, blueprints, adèle class space, prismatic cohomology, arithmetic sites) doesn't close it. New mathematics is needed, plausibly along the hybrid + geometric lines identified here.

The project has, hopefully, made the path forward legible. That's the most that can be done at the meta-analysis level.
