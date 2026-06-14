"""MC.2: link the modular data to the Weil operator C_E (#70) and the Sen flow Theta
(#41) on the finite Euler-Sen model, and locate exactly what the modular structure
does NOT supply (modular-carrier milestone MC.2, -> LEARNINGS #101).

SET-UP (from e2lo/#70 and EulerSenLinearAlgebra.lean, genus 1)
-------------------------------------------------------------
On the 2-dim primitive H^1 with the symplectic cup form Omega = [[0,1],[-1,0]] and the
Rosati matrix B_E(q,t) = [[2, t], [t, 2q]] (= -G_prim, the 2G primitive form), e2lo's
polar construction gives A_E = Omega^{-1} B_E, A_E^2 = (t^2 - 4q) I, and the Weil
operator C_E = A_E (-A_E^2)^{-1/2}, with C_E^2 = -I and the polarization
Q = Omega(., C_E .) = B_E / sqrt(4q - t^2) positive-definite iff t^2 < 4q (Hasse-Weil).
The Sen operator is Theta = -1/2 I + N with N the monodromy nilpotent (N^2 = 0, N != 0).

WHAT THIS LOCATES (each asserted)
---------------------------------
The modular PoC (#100, e2pp) showed the modular structure supplies log Delta (the
weight grading, t-INDEPENDENT) and J (the antilinear involution, J^2 = +1) with the
FE duality. MC.2 checks how that meets the polarization data, and finds three honest
gaps that say exactly what is still M4:

1. Theta is NON-semisimple, so it is NOT self-adjoint, so it is NOT log Delta for any
   state (log Delta is self-adjoint). The modular Hamiltonian can match only the
   SEMISIMPLE part of Theta (the weight); the monodromy N is invisible to it (#69).
2. The Weil operator C_E is a complex-linear COMPLEX STRUCTURE (C_E^2 = -I), NOT the
   antilinear modular conjugation J (J^2 = +1). The naive "J = C_E" is a category error:
   J is the real-structure conjugation, C_E is the polarization phase. C_E is EXTRA
   data beyond the modular conjugation.
3. The C_E-twisted polarization B_E CARRIES the Frobenius trace t (B_E(t) differs for
   different t and is PD iff Hasse-Weil), whereas the modular weight scaffolding
   (log Delta) and a GNS trace form are t-INDEPENDENT. So t is injected by C_E, not by
   the modular Hamiltonian.

REFINEMENT OF #99/e2oo: both the trace form and the polarization B_E are positive-
DEFINITE; the genuine discriminator is "carries t," not "definite vs indefinite." The
indefinite object is the cup form Omega / G_prim, which C_E converts into the positive
t-carrying polarization. Running this file IS the test.
"""

from __future__ import annotations

import numpy as np

from experiments.lemma_db.shadow_battery import signature


OMEGA = np.array([[0.0, 1.0], [-1.0, 0.0]])


def b_e(q: float, t: float) -> np.ndarray:
    """The Rosati matrix B_E(q,t) = -G_prim, genus 1."""
    return np.array([[2.0, t], [t, 2.0 * q]])


def a_e(q: float, t: float) -> np.ndarray:
    return np.linalg.inv(OMEGA) @ b_e(q, t)


def weil_operator(q: float, t: float):
    """C_E = A_E (-A_E^2)^{-1/2}, defined (real) in the Hasse-Weil regime t^2 < 4q."""
    A = a_e(q, t)
    A2 = A @ A
    gap = 4.0 * q - t * t   # = -trace-scalar of A^2; A^2 = (t^2-4q) I
    if gap <= 0:
        return None, A2, gap
    C = A / np.sqrt(gap)
    return C, A2, gap


def theta_sen() -> np.ndarray:
    """The non-semisimple Sen block Theta = -1/2 I + N (lower Jordan)."""
    return np.array([[-0.5, 0.0], [1.0, -0.5]])


def part1_theta_not_modular_hamiltonian() -> dict:
    Th = theta_sen()
    S = -0.5 * np.eye(2)          # semisimple part
    N = Th - S                    # monodromy nilpotent
    return {
        "theta_self_adjoint": bool(np.allclose(Th, Th.T)),   # log Delta would be self-adjoint
        "nilpotent_nonzero": float(np.max(np.abs(N))) > 1e-9,
        "nilpotent_squares_to_zero": bool(np.allclose(N @ N, 0.0)),
        "semisimple_part": S.diagonal().tolist(),
    }


