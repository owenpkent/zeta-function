# Reading notes: Deninger, *Arithmetic Geometry and Analysis on Foliated Spaces* (Arizona Winter School lectures, 23 May 2005)

> Reference-library read-through ([`README.md`](README.md)). A lecture-series
> consolidation of the 1998 ICM ([`Deninger-1998-ICM-Analogies-Foliated.md`](Deninger-1998-ICM-Analogies-Foliated.md))
> and the 2002 Liege paper ([`Deninger-2002-NT-Dynamical-Foliated.md`](Deninger-2002-NT-Dynamical-Foliated.md)),
> "properly updated" (his words), prepared for the Southwestern Center for Arithmetic
> Algebraic Geometry at Arizona (invited by Minhyong Kim). For the project it is the
> single best one-stop statement of Deninger's program: the same conjectural
> cohomology `H^i_dyn("spec o bar", R)`, the same `Θ = 1/2 + A` RH argument, the same
> leafwise Hodge / ALK trace formula, plus the explicit `det_inf` derivation of EVERY
> Euler factor (finite, real `∞`, complex `∞`) from one regularized determinant, and
> the framing of the missing object inside "Arithmetic Topology" (the 3-manifold /
> knots-as-primes analogy). Pages refer to the PDF in
> `references/02_deninger_program/`. Read in full: pp.1-32 (the entire body, through
> the laminated-space working hypothesis). Companion notes: 1998, 2002, Deninger I/II,
> and [`Alvarez-Lopez-Kordyukov-Leichtnam-2017-Trace-Formula-Foliated-Flows.md`](Alvarez-Lopez-Kordyukov-Leichtnam-2017-Trace-Formula-Foliated-Flows.md).

## One-line takeaway

The mature, self-contained statement of Deninger's program for a general number field
`K`: a cohomology `H^i_dyn("spec o bar", R)` (with `"spec o bar" = spec o_K ∪ {p|∞}`
cast as the analogue of a projective curve over a finite field) whose `H^1`-spectrum is
the zeta zeros, with a Hodge `*` forcing `Θ = 1/2 + A` (RH), realized conjecturally by
reduced leafwise cohomology of a foliated flow. The genuinely consolidated piece is
**Proposition 3.1**: every Euler factor (finite `1 - Np^{-s}`, real `∞` the
`√2 π^{s/2} Γ(s/2)` factor, complex `∞` the `(2π)^s Γ(s)` factor) is one and the same
regularized determinant `det_inf((s-Θ)/2π | R_p)^{-1}` evaluated on a different `R_p`.
The honest Direction-8 obstruction is stated cleanly (p.19): the strong `*`-on-forms
condition (the conformal `α = 1` scaling) "I do not think will exist for dynamical
systems relevant for number fields ... one will need the Kahler identities on
cohomology."

## Technical content (section by section)

**Sect. 2 (pp.2-3): the analytic objects.** `ζ_K(s) = prod_p (1 - Np^{-s})^{-1}`,
archimedean factors `ζ_p(s) = 2^{-1/2} π^{-s/2} Γ(s/2)` (real) / `(2π)^{-s} Γ(s)`
(complex), completed `ζ_K-hat = ζ_K prod_{p|∞} ζ_p`, functional equation
`ζ_K-hat(1-s) = |d_K|^{s-1/2} ζ_K-hat(s)`. Hasse-Weil `ζ_X(s) =
prod_{x∈|X|}(1 - N(x)^{-s})^{-1}`. Target: Deligne's `Re = ν/2` for `X/F_p` (via
Lefschetz + Poincare duality), conjecturally extended to `X/Z`; Soule's order-of-
vanishing formula (1) in terms of motivic cohomology `H^i_M(X, Q(n)) = Gr^n_γ K_{2n-i}`.

**Sect. 3 (pp.3-13): the conjectural cohomological formalism.**
- **Regularized determinant.** Same as 1998: `det_inf(Θ|H) = prod_{α∈sp(Θ)} α =
  exp(-ζ_Θ'(0))`, `ζ_Θ(s) = Σ_{0≠α} α^{-s}` (`-π < arg α ≤ π`); example spectrum
  `{1,2,3,...}` gives `√(2π)`.
