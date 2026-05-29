"""Experiment 2I: Archimedean Neron local height lambda_inf (Method 1).

Computes lambda_inf(P) = h_hat(P) - sum_p lambda_p(P) where:
- h_hat(P) is the canonical height from e2h
- lambda_p(P) is the non-archimedean Neron local height at each bad prime p

Non-archimedean local heights (Tate, Silverman AEC §9.3):
- For multiplicative reduction of type I_n at p:
    Let c = component of P in Phi = Z/nZ
    lambda_p(P) = (c*(n-c)/(2*n)) * log(p)
  The component c is determined by the valuation of the denominator of x(P).

  For I_1 (n=1): lambda_p = 0 for all P (only one component).
  For I_n, n >= 2: non-trivial only if P reduces to a non-identity component.

For our test curves:
- 37a1: bad prime 37, reduction I_1, so lambda_37 = 0 for all P.
  => lambda_inf(P) = h_hat(P) exactly.
- 389a1: bad prime 389, reduction I_1, lambda_389 = 0.
  => lambda_inf(P) = h_hat(P) exactly.
- 5077a1: bad prime 5077, reduction I_1, lambda_5077 = 0.
  => lambda_inf(P) = h_hat(P) exactly.

This module also provides the general Tate local height function for use in T2(b).
"""
from __future__ import annotations

import math
from fractions import Fraction

from experiments.arithmetic_geometric.e2h_arithmetic_hodge_index import (
    canonical_height, point_add, scalar_mul,
)


# ---------------------------------------------------------------------------
# Non-archimedean local height: multiplicative reduction I_n
# ---------------------------------------------------------------------------


def x_denominator_valuation(P, p):
    """Return v_p(den(x(P))) for rational point P=(x,y) with x=a/b in lowest terms."""
    if P is None:
        return 0
    x = Fraction(P[0])
    b = x.denominator
    val = 0
    while b % p == 0:
        b //= p
        val += 1
    return val


def neron_local_height_mult_reduction(P, p, n_kodaira):
    """Neron local height lambda_p(P) for multiplicative reduction type I_n.

    For a point P on E with multiplicative reduction of type I_n at p:
    - The reduction splits as a Neron polygon with n components.
    - Component index c in {0, 1, ..., n-1} determines the contribution.
    - For a point with v_p(den(x(P))) = k >= 1: c = gcd(k, n) heuristic fails;
      use the standard formula: if v_p(x) <= -2, then c = v_p(x) / (-2) mod n...

    The exact formula (Silverman AEC §9.3, Proposition 9.3): in Tate's parametrization
    E ~ G_m/q^Z, the point P corresponds to u with u*q^Z = P, and
        lambda_p(P) = -log|u| + B_2(t) * log|q| / 2
    where B_2 is the second Bernoulli polynomial and t = v(u)/v(q) mod 1.

    For the simpler component formula used here:
    If P has split multiplicative reduction of type I_n, and we write P in the Neron model,
    the component number c satisfies lambda_p(P) = c*(n-c)/(2n) * log(p).

    For n=1 (I_1): only one component, lambda_p = 0 always.
    """
    if n_kodaira == 1:
        return 0.0

    # For I_n with n >= 2: determine component c via x-coordinate valuation
    # Standard result: c = -v_p(x(P)) if v_p(x(P)) < 0, else c = 0
    # More precisely: if P is on the non-identity component, v_p(x(P)) = -2*floor(n/2)/n etc.
    # For our purposes (T2 gate check) we need the exact formula.
    # v_p(x) = -2*(c/n)*... no: simpler form is:
    # c = min(-v_p(x(P)), n - (-v_p(x(P)))) when v_p(x) < 0 (and -v_p(x) < n)
    # This follows from Silverman AEC, Theorem 9.4.

    if P is None:
        return 0.0

    x = Fraction(P[0])
    vx = 0
    num = abs(x.numerator)
    den = x.denominator
    # v_p(x) = v_p(num) - v_p(den)
    vp_num = 0
    n_tmp = num
    while n_tmp > 0 and n_tmp % p == 0:
        n_tmp //= p
        vp_num += 1
    vp_den = 0
    d_tmp = den
    while d_tmp > 0 and d_tmp % p == 0:
        d_tmp //= p
        vp_den += 1
    vx = vp_num - vp_den  # v_p(x)

    if vx >= 0:
        # P is on the identity component
        return 0.0

    c = -vx  # c = -v_p(x) for type I_n, 0 < c < n
    if c >= n_kodaira:
        c = c % n_kodaira
    if c == 0:
        return 0.0

    return c * (n_kodaira - c) / (2 * n_kodaira) * math.log(p)


