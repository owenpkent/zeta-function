# Operations Guide: AI-Only Execution of the RH Proof Program

> How to run this repo as the operational substrate for the AI-only proof program described in [`docs/03_research/proof_program_ai_only.md`](docs/03_research/proof_program_ai_only.md). For the AI-augmented variant (with human in the critical path), see [`docs/03_research/proof_program.md`](docs/03_research/proof_program.md) instead.
>
> **Scope of this guide**: how to launch sessions, deploy agents, maintain state, escalate to human review. Not the mathematical content (that lives in `experiments/`, `docs/03_research/`, `lean/`).

## 1. The repo as substrate

This repository is structured as the operational substrate for AI-only execution:

| Component | Path | Role |
|---|---|---|
| Agent role specifications | [`.claude/agents/`](.claude/agents/) | Six specialized agents: surveyor, builder, verifier, adversary, synthesizer, orchestrator. Each is a subagent that can be deployed via the `Agent` tool. |
| Phase state | [`PHASE_STATE.md`](PHASE_STATE.md) | Current phase, current sub-task, last verification, next steps. Read by ORCHESTRATOR at start of every session. |
| Project narrative | [`experiments/LEARNINGS.md`](experiments/LEARNINGS.md) | 15+ cross-architecture findings. Updated by SYNTHESIZER. |
| Status table | [`experiments/PROOF_ARCHITECTURES_PLAN.md`](experiments/PROOF_ARCHITECTURES_PLAN.md) | Per-experiment status. Updated as work lands. |
| Scorecards | [`experiments/arithmetic_geometric/2A_*.md`](experiments/arithmetic_geometric/) | Per-candidate evaluations against 17-constraint framework. |
| Strategic plans | [`docs/03_research/proof_program*.md`](docs/03_research/) | AI-augmented and AI-only operational programs. |
| Eight research directions | [`docs/03_research/research_directions/`](docs/03_research/research_directions/) | Per-direction execution roadmaps. |
| Formal verification | [`lean/`](lean/) | Lean 4 / Mathlib project. Every structural claim verified here is canonical. |
| Persistent memory | [`memory/MEMORY.md`](memory/) | Cross-session context. Read at session start. |

## 2. The session loop

Each AI-only session follows this pattern:

### 2.1 Session start

1. ORCHESTRATOR reads [`PHASE_STATE.md`](PHASE_STATE.md) and [`experiments/LEARNINGS.md`](experiments/LEARNINGS.md).
2. ORCHESTRATOR decides session goal based on prior session's recommended next steps.
3. ORCHESTRATOR deploys agents via the `Agent` tool with `subagent_type` matching the role (e.g., `subagent_type: surveyor`).

### 2.2 Agent deployment (parallel where possible)

For mapping work (Phase 0, 1, 2):
- Deploy 1-3 SURVEYORs on the relevant sub-corpus.
- Deploy 3-5 BUILDERs on the same research direction with different attack angles.
- Deploy 1-2 VERIFIERs to formalize BUILDER outputs.
- Deploy 1-2 ADVERSARYs to stress-test outputs.

For construction work (Phase 3, 4):
- Deploy 5-10 BUILDERs in parallel across the three attack angles.
- VERIFIER and ADVERSARY scale with BUILDER output.

The `Agent` tool in this Claude Code session supports multiple parallel agents via separate tool calls in a single message.

### 2.3 Synthesis

After agent outputs land:
- Deploy SYNTHESIZER to integrate the verified outputs.
- SYNTHESIZER updates [`experiments/LEARNINGS.md`](experiments/LEARNINGS.md), [`experiments/PROOF_ARCHITECTURES_PLAN.md`](experiments/PROOF_ARCHITECTURES_PLAN.md), scorecards, [`PHASE_STATE.md`](PHASE_STATE.md).

### 2.4 Session end

ORCHESTRATOR writes to [`PHASE_STATE.md`](PHASE_STATE.md):
- Current phase + sub-task.
- Sessions used / budgeted.
- Pending agent outputs.
- Recommended next agent deployments.
- Falsifiability triggers approaching or hit.

### 2.5 Commit

The session's work is committed to git with a clear message: "Phase X.Y: BUILDER outputs + VERIFIER results + ADVERSARY findings". Each commit is reproducible.

## 3. Scheduled / continuous execution

For multi-year compute, the session loop runs on a schedule:

### 3.1 Via Claude Code's `/loop` or `/schedule`

- `/loop`: AI self-paces iterations. Useful for tight feedback loops within a phase.
- `/schedule`: cron-driven scheduled agent runs. Useful for the multi-year program horizon.

Configuration: see Claude Code docs for the user-invocable `loop` and `schedule` skills.

### 3.2 Suggested cadence per phase

| Phase | Suggested cadence | Approximate sessions |
|---|---|---|
| 0 Foundation | Daily, 6-12 months | 200-400 |
| 1 Lambda-blueprints | Daily, 6-12 months | 200-400 |
| 2 Prismatic cohomology | Daily, 12-18 months | 400-600 |
| 3 Intersection theory | Daily, 12-24 months | 400-800 |
| 4 Hodge index | Daily across 10-100 parallel agents, 2-5 years | 1000-10000 |
| 5 Assembly | Daily, 3-6 months | 100-200 |
| 6 Verification | Continuous Mathlib build checks | 100+ |

Total: 2500-12000 sessions over 5-10 calendar years.

## 4. Verification stack

Every claim must pass through the four-layer verification stack before becoming canonical:

1. **Mechanical computation**: at least two independent code paths (`mpmath` + `sage`, or `cvxpy` + `scipy linprog`). Agreement required.
2. **Symbolic verification**: symbolic algebra (`sympy`) where applicable.
3. **Formal proof in Lean 4**: structural claims formalized in [`lean/ZetaRH/`](lean/ZetaRH/) and proved via Mathlib + automated proof search.
4. **Multi-agent consensus**: three independent VERIFIER runs produce the same conclusion.

