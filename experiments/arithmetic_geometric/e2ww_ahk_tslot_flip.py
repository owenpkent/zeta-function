"""9A connection note (NOT an advance): re-derive e2uu's "the gap is P3" from the breadth
direction, and record the FAITHFULNESS CAVEAT the attempt surfaced. Adversary-corrected
(scratchpad/ahk_tslot/03_adversary.md): the distinctive first-pass claim ("M4 = one matrix
entry; four axes free, one arithmetic") was WRONG and is withdrawn. What survives is a
connection plus a caveat, both honest and both modest.

WHAT THIS IS (and is NOT)
-------------------------
- It IS: a check that the breadth program's M4-polarity FINGERPRINT (#120/#121), run on the
  function-field genus-1 primitive form, lands on the SAME single constructible gap e2uu/#105
  already found -- P3, the t-carrying degree map. The two independent directions converge.
- It is NOT an advance. P6 (the actual M4 positivity) is untouched, and -- the load-bearing
  caveat -- genus 1 is the EASIEST Weil case, so this shadow CANNOT localize the hard part of M4.

THE FORM (e2uu, NS(C x C), genus 1). The primitive intersection Gram on the 2-dim middle is
  Q(a,b,s) = [[-a,-s],[-s,-b]],   arithmetic specialization a = 2g, b = 2gq, s = t  (g=1).
It is negative-definite (the polarization P6) iff det > 0 iff s^2 < a*b, i.e. t^2 < 4 g^2 q =
the Weil bound. |t| > 2 sqrt(q) is an off-line zero (a Frobenius eigenvalue off the circle),
and the form FLIPS to indefinite -- the FF avatar of the off-line-flip test (offline_flip_test.py,
#96).

THE CONNECTION (re-derives P3, the e2uu gap). Running the breadth FINGERPRINT/battery() on this
form (imported below from breadth_corpus): it is the master transfer-candidate (Weil/Rosati),
hitting every fingerprint axis and surviving the battery. So the breadth program, pointed at the
construction, recovers exactly the object 09A targets. And the off-line flip is on the SIGN of
the form (not class-membership), so it passes the #121 selection-not-sign screen Bridgeland
failed. The constructible gap the spec leaves is P3: the bare combinatorial lattice (e2uu) gives
the 2x2 SHAPE for free but with the off-diagonal coupling s = 0 (t-blind); supplying the
arithmetic Gram (a,b,s) = (2g, 2gq, t) -- the JOINT datum, q in the diagonal AND t off-diagonal,
both arithmetic, tied by the functional-equation relation a*b = 4 g^2 q -- is P3, the unbuilt
arithmetic intersection theory over Z.

WITHDRAWN OVERCLAIM (adversary). The first pass claimed "the entire arithmetic is the single
coupling s = t; M4 localizes to one matrix entry." FALSE: the diagonal b = 2gq carries q (a
separate arithmetic input; the flip threshold 2g*sqrt(q) moves with q), and the complex-root /
fixed-locus axes both REQUIRE a*b = 4 g^2 q. The arithmetic is the JOINT Gram = P3, not one entry.
Control B ("a random coupling flips too, so only s=t is arithmetic") is a tautology -- it shows
detector faithfulness (the form responds to its own off-diagonal), not concentration; the actual
discriminator between s=t and a generic s IS the Weil bound = M4, which no cheap control can show.

THE FAITHFULNESS CAVEAT (the real, honest yield). Genus 1 is the EASIEST Weil case: the 2x2
negative-definiteness is just det > 0 for a binary quadratic form, which Hasse proved in 1933
from norm-form positivity -- before Weil, with NO Hodge index theorem. So in this shadow P6 looks
automatic the instant P3 is supplied. That is an ARTIFACT of genus 1. The genuine M4 difficulty --
higher-RANK Rosati positivity (Hodge-Riemann on a >2-dim primitive part), the archimedean Gamma_S
place, and the global S -> infinity assembly -- is exactly what the 2x2 genus-1 form discards.
So the breadth fingerprint is a GENUS-1-FAITHFUL shape, and "the fingerprint localizes M4" must
NOT be read as "M4 is elementary once P3 is supplied." The fingerprint is necessary, genus-1-
faithful, and silent about the rank/archimedean/global content where M4 is actually hard.

D-H / K1 / K2. K1-clean: the form is the signature of an intersection Gram built from intersection
numbers and a free trace parameter t; zero locations are never input (the off-line flip is a
hypothetical sweep of t). K2: D-H has no Euler product => no Frobenius => no q => no NS(C x C) at
all -- it builds NONE of the form (not "the diagonal but not s"; the whole object is unbuildable),
exactly 09A's K2.

Run:
  python -m experiments.arithmetic_geometric.e2ww_ahk_tslot_flip
"""

