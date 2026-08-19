"""Animated companions to the research-figure gallery (local GIFs, both themes).

  9. the explicit formula building the prime staircase, one zero pair at a time
 10. dragging one zero off the line: watch the prime-counting error grow
 11. the circle carrier resolving the spectrum as its circumference grows
 12. the window narrowing into the central hole: the margin thinning live

Run from the repo root (after make_figs.py at least once):
  python visualizations/research/make_anims.py
  python visualizations/research/make_anims.py --only 10

GIFs land in _out/ next to the static figures and join the same gallery.
"""

from __future__ import annotations

import argparse
import sys
import time
from math import pi
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import make_figs as MF  # noqa: E402
from make_figs import OUT, THEMES, register, write_gallery, zeta_gammas  # noqa: E402
from experiments.arithmetic_geometric.e2an_sp_object_v0 import (  # noqa: E402
    lambda_sieve, multiplier,
)

FPS = 10


def save_anim(anim, base, T, title, caption, fps=FPS):
    path = OUT / f"{base}__{T['name']}.gif"
    anim.save(path, writer=PillowWriter(fps=fps))
    plt.close(anim._fig)
    register(base, "gif", title, caption)
    print(f"  saved {path.name}")


# ---------------------------------------------------------------------------
# 9. the explicit formula, built one zero pair at a time
# ---------------------------------------------------------------------------

def anim9(T):
    print("anim 9: the staircase assembling")
    gam = zeta_gammas(200.0)
    lam = lambda_sieve(120)
    psi_true = np.concatenate([[0.0], np.cumsum(lam[1:])])
    x = np.linspace(2.0, 100.0, 1500)
    base_curve = x - np.log(2 * pi) - 0.5 * np.log(1 - x ** (-2.0))
    waves = np.array([-2 * np.real(x ** (0.5 + 1j * g) / (0.5 + 1j * g)) for g in gam])
    partial = np.concatenate([[np.zeros_like(x)], np.cumsum(waves, axis=0)])

    with plt.style.context(T["style"]):
        fig, ax = plt.subplots(figsize=(10.5, 6))
        ax.step(np.arange(len(psi_true)), psi_true, where="post", color=T["grey"], lw=1.3)
        (ln,) = ax.plot([], [], color=T["red"], lw=1.3)
        txt = ax.text(0.03, 0.94, "", transform=ax.transAxes, fontsize=13, color=T["fg"])
        ax.set_xlim(2, 100)
        ax.set_ylim(0, 105)
        ax.set_xlabel("x")
        ax.set_ylabel("psi(x)")
        ax.set_title("zeros are added one pair at a time; the staircase assembles")

        frames = list(range(len(gam) + 1)) + [len(gam)] * 14

        def update(K):
            ln.set_data(x, base_curve + partial[K])
            txt.set_text(f"{K} zero pair{'s' if K != 1 else ''}")
            return ln, txt

        anim = FuncAnimation(fig, update, frames=frames, blit=True)
        save_anim(anim, "09_anim_explicit", T, "Watch the zeros build the primes",
                  "The same picture as figure 3, in motion: start from the smooth curve "
                  "(zero zeros) and add one cosine wave per zero pair, in height order. Every "
                  "wave has the same shape; only its frequency (the zero's height) and phase "
                  "differ. Ninety-one pairs later the waves have conspired into the prime "
                  "staircase, corner by corner. Nothing about the primes was fed in: the "
                  "staircase is stored in the zeros.")


# ---------------------------------------------------------------------------
# 10. dragging one zero off the line
# ---------------------------------------------------------------------------

