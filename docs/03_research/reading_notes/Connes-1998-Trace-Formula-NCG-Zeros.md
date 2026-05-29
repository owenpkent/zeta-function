# Reading notes: Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function* (arXiv:math/9811068, 1998)

> Entry in the reference-library read-through
> ([`references/README.md`](../../../references/README.md)). The foundational NCG-attack
> paper: Connes gives a spectral interpretation of the critical zeros as an **absorption
> spectrum**, recasts the Riemann-Weil explicit formula as a **trace formula** on the
> adele class space `X = A/k*`, and proves the global trace formula holds **if and only
> if RH holds for all L-functions with Grossencharakter**. Source of the "absorption
> spectrum" picture and of the K1 wall the project's R3.5/3M analyses diagnosed. Mapped
> to the four-level framing, the D-H discipline (3M), the orbit/von Mangoldt picture
> (2R), and the product-surface front (2K, via Connes-Consani 2015 which realizes this
> space algebro-geometrically). Direction 4.6 = the trace formula (Connes has it at every
> finite place); Direction 8 = the SIGNATURE (the global positivity, equivalent to RH).
> Pages refer to the PDF in `references/04_ncg_connes/`. Read deeply: pp.1-18 (intro, §I
> quantum chaos / Riemann flow, §II Weil dictionary + absorption spectrum, §III adele
> class space + Theorem 1, §IV distribution trace formula for flows), pp.19-37 (§V the
> local field case + Theorem 3, §VI formal global trace computation, §VII S-local trace
> formula + Theorem 4), and pp.38-52 (§VIII the global case + Theorem 5 the RH-equivalence,
> general remarks, Appendix I).

## One-line takeaway

Connes realizes the critical zeros of zeta and L-functions as an **absorption spectrum**
(missing lines / cohomological / "negative" Hilbert space `(-)H`, not an emission point
spectrum), on a Sobolev-weighted `L^2` of the adele class space `X = A/k*` under the
idele class group `C_k = GL_1(A)/k*`. The Riemann-Weil explicit formula becomes a
**trace formula** (a Lefschetz formula in the spirit of Atiyah-Bott, not a semiclassical
Selberg formula), and the global trace formula is shown **equivalent to RH for all
Grossencharakter L-functions** via positivity of the Weil distribution. The whole
construction mimics the Weil function-field proof: zeros <-> Frobenius eigenvalues on
`H^1_et`, functional equation <-> Riemann-Roch / Poincare duality, explicit formula <->
Lefschetz, RH <-> Castelnuovo positivity. The improvement over the earlier [Co] is the
**elimination of the Sobolev parameter `delta`** by a cutoff `R_Lambda = P-hat_Lambda
P_Lambda`.

## Technical content (section by section)

**Intro (pp.2-5).** The spectral side is "entirely canonical" (no zeta input, no
analytic continuation needed). Critical zeros appear per se; non-critical zeros appear as
**resonances** entering via their harmonic potential `d mu_rho` with respect to the
critical line. The two preliminary results: Theorem 1 (§III), a spectral realization of
the critical zeros that needs an "unnatural parameter `delta`" (a Sobolev exponent
turning the absorption spectrum into a point spectrum); and §VI, a formal computation of
the character giving the Weil distribution. The two problems (rigorous meaning + remove
`delta`) are solved by Theorem 3 (local, §V), Theorem 4 (S-local, §VII), and Theorem 5
(global equivalence, §VIII). The Polya-Hilbert idea is recalled: find `(H, D)` with `D`
giving the zeros, where naturality forbids defining `H` as `l^2` of the zeros.

