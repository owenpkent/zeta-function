# Reading notes: Deninger, *Some Analogies Between Number Theory and Dynamical Systems on Foliated Spaces* (ICM 1998)

> Reference-library read-through ([`README.md`](README.md)). This is the founding
> manifesto of the entire "Direction 4 (foliation)" half of the program: the ICM
> address (Doc. Math. J. DMV, Extra Vol. ICM 1998, I, 163-186) where Deninger first
> laid out, in one place, both (a) the conjectural infinite-dimensional cohomology
> `H^i("Spec Z bar", R)` whose `H^1`-spectrum is the zeta zeros, and (b) the claim
> that the reduced leafwise cohomology of one-codimensional foliated dynamical
> systems has exactly the structural properties that cohomology should have. It is
> the source from which the Leichtnam 2006, ALK 2017, and Deninger 2002/2005 notes
> all descend, and the place where the Direction 4.6 (Lefschetz / `det_inf`) and
> Direction 8 (Hodge-`*` signature) targets are stated as a single picture. Pages
> refer to the PDF in `references/02_deninger_program/`. Read in full: pp.1-24 (the
> entire mathematical body plus the reference list). Companion notes:
> [`Deninger-2002-NT-Dynamical-Foliated.md`](Deninger-2002-NT-Dynamical-Foliated.md),
> [`Deninger-2005-Arithmetic-Geometry-Foliated.md`](Deninger-2005-Arithmetic-Geometry-Foliated.md),
> [`Deninger-I-regularized-determinants.md`](Deninger-I-regularized-determinants.md),
> [`Deninger-II-regularized-determinants.md`](Deninger-II-regularized-determinants.md),
> [`Alvarez-Lopez-Kordyukov-Leichtnam-2017-Trace-Formula-Foliated-Flows.md`](Alvarez-Lopez-Kordyukov-Leichtnam-2017-Trace-Formula-Foliated-Flows.md).

## One-line takeaway

The arithmetic side wants a cohomology `H^i("Spec Z bar", R)` carrying a flow whose
generator `Θ` has the zeta zeros as `H^1`-spectrum, a Poincare duality (functional
equation), and a Hodge `*`-operator forcing `Θ = 1/2 + A` with `A` skew-symmetric
(RH). The dynamical side delivers a literal model: the reduced leafwise cohomology
`H-bar^i_F(X)` of a one-codimensional foliated flow, with closed orbits of length
`log p` playing the primes, a stationary point playing the archimedean place, and a
Guillemin-Sternberg / Lefschetz trace formula reproducing the explicit formula. The
1998 picture is the union of the Direction 4.6 target (trace formula / `det_inf`) and
the Direction 8 target (the Hodge-`*` signature), stated together for the first time.

## Technical content (section by section)

**Sect. 1-2 (pp.1-5): the analytic objects to be lifted.** `ζ(s) = prod_p (1-p^{-s})^{-1}`,
with the archimedean Euler factor `ζ_∞(s) = 2^{-1/2} π^{-s/2} Γ(s/2)` and the completed
`ζ-hat(s) = ζ(s) ζ_∞(s)`, holomorphic on `C \ {0,1}` with simple poles at `0,1` and
functional equation `ζ-hat(1-s) = ζ-hat(s)`. The Hasse-Weil zeta `ζ_X(s) =
prod_{x∈|X|}(1 - N(x)^{-s})^{-1}` for `X/Z` generalizes it. The target motivation is
explicit: for proper regular `X/F_p`, Deligne proved the zeros (resp. poles) of
`ζ_X-hat` have `Re = ν/2` for odd (resp. even) `ν`, via the Lefschetz trace formula
and Poincare duality for `l`-adic cohomology, and "one may expect the same" for
arbitrary `X/Z`. Soule's conjecture (formula (1)) on `ord_{s=d-n} ζ_X` in terms of
`Gr^n_γ K_{2n-i}(X) ⊗ Q` and the motivic conjectures (Conjectures 2.1: meromorphic
continuation + functional equation `L-hat(M,s) = ε(M,s) L-hat(M*, 1-s)`; Artin; Riemann
`Re = (w+1)/2`; Deligne-Beilinson-Scholl `ord_{s=0}`) are the wishlist the cohomology
must explain.

