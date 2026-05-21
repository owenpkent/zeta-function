"""The Davenport-Heilbronn L-function: our wrong-approach detector.

Davenport and Heilbronn (1936) constructed a Dirichlet series

    f(s) = sum_n c_n / n^s

with coefficients c_n periodic mod 5, that satisfies a Riemann-style
functional equation but has zeros off the critical line. Because it has
no Euler product, it lies outside the Selberg class, and any RH-style
method that "proves" all its zeros are on the critical line is wrong.

Construction: c_n is periodic with period 5, and one period is

    (c_1, c_2, c_3, c_4, c_5) = (1, kappa, -kappa, -1, 0)

where

    kappa = (sqrt(10 - 2 sqrt(5)) - 2) / (sqrt(5) - 1) ~= 0.2841

is the unique value making the functional equation hold. (See
Titchmarsh, "The Theory of the Riemann Zeta Function", 2nd ed., section
on Davenport-Heilbronn, or Iwaniec-Kowalski Analytic Number Theory.)

Evaluation uses the Hurwitz zeta representation
    f(s) = 5^{-s} sum_{a=1}^5 c_a * zeta_Hurwitz(s, a/5)
which gives analytic continuation to all of C.

Known facts we use as numerical sanity checks:
  - f satisfies f(s) = chi_DH(s) f(1 - s) for a known chi_DH built from
    Gamma factors and powers of 5/pi.
  - f has infinitely many zeros on Re(s) = 1/2 (Selberg, Levinson-style
    results).
  - f has infinitely many zeros off Re(s) = 1/2 (Davenport-Heilbronn
    original result). The smallest off-line zero pair is in the upper
    half plane near gamma ~ 85.7 with beta noticeably different from
    1/2; this is established numerically when we run zeros().
"""

from __future__ import annotations

import hashlib
import pickle
from pathlib import Path

import mpmath as mp

from .lfunction import LFunction


CACHE_DIR = Path(__file__).resolve().parent / "_cache"


def _kappa(dps: int = 50):
    """The Davenport-Heilbronn constant kappa = tan(theta)."""
    prev = mp.mp.dps
    mp.mp.dps = max(dps, prev)
    try:
        sqrt5 = mp.sqrt(5)
        num = mp.sqrt(10 - 2 * sqrt5) - 2
        den = sqrt5 - 1
        return num / den
    finally:
        mp.mp.dps = prev


