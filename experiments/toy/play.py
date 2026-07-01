"""The toy sandbox demo: grade the M4 move where the answer is known.

Run:
    python -m experiments.toy.play

It (1) prints the battery, (2) grades the two reference candidates (the e2xx moment
matrix and the #143 Schur-Cohn circle certificate: both all green, by independent
theorems), (3) grades two deliberately-bad candidates to show the grader has teeth, and
(4) runs the spectral (Selberg / Hilbert-Polya) toy. The point is the loop: write a
candidate construction, run it here, and get told instantly whether it reproduces Weil,
catches the off-line zeros, stayed K1-clean, and is immune to Davenport-Heilbronn.
"""

from __future__ import annotations

from experiments.toy.instances import FULL_BATTERY
from experiments.toy.grader import (
    grade,
    moment_matrix_candidate,
    schur_cohn_candidate,
    identity_candidate,
    diag_moment_candidate,
)
from experiments.toy import selberg


def show_battery() -> None:
    print("THE BATTERY (the answer key; candidates never see the eigenvalues)\n")
    for inst in FULL_BATTERY:
        if inst.has_euler:
            tag = "RH-true " if inst.rh_true else "RH-false"
            print(f"  {tag}  genus {inst.genus}  q={inst.q:<3}  "
                  f"circle-defect={inst.circle_defect():.2e}   {inst.name}")
        else:
            print(f"  RH-false  (no Euler product, no finite spectrum)        {inst.name}")
    print()


def main() -> None:
    print("=" * 78)
    print("RH TOY SANDBOX  --  a checkable training ground for the M4 move")
    print("=" * 78 + "\n")

    show_battery()

    print("-" * 78)
    print("GRADING CANDIDATES\n")
    print(grade(moment_matrix_candidate, "moment_matrix (reference, = e2xx G_m)").report())
    print()
    print(grade(schur_cohn_candidate,
                "schur_cohn (2nd reference, Cohn 1922 + Schur-Cohn, #143)").report())
    print()
    print(grade(identity_candidate, "identity (soft positivity, no RH content)").report())
    print()
    print(grade(diag_moment_candidate, "diagonal c_0 (unconditional norm, wrong polarity)").report())
    print()

    print("-" * 78)
    selberg.demo()

    print("\n" + "-" * 78)
    print(
        "THE CAVEAT (read before trusting a green scorecard):\n"
        "  The toy trains the MOVE; it cannot contain the OBSTRUCTION. The function-field\n"
        "  spectrum is finite and on one circle; zeta's is infinite and accumulates (the\n"
        "  (1,p) bidegree). The moment-matrix move that is ALL GREEN here provably DISSOLVES\n"
        "  over Z: zeta's Li sequence is log-concave, not a moment sequence (LEARNINGS #128\n"
        "  Front 2). So a green scorecard means 'the move is K1-clean and correct in the toy',\n"
        "  NOT 'it lifts to RH'. The delta between toy-success and Z-failure is the compass."
    )


if __name__ == "__main__":
    main()
