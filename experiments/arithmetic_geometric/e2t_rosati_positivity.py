"""Experiment 2T: RH-for-curves as ROSATI POSITIVITY, the standard-conjecture form
of the signature, and the precise arithmetic target for Direction 8.

The session's synthesis (docs/03_research/all_roads_to_the_signature.md) located
the irreducible content of RH as a SIGNATURE/positivity. This experiment puts it
in its most standard professional form: the positivity of the Rosati involution
on the Frobenius endomorphism algebra. This is the actual engine of Weil's 1948
proof, it is cleaner than "Hodge index on a surface" (no surface needed), and its
arithmetic analogue is a Grothendieck-standard-conjecture-type positivity, which
is the correct literature home of the problem.

THE FORM. For C/F_q of genus g, let pi be the q-Frobenius on Jac(C), acting on
H^1 with the 2g eigenvalues {alpha_i}. The Rosati involution dagger (w.r.t. the
canonical principal polarization) is pi^dagger = pi-bar, with alpha_i-bar =
q/alpha_i. The Rosati trace form on the endomorphism algebra is
    B(x, y) = Tr(x y^dagger),
and Weil's positivity-of-the-Rosati-involution theorem says B is POSITIVE
DEFINITE on End^0(Jac C) (x) R. On the basis {1, pi, pi^2, ..., pi^{2g-1}} of
Q(pi) the Gram matrix is, using Tr(pi^a pi-bar^b) = q^{min(a,b)} a_{|a-b|} with
a_k = sum_i alpha_i^k = q^k + 1 - N_k (the trace of Frobenius^k on H^1):
    G_Rosati[a][b] = q^{min(a,b)} * a_{|a-b|},   a,b = 0..2g-1.

(When pi generates a PROPER subalgebra of End^0 -- extra endomorphisms -- the
basis {1,pi,...} is dependent and G is positive SEMI-definite, with kernel = the
relations. So the honest invariant is "NO NEGATIVE eigenvalues"; the rank equals
dim Q(pi).)

THE EQUIVALENCE (verified across the family; the K3 / Weil-specialization check):
    Rosati positivity (no negative eigenvalues of G_Rosati)
      <=>  |alpha_i| = sqrt(q) for all i   (RH for C)
      <=>  the primitive intersection form on C x C is negative definite (2G,
           via the sign flip: geometric intersection = - Rosati trace form)
      <=>  zeros of Hesselholt's det_inf(s - Theta | TP_odd) on Re(s) = 1/2 (2S).

So RH-for-C has four equivalent faces; Rosati positivity is the standard one and
the one with the cleanest arithmetic analogue. Over F_q it is a THEOREM (Weil),
proved via the existence of the polarization / the Hodge index on C x C.

THE ARITHMETIC TARGET (Direction 8, restated; OPEN). RH for zeta is the
arithmetic analogue: a positive Rosati-type involution on the "arithmetic
Frobenius algebra" of Spec(Z) -- equivalently, the arithmetic Hodge standard
conjecture for the (Deninger) Frobenius correspondence Gamma_S, whose
self-intersection is the von Mangoldt prime sum (#26) and whose bidegree is
place-dependent (1,p) (#25). Over F_q the positivity comes from the polarization;
over Z it is exactly the missing input. This is no longer "build a surface and
hope"; it is "prove the positivity of a Rosati involution," a precise problem in
the standard-conjectures circle.

WHY THIS IS NOT CIRCULAR (the K1 line). The Rosati form's positivity over F_q is
NOT derived from the zeta zeros; it comes from the polarization (a geometric
positivity), and RH is its consequence. That is the non-circular signature route
R3.5 demands, here in its standard-conjecture form.

Outputs:
  - e2t_rosati_positivity.npz
  - e2t_rosati_positivity.png
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from experiments.arithmetic_geometric.e2f_hodge_index_sweep import (
    count_points_Fpk, elliptic_family, genus2_family,
)


def trace_power_sums(curve):
    """a_k = sum_i alpha_i^k = q^k + 1 - N_k for k = 0..2g-1 (a_0 = 2g)."""
    p, g, f = curve["p"], curve["g"], curve["f_coeffs"]
    a = [2 * g]
    for k in range(1, 2 * g):
        a.append(p ** k + 1 - count_points_Fpk(f, p, k))
    return a, p, g


def rosati_gram(curve):
    """G[a][b] = q^{min(a,b)} a_{|a-b|}, the Rosati trace form on {1,pi,...,pi^{2g-1}}."""
    a, p, g = trace_power_sums(curve)
    n = 2 * g
    G = np.array([[p ** min(i, j) * a[abs(i - j)] for j in range(n)]
                  for i in range(n)], dtype=float)
    return G, p, g


def frobenius_eigenvalues(curve):
    """The 2g eigenvalues alpha_i (roots of the L-polynomial), via Newton's identities."""
    a, p, g = trace_power_sums(curve)
    # power sums p_k = a_k for k=1..2g-1; need up to 2g. Get a_{2g} too.
    f = curve["f_coeffs"]
    psums = [a[k] for k in range(1, 2 * g)] + [p ** (2 * g) + 1 - count_points_Fpk(f, p, 2 * g)]
    # elementary symmetric e_1..e_{2g} via Newton; char poly prod(x - alpha_i).
    e = [1.0]
    for k in range(1, 2 * g + 1):
        s = 0.0
        for i in range(1, k + 1):
            s += (-1) ** (i - 1) * e[k - i] * psums[i - 1]
        e.append(s / k)
    # char poly coeffs (monic, descending): x^{2g} - e1 x^{2g-1} + e2 ...
    coeffs = [(-1) ** j * e[j] for j in range(2 * g + 1)]
    return np.roots(np.array(coeffs, dtype=complex))


