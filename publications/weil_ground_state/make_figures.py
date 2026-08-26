"""P12 print figures F1-F4 for the Weil ground-state note.

Sources (tracked npz artifacts next to their scripts, per the evidence rule):
  F1  experiments/arithmetic_geometric/e2ao_scaling_ladder.npz
  F2  experiments/arithmetic_geometric/e2aq_xi_convergence.npz
      (the per-zero graded profile gamma_6..gamma_9 is the dossier-cited
       measurement, e2aq_xi_convergence.md item "the frontier is GRADED";
       values hardcoded below with that citation)
  F3  experiments/arithmetic_geometric/e2as_deep_xi_ladder.npz
      experiments/arithmetic_geometric/e2au_turnaround_ladder.npz
  F4  experiments/arithmetic_geometric/e2aw_energy_gap.npz

Design: single-column print figures (PDF for LaTeX; PNG preview for the
markdown draft). Palette = the repo dataviz skill's validated default
categorical hues (blue #2a78d6 / orange #eb6834 / aqua #1baf7a; neutral inks
#0b0b0b / #52514e), colorblind-validated per that skill's validator; one axis
per panel; thin marks; recessive grid; direct labels where they fit.

Run:  python -m publications.weil_ground_state.make_figures
Out:  publications/weil_ground_state/figures/f{1..4}.{pdf,png}
"""

from __future__ import annotations

from math import pi, sqrt
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
EXP = HERE.parent.parent / "experiments" / "arithmetic_geometric"
OUT = HERE / "figures"

BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
INK, INK2 = "#0b0b0b", "#52514e"
GAMMA1 = 14.134725

plt.rcParams.update({
    "font.size": 9, "axes.labelsize": 9, "axes.titlesize": 9,
    "legend.fontsize": 7.5, "xtick.labelsize": 8, "ytick.labelsize": 8,
    "axes.edgecolor": INK2, "axes.linewidth": 0.7,
    "xtick.color": INK2, "ytick.color": INK2,
    "axes.labelcolor": INK, "text.color": INK,
    "grid.color": "#dddbd6", "grid.linewidth": 0.5,
    "legend.frameon": False, "figure.dpi": 300, "savefig.dpi": 300,
})


def save(fig, name):
    OUT.mkdir(exist_ok=True)
    for ext in ("pdf", "png"):
        fig.savefig(OUT / f"{name}.{ext}", bbox_inches="tight")
    plt.close(fig)
    print(f"wrote figures/{name}.pdf + .png")


def f1():
    d = np.load(EXP / "e2ao_scaling_ladder.npz")
    sig = d["sigmas"]
    mz, mp_, err = d["margin_zero"], d["margin_prime"], d["assembly_err"]
    fig, ax = plt.subplots(figsize=(4.6, 3.1))
    ss = np.linspace(0.18, 0.72, 200)
    ax.semilogy(ss ** 2, 4 * sqrt(pi) * ss * np.exp(-GAMMA1 ** 2 * ss ** 2),
                ls="--", lw=1.2, color=INK, zorder=2,
                label=r"$4\sqrt{\pi}\,\sigma\,e^{-\gamma_1^2\sigma^2}$")
    ax.semilogy(sig ** 2, mz, "o", ms=5, color=BLUE, zorder=4,
                label="margin (zero side, exact)")
    ax.semilogy(sig ** 2, err, "-", lw=1.0, color=INK2, alpha=0.8, zorder=1,
                label="prime-side assembly floor")
    ok = mp_ > 0
    ax.semilogy(sig[ok] ** 2, mp_[ok], "x", ms=6, mew=1.4, color=ORANGE,
                zorder=5, label="prime-side value")
    ax.axvline(0.3 ** 2, color=INK2, lw=0.6, ls=":")
    ax.annotate("certification floor\ncrossed at $\\sigma = 0.3$",
                xy=(0.105, 1e-9), fontsize=7.5, color=INK2, ha="left")
    ax.annotate("slope $-199.79$ vs $-\\gamma_1^2 = -199.79$\n"
                "intercept $1.959$ vs $\\ln 4\\sqrt{\\pi} = 1.959$\n"
                "$R^2 = 1.000000$",
                xy=(0.30, 1e-28), fontsize=7.5, color=INK, ha="left")
    ax.set_xlabel(r"$\sigma^2$")
    ax.set_ylabel(r"margin$(\sigma)$")
    ax.set_ylim(1e-45, 3e-2)
    ax.grid(True, axis="y", alpha=0.6)
    leg = ax.legend(loc="lower left", handlelength=1.6, frameon=True)
    leg.get_frame().set_facecolor("white")
    leg.get_frame().set_edgecolor("none")
    save(fig, "f1")


