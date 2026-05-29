# Reading notes: Deninger, *Motivic L-functions and regularized determinants* (I)

> Foundational paper of Deninger's program (Proc. Symp. Pure Math. 55-1, 1994,
> 707-743). Entry in the reference-library read-through
> ([`references/README.md`](../../../references/README.md)). This paper makes the
> regularized-determinant formalism rigorous, constructs the local (per-prime)
> infinite-dimensional cohomologies via the Riemann-Hilbert correspondence, derives
> both the non-archimedean Euler factor `(1 - q^{-s}F)^{-1}` and the archimedean
> Gamma-factor as regularized characteristic series of one and the same operator,
> and (the most novel takeaway for us) identifies the SIGN in the functional equation
> with a regularized superdimension = the Atiyah-Patodi-Singer eta-invariant. It is
> the machinery under 2R (the determinant), under the Lean `ExplicitFormula`
> archimedean kernel (the Gamma-factor), and under Direction 4.6 (the regularized
> determinant target). Pages refer to the PDF in `references/02_deninger_program/`.

## One-line takeaway

Deninger I gives the rigorous definition of `det_inf(Theta|V)` (a zeta-regularized
determinant on a countable-dimensional space), constructs the local cohomology
`H(D)` via the Riemann-Hilbert correspondence on `G_m` (the additive eigenvalues of
the generator `Theta` are the logarithms of the multiplicative eigenvalues of the
local Frobenius `F`, `Sp(Theta) = e^{-1}Sp(F)`), realizes BOTH local L-factors (the
finite Euler factor `1 - q^{-s}F` and the archimedean Gamma-factor) as regularized
characteristic series of `Theta`, and pins the functional-equation sign to a
regularized superdimension `sdim_inf Theta` which is the APS eta-invariant. This is
the formal substrate under 2R, under the Lean archimedean kernel, and the precise
meaning of the determinant in Direction 4.6.

## Technical content (section by section)

**Section 0, Introduction (pp.1-2).** Deninger states the program's promises
verbatim. [De1], [De2] interpreted local L-factors of pure motives as regularized
characteristic power series on infinite-dimensional cohomologies; that suggested an
"arithmetic site" whose global cohomology would connect to global motivic L-series,
and in particular a formula for the Riemann xi-function as a regularized
characteristic power series (proved in [De2] section 4). This paper extends the
interpretation to MIXED motives. For the finite primes it gives an improved
construction of the infinite-dimensional cohomologies using an elementary case of
the Riemann-Hilbert correspondence, dropping the semisimplicity assumption of [De2]
(a point noted independently by S. Bloch). The stated objectives for the
"still speculative arithmetic cohomology" are exactly the project's milestone list:
(a) "What form should a Lefschetz fixed point formula take? We mention the relation
with explicit formulas in analytic number theory" (= Direction 4.6 / 2R); (b) "We
give a short proof in the spirit of [Se] of the Riemann hypotheses assuming that a
Hodge *-operator with standard properties exists on the prospected cohomologies"
(= Direction 8, the signature); (c) "we relate the functional equation for motivic
L-series to Poincare duality"; (d) "relations between a Kuenneth formula and
Kurokawa's multiple zeta functions" (= the product / cross structure, the 2K theme).
In sections 1-6 everything is proved; section 7 is speculative.

