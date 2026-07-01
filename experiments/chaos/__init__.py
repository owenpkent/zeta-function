"""Chaos and strange-attractor playground.

A small, self-contained numerical thread for classical deterministic chaos:
Lyapunov spectra, fractal dimensions, and the multifractal generalized-dimension
ladder. It sits next to the multifractal thread (experiments/multifractal) and
shares its MFDFA implementation. See README.md for the through-line to the
project's log-correlated / quantum-chaos material.
"""

from .systems import SYSTEMS, Flow, DiscreteMap, integrate

__all__ = ["SYSTEMS", "Flow", "DiscreteMap", "integrate"]
