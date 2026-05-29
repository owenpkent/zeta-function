"""Experiment 2G: positivity from a SIGNATURE -- the Hodge index theorem on C x C
made computational, as the Weil template for Direction 8.

This opens the Direction 8 thread ([08_hodge_index_surface.md](../../docs/03_research/research_directions/08_hodge_index_surface.md)),
the project's central open problem: prove a Hodge index theorem on a constructed
arithmetic surface below Spec(Z), giving RH-positivity from the SIGNATURE of an
intersection form rather than from a trace identity (the R3.5 / K1 escape route).

2F exhibited the function-field RH *bound* |alpha_i| = sqrt(q) from point counts.
But the bound is the CONSEQUENCE; the *mechanism* is the Hodge index theorem on
the surface C x C, which 2F never builds. This experiment builds it: the
intersection form on an explicit sublattice of NS(C x C), and shows its SIGNATURE
is what forces the Weil bound. This realizes Direction 8 milestones 5.1 (state the
Hodge index precisely) and 5.5 (Weil specialization / the K3 check) in concrete,
exact, verifiable form, and pins down the target object a Spec(Z) lift must
reproduce.

## The construction (Weil 1948, made computational)

On the smooth projective surface S = C x C for C of genus g over F_q, take the
divisor classes
    e  = {P} x C   (fibre of the first projection)
    f  = C x {P}   (fibre of the second projection)
    Delta          (the diagonal)
    Gamma          (the graph of the q-power Frobenius phi: C -> C)
with the classical intersection numbers
    e^2 = f^2 = 0,   e.f = 1,
    e.Delta = f.Delta = 1,   Delta^2 = 2 - 2g           (adjunction)
    e.Gamma = 1,   f.Gamma = q   (Frobenius is a (1, q) correspondence)
    Delta.Gamma = N_1 = #C(F_q)  (Lefschetz fixed-point count)
    Gamma^2 = q (2 - 2g)         (deg(phi) . Delta^2)

{e, f} span a hyperbolic plane (signature (1, 1)). The Hodge index theorem says
the intersection form on its orthogonal complement (the "primitive" classes) is
NEGATIVE DEFINITE. Project Delta and Gamma into the primitive part:
    Delta_0 = Delta - (Delta.f) e - (Delta.e) f = Delta - e - f
    Gamma_0 = Gamma - (Gamma.f) e - (Gamma.e) f = Gamma - q e - f
Using e^2 = f^2 = 0, e.f = 1, for any D, E: D_0.E_0 = D.E - (D.e)(E.f) - (D.f)(E.e).
Hence the primitive Gram matrix is
    Delta_0^2      = (2 - 2g) - 2          = -2g
    Gamma_0^2      = q(2 - 2g) - 2q        = -2gq
    Delta_0.Gamma_0 = N_1 - 1 - q          = -(q + 1 - N_1) = -t
where t := q + 1 - N_1 = trace of Frobenius on H^1 = sum of the 2g eigenvalues.

So the primitive Gram is
    G_prim = [[ -2g , -t  ],
              [ -t  , -2gq]].

## The headline: the Hasse-Weil bound IS the signature condition

Hodge index => G_prim is negative definite
            <=> det(G_prim) > 0 and trace < 0
            <=> 4 g^2 q - t^2 > 0
            <=> |t| < 2 g sqrt(q)        (the Hasse-Weil / Riemann bound).

Iterating over Frobenius powers phi^n (t_n = q^n + 1 - N_n = sum alpha_i^n) gives
|sum alpha_i^n| <= 2 g q^{n/2} for all n, which forces |alpha_i| = sqrt(q) for
every eigenvalue. This is "positivity from a signature": the negative-definiteness
of an intersection form, not any trace identity, is what closes RH. That is
exactly the structure Direction 8 must reproduce over Spec(Z), and exactly the K1
escape route R3.5 identifies as unique.

## K1 / K2 / K3 reading

- K3 (Weil specialization): this experiment IS the function-field case, exact.
- K1 (no-shortcut escape): positivity here comes from the SIGNATURE of a Gram
  matrix (eigenvalue signs), not from a trace identity. That is the structural
  feature R3.5 says a valid RH proof must have. We verify the signature is the
  load-bearing step (the bound fails the instant the primitive form acquires a
  non-negative eigenvalue).
- K2 (D-H discipline): the construction is unbuildable for Davenport-Heilbronn.
  D-H has no Euler product, hence no Frobenius endomorphism, hence no graph
  Gamma, no surface, no Delta^2 = 2 - 2g. The Weil template cannot even be set up.
  This is the geometric face of the 3M finding (no Euler product <=> the von
  Mangoldt weight delocalizes off prime powers): no Euler product <=> no Frobenius
  correspondence to put on the surface.

Outputs:
  - e2g_intersection_signature.npz : per-curve Gram matrices, signatures, bounds
  - e2g_intersection_signature.png : signature + Hasse-Weil margin across the family
  - stdout : per-curve table
"""

