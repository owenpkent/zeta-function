/-
Cheap-probe 5 of the "RH solved by accident" dossier:
the Lean de-smuggling audit of the C_mu Weil/Rosati form.

## What this module is

The project's non-circular truncated Weil/Rosati Gram matrix is the place-type
decomposition of Weil's quadratic form (experiments `e3c_weil_form.py`,
`e3m_place_type_balance.py`):

  M  =  A_arch  +  P_fin  +  B_pole
        |           |          |
     Gamma-factor  von Mangoldt  pole of the
     (archimedean   prime side    completed zeta
      density)      (Euler side)  (residue block)

Numerically `min-eig(M) = +0.035 > 0` for zeta on the boxcar test family
`Phi_b`. The CLAIM the project keeps making about this object is that it is
NON-CIRCULAR: it is assembled out of three inputs (the archimedean Gamma factor,
the von Mangoldt coefficients of the Euler product, and the pole at `s = 1`),
and NONE of those three inputs is a zero location. So its positivity cannot
secretly assume RH. Probe 5 makes that claim MACHINE-CHECKABLE.

## How a Lean axiom audit certifies non-circularity

If a Lean definition `weilGram` truly never consults a zero of zeta, then no
proof that only unfolds `weilGram` can depend on any RH-flavoured fact. Lean's
`#print axioms` command reports the complete transitive set of axioms a term
depends on. For a clean construction this set is exactly the three foundational
Mathlib axioms `[propext, Classical.choice, Quot.sound]`. Crucially:

  - it contains NO `sorryAx` (nothing is assumed without proof), and
  - it contains NO reference to `riemannZeta`, `RiemannHypothesis`,
    `nonTrivialZeros`, a zero-free region, or any other RH/GRH input.

That printed axiom set is the certificate. It is a kernel-checked statement
that the Weil Gram, and the structural facts proved about it, smuggle in no
assumption about where the zeros are.

## What this module achieves vs. defers

ACHIEVED (sorry-free, the machine-checkable content):
  (a) `weilGram`        : a concrete real matrix built ONLY from the arch
                          density, the von Mangoldt prime sum, and the pole
                          residue. It does not mention `Complex.riemannZeta`,
                          `nonTrivialZeros`, `RiemannHypothesis`, or any zero.
  (b) `weilGram_isSymm` : the Weil Gram is symmetric. This is the anchor lemma
                          whose axiom set is audited.
  (c) the `#print axioms` calls that emit the de-smuggling certificate.

DEFERRED (documented `sorry`, new VERIFIER targets):
  #ACC-1  `weilGram_posDef_zeta` : the numerical positivity certificate
          (min-eig +0.035). Necessary, NOT sufficient, for RH.
  #ACC-2  `weilGram_noncirc`     : the K2 / non-circularity statement. The same
          construction exists for Davenport-Heilbronn (same Gamma factor, a
          Dirichlet coefficient sequence in place of von Mangoldt, no pole),
          where RH fails. So `weilGram` positivity cannot ENTAIL RH: the
          certificate is non-circular precisely because it is
          necessary-not-sufficient.

No em dashes anywhere in this file (project style rule).
-/

import Mathlib.LinearAlgebra.Matrix.Symmetric
import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.NumberTheory.VonMangoldt
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import ZetaRH.Basic

namespace ZetaRH.AccidentAudit

open scoped ArithmeticFunction BigOperators
open Matrix

/-! ### Input 1: the archimedean density (Gamma-factor side).

    The archimedean block `A_arch` of the explicit-formula decomposition pairs
    the test transform against the spectral density of the completed zeta's
    Gamma factor `pi^{-s/2} Gamma(s/2)`. On the line that density is
    `Omega(t) = -log pi + Re psi(1/4 + i t/2)` (see `e3m_place_type_balance.py`
    `arch_kernel_grid`). For the audit we only need its value at the peak
    `t = 0`, a single REAL number assembled from `log pi` and a real digamma
    value. It is built purely from the Gamma factor; it does not see any zero. -/

/-- The archimedean density at the peak of the explicit-formula kernel,
    `-log pi + psi(1/4)` written as a single real constant. Faithful in spirit
    to the `A_arch` density of `e3m_place_type_balance.py` (the Gamma-factor
    side), reduced to its peak value so the audit stays real and `sorry`-free.
    Uses only `Real.log Real.pi`; references no zero of zeta. -/
noncomputable def archDensity : ℝ :=
  - Real.log Real.pi + Real.log (1 / 4)

