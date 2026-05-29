# Reading notes: Morishita, *Analogies between Knots and Primes, 3-Manifolds and Number Rings* (arXiv:0904.3399, 2009)

> Arithmetic-topology dictionary entry, the foundational survey. Folder
> [`references/05_arithmetic_topology/`](../../../references/05_arithmetic_topology/).
> This is the expanded English translation of Morishita's survey of the MKR
> (Mazur-Kapranov-Reznikov) dictionary: primes are knots, $\mathrm{Spec}(\mathcal{O}_k)$
> is a 3-manifold, the linking number is the Legendre symbol, quadratic reciprocity is the
> symmetry of a cup-product intersection form. It is the source paper behind the Li-Sia
> tutorial notes (same folder) and the reference the Morishita bridge (2K, arXiv:2508.15971)
> extends. Read order: read this first, then Li-Sia for the worked undergraduate version.
> Pages refer to the PDF (41pp total). Read DEEPLY: pp.1-20 (Introduction; §1 knots and
> primes; §2 linking numbers and Legendre symbols; §3 link groups and pro-$l$ Galois groups;
> §4 Milnor invariants and multiple power residue symbols; §5 homology groups and ideal class
> groups). Sections 6-8 (3-manifold coverings/class field theory, Alexander-Fox/Iwasawa,
> deformations) read via contents.

## One-line takeaway

A prime $\mathrm{Spec}(\mathbb{F}_p)\hookrightarrow\mathrm{Spec}(\mathbb{Z})$ is the
arithmetic analogue of a knot $S^1\hookrightarrow S^3$, and under this dictionary the mod-2
Legendre symbol is realized as a cup-product intersection number on the arithmetic
3-manifold, with quadratic reciprocity $\mathrm{lk}(K,L)=\mathrm{lk}(L,K)$ becoming the
SYMMETRY of that pairing. This is the simplest fully worked instance of the project's
Direction-8 template (an arithmetic law = a property of an intersection form), realized one
dimension below the surface case Direction 8 builds, and it is already machine-checkable in
the $\mathbb{F}_2$, two-prime case.

## Technical content (section by section)

**Introduction (pp.1-2).** The 3-dimensional view of a number ring was first recognized by
Tate-Artin-Verdier: classical class field theory (Takagi-Artin) restates as a sort of
3-dimensional Poincare duality in the etale cohomology of a number ring (ref [44]). Mazur
(and Manin) pointed out the knots-primes analogy from this homotopical viewpoint in the
mid-1960s; Kapranov and Reznikov revived it as "arithmetic topology." Morishita's own
entry was the analogy between a Galois group with restricted ramification and a link group.
The survey's stated aim: explain classical invariants (linking numbers, power residue
symbols, Alexander vs Iwasawa polynomials) from a uniform group-theoretic point of view,
and develop arithmetic analogues of Milnor's higher linking numbers, recovering Gauss's
genus theory as a special case.

**§1 Knots and primes (pp.3-6).** The atom of the dictionary:
- $S^1$ is the Eilenberg-MacLane space $K(\mathbb{Z},1)$; its arithmetic analog is
  $K(\hat{\mathbb{Z}},1)\simeq\mathrm{Spec}(\mathbb{F}_q)$ etale-homotopically (eq. (1.1)),
  since $\pi_1^{et}(\mathrm{Spec}\,\mathbb{F}_q)=\mathrm{Gal}(\bar{\mathbb{F}}_q/\mathbb{F}_q)
  =\hat{\mathbb{Z}}$ and the only nonzero homotopy group is $\pi_1$. A finite cyclic covering
  $\mathbb{R}/n\mathbb{Z}\to\mathbb{R}/\mathbb{Z}$ corresponds to a finite cyclic extension
  $\mathbb{F}_{q^n}/\mathbb{F}_q$; the loop $l(x)=x+1$ corresponds to Frobenius
  $\mathrm{Fr}(x)=x^q$.
