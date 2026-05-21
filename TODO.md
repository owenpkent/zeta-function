# TODO — Riemann Zeta Function Study Repo

## Done

### Repo and docs

- [x] Set up repo structure
- [x] Write README.md
- [x] **docs/solutions/** — known approaches and obstructions per architecture
- [x] **docs/research_atlas/** — master research map, all approaches and obstructions
- [x] **docs/02_graduate/log_correlated_fields_intro.md** — log-correlated fields, four-level RH framing, primes-zeros Fourier duality
- [x] **docs/03_research/** — extreme values, log-correlated fields, new mathematics
- [x] **CLAUDE.md** — project context for AI assistants

### Experimental thread (see `experiments/PROOF_ARCHITECTURES_PLAN.md`)

- [x] Phase 0: shared infrastructure (LFunction interface, zeta, Davenport-Heilbronn control, smoke test 5/5)
- [x] Arch 3A: zeta Li coefficients, positivity confirmed for n=1..500
- [x] Arch 3B: per-zero Li diagnostic; central finding: small-n Li positivity does NOT distinguish zeta from D-H
- [x] Arch 3C: Weil quadratic form via Gram matrix; M^DH has negative eigenvalues (wrong-approach detector witness)
- [x] Arch 3D: scaling study of witness with K and T_max; witness deepens with K
- [x] Arch 1A: Berry-Keating discretization; density-mismatch with zeta documented
- [x] Arch 4B: non-negative trig polynomial LP saturates Fejér bound; classical 3+4cos+cos2 sub-optimal at degree 2
- [x] Arch 2B: Weil RH for E: y^2 = x^3 + x + 1 over F_5 verified end-to-end

### Pre-existing experiments

- [x] **experiments/multifractal/** — E0 benchmarks, E1 zeta MFDFA, E2 FHK max fit, E3 psi MFDFA

## Open — experimental

- [ ] Arch 3B-extension: direct xi-derivative Li computation for D-H to reach n ~ 25,000 and observe lambda_n < 0
- [ ] Arch 3E: quantify the Li / de Bruijn-Newman relationship
- [ ] Arch 1B: Sierra-Townsend hyperbolic-half-plane model; reproduce eigenvalue match against first 100 zeros
- [ ] Arch 1C: apply candidate operators to Davenport-Heilbronn (wrong-approach check)
- [ ] Arch 1D: Connes adèle-class space literature review
- [ ] Arch 4A: Vinogradov-Korobov reproduction; localize where the 2/3 exponent appears
- [ ] Arch 4C: map conditional-improvement landscape (Heath-Brown, Pintz, Ford)
- [ ] Arch 4D: search for structurally new auxiliary inequalities beyond non-negative trig polynomials
- [ ] Arch 2A: Weil-proof step-by-step diff table (curves-over-F_q vs Z)
- [ ] Arch 2C: survey state of F_1 / Arakelov-cohomology programs as of 2025
- [ ] Arch 2D: identify the smallest open conjecture in Deninger's program worth targeting
- [ ] Cross-cut: Selberg-class systematic comparison across architectures

## Open — docs and visualizations

- [ ] Convert PDFs to Markdown — all 4 source PDFs (text conversions exist in sources/, refine)
- [ ] **docs/00_intuitive/** — write intuitive-level explanation
- [ ] **docs/01_undergraduate/** — write undergrad-level explanation
- [ ] **docs/implications/** — why RH matters (primes, physics, crypto)
- [ ] manim scene: ZetaSeriesIntro — partial sums of zeta(s), s real
- [ ] manim scene: ComplexPlane — plotting zeta on the complex plane
- [ ] manim scene: AnalyticContinuation — extending beyond Re(s) > 1
- [ ] manim scene: CriticalStrip — the critical strip 0 < Re(s) < 1
- [ ] manim scene: ZerosOnCriticalLine — known non-trivial zeros at Re(s) = 1/2
- [ ] manim scene: PrimeConnectionExplainer — zeta and prime counting function

## ML / formalization backlog

- [ ] Set up zero data pipeline (Odlyzko tables, LMFDB)
- [ ] Build ML experiment framework for zero pattern analysis
- [ ] Implement operator discovery pipeline (parameterized operators + spectral matching)
- [ ] Implement Weil positivity numerical explorer (largely subsumed by Arch 3C, extend with neural-net basis)
- [ ] Li criterion sequence analysis and prediction
- [ ] Robin's inequality adversarial search (colossally abundant numbers)
- [ ] Formalize RH equivalences in Lean 4
- [ ] Add glossary of terms
- [ ] Add bibliography / further reading
- [ ] Link visualizations to corresponding doc sections
- [ ] Add Jupyter notebooks for interactive exploration
- [ ] Explore L-functions generalization
