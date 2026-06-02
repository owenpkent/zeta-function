"""Experiment M3.2: Stress-test the M_euler discriminator.

M3 (e3m_analytic_domination.py) claimed that M_euler = A_arch + P_pp + B_pole
is "the true geometric RH test": positive for zeta (+0.035) and the RH-holding
principal Epstein d=47 (+0.676), negative for Davenport-Heilbronn (-0.929).

But M_euler is formed by DELETING the composite block P_comp by hand. For an
Euler product that deletion is automatic; for a non-Euler L it is imposed, and
is logically the same as assuming an Euler-product geometry. The conjecture that
this is geometrically forced (Direction 8B/8C) is NOT proved. So before building
the geometric signature on top of M_euler, we must answer one question:

    Is M_euler an actual RH detector, or does it only look like one because the
    three M3 controls were favorable?

This script attacks that question with the controls M3 omitted. Two failure modes
would falsify M_euler as a detector:

  (A) FALSE NEGATIVE: an Euler product satisfying RH with M_euler < 0. We add the
      Dirichlet L-functions chi3, chi4 (genuine Euler products, GRH believed,
      P_comp must be exactly 0). If M_euler < 0 for either, the archimedean bound
      A_arch does NOT in general dominate the prime-power block, and M3's positive
      reading for zeta was zeta-specific luck, not a geometric law.

  (B) FALSE POSITIVE: a non-Euler L with off-line zeros (RH FALSE) but M_euler > 0.
      The decisive case: the NON-PRINCIPAL Epstein form of discriminant 47 (class
      number 5), which has a genuine off-line zero pair at rho ~ 0.634 + 32.05 i.
      It shares the EXACT archimedean setup (Gamma factor, conductor sqrt(47)) of
      the principal d=47 form M3 already tested and found positive (+0.676). So
      this is a clean controlled flip: same everything except RH-true -> RH-false.
      If M_euler stays >= 0, the "stealth window broken" claim collapses: the
      window was not broken, only relocated to a harder example.

Reusing the validated block builders from e3m keeps the archimedean normalization
(the M2.6 C_mu fix) identical, so any sign behavior is attributable to the L-data,
not to a kernel change.

Outputs:
  - e3m2_stress_test.npz
  - e3m2_stress_test.png
"""

from __future__ import annotations

import argparse
import time
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np

from experiments._shared import (
    zeta_L, DavenportHeilbronn, epstein_for_discriminant, chi3_L, chi4_L,
)
from experiments.positivity.e3m_place_type_balance import (
    pole_block, lambda_coeffs_from_dirichlet, von_mangoldt_zeta, numeric_residue_at_one,
)
from experiments.positivity.e3m_analytic_domination import split_finite_block
from experiments.arithmetic_geometric.e2v_rosati_balance_M2_5 import arch_block_bombieri


def build_targets():
    """The control suite. Tuple fields mirror e3m's `targets`:
    (label, L, mu_list, log_Q, residue, has_euler, rh, note)

    rh is the GROUND TRUTH at reachable height (what a correct detector must
    return the sign of). The two probes M3 omitted are flagged in `note`.
    """
    dh = DavenportHeilbronn()
    eps47_prin = epstein_for_discriminant(47, principal=True)   # RH holds <= 120 (M3 control)
    eps47_off = epstein_for_discriminant(47, principal=False)   # off-line zero ~0.634+32.05i: RH FALSE
    eps15_off = epstein_for_discriminant(15, principal=False)   # no off-line zeros < T=80: RH holds (reachable)

    return [
        # ---- Euler products: P_comp must be 0; RH believed => M_euler should be > 0
        ("zeta",        zeta_L,     [0.0],      mp.mpf(0),           1.0,  True,  True,  "M3 baseline"),
        ("chi3",        chi3_L,     [1.0],      mp.log(mp.sqrt(3)),  0.0,  True,  True,  "PROBE A: Euler, RH true"),
        ("chi4",        chi4_L,     [1.0],      mp.log(mp.sqrt(4)),  0.0,  True,  True,  "PROBE A: Euler, RH true"),
        # ---- Non-Euler, RH FALSE: M_euler should be < 0 if it is a real detector
        ("DH",          dh,         [1.0],      mp.log(mp.sqrt(5)),  0.0,  False, False, "M3 control"),
        ("Eps47_off",   eps47_off,  [0.0, 1.0], mp.log(mp.sqrt(47)), None, False, False, "PROBE B: off-line zero, RH FALSE"),
        # ---- Non-Euler, RH holds at reachable height: M_euler should be > 0
        ("Eps47_prin",  eps47_prin, [0.0, 1.0], mp.log(mp.sqrt(47)), None, False, True,  "M3 control"),
        ("Eps15_off",   eps15_off,  [0.0, 1.0], mp.log(mp.sqrt(15)), None, False, True,  "no off-line < T=80"),
    ]


