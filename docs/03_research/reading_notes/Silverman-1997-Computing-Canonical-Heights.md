# Reading notes: Silverman, *Computing Canonical Heights with Little (or No) Factorization* (Math. Comp. 66, 1997)

> Computational-source note, read IN DEPTH. Folder
> [`references/07_elliptic_curve_heights/`](../../../references/README.md). 19-page paper
> (Math. Comp. 66, no. 218, pp. 787-805). A continuation of Silverman 1988. Read the
> abstract, intro, §1 (the decomposition formula (3), the finite case-split, and the full
> factorization-avoiding regrouping machinery), and §2 (the pseudocode). This note states
> the practical decomposition and the factorization-free method precisely. Pages refer to
> the journal page numbers printed on each page.
> Read: pp. 787-797 (intro through the §2 pseudocode and subroutines).

## One-line takeaway

This paper sharpens the canonical-height computation of Silverman 1988 in two ways the
project uses. It states the practical decomposition (3)
h-hat(P) = lambda_inf(P) + log(d) + sum_{p | Delta, p does not divide d} lambda_p(P) for
P = (a/d^2, b/d^3), separating the trivial log(d) good-reduction part from the genuinely
bad primes; and it gives a method to compute the non-archimedean total WITHOUT factoring
Delta, by grouping primes p whose lambda_p/log p share the same value n_p/N_p (factoring
only gcd(c4, c6)). It also names Cohen Alg. 7.5.7 as the fast theta archimedean series.

## Technical content (section by section)

**The motivation and decomposition (3) (intro + Step 1, pp. 787-788).** The standard
method is h-hat(P) = sum_v n_v lambda_v(P) (Eq. 2). The archimedean lambda_inf is "easily
computed using a rapidly convergent series"; the bad-prime lambda_p are "extremely easy to
calculate" ONCE you know which primes divide Delta. The bottleneck is factoring Delta for
curves with large coefficients (which arise in high-rank searches, where independence is
tested via det(<P_i, P_j>) != 0). The practical decomposition, for P = (a/d^2, b/d^3) in
lowest terms (Eq. 3): h-hat(P) = lambda_inf(P) + log(d) + sum_{p | Delta, p does not divide
d} lambda_p(P). The log(d) term collects the good-reduction contribution of primes dividing
the denominator; only bad primes not dividing d need the full case-split.

**The finite local-height case-split (p. 789).** With A, B from the usual numerators,
N = ord_v(Delta), n = min(B, N/2): good reduction (min(A,B) <= 0)
lambda_v = max(0, -(1/2) ord_v(x)); multiplicative (ord_v(c4)=0) lambda_v = -n(N-n)/(2N);
additive C >= 3B gives -(1/3)B, else -(1/8)C. (Same as Silverman 1988 Theorem 5.2 / Cohen
7.5.6 / Cremona 3.4.1, in the smaller normalization with the explicit 1/2, 1/(2N), 1/3,
1/8.) Remark: these are NON-NORMALIZED heights; the literature symbol may differ by
v(Delta), which cancels when summed.

**The fast archimedean series is Cohen 7.5.7 (Step 4, p. 790).** Two standard methods:
Tate's geometric switch-series of Silverman 1988 ("[20]"), and "an alternative series,
somewhat more complicated but much faster converging, in [3, Algorithm 7.5.7]," using the
Néron/Tate theta-function form with periods via the AGM.

**The factorization-free machinery (Steps 5-9, pp. 790-797, the paper's actual
contribution).** The 9-step algorithm avoids factoring Delta:
- Step 3: factor only gcd(c4, c6) to get a minimal model.
- Step 5: formal-group / denominator contribution H += (1/2) log(denominator of x_1).
- Step 6: strip small primes p < p_0 (a chosen bound) directly.
- Step 7: additive-reduction primes are exactly those dividing gcd(c4, c6), already known.
- Step 8: "good reduction" primes (P in E_0(Q_p)) are removed by computing
  A_1 = num(3x^2+2a2x+a4-a1y), B_1 = num(2y+a1x+a3) and replacing Delta by
  gcd(Delta, A_1^inf, B_1^inf) (the part composed of primes dividing A_1, B_1), NO
  factoring needed.
