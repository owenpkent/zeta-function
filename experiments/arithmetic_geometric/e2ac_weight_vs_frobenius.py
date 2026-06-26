"""Chasing the H^1 (the follow-up to #124): where does the odd cohomology with a sqrt q-Frobenius
come from over Spec(Z)? Audit the prismatic/Sen/Deninger ODD operators against the e2xx moment
requirement. The finding CONVERGES #124 (the matroid is Tate, no H^1) with #44 (the prismatic
F, Theta are LINES, the zeros in neither): both candidates carry the WEIGHT operator (real-line
spectrum), not the FROBENIUS (circle, |alpha|=sqrt q). e2xx's moment lens IS the circle-vs-line
discriminator. A convergence/synthesis, not a new theorem; M3/#25 unchanged.

THE QUESTION (from #124)
------------------------
#124 (e2yy) showed a matroid Chow ring is purely EVEN/Tate and has no H^1 where the modulus-sqrt q
Frobenius eigenvalues live; "P3 = supply the H^1 the Tate ring lacks." The natural next question
(the user's pick): the prismatic / Sen / Deninger world is the standard home for ODD cohomology
over Spec(Z) -- does IT supply the H^1 with a sqrt q-Frobenius whose moment matrix (e2xx) is RH?

THE DISCRIMINATOR (e2xx's moment lens: CIRCLE vs LINE)
-----------------------------------------------------
e2xx (#123): RH-for-the-curve = positivity of the trigonometric MOMENT matrix of the Frobenius
spectrum, which requires that spectrum to lie on a CIRCLE |alpha| = sqrt q (pure weight 1, the
functional-equation pairing alpha <-> q/alpha). A FROBENIUS on pure weight w has |eig| = q^{w/2}
(a circle). A WEIGHT / GRADING operator (the degree, the Hodge-Tate grading) has REAL, integer
spectrum (a LINE). The moment matrix of a circle spectrum is PSD (RH); the moment matrix of a real
off-circle spectrum is INDEFINITE. So:

    CIRCLE spectrum  =  Frobenius  =  the SIGNATURE  =  the moment-positivity object  =  RH
    LINE   spectrum  =  weight/grading or orbit-length  =  the TRACE  =  realization

THE AUDIT (the Spec(Z) odd operators are WEIGHT operators, not Frobenius spectra)
--------------------------------------------------------------------------------
  * Matroid grading (the Lefschetz sl_2 Cartan H, #124/AHK): spectrum = the DEGREES {0,1,..,r}.
  * Prismatic SEN operator Theta (Bhatt-Lurie, #44): spectrum = the Hodge-Tate weights {-n}.
  * Prismatic FROBENIUS F / Deninger flow (#26/#44): spectrum = {log p} (orbit lengths / trace).

These are WEIGHTS and ORBIT-LENGTHS (real exponents), NOT q-symmetric Frobenius eigenvalues: they
are not closed under the functional-equation involution alpha <-> q/alpha, and the grading spectra
even contain 0. So they CANNOT enter the circle-Frobenius moment object at all -- a category
mismatch (the code itself errors if you try, because of the 0). The matroid grading and the Sen
Theta are the SAME KIND of object -- a real-line WEIGHT operator -- but (ADVERSARY correction) #124
and #44 are UNEQUAL POSITIONS on the all-roads map: the matroid (#124) has no H^1 and does NOT even
realize zeta as a trace; the prismatic candidate (#44) DOES realize zeta (both F and Theta halves)
and lacks ONLY the signature -- the live M4 target. Do not flatten them into "one finding." The
non-trivial zeros (the circle Frobenius on the global H^1) are the SIGNATURE of how F and Theta
combine, which the prismatic candidate does not carry (#44), in the analytic continuation invisible
to the local line data (#42). e2xx's moment lens is what names "circle": Toeplitz positivity
requires |alpha| = sqrt q.

WHAT THIS FILE DOES (and does NOT)
----------------------------------
Illustrates the #119 circle-vs-line discriminator (on-circle Frobenius PSD, off-circle indefinite),
shows the three Spec(Z) odd operators are WEIGHT/orbit operators that cannot even be a Frobenius
spectrum (the category mismatch), and states the corrected convergence: chasing the H^1 the Tate
lattice lacks lands on the prismatic candidate's MISSING SIGNATURE = the circle-Frobenius moment
positivity = the LIVE M4 target, viewed from the odd-cohomology side. It is a SYNTHESIS of #123 +
#124 + #44 + #42 + #119 + #30, NOT a new theorem; the circle Frobenius on the Spec(Z) H^1 is M3/#25,
untouched. The one (small) organizing increment is the circle-vs-line moment vocabulary applied to
the odd operators; the rest is restatement, and the H^1 chase confirms the live M4 target rather
than finding a new place.

Run:
  python -m experiments.arithmetic_geometric.e2ac_weight_vs_frobenius
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np

from experiments.arithmetic_geometric.e2xx_higher_rank_rosati import moment_sequence, toeplitz_moment


def _moment_matrix_of_spectrum(us, m: int) -> np.ndarray:
    """The e2xx moment matrix of a Frobenius 'spectrum' {u_i} (each paired with 1/u_i, the
    functional-equation involution). For |u_i|=1 (a circle) it is the RH-PSD object; for real
    u_i off the circle (a still-q-symmetric but RH-violating Frobenius) it is indefinite."""
    c = moment_sequence(us, m + 1)
    return toeplitz_moment(c, m)


def signature(M: np.ndarray, tol: float = 1e-7) -> tuple:
    ev = np.linalg.eigvalsh(0.5 * (M + M.T))
    scale = max(1.0, float(np.max(np.abs(ev))))
    return (int(np.sum(ev > tol * scale)), int(np.sum(ev < -tol * scale)))


# ===========================================================================
# Part 1: the discriminator -- on-circle Frobenius PSD, off-circle Frobenius indefinite (#119).
# ===========================================================================
def part1_circle_vs_offcircle() -> dict:
    """Among q-symmetric FROBENIUS spectra (closed under u <-> 1/u), on-circle (RH) is PSD and
    off-circle (RH-violated) is indefinite. This is the #119 discriminator (an off-circle Frobenius
    fails RH), illustrated via the e2xx moment matrix; it is NOT new -- e2xx already states it."""
    m = 3
    circle = [complex(math.cos(0.5), math.sin(0.5)), complex(math.cos(2.0), math.sin(2.0))]  # |u|=1
    off = [1.9, 2.6]                                   # real, |u|>1 -> a q-symmetric off-circle Frobenius
    sig_c, sig_o = signature(_moment_matrix_of_spectrum(circle, m)), signature(_moment_matrix_of_spectrum(off, m))
    return {"circle_signature": sig_c, "circle_psd": sig_c[1] == 0,
            "offcircle_signature": sig_o, "offcircle_indefinite": sig_o[1] > 0,
            "note": "an off-circle FROBENIUS (q-symmetric, real |u|>1) is indefinite = #119; a "
                    "near-circle pair can pass at small m (e2xx's marginal-positivity caveat)."}


# ===========================================================================
# Part 2: the Spec(Z) odd operators are WEIGHT operators -- they CANNOT even be a Frobenius
# spectrum (not q-symmetric, contain 0): a category mismatch the code itself proves.
# ===========================================================================
def part2_weight_operators_are_not_frobenius(r: int = 4, N: int = 6, n_primes: int = 6) -> dict:
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23][:n_primes]
    operators = {
        "matroid grading (Lefschetz Cartan, #124)": [float(k) for k in range(r + 1)],     # degrees {0..r}
        "prismatic Sen Theta (#44)": [float(-n) for n in range(N + 1)],                    # Hodge-Tate {-n}
        "prismatic Frobenius F / flow (#26/#44)": [math.log(p) for p in primes],           # {log p}
    }
    rows = []
    for name, spec in operators.items():
        on_circle = all(abs(abs(x) - 1.0) < 1e-9 for x in spec)
        contains_zero = any(abs(x) < 1e-12 for x in spec)
        # a Frobenius spectrum is closed under the FE involution alpha <-> q/alpha (q=1 normalized:
        # u <-> 1/u); a weight/grading/orbit spectrum is NOT (it is a real arithmetic progression
        # or a set of orbit lengths), and CANNOT be inverted where it contains 0.
        q_symmetric = (not contains_zero) and all(
            any(abs(x * y - 1.0) < 1e-9 for y in spec) for x in spec)
        rows.append({"operator": name, "spectrum_sample": [round(x, 4) for x in spec[:5]],
                     "on_circle": on_circle, "contains_zero": contains_zero,
                     "q_symmetric_frobenius_spectrum": q_symmetric,
                     "can_enter_moment_object": (not contains_zero) and q_symmetric})
    return {"rows": rows,
            "none_is_a_frobenius_spectrum": all(not r_["can_enter_moment_object"] for r_ in rows),
            "category_mismatch": "weights/orbit-lengths are exponents, not q-symmetric eigenvalues; "
                                 "they cannot enter the circle-Frobenius moment object at all (the "
                                 "grading spectra even contain 0). This IS the category mismatch."}


# ===========================================================================
# Part 3: the convergence -- CORRECTED (adversary): same KIND of weight operator, but the
# combinatorial and prismatic candidates are UNEQUAL positions on the all-roads map.
# ===========================================================================
def part3_convergence() -> dict:
    return {
        "matroid_124": "Tate/even, graded by a WEIGHT operator (Lefschetz Cartan, real degrees); "
                       "has NO H^1 and does not even realize zeta as a trace -- the LESS advanced position.",
        "prismatic_44": "carries Theta (weight {-n}) and F ({log p}), and DOES realize zeta as a "
                        "trace (both halves, #44); it lacks ONLY the signature -- the LIVE M4 target.",
        "same_kind_not_same_position": "the matroid grading and Sen Theta are the SAME KIND of object "
                                       "(a real-line weight operator), but #124 and #44 are UNEQUAL "
                                       "positions: do NOT flatten them into 'one finding'. The "
                                       "prismatic candidate has the realization; the matroid lacks it.",
        "where_the_H1_chase_lands": "chasing the H^1 the Tate lattice lacks leads to the prismatic "
                                    "candidate, which has the odd operators and the realization but "
                                    "NOT the circle Frobenius's MOMENT positivity = the signature = M4. "
                                    "So the H^1-with-circle-Frobenius is not a new place; it is the "
                                    "live M4 signature gap, viewed from the odd-cohomology side.",
        "moment_lens": "e2xx's Toeplitz positivity NAMES 'circle' (|alpha|=sqrt q) = the circle-vs-"
                       "line discriminator (#119) at the operator-spectrum level; this is the one "
                       "(small) organizing increment, the rest is #44 + #119 + #42 + #30 restated.",
    }


def demo() -> int:
    print("=" * 92)
    print("e2ac: chasing the H^1 -- the Spec(Z) odd operators are WEIGHT lines, not the Frobenius")
    print("circle; #124 (matroid Tate) and #44 (prismatic F,Theta lines) converge on the same gap")
    print("=" * 92)

    print("\n[1] The discriminator (#119, illustrated): among q-symmetric FROBENIUS spectra,")
    print("    on-circle is PSD (RH), off-circle is indefinite (not new -- e2xx states it):")
    p1 = part1_circle_vs_offcircle()
    print(f"    on-circle (|u|=1): moment signature {p1['circle_signature']}  PSD={p1['circle_psd']}")
    print(f"    off-circle Frobenius (real |u|>1): signature {p1['offcircle_signature']}  "
          f"indefinite={p1['offcircle_indefinite']}")
    print(f"    note: {p1['note']}")

    print("\n[2] The Spec(Z) odd operators are WEIGHT operators -- they CANNOT even be a Frobenius")
    print("    spectrum (not q-symmetric; the grading spectra contain 0): the category mismatch:")
    p2 = part2_weight_operators_are_not_frobenius()
    for r in p2["rows"]:
        print(f"    {r['operator']:42}: ~{r['spectrum_sample']}  contains-0={r['contains_zero']}  "
              f"q-symmetric-Frobenius={r['q_symmetric_frobenius_spectrum']}  "
              f"can-enter-moment-object={r['can_enter_moment_object']}")
    print(f"    => none is a Frobenius spectrum ({p2['none_is_a_frobenius_spectrum']}); "
          f"{p2['category_mismatch']}")

    print("\n[3] The convergence (CORRECTED -- adversary): same KIND of weight operator, but #124")
    print("    and #44 are UNEQUAL positions (do not flatten them):")
    p3 = part3_convergence()
    print(f"    #124 (matroid):   {p3['matroid_124']}")
    print(f"    #44  (prismatic): {p3['prismatic_44']}")
    print(f"    same KIND, not same position: {p3['same_kind_not_same_position']}")
    print(f"    where the H^1 chase lands: {p3['where_the_H1_chase_lands']}")
    print(f"    the one organizing increment: {p3['moment_lens']}")

    print("\n" + "=" * 92)
    print("VERDICT (a synthesis, honestly scoped -- adversary-corrected):")
    print("  - e2xx's moment positivity requires a CIRCLE spectrum (|alpha|=sqrt q, pure weight 1)")
    print("    = the Frobenius = the signature (#119). The Spec(Z) odd operators -- the matroid")
    print("    grading (Lefschetz Cartan), the Sen Theta {-n}, the Frobenius F/flow {log p} -- are")
    print("    WEIGHT/orbit operators (real lines), NOT q-symmetric Frobenius spectra: they cannot")
    print("    even enter the circle-Frobenius moment object (a category mismatch the code proves).")
    print("  - The matroid grading and Sen Theta are the SAME KIND (a weight operator), but #124")
    print("    (matroid: no H^1, no realization) and #44 (prismatic: realizes zeta, lacks only the")
    print("    signature = the LIVE M4 target) are UNEQUAL positions -- do not flatten them.")
    print("  - Chasing the H^1 lands on the prismatic candidate's MISSING SIGNATURE = the circle")
    print("    Frobenius's moment positivity = M4, viewed from the odd-cohomology side. Not a new")
    print("    place; the live M4 gap. UNTOUCHED.")
    print("  - Net: mostly #44 + #119 + #42 + #30 restated; the one small increment is the circle-")
    print("    vs-line moment vocabulary applied to the odd operators. NOT a new theorem.")
    print("=" * 92)

    # ---- structural assertions ----
    assert p1["circle_psd"] and p1["offcircle_indefinite"], \
        "Part 1: on-circle Frobenius must be PSD, off-circle indefinite (#119)"
    assert p2["none_is_a_frobenius_spectrum"], \
        "Part 2: no weight/orbit operator can be a q-symmetric Frobenius spectrum (category mismatch)"
    print("\n(all structural assertions hold)")

    out = Path(__file__).resolve().parent / "e2ac_weight_vs_frobenius.npz"
    np.savez_compressed(out, circle_signature=np.array(p1["circle_signature"]),
                        offcircle_signature=np.array(p1["offcircle_signature"]),
                        none_is_frobenius=p2["none_is_a_frobenius_spectrum"])
    print(f"\nSaved {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(demo())
