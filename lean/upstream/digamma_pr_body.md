# Mathlib PR body: digamma reflection, iterated recurrence, and duplication

This file is a ready-to-submit Mathlib PR body for three digamma identities that are
absent from current Mathlib master. The contribution is staged and kernel-verified in
[`../ZetaRH/DigammaExtras.lean`](../ZetaRH/DigammaExtras.lean) (Lean/Mathlib v4.30.0,
sorry-free, `#print axioms` clean). Copy the title and description below into the GitHub
PR form after completing the manual checklist at the end. This repository cannot open the
PR itself; the fork, CLA, and review steps are manual GitHub actions for Owen.

---

## 1. PR title

```
feat(Analysis/SpecialFunctions/Gamma/Digamma): reflection, iterated recurrence, and duplication for digamma
```

---

## 2. PR description

This PR adds three standard identities for `Complex.digamma` to
`Mathlib/Analysis/SpecialFunctions/Gamma/Digamma.lean`:

- the iterated recurrence `digamma (s + n) = digamma s + sum_{k < n} (s + k)⁻¹`,
- the reflection formula `digamma (1 - s) - digamma s = pi * cot (pi * s)`,
- the duplication (doubling) formula `digamma (2 * s) = (1/2) * (digamma s + digamma (s + 1/2)) + log 2`.

These are the natural digamma companions to results already in Mathlib:

- the single-step recurrence `Complex.digamma_apply_add_one` (the iterated form is its
  finite-induction closure);
- the Gamma reflection formula `Complex.Gamma_mul_Gamma_one_sub` (the digamma reflection
  is its logarithmic derivative);
- the Legendre duplication formula `Complex.Gamma_mul_Gamma_add_half` (the digamma
  duplication is its logarithmic derivative).

All three live in `namespace Complex` and target the existing file
`Mathlib/Analysis/SpecialFunctions/Gamma/Digamma.lean`. Each proof is short and uses only
existing Mathlib API (the `Gamma_mul_Gamma_*` product formulas plus the `logDeriv` calculus
lemmas `logDeriv_comp`, `logDeriv_mul`, `logDeriv_mul_const`, `logDeriv_div`, `logDeriv_apply`).
No new imports beyond the Gamma/Beta and `logDeriv` files are required; see the import note in
section 3.

The three theorems were developed and kernel-checked against Lean/Mathlib v4.30.0; the
`#print axioms` output for each is exactly `[propext, Classical.choice, Quot.sound]` (no
`sorryAx`, no `ofReduceBool`, no `native_decide`).

---

## 3. Theorem statements to add (verified signatures)

These are copied verbatim from the verified unit
[`../ZetaRH/DigammaExtras.lean`](../ZetaRH/DigammaExtras.lean), where they are proved
sorry-free. The proof bodies transfer verbatim; only the surrounding imports and (optionally)
the reflection RHS form may need adjustment to match the current master commit (see notes).

### 3.1 Iterated recurrence

```lean
/-- **The iterated digamma recurrence** `ψ(s+n) = ψ(s) + ∑_{k<n} 1/(s+k)`, for
    `s ∉ {0, -1, -2, …}`. Proved by induction from `digamma_apply_add_one`. -/
theorem digamma_apply_add_nat {s : ℂ} (hs : ∀ m : ℕ, s ≠ -(m : ℂ)) (n : ℕ) :
    digamma (s + n) = digamma s + ∑ k ∈ Finset.range n, (s + k)⁻¹
```

Relies on: `Complex.digamma_apply_add_one` (single-step recurrence) and `Finset.sum_range_succ`.
Proof is a straight induction on `n`.

### 3.2 Reflection

```lean
/-- **The digamma reflection formula** `ψ(1-s) - ψ(s) = π cot(π s)`, for `s ∉ ℤ`.
    Proved from `Complex.Gamma_mul_Gamma_one_sub` by taking logarithmic derivatives. -/
theorem digamma_reflection {s : ℂ} (hs : ∀ m : ℤ, s ≠ m) :
    digamma (1 - s) - digamma s
      = (Real.pi : ℂ) * (Complex.cos ((Real.pi : ℂ) * s) / Complex.sin ((Real.pi : ℂ) * s))
```

