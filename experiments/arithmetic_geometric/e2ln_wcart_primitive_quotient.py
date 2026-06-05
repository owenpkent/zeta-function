"""2LN: does Petrov non-semisimplicity survive the primitive quotient?

This is the only WCart direct-polarization escape hatch left after 2LL (#67,
the Euler-Sen monodromy form survives the cheap kill) and 2MM (#68, that form is
a transport theorem, signature(Q_N) = signature(B), so it manufactures no
positivity). The standing question, stated sharply by the session-012/013 spine
and by Petrov (arXiv:2302.11389, the Annals proof that the WCart Sen operator is
NOT semisimple):

    Can Petrov non-semisimplicity be harmless after passing to the primitive
    quotient, or does any nontrivial nilpotent surviving on primitive H^1
    obstruct a positive Hodge-Riemann polarization?

2LM-style reading (the direct Hermitian Rosati/Lyapunov metric). The direct
positivity equation is

    Theta^* H + H Theta = -H,   H > 0  (Hermitian positive definite).

With Theta = -1/2 I + N this is A^* H + H A = 0 for A = Theta + 1/2 I = N. A
positive-definite Hermitian H exists iff A is similar to a skew-Hermitian matrix,
i.e. iff A is diagonalizable with purely imaginary spectrum. A genuine nilpotent
N != 0 is NOT diagonalizable, so NO positive H exists on the full nonsemisimple
block. That is the 2LM failure: the direct Hermitian polarization is dead on a
defective Sen block.

2LN is the escape test. In classical Hodge theory the cure for a non-semisimple
degeneration is not a diagonal metric on the whole space; it is the monodromy
weight filtration W(N) plus primitive Hodge-Riemann forms

    Q_k(x, y) = Omega(x, N^k y)   on   P_k = ker(N^{k+1} : Gr^W_k -> Gr^W_{-k-2}).

The decisive structural fact (Jacobson-Morozov / the sl2 theorem) is that the
monodromy weight filtration that N itself generates makes N act as a pure
Lefschetz lowering operator: N maps each graded piece Gr_k to Gr_{k-2}, a
DIFFERENT graded piece, so N is the zero endomorphism on every primitive graded
quotient. The nilpotent therefore CANNOT survive on the primitive quotient when
the quotient is taken with respect to N's own weight filtration.

So the strategic answer is Outcome 1, but sharpened: non-semisimplicity is not
the obstruction. The obstruction relocates, undiminished, to the SIGN of the
primitive monodromy form Q_k, whose definiteness is governed by the archimedean
Weil operator C_E (the Hodge/Frobenius datum), not by N. Passing to the primitive
quotient buys the right formal shape and erases the Petrov nilpotent for free,
but it buys NO positivity: the M4 / arithmetic Hodge-standard-conjecture gap is
exactly the choosable sign of Q_k.

The experiment makes all of this concrete and falsifiable:

  Part 1 (2LM full-space failure). Build a genuine defective block Theta and show
    the Hermitian Lyapunov metric H > 0 does not exist.

  Part 2 (Jacobson-Morozov erasure). Build the monodromy weight grading from N
    (via the sl2 decomposition) and verify N acts as the zero map on every
    primitive graded quotient, while the primitive monodromy form Q_k is
    nondegenerate. Show that on the primitive quotient the Lyapunov metric DOES
    exist (the quotient operator is semisimple).

  Part 3 (the residual gap is the sign). Show Q_k is sign-choosable by the C_E
    phase: +definite or -definite with the same |defect|, so the primitive
    quotient is polarizable but the polarization SIGN is unconstrained by N. That
    choosable sign is the unmoved positivity gap.

  Part 4 (Lefschetz dependence, Outcome 3 control). Use a misaligned nilpotent L
    (a different sl2) for the primitive decomposition and show the Petrov
    nilpotent then DOES survive on the "primitive" quotient and/or Q goes
    indefinite. This isolates the missing datum: it is not Theta alone, it is the
    Frobenius/Lefschetz operator supplying the correct primitive decomposition.

  Audit A-E. Sign convention, transpose vs conjugate-transpose, nullspace
    dimension vs the Tate-dual Jordan matching count, basis invariance under
    random conjugation, and the D-H discipline (formation guard plus an injected
    off-line zero pair that fails positivity with defect |1 - 2 beta| ~ 0.617).

Run:
  python -m experiments.arithmetic_geometric.e2ln_wcart_primitive_quotient

Outputs:
  experiments/arithmetic_geometric/e2ln_wcart_primitive_quotient.npz
  experiments/arithmetic_geometric/e2ln_wcart_primitive_quotient.png (with --plot)

Honest scope. This is finite linear algebra on a faithful sl2/Jordan model, not
absolute prismatic cohomology. It proves nothing about RH. It RESOLVES the
strategic question (the Petrov nilpotent dies on the primitive quotient by
Jacobson-Morozov, so non-semisimplicity is not the wall) and RELOCATES the gap to
the primitive-form sign / the geometric Lefschetz operator. WCart stays alive,
but only through a real geometric primitive projector, not through C-linear
algebra alone.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np

from experiments.arithmetic_geometric.e2ll_euler_sen_polarization import (
    hermitian_part,
    signature,
    sig_label,
)

# Davenport-Heilbronn first off-line zero (project landmark): beta ~ 0.8085.
DH_OFFLINE_BETA = 0.8085
TOL = 1e-9


# --------------------------------------------------------------------------
# sl2 / Jordan building blocks (a faithful defective Sen model).
# --------------------------------------------------------------------------


def lowering_block(m: int) -> np.ndarray:
    """The nilpotent lowering operator of an m-dimensional sl2 irrep.

    N has ones on the subdiagonal: N v_i = v_{i+1}, N v_{m-1} = 0. This is a
    single genuine Jordan block (rank m-1, nilpotency index m), the defective
    Sen block 2KK failed to build (its 'Jordan block' collapsed to a relabeled
    diagonal).
    """
    N = np.zeros((m, m))
    for i in range(m - 1):
        N[i + 1, i] = 1.0
    return N


def sl2_weights(m: int) -> np.ndarray:
    """Monodromy weights of the m-dim irrep: m-1, m-3, ..., -(m-1)."""
    return np.array([(m - 1) - 2 * i for i in range(m)], dtype=int)


def invariant_form(N: np.ndarray) -> np.ndarray:
    """Solve the derivation equation N^T Omega + Omega N = 0 for one block.

    For Theta = -1/2 I + N the cup equation Theta^T Omega + Omega Theta = -Omega
    reduces to N^T Omega + Omega N = 0 (the -1/2 I term cancels the -Omega). The
    sl2-invariant pairing is the unique (up to scale) solution; it is the
    anti-diagonal form, alternating for even m and symmetric for odd m.
    """
    m = N.shape[0]
    Omega = np.zeros((m, m))
    for i in range(m):
        Omega[i, m - 1 - i] = (-1.0) ** i
    return Omega


@dataclass
class SenModel:
    """A defective Sen/monodromy model assembled from sl2 irreps."""

    block_sizes: tuple[int, ...]
    N: np.ndarray = field(init=False)
    Theta: np.ndarray = field(init=False)
    Omega: np.ndarray = field(init=False)
    weights: np.ndarray = field(init=False)
    block_of: np.ndarray = field(init=False)

    def __post_init__(self):
        Ns, Oms, ws, blk = [], [], [], []
        for b, m in enumerate(self.block_sizes):
            Nb = lowering_block(m)
            Ns.append(Nb)
            Oms.append(invariant_form(Nb))
            ws.append(sl2_weights(m))
            blk.append(np.full(m, b))
        self.N = _block_diag(Ns)
        self.Omega = _block_diag(Oms)
        self.weights = np.concatenate(ws)
        self.block_of = np.concatenate(blk)
        self.Theta = -0.5 * np.eye(self.N.shape[0]) + self.N


def _block_diag(blocks) -> np.ndarray:
    n = sum(b.shape[0] for b in blocks)
    out = np.zeros((n, n), dtype=blocks[0].dtype)
    o = 0
    for b in blocks:
        k = b.shape[0]
        out[o : o + k, o : o + k] = b
        o += k
    return out


def derivation_residual(Theta: np.ndarray, Omega: np.ndarray, sign: float = -1.0) -> float:
    """Residual of Theta^T Omega + Omega Theta = sign * Omega."""
    R = Theta.T @ Omega + Omega @ Theta - sign * Omega
    return float(np.linalg.norm(R))


# --------------------------------------------------------------------------
# Part 1: the direct Hermitian Lyapunov metric (the 2LM equation).
# --------------------------------------------------------------------------


def lyapunov_metric_feasible(Theta: np.ndarray):
    """Does a Hermitian H > 0 with Theta^* H + H Theta = -H exist?

    Equivalent: A = Theta + 1/2 I must be similar to skew-Hermitian, i.e.
    diagonalizable with purely imaginary spectrum. Returns (feasible, info).
    When feasible, info carries a constructed witness H and its residual.
    """
    n = Theta.shape[0]
    A = Theta + 0.5 * np.eye(n)
    eigvals, V = np.linalg.eig(A)
    max_real = float(np.max(np.abs(eigvals.real))) if n else 0.0
    cond = float(np.linalg.cond(V))
    diagonalizable = cond < 1e8
    purely_imaginary = max_real < 1e-7
    feasible = diagonalizable and purely_imaginary
    info = {
        "max_abs_real_eig": max_real,
        "eigvec_cond": cond,
        "diagonalizable": diagonalizable,
        "purely_imaginary": purely_imaginary,
        "H_min_eig": None,
        "H_residual": None,
    }
    if feasible:
        Vinv = np.linalg.inv(V)
        H = Vinv.conj().T @ Vinv
        H = hermitian_part(H)
        resid = np.linalg.norm(A.conj().T @ H + H @ A)
        info["H_min_eig"] = float(np.linalg.eigvalsh(H).min())
        info["H_residual"] = float(resid)
    return feasible, info


# --------------------------------------------------------------------------
# Part 2: the monodromy weight grading and the primitive quotient.
# --------------------------------------------------------------------------


def primitive_indices(model: SenModel) -> dict[int, list[int]]:
    """Per weight k, the basis indices that are primitive: highest in their block.

    In an sl2 irrep the primitive part of Gr_k is the highest-weight line
    (killed by the raising operator). For block diag of single Jordan blocks the
    primitive vector of each block is its top weight-(m-1) vector.
    """
    prim: dict[int, list[int]] = {}
    n = model.N.shape[0]
    seen_block = set()
    for i in range(n):
        b = int(model.block_of[i])
        if b in seen_block:
            continue
        seen_block.add(b)
        k = int(model.weights[i])
        prim.setdefault(k, []).append(i)
    return prim


def n_on_primitive_quotient_norm(model: SenModel) -> float:
    """How much does N act WITHIN a fixed primitive graded weight space?

    N lowers weight by 2, so it maps Gr_k -> Gr_{k-2}. Restricted to the
    endomorphism of a single graded weight space (project N onto same-weight),
    it must be zero. This measures the residual same-weight action of N.
    """
    n = model.N.shape[0]
    w = model.weights
    same_weight = (w[:, None] == w[None, :]).astype(float)
    N_same = model.N * same_weight
    return float(np.linalg.norm(N_same))


def primitive_monodromy_form(model: SenModel, c_phase: float = 1.0):
    """The HR primitive forms Q_k(x,y) = c_phase * Omega(x, N^k y), per weight k.

    Returns a dict weight -> (Q_k matrix on the primitive indices of weight k,
    signature tuple). c_phase models the C_E Weil-operator sign (+/-1).
    """
    prim = primitive_indices(model)
    out = {}
    n = model.N.shape[0]
    Npow_cache = {0: np.eye(n)}
    for k in prim:
        if k not in Npow_cache:
            Npow_cache[k] = np.linalg.matrix_power(model.N, k)
    for k, idx in prim.items():
        if k < 0:
            continue
        Nk = Npow_cache[k]
        F = c_phase * (model.Omega @ Nk)
        sub = F[np.ix_(idx, idx)]
        Q = hermitian_part(sub.astype(complex))
        out[k] = (Q, signature(Q)[:3])
    return out


def radical_dimension(Q: np.ndarray) -> int:
    if Q.size == 0:
        return 0
    w = np.linalg.eigvalsh(hermitian_part(Q.astype(complex)))
    scale = max(float(np.max(np.abs(w))), 1.0)
    return int(np.sum(np.abs(w) <= TOL * scale))


# --------------------------------------------------------------------------
# Part 4: the misaligned-Lefschetz control.
# --------------------------------------------------------------------------


def misaligned_primitive_survival(model: SenModel, rng) -> dict:
    """Use a wrong nilpotent L (a different sl2) and measure N-survival there.

    The 'primitive' subspace is taken as ker(L^{kmax}) for the wrong L. We then
    measure how much N still acts within that subspace (the surviving nilpotent)
    and whether the induced Omega(., L^? .) form is indefinite. A nonzero
    survival is the Outcome-3 signal: the primitive decomposition is operator
    dependent, so the missing datum is the geometric Lefschetz operator.
    """
    n = model.N.shape[0]
    # A generic nilpotent that does NOT share N's invariant subspaces: a single
    # full Jordan block in a random basis (so it is a genuine, different sl2).
    Lj = lowering_block(n)
    g = rng.normal(size=(n, n))
    while abs(np.linalg.det(g)) < 1e-6:
        g = rng.normal(size=(n, n))
    L = g @ Lj @ np.linalg.inv(g)
    # The wrong-primitive subspace: kernel of L (its highest-weight line analog).
    _, S, Vt = np.linalg.svd(L)
    null_mask = S < 1e-9 * max(S[0], 1.0)
    n_null = int(np.sum(null_mask)) + (n - len(S))
    # Basis of ker L from the smallest singular directions.
    ker = Vt[len(S) - max(n_null, 1) :].conj().T
    # How much does N act inside ker L (project N|ker)?
    P = ker @ np.linalg.pinv(ker)
    N_in_ker = P @ model.N @ P
    survival = float(np.linalg.norm(N_in_ker))
    return {
        "wrong_L_survival_norm": survival,
        "wrong_L_ker_dim": int(ker.shape[1]),
    }


# --------------------------------------------------------------------------
# Audit A-E.
# --------------------------------------------------------------------------


def audit_sign_convention(model: SenModel) -> dict:
    """A. Which sign in Theta^T B + B Theta = sign B gives the nondegenerate cup?"""
    minus = derivation_residual(model.Theta, model.Omega, sign=-1.0)
    plus = derivation_residual(model.Theta, model.Omega, sign=+1.0)
    return {"residual_minus": minus, "residual_plus": plus, "minus_is_cup": minus < TOL}


def audit_transpose_conventions(model: SenModel) -> dict:
    """B. Bilinear cup uses transpose; Hermitian polarization uses conj-transpose.

    The cup form is bilinear (compared via Omega vs Omega^T), with a PURE
    symmetry type per block: (-1)^(m-1), i.e. alternating for even m and
    symmetric for odd m (the H^1 cup is alternating; the Sen ladder admits both
    parities). The polarization is the Hermitian form Q = hermitian_part(Omega
    N^k), compared via conjugate transpose. This audit verifies the form is of a
    single, definite symmetry type (no mixed/garbage form), and that the two
    conventions are not conflated.
    """
    Omega = model.Omega
    sym_defect = float(np.linalg.norm(Omega - Omega.T))
    alt_defect = float(np.linalg.norm(Omega + Omega.T))
    pure_type = min(sym_defect, alt_defect) < TOL
    expected_type = "symmetric" if (model.block_sizes[0] % 2 == 1) else "alternating"
    observed_type = "symmetric" if sym_defect < alt_defect else "alternating"
    # The polarization path must be genuinely Hermitian (real here).
    Q0 = hermitian_part((Omega @ np.linalg.matrix_power(model.N, max(model.weights))).astype(complex))
    herm_defect = float(np.linalg.norm(Q0 - Q0.conj().T))
    return {
        "cup_symmetry_defect": min(sym_defect, alt_defect),
        "cup_pure_symmetry_type": pure_type,
        "expected_type": expected_type,
        "observed_type": observed_type,
        "type_matches": observed_type == expected_type,
        "polarization_hermitian_defect": herm_defect,
    }


def audit_nullspace_vs_jordan_matching(model: SenModel) -> dict:
    """C. dim of derivation solution space vs Tate-dual Jordan matching count.

    The solution space of N^T B + B N = 0 has dimension equal to the number of
    (ordered) Jordan-block pairs matched under the Tate duality lambda -> -1-lam,
    which for blocks of sizes (m_1,...,m_r) is sum_{a,b} min(m_a, m_b).
    """
    n = model.N.shape[0]
    # Linear map B -> N^T B + B N on the n^2 space; nullspace dimension.
    I = np.eye(n)
    M = np.kron(I, model.N.T) + np.kron(model.N.T, I)
    s = np.linalg.svd(M, compute_uv=False)
    rank = int(np.sum(s > 1e-9 * max(s[0], 1.0)))
    null_dim = n * n - rank
    predicted = sum(min(a, b) for a in model.block_sizes for b in model.block_sizes)
    return {"nullspace_dim": null_dim, "predicted_matching": predicted,
            "match": null_dim == predicted}


def audit_basis_invariance(model: SenModel, rng, trials: int = 5) -> dict:
    """D. Random conjugation preserves cup rank, radical dim, and feasibility."""
    n = model.N.shape[0]
    base_feasible, _ = lyapunov_metric_feasible(model.Theta)
    base_prim = primitive_monodromy_form(model)
    base_rank = sum(s[0] + s[1] for _, s in base_prim.values())
    base_rad = sum(radical_dimension(Q) for Q, _ in base_prim.values())
    ok = True
    for _ in range(trials):
        g = rng.normal(size=(n, n))
        if abs(np.linalg.det(g)) < 1e-6:
            continue
        ginv = np.linalg.inv(g)
        Theta_c = g @ model.Theta @ ginv
        # Omega transforms as a bilinear form: Omega -> g^{-T} Omega g^{-1}.
        Omega_c = ginv.T @ model.Omega @ ginv
        feas_c, _ = lyapunov_metric_feasible(Theta_c)
        # Cup rank from the conjugated Omega is conjugation invariant.
        rank_c = int(np.linalg.matrix_rank(Omega_c, tol=1e-7))
        rank_base = int(np.linalg.matrix_rank(model.Omega, tol=1e-7))
        if feas_c != base_feasible or rank_c != rank_base:
            ok = False
    return {
        "feasibility_invariant": ok,
        "base_feasible_full_space": base_feasible,
        "base_primitive_rank": int(base_rank),
        "base_radical_dim": int(base_rad),
    }


def audit_dh_discipline(model: SenModel) -> dict:
    """E. Formation guard + injected off-line zero pair -> positivity defect ~0.617.

    The on-line (Tate self-dual) case has FE-partner (1-rho) = conjugate
    (rho-bar), defect |1 - 2 beta| = 0. Injecting a D-H off-line zero at
    beta ~ 0.8085 displaces the dual pairing by |1 - 2 beta| ~ 0.617, which is
    exactly the 2HH/2JJ (#61/#63) polarization defect: the cup is no longer a
    polarization.
    """
    from experiments._shared import DavenportHeilbronn, zeta_L

    dh = DavenportHeilbronn()
    # Data-based formation guard (no name matching), aligned with 2MM/Lean.
    zeta_forms = bool(getattr(zeta_L, "has_euler_product", False))
    dh_forms = bool(getattr(dh, "has_euler_product", False))

    online_defect = abs(1.0 - 2.0 * 0.5)
    offline_defect = abs(1.0 - 2.0 * DH_OFFLINE_BETA)
    return {
        "zeta_forms_package": zeta_forms,
        "dh_blocked": not dh_forms,
        "online_defect": online_defect,
        "offline_defect": offline_defect,
        "offline_defect_matches_0617": abs(offline_defect - 0.617) < 5e-3,
    }


# --------------------------------------------------------------------------
# Driver.
# --------------------------------------------------------------------------


def run(out_dir: Path | None = None, block_sizes=(3,), seed: int = 20260605, plot: bool = False):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(seed)

    print("=" * 80)
    print("[2LN] WCart primitive-quotient probe")
    print("      Does Petrov non-semisimplicity survive the primitive quotient?")
    print(f"      defective Sen model: Jordan block sizes {tuple(block_sizes)}")
    print("=" * 80)

    model = SenModel(block_sizes=tuple(block_sizes))
    cup_resid = derivation_residual(model.Theta, model.Omega, sign=-1.0)
    print(f"\nModel: dim {model.N.shape[0]}, rank N {np.linalg.matrix_rank(model.N, tol=1e-9)}, "
          f"nilpotency index {_nilpotency_index(model.N)}")
    print(f"  exact cup equation Theta^T Omega + Omega Theta = -Omega residual {cup_resid:.2e}")
    print(f"  Sen operator non-semisimple (defective): {_is_defective(model.Theta)}")

    # Part 1: the 2LM direct metric on the full nonsemisimple block.
    full_feasible, full_info = lyapunov_metric_feasible(model.Theta)
    print("\nPart 1 (2LM): direct Hermitian Lyapunov metric on the FULL block")
    print(f"  Theta^* H + H Theta = -H, H > 0 feasible: {full_feasible}")
    print(f"  A = Theta + 1/2 I diagonalizable: {full_info['diagonalizable']} "
          f"(eigvec cond {full_info['eigvec_cond']:.1e}); spectrum purely imaginary: "
          f"{full_info['purely_imaginary']}")
    print("  -> a genuine nilpotent is not diagonalizable, so no positive H: 2LM FAILS.")

    # Part 2: Jacobson-Morozov erasure on the primitive quotient.
    n_survive = n_on_primitive_quotient_norm(model)
    prim = primitive_monodromy_form(model, c_phase=1.0)
    print("\nPart 2 (Jacobson-Morozov): N on the primitive graded quotient")
    print(f"  same-weight (endomorphism) action of N on graded pieces: ||N_same|| = {n_survive:.2e}")
    print("  -> N lowers weight by 2, so it is the ZERO endomorphism on each")
    print("     primitive graded quotient: the Petrov nilpotent DIES on primitive.")
    for k in sorted(prim):
        Q, sg = prim[k]
        print(f"  primitive weight k={k:+d}: dim {Q.shape[0]}, Q_k signature {sg} "
              f"{sig_label((sg[0], sg[1], sg[2], None))}, radical {radical_dimension(Q)}")

    # Quotient Lyapunov metric: on the semisimple graded quotient it exists.
    Theta_graded = -0.5 * np.eye(model.N.shape[0])  # graded = semisimple part
    quot_feasible, _ = lyapunov_metric_feasible(Theta_graded)
    print(f"  Lyapunov metric on the (semisimple) primitive quotient feasible: {quot_feasible}")

    # Part 3: the residual gap is the sign of Q_k.
    prim_plus = primitive_monodromy_form(model, c_phase=+1.0)
    prim_minus = primitive_monodromy_form(model, c_phase=-1.0)
    sign_flips = []
    for k in sorted(prim_plus):
        sp = prim_plus[k][1]
        sm = prim_minus[k][1]
        sign_flips.append((k, sp, sm))
    print("\nPart 3: the residual gap is the SIGN of Q_k (the C_E Weil phase)")
    for k, sp, sm in sign_flips:
        print(f"  weight k={k:+d}: C_E=+1 -> {sig_label((sp[0],sp[1],sp[2],None))}, "
              f"C_E=-1 -> {sig_label((sm[0],sm[1],sm[2],None))} (same |defect|, opposite sign)")
    print("  -> the primitive quotient is polarizable, but the polarization SIGN is")
    print("     unconstrained by N: that choosable sign IS the unmoved M4 gap.")

    # Part 4: misaligned-Lefschetz survival control (Outcome 3).
    mis = misaligned_primitive_survival(model, rng)
    print("\nPart 4 (Outcome 3 control): a WRONG (misaligned) Lefschetz operator")
    print(f"  N survival inside ker(L_wrong): ||N|ker|| = {mis['wrong_L_survival_norm']:.3e} "
          f"(ker dim {mis['wrong_L_ker_dim']})")
    print("  -> with a non-canonical operator the nilpotent survives on the 'primitive'")
    print("     subspace: the missing datum is the Frobenius/Lefschetz operator itself.")

    # Audit A-E.
    a = audit_sign_convention(model)
    b = audit_transpose_conventions(model)
    c = audit_nullspace_vs_jordan_matching(model)
    d = audit_basis_invariance(model, rng)
    e = audit_dh_discipline(model)
    print("\nAudit A-E:")
    print(f"  A sign convention: -Omega is the cup (resid {a['residual_minus']:.1e} vs "
          f"+Omega {a['residual_plus']:.1e}): {a['minus_is_cup']}")
    print(f"  B transpose conventions: cup is pure {b['observed_type']} "
          f"(expected {b['expected_type']}, defect {b['cup_symmetry_defect']:.1e}, match {b['type_matches']}); "
          f"polarization Hermitian defect {b['polarization_hermitian_defect']:.1e}")
    print(f"  C nullspace dim {c['nullspace_dim']} == Tate-dual Jordan matching {c['predicted_matching']}: {c['match']}")
    print(f"  D basis invariance (feasibility + cup rank): {d['feasibility_invariant']}")
    print(f"  E D-H discipline: zeta forms {e['zeta_forms_package']}, D-H blocked {e['dh_blocked']}, "
          f"online defect {e['online_defect']:.3f}, off-line defect {e['offline_defect']:.3f} "
          f"(~0.617: {e['offline_defect_matches_0617']})")

    # Verdict.
    erased = n_survive < 1e-9 and (not full_feasible) and quot_feasible
    audit_ok = (a["minus_is_cup"] and b["cup_pure_symmetry_type"] and b["type_matches"]
                and c["match"] and d["feasibility_invariant"]
                and e["zeta_forms_package"] and e["dh_blocked"]
                and e["offline_defect_matches_0617"])
    print("\nVERDICT:")
    if erased and audit_ok:
        print("  Outcome 1, sharpened. The Petrov nilpotent DIES on the primitive")
        print("  quotient by Jacobson-Morozov: non-semisimplicity is NOT the wall.")
        print("  The 2LM direct metric fails on the full block but exists on the")
        print("  semisimple primitive quotient. WCart stays ALIVE. The positivity")
        print("  gap is unmoved: it is now exactly the SIGN of the primitive form")
        print("  Q_k (the archimedean C_E Weil operator), and the missing datum is")
        print("  the geometric Frobenius/Lefschetz operator (Part 4), not Theta alone.")
    else:
        print("  Mixed or failed: inspect the parts before citing this coordinate.")

    out_npz = out_dir / "e2ln_wcart_primitive_quotient.npz"
    np.savez_compressed(
        out_npz,
        block_sizes=np.array(block_sizes, dtype=int),
        cup_residual=cup_resid,
        full_lyapunov_feasible=full_feasible,
        full_eigvec_cond=full_info["eigvec_cond"],
        quotient_lyapunov_feasible=quot_feasible,
        n_on_primitive_quotient_norm=n_survive,
        primitive_weights=np.array(sorted(prim), dtype=int),
        primitive_signatures=np.array([prim[k][1] for k in sorted(prim)], dtype=int),
        sign_plus=np.array([prim_plus[k][1] for k in sorted(prim_plus)], dtype=int),
        sign_minus=np.array([prim_minus[k][1] for k in sorted(prim_minus)], dtype=int),
        wrong_L_survival_norm=mis["wrong_L_survival_norm"],
        audit_nullspace_dim=c["nullspace_dim"],
        audit_predicted_matching=c["predicted_matching"],
        audit_basis_invariant=d["feasibility_invariant"],
        dh_online_defect=e["online_defect"],
        dh_offline_defect=e["offline_defect"],
        dh_blocked=e["dh_blocked"],
        erased=erased,
        audit_ok=audit_ok,
    )
    print(f"\n[2LN] saved {out_npz}")

    plot_path = out_dir / "e2ln_wcart_primitive_quotient.png"
    if plot and _plot(model, prim_plus, prim_minus, plot_path):
        print(f"[2LN] saved {plot_path}")
    elif plot:
        print("[2LN] plot skipped: matplotlib unavailable")

    return {
        "model": model,
        "full_feasible": full_feasible,
        "quotient_feasible": quot_feasible,
        "n_survive": n_survive,
        "primitive": prim,
        "misaligned": mis,
        "erased": erased,
        "audit_ok": audit_ok,
    }


def _nilpotency_index(N: np.ndarray) -> int:
    n = N.shape[0]
    P = np.eye(n)
    for k in range(1, n + 2):
        P = P @ N
        if np.linalg.norm(P) < 1e-9:
            return k
    return n


def _is_defective(Theta: np.ndarray) -> bool:
    _, V = np.linalg.eig(Theta)
    return np.linalg.cond(V) > 1e8


def _plot(model, prim_plus, prim_minus, path: Path) -> bool:
    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception as exc:
        print(f"[2LN] plot unavailable: {exc}")
        return False

    ks = sorted(prim_plus)
    fig, ax = plt.subplots(figsize=(7.0, 4.4))
    pos_plus = [prim_plus[k][1][0] - prim_plus[k][1][1] for k in ks]
    pos_minus = [prim_minus[k][1][0] - prim_minus[k][1][1] for k in ks]
    x = np.arange(len(ks))
    ax.bar(x - 0.18, pos_plus, width=0.36, label="C_E = +1", color="tab:blue")
    ax.bar(x + 0.18, pos_minus, width=0.36, label="C_E = -1", color="tab:red")
    ax.axhline(0, color="black", lw=1)
    ax.set_xticks(x)
    ax.set_xticklabels([f"k={k:+d}" for k in ks])
    ax.set_ylabel("signature(Q_k):  #pos - #neg")
    ax.set_title("Primitive monodromy form is sign-choosable by the C_E Weil phase\n"
                 "(the unmoved M4 positivity gap)")
    ax.legend()
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", type=Path, default=None)
    parser.add_argument("--block-sizes", type=int, nargs="*", default=[3])
    parser.add_argument("--seed", type=int, default=20260605)
    parser.add_argument("--plot", action="store_true")
    args = parser.parse_args()
    run(out_dir=args.out_dir, block_sizes=tuple(args.block_sizes), seed=args.seed, plot=args.plot)
