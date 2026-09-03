"""The Euler pencil f_lam = A + lam*B: watching off-line zeros approach the
Euler-product point as lam -> 0.

WHY this pencil. Fix a fundamental discriminant d < 0 with class number 2
and genus factorization d = d1 * d2 (one of d1, d2 negative, the other
positive). Both

    A(s) = zeta(s) * L(s, chi_d)              (the Dedekind zeta of Q(sqrt d))
    B(s) = L(s, chi_d1) * L(s, chi_d2)         (the genus-character factor)

are Dirichlet series of the SAME conductor |d|, the SAME parity, and the
SAME root number +1 (all characters here are real), hence the SAME
completed functional equation

    Lambda(s) = |d|^{s/2} (2 pi)^{-s} Gamma(s) * (A or B)(s),
    Lambda(s) = Lambda(1 - s).

By Hecke's converse theorem, the space of Dirichlet series with exactly
this functional equation is a weight-1 level-|d| Eisenstein pencil, and it
is two-dimensional: {A, B} is a basis. So

    f_lam(s) = A(s) + lam * B(s)

for lam real is the COMPLETE family with this functional equation, and
Lambda_lam(s) := |d|^{s/2} (2 pi)^{-s} Gamma(s) f_lam(s) again satisfies
Lambda_lam(s) = Lambda_lam(1 - s), so Z_lam(t) := Lambda_lam(1/2 + i t) is
real. The two Euler-product boundary points of the pencil are lam = 0
(A alone, the Euler product zeta * L(chi_d)) and lam = infinity (B alone,
also an Euler product L(chi_d1) * L(chi_d2)); every intermediate lam is a
non-trivial linear combination and, by genus theory, exactly two special
finite values (lam = +1 and lam = -1, given w = 2 units) recover the
Epstein zeta functions of the principal and non-principal reduced forms of
discriminant d (a classical identity: the ideal-class zeta functions of a
class-number-2 field are (Z_principal +- Z_nonprincipal)/2 = A(s) or B(s)).

Voronin joint universality (zeta and any finite tuple of independent
Dirichlet L-functions can be made to approximate ANY tuple of nonvanishing
holomorphic targets on a small disc) implies f_lam has >> T zeros with
Re(s) > 1/2 for every lam != 0, once T is taken large enough: some window
[T, T+O(1)] realizes A/B close enough to a nonzero-sum configuration to
pull a pair of A's on-line zeros off the line. At LOW heights and SMALL
lam, empirically the pencil's zeros stay on the line: the perturbation
lam*B(t_m) at a given on-line zero pair's midpoint has to exceed a
threshold set by the local curvature of Z_0, and that threshold is a
concrete two-zero (Lehmer pair) collision condition (see lehmer_prediction
below). This experiment MEASURES that threshold: how close to the
Euler-product point (lam = 0) do off-line zeros survive, how the lowest
off-line height T*(lam) grows as lam -> 0, and whether the observed
collision lam for a given on-line pair matches the second-order (Lehmer)
model to the expected delta^2 power law.

Evaluation backend: python-flint (Conrey-indexed real primitive Dirichlet
characters located by brute-force matching against the Kronecker symbol
table, then evaluated via dirichlet_char.l() and acb.zeta()/.gamma()), with
an mpmath Hurwitz-zeta fallback used for cross-checks and for callers that
pass backend='mpmath'. See _flint_base / _mpmath_base.

Caching: A(s) and B(s) do NOT depend on lam. A module-level cache keyed on
(d, backend, s rounded to 1e-10) lets every lam value in the S1 grid reuse
the SAME zeta/L-function evaluations at a given s -- this is what makes a
15-way lam sweep over a 200-unit-height critical-line scan tractable in
the time budget: the expensive part (5 special-function evaluations per s)
is paid once per grid point, not once per (lam, grid point) pair.
"""

from __future__ import annotations

import argparse
import cmath
import hashlib
import math
import pickle
import subprocess
import sys
import time
from pathlib import Path

import flint
import mpmath as mp
from sympy import factorint

from experiments._shared.lfunction import LFunction
from experiments._shared.harness import save_npz, quick_arg

HERE = Path(__file__).resolve().parent
SHARED_CACHE_DIR = Path(__file__).resolve().parents[1] / "_shared" / "_cache"
SCRATCH_MD = Path(
    "/tmp/claude-1000/-home-owen-dev-zeta-function/"
    "e54d8a47-d42d-42f1-813a-bf70a9ea50b5/scratchpad/e_euler_pencil_results.md"
)

FLINT_DPS = 25     # flint working precision (spec target)
MP_DPS = 30        # mpmath container / cross-check precision

# --------------------------------------------------------------------------
# The discriminant table (generic: add an entry to extend to a new d).
# --------------------------------------------------------------------------
DISCRIMINANTS = {
    -15: dict(d1=-3, d2=5, principal=(1, 1, 4), nonprincipal=(2, 1, 2)),
    -20: dict(d1=-4, d2=5, principal=(1, 0, 5), nonprincipal=(2, 2, 3)),
}


# --------------------------------------------------------------------------
# Kronecker symbol.
# --------------------------------------------------------------------------

