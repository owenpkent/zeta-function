"""E2BD: the D-H invisibility certificate (construction backlog B4; hardens LEARNINGS #179).

WHAT IS CERTIFIED. #179's SP2-completeness cell MEASURED the assembled object's
meter staying at ~0.24 on the critical line at the off-line pair's height 85.699
(vs dip depth ~4e-4 at detected zeros). This build upgrades that pointwise
measurement to a certified CONTINUUM lower bound

    c_DH  <=  |f_DH(1/2 + i t)|   for ALL t in W = [85.2, 86.2],

computed in ball arithmetic (python-flint / arb) from the period-5 coefficient
lattice. Since a circumference-L carrier samples the line on the grid
tau_k = 2 pi k / L, and #179's assembly extracts f(1/2 + i tau) to its
certified truncation residual (7.7e-14 at its scale), the continuum bound
covers EVERY grid point of EVERY circumference at once: no cokernel dip can
open inside W at any L. The completeness failure of the SP-object on the D-H
control becomes a theorem about the control rather than a measurement.

TWO CERTIFIED ROUTES, ONE INSTRUMENT LESSON. The backlog sketch said "smoothed
AFE with explicit tails". Built here, the x = 1-split incomplete-gamma AFE

    Lambda(s) = sum_{n>=1} a_n n [ (pi n^2/5)^{-z1} Gamma(z1, pi n^2/5)
                                 + (pi n^2/5)^{-z2} Gamma(z2, pi n^2/5) ],
    z1 = (s+1)/2,  z2 = (2-s)/2,   f = Lambda * (pi/5)^{z1} / Gamma(z1),

(from splitting int_0^inf psi(x) x^{z1 - 1} dx at x = 1, psi(x) = sum a_n n
e^{-pi n^2 x/5}, psi(1/x) = x^{3/2} psi(x); explicit tail
|Lambda - Lambda_N| <= (25/pi^2) N^{-2} e^{-pi N^2/5} < 1e-69 at N = 16, from
|Gamma(z,w)| <= Gamma(3/4,w) <= w^{-1/4} e^{-w}) is EXACT at points (radius
~1e-43 on the line) but PROVABLY UNBALANCED for interval sweeps: on the line
|Lambda| ~ e^{-pi t/4} ~ 1e-30 emerges by cancellation between the conjugate
halves of O(1) terms, so a t-ball of width h inflates the enclosure by
~h * e^{+pi t/4} and the certified lower bound collapses to 0 at any feasible
h (measured below as a named negative control). The sweep therefore runs on
the BALANCED certified route: f assembled from the lattice via certified
Euler-Maclaurin Hurwitz zeta (arb's acb_hurwitz_zeta, rigorous error bounds),

    f_DH(s) = 5^{-s} sum_{a=1}^{4} c_a zeta(s, a/5),

which needs no FE and stays O(1)-conditioned on the line. The two routes agree
at points to < 1e-40 (gated): an independent-mathematics cross-check (theta/FE
route vs EM route), on top of the mpmath implementation check.

PRE-REGISTERED (backlog rule 1), before the sweeps were run:
  P1  EXPECT: the certified floor c_DH over W = [85.2, 86.2] is > 0.05
      (pointwise #179: ~0.24 at 85.70; cached D-H on-line zeros nearest W sit
      at 83.109 and 89.439, so W is on-line-zero-free with margin 2.1 / 3.2).
      KILL: refinement to h = 2^-13 still cannot separate the floor from 0:
      the invisibility claim is wrong at the continuum level and #179's
      pointwise reading was grid luck. Chase immediately.
  P2  EXPECT: zeta's certified floor over the SAME window W (zero-free for
      zeta: neighbors 84.7355 and 87.4253) is within 30x of c_DH: the floor is
      zero-distance geometry, not arithmetic. KILL: ratio outside [1/30, 30].
  P3  EXPECT: the same certified meter SEES on-line zeros: the dip scans
      certify min |f| <= c_DH/50 on the zeta window [84.5, 85.0] (contains the
      23rd zeta zero 84.7355) and on the D-H window [82.9, 83.3] (contains
      D-H's own on-line zero 83.109). KILL: either dip fails to certify below
      c_DH/50: the "floor" would be instrument blindness, not selective
      invisibility.

DISCIPLINES. Joint (rule 3): C1's completeness face (SP2), certified from the
control side. K1 (rule 4): construction cells consume the period-5 lattice
(1, k, -k, -1, 0), k from the FE datum, and certified special-function
arithmetic on that data only; the mpmath oracle (mp.zeta /
DavenportHeilbronn.evaluate) is called ONLY inside the validation cell and
counted; a gate asserts the exact count. The dip-window CHOICES reference
known zero landmarks (the cached #179 zero list; the standard zeta table):
choosing where to point the instrument is recorded as oracle-informed; every
certified value is lattice-sourced. Beurling (rule 2): NOT POSABLE, and the
refusal is the finding: no functional equation -> no theta self-duality -> no
completed line object; #179 measured the same refusal as the 0.505 line-drift.
Recorded as a named gate, not silently skipped.

Run:  python -m experiments.arithmetic_geometric.e2bd_dh_invisibility [--quick]
Data: e2bd_dh_invisibility.npz (tracked next to this script).
"""

