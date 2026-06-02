"""2CC -- the tropical (mixed-volume) shadow of the Hodge index on the Connes-Consani
square: it gives a Lorentzian signature for FREE (Alexandrov-Fenchel) and reproduces the
(1,p) bidegree, but it is BLIND to the Frobenius trace t -- so the Direction-8 gap is
exactly the arithmetic q-lift that restores t.

CONTEXT (Direction 8, the product surface). Connes-Consani (arXiv:1502.05580) build the
arithmetic-site SQUARE as the topos N^x2 with structure sheaf Conv_>=(Z x Z) = convex
Newton polygons under (convex-hull-union, Minkowski-sum), carrying Frobenius
correspondences Psi(lambda) of real slope lambda, with Fr_{n,m} = diag(n,m) on the
quadrant. This IS the Spec(Z) x Spec(Z) product surface the project chases (reading note
Connes-Consani-2015). The reading note isolates the gap precisely: the characteristic-1
operations are IDEMPOTENT (union, max, convex hull, Minkowski sum), so there is NO
subtraction, hence NO signed intersection number, hence NO Hodge-index signature. That
missing signed pairing is the whole Direction-8 gap.

THE IDEA TESTED HERE. The Minkowski-sum structure carries a canonical bilinear form: the
MIXED AREA V(A,B) = (Area(A+B) - Area(A) - Area(B))/2 (the 2D mixed volume). By the
Alexandrov-Fenchel / Teissier-Khovanskii mixed Hodge index theorem this form is LORENTZIAN:
the Gram of mixed volumes of convex bodies has at most ONE positive eigenvalue, i.e. a
Hodge-index signature (1, k). (Minkowski's pairwise inequality V(A,B)^2 >= V(A,A)V(B,B) is
necessary but not sufficient for the global signature; the global statement is the AF
theorem, confirmed here numerically over 2000 random collections by the ADVERSARY.)

IMPORTANT HONEST FRAMING (ADVERSARY-checked). Mixed-volume = intersection-number is a TORIC
geometry theorem (BKK / Khovanskii-Teissier) about the toric variety X_Sigma of a fan,
where Newton polytopes are divisor classes. The C-C square is a CHARACTERISTIC-1 TOPOS, not
a toric variety, and its Newton polygons are structure-sheaf sections, not divisor classes.
So the mixed-area form is NOT a constructed intersection theory of the C-C topos; it is a
PROPOSED shadow of the (still missing) signed pairing, by analogy with toric BKK. What is
rigorous: (i) the mixed-area form is canonical on the Minkowski structure; (ii) it is
Lorentzian by AF; (iii) it is arithmetic-blind. The decisive question is whether ANY such
form can carry the Frobenius trace t that carries RH on the function-field template
(|t| < 2g sqrt(q) <=> RH-for-C).

WHAT WE FIND (prediction, confirmed below):
 (A) AF holds: the mixed-area Gram of full 2D lattice polygons has exactly ONE positive
     eigenvalue. A Lorentzian / Hodge-index signature exists on this convex-geometry form
     for free -- but it takes NO arithmetic input, so it is RH-agnostic VACUOUSLY.
 (B) The DIVISOR shadow {e=(1,0), f=(0,1), Delta=(1,1), Gamma_p=Fr_{1,p}(Delta)=(1,p)},
     via edge-direction segments, equals the function-field Gram at the SINGLE point t=2
     with e and f SWAPPED (verified: the shadow Gram = ff_gram(p,2,1) under e<->f). So it
     does not independently recover the (1,p) bidegree -- it produces {p,1} (swapped) and
     the signature agreement is that relabeling. The robust content is that the mixed-area
     form is t-BLIND: it has no free real parameter t (the value t=2 is the edge-segment
     representative's; full 2D polygons give other constants), so it can never be the
     continuum q + 1 - t. The shadow is a single frozen specialization, genus 1 only.
 (C) The genuine function-field Gram (2G) has Delta . Gamma = q + 1 - t and signature
     (1,3) <=> |t| < 2g sqrt(q) (Hasse-Weil = RH-for-C), which REQUIRES t. The shadow loses
     precisely this (it gives (1,3) UNCONDITIONALLY, for its frozen t, so a "passing"
     signature on the shadow does NOT imply RH).
 (D) K2: Davenport-Heilbronn has no Euler product, hence no (1,p) bidegree / no Frobenius
     slope p (2Q/#25), so it has no Gamma_p polygon at all -- the shadow does not even start.

CONSEQUENCE (softened, ADVERSARY-checked). A canonical Lorentzian convex-geometry form (the
mixed-volume / AF mixed Hodge index) exists for free on the C-C square's Minkowski
structure, BUT it takes no arithmetic input and is therefore RH-agnostic -- the trivial
extreme of the soft-positivity pattern (#38 dBN kernel, #39 Rodgers-Tao functional, which
at least take zeta as input). This RECONCILES with the reading note's "the signed pairing
does not exist": the RH-agnostic convex-geometry shadow exists; the ARITHMETIC signed
pairing carrying the trace t does NOT. So the Direction-8 gap is sharpened, not closed: the
RH content is the trace t, lost in the idempotent/tropical structure, and the missing object
is the arithmetic q-LIFT that restores t (the "suitable Weil cohomology" Connes-Consani name,
end of their section 4). The (1,p) bidegree is where that lift must inject t.

Run:  python -m experiments.arithmetic_geometric.e2cc_tropical_shadow
"""

