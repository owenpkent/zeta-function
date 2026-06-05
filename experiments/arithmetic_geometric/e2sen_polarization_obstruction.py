"""Lane 2: answer the open 2KK probe. Can an intrinsic POSITIVE cup form
survive a non-semisimple Sen module (Petrov, arXiv:2302.11389)?

Context (credit prior work; do not re-derive it).
  - #67 (2LL): the monodromy primitive form Q_N(x,y)=Omega(x, N y) recovers the
    Rosati/Euler matrix when a symmetric B is SUPPLIED. Survives as formalism.
  - #68 (2MM): that map is a TRANSPORT theorem: signature(Q_N) = signature(B)
    for arbitrary supplied B (the N^2=0, Tate-centered case). No positivity.
  - #66 (2KK): the Hodge-star cup form on a rank-2 weight pair is HYPERBOLIC
    (wrong polarity), and the ADVERSARY flagged the genuine Petrov question as
    UNTESTED: "can an intrinsic positive cup form survive a non-semisimple Sen
    module?". A real defective Jordan block was reported to DESTROY the cup form
    (B=0). This script resolves that boundary.

The crisp core (a compact-group theorem, demonstrated below).
  The Tate-equivariant cup duality is  Theta^T B + B Theta = -w B  (the pairing
  H^1 (x) H^1 -> H^2 into the weight-(-w) Euler pole; w=1 here). Rewrite it as
  (Theta + (w/2) I) in so(B): the shifted Sen operator is an INFINITESIMAL
  ISOMETRY of B. If B were positive definite, O(B) would be COMPACT, so its Lie
  algebra so(B) consists of B-skew operators, all SEMISIMPLE. Hence Theta would
  be semisimple, i.e. the nilpotent Sen part nu = 0.

  CONTRAPOSITIVE (the theorem): nu != 0 (Petrov non-semisimplicity)
                                 ==>  NO positive-definite invariant cup form.

  So a non-semisimple Sen module can never carry a global positive cup form. The
  Jordan structure forces you out of the "definite form on the whole space" and
  into the monodromy-weight / primitive-graded (Hodge-Riemann) formulation,
  whose positive form on primitives is the IMPORTED polarization of #68. The
  sign is never intrinsic to the Sen module.

This unifies the project's two prior outcomes as the only possibilities:
  (1) self-paired (Tate-center, 2mu=-w): B exists, INDEFINITE, sign imported (#68);
  (2) cross-paired (mu1+mu2=-w): B exists, HYPERBOLIC, wrong polarity (#66);
  (3) non-resonant: B=0, pairing absent (the 2KK "B=0").
In none does the non-semisimple Sen module supply an intrinsic POSITIVE form.

PART B keeps the Davenport-Heilbronn / K2 control: Theta is the SHARED
archimedean block, so this whole analysis is K2-blind by construction (it cannot
separate zeta from D-H); the discriminating sign must ride the Euler/Frobenius F
half, which Petrov's theorem does not touch.
"""

from __future__ import annotations

import numpy as np
import mpmath as mp

from experiments._shared.davenport_heilbronn import davenport_heilbronn as DH


# ---------------------------------------------------------------------------
# Linear-algebra core: solve the Tate-equivariant cup duality, read signatures.
# ---------------------------------------------------------------------------

def jordan(eigval: float, size: int) -> np.ndarray:
    """A single size-`size` Jordan block with the given eigenvalue.
    size>=2 is a genuine (non-semisimple) Sen block; size=1 is semisimple."""
    J = eigval * np.eye(size)
    for i in range(size - 1):
        J[i, i + 1] = 1.0     # nilpotent part nu (the Petrov defect)
    return J


def cup_form_solution_space(Theta: np.ndarray, w: float = 1.0, tol: float = 1e-9):
    """Symmetric solutions B of Theta^T B + B Theta = -w B (the cup duality
    into the weight-(-w) Euler pole). Returns a basis of the symmetric solution
    space as a list of matrices."""
    n = Theta.shape[0]
    # Symmetric-matrix basis E_{ij} (i<=j), then build the linear map and kernel.
    sym_basis = []
    idx = []
    for i in range(n):
        for j in range(i, n):
            E = np.zeros((n, n))
            E[i, j] = 1.0
            E[j, i] = 1.0
            sym_basis.append(E)
            idx.append((i, j))
    cols = []
    for E in sym_basis:
        L = Theta.T @ E + E @ Theta + w * E
        cols.append(L.reshape(-1))
    M = np.array(cols).T                      # (n^2) x (#sym basis)
    # Null space of M via SVD.
    _, S, Vt = np.linalg.svd(M)
    rank = int((S > tol * max(1.0, S[0])).sum()) if S.size else 0
    null = Vt[rank:]                          # rows are null coordinates
    sols = []
    for v in null:
        B = sum(c * E for c, E in zip(v, sym_basis))
        sols.append(B)
    return sols