**§I Quantum chaos and the hypothetical Riemann flow (pp.5-7).** Semiclassical
(Gutzwiller) oscillatory counting `N_osc(E) ~ (1/pi) sum_{gamma_p} sum_m (1/m)
(1/(2 sh(m lambda_p/2))) sin(S_pm(E))` (eq. 6) compared with the Euler-product form
`N_osc(E) ~ -(1/pi) sum_p sum_m (1/m) p^{-m/2} sin(mE log p)` (eq. 7). This forces:
**(A)** primitive periodic orbits labelled by primes `p`, periods `log p`, instability
exponents `+/- log p`; **(B)** the Riemann flow has **no time-reversal symmetry** (which
excludes geodesic flows). Two "fundamental difficulties" persist: the overall **minus
sign** in (7), and that `2 sh(m lambda_p/2) ~ p^{m/2}` only asymptotically in `m`. These
are resolved only by passing to the function-field / cohomological picture.

**§II Algebraic geometry and global fields of non-zero characteristic (pp.7-9).** The
function-field dictionary (eq. 1):

| Spectral interpretation of zeros | Eigenvalues of Frobenius on `H^1_et` |
| Functional equation | Riemann-Roch (Poincare duality) |
| Explicit formulas | Lefschetz formula for Frobenius |
| Riemann hypothesis | **Castelnuovo positivity** |

The minus sign of §I is resolved: zeros live in `H^1_et(Sigma-bar, Q_l)`, which appears
with an overall minus in Lefschetz `sum (-1)^j Tr(phi*|H^j) = sum_{phi(x)=x} 1` (eq. 3).
**(C)**: the Polya-Hilbert space should appear from its negative `(-)H`, i.e. the zero
spectrum is an **absorption** (cohomological) spectrum. **(D)**: the natural group
replacing `R` is the idele class group `C_k = GL_1(A)/k*`.

**§III Spectral interpretation of critical zeros (pp.9-14).** The space `X = A/k*`
(adeles mod multiplicative `k*`), with von Neumann algebra `R_{01} = L^infinity(A) >| k*`
the **hyperfinite factor of type II_infinity**; `C_k` acts by `(j,a) -> ja`. The Hilbert
space `L^2_delta(X)_0` is the completion of the codimension-2 subspace `S(A)_0 = {f in
S(A) : f(0) = 0, int f dx = 0}` (eq. 6) under the Sobolev-weighted norm
`||f||_delta^2 = int |sum_{q in k*} f(qx)|^2 (1 + log^2|x|)^{delta/2} |x| d*x` (eq. 7),
`delta > 1`. The two conditions produce the trivial module `C` plus the **Tate twist
`C(1)`** (the 2-dim supplement `C (+) C(1)`, eqns 10-11). The representation `U(j)f(x) =
f(j^{-1}x)` (eq. 9) is intertwined by the isometry `E(f)(g) = |g|^{1/2} sum_{q in k*}
f(qg)` into the left regular representation `V` of `C_k` on `L^2_delta(C_k)`, with
`E U(a) = |a|^{1/2} V(a) E` (eq. 19). The Polya-Hilbert space is the **cokernel** `H =
L^2_delta(C_k)/Im(E)` (so it appears as a quotient, consistent with (C)). Decompose by
characters `chi` of `K = ker|.|`: `H = (+)_chi H_chi`. For `char(k) = 0`, the action of
`R*_+` on `H_chi` is generated by an operator `D_chi` with purely imaginary spectrum
(`D_chi xi = lim (1/eps)(W_chi(e^eps) - 1) xi`, eq. 26). **Theorem 1**: `Sp D_chi subset
iR` is the set of imaginary parts of zeros of `L(chi-tilde, .)` on the critical line:
`rho in Sp D <=> L(chi-tilde, 1/2 + rho) = 0`; the multiplicity in `Sp D` is the largest
integer `n < (1+delta)/2`, `n <=` (mult of zero). **Corollary 2**: `W(h) = int W(g) h(g)
d*g` is trace class with `Trace W(h) = sum_{L(chi-tilde, 1/2+rho)=0} h-hat(chi-tilde,
rho)`. Note (p.14-15): this realizes only the `Re = 1/2` zeros, and the `delta`-dependence
is the artefact. The formal character (eq. 34): `"Trace" U(h) = h-hat(0) + h-hat(1) -
sum_{L(chi,rho)=0, Re rho = 1/2} h-hat(chi, rho) + infinity h(1)`, sitting in the exact
sequence `0 -> L^2(X)_0 -> L^2(C_k) -> H -> 0` (eq. 33). The minus sign and the cokernel
realize the absorption picture.

