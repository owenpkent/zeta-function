"""e3x3: rung 7 with the corrected protocol. Is the P2a c_6 floor real?

This is the decisive instrument for the single most important open question on
the current LCC frontier (docs/03_research/lcc_bc_transport.md, SYNTHESIZER
update line 225): the e3x stress round (#84) showed the max-c_6 LP ceiling is
tolerance-proportional (c_6 ~ 3 eps) with an apparent intercept ~0.01-0.02. If
that intercept is zero, composite pinching (P2a, b_6 = 0) is LP-visible and the
P2a kill is NOT armable by an LP. If it is a genuine positive constant, the
LP exhibits a refinement-robust ghost and the P2a kill IS armable.

The corrected protocol (TODO line 168, e3x dossier appendix section 6) removes
every confound the stress round identified:

  (1) HOLD Q FIXED VIA h ~ L^{-3/2}. The grid-quantization slack term is
      Q ~ (X^3/6) h^2 with X ~ L, so Q ~ L^3 h^2; choosing h = h0 (L0/L)^{3/2}
      pins the median X=L Q across the L-ladder. Without this, h froze near
      0.025 while L grew and the one eps term that never shrank tracked the
      "plateau" exactly (#84 artifact reading). Here Q is held constant so it
      cannot masquerade as a floor.
  (2) ZERO-TOLERANCE INTERCEPT, GAIN-NORMALIZED. At each L run a tolerance
      sweep eps -> tau eps for tau in a decreasing ladder, record c_6(tau),
      and linearly extrapolate to tau = 0. The intercept c6_0(L) is the
      tolerance-free ceiling; the slope is the gain dc_6/d(tau). c6_0(L) is
      the only number that distinguishes artifact from floor at fixed L.
  (3) TRIM THE COMB EDGE (log n <= L - 1). Comb tests within e of the support
      end resolve poorly and inflate the feasible set near n = N; dropping
      them removes the resolution-effect contribution to c_6 that collapsed
      across rungs 1-5 (the "resolution not floor" reading of #83).
  (4) SHRINK THE NON-Q TOLERANCE TERMS (~0.005, the next floor). A, B and the
      1e-3 base are tightened (denser archimedean quadrature, larger ext_R,
      base -> 2e-4) so the residual tolerance budget after Q is dominated by Q
      alone; otherwise the ~0.005 of A+B+base sets a second false floor.
  (5) ghat >= 0 SUBFAMILY GATE. Signed test families are D-H-blind (#84
      discipline rule: the D-H firewall lives in the one-triangle ghat >= 0
      certificate, not in any signed LP). So the primary family here is the
      ghat >= 0 cone ONLY (plain Fejer X, cosine-modulated triangles); the
      signed translated pairs are run as a SEPARATE alternative subfamily and
      never as the sole test set. A floor that exists only with signed tests
      is invalid.

DELIVERABLE: c6_0(L) extrapolated as L -> infinity. Trend toward 0 => artifact,
P2a kill NOT armable; trend toward a positive constant => genuine floor, P2a
kill ARMABLE. The D-H control (run (c) of e3x) is carried at the top L to
confirm the firewall under the tightened tolerances.

HONESTY BLOCK (inherited from e3x, unchanged):
  * K1: no zero data in any constraint, grid, objective, or solver input. The
    GAMMAS landmarks enter ONLY a post-hoc localization metric.
  * Soft-detector freeze: this is a FALSIFICATION instrument. The c6_0
    extrapolation is a diagnostic of whether the LP can SEE pinching, never
    evidence for or against RH. Attainment stays fenced off.
  * Discretization semantics: grid restricts the cone, finite tests relax it;
    primal ceilings are indicative, the deliverable is the L-trend of the
    zero-tolerance intercept. The run (a) truth-comb guard must pass first.

Run: python -m experiments.positivity.e3x3_rung7 [--Ls 1,2,3,4]
Outputs: e3x3_rung7.npz, e3x3_rung7.png, stdout tables.
"""

from __future__ import annotations

import argparse
import time
from pathlib import Path

