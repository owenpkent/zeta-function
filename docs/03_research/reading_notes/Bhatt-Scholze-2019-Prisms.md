# Reading notes: Bhatt & Scholze, *Prisms and prismatic cohomology* (Annals 2022)

> Folder `references/01_prismatic_cohomology/`. This is the founding paper of
> prismatic cohomology, the cohomology substrate Direction 3 names and Direction 4
> wants to run a flow on. Read it for the base definitions (prism, prismatic site,
> structure sheaf, Frobenius), and to settle the first question the program must ask
> of any candidate substrate: is this one-prime or all-primes. Answer: this paper is
> **one-prime** (it opens "Fix a prime p"). The all-primes / absolute theory is the
> companion note Bhatt-Lurie-2022. Read in the order README §01 gives: this first,
> then Bhatt-Lurie (absolute), then the two BMS papers (the precursors).
> Pages read: pp.1-6 (TOC, §1 Introduction through Theorem 1.8, Examples 1.9-1.12).

## One-line takeaway

A **prism** is a pair (A, I): a delta-ring A (a ring with a lift of Frobenius
encoded as a p-derivation) plus an invertible ideal I, with A both p-adically and
I-adically complete and a distinguished-element condition. To a smooth p-adic
formal scheme X over A/I it attaches the **prismatic site** (X/A) and a structure
sheaf O with a Frobenius-semilinear map phi, and the resulting cohomology
RGamma(X/A) specializes to (and refines) crystalline, de Rham, and etale cohomology
all at once. The whole construction is over a **fixed prime p**: it is the
single-prime building block, not the Spec(Z) object the product surface needs.

## The points that matter, mapped to the project

1. **Frobenius is built in, as a delta-structure (Def 1.1, Remark 1.2).** A prism's
   ring A carries phi_A, a lift of the Frobenius on A/p, packaged as a p-derivation
   delta (delta "lowers p-adic order of vanishing by 1"). For p-torsionfree A this
   is literally the datum of a ring map lifting Frobenius mod p. So the Frobenius the
   program keeps reaching for (Gamma_S, the geometric Frobenius correspondence) is
   not an add-on here: it is the defining structure of the coefficient ring.
   -> This is the local-at-p Frobenius. 2Q's finding was that the global Gamma_S must
   carry a **place-dependent (1,p) bidegree, one Frobenius scale per prime**, not the
   single scale q of the function field. Bhatt-Scholze supplies exactly one such
   scale (one phi_A per prism, per p). The program needs to glue these over all p,
   which is precisely why the **absolute** theory (next note) is the relevant one and
   this one is the per-prime input.

2. **The prismatic site probes X by prisms; the structure sheaf carries phi (Def
   1.6, Thm 1.8).** (X/A) is the opposite category of prisms (B,J) over (A,I) with a
   flat cover Spf(B/J) -> X; O sends (B,J) to B. Theorem 1.8 then proves the four
   comparisons: crystalline (I=(p)), Hodge-Tate, de Rham, and etale (A perfect, fixed
   points of Frobenius on RGamma/p^n[1/I]). One theory, all the specializations.
   -> This is the concrete content of "prismatic = the p-adic transversal's
   cohomology." Leichtnam 2006's transversal is locally Z_p^m and his trace-class
   property comes from contraction along it. Bhatt-Scholze is the cohomology theory
   that lives over that Z_p direction. The etale comparison (Frobenius-fixed points
   recover the topological cohomology) is the structural reason a Frobenius/flow can
   sit on this substrate at all: the geometry is recovered as a phi=1 locus.

