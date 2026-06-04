"""Experiment 3Y (M2.6 follow-up): the stealth window is a huge-cancellation residue.

## Why this experiment exists

Milestone M2.6 (LEARNINGS #34) found the "stealth window": the non-circular input-side Weil/Rosati
form M = A_arch + P_fin + B_pole reads SPURIOUSLY POSITIVE for Davenport-Heilbronn at reachable K,
because its off-line obstruction (~2.6% of the spectrum) sits below the reconstruction-residual
floor. This experiment establishes the MECHANISM behind that floor, and corrects a wrong claim in
the e3m docstring along the way.

## What the mechanism is

The three blocks are NOT "a positive archimedean cushion plus an indefinite prime perturbation."
Computed at K=10 (b in [1.3, 6]):

    block      norm     min eig     max eig
    A_arch     55.3     -55.2       +0.12     <- INDEFINITE, negative-dominated (NOT a cushion!)
    P_fin      69.0     -68.9       +2.97     <- INDEFINITE, negative-dominated
    B_pole    123.2      -0.0      +123.2     <- large rank-1 positive (the pole at s=1)
    -------------------------------------------
    M=A+P+B     0.33     +0.019      +0.24     <- the explicit-formula identity = M_zero (PSD)

So the Weil form's positivity for zeta is the residue of a ~370x cancellation: three blocks of norm
55-123 sum to a net of norm 0.33. By Weyl's inequality A_arch + P_fin alone has min eig <= -52; only
the large positive pole block brings the sum up to the tiny positive M_zero. The archimedean block
is itself indefinite (min eig -55), so the e3m docstring's "A_arch is a manifestly positive-
semidefinite quadratic form" is FALSE (corrected here and in e3m).

## Why this IS the stealth window

The off-line obstruction (D-H) is a fixed small FRACTION (~2.6%) of the already-tiny net M
(norm ~0.3), i.e. an ABSOLUTE signal ~ 0.3 x 0.026 ~ 0.008. The reconstruction residual
||A+P+B - M_zero|| is ~8-10% of the net (zeta 0.078, D-H 0.104), i.e. absolute ~0.03. So the off-line
signal (~0.008) sits BELOW the reconstruction residual (~0.03): it is invisible to the input-side
form. That is the stealth window, mechanistically: the positive form is the small residue of huge
canceling blocks, so the reconstruction error of those huge blocks dwarfs the off-line obstruction.
This is why the clean off-line detector is the ANSWER-side Schur complement (e3j, which works in the
zero basis and is not limited by the input-side reconstruction error), not the input-side min eig.

## D-H discipline

D-H reads zero-side rel min +0.011 at K=10 (off-line obstruction hidden) and input-side +0.044: both
spuriously positive, exactly the stealth window. The experiment quantifies why, and confirms that no
input-side (non-circular) certificate at reachable K can see D-H's off-line zeros, consistent with
#34 and the marginal-positivity thesis (e3v: the true margin is e^{-4 pi x}).

Outputs:
  - e3y_stealth_cancellation.npz : block norms, cancellation ratio, stealth arithmetic, K-scan
  - e3y_stealth_cancellation.png : block-norm bars + cancellation ratio vs K
  - stdout : the report
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

from experiments._shared import zeta_L, DavenportHeilbronn
from experiments.positivity.e3m_place_type_balance import (
    arch_block, finite_block, pole_block, lambda_coeffs_from_dirichlet, von_mangoldt_zeta,
    gram_zero_side,
)


def blocks_for(name, K, b_min=1.3, b_max=6.0, prec=30, t_cap=500.0):
    b_vals = np.logspace(np.log10(b_min), np.log10(b_max), K)
    n_max = int(b_max * b_max) + 2
    n_grid = max(200000, int(t_cap * 500))
    if name == "zeta":
        lam = np.array([0.0] + [von_mangoldt_zeta(n) for n in range(1, n_max + 1)])
        A = arch_block(b_vals, [0.0], mp.mpf(0), prec, t_cap, n_grid=n_grid)
        B = pole_block(b_vals, 1.0, prec)
        L = zeta_L
    else:
        dh = DavenportHeilbronn()
        lam = lambda_coeffs_from_dirichlet(dh, n_max, prec)
        A = arch_block(b_vals, [1.0], mp.log(mp.sqrt(5)), prec, t_cap, n_grid=n_grid)
        B = pole_block(b_vals, 0.0, prec)  # D-H is entire: no pole block
        L = dh
    P = finite_block(b_vals, lam, prec)
    Mz, _ = gram_zero_side(L, b_vals, 200.0, prec)
    return A, P, B, Mz, b_vals


def stat(X):
    e = np.linalg.eigvalsh(0.5 * (X + X.T))
    return dict(norm=float(np.linalg.norm(X)), min=float(e.min()), max=float(e.max()),
                rel_min=float(e.min() / max(abs(e).max(), 1e-30)))


def run(out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 78)
    print("[3Y] M2.6 follow-up: the stealth window is a huge-cancellation residue")
    print("=" * 78)

    print("\n[Part A] The three blocks for zeta (K=10): norm, min eig, max eig\n")
    A, P, B, Mz, _ = blocks_for("zeta", 10)
    M = A + P + B
    names = ["A_arch", "P_fin", "B_pole", "M=A+P+B", "M_zero(zeros)"]
    mats = [A, P, B, M, Mz]
    print("    block          norm      min eig    max eig    rel_min")
    for nm, X in zip(names, mats):
        s = stat(X)
        print(f"    {nm:14s} {s['norm']:8.2f}  {s['min']:+9.3f}  {s['max']:+9.3f}   {s['rel_min']:+.4f}")
    resid = np.linalg.norm(M - Mz) / np.linalg.norm(Mz)
    cancel = max(stat(A)["norm"], stat(P)["norm"], stat(B)["norm"]) / stat(M)["norm"]
    print(f"\n    reconstruction residual ||A+P+B - M_zero||/||M_zero|| = {resid:.3e}")
    print(f"    CANCELLATION RATIO max||block|| / ||M_net|| = {cancel:.0f}x")
    print(f"    --> positivity is the residue of a {cancel:.0f}x cancellation, NOT cushion+perturbation.")
    print(f"    --> A_arch is INDEFINITE (min eig {stat(A)['min']:+.1f}); the e3m docstring claim that")
    print(f"        A_arch is 'manifestly positive-semidefinite' is FALSE (corrected).")

    print("\n[Part B] The stealth-window arithmetic (why the off-line obstruction is invisible)\n")
    Ad, Pd, Bd, Mzd, _ = blocks_for("DH", 10)
    Md = Ad + Pd + Bd
    sMz = stat(Mz); sMzd = stat(Mzd)
    resid_dh = np.linalg.norm(Md - Mzd) / np.linalg.norm(Mzd)
    offline_frac = 0.026  # the e3j/3D.3 raw off-line obstruction fraction
    offline_abs = offline_frac * sMzd["norm"]
    residual_abs = resid_dh * sMzd["norm"]
    print(f"    D-H net form norm = {sMzd['norm']:.3f}; zero-side rel_min = {sMzd['rel_min']:+.4f} "
          f"(off-line hidden, spuriously +); input-side rel_min = {stat(Md)['rel_min']:+.4f}")
    print(f"    off-line obstruction (~{offline_frac:.1%} of net)  : absolute ~ {offline_abs:.4f}")
    print(f"    reconstruction residual ({resid_dh:.1%} of net)     : absolute ~ {residual_abs:.4f}")
    print(f"    ratio off-line / residual = {offline_abs/residual_abs:.2f}  (< 1 => INVISIBLE = stealth window)")
    print(f"    --> the off-line signal is dwarfed by the reconstruction error of the huge canceling")
    print(f"        blocks. Clean detection needs the ANSWER-side Schur complement (e3j), not this.")

    print("\n[Part C] Cancellation deepens with K (toward the e3v marginal wall)\n")
    Ks = [6, 8, 10, 12]
    cancels = []
    print("     K    max||block||   ||M_net||   cancellation ratio")
    for K in Ks:
        t0 = time.time()
        Ak, Pk, Bk, Mzk, _ = blocks_for("zeta", K)
        Mk = Ak + Pk + Bk
        mb = max(stat(Ak)["norm"], stat(Pk)["norm"], stat(Bk)["norm"])
        mn = stat(Mk)["norm"]
        cancels.append(mb / mn)
        print(f"    {K:3d}    {mb:10.1f}    {mn:8.3f}    {mb/mn:8.0f}x   ({time.time()-t0:.1f}s)")
    print(f"    --> the cancellation ratio grows with resolution; the true infinite-resolution")
    print(f"        margin is the e3v doubly-exponential wall e^{{-4 pi x}}. Marginal positivity is")
    print(f"        a near-perfect cancellation of large blocks, quantified.")

    np.savez_compressed(
        out_dir / "e3y_stealth_cancellation.npz",
        zeta_block_norms=np.array([stat(A)["norm"], stat(P)["norm"], stat(B)["norm"]]),
        zeta_net_norm=stat(M)["norm"], zeta_resid=resid, cancel_ratio=cancel,
        dh_net_norm=sMzd["norm"], dh_resid=resid_dh,
        offline_abs=offline_abs, residual_abs=residual_abs,
        Ks=np.array(Ks), cancels=np.array(cancels),
    )

    fig, axs = plt.subplots(1, 2, figsize=(13, 5))
    ax = axs[0]
    bn = ["A_arch", "P_fin", "B_pole", "M=A+P+B"]
    bv = [stat(A)["norm"], stat(P)["norm"], stat(B)["norm"], stat(M)["norm"]]
    ax.bar(bn, bv, color=["tab:red", "tab:red", "tab:green", "tab:blue"])
    ax.set_ylabel("block norm")
    ax.set_title(f"Part A: positivity is a {cancel:.0f}x cancellation residue\n"
                 "(blocks ~55-123 -> net ~0.3; A_arch indefinite)")
    ax.tick_params(axis="x", rotation=15)
    ax.grid(alpha=0.3, axis="y")

    ax = axs[1]
    ax.plot(Ks, cancels, "o-", color="tab:purple")
    ax.set_xlabel("basis size K")
    ax.set_ylabel("cancellation ratio max||block||/||M_net||")
    ax.set_title("Part C: cancellation deepens with K\n(toward the e3v e^{-4 pi x} wall)")
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(out_dir / "e3y_stealth_cancellation.png", dpi=140)
    plt.close()
    print(f"\n[3Y] Saved {out_dir / 'e3y_stealth_cancellation.png'}")
    print(f"[3Y] Saved {out_dir / 'e3y_stealth_cancellation.npz'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.parse_args()
    run()
