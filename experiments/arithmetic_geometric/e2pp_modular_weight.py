"""Modular-carrier proof-of-concept: the type III modular structure supplies the
weight grading + FE-duality the trace lacks (scoping for the #99 steer, -> #100).

THE STEER (from #99, e2oo)
--------------------------
The P3-P4 probe showed a faithful TRACE gives only a positive-DEFINITE, D-H-blind
form (the wrong M4 signature), and that the natural arithmetic algebra is type III_1
(Bost-Connes), which has no faithful trace. The constructive steer: the polarization
must ride on the MODULAR structure (the type III modular flow = the Frobenius/scaling
dynamics), not on a trace. This PoC tests the cheap feasibility question that steer
implies: does the modular (non-tracial) structure actually SUPPLY ingredients the
trace cannot?

WHAT TOMITA-TAKESAKI GIVES (finite-dim model)
---------------------------------------------
For the state phi(x) = Tr(rho x) on M_n (rho > 0, Tr rho = 1) acting on its GNS space:
  modular operator   Delta(x) = rho x rho^{-1}        (spectrum {rho_i/rho_j})
  modular flow       sigma_t(x) = rho^{it} x rho^{-it}  (the dynamics; = Frobenius/scaling)
  modular conjugation J(x) = rho^{1/2} x* rho^{-1/2}    (antilinear involution; the Weil/Hodge C-operator avatar)
log Delta is the modular Hamiltonian; its spectrum is the WEIGHT grading.

THREE STRUCTURAL FACTS THIS PoC ESTABLISHES (each asserted)
----------------------------------------------------------
1. A TRACE is weightless: rho = I/n => Delta = I, no weight grading, sigma_t trivial.
   (Why the trace cannot carry the Hodge weight filtration: it has no weights.)
2. A MODULAR (non-tracial) state supplies a nontrivial weight grading: log Delta has a
   nonzero spectrum = the candidate weight filtration (#93: the halving = the Poincare
   weight ladder; the Frobenius eigenvalue moduli q^{w/2}).
3. The weight grading carries the FE/Poincare DUALITY for free: J Delta J = Delta^{-1},
   so the spectrum of log Delta is symmetric under negation (Gr_w <-> Gr_{-w}, the s<->1-s
   functional-equation symmetry). Perfectness is free; what is NOT supplied is the
   positivity/signature (M4) -- consistent with the all-roads thesis.

This is a POSITIVE feasibility nugget (the modular route supplies the weight ladder +
the duality the trace lacks), NOT a proof: the indefinite polarization that carries t
and is euler-gated is still M4. Running this file IS the test.
"""

from __future__ import annotations

import numpy as np


def matrix_units(d: int) -> list:
    out = []
    for i in range(d):
        for j in range(d):
            E = np.zeros((d, d), dtype=complex)
            E[i, j] = 1.0
            out.append(E)
    return out


def modular_data(rho: np.ndarray):
    """Tomita-Takesaki data for phi(x) = Tr(rho x) on M_d. Returns callables
    Delta, J and the rho^{+-1/2} roots. Delta(x) = rho x rho^{-1}; J(x) = rho^{1/2} x* rho^{-1/2}."""
    ev, U = np.linalg.eigh(rho)
    r_half = U @ np.diag(np.sqrt(ev)) @ U.conj().T
    r_inv = U @ np.diag(1.0 / ev) @ U.conj().T
    r_inv_half = U @ np.diag(1.0 / np.sqrt(ev)) @ U.conj().T
    Delta = lambda x: rho @ x @ r_inv
    J = lambda x: r_half @ x.conj().T @ r_inv_half
    return Delta, J


def weight_spectrum(rho: np.ndarray) -> list:
    """Spectrum of log Delta = { log(rho_i / rho_j) }: the modular weight grading."""
    d = rho.shape[0]
    ev = np.linalg.eigvalsh(rho)
    return sorted(round(float(np.log(ev[i] / ev[j])), 9) for i in range(d) for j in range(d))


def block_trace_is_weightless(d: int = 3) -> dict:
    rho = np.eye(d, dtype=complex) / d           # the (faithful) tracial state
    spec = weight_spectrum(rho)
    return {"rho": "I/d (trace)", "weights": spec, "weightless": all(abs(w) < 1e-9 for w in spec)}


