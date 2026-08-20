"""Certified smallest-eigenvalue enclosures for the Weil-form minimizer pipeline.

WHY THIS EXISTS. The B2c experiment arc (e2ar_hard_window_xi, e2as_deep_xi_ladder,
and the planned B2c-deep2 ladder at dps 110) solves symmetric generalized
eigenproblems Q c = lambda G c (zero-side Weil Gram against an exact L^2 Gram)
with mpmath eigsy after a Cholesky reduction. A dps-50 run once returned a
silently degenerate ground state (precision starvation) that only a hand-built
gate caught. This module replaces "solved at dps N" with "proven enclosure":

  certify_smallest(A, B) returns a RIGOROUS interval [lo, hi] containing the
  smallest eigenvalue of the symmetric pencil (A, B), a certified residual
  bound on the returned eigenvector, and a spectral-gap-based sin(theta)
  bound, all computed in ball arithmetic (python-flint / arb) with outward
  rounding. precision_ladder() re-solves along a dps schedule and flags
  starvation automatically: a radius that fails to shrink IS the detector.

CERTIFICATION SEMANTICS (read before trusting a number):
  - Input entries are taken as EXACT dyadic rationals (every mpf / float is
    one). The mpf -> arb conversion below is exact and self-checked. The
    certificate therefore covers the matrix AS GIVEN; error committed while
    BUILDING the entries (truncated zero sums, quadrature, spline tails) is
    the caller's ledger, exactly as in the e2ar/e2as tail-floor bookkeeping.
  - Primary route (flint): eigenvalue enclosures come from arb's certified
    nonsymmetric eigensolver (acb_mat.eig, Rump / van der Hoeven-Mourrain,
    available in the installed python-flint 0.9.0). For the generalized
    problem the pencil is passed as a rigorous ball enclosure of B^{-1}A
    (arb_mat.solve is a verified solve), and B's positive definiteness is
    itself certified by enclosing B's spectrum. On top of that, a Rump-style
    symmetric residual bound ||Av - mu Bv||_{B^{-1}} / ||v||_B is computed in
    ball arithmetic: it tightens the eigenvalue interval when the rest of the
    spectrum is certified away, and it feeds the Davis-Kahan eigenvector
    bound sin(theta) <= residual / gap. All of this is directed-rounding
    rigorous: certified=True.
  - Fallback route (flint absent or use_flint=False): the same quantities in
    mpmath at elevated precision with explicit slack. mpmath rounds to
    nearest, so this is labeled certified=False, "high-confidence, not
    directed-rounding rigorous". It never masquerades as a certificate.

Isolation honesty: when eigenvalues cluster below the working precision, the
flint solver cannot isolate them; we then fall back to cluster enclosures
(multiple=True), which keep containment but honestly widen the interval and
drop the gap. That widening is the precision-starvation signature the ladder
watches for.

Consumers: experiments/arithmetic_geometric/e2a* ladders (Gram pencils, n of
order 10-40, dps 50-110). Typical call, mirroring the e2ar reduction:

    from experiments._shared.certified_eig import certify_smallest
    cert = certify_smallest(Qz, G, dps=110)
    assert cert.certified and cert.radius < tol

Run the checks: python -m experiments._shared.test_certified_eig
"""

from __future__ import annotations

import mpmath as mp
from mpmath.libmp import from_man_exp

try:
    from flint import arb, arb_mat, acb_mat, ctx as _fctx
    HAVE_FLINT = True
except ImportError:  # pragma: no cover (flint is installed in this venv)
    HAVE_FLINT = False

_LOG2_10 = 3.321928094887362


# ----------------------------------------------------------------------------
# exact conversions (the rigor of everything downstream rests on these)
# ----------------------------------------------------------------------------

def _exact_mpf(x):
    """Coerce a scalar to an EXACT mpf, independent of the working precision.

    ints go through from_man_exp so huge integers do not get rounded by the
    ambient mp.dps; floats are already dyadic; strings round at current dps
    (documented, acceptable for test construction only).
    """
    if isinstance(x, mp.mpf):
        return x
    if isinstance(x, int):
        return mp.make_mpf(from_man_exp(x, 0))
    if isinstance(x, float):
        with mp.workprec(64):  # floats have 53-bit mantissas: exact here
            return mp.mpf(x)
    if isinstance(x, mp.mpc):
        if x.imag != 0:
            raise ValueError("complex entry with nonzero imaginary part: %r" % (x,))
        return x.real
    try:
        with mp.workprec(64):
            return mp.mpf(float(x))  # numpy scalars land here, exactly
    except (TypeError, ValueError):
        return mp.mpf(x)


