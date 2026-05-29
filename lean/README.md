# Lean 4 / Mathlib formalization of the zeta function proof program

> Formal verification stack for the AI-only proof program. See [`docs/03_research/proof_program_ai_only.md`](../docs/03_research/proof_program_ai_only.md) §2.2 for context.
>
> **Goal**: every structural claim in the project (R3.5 no-shortcut theorem, 4E.3 line-restriction lemma, the eventual Hodge index theorem) is translated to Lean 4 and verified by Mathlib's kernel.

## Status

**Phase 1 substrate, GREEN BUILD as of 2026-05-25.** Project infrastructure is set up, the placeholder `True` predicates have been upgraded to typed-but-stubbed predicates with concrete VERIFIER targets, and `lake build` succeeds end-to-end against Mathlib v4.13.0 on Windows + Lean 4.13.0. All 2250 modules compile. The remaining warnings are exactly the documented `sorry` markers in the VERIFIER-target table below.

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
    ├── PrismaticCohomology.lean     # Direction 3: prismatic cohomology of W(ℤ) (placeholder)
    ├── PrismaticFoliation.lean      # Direction 4: prismatic foliation hypothesis M3 (placeholder)
    ├── HodgeIndex.lean              # Direction 8: the central open problem
    └── KillCriteria.lean            # K1-K4 formalizations
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
| #2H-1      | HodgeIndex.lean               | 2H Faltings-Hriljac arithmetic Hodge index: Néron-Tate height-pairing Gram matrix is `PosDef`. Sorry (needs Mathlib canonical heights + Faltings-Hriljac). |
| #EF-1      | ExplicitFormula.lean          | The Weil explicit formula for ζ: a `WeilExplicitFormula` bundle exists (spectral side = arch + pole − prime). Sorry (needs digamma kernel + sum-over-zeros theory). |
| #EF-2      | ExplicitFormula.lean          | **The Weil positivity criterion**: `weilForm`-positivity on all admissible tests ⟺ `RiemannHypothesis zeta`. The Architecture-3 centerpiece (LEARNINGS #17). Sorry. |
| #EF-2a     | ExplicitFormula.lean          | Construct `weilForm` (the Hermitian form `∑_ρ f̂(ρ)\overline{f̂(\barρ)}`) from the bundle via the positive-type/self-dual test. Sorry. |
| #EF-arch   | ExplicitFormula.lean          | The archimedean kernel. Kernel part **DISCHARGED**: `digamma := logDeriv Complex.Gamma`, `digamma_eq` proved, `archKernel` concrete, and the recurrence `digamma_add_one` (`ψ(s+1)=ψ(s)+1/s`) **PROVED** (no sorry) from `Complex.Gamma_add_one`. Remaining: the integral pairing (#EF-class). |
| #EF-class  | ExplicitFormula.lean          | The analytic side-conditions on `AdmissibleTest` (smoothness/decay/strip of holomorphy) that make the functionals well-defined and #EF-1 true. |
| #EF-K2     | ExplicitFormula.lean          | The D-H instance showing the criterion does NOT certify RH for Davenport-Heilbronn (prime side delocalises; experiment 3M #20). |

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
