"""Experiment 3Z: the multiplicativity obstruction -- D-H has no equilibrium product state.

## Why this experiment exists (overnight cycle C4)

The construction sweep's Mechanism 2 (docs/03_research/building_the_missing_positivity.md) argued,
but did not quantify, that the Bost-Connes equilibrium state factors over primes (a PURE PRODUCT
state) ONLY for a genuine Euler product, and that Davenport-Heilbronn -- a linear combination
c1 L(s,chi1) + c2 L(s,chi2) -- is a statistical MIXTURE c1 phi^(1) + c2 phi^(2), never a product
state. The obstruction is the pointwise multiplicativity defect of the Dirichlet coefficients. This
experiment makes it concrete and ties it to the project's D-H discipline.

It complements e3w (LEARNINGS #53): e3w measured non-Euler-ness analytically (the Rankin loglog-
coefficient, a density invariant); this measures it ALGEBRAICALLY (a_{mn} - a_m a_n on coprime
pairs) and gives the operator-algebra reading (no product state).

## The construction

An Euler product L(s) = prod_p L_p(s) is equivalent to MULTIPLICATIVITY of its Dirichlet
coefficients: a_{mn} = a_m a_n whenever gcd(m,n) = 1. In the Bost-Connes quantum statistical system
each prime is one bosonic mode, the partition function factors Z(beta) = prod_p Z_p(beta), and the
beta>1 equilibrium (KMS) state is the restricted tensor product phi_beta = (x)'_p rho_{beta,p} -- a
PURE PRODUCT STATE -- precisely because the coefficients multiply. For a sum of two distinct
primitive L-functions the only natural state is the convex combination of the two constituents'
product states, a MIXTURE, which is a product state iff the constituents coincide. So:

    multiplicativity defect = 0   <=>   Euler product   <=>   pure equilibrium product state exists.

## What it shows

  Part A. Multiplicativity defect d(L) = mean over coprime m,n (mn <= N) of |a_{mn} - a_m a_n|,
    normalized. zeta and chi3 (Euler products): d = 0 to machine precision. D-H and Epstein-d47-
    principal (non-Euler): d > 0.
  Part B. The Bost-Connes reading: D-H's coefficients are literally c1 a^(chi1) + c2 a^(chi2), and
    the defect equals the cross-term c1 c2 (a^(1)_{mn} - a^(1)_m a^(1)_n + ...) measuring how far the
    mixture is from a product state. Exhibited on small coprime pairs.
  Part C. The D-H discipline / the trap. The defect detects NON-EULER-ness, not RH-failure:
    Epstein-d47-principal is non-multiplicative (d > 0) but RH-TRUE. So, exactly like e3w, the
    Bost-Connes product-state obstruction is a clean, non-circular, D-H-discriminating K2 firewall
    but is NECESSARY-NOT-SUFFICIENT for RH. It sharpens the 2A_R1 D-H exclusion from "D-H is a linear
    combination" to "D-H provably has no equilibrium product state," without being a route to RH.

  CORRECTION (2026-09-04, LEARNINGS #217/#218). Part C's witness is retired: Epstein-d47-principal is
    RH-FALSE (seven off-line pairs below height 70, certified 2026-09-02 after the Chowla-Selberg tail
    repair), so "non-multiplicative but RH-TRUE" no longer holds for any Epstein form in the repo (by
    Voronin, no class-number >= 2 Epstein zeta is RH-true). The necessary-not-sufficient reading
    survives on a better witness (e3ac_entropic_exports): the Euler pencil f_lambda is non-
    multiplicative for every lambda != 0 while its lowest off-line height climbs without bound as
    lambda -> 0, and L(chi_-3)L(chi_5) is an Euler product (RH under GRH) whose Gibbs weights are
    SIGNED, so it is not a state at all. Part B's "statistical MIXTURE" needs the same sign caveat:
    D-H's weights c1 a^(1) + c2 a^(2) are signed, so D-H is not a state; Epstein IS a state and is a
    signed combination a_A +- a_B of two product functionals, one of which (a_B) is not a state.
    Separability is automatic for every diagonal state and carries no information; the entropy
    version of this defect (total correlation across prime modes) is measured in e3ac.

Outputs:
  - e3z_multiplicativity_obstruction.npz : defect per control, sample coprime-pair table
  - e3z_multiplicativity_obstruction.png : defect bar chart (Euler vs non-Euler, RH status)
  - stdout : the report
"""

from __future__ import annotations

import argparse
import time
from math import gcd
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from experiments._shared import (
    zeta_L, DavenportHeilbronn, chi3_L, epstein_for_discriminant,
)


def coeffs(L, N):
    a = np.zeros(N + 1)
    for n in range(1, N + 1):
        a[n] = complex(L.dirichlet_coefficient(n)).real
    return a


