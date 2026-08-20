"""Checks for experiments._shared.certified_eig (the enclosure certifier).

Standalone module in the repo's test pattern (no pytest): run

    python -m experiments._shared.test_certified_eig

and expect the last line to read N/N passed. Covers: exact conversion
round-trips, containment on matrices with known spectra, an ill-conditioned
Hilbert pencil at high dps, the generalized problem against mpmath's eig on
B^{-1}A, honest widening on a near-degenerate pair, the precision ladder
detecting starvation and converging, and the fallback path refusing to claim
certification.
"""

from __future__ import annotations

import time

import mpmath as mp

from experiments._shared.certified_eig import (
    HAVE_FLINT, certify_smallest, precision_ladder, _mpf_to_arb,
    _exact_arb_to_mpf)

CHECKS: list[tuple[str, bool, str]] = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok), detail))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           (" : " + detail) if detail else ""))


def tridiag(n, d, o):
    M = mp.matrix(n, n)
    for i in range(n):
        M[i, i] = mp.mpf(d)
        if i + 1 < n:
            M[i, i + 1] = M[i + 1, i] = mp.mpf(o)
    return M


def hilbert(n, dps):
    with mp.workdps(dps):
        H = mp.matrix(n, n)
        for i in range(n):
            for j in range(n):
                H[i, j] = mp.mpf(1) / (i + j + 1)
    return H


def t_exact_conversion():
    mp.mp.dps = 50
    x = mp.mpf(1) / mp.mpf(3)
    a = _mpf_to_arb(x)
    check("mpf->arb->mpf roundtrip exact at dps 50",
          a.is_exact() and _exact_arb_to_mpf(a) == x)
    big = mp.make_mpf(mp.libmp.from_man_exp((1 << 300) + 7, -350))
    check("wide-mantissa roundtrip exact",
          _exact_arb_to_mpf(_mpf_to_arb(big)) == big)


def t_known_2x2():
    # spectrum of [[2,1],[1,3]] is (5 +/- sqrt 5)/2, exactly
    A = mp.matrix([[2, 1], [1, 3]])
    cert = certify_smallest(A, dps=50)
    with mp.workdps(80):
        truth = (5 - mp.sqrt(5)) / 2
    check("2x2 route is flint + certified",
          cert.route == "flint" and cert.certified)
    check("2x2 interval contains (5-sqrt5)/2",
          cert.lo <= truth <= cert.hi,
          "[%s, %s]" % (mp.nstr(cert.lo, 20), mp.nstr(cert.hi, 20)))
    check("2x2 radius below 1e-40", cert.radius < mp.mpf(10) ** -40,
          "radius %s" % mp.nstr(cert.radius, 3))


def t_known_tridiag():
    # tridiag(2,-1) of size n has eigenvalues 2 - 2 cos(k pi/(n+1)), exactly
    n = 8
    cert = certify_smallest(tridiag(n, 2, -1), dps=50)
    with mp.workdps(80):
        truth = 2 - 2 * mp.cos(mp.pi / (n + 1))
    check("tridiag8 interval contains 2 - 2cos(pi/9)",
          cert.certified and cert.lo <= truth <= cert.hi)
    check("tridiag8 gap and vector bounds present",
          cert.gap_lower is not None and cert.gap_lower > 0
          and cert.sin_theta_bound is not None
          and cert.sin_theta_bound < mp.mpf(10) ** -30,
          "gap_lo %s sin %s" % (mp.nstr(cert.gap_lower, 5),
                                mp.nstr(cert.sin_theta_bound, 3)))


def t_hilbert_ill_conditioned():
    # cond(H_10) ~ 1.6e13: the certificate must survive it at dps 60
    H = hilbert(10, 60)
    cert = certify_smallest(H, dps=60)
    with mp.workdps(140):
        E, _ = mp.eigsy(mp.matrix(H))
        truth = min(mp.re(E[i]) for i in range(10))
    check("hilbert10 certified containment at dps 60",
          cert.certified and cert.lo <= truth <= cert.hi,
          "truth %s in [%s, %s]" % (mp.nstr(truth, 10),
                                    mp.nstr(cert.lo, 10),
                                    mp.nstr(cert.hi, 10)))
    check("hilbert10 radius below 1e-30", cert.radius < mp.mpf(10) ** -30,
          "radius %s" % mp.nstr(cert.radius, 3))


