# Mathlib port: rational root theorem with multiplicity

Ready-to-apply port of the P10 FORMAL-axis deliverable
([`../ZetaRH/RationalRootFloor.lean`](../ZetaRH/RationalRootFloor.lean), #RR-1/#RR-2, sorry-free,
axiom-clean, full UFD generality) into Mathlib's own `RingTheory/Polynomial/{Content,GaussLemma,
RationalRoot}.lean`. This file carries the exact code to drop in, file by file, plus what was
learned getting it to build. [`rational_root_floor_pr_body.md`](rational_root_floor_pr_body.md)
carries the PR title, description, and AI-use disclosure to paste into GitHub.

## Drift check (2026-07-17, against live master)

Fetched the current master copy of all three target files from `raw.githubusercontent.com` and
diffed against this project's pinned Lean/Mathlib `v4.30.0` checkout
(`lean/.lake/packages/mathlib`, commit `c5ea00351c`, tag `v4.30.0`, the same commit the P1/P2 PRs
were built against):

- **`RationalRoot.lean`: one line of drift, unrelated to this port.** `num_dvd_of_is_root`'s proof
  reads `have inst := Classical.propDecidable` in the pinned copy vs `haveI inst :=
  Classical.propDecidable` on master. This is an instance-search style tweak somewhere in the
  file's history since 2026-05-26; it does not touch `den_dvd_of_is_root`, `num_dvd_of_is_root`, or
  any declaration this port calls or extends. Both are byte-for-byte identical otherwise, same
  typeclass context (`UniqueFactorizationMonoid A`, `IsFractionRing A K`). **No
  `rootMultiplicity`-adjacent declaration has appeared in the file on master.**
- **`GaussLemma.lean` / `Content.lean`: textually drifted elsewhere, but every declaration this
  port depends on is present under the same name and signature**: `IsPrimitive`, `isPrimitive_one`,
  `IsPrimitive.mul`, `content_eq_zero_iff`, `eq_C_content_mul_primPart`, `isPrimitive_primPart`,
  `primPart_dvd`, `IsPrimitive.dvd_of_fraction_map_dvd_fraction_map`, and the
  `section NormalizedGCDMonoid` / `[Nonempty (NormalizedGCDMonoid R)]` hypothesis pattern both files
  already use (see "Typeclass note" below).
- `gh api search/issues` for `RationalRoot rootMultiplicity is:pr` against
  `leanprover-community/mathlib4`: zero hits. Re-confirms the 2026-07-02 prior-art CLEAR-TO-PR
  verdict; no competing PR has appeared in the intervening two weeks.

**Verdict: safe to port onto current master as-is.** The rebase in the checklist below is
mechanical, not a re-derivation.

## Build verification (2026-07-17, this session)

Elan/lake/lean and the `gh` CLI (authenticated, `owenpkent`, `repo`+`workflow` scopes) are all
available on this machine, and the fork `owenpkent/mathlib4` already exists on GitHub (used for
P1/P2). No separate writable mathlib4 clone was present, but this project's own pinned dependency
checkout (`lean/.lake/packages/mathlib`, a full, unshallowed clone of
`leanprover-community/mathlib4`, detached at the `v4.30.0` tag with a warm olean cache) is one. To
get a real build signal without disturbing that shared checkout:

1. Created a disposable branch at the existing pinned commit (`git checkout -b
   rr-floor-port-buildtest`) -- zero-cost, no working-tree change.
2. Applied the port below directly to `Content.lean`, `GaussLemma.lean`, `RationalRoot.lean`.
3. Ran `lake build Mathlib.RingTheory.Polynomial.RationalRoot`.
4. Iterated on one real build failure (see "Typeclass note" below) until clean.
5. Confirmed axiom-cleanliness with temporary `#print axioms` lines, then deleted them.
6. **Reverted everything**: `git checkout --` the three files, `git checkout` back to the pristine
   detached `v4.30.0` HEAD, `git branch -D` the disposable branch. Final `git status --short` in
   that checkout is empty -- it is exactly as it was found. Nothing was pushed anywhere.

Result:

- **Build green**, zero errors, zero warnings after the fix below: `Build completed successfully
  (1860 jobs)`.
