# Reading notes: Hartshorne, *Algebraic Geometry* (GTM 52, Springer 1977) -- Ch V.1 + I.7 deep note

> Intersection/Hodge reference textbook. Folder
> [`references/06_intersection_hodge/`](../../../references/06_intersection_hodge/).
> This is a 514-page graduate textbook, NOT a paper, but the relevant material for Direction 8
> is concentrated and was read closely: **Chapter V.1 (Geometry on a Surface)** is the
> classical intersection-theory-on-a-surface plus the Hodge index theorem that the in-house 2G
> $C\times C$ template instantiates and that Direction 8 must lift to
> $\mathrm{Spec}(\mathbb{Z})^2$, and **Chapter I.7 (Intersections in Projective Space)** is the
> Bezout / intersection-multiplicity prerequisite layer. Crucially, V.1 Exercise 1.10 spells
> out WEIL'S PROOF of the function-field RH via the Hodge index theorem, which is exactly the
> 2G result. Pages refer to the PDF; note the PDF page number is offset from the printed book
> page by about 7 (e.g. printed p.357 is PDF p.371). Read DEEPLY: printed pp.357-368 (V.1
> Theorem 1.1 through the Nakai-Moishezon criterion, including the Hodge index theorem 1.9 and
> the Weil-RH exercise 1.10) and printed pp.47-54 (I.7 dimension theorems, degree via Hilbert
> polynomial, generalized Bezout).

## One-line takeaway

Hartshorne V.1 gives the exact classical theory Direction 8 is lifting: on a nonsingular
projective surface there is a UNIQUE symmetric intersection pairing $\mathrm{Div}\,X\times
\mathrm{Div}\,X\to\mathbb{Z}$ (Theorem 1.1), and the Hodge Index Theorem (Theorem 1.9) says this
form has signature $(1,\rho-1)$ on $\mathrm{Num}\,X\otimes\mathbb{R}$ (one $+1$, the rest $-1$).
Exercise 1.10 then derives the function-field RH from this signature by computing the
self-intersections of the diagonal and a Frobenius graph on $C\times C$ and applying the
index inequality. That is precisely the 2G template. Direction 8 = lift Chapter V.1 (the
symmetric pairing + the signature) to the arithmetic surface $\mathrm{Spec}(\mathbb{Z})^2$.

## Technical content (section by section)

**V.1 Theorem 1.1 (the intersection pairing; printed p.357-358).** For a nonsingular
projective surface $X$ over an algebraically closed field, there is a UNIQUE pairing
$\mathrm{Div}\,X\times\mathrm{Div}\,X\to\mathbb{Z}$, written $C.D$, such that:
1. if $C,D$ are nonsingular curves meeting transversally, $C.D=\#(C\cap D)$;
2. it is SYMMETRIC: $C.D=D.C$;
3. it is ADDITIVE: $(C_1+C_2).D=C_1.D+C_2.D$;
4. it depends only on linear equivalence classes: $C_1\sim C_2\Rightarrow C_1.D=C_2.D$.
Existence/uniqueness proof (pp.358-359): use Bertini (Lemma 1.2) to move any divisor into a
difference of nonsingular curves meeting transversally; reduce the count to
$\deg(\mathscr{L}(D)\otimes\mathcal{O}_C)$ (Lemma 1.3); check independence of the moving. So the
pairing exists on the cone of very ample divisors and extends by linearity. This is the
foundational object: a symmetric, linear-equivalence-invariant, $\mathbb{Z}$-valued form on
divisor classes.

**Local multiplicity (Prop 1.4, printed p.360) and self-intersection (Ex 1.4.1-1.4.4, p.360-361).**
For curves with no common component, $C.D=\sum_{P\in C\cap D}(C.D)_P$ where the local
multiplicity $(C.D)_P=\mathrm{length}\,\mathcal{O}_{P,X}/(f,g)$ (links back to I.7). The
self-intersection $D^2=D.D$ is defined via linear equivalence; $C^2=\deg_C(\mathscr{L}(C)
\otimes\mathcal{O}_C)=\deg(\text{normal bundle})$. The canonical divisor $K$ (from
$\omega_X=\wedge^2\Omega_{X/k}$) gives the adjunction formula (Prop 1.5): for a nonsingular
curve $C$ of genus $g$ on $X$, $2g-2=C.(C+K)$. Examples: $\mathbb{P}^2$ has $h^2=1$ (the
hyperbolic-free case), giving Bezout $C.D=nm$ (Ex 1.4.2); $K_{\mathbb{P}^2}=-3h$, $K^2=9$.