**Sect. 3 (pp.5-12): the conjectural cohomological formalism.** The regularized
determinant: for `Θ` on `H` a countable sum of finite-dim `Θ`-invariant `H_α`,
`det_inf(Θ|H) := prod_{α∈sp(Θ)} α := exp(-ζ_Θ'(0))` where `ζ_Θ(s) = Σ_{0≠α} α^{-s}`
(branch `-π < arg α ≤ π`), zero if `0 ∈ sp(Θ)`. Worked example: spectrum `{1,2,3,...}`
with multiplicity one gives `det_inf = √(2π)` since `ζ'(0) = -log√(2π)`.
- **Proposition 3.1 (every local Euler factor is one `det_inf`).** Let `R_p` (`p ≠ ∞`)
  be the real finite Fourier series on `R/(log p)Z`, and `R_∞ = R[exp(-2y)]`, each
  with `R`-action `(σ^t f)(y) = f(y+t)` and generator `Θ = d/dy`. Then
  `ζ_p(s) = det_inf((s-Θ)/2π | R_p)^{-1}` for all `p ≤ ∞`. Proof via Lerch's formula
  for the Hurwitz zeta derivative at `0`.
- **Formula (3) (the global conjecture).** `"Spec Z bar" = Spec Z ∪ {∞}` is to behave
  like a projective curve over a finite field, so
  `ζ-hat(s) = prod_{i=0}^2 det_inf((s-Θ)/2π | H^i("Spec Z bar", R))^{(-1)^{i+1}}`,
  with `H^0 = R` (`Θ = 0`), `H^1` infinite-dimensional with `sp(Θ) =` the non-trivial
  zeros (with multiplicity), `H^2 ≅ R` (`Θ = id`), `H^i = 0` for `i > 2`. This yields
  `ξ(s) = (s/2π)((s-1)/2π) ζ-hat(s) = prod_ρ (s-ρ)/2π` (which "turned out to be true,"
  ref. [D2],[SchS]). Trace iso `tr: H^2 → R(-1)` and cup product `∪: H^i × H^{2-i} →
  H^2 ≅ R(-1)`, refining to `H^i(C)^{Θ~α} × H^{2-i}(C)^{Θ~1-α} → C` (Poincare duality
  compatible with the functional equation; `Θ~α` = generalized `α`-eigenspace).
- **The RH mechanism `Θ = 1/2 + A` (p.7).** Assume (as for compact Riemann surfaces) a
  Hodge `*: H^1 → H^1` giving a positive-definite scalar product `<f,f'> = tr(f ∪ *f')`,
  and that the flow `λ^t = exp(tΘ) = (φ^t)^*` makes `Θ` a derivation for `∪` commuting
  with `*`. From `Θ(f1 ∪ f2) = Θf1 ∪ f2 + f1 ∪ Θf2` (the `H^2`-weight being `1`, hence
  `tr ∘ Θ = tr`) one gets `<f1,f2> = <Θf1,f2> + <f1,Θf2>`, forcing `Θ = 1/2 + A` with
  `A` skew-symmetric. Hence `sp(Θ) ⊂ {Re = 1/2}`: RH. Deninger adds the
  Montgomery-Sarnak remark: the zero-spacing statistics match random matrices, and
  (Kontsevich) the hermitian and real-skew-symmetric spacing statistics agree, fitting
  a skew `A`. The completion of `H^1` under `<,>` is "the space Hilbert was looking
  for, and that Berry suggested to realize in a quantum physical setting."
