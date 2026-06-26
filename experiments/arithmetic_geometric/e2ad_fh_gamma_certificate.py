"""The Arakelov face of M4 (the #125 follow-up, the user's pick): re-catalog the Faltings-Hriljac +
Gamma_S "global-assembly certificate" through the e2xx moment lens. ADVERSARY-CORRECTED
(scratchpad/higher_rank_faces/03_adversary_e2ad.md): the first pass's two cute identifications --
"FH = the (0,0) entry" and "Gamma_S assembles the FH height" -- are WITHDRAWN (a type mismatch and a
misattribution). What SURVIVES is one weak-form refinement of #125 plus a correct per-prime
computation; the rest is #25/#44/#125/#30 re-narrated in moment-Gram vocabulary. NOT a new theorem.

THE ONE SURVIVING REFINEMENT (of #125, weak form)
-------------------------------------------------
In the e2xx NORMALIZED moment matrix [c_{|j-k|}] (c_n = (q^n+1-#C(F_{q^n}))/q^{n/2}), the DIAGONAL
is the uniform NORM c_0 = 2g (UNCONDITIONAL) and the RH-detecting FLIP lives entirely in the
OFF-DIAGONAL Frobenius coupling c_1 = t/sqrt q (conditional). So:

  * the Faltings-Hriljac / Neron-Tate height pairing being UNCONDITIONALLY positive-definite (#22-24,
    #125) is "the right shape for a NORM / a diagonal", NOT a defect -- it is the arithmetic analogue
    of the unconditional NORM structure of the moment matrix (the PD part), NOT "the wrong shape".

CORRECTION (adversary): FH is the analogue of the WHOLE normalized PD moment matrix (an r x r
regulator), NOT a single entry. The first pass's "FH = Delta_0^2 = -2g" is a TYPE MISMATCH (one
number vs r x r; negative vs positive-definite; product-surface diagonal vs single-surface
regulator). And the un-normalized asymmetry Delta_0^2=-2g vs Gamma_0^2=-2gq is just the un-divided
q-scale (the (1,q) bidegree), NOT a height-vs-Frobenius decomposition; after normalization the
diagonal is uniformly 2g.

THE PER-PRIME FROBENIUS COUPLING (a correct, real computation)
-------------------------------------------------------------
The off-diagonal Frobenius coupling, over Spec(Z), is per-prime: a_p = p + 1 - #E(F_p), with the
Hasse bound |a_p| <= 2 sqrt p <=> a_p^2 - 4p < 0 (complex roots = the per-prime circle |alpha|=sqrt p,
the per-prime RH; a THEOREM of Hasse 1933 -- the SAME single fact, not two). Computed on the real
curve 389a1, every a_p is Hasse-bounded. The per-prime circle has radius sqrt p, a DIFFERENT scale
at every prime: the (1,p) place-dependent bidegree (#25).

Gamma_S, AND WHAT IT DOES NOT DO (the sharpest correction)
---------------------------------------------------------
The completed L-function Lambda(E,s) = N^{s/2}(2pi)^{-s}Gamma(s) L(E,s) joins the FINITE primes (the
Euler product, the per-prime a_p) with the ARCHIMEDEAN place (Gamma_S, the Gamma-factor) into one
analytic object. So Gamma_S assembles the FROBENIUS / off-diagonal data across scales -- the a_p and
the archimedean factor -- as a TRACE (the L-function / explicit-formula sum), not a SIGNED PAIRING.
It does NOT contain the Neron-Tate HEIGHT: the height-to-L link is BSD (the central value/derivative
at s=1, a CONJECTURE), not the functional-equation Gamma-factor. So "Gamma_S assembles the FH height"
is WITHDRAWN; Gamma_S assembles the Frobenius/finite+archimedean side only.

THE GAP (= #25, restated -- not a new localization)
---------------------------------------------------
Assembling the per-prime Frobenius couplings (scale sqrt p each) into ONE signed pairing at a single
compatible scale is the place-dependent (1,p) bidegree obstruction (#25), here re-narrated as "the
signed-pairing assembly across per-prime scales." It adds no localization beyond #25/#44. The
analytic join (Gamma_S / Lambda) exists; the SIGNED-PAIRING join (the Weil cohomology / the moment
positivity over Spec(Z)) is M4/#25, UNTOUCHED.

WHAT THIS FILE DOES (honestly): one correct per-prime computation (a_p for 389a1, Hasse-verified),
the weak-form #125 refinement (unconditional = norm/diagonal; the flip is off-diagonal), and the
scale-mismatch picture (#25). It is a RE-CATALOGING of #25/#44/#125/#30 in moment-Gram vocabulary,
with the two first-pass identifications withdrawn. NOT a new theorem; M4/#25 untouched.

Run:
  python -m experiments.arithmetic_geometric.e2ad_fh_gamma_certificate
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np


# 389a1: y^2 + y = x^3 + x^2 - 2x (conductor 389, RANK 2; Neron-Tate regulator ~ 0.1525 > 0, #22-24).
CURVE_389A1 = (0, 1, 1, -2, 0)


def count_points_Fp(p: int, coeffs) -> int:
    a1, a2, a3, a4, a6 = coeffs
    N = 1                                              # the point at infinity
    for x in range(p):
        rhs = (x ** 3 + a2 * x * x + a4 * x + a6) % p
        for y in range(p):
            if (y * y + a1 * x * y + a3 * y) % p == rhs:
                N += 1
    return N


def frobenius_traces(coeffs, primes) -> list:
    rows = []
    for p in primes:
        a = p + 1 - count_points_Fp(p, coeffs)
        rows.append({"p": p, "a_p": a, "hasse_complex": a * a - 4 * p < 0,   # |a|<=2sqrt p <=> a^2-4p<0
                     "scale_sqrt_p": round(math.sqrt(p), 4)})
    return rows


# ===========================================================================
# (1) The NORMALIZED moment matrix: uniform norm diagonal + conditional off-diagonal.
# ===========================================================================
def part1_normalized_moment() -> dict:
    """The e2xx NORMALIZED moment matrix [c_{|j-k|}], g=1: diagonal c_0 = 2g (UNIFORM NORM,
    unconditional) and off-diagonal c_1 = t/sqrt q (the FROBENIUS coupling, conditional -- it flips
    PSD->indefinite at |c_1| = 2g). The un-normalized [[-2g,-t],[-t,-2gq]] asymmetry is the q-scale,
    NOT a height/Frobenius split (adversary)."""
    g, q = 1.0, 25.0
    rows = []
    for t in (6.0, 9.0, 11.0):                          # |t|<2g sqrt q=10 (RH) then off
        c1 = t / math.sqrt(q)
        G = np.array([[2 * g, c1], [c1, 2 * g]])        # normalized: diagonal uniform 2g
        rows.append({"t": t, "c1": round(c1, 4), "psd": bool(np.all(np.linalg.eigvalsh(G) > -1e-12)),
                     "weil": t * t < 4 * g * g * q})
    return {"g": g, "q": q, "rows": rows,
            "diagonal_uniform_norm": "c_0 = 2g on BOTH diagonal slots (unconditional)",
            "flip_is_offdiagonal": "the RH-detecting flip is c_1 = t/sqrt q only (conditional)"}


# ===========================================================================
# (2) FH = the unconditional NORM / PD structure (a theorem; NOT a single entry).
# ===========================================================================
def part2_fh_is_the_norm() -> dict:
    """Faltings-Hriljac / Neron-Tate is UNCONDITIONALLY positive-definite (theorem, #22-24,
    validated ranks 1-4). It is the arithmetic analogue of the moment matrix's unconditional NORM
    (the PD part), NOT a single entry (type-corrected, adversary). No toy matrix: the PD-ness is the
    THEOREM; for 389a1 (rank 2) the Neron-Tate regulator ~ 0.1525 > 0 (a 2x2 PD Gram, #22-24/e2h)."""
    return {"fh_positive_definite": True, "is_unconditional": True,
            "analogue_of": "the WHOLE normalized PD moment structure (an r x r regulator), not the "
                           "single entry -2g (type mismatch withdrawn)",
            "refinement_of_125": "FH unconditionally PD = the right shape for a NORM/diagonal, not "
                                 "'the wrong shape'; the RH flip is the off-diagonal Frobenius coupling",
            "regulator_389a1": 0.1525, "rank": 2}


# ===========================================================================
# (3) The per-prime Frobenius coupling a_p (real curve) and the scale mismatch (#25).
# ===========================================================================
def part3_per_prime(coeffs, primes) -> dict:
    traces = frobenius_traces(coeffs, primes)
    scales = sorted({r["scale_sqrt_p"] for r in traces})
    return {"traces": traces, "all_hasse_complex": all(r["hasse_complex"] for r in traces),
            "num_distinct_scales": len(scales), "per_prime_scales": scales,
            "scale_mismatch": "the FH norm is GLOBAL (1 scale); the per-prime Frobenius couplings a_p "
                              f"live at {len(scales)} scales sqrt p (the (1,p) bidegree, #25). This is "
                              "#25 restated, not a new localization."}


# ===========================================================================
# (4) Gamma_S assembles the FROBENIUS side (a trace), NOT the height (adversary).
# ===========================================================================
def part4_gamma_s() -> dict:
    return {
        "joins": "Lambda(E,s) joins the FINITE primes (Euler product, the a_p) + the ARCHIMEDEAN "
                 "place (Gamma_S) into one analytic object -- a TRACE (the L-function).",
        "does_not_contain_height": "Lambda does NOT contain the Neron-Tate height; the height-to-L "
                                   "link is BSD (s=1, a conjecture), NOT the FE Gamma-factor. So "
                                   "'Gamma_S assembles the FH height' is WITHDRAWN.",
        "gap": "the SIGNED-PAIRING assembly of the per-prime Frobenius couplings at one scale = the "
               "Weil cohomology over Spec(Z) = M4/#25, untouched (a restatement of #25, not new).",
    }


def demo() -> int:
    print("=" * 94)
    print("e2ad: the Arakelov-face certificate, re-cataloged through the moment lens (adversary-corrected)")
    print("=" * 94)

    print("\n[1] The NORMALIZED moment matrix: uniform NORM diagonal + conditional off-diagonal flip:")
    p1 = part1_normalized_moment()
    for r in p1["rows"]:
        print(f"    t={r['t']:>4} (c_1={r['c1']}): normalized Gram PSD={r['psd']}  Weil={r['weil']}")
    print(f"    {p1['diagonal_uniform_norm']}; {p1['flip_is_offdiagonal']}")

    print("\n[2] FH = the unconditional NORM (PD, theorem #22-24) -- NOT a single entry (type-corrected):")
    p2 = part2_fh_is_the_norm()
    print(f"    FH positive-definite (unconditional): {p2['fh_positive_definite']}; 389a1 rank "
          f"{p2['rank']} regulator ~ {p2['regulator_389a1']} > 0")
    print(f"    analogue of: {p2['analogue_of']}")
    print(f"    refines #125: {p2['refinement_of_125']}")

    print("\n[3] The per-prime Frobenius couplings a_p (real curve 389a1) + the scale mismatch (#25):")
    p3 = part3_per_prime(CURVE_389A1, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])
    for r in p3["traces"][:6]:
        print(f"    p={r['p']:>2}: a_p={r['a_p']:>3}  Hasse(a_p^2-4p<0, on circle |alpha|=sqrt {r['p']}"
              f"={r['scale_sqrt_p']})={r['hasse_complex']}")
    print(f"    all Hasse-bounded (complex roots): {p3['all_hasse_complex']}; "
          f"{p3['num_distinct_scales']} distinct scales sqrt p. {p3['scale_mismatch']}")

    print("\n[4] Gamma_S joins the FROBENIUS side as a TRACE -- NOT the height (adversary correction):")
    p4 = part4_gamma_s()
    print(f"    {p4['joins']}")
    print(f"    {p4['does_not_contain_height']}")
    print(f"    GAP: {p4['gap']}")

    print("\n" + "=" * 94)
    print("VERDICT (honest -- a re-cataloging, two identifications withdrawn):")
    print("  - SURVIVES: (i) a_p for 389a1 is correct (Hasse-bounded, per-prime circle |alpha|=sqrt p);")
    print("    (ii) one weak-form refinement of #125 -- in the normalized moment matrix the diagonal")
    print("    is the UNCONDITIONAL norm and the RH flip is the OFF-DIAGONAL Frobenius coupling, so")
    print("    FH being unconditionally PD is the right shape for a NORM, not 'the wrong shape'.")
    print("  - WITHDRAWN: 'FH = the (0,0) entry -2g' (type mismatch: FH is an r x r PD regulator, the")
    print("    analogue of the WHOLE normalized PD matrix); 'Gamma_S assembles the FH height' (Lambda")
    print("    joins finite+archimedean = the Frobenius side, NOT the height; height->L is BSD at s=1).")
    print("  - The 'certificate' = #25's (1,p) bidegree restated in moment-Gram vocabulary; no new")
    print("    localization. NET: a re-cataloging of #25/#44/#125/#30, NOT a new theorem. M4/#25 UNTOUCHED.")
    print("=" * 94)

    # ---- structural assertions ----
    assert p1["rows"][0]["psd"] and not p1["rows"][2]["psd"], \
        "Part 1: the normalized moment Gram must be PSD on-line (t=6) and flip off-line (t=11)"
    assert p3["all_hasse_complex"] and p3["num_distinct_scales"] > 1, \
        "Part 3: all per-prime a_p Hasse-bounded (complex roots), at multiple scales (#25)"
    print("\n(all structural assertions hold)")

    out = Path(__file__).resolve().parent / "e2ad_fh_gamma_certificate.npz"
    np.savez_compressed(out, primes=np.array([r["p"] for r in p3["traces"]]),
                        a_p=np.array([r["a_p"] for r in p3["traces"]]),
                        per_prime_scales=np.array(p3["per_prime_scales"]))
    print(f"\nSaved {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(demo())
