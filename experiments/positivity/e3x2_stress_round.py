"""e3x2: ADVERSARY stress round on the e3x Lonely Crystal LP instrument.

Executes the four handoff attacks from e3x_lonely_crystal_lp.md section 6:

  A1  rung-6 stress: L = log 20000 (N = 20000), om_max = 120, 260 tests,
      R = 130. Grid h = 0.02 is chosen so the grid-quantization tolerance
      Q ~ (X^3/6) h^2 at the X = L tests MATCHES rung 5 (Q/2 = 0.032);
      running rung 6 at h = 0.025 would loosen the slack budget by 57% and
      confound the trend read. One extra build at h = 0.025 (c_1, c_6 only)
      measures d(ceiling)/dQ at fixed L: the artifact discriminator.
  A2  family independence: Hann (raised-cosine) windows with the same
      X / omega / T recipe at rung-5 resolution; shifted (h/2) and jittered
      (+-0.4h, fixed seed) mu grids under the Fejer family. D-H phase-1 is
      rerun once under the Hann family (firewall family-independence).
  A3  ghost hunt: fix c_6 >= 0.2 at rung 5 and minimize the slack-budget
      scale tau (|s_j| <= tau eps_j); then give the resulting ghost every
      chance at rung 6 (additions of mu and comb mass allowed, removals
      not) and phase-1 its violation; also evaluate the ghost against the
      Hann tests and the dense low-omega probes. Kill criterion: a
      refinement-robust c_6 >= 0.2.
  A4  c_1 plateau autopsy: equality duals + slack saturation at the rung-5
      max-c_1 optimum; eps decomposition (arch tail A + beyond-grid B +
      grid quantization Q + 1e-3 base); pure-h sweep h = 0.015 / 0.0125 at
      fixed tests; dense low-omega probes (om step 0.15 on (0, 13], X = L)
      testing the #82 prediction that no compact-support probe family moves
      the plateau.

ARTIFACT HYPOTHESIS UNDER TEST (stated before running, falsifiable):
  max c_1 ~ Q/2 + O(few 1e-3). Q = 2 max|second difference of ghat on the
  fine mu grid|, ~ (X^3/6) h^2 for the X = L modulated tests. Across e3x
  rungs 3-5, Q/2 = 0.025 / 0.032 / 0.032 while the reported c_1 "plateau"
  was 0.031 / 0.032 / 0.030: h froze near 0.025 while L grew, so the one
  eps term that never shrank tracks the plateau exactly. Discriminating
  predictions: c_1 ~ 0.012 at h = 0.015, ~ 0.008 at h = 0.0125 (rung-5
  tests), ~ 0.032 at rung-6 h = 0.02, ~ 0.051 at rung-6 h = 0.025. The
  #82 reading predicts a stable ~ 0.03 everywhere instead.

Solver: scipy linprog/HiGHS for all stress LPs (the cvxpy/CLARABEL path of
e3x canonicalizes ~260 x 27k dense systems too slowly for this round). The
HiGHS pipeline is cross-validated against e3x's published CLARABEL rung-5
values (max c_6 0.2133, max c_1 0.0299, c_2 in [0.4166, 0.5488], D-H t*
0.3697) before any new number is trusted.

Guard policy: every new grid/tolerance configuration re-runs the run (a)
truth-feasibility check (the e3x guard). Variants use a bounded least
squares witness (TRF) for the feasibility ratio, escalating to full NNLS
only if the fast witness fails; localization metrics from TRF witnesses are
lower bounds (TRF spreads mass where NNLS concentrates it) and are labeled.

K1 hygiene: uniform / offset / jittered grids and uniform test lattices
only; the jitter seed is fixed, not tuned; no zero ordinate enters any
constraint, grid, objective, or test choice. Zero landmarks and the r <= 13
window appear only in post-hoc diagnostics labeled POST-HOC. Soft-detector
freeze: trends and certificates only; nothing here is evidence for RH.

Run: python -m experiments.positivity.e3x2_stress_round [--attacks V,A1,A2,A3,A4]
Outputs: e3x2_stress_round.npz + stdout. The md appendix is written separately.
"""

from __future__ import annotations

import argparse
import time
import traceback
from pathlib import Path

import numpy as np
from scipy.integrate import simpson
from scipy.optimize import linprog, lsq_linear, nnls
from scipy.sparse import coo_matrix

from experiments.positivity import e3x_lonely_crystal_lp as e3x
from experiments.positivity.e3x_lonely_crystal_lp import (
    R_ARCH, DR_ARCH, TWO_PI, LOG2, GAMMAS,
    omega_zeta, omega_dh, vm_comb, tail_integral,
    test_ghat, test_g, test_pole, test_env)

PI = np.pi
OUT_DIR = Path(__file__).resolve().parent
NPZ_PATH = OUT_DIR / "e3x2_stress_round.npz"
SOLVE_T = [0.0]   # accumulated LP/NNLS seconds (budget tracking)


# ----------------------------------------------------------------------------
# Hann test family ("hmod", X, om) and ("htrans", a, T)
# base window: hann(x; X) = (1 + cos(pi x / X)) / 2 on |x| <= X
# ghat_base(r) = X sinc(u) pi^2 / (pi^2 - u^2), u = rX  (entire in r)
# ----------------------------------------------------------------------------

def _hann_ghat_base(r, X):
    """Real-axis evaluation, numerically stable across the removable
    singularity at u = pi via the shifted form X pi^2 sinc(u - pi)/(u(u+pi))."""
    u = np.abs(np.asarray(r, dtype=float)) * X
    scalar = (u.ndim == 0)
    u = np.atleast_1d(u).astype(float)
    out = np.empty_like(u)
    lo = u <= PI / 2
    ul = u[lo]
    out[lo] = X * np.sinc(ul / PI) * PI ** 2 / (PI ** 2 - ul ** 2)
    uh = u[~lo]
    v = uh - PI
    out[~lo] = X * PI ** 2 * np.sinc(v / PI) / (uh * (uh + PI))
    return float(out[0]) if scalar else out


