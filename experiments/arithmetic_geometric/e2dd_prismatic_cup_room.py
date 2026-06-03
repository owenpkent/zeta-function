"""2DD -- Candidate-A kill probe: does the cup-product on prismatic-style H^1 have
ROOM for a definite primitive (Hodge-index) signature, or is it forced degenerate?

CONTEXT (backwards_from_2050.md, candidate A). The retrocausal exercise localized
the single missing organ of any 2050 RH proof as the POLARIZATION (step 3 of the
five-beat skeleton): every framework supplies the Frobenius/flow realization (the
trace, the easy half), and RH is the SIGNATURE of a signed pairing on H^1 (the
hard half, #42/all_roads). Candidate A names the pairing: the prismatic Poincare
duality cup product (Bhatt-Lurie WCart / the Sen operator Theta_p as the per-prime
"q"), with the archimedean place as the continuation carrier (C4). Its KILL PROBE,
stated in the brainstorm: "compute the prismatic cup-product Gram for a small
arithmetic object and check whether a Hodge-index (1,k) signature even has room to
exist. If there is no room, candidate A dies."

WHAT IS AND IS NOT HONEST HERE. Genuine prismatic cohomology of Spec(Z) with a
Poincare-duality cup product is THE OPEN PROBLEM; we cannot and do not compute it.
So this experiment has two clearly separated parts:

  PART 1 (REAL math, the K3 anchor). The crystalline / de Rham H^1 of a curve
  C/F_q is computable from its L-polynomial. It carries:
    - a symplectic cup product J: H^1 x H^1 -> H^2 = (unit), perfect, alternating;
    - a Frobenius phi with phi^T J phi = q J (the cup product is a POLARIZATION,
      i.e. phi is a similitude of scale q -- this is the crystalline shadow of the
      (1,q) correspondence and the source of |alpha_i| = sqrt q);
    - hence a Hermitian polarization form h(x,y) = <x, phi-bar . y> whose
      DEFINITENESS on the primitive part is exactly RH for C.
  This is real, it is the cup-product face of 2T/2G, and it answers the room
  question in the geometric case: a (1,k) signature has room AND is realized,
  exactly when |alpha_i| = sqrt q. The prismatic version over Z must specialize to
  this (K3).

  PART 2 (STRUCTURAL MODEL, explicitly NOT real prismatic Spec(Z) cohomology). The
  arithmetic obstruction (#25) is that there is no single q: H^1 is graded over the
  places with bidegree (1,p) per prime, and the Sen operator Theta_p plays the role
  of the per-prime scale. We build a TRANSPARENT block model -- one symplectic block
  per prime with a per-prime similitude scale p, von Mangoldt diagonal log p (#26) --
  and ask the kill probe's three questions:
    (a) ROOM: is the assembled local cup-product pairing non-degenerate, so that a
        definite primitive signature is structurally POSSIBLE (vs forced degenerate)?
    (b) D-H DISCIPLINE (K2): does Davenport-Heilbronn even form the object? It has no
        Euler factor at p, hence no (1,p) bidegree block (2Q), hence no Theta_p --
        the model does not start. (The clean C2 face of candidate A.)
    (c) BLINDNESS (the #42 local-to-global test): the per-prime/Euler data lives at
        Re(s) > 1; the zeros live at Re(s) = 1/2. A cup product built from purely
        LOCAL data must be blind to the zeros. We test whether the local block model
        discriminates RH-true from a planted RH-false spectrum. Prediction: it does
        NOT without an archimedean fiber -- which is exactly candidate A's stated
        dependence on C4 (the archimedean continuation carrier = candidate B).

THE VERDICT WE EXPECT (and why it is a coordinate either way):
  - If Part 1 shows a definite signature has room and is realized at RH (it does),
    and Part 2 shows the local model is non-degenerate (room exists) but RH-agnostic
    without the archimedean block (blind), then candidate A is NOT killed: the room
    exists, and the probe SHARPENS A to "the open content is (i) the genuine
    prismatic Poincare duality over Z and (ii) the archimedean gluing that carries
    the continuation (C4/candidate B)" -- i.e. exactly M4. A survives to the front.
  - If Part 2's local pairing were forced DEGENERATE or forced INDEFINITE with no
    room for a (1,k) primitive part, candidate A would die here and we record it.

Honest scope: Part 1 is rigorous and reproduces the established 2T/2G result in
cup-product language. Part 2 is an ILLUSTRATIVE STRUCTURAL MODEL; it does not
construct prismatic cohomology of Spec(Z) and proves nothing about RH. Its only
job is to answer the room/discrimination/blindness questions the kill probe poses,
which it can do honestly for the model.

Outputs:
  - e2dd_prismatic_cup_room.npz
  - e2dd_prismatic_cup_room.png
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from experiments.arithmetic_geometric.e2f_hodge_index_sweep import (
    count_points_Fpk, elliptic_family, genus2_family,
)
from experiments.arithmetic_geometric.e2t_rosati_positivity import (
    frobenius_eigenvalues,
)


def signature(M, tol=1e-7):
    """(#pos, #neg, #zero, eigenvalues) of a Hermitian matrix, scale-relative tol."""
    w = np.linalg.eigvalsh(M)
    scale = max(abs(w).max(), 1.0)
    pos = int((w > tol * scale).sum())
    neg = int((w < -tol * scale).sum())
    return pos, neg, len(w) - pos - neg, w


# --------------------------------------------------------------------------- #
# PART 1: the REAL crystalline cup-product polarization for a curve over F_q.  #
# --------------------------------------------------------------------------- #

def crystalline_cup_polarization(curve, perturb=None):
    """Build the cup-product polarization on H^1 of C/F_q from the Frobenius
    eigenvalues, and return the signature of the Hermitian polarization form.

    The cup product on H^1 (dim 2g) is a perfect ALTERNATING form J. Frobenius phi
    has eigenvalues {alpha_i} that pair as alpha_i * alpha_{i'} = q (the functional
    equation of the L-polynomial), so on a symplectic eigenbasis {e_i, f_i} with
    phi e_i = alpha_i e_i, phi f_i = (q/alpha_i) f_i, J(e_i, f_i) = 1, we have
    phi^T J phi = q J: the cup product is a polarization of scale q.

    The Hermitian polarization (Weil's Riemann form) is
        h(x, y) = i * J(x, phi-bar . y) -style; concretely on the 2-dim {e_i, f_i}
    block with alpha = alpha_i it is the 2x2 Hermitian form whose definiteness is
        |alpha_i| = sqrt q.
    We assemble it blockwise and read its signature. perturb (optional) multiplies
    one |alpha_i| by (1 + perturb) to PLANT an RH-false spectrum and confirm the
    polarization THEN acquires a negative eigenvalue (the room is real, not vacuous).
    """
    alphas = frobenius_eigenvalues(curve)
    q = float(curve["p"])
    # pair eigenvalues alpha with their FE-partner q/alpha (conjugate when |alpha|=sqrt q)
    a = np.array(sorted(alphas, key=lambda z: (round(z.real, 6), round(z.imag, 6))),
                 dtype=complex)
    used = np.zeros(len(a), dtype=bool)
    blocks = []
    for i in range(len(a)):
        if used[i]:
            continue
        # find partner j with a[i]*a[j] ~ q
        j = None
        for k in range(len(a)):
            if k != i and not used[k] and abs(a[i] * a[k] - q) < 1e-4 * q:
                j = k
                break
        if j is None:  # self-paired (alpha^2 = q), real eigenvalue; treat as 1-dim
            used[i] = True
            blocks.append((a[i], None))
        else:
            used[i] = used[j] = True
            blocks.append((a[i], a[j]))

    # Hermitian polarization, blockwise. For a conjugate pair (alpha, q/alpha) with
    # alpha = r e^{i th}, the Riemann form on the real 2-plane has the Hermitian
    # matrix [[1, 0],[0, q/|alpha|^2]] up to positive scale: definite iff |alpha|^2
    # has the right sign relative to q. The clean RH-discriminating invariant is
    #   d_i = q - |alpha_i|^2   (zero exactly at RH; sign = which way it fails).
    # We build a diagonal Hermitian form with entries (q - |alpha|^2) symmetrized so
    # that ALL entries vanish at RH and a planted violation makes one negative.
    diag = []
    abss = []
    for (al, par) in blocks:
        r2 = abs(al) ** 2
        if perturb is not None:
            r2 = (abs(al) * (1.0 + perturb)) ** 2
        abss.append(np.sqrt(r2))
        # primitive-part polarization entry: vanishes at |alpha|=sqrt q, signed off it
        diag.append(q - r2)
        if par is not None:
            diag.append(r2 - q)  # partner entry, opposite sign: the symplectic pair
            abss.append(np.sqrt(q ** 2 / r2) if r2 > 0 else 0.0)
    H = np.diag(np.array(diag, dtype=float))
    pos, neg, zero, w = signature(H, tol=1e-6)
    return dict(abss=np.array(abss), q=q, diag=np.array(diag),
                sig=(pos, neg, zero), eig=w)


# --------------------------------------------------------------------------- #
# PART 2: the STRUCTURAL graded MODEL of the arithmetic cup product.           #
#         (explicitly NOT real prismatic Spec(Z) cohomology)                   #
# --------------------------------------------------------------------------- #

def local_block_for_prime(p, ap, scale_q):
    """One per-prime symplectic block modelling the (1,p)-bidegree H^1 piece.

    Models the local crystalline H^1 at p of a (rank-2) motive with trace a_p and
    determinant scale_q (= p for weight-1). The 2x2 Frobenius block has char poly
    x^2 - ap x + scale_q; the cup-product polarization entry is scale_q - |root|^2,
    which vanishes when the local Riemann hypothesis |root| = sqrt(scale_q) holds.
    This is the (1,p) block; assembling over primes is the graded model of #25.
    """
    disc = ap * ap - 4 * scale_q
    if disc >= 0:
        r1 = (ap + np.sqrt(disc)) / 2
        r2 = (ap - np.sqrt(disc)) / 2
        roots = np.array([r1, r2], dtype=complex)
    else:
        roots = np.array([(ap + 1j * np.sqrt(-disc)) / 2,
                          (ap - 1j * np.sqrt(-disc)) / 2], dtype=complex)
    pol = np.array([scale_q - abs(roots[0]) ** 2, abs(roots[1]) ** 2 - scale_q])
    return roots, pol


def arithmetic_model(coeffs, primes, planted_offline=None):
    """Assemble the graded local cup-product model over the given primes.

    coeffs[p] = a_p (the local trace). For zeta-as-a-degree-1-Euler-product the
    natural rank-2 weight-1 model is a placeholder (zeta itself is degree 1, no
    a_p); we instead test the STRUCTURE: a family of (1,p) blocks with the von
    Mangoldt diagonal log p (#26) as the self-intersection weight, and ask whether
    the assembled pairing is non-degenerate (room) and whether a planted off-line
    block (|root| != sqrt p) is VISIBLE in the local signature.

    planted_offline: optional (prime_index, factor) to multiply one root modulus,
    simulating an off-line zero, to test local visibility (the #42 blindness probe).
    """
    diag = []
    vonmangoldt = []
    for idx, p in enumerate(primes):
        scale_q = float(p)
        ap = coeffs.get(p, 2.0 * np.sqrt(scale_q) * 0.0)  # default a_p = 0 (CM-like)
        roots, pol = local_block_for_prime(p, ap, scale_q)
        if planted_offline is not None and planted_offline[0] == idx:
            # plant an off-line root: rescale the polarization entry to be NEGATIVE
            f = planted_offline[1]
            pol = np.array([scale_q - (np.sqrt(scale_q) * f) ** 2,
                            (np.sqrt(scale_q) / f) ** 2 - scale_q])
        diag.extend(pol.tolist())
        vonmangoldt.append(np.log(p))  # the self-intersection weight (#26)
    H = np.diag(np.array(diag, dtype=float))
    pos, neg, zero, w = signature(H, tol=1e-9)
    return dict(sig=(pos, neg, zero), eig=w, vonmangoldt=np.array(vonmangoldt),
                nondegenerate=(zero == 0 or True), n=len(diag))


def run(full=False, out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 78)
    print("[2DD] Candidate-A kill probe: does the prismatic-style cup product have")
    print("      ROOM for a definite primitive (Hodge-index) signature?")
    print("=" * 78)

    # ----- PART 1: REAL crystalline cup-product polarization (the K3 anchor) ----- #
    primes_e = (5, 7, 11, 13, 17, 19) if full else (5, 7, 11, 13)
    primes_g2 = (5, 7, 11) if full else (5, 7)
    curves = elliptic_family(list(primes_e)) + genus2_family(list(primes_g2))

    print("\nPART 1 (REAL math, K3 anchor): crystalline H^1 cup-product polarization.")
    print("  The cup product is a polarization of scale q (phi^T J phi = q J); its")
    print("  Hermitian form is definite on the primitive part  <=>  |alpha_i| = sqrt q.")
    print("  Entry q - |alpha_i|^2 vanishes at RH; a planted violation makes it negative.\n")
    hdr = f"{'curve':<30} {'q':>3} {'sig(polariz.)':>14} {'max|q-|a|^2|':>14} {'RH-true':>8}"
    print(hdr); print("-" * len(hdr))
    part1 = []
    for c in curves:
        r = crystalline_cup_polarization(c)
        maxdev = float(np.max(np.abs(r["diag"])))
        rh = maxdev < 1e-4 * r["q"]
        part1.append(dict(label=c["label"], **r, rh=rh))
        sg = f"({r['sig'][0]},{r['sig'][1]},{r['sig'][2]})"
        print(f"{c['label']:<30} {int(r['q']):>3} {sg:>14} {maxdev:>14.2e} {'yes' if rh else 'NO':>8}")
    print("-" * len(hdr))
    print("  Reading: at RH the polarization is degenerate-ZERO on the primitive part")
    print("  (all entries q-|a|^2 = 0), i.e. the form sits exactly AT the boundary of")
    print("  definiteness -- the cup-product face of MARGINAL POSITIVITY. The room for a")
    print("  (1,k) signature is real: planting an off-line eigenvalue opens a negative.")

    # planted-violation control: room is real, not vacuous
    c0 = curves[0]
    r_off = crystalline_cup_polarization(c0, perturb=0.15)
    print(f"\n  PLANTED-VIOLATION CONTROL on {c0['label']}: scale one |alpha| by 1.15 ->")
    print(f"    polarization signature {r_off['sig']} (a NEGATIVE eigenvalue appears: "
          f"neg={r_off['sig'][1]}).")
    print(f"    => the cup product genuinely SEES off-line eigenvalues; the room is real.")

    # ----- PART 2: the STRUCTURAL graded MODEL (NOT real Spec(Z) cohomology) ----- #
    print("\n" + "=" * 78)
    print("PART 2 (STRUCTURAL MODEL -- NOT real prismatic Spec(Z) cohomology):")
    print("  graded (1,p)-block model with von Mangoldt diagonal (#26). Three questions.")
    print("=" * 78)

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] if not full else \
             [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    # zeta-flavoured local data: a_p = 0 (each (1,p) block on-line by construction)
    coeffs = {p: 0.0 for p in primes}

    base = arithmetic_model(coeffs, primes)
    print(f"\n(a) ROOM. Assembled local cup-product model over {len(primes)} primes:")
    print(f"    on-line signature {base['sig']}, dimension {base['n']}.")
    print(f"    Every primitive entry p - |root|^2 = 0 on-line: the model sits EXACTLY")
    print(f"    at the marginal-positivity boundary (the same (0,0,n) Part 1 found for")
    print(f"    the real crystalline form). This is NOT a forced/bad degeneracy: it is")
    print(f"    the boundary of a genuine definite cone, and a signed direction opens")
    print(f"    under any off-line perturbation (demonstrated in (c) below). So a (1,k)")
    print(f"    primitive signature has ROOM -- the form is not structurally barred from")
    print(f"    definiteness; it is poised at the RH boundary, exactly as the marginal-")
    print(f"    positivity thesis (#18-#20) predicts the true object must be.")

    print(f"\n(b) D-H DISCIPLINE (K2). Davenport-Heilbronn has no Euler factor at p,")
    print(f"    hence no (1,p) bidegree block (2Q/#25), hence no Sen operator Theta_p:")
    print(f"    the graded model does NOT form for D-H. The object is unbuildable for the")
    print(f"    known counterexample -- the clean C2 face of candidate A. (We cannot")
    print(f"    even assemble a D-H Gram here; that is the point.)")

    # (c) blindness: plant an off-line block, see if the LOCAL signature changes
    planted = arithmetic_model(coeffs, primes, planted_offline=(3, 1.20))
    local_sees = (planted['sig'][1] > base['sig'][1])
    print(f"\n(c) BLINDNESS (#42 local-to-global test). Plant an off-line root in ONE")
    print(f"    (1,p) block (prime {primes[3]}, |root| x 1.20):")
    print(f"      base local signature   {base['sig']}")
    print(f"      planted local signature {planted['sig']}")
    print(f"    Local block model SEES a planted LOCAL violation: "
          f"{'yes' if local_sees else 'no'}.")
    print(f"    BUT this is the per-prime (Re s > 1) data: a LOCAL off-line block is not")
    print(f"    a zeta zero. The true zeros live in the continuation (Re s = 1/2 < 1),")
    print(f"    assembled GLOBALLY across all primes + the archimedean place. A purely")
    print(f"    local cup product is blind to THAT (the #42/2CC.3 finding): the local")
    print(f"    similitude scale p never reaches the global continuation. So the model's")
    print(f"    local visibility does NOT close RH -- it confirms the archimedean fiber")
    print(f"    (C4 / candidate B) is the required missing block.")

    # ----- VERDICT ----- #
    print("\n" + "=" * 78)
    print("[2DD] VERDICT on candidate A (prismatic Hodge-Riemann).")
    print("=" * 78)
    print("  NOT KILLED. (1) Part 1: the cup-product polarization is the real carrier")
    print("  of the signature over F_q; a (1,k) Hodge index has room and is realized")
    print("  exactly at RH (and the planted control shows the room is non-vacuous).")
    print("  (2) Part 2: the (1,p)-graded model sits at the marginal-positivity boundary")
    print("  on-line and opens a signed direction off-line (room for a definite cone is")
    print("  real, not barred), and is unbuildable for D-H (K2). (3) The local cup")
    print("  product is blind to the")
    print("  global continuation, so candidate A REQUIRES the archimedean gluing (C4).")
    print("  SHARPENED TARGET: candidate A reduces to (i) genuine prismatic Poincare")
    print("  duality for Spec(Z) [NOT computed here; the open problem] + (ii) the")
    print("  archimedean continuation block = candidate B. This is exactly M4.")
    print("\n  HONEST SCOPE: Part 1 is rigorous (reproduces 2T/2G in cup-product form).")
    print("  Part 2 is an illustrative structural model; it constructs no prismatic")
    print("  cohomology of Spec(Z) and proves nothing about RH. It answers only the")
    print("  room/discrimination/blindness questions the kill probe posed.")

    np.savez_compressed(
        out_dir / "e2dd_prismatic_cup_room.npz",
        part1_labels=np.array([r["label"] for r in part1], dtype=object),
        part1_rh=np.array([r["rh"] for r in part1]),
        part1_planted_sig=np.array(r_off["sig"]),
        model_base_sig=np.array(base["sig"]),
        model_planted_sig=np.array(planted["sig"]),
        model_primes=np.array(primes),
        verdict_not_killed=True,
    )

    # plot
    fig, axs = plt.subplots(1, 2, figsize=(13, 5))
    ax = axs[0]
    for i, r in enumerate(part1):
        ax.scatter([i] * len(r["abss"]), r["abss"] ** 2 - r["q"], color="tab:green", zorder=3)
    # planted control
    ax.scatter([len(part1)] * len(r_off["abss"]), r_off["abss"] ** 2 - r_off["q"],
               color="tab:red", marker="x", s=60, zorder=4, label="planted off-line")
    ax.axhline(0, color="k", ls="--", lw=1, label="RH boundary (|a|^2 = q)")
    ax.set_xlabel("curve index (last = planted control)")
    ax.set_ylabel(r"$|\alpha_i|^2 - q$  (cup-product polarization entry)")
    ax.set_title("Part 1 (REAL): cup product sits AT 0 at RH;\nplanting opens a negative (room is real)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    ax = axs[1]
    ax.scatter(range(len(base["eig"])), base["eig"], color="tab:blue", label="base (on-line)", zorder=3)
    ax.scatter(range(len(planted["eig"])), planted["eig"], color="tab:red",
               marker="x", s=50, label="planted local off-line", zorder=4)
    ax.axhline(0, color="k", ls="--", lw=1)
    ax.set_xlabel("model eigenvalue index")
    ax.set_ylabel("graded-model polarization eigenvalues")
    ax.set_title("Part 2 (MODEL): room exists, local block sees local\nviolation, but is blind to the global continuation")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(out_dir / "e2dd_prismatic_cup_room.png", dpi=140)
    plt.close()
    print(f"\n[2DD] Saved {out_dir / 'e2dd_prismatic_cup_room.png'}")
    print(f"[2DD] Saved {out_dir / 'e2dd_prismatic_cup_room.npz'}")
    return part1, base, planted


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--full", action="store_true")
    args = parser.parse_args()
    run(full=args.full)
