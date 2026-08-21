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
- **A3. The off-line implant: the rigidity curve (Frankenstein multiplier).** Move one zero pair of $\xi$ off the line by $\delta$ via a Blaschke factor and track the prime side: the correction to the von Mangoldt measure is an explicit CONTINUOUS density (mass off the log-prime-power lattice). Measure leak($\delta$, window $X$): pre-registered law $\sim e^{\delta X}$-growth, invisible for $X \ll 1/\delta$: the object-side twin of the primes-thread bound (an off-line zero above height $3\times10^{12}$ needs $x \sim 10^{150}$ to surface). Deliverable: the CALIBRATED detector: what an off-line zero costs in Euler-structure violation, as a curve. KILL: if some discrete redistribution of $a_n$ absorbs the leak on the lattice, the detector is weaker than believed and the bracket needs a sharper clause. Probes C2's contrapositive. Cost S-M.
- **A4. The zeta-to-Beurling interpolation ramp.** $b_p(t) = p\,e^{t\varepsilon_p}$, $t \in [0,1]$: drift, duality defect, and vM-identity stability vs $t$ at fixed data depth. Pre-registered (the counting-side twin of #172's continuity obstruction): a smooth ramp with no cliff, knee position set by the data meter, i.e. finite-scale instruments cannot see the arithmetic 0/1: quantifying exactly where arithmetic becomes visible to finite data. Cost S.

## 2. Family B: upgrades to the assembled object at its two joints

- **B1. The coupled SP4 ladder (where does C1 bind?).** #180 measured the two-sidedness residual FLAT ($10^{-8}$-$10^{-7}$) over prime windows to $e^6$ at the fixed spectral meter: C1 does not bind there. Grow both meters together (extended-precision line engine, narrower probes, emergent spectrum to $T \sim 300$-$1000$) until the residual departs its floor: the measured exchange rate between prime data and spectral data in the object. Cost M (precision engineering).
- **B2. The wrong polarization, built anyway (the tariff inside the object).** Equip the v0 cokernel with candidate metrics ($L^2$ on the circle; the $\mathcal{E}$-pullback; a Christoffel-weighted metric) and score each against the 7-property SP5 spec cell-by-cell. Pre-registered: every metric making the flow self-adjoint with the right spectrum consumes zero locations (K1) or the uniform growth clause (#160/#171); typing that demand in the object's own coordinates mints coordinate system #4 for M4 (the trojan-ledger's stated purpose for such builds). Probes C2. Cost M.
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
- **B2c-gap (cheap; the arc's coda).** Measure the energy sub-optimality of
  the $\Xi$-state: $Q(k_\lambda)/\|k_\lambda\|^2$ against $\lambda_0(a)$
  across the ladder: what a corrected selection principle must pay. One run
  on existing machinery. Cost S.
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

- **C1. The function-field twin (the shadow instance).** The same five-component pipeline for a curve over $\mathbb{F}_q$ (start with the e2b curve over $\mathbb{F}_5$): lattice = effective divisors by degree, circle circumference $\log q$ (every place commensurable), multiplier = the curve's zeta on its line. Expect: emergent spectrum EXACTLY periodic (the rung-2 arithmetic progression, step $2\pi/\log q$), SP4 exact (Grothendieck), SP5 backed by Hodge index. Deliverable: the $\mathbb{F}_q$ column of the satisfiability matrix filled by MEASUREMENT through identical code; the per-cell difference between the zeta column and the $\mathbb{F}_q$ column is the missing structure, displayed in one table. Also the standing regression control for every future candidate. The shadow discipline applied to the assembly itself. Cost M.
- **C2. The eta-form second variation (#178 trigger 1, given shape).** The finite-conductor second-variation matrix of the arithmetic eta over character space; measure its signature and what forces it. Pre-registered fork: it reproduces the Weil form (M4 in APS costume: coordinate #5) or fails forcing (trigger 1 hardens). Cost M.
- **C3. The CCM Section-7 operator audit (rung-4 hand-off, still unexecuted).** Implement the arXiv 2511.22755 determinant family ($\det_{reg} = -i\lambda^{-iz}\hat\xi(z)$) at finite cutoff; run the R3.5/K1 audit, the W6-vs-#143 gate, and the pipeline scorecard on it. Cost M-L.
- **C4. B2-Lean: the interface as a structure.** `SPInterface` with the five components as fields; the function-field instance inhabits it sorry-free (extending ToyModel/FunctionFieldRH); v0 as the four-of-five finite-scale inhabitant; D-H and Beurling as typed refusals (which field cannot be filled, as a type error). The matrix becomes machine-checked and "the missing object" a first-class term. Cost L.

## 4. Suggested order

1. **A1 + A2** in one session (pure pipeline reuse; completes the design matrix).
2. **A3** (the rigidity curve: the most quotable new instrument).
3. **C1** (the shadow column: highest strategic value per unit work).
4. **B2** (the tariff typed inside the object).
5. **B1, B3, B4** as follow-ups hardening the #179/#180 bank.
6. **C2, C3, C4** as the heavier tier.

Wrong outcomes are acceptable at every entry; unregistered outcomes are not.
