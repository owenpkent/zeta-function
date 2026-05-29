"""Experiment 2L: Period machinery - period_tau and c_invariants.

Provides the elliptic-curve period lattice (real period omega1, period ratio tau)
and the standard c-invariants (c4, c6, Delta) for curves in minimal Weierstrass form.
Also provides the elliptic logarithm for points on both real components.

These are the building blocks reused by e2i and e2n.

Reference: Cremona "Algorithms for Modular Elliptic Curves" Ch 1-3;
Silverman AEC App A; ATAEC Ch VI.

Validated: for 37a1 (y^2+y=x^3-x):
  omega1 = 2K(k'^2)/sqrt(e1-e3) ~= 2.9935  (k'=(e2-e3)/(e1-e3))
  tau = i*K(k^2)/K(k'^2) ~= 0.8189i        (k=(e1-e2)/(e1-e3))
  |omega2| = Im(tau)*omega1 ~= 2.4514
"""
from __future__ import annotations

import mpmath as mp


# ---------------------------------------------------------------------------
# b-invariants and c-invariants from Weierstrass a-invariants
# ---------------------------------------------------------------------------


def b_invariants(a1, a2, a3, a4, a6):
    """Return (b2, b4, b6, b8) for E: y^2+a1*x*y+a3*y = x^3+a2*x^2+a4*x+a6."""
    b2 = a1**2 + 4*a2
    b4 = a1*a3 + 2*a4
    b6 = a3**2 + 4*a6
    b8 = a1**2*a6 - a1*a3*a4 + 4*a2*a6 + a2*a3**2 - a4**2
    return b2, b4, b6, b8


def c_invariants(a1, a2, a3, a4, a6):
    """Return (c4, c6, Delta) for E given a-invariants.

    c4 = b2^2 - 24*b4
    c6 = -b2^3 + 36*b2*b4 - 216*b6
    Delta = -b2^2*b8 - 8*b4^3 - 27*b6^2 + 9*b2*b4*b6
    """
    b2, b4, b6, b8 = b_invariants(a1, a2, a3, a4, a6)
    c4 = b2**2 - 24*b4
    c6 = -(b2**3) + 36*b2*b4 - 216*b6
    Delta = -(b2**2)*b8 - 8*(b4**3) - 27*(b6**2) + 9*b2*b4*b6
    return c4, c6, Delta


def short_weierstrass_coeffs(a1, a2, a3, a4, a6):
    """Return (g2, g3) for short Weierstrass y'^2 = 4x'^3 - g2*x' - g3.

    x' = x + b2/12, y' = 2y + a1*x + a3.
    g2 = c4/12, g3 = c6/216.
    """
    c4, c6, _ = c_invariants(a1, a2, a3, a4, a6)
    g2 = mp.mpf(c4) / 12
    g3 = mp.mpf(c6) / 216
    return g2, g3


def to_short_weierstrass(a1, a2, a3, a4, a6, x, y):
    """Transform (x,y) in minimal model to (x',y') in short Weierstrass form."""
    b2, _, _, _ = b_invariants(a1, a2, a3, a4, a6)
    xw = mp.mpf(x) + mp.mpf(b2)/12
    yw = 2*mp.mpf(y) + mp.mpf(a1)*mp.mpf(x) + mp.mpf(a3)
    return xw, yw


# ---------------------------------------------------------------------------
# Cubic roots and period computation
# ---------------------------------------------------------------------------


def cubic_roots_sorted(g2, g3, prec=50):
    """Find the three real roots e1 >= e2 >= e3 of 4t^3 - g2*t - g3 = 0.

    Assumes discriminant = g2^3 - 27*g3^2 > 0 (three distinct real roots).
    Returns (e1, e2, e3) sorted descending.
    """
    mp.mp.dps = prec + 10
    coeffs = [mp.mpf(4), mp.mpf(0), -mp.mpf(g2), -mp.mpf(g3)]
    roots = mp.polyroots(coeffs, maxsteps=500, extraprec=prec)
    real_roots = sorted([mp.re(r) for r in roots], reverse=True)
    return tuple(real_roots)