- **Proposition 3.1 (EVERY Euler factor as one `det_inf`), pp.5-7.** With `R_p` (`p∤∞`)
  the real finite Fourier series on `R/(log Np)Z`, `R_p = R[exp(-2y)]` (real `∞`),
  `R_p = R[exp(-y)]` (complex `∞`), and `Θ = d/dy`:
  `ζ_p(s) = det_inf((s-Θ)/2π | R_p)^{-1}` for all places `p`. **The explicit
  computations** (the substance this note adds over Deninger I): the Hurwitz/Lerch
  inputs `ζ(0,z) = 1/2 - z`, `∂_s ζ(0,z) = log((1/√2π) Γ(z))`, and
  `prod_{ν∈Z} γ(z+ν) = 1 - e^{-2πiz}` (Im γ > 0) / `1 - e^{2πiz}` (Im γ < 0) from
  `Γ(z)Γ(1-z) = π/sin πz`. Then:
  - finite `p`: `det_inf((s-Θ)/2π | R_p) = prod_{ν∈Z}(1/2π)(s - 2πiν/log Np) = 1 -
    exp(-2πi · s log Np / 2πi) = 1 - Np^{-s} = ζ_p(s)^{-1}`.
  - real `∞`: `det_inf((s-Θ)/2π | R[exp(-2y)]) = prod_{ν≥0}(1/2π)(s+2ν) =
    prod_{ν≥0}(1/π)(s/2 + ν) = π^{s/2 - 1/2}((1/√2π)Γ(s/2))^{-1} =
    (√2 π^{s/2} Γ(s/2))^{-1} = ζ_p(s)^{-1}`.
  - complex `∞`: `det_inf((s-Θ)/2πi | R[exp(-y)]) = prod_{ν≥0}(1/2π)(s+ν) =
    (2π)^{s-1/2}((1/√2π)Γ(s))^{-1} = ((2π)^s Γ(s))^{-1} = ζ_p(s)^{-1}`.
- **Formula (3) (the global conjecture).** `"spec o bar" = spec o ∪ {p|∞}` is analogous
  to a projective curve over `F_p` (with `ζ_X-hat(s,R) = prod_i det(1 - p^{-s} Fr_p^* |
  H^i_et(X-bar,R))^{(-1)^{i+1}}` the model). Conjecturally
  `ζ_K-hat(s) = prod_{i=0}^2 det_inf((s-Θ)/2π | H^i_dyn("spec o bar", R))^{(-1)^{i+1}}`,
  `H^0 = R` (`Θ=0`), `H^1` infinite-dim (`sp Θ =` non-trivial zeros with
  multiplicity), `H^2 ≅ R` (`Θ=id`), `H^i = 0` for `i > 2`; implies
  `ξ_K(s) = (s/2π)((s-1)/2π) ζ_K-hat(s) = prod_ρ (s-ρ)/2π` (true, [13],[44]). Trace iso
  `tr: H^2_dyn ≅ R(-1)`, cup pairing `H^i × H^{2-i} → H^2 ≅ R(-1)`, refined to
  `H^i(C)^{Θ~α} × H^{2-i}(C)^{Θ~1-α} → C` (Poincare duality ↔ functional equation).
- **The `Θ = 1/2 + A` RH argument (p.9).** Same as 1998: a Hodge `*: H^1_dyn ≅ H^1_dyn`
  with `(f,f') = tr(f ∪ *f')` positive definite, `Θ` a derivation commuting with `*`
  (since `λ^t = exp(tΘ) = (φ^t)^*`), forces from `f1 ∪ f2 = Θ(f1∪f2) = ...` that
  `(f1,f2) = (Θf1,f2) + (f1,Θf2)`, i.e. `Θ = 1/2 + A`, `A` skew, hence RH. Same
  Montgomery-Sarnak-Kontsevich remark (hermitian vs real-skew-symmetric spacing
  statistics agree). The completion of `H^1_dyn` under `(,)` is the Hilbert-Polya / Berry
  quantum-physical space.
- **Proposition 3.2 (the explicit formula) + distributional form (5).**
  `Φ(0) - Σ_ρ Φ(ρ) + Φ(1) = -log|d_{K/Q}| φ(0) + Σ_{p|∞... actually p∤∞} log Np
  (Σ_{k≥1} φ(k log Np) + Σ_{k≤-1} Np^k φ(k log Np)) + Σ_{p|∞} W_p(φ)`, with the `Γ`-factor
  distributions `W_p(φ) = ∫ φ(t)/(1 - e^{κ_p t}) dt` (`κ_p = -1` complex, `-2` real).
  Distributional form (6): `Σ_i (-1)^i Tr(φ^* | H^i_dyn("spec o bar", R)) =
  -log|d_{K/Q}| δ_0 + Σ_{p∤∞} log Np (Σ_{k≥1} δ_{k log Np} + Σ_{k≤-1} Np^k δ_{k log Np})
  + Σ_{p|∞} W_p`. The distributional trace `Σ_ρ e^{tρ}` converges as a distribution (not
  pointwise) since `Σ_ρ Φ(ρ)` converges per test function.
