# The acoustic reframing: passive medium (Euler product) vs lossless medium (RH)

> Thread opened 2026-06-13 from Owen's suggestion that RH connects to acoustic
> modeling. Step 1 was an adversarial reverse-engineering workflow
> (`acoustic-rh-step1`); Step 2 is two local probes,
> [`eac1_impedance_passivity.py`](../../experiments/acoustic/eac1_impedance_passivity.py)
> and [`eac2_ff_passive_lossless.py`](../../experiments/acoustic/eac2_ff_passive_lossless.py).
> Verdict: the acoustic frame is the right LANGUAGE for the missing positivity,
> not a new lever by itself. It earns its keep by splitting RH cleanly and
> locating the gap precisely. Honest scope is in the last section.

## The one-line result

RH's positivity factors into **two different statements**, and a passive-network
reading separates them where every prior attempt in this repo conflated them:

| Piece | Acoustic meaning | Logical status |
|---|---|---|
| **Comb / prime-side positivity** ($\Lambda(n) \ge 0$) | the medium is **passive** ($Z=-\zeta'/\zeta$ is the Laplace transform of a positive measure) | **unconditional** = the Euler product; **separates D-H** |
| **Line-location positivity** (poles of $Z$ on $\mathrm{Re}=\tfrac12$) | the medium is **lossless** (reactance one-port; poles on $i\mathbb{R}$ after the $\tfrac12$-shift) | $=$ **RH**; circular (R3.5 trace side) |

The new mathematics is neither end: it is the **coupling** that turns passive into
lossless. In the function field that coupling is a theorem (Hodge index /
Castelnuovo-Severi); over $\mathrm{Spec}(\mathbb{Z})$ it is exactly the missing M4
polarization, now restated as "the arithmetic medium is provably contractive."

## The dictionary (Weil explicit formula as a 1D acoustic system)

Read the place-decomposed Weil form $M = A_{\mathrm{arch}} + P_{\mathrm{fin}} +
B_{\mathrm{pole}}$ as a semi-infinite vibrating string / lossless transmission line:

- **zeros of $\zeta$** $=$ resonant frequencies of the medium (Deninger's needed
  $\mathbb{R}$-flow $=$ the wave propagator);
- **$B_{\mathrm{pole}}$** (pole at $s=1$) $=$ the $+1$ time-like direction of the
  Minkowski energy form / the boundary drive at the semi-infinite end;
- **$P_{\mathrm{fin}}$** (prime side, Frobenius correspondence) $=$ the discrete
  impedance atoms spaced $\log p$ (a Brune passive comb); exists iff Euler product;
- **$A_{\mathrm{arch}}$** (Gamma factor) $=$ the radiation/limit-point tail at infinity;
- **non-compactness of $\mathrm{Spec}(\mathbb{Z})$** $=$ the string is semi-infinite
  (Weyl limit-point case);
- **finding #80 (moment matrix never flat)** $=$ the string sits on the
  indeterminate-moment / limit-point boundary (the sharpest new-to-repo mapping).

The **Lorentzian $(1,n-1)$ Hodge signature** is NOT the (positive-definite) energy
of a physical string; it is the **spacetime d'Alembertian** energy-momentum form,
$+1$ on the time/pole direction and $-1$ on the spatial prime+archimedean modes.
The match is FORCED by choosing the wave-operator energy form, not free.

## Probe 1 (EAC.1): the impedance, passive vs active

The driving-point impedance $Z_L(s) = -L'/L(s) = \sum_n \Lambda_L(n)\,n^{-s}$ is
the Laplace transform of the generalized von Mangoldt comb. Since
$(-1)^k Z_L^{(k)}(s) = \sum_n \Lambda_L(n)(\log n)^k n^{-s}$, the medium is
**passive** (complete monotonicity / a positive representing measure) **iff
$\Lambda_L(n)\ge 0$ for all $n$**. Computing the comb exactly:

- **$\zeta$**: $\Lambda(n)$ is the ordinary von Mangoldt comb, $\ge 0$ for every
  $n$ (controls $\Lambda(2)=\Lambda(4)=\log 2$, $\Lambda(6)=0$, $\Lambda(9)=\log 3$
  all verified). PASSIVE, unconditionally.
- **Davenport-Heilbronn**: $\Lambda_{DH}(n)$ goes **negative immediately at
  $n=3$** (the first prime $\equiv 3 \bmod 5$, period-5 coefficient $-\kappa<0$),
  with 59 of the first 200 entries negative. The truncated real-axis impedance is
  even negative ($Z_{DH}(1.5)\approx -0.08$). ACTIVE: no positive representing
  measure, not synthesizable as a passive network.

This is the prime-side D-H discriminator that **e2db's archimedean $m$-function
reading was blind to**: e2db built positivity from $E(z)=\xi(1-iz)$ (the
functional-equation / Gamma side, which D-H also has), so D-H's obstruction was
archimedean-suppressed below the float floor. Sourcing positivity from
$P_{\mathrm{fin}}$ (the prime atoms) instead makes D-H fail loudly at $n=3$.

## Probe 2 (EAC.2): the function-field coupling, verified

Normalize the Frobenius eigenvalues to scattering values $s_i := \alpha_i/\sqrt q$.
Then for a curve $C/\mathbb{F}_q$:

- **passive** (contractive, $\max_i|s_i|\le 1$) $\iff$ $|\alpha_i|\le\sqrt q$
  $\iff$ the primitive intersection form on $C\times C$ is negative definite
  $\iff$ the exact Hodge margin $4g^2q - t^2 > 0$. Positivity from a **signature**
  (the R3.5-escape side), not from assuming the operator is unitary.
- **reciprocal** (functional equation): the multiset $\{\alpha_i\}$ is closed under
  $\alpha\mapsto q/\alpha$, so $\min_i|s_i| = 1/\max_i|s_i|$. UNCONDITIONAL.
- **lossless** (RH): all $|s_i|=1$.

**The coupling**: passive gives $\max|s|\le 1$; reciprocal gives
$\min|s| = 1/\max|s|\ge 1$; with $\min\le\max$ the three force $\max|s|=\min|s|=1$.
In one line,
$$ (\|S\|\le 1)\ \text{AND}\ (\{\alpha\}=\{q/\alpha\}) \ \Longrightarrow\ |\alpha_i|=\sqrt q. $$
Verified on 9 curves (elliptic and genus 2, $q\le 19$): passive 9/9 (exact Hodge
margin), reciprocal 9/9, lossless 9/9, coupling 9/9. This is Weil's two-sided
argument read as network theory: the Hodge-index energy form supplies one
inequality, the functional equation supplies the other, together they pin the
resonances onto the critical circle.

**Marginal positivity, explained.** The passive bound is **never slack**:
$\max|s|=1$ exactly on every curve. A reciprocal passive network is *forced*
lossless and cannot be strictly contractive without breaking reciprocity. So the
project's marginal-positivity thesis ("RH is just barely true, no buffer") is, in
this mirror, the statement that the medium is reciprocal: reciprocity saturates
passivity. Soft/robust proofs fail because there is no slack to spend.

## The Spec(Z) gap, located precisely

The coupling needs three ingredients. Over $\mathrm{Spec}(\mathbb{Z})$:

| Ingredient | Function field | $\zeta$ / $\mathrm{Spec}(\mathbb{Z})$ |
|---|---|---|
| (i) reciprocal symmetry | functional eq. of $Z_C$ | **HAVE IT**: $\xi(s)=\xi(1-s)$ |
| (ii) passive medium | Euler product / Frobenius comb | **HAVE IT**: Euler product (EAC.1) |
| (iii) Lorentzian energy form | Hodge index on $C\times C$ | **MISSING**: no surface $\mathrm{Spec}(\mathbb{Z})^{\times 2}$, no Frobenius graph, so no signature to deliver the one-sided contractivity bound |

We possess **both inputs** to the coupling (symmetry + passivity); the single
missing object is the energy form (iii) whose **signature** makes the arithmetic
medium provably contractive. That is the missing M4 polarization, restated in
acoustic terms. D-H fails at (ii) already (no Euler product = active medium), so
the coupling never even starts for it: the K2 discipline, geometric face.

## Step 3 (EAC.3): reverse-engineering ingredient (iii) - the halving form

Pushing the reverse-engineering one level deeper:
[`eac3_halving_and_allpass.py`](../../experiments/acoustic/eac3_halving_and_allpass.py).

**The halving.** There are two bounds on the resonances. The PASSIVE (trivial)
bound is FREE from the Euler product: function field $|\alpha_i| \le q$ (exponent
1); zeta has no zeros in $\mathrm{Re}>1$ (abscissa 1), exactly because
$Z=-\zeta'/\zeta=\sum\Lambda(n)n^{-s}$ is a convergent positive-comb Dirichlet
series there. The RH bound is the SHARPENED one: $|\alpha_i|=\sqrt q$ (exponent
$\tfrac12$); $\mathrm{Re}=\tfrac12$ (abscissa $\tfrac12$). So **RH is precisely the
statement that the passive bound is HALVED**: exponent $1\to\tfrac12$,
$q\to\sqrt q$, abscissa $1\to\tfrac12$. In the function field the halving is a
theorem (the Hodge index on $C\times C$); verified on 9 curves the realized
exponent $\log|\alpha|/\log q = 0.50000$ exactly while passivity alone only gives
$\le 1$. **Ingredient (iii), restated sharply: the energy form whose signature
halves the free passive exponent $1\to\tfrac12$.** This also explains the analytic
ceiling: zero-free-region methods chip the abscissa from 1 toward $\tfrac12$
analytically and stall at the Vinogradov-Korobov $2/3$ exponent, because the
halving is geometric (a signature), not analytic.

**On-shell vs off-shell (a clarification that prevents a trap).** The zeros-side
Weil Gram $W(f)=\sum_\rho \hat f(\rho)^2$ is positive-DEFINITE under RH (signature
$(K,0)$, since the $\hat f(\rho)$ are real; e3c2/e3r). The function-field
intersection form that PRODUCES the bound is LORENTZIAN $(1,n-1)$ (e2g). These are
different forms. The acoustic reading names the difference: the Weil Gram is the
ON-SHELL, lossless spectral form (it already sums over the true zeros, hence
circular); ingredient (iii) is the OFF-SHELL energy form on arithmetic divisor
classes, Lorentzian, from whose signature the zeros emerge. lossless-vs-passive
maps onto on-shell-definite-vs-off-shell-Lorentzian. Do not mistake the (definite,
circular) Weil Gram for the (Lorentzian, productive) polarization.

**The all-pass mechanism (why passivity is necessary but not sufficient).** The
functional equation makes the completed $L$ a lossless all-pass / para-unitary
system, for BOTH zeta and D-H. An off-line zero $\rho$ carries a full orbit
$\{\rho,1-\rho,\bar\rho,1-\bar\rho\}$: a genuine 4-point all-pass section (mirror
pairs straddling the line). An on-line zero degenerates ($1-\rho=\bar\rho$) to a
2-point pair on the axis. So **RH $\iff$ every all-pass section is degenerate
(pinned to the axis)**. Verified: a zeta zero gives a degenerate 2-point orbit;
D-H's $\rho\approx 0.808+85.7i$ gives a genuine 4-point quad. Passivity forbids
sections only in $\mathrm{Re}>1$; the strip $\tfrac12<\beta<1$ is the gap (iii)
must close. D-H's active impedance (signed comb) permits the quad; zeta's passive
impedance does not in $\mathrm{Re}>1$, but passivity alone cannot reach
$\mathrm{Re}=\tfrac12$ - that is the halving form's job.

## Step 4 (EAC.4): where the halving comes from - Poincare duality

[`eac4_arithmetic_diagonal.py`](../../experiments/acoustic/eac4_arithmetic_diagonal.py).
EAC.3 said (iii) must halve the bound; EAC.4 reverse-engineers *why a halving is even
possible*. The answer: **Poincare duality places the self-dual middle weight at the
geometric mean of the two extremes.** Frobenius acts on a curve's cohomology with

$$|H^0| = 1 = q^0, \qquad |H^1| = q^{1/2}, \qquad |H^2| = q = q^1,$$

and the RH modulus $q^{1/2}$ is *exactly* the geometric mean $\sqrt{|H^0|\cdot|H^2|}
= \sqrt{1\cdot q}$ (verified on every curve). Poincare duality $H^i\cong
H^{2-i}(-1)$ pairs $H^0$ with $H^2$ (the two poles of $\zeta_C$) and makes $H^1$
*self-dual*, hence forced onto the self-dual locus $|\alpha|=\sqrt q$ = the critical
line. **The halving is Poincare duality + self-duality of the middle weight, not a
separate positivity.** Equivalently in the primitive intersection form: $|\Delta_0^2|
= 2g$ is $q$-free (the diagonal / weight-0 leg) while $|\Gamma_0^2| = 2gq$ carries
the $q$ (the Frobenius / prime leg); the bound $2g\sqrt q$ is their geometric mean,
and the exponent $\tfrac12$ is the average of the leg weights $\{0,1\}$.

**Arithmetic.** The functional equation $\xi(s)=\xi(1-s)$ IS this Poincare duality:
it pairs the pole at $s=1$ (the weight-2 / $H^2$ leg, residue 1) with the structure
at $s=0$ (the weight-0 / $H^0$ leg), and its fixed locus is $\mathrm{Re}=\tfrac12$ -
the self-dual middle where the zeros (the $H^1$ analogue) must live (FE verified
numerically, residual $\sim 10^{-32}$). zeta HAS the duality (FE) and the passive
medium (Euler product, EAC.1). **The missing ingredient (iii) is the weight-graded
cohomology whose self-dual middle is forced to $\mathrm{Re}=\tfrac12$** -
equivalently, the statement that the arithmetic "$\Delta^2$" (diagonal
self-intersection) is the $q$-free, weight-0 leg. This is exactly Deninger's missing
motivic cohomology, now with a one-line job description: **supply the weight
filtration whose self-dual middle is $\mathrm{Re}=\tfrac12$.** D-H has no pole (it is
entire) = no $H^2$ leg = no geometric mean can form: the geometric face of "D-H has
no surface, no weight ladder, no halving."

The reverse-engineering has thus converged, from the acoustic side, onto the known
Deninger/motivic-weight target - but via a path that simultaneously explains the
$2/3$ analytic ceiling (the halving is geometric, not analytic), the D-H discipline
(no weight ladder without an Euler product), and marginal positivity (reciprocity
saturates passivity). That convergence is a confirmation of the target, not a new
construction of it.

## Honest scope (what is new, what is not)

- **Not new to the literature.** The basic dictionary (zeros = canonical-system
  spectrum; positive mass density $\iff$ Herglotz $m$-function; the explicit
  Hamiltonian-from-$\zeta$) is classical: de Branges (1968), Lagarias (2006,
  RH $\iff$ $E$ Hermite-Biehler), Suzuki (2012, PSD of the Hamiltonian family for
  all $\omega>0$ $=$ RH, unconditional only for $\omega>1$), Krein/Romanov.
- **Does NOT escape R3.5.** The *lossless* positivity ("the $m$-function is
  Herglotz / the string has positive mass") is, by Lagarias, *exactly* RH and is a
  self-adjoint-operator positivity: it is the trace-theoretic side R3.5 forecloses,
  RH-in-a-costume. By Krein's theorem a positive-mass string with any resonances
  exists generically, so "the string is passive" alone constrains nothing.
- **What is genuinely useful here.** (1) The clean split of RH-positivity into the
  unconditional, D-H-separating *passive* piece and the circular *lossless* piece.
  (2) The impedance reading sources the D-H separation from the prime side, where
  e2db's archimedean reading was blind (though as a discriminator this equals the
  known finding #37, now in network language). (3) The coupling
  passive+reciprocal$\Rightarrow$lossless as the acoustic form of the Hodge-index
  step, verified on $\mathbb{F}_q$. (4) The precise localization: the gap is
  ingredient (iii), the Lorentzian energy form, not (i) or (ii). (5) Marginal
  positivity $=$ reciprocity saturating passivity. (6) #80 $=$ the limit-point /
  indeterminate-moment boundary.

This is a clarifying reframe and a sharpened target, not a new theorem. It points
the next work at the same object the whole program converges on (the M4 Euler-pole
$H^2$ cup polarization), now wearing a name that says what it must DO: make the
medium contractive. See [all_roads_to_the_signature.md](all_roads_to_the_signature.md)
and [new_mathematics.md](new_mathematics.md) §9.4 (the 2K dictionary).
