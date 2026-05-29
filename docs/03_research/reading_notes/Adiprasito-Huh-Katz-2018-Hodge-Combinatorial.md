# Reading notes: Adiprasito, Huh, Katz, *Hodge Theory for Combinatorial Geometries* (arXiv:1511.02888v2, Ann. of Math. 2018)

> Intersection/Hodge entry, and the direct source for Direction 8 attack angle 4.A
> (tropical Hodge index lifted to the arithmetic surface). Folder
> [`references/06_intersection_hodge/`](../../../references/06_intersection_hodge/).
> This is the paper that proves the Hard Lefschetz theorem and the Hodge-Riemann relations
> for the Chow ring of an ARBITRARY matroid, with no underlying variety. It is the proof
> that a Hodge-index-type SIGNATURE can exist on a purely combinatorial object that is not
> a projective variety, which is exactly the move Direction 8 needs ($\mathrm{Spec}(\mathbb{Z})^2$
> is not a classical projective surface either). Read order: read alongside Hartshorne Ch V
> (the classical surface case the tropical version generalizes) and Voisin Ch 6.3/7 (the
> Hodge index / Hodge-Riemann relations being generalized). Pages refer to the PDF. Read:
> pp.1-8 (§1 introduction with the main theorem 1.4; §2 finite sets, fans, Bergman fans).

## One-line takeaway

AHK build a Chow ring $A^*(\mathrm{M})_\mathbb{R}$ for any matroid $\mathrm{M}$ and prove
it satisfies Poincare duality, the Hard Lefschetz theorem, AND the Hodge-Riemann relations
(Theorem 1.4), DESPITE there being no projective variety underneath when $\mathrm{M}$ is
not realizable. The Hodge-Riemann relations give a bilinear form $Q^q_\ell$ that is
**definite (up to sign) on primitive classes**: that signed-definiteness IS a Hodge-index
signature, manufactured combinatorially. This is the existence proof that the Direction-8
signature can live on a non-variety, the precise content of attack angle 4.A.

## The points that matter, mapped to the project

1. **Theorem 1.4: Hard Lefschetz + Hodge-Riemann for an arbitrary matroid's Chow ring (p.4).**
   For $\ell$ from a strictly submodular function: (1) multiplication $L^q_\ell: A^q\to A^{r-q}$
   is an isomorphism (Hard Lefschetz), and (2) the form $Q^q_\ell(a_1,a_2)=(-1)^q\deg(a_1\cdot
   L^q_\ell a_2)$ is symmetric and **positive definite on the kernel of $\ell\cdot L^q_\ell$**
   (Hodge-Riemann). The proof goes through the Hodge-Riemann relations for ANY strictly convex
   piecewise-linear function on the tropical linear space (Bergman fan) $\Sigma_\mathrm{M}$
   (Theorem 8.8).
   -> This is attack angle 4.A in its source form. The Hodge-Riemann relations are precisely
   a SIGNATURE statement: the intersection form is positive definite on a primitive subspace
   and the global signature is fixed by the $(-1)^q$ sign pattern. Direction 8's milestone is
   "signature $(1,k)$, the primitive form negative definite" on the arithmetic surface. AHK
   proves the matroid/tropical analogue of exactly that statement and, decisively, proves it
   WITHOUT a variety. The lift Direction 8 wants is: replace the Bergman fan $\Sigma_\mathrm{M}$
   by a tropical/combinatorial model of $\mathrm{Spec}(\mathbb{Z})^2$ and run the same machine.

2. **The signature exists with no projective variety underneath (§1.1-1.2, pp.3-4).** AHK are
   explicit that $A^*(\mathrm{M})_\mathbb{R}$ is the Chow ring of a smooth but NON-COMPACT toric
   variety $X(\Sigma_\mathrm{M})$, "Chow equivalent" to a projective variety if and only if
   $\mathrm{M}$ is realizable; for non-realizable $\mathrm{M}$ "there is no reason to expect a
   working Hodge theory," yet they prove one exists anyway. The proof is McMullen-style induction
   on the fan (matroidal flips), not Hodge theory of a variety.
   -> This is the load-bearing methodological fact for Direction 8. $\mathrm{Spec}(\mathbb{Z})^2$
   is not a classical projective surface (no base field, no $\mathbb{C}$-points giving Kahler
   Hodge theory), so the classical Hodge index theorem (Voisin 6.3, Hartshorne V.1) does not
   apply directly. AHK demonstrate the signature can be obtained by a purely combinatorial /
   inductive route that bypasses the variety. Direction 8's bet is that the arithmetic surface
   admits a similar bypass. AHK is the proof of concept that "no variety" is not fatal to "has
   a Hodge index signature."

