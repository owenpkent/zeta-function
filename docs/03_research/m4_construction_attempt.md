# The M4 construction attempt: a direct 3-front attack on RH (2026-06-26, #128)

> Reconstructed dossier. The original working reports lived in a non-tracked
> `scratchpad/m4_attempt/0{1,2,3}_*.md` and were not committed; this document
> recovers their content from the LEARNINGS #128 record and the one tracked
> artifact, [`../../experiments/positivity/e3s_li_hankel_dissolves.py`](../../experiments/positivity/e3s_li_hankel_dissolves.py)
> (the verified Front-2 no-go). It is the canonical, tracked home for the attempt.

## What this was

The program's first genuine, full-effort attempt at RH for $\zeta$ itself, rather
than cataloging what frameworks lack. Three independent BUILDER fronts, built to
disagree, attacked the M4 positivity head-on:

1. **Weil-form analytic domination**: prove the Bombieri-Weil explicit-formula
   quadratic form $\ge 0$ using the Euler product.
2. **Moment-matrix Gram factorization**: lift the e2xx trigonometric-moment object
   ([#123](../../experiments/arithmetic_geometric/e2xx_higher_rank_rosati.md)) to
   $\zeta$ and exhibit it as a manifest Gram matrix.
3. **Hilbert-Polya / circle-Frobenius operator**: build a self-adjoint operator
   whose spectrum is the imaginary parts of the zeros.

**All three wall. None produces a candidate proof. All three land on the same gap.**
That is the result: a 3-front convergence is the strongest evidence yet that the gap
is a single object. The D-H firewall held on all three fronts. M4 is untouched, and
now characterized from the construction side as well as the survey side
([`all_roads_to_the_signature.md`](all_roads_to_the_signature.md)).

## The universal gap

The Euler product converges only on $\mathrm{Re}(s)>1$, where it is a **trace**. The
zeros live in $\mathrm{Re}(s)<1$, accumulating on the critical line $\mathrm{Re}(s)=\tfrac12$,
where the **signature** (the polarization, the signed pairing, the $\eta>0$ metric)
lives. Continuing the Euler-side positivity across the line is the missing Weil
cohomology over $\mathrm{Spec}(\mathbb{Z})$ = M4 (#42/#25). Every front re-derives this
identical wall in its own language.

## Front 1: Weil-form analytic domination

The genuinely Euler-specific lever is the per-prime **Poisson/Herglotz completion**.
Each local factor's contribution to the explicit-formula form is

$$\kappa_p(r) = \sum_{k\ge1} p^{-k/2}\cos(k\, r \log p) = -\tfrac12 + \tfrac12\,\frac{1-1/p}{\lvert 1-p^{-1/2+ir}\rvert^2},$$

a **positive Poisson kernel** (verified to $2.2\times10^{-15}$). This gives the
unconditional bound "each prime's contribution to $W_p \ge -(\log p)\,g(0)$", using the
prime-power factorization that Davenport-Heilbronn lacks (#20). It walls three ways:

- **(W1) Wrong sign.** It bounds the prime term from **below**. Weil positivity needs
  the prime term bounded from **above** by the archimedean cushion.
- **(W2) Divergent / lossy.** Summed per-prime independently it is off by
  $\sim g(0)e^{2A}$ (Chebyshev $\theta$) versus the archimedean $\sim g(0)\log$, because
  it discards the cross-prime cancellation that a single spectral weight
  $\hat\phi^2$ enforces. That lost cancellation **is** RH.
- **(W3) Lives at $\mathrm{Re}(s)>1$.** The regularized prime kernel is
  $\mathrm{Re}[-\zeta'/\zeta(1/2+ir)]$, whose singular support is exactly the zeros.
  Every unconditional Euler handle lives on $\mathrm{Re}(s)>1$ and cannot be continued
  to $\mathrm{Re}(s)=1/2$ without already knowing the zeros (#42).

**Load-bearing correction (fixes a standing framing).** The natural decomposition
"$A_{\mathrm{inf}}\ge0$, just bound the prime sum $P$" is **false**:
$A_{\mathrm{arch}}+B_{\mathrm{pole}}$ is **not** PSD (min eigenvalue $-1.75$ for $\zeta$).
The archimedean term is calibrated to be **cancelled** by the primes; $\zeta$'s
positivity is the residue of a **three-way near-cancellation**, not "archimedean
dominates prime." This is the analytic root of the marginal-positivity wall
(#18/#19): no buffer is created.

*Honest partial.* On the small-support cone
$\mathrm{supp}\,\phi \subset (-\tfrac{\log 2}{2}, \tfrac{\log 2}{2})$ the prime sum
vanishes and $W\ge0$ rigorously, but that is the prime-free base case (positive for
D-H too): zero RH content.

## Front 2: moment-matrix Gram factorization

The moment-matrix lift of e2xx ([#123](../../experiments/arithmetic_geometric/e2xx_higher_rank_rosati.md))
to $\zeta$ **dissolves**. Mapped to the circle by $w = 1 - 1/\rho$, the zero spectrum
accumulates at the archimedean point $w=1$, so the Toeplitz moment
$C_n = \sum_\rho w_\rho^n$ **diverges**: there is no single circle / $q$ (the $(1,p)$
bidegree, #25). The Gram $M = V^\top V$ indexed by zeros is PSD iff RH (circular);
factored from primes $M = A_{\mathrm{arch}} + P_{\mathrm{fin}} + B_{\mathrm{pole}}$,
the von Mangoldt subtraction $P_{\mathrm{fin}}$ is the obstruction.

**Verified structural no-go**
([`e3s_li_hankel_dissolves.py`](../../experiments/positivity/e3s_li_hankel_dissolves.py)):
the Li-coefficient Hankel $[\lambda_{i+j}]$ is **not PSD even for $\zeta$** (min eig
$-0.014, -0.055, \dots$ at sizes $2, 3, \dots$), because $\zeta$'s Li sequence is
strictly **log-concave** ($\lambda_n \sim \tfrac{n}{2}\log n$, Bombieri-Lagarias;
verified 14/14 log-concave, 0/14 log-convex), while a Hamburger moment sequence must
be **log-convex**. So $\{\lambda_n\}$ is categorically **not** a moment sequence, and
the moment-matrix framing of M4 is genus-faithful (a finite Frobenius spectrum over
$\mathbb{F}_q$), dissolving over $\mathbb{Z}$'s infinite accumulating spectrum. Only the
**termwise** $\lambda_n\ge0$ (the Weil form, Level 4) survives.

This is the #122 genus-1-faithfulness caveat one level up, and it sharpens #27 from
"non-Euler detector" to "log-concave, not a moment sequence." RH is unaffected: RH is
termwise positivity, not Hankel PSD.

## Front 3: Hilbert-Polya / circle-Frobenius operator

The only build that passes the #4 filter (genuinely injects the Euler product) is the
Connes idele-class scaling operator $D$. It is self-adjoint with **absolutely
continuous** spectrum (the whole real line), and the zeros are **resonances** (poles of
$\xi(2s-1)/\xi(2s)$ in the Eisenstein continuous spectrum), **not eigenvalues**.
Self-adjointness fixes $\gamma\in\mathbb{R}$ (automatic) and is **silent** on
$\mathrm{Re}(\rho)$, the one coordinate RH is about. This is sharper than "no operator
exists": a good self-adjoint operator exists; the zeros just are not its eigenvalues.
Forcing discreteness via a cutoff **is** global Weil positivity = RH (K1-circular).

For $\zeta$ the local factor is weight $0$ ($\alpha_p=1$), so the $\sqrt p$ circle is
the curve / elliptic (Hasse) object, **not** $\zeta$'s. This sharpens e2ad's per-prime
framing: the $a_p$ / Hasse structure belongs to $L(E,s)$ (the weight-1 motive), not
$\zeta$ (the weight-0 trivial motive).

**Compression (the residue).** RH $\iff$ PT-symmetry unbroken $\iff$ a positive metric
$\eta>0$ with $\eta H \eta^{-1} = H^*$ exists. The archimedean place gives the PT / FE
involution for free, and D-H **shares** it (which is why the firewall correctly does
**not** separate $\zeta$ from D-H at the symmetry level: D-H's off-line zeros are a
PT-conjugate pair). The discriminator is $\eta>0$ = the missing Euler-side
polarization = M4. So the spectral route re-derives the **identical** gap as the
geometric route (all-roads #30), compressed into one operator-theoretic predicate
(Bender-Brody-Muller is the canonical K1 instance).

## The synthesis

Three independent attacks on RH, three honest walls, **one gap**: the Euler product
($\mathrm{Re}(s)>1$, a trace) cannot be continued to the critical line
($\mathrm{Re}(s)=\tfrac12$, where the signature / the polarization / $\eta>0$ / the
signed pairing lives) without the missing Weil cohomology. The attempt was genuine
and full-effort; it did not close (as expected for RH). Its value is the 3-front
convergence (the gap is one object) plus three verified residues:

1. the per-prime Poisson completion and the three-way-cancellation correction
   ($A_{\mathrm{arch}}+B_{\mathrm{pole}}$ not PSD, min eig $-1.75$);
2. the Li-Hankel non-PSD no-go (log-concave, not a moment sequence);
3. the PT / $\eta>0$ operator compression.

## Forward Lean targets

Handed to [`../../lean/ZetaRH/R3_5.lean`](../../lean/ZetaRH/R3_5.lean): a
discrete-vs-continuous-spectrum predicate (Front 3), a $P(T)$ / $\eta>0$ predicate, and
the Li-Hankel no-go (Front 2). Proposed **VT-NP1**: finite Euler-product zero-freeness
on $\mathrm{Re}(s)>0$ plus the M4-reduction, extending
`HodgeIndex.negDef_iff_hasseWeil`.

## Cross-references

- LEARNINGS #128 (the full record this dossier reconstructs).
- Survey-side convergences and the construction-side summary:
  [`all_roads_to_the_signature.md`](all_roads_to_the_signature.md).
- Front 2 object lifted: [#123 / e2xx](../../experiments/arithmetic_geometric/e2xx_higher_rank_rosati.md);
  Front 3 chases the $H^1$ / odd-Frobenius of #124/#126; Front 3 sharpens the
  per-prime framing of #127 / e2ad.
- Marginal positivity (= Front 1's three-way cancellation): #18/#19,
  [`08A_rosati_standard_conjecture.md`](research_directions/08A_rosati_standard_conjecture.md).
- The universal local-to-global wall: #42/#25; trace-vs-signature: #30.
