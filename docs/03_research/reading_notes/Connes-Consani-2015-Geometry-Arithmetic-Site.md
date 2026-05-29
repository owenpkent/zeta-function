# Reading notes: Connes-Consani, *Geometry of the Arithmetic Site* (arXiv:1502.05580, 2015)

> Entry in the reference-library read-through
> ([`references/README.md`](../../../references/README.md)). This is the paper most
> directly on the project's LIVE front: it constructs a geometric SQUARE of a site
> built from `Spec(Z)`, with a one-parameter semigroup of **Frobenius correspondences**
> on that square. That is exactly the missing object Direction 8 / 2K name (a product
> `Spec(Z) x Spec(Z)` with a Frobenius correspondence `Gamma_S`), realized here over
> the tropical/characteristic-1 base `R^max_+` instead of over a field. Mapped to 2K
> (the absolute base point), 2Q (the Frobenius correspondence), and the product-surface
> milestone. Pages refer to the PDF in `references/04_ncg_connes/`. Read: pp.1-8 (intro,
> Theorem 1.1, Theorem 1.2, the topos `N^x-hat` and its points = rank-one ordered
> groups, adelic interpretation Prop 2.5) and pp.22-25 (§6, the square `N^x2-hat` and
> the Frobenius correspondences). §§3-5, 7-8 skimmed via the intro.

## One-line takeaway

Connes-Consani build the **Arithmetic Site** `(N^x-hat, Z_max)`: a Grothendieck topos
(functors from the multiplicative monoid `N^x` to Sets) with a characteristic-1
(tropical) structure sheaf `Z_max = (Z u {-inf}, max, +)`, whose points over the
semifield `R^max_+` coincide exactly with Connes' adele class space quotient
`Z-hat^x \ A_Q / Q*`, and on which the action of `R*_+` reproduces the **Frobenius
flow**. Crucially (§6) they construct the **square** of the site as the topos
`N^x2-hat` with structure sheaf `Z_min (x)_B Z_min`, and exhibit a one-parameter
semigroup of **Frobenius correspondences** `Psi(lambda)`, `lambda in R*_+`, living as
sub-objects of that square, with composition law `Psi(lambda) o Psi(lambda') = Psi(lambda lambda')`.
This is a concrete `Spec(Z)`-flavoured product surface plus Frobenius correspondence,
the literal target of the project's Direction 8.

## The points that matter, mapped to the project

1. **The points of the site = Connes' adele class space (Theorem 1.1, Prop 2.5).** The
   points of `(N^x-hat, Z_max)` over `R^max_+` are the quotient `A_Q/Q*` by the maximal
   compact `Z-hat^x` of the idele class group, i.e. `Z-hat^x \ A_Q / Q*`; the Frobenius
   automorphisms `Fr_lambda` of `R^max_+` act as the idele class group action. The
   abstract points of `N^x-hat` are the rank-one ordered groups, i.e. non-trivial
   subgroups of `(Q, Q_+)`, with `H_a = {q in Q : aq in Z-hat}` (Prop 2.5).
   -> This is the **algebro-geometric realization of the Connes-1998 adelic space**
   (the space the K1 wall lives on). The project's 2K Morishita bridge links Deninger's
   foliated systems to exactly this Connes-Consani adelic space; this paper IS the
   algebraic-geometry half of that bridge. Closed points (primes) <-> periodic orbits
   of the Frobenius flow.

2. **Characteristic 1 / tropical base replaces `F_q` in the `q -> 1` limit (intro, §1.1).**
   The structure sheaf is the semifield of characteristic one `Z_max`; the role of the
   algebraic closure of `F_q` (as `q -> 1`) is played by the tropical semifield
   `R^max_+ = ([0,inf), x, max)` with Frobenius `Fr_lambda(x) = x^lambda`. The fixed
   points of all `Fr_lambda` form the Boolean semifield `B = {0,1}`, the only finite
   semifield (`Gal_B(R^max_+) = R*_+`).
   -> This is the project's "absolute base point" (2K) made concrete: the missing
   "field with one element" base is supplied by characteristic-1 / tropical geometry.
   The continuum of Frobenius scales `R*_+` (not a single `q`) is the same answer to
   2Q's open question "what plays the role of `q` over `Spec(Z)`" that Leichtnam's
   continuous Frobenius `R*_+` gives on the flow side. Two independent literatures
   converge on `R*_+`-as-Frobenius.