- **Proposition 3.2 = the explicit formula as a Lefschetz trace (p.8).** For
  `φ ∈ D(R^+)`, `Φ(s) = ∫ φ(t) e^{ts} dt`, the explicit formula reads
  `Φ(0) - Σ_ρ Φ(ρ) + Φ(1) = Σ_p log p Σ_{k≥1} φ(k log p) + ∫_0^∞ φ(t)/(1-e^{-2t}) dt`.
  With a distributional trace `Tr(λ|H)_dis = Σ_n Tr(λ|H_n)_dis = Σ_{α∈sp(Θ)} <e^{tα}>`,
  this becomes (formula (5)):
  `Σ_i (-1)^i Tr(φ^* | H^i("Spec Z bar", R))_dis = Σ_p log p Σ_{k≥1} δ_{k log p} +
  <(1-e^{-2t})^{-1}>`,
  where Poisson summation gives `Tr(σ | R_p)_dis = log p Σ_k δ_{k log p}` (finite `p`)
  and a direct calculation gives `Tr(σ | R_∞)_dis = <(1-e^{-2t})^{-1}>` (the
  archimedean term). Formula (6) rewrites this as a sheaf-theoretic Lefschetz formula
  `Σ_i (-1)^i Tr(φ^* | H^i)_dis = Σ_{p≤∞} Tr(φ^* | R_p)_dis`.
- **Hasse-Weil + motivic generalization (pp.9-12).** `ζ_X(s) = prod_{i=0}^{2d}
  det_inf((s-Θ)/2π | H^i_c("X", R))^{(-1)^{i+1}}` (formula (7)); Poincare duality (8)
  `H^i_c × H^{2d-i} → H^{2d}_c ≅ R(-d)`; the order-of-vanishing and Tate-conjecture
  consequences (9). **Theorem 3.3:** on `F_p`-schemes such a cohomology with linear
  flow exists (the `l`-adic construction), satisfying (7),(8), with (9) reducing to the
  Tate conjecture; it does NOT generalize to `X/Z` flat. **The Arakelov `*`-argument
  (p.11):** if `H^i("X bar", R)` existed on an Arakelov compactification with
  `ζ_X-hat = prod det_inf(...)`, a Hodge `*: H^i → H^{2d-i}` with
  `φ^{t*} ∘ * = (e^t)^{d-i} * ∘ φ^{t*}`, i.e. `Θ ∘ * = * ∘ (d-i+Θ)` (the flow scales
  the metric by `e^t`), would force `Θ - i/2` skew, hence the Riemann hypotheses. The
  last equation "means the flow changes the metric defining the `*`-operator by the
  conformal factor `e^t`" -- the crux `α=1` condition (see 2002/2005 notes).
  **Theorem 3.4:** a functor `F_p` from motives to flow-spaces with `L_p(M,s) =
  det_inf((s-Θ)/2π | F_p(M))^{-1}`, with `F_p(M) ⊗ F_p(M') → F_p(M⊗M')` and a real
  structure / perfect pairing at `p = ∞` (`Ext^1_{MH_R}(R(0), M_B*(1))`). The integral
  motives `M_Z` (integral at all `p ≤ ∞`) carry `tr: H^2(R(1)) → R`, and orthogonal
  motives of weight `w` give a symplectic form on `H^1(F(M))^{Θ~(w+1)/2}`, forcing even
  central order and sign `+1`.

