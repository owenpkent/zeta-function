# Reading notes: Bhatt & Lurie, *Absolute prismatic cohomology* (arXiv:2201.06120, 2022)

> Folder `references/01_prismatic_cohomology/`. This is the **absolute** (all-primes,
> over Spec(Z_p)) prismatic theory, and it is the most directly on-target prismatic
> source for the program. Where Bhatt-Scholze fixes a prime and a base prism, this
> paper recasts the *whole* absolute prismatic site of Spec(Z_p) (the category of all
> bounded prisms) as quasicoherent sheaves on a single algebro-geometric object, the
> **Cartier-Witt stack** WCart, which carries a global **Frobenius endomorphism F**
> and, on its **Hodge-Tate divisor** WCart^HT, a **Sen operator** Theta. Theta is a
> genuine infinitesimal flow generator: it acts on the n-th graded piece of the
> diffracted Hodge complex by multiplication by -n, and its exponential
> exp(log(u) Theta) recovers the action of the cyclotomic group (1 + pZ_p)^x. That is
> precisely the flow-on-the-substrate object Direction 4.6 and Deninger's R-flow have
> been asking prismatic cohomology to provide. Read after Bhatt-Scholze (per-prime)
> and before the two BMS precursors.

## One-line takeaway

The absolute prismatic site Spf(Z_p)_prism is "the category of all bounded prisms,"
and it is geometrized by the **Cartier-Witt stack** WCart = [WCart_0 / W^x]:
quasicoherent (perfect) complexes on WCart = perfect prismatic crystals on Spf(Z_p).
On WCart there is a **Frobenius endomorphism F** (a lift of Frobenius, Construction
3.6.1) that **contracts** the Hodge-Tate divisor WCart^HT to the de Rham point, and
on WCart^HT a **Sen operator** Theta whose eigenvalues control everything: QCoh(WCart^HT)
= pairs (M, Theta) (Theorem 3.5.8), Theta acts on the n-th conjugate-graded piece of
the diffracted Hodge complex by -n, exp(log(u) Theta) = the cyclotomic action gamma_u,
and the classical Sen operator of p-adic Hodge theory is recovered exactly (Theorem
3.9.5: g acts by exp(log(chi(g)) Theta)). WCart has cohomological dimension 1; the
heuristic is that absolute prismatic cohomology of X is its de Rham cohomology
**relative to "the field with one element,"** over which X has relative dimension n+1.

## Technical content (section by section)

### §1.1-1.2 Goal and the move from relative to absolute

The motivating question (Question 1.1.1): for a smooth proper X_K over K of char 0,
de Rham cohomology RGamma_dR(X/O_K) and p-adic etale cohomology RGamma_et(X_Kbar, Z_p)
are two refinements of the same complex-geometric singular cohomology; is there one
finer invariant recovering both, with new structure on each? Over algebraically closed
C, [BMS1] answered this with A_inf-cohomology (their Theorem 1.2.1, reproduced):
RGamma_dR(X/O_K) = O_K (tensor_A_inf) RGamma_A_inf(X), and
RGamma_et(X_K, Z_p) = (RGamma_A_inf(X)[1/xi]^)^{phi=1}, with xi a generator of
ker(theta : A_inf -> O_C). The relative prismatic cohomology of [Bhatt-Scholze]
generalizes RGamma_A_inf to non-perfect base prisms. **This paper studies the
absolute case**: it lets the prism (A, I) vary over *all* bounded prisms at once.

Prism (torsion-free case, Def 1.2.2): a pair (A, I), A a torsion-free commutative
ring with a Frobenius lift phi_A (phi_A(x) = x^p mod p), I an invertible ideal, A both
p- and I-adically complete, and the set { (phi_A(x) - x^p)/p }_{x in I} generating the
unit ideal. Perfect if phi_A is an isomorphism; bounded if A/I has bounded p-torsion.
Key examples: the perfect prism (A_inf = W(O_C^flat), ker theta) (Ex 1.2.4), the
crystalline prism (W(k), (p)) giving crystalline cohomology (Ex 1.2.5), and the q-de
Rham prism (Z_p[[q-1]], ([p]_q)) with A/I = Z_p[zeta_p] giving q-de Rham cohomology
(Ex 1.2.6).

