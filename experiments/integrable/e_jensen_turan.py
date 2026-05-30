"""Jensen polynomials and Turan inequalities for xi vs the completed D-H function.

Direction 13 (docs/03_research/research_directions/13_infinite_genus_tau_function.md)
proposes realizing the completed xi(s) as a tau-function, where RH becomes the
positivity of an infinite-genus period form. The cheapest, most rigorous entry
point is the Jensen-polynomial / Turan-inequality framework (Polya;
Csordas-Norfolk-Varga 1986; Griffin-Ono-Rolen-Zagier 2019). These are exactly
the degree-1 Hodge-Riemann (log-concavity / real-rootedness) content, so this
experiment is simultaneously the falsification test for Direction 9's
"log-concavity" claim and Direction 13's "tau-function/integrable" claim.

Setup. For a real entire function with even part written as
    Xi(z) = sum_{m>=0} c_m z^{2m},
define the Polya moments a_m = (-1)^m c_m (these are POSITIVE for zeta, the
moments of the Polya measure). The Jensen polynomial of degree d, shift n is
    J^{d,n}(X) = sum_{j=0}^d  C(d,j) a_{n+j} X^j.
Pólya-Jensen theorem: Xi has only REAL zeros (RH, for zeta) IFF every J^{d,n}
is hyperbolic (all real roots). The degree-2 case is the Turan inequality
    a_{n+1}^2 >= a_n a_{n+2}.

Decisive question (the D-H discipline). zeta should satisfy hyperbolicity
(GORZ 2019 proved it for all large n). The completed Davenport-Heilbronn
function has off-line zeros, hence Xi_DH has NON-REAL zeros, so SOME Jensen
polynomial must be non-hyperbolic. Does the violation appear at a reachable
(d, n) and precision, or is it buried below a stealth-window floor (the
off-line zeros sit at height ~85.7, far from z=0)? We report which, and we
include the Epstein d=47 principal control (non-Euler but RH-holding up to
T=120) to separate "detects non-Euler-ness" from "detects RH-failure"
(the LEARNINGS #20 reformulation trap).

Outputs:
  - e_jensen_turan.npz
  - e_jensen_turan.png
"""

from __future__ import annotations

import argparse
import time
from math import comb
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np


# ---------------------------------------------------------------------------
# Completed functions (entire, real on the critical line, even in z = -i(s-1/2))
# ---------------------------------------------------------------------------

def xi_zeta(s):
    """Riemann xi: xi(s) = (1/2) s (s-1) pi^{-s/2} Gamma(s/2) zeta(s). Entire."""
    s = mp.mpc(s)
    return mp.mpf(1) / 2 * s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def _dh_f(s):
    """The raw Davenport-Heilbronn Dirichlet series via Hurwitz zeta."""
    s = mp.mpc(s)
    sqrt5 = mp.sqrt(5)
    k = (mp.sqrt(10 - 2 * sqrt5) - 2) / (sqrt5 - 1)
    c = [mp.mpf(1), k, -k, mp.mpf(-1), mp.mpf(0)]
    return mp.power(5, -s) * sum(c[a - 1] * mp.zeta(s, mp.mpf(a) / 5) for a in range(1, 6))


def xi_dh(s):
    """A symmetric completion of D-H (odd character, conductor 5).

    Lambda(s) = (5/pi)^{s/2} Gamma((s+1)/2) f(s). For an odd character of
    conductor 5 this is the natural gamma factor; we verify realness on the
    line and the s <-> 1-s symmetry numerically in run().
    """
    s = mp.mpc(s)
    return mp.power(5 / mp.pi, s / 2) * mp.gamma((s + 1) / 2) * _dh_f(s)