Relies on: `Complex.Gamma_mul_Gamma_one_sub`, `Complex.Gamma_ne_zero`,
`Complex.differentiableAt_Gamma`, `logDeriv_comp`, `logDeriv_mul`, `logDeriv_div`,
`logDeriv_apply`, `Complex.sin_eq_zero_iff`.

Note on the RHS form (RESOLVED against the pinned Mathlib v4.30.0): `Complex.cot` DOES exist
(`Mathlib/Analysis/Complex/Trigonometric.lean`, `def cot (z : ℂ) : ℂ`), along with
`Complex.cot_eq_cos_div_sin : cot x = cos x / sin x`. So a maintainer will almost certainly prefer
the RHS `(Real.pi : ℂ) * Complex.cot ((Real.pi : ℂ) * s)`. To switch to it, state the theorem goal
with `Complex.cot` and add `rw [Complex.cot_eq_cos_div_sin]` as the FIRST step of the proof (turning
the `cot` goal into the verified `cos / sin` form), after which the existing proof body closes
verbatim. The verified unit currently ships the explicit `cos / sin` form; both are correct, so this
is purely a maintainer-preference cosmetic. (Re-confirm `Complex.cot` is still present on whatever
master commit you rebase onto; it has been stable.)

### 3.3 Duplication

```lean
/-- **The digamma duplication formula** `ψ(2s) = ½(ψ(s) + ψ(s+½)) + log 2`, for
    `s, s+½ ∉ {0, -1, -2, …}`. Proved from Legendre's doubling
    `Complex.Gamma_mul_Gamma_add_half` by taking logarithmic derivatives. -/
theorem digamma_two_mul {s : ℂ} (hs : ∀ m : ℕ, s ≠ -(m : ℂ))
    (hsh : ∀ m : ℕ, s + 1 / 2 ≠ -(m : ℂ)) :
    digamma (2 * s) = (1 / 2) * (digamma s + digamma (s + 1 / 2)) + Complex.log 2
```

Relies on: `Complex.Gamma_mul_Gamma_add_half` (Legendre doubling), `Complex.Gamma_ne_zero`,
`Complex.differentiableAt_Gamma`, `logDeriv_comp`, `logDeriv_mul`, `logDeriv_mul_const`,
`Complex.cpow_def_of_ne_zero`, `HasDerivAt.cexp`. The proof handles the `Real.sqrt Real.pi`
and `2 ^ (1 - 2 z)` factors from the Legendre product by logarithmic differentiation.

### 3.4 Imports

`DigammaExtras.lean` builds these against the imports:

```lean
import Mathlib.Analysis.SpecialFunctions.Gamma.Digamma
import Mathlib.Analysis.SpecialFunctions.Gamma.Beta
import Mathlib.Analysis.SpecialFunctions.Gamma.Deriv
import Mathlib.Analysis.Calculus.LogDeriv
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
```

When dropping the theorems into the in-tree `Digamma.lean`, the `Digamma` import is the file
itself, so the only genuinely new dependency to add at the top of `Digamma.lean` is
`Mathlib.Analysis.SpecialFunctions.Gamma.Beta` (for the `Gamma_mul_Gamma_one_sub` and
`Gamma_mul_Gamma_add_half` product formulas). Confirm via shake/import-minimization (section 4)
whether `Gamma.Deriv`, `Calculus.LogDeriv`, and the `BigOperators` Finset file are already
transitively available through `Digamma.lean`'s existing imports; add only what shake reports as
missing.

### 3.5 Naming note for the maintainer

