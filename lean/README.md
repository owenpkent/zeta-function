# Lean 4 / Mathlib formalization of the zeta function proof program

> Formal verification stack for the AI-only proof program. See [`docs/03_research/proof_program_ai_only.md`](../docs/03_research/proof_program_ai_only.md) §2.2 for context.
>
> **Goal**: every structural claim in the project (R3.5 no-shortcut theorem, 4E.3 line-restriction lemma, the eventual Hodge index theorem) is translated to Lean 4 and verified by Mathlib's kernel.

## Status

**Skeleton only as of 2026-05-25.** Project infrastructure is set up; theorem statements are placeholder `sorry` stubs. Substantial Mathlib expansion required before any theorem is provable.

## Structure

```
lean/
├── lakefile.lean           # Lake build configuration
├── lean-toolchain          # Lean version pin
├── ZetaRH.lean             # Main module: imports all sub-modules
└── ZetaRH/
    ├── Basic.lean          # Foundational definitions: L-functions, zeros, Selberg class
    ├── DavenportHeilbronn.lean   # The D-H L-function and its off-line zeros
    ├── R3_5.lean           # No-shortcut theorem: trace-formula NCG has P ⟺ RH
    ├── LineRestriction.lean # 4E.3 line-restriction lemma
    ├── LambdaBlueprints.lean    # Direction 1: Lambda-blueprint framework
    ├── PrismaticCohomology.lean # Direction 3: prismatic cohomology of W(Z)
    ├── PrismaticFoliation.lean  # Direction 4: prismatic foliation hypothesis M3
    ├── HodgeIndex.lean     # Direction 8: the central open problem
    └── KillCriteria.lean   # K1-K4 formalizations
```

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

## How agents use this

- **BUILDER**: writes mathematical definitions in `ZetaRH/`.
- **VERIFIER**: translates BUILDER definitions into Lean and proves theorems. Marks `sorry` stubs for un-proved claims with explicit follow-up tasks.
- **ADVERSARY**: writes Lean-formalized counterexamples or attacks proposed theorems.
- **SYNTHESIZER**: maintains this README and the cross-references to the rest of the project.

## Cross-references

- [`../docs/03_research/proof_program.md`](../docs/03_research/proof_program.md): AI-augmented variant of the proof program.
- [`../docs/03_research/proof_program_ai_only.md`](../docs/03_research/proof_program_ai_only.md): AI-only variant.
- [`../docs/03_research/research_directions/`](../docs/03_research/research_directions/): the eight research directions.
- [`../experiments/PROOF_ARCHITECTURES_PLAN.md`](../experiments/PROOF_ARCHITECTURES_PLAN.md): the test plan.
- [`../experiments/LEARNINGS.md`](../experiments/LEARNINGS.md): cross-architecture findings.
