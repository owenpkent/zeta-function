# Mathlib PR body: `Real.arcosh`

## STATUS: DO NOT SUBMIT -- DUPLICATE FOUND, already merged upstream

**Before writing anything below, verify this is still true**, since it changes the
disposition of this whole package: check whether
`Mathlib/Analysis/SpecialFunctions/Arcosh.lean` still exists on current master
(`grep -rl "def arcosh" path/to/mathlib4/Mathlib/Analysis/SpecialFunctions/`).

This PR was drafted (statement + a from-scratch proof set, staged in
[`Arcosh.lean`](./Arcosh.lean)) before checking the pinned Mathlib checkout this project
actually builds against. That check, run this session, found:

- `Mathlib/Analysis/SpecialFunctions/Arcosh.lean` **already exists** in the pinned
  checkout (`lean/.lake/packages/mathlib`, commit `c5ea00351c`, tag `v4.30.0`, dated
  2026-05-26).
- Its `git log` shows the file was added at commit `b27e7964c1` on **2026-03-23** --
  authored by **Yuval Filmus**, i.e. it landed in Mathlib roughly two months before this
  project's own pin, not after.
- Its contents (`Real.arcosh`, `Real.cosh_arcosh`, `Real.arcosh_cosh`, `Real.arcosh_zero`
  [`arcosh 1 = 0`, playing the role a PR here would call `arcosh_one`],
  `Real.arcosh_nonneg`, `Real.arcosh_pos`, `Real.strictMonoOn_arcosh`,
  `Real.arcosh_le_arcosh`, `Real.arcosh_lt_arcosh`, `Real.continuousOn_arcosh`,
  `Real.hasStrictDerivAt_arcosh` / `Real.hasDerivAt_arcosh`,
  `Real.differentiableAt_arcosh` / `Real.differentiableOn_arcosh`,
  `Real.contDiffAt_arcosh` / `Real.contDiffOn_arcosh`, `Real.analyticAt_arcosh` and
  friends, plus `Real.coshPartialEquiv` and `Real.coshOpenPartialHomeomorph` bundling)
  is a **superset** of every lemma this draft was going to propose, including the exact
  lemma set requested by analogy with `Real.arsinh` (`cosh_arcosh`, `arcosh_cosh`,
  monotonicity, continuity, differentiability) plus the `PartialEquiv` bundling and
  analyticity that this draft only got as far as TODO-marking (see §3.3).

**The recorded gap claim this PR was meant to close** -- in
[`../ZetaRH/VerifierQueue.lean`](../ZetaRH/VerifierQueue.lean) line 136
("Mathlib has `Real.arsinh` but (as of the v4.30.0 pin) no `Real.arcosh`") and
[`experiments/lemma_db/verifier_queue.md`](../../experiments/lemma_db/verifier_queue.md)
§3/§5 ("Two small upstream candidates fell out of the triage: `Real.arcosh` (absent;
...)") -- **was false at the time it was recorded**, or at least false by the v4.30.0
pin date. `Real.arcosh` was already in Mathlib master before v4.30.0 was tagged. This is
a project bookkeeping error, not a Mathlib gap. Both source locations should have their
"absent" language corrected the next time either file is touched (not done as part of
this staging pass, since this task was staging only).

**What to actually do with this package:** nothing upstream. Optionally, swap the
project's own `arcoshReal` (`VerifierQueue.lean`) for Mathlib's `Real.arcosh` directly
the next time that file is built and wired in -- it is a strictly larger, already-merged
API doing the identical job (same closed form, same core lemma), which would delete the
project's local definition rather than add one. That is a housekeeping item, not a PR.

The rest of this document is kept in the original submit-ready format, as a record of
the independent derivation and for the (now moot) case that the upstream file is ever
reverted or the naming changes.

---

## 1. PR title (not to be filed)

```
feat(Analysis/SpecialFunctions): add Real.arcosh
```

## 2. PR description (not to be filed)

This would have added the inverse hyperbolic cosine to Mathlib, as the natural sibling
of `Real.arsinh` (`Mathlib/Analysis/SpecialFunctions/Arsinh.lean`):

- `Real.arcosh (x : ℝ) : ℝ := Real.log (x + Real.sqrt (x ^ 2 - 1))`, the standard closed
  form (the same one `Real.arsinh x = log (x + sqrt (1 + x^2))` uses, adapted to the
  domain shift);
- `Real.cosh_arcosh`: for `1 ≤ x`, `cosh (arcosh x) = x`;
- `Real.arcosh_cosh`: for `0 ≤ x`, `arcosh (cosh x) = x`;
- `Real.arcosh_one`, `Real.arcosh_nonneg`, `Real.arcosh_pos`;
- `Real.strictMonoOn_arcosh`, `Real.arcosh_le_arcosh`, `Real.arcosh_lt_arcosh`
  (monotonicity on `[1, ∞)`, matching `arsinh_le_arsinh` / `arsinh_lt_arsinh`);
- `Real.continuousOn_arcosh` (continuity on `[1, ∞)`);
- `Real.hasDerivAt_arcosh`, `Real.differentiableAt_arcosh`, `Real.differentiableOn_arcosh`
  (differentiability on `(1, ∞)`, with the explicit derivative
  `(sqrt (x^2-1))⁻¹`).

