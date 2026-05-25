/-
The four kill criteria for evaluating proposed RH proof methods.

Defined in `experiments/arithmetic_geometric/2A_candidate_evaluation.md`
and reiterated in `experiments/PROOF_ARCHITECTURES_PLAN.md` § Why we test
kill criteria, not goals.

Skeleton only as of 2026-05-25.
-/

import ZetaRH.Basic
import ZetaRH.DavenportHeilbronn

namespace ZetaRH.KillCriteria

variable (Claim : Prop)
variable (L : LFunction)

/--
K1: the proposed intermediate claim is provably RH-equivalent (circular).

A method "proving" an intermediate claim P from which RH follows trivially is
circular if P is itself provably equivalent to RH. The R3.5 no-shortcut theorem
formalizes this for trace-formula NCG approaches.
-/
def K1_circularity : Prop :=
  Claim ↔ RiemannHypothesis L

/--
K2: the method gives the same conclusion for zeta and Davenport-Heilbronn.

D-H has a functional equation but no Euler product and known off-line zeros.
A method that "proves RH" for D-H is wrong because RH for D-H is provably false.
-/
def K2_dh_blind (M : LFunction → Prop) : Prop :=
  M zeta_function ∧ M davenport_heilbronn

/--
K3: the method does not survive contact with a worked function-field example.

If the method, restricted to a curve over F_q, fails to recover Weil's 1948
proof, it is missing essential structure.
-/
def K3_function_field_failure : Prop :=
  True  -- placeholder; precise form requires curves-over-F_q infrastructure

/--
K4: the method's central object cannot be constructed without invoking
RH-strength input.

Many proposed constructions implicitly assume RH (or GRH-strength results)
in their setup. K4 flags this.
-/
def K4_rh_input_required : Prop :=
  True  -- placeholder

/-- The R3.5 no-shortcut theorem (LEARNINGS finding context).

In Lean form: every trace-formula NCG framework with standard spectral
identification has positivity ⟺ RH. Skeleton; proof TBD. -/
theorem no_shortcut_theorem_sketch (P : Prop) :
    (P ↔ RiemannHypothesis zeta_function) → K1_circularity P zeta_function := by
  intro h
  unfold K1_circularity
  exact h

end ZetaRH.KillCriteria
