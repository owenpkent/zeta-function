# Reading notes (ROLE NOTE, FRONT MATTER ONLY): Voisin, *Hodge Theory and Complex Algebraic Geometry I* (Cambridge Studies 76, CUP 2002, transl. Schneps)

> Intersection/Hodge reference textbook. Folder
> [`references/06_intersection_hodge/`](../../../references/06_intersection_hodge/).
> IMPORTANT: the PDF in the repo is FRONT MATTER ONLY (title, copyright, full table of
> contents, and the first ~4 pages of Chapter 1, about 24 pages total). The body of the
> book is NOT in this file. This is therefore a ROLE NOTE built from the TOC: it records
> WHICH Voisin chapters serve Direction 8 (the Hodge index theorem and the Hodge-Riemann
> bilinear relations / polarisation), so a future reader knows what to obtain and read.
> Read order: this is the rigorous complex-geometry counterpart to Hartshorne's classical
> surface treatment and to AHK's combinatorial generalization; read it for the precise
> Hodge-theoretic statement of the signature. Pages refer to the PDF (front matter).
> Read: pp.v-ix (full TOC) and pp.21-25 (Chapter 1 opening, holomorphic functions; all
> the substantive PDF contains).

## One-line takeaway

This file is only the front matter, but its TOC pins exactly which Voisin sections give the
Direction-8 signature in its sharpest classical-Hodge form: **§6.3 The Hodge index theorem**
(the signature of the intersection form on a Kahler surface) and **§7.1.2 Polarisation /
§7.2.3 Hodge structures of weight 2** (the Hodge-Riemann bilinear relations, the definiteness
that AHK later generalize to matroids). These are the theorems Direction 8 lifts and AHK
de-varietizes.

## Chapter-by-chapter role map for Direction 8 (from the TOC)

