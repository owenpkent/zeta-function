/-
Upstream-staging unit: the conjugation symmetry of the Riemann zeta function.

`riemannZeta (conj s) = conj (riemannZeta s)` (for `s ≠ 1`) is a standard fact ABSENT from Mathlib:
Mathlib carries the functional equation (`riemannZeta_one_sub`) but not this reflection symmetry. This
file is a Mathlib-style, PROJECT-DEPENDENCY-FREE verified unit (imports only Mathlib, top-level
namespace, `conj` notation), staged for upstreaming to
`Mathlib/NumberTheory/LSeries/RiemannZeta.lean`. PR body:
`lean/upstream/riemann_zeta_conj_pr_body.md`.

Proof idea: ζ has real Dirichlet coefficients, so on `Re s > 1` the L-series gives
`conj (ζ (conj s)) = ζ s` termwise; the identity principle for analytic functions then propagates
this across the connected domain `ℂ ∖ {1}`. Analyticity of `conj ∘ ζ ∘ conj` is the anti-holomorphic
composition `HasDerivAt.conj_conj`.
-/

import Mathlib.NumberTheory.LSeries.RiemannZeta
import Mathlib.Analysis.Calculus.Deriv.Star
import Mathlib.Analysis.Analytic.Uniqueness
import Mathlib.Analysis.Normed.Module.Connected

open Complex ComplexConjugate

/-- **Conjugation symmetry of the Riemann zeta function:** `ζ(s̄) = conj ζ(s)` for `s ≠ 1`.
    Since ζ has real Dirichlet coefficients, `conj (ζ (conj s)) = ζ s` holds termwise on `Re s > 1`,
    and the identity principle propagates it to the connected domain `ℂ ∖ {1}`. -/
theorem riemannZeta_conj {s : ℂ} (hs : s ≠ 1) :
    riemannZeta (conj s) = conj (riemannZeta s) := by
  -- `conj ∘ ζ ∘ conj` is analytic on `{1}ᶜ` (anti-holomorphic composition)
  have hg_diff : DifferentiableOn ℂ
      (fun z => conj (riemannZeta (conj z))) {1}ᶜ := by
    intro z hz
    have hzz : z ≠ 1 := hz
    have hcz : conj z ≠ 1 := fun h => hzz (by
      have := congrArg (starRingEnd ℂ) h
      rwa [Complex.conj_conj, map_one] at this)
    have hgd := ((differentiableAt_riemannZeta hcz).hasDerivAt).conj_conj
    rw [Complex.conj_conj] at hgd
    exact hgd.differentiableAt.differentiableWithinAt
  have hg_an : AnalyticOnNhd ℂ (fun z => conj (riemannZeta (conj z))) {1}ᶜ :=
    hg_diff.analyticOnNhd isOpen_compl_singleton
  -- `conj (ζ (conj z)) = ζ z` on `Re > 1`, termwise via the L-series
  have hgz : ∀ z : ℂ, 1 < z.re → conj (riemannZeta (conj z)) = riemannZeta z := by
    intro z hz1
    have hcz1 : 1 < (conj z).re := by rw [Complex.conj_re]; exact hz1
    have hterm : ∀ n : ℕ, conj (1 / (n : ℂ) ^ (conj z)) = 1 / (n : ℂ) ^ z := by
      intro n
      have harg : (n : ℂ).arg ≠ Real.pi := by
        rw [show (n : ℂ) = (((n : ℝ)) : ℂ) by push_cast; ring,
          Complex.arg_ofReal_of_nonneg (by positivity)]
        exact Real.pi_pos.ne
      have hpow : conj ((n : ℂ) ^ (conj z)) = (n : ℂ) ^ z := by
        have hcc := Complex.conj_cpow (n : ℂ) z harg
        rw [Complex.conj_natCast] at hcc
        exact hcc.symm
      rw [map_div₀, map_one, hpow]
    rw [zeta_eq_tsum_one_div_nat_cpow hcz1, Complex.conj_tsum,
      zeta_eq_tsum_one_div_nat_cpow hz1]
    exact tsum_congr hterm
  -- identity principle on the connected `{1}ᶜ`, anchored at `s = 2`
  have hfg : (fun z => conj (riemannZeta (conj z))) =ᶠ[nhds (2 : ℂ)] riemannZeta :=
    Filter.eventuallyEq_of_mem
      ((isOpen_lt continuous_const Complex.continuous_re).mem_nhds (by norm_num))
      (fun z hz => hgz z hz)
  have hU : IsPreconnected ({1}ᶜ : Set ℂ) :=
    (isConnected_compl_singleton_of_one_lt_rank
      (by rw [Complex.rank_real_complex]; norm_num) 1).isPreconnected
  have heq := hg_an.eqOn_of_preconnected_of_eventuallyEq analyticOn_riemannZeta hU
    (by norm_num : (2 : ℂ) ∈ ({1}ᶜ : Set ℂ)) hfg
  have key : conj (riemannZeta (conj s)) = riemannZeta s := heq hs
  have hkey := congrArg (starRingEnd ℂ) key
  rwa [Complex.conj_conj] at hkey

/-- The zeros of `riemannZeta` are symmetric under complex conjugation (away from the pole `s = 1`):
    `ζ(s̄) = 0 ↔ ζ(s) = 0`. -/
theorem riemannZeta_conj_eq_zero_iff {s : ℂ} (hs : s ≠ 1) :
    riemannZeta (conj s) = 0 ↔ riemannZeta s = 0 := by
  rw [riemannZeta_conj hs]; simp
