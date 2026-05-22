# 2A Candidate Dossier: Lorscheid's blueprint framework

> A deeper look at Lorscheid's blueprint reinterpretation of 𝔽₁ (Lorscheid 2012-2015), as a candidate for the missing mathematics of Architecture 2. Companion to [2A_candidate_evaluation.md](2A_candidate_evaluation.md), [2A_R1_DH_exclusion.md](2A_R1_DH_exclusion.md), [2A_R2_fiber_product.md](2A_R2_fiber_product.md), [2A_borger_dossier.md](2A_borger_dossier.md).
>
> Where Borger came from K-theory and Adams operations, Lorscheid came from a different direction: **Tits-Weyl models of algebraic groups** and the search for a category in which both ordinary schemes and monoid schemes (Deitmar 2005) live naturally.

## 1. Historical origin: the search for Tits-Weyl models

Tits' "𝔽₁" goes back to 1957: Tits observed that **finite simple groups of Lie type** (like GL_n(𝔽_q)) have certain combinatorial structures (the Weyl group, the building) that "degenerate" sensibly when q = 1. The Weyl group of GL_n(𝔽_q) is the symmetric group S_n; this is the "Lie group over 𝔽₁."

The challenge: this works at the level of GROUPS, but to make it work at the level of SCHEMES, one needs a category where:

- Ordinary group schemes (like GL_n, defined over ℤ) live as objects.
- The "𝔽₁-versions" (essentially the Weyl groups) also live as objects.
- A morphism GL_n,𝔽₁ → GL_n,ℤ recovers Tits's observation.

This was the Tits-Weyl model program. Multiple attempts (Soulé, Deitmar, Connes-Consani, Toën-Vaquié) failed to give a fully satisfactory category. **Lorscheid's blueprints (2012) is one of the most successful**: a category in which both ordinary schemes and monoid schemes coexist, and Tits-Weyl models for algebraic groups can be constructed uniformly.

## 2. Blueprints, formally

**Definition** (blueprint): A blueprint is a pair (B, B^•) where:
- B is a commutative monoid (= multiplicative structure).
- B^• ⊆ ℕ[B] × ℕ[B] is a "pre-addition" — a sub-equivalence-relation on the free commutative monoid on B, encoding the addition rules.

Equivalently: B^• is a commutative semiring with underlying multiplicative monoid B, and a quotient relation encoding how sums equal each other.

More concretely: a blueprint is a presentation of a ring-like object that allows partial addition rules. Examples make this clearer.

**Examples**:

- **Any commutative ring R**: take B = (R, ×) and B^• = the addition relations of R. So ℤ is a blueprint, ℚ is a blueprint, every ring is a blueprint.
- **Any commutative monoid M**: take B = M and B^• = the trivial relations. So pointed sets like {0, 1} are blueprints with trivial addition.
- **𝔽₁ in Lorscheid's sense**: the blueprint with B = {0, 1} (multiplicative monoid) and B^• = {1 + 1 = 0} or trivial — depending on convention. Several variants exist (𝔽₁, 𝔽₁², semiring blueprints, ...).
- **𝔽₁[x]**: the blueprint with monoid {0, 1, x, x², ...} and no further addition relations. Plays the role of "polynomial ring over 𝔽₁."
- **Semirings**: ℕ as a blueprint with B = ℕ multiplicatively and B^• = the additive relations of ℕ.

The key insight: **blueprints generalize rings by relaxing the requirement that every pair of elements has a sum**. Some pairs may not have a sum; the "addition relations" B^• only specify which sums DO exist and equal what.

## 3. The category of blueprints

**Morphisms**: A blueprint morphism f: (B, B^•) → (B', B'^•) is a monoid morphism B → B' that respects the addition relations (i.e., if a + b = c is a relation in B^•, then f(a) + f(b) = f(c) is a relation in B'^•).

The category Blpr has:
- Initial object: 𝔽₁ (smallest blueprint).
- Terminal object: zero blueprint.
- All limits and colimits (Lorscheid 2012).
- A faithful functor Rings → Blpr (embedding ordinary rings as blueprints).
- A functor Monoids → Blpr (embedding monoid schemes as blueprints with trivial relations).

**Blueprint schemes**: built by gluing affine blueprints along Zariski-like covers, in analogy with ordinary schemes. Lorscheid 2012 develops this scheme theory.

