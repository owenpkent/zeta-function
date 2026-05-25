# Phase State (operational)

> Read by ORCHESTRATOR at the start of every AI-only session. Maintained by SYNTHESIZER. Living document.

## Current state (2026-05-25)

**Active mode**: AI-augmented (with human owner in critical path). Transition to AI-only execution per [`docs/03_research/proof_program_ai_only.md`](docs/03_research/proof_program_ai_only.md) requires infrastructure not yet built (see [`OPERATIONS.md`](OPERATIONS.md) §7).

**Current phase**: Phase 0 (Foundation), substantially complete. Phase 1 (Direction 1, Lambda-blueprints) entered in session 002 with milestone 4.1 having three candidate definitions on the table.

**Phase 0 deliverables done**:
- ✅ Six 2A candidate scorecards (Deitmar, Lorscheid, Borger, Connes, Connes-Consani, Deninger).
- ✅ R-series structural analyses (R1, R2, R2.5, R3, R3.5, R3.6, R3.6.3, R4, R5).
- ✅ 2A_path_forward synthesis.
- ✅ 2C F_1 / Arakelov survey as of 2025.
- ✅ 2D Deninger micro-target identification (M3 prismatic foliation hypothesis).
- ✅ 15 cross-architecture findings in [`experiments/LEARNINGS.md`](experiments/LEARNINGS.md).
- ✅ Eight research directions documented in [`docs/03_research/research_directions/`](docs/03_research/research_directions/).
- ✅ AI-augmented and AI-only proof programs documented.
- ✅ Lean 4 Phase 1 substrate (green build on Lean 4.13.0 + Mathlib v4.13.0; typed definitions with documented VERIFIER target IDs).
- ✅ Agent role specifications in [`.claude/agents/`](.claude/agents/).
- ✅ Operations guide ([`OPERATIONS.md`](OPERATIONS.md)).