**Section 1, Regularized determinants and dimensions (pp.2-6).** This is the rigorous
definition. Let `Theta` be an endomorphism of a complex vector space `V` of countable
dimension. Conditions: (1) `V` is a direct sum of finite-dimensional `Theta`-invariant
subspaces, with each `alpha in C` an eigenvalue on at most finitely many of them;
equivalently (1') `V = (+)_alpha V_alpha` with `V_alpha = Ker(Theta - alpha)^n` for `n`
large, `m(alpha) = dim V_alpha` the algebraic multiplicity. (2) The eigenvalue Dirichlet
series `zeta_Theta(s) = sum_{alpha != 0} alpha^{-s}` (principal branch `-pi < Arg alpha <= pi`)
converges absolutely for `Re s >> 0` and continues holomorphically past `s = 0`. Then
the definitions (1.1):
`dim_inf(Theta|V) = dim V_0 + zeta_Theta(0)` and
`det_inf(Theta|V) = exp(-zeta'_Theta(0))` if `0 not-in Sp(Theta)`, else `= 0`.
**Lemma 1.2**: for a commutative diagram with exact rows `0 -> V' -> V -> V'' -> 0` and
`Theta`-equivariant verticals, if `det_inf Theta'` and `det_inf Theta''` are defined then
so is `det_inf Theta`, with `det_inf Theta = det_inf Theta' . det_inf Theta''` and
`dim_inf Theta = dim_inf Theta' + dim_inf Theta''` (determinants multiply, dimensions add
on exact triangles). For real `delta > 0`,
`det_inf(delta . Theta | V) = delta^{dim_inf(Theta|V)} det_inf(Theta|V)`.

The functional-equation sign needs `delta = -1`, which is where the **regularized
superdimension** enters (1.3). Given a `Theta`-invariant splitting `V = V^+ (+) V^-`,
assume the two half-Dirichlet-series `zeta_{Theta^+}, zeta_{Theta^-}` continue to
`Re s > -eps` with at most a first-order pole at `s = 0`, writing
`zeta_{Theta^+-}(s) = lambda^{+-}/s + H^{+-}(s)`. Then
`sdim_inf Theta = (dim V_0^+ + H^+(0)) - (dim V_0^- + H^-(0))`.
**Lemma 1.4**: the superdimension is independent of the choice of standard decomposition
(commensurable splittings give the same value), and when both half-dimensions exist their
difference is an even integer. (1.5) fixes a standard decomposition by the argument of
the eigenvalue: `V^+` collects `alpha = 0` or `-pi < Arg alpha <= 0`, `V^-` collects
`0 < Arg alpha <= pi`. **Lemma 1.6** (the sign formula): if `det_inf Theta` and
`sdim_inf Theta` exist then `det_inf(-Theta) = e^{i pi (sdim_inf Theta)} det_inf Theta`.
Proof uses `Arg(-alpha) = Arg alpha +- pi` to write
`zeta_{-Theta}(s) = e^{-i pi s} zeta_{Theta^+}(s) + e^{i pi s} zeta_{Theta^-}(s)`, with the
`lambda^+ + lambda^- = 0` cancellation (forced by `det_inf Theta` being defined) making
this holomorphic at `s = 0`. **The decisive remark** (end of section 1): "If `dim_inf
Theta^{+-}` exist, then `sdim_inf Theta` can be viewed as the eta-invariant of `Theta`
in the sense of Atiyah-Patodi-Singer." So the functional-equation sign is governed by a
regularized `dim^+ - dim^-`, a signature-flavoured quantity living on the trace side.

**Section 2, Regularized determinants and Riemann-Hilbert on `G_m` (pp.6-13).** This is
the local construction for the finite primes, now free of the semisimplicity hypothesis.
On `G_m / C` consider regular-singular algebraic differential equations `(M, nabla)`. Fix
`i = sqrt(-1)`, identify `Z = pi_1(C^*, 1)` via `1 -> e^{2 pi i t}`. Set
`L = Gamma(G_m, O) = C[z, z^{-1}]`, the generator `Theta = z d/dz`, and `Delta = L[Theta]`.
**D.E.R.S.(`G_m`)** is the category of left `Delta`-modules `D` regular-singular at `0, inf`,
free of finite rank over `L`. Since `L` is principal, the functor
`H(D) = (D (x)_L O(C))^{Theta = 0}` (the horizontal sections, with `e: C -> C^*`,
`e(tau) = exp(2 pi i tau)` the universal cover and `Theta` acting by `(1/2 pi i) d/d tau`)
is an equivalence between D.E.R.S.(`G_m`) and finite-dimensional complex representations of
`Z`. Key facts: `rk_L D = dim_C H(D)` (2.1); the comparison `H^w(t, D) = H^w(Z, H(D))`
(2.3), `D^{Theta = 0} = H(D)^Z` and `D/Theta D = H(D)_Z` (2.4). Writing `L(alpha)` for the
rank-one module on which `Theta` acts by `Theta_L - alpha`, every object is a successive
extension of the `L(alpha)` (Remark 2.5). Let `F` be the inverse-monodromy automorphism on
`H(D)` (the action of `-1 in Z`).

**Corollary 2.6** (the local `log p <-> p` law): as sets with multiplicities,
`Sp(Theta) = e^{-1} Sp(F)`, i.e. the additive eigenvalues of the generator are the
logarithms (`/ 2 pi i`) of the multiplicative eigenvalues of the local Frobenius/monodromy
`F`. **Lemma 2.7** (the archimedean Gamma-factor as a regularized product): the regularized
product `prod_{nu in Z} gamma(z + nu) = 1 - e^{-2 pi i z}` (resp. `1 - e^{2 pi i z}`,
depending on `Im z` and `sign gamma`), proved through the Hurwitz zeta function with
`zeta(0, z) = 1/2 - z` and `partial_s zeta(0, z) = log Gamma(z) - (1/2) log 2 pi`, giving
`exp(-partial_s zeta-bar(0, z)) = (Gamma(z)/sqrt(2 pi))^{-1}` (2.7.1). So the Gamma-function
itself is a regularized determinant. **Corollary 2.8 / (2.9)**: for `q > 1`,
`Theta_q = (2 pi i / log q) Theta`, the finite local L-factor is the regularized
characteristic series of `Theta_q`:
`det_inf(delta(s -+ Theta_q) | D) = det(1 - q^{-s} F^{-+1} | H(D))`.
And (2.10) computes the sign of the same regularized determinant under `Theta -> -Theta`:
`det_inf(-delta(s - Theta_q)|D) = eps(s) det_inf(delta(s - Theta_q)|D)` with
`eps(s) = (-q^s)^{dim H(D)} det(F | H(D))^{-1}`, the local epsilon-factor, again an instance
of the sdim/eta sign formula 1.6. (2.11)-(2.12) give twists `D(alpha)` and an explicit
quasi-inverse `D(H) = (H_s (x)_C B)^Z` (with the unipotent part feeding `(1/2 pi i) log F_u`)
that fixes the [De2] error of taking the wrong derivation when `F` is not semisimple.

**Section 3, The non-archimedean local L-factors (pp.13-16).** Globalizes section 2 to
mixed motives. For a local non-archimedean field `K`, inertia `I`, geometric Frobenius `F`,
and a mixed motive `M` with l-adic realization `M_l`, the `E (x) C`-valued local factor is
`L_K(M, s) = (det_C(1 - F N p^{-s} | M_{l,i,sigma}^I)^{-1})_sigma`. Composing the l-adic
realization with a quasi-inverse `D` to `H` gives an `E`-linear functor
`F = F_{p,l,i}: MM_K(E) -> D_p(E)`, and **Proposition 3.2**:
`L_K(M, s) = det_inf(delta(s - Theta) | F_p(M)_sigma)^{-1}`. The good-reduction restriction
`H^*(_/L)` is a tensor functor between Tannakian categories, hence "a cohomology theory on
motives in the sense of Grothendieck" (with Poincare duality, Kuenneth, Chern classes), but
its definition through l-adic cohomology "just shows that such a theory exists; an
independent construction would be of great interest." This is the precise statement of the
gap Direction 4.6 must fill on the finite-place side.

**Section 4, Interlude: varieties over finite fields (pp.16-17).** The Weil-conjecture
prototype. For `X / F_q`, `H^*(X/L) = D(H^*(X-bar, Q_l) (x) C)` with geometric Frobenius
`F`. **Proposition 4.1**:
`i det_{Q_l}(1 - q^{-s} Fr_q^* | H^w(X-bar, Q_l)) = det_inf(s - Theta_q | H^w(X/L))`, and the
functional equation
`det_inf(s - Theta_q | H^w) = eps_w(s)^{-1} det_inf((d - s) - Theta_q | H^{2d-w})` falls out of
Poincare duality `H^w x H^{2d-w} -> H^{2d} -> L(-d)`, with the global sign
`zeta_X(s) = e^{i pi (chi^+(s) - chi^-(s))} zeta_X(d - s)`, again the sdim/eta sign. By
Deligne the `Theta_q`-eigenvalues on `H^w` have weight `w`, i.e. real part `w/2`. This is the
RH analogue that holds in the function-field world and that the program is trying to lift.

**Section 5, Logarithmic connections and the archimedean factor (pp.17-20).** Builds the
archimedean analogue `F_inf` of the finite-place functor. D.E.L.S.(`G_a`) is vector bundles
on `G_a` with a connection having at most a log pole at `0`; `L^+ = C[z]`, `Theta = z d/dz`.
For `K = R` or `C`, `e_K = [C : K]`, `Theta_K = -e_K Theta`. The category `Fil_K` of filtered
vector spaces (with an involution `F_inf` in the real case) maps by `D^+(V) = Fil^0(V (x) L)`
(real case `Fil^0(V (x) L)^{F_inf = id}`, viewed via the squaring map `sq(z) = z^2`).
**Proposition 5.1**: every object of `Fil_K` is a finite sum of Tate twists `C(n)`, and
`D^+` is an equivalence onto a subcategory of `D_K`. **Proposition 5.2** (the archimedean
local factor as a regularized determinant): for `V` in `Fil_K` with `d_nu = dim Gr^nu V`,
`det_inf((1/2 pi)(s - Theta_K) | D^+(V)) = prod_{nu in Z} Gamma_K(s - nu)^{-d_nu}`,
where `Gamma_R(s) = 2^{-1/2} pi^{-s/2} Gamma(s/2)` and `Gamma_C(s) = (2 pi)^{-s} Gamma(s)`.
Remark: completing the Riemann zeta at infinity with `Gamma_{R,delta}` introduces the
epsilon-factor `(2 pi delta)^{s - 1/2}` in the functional equation. So the archimedean
place is handled by the SAME `det_inf` formalism as the finite places: the finite Euler
factor `1 - q^{-s} F` (section 2) and the Gamma-factor (section 5) are both regularized
characteristic series of one operator `Theta`, only the spectrum differs (a single
Frobenius eigenvalue at a finite place, the integer lattice `Z` of Hodge weights at infinity).

## Points mapped to the project

1. **The program's milestone list IS Deninger's section 0.** The four stated objectives
   (Lefschetz formula / explicit formula = 4.6 and 2R; Hodge-* RH proof = Direction 8;
   functional equation = Poincare duality; Kuenneth = Kurokawa multiple zetas = the
   product/cross structure of 2K) are the project's four-direction decomposition stated by
   Deninger in 1994. Good external confirmation that the program is organized along the
   author's own axes.
   -> Read the project's Direction-4.6-and-8 split as Deninger's (a) and (b); they are not
   independent inventions.

2. **2R is now grounded: section 1 is the rigorous definition of the object 2R computed.**
   The `det_inf(Theta|V) = exp(-zeta'_Theta(0))` of (1.1), with the exact-triangle
   multiplicativity of Lemma 1.2, is the precise meaning of the `det_zeta(s - Theta)` in
   Direction 4.6. 2R verified `-zeta'/zeta = sum Lambda(n) n^{-s}`, the log-derivative of
   exactly this regularized determinant over the `H^1` prime side. Deninger I is the
   definition that makes 2R's "regularized determinant" rigorous rather than formal.
   -> Cite Deninger I section 1 for "what `det_zeta(s - Theta)` means" whenever 4.6/2R is
   written up.

3. **A trace-side signature exists: `sdim_inf Theta` = the APS eta-invariant (1.3-1.6).**
   This is the most novel takeaway for the live front. The functional-equation sign is
   `det_inf(-Theta) = e^{i pi sdim_inf Theta} det_inf Theta`, and `sdim_inf Theta` is a
   regularized `dim V^+ - dim V^-`, explicitly the eta-invariant of `Theta`. A
   signature-flavoured quantity therefore appears on the regularized-determinant (trace)
   side itself, governing the sign. This is the closest the trace side comes to the
   Direction-8 Hodge-* signature, and it is exactly where 2R stops: 2R produces the
   spectrum / `det`; the sign / `sdim` / eta is the next structural layer. The local
   instance is the epsilon-factor `eps(s) = (-q^s)^{dim H(D)} det(F|H(D))^{-1}` of (2.10);
   over finite fields it is the `eps_w(s)` of section 4.
   -> Treat `sdim_inf` / eta as a candidate bridge from 2R (trace spectrum) to Direction 8
   (Hodge-* signature). The Hodge-*-operator's job is precisely to make this `sdim` / eta
   controllable. This is the thread most worth pulling for the trace-to-signature question
   (deepened by Deninger II section 6, where the same Theta-as-derivation becomes a
   skew-adjoint operator on the cup-product pairing).

4. **The local `log p <-> p` passage is the Riemann-Hilbert `Sp(Theta) = e^{-1}Sp(F)`
   (Corollary 2.6).** The additive eigenvalues of the generator are the logarithms of the
   multiplicative eigenvalues of the local Frobenius. This is the local form of 2Q's `(1, p)`
   bidegree and 2R's `{log p}` orbit lengths: `log(Frobenius eigenvalue) = generator
   eigenvalue`, the same `log p <-> p` passage, now pinned to a theorem rather than a slogan.
   The non-semisimple version (the unipotent part `(1/2 pi i) log F_u`, 2.12) is the technical
   improvement over [De2], which the program inherits for free.
   -> 2Q's bidegree and 2R's orbit lengths are the global assembly of the local 2.6. Use 2.6
   as the local certificate.

5. **The Lean archimedean kernel is on solid ground (Lemma 2.7, Proposition 5.2).** Deninger
   derives the Gamma-factor `Gamma_R(s) = 2^{-1/2} pi^{-s/2} Gamma(s/2)` itself as a
   regularized product / regularized determinant of `Theta` on the Hodge lattice. The Lean
   `ExplicitFormula` `archKernel = -(1/2) log pi + (1/2) psi(1/4 + i r / 2)` is the
   log-derivative of this Gamma-factor, and `digamma = (log Gamma)'`. The archimedean block
   `A_arch` (2I) is this regularized Gamma-factor; the finite places are the `1 - q^{-s} F`
   Euler factors of (2.9); ALL places use the SAME `det_inf` formalism, only the spectrum of
   `Theta` differs.
   -> No change needed to the Lean kernel, but the foundation is now explicit and uniform:
   `new_mathematics.md` section 4.2's "cohomology that knows about archimedean primes" is
   made concrete at the local level by section 5 (the Hodge-weight lattice `Z` is the
   archimedean spectrum of `Theta`).

6. **The functional equation = Poincare duality (section 4), the product = Kuenneth /
   Kurokawa (section 0).** Section 4 derives the function-field functional equation from
   Poincare duality `H^w x H^{2d-w} -> L(-d)` as an identity of regularized determinants. The
   Kuenneth / Kurokawa remark in section 0 is the seed of the 2K product theme: the cross
   structure should multiply L-functions, and additive relations among zeros (the
   Kontsevich-Manin question) would be the cup-product trace, made precise in Deninger II
   section 3.7.
   -> The 2K product gap and the Direction-8 duality are both already named in Deninger I
   section 0; Deninger II section 3.7 / section 6 sharpen them.

## What this changes for the program

- **2R is grounded.** Section 1 is the rigorous regularized determinant whose log-derivative
  2R computed. Cite it for the meaning of `det_zeta(s - Theta)`.
- **A trace-side signature exists: the eta-invariant / superdimension.** The
  functional-equation sign is governed by `sdim_inf Theta` (the APS eta-invariant), a
  regularized `dim^+ - dim^-` living on the trace side yet signature-flavoured. This is a
  possible conceptual bridge from 2R (spectrum) toward the Direction-8 Hodge-* signature, and
  it sharpens what "the signature must emerge from the flow" means: the Hodge-*-operator must
  control this `sdim` / eta.
- **The local `log p <-> p` passage is a theorem (2.6).** `Sp(Theta) = e^{-1}Sp(F)`. 2Q's
  bidegree and 2R's orbit lengths are the global assembly of this local fact.
- **The Lean archimedean kernel is on solid ground.** Deninger derives the Gamma-factor as a
  regularized determinant of `Theta` on the Hodge lattice; the Lean kernel is its
  log-derivative. The finite Euler factors and the archimedean Gamma-factor are two instances
  of one `det_inf` formalism (sections 2 and 5), uniform across all places.

## Actionable

- The `sdim_inf` / eta-invariant to Hodge-* signature link (section 1 here + Deninger II
  section 6) is the thread most worth pulling for the trace-to-signature question. No new
  computation yet, but it is the cleanest statement of "what would make the signature emerge":
  the Hodge-* operator must make the regularized superdimension / eta controllable. Deninger II
  section 6 turns the same `Theta`-as-derivation into a skew-adjoint operator
  `Theta - (n+1)/2 . id` on a perfect alternating cup-product pairing, forcing the order to be
  even (sign `+1`); that is the next concrete step to study.
- Next read in the program order: Deninger II (the `H^1` whose `Theta`-eigenvalues are the
  zeta zeros, the regularized determinant 3.8, the section 3.7 product gap, and the section 6
  signature mechanism), then Leichtnam 2006 (the foliated-flow trace formula realizing this
  `H^1`), then Alvarez-Lopez-Kordyukov-Leichtnam 2017 (the general foliated trace formula).

## Status

Read deeply: pp.1-20 (section 0 introduction; section 1 the regularized determinant 1.1,
exact-triangle Lemma 1.2, the superdimension 1.3-1.5 and the eta-invariant sign Lemma 1.6;
section 2 the Riemann-Hilbert equivalence on `G_m`, the comparison 2.3/2.4, Corollary 2.6
`Sp(Theta) = e^{-1}Sp(F)`, the regularized-product Lemma 2.7, the local L-factor and
epsilon-factor 2.8/2.9/2.10, the quasi-inverse 2.11/2.12; section 3 the non-archimedean local
factor and Proposition 3.2; section 4 the finite-field prototype and functional equation
Proposition 4.1; section 5 the filtered-vector-space functor `D^+` and the archimedean
Gamma-factor as a regularized determinant Proposition 5.2). The remaining sections 6-7 (the
global archimedean `F_inf` and the speculative arithmetic-site discussion) are covered through
the cross-references in Deninger II. Honest depth: the regularized-determinant formalism
(section 1), the Riemann-Hilbert local construction (section 2), and the two local-factor
computations (sections 2 and 5) are understood at the statement level with the key proofs
traced; the finest analytic-continuation estimates in the Hurwitz-zeta computation of 2.7 are
summarized, not re-derived line by line.
