# E2AO: the scaling ladder, and the closed form of the window margin

**Date**: 2026-08-19. **Status**: BUILDER round, executed; 16/16 checks. **Code**: [`e2ao_scaling_ladder.py`](e2ao_scaling_ladder.py). **Data**: `e2ao_scaling_ladder.npz` (tracked, evidence rule). **Parent**: [`e2an_sp_object_v0.md`](e2an_sp_object_v0.md) (LEARNINGS #179), whose handed-forward item 1 this executes.

## 0. What was asked and what came back

The #179 hand-off: scale the assembled SP-object and measure how the SP4 residual and the SP5 margin move, putting a number on the C1/C2 gaps from the object side. The ladder ran three axes. Two returned flat-green robustness results (C1 does not bind in the tested range; the D-H invisibility is scale-robust). The third returned more than a number: **the SP5 window margin has a closed form, found after the run refuted the round's own registered prediction**:

$$\mathrm{margin}(\sigma) \;=\; 4\sqrt{\pi}\,\sigma\, e^{-\gamma_1^2 \sigma^2}\,(1 + O(e^{-\sigma^2(\gamma_2^2-\gamma_1^2)})),\qquad \gamma_1 = 14.134725\ldots$$

Measured: slope $-199.79$ vs $-\gamma_1^2 = -199.79$, intercept $1.959$ vs $\ln(4\sqrt{\pi}) = 1.959$, $R^2 = 1.000000$, over 38 orders of magnitude (margin $4.8\times10^{-4}$ at $\sigma = 0.2$ down to $1.5\times10^{-42}$ at $\sigma = 0.7$).

## 1. Axis 1 (SP5, the C2 number): the margin law and its refuted precursor

Setup: window family $g_\omega(x) = e^{-x^2/2\sigma^2}\cos(\omega x)$; margin = min over a dense $\omega$-grid of the Weil form per unit $L^2$ mass, $Q(g_\omega)/\|g_\omega\|^2$; prime side assembled from pole + $\Lambda$-sums + archimedean digamma integral (K1-clean), zero side as validation and as the precision instrument past the prime side's floor.

**The registered guess was wrong, and the refutation is the finding.** Predicted: the worst mode dodges into the midgap at $\omega^* = \gamma_1/2$, exponent $(\gamma_1/2)^2 \approx 49.9$. Measured: $\omega^* = 0$ at every rung, exponent $\gamma_1^2 \approx 199.8$. Reason, verified by the assembly itself: **the pole does not penalize the unmodulated bump, because the explicit formula cancels the pole term against primes + archimedean exactly** (v0's $H^0$ cancellation, here doing work). The deepest spectral hole is therefore the full central gap $(-\gamma_1, \gamma_1)$, its center is the origin, and the margin is carried by the first zero alone. Given $\omega^* = 0$ the closed form is elementary (the Gaussian's value at $\gamma_1$); the content is $\omega^* = 0$, the identification of the decisive spectral geometry (the hole around the EF-cancelled pole), and the two prices below.

**Price 1 (the certification cost: the C2 statement).** The prime side assembles this exponentially small margin out of $O(1)$ pole/arch/prime terms that cancel. At assembly accuracy $\varepsilon$ it certifies the margin only while $\mathrm{margin}(\sigma) > \varepsilon$, i.e. for $\sigma^2 < \ln(c/\varepsilon)/\gamma_1^2$. Measured: at $\varepsilon \approx 10^{-5}$-$10^{-6}$ the bottom rung is certified ($\sigma = 0.2$: prime side $4.8\times10^{-4}$, matching the exact margin to $3.8\times10^{-7}$) and the floor is crossed at $\sigma = 0.3$; every rung beyond saturates at the floor. **Certifying Weil positivity prime-side at window scale $\sigma$ costs $e^{\gamma_1^2\sigma^2}$ in assembly precision.** That is the determinant-class clause (M4's trace-formula name) priced at finite scale: the uniform statement RH needs is the $\sigma \to \infty$ survival of a quantity whose certification cost, in this coordinate system, is exponential in $\sigma^2$.

**Price 2 (instrument honesty).** Two measured traps are recorded as design constraints. (i) Generalized (multi-mode) margins below the $G$-conditioning floor are meaningless; and with enough modes the truncated zero-side Gram is rank-deficient by construction, so the multi-mode bottom reads "0 below double precision" at every rung (checked as such). The single-mode family carries the law and is an upper-bound family: Weil positivity's RH-equivalence lives on the full test space, which no finite instrument spans. (ii) The margin must be defined per unit $L^2$ mass (a Rayleigh quotient); raw Gram bottom eigenvalues conflate form marginality with basis redundancy (v0's $-1.9\times10^{-16}$ read partially that way; this round's instrument separates them).

Scope note for honesty: the law is the floor of the modulated-Gaussian single-mode family at scale $\sigma$, first-zero-dominated; it is a lower bound on nothing and an upper bound on the full-space infimum. Its role is coordinates, not a theorem about all of Weil positivity.

## 2. Axis 2 (SP4, the C1 number): the residual does not bind in the tested range

$x_0 = 2..6$ (primes to $e^6 = 403$), spectral meter fixed at the object's emergent spectrum ($T = 100$, $10^{-4}$ localization): the two-sidedness residual is flat at $2\times10^{-8}$-$1\times10^{-7}$ on both the true zeros and the object's own spectrum, max relative $3.9\times10^{-8}$. No degradation with window depth: at this spectral meter, every tested prime window closes. The C1 gap sits below this measurement's floor throughout; making it bind needs a deeper ladder (larger $x_0$ with the zero-side ceiling raised in step), which is exactly the two-meter law's coupled-growth direction.

## 3. Axis 3 (the carrier): descent exact and D-H invisibility scale-robust

$L = 8, 10, 12, 14, 16$: the descent identity (fold = sampled multiplier) holds at $\le 9.7\times10^{-10}$ at every circumference; $|m|$ at the grid point nearest each true zero tracks the grid offset (corr 0.68-0.88: the carrier's resolution law); and the **D-H off-line landmark stays invisible at every circumference** (relative $|m|$ over the window: 0.252, 0.413, 0.289, 0.238, 0.253: never below 0.238, against $4\times10^{-4}$ dips at genuine zeros). The completeness failure of the control is not an artifact of one carrier scale.

## 4. Verdict and hand-off

Frontier UNMOVED (the ladder is measurement on the v0 object). What it banks: the closed-form margin law with its $\gamma_1^2$ exponent and $\omega^* = 0$ geometry; the certification-cost reading of C2 ($e^{\gamma_1^2\sigma^2}$ per window scale at fixed assembly accuracy); C1 not binding at the tested meters; the scale-robust invisibility certificate. Handed forward: (1) make the certification-cost statement precise as a theorem about THIS assembly (error propagation from quadrature/truncation constants to the floor $\sigma$); (2) the coupled SP4 ladder ($x_0$ and the spectral ceiling grown together) to find where C1 first binds; (3) the D-H invisibility certificate as a provable lower bound on $|m_{DH}|$ over the landmark window from its coefficient lattice (unchanged from #179).
