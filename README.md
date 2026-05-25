# Riemann Zeta Function — Deep Study Repo

A multi-level exploration of the Riemann Zeta Function and the Riemann Hypothesis: from intuitive visual understanding through graduate-level analysis to the frontier of current research. Includes a computational experimental thread organized around testing the four candidate RH proof architectures.

## What's Here

This repo is structured so you can enter at any level and go as deep as you want.

```
zeta-function/
├── docs/                        # All written explanations
│   ├── 00_intuitive/            # No math required — visual, conceptual
│   ├── 01_undergraduate/        # Calculus, complex numbers, series
│   ├── 02_graduate/             # Analytic continuation, functional equation,
│   │                            #   log-correlated fields, four-level RH framing
│   ├── 03_research/             # Current approaches, extreme values
│   ├── implications/            # Why it matters (primes, physics, crypto)
│   ├── solutions/               # Known approaches to the Riemann Hypothesis
│   └── research_atlas/          # ★ Master research map — all attempts, failures, ML directions
├── experiments/                 # ★ Computational thread; proof-architecture tests
│   ├── PROOF_ARCHITECTURES_PLAN.md
│   ├── _shared/                 # LFunction interface, zeta, Davenport-Heilbronn control
│   ├── positivity/              # Arch 3 (Li coefficients, Weil quadratic form)
│   ├── spectral/                # Arch 1 (Berry-Keating discretization)
│   ├── zero_free/               # Arch 4 (non-negative trig polynomial LP)
│   ├── arithmetic_geometric/    # Arch 2 (worked Weil-curves example over F_5)
│   └── multifractal/            # Log-correlated field experiments (pre-existing)
├── sources/                     # Original PDFs and their converted text
├── visualizations/              # manim animation scripts
├── CLAUDE.md                    # Project context for AI assistants
└── LLM_ONBOARDING.md            # User context + tech stack
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
| Experiments — Arch 3 (positivity) | ✅ 3A-3D, 3B.2, 3D.2-3D.4, 3E (literature), 3F-3I complete |
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
