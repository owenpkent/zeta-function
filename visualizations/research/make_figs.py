"""Research-figure gallery: theme-aware figures + the gallery UI.

Every figure renders twice (light and dark variants); expensive data (mpmath
grids, zero lists, the lattice engine) is computed once and cached across the
two renders. The gallery (_out/index.html) is a self-contained page: dark mode
by default with a toggle, sidebar navigation, lightbox with keyboard arrows.
Animated GIFs are produced by make_anims.py into the same gallery.

Run from the repo root:
  python visualizations/research/make_figs.py            (all figures, both themes)
  python visualizations/research/make_figs.py --only 3   (one figure)
  python visualizations/research/make_figs.py --html     (rebuild index.html only)

Then open visualizations/research/_out/index.html in a browser.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from math import log, pi
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT))

import mpmath as mp                                        # noqa: E402
from experiments._shared import zeta_L, DavenportHeilbronn  # noqa: E402
from experiments.arithmetic_geometric.e2an_sp_object_v0 import (  # noqa: E402
    Probe, build_dh_lattice, build_zeta_lattice, detect_zeros,
    lambda_sieve, line_integrand, multiplier, multiplier_at,
)

OUT = HERE / "_out"
OUT.mkdir(exist_ok=True)

THEMES = {
    "light": dict(name="light", style="default", bg="#fbfaf7", panel="#ffffff",
                  fg="#1c1c1c", muted="#555555", blue="#1f4e8c", red="#c22040",
                  green="#1e7a34", gold="#8a6d00", goldfill="gold", grey="#595959",
                  zline="#c9c9c9", orange="#c07800",
                  cell={1: "#a9d8a9", -1: "#f2a9a9", 0: "#d9d9d9"}, celltxt="#1c1c1c"),
    "dark": dict(name="dark", style="dark_background", bg="#0e1117", panel="#131824",
                 fg="#e8e6e3", muted="#9aa4b2", blue="#6ea8ff", red="#ff6b7a",
                 green="#7bd88f", gold="#e3c05a", goldfill="#8a6d1a", grey="#b0b0b0",
                 zline="#3a4150", orange="#f0a35e",
                 cell={1: "#265c33", -1: "#6e2a35", 0: "#3a3f47"}, celltxt="#e8e6e3"),
}

_CACHE: dict = {}
FIGDATA: list[tuple[str, str, str, str]] = []   # (base, ext, title, caption)


def register(base, ext, title, caption):
    if not any(b == base for b, _, _, _ in FIGDATA):
        FIGDATA.append((base, ext, title, caption))


def save(fig, base, T, title, caption):
    fig.savefig(OUT / f"{base}__{T['name']}.png", dpi=140, bbox_inches="tight",
                facecolor=T["bg"])
    plt.close(fig)
    register(base, "png", title, caption)
    print(f"  saved {base}__{T['name']}.png")


def zeta_gammas(Tmax: float) -> np.ndarray:
    key = ("gz", Tmax)
    if key not in _CACHE:
        _CACHE[key] = np.array([float(mp.im(r)) for r in zeta_L.zeros(T_max=Tmax, prec=30)])
    return _CACHE[key]


def engine():
    if "engine" not in _CACHE:
        print("building the e2an lattice engine (integer sums)")
        lat_z = build_zeta_lattice(70000)
        lat_d = build_dh_lattice(70000)
        probe = Probe(c=1.9, sigma=0.04)
        _, integ_z = line_integrand(lat_z, probe)
        _, integ_d = line_integrand(lat_d, probe)
        _CACHE["engine"] = (lat_z, lat_d, probe, integ_z, integ_d)
    return _CACHE["engine"]


# ---------------------------------------------------------------------------
# 1. the problem in one picture
# ---------------------------------------------------------------------------

def fig1(T):
    if "f1" not in _CACHE:
        print("fig 1: computing strip grids (mpmath; ~2 min, cached across themes)")
        mp.mp.dps = 10
        sig = np.linspace(-0.5, 1.5, 90)
        tt = np.linspace(0.5, 60.0, 200)
        Z = np.empty((len(tt), len(sig)))
        for i, t in enumerate(tt):
            for j, s in enumerate(sig):
                Z[i, j] = float(mp.log10(abs(mp.zeta(mp.mpc(s, t))) + mp.mpf("1e-12")))
        dh = DavenportHeilbronn()
        sig2 = np.linspace(-0.5, 1.5, 70)
        tt2 = np.linspace(80.0, 92.0, 100)
        D = np.empty((len(tt2), len(sig2)))
        for i, t in enumerate(tt2):
            for j, s in enumerate(sig2):
                D[i, j] = float(mp.log10(abs(dh.evaluate(mp.mpc(s, t))) + mp.mpf("1e-12")))
        rhos = [complex(r) for r in dh.zeros(T_max=92.0, prec=30)]
        _CACHE["f1"] = (sig, tt, Z, sig2, tt2, D,
                        [r for r in rhos if abs(r.real - 0.5) < 0.01 and 80 <= r.imag <= 92],
                        [r for r in rhos if abs(r.real - 0.5) >= 0.01 and 80 <= r.imag <= 92])
    sig, tt, Z, sig2, tt2, D, dh_on, dh_off = _CACHE["f1"]
    gz = zeta_gammas(60.0)
    with plt.style.context(T["style"]):
        fig, axes = plt.subplots(1, 2, figsize=(12.5, 7))
        for ax, M, ss, ts, name in ((axes[0], Z, sig, tt, "Riemann zeta"),
                                    (axes[1], D, sig2, tt2, "Davenport-Heilbronn")):
            im = ax.imshow(M, origin="lower", aspect="auto", cmap="viridis",
                           extent=[ss[0], ss[-1], ts[0], ts[-1]], vmin=-3, vmax=1.2)
            ax.axvline(0.5, color="white", lw=1.0, ls="--", alpha=0.85)
            ax.set_xlabel("Re(s)")
            ax.set_title(name)
            fig.colorbar(im, ax=ax, label="log10 |f(s)|", shrink=0.85)
        axes[0].set_ylabel("Im(s)")
        axes[0].plot([0.5] * len(gz), gz, "o", ms=7, mfc="none", mec="w", mew=1.4)
        for r in dh_on:
            axes[1].plot(r.real, r.imag, "o", ms=7, mfc="none", mec="w", mew=1.4)
        for k, r in enumerate(dh_off):
            axes[1].plot(r.real, r.imag, "o", ms=11, mfc="none", mec=T["red"], mew=2.2)
            if k == 1:
                axes[1].annotate("off the line", (r.real, r.imag), color=T["red"],
                                 textcoords="offset points", xytext=(12, 10), fontsize=11)
        fig.suptitle("The problem: do zeros ever leave the line?  (dark spots = zeros)",
                     fontsize=14)
        save(fig, "01_the_problem", T, "The problem in one picture",
             "Left: |zeta(s)| on the critical strip; every dark spot (zero) sits on the dashed "
             "line Re(s) = 1/2, and RH says that never fails. Right: the Davenport-Heilbronn "
             "function, which has zeta's functional equation but NO Euler product; its zeros "
             "mostly sit on the line too, except the circled pair at Re(s) = 0.808 / 0.192, "
             "height 85.7. So leaving the line is possible in general; something about zeta "
             "specifically (the Euler product bound to the integer lattice) must forbid it. "
             "That 'something' is the whole problem.")


# ---------------------------------------------------------------------------
# 2. zeros emerging from the integers
# ---------------------------------------------------------------------------

def fig2(T):
    lat_z, _, probe, integ_z, _ = engine()
    if "f2" not in _CACHE:
        tau, m = multiplier(lat_z, probe, integrand=integ_z)
        _CACHE["f2"] = (tau, np.abs(m), detect_zeros(tau, np.abs(m)))
    tau, am, em = _CACHE["f2"]
    gz = zeta_gammas(100.0)
    with plt.style.context(T["style"]):
        fig, axes = plt.subplots(2, 1, figsize=(12.5, 7.5))
        ax = axes[0]
        ax.semilogy(tau, am, lw=0.7, color=T["blue"])
        ax.plot([g for g, _ in em], [d for _, d in em], "v", color=T["red"], ms=6)
        ax.set_xlim(0, 100)
        ax.set_ylim(1e-4, 30)
        ax.set_ylabel("|m(tau)|  (log scale)")
        ax.set_title("the multiplier extracted from  sum over n <= 70000  "
                     "(zeta itself is never evaluated)")
        ax = axes[1]
        ax.semilogy(tau, am, lw=1.0, color=T["blue"])
        for g in gz:
            ax.axvline(g, color=T["zline"], lw=0.9, zorder=0)
        ax.set_xlim(10, 32)
        ax.set_ylim(1e-4, 10)
        ax.set_xlabel("tau   (height on the critical line)")
        ax.set_ylabel("|m(tau)|")
        ax.set_title("zoom: the dips land exactly on the true zeros (vertical lines), to about 1e-4")
        fig.suptitle("Where the zeros come from: raw integer sums, Mellin-transformed", fontsize=14)
        save(fig, "02_zeros_from_integers", T, "Zeros emerging from the integers",
             "The e2an object's engine: take the plain integer lattice (n = 1..70000, nothing "
             "else), form the regularized sum of a bump over all its dilates, and Fourier-"
             "transform along the critical line. The result m(tau) IS zeta on the line, and its "
             "dips (markers = automatic detections) are the zeros, recovered to 1e-4 without "
             "ever evaluating zeta. This is the sense in which the 'hidden object' is real: its "
             "spectrum is sitting inside the integers.")


# ---------------------------------------------------------------------------
# 3. the explicit formula
# ---------------------------------------------------------------------------

def fig3(T):
    gam = zeta_gammas(200.0)
    lam = lambda_sieve(120)
    psi_true = np.concatenate([[0.0], np.cumsum(lam[1:])])
    x = np.linspace(2.0, 100.0, 4000)

    def psi_from_zeros(K):
        acc = x - np.log(2 * pi) - 0.5 * np.log(1 - x ** (-2.0))
        for g in gam[:K]:
            rho = 0.5 + 1j * g
            acc = acc - 2 * np.real(x ** rho / rho)
        return acc

    with plt.style.context(T["style"]):
        fig, axes = plt.subplots(2, 2, figsize=(13, 8.5), sharex=True, sharey=True)
        for ax, K in zip(axes.flat, [0, 10, 40, len(gam)]):
            ax.step(np.arange(len(psi_true)), psi_true, where="post", color=T["grey"],
                    lw=1.2, label="psi(x): count log p at prime powers")
            ax.plot(x, psi_from_zeros(K), color=T["red"], lw=1.1,
                    label=f"rebuilt from {K} zero pairs")
            ax.set_xlim(2, 100)
            ax.set_ylim(0, 105)
            ax.legend(loc="upper left", fontsize=9)
        for ax in axes[1]:
            ax.set_xlabel("x")
        for ax in axes[:, 0]:
            ax.set_ylabel("psi(x)")
        fig.suptitle("The explicit formula: the zeros are the music of the primes "
                     "(each zero pair is one wave; together they build the staircase)",
                     fontsize=13.5)
        save(fig, "03_explicit_formula", T, "Zeros build the primes",
             "psi(x) jumps by log p at every prime power (grey staircase). The other curve is x "
             "minus one cosine-like wave per zero pair: with 0 zeros it is just the smooth line; "
             "with 10 it wobbles; with all 91 pairs below height 200 it locks onto the staircase "
             "corner by corner, up to the finite-truncation ripple (about 0.1 at x = 10 growing "
             "to about 1 near x = 100, i.e. under one percent of the plot; more zeros shrink it: "
             "the exact identity needs them all). Zeros and primes are exact Fourier duals: this is the two-sided "
             "trace formula (SP4) as a picture, and it is why the zeros' positions are not "
             "decoration; they carry all the prime information. The animated version below "
             "adds the zeros one at a time.")


# ---------------------------------------------------------------------------
# 4. the error budget
# ---------------------------------------------------------------------------

def fig4(T):
    if "f4" not in _CACHE:
        N = 1_000_000
        lam = lambda_sieve(N)
        psi = np.cumsum(lam[1:])
        xs = np.unique(np.geomspace(100, N, 500).astype(int))
        _CACHE["f4"] = (xs, np.abs(psi[xs - 1] - xs))
    xs, err = _CACHE["f4"]
    with plt.style.context(T["style"]):
        fig, ax = plt.subplots(figsize=(11.5, 7))
        ax.loglog(xs, err, lw=1.2, color=T["blue"], label="|psi(x) - x|  (measured)")
        ax.loglog(xs, np.sqrt(xs) * np.log(xs) ** 2 / (8 * pi), "--", color=T["green"],
                  label="sqrt(x) log^2 x / 8 pi   (the RH bound)")
        ax.loglog(xs, xs ** 0.6 / 30, ":", color=T["orange"], lw=2,
                  label="x^0.6 / 30   (one zero at Re = 0.6)")
        ax.loglog(xs, xs ** 0.75 / 30, ":", color=T["red"], lw=2,
                  label="x^0.75 / 30   (one zero at Re = 0.75)")
        ax.set_xlabel("x")
        ax.set_ylabel("prime-counting error")
        ax.legend(fontsize=10)
        ax.set_title("What Re(zero) = 1/2 buys: the prime-counting error stays square-root small")
        save(fig, "04_error_budget", T, "Why Re = 1/2 matters",
             "The measured prime-counting error |psi(x) - x| (solid) hugs the square-root "
             "envelope (dashed): that containment for ALL x is exactly RH. A single zero at "
             "Re = 0.6 or 0.75 would eventually force the error up the dotted lines: one rogue "
             "zero permanently worsens every prime estimate. This is also why no finite "
             "computation settles RH from the prime side: an off-line zero high in the strip "
             "only separates from the square-root envelope at astronomically large x (the "
             "primes thread measured that a zero above height 3e12 needs x ~ 10^150 to "
             "surface). The animated version below drags a zero off the line and watches "
             "the damage grow.")


# ---------------------------------------------------------------------------
# 5. the SP scorecard
# ---------------------------------------------------------------------------

def fig5(T):
    rows = ["SP1 trace realization", "SP1c duality (FE)", "H0: pole = density",
            "descent converges", "SP2 spectrum emerges", "SP2 completeness",
            "SP3 Euler (b_n support)", "SP4 trace formula", "SP5 positivity margin"]
    cols = ["zeta", "D-H\n(FE, no Euler)", "Beurling\n(Euler, no lattice)"]
    Vals = [[+1, +1, +1], [+1, +1, -1], [+1, +1, +1], [+1, +1, -1], [+1, +1, -1],
            [0, -1, -1], [+1, -1, +1], [+1, -1, -1], [0, -1, -1]]
    Lbls = [["2.5e-12", "7.7e-14", "finite scale"],
            ["2.4e-11", "2.2e-11", "defect 0.67"],
            ["R = 1.000", "R = 0 (entire)", "R = its density"],
            ["drift 2e-12", "ok", "drift 0.51"],
            ["29/29 to T=100", "100% on-line", "unstable"],
            ["= RH (open)", "off-line invisible", "n/a"],
            ["b = Lambda exact", "b_6 = 1.94 leak", "exact on semigroup"],
            ["resid 1e-7", "not posable", "no Gamma factor"],
            ["margin 0 at fp", "indefinite", "not well-posed"]]
    with plt.style.context(T["style"]):
        fig, ax = plt.subplots(figsize=(11.5, 7.5))
        for i in range(len(rows)):
            for j in range(3):
                ax.add_patch(plt.Rectangle((j, len(rows) - 1 - i), 1, 1,
                                           color=T["cell"][Vals[i][j]], ec=T["bg"], lw=2))
                ax.text(j + 0.5, len(rows) - 1 - i + 0.5, Lbls[i][j], ha="center",
                        va="center", fontsize=9.5, color=T["celltxt"])
        ax.set_xlim(0, 3)
        ax.set_ylim(0, len(rows))
        ax.set_xticks([0.5, 1.5, 2.5])
        ax.set_xticklabels(cols, fontsize=11)
        ax.set_yticks([len(rows) - 1 - i + 0.5 for i in range(len(rows))])
        ax.set_yticklabels(rows, fontsize=10.5)
        ax.set_title("The assembled object, scored per component (green = passes, red = fails, "
                     "grey = the open joint)\none pipeline, three systems (e2an, LEARNINGS #179)",
                     fontsize=12)
        ax.tick_params(length=0)
        for s in ax.spines.values():
            s.set_visible(False)
        save(fig, "05_sp_scorecard", T, "The five-component scorecard",
             "The missing object has five components (carrier, endomorphism, base, trace "
             "formula, polarization). We built one and ran zeta plus both controls through "
             "identical code. Read the columns: D-H passes every functional-equation cell and "
             "fails every Euler cell; Beurling exactly the mirror. Zeta alone fills the column, "
             "and its two grey cells are the two open joints: completeness of the spectrum "
             "(that IS RH) and the uniform positivity margin (M4). A proof has to turn exactly "
             "those two cells green.")


# ---------------------------------------------------------------------------
# 6. the margin law
# ---------------------------------------------------------------------------

def fig6(T):
    d = np.load(ROOT / "experiments/arithmetic_geometric/e2ao_scaling_ladder.npz")
    sig, mz, floor = d["sigmas"], d["margin_zero"], d["assembly_err"]
    ss = np.linspace(0.15, 0.75, 200)
    law = 4 * np.sqrt(pi) * ss * np.exp(-14.134725 ** 2 * ss ** 2)
    with plt.style.context(T["style"]):
        fig, ax = plt.subplots(figsize=(11.5, 7))
        ax.semilogy(sig, mz, "o", ms=9, color=T["blue"], label="measured margin (exact side)")
        ax.semilogy(ss, law, "-", color=T["red"], lw=1.5,
                    label="closed form  4 sqrt(pi) sigma exp(-gamma_1^2 sigma^2)")
        ax.semilogy(sig, floor, "s--", color=T["grey"], ms=6,
                    label="prime-side assembly floor (certification limit)")
        ax.axvspan(0.15, 0.27, color=T["green"], alpha=0.13)
        ax.axvspan(0.27, 0.75, color=T["red"], alpha=0.08)
        ax.text(0.185, 1e-30, "certifiable", color=T["green"], fontsize=12)
        ax.text(0.5, 1e-30, "margin exists but cannot be certified\nfrom the prime side "
                "at this precision", color=T["red"], fontsize=12, ha="center")
        ax.set_xlabel("window scale sigma")
        ax.set_ylabel("Weil-form margin per unit L2 mass")
        ax.set_ylim(1e-45, 1)
        ax.legend(fontsize=10, loc="upper right")
        ax.set_title("The positivity margin vs window size: exact law, and the exponential "
                     "cost of certifying it (e2ao, LEARNINGS #180)")
        save(fig, "06_margin_law", T, "The margin law and its price",
             "RH is equivalent to a quadratic form staying nonnegative on every window. "
             "Measured: the form's margin (dots) follows the closed form margin = 4 sqrt(pi) "
             "sigma exp(-gamma_1^2 sigma^2), shrinking by a factor ~10^38 across this plot "
             "while staying positive. The squares are the best precision our prime-side "
             "assembly achieves: right of the crossing, the margin is smaller than any error "
             "bar, so positivity exists but cannot be certified from prime data at that "
             "precision. The proof RH needs is exactly a way to certify this ever-thinner "
             "positivity uniformly: that is M4, and this picture is its price tag.")


# ---------------------------------------------------------------------------
# 7. the central hole
# ---------------------------------------------------------------------------

def fig7(T):
    g1 = 14.134725
    gz = zeta_gammas(60.0)
    t = np.linspace(-45, 45, 2000)
    sigma = 0.35
    gh = np.exp(-sigma ** 2 * t ** 2 / 2)
    with plt.style.context(T["style"]):
        fig, ax = plt.subplots(figsize=(12, 5.6))
        for g in np.concatenate([gz, -gz]):
            if abs(g) <= 45:
                ax.axvline(g, color=T["zline"], lw=1.4)
        ax.axvspan(-g1, g1, color=T["goldfill"], alpha=0.18)
        ax.fill_between(t, gh, color=T["blue"], alpha=0.35)
        ax.plot(t, gh, color=T["blue"], lw=1.5)
        ax.annotate("the spectral hole: no zeros in (-14.13, 14.13)", (0, 1.045),
                    ha="center", fontsize=11.5, color=T["gold"])
        ax.annotate("window mode parked in the hole\n(width 1/sigma)", (0, 0.55),
                    ha="center", fontsize=10.5, color=T["blue"])
        ax.annotate("(the pole also lives at the center, but the explicit formula\n"
                    "cancels it exactly: the hole is genuinely free)", (0, 0.30),
                    ha="center", fontsize=10, color=T["muted"])
        ax.annotate("only this leakage onto the first zero\nis charged:  "
                    "exp(-gamma_1^2 sigma^2)",
                    (g1, float(np.exp(-sigma ** 2 * g1 ** 2 / 2))),
                    textcoords="offset points", xytext=(15, 45), fontsize=10.5,
                    color=T["red"], arrowprops=dict(arrowstyle="->", color=T["red"]))
        ax.set_xlim(-45, 45)
        ax.set_ylim(0, 1.12)
        ax.set_xlabel("tau  (spectral axis; vertical lines = zeros at +/- gamma_k)")
        ax.set_yticks([])
        ax.set_title("Why the margin decays like exp(-gamma_1^2 sigma^2): "
                     "the worst window hides in the central hole")
        save(fig, "07_central_hole", T, "The central hole",
             "The margin's whole size is geometry: the zero set (vertical comb) has its deepest "
             "hole in the middle, radius gamma_1 = 14.13, because zeros come in +/- pairs. A "
             "window mode of scale sigma parks its spectral mass there and only pays for its "
             "Gaussian tail leaking onto the first zero: exp(-gamma_1^2 sigma^2). The naive "
             "guess said the pole at the center would forbid parking there; measurement refuted "
             "it: the explicit formula cancels the pole exactly. Wider windows hide deeper, the "
             "margin thins forever but never hits zero: RH is the claim that this never fails, "
             "on any window. The animated version below narrows the window live.")


# ---------------------------------------------------------------------------
# 8. the carrier
# ---------------------------------------------------------------------------

def fig8(T):
    lat_z, lat_d, probe, integ_z, integ_d = engine()
    gz = zeta_gammas(100.0)
    if "f8" not in _CACHE:
        data = {}
        for L in (8.0, 16.0):
            ks = np.arange(1, int(100 * L / (2 * pi)) + 1)
            tk = 2 * pi * ks / L
            data[L] = (tk, np.abs(multiplier_at(lat_z, probe, tk, integrand=integ_z)),
                       np.abs(multiplier_at(lat_d, probe, tk, integrand=integ_d)))
        _CACHE["f8"] = data
    data = _CACHE["f8"]
    with plt.style.context(T["style"]):
        fig, axes = plt.subplots(2, 2, figsize=(13, 8), width_ratios=[2, 1])
        for row, L in enumerate((8.0, 16.0)):
            tk, mz, md = data[L]
            ax = axes[row, 0]
            ax.semilogy(tk, mz, "o-", ms=3.5, lw=0.6, color=T["blue"])
            for g in gz:
                ax.axvline(g, color=T["zline"], lw=0.8, zorder=0)
            ax.set_xlim(5, 100)
            ax.set_ylim(1e-3, 30)
            ax.set_ylabel(f"L = {L:.0f}\n|m| on the grid")
            if row == 0:
                ax.set_title("zeta: the circle carrier (grid step 2 pi / L)")
            ax = axes[row, 1]
            ax.semilogy(tk, md, "o-", ms=3.5, lw=0.6, color=T["grey"])
            ax.axvspan(85.2, 86.2, color=T["red"], alpha=0.2)
            ax.plot([85.699], [0.35], "*", color=T["red"], ms=16)
            ax.set_xlim(80, 92)
            ax.set_ylim(1e-3, 30)
            if row == 0:
                ax.set_title("D-H near its off-line pair")
        axes[1, 0].set_xlabel("tau")
        axes[1, 1].set_xlabel("tau")
        fig.suptitle("The finite carrier: on-line zeros appear as the grid refines; "
                     "the off-line pair (star) NEVER makes a dip, at any circumference",
                     fontsize=13)
        save(fig, "08_carrier", T, "The carrier and its blind spot",
             "The object's carrier is a circle whose Fourier grid samples the critical line; "
             "bigger circumference = finer grid = more zeros resolved (left, zeta at L = 8 vs "
             "16; vertical lines are true zeros). Right: the same carrier for D-H around height "
             "85.7. Its off-line pair (star, at Re = 0.808) produces NO dip in the shaded band "
             "at either circumference: values on the line stay around 0.24 of local scale. The "
             "carrier lives ON the line, so it can only ever see on-line zeros: proving its "
             "spectrum is COMPLETE is literally proving RH. That is the C1 joint, drawn. The "
             "animated version below slides L continuously.")


# ---------------------------------------------------------------------------
# 13. the GUE statistics: the agreement, and its exact blindness
# ---------------------------------------------------------------------------

def gue_data():
    """~30k zeros near height 1e6 from the primes-thread Riemann-Siegel engine,
    with unfolded spacings and the empirical pair correlation."""
    if "gue" not in _CACHE:
        from experiments.primes import rsz
        print("fig 13: computing ~30k zeros near height 1e6 (rsz engine)")
        t0 = 1.0e6
        g = rsz.zeros_in(t0, t0 + 15750.0)
        s = rsz.unfold(g)
        u, r2 = rsz.pair_correlation(s, umax=3.0, nbins=60)
        _CACHE["gue"] = (g, s, u, r2)
        print(f"  {len(g)} zeros, mean unfolded spacing {float(np.mean(s)):.4f}")
    return _CACHE["gue"]


def fig13(T):
    from experiments.primes import rsz
    g, s, u, r2 = gue_data()
    sx = np.linspace(0, 3.5, 400)
    with plt.style.context(T["style"]):
        fig, (axl, axr) = plt.subplots(1, 2, figsize=(12.5, 5.8))
        axl.hist(s, bins=np.linspace(0, 3.5, 46), density=True, color=T["blue"],
                 alpha=0.55, label=f"{len(g):,} zeros near height 1e6")
        axl.plot(sx, rsz.wigner_gue(sx), color=T["red"], lw=2,
                 label="GUE random-matrix prediction")
        axl.plot(sx, np.exp(-sx), "--", color=T["grey"], lw=1.5,
                 label="uncorrelated (Poisson) foil")
        axl.set_xlabel("gap to the next zero  (unit mean)")
        axl.set_ylabel("probability density")
        axl.set_title("consecutive-gap distribution")
        axl.legend(fontsize=9)
        axr.plot(u, r2, "o", ms=4, color=T["blue"], label="measured pair correlation")
        axr.plot(sx, rsz.sine_kernel(sx), color=T["red"], lw=2,
                 label="Montgomery / GUE sine kernel")
        axr.axhline(1.0, ls="--", color=T["grey"], lw=1.5, label="Poisson foil")
        axr.set_xlim(0, 3)
        axr.set_ylim(0, 1.25)
        axr.set_xlabel("distance between zeros  (unit mean)")
        axr.set_ylabel("relative pair density")
        axr.set_title("two-point correlation")
        axr.legend(fontsize=9, loc="lower right")
        fig.suptitle("The zeros repel like eigenvalues of a random Hermitian matrix "
                     "(computed locally; the Hilbert-Polya hint)", fontsize=13.5)
        save(fig, "13_gue_agreement", T, "The GUE statistics: the operator hint",
             "Roughly thirty thousand zeros near height one million, computed here by the "
             "primes thread's Riemann-Siegel engine. Left: the gaps between consecutive "
             "zeros avoid zero (repulsion) and follow the GUE random-matrix curve, not the "
             "uncorrelated foil. Right: the two-point correlation matches Montgomery's sine "
             "kernel. This is the strongest hint that the zeros are the spectrum of a hidden "
             "self-adjoint operator. The essential caveat is the next entry: this entire "
             "picture is computed from the zeros' HEIGHTS alone, so it is provably blind to "
             "the one thing RH asserts.")


# ---------------------------------------------------------------------------
# 15. the polar picture: zeta as a curve threading the origin
# ---------------------------------------------------------------------------

def polar_data():
    """zeta trajectories via mpmath everywhere. (The Riemann-Siegel engine is
    NOT usable here: its asymptotic main sum is empty below t ~ 2 pi, and the
    curve's low-t arc from zeta(1/2) = -1.4604 is exactly what these pictures
    must get right. Verified against the classical reference plot.)"""
    if "polar" not in _CACHE:
        print("fig 15: zeta trajectories (mpmath; ~20 s, cached across themes)")
        mp.mp.dps = 12
        t = np.arange(0.0, 50.0, 0.02)
        zline = np.array([complex(mp.zeta(mp.mpc(0.5, tt))) for tt in t])
        tm = np.arange(0.0, 50.0, 0.05)
        sigmas = np.round(np.linspace(0.5, 0.75, 26), 4)
        fam = {}
        for sg in sigmas:
            if abs(sg - 0.5) < 1e-9:
                fam[sg] = np.interp(tm, t, zline.real) + 1j * np.interp(tm, t, zline.imag)
            else:
                fam[sg] = np.array([complex(mp.zeta(mp.mpc(sg, tt))) for tt in tm])
        _CACHE["polar"] = (t, zline, tm, sigmas, fam)
    return _CACHE["polar"]


def _traj(ax, z, tvals, T, cmap="viridis"):
    from matplotlib.collections import LineCollection
    pts = np.column_stack([z.real, z.imag]).reshape(-1, 1, 2)
    segs = np.concatenate([pts[:-1], pts[1:]], axis=1)
    lc = LineCollection(segs, cmap=cmap, array=tvals[:-1], lw=1.3)
    ax.add_collection(lc)
    ax.plot([0], [0], "+", ms=14, mew=2.2, color=T["red"], zorder=5)
    ax.set_xlim(-3.2, 5.0)
    ax.set_ylim(-3.6, 3.6)
    ax.set_aspect("equal")
    ax.set_xlabel("Re zeta")
    return lc


def fig15(T):
    t, zline, tm, sigmas, fam = polar_data()
    gz = zeta_gammas(50.0)
    with plt.style.context(T["style"]):
        fig, (axl, axr) = plt.subplots(1, 2, figsize=(12.5, 6.4))
        lc = _traj(axl, zline, t, T)
        axl.set_ylabel("Im zeta")
        axl.set_title(f"on the critical line: {len(gz)} passes through 0 for t <= 50\n"
                      "(every pass through the cross IS a zero)")
        z75 = fam[sigmas[-1]]
        _traj(axr, z75, tm, T)
        axr.set_title("at Re(s) = 0.75: the curve loops and loops\nand never returns to 0")
        cb = fig.colorbar(lc, ax=[axl, axr], shrink=0.8, pad=0.02)
        cb.set_label("t  (height)")
        fig.suptitle("zeta as a moving point: s = sigma + i t, t running upward", fontsize=13.5)
        save(fig, "15_polar_line", T, "The polar picture: threading the origin",
             "Fix the real part and let t run: zeta(sigma + i t) traces a curve in the "
             "complex plane (color = height). On the critical line (left) the curve spirals "
             "and keeps threading the origin: ten exact passes below t = 50, one per zero. "
             "At Re(s) = 0.75 (right) the same function loops endlessly but never touches "
             "the cross. RH is the statement that the coming-home-to-zero behaviour happens "
             "ONLY at Re(s) = 1/2: the animated version below traces the curve live and "
             "then slides the real part, watching the origin passes detach.")


# ---------------------------------------------------------------------------
# 17. the phase plot: arg zeta over the plane (Wegert-style domain coloring)
# ---------------------------------------------------------------------------

def fig17(T):
    if "phase" not in _CACHE:
        print("fig 17: phase grid (mpmath; ~1-2 min, cached across themes)")
        mp.mp.dps = 8
        sig = np.linspace(-5.5, 3.5, 150)
        tt = np.linspace(0.02, 40.0, 420)
        A = np.empty((len(tt), len(sig)))
        for i, t in enumerate(tt):
            for j, s in enumerate(sig):
                A[i, j] = float(mp.arg(mp.zeta(mp.mpc(s, t))))
        _CACHE["phase"] = (sig, tt, A)
    sig, tt, A = _CACHE["phase"]
    gz = zeta_gammas(40.0)
    with plt.style.context(T["style"]):
        fig, ax = plt.subplots(figsize=(10.5, 8))
        ax.imshow((A + pi) / (2 * pi), origin="lower", aspect="auto", cmap="hsv",
                  extent=[sig[0], sig[-1], tt[0], tt[-1]], interpolation="bilinear")
        ax.axvline(0.5, color="k", lw=0.8, ls="--", alpha=0.6)
        ax.plot([0.5] * len(gz), gz, "o", ms=9, mfc="none", mec="k", mew=1.6)
        ax.plot([-2, -4], [0.35, 0.35], "o", ms=9, mfc="none", mec="k", mew=1.6)
        ax.plot([1], [0.35], "s", ms=9, mfc="none", mec="k", mew=1.9)
        ax.annotate("trivial zeros", (-3, 1.2), ha="center", fontsize=10, color="k")
        ax.annotate("pole", (1.15, 1.4), fontsize=10, color="k")
        ax.set_xlabel("Re(s)")
        ax.set_ylabel("Im(s)")
        ax.set_title("the phase of zeta: hue = arg zeta(s); every color pinwheel is a zero, "
                     "the pole winds the other way")
        save(fig, "17_phase_plot", T, "The phase plot: zeros as pinwheels",
             "Color every point by the ANGLE of zeta(s) (hue runs one full cycle as the "
             "angle does). A zero is a point where all colors meet, winding counter-"
             "clockwise (circles: the trivial zeros at -2, -4 and the critical-line zeros); "
             "the pole at s = 1 is the reverse pinwheel (square). Counting zeros inside a "
             "region = counting how often the color wheel turns along its boundary (the "
             "argument principle): this picture is literally how N(T) is computed, and it "
             "makes visible that zeros are topological objects: they cannot quietly vanish, "
             "only move. RH says all the on-strip pinwheels sit on the dashed line.")


# ---------------------------------------------------------------------------
# 18. zeros hear the primes: the dual spike plot (instrument)
# ---------------------------------------------------------------------------

def fig18(T):
    from experiments.primes import rsz
    if "spikes" not in _CACHE:
        print("fig 18: ~8900 zeros (rsz), then the trigonometric sum over them")
        g = rsz.zeros_in(10.0, 9000.0)
        w = 0.5 * (1 + np.cos(pi * np.arange(len(g)) / len(g)))     # Hann taper
        t = np.linspace(0.2, 4.6, 6000)
        S = np.zeros_like(t)
        for i in range(0, len(g), 800):
            S = S + (w[i:i + 800, None] * np.cos(np.outer(g[i:i + 800], t))).sum(axis=0)
        P = np.abs(S) / np.sum(w)
        _CACHE["spikes"] = (g, t, P)
    g, t, P = _CACHE["spikes"]
    lam = lambda_sieve(105)
    npow = [n for n in range(2, 100) if lam[n] > 0]
    pred = np.array([lam[n] / np.sqrt(n) for n in npow])
    # scale the predicted comb to the measured log-2 peak
    i2 = np.argmin(np.abs(t - log(2)))
    scale = P[max(0, i2 - 5):i2 + 6].max() / pred[0]
    with plt.style.context(T["style"]):
        fig, ax = plt.subplots(figsize=(12.5, 6.2))
        ax.plot(t, P, lw=0.9, color=T["blue"],
                label=f"|weighted sum of cos(t gamma)| over {len(g)} zeros")
        ml, sl, bl = ax.stem([log(n) for n in npow], pred * scale,
                             linefmt="-", markerfmt=" ", basefmt=" ")
        plt.setp(sl, color=T["red"], alpha=0.75, lw=1.6)
        for n in (2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 25, 27, 32, 49, 64, 81):
            ax.annotate(str(n), (log(n), pred[npow.index(n)] * scale),
                        textcoords="offset points", xytext=(0, 5),
                        ha="center", fontsize=8.5, color=T["red"])
        ax.set_xlim(0.2, 4.6)
        ax.set_ylim(0, None)
        ax.set_xlabel("t   (the spike at t = log n)")
        ax.set_ylabel("spectral power of the zeros")
        ax.legend(fontsize=10, loc="upper right")
        ax.set_title("the zeros, summed as pure tones, spike EXACTLY at log(prime powers), "
                     "with heights Lambda(n)/sqrt(n)")
        save(fig, "18_zeros_hear_primes", T, "The zeros hear the primes",
             "The reverse direction of figure 2: there, integer sums produced the zeros; "
             "here, sum cos(t gamma) over 8,880 zeros (computed locally) and the result "
             "spikes at t = log 2, log 3, log 4, log 5 ... : every prime POWER announces "
             "itself, with the predicted heights Lambda(n)/sqrt(n) (red comb, one scale "
             "factor fitted at log 2, all other heights then forced). This is the explicit "
             "formula read backwards, and it sharpens the GUE lesson of entry 14: the "
             "zeros' statistics DO carry arithmetic (these spikes are invisible to pure "
             "random-matrix universality), yet consume only the heights, so even THIS "
             "cannot see the real parts. The conservation law, drawn from the statistics "
             "side.")


# ---------------------------------------------------------------------------
# 19. Z(t), Gram points, and the Lehmer near-miss
# ---------------------------------------------------------------------------

def fig19(T):
    from experiments.primes import rsz
    if "zt" not in _CACHE:
        t1 = np.arange(10.0, 110.0, 0.01)
        z1 = rsz.zed(t1)
        ng = np.arange(-1, 300)
        gp = rsz.gram_point(ng)
        sel = (gp >= 10.0) & (gp <= 110.0)
        gp, ng = gp[sel], ng[sel]
        zg = rsz.zed(gp)
        t2 = np.arange(7004.0, 7006.2, 0.0005)
        z2 = rsz.zed(t2)
        _CACHE["zt"] = (t1, z1, gp, ng, zg, t2, z2)
    t1, z1, gp, ng, zg, t2, z2 = _CACHE["zt"]
    gram_ok = np.sign(zg) == np.where(ng % 2 == 0, 1.0, -1.0)
    with plt.style.context(T["style"]):
        fig, (ax, axl) = plt.subplots(2, 1, figsize=(12.5, 8))
        ax.plot(t1, z1, lw=0.8, color=T["blue"])
        ax.axhline(0, color=T["muted"], lw=0.8)
        ax.plot(gp[gram_ok], np.zeros(int(gram_ok.sum())), "|", ms=12, color=T["green"],
                label="Gram points (sign as predicted)")
        if (~gram_ok).any():
            ax.plot(gp[~gram_ok], np.zeros(int((~gram_ok).sum())), "|", ms=12,
                    color=T["red"], label="Gram's law fails")
        ax.set_xlim(10, 110)
        ax.set_xlabel("t")
        ax.set_ylabel("Z(t)")
        ax.legend(fontsize=9, loc="upper right")
        ax.set_title("Z(t): a REAL function whose sign changes are the zeros "
                     "(this is what certified verification walks)")
        axl.plot(t2, z2, lw=1.1, color=T["blue"])
        axl.axhline(0, color=T["muted"], lw=0.8)
        # the close pair: the two sign changes inside [7005.0, 7005.2]
        win = (t2 >= 7005.0) & (t2 <= 7005.2)
        tw, zw = t2[win], z2[win]
        ic = np.flatnonzero(np.sign(zw[:-1]) != np.sign(zw[1:]))
        z1p, z2p = float(tw[ic[0]]), float(tw[ic[1]])
        between = (tw > z1p) & (tw < z2p)
        ext = float(zw[between][np.argmax(np.abs(zw[between]))])
        axl.annotate("the Lehmer pair: two zeros "
                     f"{z2p - z1p:.3f} apart;\nbetween them Z barely reaches {ext:.4f}\n"
                     "(see the zoom)", (7005.08, 0.0),
                     textcoords="offset points", xytext=(-190, -60), fontsize=10.5,
                     color=T["red"], arrowprops=dict(arrowstyle="->", color=T["red"]))
        axi = axl.inset_axes([0.60, 0.55, 0.37, 0.42])
        axi.plot(t2, z2, lw=1.2, color=T["blue"])
        axi.axhline(0, color=T["muted"], lw=0.7)
        axi.set_xlim(7005.02, 7005.15)
        axi.set_ylim(-0.012, 0.006)
        axi.set_title("zoom: the arch", fontsize=9)
        axi.tick_params(labelsize=7)
        axl.set_xlim(7004.0, 7006.2)
        axl.set_ylim(-1.2, 1.2)
        axl.set_xlabel("t")
        axl.set_ylabel("Z(t)")
        axl.set_title("Lehmer's phenomenon: RH survives here by less than 0.005")
        save(fig, "19_zt_gram", T, "Z(t), Gram points, and the Lehmer near-miss",
             "Top: the Riemann-Siegel Z function, a real rotation of zeta on the line; "
             "every sign change is a zero, which is how this repo's certified verification "
             "walked 118.5 million of them. Ticks mark Gram points, where Z is 'supposed' "
             "to alternate sign; the red ones are Gram-law failures (about 15 percent "
             "eventually). Bottom: the famous Lehmer pair near t = 7005: two zeros only "
             "0.04 apart, with |Z| between them under five thousandths. If that little arch "
             "had failed to cross, RH would be false. Nothing protects it in any proven "
             "way: this is what the missing positivity has to forbid, forever.")


# ---------------------------------------------------------------------------
# 20. the near-failure direction: the Weil form's ground state (instrument)
# ---------------------------------------------------------------------------

def ground_state(sigma: float, cutoff: float = 1e-10):
    """Generalized bottom eigenvector of the zero-side Weil Gram against the
    L2 Gram, on the modulated-Gaussian window basis (zeros to T = 200, basis
    small enough that the Gram has full rank: no truncation-null ambiguity)."""
    gz = zeta_gammas(200.0)
    domega = 1.0 / (2.0 * sigma)
    omegas = np.arange(0.0, 34.0 + 1e-9, domega)
    W1, W2 = np.meshgrid(omegas, omegas, indexing="ij")
    G = (sigma * np.sqrt(pi) / 2) * (np.exp(-sigma ** 2 * (W1 - W2) ** 2 / 4)
                                     + np.exp(-sigma ** 2 * (W1 + W2) ** 2 / 4))
    def ghat(w, tv):
        return sigma * np.sqrt(pi / 2) * (np.exp(-sigma ** 2 * (tv - w) ** 2 / 2)
                                          + np.exp(-sigma ** 2 * (tv + w) ** 2 / 2))
    tab = np.array([ghat(w, gz) for w in omegas])
    Qz = 2.0 * tab @ tab.T
    wG, V = np.linalg.eigh(G)
    keep = wG > cutoff * wG[-1]
    Wm = V[:, keep] / np.sqrt(wG[keep])
    ev, U = np.linalg.eigh(Wm.T @ Qz @ Wm)
    c = Wm @ U[:, 0]                       # G-normalized: c'Gc = 1
    return omegas, c, float(ev[0])


def ground_state_mp(sigma: float = 0.55, dps: int = 50):
    """High-precision minimizer. Needed because the margin at this scale
    (~1e-26) sits far below double precision AND below what float-accurate
    zeros can support, so both the arithmetic and the zeros run at `dps`
    digits. Zeros are disk-cached across runs."""
    import json
    zcache = OUT / "_zeros_dps50.json"
    mp.mp.dps = dps
    if zcache.exists():
        gz = [mp.mpf(s) for s in json.loads(zcache.read_text())]
    else:
        print(f"  computing 91 zeros at {dps} digits (one-time, disk-cached)")
        gz = []
        k = 1
        while True:
            z = mp.zetazero(k)
            if mp.im(z) > 200:
                break
            gz.append(mp.im(z))
            k += 1
        zcache.write_text(json.dumps([mp.nstr(g, dps) for g in gz]))
    domega = 1.0 / (2.0 * sigma)
    omegas = np.arange(0.0, 34.0 + 1e-9, domega)
    J = len(omegas)
    sg = mp.mpf(sigma)
    G = mp.zeros(J, J)
    for a in range(J):
        for b in range(J):
            wa, wb = mp.mpf(omegas[a]), mp.mpf(omegas[b])
            G[a, b] = (sg * mp.sqrt(mp.pi) / 2) * (mp.e**(-sg**2 * (wa - wb)**2 / 4)
                                                   + mp.e**(-sg**2 * (wa + wb)**2 / 4))
    tab = mp.zeros(J, len(gz))
    for a in range(J):
        wa = mp.mpf(omegas[a])
        for b, g in enumerate(gz):
            tab[a, b] = sg * mp.sqrt(mp.pi / 2) * (mp.e**(-sg**2 * (g - wa)**2 / 2)
                                                   + mp.e**(-sg**2 * (g + wa)**2 / 2))
    Qz = 2 * tab * tab.T
    L = mp.cholesky(G)
    Li = mp.inverse(L)
    A = Li * Qz * Li.T
    E, V = mp.eigsy(A)
    i0 = min(range(J), key=lambda i: E[i])
    v = mp.matrix([V[r, i0] for r in range(J)])
    c = Li.T * v
    cf = np.array([float(c[r]) for r in range(J)])
    norm = float(mp.re((c.T * (G * c))[0]))
    lg = float(mp.log10(abs(E[i0]))) if E[i0] != 0 else float("-inf")
    return omegas, cf / np.sqrt(norm), lg


def _nodes(tv, gh):
    i = np.flatnonzero(np.sign(gh[:-1]) != np.sign(gh[1:]))
    return tv[i]


def fig20(T):
    if "gs" not in _CACHE:
        print("fig 20: ground states of the window Weil form across scales")
        GS = {sg: ground_state(sg)[:2] for sg in (0.20, 0.25, 0.30, 0.35)}
        print("  50-digit solves at sigma = 0.45, 0.55 (margins below fp need real precision)")
        om45, cf45, lg45 = ground_state_mp(0.45)
        om, cf, lg = ground_state_mp(0.55)
        GS[0.55] = (om, cf)
        slope = (lg - lg45) * np.log(10) / (0.55 ** 2 - 0.45 ** 2)
        print(f"  multi-mode margin: 1e{lg45:.1f} at 0.45, 1e{lg:.1f} at 0.55; "
              f"implied exponent {slope:.0f} per sigma^2 (single-mode law: -199.8)")
        # locking metric, both directions: does every zero get a node, and how
        # many of the minimizer's nodes sit on zeros vs free in the central hole
        gzz = zeta_gammas(60.0)
        gz_band = gzz[gzz <= 38.0]
        tvv = np.linspace(1.0, 38.0, 8000)
        for sg, (omg, cc) in sorted(GS.items()):
            gh = np.zeros_like(tvv)
            for w, co in zip(omg, cc):
                gh += co * sg * np.sqrt(pi / 2) * (np.exp(-sg**2 * (tvv - w)**2 / 2)
                                                   + np.exp(-sg**2 * (tvv + w)**2 / 2))
            nd = _nodes(tvv, gh)
            if len(nd):
                z2n = [float(np.min(np.abs(nd - g))) for g in gz_band]
                in_hole = int(np.sum(nd < 14.0))
                print(f"  sigma = {sg}: every-zero-gets-a-node max dist = "
                      f"{max(z2n):.3f} (median {np.median(z2n):.3f}); "
                      f"{in_hole}/{len(nd)} nodes free inside the hole")
        _CACHE["gs"] = GS
    GS = _CACHE["gs"]
    gz = zeta_gammas(60.0)
    lam = lambda_sieve(60)
    tv = np.linspace(0, 55, 3000)
    x = np.arange(-14.0, 14.0, 2e-3)
    with plt.style.context(T["style"]):
        fig, (axs, axa) = plt.subplots(2, 1, figsize=(12.5, 9))
        for k, (sg, (omegas, c)) in enumerate(sorted(GS.items())):
            gh = np.zeros_like(tv)
            for w, cc in zip(omegas, c):
                gh += cc * sg * np.sqrt(pi / 2) * (np.exp(-sg ** 2 * (tv - w) ** 2 / 2)
                                                   + np.exp(-sg ** 2 * (tv + w) ** 2 / 2))
            gh = gh / np.max(np.abs(gh)) * (1 if gh[np.argmax(np.abs(gh))] > 0 else -1)
            axs.plot(tv, gh + 2.2 * k, lw=1.1, color=T["blue"])
            tag = f"sigma = {sg}" + ("  (50-digit solve)" if sg > 0.5 else "")
            axs.text(45.5, 2.2 * k + 0.35, tag, fontsize=10, color=T["fg"])
            axs.axhline(2.2 * k, color=T["muted"], lw=0.4)
            gx = np.zeros_like(x)
            for w, cc in zip(omegas, c):
                gx += cc * np.exp(-x * x / (2 * sg ** 2)) * np.cos(w * x)
            from scipy.signal import fftconvolve
            corr = fftconvolve(gx, gx) * 2e-3
            xc = np.arange(len(corr)) * 2e-3 + 2 * x[0]
            corr = corr / np.max(np.abs(corr))
            sel = (xc >= 0) & (xc <= 5.0)
            axa.plot(xc[sel], corr[sel] + 1.4 * k, lw=1.1, color=T["blue"])
            axa.text(4.55, 1.4 * k + 0.28, f"sigma = {sg}", fontsize=10, color=T["fg"])
            axa.axhline(1.4 * k, color=T["muted"], lw=0.4)
        for g in gz:
            axs.axvline(g, color=T["zline"], lw=0.9, zorder=0)
        axs.set_xlim(0, 55)
        axs.set_xlabel("tau   (vertical lines = the zeros)")
        axs.set_ylabel("ghat of the ground state (stacked)")
        axs.set_title("the spectral shape of the ALMOST-NEGATIVE direction, as the window grows")
        for n in range(2, 55):
            if lam[n] > 0:
                axa.axvline(log(n), color=T["zline"], lw=0.9, zorder=0)
                if n in (2, 3, 4, 5, 7, 8, 9, 11, 16, 32):
                    axa.text(log(n), -0.75, str(n), ha="center", fontsize=8,
                             color=T["muted"])
        axa.set_xlim(0, 5)
        axa.set_xlabel("x   (vertical lines = log of prime powers; the Weil form's prime "
                       "term samples the autocorrelation exactly there)")
        axa.set_ylabel("autocorrelation (stacked)")
        save(fig, "20_ground_state", T, "The near-failure direction (instrument)",
             "A research instrument, not an illustration. For each window scale, solve for "
             "the function on which the Weil form is SMALLEST per unit mass: the direction "
             "in which positivity almost fails, i.e. M4's hardest direction at that scale. "
             "Three measured facts from this instrument's first runs. (i) At EVERY scale "
             "the minimizer places a node on every zero its frequency band can reach, to "
             "0.004: it interpolate-vanishes on the spectrum, always; its surplus freedom "
             "(0 of 6 nodes at sigma 0.2, 13 of 32 at 0.55) parks inside the central hole "
             "where the form cannot charge it. (ii) Because of that, the multi-mode margin "
             "SATURATES in sigma (measured exponent -12 per sigma^2 against the "
             "single-mode law's -199.8): the bottom is set by the leak past the frequency "
             "CEILING onto the first unreachable zero, so the honest scaling variable for "
             "the full space is the band ceiling, not the window width: a second law, "
             "distinct from entry 6's. (iii) Beyond sigma ~ 0.45 the margin sits so far "
             "below double precision that a naive solve returns an arbitrary member of a "
             "numerical null cone, so the large-scale curves here are 50-digit solves on "
             "50-digit zeros: the certification-cost law at the eigenvector level. "
             "Bottom panel: the minimizer's autocorrelation, which is exactly what the "
             "explicit formula's prime term samples at log(prime powers) (vertical lines). "
             "Whatever this object converges to IS the shape a positivity proof must "
             "control.")


# ---------------------------------------------------------------------------
# the gallery UI
# ---------------------------------------------------------------------------

def write_gallery():
    man_path = OUT / "manifest.json"
    man = json.loads(man_path.read_text()) if man_path.exists() else {}
    # migrate any old-format entries and merge this session's registrations
    man = {k: v for k, v in man.items() if isinstance(v, dict) and "ext" in v}
    for base, ext, title, cap in FIGDATA:
        man[base] = {"ext": ext, "title": title, "caption": cap}
    man_path.write_text(json.dumps(man, indent=1))

    items = []
    for base in sorted(man):
        ext = man[base]["ext"]
        if (OUT / f"{base}__dark.{ext}").exists() or (OUT / f"{base}__light.{ext}").exists():
            items.append({"base": base, "ext": ext, "title": man[base]["title"],
                          "caption": man[base]["caption"],
                          "anim": base.split("_")[1] == "anim" if "_" in base else False})
    items_json = json.dumps(items)

    html = """<!doctype html><html data-theme="dark"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Seeing the problem</title>
