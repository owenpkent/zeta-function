# 2A — R2: Computing Spec(ℤ) ×_𝔽₁ Spec(ℤ) in Borger and Lorscheid frameworks

> Companion to [2A_candidate_evaluation.md](2A_candidate_evaluation.md) §V. R2 examines constraint (ii) — "Non-trivial fiber product: Spec(ℤ) ×_S Spec(ℤ) must be a 2-dimensional object" — for the two most mature 𝔽₁ candidates: Borger's Λ-rings (2009) and Lorscheid's blueprints (2012). The goal is to upgrade the (ii) verdicts from "🟡 partial" / "⏳ open" toward a precise statement of what's been computed, what's known about the dimension, and what would be needed to satisfy the constraint fully.
>
> **Caveat upfront**: this is a literature survey informed by my best understanding of Borger 2009, Borger-de Smit 2008, Lorscheid 2012, and follow-up work through ~2020. Where I'm uncertain about a specific theorem or definition, I'll flag it explicitly. Corrections welcome.

## 1. The question, precisely

In Weil's proof for curves over 𝔽_q, the surface C × C is constructed as a fiber product over Spec(𝔽_q). The arithmetic analogue should be:

$$\mathrm{Spec}(\mathbb{Z}) \times_{\mathrm{Spec}(\mathbb{F}_1)} \mathrm{Spec}(\mathbb{Z})$$

where Spec(𝔽₁) is "the scheme below Spec(ℤ)." Constraint (ii) asks whether this fiber product, computed within the candidate framework, is a 2-dimensional object — not a 1-dimensional collapse (which is what happens with the trivial fiber product over Spec(ℤ): Spec(ℤ) ×_{Spec(ℤ)} Spec(ℤ) = Spec(ℤ), the diagonal).

The fiber product is 2-dimensional **as needed** if and only if:
- It has Krull dimension 2 (the most common interpretation), OR
- It has cohomological dimension 2 for some cohomology theory, OR
- It carries an intersection theory with the right number of "directions" for divisors.

The strictest reading: the fiber product should be a proper, smooth, 2-dimensional scheme-like object with a Picard group, an intersection pairing, and the signature structure needed for Castelnuovo-Severi-style positivity.

Most existing 𝔽₁ candidates achieve some weaker version of this.

## 2. Borger's framework: Spec(ℤ) ×_{𝔽₁} Spec(ℤ) via the big Witt ring

### 2.1 Setup: Λ-rings and the Borger interpretation of 𝔽₁

A **Λ-ring** is a commutative ring A equipped with commuting endomorphisms {ψ_p}_p (one for each prime), called **Adams operations**, satisfying:

- ψ_p is a ring endomorphism: ψ_p(x + y) = ψ_p(x) + ψ_p(y), ψ_p(xy) = ψ_p(x) ψ_p(y)
- ψ_p(x) ≡ x^p (mod p) for all x ∈ A
- The ψ_p commute pairwise: ψ_p ψ_q = ψ_q ψ_p

Borger's reinterpretation of 𝔽₁: **schemes over 𝔽₁ are Λ-schemes** (Λ-rings on the affine side). The initial Λ-ring is **ℤ** with its canonical Λ-structure: ψ_p(n) = n for all n ∈ ℤ (this satisfies n ≡ n^p mod p by Fermat's little theorem).

So in this view, Spec(𝔽₁) = Spec(ℤ with Λ-structure), and the morphism Spec(ℤ) → Spec(𝔽₁) is **forgetting** the Λ-structure: an ordinary ℤ-algebra A is treated as a Λ-ring by "discarding" the Adams operations.

The arithmetic-geometric morphism Spec(ℤ) → Spec(𝔽₁) is therefore the forgetful functor U: Λ-Rings → Rings, viewed as a base-change morphism in the opposite categories.

### 2.2 The fiber product

In Λ-ring algebra, the fiber product Spec(ℤ) ×_{𝔽₁} Spec(ℤ) corresponds to the pushout (in Λ-rings) of two copies of ℤ under the diagonal:

$$\text{ℤ} \otimes_{(\mathrm{ℤ},\, \mathrm{canonical}\, \Lambda)} \text{ℤ}$$

The tensor product is computed in the category of Λ-rings, which is different from the ordinary tensor product of commutative rings.

