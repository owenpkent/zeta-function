# Phase State (operational)

> Read by ORCHESTRATOR at the start of every AI-only session. Maintained by SYNTHESIZER. Living document.

## Current state (2026-05-25)

**Active mode**: AI-augmented (with human owner in critical path). Transition to AI-only execution per [`docs/03_research/proof_program_ai_only.md`](docs/03_research/proof_program_ai_only.md) requires infrastructure not yet built (see [`OPERATIONS.md`](OPERATIONS.md) §7).

**Current phase**: Phase 0 (Foundation), substantially complete. Phase 1 (Direction 1, Lambda-blueprints) entered in session 002 with milestone 4.1 having three candidate definitions on the table.

**Phase 0 deliverables done**:
- ✅ Six 2A candidate scorecards (Deitmar, Lorscheid, Borger, Connes, Connes-Consani, Deninger).
- ✅ R-series structural analyses (R1, R2, R2.5, R3, R3.5, R3.6, R3.6.3, R4, R5).
- ✅ 2A_path_forward synthesis.
- ✅ 2C F_1 / Arakelov survey as of 2025.
- ✅ 2D Deninger micro-target identification (M3 prismatic foliation hypothesis).
- ✅ 15 cross-architecture findings in [`experiments/LEARNINGS.md`](experiments/LEARNINGS.md).
- ✅ Eight research directions documented in [`docs/03_research/research_directions/`](docs/03_research/research_directions/).
- ✅ AI-augmented and AI-only proof programs documented.
- ✅ Lean 4 Phase 1 substrate (green build on Lean 4.13.0 + Mathlib v4.13.0; typed definitions with documented VERIFIER target IDs).
- ✅ Agent role specifications in [`.claude/agents/`](.claude/agents/).
- ✅ Operations guide ([`OPERATIONS.md`](OPERATIONS.md)).

