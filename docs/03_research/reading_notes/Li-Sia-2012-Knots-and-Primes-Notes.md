# Reading notes: Li and Sia, *Knots and Primes* (Harvard Summer 2012 Tutorial Notes)

> Arithmetic-topology dictionary entry, undergraduate version. Folder
> [`references/05_arithmetic_topology/`](../../../references/05_arithmetic_topology/).
> These are the clean, self-contained tutorial notes (Chao Li and Charmaine Sia, Harvard
> 2012) built directly on Morishita's textbook *Knots and Primes: An Introduction to
> Arithmetic Topology* (the survey by the same author is in this folder). They are more
> explicit and example-driven than the survey: a complete one-page dictionary TABLE, a full
> elementary proof of quadratic reciprocity, the Wirtinger presentation worked on the trefoil,
> and a careful treatment of covering spaces. Read order: read AFTER the Morishita survey for
> the gentler, fully proved version; or BEFORE it as the on-ramp. Pages refer to the PDF
> (41pp). Read DEEPLY: pp.1-12 (Lecture 1: rings/spaces, knots-primes analogy, Table 1, knot
> diagrams and the knot group / Wirtinger presentation; Lecture 2: quadratic reciprocity in
> full with the Legendre-symbol-as-homomorphism derivation and Rousseau's CRT proof; Lecture
> 3: covering spaces, Galois coverings, the covering / subgroup correspondence). Later lectures
> (Alexander/Iwasawa polynomials, genus theory) read via Table 1.

## One-line takeaway

The same MKR dictionary as Morishita but with everything proved at the undergraduate level: a
complete one-page Table 1 giving every analogy at a glance, the Legendre symbol identified as
the quotient homomorphism $\mathbb{F}_p^\times\to\{\pm1\}$ (kernel = the squares, an index-2
subgroup, the simplest possible signature datum), quadratic reciprocity proved from the CRT,
and the clean statement that $\mathrm{Spec}(\mathbb{Z})$ is $\mathbb{R}^3$ while the correct
$S^3$ is $\mathrm{Spec}(\mathbb{Z})\cup\{\infty\}$. This is the project's most usable reference
for the dictionary and for why $\infty$ is the compactifying point.

## Technical content (section by section)

**Lecture 1 (pp.2-7): the analogy and the knot group.**
- Rings and spaces (1.1-1.2). $\mathbb{C}[t]$ has Krull dimension 1, so $\mathrm{Spec}\,\mathbb{C}[t]$
  is a line with closed points $(t-a)$ and a generic point (the zero ideal); the inclusion
  $\mathrm{Spec}\,\mathbb{C}\hookrightarrow\mathrm{Spec}\,\mathbb{C}[t]$ corresponds to the
  quotient $\mathbb{C}[t]\twoheadrightarrow\mathbb{C}[t]/(t-a)$. Identically, $\mathbb{Z}$ has
  Krull dimension 1, $\mathrm{Spec}\,\mathbb{Z}$ is a "line" with closed points $(p)$, and
  $\mathrm{Spec}\,\mathbb{F}_p\hookrightarrow\mathrm{Spec}\,\mathbb{Z}$ corresponds to
  $\mathbb{Z}\twoheadrightarrow\mathbb{Z}/(p)$.
- The atom of the dictionary (1.2). $\mathrm{Spec}\,\mathbb{F}_p$ has etale homotopy groups
  $\pi_1^{et}=\mathrm{Gal}(\bar{\mathbb{F}}_p/\mathbb{F}_p)=\hat{\mathbb{Z}}$ and $\pi_i^{et}=0$
  for $i\ge2$, the same shape as $\pi_1(S^1)=\mathbb{Z}$, $\pi_i(S^1)=0$ for $i\ge2$ (both are
  $K(\pi,1)$ spaces). So $\mathrm{Spec}\,\mathbb{F}_p$ is an arithmetic $S^1$. Artin-Verdier
  duality is "some sort of Poincare duality for 3-manifolds" and $\pi_1^{et}(\mathrm{Spec}\,
  \mathbb{Z})=1$, so $\mathrm{Spec}\,\mathbb{Z}$ is $\mathbb{R}^3$; the prime at infinity gives
  $\mathrm{Spec}\,\mathbb{Z}\cup\{\infty\}=S^3$, and $\mathrm{Spec}\,\mathbb{F}_p
  \hookrightarrow\mathrm{Spec}\,\mathbb{Z}$ is the analogue of $S^1\hookrightarrow\mathbb{R}^3$.
