"""The operator-level statement of P3 (Option 1, continuing e2uu/#105 + e2xx/#123),
ADVERSARY-CORRECTED (scratchpad/higher_rank_faces/01_adversary.md): why a matroid Chow ring
cannot natively carry the Frobenius pi whose powers generate P(T) -- because it is purely
EVEN/Tate and has no H^1 where the modulus-sqrt q eigenvalues live.

SCOPE CORRECTION (load-bearing, adversary): this is a GENUS-1 statement (a 2x2 operator on the
(1,2,1) Chow ring), NOT a higher-rank construction. No genus >= 2 Chow ring is built; the
"whose powers generate P(T)" content is e2xx's (#123) and at genus 1 collapses to e2uu's single
t_1 (#105). The earlier "higher-rank P3" label is WITHDRAWN. What this file gives is the
operator-level (genus-1) reformulation of the e2uu/#105 gap, plus one genuinely new wrinkle.

THE QUESTION
------------
e2xx (#123) sharpened the AHK gap: the moment sequence {t_n} = the curve's zeta P(T) is generated
by one Frobenius endomorphism pi (char poly P(T)), so "carry P(T)" = "supply pi, a degree-
preserving self-map with the Weil normalization |eig(pi)| = sqrt q". Does a matroid Chow ring
CONTAIN such a pi as a genuine graded-ring endomorphism?

THE ANSWER (a near-theorem, not three examples)
-----------------------------------------------
A degree-preserving GRADED-RING endomorphism T of A^1 must respect the Chow multiplication
A^1 x A^1 -> A^2, which on A^1 = span(e1, p1) of the (1,2,1) ring is the LORENTZIAN form
  e1.e1 = e2,  e1.p1 = 0,  p1.p1 = -e2,   i.e.  Q = diag(1, -1)   (the Hodge-index (1,n-1), e2g/#48).
So T must be a SIMILITUDE of Q:  T^T Q T = mu Q. The similitudes of an indefinite binary form are:

  (1) ROOTS OF UNITY  (diagonal diag(lam, 1/lam) preserves Q only for lam^4 = 1): |eig| = 1.
      = matroid automorphisms; the characteristic-1 / q=1 shadow (#40).
  (2) HYPERBOLIC BOOSTS  (the general similitude): REAL, unequal eigenvalues. These are the
      REAL-ROOT half (#119) = the OFF-LINE / non-RH Frobenius (t^2 > 4q). A whole class.
  (3) The SCALAR  lam.Id: |eig| = |lam|, and to be a valid (real-moment) Frobenius it is forced
      to lam = +-sqrt q, the DEGENERATE supersingular boundary t = +-2g sqrt q.

The GENERIC interior Frobenius pi (RH, |t| < 2g sqrt q) has eigenvalues sqrt q * u, sqrt q * conj(u)
with |u| = 1 -- a scaled ROTATION. A rotation preserves the DEFINITE form diag(1, 1), NOT the
indefinite Chow product diag(1, -1). So the on-circle Frobenius is NOT a similitude of Q, i.e.
NOT a graded-ring endomorphism of the lattice at all. This is #119 (real-root combinatorial vs
complex-root Frobenius) AS A NEAR-THEOREM, and it is the genuine obstruction the eigenvalue-
modulus picture only shadows.

THE CLEANEST PHRASING (the deepest content)
-------------------------------------------
A matroid Chow ring is purely EVEN / algebraic (Tate type): it is the analogue of H^{2*}, every
class in weight 2k, all Frobenius eigenvalues powers of q (here the trivial q^0 = 1 on A^1). The
modulus-sqrt q (half-integer-weight) Frobenius eigenvalues live in ODD, weight-1 cohomology
(H^1, a symplectic similitude) -- which a Chow ring DOES NOT HAVE. Putting the H^1 Frobenius onto
A^1 (weight-2, NS-like, symmetric Lorentzian) is a category mismatch; that mismatch IS why the
lattice cannot supply pi. "P3 = supply the arithmetic Frobenius" = "supply the H^1 the Tate-type
combinatorial ring lacks". This is the honest content of #40, sharpened.

THE ONE GENUINELY NEW WRINKLE (adversary-confirmed sound)
---------------------------------------------------------
The scalar (scaling) self-map reaches |eig| = sqrt q but, being scalar (alpha = q/alpha) under a
REAL moment sequence, lands EXACTLY on the degenerate supersingular boundary t = +-2g sqrt q. So
even the one native operator that hits modulus sqrt q is pinned to the RH-extremal point, never
the interior. (Everything else here is #40 + #119 + e2xx at the operator level.)

K1/K2: K1-clean (eigenvalue/form geometry; no zeros input). K2: no Euler product => no Frobenius
=> no matroid (09A K2); D-H builds no lattice.

Run:
  python -m experiments.arithmetic_geometric.e2yy_higher_rank_p3_frobenius
"""