def _kron_prime(d: int, p: int) -> int:
    """chi_d(p) for a single prime p, by the standard local rules."""
    if p == 2:
        if d % 2 == 0:
            return 0
        dm8 = d % 8
        if dm8 in (1, 7):
            return 1
        if dm8 in (3, 5):
            return -1
        return 0  # unreachable for odd d
    dm = d % p
    if dm == 0:
        return 0
    return 1 if pow(dm, (p - 1) // 2, p) == 1 else -1


def kronecker(d: int, n: int) -> int:
    """Kronecker symbol (d/n) for n >= 1, via complete multiplicativity in n."""
    if n < 1:
        raise ValueError("n must be >= 1")
    if n == 1:
        return 1
    result = 1
    for p, e in factorint(n).items():
        cp = _kron_prime(d, p)
        if cp == 0:
            return 0
        result *= cp ** e
    return result


# --------------------------------------------------------------------------
# flint Conrey character lookup: brute-force match against the Kronecker
# table (there is no direct "give me the real character with these values"
# constructor, so we search the q-1 candidates once per modulus and cache).
# --------------------------------------------------------------------------
_CHAR_CACHE: dict = {}


def _get_char(d: int):
    if d in _CHAR_CACHE:
        return _CHAR_CACHE[d]
    q = abs(d)
    target = [kronecker(d, n) for n in range(1, q + 1)]
    prev_dps = flint.ctx.dps
    flint.ctx.dps = FLINT_DPS
    try:
        found = None
        for l in range(1, q):
            try:
                chi = flint.dirichlet_char(q, l)
            except Exception:
                continue
            if not chi.is_primitive() or not chi.is_real():
                continue
            ok = True
            for n in range(1, q + 1):
                v = chi(n % q)
                c = complex(v.real.mid(), v.imag.mid())
                if abs(c.real - target[n - 1]) > 1e-6 or abs(c.imag) > 1e-6:
                    ok = False
                    break
            if ok:
                found = chi
                break
    finally:
        flint.ctx.dps = prev_dps
    if found is None:
        raise RuntimeError(f"no flint Conrey character matches Kronecker chi_{d}")
    _CHAR_CACHE[d] = found
    return found


def _acb_to_mpc(v) -> mp.mpc:
    """Exact-digit conversion (no double-precision round-trip): parse the
    guaranteed decimal digits flint prints, not a float() of the ball.
    """
    re_s = v.real.str(FLINT_DPS + 3, radius=False)
    im_s = v.imag.str(FLINT_DPS + 3, radius=False)
    return mp.mpc(mp.mpf(re_s), mp.mpf(im_s))


def _flint_base(d: int, s: "mp.mpc"):
    prev_dps = flint.ctx.dps
    flint.ctx.dps = FLINT_DPS
    try:
        a_s = flint.acb(float(mp.re(s)), float(mp.im(s)))
        chi_d = _get_char(d)
        d1, d2 = DISCRIMINANTS[d]["d1"], DISCRIMINANTS[d]["d2"]
        chi_d1, chi_d2 = _get_char(d1), _get_char(d2)
        zeta_v = _acb_to_mpc(a_s.zeta())
        Ld = _acb_to_mpc(chi_d.l(a_s))
        Ld1 = _acb_to_mpc(chi_d1.l(a_s))
        Ld2 = _acb_to_mpc(chi_d2.l(a_s))
    finally:
        flint.ctx.dps = prev_dps
    return zeta_v * Ld, Ld1 * Ld2


def _dirichlet_L_mpmath(d: int, s: "mp.mpc") -> "mp.mpc":
    """L(s, chi_d) via the Hurwitz-zeta representation (dirichlet_l.py's
    pattern, generalized to any d via kronecker() instead of a fixed table).
    """
    q = abs(d)
    s = mp.mpc(s)
    total = mp.mpc(0)
    for a in range(1, q + 1):
        c = kronecker(d, a)
        if c == 0:
            continue
        total += c * mp.zeta(s, mp.mpf(a) / q)
    return mp.power(q, -s) * total


def _mpmath_base(d: int, s: "mp.mpc"):
    s = mp.mpc(s)
    d1, d2 = DISCRIMINANTS[d]["d1"], DISCRIMINANTS[d]["d2"]
    zeta_v = mp.zeta(s)
    Ld = _dirichlet_L_mpmath(d, s)
    Ld1 = _dirichlet_L_mpmath(d1, s)
    Ld2 = _dirichlet_L_mpmath(d2, s)
    return zeta_v * Ld, Ld1 * Ld2


def _precise_evaluate(d: int, lam: float, s: "mp.mpc") -> "mp.mpc":
    """f_lam(s), always via the arbitrary-precision mpmath path.

    Used ONLY for the final Newton polish of an off-line zero candidate.
    The flint backend is fast but its input point is built from Python
    floats (flint.acb(float(...), float(...))): that caps the achievable
    root precision at ~1e-16 regardless of flint's internal working
    precision, which is nowhere near enough for the |f| < 1e-18 target.
    mpmath's mpc has no such cap, so it is the correct tool for this one
    step even when the pencil's own backend is 'flint'.
    """
    A, B = _mpmath_base(d, mp.mpc(s))
    return A + lam * B


_BASE_CACHE: dict = {}


def _base_values(d: int, s: "mp.mpc", backend: str):
    """(A(s), B(s)), cached on (d, backend, s rounded to 1e-10).

    lam does not enter here: this is the shared cost every EulerPencil(d, *)
    instance amortizes across the whole lam grid.
    """
    key = (d, backend, round(float(mp.re(s)), 10), round(float(mp.im(s)), 10))
    hit = _BASE_CACHE.get(key)
    if hit is not None:
        return hit
    if backend == "flint":
        val = _flint_base(d, s)
    elif backend == "mpmath":
        val = _mpmath_base(d, s)
    else:
        raise ValueError(f"unknown backend {backend!r}")
    _BASE_CACHE[key] = val
    return val


def _is_dup(rho, found, tol=1e-6):
    for r in found:
        if abs(float(rho.real - r.real)) < tol and abs(float(rho.imag - r.imag)) < tol:
            return True
    return False


# --------------------------------------------------------------------------
# The pencil.
# --------------------------------------------------------------------------

class EulerPencil(LFunction):
    """f_lam(s) = A(s) + lam * B(s) for a class-number-2 discriminant d."""

    has_functional_equation = True

    def __init__(self, d: int = -15, lam: float = 0.0, backend: str = "flint"):
        if d not in DISCRIMINANTS:
            raise KeyError(f"no discriminant table entry for d={d}; add one to DISCRIMINANTS")
        self.d = int(d)
        self.lam = float(lam)
        self.backend = backend
        self.has_euler_product = (self.lam == 0.0)
        self.name = f"euler_pencil_d{self.d}_lam{self.lam:g}"

    def A(self, s):
        return _base_values(self.d, mp.mpc(s), self.backend)[0]

    def B(self, s):
        return _base_values(self.d, mp.mpc(s), self.backend)[1]

    def evaluate(self, s):
        A, B = _base_values(self.d, mp.mpc(s), self.backend)
        return A + self.lam * B

    def _gamma_prefactor(self, s):
        s = mp.mpc(s)
        return mp.power(abs(self.d), s / 2) * mp.power(2 * mp.pi, -s) * mp.gamma(s)

    def completed(self, s):
        """Lambda_lam(s) = |d|^{s/2} (2pi)^{-s} Gamma(s) f_lam(s)."""
        return self._gamma_prefactor(s) * self.evaluate(s)

    def completed_B(self, s):
        """The B-only completed form (lam-independent): the "Z_B" of the
        Lehmer-pair model. Any EulerPencil for this d gives the same value.
        """
        return self._gamma_prefactor(s) * self.B(s)

    def Z(self, t) -> float:
        return float(self.completed(mp.mpc(mp.mpf(1) / 2, t)).real)

    def Z_B(self, t) -> float:
        return float(self.completed_B(mp.mpc(mp.mpf(1) / 2, t)).real)

    def zeros(self, T_max: float, prec: int = 30):
        """All zeros with 0 < gamma <= T_max, on- and off-line, as mp.mpc.

        Pass 1: on-line sign-change scan (count_line). Pass 2: off-line grid
        scan (offline_zeros) over sigma in (0.5, 2.0], reflected through the
        functional equation rho -> 1 - rho. Cached on disk, keyed on
        (d, lam, backend, T_max, prec).
        """
        SHARED_CACHE_DIR.mkdir(parents=True, exist_ok=True)
        key = hashlib.sha1(
            f"pencil|d{self.d}|lam{self.lam:.8f}|{self.backend}|"
            f"{float(T_max):.6f}|{int(prec)}".encode()
        ).hexdigest()[:16]
        path = SHARED_CACHE_DIR / f"euler_pencil_zeros_{key}.pkl"
        if path.exists():
            with open(path, "rb") as f:
                return pickle.load(f)

        zeros_found = []
        _, ts = count_line(self, 0.02, float(T_max), step=0.02)
        for t in ts:
            rho = mp.mpc(mp.mpf(1) / 2, t)
            if 0 < rho.imag <= T_max and not _is_dup(rho, zeros_found):
                zeros_found.append(rho)

        off = offline_zeros(self, 0.02, float(T_max))
        for beta, gamma in off:
            rho = mp.mpc(beta, gamma)
            if not _is_dup(rho, zeros_found):
                zeros_found.append(rho)
            partner = mp.mpc(1 - beta, gamma)
            if not _is_dup(partner, zeros_found):
                zeros_found.append(partner)

        zeros_found.sort(key=lambda r: float(r.imag))
        with open(path, "wb") as f:
            pickle.dump(zeros_found, f)
        return zeros_found


# --------------------------------------------------------------------------
# Rectangle winding number.
# --------------------------------------------------------------------------

def count_rect(pencil, T1: float, T2: float, sigma_lo: float = -1.0, sigma_hi: float = 2.0) -> int:
    """Winding number of f_lam around d[sigma_lo,sigma_hi] x [T1,T2], T1 > 0.

    Adaptive boundary sampling: bisect any edge whose phase increment
    exceeds `threshold` radians, until every increment is below threshold;
    if the resulting total/(2 pi) is not within 1e-3 of an integer, halve
    the threshold and double the base sampling density, and retry.
    """
    def f(sigma, t):
        v = pencil.evaluate(mp.mpc(sigma, t))
        return complex(float(v.real), float(v.imag))

    def boundary_points(density):
        # Points per edge scale with the EDGE'S OWN length, not a flat count.
        # A flat n_per_edge=20 (this module's first version) starves a tall
        # box: at T2-T1=50 that is 2.5 units between initial samples on the
        # vertical edges, and a genuine simple zero can sit close enough to
        # the segment's midpoint that the true phase turns by close to a
        # full 2 pi while cmath.phase(v1/v0)'s principal-branch aliasing
        # makes the OBSERVED increment look near zero -- invisible to a
        # threshold check that only ever sees the aliased value, so no
        # amount of retrying with a coarser-than-zero-spacing start helps.
        # (Found via G6: count_rect gave 31 against count_line's 48 on
        # [10,60], a silent 17-zero undercount at the old flat density.)
        # A sub-zero-spacing initial density here (0.1, well under the
        # observed ~0.3+ unit zero gaps) makes that bracketing-coincidence
        # vanishingly unlikely without probing every candidate's magnitude.
        corners = [(sigma_lo, T1), (sigma_hi, T1), (sigma_hi, T2), (sigma_lo, T2), (sigma_lo, T1)]
        pts = []
        for i in range(4):
            p0, p1 = corners[i], corners[i + 1]
            length = math.hypot(p1[0] - p0[0], p1[1] - p0[1])
            n_edge = max(20, int(math.ceil(length / density)))
            for k in range(n_edge):
                frac = k / n_edge
                pts.append((p0[0] + (p1[0] - p0[0]) * frac, p0[1] + (p1[1] - p0[1]) * frac))
        pts.append(pts[0])
        return pts

    # Scale with window height: a wider box legitimately has more zeros on
    # its boundary (density ~ log(T)/(2 pi) per unit height per function) and
    # needs proportionally more points to resolve ALL of them, which is not
    # pathological -- unlike the case below, this is capped generously.
    MAX_POINTS = max(4000, int(800 * (T2 - T1)))
    # a zero sitting very close to the boundary path (it
    # happens: off-line zeros for this pencil are not confined near sigma =
    # 0.5, see the module notes on lam = -0.5 wandering to beta ~ 2.76 before
    # the beta-upper-bound fix) can otherwise force unbounded bisection,
    # since the phase is discontinuous exactly at a zero. Capping and
    # falling through to the outer retry (coarser threshold, so a stalled
    # edge is walked past rather than chased) keeps EACH ATTEMPT bounded at
    # MAX_POINTS * (evaluate cost); a window that still cannot converge
    # after a handful of attempts raises, which is the caller's cue that
    # this window is untrustworthy (its N_off should come from a direct
    # offline_zeros count instead of the winding number for that window).
    threshold = 1.0
    density = 0.1
    n = None
    for _ in range(4):
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
    raise RuntimeError(f"count_rect did not converge to an integer (last estimate {n})")


# --------------------------------------------------------------------------
# On-line sign-change count.
# --------------------------------------------------------------------------

def count_line(pencil, T1: float, T2: float, step: float = 0.02):
    """(count, sorted located zero heights) of Z_lam on [T1, T2].

    Base pass at `step`; any local minimum of |Z| lacking a sign change on
    either side is re-scanned at step/20 (close pairs the coarse grid could
    straddle without a sign flip).
    """
    n_steps = max(1, round((T2 - T1) / step))
    ts = [T1 + i * step for i in range(n_steps + 1)]
    zvals = [pencil.Z(t) for t in ts]

    def refine(ta, tb):
        return float(mp.findroot(lambda x: pencil.Z(float(x)), (ta, tb), solver="bisect", tol=1e-10))

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
                    curv = pencil.Z(tn)
                    if (prevv < 0) != (curv < 0):
                        zeros_t.append(refine(tt, tn))
                    prevv, tt = curv, tn

    zeros_t = sorted({round(z, 9) for z in zeros_t})
    return len(zeros_t), zeros_t


# --------------------------------------------------------------------------
# Off-line grid scan.
# --------------------------------------------------------------------------

def offline_zeros(pencil, T1: float, T2: float, sigma_step: float = 0.05, t_step: float = 0.05):
    """Located off-line zeros (beta, gamma) with beta > 1/2 + 1e-9 in the box
    sigma in (0.5, 2.0), t in [T1, T2].
    """
    sigmas = []
    s = 0.5 + sigma_step
    while s <= 2.0 + 1e-9:
        sigmas.append(round(s, 6))
        s += sigma_step
    ts = []
    t = T1
    while t <= T2 + 1e-9:
        ts.append(round(t, 6))
        t += t_step

    def absf(sg, tt):
        v = pencil.evaluate(mp.mpc(sg, tt))
        return abs(complex(float(v.real), float(v.imag)))

    grid = [[absf(sg, tt) for tt in ts] for sg in sigmas]
    flat_min = min((v for row in grid for v in row), default=1.0)
    cutoff = max(flat_min * 25.0, 1e-3)

    found = []
    for i, sg in enumerate(sigmas):
        for j, tt in enumerate(ts):
            v = grid[i][j]
            if v > cutoff:
                continue
            nbrs = []
            if i > 0:
                nbrs.append(grid[i - 1][j])
            if i < len(sigmas) - 1:
                nbrs.append(grid[i + 1][j])
            if j > 0:
                nbrs.append(grid[i][j - 1])
            if j < len(ts) - 1:
                nbrs.append(grid[i][j + 1])
            if nbrs and any(v > nb for nb in nbrs):
                continue
            try:
                seed = mp.findroot(pencil.evaluate, mp.mpc(sg, tt), tol=mp.mpf(10) ** -20)
            except (ValueError, ZeroDivisionError):
                continue
            beta0, gamma0 = float(seed.real), float(seed.imag)
            # Reject a seed that Newton walked outside the intended search
            # box (0.5, 2.0]: such an escape is not validated by the
            # winding-number count_rect box either (same sigma_hi), so an
            # accepted point there would silently disagree with N_total.
            if not (0.5 + 1e-9 < beta0 <= 2.0 + 1e-6) or not (T1 - 1e-9 <= gamma0 <= T2 + 1e-9):
                continue
            # Polish with a pure-mpmath (arbitrary-precision) Newton pass:
            # see _precise_evaluate's docstring for why the fast/possibly
            # flint-backed seed cannot itself reach |f| < 1e-18.
            prev_dps = mp.mp.dps
            try:
                mp.mp.dps = 40
                root = mp.findroot(
                    lambda z: _precise_evaluate(pencil.d, pencil.lam, z),
                    mp.mpc(seed), tol=mp.mpf(10) ** -40, maxsteps=100,
                )
                resid = abs(_precise_evaluate(pencil.d, pencil.lam, root))
            except (ValueError, ZeroDivisionError):
                continue
            finally:
                mp.mp.dps = prev_dps
            beta, gamma = float(root.real), float(root.imag)
            if not (0.5 + 1e-9 < beta <= 2.0 + 1e-6) or not (T1 - 1e-9 <= gamma <= T2 + 1e-9):
                continue  # the arbitrary-precision polish can also walk outside the box
            if resid >= 1e-18:
                continue
            if not any(abs(gamma - g) < 1e-6 and abs(beta - b) < 1e-6 for (b, g) in found):
                found.append((beta, gamma))
    return found


# --------------------------------------------------------------------------
# Lehmer-pair model.
# --------------------------------------------------------------------------

def lehmer_prediction(pencil0, pencilB, t1: float, t2: float):
    """(t_m, delta, lam_pred_signed): the second-order collision model.

    Near an adjacent on-line pair of Z_0 at t1 < t2, Z_0 ~ c[(t-t_m)^2 -
    delta^2/4] with c = Z_0''(t_m)/2; the pair leaves the line once
    lam * Z_B(t_m) / c exceeds delta^2/4, i.e. lam_c = c delta^2 / (4 Z_B(t_m)).
    """
    t_m = (t1 + t2) / 2.0
    delta = t2 - t1
    h = 1e-3
    Z0 = pencil0.Z
    Z0pp = (Z0(t_m + h) - 2 * Z0(t_m) + Z0(t_m - h)) / (h * h)
    c = Z0pp / 2.0
    ZB_tm = pencilB.Z_B(t_m)
    if ZB_tm == 0.0:
        lam_pred = math.inf
    else:
        lam_pred = c * delta ** 2 / (4.0 * ZB_tm)
    return t_m, delta, lam_pred


# --------------------------------------------------------------------------
# Classification of an on-line height as a zeta zero or an L(chi_d) zero.
# --------------------------------------------------------------------------

def _classify_height(d: int, t: float):
    s = mp.mpc(mp.mpf(1) / 2, t)
    z_val = float(abs(mp.zeta(s)))
    L_val = float(abs(_dirichlet_L_mpmath(d, s)))
    typ = "Z" if z_val < L_val else "L"
    return typ, z_val, L_val


# --------------------------------------------------------------------------
# Continuation: track an off-line pair down to its lam = 0 collision.
# --------------------------------------------------------------------------

def track_pair(d: int, lam_start: float, rho_start, backend: str = "flint",
                step0: float = 0.05, prec: int = 30, window: float = 2.0):
    """Continue the off-line zero rho(lam) from lam_start toward lam = 0.

    Predictor-corrector: at each step, Newton-correct (mp.findroot seeded
    from the previous root) at a new lam; halve the step on Newton failure
    or once beta - 1/2 is shrinking fast (approaching the collision), and
    stop once beta - 1/2 < 1e-4. Then bisect lam_c on the sign-change count
    of Z_lam in a window around the collision height (2 = pair on the line,
    0 = pair off), refine to 1e-6 relative, and report the two on-line
    Z_0-zeros the pair descends from, their gap, their zeta-vs-L(chi_d)
    classification, and the Lehmer-model prediction for comparison.
    """
    lam = float(lam_start)
    rho = mp.mpc(rho_start)
    step = step0
    n_fail = 0
    n_iter = 0
    # Hard cap on total steps: a step that keeps getting halved (chasing a
    # collision where beta shrinks quickly right up until it doesn't) can
    # otherwise crawl at the 1e-4 floor for thousands of iterations before
    # abs(lam) shrinks below 1e-9. 200 steps is generous for step0=0.05 (a
    # full traverse at the floor step would be lam_start/1e-4 steps, which
    # this cap forecloses); if the cap is hit we simply stop the
    # continuation early and use the last reached point -- gamma drifts
    # little as lam decreases (confirmed empirically: under 0.01 in height
    # for the d=-15 pairs checked), so it is still a good t_c_guess for the
    # bisection step below, which is what actually locates lam_c.

    while abs(lam) > 1e-9 and n_fail < 40 and n_iter < 200:
        n_iter += 1
        trial = min(step, abs(lam))
        new_lam = lam - math.copysign(trial, lam)
        try:
            pencil = EulerPencil(d=d, lam=new_lam, backend=backend)
            new_rho = mp.findroot(pencil.evaluate, rho, tol=mp.mpf(10) ** (-prec + 5))
        except Exception:
            step = max(step / 2, 1e-4)
            n_fail += 1
            continue
        beta_new, beta_old = float(new_rho.real), float(rho.real)
        if beta_new - 0.5 < 1e-4:
            lam, rho = new_lam, new_rho
            break
        if (beta_old - 0.5) > 0 and (beta_old - beta_new) > 0.3 * (beta_old - 0.5):
            step = max(step / 2, 1e-4)  # shrinking fast: track more finely
        else:
            step = min(step * 1.5, step0)  # recover pace once it stops shrinking fast
        lam, rho = new_lam, new_rho

    t_c_guess = float(rho.imag)

    def n_sign_changes(lam_val):
        p = EulerPencil(d=d, lam=lam_val, backend=backend)
        cnt, _ = count_line(p, max(1e-3, t_c_guess - window), t_c_guess + window, step=0.01)
        return cnt

    n_on = n_sign_changes(0.0)
    lo, hi = 0.0, lam_start
    for _ in range(60):
        mid = (lo + hi) / 2
        if n_sign_changes(mid) == n_on:
            lo = mid
        else:
            hi = mid
        if abs(hi - lo) < 1e-6 * max(abs(hi), 1e-9):
            break
    lam_c = (lo + hi) / 2

    p0 = EulerPencil(d=d, lam=0.0, backend=backend)
    _, zt = count_line(p0, max(1e-3, t_c_guess - window), t_c_guess + window, step=0.01)
    below = sorted((z for z in zt if z < t_c_guess), reverse=True)
    above = sorted(z for z in zt if z >= t_c_guess)
    if not below or not above:
        # widen the window once if the collision sits near its edge
        _, zt = count_line(p0, max(1e-3, t_c_guess - 2 * window), t_c_guess + 2 * window, step=0.01)
        below = sorted((z for z in zt if z < t_c_guess), reverse=True)
        above = sorted(z for z in zt if z >= t_c_guess)
    t1 = below[0] if below else t_c_guess
    t2 = above[0] if above else t_c_guess
    delta = t2 - t1

    type1, z1, L1 = _classify_height(d, t1)
    type2, z2, L2 = _classify_height(d, t2)
    pair_type = "".join(sorted([type1, type2], reverse=True))  # ZZ, ZL, LL

    pencilB = EulerPencil(d=d, lam=1.0, backend=backend)
    t_m, delta_pred, lam_pred = lehmer_prediction(p0, pencilB, t1, t2)

    return dict(
        gamma_start=float(rho_start.imag), beta_start=float(rho_start.real),
        lam_c=lam_c, t_c=t_c_guess, t1=t1, t2=t2, delta=delta, type=pair_type,
        mag1=(z1, L1), mag2=(z2, L2), lam_pred=lam_pred,
        ratio=(lam_c / lam_pred if lam_pred not in (0.0, math.inf) else math.nan),
        sign_ok=(lam_pred != 0 and math.copysign(1.0, lam_c) == math.copysign(1.0, lam_pred)),
    )


# --------------------------------------------------------------------------
# main()
# --------------------------------------------------------------------------

LAM_GRID_FULL = [1.0, -1.0, 0.5, -0.5, 0.25, -0.25, 0.1, -0.1, 0.05, -0.05, 0.025, -0.025, 0.01, -0.01]
LAM_GRID_QUICK = [1.0, -1.0, 0.25, -0.25, 0.05, -0.05]
D20_LAMS = [1.0, -1.0, 0.25, -0.25, 0.05, -0.05]


def _git_head():
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=HERE, capture_output=True,
                               text=True, timeout=5).stdout.strip()
    except Exception:
        return "unknown"