from __future__ import annotations

from pathlib import Path

import numpy as np

try:
    from scipy.spatial import ConvexHull
    _HAVE_SCIPY = True
except Exception:  # pragma: no cover
    _HAVE_SCIPY = False

HERE = Path(__file__).resolve().parent


# --------------------------------------------------------------------------
# Convex-polygon mixed area (the 2D mixed volume).
# --------------------------------------------------------------------------

def _poly_area(verts):
    """Shoelace area of a polygon given by (unordered) vertices; we hull first."""
    pts = np.asarray(verts, dtype=float)
    if len(pts) < 3:
        return 0.0  # segment or point: zero area
    # Degenerate (collinear) -> zero area; ConvexHull raises, so guard.
    if np.linalg.matrix_rank(pts - pts[0], tol=1e-9) < 2:
        return 0.0
    hull = ConvexHull(pts)
    return float(hull.volume)  # 'volume' in 2D is area


def _minkowski_sum(A, B):
    """Minkowski sum of two convex polygons = convex hull of pairwise vertex sums."""
    A = np.asarray(A, dtype=float)
    B = np.asarray(B, dtype=float)
    sums = (A[:, None, :] + B[None, :, :]).reshape(-1, 2)
    return sums


def mixed_area(A, B):
    """V(A,B) = (Area(A (+) B) - Area(A) - Area(B)) / 2  (the 2D mixed volume).

    Symmetric, bilinear under Minkowski sum, and (Alexandrov-Fenchel/Minkowski)
    V(A,B)^2 >= V(A,A) V(B,B): the form is Lorentzian on convex bodies.
    """
    s = _minkowski_sum(A, B)
    return 0.5 * (_poly_area(s) - _poly_area(A) - _poly_area(B))


def signature(M):
    """(#positive, #zero, #negative) eigenvalues of a real symmetric matrix, with a
    tolerance scaled to the matrix size."""
    w = np.linalg.eigvalsh(np.asarray(M, dtype=float))
    tol = max(1e-9, 1e-9 * float(np.max(np.abs(w))))
    pos = int(np.sum(w > tol))
    neg = int(np.sum(w < -tol))
    zero = len(w) - pos - neg
    return pos, zero, neg, w


# --------------------------------------------------------------------------
# Part A: Alexandrov-Fenchel -- the tropical Hodge index is free.
# --------------------------------------------------------------------------