**Sect. 4 (pp.12-18): dynamical systems on foliated spaces -- the model.**
- **Proposition 4.1 (Guillemin-Sternberg fixed-point formula).** For a smooth flow
  `φ^t` on compact `X` with non-degenerate compact orbits (a fixed point `x` has
  `T_x φ^t` without eigenvalue `1`; on a length-`l(γ)` periodic orbit, `T_x φ^{kl(γ)}`
  has eigenvalue `1` only along the flow direction `Y_φ`), and a bundle `E` with action
  `ψ^t: φ^{t*}E → E` opposite to `φ`, the distributional trace `Tr(ψ^*|Γ(X,E)) =
  π_* Δ^* K_{ψ^*}` (Schwartz kernel pulled back along the diagonal; the wave-front /
  transversality conditions make this defined) equals
  `Σ_γ l(γ) Σ_{k≥1} Tr(ψ_x^{kl(γ)} | E_x) / |det(1 - T_x φ^{kl(γ)} | T_x X / T_x^0)|
  δ_{kl(γ)} + Σ_x <Tr(ψ_x^t|E_x) / |det(1 - T_x φ^t | T_x X)|>` (`γ` periodic orbits,
  `x` stationary points).
- **Foliated reduction (formulas (19)-(22)).** Assume `X` carries a codimension-one
  foliation with leaf-tangent bundle `T_0 ⊂ TX`, `Tφ^t(T_0) = T_0`, with the
  transversal open set `U` (`T_0 ⊕ T_x^0 = T_x X`) containing all periodic orbits; at a
  fixed point `T_x φ^t` acts on `T_x X / T_{0x}` by `e^{κ_x t}`. Set
  `ε_γ(k) = sgn det(1 - T_x φ^{kl(γ)} | T_0)`, `ε_x = sgn det(1 - T_x φ^t | T_x X)`.
  Applying 4.1 to `Λ^i T_0^* ⊗ E` and the flat leafwise connection `δ_0` (fine
  resolution of the sheaf `F = ker(δ_0: E → T_0^* ⊗ E)` of leafwise-locally-constant
  sections; `F = R` for `E = X × R`), and replacing cohomology by the reduced leafwise
  cohomology `H-bar^i(X, F)` (the maximal Hausdorff quotient of `H^i(X,F)`, since
  `im δ_0` need not be closed), gives the conjectural dynamical Lefschetz formula (20):
  `Σ_i (-1)^i Tr(ψ^* | H-bar^i(X,F)) = Σ_γ l(γ) Σ_{k≥1} ε_γ(k) Tr(ψ_x^{kl(γ)}|E_x)
  δ_{kl(γ)} + Σ_x ε_x <Tr(ψ_x^t|E_x) / (1 - e^{κ_x t})>`, and for `E = X × R` the trivial
  bundle (formula (21)/(22)):
  `Σ_i (-1)^i Tr(ψ^* | H-bar^i(X,R)) = Σ_γ l(γ) Σ_{k≥1} ε_γ(k) δ_{kl(γ)} +
  Σ_x ε_x <(1 - e^{κ_x t})^{-1}>`.
  Deninger flags the analytic difficulty (the trace on the infinite-dimensional
  `H-bar^i` is not defined in general; for suspensions and Riemannian foliations
  something can be done via the Alvarez Lopez-Kordyukov Hodge theorem). The "geometric
  point" stalk `F_γ-bar = Γ(R/l(γ)Z, γ-bar^{-1}F)` with Poisson summation gives the
  closed-orbit `δ_{kl(γ)}` sum; the stationary `Tr(ψ^*|F_x)_dis = <(1-e^{κ_x t})^{-1}>`.
  Note (22) resp. (21) "resembles the cohomological version of the explicit formulas
  (5) resp. (10)," but compact manifolds are too restrictive (the obstruction is made
  precise in the 2002 note: manifolds force `α = 0`, forbid fixed points).

**Sect. 5 (pp.18-24): the arithmetic dictionary and what the missing space must be.**
- The searched-for `("Spec Z bar", φ^t)` should be infinite-dimensional with a
  Grothendieck topology and some compactness; closed orbits `γ` with `l(γ) = log p`
  are the primes, a stationary point `x_∞` with `κ_{x_∞} = -2` is the place `∞`, all
  with positive sign. There are codimension-one foliations on `"Spec Z bar"` and on
  `"X"`; the conjectured cohomologies are the dense smooth subspaces of the reduced
  leafwise cohomologies. **Dimension count:** leaves are two-dimensional (resp.
  `2 dim X`), so `"Spec Z bar"` is three-dimensional (resp. `dim X + 1`), matching the
  etale cohomological dimensions and the "primes = knots" arithmetic-topology picture.