- **Axiom-clean**: `#print axioms` on all 5 newly-public declarations
  (`Polynomial.IsPrimitive.pow`, `Polynomial.isPrimitive_prod`,
  `Polynomial.IsPrimitive.dvd_of_fraction_map_dvd`, `den_pow_rootMultiplicity_dvd_leadingCoeff`,
  `prod_den_pow_rootMultiplicity_dvd_leadingCoeff`) reports exactly `[propext, Classical.choice,
  Quot.sound]` -- no `sorryAx`, no `native_decide`.

This is a build against the pinned `v4.30.0` commit, not a live-master fork checkout (see the
checklist for what that last step still needs). Given the drift check above, that gap is believed
to be purely mechanical.

## Typeclass note (why this differs slightly from `RationalRootFloor.lean`)

[`RationalRootFloor.lean`](../ZetaRH/RationalRootFloor.lean) states everything under one hypothesis,
`[UniqueFactorizationMonoid A]`, deriving `NormalizedGCDMonoid A` internally via `letI :
NormalizedGCDMonoid A := Nonempty.some inferInstance`. That works there because the project's Lean
environment imports a wide enough slice of Mathlib for the relevant automatic instance
(`Mathlib/RingTheory/UniqueFactorizationDomain/GCDMonoid.lean:74`, `instance (α)
[CommMonoidWithZero α] [UniqueFactorizationMonoid α] : Nonempty (NormalizedGCDMonoid α)`) to be
reachable.

Mathlib's own `Content.lean` and `GaussLemma.lean` sit lower in the import DAG and do **not** reach
that instance. This was not a guess: the first build attempt, with the two `Content.lean` helper
lemmas stated under a freshly-derived `[UniqueFactorizationMonoid R]` exactly as in
`RationalRootFloor.lean`, failed with

```
error: Mathlib/RingTheory/Polynomial/Content.lean:471:48: failed to synthesize instance of type class
  Nonempty (NormalizedGCDMonoid R)
```

Both target files already have an established workaround for exactly this situation: thread
`[NormalizedGCDMonoid R]` (`Content.lean`'s own `section NormalizedGCDMonoid`) or `[Nonempty
(NormalizedGCDMonoid R)]` (`GaussLemma.lean`'s own nested `section NormalizedGCDMonoid`) as an
explicit section hypothesis, rather than deriving it from UFD-ness. This port follows suit instead
of fighting the import graph:

- `IsPrimitive.pow` / `isPrimitive_prod` land inside `Content.lean`'s existing `section
  NormalizedGCDMonoid` (already has `[NormalizedGCDMonoid R]` in scope). This is **more general**
  than the UFD-only form in `RationalRootFloor.lean`, not just a workaround: they now hold for any
  `NormalizedGCDMonoid`, not only UFDs, and neither proof needed anything UFD-specific in the first
  place (only `isPrimitive_one` and `IsPrimitive.mul`, both already `NormalizedGCDMonoid`-level
  facts).
- `IsPrimitive.dvd_of_fraction_map_dvd` lands inside `GaussLemma.lean`'s existing `section
  NormalizedGCDMonoid` (nested in `section FractionMap`, which already has `[Nonempty
  (NormalizedGCDMonoid R)]` and the fraction field `K` in scope). Same generalization, same
  reasoning.
- `RationalRoot.lean`'s own two headline theorems still need `UniqueFactorizationMonoid A` (for
  `num_den_reduced`, a genuinely UFD-specific fact about reduced numerator/denominator pairs), so
  they keep that hypothesis from the file's existing `section RationalRootTheorem`, and separately
  pick up `[Nonempty (NormalizedGCDMonoid A)]` -- scoped to a narrow inner `section ... end` around
  just the two declarations that call the relocated helpers, so it does not leak into
  `isPrimitive_den_mul_X_sub_C_num` / `map_den_mul_X_sub_C_num` / `leadingCoeff_den_mul_X_sub_C_num`
  (which don't need it) or the pre-existing `namespace UniqueFactorizationMonoid` block that follows
  (confirmed by re-running the build: without this scoping, the `linter.unusedSectionVars` linter
  flagged all three of those plus the pre-existing `UniqueFactorizationMonoid.integer_of_integral`).

Net effect: 3 of the 9 new declarations end up strictly more general than
`RationalRootFloor.lean`'s originals (`UniqueFactorizationMonoid` weakened to plain
`NormalizedGCDMonoid`), and the two headline theorems gain one extra, always-true-for-a-UFD
hypothesis (`Nonempty (NormalizedGCDMonoid A)`) that a maintainer may ask to drop if
`RationalRoot.lean` picks up a heavier transitive import in the future. Flagged as a likely review
topic in [`rational_root_floor_pr_body.md`](rational_root_floor_pr_body.md).

A second, separate naming question was resolved empirically rather than by convention alone: the
`RationalRootFloor.lean` docstrings had suggested `Polynomial.`-prefixed "intended Mathlib names"
for the `RationalRoot.lean`-target declarations too, but `RationalRoot.lean`'s own pre-existing
content (`num_dvd_of_is_root`, `den_dvd_of_is_root`) is top-level and unqualified, not inside
`namespace Polynomial`. The port matches the file it actually lands in: all six `RationalRoot.lean`
additions are top-level/unqualified, exactly like their neighbors.

## The port, file by file

### 1. `Mathlib/RingTheory/Polynomial/Content.lean`

Insert right before the file's final `end Polynomial` (i.e. still inside the existing `section
NormalizedGCDMonoid`, immediately after `degree_gcd_le_right`):

```lean
/-- Powers of a primitive polynomial are primitive. -/
theorem IsPrimitive.pow {q : R[X]} (hq : q.IsPrimitive) (n : ℕ) :
    (q ^ n).IsPrimitive := by
  induction n with
  | zero => rw [pow_zero]; exact isPrimitive_one
  | succ k ih => rw [pow_succ]; exact ih.mul hq