**Phase 0 deliverables remaining**:
- ⏳ Independent expert verification of the 2A scorecards (HUMAN: requires expert correspondents).
- ⏳ Identify expert correspondents in arithmetic geometry, NCG, prismatic cohomology (HUMAN).
- 🟡 Lean 4 / Mathlib expansion: PHASE 1 SUBSTRATE landed (2026-05-25) and BUILD IS GREEN. The placeholder `True`/`Unit` skeleton has been upgraded to typed data wired to Mathlib `riemannZeta`, real complex-analytic L-functions, real bivariate cosine polynomials, and typed Lambda-blueprint axioms. `lake build` succeeds end-to-end on Windows 11 with Lean 4.13.0 + Mathlib v4.13.0 (all 2250 modules compile; warnings are exactly the documented `sorry` markers). See [`lean/README.md`](lean/README.md) for the VERIFIER target ID table (#FE-1..#MB-6). Full proof closure remains multi-year.

**Architectures 1, 3, 4 status**: substantially closed at the project level.
- Arch 1 (spectral): 1A-1C complete; 1D literature pending.
- Arch 3 (positivity): complete through 3B.3 rigorous Li witness at n = 336,000 + 3F-3I Weil-form duality cross-cuts + 3J Schur-complement two-clock decomposition (asymptote -78.7%, sharpens raw Gram detector by ~30x) + 3K hypothetical-off-line-zero perturbation (disproof in Gram-matrix family has no leverage point) + **3L Epstein second control (session 003): the Weil-form Schur detector obeys the same counting law (schur_neg = #off-line heights) on a structurally independent off-line construction (Epstein zeta of disc -47), generalising the wrong-approach discipline beyond D-H** + **3B.4 second Li-criterion off-line witness (Epstein lambda_n crosses negative at n = 110,000) plus rigorous Selberg-vs-off-line discrimination.**
- Arch 4 (analytic): complete through 4E.8 SDP saturation + 4A+4C V-K dossier + **4E.9 Heath-Brown multi-zero MT SDP (session 003, Direction 7): the multi-zero MT shape factor does NOT exceed the 1D Fejer ceiling (best ratio <= 1, optimal certificate rank 2). The LP/SDP/SOS family is now fully closed.** Remaining research-grade escape: Bombieri variational SOS (Direction 6).

## Compute budget

| Item | Used | Budgeted | Remaining |
|---|---|---|---|
| Project sessions to date | ~50-100 (estimate) | unbounded (project-level) | n/a |
| Lean 4 proofs landed | 1 (RHMathlib_iff_RH_zeta) + Phase 1 typed substrate | per-direction (see Directions 1-8) | substantial |
| Mathlib contributions | 0 | 5-10 person-years | substantial |

## Recommended next session actions

**See [`experiments/orchestrator_sessions/session_005.md`](experiments/orchestrator_sessions/session_005.md) for the latest (session-005) narrative: 2Q (the place-dependent bidegree obstruction) + the Lean Weil-explicit-formula thread. [`session_004.md`](experiments/orchestrator_sessions/session_004.md) has the prior arc.**

Session 004 (2026-05-28/29) completed the SINGLE-arithmetic-surface side of Direction 8: the place-type Weil-form decomposition (3M), the function-field Hodge index as a signature (2G), and over Spec(Z) the Faltings-Hriljac positive-definite height pairing at ranks 1-4 (2H/2M) plus the COMPLETE, authoritatively-validated local-height decomposition (2I archimedean incidence, 2L Petersson self-incidence, 2P Silverman finite+real = h_hat). 2K is the dictionary mapping all of this to the would-be `Spec(Z) x Spec(Z)` intersection form; 2K sec 6b has the 2026 literature state. Lean: 2G signature theorem machine-proved, 2H stated (build green).

Recommended next steps (in priority order):

1. **The product surface (the real target).** Everything that lives on a SINGLE arithmetic surface is now in hand and validated. The only missing object is `Spec(Z) x Spec(Z)` and its Frobenius correspondence (2K sec 4). Concretely: pursue Directions 1-4 (Lambda-blueprints / prismatic) with the now-SPECIFIED goal -- construct `S` whose intersection form is the Weil-form Gram `A_arch + P_fin + B_pole` with `B_pole` (the pole of zeta at s=1) as the hyperbolic `(+1)` direction; or push the Morishita Deninger<->Connes-Consani bridge (arXiv:2508.15971, now in Munster J. Math.; bridges the two frameworks for ABELIAN number fields via arithmetic topology but constructs NO pairing) toward an actual intersection pairing. **Sharpened in-session (2Q, LEARNINGS #25):** the missing correspondence `Gamma_S` is now specified down to its bidegree -- place-dependent `(1, p)` per prime (vs the FF single-scale `(1, q)`), forcing infinite-dim `H^i` and the `R`-flow as consequences, and pinning `Gamma_S^2` to the regularized von Mangoldt prime sum (the Direction 4.6 determinant). The concrete next computable step is Direction 4.6: build `det_zeta(s - Phi_t | H^*_{F,pr})` and verify it reproduces the Euler product -- the first place the `(1,p)` bidegree becomes an honest regularized intersection number.
2. **Finish T3 cleanly (optional, low priority).** 2P already achieves T3's intent via the authoritative algorithm; the theta cross-check (e2n, BLOCKED) is now confirmatory-only.
3. **Lean.** The Weil explicit formula + positivity criterion have a green typed SCAFFOLD (`ExplicitFormula.lean`, #EF-1/#EF-2, session 005). Done in-session: #MB-1/#MB-2/#MB-6 discharged to real proofs; `digamma`/`archKernel` concrete (#EF-arch kernel). Next Lean rungs, in order of tractability: (a) upstream `digamma` to Mathlib proper + prove its basic identities (recurrence `ψ(s+1)=ψ(s)+1/s`, reflection); (b) state and prove a concrete `archTerm`/integral pairing (#EF-class) once a Fourier/Mellin transform is fixed; (c) the genuine #EF-1 (explicit formula) and #EF-2 (Weil criterion) -- multi-step, need sum-over-zeros theory; (d) the 2H Faltings-Hriljac dependencies if/when Mathlib gains canonical heights.
4. **Remote autonomy infrastructure.** The `/schedule` remote agent did NOT push (cloud env lacks repo write access); the routine is disabled. Before relying on unattended runs, grant the cloud environment write/PR access and TEST one push.

## Falsifiability triggers (per proof_program_ai_only.md §4)

- Phase 0 reveals R3.5 too narrow: ✅ NOT triggered (R3.5 structural content now formally verified in Lean as of session 002).
- Phase 1 fails at milestone 4.1 (no consistent F-F definition): ✅ NOT triggered (three candidates produced; A=B, C strict refinement; all three pass K2).
- Phase 1 fails at Lambda-Blpr fiber products (milestone 4.5): NOT YET TESTED.
- Phase 2 fails at prismatic foliation hypothesis: NOT YET TESTED.
- Phase 3 fails at intersection product: NOT YET TESTED.
- Phase 4 fails after 5 calendar years of parallel Hodge index attempts: NOT YET TESTED.

## Pending agent outputs

Session 002 outputs landed: three F-F candidates ([A](experiments/arithmetic_geometric/D1_4_1_fermat_frobenius_candidate_A.md), [B](experiments/arithmetic_geometric/D1_4_1_fermat_frobenius_candidate_B.md), [C](experiments/arithmetic_geometric/D1_4_1_fermat_frobenius_candidate_C.md)) plus R3.5 verification ([diagnostic](experiments/orchestrator_sessions/r3_5_verification_attempt.md), [updated Lean](lean/ZetaRH/R3_5.lean)). Awaiting session 003 deployments: VERIFIER-1A/B/C on the F-F candidates' Lean targets, plus ADVERSARY on D-H exclusion across all three.

## Last verified state

- Git commit: `6e42aa7` (session 005; through the digamma recurrence, committed, not pushed). Uncommitted: 2R ([e2r_dynamical_zeta](experiments/arithmetic_geometric/e2r_dynamical_zeta.md), LEARNINGS #26) -- the Ruelle dynamical-zeta realization of `Gamma_S^2` (`-zeta'/zeta`, orbit lengths `{log p}`; D-H has no orbit spectrum) + LEARNINGS/2Q/PHASE_STATE updates. Six Lean+math commits local; 2R uncommitted.
- LEARNINGS.md last finding: #25 (the place-dependent bidegree obstruction: `Gamma_S` is a `(1,p)`-per-prime correspondence, from which infinite-dim `H^i` + the `R`-flow follow and `Gamma_S^2` is pinned to the von Mangoldt prime sum); previously #24 (complete single-arithmetic-surface Hodge-index picture: ranks 1-4 PosDef + full Silverman local decomposition = h_hat). Session 004 added #20 (input-side place-type / Euler fingerprint), #21 (2G function-field signature = Hasse-Weil), #22 (2H Faltings-Hriljac over Spec(Z)), #23 (2I archimedean local height), #24.
- Direction 8: function-field template (2G) + arithmetic single-surface (2H/2I/2L/2M/2O/2P) complete and validated; the dictionary + lift gap in 2K. Remaining: the product surface `Spec(Z) x Spec(Z)` + Frobenius.
- Lean: `lake build` green on Lean 4.13.0 + Mathlib v4.13.0; 2G `negDef_iff_hasseWeil` machine-proved (no sorry), 2H Faltings-Hriljac stated (documented sorry). Earlier R3.5 sorry eliminated (session 002).

## Session log (recent)

| Date | Session focus | Commits | Key outputs |
|---|---|---|---|
| 2026-05-29 | Session 005: the product surface (Direction 8) -- sharpen the `Gamma_S` spec; then Lean explicit-formula scaffold; then 2R dynamical realization | `1b4701d`..`6e42aa7` + TBD | **2R** ([e2r_dynamical_zeta](experiments/arithmetic_geometric/e2r_dynamical_zeta.md), LEARNINGS #26): the Ruelle dynamical-zeta realization of `Gamma_S^2`. Orbit lengths `l(gamma_p)=log p` (= 2Q place-weights); `prod_p (1-p^{-s})^{-1}=zeta` and `sum_n Lambda(n)n^{-s}=-zeta'/zeta=Gamma_S^2` (verified to 2e-4 at s=2). D-H control: `Lambda_DH` delocalizes off prime powers (37.4 vs 36.9, first at n=6), so no closed-orbit spectrum -> no flow (dynamical K2). Makes the Deninger half of the Morishita bridge concrete; explicitly NOT a new RH route (spectrum, not signature). **Lean**: new `ExplicitFormula.lean` -- the highest-leverage Mathlib target (LEARNINGS #17). Weil explicit formula bundle for ζ (`weil_explicit_formula_zeta`, #EF-1) + the Weil positivity criterion (`weil_positivity_criterion`: `weilForm`-positivity ⟺ `RiemannHypothesis zeta`, #EF-2). Prime side `primeSum` CONCRETE via Mathlib `vonMangoldt`; spectral/arch/pole bundled. Build GREEN (3 documented sorries + structural targets #EF-arch/#EF-class/#EF-K2). The Architecture-3 face of the positivity whose Architecture-2 face is `HodgeIndex.negDef_iff_hasseWeil`. **2Q** ([e2q_frobenius_bidegree](experiments/arithmetic_geometric/e2q_frobenius_bidegree.md)): the place-dependent BIDEGREE obstruction. The single sharpest break from the FF template: `Gamma` is a `(1,q)` correspondence with ONE scale, but `Gamma_S` over Spec(Z) has bidegree `(1,p)` per prime (no single `q`; scale spread diverges). DERIVES Deninger's two headline features (infinite-dim `H^i`, `R`-flow not `Z`-action) as consequences, PINS `Gamma_S^2` = regularized von Mangoldt prime sum = Direction 4.6 determinant (adjunction input `12 h_Fal` from 2J/2L), and recasts K2 as a bidegree statement (`(1,p)` local bidegree = Euler factor; D-H has none). Verified the Morishita bridge paper (arXiv:2508.15971): bridges the two frameworks for abelian number fields but builds no pairing. LEARNINGS #25; 2K sec 4 sharpened. Illustration not proof (by design). |
| 2026-05-29 | Session 004 cont.: complete the single-arithmetic-surface Hodge-index picture (2L/2M/2O/2N/2P) + Lean + remote-autonomy lessons | 62b4717, fbba5dd..8cd4096 | **Lean**: 2G `negDef_iff_hasseWeil` (Hasse-Weil = negative-definite signature) MACHINE-PROVED, 2H Faltings-Hriljac stated; build green. **2M** rank-4 Hodge index PosDef (234446a1), ranks 1-4 confirmed. **2L** archimedean self-intersection (Petersson norm of Delta), gates pass (j(tau)=j(E) 1e-51, SL2Z 1e-50). **2O** bad-prime: I_1 => identically 0 (closes 2I caveat); I_2 => Z/2 component periodicity. **2P** AUTHORITATIVE Silverman local heights (Cohen 7.5.6/7.5.7, Cremona 3.4, from owner-supplied books): h_inf + sum_p h_p = h_hat validated all curves/multiples (resid to 1e-8); confirms 2I normalization, corrects 2O attribution, achieves blocked-T3 intent. **2N** theta cross-check BLOCKED honestly (gate failed, not claimed; superseded by 2P). **2K/2J** the Spec(Z)xSpec(Z) dictionary + Arakelov adjunction + 2026 literature (Deninger<->Connes-Consani bridge). LEARNINGS #24. PROCESS: overnight ScheduleWakeup loop did NOT fire (session-bound); /schedule remote agent did NOT push (cloud env lacks repo write access, routine disabled) -- in-session gated work is the proven reliable path. |
| 2026-05-28 | Session 004: attack from `new_mathematics.md` framing -> 3M (input-side place-type) then 2G (open Direction 8) | b0c6e77, 18483e2, fbba5dd | **3M** input-side place-type decomposition of the Weil form (M = A_arch + P_fin + B_pole, computable from Gamma factor + Dirichlet coefficients, no zeros): finite/pole blocks validated vs 3F; Euler-product fingerprint (Lambda_L delocalizes off prime powers iff no Euler product; zeta 0, D-H 64 from n=6); decisive control via Epstein class-number ladder shows composite support detects NON-EULER not RH-failure (reformulation trap, failure mode #5); arch block has diagnosed ~0.06 normalization gap; cancellation finding sharpens marginal positivity. LEARNINGS #20. **2G** opens Direction 8: Hodge index on C x C as a SIGNATURE -- full Gram (1,3), primitive negative definite, = Hasse-Weil bound, exact across genus 1-2; the non-circular signature-side counterpart to 3M's circular trace-side; names the precise Spec(Z) lift gap. LEARNINGS #21; Direction 8 status updated. **2H** arithmetic Hodge index over Spec(Z): Neron-Tate height pairing on E(Q) positive definite (rank 1,2,3; regulators match LMFDB 0.05111/0.15246/0.41714); the Faltings-Hriljac signature, validated. With 2G completes the signature picture on both sides of the FF/NF divide. Honest caveat: naive coordinate split assigns archimedean place ~0 canonically; true sigma-function local height is the deferred next step. LEARNINGS #22. **2I** genuine archimedean Neron local height: self-DERIVED the Tate telescoping series (not transcribed), VALIDATED against LMFDB h_hat to 1e-5 (caught + corrected the documented factor-of-2). Result: integral generators are 100% archimedean on the diagonal, but the archimedean pairing alone goes indefinite by rank 3 -- positivity is GLOBAL (archimedean diagonal + finite off-diagonal glue), the arithmetic-geometry face of 3M's two-clock balance. LEARNINGS #23. Session 004 total: 8 commits (3M place-type; 2G/2H/2I Direction-8 signature on both sides of the FF/NF divide, archimedean role pinned). |
| 2026-05-28 | Session 003: four gap-closing experiments (A/B/C/D) | TBD | New `experiments/_shared/epstein_zeta.py` (Epstein zeta as independent second control, validated to 1e-31). 3L: Schur detector generalises beyond D-H (Epstein disc -47, schur_neg = #off-line heights, clean PASS). 3B.4: second Li off-line witness (Epstein neg at n=110,000) + rigorous Selberg discrimination. 2F: function-field RH bound |alpha|=sqrt(q) exact across curve/field family. 4E.9: multi-zero MT SDP does not beat Fejer (Direction 7 closes, rank-2). LEARNINGS #19-#22 added. Repo framing recast from defeatist to directional. |
| 2026-05-25 | Session 002: three BUILDERs on milestone 4.1 + VERIFIER on R3.5 | TBD | Three F-F candidates (A blueprint-relation, B Adams quotient, C delta-ring); R3.5 structural content proved by `rfl` after refactor into TraceFormulaNCG framework; build green; one sorry eliminated; LEARNINGS #16 (A=B<C triality) and #17 (Weil explicit formula gap) added |
| 2026-05-25 | Lean Phase 1 substrate + green build | `8a6c3d7` | Six modules upgraded from True/Unit placeholders to typed Mathlib-wired data; MathlibBridge.lean added; 14 VERIFIER target IDs tabulated; lake build green (Lean 4.13.0 + Mathlib v4.13.0) |
| 2026-05-25 | Arch 4E.8 SOS-SDP | `565de36` | Closes LP/SDP family escape from 4E.3 |
| 2026-05-25 | Arch 2C F_1/Arakelov survey | `fd020fc` | 280-line landscape survey |
| 2026-05-25 | Plan Why-section expansion | `a28f106` | Operational framing of project |
| 2026-05-25 | Arch 2D Deninger micro-target | `10c9f05` | M3 prismatic foliation hypothesis identified |
| 2026-05-25 | Arch 2A R3.6.3 CC infrastructure | `3a3f4e3` | Connes-Consani as geometric route infrastructure |
| 2026-05-25 | Arch 3B.3 rigorous Li witness | `30d32aa` | n = 336,000 first rigorous negativity |
| 2026-05-25 | Proof program + 8 directions | `d8a0193` | Operational + research-grade plans |
| 2026-05-25 | AI-centric plan + program | `f951298` | AI division of labor documented |
| 2026-05-25 | AI-only variant | `1928c08` | Speculative AI-only execution variant |
| 2026-05-25 | Agent substrate (pending) | TBD | This commit |

## How to update this file

- ORCHESTRATOR: update "Recommended next session actions" at session end.
- SYNTHESIZER: update everything else after agent outputs land.
- Always update "Last verified state" with the latest commit hash.
- Always update "Session log" with the latest session's work.
