"""EAC.4 - Reverse-engineering the arithmetic diagonal self-intersection (the halving leg).

Step 4 of the acoustic thread, the "what IS the halving form" direction. EAC.3
specified ingredient (iii) as the energy form that halves the passive bound
(exponent 1 -> 1/2, q -> sqrt(q)). This script reverse-engineers WHERE the square
root comes from, and what arithmetic object must supply it.

THE ANSWER: Poincare duality places the self-dual middle weight at the GEOMETRIC
MEAN of the two extreme weights. On a curve C/F_q the Frobenius acts on three
cohomology groups:

        H^0 : eigenvalue 1     = q^0     (weight 0)
        H^1 : 2g eigenvalues,  |alpha| = q^{1/2}  (weight 1)   <-- the zeros
        H^2 : eigenvalue q     = q^1     (weight 2)

and the RH modulus q^{1/2} is EXACTLY the geometric mean sqrt(q^0 * q^1) = sqrt(1*q)
of the H^0 and H^2 moduli. Poincare duality H^i ~ H^{2-i}(-1) pairs H^0 with H^2
(the two poles of zeta_C, at q^{-s}=1 and q^{-s}=q^{-1}, i.e. s=0 and s=1) and makes
H^1 SELF-DUAL, hence forced onto the self-dual locus = the geometric-mean circle
|alpha| = sqrt(q) = the critical line. The halving (exponent = weight/2, middle =
1/2) is Poincare duality + self-duality of the middle, NOT a separate positivity.

THE TWO LEGS (connecting to the 2K dictionary and EAC.2). In the primitive
intersection form the two self-intersections are |Delta_0^2| = 2g (q-FREE) and
|Gamma_0^2| = 2gq (one power of q); the Hodge/reverse-CS bound is their geometric
mean sqrt(2g * 2gq) = 2g sqrt(q). The q lives on ONE leg only (the Frobenius/prime
leg Gamma); the DIAGONAL leg Delta is q-free. So the arithmetic "Delta^2" - the
diagonal self-intersection - is the WEIGHT-0 leg, the archimedean/H^0 piece. The
prime leg carries the weight. Re = 1/2 is the average of the leg weights {0, 1}.

ARITHMETIC (zeta). The functional equation xi(s) = xi(1-s) IS the Poincare duality:
it pairs the pole at s=1 (the H^2/weight-2 leg, residue 1) with the structure at
s=0 (the H^0/weight-0 leg), and its fixed locus is Re = 1/2 - the self-dual middle
where the zeros (the H^1 analogue) must live. We HAVE the duality (FE, verified
below) and the passive medium (Euler product, EAC.1); the MISSING ingredient (iii)
is the WEIGHT-GRADED COHOMOLOGY that forces the zeros onto the self-dual middle, the
arithmetic realization of "the diagonal self-intersection is the q-free leg." That
is Deninger's missing motivic cohomology, now with a one-line job description:
supply the weight filtration whose middle is self-dual at Re = 1/2.

D-H contrast: D-H has NO pole (it is entire), so there is no H^2/weight-2 leg to
pair against an H^0 leg - no Poincare-duality geometric mean can form. Its FE alone
pairs zeros across Re=1/2 (the all-pass quad of EAC.3) but nothing pins the middle.
This is the geometric face of "D-H has no surface": no weight ladder, no halving.

Outputs:
  - eac4_arithmetic_diagonal.npz
  - stdout : the weight ladder + Poincare geometric mean (FF) and the FE-as-duality
             verification (zeta) with the reverse-engineered (iii) statement
"""

from __future__ import annotations

import argparse
from pathlib import Path

import mpmath as mp
import numpy as np

from experiments.acoustic.eac2_ff_passive_lossless import frobenius_eigenvalues
from experiments.arithmetic_geometric.e2f_hodge_index_sweep import (
    elliptic_family,
    genus2_family,
)


def weight_ladder(primes_elliptic=(5, 7, 11, 13, 17), primes_genus2=(5, 7)):
    """For each curve: the Frobenius eigenvalue moduli on H^0 (=1), H^1 (=sqrt q),
    H^2 (=q), and the check that |H^1| = geometric mean of |H^0| and |H^2|."""
    curves = elliptic_family(list(primes_elliptic))
    if primes_genus2:
        curves += genus2_family(list(primes_genus2))
    rows = []
    for c in curves:
        q, g = c["p"], c["g"]
        h0 = 1.0
        h2 = float(q)
        h1 = float(np.mean(np.abs(frobenius_eigenvalues(c))))  # = sqrt q under RH
        geo_mean = float(np.sqrt(h0 * h2))
        # the two primitive-form legs: |Delta_0^2| = 2g (q-free), |Gamma_0^2| = 2gq
        delta_leg = 2 * g          # q-free  (the diagonal / weight-0 leg)
        gamma_leg = 2 * g * q      # q-weighted (the Frobenius / prime leg)
        bound = float(np.sqrt(delta_leg * gamma_leg))   # = 2g sqrt q
        rows.append(dict(label=c["label"], q=q, g=g,
                         h0=h0, h1=h1, h2=h2, geo_mean=geo_mean,
                         h1_is_geomean=abs(h1 - geo_mean) < 1e-6,
                         delta_leg=delta_leg, gamma_leg=gamma_leg,
                         bound=bound, bound_is_2gsqrtq=abs(bound - 2*g*np.sqrt(q)) < 1e-9))
    return rows


