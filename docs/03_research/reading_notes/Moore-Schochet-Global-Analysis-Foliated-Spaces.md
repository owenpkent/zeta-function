# Reading notes (ROLE-note): Moore-Schochet, *Global Analysis on Foliated Spaces* (MSRI 9, 2nd ed., 2006)

> Entry in the reference-library read-through
> ([`references/README.md`](../../../references/README.md)). This is a 300-page
> textbook, not a paper. This is a ROLE-note: it identifies which chapters supply the
> standard machinery the project's foliated-flow Direction (4.3-4.5) needs, read via
> the table of contents (p.ix) and the Introduction (pp.1-4) plus the two prefaces,
> NOT read through. It is the canonical reference for **leafwise (tangential)
> cohomology, transverse measures, and the Connes measured-foliation index theorem**,
> which is the well-founded template under Leichtnam 2006 and the project's Direction
> 4.6 trace-formula goal. Pages refer to the PDF in
> `references/03_foliated_cohomology_trace/`.

## One-line takeaway

The standard, self-contained reference for analysis on foliated SPACES (local model
`R^p x N` with `N` a separable metric space, not necessarily a manifold, so it covers
laminations / solenoids / Cantor-transversal spaces, which is exactly the
arithmetic-flow setting). It builds tangential cohomology `H^*_tau(X)`, transverse
measures and the Ruelle-Sullivan current, characteristic classes, the leafwise
heat-equation / pseudodifferential calculus, and proves the **Connes Index Theorem**
`ind_nu(P) = <ch(P) Td(M), [C_nu]>` for a tangentially elliptic operator against an
invariant transverse measure. This is the Direction-4.3-to-4.5 machinery (finiteness,
the leafwise Hodge/de Rham analogue, duality) in textbook form.

## Chapter map: what matters for the project

1. **Chapter III, Tangential Cohomology (pp.55-74). MATTERS for Direction 4.3-4.4.**
   Defines tangential (leafwise) cohomology `H^k_tau(X) = H^k(Omega^*_tau(X))` from
   forms that are smooth ALONG leaves and only CONTINUOUS transversally (Intro p.4).
   Equals `H^k(X : R_tau)` with `R_tau` the sheaf of germs locally constant along
   leaves. Vanishes for `k > p`; has long exact sequences, Thom isomorphism. Crucially
   it is generally **non-Hausdorff**; one passes to the maximal Hausdorff quotient
   `H-bar^k_tau(X) = H^k_tau(X)/closure{0}`. Example: irrational flow on `T^2` gives
   `H^1_tau` infinite-dimensional but `H-bar^1_tau = R` (Intro p.4).
   -> This is the project's leafwise `H^*` (Direction 4.3 finiteness, 4.4 the cohomology
   itself). The non-Hausdorff phenomenon and the infinite-dimensionality of `H^1_tau`
   before quotienting is exactly the regime 2Q predicts for `Spec(Z)` (forced
   infinite-dim `H^i`). The maximal-Hausdorff-quotient step is the analytic form of the
   "finiteness" the project keeps needing and Leichtnam's Assumption (iv) supplies only
   at genus 1. The `R_tau` (locally-constant-along-leaves) sheaf is the leafwise
   analogue of the constant sheaf whose cohomology a Lefschetz formula would trace.

2. **Chapter IV, Transverse Measures (pp.75-108). MATTERS for the trace / Direction 4.6.**
   Holonomy-invariant transverse measures, the **Ruelle-Sullivan current** `C_nu`, and
   the trace `phi_nu` on the foliation algebra they induce (Intro p.2).
   -> This is the object that turns a leafwise operator into a NUMBER (a trace), the
   analytic heart of any trace formula. The project's Direction 4.6 (regularized
   determinant / Lefschetz) needs precisely an invariant transverse measure to define
   the trace whose value is the explicit-formula / von Mangoldt sum (2R). Connes-1994
   Ch. I §5 and this chapter are the same construction; Moore-Schochet is the detailed
   reference.

3. **Chapter VIII, The Index Theorem (pp.209-224) + Chapter VII, Pseudodifferential Operators (pp.167-208). MATTERS for Direction 4.6.**
   The Connes measured-foliation index theorem `ind_nu(P) = <ch(P) Td(M), [C_nu]>`
   (Intro p.2), built on the leafwise heat-equation method (VII-C Dirac operators and
   the McKean-Singer formula, VII-D the asymptotic expansion).
   -> This is the **worked, rigorous instance of a Direction-4.6-type trace formula**:
   an index/trace of a leafwise elliptic operator expressed as a geometric integral
   against the transverse current. Leichtnam 2006 cites this machinery ([A-K00]/Connes)
   to get its conditional Lefschetz formula and `Re = 1/2`. The McKean-Singer / heat-
   kernel route (VII-C,D) is the concrete analytic technique a 4.6 attempt would model.

