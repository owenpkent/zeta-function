"""e3x: the Lonely Crystal (LCC) LP falsification instrument.

LCC (LEARNINGS #76, docs/03_research/first_principles_conjecture_program.md 3.1;
transported form in docs/03_research/lcc_bc_transport.md, LEARNINGS #82) recasts
RH as: the cone of positive log-crystals for the zeta explicit-formula source
contains exactly one point, the von Mangoldt crystal. A log-crystal is a pair
(mu, c), mu a positive tempered measure on R and c_n >= 0, satisfying for every
even test g in C_c^infty(R) with ghat(r) = int g(x) e^{irx} dx:

  (EF)  int ghat(r) dmu(r) = ghat(i/2) + ghat(-i/2) - 2 sum_{n>=1} c_n g(log n)
                             + (1/2pi) int ghat(r) Omega(r) dr,

with Omega(r) = Re psi(1/4 + ir/2) - log pi (project convention, e3aa/e3hh) and
ghat(i/2) + ghat(-i/2) = 2 int g(x) cosh(x/2) dx. The unit atom c_1 enters with
test coefficient -2 g(0). For the Davenport-Heilbronn source the analogue has NO
pole term and Omega_DH(r) = log 5 + Re psi(3/4 + ir/2) - log pi (conductor
sqrt(5), one Gamma_R(s+1) factor); Omega_DH(0) = -0.6212 (density -0.0989, the
"-0.099" of #76).

This script discretizes the cone and runs four falsification probes:

  (a) Blind crystal recovery (positive control). Comb FIXED to the von Mangoldt
      crystal c_n = Lambda(n)/sqrt(n); mu discretized as nonnegative weights on a
      UNIFORM r-grid; solve the truncated (EF) constraints by weighted NNLS. The
      known zero ordinates appear ONLY in the post-hoc localization metric,
      never in the grid, the constraints, or the solver (K1).
  (b) The c_6 floor (P2a, the open core = composite pinching). Comb free
      (c_n >= 0), maximize c_6 subject to truncated (EF)-feasibility. KILL
      CRITERION: a persistent c_6 floor that does not shrink under refinement
      kills LCC rigidity; shrinkage toward 0 means pinching is LP-visible.
  (c) D-H infeasibility certificate (the discipline control). Same machinery,
      D-H source (no pole, Omega_DH). Expected INFEASIBLE with a Farkas dual
      certificate (the Fejer-triangle dual of the #76 emptiness lemma). If D-H
      is FEASIBLE at any truncation the firewall breaks: reported loudly.
  (e) Calibration probes (P2b/P4 of #82): (e1) max and min c_2, equivalently
      kappa_2 = sqrt(2) c_2 against log 2 = 0.693147; (e2) max c_1 (P4 predicts
      it is squeezed to 0). Tracked on the same refinement ladder as (b).

Run (d) (flat-comb ghost) is CANCELLED: settled analytically by e3hh (the flat
comb c_n = c1 n^{-1/2} is infeasible for every c1 > 0).

Test family (all even, compactly supported, closed-form ghat and pole):
  * plain Fejer triangles g(x) = (1 - |x|/X)+, ghat(r) = X sinc^2(rX/2) >= 0,
    pole = (16/X)(cosh(X/2) - 1);
  * cosine-modulated triangles g(x) = (1 - |x|/X)+ cos(omega x),
    ghat(r) = (X/2)[sinc^2((r-omega)X/2) + sinc^2((r+omega)X/2)] >= 0,
    pole = 4 Re[(cosh(aX) - 1)/(a^2 X)], a = 1/2 + i omega;
  * translated triangle pairs g(x) = tri_a(x-T) + tri_a(x+T),
    ghat(r) = 2 cos(rT) a sinc^2(ra/2) (signed),
    pole = (32/a) cosh(T/2)(cosh(a/2) - 1).

DISCRETIZATION SEMANTICS (state of honesty, applies to every printout below):
  * Putting mu on a finite grid RESTRICTS the cone, and keeping finitely many
    tests RELAXES it. Primal results (feasibility, max/min values) are therefore
    INDICATIVE ONLY; the deliverables of runs (b)/(e) are refinement TRENDS, not
    single values, and a primal infeasibility could in principle be a grid
    artifact. Guard: run (a) (the true crystal) must be feasible on the same
    grid before anything else is trusted.
  * DUAL/Farkas certificates (a combination y >= 0 of tests with
    sum y_j ghat_j >= 0 on all of R, sum y_j g_j >= 0 on [0, infty), and source
    side sum y_j rhs_j < 0) are RIGOROUS infeasibility evidence in the continuum
    once the sign conditions are verified analytically. Run (c)'s deliverable is
    such a certificate; for a single plain Fejer triangle the sign conditions
    hold in closed form, so only the negativity of the source side (a 1-D
    integral with an explicit tail bound) needs checking.
  * Equality constraints carry slack variables s_j with hard bounds
    |s_j| <= eps_j (no penalty objective), because the truncations make exact
    equality unattainable: eps_j = (arch-integral truncation tail) + (allowance
    for spectral mass beyond the grid end) + (grid quantization allowance) +
    1e-3 * scale. The spectral-mass allowance uses the Riemann-von Mangoldt
    density (source-side analytic data, NOT zero locations); it enters ONLY the
    tolerance, never a constraint coefficient or objective.

HONESTY BLOCK (K1 / freeze / scope):
  * K1: no zero data in any constraint, grid, objective, or solver input. The
    ten hardcoded ordinates below (project landmarks, CLAUDE.md) are used only
    in run (a)'s post-hoc localization metric.
  * Soft-detector freeze: this is a FALSIFICATION instrument. Feasibility
    margins, localization quality, and shrinking ceilings are diagnostics of
    the instrument and of the conjecture's testable shadow; they are NEVER
    evidence for RH. A clean negative kills a mechanism; a clean positive
    supports a conjecture without proving anything.
  * What this can show: a persistent c_6 floor (kills LCC rigidity), a D-H
    feasibility (kills the firewall), LP-visibility (or not) of pinching and of
    the calibrations kappa_2 = log 2, c_1 = 0. What it cannot show: attainment
    (RH-equivalent, fenced off), or any positivity certificate.

Run: python -m experiments.positivity.e3x_lonely_crystal_lp
Outputs: e3x_lonely_crystal_lp.npz, e3x_lonely_crystal_lp.png, stdout tables.
"""

