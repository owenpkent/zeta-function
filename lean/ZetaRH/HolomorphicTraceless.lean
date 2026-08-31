/-
The #196 nugget (e2bb_eta_second_variation.md, Hand-off (i)): "if rho(w) is
holomorphic and nonreal, then w |-> f(Im rho(w)) has traceless Hessian up to
f''-terms; its corollary is the conductor-independence of the (1,1) forcing."

Pricing. The mathematical content is the two-dimensional chain rule
  Delta (f o u) = f''(u) |grad u|^2 + f'(u) Delta u
specialized to u = Im rho with rho holomorphic, where Delta u = 0 (a
Cauchy-Riemann consequence), so the f'-term vanishes identically and the
Hessian trace is PURE f''-term with weight |rho'(w)|^2.

  #HT-1  One-variable second derivative of a composition (finite, proved
         outright): if g has derivative function g' with g' differentiable at
         x0 and f has derivative function f' with f' differentiable at g x0,
         then (f o g)'' (x0) = f''(g x0) g'(x0)^2 + f'(g x0) g''(x0). Pure
         chain + product rule.

  #HT-2  The KERNEL (rung 1, the target of record): the trace of the Hessian
         of f o u along the two axis slices equals
         f''(u p) (u_x^2 + u_y^2) + f'(u p) (u_xx + u_yy).
         All derivative structure is carried as named HasDerivAt hypotheses
         in the honest KERNEL style (#S4C-2): the slice first derivatives
         u_x, u_y along the two axis lines, the slice second derivatives at
         the point, and the pointwise f'/f'' chain. Finite content, no
         complex analysis consumed.

  #HT-3  The harmonic corollary of #HT-2: if u_xx + u_yy = 0 at the point
         (the CR input "Im of holomorphic is harmonic", carried as the named
         hypothesis `harm`; in-print source: any complex analysis text),
         the trace is the pure f''-term f''(u p) (u_x^2 + u_y^2). This is
         the dossier's "traceless up to f''-terms" statement.

  #HT-4  Mathlib-gap twin of `HasDerivAt.real_of_complex`: the imaginary
         part of a complex-differentiable function restricted to a real
         parameter is differentiable with derivative the imaginary part of
         the complex derivative. Small upstream candidate (Mathlib at the
         v4.30.0 pin carries only the `.re` version).

  #HT-5  Rung 2, DISCHARGED: for rho entire with derivative function rho'
         (hypothesis `hrho`) and rho' differentiable at w (hypothesis
         `hrhod`), the harmonicity of Im rho is DERIVED from the
         Cauchy-Riemann slicing (u_xx = Im rho'', u_yy = -Im rho''), and
         the Hessian trace of f(Im rho) at w equals f''(Im rho w) |rho'(w)|^2
         (as `Complex.normSq (rhod w)`). No harmonic-function API needed:
         the cancellation is exhibited directly. The dossier's "nonreal"
         hypothesis is subsumed: f carries its own differentiability
         hypotheses, so the nonreality of rho (which in the dossier only
         protects f = |.| from its corner at 0) is not needed here.

Corollary held as a comment, not forced (per the round spec): the
conductor-independence of the (1,1) forcing. Because #HT-5's conclusion
depends on the conductor only through the point values rho'(w), f'(Im rho w),
f''(Im rho w), the traceless-up-to-f''-terms structure of the eta-Hessian is
the same at every conductor: harmonicity balances the signature for the same
reason everywhere, which is e2bb's measured (1,1) forcing at q = 5 and q = 7.

Axiom footprint target: [propext, Classical.choice, Quot.sound].
-/

import Mathlib.Analysis.Complex.RealDeriv
import Mathlib.Analysis.Calculus.Deriv.Add
import Mathlib.Analysis.Calculus.Deriv.Comp
import Mathlib.Analysis.Calculus.Deriv.Mul

namespace ZetaRH.HolomorphicTraceless

/-! ## #HT-1: second derivative of a one-variable composition -/

/-- **#HT-1.** One-variable second derivative of a composition, in
    deriv-of-deriv form. `g'` is the derivative function of `g` everywhere
    (so the first derivative of `f o g` is a known function, not just a
    point value), `g''p` is the derivative of `g'` at `x0`, `f'` is the
    derivative function of `f`, and `f''p` is the derivative of `f'` at
    `g x0`. Chain rule twice plus the product rule. -/
