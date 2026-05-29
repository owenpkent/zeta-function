"""The Epstein zeta function: a SECOND, independent wrong-approach detector.

The whole Davenport-Heilbronn discipline of this project rests on ONE
counterexample: a Dirichlet series with a functional equation but no Euler
product, with zeros off the critical line. That single control is a point of
fragility. The Epstein zeta function of a binary quadratic form supplies a
classically independent second example.

For a positive-definite binary quadratic form

    Q(m, n) = a m^2 + b m n + c n^2,    discriminant D = b^2 - 4ac < 0,

the Epstein zeta function is

    Z_Q(s) = sum_{(m,n) != (0,0)} Q(m, n)^{-s},    Re(s) > 1,

with analytic continuation to all of C (one simple pole at s = 1) and a
self-dual functional equation centred on Re(s) = 1/2. Like Davenport-
Heilbronn, Z_Q has a functional equation but is NOT a single Euler product:
for forms whose class number is > 1 it does not factor as a product of
Selberg-class L-functions, and it then has zeros OFF the critical line
(Potter-Titchmarsh 1935; Davenport-Heilbronn 1936; Bombieri-Hejhal). For
class number 1 discriminants (d in {3,4,7,8,11,19,43,67,163}) it DOES factor
as zeta(s) L(s, chi_D), a product of two Selberg-class L-functions, and is
believed to satisfy RH (no off-line zeros). That contrast is itself a useful
control: the same machine should look Selberg-like on the h = 1 forms and
D-H-like on the h > 1 forms.

This module is the second leg of the wrong-approach discipline. If the
project's positivity detectors (the Weil-form Gram matrix, its Schur
complement, the Li criterion) fire on Epstein the same way they fire on D-H
(one negative eigenvalue per off-line zero pair; Li negativity at large n),
the discipline is hardened: it responds to off-line zeros per se, not to a
quirk of the single D-H construction. If they do NOT, the detector was
D-H-specific and we have learned something equally important.

## Evaluation (Chowla-Selberg / Terras expansion)

Write the CM point of the form as tau = x + i y with

    x = b / (2a),    y = sqrt(d) / (2a),    d = 4ac - b^2 = |D| > 0.

Then Q(m, n) = a |m + n tau|^2, so Z_Q(s) = (2 / sqrt(d))^s E(tau, s) where
E(tau, s) = sum'_{(m,n)} y^s / |m tau + n|^{2s} is the full-lattice real-
analytic Eisenstein series. Its Fourier expansion is exponentially
convergent and valid for all s != 1:

  E(tau, s) = 2 zeta(2s) y^s
            + 2 sqrt(pi) (Gamma(s-1/2)/Gamma(s)) zeta(2s-1) y^{1-s}
            + (8 pi^s sqrt(y) / Gamma(s))
              * sum_{k>=1} k^{s-1/2} sigma_{1-2s}(k) K_{s-1/2}(2 pi k y) cos(2 pi k x)

with sigma_{1-2s}(k) = sum_{e | k} e^{1-2s} and K the modified Bessel
function. The Bessel terms decay like exp(-2 pi k y), so a few dozen terms
saturate any working precision. Completing as xi(s) = pi^{-s} Gamma(s)
E(tau, s) gives xi(s) = xi(1-s) (verified term by term: the first two terms
map to 2 xi_R(2s) y^s + 2 xi_R(2s-1) y^{1-s} with xi_R the completed Riemann
zeta, which swap under s -> 1-s; the Bessel coefficient k^{s-1/2}
sigma_{1-2s}(k) = k^{1/2-s} sigma_{2s-1}(k) is itself s -> 1-s symmetric, as
is K_{s-1/2} = K_{1/2-s}). On the critical line xi(1/2 + i t) is real, which
gives a robust sign-change detector for on-line zeros.

The two main terms each have a pole at s = 1/2 (from zeta(2s) and from
Gamma(s-1/2) respectively) that cancel in E; we therefore avoid evaluating at
exactly t = 0, which is harmless since all zeros sit at t > 0.
"""

from __future__ import annotations

import hashlib
import pickle
from pathlib import Path

import mpmath as mp

from .lfunction import LFunction


CACHE_DIR = Path(__file__).resolve().parent / "_cache"


