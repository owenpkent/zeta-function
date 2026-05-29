# Reading notes: Silverman, *Computing Heights on Elliptic Curves* (Math. Comp. 51, 1988)

> Computational-source note, read IN FULL. Folder
> [`references/07_elliptic_curve_heights/`](../../../references/README.md). 20-page paper
> (Math. Comp. 51, no. 183, pp. 339-358). This is the ORIGINAL source of the archimedean
> switch-series and the non-archimedean case-split that experiments 2I and 2P implement,
> and the primary documentation of the factor-of-2 normalization the project rediscovered.
> Pages refer to the journal page numbers printed on each page.
> Read: pp. 339-358 in full (intro; §1 Tate's series; §2 the universally-convergent
> modified series + pseudocode; §3 resultant lemmas; §4 explicit error bounds; §5 the
> non-archimedean Theorem 5.2 + pseudocode; §6 the four worked examples).

## One-line takeaway

This paper is the practical algorithm the project's archimedean local height is built on:
Tate's geometrically-convergent series lambda_v(P) = (1/2) log|x|_v + (1/8) sum 4^-n c_n
for real places, plus Silverman's §2 modification that switches between the parameters
t = 1/x and t' = 1/(x+1) whenever |x| gets small (so the series converges over C and
unconditionally), and the §5 non-archimedean case-split (Theorem 5.2) that becomes Cohen
Alg. 7.5.6 and Cremona Prop. 3.4.1. The Remark on p. 341 is the primary documentation of
the factor-of-2 normalization ambiguity that bit experiments 2I and 2P.

## Technical content (section by section)

**Setup and Néron's axioms (§0-1, pp. 339-341).** For E/K given by the general
Weierstrass equation (1), the canonical height h-hat: E(K) -> R is a quadratic form, and
the limit definition h-hat(P) = lim 4^-n h(x(2^n P)) is "not practical for computation"
(p. 339). Instead one uses the decomposition into local heights, Eq. (2):
h-hat(P) = sum_{v in M_K} n_v lambda-hat_v(P), the multiplicities n_v chosen so the
product formula makes the sum independent of K. The non-archimedean lambda_v is given "by
intersection theory in a well-known manner" (§5); the archimedean lambda_v is "a
transcendental function, and so efficient computation is somewhat more difficult" (p. 339).
Néron's three axioms (Eqs. 6-8, p. 341) characterize lambda_v uniquely:
- (6) duplication: lambda_v(2P) = 4 lambda_v(P) - log|2y + a1 x + a3|_v for 2P != O;
- (7) the limit lim_{P->O} (lambda_v(P) - (1/2) log|x(P)|_v) exists;
- (8) lambda_v is bounded on any v-adic open subset of E(K_v) disjoint from O.

**The factor-of-2 normalization Remark (p. 341).** Silverman states explicitly: "the
local height is sometimes normalized slightly differently. Specifically, the duplication
formula is often given with (1/4) log|Delta|_v added onto the right-hand side. ... if we
use lambda'_v to denote this new local height, then lambda_v = lambda'_v + (1/12)
log|Delta|_v." He notes that for COMPUTING he uses the lambda_v normalization (no Delta
term) because "the product formula will ensure that the extra term vanishes," while
"for theoretical purposes, lambda'_v is often more useful." This is the documented
convention split: his paper uses the SMALLER normalization, the books/BSD use the larger.

**Tate's series, Theorem 1.2 (§1, pp. 341-343).** With t = 1/x, set (Eqs. 9)
w(t) = 4t + b2 t^2 + 2 b4 t^3 + b6 t^4 and z(t) = 1 - b4 t^2 - 2 b6 t^3 - b8 t^4.
Substituting into the duplication formula (5) for x(2P) gives x(2P) = z/w and
t(2P) = 1/x(2P) = w/z (Eq. 10). Defining mu by (1/8) mu(P) = lambda(P) - (1/2) log|x(P)|_v
(Eq. 11), one gets mu(2P) = 4 mu(P) - 4 log|z(P)|_v (Eq. 12), which telescopes to
mu(P) = sum_{n=0}^N 4^-n log|z(2^n P)|_v + 4^-N mu(2^N P) (Eq. 13). Theorem 1.2 (Tate):
if every Q in E(K_v) has |x(Q)|_v > epsilon, then
lambda(P) = (1/2) log|x(P)|_v + (1/8) sum_{n>=0} 4^-n log|z(2^n P)|_v, with error O(4^-N)
in N terms. Converges provided no point of E(K_v) has x = 0; over R one can shift
coordinates to ensure this, but "if K_v = C, then the shifting trick no longer works."