- **`F`-systems and the local-system formalism (pp.20-23).** An `F`-system is an
  `F`-flow with codimension-one foliation `T_0` everywhere transversal, no fixed
  points; the length homomorphism `l: π_1^{ab}(U) → R`, `l(c) = ∫_c ω_φ`, has image the
  period group `Λ = log Q*_+` for `"Spec Z bar"`. Vector bundles with flat
  `T_0`-connection `δ_0` and opposite action `ψ` ↔ locally free `R`-modules with action
  ↔ local systems `F`; the twist `F(α)` has action `e^{-tα}`, and `Λ ⊂ log Q*_+` iff
  there is a local system `R(1)` with `R(1) = Q(1) ⊗ R`. The exact sequence
  `0 → H^{i-1}(U,F)/Im Θ → H^i(U,F) → H^i(U,F)^{Θ=0} → 0` mirrors the `l`-adic
  `0 → H^{i-1}(V-bar)_{Fr_q} → H^i(V,F) → H^i(V-bar)^{Fr_q} → 0`: arithmetic vs
  geometric cohomology. Complete `F`-systems are suspensions `M ×_Λ R`.
- **The idelic shape and the functorial sheaf `F(M)` (pp.23-24).** With multiplicative
  time, `"Spec Z bar" ≅ M ×_{Q*_+} R*_+` (idelic flavor); `M = lim M-bar` from a space
  with commuting operators for every prime. The motivic explicit formula (18) holds in
  cohomological form, with `Tr(Fr_p^k | M_l^{I_p})` finite-prime terms and an
  archimedean `<Tr(e^{Nt} | Gr_V M_B)/(1-e^{-2t})>` term. A functor `M ↦ F(M)` (from
  `R^i π_* R_X` / `R^i π_* R-bar_X`) gives sheaves with `Q`-structure
  `F_Q(Q(1)) = R(1)`. **Conclusion:** the program "requires a cohomology theory for
  algebraic schemes over the integers with properties similar to those of the reduced
  leafwise cohomology of a class of dynamical systems with one-codimensional foliations
  by pro-manifolds."

## Points mapped to the project

1. **The arithmetic wishlist `H^i("Spec Z bar", R)` (formula (3), p.7).** `H^0 = R`,
   `H^1` infinite-dim with `sp(Θ) =` non-trivial zeros, `H^2 ≅ R`, higher vanishing,
   producing `ξ(s) = prod_ρ (s-ρ)/2π`. The same object Deninger II builds rigorously
   per-motive and the Lean `det_ζ(s-Θ)` of Direction 4.6 abstracts.
   -> This is the Direction 4.6 regularized-determinant target stated at the global
   `Spec Z` level; consistent with Deninger I/II (which construct it locally and
   per-motive, of which 1998 is the global specialization).

2. **The RH mechanism: Hodge-`*` forces `Θ = 1/2 + A`, `A` skew (p.7).** The positive
   scalar product `<f,f'> = tr(f ∪ *f')` plus `Θ`-derivation + `*`-commutation gives
   `<f1,f2> = <Θf1,f2> + <f1,Θf2>`, hence `Θ = 1/2 + A` skew, hence `sp(Θ) ⊂ {Re=1/2}`.
   -> This is the Direction 8 step in its cleanest form. RH does not come from the
   spectrum / `det_inf` alone (that is 4.6); it comes from a Hodge-`*` positivity /
   signature input on `H^1`. This IS the project's marginal-positivity thesis in
   operator form: the hard content is the `*`-operator (a signature statement). 2R /
   Leichtnam reach the spectrum; `Θ = 1/2 + A` is the separate, harder gap (Direction 8).

