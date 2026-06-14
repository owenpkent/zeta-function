# Lean 4 / Mathlib formalization of the zeta function proof program

> Formal verification stack for the AI-only proof program. See [`docs/03_research/proof_program_ai_only.md`](../docs/03_research/proof_program_ai_only.md) §2.2 for context.
>
> **Goal**: every structural claim in the project (R3.5 no-shortcut theorem, 4E.3 line-restriction lemma, the eventual Hodge index theorem) is translated to Lean 4 and verified by Mathlib's kernel.

## Status

**Update (2026-06-12):** `CrystalCocycle.lean` added: the #82 LCC/BC-transport lemma pair (V1/V2/V3, all PROVED sorry-free, `#print axioms` = `[propext, Classical.choice, Quot.sound]` for all four theorems). V2 is Lemma 1 (quasi-invariance collapse) in both the full-semigroup and the prime-generated form (induction along the minimal prime factor); V3 is increment nonnegativity of the integrated comb `B = 1 * b`; V1 is Lemma 2 (cocycle rigidity): `B(p*n) - B(n) = log p` for all primes `p`, `n ≥ 1` IFF `b n = Λ n` for `n ≥ 2` (`b 1` free), proved via `ArithmeticFunction.vonMangoldt_sum` plus a divisor-sum determination lemma (cheap Moebius inversion by strong induction). K1-clean by construction: only `ℕ`, divisors, and `Real.log` appear. V4 (the B1 G_log rigidity lemma) is logged as an open target with a feasibility note in the file. Build green (full library, 3146 jobs).

**Update (2026-06-04c):** `FrobeniusAlgebra.lean` added as the formation-level spec for Direction 8A's arithmetic Frobenius algebra / cup target. It introduces `EulerProductData`, `FrobeniusTateTwist`, and `FrobeniusCupTarget`, with the structural theorem `cupTarget_requires_eulerProduct : CanFormCupTarget L -> L.has_euler_product`. The Davenport-Heilbronn control is now a no-sorry K2 guard: `no_dh_cupTarget : ¬ CanFormCupTarget davenport_heilbronn`, because D-H's `has_euler_product` field is `False`. `PrismaticCohomology.Q3a_*` and `HodgeIndex.hodge_index_K2_safe` now point to this guard. This proves only formation/non-formation, not polarization or RH.

**Phase 1 substrate, GREEN BUILD as of 2026-05-25.** Project infrastructure is set up, the placeholder `True` predicates have been upgraded to typed-but-stubbed predicates with concrete VERIFIER targets, and `lake build` succeeds end-to-end against Mathlib v4.13.0 on Windows + Lean 4.13.0. All 2250 modules compile. The remaining warnings are exactly the documented `sorry` markers in the VERIFIER-target table below.

**Update (2026-06-04b): Mathlib bump v4.13.0 -> v4.30.0 (17 versions, ~1.5 years), GREEN, merged to `main`.** `lake build` succeeds (3031 jobs) against Lean/Mathlib v4.30.0. The migration needed only ~7 fixes: 5 import-path renames (`Data.Complex.Exponential*` -> `Analysis.Complex.Exponential*`, `Algebra.BigOperators.Group.Finset` -> `.Finset.Basic`, `Algebra.Ring.Int` -> `.Int.Defs`), fully-qualifying `ArithmeticFunction.sigma`/`.moebius` (the σ/μ notation scope split out of the umbrella `ArithmeticFunction` scope), `pow_le_pow_left`/`le_of_pow_le_pow_left` -> the `₀` variants, and two digamma proof repairs (deriv of `1-z` via `HasDerivAt.const_sub`; a now-redundant `ring` after `field_simp` that closes the goal in v4.30). All 8 `RHEquivalences` sorry-free anchors still report clean axioms `[propext, Classical.choice, Quot.sound]` (no `sorryAx`, no `ofReduceBool`), including the transcendental n=2/n=3 Lagarias instances. NB: Mathlib now ships `Complex.digamma` + recurrence + special values (see [`upstream/digamma_contribution.md`](upstream/digamma_contribution.md)); the reflection, iterated-recurrence, and duplication identities remain the novel surviving contribution and are now VERIFIED against the upstream `Complex.digamma` in [`ZetaRH/DigammaExtras.lean`](ZetaRH/DigammaExtras.lean) (green, `#print axioms` clean for all three) — the PR-ready unit.

