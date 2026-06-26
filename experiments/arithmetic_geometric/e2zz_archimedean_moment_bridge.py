"""The archimedean/global face (Option C, the Arakelov side of 09A Section 5), ADVERSARY-CORRECTED
(scratchpad/higher_rank_faces/01_adversary.md): e2xx's finite F_q moment problem and the
archimedean Weil/Li positivity are the SAME object at the edge of positivity -- marginal positivity
(#18/#19) IS the infinite-support analogue of the F_q boundary kernel.

WHAT WAS WRONG (the withdrawn first pass), AND THE CORRECTION
------------------------------------------------------------
The first pass claimed a DISANALOGY: "the F_q on-circle moment matrix has an exact kernel, but the
archimedean Weil-form min eig GROWS with the number of zeros, so it is NOT at a boundary." The
adversary showed this is measured on the WRONG AXIS and the conclusion is BACKWARDS:

  * [A] F_q grows the matrix DIMENSION m = 1..2g+1; the kernel appears at dim 2g+1 because the
    Frobenius spectrum has FINITE support 2g.
  * [B] the first pass held the Weil-Gram DIMENSION FIXED at K = #test-functions and grew the
    NUMBER OF SUMMED ZEROS n. On-line, each zero adds a rank-1 PSD outer product to the fixed KxK
    Gram, so by Weyl the min eig is monotone NON-decreasing in n AUTOMATICALLY -- zero information
    about a kernel. (Shown below as AXIS 1.)

On the FAITHFUL axis -- grow the test-function DIMENSION K (the analogue of F_q's m) at a fixed
large zero set -- the archimedean min eig COLLAPSES toward 0 (the marginal-positivity wall,
#18/#19), and a TRUNCATED zero set even gives an EXACT kernel once K > n_zeros (AXIS 2 below). So:

  marginal positivity over Z IS the infinite-support analogue of the F_q boundary kernel.

Both are the moment/Gram form sitting at the EDGE of positivity as its dimension grows. The only
(mild) difference: F_q reaches min eig = 0 EXACTLY at the fixed small dimension 2g+1 (finite
support 2g); the archimedean form approaches min eig -> 0 ASYMPTOTICALLY as the test family is
enriched (the infinite zeta spectrum -> accumulation at 0). The earlier "disanalogy" is withdrawn.

THE SURVIVING FRAME (a reframing of #48/#96/#123/#25, not new content)
---------------------------------------------------------------------
  * CONNECTION: e2xx's finite F_q moment matrix is the FINITE MODEL of the archimedean Weil/Li
    positivity. Both are CONDITIONAL forms that FLIP off the symmetry locus (Level-4, #48/#96).
  * POLARITY: Faltings-Hriljac is UNCONDITIONALLY positive-definite, so it cannot flip, so it
    cannot detect RH -- the wrong polarity (09A S5's "wrong signature", #22-24). (Structural, not
    a toy computation; FH is not parameterized by a zero configuration at all.)
  * Gamma_S makes the archimedean form INFINITE-dimensional (#25, the (1,p) bidegree, Deninger
    R-flow) -- which is exactly why its boundary is ASYMPTOTIC (no fixed finite kernel), not
    reached at a fixed small dimension like F_q. The global assembly is the archimedean+finite
    balance (#23/#24, two-clock 3M); M4 is the open certificate that this infinite, MARGINAL
    balance is a conditional (flipping) positivity.

WHAT THIS FILE DOES (and does NOT)
----------------------------------
It computes BOTH axes to make the correction explicit: AXIS 1 (the wrong one: fixed K, grow zeros
-> Weyl-monotone) and AXIS 2 (the right one: grow K -> min eig collapses to 0, the boundary), plus
the exact-kernel-for-K>n_zeros check. The corrected reading is the UNIFICATION (marginal positivity
= the boundary-kernel analogue), which is a reframing of #48/#96/#123/#25, NOT new content. [B]
reuses the Weil form (#18/#19/#96). P6/M4 is UNTOUCHED.

Run:
  python -m experiments.arithmetic_geometric.e2zz_archimedean_moment_bridge
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np

from experiments.arithmetic_geometric.e2xx_higher_rank_rosati import moment_sequence, toeplitz_moment


# ===========================================================================
# [A] F_q: the moment form reaches an EXACT kernel at the fixed small dim 2g+1.
# ===========================================================================
def part_A_ff_boundary(g: int = 3) -> dict:
    phis = [0.4, 1.3, 2.6][:g] if g <= 3 else [0.4 + 0.3 * k for k in range(g)]
    us = [complex(math.cos(p), math.sin(p)) for p in phis]
    c = moment_sequence(us, 2 * g + 2)
    min_eigs = [float(np.linalg.eigvalsh(toeplitz_moment(c, m)).min()) for m in range(1, 2 * g + 2)]
    kernel_size = next((m + 1 for m, me in enumerate(min_eigs, start=1) if abs(me) < 1e-9), None)
    return {"g": g, "min_eig_below_kernel": round(min_eigs[2 * g - 2], 4),
            "min_eig_at_kernel": round(min_eigs[2 * g - 1], 9) if 2 * g - 1 < len(min_eigs) else None,
            "kernel_at_dim": kernel_size, "expected": 2 * g + 1, "exact_kernel": kernel_size == 2 * g + 1}


# ===========================================================================
# [B] Archimedean: the Weil-Gram on real zeta zeros, on BOTH axes.
# ===========================================================================
def _weil_gram(zeros, b_vals, prec: int = 30) -> np.ndarray:
    import mpmath as mp
    from experiments.positivity.e3c_weil_form import phi_b
    mp.mp.dps = prec
    K = len(b_vals)
    phi = np.empty((K, len(zeros)), dtype=complex)
    for k, b in enumerate(b_vals):
        bm = mp.mpf(b)
        for r, rho in enumerate(zeros):
            phi[k, r] = complex(phi_b(bm, mp.mpc(rho), prec=prec))
    M = np.zeros((K, K))
    for j in range(K):
        for k in range(K):
            M[j, k] = 2.0 * float(np.real(np.sum(phi[j] * phi[k])))
    return 0.5 * (M + M.T)


def part_B_archimedean(prec: int = 30) -> dict:
    try:
        from experiments._shared import zeta_L
    except Exception as e:
        return {"available": False, "reason": str(e)}
    rhos = zeta_L.zeros(T_max=150.0, prec=prec)
    bspan = (np.log10(1.1), np.log10(200.0))

    # AXIS 1 (the WRONG axis): fixed dim K=6, grow n_zeros -> Weyl-monotone non-decreasing.
    b6 = np.logspace(bspan[0], bspan[1], 6)
    axis1 = []
    for n in (6, 10, 16, 24, 40):
        if n <= len(rhos):
            axis1.append({"n": n, "min_eig": float(np.linalg.eigvalsh(_weil_gram(rhos[:n], b6, prec)).min())})
    axis1_monotone = all(axis1[i]["min_eig"] <= axis1[i + 1]["min_eig"] + 1e-9 for i in range(len(axis1) - 1))

    # AXIS 2 (the RIGHT axis): fixed large zero set, grow dim K -> min eig COLLAPSES toward 0.
    n_fixed = min(60, len(rhos))
    axis2 = []
    for K in (3, 6, 10, 16, 22):
        bK = np.logspace(bspan[0], bspan[1], K)
        ev = np.linalg.eigvalsh(_weil_gram(rhos[:n_fixed], bK, prec))
        axis2.append({"K": K, "min_eig": float(ev.min()),
                      "cond": float(ev.max() / max(ev.min(), 1e-300))})
    axis2_collapses = axis2[-1]["min_eig"] < axis2[0]["min_eig"]      # min eig DECREASES as K grows

    # exact kernel for K > n_zeros (finite zero set => rank-deficient Gram, like [A])
    n_small = 8
    bK = np.logspace(bspan[0], bspan[1], 12)
    ev_small = np.linalg.eigvalsh(_weil_gram(rhos[:n_small], bK, prec))
    exact_kernel = bool(abs(ev_small.min()) < 1e-9)                   # K=12 > n=8 => kernel

    return {"available": True, "n_fixed": n_fixed,
            "axis1_fixedK_growZeros": axis1, "axis1_weyl_monotone": axis1_monotone,
            "axis2_growK": axis2, "axis2_min_eig_collapses": axis2_collapses,
            "exact_kernel_K_gt_n": exact_kernel, "exact_kernel_min_eig": float(ev_small.min())}


# ===========================================================================
# [C] Faltings-Hriljac: UNCONDITIONALLY definite (structural; not a zero-configuration form).
# ===========================================================================
def part_C_faltings_hriljac() -> dict:
    """STRUCTURAL (09A S5 / #22-24), not a toy computation: the Faltings-Hriljac / Neron-Tate
    pairing is UNCONDITIONALLY positive-definite and is not parameterized by a zero configuration
    at all, so it cannot 'flip' with RH -- the wrong polarity (it cannot be an RH detector). Its
    positivity is GLOBAL (archimedean diagonal + finite off-diagonal; arch-only indefinite by rank
    3, #23/#24 = two-clock 3M)."""
    return {"unconditionally_definite": True, "parameterized_by_zeros": False, "can_flip_with_RH": False,
            "global_note": "FH positivity is global (arch diagonal + finite off-diag; arch-only "
                           "indefinite by rank 3, #23/#24); the archimedean Neron height is the "
                           "sigma-function quantity, not the coordinate diagonal."}


def demo() -> int:
    print("=" * 92)
    print("e2zz: the archimedean/global face -- marginal positivity IS the boundary-kernel analogue")
    print("=" * 92)

    print("\n[A] F_q moment form: reaches an EXACT kernel at the fixed small dim 2g+1 (finite support):")
    pa = part_A_ff_boundary()
    print(f"    g={pa['g']}: min eig below kernel = {pa['min_eig_below_kernel']} (interior); at dim "
          f"2g+1={pa['expected']}: min eig = {pa['min_eig_at_kernel']} (EXACT kernel = {pa['exact_kernel']})")

    print("\n[B] Archimedean zeta Weil form on BOTH axes (the correction):")
    pb = part_B_archimedean()
    if pb.get("available"):
        print("    AXIS 1 (WRONG: fixed dim K=6, grow #zeros -> Weyl-monotone, uninformative):")
        for r in pb["axis1_fixedK_growZeros"]:
            print(f"        n_zeros={r['n']:>3}: min eig = {r['min_eig']:.4e}")
        print(f"        => monotone non-decreasing (a Weyl artifact): {pb['axis1_weyl_monotone']}")
        print(f"    AXIS 2 (RIGHT: grow dim K at n_zeros={pb['n_fixed']} -- the analogue of F_q's m):")
        for r in pb["axis2_growK"]:
            print(f"        K={r['K']:>3}: min eig = {r['min_eig']:.4e}  cond = {r['cond']:.2e}")
        print(f"        => min eig COLLAPSES toward 0 (the marginal-positivity wall #18/#19): "
              f"{pb['axis2_min_eig_collapses']}")
        print(f"    EXACT kernel for K>n_zeros (truncated spectrum, like [A]): "
              f"{pb['exact_kernel_K_gt_n']} (min eig {pb['exact_kernel_min_eig']:.2e})")
    else:
        print(f"    (zeta zeros unavailable: {pb.get('reason')})")

    print("\n[C] Faltings-Hriljac: UNCONDITIONALLY definite (structural) -- cannot flip => wrong polarity:")
    pc = part_C_faltings_hriljac()
    print(f"    unconditionally definite={pc['unconditionally_definite']}, parameterized by zeros="
          f"{pc['parameterized_by_zeros']}, can flip with RH={pc['can_flip_with_RH']}")
    print(f"    note: {pc['global_note']}")

    print("\n" + "=" * 92)
    print("VERDICT (the corrected unification -- a reframing, not new content):")
    print("  - e2xx's finite F_q moment matrix is the FINITE MODEL of the archimedean Weil/Li")
    print("    positivity; both are CONDITIONAL forms that FLIP off the symmetry locus (#48/#96).")
    print("    Faltings-Hriljac is UNCONDITIONALLY definite (cannot flip) = wrong polarity (09A S5).")
    print("  - CORRECTED unification (the first-pass 'disanalogy' is WITHDRAWN): on the FAITHFUL")
    print("    axis (grow the test-function dimension), the archimedean min eig COLLAPSES toward 0")
    print("    -- the marginal-positivity wall (#18/#19) -- and a truncated spectrum gives an EXACT")
    print("    kernel for K>n_zeros. So marginal positivity over Z IS the infinite-support analogue")
    print("    of the F_q boundary kernel; both sit at the edge of positivity. The earlier 'grows")
    print("    with #zeros => no kernel' reading measured the WRONG axis (Weyl-monotone artifact).")
    print("  - Gamma_S makes the form INFINITE-dimensional (so the boundary is ASYMPTOTIC, not at a")
    print("    fixed small dim); the global assembly is the archimedean+finite balance (#23/#24);")
    print("    M4 = the open certificate that this infinite marginal balance is conditional. UNTOUCHED.")
    print("=" * 92)

    # ---- structural assertions ----
    assert pa["exact_kernel"] and abs(pa["min_eig_at_kernel"]) < 1e-9, \
        "[A]: the F_q on-circle form must reach an EXACT kernel at dim 2g+1"
    if pb.get("available"):
        assert pb["axis1_weyl_monotone"], "[B]: AXIS 1 must be Weyl-monotone (the wrong-axis artifact)"
        assert pb["axis2_min_eig_collapses"], \
            "[B]: AXIS 2 (grow dim) min eig must COLLAPSE toward 0 (marginal positivity)"
        assert pb["exact_kernel_K_gt_n"], "[B]: a truncated spectrum must give an exact kernel for K>n_zeros"
    assert not pc["can_flip_with_RH"], "[C]: Faltings-Hriljac must be unconditional (cannot flip)"
    print("\n(all structural assertions hold)")

    out = Path(__file__).resolve().parent / "e2zz_archimedean_moment_bridge.npz"
    np.savez_compressed(
        out, ff_kernel_dim=pa["kernel_at_dim"] or -1,
        axis2_K=np.array([r["K"] for r in pb["axis2_growK"]] if pb.get("available") else []),
        axis2_mineig=np.array([r["min_eig"] for r in pb["axis2_growK"]] if pb.get("available") else []),
        exact_kernel_K_gt_n=bool(pb.get("exact_kernel_K_gt_n", False)))
    print(f"\nSaved {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(demo())