from __future__ import annotations

import time
from pathlib import Path

import numpy as np
import cvxpy as cp
from scipy.integrate import simpson
from scipy.optimize import nnls
from scipy.special import digamma as sp_digamma

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

LOG_PI = np.log(np.pi)
TWO_PI = 2.0 * np.pi
R_ARCH = 1200.0      # archimedean integral truncation
DR_ARCH = 0.0025     # archimedean quadrature step

# First ten zeta zero ordinates (project landmarks, CLAUDE.md). POST-HOC ONLY:
# they appear exclusively in run (a)'s localization metric, never in any solve.
GAMMAS = np.array([
    14.134725141734693, 21.022039638771555, 25.010857580145688,
    30.424876125859513, 32.935061587739190, 37.586178158825671,
    40.918719012147495, 43.327073280914999, 48.005150881167159,
    49.773832477672302])

LOG2 = np.log(2.0)

# Refinement ladder: tests, comb support L (N = e^L), spectral window R, grid h,
# omega spacing dom, coarse extension to ext_R (absorbs spectral tail mass).
RUNGS = [
    dict(L=np.log(50.0),   N=50,   R=40.0,  h=0.05,  dom=1.5, ext_R=120.0),
    dict(L=np.log(300.0),  N=300,  R=60.0,  h=0.04,  dom=1.0, ext_R=180.0),
    dict(L=np.log(1000.0), N=1000, R=80.0,  h=0.03,  dom=0.8, ext_R=240.0),
    dict(L=np.log(5000.0), N=5000, R=100.0, h=0.025, dom=0.6, ext_R=300.0),
    # rung 5: fixed comb support, wider spectral window and denser test set
    # (isolates whether the c_6 collapse continues under test refinement alone)
    dict(L=np.log(5000.0), N=5000, R=110.0, h=0.025, dom=0.55, ext_R=330.0),
]


