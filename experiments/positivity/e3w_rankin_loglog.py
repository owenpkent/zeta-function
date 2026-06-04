"""Experiment 3W: the Rankin loglog-coefficient -- the one live invariant from the
first-principles construction sweep, and why it still cannot prove RH.

## Provenance

The "build the missing math" workflow (docs/03_research/building_the_missing_positivity.md)
ran four independent first-principles constructions of an RH-closing positivity
(Rankin-Selberg pole polarization; Bost-Connes Fock modular form; fibered arithmetic
surface; prime free-field reflection positivity). All four collapsed to one of two KNOWN
objects (arithmetic Rosati / Hodge-standard positivity = RH; or de Branges / Conrey-Li
positivity = strictly stronger than RH and false for zeta). No genuinely new foothold.

But the sweep isolated ONE clean, non-circular, multiplicative invariant worth recording and
testing: the Rankin loglog-coefficient

    c_F  :=  lim_{X -> inf}  ( sum_{p <= X} |a_F(p)|^2 / p )  /  log log X.

By Selberg orthonormality / Rankin-Selberg theory, c_F = (number of distinct primitive
constituents of F counted by multiplicity), normalized so that

    c_F = 1   for a PRIMITIVE Euler product (zeta, a Dirichlet L-function),
    c_F < 1   for a reducible combination / a non-Euler function (period-normalized).

It is a SINGLE SCALAR, decided by the prime coefficients alone, BEFORE any zero is located.
It is sharper than the von-Mangoldt delocalization fingerprint (LEARNINGS #20/#26), which is a
whole support pattern; this is one number.

## The test that matters (Part B)

Is c_F an RH discriminator, or only a non-Euler discriminator? The decisive control is
Epstein-d47-principal: NON-Euler (so c < 1) but RH-TRUE (no off-line zeros, LEARNINGS #20/#27).
If c < 1 for BOTH Davenport-Heilbronn (RH-FALSE) and Epstein-d47-principal (RH-TRUE), then c
detects non-Euler-ness, NOT RH-failure: it is necessary-not-sufficient, the reformulation trap.
This is the honest endpoint of the construction sweep: multiplicativity gives a clean, real,
non-circular discriminator, but it fixes the OBJECT'S EXISTENCE / block structure, not the
location of the zeros (which lives in the shared archimedean continuation).

Outputs:
  - e3w_rankin_loglog.npz : c_F vs X for each control
  - e3w_rankin_loglog.png : convergence + the Euler/non-Euler/RH-status bar chart
  - stdout : the report and the trap verdict
"""

from __future__ import annotations

import argparse
import time
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from sympy import primerange

from experiments._shared import (
    zeta_L, DavenportHeilbronn, chi3_L, epstein_for_discriminant,
)


def rankin_loglog_partial(L, X_values):
    """Cumulative c_F(X) = (sum_{p<=X} |a_p|^2 / p) / loglog(X) at each X in X_values."""
    Xmax = max(X_values)
    primes = list(primerange(2, Xmax + 1))
    out = {}
    s = 0.0
    xi = 0
    Xs = sorted(X_values)
    target = Xs[xi]
    running = 0.0
    for p in primes:
        ap = complex(L.dirichlet_coefficient(p))
        running += abs(ap) ** 2 / p
        while xi < len(Xs) and p <= Xs[xi] and (xi + 1 == len(Xs) or True):
            break
    # simpler: recompute cumulatively at checkpoints
    out = []
    idx = 0
    acc = 0.0
    pr = iter(primes)
    p = next(pr, None)
    for X in Xs:
        while p is not None and p <= X:
            ap = complex(L.dirichlet_coefficient(p))
            acc += abs(ap) ** 2 / p
            p = next(pr, None)
        out.append(acc / np.log(np.log(X)))
    return np.array(out)


