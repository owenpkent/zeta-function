# Reading notes: Deninger, *Some Analogies Between Number Theory and Dynamical Systems on Foliated Spaces* (ICM 1998)

> Reference-library read-through ([`README.md`](README.md)). This is the
> founding manifesto of the whole "Direction 4 (foliation)" half of the program:
> the ICM address where Deninger first laid out, in one place, both (a) the
> conjectural infinite-dimensional cohomology `H^i("Spec Z bar", R)` whose `H^1`
> spectrum is the zeta zeros, and (b) the claim that the reduced leafwise
> cohomology of one-codimensional foliated dynamical systems has exactly the
> structural properties that cohomology should have. It is the source the
> Leichtnam 2006 and ALK 2017 notes both descend from, and the place where the
> Direction 4.6 (Lefschetz/`det`) and Direction 8 (Hodge-`*` signature) targets
> are stated as a single picture. Pages refer to the PDF in
> `references/02_deninger_program/`. Read: pp.1-13 (sect.1-3, the cohomological
> formalism and the RH `Θ = 1/2 + A` argument), pp.14-23 (sect.4-5, the foliated
> dynamical systems, Guillemin-Sternberg, and the arithmetic dictionary).

## One-line takeaway

The arithmetic side wants a cohomology `H^i("Spec Z bar", R)` with a flow whose
generator `Θ` has the zeta zeros as `H^1`-spectrum, a Poincare duality (functional
equation), and a Hodge `*`-operator forcing `Θ = 1/2 + A` with `A` skew-symmetric
(RH). The dynamical side delivers a literal model: the reduced leafwise cohomology
`H-bar^i_F(X)` of a one-codimensional foliated flow, with closed orbits of length
`log p` playing the primes and a Guillemin-Sternberg/Lefschetz trace formula
reproducing the explicit formula. The 1998 picture is the union of the Direction
4.6 target (trace formula / `det_∞`) and the Direction 8 target (the Hodge-`*`
signature), stated together for the first time.

## The points that matter, mapped to the project

1. **The arithmetic wishlist `H^i("Spec Z bar", R)` (sect.3, formula (3) p.6).** Deninger
   conjectures `zeta-hat(s) = prod_i det_∞((s-Θ)/2π | H^i)^{(-1)^{i+1}}` with
   `H^0 = R` (`Θ=0`), `H^1` infinite-dimensional with `Sp(Θ) =` the non-trivial
   zeros, `H^2 = R` (`Θ=id`), higher vanishing. This is the same object Deninger II
   builds rigorously and the Lean `det_ζ(s-Θ)` of Direction 4.6 abstracts.
   -> This is the Direction 4.6 regularized-determinant target stated at the global
   `Spec Z` level. Consistent with the Deninger I/II notes: I/II construct it locally
   and per-motive, 1998 is the global conjecture they specialize.

2. **The RH mechanism: Hodge-`*` forces `Θ = 1/2 + A`, `A` skew-symmetric (sect.3, p.7).**
   With a Hodge `*` on `H^1` giving a positive-definite scalar product
   `<f,f'> = tr(f ∪ *f')`, and `Θ` a derivation for `∪` commuting with `*`, the
   identity `<Θf1,f2> + <f1,Θf2> = <f1,f2>` forces `Θ = 1/2 + A` with `A`
   skew-symmetric. Hence `Sp(Θ) ⊂ {Re = 1/2}`: RH. He adds the Montgomery-Sarnak
   note (Kontsevich: hermitian and real-skew-symmetric spacing statistics agree).
   -> **This is the Direction 8 step, in its cleanest form.** RH does not come from
   the spectrum/`det` alone (that is Direction 4.6); it comes from a Hodge-`*`
   positivity/signature input on `H^1`. The note flags exactly the project's
   marginal-positivity thesis: the hard content is the `*`-operator (a signature
   statement), not the trace formula. 2R/Leichtnam reach the spectrum; this `Θ=1/2+A`
   is the separate, harder gap.

3. **Poincare duality = functional equation; cup product = the pairing (sect.3, (8); sect.2 conj.).**
   `∪: H^i × H^{2d-i} -> H^{2d} ≅ R(-d)` is to give the functional equation, and for
   an orthogonal weight-`w` motive the induced form on `H^1` at the center is
   symplectic, forcing the central order even and sign `+1`.
   -> The product/cup structure is load-bearing: the same `H^2 ≅ R(-1)` trace
   isomorphism and cup pairing that Direction 8's intersection form needs. The 2K
   "product surface" is the geometric object that would carry this `∪`. Note (5)
   `Ext^2(Q(0),Q(1)) -> R` is Deninger's `H^2`-trace, the arithmetic shadow of the
   intersection number.

4. **The explicit formula IS the Lefschetz trace formula (sect.3, Prop 3.2 p.5, (5)/(6)).**
   `Φ(0) - Σ_ρ Φ(ρ) + Φ(1) = Σ_p log p Σ_k φ(k log p) + ∫ φ/(1-e^{-2t})` is rewritten
   as `Σ_i (-1)^i Tr(φ^* | H^i)_dis = Σ_{p≤∞} Tr(σ | R_p)_dis`, with the finite-prime
   term `Tr(σ|R_p)_dis = log p Σ_k δ_{k log p}` (Poisson summation) and the archimedean
   term `<(1-e^{-2t})^{-1}>`.
   -> **This is 2R, stated by Deninger as the defining requirement.** 2R computed
   `-ζ'/ζ = Σ Λ(n) n^{-s}` as a dynamical-zeta log-derivative with orbit lengths
   `{log p}`; formula (5) is the distributional trace identity that 2R is a face of.
   The archimedean `(1-e^{-2t})^{-1}` term is the 2I/A_arch Γ-factor contribution as a
   stationary-point (`p=∞`) trace.

