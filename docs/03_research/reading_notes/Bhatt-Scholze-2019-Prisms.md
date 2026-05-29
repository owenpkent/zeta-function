# Reading notes: Bhatt & Scholze, *Prisms and prismatic cohomology* (Annals 2022)

> Folder `references/01_prismatic_cohomology/`. This is the founding paper of
> prismatic cohomology, the cohomology substrate Direction 3 names and Direction 4
> wants to run a flow on. Read it for the base definitions (delta-ring, prism,
> prismatic site, structure sheaf, Frobenius), the comparison package (Theorem 1.8),
> and the Nygaard/conjugate filtration machinery (Theorems 1.13-1.15) that the
> absolute theory later turns into the Sen-operator grading. The first question the
> program must ask of any candidate substrate is: one-prime or all-primes. Answer:
> this paper is **one-prime** (it opens "Fix a prime p"). The all-primes / absolute
> theory is the companion note Bhatt-Lurie-2022. Read in the order README §01 gives:
> this first, then Bhatt-Lurie (absolute), then the two BMS papers (the precursors).

## One-line takeaway

A **prism** is a pair (A, I): a delta-ring A (a ring with a lift of Frobenius encoded
as a p-derivation delta) plus an invertible ideal I defining a Cartier divisor, with A
both p-adically and I-adically complete and a distinguished-element condition. To a
smooth p-adic formal scheme X over A/I it attaches the **prismatic site** (X/A) and a
structure sheaf O with a Frobenius-semilinear phi, and RGamma_prism(X/A) specializes to
(and refines) crystalline, Hodge-Tate, de Rham, and etale cohomology all at once
(Theorem 1.8). The Nygaard filtration and a conjugate filtration with Breuil-Kisin
graded pieces equip it with the grading the absolute theory later reads off via the Sen
operator. The whole construction is over a **fixed prime p** with a fixed base prism:
it is the single-prime building block, not the Spec(Z) object the product surface needs.

## Technical content (section by section)

### §2 delta-rings (the Frobenius, built in)

**Definition 2.1 (delta-ring):** a pair (R, delta) with delta : R -> R a map of sets,
delta(0) = delta(1) = 0, satisfying
  delta(xy) = x^p delta(y) + y^p delta(x) + p delta(x) delta(y),
  delta(x+y) = delta(x) + delta(y) + (x^p + y^p - (x+y)^p)/p.
**Remark 2.2 (delta-structures give Frobenius lifts):** phi(x) := x^p + p delta(x) is a
ring homomorphism lifting Frobenius on R/p. For p-torsion-free R, a delta-structure is
*equivalent* to a Frobenius lift phi, via delta(x) = (phi(x) - x^p)/p. The name
"p-derivation" comes from delta lowering p-adic order of vanishing by 1. By Wilkerson
/ Borger (Remark 2.3), a delta-structure on a flat Z-algebra is a p-typical
lambda-structure (one piece of a full lambda-ring, which would be a Frobenius lift at
*every* prime simultaneously). Witt vectors W_2(-) (Remark 2.4) carry the universal
delta-structure. So the Frobenius the program keeps reaching for is not an add-on: it
is the defining structure of the coefficient ring.

### §3 / §1 prisms

**Definition 1.1 (prism):** a pair (A, I), A a delta-ring, I an ideal defining a
Cartier divisor in Spec(A), such that (1) A is (p, I)-adically complete and (2)
I + phi_A(I) A contains p. When I = (d) is principal, condition (2) is delta(d) being a
unit; d is then a **distinguished element**. **Definition 1.4 (bounded):** (A, I) is
bounded if A/I has bounded p^infinity-torsion. **Proposition 1.5 (rigidity):** a map of
prisms (A, I) -> (B, J) forces J = IB; over a fixed base prism the ideal I does not
vary. Key examples (Example 1.3): crystalline prisms (A p-torsion-free p-complete with
Frobenius lift, I = (p)); perfect prisms (phi an isomorphism, equivalent to perfectoid
rings via (A, I) -> A/I and R -> (A_inf(R), ker theta), Theorem 1.11); Breuil-Kisin
prisms (A = W(k)[[u]], I = ker(A -> O_K)); and the **q-crystalline prism**
A = Z_p[[q-1]], I = ([p]_q) with [p]_q = (q^p - 1)/(q - 1) the q-analog of p,
A/I = Z_p[zeta_p].