- TABLE 1 (p.3), the all-in-one dictionary, in four blocks:
  - *Fundamental/Galois groups.* $\pi_1(S^1)=\mathbb{Z}=\langle l\rangle\leftrightarrow
    \pi_1(\mathrm{Spec}\,\mathbb{F}_q)=\hat{\mathbb{Z}}=\langle\sigma\rangle$; loop $l\leftrightarrow$
    Frobenius $\sigma$; universal cover $\mathbb{R}\leftrightarrow\bar{\mathbb{F}}_q$; cyclic
    cover $\mathbb{R}/n\mathbb{Z}\leftrightarrow\mathbb{F}_{q^n}/\mathbb{F}_q$.
  - *Manifolds / Spec of a ring.* tubular nbhd $V\simeq S^1\leftrightarrow\mathrm{Spec}\,
    \mathcal{O}_\mathfrak{p}$; boundary $\partial V\leftrightarrow\mathrm{Spec}\,k_\mathfrak{p}$;
    3-manifold $M\leftrightarrow$ number ring $\mathrm{Spec}\,\mathcal{O}_k$; knot
    $S^1\hookrightarrow\mathbb{R}^3\cup\{\infty\}=S^3\leftrightarrow$ rational prime
    $\mathrm{Spec}\,\mathbb{F}_p\hookrightarrow\mathrm{Spec}\,\mathbb{Z}\cup\{\infty\}$;
    "any closed oriented 3-manifold is a branched cover of $S^3$ along a link"
    $\leftrightarrow$ "any number field is a finite extension of $\mathbb{Q}$ ramified over a
    finite set of primes."
  - *Knot group / prime group.* $G_K=\pi_1(M\setminus K)\leftrightarrow G_{\{p\}}=
    \pi_1^{et}(\mathrm{Spec}\,\mathcal{O}_k\setminus\{p\})$; $G_K\cong G_L\Leftrightarrow K\sim L$
    $\leftrightarrow G_{\{p\}}\cong G_{\{q\}}\Leftrightarrow p=q$.
  - *Linking number / Legendre symbol.* $\mathrm{lk}(L,K)\leftrightarrow(q^*/p)$ with
    $q^*=(-1)^{(q-1)/2}q$; SYMMETRY $\mathrm{lk}(K,L)=\mathrm{lk}(L,K)\leftrightarrow$ quadratic
    reciprocity $(q/p)=(p/q)$ ($p,q\equiv1\bmod4$).
  - *Alexander-Fox / Iwasawa.* infinite cyclic cover $X_\infty\to X_K$, $\mathrm{Gal}=
    \langle\tau\rangle\cong\mathbb{Z}\leftrightarrow$ cyclotomic $\mathbb{Z}_p$-extension
    $k_\infty/k$, $\mathrm{Gal}=\langle\gamma\rangle\cong\mathbb{Z}_p$; knot module
    $H_1(X_\infty)\leftrightarrow$ Iwasawa module $H_\infty$; Alexander polynomial
    $\det(t\cdot\mathrm{id}-\tau\mid H_1(X_\infty)\otimes\mathbb{Q})\leftrightarrow$ Iwasawa
    polynomial $\det(T\cdot\mathrm{id}-(\gamma-1)\mid H_\infty\otimes\mathbb{Q}_p)$.
- Knot group and Wirtinger presentation (2.2, Thm 2.8). $G_K=\pi_1(S^3\setminus K)$; from a
  regular oriented diagram with arcs $c_1,\dots,c_n$ one gets generators $x_i$ (loops through
  $\infty$ under $c_i$) and one relation per crossing
  ($x_ix_kx_{i+1}^{-1}x_k^{-1}=1$ or $x_ix_k^{-1}x_{i+1}^{-1}x_k=1$), one of which is
  redundant (Fact 2.9), so $G_K$ has deficiency 1 (Cor 2.10). Worked: the trefoil
  $G=\langle x_1,x_2\mid x_1x_2x_1=x_2x_1x_2\rangle$, the braid group $B_3$, $\cong\langle
  a,b\mid a^3=b^2\rangle$ (Ex 2.12-2.13). Links: $G_L=\pi_1(S^3\setminus L)$, also deficiency 1.