<style>
:root[data-theme="dark"]{--bg:#0e1117;--fg:#e8e6e3;--muted:#9aa4b2;--card:#131824;
 --line:#252c3a;--accent:#6ea8ff;--chip:#1b2333;}
:root[data-theme="light"]{--bg:#fbfaf7;--fg:#1c1c1c;--muted:#555;--card:#ffffff;
 --line:#e2ded6;--accent:#1f4e8c;--chip:#efece5;}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);
 font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;line-height:1.55}
.layout{display:flex;max-width:1400px;margin:0 auto}
nav{width:250px;flex:none;position:sticky;top:0;height:100vh;overflow-y:auto;
 padding:1.4rem 1rem;border-right:1px solid var(--line)}
nav h1{font-size:1.05rem;margin:0 0 .3rem}
nav p{font-size:.8rem;color:var(--muted);margin:.2rem 0 1rem}
nav a{display:block;color:var(--fg);text-decoration:none;font-size:.86rem;
 padding:.42rem .6rem;border-radius:8px;margin:.1rem 0}
nav a:hover{background:var(--chip)}
nav a.anim::after{content:" \\25B6";color:var(--accent);font-size:.7em}
main{flex:1;min-width:0;padding:1.6rem 2rem 5rem}
header.top{display:flex;justify-content:space-between;align-items:center;gap:1rem}
header.top p{color:var(--muted);max-width:60ch;font-size:.95rem}
#themeBtn{background:var(--chip);color:var(--fg);border:1px solid var(--line);
 border-radius:999px;padding:.5rem .95rem;font-size:.9rem;cursor:pointer;flex:none}