3. **Poincare duality = functional equation; cup product = the pairing (formula (8);
   orthogonal-motive symplectic form, p.12).** `∪: H^i × H^{2d-i} → H^{2d} ≅ R(-d)`
   gives the functional equation; for an orthogonal weight-`w` motive the induced form
   on the central `H^1` is symplectic, forcing even central order and sign `+1`.
   -> The cup / trace structure is load-bearing: the same `H^2 ≅ R(-1)` trace iso and
   pairing Direction 8's intersection form needs. The 2K product surface
   `Spec(Z) × Spec(Z)` is the geometric object that would carry this `∪`; `tr:
   Ext^2(Q(0),Q(1)) → R` is the arithmetic shadow of the intersection number.

4. **The explicit formula IS the Lefschetz trace formula (Prop 3.2, formula (5)).**
   `Σ_i (-1)^i Tr(φ^* | H^i)_dis = Σ_p log p Σ_k δ_{k log p} + <(1-e^{-2t})^{-1}>`,
   with the finite-prime term from Poisson summation on `R_p` and the archimedean term
   `<(1-e^{-2t})^{-1}>` from `R_∞ = R[exp(-2y)]`.
   -> This is 2R, stated by Deninger as the defining requirement. 2R computed
   `-ζ'/ζ = Σ Λ(n) n^{-s}` as a dynamical-zeta log-derivative with orbit lengths
   `{log p}`; (5) is the distributional trace identity 2R is a face of. The archimedean
   `(1-e^{-2t})^{-1}` term is the 2I / `A_arch` Γ-factor contribution as a
   stationary-point (`p = ∞`, weight `κ = -2`) trace.

5. **Guillemin-Sternberg (Prop 4.1) and its foliated reduction (formulas (19)-(22)).**
   The manifold prototype `Σ_γ l(γ) Σ_k Tr(ψ^{kl}|E)/|det(1 - T_xφ^{kl}|TX/T^0)|
   δ_{kl(γ)} + (fixed-point term)`, reduced via the leafwise complex to
   `Σ_i (-1)^i Tr(ψ^* | H-bar^i_F) = Σ_γ l(γ) Σ_k ε_γ(k) δ_{kl(γ)} +
   Σ_x ε_x <(1-e^{κ_x t})^{-1}>`.
   -> This is the precise theorem-shape the Direction 4.6 trace formula must take, and
   the one ALK 2017 actually proves (closed-orbit `δ_{kl(γ)}` sum + fixed-point
   `(1-e^{κt})^{-1}` term). The lineage is explicit: GS (manifolds, Prop 4.1) →
   foliated conjecture (here, (22)) → ALK 2002 non-singular theorem → ALK 2017 with
   fixed points.

6. **The arithmetic dictionary "Spec Z bar" ↔ foliated dynamical system (sect.4-5).**
   Closed orbits `l(γ) = log p` ↔ primes; stationary point `κ_{x_∞} = -2` ↔ place `∞`;
   leaves two-dimensional; `"Spec Z bar"` three-dimensional (matching etale dimension
   and "primes = knots"); period group `⊃ log Q*_+`; idelic shape
   `M ×_{Q*_+} R*_+`; the type-III / Connes-scaling picture appears.
   -> The conceptual map under all of Direction 4. "`Spec Z bar` is 3-dimensional
   foliated by surfaces" is the same object 2K names as missing (the product surface /
   absolute base point), described as a foliated dynamical system rather than an
   arithmetic surface. The `κ_{x_∞} = -2` archimedean weight is 2I's Γ-factor place
   again.

7. **The motivic functor and orthogonal-motive sign (Thm 3.4, p.12).** `F_p` from
   motives to flow-spaces with `L_p(M,s) = det_inf(...)^{-1}`, exact on `M_Z`, with a
   real structure / perfect pairing at `∞`; orthogonal `M` ⇒ symplectic central form ⇒
   sign `+1`.
   -> This is the per-motive refinement that Deninger I/II carry out rigorously; the
   `ε`-factor and regularized super-dimension (`sdim` / η-invariant noted in Deninger I)
   are the trace-side signature data. The orthogonal-motive sign result is the
   Davenport-Heilbronn-adjacent fact: it is an Euler-product / functional-equation
   structure statement, the kind of input the D-H detector tests.

