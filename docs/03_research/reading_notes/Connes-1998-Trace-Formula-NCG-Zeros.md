# Reading notes: Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function* (arXiv:math/9811068, 1998)

> Entry in the reference-library read-through
> ([`references/README.md`](../../../references/README.md)). This is the foundational
> NCG-attack paper: Connes reduces RH (for all L-functions with Grossencharakter) to
> the validity of a single trace formula on the noncommutative space of adele
> classes `X = A/k*`, with the idele class group `C_k` acting. It is the source of the
> "absorption spectrum" picture and of the K1 wall the project's R3.5/3M analyses
> diagnosed. Mapped to the four-level framing, to the D-H discipline (3M), and to the
> product-surface front (2K). Pages refer to the PDF in `references/04_ncg_connes/`.
> Read: pp.1-13 (intro, §I quantum chaos, §II function-field dictionary, §III the
> spectral interpretation + Theorem 1). The S-local trace formula proof (§§V-VII) and
> the elimination of delta (§VIII) skimmed via the intro.

## One-line takeaway

Connes gives a spectral interpretation of the critical zeros of zeta and L-functions
as an **absorption spectrum** (missing lines, a cohomological / `negative` Hilbert
space, not an emission point spectrum), realized on `L^2` of the adele class space
`X = A/k*` under the idele class group `C_k = GL_1(A)/k*`. He recasts the Riemann-Weil
explicit formula as a **trace formula** on `X`, and proves that the global trace
formula holds **if and only if RH holds for all L-functions with Grossencharakter**.
The whole construction is built to mimic the Weil function-field proof: zeros <->
Frobenius eigenvalues, functional equation <-> Riemann-Roch / Poincare duality,
explicit formula <-> Lefschetz, RH <-> Castelnuovo positivity.

## The points that matter, mapped to the project

