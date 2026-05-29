# Reading notes: Alvarez Lopez, Kordyukov, Leichtnam, *A Trace Formula for Foliated Flows* (Dayton 2017 talk, "work in progress")

> Reference-library read-through ([`README.md`](README.md)). This is the general
> foliated-flow trace formula machinery that Deninger 2002/2005 invoke as "[AK2]"
> and Leichtnam 2006 cites as "[A-K00]". The 2002/2005 papers proved the non-singular
> (no-fixed-point) case; this slide deck is the team's attack on the case WITH fixed
> points, i.e. the case number fields actually need (the archimedean place is a fixed
> point of the flow). The source is the slide deck / extended abstract from the 32nd
> Summer Conference on Topology and its Applications (University of Dayton eCommons,
> June 2017), so depth is "what the slides commit to," not a full proof. It is the
> most direct existing work on the hardest analytic part of Direction 4.3 (trace
> class with fixed points) feeding Direction 4.6. Pages refer to the PDF in
> `references/03_foliated_cohomology_trace/`. Read in full: the entire slide sequence
> (cover, contents, "Foliated flows," "Hypotheses," the torus example, "The problem
> of the trace formula," "Motivation," "Non-singular foliated flows," "Leafwise Hodge
> isomorphism," the 2002 non-singular Lefschetz formula, "Difficulties,"
> "Distributional leafwise forms conormal to `M^0`," "Canonical short exact sequence,"
> "Term supported on `M^0`," and the full "Term supported on `M^1`" b-calculus
> sequence, through the closing slide). Companion notes:
> [`Deninger-1998-ICM-Analogies-Foliated.md`](Deninger-1998-ICM-Analogies-Foliated.md),
> [`Deninger-2002-NT-Dynamical-Foliated.md`](Deninger-2002-NT-Dynamical-Foliated.md),
> [`Deninger-2005-Arithmetic-Geometry-Foliated.md`](Deninger-2005-Arithmetic-Geometry-Foliated.md),
> [`Leichtnam-2006-Lefschetz-laminated-spaces.md`](Leichtnam-2006-Lefschetz-laminated-spaces.md),
> [`Moore-Schochet-Global-Analysis-Foliated-Spaces.md`](Moore-Schochet-Global-Analysis-Foliated-Spaces.md).

## One-line takeaway

For a foliated flow `φ^t` (leaves → leaves) on a closed manifold `M` with a
codimension-one foliation `F`, simple closed orbits and simple fixed points, the goal
is a Lefschetz distributional trace formula `L(φ) = Σ_i (-1)^i Tr^s(φ^*|H^i) =
Σ_c l(c) Σ_k ε_{kl(c)}(c) δ_{kl(c)} + Σ_p ε_p / |1 - e^{κ_p t}|` (closed orbits + fixed
points). The non-singular case (`M^0 = ∅`) is the Alvarez Lopez-Kordyukov 2002 theorem:
`A_f = ∫ φ^{t*} f(t) dt ∘ Π` is smoothing (trace class), via the leafwise Hodge
projection `Π` onto leafwise-harmonic forms. The new work splits `M = M^0 ⊔ M^1`
(fixed-point leaves vs the transversal part) and attacks each: on `M^0` (where `F` is
not Riemannian and the Schwartz kernel of `A_f` is not smooth) they replace the smooth
leafwise complex by distributional leafwise forms conormal to `M^0`, decompose via a
canonical short exact sequence into an `M^0`-supported piece (a sum of Novikov complexes
on `M^0`) and an `M^1`-restriction piece; on `M^1` (non-compact after cutting through
`M^0`) they use Melrose b-calculus, getting a b-trace `bTr^s(A_f)` whose anomaly
`bTr[A,B] ≠ 0` is the source of the extra (archimedean / fixed-point) term. As of 2017
the `m = 0` case is solved; the full computation is in progress.

## Technical content (section by section)

**Foliated flows + hypotheses (the setup).** `M` a closed manifold `dim M = n`, `F` a
foliation `codim F = 1`, `φ = (φ^t)` a foliated flow (leaves → leaves), `M^0` = union of
leaves containing fixed points, `M^1 = M \ M^0`. **Hypotheses:**
1. closed orbits simple: for any period `ℓ` and `x ∈ c`, `det(id - φ^ℓ_* : T_x F →
   T_x F) ≠ 0` ⟹ `ε_ℓ(c) = sgn det`;
