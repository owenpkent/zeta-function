# Upstream to Mathlib: submission guide

This directory stages results from the project that are **absent from Mathlib** and ready to
contribute upstream. Each is kernel-verified (sorry-free, `#print axioms` clean) against
**Lean/Mathlib v4.30.0** (toolchain `leanprover/lean4:v4.30.0`), and each has a ready-to-submit PR
body. This README is the single entry point: do the one-time setup once, then submit each PR.

Everything machine-checkable is done. What remains for every PR is the standard Mathlib GitHub
workflow, which must be carried out by a human account (this repository cannot open PRs).

## The staged contributions

| PR | Verified unit | PR body | Target Mathlib file |
|----|---------------|---------|---------------------|
| digamma: reflection, iterated recurrence, duplication | [`../ZetaRH/DigammaExtras.lean`](../ZetaRH/DigammaExtras.lean) | [`digamma_pr_body.md`](digamma_pr_body.md) | `Mathlib/Analysis/SpecialFunctions/Gamma/Digamma.lean` |
| `riemannZeta_conj`: conjugation symmetry of ζ | [`../ZetaRH/RiemannZetaConj.lean`](../ZetaRH/RiemannZetaConj.lean) | [`riemann_zeta_conj_pr_body.md`](riemann_zeta_conj_pr_body.md) | `Mathlib/NumberTheory/LSeries/RiemannZeta.lean` |

The two are **independent** (different target files, no shared new lemmas), so they are two separate
PRs and can go in either order. Suggested order: **digamma first** (it has been staged longest and
its only open question is now resolved), then `riemannZeta_conj`.

Background notes: [`digamma_contribution.md`](digamma_contribution.md) (digamma context).

## One-time setup (do once, covers all PRs)

- [ ] **Fork `leanprover-community/mathlib4`** on GitHub and clone your fork locally.
- [ ] **Sign the Mathlib CLA.** First-time contributors sign once; it covers all future PRs. The
      CLA-assistant bot posts a sign link on your first PR, or pre-sign via the CLA-assistant page.
- [ ] **Get a buildable mathlib4 checkout.** `lake exe cache get` after cloning, so you do not
      rebuild all of Mathlib from source.

## Per-PR workflow (repeat for each)

1. **Branch** off the latest `master`, e.g. `git switch -c digamma-...` / `git switch -c riemann-zeta-conj`.
2. **Drop the verified theorems** from the unit into the target file (table above), at the placement
   the PR body specifies. The proof bodies transfer verbatim from v4.30.0; only re-check against your
   rebase commit if master has drifted.
3. **Add only the imports shake reports as missing** (each PR body lists the candidate new imports).
4. **Build just the touched file** (`lake build Mathlib.<...>`), confirm `#print axioms` is still
   `[propext, Classical.choice, Quot.sound]`, then **delete the `#print axioms` lines** (diagnostic
   only, not wanted in the library).
5. **Lint + shake:** `lake exe lint-style` and `lake exe shake --fix`; fix line-length/docstring/
   naming reports and minimize imports.
6. **Commit** with a Conventional-Commits message matching the PR title; push to your fork.
7. **Open the PR** against `leanprover-community/mathlib4:master`; paste the title + description from
   the PR body. Wait for green CI.
8. **Request review** on the Lean Zulip `#mathlib4` / PR-review stream; add `awaiting-review` if you
   have triage rights.
9. **Respond to review** (naming, golfing, hypothesis phrasing); push fixups to the same branch.

## Per-PR specifics (already resolved, so you do not have to decide during submission)

- **digamma:** the reflection RHS-form question is settled. `Complex.cot` exists in v4.30.0
  (`Complex.cot_eq_cos_div_sin`), so use the RHS `↑π * Complex.cot (↑π * s)` and add
  `rw [Complex.cot_eq_cos_div_sin]` as the first proof step (details in `digamma_pr_body.md` §3.2).
  Likely review topic: lemma naming (`digamma_reflection` etc.).
- **`riemannZeta_conj`:** the only likely review topic is whether to drop the `s ≠ 1` hypothesis
  (it holds on `ℂ ∖ {1}`; the pole value question is separate). Keep `s ≠ 1` unless asked. Details
  in `riemann_zeta_conj_pr_body.md` §4.

## Not staged (and why)

- **The rank-2 symplectic determinant law** (`ZetaRH/TateModule.lean`, `det_transform`): Mathlib
  already has the general version (`Basis.det` / `LinearMap.det` / `AlternatingMap`), so the rank-2
  bilinear case is an application, not a gap. Do not submit.