# ----------------------------------------------------------------------------
# Sources
# ----------------------------------------------------------------------------

def omega_zeta(r):
    return np.real(sp_digamma(0.25 + 0.5j * np.asarray(r, dtype=float))) - LOG_PI


def omega_dh(r):
    return (np.log(5.0)
            + np.real(sp_digamma(0.75 + 0.5j * np.asarray(r, dtype=float)))
            - LOG_PI)


def vm_comb(N):
    """c_n = Lambda(n)/sqrt(n), n = 1..N (c_1 = 0). Sieve, no L-function calls."""
    lam = np.zeros(N + 1)
    spf = np.zeros(N + 1, dtype=np.int64)
    for i in range(2, N + 1):
        if spf[i] == 0:
            spf[i::i] = np.where(spf[i::i] == 0, i, spf[i::i])
    for n in range(2, N + 1):
        p, q = spf[n], n
        while q % p == 0:
            q //= p
        lam[n] = np.log(p) if q == 1 else 0.0
    n_arr = np.arange(0, N + 1, dtype=float)
    n_arr[0] = 1.0
    return (lam / np.sqrt(n_arr))[1:]          # index i -> n = i+1


# ----------------------------------------------------------------------------
# Test family: tuples (kind, p1, p2). ("mod", X, omega) covers plain Fejer at
# omega = 0; ("trans", a, T) is the translated pair.
# ----------------------------------------------------------------------------

def sinc2(u):
    return np.sinc(np.asarray(u) / np.pi) ** 2


def test_ghat(t, r):
    kind, p1, p2 = t
    r = np.asarray(r, dtype=float)
    if kind == "mod":
        X, om = p1, p2
        return 0.5 * X * (sinc2((r - om) * X / 2.0) + sinc2((r + om) * X / 2.0))
    a, T = p1, p2
    return 2.0 * np.cos(r * T) * a * sinc2(r * a / 2.0)


def test_g(t, x):
    kind, p1, p2 = t
    x = np.asarray(x, dtype=float)
    if kind == "mod":
        X, om = p1, p2
        return np.clip(1.0 - np.abs(x) / X, 0.0, None) * np.cos(om * x)
    a, T = p1, p2
    return (np.clip(1.0 - np.abs(x - T) / a, 0.0, None)
            + np.clip(1.0 - np.abs(x + T) / a, 0.0, None))


def test_pole(t):
    """ghat(i/2) + ghat(-i/2) = 2 int g(x) cosh(x/2) dx, closed form."""
    kind, p1, p2 = t
    if kind == "mod":
        X, om = p1, p2
        a = 0.5 + 1j * om
        return float(4.0 * np.real((np.cosh(a * X) - 1.0) / (a * a * X)))
    a, T = p1, p2
    return float((32.0 / a) * np.cosh(T / 2.0) * (np.cosh(a / 2.0) - 1.0))


def test_env(t, r):
    """Pointwise envelope of |ghat| valid for r > omega (used only for tails)."""
    kind, p1, p2 = t
    r = np.asarray(r, dtype=float)
    if kind == "mod":
        X, om = p1, p2
        return (2.0 / X) * (1.0 / (r - om) ** 2 + 1.0 / (r + om) ** 2)
    a, _ = p1, p2
    return 8.0 / (a * r ** 2)


def tail_integral(t, r_from, logc):
    """(1/pi) int_{r_from}^inf env(r) (log(logc * r) + 1) dr, numeric on a
    log-spaced grid (envelope ~ r^-2 log r; remainder beyond 1e7 negligible)."""
    rr = np.geomspace(r_from, 1.0e7, 4001)
    return float(np.trapezoid(test_env(t, rr) * (np.log(logc * rr) + 1.0), rr) / np.pi)


# ----------------------------------------------------------------------------
# Self-tests of the closed forms (cheap, run once)
# ----------------------------------------------------------------------------