2. fixed points simple: `det(id - φ^t_* : T_p M → T_p M) ≠ 0` for all `t ≠ 0`
   ⟹ `ε_p = sgn det`, the transverse action `φ-bar^t_* = e^{κ_p t}` on
   `N_p F = T_p M / T_p F` (`κ_p ≠ 0`), and `M^0` is a finite union of compact leaves;
3. `φ^t ⫛ F` (transversal) on `M^1 = M \ M^0`.
Worked example: the linear flow on `T^2` (the torus pictures), with `M^0` the
fixed-point fibers and the transversal directions shown as vector fields.

**The problem of the trace formula (Guillemin-Sternberg, C. Deninger).** Define a
"leafwise cohomology" `H^i` with `φ^* = (φ^{t*})`, a "distributional trace"
`Tr(φ^*|_{H^i}) ∈ C^{-∞}(R)`, and the "Lefschetz distribution"
`L(φ) := Tr^s(φ^*) = Σ_i (-1)^i Tr(φ^*|_{H^i}) ∈ C^{-∞}(R)`. **Target identity on
`R^+`:** `L(φ) = Σ_c l(c) Σ_{k=1}^∞ ε_{kl(c)}(c) δ_{kl(c)} + Σ_p ε_p / |1 - e^{κ_p t}|`,
`c` over closed orbits (`l(c)` minimal positive period), `p` over fixed points.
**Motivation (verbatim slide):** Guillemin-Sternberg (Quantization); C. Deninger
(Arithmetic Geometry, Berlin ICM 1998); "Deninger's program needs a version for
foliated spaces. Arithmetic foliated spaces?"

**Non-singular foliated flows (`M^0 = ∅`).** `φ` has no fixed point ⟹ infinitesimal
generator `X ≠ 0`. Choose a Riemannian metric on `M` with `|X| = 1` and `X ⊥ F`; then
`F` is defined by local Riemannian submersions (a bundle-like metric, a Riemannian
foliation). Leafwise complex `(C^∞(M; ΛF), d_F)`, `ΛF = Λ T^*F`, `d_F` = leafwise de
Rham. Reduced leafwise cohomology `H-bar(F) = ker d_F / closure(im d_F)`. Then
`φ^{t*}: H-bar^i(F) → H-bar^i(F)`; `H-bar^i(F)` may be infinite-dimensional, so "Trace?"
is the issue.

**Leafwise Hodge isomorphism (any Riemannian foliation on a closed manifold, any
codimension).** `δ_F` = adjoint of `d_F` on the leaves ⟹ leafwise Laplacian
`Δ_F = d_F δ_F + δ_F d_F`, symmetric in `L^2(M; ΛF)` (bundle-like metric);
`H = ker Δ_F` in `C^∞`, `L^2 H = ker Δ_F` in `L^2`; the orthogonal projection
`Π: L^2(M; ΛF) → L^2 H` restricts to `Π: C^∞(M; ΛF) → H` and induces `H-bar(F) ≅ H`
(Alvarez Lopez-Kordyukov 2001). This is the foundational lemma: it is why reduced
leafwise cohomology is a Hilbert space with a well-defined trace.

**Lefschetz trace formula, non-singular case (ALK 2002).** **The hinge fact:** for
`f ∈ C^∞_c(R)`, the operator `A_f = ∫_R φ^{t*} f(t) dt ∘ Π` is SMOOTHING (hence trace
class), even though `φ^{t*} ∘ Π` alone is NOT. Then `L(φ) = (f ↦ Tr^s A_f) ∈ C^{-∞}(R)`,
and on `R^+`: `L(φ) = Σ_c l(c) Σ_{k=0}^∞ ε_c(kl(c)) δ_{kl(c)}`. The mechanism is
explicit: smearing the flow against a test function `f(t) dt` (regularizing in `t`) plus
the harmonic projection `Π` is what produces trace class.

**Difficulties (`M^0 ≠ ∅`).** With fixed points: `F` is NOT Riemannian (only
`F^1 = F|_{M^1}` is); `F` is a transversely affine foliation almost without holonomy
(only the compact leaves in `M^0` have holonomy); and **crucially the Schwartz kernel of
`A_f` is not smooth at `M^0`**, so the smooth complex `(C^∞(M; ΛF), d_F)` fails. The
fix: another leafwise complex, of elements of `C^{-∞}(M; ΛF)` with "nice" singularities
at `M^0`.

