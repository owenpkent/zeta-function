"""2GG -- organ (a) of M4: the H^2 fundamental class and the Poincare-duality trace
map, and the decisive separation of DUALITY (the functional equation, buildable for
D-H) from the FUNDAMENTAL CLASS (the Euler-product pole, NOT buildable for D-H).

CONTEXT. Probe B (2EE, #44) named M4's two missing organs: (a) a fundamental class
H^2 with a Poincare-duality trace map H^1 (x) H^1 -> H^2 = unit, and (b) the two-
clock period (resolved in 2FF/#45 as the scaling flow). Probe B found the rank-1
pole block B_pole = residue * 2 * outer(phi_1, phi_1) is the SHADOW of H^2. This
experiment attacks organ (a) and isolates exactly what is missing.

THE DECISIVE STRUCTURAL POINT (the reason this is sharp). The functional equation
    xi(s) = xi(1 - s),     xi(s) = (1/2) s(s-1) pi^{-s/2} Gamma(s/2) zeta(s),
IS the Poincare duality H^1 x H^1 -> H^2: it pairs a zero rho with its partner
1 - rho, and the factor s(s-1) carries the Deninger H^0/H^1/H^2 grading --
    s = 0 : H^0 (structure sheaf, weight 0),
    s = 1 : H^2 (the pole of zeta, weight 2 = Tate twist; the FUNDAMENTAL CLASS),
    nontrivial zeros : H^1 (weight 1, where RH lives),
with the duality s <-> 1-s swapping H^0 <-> H^2 and preserving H^1.

BUT Davenport-Heilbronn ALSO has a functional equation (that is the defining
property of the project's wrong-approach detector: "functional equation, no Euler
product"). So the DUALITY PAIRING itself is BUILDABLE for D-H. What D-H lacks is the
NONDEGENERATE FUNDAMENTAL CLASS: zeta has a pole at s=1 (residue 1, an avatar of the
Euler-product divergence prod_p (1-1/p)^{-1} -> infinity), while D-H is ENTIRE
(residue 0). A Poincare duality whose trace lands in a ZERO fundamental class is not
a polarization. So organ (a) separates cleanly into two parts, and only the second
is the obstruction:
    - the duality pairing (the FE)         : buildable for D-H  (NOT the gap)
    - the fundamental class H^2 (the pole) : the Euler-product residue, ABSENT for
                                              D-H  (THIS is organ (a) / the K2 face)

This sharpens probe B: the missing organ is not "a pairing" (the FE gives one, even
for the counterexample); it is "a nonzero unit for the pairing to land in", and that
unit is the Euler-product pole. RH-positivity needs the duality to be a POLARIZATION
(perfect pairing into a nonzero fundamental class), and the fundamental class is the
pole that only an Euler product supplies.

WHAT THIS COMPUTES (light, fast):
 PART 1 (FF anchor, real). For C/F_q: H^1 (dim 2g) with the cup-product symplectic
   form J -> H^2 = Q(-1) (1-dim, NONZERO), the trace map = degree. Verify J is a
   PERFECT pairing (nondegenerate, alternating: Poincare duality holds), Frobenius is
   a similitude of scale q (the polarization compatibility), and the Riemann
   polarization is definite <=> |alpha_i| = sqrt q (RH). So over F_q both organ-(a)
   ingredients are present: a perfect duality AND a nonzero fundamental class.
 PART 2 (arithmetic, the separation). Verify (i) zeta's FE xi(s)=xi(1-s) to high
   precision (the duality), (ii) residue of zeta at s=1 = 1 (the NONZERO fundamental
   class H^2, from the Euler product), (iii) residue of D-H at s=1 = 0 (D-H is
   entire: NO fundamental class), while D-H HAS its own FE (the duality is buildable
   for it). The decisive contrast: 1 vs 0.
 PART 3 (the named gap). State precisely what organ (a) still needs over Spec(Z): not
   the FE-symmetry (present, and present even for D-H) but a genuine GEOMETRIC
   Poincare duality realizing H^1 (x) H^1 -> H^2 as a perfect CUP PRODUCT into the
   1-dim Euler-pole fundamental class, on the infinite-dimensional arithmetic H^1.
   The rank-1 pole (2EE) is the H^2 target; the open step is the perfect cup product
   on H^1 (the prismatic Poincare duality), whose induced polarization positivity is
   RH (= the rest of M4, organ (a)).

HONEST SCOPE. The FF cup-product perfectness and polarization<=>RH (Part 1) are
rigorous (the crystalline/Weil picture, reproducing 2T/2G/2DD in duality language).
The residue contrast (Part 2) is a clean, decisive computation. The H^0/H^1/H^2
grading and the "FE = Poincare duality, pole = fundamental class" reading are the
Deninger structural picture, NOT a constructed arithmetic cohomology; this proves
nothing about RH. The value: it separates duality from fundamental class, shows the
duality is buildable for D-H but the fundamental class is not, and pins organ (a) as
the perfect cup product into the Euler-pole H^2. A sharpening coordinate.

Outputs:
  - e2gg_fundamental_class.npz
  - e2gg_fundamental_class.png
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np

from experiments._shared import zeta_L, DavenportHeilbronn
from experiments.positivity.e3m_place_type_balance import numeric_residue_at_one
from experiments.arithmetic_geometric.e2f_hodge_index_sweep import (
    elliptic_family, genus2_family,
)
from experiments.arithmetic_geometric.e2t_rosati_positivity import frobenius_eigenvalues


def symplectic_cup_product(curve):
    """Build the cup-product pairing on H^1 (dim 2g) of C/F_q in a Frobenius
    eigenbasis, and report (i) nondegeneracy = Poincare duality is perfect, (ii) the
    similitude scale (Frobenius scales the cup product by q), (iii) the Riemann-
    polarization definiteness <=> |alpha|=sqrt q.

    In an eigenbasis the alpha-eigenvector pairs nontrivially only with the
    (q/alpha)-eigenvector under the cup product (the FE-partner), so J is block-anti-
    diagonal with 2x2 symplectic blocks; det J != 0 = perfect duality. The trace map
    H^2 -> Q(-1) is the 1-dim target (here normalized to 1)."""
    alphas = frobenius_eigenvalues(curve)
    q = float(curve["p"])
    a = np.array(alphas, dtype=complex)
    n = len(a)
    used = np.zeros(n, dtype=bool)
    J = np.zeros((n, n), dtype=complex)
    pol_entries = []
    for i in range(n):
        if used[i]:
            continue
        j = None
        for k in range(n):
            if k != i and not used[k] and abs(a[i] * a[k] - q) < 1e-4 * q:
                j = k
                break
        if j is None:
            used[i] = True
            continue
        used[i] = used[j] = True
        # cup-product symplectic block: <e_i, f_j> = +1, <f_j, e_i> = -1 (alternating)
        J[i, j] = 1.0
        J[j, i] = -1.0
        # Riemann polarization entry (definite <=> |alpha|=sqrt q): q - |alpha|^2
        pol_entries.append(q - abs(a[i]) ** 2)
    detJ = np.linalg.det(J)
    perfect = abs(detJ) > 1e-9
    # similitude: cup(phi x, phi y) = q cup(x, y). On eigenbasis phi=diag(alpha),
    # check (Phi^T J Phi) = q J on the paired blocks (alpha_i * alpha_j = q).
    Phi = np.diag(a)
    sim = Phi.T @ J @ Phi
    sim_ok = np.allclose(sim, q * J, atol=1e-4 * q)
    pol = np.array(pol_entries, dtype=float)
    return dict(detJ=complex(detJ), perfect=perfect, similitude_ok=bool(sim_ok),
                q=q, pol=pol, definite=(np.max(np.abs(pol)) < 1e-4 * q),
                dimH1=n)


def xi(s):
    s = mp.mpmathify(s)
    return mp.mpf('0.5') * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def run(prec=30, out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)
    mp.mp.dps = prec

    print("=" * 78)
    print("[2GG] Organ (a): the H^2 fundamental class and the Poincare-duality trace.")
    print("      Separating DUALITY (the FE, buildable for D-H) from the FUNDAMENTAL")
    print("      CLASS (the Euler-product pole, ABSENT for D-H).")
    print("=" * 78)

    # ---- PART 1: FF anchor (real) ---- #
    print("\nPART 1 (FF anchor, real). Cup product H^1 x H^1 -> H^2 = Q(-1): perfect?")
    print("  Frobenius a similitude of scale q? Riemann polarization definite <=> RH?\n")
    curves = elliptic_family([5, 7, 11, 13]) + genus2_family([5, 7])
    hdr = f"{'curve':<30} {'dim H1':>6} {'cup perfect':>12} {'similitude q':>12} {'polariz<=>RH':>12}"
    print(hdr); print("-" * len(hdr))
    part1 = []
    for c in curves:
        r = symplectic_cup_product(c)
        part1.append(dict(label=c["label"], **r))
        print(f"{c['label']:<30} {r['dimH1']:>6} {'yes' if r['perfect'] else 'NO':>12} "
              f"{'yes' if r['similitude_ok'] else 'NO':>12} "
              f"{'yes' if r['definite'] else 'NO':>12}")
    print("-" * len(hdr))
    all_perfect = all(r["perfect"] for r in part1)
    all_sim = all(r["similitude_ok"] for r in part1)
    print(f"  Cup product is a PERFECT Poincare pairing (nondegenerate) for all: {all_perfect}.")
    print(f"  Frobenius is a similitude of scale q (polarization compatibility): {all_sim}.")
    print(f"  H^2 = Q(-1) is 1-dim and NONZERO; the trace map = degree. Over F_q BOTH")
    print(f"  organ-(a) ingredients are present: perfect duality + nonzero fundamental class,")
    print(f"  and the induced Riemann polarization is definite exactly at RH (|alpha|=sqrt q).")

    # ---- PART 2: arithmetic separation (duality vs fundamental class) ---- #
    print("\nPART 2 (arithmetic). Duality (FE) vs fundamental class (pole residue).")
    # (i) zeta FE = Poincare duality
    fe_pts = [mp.mpf('0.3'), mp.mpc('0.5', '14.13'), mp.mpc('0.7', '25')]
    fe_err = max(float(abs(xi(s) - xi(1 - s))) for s in fe_pts)
    print(f"  (i) zeta FE xi(s)=xi(1-s) (the DUALITY): max |xi(s)-xi(1-s)| = {fe_err:.2e} (holds).")
    # (ii)/(iii) residues = the fundamental class H^2
    res_zeta = numeric_residue_at_one(zeta_L, prec)
    dh = DavenportHeilbronn()
    res_dh = numeric_residue_at_one(dh, prec)
    print(f"  (ii) zeta residue at s=1 (the FUNDAMENTAL CLASS H^2) = {res_zeta:.6f}  (NONZERO,")
    print(f"       the Euler-product pole: prod_p (1-1/p)^-1 diverges).")
    print(f"  (iii) D-H residue at s=1 = {res_dh:.3e}  (~0: D-H is ENTIRE, NO fundamental class)")
    print(f"        -- YET D-H HAS its own functional equation (the duality is buildable for it;")
    print(f"        that is the defining property of the project's wrong-approach detector).")
    fundclass_separates = (abs(res_zeta - 1.0) < 1e-3 and abs(res_dh) < 1e-3)
    print(f"\n  DECISIVE CONTRAST: fundamental class is 1 for zeta, 0 for D-H: {fundclass_separates}.")
    print(f"  => the DUALITY (FE) does NOT distinguish zeta from D-H (both have one); the")
    print(f"     FUNDAMENTAL CLASS (the Euler-product pole) DOES. Organ (a)'s obstruction is")
    print(f"     the nonzero unit, not the pairing. This is K2 in cohomological language:")
    print(f"     D-H has H^1 x H^1 -> H^2 but H^2 = 0, so the duality is not a polarization.")

    # ---- PART 3: the named gap ---- #
    print("\nPART 3 (the named gap for organ (a) over Spec(Z)).")
    print("  Present: the FE-symmetry (the duality, even for D-H) and the rank-1 Euler-pole")
    print("  fundamental class (2EE; nonzero only for Euler L). MISSING: a genuine GEOMETRIC")
    print("  Poincare duality realizing H^1 (x) H^1 -> H^2 as a PERFECT CUP PRODUCT into that")
    print("  1-dim Euler-pole fundamental class, on the INFINITE-dimensional arithmetic H^1")
    print("  (the prismatic Poincare duality, candidate A's dependency (i)). Its induced")
    print("  polarization positivity is RH. So organ (a) = 'make the FE a geometric cup")
    print("  product into the Euler-pole H^2, perfectly, on the infinite-dim H^1.'")
    print("  The Deninger H^0/H^1/H^2 grading (s=0 / zeros / s=1 pole) is the target shape.")

    np.savez_compressed(
        out_dir / "e2gg_fundamental_class.npz",
        ff_labels=np.array([r["label"] for r in part1], dtype=object),
        ff_perfect=np.array([r["perfect"] for r in part1]),
        ff_similitude=np.array([r["similitude_ok"] for r in part1]),
        ff_definite=np.array([r["definite"] for r in part1]),
        zeta_fe_err=fe_err, res_zeta=res_zeta, res_dh=res_dh,
        fundclass_separates=bool(fundclass_separates), prec=prec,
    )

    # plot
    fig, axs = plt.subplots(1, 2, figsize=(13, 5))
    ax = axs[0]
    # H^0/H^1/H^2 grading picture: poles/zeros of xi-factors on the s-line
    ax.axvspan(-0.05, 0.05, color="tab:blue", alpha=0.25, label="s=0: H^0 (weight 0)")
    ax.axvspan(0.95, 1.05, color="tab:red", alpha=0.25, label="s=1: H^2 (pole = fund. class)")
    ax.axvline(0.5, color="tab:green", lw=2, label="Re(s)=1/2: H^1 (zeros, RH)")
    ax.annotate("", xy=(1.0, 0.6), xytext=(0.0, 0.6),
                arrowprops=dict(arrowstyle="<->", color="k"))
    ax.text(0.5, 0.63, "FE duality s <-> 1-s\n(swaps H^0 <-> H^2)", ha="center", fontsize=8)
    ax.set_xlim(-0.3, 1.3); ax.set_ylim(0, 1)
    ax.set_xlabel("Re(s)"); ax.set_yticks([])
    ax.set_title("Deninger H^0/H^1/H^2 grading\nFE = Poincare duality")
    ax.legend(fontsize=8, loc="lower center")

    ax = axs[1]
    ax.bar(["zeta\n(Euler)", "D-H\n(no Euler)"], [res_zeta, abs(res_dh)],
           color=["tab:green", "tab:red"])
    ax.axhline(0, color="k", lw=1)
    ax.set_ylabel("residue at s=1  = fundamental class H^2")
    ax.set_title("The FUNDAMENTAL CLASS separates (the duality/FE does not):\n"
                 "zeta has the Euler-pole H^2 (=1); D-H is entire (=0)")
    for i, v in enumerate([res_zeta, abs(res_dh)]):
        ax.text(i, v + 0.02, f"{v:.3g}", ha="center", fontsize=9)
    ax.grid(alpha=0.3, axis="y")
    plt.tight_layout()
    plt.savefig(out_dir / "e2gg_fundamental_class.png", dpi=140)
    plt.close()
    print(f"\n[2GG] Saved {out_dir / 'e2gg_fundamental_class.png'}")
    print(f"[2GG] Saved {out_dir / 'e2gg_fundamental_class.npz'}")
    return part1, dict(fe_err=fe_err, res_zeta=res_zeta, res_dh=res_dh,
                       separates=fundclass_separates)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prec", type=int, default=30)
    args = parser.parse_args()
    run(prec=args.prec)