def _hann_ghat_cplx(z, X):
    """Entire extension at complex z (used only for poles, |Im zX| >= 1)."""
    zz = complex(z) * X
    return X * PI ** 2 * (np.sin(zz) / zz) / (PI ** 2 - zz * zz)


def htest_ghat(t, r):
    kind, p1, p2 = t
    r = np.asarray(r, dtype=float)
    if kind == "hmod":
        X, om = p1, p2
        return 0.5 * (_hann_ghat_base(r - om, X) + _hann_ghat_base(r + om, X))
    a, T = p1, p2
    return 2.0 * np.cos(r * T) * _hann_ghat_base(r, a)


def _hann_win(x, X):
    x = np.asarray(x, dtype=float)
    return np.where(np.abs(x) <= X,
                    0.5 * (1.0 + np.cos(PI * np.clip(x / X, -1.0, 1.0))), 0.0)


def htest_g(t, x):
    kind, p1, p2 = t
    x = np.asarray(x, dtype=float)
    if kind == "hmod":
        return _hann_win(x, p1) * np.cos(p2 * x)
    return _hann_win(x - p2, p1) + _hann_win(x + p2, p1)


def htest_pole(t):
    """ghat(i/2) + ghat(-i/2). hmod: 2 Re ghat_base(om + i/2). htrans:
    2 cosh(T/2) * pole_base (translation identity, even base)."""
    kind, p1, p2 = t
    if kind == "hmod":
        return float(2.0 * np.real(_hann_ghat_cplx(p2 + 0.5j, p1)))
    a, T = p1, p2
    return float(2.0 * np.cosh(T / 2.0) * 2.0 * np.real(_hann_ghat_cplx(0.5j, a)))


def htest_env(t, r):
    """|ghat| envelope valid for (r - om) X > 2 pi (tails only)."""
    kind, p1, p2 = t
    r = np.asarray(r, dtype=float)
    if kind == "hmod":
        X, om = p1, p2
        return 0.5 * PI ** 2 * (1.0 / ((r - om) * ((r - om) ** 2 * X ** 2 - PI ** 2))
                                + 1.0 / ((r + om) * ((r + om) ** 2 * X ** 2 - PI ** 2)))
    a, _ = p1, p2
    return 2.0 * PI ** 2 / (r * (r ** 2 * a ** 2 - PI ** 2))


# dispatch over both families -------------------------------------------------

def any_ghat(t, r):
    return htest_ghat(t, r) if t[0][0] == "h" else test_ghat(t, r)


def any_g(t, x):
    return htest_g(t, x) if t[0][0] == "h" else test_g(t, x)


def any_pole(t):
    return htest_pole(t) if t[0][0] == "h" else test_pole(t)


def any_tail(t, r_from, logc):
    if t[0][0] != "h":
        return tail_integral(t, r_from, logc)
    rr = np.geomspace(r_from, 1.0e7, 4001)
    return float(np.trapezoid(htest_env(t, rr) * (np.log(logc * rr) + 1.0), rr) / np.pi)


def hann_selftest():
    for t in (("hmod", 5.0, 7.0), ("hmod", 8.0, 0.0), ("htrans", 1.0, 3.0)):
        sup = t[1] if t[0] == "hmod" else t[2] + t[1]
        x = np.linspace(-sup, sup, 200001)
        g = htest_g(t, x)
        pole_q = 2.0 * simpson(g * np.cosh(x / 2.0), x=x)
        assert abs(pole_q - htest_pole(t)) <= 1e-6 * max(1.0, abs(pole_q)), t
        for r0 in (0.7, 3.3, 0.36889):   # last value sits near the u = pi seam
            gh_q = simpson(g * np.cos(r0 * x), x=x)
            assert abs(gh_q - float(htest_ghat(t, r0))) <= 1e-6, (t, r0)
    # seam continuity of the two stable forms at u = pi/2
    X = 8.5172
    a = _hann_ghat_base(PI / 2 / X - 1e-9, X)
    b = _hann_ghat_base(PI / 2 / X + 1e-9, X)
    assert abs(a - b) < 1e-6
    print("[selftest] Hann closed forms (ghat, pole, seam): OK\n")


# ----------------------------------------------------------------------------
# Generalized rung builder (mirrors e3x.build_rung; adds family, grid modes,
# dense low-omega probes; stores the eps decomposition). The Q allowance is
# always computed on the UNIFORM reference grid at the same h so that
# ceilings stay comparable across grid variants (on a jittered grid a raw
# second difference of ghat picks up first-derivative terms of order h and
# would silently loosen eps).
# ----------------------------------------------------------------------------

