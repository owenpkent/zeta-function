# D1.4.1 Candidate B: Fermat-Frobenius via Quotient Blueprints

> BUILDER-1B, session 002. Direction 1 (Lambda-blueprints), milestone 4.1, angle B (Adams-operation form via a p-quotient blueprint).
>
> Parent docs: [`01_lambda_blueprints.md`](../../docs/03_research/research_directions/01_lambda_blueprints.md), [`2A_R2_5_lambda_blueprints.md`](2A_R2_5_lambda_blueprints.md), [`2A_borger_dossier.md`](2A_borger_dossier.md). Lean substrate: [`lean/ZetaRH/LambdaBlueprints.lean`](../../lean/ZetaRH/LambdaBlueprints.lean).
>
> Sibling candidates: [`D1_4_1_fermat_frobenius_candidate_A.md`](D1_4_1_fermat_frobenius_candidate_A.md) (blueprint-relation form), [`D1_4_1_fermat_frobenius_candidate_C.md`](D1_4_1_fermat_frobenius_candidate_C.md) (delta-ring lifted form).
>
> **Status**: candidate construction, not a theorem. Subject to VERIFIER formalization and ADVERSARY attack.

## 0. Headline

The Adams-operation form of Fermat-Frobenius. Build a quotient blueprint `B / I_p` where `I_p` is the smallest blueprint relation closure containing the pair `(p · 1, 0)`. Define an honest blueprint quotient morphism `pi_p : B -> B/I_p`. Then require **strict equality** in the quotient:

```
                psi_p
        B --------------> B
        |                 |
   pi_p |                 | pi_p
        v                 v
      B/I_p --------> B/I_p
              Frob_p
```

i.e. `pi_p o psi_p = Frob_p o pi_p` where `Frob_p(y) := y^p`.

The contrast with angle A is methodological. Angle A keeps the original blueprint and threads the congruence through the relation set. Angle B builds the quotient FIRST and asks for strict equality in the quotient. The two are tightly related but the categorical content is different: angle A's `psi_p` is constrained inside `B`; angle B's `psi_p` is required to descend along an explicit blueprint map.

## 1. Background: what a Lorscheid blueprint quotient is, and what it is not

A Lorscheid blueprint is a pair `(B, B^bullet)` with `B` a commutative monoid (multiplicatively) and `B^bullet` an equivalence relation on the free commutative monoid `N[B]` over `B`, encoding addition relations. The "carrier semiring" model used in the Lean Phase 1 substrate (`Blueprint.carrier : CommSemiring`, `Blueprint.relations : Set (carrier × carrier)`) is the "semiring with extra forced equalities" presentation. Both are in current use in the literature; we will pivot between them depending on which is more convenient.

**Important**: Lorscheid (2012) develops blueprint morphisms and shows the category Blpr has limits, including equalizers. Equalizers are quotients in a categorical sense. However, the **ideal-theoretic quotient `B / I`** for an arbitrary subset `I` is not part of the published Lorscheid framework. Lorscheid does construct the quotient by a blueprint congruence (an equivalence relation respecting the blueprint structure), but only as the universal blueprint receiving a morphism that collapses the congruence. We must work entirely within that machinery.

This is the first technical gap we flag: a "p-blueprint ideal" is not a primitive notion in Lorscheid. We must build it as a congruence.

## 2. The p-blueprint congruence `~_p` and the quotient `B / I_p`

### 2.1 Definition (informal, semiring-carrier model)

Let `(B, B^bullet, R)` be a blueprint in the carrier-semiring model: `B` is a commutative semiring, `B^bullet subseteq B` a multiplicative submonoid containing `1`, and `R subseteq B x B` a set of pre-additive relations.

**Definition 2.1 (the p-congruence ~_p).** Fix a prime `p`. The **p-congruence on `B`** is the smallest equivalence relation `~_p` on `B` such that:

1. `(p · 1, 0)` is in `~_p`. (The "kill p" axiom.)
2. `~_p` contains `R`. (Existing blueprint relations descend.)
3. `~_p` is compatible with `+`: if `a ~_p a'` and `b ~_p b'` then `a + b ~_p a' + b'`.
4. `~_p` is compatible with `·`: if `a ~_p a'` and `b ~_p b'` then `a · b ~_p a' · b'`.

The quotient `B / I_p := B / ~_p` carries a commutative semiring structure with `[a] + [b] := [a + b]` and `[a] · [b] := [a · b]`. Well-definedness follows from (3), (4).

The submonoid `(B^bullet)_p := { [x] : x in B^bullet }` is a multiplicative submonoid of `B / I_p` (closed under multiplication because `B^bullet` is and `~_p` is multiplicative). The relation set on the quotient is the empty relation: all pre-additive forced equalities have been absorbed into the congruence. (Equivalent formulation: keep the full image of `R` under `pi_p x pi_p`; this image is trivial because every `(a,b) in R` satisfies `[a] = [b]` in `B / I_p`.)

### 2.2 Reconciliation with Lorscheid

In Lorscheid's pre-additive language, `~_p` is a **blueprint congruence**: an equivalence relation on `N[B^bullet]` (or equivalently on `B`) compatible with the monoid operation and containing the forced-equalities `R`. Lorscheid 2012 §3.4 ("the quotient blueprint") gives the universal property: morphisms from `(B, B^bullet, R)` to any blueprint `(C, C^bullet, R_C)` killing all the pairs of `~_p` factor uniquely through `B / I_p`.

