"""EAC.1 - The impedance probe: passive medium = Euler product, lossless = RH.

Step 2(b) of the acoustic thread. Reads the logarithmic-derivative impedance

    Z_L(s) := -L'(s)/L(s) = sum_{n>=1} Lambda_L(n) / n^s

as the driving-point impedance of the arithmetic medium attached to L. Z_L is
the Laplace transform (in the variable u = log n) of the "generalized von
Mangoldt comb" measure dPsi_L = sum_n Lambda_L(n) delta_{log n}.

KEY DICHOTOMY THIS SCRIPT MAKES CONCRETE. RH's positivity factors into two
DIFFERENT statements, and a passive-network reading separates them cleanly:

  (1) COMB / PRIME-SIDE POSITIVITY  (the medium is PASSIVE):
        Lambda_L(n) >= 0 for all n
      <=> Z_L is completely monotone on (sigma_0, infinity)
          [since (-1)^k Z_L^{(k)}(s) = sum_n Lambda_L(n) (log n)^k n^{-s}]
      <=> Z_L is the Laplace transform of a POSITIVE measure
      <=> the Euler product (Lambda_L = the genuine von Mangoldt comb,
          supported on prime powers with weight log p >= 0).
      This is UNCONDITIONAL (no RH needed) and is exactly the ingredient
      Davenport-Heilbronn lacks. It is the role finding #37 already plays,
      now read as PASSIVITY of the medium.

  (2) LINE-LOCATION POSITIVITY  (the medium is LOSSLESS):
        all non-trivial poles of Z_L (= zeros of L) lie on Re = 1/2
      <=> after the shift s -> s + 1/2, all impedance poles sit on the
          imaginary axis (a Foster lossless / reactance one-port)
      <=> RH.
      This is the circular, R3.5-trace-side positivity (Lagarias 2006:
      m-function Herglotz <=> RH). It is NOT implied by (1).

The script computes the comb Lambda_L(n) exactly (recursion below) for zeta and
for Davenport-Heilbronn, and shows:
  - zeta: Lambda(n) >= 0 for every n (von Mangoldt) -> PASSIVE, unconditional.
  - D-H : Lambda_DH(n) goes NEGATIVE immediately (at n = 3, the first prime
          === 3 mod 5, where the period-5 coefficient is -kappa < 0) -> ACTIVE.
This is the prime-side D-H discriminator that e2db's archimedean m-function
reading was BLIND to: e2db built its positivity from E(z) = xi(1-iz) (the
functional-equation / Gamma side, which D-H also has), and D-H's off-line
obstruction was archimedean-suppressed below the float floor. The impedance
reading sources positivity from the PRIME atoms instead, where D-H fails loudly.

The recursion for the generalized von Mangoldt comb. For L(s) = sum a(n) n^{-s}
with a(1) = 1, the coefficients of -L'/L satisfy
        sum_{d | n} Lambda_L(d) a(n/d) = a(n) log n,
so Lambda_L(1) = 0 and
        Lambda_L(n) = a(n) log n - sum_{d | n, d < n} Lambda_L(d) a(n/d).
For zeta (a == 1) this is the ordinary von Mangoldt Lambda; we verify that as a
control. For D-H, a(n) is the period-5 comb (1, kappa, -kappa, -1, 0).

Outputs:
  - eac1_impedance_passivity.npz : the two combs, sign data, real-axis Z values
  - stdout : the dichotomy table and the first negative D-H index
"""

from __future__ import annotations

import argparse
from pathlib import Path

import mpmath as mp
import numpy as np

from experiments._shared.davenport_heilbronn import davenport_heilbronn


