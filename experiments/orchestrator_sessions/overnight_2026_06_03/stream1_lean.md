# Stream 1 (Lean, self-verifying) — overnight 2026-06-03

> VERIFIER. The Lean build is the verifier, so this stream's output is the one
> kind of overnight progress that is real without main-agent re-derivation. All
> sorry-free lemmas below were checked by Lean's kernel and depend ONLY on the
> standard Mathlib axioms (`propext`, `Classical.choice`, `Quot.sound`); no
> `sorryAx`, no custom `axiom`.

## Toolchain status — OK

- `elan 4.2.1`, `Lake 5.0.0-6d22e0e`, `Lean 4.13.0` (`x86_64-w64-windows-gnu`).
- Mathlib pinned at `v4.13.0` (`lean/lakefile.lean`).
- `cd lean && lake build` BEFORE any change: **GREEN** ("Build completed
  successfully"), warnings are exactly the pre-existing documented `sorry`
  markers (MathlibBridge, DavenportHeilbronn, LineRestriction, LambdaBlueprints,
  PrismaticCohomology, PrismaticFoliation, HodgeIndex, ExplicitFormula).
- `lake build` AFTER adding the new file: **GREEN**. New file is picked up
  automatically by the `lean_lib ZetaRH` glob (no edit to `ZetaRH.lean` or any
  existing module was needed; the existing modules were NOT touched).

## What was produced

New file (only file added/changed this stream):
`lean/ZetaRH/OvernightDrafts2026_06_03.lean`, namespace `ZetaRH.OvernightDrafts`.

It formalizes two of this session's verified facts: the de Branges / Conrey-Li
per-zero cross-term (target (b), #43 / experiment 2DB.1) and the Lerch
regularized-determinant identity (target (a), #44 / experiment 2PR.1).

### Sorry-free, kernel-checked (6 lemmas)

These are real verification, not scaffolding.

1. `xiCL (s) := s * (s - 1) * completedRiemannZeta s` — Conrey-Li completed
   zeta (the entire `s(s-1)`-normalization; `Λ` is Mathlib's
   `completedRiemannZeta = π^{-s/2} Γ(s/2) ζ(s)`).

2. `xiCL_one_sub : xiCL (1 - s) = xiCL s`. The functional equation of `ξ`,
   proved from Mathlib's `completedRiemannZeta_one_sub` plus
   `(1-s)((1-s)-1) = s(s-1)`. In the de Branges picture this symmetry IS the
   Hermite-Biehler symmetry (the would-be Poincaré duality).

3. `deriv_xiCL_one_sub : deriv xiCL (1 - s) = -deriv xiCL s`. The derivative
   antisymmetry, proved by differentiating (2) through Mathlib's
   `deriv_comp_const_sub`. This is the structural reason the cross-term `Q`
   couples a zero `ρ` to its functional-equation partner `1-ρ`.

4. `completedRiemannZeta_eq_Gammaℝ_mul : 0 < s.re → Λ s = Γ_ℝ(s) · ζ(s)`.
   The factorization away from the `Γ_ℝ` zeros, from `riemannZeta_def_of_ne_zero`
   and `Gammaℝ_ne_zero_of_re_pos`.

5. `xiCL_eq_zero_of_zeta_zero : ζ ρ = 0 → 0 < ρ.re → xiCL ρ = 0`. `ξ` vanishes
   at every nontrivial zeta zero — the precise sense in which the de Branges
   pairing "reaches the zeros" (the converse of #42's local-data blindness).

6. `lerchRHS (s) := √(2π) / Γ(s)` — the closed form Lerch's regularized product
   equals — with:
   - `lerchRHS_one : lerchRHS 1 = √(2π)` (the experiment's `ratio = 1.000`
     anchor at `s = 1`, since `Γ(1) = 1`);
   - `lerchRHS_ne_zero_of_re_pos : 0 < s.re → lerchRHS s ≠ 0` — the **blindness**
     fact of #44, qualitatively: the Sen/Lerch archimedean determinant's closed
     form is NONZERO at every nontrivial zero (`0 < Re ρ`). The non-trivial
     zeros live in the `ζ` factor, never in this Γ-factor. (The experiment's
     `|det| ≈ 4.4e9 ≠ 0` is the quantitative version; Lean proves the
     qualitative `≠ 0`.)

### Definitions + tracked targets (`sorry`, honestly flagged)

- `deBrangesQ (ρ) := -Re{ξ'(ρ) · ξ(1+ρ)}` — the cross-term `Q` (concrete def,
  no sorry in the definition itself).
- `Is34thZetaZero` — a hypothesis bundle for `ρ₃₄` carrying `ζ ρ = 0`,
  `Re ρ = 1/2` (the ordinate is transcendental, kept symbolic, not a decimal).
- `#2DB-1` `deBrangesQ_neg_at_34`: `Q(ρ₃₄) < 0`. NUMERICAL target. Conrey-Li
  `-5.389…e-69`, reproduced to 12 sig figs in 2DB.1. Blocked: no Mathlib
  certified-numeric evaluation of `ζ'`, `ζ`, `Γ` at a transcendental ordinate.
- `#2DB-2` `deBranges_implies_RH`: de Branges pointwise positivity ⇒ RH
  (Conrey-Li IMRN 2000 (3.1)). A real theorem; blocked on de Branges `H(E)`
  reproducing-kernel theory (absent from Mathlib). The CONVERSE fails — that is
  #43's whole content, witnessed by `#2DB-1`.
- `#2PR-1` `senRegDet_exists`: existence of the zeta-regularized product
  `∏^{reg}_{n≥0}(s+n)` with value `√(2π)/Γ(s)` (Lerch). Blocked: Mathlib has NO
  zeta-regularized product (it would be built from `∂_w Hurwitz-ζ(w,s)|_{w=0}`).

## Axiom audit (`#print axioms`)

- All six sorry-free lemmas: `[propext, Classical.choice, Quot.sound]` only.
- All three targets: `[propext, sorryAx, Classical.choice, Quot.sound]` — i.e.
  the `sorry` is real and the targets are honestly NOT proved.

## What this proves / what remains

PROVED (Lean kernel, this stream):
- The Conrey-Li `ξ`'s functional equation and its derivative's antisymmetry.
- That `ξ` vanishes at the nontrivial zeta zeros (the de Branges pairing reaches
  the zeros) — the formal half of the #42/#43 converse.
- That the Lerch/Sen archimedean closed form `√(2π)/Γ(s)` is nonzero at the
  zeros (the formal "blindness" of #44) and equals `√(2π)` at `s=1`.

These are the structural, RH-agnostic facts the experiments call out: they are
exactly the TRACE side. Consistent with "all roads to the signature" (#30), none
of them touches the SIGNATURE.

REMAINS (the targets, in order of tractability for a future Lean pass):
1. `#2DB-2` (de Branges ⇒ RH) — large; needs an `H(E)` theory. Long horizon.
2. `#2PR-1` (Lerch regularized product) — a clean, self-contained Mathlib
   contribution: define `∏^{reg}` via the Hurwitz-zeta `s`-derivative at `0` and
   prove the Lerch value. Likely the best standalone upstreamable target.
3. `#2DB-1` (`Q(ρ₃₄) < 0`) — needs certified interval numerics for `ζ` at a
   specific ordinate; not feasible in Mathlib today.

Recommended next Lean step: attack `#2PR-1` by first defining the zeta-regularized
product `∏^{reg}_{n≥0}(s+n) := exp(-∂_w [∑_n (s+n)^{-w}]|_{w=0})` against
Mathlib's Hurwitz zeta `hurwitzZeta`, then proving `∂_w ζ_H(w,s)|_{w=0}` via the
Lerch formula. This converts `senRegDet_exists` from a target into a real proof
and is genuinely upstreamable. Secondary: strengthen the de Branges scaffold by
proving `Q(ρ) = Q(1-ρ)`-type symmetries from `deriv_xiCL_one_sub` + `xiCL_one_sub`
(more sorry-free structure without needing numerics).

Honesty note: nothing here advances RH. The six new lemmas are the trace/realization
side (functional equation, vanishing-at-zeros, Γ-factor nonvanishing); the signature
(the positivity that would close RH) is not engaged, exactly as the experiments record.
The value of this stream is that these specific facts are now machine-checked rather
than asserted.
