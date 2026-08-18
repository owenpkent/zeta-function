"""Vectorized Riemann-Siegel Z, and a bulk zero finder built on it.

The repo's standard zero source (experiments/_shared/zeta.py) calls
mp.zetazero(k) one zero at a time: correct, arbitrary precision, and about
0.9 s per zero at index 5000, so tens of thousands of zeros are out of
reach. Zero STATISTICS need tens of thousands. This module supplies them.

Z(t) is the Hardy function: real for real t, with |Z(t)| = |zeta(1/2+it)|,
so the zeros of zeta on the critical line are exactly the real zeros of Z,
locatable by sign changes. The Riemann-Siegel formula computes it in
O(sqrt(t)) terms:

    Z(t) = 2 sum_{n=1}^{nu} n^{-1/2} cos(theta(t) - t log n) + R(t),
    nu = floor(sqrt(t/2pi)),  R(t) = (-1)^(nu-1) (t/2pi)^(-1/4) C0(p) + ...

with theta the Riemann-Siegel phase and p the fractional part of
sqrt(t/2pi). Keeping only C0 leaves an error O(t^(-3/4)), which at t = 10^6
is about 3e-5 of a zero spacing of 0.5: ample for locating zeros, and the
accuracy is checked directly against Odlyzko's published table.

Everything is float64 and vectorized over the t-grid, so a window holding
tens of thousands of zeros takes seconds. Completeness is verifiable rather
than assumed: the number of sign changes found in [T1, T2] is compared with
the Riemann-von Mangoldt count (theta(T2) - theta(T1))/pi.

PRECISION (added 2026-08-16, the lever for pushing certified verification
past height 1e7). The Riemann-Siegel phase phi_n = theta(t) - t log n has
magnitude ~t log t, so representing it in float64 costs an absolute angle
error ~t log t * 2^-53, and cosine is 1-Lipschitz: that error passes straight
into Z. It grows like t^1.25 log t while the C_0-truncation error falls like
t^-0.75, so the two cross near t = 3e6 and by t = 1e8 the certified bound is
rounding-dominated by a factor of 1400. Passing `prec="ld"` computes the
phase (and its reduction mod 2 pi) in x86 80-bit extended precision, whose
unit roundoff 2^-64 is 2048x smaller, and only then drops to float64 for the
cosine. The certified bound at t = 1e8 falls from 1.8e-4 to 8.8e-8, which
puts it back below the C_0 truncation bound. Nothing else changes: the
float64 path is untouched and remains the default, so every previously
recorded number reproduces bit-for-bit.
"""
from __future__ import annotations

import numpy as np
from numpy.polynomial.chebyshev import chebval

TWO_PI = 2.0 * np.pi

# 80-bit extended precision is an x86 feature. On platforms where numpy's
# longdouble is just float64 (Windows MSVC, and ARM where it is float128 or
# float64) the extended path must not silently claim a bound it cannot honour.
LD_MANT = int(np.finfo(np.longdouble).nmant)
HAS_LD = LD_MANT > 53
PI_LD = np.longdouble("3.14159265358979323846264338327950288419716939937510")
TWO_PI_LD = 2 * PI_LD
_U_LD = 2.0 ** -(LD_MANT + 1) if HAS_LD else 2.0 ** -53

# Cap on the (t x n) phase matrix, so a wide t-window at large height chunks
# itself down instead of allocating tens of gigabytes. Chunking cannot change
# any result: the inner sum runs over n independently for each t.
_PHASE_BYTES = 256 << 20


