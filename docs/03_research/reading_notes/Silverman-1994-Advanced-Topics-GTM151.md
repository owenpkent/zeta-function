# Reading notes: Silverman, *Advanced Topics in the Arithmetic of Elliptic Curves* (GTM 151, ATAEC, 1994)

> Computational/theoretical-authority note, Chapter VI read IN DEPTH. Folder
> [`references/07_elliptic_curve_heights/`](../../../references/README.md). 540-page graduate
> textbook, NOT read cover to cover: read Chapter VI (Local Height Functions) in depth --
> §VI.1 existence/uniqueness (the Néron axioms, Theorem 1.1), §VI.2 the local decomposition
> (Theorem 2.1), §VI.3 the archimedean sigma-function formula (Theorem 3.2) and its
> q-expansion rewrite (Theorem 3.4) with the quasi-parallelogram law (Cor 3.3), §VI.4 the
> non-archimedean formula (Theorem 4.1) and the Tate-curve / multiplicative formula
> (Theorem 4.2). This note states the actual theorems and is the theory behind 2I and 2L.
> Pages refer to BOOK page numbers printed on each page.
> Read: book pp. 455-475 (Chapter VI §§1-4 in full).

## One-line takeaway

ATAEC Chapter VI is the THEORETICAL foundation of the Néron local height. §VI.1 (Theorem
1.1) proves existence and uniqueness of lambda_v from three axioms; §VI.2 (Theorem 2.1)
proves h-hat = (1/[K:Q]) sum_v n_v lambda_v, the local decomposition the project validates;
§VI.3 (Theorem 3.2) gives the closed archimedean formula
lambda(z) = -log| e^{-(1/2) z eta(z)} sigma(z) Delta^{1/12} | via the Weierstrass
sigma-function, with the q-expansion rewrite (Theorem 3.4) using the second Bernoulli
polynomial B_2; §VI.4 (Theorem 4.1, 4.2) gives the non-archimedean formula and the
Tate-curve multiplicative formula with the same B_2(v(u)/v(q)) structure. This is the
sigma-function archimedean theory 2I self-derives a series for and 2L uses for the
self-intersection.

## Technical content (section by section)

**§VI.1 Existence and uniqueness, Theorem 1.1 (book pp. 455-461).** The local Néron height
lambda: E(K) \ {O} -> R is the UNIQUE function satisfying:
- (i) lambda is continuous on E(K) \ {O} and bounded off any v-adic neighborhood of O;
- (ii) the limit lim_{P->O} (lambda(P) + (1/2) v(x(P))) exists;
- (iii) for all P with 2P != O,
  lambda([2]P) = 4 lambda(P) + v((2y + a1 x + a3)(P)) - (1/4) v(Delta).
It is independent of the Weierstrass equation (part b) and compatible with finite
extensions (part c). The uniqueness proof: any difference Lambda = lambda - lambda' of two
solutions satisfies Lambda([2]P) = 4 Lambda(P), so Lambda(P) = 4^-N Lambda([2^N]P) -> 0 by
boundedness. The existence proof builds lambda from the "naive" guess
lambda_1(P) = (1/2) max(v(x(P)^-1), 0), shows (via Resultant(phi, psi) = Delta^2, Lemma
1.2) that the error f(P) = lambda_1([2]P) - 4 lambda_1(P) - v(psi) + (1/4)v(Delta) is
bounded, and corrects it by Tate's telescoping (Prop 1.3): any bounded f has a unique
bounded mu with f = 4 mu - mu o [2], namely mu(P) = sum 4^-(n+1) f([2^n]P).

**§VI.2 Local decomposition of the canonical height, Theorem 2.1 (book pp. 461-462).**
h-hat(P) = (1/[K:Q]) sum_{v in M_K} n_v lambda_v(P) for all P, with n_v = [K_v : Q_v] the
local degree. Proof: Lemma 2.2 says lambda_v = (1/2) max(v(x^-1), 0) for almost all v, so
the sum is finite; the global function L(P) = (1/[K:Q]) sum n_v lambda_v satisfies
L([2]P) = 4 L(P) (by the product formula killing the v(2y+a1x+a3) and v(Delta) terms) and
L(P) = (1/2) h(x(P)) + O(1), hence L = h-hat by the standard quadratic-form argument.