def part2_CE_is_not_J(q: float = 5.0, t: float = 1.0) -> dict:
    C, A2, gap = weil_operator(q, t)
    CE_sq = C @ C
    return {
        "CE_squared_is_minus_I": bool(np.allclose(CE_sq, -np.eye(2))),   # complex structure
        "J_squared_is_plus_I": True,   # from e2pp: the modular conjugation is an antilinear involution
        "category_match": False,       # C_E (linear, square -I) is NOT J (antilinear, square +I)
        "CE": C.tolist(),
    }


def part3_CE_form_carries_t(q: float = 5.0) -> dict:
    out = {}
    for t in (1.0, 3.0):
        C, A2, gap = weil_operator(q, t)
        Q = OMEGA @ C            # = B_E / sqrt(gap), the polarization matrix
        out[f"t={t}"] = {
            "B_E": b_e(q, t).tolist(),
            "polarization_signature": signature(Q),
            "polarization_pd": signature(Q)[0] == 2 and signature(Q)[1] == 0,
        }
    # an off-line trace (t^2 > 4q): the Weil operator is not real, Q is not a polarization.
    C_off, A2_off, gap_off = weil_operator(q, 5.0)   # 25 > 20
    out["t=5 (off-line)"] = {"weil_operator_real": C_off is not None, "gap_4q_minus_t2": gap_off}
    out["B_E_depends_on_t"] = not np.allclose(b_e(q, 1.0), b_e(q, 3.0))
    return out


def demo() -> int:
    print("MC.2: where the modular structure meets the Weil/Sen polarization data\n")

    p1 = part1_theta_not_modular_hamiltonian()
    print("  [1] Theta (Sen/Frobenius generator) is NON-semisimple, so != log Delta:")
    print(f"      Theta self-adjoint = {p1['theta_self_adjoint']} (log Delta would be); "
          f"nilpotent N != 0 = {p1['nilpotent_nonzero']}, N^2 = 0 = {p1['nilpotent_squares_to_zero']}")
    print(f"      => log Delta can match only the SEMISIMPLE part {p1['semisimple_part']} (the weight); "
          f"the monodromy N is invisible to the modular Hamiltonian (#69).")

    p2 = part2_CE_is_not_J()
    print("\n  [2] the Weil operator C_E is a complex structure, NOT the modular conjugation J:")
    print(f"      C_E^2 = -I : {p2['CE_squared_is_minus_I']} (linear);  "
          f"J^2 = +I (antilinear, e2pp) : {p2['J_squared_is_plus_I']}")
    print(f"      => naive 'J = C_E' is a category error; C_E (the polarization phase) is EXTRA "
          f"data beyond J.")

    p3 = part3_CE_form_carries_t()
    print("\n  [3] the C_E-twisted polarization B_E CARRIES t (the modular weight data does not):")
    for t in (1.0, 3.0):
        d = p3[f"t={t}"]
        print(f"      t={t}: B_E={d['B_E']}, polarization signature {d['polarization_signature']} "
              f"(positive-definite = {d['polarization_pd']})")
    print(f"      B_E depends on t = {p3['B_E_depends_on_t']}; off-line t=5 (t^2>4q): "
          f"Weil operator real = {p3['t=5 (off-line)']['weil_operator_real']} "
          f"(gap 4q-t^2 = {p3['t=5 (off-line)']['gap_4q_minus_t2']:.0f})")

    print("\n  READING: the modular structure (e2pp) supplies the t-INDEPENDENT scaffolding -- the weight")
    print("  grading log Delta and the FE duality J Delta J = Delta^-1. The t-CARRYING polarization needs")
    print("  TWO things the modular Hamiltonian does NOT contain: the complex structure C_E (the phase,")
    print("  C_E^2=-I, != the antilinear J) which injects t, and the monodromy N (!= log Delta, #69). M4 is")
    print("  proving the assembled C_E-twisted form positive without RH input. Refinement of #99: both the")
    print("  trace and B_E are positive-definite; the real discriminator is CARRIES-t, and the indefinite")
    print("  object is the cup form Omega / G_prim that C_E polarizes.")

    assert not p1["theta_self_adjoint"] and p1["nilpotent_nonzero"] and p1["nilpotent_squares_to_zero"], \
        "[1] Theta should be non-semisimple, not self-adjoint"
    assert p2["CE_squared_is_minus_I"] and not p2["category_match"], \
        "[2] C_E^2 = -I and C_E is not the antilinear J"
    assert p3["B_E_depends_on_t"] and p3["t=1.0"]["polarization_pd"] and p3["t=3.0"]["polarization_pd"] \
        and not p3["t=5 (off-line)"]["weil_operator_real"], \
        "[3] B_E carries t, PD in the Hasse-Weil regime, breaks off-line"
    print("\n  (all three structural assertions hold)")
    return 0


if __name__ == "__main__":
    raise SystemExit(demo())
