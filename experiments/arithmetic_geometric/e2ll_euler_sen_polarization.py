"""2LL: finite Euler-Sen polarization probe.

This is the first cheap falsification attempt for the proposal in
docs/03_research/euler_sen_polarization_attempt.md.

The old 2KK WCart finite model used a semisimple Sen weight ladder and a diagonal
Hodge-star on the rank-2 cup support. That is rigidly hyperbolic and has wrong
polarity. This experiment tests the proposed replacement:

  - put a genuine defective Sen/Jordan block at the Tate center -1/2;
  - solve the exact cup derivation equation Theta^T Omega + Omega Theta = -Omega;
  - use the nilpotent part N = Theta + (1/2)I to form the primitive pairing
        Q_N(x,y) = Omega(x, N y)
    on the top primitive vectors;
  - compare with the naive diagonal-star form, which remains hyperbolic.

The finite model is intentionally function-field shaped. Given the genus-g
Frobenius/Rosati matrix

    B_E(g,q,t) = [[2g, t], [t, 2gq]],

the Euler-Sen construction builds H = P top + N(P) lower, with

    N(top_i) = lower_i,
    Omega(top_i, lower_j) = B_E[i,j],
    Theta = -1/2 I + N.

Then the derivation equation is exact and the primitive monodromy form on P is
exactly B_E. So positivity is equivalent to t^2 < 4 g^2 q, the function-field
Hasse-Weil/Rosati bound. This does NOT prove RH over Z; it shows the Euler-Sen
formalism can avoid 2KK's rank-2 hyperbolic trap in the one finite model where
the right answer is known.

Run:
  python -m experiments.arithmetic_geometric.e2ll_euler_sen_polarization

Outputs:
  experiments/arithmetic_geometric/e2ll_euler_sen_polarization.npz
  experiments/arithmetic_geometric/e2ll_euler_sen_polarization.png, optional with --plot
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

import numpy as np


def hermitian_part(A: np.ndarray) -> np.ndarray:
    return 0.5 * (A + A.conj().T)


def signature(A: np.ndarray, tol: float = 1e-9):
    """Return (positive, negative, zero, eigenvalues) for the Hermitian part."""
    H = hermitian_part(A)
    w = np.linalg.eigvalsh(H)
    scale = max(float(np.max(np.abs(w))) if w.size else 0.0, 1.0)
    pos = int(np.sum(w > tol * scale))
    neg = int(np.sum(w < -tol * scale))
    return pos, neg, int(len(w) - pos - neg), w


def sig_label(sig) -> str:
    p, n, z, _ = sig
    if n == 0 and z == 0:
        return "POS"
    if p == 0 and z == 0:
        return "NEG"
    if z > 0 and p == 0 and n == 0:
        return "ZERO"
    return "INDEF"


def euler_rosati_B(g: float, q: float, t: float) -> np.ndarray:
    """The positive Rosati face of the 2G primitive intersection matrix."""
    return np.array([[2.0 * g, t], [t, 2.0 * g * q]], dtype=float)


@dataclass
class EulerSenPackage:
    B: np.ndarray
    Omega: np.ndarray
    N: np.ndarray
    Theta: np.ndarray
    top: np.ndarray
    lower: np.ndarray


def build_euler_sen(B: np.ndarray, has_euler_product: bool = True) -> EulerSenPackage:
    """Build the finite Euler-Sen package from an Euler/Rosati form B.

    The structural guard is deliberately data-based, not name-based: without
    Euler product data, the package does not form.
    """
    if not has_euler_product:
        raise ValueError("no Euler product data: no Frobenius bidegrees, no Tate cup target")
    B = np.array(B, dtype=float)
    if B.shape[0] != B.shape[1]:
        raise ValueError("B must be square")
    if not np.allclose(B, B.T, atol=1e-12):
        raise ValueError("B must be symmetric")
    r = B.shape[0]
    z = np.zeros_like(B)
    # Basis order: top primitive vectors p_i, then lower vectors ell_i = N p_i.
    Omega = np.block([[z, B], [-B, z]])
    N = np.block([[z, z], [np.eye(r), z]])
    Theta = -0.5 * np.eye(2 * r) + N
    top = np.vstack([np.eye(r), np.zeros((r, r))])
    lower = np.vstack([np.zeros((r, r)), np.eye(r)])
    return EulerSenPackage(B=B, Omega=Omega, N=N, Theta=Theta, top=top, lower=lower)


def derivation_residual(pkg: EulerSenPackage) -> float:
    """Residual for Theta^T Omega + Omega Theta = -Omega."""
    R = pkg.Theta.T @ pkg.Omega + pkg.Omega @ pkg.Theta + pkg.Omega
    return float(np.linalg.norm(R))


def nilpotent_diagnostics(pkg: EulerSenPackage):
    N = pkg.N
    N2 = N @ N
    rank_N = int(np.linalg.matrix_rank(N, tol=1e-10))
    rank_N2 = int(np.linalg.matrix_rank(N2, tol=1e-10))
    # Since Theta = -1/2 I + N, the eigenspace dimension is dim ker N.
    geom_mult = pkg.Theta.shape[0] - rank_N
    alg_mult = pkg.Theta.shape[0]
    defective = rank_N > 0 and geom_mult < alg_mult
    return {
        "rank_N": rank_N,
        "rank_N2": rank_N2,
        "geom_mult": geom_mult,
        "alg_mult": alg_mult,
        "defective": defective,
        "N2_norm": float(np.linalg.norm(N2)),
    }


def primitive_monodromy_form(pkg: EulerSenPackage) -> np.ndarray:
    """Q_N on top primitive vectors: top^T Omega N top."""
    return pkg.top.T @ pkg.Omega @ pkg.N @ pkg.top


def naive_diagonal_star_form(pkg: EulerSenPackage) -> np.ndarray:
    """The 2KK-style diagonal-star baseline.

    This form remains hyperbolic: Omega composed with a diagonal sign between
    top and lower gives [[0,-B],[-B,0]], whose eigenvalues are +/- singular values
    of B. It is included to check that the new signal is really from N.
    """
    r = pkg.B.shape[0]
    star = np.diag(np.r_[np.ones(r), -np.ones(r)])
    return hermitian_part(pkg.Omega @ star)


def hasse_weil_holds(g: float, q: float, t: float) -> bool:
    return t * t < 4.0 * g * g * q


def run(out_dir: Path | None = None, q_values=(5, 7, 11), g=1, t_margin=3, plot=False):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 80)
    print("[2LL] Euler-Sen finite polarization probe")
    print("      genuine defective Theta = -1/2 I + N, N^2=0")
    print("      exact cup equation Theta^T Omega + Omega Theta = -Omega")
    print("      primitive form Q_N(x,y)=Omega(x,N y) on top vectors")
    print("=" * 80)

    rows = []
    for q in q_values:
        bound = 2.0 * g * np.sqrt(q)
        t_min = -int(np.ceil(bound)) - t_margin
        t_max = int(np.ceil(bound)) + t_margin
        for t in range(t_min, t_max + 1):
            B = euler_rosati_B(g, q, t)
            pkg = build_euler_sen(B, has_euler_product=True)
            QN = primitive_monodromy_form(pkg)
            Qstar = naive_diagonal_star_form(pkg)
            sig_QN = signature(QN)
            sig_star = signature(Qstar)
            hw = hasse_weil_holds(g, q, t)
            qn_pos = sig_label(sig_QN) == "POS"
            rows.append(
                {
                    "q": q,
                    "t": t,
                    "bound": bound,
                    "det_B": float(np.linalg.det(B)),
                    "hw": hw,
                    "qn_sig": sig_QN[:3],
                    "qn_pos": qn_pos,
                    "star_sig": sig_star[:3],
                    "resid": derivation_residual(pkg),
                }
            )

    mismatch = [r for r in rows if r["hw"] != r["qn_pos"]]
    star_rigid = all(r["star_sig"][0] == r["star_sig"][1] and r["star_sig"][2] == 0 for r in rows)

    # A representative on-line and off-bound pair for q=5.
    B_good = euler_rosati_B(g, 5, 4)   # 16 < 20, positive
    B_bad = euler_rosati_B(g, 5, 5)    # 25 > 20, indefinite
    good = build_euler_sen(B_good, has_euler_product=True)
    bad = build_euler_sen(B_bad, has_euler_product=True)

    print("\nRepresentative q=5 cases:")
    for name, t, pkg in [("inside Hasse-Weil", 4, good), ("outside Hasse-Weil", 5, bad)]:
        QN = primitive_monodromy_form(pkg)
        Qstar = naive_diagonal_star_form(pkg)
        diag = nilpotent_diagnostics(pkg)
        print(f"  {name:22s} t={t:+d}:")
        print(f"    derivation residual       {derivation_residual(pkg):.3e}")
        print(
            "    N diagnostics             "
            f"rank N={diag['rank_N']}, rank N^2={diag['rank_N2']}, "
            f"geom/alg={diag['geom_mult']}/{diag['alg_mult']}, defective={diag['defective']}"
        )
        print(f"    primitive Q_N signature   {signature(QN)[:3]} {sig_label(signature(QN))}")
        print(f"    diagonal-star signature   {signature(Qstar)[:3]} {sig_label(signature(Qstar))}")

    print("\nSweep verdict:")
    print(f"  q values checked: {list(q_values)}, genus g={g}")
    print(f"  primitive Q_N positivity matches t^2 < 4 g^2 q: {len(mismatch) == 0}")
    print(f"  mismatches: {len(mismatch)}")
    print(f"  naive diagonal-star form rigidly hyperbolic on every row: {star_rigid}")

    # Structural D-H nonformation guard.
    dh_nonformation = False
    try:
        build_euler_sen(B_good, has_euler_product=False)
    except ValueError:
        dh_nonformation = True
    print(f"  no-Euler-product guard blocks package formation: {dh_nonformation}")

    if len(mismatch) == 0 and star_rigid and dh_nonformation:
        print("\nVERDICT: survives the cheap kill.")
        print("  The monodromy primitive form is not the 2KK hyperbolic Hodge-star form:")
        print("  it recovers the Euler/Rosati matrix and flips exactly at the")
        print("  function-field Hasse-Weil bound. This is a formalism survival result,")
        print("  not an RH proof: the Euler/Rosati form B_E is supplied as input.")
    else:
        print("\nVERDICT: kill or revise.")
        print("  At least one mandatory guard failed.")

    out_npz = out_dir / "e2ll_euler_sen_polarization.npz"
    np.savez_compressed(
        out_npz,
        q=np.array([r["q"] for r in rows], dtype=float),
        t=np.array([r["t"] for r in rows], dtype=float),
        bound=np.array([r["bound"] for r in rows], dtype=float),
        det_B=np.array([r["det_B"] for r in rows], dtype=float),
        hw=np.array([r["hw"] for r in rows], dtype=bool),
        qn_pos=np.array([r["qn_pos"] for r in rows], dtype=bool),
        qn_sig=np.array([r["qn_sig"] for r in rows], dtype=int),
        star_sig=np.array([r["star_sig"] for r in rows], dtype=int),
        resid=np.array([r["resid"] for r in rows], dtype=float),
        mismatch_count=len(mismatch),
        star_rigid=star_rigid,
        dh_nonformation=dh_nonformation,
    )
    plot_path = out_dir / "e2ll_euler_sen_polarization.png"
    plotted = _plot(rows, plot_path) if plot else False
    print(f"\n[2LL] saved {out_npz}")
    if plotted:
        print(f"[2LL] saved {plot_path}")
    elif plot:
        print("[2LL] plot skipped: matplotlib is unavailable or incompatible in this environment")

    return rows


def _plot(rows, path: Path) -> bool:
    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception as exc:
        print(f"[2LL] plot unavailable: {exc}")
        return False

    q_values = sorted({r["q"] for r in rows})
    fig, axes = plt.subplots(1, len(q_values), figsize=(5.2 * len(q_values), 4.2), sharey=True)
    if len(q_values) == 1:
        axes = [axes]
    for ax, q in zip(axes, q_values):
        sub = [r for r in rows if r["q"] == q]
        t = np.array([r["t"] for r in sub])
        det = np.array([r["det_B"] for r in sub])
        qn_pos = np.array([r["qn_pos"] for r in sub])
        bound = sub[0]["bound"]
        colors = np.where(qn_pos, "tab:blue", "tab:red")
        ax.scatter(t, det, c=colors, zorder=3)
        ax.axhline(0, color="black", lw=1, ls="--")
        ax.axvline(bound, color="gray", lw=1, ls=":")
        ax.axvline(-bound, color="gray", lw=1, ls=":")
        ax.set_title(f"q={q}: primitive Q_N det")
        ax.set_xlabel("Frobenius trace t")
        ax.grid(alpha=0.3)
    axes[0].set_ylabel("det B_E = 4 g^2 q - t^2")
    fig.suptitle("Euler-Sen primitive form flips exactly at the Hasse-Weil bound")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", type=Path, default=None)
    parser.add_argument("--q", type=int, nargs="*", default=[5, 7, 11])
    parser.add_argument("--plot", action="store_true")
    args = parser.parse_args()
    run(out_dir=args.out_dir, q_values=tuple(args.q), plot=args.plot)
