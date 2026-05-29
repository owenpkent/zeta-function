# Reading notes: Deninger, *Number Theory and Dynamical Systems on Foliated Spaces* (Liege 2001 / arXiv math.NT/0204110, 2002)

> Reference-library read-through ([`README.md`](README.md)). The sequel to the 1998
> ICM ([`Deninger-1998-ICM-Analogies-Foliated.md`](Deninger-1998-ICM-Analogies-Foliated.md)),
> written deliberately without motives. This is where the conjectural 1998 picture
> first meets a real theorem on the dynamical side: the Alvarez Lopez-Kordyukov
> trace formula for flows transversal to a one-codimensional foliation, and the
> resulting Corollary 3.5 (`Re = α/2` from `Θ = α/2 + S`, `S` skew-adjoint). It also
> states sharply why the manifold setting forces `α = 0` and hence why laminated
> spaces (and ultimately fixed points) are needed for number theory, the gap ALK
> 2017 attacks. Pages refer to the PDF in `references/02_deninger_program/`.
> Read: pp.1-18 (sect.1-4, foliation cohomology, the ALK trace formula, the explicit-
> formula comparison), pp.19-22 (sect.5, laminated spaces / generalized solenoids).

## One-line takeaway

For a Riemannian foliation `F` on a compact manifold with an `F`-compatible flow
that is everywhere transversal (no fixed points), Alvarez Lopez-Kordyukov prove a
genuine Lefschetz trace formula: the operator `A_φ = ∫ φ(t) φ^{t*} dt` on reduced
leafwise cohomology is trace class, and the resulting `Tr(φ^*|H-bar^n_F)` reproduces
the closed-orbit side of the explicit formula. The infinitesimal generator splits
`Θ = α/2 + S` (`S` skew-adjoint, `α` the conformal weight of the flow), so the
`H^1`-spectrum sits on `Re = α/2`. The catch: in the manifold setting `α = 0`
(isometric flow), the wrong weight for number fields (which need `α = 1`), and the
flow has no fixed points (number fields need `p = ∞` as a fixed point). That double
mismatch is the explicit motivation for laminated spaces and for ALK 2017.

## The points that matter, mapped to the project

1. **Reduced leafwise cohomology + the leafwise Hodge theorem (sect.2, (2)).** `H-bar^n_F(X)
   = ker d_F / closure(im d_F)`, a nuclear Frechet space, infinite-dimensional even
   for `H-bar^1`. For Riemannian foliations with a bundle-like metric the
   Alvarez Lopez-Kordyukov Hodge theorem gives `ker Δ_F ≅ H-bar^n_F(X)` (deep: `Δ_F`
   is only leafwise elliptic, ordinary elliptic regularity fails). This yields a
   Hodge `*_F`, a trace `tr: H-bar^d_F -> R`, a non-degenerate cup pairing, a Kunneth
   formula, and (Kahler case) an `H^{pq}` decomposition with hard-Lefschetz.
   -> This is the analytic substrate Direction 4.3 (finiteness/Hodge) needs and the
   `H^1` of Direction 4.6 is modeled on. The Kunneth `H-bar^*_{X×Y}` (sect.2 (6)) is
   the foliated analogue of the 2K product structure: it shows the product/`×` works
   at the leafwise-cohomology level once you have the spaces.

2. **The RH mechanism `Θ = α/2 + S` (Theorem 2.1 p.8, Corollary 3.5 p.13).** For a
   3-manifold with a Riemannian surface foliation, dense leaf, and a flow conformal on
   `TF` with factor `e^{αt}`: `Θ = 0` on `H-bar^0`, `Θ = α` on `H-bar^2`, and on
   `H-bar^1` `Θ = α/2 + S` with `S` skew-symmetric. Hence `Sp(Θ) ⊂ {Re = α/2}`. The
   proof: conformality makes `e^{-(α/2)t}φ^{t*}` orthogonal, so by Stone `T = -iS` is
   self-adjoint; equivalently `-(Θ - α/2)^2 = Δ^1|_{ker Δ^1_F}` (sect.3 p.14).
   -> **This is the proved, conditional version of the 1998 `Θ = 1/2 + A` RH argument
   (Direction 8 step).** It is the flow-side `Re = α/2` theorem that Leichtnam 2006
   then specializes to laminated spaces with `α` set by `|ξ| = √q`. Note the
   structure: `Re = α/2` is forced by the Hodge `*`-positivity + conformality, exactly
   the marginal-positivity content. The skew part `S` carries the zeros.