from __future__ import annotations

import cmath
import math
from pathlib import Path

import numpy as np

Q_LOR = np.diag([1.0, -1.0])                       # the Lorentzian Chow product on A^1 = (e1, p1)
Q_DEF = np.diag([1.0, 1.0])                        # the definite form (what a rotation preserves)


def preserves_up_to_scalar(T: np.ndarray, form: np.ndarray, tol: float = 1e-9):
    """Return mu if T^T form T = mu form for a single scalar mu (T is a similitude of `form`),
    else None."""
    M = T.conj().T @ form @ T
    ratios = []
    for i in range(2):
        for j in range(2):
            if abs(form[i, j]) > tol:
                ratios.append(M[i, j] / form[i, j])
            elif abs(M[i, j]) > tol:
                return None
    mu0 = ratios[0]
    if all(abs(r - mu0) < tol * max(1.0, abs(mu0)) for r in ratios):
        return complex(mu0)
    return None


def eig_moduli(M: np.ndarray) -> list:
    return sorted(round(float(abs(z)), 6) for z in np.linalg.eigvals(M))


# ===========================================================================
# (1) Roots of unity: diagonal graded-ring endos preserve Q only for lam^4 = 1.
# ===========================================================================
def part1_roots_of_unity() -> dict:
    rows = []
    for lam in (1.0, -1.0, 1j, 2.0, math.sqrt(5.0)):
        T = np.diag([lam, 1.0 / lam]).astype(complex)
        mu = preserves_up_to_scalar(T, Q_LOR)
        rows.append({"lam": str(lam), "preserves_lorentzian": mu is not None,
                     "eig_moduli": eig_moduli(T)})
    return {"rows": rows,
            "only_roots_of_unity": all(r["preserves_lorentzian"] == (abs(complex(eval(r["lam"]))**4 - 1) < 1e-9)
                                       for r in rows)}


# ===========================================================================
# (2) Hyperbolic boosts: the general similitude of Q -- REAL eigenvalues (#119).
# ===========================================================================
def part2_boosts_are_real(q: float = 5.0) -> dict:
    sq = math.sqrt(q)
    rows = []
    for theta in (0.0, 0.3, 0.8, 1.5):
        ch, sh = math.cosh(theta), math.sinh(theta)
        B = sq * np.array([[ch, sh], [sh, ch]])    # scaled boost, similitude factor mu = q
        mu = preserves_up_to_scalar(B, Q_LOR)
        ev = np.linalg.eigvals(B)
        both_sqrt_q = bool(np.all(np.abs(np.abs(ev) - sq) < 1e-6))   # raw, not rounded
        rows.append({"theta": theta, "is_similitude": mu is not None,
                     "mu": round(float(mu.real), 4) if mu is not None else None,
                     "eigs_real": bool(np.allclose(ev.imag, 0)),
                     "eig_moduli": eig_moduli(B), "both_sqrt_q": both_sqrt_q})
    # the scalar (theta=0) has BOTH moduli = sqrt q; every non-trivial boost has unequal moduli
    scalar_row = next(r for r in rows if r["theta"] == 0.0)
    only_scalar_hits_sqrt_q = scalar_row["both_sqrt_q"] and all(
        not r["both_sqrt_q"] for r in rows if r["theta"] != 0.0)
    return {"q": q, "sqrt_q": round(sq, 6), "rows": rows,
            "boosts_real_eigs": all(r["eigs_real"] for r in rows),
            "only_scalar_double_sqrt_q": only_scalar_hits_sqrt_q}


