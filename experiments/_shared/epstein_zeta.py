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

BESSEL-K CONVERGENCE HOLE, FOUND AND FIXED 2026-09-02. Overnight runs of six
experiments using the d=47 forms (class number 5; y = sqrt(47)/(2a) is small
enough at both a=1 and a=2 that 2 pi y ~ 10.8-21.5 is comparable to the
|Im(s)| values zeros() explores up to T_max=60) all died with
`mpmath.libmp.libhyper.NoConvergence` raised from inside mp.besselk, called
from eisenstein()'s Bessel tail. Root cause: mp.besselk picks its algorithm
from |x| ALONE (mpmath/functions/bessel.py: once mag(x) >= 1 it always uses
the large-argument asymptotic 2F0 series), with no regard for |nu|; that
series is only numerically valid once x is large relative to |nu| (past the
Bessel function's turning point), and mpmath correctly refuses to converge
below it rather than return a wrong answer. This module's own well-behaved
(nu, x) grid (any (sigma, t) actually swept by zeros(), t up to 200, sigma in
[-1, 2]) never hits this: it only surfaces when zeros()'s off-line findroot
refinement (Pass 2, the 2D-scan candidate refinement) overshoots its seed
during Newton/secant iteration, since x = 2 pi k y is pinned by k alone while
nu = s - 1/2 can pick up an excursion-driven |Im(nu)| or |Re(nu)| far outside
anything a sample grid would visit. Fix: `_besselk_robust()` tries
mp.besselk first (unchanged cost on the overwhelmingly common success path)
and, only on `NoConvergence`/`ValueError`/`ZeroDivisionError`, falls back to
the reflection formula

    K_nu(x) = (pi / 2) * (I_{-nu}(x) - I_nu(x)) / sin(pi nu),

built entirely from mp.besseli, whose series (DLMF 10.25.2) is
UNCONDITIONALLY convergent for every nu and x (no algorithm-selection blind
spot: mpmath uses the same series regardless of |x|). A first attempt at
this fallback used the more obvious DLMF 10.32.10 integral representation
K_nu(x) = int_0^inf exp(-x cosh t) cosh(nu t) dt instead; it was WRONG twice
over before landing on besseli, each time silently (no exception, just a
confidently wrong number), which is worth recording so nobody re-walks the
same path: (1) a plain `mp.quad(f, [0, U])` under-resolves the oscillation
in cosh(nu t) once |Im(nu)| is large (measured 45% relative error at
nu=60j, x=21.5) -- fixed by handing mp.quad explicit breakpoints spaced
within a fraction of one oscillation period; but (2) the integral itself
then turned out to need up to ~32 extra decimal guard digits at nu=60j,
x=21.5 (the pointwise integrand peaks around 1e-10 while the converged
integral is ~1e-42: that gap IS the cancellation, and no amount of
breakpoint refinement recovers digits the guard budget never allocated).
The besseli reflection formula sidesteps both failure modes directly: I_nu
and I_{-nu} are individually LARGE and only mildly cancel in the regime
where besselk's asymptotic series fails (verified 2026-09-02: lost digits
~0 at nu=60j/x=21.5 and nu=(200+200j)/x=10.77) -- which is exactly the
regime `_besselk_robust` calls this fallback in, since besselk's own
asymptotic series already succeeds everywhere else. The formula has its own
(mirror-image) cancellation regime -- I_nu and I_{-nu} become large and
NEARLY EQUAL once x is large relative to |nu| (measured ~34+ lost digits at
nu=60j, x=300, worse than a single precision-boost pass can safely recover)
-- but that is exactly the regime besselk's own asymptotic series already
handles correctly, so `_besselk_robust` never reaches the fallback there.
See `_besselk_robust`/`_besselk_via_besseli` below for the implementation,
the self-measured cancellation guard, and further validation notes.

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