**Example V.1.4.3, the quadric surface $X=\mathbb{P}^1\times\mathbb{P}^1$ (printed p.361). The
baby $C\times C$.** $\mathrm{Pic}\,X=\mathbb{Z}\oplus\mathbb{Z}$ with generators $l$ of type
$(1,0)$ and $m$ of type $(0,1)$; $l^2=0$, $m^2=0$, $l.m=1$ (two lines from the same family are
skew; two from opposite families meet in one point). So a class of type $(a,b)$ and one of type
$(a',b')$ pair as $ab'+a'b$: the intersection form is the HYPERBOLIC PLANE
$\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$, signature $(1,1)$. The canonical
divisor has type $(-2,-2)$, so $K^2=8$.

**Hodge Index Theorem (Theorem 1.9, printed p.364) and its signature reading (Remark 1.9.1).**
Statement: if $H$ is ample on $X$ and $D\not\equiv0$ is a divisor with $D.H=0$, then $D^2<0$.
Proof: assume $D^2\ge0$ and derive a contradiction from the Nakai-Moishezon/Riemann-Roch
machinery (if $D^2>0$ then $D+nH$ is eventually effective, forcing $D.H>0$; if $D^2=0$ replace
$D$ by a modified $E'$ with $E'.H=0$ and $E'^2>0$). Remark 1.9.1 is the SIGNATURE
interpretation: the intersection pairing induces a nondegenerate form on
$\mathrm{Num}\,X=\mathrm{Pic}\,X/\mathrm{Pic}^\tau X$, a finitely generated free abelian group
(Neron-Severi). By Sylvester's law of inertia the form diagonalizes over $\mathbb{R}$ to
$\pm1$'s with invariant signature, and Theorem 1.9 says there is exactly ONE $+1$ (the direction
of the ample $H$), the rest $-1$: SIGNATURE $(1,\rho-1)$, where $\rho=\mathrm{rank}\,
\mathrm{Num}\,X$. So the orthogonal complement of an ample class (the "primitive" part) is
NEGATIVE DEFINITE. Example 1.9.2: on the quadric, $H$ of type $(1,1)$ and $D$ of type $(1,-1)$
give $H^2=2$, $H.D=0$, $D^2=-2$, exhibiting the $(1,1)$ signature explicitly.

**Riemann-Roch (Thm 1.6) and Nakai-Moishezon (Thm 1.10).** $l(D)-s(D)+l(K-D)=\tfrac12 D.(D-K)
+1+p_a$, with $H^2=$ the Hilbert-polynomial leading coefficient. Nakai-Moishezon: $D$ is ample
iff $D^2>0$ and $D.C>0$ for all irreducible curves $C$. (Ex 1.10.1 notes Mumford's example of a
$D$ with $D.C>0$ for all $C$ but $D^2=0$, hence not ample, a cautionary "passes the curve test
but fails the self-intersection test" remark, the surface analogue of the BH17 / D-H
discipline.)

**EXERCISE V.1.10: Weil's proof of the function-field RH (printed p.368). THIS IS THE 2G
TEMPLATE.** Let $C$ be a curve of genus $g$ over $\mathbb{F}_q$ with $N$ rational points, so
$N=1-a+q$ where $|a|\le2g\sqrt q$ is the RH bound to be proved. On $X=C\times C$, take the
Frobenius morphism $f:C\to C$ (raising to $q$th powers), its graph $\Gamma=\Gamma_f\subset X$,
and the diagonal $\Delta\subset X$. Then (the exercise asks one to show):
- $\Gamma^2=q(2-2g)$ (the graph of $q$-power Frobenius has self-intersection $q\cdot(2-2g)$,
  using $\Delta^2=2-2g$ from Ex 1.6 and the type bookkeeping),
- $\Gamma.\Delta=N$ (intersections of the Frobenius graph with the diagonal = fixed points =
  $\mathbb{F}_q$-rational points),