# --------------------------------------------------------------------------
# Riemann-Siegel correction coefficients C_0 and C_1.
#
# With z = 2p - 1, p = frac(sqrt(t/2pi)), the classical form (Edwards,
# *Riemann's Zeta Function*, 7.4) is
#     Psi(z) = cos(pi(z^2/2 + 3/8)) / cos(pi z) = C_0(z),
#     C_1(z) = -Psi'''(z) / (12 pi^2),
# where the textbook constant is 2^5*3*pi^2 for the variable u = p - 1/2 and
# ours is eight times smaller because z = 2u, so d^3/du^3 = 8 d^3/dz^3. That
# factor was caught by measurement, not by reading: the residual left after
# the C_0 term, rescaled by a^(3/2), came out exactly 8.0000x the 96 pi^2
# version across the whole range of z (median 7.99912 over 800 samples).
#     Z = 2 sum + (-1)^(nu-1) a^(-1/2) [C_0 + C_1/a + ...],  a = sqrt(t/2pi),
# and the C_0 written that way is exactly the quotient the k=0 path uses
# (checked: they agree to 4.7e-14 across p in (0,1)).
#
# Psi is entire -- the zeros of cos(pi z) at z = +-1/2 are removable -- but
# the quotient evaluates 0/0 there and loses digits nearby (measured: 3e-8 of
# absolute error at p = 1/4 + 1e-9). Both coefficients are therefore carried
# as degree-26 Chebyshev fits on [-1, 1], which are stable everywhere and
# vectorize. Psi is even so C_1 is odd, which is visible in the coefficients
# (the vanishing alternate entries) and is checked by the test suite.
#
# The constants below are not magic: _regen_correction_coeffs() rebuilds them
# from the definitions at 80-digit precision, and test_primes.py calls it and
# compares. Regenerated accuracy on 997 points off the fit nodes: 6.1e-16 for
# C_0, 5.2e-18 for C_1.
_C0_CHEB = np.array([
    6.4266728623976854e-01, 5.1028004907222687e-17, 2.7197299999785501e-01,
    -5.8493057696110667e-17, 1.0738605819340339e-02, 7.4666367091895151e-17,
    -1.3743815296336560e-03, -1.5555314837244396e-17, -1.2468221880322983e-04,
    -2.1270639485435896e-17, -5.7645997067549433e-07, -6.4823584229381263e-17,
    2.7280674304606738e-07, -4.2923615438065997e-17, 8.0779531217569275e-09,
    -4.2989485975810010e-17, -2.0884608467137706e-10, -7.6542007360834068e-17,
    -1.3115567166826439e-11, 2.9193906653651459e-17, -1.4222584406208316e-14,
    -3.7780349787078361e-17, 1.0271348603151929e-14, -2.4134038378596327e-17,
    1.6191578480176443e-16, -4.7102773760513294e-17, -5.5934543840609536e-17])
_C1_CHEB = np.array([
    -3.4694469519538493e-19, 1.0697913921003001e-02, -1.4998321217407235e-18,
    1.7170651243377893e-02, -6.7100682103325962e-18, 2.7932111497884723e-03,
    5.4316636161314684e-19, -3.6375653719275581e-05, 2.5057819349678655e-18,
    -2.7108955231154178e-05, -5.0206500253719017e-18, -1.0483749866729966e-06,
    -1.7670411378696167e-18, 5.8864671663355178e-08, 3.8111200547243348e-18,
    4.3229672631153196e-09, 1.2936226392339328e-18, -1.1369592950920907e-11,
    3.9252311467094391e-18, -6.6998265975682976e-12, 3.9252311467094399e-18,
    -1.0079944519360509e-13, -2.9439233600320805e-18, 5.1478639842385970e-15,
    9.8130778667736017e-19, 1.4713483626493671e-16, 1.4719616800160405e-18])
_C0_FIT_ERR = 1e-15      # generous cover for the fit plus its evaluation
_C1_FIT_ERR = 1e-16