- Step 9: multiplicative-reduction primes are handled WITHOUT factoring Delta_1 by
  exploiting that t_p(Q) = n_p(Q)/N_p satisfies t_p(mQ) = m t_p(Q) mod Z. Compute
  2P, 3P, ... mod Delta_{m-1}, set B_m = 2y_m + a1 x_m + a3, split off
  Delta_m = gcd(Delta_{m-1}, B_m^inf). Primes with n_p/N_p = i/m are isolated by computing
  gcd(Delta'_m, B_k) for several k and inverting an integer matrix M_m of least-residue
  entries {ij}_m (the "Demjanenko-type" matrix). The contribution is
  H -= (1/2) sum_{i, gcd(i,m)=1} (i(m-i)/m^2) log gcd(Delta'_m, alpha_i^inf). The m-loop
  runs m = 2..10 (the matrix M'_m fails to invert at m = 16, 4 | m).

**Pseudocode (§2, pp. 795-797).** The full PROGRAM with the gcd(M, N^inf) subroutine
(repeated gcd until stable) and the minimal-model subroutine.

## Points mapped to the project

1. **Decomposition (3) is the form 2O/2P organize around.** 2P sums over "p | Delta or
   p | den(x)" and 2O's "lambda_good = log x-denominator with p removed" are Eq. (3). It is
   why 2I found lambda_inf(P) = h-hat(P) for INTEGRAL generators: integral x means d = 1, so
   log(d) = 0 and the bad-prime terms vanish on I_1 primes (the case 2O closed). Cremona's
   Eq. (3.4.2) h-hat = h_inf + 2 log(c) + sum_p h_p is this same formula in the doubled BSD
   normalization. ->

2. **The finite case-split (p. 789) is Silverman 1988 Theorem 5.2 restated.** Same A, B, C,
   N, M logic 2P implements (the multiplicative branch -n(N-n)/(2N) is the I_N
   component-group height 2O measured period-2 on). Note the smaller normalization here vs
   the doubled forms 2P uses. ->

3. **Names Cohen 7.5.7 as the fast archimedean route.** Pins the cross-reference: the
   theta/AGM series 2P/2I note as the high-precision route is "[3, Algorithm 7.5.7]." The
   A_arch block can be computed the geometric switch-series way (2I/2P) or the faster theta
   way (Cohen 7.5.7) if precision becomes the bottleneck. ->

4. **The factorization-free machinery is the scaling path for larger curves.** Not on the
   critical path now: 37a/389a/5077a have prime conductor, trivial to factor, so 2O/2P
   factor Delta directly. It matters only when the program reaches large-coefficient /
   high-rank curves (more generators for a richer A_arch signature) where Delta is
   unfactorable. The t_p(mQ) = m t_p(Q) mod Z trick and the Demjanenko-type matrix are the
   tools that make the non-archimedean total computable then. Worth knowing it exists; not
   needed at current rank 1-4. ->

## What this changes for the program

- **Confirms the 2P/2O decomposition is the textbook one.** Formula (3) with the log(d)
  good-reduction term is the practical canonical-height decomposition; 2P implements it and
  validated it to ~1e-8. The project's organization (archimedean + log(den) + bad primes)
  is exactly Silverman 1997's.
- **Names the fast archimedean route.** If A_arch precision ever limits a computation, use
  the theta/AGM series (Cohen 7.5.7), not the geometric switch-series. A pointer, not a
  current need.
- **Has a factorization-free path for large curves.** When the program tests the height
  pairing on high-rank / large-coefficient curves, the §1 regrouping (the n_p/N_p = i/m
  isolation via the integer matrix) is the tool that makes the non-archimedean total
  computable without factoring Delta.

## Status

- **Honest depth:** read pp. 787-797: the decomposition (3), the local case-split, the
  Cohen 7.5.7 pointer, and the full factorization-avoiding machinery (Steps 5-9 with the
  Demjanenko-type matrix M_m) plus the §2 pseudocode. Did not work through the §3 worked
  examples in detail; the method is fully understood from §1-2.
- **Used by:** the project's local-decomposition program (2O/2P) uses the same decomposition
  and case-split; the "little or no factorization" reference cited in the 07 folder index.
  The factorization-free machinery itself is not yet exercised (curves are small).
- **Direction 8 bearing:** confirms the A_arch + log(d) + sum_p A_p = h-hat structure and
  supplies the scaling path (factorization-free finite total, fast theta archimedean series)
  for pushing the single-surface signature computation to larger, higher-rank curves where
  the A_arch block has more generators and the Hodge-index signature is richer.