## What this changes for the program

- **Direction 4.6 and Direction 8 are one picture, stated in 1998.** The trace formula
  / `det_inf` (4.6) and the Hodge-`*` signature giving RH (8) are not two unrelated
  milestones: they are the two halves of Deninger's single conjectural cohomology. 4.6
  is "the spectrum exists and the trace formula (5) holds"; 8 is "the `*` makes
  `Θ = 1/2 + A`." This note is the canonical citation for that split.
- **`Θ = 1/2 + A` is the marginal-positivity thesis in operator form.** RH is exactly
  the statement that the `*`-positivity is enough to pin `Re Θ = 1/2`. There is no
  slack: a skew part `A` with the wrong structure breaks it. This matches the in-house
  finding that any proof must engage exact zeta structure (the `*`-operator), not soft
  positivity.
- **The GS → foliated → ALK lineage is explicit.** Prop 4.1 is the manifold prototype;
  (19)-(22) the foliated conjecture; ALK 2002/2017 the proofs. Direction 4.6 work
  should treat (22) as the exact target distribution and the ALK trace-class mechanism
  as the route.
- **The missing object is the same one 2K names.** Whether described as `"Spec Z bar"`
  (a 3-dim foliated dynamical system / idelic `M ×_{Q*_+} R*_+`) or as
  `Spec(Z) × Spec(Z)` (an arithmetic surface), the hole is identical: a base over which
  the product / `∪` / duality lives. The two languages are two coordinate charts on one
  gap.

## Actionable

- Use formula (5) / (22) as the precise Direction-4.6 target when writing any 4.6
  attempt: closed-orbit sum `Σ_γ l(γ) Σ_k ε_γ(k) δ_{kl(γ)}` plus the archimedean
  stationary term `<(1-e^{-2t})^{-1}>` (weight `κ_{x_∞} = -2`).
- The `Θ = 1/2 + A` argument (p.7) is the cleanest Direction-8 statement to carry
  forward: the entire hard step is the existence and `Θ`-equivariance of the Hodge `*`
  on `H^1`. Pair with Deninger II sect.6 (the `*` / signature) and the trace-side
  `sdim` / η-invariant noted in Deninger I.
- No new computation beyond 2R. The chain is: 2R = the orbit-length spectrum and the
  von Mangoldt side of (5); the archimedean term of (5) = 2I; `Θ = 1/2 + A` = the
  Direction-8 target not yet realized.

## Status

Read pp.1-24 of 24 (the full mathematical body plus references): sect.1 intro and the
target (Deligne `Re = ν/2`, Soule, motivic conjectures 2.1); sect.2 geometric
zeta/L-functions; sect.3 the regularized-determinant formalism (Prop 3.1 all local
factors as `det_inf`, formula (3) the global conjecture, the `Θ = 1/2 + A` RH argument
p.7, Prop 3.2 the explicit-formula-as-Lefschetz formula (5), Thm 3.3 the `F_p`-scheme
realization, the Arakelov `*`-argument p.11, Thm 3.4 the motivic functor); sect.4 the
Guillemin-Sternberg formula (Prop 4.1) and its foliated reduction (19)-(22); sect.5 the
arithmetic dictionary, `F`-systems / local-system formalism, the idelic shape, and the
conclusion. Honest depth: the motivic-functor construction (Thm 3.4) and the `l`-adic
realization (Thm 3.3) are read as Deninger I/II / Deligne material; the leafwise-Hodge
and trace-class analysis behind (22) is read as the cited ALK material (detailed in the
2002 and 2017 notes).