**Phase 0 deliverables remaining**:
- ⏳ Independent expert verification of the 2A scorecards (HUMAN: requires expert correspondents).
- ⏳ Identify expert correspondents in arithmetic geometry, NCG, prismatic cohomology (HUMAN).
- 🟡 Lean 4 / Mathlib expansion: PHASE 1 SUBSTRATE landed (2026-05-25) and BUILD IS GREEN. The placeholder `True`/`Unit` skeleton has been upgraded to typed data wired to Mathlib `riemannZeta`, real complex-analytic L-functions, real bivariate cosine polynomials, and typed Lambda-blueprint axioms. `lake build` succeeds end-to-end on Windows 11 with Lean 4.13.0 + Mathlib v4.13.0 (all 2250 modules compile; warnings are exactly the documented `sorry` markers). See [`lean/README.md`](lean/README.md) for the VERIFIER target ID table (#FE-1..#MB-6). Full proof closure remains multi-year.

**Architectures 1, 3, 4 status**: substantially closed at the project level.
- Arch 1 (spectral): 1A-1C complete; 1D literature pending.
- Arch 3 (positivity): complete through 3B.3 rigorous Li witness at n = 336,000 + 3F-3I Weil-form duality cross-cuts + 3J Schur-complement two-clock decomposition (asymptote -78.7%, sharpens raw Gram detector by ~30x) + 3K hypothetical-off-line-zero perturbation (disproof in Gram-matrix family has no leverage point).
- Arch 4 (analytic): complete through 4E.8 SDP saturation + 4A+4C V-K dossier. The LP/SDP family is structurally closed; remaining escapes (Bombieri variational SOS, Heath-Brown multi-zero MT) are research-grade Directions 6 and 7.

## Compute budget

| Item | Used | Budgeted | Remaining |
|---|---|---|---|
| Project sessions to date | ~50-100 (estimate) | unbounded (project-level) | n/a |
| Lean 4 proofs landed | 1 (RHMathlib_iff_RH_zeta) + Phase 1 typed substrate | per-direction (see Directions 1-8) | substantial |
| Mathlib contributions | 0 | 5-10 person-years | substantial |

## Recommended next session actions

**See [`experiments/orchestrator_sessions/session_002.md`](experiments/orchestrator_sessions/session_002.md) for the current session's concrete plan.**

Summary of session 002 outcomes (2026-05-25):
- Three BUILDERs returned three F-F candidates for Direction 1 milestone 4.1. Candidates A (blueprint-relation) and B (Adams quotient) are logically equivalent; candidate C (delta-ring lifted) is strictly stronger and uncovers a real F_p obstruction (Buium polynomial does not vanish in F_p, so F_p is not a native delta-blueprint at p).
- VERIFIER on R3.5 eliminated the global sorry by refactoring R3.5 into a typed `TraceFormulaNCG` framework; the structural content of R3.5 ("Positivity F t ↔ RH F.target_L for any of P-SA, P-Q, P-OP") is now proved by `rfl`. Build remains green. Highest-leverage Mathlib gap identified: Weil's explicit formula in operator form.
- Recommended session 003 deployment: three VERIFIERs in parallel attempting `#FF-A-1..3`, `#FF-B-1..3`, `#FF-C-1..4` plus one ADVERSARY targeting D-H against all three candidates. Details in session_002.md.

Higher-level strategic options remain (Option B AI-only transition requires $20M-50M infrastructure; Option C human-group handoff is the conservative fallback). The session-002 plan is Option A continuation.

## Falsifiability triggers (per proof_program_ai_only.md §4)

- Phase 0 reveals R3.5 too narrow: ✅ NOT triggered (R3.5 structural content now formally verified in Lean as of session 002).
- Phase 1 fails at milestone 4.1 (no consistent F-F definition): ✅ NOT triggered (three candidates produced; A=B, C strict refinement; all three pass K2).
- Phase 1 fails at Lambda-Blpr fiber products (milestone 4.5): NOT YET TESTED.
- Phase 2 fails at prismatic foliation hypothesis: NOT YET TESTED.
- Phase 3 fails at intersection product: NOT YET TESTED.
- Phase 4 fails after 5 calendar years of parallel Hodge index attempts: NOT YET TESTED.

## Pending agent outputs

Session 002 outputs landed: three F-F candidates ([A](experiments/arithmetic_geometric/D1_4_1_fermat_frobenius_candidate_A.md), [B](experiments/arithmetic_geometric/D1_4_1_fermat_frobenius_candidate_B.md), [C](experiments/arithmetic_geometric/D1_4_1_fermat_frobenius_candidate_C.md)) plus R3.5 verification ([diagnostic](experiments/orchestrator_sessions/r3_5_verification_attempt.md), [updated Lean](lean/ZetaRH/R3_5.lean)). Awaiting session 003 deployments: VERIFIER-1A/B/C on the F-F candidates' Lean targets, plus ADVERSARY on D-H exclusion across all three.

## Last verified state

- Git commit: `8a6c3d7` (Lean Phase 1 substrate green build).
- LEARNINGS.md last finding: #15 (4E.8 polynomial-ideal SOS). Session 002 adds #16 (F-F triality A=B<C) and #17 (Weil explicit formula as highest-leverage Mathlib gap).
- Plan status table: current through Arch 4E.8, 2C, 2D, R3.6.3, 3B.3.
- Lean: `lake build` green on Lean 4.13.0 + Mathlib v4.13.0; R3.5 sorry eliminated in session 002; remaining sorries are documented VERIFIER targets.

## Session log (recent)

| Date | Session focus | Commits | Key outputs |
|---|---|---|---|
| 2026-05-25 | Session 002: three BUILDERs on milestone 4.1 + VERIFIER on R3.5 | TBD | Three F-F candidates (A blueprint-relation, B Adams quotient, C delta-ring); R3.5 structural content proved by `rfl` after refactor into TraceFormulaNCG framework; build green; one sorry eliminated; LEARNINGS #16 (A=B<C triality) and #17 (Weil explicit formula gap) added |
| 2026-05-25 | Lean Phase 1 substrate + green build | `8a6c3d7` | Six modules upgraded from True/Unit placeholders to typed Mathlib-wired data; MathlibBridge.lean added; 14 VERIFIER target IDs tabulated; lake build green (Lean 4.13.0 + Mathlib v4.13.0) |
| 2026-05-25 | Arch 4E.8 SOS-SDP | `565de36` | Closes LP/SDP family escape from 4E.3 |
| 2026-05-25 | Arch 2C F_1/Arakelov survey | `fd020fc` | 280-line landscape survey |
| 2026-05-25 | Plan Why-section expansion | `a28f106` | Operational framing of project |
| 2026-05-25 | Arch 2D Deninger micro-target | `10c9f05` | M3 prismatic foliation hypothesis identified |
| 2026-05-25 | Arch 2A R3.6.3 CC infrastructure | `3a3f4e3` | Connes-Consani as geometric route infrastructure |
| 2026-05-25 | Arch 3B.3 rigorous Li witness | `30d32aa` | n = 336,000 first rigorous negativity |
| 2026-05-25 | Proof program + 8 directions | `d8a0193` | Operational + research-grade plans |
| 2026-05-25 | AI-centric plan + program | `f951298` | AI division of labor documented |
| 2026-05-25 | AI-only variant | `1928c08` | Speculative AI-only execution variant |
| 2026-05-25 | Agent substrate (pending) | TBD | This commit |

## How to update this file

- ORCHESTRATOR: update "Recommended next session actions" at session end.
- SYNTHESIZER: update everything else after agent outputs land.
- Always update "Last verified state" with the latest commit hash.
- Always update "Session log" with the latest session's work.
