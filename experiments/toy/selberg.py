"""The spectral toy: a self-adjoint operator puts the zeros on the line (Architecture 1).

This is the Hilbert-Polya training ground. For a compact hyperbolic surface the Selberg
zeta function Z(s) has its non-trivial zeros at

    s = 1/2 +- i r_n,     where   1/4 + r_n^2 = lambda_n = eigenvalue of the Laplacian.

The Laplacian is SELF-ADJOINT and NON-NEGATIVE, so lambda_n >= 0. For lambda_n >= 1/4 the
quantity r_n = sqrt(lambda_n - 1/4) is REAL, and the zero sits exactly on Re(s) = 1/2: the
RH-analogue is a THEOREM, and it holds *because* the operator is self-adjoint and bounded
below. This is the world where Hilbert-Polya is realized.

The toy lesson (which is exactly why the move does NOT transfer to zeta, LEARNINGS #128
Front 3): here the zeros ARE eigenvalues of a positive self-adjoint operator, so
self-adjointness fixes them on the line for free. For zeta the only natural self-adjoint
operator (the Connes idele-class scaling operator) has CONTINUOUS spectrum and the zeros are
RESONANCES, not eigenvalues; self-adjointness then fixes the imaginary part (automatic) and
is silent on Re(rho), the one coordinate RH is about. The toy realizes the structure; the
realization is precisely what is missing over Z.

We model the "Laplacian" by a small symmetric matrix (self-adjoint, real eigenvalues) and
show two things:
  * self-adjoint + spectrum >= 1/4  => all zeros on Re(s) = 1/2 (RH-analogue holds);
  * a NON-self-adjoint (non-normal) operator can have complex eigenvalues => off-line zeros,
    so self-adjointness is the load-bearing hypothesis.
"""

from __future__ import annotations

import cmath
from dataclasses import dataclass

import numpy as np


@dataclass
class SpectralVerdict:
    on_line: bool
    max_offline: float     # max |Re(s) - 1/2| over the non-trivial zeros
    zeros: list            # the s-values 1/2 +- i sqrt(lambda - 1/4)


def selberg_zeros_from_spectrum(eigs) -> list:
    """Map Laplacian eigenvalues lambda to Selberg-zeta zeros s = 1/2 +- i sqrt(lambda-1/4).
    Real lambda >= 1/4 -> on the line; lambda < 1/4 -> real s (exceptional); complex lambda
    (non-self-adjoint operator) -> generic off-line s."""
    zeros = []
    for lam in eigs:
        r = cmath.sqrt(complex(lam) - 0.25)
        zeros.append(0.5 + 1j * r)
        zeros.append(0.5 - 1j * r)
    return zeros


def critical_line_verdict(eigs, tol: float = 1e-9) -> SpectralVerdict:
    zeros = selberg_zeros_from_spectrum(eigs)
    # An exceptional small eigenvalue (lambda in [0,1/4)) gives a real s off the line; for the
    # RH-analogue (all non-trivial zeros on Re(s)=1/2) we require lambda >= 1/4 as well.
    offline = max(abs(z.real - 0.5) for z in zeros) if zeros else 0.0
    return SpectralVerdict(on_line=offline <= tol, max_offline=offline, zeros=zeros)


def random_self_adjoint(n: int, lo: float, seed: int) -> np.ndarray:
    """A symmetric (self-adjoint) n x n matrix with eigenvalues >= lo. Built A = Q diag(d) Q^T
    with d >= lo, so it is a faithful finite stand-in for a Laplacian bounded below by lo."""
    rng = np.random.default_rng(seed)
    Q, _ = np.linalg.qr(rng.standard_normal((n, n)))
    d = lo + rng.uniform(0.0, 3.0, size=n)
    return Q @ np.diag(d) @ Q.T


def break_self_adjointness(A: np.ndarray, eps: float, seed: int) -> np.ndarray:
    """Add a non-symmetric perturbation: the operator is no longer self-adjoint, eigenvalues
    can go complex, and the zeros leave the line. Shows self-adjointness is load-bearing."""
    rng = np.random.default_rng(seed)
    N = rng.standard_normal(A.shape)
    return A + eps * (N - N.T)   # antisymmetric part => generally complex spectrum


def demo() -> None:
    print("Spectral toy (Selberg / Hilbert-Polya): self-adjointness puts zeros on the line\n")

    A = random_self_adjoint(6, lo=0.25, seed=1)
    v = critical_line_verdict(np.linalg.eigvalsh(A))
    print("  SELF-ADJOINT Laplacian, spectrum >= 1/4 (the proven Selberg world):")
    print(f"    all zeros on Re(s)=1/2 ? {v.on_line}   max |Re(s)-1/2| = {v.max_offline:.2e}")

    B = break_self_adjointness(A, eps=0.4, seed=2)
    eigs = np.linalg.eigvals(B)   # general (complex) eigenvalues
    v2 = critical_line_verdict(eigs)
    print("\n  NON-self-adjoint perturbation (the hypothesis removed):")
    print(f"    all zeros on Re(s)=1/2 ? {v2.on_line}   max |Re(s)-1/2| = {v2.max_offline:.2e}")

    print(
        "\n  Lesson: in the Selberg world the zeros ARE eigenvalues of a positive self-adjoint\n"
        "  operator, so the line is automatic. For zeta the zeros are RESONANCES, not\n"
        "  eigenvalues (Connes' operator has continuous spectrum), so self-adjointness fixes\n"
        "  Im(rho) for free and says nothing about Re(rho). The toy realizes Hilbert-Polya;\n"
        "  that realization is exactly what is missing over Z (LEARNINGS #128 Front 3)."
    )


if __name__ == "__main__":
    demo()
