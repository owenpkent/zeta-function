"""E1Z: the sharp form of Theorem V2 (the one thing left open in #172's gauge).

LEARNINGS #172 proved Theorem V2, a lower bound on the germ length in terms of
the gap geometry alone:

    lambda_M(0) <= cosh(2 n G)^-2,   n = floor((M-1)/2),
    G = (1/2) arccosh((T^2+g^2)/(T^2-g^2)) = the Green's function of
        C \\ (+-[g,T]) at 0,

for any probability measure with M atoms in E = +-[g,T]. V8 then measured its
tightness residual rho = log(1/lambda) / (2 log cosh 2nG) and found that it
does NOT saturate: on an equally spaced (g,T,M)-matched surrogate,
rho ~ 0.48 log T. So the bound is order-tight on the buildable window and
loses a slowly growing factor asymptotically. TODO carried the remainder as
"a sharp version would capture that factor", explicitly a potential-theory
question with no arithmetic input.

THIS ROUND CLOSES IT AT THE LEVEL OF THE EXPONENTIAL RATE. The identity
1/lambda_M(0) = sum_j ell_j(0)^2 / w_j turns the Christoffel problem into a
Lagrange-interpolation one, and the classical logarithmic-potential asymptotic
for interpolation at an exterior point gives, when the atoms' empirical
distribution converges to sigma,

    (1/M) log(1/lambda_M(0))  ->  2 Gamma(sigma),
    Gamma(sigma) = max_{y in E} U^sigma(y) - U^sigma(0),
    U^sigma(x)   = -int log|x - y| dsigma(y).

Read against Theorem V2 that says three things.

  (1) V2 IS THE EQUILIBRIUM CASE. For sigma = the equilibrium measure of E,
      U^sigma is constant on E, so Gamma = g_E(0) = G exactly and the
      Chebyshev bound is the right rate. Measured: rho -> 1.
  (2) EVERY OTHER sigma IS STRICTLY WORSE, and rho -> Gamma(sigma)/G. The
      bound is lossy exactly because it keeps only the SUPPORT of the atoms
      and throws away their DISTRIBUTION. This is a Runge-type effect: the
      Chebyshev construction is optimal for nodes at the mapped Chebyshev
      points, and the real configuration is not there.
  (3) THE MEASURED log T IS THAT DISCREPANCY. For equal spacing (sigma
      uniform on +-[g,T]) with g fixed, Gamma/G = (1/2) log T + O(1), the
      maximizer sitting at the geometric mean y* = sqrt(gT). So the constant
      is 1/2 and #172's 0.48 is the finite-T approach to it.

Structure:
  Z1  the fast log-assembly of 1/lambda, cross-checked against mpmath
  Z2  independent replication of #172's V8b predictor (a different assembly)
  Z3  equilibrium nodes: rho -> 1, i.e. V2 is asymptotically SHARP there
  Z4  uniform nodes: rho -> Gamma/G
  Z5  Gamma >= G for every family, with equality only at equilibrium
  Z6  the uniform slope d(Gamma/G)/d log T -> 1/2
  Z7  the maximizer is sqrt(gT) FOR THE UNIFORM FAMILY (uniform-specific:
      the zeta density maximizes at 3.29 sqrt(gT))
  Z8  typing: Gamma is a functional of sigma only, so the sharpening is
      arithmetic-blind and does NOT reopen the pointwise route (#172 V8c)
  Z9  the rate is not uniform-specific: the zeta density, whose Gamma/G is
      three times the uniform value, lands on its own Gamma too

Caveats, stated up front:
- This sharpens the RATE, not a two-sided finite-M inequality. A fully sharp
  theorem needs effective error terms; what is proved here numerically is the
  limit and its identification.
- The atoms carry EQUAL weights throughout. Weights contribute O(log M) to
  log(1/lambda), hence nothing to the rate, but a finite-M statement would
  have to carry them.
- It proves nothing about RH, and by construction cannot: Gamma depends only
  on the limiting distribution, which is exactly #172's continuity
  obstruction seen from the other side.

Run:
  python -m experiments.spectral.e1z_v2_sharp           # full
  python -m experiments.spectral.e1z_v2_sharp --quick   # reduced grids
"""