section.card{background:var(--card);border:1px solid var(--line);border-radius:14px;
 padding:1.1rem 1.3rem 1.3rem;margin:1.6rem 0;scroll-margin-top:1rem}
section.card h2{font-size:1.08rem;margin:.1rem 0 .8rem}
section.card h2 .n{color:var(--accent);margin-right:.5rem}
section.card img{width:100%;border-radius:8px;cursor:zoom-in;display:block;background:#fff0}
section.card p{font-size:.95rem;color:var(--muted);margin:.85rem 0 0}
.badge{font-size:.7rem;color:var(--accent);border:1px solid var(--accent);
 border-radius:999px;padding:.1rem .5rem;vertical-align:middle;margin-left:.5rem}
#lb{position:fixed;inset:0;background:rgba(0,0,0,.92);display:none;z-index:50;
 align-items:center;justify-content:center;flex-direction:column;gap:.7rem;padding:1rem}
#lb.open{display:flex}
#lb img{max-width:96vw;max-height:86vh;border-radius:8px}
#lb .cap{color:#ddd;font-size:.9rem;max-width:90ch;text-align:center}
#lb .hint{color:#888;font-size:.75rem}
@media (max-width:900px){.layout{display:block}nav{position:static;width:auto;height:auto;
 border-right:none;border-bottom:1px solid var(--line)}}