def build_custom(cfg, family="fejer", grid_mode="uniform", lowom_step=None,
                 seed=20260611):
    L, N, R, h, dom, ext_R = (cfg["L"], cfg["N"], cfg["R"], cfg["h"],
                              cfg["dom"], cfg["ext_R"])
    om_max = R - 10.0
    mk = ("mod", "trans") if family == "fejer" else ("hmod", "htrans")
    tests = []
    for X in sorted({2.0, round(0.5 * L, 4), round(0.75 * L, 4), round(L, 4)}):
        tests.append((mk[0], float(X), 0.0))
    oms = [float(om) for om in np.arange(dom, om_max + 1e-9, dom)]
    if lowom_step is not None:
        base_arr = np.asarray(oms)
        for o in np.arange(lowom_step, 13.0 + 1e-9, lowom_step):
            if np.min(np.abs(base_arr - o)) > 1e-9:
                oms.append(float(o))
        oms.sort()
    for om in oms:
        tests.append((mk[0], float(round(L, 4)), float(om)))
    for T in np.arange(1.0, L - 1.0 + 1e-9, 0.5):
        tests.append((mk[1], 1.0, float(T)))
    J = len(tests)

    r_fine_u = np.arange(0.0, R + h / 2, h)
    if grid_mode == "uniform":
        r_fine = r_fine_u
    elif grid_mode == "shifted":
        r_fine = r_fine_u + h / 2
    elif grid_mode == "jitter":
        rng = np.random.default_rng(seed)
        r_fine = np.sort(np.clip(
            r_fine_u + rng.uniform(-0.4 * h, 0.4 * h, r_fine_u.size), 0.0, None))
    else:
        raise ValueError(grid_mode)
    r_ext = np.arange(R + 0.5, ext_R + 1e-9, 0.5)
    r_grid = np.concatenate([r_fine, r_ext])
    M_fine = len(r_fine)

    Smat = np.vstack([any_ghat(t, r_grid) for t in tests])
    x_n = np.log(np.arange(1, N + 1, dtype=float))
    Cmat = 2.0 * np.vstack([any_g(t, x_n) for t in tests])
    Sq = (Smat[:, :M_fine] if grid_mode == "uniform"
          else np.vstack([any_ghat(t, r_fine_u) for t in tests]))

    r_arch = np.arange(0.0, R_ARCH + DR_ARCH / 2, DR_ARCH)
    omz, omd = omega_zeta(r_arch), omega_dh(r_arch)
    arch_z = np.empty(J)
    arch_d = np.empty(J)
    for j, t in enumerate(tests):
        gh = any_ghat(t, r_arch)
        arch_z[j] = simpson(gh * omz, x=r_arch) / np.pi
        arch_d[j] = simpson(gh * omd, x=r_arch) / np.pi
    pole = np.array([any_pole(t) for t in tests])
    rhs_z = pole + arch_z
    rhs_d = arch_d.copy()

    eps_z = np.empty(J)
    eps_d = np.empty(J)
    cA = np.empty(J)
    cB = np.empty(J)
    cQ = np.empty(J)
    cbase = np.empty(J)
    for j, t in enumerate(tests):
        A_z = any_tail(t, R_ARCH, 1.0 / TWO_PI)
        A_d = any_tail(t, R_ARCH, 5.0 / TWO_PI)
        B_z = any_tail(t, ext_R, 1.0 / TWO_PI)
        B_d = any_tail(t, ext_R, np.sqrt(5.0) / TWO_PI)
        d2 = float(np.max(np.abs(np.diff(Sq[j], n=2)))) if M_fine > 2 else 0.0
        Q = 2.0 * d2
        cA[j], cB[j], cQ[j] = A_z, B_z, Q
        cbase[j] = 1e-3 * max(1.0, abs(rhs_z[j]))
        eps_z[j] = A_z + B_z + Q + cbase[j]
        eps_d[j] = A_d + B_d + Q + 1e-3 * max(1.0, abs(rhs_d[j]))

    return dict(cfg=cfg, tests=tests, J=J, r_grid=r_grid, M_fine=M_fine,
                om_max=om_max, Smat=Smat, Cmat=Cmat, x_n=x_n,
                rhs_z=rhs_z, rhs_d=rhs_d, eps_z=eps_z, eps_d=eps_d,
                arch_z=arch_z, arch_d=arch_d, pole=pole,
                eps_A=cA, eps_B=cB, eps_Q=cQ, eps_base=cbase, family=family)


def eps_decompose_e3x(rg):
    """Post-hoc eps decomposition for a rung built by e3x.build_rung."""
    J = rg["J"]
    cA = np.empty(J)
    cB = np.empty(J)
    cQ = np.empty(J)
    cbase = np.empty(J)
    M_fine = rg["M_fine"]
    for j, t in enumerate(rg["tests"]):
        cA[j] = any_tail(t, R_ARCH, 1.0 / TWO_PI)
        cB[j] = any_tail(t, rg["cfg"]["ext_R"], 1.0 / TWO_PI)
        cQ[j] = 2.0 * float(np.max(np.abs(np.diff(rg["Smat"][j, :M_fine], n=2))))
        cbase[j] = 1e-3 * max(1.0, abs(rg["rhs_z"][j]))
    rg["eps_A"], rg["eps_B"], rg["eps_Q"], rg["eps_base"] = cA, cB, cQ, cbase
    return rg


# ----------------------------------------------------------------------------
# Run (a) guard with a fast TRF witness (escalates to NNLS if the witness
# fails feasibility, since TRF residuals upper-bound nothing a priori)
# ----------------------------------------------------------------------------

def run_a_guard(rg, force_nnls=False):
    """Truth-comb feasibility guard as a HiGHS phase-1 LP: minimize the max
    weighted residual t over w >= 0 with |Smat w - rhs_a| <= t eps. This is
    the exact guard semantics (NNLS minimizes the wrong norm and its active
    set thrashes on signed test families such as Hann). The LP vertex w is
    sparse (support <= 2J), so the POST-HOC localization stays meaningful."""
    cfg = rg["cfg"]
    c_lam = vm_comb(cfg["N"])
    rhs_a = rg["rhs_z"] - rg["Cmat"] @ c_lam
    S = rg["Smat"]
    J, M = S.shape
    eps = rg["eps_z"]
    A_ub = np.vstack([np.hstack([S, -eps[:, None]]),
                      np.hstack([-S, -eps[:, None]])])
    b_ub = np.concatenate([rhs_a, -rhs_a])
    cost = np.zeros(M + 1)
    cost[-1] = 1.0
    t0 = time.time()
    res = linprog(cost, A_ub=A_ub, b_ub=b_ub,
                  bounds=[(0.0, None)] * (M + 1), method="highs")
    solver = "lp"
    if res.status == 0:
        w = res.x[:M]
        ratio = float(res.fun)
    else:
        w, _ = nnls(S / eps[:, None], rhs_a / eps, maxiter=50 * J)
        ratio = float(np.max(np.abs(S @ w - rhs_a) / eps))
        solver = "nnls-fallback"
    dt = time.time() - t0
    SOLVE_T[0] += dt

    # POST-HOC localization diagnostic (zero ordinates used ONLY here)
    r = rg["r_grid"][:rg["M_fine"]]
    wf = w[:rg["M_fine"]]
    gam_use = GAMMAS[GAMMAS <= rg["om_max"] - 2.0]
    r_cap = gam_use[-1] + 2.0 if len(gam_use) else 0.0
    tot = float(wf[r <= r_cap].sum())
    hit = sum(float(wf[np.abs(r - gm) <= 0.5].sum()) for gm in gam_use)
    hit_frac = hit / tot if tot > 0 else 0.0
    low_frac = float(wf[r <= 13.0].sum()) / tot if tot > 0 else 0.0
    return dict(w=w, ratio=ratio, hit_frac=hit_frac, low_frac=low_frac,
                solver=solver, dt=dt)


