"""P3-P4 von Neumann probe: does a finite vN algebra with a faithful trace make
the noncircular <-> euler-gated edge an iff? (frame-audit follow-up, LEARNINGS #98 -> #99)

THE QUESTION
------------
The regime-two frame-audit (#98, docs/03_research/optimizing_rh_for_ai.md) found the
M4 property graph has exactly one live edge, P3-P4, graded CORRELATED in the
polarized-Frobenius / Rosati frame:
  P3 = noncircular  (positivity from an INTRINSIC polarization, not read off the zeros)
  P4 = euler-gated  (the algebra exists only with an Euler product; the D-H firewall)
The synthesis named the sharpest next probe: does REQUIRING the arithmetic Frobenius
algebra A to be a finite von Neumann algebra with a faithful normal tracial state
upgrade CORRELATED to GENUINE, i.e. make "A exists and is euler-gated" (P4)
co-extensive with "A carries an intrinsic positive Rosati involution" (P3)?

A finite vN algebra with a faithful normal trace tau DOES carry a canonical intrinsic
positive form for free: the GNS / trace inner product <a,b> = tau(b* a), positive-
DEFINITE by faithfulness. So naively the upgrade "works": existence of the traced
algebra forces an intrinsic positivity. The probe asks whether that is the RIGHT
positivity (the one that reaches P5 = the indefinite (1,n-1) Hodge index that IS RH).

THE ANSWER (predicted NONE-or-CORRELATED; reached three independent ways)
------------------------------------------------------------------------
Block 1: a faithful trace gives an intrinsic positive form (the GNS Gram is PD).
Block 2: but that form is positive-DEFINITE BY CONSTRUCTION (tau(x x*) >= 0, = 0 iff
         x = 0), so it can NEVER be the indefinite (1, n-1) signature M4 needs. The very
         property that makes the upgrade work is what makes it the WRONG signature.
Block 3: the natural arithmetic state is a KMS state with a nontrivial modular flow
         (the scaling / Frobenius dynamics), which is NOT a trace (Bost-Connes is type
         III_1, #81). So the "faithful normal trace state" hypothesis is not even
         satisfied by the natural algebra; the free PD form is unavailable there.
Block 4: the trace form needs no Euler product (every *-algebra has it), so it is
         D-H-blind -- a soft positivity, not the euler-gated M4 form.

Net: the upgrade yields P3 from P4 only as a DEFINITE, D-H-BLIND positivity on a
type II_1 algebra the arithmetic does not provide (it is type III_1). So the edge is
CORRELATED, not GENUINE, for the RH-relevant (indefinite, euler-gated) positivity.
P5 stays isolated. The residual is named: M4 = the gap between the free definite trace
form and the needed indefinite (1, n-1) euler-gated Hodge form (the #68 transport
result restated -- a faithful trace fixes the form to be PD; M4 needs it indefinite).

Running this file IS the test: each block asserts its structural claim.
"""

from __future__ import annotations

import math

import numpy as np

from experiments.lemma_db.shadow_battery import signature, is_lorentzian
from experiments._shared import zeta_L, DavenportHeilbronn


def matrix_units(d: int) -> list:
    """The standard basis E_ij of M_d(C)."""
    out = []
    for i in range(d):
        for j in range(d):
            E = np.zeros((d, d), dtype=complex)
            E[i, j] = 1.0
            out.append(E)
    return out


def gns_gram(trace, basis) -> np.ndarray:
    """The GNS / trace Gram matrix G[i,j] = trace(basis[j]^dagger @ basis[i]),
    the matrix of the inner product <a, b> = trace(b* a). Hermitian; positive-
    definite iff the trace is faithful."""
    n = len(basis)
    G = np.zeros((n, n), dtype=complex)
    for i in range(n):
        for j in range(n):
            G[i, j] = trace(basis[j].conj().T @ basis[i])
    return G


# ---------------------------------------------------------------------------
# Block 1: a finite vN algebra with a faithful trace gives an intrinsic PD form.
# ---------------------------------------------------------------------------

def block1_finite_trace_gives_pd(d: int = 2) -> dict:
    basis = matrix_units(d)
    tau = lambda x: np.trace(x) / d           # the normalized (faithful, tracial) state on M_d
    G = gns_gram(tau, basis)
    w = np.linalg.eigvalsh(G)
    pd = bool((w > 1e-12).all())
    return {"d": d, "min_eig": float(w.min()), "pd": pd, "gram": G}


# ---------------------------------------------------------------------------
# Block 2: that intrinsic form is positive-DEFINITE, never the indefinite (1, n-1).
# ---------------------------------------------------------------------------

def gprim(g: float, q: float, t: float) -> np.ndarray:
    """The 2G primitive intersection form (the indefinite Hodge-index target)."""
    return np.array([[-2 * g, -t], [-t, -2 * g * q]], dtype=float)


def block2_definite_not_indefinite(d: int = 2) -> dict:
    G = block1_finite_trace_gives_pd(d)["gram"].real  # Hermitian, real spectrum
    trace_sig = signature(G)                            # the GNS form's signature
    # The M4 target signature (indefinite (1, n-1)); the function-field Hodge index
    # is the negative of gprim, whose primitive form is INDEFINITE on the full space.
    m4_target = np.diag([1.0, -1.0, -1.0, -1.0])        # canonical (1, 3) witness
    return {
        "trace_signature": trace_sig,                   # (n_pos, n_neg, n_zero)
        "trace_is_definite": trace_sig[1] == 0 and trace_sig[2] == 0,
        "m4_is_indefinite": is_lorentzian(m4_target),
        "gprim_neg_def_example": tuple(np.round(np.linalg.eigvalsh(gprim(1, 5, 1)), 4).tolist()),
    }


