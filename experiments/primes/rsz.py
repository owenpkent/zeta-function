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
"""
from __future__ import annotations

import numpy as np

TWO_PI = 2.0 * np.pi


def theta(t: np.ndarray | float) -> np.ndarray:
    """Riemann-Siegel phase, asymptotic series (error ~1e-9 for t > 50)."""
    t = np.asarray(t, dtype=np.float64)
    return (0.5 * t * np.log(t / TWO_PI) - 0.5 * t - np.pi / 8
            + 1.0 / (48.0 * t) + 7.0 / (5760.0 * t**3))


def n_count(t: np.ndarray | float) -> np.ndarray:
    """Smooth zero-counting function N(t) = theta(t)/pi + 1 (drops S(t))."""
    return theta(t) / np.pi + 1.0


def zed(t: np.ndarray, chunk: int = 20000) -> np.ndarray:
    """Riemann-Siegel Z(t), vectorized, main sum plus the C0 remainder."""
    t = np.asarray(t, dtype=np.float64)
    out = np.empty(t.size)
    for i in range(0, t.size, chunk):
        tc = t[i : i + chunk]
        a = np.sqrt(tc / TWO_PI)
        nu = np.floor(a).astype(np.int64)
        th = theta(tc)
        nmax = int(nu.max())
        n = np.arange(1, nmax + 1, dtype=np.float64)
        # cos(theta - t log n) / sqrt(n), zeroing terms beyond nu(t)
        phase = th[:, None] - np.outer(tc, np.log(n))
        terms = np.cos(phase) / np.sqrt(n)
        terms[n[None, :] > nu[:, None]] = 0.0
        main = 2.0 * terms.sum(axis=1)
        p = a - nu
        c0 = np.cos(TWO_PI * (p * p - p - 0.0625)) / np.cos(TWO_PI * p)
        out[i : i + chunk] = main + np.where(nu % 2 == 0, -1.0, 1.0) * a**-0.5 * c0
    return out


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


def zeros_in(t0: float, t1: float, step: float = 0.02, refine: int = 60) -> np.ndarray:
    """All zeros of Z in [t0, t1] via sign changes plus vectorized bisection."""
    grid = np.arange(t0, t1 + step, step)
    z = zed(grid)
    i = np.flatnonzero(np.sign(z[:-1]) != np.sign(z[1:]))
    lo, hi = grid[i], grid[i + 1]
    zlo = z[i]
    for _ in range(refine):
        mid = 0.5 * (lo + hi)
        zm = zed(mid)
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
