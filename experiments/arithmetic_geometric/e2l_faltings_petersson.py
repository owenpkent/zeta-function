"""Experiment 2L: the archimedean self-intersection -- Petersson norm of the
discriminant and the Faltings height (the omega-bar^2 companion to 2I's lambda_inf).

The 2J numerical follow-up. 2J argued that the arithmetic adjunction
omega-bar^2 = 12 h_Fal is the analogue of the function-field Delta^2 = 2-2g, with
the archimedean piece the Petersson norm of the weight-12 discriminant modular form
||Delta||_Pet(tau) = (Im tau)^6 |Delta(tau)|. This computes it.

## Self-contained validation gates (no external lookup)

(a) tau is computed from the curve's period lattice via the AGM. GATE: the Klein
    j-invariant j(tau) (mpmath.kleinj) must equal the curve's own j-invariant
    j(E) = c4^3 / Delta, computed from the Weierstrass coefficients. This validates
    that tau is the correct period point.
(b) ||Delta||_Pet is a weight-0 (SL_2(Z)-invariant) function. GATE:
    ||Delta||_Pet(tau) = ||Delta||_Pet(tau+1) = ||Delta||_Pet(-1/tau) to high
    precision. This validates the Petersson-norm computation.

Only if BOTH gates pass is the result trusted (per the overnight protocol).

## What is reported

For each curve: tau, j(tau) vs j(E), ||Delta||_Pet(tau), and the stable Faltings
height in the normalization
    h_Fal(E) = (1/12) log|Delta_min| - (1/12) log||Delta||_Pet(tau) - log(2 pi),
i.e. omega-bar^2 / 12 with the archimedean (Petersson) piece made explicit. The
absolute normalization constant is convention-dependent (the 2I factor-of-2 lesson);
what is robustly validated here is tau (gate a) and the archimedean invariant
||Delta||_Pet (gate b). We additionally report h_Fal and flag it as
"normalization-dependent" unless an independent known value is supplied.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np

from experiments.arithmetic_geometric.e2i_archimedean_local_height import b_invariants
from experiments.arithmetic_geometric.e2h_arithmetic_hodge_index import CURVES


def c_invariants(a):
    b2, b4, b6, b8 = b_invariants(a)
    c4 = b2 * b2 - 24 * b4
    c6 = -b2 ** 3 + 36 * b2 * b4 - 216 * b6
    Delta = (c4 ** 3 - c6 ** 2)
    Delta = mp.mpf(Delta) / 1728
    return c4, c6, Delta


def period_tau(a, prec=50):
    """Period point tau of E (= lattice shape; depends only on j). Uses the model
    y^2 = x^3 - 27 c4 x - 54 c6 (scaling the curve does not change tau), finds the
    cubic roots, and forms tau via the AGM half-periods. Returns tau in the upper
    half plane."""
    mp.mp.dps = prec
    c4, c6, _ = c_invariants(a)
    A = mp.mpf(-27 * c4)
    B = mp.mpf(-54 * c6)
    # roots of x^3 + A x + B
    e = mp.polyroots([1, 0, A, B], maxsteps=200, extraprec=4 * prec)
    e1, e2, e3 = e[0], e[1], e[2]
    # AGM half-periods (complex AGM handles 1-real-root and 3-real-root cases):
    #   omega1 = pi / AGM(sqrt(e1-e3), sqrt(e1-e2))
    #   omega3 = i pi / AGM(sqrt(e1-e3), sqrt(e2-e3))
    # tau = omega3 / omega1. Root labelling fixes a representative; gate (a) checks it.
    def agm(x, y):
        return mp.agm(x, y)
    w1 = mp.pi / agm(mp.sqrt(e1 - e3), mp.sqrt(e1 - e2))
    w3 = (1j * mp.pi) / agm(mp.sqrt(e1 - e3), mp.sqrt(e2 - e3))
    tau = w3 / w1
    if mp.im(tau) < 0:
        tau = -tau
    # reduce into a sane strip for kleinj/eta convergence: tau -> tau mod 1, and
    # invert if |tau|<1 (one step of fundamental-domain reduction is enough for j check)
    tau = mp.mpc(mp.re(tau) - mp.floor(mp.re(tau) + mp.mpf("0.5")), mp.im(tau))
    return tau


def petersson_norm_disc(tau, prec=50):
    """||Delta||_Pet(tau) = (Im tau)^6 |Delta(tau)|, with the normalized weight-12
    cusp form Delta(tau) = eta(tau)^24 (we DROP the (2pi)^12 constant; it cancels in
    the SL2Z-invariance gate and is folded into the normalization elsewhere).
    eta(tau) = exp(pi i tau/12) prod_{n>=1} (1 - q^n), q = exp(2 pi i tau)."""
    mp.mp.dps = prec
    q = mp.e ** (2j * mp.pi * tau)
    # product prod (1-q^n)
    prod = mp.mpf(1)
    n = 1
    while True:
        term = 1 - q ** n
        prod *= term
        if abs(q ** n) < mp.mpf(10) ** (-(prec + 8)):
            break
        n += 1
        if n > 100000:
            break
    eta = mp.e ** (1j * mp.pi * tau / 12) * prod
    Delta = eta ** 24
    return (mp.im(tau)) ** 6 * abs(Delta)


def run(prec=50, out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)
    mp.mp.dps = prec

    print("[2L] Archimedean self-intersection: Petersson norm of the discriminant.")
    print("     Gates: (a) j(tau) == j(E) [validates tau]; (b) ||Delta||_Pet SL2Z-invariant.\n")

    results = []
    all_gate_a = True
    all_gate_b = True
    for curve in CURVES:
        a = tuple(int(c) for c in curve["a"])
        c4, c6, Delta = c_invariants(a)
        jE = mp.mpf(c4) ** 3 / Delta
        tau = period_tau(a, prec=prec)
        # mpmath.kleinj is the NORMALIZED Klein invariant J = j/1728 (J(i)=1), so the
        # standard j-invariant is 1728 * kleinj(tau). (Confirmed: the bare value was
        # off from j(E) by exactly 1728 across all curves -- gate (b) below shows tau
        # itself is correct via SL2Z-invariance; this is purely the kleinj convention.)
        jtau = 1728 * mp.kleinj(tau)
        gate_a_err = abs(jtau - jE) / max(abs(jE), 1)
        gate_a = gate_a_err < mp.mpf(10) ** (-6)

        pet = petersson_norm_disc(tau, prec=prec)
        pet_T = petersson_norm_disc(tau + 1, prec=prec)         # tau -> tau+1
        pet_S = petersson_norm_disc(-1 / tau, prec=prec)        # tau -> -1/tau
        gate_b_err = max(abs(pet - pet_T) / abs(pet), abs(pet - pet_S) / abs(pet))
        gate_b = gate_b_err < mp.mpf(10) ** (-8)

        # Faltings height (normalization-dependent; archimedean piece is -1/12 log||Delta||_Pet)
        # h_Fal = (1/12)( log|Delta_min| - log||Delta||_Pet ) - log(2 pi), with the
        # (2pi)^12 reinstated: ||Delta||_full = (2pi)^12 ||Delta||_Pet.
        Delta_min = abs(Delta)  # minimal model assumed for these LMFDB-minimal curves
        log_pet_full = mp.log(pet) + 12 * mp.log(2 * mp.pi)
        h_fal = (mp.log(Delta_min) - log_pet_full) / 12

        all_gate_a = all_gate_a and gate_a
        all_gate_b = all_gate_b and gate_b
        results.append(dict(label=curve["label"], tau=complex(tau),
                            jE=float(jE), jtau=complex(jtau).real,
                            gate_a=bool(gate_a), gate_a_err=float(gate_a_err),
                            pet=float(pet), gate_b=bool(gate_b), gate_b_err=float(gate_b_err),
                            h_fal=float(h_fal), Delta_min=float(Delta_min)))
        print(f"  --- {curve['label']} ---")
        print(f"      tau = {complex(tau):.6f}   Im tau = {float(mp.im(tau)):.6f}")
        print(f"      j(E)   = {float(jE):.6f}")
        print(f"      j(tau) = {float(mp.re(jtau)):.6f}   gate(a) |j(tau)-j(E)|/|j(E)| = {float(gate_a_err):.2e}  "
              f"{'PASS' if gate_a else 'FAIL'}")
        print(f"      ||Delta||_Pet(tau) = {float(pet):.6e}   SL2Z-invariance err = {float(gate_b_err):.2e}  "
              f"{'PASS' if gate_b else 'FAIL'}")
        print(f"      Delta_min = {float(Delta_min):.0f}   h_Fal (normalization-dependent) = {float(h_fal):.6f}")
        print()

    print(f"[2L] GATE (a) j(tau)==j(E) for ALL curves: {all_gate_a}")
    print(f"[2L] GATE (b) ||Delta||_Pet SL2Z-invariant for ALL curves: {all_gate_b}")
    gates_pass = all_gate_a and all_gate_b
    print(f"[2L] BOTH GATES PASS: {gates_pass}  -> {'commit' if gates_pass else 'BLOCK (write findings, do not commit)'}")

    _save_and_plot(results, out_dir)
    return results, gates_pass


def _save_and_plot(results, out_dir):
    save = {"n": len(results)}
    for i, r in enumerate(results):
        save[f"c{i}_tau"] = r["tau"]; save[f"c{i}_jE"] = r["jE"]
        save[f"c{i}_pet"] = r["pet"]; save[f"c{i}_h_fal"] = r["h_fal"]
        save[f"c{i}_gate_a"] = r["gate_a"]; save[f"c{i}_gate_b"] = r["gate_b"]
    np.savez_compressed(out_dir / "e2l_faltings_petersson.npz", **save)

    fig, ax = plt.subplots(1, 2, figsize=(12, 5))
    labels = [f"rank {i+1}" for i in range(len(results))]
    ax[0].bar(labels, [max(r["gate_a_err"], 1e-18) for r in results], color="tab:blue", label="gate (a) |j(tau)-j(E)|")
    ax[0].bar(labels, [max(r["gate_b_err"], 1e-18) for r in results], color="tab:orange", alpha=0.6, label="gate (b) SL2Z err")
    ax[0].set_yscale("log"); ax[0].axhline(1e-6, color="r", ls="--")
    ax[0].set_title("Validation gates (must be tiny)"); ax[0].legend(fontsize=8); ax[0].grid(alpha=0.3)
    ax[1].bar(labels, [r["h_fal"] for r in results], color="tab:green")
    ax[1].set_title("Faltings height (archimedean piece = -1/12 log||Delta||_Pet)\n[absolute normalization convention-dependent]")
    ax[1].grid(alpha=0.3, axis="y")
    plt.tight_layout()
    plt.savefig(out_dir / "e2l_faltings_petersson.png", dpi=140)
    plt.close()
    print(f"[2L] Saved {out_dir / 'e2l_faltings_petersson.png'} and .npz")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prec", type=int, default=50)
    args = parser.parse_args()
    run(prec=args.prec)