**Distributional leafwise forms conormal to `M^0`.** `X(M, F)` = infinitesimal
transformations of `(M, F)` = infinitesimal generators of foliated flows; it generates
the `C^∞(M)`-module `X(M, M^0) = { Y ∈ X(M) | Y tangent to M^0 }`; `X(M, M^0)`
generates `Diff(M, M^0; ΛF)`, and `d_F ∈ Diff(M, M^0; ΛF)`. With `H^s(M; ΛF)` the
Sobolev space of order `s`, define the **conormal complex**:
`I^{[s]}(M, M^0; ΛF) = { α ∈ H^s(M; ΛF) | Diff(M, M^0; ΛF) · α ⊂ H^s(M; ΛF) }`,
`I(M, M^0; ΛF) = ∪_s I^{[s]}(M, M^0; ΛF)`. `d_F` extends continuously to
`C^{-∞}(M; ΛF)`, giving the reduced cohomology `H-bar(I(M, M^0; ΛF), d_F)`.

**Canonical short exact sequence.** `α ∈ I(M, M^0; ΛF)` restricts to `α|_{M^1} ∈
C^∞(M^1; ΛF^1)`, giving the canonical SES
`0 → { α ∈ I(M,M^0;ΛF) | supp α ⊂ M^0 } → I(M,M^0;ΛF) → { α|_{M^1} | α ∈ I(M,M^0;ΛF) }
→ 0`, with a (non-canonical) continuous section, hence a direct-sum decomposition of
`H-bar(I(M,M^0;ΛF), d_F)`. One defines `L(φ)` on each summand separately and studies the
two trace formulas.

**Term supported on `M^0` (the fixed-point / archimedean term).** Assume `F`
transversely oriented ⟹ `∃ ω, η ∈ C^∞(M; Λ^1 M)` with `TF = ker ω` and `dω = ω ∧ η`;
transversely affine ⟹ can take `dη = 0`. Using `δ`-sections at `M^0` and their
transverse derivatives:
`{ α ∈ I(M,M^0;ΛF) | supp α ⊂ M^0 } ≅ ⊕_{k≥0} C^∞(M^0; Λ M^0 ⊗ Ω^{-1} N M^0)`, with
`d_F = ⊕_{k≥0} (d_{M^0} + k η∧)`. **These are Novikov complexes on the compact manifold
`M^0`** (the `k η∧` twist is the Novikov / Morse-deformation term). The `⊕_k` graded
structure (a geometric series over `k`) is the analytic origin of the archimedean
`1/(1 - e^{κt})` factor: the Γ-factor as a sum over transverse jets `k`. The slides mark
the fixed-point contributions "Expected contributions?" -- this is the open computation.

**Term supported on `M^1` (the b-calculus / Melrose side -- new and not in the prior
note).** `F` is almost without holonomy (only the compact `M^0`-leaves have holonomy).
"Cutting" `M` through `M^0` gives a finite union of compact foliated manifolds WITH
BOUNDARY `(M_l, F_l)`, `M^1 ≡ ⊔_l M̊_l`, `F^1 ≡ ⊔_l F̊_l` (Hector). There is a
bundle-like metric `g^1` for `(M^1, F^1)` of bounded geometry, and the Hodge isomorphism
`H-bar(H^∞(M^1; ΛF^1), d_{F^1}) ≅ ⊕_l H-bar(H^∞(M̊_l; ΛF̊_l), d_{F̊_l}) ≅
⊕_l ker Δ_{F̊_l}`. Then `A_f` is defined on each `L^2(M̊_l; ΛF̊_l)`. **Difficulty:**
`M^1` is not compact ⟹ smoothing operators are NOT trace class. **Fix:** take `g^1` to
be a b-metric on the manifolds-with-boundary `M_l` (Melrose b-calculus, 1993); then
`A_f ∈ Ψ_b^{-∞}(M_l; ΛF_l)`, and `A_f` has a b-trace `bTr^s(A_f)`, a part of `L(φ)`.
**The key anomaly:** the b-trace is NOT a trace -- `bTr[A, B] ≠ 0`. The `M^1`
contribution is therefore "contribution of the closed orbits + extra term," and the
extra term (from the b-trace anomaly at the boundary `= M^0`) is again a fixed-point /
archimedean contribution. There is a defining function `ρ ∈ C^∞(M_l)` with
`∂M_l = {ρ = 0}`, `dρ ≠ 0`, `dρ = ρ η`; then
`{ α|_{M^1} | α ∈ I(M,M^0;ΛF) } = ⊕_l ∪_{m≥0} ρ^{-m} H^∞(M̊_l; ΛF̊_l)`, and
multiplication by `ρ^m` gives `(ρ^{-m} H^∞(M̊_l; ΛF̊_l), d_{F̊_l}) ≅
(H^∞(M̊_l; ΛF̊_l), d_{F̊_l} + m η∧)` -- again a Novikov perturbation. **Status (closing
slides):** "We solved the case where `m = 0` with the above argument using `A_f`";
the Novikov-complex versions (`m ≥ 1`) and the final fixed-point contribution are in
progress.