def xi_epstein_d47_principal(s):
    """Entire completed Epstein zeta for the d=47 principal form (non-Euler, RH ok <=120).

    The bare completion pi^{-s} Gamma(s) E(tau,s) has simple poles at s=0,1
    (from the Eisenstein pole at s=1 and the Gamma pole at s=0). The factor
    (1/2) s (s-1), which is symmetric under s <-> 1-s, clears both and leaves
    an entire, real-on-the-line, even-in-z function, exactly as Riemann's xi
    does for zeta. This is the d=47 principal control: non-Euler but with NO
    off-line zeros up to T=120 (LEARNINGS #20).
    """
    from experiments._shared.epstein_zeta import epstein_d47_principal
    s = mp.mpc(s)
    return mp.mpf(1) / 2 * s * (s - 1) * epstein_d47_principal.completed(s)


# ---------------------------------------------------------------------------
# Polya moments and Jensen polynomials
# ---------------------------------------------------------------------------

def polya_moments(xi_func, M, prec, N=65, radius="1.0"):
    """Even Taylor coefficients of Xi(z) = xi_func(1/2 + i z), then Polya moments.

    Returns (a, c, diag) where c_m = coeff of z^{2m} in Xi(z),
    a_m = (-1)^m c_m (the Polya moments), and diag is a dict of accuracy
    diagnostics. Coefficients are extracted by sampling Xi on a circle of
    radius `radius` at N points and applying the discrete Cauchy transform
        c_k = (1 / (N r^k)) sum_j Xi(r w^j) w^{-jk},   w = exp(2 pi i / N),
    which costs N function evaluations total (not per coefficient) and is far
    faster and more stable here than mp.taylor's adaptive quadrature.

    Built-in accuracy checks: for an even real Xi the odd coefficients and the
    imaginary parts of the even coefficients must vanish; their max magnitude
    is returned as a noise floor.
    """
    mp.mp.dps = prec
    r = mp.mpf(radius)

    def Xi(z):
        return xi_func(mp.mpf(1) / 2 + mp.mpc(0, 1) * z)

    samples = [Xi(r * mp.expjpi(mp.mpf(2) * j / N)) for j in range(N)]
    c_full = []
    for k in range(2 * M + 1):
        acc = mp.mpc(0)
        for j in range(N):
            acc += samples[j] * mp.expjpi(mp.mpf(-2) * j * k / N)
        c_full.append(acc / (N * mp.power(r, k)))
    odd_resid = max(abs(c_full[2 * m + 1]) for m in range(M)) if M > 0 else mp.mpf(0)
    even_imag = max(abs(c_full[2 * m].imag) for m in range(M + 1))
    noise = float(max(odd_resid, even_imag))
    c = [c_full[2 * m].real for m in range(M + 1)]
    a = [((-1) ** m) * c[m] for m in range(M + 1)]
    diag = dict(noise_floor=noise, odd_resid=float(odd_resid),
                even_imag=float(even_imag))
    return a, c, diag


def jensen_polynomial_roots(a, d, n):
    """Roots of J^{d,n}(X) = sum_{j=0}^d C(d,j) a_{n+j} X^j (numpy, descending)."""
    if n + d >= len(a):
        return None
    coeffs_low_to_high = [comb(d, j) * float(a[n + j]) for j in range(d + 1)]
    poly = np.array(coeffs_low_to_high[::-1], dtype=float)
    # strip leading zeros
    while len(poly) > 1 and poly[0] == 0.0:
        poly = poly[1:]
    if len(poly) <= 1:
        return np.array([])
    return np.roots(poly)


def hyperbolicity_report(a, d_list, n_max_shift):
    """For each degree d, find the shifts n where J^{d,n} is NON-hyperbolic.

    Returns dict d -> (n_tested, n_nonhyperbolic, list_of_bad_shifts,
    max_imag_part_seen).
    """
    out = {}
    for d in d_list:
        bad = []
        tested = 0
        max_imag = 0.0
        for n in range(0, n_max_shift + 1):
            r = jensen_polynomial_roots(a, d, n)
            if r is None:
                break
            tested += 1
            imag = float(np.max(np.abs(r.imag))) if len(r) else 0.0
            max_imag = max(max_imag, imag)
            # numerically non-hyperbolic if any root has appreciable imaginary part
            if imag > 1e-9 * (1 + float(np.max(np.abs(r.real))) if len(r) else 1.0):
                bad.append(n)
        out[d] = (tested, len(bad), bad, max_imag)
    return out


