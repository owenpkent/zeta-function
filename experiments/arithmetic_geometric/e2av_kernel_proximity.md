# E2AV: the proximity resolution: CCM's kernel IS Xi, and the ground state departs from it exactly as the collapse said

**Date**: 2026-08-21. **Status**: BUILDER round, executed; 4/4 checks (1255 s; dps-80 solves on the 110-digit zero cache; refined resolution m = 112a). **Code**: [`e2av_kernel_proximity.py`](e2av_kernel_proximity.py). **Data**: `e2av_kernel_proximity.npz` (tracked). **Executes**: B2c-prox, resolving the #189 dichotomy. **Kernel built from source**: CCM (7.5)-(7.6), $k_\lambda = E(h_\lambda)$ with the Fourier-self-dual Hermite-limit seed $h = \psi_0 - \alpha\psi_4$ (vanishing integral, $\alpha = 1.632993$; self-duality and the integral verified in-run to $10^{-15}$), carrying CCM's own Lemma 7.2 substitution bound $c\lambda^{-2}$ as the caveat (0.002 by $a = 3$, zero by $a = 4$).

## 0. The two readouts

**Readout 1: the kernel is a scalar multiple of $\Xi$, immediately and exactly.** $\hat k/(c\,\Xi)$ = 1.000000 at every test point and every window $a = 1..4$ (drift $10^{-6}$ at $a = 4$: quadrature-level). CCM's Lemma 7.3 is confirmed constructively with NO finite-$\lambda$ transient: the self-dual seed plus the vanishing integral capture the full Mellin mass already at $a = 1$ (the theta mechanism at work). There is no "slow kernel limit" for the conjecture to hide behind.

**Readout 2: the kernel-groundstate proximity decays monotonically once past CCM's evidence range.**

| a | 1.0 | 1.5 | 2.0 | 2.5 | 3.0 | 3.5 | 4.0 |
|---|-----|-----|-----|-----|-----|-----|-----|
| $|\cos(k_\lambda, \xi_\lambda)|$ | 0.9988 | 0.9880 | 0.9391 | 0.8759 | 0.8133 | 0.7569 | 0.7152 |
| $\lambda^{-2}$ caveat | 0.135 | 0.050 | 0.018 | 0.007 | 0.002 | 0.001 | 0.000 |

At $a = 1$ ($\lambda = e \approx 2.7$, inside their tested $\lambda \le 6$): 0.9988: their numerical evidence reproduced. Beyond: steady decay, ~0.05-0.06 per half-window, entirely real (the caveat is dead from $a = 2.5$). The ground state's own $\Xi$-ratios collapse alongside (side-by-side in the log), consistent to the digit with #189's certified ladder.

## 1. The resolution of the #180-#190 arc

Every measured and proven fact now coexists without tension:
- CCM's Lemma 7.3 (kernel $\to \Xi$): TRUE, and in fact exact-at-scale (Readout 1).
- CCM's numerical proximity at $\lambda \le 6$: TRUE (our 0.9988 at their range).
- Our certified collapse of the unconstrained ground state (#185/#189): TRUE.
- The reconciliation: **the proximity itself degrades** once the window grows past their evidence range: the ground state departs from the $\Xi$-shaped kernel monotonically.

The consequence, stated with care: CCM write of the kernel-groundstate step "Justifying rigorously this step is the main remaining obstacle to our approach to RH." Our measurement says the step, as an approximation statement at growing windows, fails quantitatively in the accessible range: the obstacle is not merely unproven; on the current evidence the guess degrades where it matters. For conjecture (1.2) as Suzuki states it (the ground state's FT $\to \xi$): the certified data through $a = 4$ shows the opposite trend for the unconstrained object, and the kernel's exactness shows the failure is not on the kernel side. What survives untouched: the possibility that a DIFFERENT selection principle (not the raw bottom of $Q_{W\lambda}$) picks the $\Xi$-shaped state: the kernel itself proves such a state exists in the window space at every scale; it is simply not the minimizer beyond $a \approx 1$.

That last sentence is the arc's constructive gift to the program: the $\Xi$-shape IS present in every window (as $k_\lambda$), at Rayleigh quotient... measurable next: $Q(k_\lambda)/\|k_\lambda\|^2$ vs $\lambda_0$: the "energy gap" between the conjectured state and the true bottom, as a function of $a$: one cheap follow-up (B2c-gap) that would quantify exactly how sub-optimal the $\Xi$-state is and what a corrected conjecture must pay.

## 2. Scope and caveats

Hermite-limit substitution for the prolate eigenfunctions (CCM Lemma 7.2, $\le c\lambda^{-2}$: dominant only at $a = 1$, where the proximity is anyway high); ground-state solves at the gate-passing refined resolution (m = 112a) with the dps-80 protocol (the dps-50 attempt failed PD-ness of the degree-25 spline Gram at $J = 189$: 38 digits of alternating-sum cancellation: the failure mode now documented); proximity metrics in float from mp evaluations (percent-level claims only). Frontier UNMOVED (a diagnostic of the corpus's approach, zeros consumed by design).

## 3. Hand-off

(i) **B2c-gap** (cheap): $Q(k_\lambda)/\|k_\lambda\|^2$ vs $\lambda_0(a)$: the energy sub-optimality of the $\Xi$-state across windows; (ii) P12: all sections now have content: the note's closing line is this round's resolution; law-novelty pass then draft; (iii) optional courtesy: the finding is directly relevant to the authors of 2511.22755 and 2606.09096: Owen's call whether to communicate after P12 is drafted.
