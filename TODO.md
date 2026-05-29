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
- [x] Arch 3J: Schur complement of Weil-form Gram matrix against on-line cushion — irreducible off-line obstruction is ~30x sharper than raw spectrum (rel min asymptote -78.7% vs -2.6%), signature exactly (N_off, N_off) per off-line gamma in UHP; quantitative form of marginal-positivity thesis (see experiments/positivity/e3j_schur_complement.py + README §3J)
- [x] Arch 3K: hypothetical off-line zero perturbation — Schur signal scales as 16*(beta-1/2)^2 across four decades; float64 stealth window (eps < 10^-5) is looser than Platt-Trudgian rigorous bound (eps < 10^-7); disproof in Gram-matrix family has no leverage point (see experiments/positivity/e3k_hypothetical_offline.py + README §3K)
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
- [x] Arch 2A R2: fiber product computation in Borger and Lorscheid (see experiments/arithmetic_geometric/2A_R2_fiber_product.md + companion dossiers 2A_borger_dossier.md, 2A_lorscheid_dossier.md)
- [x] Arch 2A R2.5: Λ-blueprint hybrid proposal (see experiments/arithmetic_geometric/2A_R2_5_lambda_blueprints.md)
- [x] Arch 2A R3: Connes-Consani K1 analysis (see experiments/arithmetic_geometric/2A_R3_connes_positivity.md)
- [x] Arch 2A R3.5: no-shortcut theorem for NCG approaches (see experiments/arithmetic_geometric/2A_R3_5_K1_universality.md)
- [x] Arch 2A R3.6: deep dive on Connes-Consani arithmetic site / hyperrings / characteristic-one geometry (see experiments/arithmetic_geometric/2A_R3_6_arithmetic_site.md) — all formulations probably fail K1; Connes-Consani (xi)-(xiii) sharpened from 🟡 to ❌
- [x] Arch 2A R4: Borger Frobenius + Connes trace formula hybrid analysis (see experiments/arithmetic_geometric/2A_R4_borger_connes_hybrid.md)
- [x] Arch 2A R5: prismatic cohomology investigation (see experiments/arithmetic_geometric/2A_R5_prismatic_cohomology.md)
- [x] Arch 2A path forward strategic synthesis (see experiments/arithmetic_geometric/2A_path_forward.md)
- [x] Arch 2E: numerical probe of bare psi_p spectrum on concrete Lambda-rings (see experiments/arithmetic_geometric/e2e_adams_spectrum.py + 2E_adams_spectrum_probe.md) — confirmed predicted negative result: roots of unity / {0} / powers of p, no structural relation to zeta zeros; randomization control rules out apparent K-theory near-coincidence as signal

### Session 003 (2026-05-28): gap-closing experiments

- [x] Shared: Epstein zeta as an independent second wrong-approach control (experiments/_shared/epstein_zeta.py). Chowla-Selberg / Terras evaluation validated to 1e-31 against the class-number-1 anchor Z_Q = 4 zeta(s) beta(s) and to 1e-32 against its own functional equation. Off-line zeros found for the class-number-5 disc -47 non-principal form (rho ~ 0.634 + 32.05 i); the principal form has none (Selberg-like contrast).
- [x] Arch 3L: Epstein second-control test of the Weil-form Schur detector (experiments/positivity/e3l_epstein_control.py). The counting law schur_neg = #off-line heights, schur_dim = 2 x #off-line heights holds identically on Epstein as on D-H (clean PASS, K up to 300). The wrong-approach detector GENERALISES beyond Davenport-Heilbronn. LEARNINGS #19.
- [x] Arch 3B.4: rigorous Li-criterion discrimination across five L-functions (experiments/positivity/e3b4_li_discrimination.py). Reproduces D-H rigorous negativity (n=336,000), Selberg controls rigorously positive (n=50,000), and gives a SECOND off-line Li witness: Epstein lambda_n < 0 rigorously from n=110,000 (Epstein scanned to T=500 so the tail bound is negligible). Full rigorous discrimination at n=336,000: lambda_n^DH < 0 and lambda_n^Epstein < 0 < lambda_n^zeta, lambda_n^chi3. LEARNINGS #22.
- [x] Arch 2F: function-field Hodge-index positivity sweep (experiments/arithmetic_geometric/e2f_hodge_index_sweep.py). Weil RH bound |alpha_i| = sqrt(q) holds exactly (0.000e+00) across elliptic curves over F_5..F_23 and genus-2 curves over F_5..F_13. Exhibits the positivity target a Spec(Z) lift must reproduce. LEARNINGS #20.
- [x] Arch 4E.9: Heath-Brown multi-zero MT SDP, Direction 7 (experiments/zero_free/e4e9_heath_brown_sdp.py). The multi-zero MT shape factor does NOT exceed the 1D Fejer ceiling (best ratio <= 1, rank-2 certificate). Closes the last LP/SDP/SOS escape from the 4E.3 lemma. LEARNINGS #21.

### Session 004 (2026-05-28/29): Direction 8 single-arithmetic-surface side

