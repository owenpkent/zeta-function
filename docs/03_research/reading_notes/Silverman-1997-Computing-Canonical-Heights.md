# Reading notes: Silverman, *Computing Canonical Heights with Little (or No) Factorization* (Math. Comp. 66, 1997)

> Computational-source note. Folder
> [`references/07_elliptic_curve_heights/`](../../../references/README.md). This is a
> 19-page paper; read the abstract, intro, and §1 (the algorithm description, including
> the finite local-height case-split and the factorization-avoiding regrouping). A
> continuation of Silverman 1988. Pages refer to the PDF. Read: pp. 787-790 (intro, the
> decomposition formula (3), the local-height case-split, the gcd(c4,c6) regrouping idea).

## One-line takeaway

This paper sharpens the canonical-height computation of Silverman 1988 in two ways the
project uses: it states the practical decomposition `h_hat(P) = lambda_inf(P) + log(d) +
sum_{p | Delta, p does not divide d} lambda_p(P)` for `P = (a/d^2, b/d^3)` (separating the
trivial `log(d)` good-reduction part from the genuinely bad primes), and it gives a method
to compute the non-archimedean total WITHOUT factoring `Delta` (group terms with the same
local-height form, factoring only `gcd(c4, c6)`). It also points at Cohen's Alg. 7.5.7 as
the fast theta archimedean series.

## The points that matter, mapped to the project

1. **The practical decomposition formula (3), p. 788.** For `P = (a/d^2, b/d^3)` in lowest
   terms, `h_hat(P) = lambda_inf(P) + log(d) + sum_{p | Delta, p does not divide d} lambda_p(P)`.
   The `log(d)` term collects the good-reduction contribution of primes dividing the
   denominator; only bad primes not dividing `d` need the full local-height case-split.
   -> This is exactly the form 2O/2P organize around: 2P's "sum over `p | Delta or p | den(x)`"
   and 2O's "lambda_good = log x-denominator with p removed." Formula (3) is why 2I found
   `lambda_inf(P) = h_hat(P)` for integral generators: integral `x` means `d = 1`, so
   `log(d) = 0` and the bad-prime terms vanish on the identity component (the I_1 case 2O
   closed). Cremona's Eq. (3.4.2) is this same formula with the BSD factor of 2.

2. **The finite local-height case-split (p. 789).** With `A = ord_v(...)`, `B = ord_v(2y+a1 x+a3)`,
   `N = ord_v(Delta)`, `n = min(B, N/2)`: good reduction `lambda_v = max(0, -(1/2) ord_v(x))`;
   multiplicative `lambda_v = -n(N-n)/(2N)`; additive `C>=3B` gives `-(1/3)B`, else `-(1/8)C`.
   -> The same case-split as Silverman 1988 Theorem 5.2 / Cohen 7.5.6 / Cremona 3.4.1, in
   the BSD-halved normalization (note the `1/2`, `1/(2N)`, `1/8` vs the doubled forms 2P
   uses). The multiplicative branch `-n(N-n)/(2N)` is the I_n component-group height whose
   period-2 behavior 2O measured on the I_2 curve.

3. **The fast archimedean series is Cohen 7.5.7 (p. 788).** Silverman states there are two
   standard archimedean methods: the Tate switch-series of his 1988 paper ("[20]"), which
   "converges geometrically," and "an alternative series, somewhat more complicated but
   much faster converging, in [3, Algorithm 7.5.7]," which uses Néron/Tate's theta-function
   form with the elliptic integrals computed by the AGM.
   -> This pins the cross-reference: Cohen GTM 138 Alg. 7.5.7 (the theta/AGM series the
   project notes as the high-precision route) is named here as the fast alternative to the
   1988 switch-series. The `A_arch` block can be computed either way; 2I/2P used the
   switch-series, Cohen 7.5.7 is the faster theta route if precision becomes the bottleneck.

4. **Factorization-free non-archimedean total (the paper's actual contribution).** Group
   the terms of (3) whose `lambda_p` have the same form, so the non-archimedean total can be
   computed factoring only `gcd(c4, c6)` rather than all of `Delta`. Useful for curves with
   huge coefficients (large-rank searches) where `Delta` cannot be factored.
   -> Not on the critical path for the project's small curves (37a/389a/5077a have prime
   conductor, trivial to factor), so 2O/2P factor `Delta` directly. This matters only if a
   future experiment reaches into the large-coefficient / large-rank regime where the
   `A_arch` block must be assembled for a curve with an unfactorable discriminant. Worth
   knowing the method exists; not needed at current rank 1-4.

## What this changes for the program

- **Confirms the 2P/2O decomposition is the textbook one.** Formula (3) with the `log(d)`
  good-reduction term is the practical canonical-height decomposition; 2P implements it and
  validated it to `~1e-8`. The project's organization (archimedean + `log(den)` + bad
  primes) is exactly Silverman 1997's.
- **Names Cohen 7.5.7 as the fast archimedean route.** If `A_arch` precision ever limits a
  computation, this paper says use the theta/AGM series (Cohen 7.5.7), not the geometric
  switch-series. A useful pointer, not a current need.
- **Has a factorization-free path for large curves.** When the program eventually tests the
  height pairing on high-rank / large-coefficient curves (more generators for a richer
  `A_arch` signature), this paper's regrouping is the tool that makes the non-archimedean
  total computable without factoring `Delta`.

## Status

- **Honest depth:** read the abstract, intro, and §1 algorithm description (pp. 787-790):
  the decomposition (3), the local case-split, the Cohen 7.5.7 pointer, and the
  factorization-avoiding idea. Did not work through the later sections' worked examples and
  the detailed bounds on the `gcd(c4,c6)` grouping; the method is understood from §1.
- **Used by:** the project's local-decomposition program (2O/2P) uses the same decomposition
  and case-split; this paper is the "little or no factorization" reference cited in the 07
  folder index. The factorization-free method itself is not yet exercised (curves are
  small).
- **Direction 8 bearing:** confirms the `A_arch + log(d) + sum_p A_p = h_hat` structure and
  supplies the scaling path (factorization-free finite total, fast theta archimedean series)
  for ever pushing the single-surface signature computation to larger, higher-rank curves.