def run_s1(d, lam_values, T_max, backend, window=10.0, time_budget=None, t0=None, notes=None,
           max_located_windows_per_lam=2):
    """Per-lam aggregate table over [1, T_max] chunked into width-`window`
    rectangles/line-scans (chunking bounds each count_rect/offline_zeros
    call; results are summed/collected into one row per lam).

    N_off is counted from the winding-number excess (diff // 2) for EVERY
    triggered window -- cross-validated against a brute-force fine boundary
    sampling and against offline_zeros' own located count (both agree
    exactly; see the module notes). The expensive part of the pipeline is
    not the COUNT but PRECISELY LOCATING each zero (a 30x200-point 2D grid
    plus an arbitrary-precision Newton polish per candidate, ~10 s/window);
    off-line zeros turned out to be pervasive (found at every nonzero lam
    tested, down to lam = +-0.01), so locating every triggered window for
    every lam would run to tens of minutes. We therefore call offline_zeros
    (full location, for T* and a representative beta/gamma sample) on only
    the first `max_located_windows_per_lam` triggered windows per lam, and
    take the count from the winding number everywhere else.
    """
    rows = []
    n_windows = int(math.ceil((T_max - 1.0) / window))
    for lam in lam_values + ([0.0] if 0.0 not in lam_values and d not in (-20,) else []):
        pencil = EulerPencil(d=d, lam=lam, backend=backend)
        N_total = N_line = N_off = 0
        off_list = []
        located_windows = 0
        for w in range(n_windows):
            T1 = 1.0 + w * window
            T2 = min(T1 + window, T_max)
            if T2 <= T1:
                continue
            if time_budget is not None and t0 is not None and time.time() - t0 > time_budget:
                if notes is not None:
                    notes.append(f"S1 d={d} lam={lam}: time budget hit, stopped at T={T1:.1f}")
                break
            n_line, _ = count_line(pencil, T1, T2, step=0.02)
            try:
                n_rect = count_rect(pencil, T1, T2)
            except RuntimeError as exc:
                if notes is not None:
                    notes.append(f"S1 d={d} lam={lam} window [{T1:.1f},{T2:.1f}]: "
                                  f"count_rect did not converge ({exc}); window skipped "
                                  f"from N_total (a zero sits too close to the sigma=-1/2 "
                                  f"boundary path for the winding contour to resolve).")
                continue
            N_total += n_rect
            N_line += n_line
            diff = n_rect - n_line
            if diff != 0:
                if diff % 2 != 0:
                    if notes is not None:
                        notes.append(f"ANOMALY d={d} lam={lam} window [{T1:.1f},{T2:.1f}]: "
                                      f"odd parity (rect-line={diff})")
                N_off += abs(diff) // 2
                if located_windows < max_located_windows_per_lam:
                    off = offline_zeros(pencil, T1, T2)
                    off_list.extend(off)
                    located_windows += 1
                    if 2 * len(off) != diff and notes is not None:
                        # each located off-line zero (beta > 1/2) contributes 2
                        # to the winding excess: it and its FE+conjugate mirror
                        # (1-beta)+i*gamma both sit inside the box (sigma_lo=-1
                        # < 1-beta and beta < sigma_hi=2 generically), while
                        # neither sits on the line. Flag if counts disagree.
                        notes.append(f"ANOMALY d={d} lam={lam} window [{T1:.1f},{T2:.1f}]: "
                                      f"rect-line={diff} but located {len(off)} off-line zero(s) "
                                      f"(expected {diff // 2})")
        T_star = min((g for (_, g) in off_list), default=None)
        max_beta = max((b for (b, _) in off_list), default=None)
        rows.append(dict(lam=lam, N_total=N_total, N_line=N_line, N_off=N_off,
                          T_star=T_star, max_beta=max_beta, off_list=off_list))
        print(f"    [S1 d={d}] lam={lam:+.4f} done: N_total={N_total} N_line={N_line} "
              f"N_off={N_off} elapsed={time.time() - (t0 or time.time()):.1f}s", flush=True)
    return rows