def _mpf_to_arb(x):
    """Exact mpf -> arb. Self-checked: raises if the conversion rounded.

    An mpf is sign * man * 2^exp; we rebuild that product with the flint
    precision temporarily raised above the mantissa width so no rounding can
    occur, then assert exactness. The raw _mpf_ tuple is read WITHOUT
    re-wrapping in mp.mpf(), because the mpf constructor re-rounds to the
    ambient dps and would silently truncate wide-mantissa entries (the exact
    silent-precision-loss failure this module exists to prevent).
    """
    if not isinstance(x, mp.mpf):
        x = _exact_mpf(x)
    sign, man, exp, _bc = x._mpf_
    if man == 0:
        if exp == 0:
            return arb(0)
        raise ValueError("non-finite entry cannot be certified: %r" % (x,))
    old = _fctx.prec
    try:
        _fctx.prec = max(old, man.bit_length() + 16)
        v = arb(-man if sign else man) * (arb(2) ** exp)
    finally:
        _fctx.prec = old
    if not v.is_exact():
        raise AssertionError("mpf->arb conversion rounded (bug)")
    return v


def _exact_arb_to_mpf(a):
    """Exact arb (radius zero) -> exact mpf, independent of mp.dps."""
    if not a.is_exact():
        raise AssertionError("expected an exact arb bound, got a ball")
    man, exp = a.mid().man_exp()
    return mp.make_mpf(from_man_exp(int(man), int(exp)))


def _arb_lo(a):
    """Rigorous mpf lower bound of an arb ball (rounded down by arb)."""
    return _exact_arb_to_mpf(a.lower())


def _arb_hi(a):
    """Rigorous mpf upper bound of an arb ball (rounded up by arb)."""
    return _exact_arb_to_mpf(a.upper())


def _as_mp_matrix(X, name):
    """Normalize input (mp.matrix, nested lists, numpy array) to mp.matrix."""
    if isinstance(X, mp.matrix):
        rows = [[X[i, j] for j in range(X.cols)] for i in range(X.rows)]
    else:
        try:
            rows = [list(r) for r in X]
        except TypeError:
            raise ValueError("%s: expected a matrix-like object" % name)
    n = len(rows)
    if n == 0 or any(len(r) != n for r in rows):
        raise ValueError("%s: matrix must be square and nonempty" % name)
    M = mp.matrix(n, n)
    for i in range(n):
        for j in range(n):
            v = _exact_mpf(rows[i][j])
            if not mp.isfinite(v):
                raise ValueError("%s[%d,%d] is not finite" % (name, i, j))
            M[i, j] = v
    for i in range(n):
        for j in range(i + 1, n):
            if M[i, j] != M[j, i]:
                # the consumers build exactly symmetric Grams; a mismatch here
                # means the caller sent the wrong object, not roundoff
                raise ValueError(
                    "%s is not exactly symmetric at (%d,%d); symmetrize at the "
                    "call site if that is intended" % (name, i, j))
    return M


# ----------------------------------------------------------------------------
# result containers
# ----------------------------------------------------------------------------

