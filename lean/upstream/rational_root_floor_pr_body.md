# Mathlib PR body: rational root theorem with multiplicity

This file is a ready-to-submit Mathlib PR body for the multiplicity generalization of the rational
root theorem, absent from current Mathlib master. The contribution is staged and kernel-verified in
[`../ZetaRH/RationalRootFloor.lean`](../ZetaRH/RationalRootFloor.lean) (Lean/Mathlib v4.30.0,
sorry-free, `#print axioms` clean, full UFD generality) and, this session, applied directly to
Mathlib's own `Content.lean` / `GaussLemma.lean` / `RationalRoot.lean` and rebuilt green in place
(see [`rational_root_floor_port.md`](rational_root_floor_port.md) for the exact diff, the build
log, and a note on two typeclass generalizations that fell out of fitting the port into Mathlib's
actual import graph). Copy the title and description below into the GitHub PR form after completing
the manual checklist in `rational_root_floor_port.md`. This repository cannot open the PR itself;
the fork, branch, and review steps are manual GitHub actions for Owen.

---

## 1. PR title

```
feat(RingTheory/Polynomial/RationalRoot): rational root theorem with multiplicity
```

---

## 2. PR description

This PR adds the rational root theorem with multiplicity to
`Mathlib/RingTheory/Polynomial/RationalRoot.lean`:

- `den_pow_rootMultiplicity_dvd_leadingCoeff`: if `r : K` is a root of `p : A[X]` (`A` a UFD, `K`
  its fraction field) with multiplicity `m = rootMultiplicity r (p.map (algebraMap A K))`, then
  `(den A r) ^ m ∣ p.leadingCoeff`;
- `prod_den_pow_rootMultiplicity_dvd_leadingCoeff`: the multi-point version, `∏ r ∈ s, (den A r) ^
  rootMultiplicity r ∣ p.leadingCoeff` over any finite set `s : Finset K` (the denominators need
  **not** be pairwise coprime in `A`; the recombination happens on the polynomial side, where the
  root factors at distinct points are pairwise coprime over `K`).

These generalize the existing multiplicity-one statement `den_dvd_of_is_root`: at `m = 1` the new
theorem recovers it exactly (a guard `example` in the staged unit confirms this). Three supporting
lemmas travel with them, placed in the files whose existing content they extend:

- `Polynomial.IsPrimitive.pow` and `Polynomial.isPrimitive_prod` (`Content.lean`): powers and finite
  products of primitive polynomials stay primitive;
- `Polynomial.IsPrimitive.dvd_of_fraction_map_dvd` (`GaussLemma.lean`): a one-sided Gauss descent --
  if a *primitive* `g` divides `f` over the fraction field, it divides `f` over the base ring. This
  relaxes the two-sided primitivity hypothesis of the existing
  `IsPrimitive.dvd_of_fraction_map_dvd_fraction_map` by routing `f` through its primitive part (the
  content becomes a unit in `K[X]`).

**Proof route.** The reduced linear factor `C (den A r) * X - C (num A r)` is primitive (a constant
divisor of both coefficients divides the reduced numerator/denominator pair, hence is a unit) and,
over `K`, a unit multiple of `X - C r`. Its `rootMultiplicity`-power therefore divides `p.map
(algebraMap A K)` (`pow_rootMultiplicity_dvd`), and one-sided Gauss descent brings the divisibility
back down to `A`; multiplicativity of the leading coefficient finishes. The multi-point case
recombines the same argument over a product of linear factors that are pairwise coprime over `K`
(`isCoprime_X_sub_C_of_isUnit_sub`, `Finset.prod_dvd_of_coprime`).

**A hypothesis note.** `Polynomial.IsPrimitive.pow` / `Polynomial.isPrimitive_prod` and
`Polynomial.IsPrimitive.dvd_of_fraction_map_dvd` are stated one notch more generally than a first
draft (built as a standalone unit) used: `[NormalizedGCDMonoid R]` / `[Nonempty
(NormalizedGCDMonoid R)]` rather than `[UniqueFactorizationMonoid R]`, matching the hypothesis level
their host sections in `Content.lean` / `GaussLemma.lean` already use, and strictly more general
(neither proof needs anything UFD-specific). `RationalRoot.lean`'s own two new theorems keep
`UniqueFactorizationMonoid A` (needed for `num_den_reduced`) and separately pick up `Nonempty
(NormalizedGCDMonoid A)`, narrowly scoped to just those two declarations.

All nine new declarations (5 newly-public, 4 `RationalRoot.lean`-local supporting lemmas) build
green and `#print axioms` clean (`[propext, Classical.choice, Quot.sound]`; no `sorryAx`, no
`native_decide`) applied directly to Mathlib's own source tree at commit `c5ea00351c` (tag
`v4.30.0`), not merely as a downstream import. Three `public import`s are added to
`RationalRoot.lean` (`RingTheory.Polynomial.GaussLemma`, `Algebra.Polynomial.BigOperators`,
`RingTheory.Coprime.Lemmas`), confirmed sufficient by the green build; import minimization via
`shake` is still open (see checklist).

---