- **Hasse-Weil generalization (7)-(10) + Theorem 3.3 (Arakelov `*`-argument), pp.11-13.**
  `ζ_X(s) = prod_{i=0}^{2d} det_inf((s-Θ)/2π | H^i_dyn,c(X,R))^{(-1)^{i+1}}` (7);
  Poincare duality `H^i_dyn,c × H^{2d-i}_dyn → H^{2d}_dyn,c ≅ R(-d)` (8); Tate-conjecture
  analogue (9); explicit formula (10) `-(log A_X) δ_0 + Σ_x log N(x)(Σ_{k≥1} δ_{...} +
  Σ_{k≤-1} N(x)^k δ_{...})` (`A_X` the conductor). **Theorem 3.3:** on `F_p`-schemes a
  cohomology with linear flow exists satisfying (7),(8),(9 ↔ Tate), via `l`-adic
  cohomology; it does NOT generalize to `X/Z` flat. **The Arakelov `*`-condition
  (formula (11), p.13):** if `H^i_dyn("X bar", R)` existed on an Arakelov compactification
  with `ζ_X-hat = prod det_inf(...)`, then a Hodge `*: H^i → H^{2d-i}` with
  `φ^{t*} ∘ * = (e^t)^{d-i} * ∘ φ^{t*}`, i.e. `Θ ∘ * = * ∘ (d-i+Θ)`, would force
  `Θ - i/2` skew, hence RH. "On the level of forms equation (11) means the flow changes
  the metric defining the `*`-operator by the conformal factor `e^t`. **However,
  equation (11) for forms is a much stronger condition than for cohomology classes.**"
  Consani's refinement `H^i_ar` with a monodromy operator `N` (the bad-semistable-
  reduction-at-`∞` picture) is noted.

**Sect. 4 (pp.13-19): foliation cohomology, leafwise Hodge, Kahler/Lefschetz package.**
Reduced leafwise cohomology `H-bar^n(X,R) = ker d_F / closure(im d_F)`, nuclear Frechet,
infinite-dim `H-bar^1`; flow generator `Θ` an `R`-linear derivation (formula (12)).
- **Properties (13)-(19) for Riemannian foliations.** Leafwise Hodge iso (13)
  `ker Δ_F^n ≅ H-bar^n(X,R)` (Alvarez Lopez-Kordyukov [1], deep -- `Δ_F` only leafwise
  elliptic, fails for non-Riemannian `F`); Hodge `*_F` (14); trace `tr: H-bar^d → R`,
  `tr(h) = ∫_X *_F(H(h)) vol` (15); scalar product `(h,h') = tr(h ∪ *_F h')` (15);
  non-degenerate cup pairing (16); Kunneth (17) `H-bar^n_{F_X} ⊗-hat H-bar^m_{F_Y} ≅
  H-bar^{n+m}_{F_{X×Y}}`; Kahler-foliation `H^{pq}`-decomposition (18) `H-bar^n ⊗ C =
  ⊕_{p+q=n} H^{pq}`, `H^{pq} ≅ H-bar^q(X, Ω^p_F)`; hard-Lefschetz isos (19)
  `L_F^i: H-bar^{d-i} ≅ H-bar^{d+i}` and a polarizable ind-`R`-Hodge structure of weight
  `n` on `H-bar^n_prim`.
- **Theorem 4.1 (`Θ = α/2 + S`, the toy model).** `X` compact 3-manifold, `F`
  Riemannian surface foliation with dense leaf, `φ` `F`-compatible conformal on `TF`
  with factor `e^{αt}` (formula (20)). Then `Θ = 0` on `H-bar^0 = R`, `Θ = α` on
  `H-bar^2 ≅ R`, and `Θ = α/2 + S` (`S` skew) on `H-bar^1` (formula (21), proof as in
  2002). **Deninger's caution (p.19), the honest Direction-8 hurdle:** "The existence of
  a conformal metric for the flow simplifies the analysis. However, I do not think that
  such a metric will exist for dynamical systems relevant for number fields. In order to
  verify equation (11) for them one will need the Kahler identities on cohomology."

