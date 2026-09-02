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

ACCURACY DEFECT, FOUND AND FIXED 2026-09-01. eisenstein()'s Bessel-tail loop
stopped once several consecutive terms fell below a fixed ABSOLUTE tolerance,
but each term is later multiplied by the prefactor 8 pi^s sqrt(y) / Gamma(s),
whose magnitude grows like exp(pi |Im(s)| / 2). For nu = s - 1/2 with
|Im(nu)| = |Im(s)| = t, the terms K_nu(2 pi k y) do not decay with k until
2 pi k y exceeds roughly t: below that they are merely tiny in absolute terms
(not yet converging), so the old loop mistook "small" for "converged" and
quit after 1-2 terms once t was large enough. This was accurate to ~1e-30 at
mp.dps = 30 below about t = 45-50 but returned a smooth, WRONG function
(complete with its own fake zeros) from about t = 50-60 upward: relative
error against an independent evaluation was already 3e-20 at t = 50, 0.45 at
t = 60, and of order 1 for every t from 60 to 200 tested. Every tracked
Epstein result computed at |Im(s)| above ~50 PREDATES this fix and should be
treated as unreliable; results below that height are unaffected. The fix
(see eisenstein()'s own docstring) makes the loop run until k passes the
Bessel cutoff t / (2 pi y) plus a decay margin, and judges convergence on
each term's contribution after the prefactor, not before it.
"""

from __future__ import annotations

import hashlib
import pickle
import sys
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
        """Full-lattice real-analytic Eisenstein series E(tau, s).

        CORRECTION (2026-09-01): see the module docstring's dated note for the
        accuracy defect this replaces. Two changes from the old loop, both
        required:

        (a) The Bessel tail is OSCILLATORY, not decaying, until k exceeds
            roughly |Im(s)| / (2 pi y): for nu = s - 1/2, |Im(nu)| = |Im(s)|,
            and K_nu(2 pi k y) does not enter its exponential-decay regime
            until the argument 2 pi k y exceeds the order's imaginary part.
            The loop must not even START checking for convergence before
            that point, let alone stop there.
        (b) Convergence must be judged on the term's contribution AFTER the
            prefactor (8 pi^s sqrt(y) / Gamma(s), which grows like
            exp(pi |Im(s)| / 2) via 1/Gamma(s)) is applied, relative to the
            running total in that same scale -- not the bare pre-prefactor
            term against a fixed absolute tolerance. The bare term can be
            astronomically tiny (measured ~1e-138 at k=1, t=200) while its
            scaled contribution is still order 1, which is exactly what let
            the old loop quit after 1-2 terms at large |Im(s)|.

        A modest fixed guard-digit margin is used for the internal working
        precision (restored before returning). Measured 2026-09-01: mpmath's
        besselk/gamma/zeta already retain full relative precision at dps=30
        for these parameters regardless of magnitude (checked against an
        independent higher-precision evaluation up to |Im(s)|=200: besselk
        relative error ~1e-32 at dps=30 whether its value is ~1 or ~1e-138),
        so the dominant defect was purely the truncation logic above, not
        per-term precision loss. A guard budget that scales with |Im(s)| the
        way the prefactor does (~pi t / (2 ln 10) extra digits) was measured
        too: it costs 5-10x more wall time per evaluation at t=200 for no
        accuracy gain over this fixed margin in the range validated here, so
        it was not adopted as the default.
        """
        s = mp.mpc(s)
        target_dps = mp.mp.dps
        t_im = abs(mp.im(s))
        guard = 15
        prev_dps = mp.mp.dps
        mp.mp.dps = target_dps + guard
        try:
            x, y = self._tau(mp.mp.dps)

            # Two main (meromorphic) terms.
            term1 = 2 * mp.zeta(2 * s) * mp.power(y, s)
            term2 = (2 * mp.sqrt(mp.pi) * mp.gamma(s - mp.mpf(1) / 2) / mp.gamma(s)
                     * mp.zeta(2 * s - 1) * mp.power(y, 1 - s))

            # Exponentially convergent Bessel tail.
            pref = 8 * mp.power(mp.pi, s) * mp.sqrt(y) / mp.gamma(s)
            two_pi_y = 2 * mp.pi * y
            # Do not even look for convergence before k passes the Bessel
            # cutoff |Im(s)| / (2 pi y), plus enough further steps for the
            # post-cutoff exponential decay (rate ~2 pi y per step) to reach
            # the working precision.
            decay_margin = int(mp.ceil(mp.mp.dps * mp.log(10) / two_pi_y)) + 5
            min_k = int(mp.ceil(t_im / two_pi_y)) + decay_margin
            tol = mp.mpf(10) ** (-(mp.mp.dps - 2))
            tail = mp.mpc(0)
            k = 1
            recent = []
            while True:
                bess = mp.besselk(s - mp.mpf(1) / 2, two_pi_y * k)
                term = (mp.power(k, s - mp.mpf(1) / 2) * self._sigma(k, 1 - 2 * s)
                        * bess * mp.cos(2 * mp.pi * k * x))
                tail += term
                # Convergence in the FINAL scale: cos and sigma are O(1), but
                # the physically meaningful quantity is term * pref against
                # the partial sum * pref, not the bare term against a fixed
                # absolute floor (see (b) above). Still require several
                # CONSECUTIVE small contributions: when x = b/(2a) is a "nice"
                # rational (e.g. x = 1/4 for the form (2,1,2), discriminant
                # 15), cos(2 pi k x) vanishes exactly for one parity of k,
                # producing a spuriously tiny contribution while the OTHER
                # parity's terms are still significant.
                contrib = abs(term * pref)
                scale = max(mp.mpf(1), abs(tail * pref))
                recent.append(contrib / scale)
                if len(recent) > 4:
                    recent.pop(0)
                if k >= min_k and len(recent) >= 4 and max(recent) < tol:
                    break
                if k > 2000:  # hard cap; only reached for pathological tiny y
                    break
                k += 1
            result = term1 + term2 + pref * tail
        finally:
            mp.mp.dps = prev_dps
        return +result  # round back down to the caller's working precision

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

    def _certify_offline(self, root):
        """Certify a Newton-refined off-line candidate before accepting it.

        Two independent checks, BOTH required:

        1. Winding number 1 around a small circle at the current working
           precision (catches Newton converging to a nearby non-zero local
           minimum of |Z| rather than an actual root).

        2. |Z(root)| re-evaluated at substantially HIGHER precision than the
           candidate was found at. This catches a second, different failure
           mode discovered while hardening this method: eisenstein()'s
           Bessel-tail loop stops once several consecutive terms fall below
           an ABSOLUTE tolerance, but the terms are then multiplied by the
           prefactor 8 pi^s sqrt(y) / Gamma(s), whose magnitude grows like
           exp(pi |Im(s)| / 2) (from 1/Gamma(s)). At large |Im(s)| the
           absolute check can therefore declare "converged" after too few
           terms, leaving a self-consistent but WRONG value. Both Newton's
           method and a same-precision winding check are fooled identically,
           because they interrogate the same under-converged function. Re-
           evaluating at higher precision forces the tail to run further and
           exposes the discrepancy: a genuine root stays near zero, a
           precision artifact does not. (evaluate/completed/eisenstein
           themselves are left untouched; this only adds a verification
           step around them.)

        Returns (accepted, winding, |Z| at working precision, |Z| at the
        higher check precision or None if the first check already failed).
        """
        zval = abs(self.evaluate(root))
        winding = _winding_number(self.evaluate, root)
        if not (winding == 1 and zval < mp.mpf(10) ** -10):
            return False, winding, zval, None
        prev_dps = mp.mp.dps
        mp.mp.dps = prev_dps + 30
        try:
            zval_hi = abs(self.evaluate(root))
        finally:
            mp.mp.dps = prev_dps
        accepted = zval_hi < mp.mpf(10) ** -6
        return accepted, winding, zval, zval_hi

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
            f"{float(scan_step):.4f}|{float(sigma_step):.4f}|cert3".encode()
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
            # RECALL FIX (2026-09-01): this used to also require v < thresh
            # (an absolute cutoff calibrated from a single reference point,
            # cal = |Z(0.3+10i)| * 0.04). That rejected genuine off-line
            # zeros with a shallow/narrow dip: measured for d=15 principal,
            # the true zero at 0.69559+20.34597i (|Z| ~ 9e-6 at the exact
            # root) sampled on the grid at 0.70+20.25i as |Z| = 0.2142, a
            # strict 2D local minimum, but ABOVE thresh = 0.1040 -- so it was
            # never even tried as a Newton seed and the zero was silently
            # missed (a recall bug, separate from and downstream of the
            # accuracy bug above: this height is well under the ~50 cutoff
            # where the accuracy bug bites). Strict 2D local-minimality alone
            # is now the filter; findroot's own exception handling plus the
            # magnitude/winding/higher-precision certification below reject
            # the local minima that are not actually near a root.
            for i, sg in enumerate(sigmas):
                for jt, tt in enumerate(ts):
                    v = grid[i][jt]
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
                        # Newton refinement alone is not sufficient: it can
                        # converge to a nearby local minimum of |Z| that is
                        # small but never zero, or to a zero of eisenstein()'s
                        # own under-converged Bessel tail at large |Im(s)|.
                        # Certify with an independent winding-number count
                        # PLUS a higher-precision magnitude re-check before
                        # accepting it as a genuine off-line zero (see
                        # _certify_offline).
                        accepted, winding, zval, zval_hi = self._certify_offline(root)
                        if accepted:
                            zeros_found.append(root)
                        else:
                            print(
                                f"[epstein_zeta] rejected off-line candidate "
                                f"{complex(root)!r} for {self.name}: "
                                f"winding={winding}, |Z|={float(zval):.3e}, "
                                f"|Z|@higher-prec="
                                f"{'n/a' if zval_hi is None else format(float(zval_hi), '.3e')}",
                                file=sys.stderr,
                            )

            # Augment off-line zeros with FE partner 1 - rho and conjugate
            # partner (1 - beta) + i gamma, verifying each really is a zero.
            augmented = list(zeros_found)
            for z in zeros_found:
                if abs(float(z.real) - 0.5) > 1e-4:
                    for partner in (mp.mpc(mp.mpf(1) - z.real, z.imag),):
                        if (mp.mpf(0) < partner.imag <= T_max
                                and not _is_duplicate(partner, augmented)):
                            paccepted, pwinding, pzval, pzval_hi = self._certify_offline(partner)
                            if paccepted:
                                augmented.append(partner)
                            else:
                                print(
                                    f"[epstein_zeta] rejected FE-partner "
                                    f"candidate {complex(partner)!r} for "
                                    f"{self.name}: winding={pwinding}, "
                                    f"|Z|={float(pzval):.3e}, |Z|@higher-prec="
                                    f"{'n/a' if pzval_hi is None else format(float(pzval_hi), '.3e')}",
                                    file=sys.stderr,
                                )
            zeros_found = sorted(augmented, key=lambda r: float(r.imag))
        finally:
            mp.mp.dps = prev_dps

        with open(path, "wb") as f:
            pickle.dump(zeros_found, f)
        return zeros_found


def _winding_number(func, rho, r=0.05, n0: int = 240, max_doublings: int = 5):
    """Winding number of `func` around the circle of radius r centred at rho.

    Independent of Newton's method: a spurious candidate that findroot
    converges to (a nearby local minimum of |func| that is small but never
    zero, rather than an actual root) has winding number 0, not 1, so this
    catches exactly the failure mode Newton refinement cannot see on its
    own. Refines the sample count (doubling) until every consecutive phase
    increment along the circle is below 1 radian, per the discipline that
    a coarse phase-increment estimate of the argument principle is only
    trustworthy once each step is well inside one full turn.
    """
    rho = mp.mpc(rho)
    n = n0
    total = mp.mpf(0)
    for _ in range(max_doublings):
        pts = [rho + mp.mpc(r) * mp.expjpi(2 * mp.mpf(k) / n) for k in range(n + 1)]
        vals = [func(p) for p in pts]
        if any(v == 0 for v in vals):
            r = r * mp.mpf("1.0000001")
            continue
        total = mp.mpf(0)
        max_step = mp.mpf(0)
        for k in range(n):
            dphi = mp.arg(vals[k + 1] / vals[k])
            total += dphi
            if abs(dphi) > max_step:
                max_step = abs(dphi)
        if max_step < 1:
            break
        n *= 2
    return int(mp.nint(total / (2 * mp.pi)))


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
#
# CORRECTION (2026-09-01). The "d=15, d=23 have NO off-line zeros" sentence
# above was tested only against the NON-PRINCIPAL forms (this module's
# epstein_d15 and epstein_for_discriminant(23)); it is FALSE for BOTH classes
# of d=15. An independent winding-number certifier plus a rectangle-contour
# (argument-principle) census, cross-checked against a second, gated
# evaluation (mpmath Hurwitz-zeta route, independent of this module),
# certifies FOUR off-line zeros below T=40 for the PRINCIPAL form
# (x^2+xy+4y^2): 0.80001+12.03860i, 0.92746+15.49663i, 0.69559+20.34597i,
# 0.74026+33.75685i (each with functional-equation partner 1-beta+i*gamma);
# and ONE for the NON-PRINCIPAL form (2x^2+xy+2y^2, epstein_d15 below):
# 0.75807+24.48282i. The old zeros() scan both INVENTED a spurious root
# (principal form, near 0.700741+84.76354i: winding number 1 and
# |Z| ~ 2e-29 to 2e-30 when evaluated at the SAME working precision the
# candidate was found at, but re-evaluating eisenstein() at 30 MORE digits
# of working precision drives |Z| to O(1) instead of toward zero, so it was
# never a genuine root -- a precision artifact of the Bessel-tail
# convergence check below, not a Newton-refinement fluke) and MISSED three
# genuine ones (principal: 20.35, 33.76; non-principal: 24.48 -- the 2D
# magnitude scan's grid/threshold can step over a shallow or narrow dip).
# zeros() now certifies every candidate it DOES find with a winding-number
# count plus a higher-precision magnitude re-check (see _certify_offline)
# before returning it, which fixes the false positive; the false negatives
# (the scan's RECALL) are a separate, open issue this fix does not address.
#
# SEPARATE FINDING (2026-09-01): the "d=47 PRINCIPAL form has no off-line
# zeros up to T=120, Selberg-like contrast" sentence above is ALSO false.
# The same certification (winding number 1, |Z| stable and shrinking from
# ~1.5e-29 at 30 digits to ~6e-64 at 90 digits under Newton re-refinement)
# confirms a genuine off-line zero pair at rho ~ 0.724531+64.646629i (and
# 0.275469+64.646629i). This sits above the T_max=60 used for this form in
# e3l_epstein_control.py, so 3L's own recorded schur_neg=0 result for
# epstein_d47_principal is unaffected, but the "Selberg-like control" framing
# (h=47 is prime, so genus theory gives no 2-term split of the class group;
# neither class's Epstein zeta has a structural reason to satisfy RH) does
# not hold and should not be relied on beyond the T_max actually tested.
epstein_d47 = epstein_for_discriminant(47, principal=False)            # off-line control
epstein_d47_principal = epstein_for_discriminant(47, principal=True)   # off-line pair at T~64.6 (see correction); PSD-looking only for T_max<=60
epstein_d15 = epstein_for_discriminant(15, principal=False)            # HAS an off-line pair at T~24.48 (see correction); old comment was wrong