**The universally-convergent modified series, Theorem 2.2 (§2, pp. 343-346).** When some
2^n P has small x, switch to the shifted parameter x' = x + 1, t' = t/(1+t), with primed
invariants (Eq. 14): b2' = b2 - 12, b4' = b4 - b2 + 6, b6' = b6 - 2b4 + b2 - 4,
b8' = b8 - 3b6 + 3b4 - b2 + 3, and primed w', z' the analogues of w, z. The two parameters
are related by mu = mu' + 4 log|1+t|_v (Eq. 17), giving the "mixed" duplication formulas
(Eq. 18): mu(Q) = log|z(Q) + w(Q)|_v + (1/4) mu'(2Q) and
mu'(Q) = log|z'(Q) - w'(Q)|_v + (1/4) mu(2Q). Theorem 2.2 assembles a sequence c_n with
Boolean switching flags beta_n (beta = 1 = use t-series, beta = 0 = use t'-series),
switching whenever |w| > 2|z| (resp. |w'| > 2|z'|), so that
lambda(P) = (1/2) c_{-1} + (1/8) sum_{n>=0} 4^-n c_n converges for ANY local field,
real or complex, with error O(4^-N). The paper gives explicit PSEUDOCODE (p. 345) for the
subroutine: initialize t = 1/x if |x| >= 1/2 (beta = 1) else t = 1/(x+1) (beta = 0),
then loop computing w, z, accumulating mu += 4^-n log|z| (or log|z+w| with a switch
beta -> 1-beta), and return lambda = ... + (1/8) mu.

**Resultant lemmas and explicit error bounds (§3-4, pp. 346-350).** Proposition 3.1:
Res(z(T), w(T)) = Delta^2 (the resultant of the two Tate polynomials is the square of the
discriminant; three proofs given, including via the doubling map as a finite morphism of
P^1). Lemma 3.2 bounds how small two polynomials with distinct roots can simultaneously
be. Theorem 4.2 makes the error explicit: log||Delta_v|^2 / 2^60 H^8| <= c_n <=
log(2^11 H) where H = max(4, |b2|, 2|b4|, 2|b6|, |b8|), and (part c) to get d decimal
places it suffices to take N >= (5/3)d + 1/2 + (3/4) log(7 + (4/3) log H + (1/3) log
max(1, |Delta_v|^-1)) terms. Example 4.3: 50 decimals for a curve with H <= 10^100 needs
about 89 terms.

**Non-archimedean local height, Theorem 5.2 (§5, pp. 351-354).** With ord_v normalized
onto Z and a v-minimal Weierstrass equation, the case-split:
- (a) good / nonsingular reduction (P in E_0(K_v), detected by
  ord_v(3x^2 + 2a2 x + a4 - a1 y) <= 0 OR ord_v(2y + a1 x + a3) <= 0):
  lambda_v(P) = max(0, -(1/2) log|x|_v);
- (b) multiplicative reduction (ord_v(c4) = 0, type I_N): with N = ord_v(Delta) and
  n = min(ord_v(2y+a1x+a3), N/2), lambda_v(P) = (n(N-n)/(2N)) log|Delta|_v. (Lemma 5.1
  derives n = ord_v(2y+a1x+a3) when 0 < n < N/2; this is the I_N component-group index.)
- (c) additive type IV / IV* (ord_v psi_3 >= 3 ord_v psi_2):
  lambda_v(P) = (1/3) log|psi_2(P)|_v;
- (d) additive type III / III* / I_M* (otherwise): lambda_v(P) = (1/8) log|psi_3(P)|_v,
  where psi_2 = 2y+a1x+a3, psi_3 = 3x^4+b2x^3+3b4x^2+3b6x+b8. PSEUDOCODE on p. 354 (the
  A, B, C, N, M case-split returning Lambda log(q_v)/[K_v:Q_v]).

**Worked examples (§6, pp. 355-357).** Example 1: X_1(11), E: y^2 + y = x^3 - x^2 over
Q(sqrt(-2)), the point P = (2 + sqrt(-2), 1 + 2 sqrt(-2)), archimedean height computed to
50 digits (0.45754773...). Example 2-3: y^2 + 4y = x^3 + 6ix over Q(i), the complex case
where the C-convergent §2 series is needed; h-hat((0,0)) = 0.33689820... Example 4 (the
one that matters for 2O): E: y^2 + 21xy + 494y = x^3 + 26x^2 over Q, P = (0,0), with
Delta = -2^13 13^3 19^2, multiplicative reduction at 2, 13, 19. The TABLE on p. 357 gives
the per-prime heights via Theorem 5.2(b): at p=2, N=13, n=1, lambda = -(6/13) log 2 =
-0.3199...; at p=13, N=3, n=1, lambda = -(1/3) log 13 = -0.8543...; at p=19, N=2, n=1,
lambda = -(1/4) log 19 = -0.7361...; archimedean lambda = 1.9215...; total h-hat(P) =
0.010492. This is the multiplicative-reduction worked example whose I_N structure 2O
measured.

## Points mapped to the project

1. **Néron's three axioms (Eqs. 6-8) are what 2I self-derives from, not transcribes.**
   The 2I docstring rebuilds the archimedean series from the duplication formula and
   validates it against h-hat; the walk-back recursion
   lambda_inf(Q) = (1/4) lambda_inf(2Q) + (1/2) log|2y+a1x+a3| in
   [`e2i_archimedean_local_height.py`](../../../experiments/arithmetic_geometric/e2i_archimedean_local_height.py)
   is exactly axiom (6) rearranged into the h-hat normalization. ->

2. **Tate's series (Theorem 1.2) is verbatim the 2I telescoping ansatz.** The polynomials
   z(t) = 1 - b4 t^2 - 2 b6 t^3 - b8 t^4 and w(t) = 4t + b2 t^2 + 2 b4 t^3 + b6 t^4 in 2I's
   `_z` and `_w` are Silverman's Eq. (9) exactly; 2I's series mu = (1/2) log|x| + (1/2)
   sum 4^-(n+1) log|z| is the (1/8) sum 4^-n c_n of Theorem 1.2 with c_n = log|z(2^n P)|. ->

3. **The §2 modified switch-series (Theorem 2.2) IS the 2P beta-switch.** The
   `if |x|<0.5: t=1/(x+1); beta=0 else: t=1/x; beta=1` logic and the primed-invariant
   formulas b2' = b2-12, b4' = b4-b2+6, b6' = b6-2b4+b2-4, b8' = b8-3b6+3b4-b2+3 in
   [`e2p_silverman_local_heights.py`](../../../experiments/arithmetic_geometric/e2p_silverman_local_heights.py)
   are Eq. (14) and the pseudocode on p. 345 transcribed (via Cremona §3.4). 2I lacked the
   switch and worked around small/zero x by doubling up to |x| >= 1; 2P added the
   authoritative Theorem-2.2 switch and so handles complex places and small x correctly. ->

4. **The factor-of-2 Remark (p. 341) is the exact trap 2I hit.** 2I's docstring records:
   "the bare ansatz reconstructed h-hat/2 EXACTLY -- the documented factor-of-2 between
   Silverman's 1988 paper and his books / the LMFDB regulator convention." That is
   precisely the lambda_v vs lambda'_v = lambda_v + (1/12) log|Delta|_v split on p. 341.
   2I rescaled lambda = 2 mu to land in the h-hat = sum_v lambda_v (BSD) convention; the
   project's whole local-decomposition program (2I/2L/2O/2P) uses the doubled convention. ->

5. **Theorem 5.2 is the origin of the finite case-split in Cohen 7.5.6 / Cremona 3.4.1.**
   The A, B, C, N, M case-split in 2P's `finite_local_height` is Theorem 5.2 verbatim (via
   Cremona, who states "this is Theorem 5.2 of [59]"). The multiplicative branch
   lambda_v = n(N-n)/(2N) log|Delta|_v (case b) is the I_N component-group height; the
   period-2 behavior 2O measured on the I_2 curve y^2 = x^3 + 19x - 20 is exactly this
   formula over the Z/2 component group, and Example 4's table (p. 357) is the worked
   precedent for reading bad-prime contributions as n(N-n)/N rationals times log p. ->

