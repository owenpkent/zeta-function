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

**2026-09-01 update (branch `rational-root-floor` in the local mathlib4 checkout, master commit
`8acb872c31`, toolchain v4.34.0-rc2):** the port was rebased onto live master with two drift
adaptations, and the body below reflects the rebased state.

1. **The GaussLemma.lean addition was dropped.** Master has since generalized
   `Polynomial.IsPrimitive.dvd_of_fraction_map_dvd_fraction_map` to exactly the one-sided form our
   planned `IsPrimitive.dvd_of_fraction_map_dvd` provided (only the divisor needs to be primitive),
   so the planned lemma is redundant and the two proofs call the existing Mathlib lemma directly.
   The PR now touches two files, not three, and adds eight declarations, not nine.
2. **The extra `Nonempty (NormalizedGCDMonoid A)` hypothesis was dropped.** On current master
   `RingTheory/Localization/NumDen.lean` publicly imports
   `RingTheory/UniqueFactorizationDomain/GCDMonoid.lean`, whose priority-100 instance chain
   (`UniqueFactorizationMonoid A` to `IsGCDMonoid A` to `Nonempty (NormalizedGCDMonoid A)`) is
   therefore in scope in `RationalRoot.lean`. The two headline theorems need only the file's
   existing `UniqueFactorizationMonoid A` context, matching the original staged generality. This
   resolves (in our favor) the review topic pre-flagged below in earlier drafts.

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
theorem recovers it exactly (a guard `example` confirmed this against the branch). Two supporting
lemmas travel with them, placed in `Content.lean`, whose existing content they extend:

- `Polynomial.IsPrimitive.pow` and `Polynomial.isPrimitive_prod`: powers and finite
  products of primitive polynomials stay primitive.

**Proof route.** The reduced linear factor `C (den A r) * X - C (num A r)` is primitive (a constant
divisor of both coefficients divides the reduced numerator/denominator pair, hence is a unit) and,
over `K`, a unit multiple of `X - C r`. Its `rootMultiplicity`-power therefore divides `p.map
(algebraMap A K)` (`pow_rootMultiplicity_dvd`), and one-sided Gauss descent (the existing
`IsPrimitive.dvd_of_fraction_map_dvd_fraction_map`) brings the divisibility back down to `A`;
multiplicativity of the leading coefficient finishes. The multi-point case recombines the same
argument over a product of linear factors that are pairwise coprime over `K`
(`isCoprime_X_sub_C_of_isUnit_sub`, `Finset.prod_dvd_of_coprime`).

**A hypothesis note.** `Polynomial.IsPrimitive.pow` / `Polynomial.isPrimitive_prod` are stated
under `[NormalizedGCDMonoid R]`, matching the hypothesis level of their host section in
`Content.lean` (neither proof needs anything UFD-specific). The six `RationalRoot.lean`
declarations need only the file's existing `UniqueFactorizationMonoid A` context: where a
`NormalizedGCDMonoid A` instance is required to invoke the `Content.lean` lemmas, the proofs
materialize one locally via `let : NormalizedGCDMonoid A := Nonempty.some inferInstance` (the
`Nonempty` instance comes from `UniqueFactorizationMonoid A` through `IsGCDMonoid A`, in scope via
the file's existing `RingTheory.Localization.NumDen` import), the same idiom `GaussLemma.lean`
already uses. The statements are instance-independent.

All eight new declarations (two in `Content.lean`, six in `RationalRoot.lean`) build green and
`#print axioms` clean (`[propext, Classical.choice, Quot.sound]`; no `sorryAx`, no
`native_decide`) on master commit `8acb872c31` (toolchain v4.34.0-rc2), with `lake exe lint-style`
and the batteries env linter (`runLinter`) passing on both touched modules, and all direct
downstream importers rebuilt green. Three `public import`s are added to `RationalRoot.lean`
(`RingTheory.Polynomial.GaussLemma`, `Algebra.Polynomial.BigOperators`,
`RingTheory.Coprime.Lemmas`); each is used directly by the new proofs (`shake` no longer exists as
a lake executable on current master, so no automated minimization pass was run).

---

**AI use disclosure** (per Mathlib's contribution guidelines): this generalization was developed in
a personal research project with the help of an AI coding agent (Claude Code). The agent developed
the multiplicity generalization and its proof (building on the existing single-multiplicity
`den_dvd_of_is_root`), then ported it directly onto Mathlib's own source files: placing the two
primitivity lemmas in `Content.lean`'s existing `NormalizedGCDMonoid` section (a weaker hypothesis
than the UFD one the standalone draft used; neither proof needs anything UFD-specific), adapting
the imports to the module system, and rebasing onto current master. During the rebase the agent
found that Mathlib had independently generalized
`IsPrimitive.dvd_of_fraction_map_dvd_fraction_map` to the one-sided form an earlier draft of this
PR supplied as a new lemma, so that lemma was dropped and the proofs call the existing one. Build
green, `#print axioms` clean, and linters passing were confirmed directly against Mathlib's source
tree. The underlying result is a natural generalization of an existing Mathlib theorem, and every
proof step uses only existing Mathlib API. I have reviewed and understand the proofs, take
responsibility for the content, and will respond to review in my own words.

---

## 3. Theorem statements to add (verified signatures)

Full code for all declarations, with exact insertion points, is in
[`rational_root_floor_port.md`](rational_root_floor_port.md) section "The port, file by file"
(as-committed state on the `rational-root-floor` branch; the 2026-09-01 update above records the
two deltas against that document). Summary:

| Declaration | Target file | Role |
|---|---|---|
| `Polynomial.IsPrimitive.pow` | `Content.lean` | powers of a primitive polynomial are primitive |
| `Polynomial.isPrimitive_prod` | `Content.lean` | finite products of primitive polynomials are primitive |
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
- **Possible `private` on the four helper lemmas** (`isPrimitive_den_mul_X_sub_C_num` through
  `den_mul_X_sub_C_num_pow_rootMultiplicity_dvd`): kept public here, matching this file's existing
  precedent (`num_isRoot_scaleRoots_of_aeval_eq_zero` is public plumbing too), but a maintainer may
  see them as implementation detail.

---

## 4. Remaining manual steps for Owen

As of 2026-09-01 the branch is prepared locally: `rational-root-floor` in
`/home/owen/dev/mathlib4-pr`, committed on top of master commit `8acb872c31`, built, axiom-checked,
and linted. What remains: push the branch to the fork (`owenpkent/mathlib4`), open the PR with the
title/description above, request review, and reply to reviewers in your own words (Mathlib's AI
policy forbids LLM-written review replies, same constraint as P1/P2).

---

## 5. What this proves / what remains

**Proves.** The multiplicity generalization and its multi-point form are mathematically and
formally established: eight declarations, sorry-free, that compile against Mathlib's real
`RingTheory/Polynomial/{Content,RationalRoot}.lean` (not a standalone downstream copy), with
`#print axioms` showing only the foundational axioms `propext`, `Classical.choice`, `Quot.sound`.
No `axiom`, no `sorry`, no `native_decide`. Verified 2026-09-01 by committing the port on the
`rational-root-floor` branch of the local mathlib4 checkout at master commit `8acb872c31`,
building the touched modules and all their direct downstream importers, and passing `lake exe
lint-style` plus the batteries env linter on both touched modules.

**Remains.** Pushing the branch to the fork and the standard PR/review workflow, which must be
carried out by a human GitHub account. None of these is a mathematical gap.
