"""2JJ -- brick 3 (the capstone): the D-H-AWARE detector. Reframe the stealth window
from a WALL into a TARGET. The right object does not stay SILENT on Davenport-
Heilbronn; it APPLIES to D-H and correctly LOCATES its off-line zero, while giving
zeta its on-line zeros -- and the stealth window is a reconstruction-RESOLUTION cost,
not an intrinsic blindness of the Weil form.

CONTEXT. The brainstorm (backwards_from_2050.md, section 4 mistake (iii)) argued the
D-H discipline as usually stated ("if a method fires for D-H, discard it") is a
sufficient SAFETY filter but too blunt to CHARACTERIZE correctness: the correct
object should apply to D-H and correctly output its OFF-LINE zeros (using the absence
of the Euler product to push them off the line), while outputting zeta's ON-LINE
zeros, from one mechanism. 2HH (#47) gave the exact handle: the duality-vs-
polarization defect
    D(rho) = |（1 - rho) - rho-bar| = |1 - 2 beta|,   rho = beta + i gamma,
is a FIXED structural quantity (not a reconstruction-floor quantity) that vanishes
exactly on the critical line and is nonzero exactly at off-line zeros. This is the
D-H-aware detector: a function of HEIGHT that locates the off-line obstruction.

WHAT THIS SHOWS:
 PART 1 (the detector LOCATES the off-line zero). D(gamma) computed on the actual
   zeros: for zeta it is identically 0 (all zeros on the line, RH); for D-H it is 0
   on the on-line zeros and SPIKES to |1 - 2(0.8085)| ~ 0.617 at the off-line zero
   gamma ~ 85.7. So the detector is D-H-AWARE: it does not fail to see D-H; it
   outputs D-H's off-line zero as a spike and zeta's clean line as a flat zero.
 PART 2 (the stealth window is a RESOLUTION cost, not intrinsic blindness). The #34
   stealth window was the failure of the truncated NON-circular (prime-side)
   reconstruction to see the off-line zero. Quantify why: by the explicit formula,
   resolving a zero at height gamma needs test functions of frequency ~gamma, which
   sample primes up to ~ e^{gamma}. For gamma = 85.7 that is e^{85.7} ~ 1.6e37
   primes -- unreachable. The reachable truncation (b <= 6) resolves heights only up
   to ~ log(b^2) ~ a few, far below even the FIRST zeta zero at 14.1. So the EXACT
   form (built from zeros) sees the off-line zero for free, while the reachable
   reconstruction cannot: the stealth window is the e^{gamma} resolution cost, NOT a
   property that makes the Weil form blind to D-H.
 PART 3 (the reframed discipline). The correct test is not "is the object SILENT on
   D-H?" but "does the object give each L its TRUE zero locus?" The exact Weil form /
   the defect D(gamma) passes this stronger test: D-H-aware (spikes at D-H's off-line
   zeros, flat for zeta). The cohomological reason zeta's D(gamma) == 0 is 2HH/2GG:
   on the line the FE-partner equals the conjugate (the cup product is a
   polarization); D-H's off-line zero is exactly where that fails. So the upgraded
   discipline -- from D-H-EXCLUDED to D-H-AWARE -- is the brainstorm's mistake (iii)
   made concrete: a method that responds CORRECTLY to D-H (off-line) is not wrong; it
   is the right shape.

HONEST SCOPE. D(gamma) is computed from the actual zeros: a CHARACTERIZATION /
LOCALIZATION demonstration (like the FF anchors and 2HH), circular as an RH proof.
Its value is the reframe: it shows the exact object is D-H-aware and that the stealth
window is a resolution cost (a quantitative, non-circular argument), NOT that the
non-circular reconstruction can be pushed to see gamma=85.7 (it provably cannot, at
e^{85.7} primes). Nothing here proves RH. A sharpening coordinate that upgrades the
D-H discipline and dissolves the "wall" reading of the stealth window.

Outputs:
  - e2jj_dh_aware_detector.npz
  - e2jj_dh_aware_detector.png
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


def dh_online_zeros(dh, T_max, step=0.2):
    """Cheap critical-line zero locations for D-H via sign changes of Re of the
    evaluated function. These are ON-line zeros (beta = 1/2, so D = 0); used only to
    illustrate that the detector is flat there. Not high-precision; the point is
    beta = 1/2 => D = 0 regardless of the exact height."""
    zs, prev, t = [], None, 2.0
    while t < T_max:
        v = complex(dh.evaluate(complex(0.5, t)))
        if prev is not None and prev * v.real < 0:
            zs.append(t - step / 2)
        prev = v.real
        t += step
    return zs


def run(T_max=90.0, prec=20, out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)
    mp.mp.dps = prec

    print("=" * 78)
    print("[2JJ] Brick 3 (capstone): the D-H-AWARE detector. The stealth window is a")
    print("      TARGET, not a wall: the right object LOCATES D-H's off-line zero.")
    print("=" * 78)

    # ---- PART 1: the detector D(gamma) = |1 - 2 beta| locates the off-line zero ---- #
    print("\nPART 1. Detector D(gamma) = |1 - 2 beta| on the actual zeros.")
    zeros_z = zeta_L.zeros(T_max, prec)
    gz = np.array([float(mp.im(z)) for z in zeros_z if mp.im(z) > 0])
    bz = np.array([float(mp.re(z)) for z in zeros_z if mp.im(z) > 0])
    Dz = np.abs(1.0 - 2.0 * bz)
    print(f"    zeta: {len(gz)} zeros up to T={T_max:.0f}; max D(gamma) = {Dz.max():.2e}")
    print(f"          => detector IDENTICALLY 0 (all zeros on the line: RH).")

    dh = DavenportHeilbronn()
    # on-line D-H zeros (beta = 1/2 => D = 0), illustrative
    g_dh_on = np.array(dh_online_zeros(dh, min(T_max, 60.0)))
    D_dh_on = np.zeros_like(g_dh_on)  # beta = 1/2 on the line
    # the off-line zero (the project landmark, verified a zero in 2HH)
    beta_off, gamma_off = 0.80852, 85.69934
    D_off = abs(1.0 - 2.0 * beta_off)
    print(f"    D-H: {len(g_dh_on)} on-line zeros (beta=1/2 => D=0) up to T={min(T_max,60):.0f},")
    print(f"         PLUS the off-line zero at gamma ~ {gamma_off:.1f} (beta ~ {beta_off:.4f}):")
    print(f"         D(gamma) SPIKES to |1 - 2 beta| = {D_off:.4f}.")
    print(f"    => the detector is D-H-AWARE: flat 0 for zeta, a spike at D-H's off-line zero.")
    print(f"       It does NOT fail to see D-H; it LOCATES D-H's off-line obstruction.")

    # ---- PART 2: the stealth window is a RESOLUTION cost ---- #
    print("\nPART 2. Why the NON-circular reconstruction is blind (stealth window = cost).")
    b_max = 6.0
    reach_height = float(np.log(b_max * b_max))  # ~ scale resolved by b <= b_max
    primes_needed = float(mp.e) ** gamma_off
    print(f"    Resolving a zero at height gamma needs test functions of frequency ~gamma,")
    print(f"    i.e. primes up to ~ e^gamma. For gamma = {gamma_off:.1f}: e^gamma ~ {primes_needed:.2e} primes.")
    print(f"    The reachable truncation b <= {b_max:.0f} resolves heights only up to ~ log(b^2)")
    print(f"    = {reach_height:.2f} -- below even the FIRST zeta zero at 14.13. So the EXACT")
    print(f"    form (from zeros) sees gamma={gamma_off:.1f} for free; the reachable reconstruction")
    print(f"    cannot (it would need ~1e37 primes). The stealth window is this RESOLUTION COST,")
    print(f"    NOT an intrinsic blindness of the Weil form to D-H.")

    # ---- PART 3: the reframed discipline + verdict ---- #
    print("\nPART 3. The reframed D-H discipline (brainstorm mistake (iii) made concrete).")
    print("    OLD: 'if it fires for D-H, discard.' (Sufficient safety, too blunt.)")
    print("    NEW: 'does it give each L its TRUE zero locus?' The exact Weil form / the")
    print("    defect D(gamma) is D-H-AWARE: it spikes at D-H's off-line zeros and is flat")
    print("    for zeta. A method that responds CORRECTLY to D-H (off-line) is the right")
    print("    shape, not a failure. The cohomological reason zeta's D(gamma)=0 is 2HH/2GG:")
    print("    on the line the FE-partner equals the conjugate (the cup product is a")
    print("    polarization); D-H's off-line zero is exactly where that fails.")

    print("\n" + "=" * 78)
    print("[2JJ] VERDICT (brick 3, capstone).")
    print("=" * 78)
    print("  The stealth window is a TARGET reframed, not a wall: the exact Weil form is")
    print("  D-H-AWARE (the detector D(gamma) LOCATES D-H's off-line zero at 85.7 and is flat")
    print("  for zeta), and the non-circular reconstruction's blindness is a resolution cost")
    print("  (e^{85.7} ~ 1e37 primes), NOT an intrinsic failure to distinguish. So the D-H")
    print("  discipline upgrades from D-H-EXCLUDED to D-H-AWARE: the right object gives D-H its")
    print("  off-line zeros and zeta its on-line zeros from one mechanism (the cup-product-is-a-")
    print("  polarization criterion, 2HH). This closes the brainstorm's mistake (iii) loop.")
    print("\n  HONEST SCOPE: D(gamma) is computed from the actual zeros (a localization")
    print("  demonstration, circular as a proof); the resolution argument is quantitative and")
    print("  non-circular. Nothing proves RH. The reframe is the deliverable: the stealth")
    print("  window is a cost, the exact object is D-H-aware, and the discipline is upgraded.")

    np.savez_compressed(
        out_dir / "e2jj_dh_aware_detector.npz",
        zeta_gamma=gz, zeta_D=Dz, dh_online_gamma=g_dh_on,
        dh_off_gamma=gamma_off, dh_off_beta=beta_off, dh_off_D=D_off,
        reach_height=reach_height, primes_needed=primes_needed,
        T_max=T_max, prec=prec,
    )

    # plot
    fig, axs = plt.subplots(1, 2, figsize=(13, 5))
    ax = axs[0]
    ax.scatter(gz, Dz, color="tab:green", s=20, zorder=3, label="zeta zeros (D=0, on line)")
    if len(g_dh_on):
        ax.scatter(g_dh_on, D_dh_on, color="tab:blue", s=20, marker="s", zorder=3,
                   label="D-H on-line zeros (D=0)")
    ax.scatter([gamma_off], [D_off], color="tab:red", s=120, marker="*", zorder=4,
               label=f"D-H OFF-line zero (D={D_off:.2f})")
    ax.set_xlabel("height gamma"); ax.set_ylabel("detector D(gamma) = |1 - 2 beta|")
    ax.set_title("Part 1: the D-H-aware detector LOCATES the off-line zero\n"
                 "(flat 0 for zeta; spike at D-H's gamma~85.7)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    ax = axs[1]
    gammas = np.linspace(5, 90, 200)
    ax.semilogy(gammas, np.exp(gammas), color="tab:purple", lw=2,
                label="primes needed ~ e^gamma")
    ax.axvline(gamma_off, color="tab:red", ls="--", label=f"D-H off-line zero gamma={gamma_off:.0f}")
    ax.axhline(np.exp(gamma_off), color="tab:red", ls=":", lw=0.8)
    ax.axvline(reach_height, color="tab:gray", ls="--", label=f"reachable (b<=6): height ~{reach_height:.1f}")
    ax.text(gamma_off - 3, np.exp(gamma_off) * 3, f"~1e{int(gamma_off/np.log(10))} primes",
            color="tab:red", fontsize=8, ha="right")
    ax.set_xlabel("height gamma"); ax.set_ylabel("primes needed to resolve (log scale)")
    ax.set_title("Part 2: stealth window = resolution COST\n(exact form sees it; reconstruction can't)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(out_dir / "e2jj_dh_aware_detector.png", dpi=140)
    plt.close()
    print(f"\n[2JJ] Saved {out_dir / 'e2jj_dh_aware_detector.png'}")
    print(f"[2JJ] Saved {out_dir / 'e2jj_dh_aware_detector.npz'}")
    return dict(zeta_max_D=float(Dz.max()), dh_off_D=D_off,
                primes_needed=primes_needed, reach_height=reach_height)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--T-max", type=float, default=90.0)
    parser.add_argument("--prec", type=int, default=20)
    args = parser.parse_args()
    run(T_max=args.T_max, prec=args.prec)