A claim is canonical when ALL FOUR layers agree. Until then, the claim is provisional and marked as such in SYNTHESIZER's output.

## 5. Escalation to human review

Even in AI-only execution, certain decisions warrant human review (per [`proof_program_ai_only.md`](docs/03_research/proof_program_ai_only.md) §7):

- **A claimed proof of RH**: submit to human peer review before any public announcement. The verification stack catches errors but human judgment validates the choice of formalization.
- **A claimed disproof of RH**: even stronger requirement. Verify computational refutation against multiple independent code paths and human-checked numerics.
- **A discovery that the architectural picture is wrong**: e.g., a counterexample to R3.5. Surface to human review before pivoting.
- **A novel mathematical object requiring expert judgment**: e.g., a candidate foliated dynamical system X. Expert review of mathematical taste.

ORCHESTRATOR explicitly flags such situations and pauses pending human input.

## 6. Falsifiability triggers

Per [`proof_program_ai_only.md`](docs/03_research/proof_program_ai_only.md) §4, the program is ABANDONED (or fundamentally restructured) if:

- Phase 0 reveals R3.5 is too narrow (some NCG approach escapes K1).
- Phase 1 fails at Lambda-Blpr fiber products (no consistent definition).
- Phase 2 fails at the prismatic foliation hypothesis.
- Phase 3 fails at the intersection product.
- Phase 4 fails after 5 calendar years (~1000 focused sessions) of parallel Hodge index attempts.

ORCHESTRATOR tracks these triggers in [`PHASE_STATE.md`](PHASE_STATE.md) and proposes abandonment when any is hit.

## 7. Costs and prerequisites

To actually run this program:

| Resource | Estimated cost |
|---|---|
| Compute (multi-agent parallel for 5-10 years) | $10M-100M |
| Lean 4 / Mathlib expansion (5-10 person-years) | $1M-3M (can be 50-70% AI) |
| Orchestration software (1-2 years initial dev) | $0.5M-1M |
| Human oversight (part-time supervision) | $0.5M-2M/year |
| **Total upfront (years 0-2)**: | $20M-50M |
| **Total program cost**: | $50M-200M |

This is a major-mathematics research investment. Comparable to a large LHC experiment or a Decadal Survey priority project in astronomy.

## 8. Current state (as of 2026-05-25)

**Approximately 50-70% of Phase 0 complete** via AI-augmented (not AI-only) execution. The repo has:
- Six 2A candidate scorecards.
- All R-series structural analyses (R1, R2, R2.5, R3, R3.5, R3.6, R3.6.3, R4, R5).
- The 2A_path_forward synthesis.
- The 2C F_1/Arakelov survey.
- The 2D Deninger micro-target identification.
- 15 cross-architecture findings in LEARNINGS.md.
- 4E.8 closing the LP/SDP family.
- 3B.3 rigorous Li-negativity witness at n = 336,000.
- Documented 8 research directions.
- Documented AI-augmented + AI-only operational programs.
- This operations guide.
- Lean 4 Phase 1 substrate: typed Mathlib-wired definitions for LFunction, RH, D-H, bivariate cosine polynomials, Lambda-blueprints. `lake build` is green on Lean 4.13.0 + Mathlib v4.13.0. All remaining warnings are documented VERIFIER target IDs (see [`lean/README.md`](lean/README.md)).

**Not yet started in this repo**:
- Multi-agent orchestration software.
- Lean 4 Mathlib expansion beyond the Phase 1 substrate (proving the VERIFIER targets, contributing upstream definitions).
- Cron-driven scheduled execution.
- A serious 1000+ session compute budget.

To transition from AI-augmented (current state) to AI-only (target state), the prerequisites in §7 must be funded and built. As of 2026, this is a target design, not an operating program.

## 9. For someone picking up this repo

If you (a future Claude session, or a human, or a research group) want to operate this repo as the AI-only proof program substrate:

1. **Read** [`PHASE_STATE.md`](PHASE_STATE.md) for current state.
2. **Read** [`experiments/LEARNINGS.md`](experiments/LEARNINGS.md) for the cumulative narrative.
3. **Read** [`docs/03_research/proof_program_ai_only.md`](docs/03_research/proof_program_ai_only.md) for the strategic plan.
4. **Read** [`.claude/agents/orchestrator.md`](.claude/agents/orchestrator.md) for how to drive sessions.
5. **Run** one session of ORCHESTRATOR to plan the next phase of work.
6. **Deploy** the agents ORCHESTRATOR recommends, via the `Agent` tool with appropriate `subagent_type`.
7. **Commit** the session's work with a clear message.
8. **Update** PHASE_STATE.md for the next session.

This is iterative. The compounding effect across thousands of sessions is what produces the program output.

## 10. Cross-references

- [`docs/03_research/proof_program.md`](docs/03_research/proof_program.md): AI-augmented variant of the proof program.
- [`docs/03_research/proof_program_ai_only.md`](docs/03_research/proof_program_ai_only.md): AI-only variant.
- [`docs/03_research/research_directions/`](docs/03_research/research_directions/): eight research directions.
- [`experiments/PROOF_ARCHITECTURES_PLAN.md`](experiments/PROOF_ARCHITECTURES_PLAN.md): test plan.
- [`experiments/LEARNINGS.md`](experiments/LEARNINGS.md): cross-architecture findings.
- [`lean/README.md`](lean/README.md): Lean 4 formalization status.
- [`PHASE_STATE.md`](PHASE_STATE.md): current operational state.