ZEROS() REWRITTEN TO A WINDOWED ARGUMENT-PRINCIPLE CENSUS, 2026-09-02. The
old zeros() did a blind 2D grid of |Z| over sigma in (0.5, ...] x t in
(0, T_max] with Newton refinement that could overshoot to absurd points
(observed nu ~ -1.2e5 - 1.4e5 i, which is exactly what forced the besselk
fallback above) and took over an hour at T_max = 60 for the d = 47 forms.
It is replaced by the same discipline used in
experiments/criticality/e_euler_pencil.py (count_rect / count_line /
offline_zeros, ported below as `_count_rect` / `_count_line` /
`_offline_scan_window`): for width-10 windows [T1, T2] covering t in
[1, T_max] (starting past t = 0 to dodge the s = 1 pole), N_rect (the
winding number of evaluate() around [-1, 2] x [T1, T2]) minus N_line (sign
changes of the new Z(t) method on [T1, T2]) gives the window's off-line
zero count by the argument principle: COMPLETE (no zero, however shallow
or narrow its |Z| dip, can be missed by a grid step) and CHEAP (a window
with zero off-line zeros, the overwhelming majority, costs only the
contour + line work, a few hundred evaluations, not a 6000-point 2D grid).
The 2D |evaluate| local-minimum scan only runs inside a window whose count
is actually positive, and its Newton refinement is CLAMPED to that
window's box (any step landing outside sigma in [0.5, 2.0] or t outside
[T1 - 0.5, T2 + 0.5] is rejected and the step halved instead, abandoning
the seed after ~40 iterations): this is what prevents the old overshoot
incident from recurring, since a clamped iterate can no longer wander to a
|Im(nu)| the besselk fallback was built for. That fallback should now fire
rarely or never (see _BESSELK_FALLBACK_COUNT); it is kept as insurance,
not removed, since a clamped Newton step can still land near the box edge
where nu picks up a moderate imaginary part before _certify_offline (left
completely unchanged by this rewrite) rejects it.