class EigEnclosure:
    """Enclosure of the smallest eigenvalue of a symmetric pencil (A, B).

    Fields:
      lo, hi        rigorous bounds (exact mpf) when certified=True
      radius        (hi - lo) / 2
      mu            approximate smallest eigenvalue (for display / seeding)
      vec           approximate eigenvector, B-normalized mp.matrix, or None
      residual_bound  certified ||A v - mu B v||_{B^{-1}} / ||v||_B, or None;
                      by the symmetric residual theorem some eigenvalue lies
                      within this distance of mu
      gap_lower     certified lower bound on the distance from the smallest
                    eigenvalue interval to the rest of the spectrum, or None
      sin_theta_bound  certified Davis-Kahan bound on the angle between vec
                    and the true ground eigenvector (B-inner-product), or None
      certified     True only on the ball-arithmetic route with all proofs done
      spd_certified True/False when B was checked, None for B=None
      isolated      whether flint isolated every eigenvalue (False = cluster
                    enclosures: containment holds, interval honestly wide)
      route         "flint" or "mpmath-fallback"
      mode          eig algorithm actually used
      prec_bits     working precision (bits) of the successful attempt
      notes         list of human-readable caveats
    """

    def __init__(self, **kw):
        self.n = kw["n"]
        self.dps = kw["dps"]
        self.prec_bits = kw["prec_bits"]
        self.route = kw["route"]
        self.mode = kw["mode"]
        self.isolated = kw["isolated"]
        self.certified = kw["certified"]
        self.spd_certified = kw["spd_certified"]
        self.lo = kw["lo"]
        self.hi = kw["hi"]
        self.mu = kw["mu"]
        self.vec = kw["vec"]
        self.residual_bound = kw["residual_bound"]
        self.gap_lower = kw["gap_lower"]
        self.sin_theta_bound = kw["sin_theta_bound"]
        self.notes = kw["notes"]
        if mp.isfinite(self.lo) and mp.isfinite(self.hi):
            with mp.workprec(max(self.prec_bits + 20, 120)):
                self.radius = (self.hi - self.lo) / 2
        else:
            self.radius = mp.inf

    def as_dict(self):
        return {
            "n": self.n, "dps": self.dps, "prec_bits": self.prec_bits,
            "route": self.route, "mode": self.mode, "isolated": self.isolated,
            "certified": self.certified, "spd_certified": self.spd_certified,
            "lo": self.lo, "hi": self.hi, "radius": self.radius, "mu": self.mu,
            "vec": self.vec, "residual_bound": self.residual_bound,
            "gap_lower": self.gap_lower,
            "sin_theta_bound": self.sin_theta_bound, "notes": list(self.notes),
        }

    def __repr__(self):
        tag = "CERTIFIED" if self.certified else "UNCERTIFIED"
        return ("<EigEnclosure %s route=%s mode=%s lam_min in [%s, %s] "
                "radius~%s>" % (tag, self.route, self.mode,
                                mp.nstr(self.lo, 12), mp.nstr(self.hi, 12),
                                mp.nstr(self.radius, 3)))


class LadderResult:
    """Trajectory of certify_smallest along a dps schedule.

    converged: some step reached a certified radius < tol.
    starved:   the schedule ended without convergence (the detector firing).
    stalled:   a consecutive certified pair shrank by less than 2x, i.e. more
               digits bought no accuracy: the classic starvation signature.
    """

    def __init__(self, steps, tol, final):
        self.steps = steps
        self.tol = tol
        self.final = final
        self.converged = any(
            s["certified"] and s["radius"] < tol for s in steps)
        self.starved = not self.converged
        self.stalled = False
        cert_radii = [s["radius"] for s in steps
                      if s["certified"] and mp.isfinite(s["radius"])]
        for a, b in zip(cert_radii, cert_radii[1:]):
            if a > 0 and b / a > mp.mpf("0.5"):
                self.stalled = True

    def __repr__(self):
        return ("<LadderResult %s steps=%d final_radius~%s tol=%s>" %
                ("CONVERGED" if self.converged else "STARVED", len(self.steps),
                 mp.nstr(self.final.radius, 3) if self.final else "?",
                 mp.nstr(mp.mpf(self.tol), 3)))


# ----------------------------------------------------------------------------
# approximate solve (mpmath): seeds the vector and the residual certificate
# ----------------------------------------------------------------------------

def _approx_smallest_mp(A, B, dps):
    """Approximate (mu, v) for the pencil, v B-normalized, via the same
    Cholesky reduction the e2ar/e2as consumers use. Not rigorous by itself:
    every number it produces is later re-checked in ball arithmetic."""
    n = A.rows
    with mp.workdps(dps + 10):
        if B is None:
            E, V = mp.eigsy(mp.matrix(A))
            i0 = min(range(n), key=lambda i: mp.re(E[i]))
            mu = mp.re(E[i0])
            v = mp.matrix([V[r, i0] for r in range(n)])
            nrm = mp.sqrt(sum(v[r] ** 2 for r in range(n)))
        else:
            L = mp.cholesky(mp.matrix(B))
            Li = mp.inverse(L)
            M = Li * mp.matrix(A) * Li.T
            M = (M + M.T) / 2  # kill rounding drift before eigsy
            E, V = mp.eigsy(M)
            i0 = min(range(n), key=lambda i: mp.re(E[i]))
            mu = mp.re(E[i0])
            v = Li.T * mp.matrix([V[r, i0] for r in range(n)])
            nrm = mp.sqrt(mp.re((v.T * (mp.matrix(B) * v))[0]))
        if nrm <= 0 or not mp.isfinite(nrm):
            raise ValueError("degenerate approximate eigenvector")
        for r in range(n):
            v[r] = v[r] / nrm
    return mu, v