# ===========================================================================
# (3) The complex Frobenius preserves the DEFINITE form, NOT the Chow product.
# ===========================================================================
def part3_frobenius_preserves_definite(q: float = 5.0) -> dict:
    sq = math.sqrt(q)
    u = cmath.rect(1.0, 0.6)                        # on the unit circle: an interior RH Frobenius
    R = sq * np.array([[u.real, -u.imag], [u.imag, u.real]])   # scaled rotation (real 2x2)
    mu_def = preserves_up_to_scalar(R, Q_DEF)
    mu_lor = preserves_up_to_scalar(R, Q_LOR)
    ev = np.linalg.eigvals(R)
    return {"q": q, "sqrt_q": round(sq, 6), "eig_moduli": sorted(round(float(abs(z)), 4) for z in ev),
            "preserves_definite": mu_def is not None,
            "mu_definite": round(float(mu_def.real), 4) if mu_def is not None else None,
            "preserves_chow_product": mu_lor is not None,
            "not_a_graded_ring_endo": mu_lor is None}


# ===========================================================================
# (4) The scaling wrinkle (the one genuinely new, sound bit): |eig|=sqrt q but boundary.
# ===========================================================================
def part4_scaling_only_boundary(q: float = 5.0, g: int = 1) -> dict:
    rows = []
    for label, lam in [("real lam=+sqrt q", math.sqrt(q)), ("real lam=-sqrt q", -math.sqrt(q)),
                       ("complex lam", cmath.rect(math.sqrt(q), 0.6))]:
        pi = lam * np.eye(2, dtype=complex)
        c1 = complex(np.trace(pi)) / math.sqrt(q)
        rows.append({"label": label, "scalar": True, "eig_moduli": eig_moduli(pi),
                     "c1": complex(round(c1.real, 4), round(c1.imag, 4)), "c1_real": abs(c1.imag) < 1e-9,
                     "at_boundary": abs(abs(c1.real) - 2 * g) < 1e-9 and abs(c1.imag) < 1e-9})
    valid = [r for r in rows if r["c1_real"]]
    return {"boundary_c1": 2 * g, "rows": rows,
            "scalings_only_boundary": len(valid) > 0 and all(r["at_boundary"] for r in valid)}


