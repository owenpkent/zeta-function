"""Experiment 2M (part a): the arithmetic Hodge index at RANK 4.

Extends 2H (Faltings-Hriljac positive-definiteness of the Neron-Tate height pairing,
shown there for ranks 1, 2, 3) to rank 4, on the smallest-conductor rank-4 elliptic
curve 234446a1: y^2 + x y = x^3 - x^2 - 79 x + 289, [a1,a2,a3,a4,a6]=[1,-1,0,-79,289]
(Stein-Jorza-Balakrishnan; conductor 234446 = 2 * 117223).

## Method (reuses the validated 2H machinery; no guessed generators)

Generators are NOT hard-coded from an external source. Instead we find INTEGRAL
points on the curve directly (each verified on-curve by construction) and rely on
the structure of the height pairing: the Neron-Tate pairing is a genuine inner
product on E(Q) tensor R, hence positive SEMI-definite on any set of points, with
rank equal to the number of independent points. We compute the height-pairing Gram
matrix on 8 integral points (via the validated canonical_heights / group law in
e2h_arithmetic_hodge_index.py) and read its signature.

## Validation gate

The 8x8 Gram must be positive semi-definite (no negative eigenvalues) with exactly
4 strictly positive eigenvalues (= the curve's rank; the other 4 are the dependent
directions, near zero). 4 positive eigenvalues, none negative => the arithmetic
Hodge index (positive-definiteness on the independent / rank-4 subspace) holds at
rank 4. PASS only if (positive count == 4) and (no negative eigenvalue).

## Result

Eigenvalues of the 8x8 height Gram (n_iter=6):
  [-0.0001, 0.0, 0.0001, 0.0002, 3.1432, 4.3373, 4.6712, 5.3863]
4 strictly positive, 4 near-zero (the 4 relations among 8 points on a rank-4
group), NONE negative. GATE PASSES. Faltings-Hriljac positive-definiteness now
exhibited at ranks 1, 2, 3 (2H) and 4 (here).
"""

from __future__ import annotations

import argparse
from pathlib import Path

import math
import numpy as np
from sympy import Integer

from experiments.arithmetic_geometric.e2h_arithmetic_hodge_index import add, canonical_heights


# 234446a1: y^2 + x y = x^3 - x^2 - 79 x + 289
CURVE_A = (1, -1, 0, -79, 289)


def integral_points(a, x_lo=-40, x_hi=260):
    """Integral points (x, y) on y^2 + a1 x y + a3 y = x^3 + a2 x^2 + a4 x + a6,
    via the quadratic in y: y = (-(a1 x + a3) +/- sqrt(D))/2,
    D = (a1 x + a3)^2 + 4(x^3 + a2 x^2 + a4 x + a6)."""
    a1, a2, a3, a4, a6 = a
    pts = []
    for x in range(x_lo, x_hi):
        D = (a1 * x + a3) ** 2 + 4 * (x ** 3 + a2 * x ** 2 + a4 * x + a6)
        if D < 0:
            continue
        r = math.isqrt(D)
        if r * r != D:
            continue
        for s in ({r, -r} if r else {0}):
            num = -(a1 * x + a3) + s
            if num % 2 == 0:
                pts.append((x, num // 2))
    # de-dup preserving order
    out = []
    for p in pts:
        if p not in out:
            out.append(p)
    return out


def height_gram(points, a, n_iter=6):
    hh = [canonical_heights(P, a, n_iter=n_iter)[0] for P in points]
    n = len(points)
    G = np.zeros((n, n))
    for i in range(n):
        G[i, i] = hh[i]
        for j in range(i + 1, n):
            hpq = canonical_heights(add(points[i], points[j], a), a, n_iter=n_iter)[0]
            G[i, j] = G[j, i] = 0.5 * (hpq - hh[i] - hh[j])
    return G


def run(n_iter=6, out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    a = tuple(Integer(c) for c in CURVE_A)
    print("[2M] Arithmetic Hodge index at RANK 4 (curve 234446a1).")
    allpts = integral_points(a)
    print(f"     integral points found: {len(allpts)}")
    # a spread of 8 small points (independence emerges from the Gram rank)
    chosen = [(-10, 7), (-9, 19), (-8, 23), (-7, 25), (-4, 25), (0, 17), (1, 14), (3, 7)]
    chosen = [c for c in chosen if c in allpts] or allpts[:8]
    P = [(Integer(x), Integer(y)) for (x, y) in chosen]
    print(f"     using points: {[(int(p[0]),int(p[1])) for p in P]}")

    G = height_gram(P, a, n_iter=n_iter)
    w = np.linalg.eigvalsh(G)
    pos = int((w > 1e-3).sum())
    neg = int((w < -1e-3).sum())
    near0 = len(w) - pos - neg
    gate = (pos == 4 and neg == 0)

    print(f"     height-pairing Gram eigenvalues: {np.round(w, 4).tolist()}")
    print(f"     positive (rank): {pos}   near-zero: {near0}   negative: {neg}")
    print(f"[2M] GATE (4 positive, none negative -> rank-4 arithmetic Hodge index PosDef): "
          f"{'PASS' if gate else 'FAIL'}")

    np.savez_compressed(out_dir / "e2m_rank4_posdef.npz",
                        curve=np.array(CURVE_A), points=np.array(chosen),
                        gram=G, eigenvalues=w, rank=pos, gate=gate)
    print(f"[2M] Saved {out_dir / 'e2m_rank4_posdef.npz'}")
    return gate, w


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-iter", type=int, default=6)
    args = parser.parse_args()
    run(n_iter=args.n_iter)
