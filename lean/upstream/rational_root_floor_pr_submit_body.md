This PR adds the rational root theorem with multiplicity to
`Mathlib/RingTheory/Polynomial/RationalRoot.lean`:

- `den_pow_rootMultiplicity_dvd_leadingCoeff`: if `r : K` is a root of `p : A[X]` (`A` a UFD, `K`
  its fraction field) with multiplicity `m = rootMultiplicity r (p.map (algebraMap A K))`, then
  `(den A r) ^ m ∣ p.leadingCoeff`;
- `prod_den_pow_rootMultiplicity_dvd_leadingCoeff`: the multi-point version, `∏ r ∈ s, (den A r) ^
  rootMultiplicity r ∣ p.leadingCoeff` over any finite set `s : Finset K` (the denominators need
  **not** be pairwise coprime in `A`; the recombination happens on the polynomial side, where the
  root factors at distinct points are pairwise coprime over `K`);
- `den_mul_X_sub_C_num_pow_rootMultiplicity_dvd`: the `A`-level form both corollaries come from,
  `(C (den A r) * X - C (num A r)) ^ m ∣ p` in `A[X]`.

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
declarations (three public, and three `private` helpers about the reduced linear factor:
`isPrimitive_den_mul_X_sub_C_num`, `map_den_mul_X_sub_C_num`,
`leadingCoeff_den_mul_X_sub_C_num`) need only the file's existing
`UniqueFactorizationMonoid A` context: where a
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

**Import-graph cost: zero downstream.** The three added imports grow `RationalRoot.lean`'s own
transitive closure by 30 modules (1614 -> 1644), mostly the `FieldTheory.SplittingField` /
`IntermediateField` / `Minpoly` cone that `GaussLemma.lean` pulls in. That growth does not
propagate: `RationalRoot.lean` has exactly three importers in Mathlib
(`RingTheory/Polynomial/IsIntegral.lean`, `RingTheory/DedekindDomain/Basic.lean`,
`NumberTheory/Niven.lean`), and all three already import `GaussLemma` and
`SplittingField.Construction` transitively today, so no file in Mathlib gains an import from this
PR. If a maintainer would still rather keep `RationalRoot.lean` light, the six declarations move to
a new `RingTheory/Polynomial/RationalRootMultiplicity.lean` without any proof change; I am happy to
do that on request.

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
