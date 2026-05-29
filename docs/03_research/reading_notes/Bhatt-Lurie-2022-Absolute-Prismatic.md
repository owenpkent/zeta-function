# Reading notes: Bhatt & Lurie, *Absolute prismatic cohomology* (arXiv:2201.06120, 2022)

> Folder `references/01_prismatic_cohomology/`. This is the **absolute** (all-primes,
> over Spec(Z_p)) prismatic theory, and it is the most directly on-target prismatic
> source for the program. Where Bhatt-Scholze fixes a prime, this paper recasts the
> whole prismatic site of Spec(Z_p) as quasicoherent sheaves on a single stack (the
> **Cartier-Witt stack** WCart) carrying a Frobenius endomorphism and a **Sen
> operator** Theta. The Sen operator is a genuine infinitesimal flow generator acting
> diagonally on graded pieces by multiplication by -n. That is exactly the
> flow-on-the-substrate object Direction 4 and Deninger's R-flow have been asking
> prismatic cohomology to provide. Read after Bhatt-Scholze (per-prime) and before
> the two BMS precursors.
> Pages read: pp.1-10 (TOC, §1.1-1.6: Goal, history, the Cartier-Witt stack and
> prismatic crystals, diffracted Hodge cohomology + Hodge-Tate divisor + Sen
> operator, Nygaard filtration, syntomic cohomology).

## One-line takeaway

The absolute prismatic site Spf(Z_p)_prism is "the category of all bounded prisms,"
and it is geometrized by the **Cartier-Witt stack** WCart: perfect complexes on
WCart = perfect prismatic crystals on Spf(Z_p). On WCart there is a **Frobenius
endomorphism F** (lifting Frobenius on O/p) and, on the Hodge-Tate divisor
WCart^HT inside it, a **Sen operator** Theta whose eigenvalues control everything:
Theta acts on the n-th graded piece of the diffracted Hodge complex by -n, and its
eigenvalues being distinct mod p is what forces degeneration (a clean spectral
statement). WCart has cohomological dimension 1: the heuristic is that the absolute
prismatic cohomology of X is its de Rham cohomology **relative to "the field with
one element,"** over which X has relative dimension n+1.

## The points that matter, mapped to the project

1. **This is the absolute, all-primes theory, and it has a base-point story (§1.3).**
   Spf(Z_p)_prism is the category of all bounded prisms; its geometrization is WCart,
   and prismatic crystals on Spf(Z_p) become quasicoherent sheaves on WCart. The
   prismatic cohomology sheaf H_prism(X) is one such crystal (Example 1.3.1).
   -> This is the prismatic answer to **2K's missing absolute base point /
   Spec(F_1)**. Bhatt-Lurie state the heuristic in §1.4 / Remark 1.4.1 explicitly:
   absolute prismatic cohomology of X behaves like de Rham cohomology of X **relative
   to "the field with one element."** That is the program's F_1 base, realized as a
   stack (WCart) rather than a ring. The product surface Spec(Z) x_{F_1} Spec(Z)
   would be the self-fiber-product over this base; WCart is a concrete candidate for
   the "x Spec(F_1)" the program needs.

2. **The Cartier-Witt stack carries a Frobenius endomorphism F (Remark 1.3.4, §3.6).**
   O on Spf(Z_p)_prism comes with an endomorphism lifting Frobenius on O/p; this is a
   map F : WCart -> WCart lifting the Frobenius of WCart x Spec(F_p). Geometric
   prismatic crystals are naturally **prismatic F-crystals**: E with F*E -> E.
   -> This is the global Frobenius the program wants for **Gamma_S**, now living on
   the absolute stack rather than per-prime. The per-prime phi_A of Bhatt-Scholze are
   the local pieces; F on WCart is their assembly over all p. 2Q said Gamma_S must be
   place-dependent (one scale per prime); F on WCart is a single global endomorphism
   of the stack that nonetheless restricts to each prime's Frobenius, which is exactly
   the shape "one map, place-dependent action" 2Q was groping for.

3. **The Sen operator Theta is the flow generator, acting by -n on graded pieces
   (§1.4, Thm 3.5.8 region, Notation 4.7.2).** The Hodge-Tate divisor WCart^HT is the
   completed classifying stack of G_m^sharp; quasicoherent complexes on it are pairs
   (M, Theta) with M a complex and Theta an endomorphism (the **Sen operator**). On
   the diffracted Hodge complex, Theta is compatible with the conjugate filtration and
   acts on gr_n by multiplication by **-n**; the conjugate filtration splits
   rationally into eigenspaces of Theta. When the eigenvalues are distinct mod p, the
   Hodge-to-de-Rham spectral sequence degenerates (their Deligne-Illusie via Sen,
   Remark 1.4.2).
   -> This is the single most program-relevant object in the prismatic literature.
   Deninger's program (note: Deninger I §1) defines a generator Theta whose
   regularized determinant is zeta and whose eigenvalues are the zeta zeros; the
   Riemann-Hilbert relation Sp(Theta) = e^{-1} Sp(F) ties additive eigenvalues of the
   generator to multiplicative eigenvalues of Frobenius. Bhatt-Lurie's Sen operator is
   a real, defined operator on the cohomology that (a) is a Frobenius-companion (it
   lives on the Hodge-Tate divisor next to F on WCart) and (b) has explicit integer
   eigenvalues -n governing the grading. It is the prismatic incarnation of the
   "infinitesimal generator of the flow" Direction 4.6 and Leichtnam 2006's scaling
   flow both want. The program should treat Theta as the candidate for Deninger's R.

