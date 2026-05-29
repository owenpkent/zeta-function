"""Experiment 2N (overnight T3): independent theta/Green's-function cross-check of 2I.

*** STATUS: BLOCKED (gate failed) -- this attempt does NOT validate. ***
The difference lambda_2I - lambda_theta is NOT constant across points (spread ~0.24),
so this theta normalization does not reproduce 2I's z-dependence. Preserved for a
future resumption that fixes the elliptic-log branch / theta-argument / period
normalization. See experiments/orchestrator_sessions/_NIGHT_FINDINGS.md. 2I itself
remains independently validated against h_hat; this was only a confirmatory check.


2I computed the archimedean Neron local height lambda_inf(P) via the Tate
telescoping series. This recomputes its z-DEPENDENCE by a completely independent
route -- the elliptic logarithm z_P plus the Jacobi theta_1 Green's function on
E(C) = C/Lambda -- and checks the two agree.

## Method

Convert the curve to the Weierstrass p-form y^2 = 4x^3 - g2 x - g3 (g2 = c4/12,
g3 = c6/216) with X = x + b2/12. For a point P with X_P >= e1 (largest real root,
identity real component), the real elliptic logarithm is
    z_P = int_{X_P}^{inf} dt / sqrt(4 t^3 - g2 t - g3),
and the real period omega1 = 2 int_{e1}^{inf} dt/sqrt(...). Put u = z_P / (2 omega1)
... (normalized so the lattice is Z + Z tau, tau from period_tau). The
quasi-periodic-invariant Green's building block is
    lambda_theta(P) = -log|theta_1(pi u | q)| + pi (Im u)^2 / Im tau,   q = e^{i pi tau},
which captures the z-dependence of the archimedean local height up to an additive
constant C(tau) (the metric / discriminant normalization, the same for all P).

## Gate (honest)

We do NOT require the absolute value to match 2I (that needs C(tau) derived). We
require the WEAKER, still-meaningful statement: lambda_2I(P) - lambda_theta(P) is
CONSTANT across several points P (the generators and their small multiples) for a
given curve, to < 1e-3. A constant difference means the theta route independently
reproduces the z-dependence of 2I's lambda_inf, with only the per-curve constant
unfixed. PASS = difference constant per curve. If it is NOT constant, the formula /
elliptic-log is wrong -> BLOCK with findings (do not fudge). If a clean constant is
found, we additionally report it and whether it matches a simple expression in
eta(tau) (a bonus, not required for the gate).
"""

from __future__ import annotations

from pathlib import Path

import mpmath as mp
import numpy as np

from experiments.arithmetic_geometric.e2h_arithmetic_hodge_index import add, double, O, _x_parts
from experiments.arithmetic_geometric.e2i_archimedean_local_height import lambda_inf, b_invariants
from experiments.arithmetic_geometric.e2l_faltings_petersson import c_invariants, period_tau
from sympy import Integer

CURVES = {
    "37a1": (0, 0, 1, -1, 0),
    "389a1": (0, 1, 1, -2, 0),
    "5077a1": (0, 0, 1, -7, 6),
}
GENS = {
    "37a1": [(0, 0)],
    "389a1": [(-1, 1), (0, 0)],
    "5077a1": [(-2, 3), (-1, 3), (0, 2)],
}


def weierstrass_g2g3(a, prec):
    mp.mp.dps = prec
    c4, c6, _ = c_invariants(tuple(Integer(c) for c in a))
    g2 = mp.mpf(int(c4)) / 12
    g3 = mp.mpf(int(c6)) / 216
    return g2, g3


def real_period_and_roots(g2, g3, prec):
    mp.mp.dps = prec
    roots = mp.polyroots([4, 0, -g2, -g3], maxsteps=200, extraprec=4 * prec)
    # sort real roots descending; for 3 real roots e1>e2>e3
    rr = sorted([r for r in roots], key=lambda z: mp.re(z), reverse=True)
    e1, e2, e3 = rr[0], rr[1], rr[2]
    # real period of y^2=4x^3-g2x-g3 : 2*omega1 = 2*pi/AGM(sqrt(e1-e3), sqrt(e1-e2)) (3 real roots)
    return e1, e2, e3


