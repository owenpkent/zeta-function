"""E1W: the literal Burnol bilinear extension. Does the kappa=1 ansatz survive?

ROLE: BUILDER. Executes PHASE_STATE next-step 1, third clause: "verify the
negative-square kernel ansatz against Burnol's literal bilinear extension."

WHY THIS RUNG. LEARNINGS #168(iii) answered the L_a negative-square question
at CANDIDATE tier: modeling the pole pair s = 0, 1 of the zeta-loaded Sonine
space L_a as an additive generalized-Nevanlinna singular term with mirror
poles about Re(s) = 1/2 gives a 2x2 evaluator block [[0, -rho], [-rhobar, 0]]
of signature (1,1), i.e. exactly one negative square (kappa = 1). Its recorded
honest limit: that used a LOCAL ADDITIVE KERNEL ANSATZ, never checked against
what Burnol actually defines. This module computes the literal object.

THE LITERAL OBJECT (Burnol, arXiv:math/0203120, JTNB 16 (2004) 65-94; the
verbatim quotes and equation numbers are in e1w_burnol_bilinear.md):
  - K = L^2(0, infinity; dt), F_+(f)(u) = 2 int_0^inf cos(2 pi t u) f(t) dt
    (Note 2 of the paper). L_a = {f in K : f constant on (0,a) and F_+(f)
    constant on (0,a)} is a SUB-HILBERT SPACE of K (Section 2). K_a is the
    same with "constant" replaced by "vanishing".
  - Prop 2.2: for f in L_a, M(f)(s) = pi^(-s/2) Gamma(s/2) fhat(s) is
    meromorphic with at most simple poles at s = 0, 1; the residue evaluators
    are continuous linear forms represented via the BILINEAR pairing
    [f, g] = int_0^inf f g dt by vectors Y_0^a, Y_1^a in L_a.
  - Prop 4.5 (second proof): L_a^perp (in K) is the closure of
    Phi_0 + F_+(Phi_0) with Phi_0 = mean-zero L^2(0,a); dim(L_a / K_a) = 2.

THE DERIVED DICTIONARY (proved in the dossier, Section 4; verified here):
  Res_1 M(f) = -f(0+), Res_0 M(f) = (F_+ f)(0+) for f in L_a. Hence
  Y_1^a = P_{L_a} u_1 with u_1 = -(1/a) 1_(0,a), and Y_0^a = P_{L_a} u_0 with
  u_0 = (1/a) F_+ 1_(0,a); moreover Y_0^a = -F_+(Y_1^a) exactly (the
  closed-form relation #168 recorded as missing). The extension block, in
  BOTH the bilinear convention ([Y_i, Y_j] = the coefficient matrix of the
  doubly-singular part of the literal reproducing kernel) and the Hermitian
  convention (the Gram matrix of the orthogonal complement L_a - K_a), is
  the SAME real symmetric 2x2 matrix
      B = [[N, beta], [beta, N]],  N = ||Y_1||^2,  beta = (Y_0, Y_1),
  because Y_0, Y_1 are real. Its signature decides the pre-registered
  outcome: (1,1) would CONFIRM the ansatz, (2,0) CORRECTS it to kappa = 0.

WHAT THE COMPUTATION DOES. Two independent routes to B:
  ROUTE A: Legendre-Galerkin. Orthonormal mean-zero shifted Legendre basis
    for Phi_0, Gauss-Legendre quadrature (nodes by Newton at mp precision),
    LU solve of the 2K x 2K Gram system, Schur-complement formula for B.
  ROUTE B: Chebyshev-Galerkin. Mean-zero shifted Chebyshev basis (non-
    orthogonal), Clenshaw-Curtis quadrature, same abstract algebra on a
    different Gram. At matched K the exact-arithmetic answers coincide, so
    the A-vs-B discrepancy measures the numerical error of both code paths.
  ROUTE R (residue reading): B is re-read off the CONSTANT values of the
    computed projections (Res_1 = -constant), evaluated pointwise at spread
    points of (0,a); this instantiates Prop 2.2's residue functionals
    directly and converges with K independently of the Gram algebra.
Plus convention anchors pinning the implementation to the paper: the
completed-Mellin functional equation on the Gaussian, chi(s) =
pi^(s-1/2) Gamma((1-s)/2) / Gamma(s/2) = zeta(s)/zeta(1-s) (eqs (7)-(8)),
the indicator Mellin identity, and the co-Poisson formula (9) verified
end-to-end numerically (full mode).

VERDICT (measured; see main): CORRECTED. The literal extension block is
positive definite, signature (2,0), zero negative squares, at every a and
every discretization: kappa(L_a) = 0. The literal diagonal N = ||Y_1||^2 > 0
is NOT zero (the ansatz's telescoping predicted 0), and |beta| < N always.
The ansatz's (1,1) block reappears exactly at the F_+-twisted pairing
[f, F_+ g], which is NOT the space's inner product: block
[[-beta, -N], [-N, -beta]], eigenvalues -beta -+ N, signature (1,1). That is
the corrected home of the mirror-pole mechanism.

Run:  python -m experiments.spectral.e1w_burnol_bilinear [--quick]
Full mode ~3-5 min (writes/checks e1w_burnol_bilinear.npz); quick ~1 min.
"""