## 4. Lorscheid's interpretation of 𝔽₁

In Lorscheid's framework, **𝔽₁ is the initial blueprint**. Schemes over 𝔽₁ are blueprint schemes.

The morphism Spec(ℤ) → Spec(𝔽₁) corresponds to the inclusion 𝔽₁ ⊂ ℤ at the blueprint level: the multiplicative monoid {0, 1} of 𝔽₁ embeds into the multiplicative monoid of ℤ, and the (trivial) addition relations of 𝔽₁ are a subset of ℤ's.

**Why blueprints over Deitmar's monoid schemes**:

Deitmar (2005) defined 𝔽₁-schemes via commutative monoids alone, no addition. This works for some things (count of "points," combinatorial structures), but **misses the addition relations** that distinguish ℤ from ℕ from "ℤ with weird addition." Blueprints fix this by adding back the addition relations as extra structure.

The advantage: **Lorscheid's framework subsumes both Deitmar's monoid schemes AND ordinary schemes** in one category. The two are not competing parallel worlds; they're both special cases of blueprints.

**Why blueprints over Connes-Consani's hyperrings**:

Connes-Consani use "hyperrings" — rings where addition is multivalued. Blueprints are a different formalism with similar motivation: relax the addition structure. Lorscheid argues blueprints are more flexible: they handle both ordinary rings and Connes-Consani hyperrings as special cases.

## 5. The arithmetic surface in Lorscheid's framework

Per R2, the fiber product Spec(ℤ) ×_{𝔽₁} Spec(ℤ) in Lorscheid's framework gives the blueprint (ℤ × ℤ, doubled relations):

- Multiplicative monoid: ℤ × ℤ with componentwise multiplication.
- Addition relations: from both copies of ℤ.

**Concretely**: the result is a blueprint where you can multiply elements like (3, 5) × (2, 7) = (6, 35) componentwise, AND you can add elements within each component using the ordinary addition of ℤ. But mixing components additively (like (3, 0) + (0, 5) = ?) is not in the relations — the two ℤ factors stay "separate" additively.

**Dimensional analysis**: Lorscheid defines a notion of blueprint dimension. For (ℤ × ℤ, doubled relations), this dimension is 2 (= sum of the dimensions of the two ℤ factors, or product of the two scheme structures, depending on the precise definition).

So **constraint (ii) is satisfied** in Lorscheid's blueprint dimension theory: the fiber product is a genuinely 2-dimensional blueprint scheme.

## 6. Recovery of function-field RH

For curves C/𝔽_q, the blueprint framework reduces to ordinary scheme theory (since 𝔽_q is an ordinary ring). The fiber product C ×_{𝔽_q} C is just the usual scheme-theoretic fiber product, which we already know gives Weil's RH.

So **constraint (xiv) is satisfied** for Lorscheid's framework, with the function-field reduction being completely transparent.

This is a key strength: Lorscheid doesn't have to specially treat the 𝔽_q case — it falls out as the "additive relations are complete" subcategory of blueprints.

## 7. Tits-Weyl models for algebraic groups

A major application of blueprints is the construction of **Tits-Weyl models for algebraic groups**. For each algebraic group G over ℤ (like GL_n, SO_n, Sp_n), there is a blueprint scheme G_{𝔽₁} such that:

- G_{𝔽₁} reduces to the Weyl group of G when restricted to 𝔽_q-points and "degenerated to q = 1."
- The structure morphism G → G_{𝔽₁} captures the relationship between the algebraic group and its Weyl group.

This is the part of Lorscheid's program that **already works**: Tits-Weyl models exist and have been computed for the classical algebraic groups. It's the most concrete success of the blueprint framework.