3. **The Hodge-Riemann relations are STRONGER than Hard Lefschetz, and they are what closes
   the target inequality (§1, p.4; §9 cited).** AHK note Hodge-Riemann implies Hard Lefschetz,
   and that it is the Hodge-Riemann relations (the definiteness, i.e. the signature), not merely
   Hard Lefschetz, that proves the log-concavity conjectures (Conjectures 1.1, 1.2) via reading
   the characteristic-polynomial coefficients as intersection numbers (§9).
   -> Direct rhyme with the project's marginal-positivity thesis. The PROOF needs the definite
   (signature) statement, not the weaker isomorphism (Hard Lefschetz) statement. Mirror of the
   in-house finding that RH lives at Level 4 (positivity/signature), not Level 3
   (spectral/isomorphism): a Lefschetz isomorphism is compatible with a wrong-signature world,
   the definiteness is what forces the bound. The BH17 counterexample AHK cite (a tropical
   variety with Poincare duality + Hard Lefschetz but NOT Hodge-Riemann) is the tropical
   D-H-discipline analogue: an object that passes every test except the signature one, proving
   the signature is the real content.

4. **Reduced characteristic polynomial coefficients = intersection numbers (§9, summarized p.5).**
   The coefficients $w_k(\mathrm{M})$ of the characteristic polynomial are identified with
   intersection numbers in the Chow ring, and log-concavity $w_{k-1}w_{k+1}\le w_k^2$ falls out
   of the Hodge-Riemann signature.
   -> Template for what Direction 8 must produce on $\mathrm{Spec}(\mathbb{Z})^2$: the zeta /
   $L$-function data (here the characteristic polynomial; there $\zeta$ via $\Gamma_S^2=-\zeta'/\zeta$,
   per 2R/2Q) should be readable as intersection numbers, and RH should fall out of the signature
   of the form pairing those numbers. AHK is the cleanest finished instance of "arithmetic/combinatorial
   invariant = intersection number, inequality = Hodge index signature."

5. **The machinery: Bergman fan, order filters, matroidal flips, deg map (§2, pp.5-8).** The
   Chow ring is built from the poset of flats; the geometry is a complete unimodular fan
   $\Sigma_\mathrm{M}$ obtained from the standard simplex fan by stellar subdivisions; "deg" is
   the canonical $A^r(\mathrm{M})\cong\mathbb{R}$ isomorphism normalized by $\deg(x_{F_1}\cdots
   x_{F_r})=1$ on flags of flats. The whole proof is fan combinatorics, no schemes.
   -> The concrete toolkit Direction 8's 4.A would adapt. The open question for the project:
   what is the matroid / fan / order-filter structure attached to $\mathrm{Spec}(\mathbb{Z})^2$
   and its Frobenius correspondence $\Gamma_S$? AHK does not answer that (it is about matroids),
   but it gives the exact target shape: a graded ring with Poincare duality, a Lefschetz element
   $\ell$, and a deg map, on which Hodge-Riemann is then proved by induction.

## What this changes for the program

- **Attack angle 4.A now has its primary source pinned.** AHK is the existence theorem that a
  Hodge-index signature can be built combinatorially with no variety underneath. That is the
  whole hope of Direction 8 (lift the signature to $\mathrm{Spec}(\mathbb{Z})$ where there is
  no projective surface). The note to carry forward: the SIGNATURE (Hodge-Riemann definiteness),
  not Hard Lefschetz, is the content, and it is provable by fan induction.
- **The BH17 example is the tropical D-H discipline.** A tropical variety with Poincare duality
  and Hard Lefschetz but failing Hodge-Riemann is exactly the kind of "passes everything except
  the signature" counterexample the project's wrong-approach detector lives for. Any Direction-8
  construction must produce the Hodge-Riemann definiteness, not just duality + Lefschetz, or it
  is the BH17 world.
- **Concrete next-step shape, not yet a computation.** Direction 8's 4.A needs a fan / matroid
  model of $\mathrm{Spec}(\mathbb{Z})^2 + \Gamma_S$. AHK gives the target ring structure
  (graded, Poincare duality, deg, Lefschetz $\ell$ from a submodular function) the model would
  have to realize. No project-native computation lands from this paper directly; it is the
  structural blueprint for 4.A.

## Status

Read pp.1-8 (§1 introduction including the main Theorem 1.4 statement and the realizability /
BH17 discussion; §2 finite sets, polyhedra, Bergman fans and order filters). The actual proofs
of Hard Lefschetz and Hodge-Riemann are in §§7-8 (not read in detail; the §1 statements and the
§9 application logic are what matter for 4.A). This is the highest-relevance paper of the five
for the live Direction-8 front: it is the existence proof for a no-variety Hodge-index signature.