- LOCAL structure at a prime (eq. (1.2)). A tubular neighborhood $V=S^1\times D^2$ of a knot
  is homotopy equivalent to $S^1$, and $V\setminus S^1$ to the boundary torus $\partial V$.
  On the arithmetic side $\mathrm{Spec}(\mathcal{O}_\mathfrak{p})$ (the $\mathfrak{p}$-adic
  integer ring) plays $V$, and $\mathrm{Spec}(k_\mathfrak{p})$ (the $\mathfrak{p}$-adic field)
  plays $\partial V$. The peripheral group $\pi_1(\partial V)=\langle\alpha,\beta\mid
  [\alpha,\beta]=1\rangle$ (free abelian on meridian $\alpha$, longitude $\beta$) maps to the
  tame quotient $\pi_1^{tame}(\mathrm{Spec}\,k_\mathfrak{p})=\langle\tau,\sigma\mid
  \tau^{q-1}[\tau,\sigma]=1\rangle$: meridian $\alpha\leftrightarrow$ monodromy/inertia
  $\tau$, longitude $\beta\leftrightarrow$ Frobenius $\sigma$.
- GLOBAL (eq. (1.3)). Artin-Verdier: $\mathrm{Spec}(\mathcal{O}_k)$ has etale cohomological
  dimension 3 (up to 2-torsion) and 3-dimensional Poincare duality, so it is a 3-manifold;
  the prime $\mathrm{Spec}(\mathbb{F}_\mathfrak{p})\hookrightarrow\mathrm{Spec}(\mathcal{O}_k)$
  is a knot. Since $\pi_1(\mathrm{Spec}\,\mathbb{Z})=1$ (Hermite-Minkowski, the analogue of
  the Poincare conjecture), $\mathrm{Spec}(\mathbb{Z})$ is $\mathbb{R}^3$ and
  $\mathrm{Spec}(\mathbb{Z})\cup\{\infty\}=S^3$, with $\infty$ the END-compactification point.
  The infinite primes are the ends of a non-compact 3-manifold.
- The knot group $G_K=\pi_1(S^3\setminus K)$ determines a prime knot up to orientation
  ((1.4), Whitten / Gordon-Luecke); arithmetic analog $G_{\{p\}}\cong G_{\{q\}}\Leftrightarrow
  p=q$ ((1.5)). The Galois group $G_S=\pi_1(\mathrm{Spec}(\mathcal{O}_k\setminus S))$ with $S$
  a finite set of primes is the analogue of a LINK group $G_L=\pi_1(M\setminus L)$.
- The "no constant field" wall (p.6): a curve $C/\mathbb{F}_q$ is a surface-bundle over the
  circle $\mathrm{Spec}\,\mathbb{F}_q$ (exact sequence $1\to\pi_1(C\otimes\bar{\mathbb{F}}_q)
  \to\pi_1(C)\to\pi_1(\mathrm{Spec}\,\mathbb{F}_q)\to1$), but a number ring has NO constant
  field, so $\pi_1(\mathrm{Spec}\,\mathcal{O}_k)$ behaves like a random 3-manifold group, not
  like $\pi_1(C)$. Iwasawa's $\mathbb{Z}_p$-tower is RAMIFIED, so it is the analogue of cyclic
  coverings BRANCHED along a knot, not the unramified constant-field extension.

