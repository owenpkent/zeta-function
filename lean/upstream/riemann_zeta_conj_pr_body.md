# Mathlib PR body: conjugation symmetry of the Riemann zeta function

This file is a ready-to-submit Mathlib PR body for the reflection (conjugation) symmetry
`riemannZeta (conj s) = conj (riemannZeta s)`, which is absent from current Mathlib. The
contribution is staged and kernel-verified in
[`../ZetaRH/RiemannZetaConj.lean`](../ZetaRH/RiemannZetaConj.lean) (Lean/Mathlib v4.30.0,
sorry-free, `#print axioms` clean, project-dependency-free: imports only Mathlib). Copy the title
and description below into the GitHub PR form after completing the manual checklist at the end. This
repository cannot open the PR itself; the fork, CLA, and review steps are manual GitHub actions for
Owen.

---

## 1. PR title

```
feat(NumberTheory/LSeries/RiemannZeta): conjugation symmetry of riemannZeta
```

---

## 2. PR description

This PR adds the reflection (conjugation) symmetry of the Riemann zeta function to
`Mathlib/NumberTheory/LSeries/RiemannZeta.lean`:

- `riemannZeta_conj` : for `s ≠ 1`, `riemannZeta (conj s) = conj (riemannZeta s)`;
- `riemannZeta_conj_eq_zero_iff` : for `s ≠ 1`, `riemannZeta (conj s) = 0 ↔ riemannZeta s = 0`
  (the zeros are symmetric under complex conjugation).

This is the natural companion to the functional equation already in Mathlib
(`riemannZeta_one_sub`). Together the two symmetries `s ↦ 1 - s` and `s ↦ conj s` generate the
quadruple symmetry `{ρ, 1-ρ, conj ρ, 1-conj ρ}` of the nontrivial zeros, and the reflection
symmetry alone is a basic, frequently-used fact (it is why the zeros come in conjugate pairs).

Mathematical content: ζ has real Dirichlet coefficients, so on `Re s > 1` the identity
`conj (ζ (conj s)) = ζ s` holds termwise from `zeta_eq_tsum_one_div_nat_cpow` and
`conj ((n : ℂ) ^ w) = (n : ℂ) ^ conj w` (`Complex.conj_cpow` + `Complex.conj_tsum`). The identity
principle for analytic functions (`AnalyticOnNhd.eqOn_of_preconnected_of_eventuallyEq`) then
propagates it across the connected domain `ℂ ∖ {1}`. Analyticity of `conj ∘ ζ ∘ conj` is the
anti-holomorphic composition `HasDerivAt.conj_conj`; preconnectedness of `ℂ ∖ {1}` is
`isConnected_compl_singleton_of_one_lt_rank` together with `Complex.rank_real_complex`.

Both theorems were developed and kernel-checked against Lean/Mathlib v4.30.0; the `#print axioms`
output for each is exactly `[propext, Classical.choice, Quot.sound]` (no `sorryAx`, no
`native_decide`). The staged unit imports only Mathlib (no project dependencies), so the proof
bodies transfer verbatim.

---

## 3. Theorem statements to add (verified signatures)