def block_modular_supplies_weights(weights=(1.0, 2.0, 4.0)) -> dict:
    d = len(weights)
    rho = np.diag(np.array(weights, dtype=complex))
    rho = rho / np.trace(rho)                     # a non-tracial (modular / KMS) state
    spec = weight_spectrum(rho)
    nontrivial = any(abs(w) > 1e-9 for w in spec)
    symmetric = np.allclose(spec, sorted(-w for w in spec), atol=1e-9)   # FE / Poincare duality
    return {"rho": "diag (modular)", "weights": spec,
            "nontrivial_grading": nontrivial, "fe_symmetric": symmetric}


def block_J_is_involutive_and_dualizes(weights=(1.0, 2.0, 4.0)) -> dict:
    """J is an antilinear involution (J^2 = 1), and it dualizes the modular operator:
    J Delta J = Delta^{-1} (the operator form of the FE / Poincare duality)."""
    d = len(weights)
    rho = np.diag(np.array(weights, dtype=complex))
    rho = rho / np.trace(rho)
    Delta, J = modular_data(rho)
    r_inv = np.linalg.inv(rho)
    Delta_inv = lambda x: r_inv @ x @ rho
    basis = matrix_units(d)
    j_invol = max(np.max(np.abs(J(J(x)) - x)) for x in basis)            # J^2 = 1
    jdj_dual = max(np.max(np.abs(J(Delta(J(x))) - Delta_inv(x))) for x in basis)  # J Delta J = Delta^{-1}
    return {"J_involution_residual": float(j_invol),
            "JDeltaJ_eq_DeltaInv_residual": float(jdj_dual),
            "J_is_involution": j_invol < 1e-9, "J_dualizes_Delta": jdj_dual < 1e-9}


def demo() -> int:
    print("Modular-carrier PoC: does the type III modular structure supply what the trace lacks?\n")

    t = block_trace_is_weightless()
    print(f"  [1] the TRACE is weightless: rho = I/d -> log Delta spectrum {t['weights']}  "
          f"(weightless = {t['weightless']})")
    print(f"      a trace has no weight grading, so it cannot carry the Hodge weight filtration.")

    m = block_modular_supplies_weights()
    print(f"\n  [2] a MODULAR (non-tracial) state supplies a weight grading:")
    print(f"      log Delta spectrum {m['weights']}  (nontrivial = {m['nontrivial_grading']})")
    print(f"      = the candidate weight ladder (#93 Poincare halving; Frobenius moduli q^(w/2)).")

    j = block_J_is_involutive_and_dualizes()
    print(f"\n  [3] the modular conjugation J is an involution that DUALIZES Delta (FE / Poincare):")
    print(f"      J^2 = 1 (residual {j['J_involution_residual']:.1e}); "
          f"J Delta J = Delta^{{-1}} (residual {j['JDeltaJ_eq_DeltaInv_residual']:.1e})")
    print(f"      so the weight spectrum is symmetric under negation (Gr_w <-> Gr_-w = s<->1-s); "
          f"FE-symmetric = {m['fe_symmetric']}.")

    print("\n  READING: the modular (type III) structure supplies, FOR FREE, the weight grading and the")
    print("  FE/Poincare duality that the trace lacks. This is why 'the arithmetic lives in the modular")
    print("  structure, not the trace' (#99). What is NOT supplied is the POSITIVITY/signature (M4): J is")
    print("  the avatar of the Weil/Hodge C-operator, but proving the J-twisted indefinite form is a")
    print("  polarization that carries t and is euler-gated is the same open kernel. Perfectness free,")
    print("  positivity the gap -- the all-roads thesis, now on the modular side.")

    assert t["weightless"], "[1] the trace should be weightless"
    assert m["nontrivial_grading"] and m["fe_symmetric"], "[2] modular state should give a symmetric nontrivial grading"
    assert j["J_is_involution"] and j["J_dualizes_Delta"], "[3] J should be an involution dualizing Delta"
    print("\n  (all three structural assertions hold)")
    return 0


if __name__ == "__main__":
    raise SystemExit(demo())