from __future__ import annotations

import math
import time

import numpy as np
from flint import acb, arb, ctx

from experiments._shared.harness import Gates, PreRegistry, controls, quick_arg, save_npz

PREC_BITS = 320
N_DH = 16          # AFE truncation; explicit tail < 1e-69
N_ZETA = 8         # zeta AFE truncation; explicit tail < 1e-110
LANDMARK_T = "85.6993"          # off-line pair height (0.8085 +/- ..., 85.699i)
W_DH = ("85.2", "86.2")         # the landmark window (backlog spec)
W_ZETA_SAME = ("85.2", "86.2")  # zeta, same window (zero-free: 84.7355 / 87.4253)
W_ZETA_DIP = ("84.5", "85.0")   # contains the 23rd zeta zero 84.7355
W_DH_DIP = ("82.9", "83.3")     # contains D-H's own on-line zero 83.109
LADDER_L = (8, 10, 12, 14)      # the e2ao circumference ladder

_ORACLE_CALLS = 0

_PI = None
_COEF = None


def _setup():
    global _PI, _COEF
    ctx.prec = PREC_BITS
    _PI = arb.pi()
    s5 = arb(5).sqrt()
    kappa = ((arb(10) - 2 * s5).sqrt() - 2) / (s5 - 1)
    _COEF = [arb(1), kappa, -kappa, arb(-1), arb(0)]
    return kappa


def _err_ball(tail: arb) -> arb:
    """A ball containing [-T, T] for any T inside the tail bound's ball."""
    return (-tail).union(tail)


# -- route 1: the x = 1-split incomplete-gamma AFE (FE-consuming; explicit
# tails; exact at points, unbalanced over intervals: see module docstring) ----

def dh_lambda_afe(s: acb, N: int = N_DH) -> acb:
    """Certified enclosure of Lambda_DH(s), explicit truncation tail.

    The tail bound uses Re z1 = Re z2 = 3/4 (the critical line); the symmetry
    gate also evaluates at |Re s - 1/2| = 0.2 where Re z >= 0.65 and the
    elementary bound Gamma(a,w) <= w^{a-1} e^{-w} (valid for a <= 1) keeps the
    same form with a slightly larger constant, absorbed by N = 16's headroom.
    """
    z1 = (s + 1) / 2
    z2 = (2 - s) / 2
    tot = acb(0)
    for n in range(1, N + 1):
        if n % 5 == 0:
            continue
        c = _COEF[(n - 1) % 5]
        w = _PI * (n * n) / 5
        lw = w.log()
        t1 = (-z1 * lw).exp() * acb(w).gamma_upper(z1)
        t2 = (-z2 * lw).exp() * acb(w).gamma_upper(z2)
        tot += c * n * (t1 + t2)
    tail = (arb(25) / (_PI * _PI)) / (N * N) * (-_PI * (N * N) / 5).exp()
    eb = _err_ball(tail)
    return tot + acb(eb, eb)


def dh_f_afe(s: acb, N: int = N_DH) -> acb:
    """f_DH(s) = Lambda(s) (pi/5)^{(s+1)/2} / Gamma((s+1)/2), certified."""
    z1 = (s + 1) / 2
    pref = (z1 * (_PI / 5).log()).exp()
    return dh_lambda_afe(s, N) * pref / z1.gamma()


