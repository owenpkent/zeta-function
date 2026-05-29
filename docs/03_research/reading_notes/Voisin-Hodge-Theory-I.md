# Reading notes (ROLE NOTE, FRONT MATTER ONLY in repo): Voisin, *Hodge Theory and Complex Algebraic Geometry I* (Cambridge Studies 76, CUP 2002, transl. Schneps)

> Intersection/Hodge reference textbook. Folder
> [`references/06_intersection_hodge/`](../../../references/06_intersection_hodge/).
> IMPORTANT: the PDF in the repo is FRONT MATTER ONLY (title, copyright, the complete table of
> contents pp.v-ix, and the first ~4 pages of Chapter 1 on holomorphic functions, pp.21-25;
> 24 pages total). THE BODY OF THE BOOK IS NOT IN THIS FILE. This is therefore a ROLE NOTE: it
> records which Voisin sections give the Direction-8 signature in its sharpest classical-Hodge
> form, with precise statements of those results supplied FROM GENERAL KNOWLEDGE (explicitly
> flagged, since they are not in this PDF), and with the exact printed page numbers read off
> the TOC. Voisin is the rigorous complex-geometry counterpart to Hartshorne's algebraic
> surface treatment and the classical original that AHK de-varietizes. Read DEEPLY of what is
> present: pp.v-ix (the full TOC, read in full) and pp.21-25 (Chapter 1 opening: holomorphic
> functions, the $\partial/\partial\bar z$ operators, Cauchy/Hartogs, Stokes background, all
> the substantive PDF contains).

## One-line takeaway

The repo file is only front matter, but its TOC pins exactly which Voisin sections give the
Direction-8 signature in its sharpest Kahler-Hodge form: **§6.3 The Hodge index theorem**
(printed p.150, the signature of the intersection form on the middle cohomology of a Kahler
manifold) resting on **§6.1 The Hodge decomposition** (p.139) and **§6.2 Lefschetz
decomposition** (p.144); and **§7.1 Polarisation / §7.2.3 Hodge structures of weight 2** (pp.157,
170, the Hodge-Riemann bilinear relations, the definiteness AHK later reproduce combinatorially);
plus **§7.3.2 pullback and Gysin** (p.176), **§11.3.3 / §12.2.1 Correspondences** (pp.285, 300,
where the Frobenius correspondence $\Gamma_S$ lives classically). These are the theorems
Direction 8 lifts, Hartshorne V.1 gives algebraically, and AHK de-varietizes.

## Technical content (section by section, from the TOC; statements flagged as general knowledge)

The following are NOT read from this PDF (it has only front matter and Chapter 1); the
statements are supplied from standard knowledge of Voisin Vol. I and are flagged accordingly.
Printed page numbers are read off the TOC, which IS in the PDF.

**Chapter 6, The Case of Kahler Manifolds (printed pp.137-155).**
- **§6.1 The Hodge decomposition (p.139; 6.1.1 Kahler identities, 6.1.2 comparison of
  Laplacians).** *[general knowledge]* For a compact Kahler manifold $X$, the Kahler identities
  $[\Lambda,\bar\partial]=-i\partial^*$ etc. force $\Delta_d=2\Delta_\partial=2\Delta_{\bar\partial}$,
  giving the Hodge decomposition $H^k(X,\mathbb{C})=\bigoplus_{p+q=k}H^{p,q}(X)$ with
  $\overline{H^{p,q}}=H^{q,p}$. This is the structure that makes "the $(1,1)$ part" and hence
  "primitive form" meaningful.