def _regen_correction_coeffs(deg: int = 26, nodes: int = 400, dps: int = 80):
    """Rebuild (_C0_CHEB, _C1_CHEB) from the definitions. Audit hook.

    Slow (mpmath third derivatives at `dps` digits), so it is never called at
    import; the test suite calls it and compares against the constants above.
    """
    import mpmath as _mp
    prev = _mp.mp.dps
    _mp.mp.dps = dps
    try:
        def psi(z):
            z = _mp.mpf(z)
            den = _mp.cos(_mp.pi * z)
            if abs(den) > _mp.mpf(10) ** (-20):
                return _mp.cos(_mp.pi * (z * z / 2 + _mp.mpf(3) / 8)) / den
            # removable zero at z = +-1/2: w = z -+ 1/2 gives
            # Psi = sin(pi w (w+1)/2) / sin(pi w)
            w = z - _mp.sign(z) / 2
            return _mp.sin(_mp.pi * w * (w + 1) / 2) / _mp.sin(_mp.pi * w)

        x = np.cos(np.pi * (np.arange(nodes) + 0.5) / nodes)
        y0 = np.array([float(psi(v)) for v in x])
        y1 = np.array([float(-_mp.diff(psi, _mp.mpf(v), 3) / (12 * _mp.pi**2))
                       for v in x])
    finally:
        _mp.mp.dps = prev
    return (np.polynomial.chebyshev.chebfit(x, y0, deg),
            np.polynomial.chebyshev.chebfit(x, y1, deg))


def best_prec() -> str:
    """The most accurate phase precision this machine actually supports."""
    return "ld" if HAS_LD else "f8"


def _require(prec: str) -> str:
    if prec not in ("f8", "ld"):
        raise ValueError(f"prec must be 'f8' or 'ld', got {prec!r}")
    if prec == "ld" and not HAS_LD:
        raise RuntimeError(
            "prec='ld' needs an extended-precision longdouble; this platform's "
            f"longdouble has a {LD_MANT}-bit mantissa (float64 is 52). Use "
            "prec='f8', or best_prec() to pick automatically.")
    return prec


def theta(t: np.ndarray | float, prec: str = "f8") -> np.ndarray:
    """Riemann-Siegel phase, asymptotic series (error ~1e-9 for t > 50)."""
    if _require(prec) == "ld":
        t = np.asarray(t, dtype=np.longdouble)
        half = np.longdouble(0.5)
        return (half * t * np.log(t / TWO_PI_LD) - half * t - PI_LD / 8
                + 1 / (48 * t) + 7 / (5760 * t**3))
    t = np.asarray(t, dtype=np.float64)
    return (0.5 * t * np.log(t / TWO_PI) - 0.5 * t - np.pi / 8
            + 1.0 / (48.0 * t) + 7.0 / (5760.0 * t**3))


def n_count(t: np.ndarray | float) -> np.ndarray:
    """Smooth zero-counting function N(t) = theta(t)/pi + 1 (drops S(t))."""
    return theta(t) / np.pi + 1.0