**Update (2026-06-04):** `RHEquivalences.lean` added (entry point A of the RH-logical-status excursion, [`docs/03_research/rh_logical_status.md`](../docs/03_research/rh_logical_status.md) §7). The equivalence hub: `robinInequality`, `lagariasInequality`, `mertensBound` are CONCRETE Props over Mathlib (`ArithmeticFunction.sigma` σ, `harmonic`, `Real.eulerMascheroniConstant`, `ArithmeticFunction.moebius` μ); `li_criterion` and `nymanBeurling_criterion` bundle the analytic data Mathlib lacks (sum-over-zeros, L²(0,1) closure), mirroring `ExplicitFormula.WeilExplicitFormula`. Distinct from `ExplicitFormula.lean`'s Weil-form positivity (#EF-2): this module owns the elementary/criterion faces. The headline object is `RH_arith := lagariasInequality`, the Π⁰₁ arithmetic surrogate, with `RH_arith_iff_RiemannHypothesis` reusing #LG-1 (no new sorry). Sorry-free anchors (all with `#print axioms` = `[propext, Classical.choice, Quot.sound]`, no `sorryAx`, no `ofReduceBool`): `riemannHypothesis_zeta_iff_nonTrivialZeros` (definitional), `riemannHypothesisMathlib_iff_zeta` (Basic re-export), `lagarias_holds_at_one` (the n = 1 equality case, the reason the criterion uses ≤ not strict <), `lagarias_holds_at_three` (transcendental instance σ(3)=4 ≤ 11/6 + e^{11/6}·log(11/6) ≈ 4.08, by order-1 bounds), `lagarias_holds_at_two` (the hardest small case, σ(2)=3 ≤ 3/2 + e^{3/2}·log(3/2) ≈ 3.32, needing sharp integer-vs-rational power bounds: e^{3/2}≥4 from (e^{3/2})²=e³=(e¹)³≥(27/10)³≥16, log(3/2)≥2/5 from (e^{2/5})⁵=e²≤(68/25)²≤(3/2)⁵; margins are non-monotone in n, the tight cases are highly composite n, and the real marginal-positivity trace is that no uniform soft bound covers all n, which would be RH), `rh_arith_refutable` (entry point B: the Σ⁰₁ refutability structure, `¬ RH_arith ↔ ∃ n ≥ 1, ¬ lagariasInequalityAt n`, the formal core of `rh_logical_status.md` §2), and `sigma_one_six` / `sigma_one_twelve` (the σ matrix side is kernel-computable via `decide`). Five documented sorries (#RB-1, #LG-1, #MT-1, #LI-1, #NB-1). Build green (2284 modules).