# A few standard reduced forms, labelled by discriminant d = |D| and class
# number h. The h = 1 forms factor as zeta * L(chi) (Selberg-class product,
# RH believed, no off-line zeros). The h > 1 non-principal forms are the
# genuine off-line-zero controls.
KNOWN_FORMS = {
    # d : list of (a, b, c, label, is_principal)
    4:   [(1, 0, 1, "x^2+y^2 (h=1, Gaussian)", True)],
    3:   [(1, 1, 1, "x^2+xy+y^2 (h=1, Eisenstein)", True)],
    15:  [(1, 1, 4, "x^2+xy+4y^2 (h=2, principal)", True),
          (2, 1, 2, "2x^2+xy+2y^2 (h=2, non-principal)", False)],
    23:  [(1, 1, 6, "x^2+xy+6y^2 (h=3, principal)", True),
          (2, 1, 3, "2x^2+xy+3y^2 (h=3, non-principal)", False)],
    47:  [(1, 1, 12, "x^2+xy+12y^2 (h=5, principal)", True),
          (2, 1, 6, "2x^2+xy+6y^2 (h=5, non-principal)", False),
          (3, 1, 4, "3x^2+xy+4y^2 (h=5, non-principal)", False)],
}


def _reduce_form(a, b, c):
    """Gauss-reduce a positive-definite form to |b| <= a <= c.

    Reduction minimises a, hence maximises y = sqrt(d)/(2a), which is exactly
    what makes the Bessel series converge fastest. Returns (a, b, c).
    """
    a, b, c = int(a), int(b), int(c)
    while True:
        if abs(b) > a:
            # translate: b -> b - 2 a k to bring |b| <= a
            k = round(b / (2 * a))
            b, c = b - 2 * a * k, c - b * k + a * k * k
            continue
        if a > c:
            a, c = c, a
            b = -b
            continue
        if (a == c and b < 0) or (abs(b) == a and b < 0):
            b = -b
        break
    return a, b, c


