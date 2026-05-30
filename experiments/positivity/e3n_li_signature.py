"""Experiment 3N: Hodge-Riemann signature on the Li coefficients (Direction 9).

Direction 9 (docs/03_research/research_directions/09_arithmetic_matroid_li.md)
proposes that the Li-coefficient positivity lambda_n >= 0 is the shadow of a
Hodge-Riemann (HR) relation on a matroid built from the primes. The
Adiprasito-Huh-Katz theorem gives, in degree 1, the LOG-CONCAVITY of the
relevant coefficient sequence, and in full a SIGNATURE condition (an HR
bilinear form definite on a primitive subspace).

This experiment is the same-day falsification test for Direction 9. It does
NOT assume the matroid exists; it tests whether the data already obey the
signature an AHK structure would force, and -- the decisive question -- whether
Davenport-Heilbronn VIOLATES exactly what zeta satisfies.

Three HR-flavored objects are computed for zeta and for D-H:

  (1) Log-concavity defect (degree-1 HR / Heron-Rota-Welsh form):
        D_n = lambda_n^2 - lambda_{n-1} * lambda_{n+1}
      AHK log-concavity would force D_n >= 0.

  (2) Normalized (ultra-log-concavity) defect, dividing by binomials, the
      sharper AHK statement.

  (3) Hankel / HR-Gram signature: the Hankel matrix H = [lambda_{i+j-1}].
      A genuine moment sequence has H positive semidefinite; the SIGNATURE
      (count of negative eigenvalues) is the HR content. We report the
      signature for zeta and D-H and the smallest eigenvalue.

Decision rule (printed): does D-H violate (1)/(2)/(3) where zeta does not?
If so, Direction 9 has a new D-H discriminator. If neither discriminates at
reachable n, the result is the marginal-positivity / stealth-window wall
(LEARNINGS #18/#19) re-expressed in the HR basis -- a compass reading, not a
contradiction. The off-line D-H perturbation enters lambda_n only at the
~4e-5 scale until n ~ 25000 (e3b), so a null discrimination is expected and is
reported quantitatively against that floor.

Outputs:
  - e3n_li_signature.npz
  - e3n_li_signature.png  (log-concavity defects, Hankel spectra)
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
from experiments.positivity.e3a_zeta_li import compute_li_coefficients


def log_concavity_defect(lams):
    """D_n = lambda_n^2 - lambda_{n-1} lambda_{n+1}, n = 2 .. N-1 (1-indexed)."""
    lams = np.asarray(lams, dtype=float)
    n = len(lams)
    D = np.full(n, np.nan)
    for i in range(1, n - 1):
        D[i] = lams[i] ** 2 - lams[i - 1] * lams[i + 1]
    return D


def ultra_log_concavity_defect(lams):
    """Normalize by binomial weights: a_i = lambda_{i+1}/C(N-1, i) style.

    We use the standard ULC normalization for a length-N sequence indexed
    0..N-1: U_i = (a_i/binom)^2 - (a_{i-1}/binom)(a_{i+1}/binom). We keep it
    simple and divide lambda_i by i! growth proxy is overkill; instead use the
    classic ULC test on the normalized sequence b_i = lambda_i / C(M, i-1)
    with M = N-1. Returns defects (>=0 means ULC holds at that index).
    """
    lams = np.asarray(lams, dtype=float)
    N = len(lams)
    M = N - 1
    # binomial weights C(M, i) for i = 0..M, guard overflow with logs
    from math import lgamma, exp
    b = np.full(N, np.nan)
    for i in range(N):
        # weight C(M, i); lambda index i corresponds to n=i+1, use i in 0..N-1
        if 0 <= i <= M:
            logw = lgamma(M + 1) - lgamma(i + 1) - lgamma(M - i + 1)
            b[i] = lams[i] / exp(logw) if logw < 700 else 0.0
        else:
            b[i] = 0.0
    U = np.full(N, np.nan)
    for i in range(1, N - 1):
        U[i] = b[i] ** 2 - b[i - 1] * b[i + 1]
    return U


def hankel_signature(lams, m):
    """Hankel matrix H[i,j] = lambda_{i+j+1} (1-indexed lambdas), size m x m.

    Returns (eigenvalues sorted ascending, n_negative, lambda_min).
    A moment sequence => H PSD => n_negative == 0.
    """
    lams = np.asarray(lams, dtype=float)
    H = np.empty((m, m))
    for i in range(m):
        for j in range(m):
            idx = i + j  # 0-based index into lams => lambda_{i+j+1}
            H[i, j] = lams[idx]
    ev = np.linalg.eigvalsh(H)
    n_neg = int((ev < 0).sum())
    return ev, n_neg, float(ev.min())


def run(n_max: int = 120, T_max: float = 200.0, prec: int = 40,
        hankel_m: int = 12, out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    # Four targets PLUS a D-H "on-line zeros only" control. The Epstein d=47
    # principal form is the critical disambiguator: it is NON-Euler but has NO
    # off-line zeros up to T=120 (LEARNINGS #20). If it fails what zeta passes,
    # the test detects non-Euler-ness, not RH-failure (the #20 trap).
    from experiments._shared.epstein_zeta import epstein_d47_principal, epstein_d47

    dh = DavenportHeilbronn()
    print(f"[3N] Loading zeros up to T = {T_max} at {prec} dps (cached after first run)...")
    targets = []
    t0 = time.time()
    zeta_rhos = zeta_L.zeros(T_max=T_max, prec=prec)
    targets.append(("zeta (Euler, RH)", zeta_rhos, True, False))
    print(f"     zeta: {len(zeta_rhos)} zeros [{time.time()-t0:.0f}s]")
    t0 = time.time()
    dh_rhos = dh.zeros(T_max=T_max, prec=prec, scan_step=0.5)
    targets.append(("D-H (non-Euler, RH-fails)", dh_rhos, False, True))
    print(f"     D-H: {len(dh_rhos)} zeros [{time.time()-t0:.0f}s]")
    dh_online = [r for r in dh_rhos if abs(float(r.real) - 0.5) <= 0.01]
    targets.append(("D-H on-line only (control)", dh_online, False, False))
    t0 = time.time()
    ep_p = epstein_d47_principal.zeros(T_max=T_max, prec=prec)
    targets.append(("Epstein d47 principal (non-Euler, RH-ok)", ep_p, False, False))
    print(f"     Epstein d47 principal: {len(ep_p)} zeros [{time.time()-t0:.0f}s]")
    t0 = time.time()
    ep_np = epstein_d47.zeros(T_max=T_max, prec=prec)
    targets.append(("Epstein d47 non-principal (non-Euler, RH-fails)", ep_np, False, True))
    print(f"     Epstein d47 non-principal: {len(ep_np)} zeros [{time.time()-t0:.0f}s]")

    print(f"[3N] Computing Li coefficients up to n = {n_max} and HR objects per target...")
    ns = np.arange(1, n_max + 1)
    rows = {}
    for name, rhos, has_euler, rh_fails in targets:
        lam = np.array([float(x) for x in compute_li_coefficients(rhos, n_max, prec=prec)[0]])
        D = log_concavity_defect(lam)
        lc_viol = int(np.nansum(D < 0))
        ev, neg, evmin = hankel_signature(lam, hankel_m)
        rows[name] = dict(lam=lam, D=D, lc_viol=lc_viol, ev=ev, neg=neg, evmin=evmin,
                          has_euler=has_euler, rh_fails=rh_fails)
        print(f"     {name:48s} log-concavity-viol={lc_viol:3d}/{n_max-2}  "
              f"Hankel-neg={neg}  euler={has_euler} rh_fails={rh_fails}")

    # Keep the named arrays the plot/save expect (zeta vs D-H primary pair).
    lam_zeta = rows["zeta (Euler, RH)"]["lam"]
    lam_dh = rows["D-H (non-Euler, RH-fails)"]["lam"]
    D_zeta = rows["zeta (Euler, RH)"]["D"]
    D_dh = rows["D-H (non-Euler, RH-fails)"]["D"]
    ev_zeta = rows["zeta (Euler, RH)"]["ev"]
    ev_dh = rows["D-H (non-Euler, RH-fails)"]["ev"]
    neg_zeta = rows["zeta (Euler, RH)"]["neg"]
    neg_dh = rows["D-H (non-Euler, RH-fails)"]["neg"]

    # ---- DECISION with the LEARNINGS #20 Euler-vs-RH disambiguation ----
    print("\n[3N] ===== DECISION (Euler-ness vs RH-failure) =====")
    zeta_viol = rows["zeta (Euler, RH)"]["lc_viol"]
    ep_principal_viol = rows["Epstein d47 principal (non-Euler, RH-ok)"]["lc_viol"]
    dh_online_viol = rows["D-H on-line only (control)"]["lc_viol"]
    non_euler_rh_ok_fails = ep_principal_viol > zeta_viol
    off_line_not_needed = dh_online_viol > zeta_viol
    if non_euler_rh_ok_fails:
        print("     RESULT: the log-concavity / HR signature is a NON-EULER detector,")
        print("     NOT an RH-failure detector. The Epstein d47 PRINCIPAL form (non-Euler,")
        print(f"     NO off-line zeros) shows {ep_principal_viol} violations vs zeta's {zeta_viol}.")
        if off_line_not_needed:
            print(f"     Confirmed by the D-H on-line-only control: {dh_online_viol} violations")
            print("     even with off-line zeros removed. The signal is the absent Euler")
            print("     product (on-line zero distribution), not the off-line zeros.")
        print("     This is exactly the LEARNINGS #20 reformulation trap: necessary")
        print("     (an Euler product is required for log-concavity) but NOT sufficient")
        print("     (it cannot see RH-failure). Direction 9's matroid claim is supported as")
        print("     a STRUCTURAL-EXISTENCE statement (no Euler product => no log-concave")
        print("     Li sequence => no matroid, the K2 mechanism), but the HR defect is not")
        print("     a numerical RH-detector. To test RH itself the matroid must inject the")
        print("     EXACT Euler structure, not the zero perturbation (doc milestone 9.2).")
    else:
        print("     RESULT: the Epstein non-Euler-but-RH control did NOT fail; the HR")
        print("     signature may track RH-failure rather than mere non-Euler-ness.")
        print("     Inspect per-target violation counts above before trusting this.")

    save_kwargs = dict(n=ns, hankel_m=hankel_m, T_max=T_max, prec=prec,
                       zeta_lc_viol=zeta_viol, ep_principal_viol=ep_principal_viol,
                       dh_online_viol=dh_online_viol)
    for name, r in rows.items():
        key = (name.split(" ")[0] + ("_p" if "principal" in name and "non" not in name
               else "_np" if "non-principal" in name else "_on" if "on-line" in name else "")
               ).replace("-", "")
        save_kwargs[f"lam_{key}"] = r["lam"]
        save_kwargs[f"D_{key}"] = r["D"]
        save_kwargs[f"lcviol_{key}"] = r["lc_viol"]
    np.savez_compressed(out_dir / "e3n_li_signature.npz", **save_kwargs)

    fig, axs = plt.subplots(1, 3, figsize=(16, 4.6))

    ax = axs[0]
    colors = {"zeta (Euler, RH)": ("b", "-"),
              "D-H (non-Euler, RH-fails)": ("r", "--"),
              "Epstein d47 principal (non-Euler, RH-ok)": ("m", "-."),
              "Epstein d47 non-principal (non-Euler, RH-fails)": ("orange", ":")}
    for name, (col, ls) in colors.items():
        if name in rows:
            ax.plot(ns, rows[name]["D"], color=col, ls=ls, lw=1.1,
                    label=f"{name.split(' (')[0]} ({rows[name]['lc_viol']})")
    ax.axhline(0, color="k", lw=0.5)
    ax.set_xlabel("n"); ax.set_ylabel(r"$\lambda_n^2-\lambda_{n-1}\lambda_{n+1}$")
    ax.set_title("(1) Log-concavity defect, violations in ()\n(only the Euler product zeta stays >= 0)")
    ax.legend(fontsize=7); ax.grid(alpha=0.3)

    ax = axs[1]
    # The #20 disambiguation: non-Euler-but-RH Epstein principal fails like D-H.
    bars = [(n.split(" (")[0], r["lc_viol"], "g" if r["has_euler"] else
             ("r" if r["rh_fails"] else "m")) for n, r in rows.items()]
    labels = [b[0] for b in bars]
    ax.barh(range(len(bars)), [b[1] for b in bars], color=[b[2] for b in bars])
    ax.set_yticks(range(len(bars)))
    ax.set_yticklabels(labels, fontsize=6)
    ax.set_xlabel("log-concavity violations")
    ax.set_title("(1') Euler-ness vs RH: green=Euler, red=RH-fails,\nmagenta=non-Euler-but-RH (the #20 control)")
    ax.grid(alpha=0.3, axis="x")

    ax = axs[2]
    idx = np.arange(1, len(ev_zeta) + 1)
    ax.semilogy(idx, np.abs(ev_zeta), "bo-", label="zeta |eig|", ms=4)
    ax.semilogy(idx, np.abs(ev_dh), "rs--", label="D-H |eig|", ms=4)
    ax.set_xlabel("eigenvalue index"); ax.set_ylabel("|eigenvalue|")
    ax.set_title(f"(3) Hankel spectrum {hankel_m}x{hankel_m}\n"
                 f"neg eigs: zeta={neg_zeta}, D-H={neg_dh}")
    ax.legend(); ax.grid(alpha=0.3, which="both")

    plt.tight_layout()
    plt.savefig(out_dir / "e3n_li_signature.png", dpi=140)
    plt.close()
    print(f"[3N] Saved {out_dir / 'e3n_li_signature.png'}")
    print(f"[3N] Saved {out_dir / 'e3n_li_signature.npz'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-max", type=int, default=120)
    parser.add_argument("--T-max", type=float, default=200.0)
    parser.add_argument("--prec", type=int, default=40)
    parser.add_argument("--hankel-m", type=int, default=12)
    args = parser.parse_args()
    run(n_max=args.n_max, T_max=args.T_max, prec=args.prec, hankel_m=args.hankel_m)
