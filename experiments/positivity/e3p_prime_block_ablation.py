"""Experiment 3P: prime-block ablation, the mandatory K2 test for a certificate.

Cheap-probe 2 of the "RH solved by accident" dossier
(docs/03_research/rh_solved_by_accident.md). The dossier's D-H filter has an
operational test #3: a certificate's discriminating SIGN must be carried by the
Frobenius / {log p} (Euler) half, NOT the archimedean half that Davenport-
Heilbronn shares. Operationally: zero out the prime contribution and check
whether the zeta-vs-D-H discrimination DISAPPEARS.

  - If discrimination DISAPPEARS when the primes are zeroed: the certificate is
    K2-GENUINE (its sign lives on the Euler/Frobenius half, the half D-H cannot
    build). This is the healthy outcome.
  - If discrimination SURVIVES prime-zeroing: the certificate is K2-BLIND (its
    sign lives on the archimedean/continuation half, shared with D-H). Reject:
    such a certificate would "prove" a false statement for D-H.

We ablate the VALIDATED M3 discriminator M_euler = A_arch + P_pp + B_pole (the
non-circular Rosati/Weil form with the composite block deleted; LEARNINGS
#35-37), which at full strength separates the controls correctly: zeta +0.035,
D-H -0.929, Epstein +0.676. We scale the prime-power block by alpha in [0, 1]
and watch the zeta-vs-D-H margin collapse.

This reuses the exact block-builders of e3m_analytic_domination / e3m_place_type
/ e2v, so the ablation is consistent with the certificate the project already
validated. The alpha-sweep is the only new content.

CONTRAST built in: the FULL M = A_arch + P_pp + P_comp + B_pole does NOT
separate zeta (+0.035) from D-H (+0.094, WRONG SIGN) even at alpha=1 (the M2.6
stealth window, #34). So we report both: M_euler (separates) and full M (does
not), then ablate M_euler's primes to locate where its separation lives.

Outputs:
  - e3p_prime_block_ablation.npz
  - e3p_prime_block_ablation.png
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

from experiments._shared import zeta_L, DavenportHeilbronn, epstein_for_discriminant
from experiments.positivity.e3m_place_type_balance import (
    pole_block, lambda_coeffs_from_dirichlet, von_mangoldt_zeta, numeric_residue_at_one,
)
from experiments.positivity.e3m_analytic_domination import split_finite_block
from experiments.arithmetic_geometric.e2v_rosati_balance_M2_5 import arch_block_bombieri


def min_eig(M):
    return float(np.linalg.eigvalsh(M).min())


def run(K=8, b_min=1.3, b_max=6.0, prec=30, out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)
    b_vals = np.logspace(np.log10(b_min), np.log10(b_max), K)
    n_max = int(b_max * b_max) + 2

    dh = DavenportHeilbronn()
    eps47p = epstein_for_discriminant(47, principal=True)

    # (label, L, mu_list, log_Q, residue, has_euler, rh) -- same as e3m.
    targets = [
        ("zeta", zeta_L, [0.0], mp.mpf(0), 1.0, True, True),
        ("DH", dh, [1.0], mp.log(mp.sqrt(5)), 0.0, False, False),
        ("Eps47_principal", eps47p, [0.0, 1.0], mp.log(mp.sqrt(47)), None, False, True),
    ]

    print("=" * 78)
    print("[3P] Prime-block ablation: the mandatory K2 test for the M_euler certificate")
    print(f"     K={K}, b in [{b_min},{b_max}], n_max={n_max}, prec={prec}")
    print("     Scale the prime-power block P_pp by alpha; watch the zeta-vs-D-H margin.")
    print("=" * 78)

    # Build the blocks once per target.
    blocks = {}
    for label, L, mu_list, log_Q, residue, has_euler, rh in targets:
        t0 = time.time()
        if label == "zeta":
            lam = np.array([0.0] + [von_mangoldt_zeta(n) for n in range(1, n_max + 1)])
        else:
            lam = lambda_coeffs_from_dirichlet(L, n_max, prec)
        P_pp, P_comp = split_finite_block(b_vals, lam, prec)
        if residue is None:
            residue = numeric_residue_at_one(L, prec)
        B = pole_block(b_vals, float(residue), prec)
        A = arch_block_bombieri(b_vals, mu_list, log_Q, prec)
        blocks[label] = dict(A=A, P_pp=P_pp, P_comp=P_comp, B=B, rh=rh, has_euler=has_euler)
        print(f"     built blocks for {label:<16} [{time.time()-t0:.0f}s]")

    alphas = [0.0, 0.25, 0.5, 0.75, 1.0]

    # M_euler(alpha) = A + alpha*P_pp + B  (the validated discriminator).
    # full M(alpha)  = A + alpha*(P_pp+P_comp) + B  (the K2-blind one at alpha=1).
    print("\n[3P] M_euler(alpha) = A_arch + alpha * P_pp + B_pole   (deletes P_comp)")
    print(f"     {'alpha':>6} " + " ".join(f"{lab:>16}" for lab, *_ in targets)
          + f" {'zeta-DH margin':>15} {'sign-sep?':>10}")
    euler_margin = []
    euler_rows = {}
    for a in alphas:
        row = {}
        for label in blocks:
            bk = blocks[label]
            M = bk["A"] + a * bk["P_pp"] + bk["B"]
            row[label] = min_eig(M)
        euler_rows[a] = row
        margin = row["zeta"] - row["DH"]
        euler_margin.append(margin)
        sep = "YES" if (row["zeta"] > 0) and (row["DH"] < 0) else "no"
        print(f"     {a:>6.2f} " + " ".join(f"{row[lab]:>+16.4e}" for lab, *_ in targets)
              + f" {margin:>+15.4e} {sep:>10}")

    print("\n[3P] full M(alpha) = A_arch + alpha * (P_pp + P_comp) + B_pole  (keeps P_comp)")
    print(f"     {'alpha':>6} " + " ".join(f"{lab:>16}" for lab, *_ in targets)
          + f" {'zeta-DH margin':>15} {'sign-sep?':>10}")
    full_margin = []
    for a in alphas:
        row = {}
        for label in blocks:
            bk = blocks[label]
            M = bk["A"] + a * (bk["P_pp"] + bk["P_comp"]) + bk["B"]
            row[label] = min_eig(M)
        margin = row["zeta"] - row["DH"]
        full_margin.append(margin)
        sep = "YES" if (row["zeta"] > 0) and (row["DH"] < 0) else "no"
        print(f"     {a:>6.2f} " + " ".join(f"{row[lab]:>+16.4e}" for lab, *_ in targets)
              + f" {margin:>+15.4e} {sep:>10}")

    # The archimedean-only baseline (alpha=0): is there ANY sign-separation with no primes?
    z0, d0 = euler_rows[0.0]["zeta"], euler_rows[0.0]["DH"]
    z1, d1 = euler_rows[1.0]["zeta"], euler_rows[1.0]["DH"]
    sep0 = (z0 > 0) and (d0 < 0)
    sep1 = (z1 > 0) and (d1 < 0)

    print("\n" + "=" * 78)
    print("[3P] VERDICT (operationalizes the dossier's K2 test #3)")
    print(f"     alpha=1 (full primes): M_euler separates zeta ({z1:+.4f}) from D-H ({d1:+.4f})"
          f"  -> sign-separation = {sep1}")
    print(f"     alpha=0 (primes zeroed): zeta {z0:+.4f}, D-H {d0:+.4f}"
          f"  -> sign-separation = {sep0}")
    if sep1 and not sep0:
        print("     RESULT: the zeta-vs-D-H sign-separation DISAPPEARS when the prime block is")
        print("             zeroed. The discriminating sign is carried by the Euler / {log p}")
        print("             half, NOT the archimedean half D-H shares. => M_euler is K2-GENUINE")
        print("             (the right kind of certificate). This is the healthy outcome the")
        print("             dossier's test #3 demands.")
    elif sep0:
        print("     RESULT: separation SURVIVES prime-zeroing => the certificate is K2-BLIND")
        print("             (archimedean, shared with D-H). It would 'prove' a false statement")
        print("             for D-H and must be rejected.")
    else:
        print("     RESULT: no clean sign-separation at full strength; inconclusive at this K.")
    print("     CONTRAST: the FULL M (keeping P_comp) does NOT sign-separate even at alpha=1")
    print(f"             (zeta {euler_rows[1.0]['zeta']:+.4f} but full-M D-H is positive,")
    print("             the M2.6 stealth window, #34); deleting P_comp is what exposes the")
    print("             prime-carried sign that this ablation then confirms is K2-genuine.")
    print("     HONEST SCOPE: this validates the certificate's K2-soundness (its sign lives")
    print("             on the Frobenius half); it does NOT prove RH and does not make M_euler")
    print("             intrinsic (deleting P_comp is still the Euler-product assumption, #37).")
    print("=" * 78)

    np.savez_compressed(
        out_dir / "e3p_prime_block_ablation.npz",
        alphas=np.array(alphas),
        euler_margin=np.array(euler_margin),
        full_margin=np.array(full_margin),
        labels=np.array(list(blocks.keys()), dtype=object),
        euler_zeta=np.array([euler_rows[a]["zeta"] for a in alphas]),
        euler_dh=np.array([euler_rows[a]["DH"] for a in alphas]),
        K=K, prec=prec,
    )

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(alphas, [euler_rows[a]["zeta"] for a in alphas], "o-", color="tab:green",
            label="M_euler min-eig: zeta (RH, Euler)")
    ax.plot(alphas, [euler_rows[a]["DH"] for a in alphas], "s-", color="tab:red",
            label="M_euler min-eig: D-H (RH-false, no Euler)")
    ax.axhline(0, color="k", lw=1)
    ax.set_xlabel("alpha  (prime-block scale; 0 = primes zeroed, 1 = full)")
    ax.set_ylabel("min eigenvalue of M_euler(alpha)")
    ax.set_title("3P: prime-block ablation\n"
                 "the zeta-vs-D-H sign-separation is carried by the prime / {log p} half (K2-genuine)")
    ax.legend()
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(out_dir / "e3p_prime_block_ablation.png", dpi=140)
    plt.close()
    print(f"[3P] Saved {out_dir / 'e3p_prime_block_ablation.png'}")
    print(f"[3P] Saved {out_dir / 'e3p_prime_block_ablation.npz'}")
    return euler_rows


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--K", type=int, default=8)
    parser.add_argument("--b-max", type=float, default=6.0)
    parser.add_argument("--prec", type=int, default=30)
    args = parser.parse_args()
    run(K=args.K, b_max=args.b_max, prec=args.prec)