**Key fact** (Borger 2009): the forgetful functor U: Λ-Rings → Rings has a right adjoint W, the **big Witt vector functor**. So:

$$\mathrm{Hom}_{\Lambda\text{-Rings}}(A, W(B)) = \mathrm{Hom}_{\mathrm{Rings}}(U(A), B)$$

This adjunction has a key consequence for fiber products:

$$\text{ℤ} \otimes_{\Lambda} \text{ℤ} \cong W(\text{ℤ} \otimes_{\mathrm{ℤ}} \text{ℤ}) = W(\text{ℤ})$$

Wait — that needs care. The exact computation requires understanding what "tensor in Λ-rings" is, which I'll claim (subject to verification) is computed by:

$$\mathrm{Spec}(\mathbb{Z}) \times_{\mathrm{Spec}(\mathbb{F}_1)} \mathrm{Spec}(\mathbb{Z}) \simeq \mathrm{Spec}(W(\mathbb{Z}))$$

where **W(ℤ) is the big Witt vector ring of ℤ**.

### 2.3 What is W(ℤ)?

The big Witt vector ring W(A) of a commutative ring A consists of sequences (a₁, a₂, a₃, ...) with a_n ∈ A, equipped with:

- Componentwise addition (after the universal polynomial formulas)
- A multiplication structure tied to the "ghost components"
- Frobenius and Verschiebung maps

Equivalently and more concretely: W(A) is isomorphic (as a set) to **1 + tA[[t]]** (formal power series with constant term 1), with multiplication being formal-series multiplication. The isomorphism sends (a₁, a₂, ...) to the power series ∏_n (1 - a_n t^n)^(-1) or similar (sign conventions vary).

For A = ℤ:

- **W(ℤ) is isomorphic to 1 + tℤ[[t]]** as a multiplicative monoid.
- As a ring, W(ℤ) is a topological ring with a natural inverse limit structure: W(ℤ) = lim_n W_n(ℤ) where W_n is the n-truncated Witt vectors.
- W(ℤ) contains ℤ via the "Teichmüller representative" map a ↦ (a, 0, 0, ...).

### 2.4 Dimension analysis

This is where it gets delicate. What is **dim Spec(W(ℤ))**?

**Krull dimension of W(ℤ)**: this is non-trivial. W(ℤ) is uncountable (it has a power series component). It has many prime ideals corresponding to combinations of primes in ℤ and "Verschiebung" directions.

I do not have a definitive published Krull dimension for W(ℤ) in hand. I believe it is **infinite** (since the topology has infinite-dimensional aspects), but I'm not confident in this claim.

**For truncated Witt vectors W_n(ℤ)**: these are more tractable. W_n(ℤ_(p)) (localized at p) has Krull dimension 2 — one dimension from ℤ_(p) itself, plus one from the n-truncated Witt structure. The truncated case is closer to what Weil's proof needs (a 2-dimensional surface).

So the candidate object: **Spec(W_n(ℤ)) for some n**, rather than Spec(W(ℤ)) itself, may be the right 2-dimensional object. The dimension counting is:

- Spec(ℤ) is 1-dimensional (one prime ideal direction)
- W_n(ℤ) adds a finite "tower" structure
- Spec(W_n(ℤ)) is 2-dimensional when restricted to each prime localization

**Verdict on (ii) for Borger**: Spec(W(ℤ)) is the candidate object; **whether it's "the right 2-dimensional object" for Weil's proof template is open**. The truncations W_n(ℤ) are 2-dimensional in the right sense but it's unclear how to combine them into a single object with proper intersection theory.

### 2.5 Intersection theory and Hodge index

For the surface Spec(W(ℤ)) to satisfy the next constraints (vi, vii) and ultimately the Hodge index theorem (xi), it would need:

- A well-defined Picard group Pic(Spec(W(ℤ))) — which exists in the formal scheme sense.
- A cycle class map to a "second cohomology" H²
- A symmetric bilinear intersection pairing
- The Hodge index theorem on this pairing

To my knowledge, **none of these have been worked out explicitly for Spec(W(ℤ))** in the Borger framework. The framework is sufficiently mature to ASK these questions, but the answers are open.

### 2.6 Updated (ii) verdict for Borger

Previous: ⏳ (open).

