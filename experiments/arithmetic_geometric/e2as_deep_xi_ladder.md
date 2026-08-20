# E2AS: the deep xi ladder: the narrowing is REAL: the xi shape is a transient at a ~ 1

**Date**: 2026-08-20. **Status**: BUILDER round, executed; 5/5 checks (215 s ladder + one-time 80-digit zero computation). **Code**: [`e2as_deep_xi_ladder.py`](e2as_deep_xi_ladder.py). **Data**: `e2as_deep_xi_ladder.npz` (tracked); zero cache `zeros_dps80_T350.json` (regenerable, 169 zeros at 80 digits). **Executes**: backlog B2c-deep, deciding the question e2ar (#184) recorded without claim. **Target**: the object of Suzuki arXiv:2606.09096 conjecture (1.2), which his paper states is "expected to approximate xi(1/2 - iz)" for CCM's lowest eigenfunction: conjectural there, with his own numerics supporting only his separate limit (1.12), not (1.2). To our knowledge (CCM's successor paper [4] not yet pulled: queued), this is the first certified numerical probe of (1.2)'s object at finite window.

## 0. The verdict

**The narrowing is real.** At 80-digit arithmetic on 80-digit zeros to T = 350 (the two walls #184 measured), the previously-degenerate refined solves become healthy (a = 2.0 refined: gap 2080 against the 50-digit run's 0.9), the per-rung convergence gates pass at a = 1.0, 2.0, 2.5 (shifts 0.026, **0.006**, 0.041), and the certified rungs say:

| a | gate | certificates | ratio v/(c Xi) at z = 6 | status |
|---|------|--------------|--------------------------|--------|
| 1.0 | 0.026 converged | clean | **+1.12** | the xi shape (#184's rung, reproduced cross-precision) |
| 1.5 | 0.075 NOT converged | clean | +0.62 | consistent interpolation, ungated |
| 2.0 | 0.006 converged | clean (mixing 0.04) | **+0.20** | the load-bearing rung: certified strict narrowing |
| 2.5 | 0.041 converged | mixing FAILS (9.0) | +0.03 | consistent continuation, uncertified |

So the finite-a hard-window Weil-form ground state passes THROUGH the xi shape near a = 1 and then narrows strictly below it: at the certificate-clean, basis-converged a = 2.0 window, its Fourier transform carries only a fifth of Xi's relative mass at z = 6. The approach to (1.2)'s conjectured limit is NON-MONOTONE at accessible windows.

## 1. What this means, said carefully

If (1.2) is true, the shape must RETURN to Xi at larger a: a concrete, measurable prediction (the natural next windows a = 3-5 need zeros to T ~ 600 and dps ~ 100-120 with the same gates: measured requirements, feasible). If instead the narrowing trend continues, the conjectured limit needs modification (the normalization c_a cannot rescue pointwise convergence once the ratios at fixed z head to 0). Either way this is information the live corpus does not currently have: Suzuki's paper proves nothing about (1.2), tests only (1.12), and cites CCM's expectation. Caveat held open until CCM [4] is pulled: their zeta-regularized determinant representation of the same function might include numerics; the pull is queued and the claim above is worded as "first to our knowledge."

Physical reading, consistent with everything measured since #180: the Rayleigh quotient rewards concentrating spectral mass deep in the central hole; at small a the type-a bandwidth constraint forbids concentration (the lobe is wide: ratios above 1 at a = 0.75-1); as a grows, concentration becomes affordable while zero-annihilation stays cheap, so the lobe narrows. The xi shape appears exactly at the crossover. Under this reading a return at larger a would require the growing zero-annihilation burden to eventually dominate: which is precisely what (1.2) implicitly claims, and what the next windows would test.

## 2. Protocol notes (what the deep run fixed and caught)

- The 50-digit degeneracy at a = 2 (#184's gate failure) was PRECISION STARVATION, not intrinsic: 80-digit zeros restore a healthy spectrum. Per-quantity gating again: eigenvalues keep falling under refinement while shapes converge.
- The a = 2.5 mixing certificate fails ($\sqrt{\mathrm{tail}_0\mathrm{tail}_1}/(\lambda_1-\lambda_0) = 9$): the scope boundary is self-documented in the checks; fixing it needs deeper zero sets (smaller tails) per the same arithmetic that set T = 350 for a <= 2.5.
- Per-quantity discipline, third instance: the refined deep solves' $\lambda_0$ VALUES are tail-limited (the $a = 2.0$ refined bottom sits below ten times its tail bound and is reported as a bound, not a value); the shape claims rest on the VECTOR certificates (mixing + convergence gate), which pass on all claimed rungs.
- Cross-precision reproduction: the a = 1 rung's ratios match #184 within 0.03.
- Zero cache validated against Riemann-von Mangoldt at T = 350 (169 vs 169.10).

## 3. Hand-off

(i) **B2c-deep2** (optional, costed): a = 3-5 at T ~ 600, dps 100-120, gates as here: decides return-vs-continuation, i.e. tests (1.2) where it must show itself; (ii) **pull CCM [4]** (the 2025+ paper with the determinant representation) and re-run the novelty wording against it; (iii) fold the verdict into the P12 packaging case: the arc #180-#185 now ends on a sharp, externally-relevant statement.