# ----------------------------------------------------------------------------
# flint route
# ----------------------------------------------------------------------------

def _eig_balls_retry(make_target, prec, max_prec_mult):
    """Certified spectrum enclosure with a bounded escalation ladder.

    Isolation first (rump, then the default algorithm), doubling precision up
    to max_prec_mult; only then cluster enclosures (multiple=True), which keep
    containment when isolation is hopeless. Escalating precision is legitimate
    refinement because the target matrix entries are exact (or rebuilt at the
    escalated precision by make_target).
    """
    mults = [m for m in (1, 2, 4) if m <= max_prec_mult]
    for phase in ("isolated", "multiple"):
        for m in mults:
            p = prec * m
            _fctx.prec = p
            target = make_target()
            if phase == "isolated":
                for algo in ("rump", None):
                    try:
                        E = target.eig(algorithm=algo)
                    except ValueError:
                        continue
                    if all(e.is_finite() for e in E):
                        return E, True, (algo or "vdh_mourrain"), p
            else:
                try:
                    E = target.eig(multiple=True)
                except (ValueError, NotImplementedError):
                    continue
                if all(e.is_finite() for e in E):
                    return E, False, "multiple", p
    return None, False, "failed", prec


def _certify_flint(A, B, dps, prec, want_vector, max_prec_mult, notes):
    n = A.rows
    Aarb = arb_mat([[_mpf_to_arb(A[i, j]) for j in range(n)] for i in range(n)])
    Barb = None
    spd_certified = None
    if B is not None:
        Barb = arb_mat([[_mpf_to_arb(B[i, j]) for j in range(n)]
                        for i in range(n)])
        # SPD proof: enclose ALL of B's spectrum; a positive lower bound on
        # the union is a proof, and it is what licenses both the pencil
        # reduction and the residual theorem below
        bballs, _biso, _bmode, _bp = _eig_balls_retry(
            lambda: acb_mat(Barb), prec, max_prec_mult)
        if bballs is None:
            notes.append("could not enclose spectrum(B); SPD unproven")
            spd_certified = False
        else:
            bmin = min(_arb_lo(e.real) for e in bballs)
            spd_certified = bool(bmin > 0)
            if not spd_certified:
                notes.append("B not certified positive definite "
                             "(lambda_min(B) lower bound %s)" % mp.nstr(bmin, 6))

    def make_target():
        if Barb is None:
            return acb_mat(Aarb)
        # verified solve: the balls of B^{-1}A contain the true pencil matrix,
        # so certified eig on them encloses the true pencil spectrum
        return acb_mat(Barb.solve(Aarb))

    try:
        balls, isolated, mode, prec_used = _eig_balls_retry(
            make_target, prec, max_prec_mult)
    except ZeroDivisionError:
        balls, isolated, mode, prec_used = None, False, "failed", prec
        notes.append("B numerically singular at working precision")

    if balls is None:
        notes.append("flint eigensolver failed at all attempted precisions; "
                     "raise dps")
        return EigEnclosure(
            n=n, dps=dps, prec_bits=prec_used, route="flint", mode=mode,
            isolated=False, certified=False, spd_certified=spd_certified,
            lo=mp.ninf, hi=mp.inf, mu=None, vec=None, residual_bound=None,
            gap_lower=None, sin_theta_bound=None, notes=notes)

    if not isolated:
        notes.append("eigenvalues not isolated at this precision: cluster "
                     "enclosures used; interval is honestly wide (this is "
                     "the precision-starvation signature)")

    # the pencil spectrum is real (A symmetric, B SPD), so real-interval
    # projections of the balls are rigorous; lambda_min lies in
    # [min of lower bounds, min of upper bounds] regardless of which ball
    # holds it
    los = [_arb_lo(e.real) for e in balls]
    his = [_arb_hi(e.real) for e in balls]
    lo = min(los)
    i_star = min(range(len(his)), key=lambda i: his[i])
    hi = his[i_star]
    others_lo = (min(los[j] for j in range(len(los)) if j != i_star)
                 if len(los) > 1 else None)

    gap_lower = None
    if others_lo is not None:
        _fctx.prec = prec_used
        g = (_mpf_to_arb(others_lo) - _mpf_to_arb(hi)).lower()
        gmp = _exact_arb_to_mpf(g)
        if gmp > 0:
            gap_lower = gmp

    # approximate pair: seeds the vector output and the Rump-style residual
    # tightening; its numbers are exact dyadics so re-checking them in arb
    # costs nothing in rigor
    mu = vec = None
    residual_bound = sin_theta_bound = None
    if want_vector:
        try:
            mu, vec = _approx_smallest_mp(A, B, dps)
        except Exception as ex:
            notes.append("approximate eigenpair unavailable (%s); value "
                         "enclosure unaffected" % type(ex).__name__)
    if vec is not None and (B is None or spd_certified):
        _fctx.prec = 2 * prec_used  # residual cancels catastrophically:
        # entries are exact so doubling precision recovers it rigorously
        v_arb = arb_mat([[_mpf_to_arb(vec[r])] for r in range(n)])
        mu_arb = _mpf_to_arb(mu)
        Av = Aarb * v_arb
        Bv = (Barb * v_arb) if Barb is not None else v_arb
        r_col = Av - Bv * mu_arb
        y = Barb.solve(r_col) if Barb is not None else r_col
        num = (r_col.transpose() * y)[0, 0]
        den = (v_arb.transpose() * Bv)[0, 0]
        den_lo = den.lower()
        if den_lo > 0:
            num_hi = num.upper()
            if num_hi < 0:
                num_hi = arb(0)
            eps_ball = (num_hi / den_lo).sqrt()
            eps_hi = eps_ball.upper()
            residual_bound = _exact_arb_to_mpf(eps_hi)
            if others_lo is not None:
                others_arb = _mpf_to_arb(others_lo)
                mu_plus = _exact_arb_to_mpf((mu_arb + eps_hi).upper())
                mu_minus = _exact_arb_to_mpf((mu_arb - eps_hi).lower())
                if _mpf_to_arb(mu_plus) < others_arb:
                    # the residual theorem puts SOME eigenvalue within eps of
                    # mu; everything except lambda_min is certified above
                    # mu + eps, so that eigenvalue IS lambda_min: intersect
                    new_lo, new_hi = max(lo, mu_minus), min(hi, mu_plus)
                    if new_lo <= new_hi:
                        lo, hi = new_lo, new_hi
                    else:
                        notes.append("residual interval inconsistent with "
                                     "spectrum enclosure; kept the wider one")
                    delta = (others_arb - mu_arb).lower()
                    if delta > eps_hi:
                        sin_theta_bound = _exact_arb_to_mpf(
                            (eps_hi / delta).upper())
        else:
            notes.append("could not lower-bound ||v||_B > 0; residual "
                         "certificate skipped")

    certified = bool(B is None or spd_certified)
    if not certified:
        notes.append("enclosure reported but NOT certified (SPD proof for B "
                     "is missing)")
    if mu is None:
        with mp.workprec(max(prec_used, 120)):
            mu = (lo + hi) / 2
    return EigEnclosure(
        n=n, dps=dps, prec_bits=prec_used, route="flint", mode=mode,
        isolated=isolated, certified=certified, spd_certified=spd_certified,
        lo=lo, hi=hi, mu=mu, vec=vec, residual_bound=residual_bound,
        gap_lower=gap_lower, sin_theta_bound=sin_theta_bound, notes=notes)