**Lecture 2 (pp.7-10): quadratic reciprocity, proved.** Motivation from Fermat's
$p=x^2+y^2\Leftrightarrow p\equiv1\bmod4$, which reduces to "$-1$ is a QR mod $p$." The
Legendre symbol $(\tfrac{a}{p})=\pm1$ for QR/non-QR (Def 3.6). The conceptual reframing
(Remark 3.7) is the point for the project: $(\mathbb{F}_p^\times)^2\hookrightarrow
\mathbb{F}_p^\times$ is an index-2 subgroup, giving an exact sequence
$1\to(\mathbb{F}_p^\times)^2\to\mathbb{F}_p^\times\to\{\pm1\}\to1$, and the Legendre symbol IS
the quotient HOMOMORPHISM $\mathbb{F}_p^\times\to\{\pm1\}$. Hence multiplicativity
(Prop 3.8) and Euler's criterion $(\tfrac{a}{p})=a^{(p-1)/2}$ (Prop 3.9) are forced. The
supplementary laws (Prop 3.11): $(\tfrac{-1}{p})=(-1)^{(p-1)/2}$, $(\tfrac{2}{p})=
(-1)^{(p^2-1)/8}$. Quadratic reciprocity (Thm 3.12) $(\tfrac{p}{q})=(\tfrac{q}{p})
(-1)^{\frac{p-1}{2}\frac{q-1}{2}}$ is proved by Rousseau's CRT argument: from
$(\mathbb{Z}/pq)^\times\cong\mathbb{F}_p^\times\times\mathbb{F}_q^\times$, compute the product
of a chosen half-system of coset representatives two ways and compare signs. Worked numerical
examples ($(\tfrac{3}{11})$, $(\tfrac{137}{227})$). Remark 3.15: QR generalizes to Artin
reciprocity in class field theory.

**Lecture 3 (pp.11-12+): covering spaces.** The framework for studying $\pi_1(X)$ as a Galois
group $\mathrm{Gal}(\tilde X/X)$: unramified coverings (Def 4.1), covering transformations
$\mathrm{Aut}(Y/X)$, Galois (normal) coverings (Def 4.4), and the main theorem (Thm 4.5): a
bijection {connected coverings $h:Y\to X$}/iso $\leftrightarrow$ {subgroups of $\pi_1(X,x)$}/conj,
with $h$ Galois iff $h_*\pi_1(Y)$ is normal, and then $\mathrm{Gal}(Y/X)\cong\pi_1(X)/h_*\pi_1(Y)$.
The universal cover $\leftrightarrow$ the trivial subgroup, $\mathrm{Gal}(\tilde X/X)=\pi_1(X)$.
This is the exact topological mirror of the Galois correspondence for field extensions, the
formal backbone of the whole dictionary. Worked: coverings of $S^1$ are $h_n:S^1\to S^1$ and
the universal $\mathbb{R}\to S^1$ with $\mathrm{Gal}=\mathbb{Z}$.

## Points mapped to the project

1. **The full dictionary table (Table 1, p.3) is the project's single-glance reference.** The
   line that matters for Direction 8: linking number $\leftrightarrow$ Legendre symbol, and its
   SYMMETRY $\leftrightarrow$ reciprocity. The bottom Iwasawa row,
   $\det(T\cdot\mathrm{id}-(\gamma-1)\mid H_\infty)$, is the characteristic-polynomial /
   determinant face that 2R's $\det_\zeta$ and the Alexander-polynomial analogy share. Cite
   Table 1 for the dictionary; cite Morishita §2 for the cup-product realization Table 1
   summarizes in one line. ->

2. **The Legendre symbol is literally a quotient homomorphism onto $\{\pm1\}$ (Remark 3.7).**
   This is the cleanest statement of the structural fact for Direction 8: the kernel
   $(\mathbb{F}_p^\times)^2$ is an index-2 subgroup, and the symbol is the resulting sign. An
   index-2 quotient (a single $\pm1$) is the simplest possible "signature" datum, and quadratic
   reciprocity is its symmetry. The Direction-8 milestone (Hodge index, signature $(1,k)$,
   primitive form negative definite) is the high-dimensional generalization of "a sign attached
   to a pairing of two primes is symmetric." Li-Sia gives the most explicit version of the
   atom that Direction 8 wants to scale up. ->