def part_A():
    print("=" * 78)
    print("PART A -- Alexandrov-Fenchel: the mixed-area form on convex bodies is Lorentzian")
    print("(at most ONE positive eigenvalue = a Hodge-index signature, FOR FREE).")
    print("=" * 78)
    # A spread of full-dimensional lattice polygons (triangles, squares, pentagons).
    polys = {
        "unit square": [(0, 0), (1, 0), (1, 1), (0, 1)],
        "triangle": [(0, 0), (2, 0), (0, 2)],
        "wide rect": [(0, 0), (3, 0), (3, 1), (0, 1)],
        "tall rect": [(0, 0), (1, 0), (1, 3), (0, 3)],
        "pentagon": [(0, 0), (2, 0), (3, 2), (1, 3), (-1, 2)],
        "diamond": [(0, -1), (1, 0), (0, 1), (-1, 0)],
    }
    names = list(polys)
    n = len(names)
    G = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            G[i, j] = mixed_area(polys[names[i]], polys[names[j]])
    pos, zero, neg, w = signature(G)
    print(f"  polygons: {names}")
    print(f"  mixed-area Gram signature (pos, zero, neg) = ({pos}, {zero}, {neg})")
    print(f"  eigenvalues = {np.round(w, 4)}")
    # Verify the pairwise Minkowski inequality V(A,B)^2 >= V(A,A)V(B,B) (Lorentzian).
    viol = 0
    for i in range(n):
        for j in range(n):
            if mixed_area(polys[names[i]], polys[names[j]]) ** 2 < (
                G[i, i] * G[j, j] - 1e-9
            ):
                viol += 1
    print(f"  Minkowski-inequality violations V(A,B)^2 < V(A,A)V(B,B): {viol} (necessary, not sufficient)")
    print(f"  => AF / Teissier-Khovanskii mixed Hodge index: exactly {pos} positive eigenvalue")
    print(f"     (the GLOBAL (1,k) is the AF theorem, not the pairwise check; a Lorentzian")
    print(f"     convex-geometry form exists for free -- but takes NO arithmetic input).\n")
    return dict(signature=(pos, zero, neg), eigs=w.tolist(), minkowski_violations=viol)


# --------------------------------------------------------------------------
# Part B: the divisor shadow on the C-C square -- reproduces the (1,p) bidegree
# but freezes the trace t = 2.
# --------------------------------------------------------------------------

def _seg_cross(u, v):
    """Mixed area of segments [0,u], [0,v] = |u x v| / 2 (segments have zero area)."""
    return 0.5 * abs(u[0] * v[1] - u[1] * v[0])


def part_B(p=5):
    print("=" * 78)
    print(f"PART B -- the divisor shadow {{e,f,Delta,Gamma}} on the C-C square (slope p={p})")
    print("via mixed area of edge-direction segments. Fr_{1,p}=diag(1,p) sends the")
    print("diagonal (slope 1) to slope p -- the (1,p) bidegree of 2Q.")
    print("=" * 78)
    dirs = {"e": (1, 0), "f": (0, 1), "Delta": (1, 1), "Gamma": (1, p)}
    names = list(dirs)
    n = len(names)
    # Intersection numbers = 2 * mixed area (normalize so e.f = 1).
    M = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            M[i, j] = 2.0 * _seg_cross(dirs[names[i]], dirs[names[j]])
    print("  shadow intersection numbers (2 x mixed area, e.f normalized to 1):")
    for i, ni in enumerate(names):
        row = "  ".join(f"{nj}.{ni}={M[i, j]:.0f}" for j, nj in enumerate(names))
        print(f"    {row}")
    # The bidegree {Gamma.e, Gamma.f} and the trace-carrying Delta.Gamma.
    ge, gf = M[names.index("Gamma"), names.index("e")], M[names.index("Gamma"), names.index("f")]
    dg = M[names.index("Delta"), names.index("Gamma")]
    print(f"  bidegree {{Gamma.e, Gamma.f}} = {{{ge:.0f}, {gf:.0f}}}  (2Q's {{1,p}}, but ORIENTATION SWAPPED:")
    print(f"     the shadow Gram equals the function-field Gram ff_gram(p,t=2,g=1) with e<->f.)")
    print(f"  Delta.Gamma (shadow) = {dg:.0f};  function-field = q+1-t = {p + 1} - t.")
    print(f"  => shadow = ({p}+1) - t at t={p + 1 - dg:.0f}: NOT an independent recovery, a relabeled t=2 slice.")
    pos, zero, neg, w = signature(M)
    print(f"  shadow Gram signature (pos, zero, neg) = ({pos}, {zero}, {neg})")
    print(f"  ROBUST KEY (not the value t=2, which is the edge-segment representative): the")
    print(f"       mixed-area form has NO free real parameter t, so it can never be the")
    print(f"       continuum q+1-t. It is t-BLIND -- cannot see which curve. RH is invisible.\n")
    return dict(bidegree=(ge, gf), delta_gamma_shadow=dg, frozen_t=p + 1 - dg,
                signature=(pos, zero, neg))