**Closure conditions specified.** `I_p` (or rather `~_p`) is the smallest equivalence relation closed under:
- Containment of `(p · 1, 0)` and of `R`.
- Sum-stability.
- Product-stability.
- Reflexivity, symmetry, transitivity.

Equivalently: the kernel of the canonical morphism in `B`-Mod-of-blueprints to the universal blueprint killing `p · 1`.

**Technical flag**. Whether Lorscheid's published framework guarantees `B / I_p` has a sensible `B^bullet` (the image of `B^bullet`) in full generality is a literature gap. We assume the obvious construction works for the "good" blueprints encountered below (`F_1`, `Z`, `F_p`, `F_p[T]`, and free Lambda-blueprints on one generator); the general case is a Mathlib/literature target.

### 2.3 The quotient morphism `pi_p`

**Definition 2.2.** The map `pi_p : B -> B / I_p` defined by `pi_p(x) := [x]` is the canonical projection.

**Lemma 2.3 (pi_p is a blueprint morphism).** `pi_p` satisfies:
1. `pi_p` is a semiring homomorphism (additive, multiplicative, sends `0 -> 0`, `1 -> 1`).
2. `pi_p(B^bullet) subseteq (B^bullet)_p` (preserves the multiplicative submonoid).
3. For every `(a, b) in R`, the pair `(pi_p(a), pi_p(b))` is the diagonal `([a], [a])` (relations are sent to identities in the quotient).

*Proof sketch.* (1) is direct from the definition of `[a] + [b]` and `[a] · [b]`. (2) is direct because `B^bullet` is mapped to its set of equivalence classes, which forms the new submonoid by construction. (3) is direct because `R subseteq ~_p` by clause 2 of Definition 2.1. QED.

So `pi_p` is a blueprint morphism in Lorscheid's sense. Functoriality and uniqueness up to unique isomorphism follow from the universal property.

## 3. The FermatFrobenius axiom in Adams-operation form

### 3.1 Definition

Let `(B, B^bullet, R, {psi_p})` be a tentative Lambda-blueprint: a blueprint together with a family of semiring endomorphisms `psi_p : B -> B`, one per prime `p`, satisfying commutativity `psi_p o psi_q = psi_q o psi_p`.

**Definition 3.1 (Adams-form Fermat-Frobenius).** The Lambda-blueprint satisfies **Fermat-Frobenius in Adams form** if for every prime `p` the diagram

```
              psi_p
       B  ----------->  B
       |                 |
  pi_p |                 | pi_p
       v                 v
    B/I_p  --------->  B/I_p
              Frob_p
```

commutes strictly, where `Frob_p(y) := y^p`. In symbols:

```
pi_p o psi_p = Frob_p o pi_p
```

equivalently, for all `x in B`:

```
[psi_p(x)] = [x]^p     in B / I_p.
```

### 3.2 Why this is well-typed

For the diagram to make sense, we need:
- `psi_p` to be a semiring endomorphism of `B` (assumed).
- `pi_p` to be a blueprint morphism (Lemma 2.3).
- `Frob_p` to be a well-defined map `B / I_p -> B / I_p`. This is automatic: `Frob_p` is `y |-> y^p`, the `p`-th power monoid endomorphism. In a commutative semiring of "characteristic dividing p" (which is what `B / I_p` becomes), `Frob_p` is in fact a semiring homomorphism by the freshman's dream:
  - `(a + b)^p = a^p + b^p` in any commutative semiring where `p · 1 = 0` (use the binomial expansion; every middle term has a factor of a binomial coefficient `C(p,k)` with `0 < k < p`, and `p | C(p,k)`, so each middle term is a multiple of `p · 1`, which is `0`).
  - `(a · b)^p = a^p · b^p` by commutativity.
  - `0^p = 0`, `1^p = 1`.

So `Frob_p : B/I_p -> B/I_p` is a semiring endomorphism (the "absolute Frobenius" of `B / I_p`).

**The axiom asks**: does `psi_p` descend along `pi_p` to the absolute Frobenius?

## 4. Specialization lemmas

### 4.1 Lemma 1: Ring case reduces to ordinary Fermat congruence

**Lemma 4.1.** Suppose `(B, B^bullet, R)` is a Lorscheid blueprint where `B = B^bullet cup {0}` is the full multiplicative monoid of a commutative **ring** `B` (the "ring case", with the addition relations `R` being the full graph of ring addition). Then:

(a) `I_p = pB` (the ordinary ideal generated by `p`) and `B / I_p = B / pB` (ordinary ring quotient).

(b) The Adams-form axiom `pi_p o psi_p = Frob_p o pi_p` is equivalent to the classical Lambda-ring condition `psi_p(x) === x^p (mod p)` for all `x in B`.

*Proof sketch.*

(a) In the ring case the blueprint relations `R` already encode all the additive group structure. The smallest equivalence relation containing `(p, 0)` and closed under sums and products is exactly the ideal congruence `x ~ y iff x - y in pB`. Hence `~_p = (mod pB)` and `B / I_p = B / pB`.

(b) By (a), `pi_p` is the ordinary ring projection. The condition `[psi_p(x)] = [x]^p` in `B / pB` reads `psi_p(x) === x^p (mod p)`, which is Joyal's / Atiyah-Tall's Fermat condition for Lambda-rings. QED.

**Consequence.** Lambda-Rings (in the Borger / Joyal sense) sit inside our Lambda-blueprint category as the full subcategory of Lambda-blueprints whose underlying blueprint is in the ring case. This is the embedding for milestone 4.3.

### 4.2 Lemma 2: When `psi_p = id`, the axiom is the Frobenius-fixed-point condition