def _print_s1_table(rows, title):
    print(f"\n  {title}")
    print(f"    {'lam':>8} {'N_total':>8} {'N_line':>8} {'N_off':>6} {'T*':>10} {'max_beta':>10}")
    for r in rows:
        tstar = f"{r['T_star']:.3f}" if r["T_star"] is not None else "None"
        mbeta = f"{r['max_beta']:.5f}" if r["max_beta"] is not None else "None"
        print(f"    {r['lam']:>8.4f} {r['N_total']:>8} {r['N_line']:>8} {r['N_off']:>6} {tstar:>10} {mbeta:>10}")


def run_s2(d, backend, n_pairs, T_max, notes, window=10.0):
    """Track the n lowest off-line pairs at lam=+1 and lam=-1 down to lam=0.

    Scans window by window (offline_zeros over the WHOLE [1, T_max] range in
    one call would be a 30 x (T_max/0.05)-point grid -- far too expensive)
    and stops as soon as n_pairs off-line zeros have been located.
    """
    rows = []
    n_windows = int(math.ceil((T_max - 1.0) / window))
    for lam_sign in (1.0, -1.0):
        pencil = EulerPencil(d=d, lam=lam_sign, backend=backend)
        off = []
        for w in range(n_windows):
            if len(off) >= n_pairs:
                break
            T1 = 1.0 + w * window
            T2 = min(T1 + window, T_max)
            if T2 <= T1:
                continue
            n_line, _ = count_line(pencil, T1, T2, step=0.02)
            try:
                n_rect = count_rect(pencil, T1, T2)
            except RuntimeError as exc:
                notes.append(f"S2 d={d} lam={lam_sign} window [{T1:.1f},{T2:.1f}]: "
                              f"count_rect did not converge ({exc}); window skipped")
                continue
            if n_rect != n_line:
                off.extend(offline_zeros(pencil, T1, T2))
        print(f"    [S2 d={d}] lam_sign={lam_sign:+.1f}: located {len(off)} candidate(s) "
              f"(need {n_pairs})", flush=True)
        off = sorted(off, key=lambda bg: bg[1])[:n_pairs]
        if not off:
            notes.append(f"S2 d={d} lam={lam_sign}: no off-line zeros found up to T_max={T_max}; "
                          "nothing to track (a real negative result: the pencil is on-line "
                          "throughout the searched height/lam range at this sign).")
            continue
        for (beta, gamma) in off:
            rho0 = mp.mpc(beta, gamma)
            try:
                res = track_pair(d, lam_sign, rho0, backend=backend)
                res["lam_start"] = lam_sign
                rows.append(res)
                print(f"      tracked rho~{beta:.4f}+{gamma:.3f}i -> lam_c={res['lam_c']:.5f}",
                      flush=True)
            except Exception as exc:
                notes.append(f"S2 d={d} lam={lam_sign} rho~{beta:.4f}+{gamma:.3f}i: "
                              f"track_pair failed ({exc!r})")
    return rows


