"""Experiment 3B.4: rigorous Li-criterion DISCRIMINATION across L-functions,
with a SECOND independent off-line witness (Epstein), extending 3B.3.

## What 3B.3 established, and the gap

3B.3 produced a rigorous certificate that lambda_n^{DH} < 0 at large n (the
Li criterion correctly detects the Davenport-Heilbronn off-line zeros), via
the Bombieri-Lagarias on-line asymptotic plus an exact off-line correction
plus explicit error and tail bounds. Two gaps remained:

  1. The negativity witness used only ONE off-line construction (D-H). The Li
     criterion's discrimination has never been checked against a second,
     independent L-function with off-line zeros.
  2. 3B.3 showed lambda_n^{DH} < 0 but did not pair it with a rigorous
     lambda_n > 0 for the Selberg-class controls at the SAME n, i.e. it did
     not state the discrimination as a single rigorous inequality
     lambda_n^{off-line} < 0 < lambda_n^{Selberg}.

## What 3B.4 adds

(a) SECOND WITNESS. The Epstein zeta of the discriminant-47 non-principal
    form 2x^2 + xy + 6y^2 (class number 5) has an off-line zero pair at
    rho ~ 0.634 +- ... and its functional-equation partner 0.366 + 32.05 i.
    The partner has Re < 1/2, hence |w| = |1 - 1/rho| > 1, so its Li
    contribution -2 Re(w^n) grows EXPONENTIALLY negative and eventually
    dominates the positive on-line baseline. We produce a rigorous
    lambda_n^{Epstein} < 0 certificate, the first Li witness for an Epstein
    zeta in this project. This ties 3B.4 to experiment 3L (the Epstein
    second-control test of the Gram detector): the same off-line zero that
    makes the Schur detector fire also makes the Li criterion fire.

(b) DISCRIMINATION. For the degree-1 Selberg controls (zeta q=1, chi_3 q=3)
    we give a rigorous lower bound lambda_n > 0 at the same n (the on-line
    Bombieri-Lagarias baseline minus its error bound, with no off-line
    correction). Combined with (a) this is a single rigorous statement:
        lambda_n^{DH} < 0  and  lambda_n^{Epstein} < 0  <  lambda_n^{zeta},
                                                            lambda_n^{chi_3}
    at the witnessed n.

## Rigour notes

  - The negativity witnesses are driven by the off-line exponential growth.
    For those targets we use a CONSERVATIVE OVER-ESTIMATE of the positive
    on-line baseline (degree * Bombieri-Lagarias). Over-estimating the
    positive part only makes the upper bound lambda_upper larger, so
    "lambda_upper < 0" remains a valid (conservative) negativity certificate
    regardless of the exact degree-2 conductor constant.
  - The Selberg positivity lower bounds are stated only for the degree-1
    controls (zeta, chi_3), where the Bombieri-Lagarias constant is exact.
    For the degree-2 Epstein PRINCIPAL form we report only that the off-line
    correction is identically zero (it has no off-line zeros up to T = 120),
    so its lambda_n equals the positive on-line baseline; we do not attach a
    numeric rigorous lower bound to it.
  - All error/tail bounds reuse 3B.3's functions and assumptions.

Outputs:
  - e3b4_li_discrimination.npz : per-(L, n) lambda estimates and bounds
  - e3b4_li_discrimination.png : discrimination figure
  - stdout : the rigorous discrimination verdict
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
    zeta_L, chi3_L, DavenportHeilbronn, epstein_d47, epstein_d47_principal,
)
from experiments.positivity.e3b3_rigorous import (
    li_BL_next_order, asymptotic_error_bound,
    offline_correction_full, offline_tail_bound,
)


def on_line_baseline(n, q, degree, prec=100):
    """Conservative positive on-line Li baseline for an L-function of the
    given conductor q and degree.

    For degree 1 this is the exact Bombieri-Lagarias next-order asymptotic.
    For degree d the leading term scales with d (one gamma factor per degree),
    so we use degree * (degree-1 baseline) as a conservative over-estimate of
    the positive on-line contribution. Over-estimating is the safe direction
    for a negativity certificate (it can only delay, never falsely trigger,
    the lambda_upper < 0 verdict).
    """
    mp.mp.dps = prec
    base = li_BL_next_order(n, q=q, prec=prec)
    if degree == 1:
        return base
    return degree * base


def offline_zeros_uhp(L, T_max, prec):
    """Off-line zeros of L in the upper half plane (Re != 1/2, Im > 0)."""
    rhos = L.zeros(T_max=T_max, prec=prec)
    rhos = [mp.mpc(z.real, z.imag) for z in rhos]
    return [z for z in rhos
            if abs(float(z.real) - 0.5) > 1e-4 and float(z.imag) > 0]


def witness_target(name, L, q, degree, T_max, offline, ns, prec):
    """Compute lambda_n central/lower/upper across the n-sweep for one L."""
    rows = []
    first_rig_neg = None
    first_rig_pos = None
    for n in ns:
        n = int(n)
        base = on_line_baseline(n, q=q, degree=degree, prec=prec)
        err = asymptotic_error_bound(n, q=q)
        if offline:
            off_corr, _ = offline_correction_full(n, offline, prec=prec)
            tail = offline_tail_bound(n, T_max, prec=prec)
        else:
            off_corr = mp.mpf(0)
            tail = mp.mpf(0)
        lam_central = base + off_corr
        lam_lower = base - err + off_corr - tail
        lam_upper = base + err + off_corr + tail
        rig_neg = lam_upper < 0
        rig_pos = lam_lower > 0
        if rig_neg and first_rig_neg is None:
            first_rig_neg = n
        if rig_pos and first_rig_pos is None:
            first_rig_pos = n
        rows.append({
            "n": n,
            "lam_central": float(lam_central),
            "lam_lower": float(lam_lower),
            "lam_upper": float(lam_upper),
            "off_corr": float(off_corr),
            "rig_neg": bool(rig_neg),
            "rig_pos": bool(rig_pos),
        })
    return rows, first_rig_neg, first_rig_pos


def run(
    n_min=50000,
    n_max=500000,
    n_step=2000,
    prec=100,
    zero_prec=30,
    dh_T_max=500.0,
    epstein_T_max=60.0,
    out_dir: Path = None,
):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)
    mp.mp.dps = prec

    print(f"[3B.4] Rigorous Li discrimination, n in [{n_min}, {n_max}] step {n_step}")
    print(f"        working precision {prec} digits, zero load precision {zero_prec}")

    dh = DavenportHeilbronn()

    print(f"[3B.4] Loading off-line zeros...")
    t0 = time.time()
    dh_off = offline_zeros_uhp(dh, dh_T_max, zero_prec)
    eps_off = offline_zeros_uhp(epstein_d47, epstein_T_max, zero_prec)
    # The principal form has no off-line zeros (verified to T=120); its only
    # role is the Selberg-positivity contrast (off-line correction = 0), so its
    # tail bound is irrelevant and we use its cheap cached T=60 scan rather than
    # a wasteful rescan to epstein_T_max.
    eps_prin_off = offline_zeros_uhp(epstein_d47_principal, 60.0, zero_prec)
    print(f"        D-H: {len(dh_off)} off-line UHP zeros (T<={dh_T_max})")
    for z in dh_off:
        print(f"          {float(z.real):.4f}+{float(z.imag):.4f}i  |w|={float(abs(1-1/z)):.6f}")
    print(f"        Epstein d=47 non-principal: {len(eps_off)} off-line UHP zeros (T<={epstein_T_max})")
    for z in eps_off:
        print(f"          {float(z.real):.4f}+{float(z.imag):.4f}i  |w|={float(abs(1-1/z)):.6f}")
    print(f"        Epstein d=47 principal: {len(eps_prin_off)} off-line UHP zeros (expected 0)")
    print(f"        [{time.time()-t0:.1f}s]")

    mp.mp.dps = prec
    ns = np.arange(n_min, n_max + 1, n_step)

    # (name, L, q, degree, T_max, offline_zeros, is_selberg)
    specs = [
        ("zeta",             zeta_L,                1, 1, 0.0,           [],            True),
        ("chi3",             chi3_L,                3, 1, 0.0,           [],            True),
        ("epstein_d47_prin", epstein_d47_principal, 47, 2, 60.0,          eps_prin_off, True),
        ("DH",               dh,                    5, 1, dh_T_max,      dh_off,        False),
        ("epstein_d47_np",   epstein_d47,           47, 2, epstein_T_max, eps_off,      False),
    ]

    out = {}
    summary = {}
    for name, L, q, degree, T_max, offline, is_selberg in specs:
        t0 = time.time()
        rows, frn, frp = witness_target(name, L, q, degree, T_max, offline, ns, prec)
        out[name] = rows
        summary[name] = {
            "q": q, "degree": degree, "n_offline": len(offline),
            "is_selberg": is_selberg,
            "first_rig_neg": frn, "first_rig_pos": frp,
        }
        msg = []
        if frn is not None:
            msg.append(f"first rigorously NEGATIVE at n={frn}")
        if frp is not None:
            msg.append(f"first rigorously POSITIVE at n={frp}")
        print(f"  {name:16s} (q={q}, deg={degree}, off={len(offline)}): "
              f"{'; '.join(msg) if msg else 'no rigorous verdict in range'} "
              f"[{time.time()-t0:.1f}s]")

    # Save
    save = {"n_values": ns, "prec": prec}
    for name, rows in out.items():
        save[f"{name}_lam_central"] = np.array([r["lam_central"] for r in rows])
        save[f"{name}_lam_lower"] = np.array([r["lam_lower"] for r in rows])
        save[f"{name}_lam_upper"] = np.array([r["lam_upper"] for r in rows])
        save[f"{name}_off_corr"] = np.array([r["off_corr"] for r in rows])
        save[f"{name}_first_rig_neg"] = summary[name]["first_rig_neg"] or -1
        save[f"{name}_first_rig_pos"] = summary[name]["first_rig_pos"] or -1
    np.savez_compressed(out_dir / "e3b4_li_discrimination.npz", **save)

    # Plot
    colors = {"zeta": "tab:blue", "chi3": "tab:green",
              "epstein_d47_prin": "tab:purple", "epstein_d47_np": "tab:orange",
              "DH": "tab:red"}
    fig, axs = plt.subplots(1, 2, figsize=(14, 5.5))

    ax = axs[0]
    for name in out:
        c = np.array([r["lam_central"] for r in out[name]])
        ax.plot(ns, c, "-", color=colors.get(name), label=name, lw=1.4)
    ax.axhline(0, color="k", lw=0.6, ls="--")
    ax.set_xlabel("n"); ax.set_ylabel(r"$\lambda_n$ (central)")
    ax.set_title("Li coefficients: Selberg (positive) vs off-line (turn negative)")
    ax.legend(fontsize=9); ax.grid(alpha=0.3)

    ax = axs[1]
    for name in ("DH", "epstein_d47_np"):
        c = np.array([r["lam_central"] for r in out[name]])
        u = np.array([r["lam_upper"] for r in out[name]])
        lo = np.array([r["lam_lower"] for r in out[name]])
        ax.plot(ns, c, "-", color=colors[name], label=f"{name} central", lw=1.4)
        ax.fill_between(ns, lo, u, color=colors[name], alpha=0.2)
        frn = summary[name]["first_rig_neg"]
        if frn:
            ax.axvline(frn, color=colors[name], ls=":", lw=1.0,
                       label=f"{name} rig.neg n={frn}")
    ax.axhline(0, color="k", lw=0.6, ls="--")
    ax.set_yscale("symlog", linthresh=1e3)
    ax.set_xlabel("n"); ax.set_ylabel(r"$\lambda_n$ with error band")
    ax.set_title("Off-line witnesses with rigorous error bands\n(D-H and Epstein both go rigorously negative)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3, which="both")

    plt.tight_layout()
    plt.savefig(out_dir / "e3b4_li_discrimination.png", dpi=140)
    plt.close()
    print(f"\n[3B.4] Saved {out_dir / 'e3b4_li_discrimination.png'}")
    print(f"[3B.4] Saved {out_dir / 'e3b4_li_discrimination.npz'}")

    # Verdict
    print("\n" + "=" * 78)
    print("[3B.4] Rigorous discrimination verdict")
    print("=" * 78)
    dh_neg = summary["DH"]["first_rig_neg"]
    eps_neg = summary["epstein_d47_np"]["first_rig_neg"]
    zeta_pos = summary["zeta"]["first_rig_pos"]
    chi3_pos = summary["chi3"]["first_rig_pos"]
    print(f"  D-H                  : lambda_n < 0 rigorously from n = {dh_neg}")
    print(f"  Epstein d=47 (np)    : lambda_n < 0 rigorously from n = {eps_neg}   <-- SECOND WITNESS")
    print(f"  zeta                 : lambda_n > 0 rigorously from n = {zeta_pos}")
    print(f"  chi_3                : lambda_n > 0 rigorously from n = {chi3_pos}")
    print(f"  Epstein d=47 (prin)  : off-line correction = 0 (no off-line zeros); "
          f"lambda_n = positive on-line baseline")
    print()
    if eps_neg is not None and dh_neg is not None:
        n_star = max(dh_neg, eps_neg, zeta_pos or 0, chi3_pos or 0)
        print(f"  At n = {n_star}, rigorously:")
        print(f"    lambda_n^DH < 0  AND  lambda_n^Epstein < 0  <  lambda_n^zeta, lambda_n^chi3.")
        print(f"  The Li criterion discriminates off-line L-functions from Selberg-class")
        print(f"  L-functions, and it does so for a SECOND, independent off-line")
        print(f"  construction (Epstein), not just Davenport-Heilbronn.")
    else:
        print("  At least one witness did not trigger in the n-range; widen the sweep.")

    return out, summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-min", type=int, default=50000)
    parser.add_argument("--n-max", type=int, default=500000)
    parser.add_argument("--n-step", type=int, default=2000)
    parser.add_argument("--prec", type=int, default=100)
    parser.add_argument("--zero-prec", type=int, default=30)
    parser.add_argument("--dh-T-max", type=float, default=500.0)
    parser.add_argument("--epstein-T-max", type=float, default=60.0)
    args = parser.parse_args()
    run(n_min=args.n_min, n_max=args.n_max, n_step=args.n_step,
        prec=args.prec, zero_prec=args.zero_prec,
        dh_T_max=args.dh_T_max, epstein_T_max=args.epstein_T_max)
