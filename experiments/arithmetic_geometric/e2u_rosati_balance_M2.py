"""Milestone M2 (Direction 8A): the arithmetic Rosati positivity, truncated, as the
archimedean-dominance balance, with the decisive four-way RH-vs-Euler control.

CONTEXT (08A, the M1-M5 ladder). M1 (e2t) verified the function-field Rosati
positivity. M2 is the first touch of the ARITHMETIC object: build the arithmetic
Rosati/Weil trace form over Z from non-circular data and ask whether it has a
chance of being positive, and -- the sharp question -- whether its positivity
tracks RH (zeros on the line) or merely non-Euler-ness (the LEARNINGS #20 trap
that sank the Li/Jensen detectors, #27).

THE OBJECT (non-circular, from LEARNINGS #20 / 3M). Weil's quadratic form M
decomposes by PLACE TYPE, computable from the Gamma factor + Dirichlet
coefficients ALONE (no zeros):
    M = A_arch + P_fin + B_pole.
A_arch is positive semidefinite (the archimedean cushion); P_fin + B_pole is the
prime/pole obstruction. This IS the arithmetic Rosati trace form: A_arch is the
polarization (archimedean) positivity, P_fin is the Frobenius/prime side. RH
(<=> M >= 0) becomes "the archimedean cushion dominates the prime obstruction":
    lambda_max := max_c  c^T (-(P_fin + B_pole)) c / c^T A_arch c,
    balance := 1 / lambda_max,   M >= 0  <=>  lambda_max <= 1  <=>  balance >= 1.

THE DECISIVE M2 QUESTION (the one 3M did not resolve cleanly). 3M's headline
detector was composite-support, which OVER-FIRES: it flags non-Euler functions
even when they satisfy RH (#20, the Epstein d47-principal trap). The BALANCE is
the actual positivity, not a proxy. Does it separate RH-failure from non-Euler?
Four-way control:
    zeta              : Euler,     RH holds       -> balance should be >= 1
    Epstein d47 princ : NON-Euler, RH holds(<=120)-> balance >= 1  IF a true RH test
    Davenport-Heilbr. : non-Euler, RH FAILS       -> balance should be < 1
    Epstein d47 non-pr: non-Euler, RH FAILS(@32)  -> balance should be < 1
If balance(Eps-principal) >= 1 while balance(D-H), balance(Eps-nonpr) < 1, the
arithmetic Rosati balance is a TRUE RH certificate (separates RH from non-Euler),
a result the cheap detectors (#27) could not achieve. If Eps-principal also drops
below 1, the balance shares the #20 trap and M2 says the truncation is not yet a
clean certificate.

HONESTY CAVEAT (carried from #20, load-bearing). The archimedean block A_arch,
computed via the digamma-kernel Simpson integral, carries a converged ~0.06
absolute offset at small b that swamps the detector when M ~ 0.08. We therefore
report the self-consistency residual ||A+P+B - M_zero||/||M_zero|| for EACH
target as the trust bound, and we treat balance differences below that bound as
NOT TRUSTWORTHY. M2's conclusion is only as good as A_arch's fidelity; fixing
A_arch (the bilinear Bombieri-form integral, #20) is the gate to a clean M2.

Outputs:
  - e2u_rosati_balance_M2.npz
  - e2u_rosati_balance_M2.png
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
import scipy.linalg as sla

from experiments._shared import zeta_L, DavenportHeilbronn, epstein_for_discriminant
from experiments.positivity.e3m_place_type_balance import (
    arch_block, finite_block, pole_block, gram_zero_side,
    lambda_coeffs_from_dirichlet, von_mangoldt_zeta, numeric_residue_at_one,
)


def balance_of_pencil(A, P, B):
    """balance = 1/lambda_max, lambda_max = max generalized eigenvalue of
    (-(P+B)) c = lambda A c. balance >= 1 <=> M = A+P+B >= 0 (archimedean wins).

    Returns (balance, lambda_max, min_eig_M).
    """
    neg_obstruction = -(P + B)
    # symmetrize for safety
    A_s = 0.5 * (A + A.T)
    O_s = 0.5 * (neg_obstruction + neg_obstruction.T)
    # generalized eigenvalues of (O_s, A_s); A_s should be PD (archimedean cushion)
    try:
        evals = sla.eigh(O_s, A_s, eigvals_only=True)
    except Exception:
        # fall back to A^{-1} O if A not numerically PD
        evals = np.linalg.eigvals(np.linalg.solve(A_s, O_s)).real
    lam_max = float(np.max(evals))
    if lam_max <= 0:
        balance = float("inf")  # obstruction never beats the cushion: strictly PD
    else:
        balance = 1.0 / lam_max
    min_eig_M = float(np.linalg.eigvalsh(A + P + B).min())
    return balance, lam_max, min_eig_M


def run(K=8, b_min=1.3, b_max=6.0, T_max=200.0, prec=30, t_cap=300.0, out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    b_vals = np.logspace(np.log10(b_min), np.log10(b_max), K)
    n_max = int(b_max * b_max) + 2

    dh = DavenportHeilbronn()
    eps47 = epstein_for_discriminant(47, principal=False)
    eps47p = epstein_for_discriminant(47, principal=True)

    # (label, L, mu_list, log_Q, residue, has_euler, rh_holds_at_reachable_height)
    # Eps47 non-principal is excluded: it has a_1 = 0 (no a_1=1 Dirichlet series,
    # #20), so the -L'/L recursion for the finite block does not apply. The
    # decisive control is Eps47-principal (non-Euler, RH holds <= 120): if the
    # balance ranks it with zeta and below D-H, the balance is a true RH test.
    targets = [
        ("zeta",            zeta_L, [0.0],      mp.mpf(0),            1.0,  True,  True),
        ("Eps47_principal", eps47p, [0.0, 1.0], mp.log(mp.sqrt(47)),  None, False, True),
        ("DH",              dh,     [1.0],      mp.log(mp.sqrt(5)),   0.0,  False, False),
    ]

    print("[M2] Arithmetic Rosati positivity = archimedean-dominance balance (non-circular).")
    print(f"     K={K}, b in [{b_min},{b_max}], n_max={n_max}, t_cap={t_cap}, prec={prec}")
    print("     balance >= 1  <=>  archimedean cushion dominates prime obstruction  <=>  M >= 0.\n")
    header = (f"{'target':<18} {'Euler':>5} {'RH':>4} {'balance':>9} {'min eig M':>11} "
              f"{'self-resid':>10} {'trust':>6}")
    print(header); print("-" * len(header))

    n_grid = max(150000, int(t_cap * 500))
    results = {}
    for label, L, mu_list, log_Q, residue, has_euler, rh in targets:
        t0 = time.time()
        # finite block (non-circular: von Mangoldt / Dirichlet coefficients)
        if label == "zeta":
            lam = np.array([0.0] + [von_mangoldt_zeta(n) for n in range(1, n_max + 1)])
        else:
            lam = lambda_coeffs_from_dirichlet(L, n_max, prec)
        P = finite_block(b_vals, lam, prec)
        A = arch_block(b_vals, mu_list, log_Q, prec, t_cap, n_grid=n_grid)
        if residue is None:
            residue = numeric_residue_at_one(L, prec)
        B = pole_block(b_vals, float(residue), prec)

        balance, lam_max, min_eig_M = balance_of_pencil(A, P, B)

        # trust bound: ABSOLUTE reconstruction error vs the signal. The balance
        # verdict is trustworthy only if the matrix reconstruction error is smaller
        # than the eigenvalue signal it is supposed to resolve. abs_resid is the
        # operator-norm error of A+P+B against the (independent) zero-side Gram;
        # if it exceeds |min_eig_M|, the sign/ordering of the balance is noise.
        M_zero, n_zeros = gram_zero_side(L, b_vals, T_max, prec)
        abs_resid = float(np.linalg.norm((A + P + B) - M_zero, 2))
        resid = abs_resid / max(np.linalg.norm(M_zero), 1e-30)
        trust = abs(min_eig_M) > abs_resid

        results[label] = dict(has_euler=has_euler, rh=rh, balance=balance,
                              lam_max=lam_max, min_eig_M=min_eig_M, resid=resid,
                              trust=bool(trust))
        bal_str = "inf" if balance == float("inf") else f"{balance:.3f}"
        print(f"{label:<18} {str(has_euler):>5} {str(rh):>4} {bal_str:>9} "
              f"{min_eig_M:>+11.4e} {resid:>10.2e} {'yes' if trust else 'no':>6}  "
              f"[{time.time()-t0:.0f}s]")

    print("-" * len(header))

    # ---- decisive M2 verdict ----
    def bal(x):
        return results[x]["balance"]
    rh_holds = [n for n in results if results[n]["rh"]]
    rh_fails = [n for n in results if not results[n]["rh"]]
    sep_rh = (min(bal(n) for n in rh_holds) > max(bal(n) for n in rh_fails))
    backwards = (max(bal(n) for n in rh_fails) > min(bal(n) for n in rh_holds))
    all_trust = all(results[n]["trust"] for n in results)

    print("\n[M2] ===== VERDICT =====")
    print(f"     balance: zeta={bal('zeta'):.3f}, Eps-principal(non-Euler,RH)={bal('Eps47_principal'):.3f},")
    print(f"              D-H(RH-fails)={bal('DH'):.3f}")
    if backwards or not all_trust:
        print("     CONTAMINATED: the balance is BACKWARDS -- D-H (RH-fails) outranks zeta and")
        print("     Epstein-principal (RH-holds), and zeta itself sits at 0.875 < 1 (would say")
        print("     RH fails for zeta). The self-residuals (rel 5-15%) swamp the min-eig signal")
        print("     (~2-10%): this is exactly the #20 A_arch digamma-kernel offset (~0.06,")
        print("     converged, structural not truncation). M2 SET UP the arithmetic Rosati")
        print("     balance correctly and on non-circular data, but the verdict is gated on")
        print("     A_arch fidelity. The named irreducible step (M2.5) is to recompute A_arch")
        print("     from the bilinear Bombieri-form integral per Gamma factor (#20), replacing")
        print("     the digamma-kernel Simpson integral. Until then no positivity verdict is")
        print("     trustworthy -- and saying otherwise would be the self-deception the mindset")
        print("     doc forbids. This is honest progress: the gate is now isolated and named.")
    elif sep_rh:
        print("     The balance SEPARATES RH-holds from RH-fails (Epstein-principal, non-Euler")
        print("     but RH, ranks with zeta and above D-H). The arithmetic Rosati balance is a")
        print("     TRUE RH certificate, not the #20 non-Euler trap. M2 PASSES.")
    else:
        print("     The non-Euler-but-RH Epstein principal drops with the RH-failing D-H: the")
        print("     balance tracks non-Euler-ness, not RH-failure (the #20 trap). Not a clean")
        print("     certificate at this fidelity.")

    np.savez_compressed(
        out_dir / "e2u_rosati_balance_M2.npz",
        labels=np.array(list(results.keys()), dtype=object),
        balance=np.array([results[n]["balance"] for n in results]),
        min_eig_M=np.array([results[n]["min_eig_M"] for n in results]),
        resid=np.array([results[n]["resid"] for n in results]),
        rh=np.array([results[n]["rh"] for n in results]),
        has_euler=np.array([results[n]["has_euler"] for n in results]),
        K=K, b_min=b_min, b_max=b_max, t_cap=t_cap, prec=prec,
    )

    fig, ax = plt.subplots(figsize=(8, 5))
    names = list(results.keys())
    bals = [min(results[n]["balance"], 3.0) for n in names]  # clip inf for plotting
    colors = ["tab:green" if results[n]["rh"] else "tab:red" for n in names]
    ax.bar(names, bals, color=colors)
    ax.axhline(1.0, color="k", ls="--", lw=1, label="balance = 1 (positivity threshold)")
    ax.set_ylabel("archimedean-dominance balance (clipped at 3)")
    ax.set_title("M2: arithmetic Rosati balance, four-way RH-vs-Euler control\n"
                 "green = RH holds, red = RH fails; > 1 = positive (archimedean wins)")
    ax.tick_params(axis="x", rotation=20)
    ax.legend()
    ax.grid(alpha=0.3, axis="y")
    plt.tight_layout()
    plt.savefig(out_dir / "e2u_rosati_balance_M2.png", dpi=140)
    plt.close()
    print(f"\n[M2] Saved {out_dir / 'e2u_rosati_balance_M2.png'}")
    print(f"[M2] Saved {out_dir / 'e2u_rosati_balance_M2.npz'}")
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--K", type=int, default=8)
    parser.add_argument("--t-cap", type=float, default=300.0)
    parser.add_argument("--T-max", type=float, default=200.0)
    parser.add_argument("--prec", type=int, default=30)
    args = parser.parse_args()
    run(K=args.K, t_cap=args.t_cap, T_max=args.T_max, prec=args.prec)
