# Reading notes: Cohen, *A Course in Computational Algebraic Number Theory* (GTM 138, 1993)

> Computational-authority note, §7.5 read IN DEPTH. Folder
> [`references/07_elliptic_curve_heights/`](../../../references/README.md) (single-surface
> height machinery for Architecture 2, Direction 8). 556-page reference textbook, NOT read
> cover to cover: read the §7.4-7.5 elliptic-curve material in depth (the canonical-height
> framing on book p. 404, Algorithm 7.5.6 the finite part, Algorithm 7.5.7 the archimedean
> theta/q-expansion part on book p. 405). This note states both algorithms step by step and
> points the program at the exact source experiment 2P implements. Pages refer to the BOOK
> page numbers printed on each page (PDF offset ~ +20).
> Read: book pp. 394-409 (the elliptic-curve algorithms, both height algorithms, the
> regulator/BSD framing).

## One-line takeaway

Cohen §7.5 gives the two textbook algorithms that decompose the canonical height of a
point on E/Q into local pieces: Algorithm 7.5.6 computes the FINITE (non-archimedean)
contribution by the A, B, C, N, M valuation case-split (= Silverman 1988 Theorem 5.2), and
Algorithm 7.5.7 computes the ARCHIMEDEAN contribution by a theta-function / q-expansion
series built from the periods omega1, omega2 and the elliptic logarithm of P. Their sum is
h-hat(P). This is the authoritative source experiment 2P names in its header, and the
per-place decomposition whose archimedean block is the A_arch of Direction 8. Book p. 404
also states the regulator IS the height-pairing determinant and the pairing is "positive
definite," the computational form of the Faltings-Hriljac signature.

## Technical content (section by section)

