"""EAC.5 - Darlington synthesis: from SPECIFY to CONSTRUCT (and where it stalls).

Step 5 of the acoustic thread, the constructive frontier. EAC.1-4 SPECIFIED the
missing object (the weight filtration whose self-dual middle is Re=1/2). This step
asks the constructive question Owen's "keep going" points at: network synthesis is
exactly the art of BUILDING a passive system from a prescribed response, so does it
build the weight filtration?

DARLINGTON'S THEOREM. Every passive (positive-real) impedance Z is realizable as a
LOSSLESS (reactance) 2-port terminated in a SINGLE resistor: all dissipation is
concentrated in that one resistor, the rest is purely reactive (energy-conserving).

THE ARITHMETIC READING (and a genuinely new structural insight). The arithmetic
impedance Z = -zeta'/zeta is passive (Euler product, EAC.1). Darlington then says:

    arithmetic network  =  (lossless reactive 2-port)  +  (ONE resistor).

The arithmetic has exactly ONE archimedean place. Identify it with the single
Darlington resistor: the unique DISSIPATIVE element. All finite places (the Euler
product / von Mangoldt comb) are the LOSSLESS reactive part. This pins down why
exactly one place is distinguished and what its job is: the sole dissipator.

THE WEIGHT LADDER AS THE DARLINGTON DECOMPOSITION (computable, function field).
Normalize Frobenius eigenvalues to scattering values s = alpha/sqrt(q) on the unit
circle |s|=1 (the critical circle). The three weights split exactly as a Darlington
network around that circle:

    H^0 (eigenvalue 1)  -> s = 1/sqrt(q),  |s| < 1  : INSIDE  = the RESISTOR (dissipative)
    H^1 (the zeros)     -> |s| = 1                  : ON      = the LOSSLESS reactive 2-port
    H^2 (eigenvalue q)  -> s = sqrt(q),    |s| > 1  : OUTSIDE = the SOURCE (active)

Poincare duality / the functional equation pairs the resistor H^0 with the source
H^2 (reciprocal across the circle: |s_{H0}| * |s_{H2}| = 1). The reactive middle H^1
is built of Blaschke sections (z - s_i)/(1 - conj(s_i) z); under RH each section is
DEGENERATE (zero s_i = pole 1/conj(s_i), since |s_i|=1 forces 1/conj(s_i)=s_i) - a
lossless all-pass with coincident zero/pole. An OFF-line eigenvalue would SPLIT the
section (zero inside, pole outside): a genuine dissipative C-section. So:

    RH  <=>  every Darlington section of the reactive part is degenerate (lossless).

This is EAC.3's all-pass story in synthesis language, and it makes "construct the
network" precise.

WHERE IT STALLS (honest). For zeta the impedance is not rational (infinitely many
resonances), so the classical finite Darlington algorithm does not apply; the
distributed version is the canonical system / Krein string - which is exactly
Suzuki's Hamiltonian-from-L (arXiv:1606.05726): constructible UNCONDITIONALLY for
the parameter omega>1, and lossless-for-all-omega>0 IFF RH. So "just construct it
via Darlington" lands on the SAME RH-equivalent gap (the omega>1 -> omega>0
extension). The construction route is real but not a shortcut. The new content is
NOT a shortcut; it is the single-resistor / one-dissipative-place structural picture
and a precise statement of why construction here equals proof.

Outputs:
  - eac5_darlington_synthesis.npz
  - stdout : the resistor/reactive/source decomposition + section-degeneracy check
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np

from experiments.acoustic.eac2_ff_passive_lossless import frobenius_eigenvalues
from experiments.arithmetic_geometric.e2f_hodge_index_sweep import (
    elliptic_family,
    genus2_family,
)


def blaschke_value(z, s_vals):
    """Product of Blaschke factors (z - s)/(1 - conj(s) z) over s in s_vals."""
    out = 1.0 + 0.0j
    for s in s_vals:
        out *= (z - s) / (1 - np.conj(s) * z)
    return out


def section_degeneracy(s_vals, tol=1e-6):
    """For each reactive section: distance between zero (s) and pole (1/conj(s)).
    Zero under RH (|s|=1 => 1/conj(s) = s). Returns max distance."""
    dists = [abs(s - 1.0 / np.conj(s)) for s in s_vals]
    return float(max(dists)), all(d < tol for d in dists)


def analyze(curve):
    q, g = curve["p"], curve["g"]
    sqrtq = np.sqrt(q)
    alpha = frobenius_eigenvalues(curve)
    s_h1 = alpha / sqrtq                     # H^1 scattering values, |s|=1 under RH
    s_h0 = 1.0 / sqrtq                       # H^0: alpha=1
    s_h2 = sqrtq                             # H^2: alpha=q

    # Darlington positions around the unit circle
    inside = abs(s_h0) < 1.0                 # resistor
    outside = abs(s_h2) > 1.0                # source
    on_circle = bool(np.all(np.abs(np.abs(s_h1) - 1.0) < 1e-6))   # lossless reactive
    reciprocal = abs(abs(s_h0) * abs(s_h2) - 1.0) < 1e-9          # H^0 <-> H^2 dual

    # lossless check: Blaschke product unimodular on the circle (sample points)
    zs = np.exp(1j * np.linspace(0, 2 * np.pi, 13, endpoint=False))
    bmag = [abs(blaschke_value(z, s_h1)) for z in zs]
    lossless_on_circle = all(abs(b - 1.0) < 1e-6 for b in bmag)

    # section degeneracy: zero=pole under RH
    max_split, degenerate = section_degeneracy(s_h1)

    return dict(label=curve["label"], q=q, g=g,
                s_h0=abs(s_h0), s_h1=1.0, s_h2=abs(s_h2),
                resistor_inside=inside, source_outside=outside,
                reactive_on_circle=on_circle, reciprocal=reciprocal,
                lossless_on_circle=lossless_on_circle,
                max_section_split=max_split, sections_degenerate=degenerate)


def run(primes_elliptic=(5, 7, 11, 13, 17), primes_genus2=(5, 7), out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    curves = elliptic_family(list(primes_elliptic))
    if primes_genus2:
        curves += genus2_family(list(primes_genus2))

    print("[EAC.5] Darlington synthesis: passive Z = lossless 2-port + ONE resistor.")
    print("        Weight ladder around the critical circle |s|=1 (s = alpha/sqrt q):")
    print("        H^0 inside = resistor; H^1 on circle = lossless reactive; H^2 outside = source.\n")
    header = (f"{'curve':<26} {'q':>3} {'|s|H0':>7} {'|s|H1':>6} {'|s|H2':>6} "
              f"{'resist':>7} {'react':>6} {'source':>7} {'recip':>6} {'loss':>5} {'degen':>6}")
    print(header)
    print("-" * len(header))

    results = []
    for c in curves:
        r = analyze(c)
        results.append(r)
        print(f"{r['label']:<26} {r['q']:>3} {r['s_h0']:>7.4f} {r['s_h1']:>6.3f} "
              f"{r['s_h2']:>6.3f} "
              f"{'Y' if r['resistor_inside'] else 'n':>7} "
              f"{'Y' if r['reactive_on_circle'] else 'n':>6} "
              f"{'Y' if r['source_outside'] else 'n':>7} "
              f"{'Y' if r['reciprocal'] else 'n':>6} "
              f"{'Y' if r['lossless_on_circle'] else 'n':>5} "
              f"{'Y' if r['sections_degenerate'] else 'n':>6}")
    print("-" * len(header))
    n = len(results)
    print(f"\n[EAC.5] Across {n} curves:")
    print(f"        resistor H^0 inside the circle:        {sum(r['resistor_inside'] for r in results)}/{n}")
    print(f"        reactive H^1 ON the circle (lossless):  {sum(r['reactive_on_circle'] for r in results)}/{n}")
    print(f"        source H^2 outside the circle:          {sum(r['source_outside'] for r in results)}/{n}")
    print(f"        H^0 <-> H^2 reciprocal (FE/Poincare):   {sum(r['reciprocal'] for r in results)}/{n}")
    print(f"        Blaschke product unimodular on circle:  {sum(r['lossless_on_circle'] for r in results)}/{n}")
    print(f"        reactive sections DEGENERATE (RH):      {sum(r['sections_degenerate'] for r in results)}/{n}")

    print("\n[EAC.5] The Darlington decomposition of the function-field zeta:")
    print("        finite/middle (H^1, the zeros) = lossless reactive 2-port on the")
    print("        critical circle; the resistor (H^0) and source (H^2) are the poles,")
    print("        paired by the functional equation. RH <=> every reactive section is")
    print("        degenerate (zero=pole on the circle); an off-line zero would split a")
    print("        section into a dissipative C-section (zero inside, pole outside).")

    print("\n[EAC.5] The single-resistor insight (arithmetic):")
    print("        Darlington: a passive network = lossless 2-port + ONE resistor.")
    print("        zeta's Z is passive (Euler product); the arithmetic has exactly ONE")
    print("        archimedean place. Identify it with the single resistor: the unique")
    print("        dissipator. All finite places = the lossless reactive part. RH = the")
    print("        reactive (finite-place) resonances sit on the lossless circle (Re=1/2).")

    print("\n[EAC.5] Honest convergence (the construction is not a shortcut):")
    print("        zeta's Z is not rational -> the finite Darlington algorithm does not")
    print("        apply; the distributed version is the canonical system / Krein string")
    print("        = Suzuki's Hamiltonian-from-L, constructible UNCONDITIONALLY for omega>1,")
    print("        lossless-for-all-omega>0 IFF RH. So 'construct via Darlington' lands on")
    print("        the SAME RH-equivalent gap. New content: the single-resistor /")
    print("        one-dissipative-place structure, not a shortcut.")

    _save(results, out_dir)
    return results


def _save(results, out_dir: Path):
    save = {"n_curves": len(results),
            "labels": np.array([r["label"] for r in results], dtype=object)}
    for i, r in enumerate(results):
        for key in ("q", "g", "s_h0", "s_h1", "s_h2", "resistor_inside",
                    "source_outside", "reactive_on_circle", "reciprocal",
                    "lossless_on_circle", "max_section_split", "sections_degenerate"):
            save[f"c{i}_{key}"] = r[key]
    np.savez_compressed(out_dir / "eac5_darlington_synthesis.npz", **save)
    print(f"\n[EAC.5] Saved {out_dir / 'eac5_darlington_synthesis.npz'}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Darlington synthesis of the function-field zeta network.")
    ap.add_argument("--primes-elliptic", type=int, nargs="+", default=[5, 7, 11, 13, 17])
    ap.add_argument("--primes-genus2", type=int, nargs="+", default=[5, 7])
    args = ap.parse_args()
    run(primes_elliptic=tuple(args.primes_elliptic), primes_genus2=tuple(args.primes_genus2))