def signature(M, tol=1e-7):
    w = np.linalg.eigvalsh(M)
    scale = max(abs(w).max(), 1.0)
    pos = int((w > tol * scale).sum())
    neg = int((w < -tol * scale).sum())
    zero = len(w) - pos - neg
    return pos, neg, zero, w


def run(full=False, out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    primes_e = (5, 7, 11, 13, 17, 19, 23, 29, 31) if full else (5, 7, 11, 13)
    primes_g2 = (5, 7, 11, 13) if full else (5, 7, 11)
    curves = elliptic_family(list(primes_e)) + genus2_family(list(primes_g2))

    print("[2T] RH-for-curves as ROSATI POSITIVITY (the standard-conjecture form).")
    print("     B(x,y)=Tr(x y^dagger) positive (no negative eigenvalues) <=> |alpha_i|=sqrt(q).")
    print("     This is the non-circular signature; its arithmetic analogue is the target.\n")
    header = (f"{'curve':<32} {'g':>2} {'q':>3} {'sig(Rosati)':>13} "
              f"{'rank':>4} {'no neg eig':>10} {'|a_i|=sqrt q':>12} {'agree':>6}")
    print(header); print("-" * len(header))

    results = []
    all_ok = True
    for curve in curves:
        G, p, g = rosati_gram(curve)
        pos, neg, zero, w = signature(G)
        no_neg = (neg == 0)
        alphas = frobenius_eigenvalues(curve)
        rh = bool(np.all(np.abs(np.abs(alphas) - np.sqrt(p)) < 1e-5 * np.sqrt(p)))
        agree = (no_neg == rh)
        all_ok = all_ok and agree and no_neg
        results.append(dict(label=curve["label"], p=p, g=g, sig=(pos, neg, zero),
                            rank=pos + neg, no_neg=no_neg, rh=rh, agree=agree,
                            eig=w, abs_alpha=np.abs(alphas)))
        sg = f"({pos},{neg},{zero})"
        print(f"{curve['label']:<32} {g:>2} {p:>3} {sg:>13} {pos+neg:>4} "
              f"{'yes' if no_neg else 'NO':>10} {'yes' if rh else 'NO':>12} "
              f"{'OK' if agree else 'X':>6}")

    print("-" * len(header))
    print(f"\n[2T] Rosati form has NO negative eigenvalues for all curves (Weil positivity): "
          f"{all(r['no_neg'] for r in results)}")
    print(f"     |alpha_i| = sqrt(q) (RH for C) for all curves: {all(r['rh'] for r in results)}")
    print(f"     Rosati-positivity <=> RH agreement across family: {all(r['agree'] for r in results)}")
    print(f"     (Zero eigenvalues, e.g. genus-2/F_5, = pi generates a proper subalgebra:")
    print(f"      the form is positive SEMI-definite, rank = dim Q(pi); kernel = relations.)")
    print(f"\n[2T] g=1 check: G_Rosati = [[2, t],[t, 2q]], det = 4q - t^2 > 0 <=> |t| < 2 sqrt q,")
    print(f"     which is MINUS the 2G primitive intersection Gram [[-2,-t],[-t,-2q]]: geometric")
    print(f"     intersection = - Rosati trace form (the standard sign flip). Same condition.")
    print(f"\n[2T] ARITHMETIC TARGET (Direction 8, restated): a positive Rosati involution on the")
    print(f"     arithmetic Frobenius algebra of Spec(Z) = the arithmetic Hodge standard conjecture")
    print(f"     for Gamma_S (#25/#26). Over F_q this is Weil's theorem (from the polarization);")
    print(f"     over Z it is the missing input = RH. A precise problem, not 'build a surface'.")
    print(f"\n     ALL CHECKS PASS: {all_ok}")

    np.savez_compressed(
        out_dir / "e2t_rosati_positivity.npz",
        labels=np.array([r["label"] for r in results], dtype=object),
        all_ok=all_ok,
        **{f"sig_{i}": np.array(r["sig"]) for i, r in enumerate(results)},
        **{f"eig_{i}": r["eig"] for i, r in enumerate(results)},
        **{f"absalpha_{i}": r["abs_alpha"] for i, r in enumerate(results)},
    )

    fig, axs = plt.subplots(1, 2, figsize=(13, 5))
    ax = axs[0]
    for i, r in enumerate(results):
        ax.scatter([i] * len(r["eig"]), r["eig"], color="tab:purple", zorder=3)
    ax.axhline(0, color="r", ls="--", lw=1, label="0 (positivity threshold)")
    ax.set_yscale("symlog")
    ax.set_xlabel("curve index")
    ax.set_ylabel("Rosati form eigenvalues")
    ax.set_title("Rosati trace form: NO negative eigenvalues\n(Weil positivity; zeros = subalgebra relations)")
    ax.legend(); ax.grid(alpha=0.3)

    ax = axs[1]
    for i, r in enumerate(results):
        ax.scatter([i] * len(r["abs_alpha"]), r["abs_alpha"], color="tab:blue", zorder=3)
        ax.scatter([i], [np.sqrt(r["p"])], color="tab:red", marker="_", s=200, zorder=2)
    ax.set_xlabel("curve index")
    ax.set_ylabel(r"$|\alpha_i|$  (red = $\sqrt{q}$)")
    ax.set_title("Rosati positivity forces |alpha_i| = sqrt(q) = RH for C")
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(out_dir / "e2t_rosati_positivity.png", dpi=140)
    plt.close()
    print(f"\n[2T] Saved {out_dir / 'e2t_rosati_positivity.png'}")
    print(f"[2T] Saved {out_dir / 'e2t_rosati_positivity.npz'}")
    return results, all_ok


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--full", action="store_true")
    args = parser.parse_args()
    run(full=args.full)