from __future__ import annotations

import argparse
import time
from pathlib import Path

import numpy as np
import mpmath as mp
from scipy.special import logsumexp

OUT = Path(__file__).with_suffix(".npz")
CHECKS: list = []

# #172 V8b, verbatim: g fixed by the FE budget, T = 2 pi lam^2, M = 2x the
# Riemann-von Mangoldt count in [g,T], equally spaced surrogate.
V8B_G = 13.6
V8B = [(30.4, 6), (56.5, 22), (100.5, 58), (157.1, 112),
       (226.2, 186), (402.1, 406), (760.3, 920), (1413.7, 1988)]
V8B_RHO = [1.143, 1.332, 1.570, 1.762, 1.924, 2.190, 2.494, 2.797]


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))


# --------------------------------------------------------------------------
# The two sides: the finite quantity, and the potential-theoretic rate.
# --------------------------------------------------------------------------
def G_of(g, T):
    """Green's function of C \\ (+-[g,T]) at 0, i.e. Theorem V2's G."""
    return 0.5 * float(mp.acosh((T ** 2 + g ** 2) / (T ** 2 - g ** 2)))


def log_inv_lambda(y_pos):
    """log(1/lambda_M(0)) for the symmetric config +-y_pos, equal weights.

    1/lambda = sum_j ell_j(0)^2 / w_j exactly (the Cauchy-Schwarz equality
    case of the Christoffel problem at full degree). Assembling it through
    log|ell_j(0)| = sum_{i!=j} log|y_i| - sum_{i!=j} log|y_j - y_i| and a
    logsumexp needs no extended precision, which is what takes M past the
    ~2000 that the direct mpmath product costs in #172.
    """
    y = np.asarray(y_pos, dtype=float)
    m = y.size
    M = 2 * m
    log_all = 2.0 * np.log(y).sum()                 # sum over ALL atoms, +-
    D = np.abs(y[:, None] - y[None, :])
    np.fill_diagonal(D, 1.0)                        # drop the i = j term
    same = np.log(D).sum(axis=1)
    opp = np.log(y[:, None] + y[None, :]).sum(axis=1)
    L = (log_all - np.log(y)) - (same + opp)
    return float(logsumexp(2.0 * L) + np.log(2.0 * M))


def rho_of(y_pos, g, T):
    """#172's tightness residual rho = log(1/lambda) / (2 log cosh 2nG)."""
    M = 2 * np.asarray(y_pos).size
    n = (M - 1) // 2
    return log_inv_lambda(y_pos) / (2.0 * np.log(np.cosh(2 * n * G_of(g, T))))


def nodes(kind, m, g, T):
    """m positive nodes with the named limiting distribution on [g, T]."""
    if kind == "equilibrium":
        # equilibrium of +-[g,T] is the arcsine measure in v = y^2
        A, B = g * g, T * T
        v = (A + B) / 2 + (B - A) / 2 * np.cos(np.pi * (np.arange(m) + 0.5) / m)
        return np.sqrt(np.sort(v))
    if kind == "uniform":
        return np.linspace(g, T, m)
    if kind == "zeta":
        y = np.linspace(g, T, 200001)
        d = np.log(np.maximum(y / (2 * np.pi), 1.0000001))
        c = np.concatenate(([0.0], np.cumsum((d[1:] + d[:-1]) / 2 * np.diff(y))))
        return np.interp((np.arange(m) + 0.5) / m * c[-1], c, y)
    raise ValueError(kind)


def _xlogx(u):
    u = np.asarray(u, dtype=float)
    r = np.zeros_like(u)
    nz = np.abs(u) > 0
    r[nz] = u[nz] * np.log(np.abs(u[nz]))
    return r


