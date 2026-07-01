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

The SECOND reference (`schur_cohn_candidate`, LEARNINGS #143) is the classical circle
certificate from the geometry-of-polynomials corpus: Newton's identities recover the
L-polynomial phi from the point-count moments, Cohn (1922) reduces "all zeros of the
self-inversive phi on |z| = 1" to "all zeros of phi' in the closed unit disk", and the
Schur-Cohn matrix of phi' certifies THAT by positive semidefiniteness. Independent theorem,
same all-green scorecard: the 1922 certificate is itself signature-shaped (functional
equation free, positivity the entire content), which is the M4 shape stated from a corpus
that never heard of Weil.
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


# ---------------------------------------------------------------------------
# The second reference candidate: the classical circle certificate
# (Cohn 1922 + Schur-Cohn), wired in per LEARNINGS #143. Independent of the
# Caratheodory-Toeplitz moment route: a different theorem, the same verdicts.
# ---------------------------------------------------------------------------
def _lower_toeplitz(col: np.ndarray) -> np.ndarray:
    """The m x m lower-triangular Toeplitz matrix T with T[j, l] = col[j - l] for l <= j."""
    m = len(col)
    T = np.zeros((m, m), dtype=complex)
    for j in range(m):
        T[j, : j + 1] = col[j::-1]
    return T


def schur_cohn_matrix(coeffs) -> np.ndarray:
    """The Schur-Cohn matrix of f: the Bezoutian of (f*, f) relative to the unit circle.

    CONVENTION (the brute-force validation in test_toy.test_schur_cohn_formula is the
    arbiter, not this comment): coeffs are DESCENDING (numpy convention). Writing
    f(z) = sum_{k=0}^m a_k z^k and b_k = conj(a_{m-k}) for the coefficients of the
    reversed conjugate f*(z) = z^m conj(f(1/conj z)), and T_a, T_b for the m x m
    lower-triangular Toeplitz matrices with first columns (a_0..a_{m-1}), (b_0..b_{m-1}):

        S = T_b T_b^H - T_a T_a^H,

    equivalently S[j,k] = sum_{l<=min(j,k)} (b_{j-l} conj(b_{k-l}) - a_{j-l} conj(a_{k-l})),
    the coefficient matrix of (f*(z) conj(f*(w)) - f(z) conj(f(w))) / (1 - z conj(w)).

    Schur-Cohn theorem: all roots of f in the CLOSED unit disk => S is PSD; and when f
    and f* are coprime (no on-circle root, no root pair z0, 1/conj(z0) symmetric across
    the circle) the number of negative eigenvalues of S equals the number of roots
    outside the disk, so NOT-PSD <=> some root outside. Common factors of f and f*
    contribute ZERO eigenvalues; the extreme case is a self-inversive f, where S = 0
    identically (the maximally singular branch, #143). That degeneracy is exactly WHY
    Cohn's criterion certifies the self-inversive phi through its DERIVATIVE: phi' is
    not self-inversive, and gcd(phi', phi'*) is supported on the multiple roots of phi
    (from the identity phi'* = n phi - z phi'), so for squarefree phi the certificate
    is exact and a multiple root ON the circle (the supersingular boundary) only adds
    a zero eigenvalue, keeping the verdict PSD.
    """
    a = np.asarray(coeffs, dtype=complex)[::-1]      # ascending a_0..a_m
    m = len(a) - 1
    if m < 1:
        raise ValueError("Schur-Cohn needs degree >= 1")
    b = np.conj(a[::-1])                             # ascending coefficients of f*
    T_a = _lower_toeplitz(a[:m])
    T_b = _lower_toeplitz(b[:m])
    S = T_b @ T_b.conj().T - T_a @ T_a.conj().T
    return (S + S.conj().T) / 2.0


def _phi_from_moments(c: np.ndarray, n: int) -> np.ndarray:
    """Newton's identities: recover the monic phi(z) = prod_u (z - u) (degree n, real
    DESCENDING coefficients) from the power sums c_1..c_n. K1-clean by construction:
    the power sums ARE the exposed point-count moments, never the eigenvalues."""
    e = np.zeros(n + 1)
    e[0] = 1.0
    for k in range(1, n + 1):
        e[k] = sum((-1) ** (i - 1) * e[k - i] * c[i] for i in range(1, k + 1)) / k
    return np.array([(-1.0) ** k * e[k] for k in range(n + 1)])


def schur_cohn_candidate(data: ToyData) -> Optional[np.ndarray]:
    """The #143 classical circle certificate as an executable M4 move.

    Pipeline (K1-clean: only the point-count moments c_1..c_{2g} are used):
      1. Newton's identities recover the monic phi(z) = prod (z - u), degree n = 2g,
         real coefficients; phi is self-inversive because the functional equation
         closes the root multiset under u -> 1/u. The FE is thus an IDENTITY here
         (pairing free), mirroring #143: positivity is the entire content.
      2. Cohn (1922): a self-inversive phi has ALL zeros on |z| = 1 iff phi' has all
         zeros in the CLOSED unit disk.
      3. Schur-Cohn: phi' has all zeros in the closed unit disk iff its Schur-Cohn
         matrix is PSD (real symmetric here, since the coefficients are real).
    So PSD(SchurCohn(phi')) <=> RH-for-the-instance, a theorem independent of the
    Caratheodory-Toeplitz route used by `moment_matrix_candidate`.

    Genus-1 anchor (hand-checkable): phi(z) = z^2 - (t/sqrt p) z + 1 gives
    phi'(z) = 2z - t/sqrt p, whose 1x1 Schur-Cohn matrix is [4 - t^2/p]: PSD iff
    t^2 <= 4p, exactly the Hasse window. The supersingular boundary t^2 = 4q makes
    the matrix PSD-SINGULAR (min eigenvalue exactly 0), which the grader's -PSD_TOL
    threshold already accepts as PSD; no global tolerance change is needed.

    Returns None (uninstantiable) without an Euler product (no moments: the D-H
    firewall) or with fewer than 2g exposed moments (Newton needs c_1..c_{2g})."""
    if not data.has_euler or data.moments is None:
        return None
    n = 2 * data.genus
    if n < 2 or len(data.moments) - 1 < n:
        return None
    c = np.asarray(data.moments, dtype=float)
    phi = _phi_from_moments(c, n)
    dphi = np.polyder(phi)
    return np.real(schur_cohn_matrix(dphi))


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