# ----------------------------------------------------------------------------
# mpmath fallback (never claims certification)
# ----------------------------------------------------------------------------

def _certify_fallback(A, B, dps, prec, want_vector, notes):
    n = A.rows
    dps2 = int(1.5 * dps) + 30
    mu1, _v1 = _approx_smallest_mp(A, B, dps)
    mu2, v2 = _approx_smallest_mp(A, B, dps2)
    with mp.workdps(dps2 + 20):
        Am, Bm = mp.matrix(A), (mp.matrix(B) if B is not None else None)
        r = Am * v2 - mu2 * (Bm * v2 if Bm is not None else v2)
        if Bm is not None:
            num = mp.re((r.T * mp.lu_solve(Bm, r))[0])
            den = mp.re((v2.T * (Bm * v2))[0])
        else:
            num = mp.re((r.T * r)[0])
            den = mp.re((v2.T * v2)[0])
        eps_est = mp.sqrt(max(num, mp.mpf(0)) / den) if den > 0 else mp.inf
        scale = max(mp.mpf(1), abs(mu2))
        # explicit slack: cross-precision drift + residual estimate + a
        # floor at the working epsilon, all times 10; honest but NOT a proof
        slack = 10 * (abs(mu1 - mu2) + eps_est + scale * mp.mpf(10) ** (-dps2))
        lo, hi = mu2 - slack, mu2 + slack
    notes.append("mpmath fallback: high-confidence, not directed-rounding "
                 "rigorous (install python-flint for certification)")
    return EigEnclosure(
        n=n, dps=dps, prec_bits=prec, route="mpmath-fallback",
        mode="eigsy+slack", isolated=False, certified=False,
        spd_certified=None, lo=lo, hi=hi, mu=mu2,
        vec=(v2 if want_vector else None), residual_bound=None,
        gap_lower=None, sin_theta_bound=None, notes=notes)


