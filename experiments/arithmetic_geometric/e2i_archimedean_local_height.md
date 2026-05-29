# 2I: the genuine archimedean Neron local height, self-derived and validated

> Experiment [e2i_archimedean_local_height.py](e2i_archimedean_local_height.py).
> Completes the archimedean question 2H left open: compute the genuine archimedean
> Neron local height `lambda_inf(P)` (the transcendental piece the naive coordinate
> split could not see) and show how the archimedean place carries the arithmetic
> Hodge index regulator over Spec(Z).

## What 2H left, and why this is the right object

2H showed the height pairing on `E(Q)` is positive definite (Faltings-Hriljac,
validated against LMFDB regulators), but its naive coordinate split assigned the
archimedean place ~0 -- the wrong decomposition. The genuine archimedean
contribution is the Neron local height `lambda_inf`, a transcendental quantity.

## Self-derived, not transcribed (and validated against ground truth)

Rather than transcribe Tate's series (the source PDFs would not extract cleanly,
and the literature carries a known factor-of-2 normalization trap), the series is
**derived** from the duplication formula and the canonical recursion, then
**validated numerically** against the already-LMFDB-matched canonical height
`h_hat`. With b-invariants and `t = 1/x`, `1/x(2P) = w(t)/z(t)` where
`z(t)=1-b4 t^2-2 b6 t^3-b8 t^4`, `w(t)=4t+b2 t^2+2 b4 t^3+b6 t^4`. The telescoping
ansatz `mu(P)=½log|x|+½ sum 4^{-(n+1)} log|z(t_n)|` satisfies
`mu(P)-¼mu(2P)=¼log|2y+a1 x+a3|`, whose sum over all places is 0 by the product
formula, so `sum_v mu_v` is canonical.

**The factor of 2, found empirically.** The bare ansatz reconstructed `h_hat/2`
*exactly* for every test point -- the documented Silverman-paper-vs-books
normalization. Rescaling to `lambda = 2 mu` (so `lambda_inf = log|x| + sum 4^{-(n+1)} log|z|`,
walk-back `lambda(Q)=¼lambda(2Q)+½log|2y+a1 x+a3|`) gives the `h_hat = sum_v lambda_v`
convention. Small/zero `x` (e.g. 37a's `(0,0)`) is handled by doubling up to
`|x|>=1`, running the series, and walking back.

## Validation (CONFIRMED, residual limited only by h_hat precision)

`lambda_inf(P) + log(den x(P)) = h_hat(P)`, residuals 1e-5 to 1e-9 across all points
(the residual is the canonical-height limit truncation, not the local height):

| curve | point | h_hat | lambda_inf | finite | recon | resid |
|---|---|---:|---:|---:|---:|---:|
| 37a | P=(0,0) | 0.051103 | 0.051111 | 0 | 0.051111 | 8e-6 |
| 389a | P=(-1,1) | 0.686642 | 0.686667 | 0 | 0.686667 | 3e-5 |
| 389a | 2P (x-den 9) | 2.746650 | 0.549444 | 2.197225 (=log 9) | 2.746668 | 2e-5 |
| 5077a | P=(-2,3) | 1.368572 | 1.368573 | 0 | 1.368573 | 6e-9 |
| 5077a | 2P (x-den ...) | 5.474290 | 1.582470 | 3.891820 | 5.474290 | 3e-8 |

For non-integral points the finite places enter and the full local decomposition
`lambda_inf + sum_p lambda_p = h_hat` validates exactly -- a strong, independent
check on both the archimedean series and the finite formula.

## The result: how the archimedean place enters the signature

- **The archimedean place carries 100% of the diagonal.** Every generator here has
  integral `x`, so its finite local heights vanish and `lambda_inf(P) = h_hat(P)`:
  each individual canonical height is purely archimedean. The archimedean trace
  share of the regulator is 100%.

- **But positivity (the signature) is GLOBAL, not archimedean-only.** The
  archimedean pairing matrix alone is positive definite at ranks 1 and 2 but
  **indefinite at rank 3** (5077a: archimedean Gram det = -0.92). The off-diagonal
  finite contributions (from non-integral `P+Q`) are what make the *total* pairing
  positive definite (Faltings-Hriljac). Neither place alone produces the signature;
  the archimedean place supplies the bulk (all the diagonal) and the finite places
  supply the off-diagonal corrections.

This is the concrete, correct answer to "how does the archimedean place enter the
arithmetic Hodge index signature," and it mirrors the session's 3M two-clock theme
on the arithmetic-geometry side: positivity is a balance between the archimedean
cushion (here, the entire diagonal) and the finite places (here, the off-diagonal
glue), with the signature emerging only from their sum.

## Status

- **Solid, validated:** the genuine archimedean Neron local height, self-derived
  and confirmed against LMFDB-matched `h_hat` to ~1e-5; the finite local heights
  (exact); the full local decomposition `lambda_inf + sum_p lambda_p = h_hat`; and
  the structural reading (archimedean carries the diagonal, positivity is global).
- **References for cross-check (not needed for correctness here):** Cohen,
  *A Course in Computational Algebraic Number Theory*, Algorithm 7.5.7; Silverman,
  *Advanced Topics in the Arithmetic of Elliptic Curves*, Ch. VI.
- **Direction 8 bearing:** 2G (function field) + 2H + 2I (arithmetic) together make
  the Hodge-index signature concrete and validated on a single arithmetic surface,
  with the archimedean place's role pinned. The open lift remains the product
  surface `Spec(Z) x Spec(Z)` and its Frobenius -- where this archimedean
  local-height structure would have to be globalized into a genuine intersection
  pairing.

## Outputs

- `e2i_archimedean_local_height.npz`: per-curve pairing matrices (full/arch), shares, residuals.
- `e2i_archimedean_local_height.png`: validation residuals + archimedean regulator share.