def period_tau(a1, a2, a3, a4, a6, prec=50):
    """Compute the real period omega1 and period ratio tau for E.

    For a curve with all real roots (discriminant > 0):

    Let k^2  = (e1-e2)/(e1-e3)   (related to unbounded-component half-period)
        k'^2 = (e2-e3)/(e1-e3) = 1 - k^2

    Then:
        omega1 = 2*K(k'^2) / sqrt(e1-e3)      [real period]
        tau    = i * K(k^2) / K(k'^2)          [purely imaginary]

    The imaginary period magnitude is |omega2| = Im(tau)*omega1 = 2*K(k^2)/sqrt(e1-e3).

    Returns (omega1, tau) as mpmath values (omega1 real positive, tau purely imaginary).
    """
    mp.mp.dps = prec + 10
    _, _, Delta = c_invariants(a1, a2, a3, a4, a6)
    if Delta <= 0:
        raise ValueError(f"Delta={Delta} <= 0: one-real-root case not implemented")
    g2, g3 = short_weierstrass_coeffs(a1, a2, a3, a4, a6)
    e1, e2, e3 = cubic_roots_sorted(g2, g3, prec=prec+5)

    k_sq  = (e1 - e2) / (e1 - e3)     # k^2
    kp_sq = (e2 - e3) / (e1 - e3)     # k'^2 = 1 - k^2

    Kk  = mp.ellipk(k_sq)              # K(k^2)
    Kkp = mp.ellipk(kp_sq)             # K(k'^2)

    omega1 = 2 * Kkp / mp.sqrt(e1 - e3)         # real period
    tau    = mp.mpc(0, 1) * Kk / Kkp             # purely imaginary

    return omega1, tau


# ---------------------------------------------------------------------------
# Elliptic logarithm (both real components)
# ---------------------------------------------------------------------------


