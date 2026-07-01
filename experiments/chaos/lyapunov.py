"""Lyapunov spectrum via the Benettin algorithm (tangent-space QR).

The largest Lyapunov exponent measures the exponential rate at which nearby
trajectories separate: |delta(t)| ~ |delta(0)| exp(lambda t). A positive
largest exponent is the operational definition of chaos.

To get the full ordered spectrum lambda_1 >= lambda_2 >= ... we evolve an
orthonormal frame of tangent vectors under the linearized dynamics (the
variational equation dQ/dt = J(x) Q for a flow, Q -> J(x) Q for a map) and
periodically re-orthonormalize by QR decomposition. The exponents are the
long-time average growth rates of the diagonal of R:

    lambda_i = (1 / total_time) sum over renormalizations of log |R_ii|.

Gram-Schmidt (QR) processes columns in order, so the estimator returns the
exponents already sorted from largest to smallest.

Reference: Benettin et al. (1980); Wolf et al., Physica D 16 (1985) 285.
"""

from __future__ import annotations

import numpy as np


def _qr_positive(A):
    """QR with the sign convention diag(R) >= 0 (keeps the frame consistent)."""
    Q, R = np.linalg.qr(A)
    signs = np.sign(np.diag(R))
    signs[signs == 0] = 1.0
    Q = Q * signs
    R = R * signs[:, None]
    return Q, R


def lyapunov_spectrum(system, total_time=None, n_steps=None, renorm_every=1):
    """Estimate the full Lyapunov spectrum of a Flow or DiscreteMap.

    For a Flow, total_time sets the measurement length (default 600 time units).
    For a DiscreteMap, n_steps sets the number of iterates (default 200000).
    Returns a numpy array of exponents, largest first. Flow exponents are per
    unit time; map exponents are per iterate.
    """
    n = system.dim
    Q = np.eye(n)
    accum = np.zeros(n)

    if system.is_map:
        n_steps = int(n_steps if n_steps is not None else 200_000)
        s = np.array(system.x0, dtype=float)
        for _ in range(int(system.transient)):
            s = system.step(s)
        count = 0
        for k in range(n_steps):
            Q = system.jac(s) @ Q
            s = system.step(s)
            if (k + 1) % renorm_every == 0:
                Q, R = _qr_positive(Q)
                accum += np.log(np.abs(np.diag(R)))
                count += 1
        return accum / n_steps

    # Flow: integrate state and tangent frame together with RK4.
    dt = system.dt
    total_time = float(total_time if total_time is not None else 600.0)
    n_steps = int(round(total_time / dt))
    deriv, jac = system.deriv, system.jac

    s = np.array(system.x0, dtype=float)
    for _ in range(int(round(system.transient / dt))):
        # transient advances the state only
        k1 = deriv(s)
        k2 = deriv(s + 0.5 * dt * k1)
        k3 = deriv(s + 0.5 * dt * k2)
        k4 = deriv(s + dt * k3)
        s = s + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)

    def aug(y, M):
        return deriv(y), jac(y) @ M

    for k in range(n_steps):
        a1y, a1Q = aug(s, Q)
        a2y, a2Q = aug(s + 0.5 * dt * a1y, Q + 0.5 * dt * a1Q)
        a3y, a3Q = aug(s + 0.5 * dt * a2y, Q + 0.5 * dt * a2Q)
        a4y, a4Q = aug(s + dt * a3y, Q + dt * a3Q)
        s = s + (dt / 6.0) * (a1y + 2 * a2y + 2 * a3y + a4y)
        Q = Q + (dt / 6.0) * (a1Q + 2 * a2Q + 2 * a3Q + a4Q)
        if (k + 1) % renorm_every == 0:
            Q, R = _qr_positive(Q)
            accum += np.log(np.abs(np.diag(R)))

    return accum / (n_steps * dt)


def kaplan_yorke(exponents):
    """Kaplan-Yorke (Lyapunov) dimension from an ordered exponent spectrum.

    D_KY = k + (lambda_1 + ... + lambda_k) / |lambda_{k+1}|, where k is the
    largest index for which the partial sum of exponents is non-negative.
    Returns the system dimension if the whole spectrum sums non-negative
    (no contraction captured), and 0.0 if even the first exponent is negative.
    """
    lam = np.sort(np.asarray(exponents, dtype=float))[::-1]
    partial = 0.0
    k = 0
    for i, li in enumerate(lam):
        if partial + li < 0.0:
            k = i
            break
        partial += li
    else:
        return float(len(lam))
    if k == 0:
        return 0.0
    return k + partial / abs(lam[k])
