# Reading notes: Deninger, *Motivic L-functions and regularized determinants II*

> First entry in the reference-library read-through (see
> [`references/README.md`](../../../references/README.md)). This is the
> highest-priority source for the live front (Direction 4.6 → 8): its content is,
> almost line for line, the object the program is trying to build. Notes are mapped
> to the project's findings (2Q, 2R, 2K, 2I) and milestones (Direction 4.6,
> Direction 8). Pages refer to the PDF in
> `references/02_deninger_program/`.

## One-line takeaway

Deninger's `H^1(𝒴, F(ℚ(0)))` whose `Θ`-eigenvalues are exactly the non-trivial
zeros of `ζ_k`, with the completed `ζ` as a regularized determinant
`det_∞((s-Θ)/2π | H^*)`, **is** the object Direction 4.6 must construct. The program's
2R realized its *spectrum* (a dynamical zeta with orbit lengths `{log p}`); Deninger
specifies the *cohomology* that spectrum should live on. And §3.7 states the
2K/2Q product-surface gap in Deninger's own words.

## The points that matter, mapped to the project

1. **Semigroup `T⁺ = (ℝ^{≥0}, +)`, not a group (p.2).** Deninger is deliberately
   cautious: he expects only a *semigroup* action, "because explicit formulas in
   analytic number theory take the form of a Lefschetz trace formula only if we
   restrict attention to test functions with support on `ℝ⁺`" (citing Deninger-
   Schröter 3.2.3). `Θ` is the infinitesimal generator.
   → **Direct match to 2Q/2R.** This is exactly the flow `Φ_t = ∏_p U_{log p}^{t/log p}`
   forced by 2Q, and the test-function restriction is the same one in our Weil-form
   work. The "semigroup not group" caution is the analytic shadow of 2Q's
   place-dependent bidegree (a one-sided Frobenius semigroup `{Fr_q^ν | ν≥0}`).

2. **The space `𝒴` is singular at the archimedean places (p.2).** `𝒴` (associated
   to `spec(O_k) ∪ {p|∞}`) is analogous to `Y = Y₀ ⊗_{F_q} F̄_q`, with `T⁺`
   corresponding to the Frobenius semigroup `ℤ⁺`. It is "expected to be highly
   singular in the points corresponding to the archimedean places," so `H^i(Y, j_*M)`
   is really *intersection* cohomology (Poincaré duality + weights survive, (1.1)).
   → **Match to 2I/2K (#23):** the archimedean place is special; positivity is global;
   the surface must be compactified/singular at `∞`. Deninger's "intersection
   cohomology at the archimedean singularity" is the home for 2I's `λ_inf`.

3. **The 4.6 target, verbatim (p.3).** `H⁰(𝒴, F(ℚ(0))) = ℂ(0)`,
   `H²(𝒴, F(ℚ(0))) ≅ ℂ(-1)` (via Tr), and **`H¹(𝒴, F(ℚ(0)))` decomposes into the
   finite-dimensional generalized eigenspaces `lim_N Ker(Θ - ρ·id)^N` with eigenvalues
   `ρ` the non-trivial zeros of `ζ_k(s)`** (with multiplicities).
   → This is **exactly** the cohomology Direction 4.6 must produce. 2R gave the
   spectrum side (`-ζ'/ζ`, orbit lengths `{log p}`); this is the `H^1` it should be
   the spectrum *of*. The `H⁰`/`H²` give the pole/`ℂ(-1)` (the `B_pole` block of 2K).

4. **The regularized-determinant form (3.8).**
   `L̂(M,s) = ∏_{i=0}^{2} det_∞((s-Θ)/2π | H^i(𝒴, F(M)))^{(-1)^{i+1}}`.
   → This is the precise shape of 4.6's `det_ζ(s - Φ_t | H^*_{F,pr})`: `ζ` is the `H¹`
   determinant divided by the `H⁰·H²` determinants (the zeros over the pole/archimedean
   factors), the function-field pattern lifted. 2R verified the `H¹`/prime-side
   content numerically; (3.8) is the structural identity it instantiates.

5. **§3.7 — the product-surface gap, in Deninger's own words.** `Θ` is a *derivation*
   for cup product (Leibniz). Kontsevich-Manin suggested looking for additive relations
   `ρ₁ + ρ₂ = ρ₃` among zeros of Hasse-Weil zetas of `X, Y, X×Y`. "No non-trivial such
   relations were found by the computer." The stated reason: **"the fibre products
   `X×Y` are taken over the generic point `spec ℚ` of the curve `𝒴`, and not over an
   absolute base point."**
   → This is **precisely the 2K/2Q gap.** The missing "absolute base point" is
   `Spec(F₁)`; `X ×_ℚ Y` is not the product surface `Spec(ℤ) ×_{F₁} Spec(ℤ)`. Deninger
   names the exact obstruction the program calls "the one missing object." Worth
   recording that he confirms a *computer search* for the naive additive relations
   came up empty — i.e. the structure is not visible at the level of `×_ℚ`, only over
   the absolute base.

6. **§6 — the signature pairing (pp.10-11).** For an orthogonal motive, the cup-product
   pairing `[.,.] : H¹ × H¹ → H² → ℂ(-n-1)` is "perfect and alternating," and `Θ`
   satisfies Leibniz; this is used to argue the global root number is `+1`.
   → This is the **Direction 8 signature mechanism** in Deninger's formalism: positivity/
   sign from a perfect cup-product pairing on `H¹`. The thing 2R does *not* supply
   (only the spectrum) and Direction 8 needs. Deninger's pairing is the template for
   "the signature, not just the spectrum."

7. **Finite-vs-infinite determinant puzzle (p.8, remark after 4.11).** Whether the
   regularized `det_∞` equals a finite `det_ℚ I_∞⁺(M)` (Beilinson) "up to powers of `2π`
   and rational factors remains to be found... observed before in physics... the
   mechanism remains unclear."
   → Flags that even granting 4.6, the bridge from the regularized determinant to a
   *computable finite* quantity is itself open. Relevant if we ever try to make 4.6's
   determinant numerically checkable beyond the Euler-product piece 2R already did.

## What this changes for the program

- **2Q/2R are confirmed as the right reduction.** Deninger independently arrives at
  the semigroup/flow, the `{log p}` orbit/Frobenius structure, the archimedean
  singularity, and the regularized determinant. 2R's dynamical zeta is the spectrum of
  his `H¹`; 2Q's bidegree is his one-sided Frobenius semigroup. Good external validation
  that the session-005 work is pointed correctly.
- **The gap is sharpened identically.** §3.7 = the 2K "absolute base point"/product-
  surface gap. Direction 8's job is his §6 cup-product signature on `H¹`; that is the
  part 2R explicitly does not reach.
- **Actionable next read:** Deninger I (the construction of `F_p(M)` and the local
  `det_∞`), then Leichtnam 2006 (a Lefschetz trace formula for laminated spaces built
  for exactly this `H¹`), then Álvarez López-Kordyukov-Leichtnam 2017. These are the
  concrete attempts at the `H^*_{F,pr}` + trace formula that 4.6 needs.

## Status

Read: pp. 1-11 (intro through §6). Remaining pp. 12-19 (rest of §6 + later sections)
are the orthogonal-motive root-number computation; lower priority for the surface
gap but relevant to the signature mechanism. First reference-library entry done.
