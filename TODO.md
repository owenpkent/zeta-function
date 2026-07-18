# TODO — Riemann Zeta Function Study Repo

> Consolidated 2026-07-17. This file carries OPEN work only. The full session history (every Done item from 2026-05 onward, plus these open items in their original context) is frozen verbatim in [TODO_ARCHIVE.md](TODO_ARCHIVE.md); "(archive NNN)" pointers below are line numbers there. Convention unchanged: `- [ ]` checkboxes, check items off here; on the next compaction pass rotate checked items into the archive.

## Open — the corridor and its pivot (S4/R1; LEARNINGS #158-#164; exit rule fired + closure RATIFIED 2026-07-17)

- [ ] **THE POST-CORRIDOR PIVOT (the sharpest live coordinate after #163/#164):** attempt the S4 identity clause on the theta/modular-interpolation side (the lattice clause is paid by construction there, per #160's engine reading) and build at the C1 = SP2-and-SP3 counting joint (the SP3c/W6 derived-base rung; [`missing_object_interface.md`](docs/03_research/missing_object_interface.md)). First rungs (SURVEYOR-cheap, also the #164 reopen conditions): (i) Baranov-Borichev-Havin meromorphic model-space majorant theory vs Burnol's $L_a$ (can the majorant machinery be repaired past the codim-2 pole pair at $s = 0, 1$?); (ii) pin the Kulikov-Nazarov-Sodin space definition against the actual growth $\lambda_j \sim \log j$ of $\{k \log p\}$.
- [ ] **Sonin-projector family, RE-SCOPED by #164 (the well-posedness half is MOOT: Carneiro-Littmann is ill-posed on the zeta-loaded branch $L_a$; optional bounded confirmation of falsifiers 1/3 only):** build a Sonin projector / true operator eigenbasis for the CCM carrier (not in any cache; a new experiment) and test (a) the one-sided extremal problem in the Sonin space (Carneiro-Littmann machinery; well-posedness itself open, no literature collision found) and (b) rank behavior at $\{k \log p\}$ against the e1o multiplicity instrument. Screen any candidate against the DMV kill + the repo Beurling fake + D-H unposability ([`s4_carrier_audit.md`](docs/03_research/s4_carrier_audit.md) Section 3 screen).
- [ ] **Rank-one interlacing:** the last untouched #154 upgrade-spec ingredient (2); flagged "the one untouched item" in three consecutive PHASE_STATE updates. Closing it retires the #154 ledger.
- [ ] **SURVEYOR:** (i) pin von Koch 1901 / Schoenfeld 1976 at source (converse half of the Theorem-A iff; not load-bearing for Theorem A itself); (ii) the $\theta \le 1/2$ Beurling corner (the one unsourced DMV-screen escape hatch); (iii) Carneiro-Littmann well-posedness in the CCM Sonin space; (iv) refresh the WATCH sweep ([`sourcing_gap_r1.md`](docs/03_research/sourcing_gap_r1.md) quadruple + Connes/Consani/Moscovici/van Suijlekom submissions + the bilinear-Mobius school + the dBN PF-order line; last full sweep 2026-07-03).
- [ ] **The complex ghost class + the sqrt13 hint (e1n):** heavier-tail read (sigma = 1.6) or a sharper instrument; the dressing-migration question; the corrected-window rerun. Full statement: archive 327 / [`e1n_prime_comb.md`](experiments/spectral/e1n_prime_comb.md).
- [ ] **Lean targets (VERIFIER, all classical, from the e1n/e1o .md):** the corrected abscissa lemma (nonnegative-envelope form only; the pre-fix statement is FALSE); the Abel nonneg upgrade; the $(-1)^n n^{1/4}$ witness; the $\pi/4 - 5/(2t)$ closed form; exp-closure of absolutely convergent Dirichlet series; Lemma L (Landau); $\zeta < 0$ on $(0,1)$ via eta; the $s = 1$ pole cancellation.
- [ ] **Frame-audit follow-ups (2026-07-17):** see [`docs/03_research/ccm_corridor_frame_audit.md`](docs/03_research/ccm_corridor_frame_audit.md) + LEARNINGS #163. Status: falsifiers 2 and 4 DONE same day (#164, [`s4_cheap_falsifiers_survey.md`](docs/03_research/s4_cheap_falsifiers_survey.md); falsifier 2 TRIPPED adversary-verified, exit rule fired conditional on the two pivot-item residuals); falsifiers 1/3 = the optional bounded confirmation above; falsifier 5 (the $\theta \le 1/2$ corner) lives in the SURVEYOR item.

## Open — publications (registry: PUBLICATIONS.md)

- [ ] **P2 (Mathlib PR [#41132](https://github.com/leanprover-community/mathlib4/pull/41132), digamma): ACTIVE, updated 2026-07-17.** Check the fresh reviewer activity and prepare Owen's replies (in his own words per Mathlib AI policy). P1 ([#41133](https://github.com/leanprover-community/mathlib4/pull/41133), `riemannZeta_conj`) is resolved: **merged by Bors 2026-07-07** (GitHub shows state=closed, merged=false; the "[Merged by Bors]" title prefix is mathlib's merge signature). Registry updated; the old "READY: submit" item (archive 190) is superseded.
- [ ] **P10 rational-root floor: open the mathlib4 PR.** CLEAR-TO-PR since 2026-07-02 (#RR-1/#RR-2 machine-checked in full UFD generality). **2026-07-17: port BUILD-VERIFIED against the pinned checkout** (real Mathlib source, disposable branch, green + axiom-clean, then reverted; instance-cycle fix folded in) **+ PR body staged** ([`rational_root_floor_pr_body.md`](lean/upstream/rational_root_floor_pr_body.md), [`rational_root_floor_port.md`](lean/upstream/rational_root_floor_port.md)); remaining steps mechanical (fork branch, paste verified diff, rebuild, lint, open). Sequencing: after P2 round 2 clears.
- [ ] **P9 paired-subtorus note (HUMAN steps):** MathSciNet session; citation pins (GKW author list, Kabluchko volume/pages, Hinkkanen page range); author-name + acknowledgments calls; then the arXiv package (math.CV, cross-list math.CO/math.PR). Draft written and compiling since 2026-07-01.
- [ ] **P11 tameness-trade gates:** expert model-theorist reader; verify remaining FETCH-tagged attributions; keystone-stays-open watch.
- [ ] **P4 next:** an expert reader for the scorecard's (iii) polarization column, then write §4 + a full revision (sequence after P1/P2). (HIGH-1) the Deninger + one prismatic/THH survey read before any "confirmed distinctive" language. (archive 200, 211)
- [ ] **Portfolio decisions (Owen-gated; now out of date with the registry):** the recorded shape {P1, P2, P6 standalone; P3/P5/P7/P8 fold into P4} predates P9/P10/P11 joining as standalone rows. Re-confirm. P5: fold into P4 (recommended) or standalone only with expert confirmation. P6: ship the path-(a) conditional reduction now, and/or budget the unconditional Hasse bound as a real multi-month project. (archive 192, 194, 204)
- [ ] **(MED-5)** apply the K1 circularity gate question retroactively to any future candidate; P4 and P8 are flagged circularity-adjacent. (archive 213)
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