import os
import sys

import mpmath as mp
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
NPZ_PATH = os.path.join(HERE, "e1w_burnol_bilinear.npz")

# ----------------------------------------------------------------------
# quadrature
# ----------------------------------------------------------------------

def gauss_legendre(n):
    """Nodes/weights on [-1,1], Newton iteration at working precision."""
    xs, ws = [], []
    with mp.workdps(mp.mp.dps + 10):
        tol = mp.mpf(10) ** (-(mp.mp.dps - 4))
        for i in range(1, n + 1):
            x = mp.cos(mp.pi * (i - mp.mpf(1) / 4) / (n + mp.mpf(1) / 2))
            for _ in range(100):
                p0, p1 = mp.mpf(1), x
                for k in range(2, n + 1):
                    p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
                dp = n * (x * p1 - p0) / (x * x - 1)
                dx = p1 / dp
                x -= dx
                if abs(dx) < tol:
                    break
            p0, p1 = mp.mpf(1), x
            for k in range(2, n + 1):
                p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
            dp = n * (x * p1 - p0) / (x * x - 1)
            xs.append(+x)
            ws.append(2 / ((1 - x * x) * dp * dp))
    return xs, ws


def clenshaw_curtis(n):
    """n+1 Chebyshev-Lobatto nodes/weights on [-1,1] (Trefethen clencurt).

    n must be even. Returns nodes x_j = cos(j pi / n), j = 0..n.
    """
    assert n % 2 == 0
    xs = [mp.cos(mp.pi * j / n) for j in range(n + 1)]
    ws = []
    for j in range(n + 1):
        if j == 0 or j == n:
            ws.append(mp.mpf(1) / (n * n - 1))
            continue
        th = mp.pi * j / n
        s = mp.mpf(0)
        for k in range(1, n // 2):
            s += mp.cos(2 * k * th) / (4 * k * k - 1)
        w = (mp.mpf(2) / n) * (1 - 2 * s - mp.cos(n * th) / (n * n - 1))
        ws.append(w)
    return xs, ws


# ----------------------------------------------------------------------
# bases on (0, a): values at quadrature nodes
# ----------------------------------------------------------------------

def legendre_basis(K, a, ts):
    """Orthonormal mean-zero basis phi_k, k=1..K: sqrt((2k+1)/a) P_k(2t/a-1)."""
    ys = [2 * t / a - 1 for t in ts]
    n = len(ys)
    P0 = [mp.mpf(1)] * n
    P1 = list(ys)
    rows = []
    for k in range(1, K + 1):
        if k == 1:
            Pk = P1
        else:
            Pk = [((2 * k - 1) * ys[i] * P1[i] - (k - 1) * P0[i]) / k for i in range(n)]
            P0, P1 = P1, Pk
        c = mp.sqrt(mp.mpf(2 * k + 1) / a)
        rows.append([c * v for v in Pk])
    return rows


def chebyshev_basis(K, a, ts):
    """Mean-zero basis psi_k = T_k(2t/a-1) - m_k, m_k = mean of T_k on [-1,1]."""
    ys = [2 * t / a - 1 for t in ts]
    n = len(ys)
    T0 = [mp.mpf(1)] * n
    T1 = list(ys)
    rows = []
    for k in range(1, K + 1):
        if k == 1:
            Tk = T1
        else:
            Tk = [2 * ys[i] * T1[i] - T0[i] for i in range(n)]
            T0, T1 = T1, Tk
        mk = mp.mpf(0) if k % 2 == 1 else mp.mpf(1) / (1 - k * k)
        rows.append([v - mk for v in Tk])
    return rows


# ----------------------------------------------------------------------
# the extension block B
# ----------------------------------------------------------------------

def build_config(a, K, n, route):
    """Build quadrature-level data for one (a, K) at basis size K.

    Returns dict with S (basis Gram), C (cross Gram (b_j, F_+ b_k)),
    cvec (int b_k(t) sin(2 pi a t)/(pi t) dt), plus node data for the
    residue reading.
    """
    if route == "A":
        xs, ws = gauss_legendre(n)
        ts = [a * (x + 1) / 2 for x in xs]
        tws = [a * w / 2 for w in ws]
        basis = legendre_basis(K, a, ts)
    else:
        xs, ws = clenshaw_curtis(n)
        ts = [a * (x + 1) / 2 for x in xs]
        tws = [a * w / 2 for w in ws]
        basis = chebyshev_basis(K, a, ts)
    m = len(ts)
    # S_jk = (b_j, b_k) on (0,a)
    S = mp.matrix(K, K)
    for j in range(K):
        for k in range(j, K):
            s = mp.mpf(0)
            for i in range(m):
                s += basis[j][i] * basis[k][i] * tws[i]
            S[j, k] = s
            S[k, j] = s
    # cosine kernel and C_jk = 2 sum w_i w_l b_j(i) cos(2 pi t_i t_l) b_k(l)
    Cos = [[mp.cos(2 * mp.pi * ts[i] * ts[l]) for l in range(m)] for i in range(m)]
    A = [[basis[k][i] * tws[i] for i in range(m)] for k in range(K)]
    Mt = []
    for k in range(K):
        row = []
        for l in range(m):
            s = mp.mpf(0)
            for i in range(m):
                s += A[k][i] * Cos[i][l]
            row.append(s)
        Mt.append(row)
    C = mp.matrix(K, K)
    for j in range(K):
        for k in range(K):
            s = mp.mpf(0)
            for l in range(m):
                s += Mt[j][l] * A[k][l]
            C[j, k] = 2 * s
    # svals(t) = (F_+ 1_(0,a))(t) = sin(2 pi a t)/(pi t), with t=0 limit 2a
    svals = [(2 * a if t == 0 else mp.sin(2 * mp.pi * a * t) / (mp.pi * t)) for t in ts]
    cvec = [sum(basis[k][i] * svals[i] * tws[i] for i in range(m)) for k in range(K)]
    return {"a": a, "K": K, "route": route, "ts": ts, "tws": tws,
            "basis": basis, "S": S, "C": C, "cvec": cvec}


def sub_config(cfg, K):
    """Restrict a built config to the first K basis functions (nested bases)."""
    K0 = cfg["K"]
    assert K <= K0
    S = mp.matrix(K, K)
    C = mp.matrix(K, K)
    for j in range(K):
        for k in range(K):
            S[j, k] = cfg["S"][j, k]
            C[j, k] = cfg["C"][j, k]
    return {"a": cfg["a"], "K": K, "route": cfg["route"], "ts": cfg["ts"],
            "tws": cfg["tws"], "basis": cfg["basis"][:K], "S": S, "C": C,
            "cvec": cfg["cvec"][:K]}


def solve_block(cfg):
    """Solve for the extension block B and the projection coefficients.

    G = [[S, C], [C, S]] (C is symmetric since F_+ is self-adjoint and real);
    b1 = [0; -c/a] (u_1 is orthogonal to the mean-zero block),
    b0 = [c/a; 0]  (u_0 is orthogonal to the F_+ block).
    B_ij = (u_i, u_j) - b_i^T G^{-1} b_j  (Schur complement = Gram of the
    projections Y_i = u_i - P_V u_i).
    """
    a, K = cfg["a"], cfg["K"]
    S, C, cvec = cfg["S"], cfg["C"], cfg["cvec"]
    G = mp.matrix(2 * K, 2 * K)
    for j in range(K):
        for k in range(K):
            G[j, k] = S[j, k]
            G[K + j, K + k] = S[j, k]
            G[j, K + k] = C[j, k]
            G[K + j, k] = C[k, j]
    b1 = mp.matrix(2 * K, 1)
    b0 = mp.matrix(2 * K, 1)
    for k in range(K):
        b1[K + k] = -cvec[k] / a
        b0[k] = cvec[k] / a
    x1 = mp.lu_solve(G, b1)
    x0 = mp.lu_solve(G, b0)
    u0u1 = -mp.si(2 * mp.pi * a * a) / (mp.pi * a * a)
    B11 = 1 / a - sum(b1[i] * x1[i] for i in range(2 * K))
    B00 = 1 / a - sum(b0[i] * x0[i] for i in range(2 * K))
    B01 = u0u1 - sum(b0[i] * x1[i] for i in range(2 * K))
    B10 = u0u1 - sum(b1[i] * x0[i] for i in range(2 * K))
    swap_err = mp.mpf(0)
    for k in range(K):
        swap_err = max(swap_err, abs(x0[k] + x1[K + k]), abs(x0[K + k] + x1[k]))
    return {"N": B11, "B00": B00, "beta": B01, "B10": B10,
            "x1": x1, "x0": x0, "swap_err": swap_err}


def residue_reading(cfg, sol, tstars):
    """Read B off the constants: Res_1 M(f) = -f(0+) for f in L_a.

    Y_1(t) = u_1(t) - sum alpha_k b_k(t) - sum beta_k (F_+ b_k)(t) evaluated
    pointwise at t* in (0,a); N_res = -mean Y_1(t*), beta_res = -mean Y_0(t*).
    The spread of Y over the t* certifies (im)perfection of the constancy.
    """
    a, K = cfg["a"], cfg["K"]
    ts, tws, basis = cfg["ts"], cfg["tws"], cfg["basis"]
    m = len(ts)
    x1, x0 = sol["x1"], sol["x0"]

    def bk_at(k, t):
        # value of basis function k at arbitrary t via its definition
        y = 2 * t / a - 1
        if cfg["route"] == "A":
            c = mp.sqrt(mp.mpf(2 * (k + 1) + 1) / a)
            return c * mp.legendre(k + 1, y)
        deg = k + 1
        mk = mp.mpf(0) if deg % 2 == 1 else mp.mpf(1) / (1 - deg * deg)
        return mp.chebyt(deg, y) - mk

    def fplus_bk_at(k, t):
        s = mp.mpf(0)
        for l in range(m):
            s += tws[l] * mp.cos(2 * mp.pi * t * ts[l]) * basis[k][l]
        return 2 * s

    vals1, vals0 = [], []
    for t in tstars:
        u1 = -1 / a
        u0 = mp.sin(2 * mp.pi * a * t) / (mp.pi * t) / a
        y1 = u1 - sum(x1[k] * bk_at(k, t) for k in range(K)) \
                - sum(x1[K + k] * fplus_bk_at(k, t) for k in range(K))
        y0 = u0 - sum(x0[k] * bk_at(k, t) for k in range(K)) \
                - sum(x0[K + k] * fplus_bk_at(k, t) for k in range(K))
        vals1.append(y1)
        vals0.append(y0)
    N_res = -sum(vals1) / len(vals1)
    beta_res = -sum(vals0) / len(vals0)
    spread = max(max(vals1) - min(vals1), max(vals0) - min(vals0))
    return N_res, beta_res, spread


# ----------------------------------------------------------------------
# convention anchors (pin the implementation to Burnol's paper)
# ----------------------------------------------------------------------

def M_gaussian(s):
    """Completed right Mellin transform of f(t) = exp(-pi t^2) (closed form)."""
    # fhat(s) = int_0^inf exp(-pi t^2) t^-s dt = pi^((s-1)/2) Gamma((1-s)/2) / 2
    return mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.pi ** ((s - 1) / 2) \
        * mp.gamma((1 - s) / 2) / 2


def chi_gamma(s):
    """Burnol eq (7): chi(s) = pi^(s-1/2) Gamma((1-s)/2) / Gamma(s/2)."""
    return mp.pi ** (s - mp.mpf(1) / 2) * mp.gamma((1 - s) / 2) / mp.gamma(s / 2)


def check_conventions():
    """Returns worst errors of the three closed-form convention anchors."""
    # (i) FE of the Gaussian: M(F_+ f) (s) = M(f)(1-s) with F_+ f = f
    e1 = mp.mpf(0)
    for s in [mp.mpc("0.3", "1.7"), mp.mpc("0.9", "-2.2"), mp.mpc("2.4", "0.5")]:
        e1 = max(e1, abs(M_gaussian(s) - M_gaussian(1 - s)))
    # (ii) chi(s) = zeta(s)/zeta(1-s), eqs (7)-(8)
    e2 = mp.mpf(0)
    for s in [mp.mpc("0.3", "1.1"), mp.mpc("0.7", "3.0"),
              mp.mpc("1.6", "-0.8"), mp.mpc("-0.4", "2.3")]:
        e2 = max(e2, abs(chi_gamma(s) - mp.zeta(s) / mp.zeta(1 - s)) / abs(chi_gamma(s)))
    # (iii) Mellin of F_+ 1_(0,a): (1/pi) Gamma(-s) sin(-pi s/2) (2 pi a)^s
    #       must equal chi(s) a^s / s   (the FE applied to the indicator)
    e3 = mp.mpf(0)
    a = mp.mpf("0.7")
    for s in [mp.mpc("0.4", "1.3"), mp.mpc("0.6", "-2.1"), mp.mpc("0.25", "0.9")]:
        lhs = mp.gamma(-s) * mp.sin(-mp.pi * s / 2) * (2 * mp.pi * a) ** s / mp.pi
        rhs = chi_gamma(s) * a ** s / s
        e3 = max(e3, abs(lhs - rhs) / abs(rhs))
    return e1, e2, e3


def check_copoisson(T=240.0, tstar=mp.mpf("0.3")):
    """End-to-end check of Burnol eq (9) at our conventions.

    g(t) = (t - 0.6)^2 (1.5 - t)^2 on [0.6, 1.5]; h(t) = co-Poisson sum
    sum_{m>=1} g(m/t)/t - ghat(0). Then F_+(h)(t*) must equal
    sum_{n>=1} g(t*/n)/n - ghat(1) = -ghat(1) for t* < 0.6.
    Returns (relative error, tail bound estimate).
    """
    ag, Ag = mp.mpf("0.6"), mp.mpf("1.5")

    def g(x):
        if x <= ag or x >= Ag:
            return mp.mpf(0)
        return (x - ag) ** 2 * (Ag - x) ** 2

    ghat0 = mp.quad(g, [ag, Ag])
    ghat1 = mp.quad(lambda x: g(x) / x, [ag, Ag])

    def h(t):
        lo = int(mp.ceil(ag * t))
        hi = int(mp.floor(Ag * t))
        s = mp.mpf(0)
        for mm in range(max(lo, 1), hi + 1):
            s += g(mm / t)
        return s / t - ghat0

    # composite Gauss on [0, T], panels of length 0.5, 12-point rule
    xs, ws = gauss_legendre(12)
    npan = int(T / 0.5)
    total = mp.mpf(0)
    for p in range(npan):
        lo = mp.mpf(p) / 2
        for x, w in zip(xs, ws):
            t = lo + (x + 1) / 4
            total += (w / 4) * h(t) * mp.cos(2 * mp.pi * t * tstar)
    fplus_h = 2 * total
    target = -ghat1
    relerr = abs(fplus_h - target) / abs(target)
    tail = abs(h(mp.mpf(T))) * T  # crude scale of the neglected tail mass
    return relerr, tail


# ----------------------------------------------------------------------
# main
# ----------------------------------------------------------------------

def main(quick=False):
    results = []

    def check(name, ok, detail=""):
        results.append((name, bool(ok)))
        print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")

    if quick:
        mp.mp.dps = 34
        avals = ["0.5", "1.0", "1.25"]
        Ks = [8, 12, 16]
        nA, nB = 64, 56
    else:
        mp.mp.dps = 44
        avals = ["0.3", "0.5", "0.8", "1.0", "1.25", "1.6"]
        Ks = [4, 8, 16, 20, 24]
        nA, nB = 96, 88
    Kmax = Ks[-1]

    # -- conventions --------------------------------------------------
    e1, e2, e3 = check_conventions()
    check("T01 gaussian FE (Note 2 + Thm 2.1 conventions)", e1 < mp.mpf("1e-30"),
          f"worst {mp.nstr(e1, 3)}")
    check("T02 chi: Gamma form == zeta(s)/zeta(1-s) (eqs (7)-(8))",
          e2 < mp.mpf("1e-30"), f"worst rel {mp.nstr(e2, 3)}")
    check("T03 indicator Mellin FE identity", e3 < mp.mpf("1e-30"),
          f"worst rel {mp.nstr(e3, 3)}")

    # -- quadrature self-tests ---------------------------------------
    a_t = mp.mpf("0.8")
    xs, ws = gauss_legendre(24)
    got = sum(w * (a_t * (x + 1) / 2) ** 7 for x, w in zip(xs, ws)) * a_t / 2
    check("T04 Gauss-Legendre exactness (t^7 on (0,a))",
          abs(got - a_t ** 8 / 8) < mp.mpf("1e-32"), f"err {mp.nstr(abs(got - a_t**8/8), 3)}")
    xs, ws = clenshaw_curtis(40)
    got = sum(w * (a_t * (x + 1) / 2) ** 7 for x, w in zip(xs, ws)) * a_t / 2
    gotc = sum(w * mp.cos(2 * mp.pi * (a_t * (x + 1) / 2) * mp.mpf("0.56"))
               for x, w in zip(xs, ws)) * a_t / 2
    ref = mp.sin(2 * mp.pi * a_t * mp.mpf("0.56")) / (2 * mp.pi * mp.mpf("0.56"))
    okcc = abs(got - a_t ** 8 / 8) < mp.mpf("1e-30") and abs(gotc - ref) < mp.mpf("1e-30")
    check("T05 Clenshaw-Curtis exactness (t^7 and cosine)", okcc,
          f"errs {mp.nstr(abs(got - a_t**8/8), 3)}, {mp.nstr(abs(gotc - ref), 3)}")

    # -- build grid ----------------------------------------------------
    grid = {}       # (a_str, route) -> full config at Kmax
    sols = {}       # (a_str, route, K) -> solution
    worst_meanzero = mp.mpf(0)
    worst_csym = mp.mpf(0)
    for a_str in avals:
        a = mp.mpf(a_str)
        for route, n in [("A", nA), ("B", nB)]:
            cfg = build_config(a, Kmax, n, route)
            grid[(a_str, route)] = cfg
            mz = max(abs(sum(cfg["basis"][k][i] * cfg["tws"][i]
                             for i in range(len(cfg["ts"])))) for k in range(Kmax))
            worst_meanzero = max(worst_meanzero, mz)
            cs = max(abs(cfg["C"][j, k] - cfg["C"][k, j])
                     for j in range(Kmax) for k in range(Kmax))
            worst_csym = max(worst_csym, cs)
            for K in Ks:
                sols[(a_str, route, K)] = solve_block(sub_config(cfg, K) if K < Kmax else cfg)
    check("T06 basis mean-zero (both routes, all a)", worst_meanzero < mp.mpf("1e-30"),
          f"worst {mp.nstr(worst_meanzero, 3)}")
    check("T07 C symmetry = F_+ self-adjointness (both routes)",
          worst_csym < mp.mpf("1e-28"), f"worst {mp.nstr(worst_csym, 3)}")

    # -- structure and convergence -------------------------------------
    ok_mono, ok_contr = True, True
    worst_struct = mp.mpf(0)
    for a_str in avals:
        seq = [sols[(a_str, "A", K)]["N"] for K in Ks]
        for i in range(len(seq) - 1):
            if seq[i + 1] > seq[i] + mp.mpf("1e-30"):
                ok_mono = False
        for i in range(len(seq) - 2):
            d1 = abs(seq[i + 1] - seq[i])
            d2 = abs(seq[i + 2] - seq[i + 1])
            if d2 > d1 + mp.mpf("1e-30"):
                ok_contr = False
        for route in ("A", "B"):
            s = sols[(a_str, route, Kmax)]
            worst_struct = max(worst_struct, abs(s["B00"] - s["N"]),
                               abs(s["beta"] - s["B10"]), s["swap_err"])
    check("T08 K-monotonicity of N (projection nesting)", ok_mono)
    check("T09 K-contraction of N increments", ok_contr)
    check("T10 structural identities B00=B11, B01=B10, coefficient swap",
          worst_struct < mp.mpf("1e-25"), f"worst {mp.nstr(worst_struct, 3)}")

    # -- the verdict: signature per a ----------------------------------
    print()
    print("  a      N=||Y_1||^2      beta=(Y_0,Y_1)    eig_min=N+beta   eig_max=N-beta  |beta|/N")
    n_neg_total = 0
    for a_str in avals:
        s = sols[(a_str, "A", Kmax)]
        N, beta = s["N"], s["beta"]
        emin, emax = N + beta, N - beta
        n_neg = (1 if emin < 0 else 0) + (1 if emax < 0 else 0)
        n_neg_total += n_neg
        print(f"  {a_str:5s}  {mp.nstr(N, 12):16s}  {mp.nstr(beta, 12):16s}  "
              f"{mp.nstr(emin, 8):15s}  {mp.nstr(emax, 8):15s}  {mp.nstr(abs(beta)/N, 8)}")
        # margin: the K-increment must be well below the small eigenvalue,
        # else the sign is not resolved by this discretization
        dK = abs(sols[(a_str, "A", Ks[-1])]["N"] - sols[(a_str, "A", Ks[-2])]["N"])
        resolved = dK < emin * mp.mpf("0.01")
        check(f"T11 signature(a={a_str}) = (2,0), margin resolved",
              n_neg == 0 and emin > 0 and resolved,
              f"eig_min {mp.nstr(emin, 5)}, K-increment {mp.nstr(dK, 3)}")
    print()

    # -- route agreement ----------------------------------------------
    worst_AB = mp.mpf(0)
    for a_str in avals:
        sA = sols[(a_str, "A", Kmax)]
        sB = sols[(a_str, "B", Kmax)]
        scale = max(sA["N"], mp.mpf("1e-12"))
        worst_AB = max(worst_AB,
                       abs(sA["N"] - sB["N"]) / scale,
                       abs(sA["beta"] - sB["beta"]) / scale)
    tol_AB = mp.mpf("1e-20")
    check("T12 route A vs route B agreement (matched K)", worst_AB < tol_AB,
          f"worst rel {mp.nstr(worst_AB, 3)} (tol {mp.nstr(tol_AB, 2)})")

    # -- residue reading ----------------------------------------------
    worst_res = mp.mpf(0)
    worst_spread = mp.mpf(0)
    for a_str in avals:
        a = mp.mpf(a_str)
        cfg = grid[(a_str, "A")]
        s = sols[(a_str, "A", Kmax)]
        tstars = [a * mp.mpf(f) for f in ("0.15", "0.35", "0.55", "0.75", "0.95")]
        N_res, beta_res, spread = residue_reading(cfg, s, tstars)
        scale = max(s["N"], mp.mpf("1e-12"))
        worst_res = max(worst_res, abs(N_res - s["N"]) / scale,
                        abs(beta_res - s["beta"]) / scale)
        worst_spread = max(worst_spread, spread / scale)
    tol_res = mp.mpf("1e-4") if quick else mp.mpf("1e-3")
    check("T13 residue reading (constants) vs Gram reading", worst_res < tol_res,
          f"worst rel {mp.nstr(worst_res, 3)}, constancy spread {mp.nstr(worst_spread, 3)}")

    # -- n-stability ----------------------------------------------------
    a = mp.mpf("1.0")
    cfg_lo = build_config(a, Ks[-2], int(nA * 3 / 4), "A")
    s_lo = solve_block(cfg_lo)
    s_hi = sols[("1.0", "A", Ks[-2])]
    dn = abs(s_lo["N"] - s_hi["N"]) + abs(s_lo["beta"] - s_hi["beta"])
    check("T14 quadrature n-stability (a=1.0)", dn < mp.mpf("1e-25"),
          f"delta {mp.nstr(dn, 3)}")

    # -- ansatz discriminators -----------------------------------------
    min_ratio = min(sols[(a_str, "A", Kmax)]["N"] / abs(sols[(a_str, "A", Kmax)]["beta"])
                    for a_str in avals)
    min_diag = min(sols[(a_str, "A", Kmax)]["N"] for a_str in avals)
    check("T15 CORRECTED: literal diagonal N > 0 (ansatz predicted 0), N > |beta|",
          min_diag > 0 and min_ratio > 1,
          f"min N {mp.nstr(min_diag, 5)}, min N/|beta| {mp.nstr(min_ratio, 8)}")

    ok_tw = True
    for a_str in avals:
        s = sols[(a_str, "A", Kmax)]
        N, beta = s["N"], s["beta"]
        tw_eigs = sorted([-beta - N, -beta + N])
        if not (tw_eigs[0] < 0 < tw_eigs[1]):
            ok_tw = False
    check("T16 twisted pairing [f, F_+ g] block has signature (1,1) at every a",
          ok_tw, "the corrected home of the ansatz's mirror-pole (1,1)")

    # -- small-a closed-form anchor (full only) ------------------------
    if not quick:
        s = sols[("0.3", "A", Kmax)]
        a = mp.mpf("0.3")
        u0u1 = -mp.si(2 * mp.pi * a * a) / (mp.pi * a * a)
        ok_anchor = abs(s["N"] - 1 / a) < mp.mpf("0.01") and \
            abs(s["beta"] - u0u1) < mp.mpf("0.01")
        check("T17 small-a anchor: N -> 1/a, beta -> (u_0,u_1) = -Si(2 pi a^2)/(pi a^2)",
              ok_anchor,
              f"N-1/a {mp.nstr(s['N'] - 1/a, 3)}, beta-(u0,u1) {mp.nstr(s['beta'] - u0u1, 3)}")

    # -- co-Poisson end-to-end (full only) ------------------------------
    if not quick:
        with mp.workdps(20):
            relerr, tail = check_copoisson()
        check("T18 co-Poisson formula (9) end-to-end: F_+(cP(g)) = -ghat(1) on (0,a)",
              relerr < mp.mpf("1e-3"),
              f"rel err {mp.nstr(relerr, 3)} (truncation-limited; tail scale {mp.nstr(tail, 2)})")

    # -- npz record ------------------------------------------------------
    if not quick:
        rec = {}
        for a_str in avals:
            for route in ("A", "B"):
                for K in Ks:
                    s = sols[(a_str, route, K)]
                    rec[f"N_{a_str}_{route}_{K}"] = float(s["N"])
                    rec[f"beta_{a_str}_{route}_{K}"] = float(s["beta"])
        rec["avals"] = np.array([float(mp.mpf(x)) for x in avals])
        rec["Ks"] = np.array(Ks)
        if os.path.exists(NPZ_PATH):
            old = np.load(NPZ_PATH)
            worst = 0.0
            for key in rec:
                if key in ("avals", "Ks"):
                    continue
                if key in old.files:
                    d = abs(rec[key] - float(old[key]))
                    scale = max(abs(float(old[key])), 1e-12)
                    worst = max(worst, d / scale)
            check("T19 npz record consistency (regeneration matches tracked record)",
                  worst < 1e-10, f"worst rel {worst:.3e}")
        else:
            np.savez(NPZ_PATH, **rec)
            check("T19 npz record written", os.path.exists(NPZ_PATH), NPZ_PATH)

    n_pass = sum(1 for _, ok in results if ok)
    print(f"\n{n_pass}/{len(results)} passed")
    return n_pass == len(results)


if __name__ == "__main__":
    quick = "--quick" in sys.argv
    ok = main(quick=quick)
    sys.exit(0 if ok else 1)