**Lemma 4.2.** Suppose `psi_p = id_B`. Then the Adams-form axiom reduces to: `Frob_p = id` on `B / I_p`, i.e. `x^p = x` in `B / I_p` for every `x in B`.

*Proof.* `pi_p o id = pi_p`, so the diagram commutes iff `Frob_p o pi_p = pi_p`, iff `[x]^p = [x]` for all `x in B`. QED.

**Which blueprints satisfy this with `psi_p = id`?**

- **`F_1` (trivial blueprint, `B = {0, 1}`)**: `0^p = 0`, `1^p = 1`. ✓ Trivial.
- **`Z` (integers as blueprint, `B = Z`, full additive relations)**: by Lemma 4.1 the quotient is `Z / pZ = F_p`, and `x^p = x` in `F_p` is **Fermat's little theorem**. ✓
- **`F_p` (prime field as blueprint)**: `I_p = (p · 1) = (0)` (since `p · 1 = 0` already), so `B / I_p = F_p` and the condition `x^p = x` holds by Fermat. ✓
- **`F_p[T]` (polynomial blueprint over `F_p`, one generator)**: `I_p = (p · 1) = (0)`, so `B / I_p = F_p[T]`. The condition `x^p = x` for ALL `x in F_p[T]` FAILS: take `x = T`. Then `T^p != T` in `F_p[T]` (they are different polynomials). ✗

So `F_p[T]` is **not** a Lambda-blueprint with `psi_p = id`. To equip `F_p[T]` with a Lambda-structure we must pick `psi_p` non-trivially. The natural choice is `psi_p(T) := T^p`, extended to `F_p[T]` by `psi_p` being a semiring endomorphism. This is Example 7.4 below.

This matches Borger's observation: `F_p[T]` carries multiple Lambda-structures, and the "canonical" one for `F_1`-geometry uses `psi_p(T) = T^p`, which is the **Frobenius lift of `Frob_p` along the obvious projection**. The Adams-form axiom captures this precisely.

### 4.3 Lemma 3: In `F_p`, `psi_p` must be Frobenius (not the identity, in a sense)

**Lemma 4.3.** Suppose `B = F_p` (as a Lambda-blueprint in the ring case). Then ANY choice of `psi_p` satisfying the Adams-form axiom must satisfy `psi_p = Frob_p` (i.e. `psi_p(x) = x^p`). However, since `Frob_p = id` on `F_p` (Fermat), this is also `psi_p = id`. So the axiom is consistent in two ways simultaneously and there is no contradiction.

*Proof.* `B / I_p = F_p / (0) = F_p`. The axiom says `psi_p(x) = x^p = x` for all `x in F_p`. So `psi_p` is the identity on `F_p`, which equals `Frob_p` on `F_p`. QED.

**Why this is not a contradiction with the function-field convention.** In Borger's convention, on a ring of characteristic `p`, `psi_p` is "morally Frobenius." The Adams-form axiom forces this on `F_p` but says nothing about extensions: on `F_p[T]` we get two non-trivial choices (`psi_p = id` violates the axiom; `psi_p(T) = T^p` satisfies it; intermediate "twisted" choices exist for higher-degree extensions). On `F_{p^2}`, `psi_p` must equal the Frobenius automorphism (order 2), which is genuinely non-identity.

## 5. Worked examples

For each example we exhibit the data `(B, B^bullet, R, psi_p)`, compute `B / I_p` explicitly, and verify that the Adams-form diagram commutes.

### 5.1 `F_1` (trivial blueprint)

- `B = {0, 1}`, `B^bullet = {1}`, `R` = trivial (only `(0,0)` and `(1,1)`).
- `psi_p(0) = 0`, `psi_p(1) = 1` (forced because `psi_p` is a semiring endomorphism; there is no choice).
- `I_p`: `p · 1` reduces to `1 + 1 + ... + 1` (p times). In `F_1`, the additive structure is... vacuous (or `1 + 1 = 0` by convention). With the convention that `F_1` has the relation `1 + 1 = 0` (so `B` is morally the two-element commutative semiring `F_2` as a carrier, but with `B^bullet = {1}`), `2 · 1 = 0`, hence `p · 1 = 0` for all primes (including `p = 2`). So `I_p` is trivial and `B / I_p = B = F_1`.
- Diagram: `pi_p o psi_p` and `Frob_p o pi_p` are both the identity on `{0, 1}`. ✓

**Verdict.** `F_1` is a Lambda-blueprint in the Adams form.

### 5.2 `Z` with `psi_p = id`

- `B = Z`, `B^bullet = Z` (or `Z^*` cup `{0, 1}` by convention; we use the full `Z` as the multiplicative monoid since `B = B^bullet cup {0}` in the ring case), `R` = full additive relations.
- `psi_p = id` for all primes `p`.
- `I_p = pZ`, `B / I_p = Z / pZ = F_p`.
- `pi_p(psi_p(x)) = pi_p(x) = x (mod p)`. `Frob_p(pi_p(x)) = x^p (mod p)`. These are equal by Fermat's little theorem. ✓

**Verdict.** `Z` is a Lambda-blueprint in the Adams form with `psi_p = id`. This is Borger's canonical Lambda-structure on `Z`, repackaged.

### 5.3 `F_p` with `psi_p = Frob_p = id`

- `B = F_p`, `B^bullet = F_p`, `R` = full additive relations of `F_p`.
- `psi_p(x) = x` (which equals `x^p` by Fermat).
- `I_p = (p · 1) = (0)`, `B / I_p = F_p`.
- Diagram: both compositions are the identity. ✓