4. **WCart has cohomological dimension 1 (Remark 1.4.1).** Absolute prismatic
   cohomology of a smooth affine X of relative dimension n vanishes above n+1; the
   reading is "de Rham cohomology relative to F_1, which adds one dimension."
   -> Two things for the program. First, **dimension +1** is the arithmetic-surface
   intuition: Spec(Z) is an arithmetic curve, and the F_1 base adds the second
   dimension to make a surface, which is the dimension count Direction 8's
   intersection form lives on. Second, cohomological dimension 1 is a finiteness-flavor
   statement; but note it is bounded relative dimension, not finite-dimensional total
   cohomology. 2Q forces dim H^i = infinity over Spec(Z); the Sen-operator /
   conjugate-filtration picture is graded with infinitely many pieces (Theta has
   eigenvalues -n for all n >= 0), consistent with the infinite-dimensionality 2Q
   predicts. So the substrate is naturally infinite-dimensional in the right way.

5. **Nygaard filtration + Frobenius morphism + syntomic cohomology give the trace /
   fixed-point machinery (§1.5-1.6).** RGamma_prism(X) carries a Frobenius morphism
   phi and an absolute Nygaard filtration; the n-th syntomic complex is the **fiber of
   (phi{n} - iota)** on Fil^n. Syntomic cohomology is built as a Frobenius-fixed-point
   (phi=1) construction, with comparison to etale cohomology of the generic fiber.
   -> The shape "fiber of (phi - 1)" is the algebraic skeleton of a **Lefschetz /
   regularized-determinant** statement (Direction 4.6's det(s - Phi)). 2R realized
   Gamma_S^2 as the log-derivative of a dynamical zeta, -zeta'/zeta = sum Lambda(n)
   n^{-s}; the syntomic (phi-1)-fiber is the cohomological home for such a
   trace-of-Frobenius. The Nygaard filtration is the grading the det would be taken
   over.

## What this changes for the program

- **This, not Bhatt-Scholze, is the prismatic object Direction 3 should point at for
  the live front.** It is absolute (all primes / Spec(Z_p)), it has an F_1-relative
  base-point heuristic (addresses 2K), it carries a global Frobenius F on WCart
  (candidate Gamma_S assembly), and it carries the Sen operator Theta (candidate
  Deninger R / flow generator). Bhatt-Scholze is the per-prime input; this is where
  the gluing lives.
- **The Sen operator is the concrete handle for the flow.** Theta acts by -n on
  graded pieces and is the companion of the Frobenius on the Hodge-Tate divisor. This
  is the closest existing operator to Deninger's eigenvalue-generator. Pulling the
  thread "is Sp(Theta) relatable to zeta zeros, in the Spec(Z) (not Z_p) limit" is the
  natural next research question; the per-prime Z_p version is integer-spectrum (-n),
  so the arithmetic content must come from how these glue across primes and across the
  archimedean place (2I), not from a single prime.
- **Still no signature.** WCart's cohomological dimension 1 and the conjugate
  filtration give a graded structure and a +1-dimension count that match Direction 8's
  surface intuition, but the paper proves comparison and degeneration results, not an
  intersection-form index theorem. The (+,-) signature split Direction 8 needs is not
  constructed here. What this paper gives Direction 8 is the **graded substrate (the
  Nygaard / conjugate filtration) on which a cup-product and a Hodge-star could be
  defined**, plus the dimension count. The Hodge-index step remains open.
- **Caveat on scope.** This is Spec(Z_p) and unramified W(k); the archimedean place
  (2I, the program's hardest place) is outside it. The product surface needs Spec(Z)
  with infinity, so WCart is the finite-places half of the F_1 base, not the whole of
  it. The archimedean factor (Deninger's Gamma-factor as a regularized determinant,
  per the Deninger I note) is a separate gluing problem.

## Status

Read pp.1-10 of the PDF in `references/01_prismatic_cohomology/`: TOC and the full
introduction §1.1-1.6 (Goal; recent history with A_inf-cohomology Thm 1.2.1;
Cartier-Witt stack WCart and prismatic crystals §1.3 including Remark 1.3.4 on the
Frobenius F and Remark 1.3.5 on Drinfeld's independent discovery; diffracted Hodge
cohomology, the Hodge-Tate divisor, and the **Sen operator** §1.4 with Remarks
1.4.1-1.4.3; the Nygaard filtration §1.5; syntomic cohomology §1.6). The technical
bodies (§§2-9, appendices) were not read.