**Sect. 5 (pp.20-24): dynamical Lefschetz trace formulas.** Conjecture 5.1 (formula
(22)): the general foliated trace formula `Σ_n (-1)^n Tr(φ^*|H-bar^n) = Σ_γ l(γ)
Σ_{k≥1} ε_γ(k) δ_{kl(γ)} + Σ_x ε_x |1 - e^{κ_x t}|^{-1}` in `D'(R^{>0})`, unknown with
fixed points except `dim X = 1`; the analytic difficulty is `Δ_F` not transversally
elliptic to the `R`-action. Theorem 5.3 ([2], ALK 2002, formula (23)): for transversal
flows `A_φ = ∫ φ(t) φ^{t*} dt` is trace class, giving `χ_Co(F,μ) δ_0 + Σ_γ l(γ)
Σ_{k∈Z\0} ε_γ(k) δ_{kl(γ)}`. Theorem 5.4 (spectral form, Stone). **Corollary 5.5**
(formula (24)): the conditional `Re = α/2` for everywhere-transversal conformal flows on
3-manifolds (proof via `e^{-αt/2}φ^{t*}` orthogonal + Stone, or `-(Θ-α/2)^2 =
Δ^1|_{ker Δ^1_F}`); Remark 2 forces `α = 0`; Remark a (p.25): the imaginary parts `r`
of `ρ = α/2 + ir` have `r^2 ∈ sp(Δ^1)`, raising the question whether `Im(ρ)^2` for the
`ζ_K` zeros lie in the spectrum of a Laplace-Beltrami operator.

**Sect. 6 (pp.25-27): explicit-formula comparison, the same obstructions.** Formula (28)
(the `R^{>0}` distributional explicit formula for `ζ_K`) vs Corollary 5.5's (24): the
dictionary `spec o_K ∪ {p|∞}` ↔ 3-dim `(X, φ^t, F)`, finite `p` ↔ orbit `l(γ_p) =
log Np`, infinite `p` ↔ fixed point `κ_{x_p} = κ_p`, `H^i_dyn ↔ H-bar^i(X,R)`. Fact 6.1
(= Fact 4.2 of 2002): `χ_Co(F,μ) ≤ 0` matches `-log|d_{K/Q}| ≤ 0`; refined via Connes'
Riemann-Roch to the Arakelov Euler characteristic `χ_Ar(O_{spec o_K bar}) =
-log√|d_{K/Q}|` (formula (30)). The two mismatches restated: number theory needs `α = 1`
(the `e^t` scaling, formula (31)), impossible for manifolds (`α = 0`); and the `k ≤ -1`
coefficients are `±1` (manifold) vs `Np^k = e^{k log Np}` (number field).

**Sect. 7 (pp.27-32): laminated spaces / smooth solenoids.** Foliated spaces in the
sense of Moore-Schochet [33] (transition maps `(f_{ij}(x,y), g_{ij}(y))`, `D_x^α f`
continuous); generalized solenoids (locally `L_i × T_i`, `T_i` totally disconnected),
classical `S^1_p = R ×_Z Z_p`. **Warning (p.30):** a manifold with a smooth foliation is
also a foliated space, but the sheaves differ (manifold demands transverse smoothness,
foliated-space only continuity). Foliations of solenoids by laminated `L` with
`FL`-substructure; `H-bar^*(X, R_F)`. **Working hypothesis 7.5 (formula (32))** = the 2002
working hypothesis (26): for a compact smooth solenoid `X` with codimension-one `F` and
`F`-compatible `φ`, a `D'(R*)`-valued trace with closed-orbit (`δ_{kl(γ)}`, `k ≥ 1`:
`ε_γ(k)`; `k ≤ -1`: `ε_γ(|k|) det(-T_xφ^{kl(γ)}|T_xF)`) plus fixed-point terms `W_x`
(two-sided, formulas after (32)). Remark 7.6: Leichtnam [31] proved certain
fixed-point-free cases with `L^2`-transverse foliation cohomology; the uniform
coefficient formula (33), manifold case `|det(T_xφ^{kl}|T_xF)| = 1`, conformal case (4)
`= e^{kl(γ)}`, giving formula (35) which "fits perfectly with the explicit formula (6)
if all `ε_{γ_p}(k) = 1` and `ε_{x_p} = 1`" (then `e^{kl(γ_p)} = Np^k`, `W_{x_p} = W_p`).
The fixed-point structure `T_xφ^{kl} = e^{(k/2)l} O_k`, `O_k ∈ SO(T_xF)`.