# ----------------------------------------------------------------------------
# HiGHS LP layer
# ----------------------------------------------------------------------------

def lp_ceiling(rg, n_idx, sense="max", eps_scale=1.0, floor=None, duals=False,
               tag=""):
    """max/min c_{n_idx+1} over the truncated cone. Variables [w, c, s]."""
    S, C = rg["Smat"], rg["Cmat"]
    J, M = S.shape
    N = C.shape[1]
    nv = M + N + J
    A_eq = np.hstack([S, C, np.eye(J)])
    cost = np.zeros(nv)
    cost[M + n_idx] = -1.0 if sense == "max" else 1.0
    eps = eps_scale * rg["eps_z"]
    bounds = ([(0.0, None)] * (M + N)
              + [(-float(e), float(e)) for e in eps])
    if floor is not None:
        i, v = floor
        bounds[M + i] = (float(v), None)
    t0 = time.time()
    res = linprog(cost, A_eq=A_eq, b_eq=rg["rhs_z"], bounds=bounds,
                  method="highs")
    dt = time.time() - t0
    SOLVE_T[0] += dt
    ok = res.status == 0
    val = (-res.fun if sense == "max" else res.fun) if ok else np.nan
    print(f"      [{tag or ('c%d_%s' % (n_idx + 1, sense))}: "
          f"{'optimal' if ok else 'status=' + str(res.status)} "
          f"val={val:.4f} in {dt:.0f}s]", flush=True)
    out = dict(val=val, ok=ok, dt=dt)
    if ok and duals:
        out["y"] = np.asarray(res.eqlin.marginals, dtype=float)
        out["w"] = res.x[:M]
        out["c"] = res.x[M:M + N]
        out["s"] = res.x[M + N:]
    elif ok:
        out["w"] = res.x[:M]
        out["c"] = res.x[M:M + N]
        out["s"] = res.x[M + N:]
    return out


def lp_phase1_dh(rg, tag="dh_phase1"):
    """min t s.t. S w + C c + s = rhs_d, |s_j| <= eps_d_j + t. t* > 0 means
    the truncated D-H cone is infeasible at the stated tolerances."""
    S, C = rg["Smat"], rg["Cmat"]
    J, M = S.shape
    N = C.shape[1]
    nv = M + N + J + 1
    A_eq = np.hstack([S, C, np.eye(J), np.zeros((J, 1))])
    rows = np.concatenate([np.arange(J), np.arange(J), np.arange(J, 2 * J),
                           np.arange(J, 2 * J)])
    cols = np.concatenate([M + N + np.arange(J), np.full(J, nv - 1),
                           M + N + np.arange(J), np.full(J, nv - 1)])
    vals = np.concatenate([np.ones(J), -np.ones(J), -np.ones(J), -np.ones(J)])
    A_ub = coo_matrix((vals, (rows, cols)), shape=(2 * J, nv))
    b_ub = np.concatenate([rg["eps_d"], rg["eps_d"]])
    cost = np.zeros(nv)
    cost[-1] = 1.0
    bounds = ([(0.0, None)] * (M + N) + [(None, None)] * J + [(0.0, None)])
    t0 = time.time()
    res = linprog(cost, A_eq=A_eq, b_eq=rg["rhs_d"], A_ub=A_ub, b_ub=b_ub,
                  bounds=bounds, method="highs")
    dt = time.time() - t0
    SOLVE_T[0] += dt
    ok = res.status == 0
    t_star = res.fun if ok else np.nan
    print(f"      [{tag}: {'optimal' if ok else 'status=' + str(res.status)} "
          f"t*={t_star:.4f} in {dt:.0f}s]", flush=True)
    farkas = None
    if ok and res.eqlin is not None:
        y = np.asarray(res.eqlin.marginals, dtype=float)
        if np.max(np.abs(y)) > 0:
            if float(y @ rg["rhs_d"]) > 0:
                y = -y
            y = y / np.max(np.abs(y))
            r_chk = np.arange(0.0, 600.0, 0.01)
            u = np.zeros_like(r_chk)
            for j, tt in enumerate(rg["tests"]):
                if abs(y[j]) > 1e-12:
                    u += y[j] * any_ghat(tt, r_chk)
            v = y @ rg["Cmat"]
            farkas = dict(src=float(y @ rg["rhs_d"]), u_min=float(u.min()),
                          v_min=float(v.min()),
                          n_active=int(np.sum(np.abs(y) > 1e-6)))
    return dict(t_star=t_star, ok=ok, farkas=farkas)