4. **Chapter V, Characteristic Classes (pp.109-128) + Appendix A (the dbar-operator, A2 the dbar-index theorem and Riemann-Roch, pp.225-247). MATTERS for duality / Direction 4.5.**
   Leafwise characteristic classes; the leafwise `dbar` and a Riemann-Roch / index
   statement along the leaves.
   -> Direction 4.5 wants a Poincare-duality / Riemann-Roch analogue on the leafwise
   cohomology (the functional-equation row of the Weil dictionary). Appendix A2 is the
   leafwise Riemann-Roch prototype. This is the duality machinery, distinct from the
   signature/Hodge-index (Direction 8) which this book does NOT provide.

5. **Chapter VI, Operator Algebras (pp.129-166) + Chapter II, Foliated Spaces (pp.31-54) + Chapter I, Locally Traceable Operators (pp.13-30). Background.**
   The foliation `C*`/von Neumann algebra (`C*_r(G(M))`, `K_0` as index home, Intro
   p.2), the precise definition of a foliated space (local model `R^p x N`, `N` any
   separable metric space, Intro p.3), and the locally-traceable-operator definition of
   the analytic index.
   -> The "`N` not necessarily a manifold" generality (II) is exactly why this book,
   not the manifold-only Atiyah-Singer, is the right reference: the arithmetic foliated
   spaces (Leichtnam's `D x Z_p^m` transversal, solenoids, Cantor transversals) are
   foliated SPACES, not foliated manifolds. Appendix D (Gap Labeling, Bellissard) is the
   tilings/quasicrystal application, tangential here.

## What this changes for the program

- **It is the rigorous toolbox under the foliated-flow Direction, not a new result.**
  Direction 4.3 (finiteness) = the maximal-Hausdorff-quotient `H-bar^*_tau` story
  (Ch. III). Direction 4.4 (the cohomology) = tangential cohomology (Ch. III).
  Direction 4.5 (duality) = leafwise Riemann-Roch / characteristic classes (Ch. V,
  App. A). Direction 4.6 (trace formula) = the measured-foliation index theorem
  (Ch. VIII) against the Ruelle-Sullivan current (Ch. IV). Cite by chapter.
- **The infinite-dimensional / non-Hausdorff cohomology is normal here, and that is the
  point.** 2Q forces infinite-dim `H^i` over `Spec(Z)`; Moore-Schochet shows this is the
  generic foliated situation (irrational flow on `T^2`), with the finiteness recovered
  only after the Hausdorff quotient. So the project's infinite-dimensionality is not a
  pathology, it is the expected leafwise phenomenon, and the open question is what plays
  the role of the transverse measure / Hausdorff quotient for `Spec(Z)`.
- **This book gives the trace and the index, NOT the signature.** The Hodge-index /
  Castelnuovo positivity (Direction 8) is not in here; Moore-Schochet stops at the index
  theorem (a trace), which is the Direction-4.6 level. The signature step remains the
  separate, harder gap, consistent with the Leichtnam note's closing observation that
  `Re = 1/2` from the flow is spectral, not a signature.

## Actionable

- No line-by-line read warranted now. If Direction 4.3 (finiteness) becomes active, the
  targeted read is Chapter III (tangential cohomology, the non-Hausdorff / Hausdorff-
  quotient mechanism, ~20 pp). If Direction 4.6 (trace formula) becomes active, read
  Chapter IV (transverse measures / Ruelle-Sullivan, ~34 pp) then Chapter VIII (the
  index theorem, ~16 pp) with VII-C,D (heat kernel / McKean-Singer) as needed.
- Keep this note as the index into the textbook; it is the reference Leichtnam 2006 and
  any Direction-4.x experiment should be checked against for the standard definitions.

## Status

ROLE-note. Read: contents p.ix, both prefaces (pp.xi-xiii, which credit Connes' 1979
foliated index theorem as the centerpiece), and the Introduction pp.1-4 (foliated-space
definition, tangential cohomology, transverse measures + Ruelle-Sullivan current, the
Connes Index Theorem statement). Chapter bodies NOT read; relevance assessed from the
TOC and the Introduction's own summaries. Honest depth: navigation note mapping the
project's Direction-4.3-to-4.6 needs onto specific chapters (III, IV, V, VII, VIII,
App. A), not a content summary of any chapter.