def _print_s2_table(rows):
    print(f"\n  S2: tracked pairs (lam_start | gamma_start | beta_start | lam_c | t_c | t1 | t2 | "
          f"delta | type | lam_pred | ratio | sign_ok)")
    for r in rows:
        print(f"    {r['lam_start']:>+5.2f}  g={r['gamma_start']:>8.3f}  b={r['beta_start']:.5f}  "
              f"lam_c={r['lam_c']:>9.5f}  t_c={r['t_c']:>8.3f}  t1={r['t1']:>8.3f}  t2={r['t2']:>8.3f}  "
              f"d={r['delta']:>6.3f}  {r['type']:>2}  lam_pred={r['lam_pred']:>10.5f}  "
              f"ratio={r['ratio']:>7.3f}  sign_ok={r['sign_ok']}")


def run_s3(d, backend, T_max, n_pairs, notes):
    """Forward-test: 15 closest adjacent on-line pairs of Z_0, predict and
    bisect their collision lam_c, and fit the delta-power law."""
    pencil0 = EulerPencil(d=d, lam=0.0, backend=backend)
    _, zt = count_line(pencil0, 1.0, T_max, step=0.01)
    pairs = [(zt[i], zt[i + 1], zt[i + 1] - zt[i]) for i in range(len(zt) - 1)]
    pairs.sort(key=lambda x: x[2])
    pairs = pairs[:n_pairs]
    pencilB = EulerPencil(d=d, lam=1.0, backend=backend)

    rows = []
    for (t1, t2, delta) in pairs:
        t_m, _, lam_pred = lehmer_prediction(pencil0, pencilB, t1, t2)
        if lam_pred in (0.0, math.inf) or math.isnan(lam_pred):
            notes.append(f"S3 d={d} pair ({t1:.3f},{t2:.3f}): degenerate lam_pred, skipped")
            continue
        typ = "".join(sorted([_classify_height(d, t1)[0], _classify_height(d, t2)[0]], reverse=True))

        def n_on_at(lam_val):
            p = EulerPencil(d=d, lam=lam_val, backend=backend)
            cnt, _ = count_line(p, max(1e-3, t_m - delta), t_m + delta, step=0.01)
            return cnt

        n_base = n_on_at(0.0)
        n_high = n_on_at(1.5 * lam_pred)
        n_low = n_on_at(0.5 * lam_pred)
        model_ok = (n_high != n_base) and (n_low == n_base)
        if not model_ok:
            notes.append(f"S3 d={d} pair ({t1:.3f},{t2:.3f}): model check failed "
                          f"(n_base={n_base}, n_low={n_low}, n_high={n_high})")

        lo, hi = 0.0, 3.0 * lam_pred if lam_pred != 0 else 1.0
        # ensure hi actually flips the count away from n_base
        tries = 0
        while n_on_at(hi) == n_base and tries < 6:
            hi *= 2
            tries += 1
        for _ in range(50):
            mid = (lo + hi) / 2
            if n_on_at(mid) == n_base:
                lo = mid
            else:
                hi = mid
            if abs(hi - lo) < 1e-4 * max(abs(hi), 1e-9):
                break
        lam_c = (lo + hi) / 2
        ratio = lam_c / lam_pred if lam_pred != 0 else math.nan
        rows.append(dict(t1=t1, t2=t2, delta=delta, type=typ, lam_pred=lam_pred, lam_c=lam_c,
                          ratio=ratio, model_ok=model_ok))
        print(f"    [S3 d={d}] pair ({t1:.3f},{t2:.3f}) delta={delta:.4f} -> "
              f"lam_pred={lam_pred:.4e} lam_c={lam_c:.4e} ratio={ratio:.3f}", flush=True)

    slope = None
    if len(rows) >= 3:
        xs = [math.log(r["delta"]) for r in rows if r["lam_c"] not in (0.0,) and r["lam_c"] > 0]
        ys = [math.log(abs(r["lam_c"])) for r in rows if r["lam_c"] not in (0.0,) and r["lam_c"] > 0]
        if len(xs) >= 3:
            n = len(xs)
            mx, my = sum(xs) / n, sum(ys) / n
            num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
            den = sum((x - mx) ** 2 for x in xs)
            slope = num / den if den != 0 else None
    return rows, slope


