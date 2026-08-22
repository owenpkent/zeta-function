# E2AW: the energy of the Xi-state: the naive gap at $a = 1$, the crossover at $a = 1.5$, and the instrument's horizon

**Date**: 2026-08-21. **Status**: BUILDER round, executed; 10/10 checks (4751 s; dps-80 protocol on the 110-digit zero cache, 1069 zeros to $T = 1500$). **Code**: [`e2aw_energy_gap.py`](e2aw_energy_gap.py). **Data**: `e2aw_energy_gap.npz` (tracked). **Executes**: B2c-gap, the coda of the B2c chain (#183-#190), and the last open item of the arc.

## 0. The three readouts

**Readout 1 (the naive B2c-gap, answered where it is well-posed).** At $a = 1$, the one rung below the horizon (Readout 2), the $\Xi$-state pays a REAL energy premium: the kernel's true window energy is $10^{-14.0}$ against the instrument's certified bottom $\lambda_0 = 10^{-24.1}$: ten orders of magnitude. The instrument's ground state there is $\Xi$-shaped to 5 percent (#184) yet sits ten orders deeper than the EXACTLY $\Xi$-proportional kernel: at these depths the bottom is so shape-sensitive that a 5-percent $L^2$ deviation from $\Xi$ buys ten orders of energy. Any corrected selection principle for (1.2) must respect that sensitivity: pointwise shape convergence and energy ordering are almost decoupled coordinates.

**Readout 2 (the pincer: the pre-registered crossover FIRED, at the first rung past $a = 1$).** The kernel's full-line Mellin transform vanishes exactly at every on-line zero (fact E3 below), so its windowed Weil-form energy is controlled by the window-truncation tails alone, and the certified bound $B(a)$ collapses doubly-exponentially. It crosses BELOW the instrument's certified bottom at $a = 1.5$ and the gap then explodes:

| $a$ | 1.0 | 1.5 | 2.0 | 2.5 | 3.0 | 3.5 | 4.0 |
|---|---|---|---|---|---|---|---|
| $\lg \lambda_0$ (instrument bottom) | $-24.1$ | $-42.3$ | $-46.0$ | $-48.7$ | $-50.7$ | $-52.9$ | $-55.2$ |
| $\lg B$ (kernel energy, certified bound) | $-13.1$ | $-45.9$ | $-138.2$ | $-392.1$ | $-1085.8$ | $-2975.2$ | $-8114.9$ |
| $\lg$ (sharp value, where cancellation permits) | $-14.0$ | $-46.9$ | $-139.5$ | | | | |
| $\lg(\lambda_0 / B)$ | $-11$ | $+4$ | $+92$ | $+343$ | $+1035$ | $+2922$ | $+8060$ |

From $a = 1.5$ on, the $\Xi$-shaped kernel is a strictly deeper trial state than anything the instrument resolves: 4 orders at $a = 1.5$, 92 at $a = 2$, 8060 at $a = 4$. The continuum window bottom satisfies $\lambda_0^{\mathrm{cont}}(a) \le B(a)$, unconditionally.

**Readout 3 (the horizon law).** $\lg B(a)$ tracks $-2\pi e^{2a}/\ln 10$ with a slowly growing polynomial offset ($+7$ to $+20$ decades across the ladder), and the tail integral $T_1 = \int_a^\infty |k|$ matches the analytic scale $e^{-\pi e^{2a}}$ to the leading digit at every rung ($\lg T_1$: $-8.0, -24.8, -71.3, -198.8, -546.2, -1491.4, -4061.9$ against $\pi e^{2a}/\ln 10$: $10.1, 27.4, 74.5, 202, 550, 1494, 4066$). Consequence, priced: resolving the continuum valley at window $a$ needs working precision $\sim 2\pi e^{2a}/\ln 10$ digits AND a basis whose approximation floor matches: $\sim 140$ digits at $a = 2$, $\sim 1100$ at $a = 3$, $\sim 8100$ at $a = 4$; the knot count for a fixed-degree spline basis grows exponentially alongside. Direct minimization cannot see (1.2)'s object beyond $a \approx 1.5$-$2$ at any realistic precision.

## 1. The exact facts the pincer rests on (each verified in-run)

- **(E1) The seed is exact.** With $\alpha = 2\sqrt6/3$ (closed form: $\int \psi_n = \psi_n(0)$ for Fourier-self-dual $\psi_n$ of eigenvalue $+1$, so the vanishing-integral condition IS $h(0) = 0$), the seed $h = \psi_0 - \alpha\psi_4$ has $\int h = 0$ and $h(0) = 0$ exactly. Verified: $|\int h| = 1.4\times10^{-81}$, $h(0) = 0.0$ at dps 80. (e2av used a float-trapezoid $\alpha$; the closed form is new bookkeeping.)
- **(E2) $k = E(h)$ is exactly even in log coordinates** (Poisson with $\hat h = h$, $\int h = h(0) = 0$). Verified: relative defect $\le 2.5\times10^{-45}$ at sample points: the theta mechanism, watched working at full precision.
- **(E3) The full-line Mellin transform vanishes at every on-line zero.** $\hat k_{\mathrm{full}}(z) = \zeta(\tfrac12 - iz)\,\tilde h(\tfrac12 - iz)$ (absolute convergence for $\Re s > 1$; the two-sided decay from E2 makes the transform entire; continuation gives the line). Hence $\hat k_{\mathrm{win}}(\gamma_b) = -(\text{FT of the two tails})(\gamma_b)$, and $Q(k_{\mathrm{win}}) \le 2\sum_b \min\big(2T_1,\, 2(|k(a)| + T_1')/\gamma_b\big)^2$ plus a density-tail term with an $e^{a}$ allowance for potential off-line zeros above the certified cutoff. VERIFIED NUMERICALLY at $a = 1$: the direct oscillatory window integral equals minus the tail FT to relative deviation $8\times10^{-73}$, $1\times10^{-73}$, $2\times10^{-74}$ at $\gamma_1, \gamma_2, \gamma_{10}$: the identity is exact at working precision, not an approximation.

Bound soundness closed the loop where cancellation permits a sharp value: $Q_{\mathrm{sharp}}/\|k\|^2 \le B$ at $a = 1.0, 1.5, 2.0$ with a factor $\sim 8$-$20$ slack (digits-left at the $a = 2$ sharp sum: 9, so its two significant figures stand).

## 2. Machinery parity (the instrument is the same one, bit for bit)

The ported builder reproduces `HardWindowGS` exactly ($|\Delta\lg\lambda_0| = 0.0$ at $a = 1, 1.5$); the fresh dps-80 $\lambda_0$ ladder matches e2as at the gated rungs ($-24.1$ vs $-24.1$, $-42.3$ vs $-42.4$) and, informationally, matches e2au's dps-110 values at $a = 3, 3.5, 4$ TO THE DISPLAYED DIGIT ($-50.7, -52.9, -55.2$): the resolvable bottom is dps-robust, i.e. a real property of (basis, truncated form), not solver noise. The mp projection reproduces e2av's float proximity curve to four decimals at every rung ($0.9988, 0.9880, 0.9391, 0.8759, 0.8133, 0.7569, 0.7152$): READOUT 2 of #190 revalidated in passing at higher precision.

## 3. What the crossover re-scopes (the honest ledger)

The bridge assumption, previously implicit, now measured and FAILED beyond $a^* \in (1, 1.5]$: "the instrument's certified bottom tracks the continuum ground state." Consequences for the arc's wording:

- **#185(ii) ("if the trend continues, the conjectured limit needs modification"): WITHDRAWN beyond $a^*$.** The certified narrowing through $a = 4$ (#189) stands as measured, as a statement about the RESOLVABLE-SUBSPACE optimum: the deepest state expressible at knot pitch $1/56$ and dps 80-110. It says nothing about the continuum object once the true valley is $10^{-92}$-and-beyond below the basis floor.
- **#189(iii)'s dichotomy gains the branch that fires.** "Collapse + proven kernel limit coexist only if the proximity fails" had a third branch: the instrument lost the continuum bottom. It did, at $a^*$; the certified collapse and CCM's Lemma 7.3 coexist with NO tension about (1.2) itself.
- **#190's proximity decay: re-scoped, not retracted.** $|\cos(k_\lambda, \xi_\lambda)|$ decays exactly as measured, where $\xi_\lambda$ is the resolvable optimum. CCM's "educated guess" concerns THEIR operator's actual ground state: nothing certified here contradicts it. At $a = 1$ (below the horizon) everything agrees at $0.9988$.
- **What is NOT withdrawn:** the $a = 1$ transient (#184) is below the horizon and real; the $a = 1$ energy premium of the exact $\Xi$-state (Readout 1) is real; the collapse phenomenology (#185/#189) is real about the instrument class every published numeric also belongs to.

The same lens re-reads the sibling literature: CCM's own proximity evidence spans $\lambda \le 6$ ($a \le 1.79$), straddling the horizon (at $a = 1.79$, $B \sim 10^{-88}$: past any double-precision floor); Groskin's arithmetic-side ladder measures $\lambda_{\min} \approx 10^{-334}$ at basis $N = 250$, dps 500, while his own extrapolation and Connes' Section-6.4 law put the true value near $10^{-537}$/$10^{-530}$: a floor sitting $\sim 200$ orders above the target, the arithmetic-side face of the same crossover. The zero-side horizon here is the first CERTIFIED instance (the kernel is an explicit witness; the bound is unconditional).

## 4. Scope and caveats

Quadrature-level rigor (mp integrals of positive integrands for the bounds; interval-arithmetic upgrade named below); the kernel is OUR admissible trial state (Hermite-limit seed: the pincer needs nothing about CCM's prolate kernel, and its $\Xi$-proximity is e2av Readout 1: scalar multiple to six decimals); R(Pk), the WITHIN-basis Rayleigh quotient of the projected kernel, is floor-typed at every rung (the projection residual's energy dominates it: $\lg$ resid$^2$ $= -11.4$ at $a = 1$, edge-layer-driven since splines vanish at $\pm a$ while $k$ does not, and $-39.4$ from $a = 1.5$ on, the interior approximation floor at pitch $1/56$): so R(Pk) measures the basis's kernel-representation floor, and the honest kernel energies are the sharp values and $B(a)$. The above-cutoff zero allowance carries $e^{a}$ for potential off-line zeros beyond $T = 1500$; zeros to the cutoff are certified on-line in the cache. Frontier verdict: UNMOVED (a diagnostic of the corpus's numerical approach; zeros consumed by design).

## 5. Hand-off

(i) **P12 Section 7**: this round supplies its closing content (drafted same-day). (ii) Optional hardening: interval arithmetic on the three tail integrals and the zero sum turns $B(a)$ into a theorem about the windowed kernel; the exact seed facts (E1) are a self-contained VERIFIER candidate (Gaussian-Hermite integrals). (iii) The courtesy-communication option to the 2511.22755/2606.09096 authors (Owen's call after P12) now carries a sharper message: their kernel is variationally excellent (doubly-exponentially near-null), their guess is untouched by every certified collapse in range, and the conjecture's numerics are horizon-limited for EVERY direct-minimization instrument including theirs and ours. (iv) The B2c chain is COMPLETE: A1/A2/B2b/B2c/-hard/-deep/-deep2/-obj/-lit/-prox/-gap all executed.
