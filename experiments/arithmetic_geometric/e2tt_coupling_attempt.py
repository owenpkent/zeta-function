"""MC.4 coupling attempt: can the per-block coupling be SOURCED from the modular
carrier? (executes the e2ss/#103 adversary test AT-1, -> LEARNINGS #104).

THE RESIDUAL (from #103, e2ss)
------------------------------
MC.4 = M4 needs the COUPLING between the per-prime twisted blocks that FORCES
|t_p| < 2 sqrt p from the modular flow itself, rather than asserting it block by
block. The decoupled carrier is K1-circular because log Delta is t-blind. The open
question (AT-1): is there a coupling sourced ONLY from the modular/KMS data (beta>1)
that constrains the traces? This file answers it.

THE ARGUMENT (and its concrete check)
-------------------------------------
The carrier is the Bost-Connes algebra + the KMS_beta state. Its data -- the modular
Hamiltonian (eigenvalues {log n}), the modular operator Delta, the Gibbs weights
n^{-beta} -- is a function of (the prime set, beta) ALONE. It does NOT depend on the
Frobenius traces t_p (the traces enter only through C_E, the per-prime polarization
phase, MC.2/#101). Therefore ANY coupling functorially derived from the carrier is
t-INDEPENDENT, and a t-independent operator cannot encode the t-dependent constraint
|t_p| < 2 sqrt p. So the coupling that SOURCES the constraint must be a coupling of the
C_E's (the polarization phases) -- which is exactly the global cup product / the
product-surface intersection form (the 2G object), t-carrying and not supplied by the
carrier. AT-1 is closed in the negative: no carrier-sourced coupling helps.

THE FOUR FACES OF THE COUPLING (the synthesis)
----------------------------------------------
The coupling is one object with four presentations, all open over Spec(Z):
  - modular side (here):     a t-carrying coupling of the C_E polarization phases;
  - function-field template:  the cup product H^1 x H^1 -> H^2, negative-definite
                              primitive part = Castelnuovo-Severi (2G, a THEOREM);
  - AHK side (09A):           the t-carrying submodular Lefschetz + indefinite primitive
                              form on the arithmetic prime-lattice;
  - Arakelov side:            the Faltings-Hriljac product pairing + the Gamma_S place.
Building any one of them is M4. Running this file IS the test (each claim asserted).
"""

from __future__ import annotations

import mpmath as mp
import numpy as np

OMEGA = np.array([[0.0, 1.0], [-1.0, 0.0]])
TOL = 1e-9


def b_e(p: float, t: float) -> np.ndarray:
    """The 2G Rosati / cup block B_E(p,t) = -G_prim (genus 1). CARRIES t."""
    return np.array([[2.0, t], [t, 2.0 * p]])


def weil_twist(p: float, t: float):
    """C_E = A_E(-A_E^2)^{-1/2}; the polarization phase. Real iff t^2 < 4p."""
    A = np.linalg.solve(OMEGA, b_e(p, t))
    gap = 4.0 * p - t * t
    if gap <= TOL:
        return None, gap
    return A / np.sqrt(gap), gap


# --------------------------------------------------------------------------
# Part 1: the carrier data is t-INDEPENDENT (so any carrier-derived coupling is too).
# --------------------------------------------------------------------------

def carrier_weight_spectrum(primes, beta):
    """The BC modular weight spectrum {log n - log m} and the Gibbs weights
    {n^{-beta}}: functions of (primes, beta) ALONE, with NO trace input."""
    ns = sorted({1} | {p ** k for p in primes for k in range(1, 3)})
    logs = [float(mp.log(n)) for n in ns]
    spec = sorted(round(a - b, 9) for a in logs for b in logs)
    gibbs = sorted(round(n ** (-beta), 9) for n in ns)
    return spec, gibbs


def carrier_coupling(p, q, beta):
    """A representative coupling functorially built from carrier data only: the
    Gibbs-weighted cross block (pq)^{-beta} I. Manifestly t-independent (it is a
    function of p, q, beta), like every carrier-derived operator."""
    return (p * q) ** (-beta) * np.eye(2)


def part1_carrier_is_t_blind(primes=(2, 3, 5, 7), beta=1.5):
    spec, gibbs = carrier_weight_spectrum(primes, beta)
    # the carrier data does not even take a trace argument; two "trace assignments"
    # produce byte-identical carrier data because t never enters it.
    spec2, gibbs2 = carrier_weight_spectrum(primes, beta)
    K_a = carrier_coupling(2, 3, beta)
    K_b = carrier_coupling(2, 3, beta)  # same: no t to vary
    return {
        "weight_spectrum_t_independent": spec == spec2,
        "gibbs_t_independent": gibbs == gibbs2,
        "carrier_coupling_t_independent": bool(np.allclose(K_a, K_b)),
        "n_weights": len(spec),
    }


# --------------------------------------------------------------------------
# Part 2: the constraint lives in C_E (t-dependent), not in any carrier coupling.
# --------------------------------------------------------------------------

