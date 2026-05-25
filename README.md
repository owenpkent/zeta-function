# Riemann Zeta Function — Deep Study Repo

A multi-level exploration of the Riemann Zeta Function and the Riemann Hypothesis: from intuitive visual understanding through graduate-level analysis to the frontier of current research. Includes a computational experimental thread organized around testing the four candidate RH proof architectures.

**Operational substrate**: this repo is also structured as the substrate for an AI-augmented (and, speculatively, AI-only) proof program for RH. See [`OPERATIONS.md`](OPERATIONS.md) for how to operate it, [`PHASE_STATE.md`](PHASE_STATE.md) for current state, [`docs/03_research/proof_program.md`](docs/03_research/proof_program.md) for the AI-augmented plan, and [`docs/03_research/proof_program_ai_only.md`](docs/03_research/proof_program_ai_only.md) for the AI-only speculative variant. The repo is a handoff artifact: ~50-70% of Phase 0 is done; Phases 1-5 require expert collaborators and multi-year compute.

## What's Here

This repo is structured so you can enter at any level and go as deep as you want.

```
zeta-function/
├── docs/                        # All written explanations
│   ├── 00_intuitive/            # No math required: visual, conceptual
│   ├── 01_undergraduate/        # Calculus, complex numbers, series
│   ├── 02_graduate/             # Analytic continuation, functional equation,
│   │                            #   log-correlated fields, four-level RH framing
│   ├── 03_research/             # Current approaches, extreme values, PROOF PROGRAMS
│   │   ├── proof_program.md     # ★ AI-augmented (human-led) proof program
│   │   ├── proof_program_ai_only.md  # ★ AI-only speculative variant
│   │   └── research_directions/ # ★ 8 research-grade directions with operational specs
│   ├── implications/            # Why it matters (primes, physics, crypto)
│   ├── solutions/               # Known approaches to the Riemann Hypothesis
│   └── research_atlas/          # Master research map: all attempts, failures, ML directions
├── experiments/                 # ★ Computational thread; proof-architecture tests
│   ├── PROOF_ARCHITECTURES_PLAN.md    # Test plan + AI-centric methodology
│   ├── LEARNINGS.md             # 15+ cross-architecture findings
│   ├── _shared/                 # LFunction interface, zeta, Davenport-Heilbronn control
│   ├── positivity/              # Arch 3 (Li coefficients, Weil quadratic form, 3B.3 rigorous)
│   ├── spectral/                # Arch 1 (Berry-Keating discretization)
│   ├── zero_free/               # Arch 4 (LP/SDP family through 4E.8)
│   ├── arithmetic_geometric/    # Arch 2 (2A diff, R1-R5, R3.6, R3.6.3, 2C, 2D, 2E)
│   └── multifractal/            # Log-correlated field experiments (pre-existing)
├── lean/                        # ★ Lean 4 / Mathlib formal verification (skeleton)
│   ├── lakefile.lean
│   ├── ZetaRH.lean              # Main module
│   └── ZetaRH/                  # R3.5, LineRestriction, LambdaBlueprints, HodgeIndex, ...
├── .claude/agents/              # ★ AI agent role specifications for AI-only execution
│   ├── surveyor.md              # Literature survey + scorecard maintenance
│   ├── builder.md               # Propose constructions
│   ├── verifier.md              # Formalize in Lean 4
│   ├── adversary.md             # K1-K4 attack; D-H discipline
│   ├── synthesizer.md           # Integrate outputs into project dossier
│   └── orchestrator.md          # Schedule work, manage compute budget
├── sources/                     # Original PDFs and their converted text
├── visualizations/              # manim animation scripts
├── OPERATIONS.md                # ★ How to operate this repo as the proof-program substrate
├── PHASE_STATE.md               # ★ Current operational state (read by ORCHESTRATOR)
└── CLAUDE.md                    # Project + owner context for AI assistants (merged successor of LLM_ONBOARDING.md)
```

## The Question

The **Riemann Hypothesis** states:

> All non-trivial zeros of the Riemann zeta function have real part equal to 1/2.

It has been open since 1859. It is one of the Millennium Prize Problems (worth $1,000,000). It governs the distribution of prime numbers, and its implications ripple through number theory, physics, cryptography, and beyond.

## Levels

| Level | Folder | Prerequisites |
|-------|--------|---------------|
| Intuitive | `docs/00_intuitive/` | None — curiosity only |
| Undergraduate | `docs/01_undergraduate/` | Calculus, basic complex numbers |
| Graduate | `docs/02_graduate/` | Complex analysis, real analysis |
| Research | `docs/03_research/` | Graduate mathematics |
| **Research Atlas** | `docs/research_atlas/` | **Start here for ML research** — full catalog of approaches, failures, obstructions, and ML directions |

