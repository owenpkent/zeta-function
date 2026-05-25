# A Proof Program for the Riemann Hypothesis: AI-Only Execution Variant

> **Sibling to** [`proof_program.md`](proof_program.md) (which is the AI-augmented, human-led version). This document is the variant where AI does everything: literature synthesis, structural mapping, mathematical creativity, formal verification, and (via formal proof assistants) the verification process itself. No human researcher in the critical path.
>
> **Premise**: assume an AI system (or coordinated set of AI agents) with current best capabilities (Claude Opus 4.7 + similar) PLUS access to:
> - Mathematical libraries (`mpmath`, `numpy`, `cvxpy`, `sympy`, `sage`).
> - Formal theorem provers (`Lean 4` + Mathlib, `Coq`, `Isabelle`).
> - The full arXiv corpus and major journal databases.
> - Persistent memory across multi-year-equivalent compute time.
> - Multi-agent orchestration to run independent attempts in parallel.
>
> The question this document answers: **what would the proof program look like if AI agents executed every phase without human researchers in the critical path?** This is partly aspirational, partly speculative, and partly a design exercise in falsifiability under AI-only execution. The honest version of [`proof_program.md`](proof_program.md) says AI cannot do the construction work; this document asks what the program would have to be designed to overcome that.
>
> **Critical reading guidance**: this is NOT a claim that AI can prove RH today. It is a design specification for a research program that would attempt RH using AI as the sole executor, with capability requirements identified. The probability of success under this variant is LOWER than the AI-augmented + human-led variant, not higher.

---

## 0. The capability gap

The AI-augmented version of [`proof_program.md`](proof_program.md) explicitly says AI cannot do:

1. Genuinely novel mathematical creativity (the Hodge index theorem).
2. Construct genuinely new mathematical objects (the foliated space).
3. Long-horizon multi-year research focus.
4. Independent expert judgment without external verification.
5. Discovering structural obstacles AI's training did not cover.

For AI-only execution, each of these gaps must be addressed by program design, not by assuming the capability exists. The strategies:

| Gap | Mitigation strategy |
|---|---|
| 1. Mathematical creativity | Multi-agent parallel exploration of candidate proofs. Each agent tries a different attack angle. Formal verification filters out the wrong ones. Volume substitutes for individual creativity. |
| 2. Constructing new objects | Constrain the construction space via the 17-constraint scorecard; brute-force search over structural choices satisfying constraints; formal verification of each candidate's properties. |
| 3. Long-horizon focus | Persistent project state in git + dossier files; multi-year-equivalent compute scheduled in distinct sessions with explicit handoff state; agents read prior session state as context. |
| 4. Independent judgment | Multi-agent consensus + formal verification. Three independent agents must agree, AND the result must be machine-checked, before accepting any claim. |
| 5. Detecting novel obstacles | Adversarial counter-example agents whose only job is to find gaps in proposed proofs; broad analogy search across the mathematical literature. |

These mitigations are speculative for capability 1 and 5. They may or may not suffice. The probability assessment below reflects this uncertainty.

---

## 1. Goal hierarchy (unchanged from AI-augmented version)

