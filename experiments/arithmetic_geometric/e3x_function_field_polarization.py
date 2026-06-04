"""Experiment 3X: the function-field polarization, made concrete -- Level 5 where it is a theorem.

## Why this experiment exists

The session's construction sweep (docs/03_research/building_the_missing_positivity.md) concluded
that the missing math is a POLARIZATION: a signed intersection pairing whose negative-definiteness
on a primitive subspace is RH, and which is UNbuildable for Davenport-Heilbronn. Over function
fields this object EXISTS and the analogue of RH is Weil's theorem. This experiment builds it
concretely so we can see exactly what we are missing, and measure its BUFFER (which over Z is the
doubly-exponential marginal wall of e3v, but over F_q is healthy and O(q)).

## The construction (Weil's proof, on the surface E x E)

For an elliptic curve E / F_q with Frobenius trace a (so #E(F_q) = q + 1 - a, |a| <= 2 sqrt q by
Hasse = RH for E), work on the surface S = E x E. The Neron-Severi lattice contains the classes
  h = E x {P}   (horizontal),   v = {P} x E   (vertical),   Delta = diagonal,   Gamma = graph of
the q-Frobenius endomorphism. Their intersection numbers (all four are genus-1 curves with self-
intersection 0 by adjunction on a K-trivial surface) are:

  h.v = 1,  h.Delta = 1,  v.Delta = 1,  h.Gamma = 1,  v.Gamma = q,  Delta.Gamma = #E(F_q) = q+1-a.

The Hodge Index Theorem (a THEOREM here) says the intersection form on NS(S) (x) R has signature
(1, rho - 1): one positive eigenvalue, the rest negative. On the primitive part (orthogonal to an
ample class H), the form is NEGATIVE-DEFINITE, and applying it to the Frobenius class yields, by the
Cauchy-Schwarz / Hodge-index inequality, a^2 <= 4q. That negative-definiteness IS the polarization /
the Rosati positivity, and it IS RH for E.

## What this experiment shows

  Part A. For real elliptic curves over F_p (point-counted), the 4x4 Gram on {h,v,Delta,Gamma} has
    signature exactly (1, 3) for every curve: the Hodge index holds, the polarization exists.
  Part B. The primitive-part form (orthogonal to the ample H = h+v) is negative-definite, and the
    induced bound is a^2 <= 4q with BUFFER 4q - a^2 = O(q), a HEALTHY, definite margin.
  Part C. The contrast that names the missing math. Over F_q the polarization is a theorem with an
    O(q) buffer; over Z the analogous Weil form (e3v) has only a doubly-exponential e^{-4 pi x}
    buffer (no buffer), AND the surface Spec(Z) x Spec(Z) carrying Gamma is not even constructed.
    The missing math is exactly this object: the polarization that is automatic here.
  D-H check: D-H has no Euler product, hence no Frobenius endomorphism, hence no Gamma class and no
    surface. The construction does not even start for D-H -- precisely why it is RH-relevant.

Outputs:
  - e3x_function_field_polarization.npz : per-curve a, signature, buffer
  - e3x_function_field_polarization.png : signature stability + the O(q) buffer vs the integer wall
  - stdout : the report
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def count_points(A, B, p):
    """#E(F_p) for y^2 = x^3 + A x + B (affine + point at infinity), simple Legendre count."""
    # number of affine solutions + 1 (infinity)
    n = 1
    squares = set((y * y) % p for y in range(p))
    # count y for each x via Legendre symbol of RHS
    for x in range(p):
        rhs = (x * x * x + A * x + B) % p
        if rhs == 0:
            n += 1
        elif rhs in squares:
            n += 2
    return n


def intersection_gram(q, a):
    """4x4 intersection matrix on {h, v, Delta, Gamma} on E x E."""
    DG = q + 1 - a  # Delta.Gamma = #E(F_q)
    # rows/cols: h, v, Delta, Gamma ; all self-intersections 0
    return np.array([
        [0.0, 1.0, 1.0, 1.0],
        [1.0, 0.0, 1.0, float(q)],
        [1.0, 1.0, 0.0, float(DG)],
        [1.0, float(q), float(DG), 0.0],
    ])


def primitive_min_eig(G):
    """Negative-definiteness check on the primitive part: restrict G to the orthocomplement
    (w.r.t. G) of an ample class H = h + v, return the max eigenvalue there (should be < 0)."""
    H = np.array([1.0, 1.0, 0.0, 0.0])  # ample h+v
    GH = G @ H
    H2 = H @ G @ H  # = 2 > 0
    # primitive subspace = {x : (G x) . H_dual ...}; use vectors G-orthogonal to H:
    # build basis of the 3-dim space {x : x^T G H = 0}
    c = GH  # x must satisfy c . x = 0
    # null space of the single row c
    _, _, Vt = np.linalg.svd(c.reshape(1, -1))
    B = Vt[1:].T  # 4x3, columns span {x: c.x=0}
    Gp = B.T @ G @ B
    Gp = 0.5 * (Gp + Gp.T)
    return float(np.linalg.eigvalsh(Gp).max()), np.linalg.eigvalsh(Gp)


