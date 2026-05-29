# Reading notes (ROLE NOTE): Hartshorne, *Algebraic Geometry* (GTM 52, Springer 1977)

> Intersection/Hodge reference textbook. Folder
> [`references/06_intersection_hodge/`](../../../references/06_intersection_hodge/).
> This is a 496-page graduate textbook, NOT a paper. This is a ROLE NOTE: it records WHICH
> chapters serve Direction 8 and why, with the relevant chapter intros read, rather than a
> linear read-through. The single most relevant chapter is **Chapter V (Surfaces)**, whose
> §1 (Geometry on a Surface) is the classical intersection-theory-on-a-surface plus Hodge
> index theorem that the in-house 2G $C\times C$ template instantiates and that Direction 8
> must lift to $\mathrm{Spec}(\mathbb{Z})^2$. Pages refer to the PDF. Read: front matter +
> full TOC (pp.ix-xiv), and Chapter V intro + §1 "Geometry on a Surface" (pp.356-361, the
> intersection pairing Theorem 1.1 and its examples).

## One-line takeaway

Hartshorne Chapter V §1 gives the classical theory Direction 8 is trying to lift: on a
nonsingular projective surface there is a unique symmetric intersection pairing
$\mathrm{Div}\,X\times\mathrm{Div}\,X\to\mathbb{Z}$ (Theorem 1.1), and the Hodge index
theorem says this form has signature $(1,\rho-1)$ (one positive eigenvalue, the rest
negative). That signature on the surface $C\times C$ IS the Weil/Hasse-Weil bound (the
function-field RH), the 2G template. Direction 8 = lift this exact chapter to the arithmetic
surface $\mathrm{Spec}(\mathbb{Z})^2$.

## Chapter-by-chapter role map for Direction 8

1. **Chapter V, Surfaces (pp.356-453) is the core chapter.** The chapter intro (p.356) states
   it explicitly: "Sections 1, 3 and 5 are general. Here we develop intersection theory on a
   surface and prove the Riemann-Roch theorem. As applications we give the Hodge index theorem
   and the Nakai-Moishezon criterion for an ample divisor."
   -> Direction 8 is the lift of this chapter to $\mathrm{Spec}(\mathbb{Z})^2$. Everything the
   project's milestone names (intersection form, signature, primitive form negative definite)
   is classical content of Chapter V §1.

2. **§V.1 Geometry on a Surface (pp.357-368) is THE section.** Theorem 1.1 (p.357-358): there
   is a unique pairing $\mathrm{Div}\,X\times\mathrm{Div}\,X\to\mathbb{Z}$, $C.D$, that is
   (1) $=\#(C\cap D)$ for transversal nonsingular curves, (2) symmetric, (3) additive, (4)
   depends only on linear equivalence classes. Proposition 1.4 computes it locally; Example
   1.4.4 defines self-intersection and the canonical divisor $K$; Prop 1.5 is the adjunction
   formula $2g-2=C.(C+K)$. The Hodge index theorem itself is later in §1 (signature $(1,\rho-1)$
   of the form on $\mathrm{Num}\,X$).
   -> This is the exact object Direction 8 needs on the arithmetic surface: a symmetric
   $\mathbb{Z}$-valued intersection form, with a SIGNATURE. The in-house 2G result (primitive
   form on $C\times C$ negative definite = Hasse-Weil bound) is precisely the Hodge index
   theorem of this section applied to $X=C\times C$. The missing arithmetic object ($\Gamma_S$,
   2Q/2R) plays the role of a divisor/correspondence class on $X$ whose self-intersection
   $\Gamma_S^2 = -\zeta'/\zeta$ the form must control.