**The canonical height and the regulator (book p. 404).** Cohen states the limit
definition h-hat(P) = lim_{n->inf} h(2^n P) / 2^{2n} "exists and defines a positive
definite quadratic form on R tensor E(Q)." The symmetric bilinear form
<P, Q> = h-hat(P+Q) - h-hat(P) - h-hat(Q) is the canonical height pairing "used to compute
the regulator in the Birch and Swinnerton-Dyer Conjecture 7.3.9." Key properties stated:
h-hat(P) = 0 iff P is torsion; det(<P_i, P_j>) = 0 iff there is a relation among the P_i
that is a torsion point; hence on a basis P_1,...,P_r of the torsion-free part, the
determinant R(E/Q) is the elliptic regulator. Cohen then notes the height "can be expressed
as a sum of local functions, one for each prime number p and one for the Archimedean prime
infinity," computed "in this form to Silverman [Sil2]," always assuming a global minimal
equation (obtained by Algorithm 7.5.3, Tate's algorithm).

**Algorithm 7.5.6 (finite part of the height), book p. 404.** Given the global minimal
model a1,...,a6 and a rational P = (x, y):
1. [Initialize] Compute b2, b4, b6, b8, c4, Delta via Formulas (7.1). Set
   z <- (1/2) ln(denominator of x);
   A <- numerator of 3x^2 + 2a2 x + a4 - a1 y;
   B <- numerator of 2y + a1 x + a3;
   C <- numerator of 3x^4 + b2 x^3 + 3 b4 x^2 + 3 b6 x + b8;
   D <- gcd(A, B).
2. [Loop on p] If D = 1, output z and terminate. Otherwise choose a prime p | D, set
   D <- D/p until p does not divide D.
3. [Add local contribution] If p does not divide c4, set N <- v_p(Delta),
   n <- min(v_p(B), N/2), z <- z - (n(N-n)/(2N)) ln p. Otherwise, if v_p(C) >= 3 v_p(B)
   set z <- z - (v_p(B)/3) ln p; else z <- z - (v_p(C)/8) ln p. Go to step 2.

This is the FINITE block of the decomposition h_inf + sum_p h_p = h-hat, the Silverman
1988 Theorem 5.2 case-split in textbook form (the (1/2), (1/(2N)), (1/3), (1/8)
coefficients are the smaller normalization; the project doubles them).

**Algorithm 7.5.7 (archimedean height at infinity), book p. 405.** Cohen flags that the
archimedean term, originally defined via sigma-functions and then via Tate's geometric
series (Silverman 1988), "has a faster rate of convergence by using q-expansions, so it
should be preferred for high-precision calculations":
1. [Initialize] Compute b2, b4, b6, Delta. Use Algorithm 7.4.7 for the periods
   omega1, omega2; Algorithm 7.4.8 for the elliptic logarithm z of P. Set
   lambda <- 2 pi / omega1, t <- lambda Re(z), q <- e^{2 i pi omega2 / omega1}
   (q real, |q| < 1).
2. [Compute theta function] theta <- sum_{n>=0} sin((2n+1) t) (-1)^n q^{n(n+1)/2},
   stopping when q^{n(n+1)/2} is sufficiently small.
3. [Terminate] Output
   (1/32) ln|Delta / q| + (1/8) ln( (x^3 + (b2/4) x^2 + (b4/2) x + b6/4) / lambda )
   - (1/4) ln|theta|.

The canonical height is the sum of the 7.5.6 and 7.5.7 contributions. The archimedean
term is a TRANSCENDENTAL object: a theta value at the elliptic logarithm of P. (The
"theta" here is the Jacobi theta series; this is the q-expansion form of the
sigma-function formula of Silverman ATAEC VI.3 / Theorem 3.4.)

**The neighboring machinery (book pp. 394-403, 7.4-7.5.3).** Algorithm 7.4.7/7.4.8 (the
period lattice and elliptic logarithm via the AGM), Algorithm 7.4.10 (reduction of a
general cubic to Weierstrass form), 7.5.1/7.5.3 (Tate's algorithm and the minimal model)
are the input subroutines; the period lattice via AGM is the same machinery 2L uses for
tau and the Petersson norm. §7.5.3 (the L-function, Prop. 7.5.8) is the BSD analytic side,
not used by the height experiments.

## Points mapped to the project

1. **Algorithm 7.5.6 is the finite local height in 2P.** The A, B, C, N, M case-split in
   `finite_local_height` of
   [`e2p_silverman_local_heights.py`](../../../experiments/arithmetic_geometric/e2p_silverman_local_heights.py)
   is Algorithm 7.5.6 (in the doubled BSD normalization). 2P's corrected attribution on the
   I_2 curve (the -0.347 contribution coming from p=2, not p=11) is this case-split applied
   prime by prime. Cited in the 2P header "Cohen Alg. 7.5.6/7.5.7." ->

2. **Algorithm 7.5.7 is the fast theta/q-expansion archimedean height.** This is the
   analytic A_arch diagonal. Silverman 1997 names it by this exact ID ("[3, Algorithm
   7.5.7]") as the fast alternative to the Tate switch-series. 2P's archimedean block
   h_inf and 2I's lambda_inf both compute this quantity (2P/2I use the geometric
   switch-series route; 7.5.7 is the faster theta route Cohen recommends for
   high-precision); 2P validated the total to ~1e-8 against the independent limit h-hat. ->

3. **The algebraic-vs-analytic split IS the finite-vs-archimedean split.** Algorithm 7.5.6
   returns rational multiples of log p (intersection-theoretic, arithmetic); Algorithm
   7.5.7 returns a transcendental theta value. 2I made this structural fact central: the
   archimedean place carries the transcendental bulk of the regulator (100% of the diagonal
   for integral generators), the finite places are arithmetic corrections. This is the
   finite-vs-archimedean split of the Arakelov / Hodge-index decomposition. ->

4. **Book p. 404's regulator statement IS the single-surface signature.** Cohen states the
   height pairing is a positive-definite quadratic form and R(E/Q) = det(<P_i, P_j>) with
   det = 0 iff dependent. That is the Faltings-Hriljac positive-definiteness validated in
   2H/2M against LMFDB regulators. The Direction-8 task is to make that determinant's sign
   emerge from an intersection form on Spec(Z) x Spec(Z), not just from the analytic
   height; Cohen is the computational statement of the positivity that has to be lifted. ->

## What this changes for the program

- **2P is grounded in the authoritative reference.** The finite case-split (7.5.6) and the
  theta archimedean series (7.5.7) are the textbook algorithms; the program cites Cohen GTM
  138 §7.5 as the reference implementation behind the validated h_inf + sum_p h_p = h-hat
  decomposition. No re-derivation needed.
- **The fast archimedean route is theta/q-expansion, not the Tate switch-series.** If the
  A_arch diagonal precision ever becomes the bottleneck (large rank, large height), 7.5.7's
  q-expansion is the preferred algorithm; the geometric switch-series of Silverman 1988 /
  Cremona §3.4 is the slower fallback 2I/2P currently use.
- **Positive-definiteness of the pairing is the computational form of the signature.**
  Cohen's regulator-determinant statement is the single-surface positivity 2H/2M validated;
  Direction 8 is the task of giving that sign an intersection-theoretic origin.

## Status

- **Honest depth:** read book pp. 394-409 (the §7.4-7.5 elliptic-curve algorithms), both
  height algorithms stated step by step above and matched against the 2P implementation,
  plus the regulator/BSD framing on p. 404. Did NOT read the other ~540 pages (number-field
  algorithms, factoring, lattice reduction, class groups) -- not relevant to the height
  decomposition.
- **Used by:** experiment 2P (both algorithms, verbatim), 2I (the archimedean part, the
  named cross-check reference), 2L (the AGM period machinery 7.4.7).
- **Direction 8 bearing:** the per-place height decomposition is the Arakelov-style local
  picture on a single arithmetic surface; the archimedean block (7.5.7) is the A_arch
  diagonal, the finite blocks (7.5.6) the off-diagonal arithmetic glue, and the
  positive-definiteness of their sum (p. 404) is the validated single-surface signature.
