# Reading notes: Bhatt-Morrow-Scholze, *Topological Hochschild homology and integral p-adic Hodge theory* (BMS2)

> Folder `references/01_prismatic_cohomology/`. The BMS2 paper: the THH / filtration
> precursor to prismatic cohomology. It reconstructs the BMS1 A_inf-cohomology (and a
> Breuil-Kisin refinement over O_K, K discretely valued) out of **topological cyclic
> homology** TC, equipping everything with a **motivic-style filtration** whose graded
> pieces are the cohomology. For the program the load-bearing facts are: (a) the
> Frobenius on the cohomology is the same Frobenius as the cyclotomic Frobenius on THH,
> the ultimate source of the phi in all these theories; (b) the Nygaard filtration
> appears here as a complete filtration on TC^- / A_inf-cohomology, the grading a flow
> or a signature would need. Read last of the four prismatic sources (it is the
> homotopy-theoretic backstory; the prismatic site reproves its main theorem more
> cleanly, per Remark 1.3).
> Pages read: pp.1-6 (TOC, §1.1 Breuil-Kisin modules Thm 1.2, §1.2 THH reminder + the
> cyclotomic Frobenius phi_p, §1.3 from THH to BK modules Thm 1.6, §1.4 motivic
> filtrations Def 1.7 / Thm 1.8-1.12).

## One-line takeaway

THH(A) is a circle-equivariant ring spectrum carrying a **cyclotomic Frobenius**
phi_p : THH(A) -> THH(A)^{tC_p}; from it one forms TC^- = THH^{hT} and TP =
THH^{tT}, and pi_0 TC^-(A) acquires a Frobenius endomorphism phi that is "the
ultimate source" of the Frobenius on BMS1's A_inf-cohomology. Building a **motivic /
Postnikov filtration** on TC^-, TP, THH yields a complete exhaustive filtration whose
graded pieces are the A_inf-cohomology (mixed char) or crystalline cohomology (char
p), and whose associated Nygaard filtration matches the classical one. So the
Frobenius and the Nygaard grading both come, at bottom, from algebraic topology.

## The points that matter, mapped to the project

1. **The Frobenius on the cohomology is the cyclotomic Frobenius of THH (§1.2-1.3,
   Thm 1.6).** phi_p : THH(A) -> THH(A)^{tC_p} is an essential, genuinely topological
   feature (provably absent from algebraic Hochschild homology); it induces a
   Frobenius phi on pi_0 TC^-(A;Z_p) ~ pi_0 TP(A;Z_p), which is "the ultimate source
   of the endomorphism phi of RGamma_S(X)" and is a lift of Frobenius mod p
   (justifying the name). Hesselholt's pi_0 TC^-(R) ~ A_inf(R) for perfectoid R (Thm
   1.6) is the starting point.
   -> This traces the program's wanted Frobenius (Gamma_S) all the way down to a
   topological origin. The chain is: cyclotomic Frobenius on THH -> phi on TC^-/TP ->
   phi on A_inf-cohomology (BMS1) -> phi on prismatic cohomology / F on WCart
   (Bhatt-Lurie). For 2Q, the takeaway is that the Frobenius is **forced and canonical
   at every level**, not a choice; the place-dependence 2Q needs has to be engineered
   on top of this canonical phi, since THH gives one cyclotomic Frobenius per prime p
   (the C_p-Tate construction), which is itself the per-prime structure.

2. **The Nygaard filtration is a complete filtration on TC^- coming from a spectral
   sequence (Remark 1.11, §1.4).** For quasisyntomic A, the E_infty-Z_p-algebra
   A_inf-hat = RGamma_syn(A, pi_0 TC^-) carries a complete filtration N^{>=*}, the
   **Nygaard filtration**, identified with the classical Nygaard filtration on
   crystalline cohomology (Thm 1.10 region) and a mixed-char version of it. The
   motivic filtration (Thm 1.12) is the Postinikov / even filtration, graded pieces in
   even degrees, reminiscent of the motivic filtration on algebraic K-theory.
   -> A **graded structure on the cohomology, arising from a filtration with a clean
   spectral sequence**. This is the same Nygaard grading Bhatt-Lurie's Sen operator
   acts on diagonally (by -n). For Direction 8, this is where the grading underlying a
   cup-product / Hodge-star would come from; for Direction 4, it is the filtration the
   regularized determinant det(s - Theta) would be taken over. BMS2 shows the grading
   is not ad hoc: it is the motivic/even filtration of a K-theory-like object.