from __future__ import annotations

import argparse
import time
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from experiments.arithmetic_geometric.e2f_hodge_index_sweep import (
    count_points_Fpk,
    elliptic_family,
    genus2_family,
)


def full_gram(q: int, g: int, N1: int) -> np.ndarray:
    """The 4x4 intersection Gram matrix on the sublattice {e, f, Delta, Gamma}
    of NS(C x C), in that basis order. Exact integer entries."""
    Dsq = 2 - 2 * g
    G = np.array([
        # e        f        Delta    Gamma
        [0,        1,       1,       1     ],   # e
        [1,        0,       1,       q     ],   # f
        [1,        1,       Dsq,     N1    ],   # Delta
        [1,        q,       N1,      q * Dsq],  # Gamma
    ], dtype=float)
    return G


def primitive_gram(q: int, g: int, N1: int):
    """The 2x2 Gram on the primitive parts {Delta_0, Gamma_0} (orthogonal to the
    hyperbolic {e, f} plane). Returns (G_prim, t) with t = q + 1 - N1."""
    t = q + 1 - N1
    G_prim = np.array([
        [-2 * g, -t      ],
        [-t,     -2 * g * q],
    ], dtype=float)
    return G_prim, t


def signature(M: np.ndarray, tol: float = 1e-9):
    """(# positive, # negative, # zero) eigenvalues of a symmetric matrix."""
    w = np.linalg.eigvalsh(M)
    scale = max(abs(w).max(), 1.0)
    pos = int((w > tol * scale).sum())
    neg = int((w < -tol * scale).sum())
    zero = len(w) - pos - neg
    return pos, neg, zero, w


def analyze_curve(curve) -> dict:
    p, g, f_coeffs = curve["p"], curve["g"], curve["f_coeffs"]
    N1 = count_points_Fpk(f_coeffs, p, 1)
    t = p + 1 - N1

    G_full = full_gram(p, g, N1)
    G_prim, _ = primitive_gram(p, g, N1)

    sig_full = signature(G_full)
    sig_prim = signature(G_prim)

    # Hodge index predictions:
    #   full {e,f,Delta,Gamma}: exactly one positive eigenvalue -> signature (1, 3).
    #   primitive {Delta_0,Gamma_0}: negative definite -> signature (0, 2).
    hodge_full_ok = (sig_full[0] == 1)
    hodge_prim_ok = (sig_prim[0] == 0 and sig_prim[1] == 2)

    # The Hasse-Weil bound as the signature condition.
    margin = 4 * g * g * p - t * t          # > 0  <=>  |t| < 2g sqrt(q)
    hasse_weil_ok = (abs(t) < 2 * g * np.sqrt(p) + 1e-9)
    # the two must agree: negative-definiteness of G_prim <=> Hasse-Weil.
    consistent = (hodge_prim_ok == (margin > 0))

    return dict(
        p=p, g=g, label=curve["label"], N1=N1, t=t,
        G_full=G_full, G_prim=G_prim,
        sig_full=sig_full[:3], eig_full=sig_full[3],
        sig_prim=sig_prim[:3], eig_prim=sig_prim[3],
        hodge_full_ok=hodge_full_ok, hodge_prim_ok=hodge_prim_ok,
        margin=float(margin), hasse_weil_ok=hasse_weil_ok,
        consistent=consistent,
    )