# --------------------------------------------------------------------------
# Part C: the genuine function-field Gram (2G) -- needs t, gives Hasse-Weil = RH.
# --------------------------------------------------------------------------

def ff_gram(q, t, g=1):
    """Intersection Gram on {e, f, Delta, Gamma_Frob} in NS(C x C) (cf. 2G/2Q).

    e.e=f.f=0, e.f=1, e.Delta=f.Delta=1, Delta.Delta=2-2g,
    Gamma.e=1, Gamma.f=q, Delta.Gamma = #C(F_q) = q+1-t, Gamma.Gamma = q(2-2g).
    """
    d2 = 2 - 2 * g
    return np.array([
        [0, 1, 1, 1],
        [1, 0, 1, q],
        [1, 1, d2, q + 1 - t],
        [1, q, q + 1 - t, q * d2],
    ], dtype=float)


def part_C(p=5):
    print("=" * 78)
    print(f"PART C -- the genuine function-field Gram (2G), q={p}: needs t, gives Hasse-Weil")
    print("=" * 78)
    q = p
    # Sweep t over the Hasse-Weil window |t| < 2 sqrt(q) (genus 1) and outside it.
    import math
    bound = 2 * math.sqrt(q)
    print(f"  Hasse-Weil window (g=1): |t| < 2 sqrt(q) = {bound:.3f}")
    rows = []
    for t in range(-int(bound) - 2, int(bound) + 3):
        G = ff_gram(q, t, g=1)
        pos, zero, neg, w = signature(G)
        # primitive (orthogonal complement of the hyperbolic {e,f}) negative-definiteness:
        # the full signature is (1,3) exactly when |t| < 2 sqrt(q) (RH for the curve).
        rh_ok = abs(t) < bound
        sig_ok = (pos == 1 and neg == 3)
        flag = "RH-window" if rh_ok else "OUTSIDE"
        match = "sig(1,3)" if sig_ok else f"sig({pos},{neg})"
        rows.append((t, rh_ok, sig_ok))
        print(f"    t={t:+d}  |t|<2sqrt(q): {str(rh_ok):<5}   {match:<10} [{flag}]")
    agree = all((rh == sg) for (_, rh, sg) in rows)
    print(f"  signature(1,3)  <=>  |t| < 2 sqrt(q)  for every t tested: {agree}")
    print("  => the function-field Hodge index REQUIRES the trace t; it is the RH content.")
    print("     The tropical shadow (Part B) froze t and is therefore RH-blind.\n")
    return dict(hasse_weil_bound=bound, signature_tracks_RH=agree)


# --------------------------------------------------------------------------
# Part D: K2 (Davenport-Heilbronn) -- no Euler product => no (1,p) bidegree => no shadow.
# --------------------------------------------------------------------------

def part_D():
    print("=" * 78)
    print("PART D -- K2 (Davenport-Heilbronn): the shadow construction does not start")
    print("=" * 78)
    print("  The shadow needs a Frobenius slope p at each place (the (1,p) bidegree, 2Q),")
    print("  which IS the local Euler factor (1 - p^{-s})^{-1}. Davenport-Heilbronn has a")
    print("  functional equation but NO Euler product, so its von Mangoldt analogue")
    print("  delocalizes off prime powers (#20) -- there are no clean per-place local")
    print("  degrees to form a Gamma_p polygon. So there is no tropical shadow for D-H at")
    print("  all: no Gamma_S, no surface (2Q/#25). The mixed-volume route is automatically")
    print("  K2-clean -- it cannot even be set up for the wrong-approach detector.\n")
    return dict(dh_has_shadow=False)


