# Reading notes: Morishita, *Analogies between Knots and Primes, 3-Manifolds and Number Rings* (arXiv:0904.3399, 2009)

> Arithmetic-topology dictionary entry. Folder
> [`references/05_arithmetic_topology/`](../../../references/05_arithmetic_topology/).
> This is the foundational survey of the MKR (Mazur-Kapranov-Reznikov) dictionary:
> primes are knots, $\mathrm{Spec}(\mathcal{O}_k)$ is a 3-manifold, the linking number
> is the Legendre symbol. It is the source paper behind the Li-Sia tutorial notes (same
> folder) and the reference the Morishita bridge (2K, arXiv:2508.15971) extends.
> Read order: read this first, then Li-Sia for the worked undergraduate version. Pages
> refer to the PDF. Read: pp.1-9 (intro, §1 knots and primes, §2 linking numbers and
> Legendre symbols).

## One-line takeaway

A prime $\mathrm{Spec}(\mathbb{F}_p) \hookrightarrow \mathrm{Spec}(\mathbb{Z})$ is the
arithmetic analogue of a knot $S^1 \hookrightarrow S^3$, because $\mathrm{Spec}(\mathbb{F}_p)$
is etale-homotopically a $K(\hat{\mathbb{Z}},1) = S^1$ and $\mathrm{Spec}(\mathbb{Z})\cup\{\infty\}$
has the Artin-Verdier 3-dimensional Poincare duality of $S^3$. The whole dictionary
(meridian/inertia, longitude/Frobenius, linking number/Legendre symbol, knot group/decomposition
group) follows from this one analogy, and crucially it gives the project a SECOND,
independent geometric language for "how a prime sits inside $\mathrm{Spec}(\mathbb{Z})$"
that is NOT the curves-over-$\mathbb{F}_q$ language Direction 8 lifts.

## The points that matter, mapped to the project

1. **$S^1 \leftrightarrow \mathrm{Spec}(\mathbb{F}_q)$ and $S^3 \leftrightarrow \mathrm{Spec}(\mathbb{Z})\cup\{\infty\}$ (§1, (1.1)-(1.3)).**
   $S^1 = K(\mathbb{Z},1)$ and $\mathrm{Spec}(\mathbb{F}_q) = K(\hat{\mathbb{Z}},1)$
   etale-homotopically; the loop $\leftrightarrow$ Frobenius. Artin-Verdier (1965, the
   Tate-Artin-Verdier 3-dimensional Poincare duality for the etale cohomology of a number
   ring) is what makes $\mathrm{Spec}(\mathcal{O}_k)$ a 3-manifold. The infinite prime is
   the "end" / point at infinity making $\mathrm{Spec}(\mathbb{Z})\cup\{\infty\}$ a closed
   $S^3$ (Hermite-Minkowski $\Rightarrow \pi_1(\mathrm{Spec}(\mathbb{Z}))=1$, the analogue
   of the Poincare conjecture).
   -> This is the archimedean place $\infty$ that 2I treats and that Direction 8 needs to
   include to compactify the surface. Morishita's "infinite prime = end of a non-compact
   3-manifold" is the topological reason the archimedean place must be added by hand, the
   same compactification 2K's "absolute base point" is reaching for.

2. **Meridian $\leftrightarrow$ inertia, longitude $\leftrightarrow$ Frobenius (§1, (1.2)).**
   The peripheral group $\pi_1(\partial V) = \langle \alpha,\beta \mid [\alpha,\beta]=1\rangle$
   maps to the tame quotient $\pi_1^{tame}(\mathrm{Spec}(k_\mathfrak{p})) = \langle \tau,\sigma
   \mid \tau^{q-1}[\tau,\sigma]=1\rangle$: meridian $\alpha \leftrightarrow$ monodromy/inertia
   $\tau$, longitude $\beta \leftrightarrow$ Frobenius $\sigma$.
   -> This is the LOCAL structure at one prime. It is the same Frobenius-at-$p$ that
   $\Gamma_S$ (2Q/2R) carries with its place-dependent $(1,p)$ bidegree. Morishita supplies
   the topological picture (a knotted $S^1$ with a meridian-longitude torus boundary) for
   the object whose self-intersection 2R computed as $-\zeta'/\zeta$.