## Points mapped to the project

1. **The precise foliated-flow trace formula being proved.** `L(φ) := Tr^s(φ^*) ∈
   C^{-∞}(R)`, target on `R^+`: `Σ_c l(c) Σ_{k≥1} ε_{kl(c)}(c) δ_{kl(c)} + Σ_p ε_p /
   |1 - e^{κ_p t}|`, credited to Guillemin-Sternberg and C. Deninger (ICM 1998),
   motivated by "Deninger's program needs a version for foliated spaces."
   -> The exact Direction 4.6 target distribution, the foliated form of the explicit
   formula (1998 formula (5)/(22), 2002 formula (26), 2005 formula (32)). The
   closed-orbit term is the `Σ_p log p Σ_k δ_{k log p}` von Mangoldt side (2R's
   orbit-length spectrum); the fixed-point term `ε_p / |1 - e^{κ_p t}|` is the
   archimedean Γ-factor (2I / `A_arch`). The slides name Deninger's program as the
   motivation, so this is self-consciously the machinery for Direction 4.6.

2. **The simplicity hypotheses + the `M = M^0 ⊔ M^1` split.** Closed orbits simple
   (`det(id - φ^ℓ_*|T_xF) ≠ 0`, `ε_ℓ(c) = sgn det`); fixed points simple
   (`det(id - φ^t_*|T_pM) ≠ 0`, `ε_p = sgn det`, `φ-bar^t_* = e^{κ_p t}` on `N_pF`,
   `M^0` a finite union of compact leaves); `φ^t ⫛ F` on `M^1`.
   -> The non-degeneracy conditions of the 1998/2002 conjectures made precise. The split
   `M = M^0 ⊔ M^1` is the key device: `M^1` carries the closed-orbit / Riemannian /
   finite-prime analysis, `M^0` the fixed-point / archimedean analysis. For the
   arithmetic dictionary `M^0` = the archimedean place(s), `M^1` = the finite primes;
   `κ_p` is the archimedean weight `κ = -2` (real) / `-1` (complex) of the explicit
   formula.

3. **Leafwise Hodge isomorphism (the finiteness / trace-class enabler).** For ANY
   Riemannian foliation on a closed manifold, any codimension: bundle-like metric ⟹
   `Δ_F` symmetric in `L^2`, `H = ker Δ_F`, `Π: C^∞ → H` inducing `H-bar(F) ≅ H`
   (ALK 2001).
   -> The cited "[A-K00]" Hodge machinery behind Leichtnam 2006's `H^1_τ` and Deninger
   2002/2005's leafwise-Hodge package. It is why reduced leafwise cohomology is a
   Hilbert space with a well-defined trace at all. Direction 4.3 (finiteness) is exactly
   `H-bar(F) ≅ ker Δ_F` plus the trace-class statement in point 4. The generality
   (arbitrary codimension, any Riemannian foliation) is why it is the foundational lemma
   the whole program leans on.

