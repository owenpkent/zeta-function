# Reading notes (ROLE-note, deep): Moore-Schochet, *Global Analysis on Foliated Spaces* (MSRI 9, 2nd ed., 2006)

> Entry in the reference-library read-through
> ([`references/README.md`](../../../references/README.md)). A ~300-page textbook, not a
> paper. ROLE-note: identifies which chapters supply the standard machinery the project's
> foliated-flow Direction (4.3-4.6) needs, with the key definitions/theorems stated
> precisely from the Introduction (which gives a full technical summary, not just chapter
> titles). It is the canonical reference for **leafwise (tangential) cohomology,
> transverse measures + the Ruelle-Sullivan current, the Riesz representation theorem for
> invariant transverse measures, and the Connes measured-foliation index theorem**, the
> well-founded template under Leichtnam 2006 and the project's Direction-4.6 trace-formula
> goal. Read: contents p.ix, both prefaces, and the Introduction in depth (pp.1-10 of the
> PDF: foliated-space definition, tangential cohomology + the non-Hausdorff / Hausdorff-
> quotient phenomenon, locally-traceable operators + local index as a tangential measure,
> transverse measures + Ruelle-Sullivan current, the Riesz representation theorem
> `MT(X) ~ H^tau_p(X)`, the Connes Index Theorem, the Connes-Skandalis sharpening, plus
> the chapter-by-chapter summaries I-VIII). Pages refer to the PDF in
> `references/03_foliated_cohomology_trace/`.

## One-line takeaway

The self-contained reference for analysis on foliated SPACES (local model `R^p x N`, `N`
a separable metric space, not necessarily a manifold, so it covers laminations /
solenoids / Cantor-transversal spaces -- exactly the arithmetic-flow setting). It builds
tangential cohomology `H^*_tau(X)`, transverse measures + the Ruelle-Sullivan current
`C_nu`, leafwise characteristic classes, the leafwise heat-equation / pseudodifferential
calculus, and proves the **Connes Index Theorem** `ind_nu(P) = <ch(P) Td(M), [C_nu]>` for
a tangentially elliptic operator against an invariant transverse measure. The crucial
structural facts for the project: tangential cohomology is generically **infinite-
dimensional and non-Hausdorff** (the irrational flow on `T^2` has `H^1_tau` infinite-dim
but `H-bar^1_tau = R`), and the index is a **real (non-integer) number** = a tangential
measure paired with the Ruelle-Sullivan current. This is the Direction-4.3-to-4.6 machinery
(finiteness, leafwise de Rham, duality, the trace formula) in textbook form, stopping at
the index (a trace), NOT the signature (Direction 8).

## Technical content (chapter map, with precise statements)

**Introduction (pp.1-10).** Frames everything around the **Connes Index Theorem**:
- **Foliated space** (def, Intro p.3): a separable metrizable `X` with a regular foliated
  atlas whose charts `phi_alpha: U_alpha -> L_alpha x N_alpha` (`L = R^p`, `N` a separable
  metric space, NOT necessarily a manifold) have tangentially smooth transitions. Leaves
  are smooth `p`-manifolds; there is a tangent bundle `FX -> X`. A solenoid (leaves dim 1,
  `N` = Cantor set), a lamination, `prod_1^infinity S^1` foliated by lines (with
  `{1} x prod_2^infinity S^1` a transversal) are foliated SPACES, not manifolds. This
  "`N` any separable metric space" generality is why this book, not manifold-only
  Atiyah-Singer, is the right reference for arithmetic-flow spaces.
- **Holonomy groupoid `G(X)`** (Intro p.5): triples `(x, y, [alpha])`, `x,y` on a leaf,
  `[alpha]` a holonomy class of a path; a (possibly non-Hausdorff) foliated space. For a
  complete transversal `N`, `G_N^N` is a discrete model.