from __future__ import annotations

from math import comb, sqrt

import numpy as np

try:
    from experiments.lemma_db.breadth_corpus import battery, _S
    _HAVE_CORPUS = True
except Exception:                       # keep runnable if the corpus module moves
    _HAVE_CORPUS = False


# ---------------------------------------------------------------------------
# The AHK / FF primitive form (e2uu): Q(a,b,s) = [[-a,-s],[-s,-b]].
# ---------------------------------------------------------------------------
def Q_form(a: float, b: float, s: float) -> np.ndarray:
    return np.array([[-a, -s], [-s, -b]], dtype=float)


def is_neg_def(M: np.ndarray) -> bool:
    return bool(np.all(np.linalg.eigvalsh(M) < 0))


def signature(M: np.ndarray) -> tuple:
    ev = np.linalg.eigvalsh(M)
    return (int(np.sum(ev > 1e-12)), int(np.sum(ev < -1e-12)))


# ---------------------------------------------------------------------------
# (1) The off-line-flip on the FF shadow: the form is the polarization on-line and flips
#     off-line. The flip is on the SIGN (passes #121 selection-not-sign).
# ---------------------------------------------------------------------------
def offline_flip_ff(q: float = 25.0, g: float = 1.0) -> list:
    """Weil bound |t| <= 2 sqrt(q) (g=1) IS RH. |t| < 2 sqrt q = on-line (neg-def polarization);
    |t| > 2 sqrt q = off-line zero (indefinite). Sweep t across the boundary."""
    a, b = 2 * g, 2 * g * q
    two_sq = 2 * g * sqrt(q)
    rows = []
    for label, t in [("on-line (t small)", 0.5 * two_sq), ("on-line (interior)", 0.9 * two_sq),
                     ("off-line (just past)", 1.05 * two_sq), ("off-line (far)", 1.3 * two_sq)]:
        M = Q_form(a, b, t)
        rows.append({"label": label, "t": t, "two_sqrt_q": two_sq,
                     "weil_bound_holds": t * t < 4 * g * g * q, "signature": signature(M),
                     "neg_def": is_neg_def(M)})
    return rows


# ---------------------------------------------------------------------------
# (2) The connection: the breadth FINGERPRINT/battery() on the FF form = the master candidate.
# ---------------------------------------------------------------------------
def fingerprint_on_ff_form() -> dict:
    """Run the breadth corpus battery() on the FF/Weil-Rosati form's skeleton. It is the master
    transfer-candidate: contingent + complex-root + line-axis + output-indefinite (SIGN flips,
    not membership) + prohibitive-on-a-fixed-locus, surviving the battery. So the breadth program,
    pointed at the construction, recovers exactly the 09A target object."""
    if not _HAVE_CORPUS:
        return {"available": False}
    weil = _S(1, 1, 1, 1, 1, "contingent", 1, "signature", 1, "all-heights", "complex",
              "line", "prohibitive", "output-indefinite")
    return {"available": True, "battery_fires": battery(weil),
            "is_transfer_candidate": battery(weil) == []}