4. **The non-singular trace-class theorem (ALK 2002).** `A_f = ∫_R φ^{t*} f(t) dt ∘ Π`
   is SMOOTHING (hence trace class), even though `φ^{t*} ∘ Π` is not; on `R^+`,
   `L(φ) = Σ_c l(c) Σ_{k≥0} ε_c(kl(c)) δ_{kl(c)}`.
   -> The precise hypothesis-and-mechanism for Direction 4.3 in the no-fixed-point case.
   The mechanism (smearing in `t` against `f(t) dt` plus harmonic projection `Π`) is the
   analytic content under Leichtnam 2006's "contraction process makes `∫ α(s)(φ^t)^* ds
   ∘ π^j_τ` trace class." It tells a Direction-4.6 builder the exact object to model:
   not `φ^{t*}` but its `f`-smearing composed with `Π`.

5. **The fixed-point obstruction and the conormal-distribution fix.** With `M^0 ≠ ∅`:
   `F` not Riemannian, transversely affine almost without holonomy, and the Schwartz
   kernel of `A_f` not smooth at `M^0`; the fix is the conormal complex
   `I(M, M^0; ΛF)` (Sobolev-graded distributional leafwise forms), with `d_F` extended
   to `C^{-∞}` and reduced cohomology `H-bar(I(M,M^0;ΛF), d_F)`.
   -> The precise statement of why fixed points are the hard part of Direction 4.3/4.6,
   and the team's strategy. Exactly the gap Deninger 2002 (`α=0` / no-fixed-point) and
   Leichtnam 2006 (assumption only at `g = 1`) left open. The archimedean place IS a
   fixed point, so the non-singular ALK 2002 theorem alone cannot give the full explicit
   formula; this conormal complex is the route to including the `p=∞` Γ-factor term
   rigorously. The "transversely affine, almost without holonomy" geometry near `M^0` is
   a concrete model for the archimedean local structure.

6. **The canonical SES + the `M^0`-supported Novikov term.** SES `0 → {supp ⊂ M^0} →
   I(M,M^0;ΛF) → {α|_{M^1}} → 0`, with a continuous section ⟹ direct-sum decomposition;
   the `M^0`-supported piece `≅ ⊕_{k≥0} C^∞(M^0; ΛM^0 ⊗ Ω^{-1} NM^0)` with
   `d_F = ⊕_k (d_{M^0} + k η∧)` (Novikov complexes on `M^0`).
   -> The strategy is "split the trace formula into a transversal (closed-orbit /
   finite-prime) part and a fixed-point (archimedean) part, and handle each." The
   `⊕_k (d_{M^0} + k η∧)` graded structure (a geometric series over the transverse jet
   index `k`) is the analytic origin of the archimedean `1/(1 - e^{κt})` factor: the
   Γ-factor as a sum over transverse jets. This is the cleanest available picture of how
   the archimedean term (2I) arises inside the trace formula.

7. **The `M^1` b-calculus side: where the extra (archimedean) term actually appears.**
   Cutting `M` through `M^0` gives manifolds-with-boundary `(M_l, F_l)`; a b-metric
   (Melrose 1993) makes `A_f ∈ Ψ_b^{-∞}`, with a b-trace `bTr^s(A_f)`; the anomaly
   `bTr[A, B] ≠ 0` means the `M^1` contribution is "closed orbits + extra term," the
   extra term coming from the boundary `= M^0`.
   -> This is the part the prior note missed entirely, and it is structurally important:
   the archimedean / fixed-point contribution shows up TWICE -- once as the
   `M^0`-supported Novikov term and once as the b-trace anomaly on `M^1` -- which is why
   the fixed-point case is genuinely harder than just "add a stationary term." For the
   program it identifies the precise analytic object (the Melrose b-trace defect at the
   archimedean boundary) that a project-native model of the Γ-factor term must reproduce.
   The defining function `ρ` with `dρ = ρ η` and the `ρ^{-m} H^∞ ≅ (H^∞, d + m η∧)`
   Novikov perturbation is the concrete mechanism.

## What this changes for the program

- **Direction 4.3 (finiteness / trace class) has a precise, two-regime status.**
  Non-singular regime (finite primes only): SOLVED by ALK 2002 (`A_f = ∫ φ^{t*} f dt ∘
  Π` smoothing). Singular regime (with the archimedean fixed point): IN PROGRESS via the
  conormal complex `I(M,M^0;ΛF)` on `M^0` AND the b-calculus on `M^1`. This note is the
  citation for both the solved part and the live attack on the open part.
- **The archimedean place IS the fixed-point difficulty, and it is doubly hard.** The
  Γ-factor is not a hand-added piece; it is the trace contribution of the flow's fixed
  point `M^0`, and it appears both as the `⊕_k (d_{M^0} + k η∧)` Novikov term (the
  `1/(1-e^{κt})` geometric series) AND as the Melrose b-trace anomaly `bTr[A,B] ≠ 0` at
  the boundary. The reason it is analytically hard (non-smooth Schwartz kernel,
  non-Riemannian `F` near `M^0`, non-compact `M^1`) is the same reason the archimedean
  place resists a clean cohomological treatment.
- **It tells a Direction-4.6 builder exactly what to model.** The object is the smeared,
  harmonic-projected operator `A_f`, not `φ^{t*}`; trace class comes from smearing in
  `t` plus `Π`; with fixed points one needs distributional forms conormal to `M^0` and a
  b-metric on the cut-open `M^1` whose b-trace anomaly carries the extra term. Any
  project-native model of the trace formula should reproduce this structure.
- **It is "work in progress" / a slide deck, not a finished theorem.** Honest caveat:
  the general (fixed-point) case is presented as a strategy with the key constructions
  stated and the `m = 0` case solved, but the final trace-formula computation on the
  `M^0` summand (the "Expected contributions?") and the `m ≥ 1` Novikov versions left in
  progress. So for the program, the singular case is "machinery identified and under
  construction," not "available off the shelf." This matches the in-house reading that
  the archimedean / fixed-point step is the open analytic frontier.
- **D-H discipline.** The trace formula's closed-orbit spectrum `{l(c)} = {log Np}` is an
  Euler-product fingerprint; the Davenport-Heilbronn function has no Euler product and no
  primitive-orbit spectrum (the 2R / Leichtnam 2006 finding). This machinery is on the
  right side of the wrong-approach detector: it engages the orbit spectrum that
  distinguishes zeta from D-H.

## Actionable

- Cite this as the precise reference for: (a) the non-singular trace-class mechanism
  `A_f = ∫ φ^{t*} f dt ∘ Π` smoothing (Direction 4.3, finite-prime regime); (b) the
  conormal-distribution complex `I(M,M^0;ΛF)` and its `⊕_k (d_{M^0} + k η∧)`
  `M^0`-supported Novikov piece (the strategy for the archimedean fixed-point regime);
  and (c) the Melrose b-calculus on the cut-open `M^1` with the b-trace anomaly
  `bTr[A,B] ≠ 0` as the source of the extra fixed-point term.
- The `⊕_k (d_{M^0} + k η∧)` graded `M^0`-complex and the `ρ^{-m} H^∞ ≅ (H^∞, d + m η∧)`
  Novikov perturbation are the concrete objects to study if the program wants to derive
  the archimedean `1/(1 - e^{κt})` Γ-factor term from the flow rather than assume it.
  Pair with Deninger 2005 Prop 3.1 (the Γ-factor as `det_inf` on `R[exp(-2y)]`): both are
  "Γ-factor as a sum / product over transverse jets `k`."
- Track whether the finished paper appears (this is 2017 "in progress," `m = 0` solved):
  a completed general-case trace formula would be the first rigorous foliated explicit
  formula including the archimedean place, a direct Direction-4.6 deliverable. No project
  computation follows directly; this is analytic / structural input.

## Status

Read the full slide deck (cover, contents, and all build-stages of: "Foliated flows,"
"Hypotheses," the torus example, "The problem of the trace formula," "Motivation,"
"Non-singular foliated flows," "Leafwise Hodge isomorphism," the 2002 non-singular
"Lefschetz trace formula," "Difficulties," "Distributional leafwise forms conormal to
`M^0`," "Canonical short exact sequence," "Term supported on `M^0`," the full "Term
supported on `M^1`" b-calculus sequence (cutting `M` through `M^0`, the b-metric,
`A_f ∈ Ψ_b^{-∞}`, the b-trace anomaly `bTr[A,B] ≠ 0`, the defining function `ρ` and the
`ρ^{-m} H^∞ ≅ (H^∞, d + m η∧)` Novikov perturbation), and the closing "m = 0 solved"
slide). Honest depth: this is a presentation, so the trace-class claims, the leafwise
Hodge isomorphism, and the b-calculus statements are given with their mechanism but
without full analytic proofs (those live in the ALK 2001/2002 papers, Melrose's
b-calculus, and the eventual full article). The general (fixed-point) case is explicitly
"work in progress" with only the `m = 0` case solved as of the talk.
