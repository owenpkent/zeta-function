"""Abstract L-function interface used across all proof-architecture experiments.

The interface is deliberately minimal: every architecture (positivity,
spectral, zero-free, arithmetic-geometric) only needs evaluation on the
complex plane, zeros (when known on or near the critical line), and a few
analytic invariants (functional-equation gamma factor, conductor).

Concrete implementations live in:
  zeta.py                  - the Riemann zeta function
  davenport_heilbronn.py   - the 1936 Davenport-Heilbronn construction
                              (functional equation, no Euler product,
                              off-line zeros known)
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Iterable

import mpmath as mp


class LFunction(ABC):
    """Minimal interface every L-function-like object must implement.

    Conventions:
      - All complex inputs/outputs use mp.mpc with the current mp.mp.dps.
      - zeros() returns rho = beta + i*gamma with beta in [0, 1]. For
        objects believed to satisfy a Riemann hypothesis, beta will be
        1/2; for the Davenport-Heilbronn control, some beta are not 1/2.
      - has_euler_product distinguishes Selberg-class candidates from
        contrived counterexamples like D-H.
    """

    name: str
    has_euler_product: bool
    has_functional_equation: bool

    @abstractmethod
    def evaluate(self, s) -> "mp.mpc":
        """Evaluate the L-function at s (complex). Uses current mp.mp.dps."""

    @abstractmethod
    def zeros(self, T_max: float, prec: int = 30) -> list:
        """Return zeros rho = beta + i*gamma with 0 < gamma <= T_max.

        Each zero is an mp.mpc. For zeta this delegates to mp.zetazero;
        for the Davenport-Heilbronn control we use mpmath's findroot.
        """

    def dirichlet_coefficient(self, n: int) -> "mp.mpc":
        """The n-th coefficient if represented as a Dirichlet series.

        Optional; concrete classes override when applicable. Used for
        Euler-product / Selberg-class diagnostics.
        """
        raise NotImplementedError(f"{self.name} does not expose Dirichlet coefficients")

    def __repr__(self):
        flags = []
        if self.has_euler_product:
            flags.append("Euler")
        if self.has_functional_equation:
            flags.append("FE")
        return f"<LFunction {self.name} ({', '.join(flags) or 'plain'})>"


def li_coefficients(
    L: LFunction,
    n_max: int,
    T_max: float = 1000.0,
    prec: int = 50,
):
    """Li coefficients lambda_n = sum_rho (1 - (1 - 1/rho)^n).

    The sum is over all non-trivial zeros rho. We assume zeros() returns
    those with Im rho > 0; we pair each rho with its complex conjugate
    rho_bar to get the full sum (which equals 2 * Re of the half sum).

    Convergence is conditional and slow; we truncate at |Im rho| <= T_max
    and return (coeffs, last_terms) so callers can inspect truncation
    error.

    For zeta, Li's criterion states: RH iff lambda_n >= 0 for all n >= 1.
    For Davenport-Heilbronn the sum will reveal negativity once the
    off-line zeros come into play, even at small n.
    """
    mp.mp.dps = prec
    rhos = L.zeros(T_max, prec=prec)
    one = mp.mpf(1)
    coeffs = []
    last_terms = []
    for n in range(1, n_max + 1):
        s = mp.mpf(0)
        last = mp.mpf(0)
        for rho in rhos:
            term = (one - (one - one / rho) ** n).real * 2
            s += term
            last = term
        coeffs.append(s)
        last_terms.append(last)
    return coeffs, last_terms