# ----------------------------------------------------------------------------
# public API
# ----------------------------------------------------------------------------

def certify_smallest(A, B=None, dps=None, want_vector=True, use_flint=True,
                     max_prec_mult=4):
    """Rigorous enclosure of the smallest eigenvalue of the pencil (A, B).

    A: symmetric real matrix (mp.matrix, nested lists, or numpy array).
    B: optional symmetric positive definite matrix for the generalized
       problem A v = lambda B v; B's definiteness is itself certified.
    dps: decimal working precision (default: current mp.mp.dps). Entries are
       consumed exactly; dps controls only the certification arithmetic.
    use_flint: set False to force the (uncertified) mpmath fallback.
    max_prec_mult: internal precision-escalation cap for the flint solver
       (1 disables escalation; precision_ladder uses that so starvation at
       the REQUESTED dps stays visible instead of being silently rescued).

    Returns an EigEnclosure. certified=True only on the ball-arithmetic
    route with every proof obligation discharged.
    """
    if dps is None:
        dps = mp.mp.dps
    dps = int(dps)
    if dps < 5:
        raise ValueError("dps too small to mean anything: %d" % dps)
    prec = int(dps * _LOG2_10) + 30
    A = _as_mp_matrix(A, "A")
    Bm = None
    if B is not None:
        Bm = _as_mp_matrix(B, "B")
        if Bm.rows != A.rows:
            raise ValueError("A and B must have the same dimension")
    notes = []
    if use_flint and HAVE_FLINT:
        old = _fctx.prec
        try:
            return _certify_flint(A, Bm, dps, prec, want_vector,
                                  max(1, int(max_prec_mult)), notes)
        finally:
            _fctx.prec = old
    if use_flint and not HAVE_FLINT:
        notes.append("python-flint not importable; fell back to mpmath")
    return _certify_fallback(A, Bm, dps, prec, want_vector, notes)


def precision_ladder(builder_fn, dps_list, tol, use_flint=True, **kw):
    """Automatic precision-starvation detector.

    builder_fn(dps) must return A or (A, B) REBUILT at that dps (matching the
    consumers, whose Gram entries are recomputed per rung). The ladder
    certifies at each dps in ascending order, stops as soon as a certified
    radius drops below tol, and reports the whole trajectory. Escalation
    inside certify_smallest is disabled (max_prec_mult=1) so each rung
    measures the requested precision honestly: a radius that fails to shrink
    rung-to-rung is starvation, and result.starved / result.stalled say so.
    """
    tol = mp.mpf(tol)
    kw.setdefault("want_vector", False)
    kw.setdefault("max_prec_mult", 1)
    steps = []
    final = None
    prev_radius = None
    for dps in dps_list:
        built = builder_fn(int(dps))
        Ab, Bb = built if isinstance(built, tuple) else (built, None)
        cert = certify_smallest(Ab, Bb, dps=int(dps), use_flint=use_flint,
                                **kw)
        shrink = None
        if (prev_radius is not None and mp.isfinite(prev_radius)
                and prev_radius > 0 and mp.isfinite(cert.radius)):
            shrink = cert.radius / prev_radius
        steps.append({
            "dps": int(dps), "lo": cert.lo, "hi": cert.hi,
            "radius": cert.radius, "certified": cert.certified,
            "isolated": cert.isolated, "mode": cert.mode, "shrink": shrink,
        })
        final = cert
        prev_radius = cert.radius
        if cert.certified and cert.radius < tol:
            break
    return LadderResult(steps, tol, final)
