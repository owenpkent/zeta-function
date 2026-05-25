# LLM Onboarding

Quick reference for AI assistants working on this repository.

> **For project-specific technical context** (the four proof architectures, the Davenport-Heilbronn discipline, file-naming conventions, the LFunction interface, math style), see [`CLAUDE.md`](CLAUDE.md). This file focuses on the human-side context: about the owner, tech stack, and conventions.

---

## Project Overview

**Name:** Riemann Zeta Function — Deep Study Repo
**Purpose:** Multi-level exploration of the Riemann zeta function and Riemann Hypothesis, from intuitive to research-level, with manim visualizations and a computational experimental thread organized around testing the four candidate RH proof architectures.

**START HERE for research strategy:** [`docs/research_atlas/README.md`](docs/research_atlas/README.md) — comprehensive catalog of all approaches, what failed, what's missing, with a companion section pointing to the experiments.

**START HERE for experiments:** [`experiments/PROOF_ARCHITECTURES_PLAN.md`](experiments/PROOF_ARCHITECTURES_PLAN.md) — the test plan with current status per architecture, AI-centric methodology.

**START HERE for proof program work:** [`PHASE_STATE.md`](PHASE_STATE.md) (current operational state) + [`OPERATIONS.md`](OPERATIONS.md) (how to drive the agent loop) + [`docs/03_research/proof_program.md`](docs/03_research/proof_program.md) (AI-augmented + human-led plan) + [`docs/03_research/proof_program_ai_only.md`](docs/03_research/proof_program_ai_only.md) (speculative AI-only variant).

**START HERE if continuing a multi-agent session:** [`experiments/orchestrator_sessions/`](experiments/orchestrator_sessions/) — last ORCHESTRATOR's plan for the next session. Read the highest-numbered file.

## About the Owner

I'm Owen — a wheelchair user with muscular dystrophy.

- **Typing is hard** — Be proactive. Make decisions. Don't ask for confirmation on small things.
- **Offer A/B/C choices** — I can type one letter instead of explaining.
- **PowerShell on Windows** — Use PowerShell syntax. Prefer single-line commands.
- **Accessibility matters** — Many of my projects are tools I actually need.

---

## Key Files

| File | Purpose |
|------|---------|
| `CLAUDE.md` | Project technical context (architectures, conventions, LFunction interface) |
| `README.md` | Project overview, status, structure map |
| `TODO.md` | Task tracking (`- [ ]` checkbox format) |
| `OPERATIONS.md` | How to operate this repo as the AI-only proof program substrate |
| `PHASE_STATE.md` | Current phase, sub-task, falsifiability triggers, next-session plan |
| `docs/` | All written explanations by level |
| `docs/research_atlas/` | Master research map; all approaches, failures, ML directions |
| `docs/03_research/proof_program.md` | The AI-augmented operational proof program |
| `docs/03_research/proof_program_ai_only.md` | Speculative AI-only execution variant |
| `docs/03_research/research_directions/` | Eight research-grade directions with operational specs |
| `experiments/` | Computational experimental thread (four proof architectures) |
| `experiments/PROOF_ARCHITECTURES_PLAN.md` | The test plan with current status per architecture |
| `experiments/LEARNINGS.md` | 15+ cross-architecture findings (the synthesis surface) |
| `experiments/orchestrator_sessions/` | Per-session ORCHESTRATOR plans (read highest-numbered first) |
| `lean/` | Lean 4 / Mathlib formal verification skeleton |
| `lean/smoke_test.sh` | Quick check that Lean builds (run once after edits) |
| `.claude/agents/` | Six agent role specs: surveyor / builder / verifier / adversary / synthesizer / orchestrator |
| `sources/` | Source PDFs and their text conversions |
| `visualizations/` | manim animation scripts |
| `LLM_ONBOARDING.md` | This file |

---

## Repo Structure

```
zeta-function/
├── docs/
│   ├── 00_intuitive/            # No math required
│   ├── 01_undergraduate/        # Calculus + complex numbers
│   ├── 02_graduate/             # Complex analysis, log-correlated fields, four-level RH framing
│   ├── 03_research/             # Frontier approaches, extreme values
│   ├── implications/            # Why RH matters
│   ├── solutions/               # Known proof attempts/approaches
│   └── research_atlas/          # Master research map
├── experiments/
│   ├── PROOF_ARCHITECTURES_PLAN.md
│   ├── _shared/                 # LFunction interface, zeta, Davenport-Heilbronn control
│   ├── positivity/              # Arch 3 (Li coefficients, Weil quadratic form, Gram-matrix detector at K=1000 and T_max=500, 3E Li/dBN literature)
│   ├── spectral/                # Arch 1 (Berry-Keating discretization, Sierra-Townsend variants, 1D Connes adèle literature)
│   ├── zero_free/               # Arch 4 (non-negative trig polynomial LP, multivariate balanced-sum LPs up to d=4, MT translation, constrained-domain LP, multi-zero LP, 4A+4C V-K + conditional-landscape literature)
│   ├── arithmetic_geometric/    # Arch 2 (worked Weil example over F_5; 2A evaluation framework with R1-R5 follow-ups, hybrid proposals; 2E Adams-spectrum probe; 5/6 candidate dossiers: Borger, Lorscheid, Connes, Deninger, Deitmar)
│   ├── multifractal/            # Log-correlated field experiments (pre-existing)
│   ├── LEARNINGS.md             # Cross-cutting findings synthesis
│   └── PROOF_ARCHITECTURES_PLAN.md  # Test plan and per-experiment status
├── sources/                     # Source PDFs and text conversions
├── visualizations/              # manim scenes
│   ├── 01_series_intro/
│   ├── 02_complex_plane/
│   └── ...
├── CLAUDE.md
├── README.md
├── TODO.md
└── LLM_ONBOARDING.md
```

---

## Tech Stack

- **Language:** Python (primary). Lean 4 (formal verification).
- **Python libraries:** `mpmath` (high-precision arithmetic), `numpy`, `scipy`, `cvxpy` (LP/SDP optimization with CLARABEL/SCS solvers), `sympy`, `matplotlib`.
- **Visualization:** manim (3Blue1Brown) — `pip install manim`.
- **Formal verification:** Lean 4 + Mathlib (`lean/` directory, requires `elan` to build).
- **Docs:** Markdown with LaTeX math (`$...$` inline, `$$...$$` block in files; plain Unicode in chat).

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

## Math Notation

Use standard LaTeX in Markdown:
- Inline: `$\zeta(s)$`
- Block: `$$\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s}$$`

---

## Git Commits

```powershell
git add -A; git commit -m "docs: add intuitive explanation"; git push
```

Conventional commits: `feat:`, `fix:`, `docs:`, `refactor:`, `chore:`

---

## Constellation

This repo is tracked by Constellation. It has `README.md` with `## Status` and `TODO.md` with checkboxes.