For Architecture 2 purposes, this is less directly relevant (we're interested in zeta of Spec(ℤ), not in algebraic groups), but it demonstrates that the blueprint framework can do real arithmetic-geometric work.

## 8. What Lorscheid's framework predicts about ζ

This is where the framework is less developed than Borger's. Lorscheid's blueprints don't have a built-in "Frobenius substitute" — that's Borger's specific contribution.

In Lorscheid's framework, ζ would arise via the L-function of an arithmetic scheme structure on 𝔽₁ (the initial blueprint) or some twisted version. The prediction would be:

- ζ is the L-function of the blueprint scheme Spec(𝔽₁) (modulo precise definitions of "blueprint L-function").
- Dirichlet L-functions arise from twists.

But the framework as currently developed doesn't explicitly produce ζ from a blueprint L-function calculation. **This is a gap**: constraint (x) (Euler-factor compatibility) is not as well-served by Lorscheid as by Borger.

## 9. Strengths of the Lorscheid framework

1. **Unifies ordinary schemes and monoid schemes**: blueprints contain both as subcategories, simplifying comparison.
2. **Compatibility with Tits-Weyl models**: a major application that works.
3. **Categorical maturity**: well-developed scheme theory, all limits and colimits, sheaf theory.
4. **Conceptually intuitive**: blueprints are "rings with some addition relations missing." This is easier to grasp than Λ-rings or hyperrings.
5. **Fiber product is genuinely 2-dimensional** in the framework's own dimension theory (constraint ii is satisfied).
6. **Compatibility with function fields is trivial**: ordinary scheme theory is a subcategory.

## 10. Limitations of the Lorscheid framework

1. **No built-in Frobenius substitute**: unlike Borger, blueprints don't have Adams operations or any direct analogue. To get a Frobenius substitute in Lorscheid's framework, one would have to enrich the blueprint structure (e.g., "Λ-blueprints") — not done.
2. **L-function theory underdeveloped**: ζ does not arise naturally from blueprint constructions in the existing literature. Constraints (viii)-(x) are largely empty for Lorscheid.
3. **No intersection theory** on blueprint surfaces (constraint vi): the categorical setup is there but the cycle class theory has not been built.
4. **No cohomology theory** matching the infinite zeta spectrum (constraint iv): Lorscheid has some cohomological constructions but they're discrete-prime in nature, not matching the continuum of zeta zeros.
5. **Not Hodge index ready**: the deepest constraint (xi) is far from being addressable in this framework.

## 11. Active research questions specific to Lorscheid

As of ~2025, blueprint research focuses on:

- **Sheaf cohomology on blueprint schemes**: developing the analogue of étale cohomology for the surface (ℤ × ℤ, doubled relations) and other blueprint surfaces.
- **Intersection theory on blueprint schemes**: constraint (vi). Active work but no breakthrough.
- **Connection to other 𝔽₁ frameworks**: how does Lorscheid relate to Borger, Connes-Consani, Soulé? Each framework prefers to package the same data differently; cleaner cross-framework dictionaries are being developed.
- **Tits-Weyl model refinements**: ongoing work generalizing the algebraic-group case.
- **Blueprint-enriched derived structures**: do derived blueprints / ∞-blueprint categories give better access to cohomology?

## 12. Combinability with other candidates

**With Borger**: blueprints and Λ-rings are categorically different but conceptually compatible. A "Λ-blueprint" candidate (a blueprint enriched with Adams operations) would in principle combine Lorscheid's surface structure with Borger's Frobenius. As of my knowledge, this hybrid has not been explicitly developed, but it's a natural candidate. Strong R4 direction.

**With Connes**: Lorscheid's blueprints and Connes' hyperrings are dual approaches to "addition relaxation." Connes uses multivalued addition; Lorscheid uses missing addition. The two can probably be translated into each other for many constructions, but the underlying technical infrastructure is different. Combination would require choosing one formalism.

**With Deninger**: Lorscheid's blueprint surface could in principle serve as the base for Deninger's foliated space. The foliated structure would have to be added on top of the blueprint structure, which doesn't seem categorically obstructed but hasn't been done.

## 13. Open scorecard items for Lorscheid (post-R1, R2)

Updated based on R1 and R2:

| Constraint | Status | What's needed to close |
|---|---|---|
| (i) | ✅ | — (done) |
| (ii) | 🟡 | Develop intersection theory on the blueprint surface |
| (iii) | ✅ | — (function fields are blueprint subcategory) |
| (iv) | 🟡 | Build a blueprint cohomology with infinite-dim H¹ matching zeta spectrum |
| (v) | ⏳ | Construct Poincaré duality on the blueprint cohomology |
| (vi) | ⏳ | Develop cycle class map and intersection pairing |
| (vii) | ⏳ | Prove Künneth |
| (viii) | ⏳ | Add Frobenius substitute (probably requires enrichment to Λ-blueprints) |
| (ix) | ⏳ | Develop Lefschetz trace formula |
| (x) | ⏳ | Show local Euler factors emerge from blueprint structure |
| (xi) | ⏳ | Hodge index theorem (universally open) |
| (xii) | ⏳ | Prove (xi) without RH input |
| (xiii) | ⏳ | Apply Castelnuovo-Severi argument |
| (xiv) | ✅ | — (ordinary scheme theory recovered) |
| (xv) | ⏳ | Twist by Dirichlet characters in blueprint framework |
| (xvi) | ⏳ | Selberg-class as natural domain |
| (xvii) | ✅ | — (R1 confirmed; D-H not constructible in blueprints) |

Eleven ⏳ items, two 🟡 items, four ✅ items. More open items than Borger because Lorscheid has not addressed the Frobenius and cohomology sides as deeply.

## 14. Bottom line on Lorscheid

**Best aspect**: the blueprint category is conceptually clean, categorically mature, and the fiber product gives a genuinely 2-dimensional surface object. Constraints (i)-(iii) and (xiv) are well-handled.

**Worst aspect**: no Frobenius substitute and no L-function theory natively. The Borger-style "Frobenius is built in" is absent; one would have to enrich blueprints with Λ-structure to get there.

**Most likely path forward**: **Λ-blueprints** (combining Borger's Adams operations with Lorscheid's blueprint structure). This is conceptually natural, would inherit Lorscheid's surface structure (constraint ii ✅) and Borger's Frobenius (constraint viii). As of my knowledge, no one has published a full Λ-blueprint framework, but it would address the gaps in both candidates simultaneously.

**Comparison to Borger**: Lorscheid's framework is better on the geometric/surface side (constraints i-iii, xiv); Borger is better on the algebraic/Frobenius side (constraint viii). Each is "half a candidate." The natural hybrid is Λ-blueprints.

## 15. Suggested research targets specific to Lorscheid

- **L1**: develop blueprint sheaf cohomology of (ℤ × ℤ, doubled relations) explicitly. Compute H¹, H². Identify what these spaces look like categorically.
- **L2**: explore Λ-blueprints. Define a Λ-blueprint as a blueprint with commuting Adams operations satisfying the Fermat-Frobenius condition. Verify that ℤ has a canonical Λ-blueprint structure and that the fiber product ℤ ⊗_𝔽₁ ℤ in Λ-blueprints gives Spec(W(ℤ))-like structure plus blueprint relations.
- **L3**: investigate cycle classes on blueprint surfaces. Even partial development (e.g., for Tits-Weyl models) would inform what cycle class theory could look like for the arithmetic surface.

L2 in particular is the most direct path to a hybrid candidate that addresses more than half of the 17 constraints.

## References (Lorscheid-specific)

- Lorscheid, O. (2012). *The geometry of blueprints. Part I: Algebraic background and scheme theory*. Adv. Math. 229, 1804–1846. The foundational paper.
- Lorscheid, O. (2015). *The geometry of blueprints. Part II: Tits-Weyl models of algebraic groups*. Forum Math. Sigma 6, e20.
- Lorscheid, O. (2018). *𝔽₁ for everyone*. Jahresber. Dtsch. Math.-Ver. 120, 83–116. An accessible expository overview.
- Lorscheid, O.; Tossici, D. (2018). *On the spectrum of a blueprint*. Bull. London Math. Soc. 50, 615–631.
- Deitmar, A. (2005). *Schemes over 𝔽₁*. In: Number Fields and Function Fields — Two Parallel Worlds, Birkhäuser. The earlier monoid scheme approach that Lorscheid generalizes.
- Tits, J. (1957). *Sur les analogues algébriques des groupes semi-simples complexes*. Colloque d'algèbre supérieure (Bruxelles), 261–289. The original 𝔽₁ observation.
- Connes, A.; Consani, C. (2011). *On the notion of geometry over 𝔽₁*. J. Algebraic Geom. 20, 525–557. Companion approach via hyperrings.
- Toën, B.; Vaquié, M. (2009). *Au-dessous de Spec(ℤ)*. J. K-Theory 3, 437–500. Another generalized-scheme approach.
