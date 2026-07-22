# TODO — Riemann Zeta Function Study Repo

> Consolidated 2026-07-17. This file carries OPEN work only. The full session history (every Done item from 2026-05 onward, plus these open items in their original context) is frozen verbatim in [TODO_ARCHIVE.md](TODO_ARCHIVE.md); "(archive NNN)" pointers below are line numbers there. Convention unchanged: `- [ ]` checkboxes, check items off here; on the next compaction pass rotate checked items into the archive.

## Open — the corridor and its pivot (S4/R1; LEARNINGS #158-#164; exit rule fired + closure RATIFIED 2026-07-17)

- [x] **THE POST-CORRIDOR PIVOT, FIRST RUNGS EXECUTED 2026-07-17/18 (#166/#167/#168):** both survey rungs discharged the #164 reopen conditions (BBH NOT-REPAIRABLE-AS-SEARCHED; KNS fits-in-part with zero S4 content), and both builds landed on their pre-registered walls nameably: e2al (C1/SP3c, 27/27: the index-only $F/V$ layer Beurling-blind by literal test, arithmetic size entering ONLY at the truncation boundary, $f_{TC}$ non-multiplicative across seven natural variants) and e1q (theta wrap, 25/25: lattice-alone gives only conditioning mirages, hardening monotonically through $M = 154$). Both walls point at the SAME missing tie: the additive lattice bound to the multiplicative structure.
- [ ] **NEXT PIVOT RUNGS (from #166/#167/#168):** (a) the modular/Hecke corpus sweep vs the S4 spec (Cohn-Elkies / Viazovska / Radchenko-Viazovska; the lattice-times-Euler tie IS what modular forms are; zero repo mentions before the frame audit); (b) the $HB_1$ one-sided extremal-theorem question ($\kappa = 1$ at candidate tier, [`la_negative_square_check.md`](docs/03_research/reading_notes/la_negative_square_check.md); also verify the local kernel ansatz against Burnol's literal bilinear extension); (c) the C1 metric-ingredient question (what supplies $\log p$ as SIZE past the e2al boundary leak).
- [ ] **The e1u rung (#170, sibling of the modular/Hecke rung): the trace-normed canonical-system chain embedding.** Build the finite Hamiltonian chain from the ghost-quotiented nested matrices (the e1s Cauchy-compression nesting is the finite germ), embed in the compact space of trace-normed Hamiltonians (Hur 1501.01268 at source; the $H \mapsto m$ homeomorphism), and measure the two ENTANGLED relocated clauses: (a) identification of the limit chain (= the #160 pin, lattice site) and (b) no-mass-escape of the limit Hamiltonian (Euler site; alone Beurling-satisfiable, so discrimination-free by itself). Named builder-must-fix: the indivisible-tail embedding normalization of a finite chain into the compact space. The T1f lead rides along: does the gauged zeta/D-H measure-face separation (fneg_q 0.028 vs 0.05+) persist or close with $\lambda$, and can the deep-dressed mass collapse (sum$|a_q|$ down to 0.0017) be controlled without consuming the identification (Prokhorov on normalized measures is the clean framing). Pre-registered adversary question: reformulation-not-reduction (statement-level equivalence of clause (b) to uniform det-class control was attacked in #170 and did NOT land; the residual risk is price-level). Full spec: [`trojan_horse_m4.md`](docs/03_research/trojan_horse_m4.md) Section 6 + [`e1t_compact_class_limit.md`](experiments/spectral/e1t_compact_class_limit.md) handed-forward.
- [x] **Sonin-projector family: half (b) DONE via the parallel line (2026-07-12 work, merged 2026-07-22 as LEARNINGS #169, [`e1r_sonin_projector.py`](experiments/spectral/e1r_sonin_projector.py) 10/10, adversary PASS_WITH_FIXES):** the carrier's OWN spectral data (Weil energy eigenbasis, non-orthogonal $D_{\log}$ eigenbasis, discrete central-window Sonin projection, E-map shift-sum proxy) supplies NO S4 mechanism; the one rank drop is a spatial-window mirage confirmed by execution; `s4_spec_answer = NEGATIVE, closed for every buildable family`. This is the bounded confirmation #164 left optional, so the corridor closure is DOUBLE-CONFIRMED. Half (a) stays MOOT per #164. Residual (optional only, low priority): the faithful metaplectic self-dual Sonin projector of arXiv:2310.18423, the sole unbuilt variant.
- [x] **Rank-one interlacing: DONE 2026-07-17** ([`e1p_rank_one_interlacing.py`](experiments/spectral/e1p_rank_one_interlacing.py), LEARNINGS #165, adversary PASS_WITH_FIXES): measured family-uniform profile ($\le 2$, one $\sqrt{13}$ point at 3, D-H-blind, not a theorem instance by the twisted-inner-product caveat); lands on the #143 side; the rank-$\le 2$ pole block is the one genuine Weyl/Cauchy instance, input-faithful but RH-blind. **The #154 ledger is fully retired.** REPLICATED independently on the parallel line (#169, [`e1s_rank_one_interlacing.py`](experiments/spectral/e1s_rank_one_interlacing.py) 14/14, run 2026-07-12 without knowledge of this run): same $\le 2$ profile, same single $\sqrt{13}$ exception cell.
- [ ] **Reconcile the e1s vs #165 interlacing verdicts (cheap, one look):** #169/e1s grades Weyl-on-$Q$ ($Q_\zeta = Q_{\rm entire} + P$, $\mathrm{rank}(P)=2$) as a RIGOROUS $\le 2$; #165/e1p grades the profile not-a-theorem-instance via the twisted-inner-product caveat. Decide whether the caveat undercuts the Hermitian-$Q$ reading or only the non-normal $M$-shadow.
- [ ] **The D-H undercount look (#169, one look):** WHY does D-H undercount the lattice by 1-2 (genuine, ghost-free) at $\lambda \in \{3.3, 3.6, 4.0, 4.5\}$ while zeta-OFF stays exact at $\sqrt{13}$? Adversary-found in the e1s round; mechanism uncharacterized.
- [ ] **SURVEYOR:** (i) pin von Koch 1901 / Schoenfeld 1976 at source (converse half of the Theorem-A iff; not load-bearing for Theorem A itself); (ii) the $\theta \le 1/2$ Beurling corner (the one unsourced DMV-screen escape hatch); (iii) Carneiro-Littmann well-posedness in the CCM Sonin space; (iv) WATCH sweep refreshed 2026-07-18 ([`watch_sweep_2026-07-18.md`](docs/03_research/reading_notes/watch_sweep_2026-07-18.md): 14 papers, 0 load-bearing, Groskin 2607.02828 the one ADJACENT-WATCH; next cadence ~2026-08-01); (v) small #170 hardening item: source-read Remling's book Section 5.2 / Cor. 5.8 (the trace-normed compactness + $H \mapsto m$ homeomorphism are currently carried by Hur 1501.01268 at source plus the Forester-Remling citation; the survey's one remaining tag).
- [ ] **The complex ghost class + the sqrt13 hint (e1n):** heavier-tail read (sigma = 1.6) or a sharper instrument; the dressing-migration question; the corrected-window rerun. Full statement: archive 327 / [`e1n_prime_comb.md`](experiments/spectral/e1n_prime_comb.md).
- [ ] **Lean targets (VERIFIER, all classical, from the e1n/e1o .md):** the corrected abscissa lemma (nonnegative-envelope form only; the pre-fix statement is FALSE); the Abel nonneg upgrade; the $(-1)^n n^{1/4}$ witness; the $\pi/4 - 5/(2t)$ closed form; exp-closure of absolutely convergent Dirichlet series; Lemma L (Landau); $\zeta < 0$ on $(0,1)$ via eta; the $s = 1$ pole cancellation. UPDATE (#169 merge): five e1o-side classical targets are ALREADY machine-checked in [`S4Carrier.lean`](lean/ZetaRH/S4Carrier.lean) (#S4C-1 Euler-gate nonnegativity via `vonMangoldt_nonneg`; #S4C-2 tail-divergence kernel modulo the named Chebyshev EXTERNAL hypothesis; #S4C-3 structural-nil span; #S4C-4 decimation rank-1 collapse; #S4C-5 trig-Vandermonde nonsingularity); check overlap before re-formalizing.
- [ ] **Frame-audit follow-ups (2026-07-17):** see [`docs/03_research/ccm_corridor_frame_audit.md`](docs/03_research/ccm_corridor_frame_audit.md) + LEARNINGS #163. Status: falsifiers 2 and 4 DONE same day (#164, [`s4_cheap_falsifiers_survey.md`](docs/03_research/s4_cheap_falsifiers_survey.md); falsifier 2 TRIPPED adversary-verified, exit rule fired conditional on the two pivot-item residuals); falsifiers 1/3 = the optional bounded confirmation above; falsifier 5 (the $\theta \le 1/2$ corner) lives in the SURVEYOR item.

## Open — publications (registry: PUBLICATIONS.md)

- [ ] **P2 (Mathlib PR [#41132](https://github.com/leanprover-community/mathlib4/pull/41132), digamma): ACTIVE, updated 2026-07-17.** Check the fresh reviewer activity and prepare Owen's replies (in his own words per Mathlib AI policy). P1 ([#41133](https://github.com/leanprover-community/mathlib4/pull/41133), `riemannZeta_conj`) is resolved: **merged by Bors 2026-07-07** (GitHub shows state=closed, merged=false; the "[Merged by Bors]" title prefix is mathlib's merge signature). Registry updated; the old "READY: submit" item (archive 190) is superseded.
- [ ] **P10 rational-root floor: open the mathlib4 PR.** CLEAR-TO-PR since 2026-07-02 (#RR-1/#RR-2 machine-checked in full UFD generality). **2026-07-17: port BUILD-VERIFIED against the pinned checkout** (real Mathlib source, disposable branch, green + axiom-clean, then reverted; instance-cycle fix folded in) **+ PR body staged** ([`rational_root_floor_pr_body.md`](lean/upstream/rational_root_floor_pr_body.md), [`rational_root_floor_port.md`](lean/upstream/rational_root_floor_port.md)); remaining steps mechanical (fork branch, paste verified diff, rebuild, lint, open). Sequencing: after P2 round 2 clears.
- [ ] **P9 paired-subtorus note (HUMAN steps):** MathSciNet session; citation pins (GKW author list, Kabluchko volume/pages, Hinkkanen page range); author-name + acknowledgments calls; then the arXiv package (math.CV, cross-list math.CO/math.PR). Draft written and compiling since 2026-07-01.
- [ ] **P11 tameness-trade gates:** expert model-theorist reader; verify remaining FETCH-tagged attributions; keystone-stays-open watch.
- [ ] **P4 next:** an expert reader for the scorecard's (iii) polarization column, then write §4 + a full revision (sequence after P1/P2). (HIGH-1) the Deninger + one prismatic/THH survey read before any "confirmed distinctive" language. (archive 200, 211)
- [ ] **Portfolio decisions (Owen-gated; now out of date with the registry):** the recorded shape {P1, P2, P6 standalone; P3/P5/P7/P8 fold into P4} predates P9/P10/P11 joining as standalone rows. Re-confirm. P5: fold into P4 (recommended) or standalone only with expert confirmation. P6: ship the path-(a) conditional reduction now, and/or budget the unconditional Hasse bound as a real multi-month project. (archive 192, 194, 204)
- [ ] **(MED-5)** apply the K1 circularity gate question retroactively to any future candidate; P4 and P8 are flagged circularity-adjacent. (archive 213)
- [ ] **Mathlib upstream candidate (#169): the Chebyshev $\psi(x) \ge c\,x$ lower bound.** Mathlib has no directly usable form; [`S4Carrier.lean`](lean/ZetaRH/S4Carrier.lean) #S4C-2 carries it as an honest EXTERNAL hypothesis. Formalizing it upstream would let #S4C-2 stand unconditionally (pairs naturally with the P10 PR workflow).
- [ ] **Citation-check target #5 RE-RUN** (the inverted Kaplan-Shelah FETCH catch): previously recorded only inside a checked archive item (archive 223) with no open checkbox of its own; given one here so it cannot be silently lost.

Drift notes (2026-07-17 audit): archive 195 (P8 lit-check) was already DONE 2026-06-16 (verdict: no standalone novelty, fold into P4 Pillar 3). Archive 351 ("Formalize RH equivalences in Lean 4") was done long ago ([`RHEquivalences.lean`](lean/ZetaRH/RHEquivalences.lean), LEARNINGS #64). Both stay checked-off context in the archive.

## Open — research (standing, older threads; full statements at the archive pointers)

- [ ] **Direction 8, the real gap:** construct the global Frobenius/Lefschetz signed trace pairing over Spec(Z) that supplies the trace t (= Spec(Z) x Spec(Z) + Gamma_S). Construction work in arithmetic geometry, not a compute task. (archive 152)
- [ ] **The local-to-global Weil cohomology** (M3/#25, Direction 8's central open step); the pairing must be RH-EQUIVALENT (a sum like $\lambda_n$), not the de Branges cross-term. (archive 258)
- [ ] **The 9A AHK arithmetic-lattice BUILDER target** (P1-P5 build; P6 = M4 left open; the 9A.3 function-field shadow is the same-day kill). (archive 261)
- [ ] **MC.4 residual: the per-block coupling** (the global Frobenius/Lefschetz signed-trace pairing that forces $|t_p| < 2\sqrt{p}$ from the modular flow, sourced not propagated). (archive 271)
- [ ] **The arithmetic q-lift:** deform the mixed-volume form (or build a Weil cohomology of the C-C square) whose $\Delta.\Gamma$ is the point count $q + 1 - t$; the (1,p) bidegree (2Q) is where t must inject. (archive 253)
- [ ] **Product-surface intersection signature:** geometricize the M_euler trace-side positivity as a Hodge index on Spec(Z) x Spec(Z) via WCart or N^2-hat. (archive 251)
- [ ] **Lever B O1 (months, FLT-adjacent):** the rank-2 integer Frobenius representation A feeding `hasse_of_matrix`; plan in [`lever_b_function_field_plan.md`](docs/03_research/lever_b_function_field_plan.md). (archive 279)
- [ ] **Model-theoretic Frobenius Lean ladder:** T2 CompatibleRing/Los transport (multi-day, feasible); T4 BLOCKED-ON-MATHLIB (saturation machinery absent); ADVERSARY residual A3. (archive 219-222)
- [ ] **Lean (VERIFIER) remaining: V4 + the unconditional pair** (B1 G_log rigidity assembly; the slope-1 lemma; the flat-comb exclusion as the first FiniteCertificates-style EF-positivity theorems). (archive 179)
- [ ] **Toy sandbox:** the H2 mesh-min-monotonicity conjecture (possible small proof); VT-PS1..4 Lean targets (Vieta form of Lemma E first); the SC next rung (genus-2 `cohn_criterion` instantiation and/or its Mathlib PR). (archive 236-238)
- [ ] **Workaround slate, remaining follow-ons:** e3bb/e3cc exact-rational c_6 dual + ghost-crystal search; e3ee decimation bifurcation; e3ff two-prime exact identity; certificate PSLQ miner; Lean FiniteCertificates export. (archive 180)
- [ ] **ECC e1x spectral-leakage experiment** (truncated prime crystal as a transfer recursion; kills ECC clause E3 on leakage; interval-arithmetic J-contractivity rider). (archive 164)
- [ ] **e3x rung 7** (corrected protocol only: Q fixed via $h \sim L^{-3/2}$, gain-normalized c/eps, zero-tolerance intercept). (archive 175)
- [ ] **12.4' Gaussian-smoothed explicit-formula route** (low prior; predicted FALSE by the #38 suppression law). (archive 260)
- [ ] **R3.6.3:** Connes-Consani machinery as INFRASTRUCTURE for the geometric route (topos/sheaf tools for intersection theory despite the K1-failing positivity formulations). (archive 297)
- [ ] **Arakelov standing directive:** do NOT run a fourth Arakelov front or survey; spend on isolable RH-independent sub-pieces + watch for an external Gamma_S/polarization theorem. (archive 317)

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
- [ ] Add glossary of terms
- [ ] Link visualizations to corresponding doc sections
- [ ] Add Jupyter notebooks for interactive exploration
- [ ] Explore L-functions generalization

## Housekeeping

- [ ] Rotate checked items from this file into TODO_ARCHIVE.md periodically; keep this file open-only.
- [ ] Keep `python -m experiments.run_all_tests` green after every merge (added 2026-07-17).