**§IV The distribution trace formula for flows on manifolds (pp.16-18).** Atiyah-Bott /
Guillemin-Sternberg background. For `phi` transverse to the diagonal, `"Trace"(U) =
sum_{phi(x)=x} 1/|1 - phi'(x)|` (eq. 7); the alternating sum gives the Lefschetz formula.
For a flow `F_t = exp(tv)`, with `h(0) = 0` to avoid the non-transverse identity:
`"Trace"(int h(t) U_t dt) = sum_gamma int_{I_gamma} h(u)/|1 - (F_u)*| d*u` (eq. 17), sum
over periodic orbits `gamma` (zeros of `v` counted as orbits), `I_gamma` the isotropy
subgroup, `(F_u)*` the Poincare return map. For the scaling flow `F_t(x) = e^t x` on `R`:
`"Trace"(U(h)) = int h(u)/|1-u| d*u` (eq. 21) -- the key local kernel `1/|1-u|`.

**§V The action `(lambda, x) -> lambda x` of `K*` on a local field `K` (pp.19-24).**
Treats the lack of transversality at `h(1) != 0` rigorously. **Theorem 3**: for `K` a
local field with character `alpha`, `h in S(K*)` compactly supported, the cutoff
`R_Lambda = P-hat_Lambda P_Lambda` (infrared `|x| <= Lambda` and ultraviolet `F P_Lambda
F^{-1}`) gives `Trace(R_Lambda U(h)) = 2 h(1) log' Lambda + int' h(u^{-1})/|1-u| d*u +
o(1)` as `Lambda -> infinity`, with the **privileged principal value** `int'` determined
by the unique distribution agreeing with `du/|1-u|` off `u=1` whose Fourier transform
vanishes at 1. The proof computes the symbol `sigma(x,xi) = rho^{-1} g-hat(x xi)` and uses
`F-hat(varphi)(a) = rho^{-1} |a|^{-1}` for `varphi(u) = -log|u|` (eq. 34). Appendix II
checks this principal value is **the same as in Weil's explicit formulas**.

**§VI The global case and the formal trace computation (pp.25-28).** For `C_k` acting on
`X = A/k*`: the fixed points `phi^{-1}(Z)` project onto the union of hyperplanes `H_v =
pi(H-tilde_v)`, `H-tilde_v = {x : x_v = 0}` (eq. 5), one per place `v`. The isotropy group
of a generic point of `H_v` is `I_x = k_v*` (eq. 7); the transverse space is `N_x = k_v`;
the contribution is `int_{k_v*} h(lambda)/|1-lambda| d*lambda` (eq. 13). Summing:
`"Trace"(U(h)) = sum_v int_{k_v*} h(u^{-1})/|1-u| d*u` (eq. 15), which (restricted to
`h(1)=0`) is **exactly the Weil distribution** `h-hat(0) + h-hat(1) - sum_{L(chi,rho)=0}
h-hat(chi,rho) + infinity h(1)` (eq. 16), now with the restriction `Re rho = 1/2`
removed. **Crucial positivity remark (p.28):** if `h >= 0` (and `h(1) = 0`), the RHS is
positive; this is the positivity of **permutation matrices**, not of quantization. The
expected formula is a Lefschetz formula in the spirit of [AB], not a semiclassical
formula.

