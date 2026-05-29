# Reading notes: Alvarez Lopez, Kordyukov, Leichtnam, *A Trace Formula for Foliated Flows* (Dayton 2017 talk, "work in progress")

> Reference-library read-through ([`README.md`](README.md)). This is the general
> foliated-flow trace formula machinery that Deninger 2002/2005 invoke as "[AK2]"
> and Leichtnam 2006 cites as "[A-K00]". The 2002/2005 papers proved the
> non-singular (no-fixed-point) case; this is the team's attack on the case WITH
> fixed points, i.e. the case number fields actually need (the archimedean place is
> a fixed point of the flow). The source is a slide deck / extended abstract from the
> 32nd Summer Conference on Topology, so depth is "what the slides commit to," not a
> full proof. It is the most direct existing work on the hardest analytic part of
> Direction 4.3 (trace class with fixed points) feeding Direction 4.6. Pages refer to
> the PDF in `references/03_foliated_cohomology_trace/`. Read: the full slide
> sequence (cover + sect.1 the trace formula, sect.2 non-singular case, sect.3 the
> general case with the conormal-distribution leafwise complex).

## One-line takeaway

For a foliated flow `φ^t` (leaves -> leaves) on a closed manifold `M` with a
codimension-one foliation `F`, with simple closed orbits and simple fixed points, the
goal is a Lefschetz distributional trace formula `L(φ) = Σ_i (-1)^i Tr^s(φ^*|H^i) =
Σ_c l(c) Σ_k ε_{kl(c)}(c) δ_{kl(c)} + Σ_p ε_p / |1 - e^{κ_p t}|` (closed orbits + fixed
points). The non-singular case (`M^0 = ∅`) is the Alvarez Lopez-Kordyukov 2002 theorem:
`A_f = ∫ φ^{t*} f(t) dt ∘ Π` is smoothing (trace class), via the leafwise Hodge
projection `Π` onto leafwise-harmonic forms. The new work is the fixed-point case
(`M^0 ≠ ∅`): there the foliation is no longer Riemannian and the Schwartz kernel of
`A_f` is not smooth at `M^0`, so they replace the smooth leafwise de Rham complex with a
complex of distributional leafwise forms conormal to `M^0`, split off the `M^0`-supported
piece via a canonical short exact sequence, and compute each term's trace formula.

## The points that matter, mapped to the project