## What this changes for the program

- **2I's self-derivation is validated against its primary source.** Every piece 2I
  reconstructed empirically (the z, w polynomials, axiom 6, the factor-of-2) is explicitly
  in this paper. The numerical agreement with h-hat plus Néron uniqueness (the axioms have
  a unique solution) means 2I's series IS the local height, not merely a function that
  happens to match.
- **2P is the authoritative archimedean algorithm; 2I is the validated hand-derived
  precursor without the switch.** Theorem 2.2 (the universally convergent series) is what
  2P adds over 2I; this paper is the literal source.
- **The normalization is traced to its primary documentation.** The perennial factor-of-2
  in 2I/2L/2P is the p. 341 Remark, restated by Cremona (Gross's footnote). The project's
  convention (h-hat = sum_v lambda_v, BSD, double the paper) is the right one, and the
  regulator's positive-definiteness (the Direction-8 signature) depends on this being
  consistent across all places.

## Status

- **Honest depth:** read all 20 pages. §1-2 (the two archimedean series + pseudocode) and
  §5 (the non-archimedean Theorem 5.2 + pseudocode) are the load-bearing sections and are
  transcribed precisely above; §3-4 (resultant lemmas, explicit O(4^-N) error bounds) read
  for the N-term count formula 2P uses; §6 examples read in full, including Example 4's
  multiplicative-reduction table relevant to 2O.
- **Used by:** experiment 2I (archimedean series from the axioms; the factor-of-2
  normalization), 2P (Theorem 2.2 switch-series and Theorem 5.2 finite case-split, via
  Cohen/Cremona), 2O (the multiplicative branch n(N-n)/(2N), I_N component periodicity).
- **Direction 8 bearing:** primary source of the archimedean A_arch series and the
  finite-place case-split. The normalization Remark documents the height convention the
  arithmetic-Hodge-index signature (the positive-definite regulator of 2H/2M) is read off
  in. The transcendental-archimedean / algebraic-finite split is Silverman's §1-vs-§5 split.