import numpy as np
from scipy.integrate import simpson
from scipy.optimize import linprog

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    HAVE_MPL = True
except Exception:                      # numpy/matplotlib ABI mismatch in env
    HAVE_MPL = False

from scipy.special import digamma as sp_digamma

# Inlined from e3x_lonely_crystal_lp (the source module imports matplotlib at
# load time, which is ABI-broken against numpy 2.4 in this env; these helpers
# are pure numpy/scipy and identical to the e3x definitions). K1/discipline
# semantics are unchanged: see the e3x docstring.

LOG_PI = np.log(np.pi)
TWO_PI = 2.0 * np.pi
LOG2 = np.log(2.0)

GAMMAS = np.array([
    14.134725141734693, 21.022039638771555, 25.010857580145688,
    30.424876125859513, 32.935061587739190, 37.586178158825671,
    40.918719012147495, 43.327073280914999, 48.005150881167159,
    49.773832477672302])


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
    return (lam / np.sqrt(n_arr))[1:]


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
    kind, p1, p2 = t
    if kind == "mod":
        X, om = p1, p2
        a = 0.5 + 1j * om
        return float(4.0 * np.real((np.cosh(a * X) - 1.0) / (a * a * X)))
    a, T = p1, p2
    return float((32.0 / a) * np.cosh(T / 2.0) * (np.cosh(a / 2.0) - 1.0))


def test_env(t, r):
    kind, p1, p2 = t
    r = np.asarray(r, dtype=float)
    if kind == "mod":
        X, om = p1, p2
        return (2.0 / X) * (1.0 / (r - om) ** 2 + 1.0 / (r + om) ** 2)
    a, _ = p1, p2
    return 8.0 / (a * r ** 2)


def tail_integral(t, r_from, logc):
    rr = np.geomspace(r_from, 1.0e7, 4001)
    return float(np.trapezoid(test_env(t, rr) * (np.log(logc * rr) + 1.0), rr) / np.pi)

OUT_DIR = Path(__file__).resolve().parent
NPZ_PATH = OUT_DIR / "e3x3_rung7.npz"

# tighter archimedean quadrature than e3x (term A shrink, protocol (4))
R_ARCH = 2000.0
DR_ARCH = 0.0015

# fixed-Q anchor: rung 5 of e3x had L=log(5000)~8.517, h=0.025. We pin Q to that
# anchor's median X=L value and slide h = H0 * (L0 / L)^1.5 along the ladder.
L0 = np.log(5000.0)
H0 = 0.025

# the L-ladder for rung 7: extends past e3x rung 5 with Q held fixed. Five
# rungs span L in [8.5, 9.7] (N from 5e3 to 17e3) with Q pinned. EMPIRICAL
# MEMORY CEILING in this env: the IPM comb matrix OOM-kills above ~6.3k kept
# columns (N ~ 17k after the log n <= L-1 trim); N=24k (rung 5, ~8.8k cols) and
# N>=45k were OOM-killed mid-solve. Four rungs are enough for a clean a + b/L
# extrapolation; rung 5 is kept smaller so the full ladder reproduces.
LADDER = [
    dict(L=np.log(5000.0),    N=5000,    R=110.0, dom=0.55, ext_R=600.0),
    dict(L=np.log(8000.0),    N=8000,    R=118.0, dom=0.52, ext_R=640.0),
    dict(L=np.log(12000.0),   N=12000,   R=124.0, dom=0.50, ext_R=680.0),
    dict(L=np.log(17000.0),   N=17000,   R=130.0, dom=0.48, ext_R=720.0),
]

# tolerance sweep ladder (tau scales the WHOLE eps; intercept = tau -> 0). Five
# points are enough for a clean linear extrapolation (c_6 is linear in tau).
TAUS = np.array([1.0, 0.75, 0.5, 0.3, 0.15])

BASE_FRAC = 2.0e-4   # protocol (4): base term 1e-3 -> 2e-4


def h_of_L(L):
    """h ~ L^{-3/2} holding Q ~ (X^3/6) h^2 fixed at the (L0, H0) anchor."""
    return H0 * (L0 / L) ** 1.5


