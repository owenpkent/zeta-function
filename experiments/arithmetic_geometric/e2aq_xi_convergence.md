# E2AQ: the xi-convergence test and the Omega-ladder (both pre-registrations refuted, both replaced by sharper laws)

**Date**: 2026-08-20. **Status**: BUILDER round, executed; 10/10 checks (69 s; 50-digit protocol throughout, zeros at 50 digits disk-cached). **Code**: [`e2aq_xi_convergence.py`](e2aq_xi_convergence.py). **Data**: `e2aq_xi_convergence.npz` (tracked). **Executes**: backlog B2c (xi-convergence, soft-window analogue) and B2b (the Omega-ladder). **Prior art**: [`weil_positivity_prior_art_sweep.md`](../../docs/03_research/reading_notes/weil_positivity_prior_art_sweep.md) (Suzuki arXiv:2606.09096 conjecture (1.2) is the target of Part 1).

## 0. Verdicts up front

Both parts pre-registered a law; the run refuted both; the refutations resolved into sharper measured laws, all now encoded as the module's checks. Frontier UNMOVED; what moved is the instrument-level understanding of what the window margin IS.

## 1. Part 1: the soft-window minimizer does NOT converge to Xi, and why

Suzuki (1.2) (after CCM): the HARD-window localized ground state's Fourier transform converges to $\xi(1/2+iz)$. Our soft-window analogue (the modulated-Gaussian family's Rayleigh-quotient minimizer): the central-shape residual against a fitted multiple of $\Xi$ on $[0, 10]$ is 33-154 at every scale, with the fitted scale unstable in sign. **Mechanism, visible in the numbers**: the Rayleigh quotient REWARDS parking norm in the central spectral hole (mass where the form cannot charge it lowers the quotient), so the central lobe is nearly-degenerate norm-stuffing, not a determined shape. The hard-window operator $A_a$ has a unique rigid ground state; our family's bottom is soft exactly in the hole directions. **Typed outcome: family-dependence, not evidence against (1.2).** The faithful test needs the hard-window basis (sine modes on $[-a, a]$): queued as B2c-hard.

**What DID survive, sharpened by two orders of understanding**: the zero-locking. With the node metric fixed (nearest sign change to each $\gamma$, 50-digit bisection), the minimizer's nodes sit within $10^{-38}$-$10^{-41}$ of $\gamma_1, \gamma_2, \gamma_3$ at every scale: when the mode count exceeds the reachable zero count, the minimizer annihilates the reachable zeros EXACTLY at working precision (#181's $4\times10^{-3}$ was grid resolution, not the phenomenon). The locking is the family-robust part of the (1.2) circle; the central lobe is the family-fragile part. That split is the round's Part-1 finding.

## 2. Part 2: the nearest-gap law is dead; the frontier law replaces it

Pre-registered: $\log \mathrm{margin}(\Omega) \sim -\sigma^2(\gamma_{\mathrm{next}}(\Omega) - \Omega)^2$. Refuted three ways: same-gap rungs ($\Omega = 20$ vs $24$, gap $\approx 1.01$ both) differ by 1.5 decades; the margin RISES monotonically with $\Omega$ ($10^{-47.8}$ at $\Omega = 15$ to $10^{-37.3}$ at $42$) regardless of gap; the gap$^2$ regressor's fitted slope is $\sigma$-blind (ratio 1.01 across $\sigma = 0.45/0.55$ against a predicted 1.49).

The replacement, measured and mechanism-checked:

- **The frontier law.** With the mode grid held FIXED (the naive $\sigma$-sweep is confounded: growing $J$ deepens annihilation faster than the Gaussian narrows, flipping the derivative's sign, $+25.1$ naive vs $-85.2$ fixed), the $\sigma$-derivative of the log-margin at $\Omega = 34$ is $-85.2$, matching $-(\gamma_8 - \Omega)^2 = -(43.33 - 34)^2 = -87.0$ to 2 percent. The margin is the Gaussian leak onto **the first zero the family cannot annihilate**: the annihilation frontier, which here sits TWO zeros past the nominal ceiling (the family kills $\gamma_6 = 37.59$ and $\gamma_7 = 40.92$ with its spare dimensions).
- **The frontier is GRADED, not binary.** Node precision degrades monotonically across the edge: $2\times10^{-35}$ at $\gamma_6$, $5\times10^{-29}$ at $\gamma_7$, $1\times10^{-23}$ at $\gamma_8$, $2\times10^{-10}$ at $\gamma_9$: about six decades per zero. Partial annihilation continues past the frontier; the $\sigma$-slope still selects $\gamma_8$ because its residual leak dominates.
- **The Omega-trend is collective.** The monotone rise of the margin with $\Omega$ tracks the growing zero density at the edge (gaps shrinking like $2\pi/\log$), not any single gap.
- **Honesty note applied upstream**: #181's retrodiction ("$\sigma$-slope $-12 \approx -(\gamma_{\mathrm{next}}-\Omega)^2 = -12.9$") is DOWNGRADED to coincidence: its two $\sigma$ points had different mode counts, and the confound is now measured.

## 3. The unified reading (for the C2 corridor)

Both margin laws are one statement at different capacities: **the window margin is always a single-zero Gaussian leak at the family's annihilation capacity edge.** The single-mode family can annihilate nothing, so it pays $\gamma_1$ (#180's closed form, exponent $\gamma_1^2$); a $J$-mode family pays $\gamma_{\mathrm{frontier}}(J)$, with the frontier graded. Weil positivity's uniform statement is then: however the capacity grows, the leak onto the first unpaid zero never goes negative: every zero is eventually "paid for" exactly once. That is a coordinates-level restatement of the completeness/positivity joint, now with a measured graded-frontier structure attached.

## 4. Hand-off

(i) **B2c-hard**: the faithful hard-window (sine-basis) xi-convergence test: the family-fragile central lobe is exactly where (1.2)'s content lives, and the hard window restores the rigidity; (ii) the frontier-capacity law $\gamma_{\mathrm{frontier}}(J, \Omega, \sigma)$ as a measurable function (how many zeros past the ceiling can $J$ modes kill: the graded profile suggests a clean per-zero cost); (iii) fold the corrected #181 note into any future citation of the band-ceiling slope.