3. **Linking number = Legendre symbol = an intersection/cup product (§2, (2.1)-(2.2)).**
   The mod-2 linking number $\mathrm{lk}_2(p,q)$ is defined via the Frobenius conjugacy class
   in $\mathrm{Gal}(Y_p/X_p) = \mathbb{Z}/2$, giving $(-1)^{\mathrm{lk}_2(p,q)} = (p/q)$.
   Crucially Morishita realizes it as a **cup product** of cohomology classes:
   $H^2_c(X_q,\mathbb{F}_2)\times H^1(X_q,\mathbb{F}_2) \xrightarrow{\cup} H^3_c = \mathbb{Z}/2$,
   $[(p)]\cup[\Sigma] = \mathrm{lk}_2(p,q)$, and quadratic reciprocity $\mathrm{lk}(K,L)=\mathrm{lk}(L,K)$
   is the SYMMETRY of this pairing.
   -> Direct conceptual rhyme with Direction 8. Here a reciprocity law (the symmetry of a
   prime-prime pairing) IS the symmetry of a cup-product intersection form on an arithmetic
   3-manifold. Direction 8 wants RH to be the SIGNATURE of an intersection form on an
   arithmetic surface ($\mathrm{Spec}(\mathbb{Z})^2$). Same move (arithmetic statement =
   property of a cup product), one dimension up: Morishita pairs two primes (knots) in a
   3-manifold; Direction 8 pairs the diagonal and Frobenius correspondence on a 4-real-dimensional
   surface. Morishita is the 3-manifold shadow of the surface intersection theory Direction 8 builds.

4. **The Gauss linking integral as a Feynman/Gaussian integral (§2, (2.3)-(2.4)).**
   The Legendre symbol is a Gauss sum $(\sum_{x}\zeta^{x^2})^{q-1}=(p/q)$, the $\mathbb{F}_p$
   analogue of the Gaussian integral $\int e^{-x^2}$; and the linking number has a
   gauge-theoretic (Chern-Simons / abelian BF) integral expression.
   -> Tangential to Direction 8 but worth flagging: this is the QFT/path-integral face of
   the same pairing, the same gauge-theory thread Connes-Consani and the Deninger foliated-flow
   picture (Leichtnam note, point 2.4) live in. A possible bridge if Direction 8's signature
   ever wants a partition-function interpretation.

5. **Why number rings are NOT curves over $\mathbb{F}_q$ (§1, p.6).** Morishita is explicit:
   a curve $C/\mathbb{F}_q$ is a surface-bundle over the "circle" $\mathrm{Spec}(\mathbb{F}_q)$
   (exact sequence $1\to\pi_1(C\otimes\bar{\mathbb{F}}_q)\to\pi_1(C)\to\pi_1(\mathrm{Spec}\,\mathbb{F}_q)\to1$),
   but a number ring HAS NO CONSTANT FIELD, so $\pi_1(\mathrm{Spec}\,\mathcal{O}_k)$ behaves
   like a random 3-manifold group, NOT like $\pi_1(C)$. Iwasawa's $\mathbb{Z}_p$-tower is
   ramified, so it is the analogue of cyclic coverings branched along a knot, not the
   unramified constant-field extension.
   -> This is the SAME wall as 2K/Leichtnam's "no Frobenius lift for $g\ge2$": the
   function-field template (Direction 8's 2G $C\times C$ source) does not transfer naively
   because $\mathrm{Spec}(\mathbb{Z})$ lacks the base field. Morishita's framing says the
   missing object is not a curve-analogue but a 3-manifold-analogue. Direction 8's bet is
   that the right object is the surface $\mathrm{Spec}(\mathbb{Z})\times\mathrm{Spec}(\mathbb{Z})$;
   Morishita's MKR dictionary is the rival/complementary bet that the right object is
   genuinely 3-dimensional. Useful to hold both: the product surface is 2-arithmetic-dimensional,
   the MKR 3-manifold is 3-real-dimensional. The "$\times$ a second copy" theme is exactly
   where these meet.

## What this changes for the program

- **A second geometric language for the prime $\hookrightarrow \mathrm{Spec}(\mathbb{Z})$
  embedding.** Direction 8 works in the curves-over-$\mathbb{F}_q$ / intersection-on-a-surface
  language (2G). Morishita gives the orthogonal 3-manifold/knot language. Both make
  reciprocity a symmetry of a pairing. Keeping both in view is cheap insurance against
  the "no constant field" wall.
- **Reciprocity-as-pairing-symmetry is a recurring signal.** Point 3 (Legendre symbol =
  cup-product symmetry) is the 3-manifold precursor of the Direction-8 thesis (RH = signature
  of a surface intersection form). It does not prove anything for $\zeta$, but it shows the
  "arithmetic law = property of an intersection pairing" template is real and already
  machine-checkable in the simplest ($\mathbb{F}_2$, two primes) case.
- **The infinite prime is forced to be the end/compactification point.** Confirms 2I/2K:
  the archimedean place is the $\infty$ that closes the manifold, added by hand, not arising
  from the finite-prime structure.

## Status

Read pp.1-9 (intro, §1 knots-primes dictionary, §2 linking numbers and Legendre symbols).
Sections 3-8 (pro-$l$ Galois / link groups, Milnor invariants, Iwasawa theory, deformations)
skimmed via the contents only. This is an expository survey, not a theorem paper; depth here
is appropriate. The cup-product realization of the Legendre symbol (§2) is the load-bearing
point for Direction 8.
