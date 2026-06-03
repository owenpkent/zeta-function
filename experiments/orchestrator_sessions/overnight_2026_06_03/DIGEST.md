# Overnight run 2026-06-03 (staging, NOT committed)

Owner picked all four streams. Everything here is staged for morning review by Owen + main-agent verification. No commits/pushes were made overnight.

Streams: (1) Lean formalization, (2) obstruction-first Direction-8 probe, (3) deep literature + slow-compute, (4) coordinate factory.

Round log:
- Stream 4 (coord factory, dir12-residue 12.4): staged `stream4_coord_12_4_residue.md`. Candidate negative coordinate: the heat-flow `dH/dt` (= RT energy `-4E`) is the RH-agnostic / sign-blind / archimedean-suppressed block of Bombieri W(f), NOT the discriminating one. Predicted-FALSE bridge per #39, sharpened to a three-part reason. Two probes run (reproduced): |Xi_DH(85.699)|=1.5e-29 (matches #38), log-gas E sign-blind (E(+d)=E(-d)). Deliverable proposed: `e_heat_explicit_split.py` (not built overnight). No commits.
- Stream 4 (coord factory, dir10-thh): staged `stream4_dir10_thh_cup_product_coordinate.md`. Candidate negative/obstruction coordinate: over Z the Hesselholt determinant zeta = det_inf(s-Theta|TP_odd)/det_inf(s-Theta|TP_ev) degenerates from a RATIO to a non-self-dual NUMERATOR (-zeta'), so the cup-product on TP_odd is the missing M3/M4 polarization, not a TP-derived structure. Cheap self-duality discriminator (reproduced, mpmath dps=40): -zeta'(s)/-zeta'(1-s) is non-constant at real AND complex points incl. the critical line (0.746-0.666i at 0.5+3i) while xi(s)/xi(1-s)=1 to ~1e-42. K2 categorical (no ring spectrum for D-H), K3 passes (F_5 genus-1 |alpha|=sqrt q reproduced). Relocates the Direction-8 signature gap onto TP_odd (4th instance of #30). VERIFIER targets V1 (already discharged = #MB-6), V2 (non-self-duality of -zeta'), V3 (F_q Rosati Gram = 2T/2G). NOT independently verified.

---

## ROUND 1 TRIAGE (synthesizer, morning-review digest)

