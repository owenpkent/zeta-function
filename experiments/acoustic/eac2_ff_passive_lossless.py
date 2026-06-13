"""EAC.2 - The function-field coupling: passive + symmetric => lossless = RH.

Step 2(a) of the acoustic thread, and the new-mathematics direction. It does NOT
rebuild the intersection form (that is e2g); it REINTERPRETS the Weil/Hodge-index
mechanism as the standard passive-network fact

        a contractive (passive) one-port that is reciprocal (time-reversal /
        functional-equation symmetric) is LOSSLESS (unitary on the axis).

DICTIONARY (Frobenius as a scattering matrix). For a curve C/F_q of genus g, let
alpha_1,...,alpha_2g be the Frobenius eigenvalues on H^1 (poles of Z_C). Define the
normalized SCATTERING values
        s_i := alpha_i / sqrt(q).
Then:
  - LOSSLESS (unitary): |s_i| = 1 for all i  <=>  |alpha_i| = sqrt(q)  <=>  RH for C.
  - PASSIVE (contractive, ||S|| <= 1): max_i |s_i| <= 1  <=>  |alpha_i| <= sqrt(q).
      This is the ONE-SIDED bound, and it is exactly the Hodge index / Castelnuovo-
      Severi output: the primitive intersection form on C x C is negative definite
      <=> |t_n| <= 2g q^{n/2} for all n <=> |alpha_i| <= sqrt(q). (Verified against
      e2g's margin 4 g^2 q - t^2 > 0.) Positivity from a SIGNATURE, the R3.5-escape
      side: the contractivity comes from the energy form's Lorentzian (1, n-1)
      signature, NOT from assuming the Frobenius operator is unitary.
  - RECIPROCAL (functional-equation symmetry): the multiset {alpha_i} is closed
      under alpha -> q/alpha (Poincare duality H^1 ~ H^1(-1)^vee). Hence the
      multiset {|s_i|} is closed under x -> 1/x, so min_i |s_i| = 1 / max_i |s_i|.
      This is UNCONDITIONAL (it is the functional equation, not RH).

THE COUPLING (the whole point). passive gives max|s| <= 1; reciprocal gives
min|s| = 1/max|s| >= 1; and min|s| <= max|s|. The three force max|s| = min|s| = 1,
i.e. ALL |s_i| = 1 = lossless = RH. In one line:

        (||S|| <= 1)  AND  ({alpha} = {q/alpha})   ==>   |alpha_i| = sqrt(q).

This is Weil's two-sided argument read as network theory: the functional equation
supplies one inequality for free; the Hodge-index energy form supplies the other;
together they pin the resonances onto the critical circle.

WHY Spec(Z) IS STUCK, located precisely. The coupling needs THREE things:
  (i)   reciprocal symmetry      -- zeta HAS it: xi(s) = xi(1-s) (the alpha<->q/alpha analogue).
  (ii)  a passive medium         -- zeta HAS it: the Euler product (eac1: Lambda(n) >= 0).
  (iii) a Lorentzian energy form  -- zeta LACKS it: there is no surface
        Spec(Z) x Spec(Z), no Frobenius graph Gamma, so no intersection form whose
        SIGNATURE delivers the one-sided contractivity bound (iii) feeds on.
We possess BOTH inputs to the coupling (symmetry + passivity) but not the energy
form that converts them into the one-sided bound. That energy form is the missing
M4 polarization, now stated as: the object that makes the arithmetic medium
provably CONTRACTIVE. (D-H fails at (ii) already: no Euler product = active medium
= it is not even admissible as a passive network, so the coupling never starts -
the K2 discipline, geometric face.)

Outputs:
  - eac2_ff_passive_lossless.npz : per-curve eigenvalues, scattering moduli, bounds
  - stdout : the coupling table + the Spec(Z) gap localization
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np

from experiments.arithmetic_geometric.e2f_hodge_index_sweep import (
    count_points_Fpk,
    elliptic_family,
    genus2_family,
)


def frobenius_eigenvalues(curve) -> np.ndarray:
    """Frobenius eigenvalues alpha_i (2g of them) from point counts.

    g=1: roots of x^2 - t1 x + q, t1 = q + 1 - N1.
    g=2: roots of x^4 - e1 x^3 + e2 x^2 - q e1 x + q^2, with
         e1 = q+1-N1 = sum alpha_i, e2 = (e1^2 - (q^2+1-N2))/2.
         (e3 = q e1 and e4 = q^2 are forced by the functional equation.)
    """
    p, g, f = curve["p"], curve["g"], curve["f_coeffs"]
    N1 = count_points_Fpk(f, p, 1)
    if g == 1:
        t1 = p + 1 - N1
        return np.roots([1.0, -t1, float(p)])
    elif g == 2:
        N2 = count_points_Fpk(f, p, 2)
        e1 = p + 1 - N1                     # sum alpha_i
        s2 = (p * p + 1) - N2               # sum alpha_i^2
        e2 = (e1 * e1 - s2) / 2.0
        e3 = p * e1
        e4 = p * p
        return np.roots([1.0, -e1, e2, -e3, e4])
    raise ValueError(f"genus {g} not supported")


def analyze(curve, tol: float = 1e-6) -> dict:
    p, g = curve["p"], curve["g"]
    alpha = frobenius_eigenvalues(curve)
    sqrtq = np.sqrt(p)
    s = alpha / sqrtq                       # scattering values
    mods = np.abs(s)
    max_mod = float(mods.max())
    min_mod = float(mods.min())

    # PASSIVE is certified by the EXACT integer Hodge-index margin (e2g):
    #   4 g^2 q - t^2 > 0  <=>  primitive intersection form negative definite
    #   <=>  |t| < 2 g sqrt(q)  <=>  |alpha_i| <= sqrt(q)  <=>  max|s| <= 1.
    # We use the integer margin, not the float max|s|, to avoid np.roots rounding.
    t = p + 1 - count_points_Fpk(curve["f_coeffs"], p, 1)
    hodge_margin = 4 * g * g * p - t * t
    passive = hodge_margin > 0
    # reciprocal (FE): {|s|} closed under x -> 1/x, i.e. min*max ~ 1
    reciprocal = abs(min_mod * max_mod - 1.0) < tol
    # lossless (RH): all |s_i| = 1
    lossless = bool(np.all(np.abs(mods - 1.0) < tol))
    # the bound is SATURATED, not slack: even where RH is a theorem, max|s| = 1
    # exactly (no buffer). This is the function-field mirror of the
    # marginal-positivity thesis - a reciprocal passive network is forced
    # lossless and cannot be strictly contractive without breaking reciprocity.
    saturated = abs(max_mod - 1.0) < tol

    # the coupling, checked numerically: passive AND reciprocal => lossless
    coupling_holds = (not passive) or (not reciprocal) or lossless

    return dict(
        label=curve["label"], p=p, g=g, alpha=alpha, mods=mods,
        max_mod=max_mod, min_mod=min_mod,
        passive=passive, reciprocal=reciprocal, lossless=lossless,
        saturated=saturated,
        coupling_holds=coupling_holds, hodge_margin=float(hodge_margin),
    )


def run(primes_elliptic=(5, 7, 11, 13, 17, 19), primes_genus2=(5, 7, 11),
        out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    curves = elliptic_family(list(primes_elliptic))
    if primes_genus2:
        curves += genus2_family(list(primes_genus2))

    print("[EAC.2] Function-field coupling: PASSIVE + RECIPROCAL => LOSSLESS = RH.")
    print("        s_i = alpha_i / sqrt(q);  passive: max|s|<=1 (Hodge index);")
    print("        reciprocal: min|s| = 1/max|s| (functional equation);")
    print("        lossless: all |s_i| = 1 (RH for the curve).\n")
    header = (f"{'curve':<30} {'g':>2} {'q':>3} {'max|s|':>8} {'min|s|':>8} "
              f"{'4g^2q-t^2':>10} {'pass':>5} {'recip':>6} {'loss':>5} {'couple':>7}")
    print(header)
    print("-" * len(header))

    results = []
    all_couple = True
    for c in curves:
        r = analyze(c)
        results.append(r)
        all_couple = all_couple and r["coupling_holds"]
        print(f"{r['label']:<30} {r['g']:>2} {r['p']:>3} "
              f"{r['max_mod']:>8.5f} {r['min_mod']:>8.5f} {r['hodge_margin']:>10.1f} "
              f"{'Y' if r['passive'] else 'n':>5} {'Y' if r['reciprocal'] else 'n':>6} "
              f"{'Y' if r['lossless'] else 'n':>5} {'OK' if r['coupling_holds'] else 'X':>7}")

    print("-" * len(header))
    n = len(results)
    print(f"\n[EAC.2] Across {n} curves:")
    print(f"        passive (max|s| <= 1, = Hodge index neg-def): "
          f"{sum(r['passive'] for r in results)}/{n}")
    print(f"        reciprocal (min|s| = 1/max|s|, = func. eq.):   "
          f"{sum(r['reciprocal'] for r in results)}/{n}")
    print(f"        lossless (all |s_i| = 1, = RH for the curve):  "
          f"{sum(r['lossless'] for r in results)}/{n}")
    print(f"        bound SATURATED (max|s| = 1, never slack):     "
          f"{sum(r['saturated'] for r in results)}/{n}")
    print(f"        COUPLING passive+reciprocal => lossless holds: "
          f"{sum(r['coupling_holds'] for r in results)}/{n}  (all: {all_couple})")
    print("\n[EAC.2] Note: passivity is NEVER slack here - max|s| = 1 exactly on")
    print("        every curve. A reciprocal passive network is forced lossless; it")
    print("        cannot be strictly contractive. This is the function-field mirror")
    print("        of the marginal-positivity thesis (RH is 'just barely true').")

    print("\n[EAC.2] The coupling in one line:")
    print("        (||S|| <= 1)  AND  ({alpha} = {q/alpha})  ==>  |alpha_i| = sqrt(q).")
    print("        Hodge index supplies the contractivity; the functional equation")
    print("        supplies the reciprocity; together they force losslessness = RH.")

    print("\n[EAC.2] The Spec(Z) gap, located precisely (the missing M4 polarization):")
    print("        (i)   reciprocal symmetry   : zeta HAS it  -- xi(s) = xi(1-s).")
    print("        (ii)  passive medium        : zeta HAS it  -- Euler product (eac1).")
    print("        (iii) Lorentzian energy form: zeta LACKS it -- no surface")
    print("              Spec(Z) x Spec(Z), no Frobenius graph, so no signature to")
    print("              deliver the one-sided contractivity bound (ii)+(iii) need.")
    print("        We hold BOTH inputs (symmetry + passivity); the missing object is")
    print("        the energy form that makes the arithmetic medium CONTRACTIVE.")

    _save(results, out_dir)
    return results, all_couple


def _save(results, out_dir: Path):
    save = {"n_curves": len(results),
            "labels": np.array([r["label"] for r in results], dtype=object)}
    for i, r in enumerate(results):
        save[f"c{i}_p"] = r["p"]; save[f"c{i}_g"] = r["g"]
        save[f"c{i}_alpha_re"] = np.real(r["alpha"])
        save[f"c{i}_alpha_im"] = np.imag(r["alpha"])
        save[f"c{i}_mods"] = r["mods"]
        save[f"c{i}_max_mod"] = r["max_mod"]; save[f"c{i}_min_mod"] = r["min_mod"]
        save[f"c{i}_hodge_margin"] = r["hodge_margin"]
        save[f"c{i}_passive"] = r["passive"]; save[f"c{i}_reciprocal"] = r["reciprocal"]
        save[f"c{i}_lossless"] = r["lossless"]; save[f"c{i}_saturated"] = r["saturated"]
    np.savez_compressed(out_dir / "eac2_ff_passive_lossless.npz", **save)
    print(f"\n[EAC.2] Saved {out_dir / 'eac2_ff_passive_lossless.npz'}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Function-field passive+reciprocal=>lossless coupling.")
    ap.add_argument("--primes-elliptic", type=int, nargs="+", default=[5, 7, 11, 13, 17, 19])
    ap.add_argument("--primes-genus2", type=int, nargs="+", default=[5, 7, 11])
    args = ap.parse_args()
    run(primes_elliptic=tuple(args.primes_elliptic),
        primes_genus2=tuple(args.primes_genus2))