**§2 Linking numbers and Legendre symbols (pp.6-9). The load-bearing section for Direction 8.**
The mod-2 linking number $\mathrm{lk}(K,L)$ of a 2-component link is realized as the covering
transformation of the unique unbranched double cover $Y_K\to X_K=S^3\setminus K$ applied to a
longitude $\beta_L$: $\pi_1(X_K)\to\mathrm{Gal}(Y_K/X_K)=\mathbb{Z}/2$, $[\beta_L]\mapsto
\mathrm{lk}(K,L)\bmod 2$. Equivalently (and this is the form that matters) it is a CUP PRODUCT
of cohomology classes. With $X_L=S^3\setminus L$ and $\Sigma$ a Seifert surface of $L$:
$$H^2_c(X_L,\mathbb{F}_2)\times H^1(X_L,\mathbb{F}_2)\xrightarrow{\cup}H^3_c(X_L,\mathbb{F}_2)
=\mathbb{Z}/2,\qquad [K]\cup[\Sigma]=\mathrm{lk}(K,L)\bmod 2.$$
The arithmetic mirror (pp.7-8): for distinct odd primes $p,q\equiv1\bmod4$, take the etale
double cover $Y_p\to X_p=\mathrm{Spec}(\mathbb{Z})\setminus\{(p)\}=\mathrm{Spec}(\mathbb{Z}[1/p])$,
where $Y_q$ is the spectrum of the normalization of $\mathbb{Z}[1/p]$ in $\mathbb{Q}(\sqrt{p})$.
Define $\mathrm{lk}_2(p,q)$ by the image of Frobenius over $q$ in
$\mathrm{Gal}(Y_p/X_p)=\mathbb{Z}/2$. Since $\sigma_q$ fixes $\sqrt{p}\Leftrightarrow p$ is a
QR mod $q$:
$$(-1)^{\mathrm{lk}_2(p,q)}=\left(\tfrac{p}{q}\right)\qquad(2.1).$$
The Legendre symbol is then ALSO an intersection number, via the dual cup product: regard $(q)$
as a "meridian" with Kummer character $\chi_q$, define a "Seifert surface" class $[\Sigma]\in
H^1(X_q,\mathbb{F}_2)$ with $\partial[\Sigma]=\chi_q$, identify the "knot" $(p)\in
\mathbb{Q}_q^\times/(\mathbb{Q}_q^\times)^2=H^1(\mathbb{Q}_q,\mathbb{F}_2)$ with its class
$[(p)]\in H^2_c(X_q,\mathbb{F}_2)$, and pair:
$$H^2_c(X_q,\mathbb{F}_2)\times H^1(X_q,\mathbb{F}_2)\xrightarrow{\cup}H^3_c=\mathbb{Z}/2,\qquad
[(p)]\cup[\Sigma]=\mathrm{lk}_2(p,q).$$
The PUNCHLINE (eq. (2.2)): the Legendre symbol is nothing but the mod-2 linking number, and the
Gauss reciprocity law corresponds to the SYMMETRY of the linking number:
$$\mathrm{lk}(K,L)=\mathrm{lk}(L,K)\ \longleftrightarrow\ \left(\tfrac{p}{q}\right)=
\left(\tfrac{q}{p}\right)\quad(p,q\equiv1\bmod4).$$
Two further faces (eqs. (2.3)-(2.4)): the Gauss-sum expression
$(\sum_{x\in\mathbb{F}_p}\zeta^{x^2})^{q-1}=(p/q)$ is the $\mathbb{F}_p$ analogue of the Gaussian
integral $\int e^{-x^2}$; and Gauss's electromagnetic linking integral
$\int_K\int_L\omega(x-y)=\mathrm{lk}(K,L)$ has a Chern-Simons/abelian-BF gauge-theoretic Feynman
form, an infinite-dimensional Gaussian, so (2.3) and (2.4) are analogues.