- **Tangential / leafwise cohomology** (Intro p.4): `Omega^k_tau(X) = Gamma_tau(Lambda^k
  F*)` (forms smooth ALONG leaves, only CONTINUOUS transversally); `H^k_tau(X) =
  H^k(Omega^*_tau(X)) = H^k(X : R_tau)`, `R_tau` the sheaf of germs locally constant along
  leaves. Vanishes for `k > p`; has Mayer-Vietoris, suspension/Thom isomorphisms. Crucially
  **generally NON-Hausdorff**; one passes to the maximal Hausdorff quotient `H-bar^k_tau(X)
  = H^k_tau(X)/closure{0}`. **Example: irrational flow on `T^2` -> `H^1_tau` infinite-
  dimensional but `H-bar^1_tau = R`** (Intro p.4).
- **Locally traceable operators + local index** (Intro pp.5-6): for a tangential,
  tangentially elliptic `D`, `Ker D_l` and `Ker D_l*` may be infinite-dimensional so
  `dim Ker D_l - dim Ker D_l*` is meaningless; but they are LOCALLY finite-dimensional, so
  the local index `iota_{D_l} = mu_{Ker D_l} - mu_{Ker D_l*}` is a signed Radon measure on
  the leaf, and `iota_D = {iota_D^x}` is a **tangential measure** (a family of Radon
  measures on leaves with Borel-invariance, Def 4.11), the abstract **analytic index** of
  `D`. If `F` is oriented, `iota_D` defines a class in `H-bar^p_tau(X)`.
- **Transverse measures** (Intro p.6): for a Borel equivalence relation with a cocycle
  `Delta in Z^1(R, R*)`, a transverse measure of modulus `Delta`; `Delta = 1` gives an
  **invariant** transverse measure. `MT(X)` = the space of invariant transverse measures.
- **Ruelle-Sullivan current + Riesz representation** (Intro pp.6-7, p.9): the integration
  process `(lambda, nu) -> lambda d nu -> int lambda d nu` produces, from an invariant
  transverse measure `nu`, the **Ruelle-Sullivan current `C_nu` in `Omega^tau_p(X)`** (a
  cycle iff `nu` is invariant). The pairing `MT(X) x Omega^p_tau(X) -> R` gives the
  **Ruelle-Sullivan map `MT(X) -> Hom_cont(H^p_tau(X), R) = H^tau_p(X)`. Riesz
  representation theorem: this map is an ISOMORPHISM** (Intro p.7). Consequence: `X` has
  no invariant transverse measure iff `H-bar^p_tau(X) = 0`.
- **The Connes Index Theorem** (Intro pp.2, 7): for `D` tangential tangentially elliptic
  on a compact oriented foliated space, and `nu` an invariant transverse measure,
  `ind_nu(P) = phi_nu(ind P) = int iota_D d nu = int iota_D^top d nu`, where `iota_D^top =
  +/- [Phi_tau^{-1} ch_tau(D)] Td_tau(X)`. Reformulated via Riesz: `[iota_D] = [iota_D^top]
  in H-bar^p_tau(X)`. The index is a **real number** (not integer) when `[C_nu]` is not
  rational. (If `X` has no invariant transverse measure, `H-bar^p_tau(X) = 0` and `iota_D
  in {0}`.)
- **Connes-Skandalis sharpening** (Intro p.8): the reduced `C*`-algebra `C*_r(G(X))` with
  the pseudodifferential extension `0 -> C*_r(G(X)) -> P-bar^0 -> Gamma(S*F, End E) -> 0`,
  so the tangential symbol gives a class in `K_0(C*_r(G(X)))`; even with an invariant
  transverse measure, if the symbol has finite order in `K_0(C*_r(X))` then `[iota_D] = 0`
  in `H^p_tau(X)`. The Type-III situation appears here.

**Chapter I, Locally Traceable Operators (pp.13-30).** The local trace `mu_T` of a positive
operator `T` on `L^2(Y,E)` via `Trace(f^{1/2} T f^{1/2}) = int f d mu_T`; the local index
`iota_D` of an elliptic operator on a noncompact manifold; the formal degree of a
representation of a unimodular group in these terms. The analytic foundation for "index =
a measure" rather than "index = an integer."