1. **The function-field dictionary IS the project's milestone list (§II, p.8).**
   Connes writes the four-line dictionary explicitly: spectral interpretation of zeros
   <-> eigenvalues of Frobenius on `H^1_et`; functional equation <-> Riemann-Roch
   (Poincare duality); explicit formulas <-> Lefschetz formula for Frobenius; RH <->
   **Castelnuovo positivity**. The Lefschetz line is the project's Direction 4.6; the
   Castelnuovo-positivity line is the project's Direction 8 (the Hodge-index
   SIGNATURE). Connes and the project are aiming at the same two milestones from
   opposite sides (his analytic/adelic side, the project's arithmetic-surface side).
   -> Direction 4.6 and Direction 8 are exactly the two bottom rows of Connes' Weil
   dictionary; this paper is the canonical statement of what those rows should mean.

2. **The absorption spectrum / "negative" Hilbert space `(-)H` (§II (C), p.8).** The
   overall minus sign in the Lefschetz formula `Sum (-1)^j Tr(phi*|H^j) = Sum_{phi(x)=x} 1`
   forces the Polya-Hilbert space to appear from its negative `(-)H`. So the zeros are
   an absorption (cohomological) spectrum, not an emission spectrum. This is the same
   minus sign the project keeps meeting: Deninger I's superdimension / eta-invariant,
   Leichtnam's `alpha(-kl)` vs `alpha(kl)` dissymmetry.
   -> The "cohomological / minus-sign" nature of the zero spectrum is a structural
   constant across the whole arithmetic-geometric front. 2R's `-zeta'/zeta` (the
   minus on the log-derivative) is the same sign, and it is why the spectrum must live
   in `H^1` (odd cohomology), consistent with 2Q forcing infinite-dim `H^i`.

3. **The space is the adele class space `X = A/k*`, von Neumann algebra type II_infinity (§III, p.9).**
   `X = A/k*` (adeles mod multiplicative `k*`), with `R_{01} = L^infinity(A) >| k*` the
   hyperfinite II_infinity factor; `C_k` acts by `(j,a) -> ja`. The Hilbert space
   `L^2_delta(X)_0` is built on the codimension-2 subspace `{f : f(0)=0, integral f = 0}`
   (the two conditions produce the trivial module `C` plus the Tate twist `C(1)`).
   -> This is the **Connes adelic space** that the Morishita bridge (2K) links to
   Deninger's foliated dynamical systems. Note the type: II_infinity here for the
   `L^2`-attack, vs Leichtnam's III_{1/q} for the dynamical-flow side. The project's
   2K finding "the Morishita bridge builds NO pairing" sits exactly here: Connes gives
   the space and the trace, but the positivity (Castelnuovo line) is what is missing.

4. **Theorem 1 (p.13): conditional spectral realization, the delta-parameter caveat.**
   For `chi` a character of `K = ker|.|`, the operator `D_chi` (generator of the scaling
   action of `R*_+` on the sector `H_chi`) has discrete spectrum `Sp D_chi subset iR`
   equal to the imaginary parts of the zeros of `L(chi-tilde, .)` on the critical line:
   `rho in Sp D <=> L(chi-tilde, 1/2 + rho) = 0`. The catch is the Sobolev-type
   parameter `delta > 1` (the weight `(1 + log^2|x|)^{delta/2}`) needed to turn the
   absorption spectrum into a point spectrum; multiplicities depend on `delta`.
   -> This is the explicit form of the **K1 wall**. The theorem realizes only the
   `Re = 1/2` zeros as a spectrum; it does not by itself force ALL zeros onto the line.
   That last step is the trace-formula positivity, which §VIII shows is EQUIVALENT to
   RH, not a proof of it. The construction is non-circular as a spectral realization
   but circular as a positivity proof: exactly the R3.5/3M diagnosis.

5. **The equivalence: trace formula <=> RH (intro, p.3 + §VIII).** §VII proves the
   S-local trace formula unconditionally (any finite set of places, including the
   non-type-I case `|S| >= 3`); §VIII shows the GLOBAL trace formula is left open and
   is equivalent to RH for all Grossencharakter L-functions. The spectral side is
   "entirely canonical" (no zeta input); proving its equality with the geometric
   (Weil-distribution) side via positivity of the Weil distribution would give RH.
   -> The project's 3M finding lands here precisely: NCG-trace positivity is the whole
   game, and asserting it is asserting RH. The trace formula is true at every finite
   place; the obstruction is global positivity, the same "no buffer" margin the
   marginal-positivity thesis records on the Arch-3 side.

6. **The Riemann flow must break time-reversal; orbits are primes with length log p (§I, (A),(B), p.6-8).**
   Matching the semiclassical `N_osc(E)` (Gutzwiller) against the Euler-product
   `N_osc(E) ~ -(1/pi) Sum_p Sum_m (1/m) p^{-m/2} sin(mE log p)` forces: primitive
   periodic orbits labelled by primes `p`, periods `log p`, instability exponents
   `+/- log p`, and **no time-reversal symmetry** (which excludes geodesic flows). The
   overall minus sign and the finite-`m` mismatch are the "two fundamental difficulties"
   resolved only by going to the function-field / cohomological picture.
   -> This is 2R stated on the dynamical side and Leichtnam's (1)/(3) stated
   analytically: orbit lengths `{log p}`, the von Mangoldt sum, the dynamical-zeta
   `-zeta'/zeta`. The "no time-reversal" requirement is the same one-sided-semigroup
   (`R*_+`, not `R`) structure Deninger II and Leichtnam flag. D-H, lacking an Euler
   product, has no such `{log p}` orbit spectrum (3M): the wrong-approach detector
   fires here too.

## What this changes for the program

- **The NCG attack is the analytic dual of the project's arithmetic-surface attack.**
  Same Weil dictionary, same two open milestones (Lefschetz, Castelnuovo positivity).
  Connes supplies the space (`A/k*`), the group action (`C_k`), and the trace; the
  project's Direction 8 supplies the would-be intersection form. They meet at the
  positivity / signature line, which is unproven on both sides.
- **The K1 wall is precisely located: it is the global trace-formula positivity (§VIII).**
  Theorem 1 realizes the critical zeros conditionally (with `delta`); §VIII shows
  closing it is equivalent to RH. The project's R3.5/3M "NCG-trace positivity is
  circular" is the exact reading of this paper. Cite §VIII for the equivalence.
- **The minus sign / absorption spectrum is a hard structural constant.** It recurs as
  Deninger's eta-invariant, Leichtnam's orbit dissymmetry, and 2R's `-zeta'/zeta`. Any
  Direction-8 signature must reproduce this sign (odd cohomology, `H^1`), consistent
  with 2Q forcing infinite-dimensional cohomology.
- **D-H discipline holds at the trace level.** The orbit spectrum `{log p}` exists only
  because of the Euler product. D-H has none (3M). So Connes' geometric side does
  distinguish zeta from D-H, which is reassuring: the NCG framework is not a
  wrong-approach by the 3M test, but its missing step (positivity) is the real one.

## Actionable

- The cleanest project-facing statement is the equivalence in §VIII: global trace
  formula <=> RH. Use it to frame why Direction 8 (the signature/positivity) and not
  Direction 4.6 (the trace formula, which Connes has at finite places) is the genuine
  RH-closing step.
- The `C` + `C(1)` (trivial + Tate twist) supplement in `L^2_delta(X)_0` (eq. 6, 10,
  11) is the adelic shadow of the two trivial cohomologies `H^0`, `H^2` flanking the
  zero-bearing `H^1`. Worth carrying into any Lefschetz/`H^*` bookkeeping for Direction
  4.6.

## Status

Read pp.1-13 (intro, §I quantum chaos / Riemann flow, §II function-field dictionary +
absorption spectrum, §III adele class space + Theorem 1). §§IV-VIII (distribution
trace formula, local/global proofs, elimination of delta) and the three appendices
read via the introduction's summary, not line by line. Honest depth: the spectral
realization (Thm 1) and the RH-equivalence framing (§VIII) are understood; the
detailed S-local trace computation is not verified line by line.