def selftest():
    for t in (("mod", 5.0, 7.0), ("mod", 8.0, 0.0), ("trans", 1.0, 3.0)):
        sup = t[1] if t[0] == "mod" else t[2] + t[1]
        x = np.linspace(-sup, sup, 200001)
        g = test_g(t, x)
        pole_q = 2.0 * simpson(g * np.cosh(x / 2.0), x=x)
        assert abs(pole_q - test_pole(t)) <= 1e-6 * max(1.0, abs(pole_q)), t
        for r0 in (0.7, 3.3):
            gh_q = simpson(g * np.cos(r0 * x), x=x)
            assert abs(gh_q - float(test_ghat(t, r0))) <= 1e-6, (t, r0)
    assert abs(omega_zeta(0.0) + 5.3721834) < 1e-5
    assert abs(omega_dh(0.0) + 0.6211530) < 1e-5
    print("[selftest] closed forms (ghat, pole) and Omega conventions: OK\n")


# ----------------------------------------------------------------------------
# Rung assembly
# ----------------------------------------------------------------------------

def build_rung(cfg):
    L, N, R, h, dom, ext_R = (cfg["L"], cfg["N"], cfg["R"], cfg["h"],
                              cfg["dom"], cfg["ext_R"])
    om_max = R - 10.0
    tests = []
    for X in sorted({2.0, round(0.5 * L, 4), round(0.75 * L, 4), round(L, 4)}):
        tests.append(("mod", float(X), 0.0))
    for om in np.arange(dom, om_max + 1e-9, dom):
        tests.append(("mod", float(L), float(om)))
    for T in np.arange(1.0, L - 1.0 + 1e-9, 0.5):
        tests.append(("trans", 1.0, float(T)))
    J = len(tests)

    r_fine = np.arange(0.0, R + h / 2, h)
    r_ext = np.arange(R + 0.5, ext_R + 1e-9, 0.5)
    r_grid = np.concatenate([r_fine, r_ext])
    M_fine = len(r_fine)

    Smat = np.vstack([test_ghat(t, r_grid) for t in tests])
    x_n = np.log(np.arange(1, N + 1, dtype=float))
    Cmat = 2.0 * np.vstack([test_g(t, x_n) for t in tests])

    r_arch = np.arange(0.0, R_ARCH + DR_ARCH / 2, DR_ARCH)
    omz, omd = omega_zeta(r_arch), omega_dh(r_arch)
    arch_z = np.empty(J)
    arch_d = np.empty(J)
    for j, t in enumerate(tests):
        gh = test_ghat(t, r_arch)
        arch_z[j] = simpson(gh * omz, x=r_arch) / np.pi
        arch_d[j] = simpson(gh * omd, x=r_arch) / np.pi
    pole = np.array([test_pole(t) for t in tests])
    rhs_z = pole + arch_z
    rhs_d = arch_d.copy()                      # D-H: no pole term

    # tolerances: arch tail (A) + spectral mass beyond grid end (B, RvM density,
    # tolerance-only) + grid quantization (Q) + 1e-3 * scale
    eps_z = np.empty(J)
    eps_d = np.empty(J)
    for j, t in enumerate(tests):
        A_z = tail_integral(t, R_ARCH, 1.0 / TWO_PI)
        A_d = tail_integral(t, R_ARCH, 5.0 / TWO_PI)
        B_z = tail_integral(t, ext_R, 1.0 / TWO_PI)
        B_d = tail_integral(t, ext_R, np.sqrt(5.0) / TWO_PI)
        d2 = float(np.max(np.abs(np.diff(Smat[j, :M_fine], n=2)))) if M_fine > 2 else 0.0
        Q = 2.0 * d2
        eps_z[j] = A_z + B_z + Q + 1e-3 * max(1.0, abs(rhs_z[j]))
        eps_d[j] = A_d + B_d + Q + 1e-3 * max(1.0, abs(rhs_d[j]))

    return dict(cfg=cfg, tests=tests, J=J, r_grid=r_grid, M_fine=M_fine,
                om_max=om_max, Smat=Smat, Cmat=Cmat, x_n=x_n,
                rhs_z=rhs_z, rhs_d=rhs_d, eps_z=eps_z, eps_d=eps_d,
                arch_z=arch_z, arch_d=arch_d, pole=pole)


# ----------------------------------------------------------------------------
# Run (a): blind crystal recovery (positive control)
# ----------------------------------------------------------------------------

