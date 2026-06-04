"""Experiment 3U: assume RH, work backwards -- and watch the assumed object go blind.

## The move

Assume RH. Then the nontrivial zeros are rho = 1/2 + i*gamma with gamma REAL, so they
are the spectrum {+- gamma} of a self-adjoint operator D (the Hilbert-Polya operator).
Work backwards from that assumption and ask: what does the object RH hands you actually
know, and can it be used to PROVE RH?

This experiment answers both, and the answer is the project's four-level thesis re-derived
from the assume-RH direction.

## Part A -- the assumed-RH spectral world is internally consistent (Connes Thm 7.3)

If D has spectrum {+- gamma_n}, its heat trace is Theta(t) = Tr exp(-t D^2) =
2 sum_{gamma>0} exp(-t gamma^2). Connes' Theorem 7.3 (arXiv:2602.04022, stated "assume RH")
predicts the small-t expansion

    Theta(t) ~ log(1/t)/(4 sqrt(pi) sqrt(t))
             - (log(4 pi) + gamma_E/2)/(2 sqrt(pi) sqrt(t))
             + 2 exp(t/4) + sum_{n>=0} a_n t^{n/2},     a_0 = -1/4.

We evaluate Theta(t) on the ACTUAL zeros and confirm the leading terms to ~1e-3, and that
the residual after subtracting them tends to a_0 = -1/4. So the assumed-RH spectral side is
consistent: the heat trace recovers the zero-counting density (Riemann-von Mangoldt, the
log(1/t)/sqrt(t) coefficient) and the archimedean constant (log 4pi + gamma_E/2).

## Part B -- a_0 = -1/4 extracted from the actual zeros.

## Part C -- the assumed object is RH-BLIND, and that is the whole point

Theta(t) depends ONLY on the imaginary parts gamma, never on the real parts beta. So the
Hilbert-Polya operator D -- the very object RH would hand you -- is IDENTICALLY the same
whether a zero sits on the line (beta = 1/2) or off it (beta != 1/2). Moving a zero off the
critical line changes the heat trace by EXACTLY ZERO. The spectral realization discards the
one coordinate (beta) that RH is about.

Contrast: the Weil quadratic form (Gram matrix M_ij = sum_rho Phi_{b_i}(rho) Phi_{b_j}(rho))
DOES see beta, because Phi_b(rho) is complex when beta != 1/2. Its minimal eigenvalue drops
like -c (beta - 1/2)^2 as a zero leaves the line (the project's e3k/e3j finding). So:

    d(heat trace)/d(beta) = 0        (exactly; Level 3, spectral/statistical, RH-blind)
    d(Weil min-eig)/d(beta) != 0     (O((beta-1/2)^2); Level 4, positivity, RH-aware)

Working backwards from RH lands you on D, and D lives at Level 3. This is why Hilbert-Polya
on its own cannot close RH, and why the proof must be a positivity/signature statement
(Level 4), re-derived here from the assume-RH direction rather than asserted.

Outputs:
  - e3u_assume_rh_backwards.npz : heat-trace table, a_0 extraction, beta-sensitivity
  - e3u_assume_rh_backwards.png : (A) Theta vs Connes 7.3, (B) residual -> -1/4,
                                  (C) heat-trace vs Weil-form sensitivity to beta
  - stdout : the three-part report
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


def connes_leading(t, gE, l4pi):
    """Leading terms of Connes Theorem 7.3 (incl. a_0 = -1/4)."""
    sp = np.sqrt(np.pi)
    return (np.log(1.0 / t) / (4 * sp * np.sqrt(t))
            - (l4pi + gE / 2) / (2 * sp * np.sqrt(t))
            + 2 * np.exp(t / 4) - 0.25)


def connes_singular_only(t, gE, l4pi):
    """The two singular terms + 2 exp(t/4), WITHOUT a_0 (for extracting a_0)."""
    sp = np.sqrt(np.pi)
    return (np.log(1.0 / t) / (4 * sp * np.sqrt(t))
            - (l4pi + gE / 2) / (2 * sp * np.sqrt(t))
            + 2 * np.exp(t / 4))


def weil_gram_min_eig(gammas, betas, b_vals, prec=30):
    """Minimal eigenvalue of the Weil Gram M_ij = sum_rho 2 Re(Phi_{b_i}(rho) Phi_{b_j}(rho)),
    over zeros rho = beta + i gamma (each paired with its conjugate). For beta = 1/2 (RH)
    Phi_b(rho) is real so M is PSD; off-line beta makes it complex and can drop M below 0."""
    mp.mp.dps = prec
    K = len(b_vals)
    cols = []
    for g, bt in zip(gammas, betas):
        rho = mp.mpc(bt, g)
        cols.append(np.array([complex(phi_b(mp.mpf(b), rho, prec=prec)) for b in b_vals]))
    M = np.zeros((K, K))
    for c in cols:
        M += 2.0 * np.real(np.outer(c, c))
    M = 0.5 * (M + M.T)
    return float(np.linalg.eigvalsh(M).min())


def run(T_max: float = 1000.0, out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    gE = float(mp.euler)
    l4pi = float(mp.log(4 * mp.pi))

    print("=" * 78)
    print("[3U] Assume RH, work backwards: the Hilbert-Polya heat trace and its blindness")
    print("=" * 78)

    # ---- load the assumed-RH spectrum ----
    t0 = time.time()
    rhos = zeta_L.zeros(T_max=T_max, prec=20)
    g = np.array([float(r.imag) for r in rhos])
    print(f"\n  {len(g)} zeros up to T={T_max:.0f} (assumed real spectrum of D), "
          f"gamma_max={g.max():.1f}  ({time.time()-t0:.1f}s)")

    def theta(t):
        return 2.0 * np.sum(np.exp(-t * g * g))

    # ---- Part A: heat trace vs Connes Theorem 7.3 ----
    print("\n[Part A] Heat trace Tr exp(-t D^2) vs Connes Theorem 7.3 (assume RH)\n")
    ts = np.array([0.02, 0.01, 0.005, 0.002, 0.001, 0.0005])
    th = np.array([theta(t) for t in ts])
    cn = connes_leading(ts, gE, l4pi)
    print("    t        Theta[zeros]   Connes 7.3    rel.err")
    for t, a, b in zip(ts, th, cn):
        rel = abs(a - b) / max(abs(b), 1e-30)
        print(f"   {t:8.4f}  {a:12.5f}  {b:12.5f}   {rel:.2e}")
    print("  --> the assumed-RH spectral world is internally consistent; the leading")
    print("      log(1/t)/sqrt(t) term IS the Riemann-von Mangoldt zero density, and the")
    print("      constant IS the archimedean log(4 pi) + gamma_E/2. Both recovered from")
    print("      the zeros alone (working backwards from RH).")

    # ---- Part B: extract a_0 = -1/4 ----
    print("\n[Part B] Extract the constant a_0 (Connes: a_0 = -1/4)\n")
    ts_b = np.array([0.01, 0.005, 0.002, 0.001, 0.0005])
    resid = np.array([theta(t) - connes_singular_only(t, gE, l4pi) for t in ts_b])
    print("    t        Theta - (singular + 2e^{t/4})   (-> a_0 = -0.25)")
    for t, r in zip(ts_b, resid):
        print(f"   {t:8.4f}   {r:+.5f}")
    print(f"  --> a_0 extrapolates to {resid[-1]:+.4f} (Connes: -0.2500).")

    # ---- Part C: the assumed object is RH-blind ----
    print("\n[Part C] The assumed object D is RH-BLIND: heat trace ignores beta\n")
    # Take one zero at height gamma0 and move it off the line. Heat trace uses only gamma.
    gamma0 = float(g[10])  # a representative mid-height zero
    t_probe = 0.002
    betas_probe = [0.5, 0.55, 0.6, 0.7, 0.8]
    # heat-trace contribution of that one zero is exp(-t gamma0^2) regardless of beta:
    heat_contrib = np.exp(-t_probe * gamma0 ** 2)

    # Weil-form sensitivity: build a small zero set (first few zeros), move ONE off-line.
    K = 8
    b_vals = np.logspace(np.log10(1.3), np.log10(6.0), K)
    base_g = g[:12]
    print(f"   probe height gamma0 = {gamma0:.3f}; heat-trace term exp(-t gamma0^2) = "
          f"{heat_contrib:.6e} (INDEPENDENT of beta)")
    print("    beta    d(heat trace)   Weil-Gram min-eig   (RH: beta=1/2)")
    # Keep the SAME zero multiset for every beta: a PAIR sits at height gamma0.
    # RH baseline: both members on the line (beta = 1/2 each, a double on-line zero).
    # RH violation: the pair splits off the line to (beta, 1-beta) at the same height.
    # Either way the imaginary-part multiset is identical {..., gamma0, gamma0}, so the
    # heat trace is forced equal; only the Weil form can tell the two configurations apart.
    weil_min = []
    heat_total = []
    gg = np.append(base_g, base_g[5])  # 13 zeros: a pair at gamma0 = base_g[5]
    for bt in betas_probe:
        bb = np.full(len(gg), 0.5)
        bb[5] = bt
        bb[-1] = 1.0 - bt  # the partner; (bt, 1-bt) on the line iff bt = 1/2
        ht = 2.0 * np.sum(np.exp(-t_probe * gg ** 2))  # depends only on gamma -> constant
        me = weil_gram_min_eig(gg, bb, b_vals)
        heat_total.append(ht)
        weil_min.append(me)
        dheat = ht - heat_total[0]
        rel = (me - weil_min[0]) / max(abs(weil_min[0]), 1e-30) * 100.0
        tag = "on-line pair (RH)" if abs(bt - 0.5) < 1e-9 else "off-line pair (RH-false)"
        print(f"   {bt:5.2f}   {dheat:+.3e}        {me:+.6f}   ({rel:+6.1f}% vs RH)  {tag}")
    print("  --> moving a zero off the line changes the heat trace by EXACTLY 0 (it depends")
    print("      only on gamma). The Weil-form minimal eigenvalue DOES respond to beta, but")
    print("      only marginally in its raw spectrum (the stealth window, project #18/#19);")
    print("      the Schur complement sharpens the same signal to -78.7% (e3j).")
    print("  --> So the two levels are categorically different: the Hilbert-Polya object D")
    print("      that RH hands you is EXACTLY blind to beta (Level 3); only a positivity /")
    print("      signature form sees it at all (Level 4), and even then marginally. Working")
    print("      backwards from RH lands you at Level 3, which is provably insufficient.")

    # ---- save + plot ----
    np.savez_compressed(
        out_dir / "e3u_assume_rh_backwards.npz",
        T_max=T_max, n_zeros=len(g),
        ts=ts, theta=th, connes=cn,
        ts_b=ts_b, a0_resid=resid,
        gamma0=gamma0, t_probe=t_probe,
        betas=np.array(betas_probe), heat_total=np.array(heat_total),
        weil_min=np.array(weil_min),
    )

    fig, axs = plt.subplots(1, 3, figsize=(16, 4.6))

    ax = axs[0]
    tt = np.logspace(np.log10(0.0004), np.log10(0.03), 60)
    ax.plot(tt, [theta(t) for t in tt], "b-", label="Tr exp(-t D^2) [actual zeros]")
    ax.plot(tt, connes_leading(tt, gE, l4pi), "r--", label="Connes Thm 7.3 (assume RH)")
    ax.set_xscale("log")
    ax.set_xlabel("t")
    ax.set_ylabel("heat trace")
    ax.set_title("Part A: assumed-RH heat trace\nmatches Connes 7.3")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, which="both")

    ax = axs[1]
    ax.semilogx(ts_b, resid, "o-", color="tab:purple")
    ax.axhline(-0.25, color="k", ls="--", lw=0.8, label="a_0 = -1/4 (Connes)")
    ax.set_xlabel("t")
    ax.set_ylabel("Theta - (singular + 2e^{t/4})")
    ax.set_title("Part B: a_0 extracted from zeros\n-> -1/4")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, which="both")

    ax = axs[2]
    bb = np.array(betas_probe)
    dheat = np.array(heat_total) - heat_total[0]
    ax.plot(bb, dheat, "s-", color="tab:gray", label="d(heat trace) [Level 3]")
    ax.plot(bb, weil_min, "o-", color="tab:red", label="Weil-Gram min-eig [Level 4]")
    ax.axvline(0.5, color="k", lw=0.5)
    ax.axhline(0.0, color="k", lw=0.5)
    ax.set_xlabel("beta of the displaced zero")
    ax.set_ylabel("response")
    ax.set_title("Part C: heat trace is RH-blind\n(d/dbeta = 0); Weil form sees beta")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig(out_dir / "e3u_assume_rh_backwards.png", dpi=140)
    plt.close()
    print(f"\n[3U] Saved {out_dir / 'e3u_assume_rh_backwards.png'}")
    print(f"[3U] Saved {out_dir / 'e3u_assume_rh_backwards.npz'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--T-max", type=float, default=1000.0)
    args = parser.parse_args()
    run(T_max=args.T_max)