The verified file names the reflection theorem `digamma_reflection`. An earlier staging note
proposed `digamma_one_sub_sub` (read literally as "one sub, sub", matching the LHS
`digamma (1 - s) - digamma s`). Mathlib naming convention would tend to favor the descriptive
`digamma_reflection` (paralleling `Gamma`'s reflection lemma name), so this PR uses
`digamma_reflection`. Defer to maintainer preference if they request a rename; the proof body is
unaffected.

---

## 4. Remaining manual steps for Owen (checklist)

This repository cannot open the PR. The following are manual GitHub steps. Do them in order.

- [ ] **Fork mathlib4.** Fork `leanprover-community/mathlib4` on GitHub and clone your fork
      locally (or use an existing fork). Create a feature branch, e.g.
      `git switch -c digamma-reflection-recurrence-duplication`.
- [ ] **Sign the Mathlib CLA.** First-time contributors must sign the Contributor License
      Agreement. The CLA-assistant bot comments on the PR with a sign link; signing once
      covers all future PRs. (Sign at the link the bot posts, or pre-sign via the CLA-assistant
      page.)
- [ ] **Rebase the three theorems onto the current master commit.** `DigammaExtras.lean` was
      built against the v4.30.0 tag (commit `c5ea00351...`); master may have drifted. Pull the
      latest `master`, then drop the three theorems (sections 3.1 to 3.3) into
      `Mathlib/Analysis/SpecialFunctions/Gamma/Digamma.lean` inside the existing
      `namespace Complex ... end Complex` block. Place them after `digamma_apply_add_one`
      (recurrence) and near the special-value lemmas. Add only the imports shake says are
      missing (section 3.4).
- [ ] **Reflection RHS form (already resolved).** `Complex.cot` is present in v4.30.0
      (`Complex.cot_eq_cos_div_sin`), so prefer the RHS `(Real.pi : ℂ) * Complex.cot ((Real.pi : ℂ) * s)`:
      state the goal with `Complex.cot` and add `rw [Complex.cot_eq_cos_div_sin]` as the first proof
      step (see section 3.2). Re-run the proof to confirm it still closes on your rebase commit.
- [ ] **Build the touched file.** From the mathlib4 root, build just the target to confirm green:
      `lake build Mathlib.Analysis.SpecialFunctions.Gamma.Digamma`
      (a full `lake build` is unnecessary and slow). Confirm the three `#print axioms` outputs
      are still `[propext, Classical.choice, Quot.sound]`, then DELETE the `#print axioms` lines
      before committing (they are diagnostic only and not wanted in the library file).
- [ ] **Run the style linter.** `lake exe lint-style` (text/style linter) and the in-file
      `#lint`/environment linters that CI runs. Fix any line-length, docstring, or naming-lint
      reports. Confirm each new theorem has a module-consistent docstring (the staged docstrings
      already follow the `/-- ... -/` convention).
- [ ] **Run shake / import minimization.** `lake exe shake --fix` (or `python3 scripts/shake.py`
      per current tooling) to minimize imports and confirm `Gamma.Beta` is the only added
      dependency that is actually needed; remove any import shake flags as redundant.
- [ ] **Commit and push to your fork.** Use a Conventional-Commits message matching the PR title,
      e.g. `feat(Analysis/SpecialFunctions/Gamma/Digamma): reflection, iterated recurrence, and duplication for digamma`.
- [ ] **Open the PR.** Target `leanprover-community/mathlib4:master` from your branch. Paste the
      title (section 1) and description (section 2) into the PR form. Mathlib CI (build + linters)
      runs automatically; wait for green.
- [ ] **Request a topic-area review.** Post in the Lean Zulip `#mathlib4` (or the PR-review
      stream) noting the PR number and that it adds digamma reflection/recurrence/duplication; add
      the `awaiting-review` label if you have triage rights, otherwise a maintainer will.
- [ ] **Respond to review.** Address maintainer comments (likely: lemma naming such as
      `digamma_reflection` vs an alternative, RHS cotangent form, hypothesis phrasing
      `∀ m : ℕ, s ≠ -(m : ℂ)` vs an existing `s ∉ ...` predicate, and golfing). Push fixups to the
      same branch; CI re-runs. Once approved, a maintainer adds it to the merge queue.

---

## 5. What this proves / what remains

**Proves.** The three identities are mathematically and formally established: they compile
sorry-free against the real upstream `Complex.digamma` on Lean/Mathlib v4.30.0, with
`#print axioms` showing only the foundational axioms `propext`, `Classical.choice`, `Quot.sound`.
No `axiom`, no `sorry`, no `native_decide`. They depend solely on existing Mathlib API.

**Remains.** Purely procedural/manual: rebasing onto current master (in case of post-v4.30.0
drift), the maintainer-facing naming and RHS-form decisions (section 3.5, section 3.2), the
CLA and fork, and review iteration. None of these is a mathematical gap; they are the standard
Mathlib submission workflow, which must be carried out by a human GitHub account.
