# Mathlib contribution staging: three digamma identities (reflection, iterated recurrence, duplication)

> Tier-1 move 1A from the needle-map ([`STATE_OF_THE_PROGRAM.md`](../../STATE_OF_THE_PROGRAM.md) Update 2026-06-04). Status: **half-preempted; the 3 surviving identities are now VERIFIED against the upstream `Complex.digamma`** in [`../ZetaRH/DigammaExtras.lean`](../ZetaRH/DigammaExtras.lean) (green on Lean/Mathlib v4.30.0 after the cache bump; `#print axioms` clean for all three). This note packages the contribution; `DigammaExtras.lean` is the PR-ready, build-checked unit.

## The finding (2026-06-04 re-check of current Mathlib master)

The needle-map flagged "upstream the digamma module to Mathlib" as the highest-value *bounded* move, with the explicit caveat: re-check against current master, since our pinned cache is Mathlib v4.13.0 (~1.5 years old) and preemption was likely. The re-check (GitHub code search + raw file read of master):

**Mathlib master already has `Mathlib/Analysis/SpecialFunctions/Gamma/Digamma.lean`** (namespace `Complex`), containing:

| Mathlib master declaration | Our `ExplicitFormula.lean` equivalent | Status |
|---|---|---|
| `digamma : ℂ → ℂ := logDeriv Gamma` | `digamma := logDeriv Complex.Gamma` | PREEMPTED (identical) |
| `digamma_def : digamma = logDeriv Gamma` | `digamma_eq` (pointwise, via `logDeriv_apply`) | PREEMPTED |
| `digamma_apply_add_one (s) (hs : ∀ m:ℕ, s ≠ -m) : digamma (s+1) = digamma s + s⁻¹` | `digamma_add_one` (`... + 1/s`, same hypothesis) | PREEMPTED |
| `digamma_one : digamma 1 = -eulerMascheroniConstant` | `digamma_one` | PREEMPTED |
| `digamma_one_half : digamma (1/2) = -2*log 2 - eulerMascheroniConstant` | `digamma_half` | PREEMPTED |
| `meromorphic_digamma` | (not in our file) | n/a |

So 3 of our 6 identities (def, recurrence, both special values, the `logDeriv` form) are already in Mathlib. **The three that are genuinely absent and remain a real contribution:** reflection, iterated recurrence, duplication. All three are proved sorry-free in our substrate.

## The three surviving identities (compile-ready statements, in `Complex` namespace)

Verified proofs to lift: [`lean/ZetaRH/ExplicitFormula.lean`](../ZetaRH/ExplicitFormula.lean), `digamma_add_nat` (lines ~144-155), `digamma_reflection` (lines ~162-237), `digamma_duplication` (lines ~249-323). They are kernel-checked against Mathlib v4.13.0 (`#print axioms` clean: `[propext, Classical.choice, Quot.sound]`).

```lean
/-- The iterated digamma recurrence `ψ(s+n) = ψ(s) + ∑_{k<n} 1/(s+k)`. -/
theorem digamma_apply_add_nat (s : ℂ) (hs : ∀ m : ℕ, s ≠ -m) (n : ℕ) :
    digamma (s + n) = digamma s + ∑ k ∈ Finset.range n, (s + k)⁻¹

/-- The digamma reflection formula `ψ(1-s) - ψ(s) = π cot(πs)`, for `s ∉ ℤ`. -/
theorem digamma_one_sub_sub (s : ℂ) (hs : ∀ m : ℤ, s ≠ m) :
    digamma (1 - s) - digamma s = π * (Complex.cos (π * s) / Complex.sin (π * s))
    -- if Mathlib has `Complex.cot`, prefer: = π * Complex.cot (π * s)

/-- The digamma duplication formula `ψ(2s) = ½(ψ(s) + ψ(s+½)) + log 2`. -/
theorem digamma_two_mul (s : ℂ) (hs : ∀ m : ℕ, s ≠ -m) (hsh : ∀ m : ℕ, s + 1/2 ≠ -m) :
    digamma (2 * s) = 2⁻¹ * (digamma s + digamma (s + 1/2)) + Complex.log 2
```

## Name-adaptation map (our substrate → Mathlib master) for lifting the proofs

- `digamma_eq s` (ours: `digamma s = deriv Gamma s / Gamma s`) becomes `logDeriv_apply Gamma s` after `rw [digamma_def]`, or use `digamma_def` and unfold; Mathlib's `digamma` is defeq to `logDeriv Gamma` (`digamma_def := rfl`).
- `digamma_add_one hs` (ours: `... = digamma s + 1/s`) becomes `digamma_apply_add_one s hs` (`... + s⁻¹`); bridge `1/s = s⁻¹` with `one_div` where the proof's `linear_combination`/`Finset.sum` steps expect `1/(s+k)` vs `(s+k)⁻¹`.
- Source lemmas the proofs need are all present in master: `Complex.Gamma_mul_Gamma_one_sub` (reflection), `Complex.Gamma_mul_Gamma_add_half` (Legendre duplication), `Complex.Gamma_add_one`, `Complex.differentiableAt_Gamma`, `Complex.Gamma_ne_zero`, `logDeriv_comp`, `logDeriv_mul`, `logDeriv_div`, `logDeriv_id'`.
- Master uses the Lean module system (`public import ...`); the target file's imports are `Mathlib.Analysis.Meromorphic.Complex`, `Mathlib.NumberTheory.Harmonic.GammaDeriv`, `Mathlib.Analysis.SpecialFunctions.Complex.LogDeriv`. The reflection/duplication proofs additionally need the `Gamma_mul_Gamma_*` lemmas (Gamma/Beta), so add `Mathlib.Analysis.SpecialFunctions.Gamma.Beta`.

## Verification status and the remaining step before PR

**Verified (2026-06-04, after the v4.30.0 cache bump):** the three theorems compile GREEN against the upstream `Complex.digamma` in [`../ZetaRH/DigammaExtras.lean`](../ZetaRH/DigammaExtras.lean), and `#print axioms` is `[propext, Classical.choice, Quot.sound]` for each (no `sorryAx`, no `ofReduceBool`). The proofs transferred essentially verbatim from `ExplicitFormula.lean`: the only adaptations were the recurrence name (`digamma_add_one` -> `digamma_apply_add_one`), `1/s` -> `s⁻¹`, and unfolding via `digamma_def` (since `Complex.digamma` is definitionally `logDeriv Gamma`, the predicted break points did not bite).

**Before opening the PR:** rebase the three theorems from `DigammaExtras.lean` onto the exact Mathlib commit being targeted (we built against the v4.30.0 tag, c5ea00351...; master may have drifted), drop them into `Mathlib/Analysis/SpecialFunctions/Gamma/Digamma.lean` (they already live in `namespace Complex`), and align names/docstrings to Mathlib conventions (e.g. a maintainer may prefer `Complex.cot` in the reflection statement, or a particular lemma name). Submitting the PR (fork, CLA, review) is a manual GitHub step for the maintainer; this repo cannot do it.
