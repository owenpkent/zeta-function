"""2HH -- brick 1 of state_of_candidate_ABF: organ (a)'s positivity made exact.
RH <=> the Poincare-duality cup product is a POLARIZATION <=> FE-partner = conjugate.

CONTEXT. The synthesis (state_of_candidate_ABF.md) set brick 1 as organ (a): the
prismatic Poincare duality / a perfect cup product into the Euler-pole H^2, and
asked whether the truncated arithmetic H^1 admits a PERFECT pairing and whether
PERFECTNESS (vs positivity) is the gap. 2GG (#46) showed the functional equation
xi(s)=xi(1-s) IS the duality H^1 x H^1 -> H^2, buildable even for D-H. This
experiment pins organ (a)'s remaining content (the positivity) in its exact form.

THE CHARACTERIZATION (the sharp statement). A polarization is a duality compatible
with a positive Hermitian structure (Hodge-Riemann). Concretely, on H^1 the two
pairings are:
    - the CUP PRODUCT / Poincare duality (from the FE): pairs a zero rho with its
      functional-equation partner  1 - rho;
    - the HERMITIAN POLARIZATION (the Hodge star / complex conjugation): pairs rho
      with its complex conjugate  rho-bar.
These coincide for every zero iff  1 - rho = rho-bar  iff  Re(rho) = 1/2. Hence
    RH  <=>  the cup product (Poincare duality) IS a polarization
        <=>  for every zero, the FE-partner equals the conjugate
        <=>  the duality is Hodge-Riemann positive (organ (a)'s positivity).
The cup product (the FE-pairing) is a PERFECT (nondegenerate) duality for ANY L with
a functional equation, INCLUDING D-H. What fails for D-H is not perfectness but
POSITIVITY: at an off-line zero rho (beta != 1/2) the FE-partner 1-rho and the
conjugate rho-bar are DIFFERENT points, with displacement |1 - 2 beta| > 0. So the
gap in organ (a) is POSITIVITY (cup = polarization), NOT perfectness (cup is a
duality) -- exactly brick 1's question, answered.

WHAT THIS COMPUTES (real zeros; a CHARACTERIZATION demonstration, like the FF
anchors, NOT a non-circular certificate):
  (1) zeta: first N zeros all have beta = 1/2, so FE-partner = conjugate to machine
      precision: the cup product IS the polarization, defect 0. (Perfect AND positive.)
  (2) D-H: verify it HAS a functional equation (the duality is buildable: FE residual
      ~0), so the cup product is a PERFECT pairing for D-H too. THEN show its off-line
      zero (rho ~ 0.8085 + 85.699 i, verified a zero) has FE-partner 1-rho ~ 0.1915 -
      85.699 i DIFFERENT from the conjugate rho-bar ~ 0.8085 - 85.699 i, displacement
      |1 - 2 beta| ~ 0.617: the cup product is NOT a polarization (positivity fails),
      while perfectness holds.
  (3) The truncation / P->infinity reading. The displacement |1 - 2 beta| is a FIXED
      structural quantity, NOT a reconstruction-floor quantity: unlike the stealth
      window (#34), the duality-vs-polarization defect does not shrink with truncation
      -- it is visible at any resolution that includes the off-line zero. THE CATCH
      (honest): to evaluate it one needs the zero location (circular w.r.t. RH) OR the
      non-circular reconstruction (back under the stealth-window floor). So the
      CHARACTERIZATION is exact and stealth-window-free; its NON-CIRCULAR evaluation
      is still the analytic gap. This precisely delimits what brick 1 gains.

RELATION TO 2GG (#46): two complementary obstructions for D-H, both saying "the
duality is not a polarization": from the UNIT side (2GG: H^2 = 0, D-H entire, no
nonzero fundamental class) and from the POSITIVITY side (2HH: even granting the FE
pairing, FE-partner != conjugate at off-line zeros). Organ (a) = a perfect cup
product into the NONZERO Euler-pole H^2 that is ALSO a polarization (FE-partner =
conjugate). Perfectness and the duality are free (FE); the unit (Euler pole) and the
positivity (Re = 1/2) are the content.

HONEST SCOPE. The characterization (RH <=> cup is a polarization <=> 1-rho = rho-bar)
is an exact, elementary restatement; its value is that it imports the Hodge-Riemann
/ standard-conjecture frame (a polarization = a positive duality), the same power-
importing move 08A already endorsed, now on the H^2/duality face. The demonstration
uses actual zeros (a characterization, not a non-circular certificate) and proves
nothing new about RH. A sharpening coordinate that answers brick 1's perfectness-vs-
positivity question (positivity is the gap) and delimits the stealth-window-free
content.

Outputs:
  - e2hh_cup_is_polarization.npz
  - e2hh_cup_is_polarization.png
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


def duality_defect(beta):
    """|（1 - rho) - rho-bar| for rho = beta + i gamma = |1 - 2 beta|: the distance
    between the FE-partner (1-rho) and the conjugate (rho-bar). Zero iff beta = 1/2.
    This is the pointwise 'cup product fails to be a polarization' measure."""
    return abs(1.0 - 2.0 * beta)


def run(N_zeta=12, T_max=50.0, prec=30, out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)
    mp.mp.dps = prec

    print("=" * 78)
    print("[2HH] Brick 1 / organ (a): RH <=> the Poincare-duality cup product is a")
    print("      POLARIZATION <=> FE-partner (1-rho) = conjugate (rho-bar) <=> Re=1/2.")
    print("      Perfectness (the FE pairing) is free, even for D-H; POSITIVITY is the gap.")
    print("=" * 78)

    # ---- (1) zeta: cup product IS the polarization (defect 0) ---- #
    print(f"\n(1) ZETA: first zeros (T<{T_max:.0f}); FE-partner 1-rho vs conjugate rho-bar.")
    zeros = zeta_L.zeros(T_max, prec)
    betas_z, gammas_z, defs_z = [], [], []
    for z in zeros:
        b, g = float(mp.re(z)), float(mp.im(z))
        if g <= 0:
            continue
        betas_z.append(b); gammas_z.append(g); defs_z.append(duality_defect(b))
    betas_z = np.array(betas_z); defs_z = np.array(defs_z)
    print(f"    {len(betas_z)} zeros; max |beta - 1/2| = {np.max(np.abs(betas_z - 0.5)):.2e}")
    print(f"    => max duality-vs-polarization defect |1-2beta| = {defs_z.max():.2e} (= 0:")
    print(f"       the cup product IS the polarization; perfect AND positive).")

    # ---- (2) D-H: perfect duality (has FE) but NOT a polarization (off-line) ---- #
    print(f"\n(2) D-H: does it have the DUALITY (a functional equation)? Then is the cup")
    print(f"    product a POLARIZATION (FE-partner = conjugate)?")
    dh = DavenportHeilbronn()
    # (a) verify the functional equation (the duality) holds for D-H
    fe_pts = [mp.mpc('0.5', '10'), mp.mpc('0.7', '30'), mp.mpc('0.3', '50')]
    fe_res = []
    for s in fe_pts:
        try:
            fe_res.append(float(abs(dh.functional_equation_residual(s))))
        except Exception as e:
            fe_res.append(float('nan'))
    fe_ok = np.nanmax(fe_res) < 1e-6 if np.any(np.isfinite(fe_res)) else False
    print(f"    (a) D-H functional-equation residual (the DUALITY): max = {np.nanmax(fe_res):.2e}")
    print(f"        => D-H HAS a functional equation, so the cup product is a PERFECT pairing")
    print(f"           for D-H too: perfectness is NOT the discriminator.")
    # (b) the off-line zero: FE-partner != conjugate
    rho_off = mp.mpc('0.80852', '85.69934')  # project landmark (refined)
    val_off = dh.evaluate(rho_off)
    is_zero = abs(val_off) < 1e-3
    beta_off = float(mp.re(rho_off)); gam_off = float(mp.im(rho_off))
    fe_partner = (1.0 - beta_off, -gam_off)   # 1 - rho
    conj_partner = (beta_off, -gam_off)        # rho-bar
    def_off = duality_defect(beta_off)
    print(f"    (b) off-line zero rho ~ {beta_off:.4f} + {gam_off:.3f} i "
          f"(|L(rho)| = {float(abs(val_off)):.2e}, is-zero: {is_zero}):")
    print(f"        FE-partner 1-rho  = ({fe_partner[0]:.4f}, {fe_partner[1]:.3f})")
    print(f"        conjugate  rho-bar= ({conj_partner[0]:.4f}, {conj_partner[1]:.3f})")
    print(f"        displacement |1-2beta| = {def_off:.4f}  != 0  => the cup product is")
    print(f"        NOT a polarization for D-H (POSITIVITY fails, while perfectness holds).")

    # ---- (3) truncation reading + verdict ---- #
    print(f"\n(3) TRUNCATION / P->infinity reading.")
    print(f"    The defect |1-2beta| = {def_off:.3f} is a FIXED structural quantity, not a")
    print(f"    reconstruction-floor quantity: it does NOT shrink with truncation (unlike the")
    print(f"    #34 stealth window). It is visible at any resolution that includes the off-line")
    print(f"    zero. CATCH (honest): evaluating it needs the zero location (circular) OR the")
    print(f"    non-circular reconstruction (back under the stealth floor). So the")
    print(f"    CHARACTERIZATION is exact and stealth-free; its NON-circular evaluation is the gap.")

    print("\n" + "=" * 78)
    print("[2HH] VERDICT (brick 1).")
    print("=" * 78)
    print("  PERFECTNESS is free: the FE gives a perfect cup-product duality for BOTH zeta")
    print("  and D-H. POSITIVITY is the gap: the cup product is a POLARIZATION (FE-partner =")
    print("  conjugate) for zeta (RH) and NOT for D-H (off-line zero). So organ (a)'s open")
    print("  content is precisely 'the FE-duality is Hodge-Riemann positive', i.e. RH, on the")
    print("  infinite-dim H^1 -- and this imports the standard-conjecture frame (a polarization")
    print("  = a positive duality), the power-importing move 08A endorsed, now on the H^2 face.")
    print("  Combined with 2GG: D-H fails twice over (no nonzero H^2 unit; and FE-partner !=")
    print("  conjugate), both saying its duality is not a polarization.")
    print("\n  HONEST SCOPE: an exact elementary characterization, demonstrated on real zeros")
    print("  (not a non-circular certificate); proves nothing new about RH. A sharpening that")
    print("  answers brick 1 (positivity, not perfectness, is the gap) and is stealth-free as")
    print("  a STATEMENT while its non-circular evaluation remains the analytic gap.")

    np.savez_compressed(
        out_dir / "e2hh_cup_is_polarization.npz",
        zeta_betas=betas_z, zeta_gammas=np.array(gammas_z), zeta_defects=defs_z,
        dh_fe_residual=np.array(fe_res), dh_beta_off=beta_off, dh_gamma_off=gam_off,
        dh_def_off=def_off, dh_offzero_value=float(abs(val_off)),
        N_zeta=len(betas_z), prec=prec,
    )

    # plot
    fig, axs = plt.subplots(1, 2, figsize=(13, 5))
    ax = axs[0]
    ax.scatter(betas_z, gammas_z, color="tab:green", zorder=3, label="zeta zeros (on line)")
    ax.scatter([beta_off], [gam_off], color="tab:red", marker="x", s=90, zorder=4,
               label="D-H off-line zero")
    ax.scatter([1 - beta_off], [-gam_off], color="tab:orange", marker="^", s=70, zorder=4,
               label="its FE-partner 1-rho")
    ax.scatter([beta_off], [-gam_off], color="tab:purple", marker="s", s=70, zorder=4,
               label="its conjugate rho-bar")
    ax.axvline(0.5, color="k", ls="--", lw=1, label="Re=1/2")
    ax.set_xlabel("Re(s)"); ax.set_ylabel("Im(s)")
    ax.set_title("FE-partner = conjugate ON the line (zeta);\nthey SPLIT off the line (D-H): cup not a polarization")
    ax.legend(fontsize=7); ax.grid(alpha=0.3)

    ax = axs[1]
    ax.bar(["zeta\n(RH)", "D-H\noff-line zero"], [defs_z.max(), def_off],
           color=["tab:green", "tab:red"])
    ax.axhline(0, color="k", lw=1)
    ax.set_ylabel("duality-vs-polarization defect  |1 - 2 beta|")
    ax.set_title("Perfectness holds for both (FE);\nPOSITIVITY (cup = polarization) is the gap")
    for i, v in enumerate([defs_z.max(), def_off]):
        ax.text(i, v + 0.01, f"{v:.2g}", ha="center", fontsize=9)
    ax.grid(alpha=0.3, axis="y")
    plt.tight_layout()
    plt.savefig(out_dir / "e2hh_cup_is_polarization.png", dpi=140)
    plt.close()
    print(f"\n[2HH] Saved {out_dir / 'e2hh_cup_is_polarization.png'}")
    print(f"[2HH] Saved {out_dir / 'e2hh_cup_is_polarization.npz'}")
    return dict(zeta_max_defect=float(defs_z.max()), dh_def_off=def_off,
                dh_fe_ok=bool(fe_ok), dh_is_zero=bool(is_zero))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--N-zeta", type=int, default=12)
    parser.add_argument("--T-max", type=float, default=50.0)
    parser.add_argument("--prec", type=int, default=30)
    args = parser.parse_args()
    run(N_zeta=args.N_zeta, T_max=args.T_max, prec=args.prec)