def run_a(rg):
    cfg = rg["cfg"]
    c_lam = vm_comb(cfg["N"])
    rhs_a = rg["rhs_z"] - rg["Cmat"] @ c_lam
    Aw = rg["Smat"] / rg["eps_z"][:, None]
    bw = rhs_a / rg["eps_z"]
    w, _ = nnls(Aw, bw)
    res = rg["Smat"] @ w - rhs_a
    ratio = float(np.max(np.abs(res) / rg["eps_z"]))

    # post-hoc localization (the ONLY place zero ordinates are used)
    r = rg["r_grid"][:rg["M_fine"]]
    wf = w[:rg["M_fine"]]
    gam_use = GAMMAS[GAMMAS <= rg["om_max"] - 2.0]
    r_cap = gam_use[-1] + 2.0 if len(gam_use) else 0.0
    tot = float(wf[r <= r_cap].sum())
    hit = 0.0
    win_mass, win_cent = [], []
    for gm in gam_use:
        m = np.abs(r - gm) <= 0.5
        wm = float(wf[m].sum())
        hit += wm
        win_mass.append(wm)
        win_cent.append(float((wf[m] * r[m]).sum() / wm) if wm > 1e-12 else np.nan)
    low = float(wf[r <= 13.0].sum())
    hit_frac = hit / tot if tot > 0 else 0.0
    low_frac = low / tot if tot > 0 else 0.0
    return dict(w=w, ratio=ratio, hit_frac=hit_frac, low_frac=low_frac,
                gam_use=gam_use, win_mass=np.array(win_mass),
                win_cent=np.array(win_cent), tot=tot)


# ----------------------------------------------------------------------------
# Runs (b)/(e): LP ceilings over the truncated cone
# ----------------------------------------------------------------------------

def _solve(prob):
    """CLARABEL first; bounded SCS fallback, loudly reported (a silent
    unbounded-iteration fallback can stall a rung for tens of minutes)."""
    try:
        prob.solve(solver=cp.CLARABEL, max_iter=200)
        if prob.status in ("optimal", "optimal_inaccurate"):
            return prob.status
        print(f"      [solver note: CLARABEL status {prob.status}, "
              f"falling back to SCS]", flush=True)
    except Exception as exc:
        print(f"      [solver note: CLARABEL raised {type(exc).__name__}, "
              f"falling back to SCS]", flush=True)
    prob.solve(solver=cp.SCS, max_iters=25000)
    return prob.status + "(SCS)"


def run_be(rg):
    Mg, N, J = rg["Smat"].shape[1], rg["cfg"]["N"], rg["J"]
    w = cp.Variable(Mg, nonneg=True)
    c = cp.Variable(N, nonneg=True)
    s = cp.Variable(J)
    cons = [rg["Smat"] @ w + rg["Cmat"] @ c + s == rg["rhs_z"],
            cp.abs(s) <= rg["eps_z"]]
    out = {}
    for key, expr, sense in (("c6_max", c[5], "max"), ("c1_max", c[0], "max"),
                             ("c2_max", c[1], "max"), ("c2_min", c[1], "min")):
        t0 = time.time()
        obj = cp.Maximize(expr) if sense == "max" else cp.Minimize(expr)
        prob = cp.Problem(obj, cons)
        status = _solve(prob)
        val = float(prob.value) if prob.value is not None else np.nan
        out[key] = (val, status)
        print(f"      [{key}: {status} in {time.time()-t0:.0f}s]", flush=True)
    return out


# ----------------------------------------------------------------------------
# Run (c): D-H infeasibility + Farkas certificate
# ----------------------------------------------------------------------------