and applying the Hodge-index inequality (Ex 1.9, the Castelnuovo-Severi inequality
$(D^2)(H^2)\le(D.H)^2$ for the right classes) to $D=r\Gamma+s\Delta$ for all $r,s$ yields the
bound $|N-(q+1)|\le2g\sqrt q$. So the function-field RH (Hasse-Weil bound) IS the Hodge index
signature on $C\times C$ applied to $\{\Delta,\Gamma\}$. Hartshorne flags this exercise
explicitly as "Weil's proof of the analogue of the Riemann Hypothesis for curves" and points to
App. C, Ex 5.7 for the cohomological interpretation.

**I.7 Intersections in Projective Space (printed pp.47-54). The prerequisite Bezout layer.**
Dimension theorems: in $\mathbb{P}^n$, every component of $Y\cap Z$ has dimension $\ge r+s-n$
(Thm 7.2), and is nonempty if $r+s\ge n$. The DEGREE of a projective variety is defined via the
Hilbert polynomial (Hilbert-Serre Thm 7.5: $\varphi_M(l)=P_M(l)$ for $l\gg0$, $\deg P_M=\dim
Z(\mathrm{Ann}\,M)$; degree $=r!\times$ leading coefficient, Prop 7.6). The generalized Bezout
theorem (Thm 7.7): for $Y$ of dimension $\ge1$ and a hypersurface $H$ not containing $Y$,
$\sum_j i(Y,H;Z_j)\deg Z_j=(\deg Y)(\deg H)$, with intersection multiplicity $i(Y,H;Z_j)=
\mu_{\mathfrak{p}_j}(S/(I_Y+I_H))$. Corollary 7.8 is classical Bezout for plane curves:
$\sum i(Y,Z;P_j)=de$. This is the classical model for "multiplicity of intersection at a point"
that V.1's local multiplicity (Prop 1.4) and the arithmetic place-dependent contribution rely
on.

## Points mapped to the project

1. **Direction 8's classical target is V.1 Theorem 1.1 + Theorem 1.9.** When the program says
   "lift the Hodge index signature to the arithmetic surface," the precise classical statement
   being lifted is Theorem 1.1 (the UNIQUE symmetric $\mathbb{Z}$-valued pairing) plus Theorem
   1.9 + Remark 1.9.1 (the SIGNATURE $(1,\rho-1)$, primitive part negative definite). The 2G
   in-house Lean result is this theorem for $X=C\times C$. The arithmetic object $\Gamma_S$
   (2Q/2R) is meant to play a correspondence/divisor class on the arithmetic $X$ whose
   self-intersection $\Gamma_S^2=-\zeta'/\zeta$ the form must control. ->

2. **Exercise V.1.10 IS the 2G result, stated in the textbook.** $\Gamma^2=q(2-2g)$,
   $\Gamma.\Delta=N$, and the Hodge-index inequality applied to $r\Gamma+s\Delta$ gives the
   Hasse-Weil bound. This is the function-field RH = signature-of-the-$C\times C$-form template
   the entire project is lifting, and it is exactly what 2G machine-proved in Lean. The arithmetic
   lift Direction 8 wants is: replace $C\times C$ by $\mathrm{Spec}(\mathbb{Z})^2$, $\Gamma_f$ by
   the arithmetic Frobenius correspondence $\Gamma_S$, $\Delta$ by the arithmetic diagonal, and
   $N$ (point count) by the $\zeta$-data, then run the same Hodge-index argument. This exercise
   is the single most load-bearing pointer in Hartshorne for the project: it is the source
   form of the move. ->

3. **Example V.1.4.3 ($\mathbb{P}^1\times\mathbb{P}^1$, hyperbolic form) is the simplest product
   surface and the first link in the generalization chain.** $\mathbb{P}^1\times\mathbb{P}^1$
   hyperbolic $(1,1)$ form $\to$ $C\times C$ form with diagonal and Frobenius graph (Ex 1.10)
   $\to$ (Direction 8) $\mathrm{Spec}(\mathbb{Z})^2$ form with $\Gamma_S$. The off-diagonal
   $l.m=1$ structure is the pairing that, on $C\times C$, becomes the function-field RH; the
   $(1,p)$ bidegree of $\Gamma_S$ (2Q) is the arithmetic echo of the $(a,b)$ bidegree bookkeeping
   in this example. Example 1.9.2 shows the signature on the quadric explicitly. ->