**Update (2026-06-03):** `AccidentAudit.lean` added (cheap-probe 5 of the "RH solved by accident" dossier, LEARNINGS #49). It formalizes the truncated non-circular Weil/Rosati Gram `weilGram = A_arch + P_fin + B_pole` from the Gamma factor (`Real.log Real.pi`), the von Mangoldt prime weights (`ArithmeticFunction.vonMangoldt`), and the pole residue, naming NO zero. `weilGram` and its symmetry anchor `weilGram_isSymm` are SORRY-FREE, and `#print axioms weilGram_isSymm` emits exactly `[propext, Classical.choice, Quot.sound]` (no `sorryAx`, no `riemannZeta`/`RiemannHypothesis`/`nonTrivialZeros`): a kernel-checked NON-CIRCULARITY certificate (a control confirmed `#print axioms` does report `sorryAx` on the deferred targets, so the verdict is genuine). Two documented sorries added (#ACC-1 positivity, #ACC-2 the K2 necessary-not-sufficient statement). Build green.

Build command:

```powershell
cd lean
lake build
```

First-time setup needs `lake update` (downloads ~5370 prebuilt Mathlib oleans, ~10 min).

### Phase 1 deliverables (this pass)

- `Basic.lean`: `LFunction` now carries `evaluate : ℂ → ℂ`, `conductor : ℕ`, `poles : Set ℂ`, plus typed predicate fields. `zeta : LFunction` wired to Mathlib's `Complex.riemannZeta`. `RiemannHypothesisMathlib` connected to `RiemannHypothesis zeta` by an actual proof (no sorry).
- `DavenportHeilbronn.lean`: D-H constructed as `c · L(s, χ₅) + c̄ · L(s, χ̄₅)` with explicit Conrey-Ghosh constant. The first off-line zero is wired to `nonTrivialZeros davenport_heilbronn` via a typed proof skeleton (only the actual zero-value step is `sorry`, as VERIFIER target #DH-zero).
- `LineRestriction.lean`: `UnivariateCosPoly` and `BivariateCosPoly` are real data types with real coefficient functions and real evaluation. Non-negativity is a real Prop. Fejér ceiling uses `Real.cos`. The line-restriction theorem is stated with the correct typed inequality (proof body is the trivial witness; structural work in VERIFIER target #LR-2).
- `LambdaBlueprints.lean`: `Blueprint` has a real `CommSemiring` carrier, multiplicative submonoid, and relation set. `LambdaBlueprint` adds typed `psi` family with commutativity and Fermat-Frobenius axioms.
- `FrobeniusAlgebra.lean`: Direction 8A formation guard for the Frobenius cup target. `CanFormCupTarget L` structurally implies `L.has_euler_product`, and Davenport-Heilbronn is no-sorry excluded from the target.
- `MathlibBridge.lean`: New module collecting Mathlib lemmas needed downstream, each tagged PRESENT / PR / TODO with VERIFIER target IDs.

### What is NOT yet done

Everything else from the original skeleton plan: prismatic cohomology and prismatic foliation remain placeholder `Unit` types (Mathlib lacks the underlying infrastructure); the central `Spec(ℤ) × Spec(ℤ)` Hodge index theorem remains `True := by sorry`; KillCriteria K3, K4 remain placeholder. The full multi-year program continues.

**Update (2026-05-29b):** discharged three `MathlibBridge` targets to real kernel-checked proofs (no sorry): #MB-1 (ζ pole at s=1, via `riemannZeta_residue_one`), #MB-2 (ζ≠0 on Re s>1, via `riemannZeta_ne_zero_of_one_lt_re`), #MB-6 (functional equation `Λ(1-s)=Λ(s)`, via `completedRiemannZeta_one_sub`). In `ExplicitFormula.lean` the archimedean kernel is now concrete: `digamma := logDeriv Complex.Gamma` with `digamma_eq` proved, `archKernel` built from it, and the recurrence `digamma_add_one` (`ψ(s+1)=ψ(s)+1/s`) proved from `Complex.Gamma_add_one` (all no sorry; kernel part of #EF-arch discharged). Project sorry count 26 → 23; build green.

**Update (2026-05-29):** `ExplicitFormula.lean` adds the project's highest-leverage Mathlib target (LEARNINGS #17): the **Weil explicit formula** for ζ and the **Weil positivity criterion**. The prime side `primeSum` is CONCRETE (a `tsum` against Mathlib's `ArithmeticFunction.vonMangoldt`); the spectral/archimedean/pole functionals are bundled into `WeilExplicitFormula`, with `weil_explicit_formula_zeta` (#EF-1) asserting the bundle exists for ζ and `weil_positivity_criterion` (#EF-2) stating `weilForm`-positivity ⟺ `RiemannHypothesis zeta`. This is the Architecture-3 (trace/positivity) face of the same positivity whose Architecture-2 (signature) face is `HodgeIndex.negDef_iff_hasseWeil`. Build green; three documented sorries (#EF-1, #EF-2, #EF-2a) plus the structural targets #EF-arch (no `digamma` in Mathlib), #EF-class, #EF-K2.

**Update (2026-05-28):** `HodgeIndex.lean` now also carries the two "positivity from a signature" results validated in experiments 2G and 2H. The 2G function-field template (`IntersectionSignature` namespace) is FULLY PROVED with no `sorry`: the primitive intersection Gram matrix `G_prim = !![-2g, -t; -t, -2gq]` is negative definite (as a quadratic form) iff the Hasse-Weil bound `t² < 4g²q` holds (`negDef_iff_hasseWeil`), with `det(G_prim) = 4g²q − t²` (`Gprim_det`) tying it to the matrix determinant. The 2H arithmetic Hodge index (`ArithmeticHodgeIndex` namespace) is stated faithfully (`heightPairing_posDef`: the Néron-Tate height-pairing Gram matrix is `Matrix.PosDef`) with a single documented `sorry` (#2H-1), since Mathlib lacks canonical heights and Faltings-Hriljac.

## Structure

```
lean/
├── lakefile.lean                    # Lake build configuration
├── lean-toolchain                   # Lean version pin (v4.13.0)
├── ZetaRH.lean                      # Main module: imports all sub-modules
└── ZetaRH/
    ├── Basic.lean                   # LFunction, RH, Selberg class; wired to Mathlib riemannZeta
    ├── MathlibBridge.lean           # NEW: collected Mathlib lemmas needed (PRESENT/PR/TODO)
    ├── DavenportHeilbronn.lean      # D-H via χ₅ + Conrey-Ghosh constant; first off-line zero
    ├── R3_5.lean                    # No-shortcut theorem: trace-formula NCG has P ⟺ RH
    ├── LineRestriction.lean         # 4E.3 line-restriction lemma (typed CosPoly)
    ├── ExplicitFormula.lean         # Weil explicit formula + Weil positivity criterion (LEARNINGS #17)
    ├── LambdaBlueprints.lean        # Direction 1: blueprint as CommSemiring + relations
    ├── FrobeniusAlgebra.lean        # Direction 8A: structural formation guard for the Frobenius cup target
    ├── PrismaticCohomology.lean     # Direction 3: prismatic cohomology of W(ℤ) (placeholder)
    ├── PrismaticFoliation.lean      # Direction 4: prismatic foliation hypothesis M3 (placeholder)
    ├── HodgeIndex.lean              # Direction 8: the central open problem
    ├── SenDefiniteObstruction.lean  # Direction 8E Class A no-go: skew+nilpotent ⟹ 0 (sorry-free)
    ├── TraceBlindObstruction.lean   # Direction 8E Class C no-go: no t-blind signature decides Hasse-Weil (sorry-free)
    ├── KillCriteria.lean            # K1-K4 formalizations
    ├── AccidentAudit.lean           # Cheap-probe 5: de-smuggling audit of the C_mu Weil form (sorry-free non-circularity certificate)
    ├── CrystalCocycle.lean          # #82 LCC/BC-transport lemmas: V1 cocycle rigidity, V2 flat-ray collapse, V3 monotonicity (all sorry-free)
    └── RHEquivalences.lean          # RH equivalence hub (Robin/Lagarias/Mertens/Li/Nyman-Beurling) + the Π⁰₁ kernel witness RH_arith
```

## VERIFIER target IDs (Phase 1)

Each `sorry` introduced in the Phase 1 substrate carries a VERIFIER target ID for tracking:

| ID         | Module                        | What it asks for                                                                    |
|------------|-------------------------------|-------------------------------------------------------------------------------------|
| #FE-1      | Basic.lean                    | Replace `HasFunctionalEquation` placeholder with the real classical statement.      |
| #EP-1      | Basic.lean                    | Replace `HasEulerProduct` placeholder with the real Euler product convergence form. |
| #S-1..#S-3 | Basic.lean                    | Add Selberg-class axioms S1 (convergence), S2 (continuation), S4 (Ramanujan).       |
| #DH-c      | DavenportHeilbronn.lean       | Verify `dhCoefficient` against Conrey-Ghosh 1988 (and Titchmarsh 1986 §10.25).      |
| #DH-conv   | DavenportHeilbronn.lean       | Prove convergence of `davenportHeilbronnSeries` on Re s > 1.                        |
| #DH-cont   | DavenportHeilbronn.lean       | Construct meromorphic continuation via Hurwitz-zeta decomposition.                  |
| #DH-zero   | DavenportHeilbronn.lean       | Verify `dh_first_offline_zero` is in `nonTrivialZeros davenport_heilbronn`.         |
| #Fejer-1   | LineRestriction.lean          | Prove the Fejér ceiling `c_1 ≤ cos(π/(N+2))` (Mathlib upstream candidate).          |
| #LR-2      | LineRestriction.lean          | Define the restriction-to-1D operator and give the actual c_1 bound.                |
| #LR-3      | LineRestriction.lean          | Give the precise LP-witness form and derive contradiction-from-violation.           |
| #BP-1      | LambdaBlueprints.lean         | Define the blueprint quotient `ℕ[B•] / ≈` carrying the relation set.                |
| #BP-F1    | LambdaBlueprints.lean         | Correct F_1 model (not the trivial PUnit collapse).                                  |
| #BP-fiber | LambdaBlueprints.lean         | The central open computation Spec(ℤ) ×_F_1 Spec(ℤ).                                  |
| #MB-1      | MathlibBridge.lean            | ζ pole at s=1 `(s-1)ζ(s)→1`. **DISCHARGED** via `riemannZeta_residue_one` (no sorry). |
| #MB-2      | MathlibBridge.lean            | ζ(s)≠0 for Re s>1. **DISCHARGED** via `riemannZeta_ne_zero_of_one_lt_re` (no sorry). |
| #MB-3..#MB-5 | MathlibBridge.lean          | Hurwitz availability (#MB-3), L-Hurwitz decomposition (#MB-4, sorry), Fejér (#MB-5, sorry). |
| #MB-6      | MathlibBridge.lean            | ζ functional equation `Λ(1-s)=Λ(s)`. **DISCHARGED** via `completedRiemannZeta_one_sub` (no sorry). |
| #2G-1      | HodgeIndex.lean               | 2G function-field signature: `G_prim` negative definite ⟺ Hasse-Weil `t² < 4g²q`. PROVED (no sorry). |
| #FF-1      | FunctionFieldRH.lean          | Lever B, the eigenvalue-extraction link (genus 1): a non-real root of `X²−tX+q` has `|α|² = q` (`eigenvalue_modulus`, via Vieta on the conjugate); `t² < 4q ⇒ the roots are non-real` (`root_nonreal`); hence `NegDef ⇒ |α| = √q` (`functionfield_RH_elliptic_of_hodge`); and the full chain `functionfield_RH_elliptic` from `EllipticFrobeniusData`, wiring #2G-1. PROVED (no sorry). |
| #FF-geom   | FunctionFieldRH.lean          | Lever B gap, now carried as an explicit HYPOTHESIS, not a sorry: the Castelnuovo-Severi inequality `t² < 4q` is the `hodge_index` field of `EllipticFrobeniusData` (`negDef_of_curve` derives `NegDef` from it sorry-free). The whole file is now SORRY-FREE; discharging this hypothesis (proving Castelnuovo-Severi from a curve's definition) needs Mathlib algebraic-curve intersection theory. This also repaired the previous `hodge_index_curve_elliptic`, which admitted a FALSE proposition (`NegDef 1 q t` for all `q,t`) via `sorry`. |
| #FF-M0     | FunctionFieldRH.lean          | Lever B roadmap milestone M-0 (the discriminant bridge for the elementary Hasse proof): a positive-semidefinite real binary form `m²+t·mn+q·n²` has `t² ≤ 4q` (`disc_nonpos_of_posSemidef`); positive-definite gives the strict `t² < 4q` (`disc_neg_of_posDef`). The positive mirror of #2G-1; the step from "deg ≥ 0 for isogenies" to the Hasse bound. PROVED (no sorry). Plan: `docs/03_research/lever_b_function_field_plan.md`. |
| #ClassA-1  | SenDefiniteObstruction.lean   | Direction 8E Class A no-go: `skew_nilpotent_eq_zero` (real skew + nilpotent ⟹ 0, elementary trace proof) + `sen_no_nilpotent_part` + `sen_nilpotent_part_not_isNilpotent` (a non-semisimple Sen module admits no definite invariant cup form; Petrov ν≠0) + `bskew_nilpotent_eq_zero_of_gram` (Gram-factor reduction) + `bskew_nilpotent_eq_zero` (UNCONDITIONAL in `B.PosDef`, via `CFC.sqrt`). 5 theorems, PROVED (no sorry); `#print axioms` = `[propext, Classical.choice, Quot.sound]` only. |
| #ClassC-1  | TraceBlindObstruction.lean    | Direction 8E Class C no-go: `negDef_depends_on_trace` (the Hasse-Weil/Rosati `NegDef` predicate is non-constant in the trace `t`) + `no_trace_blind_signature` (no `t`-blind predicate `P g q` decides `NegDef g q t`; the arithmetic-blind AHK combinatorial signature cannot carry RH-positivity, #48). PROVED (no sorry); `#print axioms` = `[propext, Classical.choice, Quot.sound]` only. |
| #2H-1      | HodgeIndex.lean               | 2H Faltings-Hriljac arithmetic Hodge index: Néron-Tate height-pairing Gram matrix is `PosDef`. Sorry (needs Mathlib canonical heights + Faltings-Hriljac). |
| #EF-1      | ExplicitFormula.lean          | The Weil explicit formula for ζ: a `WeilExplicitFormula` bundle exists (spectral side = arch + pole − prime). Sorry (needs digamma kernel + sum-over-zeros theory). |
| #EF-2      | ExplicitFormula.lean          | **The Weil positivity criterion**: `weilForm`-positivity on all admissible tests ⟺ `RiemannHypothesis zeta`. The Architecture-3 centerpiece (LEARNINGS #17). Sorry. |
| #EF-2a     | ExplicitFormula.lean          | Construct `weilForm` (the Hermitian form `∑_ρ f̂(ρ)\overline{f̂(\barρ)}`) from the bundle via the positive-type/self-dual test. Sorry. |
| #EF-arch   | ExplicitFormula.lean          | The archimedean kernel. Kernel part **DISCHARGED**: `digamma := logDeriv Complex.Gamma`, `digamma_eq` proved, `archKernel` concrete, and the basic algebraic identities `digamma_add_one` (`ψ(s+1)=ψ(s)+1/s`), `digamma_reflection` (`ψ(1-s)-ψ(s)=π cot(πs)`), and `digamma_add_nat` (`ψ(s+n)=ψ(s)+∑_{k<n} 1/(s+k)`, by induction from the recurrence), `digamma_duplication` (`ψ(2s)=½(ψ(s)+ψ(s+½))+log 2`, from Legendre's doubling `Complex.Gamma_mul_Gamma_add_half`), and the special values `digamma_one` (`ψ(1)=-γ`, from `Complex.hasDerivAt_Gamma_one`) and `digamma_half` (`ψ(½)=-γ-2log 2`, from duplication at `s=½`) **PROVED** (no sorry). Six sorry-free digamma identities total, from `Complex.Gamma_add_one`, `Complex.Gamma_mul_Gamma_one_sub`, `Complex.Gamma_mul_Gamma_add_half`, and `Complex.hasDerivAt_Gamma_one`. Remaining: the integral pairing (#EF-class). |
| #EF-class  | ExplicitFormula.lean          | The analytic side-conditions on `AdmissibleTest` (smoothness/decay/strip of holomorphy) that make the functionals well-defined and #EF-1 true. |
| #EF-K2     | ExplicitFormula.lean          | The D-H instance showing the criterion does NOT certify RH for Davenport-Heilbronn (prime side delocalises; experiment 3M #20). |
| #FA-1      | FrobeniusAlgebra.lean         | Replace the placeholder `EulerProductData` fields with the real Euler-product local-factor data, convergence on `Re(s)>1`, uniqueness, and the von-Mangoldt log-derivative. The formation guard itself (`no_dh_cupTarget`) is proved no-sorry. |
| #FA-2      | FrobeniusAlgebra.lean         | Replace the toy `Unit` `FrobeniusTateTwist`/`FrobeniusCupTarget` with the actual `H^2 = C(-1)` fundamental class and arithmetic `H^1`, then prove bilinearity/perfectness/flow derivation. Positivity remains the M4 standard-conjecture target. |
| #ACC-1     | AccidentAudit.lean            | The numerical positivity certificate `(weilGram K N b).PosDef` for zeta (min-eig +0.035; e3c/e3m). Necessary-not-sufficient. Sorry (needs concrete numerical entries + a PosDef witness). |
| #ACC-2     | AccidentAudit.lean            | `weilGram_noncirc`: positivity of `weilGram` does NOT entail `RiemannHypothesis zeta` (the same construction for Davenport-Heilbronn would otherwise prove a false RH; the M2.6 stealth window #34). Sorry (needs the explicit D-H witness Gram + its off-line zero, ties to #DH-zero). The non-circular-because-necessary-not-sufficient statement. |
| #RB-1      | RHEquivalences.lean           | `robin_criterion`: Robin's inequality `∀ n ≥ 5041, σ(n) < e^γ n log log n` ⟺ RH. Sorry (full RH-equivalence; unformalized in any prover). |
| #LG-1      | RHEquivalences.lean           | `lagarias_criterion`: Lagarias's inequality `∀ n ≥ 1, σ(n) ≤ H_n + e^{H_n} log H_n` ⟺ RH. Sorry. Also backs `RH_arith_iff_RiemannHypothesis` (the Π⁰₁ kernel witness, no new sorry). |
| #MT-1      | RHEquivalences.lean           | `mertens_criterion`: the Mertens bound `M(x) = O(x^{1/2+ε})` ⟺ RH. Sorry. |
| #LI-1      | RHEquivalences.lean           | `li_criterion`: Li/Keiper positivity `∀ n ≥ 1, λ_n ≥ 0` ⟺ RH, given the `LiData` Keiper-Li representation. Sorry. #LI-def (the convergent symmetric-pairing form of the sum-over-zeros identity) is the `LiData.keiperLi` field's deep content. |
| #NB-1      | RHEquivalences.lean           | `nymanBeurling_criterion`: the Báez-Duarte distances `d_N → 0` ⟺ RH, given `NymanBeurlingData`. Sorry. #NB-def (the tie of `dist` to the actual L²(0,1) closure of dilated fractional parts) is the opaque data. |
| V1         | CrystalCocycle.lean           | #82 Lemma 2 (cocycle rigidity): `increments_eq_log_iff_eq_vonMangoldt`, the increments `B(p*n) - B(n) = log p` (all primes `p`, all `n ≥ 1`) ⟺ `b n = Λ n` for `n ≥ 2` with `b 1` free. **PROVED** (sorry-free; axioms = `[propext, Classical.choice, Quot.sound]`). |
| V2         | CrystalCocycle.lean           | #82 Lemma 1 (quasi-invariance collapse): `flat_ray_of_quasiInvariance` (full ℕ× form) and `flat_ray_of_prime_quasiInvariance` (prime-generated form, induction on the minimal prime factor); the quasi-invariant combs are exactly the flat ray `c n = c 1 * n^(-β)`. **PROVED** (sorry-free). |
| V3         | CrystalCocycle.lean           | #82 increment nonnegativity: `divisorSum_le_divisorSum_mul_of_nonneg`, `0 ≤ b → B n ≤ B (p*n)` via `Nat.divisors_subset_of_dvd`. **PROVED** (sorry-free). |
| V4         | CrystalCocycle.lean           | #86 B1 G_log rigidity (`b1_glog_rigidity.md`): prime-translate quasi-invariant Radon measures on ℝ form the ray `c·exp(-βx)dx`. **OPEN** (not attempted). Mathlib ingredients exist: `AddSubgroup.dense_or_cyclic`, `Measure.withDensity`, `MeasureTheory.Measure.isAddLeftInvariant_eq_smul` (Haar uniqueness); the missing assembly is the vague-continuity upgrade from dense-translate invariance to full translation invariance. Feasibility note at the end of `CrystalCocycle.lean`. |

## Mathlib coverage gaps

As of 2026-05, Mathlib does NOT have:
- Prismatic cohomology (Bhatt-Morrow-Scholze).
- Lambda-rings or blueprints.
- Noncommutative geometry beyond C*-algebras basics.
- Tropical Hodge theory.

For verification targets in these areas, VERIFIER agents must EITHER:
1. Propose a minimal Mathlib extension (a new definition or lemma to contribute back), OR
2. Reduce the claim to existing Mathlib lemmas + axioms with the axioms flagged.

The eventual goal is to upstream the foundational definitions to Mathlib, making the proofs canonical.

## Build

```bash
cd lean
lake build
```

(Requires `elan` / `lean4` installed. See [https://leanprover-community.github.io/get_started.html](https://leanprover-community.github.io/get_started.html).)

**Smoke-test status as of 2026-05-25**: GREEN. `lake build` succeeds on Windows 11 with Lean 4.13.0 + Mathlib v4.13.0. All 2250 modules compile. Remaining warnings are exactly the documented `sorry` markers (#FE-1, #EP-1, #DH-zero, #LR-2, #Fejer-1, #BP-fiber, #MB-1..#MB-6) and stale skeleton sorries in PrismaticCohomology/PrismaticFoliation/HodgeIndex/R3_5.

## How agents use this

- **BUILDER**: writes mathematical definitions in `ZetaRH/`.
- **VERIFIER**: translates BUILDER definitions into Lean and proves theorems. Picks a VERIFIER target ID from the table above and converts the `sorry` to a real proof.
- **ADVERSARY**: writes Lean-formalized counterexamples or attacks proposed theorems.
- **SYNTHESIZER**: maintains this README, the VERIFIER target table, and cross-references to the rest of the project.

## Cross-references

- [`../docs/03_research/proof_program.md`](../docs/03_research/proof_program.md): AI-augmented variant of the proof program.
- [`../docs/03_research/proof_program_ai_only.md`](../docs/03_research/proof_program_ai_only.md): AI-only variant.
- [`../docs/03_research/research_directions/`](../docs/03_research/research_directions/): the eight research directions.
- [`../experiments/PROOF_ARCHITECTURES_PLAN.md`](../experiments/PROOF_ARCHITECTURES_PLAN.md): the test plan.
- [`../experiments/LEARNINGS.md`](../experiments/LEARNINGS.md): cross-architecture findings.