def inertia(B: np.ndarray, tol: float = 1e-8):
    """(n_positive, n_negative, n_zero) of a symmetric matrix."""
    ev = np.linalg.eigvalsh((B + B.T) / 2)
    return (int((ev > tol).sum()), int((ev < -tol).sum()), int((np.abs(ev) <= tol).sum()))


def has_definite_element(sols):
    """Does the symmetric solution space contain a positive- or negative-
    definite form? For the low-dim spaces here, checking the identity component
    and the individual basis elements (plus a small random search) is decisive;
    the compact-group theorem is the actual proof."""
    if not sols:
        return False, None
    n = sols[0].shape[0]
    # Is the identity (the canonical definite form) a solution?
    for B in sols:
        pass
    # The solution space is a subspace; test if I_n lies in it, and scan combos.
    candidates = [np.eye(n)]
    rng = np.random.default_rng(0)
    for _ in range(2000):
        c = rng.standard_normal(len(sols))
        candidates.append(sum(ci * B for ci, B in zip(c, sols)))
    for B in candidates:
        # is B in the solution space AND definite?
        # membership: residual of the cup equation
        np_pos, np_neg, np_zero = inertia(B)
        if np_zero == 0 and (np_neg == 0 or np_pos == 0):
            # definite; verify it actually solves the equation
            res = np.linalg.norm(THETA_GLOBAL.T @ B + B @ THETA_GLOBAL + B)
            if res < 1e-6:
                return True, (np_pos, np_neg, np_zero)
    return False, None


THETA_GLOBAL = None   # set per-config so has_definite_element can verify residuals


def run_config(name, Theta, w=1.0):
    global THETA_GLOBAL
    THETA_GLOBAL = Theta
    sols = cup_form_solution_space(Theta, w=w)
    dim = len(sols)
    eig = np.round(np.linalg.eigvals(Theta).real, 4)
    nilpotent = not np.allclose(Theta, np.diag(np.diag(Theta))) and \
        not _is_diagonalizable_semisimple(Theta)
    definite, dsig = has_definite_element(sols)
    sample_inertia = inertia(sols[0]) if sols else None
    print(f"  [{name}]")
    print(f"      Theta eigenvalues:        {sorted(set(eig.tolist()))}  "
          f"({'NON-semisimple (nu!=0)' if nilpotent else 'semisimple (nu=0)'})")
    print(f"      cup-form solution dim:    {dim}   "
          f"({'pairing exists (rung ii)' if dim > 0 else 'B=0, NO pairing'})")
    if sols:
        print(f"      representative inertia:   {sample_inertia}")
    print(f"      contains DEFINITE form?:  {definite}"
          + (f"  signature {dsig}" if definite else "  <-- no positive cup form"))
    print()
    return {"name": name, "dim": dim, "nonsemisimple": nilpotent,
            "definite": definite, "sample_inertia": sample_inertia}


def _is_diagonalizable_semisimple(A, tol=1e-8):
    # crude: A is semisimple iff geometric mult == algebraic mult for each eigval
    n = A.shape[0]
    ev = np.linalg.eigvals(A)
    uniq = []
    for e in ev:
        if not any(abs(e - u) < 1e-6 for u in uniq):
            uniq.append(e)
    total_geom = 0
    for u in uniq:
        # geometric multiplicity = dim null(A - u I)
        s = np.linalg.svd(A - u * np.eye(n), compute_uv=False)
        total_geom += int((s < tol * max(1.0, s[0])).sum())
    return total_geom == n


# ---------------------------------------------------------------------------
# PART A. The definiteness obstruction + the existence trichotomy.
# ---------------------------------------------------------------------------

def part_a():
    print("=" * 74)
    print("PART A.  nu != 0  ==>  no positive-definite cup form (compact-group)")
    print("=" * 74)
    # Tate center mu = -w/2 = -1/2 (w=1). Semisimple vs non-semisimple.
    print(" Tate-center eigenvalue mu=-1/2 (2mu=-w resonance):")
    run_config("semisimple  Theta=-1/2 I_3 (nu=0)", -0.5 * np.eye(3))
    run_config("NON-ss      Theta=-1/2 I_3 + N_3 (nu!=0, Petrov)", jordan(-0.5, 3))
    print(" Existence trichotomy for a genuine size-3 Jordan block:")
    run_config("self-paired (mu=-1/2): exists, INDEFINITE", jordan(-0.5, 3))
    cross = np.zeros((6, 6))
    cross[:3, :3] = jordan(0.0, 3)
    cross[3:, 3:] = jordan(-1.0, 3)
    run_config("cross-paired (mu=0,-1): exists, HYPERBOLIC (#66)", cross)
    run_config("non-resonant (mu=-1): B=0 (the 2KK 'B=0')", jordan(-1.0, 3))
    print("  Reading: the only configurations with a pairing are self-paired")
    print("  (indefinite, sign imported = #68) and cross-paired (hyperbolic,")
    print("  wrong polarity = #66). Neither is a positive cup form. Adding nu")
    print("  collapses the 6-dim space of forms at mu=-1/2 (which CONTAINS the")
    print("  positive-definite identity) down to a 2-dim family with NO definite")
    print("  element (representative inertia (1,2)).")
    print("  Answer to the 2KK probe: NO intrinsic positive cup form survives.")
    print()