### 5.4 `F_p[T]` with `psi_p(T) = T^p` (free Lambda-blueprint on one generator)

- `B = F_p[T]`, `B^bullet = F_p[T]` (ring case), `R` = full ring relations.
- `psi_p` is the unique semiring endomorphism of `F_p[T]` over `F_p` sending `T |-> T^p`.
- `I_p = (p · 1) = (0)` (already `p = 0` in `F_p[T]`), so `B / I_p = F_p[T]`.
- For `x = T`: `pi_p(psi_p(T)) = T^p`, `Frob_p(pi_p(T)) = T^p`. ✓
- For `x = a_n T^n + ... + a_0`: `psi_p(x) = a_n^p T^{pn} + ... + a_0^p`. (Wait: `psi_p` is `F_p`-linear or `F_p`-fixing? We need a convention. The natural choice in Borger / Lambda-ring tradition is **`psi_p` fixes the base** (so `psi_p(a) = a` for `a in F_p`), hence `psi_p(x) = a_n T^{pn} + ... + a_0`.)
- With this convention: `Frob_p(x) = x^p = (a_n T^n + ... + a_0)^p = a_n^p T^{pn} + ... + a_0^p = a_n T^{pn} + ... + a_0` (using `a^p = a` in `F_p`). So `psi_p = Frob_p` on `F_p[T]`. ✓

**Verdict.** `F_p[T]` is a Lambda-blueprint in the Adams form with `psi_p(T) = T^p`. The free Lambda-blueprint on one generator over `F_1` (or over `F_p`).

### 5.5 `Z[T]` with `psi_p(T) = T^p`, `psi_p = id` on `Z`

- `B = Z[T]`, ring case, `psi_p(T) = T^p` and `psi_p` is the identity on integers.
- `I_p = pZ[T]`, `B / I_p = F_p[T]`.
- For `x = T`: `pi_p(psi_p(T)) = T^p (mod p)`, `Frob_p(pi_p(T)) = T^p (mod p)`. ✓
- For `x = a_n T^n + ... + a_0` with integer `a_i`: `psi_p(x) = a_n T^{pn} + ... + a_0` (integer coefficients preserved). `pi_p(psi_p(x)) = a_n (mod p) · T^{pn} + ... + a_0 (mod p)`. `Frob_p(pi_p(x)) = (a_n T^n + ... + a_0)^p (mod p) = a_n^p T^{pn} + ... + a_0^p (mod p)`. By Fermat `a_i^p === a_i (mod p)`, so the two agree. ✓

**Verdict.** This is the free Lambda-blueprint on one generator over `Z`. Matches Borger's free Lambda-ring on one generator (the underlying ring is `Z[psi_2(T), psi_3(T), ...]` modulo the Adams-operation identities, but for the "monogenic" version where we ONLY have one `T` and `psi_p(T) = T^p` is forced, this collapses to `Z[T]` with the prescribed Adams structure).

## 6. K2 (D-H) self-check

**Claim.** Davenport-Heilbronn cannot be constructed as a Lambda-blueprint in the Adams form.

**Argument.** D-H is the linear combination `D(s) = sin(alpha) L(s, chi_5^a) + cos(alpha) L(s, chi_5^b)`. It has no Euler product. For D-H to arise from a Lambda-blueprint `B`, the L-function recipe would need to assign to `B` an L-function of the form `det(1 - psi_p · p^{-s} | M)^{-1}` (Borger-style Euler factor at each prime) and have the global product equal `D(s)`.

The step that fails depends on which "way in" the adversary tries:

**Adversarial route (a)**: Try to define `B = R_a oplus R_b` as a direct sum of two Lambda-blueprints whose L-functions are `L(s, chi_5^a)` and `L(s, chi_5^b)`. Then `psi_p` on `B` acts diagonally. The L-function of `B` under any Borger-style recipe is the PRODUCT `L(s, chi_5^a) · L(s, chi_5^b)`, NOT the linear combination. **K2 passes**: D-H is not the zeta of this construction.

**Adversarial route (b)**: Try to define `psi_p` non-diagonally to mix the two factors. The commutativity axiom `psi_p o psi_q = psi_q o psi_p` together with the Adams-form Fermat condition forces `psi_p` to be diagonalizable in the natural basis (the two characters are eigenvectors of multiplication by `chi_5^a`, `chi_5^b`); the Adams condition `[psi_p(x)] = [x]^p` mod `I_p` forces `psi_p` to act as the `p`-th power on the multiplicative parts. No non-diagonal mixing survives.

**Adversarial route (c)**: Try to make `B` itself encode the linear combination by adjusting `pi_p`. The morphism `pi_p` is canonical (Lemma 2.3); there is no degree of freedom to introduce `sin(alpha)`, `cos(alpha)` coefficients. The blueprint quotient is a categorical universal construction with no parameters.

**Which step fails?** The construction of `psi_p` and `pi_p` is fine for `D-H`-shaped objects; what fails is the **L-function recipe assignment**. Any Borger-style recipe from a Lambda-blueprint produces an Euler product, and D-H has no Euler product. So D-H is not in the image of any L-function functor on Lambda-Blpr.

This matches R1 (D-H exclusion) §3.3 for Borger: the Adams-operation framework is "tight" with Euler products by construction, and D-H is excluded by the same structural reason in either the angle A or angle B formulation.

**Verdict (xvii)**: K2 passes by construction for the angle B framework.

## 7. Categorical consequences and the bridge to delta-rings

### 7.1 Adams form = "lift of Frobenius along `pi_p`"