Motivation (as originally drafted): `arcoshReal` in this project's
[`VerifierQueue.lean`](../ZetaRH/VerifierQueue.lean) is used to give the closed form of
`bandGreen` (the Green's function of a two-sided real band complement,
`G = arcosh((T²+g²)/(T²-g²)) / 2`), which feeds Theorem V2's Christoffel germ-length
bound (`v2_germ_bound`, #VQ-2, LEARNINGS #172/#202). Any Mathlib user working with
hyperbolic-band potential theory, Chebyshev/Zolotarev estimates off `[-1,1]`, or the
inverse-cosh side of Lorentzian/hyperbolic-geometry material would want the same
primitive Mathlib already gives for `arsinh`. (This motivation is now satisfied by the
existing `Real.arcosh` file; recorded here only for completeness.)

---

## 3. Theorem statements (verified against the pinned toolchain, but NOT novel -- see STATUS)

### 3.1 Proved in this draft (verbatim in [`Arcosh.lean`](./Arcosh.lean))

Every declaration below elaborates and type-checks against Lean/Mathlib v4.30.0
(`lake env lean Arcosh.lean` on this project's pinned toolchain, run this session, zero
errors, one harmless unused-variable warning). None uses `sorry`.

| Declaration | Role | Matches (already-merged) Mathlib name |
|---|---|---|
| `arcosh` | definition, `log (x + sqrt(x²-1))` | `Real.arcosh` |
| `cosh_arcosh` | `1 ≤ x → cosh(arcosh x) = x` (ported from the repo's `cosh_arcoshReal`) | `Real.cosh_arcosh` |
| `arcosh_one` | `arcosh 1 = 0` | `Real.arcosh_zero` (named for the output, not the input) |
| `arcosh_nonneg` | `1 ≤ x → 0 ≤ arcosh x` | `Real.arcosh_nonneg` |
| `arcosh_pos` | `1 < x → 0 < arcosh x` | `Real.arcosh_pos` |
| `arcosh_cosh` | `0 ≤ x → arcosh(cosh x) = x` | `Real.arcosh_cosh` |
| `strictMonoOn_arcosh` | `StrictMonoOn arcosh (Ici 1)` | `Real.strictMonoOn_arcosh` (stated on `Ioi 0`, junk-value-robust; this draft's `Ici 1` is the same content on the domain that matters) |
| `arcosh_le_arcosh` | `1 ≤ x → 1 ≤ y → (arcosh x ≤ arcosh y ↔ x ≤ y)` | `Real.arcosh_le_arcosh` |
| `arcosh_lt_arcosh` | strict form | `Real.arcosh_lt_arcosh` |
| `continuousOn_arcosh` | `ContinuousOn arcosh (Ici 1)` | `Real.continuousOn_arcosh` |
| `hasDerivAt_arcosh` | `1 < x → HasDerivAt arcosh (sqrt(x²-1))⁻¹ x` | `Real.hasDerivAt_arcosh` (derived there from `hasStrictDerivAt_arcosh`) |
| `differentiableAt_arcosh` | corollary | `Real.differentiableAt_arcosh` |
| `differentiableOn_arcosh` | corollary | `Real.differentiableOn_arcosh` |

Proof routes (all elementary, no new machinery beyond what `Arsinh.lean` itself uses):
`cosh_arcosh` unfolds `cosh_eq`/`exp_log`/an explicit inverse identity (the repo's
original argument, unchanged); `arcosh_cosh` uses `cosh_sq`/`sinh_sq` to identify
`sqrt(cosh x ² - 1) = sinh x` then collapses `cosh x + sinh x` to `exp x` via the
`cosh_eq`/`sinh_eq` sum/difference-of-exponentials forms; monotonicity and continuity are
direct from `Real.log_lt_log` / `Real.sqrt_le_sqrt` / `ContinuousOn.log`; the derivative
is the chain rule through `HasDerivAt.sqrt` and `HasDerivAt.log` with a `field_simp; ring`
cleanup.

### 3.2 Requested but not attempted (TODO-marked in `Arcosh.lean`, not `sorry`-marked)

Two further items a complete port would want, matching what Mathlib's actual file
carries (`ContDiffOn`/`AnalyticAt`, and the `PartialEquiv`/`OpenPartialHomeomorph`
bundling `Real.coshPartialEquiv` / `Real.coshOpenPartialHomeomorph`): stated as TODO
comments with a route sketch, not as live declarations. These were not proved because,
once the duplicate was confirmed, further proof effort had no submission target; the
route sketches are left in place in case this draft is ever repurposed.

### 3.3 Imports

`Arcosh.lean` builds against:

```lean
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Deriv
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.SpecialFunctions.Trigonometric.DerivHyp
```

matching (a subset of) the actual merged file's own imports (`Log.Basic` and
`Trigonometric.DerivHyp`; the derivative lemmas pulled in `Log.Deriv` and `Sqrt`
specifically for `hasDerivAt_arcosh`).

---

## 4. Placement (as originally scoped)

`Mathlib/Analysis/SpecialFunctions/Arcosh.lean`, as the sibling of
`Mathlib/Analysis/SpecialFunctions/Arsinh.lean` -- correctly anticipated; this is exactly
where the already-merged file lives.

---

## 5. Dependency / sequencing notes

This package has no dependency on the digamma (mathlib4#41132) or `riemannZeta_conj`
(mathlib4#41133) PRs, and would have had no sequencing constraint against them. It is
independently moot regardless.

---

## 6. What this proves / what remains

**Proves.** The independent derivation is real: twelve declarations (the definition plus
eleven lemmas), proved sorry-free against the exact pinned toolchain this project builds
against, reconstructing (with different lemma names in a few spots, e.g. `arcosh_one` vs.
Mathlib's `arcosh_zero`) essentially the full lemma set Mathlib's own file provides for
the requested scope (cosh/arcosh inverse pair, monotonicity, continuity,
differentiability).

**Remains.** Nothing to submit. If `VerifierQueue.lean` or `verifier_queue.md` are
touched again, correct the "absent" claim there and consider swapping the project's
local `arcoshReal` for Mathlib's `Real.arcosh` directly (a deletion, not an addition).