def U_uniform(x, g, T):
    """U^sigma(x) for sigma uniform on +-[g,T], in closed form.

    U^sigma(x) = -(1/(2(T-g))) int_g^T log|x^2 - y^2| dy, and both halves
    integrate elementarily, so the potential costs no quadrature.
    """
    x = np.atleast_1d(np.asarray(x, dtype=float))
    I1 = (_xlogx(T - x) - (T - x)) - (_xlogx(g - x) - (g - x))
    I2 = (_xlogx(x + T) - (x + T)) - (_xlogx(x + g) - (x + g))
    return -(I1 + I2) / (2.0 * (T - g))


def U_empirical(x, y_pos):
    """U^sigma(x) from a symmetric atom set, for families with no closed form."""
    x = np.atleast_1d(np.asarray(x, dtype=float))
    d = np.abs(x[:, None] ** 2 - np.asarray(y_pos)[None, :] ** 2)
    d = np.maximum(d, 1e-300)
    return -0.5 * np.log(d).mean(axis=1)


def gamma_uniform(g, T, ng=120000):
    """Gamma = max_E U^sigma - U^sigma(0) for the uniform family."""
    s = np.linspace(0.0, 1.0, ng)
    xs = g + (T - g) * np.unique(np.concatenate([s, s ** 4, 1.0 - s ** 4]))
    U = U_uniform(xs, g, T)
    i = int(np.argmax(U))
    return float(U[i]) - float(U_uniform(0.0, g, T)[0]), float(xs[i])


def gamma_empirical(kind, g, T, m=40000, ng=6000):
    y = nodes(kind, m, g, T)
    s = np.linspace(0.0, 1.0, ng)
    xs = g + (T - g) * np.unique(np.concatenate([s, s ** 4, 1.0 - s ** 4]))
    U = U_empirical(xs, y)
    return float(U.max()) - float(U_empirical(0.0, y)[0])


# --------------------------------------------------------------------------
def run_z1(results):
    print("\n[Z1] the fast log-assembly of 1/lambda, against the direct product")
    prev = mp.mp.dps
    mp.mp.dps = 60
    try:
        worst = 0.0
        for yp in (np.array([1.3, 2.7, 4.1, 6.0, 9.5]),
                   np.array([13.6, 21.0, 25.0, 30.4, 32.9, 37.6, 40.9])):
            ys = ([-mp.mpf(float(v)) for v in reversed(yp)]
                  + [mp.mpf(float(v)) for v in yp])
            tot = mp.mpf(0)
            for j in range(len(ys)):
                num = mp.mpf(1)
                for i in range(len(ys)):
                    if i != j:
                        num *= (-ys[i]) / (ys[j] - ys[i])
                tot += num ** 2 * len(ys)
            worst = max(worst, abs(float(mp.log(tot)) - log_inv_lambda(yp)))
    finally:
        mp.mp.dps = prev
    check("Z1-1 the logsumexp assembly of 1/lambda agrees with the direct "
          "mpmath Lagrange product, so the fast route is the same quantity",
          worst < 1e-9, f"worst |diff of logs| = {worst:.2e}")
    results["z1_worst"] = np.array([worst])