# ---------------------------------------------------------------------------
# (3) The arithmetic is the JOINT Gram (q in the diagonal AND t off-diagonal) -- adversary fix.
# ---------------------------------------------------------------------------
def joint_arithmetic_check(g: float = 1.0) -> dict:
    """The threshold sqrt(a*b) = 2 g sqrt(q) MOVES with q: the diagonal carries arithmetic too.
    So the arithmetic is the JOINT Gram (a,b,s)=(2g,2gq,t), not the single coupling s. (Withdraws
    the first-pass 'one matrix entry' claim.) And dropping the FE relation a*b = 4 g^2 q breaks
    the coincidence of the det-zero with the RH locus t^2 = 4q."""
    thresholds = {q: 2 * g * sqrt(q) for q in (5, 25, 49)}
    # generic (a,b) NOT obeying a*b = 4 g^2 q: the flip locus no longer matches the Weil bound
    a_gen, b_gen, q = 3.0, 17.0, 25.0
    generic_flip_locus = sqrt(a_gen * b_gen)          # != 2 sqrt(q) = 10
    return {"threshold_moves_with_q": thresholds,
            "diagonal_carries_q": True,
            "generic_ab_flip_locus": generic_flip_locus, "weil_locus_2sqrtq": 2 * sqrt(q),
            "FE_relation_needed": "a*b = 4 g^2 q (else the flip locus != the RH locus)",
            "arithmetic_is": "the JOINT Gram (2g, 2gq, t) = P3, NOT one entry"}


# ---------------------------------------------------------------------------
# (4) K2 / D-H: D-H builds NONE of the form (no Euler => no q => no NS) -- adversary fix.
# ---------------------------------------------------------------------------
def control_dh() -> dict:
    return {"dh_has_euler_product": False,
            "dh_builds_any_of_the_form": False,
            "note": "no Euler product => no Frobenius => no q => no NS(C x C): D-H builds NONE of "
                    "the 2x2 form (not 'the diagonal but not s'); the whole object is unbuildable, "
                    "exactly 09A's K2"}


# ---------------------------------------------------------------------------
# (5) The constructible gap is P3 (e2uu): the bare lattice gives the SHAPE with s = 0.
# ---------------------------------------------------------------------------
def bare_lattice_gap(atoms=(2, 3)) -> dict:
    """e2uu, restated (NOT a new test): the Boolean lattice on the primes gives the AHK SHAPE
    (P1 product via (1+x)^n, P2 rank-symmetry) but a combinatorial degree map with off-diagonal
    s = 0 (t-blind). The single constructible gap is P3 (s = t = q+1-#C). Whether an AHK-machinable
    lattice can carry the JOINT arithmetic Gram while keeping P1+P4 is OPEN (09A Section 7); this
    note does NOT test it."""
    n = len(atoms)
    whitney = [comb(n, k) for k in range(n + 1)]
    product_ok = (np.convolve([1, 1], [1, 1]).tolist() == whitney) if n == 2 else None
    return {"atoms": atoms, "whitney": whitney, "P1_product_(1+x)^n": product_ok,
            "P2_rank_symmetric": whitney == whitney[::-1], "bare_offdiagonal_s": 0.0,
            "constructible_gap": "P3 (the t-carrying degree map = the arithmetic Gram over Z)",
            "section7_open_NOT_tested": "can P3 coexist with P1+P4 on an AHK-machinable lattice?"}