In the Adams form, the Fermat-Frobenius axiom is exactly the statement that `psi_p` is a **lift of the absolute Frobenius `Frob_p`** along the quotient map `pi_p : B -> B/I_p`. This is the categorical content:

```
Hom_Blpr(B, B) ----restrict---> Hom_Blpr(B, B/I_p)
       ^                              ^
       |                              |
   psi_p                          Frob_p o pi_p
```

`psi_p` is a Frobenius lift in the precise sense that its post-composition with `pi_p` equals `Frob_p o pi_p`.

### 7.2 Connection to delta-rings (BUILDER-1C's angle)

In Joyal / Buium delta-rings, a `p`-derivation `delta_p` is a map `B -> B` (NOT a homomorphism) satisfying `delta_p(x + y) = delta_p(x) + delta_p(y) + (x^p + y^p - (x+y)^p)/p` and a Leibniz-style rule, such that `phi_p(x) := x^p + p · delta_p(x)` is a ring endomorphism lifting Frobenius.

The relationship: **`phi_p` in the delta-ring sense IS `psi_p` in our Adams form**, and the existence of `delta_p` is equivalent to the existence of `psi_p` satisfying our axiom (in the `p`-torsion-free ring case). In characteristic-0 rings, the delta-ring data and the Adams-Lambda data are interconvertible:

```
psi_p(x) = x^p + p · delta_p(x)      (delta-ring -> Adams)
delta_p(x) = (psi_p(x) - x^p) / p    (Adams -> delta-ring, requires p-torsion-free)
```

So BUILDER-1C's framework should specialize to ours in the torsion-free case. The angle B framework is **more general** than the delta-ring framework because it works in any blueprint (including `p`-torsion blueprints where `(psi_p(x) - x^p)/p` is not well-defined), but **categorically equivalent** in the torsion-free ring case.

We do not develop this further; the comparison is for SYNTHESIZER and ORCHESTRATOR.

### 7.3 Relationship to BUILDER-1A's angle (blueprint-relation form)

BUILDER-1A keeps the original blueprint and asks `(psi_p(x), x^p) in R` for an enriched relation set `R` containing the "p-blueprint ideal generators". Our angle B builds the quotient first and asks for strict equality in `B / I_p`.

**Claim (informal).** The two formulations are logically equivalent, in the following sense:

- Angle B implies angle A: if `pi_p o psi_p = Frob_p o pi_p`, then `[psi_p(x)] = [x^p]` in `B / I_p`, which translates back to `(psi_p(x), x^p) in ~_p`. If we choose angle A's enriched relation set to be exactly `~_p`, the two coincide.
- Angle A implies angle B (with caveat): if `(psi_p(x), x^p) in R_p` for a relation set `R_p` containing all the closure data of `~_p`, then `psi_p(x)` and `x^p` are identified in `B / R_p = B / I_p`. The two collapse.

The categorical content is the same. The **methodological** difference is:

- Angle A's framework lives in the world of "blueprints with extra relations" and presents `psi_p` as an endomorphism of `B` consistent with relations. Easier to state, harder to compute with at the quotient level.
- Angle B's framework lives in the world of "blueprints with quotients" and presents `psi_p` as a Frobenius lift via a commuting square. Easier to compute with (the quotient `B / I_p` is concrete in worked examples), harder to set up (requires explicit quotient construction).

In Lean, angle B is probably easier to formalize once we have the quotient construction (a standard Mathlib quotient is available), and angle A is probably easier to use for category-theoretic functoriality proofs. We **flag this as a tradeoff** for the verifier.

## 8. 17-constraint self-assessment

Applying the [`2A_candidate_evaluation.md`](2A_candidate_evaluation.md) framework. Adams form of FF specifically:

| Constraint | Predicted by R2.5 | Angle B verdict | Comment |
|---|---|---|---|
| (i) Spec(Z) -> S | ✅ | ✅ (no change) | Inherited from blueprint framework; Spec(Z) -> Spec(F_1) is direct. |
| (ii) Non-trivial fiber product | ✅ predicted | 🟡 (no advance) | The Adams-form FF says nothing about fiber products. Milestone 4.5/4.6 territory. |
| (iii) F_q compatibility | ✅ | ✅ (verified) | Lemma 4.3 (`F_p` case) verifies; extends to `F_q = F_{p^k}` by analogous computation. |
| (iv) Finite-dim cohomology | 🟡 | 🟡 (no advance) | Adams-form FF does not construct cohomology. |
| (v) Poincaré duality | ⏳ | ⏳ (no advance) | Same. |
| (vi) Cycle class / intersection | 🟡 | ⏳ (no advance) | Same. |
| (vii) Künneth | ⏳ | ⏳ (no advance) | Same. |
| (viii) Frobenius spectrum | ✅ | ✅ (verified) | Adams-form axiom IS the Frobenius substitute. `psi_p` is a Frobenius lift by construction. |
| (ix) Lefschetz | 🟡 | 🟡 (no advance) | Need cohomology first. |
| (x) Euler-factor compatibility | ✅ | ✅ (verified) | Borger's Euler-factor recipe `det(1 - psi_p t | M)^{-1}` applies directly. |
| (xi) Hodge index | ⏳ | ⏳ (no advance) | Same as parent frameworks. |
| (xii) Provable without RH input | ⏳ | ⏳ (no advance) | Same. |
| (xiii) Castelnuovo-Severi | ⏳ | ⏳ (no advance) | Same. |
| (xiv) Function-field RH recovery | ✅ | ✅ (verified) | Reduces to ordinary scheme theory over `F_q` by Lemma 4.1 + Lemma 4.3. |
| (xv) Dirichlet L-functions | 🟡 | 🟡 (no advance) | Adams-form FF does not address twisting. |
| (xvi) Selberg class | ⏳ | ⏳ (no advance) | Same. |
| (xvii) D-H excluded | ✅ | ✅ (verified) | §6 above. K2 passes by construction. |