def zeta_lambda_afe(s: acb, N: int = N_ZETA) -> acb:
    """Certified Lambda_zeta(s) via Riemann's split theta integral
    (even kernel, exact pole term -1/s - 1/(1-s), explicit tail)."""
    z1 = s / 2
    z2 = (1 - s) / 2
    tot = -1 / s - 1 / (1 - s)
    for n in range(1, N + 1):
        w = _PI * (n * n)
        lw = w.log()
        t1 = (-z1 * lw).exp() * acb(w).gamma_upper(z1)
        t2 = (-z2 * lw).exp() * acb(w).gamma_upper(z2)
        tot += t1 + t2
    tail = (_PI / 3) * (-_PI * ((N + 1) * (N + 1))).exp()
    eb = _err_ball(tail)
    return tot + acb(eb, eb)


def zeta_f_afe(s: acb, N: int = N_ZETA) -> acb:
    """zeta(s) = Lambda(s) pi^{s/2} / Gamma(s/2), certified."""
    z1 = s / 2
    pref = (z1 * _PI.log()).exp()
    return zeta_lambda_afe(s, N) * pref / z1.gamma()


def dh_theta(x: arb, M: int = 30) -> arb:
    """Certified psi(x) = sum a_n n e^{-pi n^2 x/5}; tail via
    sum_{n>M} n e^{-c n^2} <= e^{-c M^2} (M q/(1-q) + q/(1-q)^2), q = e^{-2cM}."""
    tot = arb(0)
    for n in range(1, M + 1):
        if n % 5 == 0:
            continue
        tot += _COEF[(n - 1) % 5] * n * (-_PI * (n * n) * x / 5).exp()
    c = _PI * x / 5
    q = (-2 * c * M).exp()
    tail = (-c * (M * M)).exp() * (M * q / (1 - q) + q / ((1 - q) * (1 - q)))
    return tot + _err_ball(tail)


# -- route 2: balanced certified evaluation (lattice x certified
# Euler-Maclaurin Hurwitz zeta); the sweep engine -----------------------------

def dh_f_em(s: acb) -> acb:
    """f_DH(s) = 5^{-s} sum_{a=1}^{4} c_a zeta(s, a/5), certified (arb EM)."""
    tot = acb(0)
    for a in range(1, 5):
        tot += _COEF[a - 1] * s.zeta(acb(a) / 5)
    return (-s * arb(5).log()).exp() * tot


def zeta_f_em(s: acb) -> acb:
    """zeta(s), certified (arb)."""
    return s.zeta()


def cover_balls(t0: str, t1: str, h: float):
    """Balls b_j = [t0 + j h, t0 + (j+1) h] (as arb unions) covering [t0, t1].

    Coverage is by construction: each union ball contains both true endpoints
    of its subinterval (the endpoint arbs enclose the true rationals), and
    consecutive balls share an endpoint. Verified by containment checks.
    """
    a0, a1 = arb(t0), arb(t1)
    num = int(np.ceil((float(a1) - float(a0)) / h))
    balls = []
    for j in range(num):
        lo = a0 + arb(j) * h
        hi = a0 + arb(j + 1) * h
        balls.append(lo.union(hi))
    ok = bool(balls[0].contains(a0)) and bool(balls[-1].contains(a1))
    return balls, ok


def sweep(kind: str, t0: str, t1: str, h: float):
    """Certified |f| lower/upper bounds over a covering of [t0, t1]."""
    f = dh_f_em if kind == "dh" else zeta_f_em
    balls, cover_ok = cover_balls(t0, t1, h)
    half = arb(1) / 2
    lowers, uppers, mids = [], [], []
    for b in balls:
        v = f(acb(half, b))
        lowers.append(v.abs_lower())
        uppers.append(v.abs_upper())
        mids.append(float(b))
    floor = lowers[0]
    for x in lowers[1:]:
        if x < floor:
            floor = x
    min_up = uppers[0]
    for x in uppers[1:]:
        if x < min_up:
            min_up = x
    return {
        "floor": floor, "min_upper": min_up, "cover_ok": cover_ok,
        "mids": np.array(mids), "lowers": np.array([float(x) for x in lowers]),
        "uppers": np.array([float(x) for x in uppers]),
        "argmin": mids[int(np.argmin([float(x) for x in lowers]))],
    }