**§3 Link groups and pro-$l$ Galois groups (pp.9-12).** The huge group $G_S=
\pi_1(\mathrm{Spec}\,\mathbb{Z}\setminus S)$ is approached via its maximal pro-$l$ quotient
$G_S(l)$. Milnor (Thm 3.1, via K.T. Chen) and its pro-$l$ refinement (Thm 3.2): the pro-$l$
link group of an $n$-component link in a homology sphere is $\widehat{G_L}=\langle x_1,\dots,
x_n\mid[x_1,y_1]=\dots=[x_n,y_n]=1\rangle$ ($x_i$ meridian, $y_i$ pro-$l$ longitude). Koch's
theorem (Thm 3.4/3.5) is the exact arithmetic mirror: for $S=\{p_1,\dots,p_n\}$ with
$p_i\equiv1\bmod l$,
$$G_S(l)=\langle x_1,\dots,x_n\mid x_i^{p_i-1}[x_i,y_i]=1\ (1\le i\le n)\rangle,$$
$x_i$ = monodromy $\tau_i$, $y_i$ = extended Frobenius $\sigma_i$, with $\sigma_j\equiv
\prod_{i\ne j}\tau_i^{\mathrm{lk}_l(p_i,p_j)}$ and $\zeta_l^{\mathrm{lk}_l(p_i,p_j)}=
(p_j/p_i)_l$ the $l$-th power residue symbol. The relations $x_i^{p_i-1}[x_i,y_i]=1$ trace
back exactly to the local fundamental groups (1.2). Theorem 3.3 (Murasugi conjecture, pro-$l$
version via Anick) and Theorem 3.6 (arithmetic Murasugi for $l>2$) give the lower-central-series
ranks $a_d$ via $\prod_{d\ge1}(1-t^d)^{a_d}=(1-t)(1-nt+nt^2)$ when the mod-$l$ linking graph is
a circuit. For $l>2$ the linking number $\mathrm{lk}_l(p_i,p_j)$ is NOT symmetric (no reciprocity
in higher residues), which is why the genus-theory analogue lives at $l=2$.

**§4 Milnor invariants and multiple power residue symbols (pp.12-17).** Milnor's
$\bar\mu$-invariants $\bar\mu(I)$ (higher linking numbers, defined via Magnus expansion of a
longitude and the Fox free differential calculus; Thm 4.1: $\bar\mu(ij)=\mathrm{lk}(K_i,K_j)$,
with cyclic-symmetry and shuffle relations) have an arithmetic analogue $\overline{\mu_m}(I)$
built from the pro-$l$ Magnus expansion of Frobenius over the monodromies (Thm 4.5). The
arithmetic Milnor invariants are interpreted as MASSEY PRODUCTS in the etale cohomology of
$X_S=\mathrm{Spec}(\mathbb{Z})\setminus S$ (Thm 4.9), generalizing the cup-product = power
residue symbol relation of §2 to triple and higher symbols. Redei's triple symbol
$[p_1,p_2,p_3]=(-1)^{\mu_2(123)}$ is recovered (Example 4.7): for $l=2$,
$p_i\equiv1\bmod4$, there is a dihedral-$D_8$ extension, and $[p_1,p_2,p_3]$ measures whether
$p_3$ splits completely. Example: $S=\{13,61,937\}$ are "mod-2 Borromean primes"
($\mu_2(ij)=0$ for all pairs, $\mu_2(123)=1$), exactly mirroring the Borromean rings
($\mathrm{lk}=0$ pairwise, $\mu(123)=\pm1$).

**§5 Homology groups and ideal class groups (pp.17-20).** The dictionary
$H_1(M)\leftrightarrow$ ideal class group $H_k$ (eq. (5.1)): all knots generate 1-cycles, the
boundaries $\partial\Sigma$ are the relations, mirroring $k^\times\to I_k$, $a\mapsto(a)$.
Gauss's GENUS THEORY is recovered as the analogue of a link genus theory. For $k/\mathbb{Q}$
quadratic ramified over $n$ odd primes, two ideals are in the same genus iff
$(NI/p_i)=(NJ/p_i)$ for all $i$, and the genus map gives $H_k/H_k^2\simeq\{(u_i)\in\{\pm1\}^n
\mid\prod u_i=1\}\simeq(\mathbb{Z}/2)^{n-1}$. The topological mirror: for a double cover
$f:M\to S^3$ branched along an $n$-component link, $H_1(M)/2H_1(M)\simeq(\mathbb{Z}/2)^{n-1}$
via $[c]\mapsto(\mathrm{lk}(f_*c,K_i)\bmod2)$. Redei's matrix expressing the 4-rank of $H_k(2)$
is THE MOD-2 LINKING MATRIX (Cor 5.3: $T_L(i,i)=-\sum_{j\ne i}\mathrm{lk}(K_i,K_j)$,
$T_L(i,j)=\mathrm{lk}(K_i,K_j)$), and higher $2^d$-ranks come from a "higher linking matrix"
$T_L^{(d)}$ built from the Milnor numbers (Thm 5.2: it is a presentation matrix of the
$\widehat{\mathcal{O}}/\mathfrak{p}^d$-module $H_1(M)(l)\oplus\widehat{\mathcal{O}}/\mathfrak{p}^d$).
This is a genuine integer-valued symmetric-pairing structure (the linking matrix) controlling
an arithmetic invariant (the class-group 2-part).