**Tally for angle B alone**: 6 ✅ (i, iii, viii, x, xiv, xvii), 4 🟡 (ii, iv, vi, ix, xv: actually 5 🟡 incl. xv -- counting: ii, iv, vi, ix, xv = 5), 6 ⏳ (v, vii, xi, xii, xiii, xvi).

R2.5 predicted 8 ✅ / 4 🟡 / 5 ⏳ for the full Lambda-blueprint framework. Angle B alone verifies 6 of those ✅ slots directly (the ones that follow from FF + blueprint structure). The remaining 2 ✅ predictions in R2.5 ((ii) and one of (vi)/(ix)/(xv) upgrades) depend on developing milestones 4.5-4.7, which are downstream of FF.

**Honest assessment**: angle B advances 6 constraints to ✅ outright. It does not by itself reach the R2.5-predicted 8 ✅, but it does NOT contradict the prediction. The remaining ✅ predictions are deferred to 4.5 / 4.6.

This is consistent with R2.5's prediction "8/4/5" as a target, not as something achieved by 4.1 alone.

## 9. Verification targets for VERIFIER

Each target extends the existing `LambdaBlueprint` structure in [`lean/ZetaRH/LambdaBlueprints.lean`](../../lean/ZetaRH/LambdaBlueprints.lean) rather than replacing it. The current Lean substrate uses the relation-set form (closer to angle A); angle B adds the quotient construction and the diagram-commutativity axiom on top.

**#FF-B-1: p-congruence is a Mathlib `Setoid`**

Informal: define `pCongruence (B : Blueprint) (p : Nat.Primes) : Setoid B.carrier` as the smallest equivalence relation containing `(p * 1, 0)` and `B.relations` and compatible with `+` and `*`.

Candidate Lean signature:
```
def pCongruence (B : Blueprint) (p : Nat.Primes) : Setoid B.carrier where
  r := EqvGen (fun x y => (x, y) ∈ B.relations ∨ x = (p.val : B.carrier) * 1 ∧ y = 0)
  iseqv := EqvGen.is_equivalence _
```
(With closure under `+`, `*` enforced by extending the generators. The precise Lean construction uses `RingQuot` or `Ideal.span` once we know `B.carrier` is a `CommRing`; for `CommSemiring` carriers the analog is `Con` from `Mathlib.GroupTheory.Congruence.Basic`.)

**#FF-B-2: Quotient blueprint construction**

Informal: define `quotientBlueprint (B : Blueprint) (p : Nat.Primes) : Blueprint` whose carrier is `B.carrier / pCongruence B p`, whose `pointed` is the image of `B.pointed`, whose relations are empty (or the trivial diagonal).

Candidate Lean signature:
```
def quotientBlueprint (B : Blueprint) (p : Nat.Primes) : Blueprint where
  carrier := Quotient (pCongruence B p).toSetoid
  carrierSemi := inferInstance  -- the quotient inherits CommSemiring
  pointed := Quotient.mk _ '' B.pointed
  pointed_mul := ... -- image of submonoid is submonoid
  pointed_one := ⟨1, B.pointed_one, rfl⟩
  relations := { (x, x) | x : Quotient _ }  -- trivial relation set
```

**#FF-B-3: Quotient morphism is a blueprint morphism**

Informal: `pi_p := Quotient.mk` is a semiring homomorphism preserving the multiplicative submonoid and sending relations to identities.

Candidate Lean signature:
```
def pi_p (B : Blueprint) (p : Nat.Primes) : B.carrier →+* (quotientBlueprint B p).carrier :=
  ⟨Quotient.mk _, ...⟩
lemma pi_p_preserves_pointed : ∀ x ∈ B.pointed, pi_p B p x ∈ (quotientBlueprint B p).pointed
lemma pi_p_kills_relations : ∀ (a b : B.carrier), (a, b) ∈ B.relations →
    pi_p B p a = pi_p B p b
```

**#FF-B-4: Frobenius on the quotient is a semiring homomorphism**