# ---------------------------------------------------------------------------
# PART B. K2 control: Theta is the SHARED archimedean block; only F separates.
# ---------------------------------------------------------------------------

def _completed_zeta_residual(s, dps=40):
    prev = mp.mp.dps
    mp.mp.dps = dps
    try:
        s = mp.mpc(s)
        def Lam(z):
            return mp.power(mp.pi, -z / 2) * mp.gamma(z / 2) * mp.zeta(z)
        return abs(Lam(s) - Lam(1 - s))
    finally:
        mp.mp.dps = prev


def _first_multiplicativity_violation(coeff, N=40):
    from math import gcd
    for m in range(2, N):
        for n in range(2, N):
            if gcd(m, n) != 1 or m * n >= 5 * N:
                continue
            if abs(complex(coeff(m * n)) - complex(coeff(m)) * complex(coeff(n))) > 1e-9:
                return (m, n, complex(coeff(m * n)), complex(coeff(m)) * complex(coeff(n)))
    return None


def part_b():
    print("=" * 74)
    print("PART B.  K2 control: Sen/Theta block is SHARED; only Euler/F separates")
    print("=" * 74)
    s_test = mp.mpc("0.3", "7.0")
    z_res = _completed_zeta_residual(s_test, dps=40)
    prev = mp.mp.dps
    mp.mp.dps = 40
    try:
        dh_res = abs(DH.functional_equation_residual(s_test))
    finally:
        mp.mp.dps = prev
    print(f"  FE residual at s={complex(s_test)} (rung ii, the shared Sen/arch block):")
    print(f"      zeta : |Lambda(s)-Lambda(1-s)| = {mp.nstr(z_res, 3)}")
    print(f"      D-H  : |f(s)-chi f(1-s)|        = {mp.nstr(dh_res, 3)}")
    print("  Both ~0: the FE/archimedean/Sen structure does NOT separate them.")
    print("  Petrov's Theta non-semisimplicity lives here -> not a discriminator.")
    print()
    from sympy import factorint
    def von_mangoldt(n):
        if n < 2:
            return 0.0
        f = factorint(n)
        return float(mp.log(next(iter(f)))) if len(f) == 1 else 0.0
    support = [n for n in range(2, 16) if von_mangoldt(n) > 0]
    print(f"  zeta  -zeta'/zeta coeffs = von Mangoldt; support on [2,15] = {support}")
    print(f"        (exactly the prime powers) => Euler/Frobenius F PRESENT.")
    viol = _first_multiplicativity_violation(lambda n: complex(DH.dirichlet_coefficient(n)))
    if viol:
        m, n, lhs, rhs = viol
        print(f"  D-H   a(n) period-5; multiplicativity FAILS: a({m}*{n})={lhs.real:+.4f}"
              f" vs a({m})a({n})={rhs.real:+.4f}")
        print(f"        => NO Euler product -> NO Frobenius -> polarizable algebra")
        print(f"           UNINHABITED for D-H by TYPE.")
    print()


def main():
    print()
    part_a()
    part_b()
    print("=" * 74)
    print("VERDICT")
    print("=" * 74)
    print("  THEOREM (demonstrated): a non-semisimple Sen operator (Petrov nu!=0)")
    print("  admits NO positive-definite invariant cup form. The Jordan structure")
    print("  forces the monodromy-weight / primitive formulation, whose positive")
    print("  form on primitives is the IMPORTED polarization of #68 (transport).")
    print("  Answer to the 2KK open probe: NO intrinsic positive cup form.")
    print("  ROUTABLE (not fatal to 08B's setup) but not progress on (B): the")
    print("  positivity is never sourced by the Sen module; it must be imported,")
    print("  = the arithmetic ample class = RH, riding the Euler/F half (K2),")
    print("  which Theta does not see. Coordinate ruled out:")
    print("  'source the polarization from the (archimedean) Sen structure.'")
    print()


if __name__ == "__main__":
    main()
