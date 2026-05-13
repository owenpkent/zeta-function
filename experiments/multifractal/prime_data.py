"""Prime-number-derived time series for multifractal analysis.

Provides:
  - chebyshev_psi_series(x_max, num_points): psi(x) at log-uniform x values.
  - normalized_psi_fluctuation(x_max, num_points): Y(u) = (psi(e^u) - e^u) / e^(u/2).
  - prime_gaps(n_primes): g_k = p_{k+1} - p_k.
  - mertens_series(x_max, num_points): M(x) = sum_{n<=x} mu(n).

The normalized fluctuation Y(u) is the conjectural log-correlated dual of
log|zeta(1/2+it)|: the explicit formula identifies them up to lower-order
arithmetic noise.
"""

from __future__ import annotations

import numpy as np


def _prime_power_contributions(x_max):
    """Sorted (location, value) pairs for psi(x) jumps.

    Each prime p contributes log(p) at every power p, p^2, p^3, ... <= x_max.
    """
    try:
        from sympy import sieve  # lazy import to keep CLI startup fast
    except ImportError as exc:
        raise SystemExit(
            "sympy is required for prime data. Install it via `pip install sympy`."
        ) from exc

    x_max = int(x_max)
    primes = np.fromiter(sieve.primerange(2, x_max + 1), dtype=np.int64)
    log_primes = np.log(primes.astype(float))

    locs = []
    vals = []
    for p, lp in zip(primes, log_primes):
        pk = int(p)
        while pk <= x_max:
            locs.append(pk)
            vals.append(lp)
            pk *= int(p)
    locs = np.array(locs, dtype=np.int64)
    vals = np.array(vals, dtype=float)
    order = np.argsort(locs, kind="mergesort")
    return locs[order], vals[order]


def chebyshev_psi_series(x_max=10**6, num_points=8192, x_min=2.0):
    """Evaluate psi(x) at log-uniform x in [x_min, x_max].

    Returns (us, xs, psi_vals) where us = log(xs).
    """
    locs, vals = _prime_power_contributions(x_max)
    cum = np.cumsum(vals)

    us = np.linspace(np.log(float(x_min)), np.log(float(x_max)), int(num_points))
    xs = np.exp(us)
    idx = np.searchsorted(locs, xs, side="right") - 1
    psi_vals = np.where(idx >= 0, cum[np.clip(idx, 0, None)], 0.0)
    return us, xs, psi_vals


def normalized_psi_fluctuation(x_max=10**6, num_points=8192, x_min=2.0):
    """Y(u) = (psi(e^u) - e^u) / e^(u/2), on a uniform u grid.

    By RH, this is bounded by polylog(u) in u. On a log-uniform grid in x,
    samples are uniform in u, which is the natural log-correlated time
    variable.

    x_min defaults to 2; for cleaner large-x behavior set x_min ~ 100 to skip
    the small-prime regime where discretization noise from a sparse sample
    grid dominates.
    """
    us, xs, psi_vals = chebyshev_psi_series(
        x_max=x_max, num_points=num_points, x_min=x_min,
    )
    Y = (psi_vals - xs) / np.sqrt(xs)
    return us, Y


def prime_gaps(n_primes=10**5):
    """Sequence of consecutive prime gaps g_k = p_{k+1} - p_k for k = 1..n_primes."""
    try:
        from sympy import prime
    except ImportError as exc:
        raise SystemExit(
            "sympy is required for prime data. Install it via `pip install sympy`."
        ) from exc

    # sympy.prime(k) is the k-th prime; we want the first n_primes+1 primes.
    # For speed, use sieve up to an upper bound from prime number theorem.
    from sympy import sieve

    # nth prime < n (ln n + ln ln n) for n >= 6 (Rosser).
    n = int(n_primes) + 1
    import math
    upper = int(n * (math.log(n) + math.log(math.log(n))) * 1.2) + 100
    ps = np.fromiter(sieve.primerange(2, upper + 1), dtype=np.int64)
    if ps.size < n + 1:
        # rare edge case; widen
        ps = np.fromiter(sieve.primerange(2, upper * 2 + 1), dtype=np.int64)
    ps = ps[: n + 1]
    return np.diff(ps).astype(float)


def mertens_series(x_max=10**6, num_points=8192):
    """Mertens function M(x) = sum_{n<=x} mu(n) at log-uniform x in [2, x_max].

    Returns (us, xs, M_vals).
    """
    x_max = int(x_max)
    # Compute mu(n) for n = 1..x_max via a linear sieve (no sympy needed).
    mu = np.zeros(x_max + 1, dtype=np.int8)
    mu[1] = 1
    primes = []
    is_composite = np.zeros(x_max + 1, dtype=bool)
    for i in range(2, x_max + 1):
        if not is_composite[i]:
            mu[i] = -1
            primes.append(i)
        for p in primes:
            ip = i * p
            if ip > x_max:
                break
            is_composite[ip] = True
            if i % p == 0:
                mu[ip] = 0
                break
            else:
                mu[ip] = -mu[i]
    M_full = np.cumsum(mu[1:].astype(np.int64))  # M_full[k] = M(k+1)

    us = np.linspace(np.log(2.0), np.log(float(x_max)), int(num_points))
    xs = np.exp(us)
    idx = np.clip(np.floor(xs).astype(np.int64) - 1, 0, M_full.size - 1)
    M_vals = M_full[idx].astype(float)
    return us, xs, M_vals