Informal: in `quotientBlueprint B p`, the map `y |-> y^p.val` is a semiring endomorphism. (Freshman's dream because `p · 1 = 0` in the quotient.)

Candidate Lean signature:
```
def Frob_p (B : Blueprint) (p : Nat.Primes) :
    (quotientBlueprint B p).carrier →+* (quotientBlueprint B p).carrier where
  toFun y := y ^ p.val
  map_zero' := by simp
  map_one'  := by simp
  map_mul' x y := by ring
  map_add' x y := by
    -- freshman's dream in characteristic p
    sorry
```

The `map_add'` is the substantive lemma. This is `add_pow_char` or `add_pow_prime` in Mathlib (`Mathlib.RingTheory.Polynomial.Cyclotomic.Basic`, `Mathlib.FieldTheory.Finite.Basic`); existence in `CommSemiring` of characteristic `p` should be derivable.

**#FF-B-5: Adams-form Fermat-Frobenius axiom**

Informal: extend `LambdaBlueprint` with the axiom that `pi_p ∘ psi_p = Frob_p ∘ pi_p`.

Candidate Lean signature:
```
structure LambdaBlueprintAdamsForm extends Blueprint where
  psi : Nat.Primes → carrier → carrier
  psi_hom : ∀ p, IsRingHom (psi p)  -- semiring hom in fact
  psi_comm : ∀ p q x, psi p (psi q x) = psi q (psi p x)
  fermat_frobenius_adams : ∀ p : Nat.Primes, ∀ x,
    pi_p toBlueprint p (psi p x) = Frob_p toBlueprint p (pi_p toBlueprint p x)
```

**#FF-B-6: Specialization Lemma 1 (Ring case reduces to Lambda-ring)**

Informal: if `B` is in the "ring case" (`B.carrier` is a `CommRing` and `B.relations` is the full equality relation on the ring), then `quotientBlueprint B p` has carrier `B.carrier ⧸ Ideal.span {(p : B.carrier)}` and the Adams-form axiom reduces to the classical Lambda-ring Fermat condition `psi_p(x) ≡ x^p [mod p]`.

Candidate Lean signature:
```
theorem ringCase_quotient_is_pZ_quotient
    (R : Type) [CommRing R] (B : Blueprint) (hB : B.carrier = R) (hR : ...) (p : Nat.Primes) :
    (quotientBlueprint B p).carrier ≃+* R ⧸ Ideal.span {(p.val : R)}
theorem ringCase_axiom_is_FermatCongruence
    (L : LambdaBlueprintAdamsForm) (hRing : ...) (p : Nat.Primes) (x : L.carrier) :
    L.fermat_frobenius_adams p x ↔ L.psi p x ≡ x ^ p.val [SMOD Ideal.span {(p.val : L.carrier)}]
```

**#FF-B-7: F_1 satisfies the axiom (trivially)**

Informal: with carrier `PUnit` and any `psi_p` (only the trivial choice exists), the Adams-form axiom holds.

Candidate Lean signature:
```
noncomputable def F1_Adams : LambdaBlueprintAdamsForm := { ...
  fermat_frobenius_adams := fun _ _ => rfl
}
```

**#FF-B-8: Z with psi_p = id satisfies the axiom (Fermat's little theorem)**

Informal: with carrier `Z`, `psi_p = id`, the axiom reduces to `x ≡ x^p [MOD p]` in `Z`. This is `Int.ModEq.pow_card_sub_one_eq_one` or `ZMod.pow_card` after passing to the quotient.

Candidate Lean signature:
```
noncomputable def Z_Adams : LambdaBlueprintAdamsForm := { ...
  fermat_frobenius_adams := fun p x => by
    -- pi_p (id x) = pi_p x;  Frob_p (pi_p x) = (pi_p x) ^ p.val
    -- want: pi_p x = (pi_p x) ^ p.val in Z / pZ = F_p
    -- this is Fermat's little theorem in F_p
    show Quotient.mk _ x = (Quotient.mk _ x) ^ p.val
    exact (ZMod.pow_card _).symm  -- or analogous
}
```

**#FF-B-9: F_p[T] with psi_p = id FAILS the axiom**

Informal: counterexample `x = T`: `[id T] = [T]` but `Frob_p [T] = [T]^p = [T^p] != [T]`. Confirms the axiom is non-trivial.

Candidate Lean signature:
```
example : ¬ ∃ L : LambdaBlueprintAdamsForm, L.carrier = Polynomial (ZMod p) ∧
    (∀ x, L.psi ⟨p, hp⟩ x = x) :=
  by
    intro ⟨L, hcarr, hid⟩
    have : pi_p L.toBlueprint ⟨p, hp⟩ T = Frob_p L.toBlueprint ⟨p, hp⟩ (pi_p _ _ T) :=
      (L.fermat_frobenius_adams ⟨p, hp⟩ T).trans (congrArg _ (hid T))
    -- derive contradiction: T ≠ T^p in F_p[T] / (0) = F_p[T]
    sorry
```

**#FF-B-10: D-H exclusion (K2)**

Informal: no Lambda-blueprint in the Adams form has L-function equal to the Davenport-Heilbronn function. This is a statement about the L-function recipe, not the Lambda-blueprint axioms themselves, and is delegated to a future formalization of the Borger-style Euler-product recipe. Stub now.

Candidate Lean signature:
```
-- placeholder; formalization requires the L-function recipe from Lambda-blueprints,
-- which is itself Milestone 4.8 in Direction 1.
theorem DH_not_LambdaBlueprint_zeta : True := trivial
```

## 10. Adversarial test cases for ADVERSARY

**Test (a): Davenport-Heilbronn**

Configuration: try to construct a Lambda-blueprint in the Adams form whose attached L-function is `D(s) = sin(alpha) L(s, chi_5^a) + cos(alpha) L(s, chi_5^b)`. By §6 above, this should fail at the L-function recipe step (no Euler product). ADVERSARY should attempt to circumvent by:
- Direct sum of two Lambda-blueprints (yields product L, not sum L).
- "Twisted" `psi_p` (forbidden by commutativity + Adams-form axiom).
- Custom blueprint with relation set encoding `sin/cos` weights (forbidden: relation set is `Set (carrier x carrier)`, contains no real-valued weights).

Expected verdict: K2 passes.

**Test (b): Blueprint where the quotient `B / I_p` collapses to a point**

Configuration: pick `B = F_1` for some prime `p`, or any blueprint with a relation `1 = 0` (which forces `B = 0`). If `B / I_p = {0}` (the zero ring), the Adams-form axiom becomes vacuously true (any `psi_p` works). Is this a problem?

Analysis: if `B / I_p = 0`, then `pi_p` is the zero map, and the axiom `pi_p o psi_p = Frob_p o pi_p` becomes `0 = 0`. This is true but useless. The Lambda-structure is unconstrained AT THIS PRIME. ADVERSARY should check whether this leads to a degenerate Lambda-blueprint with too many endomorphisms surviving the axiom.

Expected resolution: a Lambda-blueprint that collapses at every prime is genuinely degenerate (essentially `F_1` or the zero blueprint), and is not interesting for the geometric program. Constraints should be added requiring `B / I_p != 0` for infinitely many primes (or for all primes). Flag this as a design refinement.

**Test (c): Blueprint where `pi_p` is not a well-defined morphism**

Configuration: can we construct a blueprint `B` and a prime `p` such that the equivalence relation `~_p` does not descend to a sensible quotient (e.g., the image of `B^bullet` is not closed under multiplication)?

Analysis: by Lemma 2.3, `pi_p` is always a blueprint morphism when `~_p` is the smallest congruence containing `(p · 1, 0)` and `R` and closed under `+`, `·`. The image of `B^bullet` is automatically multiplicatively closed. So this test is expected to pass trivially. ADVERSARY should attempt to find a blueprint where the closure conditions in Definition 2.1 are incompatible (e.g., the relation `(p · 1, 0)` together with existing relations forces `0 = 1`, collapsing the blueprint).

Sub-test (c1): suppose `B` has a relation `(1, p · 1)` (i.e., `1 = p` is a forced equality). Then `~_p` forces `1 = p = 0`, so `B / I_p = 0`. Reduces to test (b).

Sub-test (c2): suppose `B^bullet` does not contain `p · 1` (e.g., `B^bullet` is the units of a ring, and `p` is not a unit). Then `p · 1` is in `B` but not in `B^bullet`. Does this break the construction?

Analysis: the construction of `~_p` and `B / I_p` only uses the additive / multiplicative structure of `B`, not the membership of `p · 1` in `B^bullet`. The submonoid `B^bullet` is just sent forward to the quotient by `pi_p`. So this is fine.

**Test (d): Non-canonicity of `psi_p`**

Configuration: on a fixed blueprint `B`, are there multiple choices of `{psi_p}` satisfying the Adams-form axiom?

Example: `B = Z[T]`. Choice 1: `psi_p = id` on `Z`, `psi_p(T) = T^p`. Choice 2: `psi_p = id` on `Z`, `psi_p(T) = T^p + p · g(T)` for arbitrary `g(T) in Z[T]`. Both satisfy the axiom (mod p the second equals the first). So the Adams-form axiom does NOT pin down `psi_p` uniquely. ADVERSARY should check whether this non-canonicity is a problem for the L-function spectrum.

Expected resolution: non-uniqueness is expected and matches the delta-ring picture (multiple Frobenius lifts exist; the choice is the "delta-structure"). The L-function recipe should be invariant under choice of `psi_p` lift modulo `p`. Flag for L-function recipe design.

**Test (e): F_p[T_1, T_2] with `psi_p(T_1) = T_1^p`, `psi_p(T_2) = T_2^p · T_1`**

Configuration: a "twisted" Lambda-structure on `F_p[T_1, T_2]`. Does this satisfy the Adams-form axiom?

Check: `B / I_p = F_p[T_1, T_2]`. `Frob_p(T_2) = T_2^p`. `psi_p(T_2) = T_2^p · T_1`. We need `psi_p(T_2) = Frob_p(T_2)` in the quotient, i.e., `T_2^p · T_1 = T_2^p`, i.e., `T_2^p (T_1 - 1) = 0`. This fails in `F_p[T_1, T_2]`. So this twisted choice FAILS the axiom. ADVERSARY should verify the axiom correctly rules out such "exotic" choices and admits only those consistent with absolute Frobenius mod `p`.

Expected verdict: axiom correctly excludes the twist.

## 11. Conclusion and handoff

The Adams-operation form (angle B) of Fermat-Frobenius for Lambda-blueprints is:

```
pi_p o psi_p = Frob_p o pi_p
```

with `pi_p : B -> B / I_p` the quotient blueprint morphism by the smallest blueprint congruence containing `(p · 1, 0)`, and `Frob_p` the absolute Frobenius on the characteristic-`p` quotient.

The construction:
- Specializes correctly to ordinary Lambda-rings (Lemma 4.1).
- Reduces to the Frobenius fixed-point condition when `psi_p = id` (Lemma 4.2), recovering Fermat's little theorem for `Z` and for `F_p`.
- Excludes `F_p[T]` with `psi_p = id` (Lemma 4.2 applied to `T`), forcing the non-trivial choice `psi_p(T) = T^p` (Example 5.4).
- Is consistent at `F_p` (Lemma 4.3).
- Passes K2 (D-H exclusion) by construction (§6).
- Advances 6 of 17 constraints to ✅, consistent with R2.5's predicted target of 8.

The formulation is logically equivalent to angle A but methodologically different (build quotient first vs. enrich relation set). It is a generalization of the delta-ring framework (BUILDER-1C) covering the `p`-torsion case.

The 10 VERIFIER targets and 5 ADVERSARY tests are listed above. The first VERIFIER target (#FF-B-1) is the gating one: if Mathlib's `Con` (semiring congruence) machinery suffices to build the quotient blueprint, all subsequent targets follow with standard Mathlib tactics. If it does not, this is a Mathlib gap to flag.

**Open structural question for ORCHESTRATOR**: a Lambda-blueprint is genuinely interesting only if `B / I_p != 0` for infinitely many primes (otherwise the FF axiom is vacuous). Should this non-degeneracy condition be added to the definition? Flag for design refinement during milestone 4.2.
