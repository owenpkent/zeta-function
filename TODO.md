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

- [x] Phase 0: shared infrastructure (LFunction interface, zeta, Davenport-Heilbronn, Dirichlet chi_3/chi_4, smoke test 8/8)
- [x] Arch 3A: zeta Li coefficients, positivity confirmed for n=1..500
- [x] Arch 3B: per-zero Li diagnostic; small-n Li positivity does NOT distinguish zeta from D-H
- [x] Arch 3B.2: large-n Li witnesses lambda_n^DH < 0 at n = 4 x 10^5 via asymptotic + off-line correction
- [x] Arch 3C: Weil quadratic form via Gram matrix; M^DH has negative eigenvalues (wrong-approach detector)
- [x] Arch 3C.3: Selberg-class cross-cut (chi_3) confirms detector direction-selectivity
- [x] Arch 3D: scaling of witness with K and T_max; witness deepens with K
- [x] Arch 3D.2: K-scaling cross-cut over zeta, chi_3, chi_4, D-H
- [x] Arch 3D.3: K-scaling extended to K=1000 — relative min converges to -2.62%, neg count = # off-line zero pairs (fixed at 4)
- [x] Arch 3F: Weil-form duality for zeta (prime-side = zero-side to <2% at T_max=1000)
- [x] Arch 3G: Weil-form duality for D-H (oscillating Dirichlet sum, cancellation 100x looser than zeta)
- [x] Arch 3H: Weil-form duality for chi_3 (intermediate cancellation; tight cancellation is specifically zeta's pole)
- [x] Arch 3I: chi_3 unconditional path blocked by Siegel-Walfisz looseness (factor 30-120 too loose)
- [x] Arch 1A: Berry-Keating discretization; density-mismatch with zeta documented
- [x] Arch 1B: Sierra-Townsend modifications (centrifugal, Coulomb, modular log); all L-function-agnostic
- [x] Arch 1C: L-function discrimination test — best-affine RMS ratio spans factor 3 around 1
- [x] Arch 4B: non-negative trig polynomial LP saturates Fejér bound
- [x] Arch 4D, 4D.2: single-coefficient d-variate LPs decompose to tensor products
- [x] Arch 4E: balanced-sum LP max c_{1,1} + c_{2,2} exceeds tensor bound by 12% at N=2
- [x] Arch 4E.2: alpha sweep — peak gap +25% at alpha=3, N=2; clean rational LP-optimum
- [x] Arch 4E.3: +25% C-S gap does NOT translate to MT zero-free constant improvement (structural lemma)
- [x] Arch 4E.4: trivariate balanced-sum LP — gap +51% at alpha=3.25, N=2 (doubles bivariate)
- [x] Arch 4E.5: d=4 balanced-sum LP — gap [+55%, +70%] at alpha=4.5, N=2 (sub-linear scaling)
- [x] Arch 2B: Weil RH for E: y^2 = x^3 + x + 1 over F_5 verified end-to-end
- [x] Arch 2A: Weil-proof diff table + 17-constraint spec + candidate evaluation framework (see experiments/arithmetic_geometric/2A_weil_proof_diff.md and 2A_candidate_evaluation.md)
- [x] Arch 2A R1: D-H exclusion sharpening for the six scored candidates (see experiments/arithmetic_geometric/2A_R1_DH_exclusion.md)
- [x] Arch 2A R2: fiber product computation in Borger and Lorscheid (see experiments/arithmetic_geometric/2A_R2_fiber_product.md)

### Pre-existing experiments

- [x] **experiments/multifractal/** — E0 benchmarks, E1 zeta MFDFA, E2 FHK max fit, E3 psi MFDFA

## Open — experimental

- [ ] Arch 3B-extension (rigorous): direct xi-derivative Li computation for D-H at n ~ 4 x 10^5 with ~100-digit precision (3B.2 used asymptotic + off-line correction; the rigorous version replaces the asymptotic)
- [ ] Arch 3D.3 extension: test prediction "neg count = # off-line pairs" by going to T_max = 500 where D-H has more off-line pairs
- [ ] Arch 3E: quantify the Li / de Bruijn-Newman relationship (literature)
- [ ] Arch 1D: Connes adèle-class space literature review
- [ ] Arch 4A: Vinogradov-Korobov reproduction; localize where the 2/3 exponent appears
- [ ] Arch 4C: map conditional-improvement landscape (Heath-Brown, Pintz, Ford)
- [ ] Arch 4E.6: constrained-domain LP — impose P ≥ 0 only on a hypothetical-off-line-zero submanifold (the only LP direction not bounded by 1D Fejér per 4E.3's structural lemma)
- [ ] Arch 4E.7: multi-zero MT bookkeeping — Heath-Brown-style coupling for least-prime-in-AP or Siegel-zero problems
- [ ] Arch 4E.8: polynomial-ideal sum-of-squares decompositions for the Weil quadratic form
- [ ] Arch 2C: survey state of F_1 / Arakelov-cohomology programs as of 2025 (use the scorecard structure from 2A_candidate_evaluation.md)
- [ ] Arch 2D: identify the smallest open conjecture in Deninger's program worth targeting
- [x] Arch 2A R1: sharpen D-H exclusion (constraint xvii) for each of the six scored candidates (see experiments/arithmetic_geometric/2A_R1_DH_exclusion.md — all six pass K2 by construction; K2 safety conditional on Selberg conjecture)
- [x] Arch 2A R2: compute Spec(Z) x_F1 Spec(Z) in Borger / Lorscheid (see experiments/arithmetic_geometric/2A_R2_fiber_product.md — Borger: Spec(W(Z)) via big Witt ring; Lorscheid: blueprint (Z × Z, doubled relations); both 🟡 on (ii), intersection theory still open)
- [ ] Arch 2A R3: identify whether Connes-Consani positivity conjecture fails kill criterion K1 (RH-equivalence)
- [ ] Arch 2A R4: explore hybrid candidates (Borger Frobenius + Connes trace formula)
- [ ] Arch 2E (numerical probe): Adams-operation spectrum vs zeta zeros — does Borger's psi_p have zeta-zero-like spectrum at small p?

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
