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

## Non-obvious rules (read before editing code)

Quick-reference for the gotchas that are easy to get wrong. The disciplines and interface each have a fuller section below.

- **Lean `sorry`s are intentional research skeletons** (HodgeIndex, PrismaticCohomology, LambdaBlueprints, and others), not build failures. Do not "fix" them by deleting the statement; a clean `lake build` still prints many `sorry`/deprecation warnings.
- **Imports resolve from the repo root only** (`from experiments._shared import ...`). Run everything as a module from root; never `cd` into a subdir to run a script.
- **Uniform LFunction interface.** Every L-function subclasses the ABC in `experiments/_shared/lfunction.py` and implements `evaluate(s)` and `zeros(T_max, prec=30)`, so the same experiment runs on zeta and on D-H with identical code. Keep this contract when adding L-functions.
- **Tests are standalone modules, not pytest.** Each `test_*.py` / `smoke_test.py` has a `main()` under `if __name__ == "__main__"` and prints `N/N passed` (e.g. `python -m experiments.lemma_db.test_oracle`, `python -m experiments.toy.test_toy`). When you add an experiment, add its checks in this pattern.
- **The D-H and Beurling disciplines below are hard structural gates**, not optional. A method that cannot separate zeta from those controls is wrong.
- **Never commit or push without per-action authorization** (memory: `feedback_ask_before_push.md`).

## START HERE