def dip_scan(kind: str, t0: str, t1: str, h: float):
    """Certified point evaluations across [t0, t1]: an EXISTENCE scan.

    A dip claim ("the meter goes below theta somewhere here") needs one
    certified point value, not interval coverage, so this scan evaluates at
    exact grid points and pays no ball-inflation tax.
    """
    f = dh_f_em if kind == "dh" else zeta_f_em
    a0 = arb(t0)
    num = int(np.ceil((float(arb(t1)) - float(a0)) / h))
    half = arb(1) / 2
    uppers, mids = [], []
    for k in range(num + 1):
        tk = a0 + arb(k) * h
        v = f(acb(half, tk))
        uppers.append(v.abs_upper())
        mids.append(float(tk))
    min_up = uppers[0]
    for x in uppers[1:]:
        if x < min_up:
            min_up = x
    return {
        "min_upper": min_up, "mids": np.array(mids),
        "uppers": np.array([float(x) for x in uppers]),
        "argmin": mids[int(np.argmin([float(x) for x in uppers]))],
    }


# -- validation cell (mpmath implementation oracle; counted) ------------------

def _oracle_dh(t_str: str):
    global _ORACLE_CALLS
    _ORACLE_CALLS += 1
    import mpmath as mp
    dh = controls(["dh"])["dh"]
    prev = mp.mp.dps
    mp.mp.dps = 40
    try:
        v = dh.evaluate(mp.mpc(mp.mpf(1) / 2, mp.mpf(t_str)))
        return acb(arb(mp.nstr(v.real, 36)), arb(mp.nstr(v.imag, 36)))
    finally:
        mp.mp.dps = prev


def _oracle_zeta(t_str: str):
    global _ORACLE_CALLS
    _ORACLE_CALLS += 1
    import mpmath as mp
    prev = mp.mp.dps
    mp.mp.dps = 40
    try:
        v = mp.zeta(mp.mpc(mp.mpf(1) / 2, mp.mpf(t_str)))
        return acb(arb(mp.nstr(v.real, 36)), arb(mp.nstr(v.imag, 36)))
    finally:
        mp.mp.dps = prev