- [x] Arch 3M: input-side place-type decomposition of the Weil form M = A_arch + P_fin + B_pole (experiments/positivity/e3m_place_type_balance.py). LEARNINGS #20.
- [x] Arch 2G: the Hodge index as a SIGNATURE on C x C (primitive form negative definite = Hasse-Weil); machine-proved in Lean (negDef_iff_hasseWeil). LEARNINGS #21.
- [x] Arch 2H/2M: Faltings-Hriljac height pairing over Spec(Z) positive definite, ranks 1-4 (regulators match LMFDB). LEARNINGS #22.
- [x] Arch 2I/2L/2O/2P: complete Silverman local-height decomposition (archimedean Green/Petersson + every finite prime) validated h_inf + sum_p h_p = h_hat by the authoritative algorithm. LEARNINGS #23, #24.
- [x] Arch 2J/2K: arithmetic adjunction (omega-bar^2 = 12 h_Fal) + the dictionary to the would-be Spec(Z) x Spec(Z) intersection form (the product-surface gap, the Morishita bridge literature).

### Session 005 (2026-05-29): sharpen Gamma_S + the Lean explicit-formula thread

- [x] Arch 2Q: the place-dependent bidegree obstruction (experiments/arithmetic_geometric/e2q_frobenius_bidegree.py). Gamma_S must carry a (1,p) bidegree per prime, not a single scale q; forces infinite-dim H^i + the Deninger R-flow as consequences; pins Gamma_S^2 to the von Mangoldt prime sum. Sharper K2 (D-H has no local bidegrees). LEARNINGS #25.
- [x] Arch 2R: Ruelle dynamical-zeta realization of Gamma_S^2 (experiments/arithmetic_geometric/e2r_dynamical_zeta.py). Orbit lengths {log p}; prod_p (1-p^-s)^-1 = zeta and sum_n Lambda(n) n^-s = -zeta'/zeta = Gamma_S^2 (verified to 2e-4). D-H Lambda delocalizes off prime powers => no closed-orbit spectrum (dynamical K2). The Deninger half of the Morishita bridge made concrete; NOT a new RH route. LEARNINGS #26.
- [x] Lean: ExplicitFormula.lean — Weil explicit formula + Weil positivity criterion scaffold (#EF-1/#EF-2, the highest-leverage target, LEARNINGS #17); prime side concrete via Mathlib vonMangoldt.
- [x] Lean: discharged #MB-1 (zeta pole at s=1), #MB-2 (zeta nonvanishing Re s>1), #MB-6 (functional equation) to real kernel-checked proofs from existing Mathlib.
- [x] Lean: proved the digamma recurrence psi(s+1)=psi(s)+1/s (digamma_add_one) from Complex.Gamma_add_one (Mathlib has no digamma). Build green; project sorry count 26 -> 23.

### Pre-existing experiments

- [x] **experiments/multifractal/** — E0 benchmarks, E1 zeta MFDFA, E2 FHK max fit, E3 psi MFDFA

## Open — experimental

- [x] Arch 3B-extension (rigorous): rigorous Li negativity for D-H at n ~ 4 x 10^5 with >=100-digit precision and explicit error/tail bounds (3B.3, experiments/positivity/e3b3_rigorous.py; first rigorously negative at n=336,000). Extended in 3B.4 to a five-L-function discrimination with a second off-line witness (Epstein).
- [x] Arch 3D.3 extension: test prediction "neg count = # off-line pairs" by going to T_max = 500. **CONFIRMED**: D-H has 9 off-line gammas in UHP at T_max=500, n_neg = 9 (MATCH). Rel min eig = -2.597e-02 (stable at ~-2.6% across all tested T_max). Four data points total: T_max ∈ {200, 300, 350, 500}, off-gammas {4, 5, 7, 9}, all match n_neg exactly. Two non-trivial double-increments (+2 at T_max=350 and T_max=500). See experiments/positivity/e3d4_T_max_scaling.* updated.
- [x] Arch 3E: quantify the Li / de Bruijn-Newman relationship (literature). See experiments/positivity/3e_li_de_bruijn_newman.md. Both are positivity reformulations of RH: Li discrete (sequence), dBN continuous ($\Lambda = 0$ ⟺ RH per Rodgers-Tao 2018 + Newman 1976). Current dBN bounds: $0 \le \Lambda \le 0.22$. Both confirm the project's "marginal positivity" picture (LEARNINGS #7): RH is true only at the margin, which points the proof toward the exact structure of zeta rather than soft positivity.
- [x] Arch 1D: Connes adèle-class space literature review (see experiments/spectral/1d_connes_adele_literature.md). Complements 2A_connes_dossier.md from the Arch 1 angle. A rigorous numerical experiment requires research-grade work and the central spectral identification is conjectural.
- [x] Arch 4A + 4C: Vinogradov-Korobov and conditional-improvement landscape (unified literature dossier; see experiments/zero_free/4a_4c_vinogradov_korobov.md). The $2/3$ exponent is a structural ceiling within the V-K recipe: aux ineq saturated by 4B-4E.7, V-MVT at sharp form via Bourgain-Demeter-Guth 2016, explicit formula is identity. No named conditional (density hypothesis, LH, no-Siegel-zero, Heath-Brown, Pintz, Ford, BDG) pushes the exponent. **Arch 4 is a constraint-mapping architecture, not a route to RH**; pushing the exponent requires a fundamentally new input class (Arch 2 arithmetic-geometric exponential-sum machinery á la Deligne, or Arch 1 Connes spectral identification).
- [x] Arch 4E.6: constrained-domain LP — impose P ≥ 0 only on a hypothetical-off-line-zero submanifold (see experiments/zero_free/e4e6_constrained_lp.py + .md). Tested four formulations (K-point, arc-removal, zero-constrained, trick-at-off-line-height). All collapse to Fejér / full-non-negativity ceiling at well-resolved parameters; apparent gains are LP-unbounded artifacts or sparse-sampling artifacts. **4E.3's lemma is robust under naive domain relaxation.** Genuine escape requires Heath-Brown multi-zero coupling (4E.7), Bombieri variational SOS, or polynomial-ideal SOS (4E.8) — qualitatively different machinery beyond LP-over-a-subset.
- [x] Arch 4E.7: multi-zero MT bookkeeping — Heath-Brown-style coupling (see experiments/zero_free/e4e7_multi_zero_lp.py + .md). LP escape from 4E.3 is real at the shape-factor level (λ_{1,1} is 55-137× larger than λ_1² for N ∈ {2,3,4}), but the naive max c_{1,1} objective produces rank-1 (tensor-product) LP optima. A non-trivial multi-zero MT improvement for RH on zeta would require combining this with higher-harmonic structure (4E.2's +25% rank-2 gain) AND explicit Heath-Brown bookkeeping — research-grade.
- [x] Arch 4E.8: polynomial-ideal sum-of-squares (Putinar/Schmüdgen) for the MT figure of merit (experiments/zero_free/e4e8_sos_sdp.py) — SDP saturates Fejér but does not exceed it; closes the LP/SDP family escape. Extended in 4E.9 (Heath-Brown multi-zero MT, Direction 7): multi-zero shape factor also capped by Fejér (ratio <= 1, rank-2).
- [x] Arch 2C: survey state of F_1 / Arakelov-cohomology programs as of 2025 (commit fd020fc; 280-line landscape survey)
- [x] Arch 2D: identify the smallest open conjecture in Deninger's program worth targeting (commit 10c9f05; M3 prismatic foliation hypothesis, now Direction 4)
- [x] Arch 2A R1: sharpen D-H exclusion (constraint xvii) for each of the six scored candidates (see experiments/arithmetic_geometric/2A_R1_DH_exclusion.md — all six pass K2 by construction; K2 safety conditional on Selberg conjecture)
- [x] Arch 2A R2: compute Spec(Z) x_F1 Spec(Z) in Borger / Lorscheid (see experiments/arithmetic_geometric/2A_R2_fiber_product.md — Borger: Spec(W(Z)) via big Witt ring; Lorscheid: blueprint (Z × Z, doubled relations); both 🟡 on (ii), intersection theory still open)
- [x] Arch 2A R2.5: sketch the Λ-blueprint hybrid framework as a research proposal (see experiments/arithmetic_geometric/2A_R2_5_lambda_blueprints.md). Predicted scorecard 8 ✅ / 4 🟡 / 5 ⏳ if developed. Still needs rigorous definition, categorical verification, fiber product computation — thesis-level project.
- [x] Arch 2A R3: Connes-Consani K1 analysis (see experiments/arithmetic_geometric/2A_R3_connes_positivity.md). Three positivity conjectures analyzed; C1 and C2 are RH-equivalent (K1 fail); C3 is K1-uncertain. Connes / Connes-Consani (xi)-(xiii) moves from ❌ to 🟡 in the scorecard.
- [x] Arch 2A R4: explored Borger Frobenius + Connes trace formula hybrid (see experiments/arithmetic_geometric/2A_R4_borger_connes_hybrid.md) — predicted scorecard ~8 ✅ / 5 🟡 / 3 ❌; fails K1 per R3.5; value is infrastructure for the geometric route
- [x] Arch 2A R5: prismatic cohomology analyzed as candidate cohomology theory for Spec(W(ℤ)) (see experiments/arithmetic_geometric/2A_R5_prismatic_cohomology.md). δ-rings ↔ Λ-rings at one prime; predicted to close constraints (iv)-(vii). Still K1-blocked on positivity per R3.5.
- [ ] Arch 2A R3.6.3 (surfaced by R3.6): investigate whether Connes-Consani machinery (arithmetic site, hyperrings, characteristic-one geometry) can serve as INFRASTRUCTURE for the geometric route — even though its positivity formulations fail K1, the topos-theoretic / sheaf-theoretic tools might support intersection theory on a constructed surface
- [x] Arch 2E (numerical probe): Adams-operation spectrum vs zeta zeros — does Borger's psi_p have zeta-zero-like spectrum on concrete Lambda-rings? (see experiments/arithmetic_geometric/2E_adams_spectrum_probe.md — NO: spectra are roots of unity, {0}, or powers of p; confirms R5 framing that cohomology must do the lifting, bare Lambda-structure is too small)

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
