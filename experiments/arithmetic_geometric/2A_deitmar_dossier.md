# 2A Candidate Dossier: Deitmar's monoid schemes

> A deeper look at Deitmar's monoid-scheme approach to $\mathbb{F}_1$-geometry (Deitmar 2005), the original and structurally simplest of the major $\mathbb{F}_1$ frameworks. Companion to [2A_candidate_evaluation.md](2A_candidate_evaluation.md), [2A_R1_DH_exclusion.md](2A_R1_DH_exclusion.md), and the other candidate dossiers ([2A_borger_dossier.md](2A_borger_dossier.md), [2A_lorscheid_dossier.md](2A_lorscheid_dossier.md), [2A_connes_dossier.md](2A_connes_dossier.md), [2A_deninger_dossier.md](2A_deninger_dossier.md)).
>
> Deitmar's framework is the "baseline" $\mathbb{F}_1$ candidate — the simplest possible construction that gives a category of "schemes below $\mathbb{Z}$" with $\mathbb{F}_q$-schemes embedding correctly. Subsequent frameworks (Lorscheid, Borger, Connes-Consani) all build on Deitmar's intuition while adding structure. This dossier covers the framework, its strengths and limitations, and the reasons it can't directly support an RH proof.

## 1. Historical origin: the simplest $\mathbb{F}_1$

The "field with one element" $\mathbb{F}_1$ was first envisioned by Tits (1956) as a heuristic explanation of why Chevalley groups have analogs over "$\mathbb{F}_1$" (limits as $q \to 1$ of the Chevalley group construction). For decades, $\mathbb{F}_1$ remained a philosophical placeholder without a rigorous mathematical definition.

Deitmar (2005) "Schemes over $\mathbb{F}_1$" provided the first concrete realization:

**Core definition**: $\mathbb{F}_1$-geometry = the geometry of **commutative monoids**. An $\mathbb{F}_1$-algebra is a commutative monoid $M$ with absorbing element $0$. A "scheme over $\mathbb{F}_1$" is built by gluing local pieces $\mathrm{Spec}(M)$ for commutative monoids $M$, where $\mathrm{Spec}(M)$ is the set of prime ideals (= complements of submonoids closed under multiplication).

**The intuition**: a ring has both addition and multiplication. The "$q = 1$ limit" forgets addition, leaving only the multiplicative monoid structure. So an $\mathbb{F}_1$-algebra is a multiplicative monoid; an $\mathbb{F}_1$-scheme is built from monoid spectra.

**The minimal example**: $\mathbb{F}_1$ itself is the monoid $\{0, 1\}$ with $0 \cdot 0 = 0 \cdot 1 = 0$, $1 \cdot 1 = 1$. This is the initial object in commutative monoids with absorbing element.

## 2. Monoid schemes, formally