def demo() -> int:
    print("=" * 90)
    print("e2yy: the operator-level (genus-1) statement of P3 -- the matroid Chow ring is")
    print("purely even/Tate, so it has no graded-ring Frobenius with |eig| = sqrt q")
    print("=" * 90)

    print("\n[1] Graded-ring endos that are DIAGONAL preserve the Lorentzian Chow product Q=diag(1,-1)")
    print("    only for lam^4=1 (roots of unity, |eig|=1 = the q=1 / automorphism shadow #40):")
    p1 = part1_roots_of_unity()
    for r in p1["rows"]:
        print(f"    lam={r['lam']:>18}: preserves Q = {r['preserves_lorentzian']}  |eig|={r['eig_moduli']}")
    print(f"    => only roots of unity (lam^4=1): {p1['only_roots_of_unity']}")

    print("\n[2] The GENERAL similitude of Q is a hyperbolic BOOST -- REAL eigenvalues (#119, the")
    print("    off-line/non-RH half); only the SCALAR (theta=0) has both |eig|=sqrt q:")
    p2 = part2_boosts_are_real()
    for r in p2["rows"]:
        print(f"    theta={r['theta']}: similitude={r['is_similitude']} (mu={r['mu']})  "
              f"|eig|={r['eig_moduli']}  real={r['eigs_real']}  both=sqrt q? {r['both_sqrt_q']}")
    print(f"    => boosts have real eigs ({p2['boosts_real_eigs']}); only the scalar is double-sqrt q "
          f"({p2['only_scalar_double_sqrt_q']})")

    print("\n[3] The complex on-circle Frobenius (scaled ROTATION) preserves the DEFINITE form,")
    print("    NOT the indefinite Chow product => it is NOT a graded-ring endomorphism:")
    p3 = part3_frobenius_preserves_definite()
    print(f"    |eig| = {p3['eig_moduli']} (both sqrt q = {p3['sqrt_q']}); preserves diag(1,1)? "
          f"{p3['preserves_definite']} (mu={p3['mu_definite']}); preserves Chow diag(1,-1)? "
          f"{p3['preserves_chow_product']}")
    print(f"    => the on-circle Frobenius is NOT a graded-ring endo of the lattice: "
          f"{p3['not_a_graded_ring_endo']} (it needs H^1, which the Tate-type Chow ring lacks)")

    print("\n[4] The one NEW wrinkle: the scalar reaches |eig|=sqrt q but lands on the DEGENERATE")
    print("    supersingular boundary t=+-2g sqrt q (never the interior):")
    p4 = part4_scaling_only_boundary()
    for r in p4["rows"]:
        tag = "VALID" if r["c1_real"] else "INVALID (c_1 not real)"
        print(f"    {r['label']:18}: |eig|={r['eig_moduli']}  c_1={r['c1']}  {tag}"
              f"{'  (boundary)' if r['at_boundary'] else ''}")
    print(f"    => valid scalings reach ONLY the boundary c_1=+-2g=+-{p4['boundary_c1']}: "
          f"{p4['scalings_only_boundary']}")

    print("\n" + "=" * 90)
    print("VERDICT (the operator-level genus-1 statement of P3 -- adversary-corrected):")
    print("  - A degree-preserving graded-RING endomorphism of A^1 must be a SIMILITUDE of the")
    print("    Lorentzian Chow product diag(1,-1): roots of unity (automorphisms, |eig|=1, #40),")
    print("    hyperbolic BOOSTS (REAL eigenvalues = the off-line/non-RH half, #119), and the")
    print("    SCALAR (forced to the supersingular boundary t=+-2g sqrt q).")
    print("  - The GENERIC interior Frobenius is a scaled ROTATION: it preserves the DEFINITE form,")
    print("    NOT the Chow product, so it is NOT a graded-ring endomorphism. Equivalently, the")
    print("    matroid Chow ring is purely EVEN/Tate and has no H^1 where |eig|=sqrt q lives. THAT")
    print("    is why the lattice cannot supply the Frobenius P3 needs (= supply the missing H^1).")
    print("  - This is genus-1 (a 2x2 on (1,2,1)), NOT a higher-rank construction; it is #40+#119")
    print("    +e2xx at the operator level. The one new wrinkle: the scaling hits only the boundary.")
    print("    P6/M4 (proving the positivity) UNTOUCHED.")
    print("=" * 90)

    # ---- structural assertions ----
    assert p1["only_roots_of_unity"], "Part 1: diagonal graded-ring endos must be roots of unity"
    assert p2["boosts_real_eigs"] and p2["only_scalar_double_sqrt_q"], \
        "Part 2: boosts must have real eigs; only the scalar is double-sqrt q"
    assert p3["preserves_definite"] and p3["not_a_graded_ring_endo"], \
        "Part 3: the complex Frobenius preserves the DEFINITE form, not the Chow product"
    assert p4["scalings_only_boundary"], "Part 4: valid scalings must reach only the boundary"
    print("\n(all structural assertions hold)")

    out = Path(__file__).resolve().parent / "e2yy_higher_rank_p3_frobenius.npz"
    np.savez_compressed(out, sqrt_q=p2["sqrt_q"], boundary_c1=p4["boundary_c1"],
                        frobenius_not_graded_endo=p3["not_a_graded_ring_endo"],
                        scalings_only_boundary=p4["scalings_only_boundary"])
    print(f"\nSaved {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(demo())