def divisors(n: int):
    ds = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            ds.append(i)
            if i != n // i:
                ds.append(n // i)
        i += 1
    return sorted(ds)


def vonmangoldt_comb(coeff, N: int):
    """Lambda_L(n) for n = 1..N, given a callable coeff(n) = a(n) with a(1)=1.

    Exact up to current mp precision. Returns a list of mp.mpf/mp.mpc.
    """
    Lam = [mp.mpf(0)] * (N + 1)  # Lam[0] unused
    for n in range(1, N + 1):
        an = coeff(n)
        val = an * mp.log(n) if n > 1 else mp.mpf(0)
        for d in divisors(n):
            if d < n:
                val -= Lam[d] * coeff(n // d)
        Lam[n] = val
    return Lam[1:]  # index 0 -> n=1


def zeta_coeff(n: int):
    return mp.mpf(1)


def dh_coeff(n: int):
    # a(n) = period-5 comb (1, kappa, -kappa, -1, 0); a(1) = 1 as required.
    return mp.re(davenport_heilbronn.dirichlet_coefficient(n))


def impedance_real_axis(comb, sigmas):
    """Z_L(sigma) = sum_n Lambda_L(n) n^{-sigma} truncated to len(comb) terms,
    evaluated at the real points in `sigmas`. Returns dict sigma -> value."""
    out = {}
    for sg in sigmas:
        s = mp.mpf(sg)
        total = mp.mpf(0)
        for n in range(2, len(comb) + 1):
            total += comb[n - 1] / mp.power(n, s)
        out[sg] = total
    return out


def run(N: int = 200, dps: int = 40, out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)
    mp.mp.dps = dps

    print("[EAC.1] Impedance probe: PASSIVE (Euler product) vs LOSSLESS (RH).")
    print("        Z_L(s) = -L'/L(s) = sum Lambda_L(n) n^{-s}; passivity <=> comb >= 0.\n")

    zeta_comb = vonmangoldt_comb(zeta_coeff, N)
    dh_comb = vonmangoldt_comb(dh_coeff, N)

    # ---- control: zeta's comb must be the ordinary von Mangoldt (>= 0). ----
    zeta_neg = [n for n in range(1, N + 1) if float(zeta_comb[n - 1]) < -1e-25]
    # sanity: Lambda(4) = log 2, Lambda(6) = 0, Lambda(2)=log2, Lambda(9)=log3
    chk = {
        "Lambda(2)=log2": abs(float(zeta_comb[1] - mp.log(2))) < 1e-20,
        "Lambda(4)=log2": abs(float(zeta_comb[3] - mp.log(2))) < 1e-20,
        "Lambda(6)=0": abs(float(zeta_comb[5])) < 1e-20,
        "Lambda(9)=log3": abs(float(zeta_comb[8] - mp.log(3))) < 1e-20,
    }
    print("  [control] zeta comb == ordinary von Mangoldt:")
    for k, v in chk.items():
        print(f"            {k:18s} {v}")
    print(f"  [control] zeta: # negative comb entries in 1..{N}: {len(zeta_neg)}  "
          f"(expect 0)\n")

    # ---- D-H comb: where does it first go negative? ----
    dh_signs = [float(dh_comb[n - 1]) for n in range(1, N + 1)]
    first_neg = next((n for n in range(1, N + 1) if dh_signs[n - 1] < -1e-25), None)
    n_neg = sum(1 for x in dh_signs if x < -1e-25)
    n_pos = sum(1 for x in dh_signs if x > 1e-25)

    print("  [D-H] first few generalized von Mangoldt comb entries Lambda_DH(n):")
    for n in range(2, 13):
        marker = "  <-- NEGATIVE" if dh_signs[n - 1] < -1e-25 else ""
        print(f"        Lambda_DH({n:2d}) = {dh_signs[n - 1]:+.6f}{marker}")
    print(f"\n  [D-H] first NEGATIVE comb entry at n = {first_neg} "
          f"(prime 3 === 3 mod 5, coeff -kappa < 0)")
    print(f"  [D-H] negative entries in 1..{N}: {n_neg}   positive: {n_pos}")
    print(f"  [D-H] => Z_DH is NOT completely monotone => the medium is ACTIVE,")
    print(f"        not synthesizable as a passive network. This is the prime-side")
    print(f"        discriminator e2db's archimedean m-function reading was blind to.\n")

    # ---- the impedance on the real axis (illustrative, truncated) ----
    sigmas = [1.5, 2.0, 3.0, 5.0]
    Zz = impedance_real_axis(zeta_comb, sigmas)
    Zd = impedance_real_axis(dh_comb, sigmas)
    print("  [real-axis impedance Z(sigma), truncated to N terms]")
    print(f"        {'sigma':>6} {'Z_zeta':>14} {'Z_DH':>14}")
    for sg in sigmas:
        print(f"        {sg:>6.2f} {float(Zz[sg]):>14.6f} {float(Zd[sg]):>14.6f}")
    print("        (zeta: positive & decreasing = completely-monotone-consistent;")
    print("         the FULL untruncated Z_zeta is exactly completely monotone since")
    print("         every Lambda(n) >= 0. D-H's comb has negatives, so no positive")
    print("         representing measure exists -> not passive.)\n")

    print("  [SYNTHESIS] Two DIFFERENT positivities, cleanly separated:")
    print("    (1) PASSIVE  : comb >= 0  <=>  Euler product. UNCONDITIONAL.")
    print("                   zeta PASSES, D-H FAILS (at n=3). The discriminator.")
    print("    (2) LOSSLESS : impedance poles on Re=1/2 (after 1/2-shift, on iR).")
    print("                   = RH. Circular (R3.5 trace side). NOT implied by (1).")
    print("    The missing mathematics is the COUPLING (1)+symmetry => (2), i.e. the")
    print("    Hodge-index / Castelnuovo-Severi step. See eac2_ff_passive_lossless.py.")

    np.savez_compressed(
        out_dir / "eac1_impedance_passivity.npz",
        N=N, dps=dps,
        zeta_comb=np.array([float(x) for x in zeta_comb]),
        dh_comb=np.array(dh_signs),
        zeta_n_negative=len(zeta_neg),
        dh_first_negative=(-1 if first_neg is None else first_neg),
        dh_n_negative=n_neg, dh_n_positive=n_pos,
        sigmas=np.array(sigmas, dtype=float),
        Z_zeta=np.array([float(Zz[s]) for s in sigmas]),
        Z_dh=np.array([float(Zd[s]) for s in sigmas]),
    )
    print(f"\n[EAC.1] Saved {out_dir / 'eac1_impedance_passivity.npz'}")
    return dict(first_neg=first_neg, n_neg=n_neg, zeta_neg=len(zeta_neg))


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Impedance passivity probe (zeta vs D-H).")
    ap.add_argument("--N", type=int, default=200)
    ap.add_argument("--dps", type=int, default=40)
    args = ap.parse_args()
    run(N=args.N, dps=args.dps)