def demo() -> int:
    print("=" * 84)
    print("e2ww: a 9A CONNECTION NOTE (not an advance) -- breadth fingerprint re-derives P3")
    print("=" * 84)

    print("\n[1] Off-line-flip on the FF shadow (the form is the polarization; flips on the SIGN):")
    rows = offline_flip_ff()
    for r in rows:
        print(f"    {r['label']:22}: t={r['t']:.3f} vs 2sqrt(q)={r['two_sqrt_q']:.3f}  "
              f"sig(Q)={r['signature']}  neg-def={r['neg_def']}  Weil={r['weil_bound_holds']}")
    online = [r for r in rows if r["weil_bound_holds"]]
    offline = [r for r in rows if not r["weil_bound_holds"]]
    flipped = all(r["neg_def"] for r in online) and all(not r["neg_def"] for r in offline)
    print(f"    => polarization on-line, flips off-line (the SIGN flips, not membership): {flipped}")

    print("\n[2] CONNECTION: the breadth FINGERPRINT/battery() on the FF form:")
    fp = fingerprint_on_ff_form()
    if fp["available"]:
        print(f"    battery() fires = {fp['battery_fires']}  (empty = survives)")
        print(f"    => the FF/Weil-Rosati form is the MASTER transfer-candidate: "
              f"{fp['is_transfer_candidate']}. Breadth, pointed at the construction, recovers 09A.")
    else:
        print("    (breadth_corpus unavailable; skipped)")

    print("\n[3] The arithmetic is the JOINT Gram, NOT one entry (adversary fix):")
    ja = joint_arithmetic_check()
    print(f"    flip threshold 2g sqrt(q) moves with q: {ja['threshold_moves_with_q']}")
    print(f"    generic (a,b)=(3,17) flips at {ja['generic_ab_flip_locus']:.3f} != Weil locus "
          f"{ja['weil_locus_2sqrtq']:.3f}: the FE relation a*b=4g^2q is REQUIRED")
    print(f"    => arithmetic = {ja['arithmetic_is']}")

    print("\n[4] K2 / D-H (adversary fix): D-H builds NONE of the form:")
    dh = control_dh()
    print(f"    {dh['note']}")

    print("\n[5] The constructible gap is P3 (e2uu, restated -- Section 7 NOT tested):")
    bl = bare_lattice_gap()
    print(f"    Boolean lattice {bl['atoms']}: Whitney {bl['whitney']}, P1 (1+x)^n="
          f"{bl['P1_product_(1+x)^n']}, P2 sym={bl['P2_rank_symmetric']}, bare s={bl['bare_offdiagonal_s']}")
    print(f"    gap = {bl['constructible_gap']};  OPEN (not tested here): {bl['section7_open_NOT_tested']}")

    print("\n" + "=" * 84)
    print("VERDICT (a CONNECTION + a CAVEAT, NOT an advance):")
    print("  - CONNECTION: the breadth fingerprint, run on the FF form, recovers the 09A master")
    print("    object and the SAME constructible gap e2uu/#105 found -- P3. Two directions converge.")
    print("  - The arithmetic is the JOINT Gram (2g,2gq,t)=P3 (q in the diagonal too), NOT one entry")
    print("    (the first-pass '4-free/1-arithmetic' claim is WITHDRAWN, adversary).")
    print("  - FAITHFULNESS CAVEAT (the real yield): genus 1 is the EASIEST Weil case (Hasse 1933,")
    print("    norm-form positivity, no Hodge index theorem); the 2x2 makes P6 look automatic once")
    print("    P3 is supplied -- an ARTIFACT. The genuine M4 difficulty (higher-RANK Rosati, the")
    print("    archimedean Gamma_S, the global S->inf assembly) is exactly what this shadow discards.")
    print("    So 'the fingerprint localizes M4' must NOT be read as 'M4 is elementary given P3'.")
    print("  - P6 / M4 is UNTOUCHED. Sound content = e2uu/#105 + breadth #120/#121; no new ground.")
    print("=" * 84)

    assert flipped, "the FF form must be the polarization on-line and flip off-line"
    if fp["available"]:
        assert fp["is_transfer_candidate"], "the FF form must be the master transfer-candidate"
    assert bl["P2_rank_symmetric"] and bl["P1_product_(1+x)^n"], "the bare lattice must have P1+P2"
    print("\n(all structural assertions hold)")
    return 0


if __name__ == "__main__":
    raise SystemExit(demo())
