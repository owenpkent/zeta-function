# Reading notes: Deninger, *Arithmetic Geometry and Analysis on Foliated Spaces* (Arizona Winter School lectures, May 2005)

> Reference-library read-through ([`README.md`](README.md)). A lecture-series
> consolidation of the 1998 ICM ([`Deninger-1998-ICM-Analogies-Foliated.md`](Deninger-1998-ICM-Analogies-Foliated.md))
> and the 2002 Liege paper ([`Deninger-2002-NT-Dynamical-Foliated.md`](Deninger-2002-NT-Dynamical-Foliated.md)),
> "properly updated" (his words). For the project it is the single best one-stop
> statement of Deninger's program: the same conjectural cohomology
> `H^i_dyn("Spec o bar", R)`, the same `Θ = 1/2 + A` RH argument, the same leafwise
> Hodge / ALK trace formula, plus the explicit link to "arithmetic topology"
> (the 3-manifold / knots-as-primes analogy). It adds little new math beyond
> 1998+2002 but is the cleanest reference to cite. Pages refer to the PDF in
> `references/02_deninger_program/`. Read: pp.1-13 (sect.1-3, the cohomological
> formalism for Dedekind/Hasse-Weil zeta and the `Θ=1/2+A` argument), pp.14-22
> (sect.4-5, foliation cohomology, leafwise Hodge, the dynamical Lefschetz formulas).

## One-line takeaway

The mature, self-contained statement of Deninger's program. Same target as 1998/2002:
a cohomology `H^i_dyn("Spec o bar", R)` (now phrased for a general number field `K`,
with `"Spec o bar" = Spec o_K ∪ {p|∞}` cast as the analogue of a projective curve over
a finite field) whose `H^1`-spectrum is the zeta zeros, with a Hodge `*` forcing
`Θ = 1/2 + A` (RH), realized conjecturally by reduced leafwise cohomology of a foliated
flow. The genuinely consolidated piece is the explicit `det_∞` derivation of every
Euler factor (finite primes `1 - Np^{-s}`, real `∞` the `Γ(s/2)` factor, complex `∞`
the `Γ(s)` factor) from the same regularized-determinant formula, and the framing of
the missing space within "arithmetic topology."

## The points that matter, mapped to the project

1. **The whole program for a number field `K`, in one statement (sect.2-3, formula (3) p.7).**
   `zeta-hat_K(s) = prod_{i=0}^2 det_∞((s-Θ)/2π | H^i_dyn("Spec o bar", R))^{(-1)^{i+1}}`
   with `H^0 = R` (`Θ=0`), `H^1` infinite-dim (`Sp Θ =` non-trivial zeros), `H^2 = R`
   (`Θ=id`). Implies `ξ_K(s) = prod_ρ (s-ρ)/2π`. Hasse-Weil `zeta_X(s)` gets the same
   treatment (sect.3 (7)) with `H^i_dyn,c(X,R)` and Poincare duality (8).
   -> The Direction 4.6 target verbatim, generalized from `Q` to any `K`. The
   `"Spec o bar" =` "projective curve over a finite field" framing (sect.3 p.7) is the
   exact function-field-lift posture of the whole program: the proof should mimic
   Deligne/Weil with `det_∞` replacing the finite `det(1 - Frob)`.

2. **Every Euler factor as one regularized determinant (Proposition 3.1, pp.5-7).**
   With `R_p = R[exp(-2y)]` (real `∞`), `R[exp(-y)]` (complex `∞`), or finite Fourier
   series on `R/(log Np)Z` (finite `p`), and `Θ = d/dy`:
   `zeta_p(s) = det_∞((s-Θ)/2π | R_p)^{-1}` for all places. The computation gives the
   finite factor `1 - Np^{-s}`, the real factor `√2 π^{s/2} Γ(s/2)`, the complex factor
   `(2π)^s Γ(s)`, all from the Lerch/Hurwitz `ζ(0,z) = 1/2 - z`,
   `∂_s ζ(0,z) = log(Γ(z)/√2π)` and `prod_{ν∈Z} γ(z+ν) = 1 - e^{±2πiz}`.
   -> **This is the uniform "all places, one formalism" statement the Lean
   `ExplicitFormula` / `archKernel` rests on, made fully explicit for both real and
   complex archimedean places.** It refines the Deninger I note: the Γ-factor (2I /
   `A_arch`) and the finite Euler factors are the same `det_∞` object evaluated on
   different `R_p`. Good citation for "the archimedean place is not special, it is the
   `p=∞` stationary point of the same flow."

3. **The `Θ = 1/2 + A` RH argument, restated (sect.3 p.9).** Same as 1998: a Hodge `*`
   on `H^1_dyn` with `<f,f'> = tr(f ∪ *f')` positive definite, `Θ` a derivation
   commuting with `*`, forces `Θ = 1/2 + A`, `A` skew-symmetric, hence RH. Same
   Montgomery-Sarnak-Kontsevich remark (hermitian vs real-skew-symmetric statistics
   agree). The Hilbert-Polya space is the completion of `H^1_dyn` under `<,>`.
   -> Direction 8, the harder half. RH = a Hodge-`*` positivity statement on `H^1`,
   not a consequence of the trace formula alone. Consistent across 1998/2002/2005: the
   `*`-operator is the load-bearing object, the marginal-positivity thesis in operator
   form.

