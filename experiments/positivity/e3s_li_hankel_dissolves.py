"""The moment-MATRIX framing of M4 DISSOLVES over Z: the Li-coefficient Hankel matrix is NOT
positive-semidefinite even for zeta, because zeta's Li sequence is strictly LOG-CONCAVE while a
Hamburger moment sequence must be LOG-CONVEX. So the e2xx trigonometric-moment object (#123) is
GENUS-FAITHFUL (function-field only); over Z only the TERMWISE Li positivity lambda_n >= 0
(= the Weil form) survives. A verified structural no-go from the 2026-06-26 M4 construction attempt
(front 2, scratchpad/m4_attempt/02_moment_gram.md). NOT a proof of anything; a coordinate.

WHY THIS MATTERS (the e2xx caveat, one level up)
------------------------------------------------
e2xx (#123): for a curve C/F_q, RH-for-the-curve <=> the trigonometric MOMENT matrix [c_{|j-k|}]
is PSD (Caratheodory-Toeplitz), c_n the Frobenius-spectrum moments on the circle |u|=1. The natural
lift to zeta would be a MOMENT MATRIX of the zeros. The cleanest arithmetic moment data are the Li
coefficients lambda_n (Li 1997: lambda_n >= 0 for all n <=> RH). Does the Li MOMENT MATRIX (the
Hankel [lambda_{i+j}]) carry RH the way e2xx's Toeplitz matrix does over F_q? NO -- and the reason
is structural, not numerical.

THE STRUCTURAL FACT (rigorous, from the Bombieri-Lagarias asymptotic)
--------------------------------------------------------------------
A Hankel matrix [m_{i+j}] is PSD iff {m_n} is a Hamburger moment sequence m_n = integral x^n d mu,
mu >= 0. By Cauchy-Schwarz any such sequence is LOG-CONVEX: m_n^2 <= m_{n-1} m_{n+1}. But zeta's Li
sequence is strictly LOG-CONCAVE: lambda_n ~ (n/2) log n + c n (Bombieri-Lagarias), and
n -> (n/2) log n is log-concave (its log is log n + log log n - log 2 + o(1), concave), so
lambda_n^2 >= lambda_{n-1} lambda_{n+1} for all large n. Log-concave and log-convex are
INCOMPATIBLE (except geometric), so {lambda_n} is NOT a Hamburger moment sequence, so the Li-Hankel
is NOT PSD for large n. (RH is unaffected: RH is the TERMWISE lambda_n >= 0, NOT the Hankel PSD.)

So the moment-MATRIX is the wrong object over Z: it dissolves. The finite-support Frobenius
spectrum of F_q gives a genuine (finite, PSD-iff-RH) moment matrix; the INFINITE zeta zero-spectrum,
accumulating at the archimedean point, gives a divergent / log-concave sequence whose Hankel is
indefinite regardless of RH. Only the termwise lambda_n >= 0 (the Weil form, the Level-4 object,
#18/#19) survives. This is the #122 genus-1-faithfulness caveat one level up.

WHAT THIS FILE DOES. Computes zeta's Li coefficients, verifies (1) strict log-concavity (the
structural reason, matching the BL asymptotic) and (2) the Li-Hankel is non-PSD at every size, and
states the no-go. K1-clean (a structural fact about the Li sequence; no proof claim). K2: the Li
log-concavity is a NON-Euler detector (#27) -- it does NOT separate D-H; this file does not claim it
does. It is a no-go FOR THE MOMENT-MATRIX FRAMING, narrowing where M4 can live.

Run:
  python -m experiments.positivity.e3s_li_hankel_dissolves
"""

from __future__ import annotations

from pathlib import Path

import numpy as np

from experiments._shared import zeta_L
from experiments.positivity.e3a_zeta_li import compute_li_coefficients


def hankel(seq, k: int) -> np.ndarray:
    return np.array([[seq[i + j] for j in range(k)] for i in range(k)], dtype=float)