### §1.3 The Cartier-Witt stack WCart

The construction (A, I) -> RGamma_prism(X_Abar / A) is a **prismatic crystal on
Spf(Z_p)**: a rule assigning each bounded prism a perfect complex of A-modules and
each map of prisms a base-change quasi-isomorphism. The goal is to realize such
crystals as quasicoherent sheaves on one stack. WCart is that stack. The slogan
(Equation 1 of §1.3): { Perfect complexes on WCart } = { Perfect prismatic crystals
on Spf(Z_p) }. The prismatic cohomology of X is one such crystal, the **prismatic
cohomology sheaf** H_prism(X) (Example 1.3.1). The Breuil-Kisin twist
A{-1} = H^2_prism(P^1) is invertible; its inverse A{1} gives the line bundle
O_WCart{1} on WCart (Example 1.3.2). For a bounded p-adic formal scheme X one gets
the absolute prismatic complex RGamma_prism(X) and twists RGamma_prism(X){n}; the
quasisyntomic site recovers it (Theorem 4.4.30), there is a comparison to relative
prismatic cohomology (iso for perfect prisms), and a comparison to crystalline
cohomology for F_p-schemes (iso for quasisyntomic X, Theorem 4.6.1).

WCart **definition via Cartier-Witt divisors** (Def 3.1.4): a Cartier-Witt divisor of
a ring R (p nilpotent) is a generalized Cartier divisor (I, alpha), alpha : I -> W(R)
on Spec(W(R)), such that (a) the image of I -> W(R) ->> R is a nilpotent ideal, and
(b) the image of I -> W(R) --delta--> W(R) generates the unit ideal. WCart(R) is the
groupoid of these. Remark 3.1.5 ties this to prisms: (W(R), I) is a prism iff (I, iota)
is a Cartier-Witt divisor (iota the inclusion), so WCart "enlarges the set of prism
structures on W(R)." Heuristically WCart plays the role of Spf(A_init) for a
nonexistent initial prism (A_init, I_init); the category of prisms has no initial
object, so this is only heuristic, but every prism (A, I) determines a map
rho_A : Spf(A) -> WCart (Construction 3.2.4).

**Explicit presentation (Construction 3.2.1, Prop 3.2.3):** WCart_0(R) = Witt vectors
sum V^n[a_n] with a_0 nilpotent and a_1 a unit; this is an affine formal scheme
Spf(A^0), A^0 = completion of Z[a_0, a_1^{+-1}, a_2, ...] at (p, a_0). The group
W^x acts, and WCart = [WCart_0 / W^x] (quotient by the unit Witt vectors). So WCart is
a quotient stack: not a scheme, but close to algebraic.

**The de Rham point** (Example 3.2.6): applying rho_A to the crystalline prism
(Z_p, (p)) gives rho_dR : Spf(Z_p) -> WCart, whose pullback realizes the comparison
between absolute prismatic cohomology and de Rham cohomology.

### §1.3 / §3.6 The Frobenius endomorphism F of WCart

The structure sheaf O on the prismatic site carries an endomorphism lifting Frobenius
on O/p; geometrically this is a map **F : WCart -> WCart** (Construction 3.6.1),
induced by the Witt vector Frobenius W(R) -> W(R) carrying Cartier-Witt divisors to
Cartier-Witt divisors. For an F_p-algebra R, F restricts to the usual Frobenius of
WCart x Spec(F_p) (Remark 3.6.2). Geometric prismatic crystals are naturally
**prismatic F-crystals**: E with F*E -> E (Remark 1.3.4), the prismatic incarnation of
crystalline Galois representations.

**Crucial fact (Prop 3.6.6): F contracts the Hodge-Tate divisor.** F does *not*
preserve WCart^HT; instead the square
  WCart^HT -> WCart, WCart^HT -> Spf(Z_p) --rho_dR--> WCart, F : WCart -> WCart