MEASURED 2026-09-02 (full validation sweep: principal/non-principal d=15 to
T=40, principal/non-principal d=47 to T=70 and T=60, d=4 to T=60, plus the
e3l_epstein_control.py Gram/Schur run reusing those same cached results):
the besselk fallback fired ZERO times across every one of these runs
(_BESSELK_FALLBACK_COUNT stayed 0 throughout) -- the clamp above is doing
its job. The census also turned up a real dividend beyond speed: it is
COMPLETE where the old grid scan was not, and it found off-line zeros this
module's own prior ad-hoc probing had missed entirely. d=47 PRINCIPAL
(believed "Selberg-like, no off-line zeros" per the 2026-09-01 correction
above `epstein_d47 = ...`, which only checked up to the one pair it had
already stumbled on at 64.646629) in fact has off-line pairs at 24.658408,
29.377134, 44.432827 and 46.453511 as well -- FOUR pairs below height 60,
not zero. d=47 NON-PRINCIPAL similarly has two more pairs (43.520566,
47.535902) below T=60 beyond the previously known one at 32.050580. Every
one of these was independently certified (winding number 1 plus a
higher-precision magnitude recheck, `_certify_offline`, unchanged) and the
window-level census closed exactly (certified pairs accounted for every
predicted n_off, no fallback-grid retries, no warnings) in every window of
every run in this sweep. d=15 (both classes, T=40) and d=4 (T=60, the pure
Euler product control) matched their previously certified/expected counts
exactly. See PUBLICATIONS.md / e3l_epstein_control.py for the downstream
implication: e3l's own schur_neg law now correctly reports 4 off-line
heights for d=47 principal (previously an unnoticed false 0), which
*strengthens* rather than weakens 3L's result -- the detector was
never actually tested against that form's real off-line structure before.
"""

from __future__ import annotations

import cmath
import hashlib
import math
import pickle
import sys
from pathlib import Path

import mpmath as mp

from .lfunction import LFunction


CACHE_DIR = Path(__file__).resolve().parent / "_cache"

# Counts how many times _besselk_robust has had to fall back to
# _besselk_via_besseli (see the module docstring's 2026-09-02 note). Stays 0
# on every well-behaved evaluation; only fires on findroot's rare excursions.
_BESSELK_FALLBACK_COUNT = 0

# How many decimal digits of self-measured cancellation to tolerate from the
# fallback's first pass before re-deriving it at boosted precision. Set from
# the validated regime (see module docstring): a genuine fallback call
# (besselk already failed, so we are below the turning point) measured
# ~0 lost digits; double-digit loss would mean we somehow landed in the
# fallback's own hard regime (x large relative to |nu|), which should be
# unreachable since besselk succeeds there on its own.
_BESSELK_FALLBACK_MAX_LOST_DIGITS = 10


def _besselk_via_besseli(nu, x):
    """K_nu(x) via the reflection formula, built entirely from mp.besseli.

        K_nu(x) = (pi / 2) * (I_{-nu}(x) - I_nu(x)) / sin(pi nu)

    mp.besseli's series (DLMF 10.25.2) is UNCONDITIONALLY convergent for
    every complex nu and x: unlike mp.besselk, it does not branch to a
    divergent asymptotic series based on |x| alone (see the module
    docstring), so it has none of besselk's algorithm-selection blind spot.

    This has its own cancellation regime, but the MIRROR IMAGE of besselk's:
    I_{-nu}(x) and I_nu(x) are individually large and nearly equal (so their
    difference cancels badly) once x is large relative to |nu| -- exactly
    the regime where besselk's own asymptotic series already succeeds, so
    `_besselk_robust` never calls this path there. It is well conditioned
    exactly in the complementary regime (x small relative to |nu|) that
    besselk fails in and this function exists to cover.

    Returns (value, lost_digits): lost_digits is a cheap self-diagnostic,
    the decimal digits apparently consumed by cancellation in
    I_{-nu}(x) - I_nu(x) relative to max(|I_nu|, |I_{-nu}|), so the caller
    can detect (and react to) landing outside the well-conditioned regime
    instead of silently trusting a cancelled-out result.
    """
    Ip = mp.besseli(nu, x)
    Im_ = mp.besseli(-nu, x)
    diff = Im_ - Ip
    scale = max(abs(Ip), abs(Im_), mp.mpf(1))
    lost_digits = mp.mp.dps if diff == 0 else max(
        0, int(mp.ceil(mp.log10(scale / abs(diff))))
    )
    sinpi = mp.sin(mp.pi * nu)
    return mp.pi / 2 * diff / sinpi, lost_digits


def _besselk_robust(nu, x):
    """K_nu(x), falling back to _besselk_via_besseli on non-convergence.

    See the module docstring's 2026-09-02 note for why mp.besselk can raise
    NoConvergence here even though the underlying Bessel function is
    perfectly well defined. The try is free on the success path (the
    overwhelming majority of calls); only a failing call pays the fallback's
    cost. A ValueError/ZeroDivisionError guard is included alongside
    NoConvergence because the same underlying cause (an ill-conditioned
    hypergeometric evaluation) has been observed to surface as either in
    mpmath depending on which internal code path is hit.

    The fallback re-derives its own answer at boosted precision if its
    self-measured cancellation (see _besselk_via_besseli) exceeds
    _BESSELK_FALLBACK_MAX_LOST_DIGITS: this should not trigger in practice
    (see that function's docstring) but is cheap insurance against landing
    outside the validated regime, rather than silently returning a
    cancelled-out value. If even the boosted pass does not clear the bar,
    the best available estimate is returned with a loud stderr warning
    (any resulting bad root candidate is still caught downstream by
    zeros()'s own independent, higher-precision _certify_offline check).
    """
    global _BESSELK_FALLBACK_COUNT
    try:
        return mp.besselk(nu, x)
    except (mp.libmp.NoConvergence, ValueError, ZeroDivisionError):
        _BESSELK_FALLBACK_COUNT += 1
        if _BESSELK_FALLBACK_COUNT == 1:
            print(
                f"[epstein_zeta] besselk fallback to besseli's reflection "
                f"formula engaged (nu={complex(nu)!r}, x={float(x)!r}); see "
                f"module docstring, 2026-09-02 note.",
                file=sys.stderr,
            )
        val, lost_digits = _besselk_via_besseli(nu, x)
        if lost_digits <= _BESSELK_FALLBACK_MAX_LOST_DIGITS:
            return val
        prev_dps = mp.mp.dps
        try:
            mp.mp.dps = prev_dps + 2 * lost_digits + 20
            val2, lost2 = _besselk_via_besseli(mp.mpc(nu), mp.mpf(x))
            val2 = +val2
        finally:
            mp.mp.dps = prev_dps
        if lost2 > _BESSELK_FALLBACK_MAX_LOST_DIGITS:
            print(
                f"[epstein_zeta] WARNING: besselk fallback could not clear "
                f"its cancellation guard at nu={complex(nu)!r}, "
                f"x={float(x)!r} (lost_digits={lost_digits} then {lost2} "
                f"after boosting precision by {2 * lost_digits + 20} "
                f"digits); returning the best available estimate. This "
                f"regime was not exercised by the module's 2026-09-02 "
                f"validation -- see module docstring.",
                file=sys.stderr,
            )
        return val2


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
                bess = _besselk_robust(s - mp.mpf(1) / 2, two_pi_y * k)
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

    def Z(self, t) -> float:
        """Real part of completed(1/2 + i t).

        Real by the functional equation with root number +1 (see the
        module docstring's derivation of xi(s) = xi(1-s)): on Re(s) = 1/2,
        s and 1-s are complex conjugates, so xi(1/2+it) = xi(1-(1/2+it)) =
        xi(1/2-it) = conj(xi(1/2+it)) forces xi(1/2+it) real. Added
        2026-09-02 for the windowed argument-principle census in zeros():
        duck-typed the same way experiments/criticality/e_euler_pencil.py's
        EulerPencil.Z is, so `_count_line` below can be a direct port.
        """
        val = self.completed(mp.mpc(mp.mpf(1) / 2, mp.mpf(t)))
        re, im = mp.re(val), mp.im(val)
        scale = max(abs(re), mp.mpf(1))
        assert abs(im) < mp.mpf(10) ** -10 * scale, (
            f"{self.name}.completed(1/2+i*{float(t)!r}) has non-negligible "
            f"imaginary part {float(im)!r} (real part {float(re)!r}); "
            f"expected ~0 by the s -> 1-s functional equation on the line"
        )
        return float(re)

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
              scan_step: float | None = None, sigma_step: float = 0.05):
        """Zeros rho = beta + i gamma with 0 < gamma <= T_max, Re in [0,1].

        2026-09-02 REWRITE: windowed argument-principle census (see the
        module docstring's dated note). For width-10 windows [T1, T2]
        covering t in [1, T_max] (starting at t=1 to dodge the s=1 pole):

            N_rect = winding number of evaluate() around [-1,2] x [T1,T2]
            N_line = sign changes of Z(t) on [T1,T2]  (= on-line zero count)
            n_off  = N_rect - N_line                  (must be even, >= 0)

        This is COMPLETE (the argument principle cannot miss a zero the way
        a grid step can) and CHEAP (a window with n_off = 0, the ordinary
        case, costs only the contour + line work). The expensive 2D
        |evaluate| local-minimum scan over sigma in (0.5, 2.0] x t in
        [T1, T2] runs ONLY inside a window with n_off > 0, and its Newton
        refinement is CLAMPED to that window's box (t in [T1-0.5, T2+0.5],
        sigma in [0.5, 2.0]): see `_newton_clamped`. Certified candidates
        (via the unchanged `_certify_offline`) are augmented with their
        functional-equation partner 1 - conj(rho).

        `scan_step` is the on-line sign-change step. eisenstein()'s cost is
        ~0.1-0.25s per call (a Bessel series, unchanged by this rewrite),
        so a flat fine step (the old 0.25 default; even the naively "safe"
        0.05) is not just too coarse/fine in the wrong direction, it is the
        dominant COST driver: at T_max=200 a flat 0.05 step alone would be
        ~4000 evaluations before a single window's contour is even walked.
        Left at its default (None), the step is instead DERIVED per window
        from the local mean spacing of a degree-2, conductor-d L-function,
        pi / log(T sqrt(|d|) / (2 pi)) (measured ~0.6-2.8 across the ranges
        this module is validated on), divided by 6 for a comfortable safety
        margin and clipped to [0.05, 0.5]; `_count_line`'s own "local
        minimum lacking a sign change" fallback still catches any close
        pair the base step is coarser than. Passing an explicit float
        forces that FIXED step for every window instead (compatibility
        with existing call sites that relied on a constant `scan_step`).
        `sigma_step` is the 2D off-line-scan SIGMA grid step, only paid
        inside a window with n_off > 0. It stays at the spec's literal
        0.05: measurement (2026-09-02) showed the sigma direction is where
        a coarsened grid actually loses zeros (a 0.15 sigma step missed
        every one of a known window's 3 off-line pairs outright: not
        "found imprecisely", found NONE), reproducing exactly the
        2026-09-01 recall bug this module's own docstring already
        documents for a shallow/narrow dip. The T direction is far more
        forgiving: the historical record for that same case (see the dated
        correction above `epstein_d47 = ...`) shows the dip WAS found at
        the OLD code's default t-spacing of 0.25 with sigma at 0.05, so
        the 2D grid here uses sigma_step x 0.2 (close to that proven value,
        a little finer) rather than sigma_step x sigma_step: for a
        width-10 window that is 30 x 50 = 1500 calls (~4 minutes) instead
        of 30 x 200 = 6000 (~15 minutes), paid only when n_off > 0. If that
        pass still certifies fewer pairs than the census predicts, the
        window is retried ONCE at sigma_step/2 x 0.05 before warning.

        On-line zeros are returned as 1/2 + i*gamma (gamma bisected to
        1e-10 by `_count_line`); off-line zeros as beta + i*gamma and their
        FE partners. All zeros with 0 < gamma <= T_max, sorted by gamma.

        Cached per (form, T_max, prec, steps); cache key suffix 'census1'.
        """
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        key = hashlib.sha1(
            f"{self.name}|{float(T_max):.6f}|{int(prec)}|"
            f"{'auto' if scan_step is None else format(float(scan_step), '.4f')}|"
            f"{float(sigma_step):.4f}|census1".encode()
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
            on_line_heights = []   # mp.mpf gamma values
            off_line = []          # certified mp.mpc zeros (both FE partners)

            T1_start = mp.mpf(1) if float(T_max) > 1.0 else mp.mpf(T_max) / 2
            windows = []
            t = T1_start
            while t < T_max:
                t2 = min(t + 10, mp.mpf(T_max))
                windows.append((t, t2))
                t = t2

            for (Wa, Wb) in windows:
                Wa_f, Wb_f = float(Wa), float(Wb)
                step = (scan_step if scan_step is not None
                        else _mean_spacing_step(self.d, (Wa_f + Wb_f) / 2))
                try:
                    n_rect = _count_rect(self, Wa_f, Wb_f)
                except RuntimeError as exc:
                    print(f"[epstein_zeta] {self.name} window [{Wa_f},{Wb_f}]: "
                          f"{exc}; treating this window as unresolved and "
                          f"running the off-line scan defensively.",
                          file=sys.stderr)
                    n_rect = None
                n_line, line_heights = _count_line(self, Wa_f, Wb_f, step=step)

                n_off = None if n_rect is None else n_rect - n_line
                if n_off is not None and (n_off < 0 or n_off % 2 != 0):
                    # Refine both counts once, at finer settings, before
                    # giving up (per spec: "raise or warn loudly ... and
                    # refine both counts once before giving up").
                    n_line_r, line_heights_r = _count_line(
                        self, Wa_f, Wb_f, step=step / 4)
                    try:
                        n_rect_r = _count_rect(
                            self, Wa_f, Wb_f, threshold0=0.25, density0=0.1)
                    except RuntimeError:
                        n_rect_r = n_rect
                    n_off_r = n_rect_r - n_line_r
                    if n_off_r < 0 or n_off_r % 2 != 0:
                        print(
                            f"[epstein_zeta] WARNING: {self.name} window "
                            f"[{Wa_f},{Wb_f}] gives an invalid off-line "
                            f"count even after refinement (N_rect={n_rect_r}, "
                            f"N_line={n_line_r}, n_off={n_off_r}); clamping "
                            f"to the nearest valid even count and continuing.",
                            file=sys.stderr,
                        )
                        n_off_r = max(0, n_off_r - (n_off_r % 2))
                    n_rect, n_line, line_heights, n_off = (
                        n_rect_r, n_line_r, line_heights_r, n_off_r)

                on_line_heights.extend(line_heights)
                print(f"[epstein_zeta] {self.name} window [{Wa_f:.1f},{Wb_f:.1f}]: "
                      f"N_rect={n_rect} N_line={n_line} n_off={n_off}",
                      file=sys.stderr)

                if n_off is None:
                    n_off = 0  # unresolved rectangle count: fall through
                    # to a defensive scan below without a count to match.
                    run_scan = True
                else:
                    run_scan = n_off > 0

                if run_scan:
                    certified = _offline_scan_window(
                        self, Wa_f, Wb_f, sigma_step, prec, t_step=0.2)
                    if n_off and 2 * len(certified) != n_off:
                        # Fall back to a finer grid IN THIS WINDOW ONLY: the
                        # "fall back to a finer grid" the spec calls for,
                        # paid only on the rare window where the default
                        # pass did not resolve every zero the census
                        # predicted (see zeros()'s docstring).
                        certified_fine = _offline_scan_window(
                            self, Wa_f, Wb_f, sigma_step / 2, prec, t_step=0.05)
                        if 2 * len(certified_fine) == n_off:
                            certified = certified_fine
                        else:
                            print(
                                f"[epstein_zeta] WARNING: {self.name} window "
                                f"[{Wa_f},{Wb_f}]: census predicts n_off="
                                f"{n_off} off-line zero(s) but the 2D scan "
                                f"certified {len(certified)} pair(s) at the "
                                f"default grid and {len(certified_fine)} "
                                f"pair(s) at a finer grid; using the larger "
                                f"of the two.",
                                file=sys.stderr,
                            )
                            certified = (certified_fine
                                         if len(certified_fine) > len(certified)
                                         else certified)
                    for root in certified:
                        if not _is_duplicate(root, off_line):
                            off_line.append(root)
                        partner = mp.mpc(1) - mp.conj(root)
                        if not _is_duplicate(partner, off_line):
                            off_line.append(partner)

            zeros_found = []
            half = mp.mpf(1) / 2
            for g in on_line_heights:
                g = mp.mpf(g)
                if mp.mpf(0) < g <= T_max:
                    zeros_found.append(mp.mpc(half, g))
            for z in off_line:
                if mp.mpf(0) < z.imag <= T_max and not _is_duplicate(z, zeros_found):
                    zeros_found.append(z)
            zeros_found = sorted(zeros_found, key=lambda r: float(r.imag))
        finally:
            mp.mp.dps = prev_dps

        with open(path, "wb") as f:
            pickle.dump(zeros_found, f)
        return zeros_found


def _mean_spacing_step(d: int, T_mid: float, safety: float = 6.0,
                        lo: float = 0.05, hi: float = 0.5) -> float:
    """Adaptive on-line sign-change step for _count_line, from the local
    mean zero spacing of a degree-2, conductor-d L-function,
    pi / log(T sqrt(|d|) / (2 pi)), divided by `safety` and clipped to
    [lo, hi]. See zeros()'s docstring for why a flat fine step is not
    affordable here (eisenstein() costs ~0.1-0.25s/call): this keeps the
    step comfortably sub-spacing (a `safety`-fold margin) while not paying
    for far more resolution than the local zero density needs. Falls back
    to `hi` when the asymptotic formula's argument is too small to trust
    (low T, or a small T*sqrt(d) product).
    """
    x = T_mid * math.sqrt(d) / (2 * math.pi)
    if x <= math.e:
        return hi
    spacing = math.pi / math.log(x)
    return min(hi, max(lo, spacing / safety))


def _count_rect(L, T1: float, T2: float, sigma_lo: float = -1.0, sigma_hi: float = 2.0,
                 threshold0: float = 1.0, density0: float = 0.3) -> int:
    """Winding number of L.evaluate around [sigma_lo,sigma_hi] x [T1,T2], T1>0.

    Ported 2026-09-02 from experiments/criticality/e_euler_pencil.py's
    count_rect (see that module for the discovery notes this adaptive
    scheme encodes: flat point density silently undercounts a tall box,
    and a coarse phase-increment threshold can alias a near-2pi turn to
    near-zero). Adaptive boundary sampling: bisect any edge whose phase
    increment exceeds `threshold`, until every increment is below it; if
    the resulting total/(2 pi) is not within 1e-3 of an integer, halve the
    threshold and density and retry. `threshold0`/`density0` let a caller
    force a finer starting point for a refinement pass.
    """
    def f(sigma, t):
        v = L.evaluate(mp.mpc(sigma, t))
        return complex(float(v.real), float(v.imag))

    def boundary_points(density):
        corners = [(sigma_lo, T1), (sigma_hi, T1), (sigma_hi, T2), (sigma_lo, T2), (sigma_lo, T1)]
        pts = []
        for i in range(4):
            p0, p1 = corners[i], corners[i + 1]
            length = math.hypot(p1[0] - p0[0], p1[1] - p0[1])
            n_edge = max(10, int(math.ceil(length / density)))
            for k in range(n_edge):
                frac = k / n_edge
                pts.append((p0[0] + (p1[0] - p0[0]) * frac, p0[1] + (p1[1] - p0[1]) * frac))
        pts.append(pts[0])
        return pts

    # eisenstein() costs ~0.1-0.25s/call (unchanged by this rewrite), so
    # these constants are tuned down from e_euler_pencil's (whose flint
    # backend is orders of magnitude cheaper): a coarser initial density
    # (0.3 vs 0.1) plus a lower per-edge floor (10 vs 20) cut the common
    # case (few or no off-line zeros in the window) from several hundred
    # to several dozen evaluations, while the same adaptive bisection
    # safety net (below) still densifies wherever the phase actually turns
    # fast -- which is where it matters, not everywhere uniformly.
    MAX_POINTS = max(1500, int(250 * (T2 - T1)))
    threshold = threshold0
    density = density0
    n = None
    for _ in range(6):
        pts = boundary_points(density)
        vals = [f(*p) for p in pts]
        changed = True
        capped = False
        while changed:
            changed = False
            new_pts, new_vals = [pts[0]], [vals[0]]
            for i in range(len(pts) - 1):
                v0, v1 = vals[i], vals[i + 1]
                inc = abs(cmath.phase(v1 / v0)) if v0 != 0 and v1 != 0 else 2 * threshold
                if inc > threshold and len(new_pts) < MAX_POINTS:
                    mid = ((pts[i][0] + pts[i + 1][0]) / 2, (pts[i][1] + pts[i + 1][1]) / 2)
                    new_pts.append(mid)
                    new_vals.append(f(*mid))
                    changed = True
                elif inc > threshold:
                    capped = True
                new_pts.append(pts[i + 1])
                new_vals.append(vals[i + 1])
            pts, vals = new_pts, new_vals
            if len(pts) >= MAX_POINTS:
                break
        total = sum(cmath.phase(vals[i + 1] / vals[i]) for i in range(len(vals) - 1))
        n = total / (2 * math.pi)
        if not capped and abs(n - round(n)) < 1e-3:
            return round(n)
        threshold /= 2
        density /= 2
    raise RuntimeError(
        f"_count_rect did not converge to an integer winding number for "
        f"t in [{T1},{T2}] (last estimate {n})"
    )


def _count_line(L, T1: float, T2: float, step: float = 0.05):
    """(count, sorted located on-line zero heights) of L.Z on [T1, T2].

    Ported 2026-09-02 from experiments/criticality/e_euler_pencil.py's
    count_line. Base pass at `step`; any local minimum of |Z| lacking a
    sign change on either side is re-scanned at step/20 (close pairs the
    coarse grid could straddle without a sign flip). Located zeros are
    bisected to 1e-10.
    """
    n_steps = max(1, round((T2 - T1) / step))
    ts = [T1 + i * step for i in range(n_steps + 1)]
    zvals = [L.Z(t) for t in ts]

    def refine(ta, tb):
        # Ridder's method: still bracketing (same robustness guarantee as
        # bisection: the root stays trapped in [ta,tb] throughout, so it
        # cannot jump to a wrong nearby root the way secant/Newton could),
        # but superlinear instead of linear -- measured ~10 evaluations
        # instead of bisection's ~35 to reach the same 1e-10 from a
        # 0.4-wide bracket. Substituted for plain bisect 2026-09-02 because
        # L.Z() costs ~0.1-0.25s/call here (unlike e_euler_pencil's cheap
        # flint-backed Z), so evaluation count directly drives wall time.
        return float(mp.findroot(lambda x: L.Z(float(x)), (ta, tb), solver="ridder", tol=1e-10))

    zeros_t = []
    for i in range(len(ts) - 1):
        za, zb = zvals[i], zvals[i + 1]
        if za == 0.0:
            zeros_t.append(ts[i])
        elif (za < 0) != (zb < 0):
            zeros_t.append(refine(ts[i], ts[i + 1]))

    fine_step = step / 20
    for i in range(1, len(ts) - 1):
        if abs(zvals[i]) < abs(zvals[i - 1]) and abs(zvals[i]) < abs(zvals[i + 1]):
            has_change = ((zvals[i - 1] < 0) != (zvals[i] < 0)) or ((zvals[i] < 0) != (zvals[i + 1] < 0))
            if not has_change:
                tt, prevv = ts[i - 1], zvals[i - 1]
                while tt < ts[i + 1] - 1e-15:
                    tn = min(tt + fine_step, ts[i + 1])
                    curv = L.Z(tn)
                    if (prevv < 0) != (curv < 0):
                        zeros_t.append(refine(tt, tn))
                    prevv, tt = curv, tn

    zeros_t = sorted({round(z, 9) for z in zeros_t})
    return len(zeros_t), zeros_t


def _newton_clamped(evalfn, seed, box, prec: int, max_iter: int = 40):
    """Newton-refine evalfn's root from `seed`, iterate CLAMPED to `box`.

    box = (sigma_lo, sigma_hi, t_lo, t_hi). A Newton step landing outside
    the box is REJECTED and the step halved instead of taken. This is the
    guard against the 2026-09 overshoot incident recorded in the module
    docstring (Newton wandering to nu ~ -1.2e5 - 1.4e5 i): a clamped
    iterate cannot leave the window it was found in, so it cannot
    manufacture that kind of absurd argument for eisenstein()'s Bessel
    tail. The derivative is estimated with mp.diff (adaptive,
    full-precision), not a naive finite difference.

    BUG FOUND AND FIXED 2026-09-02, first cut of this function: `tol` was
    set to 10**(-prec-5) (1e-35 at the default prec=30), tighter than
    eisenstein()'s own achievable absolute precision at that working dps
    (bottoms out around 1e-28 to 1e-30, per its "guard=15" digit margin) --
    so |f0| < tol was NEVER satisfied, the loop always burned all
    `max_iter` iterations chasing rounding noise it could never clear, and
    every seed returned None even when Newton had already converged to the
    true root in under 10 steps (quadratic convergence: each step
    ~doubles the number of correct digits, so 0.1 -> 1e-25ish takes about
    6-7 steps, not 40). This is why a real, visually obvious local minimum
    (e.g. |evaluate| = 0.1245 at (0.70, 20.4), a strict local min next to
    known off-line zero 0.69559+20.34597i) still refined to `None`. Fixed
    by loosening `tol` to a value comfortably reachable at the working
    precision, and by tracking the best (smallest |f|) iterate seen so a
    seed that stops improving just short of `tol` (rounding-limited, not
    divergent) is still returned rather than discarded outright --
    `_certify_offline` (independent, its own winding number plus a
    HIGHER-precision magnitude recheck) is the actual accept/reject gate
    downstream, so returning a "best effort" candidate here costs nothing
    but a rejected print if it turns out not to be a genuine root.
    """
    sigma_lo, sigma_hi, t_lo, t_hi = box
    s = mp.mpc(seed)
    tol = mp.mpf(10) ** -(prec - 2)
    accept_floor = mp.mpf(10) ** -8  # certify_offline's own gate is 1e-10;
    # this only needs to be close enough that certify's OWN refinement
    # (same-precision winding check plus a higher-precision recheck) has a
    # real candidate to work with, not exactly below 1e-10 itself.
    scale = mp.mpf(1)
    best_s, best_abs = s, None
    for _ in range(max_iter):
        try:
            f0 = evalfn(s)
        except (ValueError, ZeroDivisionError, mp.libmp.NoConvergence):
            break
        af0 = abs(f0)
        if best_abs is None or af0 < best_abs:
            best_s, best_abs = s, af0
        if af0 < tol:
            return s
        try:
            fp = mp.diff(evalfn, s)
        except (ValueError, ZeroDivisionError, mp.libmp.NoConvergence):
            break
        if fp == 0:
            break
        delta = f0 / fp
        accepted = False
        local_scale = scale
        while local_scale > mp.mpf(10) ** -10:
            candidate = s - local_scale * delta
            csig, ct = float(mp.re(candidate)), float(mp.im(candidate))
            if sigma_lo <= csig <= sigma_hi and t_lo <= ct <= t_hi:
                s = candidate
                accepted = True
                break
            local_scale /= 2
        if not accepted:
            break
    return best_s if best_abs is not None and best_abs < accept_floor else None


def _offline_scan_window(L, Wa: float, Wb: float, sigma_step: float, prec: int,
                          t_step: float = 0.05, margin: float = 0.5):
    """Certified off-line zeros (beta > 1/2 only) of L inside window [Wa,Wb].

    2D local-minimum scan of |L.evaluate| over sigma in (0.5, 2.0] (step
    sigma_step) x t in [Wa, Wb] (step t_step), each strict local minimum
    Newton-refined with `_newton_clamped` against the box sigma in
    [0.5, 2.0], t in [Wa - margin, Wb + margin], deduplicated, then run
    through the unchanged `_certify_offline`. The caller adds each
    certified root's FE partner 1 - conj(rho); this only returns the
    beta > 1/2 member of each pair.
    """
    sigmas = []
    sg = 0.5 + sigma_step
    while sg <= 2.0 + 1e-9:
        sigmas.append(round(sg, 6))
        sg += sigma_step
    ts = []
    t = Wa
    while t <= Wb + 1e-9:
        ts.append(round(t, 6))
        t += t_step

    grid = [[float(abs(L.evaluate(mp.mpc(sg, tt)))) for tt in ts] for sg in sigmas]
    box = (0.5, 2.0, Wa - margin, Wb + margin)

    certified = []
    for i, sg in enumerate(sigmas):
        for j, tt in enumerate(ts):
            v = grid[i][j]
            nbrs = []
            if i > 0: nbrs.append(grid[i - 1][j])
            if i < len(sigmas) - 1: nbrs.append(grid[i + 1][j])
            if j > 0: nbrs.append(grid[i][j - 1])
            if j < len(ts) - 1: nbrs.append(grid[i][j + 1])
            if nbrs and any(v > nb for nb in nbrs):
                continue
            root = _newton_clamped(L.evaluate, mp.mpc(sg, tt), box, prec)
            if root is None:
                continue
            rb, rt = float(mp.re(root)), float(mp.im(root))
            if not (0.5 < rb <= 2.0 and box[2] <= rt <= box[3]):
                continue
            if _is_duplicate(root, certified):
                continue
            accepted, winding, zval, zval_hi = L._certify_offline(root)
            if accepted:
                certified.append(root)
            else:
                print(
                    f"[epstein_zeta] rejected off-line candidate "
                    f"{complex(root)!r} for {L.name} in window [{Wa},{Wb}]: "
                    f"winding={winding}, |Z|={float(zval):.3e}, "
                    f"|Z|@higher-prec="
                    f"{'n/a' if zval_hi is None else format(float(zval_hi), '.3e')}",
                    file=sys.stderr,
                )
    return certified


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
# UPDATE (2026-09-02): the census-based zeros() finds SEVEN off-line pairs of
# the d=47 principal form below T=70 (24.658, 29.377, 44.433, 46.454, 64.647,
# 66.138, 69.889) and THREE of the non-principal form below T=60 (32.051,
# 43.521, 47.536); the 2026-09-01 note below, written from the single
# certified pair at 64.647, understated the count.
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