4. **The Mumford example (Ex 1.10.1) is the surface-level D-H discipline.** A divisor with
   $D.C>0$ for all irreducible curves $C$ but $D^2=0$, hence not ample, "passes the curve test
   but fails the self-intersection test." This is the classical-surface mirror of the AHK BH17
   counterexample and the project's wrong-approach detector: the SELF-INTERSECTION / signature
   datum is the real content, not the easier curve-positivity test. Reinforces that Direction 8
   must produce the definite signature, not just a weaker positivity. ->

5. **I.7 supplies the local-multiplicity / Bezout substrate (Thm 7.7, Cor 7.8, Prop 1.4).**
   Direction 8 needs the arithmetic analogue of local intersection multiplicity at each prime
   (the place-dependent contribution to $\Gamma_S.\Delta$). I.7 is the classical model for
   "multiplicity of intersection at a point" and the degree-via-Hilbert-polynomial formalism,
   the layer beneath the V.1 global pairing. Background, but the arithmetic intersection theory
   (Arakelov-style, summing finite-place lengths plus an archimedean Green's-function term) is
   the lift of exactly this local-to-global structure. ->

## What this changes for the program

- **The classical statement Direction 8 lifts is now pinned to specific theorems and one
  exercise.** Not "some Hodge index theorem" but Theorem 1.1 (unique symmetric pairing) +
  Theorem 1.9 / Remark 1.9.1 (signature $(1,\rho-1)$, primitive part negative definite) +
  Exercise 1.10 (Weil's RH proof = the signature applied to $\Delta,\Gamma_f$ on $C\times C$).
  The 2G machine-proof corresponds to Exercise 1.10. This is the precise classical anchor for
  the live front.
- **The generalization chain is explicit and its links are named.** $\mathbb{P}^1\times
  \mathbb{P}^1$ (Ex 1.4.3) $\to C\times C$ (Ex 1.10) $\to\mathrm{Spec}(\mathbb{Z})^2+\Gamma_S$
  (Direction 8). Each step keeps the symmetric hyperbolic-ish form and reads an arithmetic
  bound off its signature.
- **The D-H discipline has a classical-surface witness too.** Mumford's Ex 1.10.1 is the same
  "passes the easy test, fails the signature test" pattern as AHK's BH17. Pair the three: D-H
  (the arithmetic counterexample), BH17 (the tropical one), Mumford (the classical-surface one).
  All say: the signature / self-intersection, not the weaker positivity, is the content.
- **Reading priority for any Direction-8 worker:** V.1 Theorems 1.1, 1.9 + Remark 1.9.1
  (pairing + signature), then Exercise 1.10 (Weil's RH proof, the 2G template), then Ex 1.6
  (diagonal self-intersection $2-2g$) and Ex 1.9 (the Castelnuovo-Severi inequality used in
  1.10), then I.7 (local multiplicity / Bezout). Appendix C (the function-field Weil conjectures,
  cohomological form) is the bridge to the project's whole framing; Appendix A (general Chow
  ring) is for higher-codimension cycles.

## Status

Read DEEPLY printed pp.357-368 (V.1: Theorem 1.1 the unique symmetric pairing with all four
properties and its existence/uniqueness proof, Lemmas 1.2-1.3, Prop 1.4 local multiplicity,
self-intersection and canonical divisor Examples 1.4.1-1.4.4, the quadric Example 1.4.3
hyperbolic form, adjunction Prop 1.5, Riemann-Roch Thm 1.6, Lemma 1.7, the HODGE INDEX THEOREM
1.9 with proof and the signature interpretation Remark 1.9.1, Example 1.9.2, Nakai-Moishezon
Thm 1.10 with Mumford caution Ex 1.10.1, and the EXERCISES including Ex 1.6 diagonal
self-intersection, Ex 1.9 Castelnuovo-Severi inequality, and Ex 1.10 Weil's proof of the
function-field RH); and printed pp.47-54 (I.7: dimension theorems 7.1-7.2, Hilbert-Serre 7.5,
degree Prop 7.6, generalized Bezout Thm 7.7, classical Bezout Cor 7.8). Appendices A
(Intersection Theory / general Chow ring) and C (the Weil conjectures, cohomological RH) located
via the TOC and chapter intros, not read line by line. This is a textbook; the load-bearing
pointer is Direction 8 = lift of V.1 (symmetric pairing Theorem 1.1 + Hodge index signature
Theorem 1.9), with Exercise 1.10 as the explicit 2G $C\times C$ template and Appendix C as the
function-field RH being lifted.