def f2():
    d = np.load(EXP / "e2aq_xi_convergence.npz")
    fig, (axl, axr) = plt.subplots(1, 2, figsize=(4.6, 2.7))
    # left: the graded per-zero profile (dossier-cited measurement)
    gammas = [r"$\gamma_6$", r"$\gamma_7$", r"$\gamma_8$", r"$\gamma_9$"]
    prec = np.log10([2e-35, 5e-29, 1e-23, 2e-10])
    xs = np.arange(4)
    axl.plot(xs, prec, "o-", ms=5, lw=1.2, color=BLUE)
    axl.plot(xs[2], prec[2], "o", ms=9, mfc="none", mec=ORANGE, mew=1.5)
    axl.annotate("frontier ($\\sigma$-slope\nselects $\\gamma_8$)",
                 xy=(2, prec[2]), xytext=(0.8, -12), fontsize=7.5,
                 color=ORANGE, arrowprops=dict(arrowstyle="-", color=ORANGE, lw=0.7))
    axl.annotate(r"$\approx 6$ decades / zero", xy=(0.15, -33), fontsize=7.5,
                 color=INK2, rotation=0)
    axl.set_xticks(xs, gammas)
    axl.set_ylabel(r"$\log_{10}$ node precision")
    axl.set_ylim(-40, -5)
    axl.grid(True, axis="y", alpha=0.6)
    # right: the frontier law on the fixed grid
    s2, lg = d["sig2b"], d["lg2b"]
    slope_meas = float(d["dslope_fixed"])
    axr.plot(s2, lg, "o", ms=5, color=BLUE, label="measured (fixed grid)")
    c = np.polyfit(s2, lg, 1)
    ss = np.linspace(s2.min() - 0.01, s2.max() + 0.01, 50)
    axr.plot(ss, np.polyval(c, ss), "-", lw=1.0, color=BLUE, alpha=0.7)
    axr.plot(ss, np.polyval([-87.0 / np.log(10), np.polyval(c, 0.5) + 87.0 / np.log(10) * 0.5], ss),
             "--", lw=1.0, color=INK,
             label=r"$-(\gamma_8-\Omega)^2 = -87.0$")
    axr.annotate(rf"$d\ln m/d\sigma^2 = {slope_meas:.1f}$",
                 xy=(0.42, -40.6), fontsize=7.5, color=INK)
    axr.set_xlabel(r"$\sigma^2$")
    axr.set_ylabel(r"$\log_{10}$ margin")
    axr.grid(True, axis="y", alpha=0.6)
    axr.legend(loc="upper right", handlelength=1.6)
    fig.tight_layout(w_pad=1.4)
    save(fig, "f2")