commutes (F collapses WCart^HT to the de Rham point). Theorem 3.6.7 shows this is
*essentially the only* way F fails to be an isomorphism: for any QCoh complex E on
WCart, the induced square of RGamma's is a pullback. Heuristically (their phrase) this
"quantifies the extent to which the non-existent initial prism (A_init, I_init) fails
to be perfect." The fiber-sequence form (p.57):
  RGamma(WCart, E) -> RGamma(WCart, F*E) -> rho_dR* E [-1].

### §1.4 / §3.4-3.5 The Hodge-Tate divisor and the diffracted Hodge complex

WCart^HT (Def 3.4.1) is the closed substack of Cartier-Witt divisors (I, alpha) with
the composite I -> W(R) ->> R equal to zero. It is the central fiber of
mu : WCart -> [A-hat^1 / G_m] over [{0}/G_m] = BG_m, so mu^HT : WCart^HT -> BG_m. The
content of §3.4 (Theorem 3.4.13) is that **WCart^HT is the (p-completed) classifying
stack of G_m^sharp**, the divided-power thickening of G_m along its identity:
G_m^sharp = Spec(O_{G_m}^sharp) where O_{G_m}^sharp is the divided-power envelope of
the ideal (t-1) in Z[t^{+-1}]. The proof goes through the structure of the group
scheme W^x[F] (kernel of Frobenius on units), which is faithfully flat over Z
(Cor 3.4.8) and after inverting p splits as a product of G_m's via ghost components
(Remark 3.4.6).

**Classification (Theorem 3.5.8):** D(WCart^HT) = pairs (M, Theta), where M is a
p-complete complex of abelian groups and Theta : M -> M is an endomorphism (the
**Sen operator**), with essential image cut out by: M is p-complete and Theta^p - Theta
acts locally nilpotently on H^*(F_p tensor M). The intuition (§3.5): a representation
of G_m is a grading M = direct-sum_n M(n), and the **weight endomorphism**
Theta(x) = nx for x in M(n) recovers the grading; G_m^sharp-reps are the same data
rationally, but Theta is the canonical integral handle on the grading. So Theta is
literally the generator of the grading by Breuil-Kisin/Hodge-Tate weight.

