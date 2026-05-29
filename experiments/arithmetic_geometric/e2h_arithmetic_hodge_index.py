"""Experiment 2H: Canonical height, group law, and height pairing matrix.

Implements:
- Rational group law on Weierstrass curves (exact Fraction arithmetic)
- Canonical (Neron-Tate) height via iterative x-coordinate doubling
- Height pairing <P, Q> = (h(P+Q) - h(P) - h(Q)) / 2
- Positive-definiteness check for rank-r pairing matrices

The canonical height uses EXACT Fraction arithmetic for n_iter doublings.
Convergence: |h_naive(2^n P)/4^n - h_hat| <= C/(3*4^n) where C = sup|eps|.
For n_iter=8: error <= ~3e-5 for curves with C <= 5. Sufficient for gate < 1e-4.

The denominator of x(2^n P) grows like exp(h_hat * 4^n). For n=8 and h_hat <= 0.5,
denominator is ~exp(13000) ~ 10^5700: Python big-integer arithmetic handles this
but is slow (~1-5s per doubling for the large curves). n_iter=7 (error ~1e-4) is
used for curves where h_hat > 0.3 to keep runtime under 60s per point.

Reference: Silverman AEC Ch VIII; Cremona "Algorithms" Ch 3.
"""
from __future__ import annotations

import math
from fractions import Fraction


# ---------------------------------------------------------------------------
# Group law (exact Fraction arithmetic)
# ---------------------------------------------------------------------------


def point_add(a1, a2, a3, a4, a6, P, Q):
    """Add two rational points on y^2+a1*x*y+a3*y = x^3+a2*x^2+a4*x+a6."""
    if P is None:
        return Q
    if Q is None:
        return P

    x1, y1 = Fraction(P[0]), Fraction(P[1])
    x2, y2 = Fraction(Q[0]), Fraction(Q[1])
    a1, a2, a3, a4, a6 = (Fraction(c) for c in (a1, a2, a3, a4, a6))

    if x1 == x2:
        if y1 + y2 + a1*x2 + a3 == 0:
            return None
        t = 2*y1 + a1*x1 + a3
        lam = (3*x1**2 + 2*a2*x1 + a4 - a1*y1) / t
        mu  = (-x1**3 + a4*x1 + 2*a6 - a3*y1) / t
    else:
        lam = (y2 - y1) / (x2 - x1)
        mu  = (y1*x2 - y2*x1) / (x2 - x1)

    x3 = lam**2 + a1*lam - a2 - x1 - x2
    y3 = -(lam + a1)*x3 - mu - a3
    return x3, y3


def point_neg(a1, a3, P):
    """Negate P = (x, y): returns (x, -y - a1*x - a3)."""
    if P is None:
        return None
    x, y = Fraction(P[0]), Fraction(P[1])
    return x, -y - Fraction(a1)*x - Fraction(a3)


def scalar_mul(a1, a2, a3, a4, a6, n, P):
    """Compute n*P by double-and-add (exact Fraction arithmetic)."""
    if n == 0 or P is None:
        return None
    if n < 0:
        P = point_neg(a1, a3, P)
        n = -n
    P = (Fraction(P[0]), Fraction(P[1]))
    result = None
    base = P
    while n > 0:
        if n & 1:
            result = point_add(a1, a2, a3, a4, a6, result, base)
        base = point_add(a1, a2, a3, a4, a6, base, base)
        n >>= 1
    return result


# ---------------------------------------------------------------------------
# Canonical height
# ---------------------------------------------------------------------------


def naive_height(x_frac):
    """Naive Weil height: log(max(|num|, den)) for x = num/den in lowest terms."""
    f = Fraction(x_frac)
    return math.log(max(abs(f.numerator), f.denominator))


def canonical_height(a1, a2, a3, a4, a6, P, n_iter=8):
    """Compute canonical height h_hat(P) via iterative doubling.

    h_hat(P) = lim_{n->inf} h_naive(x(2^n P)) / 4^n

    Uses exact Fraction arithmetic. n_iter=8 gives error <= C/(3*4^8) ~ 2e-5 for C<=5.
    For efficiency on large-height generators, caller may reduce n_iter to 7 (error ~8e-5).

    Returns float.
    """
    if P is None:
        return 0.0

    Q = (Fraction(P[0]), Fraction(P[1]))
    coeff = (a1, a2, a3, a4, a6)

    for _ in range(n_iter):
        Q2 = point_add(*coeff, Q, Q)
        if Q2 is None:
            return 0.0
        Q = Q2

    return naive_height(Q[0]) / (4**n_iter)


