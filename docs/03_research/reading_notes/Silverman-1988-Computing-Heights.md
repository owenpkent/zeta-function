# Reading notes: Silverman, *Computing Heights on Elliptic Curves* (Math. Comp. 51, 1988)

> Computational-source note. Folder
> [`references/07_elliptic_curve_heights/`](../../../references/README.md). This is a
> 20-page paper; read the intro and the two main algorithms (the modified Tate series,
> Theorem 2.2; the non-archimedean local height, Theorem 5.2), plus the worked examples.
> This is the ORIGINAL source of the archimedean switch-series 2I/2P use and the finite
> case-split. Pages refer to the PDF. Read: pp. 339-345, 355 (intro, Néron axioms,
> Tate's series, the modified series, an example).

## One-line takeaway

This paper gives the practical algorithm the project's archimedean local height is built
on: Tate's geometrically-convergent series `lambda(P) = (1/2) log|x| + (1/4) sum 4^-n c_n`
for `lambda_v` over R, plus Silverman's modification that switches between the parameters
`t = 1/x` and `t' = 1/(x+1)` whenever `|x|` gets small (so the series converges over C and
without a coordinate shift), and the non-archimedean case-split (Theorem 5.2) that becomes
Cohen 7.5.6 / Cremona 3.4.1. It also documents the factor-of-2 normalization ambiguity
that bit experiments 2I and 2P.

## The points that matter, mapped to the project

1. **The three Néron local-height properties (p. 341, Eqs. 6-8).** `lambda_v` is the
   unique function with: the duplication relation `lambda(2P) = 4 lambda(P) - log|2y+a1 x+a3|_v`;
   the limit `lambda(P) - (1/2) log|x(P)|_v -> finite` as `P -> O`; boundedness off `O`.
   -> These are exactly the relations 2I uses to SELF-DERIVE its series (the walk-back
   `lambda(Q) = (1/4) lambda(2Q) + (1/2) log|2y+a1 x+a3|` in the 2I note is this
   duplication relation rearranged). 2I did not transcribe the series; it rebuilt it from
   these axioms and validated it. This paper is the original statement of the axioms.

2. **Tate's series (Theorem 1.2, p. 342).** With `t = 1/x`, `w = 4t + b2 t^2 + 2 b4 t^3 + b6 t^4`,
   `z = 1 - b4 t^2 - 2 b6 t^3 - b8 t^4`, the archimedean local height is
   `lambda(P) = (1/2) log|x| + (1/4) sum_{n>=0} 4^-n log|z(2^n P)|`, error `O(4^-N)`.
   Converges provided no point of `E(K_v)` has `x = 0`.
   -> This is verbatim the 2I telescoping ansatz: `z(t) = 1 - b4 t^2 - 2 b6 t^3 - b8 t^4`,
   `mu(P) = (1/2) log|x| + (1/2) sum 4^-(n+1) log|z|` (2I note). The `z`, `w` definitions
   match. 2I's "factor of 2 found empirically" is the normalization remark below.

3. **The modified universally-convergent series (Theorem 2.2, §2, pp. 343-345).** When
   some `2^n P` has small `x`-coordinate, switch to the shifted parameter `x' = x+1`
   (`t' = t/(1+t)`, primed `b'_i = b2-12, b4-b2+6, b6-2b4+b2-4, b8-3b6+3b4-b2+3`), run the
   primed series, switch back when `|x'|` gets small. This makes the series converge over
   C and unconditionally.
   -> This is the `beta`-switch in 2P's algorithm (the `if |x|<0.5: t=1/(x+1); beta=0`
   logic in [`e2p_silverman_local_heights.py`](../../../experiments/arithmetic_geometric/e2p_silverman_local_heights.py)).
   2I lacked this switch and worked around small `x` by doubling up to `|x|>=1`; 2P fixed
   that with the authoritative Theorem-2.2 switch. The primed `b'_i` formulas in 2P's
   docstring are Eq. (14) of this paper.

4. **The factor-of-2 normalization remark (p. 341, Remark after Eq. 8).** Silverman notes
   the local height "is sometimes normalized slightly differently": the duplication formula
   is often given with `(1/2) log|Delta|_v` added, so `lambda'_v = lambda_v + (1/12) log|Delta|_v`;
   his paper uses the smaller normalization, "double those" of the BSD-appropriate one.
   -> This is the exact trap 2I hit: "the bare ansatz reconstructed `h_hat/2` exactly...
   the documented Silverman-paper-vs-books normalization." 2I rescaled `lambda = 2 mu` to
   match the `h_hat = sum_v lambda_v` (BSD) convention. Cremona §3.4 states the same:
   "all the formulae here are double those in the paper [59]." This paper IS [59], and its
   Remark is the primary documentation of the convention 2I/2L/2P all had to pin.

5. **The non-archimedean local height (Theorem 5.2, the finite algorithm).** Computes
   `lambda_v` at a finite prime by the `A = ord_v(3x^2+2a2 x+a4-a1 y)`,
   `B = ord_v(2y+a1 x+a3)`, `C = ord_v(3x^4+...)`, `N = ord_v(Delta)`, `M = min(B, N/2)`
   case-split (good / multiplicative / additive).
   -> This is the SAME case-split that becomes Cohen Alg. 7.5.6 and Cremona Prop. 3.4.1,
   implemented in 2P. Silverman 1988 Theorem 5.2 is the origin; Cremona explicitly says
   "this is Theorem 5.2 of [59]." The I_n component periodicity 2O observed is the
   multiplicative-reduction branch (`M(M-N)/N`) of this theorem.

## What this changes for the program

- **2I's self-derivation is validated against the right source.** The `z`, `w`,
  duplication relation, and the factor-of-2 normalization 2I reconstructed empirically
  are all explicitly in this paper. 2I rebuilt Theorem 1.2 from the axioms and discovered
  the Remark's normalization the hard way; the agreement confirms 2I is correct.
- **2P's `beta`-switch is Theorem 2.2.** The convergence-stabilizing `x <-> x+1` switching
  that 2P adds over 2I is exactly Silverman's §2 modification. 2P is the authoritative
  archimedean algorithm; 2I is the (correct, validated) hand-derived precursor without the
  switch.
- **The normalization is now traced to its primary source.** The perennial factor-of-2 in
  2I/2L/2P is documented here (p. 341 Remark) and restated by Cremona. The project's
  convention (`h_hat = sum_v lambda_v`, BSD normalization, double the paper) is the right one.

## Status

- **Honest depth:** read intro + the two main algorithms (Thm 2.2 archimedean switch-series,
  Thm 5.2 finite case-split) + the normalization Remark + Example 1 (the `X_1(11)` curve
  over `Q(sqrt(-2))`, archimedean height to 50 digits). Did not read the explicit
  tail-estimate proofs of §3-4 (Lemma 4.1, Theorem 4.2 error bound), which 2P uses only as
  the `N >= (5/3)d + 1/2 + (3/4)log(7 + (4/3)log H)` term-count formula (transcribed in the
  2P docstring).
- **Used by:** experiment 2I (the archimedean series, derived from these axioms; the
  factor-of-2 normalization), 2P (Theorem 2.2 switch-series and Theorem 5.2 finite
  case-split, via Cohen/Cremona), 2O (the multiplicative-reduction branch / I_n
  periodicity).
- **Direction 8 bearing:** this is the primary source of the archimedean `A_arch` series
  and the finite-place case-split. The normalization Remark is the documentation behind
  the project's height convention, which the regulator's positive-definiteness (the
  signature) depends on being consistent across places.