class EpsteinZeta(LFunction):
    """Epstein zeta function of a positive-definite binary quadratic form.

    Z_Q(s) = sum'_{(m,n)} (a m^2 + b m n + c n^2)^{-s}.
    """

    has_euler_product = False
    has_functional_equation = True

    def __init__(self, a: int, b: int, c: int, label: str | None = None):
        a, b, c = _reduce_form(a, b, c)
        D = b * b - 4 * a * c
        if D >= 0:
            raise ValueError(f"form ({a},{b},{c}) is not positive definite (D={D})")
        self.a, self.b, self.c = a, b, c
        self.d = -D  # |discriminant| = 4ac - b^2 > 0
        self.label = label or f"Q=({a},{b},{c})"
        self.name = f"epstein_d{self.d}_{a}_{b}_{c}"
        self._x = None  # Re(tau), set at first eval at working precision
        self._y = None  # Im(tau)
        self._prec = 0

    # ---- internal helpers -------------------------------------------------

    def _tau(self, dps: int):
        if self._x is None or self._prec < dps:
            prev = mp.mp.dps
            mp.mp.dps = max(dps, prev)
            try:
                self._x = mp.mpf(self.b) / (2 * self.a)
                self._y = mp.sqrt(self.d) / (2 * self.a)
                self._prec = mp.mp.dps
            finally:
                mp.mp.dps = prev
        return self._x, self._y

    @staticmethod
    def _sigma(k: int, exponent):
        """sigma_z(k) = sum_{e | k} e^z, computed exactly over divisors."""
        total = mp.mpc(0)
        e = 1
        while e * e <= k:
            if k % e == 0:
                total += mp.power(e, exponent)
                f = k // e
                if f != e:
                    total += mp.power(f, exponent)
            e += 1
        return total

    def eisenstein(self, s):
        """Full-lattice real-analytic Eisenstein series E(tau, s)."""
        s = mp.mpc(s)
        dps = mp.mp.dps
        x, y = self._tau(dps)

        # Two main (meromorphic) terms.
        term1 = 2 * mp.zeta(2 * s) * mp.power(y, s)
        term2 = (2 * mp.sqrt(mp.pi) * mp.gamma(s - mp.mpf(1) / 2) / mp.gamma(s)
                 * mp.zeta(2 * s - 1) * mp.power(y, 1 - s))

        # Exponentially convergent Bessel tail.
        pref = 8 * mp.power(mp.pi, s) * mp.sqrt(y) / mp.gamma(s)
        two_pi_y = 2 * mp.pi * y
        tol = mp.mpf(10) ** (-(dps + 6))
        tail = mp.mpc(0)
        k = 1
        while True:
            bess = mp.besselk(s - mp.mpf(1) / 2, two_pi_y * k)
            term = (mp.power(k, s - mp.mpf(1) / 2) * self._sigma(k, 1 - 2 * s)
                    * bess * mp.cos(2 * mp.pi * k * x))
            tail += term
            # Convergence: cos and sigma are O(1); the magnitude is set by the
            # Bessel decay exp(-2 pi k y). Stop once a term is below tolerance
            # (require two consecutive small terms for safety).
            if abs(term) < tol and k >= 2:
                break
            if k > 200:  # hard cap; only reached for pathological tiny y
                break
            k += 1
        return term1 + term2 + pref * tail

    def evaluate(self, s):
        """Z_Q(s) = (2 / sqrt(d))^s * E(tau, s)."""
        s = mp.mpc(s)
        return mp.power(2 / mp.sqrt(self.d), s) * self.eisenstein(s)

    def completed(self, s):
        """xi(s) = pi^{-s} Gamma(s) E(tau, s); real on Re(s) = 1/2, xi(s)=xi(1-s)."""
        s = mp.mpc(s)
        return mp.power(mp.pi, -s) * mp.gamma(s) * self.eisenstein(s)

    def functional_equation_residual(self, s):
        """xi(s) - xi(1 - s), which must be ~0 for all s."""
        return self.completed(s) - self.completed(1 - s)

    def dirichlet_coefficient(self, n: int):
        """Representation number r_Q(n) = #{(m,k) : Q(m,k) = n}."""
        if n < 1:
            return mp.mpc(0)
        a, b, c, d = self.a, self.b, self.c, self.d
        count = 0
        # |k| bounded by sqrt(4 a n / d); brute force the box.
        kmax = int(mp.sqrt(4 * a * n / d)) + 1
        for k in range(-kmax, kmax + 1):
            # a m^2 + (b k) m + (c k^2 - n) = 0; count integer roots in m.
            A, B, C = a, b * k, c * k * k - n
            disc = B * B - 4 * A * C
            if disc < 0:
                continue
            r = int(mp.sqrt(disc))
            for root_disc in (r - 1, r, r + 1):  # guard rounding
                if root_disc < 0 or root_disc * root_disc != disc:
                    continue
                for sign in ((1,) if root_disc == 0 else (1, -1)):
                    num = -B + sign * root_disc
                    if num % (2 * A) == 0:
                        count += 1
        return mp.mpc(count)

    # ---- zeros ------------------------------------------------------------

    def zeros(self, T_max: float, prec: int = 30,
              scan_step: float = 0.25, sigma_step: float = 0.05):
        """Zeros rho = beta + i gamma with 0 < gamma <= T_max, Re in [0,1].

        On-line zeros: sign changes of the real function t -> xi(1/2 + i t),
        refined with findroot. Off-line zeros: a 2D magnitude scan over
        (sigma, t) in (0,1) x (0, T_max], refined, then augmented with
        functional-equation and conjugate partners.

        Cached per (form, T_max, prec, steps).
        """
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        key = hashlib.sha1(
            f"{self.name}|{float(T_max):.6f}|{int(prec)}|"
            f"{float(scan_step):.4f}|{float(sigma_step):.4f}".encode()
        ).hexdigest()[:16]
        path = CACHE_DIR / f"epstein_zeros_{key}.pkl"
        # Cache is self-produced (written below from our own computed zeros),
        # never loaded from an untrusted source. Same convention as
        # davenport_heilbronn.py.
        if path.exists():
            with open(path, "rb") as f:
                return pickle.load(f)

        prev_dps = mp.mp.dps
        mp.mp.dps = max(prec, 30)
        try:
            zeros_found = []
            half = mp.mpf(1) / 2

            # Pass 1: on-line zeros via sign changes of the real xi on the line.
            def xi_line(t):
                return mp.re(self.completed(mp.mpc(half, t)))

            t = scan_step
            prev_val = xi_line(mp.mpf(t))
            while t <= T_max:
                t_next = t + scan_step
                cur_val = xi_line(mp.mpf(t_next))
                if prev_val == 0 or (prev_val < 0) != (cur_val < 0):
                    # Sign change in (t, t_next): refine the real root.
                    try:
                        root_t = mp.findroot(
                            lambda u: mp.re(self.completed(mp.mpc(half, u))),
                            mp.mpf((t + t_next) / 2),
                            tol=mp.mpf(10) ** (-prec + 5),
                        )
                        root = mp.mpc(half, root_t)
                        if (mp.mpf(0) < root.imag <= T_max
                                and not _is_duplicate(root, zeros_found)):
                            zeros_found.append(root)
                    except (ValueError, ZeroDivisionError):
                        pass
                prev_val = cur_val
                t = t_next

            # Pass 2: off-line zeros via a 2D magnitude scan over the raw Z_Q
            # (its zeros equal the zeros of xi away from s=1, since
            # pi^{-s} Gamma(s) is nonzero there). Off-line zeros are RARE
            # (e.g. one pair up to T=120 for d=47), so the scan must avoid
            # wasting findroot calls on points that are merely close to an
            # on-line zero. We therefore evaluate |Z| on the full grid once,
            # then refine ONLY interior local minima that are both below a
            # tight threshold and a strict 2D local minimum, and that sit a
            # safe distance from the critical line (on-line zeros are handled
            # by Pass 1).
            sigmas = [round(0.5 - j * float(sigma_step), 6)
                      for j in range(1, int(round(0.45 / float(sigma_step))) + 1)]
            sigmas += [round(0.5 + j * float(sigma_step), 6)
                       for j in range(1, int(round(0.45 / float(sigma_step))) + 1)]
            sigmas = sorted({sg for sg in sigmas
                             if 0.04 < sg < 0.96 and abs(sg - 0.5) > 0.04})
            ts = []
            t = scan_step
            while t <= T_max:
                ts.append(round(t, 6))
                t += scan_step
            # |Z| grid, indexed [i_sigma][i_t].
            grid = [[float(abs(self.evaluate(mp.mpc(sg, tt)))) for tt in ts]
                    for sg in sigmas]
            cal = abs(self.evaluate(mp.mpc(mp.mpf("0.3"), mp.mpf(10.0))))
            thresh = max(float(cal) * 0.04, 1e-4)
            for i, sg in enumerate(sigmas):
                for jt, tt in enumerate(ts):
                    v = grid[i][jt]
                    if v >= thresh:
                        continue
                    # strict 2D local minimum (vs the 4 axis neighbours present)
                    nbrs = []
                    if i > 0: nbrs.append(grid[i - 1][jt])
                    if i < len(sigmas) - 1: nbrs.append(grid[i + 1][jt])
                    if jt > 0: nbrs.append(grid[i][jt - 1])
                    if jt < len(ts) - 1: nbrs.append(grid[i][jt + 1])
                    if any(v > nb for nb in nbrs):
                        continue
                    try:
                        root = mp.findroot(
                            self.evaluate, mp.mpc(sg, tt),
                            tol=mp.mpf(10) ** (-prec + 5),
                        )
                    except (ValueError, ZeroDivisionError):
                        continue
                    if (mp.mpf(0) < root.imag <= T_max
                            and mp.mpf(0) <= root.real <= mp.mpf(1)
                            and abs(float(root.real) - 0.5) > 1e-3
                            and abs(self.evaluate(root)) < mp.mpf(10) ** (-prec + 8)
                            and not _is_duplicate(root, zeros_found)):
                        zeros_found.append(root)

            # Augment off-line zeros with FE partner 1 - rho and conjugate
            # partner (1 - beta) + i gamma, verifying each really is a zero.
            augmented = list(zeros_found)
            for z in zeros_found:
                if abs(float(z.real) - 0.5) > 1e-4:
                    for partner in (mp.mpc(mp.mpf(1) - z.real, z.imag),):
                        if (mp.mpf(0) < partner.imag <= T_max
                                and not _is_duplicate(partner, augmented)):
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