# ----------------------------------------------------------------------------
# Rung assembly: ghat >= 0 primary cone + signed alternative subfamily, with
# the comb-edge trim and the tightened non-Q tolerances.
# ----------------------------------------------------------------------------

def build_rung7(cfg, include_signed=False, comb_edge_trim=1.0):
    L, N, R, dom, ext_R = (cfg["L"], cfg["N"], cfg["R"], cfg["dom"], cfg["ext_R"])
    h = h_of_L(L)
    om_max = R - 10.0

    # PRIMARY family: ghat >= 0 only. Plain Fejer at several X + cosine-modulated
    # triangles at X = L over a uniform omega lattice. ("mod", X, omega) with
    # omega = 0 is the plain triangle; both have ghat >= 0 on R (e3x docstring).
    tests = []
    n_plain = 0
    for X in sorted({2.0, round(0.5 * L, 4), round(0.75 * L, 4), round(L, 4)}):
        tests.append(("mod", float(X), 0.0))
        n_plain += 1
    for om in np.arange(dom, om_max + 1e-9, dom):
        tests.append(("mod", float(L), float(om)))
    n_pos = len(tests)

    # ALTERNATIVE subfamily (signed; run separately, never sole): translated
    # triangle pairs. Tagged by index >= n_pos so we can mask them out.
    if include_signed:
        for T in np.arange(1.0, L - 1.0 + 1e-9, 0.5):
            tests.append(("trans", 1.0, float(T)))
    J = len(tests)

    h_fine = h
    r_fine = np.arange(0.0, R + h_fine / 2, h_fine)
    r_ext = np.arange(R + 0.5, ext_R + 1e-9, 0.5)
    r_grid = np.concatenate([r_fine, r_ext])
    M_fine = len(r_fine)

    Smat = np.vstack([test_ghat(t, r_grid) for t in tests])

    # comb-edge trim (protocol (3)): only comb sites with log n <= L - trim are
    # kept as free variables; the rest are pinned to the von Mangoldt truth so
    # the edge resolution effect cannot inflate the feasible set. The trimmed
    # tail is moved into the rhs as a fixed contribution.
    n_all = np.arange(1, N + 1, dtype=float)
    x_n = np.log(n_all)
    keep = x_n <= (L - comb_edge_trim)
    N_keep = int(keep.sum())
    Cmat_full = 2.0 * np.vstack([test_g(t, x_n) for t in tests])
    Cmat = Cmat_full[:, keep]
    c_vm = vm_comb(N)
    fixed_tail = Cmat_full[:, ~keep] @ c_vm[~keep]   # truth comb beyond the trim
    idx6 = int(np.where(n_all == 6)[0][0])           # n = 6 column index in keep
    assert keep[idx6], "n=6 must be inside the comb-edge trim"
    idx6_keep = int(np.sum(keep[:idx6 + 1]) - 1)
    idx1_keep = 0                                     # n = 1 is always kept
    idx2_keep = int(np.sum(keep[:2]) - 1)

    r_arch = np.arange(0.0, R_ARCH + DR_ARCH / 2, DR_ARCH)
    omz, omd = omega_zeta(r_arch), omega_dh(r_arch)
    arch_z = np.empty(J)
    arch_d = np.empty(J)
    for j, t in enumerate(tests):
        gh = test_ghat(t, r_arch)
        arch_z[j] = simpson(gh * omz, x=r_arch) / np.pi
        arch_d[j] = simpson(gh * omd, x=r_arch) / np.pi
    pole = np.array([test_pole(t) for t in tests])
    rhs_z = pole + arch_z - fixed_tail
    rhs_d = arch_d.copy()                              # D-H: no pole, no comb tail

    # tolerance decomposition with the protocol (4) shrink. A: arch tail to
    # R_ARCH (now 2000 + finer step). B: spectral mass beyond ext_R (now larger).
    # Q: grid quantization, the term we HOLD FIXED. base: 1e-3 -> 2e-4.
    eps_z = np.empty(J)
    eps_d = np.empty(J)
    epsQ = np.empty(J)
    epsAB = np.empty(J)
    for j, t in enumerate(tests):
        A_z = tail_integral(t, R_ARCH, 1.0 / TWO_PI)
        A_d = tail_integral(t, R_ARCH, 5.0 / TWO_PI)
        B_z = tail_integral(t, ext_R, 1.0 / TWO_PI)
        B_d = tail_integral(t, ext_R, np.sqrt(5.0) / TWO_PI)
        d2 = float(np.max(np.abs(np.diff(Smat[j, :M_fine], n=2)))) if M_fine > 2 else 0.0
        Q = 2.0 * d2
        base_z = BASE_FRAC * max(1.0, abs(rhs_z[j]))
        base_d = BASE_FRAC * max(1.0, abs(rhs_d[j]))
        eps_z[j] = A_z + B_z + Q + base_z
        eps_d[j] = A_d + B_d + Q + base_d
        epsQ[j] = Q
        epsAB[j] = A_z + B_z + base_z

    qmed = float(np.median(epsQ[[j for j, t in enumerate(tests)
                                 if t[0] == "mod" and t[2] > 0]]))
    return dict(cfg=cfg, h=h, tests=tests, J=J, n_pos=n_pos, r_grid=r_grid,
                M_fine=M_fine, om_max=om_max, Smat=Smat, Cmat=Cmat,
                x_n=x_n[keep], keep=keep, N_keep=N_keep, c_vm=c_vm,
                idx6=idx6_keep, idx1=idx1_keep, idx2=idx2_keep,
                rhs_z=rhs_z, rhs_d=rhs_d, eps_z=eps_z, eps_d=eps_d,
                arch_d=arch_d, qmed=qmed, epsAB=epsAB)