theorem secondDeriv_comp (f f' g g' : ℝ → ℝ) (f''p g''p x0 : ℝ)
    (hg : ∀ x, HasDerivAt g (g' x) x)
    (hg' : HasDerivAt g' g''p x0)
    (hf : ∀ t, HasDerivAt f (f' t) t)
    (hf' : HasDerivAt f' f''p (g x0)) :
    deriv (deriv (fun x => f (g x))) x0 = f''p * g' x0 ^ 2 + f' (g x0) * g''p := by
  -- the first derivative of the composition is the function f'(g x) * g'(x)
  have hd1 : deriv (fun x => f (g x)) = fun x => f' (g x) * g' x :=
    funext fun x => ((hf (g x)).comp x (hg x)).deriv
  rw [hd1]
  -- differentiate the product f'(g x) * g'(x) at x0
  have h1 : HasDerivAt (fun x => f' (g x)) (f''p * g' x0) x0 := hf'.comp x0 (hg x0)
  have h2 : HasDerivAt (fun x => f' (g x) * g' x)
      (f''p * g' x0 * g' x0 + f' (g x0) * g''p) x0 := h1.mul hg'
  rw [h2.deriv]
  ring

/-! ## #HT-2: the trace of the Hessian along axis slices (the KERNEL) -/

/-- **#HT-2 (KERNEL, rung 1).** The general trace identity. `u` is the scalar
    field, `ux`/`uy` its slice derivative functions along the horizontal line
    through `(x0, y0)` and the vertical line through `(x0, y0)` (hypotheses
    `hux`, `huy`), `uxx`/`uyy` the slice second derivatives at the point
    (hypotheses `huxx`, `huyy`), and `f'`/`f''p` the chain data for `f`
    (hypotheses `hf`, `hf'`). Then
    `(f o u)_xx + (f o u)_yy = f''(u p) (u_x^2 + u_y^2) + f'(u p) (u_xx + u_yy)`.
    Everything here is finite one-variable calculus; no harmonicity is
    consumed yet. -/
theorem trace_hessian_general (u ux uy : ℝ → ℝ → ℝ) (f f' : ℝ → ℝ)
    (x0 y0 uxx uyy f''p : ℝ)
    (hux : ∀ x, HasDerivAt (fun s => u s y0) (ux x y0) x)
    (huy : ∀ y, HasDerivAt (fun s => u x0 s) (uy x0 y) y)
    (huxx : HasDerivAt (fun s => ux s y0) uxx x0)
    (huyy : HasDerivAt (fun s => uy x0 s) uyy y0)
    (hf : ∀ t, HasDerivAt f (f' t) t)
    (hf' : HasDerivAt f' f''p (u x0 y0)) :
    deriv (deriv (fun x => f (u x y0))) x0 + deriv (deriv (fun y => f (u x0 y))) y0
      = f''p * (ux x0 y0 ^ 2 + uy x0 y0 ^ 2) + f' (u x0 y0) * (uxx + uyy) := by
  have hxx := secondDeriv_comp f f' (fun s => u s y0) (fun s => ux s y0)
    f''p uxx x0 hux huxx hf hf'
  have hyy := secondDeriv_comp f f' (fun s => u x0 s) (fun s => uy x0 s)
    f''p uyy y0 huy huyy hf hf'
  rw [hxx, hyy]
  ring

/-- **#HT-3 (the dossier's lemma).** Under the harmonicity input
    `u_xx + u_yy = 0` at the point (the Cauchy-Riemann consequence "Im of a
    holomorphic function is harmonic", carried as the named hypothesis
    `harm`; discharged from holomorphy in #HT-5), the Hessian trace of
    `f o u` is the PURE f''-term: the f'-term vanishes identically. This is
    "traceless Hessian up to f''-terms". -/
theorem trace_hessian_of_harmonic (u ux uy : ℝ → ℝ → ℝ) (f f' : ℝ → ℝ)
    (x0 y0 uxx uyy f''p : ℝ)
    (hux : ∀ x, HasDerivAt (fun s => u s y0) (ux x y0) x)
    (huy : ∀ y, HasDerivAt (fun s => u x0 s) (uy x0 y) y)
    (huxx : HasDerivAt (fun s => ux s y0) uxx x0)
    (huyy : HasDerivAt (fun s => uy x0 s) uyy y0)
    (hf : ∀ t, HasDerivAt f (f' t) t)
    (hf' : HasDerivAt f' f''p (u x0 y0))
    (harm : uxx + uyy = 0) :
    deriv (deriv (fun x => f (u x y0))) x0 + deriv (deriv (fun y => f (u x0 y))) y0
      = f''p * (ux x0 y0 ^ 2 + uy x0 y0 ^ 2) := by
  rw [trace_hessian_general u ux uy f f' x0 y0 uxx uyy f''p hux huy huxx huyy hf hf',
    harm, mul_zero, add_zero]

/-! ## #HT-4: the imaginary-part twin of `HasDerivAt.real_of_complex` -/

/-- **#HT-4 (Mathlib-gap twin, upstream candidate).** If a complex function
    `e` is differentiable at a real point, the real function `x ↦ (e x).im`
    is differentiable there with derivative `e'.im`. Mathlib at the pin has
    only the `.re` version (`HasDerivAt.real_of_complex`); the proof is the
    same composition through `Complex.imCLM`. -/
theorem hasDerivAt_im_of_complex {e : ℂ → ℂ} {e' : ℂ} {z : ℝ}
    (h : HasDerivAt e e' ↑z) :
    HasDerivAt (fun x : ℝ => (e ↑x).im) e'.im z := by
  have A : HasFDerivAt ((↑) : ℝ → ℂ) Complex.ofRealCLM z := Complex.ofRealCLM.hasFDerivAt
  have B : HasFDerivAt e
      ((ContinuousLinearMap.smulRight (1 : ℂ →L[ℂ] ℂ) e').restrictScalars ℝ)
      (Complex.ofRealCLM z) := h.hasFDerivAt.restrictScalars ℝ
  have C : HasFDerivAt Complex.im Complex.imCLM (e (Complex.ofRealCLM z)) :=
    Complex.imCLM.hasFDerivAt
  simpa using (C.comp z (B.comp z A)).hasDerivAt

/-! ## #HT-5: rung 2, harmonicity discharged from holomorphy -/

/-- **#HT-5 (rung 2, the dossier's nugget in full).** Let `ρ` be entire with
    derivative function `ρd` (hypothesis `hρ`) and let `ρd` be differentiable
    at `w` with derivative `ρdd` (hypothesis `hρd`); let `f` have derivative
    function `f'` (hypothesis `hf`) with `f'` differentiable at `Im ρ(w)`
    (hypothesis `hf'`). Then the Hessian trace of `w ↦ f(Im ρ(w))` along the
    two axis slices through `w` is the pure f''-term
    `f'' (Im ρ w) * |ρ'(w)|²`. The harmonicity of `Im ρ` is DERIVED here:
    slicing the Cauchy-Riemann structure gives `u_xx = Im ρ''(w)` and
    `u_yy = (ρ''(w)·i).re = -Im ρ''(w)`, which cancel. Only the pointwise
    smoothness of `f` rides as hypotheses; the dossier's "nonreal" clause
    (which protects `f = |·|` from its corner at `0`) is subsumed by them. -/
theorem holomorphic_im_traceless (ρ ρd : ℂ → ℂ) (ρdd w : ℂ) (f f' : ℝ → ℝ) (f''p : ℝ)
    (hρ : ∀ z, HasDerivAt ρ (ρd z) z)
    (hρd : HasDerivAt ρd ρdd w)
    (hf : ∀ t, HasDerivAt f (f' t) t)
    (hf' : HasDerivAt f' f''p ((ρ w).im)) :
    deriv (deriv (fun x : ℝ => f ((ρ ((x : ℂ) + (w.im : ℂ) * Complex.I)).im))) w.re
      + deriv (deriv (fun y : ℝ => f ((ρ ((w.re : ℂ) + (y : ℂ) * Complex.I)).im))) w.im
      = f''p * Complex.normSq (ρd w) := by
  -- x-slice of ρ through w: complex derivative along the horizontal line
  have hxE : ∀ x : ℝ, HasDerivAt (fun z : ℂ => ρ (z + (w.im : ℂ) * Complex.I))
      (ρd ((x : ℂ) + (w.im : ℂ) * Complex.I)) (x : ℂ) := by
    intro x
    have hin : HasDerivAt (fun z : ℂ => z + (w.im : ℂ) * Complex.I) 1 (x : ℂ) :=
      (hasDerivAt_id _).add_const _
    simpa using (hρ ((x : ℂ) + (w.im : ℂ) * Complex.I)).comp (x : ℂ) hin
  have hux : ∀ x : ℝ, HasDerivAt (fun s : ℝ => (ρ ((s : ℂ) + (w.im : ℂ) * Complex.I)).im)
      ((ρd ((x : ℂ) + (w.im : ℂ) * Complex.I)).im) x :=
    fun x => hasDerivAt_im_of_complex (hxE x)
  -- y-slice of ρ through w: complex derivative along the vertical line
  have hyE : ∀ y : ℝ, HasDerivAt (fun z : ℂ => ρ ((w.re : ℂ) + z * Complex.I))
      (ρd ((w.re : ℂ) + (y : ℂ) * Complex.I) * Complex.I) (y : ℂ) := by
    intro y
    have hin : HasDerivAt (fun z : ℂ => (w.re : ℂ) + z * Complex.I) Complex.I (y : ℂ) := by
      simpa using ((hasDerivAt_id ((y : ℂ))).mul_const Complex.I).const_add ((w.re : ℂ))
    simpa using (hρ ((w.re : ℂ) + (y : ℂ) * Complex.I)).comp (y : ℂ) hin
  -- Cauchy-Riemann along the vertical slice: d/dy Im ρ = Re ρ'
  have huy : ∀ y : ℝ, HasDerivAt (fun s : ℝ => (ρ ((w.re : ℂ) + (s : ℂ) * Complex.I)).im)
      ((ρd ((w.re : ℂ) + (y : ℂ) * Complex.I)).re) y := by
    intro y
    have h := hasDerivAt_im_of_complex (hyE y)
    rwa [Complex.mul_I_im] at h
  -- second derivatives at the point: slice ρd the same way
  have hρd' : HasDerivAt ρd ρdd ((w.re : ℂ) + (w.im : ℂ) * Complex.I) := by
    rwa [Complex.re_add_im]
  have huxxE : HasDerivAt (fun z : ℂ => ρd (z + (w.im : ℂ) * Complex.I)) ρdd (w.re : ℂ) := by
    have hin : HasDerivAt (fun z : ℂ => z + (w.im : ℂ) * Complex.I) 1 (w.re : ℂ) :=
      (hasDerivAt_id _).add_const _
    simpa using hρd'.comp ((w.re : ℂ)) hin
  have huxx : HasDerivAt (fun s : ℝ => (ρd ((s : ℂ) + (w.im : ℂ) * Complex.I)).im)
      ρdd.im w.re := hasDerivAt_im_of_complex huxxE
  have huyyE : HasDerivAt (fun z : ℂ => ρd ((w.re : ℂ) + z * Complex.I))
      (ρdd * Complex.I) (w.im : ℂ) := by
    have hin : HasDerivAt (fun z : ℂ => (w.re : ℂ) + z * Complex.I) Complex.I (w.im : ℂ) := by
      simpa using ((hasDerivAt_id ((w.im : ℂ))).mul_const Complex.I).const_add ((w.re : ℂ))
    simpa using hρd'.comp ((w.im : ℂ)) hin
  -- Cauchy-Riemann cancellation: u_yy = Re (ρ'' i) = -Im ρ''
  have huyy : HasDerivAt (fun s : ℝ => (ρd ((w.re : ℂ) + (s : ℂ) * Complex.I)).re)
      (-ρdd.im) w.im := by
    have h := huyyE.real_of_complex
    rwa [Complex.mul_I_re] at h
  -- chain data at the point, rewritten to the sliced coordinates
  have hf'' : HasDerivAt f' f''p ((ρ ((w.re : ℂ) + (w.im : ℂ) * Complex.I)).im) := by
    rwa [Complex.re_add_im]
  -- assemble via the harmonic kernel #HT-3; harmonicity is now a theorem
  have hker := trace_hessian_of_harmonic
    (fun a b : ℝ => (ρ ((a : ℂ) + (b : ℂ) * Complex.I)).im)
    (fun a b : ℝ => (ρd ((a : ℂ) + (b : ℂ) * Complex.I)).im)
    (fun a b : ℝ => (ρd ((a : ℂ) + (b : ℂ) * Complex.I)).re)
    f f' w.re w.im ρdd.im (-ρdd.im) f''p hux huy huxx huyy hf hf'' (by ring)
  -- beta-reduce the instantiated slice lambdas so the point rewrite can fire
  simp only [] at hker
  rw [Complex.re_add_im] at hker
  have h2 : f''p * ((ρd w).im ^ 2 + (ρd w).re ^ 2) = f''p * Complex.normSq (ρd w) := by
    rw [Complex.normSq_apply]
    ring
  exact hker.trans h2

end ZetaRH.HolomorphicTraceless