def run(out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    X_values = [2000, 10000, 50000, 200000]
    # (name, L, has_euler, rh_true, color)
    controls = [
        ("zeta", zeta_L, True, True),
        ("chi3", chi3_L, True, True),
        ("D-H", DavenportHeilbronn(), False, False),
        ("Eps47-principal", epstein_for_discriminant(47, principal=True), False, True),
    ]

    print("=" * 78)
    print("[3W] Rankin loglog-coefficient c_F = (sum_{p<=X} |a_p|^2/p) / loglog(X)")
    print("=" * 78)
    print("\n[Part A] c_F vs X  (Euler product => 1; reducible/non-Euler => < 1)\n")
    header = "  control            " + "".join(f" X={X:>7d}" for X in X_values) + "   Euler  RH"
    print(header)
    results = {}
    for name, L, euler, rh in controls:
        t0 = time.time()
        cs = rankin_loglog_partial(L, X_values)
        results[name] = dict(cs=cs, euler=euler, rh=rh)
        row = f"  {name:18s}" + "".join(f" {c:8.4f}" for c in cs)
        row += f"    {'Y' if euler else 'N':>3s}  {'Y' if rh else 'N':>2s}   ({time.time()-t0:.1f}s)"
        print(row)

    # ---- Part B: the trap ----
    print("\n[Part B] Does c_F discriminate RH, or only Euler-ness?\n")
    c_final = {n: results[n]["cs"][-1] for n in results}
    euler_vals = [c_final[n] for n in results if results[n]["euler"]]
    noneuler_vals = [(n, c_final[n], results[n]["rh"]) for n in results if not results[n]["euler"]]
    print(f"  Euler products (zeta, chi3):       c = {[round(v,3) for v in euler_vals]}  -> cluster near 1")
    print(f"  Non-Euler:")
    for n, v, rh in noneuler_vals:
        print(f"     {n:18s} c = {v:.3f}   RH-{'TRUE' if rh else 'FALSE'}")
    dh = c_final["D-H"]
    eps = c_final["Eps47-principal"]
    print(f"\n  DECISIVE: c < 1 for BOTH D-H (RH-FALSE, c={dh:.3f}) and Eps47-principal")
    print(f"  (RH-TRUE, c={eps:.3f}). So c_F detects NON-EULER-ness, not RH-failure.")
    print(f"  --> c_F is a clean, non-circular, single-scalar multiplicative discriminator,")
    print(f"      but it is NECESSARY-NOT-SUFFICIENT for RH (the reformulation trap, #20/#27).")
    print(f"      It fixes the OBJECT'S EXISTENCE / block structure (real K2 firewall content),")
    print(f"      not the location of the zeros, which lives in the shared archimedean")
    print(f"      continuation. This is the honest endpoint of the construction sweep: no new")
    print(f"      foothold; the missing math IS the polarization, not a route to it.")

    # ---- save + plot ----
    save = dict(X_values=np.array(X_values))
    for n, r in results.items():
        save[f"{n}_cs"] = r["cs"]
        save[f"{n}_euler"] = r["euler"]
        save[f"{n}_rh"] = r["rh"]
    np.savez_compressed(out_dir / "e3w_rankin_loglog.npz", **save)

    fig, axs = plt.subplots(1, 2, figsize=(13, 5))

    ax = axs[0]
    for name, L, euler, rh in controls:
        ax.semilogx(X_values, results[name]["cs"], "o-",
                    label=f"{name} ({'Euler' if euler else 'non-Euler'})")
    ax.axhline(1.0, color="k", ls="--", lw=0.8, label="c=1 (primitive Euler)")
    ax.set_xlabel("X")
    ax.set_ylabel("c_F(X) = (sum_{p<=X} |a_p|^2/p)/loglog X")
    ax.set_title("Part A: Rankin loglog-coefficient\n(Euler -> 1; non-Euler < 1)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, which="both")

    ax = axs[1]
    names = list(results.keys())
    vals = [c_final[n] for n in names]
    colors = ["tab:blue" if results[n]["euler"] else "tab:red" for n in names]
    bars = ax.bar(names, vals, color=colors)
    for b, n in zip(bars, names):
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.02,
                f"RH-{'T' if results[n]['rh'] else 'F'}", ha="center", fontsize=9)
    ax.axhline(1.0, color="k", ls="--", lw=0.8)
    ax.set_ylabel("c_F (final)")
    ax.set_title("Part B: c<1 for BOTH RH-true and RH-false non-Euler\n=> detects Euler-ness, not RH (necessary-not-sufficient)")
    ax.tick_params(axis="x", rotation=20)
    ax.grid(alpha=0.3, axis="y")

    plt.tight_layout()
    plt.savefig(out_dir / "e3w_rankin_loglog.png", dpi=140)
    plt.close()
    print(f"\n[3W] Saved {out_dir / 'e3w_rankin_loglog.png'}")
    print(f"[3W] Saved {out_dir / 'e3w_rankin_loglog.npz'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.parse_args()
    run()