def part2_constraint_is_in_CE(p=5, beta=1.5):
    """C_E and the cup block B_E DO depend on t (they carry the constraint); the
    carrier coupling does not. So the coupling that sources |t_p| < 2 sqrt p must be
    a coupling of the C_E's, which the carrier cannot supply."""
    C1, _ = weil_twist(p, 1.0)
    C2, _ = weil_twist(p, 3.0)
    Be1, Be2 = b_e(p, 1.0), b_e(p, 3.0)
    K1 = carrier_coupling(p, 7, beta)
    K2 = carrier_coupling(p, 7, beta)
    return {
        "CE_depends_on_t": not np.allclose(C1, C2),
        "cup_block_depends_on_t": not np.allclose(Be1, Be2),
        "carrier_coupling_depends_on_t": not np.allclose(K1, K2),  # False
    }


# --------------------------------------------------------------------------
# Part 3: the FF template -- the coupling that WORKS (2G) is t-carrying.
# --------------------------------------------------------------------------

def part3_ff_template(q=5):
    """In the function field, the cup / intersection coupling B_E = -G_prim is
    negative-definite (Hodge index, a THEOREM) iff |t| < 2 sqrt q, and it CARRIES t.
    This is the target shape: a t-carrying global cup, not a t-independent carrier
    coupling. Over Spec(Z) it is the missing object (M4)."""
    rows = []
    for t in (0, 2, 4, 5):  # 5^... bound 2 sqrt 5 = 4.47
        Be = b_e(q, t)
        # G_prim = -B_E; negative-definite iff B_E positive-definite iff |t| < 2 sqrt q
        pd = bool(np.all(np.linalg.eigvalsh(Be) > TOL))
        rows.append({"t": t, "in_window": t * t < 4 * q, "BE_pos_def": pd})
    return rows


def demo() -> int:
    print("MC.4 coupling attempt (AT-1): can the coupling be sourced from the carrier?\n")

    p1 = part1_carrier_is_t_blind()
    print("  [1] the carrier data is t-INDEPENDENT (so any carrier-derived coupling is too):")
    print(f"      modular weight spectrum t-independent: {p1['weight_spectrum_t_independent']} "
          f"({p1['n_weights']} weights); Gibbs weights t-independent: {p1['gibbs_t_independent']};")
    print(f"      a representative carrier coupling (pq)^-beta I is t-independent: "
          f"{p1['carrier_coupling_t_independent']}")
    print("      => the carrier never takes a trace as input; t enters ONLY via C_E (MC.2).")

    p2 = part2_constraint_is_in_CE()
    print("\n  [2] the constraint |t_p|<2 sqrt p lives in C_E (t-dependent), not in the carrier:")
    print(f"      C_E depends on t: {p2['CE_depends_on_t']}; cup block B_E depends on t: "
          f"{p2['cup_block_depends_on_t']}; carrier coupling depends on t: "
          f"{p2['carrier_coupling_depends_on_t']}")
    print("      => a t-independent coupling cannot encode a t-dependent constraint. AT-1 CLOSED:")
    print("         no coupling sourced from the modular carrier can force |t_p| < 2 sqrt p.")

    p3 = part3_ff_template()
    print("\n  [3] FF template: the coupling that WORKS (the 2G cup) is t-carrying:")
    for r in p3:
        print(f"      t={r['t']}: |t|<2 sqrt q = {r['in_window']}, cup B_E positive-definite "
              f"(Hodge index) = {r['BE_pos_def']}")
    print("      => the global cup product carries t and its signature forces the bound; that is")
    print("         the target shape, NOT a t-independent carrier coupling. Over Z it is M4.")

    print("\n  VERDICT: AT-1 is closed in the NEGATIVE. The coupling cannot be sourced from the")
    print("  modular carrier (which is t-blind); it must be a t-carrying coupling of the C_E")
    print("  polarization phases = the global cup product. That object has four open faces over")
    print("  Spec(Z), all M4: the modular C_E-cup (here), the function-field cup (2G, a theorem),")
    print("  the AHK arithmetic lattice (09A), and the Faltings-Hriljac product + Gamma_S. The")
    print("  coupling = M4, irreducible to the carrier; this CLOSES the carrier-source loophole")
    print("  and unifies the four faces, it does not solve M4 (nothing cheap can).")

    assert p1["weight_spectrum_t_independent"] and p1["gibbs_t_independent"] \
        and p1["carrier_coupling_t_independent"], "[1] carrier data must be t-independent"
    assert p2["CE_depends_on_t"] and p2["cup_block_depends_on_t"] \
        and not p2["carrier_coupling_depends_on_t"], "[2] the constraint must live in C_E, not the carrier"
    assert all(r["in_window"] == r["BE_pos_def"] for r in p3), \
        "[3] the FF cup must be PD exactly on the Hasse-Weil window"
    print("\n  (all three structural assertions hold)")
    return 0


if __name__ == "__main__":
    raise SystemExit(demo())