def run():
    if not _HAVE_SCIPY:
        raise SystemExit("scipy required (scipy.spatial.ConvexHull)")
    print("2CC -- tropical (mixed-volume) shadow of the Hodge index on the Connes-Consani square")
    print("Direction 8 / the product surface. Does the free Alexandrov-Fenchel signature")
    print("carry the arithmetic (the Frobenius trace t)? Prediction: NO (t frozen).\n")
    A = part_A()
    B = part_B(p=5)
    C = part_C(p=5)
    D = part_D()

    print("=" * 78)
    print("SYNTHESIS (ADVERSARY-checked, softened)")
    print("=" * 78)
    print("  (A) A canonical Lorentzian convex-geometry form (AF/Teissier-Khovanskii mixed")
    print("      Hodge index) exists for free on the C-C square's Minkowski structure -- but it")
    print("      takes NO arithmetic input, so it is RH-agnostic VACUOUSLY (trivial extreme of")
    print("      the #38/#39 soft-positivity pattern). It is a PROPOSED shadow (toric-BKK")
    print("      analogy), NOT a constructed intersection theory of the char-1 topos.")
    print("  (B) The divisor shadow = the function-field Gram at the single point t=2 (e<->f")
    print("      swapped), genus 1 only. Robust content: the mixed form is t-BLIND (no free")
    print("      real parameter), so it can never be the continuum q+1-t.")
    print("  (C) The function-field Hodge index REQUIRES t: sig(1,3) <=> |t|<2g sqrt(q) = RH-for-C.")
    print("      So the shadow's (1,3) is UNCONDITIONAL (RH-agnostic): passing it != RH.")
    print("  (D) K2: D-H has no Euler product => no (1,p) bidegree => no shadow (clean).")
    print()
    print("  RECONCILES with the reading note ('the signed pairing does not exist'): the")
    print("  RH-AGNOSTIC convex-geometry shadow exists for free; the ARITHMETIC signed pairing")
    print("  carrying the trace t does NOT. GAP SHARPENED, not closed: the RH content is the")
    print("  trace t, lost in the idempotent/tropical structure; the missing object is the")
    print("  arithmetic q-LIFT that restores t (the 'suitable Weil cohomology' C-C name), with")
    print("  the (1,p) bidegree the locus where the lift must inject t.")

    np.savez(
        HERE / "e2cc_tropical_shadow.npz",
        partA_sig=np.array(A["signature"]), partA_eigs=np.array(A["eigs"]),
        partB_bidegree=np.array(B["bidegree"]), partB_frozen_t=B["frozen_t"],
        partC_hasse_weil=C["hasse_weil_bound"], partC_tracks=C["signature_tracks_RH"],
    )
    _plot(A, B, C)
    print(f"\nSaved: {HERE / 'e2cc_tropical_shadow.npz'} and e2cc_tropical_shadow.png")
    return dict(A=A, B=B, C=C, D=D)


def _plot(A, B, C):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        import math
    except Exception as exc:  # pragma: no cover
        print(f"(plot skipped: {exc})")
        return
    fig, ax = plt.subplots(1, 1, figsize=(9, 6))
    # FF signature-tracks-RH picture: plot the min eigenvalue of the primitive block
    # (or simply the (1,3)-vs-not flag) against t, with the Hasse-Weil window shaded.
    q = 5
    bound = 2 * math.sqrt(q)
    ts = list(range(-7, 8))
    nneg = []
    for t in ts:
        pos, zero, neg, w = signature(ff_gram(q, t, g=1))
        nneg.append(neg)
    ax.axvspan(-bound, bound, alpha=0.15, color="tab:green", label="Hasse-Weil window |t|<2sqrt(q) (RH-for-C)")
    ax.plot(ts, nneg, "o-", color="tab:blue", label="# negative eigenvalues of FF Gram")
    ax.axhline(3, color="gray", ls="--", lw=0.8, label="sig (1,3)")
    ax.axvline(B["frozen_t"], color="tab:red", ls=":", lw=2,
               label=f"tropical shadow freezes t={B['frozen_t']} (t-blind)")
    ax.set_xlabel("Frobenius trace t")
    ax.set_ylabel("# negative eigenvalues (FF intersection Gram)")
    ax.set_title("Function-field Hodge index needs the trace t (sig(1,3) <=> RH-for-C);\n"
                 "the C-C tropical mixed-volume shadow freezes t -> RH-blind (Direction 8 gap)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(HERE / "e2cc_tropical_shadow.png", dpi=130)
    plt.close(fig)


if __name__ == "__main__":
    run()