def run(primes_elliptic=(5, 7, 11, 13), primes_genus2=(5, 7, 11),
        full: bool = False, out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    if full:
        primes_elliptic = (5, 7, 11, 13, 17, 19, 23, 29, 31)
        primes_genus2 = (5, 7, 11, 13)

    curves = elliptic_family(list(primes_elliptic))
    if primes_genus2:
        curves += genus2_family(list(primes_genus2))

    print("[2G] Positivity from a SIGNATURE: the Hodge index theorem on C x C.")
    print("     Primitive intersection form negative definite  <=>  Hasse-Weil bound")
    print("     |q + 1 - N_1| < 2 g sqrt(q).  This is the Weil template for Direction 8.\n")
    header = (f"{'curve':<34} {'g':>2} {'q':>3} {'N1':>4} {'t':>5} "
              f"{'sig(e,f,D,G)':>13} {'sig(prim)':>10} "
              f"{'4g^2q - t^2':>12} {'HW':>3} {'Hodge':>6}")
    print(header)
    print("-" * len(header))

    results = []
    all_ok = True
    for curve in curves:
        r = analyze_curve(curve)
        results.append(r)
        ok = r["hodge_full_ok"] and r["hodge_prim_ok"] and r["hasse_weil_ok"] and r["consistent"]
        all_ok = all_ok and ok
        sf = f"({r['sig_full'][0]},{r['sig_full'][1]},{r['sig_full'][2]})"
        sp = f"({r['sig_prim'][0]},{r['sig_prim'][1]})"
        print(f"{r['label']:<34} {r['g']:>2} {r['p']:>3} {r['N1']:>4} {r['t']:>5} "
              f"{sf:>13} {sp:>10} {r['margin']:>12.1f} "
              f"{'OK' if r['hasse_weil_ok'] else 'X':>3} "
              f"{'(1,3)' if r['hodge_full_ok'] else 'BAD':>6}")

    print("-" * len(header))
    print(f"\n[2G] Across the family:")
    print(f"     full Gram {{e,f,Delta,Gamma}} signature (1,3) for all curves: "
          f"{all(r['hodge_full_ok'] for r in results)}")
    print(f"     primitive Gram negative definite (0,2) for all curves: "
          f"{all(r['hodge_prim_ok'] for r in results)}")
    print(f"     Hasse-Weil |t| < 2g sqrt(q) for all curves: "
          f"{all(r['hasse_weil_ok'] for r in results)}")
    print(f"     signature condition <=> Hasse-Weil (consistency): "
          f"{all(r['consistent'] for r in results)}")
    print(f"\n[2G] The negative-definite SIGNATURE of the primitive intersection form")
    print(f"     IS the Hasse-Weil bound. Iterating over Frobenius powers forces")
    print(f"     |alpha_i| = sqrt(q): positivity from a signature, the Direction 8 target.")
    print(f"     ALL CHECKS PASS: {all_ok}")

    _save_and_plot(results, out_dir)
    return results, all_ok


def _save_and_plot(results, out_dir: Path):
    save = {"n_curves": len(results),
            "labels": np.array([r["label"] for r in results], dtype=object)}
    for i, r in enumerate(results):
        save[f"c{i}_p"] = r["p"]; save[f"c{i}_g"] = r["g"]
        save[f"c{i}_N1"] = r["N1"]; save[f"c{i}_t"] = r["t"]
        save[f"c{i}_G_full"] = r["G_full"]; save[f"c{i}_G_prim"] = r["G_prim"]
        save[f"c{i}_eig_prim"] = r["eig_prim"]; save[f"c{i}_margin"] = r["margin"]
    np.savez_compressed(out_dir / "e2g_intersection_signature.npz", **save)

    fig, axs = plt.subplots(1, 2, figsize=(13, 5))

    # Panel 1: the two primitive eigenvalues per curve (both must be < 0).
    ax = axs[0]
    idx = np.arange(len(results))
    lam1 = [r["eig_prim"][0] for r in results]
    lam2 = [r["eig_prim"][1] for r in results]
    ax.scatter(idx, lam1, color="tab:blue", label=r"$\lambda_1(G_{\rm prim})$", zorder=3)
    ax.scatter(idx, lam2, color="tab:cyan", label=r"$\lambda_2(G_{\rm prim})$", zorder=3)
    ax.axhline(0, color="r", lw=1.0, ls="--", label="0 (Hodge index threshold)")
    ax.set_xlabel("curve index")
    ax.set_ylabel("primitive Gram eigenvalues")
    ax.set_title("Hodge index: primitive intersection form is negative definite\n(both eigenvalues < 0, for every curve)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    # Panel 2: the Hasse-Weil margin 4g^2 q - t^2 = -det(G_prim) sign, per curve.
    ax = axs[1]
    margins = [r["margin"] for r in results]
    ax.bar(idx, margins, color=["tab:green" if m > 0 else "tab:red" for m in margins])
    ax.axhline(0, color="k", lw=1.0)
    ax.set_xlabel("curve index")
    ax.set_ylabel(r"$4 g^2 q - t^2$ (= signature margin)")
    ax.set_title("Hasse-Weil bound as the signature condition\n($>0$ <=> primitive form negative definite <=> $|t| < 2g\\sqrt{q}$)")
    ax.grid(alpha=0.3, axis="y")

    plt.tight_layout()
    plt.savefig(out_dir / "e2g_intersection_signature.png", dpi=140)
    plt.close()
    print(f"\n[2G] Saved {out_dir / 'e2g_intersection_signature.png'}")
    print(f"[2G] Saved {out_dir / 'e2g_intersection_signature.npz'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Intersection-form signature on C x C (Weil template).")
    parser.add_argument("--full", action="store_true", help="More primes + genus-2 curves.")
    parser.add_argument("--primes-elliptic", type=int, nargs="+", default=[5, 7, 11, 13])
    parser.add_argument("--primes-genus2", type=int, nargs="+", default=[5, 7, 11])
    args = parser.parse_args()
    run(primes_elliptic=tuple(args.primes_elliptic),
        primes_genus2=tuple(args.primes_genus2), full=args.full)