def run(K=8, b_min=1.3, b_max=6.0, prec=30, out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)
    b_vals = np.logspace(np.log10(b_min), np.log10(b_max), K)
    n_max = int(b_max * b_max) + 2

    targets = build_targets()

    print("[M3.2] Stress-test of the M_euler discriminator.")
    print(f"       K={K}, b in [{b_min},{b_max}], n_max={n_max}, prec={prec}")
    print("       A correct detector must match sign(M_euler) to the RH column.\n")

    header = (f"{'target':<12} {'Euler':>5} {'RH':>5} {'min eig(M_euler)':>17} "
              f"{'min eig(M_full)':>16} {'norm(P_comp)':>13} {'verdict':>9}  note")
    print(header)
    print("-" * len(header))

    results = {}
    any_break = False
    undefined = []
    for label, L, mu_list, log_Q, residue, has_euler, rh, note in targets:
        t0 = time.time()
        if label == "zeta":
            lam = np.array([0.0] + [von_mangoldt_zeta(n) for n in range(1, n_max + 1)])
        else:
            try:
                lam = lambda_coeffs_from_dirichlet(L, n_max, prec)
            except ValueError as e:
                # a_1 = 0: the von-Mangoldt split is UNDEFINED. This is the finding,
                # not an error. Off-line Epstein forms are non-principal (a >= 2), so
                # they never represent 1 and M_euler cannot be formed for them.
                undefined.append((label, rh, note, str(e)))
                results[label] = dict(has_euler=has_euler, rh=rh, min_eig_euler=None,
                                      min_eig_full=None, norm_comp=None, agrees=None,
                                      note=note, undefined=True)
                print(f"{label:<12} {str(has_euler):>5} {str(rh):>5} {'UNDEFINED (a_1=0)':>17} "
                      f"{'--':>16} {'--':>13} {'n/a':>9}  {note}  [{time.time()-t0:.0f}s]")
                continue

        P_pp, P_comp = split_finite_block(b_vals, lam, prec)

        if residue is None:
            residue = numeric_residue_at_one(L, prec)
        B = pole_block(b_vals, float(residue), prec)
        A = arch_block_bombieri(b_vals, mu_list, log_Q, prec)

        M_euler = A + P_pp + B
        M_full = A + P_pp + P_comp + B
        min_eig_euler = float(np.linalg.eigvalsh(M_euler).min())
        min_eig_full = float(np.linalg.eigvalsh(M_full).min())
        norm_comp = float(np.linalg.norm(P_comp))

        # A correct detector: M_euler >= 0 iff RH. Flag any disagreement.
        detector_says_rh = min_eig_euler >= 0.0
        agrees = (detector_says_rh == rh)
        verdict = "ok" if agrees else "BREAK"
        if not agrees:
            any_break = True

        # An Euler product must have P_comp = 0 up to truncation noise.
        if has_euler and norm_comp > 1e-9:
            verdict += "?Pc"

        results[label] = dict(
            has_euler=has_euler, rh=rh, min_eig_euler=min_eig_euler,
            min_eig_full=min_eig_full, norm_comp=norm_comp, agrees=agrees, note=note,
            undefined=False,
        )
        print(f"{label:<12} {str(has_euler):>5} {str(rh):>5} {min_eig_euler:>+17.4e} "
              f"{min_eig_full:>+16.4e} {norm_comp:>13.3e} {verdict:>9}  {note}  [{time.time()-t0:.0f}s]")

    print("-" * len(header))
    print("\n[M3.2] ===== VERDICT =====")
    defined_offline_rhfalse = [n for n in results
                               if not results[n]["undefined"]
                               and not results[n]["has_euler"]
                               and not results[n]["rh"]]
    if any_break:
        print("  M_euler DISAGREES with RH on at least one DEFINED control (BREAK).")
        print("  The hand-deletion of P_comp is NOT a valid RH detector in general.")
    else:
        print("  PROBE A (false negative) DEFEATED: the independent Euler products")
        print("  chi3, chi4 (RH true) give M_euler > 0 with P_comp = 0 to machine")
        print("  precision. So A_arch dominating the prime-power block is NOT a")
        print("  zeta-specific accident; it holds for genuine Euler products.")
        print()
        print("  PROBE B (false positive) is STRUCTURALLY LIMITED, not passed:")
        for label, rh, note, msg in undefined:
            print(f"   - {label}: {msg.split(':')[-1].strip()}")
        print("    Off-line Epstein zeros occur ONLY for non-principal forms (a >= 2),")
        print("    which do not represent 1 (a_1 = r_Q(1) = 0). The von-Mangoldt split")
        print("    needs a_1 != 0, so M_euler is UNDEFINED for every Epstein off-line")
        print("    control. The Epstein hardening of the D-H discipline (3L, 3B.4) does")
        print(f"    NOT transfer to M_euler. M_euler's only DEFINED non-Euler off-line")
        print(f"    control is Davenport-Heilbronn {tuple(defined_offline_rhfalse)},")
        print("    where it correctly reads negative. So the false-positive test rests")
        print("    on a SINGLE example. New gap: a second integer-supported (a_1 != 0)")
        print("    off-line control is needed to genuinely test M_euler's discipline.")

    # Save (NaN encodes UNDEFINED for the a_1 = 0 controls).
    labels = list(results.keys())
    nan = float("nan")
    np.savez_compressed(
        out_dir / "e3m2_stress_test.npz",
        labels=np.array(labels, dtype=object),
        min_eig_euler=np.array([results[n]["min_eig_euler"] if not results[n]["undefined"] else nan for n in labels]),
        min_eig_full=np.array([results[n]["min_eig_full"] if not results[n]["undefined"] else nan for n in labels]),
        norm_comp=np.array([results[n]["norm_comp"] if not results[n]["undefined"] else nan for n in labels]),
        rh=np.array([results[n]["rh"] for n in labels]),
        has_euler=np.array([results[n]["has_euler"] for n in labels]),
        undefined=np.array([results[n]["undefined"] for n in labels]),
        K=K, prec=prec,
    )

    # Plot: min eig(M_euler) per control, colored by RH ground truth. Undefined
    # controls (a_1 = 0) are drawn at 0 with a hatch and an "undef" annotation.
    fig, ax = plt.subplots(figsize=(9, 5))
    vals = [0.0 if results[n]["undefined"] else results[n]["min_eig_euler"] for n in labels]
    colors = ["tab:green" if results[n]["rh"] else "tab:red" for n in labels]
    edge = ["gray" if results[n]["undefined"]
            else ("k" if results[n]["agrees"] else "magenta") for n in labels]
    bars = ax.bar(labels, vals, color=colors, edgecolor=edge, linewidth=2.0,
                  hatch=["///" if results[n]["undefined"] else "" for n in labels])
    for b, n in zip(bars, labels):
        if results[n]["undefined"]:
            ax.text(b.get_x() + b.get_width() / 2, 0.0, "undef\n(a1=0)",
                    ha="center", va="bottom", fontsize=7, color="gray")
    ax.axhline(0, color="k", lw=1)
    ax.set_ylabel("min eig(M_euler)")
    ax.set_title("M3.2: does sign(M_euler) track RH?\n"
                 "green = RH holds (want >0), red = RH fails (want <0); "
                 "magenta edge = detector BREAK")
    ax.tick_params(axis="x", rotation=20)
    ax.grid(alpha=0.3, axis="y")
    plt.tight_layout()
    plt.savefig(out_dir / "e3m2_stress_test.png", dpi=140)
    plt.close()

    print(f"\n[M3.2] Saved {out_dir / 'e3m2_stress_test.png'}")
    print(f"[M3.2] Saved {out_dir / 'e3m2_stress_test.npz'}")
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--K", type=int, default=8)
    parser.add_argument("--b-max", type=float, default=6.0)
    parser.add_argument("--prec", type=int, default=30)
    args = parser.parse_args()
    run(K=args.K, b_max=args.b_max, prec=args.prec)
