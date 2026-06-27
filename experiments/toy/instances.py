"""The toy battery: positive (RH true) and negative (RH false) function-field instances.

Each instance is a finite Frobenius spectrum in NORMALIZED coordinates u = alpha / sqrt(q),
where alpha ranges over the Frobenius eigenvalues on H^1 of a curve of genus g over F_q.
The spectrum is closed under u -> 1/u (the Rosati pairing alpha <-> q/alpha) and under
complex conjugation (the L-polynomial has integer coefficients), so the moment sequence

    c_n = sum_u u^n   (n = 0, 1, 2, ...)

is REAL, with c_0 = 2g. Under RH every |u| = 1 (Weil), so c_n = sum 2 cos(n phi); off RH
some |u| != 1. The point-count reading is c_n = (q^n + 1 - #C(F_{q^n})) / q^{n/2}.

The eigenvalue multiset is the ANSWER KEY. A candidate construction never sees it: it
receives only `ToyData` (q, genus, the moments c_0..c_K, the Euler-product flag), which is
exactly the K1-clean information a real M4 construction is allowed to use (point counts /
the zeta numerator, not the eigenvalue moduli, never the on-circle assumption).

Provenance: genus-1 eigenvalues reuse experiments.lemma_db.fq_shadow.elliptic_eigenvalues;
the moment matrix that grades these mirrors experiments.arithmetic_geometric.e2xx; the D-H
flag mirrors experiments._shared.davenport_heilbronn (has_euler_product = False).
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from typing import Optional

import numpy as np

from experiments.lemma_db.fq_shadow import elliptic_eigenvalues


# ---------------------------------------------------------------------------
# Spectrum builders (each returns a tuple of normalized eigenvalues u, closed
# under u -> 1/u and conjugation, so the moments are real).
# ---------------------------------------------------------------------------
def on_circle_pair(phi: float) -> tuple:
    """An RH-respecting Frobenius pair: {e^{i phi}, e^{-i phi}} on |u| = 1. Genus +1."""
    return (cmath.exp(1j * phi), cmath.exp(-1j * phi))


def off_circle_quad(r: float, phi: float) -> tuple:
    """A generic off-circle quadruple {r e^{+-i phi}, (1/r) e^{+-i phi}}. RH FALSE. Genus +2.
    Conjugation- and inversion-closed, so the moments stay real. The function-field
    analogue of a Davenport-Heilbronn off-line zero (functional equation intact, |u| != 1)."""
    a = r * cmath.exp(1j * phi)
    return (a, r * cmath.exp(-1j * phi), 1 / a, (1 / r) * cmath.exp(1j * phi))


def real_off_pair(r: float) -> tuple:
    """A real off-circle pair {r, 1/r}, r != 1. RH FALSE, and on the REAL-ROOT half of the
    discriminant (t^2 - 4q >= 0): the Lorentzian / log-concave / Lee-Yang family the
    discriminant-complementarity screen retires (#119). Genus +1."""
    return (float(r), 1.0 / float(r))


@dataclass(frozen=True)
class ToyData:
    """The candidate's K1-clean view of an instance. Deliberately excludes the eigenvalue
    moduli and the on-circle assumption: a construction may use only the arithmetic data
    an M4 construction over Z is allowed (point counts / the zeta numerator)."""
    q: int
    genus: int
    moments: Optional[tuple]   # (c_0, c_1, ..., c_K); None when no Euler product exists (D-H)
    has_euler: bool


@dataclass(frozen=True)
class ToyInstance:
    name: str
    q: int
    eigenvalues_u: tuple       # ANSWER KEY: the full 2g multiset in u-coords (hidden from candidates)
    rh_true: bool
    has_euler: bool = True
    kind: str = "curve"        # 'curve' | 'fake' | 'dh'

    @property
    def genus(self) -> int:
        return len(self.eigenvalues_u) // 2

    def moment(self, n: int) -> float:
        return float(sum(u ** n for u in self.eigenvalues_u).real)

    def moments(self, K: int) -> tuple:
        return tuple(self.moment(n) for n in range(K + 1))

    def circle_defect(self) -> float:
        """max_u | |u| - 1 |: 0 iff RH holds at this instance."""
        if not self.eigenvalues_u:
            return float("nan")
        return max(abs(abs(u) - 1.0) for u in self.eigenvalues_u)

    def to_data(self, K: int) -> ToyData:
        """The K1-clean view handed to a candidate. K = how many point-count moments
        are exposed (c_0..c_K). No Euler product => no moments (the construction is
        uninstantiable, which is exactly the D-H firewall)."""
        moms = self.moments(K) if self.has_euler else None
        return ToyData(q=self.q, genus=self.genus, moments=moms, has_euler=self.has_euler)


def _elliptic_u(p: int, a: int) -> tuple:
    """Normalized eigenvalues u = alpha / sqrt(p) of E/F_p with trace a (on circle iff a^2<4p)."""
    sq = math.sqrt(p)
    return tuple(z / sq for z in elliptic_eigenvalues(p, a))


def _e2xx_fake_u() -> tuple:
    """The canonical integer genus-2 fake-zeta (e2xx / LEARNINGS #123): the L-polynomial
    P(T) = T^4 - 4T^3 + 15T^2 - 20T + 25 over q=5 has the curve functional equation but
    roots off the circle (|alpha| in {1.749, 2.859}, not sqrt(5)). The function-field
    analogue of a Davenport-Heilbronn counterexample at the form level."""
    q = 5
    alphas = np.roots([1.0, -4.0, 15.0, -20.0, 25.0])
    sq = math.sqrt(q)
    return tuple(complex(a) / sq for a in alphas)


# ---------------------------------------------------------------------------
# The positive battery: RH is true (Weil / Hasse). All eigenvalues on |u| = 1.
# ---------------------------------------------------------------------------
POSITIVE_BATTERY = [
    ToyInstance("E/F_5  (a=1, genus 1)", 5, _elliptic_u(5, 1), rh_true=True),
    ToyInstance("E/F_7  (a=2, genus 1)", 7, _elliptic_u(7, 2), rh_true=True),
    ToyInstance("E/F_13 (a=4, genus 1)", 13, _elliptic_u(13, 4), rh_true=True),
    ToyInstance(
        "synthetic genus-2 (on-circle Weil spectrum)", 9,
        on_circle_pair(0.7) + on_circle_pair(1.9), rh_true=True,
    ),
    ToyInstance(
        "synthetic genus-3 (on-circle Weil spectrum)", 9,
        on_circle_pair(0.5) + on_circle_pair(1.3) + on_circle_pair(2.5), rh_true=True,
    ),
]


# ---------------------------------------------------------------------------
# The negative battery: RH is FALSE (the function-field analogue of D-H).
# ---------------------------------------------------------------------------
NEGATIVE_BATTERY = [
    ToyInstance("e2xx fake-zeta P(T) over q=5 (genus 2, off-circle)", 5,
                _e2xx_fake_u(), rh_true=False, kind="fake"),
    ToyInstance("complex off-circle quad (r=1.25, genus 2)", 9,
                off_circle_quad(1.25, 1.1), rh_true=False, kind="fake"),
    ToyInstance("real off-circle pair r=1.5 (genus 1, real-root half)", 9,
                real_off_pair(1.5), rh_true=False, kind="fake"),
    # Davenport-Heilbronn: a functional equation but NO Euler product, so no finite
    # Frobenius spectrum and no point-count moments. The toy machinery is unbuildable
    # for it BY TYPE, which is the firewall. (The analytic object lives in
    # experiments._shared.davenport_heilbronn; here it is a typed marker.)
    ToyInstance("Davenport-Heilbronn (no Euler product)", 0, (),
                rh_true=False, has_euler=False, kind="dh"),
]

FULL_BATTERY = POSITIVE_BATTERY + NEGATIVE_BATTERY