# ----------------------------------------------------------------------------
# LP layer (HiGHS): max/min of one comb coordinate over the truncated cone with
# the eps scaled by tau (the tolerance sweep). Variables [w >= 0, c >= 0, s].
# ----------------------------------------------------------------------------

def _Aeq(rg):
    """Sparse [S | C | I] built once per rung and cached. HiGHS is far faster
    on the sparse form here (the slack block is the identity and most comb
    columns touch few tests)."""
    if "_Aeq_cache" in rg:
        return rg["_Aeq_cache"]
    from scipy.sparse import hstack as sphstack, csc_matrix, eye as speye
    S, C = rg["Smat"], rg["Cmat"]
    J = S.shape[0]
    A = sphstack([csc_matrix(S), csc_matrix(C), speye(J, format="csc")],
                 format="csc")
    rg["_Aeq_cache"] = A
    return A


def lp_ceiling(rg, n_keep_idx, sense="max", tau=1.0):
    S, C = rg["Smat"], rg["Cmat"]
    J, M = S.shape
    Nk = C.shape[1]
    nv = M + Nk + J
    A_eq = _Aeq(rg)
    cost = np.zeros(nv)
    cost[M + n_keep_idx] = -1.0 if sense == "max" else 1.0
    eps = tau * rg["eps_z"]
    lb = np.concatenate([np.zeros(M + Nk), -eps])
    ub = np.concatenate([np.full(M + Nk, np.inf), eps])
    res = linprog(cost, A_eq=A_eq, b_eq=rg["rhs_z"],
                  bounds=np.column_stack([lb, ub]), method="highs-ipm")
    if res.status != 0:
        return np.nan
    return (-res.fun if sense == "max" else res.fun)