def run(out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 78)
    print("[3X] The function-field polarization (Level 5 where it is a theorem): E x E")
    print("=" * 78)

    A, B = 1, 1  # y^2 = x^3 + x + 1
    primes = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    print(f"\n  curve y^2 = x^3 + {A}x + {B}\n")
    print("    p    a_p   |a|<2sqrt(p)?   signature(Gram)   prim max-eig   buffer 4p-a^2")
    rows = []
    for p in primes:
        N = count_points(A, B, p)
        a = p + 1 - N
        G = intersection_gram(p, a)
        eig = np.linalg.eigvalsh(G)
        n_pos = int((eig > 1e-9).sum())
        n_neg = int((eig < -1e-9).sum())
        pmax, peig = primitive_min_eig(G)
        buffer = 4 * p - a * a
        hasse = abs(a) < 2 * np.sqrt(p)
        rows.append(dict(p=p, a=a, sig=(n_pos, n_neg), pmax=pmax, buffer=buffer, hasse=hasse))
        print(f"   {p:3d}  {a:4d}      {'Y' if hasse else 'N'}            ({n_pos}, {n_neg})         "
              f"{pmax:+.3f}        {buffer:5d}")

    sigs = set(r["sig"] for r in rows)
    all_neg_prim = all(r["pmax"] < 1e-9 for r in rows)
    all_buffer_pos = all(r["buffer"] > 0 for r in rows)
    print(f"\n  Part A: signature(Gram) over all curves = {sigs}  "
          f"(Hodge Index Theorem predicts (1,3) -> {'CONFIRMED' if sigs=={(1,3)} else 'CHECK'})")
    print(f"  Part B: primitive part negative-definite for all curves: {all_neg_prim}; "
          f"buffer 4p - a^2 > 0 for all: {all_buffer_pos}")
    print(f"          buffer scales as O(p): median buffer/p = "
          f"{np.median([r['buffer']/r['p'] for r in rows]):.2f}")

    print(f"\n  Part C: the contrast that names the missing math")
    print(f"    over F_q: the polarization is a THEOREM (Hodge index), signature (1,3),")
    print(f"             primitive part negative-definite, buffer 4q - a^2 = O(q) (HEALTHY).")
    print(f"    over Z  : the analogue Weil form has buffer ~ e^{{-4 pi x}} (e3v, MARGINAL, no buffer),")
    print(f"             AND the surface Spec(Z) x Spec(Z) carrying the Frobenius class Gamma is not")
    print(f"             even constructed. THE MISSING MATH is exactly this object made automatic here.")
    print(f"    D-H     : no Euler product => no Frobenius endomorphism => no Gamma, no surface;")
    print(f"             the construction does not even start (which is why it is RH-relevant).")

    np.savez_compressed(
        out_dir / "e3x_function_field_polarization.npz",
        p=np.array([r["p"] for r in rows]),
        a=np.array([r["a"] for r in rows]),
        buffer=np.array([r["buffer"] for r in rows]),
        prim_max=np.array([r["pmax"] for r in rows]),
    )

    fig, axs = plt.subplots(1, 2, figsize=(13, 5))
    ax = axs[0]
    ps = np.array([r["p"] for r in rows])
    bufs = np.array([r["buffer"] for r in rows])
    ax.plot(ps, bufs, "o", color="tab:green", label="buffer 4q - a^2 (F_q polarization)")
    ax.plot(ps, 4 * ps, "k--", lw=0.8, label="4q envelope")
    ax.set_xlabel("q = p")
    ax.set_ylabel("Hodge-index buffer")
    ax.set_title("Part B: function-field buffer is O(q)\n(healthy, definite polarization)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    ax = axs[1]
    xs = np.linspace(2, 13, 100)
    ax.semilogy(xs, np.exp(-4 * np.pi * xs), "r-", label="integer Weil buffer ~ e^{-4 pi x} (e3v)")
    ax.semilogy(ps[:8] / 5.0 + 2, bufs[:8] / bufs[0], "go", label="F_q buffer (rescaled, O(q))")
    ax.axhline(1e-16, color="k", ls="--", lw=0.8, label="float64 floor")
    ax.set_xlabel("scale")
    ax.set_ylabel("buffer (log)")
    ax.set_title("Part C: F_q definite buffer vs Z marginal wall\n(why the integer case is hard)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, which="both")

    plt.tight_layout()
    plt.savefig(out_dir / "e3x_function_field_polarization.png", dpi=140)
    plt.close()
    print(f"\n[3X] Saved {out_dir / 'e3x_function_field_polarization.png'}")
    print(f"[3X] Saved {out_dir / 'e3x_function_field_polarization.npz'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.parse_args()
    run()