3. **The Alvarez Lopez-Kordyukov trace-class theorem (Theorem 3.3 p.11, "[AK2]").**
   For a flow everywhere transversal to a one-codimensional Riemannian `F`, the
   operator `A_φ = ∫_R φ(t) φ^{t*} dt` on `H-bar^n_F(X)` is trace class, and
   `Σ_n (-1)^n Tr(φ^*|H-bar^n_F) = χ_Co(F,μ) δ_0 + Σ_γ l(γ) Σ_k ε_γ(k) δ_{kl(γ)}` in
   `D'(R)`. The non-zero RHS forces some `H-bar^n_F` infinite-dimensional.
   -> **This is the cited "[A-K00]"/"[AK2]" theorem at the heart of Leichtnam 2006
   and the subject of the ALK 2017 note.** The trace-class mechanism (`A_φ` is
   smoothing because integrating the flow against a test function regularizes; note
   `φ^{t*}∘Π` alone is not trace class) is the concrete answer to Direction 4.3
   (finiteness). The `χ_Co(F,μ) δ_0` term is the `s=0,1` polar contribution; sect.4
   identifies it with `-log|d_{K/Q}|` (the discriminant / Connes Euler characteristic).

4. **The strong spectral statement (Theorem 3.4 p.12).** For orthogonal `φ^{t*}`,
   `T = -iΘ` is self-adjoint and `φ^{t*} = exp(itT)`; `Θ` has pure point spectrum in
   a strip `-ω ≤ Re ≤ ω`. The remark (p.14) covers the continuous-spectrum case via a
   spectral density `m(λ) ≥ 0` on the line `Re = α/2`: a contour `∫_{α/2-i∞}^{α/2+i∞}
   Φ(λ) m(λ) dλ`.
   -> The continuous-spectrum/contour form is exactly the shape needed if the zeros
   were to be a continuous spectrum rather than discrete. For the arithmetic case
   (discrete zeros) the pure-point statement is the target; the machinery handles both.