def lp_ghost_robust(rg, idx=5, target=0.2):
    """min tau s.t. crystal constraints hold with |s_j| <= tau eps_j and
    c_{idx+1} >= target. tau* < 1 exhibits a ghost with slack margin 1/tau*."""
    S, C = rg["Smat"], rg["Cmat"]
    J, M = S.shape
    N = C.shape[1]
    nv = M + N + J + 1
    A_eq = np.hstack([S, C, np.eye(J), np.zeros((J, 1))])
    rows = np.concatenate([np.arange(J), np.arange(J), np.arange(J, 2 * J),
                           np.arange(J, 2 * J)])
    cols = np.concatenate([M + N + np.arange(J), np.full(J, nv - 1),
                           M + N + np.arange(J), np.full(J, nv - 1)])
    vals = np.concatenate([np.ones(J), -rg["eps_z"], -np.ones(J), -rg["eps_z"]])
    A_ub = coo_matrix((vals, (rows, cols)), shape=(2 * J, nv))
    b_ub = np.zeros(2 * J)
    cost = np.zeros(nv)
    cost[-1] = 1.0
    bounds = [(0.0, None)] * (M + N) + [(None, None)] * J + [(0.0, None)]
    bounds[M + idx] = (float(target), None)
    t0 = time.time()
    res = linprog(cost, A_eq=A_eq, b_eq=rg["rhs_z"], A_ub=A_ub, b_ub=b_ub,
                  bounds=bounds, method="highs")
    dt = time.time() - t0
    SOLVE_T[0] += dt
    ok = res.status == 0
    tau = res.fun if ok else np.nan
    print(f"      [ghost_robust c{idx + 1}>={target}: "
          f"{'optimal' if ok else 'status=' + str(res.status)} tau*={tau:.4f} "
          f"in {dt:.0f}s]", flush=True)
    if not ok:
        return dict(tau=np.nan, ok=False)
    return dict(tau=tau, ok=True, w=res.x[:M], c=res.x[M:M + N])


def lp_ghost_completion(rg6, rg5, w5, c5):
    """Best-case rung-6 phase-1 for a fixed rung-5 ghost: additions of mu
    mass (on the rung-6 grid) and comb mass (all n <= N6) are allowed,
    removals are not. t* > 0: no completion rescues the ghost."""
    base = (np.vstack([any_ghat(t, rg5["r_grid"]) for t in rg6["tests"]]) @ w5
            + 2.0 * np.vstack([any_g(t, rg5["x_n"]) for t in rg6["tests"]]) @ c5)
    naive = np.abs(base - rg6["rhs_z"]) / rg6["eps_z"]
    S, C = rg6["Smat"], rg6["Cmat"]
    J, M = S.shape
    N = C.shape[1]
    nv = M + N + J + 1
    A_eq = np.hstack([S, C, np.eye(J), np.zeros((J, 1))])
    rows = np.concatenate([np.arange(J), np.arange(J), np.arange(J, 2 * J),
                           np.arange(J, 2 * J)])
    cols = np.concatenate([M + N + np.arange(J), np.full(J, nv - 1),
                           M + N + np.arange(J), np.full(J, nv - 1)])
    vals = np.concatenate([np.ones(J), -np.ones(J), -np.ones(J), -np.ones(J)])
    A_ub = coo_matrix((vals, (rows, cols)), shape=(2 * J, nv))
    b_ub = np.concatenate([rg6["eps_z"], rg6["eps_z"]])
    cost = np.zeros(nv)
    cost[-1] = 1.0
    bounds = [(0.0, None)] * (M + N) + [(None, None)] * J + [(0.0, None)]
    t0 = time.time()
    res = linprog(cost, A_eq=A_eq, b_eq=rg6["rhs_z"] - base, A_ub=A_ub,
                  b_ub=b_ub, bounds=bounds, method="highs")
    dt = time.time() - t0
    SOLVE_T[0] += dt
    ok = res.status == 0
    t_star = res.fun if ok else np.nan
    print(f"      [ghost_completion: {'optimal' if ok else 'status=' + str(res.status)} "
          f"t*={t_star:.4f} in {dt:.0f}s]", flush=True)
    return dict(t_star=t_star, ok=ok, naive_max=float(naive.max()),
                naive_nviol=int(np.sum(naive > 1.0)))


def ghost_cross_eval(rg_alt, rg5, w5, c5, use_dh=False):
    """Evaluate a fixed ghost against an alternative test set built on the
    same comb support and grid coverage (no completion). Returns max ratio."""
    base = (np.vstack([any_ghat(t, rg5["r_grid"]) for t in rg_alt["tests"]]) @ w5
            + 2.0 * np.vstack([any_g(t, rg5["x_n"]) for t in rg_alt["tests"]]) @ c5)
    rhs = rg_alt["rhs_d"] if use_dh else rg_alt["rhs_z"]
    eps = rg_alt["eps_d"] if use_dh else rg_alt["eps_z"]
    ratio = np.abs(base - rhs) / eps
    return float(ratio.max()), int(np.sum(ratio > 1.0))


# ----------------------------------------------------------------------------
# Attack drivers
# ----------------------------------------------------------------------------

def classify(t):
    if t[0] in ("mod", "hmod"):
        if t[2] == 0.0:
            return "plain"
        return "om<=13" if t[2] <= 13.0 else "om>13"
    return "trans"


def npz_save(store):
    save = {}
    if NPZ_PATH.exists():
        with np.load(NPZ_PATH) as old:
            save.update({k: old[k] for k in old.files})
    save.update(store)
    np.savez_compressed(NPZ_PATH, **save)