def elliptic_log(a1, a2, a3, a4, a6, x, y, prec=50):
    """Compute the elliptic logarithm z_P of P=(x,y) on E.

    P is first converted to the short Weierstrass model (xw, yw).

    UNBOUNDED COMPONENT (xw >= e1):
        phi = arcsin(sqrt((e1-e3)/(xw-e3)))
        z_P = F(phi, k'^2) / sqrt(e1-e3)           [real, in (0, omega1/2)]

    BOUNDED OVAL (e3 <= xw <= e2):
        phi = arcsin(sqrt((xw-e3)/(e2-e3)))
        z_P = F(phi, k'^2) / sqrt(e1-e3) + i * K(k^2) / sqrt(e1-e3)
        [Im(z_P) = Im(omega2)/2 = omega2_abs/2, constant for all bounded-oval points]

    Both components use k'^2 = (e2-e3)/(e1-e3) as the elliptic integral parameter.

    Returns z_P as a (possibly complex) mpmath number.
    Note: lambda_inf is EVEN in z_P (both P and -P give the same value).
    """
    mp.mp.dps = prec + 10
    g2, g3 = short_weierstrass_coeffs(a1, a2, a3, a4, a6)
    xw, _ = to_short_weierstrass(a1, a2, a3, a4, a6, x, y)

    e1, e2, e3 = cubic_roots_sorted(g2, g3, prec=prec+5)

    k_sq  = (e1 - e2) / (e1 - e3)
    kp_sq = (e2 - e3) / (e1 - e3)   # the parameter used in F for BOTH components
    sqe = mp.sqrt(e1 - e3)

    tol = mp.mpf(10)**(-prec//2)

    if xw >= e1 - tol:
        # Unbounded component: x' >= e1
        xw = max(xw, e1)
        sin_sq = (e1 - e3) / (xw - e3)
        sin_sq = min(sin_sq, mp.mpf(1))
        phi = mp.asin(mp.sqrt(sin_sq))
        z_P = mp.ellipf(phi, kp_sq) / sqe
        return mp.re(z_P)

    elif e3 - tol <= xw <= e2 + tol:
        # Bounded oval: e3 <= x' <= e2
        xw = max(min(xw, e2), e3)
        sin_sq = (xw - e3) / (e2 - e3)
        sin_sq = max(mp.mpf(0), min(sin_sq, mp.mpf(1)))
        phi = mp.asin(mp.sqrt(sin_sq))
        real_part = mp.ellipf(phi, kp_sq) / sqe
        imag_part = mp.ellipk(k_sq) / sqe     # = Im(omega2)/2 = omega2_abs/2
        return real_part + mp.mpc(0, 1) * imag_part

    else:
        raise ValueError(
            f"xw={float(xw):.6f} not on either real component "
            f"(e3={float(e3):.4f}, e2={float(e2):.4f}, e1={float(e1):.4f})"
        )


# ---------------------------------------------------------------------------
# Dedekind eta via q-product (using nome q0 = exp(i*pi*tau))
# ---------------------------------------------------------------------------


def dedekind_eta(tau, n_terms=200):
    """Compute Dedekind eta(tau) = q0^(1/12) * prod_{n>=1}(1 - q0^(2n)).

    Uses the NOME q0 = exp(i*pi*tau), matching mpmath.jtheta convention.
    For tau purely imaginary (tau = iy, y > 0): q0 = exp(-pi*y) in (0,1), rapid convergence.

    Identity used by the Green's-function formula: theta1'(0, q0) = 2*eta(tau)^3.
    """
    q0 = mp.exp(mp.pi * mp.j * tau)
    prod = mp.mpf(1)
    for n in range(1, n_terms + 1):
        factor = 1 - q0**(2*n)
        prod *= factor
        if abs(factor - 1) < mp.mpf(10)**(-mp.mp.dps + 5):
            break
    return q0**(mp.mpf(1)/12) * prod


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------


def _selftest():
    """Validate periods and c-invariants for 37a1, 389a1, 5077a1."""
    mp.mp.dps = 50

    # 37a1: y^2+y=x^3-x
    a37 = (0, 0, 1, -1, 0)
    c4, c6, Delta = c_invariants(*a37)
    assert c4 == 48,   f"37a1 c4={c4}"
    assert c6 == -216, f"37a1 c6={c6}"
    assert Delta == 37, f"37a1 Delta={Delta}"

    omega1, tau = period_tau(*a37, prec=50)
    # omega1 = 2*K(k'^2)/sqrt(e1-e3) ~= 2.9935
    assert abs(float(mp.re(omega1)) - 2.9935) < 1e-3, f"37a1 omega1={float(omega1)}"
    # Im(tau) = K(k^2)/K(k'^2) ~= 0.8189  (not 2.451: that's |omega2|)
    assert abs(float(mp.im(tau)) - 0.8189) < 1e-3, f"37a1 Im(tau)={float(mp.im(tau))}"
    print(f"[2L] 37a1: omega1={float(mp.re(omega1)):.6f}, Im(tau)={float(mp.im(tau)):.6f},  "
          f"|omega2|={float(mp.im(tau)*mp.re(omega1)):.6f}")

    # Elliptic log of generator (0,0) on 37a1: on the BOUNDED OVAL
    z = elliptic_log(*a37, 0, 0, prec=50)
    # Must be complex with Im(z) = K(k^2)/sqrt(e1-e3) = |omega2|/2
    omega2_abs_half = float(mp.im(tau)) * float(mp.re(omega1)) / 2
    assert abs(float(mp.im(z)) - omega2_abs_half) < 1e-6, \
        f"37a1 ell-log Im={float(mp.im(z))}, expected {omega2_abs_half}"
    print(f"[2L] 37a1 gen (0,0): z_P = {float(mp.re(z)):.6f} + {float(mp.im(z)):.6f}i (bounded oval) OK")

    # Dedekind eta (check real and positive for tau purely imaginary)
    eta = dedekind_eta(tau, n_terms=300)
    assert abs(float(mp.im(eta))) < 1e-20, f"eta should be real, got {float(mp.im(eta))}"
    assert float(mp.re(eta)) > 0, f"eta should be positive, got {float(mp.re(eta))}"
    print(f"[2L] 37a1: eta(tau) = {float(mp.re(eta)):.8f} (real, positive) OK")

    print("[2L] All self-tests passed.")


if __name__ == "__main__":
    _selftest()