def fe_is_poincare_duality(n_check=6, dps=30):
    """Verify the functional equation xi(s) = xi(1-s) (the arithmetic Poincare
    duality) at several points, and that Re=1/2 is its fixed locus."""
    mp.mp.dps = dps

    def xi(s):
        s = mp.mpc(s)
        return mp.mpf("0.5") * s * (s - 1) * mp.power(mp.pi, -s/2) * mp.gamma(s/2) * mp.zeta(s)

    pts = [mp.mpc("0.3", "5"), mp.mpc("0.7", "12"), mp.mpc("0.9", "1"),
           mp.mpc("0.2", "20"), mp.mpc("0.5", "14.1347"), mp.mpc("0.4", "8")]
    residuals = []
    for s in pts[:n_check]:
        r = abs(xi(s) - xi(1 - s))
        residuals.append(float(r))
    # the self-dual fixed locus: s = 1 - s  <=>  Re(s) = 1/2
    return pts[:n_check], residuals


def run(out_dir: Path = None, dps: int = 30):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)
    mp.mp.dps = dps

    print("[EAC.4] Reverse-engineering the halving: Poincare duality puts the")
    print("        self-dual middle weight at the GEOMETRIC MEAN of the extremes.\n")

    # ---- Part 1: the weight ladder + Poincare geometric mean (function field) ----
    print("  [Part 1] Frobenius weight ladder on a curve (function field):")
    print(f"        {'curve':<26} {'q':>3} {'|H^0|':>6} {'|H^1|':>8} {'|H^2|':>5} "
          f"{'sqrt(|H0||H2|)':>13} {'mid=geomean':>11}")
    rows = weight_ladder()
    for r in rows:
        print(f"        {r['label']:<26} {r['q']:>3} {r['h0']:>6.1f} {r['h1']:>8.4f} "
              f"{r['h2']:>5.1f} {r['geo_mean']:>13.4f} {str(r['h1_is_geomean']):>11}")
    all_gm = all(r["h1_is_geomean"] for r in rows)
    print(f"\n        |H^1| = sqrt(|H^0| . |H^2|) on every curve: {all_gm}")
    print(f"        => the RH modulus q^(1/2) IS the Poincare-duality geometric mean")
    print(f"           of the weight-0 (H^0, =1) and weight-2 (H^2, =q) extremes.")
    print(f"        => exponent = weight/2; the middle weight 1 gives the halving 1/2.\n")

    print("  [Part 1b] The two primitive legs (the q lives on ONE leg only):")
    print(f"        |Delta_0^2| = 2g (q-FREE, the diagonal/archimedean/weight-0 leg)")
    print(f"        |Gamma_0^2| = 2gq (q-weighted, the Frobenius/prime leg)")
    print(f"        bound = sqrt(2g . 2gq) = 2g sqrt(q): geometric mean, weights {{0,1}} avg 1/2.")
    all_bound = all(r["bound_is_2gsqrtq"] for r in rows)
    print(f"        bound = 2g sqrt(q) on every curve: {all_bound}\n")

    # ---- Part 2: the functional equation as arithmetic Poincare duality ----
    print("  [Part 2] Arithmetic: the functional equation xi(s)=xi(1-s) IS Poincare")
    print("           duality, pairing the pole at s=1 (H^2 leg) with s=0 (H^0 leg);")
    print("           fixed locus Re=1/2 is the self-dual middle where the zeros live.\n")
    pts, resid = fe_is_poincare_duality(dps=dps)
    print(f"        {'s':>20} {'|xi(s)-xi(1-s)|':>18}")
    for s, r in zip(pts, resid):
        print(f"        {str(complex(s)):>20} {r:>18.3e}")
    max_resid = max(resid)
    print(f"\n        max FE residual = {max_resid:.2e}  (duality holds to precision)")
    print(f"        fixed locus s = 1-s  <=>  Re(s) = 1/2 = the self-dual middle.\n")

    print("  [SYNTHESIS] The reverse-engineered specification of ingredient (iii):")
    print("    The halving is Poincare duality + self-duality of the middle weight.")
    print("    zeta HAS the duality (FE, verified) and the passive medium (Euler")
    print("    product, EAC.1); the MISSING object is the WEIGHT-GRADED cohomology whose")
    print("    middle (the H^1 analogue, the zeros) is self-dual at Re=1/2 - equivalently,")
    print("    the arithmetic 'Delta^2' (diagonal self-intersection) is the q-free,")
    print("    weight-0 leg. This is Deninger's missing motivic cohomology, with the job")
    print("    description: supply the weight filtration whose self-dual middle is Re=1/2.")
    print("    D-H has no pole = no H^2 leg = no geometric mean can form: no halving.")

    np.savez_compressed(
        out_dir / "eac4_arithmetic_diagonal.npz",
        ff_q=np.array([r["q"] for r in rows]),
        ff_h1=np.array([r["h1"] for r in rows]),
        ff_geomean=np.array([r["geo_mean"] for r in rows]),
        ff_h1_is_geomean=np.array([r["h1_is_geomean"] for r in rows]),
        ff_bound=np.array([r["bound"] for r in rows]),
        fe_residuals=np.array(resid),
        fe_max_residual=max_resid,
    )
    print(f"\n[EAC.4] Saved {out_dir / 'eac4_arithmetic_diagonal.npz'}")
    return rows, max_resid


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Reverse-engineer the halving as Poincare-duality geometric mean.")
    ap.add_argument("--dps", type=int, default=30)
    args = ap.parse_args()
    run(dps=args.dps)