def attack_v(store, cache):
    print("=== V: HiGHS pipeline validation against e3x CLARABEL rung 5 ===")
    rg5 = cache.setdefault("rg5", e3x.build_rung(e3x.RUNGS[4]))
    eps_decompose_e3x(rg5)
    vals = {}
    for key, idx, sense in (("c6", 5, "max"), ("c1", 0, "max"),
                            ("c2lo", 1, "min"), ("c2hi", 1, "max")):
        vals[key] = lp_ceiling(rg5, idx, sense, tag=f"V_{key}")["val"]
    ref = dict(c6=0.2133, c1=0.0299, c2lo=0.4166, c2hi=0.5488)
    ok = all(abs(vals[k] - ref[k]) <= 0.005 + 0.02 * abs(ref[k]) for k in ref)
    dh = lp_phase1_dh(rg5, tag="V_dh")
    ok = ok and abs(dh["t_star"] - 0.3697) <= 0.01
    print(f"  HiGHS {vals} vs CLARABEL {ref}; t*={dh['t_star']:.4f} vs 0.3697 "
          f"-> {'MATCH (pipeline trusted)' if ok else 'MISMATCH: STOP'}")
    if not ok:
        raise RuntimeError("HiGHS does not reproduce the e3x CLARABEL baseline")
    store.update({f"val_{k}": v for k, v in vals.items()})
    store["val_dh_tstar"] = dh["t_star"]
    npz_save(store)


def attack_a1(store, cache):
    print("\n=== A1: rung-6 stress (L=log 20000, om_max=120, Q-matched h) ===")
    cfg6 = dict(L=np.log(20000.0), N=20000, R=130.0, h=0.02, dom=0.5,
                ext_R=390.0)
    t0 = time.time()
    rg6 = cache.setdefault("rg6", e3x.build_rung(cfg6))
    eps_decompose_e3x(rg6)
    qmed = float(np.median(rg6["eps_Q"][[j for j, t in enumerate(rg6["tests"])
                                         if t[0] == "mod" and t[2] > 0]]))
    print(f"  rung 6: J={rg6['J']}, grid={len(rg6['r_grid'])}, "
          f"median Q (X=L mod tests) = {qmed:.4f} (rung-5 value 0.064) "
          f"[build {time.time() - t0:.0f}s]")
    ra = run_a_guard(rg6)
    print(f"  (a) guard: ratio={ra['ratio']:.3f} ({ra['solver']}), "
          f"hit_frac={ra['hit_frac']:.3f} (POST-HOC, TRF spreads mass), "
          f"low_frac={ra['low_frac']:.4f} "
          f"-> {'FEASIBLE' if ra['ratio'] <= 1 else 'GUARD FAIL'}")
    out = {}
    for key, idx, sense in (("c6", 5, "max"), ("c1", 0, "max"),
                            ("c2lo", 1, "min"), ("c2hi", 1, "max")):
        out[key] = lp_ceiling(rg6, idx, sense, tag=f"A1_{key}")["val"]
    dh = lp_phase1_dh(rg6, tag="A1_dh")
    # analytic one-test certificate (plain Fejer X=L), as in e3x run (c)
    L = cfg6["L"]
    j_star = next(i for i, tt in enumerate(rg6["tests"])
                  if tt[0] == "mod" and tt[2] == 0.0
                  and abs(tt[1] - round(L, 4)) < 1e-9)
    cert_val = float(rg6["arch_d"][j_star])
    cert_tail = tail_integral(rg6["tests"][j_star], R_ARCH, 5.0 / TWO_PI)
    print(f"  A1 rung 6 (h=0.02, Q-matched): max c6={out['c6']:.4f}, "
          f"max c1={out['c1']:.4f}, c2 in [{out['c2lo']:.4f}, {out['c2hi']:.4f}] "
          f"(kappa2 [{out['c2lo'] * np.sqrt(2):.4f}, {out['c2hi'] * np.sqrt(2):.4f}]), "
          f"DH t*={dh['t_star']:.4f}, cert {cert_val:.4f}+/-{cert_tail:.4f}")

    # artifact discriminator: same L, h=0.025 (Q looser by ~57%)
    cfg6b = dict(cfg6, h=0.025)
    rg6b = e3x.build_rung(cfg6b)
    eps_decompose_e3x(rg6b)
    qmed_b = float(np.median(rg6b["eps_Q"][[j for j, t in enumerate(rg6b["tests"])
                                            if t[0] == "mod" and t[2] > 0]]))
    rb = run_a_guard(rg6b)
    c6b = lp_ceiling(rg6b, 5, "max", tag="A1b_c6")["val"]
    c1b = lp_ceiling(rg6b, 0, "max", tag="A1b_c1")["val"]
    print(f"  A1b rung 6 (h=0.025, median Q={qmed_b:.4f}): guard ratio "
          f"{rb['ratio']:.3f}, max c6={c6b:.4f}, max c1={c1b:.4f}")
    print(f"  [artifact read: c1 went {out['c1']:.4f} -> {c1b:.4f} when Q/2 "
          f"went {qmed / 2:.4f} -> {qmed_b / 2:.4f} at FIXED L and tests]")
    store.update(a1_c6=out["c6"], a1_c1=out["c1"], a1_c2lo=out["c2lo"],
                 a1_c2hi=out["c2hi"], a1_tstar=dh["t_star"],
                 a1_aratio=ra["ratio"], a1_ahit=ra["hit_frac"],
                 a1_J=rg6["J"], a1_qmed=qmed, a1_certval=cert_val,
                 a1_certtail=cert_tail, a1b_c6=c6b, a1b_c1=c1b,
                 a1b_qmed=qmed_b, a1b_aratio=rb["ratio"])
    npz_save(store)