3. **$\mathrm{Spec}(\mathbb{Z})=\mathbb{R}^3$, $S^3=\mathrm{Spec}(\mathbb{Z})\cup\{\infty\}$
   (Lecture 1, p.3), stated with the explicit reason.** Artin-Verdier gives 3-dimensional
   Poincare duality and $\pi_1^{et}(\mathrm{Spec}\,\mathbb{Z})=1$. The archimedean place
   $\infty$ (2I) is exactly the one-point compactification that closes the manifold. Direction 8
   must include $\infty$ to compactify its surface and get a finite signature; Li-Sia gives the
   cleanest statement of why $\infty$ is the compactifying point, matching the Morishita note
   and the Deninger archimedean-stationary-point picture. ->

4. **Quadratic reciprocity has a finite, elementary, machine-checkable proof (Thm 3.12,
   Rousseau).** This matters operationally: the simplest signature datum and its symmetry are
   not only conceptual; the symmetry is a finite CRT computation. If the project wants to Lean-
   verify "the simplest reciprocity = symmetry of a sign," this is the proof to formalize, the
   one-dimension-down analogue of the 2G machine-proved Hasse-Weil bound. ->

5. **The covering / subgroup correspondence (Thm 4.5) is the formal backbone (Lecture 3).** The
   whole dictionary rests on $\pi_1(X)=\mathrm{Gal}(\tilde X/X)$ and the bijection between
   coverings and subgroups, the topological mirror of Galois theory. This is the "how a prime
   is knotted in $\mathrm{Spec}(\mathbb{Z})$" group-theoretic invariant, the $\pi_1$-side of the
   same embedding whose intersection-theoretic side Direction 8 studies. Worth knowing the two
   descriptions are of one object. Lower priority than points 1-3 but it is the glue. ->

## What this changes for the program

- **Best single reference for the dictionary, and the cleanest "signature atom."** Where
  Morishita is the survey with the cohomological cup-product realization, Li-Sia is the
  textbook-clean version with the all-in-one Table 1, the Legendre-symbol-as-homomorphism
  derivation (Remark 3.7), and the full reciprocity proof. The two together give the project
  both the conceptual content (a reciprocity law = symmetry of an intersection pairing) and the
  most explicit elementary statement (an index-2 sign and its symmetry).
- **Reinforces the same two structural facts as the Morishita note.** (a) The archimedean place
  is the compactifying $\infty$ (point 3), now with the explicit Artin-Verdier reason; (b)
  reciprocity is the symmetry of a pairing / the simplest signature datum (points 1, 2, 4).
  These are the two threads that touch Direction 8, and both notes agree.
- **A Lean-formalizable baby target.** The Rousseau proof of reciprocity (point 4) is a finite,
  self-contained signature-symmetry statement, the natural one-dimension-down companion to the
  2G machine-proved function-field RH. No new theorem for $\zeta$: this is pedagogy, and its
  value is as the readable on-ramp and the cleanest statement of the signature atom.

## Status

Read DEEPLY pp.1-12 (Lecture 1 full: rings/spaces 1.1-1.2, the knots-primes analogy with
explicit homotopy groups, Table 1 in all four blocks, knot diagrams and the Wirtinger
presentation Thm 2.8 with the trefoil worked; Lecture 2 full: Fermat motivation, Legendre
symbol as the quotient homomorphism Remark 3.7, Euler's criterion 3.9, supplementary laws
3.11, quadratic reciprocity 3.12 with Rousseau's CRT proof and worked examples; Lecture 3:
covering spaces, Galois coverings, the covering/subgroup correspondence Thm 4.5). Later
lectures (Alexander-Fox and Iwasawa polynomials, genus theory, the full prime/knot
homology dictionary) read via Table 1 and section heads only. These are undergraduate tutorial
notes; depth here is appropriate. Load-bearing for the project: Table 1 (the dictionary),
Remark 3.7 (the Legendre symbol as a $\pm1$ quotient = the signature atom), and the
$\mathrm{Spec}(\mathbb{Z})\cup\{\infty\}=S^3$ statement.
