"""Multifractal Detrended Fluctuation Analysis (MFDFA).

Reference: Kantelhardt, J.W. et al. (2002), "Multifractal detrended fluctuation
analysis of nonstationary time series," Physica A 316, 87-114.

For a stationary or nearly-stationary series X[0..N-1]:
  1. Form the profile Y[i] = sum_{k=0}^{i} (X[k] - mean(X)).
  2. Cut Y into 2 * floor(N/s) non-overlapping windows of length s
     (floor(N/s) from the start, floor(N/s) from the end, so the tail is used).
  3. In each window v, fit a polynomial of degree m and let F2(s, v) be the
     variance of the residual.
  4. Define F_q(s) = ( (1 / (2*floor(N/s))) sum_v F2(s,v)^(q/2) )^(1/q)
     with the q -> 0 limit handled by the log average.
  5. For a multifractal, F_q(s) ~ s^h(q) over a range of s.
  6. Scaling exponent tau(q) = q * h(q) - 1.
  7. Singularity strength alpha(q) = d tau / d q and spectrum
     D(alpha) = q * alpha - tau(q) (Legendre transform).
"""

from __future__ import annotations

import numpy as np


def mfdfa(series, scales, q_values, order=2):
    """Run MFDFA on a 1D series.

    Parameters
    ----------
    series : array_like, shape (N,)
        Input time series. Should be approximately stationary.
    scales : array_like of int
        Window sizes s. Each must satisfy 2*(order+1) <= s <= N // 4 for the
        result to be meaningful.
    q_values : array_like
        Moments q. Include both positive and negative values to probe both
        large fluctuations (q > 0) and small ones (q < 0). q = 0 is handled.
    order : int
        Degree of polynomial detrending inside each window. 1 = linear, 2 =
        quadratic. Default 2.

    Returns
    -------
    dict with keys:
        scales      : np.ndarray of scales actually used.
        q           : np.ndarray of q values.
        F           : np.ndarray, shape (len(scales), len(q)), F_q(s).
        h           : np.ndarray, shape (len(q),), generalized Hurst h(q).
        tau         : np.ndarray, q * h(q) - 1.
        alpha       : np.ndarray, singularity strength d tau / d q.
        D_alpha     : np.ndarray, singularity spectrum.
        log_intercept : np.ndarray, intercept of log F vs log s fit per q.
    """
    series = np.asarray(series, dtype=float)
    N = series.size
    scales = np.asarray(sorted(set(int(s) for s in scales)), dtype=int)
    scales = scales[(scales >= 2 * (order + 1)) & (scales <= N // 4)]
    if scales.size < 3:
        raise ValueError("Need at least 3 valid scales; got %d after filtering" % scales.size)
    q_values = np.asarray(q_values, dtype=float)

    profile = np.cumsum(series - series.mean())

    F = np.zeros((scales.size, q_values.size))
    for i, s in enumerate(scales):
        Ns = N // s
        x = np.arange(s)
        F2 = np.empty(2 * Ns)
        for v in range(Ns):
            seg = profile[v * s : (v + 1) * s]
            coef = np.polyfit(x, seg, order)
            resid = seg - np.polyval(coef, x)
            F2[v] = np.mean(resid * resid)
        for v in range(Ns):
            seg = profile[N - (v + 1) * s : N - v * s]
            coef = np.polyfit(x, seg, order)
            resid = seg - np.polyval(coef, x)
            F2[Ns + v] = np.mean(resid * resid)

        F2 = np.clip(F2, 1e-300, None)  # guard log
        for j, q in enumerate(q_values):
            if abs(q) < 1e-12:
                F[i, j] = np.exp(0.5 * np.mean(np.log(F2)))
            else:
                F[i, j] = np.mean(F2 ** (q / 2.0)) ** (1.0 / q)

    log_s = np.log(scales)
    log_F = np.log(F)
    h = np.empty(q_values.size)
    intercept = np.empty(q_values.size)
    for j in range(q_values.size):
        slope, b = np.polyfit(log_s, log_F[:, j], 1)
        h[j] = slope
        intercept[j] = b

    tau = q_values * h - 1.0
    # Numerical derivative for alpha; gradient handles non-uniform q but our q is uniform.
    alpha = np.gradient(tau, q_values)
    D_alpha = q_values * alpha - tau

    return {
        "scales": scales,
        "q": q_values,
        "F": F,
        "h": h,
        "tau": tau,
        "alpha": alpha,
        "D_alpha": D_alpha,
        "log_intercept": intercept,
    }


def hurst_summary(result):
    """One-line summary of the result, useful for printing."""
    q = result["q"]
    h = result["h"]
    h_at_2 = float(np.interp(2.0, q, h))
    width = float(result["alpha"].max() - result["alpha"].min())
    return (
        "h(q=2) = %.4f (monofractal -> 0.5); alpha spectrum width = %.4f "
        "(monofractal -> 0); q range = [%g, %g]" % (h_at_2, width, q.min(), q.max())
    )