**Chapter II, Foliated Spaces (pp.31-54). Background.** Topological foundations:
tangentially smooth partitions of unity, `K^0(X)` = subgroup generated by tangentially
smooth bundles, the holonomy groupoid `G(X)` and its discrete model `G_N^N`. The "`N` not
a manifold" generality is established here.

**Chapter III, Tangential Cohomology (pp.55-74). MATTERS for Direction 4.3-4.4.** Defines
`H^*_tau(X)` = cohomology of the leafwise de Rham complex = `H^*(X : R_tau)`; the
analogous compactly-supported `H^*_{tau c}` and vertical `H^*_{tau v}` theories on bundles;
Mayer-Vietoris, the **Kunneth isomorphism `H^*_tau(X) (x) H^*(M) ~ H^*_tau(X x M)`** (for
`M` a manifold foliated as one leaf), the **Thom isomorphism `Phi: H^k_tau(X) ~
H^{n+k}_{tau v}(E)`** for an oriented tangentially smooth `n`-plane bundle, and tangential
homology. The non-Hausdorff phenomenon and the `H-bar^*_tau` quotient live here.

**Chapter IV, Transverse Measures (pp.75-108). MATTERS for the trace / Direction 4.6.** The
general theory of groupoids (measurable + topological), transverse measures and their
integration with tangential measures `(lambda, nu) -> lambda d nu`, the **Ruelle-Sullivan
current `C_nu`** (cycle iff `nu` invariant), `MT(X)` vs invariant measures on a complete
transversal `N`, and the **Riesz representation theorem `MT(X) -> Hom_cont(H^p_tau(X), R)`
is an isomorphism**. This is the object that turns a leafwise operator into a NUMBER.

**Chapter V, Characteristic Classes (pp.109-128). MATTERS for duality / Direction 4.5.**
The Chern-Weil development of tangential characteristic classes: tangential Chern classes
`c_n^tau in H^{2n}_tau(X)`, Pontryagin `p_n^tau in H^{4n}_tau(X)`, the tangential Euler
class, the tangential Chern character and Todd genus relating the K-theory and tangential-
cohomology Thom isomorphisms (so `iota_D^top` is a well-defined form).