def t_generalized():
    # pencil A v = lambda B v with B = H_5 + I (SPD), checked against
    # mpmath's unsymmetric eig on B^{-1} A
    n = 5
    A = tridiag(n, 2, -1)
    B = hilbert(n, 60)
    for i in range(n):
        B[i, i] = B[i, i] + 1
    cert = certify_smallest(A, B, dps=60)
    with mp.workdps(90):
        Ev, _ = mp.eig(mp.inverse(mp.matrix(B)) * mp.matrix(A))
        truth = min(mp.re(e) for e in Ev)
    slack = mp.mpf(10) ** -40  # absorbs mpmath eig's own (unverified) error
    check("generalized certified with SPD proof",
          cert.certified and cert.spd_certified is True)
    check("generalized interval matches mpmath eig on B^-1 A",
          cert.lo - slack <= truth <= cert.hi + slack,
          "truth %s in [%s, %s]" % (mp.nstr(truth, 10),
                                    mp.nstr(cert.lo, 10),
                                    mp.nstr(cert.hi, 10)))
    check("generalized residual certificate is tight",
          cert.residual_bound is not None
          and cert.residual_bound < mp.mpf(10) ** -40,
          "residual %s" % mp.nstr(cert.residual_bound, 3))
    with mp.workdps(90):
        nb = mp.re((cert.vec.T * (mp.matrix(B) * cert.vec))[0])
    check("generalized eigenvector is B-normalized",
          abs(nb - 1) < mp.mpf(10) ** -50, "|v^T B v - 1| = %s"
          % mp.nstr(abs(nb - 1), 3))


def t_near_degenerate():
    # eigenvalues 1 and 1 + 2^-500, but ROTATED dense (a diagonal matrix
    # certifies exactly at any precision, which tests nothing): at dps 20 no
    # honest solver can split these, and the enclosure must widen PAST the
    # separation, not lie
    with mp.workdps(600):
        eps = mp.mpf(2) ** -500
        c, s = mp.cos(1), mp.sin(1)
        A = mp.matrix(2, 2)
        A[0, 0] = c * c + s * s * (1 + eps)
        A[1, 1] = s * s + c * c * (1 + eps)
        A[0, 1] = A[1, 0] = -c * s * eps
    sep = mp.mpf(2) ** -500
    lowc = certify_smallest(A, dps=20)
    check("near-degenerate at dps 20: containment kept",
          lowc.certified and lowc.lo <= 1 <= lowc.hi)
    check("near-degenerate at dps 20: honestly wide (radius > separation, "
          "cluster mode, no gap)",
          (not lowc.isolated) and lowc.radius > sep
          and lowc.gap_lower is None,
          "radius %s" % mp.nstr(lowc.radius, 3))
    check("near-degenerate at dps 20: starvation named in notes",
          any("starvation" in s for s in lowc.notes))
    highc = certify_smallest(A, dps=200)
    check("near-degenerate at dps 200: isolated with certified gap ~ 2^-500",
          highc.certified and highc.isolated and highc.gap_lower is not None
          and 0 < highc.gap_lower < mp.mpf(2) ** -499
          and highc.radius < mp.mpf(2) ** -600,
          "gap_lo %s radius %s" % (mp.nstr(highc.gap_lower, 3),
                                   mp.nstr(highc.radius, 3)))


def t_ladder():
    builder = lambda dps: hilbert(8, dps)
    tol = mp.mpf(10) ** -50  # reachable at dps 60, not at 30: forces 3 rungs
    lad = precision_ladder(builder, [10, 30, 60], tol)
    radii = [s["radius"] for s in lad.steps]
    check("ladder converges by dps 60",
          lad.converged and not lad.starved and lad.steps[-1]["dps"] == 60,
          "radii " + ", ".join(mp.nstr(r, 3) for r in radii))
    check("ladder radius shrinks along the schedule",
          all(radii[i + 1] < radii[i] for i in range(len(radii) - 1)))
    check("ladder final certificate certified below tol",
          lad.final.certified and lad.final.radius < tol)
    starved = precision_ladder(builder, [8, 10], mp.mpf(10) ** -35)
    check("ladder flags starvation on a too-short schedule",
          starved.starved and not starved.converged,
          "final radius %s vs tol %s" % (mp.nstr(starved.final.radius, 3),
                                         mp.nstr(tol, 3)))


def t_fallback():
    A = mp.matrix([[2, 1], [1, 3]])
    cert = certify_smallest(A, dps=40, use_flint=False)
    with mp.workdps(80):
        truth = (5 - mp.sqrt(5)) / 2
    check("fallback path reports certified=False",
          cert.certified is False and cert.route == "mpmath-fallback")
    check("fallback path labels itself non-rigorous",
          any("not directed-rounding rigorous" in s for s in cert.notes))
    check("fallback interval still contains truth",
          cert.lo <= truth <= cert.hi,
          "[%s, %s]" % (mp.nstr(cert.lo, 12), mp.nstr(cert.hi, 12)))


def main():
    t0 = time.time()
    print("certified_eig checks (flint available: %s)" % HAVE_FLINT)
    check("python-flint importable in this venv", HAVE_FLINT)
    t_exact_conversion()
    t_known_2x2()
    t_known_tridiag()
    t_hilbert_ill_conditioned()
    t_generalized()
    t_near_degenerate()
    t_ladder()
    t_fallback()
    npass = sum(1 for _, ok, _ in CHECKS if ok)
    print("elapsed: %.1fs" % (time.time() - t0))
    print("%d/%d passed" % (npass, len(CHECKS)))
    return npass == len(CHECKS)


if __name__ == "__main__":
    raise SystemExit(0 if main() else 1)
