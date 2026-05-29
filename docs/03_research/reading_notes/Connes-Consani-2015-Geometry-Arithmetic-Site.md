# Reading notes: Connes-Consani, *Geometry of the Arithmetic Site* (arXiv:1502.05580, 2015)

> Entry in the reference-library read-through
> ([`references/README.md`](../../../references/README.md)). This is the paper most
> directly on the project's LIVE front (Direction 8). It constructs a geometric SQUARE
> of a site built from `Spec(Z)`, with a one-parameter semigroup of **Frobenius
> correspondences** `Psi(lambda)` on that square. That is exactly the missing object
> that Direction 8 / 2K name: a product `Spec(Z) x Spec(Z)`-flavoured surface carrying a
> Frobenius correspondence `Gamma_S`, realized here over the tropical/characteristic-1
> base `R^max_+` instead of over a field. Mapped to 2K (the absolute base point), 2Q
> (the Frobenius correspondence and the `Z x Z` bidegree index set), 2R (`Gamma_S^2`),
> 3M (the Euler-product / D-H detector), and the product-surface + Hodge-index milestone.
> Pages refer to the PDF in `references/04_ncg_connes/`. Read deeply: pp.1-18 (intro,
> Thm 1.1, Thm 1.2, the topos `N^x-hat` and its points = rank-one ordered groups (Thm
> 2.1), adelic interpretation Prop 2.5, the structure sheaf `Z_max` and stalks Thm 3.2,
> points over `R^max_+` Thm 3.8, Hasse-Weil formula Thm 4.2, the `Spec(Z)` morphism §5)
> and pp.22-39 (§6 the square + Frobenius correspondences in full, §7 the composition
> law in full through Thm 7.7).

## One-line takeaway

Connes-Consani build the **Arithmetic Site** `(N^x-hat, Z_max)`: a Grothendieck topos
(the topos of sets with an action of the multiplicative monoid `N^x` of non-zero
naturals) with a characteristic-1 structure sheaf `Z_max = (Z u {-inf}, max, +)`, whose
points over the tropical semifield `R^max_+` coincide exactly with Connes' adele class
space quotient `Z-hat^x \ A_Q/Q*`, with the action of `R*_+` (Frobenius `Fr_lambda(x) =
x^lambda`) reproducing the idele-class / Frobenius flow. They then construct the
**square** as the topos `N^x2-hat` with structure sheaf `Z_min (x)_B Z_min` (= hereditary
subsets / Newton polygons in `Z x Z`), and exhibit a one-parameter semigroup of
**Frobenius correspondences** `Psi(lambda)`, `lambda in R*_+`, as congruences on that
square, with composition law `Psi(lambda) o Psi(lambda') = Psi(lambda lambda')`. This is
a concrete `Spec(Z)`-flavoured product surface plus Frobenius correspondence, over
characteristic 1, the literal target of Direction 8. What it does NOT carry is a signed
intersection pairing (the operations are idempotent), so the Hodge-index SIGNATURE is
exactly the residual gap.

## Technical content (section by section)