- **§6.2 Lefschetz decomposition (p.144; on forms 6.2.2, on cohomology 6.2.3).** *[general
  knowledge]* With $L=\omega\wedge-$ the Lefschetz operator and $\Lambda$ its adjoint, the
  $\mathfrak{sl}_2$-action gives Hard Lefschetz ($L^{n-k}:H^k\xrightarrow{\sim}H^{2n-k}$) and the
  primitive decomposition $H^k=\bigoplus_r L^r H^{k-2r}_{prim}$, where $H^m_{prim}=\ker(L^{n-m+1})$.
  The "primitive form negative definite" in the Direction-8 milestone requires exactly this
  primitive subspace. AHK's whole achievement is reproducing this $\mathfrak{sl}_2$/primitive
  structure COMBINATORIALLY (Hard Lefschetz on the matroid Chow ring); §6.2 is the classical
  original.
- **§6.3 The Hodge index theorem (p.150; 6.3.1 other Hermitian identities, 6.3.2 the Hodge index
  theorem at p.152). THE TARGET THEOREM.** *[general knowledge]* The Hodge-Riemann bilinear
  relations: on the primitive part $H^{p,q}_{prim}$ of a compact Kahler $X$ of dimension $n$, the
  Hermitian form $h(\alpha,\beta)=i^{p-q}(-1)^{(k)(k-1)/2}\int_X\alpha\wedge\bar\beta\wedge
  \omega^{n-k}$ ($k=p+q$) is POSITIVE DEFINITE. For a SURFACE ($n=2$) this specializes to: the
  intersection form on $H^2(X,\mathbb{R})$ restricted to the real $(1,1)$ classes has signature
  $(1,h^{1,1}-1)$, i.e. one $+1$ (the Kahler/ample direction) and the rest $-1$ (the primitive
  classes are negative definite). This is the transcendental/Kahler version of Hartshorne's
  Theorem 1.9; the 2G $C\times C$ result is this theorem for a product of curves.

**Chapter 7, Hodge Structures and Polarisations (printed pp.156-183).**
- **§7.1 Definitions (p.157; 7.1.1 Hodge structure, 7.1.2 Polarisation p.160, 7.1.3 polarised
  varieties p.161).** *[general knowledge]* A weight-$k$ Hodge structure is a lattice $H_\mathbb{Z}$
  with $H_\mathbb{C}=\bigoplus_{p+q=k}H^{p,q}$, $\overline{H^{p,q}}=H^{q,p}$. A POLARISATION is a
  $(-1)^k$-symmetric form $Q$ with the Hodge-Riemann relations: $Q(H^{p,q},H^{p',q'})=0$ unless
  $(p',q')=(q,p)$, and $i^{p-q}Q(\alpha,\bar\alpha)>0$ on the primitive part. The polarisation is
  the ABSTRACT bilinear form whose definiteness on primitive pieces is the abstract content of
  the Hodge index theorem.
- **§7.2.3 Hodge structures of weight 2 (p.170). THE SURFACE CASE.** *[general knowledge]* For a
  surface, $H^2$ is a weight-2 Hodge structure $H^{2,0}\oplus H^{1,1}\oplus H^{0,2}$; the
  polarisation (cup product) is symmetric, and the Hodge-Riemann relations on the primitive
  $(1,1)$ part give exactly the signature $(1,h^{1,1}-1)$ statement. This is the cleanest abstract
  target for a lift: a polarised weight-2 Hodge structure has a definite form (with signs) on its
  primitive $(p,q)$ pieces.
- **§7.3.2 The pullback and the Gysin morphism (p.176); §7.3.3 Hodge structure of a blowup
  (p.180).** *[general knowledge]* Functoriality: $f^*$ is a morphism of Hodge structures; the
  Gysin $f_*$ shifts weight by $2\,\mathrm{codim}$. The blowup formula decomposes the Hodge
  structure of a blown-up variety, the analytic mirror of AHK's stellar-subdivision / flip
  decompositions.