Updated: **🟡 (partial)**. The candidate object Spec(W(ℤ)) is constructed and is non-trivially "above" Spec(ℤ), so the fiber product is genuinely larger than the trivial diagonal. The dimension is 2 in the truncated case W_n(ℤ); the full case W(ℤ) has infinite-dimensional aspects that may or may not be a problem. **The constraint is partially satisfied** but a precise statement of "what is the dimension of the surface, and what is its intersection theory" is still missing.

## 3. Lorscheid's framework: blueprint tensor product

### 3.1 Setup: blueprints

A **blueprint** is a pair (M, B) where:
- M is a commutative monoid (multiplicative structure)
- B is a "relation" on the semigroup ring ℕ[M] (additive structure encoded as equivalences)

Examples:
- Any commutative ring R is a blueprint (with M = (R, ×) and B encoding the addition relations).
- Any commutative monoid M is a blueprint (with B trivial — no addition relations beyond what M provides).
- 𝔽₁ in Lorscheid's sense is the blueprint with M = {0, 1} (multiplicative monoid) and trivial B.

So ℤ is a blueprint, 𝔽₁ is a blueprint, and there's a canonical morphism 𝔽₁ → ℤ (since {0, 1} ⊂ ℤ multiplicatively).

### 3.2 The fiber product

In the category of blueprint schemes (Lorscheid 2012), fiber products are computed via the blueprint tensor product. For ℤ ⊗_{𝔽₁} ℤ:

The tensor product in blueprints is computed by first tensoring the underlying monoids (M_ℤ ⊗ M_ℤ) and then imposing the union of the relations. For ℤ ⊗_{𝔽₁} ℤ:

- M_ℤ ⊗_{M_{𝔽₁}} M_ℤ: the multiplicative monoids of ℤ are tensored over {0, 1}. Since {0, 1} is the initial monoid (multiplicatively), the tensor is just (ℤ, ×) ⊗_{(𝔽₁, ×)} (ℤ, ×) = (ℤ × ℤ, componentwise ×).
- Relations: both copies of ℤ contribute their addition relations.

The result is the blueprint (ℤ × ℤ, ×) with relations from both factors. **This is NOT a ring in the usual sense** — it's a blueprint that may or may not "represent" a familiar object.

### 3.3 Dimension

The blueprint ℤ ⊗_{𝔽₁} ℤ has:

- Monoid part (ℤ × ℤ): 2-dimensional in the monoid sense.
- Blueprint dimension (= max of monoid + ring dimensions): Lorscheid defines this and it should give 2 for this case.

So **the fiber product is 2-dimensional in Lorscheid's blueprint dimension theory**. This is closer to what we want than the trivial collapse.

However:

