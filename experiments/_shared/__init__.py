"""Shared infrastructure for the proof-architecture experiments.

Provides a uniform LFunction interface so positivity, spectral, zero-free,
and arithmetic-geometric experiments can be run against zeta and against
the Davenport-Heilbronn control with identical code paths.
"""

from .lfunction import LFunction
from .zeta import ZetaLFunction, zeta as zeta_L
from .davenport_heilbronn import DavenportHeilbronn
from .dirichlet_l import DirichletL, chi3_L, chi4_L
from .epstein_zeta import (
    EpsteinZeta,
    epstein_for_discriminant,
    epstein_d47,
    epstein_d47_principal,
    epstein_d15,
    KNOWN_FORMS,
)

__all__ = [
    "LFunction",
    "ZetaLFunction",
    "zeta_L",
    "DavenportHeilbronn",
    "DirichletL",
    "chi3_L",
    "chi4_L",
    "EpsteinZeta",
    "epstein_for_discriminant",
    "epstein_d47",
    "epstein_d47_principal",
    "epstein_d15",
    "KNOWN_FORMS",
]