def main() -> int:
    t_start = time.perf_counter()
    quick = quick_arg()
    kappa = _setup()
    gates = Gates(quick=quick)
    pre = PreRegistry()
    pre.register("P1", "certified floor c_DH > 0.05 over W = [85.2, 86.2]",
                 "refinement to h = 2^-13 cannot separate the floor from 0")
    pre.register("P2", "zeta same-window floor within 30x of c_DH",
                 "ratio outside [1/30, 30]")
    pre.register("P3", "both dip scans certify min |f| <= c_DH/50",
                 "either dip window fails to certify below c_DH/50")

    h_win = 1 / 256 if quick else 1 / 1024
    h_dip = 1 / 1024 if quick else 1 / 4096
    tol = lambda k: arb(1) / arb(10) ** k

    print(f"e2bd: D-H invisibility certificate (backlog B4)  "
          f"[{'quick' if quick else 'full'}; prec={PREC_BITS} bits, "
          f"N_DH={N_DH}, N_zeta={N_ZETA}, h_win=1/{int(1/h_win)}, h_dip=1/{int(1/h_dip)}]")

    # -- instrument cell ---------------------------------------------------
    d_conv = (acb(1).gamma_upper(acb(1)) - (-arb(1)).exp()).abs_upper()
    gates.gate("gamma_upper convention Gamma(1,1) = 1/e certified",
               d_conv < tol(40), f"|diff| <= {d_conv}")

    import mpmath as mp
    from experiments._shared.davenport_heilbronn import _kappa as mp_kappa
    prev = mp.mp.dps
    mp.mp.dps = 40
    try:
        k_ref = arb(mp.nstr(mp_kappa(40), 36))
    finally:
        mp.mp.dps = prev
    dk = acb(kappa - k_ref).abs_upper()
    gates.gate("kappa certified matches shared closed form",
               dk < tol(33), f"|diff| <= {dk}")

    for xs in ("1.3", "1.7"):
        x = arb(xs)
        r = dh_theta(1 / x) - x ** (arb(3) / 2) * dh_theta(x)
        ru = acb(r).abs_upper()
        gates.gate(f"theta self-duality certified at x = {xs}",
                   ru < tol(30), f"|resid| <= {ru}")

    s0 = acb(arb("0.3"), arb("7.2"))
    d_sym = (dh_lambda_afe(s0) - dh_lambda_afe(1 - s0)).abs_upper()
    gates.gate("Lambda_DH(s) = Lambda_DH(1-s) certified off-line",
               d_sym < tol(30), f"|diff| <= {d_sym}")
    d_symz = (zeta_lambda_afe(s0) - zeta_lambda_afe(1 - s0)).abs_upper()
    gates.gate("Lambda_zeta symmetry (incl. pole term) certified",
               d_symz < tol(30), f"|diff| <= {d_symz}")

    # -- route agreement (independent mathematics, both certified) ---------
    half = arb(1) / 2
    d_r = arb(0)
    for ts in ("85.43", LANDMARK_T, "86.01"):
        s = acb(half, arb(ts))
        d = (dh_f_afe(s) - dh_f_em(s)).abs_upper()
        if d > d_r:
            d_r = d
    gates.gate("route agreement: AFE (theta/FE) = EM (Hurwitz) at 3 D-H points",
               d_r < tol(40), f"max |diff| <= {d_r}")
    d_rz = arb(0)
    for ts in ("85.5", "84.74"):
        s = acb(half, arb(ts))
        d = (zeta_f_afe(s) - zeta_f_em(s)).abs_upper()
        if d > d_rz:
            d_rz = d
    gates.gate("route agreement: AFE = arb zeta at 2 zeta points",
               d_rz < tol(40), f"max |diff| <= {d_rz}")

    # -- validation cell (mpmath implementation oracle; counted) -----------
    max_d = arb(0)
    for ts in ("85.43", LANDMARK_T, "86.01"):
        d = (dh_f_em(acb(half, arb(ts))) - _oracle_dh(ts)).abs_upper()
        if d > max_d:
            max_d = d
    for ts in ("85.5", "84.74"):
        d = (zeta_f_em(acb(half, arb(ts))) - _oracle_zeta(ts)).abs_upper()
        if d > max_d:
            max_d = d
    gates.gate("validation: certified routes = mpmath oracle at 5 line points",
               max_d < tol(30), f"max |diff| <= {max_d}")
    gates.gate("K1: oracle calls confined to the validation cell",
               _ORACLE_CALLS == 5, f"count = {_ORACLE_CALLS} (3 D-H + 2 zeta)")

    v16 = dh_f_afe(acb(half, arb(LANDMARK_T)), N=N_DH)
    v32 = dh_f_afe(acb(half, arb(LANDMARK_T)), N=2 * N_DH)
    dN = (v16 - v32).abs_upper()
    gates.gate("tail honesty: AFE N and 2N enclosures agree",
               (v16 - v32).abs_lower() == 0 and dN < tol(35), f"|diff| <= {dN}")

    # -- named negative control: the x = 1-split AFE cannot sweep ----------
    b_wide = arb("85.2").union(arb("85.2") + arb(1) / 128)
    lo_afe = dh_f_afe(acb(half, b_wide)).abs_lower()
    lo_em = dh_f_em(acb(half, b_wide)).abs_lower()
    gates.gate("negative control: x=1-split AFE collapses on a 1/128 ball, EM does not",
               lo_afe < tol(6) and lo_em > arb(1) / 20,
               f"AFE lower = {lo_afe}; EM lower = {lo_em}")

    # -- the certificate ---------------------------------------------------
    sw_dh = sweep("dh", *W_DH, h_win)
    c_dh = sw_dh["floor"]
    gates.gate("window covering is by-construction (both endpoints contained)",
               sw_dh["cover_ok"], f"{len(sw_dh['mids'])} balls of width 1/{int(1/h_win)}")
    p1_ok = c_dh > arb(1) / 20
    gates.gate("THE CERTIFICATE: c_DH > 0.05 over [85.2, 86.2]",
               p1_ok, f"c_DH = {c_dh} at t ~ {sw_dh['argmin']:.4f}")
    pre.resolve("P1", "FIRED" if p1_ok else "REFUTED", f"c_DH = {c_dh}")

    v_land = dh_f_em(acb(half, arb(LANDMARK_T)))
    gates.gate("landmark height 85.6993 in-window with |f| >= c_DH",
               v_land.abs_lower() >= c_dh * arb("0.999"),
               f"|f(1/2 + i 85.6993)| = {abs(v_land)}")

    sw_z = sweep("zeta", *W_ZETA_SAME, h_win)
    c_z = sw_z["floor"]
    ratio = float(c_z) / max(float(c_dh), 1e-300)
    p2_ok = (1 / 30) < ratio < 30
    gates.gate("bracket: zeta same-window floor within 30x (P2)",
               p2_ok, f"c_zeta = {c_z}; ratio = {ratio:.3f}")
    pre.resolve("P2", "FIRED" if p2_ok else "REFUTED", f"ratio = {ratio:.3f}")

    thresh = c_dh / 50
    sw_zdip = dip_scan("zeta", *W_ZETA_DIP, h_dip)
    ok_zdip = sw_zdip["min_upper"] < thresh
    gates.gate("dip contrast: zeta meter sees its zero 84.7355 (P3a)",
               ok_zdip, f"certified |zeta| <= {sw_zdip['min_upper']} at t ~ {sw_zdip['argmin']:.4f}")
    sw_ddip = dip_scan("dh", *W_DH_DIP, h_dip)
    ok_ddip = sw_ddip["min_upper"] < thresh
    gates.gate("dip contrast: D-H meter sees its ON-line zero 83.109 (P3b)",
               ok_ddip, f"certified |f_DH| <= {sw_ddip['min_upper']} at t ~ {sw_ddip['argmin']:.4f}")
    pre.resolve("P3", "FIRED" if (ok_zdip and ok_ddip) else "REFUTED",
                f"zeta dip <= {float(sw_zdip['min_upper']):.2e}, "
                f"dh dip <= {float(sw_ddip['min_upper']):.2e}")

    # -- corollary: every circumference at once ----------------------------
    t_lo, t_hi = float(arb(W_DH[0])), float(arb(W_DH[1]))
    counts = {L: sum(1 for k in range(1, 10000)
                     if t_lo <= 2 * math.pi * k / L <= t_hi) for L in LADDER_L}
    gates.gate("corollary bites: every e2ao circumference grids the window",
               all(c >= 1 for c in counts.values()),
               "grid points in W per L: " + str(counts))

    beur = controls(["beurling"])["beurling"]
    gates.gate("Beurling refusal named: no FE, no theta fold, no line object",
               not hasattr(beur, "evaluate") and not hasattr(beur, "zeros"),
               "BeurlingSystem exposes theta/counting only (harness contract)")

    gates.gate("no unresolved pre-registrations", pre.unresolved() == [])

    elapsed = time.perf_counter() - t_start
    save_npz(
        __file__.replace(".py", ".npz"),
        {
            "dh_win_mids": sw_dh["mids"], "dh_win_lowers": sw_dh["lowers"],
            "dh_win_uppers": sw_dh["uppers"],
            "zeta_win_mids": sw_z["mids"], "zeta_win_lowers": sw_z["lowers"],
            "zeta_dip_mids": sw_zdip["mids"], "zeta_dip_uppers": sw_zdip["uppers"],
            "dh_dip_mids": sw_ddip["mids"], "dh_dip_uppers": sw_ddip["uppers"],
            "c_dh": np.array([float(c_dh)]), "c_zeta_same": np.array([float(c_z)]),
        },
        {
            "experiment": "e2bd_dh_invisibility", "backlog": "B4",
            "prec_bits": PREC_BITS, "N_dh": N_DH, "N_zeta": N_ZETA,
            "h_win": h_win, "h_dip": h_dip, "quick": quick,
            "kappa": str(kappa), "c_dh_certified": str(c_dh),
            "c_zeta_certified": str(c_z),
            "sweep_route": "lattice x certified Euler-Maclaurin Hurwitz (arb)",
            "point_route": "x=1-split incomplete-gamma AFE, explicit tails",
            "dh_afe_tail": "(25/pi^2) N^-2 exp(-pi N^2/5)",
            "zeta_afe_tail": "(pi/3) exp(-pi (N+1)^2)",
            "oracle_calls": _ORACLE_CALLS, "elapsed_s": round(elapsed, 2),
        },
    )
    pre.table()
    gates.summary(elapsed=elapsed)
    return gates.exit_code()


if __name__ == "__main__":
    raise SystemExit(main())