3. **The SQUARE of the site (§6): `N^x2-hat` with sheaf `Z_min (x)_B Z_min` = `Sub_>=(Z x Z)` (Prop 6.6).**
   The tensor square over the Boolean semifield `B` is identified with the `B`-module of
   hereditary subsets of `Z x Z` (finite unions of upper-right quadrants `I_(a,b) = {(x,y): x>=a, y>=b}`),
   i.e. **Newton polygons**. Addition is union; the reduced version uses convex hull and
   sum. Elements are `Sum q^{n_i} (x)_B q^{m_i}`, a semiring of characteristic 1
   (Prop 6.7). The points of the square coincide with the product of the points of the
   site (Prop 6.11).
   -> This is the **product surface** the project's Direction 8 is missing, built
   explicitly. It is not `Spec(Z) x_Z Spec(Z)` over a literal base, but the
   characteristic-1 tensor square of the site, whose elements are Newton polygons in
   `Z x Z`. The project's 2Q "(1,p) bidegree per prime" should be read against this:
   the bidegree lives naturally on a `Z x Z` square, exactly the index set here.

4. **The Frobenius correspondences `Psi(lambda)` and their composition (Theorem 1.2, eq. 27-30).**
   `Fr_{n,m}(Sum q^a (x) q^b) = Sum q^{na} (x) q^{mb}` is the action of `N^x x N^x` by
   endomorphisms of the square; geometrically `Fr_{n,m}` is the affine map `diag(n,m)`
   on the quadrant `Q = R_+ x R_+`, preserving `Q` and commuting with union and sum.
   The Frobenius correspondences `Psi(lambda)`, `lambda in R*_+`, are congruences on the
   square (sub-objects with rational slope `lambda`), defined for irrational `lambda` via
   best rational approximation, with composition `Psi(lambda) o Psi(lambda') = Psi(lambda lambda')`
   (and `= Id_eps o Psi(lambda lambda')`, a tangential deformation of the identity, when
   `lambda lambda'` becomes rational).
   -> This is a concrete, countable-combinatorial **`Gamma_S` (the Frobenius correspondence on the product)**.
   The project's 2R pins `Gamma_S^2` to the von Mangoldt prime sum / a Ruelle dynamical
   zeta. Here the composition law `Psi(lambda) o Psi(lambda') = Psi(lambda lambda')` is the
   group law of the Frobenius flow `R*_+` acting on the square. The self-intersection
   `Gamma_S^2` the project wants is the `lambda = lambda'` (diagonal) limit of this
   composition, where the tangential `Id_eps` deformation appears: that deformation
   term is the analytic shadow of the self-intersection / fixed-point contribution.

5. **The diagonal and the Hasse-Weil formula for the complete zeta (§4, Theorem 4.2/4.3).**
   Combining the counting `N(u)` of the Frobenius action on points over `R^max_+` with
   the `q -> 1` Hasse-Weil limit yields the **complete** Riemann zeta
   `zeta_Q(s) = pi^{-s/2} Gamma(s/2) zeta(s)` as the Hasse-Weil zeta of the site (so the
   archimedean Gamma-factor is included, not bolted on).
   -> The complete `zeta_Q` (Gamma-factor included) emerging from the site's own point
   count is the analogue of Deninger I deriving the Gamma-factor as a regularized
   product, and of the project's 2I archimedean block. The archimedean place is intrinsic
   here, consistent with the project's "cohomology that knows about archimedean primes."

