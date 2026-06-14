"""The function-field shadow: the positive-direction control (Generative Engine, 6d).

Spec: `docs/03_research/generative_engine.md` section 1. The mirror of the
Davenport-Heilbronn discipline. D-H is the negative filter ("a candidate must NOT
work for the counterexample"); the function-field shadow is the positive filter
("a candidate must reproduce the theorem where the theorem is known").

RH is a theorem over $\\mathbb{F}_q$ (Weil / Hasse): for an elliptic curve over
$\\mathbb{F}_p$ the Frobenius eigenvalues $\\alpha, \\bar\\alpha$ satisfy
$|\\alpha| = \\sqrt{p}$, i.e. they lie on the circle of radius $\\sqrt{q}$. So a
reformulation, specialized to $\\mathbb{F}_q$, either reproduces this (eigenvalues
on the circle) or it does not. Off-circle eigenvalues mean the reformulation
breaks the proven theorem, which is a kill.

This module provides genuine $\\mathbb{F}_q$ controls (real curves, on-circle) and
an off-line forgery (a hand-made off-circle eigenvalue set, the function-field
analogue of D-H), plus the shadow check. It is a positive evaluator: a candidate
that fails it is wrong, because it fails where RH is true.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass


@dataclass
class FqInstance:
    """A function-field specialization: eigenvalues of Frobenius at radius sqrt(q)."""
    name: str
    q: int                    # the field size (a prime p for an elliptic curve / F_p)
    eigenvalues: tuple        # complex Frobenius eigenvalues
    rh_true: bool             # whether RH (all |alpha| = sqrt(q)) is meant to hold here


def elliptic_eigenvalues(p: int, a: int) -> tuple:
    """Frobenius eigenvalues of an elliptic curve E/F_p with trace a = p + 1 - #E(F_p).
    Roots of x^2 - a x + p = 0. When a^2 < 4p they are complex conjugates with
    |alpha| = sqrt(p) exactly (Hasse = RH for the curve)."""
    disc = complex(a * a - 4 * p)
    root = cmath.sqrt(disc)
    return ((a + root) / 2, (a - root) / 2)


def circle_defect(eigenvalues, q: int) -> float:
    """max_i | |alpha_i| - sqrt(q) | / sqrt(q): the relative distance of the
    eigenvalues from the RH circle. ~0 iff RH holds at this F_q instance."""
    rq = math.sqrt(q)
    return max(abs(abs(z) - rq) for z in eigenvalues) / rq


# Genuine controls: real elliptic curves over F_p with a^2 < 4p, all on-circle.
FQ_CONTROLS = [
    FqInstance("E/F_5  (a=1)", 5, elliptic_eigenvalues(5, 1), rh_true=True),
    FqInstance("E/F_7  (a=2)", 7, elliptic_eigenvalues(7, 2), rh_true=True),
    FqInstance("E/F_11 (a=3)", 11, elliptic_eigenvalues(11, 3), rh_true=True),
    FqInstance("E/F_13 (a=4)", 13, elliptic_eigenvalues(13, 4), rh_true=True),
]


def _forgery(p: int, a: int, blow: float) -> FqInstance:
    """An off-line forgery: take a real curve and push one eigenvalue off the
    circle by factor `blow`. RH is FALSE here (the function-field analogue of D-H)."""
    e0, e1 = elliptic_eigenvalues(p, a)
    return FqInstance(f"forgery/F_{p} (blow={blow})", p, (e0 * blow, e1), rh_true=False)


FQ_FORGERY = _forgery(7, 2, 1.3)


# Shadow verdict.
SHADOW_PASS = "SHADOW_PASS"     # reproduces Weil (on-circle): consistent
SHADOW_KILL = "SHADOW_KILL"     # off-circle: breaks the proven F_q theorem
SHADOW_NA = "SHADOW_NA"         # no F_q specialization available


def fq_shadow_check(eigenvalues, q: int, tol: float = 1e-9) -> tuple:
    """The shadow filter. Returns (verdict, defect). On-circle (defect < tol)
    reproduces Weil and PASSES; off-circle KILLS (the specialization breaks RH
    where RH is a theorem)."""
    if not eigenvalues or q is None:
        return SHADOW_NA, None
    d = circle_defect(eigenvalues, q)
    return (SHADOW_PASS if d < tol else SHADOW_KILL), d


def demo() -> None:
    print("Function-field shadow (6d): the positive-direction control\n")
    print("  GENUINE CONTROLS (RH = Hasse holds; eigenvalues on the sqrt(q) circle):")
    for c in FQ_CONTROLS:
        v, d = fq_shadow_check(c.eigenvalues, c.q)
        print(f"    {c.name:18} defect={d:.2e}  -> {v}")
    print("\n  OFF-LINE FORGERY (RH false; the F_q analogue of Davenport-Heilbronn):")
    v, d = fq_shadow_check(FQ_FORGERY.eigenvalues, FQ_FORGERY.q)
    print(f"    {FQ_FORGERY.name:18} defect={d:.2e}  -> {v}")
    print("\nThe shadow PASSES where RH is proven and KILLS the off-line forgery. "
          "A candidate\nthat cannot reproduce the F_q circle is not reformulating RH; it is breaking it.")


if __name__ == "__main__":
    demo()