def run_c(rg):
    Mg, N, J = rg["Smat"].shape[1], rg["cfg"]["N"], rg["J"]
    w = cp.Variable(Mg, nonneg=True)
    c = cp.Variable(N, nonneg=True)
    s = cp.Variable(J)
    t = cp.Variable(nonneg=True)
    t0 = time.time()
    eq = rg["Smat"] @ w + rg["Cmat"] @ c + s == rg["rhs_d"]
    prob = cp.Problem(cp.Minimize(t), [eq, cp.abs(s) <= rg["eps_d"] + t])
    status = _solve(prob)
    print(f"      [dh_phase1: {status} in {time.time()-t0:.0f}s]", flush=True)
    t_star = float(t.value) if t.value is not None else np.nan

    # numerical Farkas combination from the equality duals
    y = eq.dual_value
    farkas = None
    if y is not None and np.max(np.abs(y)) > 0:
        y = np.asarray(y, dtype=float)
        if float(y @ rg["rhs_d"]) > 0:
            y = -y
        y = y / np.max(np.abs(y))
        r_chk = np.arange(0.0, 600.0, 0.01)
        u = np.zeros_like(r_chk)
        for j, tt in enumerate(rg["tests"]):
            if abs(y[j]) > 1e-12:
                u += y[j] * test_ghat(tt, r_chk)
        v = y @ rg["Cmat"]
        farkas = dict(y=y, src=float(y @ rg["rhs_d"]), u_min=float(u.min()),
                      v_min=float(v.min()), n_active=int(np.sum(np.abs(y) > 1e-6)))

    # analytic single-triangle certificate: plain Fejer X = L (ghat >= 0 on R,
    # g >= 0 on R, pole = 0 for D-H), source side = arch only
    L = rg["cfg"]["L"]
    j_star = next(i for i, tt in enumerate(rg["tests"])
                  if tt[0] == "mod" and tt[2] == 0.0 and abs(tt[1] - round(L, 4)) < 1e-9)
    cert_val = float(rg["arch_d"][j_star])
    cert_tail = tail_integral(rg["tests"][j_star], R_ARCH, 5.0 / TWO_PI)
    return dict(status=status, t_star=t_star, farkas=farkas,
                j_star=j_star, cert_val=cert_val, cert_tail=cert_tail)


# ----------------------------------------------------------------------------
# Driver
# ----------------------------------------------------------------------------