3. **Example V.1.4.3, the quadric surface $X=\mathbb{P}^1\times\mathbb{P}^1$ (p.361), is the
   baby $C\times C$.** $\mathrm{Pic}\,X=\mathbb{Z}\oplus\mathbb{Z}$ with classes $l$ (type
   $(1,0)$) and $m$ (type $(0,1)$); $l^2=0$, $m^2=0$, $l.m=1$, so the form is the hyperbolic
   plane $\binom{0\,1}{1\,0}$, signature $(1,1)$.
   -> This is the simplest product surface and the cleanest illustration of the Direction-8
   target: the intersection form on a PRODUCT of two curves is hyperbolic, the diagonal and
   the fibers are the natural classes, and the off-diagonal structure (the $l.m=1$) is the
   pairing that, for $C\times C$ with a Frobenius graph, becomes the function-field RH. The
   $(1,p)$ bidegree of $\Gamma_S$ (2Q) is the arithmetic echo of the $(a,b)$ bidegree
   bookkeeping in this example.

4. **§I.7 Intersections in Projective Space (pp.47-54) is the prerequisite / Bezout layer.**
   The chapter intro to V §1 (p.357) refers back to the intersection multiplicity defined in
   (I, Ex. 5.4) and (I, §7). §I.7 is where intersection numbers and Bezout's theorem are first
   set up classically.
   -> Background reading for the local intersection multiplicity $(C.D)_P$. Direction 8 needs
   the arithmetic analogue of local intersection multiplicity at each prime (the place-dependent
   contribution); §I.7 is the classical model for "multiplicity of intersection at a point."

5. **Appendix A, Intersection Theory (pp.424-437) and Appendix C, The Weil Conjectures
   (pp.449-458) are the bridge to the project's whole framing.** Appendix A is the Chow-ring /
   Riemann-Roch machine in general; Appendix C states the Weil conjectures and their cohomological
   interpretation (Frobenius eigenvalues, RH for varieties over $\mathbb{F}_q$).
   -> Appendix C is the function-field RH that the ENTIRE project (and Direction 8 specifically)
   is trying to lift to $\mathbb{Q}$. Read it for the precise statement of "RH over $\mathbb{F}_q$
   = Frobenius eigenvalues have absolute value $\sqrt{q}$" and its cohomological proof, which is
   the signature/positivity argument Direction 8 wants. Appendix A is the general Chow ring,
   relevant if Direction 8 moves beyond surfaces to higher-codimension cycles.

6. **Chapter IV (Curves, pp.293-355) is the one-dimension-down case.** Riemann-Roch and the
   canonical embedding for curves.
   -> Background for the adjunction formula and genus computations used throughout Chapter V.
   Lower priority for Direction 8 (the action is on the surface, not the curve), but the curve
   $C$ in $C\times C$ lives here.

## What this changes for the program

- **Direction 8's classical target is pinned to Chapter V §1.** When the program says "lift the
  Hodge index signature to the arithmetic surface," the precise classical statement being lifted
  is Hartshorne V.1 Theorem 1.1 (the unique symmetric pairing) plus the Hodge index theorem
  (signature $(1,\rho-1)$). The 2G in-house Lean result is this theorem for $X=C\times C$.
- **The product-surface structure is Example V.1.4.3 generalized.** $\mathbb{P}^1\times\mathbb{P}^1$
  hyperbolic form $\to$ $C\times C$ form with diagonal and Frobenius graph $\to$ (Direction 8)
  $\mathrm{Spec}(\mathbb{Z})^2$ form with $\Gamma_S$. The chain of generalization is explicit and
  this is its first link.
- **Reading priority for any Direction-8 worker:** V intro + V.1 (the pairing and Hodge index),
  then Appendix C (the function-field RH being lifted), then I.7 (local multiplicity), then
  Appendix A (general Chow ring) if going to higher codimension. Chapters II-III (schemes,
  cohomology) are the language substrate, read as needed.

## Status

ROLE NOTE based on the full TOC (read) plus Chapter V intro and §V.1 pp.356-361 (the intersection
pairing Theorem 1.1, local multiplicity Prop 1.4, self-intersection / canonical divisor Example
1.4.4, adjunction Prop 1.5, and the quadric-surface Example 1.4.3). The Hodge index theorem
statement itself (later in §V.1) and Appendices A/C were located via the TOC and chapter intro,
not read line by line. This is a textbook; a linear read is not the right use. The load-bearing
pointer: Direction 8 = lift of Chapter V §1 (intersection form + Hodge index signature) to
$\mathrm{Spec}(\mathbb{Z})^2$, with Appendix C as the function-field RH being lifted.
