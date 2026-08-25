# The construction backlog: build-to-test list

**Date**: 2026-08-19. **Status**: standing backlog (Owen's directive: build things, wrong is ok). **Provenance**: the #179/#180 arc ([`e2an_sp_object_v0.md`](../../experiments/arithmetic_geometric/e2an_sp_object_v0.md), [`e2ao_scaling_ladder.md`](../../experiments/arithmetic_geometric/e2ao_scaling_ladder.md)): the assembled SP-object plus its ladder showed that a deliberately wrong construction returns coordinates, and that the pipeline can score ANY coefficient lattice cell-by-cell. This file is the queue of constructions worth building on that principle.

## 0. Rules every build carries

1. **Pre-register** the expectation and the kill/exit in the probe docstring before running (the e2ao precedent: the registered midgap guess was refuted by the run and the refutation was the finding).
2. **Run the bracket**: D-H and Beurling twins through identical code wherever the construction poses for them; name the cell each control kills.
3. **Name the joint**: every build states whether it probes C1 (SP2 $\wedge$ SP3, counting side) or C2 (SP5, the polarization) or is a control/instrument.
4. **K1 posture**: construction paths consume integers/coefficients only; oracles (L-values, zeros) live in validation cells behind the call counter.
5. Wrongness gets coordinates: a LEARNINGS entry per executed build, frontier verdict stated honestly.

## 1. Family A: controls that isolate one clause (cheap, pipeline reuse)

The conservation law says zeta = Euler product $\wedge$ additive lattice. The pipeline currently holds three points of the design matrix: zeta (both clauses), Beurling (Euler only), D-H (FE without Euler, form side). These builds fill the rest.

- **A1. The Cramer control (lattice-density without Euler, counting side).** Integers $= \{n + u_n\}$, $u_n$ iid uniform $[-\tfrac12,\tfrac12]$, fixed seed: $N(x) = x + O(1)$ EXACTLY, multiplicative structure destroyed. Expect: pole/residue PASS (density exact), duality FAIL (jitter kills Poisson/theta), Euler cells FAIL, emergent spectrum unstable. KILL FOR THE FRAME: if duality passes, $x + O(1)$ counting alone buys the FE and the fourth clause is wrong; chase immediately. Completes the 2x2: the pair (A1, Beurling) separates density-lattice from multiplicative-freeness on the counting side the way (zeta, D-H) separates them on the form side. Cost S.
- **A2. The S-finite Euler ladder (smooth-number lattices).** Lattice $=$ $P$-smooth numbers, $P$ stepping through the primes: Euler exact at every rung, additive lattice absent at every finite rung (zero density, $R = 0$), recovered only at $P = \infty$. Measure duality defect($P$), residue($P$), and the multiplier's dip-depth toward the zeta zeros vs $P$. Pre-registered: the FE is NOT bought incrementally (defect stays $O(1)$, pole stays absent, then both appear only in the limit); if instead the defect decays smoothly, the lattice is purchasable in installments and the all-or-nothing reading of the fourth clause needs repair. Either outcome is a coordinate on WHERE the lattice enters. Cost S.
- **A3: EXECUTED 2026-08-22 (LEARNINGS #192, e2ax 12/12).** The implant done
  FE-honestly (merge-and-split, the local de Bruijn-Newman move); the
  $e^{\delta X}$ law refined to the exact envelope $4(\cosh(\delta u)-1)$,
  height-independent; the calibrated curve $U^*(\delta) = 1.41/\delta$
  (density register; register table banked). The kill FIRED as the
  primes-thread twin predicted (lattice absorbs in-window, lattice-
  agnostically), and the sharper clause it demands landed measured: the
  rigidity is ADMISSIBILITY: free-weight imitation is perfect and traces
  the pole's Lorentzian ghost; the nonneg fake pays $\cosh(\delta U)$ in
  multiplicity AND still fails ($\ge 0.33$ residual): C2's contrapositive
  is a positivity statement. Optional residues: the sign-constrained
  lattice cell; the ghost as an instrument.
- **A4: EXECUTED 2026-08-24 (LEARNINGS #198, e2bc 8/8).** Both
  pre-registrations landed: NO CLIFF (drift and duality linear in $t$,
  log-log slopes 0.974/0.926; a 0.1-percent jitter lifts the drift nine
  orders off the integer floor) and the knee IS the data meter's
  ($t^*$ moves 4+ orders between $X = 15000$ and $60000$); the vM
  identity exact at every $t$ (the Euler clause never breaks). The
  counting-side continuity trilogy (#172 pointwise / #188 sequence /
  A4 instrument) is complete; FAMILY A is complete. Banked: the ramp as
  a calibration axis for any future counting-side detector.

## 2. Family B: upgrades to the assembled object at its two joints

- **B1. The coupled SP4 ladder (where does C1 bind?).** #180 measured the two-sidedness residual FLAT ($10^{-8}$-$10^{-7}$) over prime windows to $e^6$ at the fixed spectral meter: C1 does not bind there. Grow both meters together (extended-precision line engine, narrower probes, emergent spectrum to $T \sim 300$-$1000$) until the residual departs its floor: the measured exchange rate between prime data and spectral data in the object. Cost M (precision engineering).
- **B2: EXECUTED 2026-08-23 (LEARNINGS #194, e2az 12/12).** The three metrics
  measured out a trilemma sharper than pre-registered: self-adjointness is
  FREE (all diagonal), and within the family D1 (primitive-positive)
  IMPLIES failing both D2 (K1-clean) and D3 (Euler contact): flat-on-dips
  IS the Weil form ($2.5\times10^{-5}$ Gram match; D-H passes at 1.00);
  the pullback is clean but $7.5\times10^{-8}$-massless at the dips (#170
  measured in-object) while seeing D-H's landmark at 0.058; Christoffel
  concentrates only at degree = atom count (#172 physics; D-H twin 311x)
  and its K1-clean surrogate starves the dips by 21 percent. COORDINATE
  #4 MINTED: M4 = the Euler side funding positivity exactly where its own
  transform vanishes (trojan ledger Section 10; score C3 against it
  first). Residues: the $|m'|^2$-channel finite statement (VERIFIER
  nugget); the pullback degeneracy locus as a candidate-screen.
- **B2c/B2b: EXECUTED 2026-08-20 (LEARNINGS #183, e2aq 10/10).** Soft-window
  xi-test: family-dependence typed (hole norm-stuffing; locking exact to
  $10^{-38}$); Omega-ladder: nearest-gap law refuted, replaced by the graded
  FRONTIER LAW ($\sigma$-slope $= -(\gamma_{frontier}-\Omega)^2$ to 2 percent).
  Live successors below.
- **B2c-hard: EXECUTED 2026-08-20 (LEARNINGS #184, e2ar 8/8).** Hard-window
  B-spline instrument: rigidity restored; at the basis-converged window
  $a = 1$ the ground state IS the xi shape ($L^2$ residual 0.051,
  refinement-stable): the first positive numerical contact with Suzuki
  (1.2). All $a \ge 1.5$ shape claims gated out by the convergence
  certificate. Live successor below.
- **B2c-deep: EXECUTED 2026-08-20 (LEARNINGS #185, e2as 5/5).** The narrowing
  is REAL: certified converged $a = 2.0$ rung at a fifth of $\Xi$'s relative
  mass at $z = 6$; the xi shape is a transient at $a \approx 1$; the approach
  to Suzuki (1.2) is non-monotone at accessible windows. Successors below.
- **B2c-lit: DONE 2026-08-20 (LEARNINGS #186).** CCM [4] (arXiv:2511.22755)
  pulled and read at depth: interior-only convergence (Lemma 7.3), real
  numerics, no unconstrained-bottom shape measurement: #185's novelty claim
  survives re-scoped.
- **B2c-obj: SETTLED AT SOURCE 2026-08-20 (LEARNINGS #187).** CCM's QWλ is
  the restriction to the FULL $L^2$ window ($\kappa$ weightless): (1.2)'s
  object IS the unconstrained bottom, #185 applies directly, the CCM-numerics
  tension dissolves (their evidence lives at $a \le 1.79$; finite-$\lambda$
  proximity is compatible with common narrowing), and the constrained e2at
  run re-scopes to a control.
- **B2c-prox: EXECUTED 2026-08-21 (LEARNINGS #190, e2av 4/4).** The kernel is
  a scalar multiple of $\Xi$ to six decimals at every window (Lemma 7.3
  exact-at-scale); the proximity decays monotonically past CCM's evidence
  range (0.9988 at $a=1$, their numerics reproduced, to 0.715 at $a=4$):
  the #189 dichotomy resolved; the $\Xi$-shape exists in every window but is
  not the minimizer beyond $a \approx 1$.
- **B2c-gap: EXECUTED 2026-08-21 (LEARNINGS #191, e2aw 10/10).** The naive
  gap is real at $a = 1$ (the $\Xi$-state pays ten orders; a 5-percent shape
  deviation buys them), and the pre-registered pincer FIRED at $a = 1.5$:
  the kernel's exact-vanishing identity makes its true window energy
  tail-controlled ($\lg B \approx -2\pi e^{2a}/\ln 10$), undercutting the
  instrument's certified bottom by 4/92/8060 orders at $a = 1.5/2/4$: the
  certified collapse re-scopes to the resolvable subspace, (1.2) is
  horizon-limited for every direct-minimization instrument, and the B2c
  chain closes with the season's second horizon law. Optional hardening:
  interval arithmetic on the three tail integrals.
- **B2c-deep2: EXECUTED 2026-08-20/21 (LEARNINGS #189, e2au).** CERTIFIED
  no-turnaround through $a = 4$ (recorded through 5): the (1.2) object
  collapses monotonically after the $a \approx 1$ transient; ratios
  bit-stable across the $T = 600 \to 1500$ depth change; certificates
  cleaned on schedule. The conjecture's fate now rests on B2c-prox above.
  Optional residue: one depth doubling ($T \sim 3000$ via #188's
  zero_polish) certifies $a = 4.5$-$5$.
- **B2d. The frontier-capacity function.** Measure
  $\gamma_{\mathrm{frontier}}(J, \Omega, \sigma)$ and the graded profile's
  per-zero cost (~6 decades/zero in e2aq): how many zeros past the ceiling
  can $J$ modes annihilate, and at what precision schedule. Cost S.
- **(superseded) B2c original spec, kept for the record:**
  Suzuki (arXiv:2606.09096, conjecture (1.2)): the localized Weil-form ground
  state's Fourier transform converges to $\xi(1/2+iz)$ as the window grows.
  Our 50-digit minimizer (`make_figs.py::ground_state_mp`) already computes
  the left side: overlay $\hat g^*_\sigma$ against $\Xi$, measure the
  convergence rate across the ladder, both bases (Gaussian-mode and, for
  fidelity to the conjecture's interval localization, a compact window).
  Either outcome matters: convergence measured = numerical support plus a
  rate for a live conjecture; failure to converge in our family = a family-
  dependence finding. Cost S. Prior art: the sweep dossier.
- **B2b. The Omega-ladder (from #181's second law).** The multi-mode window
  margin saturates in $\sigma$ and is governed by the frequency ceiling
  $\Omega$: measure margin($\Omega$) at fixed generous $\sigma$, per-rung
  precision matched to the predicted floor (50-digit protocol from
  `visualizations/research/make_figs.py::ground_state_mp`), pre-registered
  exponent = the gap to the first unreachable zero. RH's uniform statement
  lives in the $\Omega \to \infty$ direction; this ladder prices it. Cost S-M.
- **B3. The certification-cost theorem (harden #180).** Propagate the e2ao assembly's quadrature/truncation constants into a proven statement: this assembly certifies $\mathrm{margin}(\sigma)$ iff $\sigma \le \sigma^*(\varepsilon)$ with explicit constants, making the $e^{\gamma_1^2\sigma^2}$ price a theorem about the instrument rather than a measurement. Cost S-M; later Lean-able.
- **B4. The D-H invisibility certificate (harden #179).** Interval-arithmetic lower bound on $|m_{DH}|$ over the landmark window $[85.2, 86.2]$ from the coefficient lattice (smoothed AFE with explicit tails): "the object provably cannot see the off-line pair at any circumference." The completeness failure becomes a THEOREM about the control, and the proof's shape is a template for what a zeta completeness statement must supply. Probes C1's completeness face. Cost M.

## 3. Family C: foreign instances of the pipeline

- **C1: EXECUTED 2026-08-23 (LEARNINGS #193, e2ay 13/13).** The F_q column
  filled by measurement on the e2b curve: every expectation landed (exact
  periodicity to $10^{-16}$, SP4 exact Lefschetz, SP5 inhabited with Hasse
  margin 1.47 backed by Hodge index), plus one unpre-registered structural
  cell: the FF world needs the pole-ARRAY regularizer (single-pole fails at
  $10^{14}$; the array form, available from lattice data, is exact at
  $10^{-12}$). The per-cell zeta-vs-F_q table is in the dossier; the run is
  the standing regression control. Residues: higher-genus extension (cheap);
  C4 gains measured witnesses per field.
- **C2: EXECUTED 2026-08-23 (LEARNINGS #196, e2bb 11/11).** The fork took
  its unlisted third branch: the eta-Hessian on the FE-closed pencil
  EXISTS canonically (null rows $10^{-26}$; tau/step/T-stable) and its
  (1,1) signature is FORCED at both conductors: by HOLOMORPHY (zeros move
  holomorphically in the mixing parameter, so eta is harmonic at leading
  Abel order: traceless, measured 0.000/0.045 trace-to-norm). Coordinate
  #5 minted as a no-go with a mechanism: the eta route's curvature is
  conformally rigid: no positivity can be sourced there (#178's parity
  kill at second order). Trigger 1 hardened-with-structure; trigger 3 is
  the eta arc's only open door. Extras: $b_6(\kappa) = (\kappa^2+1)\log6$
  (e2an's 1.936 in closed form); the non-commuting-limits estimator
  lesson; the holomorphy-tracelessness VERIFIER nugget.
- **C3: EXECUTED 2026-08-23 (LEARNINGS #195, e2ba 9/9).** The 2511.22755
  family built from the reading note and validated by the exact zero-side
  identity ($10^{-3}$; it caught both pilot bugs). The funding value
  $\varepsilon_N(\lambda)$ tracks Connes §6.4's doubly-exponential law
  (ratios 0.97-1.73) and is horizon-priced (dps $\sim 4\pi\lambda^2/\ln10$:
  71 at their $\sqrt{13}$, 546 at Groskin's 10: their own choices confirm);
  BOTH pre-registered D-H flip windows refuted: the faithful twin tracks
  zeta to the floor (the firewall signal itself horizon-limited: the
  off-line negativity pays the #180-#183 annihilation price); reality
  persists on an O(1)-indefinite synthetic control. Gates: R3.5 wall met
  with price tag; W6 upgrade = M4 at this family; #194 refinement minted:
  M4 = UNIFORM-in-$\lambda$ D1 under D2 $\wedge$ D3. Residue: the D-H flip
  location as a costed mp job (23257 closed-form arch entries).
- **C4: EXECUTED 2026-08-24 (LEARNINGS #197, `lean/ZetaRH/SPInterface.lean`,
  full library GREEN at 3763 jobs, axiom-clean).** `SPInterface` with the
  five components as fields; `SPInterface.rh` proves every inhabitant
  satisfies its RH; `curveF5` inhabits it sorry-free with the e2ay column
  as machine-checked witnesses; `SPInterfaceSans5` + `sans5_sp5_iff_hasse`
  makes the missing fifth field EQUIVALENT to the Hasse content (M4's
  genus-1 shadow as an iff); D-H refused at SP3 (`dh_no_euler_point`:
  $\kappa^2 = -1$ impossible) and Beurling/jitter refused at the lattice
  (`b_determined` quantization + `beurling_refusal`). Bonus: first
  verified Lean state on this box (toolchain + Mathlib cache installed).

## 4. Suggested order

1. **A1 + A2** in one session (pure pipeline reuse; completes the design matrix).
2. **A3** (the rigidity curve: the most quotable new instrument).
3. **C1** (the shadow column: highest strategic value per unit work).
4. **B2** (the tariff typed inside the object).
5. **B1, B3, B4** as follow-ups hardening the #179/#180 bank.
6. **C2, C3, C4** as the heavier tier.

Wrong outcomes are acceptable at every entry; unregistered outcomes are not.