4. **The full leafwise-Hodge package for Riemannian foliations (sect.4, (13)-(19)).**
   Alvarez Lopez-Kordyukov Hodge isomorphism `ker Δ_F ≅ H-bar^n_F(X)`; Hodge `*_F`;
   trace `tr: H-bar^d_F -> R`; non-degenerate cup pairing (16); Kunneth (17); and for
   Kahler foliations an `H^{pq}` decomposition (18) with hard-Lefschetz `L_F`
   isomorphisms (19) and a polarizable ind-`R`-Hodge structure on primitive classes.
   -> The complete Direction 4.3 (finiteness/Hodge) + Direction 8 (Hodge/Lefschetz)
   toolkit, assembled. The hard-Lefschetz + polarization (19) is the structure a
   Direction-8 signature theorem would use: a polarized Hodge structure is precisely
   where a Hodge-index / signature statement lives. Note Deninger's own caution (p.19):
   a conformal metric realizing the `α≠0` flow "will [not] exist for dynamical systems
   relevant for number fields ... one will need the Kahler identities on cohomology" to
   verify the stronger `*`-intertwining (11). That is the honest Direction-8 hurdle.

5. **The Arakelov compactification and the stronger `*`-condition (Theorem 3.3 + (11), p.13).**
   If a dynamical `H^i_dyn("X bar", R)` existed on an Arakelov compactification with
   `zeta-hat_X = prod det_∞(...)`, then Poincare duality gives the functional equation,
   and a Hodge `*` with `φ^{t*}∘* = (e^t)^{d-i} *∘φ^{t*}` (i.e. the flow scales the
   metric by `e^t`) would force `Θ - i/2` skew, hence RH. Deninger stresses (11) for
   forms is much stronger than for cohomology classes.
   -> This is the cleanest statement of why the `α = 1` (factor `e^t`) flow is the
   crux, and why it is hard: it is a condition on forms (the metric), not just on
   cohomology. Same `α=0`-vs-`α=1` obstruction as the 2002 note, here tied to the
   Arakelov compactification (the 2I archimedean-completion object).

6. **Arithmetic topology: `"Spec o bar"` is 3-dimensional, primes are knots (sect.1, sect.5).**
   The lectures explicitly connect to "Arithmetic Topology" (analogies between number
   theory and 3-manifolds). `"Spec o bar"` should be a 3-dim foliated space; closed
   orbits (= primes) are 1-dimensional (knots/links) inside it; the flow's `R`-action
   is the missing archimedean Frobenius.
   -> Frames the missing object (2K) as a 3-manifold-like foliated space. This is the
   same hole as `Spec(Z) x Spec(Z)`, viewed through the Mazur "primes = knots"
   dictionary. Useful: it says the Direction-8 surface and the Deninger 3-manifold are
   two cultural descriptions of one missing geometry, and that the intersection
   form (Direction 8) corresponds to linking/cup pairings in the 3-manifold picture.

## What this changes for the program

- **Best single citation for the whole Deninger program.** Where 1998 is the original
  and 2002 carries the proved ALK theorem, 2005 is the polished, number-field-general,
  self-contained version. Cite it for: the `det_∞` Euler-factor uniformity (Prop 3.1),
  the `Θ = 1/2 + A` RH argument (p.9), and the full leafwise-Hodge package (sect.4).
- **The archimedean place is rigorously "just another `det_∞`."** Prop 3.1 derives both
  real and complex Γ-factors from the same formula as the finite factors. This nails the
  2I / `A_arch` posture: the archimedean local height / Γ-factor is the `p=∞` stationary
  point of the same flow, not a bolt-on. Direct support for the Lean archimedean kernel.
- **Direction 8's natural home is the polarized Hodge structure on `H-bar^1_prim`.** The
  hard-Lefschetz + polarization (sect.4 (19)) is exactly the setting for a Hodge-index /
  signature theorem. The honest obstruction (p.19): the strong `*`-on-forms condition
  (the `α=1` conformal scaling) is what is missing, and Deninger expects it needs Kahler
  identities, not a metric. This pins what a Direction-8 attempt must produce.
- **"Spec(Z) x Spec(Z)" and Deninger's 3-manifold are the same gap.** The arithmetic-
  topology framing says the missing surface (Direction 8) and the missing foliated
  3-space (Direction 4) are one object in two languages. Worth keeping both charts:
  the intersection form (surface) <-> linking/cup pairing (3-manifold).

## Actionable

- Use Prop 3.1 (pp.5-7) as the citation whenever the program asserts "all Euler factors,
  finite and archimedean, are one `det_∞`." It has the explicit real and complex `∞`
  computations the Deninger I note only sketched.
- The stronger `*`-on-forms condition (11) plus Deninger's caution (p.19, "will need the
  Kahler identities on cohomology") is the precise specification of the Direction-8
  hurdle. Pair with the 2002 `α=0` obstruction and the polarized-Hodge structure (19).
- No new computation beyond 2R. The arithmetic-topology framing suggests a possible
  future cross-reference to the Mazur "primes = knots" literature if Direction 8 wants a
  linking-form model of the intersection pairing.

## Status

Read pp.1-22 of the lecture notes: sect.1 intro, sect.2 Dedekind/Hasse-Weil zeta, sect.3
the cohomological formalism incl. Prop 3.1 (all Euler factors as `det_∞`), the explicit
formula, Theorem 3.3 and the `Θ=1/2+A` / Arakelov `*`-argument, sect.4 foliation
cohomology + leafwise Hodge + Kahler/Lefschetz package, sect.5 the dynamical Lefschetz
formulas (Conjecture 5.1, Theorem 5.3 = the ALK trace formula). Recognized throughout as
a consolidation of 1998+2002; depth focused on what is new or sharpest here (Prop 3.1's
explicit archimedean factors, the Arakelov `*`-condition (11), the arithmetic-topology
framing). The ALK trace-class theorem (Thm 5.3) read as a cited black box, detailed in
the ALK 2017 note.