6. **The absolute point and the structure morphism `Spec(Z) -> Arithmetic Site` (Figure 1, §5).**
   A geometric morphism of topoi `theta: Spec(Z) -> N_0^x-hat` is constructed (Theorem
   5.3), with the difference between `N^x-hat` and `N_0^x-hat` being a single adjoined
   **base point** (`N_0^x` adjoins a 0-element; §2.3, §8). §8 ties the topos `N^x-hat`
   to the structure of the (absolute) point in NCG, recasting Dixmier's matroid
   classification.
   -> The project's 2K names the gap as "the product surface / absolute base point."
   This paper is the most direct attack on that exact gap: it builds the base point
   (the adjoined 0), the morphism from `Spec(Z)`, and the square. What it does NOT build
   is a positive-definite intersection pairing on the square: the Newton-polygon
   semiring has union/convex-hull operations, not a signed cup product. So the project's
   2K reading "the bridge builds NO pairing" is exactly right for this paper too: the
   geometry and the Frobenius correspondences exist, the **signature / Hodge index
   (Direction 8) does not**.

## What this changes for the program

- **The product surface + Frobenius correspondence the project is chasing exists in the
  literature, over the characteristic-1 base.** The square `N^x2-hat` (= Newton polygons
  in `Z x Z`) and the correspondences `Psi(lambda)` with group law `Psi(lambda lambda')`
  are concrete. Direction 8 does not need to invent the product surface from scratch; it
  needs to put an intersection FORM with a controlled signature on this (or a cohomology
  of it).
- **The missing object is sharply isolated: a signed pairing, not the surface.** The
  characteristic-1 operations are idempotent (union, max, convex hull). There is no
  subtraction, hence no obvious signed intersection number, hence no Hodge index yet.
  This is the precise form of the Direction-8 gap on the Connes-Consani square, and it
  matches the project's marginal-positivity thesis (positivity is the whole content).
- **`R*_+`-as-Frobenius is now doubly attested.** Leichtnam (flow side, III_{1/q}) and
  Connes-Consani (site side, characteristic 1) both answer 2Q's "what is `q` over
  `Spec(Z)`" with the continuum `R*_+`. The project should treat a continuous Frobenius
  scaling, not a single `q`, as the settled local picture.
- **The complete `zeta_Q` is intrinsic (Gamma-factor from point counting).** Reinforces
  2I and the Deninger-I regularized Gamma-factor: the archimedean place is part of the
  geometry, not an add-on.

## Actionable

- The diagonal / self-composition `Psi(lambda) o Psi(lambda)` with its tangential
  `Id_eps` deformation (Theorem 1.2) is the literature object closest to the project's
  `Gamma_S^2 = ` von Mangoldt sum (2R). Worth a focused read of §7 (composition law) to
  see whether the `lambda lambda' in Q` deformation term carries a `log p` / prime-orbit
  spectrum, which would directly connect Connes-Consani's square to 2R's Ruelle
  dynamical zeta.
- The Newton-polygon semiring (`Sub_>=(Z x Z)`, convex hull + sum) is a concrete,
  computable object. A project-native experiment could compute the `N^x x N^x` Frobenius
  action `Fr_{n,m}` on small Newton polygons and look for the `(1,p)` bidegree pattern
  2Q predicts. This is the first Connes-Consali object that is directly amenable to the
  repo's numerical style.

## Status

Read pp.1-8 (intro, Thm 1.1, Thm 1.2, topos points = rank-one ordered groups, adelic
interpretation Prop 2.5) and pp.22-25 (§6: the square, `Z_min (x)_B Z_min = Sub_>=(Z x Z)`,
Newton polygons, Frobenius correspondences). §§3-5 (structure sheaf, stalks, Hasse-Weil
formula, `Spec(Z)` morphism) and §§7-8 (composition law, the absolute point) read via
the introduction, not line by line. Honest depth: the square construction (§6) and the
points/adelic identification (§§1-2) are understood; the §7 composition-law proof and
the §5 topos-morphism construction are summarized, not verified.