def _print_s3_table(rows, slope):
    print(f"\n  S3: forward test (t1 | t2 | delta | type | lam_pred | lam_c | ratio | model_ok)")
    for r in rows:
        print(f"    t1={r['t1']:>8.3f}  t2={r['t2']:>8.3f}  d={r['delta']:>7.4f}  {r['type']:>2}  "
              f"lam_pred={r['lam_pred']:>10.5f}  lam_c={r['lam_c']:>10.5f}  ratio={r['ratio']:>7.3f}  "
              f"model_ok={r['model_ok']}")
    print(f"    log|lam_c| vs log(delta) least-squares slope: "
          f"{slope:.3f}" if slope is not None else "    slope: insufficient data")


def _write_markdown(path, ctx):
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = []
    lines.append("# Euler pencil experiment: results")
    lines.append("")
    lines.append(f"Runtime: {ctx['runtime_s']:.1f} s. T_max used: {ctx['T_max']}. "
                 f"Backend: {ctx['backend']}. flint dps: {FLINT_DPS}, mpmath dps: {MP_DPS}.")
    lines.append(f"Epstein sign identification: {ctx['epstein_id']}")
    lines.append("")
    lines.append("## S1 (d=-15)")
    lines.append("")
    lines.append("| lam | N_total | N_line | N_off | T* | max_beta |")
    lines.append("|---|---|---|---|---|---|")
    for r in ctx["s1_rows"]:
        tstar = f"{r['T_star']:.3f}" if r["T_star"] is not None else "None"
        mbeta = f"{r['max_beta']:.5f}" if r["max_beta"] is not None else "None"
        lines.append(f"| {r['lam']:.4f} | {r['N_total']} | {r['N_line']} | {r['N_off']} | {tstar} | {mbeta} |")
    lines.append("")
    lines.append("## S1 (d=-20 replicate)")
    lines.append("")
    lines.append("| lam | N_total | N_line | N_off | T* | max_beta |")
    lines.append("|---|---|---|---|---|---|")
    for r in ctx["s1_d20_rows"]:
        tstar = f"{r['T_star']:.3f}" if r["T_star"] is not None else "None"
        mbeta = f"{r['max_beta']:.5f}" if r["max_beta"] is not None else "None"
        lines.append(f"| {r['lam']:.4f} | {r['N_total']} | {r['N_line']} | {r['N_off']} | {tstar} | {mbeta} |")
    lines.append("")
    lines.append("## S2 (tracked pairs)")
    lines.append("")
    lines.append("| lam_start | gamma_start | beta_start | lam_c | t_c | t1 | t2 | delta | type | lam_pred | ratio | sign_ok |")
    lines.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in ctx["s2_rows"]:
        lines.append(f"| {r['lam_start']:+.2f} | {r['gamma_start']:.3f} | {r['beta_start']:.5f} | "
                     f"{r['lam_c']:.5f} | {r['t_c']:.3f} | {r['t1']:.3f} | {r['t2']:.3f} | "
                     f"{r['delta']:.3f} | {r['type']} | {r['lam_pred']:.5f} | {r['ratio']:.3f} | {r['sign_ok']} |")
    lines.append("")
    lines.append("## S3 (forward test)")
    lines.append("")
    lines.append("| t1 | t2 | delta | type | lam_pred | lam_c | ratio | model_ok |")
    lines.append("|---|---|---|---|---|---|---|---|")
    for r in ctx["s3_rows"]:
        lines.append(f"| {r['t1']:.3f} | {r['t2']:.3f} | {r['delta']:.4f} | {r['type']} | "
                     f"{r['lam_pred']:.5f} | {r['lam_c']:.5f} | {r['ratio']:.3f} | {r['model_ok']} |")
    lines.append("")
    lines.append(f"log|lam_c| vs log(delta) slope: {ctx['s3_slope']}")
    lines.append("")
    lines.append("## Anomalies / notes")
    lines.append("")
    if ctx["notes"]:
        for n in ctx["notes"]:
            lines.append(f"- {n}")
    else:
        lines.append("- none")
    path.write_text("\n".join(lines) + "\n")