def zed(t: np.ndarray, chunk: int = 20000, prec: str = "f8",
        k: int = 0) -> np.ndarray:
    """Riemann-Siegel Z(t), vectorized, main sum plus the C_0..C_k remainder.

    `prec="ld"` forms the phase and its reduction mod 2 pi in extended
    precision before dropping to float64 for the cosine (see the module
    docstring); `prec="f8"` is the original float64 path, bit-for-bit.

    `k=1` adds the C_1 correction, dropping the truncation bound from
    0.127 t^-3/4 to 0.053 t^-5/4. It also switches the remainder to the
    Chebyshev evaluation, which is stable at the removable zeros of
    cos(2 pi p) where the quotient form loses digits; `k=0` keeps the
    quotient verbatim so old results reproduce exactly.
    """
    _require(prec)
    if k not in (0, 1):
        raise ValueError(f"k must be 0 or 1 (C_2 and beyond are not implemented), got {k}")
    t = np.asarray(t, dtype=np.float64)
    out = np.empty(t.size)
    # Chunk down if the phase matrix would not fit the memory budget.
    nmax_all = max(1, int(np.floor(np.sqrt(t.max() / TWO_PI))))
    itemsize = np.dtype(np.longdouble).itemsize if prec == "ld" else 8
    chunk = max(1, min(chunk, _PHASE_BYTES // (nmax_all * itemsize)))
    for i in range(0, t.size, chunk):
        tc = t[i : i + chunk]
        a = np.sqrt(tc / TWO_PI)
        nu = np.floor(a).astype(np.int64)
        nmax = int(nu.max())
        n = np.arange(1, nmax + 1, dtype=np.float64)
        if prec == "ld":
            tl = tc.astype(np.longdouble)
            nl = np.arange(1, nmax + 1, dtype=np.longdouble)
            # theta - t log n, then reduce mod 2 pi while still extended: the
            # surviving angle error is ~|phase| * 2^-64, not ~|phase| * 2^-53.
            phase = theta(tl, "ld")[:, None] - tl[:, None] * np.log(nl)[None, :]
            phase -= np.rint(phase / TWO_PI_LD) * TWO_PI_LD
            phase = phase.astype(np.float64)
        else:
            # cos(theta - t log n) / sqrt(n), zeroing terms beyond nu(t)
            phase = theta(tc)[:, None] - np.outer(tc, np.log(n))
        terms = np.cos(phase) / np.sqrt(n)
        terms[n[None, :] > nu[:, None]] = 0.0
        main = 2.0 * terms.sum(axis=1)
        p = a - nu
        sgn = np.where(nu % 2 == 0, -1.0, 1.0)          # (-1)^(nu-1)
        if k == 0:
            # The original quotient form, kept verbatim so prec="f8", k=0 is
            # bit-for-bit what every earlier run produced.
            c0 = np.cos(TWO_PI * (p * p - p - 0.0625)) / np.cos(TWO_PI * p)
            rem = c0
        else:
            z = 2.0 * p - 1.0
            rem = chebval(z, _C0_CHEB) + chebval(z, _C1_CHEB) / a
        out[i : i + chunk] = main + sgn * a**-0.5 * rem
    return out


# Gabcke (1979), "Neue Herleitung und explizite Restabschaetzung der
# Riemann-Siegel-Formel": with correction terms through C_K retained, the
# Riemann-Siegel remainder obeys |R_K(t)| < c_K * t^-(2K+3)/4 for all t >= 200.
# Odlyzko calls these essentially optimal for K <= 4. We keep C_0 only, so K = 0.
GABCKE = {0: (0.127, 0.75), 1: (0.053, 1.25), 2: (0.011, 1.75),
          3: (0.031, 2.25), 4: (0.017, 2.75)}
GABCKE_MIN_T = 200.0
_U = 2.0 ** -53          # float64 unit roundoff


def rs_truncation_bound(t: np.ndarray | float, k: int = 0) -> np.ndarray:
    """Rigorous bound on the discarded Riemann-Siegel tail (Gabcke), t >= 200."""
    c, e = GABCKE[k]
    return c * np.asarray(t, dtype=np.float64) ** (-e)


def rs_rounding_bound(t: np.ndarray | float, prec: str = "f8",
                      k: int = 0) -> np.ndarray:
    """Bound on the evaluation error of the Riemann-Siegel main sum.

    The phase phi_n = theta(t) - t log n is formed from quantities of size
    ~t log t, so its absolute error is ~(|theta| + t log nu) * u. Cosine is
    1-Lipschitz, so that error passes straight into each term; the weights
    n^-1/2 sum to at most 2 sqrt(nu), and the leading factor is 2. A final
    2 nu u covers the summation itself. Deliberately generous: over-estimating
    only costs a few escalations to exact arithmetic.

    With `prec="ld"` the phase carries the extended-precision unit roundoff
    2^-64 while the cosine and the summation keep the float64 one, since that
    is where zed() drops back down.
    """
    u_phase = _U_LD if _require(prec) == "ld" else _U
    t = np.asarray(t, dtype=np.float64)
    a = np.sqrt(t / TWO_PI)
    nu = np.floor(a)
    phase_mag = np.abs(theta(t)) + t * np.log(np.maximum(nu, 2.0))
    dphase = 4.0 * u_phase * phase_mag
    main = 4.0 * np.sqrt(nu) * (dphase + _U) + 2.0 * nu * _U

    # Evaluating the C_k remainder is not free either, and the k=0 quotient
    # form is the sharp part: cos(2 pi p) vanishes at p = 1/4 and 3/4, where
    # the numerator vanishes too, so the value is finite but computed 0/0 and
    # the relative error is amplified by 1/|cos(2 pi p)|. Bounded pointwise
    # here rather than ignored, which is what forces those (very rare) points
    # to escalate to exact arithmetic instead of being trusted. The k=1 path
    # evaluates Chebyshev fits, which have no such amplification.
    p = a - nu
    if k == 0:
        rem = 6.0 * _U / np.maximum(np.abs(np.cos(TWO_PI * p)), _U)
    else:
        rem = _C0_FIT_ERR + _C1_FIT_ERR / a + 8.0 * _U
    return main + rem / np.sqrt(a)


def rs_error_bound(t: np.ndarray | float, k: int = 0,
                   prec: str = "f8") -> np.ndarray:
    """Total rigorous error bound on zed(t): truncation plus rounding."""
    return rs_truncation_bound(t, k) + rs_rounding_bound(t, prec, k)


def rounding_crossover(k: int = 0, prec: str = "f8",
                       lo: float = 1e3, hi: float = 1e18) -> float:
    """Height where the rounding bound overtakes the C_k truncation bound.

    Below it the formula's own truncation is what limits a certified sign;
    above it the arithmetic is, and that is the wall `prec="ld"` moves.
    """
    _require(prec)
    for _ in range(200):
        mid = np.sqrt(lo * hi)
        if float(rs_rounding_bound(mid, prec, k)) < float(rs_truncation_bound(mid, k)):
            lo = mid
        else:
            hi = mid
    return float(np.sqrt(lo * hi))


def certified_sign(t: np.ndarray, z: np.ndarray | None = None,
                   dps: int = 30, prec: str = "f8",
                   k: int = 0) -> tuple[np.ndarray, int]:
    """Signs of Z(t) that are provably correct.

    Returns (signs, n_escalated). A float64 sign is accepted when |Z| exceeds
    the rigorous error bound; otherwise the point is recomputed with mpmath at
    `dps` digits, whose own error is far below any bound in play here. Raises
    if a point is genuinely too close to call, which would mean a zero sits on
    a sample point to 30 digits.
    """
    import mpmath as mp

    _require(prec)
    t = np.asarray(t, dtype=np.float64)
    if z is None:
        z = zed(t, prec=prec, k=k)
    eps = rs_error_bound(np.maximum(t, GABCKE_MIN_T), k=k, prec=prec)
    # Gabcke's bound starts at t = 200, so anything below it is never accepted
    # on the float64 value alone and always goes to exact arithmetic.
    unsafe = np.flatnonzero((np.abs(z) <= eps) | (t < GABCKE_MIN_T))
    signs = np.signbit(z)
    if unsafe.size:
        prev = mp.mp.dps
        mp.mp.dps = dps
        try:
            for i in unsafe:
                val = mp.siegelz(mp.mpf(float(t[i])))
                if abs(val) < mp.mpf(10) ** (-(dps - 6)):
                    raise RuntimeError(f"Z({t[i]!r}) is zero to {dps} digits; "
                                       "sample point sits on a zero")
                signs[i] = bool(val < 0)
        finally:
            mp.mp.dps = prev
    return signs, int(unsafe.size)


def _lambert_w(y: np.ndarray, iters: int = 40) -> np.ndarray:
    """Principal branch W(y) for y > 0, by Newton. Used only to seed gram_point."""
    y = np.asarray(y, dtype=np.float64)
    w = np.where(y > np.e, np.log(np.maximum(y, 1.1)) - np.log(np.log(np.maximum(y, 1.1))),
                 y / (1.0 + y))
    for _ in range(iters):
        ew = np.exp(w)
        w = w - (w * ew - y) / (ew * (w + 1.0))
    return w


def gram_point(n: np.ndarray | int, iters: int = 8) -> np.ndarray:
    """The Gram point g_n, i.e. the solution of theta(g) = n*pi, for n >= 0.

    Writing u = t/(2pi), theta(t) = pi*u*(log u - 1) - pi/8, so theta = n*pi
    reduces to u(log u - 1) = n + 1/8, whose solution is u = c/W(c/e) with
    c = n + 1/8. That seed is then polished by Newton on theta itself
    (theta'(t) = log(t/2pi)/2), which converges to machine precision.
    """
    n = np.asarray(n, dtype=np.float64)
    c = n + 0.125
    t = TWO_PI * c / _lambert_w(c / np.e)
    for _ in range(iters):
        t = t - (theta(t) - n * np.pi) / (0.5 * np.log(t / TWO_PI))
    return t


def zeros_in(t0: float, t1: float, step: float = 0.02, refine: int = 60,
             prec: str = "f8", k: int = 0) -> np.ndarray:
    """All zeros of Z in [t0, t1] via sign changes plus vectorized bisection."""
    _require(prec)
    grid = np.arange(t0, t1 + step, step)
    z = zed(grid, prec=prec, k=k)
    i = np.flatnonzero(np.sign(z[:-1]) != np.sign(z[1:]))
    lo, hi = grid[i], grid[i + 1]
    zlo = z[i]
    for _ in range(refine):
        mid = 0.5 * (lo + hi)
        zm = zed(mid, prec=prec, k=k)
        same = np.sign(zm) == np.sign(zlo)
        lo = np.where(same, mid, lo)
        zlo = np.where(same, zm, zlo)
        hi = np.where(same, hi, mid)
    return 0.5 * (lo + hi)


def completeness(gammas: np.ndarray, t0: float, t1: float) -> tuple[int, float]:
    """(zeros found, zeros predicted by Riemann-von Mangoldt) on [t0, t1]."""
    return int(gammas.size), float(n_count(t1) - n_count(t0))


def unfold(gammas: np.ndarray, center: float | None = None) -> np.ndarray:
    """Rescale to unit mean spacing: multiply gaps by the local zero density.

    Density at height t is log(t/2pi)/(2pi). Passing `center` uses one
    density for the whole block, which is what the high-height Odlyzko files
    need (their heights exceed float64's integer range, so only differences
    are meaningful, and the density is constant to 1e-17 across a block).
    """
    d = np.diff(gammas)
    t = np.full(d.shape, center) if center is not None else gammas[:-1]
    return d * np.log(np.asarray(t) / TWO_PI) / TWO_PI


def wigner_gue(s: np.ndarray) -> np.ndarray:
    """GUE nearest-neighbour surmise: 32/pi^2 s^2 exp(-4 s^2/pi)."""
    return 32.0 / np.pi**2 * s**2 * np.exp(-4.0 * s**2 / np.pi)


def sine_kernel(u: np.ndarray) -> np.ndarray:
    """Montgomery / GUE pair correlation: 1 - (sin(pi u)/(pi u))^2."""
    u = np.asarray(u, dtype=np.float64)
    out = np.ones_like(u)
    nz = u != 0
    out[nz] = 1.0 - (np.sin(np.pi * u[nz]) / (np.pi * u[nz])) ** 2
    out[~nz] = 0.0
    return out


def pair_correlation(spacings: np.ndarray, umax: float = 3.0,
                     nbins: int = 60) -> tuple[np.ndarray, np.ndarray]:
    """Empirical two-point correlation of unfolded zeros, on (0, umax].

    `spacings` are consecutive unfolded gaps (unit mean). Positions are their
    cumulative sum; every pair closer than umax is reached by summing over a
    bounded number of index shifts.
    """
    pos = np.concatenate(([0.0], np.cumsum(spacings)))
    counts = np.zeros(nbins)
    edges = np.linspace(0.0, umax, nbins + 1)
    k = 1
    while k < pos.size:
        d = pos[k:] - pos[:-k]
        if d.min() > umax:
            break
        counts += np.histogram(d[d <= umax], bins=edges)[0]
        k += 1
    width = umax / nbins
    return 0.5 * (edges[:-1] + edges[1:]), counts / (pos.size * width)