- **Mindset and philosophy**: [`docs/researcher_mindset.md`](docs/researcher_mindset.md). How this project works: the problem is a target not a monument, we advance a front, negative results are coordinates, honesty is the engine. Read this first; it defines what counts as progress.
- **Current spine**: [`docs/03_research/all_roads_to_the_signature.md`](docs/03_research/all_roads_to_the_signature.md) (all directions converge on one positivity) and [`docs/03_research/research_directions/08A_rosati_standard_conjecture.md`](docs/03_research/research_directions/08A_rosati_standard_conjecture.md) (RH = arithmetic Rosati positivity = the arithmetic Hodge standard conjecture, with the M1-M5 milestone ladder).
- **Spec(Z) cohomology landscape**: [`docs/03_research/spec_z_cohomology_landscape.md`](docs/03_research/spec_z_cohomology_landscape.md). The consolidating scorecard of every candidate cohomology for Spec(Z) (Deninger, Connes/Connes-Consani, prismatic/WCart, Hesselholt THH/TC, Arakelov/Faltings-Hriljac, F_1, AHK) against the one requirement that proves RH: an RH-equivalent polarization. Every candidate realizes zeta as a trace; none carries the polarization. That is the universal gap, and supplying it IS RH.
- **Research strategy**: [`docs/research_atlas/README.md`](docs/research_atlas/README.md). Comprehensive catalog of all approaches, what failed, what's missing.
- **Logical status of RH**: [`docs/03_research/rh_logical_status.md`](docs/03_research/rh_logical_status.md). RH is a $\Pi^0_1$ sentence, so undecidability is a back door to truth, not an escape (a proof of independence would itself prove RH true). Carries the adversarially-verified Gödel lever, the dead corners, the open-research map, and the Lean $\Pi^0_1$ kernel witness ([`lean/ZetaRH/RHEquivalences.lean`](lean/ZetaRH/RHEquivalences.lean)).
- **Experiments**: [`experiments/PROOF_ARCHITECTURES_PLAN.md`](experiments/PROOF_ARCHITECTURES_PLAN.md). The test plan with current status per architecture.
- **Proof program work**: [`PHASE_STATE.md`](PHASE_STATE.md) (current operational state), [`OPERATIONS.md`](OPERATIONS.md) (how to drive the agent loop), [`docs/03_research/proof_program.md`](docs/03_research/proof_program.md) (AI-augmented + human-led plan), [`docs/03_research/proof_program_ai_only.md`](docs/03_research/proof_program_ai_only.md) (speculative AI-only variant).
- **The math-iteration engines (capstone)**: [`docs/03_research/math_iteration_engines.md`](docs/03_research/math_iteration_engines.md). Synthesis of the "build our own algorithm for RH" arc: a complete generate-evaluate loop (Reduction Engine = evaluate, Generative Engine = generate) that mechanized the disciplines, regenerated the all-roads convergence, and handed back the sharpened M4 spec (the 7-property statement of the object that proves RH) plus the transfer shortlist (Hodge-Riemann / Alexandrov-Fenchel / Bost-Connes). Start here for the engine arc; it did not touch the blind spot, by design.
- **The Breadth Program (breadth as the AI edge)**: [`docs/03_research/breadth_program.md`](docs/03_research/breadth_program.md). The strategic program for turning mathematical breadth into an advantage on RH: not accumulation (survey-find-realization-CLOSE, done 12+ times) but transfer-and-compression, disciplined by a disqualifier battery. Strips M4 to a field-agnostic skeleton (S1-S7; polarity the master discriminator), with an executable corpus + skeleton query + disqualifier-complement aim ([`experiments/lemma_db/breadth_corpus.py`](experiments/lemma_db/breadth_corpus.py), 16/16 tests). Two aimed sweeps (LEARNINGS #119-#121) CONVERGED it: they produced a near necessary-and-sufficient FINGERPRINT of M4's polarity (contingent + complex-root + line-axis + output-indefinite-with-sign-flip + prohibitive-on-a-fixed-locus = a polarization) and ~13 reusable disqualifiers, then showed the fixed-indefinite-form space outside arithmetic geometry is mapped and insufficient. The honest caveat (#122): the fingerprint is genus-1-faithful and silent about where M4 is actually hard (higher-rank Rosati + the archimedean place + the global assembly). It compressed the problem; it did not touch P6.
- **The Reduction Engine (our own RH-solver algorithm)**: [`docs/03_research/reduction_engine.md`](docs/03_research/reduction_engine.md). Not a head-on attack: a problem-compression loop (reduction graph + falsification oracle) built on the lemma DB that compresses RH to its open kernel and reports the asserted-vs-proven gap. The proof program is the destination; the engine is the navigation. All five increments are built (`experiments/lemma_db/oracle.py`, `engine.py`, `lean_hook.py`, the value-function views); the four-bit "collision engine" was killed by its own adversary, the discrimination collapsing into the falsifier. It is the EVALUATE half of a math-iteration loop.
- **The Generative Engine (the generate half)**: [`docs/03_research/generative_engine.md`](docs/03_research/generative_engine.md). The organ that PROPOSES: a move-library + transfer-search (bridges, not atoms) + quality-diversity over failure cells, built around the value-signal blind spot (iterate on reformulations and bridges, not proofs; use the function-field shadow as the positive gradient and D-H as the negative one). COMPLETE: all five increments built (`experiments/lemma_db/fq_shadow.py` 6d, `generator.py` 6a+6c, `branch_specs.py` 6e, `transfer_search.py` 6b). 6e reads forcing questions off the asserted-vs-proven gap and generates the all-roads convergence mechanically; 6b retrieves the proven positivity theorems nearest the M4 residual (rediscovers Bost-Connes, demotes Lee-Yang, surfaces Hodge-Riemann/Alexandrov-Fenchel) but finds no escape to a foreign field. The honest net: the apparatus mechanizes the disciplines and sharpens M4 to the arithmetic Hodge index without touching the blind spot, by design. The Reduction Engine disposes; this proposes.
- **The missing-object interface (the SP-decomposition)**: [`docs/03_research/missing_object_interface.md`](docs/03_research/missing_object_interface.md). The missing object typed as ONE five-component interface (SP1 carrier / SP2 endomorphism / SP3 base+diagonal / SP4 trace formula / SP5 polarization): every component individually inhabited, every conjunction short of two measured, open joints C1 = SP2$\wedge$SP3 (counting side, needs no positivity) and C2 = M4. The B1 rung ladder (LEARNINGS #150-#153, 2026-07-02): the derived base EXISTS (non-collapsed, prime-aware; the wall is the two-sided trace formula, not the diagonal); per-prime W6 is EXACT (Poisson on $\mathbb{R}/(\log p)\mathbb{Z}$); the glue's missing input is the ADDITIVE LATTICE (the Beurling discipline, fourth clause: lattice-consuming); and the CCM prolate door already pays that clause via the map $\mathcal{E}$ on one circle of exactly the measured circumference, with the whole residue compressed into a uniform determinant-class limit (= #148's clause = M4).
- **Multi-agent session continuity**: [`experiments/orchestrator_sessions/`](experiments/orchestrator_sessions/). Read the highest-numbered file for the last ORCHESTRATOR's plan.
- **Lean 4 substrate**: [`lean/README.md`](lean/README.md). Phase 1 typed substrate landed 2026-05-25 with a VERIFIER target ID table.

## Core conceptual framework

The project is organized around **four candidate proof architectures** (from `docs/solutions/README.md` §8 and `experiments/PROOF_ARCHITECTURES_PLAN.md`):

1. **Spectral** (Hilbert-Pólya): self-adjoint operator whose eigenvalues are the imaginary parts of zeta zeros
2. **Arithmetic-geometric** (Deninger / $\mathbb{F}_1$): cohomology theory for $\mathrm{Spec}(\mathbb{Z})$ that lifts Weil's curves-over-$\mathbb{F}_q$ proof
3. **Direct positivity** (Weil / Li): $\lambda_n \geq 0$ for all $n$, or $\sum_\rho \hat f(\rho)\overline{\hat f(\bar\rho)} \geq 0$ on Schwartz $f$
4. **Analytic** (zero-free regions): push the Vinogradov-Korobov exponent $2/3 \to 1/2$

The four-level framing (`docs/02_graduate/log_correlated_fields_intro.md` §6) places RH at Level 4, not Level 3 (spectral/statistical). This is a targeting tool rather than a discouragement: a method that lives only at Level 3 (Selberg CLT, GUE statistics, multifractal log-correlated structure) cannot by itself close RH, because those statements are compatible with worlds where some zero has $\beta = 0.51$. Knowing that tells us where the proof must live (Level 4), so we spend effort there instead of polishing Level 3. One honest caveat (2026-06-28 frame-audit): that Level 4 *equals* positivity specifically (a polarization) is a finding so far, not a theorem. It generalizes from the Weil and Li reformulations; the two Level-4 routes not yet given a Davenport-Heilbronn discrimination test, the Nyman-Beurling density criterion and de Bruijn-Newman criticality, are the open frontier of the convergence, and neither is manifestly a polarization. Ruling a level out is how the search narrows.

## The Davenport-Heilbronn discipline

The **Davenport-Heilbronn L-function** (functional equation but no Euler product; known off-line zeros at $\rho \approx 0.808 + 85.7i$) is the project's **wrong-approach detector**. Any method in Architectures 1, 3, or 4 that does not distinguish zeta from D-H is structurally wrong: D-H is a known counterexample to its own analogue of RH, so any RH-style proof that "works" for D-H is incorrect.

Implementation: `experiments/_shared/davenport_heilbronn.py`. Run `python -m experiments._shared.smoke_test` to verify the whole shared infrastructure including this control is working (currently 9/9 tests, including a regression check on the first off-line zero location).

Architecture 2 sits outside this discipline because Deninger-style constructions intentionally require the Euler product that D-H lacks.

**The counting-side twin (2026-07-02, LEARNINGS #152): the Beurling discipline.** `experiments/_shared/beurling.py` provides a density-matched Beurling generalized-prime control: an Euler product with NO additive lattice (integer counting is not $x + O(1)$, no Poisson summation, no theta functional equation). Any counting-side construction (a trace-formula gluing, a fixed-point calculus, a W6 candidate) must fail for the Beurling fake for a reason it can name; if it works identically for the fake it consumes only circumference/density data and is structurally wrong. The bracket: D-H has the FE without the Euler product (kills form-side methods); Beurling has the Euler product without the FE/lattice (kills counting-side glues); zeta is the intersection, whose adelic package is Tate's thesis. Probe: `experiments/arithmetic_geometric/e2ak_beurling_discipline.py` (7/7).

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
│   ├── _shared/                 LFunction interface, zeta, D-H control, Beurling control
│   ├── positivity/              Arch 3 (Li coefficients, Weil quadratic form, Gram-matrix detector)
│   ├── spectral/                Arch 1 (Berry-Keating, Sierra-Townsend, 1D Connes adèle literature)
│   ├── zero_free/               Arch 4 (non-negative trig polynomial LP/SDP family, MT translation)
│   ├── arithmetic_geometric/    Arch 2 (worked Weil example over F_5; 2A R1-R5 follow-ups; dossiers)
│   ├── multifractal/            log-correlated field experiments (E0-E3)
│   ├── criticality/             Nyman-Beurling / de Bruijn-Newman D-H probes (both MIRROR)
│   ├── gradient_descent/        D4 meta-level policy-gradient against the Lean floor (function-field rehearsal)
│   ├── lemma_db/                reduction/generative engines, breadth corpus, oracle, transfer search
│   ├── toy/                     RH toy sandbox: checkable training ground for the M4 move (Python + Lean ToyModel)
│   └── orchestrator_sessions/   per-session ORCHESTRATOR plans
├── lean/                        Lean 4 / Mathlib formal verification (Phase 1 substrate as of 2026-05-25)
│   ├── ZetaRH.lean
│   └── ZetaRH/{Basic,MathlibBridge,DavenportHeilbronn,KillCriteria,R3_5,
│                LineRestriction,LambdaBlueprints,PrismaticCohomology,
│                PrismaticFoliation,HodgeIndex, ...}.lean   (many more modules; see lean/README.md)
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
| `SETUP.md` | First-time setup on a fresh machine: verified winget/pip/lake commands, `lake exe cache get`, Windows Store python-stub gotcha |
| `PUBLICATIONS.md` | Publishable-discovery registry + evaluation gate (formal Mathlib + arXiv); what is shippable and how we score a new finding. Usage guide: `publications/README.md`; drafts + adversary review live in `publications/` |
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
- **Python libraries**: `mpmath` (high-precision arithmetic), `numpy`, `scipy`, `cvxpy` (LP/SDP optimization with CLARABEL/SCS solvers), `sympy`, `matplotlib`, `duckdb` (lemma DB).
- **Visualization**: manim (3Blue1Brown style). `pip install manim`.
- **Formal verification**: Lean 4 + Mathlib, pinned `leanprover/lean4:v4.30.0` (`lean/` directory, requires `elan` to build).
- **Docs**: Markdown with LaTeX math (`$...$` inline, `$$...$$` block in files; plain Unicode in chat).

## Conventions

- **High-precision arithmetic**: `mpmath` at >=30 digits for zeros and L-function evaluation. `numpy` for downstream array work after conversion.
- **Data format**: experiments save `.npz` (numpy compressed) alongside the script. Plots save as `.png`. Both are gitignored under `experiments/**/_cache/` and `experiments/**/*.png`, but tracked .npz files live next to scripts.
- **Caching**: zero computations are slow (`mp.zetazero` for high index, D-H 2D scan). Each L-function caches per (T_max, prec) tuple under `experiments/_shared/_cache/`.
- **LFunction interface**: all L-functions subclass the ABC in `experiments/_shared/lfunction.py` and implement `evaluate(s)` and `zeros(T_max, prec=30)`. Used uniformly across architectures so the same experiment can run on zeta and D-H with identical code.
- **No linter / formatter / CI is configured.** Match the surrounding style.

## Style

- **No em dashes** anywhere. (Global preference. Use periods, colons, parentheses, or hyphens instead.) Don't add em dashes, don't use them at all, anywhere, ever. Rewrite the sentence instead.
- Inline math in markdown uses `$...$` for inline, `$$...$$` for display. KaTeX renders most things in the docs surface.
- In chat output the KaTeX surface is not available; use Unicode and plain text for math.
- Code: explanatory module-level docstrings, minimal inline comments. Comments should explain WHY, not WHAT.

## Running things

First-time setup on a fresh machine (install Python + all deps, elan + Lean/Mathlib): see [`SETUP.md`](SETUP.md). It carries the verified winget/pip/lake commands, the required `lake exe cache get` step, and the Windows Store python-stub gotcha.

```powershell
# Python deps (see SETUP.md for the Windows Store python-stub gotcha)
python -m pip install -r requirements.txt

# Smoke test the shared infrastructure (expect "9/9 passed")
python -m experiments._shared.smoke_test

# Run an experiment (each is a python module)
python -m experiments.positivity.e3c2_weil_gram
python -m experiments.spectral.e1a_berry_keating
python -m experiments.zero_free.e4b_nonneg_trig
python -m experiments.arithmetic_geometric.e2b_elliptic_curve_fp

# Build the Lean substrate (requires elan + lake)
cd lean; lake exe cache get; lake build   # cache get is REQUIRED first (else ~1h compiling Mathlib from source)

# Dependencies: see requirements.txt (numpy, scipy, mpmath, matplotlib, manim, sympy, cvxpy, duckdb)
```

Working dir is the repo root. Scripts use `from experiments._shared import ...` style imports, which only resolve from the root.

**Tests are standalone modules, not pytest**: each `test_*.py` / `smoke_test.py` has a `main()` under `if __name__ == "__main__"` and prints `N/N passed` (e.g. `python -m experiments.lemma_db.test_oracle`, `python -m experiments.toy.test_toy`). When you add an experiment, add its checks in this pattern.

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

## When to ask

- The change would alter the LFunction interface, the D-H / Beurling controls, or the smoke-test contract.
- A proposed method does not engage the four-level framing (likely Level 3, not RH-closing) or cannot separate zeta from D-H.
- Before any commit or push (per-action authorization required), or before restructuring the docs/experiments layout the atlas and PROOF_ARCHITECTURES_PLAN depend on.

## Constellation

This repo is tracked by Constellation. It has `README.md` with `## Status` and `TODO.md` with checkboxes.