1. **The precise foliated-flow trace formula being proved (sect.1, "the problem").** The
   distributional Lefschetz trace `L(φ) := Tr^s(φ^*) = Σ_i (-1)^i Tr(φ^*|H^i) ∈ C^{-∞}(R)`
   on a "leafwise cohomology" `H^i`, with target identity on `R^+`:
   `L(φ) = Σ_c l(c) Σ_{k=1}^∞ ε_{kl(c)}(c) δ_{kl(c)} + Σ_p ε_p / |1 - e^{κ_p t}|`,
   where `c` runs over closed orbits (`l(c)` = minimal period), `p` over fixed points.
   Explicitly credited to Guillemin-Sternberg and C. Deninger (ICM 1998), motivated by
   "Deninger's program needs a version for foliated spaces. Arithmetic foliated spaces?"
   -> **This is the exact Direction 4.6 target distribution**, the foliated form of the
   explicit formula (1998 formula (5)/(22), 2002 formula (26)). The closed-orbit term is
   the `Σ_p log p Σ_k δ_{k log p}` von Mongoldt side (2R's orbit-length spectrum); the
   fixed-point term `ε_p/|1 - e^{κ_p t}|` is the archimedean Γ-factor contribution (2I /
   `A_arch`). The slides name Deninger's program as the motivation, so this is
   self-consciously the machinery for Direction 4.6.

2. **The simplicity hypotheses (sect.1, "Hypotheses").** (i) closed orbits simple:
   `det(id - φ^ℓ_* : T_xF -> T_xF) ≠ 0` (gives `ε_ℓ(c) = sign det`); (ii) fixed points
   simple: `det(id - φ^t_* : T_pM -> T_pM) ≠ 0` for all `t ≠ 0` (gives `ε_p = sign det`,
   `φ-bar^t_* = e^{κ_p t}` on `N_pF = T_pM/T_pF`, and `M^0` = finite union of compact
   leaves); (iii) `φ^t` transversal to `F` on `M^1 := M \ M^0`.
   -> These are the non-degeneracy conditions of the 1998/2002 conjectures, made
   precise. The split `M = M^0 ⊔ M^1` (fixed-point leaves vs the transversal part) is the
   key structural device: `M^1` carries the closed-orbit/Riemannian analysis, `M^0` the
   fixed-point/archimedean analysis. For the arithmetic dictionary `M^0` = the
   archimedean place(s), `M^1` = the finite primes. The `κ_p` is the same archimedean
   weight `κ = -2` (real) / `-1` (complex) from the explicit formula.

3. **Leafwise Hodge isomorphism = the finiteness/trace-class enabler (sect.2, "Leafwise
   Hodge isomorphism").** For ANY Riemannian foliation on a closed manifold, any
   codimension: with a bundle-like metric, the leafwise Laplacian `Δ_F = d_F δ_F + δ_F d_F`
   is symmetric in `L^2(M;ΛF)`; `H = ker Δ_F` in `C^∞`, `L^2 H = ker Δ_F` in `L^2`, and the
   orthogonal projection `Π: L^2(M;ΛF) -> L^2 H` restricts to `Π: C^∞ -> H` inducing
   `H-bar(F) ≅ H` (the Alvarez Lopez-Kordyukov 2001 Hodge theorem).
   -> **This is the cited "[A-K00]" Hodge machinery** behind Leichtnam 2006's `H^1_τ` and
   Deninger 2002/2005's leafwise-Hodge package. It is the reason reduced leafwise
   cohomology is a Hilbert space with a well-defined trace at all. Direction 4.3
   (finiteness) is exactly this `H-bar(F) ≅ ker Δ_F` plus the trace-class statement in
   point 4. Note the generality: arbitrary codimension, any Riemannian foliation, which is
   why it is the foundational lemma the program leans on.

4. **The non-singular trace-class theorem (sect.2, "Lefschetz trace formula ... 2002").**
   The hinge fact: for `f ∈ C^∞_c(R)`, the operator `A_f = ∫_R φ^{t*} f(t) dt ∘ Π` is
   SMOOTHING (hence trace class), even though `φ^{t*} ∘ Π` alone is NOT. Then
   `L(φ) = (f ↦ Tr^s A_f) ∈ C^{-∞}(R)` and on `R^+`,
   `L(φ) = Σ_c l(c) Σ_{k=0}^∞ ε_c(kl(c)) δ_{kl(c)}` (Alvarez Lopez-Kordyukov 2002).
   -> **This is the precise hypothesis-and-mechanism for Direction 4.3, in the
   no-fixed-point case.** The mechanism: integrating the flow against a test function
   `f(t) dt` (smearing in `t`) plus the harmonic projection `Π` is what regularizes to
   trace class. This is the analytic content under Leichtnam 2006's "contraction process
   makes `∫ α(s)(φ^t)^* ds ∘ π^j_τ` trace class." It tells a Direction-4.6 builder the
   exact object to model: not `φ^{t*}` but its `f`-smearing composed with `Π`.

5. **The fixed-point obstruction and the conormal-distribution fix (sect.3, "Difficulties"
   + "Distributional leafwise forms conormal to `M^0`").** With `M^0 ≠ ∅`: `F` is NOT
   Riemannian (only `F^1 = F|_{M^1}` is); `F` is a transversely affine foliation almost
   without holonomy; and crucially **the Schwartz kernel of `A_f` is not smooth at `M^0`**,
   so the smooth complex `(C^∞(M;ΛF), d_F)` fails. The fix: a complex `I(M, M^0; ΛF)` of
   distributional leafwise forms conormal to `M^0` (Sobolev-graded
   `I^{[s]}(M,M^0;ΛF) = { α ∈ H^s | Diff(M,M^0;ΛF)·α ⊂ H^s }`), with `d_F` extended
   continuously to `C^{-∞}(M;ΛF)`, giving a reduced cohomology `H-bar(I(M,M^0;ΛF), d_F)`.
   -> **This is the precise statement of why fixed points are the hard part of Direction
   4.3/4.6, and the team's strategy for it.** It is exactly the gap Deninger 2002 (sect.4,
   `α=0` / no-fixed-point obstruction) and Leichtnam 2006 (Assumption (iv) only at g=1)
   left open. For the arithmetic program the archimedean place IS a fixed point, so the
   non-singular ALK 2002 theorem alone cannot give the full explicit formula; this
   conormal-distribution complex is the route to including the `p=∞` Γ-factor term
   rigorously. The "transversely affine, almost without holonomy" geometry near `M^0` is a
   concrete model for what the archimedean local structure must look like.

6. **The canonical short exact sequence and the `M^0`-supported term (sect.3, last
   slides).** `α ∈ I(M,M^0;ΛF)` restricts to `α|_{M^1} ∈ C^∞(M^1;ΛF^1)`, giving a canonical
   SES `0 -> {α : supp α ⊂ M^0} -> I(M,M^0;ΛF) -> {α|_{M^1}} -> 0` with a (non-canonical)
   continuous section, hence a direct-sum decomposition of `H-bar(I(M,M^0;ΛF), d_F)`. One
   defines `L(φ)` on each summand separately. For the `M^0`-supported piece, transverse
   orientation (`TF = ker ω`, `dω = ω ∧ η`, transversely affine `⟹ dη = 0`) gives, via
   `δ`-sections and transverse derivatives at `M^0`, an explicit
   `{α : supp α ⊂ M^0} ≅ ⊕_{k≥0} C^∞(M^0; ΛM^0 ⊗ Ω^{-1} N M^0)` with
   `d_F = ⊕_k (d_{M^0} + k η∧)`.
   -> The strategy is "split the trace formula into a transversal (closed-orbit /
   finite-prime) part and a fixed-point (archimedean) part, and handle each." The
   `⊕_k (d_{M^0} + k η∧)` graded structure on the `M^0` term is the analytic origin of the
   archimedean `1/(1 - e^{κt})` factor (a geometric series over `k`), i.e. the Γ-factor as
   a sum over transverse jets. This is the cleanest available picture of how the
   archimedean term (2I) arises inside the trace formula.