## Points mapped to the project

1. **The whole program for a number field `K` in one statement (formula (3), p.7).**
   `ζ_K-hat(s) = prod_{i=0}^2 det_inf((s-Θ)/2π | H^i_dyn("spec o bar", R))^{(-1)^{i+1}}`,
   `H^0 = R`, `H^1` = zeros, `H^2 ≅ R`; implies `ξ_K(s) = prod_ρ (s-ρ)/2π`. Hasse-Weil
   (7) with Poincare duality (8) gets the same treatment.
   -> The Direction 4.6 target verbatim, generalized from `Q` to any `K`. The
   `"spec o bar" =` "projective curve over a finite field" framing is the exact
   function-field-lift posture: the proof should mimic Deligne/Weil with `det_inf`
   replacing the finite `det(1 - Frob)`.

2. **Every Euler factor as one regularized determinant (Proposition 3.1, pp.5-7).**
   `ζ_p(s) = det_inf((s-Θ)/2π | R_p)^{-1}` for ALL places, with the explicit finite
   `1 - Np^{-s}`, real `√2 π^{s/2} Γ(s/2)`, complex `(2π)^s Γ(s)` computations from
   Lerch/Hurwitz and `prod_{ν∈Z} γ(z+ν) = 1 - e^{±2πiz}`.
   -> This is the uniform "all places, one formalism" statement the Lean
   `ExplicitFormula` / `archKernel` rests on, made fully explicit for both real and
   complex archimedean places. It refines the Deninger I note: the Γ-factor (2I /
   `A_arch`) and the finite Euler factors are the same `det_inf` object on different
   `R_p`. Best citation for "the archimedean place is not special, it is the `p=∞`
   stationary point of the same flow."

3. **The `Θ = 1/2 + A` RH argument, restated (p.9).** Hodge `*` on `H^1_dyn`,
   `(f,f') = tr(f ∪ *f')` positive definite, `Θ` derivation commuting with `*`, forces
   `Θ = 1/2 + A`, `A` skew, hence RH; Hilbert-Polya space = completion of `H^1_dyn`.
   -> Direction 8, the harder half. RH = a Hodge-`*` positivity statement on `H^1`, not
   a consequence of the trace formula alone. Consistent across 1998/2002/2005: the
   `*`-operator is the load-bearing object, the marginal-positivity thesis in operator
   form.

4. **The full leafwise-Hodge package for Riemannian foliations (sect.4, (13)-(19)).**
   Hodge iso `ker Δ_F ≅ H-bar^n`; `*_F`; `tr`; non-degenerate cup pairing; Kunneth; and
   (Kahler) `H^{pq}` + hard-Lefschetz + polarizable ind-`R`-Hodge structure on
   primitive classes.
   -> The complete Direction 4.3 (finiteness/Hodge) + Direction 8 (Hodge/Lefschetz)
   toolkit. The hard-Lefschetz + polarization (19) is exactly the setting for a
   Direction-8 signature / Hodge-index theorem: a polarized Hodge structure is where a
   signature statement lives. The Kunneth (17) is the foliated analogue of the 2K
   product `Spec(Z) × Spec(Z)`.

5. **The Arakelov compactification and the stronger `*`-condition (Thm 3.3 + (11),
   p.13).** A Hodge `*` with `φ^{t*} ∘ * = (e^t)^{d-i} * ∘ φ^{t*}` (the flow scales the
   metric by `e^t`) would force `Θ - i/2` skew, hence RH -- but (11) for forms is much
   stronger than for cohomology classes.
   -> The cleanest statement of why the `α = 1` (factor `e^t`) flow is the crux and why
   it is hard: it is a condition on forms (the metric), not just on cohomology. Same
   `α=0`-vs-`α=1` obstruction as 2002, here tied to the Arakelov compactification (the
   2I archimedean-completion object). Deninger's caution (p.19, "will need the Kahler
   identities on cohomology") pins what a Direction-8 attempt must produce.

