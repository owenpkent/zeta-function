# E2AY: the function-field twin: the F_q column measured, and the per-cell difference IS the missing structure

**Date**: 2026-08-23. **Status**: BUILDER round, executed; 13/13 checks (3.3 s). **Code**: [`e2ay_ff_twin.py`](e2ay_ff_twin.py). **Data**: `e2ay_ff_twin.npz` (tracked). **Executes**: backlog Family-C item C1 (the shadow instance). **Instance**: the e2b curve $E: y^2 = x^3 + x + 1$ over $\mathbb{F}_5$ ($q = 5$, $N_1 = 9$, $a = -3$, $h = 9$, $g = 1$; Hasse margin $2\sqrt5 - 3 = 1.472$). **K1 posture**: build phase consumes point/divisor counts only (guard: 0 oracle calls); the $Z$-formula oracle is validation-phase.

## 0. What was built

The e2an SP-object mechanics (Muntz descent, multiplier extraction by FFT, dip detection, log-derivative extraction, trace-formula two-sidedness, polarization cells) run on the curve's divisor lattice: coefficients $b_n = \#\{\text{effective divisors of degree } n\}$ on the single progression $\{n\log q\}$, anchored at the bottom by DIRECT point counting over $\mathbb{F}_{5^k}$, $k \le 4$ (e2b's field arithmetic), through the place-count Euler product (exp-of-series; matches the closed form $b_n = h(q^n-1)/(q-1)$ to $0.0$).

**The one structural adaptation, itself a finding (the pole-array cell).** Zeta has ONE pole and e2an regularizes with a single $R\,I_1 e^{-s}$ term. The FF world has pole ARRAYS at $\Re s = 1$ AND $\Re s = 0$ (period $2\pi/\log q$): the zeta-style regularizer fails catastrophically (measured median defect $3.5\times10^{14}$ at the FF window: the uncancelled $e^{-s}$ array integrated to $s = -70$), while the finite partial-fraction structure $Z(T) = 1 - \frac{h/(q-1)}{1-T} + \frac{h/(q-1)}{1-qT}$ supplies the full geometric-array regularizer from lattice data alone ($h = b_1$), reducing the integrand to a form in which NO $b_n$ is ever materialized, and making the extraction EXACT AS AN IDENTITY (verified: extracted $m(\tau) = Z(\tfrac12 + i\tau)$ to $1.9\times10^{-12}$; the raw-vs-reduced identity to $1.2\times10^{-12}$ on the window where the raw form's own $q^n$-scale float cancellation permits it). Two corollaries recorded: the FF descent window must extend until $e^{s/2}$ underflows the target (the left tail is a periodic spike train, not zeta's pole-cancelled dead continuum), and the reduced form is the numerically correct implementation, not a convenience.

## 1. The F_q column (all cells measured this run)

- **Engine**: $m = Z(\tfrac12+i\tau)$ to $1.9\times10^{-12}$; cross-probe $3.9\times10^{-11}$.
- **Duality**: real on the line with NO completion factor ($5.2\times10^{-9}$, at the extraction floor): the archimedean place is absent.
- **SP2 spectrum**: 51/51 predicted zeros found, 0 spurious; refined by bisection on the real multiplier to $8.9\times10^{-16}$; the spectrum is EXACTLY the periodic pair array $(\pm\theta + 2\pi k)/\log q$ (spacings $= 2\pi/\log q$ to $4.4\times10^{-16}$): the rung-2 arithmetic progression, measured. Completeness here is a THEOREM (Hasse) and is measured complete.
- **SP3 Euler**: the degree-variable log-derivative (free-semigroup Cauchy division) returns $\lambda_n = N_n \log q$ to $2.5\times10^{-14}$ ($n \le 20$), anchored to direct counts $N_{1..4} = 9, 27, 108, 675$.
- **SP4 trace formula**: EXACT (Grothendieck-Lefschetz): zero-side traces $2q^{n/2}\cos(n\hat\theta)$ equal prime-side traces $q^n + 1 - N_n$ to $2.4\times10^{-11}$ through $n = 12$, limited only by zero refinement ($\hat\theta$ to $8.9\times10^{-16}$).
- **SP5 polarization**: INHABITED and measured: $|\alpha|^2 = (\hat t_1^2 - \hat t_2)/2 = 5.0000000000$ (the on-circle statement = FF-RH), Hasse margin $2\sqrt q - |\hat t_1| = 1.4721$, $O(1)$: and here it is a theorem with a named source (Hodge index / Castelnuovo).
- **Carrier**: every place on ONE rational progression ($a_d = 9, 9, 33, 162, 612, 2571, \ldots$ at $\{n\log q\}$): a commensurable lattice.