### §4 the prismatic site

**Definition 1.6:** fix a bounded prism (A, I) and a smooth p-adic formal scheme X over
A/I. The prismatic site (X/A)_prism is the opposite of the category of prisms (B, J)
over (A, I) with a flat cover Spf(B/J) -> X over Spf(A/I). The structure sheaf O sends
(B, J) to B (an I-torsion-free delta-A-algebra), carrying a Frobenius-semilinear phi;
Obar sends (B, J) to B/J. So the site "probes X by prisms," and the cohomology is the
cohomology of this ringed site.

### §1 / Theorem 1.8 the comparison package

Set RGamma_prism(X/A) := RGamma((X/A)_prism, O), a commutative algebra in D(A) with a
phi_A-linear map phi. Theorem 1.8 proves:
(1) **Crystalline** (I = (p)): RGamma_crys(X/A) = phi_A* RGamma_prism(X/A).
(2) **Hodge-Tate** (X = Spf R affine): Omega^i_{R/(A/I)}{i} = H^i(RGamma_prism(X/A)
    tensor^L_A A/I), where M{i} = M tensor_{A/I} (I/I^2)^{tensor i} is the Breuil-Kisin
    twist. So mod I the cohomology is a *graded* object whose pieces are differential
    forms, each twisted by a power of the invertible scale ideal I.
(3) **de Rham**: RGamma_dR(X/(A/I)) = RGamma_prism(X/A) tensor^L_{A, phi_A} A/I.
(4) **Etale** (A perfect): RGamma_et(X_eta, Z/p^n) = (RGamma_prism(X/A)/p^n[1/I])^{phi=1};
    geometry recovered as a Frobenius-fixed-point (phi = 1) locus.
(5) **Base change** along maps of bounded prisms; (6) **phi an isogeny**: phi*RGamma
    -> RGamma is an isomorphism after inverting I. Example 1.9 specializes to BMS1's
    A_inf-cohomology (perfect prism A_inf, where phi_A is an iso so the pullback only
    twists the module structure) and to BMS2's Breuil-Kisin cohomology (W(k)[[u]]).
Remark 1.10: the "mysterious" Frobenius on A_inf-cohomology is explained as the
Frobenius lift on O of the prismatic site.

### §7 / §12 / §15 the conjugate and Nygaard filtrations

For S a quasiregular semiperfectoid ring (Theorem 1.13), the prismatic cohomology
collapses to a ring Prism_S (with quotient Prism_S/I), and carries two filtrations:
(1) the **conjugate filtration** Fil^conj_i on Prism_S/I, increasing, with
    gr^conj_i = (wedge^i L_{S/R}[-i])^ tensor (I/I^2)^{tensor i} (the derived exterior
    powers of the cotangent complex, twisted);
(2) the **Nygaard filtration** Fil^j_N Prism_S = { x in Prism_S : phi(x) in I^j Prism_S },
    decreasing, with the composite phi/d^j : Fil^j_N -> Prism_S/I inducing
    gr^j_N = Fil^conj_j (Prism_S/I). Comparison with topology: Prism_S-hat =
    pi_0 TP(S; Z_p) is phi-equivariantly the Nygaard completion (Theorem 1.13(3)).