**Abstract + §1 Introduction (pp.1-4).** The thesis: the arithmetic site is "an
algebraic geometric space deeply related to the non-commutative geometric approach to
RH." Its topological space is the topos `N^x-hat` of functors from the multiplicative
monoid `N^x` to Sets. Its structure sheaf is a semiring of characteristic 1, namely
`Z_max := (Z u {-inf}, max, +)`, on which `N^x` acts by Frobenius endomorphisms `Fr_k(n)
:= kn`. The role of the algebraic closure `F-bar_q` (as `q -> 1`) is played by the
semifield `R^max_+` of tropical reals, `R_+ = [0, inf)` with ordinary product and
`x v y = max(x,y)`, endowed with the one-parameter group of automorphisms `Fr_lambda(x)
= x^lambda`, `lambda in R*_+`. Fixed points of all `Fr_lambda` form the Boolean semifield
`B = {0,1}`, the only finite semifield, with `Gal_B(R^max_+) = R*_+`. **Theorem 1.1**:
the set of points of `(N^x-hat, Z_max)` over `R^max_+` coincides with the quotient
`A_Q/Q*` of the adele class space by `Z-hat^x` (= `Z-hat^x \ A_Q/Q*`); the `Fr_lambda`
action corresponds to the idele class group action. The introduction announces the
square `N^x2-hat` with sheaf `Z_min (x)_B Z_min` (the tensor square over the smallest
Boolean semifield), built from Newton polygons, and **Theorem 1.2**: the Frobenius
correspondences satisfy `Psi(lambda) o Psi(lambda') = Psi(lambda lambda')` when
`lambda lambda' not-in Q` (and for rational arguments), but `Psi(lambda) o Psi(lambda')
= Id_eps o Psi(lambda lambda')` when `lambda, lambda'` are irrational and
`lambda lambda' in Q`, where `Id_eps` is the **tangential deformation of the identity
correspondence**. Note: `Z_min := (Z u {+inf}, min, +)` is isomorphic to `Z_max` via
`n -> -n`; the multiplicative notation associates `q^n` to `n in Z_min`, so the second
operation becomes ordinary product and the first is `x v y = max` (with `0 < q < 1`).

**§2 The points of the topos `N^x-hat` (pp.5-9).** The category of points of a presheaf
topos `C-hat` is equivalent to the category of flat (filtering) functors `C -> Sets`
(§2.1). For `C = N^x` (one object `*`), a point is a flat functor `F` determined by the
set `X = F(*)` with an `N^x`-action. **Theorem 2.1**: the category of points of `N^x-hat`
is equivalent to the category of totally ordered groups isomorphic to non-trivial
subgroups of `(Q, Q_+)`, with injective morphisms of ordered groups. The proof
(Lemmas 2.2-2.3) shows the addition `x + x' := F(k + k')z` (for `F(k)z = x`, `F(k')z = x'`)
makes `X` the strictly positive part of an abelian totally ordered group `(H, H_+)`, an
increasing union of copies of `(Z, Z_+)`, hence a subgroup of `(Q, Q_+)`. §2.3 treats
the variant `N^x_0` (adjoin a 0-element to the monoid): **Theorem 2.4** gives the same
points but the category is now **pointed** (a unique initial/final object 0); `N^x_0-hat`
is `N^x-hat` with one base point adjoined. §2.4 (adelic interpretation): `A^f =
prod'_p Q_p` is the finite adeles, `Z-hat = prod Z_p` its maximal compact subring,
`A^f = Z-hat (x)_Z Q`, with `Q^x_+` acting on `A^f`. **Proposition 2.5**: every
non-trivial subgroup of `Q` is uniquely `H_a := {q in Q | aq in Z-hat}`, `a in
A^f/Z-hat^x`; the map `a -> H_a` is a canonical bijection
`Q^x_+ \ A^f / Z-hat^x  <->  {iso classes of points of N^x-hat}`. Proof via Pontryagin
duality (`Z-hat = (Q/Z)-hat`) and the structure of closed subgroups/ideals of `Z-hat`.
Remark 2.7: these subgroups are equivalently the supernatural numbers (Steinitz) in
`Z-hat/Z-hat^x`. Remark 2.8 flags the key gap at this stage: without a structure sheaf,
`N^x-hat` has too many automorphisms (arbitrary permutations of primes), so the topos
alone does not have enough geometric structure.