**Chapters 11-12, Cycles, Cycle Classes, Correspondences.**
- **§11.1 Cycle class (p.264); §11.2 Chern classes (p.276); §11.3 Hodge classes (p.279; 11.3.2
  the Hodge conjecture p.284, 11.3.3 Correspondences p.285).** *[general knowledge]* The cycle
  class map $\mathrm{CH}^k(X)\to H^{2k}(X,\mathbb{Z})$ lands in Hodge classes ($(k,k)$); the Hodge
  conjecture asks the converse for $\mathbb{Q}$-coefficients. §11.3.3 Correspondences: a cycle on
  $X\times Y$ acts on cohomology $H^*(X)\to H^*(Y)$ by $\alpha\mapsto p_{Y*}(\mathrm{cl}(\Gamma)
  \cup p_X^*\alpha)$, a morphism of Hodge structures of the appropriate bidegree.
- **§12.2.1 Correspondences (p.300).** *[general knowledge]* Correspondences acting on
  intermediate Jacobians / via the Abel-Jacobi map; the refined theory of cycles on a product
  acting on cohomology.

**What IS in the PDF (Chapter 1, pp.21-25, read).** Holomorphic functions of several variables:
$\mathbb{C}$-valued holomorphic = annihilated by $\partial/\partial\bar z_i$ (Def 1.4-1.6);
Cauchy's formula in several variables and analyticity (Thm 1.1); Riemann's removable-singularity
and Hartogs' extension theorems (Thm 1.2-1.3, extension across codimension-2 analytic subsets,
used for birational invariance of plurigenera); the Wirtinger operators $\partial f/\partial z=
\frac12(\partial_x-i\partial_y)f$ (eq. 1.3); local solution of $\partial f/\partial\bar z=g$ (for
Dolbeault exactness); and Stokes-formula background on integration of forms over manifolds with
boundary. This is the analytic substrate, NOT the Hodge-theory content; it is here only because
it is where the PDF was truncated.

## Points mapped to the project

1. **§6.3 + §7.1-7.2 is the sharpest classical statement of the Direction-8 signature target
   (printed pp.150, 157-170).** Direction 8's milestone, "signature $(1,k)$, primitive form
   negative definite," is precisely the Hodge index theorem (§6.3) / a polarised weight-2 Hodge
   structure (§7.2.3). Hartshorne V.1 gives the algebraic version over any field; Voisin gives
   the transcendental/Kahler version with the Hodge structure made explicit. The 2G $C\times C$
   result is this theorem for a product of curves. OBTAIN AND READ §6.3 and §7.2.3 for the
   cleanest signature statement. ->

2. **The primitive subspace is defined by the Lefschetz decomposition (§6.2, p.144).** "Primitive
   form negative definite" requires the primitive cohomology, which §6.2 constructs via the
   $\mathfrak{sl}_2$/Lefschetz action. This is the prerequisite for §6.3. AHK's central
   achievement is reproducing this decomposition combinatorially (Hard Lefschetz on the matroid
   Chow ring); Voisin §6.2 is the classical original. The contrast is the structural point:
   Voisin gets the primitive decomposition from a Kahler metric and harmonic theory, AHK gets it
   from fan combinatorics with no metric, and the arithmetic surface has neither, which is why
   Direction 8 needs the AHK-style variety-free route. ->

3. **The polarised-weight-2-Hodge-structure shape is the abstract lift target (§7.1.2, §7.2.3,
   pp.160, 170).** The cleanest thing to lift is not a variety but an abstract structure: a
   polarised Hodge structure of weight 2 whose form is definite (with signs) on primitive $(p,q)$
   pieces. Direction 8 wants $H^2$ of the arithmetic surface to carry such a polarised structure
   with signature $(1,k)$. AHK is the proof this abstract structure can be built with NO variety;
   Voisin §7.1-7.2 is the precise definition of what is being built. Together they bracket
   Direction 8: it wants the Voisin/Hartshorne SIGNATURE via an AHK-style variety-free route on
   $\mathrm{Spec}(\mathbb{Z})^2$. ->