For smooth X (Theorem 1.15) the Nygaard filtration exists on the quasisyntomic site,
gr^i_N RGamma_prism(X/A)^{(1)} = tau^{<=i} Obar_{R/A}{i}, and the **Frobenius is an
isogeny**: phi_A* RGamma_prism = RGamma_prism^{(1)} --phi-bar--> L eta_I RGamma_prism,
with phi-bar an isomorphism (the decalage functor L eta_I). Theorem 1.16 (perfectoid
"perfection" in mixed characteristic) and Theorem 1.17 (Z_p(n) sheaves concentrated in
degree 0; K-theory in even degrees) are the applications.

## Points mapped to the project

1. **Frobenius is built in, as a delta-structure (Def 1.1, 2.1, Remark 2.2).** A
   prism's ring A carries phi_A, a lift of Frobenius on A/p, packaged as a p-derivation
   delta. For p-torsion-free A this is *equivalent* to a Frobenius lift. So the
   Frobenius the program reaches for (Gamma_S, the geometric Frobenius correspondence)
   is the defining structure of the coefficient ring, not an add-on.
   -> This is the local-at-p Frobenius. 2Q's finding: the global Gamma_S must carry a
   **place-dependent (1, p) bidegree, one Frobenius scale per prime**, not the single
   scale q of a function field. Bhatt-Scholze supplies exactly one such scale (one
   phi_A per prism, per p). The fact (Remark 2.3) that a *full* lambda-structure is a
   compatible family of Frobenius lifts over all primes is the precise algebraic shape
   2Q wants for the global object: a delta-ring is one prime's worth of that, and the
   **absolute** theory (next note) is where the all-primes assembly lives.

2. **The prismatic site probes X by prisms; the structure sheaf carries phi; geometry
   is the phi=1 locus (Def 1.6, Thm 1.8).** Theorem 1.8 proves four comparisons as
   restrictions of one object, and the etale comparison recovers the topological
   cohomology as the Frobenius-fixed points (phi=1).
   -> This is the concrete content of "prismatic = the p-adic transversal's
   cohomology." Leichtnam 2006's transversal is locally Z_p^m and his trace-class
   property comes from contraction along it; Bhatt-Scholze is the cohomology theory
   living over that Z_p direction. The etale-comparison phi=1 locus is the structural
   reason a Frobenius/flow can sit on this substrate at all: the geometry is a
   fixed-point set of Frobenius, the same shape as a Lefschetz / trace-of-Frobenius
   statement (Direction 4.6).

3. **Hodge-Tate gives a graded structure with Breuil-Kisin twists; the conjugate and
   Nygaard filtrations refine it (Thm 1.8(2), Thm 1.13).** mod I the cohomology is
   graded by differential forms twisted by (I/I^2)^{tensor i}; the conjugate filtration
   has graded pieces the twisted derived exterior powers of L_{S/R}, and the Nygaard
   filtration { x : phi(x) in I^j } has gr^j_N = Fil^conj_j.
   -> The Breuil-Kisin twist and these two filtrations are the single-prime ancestor of
   the **graded / bidegree** structure 2Q forces and of the Hodge-type grading Direction
   8's signature needs. A signature is a (+,-) split on a graded cup-product; the
   conjugate/Nygaard filtration is where such a grading comes from. In the absolute
   theory the connecting map of the Nygaard graded pieces *is* the Sen operator Theta,
   so this filtration is also where the flow generator lives. This paper gives the
   grading per-prime; Bhatt-Lurie globalizes it and identifies its generator.