These are copied verbatim from the verified unit
[`../ZetaRH/RiemannZetaConj.lean`](../ZetaRH/RiemannZetaConj.lean), where they are proved
sorry-free at top level (matching `riemannZeta_one_sub`'s placement), under `open Complex
ComplexConjugate`.

### 3.1 Reflection symmetry

```lean
/-- **Conjugation symmetry of the Riemann zeta function:** `ζ(s̄) = conj ζ(s)` for `s ≠ 1`. -/
theorem riemannZeta_conj {s : ℂ} (hs : s ≠ 1) :
    riemannZeta (conj s) = conj (riemannZeta s)
```

Relies on: `zeta_eq_tsum_one_div_nat_cpow`, `Complex.conj_cpow`, `Complex.conj_natCast`,
`Complex.conj_tsum`, `differentiableAt_riemannZeta`, `HasDerivAt.conj_conj`,
`analyticOn_riemannZeta`, `AnalyticOnNhd.eqOn_of_preconnected_of_eventuallyEq`,
`isConnected_compl_singleton_of_one_lt_rank`, `Complex.rank_real_complex`,
`Complex.arg_ofReal_of_nonneg`, `Complex.conj_re`, `Complex.conj_conj`.

### 3.2 Zeros are conjugation-symmetric

```lean
/-- The zeros of `riemannZeta` are symmetric under complex conjugation (away from the pole `s = 1`):
    `ζ(s̄) = 0 ↔ ζ(s) = 0`. -/
theorem riemannZeta_conj_eq_zero_iff {s : ℂ} (hs : s ≠ 1) :
    riemannZeta (conj s) = 0 ↔ riemannZeta s = 0
```

Proof: `rw [riemannZeta_conj hs]; simp` (conjugation is zero iff the argument is).

### 3.3 Imports

`RiemannZetaConj.lean` builds these against the imports:

```lean
import Mathlib.NumberTheory.LSeries.RiemannZeta
import Mathlib.Analysis.Calculus.Deriv.Star
import Mathlib.Analysis.Analytic.Uniqueness
import Mathlib.Analysis.Normed.Module.Connected
```

When dropping the theorems into the in-tree `RiemannZeta.lean`, the `RiemannZeta` import is the file
itself, so the genuinely new dependencies to consider at the top of `RiemannZeta.lean` are
`Analysis.Calculus.Deriv.Star` (for `HasDerivAt.conj_conj`), `Analysis.Analytic.Uniqueness` (for the
identity principle), and `Analysis.Normed.Module.Connected` (for
`isConnected_compl_singleton_of_one_lt_rank`). `RiemannZeta.lean` already imports analyticity
machinery (`analyticOn_riemannZeta` is proved there), so some of these may already be transitively
available. Confirm via shake/import-minimization (section 4) and add only what shake reports as
missing.

---

## 4. Remaining manual steps for Owen (checklist)

This repository cannot open the PR. The following are manual GitHub steps. Do them in order.

- [ ] **Fork mathlib4.** Fork `leanprover-community/mathlib4`, clone, and create a feature branch,
      e.g. `git switch -c riemann-zeta-conj`.
- [ ] **Sign the Mathlib CLA** (first-time contributors; the CLA-assistant bot posts a sign link on
      the PR, and signing once covers all future PRs). If the digamma PR CLA was already signed, this
      is already done.
- [ ] **Rebase onto current master.** `RiemannZetaConj.lean` was built against v4.30.0; master may
      have drifted. Drop the two theorems (sections 3.1-3.2) into
      `Mathlib/NumberTheory/LSeries/RiemannZeta.lean` at top level, after `riemannZeta_one_sub` (its
      natural sibling). Ensure `open Complex ComplexConjugate` is in scope (RiemannZeta.lean already
      opens `Complex`; add `ComplexConjugate` if `conj` is not already in scope, or use
      `starRingEnd ℂ` to match the surrounding style). Add only the imports shake says are missing.
- [ ] **Build the touched file:** `lake build Mathlib.NumberTheory.LSeries.RiemannZeta`. Confirm the
      two `#print axioms` outputs are still `[propext, Classical.choice, Quot.sound]`, then DELETE
      any `#print axioms` lines before committing.
- [ ] **Run the style linter** (`lake exe lint-style`) and the environment linters CI runs; fix any
      line-length/docstring/naming reports. Each theorem already has a docstring.
- [ ] **Run shake / import minimization** (`lake exe shake --fix`) to minimize the three added
      imports to only those actually needed.
- [ ] **Commit and push to your fork** with a Conventional-Commits message matching the PR title.
- [ ] **Open the PR** targeting `leanprover-community/mathlib4:master`. Paste the title (section 1)
      and description (section 2). Wait for green CI.
- [ ] **Request review** on the Lean Zulip `#mathlib4` / PR-review stream; add `awaiting-review` if
      you have triage rights.
- [ ] **Respond to review.** Likely maintainer questions:
      - *The `s = 1` hypothesis.* The reflection holds on `ℂ ∖ {1}`. Whether it also holds at the
        pole `s = 1` (i.e. whether Mathlib's assigned value `riemannZeta 1` is real) is a separate
        question; if a maintainer wants the hypothesis dropped, it requires showing `riemannZeta 1`
        is real (or it may genuinely require `s ≠ 1`). Keep `s ≠ 1` unless asked.
      - *Naming.* `riemannZeta_conj` parallels `riemannZeta_one_sub`; the corollary name
        `riemannZeta_conj_eq_zero_iff` is descriptive. Defer to maintainer preference.
      - *`conj` vs `starRingEnd ℂ`* in the statement; match the surrounding file's convention.

---

## 5. What this proves / what remains

**Proves.** The two identities are mathematically and formally established: they compile sorry-free
against the real upstream `Complex.riemannZeta` on Lean/Mathlib v4.30.0, with `#print axioms` showing
only the foundational axioms `propext`, `Classical.choice`, `Quot.sound`. No `axiom`, no `sorry`, no
`native_decide`. They depend solely on existing Mathlib API and on no project code.

**Remains.** Purely procedural/manual: rebasing onto current master, the `s = 1` and naming
decisions (section 4), the CLA and fork, and review iteration. None is a mathematical gap; they are
the standard Mathlib submission workflow, which must be carried out by a human GitHub account.