5. **The explicit-formula comparison and the `α = 0` obstruction (sect.4, p.16-18).**
   The Dedekind explicit formula (Theorem 4.1) is written as the distributional
   identity (19) and matched term-by-term against Corollary 3.5's (13): finite place
   `p` <-> transversal closed orbit with `l(γ) = log Np`; infinite place <-> fixed
   point with `κ = κ_p`; `-log|d_{K/Q}| <-> χ_Co(F,μ)` (and `χ_Co ≤ 0` matches
   `-log|d| ≤ 0`, via Connes' `β_0 = 0` for complete leaves, Fact 4.2). **But** the
   match fails on two counts: (a) number theory needs `α = 1` (the `e^t` factor),
   impossible for manifolds where Cor 3.5 forces `α = 0`; (b) the `k ≤ -1` coefficients
   are `±1` for manifolds but `Np^k = e^{k log Np}` for number fields.
   -> **This is the precise statement of why the foliated picture is not yet the
   arithmetic one, and it is the 2K gap in flow language.** The fix requires phase
   spaces more general than manifolds (laminated spaces) AND fixed points (the
   archimedean place). Both are exactly what ALK 2017 must supply. The `χ_Co =
   -log|d_{K/Q}|` identification (sect.4 (20)-(21), via Connes Riemann-Roch and the
   Arakelov Euler characteristic `χ_Ar = -log√|d|`) is a clean 2I-flavored archimedean
   bookkeeping: the discriminant is the foliated Euler characteristic.

6. **Laminated spaces / generalized solenoids as the fix (sect.5, p.18-22).** A
   laminated space is locally `(open in R^a) × (totally disconnected)`; the classical
   solenoid `S^1_p = R ×_Z Z_p = lim(... -> R/Z -> R/Z ...)` is the model. The working
   hypothesis (5.6, (26)) extends the trace formula to such spaces and to `D'(R*)`
   (both signs of `t`), allowing `α ≠ 0` and a fixed-point term `W_x` with the correct
   `|1 - e^{κ_x t}|^{-1}` shape on `R^{>0}` and `det(...)|1-e^{κ_x|t|}|^{-1}` on `R^{<0}`.
   -> The totally-disconnected transversal here is the `Z_p` that Leichtnam 2006 makes
   the "p-adic transversal" and that the prismatic direction realizes. This is the
   Direction-3 × Direction-4 bridge in embryo: number theory enters through the
   totally-disconnected (p-adic / adelic) transversal. D-H discipline note: such a
   space carries a genuine `{log p}` closed-orbit spectrum; the Davenport-Heilbronn
   function has no Euler product and hence no such orbit spectrum, so this construction
   is on the right side of the wrong-approach detector (consistent with 2R).

## What this changes for the program

- **The `Re = α/2` theorem is real, conditional, and exactly the Direction-8 step in
  flow form.** Corollary 3.5 proves `Sp(Θ) ⊂ {Re = α/2}` from Hodge-`*` + conformality.
  RH would be the `α = 1` instance. The whole gap between "have it" and "RH" is: get a
  phase space where `α = 1` and fixed points are allowed. This sharpens Direction 4.6/8
  to a concrete analytic target.
- **The trace-class question (Direction 4.3) is solved in the non-singular case.** ALK
  2002 (Thm 3.3) is the existence proof: `A_φ = ∫ φ φ^{t*} dt` is trace class for
  transversal flows. The remaining analytic difficulty is precisely fixed points, where
  `Δ_F` is no longer transversally elliptic to the `R`-action. This is the exact
  boundary ALK 2017 pushes.
- **The 2K product-surface gap has a flow-language twin.** "Manifolds force `α = 0` and
  forbid fixed points; number theory needs `α = 1` and a fixed point at `∞`" is the same
  obstruction as "no absolute base point / no `Spec(Z) x Spec(Z)`." The discriminant
  bookkeeping `χ_Co = -log|d_{K/Q}|` shows the archimedean/global accounting already
  works; what is missing is the space.
- **The totally-disconnected transversal is where arithmetic enters.** Section 5 makes
  explicit that the move from manifolds to laminated spaces (solenoids with `Z_p`
  factors) is what could supply `α = 1`. This is direct support for the Direction-3
  (p-adic/prismatic) + Direction-4 (foliation) combination and consistent with the
  Leichtnam 2006 note's "p-adic transversal makes the trace class" finding.

## Actionable

- Treat Corollary 3.5 / Theorem 2.1 (`Θ = α/2 + S`) as the canonical conditional
  `Re = 1/2` statement on the flow side, and the `α = 0` vs `α = 1` mismatch (sect.4
  p.18) as the precise specification of what a number-theoretic phase space must fix.
- The working hypothesis (5.6) formula (26), with its two-sided `W_x` fixed-point
  distributions, is the target the ALK 2017 general-case trace formula aims to prove.
  Read it alongside ALK 2017's "term supported on `M^0`" slides.
- No new computation. The structural takeaway feeds the trace<->signature thread: 2R
  gives the orbit spectrum, Cor 3.5 gives `Re = α/2` from `*`-positivity, Direction 8 is
  the `α = 1` Hodge-`*` realization.

## Status

Read pp.1-22 of 22 (the full body): sect.1 intro, sect.2 foliation cohomology + leafwise
Hodge + Theorem 2.1, sect.3 the ALK trace formula (Thm 3.3) and spectral theorem (Thm
3.4) and Corollary 3.5, sect.4 the explicit-formula comparison and `α=0` obstruction,
sect.5 laminated spaces and the working hypothesis (5.6). Honest depth: the leafwise
Hodge theorem and ALK trace-class theorem are read as cited black boxes (their proofs
are in the [AKI]/[AK2] references, i.e. ALK 2017 and Moore-Schochet).