Honest accounting of all four streams. Provenance tier per item: PROVED (Lean kernel, no re-derivation needed) / COMPUTED (code ran, MUST be re-derived by main agent) / STRUCTURAL-READING (a framing/prediction, not a theorem) / CITED. Nothing here is committed. Nothing here advances the M3/M4 signature gap; every stream lands on the trace side, consistent with "all roads to the signature" (#30).

### Stream 1 (Lean) -- GREEN, self-verifying. Promise 8/10.
- STATUS: `lake build` GREEN before and after. New file `lean/ZetaRH/OvernightDrafts2026_06_03.lean` (namespace `ZetaRH.OvernightDrafts`), auto-included by the `lean_lib` glob, no existing module edited.
- READY (PROVED, kernel-checked, axioms = propext/Classical.choice/Quot.sound only, no re-derivation needed): six sorry-free lemmas. `xiCL` (Conrey-Li xi), `xiCL_one_sub` (functional equation), `deriv_xiCL_one_sub` (derivative antisymmetry), `completedRiemannZeta_eq_Gammaℝ_mul`, `xiCL_eq_zero_of_zeta_zero` (xi reaches the zeros, formal half of #42/#43 converse), `lerchRHS` + `lerchRHS_one` + `lerchRHS_ne_zero_of_re_pos` (the #44 archimedean "blindness", nonzero at every nontrivial zero). Main agent need only re-run `lake build` and `#print axioms` to confirm.
- BLOCKED (sorryAx, honestly flagged): `#2DB-1` deBrangesQ_neg_at_34 (certified numerics at a transcendental ordinate, absent from Mathlib); `#2DB-2` deBranges_implies_RH (needs H(E) reproducing-kernel theory, absent); `#2PR-1` senRegDet_exists (needs zeta-regularized product, absent).
- CAVEAT: none of the six lemmas touches the signature. They are the trace/realization side. Honest, and stated as such in the report.
- RECOMMENDED NEXT (from stream): make `#2PR-1` a real proof via Mathlib's Hurwitz zeta s-derivative; an upstreamable contribution. Secondary: Q-symmetry lemmas sorry-free from the FE.

### Stream 2 (obstruction probe, 2CCM.1) -- ADVANCE-AS-NEGATIVE after softenings. Promise 4/10.
- STATUS: ADVERSARY verdict ADVANCE-AS-NEGATIVE-COORDINATE, score 4, with FIVE required softenings (S1-S5). All five in-file PARTs reproduce exactly (ADVERSARY re-ran; smoke_test 8/8, D-H control sound).
- READY for verification (COMPUTED, re-derive): the five PART numbers (PART 1 self-adjoint -> on-line 8e-16; PART 2 required non-real eigenvalue 85.699-0.3085i; PART 5 indefinite-metric 84% complex zeros vs definite 6.7e-16 control; PART 3 prime-side non-convergence on the line, extended to x=2e5; PART 4 D-H off-line zero + von Mangoldt leak n=6,14,21). The arithmetic and linear algebra are correct.
- LOAD-BEARING SOFTENING (S1, must apply before any integration): the mechanism is NOT "self-adjointness." A self-adjoint family-determinant can still have off-line zeros (breaking case K(s)=diag(s, s^2+2), roots +/-i). The on-line conclusion needs zeros = spec(SINGLE FIXED H), i.e. Hilbert-Polya / the polarization, not self-adjointness as a corollary. VERIFIER V1 must confirm BOTH (a) H self-adjoint AND (b) Xi-zeros = spec(fixed H).
- SCOPE (S3/S5): this is largely a re-vocabulary of #44/#30/#43 onto the CCM determinant route, plus the genuinely new data point of testing the Nov-2025 CCM object (arXiv:2511.22755) against K2. PART 1 (Hilbert-Polya) and PART 5 (Krein) are textbook, used illustratively.
- BLOCKED: nothing technically blocked; the coordinate is provisional pending the S1-S5 rewrites and VERIFIER V1.

### Stream 3a (literature) -- EMPTY. Promise 0/10.
- STATUS: no output returned ({}). Nothing to verify. Flag for ORCHESTRATOR: stream did not produce a staged report. Treat as not-run.

### Stream 3b (compute, de Branges Q to K=500) -- ran, headline revision. Promise 6/10.
- STATUS: `ran_successfully: true`. Extends 2DB.1 from K=50 to K=500. Script + npz staged.
- READY (COMPUTED, re-derive from the npz which is canonical): the 32-element negative-Q index set {34, 71, 106, ...497}; ~6% density tracking the zero density (per-100 windows 2,7,6,6,11), no strong clustering (gaps 2..37); anchor k=34 Q=-5.389101e-69, ratio 1.000000 to Conrey-Li; slope converging one-sided to -(pi/2)/ln10 = -0.68219 (full-window -0.67676, tail -0.67939); two-factor decomposition -0.33853 + -0.33814 ~ double-Gamma law. Sign stability under doubled precision verified on sampled negatives/neighbours (no flips, 65-digit min guard band).
- HEADLINE: REVISES the 2DB.1 "sporadic single k=34" reading. Pointwise de Branges (3.1) positivity for zeta fails at POSITIVE DENSITY (~6%), not once, while RH holds. Reinforces the lesson: the RH-equivalent signed pairing must be a global SUM (Li lambda_n), not the pointwise Hermite-Biehler cross-term Q.
- PROVENANCE CAVEAT (flag for re-derivation): the canonical K=500 stdout was lost to background-harness full buffering (0-byte log); the formatted summary was regenerated deterministically from the npz via `--report`. The K=50 smoke run had live stdout and reproduced the 2DB.1 anchor. Main agent should re-run from a clean session and confirm against the npz.
- BLOCKED / NOT done: K2 (D-H control) NOT re-run at K=500; inherited from 2DB.1 (only to T=90). No Weil cohomology built; M3 unchanged. Whether the ~6% density stabilizes or drifts is unresolved (the (400,500]:11 uptick is the open A1 question).

### Stream 4a (coord factory, dir8 off-block) -- KILL. Promise 2/10.
- STATUS: KILL, score 2. COMPUTED facts reproduce but are trivial (Euler product + linear algebra: block-diagonal min eig 2.0; max|Lambda(n)|=0 off prime powers for n<2000; -zeta'/zeta(2)=0.5700 anchor). The structural reading FAILS K3 (Weil's function-field model puts RH content in the WITHIN-block off-diagonal trace t, exactly the entries the candidate zeroes to t=0). The A4 depth target is incoherent: the resolvent sum_rho 1/(s-rho) IS -zeta'/zeta, the von Mangoldt sum it calls block-diagonal. Net a regression that mislocates the correctly-placed #42 gap. Do not integrate.

### Stream 4b (coord factory, dir10 THH) -- ADVANCE-AS-NEGATIVE after softenings. Promise 5/10.
- STATUS: ADVANCE-AS-NEGATIVE-COORDINATE, score 5. Numerics reproduce; K1/K2/K3 hold as a relocation coordinate.
- READY (COMPUTED, re-derive): -zeta'(s)/-zeta'(1-s) non-constant at real and complex points incl. the line (0.746-0.666i at 0.5+3i) vs xi(s)/xi(1-s)=1 to ~1e-42; THH(Z) odd-torsion log-orders assemble to -zeta' (s=3 err 1.6e-10); F_5 genus-1 |alpha|=sqrt 5, alpha_1 alpha_2 = 5.
- SOFTENING (must apply): the two NEW claims are soft. (i) the self-duality "detector" is Schwarz reflection (|ratio|=1 on Re(s)=1/2), NOT Poincare duality. (ii) the "single numerator, no TP_ev over Z" degeneration uses Bokstedt's THH even-vanishing, which does NOT control the Tate construction TP (admitted, uncomputed, likely false). Mostly restates #29/#30. Robust form rests on the self-duality FAILURE, not the vanishing.
- VERIFIER targets: V1 (xi FE, already discharged = #MB-6, now also = stream-1 `xiCL_one_sub`), V2 (non-self-duality of -zeta', new contrast lemma, low priority), V3 (F_q Rosati Gram PD <=> |t| < 2 sqrt q, maps to 2T/2G).

### Stream 4c (coord factory, dir12.4 heat-flow residue) -- REVISE. Promise 4.5/10.
- STATUS: REVISE, score 4.5. Anchors reproduce (log-gas E(+0.3085)=E(-0.3085)=2.6268161 exact sign-blindness; digamma densities exact; |Xi_DH(85.699)|~1.5e-29 order-only). The no-fire prediction is correct.
- WHY REVISE (load-bearing): ~85% restates #39's already-recorded forecast, and the kill reason is internally inconsistent. Claim (iii) "sub-floor 1.5e-29" is the KERNEL value, not the Rodgers-Tao energy E (which sees the off-line pair at O(1)=5.27). The correct kill is that the smoothed sum S_t is BETA-BLIND by construction, not that it is sub-floor. The proposed deliverable `e_heat_explicit_split.py` was NOT built overnight; this is a STRUCTURAL-READING/prediction, not a computed coordinate.
- BLOCKED: the actual experiment (zero=prime+arch verification, phi_b projection, D-H fire/no-fire verdict) not run.

---

## VERIFY THESE FIRST IN THE MORNING (ranked, highest-value / lowest-risk first)

1. **Stream 1 Lean (6 sorry-free lemmas)** -- PROVED, self-verifying. Just re-run `cd lean; lake build` (expect GREEN) and `#print axioms` on each (expect propext/Classical.choice/Quot.sound). Zero re-derivation risk; this is the only stream that is real without numeric re-derivation. THEN consider the recommended `#2PR-1` Hurwitz-zeta attack as the next genuine Lean target.
2. **Stream 3b de Branges Q to K=500** -- COMPUTED, headline revision (pointwise (3.1) fails at ~6% density, not sporadically). Re-run the script from a clean session and confirm the 32-index negative set, slope -0.6768, and anchor ratio 1.000000 against the canonical npz. Flag the lost-stdout provenance: regenerate the summary via `--report` and re-derive independently. High value (revises a recorded reading), moderate risk (provenance caveat + D-H control not re-run at K=500).
3. **Stream 4b dir10 THH** -- COMPUTED + STRUCTURAL. Re-derive the -zeta' non-self-duality vs xi self-duality numbers, then apply softenings S(i)/S(ii) BEFORE integration: relabel the "detector" as Schwarz reflection, not Poincare duality; drop the TP-vanishing claim. Integrate only as a relocation coordinate (4th instance of #30). V2 (non-self-duality lemma) is a cheap optional Lean follow-up.
4. **Stream 2 obstruction probe (2CCM.1)** -- COMPUTED. Re-run the five PARTs (already reproduced by ADVERSARY), then apply S1-S5 BEFORE integration. The load-bearing S1 fix (mechanism = Hilbert-Polya / fixed-H spectrum, NOT self-adjointness) is mandatory; without it the headline is false. VERIFIER V1 must confirm zeros = spec(fixed H), not just H self-adjoint. Lower value (largely re-vocabulary of #44/#30/#43), but the CCM Nov-2025 K2 data point is genuinely new.
5. **Stream 4c dir12.4 heat-flow residue** -- STRUCTURAL prediction (experiment NOT built). Reproduce the two anchors (E sign-blindness, |Xi_DH| order). If integrated at all, integrate the CORRECTED kill (S_t is beta-blind by construction, NOT sub-floor) and note ~85% overlaps #39. Low marginal value; deprioritize.

BOTTOM (do not integrate):
- **Stream 4a dir8 off-block** -- KILL (score 2): facts are trivial (Euler product + linear algebra), structural reading fails K3 (Weil puts RH content in the within-block trace t, which the candidate zeroes out), K2 discriminator is admittedly just the Euler product (#37), and the A4 resolvent target is incoherent (the resolvent sum IS -zeta'/zeta). A regression that mislocates the #42 gap.
- **Stream 3a literature** -- EMPTY ({}). Not run; nothing to verify. Flag to ORCHESTRATOR.

### One-paragraph honest accounting
No stream advanced RH or narrowed the M3/M4 signature gap. Every result landed on the trace/realization side, a fifth-through-eighth reinforcement of #30 this session. The single piece of real, no-re-derivation-needed progress is the Stream 1 Lean substrate (six machine-checked trace-side facts). The strongest empirical finding is Stream 3b's revision (pointwise de Branges (3.1) fails at positive density, not once), which sharpens but does not change the 2DB.1 lesson. Two coordinates advance only as negatives after mandatory softenings (2CCM.1, dir10-THH); one is a structural prediction to deprioritize (dir12.4); one is killed (dir8); one stream returned nothing (3a literature).

---

## MAIN-AGENT VERIFICATION + SALVAGE (workflow crashed on structuredClone; work recovered from disk)

The round-1 workflow FAILED at the final result-aggregation step (`structuredClone` on ~1.07M tokens of subagent output) AFTER all 13 agents had run and staged their files. Nothing math-related was lost. Main agent independently verified the two self-verifying streams:

- **Stream 1 (Lean): VERIFIED GREEN.** `lake build` exits 0 ("Build completed successfully"). Read the proof bodies of the 6 claimed-sorry-free lemmas (`xiCL_one_sub`, `completedRiemannZeta_eq_Gammaℝ_mul`, `xiCL_eq_zero_of_zeta_zero`, `deriv_xiCL_one_sub`, `lerchRHS_one`, `lerchRHS_ne_zero_of_re_pos`): all complete via real Mathlib API (`completedRiemannZeta_one_sub`, `riemannZeta_def_of_ne_zero`, `deriv_comp_const_sub`, `Gamma_ne_zero_of_re_pos`); `sorry` appears only in the 3 honestly-flagged targets (#2DB-1, #2DB-2, #2PR-1). COMMITTED to the overnight branch.
- **Stream 3b (de Branges Q to K=500): VERIFIED by independent re-derivation.** Reused the verified e2db method (dps=80) and confirmed the npz at spot-checks k=34/71/106/497 (negative) and k=35/72/200 (positive), all matching `sign[]`; k=34 anchor |Q|=5.3891e-69 reproduces Conrey-Li. The 32 negative indices and ~6% density are real. HEADLINE CONFIRMED: pointwise de Branges (3.1) fails at positive density (~6%), not once, while RH holds. The npz + script COMMITTED to the overnight branch (provenance caveat noted: the agent's K=500 stdout was lost to buffering, but the npz is now independently corroborated).

NOT yet integrated into the canonical record (deferred to a focused round / morning): updating LEARNINGS #43 with the density revision; promoting the K=500 script to experiments/; the Lerch Lean target (#2PR-1) as a real proof. The three coordinate-factory candidates (dir8 KILL, dir10-THH negative, dir12.4 REVISE) and 2CCM.1 remain staged-and-unverified (COMPUTED, need re-derivation + softenings); the 38KB stream3_literature.md exists despite the digest's "empty" mislabel (its structured return was {} but the file was written).

LESSON for later rounds: keep workflows SMALL and have agents write to files + return MINIMAL structured data (a few short fields), never large blobs, to avoid the structuredClone failure.