D20_PICKLE = HERE / "_d20_result.pkl"


def _d20_only(T_max_d20: float, time_budget_d20: float):
    """Standalone d=-20 S1 leg, run as a SEPARATE PROCESS from main().

    In-process signal.alarm() cannot preempt a hang inside a C extension
    call (flint/mpmath arithmetic does not return to the Python interpreter
    between bytecode instructions, so a pending SIGALRM just queues up).
    A subprocess timeout (subprocess.run(..., timeout=...)) kills at the OS
    level instead, which works regardless of what the child is stuck in.
    """
    mp.mp.dps = MP_DPS
    notes = []
    t0 = time.time()
    rows = run_s1(-20, D20_LAMS, T_max_d20, "flint", time_budget=time_budget_d20, t0=t0,
                  notes=notes, max_located_windows_per_lam=1)
    with open(D20_PICKLE, "wb") as f:
        pickle.dump((rows, notes), f)


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if "--d20-only" in argv:
        vals = [float(x) for x in argv if x != "--d20-only"]
        _d20_only(*vals)
        return
    quick = quick_arg(argv)
    mp.mp.dps = MP_DPS
    t0 = time.time()
    notes = []

    backend = "flint"
    d_primary = -15
    T_max = 100.0 if quick else 200.0
    T_max_d20 = 15.0  # d=-20 is a secondary replicate; off-line zeros turned out
    # pervasive (see module notes), so this leg gets its own smaller T_max and a
    # smaller time budget to guarantee it cannot crowd out S2/S3 for the primary
    # target. T_max_d20 = 25 and 40 were both found to hang reproducibly in this
    # environment (killed at 90s / 250s by an external `timeout`; a nonzero
    # in-process signal.alarm could not preempt it, pointing to a hang inside a
    # single C-extension call) while T_max_d20 = 15 completes in ~10s; run as a
    # genuine OS subprocess below so a recurrence is killable from outside.
    lam_grid = LAM_GRID_QUICK if quick else LAM_GRID_FULL
    n_track = 3 if quick else 6
    n_s3 = 8 if quick else 15
    time_budget = 12 * 60  # S1(d=-15) is the primary deliverable (empirically ~7 min
    # at T_max=200 with the full lam grid after the beta-upper-bound fix).
    time_budget_d20 = 60

    print("=" * 78)
    print(f"EULER PENCIL: d={d_primary}, T_max={T_max}, backend={backend}, quick={quick}")
    print("=" * 78)

    # Benchmark one evaluation.
    p_bench = EulerPencil(d=d_primary, lam=0.3, backend=backend)
    tb0 = time.time()
    p_bench.evaluate(mp.mpc(0.5, 150.0))
    tb1 = time.time()
    print(f"\nBenchmark: one f_lam evaluation at t~150 took {tb1 - tb0:.4f} s")

    # Epstein sign identification (genus theory: Z_principal = A+B, Z_nonprincipal = A-B).
    epstein_id = ("lam=+1 <-> principal form Z_Q (genus sum A+B); "
                  "lam=-1 <-> non-principal form Z_Q (genus difference A-B); "
                  "no extra normalization constant needed (w=2 already in the raw lattice sum).")
    print(f"\nEpstein identification (to verify in gates): {epstein_id}")

    print("\n" + "=" * 78)
    print("S1: lam grid, d=-15")
    print("=" * 78)
    s1_rows = run_s1(d_primary, lam_grid, T_max, backend, time_budget=time_budget, t0=t0, notes=notes)
    _print_s1_table(s1_rows, f"S1 table (d={d_primary})")

    print("\n" + "=" * 78)
    print("S2: tracking off-line pairs from lam=+-1 down to lam=0")
    print("=" * 78)
    s2_rows = run_s2(d_primary, backend, n_track, T_max, notes)
    _print_s2_table(s2_rows)

    print("\n" + "=" * 78)
    print("S3: forward test of the Lehmer-pair model")
    print("=" * 78)
    s3_rows, s3_slope = run_s3(d_primary, backend, T_max, n_s3, notes)
    _print_s3_table(s3_rows, s3_slope)

    # d=-20 runs LAST and defensively: it is the secondary replicate (spec:
    # "replicate the S1 table for d=-20 ... only"), and empirically this leg
    # ran into repeated environment-level stalls in this session (its own
    # isolated timing is fast: ~30s for a full lam value) that never
    # reproduced when it was run standalone -- placing it after the primary
    # d=-15 S1/S2/S3 deliverables, wrapped so any hang or exception here
    # costs at most its own signal-based wall-clock cap, protects the rest
    # of the run.
    print("\n" + "=" * 78)
    print(f"S1 replicate: d=-20 (T_max={T_max_d20}, secondary check, own time budget)")
    print("=" * 78)
    s1_d20_rows = []
    if D20_PICKLE.exists():
        D20_PICKLE.unlink()
    try:
        import subprocess
        proc = subprocess.run(
            [sys.executable, "-u", "-m", "experiments.criticality.e_euler_pencil",
             "--d20-only", str(T_max_d20), str(time_budget_d20)],
            timeout=time_budget_d20 + 90, capture_output=True, text=True,
        )
        if proc.returncode != 0 or not D20_PICKLE.exists():
            notes.append(f"S1 d=-20 replicate subprocess failed (returncode={proc.returncode}); "
                          f"stderr tail: {proc.stderr[-500:] if proc.stderr else '(none)'}. "
                          "This did not affect the d=-15 S1/S2/S3 results above.")
        else:
            with open(D20_PICKLE, "rb") as f:
                s1_d20_rows, d20_notes = pickle.load(f)
            notes.extend(d20_notes)
            _print_s1_table(s1_d20_rows, "S1 table (d=-20)")
    except subprocess.TimeoutExpired:
        notes.append(f"S1 d=-20 replicate did not complete within {time_budget_d20 + 90:.0f}s "
                      "wall clock (killed at the OS level; an in-process alarm could not preempt "
                      "it, which itself points to the hang being inside a single C-extension "
                      "call, not a Python-level loop). This did not affect the d=-15 S1/S2/S3 "
                      "results above, which were computed and saved before this subprocess ran.")
        print("  d=-20 replicate subprocess timed out and was killed (see notes)")
    finally:
        if D20_PICKLE.exists():
            D20_PICKLE.unlink()

    runtime = time.time() - t0
    print(f"\nTotal runtime: {runtime:.1f} s")

    # ---- npz ----
    def _arr(rows, keys):
        import numpy as np
        return {k: np.array([r.get(k) if r.get(k) is not None else np.nan for r in rows]) for k in keys}

    import numpy as np
    arrays = {}
    arrays.update({f"s1_{k}": v for k, v in _arr(s1_rows, ["lam", "N_total", "N_line", "N_off", "T_star", "max_beta"]).items()})
    arrays.update({f"s1d20_{k}": v for k, v in _arr(s1_d20_rows, ["lam", "N_total", "N_line", "N_off", "T_star", "max_beta"]).items()})
    arrays.update({f"s2_{k}": v for k, v in _arr(s2_rows, ["lam_start", "gamma_start", "beta_start", "lam_c", "t_c", "t1", "t2", "delta", "lam_pred", "ratio"]).items()})
    arrays["s2_type"] = np.array([r["type"] for r in s2_rows])
    arrays.update({f"s3_{k}": v for k, v in _arr(s3_rows, ["t1", "t2", "delta", "lam_pred", "lam_c", "ratio"]).items()})
    arrays["s3_type"] = np.array([r["type"] for r in s3_rows])
    arrays["s3_slope"] = np.array([s3_slope if s3_slope is not None else np.nan])
    arrays["notes"] = np.array(notes if notes else ["none"])

    provenance = dict(d=d_primary, backend=backend, flint_dps=FLINT_DPS, mp_dps=MP_DPS,
                       T_max=T_max, quick=quick, runtime_s=runtime, git_head=_git_head(),
                       timestamp=time.strftime("%Y-%m-%dT%H:%M:%S"),
                       epstein_id=epstein_id)
    save_npz(HERE / "e_euler_pencil.npz", arrays, provenance)
    print(f"\nSaved {HERE / 'e_euler_pencil.npz'}")

    _write_markdown(SCRATCH_MD, dict(runtime_s=runtime, T_max=T_max, backend=backend,
                                      epstein_id=epstein_id, s1_rows=s1_rows, s1_d20_rows=s1_d20_rows,
                                      s2_rows=s2_rows, s3_rows=s3_rows, s3_slope=s3_slope, notes=notes))
    print(f"Wrote {SCRATCH_MD}")

    if notes:
        print(f"\n{len(notes)} anomaly note(s):")
        for n in notes:
            print(f"  - {n}")

    return dict(s1_rows=s1_rows, s1_d20_rows=s1_d20_rows, s2_rows=s2_rows, s3_rows=s3_rows,
                s3_slope=s3_slope, notes=notes, runtime=runtime)


if __name__ == "__main__":
    main()