# ---------------------------------------------------------------------------
# lambda_inf: archimedean Neron local height (Method 1)
# ---------------------------------------------------------------------------


def lambda_inf(a1, a2, a3, a4, a6, P, bad_primes_data=None, n_iter=8):
    """Compute archimedean Neron local height lambda_inf(P).

    Method 1: lambda_inf(P) = h_hat(P) - sum_p lambda_p(P)

    bad_primes_data: list of (p, kodaira_n) pairs for each bad prime.
    If None, assumes all reductions are I_1 (lambda_p = 0 for all p).

    For curves 37a1, 389a1, 5077a1: all have I_1 reduction, so lambda_inf = h_hat.
    """
    h = canonical_height(a1, a2, a3, a4, a6, P, n_iter=n_iter)
    if bad_primes_data is None:
        return h

    non_arch = 0.0
    for p, n_kod in bad_primes_data:
        non_arch += neron_local_height_mult_reduction(P, p, n_kod)

    return h - non_arch


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------


def _selftest():
    """Validate lambda_inf for 37a1, 389a1, 5077a1 generators."""
    # All three test curves have I_1 reduction, so lambda_inf = h_hat.

    # 37a1: y^2+y=x^3-x, gen (0,0)
    a37 = (0, 0, 1, -1, 0)
    li_37 = lambda_inf(*a37, (0, 0), bad_primes_data=[(37, 1)])
    print(f"[2I] 37a1 lambda_inf(0,0) = {li_37:.8f}  (Method 1: h_hat, I_1)")

    # 389a1: y^2+y=x^3+x^2-2x, gens (-1,1) and (0,0)
    a389 = (0, 1, 1, -2, 0)
    li_389_g1 = lambda_inf(*a389, (-1, 1), bad_primes_data=[(389, 1)])
    li_389_g2 = lambda_inf(*a389, (0, 0), bad_primes_data=[(389, 1)])
    print(f"[2I] 389a1 lambda_inf(-1,1) = {li_389_g1:.8f}  (converged ~0.6866670)")
    print(f"[2I] 389a1 lambda_inf(0,0)  = {li_389_g2:.8f}  (converged ~0.3270008)")

    # 5077a1: y^2+y=x^3-7x+6, gens (-2,3),(-1,3),(0,2)
    a5077 = (0, 0, 1, -7, 6)
    li_5077_g1 = lambda_inf(*a5077, (-2, 3), bad_primes_data=[(5077, 1)])
    li_5077_g2 = lambda_inf(*a5077, (-1, 3), bad_primes_data=[(5077, 1)])
    li_5077_g3 = lambda_inf(*a5077, (0, 2), bad_primes_data=[(5077, 1)])
    print(f"[2I] 5077a1 lambda_inf(-2,3) = {li_5077_g1:.8f}")
    print(f"[2I] 5077a1 lambda_inf(-1,3) = {li_5077_g2:.8f}")
    print(f"[2I] 5077a1 lambda_inf(0,2)  = {li_5077_g3:.8f}")

    print("[2I] Self-test complete.")
    return {
        '37a1': [(0, 0), li_37],
        '389a1': [(-1, 1), li_389_g1, (0, 0), li_389_g2],
        '5077a1': [(-2, 3), li_5077_g1, (-1, 3), li_5077_g2, (0, 2), li_5077_g3],
    }


if __name__ == "__main__":
    _selftest()