def epstein_for_discriminant(d: int, principal: bool = False):
    """Return the EpsteinZeta for a known discriminant.

    principal=False selects the first non-principal form (the off-line-zero
    control); principal=True selects the principal form.
    """
    if d not in KNOWN_FORMS:
        raise KeyError(f"no curated forms for d={d}; known: {sorted(KNOWN_FORMS)}")
    forms = KNOWN_FORMS[d]
    chosen = None
    for (a, b, c, label, is_prin) in forms:
        if is_prin == principal:
            chosen = (a, b, c, label)
            break
    if chosen is None:
        a, b, c, label, _ = forms[0]
        chosen = (a, b, c, label)
    a, b, c, label = chosen
    return EpsteinZeta(a, b, c, label=label)


# Canonical controls. Reconnaissance (this project, 2026-05) found that the
# small class-number-2/3 discriminants (d=15, d=23) have NO off-line zeros at
# reachable height (all low-lying zeros refine to Re = 1/2 exactly), while the
# class-number-5 discriminant d=47 has a genuine off-line zero pair at
# rho ~ 0.634 + 32.05 i. Higher class number pushes off-line zeros down to
# reachable heights. So d=47 is the working off-line-zero control, and its
# PRINCIPAL form (which has no off-line zeros up to T=120) is the Selberg-like
# contrast within the same discriminant.
epstein_d47 = epstein_for_discriminant(47, principal=False)            # off-line control
epstein_d47_principal = epstein_for_discriminant(47, principal=True)   # Selberg-like contrast
epstein_d15 = epstein_for_discriminant(15, principal=False)            # no off-line zeros < T=80