4. **The correspondence formalism (§7.3.2, §11.3.3, §12.2.1; pp.176, 285, 300) is where
   $\Gamma_S$ lives classically.** Direction 8's missing object is the Frobenius CORRESPONDENCE
   $\Gamma_S$ on the product surface. These sections are the classical theory of correspondences
   (cycles on $X\times Y$ acting on cohomology as morphisms of Hodge structures with a given
   bidegree), the exact formalism $\Gamma_S$ (2Q: $(1,p)$ bidegree; 2R: $\Gamma_S^2=-\zeta'/\zeta$)
   must instantiate arithmetically. The Gysin map (§7.3.2) is how a correspondence's pushforward
   shifts weight. OBTAIN §11.3.3 / §12.2.1 for the correspondence formalism. ->

5. **The Kahler-vs-no-metric contrast is itself the structural diagnosis (§6.1, Chapters 1-5).**
   Voisin's entire route to the Hodge decomposition needs a Kahler metric and harmonic forms
   (Chapters 1-5 are the $\partial,\bar\partial$/Laplacian/harmonic substrate). The arithmetic
   surface $\mathrm{Spec}(\mathbb{Z})^2$ has NO Kahler metric. That is exactly why AHK's
   variety-free route (and the project's search for an arithmetic analogue) is needed. The
   three-way contrast, Voisin needs Kahler, AHK does not but works on matroids, the arithmetic
   surface is neither, is the precise statement of the Direction-8 gap: find the structure that
   yields the §6.3 signature without either a Kahler metric or a matroid. ->

## What this changes for the program

- **Voisin §6.3 + §7.1-7.2 is the sharpest signature target; obtain and read it.** Hartshorne V.1
  (algebraic) and Voisin §6.3 (transcendental/Kahler) are the two classical faces of the same
  Hodge index theorem; AHK is the combinatorial generalisation that drops the variety. Direction
  8 sits at the intersection: it wants the Voisin/Hartshorne SIGNATURE via an AHK-style
  variety-free route on $\mathrm{Spec}(\mathbb{Z})^2$. The three notes (Hartshorne, AHK, Voisin)
  bracket the problem precisely.
- **The correspondence sections (§7.3.2, §11.3.3, §12.2.1) are the classical home of $\Gamma_S$.**
  When the program needs the precise definition of "a correspondence as a cycle on a product
  surface acting on cohomology with a given bidegree," these are the sections to read.
- **ACTION: the body of this book is not in the repo.** Only the front matter and Chapter 1
  opening are present. To use Voisin for Direction 8, obtain the full text and read §6.1-6.3
  (Hodge + Lefschetz decomposition + Hodge index, pp.139-152), §7.1-7.2 (polarisation, weight-2
  Hodge structures, pp.157-170), and §§7.3.2, 11.3.3, 12.2.1 (Gysin + correspondences, pp.176,
  285, 300). This note maps the targets with their exact page numbers; it does NOT contain their
  content, and the statements above are from general knowledge, not from this PDF.

## Status

ROLE NOTE from FRONT MATTER ONLY. The repo PDF contains the title page, copyright, the complete
table of contents (pp.v-ix, read in full, exact printed page numbers extracted), and the first
~4 pages of Chapter 1 (holomorphic functions of several variables, the $\partial/\partial\bar z$
operators, Cauchy/Hartogs, Stokes background, pp.21-25, read). The substantive Hodge-theory
chapters (§6.3 Hodge index p.150/152, §6.1-6.2 Hodge + Lefschetz decomposition pp.139-148, §7.1-7.2
polarisation and weight-2 Hodge structures pp.157-170, §7.3.2 pullback/Gysin p.176, §11.3.3 and
§12.2.1 correspondences pp.285, 300) are identified by the TOC and mapped to Direction 8, with
precise statements supplied from general knowledge and explicitly flagged as NOT from this PDF.
This is the most relevant Voisin material to obtain for the live Direction-8 front: §6.3 and
§7.1-7.2 are the signature theorems, §11.3.3/§12.2.1 are the correspondence formalism for
$\Gamma_S$.