4. **Perfect prism <-> perfectoid ring, and "perfection" exists in mixed characteristic
   (Thm 1.11, 1.16, Example 1.9).** Perfect prisms (phi an iso) = perfectoid rings; every
   prism has a perfection; A_inf = W(O_C^flat) with I = ker(theta) is the perfect prism
   behind BMS1.
   -> This pins where the BMS1 A_inf-theory sits in the prismatic picture: the
   perfect-prism case. The perfect case is the rigid one with a clean (invertible)
   Frobenius; the **non-perfect** prisms (q-de Rham, Breuil-Kisin) are where the
   deformation parameter lives, and a deformation parameter is what a flow (Direction 4
   / Deninger's R-flow) needs.

5. **q-de Rham / q-crystalline: a one-parameter deformation (Example 1.3(4), 1.9(4)).**
   A = Z_p[[q-1]], I = ([p]_q), A/I = Z_p[zeta_p], gives Scholze's q-de Rham complex.
   The scale here is the q-analog [p]_q, not p.
   -> A genuine one-parameter family inside prismatic cohomology, the nearest thing in
   the per-prime theory to a continuous deformation. This is the handle Bhatt-Lurie
   turns into the Sen operator: the cyclotomic group (1 + pZ_p)^x acts on the q-de Rham
   prism via q -> q^u, and the Sen operator is the infinitesimal generator
   (gamma_u = exp(log(u) Theta)). The program's "Deninger R-flow is forced" (2Q) wants
   exactly a continuous parameter; q is the discrete shadow, and its symmetry group
   (1 + pZ_p)^x is what the Sen flow integrates.

## What this changes for the program

- **The substrate is now named precisely, and it is per-prime.** Direction 3 says
  "prismatic cohomology." Bhatt-Scholze is the definition. But it fixes a prime p and a
  base prism throughout, so by itself it is the cohomology of one place: the local input
  to a Spec(Z) object, not the object. The product-surface / absolute-base-point gap
  (2K) is not closed here; this is the brick, not the building.

- **Frobenius is structural, not bolted on, and a full lambda-structure is the
  all-primes target.** The delta-ring / phi_A is the defining datum (good for hosting
  Gamma_S), and Remark 2.3's lambda-structure = (Frobenius lifts at all primes) is the
  exact algebraic shape of the global, place-dependent Gamma_S 2Q is groping for. The
  mismatch 2Q found (one global scale vs one-per-prime) is precisely the gap between a
  single delta-structure and a full lambda-structure.

- **Etale comparison = geometry as a phi=1 locus.** This is the structural license for
  a Lefschetz/flow picture (Direction 4.6): fixed points of Frobenius recover the
  topological cohomology, the same shape as a trace-of-Frobenius statement.

- **The conjugate/Nygaard filtration is the grading the flow and the signature will
  both use.** This paper constructs that grading per-prime, with graded pieces the
  twisted derived exterior powers of the cotangent complex (conjugate) and the
  phi-shift filtration { x : phi(x) in I^j } (Nygaard). In the absolute theory its
  connecting map is the Sen operator Theta. So Direction 8's cup-product grading and
  Direction 4's det(s - Theta) grading are the same object, supplied here per-prime.

- **No signature yet.** The Hodge-Tate/conjugate/Nygaard filtrations provide a grading;
  this paper proves comparisons, an isogeny statement on Frobenius, and vanishing /
  K-theory consequences, not an index theorem. The (+,-) split Direction 8 needs is not
  here; it would have to be built on the graded structure this paper supplies and
  Bhatt-Lurie globalizes.

## Status

Read pp.1-12 of the PDF in `references/01_prismatic_cohomology/`: the TOC and the full
§1 Introduction (Def 1.1 prism, Examples 1.3, Def 1.4-1.6 bounded prism + prismatic
site + structure sheaf, Prop 1.5 rigidity, Theorem 1.8 the comparison package (1)-(6),
Examples 1.9-1.12 including q-de Rham and the perfectoid / perfect-prism equivalence
Thm 1.11, the semiperfectoid Theorem 1.13 with the conjugate and Nygaard filtrations,
Theorem 1.15 the smooth-case Nygaard filtration and Frobenius isogeny, Theorems
1.16-1.17 perfectoidization and Z_p(n) vanishing), and the start of §2 delta-rings
(Def 2.1, Remark 2.2 Frobenius lifts, Remark 2.3 lambda-structures, Remark 2.4 Witt
vectors). The bodies of the comparison and filtration proofs (§§4-18) were not read in
full.