/-- Finite products of primitive polynomials are primitive. -/
theorem isPrimitive_prod {ι : Type*} (t : Finset ι) (f : ι → R[X])
    (h : ∀ i ∈ t, (f i).IsPrimitive) : (∏ i ∈ t, f i).IsPrimitive :=
  Finset.prod_induction f IsPrimitive (fun _ _ ha hb => ha.mul hb) isPrimitive_one h
```

No new imports needed (`Finset.prod_induction` is already reachable; confirmed by the green build).
Full names after insertion: `Polynomial.IsPrimitive.pow`, `Polynomial.isPrimitive_prod`.

### 2. `Mathlib/RingTheory/Polynomial/GaussLemma.lean`

Insert inside the existing `section NormalizedGCDMonoid` (nested in `section FractionMap`), right
after the proof ending `simp [s0, mem_nonZeroDivisors_iff_ne_zero]` and before the following
`variable (K)`:

```lean
/-- **One-sided Gauss descent.** If a primitive `g : R[X]` divides `f` over the fraction
field, it divides `f` over `R`. This relaxes the two-sided primitivity hypothesis of
`IsPrimitive.dvd_of_fraction_map_dvd_fraction_map` by routing `f` through its primitive
part (the content becomes a unit in `K[X]`). -/
theorem IsPrimitive.dvd_of_fraction_map_dvd {g f : R[X]} (hg : g.IsPrimitive)
    (h : g.map (algebraMap R K) ∣ f.map (algebraMap R K)) : g ∣ f := by
  letI : NormalizedGCDMonoid R := Nonempty.some inferInstance
  rcases eq_or_ne f 0 with rfl | hf
  · exact dvd_zero g
  · have hcont0 : f.content ≠ 0 := fun h0 => hf (content_eq_zero_iff.mp h0)
    have hcont : algebraMap R K f.content ≠ 0 := fun h0 =>
      hcont0 (IsFractionRing.injective R K (h0.trans (map_zero (algebraMap R K)).symm))
    have hmap : f.map (algebraMap R K)
        = C (algebraMap R K f.content) * f.primPart.map (algebraMap R K) := by
      conv_lhs => rw [f.eq_C_content_mul_primPart]
      rw [Polynomial.map_mul, map_C]
    have hunit : IsUnit (C (algebraMap R K f.content)) :=
      isUnit_C.mpr (isUnit_iff_ne_zero.mpr hcont)
    have h' : g.map (algebraMap R K) ∣ f.primPart.map (algebraMap R K) := by
      rwa [hmap, hunit.dvd_mul_left] at h
    exact (hg.dvd_of_fraction_map_dvd_fraction_map f.isPrimitive_primPart h').trans
      f.primPart_dvd
```

No new imports needed. Full name after insertion: `Polynomial.IsPrimitive.dvd_of_fraction_map_dvd`.

### 3. `Mathlib/RingTheory/Polynomial/RationalRoot.lean`

**3a. Imports** -- add three `public import` lines after the existing three:

```lean
public import Mathlib.RingTheory.IntegralClosure.IntegrallyClosed
public import Mathlib.RingTheory.Localization.NumDen
public import Mathlib.RingTheory.Polynomial.ScaleRoots
public import Mathlib.RingTheory.Polynomial.GaussLemma
public import Mathlib.Algebra.Polynomial.BigOperators
public import Mathlib.RingTheory.Coprime.Lemmas
```

Confirmed sufficient by the green build; not confirmed minimal (run `shake`, per the checklist).

**3b. Module docstring** -- append one sentence to the file's `/-! ... -/` header, after "Finally, we
use this to show unique factorization domains are integrally closed.":

```
We also prove the generalization to root multiplicity: if `r` is a root of `p` with multiplicity
`m`, then `(den A r) ^ m ∣ p.leadingCoeff` (`den_pow_rootMultiplicity_dvd_leadingCoeff`), together
with the multi-point product form over a finite set of points
(`prod_den_pow_rootMultiplicity_dvd_leadingCoeff`).
```

**3c. New declarations** -- insert after `exists_integer_of_is_root_of_monic`'s proof and before the
pre-existing `namespace UniqueFactorizationMonoid` block (still inside `section
RationalRootTheorem`, so `A`, `K`, `UniqueFactorizationMonoid A`, `IsFractionRing A K`, and `open
IsFractionRing IsLocalization Polynomial UniqueFactorizationMonoid` are already in scope):

```lean
/-! ### Rational root theorem with multiplicity -/

/-- The reduced linear factor `C (den A r) * X - C (num A r)` is primitive: a
constant divisor divides both `den A r` (the coefficient of `X`) and `num A r` (up
to sign, the constant coefficient), and num/den are reduced (`num_den_reduced`). -/
theorem isPrimitive_den_mul_X_sub_C_num (r : K) :
    (C (den A r : A) * X - C (num A r)).IsPrimitive := by
  intro c hc
  have h1 : c ∣ (den A r : A) := by
    have h := (C_dvd_iff_dvd_coeff c _).mp hc 1
    simpa using h
  have h0 : c ∣ num A r := by
    have h := (C_dvd_iff_dvd_coeff c _).mp hc 0
    simpa using h
  exact num_den_reduced A r h0 h1

/-- Over `K`, the reduced linear factor of `r` is the unit multiple
`C (den A r) * (X - C r)` of the root factor at `r`. -/
theorem map_den_mul_X_sub_C_num (r : K) :
    (C (den A r : A) * X - C (num A r)).map (algebraMap A K)
      = C (algebraMap A K (den A r : A)) * (X - C r) := by
  have hden0 : algebraMap A K (den A r : A) ≠ 0 :=
    IsFractionRing.to_map_ne_zero_of_mem_nonZeroDivisors (den A r).2
  have hnum : algebraMap A K (num A r) = r * algebraMap A K (den A r : A) :=
    (div_eq_iff hden0).mp (mk'_num_den' A r)
  rw [Polynomial.map_sub, Polynomial.map_mul, map_C, map_C, Polynomial.map_X,
    hnum, C_mul]
  ring

/-- The leading coefficient of the reduced linear factor is `den A r`. -/
theorem leadingCoeff_den_mul_X_sub_C_num (r : K) :
    (C (den A r : A) * X - C (num A r)).leadingCoeff = (den A r : A) := by
  have h : C (den A r : A) * X - C (num A r)
      = C (den A r : A) * X + C (-(num A r)) := by
    rw [map_neg, sub_eq_add_neg]
  rw [h, leadingCoeff_linear (nonZeroDivisors.coe_ne_zero _)]

section

variable [Nonempty (NormalizedGCDMonoid A)]

/-- The `rootMultiplicity` power of the reduced linear factor divides `p` over `A`:
over `K` the factor is a unit multiple of `X - C r`, whose `rootMultiplicity` power
divides `p.map (algebraMap A K)`, and primitivity descends the divisibility. -/
theorem den_mul_X_sub_C_num_pow_rootMultiplicity_dvd (p : A[X]) (r : K) :
    (C (den A r : A) * X - C (num A r))
      ^ rootMultiplicity r (p.map (algebraMap A K)) ∣ p := by
  letI : NormalizedGCDMonoid A := Nonempty.some inferInstance
  refine IsPrimitive.dvd_of_fraction_map_dvd (K := K)
    (IsPrimitive.pow (isPrimitive_den_mul_X_sub_C_num r) _) ?_
  rw [Polynomial.map_pow, map_den_mul_X_sub_C_num, mul_pow]
  have hunit : IsUnit (C (algebraMap A K (den A r : A))
      ^ rootMultiplicity r (p.map (algebraMap A K))) :=
    (isUnit_C.mpr (isUnit_iff_ne_zero.mpr
      (IsFractionRing.to_map_ne_zero_of_mem_nonZeroDivisors (den A r).2))).pow _
  rw [hunit.mul_left_dvd]
  exact pow_rootMultiplicity_dvd _ r

/-- **Rational root theorem with multiplicity.** If `r : K` is a root of
`p : A[X]` over the fraction field `K` of the UFD `A` with multiplicity `m`, then
`(den A r) ^ m` divides the leading coefficient of `p`. Stated unconditionally with
`m = rootMultiplicity r (p.map (algebraMap A K))`; at `m = 1` it recovers
`den_dvd_of_is_root`. -/
theorem den_pow_rootMultiplicity_dvd_leadingCoeff (p : A[X]) (r : K) :
    (den A r : A) ^ rootMultiplicity r (p.map (algebraMap A K))
      ∣ p.leadingCoeff := by
  have h := leadingCoeff_dvd_leadingCoeff
    (den_mul_X_sub_C_num_pow_rootMultiplicity_dvd p r)
  rwa [leadingCoeff_pow, leadingCoeff_den_mul_X_sub_C_num] at h

/-- **Multi-point rational root theorem with multiplicities.** For any
finite set `s` of points of the fraction field, the product over `r ∈ s` of
`(den A r) ^ rootMultiplicity r` divides the leading coefficient of `p`. The
denominators need NOT be pairwise coprime in `A`; the recombination happens on the
polynomial side, where the root factors at distinct points are pairwise coprime
over the field `K`. -/
theorem prod_den_pow_rootMultiplicity_dvd_leadingCoeff (p : A[X]) (s : Finset K) :
    (∏ r ∈ s, (den A r : A) ^ rootMultiplicity r (p.map (algebraMap A K)))
      ∣ p.leadingCoeff := by
  have hgdvd : (∏ r ∈ s, (C (den A r : A) * X - C (num A r))
      ^ rootMultiplicity r (p.map (algebraMap A K))) ∣ p := by
    letI : NormalizedGCDMonoid A := Nonempty.some inferInstance
    refine IsPrimitive.dvd_of_fraction_map_dvd (K := K)
      (isPrimitive_prod _ _ fun r _ =>
        IsPrimitive.pow (isPrimitive_den_mul_X_sub_C_num r) _) ?_
    have hmap : (∏ r ∈ s, (C (den A r : A) * X - C (num A r))
          ^ rootMultiplicity r (p.map (algebraMap A K))).map (algebraMap A K)
        = (∏ r ∈ s, C (algebraMap A K (den A r : A))
              ^ rootMultiplicity r (p.map (algebraMap A K)))
            * ∏ r ∈ s, (X - C r) ^ rootMultiplicity r (p.map (algebraMap A K)) := by
      rw [Polynomial.map_prod, ← Finset.prod_mul_distrib]
      refine Finset.prod_congr rfl fun r _ => ?_
      rw [Polynomial.map_pow, map_den_mul_X_sub_C_num, mul_pow]
    have hunit : IsUnit (∏ r ∈ s, C (algebraMap A K (den A r : A))
        ^ rootMultiplicity r (p.map (algebraMap A K))) :=
      Finset.prod_induction _ IsUnit (fun a b ha hb => ha.mul hb) isUnit_one
        fun r _ => (isUnit_C.mpr (isUnit_iff_ne_zero.mpr
          (IsFractionRing.to_map_ne_zero_of_mem_nonZeroDivisors (den A r).2))).pow _
    rw [hmap, hunit.mul_left_dvd]
    refine Finset.prod_dvd_of_coprime ?_ fun r _ => pow_rootMultiplicity_dvd _ r
    intro a _ b _ hab
    exact (isCoprime_X_sub_C_of_isUnit_sub (sub_ne_zero_of_ne hab).isUnit).pow
  have hleadeq : (∏ r ∈ s, (C (den A r : A) * X - C (num A r))
        ^ rootMultiplicity r (p.map (algebraMap A K))).leadingCoeff
      = ∏ r ∈ s, (den A r : A) ^ rootMultiplicity r (p.map (algebraMap A K)) := by
    rw [leadingCoeff_prod]
    exact Finset.prod_congr rfl fun r _ => by
      rw [leadingCoeff_pow, leadingCoeff_den_mul_X_sub_C_num]
  rw [← hleadeq]
  exact leadingCoeff_dvd_leadingCoeff hgdvd

end
```

Full names after insertion (top-level, unqualified, matching `den_dvd_of_is_root`'s own convention
in this file): `isPrimitive_den_mul_X_sub_C_num`, `map_den_mul_X_sub_C_num`,
`leadingCoeff_den_mul_X_sub_C_num`, `den_mul_X_sub_C_num_pow_rootMultiplicity_dvd`,
`den_pow_rootMultiplicity_dvd_leadingCoeff`, `prod_den_pow_rootMultiplicity_dvd_leadingCoeff`.

## Checklist: what remains

- [ ] Clone or update the existing fork (`owenpkent/mathlib4`, already used for P1/P2) locally, or
      add it as a second remote to an existing mathlib4 checkout.
- [ ] Branch off latest `master`, e.g. `git switch -c rational-root-floor`.
- [ ] Apply the three edits in "The port, file by file" above (imports, docstring, declarations) --
      this is now a mechanical copy-paste, not a re-derivation: the drift check found only one
      irrelevant line of difference between the pinned `v4.30.0` this was built against and live
      master, in a proof this port never touches.
- [ ] `lake exe cache get` (if not already warm for the checkout's commit), then `lake build
      Mathlib.RingTheory.Polynomial.RationalRoot` to reconfirm green on the fork checkout's actual
      master commit. (This session confirmed green + axiom-clean against the pinned `v4.30.0`
      commit via the project's own dependency checkout, then fully reverted; it has not yet been
      rebuilt on a fork clone's live master HEAD, since no such clone exists on this machine.)
- [ ] `lake exe lint-style` and `lake exe shake --fix`; expect at most an import-minimization report
      on the three new `public import`s in `RationalRoot.lean` (confirmed sufficient, not confirmed
      minimal).
- [ ] Commit with a Conventional-Commits message matching the PR title; push to the fork.
- [ ] Open the PR against `leanprover-community/mathlib4:master`; paste the title and description
      from [`rational_root_floor_pr_body.md`](rational_root_floor_pr_body.md).
- [ ] Request review on the Lean Zulip `#mathlib4` / PR-review stream.
- [ ] Respond to review in Owen's own words (Mathlib's AI policy forbids LLM-written review
      replies).

**Timing note.** As of 2026-07-17, P2 (`mathlib4#41132`) has an unaddressed round-2 review (see
`p2_review_round2_brief.md`). PUBLICATIONS.md's P10 entry suggests opening this PR "after P1/P2
review bandwidth clears" -- a sequencing preference for Owen to weigh, not a technical blocker; the
port itself has no dependency on P1 or P2 landing first.