def height_pairing(a1, a2, a3, a4, a6, P, Q_pt, n_iter=8):
    """Canonical height pairing <P,Q> = (h_hat(P+Q) - h_hat(P) - h_hat(Q)) / 2."""
    coeff = (a1, a2, a3, a4, a6)
    PQ = point_add(*coeff, P, Q_pt)
    hPQ = canonical_height(*coeff, PQ,  n_iter=n_iter)
    hP  = canonical_height(*coeff, P,   n_iter=n_iter)
    hQ  = canonical_height(*coeff, Q_pt, n_iter=n_iter)
    return (hPQ - hP - hQ) / 2


def pairing_matrix(a1, a2, a3, a4, a6, generators, n_iter=8):
    """Build the r x r canonical height pairing matrix for generators."""
    r = len(generators)
    coeff = (a1, a2, a3, a4, a6)
    M = [[0.0]*r for _ in range(r)]
    for i in range(r):
        M[i][i] = canonical_height(*coeff, generators[i], n_iter=n_iter)
        for j in range(i+1, r):
            pij = height_pairing(*coeff, generators[i], generators[j], n_iter=n_iter)
            M[i][j] = pij
            M[j][i] = pij
    return M


def is_positive_definite(M):
    """Check positive definiteness via Sylvester's criterion (leading minors > 0)."""
    import numpy as np
    A = np.array(M, dtype=float)
    n = len(M)
    for k in range(1, n+1):
        if np.linalg.det(A[:k, :k]) <= 0:
            return False
    return True


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------


def _selftest():
    """Validate canonical heights for 37a1, 389a1, 5077a1; build 234446a1 matrix."""
    # 37a1: y^2+y=x^3-x, gen (0,0), h_hat ~= 0.051114
    a37 = (0, 0, 1, -1, 0)
    h0 = canonical_height(*a37, (0, 0), n_iter=8)
    print(f"[2H] 37a1 h_hat(0,0)    = {h0:.7f}  (expected ~0.0511114)")
    assert abs(h0 - 0.05111) < 5e-4, f"37a1 h_hat mismatch: {h0}"

    # 389a1: y^2+y=x^3+x^2-2x, gens (-1,1) and (0,0)
    # Actual converged values (Cremona normalization h=log max(|a|,b)):
    a389 = (0, 1, 1, -2, 0)
    h_m1 = canonical_height(*a389, (-1, 1), n_iter=8)
    h_00 = canonical_height(*a389, (0, 0), n_iter=8)
    print(f"[2H] 389a1 h_hat(-1,1)  = {h_m1:.7f}  (converged ~0.6866670)")
    print(f"[2H] 389a1 h_hat(0,0)   = {h_00:.7f}  (converged ~0.3270008)")
    assert h_m1 > 0.5 and h_m1 < 1.0, f"389a1 h_hat(-1,1) out of range: {h_m1}"
    assert h_00 > 0.2 and h_00 < 0.5, f"389a1 h_hat(0,0) out of range: {h_00}"

    # 5077a1: y^2+y=x^3-7x+6, gens (-2,3),(-1,3),(0,2)
    # Actual converged values:
    a5077 = (0, 0, 1, -7, 6)
    h_g1 = canonical_height(*a5077, (-2, 3), n_iter=8)
    h_g2 = canonical_height(*a5077, (-1, 3), n_iter=8)
    h_g3 = canonical_height(*a5077, (0, 2), n_iter=8)
    print(f"[2H] 5077a1 h_hat(-2,3) = {h_g1:.7f}  (converged ~1.3685725)")
    print(f"[2H] 5077a1 h_hat(-1,3) = {h_g2:.7f}  (converged ~1.2050807)")
    print(f"[2H] 5077a1 h_hat(0,2)  = {h_g3:.7f}  (converged ~0.9909051)")

    # 234446a1 rank-4 pairing matrix (n_iter=6 for speed: error <= ~3e-4)
    print("[2H] Building 4x4 pairing matrix for 234446a1 (n_iter=6)...")
    a234 = (1, -1, 0, -79, 289)
    gens234 = [(6, -1), (4, 3), (5, -2), (8, 7)]
    M = pairing_matrix(*a234, gens234, n_iter=6)
    print("[2H] 234446a1 4x4 pairing matrix:")
    for row in M:
        print("  ", [f"{v:9.6f}" for v in row])
    pd = is_positive_definite(M)
    print(f"[2H] 234446a1 positive definite: {pd}")

    print("[2H] Self-test complete.")
    return M, pd


if __name__ == "__main__":
    _selftest()
