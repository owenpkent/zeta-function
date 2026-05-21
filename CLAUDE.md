# CLAUDE.md

Project-specific instructions for Claude Code. Read on every session start.

## What this repo is

A research-and-study project on the Riemann Hypothesis. It contains:
- Layered docs (intuitive → undergraduate → graduate → research) on $\zeta$ and the RH
- A strategic landscape document (`docs/research_atlas/`) cataloging every known proof approach with its obstructions
- A computational experimental thread (`experiments/`) organized around testing the four candidate RH proof architectures

It is **not** a tool or product. It is a research codebase. Output is markdown documents, numerical experiments, and visualizations.

## Core conceptual framework

The project is organized around **four candidate proof architectures** (from `docs/solutions/README.md` §8 and `experiments/PROOF_ARCHITECTURES_PLAN.md`):

1. **Spectral** (Hilbert-Pólya): self-adjoint operator whose eigenvalues are the imaginary parts of zeta zeros
2. **Arithmetic-geometric** (Deninger / $\mathbb{F}_1$): cohomology theory for $\mathrm{Spec}(\mathbb{Z})$ that lifts Weil's curves-over-$\mathbb{F}_q$ proof
3. **Direct positivity** (Weil / Li): $\lambda_n \geq 0$ for all $n$, or $\sum_\rho \hat f(\rho)\overline{\hat f(\bar\rho)} \geq 0$ on Schwartz $f$
4. **Analytic** (zero-free regions): push the Vinogradov-Korobov exponent $2/3 \to 1/2$

The four-level framing (`docs/02_graduate/log_correlated_fields_intro.md` §6) places RH at Level 4 (positivity), not Level 3 (spectral/statistical). This is the project's structural commitment: any method that lives only at Level 3 (Selberg CLT, GUE statistics, multifractal log-correlated structure) cannot close RH because those statements are compatible with worlds where some zero has $\beta = 0.51$.

## The Davenport-Heilbronn discipline

The **Davenport-Heilbronn L-function** (functional equation but no Euler product; known off-line zeros at $\rho \approx 0.808 + 85.7i$) is the project's **wrong-approach detector**. Any method in Architectures 1, 3, or 4 that does not distinguish zeta from D-H is structurally wrong: D-H is a known counterexample to its own analogue of RH, so any RH-style proof that "works" for D-H is incorrect.

Implementation: `experiments/_shared/davenport_heilbronn.py`. Run `python -m experiments._shared.smoke_test` to verify the control is working (5/5 tests including a regression check on the first off-line zero location).

Architecture 2 sits outside this discipline because Deninger-style constructions intentionally require the Euler product that D-H lacks.

## Repository structure

```
docs/
  00_intuitive/         intuitive-level explanations
  01_undergraduate/     undergrad-level explanations
  02_graduate/          graduate-level (incl. log-correlated fields, four-level RH framing)
  03_research/          research-level overviews (extreme values, log-correlated, FHK)
  research_atlas/       strategic landscape; the master reference for "what's been tried"
  solutions/            known proof approaches with obstructions per architecture
  implications/         why RH matters
experiments/
  PROOF_ARCHITECTURES_PLAN.md   the test plan
  _shared/              LFunction interface + zeta + Davenport-Heilbronn
  positivity/           Arch 3 (Li coefficients, Weil quadratic form, Gram-matrix witness)
  spectral/             Arch 1 (Berry-Keating discretization)
  zero_free/            Arch 4 (non-negative trig polynomials)
  arithmetic_geometric/ Arch 2 (elliptic curve over F_5 worked example)
  multifractal/         pre-existing log-correlated-field experiments (E0-E3)
sources/                source PDFs (Riemann, Wilkins translation, etc.)
visualizations/         (manim scenes, planned)
```

## Conventions

- **High-precision arithmetic**: `mpmath` at ≥30 digits for zeros and L-function evaluation. `numpy` for downstream array work after conversion.
- **Data format**: experiments save `.npz` (numpy compressed) alongside the script. Plots save as `.png`. Both are gitignored under `experiments/**/_cache/` and `experiments/**/*.png` — but tracked .npz files live next to scripts.
- **Caching**: zero computations are slow (`mp.zetazero` for high index, D-H 2D scan). Each L-function caches per (T_max, prec) tuple under `experiments/_shared/_cache/`.
- **LFunction interface**: all L-functions implement `evaluate(s)` and `zeros(T_max, prec)`. Used uniformly across architectures so the same experiment can run on zeta and D-H with identical code.

## Style

- **No em dashes** anywhere. (Global preference. Use periods, colons, parentheses, or hyphens instead.)
- Inline math in markdown uses `$...$` for inline, `$$...$$` for display. KaTeX renders most things.
- Code: explanatory module-level docstrings, minimal inline comments. Comments should explain WHY, not WHAT.
- Don't add em dashes, don't use them at all, anywhere, ever. Rewrite the sentence instead.

## Running things

```bash
# Smoke test the shared infrastructure
python -m experiments._shared.smoke_test

# Run an experiment (each is a python module)
python -m experiments.positivity.e3c2_weil_gram
python -m experiments.spectral.e1a_berry_keating
python -m experiments.zero_free.e4b_nonneg_trig
python -m experiments.arithmetic_geometric.e2b_elliptic_curve_fp

# Dependencies: see requirements.txt (numpy, scipy, mpmath, matplotlib, manim, sympy)
```

Working dir is the repo root. Scripts use `from experiments._shared import ...` style imports, which only resolve from the root.

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
