"""2MM: Euler-Sen K1 audit.

This is the adversarial follow-up to 2LL. 2LL showed that the Euler-Sen
monodromy primitive form avoids the 2KK diagonal-star hyperbolic trap in the
function-field specialization:

    Q_N(x,y) = Omega(x, N y) = B_E(x,y).

That survival result has an obvious K1 risk: if the finite formalism simply
transports the supplied symmetric form B, then it creates no positivity. The
missing theorem is still the geometric construction and positivity of B.

This module tests that risk directly:

  1. Sweep arbitrary symmetric input forms B of every signature in dimensions
     1..6 and verify Q_N has exactly the same signature as B.
  2. Verify the old diagonal-star baseline is rigidly hyperbolic for every
     nondegenerate B.
  3. Run a D-H control through a data-based Euler-product formation guard. A
     renamed Davenport-Heilbronn wrapper still fails because the guard reads
     has_euler_product, not the object name.

Run:
  python -m experiments.arithmetic_geometric.e2mm_euler_sen_k1_audit

Output:
  experiments/arithmetic_geometric/e2mm_euler_sen_k1_audit.npz
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from experiments._shared import DavenportHeilbronn, chi3_L, chi4_L, zeta_L
from experiments.arithmetic_geometric.e2ll_euler_sen_polarization import (
    build_euler_sen,
    derivation_residual,
    euler_rosati_B,
    naive_diagonal_star_form,
    primitive_monodromy_form,
    signature,
    sig_label,
)


@dataclass(frozen=True)
class EulerProductData:
    """Toy Euler-product formation witness for the finite audit.

    The important part is that this is derived from L.has_euler_product rather
    than L.name. It mirrors the Lean formation guard at toy Python level.
    """

    name: str
    has_euler_product: bool
    has_functional_equation: bool
    bidegree_rule: str = "(1,p)"


class RenamedLFunction:
    """Wrapper used to attack name-based guards."""

    def __init__(self, inner, name: str):
        self.inner = inner
        self.name = name
        self.has_euler_product = bool(getattr(inner, "has_euler_product", False))
        self.has_functional_equation = bool(getattr(inner, "has_functional_equation", False))

    def __repr__(self):
        return f"<RenamedLFunction {self.name}>"


def require_euler_product_data(L) -> EulerProductData:
    """Return Euler-product data or raise before any cup package is built."""
    has_euler = bool(getattr(L, "has_euler_product", False))
    name = getattr(L, "name", type(L).__name__)
    if not has_euler:
        raise ValueError(f"{name}: no Euler product data, so no Frobenius Tate cup target")
    return EulerProductData(
        name=name,
        has_euler_product=True,
        has_functional_equation=bool(getattr(L, "has_functional_equation", False)),
    )


def build_euler_sen_from_lfunction(B: np.ndarray, L):
    data = require_euler_product_data(L)
    return build_euler_sen(B, has_euler_product=data.has_euler_product)


def symmetric_with_signature(dim: int, n_pos: int, n_neg: int, n_zero: int, rng) -> np.ndarray:
    if n_pos + n_neg + n_zero != dim:
        raise ValueError("signature counts must add to dim")
    eigs = []
    if n_pos:
        eigs.extend(np.linspace(1.0, 2.0, n_pos))
    if n_neg:
        eigs.extend(-np.linspace(1.0, 2.0, n_neg))
    if n_zero:
        eigs.extend([0.0] * n_zero)
    eigs = np.array(eigs, dtype=float)
    rng.shuffle(eigs)
    A = rng.normal(size=(dim, dim))
    Q, _ = np.linalg.qr(A)
    return Q @ np.diag(eigs) @ Q.T


def sig_tuple(A: np.ndarray) -> tuple[int, int, int]:
    return tuple(int(x) for x in signature(A)[:3])


def run(out_dir: Path | None = None, seed: int = 20260605, max_dim: int = 6):
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 80)
    print("[2MM] Euler-Sen K1 audit")
    print("      Does Q_N create positivity, or only transport the supplied form B?")
    print("=" * 80)

    rng = np.random.default_rng(seed)
    rows = []

    # All nondegenerate signatures in dimensions 1..max_dim.
    for dim in range(1, max_dim + 1):
        for n_pos in range(dim + 1):
            n_neg = dim - n_pos
            B = symmetric_with_signature(dim, n_pos, n_neg, 0, rng)
            rows.append(_audit_B(B, f"dim{dim}_pos{n_pos}_neg{n_neg}_zero0"))

        # One singular row per dimension, to check zero transport.
        if dim >= 2:
            B = symmetric_with_signature(dim, dim - 1, 0, 1, rng)
            rows.append(_audit_B(B, f"dim{dim}_singular_one_zero"))

    transport_mismatches = [r for r in rows if not r["transport_ok"]]
    star_mismatches = [r for r in rows if not r["star_expected_ok"]]

    print("\nSignature transport sweep:")
    print(f"  dimensions checked: 1..{max_dim}")
    print(f"  rows checked: {len(rows)}")
    print(f"  Q_N signature equals input B signature: {len(transport_mismatches) == 0}")
    print(f"  transport mismatches: {len(transport_mismatches)}")
    print(f"  diagonal-star baseline has expected hyperbolic signature: {len(star_mismatches) == 0}")
    print(f"  diagonal-star mismatches: {len(star_mismatches)}")

    # Function-field anchor from 2LL, included to show the audit agrees with the
    # known positive and off-bound cases.
    ff_good = _audit_B(euler_rosati_B(1, 5, 4), "ff_q5_t4_inside")
    ff_bad = _audit_B(euler_rosati_B(1, 5, 5), "ff_q5_t5_outside")
    print("\nFunction-field anchor:")
    for row in (ff_good, ff_bad):
        print(
            f"  {row['label']:18s} input B sig={row['B_sig']} "
            f"Q_N sig={row['QN_sig']} star sig={row['star_sig']} "
            f"resid={row['residual']:.1e}"
        )

    # D-H discipline. The renamed D-H object would defeat a string guard, but
    # not a data guard.
    dh = DavenportHeilbronn()
    renamed_dh = RenamedLFunction(dh, "mystery_euler_candidate")
    formation_targets = [
        ("zeta", zeta_L, True),
        ("chi3", chi3_L, True),
        ("chi4", chi4_L, True),
        ("D-H", dh, False),
        ("renamed D-H", renamed_dh, False),
    ]
    formation_rows = []
    print("\nFormation guard:")
    for label, L, expected in formation_targets:
        formed = False
        reason = ""
        try:
            build_euler_sen_from_lfunction(euler_rosati_B(1, 5, 4), L)
            formed = True
        except ValueError as exc:
            reason = str(exc)
        ok = formed == expected
        formation_rows.append((label, formed, expected, ok, reason))
        status = "FORMED" if formed else "blocked"
        print(f"  {label:12s} {status:7s} expected={expected} ok={ok}")
        if reason:
            print(f"    reason: {reason}")

    guard_ok = all(row[3] for row in formation_rows)

    verdict_ok = len(transport_mismatches) == 0 and len(star_mismatches) == 0 and guard_ok
    print("\nVERDICT:")
    if verdict_ok:
        print("  K1 audit PASS as a negative coordinate.")
        print("  The finite Euler-Sen primitive form is a transport formalism:")
        print("  signature(Q_N) = signature(B) for arbitrary symmetric B.")
        print("  It does not manufacture positivity. The real M4 theorem is still")
        print("  the non-circular geometric construction and positivity of B.")
    else:
        print("  Audit failed. Inspect mismatches before citing this coordinate.")

    out_npz = out_dir / "e2mm_euler_sen_k1_audit.npz"
    np.savez_compressed(
        out_npz,
        labels=np.array([r["label"] for r in rows + [ff_good, ff_bad]], dtype=object),
        B_sig=np.array([r["B_sig"] for r in rows + [ff_good, ff_bad]], dtype=int),
        QN_sig=np.array([r["QN_sig"] for r in rows + [ff_good, ff_bad]], dtype=int),
        star_sig=np.array([r["star_sig"] for r in rows + [ff_good, ff_bad]], dtype=int),
        residual=np.array([r["residual"] for r in rows + [ff_good, ff_bad]], dtype=float),
        transport_ok=np.array([r["transport_ok"] for r in rows + [ff_good, ff_bad]], dtype=bool),
        star_expected_ok=np.array([r["star_expected_ok"] for r in rows + [ff_good, ff_bad]], dtype=bool),
        formation_label=np.array([r[0] for r in formation_rows], dtype=object),
        formation_formed=np.array([r[1] for r in formation_rows], dtype=bool),
        formation_expected=np.array([r[2] for r in formation_rows], dtype=bool),
        formation_ok=np.array([r[3] for r in formation_rows], dtype=bool),
        transport_mismatch_count=len(transport_mismatches),
        star_mismatch_count=len(star_mismatches),
        formation_guard_ok=guard_ok,
        verdict_ok=verdict_ok,
    )
    print(f"\n[2MM] saved {out_npz}")
    return {
        "rows": rows,
        "ff_good": ff_good,
        "ff_bad": ff_bad,
        "formation_rows": formation_rows,
        "verdict_ok": verdict_ok,
    }


def _audit_B(B: np.ndarray, label: str) -> dict:
    pkg = build_euler_sen(B, has_euler_product=True)
    QN = primitive_monodromy_form(pkg)
    Qstar = naive_diagonal_star_form(pkg)

    b_sig = sig_tuple(B)
    qn_sig = sig_tuple(QN)
    star_sig = sig_tuple(Qstar)
    residual = derivation_residual(pkg)

    rank = b_sig[0] + b_sig[1]
    z = b_sig[2]
    expected_star = (rank, rank, 2 * z)
    transport_ok = b_sig == qn_sig and np.linalg.norm(QN - B) < 1e-9 and residual < 1e-9
    star_expected_ok = star_sig == expected_star

    return {
        "label": label,
        "B_sig": b_sig,
        "QN_sig": qn_sig,
        "star_sig": star_sig,
        "B_label": sig_label(signature(B)),
        "QN_label": sig_label(signature(QN)),
        "star_label": sig_label(signature(Qstar)),
        "residual": residual,
        "transport_ok": transport_ok,
        "star_expected_ok": star_expected_ok,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", type=Path, default=None)
    parser.add_argument("--seed", type=int, default=20260605)
    parser.add_argument("--max-dim", type=int, default=6)
    args = parser.parse_args()
    run(out_dir=args.out_dir, seed=args.seed, max_dim=args.max_dim)