def main(rung_ids=None):
    out_dir = Path(__file__).resolve().parent
    print("=" * 78)
    print("e3x: Lonely Crystal LP falsification instrument (runs a, b, c, e)")
    print("=" * 78 + "\n")
    selftest()

    todo = [(k, cfg) for k, cfg in enumerate(RUNGS, start=1)
            if rung_ids is None or k in rung_ids]
    results = []
    for k, cfg in todo:
        t0 = time.time()
        rg = build_rung(cfg)
        print(f"--- rung {k}: L={cfg['L']:.3f} (N={cfg['N']}), R={cfg['R']:.0f}, "
              f"h={cfg['h']}, tests={rg['J']}, grid={len(rg['r_grid'])} "
              f"[build {time.time()-t0:.1f}s]")

        ra = run_a(rg)
        feas = ra["ratio"] <= 1.0
        print(f"  (a) control: max|res|/eps = {ra['ratio']:.3f} "
              f"-> {'FEASIBLE within tolerance' if feas else 'NOT feasible (widen grid before trusting b/c/e)'}")
        print(f"      localization: hit_frac(+-0.5 of {len(ra['gam_use'])} known "
              f"ordinates) = {ra['hit_frac']:.3f}, mass below r=13: {ra['low_frac']:.3f}")
        if len(ra["gam_use"]):
            cent_err = np.nanmax(np.abs(ra["win_cent"] - ra["gam_use"]))
            print(f"      window masses (folded, expect ~2): "
                  f"{np.round(ra['win_mass'], 2).tolist()}; "
                  f"max centroid offset = {cent_err:.3f}")

        rb = run_be(rg)
        c6, st6 = rb["c6_max"]
        c1, st1 = rb["c1_max"]
        c2hi, st2h = rb["c2_max"]
        c2lo, st2l = rb["c2_min"]
        print(f"  (b) max c_6 = {c6:.4f}  [{st6}]   (truth Lambda(6)/sqrt6 = 0)")
        print(f"  (e) max c_1 = {c1:.4f}  [{st1}]   (P4 truth 0)")
        print(f"      c_2 in [{c2lo:.4f}, {c2hi:.4f}]  [{st2l}/{st2h}]  "
              f"-> kappa_2 in [{c2lo*np.sqrt(2):.4f}, {c2hi*np.sqrt(2):.4f}] "
              f"vs log 2 = {LOG2:.6f}")

        rc = run_c(rg)
        infeas = rc["t_star"] > 1e-6
        print(f"  (c) D-H phase-1: t* = {rc['t_star']:.4f} "
              f"-> {'INFEASIBLE (firewall holds)' if infeas else 'FEASIBLE: FIREWALL BREAK, REPORT LOUDLY'}")
        if rc["farkas"] is not None:
            f = rc["farkas"]
            print(f"      LP Farkas combo: {f['n_active']} active tests, "
                  f"source side = {f['src']:.4f} (<0), min_r u = {f['u_min']:.2e}, "
                  f"min_n v = {f['v_min']:.2e}")
        print(f"      analytic certificate (plain Fejer X=L): arch_DH = "
              f"{rc['cert_val']:.4f} +/- {rc['cert_tail']:.4f} (tail) < 0; "
              f"ghat >= 0 on R, g >= 0, pole = 0 -> continuum-rigorous")
        print(f"  [rung total {time.time()-t0:.1f}s]\n")

        results.append(dict(rung=k, cfg=cfg, rg=rg, a=ra, be=rb, c=rc))

    # --------------------------------------------- persist (cumulative merge)
    out_npz = out_dir / "e3x_lonely_crystal_lp.npz"
    save = {}
    if out_npz.exists():
        with np.load(out_npz) as old:
            save.update({key: old[key] for key in old.files})
    for r in results:
        k = r["rung"]
        save[f"r{k}_c6max"] = r["be"]["c6_max"][0]
        save[f"r{k}_c1max"] = r["be"]["c1_max"][0]
        save[f"r{k}_c2min"] = r["be"]["c2_min"][0]
        save[f"r{k}_c2max"] = r["be"]["c2_max"][0]
        save[f"r{k}_a_ratio"] = r["a"]["ratio"]
        save[f"r{k}_a_hitfrac"] = r["a"]["hit_frac"]
        save[f"r{k}_a_lowfrac"] = r["a"]["low_frac"]
        save[f"r{k}_a_winmass"] = r["a"]["win_mass"]
        save[f"r{k}_dh_tstar"] = r["c"]["t_star"]
        save[f"r{k}_dh_certval"] = r["c"]["cert_val"]
        save[f"r{k}_dh_certtail"] = r["c"]["cert_tail"]
        save[f"r{k}_ntests"] = r["rg"]["J"]
    top = results[-1]
    if "top_rung" not in save or int(save["top_rung"]) <= top["rung"]:
        save["top_rung"] = top["rung"]
        save["top_r_grid"] = top["rg"]["r_grid"]
        save["top_w"] = top["a"]["w"]
    save["gammas_posthoc"] = GAMMAS
    np.savez_compressed(out_npz, **save)

    # ------------------------------------------- summary over ALL stored rungs
    ks = [k for k in range(1, len(RUNGS) + 1) if f"r{k}_c6max" in save]
    c6s = np.array([float(save[f"r{k}_c6max"]) for k in ks])
    c1s = np.array([float(save[f"r{k}_c1max"]) for k in ks])
    c2lo_a = np.array([float(save[f"r{k}_c2min"]) for k in ks])
    c2hi_a = np.array([float(save[f"r{k}_c2max"]) for k in ks])
    print("=" * 78)
    print("REFINEMENT TABLE (trends are the deliverable, not single values)")
    print("=" * 78)
    print(f"{'rung':>4} {'tests':>6} {'L':>6} {'R':>5} {'h':>6} "
          f"{'(a)res':>7} {'(a)hit':>7} {'maxc6':>8} {'maxc1':>8} "
          f"{'c2_lo':>8} {'c2_hi':>8} {'DH t*':>8}")
    for i, k in enumerate(ks):
        cfg = RUNGS[k - 1]
        print(f"{k:>4} {int(save[f'r{k}_ntests']):>6} {cfg['L']:>6.2f} "
              f"{cfg['R']:>5.0f} {cfg['h']:>6.3f} "
              f"{float(save[f'r{k}_a_ratio']):>7.2f} "
              f"{float(save[f'r{k}_a_hitfrac']):>7.3f} "
              f"{c6s[i]:>8.4f} {c1s[i]:>8.4f} "
              f"{c2lo_a[i]:>8.4f} {c2hi_a[i]:>8.4f} "
              f"{float(save[f'r{k}_dh_tstar']):>8.4f}")

    print("\nVERDICTS (instrument diagnostics, not RH evidence):")
    ok_a = (float(save[f"r{ks[-1]}_a_ratio"]) <= 1.0
            and float(save[f"r{ks[-1]}_a_hitfrac"]) >= 0.8)
    print(f"  (a) positive control: {'PASS' if ok_a else 'FAIL'} "
          f"(feasible + localized at top rung)")
    shrink6 = len(c6s) > 1 and c6s[-1] < 0.5 * float(np.max(c6s[:-1]))
    print(f"  (b) c_6 ceiling trend {np.round(c6s, 4).tolist()}: "
          f"{'COLLAPSING under refinement (pinching LP-visible so far)' if shrink6 else 'NOT clearly shrinking (floor candidate; kill criterion armed)'}")
    dh_ok = all(float(save[f"r{k}_dh_tstar"]) > 1e-6 for k in ks)
    print(f"  (c) D-H: {'INFEASIBLE at every rung + analytic certificate (firewall holds)' if dh_ok else 'FIREWALL BREAK'}")
    shrink1 = len(c1s) > 1 and c1s[-1] < 0.5 * float(np.max(c1s[:-1]))
    print(f"  (e) c_1 ceiling trend {np.round(c1s, 4).tolist()}: "
          f"{'SHRINKING (P4 LP-visible so far)' if shrink1 else 'NOT clearly shrinking'}")
    c2lo, c2hi = c2lo_a[-1], c2hi_a[-1]
    print(f"      kappa_2 interval at top rung: [{c2lo*np.sqrt(2):.4f}, "
          f"{c2hi*np.sqrt(2):.4f}] vs log 2 = {LOG2:.6f} "
          f"(truth {'inside' if c2lo*np.sqrt(2) <= LOG2 <= c2hi*np.sqrt(2) else 'OUTSIDE (instrument pathology!)'})")

    # ------------------------------------------------------------------- plot
    fig, axs = plt.subplots(1, 2, figsize=(13, 5))
    ax = axs[0]
    rgr = np.asarray(save["top_r_grid"], dtype=float)
    wf = np.asarray(save["top_w"], dtype=float)
    m60 = rgr <= 60.0
    ax.plot(rgr[m60], wf[m60], "b-", lw=0.8)
    for gm in GAMMAS:
        ax.axvline(gm, color="r", ls=":", lw=0.7)
    ax.set_xlim(0, 60)
    ax.set_xlabel("r")
    ax.set_ylabel("recovered weight w_r")
    ax.set_title("(a) blind recovery, top rung\n(red: known ordinates, post-hoc only)")
    ax = axs[1]
    ax.plot(ks, c6s, "o-", label="max c_6 (truth 0)")
    ax.plot(ks, c1s, "s-", label="max c_1 (truth 0)")
    ax.plot(ks, c2hi_a, "^--", label="max c_2")
    ax.plot(ks, c2lo_a, "v--", label="min c_2")
    ax.axhline(LOG2 / np.sqrt(2.0), color="gray", lw=0.8,
               label="c_2 truth log2/sqrt2")
    ax.set_xlabel("rung")
    ax.set_ylabel("LP value")
    ax.set_title("(b)/(e) ceilings under refinement")
    ax.set_xticks(ks)
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(out_dir / "e3x_lonely_crystal_lp.png", dpi=140)
    plt.close()
    print(f"\nSaved {out_dir / 'e3x_lonely_crystal_lp.npz'}")
    print(f"Saved {out_dir / 'e3x_lonely_crystal_lp.png'}")


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--rungs", type=str, default="",
                    help="comma-separated rung ids to (re)run, e.g. 4,5; "
                         "results merge into the cumulative npz")
    args = ap.parse_args()
    ids = [int(x) for x in args.rungs.split(",") if x.strip()] or None
    main(ids)
