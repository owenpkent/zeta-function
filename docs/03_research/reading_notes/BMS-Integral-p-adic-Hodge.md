# Reading notes: Bhatt-Morrow-Scholze, *Integral p-adic Hodge theory* (BMS1)

> Folder `references/01_prismatic_cohomology/`. The BMS1 paper the direction docs
> cite (R5 / Direction 3). This is the precursor that prismatic cohomology later
> abstracts: it constructs, for proper smooth formal schemes over O_C (C a complete
> algebraically closed nonarchimedean extension of Q_p), a cohomology theory
> **RGamma_{A_inf}** valued in Fontaine's period ring A_inf = W(O_C^flat), carrying a
> Frobenius phi, that specializes to crystalline, de Rham, and etale cohomology at
> once. It is the **single-place (one C, one perfect prism A_inf)** ancestor of the
> absolute theory. Read after Bhatt-Scholze and Bhatt-Lurie (those are the abstract
> framework; this is the concrete A_inf model the framework was built to explain).
> Pages read: pp.1-6 (TOC, §1.1 Background, §1.2 Results: Theorems 1.1-1.10,
> Breuil-Kisin-Fargues modules Def 1.5, Fargues' classification Thm 1.6).

## One-line takeaway

There is one cohomology theory RGamma_{A_inf}(X), living over all of Spec(A_inf),
with a Frobenius phi that becomes an isomorphism after inverting xi (the generator of
ker(theta : A_inf -> O_C)); restricting it to various big subsets of Spec(A_inf)
recovers crystalline (along A_inf -> W(k)), de Rham (along theta), and etale (invert
mu) cohomology. Its cohomology groups are **Breuil-Kisin-Fargues modules**, the
mixed-characteristic analogue of Dieudonne modules. The headline arithmetic
consequence: crystalline torsion bounds etale torsion, length-by-length, so p-torsion
in characteristic-p de Rham cohomology is forced by p-torsion in characteristic-0
singular homology.

## The points that matter, mapped to the project

1. **One theory over Spec(A_inf), specializing everywhere by restriction (Thm 1.8,
   1.10).** RGamma_{A_inf}(X) is a perfect complex of A_inf-modules with a phi-linear
   Frobenius; the comparisons (i)-(iv) of Thm 1.8 are just base changes along
   different maps out of A_inf (to W(k) for crystalline, theta for de Rham, A_crys,
   invert mu for etale). "The picture is that there is one cohomology theory which
   lives over all of Spec A_inf, and over various big subsets can be described through
   other cohomology theories."
   -> This "one object over a base, all known theories are its restrictions" is the
   template the program wants for **a single cohomology of the arithmetic surface
   whose restrictions to each place give the local data**. A_inf is the single-place
   (one C) case; Bhatt-Lurie's WCart is the all-primes globalization. BMS1 is the
   proof-of-concept that the unification is real.

2. **A Frobenius phi exists even though X carries none, and it comes from the tilt
   (Remark 1.9, Thm 1.8).** There is no Frobenius on X itself (char 0), yet
   RGamma_{A_inf}(X) carries phi: it comes from the Frobenius on the tilt O_C^flat
   (equivalently, on the perfect prism A_inf). phi induces a quasi-isomorphism after
   inverting xi.
   -> This is the structural precedent for putting a **Frobenius correspondence
   Gamma_S on an object with no obvious self-map**. The program's Spec(Z) x Spec(Z)
   has no geometric Frobenius the way a curve over F_q does; BMS1 shows the Frobenius
   can come from the **coefficient ring's tilt / delta-structure**, not from the
   scheme. This is the mechanism by which 2Q's place-dependent Gamma_S can exist at
   all: it lives on the coefficients (A_inf, then WCart), not on the base.

3. **The "scale" element xi and its companion mu (Thm 1.4, Def near A_crys).** xi
   generates ker(theta); mu = [epsilon]-1 with [epsilon] from a compatible system of
   p-power roots of unity; inverting mu gives etale, scalar-extending along theta
   gives de Rham. phi : A_inf[1/xi] ~ A_inf[1/phi^{-1}(xi)], i.e. Frobenius shifts the
   scale.
   -> xi is the **single per-place scale**, the A_inf analogue of the function field's
   q (and of [p]_q in the q-de Rham prism). 2Q's central finding is that over Spec(Z)
   the scale must be **place-dependent**, one xi_p per prime rather than one global q.
   BMS1 gives one xi for one place C; the program needs the family {xi_p}_p plus the
   archimedean factor (2I). The Frobenius-shifts-the-scale relation phi(xi) is the
   local form of the multiplicative-vs-additive tension Leichtnam called "of
   arithmetic nature."

4. **Cohomology groups are Breuil-Kisin-Fargues modules = mixed-char Dieudonne
   modules (Def 1.5, Thm 1.6 Fargues).** A BKF module is a finitely presented
   A_inf-module M with a phi-linear isomorphism M[1/xi] ~ M[1/phi(xi)] that is finite
   free after inverting p. Fargues classifies the finite free ones as pairs (T, Xi),
   T a finite free Z_p-module and Xi a B_dR-lattice. Kisin's mixed-char local shtukas.
   -> A BKF module is a **lattice plus a Frobenius-semilinear isomorphism away from the
   scale**: the linear-algebra shadow of a Frobenius correspondence on cohomology.
   This is the local model for what Gamma_S induces on the program's H^*. The
   "shtuka" framing (a module with a Frobenius meromorphic along a divisor) is
   precisely the function-field-correspondence structure 2G/2Q want to lift; BKF
   modules are that structure realized in mixed characteristic.

5. **Crystalline torsion bounds etale torsion; p-torsion is forced (Thm 1.1(ii),
   eq (1)).** length_{W(k)}(H^i_crys tors / p^n) >= length_{Z_p}(H^i_et tors / p^n),
   giving dim_k H^i_dR >= dim_{F_p} H^i_et. p-torsion classes in char-0 singular
   homology produce nonzero obstructions to integrating forms on any good reduction
   mod p (Remark 1.2: the Enriques surface example, H^1_dR =/= 0 in char 2).
   -> This is an **inequality between two cohomological dimensions extracted from one
   Frobenius-equipped object**. It is not a signature, but it is the same genre as
   Direction 8: a positivity/comparison statement about cohomology forced by the
   arithmetic structure. Worth keeping in view as a worked example of "the integral
   structure forces an inequality between cohomologies," which is the flavor (not the
   content) of a Hodge-index argument.