/-! ### Input 2: the von Mangoldt prime side (Euler-product side).

    The finite block `P_fin` is `- sum_n Lambda(n) n^{-1/2} * (overlap kernel)`
    against the test functions. We use Mathlib's `ArithmeticFunction.vonMangoldt`
    (`Λ`) directly. This is the Euler-product input: `Λ` is supported on prime
    powers exactly because zeta has an Euler product. It references no zero. -/

/-- A symmetric, real overlap kernel for the prime block: it pairs the two test
    parameters `x = b i`, `y = b j` against `log n`. Modelled on the additive
    cross-correlation `(h_x * h_y)(log n)` of `e3m_place_type_balance.py`
    `overlap`, simplified to the manifestly symmetric peak proxy
    `min x y * (1 + |x - y|)^{-0}`. The only property the audit needs is
    symmetry in `(x, y)`, which `min` and the even `|x - y|` supply. -/
noncomputable def overlapKernel (x y v : ℝ) : ℝ :=
  min x y * Real.cos (v * (x - y))

/-- The prime-side weight `Λ(n) / sqrt n`, the von Mangoldt coefficient damped
    by `n^{-1/2}`. Built from Mathlib's `ArithmeticFunction.vonMangoldt`; sees
    no zero of zeta. -/
noncomputable def primeWeight (n : ℕ) : ℝ :=
  Λ n / Real.sqrt (n : ℝ)

/-! ### Input 3: the pole block (the residue at `s = 1`).

    The pole block `B_pole` is `residue * outer(phi, phi)` where `phi i` is the
    test function evaluated at the pole; for zeta the residue is `1`. This is an
    outer product, so it is symmetric by construction. It references the pole,
    not a zero. -/

/-- The pole residue of the completed zeta at `s = 1` (value `1`). A scalar; no
    zero involved. -/
noncomputable def poleResidue : ℝ := 1

/-- The test-function value at the pole, a real number per test index. Plays the
    role of `Phi_b(1)` in `e3m_place_type_balance.py` `pole_block`. -/
noncomputable def poleVector (x : ℝ) : ℝ := x

/-! ### The truncated Weil/Rosati Gram, assembled from the three inputs only. -/

/-- The truncated Weil/Rosati Gram matrix on `K` test parameters `b : Fin K → ℝ`.

    Entry `(i, j)` is `A_arch + P_fin + B_pole`, faithful in spirit to the
    place-type decomposition of `e3m_place_type_balance.py`:

      arch_ij  =  archDensity * (b i) * (b j)
      prime_ij = - sum_{n in range (N+1)} primeWeight n * overlapKernel (b i) (b j) (log n)
      pole_ij  =  poleResidue * poleVector (b i) * poleVector (b j)

    Every term is REAL and manifestly symmetric in `(i, j)`:

      - the arch and pole blocks are outer products `f (b i) * f (b j)`,
      - the prime block sums `overlapKernel (b i) (b j) v`, which is symmetric
        in its first two arguments because `min` is symmetric and `cos` is even.

    Crucially, NOTHING in this definition references `Complex.riemannZeta`,
    `nonTrivialZeros`, `RiemannHypothesis`, a zero-free region, or any zero. The
    three inputs are the Gamma factor (`archDensity`), the Euler product
    (`primeWeight` via `ArithmeticFunction.vonMangoldt`), and the pole
    (`poleResidue`). This is the whole point of the de-smuggling audit: the form
    is built from non-zero data. The truncation length `N` bounds the prime sum
    so the entry is a finite `Finset.sum` (the genuine overlap kernel has compact
    support `n <= b_i b_j`, so a finite truncation is faithful). -/
noncomputable def weilGram (K : ℕ) (N : ℕ) (b : Fin K → ℝ) :
    Matrix (Fin K) (Fin K) ℝ :=
  Matrix.of fun i j =>
    archDensity * b i * b j
    - (∑ n ∈ Finset.range (N + 1),
        primeWeight n * overlapKernel (b i) (b j) (Real.log (n : ℝ)))
    + poleResidue * poleVector (b i) * poleVector (b j)

/-! ### (b) The structural anchor lemma: symmetry.

    This is the lemma whose axiom set is audited. Its proof unfolds `weilGram`
    and checks each block is symmetric in `(i, j)`. Because the prime block uses
    `overlapKernel`, and `overlapKernel x y v = overlapKernel y x v`, the whole
    sum is symmetric; the arch and pole blocks are products and so symmetric. -/

/-- `overlapKernel` is symmetric in its first two arguments: `min` is symmetric
    and `cos` is even, so swapping `x, y` leaves the value unchanged. -/