</style></head><body>
<div class="layout">
<nav><h1>Seeing the problem</h1>
<p>The Riemann Hypothesis through this repo's own objects. Click any figure to zoom;
arrow keys to move; T toggles theme.</p>
<div id="navlinks"></div></nav>
<main>
<header class="top">
<p>Batch 1 plus animations, generated locally by <code>make_figs.py</code> /
<code>make_anims.py</code>. Figures 2, 5, 6, 8 come from the built SP-object
(LEARNINGS #179/#180); the rest are the classical pictures those builds sit inside.</p>
<button id="themeBtn">theme: dark</button>
</header>
<div id="cards"></div>
</main></div>
<div id="lb"><img id="lbimg" src="" alt=""><div class="cap" id="lbcap"></div>
<div class="hint">arrows: previous / next, Esc: close</div></div>
<script>
const items = __ITEMS__;
let theme = localStorage.getItem("zf_theme") || "dark";
function src(it){ return it.base + "__" + theme + "." + it.ext; }
function build(){
  document.documentElement.dataset.theme = theme;
  document.getElementById("themeBtn").textContent = "theme: " + theme;
  document.getElementById("cards").innerHTML = items.map((it,i)=>
    `<section class="card" id="f${i}"><h2><span class="n">${i+1}</span>${it.title}` +
    (it.anim ? `<span class="badge">animated</span>` : ``) +
    `</h2><img loading="lazy" src="${src(it)}" alt="${it.title}" data-i="${i}">` +
    `<p>${it.caption}</p></section>`).join("");
  document.getElementById("navlinks").innerHTML = items.map((it,i)=>
    `<a href="#f${i}" class="${it.anim?"anim":""}">${i+1}. ${it.title}</a>`).join("");
  document.querySelectorAll("#cards img").forEach(im=>
    im.addEventListener("click", ()=>openLb(+im.dataset.i)));
}
function setTheme(t){ theme=t; localStorage.setItem("zf_theme",t); build(); }
document.getElementById("themeBtn").onclick =
  ()=>setTheme(theme==="dark"?"light":"dark");
let cur=-1;
const lb=document.getElementById("lb");
function openLb(i){ cur=i; lb.classList.add("open");
  document.getElementById("lbimg").src=src(items[i]);
  document.getElementById("lbcap").textContent=(i+1)+". "+items[i].title; }
function closeLb(){ lb.classList.remove("open"); cur=-1; }
lb.addEventListener("click",e=>{ if(e.target===lb) closeLb(); });
document.addEventListener("keydown",e=>{
  if(e.key==="t"||e.key==="T"){ setTheme(theme==="dark"?"light":"dark"); return; }
  if(cur<0) return;
  if(e.key==="Escape") closeLb();
  if(e.key==="ArrowRight"&&cur<items.length-1) openLb(cur+1);
  if(e.key==="ArrowLeft"&&cur>0) openLb(cur-1);
});
build();
</script></body></html>"""
    (OUT / "index.html").write_text(html.replace("__ITEMS__", items_json), encoding="utf-8")
    print(f"  wrote index.html ({len(items)} entries)")


FIGS = {1: fig1, 2: fig2, 3: fig3, 4: fig4, 5: fig5, 6: fig6, 7: fig7, 8: fig8,
        13: fig13, 15: fig15, 17: fig17, 18: fig18, 19: fig19, 20: fig20}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", type=int, default=0, help="build a single figure (1-8, 13)")
    ap.add_argument("--html", action="store_true", help="rebuild index.html only")
    args = ap.parse_args()
    t0 = time.time()
    if not args.html:
        todo = [args.only] if args.only else sorted(FIGS)
        for theme in ("dark", "light"):
            T = THEMES[theme]
            print(f"-- theme: {theme} --")
            for k in todo:
                FIGS[k](T)
    write_gallery()
    print(f"done in {time.time() - t0:.0f} s -> {OUT}/index.html")


if __name__ == "__main__":
    main()