**§3 The Arithmetic Site `(N^x-hat, Z_max)` (pp.10-13).** **Definition 3.1**: the
arithmetic site is `N^x-hat` endowed with the structure sheaf `O := Z_max` viewed as a
semiring in the topos via the Frobenius action `Fr_k(n) := kn`. It is a "semi-ringed
topos." **Theorem 3.2**: the stalk of `O` at the point associated to the ordered group
`H subset Q` is canonically the semiring `H_max := (H u {-inf}, max, +)`. **Proposition
3.5**: the global sections `Gamma(N^x-hat, Z_max)` are exactly the `N^x`-invariant
elements, i.e. the sub-semifield `B subset Z_max`. This says (Prop 3.5 + comment) the
arithmetic site, as a generalized scheme over `B`, behaves like a **curve that is
complete and irreducible**. §3.2 puts a structure on the points over `R^max_+`.
**Lemma 3.7**: `Phi(a, lambda) := lambda H_a` is a bijection
`Q^x_+ \ ((A^f/Z-hat^x) x R*_+)  <->  {non-zero subgroups of R with pairwise commensurable
elements}`. **Theorem 3.8** (the central identification): the points of `(N^x-hat,
Z_max)` over `R^max_+` form the quotient of the adele class space of `Q` by `Z-hat^x`;
the action of the Frobenius automorphisms `Fr_lambda` corresponds to the idele class
group action. The proof splits a point `(p, f_p^#)`, `f_p^#: K = H_max -> R^max_+`, into
two cases: (alpha) range in `B` (degenerate points, fixed by all `Fr_lambda`; these are
the points of `N^x-hat` over `B`), and (beta) range a sub-semifield of `R^max_+`, which
is determined up to iso by the rank-one subgroup `H' = {log u | u in f_p^#(K), u != 0}
subset R`. The first set is `Q^x_+ \ A^f / Z-hat^x`, the second is the
non-degenerate part; together they reconstruct the full adele class quotient. Crucially,
`Fr_lambda` acts as `H -> lambda H` (scaling on the `log` side, i.e. `log u -> lambda
log u -> 0` as `lambda -> 0`), which is the idele-class scaling action.