## Points mapped to the project

1. **The Legendre symbol = a cup-product intersection number, and reciprocity = the symmetry
   of that pairing (§2, eqs. (2.1)-(2.2)).** This is the direct conceptual rhyme with
   Direction 8 and the most important point. An arithmetic reciprocity law (the symmetry of a
   prime-prime pairing) IS the symmetry of a cup-product intersection form on an arithmetic
   3-manifold. Direction 8 wants RH to be the SIGNATURE of an intersection form on the
   arithmetic SURFACE $\mathrm{Spec}(\mathbb{Z})^2$. Same move (arithmetic statement = property
   of an intersection pairing), one arithmetic dimension up: Morishita pairs two primes (knots)
   in a 3-manifold and reads off symmetry; Direction 8 pairs the diagonal against the Frobenius
   correspondence on a surface and reads off a definite signature. Morishita is the
   3-manifold shadow of the surface intersection theory Direction 8 builds. ->

2. **The signed datum is real and already machine-checkable in the simplest case (§2, §5).**
   The mod-2 linking number / Legendre symbol is a $\pm1$ (an $\mathbb{F}_2$ pairing), the
   simplest possible "signature" datum, and Redei's mod-2 linking matrix (§5, Cor 5.3) is an
   honest symmetric integer matrix whose rank computes a class-group invariant. The
   "arithmetic law = property of an intersection pairing" template is therefore not aspirational;
   it is concrete and finite in the two-prime / quadratic case, the natural baby instance to
   pin down before the surface lift. ->

3. **The infinite prime is forced to be the end / one-point compactification (§1, eq. (1.3)).**
   $\mathrm{Spec}(\mathbb{Z})$ is $\mathbb{R}^3$ and only becomes the closed $S^3$ after adding
   $\infty$. This is the archimedean place that 2I treats and that Direction 8 must include to
   compactify its surface and get a finite signature. Morishita's "infinite prime = end of a
   non-compact 3-manifold" is the topological reason the archimedean place must be added by
   hand, the same compactification 2K's "absolute base point" is reaching for. Ties directly to
   2I and 2K. ->

4. **Local Frobenius/monodromy structure at one prime (§1, eq. (1.2); §3 Koch).** The
   meridian-longitude torus boundary, with longitude = Frobenius $\sigma$ and meridian =
   inertia $\tau$, is the topological picture of the same Frobenius-at-$p$ that $\Gamma_S$
   (2Q/2R) carries with its place-dependent $(1,p)$ bidegree. Koch's relation
   $x_i^{p_i-1}[x_i,y_i]=1$ is the local-fundamental-group data assembled across primes, the
   group-theoretic precursor of assembling $\Gamma_S$ from local pieces (2Q). Morishita supplies
   the geometric object (a knotted $S^1$ with torus boundary) whose self-intersection 2R
   computed as $-\zeta'/\zeta$. ->