1. **§6.3 The Hodge index theorem (p.150; subsections 6.3.1 Other Hermitian identities, 6.3.2
   The Hodge index theorem).** This is the complex-analytic statement of the signature of the
   intersection form on the middle cohomology of a Kahler manifold (for a surface: signature
   $(1,h^{1,1}-1)$ on the $(1,1)$ part, via the Hodge-Riemann relations).
   -> This is the precise theorem Direction 8 names as its milestone ("signature $(1,k)$,
   primitive form negative definite"). Hartshorne V.1 gives the algebraic version over any
   field; Voisin §6.3 gives the transcendental/Kahler version with the Hodge structure made
   explicit. The 2G $C\times C$ result is this theorem for a product of curves. OBTAIN AND
   READ §6.3 for the cleanest signature statement.

2. **§6.2 Lefschetz decomposition (p.144) and §6.1 The Hodge decomposition (p.139).** The
   primitive cohomology decomposition and the Hodge decomposition $H^k=\bigoplus H^{p,q}$ that
   make "primitive form" meaningful. §6.2.2-6.2.3 give the Lefschetz decomposition on forms and
   on cohomology.
   -> "Primitive form negative definite" (the Direction-8 milestone) requires the PRIMITIVE
   subspace, which is defined by the Lefschetz decomposition here. This is the prerequisite
   structure for §6.3. AHK's whole achievement is reproducing this decomposition combinatorially
   (Hard Lefschetz on the matroid Chow ring); Voisin §6.2 is the classical original.

3. **§7.1.2 Polarisation and §7.1.3 Polarised varieties (pp.160-161); §7.2.3 Hodge structures
   of weight 2 (p.170).** The polarisation is the bilinear form whose definiteness on primitive
   parts (the Hodge-Riemann bilinear relations) is the abstract content of the Hodge index
   theorem. Weight-2 Hodge structures are exactly the surface $H^2$ case.
   -> This is the abstract algebraic shape of the signature, the cleanest target for a lift:
   a polarised Hodge structure of weight 2 has a form that is definite (with signs) on
   primitive $(p,q)$ pieces. Direction 8 wants $H^2$ of the arithmetic surface to carry such a
   polarised structure with the right signature. AHK is the proof that this abstract structure
   can be built with no variety; Voisin §7.1-7.2 is the definition of what is being built.

4. **§7.3.2 The pullback and the Gysin morphism (p.176); §11.3.3 Correspondences (p.285);
   §12.2.1 Correspondences (p.300).** Functoriality of Hodge structures, the Gysin map, and
   algebraic correspondences (cycles on $X\times Y$ acting on cohomology).
   -> Direction 8's missing object is the Frobenius CORRESPONDENCE $\Gamma_S$ on the product
   surface. These sections are the classical theory of correspondences as cycles on a product
   and their action on cohomology, the exact formalism $\Gamma_S$ (2Q: $(1,p)$ bidegree;
   2R: $\Gamma_S^2=-\zeta'/\zeta$) must instantiate arithmetically. OBTAIN §11.3.3 / §12.2 for
   the correspondence formalism.

5. **§11.3.1-11.3.2 Hodge classes and the Hodge conjecture (pp.279-284); Appendix-level §11.1
   Cycle class (p.264).** The cycle class map sending an algebraic cycle to a Hodge class, and
   the Hodge conjecture (which Hodge classes are algebraic).
   -> Context, not core for Direction 8, but relevant: the question "is $\Gamma_S$ an algebraic
   cycle / does it have a cycle class" is a Hodge-conjecture-flavored question. Lower priority
   than §6.3 / §7, but worth knowing where the cycle-class formalism lives.

6. **Chapters 1-5 (preliminaries, complex manifolds, Kahler metrics, sheaves/cohomology,
   harmonic forms) and Chapter 8 (de Rham complexes, spectral sequences).** The analytic
   substrate: $\partial,\bar\partial$ operators, Laplacians, Hodge decomposition via harmonic
   forms (§5.3), Kahler identities.
   -> Background substrate. Relevant only insofar as the arithmetic surface has no Kahler
   metric, which is exactly why AHK's variety-free route (and the project's search for an
   arithmetic analogue) is needed. The contrast (Voisin needs Kahler; AHK does not; the
   arithmetic surface is neither) is itself the structural point.

## What this changes for the program

- **Voisin §6.3 + §7.1-7.2 is the sharpest statement of the Direction-8 signature target.**
  Hartshorne V.1 (algebraic) and Voisin §6.3 (transcendental/Kahler) are the two classical
  faces of the same Hodge index theorem; AHK is the combinatorial generalization that drops the
  variety. Direction 8 sits at the intersection: it wants the Voisin/Hartshorne SIGNATURE via
  an AHK-style variety-free route, on $\mathrm{Spec}(\mathbb{Z})^2$.
- **The correspondence formalism (§11.3.3 / §12.2) is where $\Gamma_S$ lives classically.**
  When the program needs the precise definition of "a correspondence as a cycle on a product
  surface acting on cohomology with a given bidegree," these are the sections.
- **ACTION: the body of this book is not in the repo.** Only the front matter is present.
  To actually use Voisin for Direction 8, obtain the full text and read §6.1-6.3 (Hodge +
  Lefschetz decomposition + Hodge index), §7.1-7.2 (polarisation, weight-2 Hodge structures),
  and §§11.3.3, 12.2 (correspondences). This note maps the targets; it does not contain their
  content.

## Status

ROLE NOTE from FRONT MATTER ONLY. The repo PDF contains only the title page, copyright, the
complete table of contents (pp.v-ix, read in full), and the first ~4 pages of Chapter 1
(holomorphic functions of several variables, pp.21-25). The substantive chapters (§6.3 Hodge
index, §7 polarisation, §11-12 correspondences) are identified by the TOC and mapped to
Direction 8, but were NOT read (not present in the file). This is the most relevant Voisin
material to obtain for the live Direction-8 front: §6.3 and §7.1-7.2 are the signature theorems,
§11.3.3/§12.2 are the correspondence formalism for $\Gamma_S$.
