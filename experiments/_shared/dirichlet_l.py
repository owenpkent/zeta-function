"""Dirichlet L-functions as LFunction objects.

A real, primitive Dirichlet character mod q gives an L-function inside
the Selberg class: it has an Euler product, a functional equation, and
GRH is believed. This module exposes it so the proof-architecture
experiments can run as a positive control alongside zeta (Selberg class,
RH believed) and Davenport-Heilbronn (functional equation only, RH known
false).

Implementation notes:
  - Evaluation uses the Hurwitz zeta representation
        L(s, chi) = q^{-s} sum_{a=1}^q chi(a) zeta(s, a/q),
    which analytically continues to all of C (with the usual pole at
    s = 1 only when chi is principal; we exclude principal characters).
  - Zero finding uses a Z-function sign-change scan on the critical
    line. For a real primitive character chi the completed L-function
        Lambda(s, chi) = (q/pi)^{(s + a)/2} Gamma((s + a)/2) L(s, chi)
    (with a in {0, 1} the parity) is real on the critical line up to
    W(chi) = +-1, so Z_chi(t) := e^{i theta(t)} L(1/2 + it, chi) with
        theta(t) = (t/2) log(q/pi) + Im log Gamma((1/2 + i t + a)/2)
    is real. Sign changes of Z_chi locate the zeros; we refine with
    findroot.
  - We only support real characters (Kronecker symbols). For complex
    characters the L-function takes complex values on the line and the
    Gram-matrix construction would no longer have phi_b(rho) real.

Provided instances:
  - chi3_L: the unique non-trivial character mod 3 (odd, real, conductor 3)
            First zero gamma ~ 8.0397.
  - chi4_L: the unique non-trivial character mod 4 (odd, real, conductor 4)
            First zero gamma ~ 6.0209.
"""

from __future__ import annotations

import hashlib
import pickle
from pathlib import Path
from typing import Sequence

import mpmath as mp

from .lfunction import LFunction


CACHE_DIR = Path(__file__).resolve().parent / "_cache"