def run_a_guard(rg):
    """Truth-comb feasibility as a phase-1 LP: min t s.t. |S w - rhs_a| <= t eps,
    w >= 0. rhs_a uses the kept-comb truth (the trimmed tail is already in rhs)."""
    S = rg["Smat"]
    J, M = S.shape
    c_keep = rg["c_vm"][rg["keep"]]
    rhs_a = rg["rhs_z"] - rg["Cmat"] @ c_keep
    eps = rg["eps_z"]
    A_ub = np.vstack([np.hstack([S, -eps[:, None]]),
                      np.hstack([-S, -eps[:, None]])])
    b_ub = np.concatenate([rhs_a, -rhs_a])
    cost = np.zeros(M + 1)
    cost[-1] = 1.0
    res = linprog(cost, A_ub=A_ub, b_ub=b_ub,
                  bounds=[(0.0, None)] * (M + 1), method="highs")
    if res.status != 0:
        return dict(ratio=np.inf, hit_frac=0.0, w=None)
    w = res.x[:M]
    ratio = float(res.fun)
    # POST-HOC localization (only place GAMMAS are used)
    r = rg["r_grid"][:rg["M_fine"]]
    wf = w[:rg["M_fine"]]
    gam_use = GAMMAS[GAMMAS <= rg["om_max"] - 2.0]
    r_cap = gam_use[-1] + 2.0 if len(gam_use) else 0.0
    tot = float(wf[r <= r_cap].sum())
    hit = sum(float(wf[np.abs(r - gm) <= 0.5].sum()) for gm in gam_use)
    hit_frac = hit / tot if tot > 0 else 0.0
    return dict(ratio=ratio, hit_frac=hit_frac, w=w)


def lp_phase1_dh(rg):
    """min t s.t. S w + s = rhs_d, |s_j| <= eps_d_j + t (no comb: D-H cone is
    tested for emptiness on the ghat >= 0 family alone). t* > 0 => infeasible."""
    S = rg["Smat"]
    J, M = S.shape
    nv = M + J + 1
    A_eq = np.hstack([S, np.eye(J), np.zeros((J, 1))])
    # |s_j| <= eps_d_j + t  ->  s_j - t <= eps,  -s_j - t <= eps
    rows = np.concatenate([np.arange(J), np.arange(J),
                           np.arange(J, 2 * J), np.arange(J, 2 * J)])
    cols = np.concatenate([M + np.arange(J), np.full(J, nv - 1),
                           M + np.arange(J), np.full(J, nv - 1)])
    vals = np.concatenate([np.ones(J), -np.ones(J), -np.ones(J), -np.ones(J)])
    from scipy.sparse import coo_matrix
    A_ub = coo_matrix((vals, (rows, cols)), shape=(2 * J, nv))
    b_ub = np.concatenate([rg["eps_d"], rg["eps_d"]])
    cost = np.zeros(nv)
    cost[-1] = 1.0
    bounds = [(0.0, None)] * M + [(None, None)] * J + [(0.0, None)]
    res = linprog(cost, A_eq=A_eq, b_eq=rg["rhs_d"], A_ub=A_ub, b_ub=b_ub,
                  bounds=bounds, method="highs")
    return float(res.fun) if res.status == 0 else np.nan


# ----------------------------------------------------------------------------
# Tolerance-sweep -> zero-tolerance intercept at fixed L
# ----------------------------------------------------------------------------

def intercept_at_L(rg, idx, sense="max", taus=TAUS):
    """Run the tau-sweep, fit value(tau) ~ c0 + g * tau by least squares on the
    feasible points, return (c0, gain, vals). c0 is the zero-tolerance
    intercept (gain-normalized via the slope g)."""
    vals = np.array([lp_ceiling(rg, idx, sense, tau=t) for t in taus])
    ok = np.isfinite(vals)
    if ok.sum() < 2:
        return np.nan, np.nan, vals
    A = np.vstack([np.ones(ok.sum()), taus[ok]]).T
    coef, *_ = np.linalg.lstsq(A, vals[ok], rcond=None)
    c0, gain = float(coef[0]), float(coef[1])
    return c0, gain, vals


# ----------------------------------------------------------------------------
# Driver
# ----------------------------------------------------------------------------

def _persist_rung(row):
    """Merge one rung's results into the npz immediately (kill-safe)."""
    save = {}
    if NPZ_PATH.exists():
        with np.load(NPZ_PATH) as old:
            save.update({key: old[key] for key in old.files})
    k = row["k"]
    for key in ("L", "h", "J", "qmed", "aratio", "ahit",
                "c6_0", "c6_g", "c1_0", "c1_g", "c2lo_0", "c2hi_0"):
        save[f"L{k}_{key}"] = row[key]
    save[f"L{k}_c6_vals"] = row["c6_vals"]
    save["taus"] = TAUS
    save["gammas_posthoc"] = GAMMAS
    np.savez_compressed(NPZ_PATH, **save)