## 2. The deliverable: the per-cell zeta-vs-$\mathbb{F}_q$ table

| Cell | zeta (e2an, measured) | $\mathbb{F}_q$ curve (this run, measured) | The difference = the missing structure |
|---|---|---|---|
| $H^0$ / pole | one simple pole; residue $1.0005$, exponent $0.5000$ | pole ARRAYS (period $2\pi/\log q$); single-pole regularizer fails at $10^{14}$, array form exact at $10^{-12}$ | the FF $\tau$-line is a compact circle; zeta's is a line: one pole against a continuum |
| Duality / FE | real only after the $\pi^{-z/2}\Gamma(z/2)$ completion ($<10^{-5}$) | real bare, no factor ($5\times10^{-9}$) | the archimedean place: present for zeta, absent for $\mathbb{F}_q$ |
| SP2 completeness | 29/29 zeros to $T=100$ at $1.3\times10^{-4}$; completeness = RH, unprovable from the object; D-H control: off-line pair invisible | 51/51 at $8.9\times10^{-16}$; completeness = Hasse's THEOREM | the completeness gap IS RH; the shadow has it for free |
| SP3 Euler | $b_n = \Lambda(n)$ exact; support = prime powers on the $\mathbb{Q}$-linearly independent $\{\log p\}$ | $\lambda_n = N_n\log q$ exact; support on ONE progression | the S4/R1 coordinate (#162/#172/#188): incommensurable vs commensurable log-lattice |
| SP4 trace formula | two-sided to a finite-scale residual ($2.5\times10^{-8}$ truth, $1.0\times10^{-7}$ object) | EXACT (Lefschetz), $2.4\times10^{-11}$ = refinement floor | Frobenius exists as an operator with a fixed-point formula; zeta's is the missing R1 |
| SP5 polarization | margin $-1.9\times10^{-16}$ on $\lambda_{\max} = 1.27$: ZERO at machine precision (marginal; e3v/#180 class) | $\|\alpha\|^2 = q$ at $10^{-10}$, margin $1.4721$, $O(1)$; source: Hodge index, a theorem | M4: the polarization zeta must supply is inhabited, quantitative, and theorem-backed in the shadow |
| Emergent spectrum shape | zeros irregular (GUE-class statistics) | exact arithmetic progressions, step $2\pi/\log q$ | commensurability again, spectrum-side |

Reading of the table against the interface doc: in the shadow BOTH open joints close: C1 (counting side) by an actual Frobenius with an exact Lefschetz formula, C2 (the polarization) by the Hodge index theorem with an $O(1)$ measured margin: while zeta's column carries a finite-scale residual at C1 and a machine-zero margin at C2. The missing object's spec, displayed as two measured columns of one pipeline.

## 3. Scope and caveats

Float throughout (all cells are relative comparisons at $10^{-9}$-$10^{-16}$); the FF instance's "oracle" ($Z$ from $P(T)$) is itself computable from lattice data ($a = q + 1 - N_1$), so the build/validation split is a discipline formality here, kept for pipeline symmetry; genus 1 only (one zero pair per period): higher-genus curves would populate the period with $2g$ zeros and are the natural extension; the e2an zeta-column numbers quoted in the table are that run's, not re-measured here. Frontier verdict: UNMOVED (the shadow column is a control and a coordinate display; nothing about zeta moved).

## 4. Hand-off

(i) **The standing regression control**: any future SP-candidate for zeta drops into this pipeline next to a column where every cell is exact and theorem-backed; deviations per cell are the diagnosis. (ii) Higher-genus extension (genus 2 curve: 4 zeros per period, tests the multi-pair completeness logic) is cheap if ever needed. (iii) The pole-array finding sharpens the C4 (Lean interface) plan: the FF instance's `SPInterface` fields now have measured witnesses to formalize against. (iv) The table's SP4/SP5 rows are the cleanest two-line statement of what M4/R1 must supply, suitable for the interface doc's rung ladder.