## Visualizations (manim)

Built with [manim](https://github.com/3b1b/manim) (3Blue1Brown's animation engine).

See `visualizations/README.md` for setup and how to render each scene.

## Source PDFs

Original source PDFs and their converted text versions live in `sources/`.

## Experimental thread

See [`experiments/PROOF_ARCHITECTURES_PLAN.md`](experiments/PROOF_ARCHITECTURES_PLAN.md) for the test plan. Four candidate RH proof architectures (spectral, arithmetic-geometric, direct positivity, analytic) with the Davenport-Heilbronn L-function as a structural wrong-approach detector throughout. ~25 experiments + literature reviews implemented across the four architectures, plus full dossier coverage for 5 of 6 major Arch 2 candidates (Borger, Lorscheid, Connes, Deninger, Deitmar). Arch 3 (positivity) has the deepest experimental thread, including a Gram-matrix wrong-approach detector validated at four T_max values (`n_neg` exactly equals number of off-line zero pairs in upper half plane at T_max ∈ {200, 300, 350, 500}).

Smoke test:
```powershell
python -m experiments._shared.smoke_test
```

## Cross-cutting findings

Synthesis of structural insights across architectures lives in [`experiments/LEARNINGS.md`](experiments/LEARNINGS.md). The dominant meta-finding from the experimental thread: **RH is marginally true** — every positivity reformulation (Weil-form, Li, de Bruijn-Newman, MT shape factor) is sharp at zero margin. Five independent reinforcing directions (LEARNINGS findings #7, #11, #12, #13 + Arch 3E literature review) all confirm there is no buffer for soft proofs. Any RH proof must use the EXACT structure of $\zeta$ (Euler product, functional equation, archimedean factor) rather than generic positivity arguments.

The 17-constraint framework for Architecture 2 candidates (see [`experiments/arithmetic_geometric/2A_candidate_evaluation.md`](experiments/arithmetic_geometric/2A_candidate_evaluation.md)) operationalizes the comparison of $\mathbb{F}_1$ programs and identifies the geometric route (intersection theory + Hodge index theorem on a constructed surface) as the unique remaining direction for breaking the K1 wall on positivity. The path forward strategic synthesis is in [`experiments/arithmetic_geometric/2A_path_forward.md`](experiments/arithmetic_geometric/2A_path_forward.md).

## Status

| Area | Status |
|------|--------|
| Repo structure | ✅ Complete |
| Solutions / approach catalog | ✅ `docs/solutions/` |
| Research atlas | ✅ `docs/research_atlas/` |
| Graduate docs (incl. log-correlated, four-level framing) | ✅ Substantial |
| Experiments — Phase 0 infrastructure | ✅ Complete |
| Experiments — Arch 3 (positivity) | ✅ 3A-3D, 3B.2, 3D.2-3D.4, 3E (literature), 3F-3I, 3J (Schur complement against on-line cushion gives ~30x sharper detector than raw spectrum, rel min asymptote -78.7%), 3K (hypothetical off-line zero perturbation, disproof path closed in Gram-matrix family) complete |
| Experiments — Arch 1 (spectral) | ✅ 1A, 1B, 1C, 1D complete (1D as literature review of Connes adèle class space) |
| Experiments — Arch 4 (zero-free regions) | ✅ 4B, 4D, 4D.2, 4E, 4E.2-4E.7 complete (4E.6: MT 1D-Fejér ceiling robust under domain relaxation; 4E.7: multi-zero LP gives 55-137× shape-factor improvement but rank-1 LP optima at naive objectives); 4A+4C complete as unified literature dossier (V-K $2/3$ exponent is a structural ceiling after BDG 2016; no named conditional pushes the exponent; Arch 4 is constraint-mapping, not a route to RH); 4E.8 pending (SOS via Putinar/Schmüdgen) |
| Experiments — Arch 2 (arithmetic-geometric) | ✅ 2A, 2B, 2E complete (2A includes R1-R5 evaluation framework with hybrid proposals AND 5 of 6 candidate dossiers: Borger, Lorscheid, Connes, Deninger, Deitmar; 2E confirms bare $\psi_p$ on concrete Λ-rings has no zeta-zero-like spectrum, validating R5's cohomology-must-lift framing); 2C, 2D pending |
| Intuitive / undergraduate docs | 🔄 In progress |
| PDF text conversions | 🔄 In progress |
| manim visualizations | 🔄 In progress |

## Quick Start

```powershell
# Set up environment
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Smoke test the experimental framework
python -m experiments._shared.smoke_test

# manim scene
manim -pql visualizations/01_series_intro/series_intro.py ZetaSeriesIntro
```