## What this changes for the program

- **Direction 4.3 (finiteness/trace class) has a precise, two-regime status.** Non-singular
  regime (finite primes only): SOLVED by ALK 2002 (`A_f = ∫ φ^{t*} f dt ∘ Π` is
  smoothing). Singular regime (with the archimedean fixed point): IN PROGRESS via the
  conormal-distribution complex `I(M,M^0;ΛF)`. This note is the citation for both the
  solved part and the live attack on the open part.
- **The archimedean place IS the fixed-point difficulty.** This reframes 2I: the Γ-factor
  is not a separate hand-added piece, it is the trace contribution of the flow's fixed
  point `M^0`, and the reason it is analytically hard (non-smooth Schwartz kernel,
  non-Riemannian `F` near `M^0`) is the same reason the archimedean place resists a clean
  cohomological treatment. The `⊕_k (d_{M^0} + kη∧)` jet structure is a candidate
  mechanism for the `1/(1-e^{κt})` Γ-factor term.
- **It tells a Direction-4.6 builder exactly what to model.** The object is the smeared,
  harmonic-projected operator `A_f`, not `φ^{t*}` itself; the trace class comes from
  smearing in `t` plus `Π`; with fixed points one needs distributional forms conormal to
  `M^0`. Any project-native model of the trace formula should reproduce this structure.
- **It is "work in progress" / a slide deck, not a finished theorem.** Honest caveat: the
  general (fixed-point) case is presented as a strategy with the key constructions stated
  but the final trace-formula computation on the `M^0` summand left in progress. So for
  the program, the singular case is "machinery identified and under construction," not
  "available off the shelf." This matches the in-house reading that the archimedean/fixed-
  point step is the open analytic frontier.
- **D-H discipline.** The trace formula's closed-orbit spectrum `{l(c)} = {log Np}` is an
  Euler-product fingerprint; the Davenport-Heilbronn function has no Euler product and no
  such primitive-orbit spectrum (the 2R / Leichtnam 2006 finding). This machinery is
  therefore on the right side of the wrong-approach detector: it engages the orbit
  spectrum that distinguishes zeta from D-H.

## Actionable

- Cite this as the precise reference for: (a) the non-singular trace-class mechanism
  `A_f = ∫ φ^{t*} f dt ∘ Π` smoothing (Direction 4.3, finite-prime regime), and (b) the
  conormal-distribution complex `I(M,M^0;ΛF)` as the strategy for the archimedean
  fixed-point regime.
- The `⊕_k (d_{M^0} + kη∧)` graded `M^0`-complex (last slide read) is the concrete object
  to study if the program wants to derive the archimedean `1/(1-e^{κt})` Γ-factor term
  from the flow rather than assume it. Pair with Deninger 2005 Prop 3.1 (the Γ-factor as
  `det_∞` on `R[exp(-2y)]`): both are "Γ-factor as a sum/product over transverse jets `k`."
- Track whether the finished paper appears (this is 2017 "in progress"): a completed
  general-case trace formula would be the first rigorous foliated explicit formula
  including the archimedean place, a direct Direction-4.6 deliverable. No project
  computation follows directly; this is analytic/structural input.

## Status

Read the full slide deck (cover, contents, and all build-stages of: "Foliated flows,"
"The problem of the trace formula," "Motivation," "Hypotheses," the torus example,
"Non-singular foliated flows," "Leafwise Hodge isomorphism," the 2002 non-singular
"Lefschetz trace formula," "Difficulties," "Distributional leafwise forms conormal to
`M^0`," "Canonical short exact sequence," "Term supported on `M^0`"). Honest depth: this
is a presentation, so the trace-class claims and the leafwise Hodge isomorphism are
stated with their mechanism but without the full analytic proofs (those live in the
Alvarez Lopez-Kordyukov 2001/2002 papers and the eventual full article). The general
(fixed-point) case is explicitly "work in progress."