**§VI.3 Archimedean explicit formula, Theorem 3.2 (book pp. 463-468).** Over C, with the
period lattice Lambda and the Weierstrass sigma-function sigma(z) and quasi-period
homomorphism eta: Lambda -> C extended R-linearly,
lambda(z) = -log| e^{-(1/2) z eta(z)} sigma(z) Delta(Lambda)^{1/12} |
          = (1/2) Re(z eta(z)) - log|sigma(z)| - (1/12) log|Delta(Lambda)|.
The Delta^{1/12} factor makes it model-independent. **Corollary 3.3 (the
quasi-parallelogram law):**
lambda(P+Q) + lambda(P-Q) = 2 lambda(P) + 2 lambda(Q) + v(x(P) - x(Q)) - (1/6) v(Delta),
the bilinear-form structure of the local height (note (x(P)-x(Q))^6/Delta is
model-independent). **Theorem 3.4 (the q-expansion):** with u = e^{2 pi i z},
q = e^{2 pi i tau} and B_2(T) = T^2 - T + 1/6 the second Bernoulli polynomial,
lambda(z) = -(1/2) B_2(Im z / Im tau) log|q| - log|1 - u| - sum_{n>=1} log|(1-q^n u)(1-q^n
u^-1)|. This is the form Cohen Alg. 7.5.7 evaluates (proof uses the sigma and Delta product
expansions plus Legendre's relation eta(1) tau - eta(tau) = ... = 2 pi i).

**§VI.4 Non-archimedean explicit formulas, Theorems 4.1 and 4.2 (book pp. 469-475).**
Theorem 4.1: over a non-archimedean complete field, for P in E_0(K) (the points with
nonsingular reduction), lambda(P) = (1/2) max(v(x(P)^-1), 0) + (1/12) v(Delta). Theorem
4.2 (Tate curve / multiplicative reduction): with the Tate parametrization
phi: K*/q^Z -> E_q(K) and u the parameter,
lambda(phi(u)) = (1/2) B_2(v(u)/v(q)) v(q) + v(1-u) + sum_{n>=1} v((1-q^n u)(1-q^n u^-1)),
and (choosing 0 <= v(u) < v(q)) this is (1/2) B_2(v(u)/v(q)) v(q) when 0 < v(u) < v(q).
The SAME second Bernoulli polynomial B_2 appears: archimedean (Theorem 3.4) and
multiplicative-reduction (Theorem 4.2) heights share the B_2 structure, with v(u)/v(q) the
non-archimedean analogue of Im z / Im tau. Additive-reduction formulas are deferred to
exercises 6.7-6.8 (the III/IV/I_M* cases of Silverman 1988 Theorem 5.2).

## Points mapped to the project

1. **Theorem 1.1's axioms are what 2I REPRODUCES, not transcribes.** The duplication axiom
   (iii) lambda([2]P) = 4 lambda(P) + v(2y+a1x+a3) - (1/4)v(Delta) is the walk-back
   recursion in
   [`e2i_archimedean_local_height.py`](../../../experiments/arithmetic_geometric/e2i_archimedean_local_height.py).
   The UNIQUENESS half of Theorem 1.1 is why 2I matching h-hat to ~1e-8 is a COMPLETE check:
   no other function satisfies the axioms, so the validated series IS the local height. ->

2. **Theorem 2.1 is the identity 2P validates end to end.** h-hat = sum_v n_v lambda_v is
   the theorem; 2P's h_inf + sum_p h_p = h-hat on 37a1/389a1/5077a1 and the I_2 curve is the
   numerical confirmation. The residual in 2P is purely the h-hat limit truncation, not a
   decomposition error. This pins the A_arch + sum_p A_p = h-hat Arakelov picture to a
   citable theorem (the "Silverman, ATAEC, Ch. VI" in the 2I status block). ->

3. **Theorem 3.2 / 3.4 is the genuine archimedean lambda_inf of 2I.** 2I self-derives an
   equivalent telescoping series; ATAEC VI.3 is the authoritative closed form
   (sigma-function, Theorem 3.2; q-expansion with B_2, Theorem 3.4). The Delta^{1/12} factor
   is the same discriminant normalization 2L computes the Petersson norm ||Delta||_Pet of
   in
   [`e2l_faltings_petersson.py`](../../../experiments/arithmetic_geometric/e2l_faltings_petersson.py). ->

4. **Corollary 3.3 (the quasi-parallelogram law) is why A_arch is a genuine bilinear form.**
   The archimedean Gram matrix 2I builds (positive definite at rank 1-2, indefinite at rank
   3 for 5077a) is lambda evaluated at P+Q, P-Q; Cor 3.3 is what makes those entries a
   well-defined symmetric pairing. The A_arch block IS this archimedean bilinear form, and
   its signature is a meaningful Hodge-index datum, not an artifact; global positivity
   comes from adding the finite blocks. ->

5. **Theorem 4.2's B_2(v(u)/v(q)) is the multiplicative formula behind 2O's period-2
   finding.** 2O measured the bad-prime local height on the I_2 curve taking exactly two
   values (period-2 in the multiple k), matching the Z/2 component group. Theorem 4.2 is
   why: the multiplicative local height is B_2(v(u)/v(q)) v(q)/2, a function of the
   component index, constant on each component. Theorem 4.1 is why integral x on a good or
   I_1 prime gives zero (the case 2O closed rigorously). ->

## What this changes for the program

- **2I and 2L are grounded in the sigma-function theory.** ATAEC VI.3 (Theorems 3.2, 3.4)
  is the authoritative archimedean local height; 2I's self-derived series is an equivalent
  route to the same lambda_inf, certified by Néron uniqueness (VI.1). 2L's Delta^{1/12} /
  Petersson-norm self-intersection is the archimedean factor of this formula.
- **The local decomposition is a theorem, not a hope.** VI.2 (Theorem 2.1) proves
  h-hat = sum lambda_v; 2P is confirmation. The A_arch + sum_p A_p = h-hat picture is a
  citable theorem.
- **The B_2 structure unifies the archimedean and multiplicative pieces.** Theorem 3.4 and
  Theorem 4.2 share the second Bernoulli polynomial, with Im z / Im tau (archimedean)
  paralleling v(u)/v(q) (multiplicative). This is the height-side hint of the
  finite-vs-archimedean "same object at two places" theme (compare the GLO q-deformation,
  2Q's two-clock question).

## Status

- **Honest depth:** read Chapter VI §§1-4 (book pp. 455-475) in depth: Theorem 1.1
  (axioms + existence/uniqueness proof), Theorem 2.1 (the decomposition), Theorem 3.2
  (sigma-function formula), Corollary 3.3 (quasi-parallelogram law), Theorem 3.4
  (q-expansion with B_2), Theorem 4.1 (E_0 non-archimedean formula), Theorem 4.2 (Tate-curve
  multiplicative formula with B_2). Did NOT read Chapters I-V (modular functions, CM,
  elliptic surfaces, Néron models / Tate's algorithm, q-curves), nor the additive-reduction
  exercises 6.7-6.8.
- **Used by:** experiment 2I (the archimedean lambda_inf sigma-function theory; the VI.1
  uniqueness that certifies the numerical match), 2L (the Delta^{1/12} Petersson-norm
  self-intersection), 2O/2P (the VI.4 non-archimedean / Theorem 4.2 multiplicative formula).
- **Direction 8 bearing:** VI.3 makes the A_arch block concrete and transcendental
  (sigma-function), VI.4 makes the finite blocks the component-group arithmetic, VI.2 ties
  them to h-hat. The single-surface arithmetic Hodge index is exactly this decomposition
  with the validated positive-definiteness of the assembled pairing (2H/2M).