class DirichletL(LFunction):
    """L-function attached to a real primitive Dirichlet character.

    Parameters
    ----------
    coeffs : sequence of length modulus
        coeffs[a] = chi(a) for a in {0, 1, ..., modulus - 1}. Must satisfy
        coeffs[0] = 0 (chi(0) = 0) and coeffs[a] in {-1, 0, 1}.
    modulus : int
        The conductor q.
    name : str, optional
        Human-readable name for printouts.
    """

    has_euler_product = True
    has_functional_equation = True

    def __init__(self, coeffs: Sequence, modulus: int, name: str = None):
        if len(coeffs) != modulus:
            raise ValueError(f"coeffs length {len(coeffs)} != modulus {modulus}")
        if coeffs[0] != 0:
            raise ValueError("coeffs[0] must be 0 (chi(0) = 0)")
        for c in coeffs:
            if c not in (-1, 0, 1):
                raise ValueError(f"coeff {c} not in {{-1, 0, 1}}; complex characters not supported")
        self._coeffs_int = [int(c) for c in coeffs]
        self._modulus = modulus
        chi_neg1 = self._coeffs_int[(modulus - 1) % modulus]
        if chi_neg1 == 1:
            self._parity = 0  # even
        elif chi_neg1 == -1:
            self._parity = 1  # odd
        else:
            raise ValueError("chi(-1) = 0 (character not primitive)")
        self.name = name or f"dirichlet_mod{modulus}"

    @property
    def modulus(self) -> int:
        return self._modulus

    @property
    def parity(self) -> int:
        return self._parity

    def dirichlet_coefficient(self, n: int):
        if n < 1:
            return mp.mpc(0)
        return mp.mpc(self._coeffs_int[n % self._modulus])

    def evaluate(self, s):
        s = mp.mpc(s)
        q = self._modulus
        total = mp.mpc(0)
        for a in range(1, q + 1):
            c = self._coeffs_int[a % q]
            if c == 0:
                continue
            total += c * mp.zeta(s, mp.mpf(a) / q)
        return mp.power(q, -s) * total

    def functional_equation_residual(self, s):
        """Lambda(s, chi) - W(chi) Lambda(1-s, chi), should be ~0.

        For a real primitive character of conductor q and parity a,
            Lambda(s) = (q/pi)^{(s+a)/2} Gamma((s+a)/2) L(s, chi)
        and Lambda(s) = W Lambda(1-s) with W = +-1. We do not assume W
        and return the residual for W = +1 and W = -1; the smaller in
        modulus is the true root sign.
        """
        s = mp.mpc(s)
        q = self._modulus
        a = self._parity
        Lam_s = mp.power(q / mp.pi, (s + a) / 2) * mp.gamma((s + a) / 2) * self.evaluate(s)
        Lam_1ms = mp.power(q / mp.pi, (1 - s + a) / 2) * mp.gamma((1 - s + a) / 2) * self.evaluate(1 - s)
        return Lam_s - Lam_1ms, Lam_s + Lam_1ms  # (W=+1 residual, W=-1 residual)

    def _theta(self, t):
        """Phase theta(t) = (t/2) log(q/pi) + Im log Gamma((1/2 + i t + a)/2)."""
        t = mp.mpf(t)
        q = self._modulus
        a = self._parity
        return (t / 2) * mp.log(mp.mpf(q) / mp.pi) + mp.loggamma(
            (mp.mpf(1) / 2 + mp.mpc(0, t) + a) / 2
        ).imag

    def Z(self, t):
        """Z_chi(t) = e^{i theta(t)} L(1/2 + i t, chi), real for real chi."""
        s = mp.mpc(mp.mpf(1) / 2, t)
        return (mp.exp(mp.mpc(0, self._theta(t))) * self.evaluate(s)).real

    def zeros(self, T_max: float, prec: int = 30, scan_step: float = 0.25):
        """Critical-line zeros 0 < gamma <= T_max via Z(t) sign changes.

        Since GRH is believed, we only scan the critical line. Each sign
        change of Z(t) yields a zero; we refine with mp.findroot. Cached
        to disk per (T_max, prec, scan_step).
        """
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        key = hashlib.sha1(
            f"{self.name}|q{self._modulus}|p{self._parity}|"
            f"{float(T_max):.6f}|{int(prec)}|{float(scan_step):.4f}".encode()
        ).hexdigest()[:16]
        path = CACHE_DIR / f"{self.name}_zeros_{key}.pkl"
        if path.exists():
            with open(path, "rb") as f:
                return pickle.load(f)

        prev_dps = mp.mp.dps
        mp.mp.dps = max(prec, 30)
        try:
            zeros_found = []
            t = mp.mpf(scan_step)
            z_prev = self.Z(t)
            t_prev = t
            while t <= T_max:
                t_next = t + scan_step
                z_next = self.Z(t_next)
                if z_prev * z_next < 0:
                    try:
                        # Refine with bisection-then-findroot for stability
                        gamma = mp.findroot(
                            lambda x: self.Z(x),
                            (t_prev, t_next),
                            solver="bisect",
                            tol=mp.mpf(10) ** (-prec + 5),
                        )
                        rho = mp.mpc(mp.mpf(1) / 2, gamma)
                        if (
                            mp.mpf(0) < rho.imag <= T_max
                            and not _is_duplicate(rho, zeros_found)
                        ):
                            zeros_found.append(rho)
                    except (ValueError, ZeroDivisionError):
                        pass
                z_prev = z_next
                t_prev = t_next
                t = t_next
            zeros_found = sorted(zeros_found, key=lambda r: float(r.imag))
        finally:
            mp.mp.dps = prev_dps

        with open(path, "wb") as f:
            pickle.dump(zeros_found, f)
        return zeros_found


def _is_duplicate(root, found, tol: float = 1e-6):
    for r in found:
        if abs(float(root.imag - r.imag)) < tol:
            return True
    return False


# Built-in instances for the small-conductor real primitive characters used
# as Selberg-class positive controls in the proof-architecture experiments.

# chi_3: Kronecker symbol (./-3), conductor 3, odd, real primitive.
#   chi_3(1) = 1, chi_3(2) = -1, chi_3(0) = 0.
chi3_L = DirichletL(coeffs=[0, 1, -1], modulus=3, name="chi3")

# chi_4: Kronecker symbol (./-4), conductor 4, odd, real primitive.
#   chi_4(1) = 1, chi_4(3) = -1, chi_4(2) = chi_4(0) = 0.
chi4_L = DirichletL(coeffs=[0, 1, 0, -1], modulus=4, name="chi4")