5. **The Guillemin-Sternberg fixed-point formula (sect.4, Prop 4.1 p.15) and its
   foliated reduction (formulas (19)-(22)).** For a flow `φ^t` on compact `X` with
   non-degenerate orbits, `Tr(ψ^* | Γ(X,E)) = Σ_γ l(γ) Σ_k Tr(ψ^{kl}_x|E_x) /
   |det(1 - T_xφ^{kl}|T_xX/T^0)| δ_{kl(γ)} + (fixed-point term)`. Passing to a
   one-codimensional foliation and the reduced leafwise cohomology `H-bar^i_F(X)`
   gives the conjectural `Σ_i (-1)^i Tr(φ^* | H-bar^i_F) = Σ_γ l(γ) Σ_k ε_γ(k) δ_{kl(γ)}
   + Σ_x ε_x <(1-e^{κ_x t})^{-1}>`, the geometric twin of (5).
   -> This is the precise theorem-shape the Direction 4.6 trace formula must take, and
   the one ALK 2017 actually proves (the closed-orbit `δ_{kl(γ)}` sum + a fixed-point
   `(1-e^{κt})^{-1}` term). The note's chain: GS (manifolds) -> foliated conjecture
   (here) -> ALK 2002 non-singular theorem -> ALK 2017 with fixed points.

6. **The arithmetic dictionary "Spec Z bar" <-> foliated dynamical system (sect.4-5, p.13).**
   Closed orbits `γ` with `l(γ) = log p` <-> primes; a stationary point `x_∞` with
   `κ_{x_∞} = -2` <-> the place `∞`; leaves two/`2 dim X`-dimensional; `"Spec Z bar"`
   should be 3-dimensional (matching the etale cohomological dimension and the
   arithmetic-topology "primes = knots" analogy). The period group must contain
   `log Q*_+`, and the type-III von Neumann / Connes scaling picture appears.
   -> This is the conceptual map under all of Direction 4. The "`Spec Z bar` is
   3-dimensional foliated by surfaces" is the same object 2K names as missing (the
   product surface / absolute base point); here it is described as a foliated
   dynamical system rather than an arithmetic surface, but it is the same hole.
   The `κ_{x_∞} = -2` archimedean weight is 2I's Γ-factor place again.

## What this changes for the program

- **The Direction 4.6 and Direction 8 targets are one picture, stated in 1998.** The
  trace formula / `det_∞` (4.6) and the Hodge-`*` signature giving RH (8) are not two
  unrelated milestones: they are the two halves of Deninger's single conjectural
  cohomology. 4.6 is "the spectrum exists and the trace formula holds"; 8 is "the `*`
  makes `Θ = 1/2 + A`." This note is the canonical citation for that split.
- **`Θ = 1/2 + A` is the marginal-positivity thesis in operator form.** RH is exactly
  the statement that the `*`-positivity is enough to pin `Re Θ = 1/2`. There is no
  slack: a single skew part `A` with the wrong structure breaks it. This matches the
  in-house finding that the proof must engage exact zeta structure (the `*`-operator),
  not soft positivity.
- **The GS -> foliated -> ALK lineage is now explicit.** The Guillemin-Sternberg
  formula (Prop 4.1) is the manifold prototype; (19)-(22) are the foliated conjecture;
  ALK 2002/2017 are the proofs. Direction 4.6 work should treat (22) as the exact
  target distribution and the ALK trace-class mechanism as the route.
- **The missing object is the same one 2K names.** Whether described as `"Spec Z bar"`
  (a 3-dim foliated dynamical system) or as `Spec(Z) x Spec(Z)` (an arithmetic
  surface), the hole is identical: a base over which the product/`∪`/duality lives.
  The two languages (Deninger foliation vs Direction-8 surface) are two coordinate
  charts on one gap.

## Actionable

- Use formula (5)/(22) as the precise statement of the Direction 4.6 target when
  writing any 4.6 attempt: closed-orbit sum `Σ_γ l(γ) Σ_k ε_γ(k) δ_{kl(γ)}` plus the
  archimedean stationary term `<(1-e^{-2t})^{-1}>`.
- The `Θ = 1/2 + A` argument (sect.3 p.7) is the cleanest Direction-8 statement to
  carry forward: the whole hard step is the existence and `Θ`-equivariance of the
  Hodge `*` on `H^1`. Worth pairing with Deninger II sect.6 (the `*`/signature) and the
  trace-side `sdim`/η-invariant noted in Deninger I.
- No new computation beyond 2R yet. Next reads (ALK 2017, then prismatic) are the
  analytic machinery for actually realizing the flow and its trace class.

## Status

Read pp.1-23 of 24 (the full mathematical body: sect.1 intro, sect.2 geometric
zeta/L, sect.3 the cohomological formalism incl. the `Θ=1/2+A` RH argument and the
explicit-formula-as-Lefschetz Prop 3.2, sect.4 the Guillemin-Sternberg formula and
its foliated reduction, sect.5 the arithmetic dictionary). References page skimmed.
The motivic-`L`-function functor details (sect.3, Thm 3.4) read but treated as
Deninger I/II material.
