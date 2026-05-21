"""Shared infrastructure for the proof-architecture experiments.

Provides a uniform LFunction interface so positivity, spectral, zero-free,
and arithmetic-geometric experiments can be run against zeta and against
the Davenport-Heilbronn control with identical code paths.
"""

from .lfunction import LFunction
from .zeta import ZetaLFunction, zeta as zeta_L
from .davenport_heilbronn import DavenportHeilbronn

__all__ = [
    "LFunction",
    "ZetaLFunction",
    "zeta_L",
    "DavenportHeilbronn",
]
