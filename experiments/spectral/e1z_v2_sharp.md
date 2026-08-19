# E1Z: the sharp form of Theorem V2

> Companion to `e1z_v2_sharp.py` / `.npz`. Closes the one item LEARNINGS #172
> left open in the Christoffel gauge, carried in TODO as "Sharpen Theorem V2
> (new, from V8)". Pure potential theory: no arithmetic input, no L-function
> is evaluated, no zero list is read. It proves nothing about RH, and Z8 shows
> why it cannot. **11/11 checks pass in full mode** (69 s).

## The question

Theorem V2 (#172) is a lower bound on the germ length in terms of the gap
geometry alone. For a probability measure with $M$ atoms in $E = \pm[g,T]$,

$$\lambda_M(0) \;\le\; \cosh(2nG)^{-2}, \qquad n = \lfloor (M-1)/2\rfloor,\quad
G = \tfrac12\operatorname{arccosh}\frac{T^2+g^2}{T^2-g^2},$$

with $G$ the Green's function of $\mathbb{C}\setminus E$ at $0$. V8 measured
its tightness residual $\rho = \log(1/\lambda)/(2\log\cosh 2nG)$ on an
equally spaced $(g,T,M)$-matched surrogate and found that it does **not**
saturate: $\rho \sim 0.48\log T$. So the bound is order-tight on the buildable
window and loses a slowly growing factor asymptotically. What was left open
was a sharp version that captures that factor.

## One-line result

**The correct exponent is not $G$ but the equilibrium discrepancy
$\Gamma(\sigma)$ of the atoms' limiting distribution, and Theorem V2 is
exactly the case $\sigma = $ equilibrium measure.** Writing
$U^\sigma(x) = -\int\log|x-y|\,d\sigma(y)$,

$$\frac{1}{M}\log\frac{1}{\lambda_M(0)} \;\longrightarrow\; 2\,\Gamma(\sigma),
\qquad
\Gamma(\sigma) \;=\; \max_{y\in E} U^\sigma(y) \;-\; U^\sigma(0),$$

so $\rho \to \Gamma(\sigma)/G$. For $\sigma$ the equilibrium measure of $E$,
$U^\sigma$ is constant on $E$ and $\Gamma = g_E(0) = G$ exactly, recovering
V2's Chebyshev rate; for every other $\sigma$, $\Gamma > G$ strictly. The
missing $\log T$ is the equilibrium discrepancy of **equal spacing**:

$$\Gamma_{\text{unif}}/G \;=\; \tfrac12\log T + O(1), \qquad
\text{maximizer at } y^\star = \sqrt{gT},$$

so the constant is exactly $1/2$ and #172's measured $0.48$ is the finite-$T$
approach to it.

## Where it comes from

The identity #172 already uses,
$1/\lambda_M(0) = \sum_j \ell_j(0)^2/w_j$, turns the Christoffel problem at
full degree into a Lagrange-interpolation one. Then

$$\frac{1}{M}\log|\ell_j(0)| \;=\; \frac1M\sum_{i\ne j}\log|y_i|
\;-\; \frac1M\sum_{i\ne j}\log|y_j-y_i|
\;\longrightarrow\; U^\sigma(y_j) - U^\sigma(0),$$

and the sum over $j$ is dominated by its largest term, giving
$2\max_{y\in E}[U^\sigma(y) - U^\sigma(0)]$. The weights contribute only
$O(\log M)$ to $\log(1/\lambda)$, hence nothing to the rate.

The reading is a Runge phenomenon. V2's Chebyshev polynomial is optimal for
nodes at the mapped Chebyshev points of $E$; a real configuration is not
there, and the bound is lossy by exactly how far its distribution sits from
the equilibrium measure. V2 keeps the atoms' **support** and discards their
**distribution**, and $\Gamma - G$ is the price.

## The measurements

All at $g = 13.6$ (the FE budget of #172's V8b), equal weights, symmetric
configurations.

**Z2, independent replication of V8b.** A different assembly of the same
quantity (log-Lagrange weights plus a `logsumexp`, so no extended precision
and $M$ well past the $\sim 2000$ the direct mpmath product costs) reproduces
#172's predictor across the whole table, worst deviation $5\times10^{-4}$:

| $T$ | 30.4 | 56.5 | 100.5 | 157.1 | 226.2 | 402.1 | 760.3 | 1413.7 |
|---|---|---|---|---|---|---|---|---|
| $M$ | 6 | 22 | 58 | 112 | 186 | 406 | 920 | 1988 |
| #172 $\rho$ | 1.143 | 1.332 | 1.570 | 1.762 | 1.924 | 2.190 | 2.494 | 2.797 |
| this run | 1.143 | 1.331 | 1.570 | 1.762 | 1.924 | 2.190 | 2.494 | 2.797 |

with the slopes $d\rho/d\log T$ reproducing to $0.001$ as well
(0.304, 0.414, 0.429, 0.445, 0.462, 0.477, 0.488). The $0.48$ finding is
therefore replicated, not inherited.

**Z3/Z4, the rate.** Pushed by the adversary round to $M = 25600$ for the
uniform family, where the gap to $\Gamma/G$ is $+0.0049$ and still
contracting $1.77\times$ per doubling with no sign of an overshoot. At
$T = 1000$, $G = 0.0136008$ and
$\Gamma_{\text{unif}} = 0.0364739$, so $\Gamma/G = 2.6817$.

| $M$ | 100 | 200 | 400 | 800 | 1600 | 3200 | 6400 |
|---|---|---|---|---|---|---|---|
| $\rho$, equilibrium nodes | 3.691 | 1.915 | 1.385 | 1.179 | 1.086 | 1.042 | 1.021 |
| $\rho$, uniform nodes | 3.598 | 2.613 | 2.570 | 2.605 | 2.635 | 2.654 | 2.666 |

(measured contraction: the equilibrium excess over $1$ shrinks $2.02\times$
per doubling of $M$, the uniform gap to $\Gamma/G$ shrinks $1.75\times$; at
$M = 6400$ the uniform gap is $0.016$ against a distance to $1$ of $1.666$.)

The equilibrium column falls monotonically to $1$, its excess contracting by
almost exactly $2\times$ per doubling of $M$, i.e. decaying like $1/M$. (An
earlier draft attributed that to a $\log M/M$ weight term; the adversary
round killed the attribution. Measured against $\log(2M)/(2M\Gamma)$ the
ratio drifts steadily from 1.38 to 0.39 across $M = 100$ to $6400$ rather
than settling, so the decay is $1/M$ and the $\log M$ is not there. The
subleading structure is left unidentified rather than guessed at.) The
uniform column climbs to $\Gamma/G = 2.6817$ from below, its gap contracting
geometrically, while its distance to $1$ never shrinks at all. So
$\rho \to 1$ for equilibrium and $\rho \to \Gamma/G \ne 1$ otherwise.

**Z9 (adversary), the rate is not uniform-specific.** The one check that
could have made the whole $\Gamma$ story an artifact of one family: does
$\rho$ go to $\Gamma/G$ for the *zeta* density, whose $\Gamma/G = 8.3521$ at
$T = 1000$ is three times the uniform value? It does, converging from above
where uniform converges from below:

| $M$ | 200 | 400 | 800 | 1600 | 3200 | 6400 | 12800 |
|---|---|---|---|---|---|---|---|
| $\rho$, zeta density | 10.741 | 9.322 | 8.780 | 8.547 | 8.442 | 8.393 | 8.370 |
| gap to $\Gamma/G$ | -2.389 | -0.970 | -0.427 | -0.195 | -0.090 | -0.041 | -0.018 |

the gap contracting $2.2\times$ per doubling. Three distributions spanning a
factor of eight in $\Gamma/G$, all landing on their own $\Gamma$.

**Z5, the inequality.** $\Gamma \ge G$ for every family, with equality only at
equilibrium: $\Gamma/G$ is $1.008$ (equilibrium), $2.682$ (uniform), $8.354$
(Riemann-von Mangoldt density) at $T = 1000$. Theorem V2 is the floor of a
one-parameter family of rates.

**Z6/Z7, the uniform law.**

| $T$ | $10^3$ | $10^4$ | $10^5$ | $10^6$ | $10^7$ | $10^8$ |
|---|---|---|---|---|---|---|
| $\Gamma/G$ | 2.6817 | 3.8050 | 4.9521 | 6.1028 | 7.2542 | 8.4204 |
| slope $d(\Gamma/G)/d\log T$ | | 0.4878 | 0.4982 | 0.4998 | 0.5000 | 0.5065 |
| argmax$/\sqrt{gT}$ | 0.99999 | 1.00000 | 1.00002 | 0.99999 | 1.00002 | 1.00009 |

The slope converges to $1/2$, and for this family the maximizer of $U^\sigma$
on $E$ sits at the geometric mean $\sqrt{gT}$, the midpoint of the band in
the logarithmic coordinate, to five digits at every height. **That last fact
is uniform-specific, not a property of the band**: the adversary round
measured the Riemann-von Mangoldt density maximizing at $3.29\sqrt{gT}$
instead, so $\sqrt{gT}$ belongs to the corollary and not to the general
statement. The $T = 10^8$ row is at the edge
of the scan resolution and should be read as such: the argmax ratio has
drifted to $1.00009$ and the slope overshoots to $0.5065$, both artefacts of a
fixed grid on a band that is now $10^8$ wide. The clean reading is $T \le
10^7$, where the slope is $0.4998$ and $0.5000$.

## The two-sided finite-M form

The caveat below used to read "this sharpens the rate, not a two-sided
finite-M inequality". That was too pessimistic: the finite-M statement is
available in two lines and was simply never written down. Since
$1/\lambda_M(0) = \sum_j \ell_j(0)^2/w_j$ is a sum of $M$ positive terms it
lies between its largest term and $M$ times it, so with the **discrete**
equilibrium discrepancy $\Gamma_M = \max_j \frac1M\log|\ell_j(0)|$:

> **THEOREM V2-TWO-SIDED.** For any $M$ distinct nonzero atoms with weights
> $w_j$,
> $$2M\Gamma_M + \log\frac{1}{w_{\max}} \;\le\; \log\frac{1}{\lambda_M(0)}
> \;\le\; 2M\Gamma_M + \log\frac{M}{w_{\min}}.$$
> **Proof.** $\max_j a_j \le \sum_j a_j \le M\max_j a_j$ with
> $a_j = \ell_j(0)^2/w_j$, then $w_{\min} \le w_j \le w_{\max}$ and
> $\max_j \ell_j(0)^2 = e^{2M\Gamma_M}$. $\square$

So $\log(1/\lambda_M(0)) = 2M\Gamma_M + O(\log(M\,w_{\max}/w_{\min}))$: a
window of width $\log(M w_{\max}/w_{\min})$ around a centre that grows like
$M$, which pins $\log(1/\lambda)$ to relative accuracy $O(\log M/M)$ and
carries the weights explicitly and nowhere else. Theorem V2 is the one-sided
closed form in $(g,T,M)$; this is the two-sided form in the actual
configuration, and $\Gamma_M \to \Gamma(\sigma)$ supplies the rate. Verified
(Z10) on all three families at $M = 100, 400, 1600$, the measured position
sitting between 0.24 and 0.57 of the way across the window in every cell.

**The unequal-weight case goes with it (Z11).** Spreading the weights over
four orders of magnitude at $M = 1600$ moves the offset
$\log(1/\lambda) - 2M\Gamma_M$ from 11.29 to 11.92 while the predicted window
widens from 7.38 to 14.66, and the offset stays inside the window at every
spread. The weights cannot move the rate because they never appear outside
that logarithm.

## What it does NOT do

**Z8, the typing.** $\Gamma$ is a functional of $\sigma$ alone. Randomizing
every atom inside its own cell, which preserves $\sigma$ exactly while
destroying every arithmetic relation among the positions, moves $\rho$ by
$O(1/M)$ (measured $0.018$ at $M = 1600$). So the sharpened rate is geometry
in the same sense V8c established for the drift itself, and closing this
residual does **not** reopen the pointwise route. That is the expected answer,
not a disappointment: #172's continuity obstruction says a continuous
functional of finitely many atom positions cannot see $\mathbb{Q}$-linear
independence, and $\Gamma$ is a functional of the limiting *distribution*,
which is even further from the atoms than that.

## Caveats

- The finite-$M$ sandwich above is exact and carries the weights, but it is
  stated in terms of the **discrete** $\Gamma_M$. What is still not effective
  is the convergence $\Gamma_M \to \Gamma(\sigma)$ itself: the measurements
  give the contraction rates (roughly $1/M$ at equilibrium, $1.75$-$2.2\times$
  per doubling elsewhere) but no proved bound on $|\Gamma_M - \Gamma(\sigma)|$
  in terms of a discrepancy between the empirical and limiting distributions.
  That is the one genuinely open step, and it is a standard
  potential-theory-with-discrepancy question rather than anything specific to
  this object.
- $\Gamma(\sigma) \ge G$ with equality iff $\sigma$ is the equilibrium
  measure is asserted here on the strength of the standard variational
  characterization plus the measurements; it is not machine-checked.
- The Riemann-von Mangoldt family is included only as a third distribution to
  separate $\Gamma$ from $G$. Nothing here depends on it being arithmetic.

## Verification targets (VERIFIER, all finite or classical)

1. **$\Gamma \ge G$ with equality iff $\sigma = \omega_E$.** The Frostman
   characterization: $U^{\omega_E}$ is constant on $E$ and minimizes the
   energy, so $\max_E U^\sigma - U^\sigma(0) \ge g_E(0)$ for every $\sigma$
   supported on $E$. Classical, and the cleanest formal statement here.
2. **The interpolation identity** $1/\lambda_M(0) = \sum_j \ell_j(0)^2/w_j$
   at full degree (already listed as a #172 target; unchanged).
3. **The uniform potential in closed form**: $U^\sigma$ for $\sigma$ uniform
   on $\pm[g,T]$ is elementary (two $x\log x$ antiderivatives), and its
   maximum over $E$ is at $\sqrt{gT}$. Finite calculus, no measure theory.
4. **$\Gamma_{\text{unif}}/G = \tfrac12\log T + O(1)$** as $T\to\infty$ at
   fixed $g$, which is target 3 plus the asymptotics of
   $G = \operatorname{arccosh}(\cdot)/2 \sim g/T$.

## Verdict fields

| field | value |
|---|---|
| `sharp_rate` | $\frac1M\log(1/\lambda_M(0)) \to 2\Gamma(\sigma)$, $\Gamma = \max_E U^\sigma - U^\sigma(0)$ |
| `v2_is_the_equilibrium_case` | YES. $\Gamma = G$ exactly at $\sigma = \omega_E$, and $\rho \to 1$ there (measured) |
| `v2_sharp_iff` | the atoms are equilibrium-distributed; every other $\sigma$ gives $\Gamma > G$ strictly |
| `the_missing_log` | the equilibrium discrepancy of equal spacing: $\Gamma/G = \frac12\log T + O(1)$, maximizer $\sqrt{gT}$. #172's 0.48 is the finite-$T$ approach to exactly one half |
| `v8b_replicated` | YES, independently: 8/8 points to $5\times10^{-4}$, slopes to 0.001, via a different assembly |
| `arithmetic_content` | NONE, provably: $\Gamma$ depends only on $\sigma$ (Z8), confirming V8c's typing rather than reopening the pointwise route |
| `frontier_delta` | ZERO. A potential-theory residual closed; M4 untouched |