def turan_defects(a):
    """Degree-2 Turan defect T_n = a_{n+1}^2 - a_n a_{n+2} (>=0 means OK)."""
    a = [float(x) for x in a]
    T = []
    for n in range(len(a) - 2):
        T.append(a[n + 1] ** 2 - a[n] * a[n + 2])
    return np.array(T)


# ---------------------------------------------------------------------------

def run(M=36, prec=50, d_list=(2, 3, 4), include_epstein=True, out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    # Sanity gates on the completions.
    mp.mp.dps = prec
    print("[JT] Completion sanity checks:")
    for name, f in [("zeta", xi_zeta), ("D-H", xi_dh)]:
        line_val = f(mp.mpc(mp.mpf(1) / 2, mp.mpf(20)))
        sym = abs(f(mp.mpc("0.3", "12")) - f(mp.mpc("0.7", "12")))
        print(f"     {name}: Xi(1/2+20i) = {complex(line_val):.6g}  "
              f"|Lambda(0.3+12i)-Lambda(0.7+12i)| = {float(sym):.3e}")

    targets = [("zeta", xi_zeta), ("D-H", xi_dh)]
    if include_epstein:
        targets.append(("Epstein d47 principal", xi_epstein_d47_principal))

    results = {}
    for name, f in targets:
        print(f"[JT] {name}: computing {M+1} Polya moments at {prec} dps...")
        t0 = time.time()
        try:
            a, c, diag = polya_moments(f, M, prec)
        except Exception as e:
            print(f"     FAILED Taylor extraction: {e}")
            continue
        n_pos = sum(1 for x in a if float(x) > 0)
        # Trust only moments well above the extraction noise floor.
        floor = max(diag["noise_floor"] * 1e3, 0.0)
        M_trust = M
        for m in range(M + 1):
            if abs(float(a[m])) < floor:
                M_trust = m - 1
                break
        a_trust = a[: M_trust + 1]
        print(f"     moments a_m: {n_pos}/{len(a)} positive; noise floor {diag['noise_floor']:.1e}; "
              f"trusting m<= {M_trust}; a_0={float(a[0]):.4e}, a_1={float(a[1]):.4e}  "
              f"[{time.time()-t0:.1f}s]")
        T = turan_defects(a_trust)
        turan_viol = int((T < 0).sum())
        hyp = hyperbolicity_report(a_trust, d_list,
                                   n_max_shift=max(0, M_trust - max(d_list) - 1))
        print(f"     Turan (d=2) violations: {turan_viol}/{len(T)}")
        for d in d_list:
            tested, nbad, bad, mxim = hyp[d]
            first_bad = bad[0] if bad else None
            print(f"     Jensen d={d}: {nbad}/{tested} non-hyperbolic shifts; "
                  f"first bad shift n={first_bad}; max|Im root|={mxim:.2e}")
        results[name] = dict(a=np.array([float(x) for x in a]),
                             c=np.array([float(x) for x in c]),
                             T=T, turan_viol=turan_viol,
                             hyp={d: (hyp[d][0], hyp[d][1], hyp[d][3]) for d in d_list},
                             first_bad={d: (hyp[d][2][0] if hyp[d][2] else -1) for d in d_list})

    # ---- Decision ----
    print("\n[JT] ===== DECISION =====")
    if "zeta" in results and "D-H" in results:
        zt = results["zeta"]["turan_viol"]
        dt = results["D-H"]["turan_viol"]
        z_hyp_bad = sum(results["zeta"]["hyp"][d][1] for d in d_list)
        d_hyp_bad = sum(results["D-H"]["hyp"][d][1] for d in d_list)
        print(f"     Turan violations: zeta={zt}, D-H={dt}")
        print(f"     Non-hyperbolic Jensen shifts (summed over d): zeta={z_hyp_bad}, D-H={d_hyp_bad}")
        ep = results.get("Epstein d47 principal")
        if ep is not None:
            ep_hyp_bad = sum(ep["hyp"][d][1] for d in d_list)
            print(f"     Epstein d47 principal (non-Euler, RH-ok): Turan={ep['turan_viol']}, "
                  f"non-hyperbolic={ep_hyp_bad}")
            if d_hyp_bad > z_hyp_bad and ep_hyp_bad <= z_hyp_bad:
                print("     -> D-H fails hyperbolicity where zeta AND the non-Euler-but-RH")
                print("        Epstein control PASS. The test tracks RH-FAILURE (off-line zeros),")
                print("        not mere non-Euler-ness. Direction 13 gets a clean D-H discriminator.")
            elif ep is not None and ep_hyp_bad > z_hyp_bad:
                print("     -> The non-Euler-but-RH Epstein control ALSO fails. The test tracks")
                print("        NON-EULER-NESS, not RH-failure (LEARNINGS #20 reformulation trap).")
            elif d_hyp_bad == 0 and z_hyp_bad == 0:
                print("     -> STEALTH WINDOW: NO function fails hyperbolicity at this Taylor")
                print("        order, not even D-H. The xi-moment / Jensen basis is dominated by")
                print("        the LOW zeros near z=0; the off-line zeros at height ~85.7 perturb")
                print("        the low-order moments below the detection floor. Contrast e3n:")
                print("        the Li-coefficient basis (sums over ALL zeros) DOES see the non-")
                print("        Euler zero distribution. Two bases, two different walls -- both")
                print("        compass readings consistent with marginal positivity (#18/#19).")
            else:
                print("     -> Inconclusive separation; inspect first-bad shifts and precision.")
        else:
            if d_hyp_bad > z_hyp_bad:
                print("     -> D-H fails hyperbolicity where zeta passes (run with Epstein to")
                print("        rule out the non-Euler trap).")
            else:
                print("     -> No discrimination at this M/prec: off-line zeros at height ~85.7 are")
                print("        below the low-order-Taylor detection floor (stealth window). This is")
                print("        the marginal-positivity wall in the Jensen basis, a compass reading.")

    # ---- Save + plot ----
    save = {}
    for name, r in results.items():
        key = name.replace(" ", "_")
        save[f"a_{key}"] = r["a"]
        save[f"T_{key}"] = r["T"]
    save["M"] = M
    save["prec"] = prec
    np.savez_compressed(out_dir / "e_jensen_turan.npz", **save)

    fig, axs = plt.subplots(1, 2, figsize=(13, 5))
    ax = axs[0]
    for name, r in results.items():
        a = r["a"]
        pos = a > 0
        ax.semilogy(np.arange(len(a))[pos], a[pos], "o-", ms=3, label=f"{name} (a_m>0)")
        if (~pos).any():
            ax.semilogy(np.arange(len(a))[~pos], -a[~pos], "x", ms=6, label=f"{name} (a_m<0)")
    ax.set_xlabel("m"); ax.set_ylabel("|Polya moment a_m|")
    ax.set_title("Polya moments (sign flips signal non-real zeros)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3, which="both")

    ax = axs[1]
    for name, r in results.items():
        T = r["T"]
        ax.plot(np.arange(len(T)), np.sign(T) * np.log10(np.abs(T) + 1e-300),
                "o-", ms=3, label=name)
    ax.axhline(0, color="k", lw=0.5)
    ax.set_xlabel("n"); ax.set_ylabel("sign(T_n) * log10|T_n|")
    ax.set_title("Turan defect T_n = a_{n+1}^2 - a_n a_{n+2}\n(negative = violation)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig(out_dir / "e_jensen_turan.png", dpi=140)
    plt.close()
    print(f"[JT] Saved {out_dir / 'e_jensen_turan.png'}")
    print(f"[JT] Saved {out_dir / 'e_jensen_turan.npz'}")
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--M", type=int, default=36)
    parser.add_argument("--prec", type=int, default=50)
    parser.add_argument("--no-epstein", action="store_true")
    args = parser.parse_args()
    run(M=args.M, prec=args.prec, include_epstein=not args.no_epstein)