def attack_a2(store, cache):
    print("\n=== A2: family independence (Hann windows; shifted/jittered grids) ===")
    cfg5 = e3x.RUNGS[4]
    t0 = time.time()
    rgh = cache.setdefault("rgh", build_custom(cfg5, family="hann"))
    qmed = float(np.median(rgh["eps_Q"][[j for j, t in enumerate(rgh["tests"])
                                         if t[0] == "hmod" and t[2] > 0]]))
    print(f"  Hann rung-5-equivalent: J={rgh['J']}, median Q={qmed:.4f} "
          f"[build {time.time() - t0:.0f}s]")
    rah = run_a_guard(rgh)
    print(f"  (a) guard: ratio={rah['ratio']:.3f} ({rah['solver']}) "
          f"-> {'FEASIBLE' if rah['ratio'] <= 1 else 'GUARD FAIL'}")
    # CLARABEL (via e3x.run_be) for the Hann ceilings: the HiGHS dual simplex
    # grinds without terminating on the signed dense Hann columns (observed
    # > 15 min vs ~1 min interior-point; two runs had to be killed)
    be = e3x.run_be(rgh)
    outh = dict(c6=be["c6_max"][0], c1=be["c1_max"][0],
                c2lo=be["c2_min"][0], c2hi=be["c2_max"][0])
    dhh = lp_phase1_dh(rgh, tag="A2h_dh")
    fk = dhh["farkas"]
    print(f"  Hann: max c6={outh['c6']:.4f} (Fejer 0.2133), "
          f"max c1={outh['c1']:.4f} (0.0299), "
          f"c2 in [{outh['c2lo']:.4f}, {outh['c2hi']:.4f}] "
          f"([0.4166, 0.5488]), DH t*={dhh['t_star']:.4f} (0.3697)")
    if fk:
        print(f"      Hann DH Farkas combo: {fk['n_active']} active, "
              f"src={fk['src']:.4f}, min u={fk['u_min']:.2e}, "
              f"min v={fk['v_min']:.2e} (signed family: u>=0 not automatic)")

    rgs = build_custom(cfg5, family="fejer", grid_mode="shifted")
    ras = run_a_guard(rgs)
    c6s = lp_ceiling(rgs, 5, "max", tag="A2s_c6")["val"]
    c1s = lp_ceiling(rgs, 0, "max", tag="A2s_c1")["val"]
    rgj = build_custom(cfg5, family="fejer", grid_mode="jitter")
    raj = run_a_guard(rgj)
    c6j = lp_ceiling(rgj, 5, "max", tag="A2j_c6")["val"]
    print(f"  shifted grid (h/2): guard {ras['ratio']:.3f}, max c6={c6s:.4f}, "
          f"max c1={c1s:.4f}")
    print(f"  jittered grid (+-0.4h, seed 20260611): guard {raj['ratio']:.3f}, "
          f"max c6={c6j:.4f}")
    dev = max(abs(outh["c6"] - 0.2133), abs(c6s - 0.2133),
              abs(c6j - 0.2133)) / 0.2133
    print(f"  c6 ceiling max relative deviation across variants: {dev:.1%} "
          f"({'within' if dev <= 0.20 else 'OUTSIDE'} the 20% gate)")
    store.update(a2_hann_c6=outh["c6"], a2_hann_c1=outh["c1"],
                 a2_hann_c2lo=outh["c2lo"], a2_hann_c2hi=outh["c2hi"],
                 a2_hann_tstar=dhh["t_star"], a2_hann_aratio=rah["ratio"],
                 a2_hann_qmed=qmed, a2_shift_c6=c6s, a2_shift_c1=c1s,
                 a2_shift_aratio=ras["ratio"], a2_jit_c6=c6j,
                 a2_jit_aratio=raj["ratio"], a2_c6_maxdev=dev)
    npz_save(store)


def attack_a3(store, cache):
    print("\n=== A3: ghost hunt (exhibit a refinement-robust c6 >= 0.2 crystal) ===")
    rg5 = cache.setdefault("rg5", e3x.build_rung(e3x.RUNGS[4]))
    gr = lp_ghost_robust(rg5, idx=5, target=0.2)
    if not gr["ok"]:
        print("  no feasible c6 >= 0.2 crystal at rung 5 at ANY slack scale "
              "(infeasible even at tau -> inf): ghost dead on arrival")
        store.update(a3_tau=np.nan)
        npz_save(store)
        return
    w5, c5 = gr["w"], gr["c"]
    # POST-HOC autopsy of the ghost (zero landmarks used only here)
    r = rg5["r_grid"]
    low_mass = float(w5[r <= 13.0].sum())
    vm = vm_comb(rg5["cfg"]["N"])
    devi = c5 - vm
    top = np.argsort(-np.abs(devi))[:6]
    print(f"  ghost at tau*={gr['tau']:.4f}: c6={c5[5]:.4f}, c2={c5[1]:.4f} "
          f"(truth 0.4901), c3={c5[2]:.4f} (truth 0.6343), "
          f"POST-HOC mu mass in r<=13: {low_mass:.4f}")
    print(f"  top comb deviations (n, ghost, truth): "
          + ", ".join(f"({i + 1}, {c5[i]:.3f}, {vm[i]:.3f})" for i in top))

    rg6 = cache.get("rg6")
    if rg6 is None:
        cfg6 = dict(L=np.log(20000.0), N=20000, R=130.0, h=0.02, dom=0.5,
                    ext_R=390.0)
        rg6 = cache.setdefault("rg6", e3x.build_rung(cfg6))
    comp = lp_ghost_completion(rg6, rg5, w5, c5)
    print(f"  rung-6 refinement: naive max violation {comp['naive_max']:.2f}x eps "
          f"({comp['naive_nviol']} tests broken); best-completion t* = "
          f"{comp['t_star']:.4f} -> "
          f"{'GHOST DIES under refinement' if comp['t_star'] > 1e-6 else 'GHOST SURVIVES: KILL ARMED'}")
    rgh = cache.get("rgh")
    hx = hv = np.nan
    if rgh is not None:
        hx, hn = ghost_cross_eval(rgh, rg5, w5, c5)
        print(f"  Hann cross-family check: max ratio {hx:.2f}x eps "
              f"({hn} tests broken) -> "
              f"{'ghost is family-fragile' if hx > 1 else 'ghost passes Hann tests'}")
        hv = hn
    store.update(a3_tau=gr["tau"], a3_ghost_c2=c5[1], a3_ghost_c3=c5[2],
                 a3_ghost_lowmass=low_mass, a3_completion_t=comp["t_star"],
                 a3_naive_max=comp["naive_max"], a3_naive_nviol=comp["naive_nviol"],
                 a3_hann_maxratio=hx, a3_hann_nviol=hv)
    npz_save(store)