**§VII Proof of the trace formula in the S-local case (pp.28-37).** For a finite set `S`
of places (with all infinite places), `X_S = prod_{v in S} k_v / O_S*` (S-units),
`C_S = J_S^1/O_S*`. As soon as `|S| >= 3` this is **non-type-I** in the sense of NCG (the
example `k = Q`, `S = {2,3,infinity}` has `O_S* = {+/- 2^n 3^m}` acting ergodically on
`{0} x R`). Lemma 1 shows the Fourier transform extends to a unitary on `L^2(X_S)`.
**Theorem 4** (the S-local trace formula, proved unconditionally): `Trace(R_Lambda U(h))
= 2 h(1) log' Lambda + sum_{v in S} int'_{k_v*} h(u^{-1})/|1-u| d*u + o(1)`. The proof
(Lemma 2, the error-term estimate `|delta_q(Lambda)| <= delta_Lambda exp(-d(q,1))` via a
word metric on `O_S*`) is the technical heart. This shows **the handling of periodic
orbits and their contribution to the trace is correct, including the non-type-I case**.

**§VIII The trace formula in the global case and elimination of `delta` (pp.37-44). THE RH-EQUIVALENCE.**
The cutoff is performed directly on `L^2(X)` so only `delta = 0` is used; all zeros play
a role (critical per se, non-critical as resonances via harmonic potential). Lemma 1
analyzes the relative position of the projections `P_Lambda, P-hat_Lambda`; in positive
characteristic this is exact, while at the **archimedean place** it relies on
Landau-Pollak-Slepian / prolate spheroidal wave functions (the operator `H_Lambda` of eq.
32 commuting with both projections; the angle operator `Theta`, `sin Theta = |P_1 - P_2|`,
eq. 30). **Theorem 5** (the main result): for `k` a global field of positive
characteristic, the following are equivalent:
(a) the trace formula `Trace(Q_Lambda U(h)) = 2 h(1) log' Lambda + sum_v int'_{k_v*}
h(u^{-1})/|1-u| d*u + o(1)` holds as `Lambda -> infinity`;
(b) all L-functions with Grossencharakter on `k` satisfy RH.
The proof (a)=>(b): the Weil distribution `Delta = log|d^{-1}| delta_1 + D - sum_v D_v`
(eq. 17) is of **positive type** (`Delta_Lambda(f * f*) >= 0`, eq. 24-25), via
`Q'_{Lambda,0} <= S_Lambda` and Weil's criterion (positivity of Weil distribution <=>
RH). The proof (b)=>(a): Lemma 3 computes `lim Delta_Lambda` from the zeros independently
of any hypothesis, with the harmonic measure `d mu_rho` of `rho` w.r.t. the line `iR`
(critical zeros give Dirac masses on the line, non-critical give a spread Poisson kernel
-- the **resonance** picture). The general remarks (pp.49-50): comparison with [Bg]
(Goldfeld, where positivity of the Weil-distribution inner product = RH but no clue how
to prove it), with [Z] (Zagier), with Deninger's hypothetical arithmetic site [D]
(noting that dividing `A` by `k*` "eliminates the linear structure" and replaces products
by sums in dimension formulas), and the extension to `GL(n)` (Soule). Section VIII closes
with deriving `N(E) ~ (E/2pi)(log(E/2pi) - 1) + 7/8 + ...` from a phase-space area
computation `(2E/2pi) log Lambda - (E/2pi)(log(E/2pi) - 1)` (eq. 43), where `<N(E)>`
appears with the all-important **minus sign** (eq. 43) confirming the absorption picture.

**Appendices.** I: proof of Theorem 1 (Tate-Iwasawa as interpreted by Weil [W2],
homogeneous distributions on `A`, L-functions as normalization factors). II: the explicit
formulas (the privileged principal value matches Weil). III: distribution trace formulas
(coordinate independence, after Guillemin-Sternberg).

## Points mapped to the project

