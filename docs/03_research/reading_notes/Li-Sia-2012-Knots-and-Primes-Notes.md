# Reading notes: Li and Sia, *Knots and Primes* (Harvard Summer 2012 Tutorial Notes)

> Arithmetic-topology dictionary entry, undergraduate version. Folder
> [`references/05_arithmetic_topology/`](../../../references/05_arithmetic_topology/).
> These are the clean, self-contained tutorial notes (Chao Li and Charmaine Sia, Harvard
> 2012) built directly on Morishita's textbook *Knots and Primes: An Introduction to
> Arithmetic Topology* (same folder has Morishita's survey). Read order: read AFTER the
> Morishita survey, or BEFORE it as the gentler entry point; the content overlaps and the
> Li-Sia version is more explicit and example-driven. Pages refer to the PDF. Read: pp.1-8
> (Lecture 1: the knots-primes dictionary table; Lecture 2: quadratic reciprocity and the
> Legendre symbol).

## One-line takeaway

The same MKR dictionary as Morishita, but with a complete one-page TABLE (Table 1, p.3)
giving every analogy at a glance, and with quadratic reciprocity worked through in full
undergraduate detail. The reason $\mathrm{Spec}(\mathbb{Z})$ is $\mathbb{R}^3$ (not $S^3$):
$\pi_1^{et}(\mathrm{Spec}\,\mathbb{Z})=1$ and Artin-Verdier duality give 3-dimensional
Poincare duality, and the correct $S^3$ is $\mathrm{Spec}(\mathbb{Z})\cup\{\infty\}$ (the
prime at infinity). This is the project's reference for the dictionary in its most usable form.

## The points that matter, mapped to the project

1. **The full dictionary table (Lecture 1, Table 1, p.3).** One table giving:
   $S^1=K(\mathbb{Z},1)\leftrightarrow\mathrm{Spec}(\mathbb{F}_q)=K(\hat{\mathbb{Z}},1)$;
   loop $\leftrightarrow$ Frobenius $\sigma$; 3-manifold $M \leftrightarrow$ number ring
   $\mathrm{Spec}(\mathcal{O}_k)$; knot $\leftrightarrow$ prime; tubular neighborhood
   $V \leftrightarrow \mathrm{Spec}(\mathcal{O}_\mathfrak{p})$; boundary $\partial V
   \leftrightarrow \mathrm{Spec}(k_\mathfrak{p})$; linking number $\leftrightarrow$ Legendre
   symbol; $\mathrm{lk}(L,K)=\mathrm{lk}(K,L)\leftrightarrow$ quadratic reciprocity;
   Alexander polynomial $\leftrightarrow$ Iwasawa polynomial.
   -> This is the project's single-glance reference for the arithmetic-topology language.
   The line that matters for Direction 8: linking number $\leftrightarrow$ Legendre symbol,
   and its SYMMETRY $\leftrightarrow$ reciprocity. The bottom Iwasawa row
   ($\det(T\cdot\mathrm{id}-(\gamma-1) \mid H_\infty)$) is the characteristic-polynomial /
   determinant face that 2R's $\det_\zeta$ and the Alexander-polynomial analogy share.

2. **$\mathrm{Spec}(\mathbb{F}_p)$ has $\pi_1^{et}=\hat{\mathbb{Z}}$, only one nonzero
   homotopy group, hence $= S^1$ (Lecture 1, p.2).** Because $\pi_1(S^1)=\mathbb{Z}=
   \mathrm{Gal}(\mathbb{R}/S^1)$ matches $\pi_1^{et}(\mathrm{Spec}\,\mathbb{F}_p)=
   \mathrm{Gal}(\bar{\mathbb{F}}_p/\mathbb{F}_p)=\hat{\mathbb{Z}}$, and both are $K(\pi,1)$
   spaces.
   -> Same point as Morishita §1, stated with the homotopy groups explicit. Confirms the
   atom of the dictionary: a residue field is a circle, a Frobenius is a loop. This is the
   "$\{\log p\}$ orbit length" of 2R seen as the length of the circle $\mathrm{Spec}(\mathbb{F}_p)$.

3. **$\mathrm{Spec}(\mathbb{Z}) = \mathbb{R}^3$, $S^3 = \mathrm{Spec}(\mathbb{Z})\cup\{\infty\}$
   (Lecture 1, pp.2-3).** Explicit: Artin-Verdier duality is "some sort of Poincare duality
   for 3-manifolds" and $\pi_1^{et}(\mathrm{Spec}\,\mathbb{Z})=1$, so $\mathrm{Spec}(\mathbb{Z})$
   is $\mathbb{R}^3$; the prime at infinity compactifies it to $S^3$.
   -> The archimedean place $\infty$ (2I) is the one-point compactification that closes the
   manifold. Direction 8 must include it to compactify the surface and get a finite signature;
   Li-Sia gives the cleanest statement of why $\infty$ is exactly the compactifying point.

4. **Quadratic reciprocity from the Legendre symbol as a group homomorphism (Lecture 2,
   §3, Prop 3.7-3.9).** The Legendre symbol is the quotient map $\mathbb{F}_p^\times\to\{\pm1\}$
   with kernel the squares $(\mathbb{F}_p^\times)^2$ (index-2 subgroup), Euler's criterion
   $(a/p)=a^{(p-1)/2}$, and reciprocity emerges as the symmetry that the dictionary identifies
   with $\mathrm{lk}(K,L)=\mathrm{lk}(L,K)$.
   -> The arithmetic content under the topological picture. For Direction 8 the relevant
   abstraction is: an index-2 quotient (a sign, a $\pm1$) is the simplest possible "signature"
   datum, and reciprocity is its symmetry. The Direction-8 signature (Hodge index, signature
   $(1,k)$, primitive form negative definite) is the high-dimensional generalization of "a
   sign attached to a pairing of two primes is symmetric."

5. **Knot group / Wirtinger presentation $\leftrightarrow$ prime group / decomposition group
   (Lecture 1, §2; Lecture 2 trefoil example).** $G_K=\pi_1(S^3\setminus K)$ with Wirtinger
   presentation $\leftrightarrow$ $G_{\{p\}}=\pi_1^{et}(\mathrm{Spec}(\mathcal{O}_k)\setminus\{p\})$;
   $G_K\cong G_L \Leftrightarrow K\sim L$ matches $G_{\{p\}}\cong G_{\{q\}}\Leftrightarrow p=q$.
   -> Not directly Direction 8, but it pins the "how a prime is knotted in $\mathrm{Spec}(\mathbb{Z})$"
   group-theoretic invariant. This is the $\pi_1$ side of the same object whose intersection-theoretic
   side Direction 8 studies. Worth knowing the two descriptions are of the same embedding.

## What this changes for the program

- **Best single reference for the dictionary.** Where Morishita is the survey, Li-Sia is the
  textbook-clean version with the all-in-one table and full reciprocity proof. Cite Li-Sia
  Table 1 for the dictionary, Morishita §2 for the cup-product realization.
- **Reinforces the same two structural facts as the Morishita note.** (a) The archimedean
  place is the compactifying $\infty$ (point 3), and (b) reciprocity is the symmetry of a
  pairing / the simplest signature datum (points 1, 4). These are the two threads that touch
  Direction 8.
- **No new theorem for $\zeta$.** This is pedagogy, not research. Its value is as the readable
  on-ramp to the arithmetic-topology language and as the cleanest statement of why $\infty$
  closes the manifold.

## Status

Read pp.1-8 (Lecture 1 full dictionary + Table 1; Lecture 2 quadratic reciprocity and Legendre
symbol). Later lectures (Alexander/Iwasawa polynomials, genus theory) skimmed via the table
only. These are undergraduate tutorial notes; depth here is appropriate. Load-bearing for the
project: Table 1 (the dictionary) and the $\mathrm{Spec}(\mathbb{Z})\cup\{\infty\}=S^3$ statement.