**§4 Hasse-Weil formula for the Riemann zeta function (pp.14-17).** §4.1 describes the
periodic orbits of the Frobenius flow on points over `R^max_+`: they correspond, at a
place `v`, to adeles `a` with `a_v = 0`. At `v = infinity` (archimedean), the condition
means the point is fixed by `Fr_lambda` (lies in the `B`-part); these are the
points over `B`. At a finite place `v = p`, the condition `a_p = 0` means
`Fr_lambda(alpha) = alpha` for all `lambda in p^Z`, i.e. the Frobenius `x -> x^p` is an
automorphism of the intermediate semifield `B subset K subset Q_max`. §4.2 (counting):
the trace formula `Tr_distr(int h(w) vartheta(w) d*w) = sum_v int'_{Q_v^x}
h(w^-1)/|1-w| d*w` (eq. 10) on the adele class space. The archimedean term gives the
distribution `kappa(u) = u^2/(u^2-1)` plus `c f(1)`, `c = (1/2)(log pi + gamma)` (eq.
14), positive on `(1, inf)`. The finite-place terms give `sum_{m>=1} log p g(p^m)` (eq.
15), i.e. **the von Mangoldt prime-power sum**. §4.3: the resulting counting distribution
`N(u)` on `[1, inf)` is fed into the `q -> 1` Hasse-Weil formula (Soule's `zeta_N(s) :=
lim_{q->1} Z(q, q^-s)(q-1)^{N(1)}`, eqns 17-22). **Theorem 4.2**: the zeta function
associated to this counting distribution is the **complete** Riemann zeta `zeta_Q(s) =
pi^{-s/2} Gamma(s/2) zeta(s)`. The counting distribution is `N(u) = u - (d/du)(sum_{rho}
order(rho) u^{rho+1}/(rho+1)) + 1`, `rho` the non-trivial zeros, derivative in the
distribution sense. Stated open question (end of §4): the missing object is a "suitable
Weil cohomology" that would let one read this equality as a Lefschetz formula.

**§5 Relation of `Spec(Z)` with the arithmetic site (pp.18-21).** A geometric morphism
of topoi `Theta: Spec(Z) -> N^x_0-hat` (Zariski topos on `Spec(Z)`) is constructed via
a flat functor `Theta^*: N^x_0 -> Sh(Spec(Z))`. The sheaf `S` (Def 5.1) has stalk at a
prime `p` the ordered group `H(p) = {q in Q | alpha_p q in Z-hat}^+` (denominators a
power of `p`); the generic point of `Spec(Z)` maps to the base point `{0}` of `N^x_0-hat`
(Remark 2.9, Thm 5.3). Prop 5.7 interprets the pullback `Theta^*(O)` via Cartier
divisors on `Spec(O^cyc)` (the ring of cyclotomic integers); the valuation
`v(pi)/varphi(n) = ... = H(p)` recovers the local picture. This is the structure
morphism `Spec(Z) -> Arithmetic Site` of Figure 1.

**§6 The square of the arithmetic site and Frobenius correspondences (pp.22-32). MOST ON-FRONT.**
§6.1: `Mod(B)` (B-modules) is a closed symmetric monoidal category; the tensor product
`E (x)_B F` is the initial object among bilinear maps, built from formal sums `sum e_i
(x) f_i` (no coefficients, idempotent) modulo `sum e_i (x) f_i ~ sum e'_j (x) f'_j iff
sum rho(e_i, f_i) = sum rho(e'_j, f'_j)` for all bilinear `rho`. §6.2 (the unreduced
square): bilinear maps `Z_min x Z_min -> R` satisfy `phi(a v b, c) = phi(a,c) (+)
phi(b,c)` etc. **Lemma 6.2** gives the relation `x1 v x2 = x1, y1 v y2 = y1  =>
(x1 (x) y1) (+) (x2 (x) y2) = x1 (x) y1` (eq. 26). **Definition 6.3**: `Sub_>=(J)` =
finite unions of intervals `I_x = {y | y >= x}` (hereditary/upper subsets). **Lemma 6.5**:
`Sub_>=(N x N)` = hereditary subsets of `N x N` (the upper-right staircase regions; see
Fig 2). **Proposition 6.6**: `psi(u,v) := {(a,b) in Z x Z | a >= u, b >= v}` is bilinear
and gives the identification `Z_min (x)_B Z_min = Sub_>=(Z x Z)` (eq. 28). So elements of
the tensor square are **Newton polygons** (hereditary subsets / staircase regions of
`Z x Z`), with addition = union. **Proposition 6.7**: multiplicative notation `q^a (x)_B
q^b`, the multiplication `(q^a (x) q^b)(q^c (x) q^d) = q^{a+c} (x) q^{b+d}` (eq. 29) turns
`S = Z_min (x)_B Z_min` into a semiring of characteristic 1; an action of `N^x x N^x` by
endomorphisms `Fr_{n,m}(sum q^a (x) q^b) := sum q^{na} (x) q^{mb}` (eq. 30), realized
geometrically as the affine map `diag(n,m)` on the quadrant `Q = R_+ x R_+` (preserves
`Q`, commutes with union and sum). **Definition 6.10**: the unreduced square
`(N^x2-hat, Z_min (x)_B Z_min)`, the topos `N^x2-hat` (= dual of `N^x x N^x`) with that
semiring structure sheaf, with two projections to `(N^x-hat, Z_max)`. **Proposition
6.11**: the points of the unreduced square over `R^max_+` coincide with the product of
the points of `(N^x-hat, Z_max)` over `R^max_+` (the stalk at `(H1,H2)` is `H1,max (x)_B
H2,max`). §6.3 (Frobenius correspondences): the product `mu: Z_min (x)_B Z_min -> Z_min`,
`mu(q^a (x) q^b) = q^{a+b}` (= inf of `n_i + m_i`, eq. 33), is the diagonal; the Frobenius
correspondence `C_r` for `r = n/m` is `mu o Fr_{n,m}`. **Proposition 6.12** computes the
range and its semiring `F(n,m)` (a Sylvester / Frobenius-coin-problem object: the range
contains the ideal `{q^a | a >= (n-1)(m-1)}`); part (iii) shows `mu o Fr_{n,m}` equals
`m_r(sum (q^{n_i} (x) q^{m_i})) = q^alpha`, `alpha = inf(rn_i + m_i)` (Fig 4). **Proposition
6.13**: for `lambda in R*_+` and `q in (0,1)`, `F(lambda, q): Z_min (x)_B Z_min -> R^max_+`,
`F(lambda, q)(sum q^{n_i} (x) q^{m_i}) = q^alpha`, `alpha = inf(lambda n_i + m_i)` is a
semiring homomorphism; `R(lambda) := F(lambda, q)(...)` is independent of `q`, and
`R(lambda) ~ R(lambda') iff lambda' in {lambda, 1/lambda}`. So `lambda` (the slope) is a
genuine real invariant of the correspondence (the Dedekind cut recovered, Prop 6.13(iii),
Remark 6.14). §6.4 (the reduced square): **Definition 6.17** `Conv_>=(Z x Z)` = closed
convex subsets `C subset R^2` with `C + R_+^2 = C` (upward-closed), `C subset z + R_+^2`,
extreme points in `Z x Z`, with operations `conv(C u C')` (convex hull of union) and
`C + C'` (Minkowski sum). **Lemma 6.18**: it is a semiring of characteristic 1.
**Proposition 6.19**: the congruence `F(lambda,q)(x) = F(lambda,q)(y)  for all lambda`
has quotient semiring `Conv_>=(Z x Z)`. **Proposition 6.21**: `Conv_>=(Z x Z)` is
multiplicatively cancellative and is the semiring of fractions of `Z_min (x)_B Z_min`
(via `gamma = convex-hull`); crucially `x -> x^n` is NOT the endomorphism `Fr_{n,n}`
(the latter is `E -> nE`, multiplication by `n` of the polygon, NOT the `n`-th power),
since `Z_min (x)_B Z_min` fails to be multiplicatively cancellative (Remark 6.9, eq.
after Prop 6.21). **Definition 6.22**: the reduced square `(N^x2-hat, Conv_>=(Z x Z))`.

**§7 Composition of Frobenius correspondences (pp.33-39). MOST ON-FRONT (the `Gamma_S^2` analogue).**
§7.1: a reduced correspondence is a triple `(R, l, r)`, `R` a mult-cancellative
semiring, `l, r: Z_min^+ -> R` semiring morphisms with `R` generated by `l(Z_min)
r(Z_min)`; `Psi(lambda) := (R(lambda), l(lambda), r(lambda))` with `l(lambda)(q^n) q^alpha
= q^{alpha + n lambda}`, `r(lambda)(q^n) q^alpha = q^{alpha + n}` (eq. 42). The
composition is computed by tensoring `R(lambda) (x)_{Z_min^+} R(lambda')` and taking the
mult-cancellative sub-semiring generated by `l(lambda) (x) Id` and `Id (x) r(lambda')`.
§7.2 (case `lambda lambda' not-in Q lambda' + Q`): **Proposition 7.3** gives the bilinear
map `psi(a,b) = Fr_lambda'(a) b` and shows the reduction is `R(lambda lambda')` with the
expected left/right actions, so `Psi(lambda) o Psi(lambda') = Psi(lambda lambda')`. §7.3
(the delicate case `lambda lambda' in Q lambda' + Q`, `lambda, lambda'` irrational):
here the reduction lands not in `R(lambda lambda')` but in `R_eps(lambda lambda',
lambda')`, the sub-semiring of germs `Germ_{eps=0}(R^max_+)` generated by `q, q^{lambda'},
Fr_{1+eps}(q^{lambda lambda'}) = q^{(1+eps) lambda lambda'}` (Prop 7.4). §7.4 introduces
the tangential deformation: **Definition 7.6** `Id_eps := (R_eps, l_eps, r_eps)`,
`l_eps(q^n) = theta_{1+eps}(q^n) = q^{(1+eps)n}`, `r_eps(q^n) = q^n`. **Theorem 7.7**
(the composition law, the main result): for `lambda, lambda' in R*_+` with `lambda
lambda' not-in Q`, `Psi(lambda) o Psi(lambda') = Psi(lambda lambda')` (same for rational
arguments); but for `lambda, lambda'` irrational with `lambda lambda' in Q`, `Psi(lambda)
o Psi(lambda') = Id_eps o Psi(lambda lambda')`, with `Id_eps` the tangential deformation
of the identity correspondence. Interpretation (intro to §7): for irrational `lambda`,
`Psi(lambda)` has a "flexibility" automatically inherited by composition; this is absent
for rational `lambda` but is restored in the tangential deformation. The
**diagonal/self-composition** is the `lambda' = lambda^{-1}` case: `Psi(lambda) o
Psi(lambda^{-1}) = Id_eps`, i.e. the identity correspondence picks up the tangential
deformation `Id_eps`.

**§8 The structure of the point in noncommutative geometry (pp.41-42).** Recasts
Dixmier's classification of matroids in terms of the noncommutative space of points of
`N^x-hat`. (Not on the project's front; read via the intro.)

## Points mapped to the project

1. **The points of the site = Connes-1998 adele class space, Theorem 1.1 + 3.8.** The
   points of `(N^x-hat, Z_max)` over `R^max_+` are `Z-hat^x \ A_Q/Q*`, with `Fr_lambda`
   the idele-class scaling action. Abstract points of `N^x-hat` (no sheaf) are the
   rank-one ordered groups `H subset Q`, equivalently `Q^x_+ \ A^f / Z-hat^x` (Prop 2.5),
   equivalently supernatural numbers (Remark 2.7). This is the **algebro-geometric
   realization of the Connes-1998 adelic space** (the space the R3.5 K1 wall lives on);
   2K's Morishita bridge links Deninger's foliated systems to exactly this Connes-Consani
   adelic space, and this paper is the algebraic-geometry half. Closed points / primes
   <-> periodic orbits of the Frobenius flow (the `a_p = 0` condition, §4.1) ->

2. **Characteristic 1 / tropical base supplies the `F_1` base point (2K), Definition 3.1 + intro.**
   The structure sheaf is `Z_max`; the role of `F-bar_q` as `q -> 1` is the tropical
   `R^max_+` with Frobenius `Fr_lambda(x) = x^lambda`. The fixed points form the Boolean
   `B = {0,1}`, the only finite semifield, with `Gal_B(R^max_+) = R*_+`. This is the
   "absolute base point" (2K) made concrete: the missing `F_1` base is supplied by
   characteristic-1 geometry, and the structure morphism `Spec(Z) -> N^x_0-hat` (§5) is
   built. The continuum of Frobenius scales `R*_+` (not a single `q`) answers 2Q's "what
   plays the role of `q` over `Spec(Z)`," the same answer Leichtnam's continuous Frobenius
   `R*_+` (type III_{1/q} flow of weights) gives on the dynamical side: two independent
   literatures converge on `R*_+`-as-Frobenius ->

3. **The SQUARE `N^x2-hat` = Newton polygons in `Z x Z` is the missing product surface (Direction 8), §6, Prop 6.6/6.11/6.22.**
   `Z_min (x)_B Z_min = Sub_>=(Z x Z)` (hereditary staircase subsets), reduced version
   `Conv_>=(Z x Z)` (convex polygons, mult-cancellative). Elements are `sum q^{n_i} (x)_B
   q^{m_i}`, indexed on the `Z x Z` lattice. Its points over `R^max_+` are the product of
   the points of the site (Prop 6.11/Remark 6.23). This is NOT `Spec(Z) x_Z Spec(Z)` over
   a literal base; it is the characteristic-1 tensor square of the site, whose elements
   live on the `Z x Z` index set. The project's 2Q "(1,p) bidegree per prime" should be
   read against this: the bidegree lives naturally on the `Z x Z` square, exactly the
   index set here. Direction 8 does not need to invent the product surface; it exists in
   the literature ->

4. **The Frobenius correspondences `Psi(lambda)` are a concrete `Gamma_S`, §6.3-§7, Thm 1.2/7.7.**
   `Fr_{n,m} = diag(n,m)` on the quadrant; `Psi(lambda)` is a congruence on the square of
   real slope `lambda` (the slope is a genuine invariant, Prop 6.13). The composition law
   `Psi(lambda) o Psi(lambda') = Psi(lambda lambda')` is the group law of the Frobenius
   flow `R*_+` acting on the square. This is a concrete, countable-combinatorial
   `Gamma_S` (the Frobenius correspondence on the product). The project's 2R pins
   `Gamma_S^2` to the von Mangoldt prime sum / a Ruelle dynamical zeta `-zeta'/zeta`. The
   self-intersection `Gamma_S^2` the project wants is the **diagonal limit** of the
   composition: `Psi(lambda) o Psi(lambda^{-1}) = Id_eps`, where the **tangential
   deformation `Id_eps`** of the identity appears (Thm 7.7, Def 7.6). That `Id_eps` term
   (a germ-level `q^{(1+eps)n}` deformation) is the analytic shadow of the
   self-intersection / fixed-point contribution. Compare 2R: the `-zeta'/zeta` log-
   derivative / orbit lengths `{log p}` should be sought in the `lambda lambda' in Q`
   deformation regime, where the orbit/prime data sits ->

5. **The complete `zeta_Q` (Gamma-factor included) is intrinsic, §4, Thm 4.2.** Combining
   the point-count `N(u)` over `R^max_+` with the `q -> 1` Hasse-Weil limit yields
   `zeta_Q(s) = pi^{-s/2} Gamma(s/2) zeta(s)`. The archimedean Gamma-factor emerges from
   the site's own point count (the `v = infinity` term `kappa(u) = u^2/(u^2-1)`, eq. 14),
   not bolted on. This reinforces 2I (the project's archimedean block) and the Deninger-I
   regularized Gamma-factor: the archimedean place is part of the geometry, consistent
   with the project's "cohomology that knows about archimedean primes" ->

6. **The Euler-product / D-H detector (3M), §4.2 finite-place terms.** The finite-place
   contributions to the counting distribution are exactly `sum_{m>=1} log p g(p^m)` (eq.
   15), the von Mangoldt prime-power sum, which exists only because of the Euler product
   (the `a_p = 0` periodic-orbit structure at each prime). A function without an Euler
   product (D-H) has no such `{log p}` orbit spectrum. So the Connes-Consani construction
   does distinguish zeta from D-H by the 3M test: the prime-localized von Mangoldt sum is
   structural, not generic ->

7. **The missing object is a SIGNED pairing, not the surface (the Direction-8 gap), §6.**
   The characteristic-1 operations on the square are idempotent (union, max, convex hull,
   Minkowski sum); there is no subtraction, hence no obvious signed intersection number,
   hence no Hodge index / Castelnuovo positivity yet. The paper itself names the residual
   gap (end of §4): a "suitable Weil cohomology" that would let one read the `N(u)`
   equality as a Lefschetz formula. This is the precise form of the Direction-8 gap on the
   Connes-Consani square, and it matches the marginal-positivity thesis: the geometry and
   the Frobenius correspondences exist, the **signature does not** ->

## What this changes for the program

- **The product surface + Frobenius correspondence the project chases exists in the
  literature, over the characteristic-1 base.** The square `N^x2-hat` (= Newton polygons
  in `Z x Z`, reduced to `Conv_>=(Z x Z)`) and the correspondences `Psi(lambda)` with
  group law `Psi(lambda lambda')` are concrete and computable. Direction 8 does not need
  to invent the product surface from scratch; it needs to put a signed intersection FORM
  with controlled signature on this square (or on a cohomology of it).
- **The missing object is sharply isolated: a signed pairing, not the surface.** The
  idempotency of the characteristic-1 operations is the obstruction to a signed
  intersection number. This is the exact form of the Direction-8 gap on the Connes-Consani
  square. It is the same content as the marginal-positivity thesis: positivity is the
  whole game.
- **`Gamma_S^2` has a concrete literature avatar: the diagonal `Id_eps` tangential deformation.**
  `Psi(lambda) o Psi(lambda^{-1}) = Id_eps` (Thm 7.7) is the literature object closest to
  2R's `Gamma_S^2 = ` von Mangoldt sum. The self-intersection is not a number here yet
  (no signed pairing), but the tangential deformation `Id_eps` is its analytic carrier.
  The prime/orbit data (`{log p}`, `-zeta'/zeta`) sits in the finite-place terms (§4.2)
  and in the `lambda lambda' in Q` composition regime.
- **`R*_+`-as-Frobenius is doubly attested.** Connes-Consani (site side, characteristic 1)
  and Leichtnam (flow side, III_{1/q}) both answer 2Q with the continuum `R*_+`. Treat a
  continuous Frobenius scaling, not a single `q`, as the settled local picture over
  `Spec(Z)`.
- **The complete `zeta_Q` is intrinsic.** Gamma-factor from point counting reinforces 2I
  and Deninger-I: the archimedean place is geometry, not an add-on.

## Actionable

- The Newton-polygon semiring (`Sub_>=(Z x Z)` / `Conv_>=(Z x Z)`, union/convex-hull +
  Minkowski sum) is a concrete, computable object. A project-native experiment could
  compute the `N^x x N^x` Frobenius action `Fr_{n,m} = diag(n,m)` on small Newton polygons
  and look for the `(1,p)` bidegree pattern 2Q predicts. This is the first Connes-Consani
  object directly amenable to the repo's numerical style.
- The diagonal self-composition `Psi(lambda) o Psi(lambda^{-1}) = Id_eps` (Thm 7.7) is the
  literature object closest to `Gamma_S^2` (2R). Worth a focused symbolic experiment on the
  `lambda lambda' in Q` (rational-product) deformation regime to see whether the `Id_eps`
  germ deformation carries a `log p` / prime-orbit spectrum, which would directly connect
  the Connes-Consani square to 2R's Ruelle dynamical zeta `-zeta'/zeta`.
- The exact gap to state for Direction 8: the square `(N^x2-hat, Conv_>=(Z x Z))` is
  multiplicatively cancellative (Prop 6.21) but its operations are idempotent (no
  subtraction). Constructing a signed intersection pairing with a Hodge-index signature on
  this square (or lifting to a Weil cohomology that has one) is the missing step. This is
  the Castelnuovo-positivity row of Connes' Weil dictionary (Connes-1998 §II) realized over
  characteristic 1.

## Status

Read deeply: pp.1-18 (intro, Thm 1.1, Thm 1.2; §2 points = rank-one ordered groups (Thm
2.1) + adelic interpretation Prop 2.5; §3 structure sheaf `Z_max`, stalks Thm 3.2, global
sections = B Prop 3.5, points over `R^max_+` Thm 3.8; §4 Hasse-Weil formula Thm 4.2,
counting distribution; §5 the `Spec(Z)` morphism) and pp.22-39 (§6 the square in full:
`Mod(B)`, the unreduced square `Z_min (x)_B Z_min = Sub_>=(Z x Z)` Prop 6.6, the action
`Fr_{n,m}` eq. 30, points Prop 6.11, the Frobenius correspondences `Psi(lambda)` Prop
6.12/6.13, the reduced square `Conv_>=(Z x Z)` Prop 6.19/6.21; §7 the composition law in
full: reduced correspondences, Prop 7.3/7.4, the tangential deformation Def 7.6, Theorem
7.7). §8 (the absolute point / matroids) read via the intro. Honest depth: the square
construction (§6), the points/adelic identification (§§1-3), the Hasse-Weil/Gamma-factor
(§4), and the composition law (§7, through Thm 7.7) are understood at the statement level
with the key proofs traced; the finest combinatorial lemmas in §7 (the germ-level
estimates establishing the tangential deformation) are summarized, not verified line by
line.
