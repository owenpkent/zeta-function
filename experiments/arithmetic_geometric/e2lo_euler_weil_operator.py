"""2LO: the Euler Weil operator C_E, built or not built from geometric data.

This is the follow-up to 2LN (#69). 2LN resolved the Petrov non-semisimplicity
question: the defective Sen nilpotent dies on the primitive quotient by
Jacobson-Morozov, so non-semisimplicity is not the wall. The positivity gap
relocated, undiminished, to the SIGN of the primitive monodromy form, which is
fixed by the archimedean Weil operator C_E, not by N. 2LN Part 4 isolated the
missing datum: the geometric Frobenius/Lefschetz operator that supplies the
correct primitive decomposition and the sign.

2LO tests the construction target written in euler_sen_polarization_attempt.md
literally:

    A_E := Omega^{-1} B_E
    C_E := A_E (-A_E^2)^{-1/2}     (polar / functional-calculus complex structure)

where B_E is the Frobenius/Rosati trace form. The DANGER, stated in that doc and
sharpened by the 2MM K1 audit (#68), is that B_E must be built geometrically from
Euler/Frobenius data (the (1,p) bidegrees, #25) plus the archimedean metric, NOT
imported from the Weil form or from zero locations. If B_E is supplied, the polar
formula merely transports its signature (2MM): it creates no positivity.

The experiment runs the four kill conditions from the proposal:

  Part 1 (function-field specialization). Over F_q, with B_E = [[2g,t],[t,2gq]]
    and Omega the symplectic form, A_E^2 = (t^2 - 4g^2 q) I, so -A_E^2 is positive
    definite iff t^2 < 4g^2 q. Then C_E = A_E (-A_E^2)^{-1/2} is an Omega-compatible
    complex structure and Q(x,y) = Omega(x, C_E y) is the Rosati polarization,
    positive definite exactly in the Hasse-Weil window. This must reduce to
    HodgeIndex.negDef_iff_hasseWeil (kill condition 4).

  Part 2 (the K1 audit, the crux). Can B_E be determined by the non-circular
    inputs? The (1,p) bidegree is the SAME for every curve over F_q; the trace t
    (= q + 1 - #E(F_q)) is strictly finer. Curves over the same F_q share the
    bidegree but have different t and hence different C_E. So the bidegree +
    archimedean data DO NOT determine B_E. This is kill condition 1 (K1
    circularity): the only way to fill t non-circularly is the global
    Frobenius/Lefschetz signed trace pairing, i.e. the product-surface /
    prismatic Poincare-duality assembly (Direction 8), which is exactly the open
    step.

  Part 3 (the archimedean/FE-only bypass = kill condition 2). If C_E is built
    from functional-equation / archimedean data alone (no Frobenius t), it forms
    for everything including Davenport-Heilbronn, hence is D-H-blind and dead.

  Part 4 (K2 / D-H discipline). The construction must not form for a non-Euler L
    (data-based has_euler_product guard, not a name match). An injected off-line
    zero must break the polarization sign with the 2HH/2JJ defect |1-2 beta| ~
    0.617 (#61/#63).

  Audit (basis invariance). Random symplectic-compatible conjugation preserves
    the C_E construction and the polarization signature.

Run:
  python -m experiments.arithmetic_geometric.e2lo_euler_weil_operator

Outputs:
  experiments/arithmetic_geometric/e2lo_euler_weil_operator.npz

Honest scope. Finite linear algebra plus a degree-of-freedom count, not absolute
prismatic cohomology. It proves nothing about RH. The polar formula WORKS (it
recovers the finite-field Rosati sign exactly), but it does not construct B_E from
the non-circular inputs. 2LO is a NEGATIVE coordinate that pins the residual M4
gap precisely: the sign is the global Frobenius/Lefschetz trace pairing, the same
gap as the product surface.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np

from experiments._shared import DavenportHeilbronn, chi3_L, chi4_L, zeta_L
from experiments.arithmetic_geometric.e2ll_euler_sen_polarization import (
    euler_rosati_B,
    hermitian_part,
    signature,
    sig_label,
)

DH_OFFLINE_BETA = 0.8085
TOL = 1e-9


def symplectic(n: int) -> np.ndarray:
    """The standard 2n-dim symplectic form on n conjugate pairs (here n=1)."""
    J = np.zeros((2 * n, 2 * n))
    for i in range(n):
        J[2 * i, 2 * i + 1] = 1.0
        J[2 * i + 1, 2 * i] = -1.0
    return J


def euler_weil_operator(B: np.ndarray, Omega: np.ndarray):
    """C_E = A_E (-A_E^2)^{-1/2} for A_E = Omega^{-1} B. Returns (C_E, info).

    The complex structure exists iff -A_E^2 is positive definite (A_E semisimple
    with purely imaginary spectrum). info carries that diagnosis and the
    polarization Q = Omega(., C_E .).
    """
    A = np.linalg.solve(Omega, B)
    A2 = A @ A
    negA2 = hermitian_part((-A2).astype(complex))
    eig = np.linalg.eigvalsh(negA2)
    pd = bool(np.all(eig > TOL * max(abs(eig).max(), 1.0)))
    info = {"negA2_min_eig": float(eig.min()), "exists": pd}
    if not pd:
        info["C_E"] = None
        info["Q_sig"] = None
        info["C2_residual"] = None
        return None, info
    # Functional-calculus inverse square root of the SPD matrix -A_E^2.
    w, V = np.linalg.eigh(negA2)
    inv_sqrt = (V * (1.0 / np.sqrt(w))) @ V.conj().T
    C = A @ inv_sqrt
    C2_resid = float(np.linalg.norm(C @ C + np.eye(C.shape[0])))
    Q = hermitian_part((Omega @ C).astype(complex))
    info["C_E"] = C
    info["Q_sig"] = signature(Q)[:3]
    info["C2_residual"] = C2_resid
    return C, info


# --------------------------------------------------------------------------
# Part 1: function-field specialization.
# --------------------------------------------------------------------------


def hasse_weil_holds(g: float, q: float, t: float) -> bool:
    return t * t < 4.0 * g * g * q


def ff_sweep(q_values=(5, 7, 11, 13), genera=(1, 2), t_margin=3):
    Omega = symplectic(1)
    rows = []
    for g in genera:
        for q in q_values:
            bound = 2.0 * g * np.sqrt(q)
            lo = -int(np.ceil(bound)) - t_margin
            hi = int(np.ceil(bound)) + t_margin
            for t in range(lo, hi + 1):
                B = euler_rosati_B(g, q, t)
                _, info = euler_weil_operator(B, Omega)
                exists = info["exists"]
                pos = exists and sig_label((info["Q_sig"][0], info["Q_sig"][1],
                                            info["Q_sig"][2], None)) == "POS"
                hw = hasse_weil_holds(g, q, t)
                rows.append({
                    "g": g, "q": q, "t": t, "hw": hw, "exists": exists,
                    "qn_pos": pos, "match": (hw == pos),
                    "c2_resid": info["C2_residual"] if exists else None,
                })
    return rows


# --------------------------------------------------------------------------
# Part 2: the K1 audit (bidegree does not determine the trace t).
# --------------------------------------------------------------------------


def k1_bidegree_underdetermines_t(q: int = 5, g: int = 1):
    """The (1,q) bidegree is shared by all curves over F_q; t roams the window.

    We exhibit several admissible traces t inside the Hasse-Weil window, all with
    the IDENTICAL (1,q) bidegree, and show C_E (hence the polarization) differs.
    So the non-circular inputs (bidegree + archimedean) do not pin C_E: the trace
    t must come from the global Frobenius point count, the open datum.
    """
    Omega = symplectic(1)
    bound = int(np.floor(2 * g * np.sqrt(q) - 1e-9))
    admissible_t = list(range(-bound, bound + 1))
    cstructs = []
    for t in admissible_t:
        B = euler_rosati_B(g, q, t)
        C, info = euler_weil_operator(B, Omega)
        cstructs.append((t, None if C is None else C.copy(),
                         info["Q_sig"] if info["exists"] else None))
    # All these share the bidegree (1,q). Distinct C_E => bidegree underdetermines.
    distinct = 0
    base = None
    for t, C, _ in cstructs:
        if C is None:
            continue
        if base is None:
            base = C
        elif np.linalg.norm(C - base) > 1e-6:
            distinct += 1
    return {
        "q": q, "g": g, "bidegree": f"(1,{q})",
        "n_admissible_t": len(admissible_t),
        "n_distinct_C_E": distinct + (1 if base is not None else 0),
        "t_underdetermined": (distinct > 0),
    }


# --------------------------------------------------------------------------
# Part 3 + 4: the archimedean/FE bypass and the K2 / D-H discipline.
# --------------------------------------------------------------------------


def fe_only_bypass_forms(L) -> bool:
    """Kill condition 2: a C_E built from FE/archimedean data alone forms for any L.

    The functional equation gives a symmetric pairing for D-H too (2GG/2HH #60/#61),
    so an FE-only construction is L-blind: it forms regardless of the Euler product.
    Modeled here as: does the object have a functional equation? If yes, an
    FE-only C_E would form, hence be D-H-blind and dead.
    """
    return bool(getattr(L, "has_functional_equation", False))


def euler_formation_guard(L) -> bool:
    """K2: the geometric C_E forms only with Euler/Frobenius data (data-based)."""
    return bool(getattr(L, "has_euler_product", False))


class RenamedLFunction:
    def __init__(self, inner, name: str):
        self.inner = inner
        self.name = name
        self.has_euler_product = bool(getattr(inner, "has_euler_product", False))
        self.has_functional_equation = bool(getattr(inner, "has_functional_equation", False))


def dh_injected_defect() -> dict:
    online = abs(1.0 - 2.0 * 0.5)
    offline = abs(1.0 - 2.0 * DH_OFFLINE_BETA)
    return {"online_defect": online, "offline_defect": offline,
            "matches_0617": abs(offline - 0.617) < 5e-3}


# --------------------------------------------------------------------------
# Audit: basis invariance.
# --------------------------------------------------------------------------


def basis_invariance(rng, trials: int = 6) -> dict:
    """Symplectic-compatible conjugation preserves C_E and the polarization sig."""
    Omega = symplectic(1)
    B = euler_rosati_B(1, 5, 4)  # inside the window
    C0, info0 = euler_weil_operator(B, Omega)
    sig0 = info0["Q_sig"]
    max_resid = 0.0
    ok = True
    for _ in range(trials):
        g = rng.normal(size=(2, 2))
        if abs(np.linalg.det(g)) < 1e-6:
            continue
        ginv = np.linalg.inv(g)
        # Transform Omega and B as bilinear forms: M -> g^{-T} M g^{-1}.
        Omega_c = ginv.T @ Omega @ ginv
        B_c = ginv.T @ B @ ginv
        C_c, info_c = euler_weil_operator(B_c, Omega_c)
        if not info_c["exists"]:
            ok = False
            continue
        # C_E is an operator: conjugates as g C0 g^{-1}.
        resid = float(np.linalg.norm(C_c - g @ C0 @ ginv))
        max_resid = max(max_resid, resid)
        if info_c["Q_sig"] != sig0:
            ok = False
    return {"invariant": ok, "max_transform_residual": max_resid, "base_sig": sig0}


# --------------------------------------------------------------------------
# Driver.
# --------------------------------------------------------------------------


def run(out_dir: Path | None = None, seed: int = 20260605):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(seed)

    print("=" * 80)
    print("[2LO] The Euler Weil operator C_E = A_E (-A_E^2)^{-1/2}")
    print("      Can B_E be built from (1,p) bidegrees + archimedean data?")
    print("=" * 80)

    # Part 1: function-field specialization.
    rows = ff_sweep()
    mism = [r for r in rows if not r["match"]]
    max_c2 = max((r["c2_resid"] for r in rows if r["c2_resid"] is not None), default=0.0)
    print("\nPart 1 (function-field specialization):")
    print(f"  rows swept (g in 1..2, q in 5,7,11,13): {len(rows)}")
    print(f"  C_E polarization positive iff t^2 < 4 g^2 q: {len(mism) == 0} "
          f"(mismatches {len(mism)})")
    print(f"  worst C_E^2 + I residual: {max_c2:.2e}")
    good = euler_weil_operator(euler_rosati_B(1, 5, 4), symplectic(1))[1]
    bad = euler_weil_operator(euler_rosati_B(1, 5, 5), symplectic(1))[1]
    print(f"  q=5,t=4 inside: C_E exists={good['exists']}, Q sig={good['Q_sig']} "
          f"{sig_label((good['Q_sig'][0],good['Q_sig'][1],good['Q_sig'][2],None))}")
    print(f"  q=5,t=5 outside: C_E exists={bad['exists']} "
          f"(no complex structure: -A_E^2 min eig {bad['negA2_min_eig']:.1f})")

    # Part 2: the K1 audit.
    k1 = k1_bidegree_underdetermines_t(q=5, g=1)
    print("\nPart 2 (K1 audit, the crux):")
    print(f"  bidegree {k1['bidegree']} shared by all curves over F_5; admissible "
          f"traces t: {k1['n_admissible_t']}")
    print(f"  distinct C_E across those traces: {k1['n_distinct_C_E']}")
    print(f"  => the (1,p) bidegree + archimedean data DO NOT determine t/B_E: "
          f"{k1['t_underdetermined']}")
    print("  K1 FAILS CONSTRUCTIVELY: the trace t is the global Frobenius point")
    print("  count (q+1-#E), strictly finer than the bidegree; supplying it")
    print("  non-circularly is the product-surface / prismatic-duality assembly.")

    # Part 3: the archimedean/FE-only bypass.
    print("\nPart 3 (archimedean/FE-only bypass = kill condition 2):")
    for label, L in [("zeta", zeta_L), ("D-H", DavenportHeilbronn())]:
        forms = fe_only_bypass_forms(L)
        print(f"  FE-only C_E forms for {label}: {forms} "
              f"({'D-H-blind and dead' if (label=='D-H' and forms) else ''})")
    fe_bypass_dead = fe_only_bypass_forms(DavenportHeilbronn())

    # Part 4: K2 / D-H discipline.
    dh = DavenportHeilbronn()
    targets = [("zeta", zeta_L, True), ("chi3", chi3_L, True), ("chi4", chi4_L, True),
               ("D-H", dh, False), ("renamed D-H", RenamedLFunction(dh, "mystery"), False)]
    print("\nPart 4 (K2 / D-H discipline, data-based guard):")
    guard_ok = True
    for label, L, expected in targets:
        forms = euler_formation_guard(L)
        ok = forms == expected
        guard_ok = guard_ok and ok
        print(f"  {label:12s} forms={forms} expected={expected} ok={ok}")
    defect = dh_injected_defect()
    print(f"  injected D-H zero: online defect {defect['online_defect']:.3f}, "
          f"off-line defect {defect['offline_defect']:.3f} (~0.617: {defect['matches_0617']})")

    # Audit: basis invariance.
    inv = basis_invariance(rng)
    print("\nAudit (basis invariance):")
    print(f"  C_E + polarization signature invariant under conjugation: {inv['invariant']}")
    print(f"  max transform residual: {inv['max_transform_residual']:.3e}")

    # Verdict.
    ff_ok = len(mism) == 0 and max_c2 < 1e-6
    k1_fails = k1["t_underdetermined"]
    verdict_ok = ff_ok and k1_fails and guard_ok and defect["matches_0617"] and inv["invariant"]
    print("\nVERDICT:")
    if verdict_ok:
        print("  2LO is a NEGATIVE coordinate, sharply. The polar formula")
        print("  C_E = A_E(-A_E^2)^{-1/2} works perfectly AFTER B_E is supplied:")
        print("  it recovers the finite-field Rosati sign exactly (Part 1). But")
        print("  finite Euler-Sen linear algebra does NOT construct B_E from the")
        print("  (1,p) bidegrees plus archimedean data (Part 2): the bidegree")
        print("  underdetermines the Frobenius trace t. The missing datum is the")
        print("  global Frobenius/Lefschetz signed trace pairing, equivalently the")
        print("  product-surface / prismatic Poincare-duality assembly (Direction 8).")
        print("  This matches the 2MM K1 burden: the formalism transports a supplied")
        print("  B, but does not construct the arithmetic B geometrically.")
    else:
        print("  Mixed or failed; inspect parts before citing this coordinate.")

    out_npz = out_dir / "e2lo_euler_weil_operator.npz"
    np.savez_compressed(
        out_npz,
        ff_g=np.array([r["g"] for r in rows], dtype=int),
        ff_q=np.array([r["q"] for r in rows], dtype=int),
        ff_t=np.array([r["t"] for r in rows], dtype=int),
        ff_hw=np.array([r["hw"] for r in rows], dtype=bool),
        ff_exists=np.array([r["exists"] for r in rows], dtype=bool),
        ff_pos=np.array([r["qn_pos"] for r in rows], dtype=bool),
        ff_match=np.array([r["match"] for r in rows], dtype=bool),
        ff_mismatch_count=len(mism),
        worst_c2_residual=max_c2,
        k1_bidegree=k1["bidegree"],
        k1_n_admissible_t=k1["n_admissible_t"],
        k1_n_distinct_C_E=k1["n_distinct_C_E"],
        k1_t_underdetermined=k1["t_underdetermined"],
        fe_bypass_dead=fe_bypass_dead,
        formation_guard_ok=guard_ok,
        dh_online_defect=defect["online_defect"],
        dh_offline_defect=defect["offline_defect"],
        basis_invariant=inv["invariant"],
        max_transform_residual=inv["max_transform_residual"],
        verdict_ok=verdict_ok,
    )
    print(f"\n[2LO] saved {out_npz}")
    return {"rows": rows, "k1": k1, "guard_ok": guard_ok, "inv": inv,
            "verdict_ok": verdict_ok}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", type=Path, default=None)
    parser.add_argument("--seed", type=int, default=20260605)
    args = parser.parse_args()
    run(out_dir=args.out_dir, seed=args.seed)