3. **TP and TC^- are periodic / fixed-point constructions (the trace genre) (§1.2).**
   TP = THH^{tT} (Tate, periodic) and TC^- = THH^{hT} (homotopy fixed points) with a
   canonical map can : TC^- -> TP; syntomic cohomology and the recovery of etale
   cohomology are built as **Frobenius-fixed-point (phi = can)** constructions.
   -> The "fixed points of Frobenius / fiber of (phi - can)" shape is the
   trace-formula / regularized-determinant skeleton (Direction 4.6, det(s - Phi)). 2R
   computed -zeta'/zeta = sum Lambda(n) n^{-s} as a dynamical-zeta log-derivative; the
   periodic-cyclic / fixed-point machinery is the homotopy-theoretic home where such a
   trace of Frobenius lives. The circle action T = S^1 on THH is itself a continuous
   one-parameter symmetry, the closest thing in this paper to a flow.

4. **Everything is assembled by quasisyntomic flat descent from semiperfectoid rings
   (Def 1.7, §1.4, Remark 1.9).** The quasisyntomic site qSyn has a base of quasiregular
   semiperfectoid rings S on which pi_0 TC^-(-;Z_p) is already a sheaf with vanishing
   higher cohomology; AOmega and the filtrations are recovered by descent. Theorem 1.8:
   AOmega ~ RGamma_syn(A, pi_0 TC^-).
   -> This descent-from-perfectoid pattern is the same move BMS1 / Bhatt-Scholze use
   (perfect prisms = perfectoid rings as the computational base). For the program it
   reinforces that the **right base for these constructions is perfectoid /
   semiperfectoid**, the F_1-flavored "maximally ramified" objects; the arithmetic
   surface's base point (2K) should be sought in that world, consistent with
   Bhatt-Lurie's WCart being built from Cartier-Witt divisors on such rings.

5. **The Breuil-Kisin refinement over discretely valued O_K (Thm 1.2).** BMS2 produces
   RGamma_S(X) over S = W(k)[[z]] (Breuil-Kisin ring) with a phi-linear Frobenius,
   recovering A_inf-cohomology after base change, de Rham along theta, crystalline of
   the special fiber along S -> W(k) (z to 0). Frobenius twists (Remark 1.4) force
   torsion in de Rham cohomology to have length a multiple of p.
   -> The Breuil-Kisin ring W(k)[[z]] is a **non-perfect prism with an explicit
   uniformizer-deformation z**: the discrete deformation parameter that, in the
   absolute theory, becomes the Sen/Nygaard direction. For the program this is another
   instance of the per-place "scale with a deformation parameter," the local raw
   material for a global flow.

## What this changes for the program

- **The Frobenius is canonical all the way down to topology.** BMS2 shows phi
  originates in the cyclotomic Frobenius of THH. This is reassurance for the Gamma_S
  program: the Frobenius the construction needs is not a free choice, it is forced.
  The work 2Q identifies (making it place-dependent / gluing over all primes and
  infinity) is the genuine remaining content, not the existence of phi.
- **The Nygaard/motivic filtration is the grading for both Direction 4 and 8.** BMS2
  is where this filtration is shown to be the even/motivic filtration of a K-theoretic
  object, with a clean spectral sequence. A regularized determinant (Direction 4.6) or
  a cup-product signature (Direction 8) would both be defined relative to this grading;
  BMS2 certifies it is structural.
- **Fixed-point / periodic constructions are the trace-formula home.** TC^-, TP, and
  the (phi = can) fiber are the homotopy-theoretic skeleton of the Lefschetz / det(s -
  Phi) statement 2R and Direction 4.6 want. No trace formula for zeta is proved here,
  but the genus of construction matches.
- **Still no signature, and this is the furthest-upstream source.** BMS2 is the
  backstory (THH), not the front. It has Frobenius and grading but no intersection
  form, no flow with zeta-zero spectrum, and (being over O_K / Z_p) no archimedean
  place. For the live front, cite Bhatt-Lurie (absolute, Sen operator) as the working
  substrate and BMS2 as the proof that its Frobenius and Nygaard grading are canonical.

## Status

Read pp.1-6 of the PDF in `references/01_prismatic_cohomology/`: TOC, §1.1 (Breuil-Kisin
modules, Thm 1.2 the S-linear cohomology theory, Remark 1.3 that the prismatic site
reproves it, Remark 1.4 Frobenius twists and torsion), §1.2 (THH reminder, the
cyclotomic Frobenius phi_p, TC^- / TP, the Frobenius on pi_0 TC^-), §1.3 (from THH to
BK modules, Hesselholt Thm 1.6, the quasisyntomic site Def 1.7, Thm 1.8 / 1.10 / 1.11
recovering AOmega and crystalline cohomology), §1.4 (motivic filtrations, Thm 1.12).
The homotopy-theoretic body (§§2-11) was not read.