def f3():
    s = np.load(EXP / "e2as_deep_xi_ladder.npz")
    u = np.load(EXP / "e2au_turnaround_ladder.npz")
    # z columns: e2as zpts [2,4,6,8]; e2au zpts [2,4,6,8,10]
    fig, ax = plt.subplots(figsize=(4.6, 3.0))
    colors = {2: BLUE, 4: ORANGE, 6: AQUA}
    for zi, z in enumerate([2, 4, 6]):
        a_all = np.concatenate([s["avals"][:3], u["avals"]])       # a=2.5 from e2au
        r_all = np.concatenate([s["ratios_ref"][:3, zi], u["ratios_ref"][:, zi]])
        conv = np.concatenate([s["conv"][:3], u["conv"]])
        ax.plot(a_all, r_all, "-", lw=1.2, color=colors[z], zorder=2)
        ax.plot(a_all[conv], r_all[conv], "o", ms=4.5, color=colors[z], zorder=3)
        ax.plot(a_all[~conv], r_all[~conv], "o", ms=5, mfc="none",
                mec=colors[z], mew=1.2, zorder=3)
        dy = {2: 0.0, 4: 0.008, 6: -0.05}[z]
        ax.annotate(f"$z={z}$", xy=(a_all[-1] + 0.06, r_all[-1] + dy),
                    color=colors[z], fontsize=8, va="center")
    ax.axhline(1.0, color=INK, lw=0.8, ls="--")
    ax.annotate(r"$\Xi$ shape", xy=(4.35, 1.03), fontsize=7.5, color=INK)
    ax.annotate("transient\nat $a \\approx 1$", xy=(1.0, 1.13), xytext=(1.35, 1.28),
                fontsize=7.5, color=INK2,
                arrowprops=dict(arrowstyle="-", color=INK2, lw=0.7))
    ax.annotate("open markers: outside\nconvergence gates (no claim)",
                xy=(3.0, 0.62), fontsize=7.5, color=INK2)
    ax.set_xlabel(r"window half-width $a$")
    ax.set_ylabel(r"$z_0$-normalized FT ratio to $\Xi$")
    ax.set_xlim(0.8, 5.5)
    ax.grid(True, axis="y", alpha=0.6)
    save(fig, "f3")


def f4():
    d = np.load(EXP / "e2aw_energy_gap.npz")
    a, l0, B, Q = d["avals"], d["lg_lam0"], d["lg_B"], d["lg_Qsharp"]
    m = ~np.isnan(Q)
    fig, (axt, axb) = plt.subplots(2, 1, figsize=(4.6, 4.4), sharex=True,
                                   height_ratios=[1.15, 1])
    for ax in (axt, axb):
        ax.axvspan(1.5, 4.1, color="#f0efeb", zorder=0)
        ax.plot(a, l0, "o-", ms=4.5, lw=1.2, color=BLUE, zorder=3)
        ax.plot(a, B, "s-", ms=4.5, lw=1.2, color=ORANGE, zorder=3)
        ax.plot(a[m], Q[m], "s", ms=6.5, mfc="none", mec=INK, mew=1.1, zorder=4)
        ax.grid(True, axis="y", alpha=0.6)
        ax.set_xlim(0.85, 4.15)
    # top: the crossover region, zoomed
    axt.set_ylim(-420, 15)
    axt.annotate("crossover $a^* \\in (1, 1.5]$", xy=(1.13, -150), fontsize=7.5,
                 color=INK, ha="center")
    axt.plot([2.0, 2.0], [l0[2], B[2]], "-", lw=0.7, color=INK2)
    axt.annotate("92 orders", xy=(2.06, -100), fontsize=7.5, color=INK2)
    axt.annotate(r"instrument bottom $\log_{10}\lambda_0$ (certified)",
                 xy=(2.6, -20), fontsize=7.5, color=BLUE)
    axt.annotate(r"kernel bound $\log_{10} B$ (unconditional)",
                 xy=(2.35, -320), fontsize=7.5, color=ORANGE)
    axt.annotate("sharp kernel value", xy=(1.55, -180), fontsize=7.5, color=INK)
    axt.set_ylabel(r"$\log_{10}$ Rayleigh quotient")
    axt.set_title("zoom: the crossover", fontsize=8, color=INK2, loc="left")
    # bottom: the full plunge
    axb.plot([4.0, 4.0], [l0[6], B[6]], "-", lw=0.7, color=INK2)
    axb.annotate("8060 orders", xy=(3.55, -4200), fontsize=7.5, color=INK2)
    axb.annotate("beyond the horizon:\nresolvable-subspace optimum",
                 xy=(1.6, -6500), fontsize=7.5, color=INK2)
    axb.set_xlabel(r"window half-width $a$")
    axb.set_ylabel(r"$\log_{10}$ RQ")
    axb.set_title("full range", fontsize=8, color=INK2, loc="left")
    fig.tight_layout(h_pad=0.8)
    save(fig, "f4")


if __name__ == "__main__":
    f1()
    f2()
    f3()
    f4()
    print("done")