def elliptic_log_real(Xp, g2, g3, prec):
    """z_P = int_{Xp}^inf dt / sqrt(4 t^3 - g2 t - g3), real (identity component)."""
    mp.mp.dps = prec
    f = lambda t: 1 / mp.sqrt(4 * t ** 3 - g2 * t - g3)
    return mp.quad(f, [Xp, mp.inf])


def run(prec=40, out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)
    mp.mp.dps = prec

    print("[2N] Independent theta/Green's-function cross-check of 2I's lambda_inf.")
    print("     Gate: lambda_2I(P) - lambda_theta(P) constant across P (per curve).\n")

    results = {}
    all_pass = True
    for name, a in CURVES.items():
        av = tuple(Integer(c) for c in a)
        b2 = b_invariants(av)[0]
        g2, g3 = weierstrass_g2g3(a, prec)
        e1, e2, e3 = real_period_and_roots(g2, g3, prec)
        tau = period_tau(av, prec=prec)
        q = mp.e ** (1j * mp.pi * tau)
        # real period (3 real roots): 2*omega1 = 2*pi/AGM(sqrt(e1-e3), sqrt(e1-e2))
        two_omega1 = 2 * mp.pi / mp.agm(mp.sqrt(e1 - e3), mp.sqrt(e1 - e2))

        diffs = []
        rows = []
        # test points: each generator and 2x, 3x
        test = []
        for g in GENS[name]:
            P = (Integer(g[0]), Integer(g[1]))
            test += [P, double(P, av), add(double(P, av), P, av)]
        for P in test:
            if P == O:
                continue
            x = mp.mpf(int(P[0].p)) / int(P[0].q)
            Xp = x + mp.mpf(int(b2)) / 12
            if Xp <= e1 + mp.mpf("1e-9"):
                continue  # not on the identity real component via this real integral
            zP = elliptic_log_real(Xp, g2, g3, prec)
            u = zP / two_omega1
            th = mp.jtheta(1, mp.pi * u, q)
            lam_theta = -mp.log(abs(th)) + mp.pi * (mp.im(u)) ** 2 / mp.im(tau)
            lam_2I = lambda_inf(P, av, prec=prec, n_terms=60)
            d = float(lam_2I - lam_theta)
            diffs.append(d)
            rows.append((P, float(lam_2I), float(lam_theta), d))
        if len(diffs) >= 2:
            spread = max(diffs) - min(diffs)
            const_ok = spread < 1e-3
        else:
            spread = float("nan"); const_ok = False
        all_pass = all_pass and const_ok
        results[name] = dict(diffs=diffs, spread=spread, const_ok=const_ok, rows=rows,
                             n_pts=len(diffs))
        print(f"  --- {name} ---  ({len(diffs)} identity-component test points)")
        for (P, l2, lt, d) in rows:
            print(f"      P=({int(P[0]):>3},{int(P[1]):>3})  lambda_2I={l2:+.5f}  "
                  f"lambda_theta={lt:+.5f}  diff={d:+.6f}")
        print(f"      difference spread = {spread:.2e}   CONSTANT (z-dependence matches 2I): "
              f"{'PASS' if const_ok else 'FAIL'}\n")

    print(f"[2N] z-dependence cross-check (diff constant per curve) for ALL curves: {all_pass}")
    print(f"     {'-> commit (independent confirmation of 2I z-dependence)' if all_pass else '-> BLOCK: write findings, do not claim'}")
    np.savez_compressed(out_dir / "e2n_greens_function_crosscheck.npz",
                        **{f"{n}_diffs": np.array(r['diffs']) for n, r in results.items()},
                        all_pass=all_pass)
    print(f"[2N] Saved {out_dir / 'e2n_greens_function_crosscheck.npz'}")
    return results, all_pass


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(); p.add_argument("--prec", type=int, default=40)
    run(prec=p.parse_args().prec)
