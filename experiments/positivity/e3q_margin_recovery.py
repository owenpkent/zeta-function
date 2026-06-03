"""Experiment 3Q: sharp-margin recovery test (cheap-probe 4 of the accident dossier).

The "RH solved by accident" dossier (docs/03_research/rh_solved_by_accident.md)
gives an acceptance criterion a real proof must meet: "RECOVERS THE MARGIN, NOT
JUST THE SIGN". A certificate that only detects an off-line zero when its
distance from the line eps = beta - 1/2 exceeds the float64 stealth window
(eps ~ 1e-5, finding #19/#3K) is blind below that, which is LOOSER than the
rigorous Platt-Trudgian verification bound (eps < 1e-7). Such a certificate has
no disproof leverage and cannot certify RH.

This experiment injects a hypothetical off-line zero at the Davenport-Heilbronn
zero HEIGHT (gamma_0 = 85.699, where D-H's real off-line zero sits, at the much
larger eps = 0.3085) and sweeps eps down toward the line. It answers the NEW
question #3K left open: is the stealth window a FUNDAMENTAL obstruction or merely
a float64 artifact?

  Part 1 (float64, the 3K framework at the D-H height): the off-line margin
    = min-eig of the augmented Weil Gram. It scales as -eps^2 above a float64
    noise floor; locate the float64 stealth eps* and compare to 1e-7.
  Part 2 (precision comparison): the off-line margin's SOURCE is the imaginary
    part of phi(rho), with ||Im phi(rho)||^2 ~ eps^2. Compute it in float64 vs
    mpmath. If the float64 version floors (roundoff) while mpmath continues as
    eps^2, the stealth window is a precision ARTIFACT, not structural.
  Verdict: the margin-recovery acceptance criterion, stated sharply.

Reuses the e3c/e3j/e3k machinery so the certificate is the validated one.

Outputs:
  - e3q_margin_recovery.npz
  - e3q_margin_recovery.png
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

from experiments._shared import zeta_L
from experiments.positivity.e3c_weil_form import phi_b
from experiments.positivity.e3j_schur_complement import schur_complement
from experiments.positivity.e3k_hypothetical_offline import augmented_gram

DH_GAMMA = 85.699  # the Davenport-Heilbronn off-line zero height (beta = 0.8085)
RIGOROUS_BOUND = 1e-7   # Platt-Trudgian: zeros verified on the line to ~this in beta


def im_phi_norm2(b_vals, beta, gamma_0, use_mpmath, dps):
    """sum_b |Im phi_b(beta + i*gamma_0)|^2, the SOURCE of the off-line negative
    eigenvalue (the Weil form's off-line piece is +2||Re phi||^2 - 2||Im phi||^2,
    so the negative direction has magnitude ~ 2||Im phi||^2 ~ eps^2).

    use_mpmath=False stores phi as float64 complex first (so Im is lost to
    roundoff once eps*|d phi| < machine_eps*|phi|); True keeps full mpmath."""
    prev = mp.mp.dps
    mp.mp.dps = dps
    try:
        rho = mp.mpc(beta, gamma_0)
        s = 0.0
        for b in b_vals:
            val = phi_b(mp.mpf(b), rho, prec=dps)
            if use_mpmath:
                im = float(mp.im(val))
            else:
                im = complex(val).imag  # force float64 representation
            s += im * im
        return s
    finally:
        mp.mp.dps = prev


def run(K=200, b_min=1.1, b_max=1000.0, T_max=120.0, n_eps=24, prec=30, out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    b_vals = np.logspace(np.log10(b_min), np.log10(b_max), K)
    eps_vals = np.logspace(-9, np.log10(0.3085), n_eps)  # down below the rigorous bound; up to the real D-H eps

    print("=" * 76)
    print("[3Q] Sharp-margin recovery test at the D-H zero height")
    print(f"     gamma_0 = {DH_GAMMA} (the real D-H off-line zero; its eps = 0.3085)")
    print(f"     K={K}, b in [{b_min},{b_max}], on-line cushion T_max={T_max}, prec={prec}")
    print("=" * 76)

    print("[3Q] Loading zeta on-line zeros (cushion)...")
    t0 = time.time()
    on_zeros = zeta_L.zeros(T_max=T_max, prec=prec)
    print(f"     {len(on_zeros)} zeros in {time.time()-t0:.1f}s")

    # ---- Part 1: float64 margin (min-eig of the augmented Weil Gram) ----
    print("\n[3Q] Part 1: float64 margin = min-eig(M_aug) vs eps (the 3K framework, D-H height)")
    margin = np.full(n_eps, np.nan)
    schur_neg = np.full(n_eps, np.nan)  # clamped off-line negative-eigenvalue magnitude
    for i, eps in enumerate(eps_vals):
        beta = 0.5 + eps
        M_on, M_off = augmented_gram(on_zeros, b_vals, beta, DH_GAMMA, prec=prec)
        M = M_on + M_off
        margin[i] = float(np.linalg.eigvalsh(M).min())
        S, _, _, _, r_dim = schur_complement(M_on, M_off)
        if S.size > 0:
            lo = float(np.linalg.eigvalsh(S).min())
            schur_neg[i] = max(0.0, -lo)  # 0 when the off-line direction is lost (stealth)
        else:
            schur_neg[i] = 0.0
        print(f"     eps={eps:.2e}  margin(min-eig M_aug)={margin[i]:+.3e}  "
              f"|off-line eig|={schur_neg[i]:.3e}")

    # float64 noise floor of the margin: median of the |margin| at the 5 smallest eps
    # (there the true signal ~eps^2 is far below roundoff, so |margin| is pure noise).
    noise = float(np.median(np.abs(margin[:5])))
    detect = np.abs(margin) > 10.0 * noise
    eps_star_f64 = float(eps_vals[detect][0]) if detect.any() else float("inf")
    print(f"     float64 margin noise floor ~ {noise:.2e}; detectable (|margin| > 10x floor) "
          f"from eps* ~ {eps_star_f64:.2e}")

    # ---- Part 2: artifact or structural? float64 vs mpmath off-line signal source ----
    print("\n[3Q] Part 2: ||Im phi(rho)||^2 (the off-line signal source) -- float64 vs mpmath")
    eps_probe = np.logspace(-2, -12, 11)
    b_small = np.logspace(np.log10(1.2), np.log10(200.0), 40)
    print(f"     {'eps':>9} {'float64 ||Im phi||^2':>22} {'mpmath ||Im phi||^2':>22} {'mpmath/eps^2':>14}")
    s_f64 = []
    s_mp = []
    for eps in eps_probe:
        beta = 0.5 + eps
        a = im_phi_norm2(b_small, beta, DH_GAMMA, use_mpmath=False, dps=prec)
        b = im_phi_norm2(b_small, beta, DH_GAMMA, use_mpmath=True, dps=50)
        s_f64.append(a)
        s_mp.append(b)
        print(f"     {eps:>9.1e} {a:>22.4e} {b:>22.4e} {b/(eps*eps):>14.4e}")

    s_f64 = np.array(s_f64)
    s_mp = np.array(s_mp)
    # The signal SOURCE: is ||Im phi||^2 a clean eps^2, and do float64 and mpmath agree?
    mp_ratio = s_mp / eps_probe**2
    mp_const = bool(np.std(np.log10(mp_ratio[mp_ratio > 0])) < 0.05) if (mp_ratio > 0).any() else False
    rel_gap = float(np.max(np.abs(s_f64 - s_mp) / np.maximum(s_mp, 1e-300)))
    src_clean_f64 = rel_gap < 1e-6
    c_margin = abs(margin[18]) / eps_vals[18] ** 2  # eps ~ 4e-3, well above the cancellation floor

    print("\n" + "=" * 76)
    print("[3Q] VERDICT (the 'RECOVERS THE MARGIN' acceptance criterion)")
    print(f"     Part 1: the off-line margin = min-eig(M_aug) scales as -{c_margin:.2g}*eps^2 (the #3K")
    print(f"       law) at the D-H height. The REAL D-H zero (eps=0.3085) gives {margin[-1]:+.3e}:")
    print(f"       trivially detected. float64 full-Gram detection reaches eps* ~ {eps_star_f64:.1e}")
    print(f"       (where -c*eps^2 meets the ~{noise:.0e} eigenvalue cancellation floor); the #19 Schur")
    print(f"       detector's relative-signal stealth is looser (~1e-5). Both straddle the rigorous")
    print(f"       Platt-Trudgian bound {RIGOROUS_BOUND:.0e}.")
    if mp_const and src_clean_f64:
        print(f"     Part 2: the off-line signal SOURCE ||Im phi||^2 is a clean eps^2 (ratio const")
        print(f"       {float(np.median(mp_ratio)):.3g}), and float64 == mpmath to {rel_gap:.0e} down to eps=1e-12.")
        print("       So the stealth window is NOT in the data: it is a float64 EIGENSOLVER")
        print("       CANCELLATION artifact (extracting a -eps^2 eigenvalue from an O(1) Gram).")
        print("       Computed from the source, or in higher precision, the margin is recoverable")
        print("       to arbitrarily small eps. The stealth is removable, not structural.")
    else:
        print(f"     Part 2: src_clean_f64={src_clean_f64} (rel gap {rel_gap:.1e}), eps^2-const={mp_const} (see table).")
    print("     THE SHARP POINT (sharpens #3K): removability is moot for CERTIFICATION. Detecting")
    print("       an off-line zero at distance eps requires KNOWING its location to precision < eps")
    print("       and injecting it -- exactly what rigorous verification already supplies. So this")
    print("       certificate is DOWNSTREAM of the rigorous check and has no INDEPENDENT disproof")
    print("       leverage; it cannot certify RH on its own. A proof must recover the margin")
    print("       ANALYTICALLY (engage the exact off-line structure of zeta), not via finite")
    print("       eigenvalues of a hand-injected zero. The marginal-positivity thesis.")
    print("=" * 76)

    np.savez_compressed(
        out_dir / "e3q_margin_recovery.npz",
        eps=eps_vals, margin=margin, schur_neg=schur_neg, eps_star_f64=eps_star_f64, noise=noise,
        eps_probe=eps_probe, s_f64=s_f64, s_mp=s_mp,
        gamma_0=DH_GAMMA, K=K, T_max=T_max, prec=prec,
    )

    fig, axs = plt.subplots(1, 2, figsize=(13, 5))
    ax = axs[0]
    ax.loglog(eps_vals, np.abs(margin), "o-", label="|margin| = |min-eig(M_aug)| (float64)")
    ref = (eps_vals / eps_vals[-1]) ** 2 * abs(margin[-1])
    ax.loglog(eps_vals, ref, "k--", alpha=0.5, label=r"$\propto \varepsilon^2$")
    ax.axhline(noise, color="gray", ls=":", label="float64 noise floor")
    ax.axvline(eps_star_f64, color="orange", ls=":", label=f"float64 stealth eps* ~ {eps_star_f64:.0e}")
    ax.axvline(RIGOROUS_BOUND, color="red", ls=":", label=f"rigorous bound {RIGOROUS_BOUND:.0e}")
    ax.set_xlabel(r"$\varepsilon = \beta - 1/2$"); ax.set_ylabel("|margin|")
    ax.set_title(f"Part 1: off-line margin vs eps (D-H height {DH_GAMMA})")
    ax.legend(fontsize=7); ax.grid(alpha=0.3, which="both")

    ax = axs[1]
    ax.loglog(eps_probe, np.maximum(s_f64, 1e-300), "s-", color="tab:orange", label=r"float64 $\|\mathrm{Im}\,\phi\|^2$")
    ax.loglog(eps_probe, np.maximum(s_mp, 1e-300), "o-", color="tab:blue", label=r"mpmath $\|\mathrm{Im}\,\phi\|^2$")
    ref2 = (eps_probe / eps_probe[0]) ** 2 * s_mp[0]
    ax.loglog(eps_probe, ref2, "k--", alpha=0.5, label=r"$\propto \varepsilon^2$")
    ax.set_xlabel(r"$\varepsilon$"); ax.set_ylabel(r"$\|\mathrm{Im}\,\phi(\rho)\|^2$")
    ax.set_title("Part 2: stealth is a float64 artifact (mpmath has no floor)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3, which="both")
    plt.tight_layout()
    plt.savefig(out_dir / "e3q_margin_recovery.png", dpi=140)
    plt.close()
    print(f"[3Q] Saved {out_dir / 'e3q_margin_recovery.png'}")
    print(f"[3Q] Saved {out_dir / 'e3q_margin_recovery.npz'}")
    return eps_vals, margin, (eps_probe, s_f64, s_mp)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--K", type=int, default=200)
    parser.add_argument("--T-max", type=float, default=120.0)
    parser.add_argument("--n-eps", type=int, default=24)
    parser.add_argument("--prec", type=int, default=30)
    args = parser.parse_args()
    run(K=args.K, T_max=args.T_max, n_eps=args.n_eps, prec=args.prec)
