# 2H: the arithmetic Hodge index over Spec(Z) (Faltings-Hriljac), validated

> Experiment [e2h_arithmetic_hodge_index.py](e2h_arithmetic_hodge_index.py). The
> step of [Direction 8](../../docs/03_research/research_directions/08_hodge_index_surface.md)
> after the 2G function-field template: exhibit the closest existing theorem to the
> Direction 8 target -- the Faltings-Hriljac arithmetic Hodge index, which holds
> over Spec(Z) -- as a positive-definite signature, and probe the archimedean place.

## The theorem being exhibited

For the minimal regular model of an elliptic curve E/Q (an arithmetic surface
E -> Spec(Z)), the Faltings-Hriljac theorem says the Arakelov intersection pairing
on degree-0 arithmetic divisors equals minus the Neron-Tate canonical height
pairing on E(Q); equivalently, the canonical height pairing on the Mordell-Weil
group is POSITIVE DEFINITE. This is the arithmetic Hodge index theorem: positivity
from a signature, over Spec(Z), and a genuine theorem (unlike the
Spec(Z) x Spec(Z) surface, which does not exist). It is the arithmetic analogue of
2G's negative-definite primitive intersection form, and the first rung of the
Direction 8 stack where a Hodge-index signature is a theorem over the integers.

## Method (exact, validated)

Canonical height via the standard limit `h_hat(P) = lim_n h_x(2^n P) / 4^n`, with
the group law in exact rationals (sympy) so x(2^n P) is an exact fraction. The
pairing `<P,Q> = (1/2)(h_hat(P+Q) - h_hat(P) - h_hat(Q))` builds the Gram matrix on
independent points.

## Result (HEADLINE, solid)

Rank 1, 2, 3 curves (LMFDB generators), all positive definite:

| curve | rank | pairing eigenvalues | signature | regulator (computed) | known |
|---|---:|---|---|---:|---:|
| 37a1 `y^2+y=x^3-x` | 1 | 0.05111 | (1, 0) | 0.051107 | 0.051111 |
| 389a1 `y^2+y=x^3+x^2-2x` | 2 | 0.1837, 0.8300 | (2, 0) | 0.152456 | 0.15246 |
| 5077a1 `y^2+y=x^3-7x+6` | 3 | 0.1560, 1.2244, 2.1842 | (3, 0) | 0.417142 | 0.41714 |

The computed regulators **match the known LMFDB values**, validating the pipeline.
The height pairing is positive definite for every curve: the arithmetic Hodge index
over Spec(Z), exhibited as a signature. This is the Spec(Z) analogue of 2G, and a
genuine theorem.

## An honest caveat about the archimedean place

The naive coordinate split `h_x = h_inf + h_fin` with
`h_inf = log max(|x|, 1)`, `h_fin = log den(x)` is exact at every step, but it is
NOT the Neron / Arakelov local-height decomposition. Empirically `h_inf / 4^n -> 0`
for all curves: the multiples 2^n P equidistribute on E(R), so |x(2^n P)| stays
bounded and the naive archimedean part washes out in the canonical limit. So the
naive split assigns ~0% to the archimedean place, and the finite (log-denominator)
part carries the whole canonical limit.

This is a TRUE fact, but it is a fact about the naive split, not about the
archimedean place's real contribution. The genuine archimedean Neron local height
`lambda_inf(P)` -- the transcendental Weierstrass-sigma / Green's-function quantity
that measures the archimedean place in the Arakelov picture -- is NOT this
coordinate part, and is not computed here. That its naive coordinate proxy is
canonically invisible is itself the lesson: the archimedean contribution does not
live in coordinates; it requires genuinely analytic (non-algebraic) machinery.
That is exactly the framing document's theme (section 4.2) that the archimedean
place is the subtle missing piece a Spec(Z) cohomology must learn to carry.

## One rigorous increment on the finite side (no transcendental input needed)

For a prime p of GOOD reduction, the Neron local height is the exact, elementary
quantity `lambda_p(P) = (1/2) max{0, -v_p(x(P))} log p`. Every generator used here
(37a (0,0); 389a (-1,1),(0,0); 5077a (-2,3),(-1,3),(0,2)) has INTEGRAL x, so
`v_p(x) >= 0` and `lambda_p(P) = 0` for every good prime p. Each curve has prime
conductor with a single bad prime (37, 389, 5077), far larger than any denominator
that appears. Hence:

  the entire good-finite contribution to the regulator is exactly ZERO; the
  positive-definite regulator is carried by the archimedean place together with at
  most the single bad prime.

This is the correct (and, for integral points, opposite-to-naive) statement: the
arithmetic Hodge index positivity for these curves is essentially an ARCHIMEDEAN
phenomenon, consistent with the whole session's theme (3M: the archimedean cushion
must dominate the finite obstruction).

## Status and next step

- **Solid:** the arithmetic Hodge index over Spec(Z) (height pairing positive
  definite, rank 1-3) is exhibited and validated against known regulators. With 2G
  this completes the "signature" picture on both sides of the function-field /
  number-field divide. The good-finite local heights of the integral generators
  vanish exactly, so the regulator is archimedean (plus a single bad prime).
- **Next (needs the exact algorithm, deliberately deferred):** the genuine
  archimedean Neron local height `lambda_inf(P)` and the single bad-prime term, to
  split the regulator as `lambda_inf + lambda_bad` exactly and quantify the
  archimedean share. This requires Tate's archimedean series (Silverman 1988,
  Math. Comp. 51, section III) -- with the documented factor-of-2 normalization
  caveat between his paper and his books -- or the Weierstrass-sigma closed form
  with its exact constants, validated by `sum_v lambda_v = h_hat`. It was NOT
  implemented here rather than ship an unvalidated transcendental formula into the
  codebase; the cleanest path is a battle-tested implementation (PARI `ellheight` /
  its local-height functions) cross-checked against the `h_hat` values this
  experiment already validates.

## Outputs

- `e2h_arithmetic_hodge_index.npz`: per-curve pairing matrices (full/arch/fin), eigenvalues.
- `e2h_arithmetic_hodge_index.png`: positive-definite signature; naive-split archimedean part (~0).
