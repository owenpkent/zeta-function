"""The grader: score a proposed M4 construction against the toy battery.

A CANDIDATE is a function

    candidate(data: ToyData) -> numpy.ndarray | None

that, from the K1-clean data alone (q, genus, the point-count moments c_0..c_K),
builds a real symmetric matrix M it claims is THE POLARIZATION: PSD <=> RH. It must
return None (or raise) when it cannot be instantiated (e.g. no Euler product => no
moments => no construction).

The grader runs the candidate over the whole battery and scores four things:

  reproduces_weil : M is PSD on every RH-true instance (matches the proven theorem).
  rejects_fakes   : M is indefinite on every RH-false instance (catches the off-line zero).
  k1_clean        : structural. The candidate only ever saw point counts, never the
                    eigenvalue moduli or the on-circle assumption, so it cannot have read
                    the answer off the zeros. (Enforced by the ToyData interface.)
  dh_immune       : on the no-Euler-product instance the construction is uninstantiable
                    (returns None), so it cannot spuriously certify Davenport-Heilbronn.

The REFERENCE candidate (`moment_matrix_candidate`) is the e2xx Toeplitz moment matrix
G = [c_{|j-k|}]; by Caratheodory-Toeplitz it is PSD at every order iff all |u| = 1 iff RH
for the curve. It scores all green. It is the known-correct M4 move in the toy; the open
problem (over Z) is to PROVE its positivity from a polarization rather than from the zeros,
and to survive the lift past the finite-spectrum / single-circle structure (LEARNINGS #128).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Optional

import numpy as np

from experiments.toy.instances import (
    ToyData,
    ToyInstance,
    FULL_BATTERY,
)

Candidate = Callable[[ToyData], Optional[np.ndarray]]

PSD_TOL = 1e-9


def is_psd(M: np.ndarray, tol: float = PSD_TOL) -> bool:
    """True iff the symmetric matrix M is positive semidefinite (min eigenvalue >= -tol)."""
    if M is None:
        return False
    w = np.linalg.eigvalsh((M + M.T) / 2.0)
    return float(w.min()) >= -tol


def min_eig(M: np.ndarray) -> float:
    if M is None:
        return float("nan")
    return float(np.linalg.eigvalsh((M + M.T) / 2.0).min())


# ---------------------------------------------------------------------------
# The reference candidate: the e2xx trigonometric moment matrix.
# ---------------------------------------------------------------------------
def moment_matrix_candidate(data: ToyData) -> Optional[np.ndarray]:
    """G[j,k] = c_{|j-k|}, the symmetric Toeplitz moment matrix on the exposed moments.
    PSD at every order iff the c_n are Fourier coefficients of a positive measure on the
    circle iff every |u| = 1 iff RH (Caratheodory-Toeplitz). Uninstantiable without an
    Euler product (no moments)."""
    if not data.has_euler or data.moments is None:
        return None
    c = np.asarray(data.moments, dtype=float)
    m = len(c)
    return np.array([[c[abs(j - k)] for k in range(m)] for j in range(m)], dtype=float)


@dataclass
class InstanceResult:
    name: str
    rh_true: bool
    buildable: bool
    psd: Optional[bool]
    min_eig: float
    correct: bool       # PSD verdict matches rh_true (or correctly unbuildable for D-H)


@dataclass
class Scorecard:
    candidate_name: str
    K: int
    results: list
    reproduces_weil: bool
    rejects_fakes: bool
    dh_immune: bool
    k1_clean: bool = True   # structural: candidates only ever receive point counts

    @property
    def all_green(self) -> bool:
        return self.reproduces_weil and self.rejects_fakes and self.dh_immune and self.k1_clean

    def report(self) -> str:
        lines = [f"  candidate: {self.candidate_name}   (K = {self.K} moments exposed)"]
        for r in self.results:
            if not r.buildable:
                verdict = "unbuildable (no Euler product)"
                mark = "OK " if r.correct else "BAD"
            else:
                verdict = f"{'PSD ' if r.psd else 'INDEF'}  min_eig={r.min_eig:+.3e}"
                mark = "OK " if r.correct else "BAD"
            tag = "RH-true " if r.rh_true else "RH-false"
            lines.append(f"    [{mark}] {tag}  {r.name:46}  {verdict}")
        lines.append(
            f"  => reproduces_weil={self.reproduces_weil}  rejects_fakes={self.rejects_fakes}  "
            f"dh_immune={self.dh_immune}  k1_clean={self.k1_clean}  "
            f"{'<<< ALL GREEN' if self.all_green else '<<< FAILS'}"
        )
        return "\n".join(lines)


def grade(candidate: Candidate, name: str = "candidate",
          battery: Optional[list] = None, K: int = 6) -> Scorecard:
    """Run `candidate` over the battery and produce a Scorecard."""
    if battery is None:
        battery = FULL_BATTERY
    results = []
    reproduces_weil = True
    rejects_fakes = True
    dh_immune = True

    for inst in battery:
        data = inst.to_data(K)
        try:
            M = candidate(data)
        except Exception:
            M = None
        buildable = M is not None

        if inst.kind == "dh":
            # The firewall: the construction must be UNINSTANTIABLE for D-H.
            correct = not buildable
            dh_immune = dh_immune and correct
            results.append(InstanceResult(inst.name, inst.rh_true, buildable, None,
                                          float("nan"), correct))
            continue

        if not buildable:
            # A curve/fake instance the candidate refused to build: counts as wrong
            # (it should certify the curves and reject the fakes, not abstain).
            correct = False
            if inst.rh_true:
                reproduces_weil = False
            else:
                rejects_fakes = False
            results.append(InstanceResult(inst.name, inst.rh_true, False, None,
                                          float("nan"), correct))
            continue

        psd = is_psd(M)
        correct = (psd == inst.rh_true)
        if inst.rh_true and not psd:
            reproduces_weil = False
        if (not inst.rh_true) and psd:
            rejects_fakes = False
        results.append(InstanceResult(inst.name, inst.rh_true, True, psd, min_eig(M), correct))

    return Scorecard(name, K, results, reproduces_weil, rejects_fakes, dh_immune)


# ---------------------------------------------------------------------------
# Demonstration "bad" candidates: show the grader has teeth.
# ---------------------------------------------------------------------------
def identity_candidate(data: ToyData) -> Optional[np.ndarray]:
    """Always returns an identity (always PSD). Certifies everything, including the fakes:
    a soft 'positivity' with no RH content. Should FAIL rejects_fakes."""
    if not data.has_euler or data.moments is None:
        return None
    m = len(data.moments)
    return np.eye(m)


def diag_moment_candidate(data: ToyData) -> Optional[np.ndarray]:
    """Uses only the diagonal c_0 (= 2g, the unconditional norm), discarding the off-diagonal
    Frobenius coupling where the RH flip lives (#127). PSD for everything => FAILS rejects_fakes.
    The toy version of 'a wrong-polarity, unconditional form cannot flag an off-line zero'."""
    if not data.has_euler or data.moments is None:
        return None
    c0 = data.moments[0]
    m = len(data.moments)
    return c0 * np.eye(m)