6. **Arithmetic topology: `"spec o bar"` is 3-dimensional, primes are knots (sect.1,
   sect.6).** The lectures connect to "Arithmetic Topology" (number theory ↔
   3-manifolds); `"spec o bar"` should be a 3-dim foliated space, closed orbits (primes)
   1-dimensional knots/links inside it, the `R`-action the missing archimedean Frobenius.
   -> Frames the missing object (2K) as a 3-manifold-like foliated space -- the same
   hole as `Spec(Z) × Spec(Z)`, viewed through the Mazur "primes = knots" dictionary.
   The Direction-8 surface and the Deninger 3-manifold are two cultural descriptions of
   one missing geometry; the intersection form (Direction 8) corresponds to linking /
   cup pairings in the 3-manifold picture.

## What this changes for the program

- **Best single citation for the whole Deninger program.** 1998 is the original, 2002
  carries the proved ALK theorem and the elliptic-curve proof of concept, 2005 is the
  polished, number-field-general, self-contained version. Cite it for: the `det_inf`
  Euler-factor uniformity (Prop 3.1, with explicit real AND complex archimedean
  factors), the `Θ = 1/2 + A` RH argument (p.9), and the full leafwise-Hodge package
  (sect.4).
- **The archimedean place is rigorously "just another `det_inf`."** Prop 3.1 derives
  both real and complex Γ-factors from the same formula as the finite factors. This
  nails the 2I / `A_arch` posture: the archimedean local height / Γ-factor is the `p=∞`
  stationary point of the same flow, not a bolt-on. Direct support for the Lean
  archimedean kernel.
- **Direction 8's natural home is the polarized Hodge structure on `H-bar^1_prim`.** The
  hard-Lefschetz + polarization (sect.4 (19)) is the setting for a Hodge-index /
  signature theorem. The honest obstruction (p.19): the strong `*`-on-forms condition
  (the `α=1` conformal scaling) is what is missing, and Deninger expects it needs Kahler
  identities, not a metric.
- **"Spec(Z) × Spec(Z)" and Deninger's 3-manifold are the same gap.** The
  arithmetic-topology framing says the missing surface (Direction 8) and the missing
  foliated 3-space (Direction 4) are one object in two languages. Keep both charts: the
  intersection form (surface) ↔ linking / cup pairing (3-manifold).

## Actionable

- Use Prop 3.1 (pp.5-7) as the citation whenever the program asserts "all Euler factors,
  finite and archimedean, are one `det_inf`." It has the explicit real and complex `∞`
  computations the Deninger I note only sketched.
- The stronger `*`-on-forms condition (11) plus Deninger's caution (p.19) is the precise
  specification of the Direction-8 hurdle. Pair with the 2002 `α=0` obstruction and the
  polarized-Hodge structure (19).
- The Remark a question (p.25) -- are `Im(ρ)^2` for the `ζ_K` zeros in the spectrum of a
  Laplace-Beltrami operator on 1-forms? -- is a concrete spectral probe worth flagging
  for any future Direction-1/4 cross-check.
- No new computation beyond 2R. The arithmetic-topology framing suggests a possible
  future cross-reference to the Mazur "primes = knots" literature if Direction 8 wants a
  linking-form model of the intersection pairing.

## Status

Read pp.1-32 of the lecture notes (the full body through the laminated-space working
hypothesis): sect.1 intro (and the "Arithmetic Topology" framing); sect.2 Dedekind /
Hasse-Weil zeta; sect.3 the cohomological formalism incl. Prop 3.1 (all Euler factors
as `det_inf`, with the explicit real and complex archimedean computations), the explicit
formula (Prop 3.2, distributional forms (5)/(6)), Theorem 3.3 and the Arakelov
`*`-condition (11); sect.4 foliation cohomology + leafwise Hodge + Kahler/Lefschetz
package (13)-(19) + Theorem 4.1 (and the p.19 caution that the conformal metric will
not exist for number fields); sect.5 the dynamical Lefschetz formulas (Conjecture 5.1,
Theorem 5.3 = ALK trace formula, Corollary 5.5 = `Re = α/2`); sect.6 the explicit-formula
comparison and the `α=0` / `±1`-vs-`Np^k` obstructions; sect.7 laminated spaces / smooth
solenoids and working hypothesis 7.5 (formula (32)/(35)). Recognized as a consolidation
of 1998+2002; depth focused on what is sharpest here (Prop 3.1's explicit archimedean
factors, the Arakelov `*`-condition, the p.19 Direction-8 caution, the
arithmetic-topology framing). The ALK trace-class theorem (Thm 5.3) and the leafwise
Hodge iso (13) read as cited black boxes, detailed in the ALK 2017 note.