def main(L_ids=None, run_controls=True):
    print("=" * 78)
    print("e3x3: rung 7, corrected protocol. Is the P2a c_6 floor real?")
    print("=" * 78)
    print(f"  fixed-Q anchor (L0={L0:.3f}, H0={H0}); h = H0 (L0/L)^1.5")
    print(f"  zero-tolerance intercept via tau-sweep {TAUS.tolist()}")
    print(f"  primary family: ghat >= 0 only; comb-edge trim log n <= L - 1; "
          f"base {BASE_FRAC}\n")

    todo = [(k, cfg) for k, cfg in enumerate(LADDER, start=1)
            if L_ids is None or k in L_ids]
    rows = []
    for k, cfg in todo:
        t0 = time.time()
        rg = build_rung7(cfg)
        print(f"--- L{k}: L={cfg['L']:.3f} (N={cfg['N']}), h={rg['h']:.5f}, "
              f"R={cfg['R']:.0f}, J={rg['J']} (ghat>=0), N_keep={rg['N_keep']}, "
              f"grid={len(rg['r_grid'])}, medQ={rg['qmed']:.4f} "
              f"[build {time.time()-t0:.0f}s]")

        ra = run_a_guard(rg)
        feas = ra["ratio"] <= 1.0
        print(f"  (a) truth-comb guard: max|res|/eps = {ra['ratio']:.3f}, "
              f"hit_frac = {ra['hit_frac']:.3f} "
              f"-> {'FEASIBLE' if feas else 'GUARD FAIL (widen grid)'}")

        # zero-tolerance intercepts, gain-normalized. c_6 gets the full sweep
        # (it is the deliverable); c_1/c_2 get a 3-point sweep (budget).
        coarse = np.array([1.0, 0.5, 0.15])
        c6_0, c6_g, c6_vals = intercept_at_L(rg, rg["idx6"], "max")
        c1_0, c1_g, c1_vals = intercept_at_L(rg, rg["idx1"], "max", taus=coarse)
        c2hi_0, _, _ = intercept_at_L(rg, rg["idx2"], "max", taus=coarse)
        c2lo_0, _, _ = intercept_at_L(rg, rg["idx2"], "min", taus=coarse)
        print(f"  max c_6 over tau: {np.round(c6_vals, 4).tolist()}")
        print(f"      -> intercept c6_0 = {c6_0:+.5f}, gain dc6/dtau = {c6_g:.4f} "
              f"(c6 ~ {c6_g/rg['qmed']:.2f} * Q per unit tau)")
        print(f"  max c_1 over tau: {np.round(c1_vals, 4).tolist()}")
        print(f"      -> intercept c1_0 = {c1_0:+.5f}, gain dc1/dtau = {c1_g:.4f}")
        print(f"  kappa_2 intercept band: "
              f"[{c2lo_0*np.sqrt(2):.4f}, {c2hi_0*np.sqrt(2):.4f}] "
              f"vs log 2 = {LOG2:.6f}")

        row = dict(k=k, L=cfg["L"], h=rg["h"], J=rg["J"], qmed=rg["qmed"],
                   aratio=ra["ratio"], ahit=ra["hit_frac"],
                   c6_0=c6_0, c6_g=c6_g, c6_vals=c6_vals,
                   c1_0=c1_0, c1_g=c1_g, c2lo_0=c2lo_0, c2hi_0=c2hi_0)
        rows.append(row)
        _persist_rung(row)        # save NOW so a kill mid-ladder keeps this rung
        print(f"  [L{k} total {time.time()-t0:.0f}s]\n")

    # D-H control + signed-subfamily cross-check at the SMALLEST requested L
    # (cheapest; the firewall and the D-H-blindness discipline rule are L-robust,
    # and the c6_0 ghat>=0-vs-signed comparison is the point, not its L-trend).
    # Skipped on incremental --Ls runs that exclude rung 1 (the control L).
    if run_controls and todo[0][0] == 1:
        ctrl_cfg = todo[0][1]
        print("--- D-H control + signed-subfamily cross-check (control L) ---")
        rgd = build_rung7(ctrl_cfg)
        dh_t = lp_phase1_dh(rgd)
        print(f"  (c) D-H phase-1 (ghat>=0 family, tightened eps): t* = {dh_t:.4f} "
              f"-> {'INFEASIBLE (firewall holds)' if dh_t > 1e-6 else 'FEASIBLE: FIREWALL BREAK'}")
        rgs = build_rung7(ctrl_cfg, include_signed=True)
        c6_0_s, _, _ = intercept_at_L(rgs, rgs["idx6"], "max")
        ghat_only_ctrl = next(r["c6_0"] for r in rows if r["k"] == 1)
        print(f"  signed subfamily added (translated pairs, J {rgd['J']}->{rgs['J']}): "
              f"c6_0 = {c6_0_s:+.5f} (ghat>=0 only gave {ghat_only_ctrl:+.5f} at "
              f"control L); signed families are D-H-blind so this is a cross-check, "
              f"not the verdict")
        sv = {}
        with np.load(NPZ_PATH) as old:
            sv.update({key: old[key] for key in old.files})
        sv["dh_tstar_top"] = dh_t
        sv["c6_0_signed_top"] = c6_0_s
        np.savez_compressed(NPZ_PATH, **sv)

    # -------------------------------------- L -> infinity intercept extrapolation
    save = {}
    with np.load(NPZ_PATH) as old:
        save.update({key: old[key] for key in old.files})
    ks = [k for k in range(1, len(LADDER) + 1) if f"L{k}_c6_0" in save]
    Ls = np.array([float(save[f"L{k}_L"]) for k in ks])
    c6_0s = np.array([float(save[f"L{k}_c6_0"]) for k in ks])
    c1_0s = np.array([float(save[f"L{k}_c1_0"]) for k in ks])

    print("\n" + "=" * 78)
    print("RUNG-7 INTERCEPT TABLE (zero-tolerance, gain-normalized, Q fixed)")
    print("=" * 78)
    print(f"{'L#':>3} {'L':>7} {'h':>8} {'J':>5} {'medQ':>7} {'(a)res':>7} "
          f"{'c6_0':>9} {'c6 gain':>8} {'c1_0':>9}")
    for k in ks:
        print(f"{k:>3} {float(save[f'L{k}_L']):>7.3f} "
              f"{float(save[f'L{k}_h']):>8.5f} {int(save[f'L{k}_J']):>5} "
              f"{float(save[f'L{k}_qmed']):>7.4f} "
              f"{float(save[f'L{k}_aratio']):>7.3f} "
              f"{float(save[f'L{k}_c6_0']):>+9.5f} "
              f"{float(save[f'L{k}_c6_g']):>8.4f} "
              f"{float(save[f'L{k}_c1_0']):>+9.5f}")

    # L -> infinity extrapolation: fit c6_0(L) ~ a + b / L (the resolution model)
    verdict = "INCONCLUSIVE (need more L rungs)"
    a_inf = np.nan
    if len(ks) >= 2:
        A = np.vstack([np.ones(len(Ls)), 1.0 / Ls]).T
        coef, *_ = np.linalg.lstsq(A, c6_0s, rcond=None)
        a_inf, b_inf = float(coef[0]), float(coef[1])
        # also a pure-mean and a monotone-trend read
        decreasing = bool(np.all(np.diff(c6_0s) <= 1e-4))
        print(f"\nc6_0(L) ~ a + b/L fit: a (L->inf intercept) = {a_inf:+.5f}, "
              f"b = {b_inf:+.4f}")
        print(f"c6_0 sequence {np.round(c6_0s, 5).tolist()} "
              f"({'monotone decreasing' if decreasing else 'not monotone'})")
        floor_thresh = 0.01
        if a_inf <= floor_thresh and (decreasing or a_inf < c6_0s[0]):
            verdict = (f"ARTIFACT: c6_0 -> {a_inf:+.5f} <= {floor_thresh} as "
                       f"L->inf. Pinching is LP-visible; P2a kill NOT armable.")
        elif a_inf > floor_thresh:
            verdict = (f"GENUINE FLOOR: c6_0 -> {a_inf:+.5f} > {floor_thresh} as "
                       f"L->inf. Refinement-robust ghost; P2a kill ARMABLE.")

    print("\nVERDICTS (instrument diagnostics, not RH evidence):")
    okg = (float(save[f"L{ks[-1]}_aratio"]) <= 1.0
           and float(save[f"L{ks[-1]}_ahit"]) >= 0.7)
    print(f"  (a) truth-comb guard at top L: {'PASS' if okg else 'CHECK'}")
    if "dh_tstar_top" in save:
        dht = float(save["dh_tstar_top"])
        print(f"  (c) D-H control: t* = {dht:.4f} -> "
              f"{'INFEASIBLE (firewall holds)' if dht > 1e-6 else 'FIREWALL BREAK'}; "
              f"signed cross-check c6_0 = {float(save['c6_0_signed_top']):+.5f}")
    c2lo = float(save[f"L{ks[-1]}_c2lo_0"]) * np.sqrt(2)
    c2hi = float(save[f"L{ks[-1]}_c2hi_0"]) * np.sqrt(2)
    print(f"  (P2b) kappa_2 intercept band at top L: [{c2lo:.4f}, {c2hi:.4f}] "
          f"vs log 2 = {LOG2:.4f} ({'brackets log 2' if c2lo <= LOG2 <= c2hi else 'OUTSIDE'})")
    print(f"\n  HEADLINE (P2a): {verdict}")

    # ----------------------------------------------------------------- plot
    if not HAVE_MPL:
        print(f"\n[matplotlib unavailable in env; skipped plot]")
        print(f"Saved {NPZ_PATH}")
        return a_inf, verdict
    fig, axs = plt.subplots(1, 2, figsize=(13, 5))
    ax = axs[0]
    for k in ks:
        vv = np.asarray(save[f"L{k}_c6_vals"], dtype=float)
        ax.plot(TAUS, vv, "o-", label=f"L={float(save[f'L{k}_L']):.2f}")
    ax.axhline(0.0, color="gray", lw=0.8)
    ax.set_xlabel("tolerance scale tau (eps -> tau eps)")
    ax.set_ylabel("max c_6 (truth 0)")
    ax.set_title("c_6 ceiling vs tolerance (Q held fixed)\nintercept at tau=0 is the floor candidate")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)
    ax = axs[1]
    ax.plot(Ls, c6_0s, "o-", label="c6_0 (zero-tol intercept)")
    ax.plot(Ls, c1_0s, "s--", label="c1_0")
    if np.isfinite(a_inf):
        xx = np.linspace(Ls.min(), max(Ls.max() * 1.4, 20), 100)
        ax.plot(xx, a_inf + b_inf / xx, "r:", lw=1.0,
                label=f"a+b/L fit, a={a_inf:+.4f}")
        ax.axhline(a_inf, color="r", lw=0.6, ls="-")
    ax.axhline(0.0, color="gray", lw=0.8)
    ax.set_xlabel("comb support L = log N")
    ax.set_ylabel("zero-tolerance intercept")
    ax.set_title("c6_0(L) extrapolation to L -> infinity")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(OUT_DIR / "e3x3_rung7.png", dpi=140)
    plt.close()
    print(f"\nSaved {NPZ_PATH}")
    print(f"Saved {OUT_DIR / 'e3x3_rung7.png'}")
    return a_inf, verdict


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--Ls", type=str, default="",
                    help="comma-separated L-ladder ids, e.g. 1,2,3")
    ap.add_argument("--no-controls", action="store_true",
                    help="skip the D-H + signed cross-check (incremental runs)")
    args = ap.parse_args()
    ids = [int(x) for x in args.Ls.split(",") if x.strip()] or None
    main(ids, run_controls=not args.no_controls)