5. **Reciprocity is symmetric only at $l=2$; higher residues are not (§3, §4).** For $l>2$ the
   power residue symbol $\mathrm{lk}_l(p_i,p_j)$ is not symmetric, which is why genus theory
   (§5) and the clean signature reading live at $l=2$. This is a useful caution for Direction 8:
   the "symmetry of the pairing" picture is cleanest for the quadratic ($\mathbb{F}_2$,
   signature-$\pm1$) datum, and the higher-order structure (Milnor numbers, Massey products) is
   genuinely non-symmetric tensor data, not a single signature. The Direction-8 surface form is
   symmetric (an intersection form), so it is the $l=2$-flavored object, not the
   higher-Milnor-invariant object. ->

6. **A second, INDEPENDENT geometric language for the prime embedding, with the "no constant
   field" wall stated sharply (§1, p.6).** Direction 8 works in the curves-over-$\mathbb{F}_q$
   / intersection-on-a-surface language (2G $C\times C$). Morishita gives the orthogonal
   3-manifold/knot language and is explicit that the number ring is NOT a curve over a base
   field (the same wall as 2K/Leichtnam's "no Frobenius lift for $g\ge2$"). His framing says
   the missing object is a 3-manifold-analogue, not a curve-analogue. Direction 8's bet is the
   2-arithmetic-dimensional product surface; Morishita's MKR bet is a 3-real-dimensional
   manifold. Holding both is cheap insurance: the "$\times$ a second copy" theme is exactly
   where the two pictures meet. ->

## What this changes for the program

- **Reciprocity-as-pairing-symmetry is the recurring Direction-8 signal, now sourced to its
  cleanest finished form.** The §2 cup-product realization of the Legendre symbol is the
  3-manifold precursor of the Direction-8 thesis (RH = signature of a surface intersection form).
  It proves nothing for $\zeta$, but it establishes that the "arithmetic law = property of an
  intersection pairing" template is real, finite, and machine-checkable in the $\mathbb{F}_2$,
  two-prime case. Pair this with the AHK note (a Hodge-Riemann SIGNATURE with no variety) and
  the Hartshorne note (the classical surface signature being lifted): Morishita supplies the
  symmetry, AHK supplies the definiteness, Hartshorne supplies the surface.
- **A concrete baby target.** Before attempting $\mathrm{Spec}(\mathbb{Z})^2$, the Redei mod-2
  linking matrix (§5) is a small symmetric integer pairing already controlling an arithmetic
  invariant. If the project wants a sandbox for "intersection form controls arithmetic," this
  is it, one dimension down and fully explicit.
- **The infinite prime as compactification is triply confirmed.** §1 (here) + the Li-Sia note +
  the Deninger archimedean-stationary-point picture all force $\infty$ to be the by-hand
  compactifying point. This is a fixed structural fact for 2I/2K, not an open question.
- **The non-symmetry of higher residues warns against over-reaching.** The clean symmetric
  signature lives at the quadratic level; Direction 8's symmetric surface form is the right
  analogue of that, not of the higher (non-symmetric) Milnor/Massey data.

## Status

Read DEEPLY pp.1-20 (Introduction; §1 knots-primes dictionary incl. local (1.2) and global
(1.3); §2 linking numbers and Legendre symbols incl. both cup-product realizations and the
reciprocity = symmetry punchline (2.2); §3 Koch/Milnor pro-$l$ presentations; §4 Milnor
invariants, Magnus/Fox calculus, Massey products, Redei triple symbol; §5 ideal class groups,
Gauss genus theory, Redei mod-2 linking matrix and higher linking matrices). Sections 6-8
(3-manifold coverings vs class field extensions, Alexander-Fox/Iwasawa torsion theory,
moduli/deformations of knot and prime group representations) read via the contents and section
heads only; they are not load-bearing for Direction 8. This is an expository survey, not a
theorem paper. The load-bearing point for Direction 8 is the §2 cup-product realization of the
Legendre symbol and the reciprocity = symmetry-of-the-pairing identity (2.2).