Same as [`proof_program.md` § 1](proof_program.md#1-goal-hierarchy). G1 through G7, with the same dependencies. The hierarchy is structural to the problem, not to who's executing it.

---

## 2. Agent architecture

AI-only execution requires multiple agent roles, each with a specialized prompt / behavior profile and shared access to the project state:

### 2.1 The roles

- **Surveyor agents**: read literature, build scorecards, update the 17-constraint framework. Multi-agent: each surveyor reads a different sub-corpus and contributes findings; consensus produces the unified scorecard.
- **Builder agents**: propose constructions (Fermat-Frobenius in blueprint language, intersection products, candidate Hodge index arguments). Multi-agent: each builder explores a different construction space; outputs are evaluated against the scorecard.
- **Verifier agents**: check proposed constructions via formal theorem provers. Convert candidate proofs to Lean 4 / Mathlib statements; run automated proof search; reject candidates that fail.
- **Adversary agents**: actively search for counterexamples and structural obstacles. Test every candidate against Davenport-Heilbronn (K2), function-field specialization (K3), and circular reasoning (K1). Try to break each proposed construction.
- **Synthesizer agents**: integrate the outputs of surveyors, builders, verifiers, and adversaries into the project dossier. Maintain the LEARNINGS.md cross-architecture findings file.
- **Orchestrator agent**: schedules work across the other roles, manages compute budget, decides when to abandon a direction and pivot.

### 2.2 The verification stack

This is the most critical AI-only design choice. Without human peer review, all proposed claims must be machine-verified:

1. **Mechanical computation**: at every claim, compute the result with at least two independent code paths (`mpmath` vs `sage`, or `cvxpy` vs `scipy linprog`). Agreement is necessary but not sufficient.
2. **Symbolic verification**: claims expressible in `sympy` / `Mathematica`-style symbolic algebra are verified there.
3. **Formal proof in Lean 4**: structural claims (R3.5 no-shortcut theorem, 4E.3 line-restriction lemma, Hodge index theorem on the constructed surface) are translated to Lean 4 statements and proved with Mathlib + automated proof search. **A claim is not accepted until its Lean proof is checked by Mathlib's kernel.**
4. **Multi-agent consensus**: three independent agent runs must produce the same Lean proof (with possibly different proof scripts) before the claim is canonical.

This stack replaces traditional peer review. Its weakness: Lean 4 / Mathlib do not yet cover all of the mathematics needed (prismatic cohomology, Lambda-rings, blueprint geometry, NCG). Substantial infrastructure work is needed to extend Mathlib before the verification stack is operational.

### 2.3 Memory and continuity

AI-only execution over a 12-18 calendar year program requires durable project state:

- The git repository is the canonical state.
- Each session re-reads the LEARNINGS findings, the 17-constraint scorecards, and the path-forward documents.
- Session-end summaries are written to `MEMORY.md` (project memory) plus per-direction dossiers.
- Compute is scheduled in coherent multi-month batches with explicit goals, not random sessions.

This is doable with current orchestration infrastructure (cron jobs, agent loops, scheduled tasks). The hard part is keeping the scientific direction coherent across years of compute.

---

## 3. Per-phase AI-only execution

Each phase is the same goal as in [`proof_program.md` § 2](proof_program.md#2-phase-structure), but executed by the agent architecture above. Key differences flagged.

### Phase 0: Foundation (3-6 months under AI-only)

Substantially the same as AI-augmented, but compressed. Surveyor agents read the F_1 / Arakelov / prismatic / NCG corpora in parallel; synthesizer agent produces the unified scorecard.

**AI-only difference**: the human-led step "identify expert correspondents" is replaced with "identify the most cited / most structurally important papers and map them as the canonical reference set". The trade-off: no expert intuition about which papers are good, but exhaustive coverage of what's published.

**Falsifiability**: if the surveyors disagree fundamentally on the scorecards (e.g., three independent surveyors score the same candidate differently), surfaces uncertainty that human intervention should resolve. In a pure AI-only run, multi-agent consensus arbitrates.

### Phase 1: Lambda-blueprints (6-12 months under AI-only)

Builder agents propose definitions of Lambda-blueprint (definition of Fermat-Frobenius in blueprint language). Multiple proposals run in parallel: blueprint-relation form, Adams operation form, delta-ring lifted form.

Verifier agents translate each proposed definition to Lean 4 and verify basic properties (composition, identity, full faithfulness of Lambda-Rings -> Lambda-Blpr).

Adversary agents test each definition against:
- Specialization to Lambda-Rings (does Lambda-Blpr properly contain Lambda-Rings?)
- Specialization to Blpr (does it contain blueprints?)
- D-H exclusion (K2 by construction)
- Fiber product computation: does Spec(Z) x_F1 Spec(Z) compute to a 2-dimensional object?

The verifier output is the canonical definition.

**Risk**: AI's proposed Fermat-Frobenius condition might be the "obvious" candidate that misses a subtle category-theoretic obstruction a human expert would catch. Mitigation: adversary agents specifically search for such obstructions; multi-agent consensus required.

**Timeline**: AI-only compresses 1-2 calendar years to 6-12 months because the agents work in parallel and don't need to context-switch.

### Phase 2: Prismatic cohomology (12-18 months under AI-only)

Builder agents apply Bhatt-Morrow-Scholze prismatic cohomology machinery to Spec(W(Z)) and to the Lambda-blueprint surface from Phase 1. Multiple candidates: derived limit of truncated Witt rings, direct formal-scheme definition, prismatic site of perfect prisms.

Verifier agents formalize the R5 questions Q1-Q5 in Lean 4 and prove them (or fail to prove and flag for adversary review).

Adversary agents test each prismatic cohomology candidate against:
- Comparison with classical theories in special cases (Spec(F_q) -> étale cohomology of points; smooth curves -> Weil cohomology).
- The 4E.3-style line-restriction lemma analogs.
- Künneth formula on products.

**Risk**: prismatic cohomology of profinite objects like Spec(W(Z)) has open technical issues even for experts (this is exactly what Direction 3's Q1 asks). AI may produce a candidate that "looks right" but has hidden infinities. Mitigation: rigorous Lean 4 formalization, multi-candidate parallel exploration.

**Timeline**: AI-only at 12-18 months (vs 2-3 years AI-augmented).

### Phase 3: Arithmetic intersection theory (12-24 months under AI-only)

Builder agents propose Chow-style groups and intersection products on the Lambda-blueprint surface. Multiple candidates: cycles modulo rational equivalence (classical), prismatic-cohomology-derived cycle classes, hyperring-valued cycle classes (per Direction 5).

Verifier agents check bilinearity, projection formula, compatibility with Frobenius. Each property is a Lean 4 theorem.

Adversary agents test:
- Specialization to Chow theory for curves over F_q.
- Compatibility with the prismatic cohomology cycle class map (Phase 2 Q4).
- K1 escape: the intersection-theoretic structure must be different from trace-formula NCG (so R3.5 doesn't apply).

**Timeline**: AI-only at 12-24 months (vs 4-6 years AI-augmented). This is the largest absolute time savings: the construction work is mechanical-ish once the constraints are spelled out, and AI agents can run many candidate constructions in parallel.

### Phase 4: The Hodge index attempt (THE crux, 2-5 years under AI-only)

This is where the AI-only hypothesis is tested. Three sub-programs run in parallel:

**4.A Tropical-arithmetic Hodge bridge**: Builder agents adapt Adiprasito-Huh-Katz tropical Hodge theory to the arithmetic surface. Try multiple "tropicalization" definitions.

**4.B Sheaf-theoretic in Connes-Consani topos**: Builder agents work in the arithmetic site topos, propose hyperring-valued Hodge structures, try to derive positivity from sheaf cohomology.

**4.C Direct algebraic-geometric**: Builder agents work on the Lambda-blueprint surface directly, propose candidate intersection forms, try to verify signature (1, k).

For each angle, verifier agents formalize candidate Hodge index statements in Lean 4. Adversary agents try to find counterexamples (intersection forms with wrong signature, candidate proofs with circular reasoning).

**The compute model**: hundreds to thousands of parallel attempts, each pursuing a different approach in detail. Most fail. A small fraction produce verifiable Lean 4 proofs. The orchestrator monitors and prunes.

**Capability requirement**: this phase requires AI agents to produce genuinely novel mathematical arguments. As of 2026, AI is not demonstrated at this level for problems of Hodge-index difficulty. The probability of success under current AI capabilities: 1-5%, conditional on Phases 1-3 succeeding.

**Falsifiability**: 5 years of parallel attempts without a Lean-verified Hodge index proof on any of the three angles. At that point, either:
- (Continue) deploy more parallel attempts; the search space is large.
- (Abandon) declare the AI-only attempt failed and escalate to human-led work (the [`proof_program.md`](proof_program.md) AI-augmented version).
- (Pivot) try non-Hodge-index angles (Bombieri variational SOS per Direction 6).

### Phase 5: Assembly (3-6 months under AI-only)

Synthesizer agents combine the Phase 4 result with Phases 1-4 into the full Weil-template proof. Verifier agents formalize the full proof in Lean 4. Adversary agents stress-test every step against K1-K4.

If Phase 4 produced a Lean-verified Hodge index theorem, Phase 5 is mechanical. Synthesizer writes the integrated proof; verifier checks the full Lean development.

### Phase 6: Verification (1-3 months under AI-only)

Replaces traditional peer review with formal verification:

- The full proof is in Lean 4 / Mathlib.
- Mathlib's kernel verifies every step.
- Independent agents run the verification (multi-agent consensus on the proof checking).
- The proof is published as a Lean development on GitHub, with the proof artifacts and the explanatory dossier.

The mathematical community can then read and judge, but the formal verification is what makes the proof canonical.

**Capability requirement**: by Phase 6 in the AI-only timeline, Lean 4 / Mathlib must cover all of the mathematics used in Phases 1-5. This requires substantial Mathlib expansion in arithmetic geometry, NCG, prismatic cohomology. Estimated: 5-10 person-years of Mathlib library work, which can itself be AI-assisted.

---

## 4. Total timeline under AI-only execution

Adding the per-phase estimates:

| Phase | AI-only time | AI-augmented time |
|---|---|---|
| 0 | 3-6 months | 12 months |
| 1 | 6-12 months | 1-2 years |
| 2 | 12-18 months | 2-3 years |
| 3 | 12-24 months | 4-6 years |
| 4 | 2-5 years | 7-12 years |
| 5 | 3-6 months | (within Phase 4) |
| 6 | 1-3 months | 3-5 years |
| **Total** | **5-10 years** | **12-18 years** |

AI-only is roughly half the calendar time of AI-augmented, but:
- Requires Lean 4 / Mathlib coverage of advanced arithmetic geometry (which itself takes years).
- Requires AI capabilities at Phase 4 (mathematical creativity for the Hodge index theorem) that are not currently demonstrated.
- Has higher variance: either the parallel search finds a proof, or it does not.

---

## 5. Probability assessment under AI-only

| Phase | AI-augmented probability | AI-only probability | Cumulative (AI-only) |
|---|---|---|---|
| 0 | 85% | 90% | 90% |
| 1 | 75% | 70% | 63% |
| 2 | 55% | 50% | 31% |
| 3 | 30% | 25% | 8% |
| 4 | 12% | 3-8% | 0.2-0.6% |
| 5 | 75% | 80% | 0.2-0.5% |
| 6 | 80% | 95% | 0.2-0.5% |

**Overall probability under AI-only: 0.2-0.5%, vs ~0.8% AI-augmented.**

AI-only is LOWER probability, not higher. The reason: Phase 4 (the Hodge index theorem) requires mathematical creativity, and AI's creativity is currently weaker than expert human mathematicians for problems of this depth. The verification stack (Lean 4) helps prevent FALSE proofs from being accepted, but it does not help DISCOVER true proofs.

The gain from AI-only is in TIMELINE (5-10 years vs 12-18) and in VERIFIABILITY (every claim is machine-checked). The loss is in PROBABILITY of finding the proof at all.

**When AI-only becomes higher probability than AI-augmented**: when AI's mathematical creativity at the Phase-4 level matches expert humans'. This is the AI capability threshold to watch. As of 2026, this is not the case for problems of Hodge-index difficulty. By 2030-2035, it might be, but this is speculation.

---

## 6. What this design accomplishes even if the proof fails

Even if AI-only execution fails to produce the RH proof, the program produces:

1. **A Lean 4 formalization of substantial arithmetic geometry**: Lambda-blueprints, prismatic cohomology of Spec(W(Z)), the 17-constraint framework, the D-H discipline, the R3.5 no-shortcut theorem. This expands Mathlib substantially.
2. **A multi-agent orchestration framework for mathematical research**: roles, verification stack, memory model. Reusable for other major-mathematics problems.
3. **A scorecard of which approaches AI agents CAN make progress on**: the Phase-by-Phase results.
4. **A demonstration of multi-year-scale persistent AI research**: durable state, consistent direction, machine-verified output.

These are not the proof of RH, but they are major contributions to AI-augmented mathematics infrastructure.

---

## 7. What's needed to actually start

If someone wanted to launch the AI-only variant today (2026), the prerequisites are:

1. **Compute**: persistent multi-agent infrastructure capable of running 10-100 agents in parallel for years. Estimated cost: $10M-100M over the program (compute alone). Major cloud provider partnership likely required.

2. **Lean 4 / Mathlib coverage**: substantial expansion of Mathlib in arithmetic geometry, NCG, prismatic cohomology. Estimated: 5-10 person-years (which can be 50-70% AI). Pre-requisite for Phase 4 and Phase 6.

3. **Orchestration software**: multi-agent role specialization, durable state, formal verification integration. Estimated: 1-2 years of software development.

4. **Initial human oversight**: even in an AI-only program, humans should monitor the orchestrator's decisions, validate the scorecards against published literature, and check for systematic AI failures. This is "AI-only with adult supervision" rather than fully autonomous.

5. **Governance**: who owns the proof if it succeeds? What if the AI produces a flawed proof that the verification stack accepts? These are real questions for an AI-only major-mathematics program.

Total upfront cost (pre-Phase-1): 2-3 years and $20M-50M to build the infrastructure. This is roughly the same as funding a traditional research group, but the work product is different (multi-agent AI infrastructure rather than a research group's intellectual output).

---

## 8. Honest assessment

The AI-only variant is a thought experiment about what a research program would look like if AI did everything. As of 2026:

- **Phases 0, 5, 6**: AI can do these now under the right verification infrastructure (Lean 4 + multi-agent orchestration). Phase 6 in particular benefits hugely from formal verification.
- **Phases 1, 2, 3**: AI can do significant parts now, with the rest requiring capability improvements over the next 3-5 years (per current AI scaling trends).
- **Phase 4**: requires AI mathematical creativity that is not currently demonstrated for problems of Hodge-index difficulty. Whether this becomes possible by 2030-2035 is genuinely uncertain.

**The honest probability**: 0.2-0.5% under AI-only, vs ~0.8% under AI-augmented. AI-only is not the right way to attempt RH today. It might become so by 2030-2035 if AI mathematical creativity improves, in which case this document becomes the operational plan.

**The honest recommendation**: pursue the AI-augmented version ([`proof_program.md`](proof_program.md)) for actual proof attempts. Use this AI-only variant as:
- A target architecture to design AI capabilities toward.
- A benchmark for evaluating when AI is ready for autonomous major-mathematics work.
- A speculative document for funding agencies considering long-term AI-for-math infrastructure.

---

## 9. Cross-cuts

- [`proof_program.md`](proof_program.md): the AI-augmented + human-led version. Higher current probability, longer timeline.
- [`research_directions/`](research_directions/): the eight directions, each of which has AI-led and human-led parts under the AI-augmented version. Under AI-only, all eight are AI-led.
- [`../../experiments/PROOF_ARCHITECTURES_PLAN.md`](../../experiments/PROOF_ARCHITECTURES_PLAN.md): the test plan. AI-centric framing already added there.

---

## 10. Honest closing

If RH is proved by AI alone in the next decade, the program will look something like what's documented here, with capability gaps that have closed via AI scaling and Mathlib expansion. If RH is not proved by AI alone, this document still serves as a record of what such an attempt would have required.

The structural picture from the project's experimental thread remains: only Architecture 2's geometric route can in principle close RH, and the Hodge index theorem on a constructed surface is the central open problem. Whether AI or humans (or both) find it, the architecture is the same.

The variant adds: with sufficient AI capability and verification infrastructure, the program is in-principle self-contained. No human in the critical path. This is not a near-term reality but a target design.

As of 2026-05-25, this is speculative. We are documenting the design now so that, when AI capabilities reach the level required, the program can begin without re-deriving the structural framework.
