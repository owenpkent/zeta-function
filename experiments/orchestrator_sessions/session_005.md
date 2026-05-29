# Session 005 synthesis: sharpen the missing correspondence (2Q), then build the Lean explicit-formula thread

> Driven by the `new_mathematics.md` / PHASE_STATE directive ("the product surface
> -- the one remaining object"). Session 004 closed the single-arithmetic-surface
> side and turned "build `Spec(Z) x Spec(Z)`" into a specification (2K). Session 005
> pushes that specification one notch further on the math side (2Q: what the missing
> Frobenius correspondence must BE), then turns to the highest-leverage formalization
> target (the Weil explicit formula + positivity criterion in Lean), landing a green
> scaffold and discharging several Mathlib-bridge lemmas to real proofs.

## The arc

**2Q -- the place-dependent bidegree obstruction** ([e2q](../arithmetic_geometric/e2q_frobenius_bidegree.md), LEARNINGS #25).
Granting 2K's dictionary (every intersection NUMBER computable, only the product
surface missing), 2Q asks what the missing correspondence `Gamma_S` must be. The
single sharpest break: on `C x C` the Frobenius graph is a `(1, q)` correspondence
with ONE scale `q` (the residue cardinality), so RH there is the algebraic
inequality `|t| < 2g sqrt(q)`. Over `Spec(Z)` the fibre over `p` is `Spec(F_p)` of
cardinality `p`, so `Gamma_S` must carry a PLACE-DEPENDENT bidegree `(1, p)` -- no
single `q` (scale spread `max(p)/min(p)` already 86.5 over the first 40 primes,
diverging). From that one fact:

- (1) no single scale => no finite `2x2` primitive Gram (block-graded over places);
- (2) one block per prime power => `H^1` infinite-dimensional => the signature is an
  infinite-dim INDEX theorem, not a determinant -- Deninger's "infinite-dimensional
  `H^i`", DERIVED;
- (3) commensurable place-scales `{log p}` acting at once FORCE a continuous
  `R`-action, the Deninger flow `Phi_t = prod_p U_{log p}^{t/log p}` -- not aesthetic,
  the only carrier of a continuum of commensurable local scales.

`Gamma_S^2` is pinned to the regularized prime-weighted sum `reg-sum_p (log p) *
(local self-int at p)` = the von Mangoldt prime side `P_fin` (2K) = the Direction 4.6
determinant `det_zeta(s - Phi_t)`, with per-fibre adjunction input `12 h_Fal` (2J/2L).
Sharper K2: a `(1, p)` local bidegree IS the Euler factor `(1 - p^{-s})^{-1}`; D-H
has no Euler product, so no local bidegrees, so no `Gamma_S`, so no surface. The
freshest external lead (Morishita, arXiv:2508.15971, now Munster J. Math.) bridges
Deninger and Connes-Consani for abelian number fields via arithmetic topology but
builds NO pairing -- route (b) "toward an actual pairing" stays open.

**Lean: the Weil explicit formula + positivity criterion** ([ExplicitFormula.lean](../../lean/ZetaRH/ExplicitFormula.lean)).
The project's highest-leverage Mathlib target (LEARNINGS #17). Mathlib v4.13.0 has
`riemannZeta`, the functional equation, the pole residue, and `vonMangoldt`, but not
the explicit formula, no digamma, and no sum-over-zeros theory. So a faithful TYPED
SCAFFOLD: the prime side `primeSum` is CONCRETE (a `tsum` against `Λ`); the spectral,
archimedean, and pole functionals are bundled into `WeilExplicitFormula` with the
identity `zeroSum = archTerm + poleTerm - primeSum`; `weil_explicit_formula_zeta`
(#EF-1) asserts the bundle exists for ζ; `weil_positivity_criterion` (#EF-2) states
`weilForm`-positivity on all admissible tests <=> `RiemannHypothesis zeta`. This is
the Architecture-3 (trace/positivity) face of the same positivity whose
Architecture-2 (signature) face is `HodgeIndex.negDef_iff_hasseWeil`. K2/D-H
discipline documented (#EF-K2). Build green.

**Lean: discharges to real proofs** ([MathlibBridge.lean](../../lean/ZetaRH/MathlibBridge.lean)).
Three placeholder sorries became kernel-checked proofs from existing Mathlib:
#MB-1 (ζ pole at `s=1`, `(s-1)ζ(s)→1`, via `riemannZeta_residue_one`), #MB-2 (ζ≠0
on `Re s>1`, via `riemannZeta_ne_zero_of_one_lt_re`), #MB-6 (functional equation
`Λ(1-s)=Λ(s)`, via `completedRiemannZeta_one_sub`; restated from the old `True`
placeholder). In `ExplicitFormula.lean` the archimedean kernel is now CONCRETE:
`digamma := logDeriv Complex.Gamma` with `digamma_eq` proved (no sorry), and
`archKernel r = -(1/2) log π + (1/2) ψ(1/4 + i r/2)` -- the `A_arch` density of the
3M decomposition (kernel part of #EF-arch discharged; the integral pairing #EF-class
remains). Project sorry count 26 → 23; full `lake build ZetaRH` green.

## The single takeaway

Session 004 specified WHAT the missing surface's intersection form is; session 005
specifies WHAT its Frobenius correspondence is (place-dependent bidegree `(1,p)`,
regularized self-intersection = the prime sum) and, separately, builds the formal
home (in Lean) for the Architecture-3 positivity criterion that the surface's
signature is meant to explain. The two threads meet at the same object: the prime
side `P_fin` is simultaneously 2Q's `Gamma_S^2`, 3M's finite block, and
`ExplicitFormula.primeSum` (the one concrete Lean functional).

## Methodological note (the discipline that held)

2Q ships as an ILLUSTRATION, explicitly not a proof (the FF single-scale family vs
the unbounded `{log p}` spectrum), avoiding the numerology trap a naive "assemble the
finite arithmetic Gram" would have been -- and it absorbs that honest-negative content
(why the finite transcription cannot exist) into the structural finding. On the Lean
side, the discipline was "discharge what Mathlib can actually close, scaffold the rest
with documented sorries": three bridge lemmas went to real proofs, the digamma kernel
went concrete, and only the genuinely-missing analytic objects (#EF-1, #EF-2, the
integral pairing) remain as flagged targets. The external lead (Morishita) was
verified by fetching the paper, not assumed from the project's prior note.

## Commits (session 005)

2Q: `1b4701d`. Lean explicit-formula scaffold: `f090765`. Bridge discharges + digamma
kernel: `960c1b4`. (All local on `main`, not pushed as of session end.)

## Recommended next steps

1. **Math (continue 2Q):** 2R -- the Ruelle dynamical-zeta realization of `Gamma_S^2`
   (closed-orbit lengths `= {log p}`; log-derivative `= -ζ'/ζ =` the prime side;
   D-H has no such primitive-length orbit spectrum). The concrete dynamical face of
   the Direction 4.6 determinant, tied to the Morishita closed-orbits↔primes bridge.
2. **Formal (continue the Lean thread):** the digamma recurrence `ψ(s+1)=ψ(s)+1/s`
   from `Complex.Gamma_add_one` (upstreamable, hardens #EF-arch); then a concrete
   `archTerm` once a Fourier/Mellin transform is fixed (#EF-class); the genuine
   #EF-1/#EF-2 need sum-over-zeros theory (multi-step).
3. **The product surface (the real target, unchanged):** Directions 1-4 with the now
   doubly-specified goal -- a surface whose intersection form is `A_arch + P_fin +
   B_pole` (2K) and whose correspondence has bidegree `(1,p)` per place (2Q).
4. **Process:** push the 3 local commits when authorized; remote-autonomy infra still
   needs cloud write/PR access tested before unattended runs (session-004 lesson).