def multiplicativity_defect(a, N):
    """Mean |a_{mn} - a_m a_n| over coprime pairs (m,n), m,n>=2, mn<=N, normalized by the
    mean |a_m a_n| over the same pairs (scale-free). Returns (defect, n_pairs, sample)."""
    num = 0.0
    den = 0.0
    cnt = 0
    sample = []
    for m in range(2, N + 1):
        if abs(a[m]) < 1e-15 and m > 2:
            pass
        for n in range(m, N + 1):
            if m * n > N:
                break
            if gcd(m, n) != 1:
                continue
            lhs = a[m * n]
            rhs = a[m] * a[n]
            num += abs(lhs - rhs)
            den += abs(rhs)
            cnt += 1
            if len(sample) < 8 and m <= 5:
                sample.append((m, n, m * n, lhs, rhs, lhs - rhs))
    defect = num / den if den > 1e-15 else num / max(cnt, 1)
    return defect, cnt, sample


def run(N: int = 400, out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    controls = [
        ("zeta", zeta_L, True, True),
        ("chi3", chi3_L, True, True),
        ("D-H", DavenportHeilbronn(), False, False),
        ("Eps47-principal", epstein_for_discriminant(47, principal=True), False, True),
    ]

    print("=" * 78)
    print("[3Z] Multiplicativity obstruction: d(L) = mean |a_{mn} - a_m a_n| / mean|a_m a_n|")
    print("=" * 78)
    print(f"\n  coprime pairs with m,n >= 2, mn <= {N}\n")
    print("    control            defect d(L)    Euler   RH")
    results = {}
    for name, L, euler, rh in controls:
        t0 = time.time()
        a = coeffs(L, N)
        d, cnt, sample = multiplicativity_defect(a, N)
        results[name] = dict(d=d, euler=euler, rh=rh, sample=sample, cnt=cnt)
        print(f"  {name:18s} {d:11.3e}      {'Y' if euler else 'N':>3s}   {'Y' if rh else 'N':>2s}"
              f"   ({cnt} pairs, {time.time()-t0:.1f}s)")

    print("\n[Part B] Sample coprime pairs (a_{mn} vs a_m a_n):\n")
    for name in ("D-H", "Eps47-principal"):
        print(f"  {name}:")
        for (m, n, mn, lhs, rhs, diff) in results[name]["sample"]:
            print(f"     a_{m}*a_{n} = {rhs:+.4f}   a_{mn} = {lhs:+.4f}   defect {diff:+.4f}")

    print("\n[Part C] The trap (D-H discipline)\n")
    dz = results["zeta"]["d"]; dc = results["chi3"]["d"]
    dd = results["D-H"]["d"]; de = results["Eps47-principal"]["d"]
    print(f"  Euler products: zeta d={dz:.1e}, chi3 d={dc:.1e}  -> 0 (multiplicative, product state)")
    print(f"  Non-Euler:      D-H  d={dd:.3f} (RH-FALSE), Eps47-principal d={de:.3f} (RH-FALSE since #217; see docstring CORRECTION)")
    print(f"  --> d > 0 for both non-Euler controls (both RH-false since #217; the necessary-not-sufficient")
    print(f"      witness is now the Euler pencil, e3ac: non-multiplicative at every lambda != 0, T* unbounded),")
    print(f"      so the multiplicativity defect detects NON-EULER-ness (= no equilibrium product")
    print(f"      state), NOT RH-failure. It is the Bost-Connes form of the K2 firewall:")
    print(f"      non-circular, D-H-discriminating, but NECESSARY-NOT-SUFFICIENT for RH.")
    print(f"      Sharpens 2A_R1: D-H is not merely 'a linear combination' -- it provably has NO")
    print(f"      equilibrium product state (its weights c1 a^(1) + c2 a^(2) are signed: not a Gibbs state;")
    print(f"      see the docstring CORRECTION and e3ac).")

    np.savez_compressed(
        out_dir / "e3z_multiplicativity_obstruction.npz",
        N=N,
        names=np.array([c[0] for c in controls]),
        defects=np.array([results[c[0]]["d"] for c in controls]),
        euler=np.array([results[c[0]]["euler"] for c in controls]),
        rh=np.array([results[c[0]]["rh"] for c in controls]),
    )

    fig, ax = plt.subplots(figsize=(8, 5))
    names = [c[0] for c in controls]
    vals = [max(results[n]["d"], 1e-17) for n in names]
    colors = ["tab:blue" if results[n]["euler"] else "tab:red" for n in names]
    bars = ax.bar(names, vals, color=colors)
    for b, n in zip(bars, names):
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() * 1.3,
                f"RH-{'T' if results[n]['rh'] else 'F'}", ha="center", fontsize=9)
    ax.set_yscale("log")
    ax.set_ylabel("multiplicativity defect d(L)")
    ax.set_title("Euler products (blue) -> 0 (product state exists);\n"
                 "non-Euler (red) -> defect > 0 for BOTH RH-true and RH-false\n"
                 "(detects non-Euler-ness, not RH: necessary-not-sufficient)")
    ax.tick_params(axis="x", rotation=20)
    ax.grid(alpha=0.3, axis="y", which="both")
    plt.tight_layout()
    plt.savefig(out_dir / "e3z_multiplicativity_obstruction.png", dpi=140)
    plt.close()
    print(f"\n[3Z] Saved {out_dir / 'e3z_multiplicativity_obstruction.png'}")
    print(f"[3Z] Saved {out_dir / 'e3z_multiplicativity_obstruction.npz'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, default=400)
    args = parser.parse_args()
    run(N=args.N)