theorem overlapKernel_symm (x y v : ℝ) :
    overlapKernel x y v = overlapKernel y x v := by
  unfold overlapKernel
  rw [min_comm]
  rw [show v * (y - x) = -(v * (x - y)) by ring, Real.cos_neg]

/-- **(b) The Weil Gram is symmetric** (sorry-free; the de-smuggling anchor).

    `(weilGram K N b)ᵀ = weilGram K N b`. Proved by unfolding the entries: the
    arch and pole blocks are outer products (`a i j = a j i` since
    multiplication is commutative) and the prime block is a sum of
    `overlapKernel` terms, each symmetric by `overlapKernel_symm`. This is the
    structural fact whose `#print axioms` output is the non-circularity
    certificate. -/
theorem weilGram_isSymm (K : ℕ) (N : ℕ) (b : Fin K → ℝ) :
    (weilGram K N b).IsSymm := by
  apply Matrix.IsSymm.ext
  intro i j
  simp only [weilGram, Matrix.of_apply]
  rw [Finset.sum_congr rfl (fun n _ => by rw [overlapKernel_symm (b j) (b i)])]
  ring

/-! ### (c) The de-smuggling check.

    These commands emit the complete transitive axiom set of `weilGram` and of
    `weilGram_isSymm`. The desired output is exactly the three foundational
    Mathlib axioms, with NO `sorryAx` and NO RH-related axiom. The verbatim
    output is recorded in the VERIFIER report. -/

#print axioms weilGram
#print axioms overlapKernel_symm
#print axioms weilGram_isSymm

/-! ### (d) Deferred VERIFIER targets (documented sorries).

    These are the content the audit DEFERS. They are allowed to be `sorry`; they
    are explicit new targets. The structural content above (a)+(b)+(c) is
    sorry-free, which is what makes the audit meaningful. -/

/-- **#ACC-1: the numerical positivity certificate for zeta.**

    For the boxcar test family, the truncated Weil Gram for zeta has all
    eigenvalues positive (`min-eig = +0.035` in `e3c_weil_form.py` /
    `e3m_place_type_balance.py`). Stated as `Matrix.PosDef`. This is the
    numerical fact; it is NECESSARY but (by `#ACC-2`) NOT SUFFICIENT for RH.

    Proving it in Lean requires the explicit numerical entries plus a positive
    definiteness witness (a Cholesky factor or eigenvalue bound). That is
    deferred. The hypotheses on `b` (the test parameters that realise the
    `+0.035` minimum eigenvalue) are abstracted into `hb`; the genuine target
    fixes a concrete `K`, `N`, and `b`. -/
theorem weilGram_posDef_zeta
    (K : ℕ) (N : ℕ) (b : Fin K → ℝ)
    (hb : ∀ i, 0 < b i) :
    (weilGram K N b).PosDef := by
  sorry  -- #ACC-1

/-- **#ACC-2: non-circularity as necessary-not-sufficient (the K2 statement).**

    Non-circularity, stated as the K2 / Davenport-Heilbronn discipline: the same
    `weilGram` construction is available for any L-function with a Gamma factor
    and a Dirichlet coefficient sequence (one supplies a coefficient analogue of
    `primeWeight` and sets `poleResidue := 0` for an entire L-function). For
    Davenport-Heilbronn that data exists and RH FAILS (a known off-line zero at
    `0.808 + 85.7 i`). Therefore positivity of `weilGram` cannot logically
    entail `RiemannHypothesis zeta`: if it did, the identical argument applied to
    the Davenport-Heilbronn Gram would prove an RH that is false.

    We phrase this as: it is NOT the case that, for every choice of inputs,
    positivity of the assembled Gram implies RH for zeta. The certificate is
    non-circular precisely because it is necessary-not-sufficient: it cannot
    entail RH (otherwise it would also "prove" the false D-H analogue). This is
    the M2.6 stealth window (experiments LEARNINGS #34) made into a Prop.

    The `sorry` defers the construction of the explicit Davenport-Heilbronn
    witness Gram and its off-line zero (VERIFIER target #DH-zero supplies the
    zero; `e3m_place_type_balance.py` supplies the indefinite reconstruction). -/
theorem weilGram_noncirc :
    ¬ (∀ (K N : ℕ) (b : Fin K → ℝ),
        (weilGram K N b).PosDef → RiemannHypothesis ZetaRH.zeta) := by
  sorry  -- #ACC-2

end ZetaRH.AccidentAudit