**Chapter VI, Operator Algebras (pp.129-166). Background.** The foliation `C*`-algebra
`C*_r(G(X))`; the **Hilsum-Skandalis isomorphism `C*_r(G(X)) ~ C*_r(G_N^N) (x) K`** ("the
foliated space fibres over a complete transversal `N` at the `C*`-algebra level"). An
invariant transverse measure `nu` induces a trace `phi_nu`; the von Neumann splitting
`W*(G(X)) ~ W*(G_N^N) (x) B(H)` is the ergodic II_infinity = II_1 (x) I_infinity
decomposition. The partial Chern character `c: K_0(C*_r(G)) -> H-bar^p_tau(X)`.

**Chapter VII, Pseudodifferential Operators (pp.167-208) + Chapter VIII, The Index Theorem (pp.209-224). MATTERS for Direction 4.6.** The leafwise pseudodifferential calculus
(parametrized to foliated spaces), the tangential principal symbol; VII-C **Dirac
operators + the McKean-Singer formula**, VII-D the heat-kernel asymptotic expansion. Chapter
VIII proves the Connes measured-foliation index theorem `ind_nu(P) = <ch(P) Td(M), [C_nu]>`
via the leafwise heat-equation method. This is the **worked, rigorous instance of a
Direction-4.6-type trace formula**: an index/trace of a leafwise elliptic operator as a
geometric integral against the transverse current. Leichtnam 2006 cites this machinery for
its conditional Lefschetz formula and `Re = 1/2`.

**Appendix A, the dbar-Operator (pp.225-247) (by Hurder). MATTERS for Direction 4.5.** The
leafwise `dbar` and A2 the **dbar-index theorem and Riemann-Roch** along leaves; A3
foliations by surfaces / complex lines (`k = 1`). The leafwise Riemann-Roch prototype (the
functional-equation row of the Weil dictionary). Appendix D (Gap Labeling, Bellissard) is
the tilings/quasicrystal application of the index theorem.

## Points mapped to the project

1. **Tangential cohomology `H^*_tau(X)` is the project's leafwise `H^*` (Direction 4.3-4.4, Ch. III).**
   Generically infinite-dimensional and non-Hausdorff before the maximal-Hausdorff quotient
   `H-bar^*_tau`. The irrational flow on `T^2` (`H^1_tau` infinite-dim, `H-bar^1_tau = R`)
   is the model. This is exactly the regime 2Q predicts for `Spec(Z)` (forced infinite-dim
   `H^i`): the infinite-dimensionality is the GENERIC foliated phenomenon, not a pathology;
   finiteness is recovered only after the Hausdorff quotient. The open question for the
   project is what plays the role of the transverse measure / Hausdorff quotient for
   `Spec(Z)`. The `R_tau` sheaf (locally constant along leaves) is the leafwise analogue of
   the constant sheaf a Lefschetz formula would trace ->

2. **Transverse measures + Ruelle-Sullivan current = the trace / Direction 4.6 (Ch. IV, intro pp.6-7).**
   An invariant transverse measure `nu` induces the Ruelle-Sullivan current `C_nu` and a
   trace `phi_nu` (Ch. VI); this is the object that turns a leafwise operator into a number.
   Direction 4.6 (regularized determinant / Lefschetz) needs precisely such a transverse
   measure to define the trace whose value is the explicit-formula / von Mangoldt sum (2R).
   Connes-1994 Ch. I §5 and this chapter are the same construction; Moore-Schochet is the
   detailed reference ->

3. **The Riesz representation theorem `MT(X) ~ H^tau_p(X)` is the finiteness control (Ch. IV, intro p.7).**
   `MT(X) -> Hom_cont(H^p_tau(X), R)` is an isomorphism, and `X` has no invariant transverse
   measure iff `H-bar^p_tau(X) = 0`. This pins the existence of a trace to the (Hausdorff-
   quotiented) top tangential cohomology. For the project: whether `Spec(Z)`-as-foliated-
   space admits an invariant transverse measure is the same question as whether its top
   `H-bar^p_tau` is nonzero, i.e. the Direction-4.3 finiteness question reframed ->

4. **The Connes Index Theorem is the worked Direction-4.6 trace formula (Ch. VIII, intro pp.2,7).**
   `ind_nu(P) = int iota_D d nu = <ch(P) Td(M), [C_nu]>`, a real (non-integer) number =
   the analytic index (a tangential measure) paired with the Ruelle-Sullivan current. This
   is the rigorous instance of "index/trace of a leafwise elliptic operator = geometric
   integral against the transverse current," the template Leichtnam 2006 specializes to get
   `Re = 1/2`. The McKean-Singer / heat-kernel route (VII-C,D) is the concrete analytic
   technique a 4.6 attempt would model. The non-integer index is the continuous-dimension /
   2Q infinite-dimensional regime made quantitative ->

5. **Leafwise Riemann-Roch (App. A2) is the duality prototype (Direction 4.5).** The
   leafwise `dbar`-index theorem / Riemann-Roch is the functional-equation row of the Weil
   dictionary realized on leafwise cohomology. Distinct from the signature / Hodge-index
   (Direction 8), which this book does NOT provide ->

6. **`N` not a manifold = why this is the right reference (Ch. II, intro p.3).** The
   arithmetic foliated spaces (Leichtnam's `D x Z_p^m` transversal, solenoids, Cantor
   transversals, `prod S^1`) are foliated SPACES, not foliated manifolds. Manifold-only
   Atiyah-Singer does not cover them; Moore-Schochet does. The Hilsum-Skandalis "fibres over
   a complete transversal" (Ch. VI) and the II_infinity = II_1 (x) I_infinity splitting are
   the structural facts behind the type-III/II_infinity types that recur on the arithmetic
   front ->

## What this changes for the program

- **It is the rigorous toolbox under the foliated-flow Direction, not a new result.**
  Direction 4.3 (finiteness) = the maximal-Hausdorff-quotient `H-bar^*_tau` story + the
  Riesz `MT(X) ~ H^tau_p(X)` criterion (Ch. III, IV). Direction 4.4 (the cohomology) =
  tangential cohomology (Ch. III). Direction 4.5 (duality) = leafwise Riemann-Roch /
  characteristic classes (Ch. V, App. A). Direction 4.6 (trace formula) = the Connes
  measured-foliation index theorem (Ch. VIII) against the Ruelle-Sullivan current (Ch. IV).
  Cite by chapter.
- **Infinite-dimensional / non-Hausdorff cohomology is normal here, and that is the point.**
  2Q forces infinite-dim `H^i` over `Spec(Z)`; Moore-Schochet shows this is the generic
  foliated situation (irrational flow on `T^2`), with finiteness recovered only after the
  Hausdorff quotient. The project's infinite-dimensionality is the expected leafwise
  phenomenon; the open question is the transverse measure / Hausdorff quotient for
  `Spec(Z)`, equivalently whether `H-bar^p_tau != 0` (Riesz).
- **This book gives the trace and the index, NOT the signature.** The Hodge-index /
  Castelnuovo positivity (Direction 8) is not in here; Moore-Schochet stops at the Connes
  index theorem (a trace, a real number), which is the Direction-4.6 level. The signature
  step remains the separate, harder gap, consistent with the Leichtnam note's observation
  that `Re = 1/2` from the flow is spectral, not a signature.

## Actionable

- No line-by-line read warranted now. If Direction 4.3 (finiteness) becomes active, read
  Chapter III (tangential cohomology, the non-Hausdorff / Hausdorff-quotient mechanism,
  ~20 pp) together with the Riesz theorem in Chapter IV. If Direction 4.6 (trace formula)
  becomes active, read Chapter IV (transverse measures / Ruelle-Sullivan, ~34 pp) then
  Chapter VIII (the index theorem, ~16 pp) with VII-C,D (heat kernel / McKean-Singer) as
  the analytic technique.
- The single most useful fact to carry forward: the index is a tangential MEASURE paired
  with the Ruelle-Sullivan current (a real number), and its existence is equivalent (Riesz)
  to `H-bar^p_tau(X) != 0`. So the project's "does `Spec(Z)` carry a trace formula" question
  and its "is the top tangential cohomology nonzero / finite" question are the same question.
- Keep this note as the index into the textbook; it is the reference Leichtnam 2006 and any
  Direction-4.x experiment should be checked against for the standard definitions.

## Status

ROLE-note (deep). Read: contents p.ix, both prefaces (which credit Connes' 1979 foliated
index theorem as the centerpiece and note the extra "foliated space" generality is needed
for the Gap Labeling application), and the Introduction in depth (PDF pp.1-10: foliated-
space definition, tangential cohomology + non-Hausdorff / Hausdorff-quotient phenomenon,
locally traceable operators + local index as a tangential measure, transverse measures +
Ruelle-Sullivan current, the Riesz representation theorem `MT(X) ~ H^tau_p(X)`, the Connes
Index Theorem statement, the Connes-Skandalis sharpening, plus the chapter-by-chapter
summaries I-VIII). Chapter bodies NOT read; the stated definitions and theorems are taken
from the Introduction's own technical summaries. Honest depth: a navigation note that now
carries the precise statements (tangential cohomology = `H^*(X : R_tau)`, the `T^2`
infinite-dim / `H-bar^1 = R` example, the Ruelle-Sullivan map = Riesz isomorphism, the
index theorem `ind_nu = <ch Td, [C_nu]>`, the index is a real number, the Hilsum-Skandalis
fibring), mapping the project's Direction-4.3-to-4.6 needs onto specific chapters (III, IV,
V, VII, VIII, App. A), not a content summary of any chapter body.