## What this changes for the program

- **BMS1 is the concrete single-place model; the abstract framework (Bhatt-Scholze,
  Bhatt-Lurie) is what to cite for Spec(Z).** For the live front, the relevant uses
  of BMS1 are: (a) it proves the unification "one Frobenius-equipped cohomology, all
  classical theories by restriction" is achievable; (b) it shows the Frobenius can
  come from the coefficient ring's tilt, the mechanism that lets Gamma_S exist on an
  object with no geometric self-map; (c) BKF modules / shtukas are the local
  linear-algebra model of what Gamma_S induces on H^*.
- **It pins the per-place scale (xi) that 2Q says must become place-dependent.** BMS1
  is one place; the program's task is the family over all p plus infinity. This note's
  job is to mark BMS1 as the local building block, not the global object.
- **No flow, no signature here.** BMS1 has the Frobenius phi but not the continuous
  generator (that is the Sen operator in Bhatt-Lurie) and not an intersection form.
  Its contribution to Direction 8 is only the genre (an inequality between
  cohomologies forced by integral arithmetic structure), not a construction.

## Status

Read pp.1-6 of the PDF in `references/01_prismatic_cohomology/`: TOC, §1.1
Background (Grothendieck's mysterious functor, Fontaine's B_crys conjecture), §1.2
Results through Theorem 1.10 (the comparison package Thm 1.1, the torsion inequality
1.1(ii) and Remarks 1.2-1.3, the functorial recovery Thm 1.4-1.7, Breuil-Kisin-Fargues
modules Def 1.5 and Fargues' classification Thm 1.6, the AOmega-complex theorems 1.8-1.10).
The construction proper (§§2-14, the Leta-operator, AOmega, comparisons) was not read.
