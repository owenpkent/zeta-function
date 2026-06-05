/-
Class C no-go: trace-blindness (Direction 8E ledger, Class C; the Lean kernel of
LEARNINGS #48, the Adiprasito-Huh-Katz arithmetic-blindness finding).

The function-field Hasse-Weil / Rosati positivity predicate `NegDef g q t`
genuinely DEPENDS on the Frobenius trace `t`: at `g = q = 1` it holds for `t = 0`
and fails for `t = 2` (it is equivalent to `t^2 < 4 g^2 q`). Therefore no
arithmetic-BLIND signature, meaning a predicate of the curve data `(g, q)` alone
with no slot for `t`, can decide it.

This is the Class C no-go. A combinatorial / matroid (Adiprasito-Huh-Katz)
Hodge-Riemann form has a signature that is an invariant of the combinatorial type
and does not see the Frobenius trace (project #40/#48: the same `(1, n-1)`
signature for `t = 2` and `t = 100`). By the theorem below such a form cannot
carry the RH-positivity content. It is a CONDITIONAL, K5-clean no-go: it prunes
the combinatorial-signature source and relocates the demand; it does not disprove
RH. The kernel formalized here is the logical core (a `t`-independent predicate
cannot equal a `t`-dependent one); tying it to the specific AHK `(1, n-1)`
rigidity is the paper argument of #48.

Companion: `lean/ZetaRH/HodgeIndex.lean` (the `IntersectionSignature.NegDef`
and `negDef_iff_hasseWeil` API this builds on).
-/

import ZetaRH.HodgeIndex

namespace ZetaRH.TraceBlindObstruction

open ZetaRH.HodgeIndex.IntersectionSignature

/-- The Hasse-Weil / Rosati positivity predicate is non-constant in the trace
`t`: at `g = q = 1` it holds at `t = 0` and fails at `t = 2`. This is the
concrete two-trace witness behind trace-blindness. -/
theorem negDef_depends_on_trace :
    NegDef 1 1 0 ∧ ¬ NegDef 1 1 2 := by
  refine ⟨(negDef_iff_hasseWeil one_pos).mpr ?_, ?_⟩
  · norm_num
  · rw [negDef_iff_hasseWeil one_pos]; norm_num

/-- Class C no-go (trace-blindness). No arithmetic-blind signature, that is no
predicate `P g q` of the curve data `(g, q)` alone with no slot for the Frobenius
trace `t`, can decide the Hasse-Weil / Rosati positivity `NegDef g q t` for all
`g, q, t` with `g > 0`. The combinatorial (AHK) Hodge-Riemann signature is such a
`t`-blind invariant, so it cannot carry the RH-positivity content. -/
theorem no_trace_blind_signature :
    ¬ ∃ P : ℝ → ℝ → Prop, ∀ g q t : ℝ, 0 < g → (NegDef g q t ↔ P g q) := by
  rintro ⟨P, hP⟩
  obtain ⟨h0, h2⟩ := negDef_depends_on_trace
  have hP0 : P 1 1 := (hP 1 1 0 one_pos).mp h0
  have hP2 : ¬ P 1 1 := fun h => h2 ((hP 1 1 2 one_pos).mpr h)
  exact hP2 hP0

end ZetaRH.TraceBlindObstruction