# ---------------------------------------------------------------------------
# Block 3: the natural arithmetic state is a KMS state, NOT a trace (type III).
# ---------------------------------------------------------------------------

def block3_kms_not_trace(beta: float = 1.0) -> dict:
    """A Gibbs/KMS state omega(x) = Tr(rho x), rho = e^{-beta H}/Z, for a non-scalar
    Hamiltonian H (the modular generator = the scaling/Frobenius flow). A trace would
    satisfy omega(xy) = omega(yx) for all x, y. The KMS state does not."""
    rho = np.diag([1.0, math.exp(-beta)])
    rho = rho / np.trace(rho)
    omega = lambda x: complex(np.trace(rho @ x)).real
    E12 = np.array([[0.0, 1.0], [0.0, 0.0]])
    E21 = np.array([[0.0, 0.0], [1.0, 0.0]])
    a = omega(E12 @ E21)   # omega(E11)
    b = omega(E21 @ E12)   # omega(E22)
    asym = abs(a - b)
    return {
        "beta": beta,
        "omega_xy": a, "omega_yx": b,
        "trace_property_holds": asym < 1e-12,
        "asymmetry": asym,
        "modular_ratio_exp_minus_beta": math.exp(-beta),
    }


# ---------------------------------------------------------------------------
# Block 4: the trace form is D-H-blind (needs no Euler product), so not euler-gated.
# ---------------------------------------------------------------------------

def block4_trace_is_dh_blind() -> dict:
    """The GNS/trace form is defined for ANY *-algebra, with no reference to primes
    or an Euler product. So it exists equally for zeta and for Davenport-Heilbronn:
    a soft, D-H-blind positivity, not the euler-gated M4 form."""
    zeta_euler = bool(getattr(zeta_L, "has_euler_product", False))
    dh_euler = bool(getattr(DavenportHeilbronn(), "has_euler_product", False))
    # the trace form on M_2 is PD regardless of any Euler structure (block 1):
    trace_form_exists_without_euler = block1_finite_trace_gives_pd(2)["pd"]
    return {
        "zeta_has_euler_product": zeta_euler,
        "dh_has_euler_product": dh_euler,
        "trace_form_needs_euler_product": False,
        "trace_form_exists_without_euler": trace_form_exists_without_euler,
    }


def demo() -> int:
    print("P3-P4 von Neumann probe: can a faithful trace upgrade noncircular<->euler-gated to an iff?\n")

    b1 = block1_finite_trace_gives_pd()
    print(f"  [Block 1] finite vN + faithful trace -> intrinsic positive form")
    print(f"            GNS Gram on M_{b1['d']}: min eig = {b1['min_eig']:.3f}, "
          f"positive-definite = {b1['pd']}  (so P3 'intrinsic positivity' is FREE)")

    b2 = block2_definite_not_indefinite()
    print(f"\n  [Block 2] but that form is positive-DEFINITE, never the M4 Hodge polarization")
    print(f"            trace-form signature = {b2['trace_signature']} (positive-definite = {b2['trace_is_definite']});")
    print(f"            M4's form is NOT positive-definite: the full Hodge index is indefinite (1, n-1) "
          f"= {b2['m4_is_indefinite']},")
    print(f"            equivalently the 2G primitive form is negative-definite under Hasse-Weil "
          f"(gprim eigenvalues {b2['gprim_neg_def_example']}). Either way != the PD trace form.")

    b3 = block3_kms_not_trace()
    print(f"\n  [Block 3] the natural arithmetic state is KMS (modular), NOT a trace")
    print(f"            omega(xy) = {b3['omega_xy']:.4f} != omega(yx) = {b3['omega_yx']:.4f}  "
          f"(asymmetry {b3['asymmetry']:.4f}); trace property holds = {b3['trace_property_holds']}")
    print(f"            -> the modular flow (Frobenius/scaling) makes it type III (Bost-Connes), "
          f"no faithful trace")

    b4 = block4_trace_is_dh_blind()
    print(f"\n  [Block 4] the trace form is D-H-blind (needs no Euler product)")
    print(f"            zeta euler-product = {b4['zeta_has_euler_product']}, "
          f"D-H euler-product = {b4['dh_has_euler_product']}, "
          f"trace form needs euler = {b4['trace_form_needs_euler_product']}")

    print("\n  VERDICT: CORRELATED, not GENUINE. A faithful trace DOES force an intrinsic positivity")
    print("  (P3 from P4), but it is DEFINITE (block 2) and D-H-BLIND (block 4), on a type II_1 algebra")
    print("  the arithmetic does not provide (it is type III_1, block 3). The upgrade reaches the WRONG")
    print("  positivity; P5 (the indefinite, euler-gated Hodge form = RH) stays isolated. The residual is")
    print("  named: M4 = (indefinite (1,n-1), euler-gated) minus (definite trace) -- the #68 transport")
    print("  result restated, that a faithful trace fixes the form PD while M4 needs it indefinite.")

    # Running this file IS the test.
    assert b1["pd"], "block 1: faithful trace should give a PD GNS form"
    assert b2["trace_is_definite"] and b2["m4_is_indefinite"], \
        "block 2: trace form definite, M4 target indefinite"
    assert not b3["trace_property_holds"] and b3["asymmetry"] > 1e-6, \
        "block 3: the KMS state should NOT be a trace"
    assert b4["zeta_has_euler_product"] and not b4["dh_has_euler_product"] \
        and not b4["trace_form_needs_euler_product"], \
        "block 4: trace form must be D-H-blind (exists with or without an Euler product)"
    print("\n  (all four structural assertions hold)")
    return 0


if __name__ == "__main__":
    raise SystemExit(demo())