def anim10(T):
    print("anim 10: one zero dragged off the line")
    gam = zeta_gammas(200.0)
    x = np.geomspace(1e2, 1e10, 900)
    lx = np.log(x)
    sqx = np.sqrt(x)
    # fixed on-line contribution of every zero except the first
    rest = np.zeros_like(x)
    for g in gam[1:]:
        rho = 0.5 + 1j * g
        rest += -2 * np.real(x ** rho / rho)
    g1 = gam[0]

    def first_pair(beta):
        # the FE forces the reflected partner at 1 - beta
        out = np.zeros_like(x)
        for b in (beta, 1 - beta) if abs(beta - 0.5) > 1e-12 else (0.5,):
            rho = b + 1j * g1
            out += -2 * np.real(np.exp(rho * lx) / rho)
        return out

    betas = np.concatenate([np.full(8, 0.5), np.linspace(0.5, 0.9, 55),
                            np.full(14, 0.9)])

    with plt.style.context(T["style"]):
        fig, (axl, axr) = plt.subplots(1, 2, figsize=(11.5, 5.6), width_ratios=[1, 2.4])
        axl.axvline(0.5, color=T["muted"], ls="--", lw=1)
        axl.plot([0.5] * 8, gam[1:9], "o", ms=5, color=T["blue"])
        (mv,) = axl.plot([0.5], [g1], "o", ms=9, color=T["red"])
        axl.set_xlim(0, 1)
        axl.set_ylim(0, 50)
        axl.set_xlabel("Re(s)")
        axl.set_ylabel("Im(s)")
        axl.set_title("one zero, dragged")
        (err,) = axr.plot([], [], lw=0.9, color=T["blue"])
        env_p, = axr.plot([], [], "--", lw=1.2, color=T["red"])
        env_m, = axr.plot([], [], "--", lw=1.2, color=T["red"])
        txt = axr.text(0.03, 0.92, "", transform=axr.transAxes, fontsize=12, color=T["fg"])
        axr.set_xscale("log")
        axr.set_xlim(1e2, 1e10)
        axr.set_ylim(-25, 25)
        axr.set_xlabel("x")
        axr.set_ylabel("(psi(x) - x) / sqrt(x)")
        axr.set_title("the prime-counting error, in square-root units")

        def update(i):
            b = betas[i]
            mv.set_data([b], [g1])
            y = (rest + first_pair(b)) / sqx
            err.set_data(x, y)
            env = 2 * np.exp((b - 0.5) * lx) / abs(b + 1j * g1) + 2 / abs(b + 1j * g1)
            env_p.set_data(x, env)
            env_m.set_data(x, -env)
            txt.set_text(f"Re(zero) = {b:.3f}")
            return mv, err, env_p, env_m, txt

        anim = FuncAnimation(fig, update, frames=len(betas), blit=True)
        save_anim(anim, "10_anim_offline", T, "What one off-line zero does",
                  "Drag the first zero from Re = 1/2 to Re = 0.9 (its reflected partner, "
                  "forced by the functional equation, moves to 0.1). On the line, the error "
                  "(psi(x) - x)/sqrt(x) is a bounded chorus of waves forever. Off the line, "
                  "one voice grows like x^(Re - 1/2) (dashed envelope) and eventually drowns "
                  "the choir: the prime-counting error is permanently worse at all large x. "
                  "RH is the statement that every voice stays bounded. Note how slowly the "
                  "envelope separates: a slightly off-line zero is invisible until enormous x, "
                  "which is why no computation can settle this from the primes.")


# ---------------------------------------------------------------------------
# 11. the carrier resolving as L grows
# ---------------------------------------------------------------------------

def anim11(T):
    print("anim 11: the carrier resolving")
    lat_z, lat_d, probe, integ_z, integ_d = MF.engine()
    if "anim11" not in MF._CACHE:
        tau_f, m_z = multiplier(lat_z, probe, integrand=integ_z)
        _, m_d = multiplier(lat_d, probe, integrand=integ_d)
        MF._CACHE["anim11"] = (tau_f, np.abs(m_z), np.abs(m_d))
    tau_f, am_z, am_d = MF._CACHE["anim11"]
    gz = zeta_gammas(100.0)
    Ls = np.concatenate([np.full(6, 6.0), np.linspace(6.0, 20.0, 57), np.full(12, 20.0)])

    with plt.style.context(T["style"]):
        fig, (axl, axr) = plt.subplots(1, 2, figsize=(11.5, 5.6), width_ratios=[2.2, 1])
        for g in gz:
            axl.axvline(g, color=T["zline"], lw=0.8, zorder=0)
        (lnz,) = axl.semilogy([], [], "o-", ms=3.5, lw=0.6, color=T["blue"])
        txt = axl.text(0.02, 0.05, "", transform=axl.transAxes, fontsize=13, color=T["fg"])
        axl.set_xlim(5, 100)
        axl.set_ylim(1e-3, 30)
        axl.set_xlabel("tau")
        axl.set_ylabel("|m| at the carrier's grid points")
        axl.set_title("zeta: vertical lines are the true zeros")
        (lnd,) = axr.semilogy([], [], "o-", ms=3.5, lw=0.6, color=T["grey"])
        axr.axvspan(85.2, 86.2, color=T["red"], alpha=0.2)
        axr.plot([85.699], [0.35], "*", color=T["red"], ms=16)
        axr.set_xlim(80, 92)
        axr.set_ylim(1e-3, 30)
        axr.set_xlabel("tau")
        axr.set_title("D-H: the off-line pair (star)")

        def update(i):
            L = Ls[i]
            ks = np.arange(1, int(100 * L / (2 * pi)) + 1)
            tk = 2 * pi * ks / L
            lnz.set_data(tk, np.interp(tk, tau_f, am_z))
            lnd.set_data(tk, np.interp(tk, tau_f, am_d))
            txt.set_text(f"circumference L = {L:.1f}   grid step {2 * pi / L:.2f}")
            return lnz, lnd, txt

        anim = FuncAnimation(fig, update, frames=len(Ls), blit=True)
        save_anim(anim, "11_anim_carrier", T, "The carrier resolving the spectrum",
                  "The object's carrier is a circle; its Fourier grid samples the critical "
                  "line at spacing 2 pi / L. As the circumference grows, grid points fall "
                  "into the zeros' dips one after another: the spectrum RESOLVES. Watch the "
                  "right panel throughout: D-H's off-line pair (star) never produces a dip "
                  "in the shaded band, at any circumference. The carrier can only see what "
                  "lives on the line; completeness of what it sees is exactly RH.")