1. **The function-field dictionary IS the project's milestone list (§II, eq. 1).** The
   four rows are: zeros <-> Frobenius on `H^1_et`; functional equation <-> Riemann-Roch
   / Poincare duality; explicit formulas <-> Lefschetz; RH <-> Castelnuovo positivity.
   The Lefschetz row is Direction 4.6; the Castelnuovo-positivity row is Direction 8 (the
   Hodge-index SIGNATURE). Connes and the project aim at the same two milestones from
   opposite sides (his analytic/adelic side, the project's arithmetic-surface side). The
   canonical statement of what Directions 4.6 and 8 should mean ->

2. **The absorption spectrum / "negative" Hilbert space `(-)H` (§II (C), §III cokernel).**
   The overall minus in Lefschetz forces the Polya-Hilbert space from its negative; the
   construction realizes `H` as a **cokernel** `L^2(C_k)/Im(E)` (eq. 33). So zeros are an
   absorption (cohomological, `H^1`) spectrum. This is the same minus the project keeps
   meeting: Deninger-I's superdimension / eta-invariant, Leichtnam's `alpha(-kl)` vs
   `alpha(kl)` dissymmetry, 2R's `-zeta'/zeta`. The §VIII phase-space `<N(E)>`-with-minus
   (eq. 43) is the cleanest statement. The minus-sign / odd-cohomology nature is a
   structural constant; any Direction-8 signature must reproduce it (consistent with 2Q
   forcing infinite-dim `H^i` and the spectrum living in `H^1`) ->

3. **The adele class space `X = A/k*`, type II_infinity (§III, eq. 3).** `R_{01} =
   L^infinity(A) >| k*` is the hyperfinite II_infinity factor. This is the Connes adelic
   space the Morishita bridge (2K) links to Deninger's foliated dynamical systems, and
   the space Connes-Consani 2015 realizes algebro-geometrically (Thm 1.1/3.8 there give
   `Z-hat^x \ A_Q/Q*`). Note the type contrast: II_infinity here for the `L^2`-attack vs
   Leichtnam's III_{1/q} for the dynamical flow side. 2K's "the bridge builds NO pairing"
   sits exactly here: Connes gives the space and the trace, the positivity is missing ->

4. **Theorem 1: conditional spectral realization, the `delta`-caveat = the K1 wall (§III).**
   `D_chi` realizes only the `Re = 1/2` zeros as a spectrum (with a `delta`-dependent
   multiplicity). It does NOT force all zeros onto the line. That step is the trace-
   formula positivity, which §VIII shows is **equivalent** to RH, not a proof of it. The
   realization is non-circular as a spectral construction but circular as a positivity
   proof: exactly the R3.5/3M diagnosis. (Note `delta` is eliminated by §VIII's cutoff,
   so the live obstruction is purely the global positivity, not `delta`.) ->

5. **The equivalence trace formula <=> RH (Theorem 5, §VIII).** §VII proves the trace
   formula unconditionally at every finite set of places `S` (including non-type-I,
   `|S| >= 3`); §VIII shows the GLOBAL trace formula is equivalent to RH for all
   Grossencharakter L-functions. The spectral side is entirely canonical (no zeta input);
   the obstruction is the global positivity of the Weil distribution `Delta` (eq. 17,
   24-25). The project's 3M lands here precisely: NCG-trace positivity is the whole game,
   and asserting it is asserting RH. This is the quantitative form of the marginal-
   positivity "no buffer" finding on the Arch-3 side -> cite §VIII / Theorem 5 ->

6. **Orbits = primes, lengths `log p`, no time-reversal (§I (A),(B); §VI finite places).**
   The Euler product forces orbit lengths `{log p}`, instability `+/- log p`, no
   time-reversal (one-sided semigroup `R*_+`, not `R`). The trace kernel `1/|1-u|` (§IV
   eq. 21, §VI eq. 13) integrates the test function against the prime/orbit data; this is
   2R on the dynamical side and Leichtnam's analytic statement. D-H, lacking an Euler
   product, has no `{log p}` orbit spectrum: the 3M wrong-approach detector fires here too.
   So Connes' geometric side does distinguish zeta from D-H ->

7. **The product-surface / `F_1` front (2K), §VIII general remarks + Connes-Consani 2015.**
   Connes explicitly relates `X = A/k*` to Deninger's hypothetical arithmetic site [D]
   and notes dividing `A` by `k*` "replaces products by sums" in dimension formulas (the
   characteristic-1 phenomenon Connes-Consani later make precise). The Connes-Consani 2015
   square `N^x2-hat` is the algebro-geometric product surface over the characteristic-1
   base whose points are the square of this space's points. So this paper is the analytic
   pole and Connes-Consani 2015 the geometric pole of the same object; the signature gap
   is shared ->

## What this changes for the program

- **The NCG attack is the analytic dual of the project's arithmetic-surface attack.** Same
  Weil dictionary, same two open milestones (Lefschetz, Castelnuovo positivity). Connes
  supplies the space (`A/k*`), the group action (`C_k`), and the trace; Direction 8
  supplies the would-be intersection form. They meet at the positivity / signature line,
  unproven on both sides.
- **The K1 wall is precisely located: global trace-formula positivity (Theorem 5, §VIII).**
  Theorem 1 realizes critical zeros (with `delta`, now eliminated); §VII proves the trace
  formula at every finite place unconditionally; §VIII shows closing the global case is
  equivalent to RH. R3.5/3M "NCG-trace positivity is circular" is the exact reading. Cite
  Theorem 5 for the equivalence.
- **The minus sign / absorption spectrum is a hard structural constant.** It recurs as
  Deninger's eta-invariant, Leichtnam's orbit dissymmetry, 2R's `-zeta'/zeta`, and the
  §VIII phase-space minus. Any Direction-8 signature must reproduce this sign (odd
  cohomology, `H^1`), consistent with 2Q forcing infinite-dimensional cohomology.
- **D-H discipline holds at the trace level.** The orbit spectrum `{log p}` exists only
  because of the Euler product (the `1/|1-u|` kernel at finite places picks up the von
  Mangoldt data). D-H has none (3M). The NCG framework is not a wrong-approach by the 3M
  test; its missing step (positivity) is the real one.

## Actionable

- The cleanest project-facing statement is Theorem 5 (§VIII): global trace formula <=> RH.
  Use it to frame why Direction 8 (the signature/positivity) and not Direction 4.6 (the
  trace formula, which Connes has at every finite place by Theorem 4) is the genuine
  RH-closing step.
- The `C (+) C(1)` (trivial + Tate twist) supplement in `L^2_delta(X)_0` (eqns 6, 10, 11,
  31-33) is the adelic shadow of the two trivial cohomologies `H^0`, `H^2` flanking the
  zero-bearing `H^1`. Carry it into any Lefschetz / `H^*` bookkeeping for Direction 4.6.
- The positivity of the RHS for `h >= 0` (§VI p.28) is the positivity of permutation
  matrices, not quantization. This is the precise sense in which the missing positivity is
  combinatorial/cohomological; pair it with the Connes-Consani idempotent-operations gap
  (no signed pairing on the square) as two faces of the same Castelnuovo-positivity hole.

## Status

Read deeply: pp.1-18 (intro; §I quantum chaos / Riemann flow eqns 1-7; §II Weil dictionary
eq. 1, absorption spectrum (C); §III adele class space, isometry `E`, cokernel `H`,
Theorem 1 + Corollary 2, exact sequences eqns 31-34; §IV distribution trace formula for
flows, the `1/|1-u|` kernel eq. 21), pp.19-37 (§V local field + Theorem 3 + the privileged
principal value; §VI formal global trace eq. 15-16 + the `h >= 0` positivity remark; §VII
S-local + Theorem 4 + Lemma 2 error estimate, the non-type-I `|S| >= 3` case), pp.38-52
(§VIII the cutoff on `L^2(X)`, Lemma 1 + prolate spheroidal functions at the archimedean
place, **Theorem 5 the RH-equivalence**, Lemma 3 / harmonic measure / resonances, general
remarks, Appendix I setup). Honest depth: the spectral realization (Thm 1), the trace
formula at finite places (Thm 4), and the RH-equivalence framing (Thm 5, eqns 17/24/25)
are understood at the statement level with the proof architecture traced; the finest
S-local error estimates (§VII Lemma 2) and the LPS / prolate-spheroidal analysis (§VIII
Lemma 1) are summarized, not verified line by line.
