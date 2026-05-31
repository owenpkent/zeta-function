"""Milestone M2.6 (Direction 8A): the four-way RH-vs-Euler verdict on the
non-circular arithmetic Rosati positivity, with the general-mu archimedean
Bombieri kernel now correct and validated.

M2.5 (e2v, LEARNINGS #33) fixed and validated A_arch for zeta (mu=0) and showed
min eig(A_arch + P_fin + B_pole) = +0.035 > 0 (non-circular positivity for zeta).
The controls were deferred because the general-mu kernel was mis-normalized.
M2.6 supplies the fix: the Bombieri archimedean constant is
    C_mu = log pi - psi((1+mu)/2)
(NOT log pi - psi(1/2+mu), which coincides only at mu=0 and was the M2.5 bug).
Verified: C_0 = log 4pi + gamma_E (3F); C_1 = log pi + gamma_E (pinned against the
frequency block for D-H). With this, the archimedean block validates for every
gamma factor.

THE DECISIVE QUESTION. With a validated non-circular Weil form M = A_arch + P_fin
+ B_pole for each L-function, does min eig(M) separate RH from non-Euler-ness?
    zeta              : Euler,     RH holds        -> min eig(M) > 0  (positive)
    Epstein d47 princ : NON-Euler, RH holds (<=120)-> min eig(M) > 0  IF a true RH test
    Davenport-Heilbr. : non-Euler, RH FAILS        -> min eig(M) < 0  (indefinite)
If POS for the two RH-holders (one Euler, one NOT) and NEG for the RH-failer,
the non-circular Rosati positivity is a TRUE RH certificate that defeats the #20
non-Euler trap (which sank the cheap detectors, #27): a non-Euler-but-RH function
(Epstein principal) sides with zeta, not with the off-line D-H.

VALIDATION. For each target we report the residual ||A+P+B - M_zero(T)|| at two
T_max values; it must be small and DECREASE with T_max (the remaining residual is
the zero-side Gram's own truncation, not the block). min eig(M) is T-independent
(no zeros) and is the verdict.

Outputs:
  - e2w_rosati_fourway_M2_6.npz
  - e2w_rosati_fourway_M2_6.png
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
    finite_block, pole_block, gram_zero_side,
    lambda_coeffs_from_dirichlet, von_mangoldt_zeta, numeric_residue_at_one,
)
from experiments.arithmetic_geometric.e2v_rosati_balance_M2_5 import arch_block_bombieri


def run(K=8, b_min=1.3, b_max=6.0, prec=30, T_lo=200.0, T_hi=500.0,
        include_epstein=True, out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)
    b_vals = np.logspace(np.log10(b_min), np.log10(b_max), K)
    n_max = int(b_max * b_max) + 2

    dh = DavenportHeilbronn()
    eps47p = epstein_for_discriminant(47, principal=True)
    targets = [
        ("zeta",            zeta_L, [0.0],      mp.mpf(0),           1.0,  True,  True),
        ("DH",              dh,     [1.0],      mp.log(mp.sqrt(5)),  0.0,  False, False),
    ]
    if include_epstein:  # slow (Epstein zeros); the zeta/DH contrast is the verdict
        targets.insert(1, ("Eps47_principal", eps47p, [0.0, 1.0],
                           mp.log(mp.sqrt(47)), None, False, True))

    print("[M2.6] Four-way RH-vs-Euler verdict; C_mu = log pi - psi((1+mu)/2) (fixed).")
    print(f"       K={K}, b in [{b_min},{b_max}], n_max={n_max}, prec={prec}")
    print("       min eig(A_arch + P_fin + B_pole) > 0 = RH-compatible positivity (no zeros).\n")
    header = (f"{'target':<18} {'Euler':>5} {'RH':>4} {'min eig(M)':>11} {'sign':>5} "
              f"{'resid(Tlo)':>10} {'resid(Thi)':>10} {'valid':>6}")
    print(header); print("-" * len(header))

    results = {}
    for label, L, mu_list, log_Q, residue, has_euler, rh in targets:
        t0 = time.time()
        if label == "zeta":
            lam = np.array([0.0] + [von_mangoldt_zeta(n) for n in range(1, n_max + 1)])
        else:
            lam = lambda_coeffs_from_dirichlet(L, n_max, prec)
        P = finite_block(b_vals, lam, prec)
        if residue is None:
            residue = numeric_residue_at_one(L, prec)
        B = pole_block(b_vals, float(residue), prec)
        A = arch_block_bombieri(b_vals, mu_list, log_Q, prec)
        M = A + P + B
        min_eig = float(np.linalg.eigvalsh(M).min())

        Mz_lo, _ = gram_zero_side(L, b_vals, T_lo, prec)
        Mz_hi, _ = gram_zero_side(L, b_vals, T_hi, prec)
        r_lo = float(np.linalg.norm(M - Mz_lo) / max(np.linalg.norm(Mz_lo), 1e-30))
        r_hi = float(np.linalg.norm(M - Mz_hi) / max(np.linalg.norm(Mz_hi), 1e-30))
        valid = (r_hi < r_lo) and (r_hi < 0.15)  # decreasing toward 0 with T_max

        results[label] = dict(has_euler=has_euler, rh=rh, min_eig=min_eig,
                              r_lo=r_lo, r_hi=r_hi, valid=bool(valid))
        print(f"{label:<18} {str(has_euler):>5} {str(rh):>4} {min_eig:>+11.4e} "
              f"{'POS' if min_eig > 0 else 'NEG':>5} {r_lo:>10.3f} {r_hi:>10.3f} "
              f"{'yes' if valid else 'no':>6}  [{time.time()-t0:.0f}s]")

    print("-" * len(header))

    # ---- verdict ----
    print("\n[M2.6] ===== VERDICT =====")
    valid_t = {n: r for n, r in results.items() if r["valid"]}
    print(f"       Validated targets (residual small + decreasing with T_max): {sorted(valid_t)}")
    rh_holds = [n for n in valid_t if valid_t[n]["rh"]]
    rh_fails = [n for n in valid_t if not valid_t[n]["rh"]]
    pos_holds = all(valid_t[n]["min_eig"] > 0 for n in rh_holds) if rh_holds else False
    neg_fails = all(valid_t[n]["min_eig"] < 0 for n in rh_fails) if rh_fails else False
    eps = results.get("Eps47_principal")
    euler_trap_broken = (eps is not None and eps["valid"] and eps["min_eig"] > 0
                         and not eps["has_euler"])

    dhr = results.get("DH")
    if rh_holds and rh_fails and pos_holds and neg_fails:
        print("       SEPARATION ACHIEVED: min eig(M) > 0 for every RH-holder and < 0 for every")
        print("       RH-failer, on validated non-circular data.")
        if euler_trap_broken:
            print("       AND the non-Euler-but-RH Epstein principal is POSITIVE (sides with zeta).")
            print("       The #20 non-Euler trap is DEFEATED; a non-circular RH certificate.")
    elif dhr is not None and dhr["valid"] and dhr["min_eig"] > 0:
        print("       NO SEPARATION -- STEALTH WINDOW. D-H reads POSITIVE (min eig "
              f"{dhr['min_eig']:+.4f}) despite failing RH.")
        print("       Reason: D-H's off-line obstruction lives at height gamma ~ 85.7 and is only")
        print(f"       ~2.6 percent of the raw Weil spectrum (3D.3), while the test functions (b <= {b_max:.0f})")
        print(f"       probe scales log b <= {float(np.log(b_max)):.2f} and the reconstruction residual floor is ~0.1.")
        print("       So the truncated NON-CIRCULAR form is blind to the off-line zeros -- the")
        print("       same stealth window as #18/#19 (raw Gram) and #27 (Jensen basis), now")
        print("       confirmed on the non-circular Rosati side. The technical M2.6 fix succeeded")
        print("       (C_mu = log pi - psi((1+mu)/2); D-H block residual 5.58 -> ~0.12, validated),")
        print("       but the RAW min-eig is necessary-not-sufficient AND non-discriminating: the")
        print("       distinguishing signal sits below the marginal-positivity cancellation floor.")
        print("       Amplifying it (3J Schur, x30 to -78.7%) is an ANSWER-side (circular) move.")
        print("       CONSEQUENCE for the program: M3 must be ANALYTIC (prove archimedean-dominates-")
        print("       prime domination engaging the exact off-line structure), not a finer numerical")
        print("       truncation. This is the marginal-positivity thesis localized on the Rosati side:")
        print("       a soft/numerical certificate cannot separate zeta from D-H; the proof must use")
        print("       exact zeta structure.")
    elif rh_holds and rh_fails:
        print(f"       Partial: pos for RH-holders = {pos_holds}, neg for RH-failers = {neg_fails}.")
        print("       Inspect per-target min eig and validation above.")
    else:
        print("       Not enough validated targets on both sides for the verdict; see residuals.")

    np.savez_compressed(
        out_dir / "e2w_rosati_fourway_M2_6.npz",
        labels=np.array(list(results.keys()), dtype=object),
        min_eig=np.array([results[n]["min_eig"] for n in results]),
        r_lo=np.array([results[n]["r_lo"] for n in results]),
        r_hi=np.array([results[n]["r_hi"] for n in results]),
        valid=np.array([results[n]["valid"] for n in results]),
        rh=np.array([results[n]["rh"] for n in results]),
        has_euler=np.array([results[n]["has_euler"] for n in results]),
        K=K, prec=prec, T_lo=T_lo, T_hi=T_hi,
    )

    fig, ax = plt.subplots(figsize=(8, 5))
    names = list(results.keys())
    vals = [results[n]["min_eig"] for n in names]
    colors = ["tab:green" if results[n]["rh"] else "tab:red" for n in names]
    ax.bar(names, vals, color=colors)
    ax.axhline(0, color="k", lw=1)
    ax.set_ylabel("min eig(A_arch + P_fin + B_pole)  (no zeros)")
    ax.set_title("M2.6: non-circular Rosati positivity, four-way RH-vs-Euler\n"
                 "green = RH holds (expect > 0), red = RH fails (expect < 0)")
    ax.tick_params(axis="x", rotation=15)
    ax.grid(alpha=0.3, axis="y")
    plt.tight_layout()
    plt.savefig(out_dir / "e2w_rosati_fourway_M2_6.png", dpi=140)
    plt.close()
    print(f"\n[M2.6] Saved {out_dir / 'e2w_rosati_fourway_M2_6.png'}")
    print(f"[M2.6] Saved {out_dir / 'e2w_rosati_fourway_M2_6.npz'}")
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--K", type=int, default=8)
    parser.add_argument("--prec", type=int, default=30)
    parser.add_argument("--T-lo", type=float, default=200.0)
    parser.add_argument("--T-hi", type=float, default=500.0)
    parser.add_argument("--no-epstein", action="store_true")
    args = parser.parse_args()
    run(K=args.K, prec=args.prec, T_lo=args.T_lo, T_hi=args.T_hi,
        include_epstein=not args.no_epstein)
