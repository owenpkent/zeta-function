"""Experiment 2I: the genuine archimedean Neron local height lambda_inf(P), and how
the archimedean place carries the arithmetic Hodge index regulator.

Follows 2H. 2H exhibited the Faltings-Hriljac arithmetic Hodge index over Spec(Z)
(height pairing on E(Q) positive definite, validated against LMFDB regulators), but
its naive coordinate split sent the archimedean part to ~0 -- the WRONG
decomposition. The genuine archimedean Neron local height is a transcendental
quantity; this experiment computes it.

## The algorithm (self-derived Tate telescoping, validated against h_hat)

Rather than transcribe a formula, we derive the archimedean local height from the
duplication formula and the canonical recursion, and then VALIDATE it numerically
against the already-LMFDB-validated canonical height h_hat. (Cohen, "A Course in
Computational Algebraic Number Theory", Algorithm 7.5.7, and Silverman ATAEC ch. VI
are the authoritative references for cross-checking.)

With b-invariants b2,b4,b6,b8 and t = 1/x, the x-coordinate of 2P is
    x(2P) = (x^4 - b4 x^2 - 2 b6 x - b8) / (4 x^3 + b2 x^2 + 2 b4 x + b6)
          = z(t) / w(t) * x ...   [in t: 1/x(2P) = w(t)/z(t)],
where
    z(t) = 1 - b4 t^2 - 2 b6 t^3 - b8 t^4     (= x^{-4} (x^4 - b4 x^2 - 2 b6 x - b8))
    w(t) = 4 t + b2 t^2 + 2 b4 t^3 + b6 t^4   (= x^{-4} (4 x^3 + b2 x^2 + 2 b4 x + b6)).

Bare ansatz (telescoping): mu(P) = (1/2) log|x| + (1/2) sum_{n>=0} 4^{-(n+1)} log|z(t_n)|,
with t_0 = 1/x, t_{n+1} = w(t_n) / z(t_n). One checks
mu(P) - (1/4) mu(2P) = (1/4) log|2y + a1 x + a3|, whose sum over ALL places is 0 by
the product formula, so sum_v mu_v is a canonical quadratic function.

EMPIRICAL NORMALIZATION (validated, not assumed): with the bare ansatz, the run
found recon = sum_v mu_v = h_hat / 2 EXACTLY -- the documented factor-of-2 between
Silverman's 1988 paper and his books / the LMFDB regulator convention. We therefore
use the h_hat = sum_v lambda_v normalization with lambda = 2 mu:
    lambda_inf(P) = log|x| + sum_{n>=0} 4^{-(n+1)} log|z(t_n)|,
    walk-back:  lambda_inf(Q) = (1/4) lambda_inf(2Q) + (1/2) log|2y(Q) + a1 x(Q) + a3|.
The series wants |x| >= 1; for small/zero x (e.g. 37a's (0,0)) we double up to
|x| >= 1, evaluate the series, and walk back with the recursion above.

## The finite side (exact, elementary)

In the same h_hat normalization, for p of good reduction the Neron local height is
lambda_p(P) = max{0, -v_p(x(P))} log p; since x has square denominator d^2, the sum
over good p is sum_p lambda_p(P) = log(den x(P)) = 2 log d. (The single bad prime of
each prime-conductor curve is huge and divides no denominator here.)

## Validation and the payoff (CONFIRMED)

For each point we check lambda_inf(P) + log(den x(P)) = h_hat(P). It holds to ~1e-5
(limited only by the canonical-height limit precision, not the local height). The
payoff: for the INTEGRAL generators (den = 1) the finite local heights vanish, so
lambda_inf(P) = h_hat(P) and the positive-definite arithmetic Hodge index regulator
is carried ENTIRELY by the archimedean place (arch trace share = 100%, archimedean
pairing matrix itself positive definite). For non-integral points (e.g. 389a's 2P,
x-denominator 9) the finite places enter and lambda_inf + sum_p lambda_p = h_hat
exactly. This is "how the archimedean place enters the signature," done correctly:
for these curves it IS the signature.

Outputs:
  - e2i_archimedean_local_height.npz
  - e2i_archimedean_local_height.png
  - stdout: per-point validation + archimedean regulator share
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np
from sympy import Rational, Integer

from experiments.arithmetic_geometric.e2h_arithmetic_hodge_index import (
    O, add, double, neg, canonical_heights, _x_parts, CURVES,
)


def b_invariants(a):
    a1, a2, a3, a4, a6 = [int(c) for c in a]
    b2 = a1 * a1 + 4 * a2
    b4 = 2 * a4 + a1 * a3
    b6 = a3 * a3 + 4 * a6
    b8 = a1 * a1 * a6 + 4 * a2 * a6 - a1 * a3 * a4 + a2 * a3 * a3 - a4 * a4
    return b2, b4, b6, b8


def _z(t, b4, b6, b8):
    return 1 - b4 * t ** 2 - 2 * b6 * t ** 3 - b8 * t ** 4


def _w(t, b2, b4, b6):
    return 4 * t + b2 * t ** 2 + 2 * b4 * t ** 3 + b6 * t ** 4


def lambda_inf_series(x_mpf, b2, b4, b6, b8, n_terms=60):
    """lambda_inf for a point with |x| >= 1, via the Tate telescoping series.

    Normalization: the bare telescoping (with 1/2 factors) sums over all places to
    h_hat/2 -- the documented factor-of-2 between Silverman's 1988 paper and his
    books / the LMFDB regulator convention (validated empirically: recon = h_hat/2
    exactly before this scaling). We use the h_hat = sum_v lambda_v normalization,
    so the series carries an overall factor 2: lambda_inf = log|x| + sum 4^{-(n+1)} log|z|.
    """
    b2 = mp.mpf(b2); b4 = mp.mpf(b4); b6 = mp.mpf(b6); b8 = mp.mpf(b8)
    t = 1 / x_mpf
    total = mp.log(abs(x_mpf))
    quarter_pow = mp.mpf(1)
    for n in range(n_terms):
        quarter_pow /= 4          # = 4^{-(n+1)}
        z = _z(t, b4, b6, b8)
        if z == 0:
            break
        total += quarter_pow * mp.log(abs(z))
        w = _w(t, b2, b4, b6)
        t = w / z
    return total


def lambda_inf(P, a, prec=40, n_terms=60, max_double=10):
    """Archimedean Neron local height of P, handling small |x| by doubling up to
    |x|>=1 and walking back via the canonical recursion."""
    mp.mp.dps = prec
    a1, a2, a3, a4, a6 = [mp.mpf(int(c)) for c in a]
    b2, b4, b6, b8 = b_invariants(a)

    # Build the orbit P, 2P, 4P, ... until |x| >= 1 (or cap).
    orbit = [P]
    Q = P
    for _ in range(max_double):
        xnum, xden = _x_parts(Q)
        xval = mp.mpf(xnum) / mp.mpf(xden)
        if abs(xval) >= 1:
            break
        Q = double(Q, a)
        orbit.append(Q)
    # series at the top of the orbit
    xnum, xden = _x_parts(orbit[-1])
    xtop = mp.mpf(xnum) / mp.mpf(xden)
    lam = lambda_inf_series(xtop, b2, b4, b6, b8, n_terms=n_terms)
    # walk back (h_hat normalization): lambda(Q) = (1/4) lambda(2Q) + (1/2) log|2y + a1 x + a3|
    for k in range(len(orbit) - 2, -1, -1):
        Qk = orbit[k]
        xk = mp.mpf(Qk[0].p) / mp.mpf(Qk[0].q)
        yk = mp.mpf(Qk[1].p) / mp.mpf(Qk[1].q)
        psi = 2 * yk + a1 * xk + a3
        lam = mp.mpf("0.25") * lam + mp.mpf("0.5") * mp.log(abs(psi))
    return lam


def finite_height(P):
    """sum_p lambda_p(P) over good primes, in the h_hat = sum_v lambda_v
    normalization. For a Weierstrass model den(x) = d^2, and the Neron finite
    local heights sum to log(den x(P)) = 2 log d in this normalization."""
    _, xden = _x_parts(P)
    return mp.log(mp.mpf(xden)) if xden > 1 else mp.mpf(0)


def run(prec=40, n_terms=60, out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)
    mp.mp.dps = prec

    print("[2I] Archimedean Neron local height lambda_inf(P), self-derived Tate series,")
    print("     validated against the LMFDB-matched canonical height h_hat.\n")

    results = []
    for curve in CURVES:
        a = tuple(Integer(c) for c in curve["a"])
        pts = curve["points"]
        print(f"  --- {curve['label']} ---")
        # validation across generators AND a few multiples (which carry denominators)
        test_pts = []
        for P in pts:
            test_pts.append(("P", P))
            test_pts.append(("2P", double(P, a)))
        rows = []
        for tag, P in test_pts:
            if P == O:
                continue
            hh, _, _ = canonical_heights(P, a, n_iter=7)
            li = float(lambda_inf(P, a, prec=prec, n_terms=n_terms))
            fin = float(finite_height(P))
            recon = li + fin
            resid = recon - hh
            xnum, xden = _x_parts(P)
            rows.append((tag, hh, li, fin, resid, xden))
            print(f"      {tag:>3}: h_hat={hh:+.6f}  lambda_inf={li:+.6f}  "
                  f"fin(1/2 log den)={fin:+.6f}  recon={recon:+.6f}  "
                  f"resid={resid:+.2e}")
        # archimedean regulator share on the generators
        r = len(pts)
        li_diag = [float(lambda_inf(P, a, prec=prec, n_terms=n_terms)) for P in pts]
        hh_diag = [canonical_heights(P, a, n_iter=7)[0] for P in pts]
        # full + archimedean pairing matrices (off-diagonals via P+Q)
        M_full = np.zeros((r, r)); M_arch = np.zeros((r, r))
        for i in range(r):
            M_full[i, i] = hh_diag[i]; M_arch[i, i] = li_diag[i]
            for j in range(i + 1, r):
                PpQ = add(pts[i], pts[j], a)
                hpq = canonical_heights(PpQ, a, n_iter=7)[0]
                lpq = float(lambda_inf(PpQ, a, prec=prec, n_terms=n_terms))
                M_full[i, j] = M_full[j, i] = 0.5 * (hpq - hh_diag[i] - hh_diag[j])
                M_arch[i, j] = M_arch[j, i] = 0.5 * (lpq - li_diag[i] - li_diag[j])
        reg_full = float(np.linalg.det(M_full))
        reg_arch = float(np.linalg.det(M_arch))
        eig_arch = np.linalg.eigvalsh(M_arch)
        arch_share = float(np.trace(M_arch) / np.trace(M_full))
        max_resid = max(abs(rr[4]) for rr in rows)
        results.append(dict(label=curve["label"], rank=r, rows=rows,
                            M_full=M_full, M_arch=M_arch, eig_arch=eig_arch,
                            reg_full=reg_full, reg_arch=reg_arch,
                            arch_share=arch_share, max_resid=max_resid))
        print(f"      => archimedean regulator det = {reg_arch:.6e} "
              f"(full {reg_full:.6e}); arch trace share = {arch_share:.1%}; "
              f"arch pairing pos-def: {bool((eig_arch > -1e-7).all())}")
        print(f"      => max validation residual |lambda_inf + fin - h_hat| = {max_resid:.2e}")
        print()

    all_valid = all(r["max_resid"] < 1e-4 for r in results)
    print(f"[2I] Self-derived lambda_inf validated against h_hat (resid < 1e-4) for "
          f"ALL points: {all_valid}")
    if all_valid:
        print(f"[2I] The archimedean Neron local height is correct. Unlike the naive")
        print(f"     coordinate split (2H, ~0% archimedean), the genuine lambda_inf")
        print(f"     carries a definite, validated share of the positive-definite")
        print(f"     arithmetic-Hodge-index regulator. This is how the archimedean")
        print(f"     place enters the signature -- the transcendental piece a")
        print(f"     Spec(Z) x Spec(Z) Hodge index would have to globalize.")

    _save_and_plot(results, out_dir)
    return results, all_valid


def _save_and_plot(results, out_dir):
    save = {"n_curves": len(results)}
    for i, r in enumerate(results):
        save[f"c{i}_rank"] = r["rank"]; save[f"c{i}_M_full"] = r["M_full"]
        save[f"c{i}_M_arch"] = r["M_arch"]; save[f"c{i}_arch_share"] = r["arch_share"]
        save[f"c{i}_max_resid"] = r["max_resid"]
    np.savez_compressed(out_dir / "e2i_archimedean_local_height.npz", **save)

    fig, axs = plt.subplots(1, 2, figsize=(13, 5))
    ax = axs[0]
    resids = [r["max_resid"] for r in results]
    ax.bar([f"rank {r['rank']}" for r in results], np.maximum(resids, 1e-18), color="tab:purple")
    ax.axhline(1e-4, color="r", ls="--", label="validation tol 1e-4")
    ax.set_yscale("log"); ax.set_ylabel(r"max $|\lambda_\infty + \mathrm{fin} - \hat h|$")
    ax.set_title("Self-derived archimedean local height:\nvalidation against LMFDB-matched h_hat")
    ax.legend(); ax.grid(alpha=0.3, axis="y")

    ax = axs[1]
    shares = [r["arch_share"] for r in results]
    ax.bar([f"rank {r['rank']}" for r in results], shares, color="tab:orange")
    ax.axhline(1.0, color="k", lw=0.5)
    ax.set_ylabel("archimedean share of regulator trace")
    ax.set_title("How the archimedean place enters the signature\n(genuine Neron lambda_inf, not the naive split)")
    ax.grid(alpha=0.3, axis="y")
    plt.tight_layout()
    plt.savefig(out_dir / "e2i_archimedean_local_height.png", dpi=140)
    plt.close()
    print(f"\n[2I] Saved {out_dir / 'e2i_archimedean_local_height.png'}")
    print(f"[2I] Saved {out_dir / 'e2i_archimedean_local_height.npz'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prec", type=int, default=40)
    parser.add_argument("--n-terms", type=int, default=60)
    args = parser.parse_args()
    run(prec=args.prec, n_terms=args.n_terms)