class DavenportHeilbronn(LFunction):
    name = "davenport_heilbronn"
    has_euler_product = False
    has_functional_equation = True

    def __init__(self):
        self._kappa_cache = None
        self._kappa_dps = 0

    def _coeffs(self, dps: int):
        if self._kappa_cache is None or self._kappa_dps < dps:
            self._kappa_cache = _kappa(dps)
            self._kappa_dps = dps
        k = self._kappa_cache
        # Period-5 coefficients (c_1, c_2, c_3, c_4, c_5)
        return [mp.mpf(1), k, -k, mp.mpf(-1), mp.mpf(0)]

    def dirichlet_coefficient(self, n: int):
        if n < 1:
            return mp.mpc(0)
        return mp.mpc(self._coeffs(mp.mp.dps)[(n - 1) % 5])

    def evaluate(self, s):
        s = mp.mpc(s)
        c = self._coeffs(mp.mp.dps)
        # f(s) = 5^{-s} * sum_{a=1..5} c[a-1] * zeta(s, a/5)
        five_pow = mp.power(5, -s)
        total = mp.mpc(0)
        for a in range(1, 6):
            total += c[a - 1] * mp.zeta(s, mp.mpf(a) / 5)
        return five_pow * total

    def functional_equation_residual(self, s):
        """Return f(s) - chi_DH(s) * f(1 - s), which should be ~0.

        Uses the conjectural form for an odd character mod 5:
            chi_DH(s) = (pi/5)^(s - 1/2) * Gamma((1 - s + 1)/2) / Gamma((s + 1)/2)
        i.e. the gamma factor for an odd character of conductor 5.

        Numerical zero of this residual across many s is our sanity test
        that we have implemented the right object.
        """
        s = mp.mpc(s)
        gamma_ratio = mp.gamma((1 - s + 1) / 2) / mp.gamma((s + 1) / 2)
        chi = mp.power(mp.pi / 5, s - mp.mpf(1) / 2) * gamma_ratio
        return self.evaluate(s) - chi * self.evaluate(1 - s)

    def zeros(self, T_max: float, prec: int = 30, scan_step: float = 0.5):
        """Find zeros with 0 < Im(s) <= T_max in a 2D strip Re(s) in [0, 1].

        Strategy:
          1. Scan along the critical line Re(s) = 1/2 at step scan_step
             to find sign changes / minima; refine to high precision.
          2. Scan a coarse 2D grid over (sigma, t) in [0.05, 0.95] x
             (0, T_max] at step scan_step, looking for off-line zeros.
             At each grid corner, evaluate |f|; if any cell minimum is
             below threshold, refine with mp.findroot.

        Caches results per (T_max, prec).

        This is intentionally not the most efficient method; correctness
        first, performance later. For T_max <= 200 it runs in seconds.
        """
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        key = hashlib.sha1(
            f"dh|{float(T_max):.6f}|{int(prec)}|{float(scan_step):.4f}".encode()
        ).hexdigest()[:16]
        path = CACHE_DIR / f"dh_zeros_{key}.pkl"
        if path.exists():
            with open(path, "rb") as f:
                return pickle.load(f)

        prev_dps = mp.mp.dps
        mp.mp.dps = max(prec, 30)
        try:
            zeros_found = []

            # Pass 1: critical-line scan via sign of Re(Z(t)) where
            # Z(t) = f(1/2 + i t) * exp(i theta(t)) would be the analogue
            # of Riemann-Siegel; for now we just scan |f(1/2 + i t)| for
            # local minima below threshold and refine.
            t = scan_step
            prev_abs = float(abs(self.evaluate(mp.mpc(mp.mpf(1) / 2, mp.mpf(t)))))
            while t <= T_max:
                t_next = t + scan_step
                cur_abs = float(
                    abs(self.evaluate(mp.mpc(mp.mpf(1) / 2, mp.mpf(t_next))))
                )
                # Heuristic: a local minimum below 0.5 likely flags a zero
                # within scan_step. Refine.
                if cur_abs < 0.5 and cur_abs < prev_abs:
                    try:
                        root = mp.findroot(
                            self.evaluate,
                            mp.mpc(mp.mpf(1) / 2, mp.mpf(t_next)),
                            tol=mp.mpf(10) ** (-prec + 5),
                        )
                        if (
                            mp.mpf(0) < root.imag <= T_max
                            and not _is_duplicate(root, zeros_found)
                        ):
                            zeros_found.append(root)
                    except (ValueError, ZeroDivisionError):
                        pass
                prev_abs = cur_abs
                t = t_next

            # Pass 2: 2D scan for off-line zeros over (sigma, t)
            sigmas = [mp.mpf(s) / 100 for s in range(10, 95, 10)]
            t = scan_step
            while t <= T_max:
                for sigma in sigmas:
                    s_try = mp.mpc(sigma, t)
                    val = abs(self.evaluate(s_try))
                    if float(val) < 0.3:
                        try:
                            root = mp.findroot(
                                self.evaluate,
                                s_try,
                                tol=mp.mpf(10) ** (-prec + 5),
                            )
                            if (
                                mp.mpf(0) < root.imag <= T_max
                                and mp.mpf(0) <= root.real <= mp.mpf(1)
                                and not _is_duplicate(root, zeros_found)
                            ):
                                zeros_found.append(root)
                        except (ValueError, ZeroDivisionError):
                            pass
                t += scan_step

            # Augment with functional-equation + conjugate partner of
            # any off-line zero found. If rho = beta + i*gamma is a zero
            # with beta != 1/2, then 1 - rho is a zero (functional eq.)
            # and conjugates are zeros (real Dirichlet coefficients), so
            # 1 - rho_bar = (1 - beta) + i*gamma is also in the upper
            # half plane. The scan may miss this partner; augment.
            augmented = list(zeros_found)
            for z in zeros_found:
                if abs(float(z.real) - 0.5) > 0.01:
                    partner = mp.mpc(mp.mpf(1) - z.real, z.imag)
                    if (
                        mp.mpf(0) < partner.imag <= T_max
                        and not _is_duplicate(partner, augmented)
                    ):
                        # Verify it really is a zero before adding
                        if abs(self.evaluate(partner)) < mp.mpf(10) ** (-prec + 10):
                            augmented.append(partner)
            zeros_found = sorted(augmented, key=lambda r: float(r.imag))
        finally:
            mp.mp.dps = prev_dps

        with open(path, "wb") as f:
            pickle.dump(zeros_found, f)
        return zeros_found


def _is_duplicate(root, found, tol: float = 1e-6):
    for r in found:
        if abs(float(root.real - r.real)) < tol and abs(float(root.imag - r.imag)) < tol:
            return True
    return False


davenport_heilbronn = DavenportHeilbronn()
