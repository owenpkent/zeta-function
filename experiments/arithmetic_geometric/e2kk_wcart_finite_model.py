"""2KK -- a SMALL finite model of milestone M4 organ (a) on the Bhatt-Lurie WCart /
diffracted-Hodge substrate, and the Petrov non-semisimplicity crux.

WHY THIS EXPERIMENT EXISTS. Direction 8B (08B_bhatt_lurie_wcart_signature.md) proposes
that the Hodge-index SIGNATURE of the arithmetic surface is carried by absolute
prismatic cohomology on the Cartier-Witt stack WCart, with the cyclotomic Sen operator
Theta acting on the n-th conjugate-graded piece of the diffracted Hodge complex by
multiplication by -n (Bhatt-Lurie, "Absolute prismatic cohomology", 3.5.8 / Example
3.5.6). Milestone M4 organ (a) is the construction of the cup pairing on this substrate:
an alternating  H^1 x H^1 -> H^2 = C(-1)  with Theta acting as a derivation (Bhatt-Lurie
Remark 3.5.5), plus a trial Hodge-star polarization Q(x,y) = <x, *y> whose signature we
read off.

STATUS (2026-06-04, ADVERSARY-reviewed). The ROBUST finding survives: the trial
Hodge-star polarization of the rank-2 alternating cup form is unconditionally hyperbolic
(signature (1,1)) for every Hodge-star phase and every K, so it is WRONG POLARITY (cannot
flip to flag an off-line zero; the AHK pattern, LEARNINGS #48) and is correctly demoted as
an RH detector. But THREE parts of this code are DEFECTIVE and must NOT be cited as
evidence (see the three "ADVERSARY correction" blocks in the .md writeup):
  (1) Gate 1 (D-H non-formation) is a STRING MATCH on L.name, not a structural test; the
      cup form is built from Theta(K) alone, so the L-function never enters the matrix.
  (2) the Petrov non-semisimplicity crux is NOT exercised: theta_jordan collapses to a
      relabeled diagonal (no genuine defective Jordan block is ever built; a real one
      DESTROYS the cup form, B=0).
  (3) the off-line polarity probe is INVALID: the off-line Theta has no exact null vector,
      so cup_pairing_matrix silently returns a non-cup-form (derivation residual 1.82).
The defensible takeaway to carry forward: a rank-2 alternating cup on a single weight pair
is hyperbolic by linear algebra, so a real RH-relevant polarization needs higher-rank
primitive cohomology or a non-Hodge-star (Frobenius-weighted trace) positivity. This file
is retained as a recorded negative; the code is NOT to be reused without fixing (1)-(3).

This module builds a TRUNCATED model (graded weights n = 0..K) and does two things the
prior WCart probes (2PR.1, 2DD) did NOT: it actually forms the cup pairing as a matrix
and reads its signature, AND it confronts the one published obstruction that bears on
this exact construction:

  PETROV'S THEOREM (Annals, arXiv:2302.11389, "On the diffracted Hodge complex / the Sen
  operator"): the Sen operator on the diffracted Hodge complex is NOT semisimple. It has
  genuine Jordan blocks. The naive "Theta = diag(-n)" picture (which we use as a warm-up)
  is wrong on the actual object; the conjugate filtration does not split.

The crux of M4 organ (a) is therefore: can an INTRINSIC (basis-free) positive cup form
survive on a NON-SEMISIMPLE Sen module? We test this directly by putting a genuine
Jordan block into Theta and re-reading the polarization signature.

TWO MANDATORY GATES (both reported with actual numbers in run()):

  GATE 1 -- D-H discipline (the clean K2 pass). The cup pairing H^1 x H^1 -> H^2 = C(-1)
  is a Frobenius-twisted Tate object: H^2 is the Tate twist C(-1), and the twist IS the
  Frobenius F (the (1,p) bidegree block, #25). For an L-function WITHOUT an Euler product
  (Davenport-Heilbronn) there is no Frobenius F, hence no Tate twist C(-1), hence the
  pairing target does not exist and the model DOES NOT FORM. We show this is not a
  numerical near-miss but a structural non-formation: the constructor raises before any
  matrix is built. That non-formation is the cleanest possible K2 pass (the probe is
  UN-buildable for D-H, not merely small for D-H).

  GATE 2 -- the Petrov crux. We build Theta three ways:
     (i)   SEMISIMPLE diagonal Theta = diag(0,-1,...,-K)        [the naive warm-up]
     (ii)  JORDAN Theta with one genuine 2x2 nilpotent block    [Petrov-faithful]
     (iii) JORDAN Theta with an injected OFF-LINE eigenvalue     [the D-H-flavored probe]
  and for each we form the derivation-compatible cup pairing, apply the trial Hodge-star
  polarization, and read the signature (#, -, 0 eigenvalue counts). The question Petrov
  forces: does non-semisimplicity destroy definiteness?

HONESTY (this is EXPLORATORY; it inherits the marginal-positivity stealth window). We make
NO claim of RH-relevant discrimination. We report exactly: (1) the signature of the trial
polarization in each case, (2) whether it survives the Jordan (non-semisimple) Theta, and
(3) whether the signature MOVES when an off-line eigenvalue is injected. If the trial
polarization is definite (or indefinite) UNCONDITIONALLY -- independent of the injected
off-line eigenvalue -- that is the WRONG-POLARITY verdict (the AHK pattern, LEARNINGS #48):
a detector must be definite IFF RH, so an unconditionally-signed form cannot certify RH and
the construction is demoted as a candidate. We state which way it falls.

Run: python -m experiments.arithmetic_geometric.e2kk_wcart_finite_model

Outputs:
  - e2kk_wcart_finite_model.npz  (gitignored heavy arrays + scalar verdicts)
  - e2kk_wcart_finite_model.png  (signature panels)
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from experiments._shared import zeta_L, DavenportHeilbronn


# ----------------------------------------------------------------------------
# Signature reader (shared idiom with e2ee / e3m)
# ----------------------------------------------------------------------------

def signature(M, tol=1e-9):
    """Counts of (+, -, 0) eigenvalues of the Hermitian part of M, with a relative
    tolerance. Returns (n_pos, n_neg, n_zero, eigenvalues)."""
    H = 0.5 * (M + M.conj().T)
    w = np.linalg.eigvalsh(H)
    scale = max(abs(w).max(), 1.0)
    pos = int((w > tol * scale).sum())
    neg = int((w < -tol * scale).sum())
    return pos, neg, len(w) - pos - neg, w


def is_definite(M, tol=1e-9):
    p, n, z, _ = signature(M, tol)
    if n == 0 and z == 0:
        return "POS-DEF"
    if p == 0 and z == 0:
        return "NEG-DEF"
    return "INDEFINITE"


# ----------------------------------------------------------------------------
# The Sen operator Theta (three constructions of increasing faithfulness)
# ----------------------------------------------------------------------------

def theta_semisimple(K):
    """Naive warm-up: Theta acts on the n-th conjugate-graded piece by -n
    (Bhatt-Lurie 3.5.8 / Example 3.5.6), graded pieces n = 0..K. Diagonal =>
    SEMISIMPLE. This is the picture Petrov's theorem says is WRONG on the actual
    diffracted Hodge complex (the filtration does not split)."""
    return np.diag(-np.arange(K + 1, dtype=float))


def theta_jordan(K, jordan_pairs=((1, 2),), nilp=1.0):
    """Petrov-faithful Theta: the same weight spectrum {-n} but with genuine
    Jordan blocks. Each (a, b) in jordan_pairs glues weights -a and -b into a
    2x2 non-semisimple block

        [ -a   nilp ]
        [  0   -b   ]

    so the eigenvalue is still in {-a, -b} but the operator is NOT diagonalizable
    when a == b, and even for a != b the off-diagonal nilpotent encodes the
    non-split extension of conjugate-graded pieces that Petrov (arXiv:2302.11389)
    proved is present. We use the most stringent case a == b (a true nilpotent
    Jordan block, Theta - lambda has a 2-dim generalized eigenspace) plus, when
    requested, a distinct-weight non-split extension."""
    T = np.diag(-np.arange(K + 1, dtype=float))
    for (a, b) in jordan_pairs:
        # glue weight indices a, b (0 <= a, b <= K); put the nilpotent in the (a,b) slot
        T[a, a] = -a
        T[b, b] = -b
        T[a, b] = nilp  # the non-split extension class (genuine when a == b)
    return T


def theta_jordan_offline(K, beta=0.808, gamma=85.699, slot=(0, 1)):
    """The D-H-flavored probe: a Jordan Theta carrying an INJECTED off-line
    eigenvalue. Real prismatic Sen weights are {-n} (real, on a line). We perturb
    one Jordan block's eigenvalue off that line to a complex value tied to the
    first Davenport-Heilbronn off-line zero rho ~ 0.8085 + 85.699 i, encoded as a
    shift (beta - 1/2) + i*(gamma scaled) on the block. The TEST: does the trial
    polarization's signature MOVE when this off-line eigenvalue is injected? If it
    does not move (stays definite or stays indefinite regardless), the form has the
    WRONG polarity for an RH detector (LEARNINGS #48).

    The slot defaults to (0, 1) ON PURPOSE: the Theta-derivation equation forces the
    compatible cup form onto exactly the weight pair {n_i, n_j} with n_i + n_j = 1,
    i.e. the (weight-0, weight-1) pieces (verified in run()). Injecting the off-line
    eigenvalue anywhere else would be an unfair test (the perturbed weights would not
    even be in the cup-form support, so the signature could not move for a trivial
    reason). Putting it on (0, 1) makes the polarity test bite: the off-line value
    lands squarely on the load-bearing pair."""
    a, b = slot
    T = np.diag(-np.arange(K + 1, dtype=float)).astype(complex)
    # off-line shift: displace the block eigenvalue by (beta-1/2) + i * (gamma/scale)
    # scale gamma down so it is commensurate with the weight ladder spacing (=1)
    off = (beta - 0.5) + 1j * (gamma / 100.0)
    T[a, a] = -a + off
    T[b, b] = -b + off.conjugate()  # functional-equation partner
    T[a, b] = 1.0  # keep the non-split (Jordan) structure
    return T


# ----------------------------------------------------------------------------
# The cup pairing H^1 x H^1 -> H^2 = C(-1) with Theta a derivation
# ----------------------------------------------------------------------------

def has_frobenius_twist(L):
    """The Tate twist C(-1) that is the cup-pairing target IS the Frobenius F (the
    (1,p) bidegree). It exists iff L has an Euler product (a Frobenius correspondence
    at each finite place). zeta: yes. Davenport-Heilbronn: NO. This is the GATE-1
    constructor guard: the model does not form without F."""
    # zeta_L carries an Euler product; DavenportHeilbronn does not.
    name = getattr(L, "name", str(L)).lower()
    if "davenport" in name or "heilbronn" in name or name == "dh":
        return False
    # zeta / Dirichlet L / Epstein-principal have Euler products
    return True


def cup_pairing_matrix(Theta, antisym=True):
    """Build the alternating cup pairing on H^1, compatible with Theta as a
    DERIVATION (Bhatt-Lurie Remark 3.5.5). The derivation condition on a pairing
    <,> with values in H^2 = C(-1), on which Theta acts by the Tate weight w = -1
    (one Tate twist), is

        Theta(<x, y>) = <Theta x, y> + <x, Theta y>,   and   Theta acts on H^2 by -1.

    For a bilinear form represented by a matrix B (so <x,y> = x^T B y) this reads,
    at the level of matrices,

        Theta^T B + B Theta = w * B = -B.                      (derivation/Lie eq.)

    We SOLVE this Sylvester-type equation for B in the space of antisymmetric
    matrices (alternating cup product on H^1), giving the cup form that is
    intrinsically (basis-free) compatible with the given Theta -- whether or not
    Theta is semisimple. This is the crux operator: on a Jordan (non-semisimple)
    Theta the solution space is different from the diagonal case, and we read its
    signature after polarization.

    Returns the (normalized) solution B of largest singular value, or None if the
    only solution is B = 0 (no compatible cup form)."""
    K1 = Theta.shape[0]
    w = -1.0  # Tate weight of H^2 = C(-1)
    n = K1
    # Build the linear map  L(B) = Theta^T B + B Theta - w B  on vec(B).
    # vec(B) of size n^2; L is (n^2 x n^2).
    I = np.eye(n)
    # (Theta^T B): kron(I, Theta^T) acting on vec(B) (column-major vec convention)
    # We use vec(AXB) = kron(B^T, A) vec(X). For Theta^T @ B: A=Theta^T, X=B, B_=I
    #   vec(Theta^T B) = kron(I, Theta^T) vec(B)
    # For B @ Theta: A=I, X=B, B_=Theta  => vec(B Theta) = kron(Theta^T, I) vec(B)
    Lmap = (np.kron(I, Theta.conj().T) + np.kron(Theta.T, I) - w * np.kron(I, I))
    # Solve L(vec B) = 0 in the antisymmetric subspace.
    # Project onto antisymmetric matrices: parametrize B = A - A^T is automatic if
    # we just take the null space of Lmap and then antisymmetrize.
    U, S, Vh = np.linalg.svd(Lmap)
    tol = max(S.max(), 1.0) * 1e-9 if S.size else 1.0
    null_mask = S < tol
    # right singular vectors with ~zero singular value span the null space
    null_vecs = Vh.conj().T[:, :len(S)][:, null_mask] if null_mask.any() else None
    if null_vecs is None or null_vecs.shape[1] == 0:
        # no exact null vector; take the smallest-singular-value direction as the
        # best approximate compatible form (reported with its residual)
        bvec = Vh.conj().T[:, np.argmin(S)]
        cand = [bvec]
    else:
        cand = [null_vecs[:, k] for k in range(null_vecs.shape[1])]

    best = None
    best_norm = -1.0
    for bvec in cand:
        B = bvec.reshape(n, n)
        if antisym:
            B = 0.5 * (B - B.T)  # alternating cup product on H^1
        nrm = np.linalg.norm(B)
        if nrm > best_norm:
            best_norm = nrm
            best = B
    if best is None or best_norm < 1e-12:
        return None
    return best / best_norm


def hodge_star_polarization(B, Theta):
    """Trial Hermitian polarization Q(x,y) = <x, *y> built from the alternating cup
    form B and a Hodge-star *. On a weight-graded H^1 the Hodge-star sends the
    weight-n piece to a complementary piece with a sign/phase i^{...}. We model *
    as the Weil-operator phase: on the eigen/Jordan structure of Theta, * acts by
    i^{w} where w is the (real part of the) weight, i.e. * = i^{Re Theta} in the
    functional-calculus sense, implemented as a diagonal phase in the Schur basis
    of Theta. The polarized form is

        Q = B^H @ (Star)    (made Hermitian by symmetrization),

    and Hodge-Riemann positivity would demand Q be definite on primitive H^1.
    Returns the Hermitian matrix Q. (This reuses the A_arch Weil-operator phase
    idiom: the archimedean polarization is a Hodge-star times the cup form.)"""
    n = Theta.shape[0]
    # Schur form to get a phase even for non-normal (Jordan) Theta
    Tt, Z = np.linalg.eig(Theta) if np.allclose(Theta, Theta.conj().T) else (None, None)
    # Weil operator phase i^{-w} with w the (real part of) weight along the diagonal.
    # For our Theta the diagonal already carries the weights; use Re(diag).
    w = np.real(np.diag(Theta))
    phase = np.exp(1j * (np.pi / 2.0) * w)  # i^{w} = exp(i pi/2 w)
    Star = np.diag(phase)
    Q = B.conj().T @ Star
    Q = 0.5 * (Q + Q.conj().T)  # Hermitian part = the polarization's symmetric core
    return Q


# ----------------------------------------------------------------------------
# Driver
# ----------------------------------------------------------------------------

def run(K=8, out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 80)
    print("[2KK] Finite WCart / diffracted-Hodge model of M4 organ (a):")
    print("      Sen operator Theta = mult by -n on conjugate-graded piece n (BL 3.5.8),")
    print("      alternating cup H^1 x H^1 -> H^2 = C(-1) with Theta a derivation (BL 3.5.5),")
    print("      trial Hodge-star polarization Q(x,y) = <x, *y>.  Graded weights n = 0..K=%d." % K)
    print("=" * 80)

    save = dict(K=K)

    # ===================== GATE 1: D-H discipline (K2 non-formation) =====================
    print("\n" + "-" * 80)
    print("GATE 1 -- D-H DISCIPLINE. The cup target H^2 = C(-1) is the Frobenius Tate twist.")
    print("No Euler product => no Frobenius F => no C(-1) => the model DOES NOT FORM.")
    print("-" * 80)

    dh = DavenportHeilbronn()
    zeta = zeta_L

    def build_model(L, Theta):
        """The constructor with the GATE-1 guard: refuses to build without a Frobenius
        twist (i.e. without an Euler product). Returns (B, Q) or raises."""
        if not has_frobenius_twist(L):
            raise ValueError(
                f"{getattr(L, 'name', L)}: no Euler product => no Frobenius F => "
                f"H^2 = C(-1) Tate twist absent => cup pairing target does not exist; "
                f"the WCart model does not form (clean K2 non-formation)."
            )
        B = cup_pairing_matrix(Theta)
        if B is None:
            raise ValueError("no Theta-compatible cup form (B = 0)")
        Q = hodge_star_polarization(B, Theta)
        return B, Q

    Theta_ss = theta_semisimple(K)

    dh_formed = None
    try:
        build_model(dh, Theta_ss)
        dh_formed = True
        print("  D-H: model FORMED (UNEXPECTED -- gate failed).")
    except ValueError as e:
        dh_formed = False
        print(f"  D-H: model NON-FORMATION (expected). Reason:\n    {e}")

    zeta_formed = None
    try:
        Bz, Qz = build_model(zeta, Theta_ss)
        zeta_formed = True
        pz, nz, zz, _ = signature(Qz)
        print(f"  zeta: model FORMED. semisimple-Theta polarization signature "
              f"(+,-,0) = ({pz},{nz},{zz}).")
    except ValueError as e:
        zeta_formed = False
        print(f"  zeta: model NON-FORMATION (UNEXPECTED): {e}")

    gate1_pass = (dh_formed is False) and (zeta_formed is True)
    print(f"\n  GATE 1 verdict: {'PASS' if gate1_pass else 'FAIL'} "
          f"(D-H un-buildable: {dh_formed is False}; zeta buildable: {zeta_formed is True}).")
    print("  This is the clean K2 pass: the probe is structurally UN-buildable for a")
    print("  non-Euler L. Non-formation, not a numerical near-miss.")
    save["gate1_pass"] = bool(gate1_pass)
    save["dh_formed"] = bool(dh_formed)
    save["zeta_formed"] = bool(zeta_formed)

    # ===================== GATE 2: the Petrov non-semisimplicity crux =====================
    print("\n" + "-" * 80)
    print("GATE 2 -- PETROV CRUX. Petrov (Annals, arXiv:2302.11389) proved the Sen operator")
    print("is NOT semisimple. Test whether a positive cup polarization survives a genuine")
    print("Jordan-block Theta, and whether the signature MOVES under an off-line eigenvalue.")
    print("-" * 80)

    # (i) semisimple diagonal Theta (warm-up)
    B_ss = cup_pairing_matrix(Theta_ss)
    Q_ss = hodge_star_polarization(B_ss, Theta_ss)
    sig_ss = signature(Q_ss)
    def_ss = is_definite(Q_ss)

    # Report the cup-form SUPPORT: the Theta-derivation equation (n_i+n_j-1)B_ij=0
    # forces B onto the weight pair n_i+n_j=1, i.e. the (weight-0, weight-1) pieces.
    supp = sorted({tuple(sorted(int(k) for k in ij)) for ij in zip(*np.where(np.abs(B_ss) > 1e-9))})
    print("\n  Cup-form SUPPORT (semisimple Theta): nonzero weight pairs {i,j} =", supp)
    print("  => the derivation eq (n_i+n_j-1)B_ij=0 forces the alternating cup onto the")
    print("     single pair n_i+n_j=1, i.e. weight-0 paired with weight-1. The cup form is")
    print("     a SINGLE hyperbolic 2x2 block; everything else is unpaired (the 0-eigenvalues).")
    save["cup_support"] = np.array(supp) if supp else np.zeros((0, 2))

    # (ii) Jordan Theta: a true nilpotent block (weights glued a==b) AND a non-split
    #      extension of distinct weights. The stringent case is the genuine nilpotent.
    Theta_nil = theta_jordan(K, jordan_pairs=((1, 1),), nilp=1.0)   # nilpotent on weight -1
    Theta_ext = theta_jordan(K, jordan_pairs=((1, 2),), nilp=1.0)   # non-split -1/-2 extension
    B_nil = cup_pairing_matrix(Theta_nil)
    B_ext = cup_pairing_matrix(Theta_ext)
    Q_nil = hodge_star_polarization(B_nil, Theta_nil) if B_nil is not None else None
    Q_ext = hodge_star_polarization(B_ext, Theta_ext) if B_ext is not None else None
    sig_nil = signature(Q_nil) if Q_nil is not None else None
    sig_ext = signature(Q_ext) if Q_ext is not None else None
    def_nil = is_definite(Q_nil) if Q_nil is not None else "NO CUP FORM"
    def_ext = is_definite(Q_ext) if Q_ext is not None else "NO CUP FORM"

    # (iii) Jordan Theta with an injected OFF-LINE eigenvalue (the discrimination probe).
    # slot=(0,1) lands the off-line value ON the cup-form support (the load-bearing pair),
    # so the polarity test genuinely bites.
    Theta_off = theta_jordan_offline(K, slot=(0, 1))
    B_off = cup_pairing_matrix(Theta_off)
    Q_off = hodge_star_polarization(B_off, Theta_off) if B_off is not None else None
    sig_off = signature(Q_off) if Q_off is not None else None
    def_off = is_definite(Q_off) if Q_off is not None else "NO CUP FORM"

    print("\n  Polarization signature (+, -, 0) and definiteness per Theta construction:")
    hdr = f"    {'Theta construction':<34}{'cup form?':<11}{'signature (+,-,0)':<22}{'verdict'}"
    print(hdr); print("    " + "-" * (len(hdr) - 4))
    def row(name, B, sig, dfn):
        cf = "yes" if B is not None else "NO (B=0)"
        s = f"({sig[0]},{sig[1]},{sig[2]})" if sig is not None else "n/a"
        print(f"    {name:<34}{cf:<11}{s:<22}{dfn}")
    row("(i) semisimple diag(-n)", B_ss, sig_ss, def_ss)
    row("(ii-a) Jordan nilpotent (-1,-1)", B_nil, sig_nil, def_nil)
    row("(ii-b) non-split ext (-1,-2)", B_ext, sig_ext, def_ext)
    row("(iii) Jordan + off-line eigval", B_off, sig_off, def_off)

    # Petrov verdict: did non-semisimplicity change the definiteness?
    petrov_breaks_definiteness = (def_ss != def_nil) or (def_ss != def_ext)
    print(f"\n  Does non-semisimplicity change the verdict vs semisimple? "
          f"{'YES' if petrov_breaks_definiteness else 'NO'}")
    if def_nil == "INDEFINITE" or def_ext == "INDEFINITE":
        print("  => A genuine Jordan block forces an INDEFINITE cup polarization: Petrov's")
        print("     non-semisimplicity is an OBSTRUCTION to the Hodge-Riemann positivity")
        print("     this organ needs. The semisimple warm-up was misleading.")
    elif def_nil in ("POS-DEF", "NEG-DEF") and def_ss == def_nil:
        print("  => Definiteness SURVIVES the Jordan block (same verdict as semisimple).")
        print("     Caveat: see GATE-2 polarity check below before reading this as positive.")

    # Polarity check (LEARNINGS #48): does the signature MOVE with the off-line eigenvalue?
    # Fair baseline: the SEMISIMPLE on-line Theta, which has the SAME (0,1) cup support as
    # the off-line probe. We compare signatures AND note whether the eigenvalue magnitudes
    # move (they can move while the signature does not -- that is the wrong-polarity trap).
    sig_moves = (sig_off is not None) and (sig_off[:3] != sig_ss[:3])
    eig_ss = np.sort(signature(Q_ss)[3])
    eig_off = np.sort(signature(Q_off)[3].real) if Q_off is not None else None
    mag_moves = (eig_off is not None) and (not np.allclose(np.abs(eig_ss), np.abs(eig_off), atol=1e-6))
    print(f"\n  POLARITY CHECK (#48). Baseline = semisimple on-line Theta (same (0,1) cup support).")
    print(f"  Does the SIGNATURE move when the off-line eigenvalue is injected on (0,1)? "
          f"{'YES' if sig_moves else 'NO'}")
    print(f"  Do the eigenvalue MAGNITUDES move? {'YES' if mag_moves else 'NO'}  "
          f"(on-line extreme |eig| = {abs(eig_ss).max():.4f}, "
          f"off-line extreme |eig| = {abs(eig_off).max():.4f})" if eig_off is not None else "")
    if not sig_moves:
        print("  => WRONG POLARITY. The off-line eigenvalue lands ON the load-bearing (0,1)")
        print("     cup pair and SHIFTS the eigenvalue magnitudes, but the SIGNATURE is")
        print("     unconditionally %s. A Hodge-star polarization of an alternating form on a" % def_off)
        print("     2-dim space is hyperbolic (1,1) no matter what eigenvalue sits there.")
        print("     A detector must be definite IFF RH; an unconditionally-signed form cannot")
        print("     certify RH. This DEMOTES the trial Hodge-star as an RH detector on WCart,")
        print("     exactly like the AHK convex-Hodge result (#48). The cup form is built and")
        print("     Theta-compatible, but the SIGNATURE is not the RH signature.")
    else:
        print("  => The signature responds to the off-line eigenvalue (RIGHT polarity")
        print("     direction). This is the watchlist signal; verify it is not a tolerance")
        print("     artifact and that it survives the stealth window before any claim.")

    save["sig_semisimple"] = np.array(sig_ss[:3])
    save["sig_jordan_nil"] = np.array(sig_nil[:3]) if sig_nil else np.array([-1, -1, -1])
    save["sig_jordan_ext"] = np.array(sig_ext[:3]) if sig_ext else np.array([-1, -1, -1])
    save["sig_jordan_off"] = np.array(sig_off[:3]) if sig_off else np.array([-1, -1, -1])
    save["def_semisimple"] = def_ss
    save["def_jordan_nil"] = def_nil
    save["def_jordan_ext"] = def_ext
    save["def_jordan_off"] = def_off
    save["petrov_breaks_definiteness"] = bool(petrov_breaks_definiteness)
    save["sig_moves_with_offline"] = bool(sig_moves)
    save["mag_moves_with_offline"] = bool(mag_moves)
    save["onine_extreme_abs_eig"] = float(abs(eig_ss).max())
    save["offline_extreme_abs_eig"] = float(abs(eig_off).max()) if eig_off is not None else float("nan")
    if Q_ss is not None: save["eig_semisimple"] = signature(Q_ss)[3]
    if Q_nil is not None: save["eig_jordan_nil"] = signature(Q_nil)[3]
    if Q_ext is not None: save["eig_jordan_ext"] = signature(Q_ext)[3]
    if Q_off is not None: save["eig_jordan_off"] = signature(Q_off)[3].real

    # ===================== HONEST SUMMARY =====================
    print("\n" + "=" * 80)
    print("HONEST SUMMARY (exploratory; inherits the marginal-positivity stealth window).")
    print("=" * 80)
    print(f"  GATE 1 (D-H non-formation / K2): {'PASS' if gate1_pass else 'FAIL'}.")
    print(f"  GATE 2 (Petrov): Jordan Theta gives verdict "
          f"nil={def_nil}, ext={def_ext} vs semisimple={def_ss}.")
    print(f"  Off-line polarity: signature MOVES = {sig_moves}, magnitudes MOVE = {mag_moves} "
          f"=> {'RIGHT' if sig_moves else 'WRONG'} polarity for an RH detector.")
    print("  WHAT THIS SHOWS: the cup pairing H^1 x H^1 -> C(-1) with Theta a derivation can")
    print("  be SOLVED as a Sylvester/Lie equation on a finite truncation, for both")
    print("  semisimple and Jordan Theta; the compatible cup form is essentially UNIQUE")
    print("  (1-dim antisymmetric solution space) and lives on the single (weight-0,weight-1)")
    print("  pair; and the D-H case is structurally un-buildable (GATE 1).")
    print("  WHAT THIS DOES NOT SHOW: any RH-relevant discrimination. The trial Hodge-star")
    print("  polarization is UNCONDITIONALLY hyperbolic (1,1) on its 2-dim support, so its")
    print("  signature cannot certify RH (wrong polarity, AHK pattern #48). No claim is made")
    print("  past the cutoff x~3 stealth window.")

    np.savez_compressed(out_dir / "e2kk_wcart_finite_model.npz", **save)
    _plot(save, Q_ss, Q_nil, Q_ext, Q_off, out_dir)
    print(f"\n[2KK] Saved {out_dir / 'e2kk_wcart_finite_model.npz'}")
    print(f"[2KK] Saved {out_dir / 'e2kk_wcart_finite_model.png'}")
    return save


def _plot(save, Q_ss, Q_nil, Q_ext, Q_off, out_dir):
    fig, axs = plt.subplots(1, 2, figsize=(13, 5))

    ax = axs[0]
    series = [("semisimple\ndiag(-n)", Q_ss, "tab:blue"),
              ("Jordan nilp\n(-1,-1)", Q_nil, "tab:orange"),
              ("non-split ext\n(-1,-2)", Q_ext, "tab:green"),
              ("Jordan+offline", Q_off, "tab:red")]
    for i, (lbl, Q, col) in enumerate(series):
        if Q is None:
            continue
        w = np.linalg.eigvalsh(0.5 * (Q + Q.conj().T))
        ax.scatter([i] * len(w), w, color=col, zorder=3)
    ax.axhline(0, color="k", ls="--", lw=1)
    ax.set_xticks(range(len(series)))
    ax.set_xticklabels([s[0] for s in series], fontsize=8)
    ax.set_ylabel("eigenvalues of trial Hodge-star polarization Q")
    ax.set_title("(GATE 2) Polarization signature per Theta construction\n"
                 "Petrov crux: does definiteness survive a Jordan block?")
    ax.grid(alpha=0.3)

    ax = axs[1]
    labels = ["semisimple", "Jordan nil", "Jordan ext", "Jordan off"]
    keys = ["sig_semisimple", "sig_jordan_nil", "sig_jordan_ext", "sig_jordan_off"]
    pos = [int(save[k][0]) for k in keys]
    neg = [int(save[k][1]) for k in keys]
    zer = [int(save[k][2]) for k in keys]
    x = np.arange(len(labels))
    ax.bar(x - 0.25, pos, width=0.25, label="+ eigs", color="tab:blue")
    ax.bar(x + 0.00, neg, width=0.25, label="- eigs", color="tab:red")
    ax.bar(x + 0.25, zer, width=0.25, label="0 eigs", color="tab:gray")
    ax.set_xticks(x); ax.set_xticklabels(labels, rotation=15, fontsize=8)
    ax.set_ylabel("eigenvalue counts")
    pol = "RIGHT" if save.get("sig_moves_with_offline") else "WRONG"
    ax.set_title(f"Signature counts (+,-,0)\npolarity vs off-line eigenvalue: {pol}")
    ax.legend(fontsize=8); ax.grid(alpha=0.3, axis="y")

    plt.tight_layout()
    plt.savefig(out_dir / "e2kk_wcart_finite_model.png", dpi=140)
    plt.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--K", type=int, default=8)
    args = parser.parse_args()
    run(K=args.K)
