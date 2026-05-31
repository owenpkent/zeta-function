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

### Session 007 (2026-05-30): creative directions (9-13), reframe, and the Rosati spine

- [x] Directions 9-13 proposed (docs/03_research/research_directions/09-13 + README), each attacking the #25 place-dependent-bidegree obstruction: 9 arithmetic matroid (AHK ↔ Li), 10 cyclotomic Frobenius over the sphere spectrum (THH/TC), 11 bidegree-as-a-measure, 12 de Bruijn-Newman criticality (Λ=0), 13 infinite-genus tau-function.
- [x] e3n (Li log-concavity / Hodge-Riemann signature): the log-concavity defect is a NON-Euler detector, not an RH detector — the Epstein d47-principal control (non-Euler, RH holds) fires with the most violations. The #20 reformulation trap in a new basis. LEARNINGS #27.
- [x] e_jensen_turan (Jensen polynomials / Turán inequalities on ξ Pólya moments): zeta, D-H, and Epstein-principal all pass at reachable order — a STEALTH WINDOW (the ξ-moment basis is blind to off-line zeros at height 85.7). Two bases, two different walls. LEARNINGS #27.
- [x] e_thh_vonmangoldt (Direction 10A.ii first pass): Bökstedt's THH(Z) torsion log-orders assemble (exactly, given the i^-s weight) to -ζ'(s); the von Mangoldt sum = Γ_S² (#26) is one Möbius factor 1/ζ away. Per-prime structure via v_p(i) verified. LEARNINGS #28.
- [x] e_necklace_mobius (Gap B): the cyclotomic C_n-fixed-point components are indexed by necklace polynomials = literally Möbius inversion (Metropolis-Rota cyclotomic identity verified exactly). The μ factor is intrinsic to the cyclotomic combinatorics. LEARNINGS #28.
- [x] SURVEYOR literature reconnaissance (survey_tc_zeta_literature.md): the THH→von Mangoldt link is not in the literature as posed; the proven template is Hesselholt's ζ(X,s)=det_inf(s-Θ|TP_odd)/det_inf(s-Θ|TP_ev) over F_q. Reorients Direction 10; the over-Z gap is #25 again; ADVERSARY flags the TC-equalizer=Möbius guess as a likely category error. LEARNINGS #29.
- [x] Synthesis: docs/03_research/all_roads_to_the_signature.md — every architecture/direction realizes ζ (determinant/trace) but RH is the SIGNATURE/positivity, the same object everywhere; the irreducible content. LEARNINGS #30.
- [x] e2s (TP odd/even = Weil Hodge-index split): triple equivalence across genus 1-2 over F_q (primitive intersection negative-definite ⟺ |α_i|=√q ⟺ Hesselholt zeros on Re=1/2). The K3 check for the TP lens.
- [x] 08A: RH reformulated as arithmetic Rosati positivity = the arithmetic Hodge standard conjecture, with the M1-M5 milestone ladder. The standard-conjecture (Grothendieck) home of the problem; non-circular (polarization, not zeros); K2-clean.
- [x] e2t (milestone M1, done): the full 2g-dimensional Rosati trace form has no negative eigenvalues across genus 1-2 over F_q ⟺ |α_i|=√q. Degeneracies (genus-2/F_5) = proper-subalgebra relations. For g=1, G_Rosati = -(2G primitive Gram). Four equivalent function-field faces of RH-for-C now recorded. LEARNINGS #31.
- [x] e2u (milestone M2, attempted): the arithmetic Rosati positivity assembled as the non-circular archimedean-dominance balance (3M place-type split). Verdict CONTAMINATED by the A_arch ~0.06 offset (balance backwards: D-H outranks zeta). Gate isolated and named (M2.5 = recompute A_arch via the bilinear Bombieri integral). LEARNINGS #32.
- [x] e2v (milestone M2.5, done): A_arch fixed via 3F's validated Bombieri physical-space integral (cross-b bilinear block), VALIDATED by T_max-convergence (residual vs zero-side Gram -> 0, so #32's contamination was the zero-side truncation), diagnostic corrected to min eig(A+P+B). RESULT: the non-circular Weil form for zeta is POSITIVE (min eig +0.035, stable across K=5..8; necessary-not-sufficient). D-H deferred to M2.6 (general-mu kernel mis-normalized). LEARNINGS #33.
- [x] e2w (milestone M2.6, done): general-mu archimedean constant fixed (C_mu = log pi - psi((1+mu)/2); the M2.5 bug was psi(1/2+mu)), verified C_0/C_1, D-H block residual 5.58 -> 0.12 (validated). Four-way verdict FAILS to separate: D-H reads spuriously positive (+0.094) -- stealth window (off-line obstruction below the residual floor; #18/#19/#27 on the Rosati side). Consequence: M3 must be ANALYTIC. LEARNINGS #34.
- [x] docs/researcher_mindset.md: the operating philosophy (target not monument; advance a front; negative results are coordinates; honesty is the engine; reformulation must import power; build the ladder; the AI-augmented research group). Wired into CLAUDE.md START HERE. Project framing recast from "long-shot catalog" to "research program with attackable milestones".

### Pre-existing experiments

- [x] **experiments/multifractal/** — E0 benchmarks, E1 zeta MFDFA, E2 FHK max fit, E3 psi MFDFA

## Open — experimental

- [x] **Milestone M2.5 (done): recompute A_arch from the bilinear Bombieri physical-space integral** (e2v_rosati_balance_M2_5.py, LEARNINGS #33). Ported 3F's validated archimedean integral into the matrix as a cross-b bilinear block; VALIDATED by T_max-convergence (residual vs the zero-side Gram -> 0, so #32's contamination was the zero-side truncation, not the block); corrected the diagnostic to min eig(A_arch + P_fin + B_pole) (the pencil "balance" wrongly presumed A_arch PD). RESULT: the non-circular Weil form for zeta is POSITIVE, min eig = +0.035 (stable +0.03..+0.05 across K=5..8), computed from the Gamma factor + primes with no zeros. Necessary-not-sufficient (finite-K truncation of the target positivity).
- [x] **Milestone M2.6 (done): general-mu archimedean Bombieri kernel fixed + validated** (e2w_rosati_fourway_M2_6.py, LEARNINGS #34). The constant is C_mu = log pi - psi((1+mu)/2) (the M2.5 control bug was psi(1/2+mu), coincides only at mu=0); verified C_0 = log4pi+gamma, C_1 = log pi+gamma; D-H block residual dropped 5.58 -> 0.12 (validated). BUT the four-way verdict FAILS to separate: min eig(M) = +0.035 (zeta, RH, correct) and +0.094 (D-H, RH-fails, WRONG SIGN). D-H's off-line obstruction (gamma ~ 85.7, ~2.6% of the raw spectrum) sits below the reconstruction-residual floor at reachable b -> the truncated non-circular form is blind to it (the stealth window #18/#19/#27, on the Rosati side). The raw min-eig is necessary-not-sufficient AND non-discriminating.
- [ ] **Milestone M3 (must be ANALYTIC, per M2.6): prove the archimedean-dominates-prime domination engaging the EXACT off-line structure** (the Euler product / Gamma-factor cancellation that distinguishes zeta from D-H below the marginal-positivity floor). A finer numerical truncation will NOT separate zeta from D-H (the signal is below the floor; Schur amplification x30 is answer-side/circular). The non-circular Weil-form infrastructure (correct for any Gamma factor) is complete + validated; this analytic domination is the open problem, where #20/3M always located it. Candidate input: the Arakelov/archimedean Green's-function positivity (2I-2L) as the polarization.

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
- [x] Add bibliography / further reading (references/README.md — 25-PDF library indexed by direction; PDFs gitignored)
- [x] Read-through of the reference library: notes for ALL 26 sources + a synthesis index in docs/03_research/reading_notes/. Top findings: Bhatt-Lurie's Cartier-Witt stack WCart ("de Rham relative to F_1" + global Frobenius F + Sen operator Theta) is the strongest candidate for 2K's F_1 base / Gamma_S / Deninger generator; Connes-Consani 2015 already builds the square N^2-hat with Frobenius correspondences Psi(lambda) but idempotent ops => no signed pairing (the Direction-8 gap isolated); Adiprasito-Huh-Katz give a Hodge-index signature with NO underlying variety (attack 4.A); Deninger/Connes confirm the signature (not the trace formula) is the load-bearing step (K1 wall). The literature independently confirms the 2Q/2R reduction and locates the gap identically to 2K. Notes are full-depth (section-by-section technical content; ~6,200 lines total).
- [ ] Link visualizations to corresponding doc sections
- [ ] Add Jupyter notebooks for interactive exploration
- [ ] Explore L-functions generalization
