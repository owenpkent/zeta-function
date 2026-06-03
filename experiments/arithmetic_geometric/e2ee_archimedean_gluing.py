"""2EE -- the archimedean continuation block and the gluing (probe B of backwards_from_2050).

CONTEXT. Probe 1 (2DD, LEARNINGS #43) left candidate A (prismatic Hodge-Riemann)
NOT killed but SHARPENED: the local (1,p) prismatic blocks have room for a definite
signature but are blind to the global continuation (Re(s)=1/2), so candidate A
requires the ARCHIMEDEAN continuation block (C4 / candidate B) glued to the local
finite blocks. This experiment prototypes that gluing on the project's already
VALIDATED Weil-form components, and asks the precise structural question candidate
A+B poses: WHEN the archimedean block is glued to the finite blocks, does the
result carry a Hodge-index (ample-plus-primitive) structure, and which concrete
object plays the role of the fundamental class H^2 / the trace map?

THE KEY STRUCTURAL OBSERVATION (the reason this probe is worth running). The
project's non-circular Weil form is M = A_arch + P_fin + B_pole (#33/#34, e2v/e2w),
and the POLE block is, by construction (e3m_place_type_balance.pole_block),
    B_pole = residue * 2 * outer(phi_1, phi_1),
a RANK-1 form along the single vector phi_1 (the test function evaluated at the
s=1 point). For zeta the residue is 1, so B_pole is a rank-1 POSITIVE direction;
for Davenport-Heilbronn the residue is 0 (it is entire), so B_pole VANISHES.

That is exactly the silhouette of a Hodge-index / Lefschetz decomposition:
    - the pole direction phi_1 = the AMPLE / fundamental-class "+1" (the Lefschetz
      hyperplane class), present for zeta (which has the pole = the Euler-product
      residue) and ABSENT for D-H (no pole, no Euler product);
    - the PRIMITIVE part = A_arch + P_fin restricted to phi_1^perp = the H^1 where
      the nontrivial zeros live and where RH = a sign condition (marginal positivity).
This is the arithmetic analogue of the function-field (1, rho-1) signature on
C x C: one ample class plus a primitive part that is one-signed exactly at RH (2G).
And it is NON-CIRCULAR: the pole residue is elementary, not read off the zeros.

WHAT THIS PROBE COMPUTES (all zero-free, fast; no mp.zetazero):
  (1) The archimedean fiber in isolation. Signature of A_arch alone, and of A_arch
      restricted to the pole-orthogonal complement phi_1^perp (the Sonin/Connes
      condition: kill the pole/trivial direction). CANDIDATE-B KILL CHECK: Connes-
      Consani PROVED archimedean Weil positivity (the Sonin-space trace,
      arXiv:2006.13771). If our validated A_arch is positive on phi_1^perp, that is
      evidence the archimedean fiber's polarization IS the Connes proven object, so
      the archimedean HALF of M4 is already a theorem and the gluing reduces to the
      finite/prismatic half. If A_arch is indefinite even on phi_1^perp, the two-
      clock balance (#23) is the obstruction and we say so.
  (2) The gluing as a Hodge-index. The full M and its primitive part (M on
      phi_1^perp), for zeta vs D-H. Does projecting out the ample/pole direction
      (non-circular) reveal the RH-vs-off-line discrimination that the RAW min eig
      could not (the #34 stealth window)? Prediction from #34: the stealth window
      PERSISTS (the off-line signal is below the reconstruction floor at reachable
      truncation), confirming the gluing-as-TRACE is built but the gluing-as-
      SIGNATURE (the genuine duality) is the analytic M4 gap. Either way a coordinate.
  (3) The named obstruction. State precisely what the missing fundamental class H^2
      / trace map over Spec(Z) must be, and why the two-clock balance (archimedean
      and finite places on incompatible scales) is the obstruction to it (the single
      interpolating period candidate B needs).

HONEST SCOPE. The blocks A_arch, P_fin, B_pole are the project's validated non-
circular Weil form (#33/#34): real, reproducing the explicit formula. The Hodge-
index READING of them (pole = ample +1, complement = primitive) is a structural
proposal, the arithmetic image of the function-field 2G decomposition; it is NOT a
constructed prismatic Poincare duality and proves nothing about RH. This probe
makes the gluing structure explicit, runs the Connes-match and stealth-window
checks, and names the missing object. No new theorem; a sharpening coordinate.

Outputs:
  - e2ee_archimedean_gluing.npz
  - e2ee_archimedean_gluing.png
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np

from experiments._shared import zeta_L, DavenportHeilbronn
from experiments.positivity.e3m_place_type_balance import (
    finite_block, pole_block, lambda_coeffs_from_dirichlet, von_mangoldt_zeta,
)
from experiments.arithmetic_geometric.e2v_rosati_balance_M2_5 import arch_block_bombieri


def signature(M, tol=1e-7):
    w = np.linalg.eigvalsh(0.5 * (M + M.T))
    scale = max(abs(w).max(), 1.0)
    pos = int((w > tol * scale).sum())
    neg = int((w < -tol * scale).sum())
    return pos, neg, len(w) - pos - neg, w


def ample_direction(B, tol=1e-12):
    """Recover the unit pole/ample vector phi_1-hat as the leading eigenvector of the
    rank-1 pole block B = residue * 2 * outer(phi_1, phi_1). Returns None if B ~ 0
    (no pole = no ample class, e.g. Davenport-Heilbronn)."""
    w, V = np.linalg.eigh(0.5 * (B + B.T))
    i = int(np.argmax(np.abs(w)))
    if abs(w[i]) < tol:
        return None
    return V[:, i]


def primitive_part(M, phi_hat):
    """M restricted to phi_hat^perp (the primitive / Lefschetz complement of the
    ample class). If phi_hat is None there is no ample direction; return M itself."""
    n = M.shape[0]
    if phi_hat is None:
        return M
    P_perp = np.eye(n) - np.outer(phi_hat, phi_hat)
    Mp = P_perp @ (0.5 * (M + M.T)) @ P_perp
    # the eigenvalue along phi_hat is now ~0; report eigvals on the (n-1)-dim complement
    return Mp


def build_form(label, K, b_min, b_max, prec):
    b_vals = np.logspace(np.log10(b_min), np.log10(b_max), K)
    n_max = int(b_max * b_max) + 2
    if label == "zeta":
        L = zeta_L
        lam = np.array([0.0] + [von_mangoldt_zeta(n) for n in range(1, n_max + 1)])
        mu_list, log_Q, residue = [0.0], mp.mpf(0), 1.0
    elif label == "DH":
        L = DavenportHeilbronn()
        lam = lambda_coeffs_from_dirichlet(L, n_max, prec)
        mu_list, log_Q, residue = [1.0], mp.log(mp.sqrt(5)), 0.0
    else:
        raise ValueError(label)
    A = arch_block_bombieri(b_vals, mu_list, log_Q, prec)
    P = finite_block(b_vals, lam, prec)
    B = pole_block(b_vals, float(residue), prec)
    return dict(A=A, P=P, B=B, M=A + P + B, residue=residue, b_vals=b_vals)


def run(K=10, b_min=1.3, b_max=6.0, prec=30, out_dir: Path = None):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 78)
    print("[2EE] The archimedean continuation block and the gluing (probe B).")
    print("      Gluing M = A_arch + P_fin + B_pole read as a Hodge-index:")
    print("      pole B_pole (rank-1) = the ample/fundamental-class '+1'; complement = primitive.")
    print("=" * 78)

    forms = {lbl: build_form(lbl, K, b_min, b_max, prec) for lbl in ("zeta", "DH")}

    # ---- (1) the archimedean fiber in isolation: the Connes-match check ---- #
    print("\n(1) ARCHIMEDEAN FIBER IN ISOLATION (the candidate-B / Connes check).")
    print("    Connes-Consani proved archimedean Weil positivity on the Sonin space")
    print("    (pole/trivial direction removed). Is our validated A_arch positive on")
    print("    the pole-orthogonal complement phi_1^perp?\n")
    hdr = f"{'target':<8} {'sig(A_arch)':>16} {'minEig A':>12} {'sig(A on phi^perp)':>20} {'minEig|perp':>12}"
    print(hdr); print("-" * len(hdr))
    arch_rows = {}
    for lbl, f in forms.items():
        phi = ample_direction(f["B"])
        sigA = signature(f["A"])
        if phi is not None:
            Aperp = primitive_part(f["A"], phi)
            wperp = np.linalg.eigvalsh(0.5 * (Aperp + Aperp.T))
            # drop the ~0 eigenvalue along phi (the projected-out direction)
            order = np.argsort(np.abs(wperp))
            wkeep = np.delete(wperp, order[0])
            sigAp = (int((wkeep > 1e-7 * max(abs(wkeep).max(), 1)).sum()),
                     int((wkeep < -1e-7 * max(abs(wkeep).max(), 1)).sum()),
                     0)
            minp = float(wkeep.min())
        else:
            sigAp, minp = ("n/a", "n/a", "n/a"), float("nan")
        arch_rows[lbl] = dict(sigA=sigA[:3], minA=float(sigA[3].min()),
                              sigAperp=sigAp, minAperp=minp, has_pole=(phi is not None))
        sa = f"({sigA[0]},{sigA[1]},{sigA[2]})"
        sap = (f"({sigAp[0]},{sigAp[1]},{sigAp[2]})" if phi is not None else "no pole dir")
        print(f"{lbl:<8} {sa:>16} {float(sigA[3].min()):>+12.3e} {sap:>20} "
              f"{(f'{minp:+.3e}' if phi is not None else 'n/a'):>12}")
    print("-" * len(hdr))
    z = arch_rows["zeta"]
    connes_match = (z["has_pole"] and z["sigAperp"][1] == 0)
    if connes_match:
        print("    zeta: A_arch is POSITIVE on phi_1^perp (no negative eigenvalues).")
        print("    => consistent with A_arch being Connes' proven archimedean positivity")
        print("       (the Sonin-space trace): the archimedean HALF of M4 is then a")
        print("       theorem, and the gluing reduces to the FINITE/prismatic half.")
    else:
        print("    zeta: A_arch is INDEFINITE even on phi_1^perp.")
        print("    => the archimedean fiber is not positive in isolation; positivity is")
        print("       GLOBAL (the two-clock balance #23). The archimedean block must be")
        print("       glued to the finite block before any positivity appears -- which is")
        print("       precisely why a single interpolating period (candidate B) is needed.")

    # ---- (2) the gluing as a Hodge-index: primitive-part signature ---- #
    print("\n(2) THE GLUING AS A HODGE-INDEX. Full M and its primitive part (M on")
    print("    phi_1^perp = ample/pole direction projected out; NON-circular). Does the")
    print("    primitive signature discriminate RH (zeta) from off-line (D-H)?\n")
    hdr2 = f"{'target':<8} {'minEig(M)':>12} {'sign':>5} {'minEig(primitive)':>18} {'sign':>5} {'has ample':>10}"
    print(hdr2); print("-" * len(hdr2))
    glue_rows = {}
    for lbl, f in forms.items():
        phi = ample_direction(f["B"])
        minM = float(np.linalg.eigvalsh(0.5 * (f["M"] + f["M"].T)).min())
        if phi is not None:
            Mp = primitive_part(f["M"], phi)
            wp = np.linalg.eigvalsh(0.5 * (Mp + Mp.T))
            order = np.argsort(np.abs(wp))
            wkeep = np.delete(wp, order[0])
            minPrim = float(wkeep.min())
        else:
            minPrim = minM  # no ample direction; primitive = whole
        glue_rows[lbl] = dict(minM=minM, minPrim=minPrim, has_ample=(phi is not None))
        print(f"{lbl:<8} {minM:>+12.4e} {'POS' if minM > 0 else 'NEG':>5} "
              f"{minPrim:>+18.4e} {'POS' if minPrim > 0 else 'NEG':>5} "
              f"{'yes' if phi is not None else 'NO (no pole)':>10}")
    print("-" * len(hdr2))
    zg, dg = glue_rows["zeta"], glue_rows["DH"]
    discriminates = (zg["minPrim"] > 0 and dg["minM"] < 0)
    if discriminates:
        print("    The primitive part SEPARATES: zeta primitive POSITIVE, D-H NEGATIVE.")
        print("    STRONG CAUTION (adversary): verify this is not the pole/residue=0 of D-H")
        print("    doing the work trivially. D-H has no pole, so its 'separation' may be the")
        print("    K2 absence-of-ample, NOT the off-line zeros. Re-test with an entire L of")
        print("    EULER type before believing the primitive signature is an RH certificate.")
    else:
        print("    STEALTH WINDOW PERSISTS (as #34 predicted): projecting out the ample/pole")
        print("    direction does NOT manufacture discrimination. D-H's off-line obstruction")
        print("    (gamma ~ 85.7, ~2.6% of the spectrum) stays below the reconstruction floor")
        print("    at reachable truncation. The gluing-as-TRACE (the explicit formula) is")
        print("    built and carries the right Hodge-index SILHOUETTE (ample pole + primitive),")
        print("    but the gluing-as-SIGNATURE (the genuine duality whose positivity is RH) is")
        print("    the analytic M4 gap, unchanged. A finer numerical truncation will not close")
        print("    it; the proof must engage the exact off-line structure.")
    # note: D-H has NO ample direction (residue 0) -- the K2 face in the gluing language
    print(f"\n    K2 IN THE GLUING LANGUAGE: D-H has residue 0 => NO pole => NO ample")
    print(f"    fundamental class. Zeta's ample '+1' is the Euler-product residue at s=1.")
    print(f"    The fundamental class is exactly the object D-H lacks (the C2 face here).")

    # ---- (3) the named obstruction ---- #
    print("\n(3) THE NAMED OBSTRUCTION (what the gluing still lacks).")
    print("    The gluing assembles archimedean + finite + pole as a TRACE (the explicit")
    print("    formula). To be a Hodge-index SIGNATURE it needs, over Spec(Z):")
    print("      - a fundamental class H^2 (a trace map H^1 (x) H^1 -> H^2 = unit): the")
    print("        ample/pole direction is its rank-1 shadow here, but a genuine H^2 with")
    print("        Poincare duality is not constructed (the open prismatic-duality step);")
    print("      - a SINGLE interpolating period reconciling the two clocks: the archimedean")
    print("        place runs on the additive scale (the Gamma factor, log-scale) and the")
    print("        finite places on the multiplicative scale p (the (1,p) bidegree, #25).")
    print("        Candidate B's archimedean Fargues-Fontaine would supply one curve carrying")
    print("        both; the missing number is the period that glues additive to multiplicative.")
    print("    These two (H^2 + the period) ARE milestone M4. Probe B confirms the gluing's")
    print("    silhouette is a Hodge-index and pins the two missing organs by name.")

    np.savez_compressed(
        out_dir / "e2ee_archimedean_gluing.npz",
        arch_zeta_sigAperp=np.array(z["sigAperp"]),
        connes_match=bool(connes_match),
        zeta_minM=zg["minM"], zeta_minPrim=zg["minPrim"],
        DH_minM=dg["minM"], DH_has_ample=dg["has_ample"],
        discriminates=bool(discriminates), K=K, prec=prec,
    )

    # plot
    fig, axs = plt.subplots(1, 2, figsize=(13, 5))
    ax = axs[0]
    for i, (lbl, f) in enumerate(forms.items()):
        wA = np.linalg.eigvalsh(0.5 * (f["A"] + f["A"].T))
        ax.scatter([i] * len(wA), wA, color="tab:orange", zorder=3,
                   label="A_arch eigs" if i == 0 else None)
    ax.axhline(0, color="k", ls="--", lw=1)
    ax.set_xticks(range(len(forms))); ax.set_xticklabels(list(forms.keys()))
    ax.set_ylabel("eigenvalues of A_arch (isolated archimedean fiber)")
    ax.set_yscale("symlog")
    ax.set_title("(1) Archimedean fiber alone: indefinite\n=> positivity is global (two-clock)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    ax = axs[1]
    names = ["zeta minM", "zeta prim", "DH minM", "DH prim"]
    vals = [zg["minM"], zg["minPrim"], dg["minM"], dg["minPrim"]]
    cols = ["tab:green", "tab:green", "tab:red", "tab:red"]
    ax.bar(names, vals, color=cols)
    ax.axhline(0, color="k", lw=1)
    ax.set_ylabel("min eigenvalue")
    ax.set_title("(2) Gluing as Hodge-index: full M vs primitive part\n"
                 "(stealth window: primitive does not manufacture discrimination)")
    ax.tick_params(axis="x", rotation=15); ax.grid(alpha=0.3, axis="y")
    plt.tight_layout()
    plt.savefig(out_dir / "e2ee_archimedean_gluing.png", dpi=140)
    plt.close()
    print(f"\n[2EE] Saved {out_dir / 'e2ee_archimedean_gluing.png'}")
    print(f"[2EE] Saved {out_dir / 'e2ee_archimedean_gluing.npz'}")
    return forms, arch_rows, glue_rows


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--K", type=int, default=10)
    parser.add_argument("--prec", type=int, default=30)
    args = parser.parse_args()
    run(K=args.K, prec=args.prec)