- Whether this 2-dimensional blueprint has the structure of a SCHEME with intersection theory is unclear. Lorscheid has developed blueprint schemes but the cycle class theory is incomplete.
- The 2-dimensionality is "Lorscheid's blueprint dimension" specifically, not necessarily the same as Krull dimension of an underlying ring (since there isn't a single underlying ring).

### 3.4 Updated (ii) verdict for Lorscheid

Previous: 🟡 (partial).

Updated: still **🟡 (partial)**, with a clearer picture of WHY. The blueprint fiber product is genuinely 2-dimensional in Lorscheid's framework, but:

- The framework's notion of "dimension" is not yet the same as Krull dimension or cohomological dimension.
- The intersection theory (constraint vi) and Künneth (vii) are not yet developed for the blueprint surface.
- Without these, Lorscheid's 2-dimensional fiber product cannot yet be plugged into Weil's proof template at step D (Hodge index).

So Lorscheid is **closer** to satisfying (ii) than Borger, but the downstream constraints (vi, vii, xi-xiii) are similarly open.

## 4. Comparison and synthesis

| Aspect | Borger | Lorscheid |
|---|---|---|
| Base 𝔽₁ | Λ-rings; initial = ℤ with canonical Λ | Blueprints; 𝔽₁ = ({0,1}, trivial relations) |
| Fiber product | Spec(W(ℤ)), big Witt ring | Blueprint (ℤ × ℤ, doubled relations) |
| Dimension claim | 2-dim in W_n(ℤ) truncations; W(ℤ) itself is infinite-dim | 2-dim in blueprint dimension theory |
| Intersection theory | Not developed | Not developed |
| Cohomology | Witt-vector cohomologies under development (de Rham-Witt etc.) | Cohomology of blueprint schemes partially developed |
| Connection to Weil step D | Not yet | Not yet |

**Both candidates produce a non-trivial fiber product** (satisfying the surface-existence half of constraint ii). **Neither has developed intersection theory on the resulting surface** (failing the "intersection-theoretic content" half of constraint vi, which is downstream of ii).

The structural situation is the same in both: the framework is mature enough to ASK what the surface is, but not mature enough to ANSWER what its intersection theory looks like.

## 5. The deeper question: which framework's surface is "right"?

Borger and Lorscheid give DIFFERENT candidates for the surface:

- **Borger**: Spec(W(ℤ)) — a "big" formal scheme
- **Lorscheid**: a blueprint with monoid (ℤ × ℤ)

If either is the correct surface, we'd expect:

1. The surface should reduce to C × C over 𝔽_q (constraint iii / xiv). Both frameworks have this reduction theorem in some form, but I'm not certain they give consistent answers when restricted to function fields.
2. The surface should have a Frobenius action whose trace formula reproduces the explicit formula for ζ (constraint ix). Connes' adelic side gives one version of this; whether Borger / Lorscheid surfaces also do is open.
3. The surface should have a Hodge index theorem (constraint xi). This is universally open.

So R2 doesn't choose between Borger and Lorscheid — both are valid partial candidates for constraint (ii). The real test will come at constraint (xi): does either surface have a positivity theorem provable without RH input? Neither has been pushed that far.

## 6. Updated scorecard rows

| Candidate | (ii) Previous | (ii) Updated | Status |
|---|---|---|---|
| Borger | ⏳ | 🟡 | Spec(W(ℤ)) is the candidate; dimension 2 in truncated case, infinite for full; intersection theory not developed |
| Lorscheid | 🟡 | 🟡 | Blueprint (ℤ × ℤ, doubled relations) is the candidate; 2-dim in blueprint sense; intersection theory not developed |

Both candidates remain at 🟡 for (ii), with R2 providing a more precise picture: the surfaces exist as candidate objects but their dimensional/intersection-theoretic structure is incomplete.

## 7. What would close the constraint?

To upgrade (ii) from 🟡 to ✅ for either candidate:

**For Borger:**
- Pick the right truncation level n for W_n(ℤ) (or compactification of W(ℤ))
- Prove Spec(W_n(ℤ)) is a proper smooth scheme of Krull dimension 2
- Develop a Picard group + intersection pairing
- Show the intersection pairing has the expected signature properties (eventually toward Hodge index)

**For Lorscheid:**
- Promote the blueprint (ℤ × ℤ, relations) to a blueprint scheme with proper categorical structure
- Develop intersection theory on blueprint schemes
- Establish a comparison theorem: blueprint surface restricted to 𝔽_q-points = ordinary surface C × C

Both lines of work are active research as of ~2025. R2 maps the state; neither has been closed.

## 8. What R2 does NOT close

R2 was concrete (compute a specific object) but didn't progress the central construction problem. Specifically:

- (xi)-(xiii) Hodge index positivity: still universally open. R2 confirmed the *candidate surfaces* exist but not the *positivity on those surfaces*.
- (vi) Cycle class / intersection pairing: still open in both Borger and Lorscheid. This is downstream of (ii) and required for (xi).
- (vii) Künneth formula: still open. Important for showing the surface decomposes as expected.

R2 produced one upgrade (Borger's (ii) from ⏳ to 🟡), plus a refined picture of what Lorscheid's existing 🟡 means. The central obstruction remains the Hodge index positivity slot.

## 8.5 Companion dossiers

The R2 analysis is summary-level. For full per-candidate analyses see:

- [2A_borger_dossier.md](2A_borger_dossier.md) — Borger's Λ-ring framework: origins in K-theory, formal definition, Adams operations, Witt vector adjunction, what the framework predicts about ζ, strengths and limitations, active research questions, combinability with other candidates, and per-constraint scorecard with what would close each open item.

- [2A_lorscheid_dossier.md](2A_lorscheid_dossier.md) — Lorscheid's blueprint framework: origins in the Tits-Weyl program, blueprints as "rings with partial addition," the blueprint surface, recovery of function-field RH, strengths and limitations, and the most-promising hybrid direction (Λ-blueprints).

**The key insight from the dossiers**: Borger and Lorscheid have complementary strengths:

- **Borger** is strong on (viii) Frobenius (Adams operations built in) but weak on (ii) surface structure (Spec(W(ℤ)) is conceptually heavy).
- **Lorscheid** is strong on (i)-(iii) base/surface (blueprints clean, fiber product 2-dim) but weak on (viii) Frobenius (no built-in Adams operations).

**A natural hybrid: Λ-blueprints.** A blueprint enriched with commuting Adams operations satisfying the Fermat-Frobenius condition. This would inherit Lorscheid's clean surface structure AND Borger's built-in Frobenius. As of my knowledge, no published work has explicitly developed Λ-blueprints, but the construction is categorically natural and would address more than half of the open 17-constraint slots in a single move.

**R2.5 (suggested)**: develop the Λ-blueprint framework. Define a Λ-blueprint as (B, B^•, {ψ_p}) where (B, B^•) is a blueprint and {ψ_p} are commuting blueprint endomorphisms satisfying ψ_p(x) ≡ x^p mod B^•(p) (with the appropriate blueprint version of Fermat). Verify ℤ has a canonical Λ-blueprint structure (likely yes, by combining ℤ's blueprint and Λ structures). Compute the fiber product in Λ-blueprints: this should give something resembling Spec(W(ℤ)) with blueprint relations.

This is more substantial than R2 itself but is the natural next research direction surfaced by the comparison.

## 9. Next-step R3 / R4 in light of R2

R2 informs the priority of R3 and R4:

- **R3 (Connes-Consani positivity classification)** is independent of R2 — different candidate, different positivity question.
- **R4 (hybrid candidates)**: R2 sharpens what a "Borger Frobenius + Connes trace formula" hybrid would need. The Frobenius substitute (Adams operations or adelic action) can be either candidate's; but they'd then have to share a surface, which is where Borger's W(ℤ) or Lorscheid's blueprint would need to provide the surface. If neither surface supports the trace formula from Connes (because of the adelic-vs-Witt mismatch), the hybrid doesn't combine cleanly.

The natural next R2.5 would be: check whether Borger's Spec(W(ℤ)) supports an action recovering Connes' adelic trace formula. If yes, hybridization is viable; if no, it isn't. This is a moderate-difficulty literature task.

## 10. Caveats and uncertainties

I want to be explicit about what I'm less confident about:

1. The exact statement of the Borger adjunction U ⊣ W and its implications for fiber products. I believe it gives Spec(W(ℤ)) as the candidate, but the precise theorem requires checking against Borger 2009.
2. The Krull dimension of W(ℤ). I claimed it's infinite for the full big-Witt ring and 2 for truncations, but haven't verified this.
3. Lorscheid's blueprint dimension theory. I claimed it gives 2 for the blueprint (ℤ × ℤ, doubled relations); this should be checked against Lorscheid's published definition.
4. Whether either candidate has been pushed to develop intersection theory or Hodge index. To my knowledge, neither has — but the literature is large and I may be missing relevant work.

For each of these, the structural picture I've sketched is likely roughly right (both candidates produce surface-like objects, neither has intersection theory developed), but the specific technical claims need verification.

The R2 conclusion is **directionally correct**: both candidates partially satisfy (ii), neither fully, and the bottleneck is intersection theory / Hodge index. The exact technical statements would benefit from refinement against the published literature.

## 11. References (R2-specific)

- Borger, J. (2009). *Λ-rings and the field with one element*. arXiv:0906.3146.
- Borger, J.; de Smit, B. (2008). *Galois theory and integral models of Λ-rings*. Bull. London Math. Soc. 40, 439–446.
- Lorscheid, O. (2012). *The geometry of blueprints. Part I: Algebraic background and scheme theory*. Adv. Math. 229, 1804–1846.
- Lorscheid, O. (2015). *The geometry of blueprints. Part II: Tits-Weyl models of algebraic groups*. Forum Math. Sigma 6, e20.
- Connes, A.; Consani, C. (2010). *From monoids to hyperstructures: in search of an absolute arithmetic*. In: Casimir Force, Casimir Operators and the Riemann Hypothesis, 147–198.
- Hesselholt, L. (2015). *The big de Rham-Witt complex*. Acta Math. 214, 135–207. (Relevant for cohomological development of Witt vectors.)

For an accessible overview: Lorscheid, O. (2018). *𝔽₁ for everyone.* Jahresber. Dtsch. Math.-Ver. 120, 83–116.