**Construction 3.5.4 (the Sen operator):** over the dual numbers Z[eps]/(eps^2), the
unit 1 + [eps] in W(R) acts on any Cartier-Witt divisor on WCart^HT; this gives an
automorphism gamma = id + eps Theta_E of pi*E, defining Theta_E. The Sen operator
obeys a **Leibniz rule** Theta_{E tensor E'} = Theta_E tensor id + id tensor Theta_E'
(Remark 3.5.5), so it is a derivation of the tensor structure; Theta vanishes on the
unit O_WCart^HT (Remark 3.5.5), and **on O_WCart^HT{n} it is multiplication by n**
(Example 3.5.6).

**Diffracted Hodge complex (Notation 4.7.12, §1.4):** the restriction
H_prism(X)|_WCart^HT is a pair (Omega^{diff}_X, Theta), where the diffracted Hodge
complex Omega^{diff}_X carries an exhaustive increasing **conjugate filtration**
Fil_0 -> Fil_1 -> ... For X smooth over W(k), gr^conj_n Omega^{diff} = Omega^n[-n]
(Hodge cohomology), and the Sen operator acts on gr^conj_n by **multiplication by -n**.
Consequently the conjugate filtration splits rationally into eigenspaces of Theta.

### §1.4 The Sen operator and degeneration (Deligne-Illusie via Sen, Remark 1.4.2)

For X_0 smooth over k of dim < p, the eigenvalues -n of Theta on gr^conj are distinct
mod p, so the conjugate filtration is canonically split (into generalized eigenspaces),
which immediately gives degeneration of the Hodge-to-de-Rham spectral sequence
H^s(X_0, Omega^t) => H^{s+t}_dR(X_0/k). This recovers Deligne-Illusie cleanly: the
arithmetic of the integer eigenvalues -n controls degeneration. **Cohomological
dimension 1** (Remark 1.4.1): for X smooth affine of relative dim n over Spf(Z_p),
H^*_prism vanishes for * > n+1; the reading is "de Rham cohomology relative to F_1,
which has relative dimension n+1."

### §3.7 Exponentiating the Sen operator: the flow

This is the operationally most important section for the program. For E on WCart^HT,
its fiber E_eta carries an action of Aut(eta)(Z_p) = G_m^sharp(Z_p) = (1 + pZ_p)^x;
each u in (1 + pZ_p)^x gives an automorphism gamma_u of E_eta, and
**gamma_u = exp(log(u) Theta_E)** (Proposition 3.7.1):
  gamma_u = sum_{m>=0} (log(u)^m / m!) Theta_E^m  (mod p^d for all d),
the divided powers log(u)^m / m! converging p-adically to 0. So the Sen operator Theta
is literally the infinitesimal generator of the cyclotomic-units action; gamma_u = u^Theta.
Proposition 3.7.3 (p odd): for a topological generator u of (1 + pZ_p)^x there is a
fiber sequence RGamma(WCart^HT, E) -> E_eta --xi_u--> E_eta with p xi_u = gamma_u - id;
the difference gamma_u - id is canonically divisible by p, and the cohomology of
WCart^HT is the fiber of (gamma_u - id)/p. The formal series for that operator is
  (u^Theta - 1)/(p Theta) = sum_{n>=1} (log(u)^n / (p n!)) Theta^{n-1}  (Remark 3.7.5).

### §3.9 Sen theory: the classical Sen operator recovered

This is the bridge to p-adic Hodge theory. Sen's theorem (Theorem 3.9.1): a
finite-dim C-vector space V with continuous semilinear Gal(K)-action has a unique
K_infty-subspace V_infty with an endomorphism Theta : V_infty -> V_infty such that
for x in V_infty and g in an open subgroup, **g(x) = exp(log(chi(g)) Theta)(x)**,
where chi : Gal -> Z_p^x is the cyclotomic character. Bhatt-Lurie's main Sen result
(Theorem 3.9.5): for a perfect complex E on WCart^HT_{W(k)} = Spf(W(k)) x WCart^HT,
there is a canonical iso of graded C-vector spaces C (tensor_W(k)) H^*(E_eta) = V^*(E)
intertwining the action of g in Gal(Kbar/K) with exp(log(chi(g)) Theta_E). So the
abstract Sen operator on WCart^HT **is** the classical Sen operator, and the action of
the Galois group is the exponential of the cyclotomic character against Theta. For
F-crystals over WCart_{W(k)} one even gets V^*(E)|_HT = C (tensor) V_0^*(E) with V_0^*
a crystalline Galois rep (Remark 3.9.4).

### §1.5 / §5 The Nygaard filtration and the Frobenius morphism

RGamma_prism(X){n} carries the **absolute Nygaard filtration** Fil^*_N (a decreasing
filtration, only partially defined Frobenius), with a Frobenius operator
phi{n} : Fil^n_N RGamma{n} -> RGamma{n}. For a perfect prism the absolute Nygaard
filtration matches the relative one of [Bhatt-Scholze]; for quasiregular semiperfectoid
R the absolute prismatic complex is the underlying ring of a prism (A, I) and
Fil^n_N corresponds to { x : phi_A(x) in I^n A } (Cor 5.6.3). There is a
Nygaard-complete variant RGamma_prism-hat. Remark 1.5.1 ties the Nygaard-completed
twists to K-theory: gr^n_M TP(R)^_p = RGamma_prism-hat(Spf R){n}[2n] (the BMS2 motivic
filtration). The graded fiber sequence (Remark 5.5.8):
  gr^m_N RGamma{n} -> RGamma(Fil^conj_m Omega^diff) --Theta+m--> RGamma(Fil^conj_{m-1} Omega^diff),
so the Sen operator Theta (shifted) is exactly the connecting map of the Nygaard graded
pieces.

### §1.6 / §8 Syntomic cohomology as a Frobenius-fixed-point fiber

The n-th syntomic complex is RGamma_syn(X, Z_p(n)) = **fiber of
(phi{n} - iota) : Fil^n_N RGamma{n} -> RGamma{n}**. For n=1 it relates to G_m via the
**prismatic logarithm** log_prism : T_p(Abar^x) -> A{1} (Construction 2.7.4) and the
syntomic first Chern class c_1^syn : RGamma_et(G_m)[-1] -> RGamma_syn(Z_p(1)), an iso
after p-completion (Theorem 7.5.6). Syntomic cohomology compares to etale cohomology of
the generic fiber (Theorem 8.3.1), satisfies flat descent, supports a full theory of
Chern classes and a projective bundle / blowup formula (§9).

### The summary diagram (p.14)

The paper closes the introduction with one master diagram tying together
RGamma_syn(Z_p(n)), the Nygaard filtration Fil^n_N RGamma{n}, the absolute prismatic
complex RGamma{n}, the Frobenius phi{n}, the Hodge filtration on the derived de Rham
complex dR-hat_R, the diffracted Hodge complex Omega^diff_R, and the absolute
cotangent complex L Omega-hat^n_R[-n] = gr^n of both the Hodge and conjugate
filtrations. This single diagram is the linear-algebra skeleton on which a flow
(via Theta) and a grading (via Nygaard) both live.

## Points mapped to the project

1. **The absolute, all-primes theory with a base-point story (§1.3).** Spf(Z_p)_prism
   is the category of all bounded prisms; WCart geometrizes it as a quotient stack
   [WCart_0/W^x], and prismatic crystals become quasicoherent sheaves on WCart. The
   prismatic cohomology sheaf H_prism(X) is one such crystal (Example 1.3.1). The
   F_1 heuristic is stated explicitly (Remark 1.4.1): absolute prismatic cohomology
   of X behaves like de Rham cohomology of X **relative to "the field with one
   element,"** over which X has relative dimension n+1.
   -> This is the prismatic answer to **2K's missing absolute base point / Spec(F_1)**.
   WCart is a concrete candidate for the "x Spec(F_1)" the program needs: the F_1 base
   realized as a *stack* (a quotient by W^x of a Witt-vector formal scheme), not a
   ring. The product surface Spec(Z) x_{F_1} Spec(Z) would be the self-fiber-product
   over this base; WCart is the finite-places half of that base.

2. **The global Frobenius F on WCart, which contracts WCart^HT (Construction 3.6.1,
   Prop 3.6.6).** F : WCart -> WCart lifts Frobenius, restricts on each F_p-fiber to
   the usual Frobenius, and (the key dynamical fact) **collapses the Hodge-Tate divisor
   to the de Rham point**. Theorem 3.6.7: this contraction is the only obstruction to
   F being an isomorphism.
   -> This is the global Frobenius the program wants for **Gamma_S**, assembled over
   all p on the absolute stack. The per-prime phi_A of Bhatt-Scholze are the local
   pieces; F on WCart glues them. 2Q said Gamma_S must be place-dependent (one scale
   per prime) yet a single object; F is exactly that: one global endomorphism of the
   stack restricting to each prime's Frobenius. And **F contracting WCart^HT to a point
   is a contraction map** in the dynamical sense, which is what a Lefschetz/flow picture
   (Direction 4.6, Leichtnam's contracting transversal) requires of its Frobenius.

3. **The Sen operator Theta is the flow generator: Theta = -n on graded pieces,
   gamma_u = exp(log(u) Theta) (Theorem 3.5.8, Example 3.5.6, Prop 3.7.1, Theorem
   3.9.5).** QCoh(WCart^HT) = pairs (M, Theta); Theta is the weight endomorphism
   (Theta = mult by n on weight-n part), it is a derivation (Leibniz rule), it acts on
   the conjugate-graded diffracted Hodge complex by -n, and **its exponential is the
   cyclotomic action**: gamma_u = u^Theta for u in (1 + pZ_p)^x, and for the classical
   Galois action g = exp(log(chi(g)) Theta).
   -> This is the single most program-relevant object in the prismatic literature, and
   the connection is now exact, not heuristic. Deninger's program (Deninger I note)
   posits a generator Theta whose regularized determinant is zeta, whose eigenvalues
   are the zeta zeros, and a Riemann-Hilbert relation Sp(Theta) = log Sp(Frobenius)
   tying the additive generator to the multiplicative Frobenius. Bhatt-Lurie's Sen
   operator is a real, defined operator that (a) is the Frobenius companion (it lives
   on WCart^HT, the divisor F contracts), (b) has explicit eigenvalues -n grading the
   cohomology, and (c) **exponentiates to the cyclotomic flow** gamma_u = exp(log(u)
   Theta), which is structurally the relation Deninger needs (additive generator,
   exponentiate to get the multiplicative group action / flow). The program should
   treat Theta as the leading prismatic candidate for Deninger's R, and the relation
   gamma_u = exp(log(u) Theta) as the prismatic form of "flow = exp(t R)."

4. **Cohomological dimension 1, infinite graded substrate (Remark 1.4.1, §3.5).**
   WCart has cohomological dimension 1, the +1-dimension being the F_1 direction; but
   the conjugate/Nygaard grading is infinite (Theta has eigenvalues -n for all n>=0).
   -> Two things. First, **dimension +1** is the arithmetic-surface intuition: Spec(Z)
   is the arithmetic curve, the F_1 base adds the second dimension to make a surface,
   the dimension count Direction 8's intersection form lives on. Second, the cohomology
   is naturally infinite-dimensional in the grading direction, consistent with 2Q's
   prediction that dim H^i = infinity over Spec(Z). The substrate is infinite-dim in
   exactly the right (graded, Theta-eigenvalue) way.

5. **The Sen operator IS the connecting map of the Nygaard graded pieces; syntomic =
   (phi-1)-fiber (Remark 5.5.8, §1.6).** gr^m_N RGamma{n} sits in a fiber sequence whose
   connecting map is Theta + m, and RGamma_syn(Z_p(n)) = fiber of (phi{n} - iota) on
   Fil^n_N.
   -> The "fiber of (phi - 1)" is the algebraic skeleton of a **Lefschetz /
   regularized-determinant** statement (Direction 4.6's det(s - Phi)). 2R realized
   Gamma_S^2 as the log-derivative of a dynamical zeta, -zeta'/zeta = sum Lambda(n)
   n^{-s}; the syntomic (phi-1)-fiber is the cohomological home for such a
   trace-of-Frobenius, and the Nygaard filtration is the grading the det would be taken
   over. That the connecting map of the graded pieces is literally Theta (shifted)
   couples the grading (Direction 8) and the flow generator (Direction 4) into one
   object, which is what the program has been trying to build by hand.

## What this changes for the program

- **This, not Bhatt-Scholze, is the prismatic object Direction 3 should point at for
  the live front.** It is absolute (all primes / Spec(Z_p)), it has an F_1-relative
  base-point heuristic (addresses 2K) realized as a concrete quotient stack, it carries
  a global Frobenius F on WCart that *contracts* WCart^HT (candidate Gamma_S assembly
  with the right contraction property), and it carries the Sen operator Theta
  (candidate Deninger R / flow generator) with the exact exponential relation
  gamma_u = exp(log(u) Theta). Bhatt-Scholze is the per-prime input; this is the
  gluing, and it has the dynamics.

- **The Sen operator is now a precise, not heuristic, handle for the flow.** The
  upgrades over the first-pass note: (a) Theta is the *weight* endomorphism, so its
  spectrum on the prismatic substrate is the integers -n (the Hodge-Tate weights);
  (b) **gamma_u = exp(log(u) Theta)** makes Theta literally the infinitesimal generator
  of the cyclotomic flow; (c) Theorem 3.9.5 identifies it with the *classical* Sen
  operator, with the Galois action being exp(log(chi(g)) Theta). The natural next
  research question is whether, in the Spec(Z) (not single-Z_p) assembly, the spectrum
  of the assembled Sen/Frobenius pair can be related to the zeta zeros. The per-prime
  Z_p version is integer-spectrum (-n), so the arithmetic content must come from how
  these glue across primes (one Theta per place, the place-dependence 2Q forces) and
  across the archimedean place (2I), not from a single prime. The relation
  gamma_u = u^Theta is the local template; the global zeta would need the product over
  places of det(1 - gamma_u | H^*)-type factors.

- **F's contraction of WCart^HT is the dynamical structure the program lacked.** The
  first-pass note only flagged F as "a global Frobenius." The sharper fact (Prop 3.6.6,
  Theorem 3.6.7) is that F is a *contraction*: it collapses the Hodge-Tate divisor to
  the de Rham point, and this is the only way it fails to be invertible. Leichtnam 2006
  and Direction 4.6 both want a contracting Frobenius/flow on a transversal; F on WCart
  is a contracting endomorphism of the absolute substrate, with WCart^HT the contracted
  locus carrying the flow generator Theta. That pairing (contracting F + generator
  Theta on the contracted divisor) is the prismatic shadow of the (Frobenius flow +
  scaling generator) pair Deninger's foliated picture needs.

- **Still no signature.** WCart's cohomological dimension 1 and the conjugate/Nygaard
  filtration give a graded structure and a +1-dimension count that match Direction 8's
  surface intuition, but the paper proves comparison, degeneration, and Chern-class
  results, not an intersection-form index theorem. The (+,-) signature split Direction
  8 needs is not constructed here. What this paper gives Direction 8 is the **graded
  substrate (the Nygaard / conjugate filtration) with its connecting map = Theta, on
  which a cup-product and a Hodge-star could be defined**, plus the dimension count and
  the full Chern-class formalism (§7-9) that a Hodge-index argument would use. The
  Hodge-index step remains the open object.

- **Caveat on scope.** This is Spec(Z_p) and unramified W(k); the archimedean place
  (2I, the program's hardest place) is outside it, and Remark 1.4.3 notes that even
  ramified K is weaker (no Sen-eigenvalue distinctness, no Deligne-Illusie analog). The
  product surface needs Spec(Z) with infinity, so WCart is the finite-places half of
  the F_1 base. The archimedean factor (Deninger's Gamma-factor as a regularized
  determinant, per the Deninger I note) is a separate gluing problem, and the
  unramified-only strength of the Sen theory is a real constraint on how far the
  prismatic Theta can be pushed toward the global flow.

## Status

Read pp.1-14 (full introduction §1.1-1.8: Goal, the relative-to-absolute move with
[BMS1] Thm 1.2.1, the Cartier-Witt stack and prismatic crystals §1.3 with Remarks
1.3.4 Frobenius F and 1.3.5 Drinfeld, diffracted Hodge cohomology + Hodge-Tate divisor
+ Sen operator §1.4 with Remarks 1.4.1-1.4.3, Nygaard filtration §1.5, syntomic
cohomology §1.6, cochains/animation §1.7, the Bestiary §1.8 with the master diagram),
plus the technical bodies: §3.1-3.2 (Cartier-Witt divisors Def 3.1.4, the
[WCart_0/W^x] presentation Prop 3.2.3, prisms-to-Cartier-Witt Construction 3.2.4, the
de Rham point Ex 3.2.6) pp.37-41; §3.4-3.5 (Hodge-Tate divisor Def 3.4.1, BG_m^sharp
classification Thm 3.4.13 region, the Sen operator Construction 3.5.4, the
weight-endomorphism picture, classification Theorem 3.5.8) pp.45-50; §3.6 (Frobenius
endomorphism Construction 3.6.1, contraction of WCart^HT Prop 3.6.6, pullback square
Thm 3.6.7) pp.55-57; §3.7 (exponentiating the Sen operator: gamma_u = exp(log(u)Theta)
Prop 3.7.1, the (gamma_u - id)/p fiber Prop 3.7.3) pp.63-65; §3.9 (Sen theory:
classical Sen Theorem 3.9.1, the recovery Theorem 3.9.5 g = exp(log(chi(g))Theta),
Prop 3.9.7) pp.74-76. The remaining bodies (§4 absolute prismatic cohomology, §5
Nygaard, §6 periodic cyclic, §7-9 Chern classes/syntomic, appendices) were not read in
full.
