# Overnight ORCHESTRATOR plan (session 004 -> 005), started 2026-05-28 night

> Autonomous run while the owner sleeps. Driven by the ORCHESTRATOR loop
> (ScheduleWakeup). Each wake: read this file, execute the next PENDING task per the
> protocol below, update the checkboxes + log, reschedule, repeat. Stop when the
> queue is exhausted or a hard blocker is hit.

## Hard protocol (the safety contract)

1. **Validation gate first.** Every task has an explicit gate (a comparison to a
   known value, an invariance, or a cross-method agreement). Run the gate.
2. **Commit ONLY if the gate passes.** A passing task: commit the artifact
   (experiment .py + .md + .npz, or doc), update LEARNINGS if it lands a structural
   finding, mark the task `[x] DONE` here with the result.
3. **On gate FAILURE: do NOT commit the result as correct.** Instead append a clear
   note to `_NIGHT_FINDINGS.md` describing what failed and the suspected cause, mark
   the task `[!] BLOCKED`, and move on. Wrong/unvalidated math must never enter the
   tree as if correct (the factor-of-2 discipline from 2I).
4. **No pushing** (owner authorizes push separately). Commits only.
5. **Bounded.** If a task can't validate after one honest attempt, BLOCK it and move
   on; do not thrash. Reschedule ~1200s between tasks (cache-aware).
6. Keep a running log in the "Log" section below each wake.

## Task queue (ordered; validation-gated)

- [ ] **T1 -- 2L Faltings height / Petersson norm** (the 2J numerical follow-up).
  Compute the period point tau of each test curve (37a1, 389a1, 5077a1) via mpmath
  (AGM / complete elliptic integrals after reduction to short Weierstrass), the
  Petersson norm ||Delta||_Pet(tau) = (Im tau)^6 |Delta(tau)| with
  Delta(tau) = (2 pi)^12 eta(tau)^24, and the archimedean part of omega-bar^2 =
  12 h_Fal. **GATES:** (a) SL_2(Z)-invariance: ||Delta||_Pet(tau) =
  ||Delta||_Pet(-1/tau) to ~1e-10; (b) the assembled stable Faltings height matches
  known values (LMFDB faltings_height for these curves) to ~1e-4. Commit e2l_* only
  if BOTH gates pass.

- [ ] **T2 -- 2M extend arithmetic Hodge index: rank 4 + bad-prime test.** Add a
  known rank-4 curve (e.g. LMFDB 234446.a / "rank 4" minimal model with generators)
  and verify the height pairing is PosDef. Separately, take a point whose
  x-denominator IS divisible by the curve's bad prime, compute the bad-prime Neron
  local height (Tate's non-arch algorithm / component contribution), and verify
  lambda_inf + sum_p lambda_p = h_hat INCLUDING the bad prime. **GATE:** residual
  vs h_hat < 1e-4 (this validates the bad-prime handling 2I deferred) AND rank-4
  pairing PosDef. Commit e2m_* only if the residual gate passes; if the bad-prime
  formula can't be validated, BLOCK that sub-part but still commit the rank-4
  PosDef extension (which reuses validated 2H machinery).

- [ ] **T3 -- 2N Arakelov Green's function cross-check of 2I.** Compute the Arakelov
  Green's function g(z_P) on E(C) = C/Lambda via theta/eta and the elliptic
  logarithm z_P of each generator, and compare to lambda_inf(P) from 2I (an
  INDEPENDENT method for the same quantity). **GATE:** |g(z_P) - lambda_inf(P)|
  < 1e-4 across the generators. Commit e2n_* only if the cross-check passes. (This
  is the strongest possible validation of 2I -- two independent computations of the
  archimedean local height.)

- [ ] **T4 -- SURVEYOR: sharpen the 2K surface specification.** Literature pass
  (WebSearch/WebFetch) on the current state of constructing an arithmetic surface
  below Spec(Z): Deninger's program status, Connes-Consani arithmetic site,
  prismatic / delta-ring approaches to Spec(Z) x_{F_1} Spec(Z), and the
  Faltings-Hriljac vs product-surface gap. Update `2K_spec_z_squared_dictionary.md`
  section 4 and Direction 8 doc with what is genuinely known vs missing as of 2026.
  **GATE:** none numerical; this is synthesis -- just be accurate and cite sources.
  Commit the doc update.

- [ ] **T5 -- Morning synthesis.** Update PHASE_STATE.md (session log, last verified
  state, recommended next actions), append any new LEARNINGS, refresh session_004.md
  with the overnight results, and write `_NIGHT_SUMMARY.md` for the owner: what ran,
  what passed/failed its gate, what was committed, and the recommended next step.

## Compute/risk notes

- T1/T3 involve transcendental period computations with normalization traps; the
  gates (SL_2(Z)-invariance, known Faltings height, cross-method agreement) are
  designed to CATCH such errors. Trust the gate, not the formula.
- Reuse the validated group law + canonical-height machinery in
  `e2h_arithmetic_hodge_index.py` and `e2i_archimedean_local_height.py`.
- If period computation for the non-short-Weierstrass curves is too fiddly, restrict
  T1/T3 to curves convertible cleanly to short Weierstrass and note the restriction.

## Log

(ORCHESTRATOR appends one block per wake: timestamp-ish, task attempted, gate
result, commit hash or BLOCKED reason.)

- INIT (2026-05-28 night): plan written; Lean 2G/2H formalization committed
  (62b4717, build green); 8 prior session-004 commits in place. Scheduling T1.
