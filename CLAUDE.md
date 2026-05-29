# CLAUDE.md

Project-specific instructions for Claude Code. Read on every session start. This file is the merged successor of the former `LLM_ONBOARDING.md`: it carries both the project's technical context (architectures, conventions, LFunction interface) and the human-side context (owner, tech stack, agent infrastructure).

## What this repo is

A research-and-study project on the Riemann Hypothesis. It contains:
- Layered docs (intuitive, undergraduate, graduate, research) on $\zeta$ and the RH
- A strategic landscape document (`docs/research_atlas/`) cataloging every known proof approach with its obstructions
- A computational experimental thread (`experiments/`) organized around testing the four candidate RH proof architectures
- A Lean 4 / Mathlib formalization skeleton (`lean/`) wired to Mathlib's `riemannZeta`

It is **not** a tool or product. It is a research codebase. Output is markdown documents, numerical experiments, visualizations, and Lean proofs.

## Stance (read this before writing any framing)

The posture of this project is that we are trying to solve RH. It is hard and the odds are long, but it is a target, not a monument, and nothing here should be written as if the problem were impossible.

When you document a negative result, frame it as progress. A method that fails (Level 3 statistics, the analytic $2/3$ ceiling, the K1 wall, soft positivity's zero margin) has removed a dead branch and sharpened where the real proof must live. Each "this won't work" is a coordinate that narrows the search.

Specifically, avoid fatalistic phrasing ("stuck," "hopeless," "can never," "no buffer for soft proofs" used as a verdict on the problem). Prefer the directional reading: the marginal-positivity finding is a **compass** that says the proof must engage the exact structure of $\zeta$, not a wall. Keep the math exactly as rigorous as it is (a provably false lemma is still false, a saturated ceiling is still saturated). Change the tone, not the theorems.

## About the owner

The owner is Owen, a wheelchair user with muscular dystrophy.

- **Typing is hard.** Be proactive. Make decisions. Don't ask for confirmation on small things.
- **Offer A/B/C choices** when input is needed. One letter is faster than a sentence.
- **PowerShell on Windows.** Use PowerShell syntax. Prefer single-line commands.
- **Accessibility matters.** Many of Owen's projects are tools he actually uses.

## START HERE

- **Research strategy**: [`docs/research_atlas/README.md`](docs/research_atlas/README.md). Comprehensive catalog of all approaches, what failed, what's missing.
- **Experiments**: [`experiments/PROOF_ARCHITECTURES_PLAN.md`](experiments/PROOF_ARCHITECTURES_PLAN.md). The test plan with current status per architecture.
- **Proof program work**: [`PHASE_STATE.md`](PHASE_STATE.md) (current operational state), [`OPERATIONS.md`](OPERATIONS.md) (how to drive the agent loop), [`docs/03_research/proof_program.md`](docs/03_research/proof_program.md) (AI-augmented + human-led plan), [`docs/03_research/proof_program_ai_only.md`](docs/03_research/proof_program_ai_only.md) (speculative AI-only variant).
- **Multi-agent session continuity**: [`experiments/orchestrator_sessions/`](experiments/orchestrator_sessions/). Read the highest-numbered file for the last ORCHESTRATOR's plan.
- **Lean 4 substrate**: [`lean/README.md`](lean/README.md). Phase 1 typed substrate landed 2026-05-25 with a VERIFIER target ID table.

## Core conceptual framework

The project is organized around **four candidate proof architectures** (from `docs/solutions/README.md` §8 and `experiments/PROOF_ARCHITECTURES_PLAN.md`):

1. **Spectral** (Hilbert-Pólya): self-adjoint operator whose eigenvalues are the imaginary parts of zeta zeros
2. **Arithmetic-geometric** (Deninger / $\mathbb{F}_1$): cohomology theory for $\mathrm{Spec}(\mathbb{Z})$ that lifts Weil's curves-over-$\mathbb{F}_q$ proof
3. **Direct positivity** (Weil / Li): $\lambda_n \geq 0$ for all $n$, or $\sum_\rho \hat f(\rho)\overline{\hat f(\bar\rho)} \geq 0$ on Schwartz $f$
4. **Analytic** (zero-free regions): push the Vinogradov-Korobov exponent $2/3 \to 1/2$

The four-level framing (`docs/02_graduate/log_correlated_fields_intro.md` §6) places RH at Level 4 (positivity), not Level 3 (spectral/statistical). This is the project's structural commitment, and it is a targeting tool rather than a discouragement: a method that lives only at Level 3 (Selberg CLT, GUE statistics, multifractal log-correlated structure) cannot by itself close RH, because those statements are compatible with worlds where some zero has $\beta = 0.51$. Knowing that tells us where the proof must live (Level 4), so we spend effort there instead of polishing Level 3. Ruling a level out is how the search narrows.

## The Davenport-Heilbronn discipline

The **Davenport-Heilbronn L-function** (functional equation but no Euler product; known off-line zeros at $\rho \approx 0.808 + 85.7i$) is the project's **wrong-approach detector**. Any method in Architectures 1, 3, or 4 that does not distinguish zeta from D-H is structurally wrong: D-H is a known counterexample to its own analogue of RH, so any RH-style proof that "works" for D-H is incorrect.

Implementation: `experiments/_shared/davenport_heilbronn.py`. Run `python -m experiments._shared.smoke_test` to verify the control is working (5/5 tests including a regression check on the first off-line zero location).

Architecture 2 sits outside this discipline because Deninger-style constructions intentionally require the Euler product that D-H lacks.

## Repository structure

```
zeta-function/
├── docs/
│   ├── 00_intuitive/            intuitive-level explanations
│   ├── 01_undergraduate/        undergrad-level explanations
│   ├── 02_graduate/             graduate-level (log-correlated fields, four-level RH framing)
│   ├── 03_research/             research-level overviews; proof programs; eight directions
│   ├── implications/            why RH matters
│   ├── solutions/               known proof attempts/approaches
│   └── research_atlas/          master research map; all approaches, failures, ML directions
├── experiments/
│   ├── PROOF_ARCHITECTURES_PLAN.md  the test plan with per-architecture status
│   ├── LEARNINGS.md             cross-cutting findings synthesis (15+ entries)
│   ├── _shared/                 LFunction interface, zeta, Davenport-Heilbronn control
│   ├── positivity/              Arch 3 (Li coefficients, Weil quadratic form, Gram-matrix detector)
│   ├── spectral/                Arch 1 (Berry-Keating, Sierra-Townsend, 1D Connes adèle literature)
│   ├── zero_free/               Arch 4 (non-negative trig polynomial LP/SDP family, MT translation)
│   ├── arithmetic_geometric/    Arch 2 (worked Weil example over F_5; 2A R1-R5 follow-ups; dossiers)
│   ├── multifractal/            log-correlated field experiments (E0-E3)
│   └── orchestrator_sessions/   per-session ORCHESTRATOR plans
├── lean/                        Lean 4 / Mathlib formal verification (Phase 1 substrate as of 2026-05-25)
│   ├── ZetaRH.lean
│   └── ZetaRH/{Basic,MathlibBridge,DavenportHeilbronn,KillCriteria,R3_5,
│                LineRestriction,LambdaBlueprints,PrismaticCohomology,
│                PrismaticFoliation,HodgeIndex}.lean
├── .claude/agents/              Six agent role specs (surveyor/builder/verifier/adversary/synthesizer/orchestrator)
├── sources/                     source PDFs (Riemann, Wilkins translation, etc.)
├── visualizations/              manim scenes
├── CLAUDE.md                    this file
├── README.md                    project overview, status, structure map
├── TODO.md                      task tracking (- [ ] checkbox format)
├── OPERATIONS.md                how to operate this repo as the AI-only proof program substrate
└── PHASE_STATE.md               current phase, sub-task, falsifiability triggers, next-session plan
```

## Key files

| File | Purpose |
|------|---------|
| `CLAUDE.md` | This file: technical + human-side context combined |
| `README.md` | Project overview, status, structure map |
| `TODO.md` | Task tracking (`- [ ]` checkbox format) |
| `OPERATIONS.md` | How to operate this repo as the AI-only proof program substrate |
| `PHASE_STATE.md` | Current phase, sub-task, falsifiability triggers, next-session plan |
| `docs/research_atlas/` | Master research map; all approaches, failures, ML directions |
| `docs/03_research/proof_program.md` | The AI-augmented operational proof program |
| `docs/03_research/proof_program_ai_only.md` | Speculative AI-only execution variant |
| `docs/03_research/research_directions/` | Eight research-grade directions with operational specs |
| `experiments/PROOF_ARCHITECTURES_PLAN.md` | The test plan with current status per architecture |
| `experiments/LEARNINGS.md` | 15+ cross-architecture findings (the synthesis surface) |
| `experiments/orchestrator_sessions/` | Per-session ORCHESTRATOR plans (read highest-numbered first) |
| `lean/` | Lean 4 / Mathlib formal verification (Phase 1 substrate landed 2026-05-25) |
| `lean/README.md` | VERIFIER target ID table for the Lean substrate |
| `.claude/agents/` | Six agent role specs |
| `sources/` | Source PDFs and their text conversions |
| `visualizations/` | manim animation scripts |

## Tech stack

- **Language**: Python (primary). Lean 4 (formal verification).
- **Python libraries**: `mpmath` (high-precision arithmetic), `numpy`, `scipy`, `cvxpy` (LP/SDP optimization with CLARABEL/SCS solvers), `sympy`, `matplotlib`.
- **Visualization**: manim (3Blue1Brown style). `pip install manim`.
- **Formal verification**: Lean 4 + Mathlib (`lean/` directory, requires `elan` to build).
- **Docs**: Markdown with LaTeX math (`$...$` inline, `$$...$$` block in files; plain Unicode in chat).

## Conventions

- **High-precision arithmetic**: `mpmath` at ≥30 digits for zeros and L-function evaluation. `numpy` for downstream array work after conversion.
- **Data format**: experiments save `.npz` (numpy compressed) alongside the script. Plots save as `.png`. Both are gitignored under `experiments/**/_cache/` and `experiments/**/*.png`, but tracked .npz files live next to scripts.
- **Caching**: zero computations are slow (`mp.zetazero` for high index, D-H 2D scan). Each L-function caches per (T_max, prec) tuple under `experiments/_shared/_cache/`.
- **LFunction interface**: all L-functions implement `evaluate(s)` and `zeros(T_max, prec)`. Used uniformly across architectures so the same experiment can run on zeta and D-H with identical code.

## Style

- **No em dashes** anywhere. (Global preference. Use periods, colons, parentheses, or hyphens instead.) Don't add em dashes, don't use them at all, anywhere, ever. Rewrite the sentence instead.
- Inline math in markdown uses `$...$` for inline, `$$...$$` for display. KaTeX renders most things in the docs surface.
- In chat output the KaTeX surface is not available; use Unicode and plain text for math.
- Code: explanatory module-level docstrings, minimal inline comments. Comments should explain WHY, not WHAT.

## Running things

```powershell
# Smoke test the shared infrastructure
python -m experiments._shared.smoke_test

# Run an experiment (each is a python module)
python -m experiments.positivity.e3c2_weil_gram
python -m experiments.spectral.e1a_berry_keating
python -m experiments.zero_free.e4b_nonneg_trig
python -m experiments.arithmetic_geometric.e2b_elliptic_curve_fp

# Build the Lean substrate (requires elan + lake)
cd lean; lake build

# Dependencies: see requirements.txt (numpy, scipy, mpmath, matplotlib, manim, sympy, cvxpy)
```

Working dir is the repo root. Scripts use `from experiments._shared import ...` style imports, which only resolve from the root.

## Git commits

```powershell
git add -A; git commit -m "docs: add intuitive explanation"; git push
```

Conventional commits: `feat:`, `fix:`, `docs:`, `refactor:`, `chore:`.

Never commit or push without per-action authorization (memory: `feedback_ask_before_push.md`).

## Agent infrastructure (AI-only proof program substrate)

This repo is structured as the operational substrate for an AI-only proof program. Six agent roles in `.claude/agents/`:

- **SURVEYOR**: literature synthesis + scorecard maintenance.
- **BUILDER**: propose mathematical constructions (definitions, candidate proofs).
- **VERIFIER**: translate to Lean 4 / Mathlib and verify.
- **ADVERSARY**: K1-K4 attack; D-H discipline; counterexample search.
- **SYNTHESIZER**: integrate verified outputs into the project dossier.
- **ORCHESTRATOR**: schedule work; manage compute budget; decide abandonment.

Deploy via the `Agent` tool with `subagent_type: <role>` (note: requires the role specs to be loaded in the session; currently invoked via `general-purpose` with the role spec passed as prompt).

See [`OPERATIONS.md`](OPERATIONS.md) for the full operational guide.

## Known landmarks

- First Davenport-Heilbronn off-line zero: $\rho \approx 0.8085 + 85.699\,i$ (and partner $0.1915 + 85.699\,i$ by functional-equation symmetry)
- Bombieri-Lagarias asymptotic for zeta Li coefficients: $\lambda_n \sim (n/2)\log n + cn$ with $c = (1 - \gamma_E - \log(2\pi))/2 \approx -0.708$
- Riemann-von Mangoldt density of zeta zeros at height $T$: $\rho_\zeta(T) = \log(T/(2\pi))/(2\pi)$
- The first ten zeta zeros at $\gamma \approx 14.13, 21.02, 25.01, 30.42, 32.94, 37.59, 40.92, 43.33, 48.01, 49.77$

## When in doubt

- The atlas (`docs/research_atlas/README.md`) is the master reference for what's been tried and what's stuck.
- The plan (`experiments/PROOF_ARCHITECTURES_PLAN.md`) is the master reference for the experimental thread.
- The Davenport-Heilbronn discipline is the project's structural sanity check.
- If a proposed method does not engage with the four-level framing, it is probably Level 3 and not RH-closing.

## Constellation

This repo is tracked by Constellation. It has `README.md` with `## Status` and `TODO.md` with checkboxes.
