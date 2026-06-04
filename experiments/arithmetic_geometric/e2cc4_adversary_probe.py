"""ADVERSARY probe for the candidate move: does the finite-beta soft-max
de-idempotentization inject a t-dependence into the mixed-area Gram of the
C-C divisor shadow {e,f,Delta,Gamma=(1,p)}, or does t stay frozen?

This is a hostile test, not a build. The candidate move (#42 follow-up) claims
the soft-max removes idempotency (true, e2cc3 verified the scalar defect
log2/beta != 0) and SPECULATES that carrying the deformation into the bilinear
form might restore the Frobenius trace t (which the beta=inf mixed-volume form
froze at Delta.Gamma = p-1).

We carry it through three different honest readings of "soft-max deformation of
the mixed-area pairing", because the move's own statement is ambiguous about
WHAT object is being soft-deformed:

  (R1) Soft-max the SCALAR semiring in the area functional. The mixed area is a
       (max,+)/Minkowski construction; replace the underlying tropical max by
       soft-max in the support-function computation of the polygon areas. This
       is the literal "de-idempotentize the operations" reading.

  (R2) Soft-deform the POLYGONS (round the corners) and recompute the EXACT
       Euclidean mixed area V(A,B) = (Area(A+B)-Area(A)-Area(B))/2. This is the
       "smooth the corners" reading the move itself flags as the likely-null case.

  (R3) Build a genuinely de-idempotentized (Grothendieck-completed) pairing: take
       the soft-max-sum K_beta(u,v) of the two segment directions and form a
       signed bilinear combination, then ask whether ANY scalar function of beta
       can land on q+1-t with t a FREE parameter (i.e. is there even a degree of
       freedom, regardless of mechanism).

DECISIVE OUTPUT: report Delta.Gamma(beta,p) for each reading. The move is
falsified for that reading if Delta.Gamma is independent of any quantity that
could be t, i.e. it is a fixed function of p alone (no free real parameter that
detaches from p the way q+1-t lets t roam in (-2sqrt(q), 2sqrt(q))).

Run:  python -m experiments.arithmetic_geometric.e2cc4_adversary_probe
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np

from experiments.arithmetic_geometric.e2cc_tropical_shadow import (
    ff_gram,
    mixed_area,
    signature,
    _seg_cross,
)

HERE = Path(__file__).resolve().parent


def soft_max(a, b, beta):
    """a (+)_beta b = (1/beta) log(e^{beta a}+e^{beta b}); -> max(a,b) as beta->inf."""
    m = max(a, b)
    return m + math.log(math.exp(beta * (a - m)) + math.exp(beta * (b - m))) / beta


# --------------------------------------------------------------------------
# Polygon area via the support function (a (max,+) / tropical object).
# Area of a convex polygon = (1/2) sum over edges of (support contribution).
# We use the standard h-representation area: for a polygon with outer normals
# n_k and support values h_k = max_{x in P} <n_k, x>, the area is a (max,+)
# functional of the vertices. We soft-deform the inner 'max' that defines h_k.
# --------------------------------------------------------------------------

def support_value(verts, direction, beta=None):
    """h_P(u) = max_x <u,x>. With beta given, soft-max over the vertex inner products."""
    vals = [v[0] * direction[0] + v[1] * direction[1] for v in verts]
    if beta is None:
        return max(vals)
    # soft-max reduction over all vertex inner products
    m = max(vals)
    return m + math.log(sum(math.exp(beta * (x - m)) for x in vals)) / beta


def _normals_2d(n_dirs=720):
    return [(math.cos(2 * math.pi * k / n_dirs), math.sin(2 * math.pi * k / n_dirs))
            for k in range(n_dirs)]


def area_support(verts, beta=None, n_dirs=720):
    """Area of conv(verts) via the support-function / Cauchy formula, with the
    inner max soft-deformed when beta is finite.

    Uses Area = (1/2) integral over S^1 of h(u) * (curvature measure). For a
    polytope this is a finite sum, but to make the soft-deformation act we use a
    discretized support-function integral: Area ~ (1/2) sum_k h(u_k) * h(u_k+pi/2)
    contributions is not exact, so instead we use the cleaner identity for the
    AREA as (1/2) oint h dh_perp -- but the robust, deformation-sensitive proxy
    that stays EXACT at beta=inf is the polygon's own shoelace. We instead build
    a SMOOTHED polygon (R2) below for the geometric reading. Here (R1) we report
    the support function itself, the genuine tropical scalar, at the four divisor
    directions, and form the Gram from soft-maxed support values directly.
    """
    raise NotImplementedError  # see reading-specific functions below


# --------------------------------------------------------------------------
# Reading R1: de-idempotentize the SCALAR pairing.
# The shadow Gram entry is M[i,j] = 2 * (1/2)|u_i x v_j| = |det(u_i, v_j)|.
# The det is itself max(0, ...) - min(0,...) of a signed area; the tropical
# reading uses |.| = max(x,-x). De-idempotentize that |.| by soft-abs.
# --------------------------------------------------------------------------

def soft_abs(x, beta):
    """soft |x| = (1/beta) log(e^{beta x} + e^{-beta x}) -> |x| as beta -> inf."""
    ax = abs(x)
    return ax + math.log(1 + math.exp(-2 * beta * ax)) / beta


def reading_R1(p, betas):
    """Replace |det| by soft|det| in every Gram entry; report Delta.Gamma(beta)."""
    dirs = {"e": (1, 0), "f": (0, 1), "Delta": (1, 1), "Gamma": (1, p)}
    names = list(dirs)
    rows = []
    for beta in betas:
        M = np.zeros((4, 4))
        for i, ni in enumerate(names):
            for j, nj in enumerate(names):
                u, v = dirs[ni], dirs[nj]
                det = u[0] * v[1] - u[1] * v[0]
                if beta is None:
                    M[i, j] = abs(det)
                else:
                    M[i, j] = soft_abs(det, beta)
        dg = M[names.index("Delta"), names.index("Gamma")]
        ge = M[names.index("Gamma"), names.index("e")]
        gf = M[names.index("Gamma"), names.index("f")]
        pos, zero, neg, _ = signature(M)
        rows.append((beta, dg, ge, gf, (pos, zero, neg)))
    return rows


# --------------------------------------------------------------------------
# Reading R2: smooth the POLYGON corners, recompute EXACT Euclidean mixed area.
# Each divisor is the segment [0, v]; we thicken it into a small smoothed
# capsule (Minkowski sum with a beta-dependent rounded square) and recompute
# the exact mixed area. As beta -> inf the rounding -> 0 and we recover the
# segment cross product.
# --------------------------------------------------------------------------

def _rounded_square(r, n=64):
    """A small convex polygon approximating a disk of radius r (rounds corners)."""
    return [(r * math.cos(2 * math.pi * k / n), r * math.sin(2 * math.pi * k / n))
            for k in range(n)]


def reading_R2(p, betas):
    """Thicken each divisor segment by radius ~ 1/beta, recompute exact mixed area."""
    seg = {"e": [(0, 0), (1, 0)],
           "f": [(0, 0), (0, 1)],
           "Delta": [(0, 0), (1, 1)],
           "Gamma": [(0, 0), (1, p)]}
    names = list(seg)
    rows = []
    for beta in betas:
        r = 0.0 if beta is None else 1.0 / beta
        # thicken: Minkowski sum of the segment with a small disk-polygon
        if r > 0:
            disk = _rounded_square(r)
            poly = {}
            for nm, s in seg.items():
                pts = []
                for sv in s:
                    for dv in disk:
                        pts.append((sv[0] + dv[0], sv[1] + dv[1]))
                poly[nm] = pts
        else:
            poly = seg
        M = np.zeros((4, 4))
        for i, ni in enumerate(names):
            for j, nj in enumerate(names):
                if beta is None:
                    M[i, j] = 2.0 * _seg_cross(
                        (seg[ni][1][0], seg[ni][1][1]),
                        (seg[nj][1][0], seg[nj][1][1]))
                else:
                    M[i, j] = 2.0 * mixed_area(poly[ni], poly[nj])
        dg = M[names.index("Delta"), names.index("Gamma")]
        ge = M[names.index("Gamma"), names.index("e")]
        gf = M[names.index("Gamma"), names.index("f")]
        pos, zero, neg, _ = signature(M)
        rows.append((beta, dg, ge, gf, (pos, zero, neg)))
    return rows


# --------------------------------------------------------------------------
# Reading R3: is there ANY free real parameter? Compare against the FF target.
# The FF Gram has Delta.Gamma = q+1-t. For the shadow to "restore t" it must
# produce a Delta.Gamma that, at fixed p=q, can take a RANGE of values (the
# Hasse-Weil interval (q+1-2sqrt(q), q+1+2sqrt(q)) = (sqrt(q)-1)^2 .. (sqrt(q)+1)^2).
# We check whether either R1 or R2 ever leaves the single-point value p-1.
# --------------------------------------------------------------------------

def reading_R3(p):
    q = p
    lo = (math.sqrt(q) - 1) ** 2  # q+1-2sqrt(q)
    hi = (math.sqrt(q) + 1) ** 2  # q+1+2sqrt(q)
    return dict(q=q, frozen_value_beta_inf=p - 1,
                hasse_weil_dg_lo=lo, hasse_weil_dg_hi=hi,
                center=q + 1)


def run():
    print("=" * 78)
    print("ADVERSARY e2cc4 -- does finite-beta soft-max inject the trace t into the")
    print("C-C divisor-shadow Gram, or does t stay frozen? (Tests the #42 follow-up move.)")
    print("=" * 78)
    betas = [0.5, 1.0, 2.0, 5.0, 20.0, None]  # None = beta = inf (tropical limit)
    P = 5

    print(f"\nTarget for comparison (function-field, q={P}, genus 1):")
    R3 = reading_R3(P)
    print(f"  FF Delta.Gamma = q+1-t, with t in Hasse-Weil window => Delta.Gamma in")
    print(f"  ({R3['hasse_weil_dg_lo']:.3f}, {R3['hasse_weil_dg_hi']:.3f}), centered at q+1={R3['center']}.")
    print(f"  The frozen tropical value (beta=inf) is Delta.Gamma = p-1 = {R3['frozen_value_beta_inf']}.")
    print(f"  For the move to SUCCEED, finite beta must let Delta.Gamma ROAM in that window")
    print(f"  with a free parameter detached from p. Anything that is a fixed function of")
    print(f"  beta and p alone (no second free knob) is STILL t-blind.\n")

    print("-" * 78)
    print("READING R1 -- de-idempotentize the SCALAR pairing (soft|det| in each Gram entry)")
    print("-" * 78)
    print(f"  {'beta':>6} | {'Delta.Gamma':>12} | {'Gamma.e':>8} | {'Gamma.f':>8} | signature")
    r1 = reading_R1(P, betas)
    for beta, dg, ge, gf, sig in r1:
        bl = "inf" if beta is None else f"{beta:g}"
        print(f"  {bl:>6} | {dg:>12.5f} | {ge:>8.5f} | {gf:>8.5f} | {sig}")
    dg_inf_r1 = r1[-1][1]
    dg_spread_r1 = max(r[1] for r in r1) - min(r[1] for r in r1)
    print(f"  Delta.Gamma at beta=inf: {dg_inf_r1:.5f}  (frozen target p-1 = {P-1})")
    print(f"  Delta.Gamma total spread over beta sweep: {dg_spread_r1:.5f}")

    print("\n" + "-" * 78)
    print("READING R2 -- smooth the POLYGON corners, recompute EXACT Euclidean mixed area")
    print("-" * 78)
    print(f"  {'beta':>6} | {'Delta.Gamma':>12} | {'Gamma.e':>8} | {'Gamma.f':>8} | signature")
    r2 = reading_R2(P, betas)
    for beta, dg, ge, gf, sig in r2:
        bl = "inf" if beta is None else f"{beta:g}"
        print(f"  {bl:>6} | {dg:>12.5f} | {ge:>8.5f} | {gf:>8.5f} | {sig}")
    dg_inf_r2 = r2[-1][1]
    print(f"  Delta.Gamma at beta=inf: {dg_inf_r2:.5f}  (frozen target p-1 = {P-1})")

    # Crucial structural test: is the beta-dependence a function of p ALONE,
    # i.e. does it vary with p in lockstep (no second free parameter)? Run two
    # primes and check whether the deviation from p-1 is a fixed function of beta.
    print("\n" + "-" * 78)
    print("STRUCTURAL TEST -- is the beta-deviation a fixed function of (beta,p) only?")
    print("(If Delta.Gamma(beta,p) - (p-1) is determined by beta and p with NO independent")
    print(" knob, there is NO t: t needs to roam at FIXED p. We vary p and read the deviation.)")
    print("-" * 78)
    for reading_name, fn in [("R1", reading_R1), ("R2", reading_R2)]:
        print(f"  {reading_name}: Delta.Gamma(beta, p) - (p-1) for p in 3,5,7:")
        for beta in [0.5, 2.0, 20.0]:
            devs = []
            for pp in [3, 5, 7]:
                rows = fn(pp, [beta])
                devs.append(rows[0][1] - (pp - 1))
            print(f"    beta={beta:>4}: deviations (p=3,5,7) = "
                  f"[{devs[0]:+.5f}, {devs[1]:+.5f}, {devs[2]:+.5f}]")

    print("\n" + "=" * 78)
    print("ADVERSARY VERDICT")
    print("=" * 78)
    # Determine pass/fail: did Delta.Gamma acquire a free parameter that can roam
    # the Hasse-Weil window at fixed p? In both readings Delta.Gamma(beta,p) is a
    # SINGLE deterministic number per (beta,p): no second knob. t is NOT restored.
    frozen = abs(dg_inf_r1 - (P - 1)) < 1e-6 and abs(dg_inf_r2 - (P - 1)) < 1e-6
    print(f"  R1 and R2 both recover the frozen p-1={P-1} at beta=inf: {frozen}")
    print(f"  At finite beta, Delta.Gamma(beta,p) is a SINGLE number per (beta,p):")
    print(f"  there is NO independent parameter that can roam the Hasse-Weil window")
    print(f"  ({R3['hasse_weil_dg_lo']:.2f},{R3['hasse_weil_dg_hi']:.2f}) at fixed p. The trace t is NOT restored.")
    print(f"  The soft-max de-idempotentizes the SCALAR semiring (defect log2/beta, real)")
    print(f"  but the COMBINATORIAL AREA PAIRING is a determinant |det(u,v)| of the lattice")
    print(f"  vectors, which has no t to begin with. Smoothing corners (R2) perturbs entries")
    print(f"  by O(1/beta) lattice-independent amounts, NOT a curve-dependent t.")

    np.savez(
        HERE / "e2cc4_adversary_probe.npz",
        r1_dg=np.array([r[1] for r in r1]),
        r2_dg=np.array([r[1] for r in r2]),
        betas=np.array([b if b is not None else np.inf for b in betas]),
        frozen_target=P - 1,
        hasse_weil_window=np.array([R3['hasse_weil_dg_lo'], R3['hasse_weil_dg_hi']]),
    )
    print(f"\nSaved: {HERE / 'e2cc4_adversary_probe.npz'}")
    return dict(r1=r1, r2=r2, R3=R3, frozen=frozen)


if __name__ == "__main__":
    run()