3. **Hodge-Tate comparison gives a graded structure with Breuil-Kisin twists (Thm
   1.8(2)).** Omega^i_{R/(A/I)}{i} = H^i(RGamma(X/A) tensor A/I), where M{i} is the
   Breuil-Kisin twist M tensor (I/I^2)^{tensor i}. So the cohomology comes filtered,
   with graded pieces the differential forms, each twisted by a power of the
   invertible "scale" ideal I.
   -> The Breuil-Kisin twist is the single-prime ancestor of the **graded /
   bidegree** structure 2Q forces and of the Hodge-type grading Direction 8's
   signature would need. A signature is a (+,-) split on a graded cup-product; the
   Hodge-Tate filtration is where such a grading would have to come from. This paper
   gives it per-prime; the absolute theory globalizes it.

4. **Perfectoid <-> perfect prism, and "perfection" exists in mixed characteristic
   (Thm 1.11, Example 1.9).** Perfect prisms (phi an isomorphism) are equivalent to
   perfectoid rings; every prism has a perfection; A_inf = W(O_C^flat) with I =
   ker(theta) is the perfect prism behind BMS1's A_inf-cohomology (Remark 1.10: the
   "mysterious" Frobenius on A_inf-cohomology is now explained as the Frobenius lift
   on O of the prismatic site).
   -> This pins where the BMS1 A_inf-theory (the next-but-one note) sits inside the
   prismatic picture: it is the perfect-prism case. For the program, the perfect case
   is the rigid one with a clean Frobenius; the **non-perfect** prisms (q-de Rham,
   Breuil-Kisin) are where the deformation parameter lives, and a deformation
   parameter is what a flow (Direction 4 / Deninger's R-flow) needs.

5. **q-de Rham and the q-crystalline prism: a one-parameter deformation (Example
   1.3(4), 1.9(4)).** The prism A = Z_p[[q-1]] with I = ([p]_q), [p]_q the q-analog
   of p, has A/I = Z_p[zeta_p], and qOmega = RGamma(X/A) recovers Scholze's q-de Rham
   complex. The scale here is the q-analog [p]_q, not p.
   -> A genuine one-parameter family sitting inside prismatic cohomology. This is the
   nearest thing in the per-prime theory to a continuous deformation, and it is the
   handle Bhatt-Lurie later turns into the Sen operator / R-flow direction. Worth
   flagging: the program's "Deninger R-flow is forced" (2Q) wants exactly a
   continuous parameter, and q is a discrete shadow of one.

## What this changes for the program

- **The substrate is now named precisely, and it is per-prime.** Direction 3 says
  "prismatic cohomology." Bhatt-Scholze is the definition. But it fixes a prime p
  throughout, so by itself it is the cohomology of one place, the local input to a
  Spec(Z) object, not the object. The product-surface / absolute-base-point gap (2K)
  is not closed here; this is the brick, not the building.
- **Frobenius is structural, not bolted on.** The delta-ring / phi_A is the defining
  datum. This is good news for hosting Gamma_S: the correspondence the program wants
  is the same kind of object the coefficient ring already carries. The mismatch 2Q
  found (one global scale vs one-per-prime) is exactly the gap between this single
  phi_A and a global Gamma_S.
- **Etale comparison = geometry as a phi=1 locus.** This is the structural license
  for a Lefschetz/flow picture (Direction 4.6): fixed points of Frobenius recover the
  topological cohomology, the same shape as a trace-of-Frobenius statement.
- **No signature yet.** The Hodge-Tate filtration provides a grading (Breuil-Kisin
  twists), but this paper proves comparisons, not an index theorem. The (+,-) split
  Direction 8 needs is not here; it would have to be built on the graded structure
  this paper supplies.

## Status

Read pp.1-6 of the PDF in `references/01_prismatic_cohomology/`: the TOC, the full
§1 Introduction (Def 1.1 prism, Remark 1.2 delta-rings, Examples 1.3 of prisms, Def
1.4-1.6 bounded prism + prismatic site + structure sheaf, Prop 1.5, Theorem 1.8 the
comparison package, Examples 1.9-1.12 including q-de Rham and the perfectoid /
perfect-prism equivalence Thm 1.11). The bodies of the comparison proofs (§§4-18)
were not read.
