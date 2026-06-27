"""The RH toy sandbox: a checkable training ground for the M4 move.

Curves over a finite field are the toy world where RH is a THEOREM (Weil 1948,
Deligne 1974) with the identical skeleton to the real problem: an Euler product,
a functional equation, and a positivity that is secretly a Hodge-index / Rosati
polarization (M4). Because the answer is known here, this sandbox can do the one
thing impossible over Z: grade a proposed M4 construction as right or wrong, and
catch a soft / circular / D-H-blind argument on contact.

Modules:
  instances : the positive battery (RH true) and negative battery (RH false: the
              function-field analogue of Davenport-Heilbronn) + the candidate's
              K1-clean data view.
  grader    : the four-part grader (reproduce-Weil / reject-fakes / K1-clean /
              D-H-immune) + the reference candidate (the e2xx moment matrix).
  selberg   : the spectral toy (self-adjoint operator => zeros on the line),
              the Architecture-1 (Hilbert-Polya) training ground.
  play      : the top-level demo tying it together.

The honest caveat: the toy trains the MOVE, it cannot contain the OBSTRUCTION.
The function-field spectrum is finite and sits on one circle; zeta's is infinite
and accumulates (the (1,p) bidegree). The delta between toy-success and Z-failure
is the compass, not the proof. See README.md and LEARNINGS #128 Front 2.
"""

from experiments.toy.instances import (
    ToyInstance,
    ToyData,
    POSITIVE_BATTERY,
    NEGATIVE_BATTERY,
    FULL_BATTERY,
)
from experiments.toy.grader import (
    grade,
    moment_matrix_candidate,
    is_psd,
    Scorecard,
)

__all__ = [
    "ToyInstance",
    "ToyData",
    "POSITIVE_BATTERY",
    "NEGATIVE_BATTERY",
    "FULL_BATTERY",
    "grade",
    "moment_matrix_candidate",
    "is_psd",
    "Scorecard",
]