**AI use disclosure** (per Mathlib's contribution guidelines): this generalization was developed in
a personal research project with the help of an AI coding agent (Claude Code). The agent developed
the multiplicity generalization and its proof (building on the existing single-multiplicity
`den_dvd_of_is_root`), then ported it directly onto Mathlib's own source files: relocating three of
the five newly-public lemmas into `Content.lean`'s and `GaussLemma.lean`'s existing sections
(generalizing two of them from `UniqueFactorizationMonoid` to the weaker `NormalizedGCDMonoid`
hypothesis already in scope there, after a real build failure showed the UFD-derived instance isn't
reachable from those files without an import cycle), adapting the imports to the new module system,
and confirming the build is green with `#print axioms` clean directly against Mathlib's source tree
(then reverting the working copy). The underlying result is a natural generalization of an existing
Mathlib theorem, and every proof step uses only existing Mathlib API. I have reviewed and understand
the proofs, take responsibility for the content, and will respond to review in my own words.

---

## 3. Theorem statements to add (verified signatures)

Full code for all nine declarations, with exact insertion points, is in
[`rational_root_floor_port.md`](rational_root_floor_port.md) section "The port, file by file". Summary:

| Declaration | Target file | Role |
|---|---|---|
| `Polynomial.IsPrimitive.pow` | `Content.lean` | powers of a primitive polynomial are primitive |
| `Polynomial.isPrimitive_prod` | `Content.lean` | finite products of primitive polynomials are primitive |
| `Polynomial.IsPrimitive.dvd_of_fraction_map_dvd` | `GaussLemma.lean` | one-sided Gauss descent |
| `isPrimitive_den_mul_X_sub_C_num` | `RationalRoot.lean` | the reduced linear factor of `r` is primitive |
| `map_den_mul_X_sub_C_num` | `RationalRoot.lean` | over `K`, that factor is a unit multiple of `X - C r` |
| `leadingCoeff_den_mul_X_sub_C_num` | `RationalRoot.lean` | its leading coefficient is `den A r` |
| `den_mul_X_sub_C_num_pow_rootMultiplicity_dvd` | `RationalRoot.lean` | the `rootMultiplicity`-power of that factor divides `p` |
| `den_pow_rootMultiplicity_dvd_leadingCoeff` | `RationalRoot.lean` | **headline**: single-point multiplicity floor |
| `prod_den_pow_rootMultiplicity_dvd_leadingCoeff` | `RationalRoot.lean` | **headline**: multi-point product form |

### Naming topics likely to come up in review

- **`RationalRoot.lean` placement is unqualified (top-level), not `Polynomial.`-namespaced.** This
  matches the file's own pre-existing convention (`num_dvd_of_is_root`, `den_dvd_of_is_root` are
  themselves top-level, not inside `namespace Polynomial`), and was confirmed to build correctly
  this way. A maintainer could ask for `Polynomial.`-namespacing instead; the proofs are unaffected
  either way.
- **The extra `Nonempty (NormalizedGCDMonoid A)` hypothesis** on the two headline theorems (see "A
  hypothesis note" above) is always true for a UFD, but this file's own import position can't prove
  that internally without risking a cycle. A maintainer may prefer to drop it if `RationalRoot.lean`
  already (or comes to) transitively import
  `Mathlib/RingTheory/UniqueFactorizationDomain/GCDMonoid.lean`; worth confirming against the actual
  master import graph at review time rather than guessing further here.
- **Possible `private` on the four helper lemmas** (`isPrimitive_den_mul_X_sub_C_num` through
  `den_mul_X_sub_C_num_pow_rootMultiplicity_dvd`): kept public here, matching this file's existing
  precedent (`num_isRoot_scaleRoots_of_aeval_eq_zero` is public plumbing too), but a maintainer may
  see them as implementation detail.

---

## 4. Remaining manual steps for Owen

Full checklist with detail: [`rational_root_floor_port.md`](rational_root_floor_port.md), section
"Checklist: what remains". Short version: clone/use the existing fork (`owenpkent/mathlib4`),
branch off master, apply the three-file diff (mechanical -- drift-checked against live master this
session), rebuild + lint on that live checkout, commit, push, open the PR with the title/description
above, request review, and reply to reviewers in your own words (Mathlib's AI policy forbids
LLM-written review replies, same constraint as P1/P2).

---

## 5. What this proves / what remains

**Proves.** The multiplicity generalization and its multi-point form are mathematically and
formally established: nine declarations, sorry-free, that compile against Mathlib's real
`RingTheory/Polynomial/{Content,GaussLemma,RationalRoot}.lean` (not a standalone downstream copy),
with `#print axioms` showing only the foundational axioms `propext`, `Classical.choice`,
`Quot.sound`. No `axiom`, no `sorry`, no `native_decide`. Verified this session by actually applying
the port to this project's pinned Mathlib checkout and building it in place (then reverting), not
merely by inspection.

**Remains.** Rebuilding on a live fork checkout of current master (the drift check found only one,
unrelated line of difference in the touched files, so this is expected to be mechanical), the
style-linter and `shake` import-minimization pass, and the standard fork/branch/PR/review workflow,
which must be carried out by a human GitHub account. None of these is a mathematical gap.