**Definition** (Deitmar 2005, modeled on Grothendieck's scheme construction):

For a commutative monoid $M$ with absorbing element $0$:
- $\mathrm{Spec}(M)$ = set of prime ideals of $M$ (an ideal $I \subset M$ with $M \setminus I$ a submonoid; prime if $ab \in I \implies a \in I$ or $b \in I$).
- Equipped with a Zariski-style topology (basic open sets $D(f) = \{p : f \notin p\}$ for $f \in M$).
- A structure sheaf $\mathcal{O}$ valued in commutative monoids.

A **monoid scheme** is a locally monoid-ringed space locally isomorphic to $\mathrm{Spec}(M)$ for some $M$.

**Morphism**: $\mathrm{Spec}(M) \to \mathrm{Spec}(N)$ is induced by a monoid homomorphism $N \to M$ (contravariant, just like rings).

**Standard examples**:
- $\mathrm{Spec}(\mathbb{F}_1) = \{(0)\}$: a single point.
- $\mathrm{Spec}(\mathbb{F}_1[t]) = \{(0), (t)\}$: an "affine line over $\mathbb{F}_1$" with two points (generic + closed at $t = 0$).
- $\mathrm{Spec}(\mathbb{Z})$ is NOT a Deitmar monoid scheme — but the multiplicative monoid $(\mathbb{Z}, \cdot)$ gives a monoid scheme that "sits below" $\mathrm{Spec}(\mathbb{Z})$ in a precise sense (the base-change functor from Deitmar schemes to ordinary schemes sends $\mathrm{Spec}((\mathbb{Z}, \cdot))$ to $\mathrm{Spec}(\mathbb{Z})$).

## 3. The category of Deitmar schemes

**Structure**:
- The category of monoid schemes has all finite limits and colimits (Deitmar 2005).
- Fiber products exist: $\mathrm{Spec}(M) \times_{\mathrm{Spec}(N)} \mathrm{Spec}(P) = \mathrm{Spec}(M \otimes_N P)$ where $\otimes_N$ is the monoid pushout.
- Base change to ordinary schemes: an "extension of scalars" functor $X \mapsto X \otimes_{\mathbb{F}_1} \mathbb{Z}$ sends a monoid scheme to an ordinary scheme over $\mathrm{Spec}(\mathbb{Z})$.

**The crucial fact**: $\mathrm{Spec}(\mathbb{Z}) \times_{\mathrm{Spec}(\mathbb{F}_1)} \mathrm{Spec}(\mathbb{Z})$ in the Deitmar category. Computing:
- "$\mathrm{Spec}(\mathbb{Z})$" in Deitmar's sense is $\mathrm{Spec}((\mathbb{Z}, \cdot))$.
- The fiber product is $\mathrm{Spec}((\mathbb{Z}, \cdot) \otimes_{\mathbb{F}_1} (\mathbb{Z}, \cdot))$.
- The monoid pushout $(\mathbb{Z}, \cdot) \otimes_{\mathbb{F}_1} (\mathbb{Z}, \cdot)$ is computed as the disjoint union of the multiplicative monoids modulo gluing of identities, which simplifies to $(\mathbb{Z}, \cdot)$ itself (since both factors are extensions of $\mathbb{F}_1 = \{0, 1\}$ in the same way).

**So the fiber product is essentially trivial**: $\mathrm{Spec}(\mathbb{Z}) \times_{\mathbb{F}_1} \mathrm{Spec}(\mathbb{Z}) \cong \mathrm{Spec}(\mathbb{Z})$ in Deitmar's framework. This is the "diagonal" — no genuine 2-dimensional surface structure.

This is the structural reason Deitmar can't serve as the basis for an RH proof via Weil's strategy: there is no genuine surface object on which intersection theory could live.

## 4. What Deitmar provides (and what it doesn't)

**Provides**:
- A clean definition of $\mathbb{F}_1$ (as $\{0, 1\}$).
- A category of "$\mathbb{F}_1$-schemes" (monoid schemes).
- Compatibility with ordinary schemes via base change.
- Compatibility with $\mathbb{F}_q$-schemes: $\mathrm{Spec}(\mathbb{F}_q)$ corresponds to $\mathrm{Spec}((\mathbb{F}_q^*, \cdot))$ in Deitmar's framework.
- A precise reduction of "$\mathbb{F}_1$" from philosophical placeholder to rigorous mathematics.

**Does NOT provide**:
- A non-trivial fiber product $\mathrm{Spec}(\mathbb{Z}) \times_{\mathbb{F}_1} \mathrm{Spec}(\mathbb{Z})$ (just gives $\mathrm{Spec}(\mathbb{Z})$ back).
- A cohomology theory rich enough to support infinitely-many zeta zeros.
- A Frobenius substitute (no Adams operations, no flow).
- An intersection theory or Hodge index theorem.

**The structural reason for the limitations**: monoid structure is **too rigid**. By dropping addition entirely, Deitmar loses the ability to construct anything that depends on linear combinations of elements (subschemes defined by polynomial equations involving addition, cohomology theories, etc.).

## 5. Deitmar's interpretation of $\mathbb{F}_1$

In Deitmar's framework, $\mathbb{F}_1$ is **literally** the monoid $\{0, 1\}$. There's no hidden structure, no "field-with-one-element" mystique — just the simplest commutative monoid with absorbing element.

**This is a strength**: the definition is unambiguous, and the category of monoid schemes is precisely defined. No conjectural existence questions.

**This is also a weakness**: the framework is so simple that it has no room for the structure (Frobenius, cohomology, intersection theory) needed to lift Weil's proof.

**Where Deitmar sits among the candidates**:

| Candidate | $\mathbb{F}_1$ realization | Extra structure |
|---|---|---|
| **Deitmar** | Monoid $\{0, 1\}$ | None — pure monoid theory |
| Lorscheid | Blueprint $(\mathbb{F}_1, \mathbb{F}_1^\bullet)$ | Additive relations |
| Borger | $\Lambda$-ring (initial = $\mathbb{Z}$ with $\psi_p = \mathrm{id}$) | Adams operations |
| Connes-Consani | Arithmetic site (topos with hyperring sheaves) | Frobenius endomorphism, topos structure |
| Deninger | (no explicit $\mathbb{F}_1$) | Foliated space + flow |

Deitmar is the categorical floor; subsequent candidates build upward.

## 6. What Deitmar predicts about $\zeta$

**Frobenius substitute** (constraint viii): not provided. Monoid schemes have no notion of Frobenius operator. Without addition, the Frobenius map $x \mapsto x^p$ is just a monoid endomorphism (the $p$-th power map), and its "spectrum" is trivial.

**Cohomology** (constraints iv-vii): there's a "monoid-scheme cohomology" defined via sheaves of monoids, but it's too rigid to support infinite-dimensional spectra. The "Betti numbers" of monoid schemes are typically very small (combinatorial invariants of the underlying poset of prime ideals).

**Euler factors** (constraint x): not provided directly. Monoid schemes don't have an analogue of the local zeta function $Z(X / \mathbb{F}_p, T) = \exp(\sum |X(\mathbb{F}_{p^n})| T^n / n)$ in any non-trivial sense.

**Positivity** (constraints xi-xiii): not provided. No intersection theory means no Hodge index.

**The bottom line**: Deitmar's framework doesn't predict ANYTHING specific about $\zeta$. It provides a category of objects on which "RH-like" questions COULD be asked, but the framework itself doesn't have the machinery to answer them.

## 7. Strengths of the Deitmar framework

1. **Maximal simplicity**: the framework is the simplest possible. Definitions are unambiguous; no conjectural objects.

2. **Foundation for subsequent frameworks**: Lorscheid's blueprints, Borger's $\Lambda$-rings, Connes-Consani's arithmetic site all build on Deitmar's intuition. Understanding Deitmar is the conceptual starting point for the more elaborate candidates.

3. **Clean function-field compatibility**: $\mathbb{F}_q$-schemes embed naturally as Deitmar monoid schemes via the multiplicative monoid $(\mathbb{F}_q^*, \cdot) \cup \{0\}$. The function-field reduction is rigorous.

4. **Compatibility with combinatorial methods**: Deitmar schemes connect naturally to toric geometry, combinatorics of monoid algebras, and related areas (Faltings, Conrad, etc., have developed bridges).

5. **K2 safety**: per [2A_R1_DH_exclusion.md](2A_R1_DH_exclusion.md), Deitmar's framework excludes D-H by construction (linear combinations of Dirichlet L-functions are not monoid-scheme operations).

## 8. Limitations of the Deitmar framework

1. **No genuine surface structure**: $\mathrm{Spec}(\mathbb{Z}) \times_{\mathbb{F}_1} \mathrm{Spec}(\mathbb{Z}) \cong \mathrm{Spec}(\mathbb{Z})$ in the monoid-scheme fiber product. No 2-dimensional object to support intersection theory.

2. **No cohomology rich enough for $\zeta$**: monoid-scheme cohomology is finite-dimensional in the combinatorial sense, can't match the infinite spectrum $\{\gamma_n\}$.

3. **No Frobenius substitute**: monoid endomorphisms exist but have trivial spectrum (essentially permutations of generators).

4. **No predictions about $\zeta$**: the framework is too rigid to make L-function-specific predictions.

5. **Mostly subsumed by later frameworks**: Lorscheid and Borger both contain Deitmar as a subcategory or limit, with additional structure on top. Pure Deitmar offers nothing they don't.

## 9. Active research questions specific to Deitmar (as of ~2025)

- **Bridges to combinatorial geometry**: how does monoid-scheme cohomology relate to combinatorial Hodge theory (Adiprasito-Huh-Katz)? This is a different RH-adjacent question (chromatic polynomials, matroid log-concavity) rather than the zeta RH.
- **Toric / log geometry foundations**: monoid schemes are essentially "toric without group action." Connections to log geometry (Kato, Ogus) are well-developed.
- **As a base for Lorscheid blueprints**: every monoid scheme is a blueprint (with trivial additive relations). Deitmar's framework is the "additive-trivial" subcategory of Lorscheid's blueprints.

Most active Deitmar research is now in directions OTHER than RH (combinatorial Hodge theory, toric geometry, log geometry). The "Deitmar RH program" effectively transitioned into "Lorscheid RH program" via the blueprint generalization.

## 10. Combinability with other candidates

**With Lorscheid (blueprints)**: Lorscheid is the natural extension of Deitmar — every monoid scheme IS a blueprint. The Lorscheid framework subsumes Deitmar's. No information loss going from Deitmar → Lorscheid; substantial structural gain.

**With Borger ($\Lambda$-rings)**: Deitmar's monoid scheme $\mathrm{Spec}((\mathbb{Z}, \cdot))$ does not naturally carry $\Lambda$-ring structure (no Adams operations on the bare multiplicative monoid). However, Borger's $\Lambda$-ring $\mathbb{Z}$ has a forgetful map to the multiplicative monoid $(\mathbb{Z}, \cdot)$, giving a comparison functor. The two frameworks are largely independent (each has its own $\mathbb{F}_1$ candidate); a combined "Deitmar + Borger" doesn't gain over either alone.

**With Connes**: Deitmar's monoid schemes don't naturally embed into Connes' noncommutative-geometric machinery. The "arithmetic site" (Connes-Consani) is closer to a topos-theoretic version of Lorscheid's blueprints than to Deitmar's monoid schemes.

**With Deninger**: no natural combination. Deitmar's framework has no dynamical structure for Deninger's flow to act on.

## 11. Open scorecard for Deitmar (post-R1)

Updated based on R1 findings:

| Constraint | Status | What's needed to close |
|---|---|---|
| (i) | ✅ | — (done: $\mathbb{F}_1 = \{0, 1\}$ explicit) |
| (ii) | 🟡 | Fiber product exists but gives back $\mathrm{Spec}(\mathbb{Z})$; not a genuine surface. Upgrade requires adding addition (= moving to Lorscheid blueprints). |
| (iii) | ✅ | $\mathbb{F}_q$-schemes embed correctly. |
| (iv) | ❌ | Monoid-scheme cohomology too rigid; no infinite-spectrum analog. |
| (v) | ❌ | No cohomology, no Poincaré duality. |
| (vi) | ❌ | No cycle class, no intersection theory. |
| (vii) | ❌ | No Künneth for the relevant cohomology. |
| (viii) | ❌ | No Frobenius substitute. Monoid endomorphisms have trivial spectrum. |
| (ix) | ❌ | No Lefschetz formula. |
| (x) | ❌ | No per-prime Euler factor mechanism. |
| (xi) | ❌ | No intersection theory, no Hodge index. |
| (xii) | ❌ | Same as (xi). |
| (xiii) | ❌ | Same as (xi). |
| (xiv) | ✅ | Function-field reduction works correctly via $\mathbb{F}_q^*$-monoid embedding. |
| (xv) | ❌ | Dirichlet L-functions not naturally encoded. |
| (xvi) | ❌ | No engagement with Selberg class. |
| (xvii) | ✅ | R1: D-H excluded by construction (no monoid-scheme operation produces linear combinations of Dirichlet series). |

Three ✅, one 🟡, no ⏳, 13 ❌.

**Decisive blocker**: everything except the foundational compatibility statements (i, iii, xiv, xvii). The framework provides almost no machinery beyond the categorical foundation.

## 12. Bottom line on Deitmar

**Best aspect**: rigorous, unambiguous, minimal. Provides the cleanest possible answer to "what is $\mathbb{F}_1$?" — and that answer is "a monoid." This is the conceptual starting point for $\mathbb{F}_1$-geometry.

**Worst aspect**: too simple to do anything. The framework provides $\mathbb{F}_1$ as a category but doesn't provide the cohomology, Frobenius substitute, or intersection theory needed for an RH proof. It's a foundation, not a building.

**Most likely path forward**: ABANDON the Deitmar-only RH program; it has no path forward by itself. Use Deitmar as the foundation for Lorscheid blueprints (which add additive relations) or compose with other frameworks (Borger's $\Lambda$-rings) to gain the needed structure.

**The historical role**: Deitmar (2005) was foundational because it established that "$\mathbb{F}_1$" could be rigorously defined at all. Subsequent frameworks (Lorscheid 2012, Connes-Consani 2009, Borger 2009) all benefit from Deitmar's having made the existence question tractable. But the Deitmar RH program itself transitioned into successor programs by ~2012.

**Cross-cut to other candidates**: Deitmar is to Arch 2 what Berry-Keating (1A) is to Arch 1 — the simplest possible construction that nominally addresses the question but lacks the structure for an actual proof. Both are pedagogical anchors but neither is a real RH-proof candidate.

## References (Deitmar-specific)

- Deitmar, A. (2005). *Schemes over $\mathbb{F}_1$*. Number Fields and Function Fields — Two Parallel Worlds, Progr. Math. 239, 87–100. The founding paper.
- Deitmar, A. (2006). *$\mathbb{F}_1$-schemes and toric varieties*. Beiträge Algebra Geom. 49(2), 517–525.
- Deitmar, A. (2008). *Remarks on zeta functions and K-theory over $\mathbb{F}_1$*. Proc. Japan Acad. Ser. A Math. Sci. 82(8), 141–146.
- Connes, A.; Consani, C. (2009). *Schemes over $\mathbb{F}_1$ and zeta functions*. Compositio Math. 146, 1383–1415. Compares Deitmar to other $\mathbb{F}_1$ approaches.
- Lorscheid, O. (2012). *The geometry of blueprints, Part I*. Adv. Math. 229, 1804–1846. The natural extension of Deitmar's monoid schemes.
- Adiprasito, K.; Huh, J.; Katz, E. (2018). *Hodge theory for combinatorial geometries*. Ann. of Math. 188(2), 381–452. A combinatorial Hodge index theorem that has been compared to the Deitmar setting (but for chromatic polynomials, not $\zeta$).
- Soulé, C. (2004). *Les variétés sur le corps à un élément*. Mosc. Math. J. 4(1), 217–244. An alternative early $\mathbb{F}_1$ approach predating Deitmar.
- Pena, J.; Lorscheid, O. (2011). *Mapping $\mathbb{F}_1$-land: An overview of geometries over the field with one element*. arXiv:0909.0069. Comparative survey across $\mathbb{F}_1$ approaches.