def run(n_max: int = 16, T_max: float = 500.0, prec: int = 30, out_dir: Path = None) -> int:
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    print("=" * 88)
    print("e3s: the moment-MATRIX framing of M4 dissolves over Z -- the Li-Hankel is non-PSD")
    print("=" * 88)

    rhos = zeta_L.zeros(T_max=T_max, prec=prec)
    lambdas, _ = compute_li_coefficients(rhos, n_max, prec=prec)
    lam = [float(x) for x in lambdas]                 # lambda_1 .. lambda_{n_max}
    print(f"\nLi coefficients lambda_1..{n_max} (from {len(rhos)} zeta zeros, T_max={T_max}):")
    print("   " + ", ".join(f"{x:.3f}" for x in lam))

    # (1) strict LOG-CONCAVITY (the structural reason; matches BL asymptotic lambda_n ~ (n/2)log n)
    all_positive = all(x > 0 for x in lam)            # RH: termwise positivity (the surviving object)
    log_concave = [lam[i] ** 2 >= lam[i - 1] * lam[i + 1] for i in range(1, len(lam) - 1)]
    n_lc = sum(log_concave)
    # a Hamburger moment sequence is LOG-CONVEX (m_n^2 <= m_{n-1} m_{n+1}); check it FAILS
    log_convex = [lam[i] ** 2 <= lam[i - 1] * lam[i + 1] for i in range(1, len(lam) - 1)]
    n_cvx = sum(log_convex)

    print(f"\n[1] termwise lambda_n > 0 (RH, the SURVIVING object): {all_positive}")
    print(f"    strictly LOG-CONCAVE (lambda_n^2 >= lambda_{{n-1}}lambda_{{n+1}}): {n_lc}/{len(log_concave)}")
    print(f"    LOG-CONVEX (the Hamburger-moment requirement): {n_cvx}/{len(log_convex)}  "
          f"=> NOT a moment sequence")

    # (2) the Li-HANKEL is NON-PSD at every size (the moment matrix dissolves)
    print(f"\n[2] the Li-Hankel [lambda_{{i+j}}] is NON-PSD at every size:")
    rows = []
    for k in (2, 3, 4, 5, 6):
        H = hankel(lam, k)
        ev = np.linalg.eigvalsh(H)
        psd = bool(ev.min() > -1e-9 * max(1.0, ev.max()))
        rows.append({"k": k, "min_eig": float(ev.min()), "relmin": float(ev.min() / ev.max()), "psd": psd})
        print(f"    {k}x{k}: min eig = {ev.min():>9.4f}  rel-min = {ev.min()/ev.max():>8.4f}  PSD = {psd}")

    print("\n" + "=" * 88)
    print("VERDICT (a verified structural NO-GO, not a proof):")
    print("  - zeta's Li sequence is strictly LOG-CONCAVE (lambda_n ~ (n/2)log n, Bombieri-Lagarias),")
    print("    while a Hamburger moment sequence must be LOG-CONVEX. Incompatible => {lambda_n} is")
    print("    NOT a moment sequence => the Li-Hankel is NON-PSD even for zeta (verified above).")
    print("  - So the e2xx moment-MATRIX object (#123) is GENUS-FAITHFUL (a finite Frobenius spectrum");
    print("    over F_q); over Z the infinite, accumulating zero-spectrum makes the matrix DISSOLVE.")
    print("    Only the TERMWISE lambda_n >= 0 (the Weil form, Level-4, #18/#19) survives = the M4")
    print("    object over Z. The #122 genus-1-faithfulness caveat, one level up.")
    print("  - RH is UNAFFECTED (RH = termwise lambda_n >= 0, not the Hankel PSD); M4 untouched.")
    print("=" * 88)

    # ---- assertions ----
    assert all_positive, "the computed Li coefficients must be positive (RH)"
    assert n_lc == len(log_concave) and n_cvx == 0, \
        "the Li sequence must be strictly log-concave (NOT log-convex => not a moment sequence)"
    assert all(not r["psd"] for r in rows), "the Li-Hankel must be non-PSD at every tested size"
    print("\n(all structural assertions hold)")

    out = out_dir / "e3s_li_hankel_dissolves.npz"
    np.savez_compressed(out, lam=np.array(lam), hankel_min_eig=np.array([r["min_eig"] for r in rows]),
                        hankel_sizes=np.array([r["k"] for r in rows]))
    print(f"\nSaved {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
