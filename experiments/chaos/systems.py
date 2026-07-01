"""Reference chaotic systems with exact Jacobians.

Each system carries both its vector field (or map) and the analytic Jacobian,
because the Lyapunov-spectrum estimator integrates the tangent (variational)
equation and needs the linearization along the trajectory. Known reference
values for the Lyapunov exponents and fractal dimension are stored alongside
so the demo scripts can be checked against the literature.

Continuous systems (Flow):
  Lorenz  (sigma=10, rho=28, beta=8/3)   canonical two-lobe attractor
  Rossler (a=b=0.2, c=5.7)               single-scroll, one fold

Discrete system (DiscreteMap):
  Henon   (a=1.4, b=0.3)                 the 2D archetype
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable

import numpy as np


@dataclass
class Flow:
    """A continuous-time dynamical system dx/dt = deriv(x)."""

    name: str
    deriv: Callable[[np.ndarray], np.ndarray]
    jac: Callable[[np.ndarray], np.ndarray]
    dim: int
    x0: np.ndarray
    dt: float
    transient: float          # time to discard before measuring
    known: dict = field(default_factory=dict)
    is_map: bool = False


@dataclass
class DiscreteMap:
    """A discrete-time dynamical system x_{n+1} = step(x_n)."""

    name: str
    step: Callable[[np.ndarray], np.ndarray]
    jac: Callable[[np.ndarray], np.ndarray]
    dim: int
    x0: np.ndarray
    transient: int
    known: dict = field(default_factory=dict)
    is_map: bool = True


# --- Lorenz ------------------------------------------------------------------

_SIGMA, _RHO, _BETA = 10.0, 28.0, 8.0 / 3.0


def _lorenz_deriv(s):
    x, y, z = s
    return np.array([
        _SIGMA * (y - x),
        x * (_RHO - z) - y,
        x * y - _BETA * z,
    ])


def _lorenz_jac(s):
    x, y, z = s
    return np.array([
        [-_SIGMA, _SIGMA, 0.0],
        [_RHO - z, -1.0, -x],
        [y, x, -_BETA],
    ])


LORENZ = Flow(
    name="Lorenz",
    deriv=_lorenz_deriv,
    jac=_lorenz_jac,
    dim=3,
    x0=np.array([1.0, 1.0, 1.0]),
    dt=0.01,
    transient=20.0,
    known={
        # Sprott / Wolf standard values.
        "lyapunov": [0.906, 0.0, -14.572],
        "kaplan_yorke": 2.062,
        "correlation_dim": 2.05,
    },
)


# --- Rossler -----------------------------------------------------------------

_A, _B, _C = 0.2, 0.2, 5.7


def _rossler_deriv(s):
    x, y, z = s
    return np.array([
        -y - z,
        x + _A * y,
        _B + z * (x - _C),
    ])


def _rossler_jac(s):
    x, y, z = s
    return np.array([
        [0.0, -1.0, -1.0],
        [1.0, _A, 0.0],
        [z, 0.0, x - _C],
    ])


ROSSLER = Flow(
    name="Rossler",
    deriv=_rossler_deriv,
    jac=_rossler_jac,
    dim=3,
    x0=np.array([1.0, 1.0, 1.0]),
    dt=0.02,
    transient=100.0,
    known={
        "lyapunov": [0.0714, 0.0, -5.39],
        "kaplan_yorke": 2.013,
        "correlation_dim": 1.99,
    },
)


# --- Henon -------------------------------------------------------------------

_HA, _HB = 1.4, 0.3


def _henon_step(s):
    x, y = s
    return np.array([1.0 - _HA * x * x + y, _HB * x])


def _henon_jac(s):
    x, y = s
    return np.array([
        [-2.0 * _HA * x, 1.0],
        [_HB, 0.0],
    ])


HENON = DiscreteMap(
    name="Henon",
    step=_henon_step,
    jac=_henon_jac,
    dim=2,
    x0=np.array([0.1, 0.1]),
    transient=1000,
    known={
        "lyapunov": [0.419, -1.623],
        "kaplan_yorke": 1.258,
        "correlation_dim": 1.22,
    },
)


SYSTEMS = {s.name: s for s in (LORENZ, ROSSLER, HENON)}


# --- Integration -------------------------------------------------------------

def _rk4_step(deriv, s, dt):
    k1 = deriv(s)
    k2 = deriv(s + 0.5 * dt * k1)
    k3 = deriv(s + 0.5 * dt * k2)
    k4 = deriv(s + dt * k3)
    return s + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)


def integrate(system, n_samples, sample_every=1, x0=None):
    """Return an (n_samples, dim) array of states on the attractor.

    The transient is discarded first. For a Flow, one RK4 step advances by
    system.dt; sample_every controls thinning (useful to reduce temporal
    autocorrelation before a dimension estimate). For a DiscreteMap each step
    is one iterate.
    """
    s = np.array(system.x0 if x0 is None else x0, dtype=float)

    if system.is_map:
        n_trans = int(system.transient)
        for _ in range(n_trans):
            s = system.step(s)
        out = np.empty((n_samples, system.dim))
        for i in range(n_samples):
            for _ in range(sample_every):
                s = system.step(s)
            out[i] = s
        return out

    dt = system.dt
    n_trans = int(round(system.transient / dt))
    for _ in range(n_trans):
        s = _rk4_step(system.deriv, s, dt)
    out = np.empty((n_samples, system.dim))
    for i in range(n_samples):
        for _ in range(sample_every):
            s = _rk4_step(system.deriv, s, dt)
        out[i] = s
    return out