# ---------------------------------------------------------------------------
# 12. the window narrowing into the hole
# ---------------------------------------------------------------------------

def anim12(T):
    print("anim 12: the margin thinning")
    g1 = 14.134725
    gz = zeta_gammas(60.0)
    t = np.linspace(-45, 45, 1200)
    sig_path = np.concatenate([np.full(6, 0.15), np.linspace(0.15, 0.72, 55),
                               np.full(12, 0.72)])
    ss = np.linspace(0.12, 0.78, 300)
    law = 4 * np.sqrt(pi) * ss * np.exp(-g1 ** 2 * ss ** 2)

    with plt.style.context(T["style"]):
        fig, (axl, axr) = plt.subplots(1, 2, figsize=(11.5, 5.4), width_ratios=[1.9, 1])
        for g in np.concatenate([gz, -gz]):
            if abs(g) <= 45:
                axl.axvline(g, color=T["zline"], lw=1.2)
        axl.axvspan(-g1, g1, color=T["goldfill"], alpha=0.18)
        (bump,) = axl.plot([], [], color=T["blue"], lw=1.5)
        fill = [axl.fill_between(t, np.zeros_like(t), color=T["blue"], alpha=0.3)]
        txt = axl.text(0.02, 0.9, "", transform=axl.transAxes, fontsize=12, color=T["fg"])
        axl.set_xlim(-45, 45)
        axl.set_ylim(0, 1.1)
        axl.set_yticks([])
        axl.set_xlabel("tau  (vertical lines = zeros)")
        axl.set_title("the window mode hiding in the central hole")
        axr.semilogy(ss, law, color=T["red"], lw=1.4)
        axr.axhline(1e-5, color=T["grey"], ls="--", lw=1.2)
        axr.text(0.14, 2e-5, "prime-side certification floor", fontsize=8.5, color=T["muted"])
        (dot,) = axr.semilogy([], [], "o", ms=10, color=T["blue"])
        state = axr.text(0.05, 0.05, "", transform=axr.transAxes, fontsize=12)
        axr.set_xlim(0.12, 0.78)
        axr.set_ylim(1e-45, 1)
        axr.set_xlabel("window scale sigma")
        axr.set_ylabel("positivity margin")
        axr.set_title("margin = 4 sqrt(pi) sigma exp(-gamma_1^2 sigma^2)")

        def update(i):
            s = sig_path[i]
            y = np.exp(-s ** 2 * t ** 2 / 2)
            bump.set_data(t, y)
            fill[0].remove()
            fill[0] = axl.fill_between(t, y, color=T["blue"], alpha=0.3)
            txt.set_text(f"sigma = {s:.2f}")
            mval = 4 * np.sqrt(pi) * s * np.exp(-g1 ** 2 * s ** 2)
            dot.set_data([s], [mval])
            ok = mval > 1e-5
            state.set_text("certifiable" if ok else "positive, but\nuncertifiable")
            state.set_color(T["green"] if ok else T["red"])
            return bump, fill[0], txt, dot, state

        anim = FuncAnimation(fig, update, frames=len(sig_path), blit=False)
        save_anim(anim, "12_anim_margin", T, "The margin thinning as the window grows",
                  "Left: the worst window mode narrows its spectral footprint into the "
                  "central hole as sigma grows, paying only its Gaussian leakage onto the "
                  "first zero. Right: its positivity margin sliding down the exact law "
                  "4 sqrt(pi) sigma exp(-gamma_1^2 sigma^2). The dashed line is the best "
                  "precision the prime-side assembly achieves: past the crossing the margin "
                  "is real but no longer certifiable from prime data. RH needs the margin "
                  "positive at EVERY sigma; M4 is the structure that would certify it "
                  "uniformly, and this is what its absence looks like.")


ANIMS = {9: anim9, 10: anim10, 11: anim11, 12: anim12}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", type=int, default=0, help="build a single animation (9-12)")
    args = ap.parse_args()
    t0 = time.time()
    todo = [args.only] if args.only else sorted(ANIMS)
    for theme in ("dark", "light"):
        T = THEMES[theme]
        print(f"-- theme: {theme} --")
        for k in todo:
            ANIMS[k](T)
    write_gallery()
    print(f"done in {time.time() - t0:.0f} s -> {OUT}/index.html")


if __name__ == "__main__":
    main()
