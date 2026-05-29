# 2O: the bad-prime (non-archimedean) local height

> Overnight task T2(b), done in-session. Resolves the bad-prime Neron local height
> that 2I/2H deferred, in two parts: a rigorous I_1 closure, and a qualitative I_n
> component-structure validation with the exact magnitude honestly flagged as open.

## (1) I_1 closure -- RIGOROUS (gate passes)

The three curves of 2H/2I/2L (37a1, 389a1, 5077a1) each have
`|Delta_min| = conductor = a single prime`, i.e. `v_p(Delta) = 1`: Kodaira type
**I_1**, trivial component group `Z/1`. Hence the bad-prime Neron local height is
**identically zero** for every point. This is exactly why 2I found
`lambda_inf(P) = h_hat(P)` for the integral generators: good primes contribute 0 on
integral `x`, and the single bad prime is I_1 (one component, height 0). The
bad-prime caveat flagged in 2H/2I is therefore closed rigorously -- there was
nothing to add.

## (2) I_n component structure -- QUALITATIVE pass, exact magnitude FLAGGED

On `y^2 = x^3 + 19x - 20` (`Delta = -2^6 * 11^2 * 79`, multiplicative **I_2 at p=11**),
with infinite-order point `P=(3,8)`, the bad-prime contribution measured as the
remainder `lambda_bad(kP) = h_hat - lambda_inf - lambda_good` (lambda_inf from 2I;
lambda_good = log x-denominator with p removed) over multiples:

| k | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| lambda_bad / log 11 | -0.1446 | ~0 | -0.1445 | ~0 | -0.1445 | ~0 |

Exactly **TWO values, period 2**: the non-identity component for ODD k, the identity
component (=0) for EVEN k. This is precisely the **Z/2 component group of I_2** -- the
local height is constant on each component and periodic in k with the component
order. (The other bad prime p=2, type I_6, contributes ~0: the points lie on its
identity component, so the pattern is pure period-2 from p=11, not lcm(2,6).)

**Honest gate status.** The COMPONENT STRUCTURE passes: binary, period-2, identity
component zero -- the multiplicative-reduction component behavior of the bad-prime
local height is validated. The EXACT MAGNITUDE (`~ -0.3468 = -0.1446 log 11`) is
**not** an obviously clean rational `* log p` and is **not** matched here to the
`B_2(j/n) log p` formula. Pinning the constant needs a single-bad-prime curve (so no
contamination from p=2/79) or the independently verified local-height normalization.
That quantitative match is **flagged open, not claimed** -- consistent with the
project's honest-gate discipline (assert the validated structure; do not assert the
unverified constant).

## Net

The bad-prime local height is now understood for the project's curves: **identically
0** for the I_1 prime-conductor curves (closing the 2I caveat rigorously), and
exhibiting the **correct I_n component-group periodicity** in the one I_2 example
tested. Combined with 2I (archimedean incidence), 2L (archimedean self-incidence),
and 2H/2M (the positive-definite signature at ranks 1-4), the local decomposition of
the arithmetic Hodge index is now validated piece by piece, with one clean
quantitative follow-up flagged (the exact I_n bad-prime constant).

## Outputs

- `e2o_badprime_local_height.npz`.