def attack_a4(store, cache):
    print("\n=== A4: c_1 plateau autopsy (duals, eps decomposition, h-sweep) ===")
    rg5 = cache.setdefault("rg5", e3x.build_rung(e3x.RUNGS[4]))
    if "eps_Q" not in rg5:
        eps_decompose_e3x(rg5)

    # eps decomposition by test class
    print("  eps decomposition at rung 5 (medians by class):")
    cls = np.array([classify(t) for t in rg5["tests"]])
    for cname in ("plain", "om<=13", "om>13", "trans"):
        m = cls == cname
        if m.any():
            print(f"    {cname:>7}: eps={np.median(rg5['eps_z'][m]):.4f} "
                  f"[A={np.median(rg5['eps_A'][m]):.4f} "
                  f"B={np.median(rg5['eps_B'][m]):.4f} "
                  f"Q={np.median(rg5['eps_Q'][m]):.4f} "
                  f"base={np.median(rg5['eps_base'][m]):.4f}] (n={m.sum()})")
    qmed5 = float(np.median(rg5["eps_Q"][cls != "trans"]))

    # dual autopsy of max c1
    sol = lp_ceiling(rg5, 0, "max", duals=True, tag="A4_c1_duals")
    y, s = sol["y"], sol["s"]
    sat = np.abs(s) / rg5["eps_z"]
    print(f"  max c1 = {sol['val']:.4f}; slack saturation (|s|/eps > 0.999) "
          f"by class (POST-HOC om<=13 split):")
    for cname in ("plain", "om<=13", "om>13", "trans"):
        m = cls == cname
        if m.any():
            print(f"    {cname:>7}: {int(np.sum(sat[m] > 0.999))}/{m.sum()} "
                  f"saturated, sum|y|={np.sum(np.abs(y[m])):.3f}")
    topj = np.argsort(-np.abs(y))[:8]
    print("  top-|y| binding tests: "
          + ", ".join(f"{rg5['tests'][j][0]}(X={rg5['tests'][j][1]:.2f},"
                      f"p2={rg5['tests'][j][2]:.2f}) y={y[j]:.3f} s/eps={sat[j]:+.2f}"
                      for j in topj))

    # pure-h sweep at fixed L and tests
    hs = []
    for h in (0.015, 0.0125):
        cfgh = dict(e3x.RUNGS[4], h=h)
        t0 = time.time()
        rgh = e3x.build_rung(cfgh)
        eps_decompose_e3x(rgh)
        clsh = np.array([classify(t) for t in rgh["tests"]])
        qmed = float(np.median(rgh["eps_Q"][clsh != "trans"]))
        ra = run_a_guard(rgh)
        c1 = lp_ceiling(rgh, 0, "max", tag=f"A4_h{h}_c1")["val"]
        c6 = lp_ceiling(rgh, 5, "max", tag=f"A4_h{h}_c6")["val"]
        c2lo = lp_ceiling(rgh, 1, "min", tag=f"A4_h{h}_c2lo")["val"]
        c2hi = lp_ceiling(rgh, 1, "max", tag=f"A4_h{h}_c2hi")["val"]
        print(f"  h={h}: median Q={qmed:.4f} (Q/2={qmed / 2:.4f}), guard "
              f"{ra['ratio']:.3f} ({ra['solver']}), max c1={c1:.4f}, "
              f"max c6={c6:.4f}, c2 in [{c2lo:.4f}, {c2hi:.4f}] "
              f"[{time.time() - t0:.0f}s]")
        hs.append((h, qmed, ra["ratio"], c1, c6, c2lo, c2hi))
    store["a4_hsweep"] = np.array(hs)

    # dense low-omega probes (the #82 local-density-floor direction)
    rgl = build_custom(e3x.RUNGS[4], family="fejer", lowom_step=0.15)
    ral = run_a_guard(rgl)
    c1l = lp_ceiling(rgl, 0, "max", tag="A4_lowom_c1")["val"]
    print(f"  dense low-om probes (step 0.15 on (0,13], J={rgl['J']}): guard "
          f"{ral['ratio']:.3f}, max c1={c1l:.4f} (baseline 0.0299) -> "
          f"{'probes MOVE the plateau' if c1l < 0.8 * 0.0299 else 'probes do NOT move the plateau'}")

    store.update(a4_c1_rung5=sol["val"], a4_qmed5=qmed5, a4_lowom_c1=c1l,
                 a4_lowom_aratio=ral["ratio"], a4_y=y, a4_sat=sat)
    npz_save(store)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--attacks", type=str, default="V,A1,A2,A3,A4")
    args = ap.parse_args()
    todo = [a.strip().upper() for a in args.attacks.split(",") if a.strip()]
    print("=" * 78)
    print("e3x2: ADVERSARY stress round on the Lonely Crystal LP (A1-A4)")
    print("=" * 78 + "\n")
    e3x.selftest()
    hann_selftest()
    store = {}
    cache = {}
    drivers = dict(V=attack_v, A1=attack_a1, A2=attack_a2, A3=attack_a3,
                   A4=attack_a4)
    t_all = time.time()
    for a in todo:
        try:
            drivers[a](store, cache)
        except Exception:
            print(f"[ATTACK {a} CRASHED]")
            traceback.print_exc()
    print(f"\n[total wall {time.time() - t_all:.0f}s, solver time "
          f"{SOLVE_T[0]:.0f}s]")
    print(f"Saved {NPZ_PATH}")


if __name__ == "__main__":
    main()