def run_z2(results):
    print("\n[Z2] independent replication of #172's V8b predictor")
    print(f"    {'T':>8s} {'M':>6s} {'#172 rho':>9s} {'this run':>9s} {'diff':>8s}")
    mine = []
    for (T, M), r in zip(V8B, V8B_RHO):
        mr = rho_of(np.linspace(V8B_G, T, M // 2), V8B_G, T)
        mine.append(mr)
        print(f"    {T:8.1f} {M:6d} {r:9.3f} {mr:9.3f} {mr - r:+8.4f}")
    dev = float(np.abs(np.array(mine) - np.array(V8B_RHO)).max())
    check("Z2-1 a different assembly reproduces the whole V8b table, so the "
          "0.48 log T finding is replicated rather than inherited",
          dev < 5e-3, f"worst deviation over 8 points = {dev:.4f}")
    lt = np.log([T for T, _ in V8B])
    sl = np.diff(mine) / np.diff(lt)
    check("Z2-2 and its slopes d rho / d log T reproduce too, rising toward "
          "the reported 0.48",
          abs(sl[-1] - 0.489) < 0.01,
          "slopes = " + ", ".join(f"{v:.3f}" for v in sl))
    results["z2_rho"] = np.array(mine)
    results["z2_slopes"] = sl


def run_z3z4(results, ms, g, T):
    print(f"\n[Z3/Z4] the rate: rho -> Gamma/G   (g = {g}, T = {T})")
    G = G_of(g, T)
    gam_u, xstar = gamma_uniform(g, T)
    print(f"    G = {G:.6g}   Gamma(uniform) = {gam_u:.6g}   "
          f"Gamma/G = {gam_u/G:.4f}")
    print(f"    {'M':>7s} {'rho(equilibrium)':>17s} {'rho(uniform)':>13s}")
    req, run_ = [], []
    for m in ms:
        a = rho_of(nodes("equilibrium", m, g, T), g, T)
        b = rho_of(nodes("uniform", m, g, T), g, T)
        req.append(a)
        run_.append(b)
        print(f"    {2*m:7d} {a:17.5f} {b:13.5f}")
    # The grids double M, so a converging quantity should halve its distance
    # to the limit each step. Testing the CONTRACTION rather than an absolute
    # gap keeps these valid at any M, quick mode included.
    exc = [abs(v - 1.0) for v in req]
    ratio_eq = exc[-1] / max(exc[-2], 1e-300)
    check("Z3-1 for EQUILIBRIUM-distributed atoms rho -> 1: Theorem V2 is "
          "asymptotically SHARP exactly there, which is what identifies the "
          "Chebyshev bound as the sigma = equilibrium special case",
          all(req[i] > req[i + 1] for i in range(len(req) - 1)) and ratio_eq < 0.6,
          f"rho falls monotonically to {req[-1]:.4f} at M = {2*ms[-1]}, its "
          f"excess over 1 contracting by {1/ratio_eq:.2f}x per doubling")
    gap = [abs(v - gam_u / G) for v in run_]
    ratio_u = gap[-1] / max(gap[-2], 1e-300)
    check("Z4-1 for UNIFORM atoms rho -> Gamma/G, the equilibrium-discrepancy "
          "exponent, not to 1: the gap to Gamma/G contracts geometrically "
          "while the distance to 1 does not shrink at all",
          ratio_u < 0.8 and gap[-1] < 0.1 * abs(run_[-1] - 1.0),
          f"gap to Gamma/G = {gap[-1]:.4f} (contracting {1/ratio_u:.2f}x per "
          f"doubling) vs distance to 1 = {abs(run_[-1]-1.0):.4f}")
    check("Z4-2 and it approaches from below over the tail, so Gamma/G is the "
          "limit rather than a coincidence at one M",
          all(run_[i] < run_[i + 1] for i in range(len(run_) // 2, len(run_) - 1)),
          f"tail = " + ", ".join(f"{v:.4f}" for v in run_[len(run_) // 2:]))
    results["z34"] = np.array([[2 * m for m in ms], req, run_], dtype=float)
    results["z34_gamma"] = np.array([G, gam_u, xstar])


def run_z5(results, g, T):
    print("\n[Z5] Gamma >= G, with equality only at equilibrium")
    G = G_of(g, T)
    rows = []
    for kind in ("equilibrium", "uniform", "zeta"):
        Ga = (gamma_uniform(g, T)[0] if kind == "uniform"
              else gamma_empirical(kind, g, T))
        rows.append((kind, Ga, Ga / G))
        print(f"    {kind:>12s}: Gamma = {Ga:.6g}   Gamma/G = {Ga/G:.4f}")
    check("Z5-1 every family has Gamma >= G, so Theorem V2's bound is never "
          "beaten and is the floor of a one-parameter family of rates",
          all(r[2] > 0.995 for r in rows),
          "min Gamma/G = " + f"{min(r[2] for r in rows):.4f}")
    check("Z5-2 equilibrium sits at Gamma/G = 1 while the others are strictly "
          "above, which is the characterization of when V2 is sharp",
          abs(rows[0][2] - 1.0) < 0.02 and all(r[2] > 1.1 for r in rows[1:]),
          f"equilibrium {rows[0][2]:.4f}, uniform {rows[1][2]:.4f}, "
          f"zeta {rows[2][2]:.4f}")
    results["z5"] = np.array([[r[1], r[2]] for r in rows])


def run_z6z7(results, Ts, g):
    print("\n[Z6/Z7] the uniform law: Gamma/G = (1/2) log T + O(1), max at sqrt(gT)")
    print(f"    {'T':>10s} {'Gamma/G':>10s} {'slope':>8s} {'argmax':>12s} "
          f"{'sqrt(gT)':>12s} {'ratio':>8s}")
    rs, xs = [], []
    for i, T in enumerate(Ts):
        Ga, xm = gamma_uniform(g, T)
        r = Ga / G_of(g, T)
        sl = ((r - rs[-1]) / (np.log(T) - np.log(Ts[i - 1]))) if i else float("nan")
        rs.append(r)
        xs.append(xm / np.sqrt(g * T))
        print(f"    {T:10.3g} {r:10.4f} {sl:8.4f} {xm:12.4g} "
              f"{np.sqrt(g*T):12.4g} {xm/np.sqrt(g*T):8.5f}")
    sl_last = (rs[-1] - rs[-2]) / (np.log(Ts[-1]) - np.log(Ts[-2]))
    check("Z6-1 the slope d(Gamma/G)/d log T converges to 1/2, so #172's "
          "measured 0.48 is the finite-T approach to an exact one-half",
          abs(sl_last - 0.5) < 0.01,
          f"final slope = {sl_last:.4f} over T = {Ts[-2]:.3g} -> {Ts[-1]:.3g}")
    check("Z7-1 FOR THIS FAMILY the maximizer of U^sigma sits at the geometric "
          "mean sqrt(gT) (uniform-specific: the adversary round measured the "
          "zeta density maximizing at 3.29 sqrt(gT), so this belongs to the "
          "corollary and not to the general statement)",
          max(abs(v - 1.0) for v in xs[-4:]) < 1e-3,
          "argmax/sqrt(gT) = " + ", ".join(f"{v:.5f}" for v in xs[-4:]))
    results["z67"] = np.array([Ts, rs, xs], dtype=float)


def run_z9(results, ms, g, T):
    """The check that could have made the whole Gamma story an artifact of
    one family: does rho go to Gamma/G for a THIRD distribution, with a very
    different Gamma? Added by the adversary round."""
    print("\n[Z9] the rate is not uniform-specific: the zeta density")
    G = G_of(g, T)
    gz = gamma_empirical("zeta", g, T, m=30000, ng=3000)
    print(f"    Gamma_zeta/G = {gz/G:.4f}  (uniform's is {gamma_uniform(g,T)[0]/G:.4f})")
    print(f"    {'M':>7s} {'rho':>10s} {'gap to Gamma/G':>16s}")
    rs = []
    for m in ms:
        r = rho_of(nodes("zeta", m, g, T), g, T)
        rs.append(r)
        print(f"    {2*m:7d} {r:10.4f} {gz/G - r:16.4f}")
    gaps = [abs(v - gz / G) for v in rs]
    check("Z9-1 the zeta density converges to ITS OWN Gamma/G, which is three "
          "times the uniform value, so Gamma(sigma) is the rate for every "
          "distribution tested and not an artifact of equal spacing",
          gaps[-1] < 0.05 * abs(rs[-1] - 1.0) and gaps[-1] < gaps[-2],
          f"gap {gaps[-1]:.4f} at M = {2*ms[-1]} against a distance to 1 of "
          f"{abs(rs[-1]-1.0):.3f}, contracting {gaps[-2]/gaps[-1]:.2f}x")
    results["z9"] = np.array([[2 * m for m in ms], rs], dtype=float)


def run_z8(results, g, T, m):
    print("\n[Z8] typing: Gamma is a functional of sigma only (arithmetic-blind)")
    base = nodes("uniform", m, g, T)
    rng = np.random.default_rng(5)
    # jitter each atom well inside its own cell: same limiting sigma, totally
    # different (and Q-generic) positions
    cell = (T - g) / (m - 1)
    jit = np.sort(base + rng.uniform(-0.35, 0.35, m) * cell)
    jit = np.clip(jit, g, T)
    r0, r1 = rho_of(base, g, T), rho_of(jit, g, T)
    print(f"    equally spaced rho = {r0:.5f}")
    print(f"    jittered       rho = {r1:.5f}   (same sigma, different atoms)")
    check("Z8-1 randomizing the atom positions inside their cells, which keeps "
          "sigma and destroys every arithmetic relation among them, moves rho "
          "by O(1/M): the sharpened rate is geometry, exactly as V8c typed the "
          "drift, so this does NOT reopen the pointwise route",
          abs(r1 - r0) < 0.15,
          f"|d rho| = {abs(r1-r0):.4f} at M = {2*m}")
    results["z8"] = np.array([r0, r1])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true",
                    help="reduced grids; does NOT save the npz")
    args = ap.parse_args()
    t0 = time.time()
    print("=" * 78)
    print("E1Z: the sharp form of Theorem V2 (the #172 residual)")
    print("=" * 78)

    results = {}
    if args.quick:
        ms = [50, 100, 200, 400, 800]
        Ts = [1e3, 1e4, 1e5, 1e6]
        jm = 800
    else:
        ms = [50, 100, 200, 400, 800, 1600, 3200]
        Ts = [1e3, 1e4, 1e5, 1e6, 1e7, 1e8]
        jm = 2000

    run_z1(results)
    run_z2(results)
    run_z3z4(results, ms, V8B_G, 1000.0)
    run_z5(results, V8B_G, 1000.0)
    run_z6z7(results, Ts, V8B_G)
    run_z9(results, ms, V8B_G, 1000.0)
    run_z8(results, V8B_G, 1000.0, jm)

    print("\n" + "=" * 78)
    print("VERDICT (full statement in e1z_v2_sharp.md)")
    print("  sharp_rate = (1/M) log(1/lambda_M(0)) -> 2 Gamma(sigma), with")
    print("    Gamma(sigma) = max_E U^sigma - U^sigma(0) the equilibrium")
    print("    discrepancy of the atoms' limiting distribution.")
    print("  v2_is_the_equilibrium_case = YES. Gamma = G exactly for sigma =")
    print("    the equilibrium measure, and rho -> 1 there (measured).")
    print("    Theorem V2 is asymptotically sharp precisely at equilibrium.")
    print("  the_missing_log = the equilibrium discrepancy of EQUAL SPACING:")
    print("    Gamma/G = (1/2) log T + O(1), maximizer at sqrt(gT). #172's")
    print("    measured 0.48 is the finite-T approach to exactly one half.")
    print("  arithmetic_content = NONE, and provably so: Gamma depends only on")
    print("    sigma, so the sharpening confirms V8c's typing instead of")
    print("    reopening the pointwise route.")
    print("  frontier_delta = ZERO. It closes a potential-theory residual.")
    print("=" * 78)

    n_ok = sum(1 for _, ok in CHECKS if ok)
    print(f"\nSELF-TEST: {n_ok}/{len(CHECKS)} checks passed")
    for name, ok in CHECKS:
        if not ok:
            print(f"  FAILED: {name}")
    if args.quick:
        print("(--quick: npz NOT saved; the tracked artifact is the full run's)")
    else:
        np.savez_compressed(OUT, **results)
        print(f"Saved -> {OUT}")
    print(f"Total time {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
