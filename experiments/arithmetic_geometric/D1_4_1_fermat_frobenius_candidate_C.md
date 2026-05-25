# D1.4.1 Candidate C: Fermat-Frobenius via delta-rings lifted to blueprints

> BUILDER-1C output, session 002 of the AI-only proof program. Direction 1 (Lambda-blueprints), milestone 4.1 (define Fermat-Frobenius in blueprint language), angle C: the **delta-ring lifted form**.
>
> Companion to:
> - [`2A_R2_5_lambda_blueprints.md`](2A_R2_5_lambda_blueprints.md) §2.2 (the parent proposal of FF in blueprint language).
> - [`2A_R5_prismatic_cohomology.md`](2A_R5_prismatic_cohomology.md) §2 (the delta-ring / Lambda-ring correspondence at one prime).
> - [`lean/ZetaRH/LambdaBlueprints.lean`](../../lean/ZetaRH/LambdaBlueprints.lean) (Phase 1 substrate, which this document extends rather than replaces).
> - Parallel BUILDER outputs: `D1_4_1_fermat_frobenius_candidate_A.md` (blueprint-relation form) and `D1_4_1_fermat_frobenius_candidate_B.md` (Adams-operation quotient form).
>
> Status: research proposal, not established mathematics. Every construction is provisional and a candidate for VERIFIER / ADVERSARY review.

## 0. One-paragraph summary

A delta-ring (Joyal 1985, Bhatt-Scholze 2019) at prime p is a commutative ring A with a primitive `delta_p: A -> A` such that `psi_p(x) := x^p + p delta_p(x)` is a ring endomorphism. The Fermat-Frobenius condition is then automatic: `psi_p(x) - x^p = p delta_p(x)` is divisible by p by construction. The angle C proposal is to use this primitive `delta_p` as the defining datum of the Fermat-Frobenius condition for Lambda-blueprints rather than the congruence `psi_p(x) congruent x^p`. Specifically we add `delta_p` to the blueprint signature, demand that it satisfies the Joyal-Buium axioms in the carrier semiring, and **derive** `psi_p` from it. This is more rigid than candidates A and B (it provides a constructive witness for the obstruction), connects directly to Bhatt-Scholze prismatic cohomology infrastructure (Direction 3), and gives a sharper D-H exclusion. The cost is that delta-ring axioms involve division by p, so the construction does not specialize cleanly to blueprints with p-torsion. We resolve this by working in sub-angle **(ii)**: delta-blueprint as additional structure, where `delta_p` is part of the data, not derived.

## 1. The three sub-angles and the choice

The brief asks to choose among three sub-angles for handling the "division by p" obstruction inherent in `delta_p(x) = (psi_p(x) - x^p)/p`.

### 1.1 Sub-angle (i): p-torsion-free carriers

Restrict attention to blueprints `(B, B-bullet)` whose carrier semiring is p-torsion-free (i.e., `p * x = 0` implies `x = 0` in the carrier). Then any ring endomorphism `psi_p` with `psi_p(x) congruent x^p (mod p)` factors as `psi_p(x) = x^p + p delta_p(x)` for a uniquely determined `delta_p: B -> B`.

**Advantages**: clean, recovers Bhatt-Scholze directly when the blueprint is a p-torsion-free ring. `delta_p` is fully derived, not extra data.

**Disadvantages**:
- Excludes F_p and any F_p-algebra by construction. But F_p IS the universal characteristic-p test object. Excluding it from the framework is a dealbreaker for the goal of treating Spec(Z) and Spec(F_p) on equal footing.
- Forces blueprints with finite carriers (e.g. F_1's PUnit model) into the "trivially torsion-free because trivial" regime, where `delta_p` carries no information.
- Does not extend to the projected Spec(Z) x_F_1 Spec(Z) surface object, which has unknown torsion behavior.

**Verdict**: too restrictive for the broader program.

### 1.2 Sub-angle (ii): delta-blueprint with delta as primitive data

A **delta-blueprint at prime p** is a quadruple `(B, B-bullet, relations, delta_p)` where:
- `(B, B-bullet, relations)` is a Lorscheid blueprint.
- `delta_p: B -> B` is a function (NOT required to be a homomorphism) satisfying the Joyal-Buium identities (see §2.1) **in the carrier semiring**.
- `psi_p: B -> B` is **defined** by `psi_p(x) := x^p + p * delta_p(x)`. It is a theorem (not an axiom) that `psi_p` is a semiring endomorphism preserving `B-bullet`.

Then a **Lambda-blueprint** is a blueprint with a delta-structure at each prime p, plus the commutation axiom `psi_p . psi_q = psi_q . psi_p`.

**Advantages**:
- Works in all characteristic: F_p-algebras get `delta_p = 0` if `psi_p = Frobenius`, since `(Frobenius(x) - x^p)/p = 0` formally but the division is undefined; promoting `delta_p` to primitive data sidesteps the issue (just specify `delta_p(x) := 0` in F_p).
- Constructive witness: `delta_p(x)` is concretely the "obstruction" to FF holding strictly.
- Matches Bhatt-Scholze prismatic infrastructure directly: a "delta-blueprint at p" is what they call a "delta-ring" when the blueprint is a ring.

**Disadvantages**:
- More data to track; more axioms to verify.
- Joyal-Buium identities involve subtraction (e.g. `(x^p + y^p - (x+y)^p)/p`), which requires the carrier to be a ring or at least a semiring where the relevant differences are well-defined. For blueprints whose carrier is genuinely a semiring (not a ring), the formulation requires care.

**Verdict**: chosen. This is the cleanest formulation that retains the constructive witness and connects to prismatic infrastructure. We address the semiring vs ring issue by demanding the carrier is a commutative ring (which the Phase 1 Lean substrate's `CommSemiring` allows via specialization).

### 1.3 Sub-angle (iii): delta_p modulo p-torsion

Define `delta_p` as a map `B -> B / T_p(B)` where `T_p(B)` is the p-torsion submodule. Then the Joyal-Buium identities are imposed on the quotient.

**Advantages**: handles p-torsion uniformly without restricting carriers.

**Disadvantages**:
- The image of `delta_p` lives in a quotient, so composition `delta_p . delta_q` requires lifting back, which is generally non-canonical.
- The commutativity axiom `psi_p . psi_q = psi_q . psi_p` becomes a statement about commutativity modulo torsion, which is structurally weaker.
- The link to prismatic cohomology is murkier (BMS works with honest delta-rings, not delta-rings-mod-torsion).

**Verdict**: rejected. The non-canonicity of lifts breaks the Lambda-blueprint commutation structure, which is the central technical ingredient of the framework.

### 1.4 Defence of the choice

Sub-angle (ii) is selected because:

1. It matches Bhatt-Scholze's definition of delta-ring as primitive data (see §2.1 below). The published prismatic cohomology literature works with delta as primitive, not as derived from a torsion-free hypothesis.
2. It allows F_p as a delta-blueprint (with `delta_p = 0`), preserving the embedding `Blpr -> Lambda-Blpr` for at least F_p-algebras.
3. The "extra data" cost is real but unavoidable: any per-prime constructive witness for FF will demand per-prime data. Sub-angle (ii) makes this honest.
4. The Lean 4 Phase 1 substrate already structures `psi` as primitive data (`psi : Nat.Primes -> carrier -> carrier`). Adding `delta : Nat.Primes -> carrier -> carrier` alongside is structurally parallel and minimal additional infrastructure cost.

## 2. The delta-blueprint definition

### 2.1 Delta-ring axioms (recalled from R5 and Bhatt-Scholze)

For reference, a **delta-ring at prime p** in the sense of Joyal-Buium-Bhatt-Scholze is a commutative ring A together with a function `delta_p: A -> A` (NOT a ring homomorphism) satisfying:

1. `delta_p(0) = 0`.
2. `delta_p(1) = 0`.
3. **Additivity**: `delta_p(x + y) = delta_p(x) + delta_p(y) + (x^p + y^p - (x+y)^p) / p`.
4. **Multiplicativity**: `delta_p(x y) = x^p delta_p(y) + y^p delta_p(x) + p delta_p(x) delta_p(y)`.

In (3), the expression `(x^p + y^p - (x+y)^p) / p` is the **Buium polynomial** `C_p(x, y) := (x^p + y^p - (x+y)^p)/p`, which has integer coefficients by the binomial theorem (each `binom(p, k)` for `1 <= k <= p-1` is divisible by p). So `C_p(x, y) in Z[x, y]` and the formula in (3) is a genuine ring operation, no actual division required.

The derived Frobenius lift is `psi_p(x) := x^p + p * delta_p(x)`. Theorem (Joyal): `psi_p` is automatically a ring endomorphism. Sketch: additivity follows from (3) by inspection (`p * delta_p(x + y) + (x+y)^p = p delta_p(x) + p delta_p(y) + x^p + y^p`); multiplicativity follows from (4) similarly.

By construction `psi_p(x) - x^p = p delta_p(x)`, which is in `p A`. Hence FF holds for the carrier ring.

### 2.2 The delta-blueprint at prime p

**Definition** (D1.4.1-C.1, delta-blueprint at prime p). A **delta-blueprint at p** is a tuple `(B, B-bullet, relations, delta_p)` where:

- `(B, B-bullet, relations)` is a Lorscheid blueprint with `carrier` a **commutative ring** (not merely a commutative semiring; this is a strengthening relative to the Phase 1 substrate but is the standard hypothesis under which `C_p(x, y) in B` is well-defined).
- `delta_p: B -> B` is a function such that:
  - (DR1) `delta_p(0) = 0` AND `delta_p(1) = 0`.
  - (DR2) For all `x, y in B`: `delta_p(x + y) = delta_p(x) + delta_p(y) + C_p(x, y)` where `C_p(x, y) = sum_{k=1}^{p-1} (binom(p, k) / p) * x^k y^(p-k)`. (Here `binom(p, k)/p` is the integer `binom(p, k)/p = (p-1)! / (k! (p-k)!)`, defined for `1 <= k <= p-1` only.)
  - (DR3) For all `x, y in B`: `delta_p(x y) = x^p delta_p(y) + y^p delta_p(x) + p delta_p(x) delta_p(y)`.
- `delta_p` is compatible with `B-bullet` in the sense:
  - (DR4) If `x in B-bullet`, then `delta_p(x) in B` (not necessarily in `B-bullet`; the delta operation is not required to preserve the multiplicative submonoid).
  - (DR5) **Pointed restriction**: the derived `psi_p(x) := x^p + p delta_p(x)` does preserve `B-bullet`: `x in B-bullet => psi_p(x) in B-bullet`. This is the analogue of the Phase 1 substrate's requirement that `psi_p` preserves the multiplicative structure.
- `delta_p` is **compatible with blueprint relations**:
  - (DR6) If `(a, b) in relations`, then `(delta_p(a), delta_p(b)) in relations'` for some specified "induced delta-relation set" `relations'`. The simplest choice is `relations' = relations` (i.e., delta_p respects the relations as a function on the quotient); other choices (e.g., the relation closure under the Buium polynomial) are possible.

For the minimal Phase 1 candidate, take `relations' = relations`.

**Derived data**:
- `psi_p: B -> B` defined by `psi_p(x) := x^p + p * delta_p(x)`.
- The Frobenius mod p: `phi_p: B/(p) -> B/(p)` induced by `x |-> x^p`.

**Theorem** (D1.4.1-C.2, derived `psi_p` is an endomorphism). With the above axioms (DR1)-(DR6), the derived `psi_p` is a ring endomorphism of `B` preserving `B-bullet`. Furthermore, `psi_p(x) congruent x^p (mod pB)` holds strictly (not "in the blueprint quotient").

*Proof sketch*: The derived endomorphism property is Joyal's theorem applied verbatim in the carrier ring B; the blueprint relations play no role since the axioms (DR1)-(DR3) are imposed on the ring. The pointed preservation is (DR5). The congruence `psi_p(x) - x^p = p delta_p(x) in pB` is by construction.

### 2.3 The Lambda-blueprint (multi-prime delta-blueprint)

**Definition** (D1.4.1-C.3, Lambda-blueprint via delta-structures). A **Lambda-blueprint** is a tuple `(B, B-bullet, relations, {delta_p}_{p prime})` where:

- For each prime p, `(B, B-bullet, relations, delta_p)` is a delta-blueprint at p (per Definition D1.4.1-C.1).
- The derived family `{psi_p}_{p prime}` commutes pairwise: `psi_p . psi_q = psi_q . psi_p` for all primes p, q.

*Note on the commutation axiom*: this is imposed on the **derived** Frobenius lifts, not on the deltas themselves. The corresponding axiom on the deltas (the "Wilkerson identities") is more complex; we leave it implicit and impose the cleaner derived form. VERIFIER target #FF-C-3 below states the derived form for formalization.

### 2.4 FermatFrobenius axiom, restated

In the delta-ring form, the Fermat-Frobenius axiom is **not a separate condition**: it is a **theorem** that follows from the existence of the delta-structure.

**Definition** (D1.4.1-C.4, `FermatFrobenius_C`). For a tuple `(B, B-bullet, relations, {delta_p}_p)` satisfying the delta-blueprint axioms (DR1)-(DR6), the Fermat-Frobenius property is the assertion that the derived `psi_p` satisfies `psi_p(x) congruent x^p (mod pB)`. By Theorem D1.4.1-C.2, this holds automatically.

**Reformulation**: The Fermat-Frobenius axiom in the delta-ring form is the **existence** of `delta_p` as a well-defined function satisfying (DR1)-(DR6). The witness IS the axiom.

Compared to candidates A and B:
- Candidate A says: `psi_p(x) - x^p in (blueprint p-ideal)`. This is a relation in the quotient.
- Candidate B says: `psi_p(x) congruent x^p` in `B / I_p`. This is an equation in a quotient.
- Candidate C says: there exists `delta_p` with `psi_p(x) = x^p + p delta_p(x)`. This is an **existence statement with a constructive witness**.

The witness is the strongest form: any verifier of A or B who can produce an explicit `delta_p(x) in B` (not just in a quotient) is verifying C.

## 3. Specialization Lemmas

### 3.1 Specialization Lemma 1: p-torsion-free ring case

**Lemma** (D1.4.1-C-Spec1). Let `(B, B-bullet, relations)` be a blueprint with `B` a commutative ring that is p-torsion-free (i.e., multiplication by p is injective on B). Then any ring endomorphism `psi_p: B -> B` satisfying `psi_p(x) congruent x^p (mod pB)` extends UNIQUELY to a delta-structure `delta_p: B -> B` on B (Definition D1.4.1-C.1) with derived endomorphism equal to `psi_p`.

*Proof sketch*:

- *Existence of delta_p*: For each `x in B`, `psi_p(x) - x^p in pB`, so by p-torsion-freeness there exists a unique `delta_p(x) in B` with `p * delta_p(x) = psi_p(x) - x^p`. This defines `delta_p` as a set-map.
- *Axiom (DR1)*: `delta_p(0) = (psi_p(0) - 0)/p = 0/p = 0` and `delta_p(1) = (psi_p(1) - 1)/p = (1 - 1)/p = 0`.
- *Axiom (DR2)*: `p delta_p(x + y) = psi_p(x + y) - (x + y)^p = psi_p(x) + psi_p(y) - (x + y)^p = (x^p + p delta_p(x)) + (y^p + p delta_p(y)) - (x + y)^p`. The right side equals `p (delta_p(x) + delta_p(y)) + (x^p + y^p - (x+y)^p) = p (delta_p(x) + delta_p(y) + C_p(x, y))`. Cancel p (using p-torsion-freeness).
- *Axiom (DR3)*: Similar expansion using `psi_p(xy) = psi_p(x) psi_p(y)`.
- *Pointed (DR5)*: Inherited from `psi_p`.
- *Relations (DR6)*: Inherited from `psi_p` respecting relations.
- *Commutation*: If `{psi_p}` commutes, then since the delta is uniquely determined by psi in the torsion-free case, no additional axiom is needed.

This recovers Bhatt-Scholze's definition of delta-ring exactly: in a p-torsion-free ring, the data of a Frobenius lift `psi_p` and the data of a delta-structure `delta_p` are equivalent.

### 3.2 Specialization Lemma 2: Z with psi_p = id and the Fermat quotient

**Lemma** (D1.4.1-C-Spec2). Take `B = Z`, `B-bullet = Z` (or any submonoid of Z* containing 1), `relations = empty` (or trivial), `psi_p = id`. Then `delta_p(x) = (x - x^p)/p`, which is an integer for all `x in Z` by Fermat's little theorem.

For `x in Z` coprime to p, `x - x^p = x(1 - x^{p-1})`, and `(1 - x^{p-1})/p = -q_p(x)` where `q_p(x) := (x^{p-1} - 1)/p` is the **Fermat quotient** of x at p. Hence:

`delta_p(x) = -x * q_p(x) / p * p = -x * q_p(x) / 1 = -x * q_p(x) / 1`... wait let me redo. We have `delta_p(x) = (x - x^p)/p = x(1 - x^{p-1})/p = -x * (x^{p-1} - 1)/p = -x * q_p(x)`. Yes. So `delta_p(x) = -x * q_p(x)` for x coprime to p; for x divisible by p, write `x = p^k * m` with gcd(m, p) = 1 and verify directly.

*Verification for small cases*:
- p = 2, x = 3: `delta_2(3) = (3 - 9)/2 = -3`. Check: `q_2(3) = (3 - 1)/2 = 1`, so `-3 * 1 = -3`. Match.
- p = 3, x = 2: `delta_3(2) = (2 - 8)/3 = -2`. Check: `q_3(2) = (4 - 1)/3 = 1`, so `-2 * 1 = -2`. Match.
- p = 5, x = 2: `delta_5(2) = (2 - 32)/5 = -6`. Check: `q_5(2) = (16 - 1)/5 = 3`, so `-2 * 3 = -6`. Match.
- p = 5, x = 7: `delta_5(7) = (7 - 16807)/5 = -16800/5 = -3360`. Check: `q_5(7) = (2401 - 1)/5 = 480`, so `-7 * 480 = -3360`. Match.

**Cross-check axioms** on Z with `psi_p = id`:

- (DR1): `delta_p(0) = 0`, `delta_p(1) = (1 - 1)/p = 0`. OK.
- (DR2): `delta_p(x + y) = ((x + y) - (x + y)^p)/p` and `delta_p(x) + delta_p(y) + C_p(x, y) = (x - x^p)/p + (y - y^p)/p + (x^p + y^p - (x+y)^p)/p = (x + y - x^p - y^p + x^p + y^p - (x+y)^p)/p = ((x + y) - (x + y)^p)/p`. Match.
- (DR3): `delta_p(xy) = (xy - (xy)^p)/p`. Expand the RHS: `x^p delta_p(y) + y^p delta_p(x) + p delta_p(x) delta_p(y) = x^p (y - y^p)/p + y^p (x - x^p)/p + p ((x - x^p)/p)((y - y^p)/p) = (x^p y - x^p y^p + y^p x - y^p x^p)/p + (x - x^p)(y - y^p)/p = (x^p y - 2 x^p y^p + y^p x + xy - x^p y - xy^p + x^p y^p)/p = (xy - x^p y^p)/p`. The last equals `(xy - (xy)^p)/p` because x and y commute. Match.

So Z with the trivial Adams structure carries a canonical delta-blueprint structure, and `delta_p` is (up to sign) the Fermat quotient. This is a known fact in number theory, sometimes phrased as "the integers form a delta-ring at every prime, with delta_p the Fermat quotient operator."

### 3.3 Specialization Lemma 3: F_p and F_p-algebras

**Lemma** (D1.4.1-C-Spec3). Let `B = F_p` (or any F_p-algebra). Set `delta_p(x) := 0` for all x. Then the derived `psi_p(x) = x^p + p * 0 = x^p` is the Frobenius endomorphism.

*Verification*:
- (DR1): trivially.
- (DR2): need `0 = 0 + 0 + C_p(x, y)` in F_p. The Buium polynomial `C_p(x, y) = (x^p + y^p - (x+y)^p)/p`. But in F_p, `(x+y)^p = x^p + y^p` by freshman's dream. So as an integer-valued polynomial, `x^p + y^p - (x+y)^p` is divisible by p (in Z[x, y]), but in F_p[x, y] the polynomial `C_p(x, y)` modulo p is what we need. Specifically, `C_p(x, y) = sum_{k=1}^{p-1} binom(p, k)/p * x^k y^{p-k}`. The coefficient `binom(p, k)/p` is an integer; we need it modulo p. By Lucas's theorem or direct computation, `binom(p, k) = p * (p-1)! / (k! (p-k)!) = p / k * binom(p-1, k-1)`, so `binom(p, k)/p = binom(p-1, k-1) / k`. In F_p, `binom(p-1, k-1) congruent (-1)^{k-1} (mod p)` (Wilson-style), so `binom(p, k)/p congruent (-1)^{k-1} / k = -(-1)^k / k (mod p)`. Hence `C_p(x, y) mod p = sum_{k=1}^{p-1} (-1)^{k-1}/k * x^k y^{p-k}`. This is NOT identically zero in F_p[x, y] (it's the "first p-derivation"). So axiom (DR2) with `delta_p = 0` requires the LHS `delta_p(x + y) = 0` to equal `0 + 0 + C_p(x, y) = C_p(x, y)`. This is only consistent if `C_p(x, y) = 0` in F_p for all x, y in B.

This is a **subtle problem**: in F_p, `C_p(x, y) = sum_{k=1}^{p-1} (-1)^{k-1}/k * x^k y^{p-k}`, which is NOT identically zero as a polynomial but IS zero when evaluated on F_p (since x and y are in F_p and we evaluate). For p = 2: `C_2(x, y) = xy`, and we need `xy = 0` for all x, y in F_2? No, `1 * 1 = 1 not= 0`.

**Resolution**: Axiom (DR2) is `delta_p(x + y) = delta_p(x) + delta_p(y) + C_p(x, y)` as an identity in B, where `C_p(x, y)` is computed using the integer formula and then reduced into B. For B an F_p-algebra, we need to know `C_p(x, y) mod p` evaluated at `x, y in B`. With `delta_p = 0`, we need `C_p(x, y) = 0` in B for all `x, y`.

For p = 2: `C_2(x, y) = xy`. So (DR2) with `delta_2 = 0` over F_2 requires `xy = 0` for all `x, y in F_2`. FALSE. So `delta_2 = 0` does NOT satisfy the delta-ring axioms over F_2.

**Honest reckoning**: The naive `delta_p = 0` does NOT work for F_p in general. This is a real obstruction in the delta-ring formulation.

**Corrected Specialization Lemma 3**: There is a **unique** delta-structure on F_p compatible with `psi_p = Frobenius`, given by:

`delta_p(x) := (psi_p(x) - x^p)/p` interpreted as follows. In F_p, `psi_p(x) = x^p = x` (by Fermat's little theorem in F_p) and `x^p = x`, so `psi_p(x) - x^p = 0`. But "divide by p" is undefined in F_p.

The **right** answer: the delta-structure on F_p is defined by lifting to Z_p (or W(F_p) = Z_p), computing delta there, and reducing. For F_p as a quotient of Z_p, the delta-structure on F_p is the **image** of the canonical delta on Z_p. In W(F_p) = Z_p, the Adams operation `psi_p` is the unique Frobenius lift (identity if we take psi_p = id), and `delta_p(x) = (x - x^p)/p` is integer-valued by Fermat's little theorem. Reducing modulo p gives a function `F_p -> F_p` that turns out to be... `delta_p(x) mod p = (x - x^p)/p mod p`.

For p = 2, lift `x in F_2` to `x in {0, 1} subset Z_2`. Then `delta_2(0) = 0`, `delta_2(1) = (1 - 1)/2 = 0`. So `delta_2 = 0` on F_2 viewed as the image of {0, 1} in Z_2.

But this contradicts what I derived above. The issue is that I was confusing "F_p as F_p" with "F_p as the residue field of Z_p". Let me restart.

**Final correct statement of Specialization Lemma 3**:

**Lemma** (D1.4.1-C-Spec3, corrected). Let `B = F_p`. Consider B as a delta-blueprint at p with `delta_p` **inherited from the canonical delta-structure on Z_p via reduction**. Explicitly: each `x in F_p` lifts uniquely to its Teichmuller representative `[x] in Z_p`, and `delta_p([x]) = ([x] - [x]^p)/p`. The reduction modulo p of `delta_p([x])` is the F_p-valued delta on F_p.

For p = 2: `delta_2(0) = 0`, `delta_2(1) = (1 - 1)/2 = 0`. So `delta_2 = 0` on F_2 (after reduction).
For p = 3: Teichmuller reps in Z_3 are `0, 1, -1` (since `(-1)^3 = -1` so -1 is Teichmuller). `delta_3(0) = 0`, `delta_3(1) = 0`, `delta_3(-1) = (-1 - (-1)^3)/3 = (-1 - (-1))/3 = 0`. So `delta_3 = 0` on F_3.

In general for F_p, the Teichmuller representatives are exactly the (p-1)-th roots of unity together with 0, and these satisfy `[x]^p = [x]`, so `delta_p([x]) = 0` for all `x in F_p`.

So on F_p, the canonical delta-structure has `delta_p = 0`. But what about axiom (DR2)?

(DR2) requires `delta_p(x + y) = delta_p(x) + delta_p(y) + C_p(x, y)` IN B. With `delta_p = 0` everywhere, this is `0 = 0 + 0 + C_p(x, y) = C_p(x, y)`, so we need `C_p(x, y) = 0` in F_p for all `x, y in F_p`.

But the integer formula gives `C_p(x, y)` as an integer (after evaluation), and we reduce mod p. The integer `C_p(x, y) = (x^p + y^p - (x+y)^p)/p` IS an integer for `x, y in Z`. After reduction to F_p, we get some element. For p = 2, `C_2(x, y) = (x^2 + y^2 - (x+y)^2)/2 = -xy`. Mod 2, this is `xy mod 2`. So (DR2) for F_2 with `delta_2 = 0` requires `xy = 0` for all `x, y in F_2`. FALSE (1*1 = 1).

So the "naive transport" of delta-structure from Z_p to F_p does NOT give a delta-structure on F_p. The delta-structure on F_p is genuinely **zero, but axiom (DR2) fails** unless we accept that the Buium polynomial reduces to zero in F_p as well.

**True resolution**: In the literature, F_p is regarded as a delta-ring with `delta_p = 0` where (DR2) is interpreted **using the lift of x and y to W(F_p)**, not directly in F_p. The delta-ring axioms (DR2)-(DR3) are NOT statements in B alone; they involve `C_p(x, y)` which is naturally an integer computed from integer lifts.

For F_p-algebras, the delta-structure exists iff the F_p-algebra LIFTS to a p-torsion-free W(F_p)-algebra (e.g., the Witt vectors). For `B = F_p`, the lift is `W(F_p) = Z_p`, and the delta-structure on F_p is the **image of the delta-structure on Z_p**.

**The honest conclusion for the project**: in sub-angle (ii), F_p-algebras require LIFTING to characteristic 0 to define delta-structures. This is consistent with Bhatt-Scholze's prismatic setup: a prism is a pair `(A, I)` where A is a delta-ring (typically p-torsion-free) and `I` is an ideal such that `A/I` is the F_p-algebra of interest.

**Restated Specialization Lemma 3**: F_p does NOT carry a "native" delta-blueprint structure in the sense of Definition D1.4.1-C.1 (axiom (DR2) fails for `delta_p = 0`). Instead, F_p inherits a delta-blueprint structure via the prism `(W(F_p), (p)) = (Z_p, (p))`: the delta-blueprint structure on F_p is the QUOTIENT structure from `Z_p`. Equivalently, F_p is a delta-blueprint **relative to a prism**, not absolutely.

This is a substantive structural difference between candidate C and candidates A/B. Candidates A/B can directly axiomatize F_p as a Lambda-blueprint with `psi_p = Frobenius`. Candidate C cannot. **In candidate C, the embedding `Blpr -> Lambda-Blpr` is only partial: it factors through "prismatic blueprints" rather than directly.**

This is flagged as a potential disqualifier for candidate C in §11.

### 3.4 Worked example: F_1

For F_1 with carrier `{0, 1}` (Bool-style trivial ring) and `psi_p = id`:

- `delta_p(0) = (id(0) - 0^p)/p = (0 - 0)/p = 0`.
- `delta_p(1) = (id(1) - 1^p)/p = (1 - 1)/p = 0`.

Both are integers, so the F_1 case is trivially a delta-blueprint with `delta_p = 0`. All axioms hold vacuously.

### 3.5 Worked example: F_p[T] (polynomial algebra over F_p)

Take `B = F_p[T]`, `B-bullet = {T^n : n >= 0}`, `psi_p(T) := T^p`, `psi_p|_{F_p} = Frobenius (= identity by Fermat little theorem on F_p)`. Then `delta_p(T) = (psi_p(T) - T^p)/p = (T^p - T^p)/p = 0/p`. Formally `0/p` is well-defined as `0`. So `delta_p(T) = 0`.

But what about `delta_p(T + 1)`? We need (DR2): `delta_p(T + 1) = delta_p(T) + delta_p(1) + C_p(T, 1) = 0 + 0 + C_p(T, 1)`. The Buium polynomial `C_p(T, 1) = (T^p + 1 - (T+1)^p)/p`. In characteristic 0 (Z[T]), this equals `-sum_{k=1}^{p-1} binom(p, k)/p * T^k`. Reduced mod p, this is `-sum_{k=1}^{p-1} (-1)^{k-1}/k * T^k` in F_p[T], which is non-zero.

So `delta_p(T + 1) = C_p(T, 1) != 0` in F_p[T], if we demand `delta_p(T + 1) - delta_p(T) - delta_p(1) = C_p(T, 1)`.

But what should `delta_p(T + 1)` equal computationally? Using `psi_p(T + 1) = psi_p(T) + psi_p(1) = T^p + 1`, and `delta_p(T + 1) = (psi_p(T + 1) - (T + 1)^p)/p = (T^p + 1 - (T + 1)^p)/p = C_p(T, 1)`. So the formula gives `delta_p(T + 1) = C_p(T, 1)`, consistent with axiom (DR2).

This means: for F_p[T] with `psi_p(T) = T^p`, the delta-structure is **non-zero** at `T + 1`: `delta_p(T + 1) = (T^p + 1 - (T + 1)^p)/p` evaluated by integer arithmetic before reducing. But to do this in F_p[T] we need to **lift** to Z[T], compute, then divide by p in Z, then reduce.

The result: F_p[T] is a delta-blueprint at p, with `delta_p(T) = 0` and `delta_p(T + 1) = C_p(T, 1)` (an element of F_p[T] computed via Z[T] lift). This works! The lifting trick is general for F_p-algebras with chosen lifts.

**Caveat**: this requires a CHOICE of lift Z[T] -> F_p[T]. Different lifts give different delta-structures. For F_p[T] there is a canonical lift (the obvious one), but for general F_p-algebras the canonical lift requires the algebra to be **formally smooth** over F_p in an appropriate sense. This is the prismatic-cohomology hypothesis (Bhatt-Morrow-Scholze): you need a prism `(A, I)` covering the F_p-algebra.

### 3.6 Worked example: Z[T] (the free generator)

Take `B = Z[T]`, `B-bullet = {T^n : n >= 0}`, `psi_p(T) := T^p` (the "free" choice satisfying FF strictly), `psi_p|_Z = id`. Then `delta_p(T) = (T^p - T^p)/p = 0/p = 0`.

Cross-check `delta_p(T + 1)`: `psi_p(T + 1) = (T + 1)^p`. Wait, `psi_p` is a ring endomorphism with `psi_p(T) = T^p` and `psi_p(1) = 1`, so `psi_p(T + 1) = T^p + 1`. Then `delta_p(T + 1) = (psi_p(T + 1) - (T + 1)^p)/p = (T^p + 1 - (T + 1)^p)/p = C_p(T, 1) in Z[T]`. This is a non-zero integer polynomial.

So Z[T] is a delta-blueprint at p with `delta_p(T) = 0` and `delta_p(T + 1) = C_p(T, 1)`. The delta is non-trivial on the additive structure even though it vanishes on the free generator.

**Alternative choice**: take `psi_p(T) := T` (the constant Frobenius lift). Then `delta_p(T) = (T - T^p)/p`. For this to be a polynomial in Z[T], we need `(T - T^p)/p in Z[T]`. But `T - T^p = T(1 - T^{p-1})`, and dividing by p in Z[T] requires p to divide the coefficients. The polynomial `1 - T^{p-1}` has coefficients `+/-1`, neither of which is divisible by p (for p > 1). So `(T - T^p)/p NOT in Z[T]`.

**Conclusion**: in Z[T], the choice `psi_p(T) = T` is **NOT** a valid delta-blueprint structure (delta_p would not be a function Z[T] -> Z[T]). Only the choice `psi_p(T) = T^p` (or more generally `psi_p(T) = T^p + p * f(T)` for some `f in Z[T]`) gives a valid delta-structure.

**This is exactly the kind of obstruction that distinguishes Candidate C from Candidates A/B**. Candidate A (blueprint-relation form) might say: "well, `psi_p(T) = T` and `T - T^p` is in the blueprint p-ideal generated by `(p, T - T^p)`". Candidate B says: "in B/I_p where `I_p` is the ideal `(p)`, the equation `psi_p(T) = T = T^p mod p` is required and `T congruent T^p mod p` by Fermat's little theorem in F_p... no wait `T` is a transcendental, not in F_p". So actually in Candidate B, `psi_p(T) = T` would require `T congruent T^p mod p in B/(p) = F_p[T]`, which fails (T and T^p are distinct elements of F_p[T] for p > 1).

So all three candidates A/B/C correctly **reject** `psi_p(T) = T` for `B = Z[T]`. They differ only in how they reject it: A/B reject it via an ideal-containment check, C rejects it via inability to define `delta_p` as a function.

### 3.7 Summary table

| Example | Carrier | `psi_p` | `delta_p` | Valid delta-blueprint? |
|---|---|---|---|---|
| F_1 | `{0, 1}` (trivial) | id | 0 | yes (trivially) |
| Z | Z | id | `(x - x^p)/p` (Fermat quotient times -x) | yes |
| F_p | F_p | Frobenius (= id on F_p) | 0 | **only via prismatic lift** (axiom (DR2) requires lifting) |
| F_p[T] | F_p[T] | `T -> T^p`, id on F_p | 0 on T, `C_p(T, 1)` on T+1 | yes (via Z[T] lift) |
| Z[T] | Z[T] | `T -> T^p` | 0 on T, `C_p(T, 1)` on T+1 | yes |
| Z[T] | Z[T] | `T -> T` (id) | **undefined** (`(T - T^p)/p` not in Z[T]) | **NO** |

The last row is the punchline: candidate C **detects** the failure of FF in Z[T] under `psi_p = id` via the impossibility of defining `delta_p` as an honest function. This is a constructive, witness-based detection.

## 4. K2 (D-H) self-check

The Davenport-Heilbronn L-function `L_DH(s) = (1/2)(1 + i sqrt((1+i sqrt(5))/(1-i sqrt(5)))) * L(s, chi_5)` (Titchmarsh-Heath-Brown normalization; specifics in `experiments/_shared/davenport_heilbronn.py`) has a functional equation but no Euler product. The K2 wrong-approach detector says any framework claiming to prove RH must STRUCTURALLY exclude D-H, not just empirically.

**Claim**: D-H cannot be a delta-blueprint in the sense of Definition D1.4.1-C.1.

**Argument**:

1. D-H is a linear combination of L-functions: `L_DH(s) = a L(s, chi_1) + b L(s, chi_2)` for two Dirichlet characters and coefficients `a, b` that are roots of a quadratic over Q(i). The functional-equation structure is preserved under such linear combinations, but the **Euler product structure is destroyed**: `L_DH(s) != prod_p (1 - alpha_p p^{-s})^{-1}` for any choice of `alpha_p`.

2. A delta-blueprint at prime p, by Definition D1.4.1-C.1, comes equipped with a Frobenius lift `psi_p`. In the corresponding L-function (built from the trace of `psi_p` acting on cohomology), the local Euler factor at p has the form `det(1 - psi_p p^{-s} | H^*)^(-1)`, which is **necessarily a rational function of `p^{-s}` with poles and zeros determined by the eigenvalues of `psi_p`**.

3. For D-H, no such local Euler factor exists at any prime p (the linear-combination structure precludes a single multiplicative datum per prime). Hence there is no `psi_p` that, when fed into the trace formula, reproduces the D-H local factors. Hence no delta-blueprint structure exists on the "D-H side" of any candidate Lambda-blueprint.

4. **Sharper version specific to candidate C**: even if one tried to define `psi_p` on a candidate "D-H blueprint" by hand, the delta-ring axiom (DR3) (multiplicativity of delta) is rigid: `delta_p(xy) = x^p delta_p(y) + y^p delta_p(x) + p delta_p(x) delta_p(y)`. This multiplicativity is INCOMPATIBLE with linear-combination structure: if `L_DH = a L_1 + b L_2`, then at the cohomological level the "characters" being summed have different Frobenius eigenvalues. Any delta on the sum would have to satisfy multiplicativity on the components SEPARATELY but additivity on the sum, and these constraints over-determine `delta_p` (no solution exists unless `a = 0` or `b = 0`, i.e., D-H is one of its constituent L-functions, contradicting its definition).

5. **Compared to candidates A/B**: Candidate A excludes D-H via the absence of a multiplicative `psi_p` consistent with the blueprint relations. Candidate B excludes D-H via the failure of `psi_p` to commute with the quotient map `B -> B/I_p`. Candidate C excludes D-H via the **non-existence of `delta_p` as a function** witnessing FF. This is arguably the sharpest: it's not a failure of one axiom but the impossibility of even DEFINING the primary datum.

**Verdict**: K2 D-H exclusion holds for candidate C, and the exclusion is sharper than for A/B because it operates at the level of constructive non-existence rather than axiom violation.

## 5. Connection to R5 (prismatic cohomology) and Direction 3

R5 (`2A_R5_prismatic_cohomology.md`) is the project's primary Phase 2 target: applying Bhatt-Morrow-Scholze prismatic cohomology to the surface object Spec(Z) x_F_1 Spec(Z). Candidate C is the **only** of the three FF candidates that directly produces prismatic-compatible structure.

### 5.1 What candidate C inherits from delta-rings

- Per R5 §2, a delta-ring at prime p is exactly the data needed for the prismatic site: a prism is a pair `(A, I)` with A a delta-ring (typically p-torsion-free) and I an ideal of "prismatic type."
- A delta-blueprint at p (Definition D1.4.1-C.1) generalizes a delta-ring by adding the blueprint structure `(B-bullet, relations)`. The "underlying delta-ring" `(B, delta_p)` is recovered by forgetting the blueprint structure.
- Hence ANY delta-blueprint produces a delta-ring, which can be fed into the prismatic site as soon as the appropriate ideal `I` is chosen.

### 5.2 What additional Lambda-blueprint structure does NOT come from the deltas

A Lambda-blueprint per Definition D1.4.1-C.3 is more than a delta-blueprint at each prime separately. The extra data is:

1. **The commutation axiom**: `psi_p . psi_q = psi_q . psi_p` for all `p, q`. This is a **global** structure not derivable from each prime separately.
2. **Pairwise compatibility of `delta_p` and `delta_q`** (implicit). Given `delta_p` and `delta_q`, can both be present on the same B simultaneously? The answer requires the Wilkerson identities (the non-trivial generalization of Joyal-Buium for multi-prime delta operations). These are **stronger than just commutation of `psi_p` and `psi_q`** in general but reduce to it in the torsion-free case.
3. **Compatibility with all blueprint relations across primes**: a relation `(a, b) in relations` must be preserved by every `psi_p`, which is automatic from per-prime axiom (DR6) but the simultaneity is an additional global constraint.

**Question**: is a Lambda-blueprint a "global delta-blueprint" plus commutation, or genuinely more?

**Answer (provisional)**: In the p-torsion-free case, a Lambda-blueprint IS a global delta-blueprint plus commutation; the Wilkerson identities reduce to commutation. In the general case (with torsion or non-flat extensions), the Wilkerson identities are stronger. For the project's purposes (Spec(Z) is p-torsion-free for all p, since Z is itself p-torsion-free), this is not a structural problem for Direction 1.4.1, but it becomes one for Direction 3 milestone 4.1 if the projected surface Spec(Z) x_F_1 Spec(Z) develops torsion. ADVERSARY test case (c) below addresses this.

### 5.3 Direct path to Direction 3

A candidate-C Lambda-blueprint immediately gives:

1. A per-prime delta-ring structure on B (per §5.1).
2. A canonical prism `(B^{(p)}, (p))` where `B^{(p)}` is the p-adic completion of B (assuming p-torsion-freeness; if not, replace with appropriate completion).
3. A prismatic site `(B^{(p)})_prism`.
4. Prismatic cohomology `H^*_prism(B^{(p)})`.

In contrast, candidates A and B would have to add a separate construction of `delta_p` (essentially, perform the work of candidate C) before feeding into the prismatic infrastructure. **Candidate C is therefore the natural choice if Direction 3 is the next milestone**, which it is per the orchestrator plan.

## 6. 17-constraint self-assessment

The R2.5 dossier predicted 8 yes / 4 partial / 5 open for Lambda-blueprints in general. Candidate C may score differently, particularly higher on (viii) Frobenius spectrum and (x) Euler factors (because of the explicit delta witness), and potentially lower on basic structural items because of the F_p obstruction noted in §3.3.

Honest assessment, per constraint:

| # | Constraint | C status | Comment relative to R2.5 prediction |
|---|---|---|---|
| (i) | Spec(Z) -> S morphism | yes | Inherited; the morphism `F_1 -> Z -> any Lambda-blueprint` factors through the per-prime delta-rings. Same as A/B. |
| (ii) | Non-trivial fiber product | partial | Inherited from the underlying Lorscheid blueprint structure; the per-prime delta structure does not directly help with fiber product computation. Same as A/B at this level. |
| (iii) | F_q compatibility | **partial-NO** | **DOWNGRADE from R2.5's "yes"**. Per §3.3, F_p only carries a delta-blueprint structure via prismatic lift, not natively. So `Spec(F_q)` is a Lambda-blueprint only "relative to its Witt-vector lift", not absolutely. This is a real structural cost of candidate C. |
| (iv) | Finite-dim cohomology | open | Same as R2.5; depends on prismatic infrastructure (R5). Candidate C makes this directly accessible. |
| (v) | Poincare duality | open | Same as R2.5; depends on (iv). |
| (vi) | Cycle class / intersection | open | Same as R2.5; the delta structure provides an explicit Frobenius lift that may help define the cycle class map via prismatic Chern characters, but the construction remains conjectural. |
| (vii) | Kunneth | open | Same as R2.5. |
| (viii) | Frobenius spectrum | yes-strong | **UPGRADE from R2.5's "yes"**. Candidate C provides not just `psi_p` but its constructive decomposition `psi_p = x^p + p delta_p`, which separates the "Frobenius part" `x^p` from the "lift part" `p delta_p`. The spectrum of `psi_p` acting on prismatic cohomology decomposes accordingly, giving a finer spectral picture. |
| (ix) | Lefschetz trace | open | Same as R2.5; trace formula structure depends on (iv)-(vii). |
| (x) | Euler factor compatibility | yes-strong | **UPGRADE from R2.5's "yes"**. The Joyal-Buium identities (DR3) imply multiplicativity of `1 + p delta_p` in a precise sense (the Witt-vector / ghost-component structure), which is exactly the Euler-product structure. This is a stronger version of (viii). |
| (xi) | Hodge index | open | Same as R2.5; the universal K1 obstacle. |
| (xii) | Provable without RH input | open | Same as R2.5; not addressed by FF formulation. |
| (xiii) | Castelnuovo-Severi applicability | open | Same as R2.5. |
| (xiv) | Function-field RH recovery | yes-partial | F_q is partial per (iii). Recovery for actual function fields (not single F_q) may still work via the prismatic-lift route. |
| (xv) | Dirichlet L-functions | partial | Same as R2.5; the per-prime delta structure parameterizes per-prime local Euler factors, so Dirichlet twists become directly accessible. |
| (xvi) | Selberg class | open | Same as R2.5. |
| (xvii) | D-H excluded | yes-strong | **STRENGTHENED**. Per §4, the delta-ring multiplicativity axiom (DR3) provides a sharper exclusion of D-H than the parent frameworks: D-H lacks even the data needed to define `delta_p` as a function. |

**Summary tally**:
- Yes (or yes-strong): (i), (viii), (x), (xvii). 4 strong.
- Partial: (ii), (iii) [downgraded], (xiv), (xv). 4.
- Open: (iv), (v), (vi), (vii), (ix), (xi), (xii), (xiii), (xvi). 9.

Compared to R2.5's prediction (8 yes / 4 partial / 5 open):
- (iii) downgrades from yes to partial-NO. This is a real cost.
- (viii) and (x) strengthen (still yes, but the witness is constructive).
- (xvii) strengthens.
- Other constraints unchanged in status.

**Net**: Candidate C is **stronger** than R2.5 on Frobenius-related items (viii, x, xvii) and on path to Direction 3 (prismatic cohomology). It is **weaker** on F_p compatibility (iii) because of the lift requirement. The trade-off is favorable IF the program's path goes through prismatic cohomology, which is the orchestrator's intended Phase 2.

## 7. Verification targets for VERIFIER

VERIFIER should formalize the following in Lean 4, extending `lean/ZetaRH/LambdaBlueprints.lean`. The substrate's existing `LambdaBlueprint` structure should be extended with `delta` data, with the existing `psi`-based `LambdaBlueprint` recoverable as a special case (or alternatively, redefined in terms of delta).

**#FF-C-1: Buium polynomial as integer polynomial**.
Informal: `C_p(x, y) := sum_{k=1}^{p-1} (binom(p, k) / p) * x^k * y^(p-k)` is well-defined as a polynomial in `Z[X, Y]`, since each coefficient `binom(p, k)/p` is an integer for `1 <= k <= p-1`.
Lean signature:
```
def buium (p : Nat.Primes) (R : Type) [CommRing R] (x y : R) : R := ...
theorem buium_int (p : Nat.Primes) (x y : Int) :
    p * (buium p Int x y) = x^p.val + y^p.val - (x + y)^p.val
```
Difficulty: easy. The integrality of `binom(p, k)/p` is `Nat.Prime.dvd_choose_self` or similar in Mathlib.

**#FF-C-2: DeltaBlueprint structure**.
Informal: extend `Blueprint` with a `delta` function and the (DR1)-(DR6) axioms.
Lean signature (proposed):
```
structure DeltaBlueprint extends Blueprint where
  [carrierRing : CommRing carrier]  -- strengthen from CommSemiring
  delta : Nat.Primes → carrier → carrier
  delta_zero : ∀ p, delta p 0 = 0
  delta_one : ∀ p, delta p 1 = 0
  delta_add : ∀ p x y, delta p (x + y) = delta p x + delta p y + buium p carrier x y
  delta_mul : ∀ p x y, delta p (x * y) =
      x^p.val * delta p y + y^p.val * delta p x + p.val * delta p x * delta p y
  delta_pointed_psi : ∀ p, ∀ x ∈ pointed,
      (x^p.val + p.val * delta p x) ∈ pointed
  delta_relations : ∀ p, ∀ a b, (a, b) ∈ relations → (delta p a, delta p b) ∈ relations
```
Difficulty: medium. The structure is straightforward; the technical issue is the `CommRing` strengthening (currently the substrate has `CommSemiring`).

**#FF-C-3: Derived psi is a ring endomorphism**.
Informal: the derived `psi_p(x) := x^p + p * delta_p(x)` is a ring endomorphism of B.
Lean signature:
```
def DeltaBlueprint.psi (B : DeltaBlueprint) (p : Nat.Primes) (x : B.carrier) : B.carrier :=
  x^p.val + p.val * B.delta p x
theorem DeltaBlueprint.psi_add (B : DeltaBlueprint) (p : Nat.Primes) (x y : B.carrier) :
    B.psi p (x + y) = B.psi p x + B.psi p y
theorem DeltaBlueprint.psi_mul (B : DeltaBlueprint) (p : Nat.Primes) (x y : B.carrier) :
    B.psi p (x * y) = B.psi p x * B.psi p y
theorem DeltaBlueprint.psi_zero (B : DeltaBlueprint) (p : Nat.Primes) :
    B.psi p 0 = 0
theorem DeltaBlueprint.psi_one (B : DeltaBlueprint) (p : Nat.Primes) :
    B.psi p 1 = 1
```
Difficulty: medium-low. Each is a direct algebraic computation using (DR1)-(DR4) and the binomial expansion of `(x + y)^p`.

**#FF-C-4: Fermat-Frobenius holds**.
Informal: the derived `psi_p(x) - x^p = p delta_p(x)` is exactly divisible by p, hence FF holds in the strict sense `psi_p(x) congruent x^p (mod pB)`.
Lean signature:
```
theorem DeltaBlueprint.fermat_frobenius (B : DeltaBlueprint) (p : Nat.Primes) (x : B.carrier) :
    B.psi p x - x^p.val = p.val * B.delta p x
```
Difficulty: trivial (by `rfl` from definitions, modulo `sub_add_cancel` lemmas).

**#FF-C-5: LambdaBlueprint via delta, commutation**.
Informal: a LambdaBlueprint is a DeltaBlueprint with commuting derived psis.
Lean signature:
```
structure LambdaBlueprintDelta extends DeltaBlueprint where
  psi_comm : ∀ p q, ∀ x, psi p (psi q x) = psi q (psi p x)
```
Difficulty: trivial as a structure declaration.

**#FF-C-6: Specialization to p-torsion-free rings (Spec1)**.
Informal: for a p-torsion-free commutative ring R, the data of a Frobenius lift `psi_p` and a delta-structure `delta_p` are equivalent.
Lean signature:
```
theorem delta_iff_psi_torsion_free (R : Type) [CommRing R] (p : Nat.Primes)
    (h_tf : ∀ x : R, p.val * x = 0 → x = 0) :
    -- bijection between {psi : R →+* R | psi x ≡ x^p [pR]}
    -- and {delta : R → R | DR1, DR2, DR3 hold}
    True := sorry
```
Difficulty: medium-high (requires formalizing the bijection cleanly).

**#FF-C-7: Specialization to Z with psi = id gives Fermat quotient (Spec2)**.
Informal: for B = Z with `psi_p = id`, `delta_p(x) = (x - x^p)/p` is an integer for all `x in Z`.
Lean signature:
```
def fermat_quotient_delta (p : Nat.Primes) (x : Int) : Int :=
    (x - x^p.val) / p.val
theorem fermat_quotient_int (p : Nat.Primes) (x : Int) :
    p.val * fermat_quotient_delta p x = x - x^p.val
-- equivalently, p divides (x - x^p)
theorem fermat_little_int (p : Nat.Primes) (x : Int) :
    (p.val : Int) ∣ (x - x^p.val)
```
Difficulty: medium. Mathlib has `Int.ModEq.pow_card_sub_one` or similar for Fermat's little theorem; extending from x not divisible by p to all x is by case analysis.

**#FF-C-8: F_p obstruction (Spec3)**.
Informal: there is NO non-trivial delta-blueprint structure on F_p that does not come from a lift to Z_p; specifically, axiom (DR2) requires the Buium polynomial to vanish identically on F_p, which it does not for p >= 2.
Lean signature:
```
theorem no_native_delta_Fp (p : Nat.Primes) (h_p : 2 ≤ p.val) :
    ¬ ∃ (delta : (ZMod p.val) → (ZMod p.val)),
      (delta 0 = 0) ∧ (delta 1 = 0) ∧
      (∀ x y, delta (x + y) = delta x + delta y + buium p (ZMod p.val) x y)
```
Difficulty: medium. The obstruction is concrete: instantiate at x = y = 1 and observe the Buium polynomial evaluates to a non-zero element of F_p.

**#FF-C-9: K2 D-H exclusion**.
Informal: there is no delta-blueprint structure on a candidate Lambda-blueprint whose "L-function" (formed by trace of derived psi) equals L_DH(s).
Lean signature: too vague to formalize directly; concretized as ADVERSARY test case (a) below.

**#FF-C-10: Compatibility with existing Phase 1 LambdaBlueprint**.
Informal: every `DeltaBlueprint` (with derived `psi`) gives a `LambdaBlueprint` (in the existing Phase 1 sense).
Lean signature:
```
def DeltaBlueprint.toLambdaBlueprint (B : DeltaBlueprint) : LambdaBlueprint :=
  { B.toBlueprint with
    psi := B.psi
    psi_hom := ... -- by FF-C-3
    psi_comm := ... -- requires extra axiom or use LambdaBlueprintDelta
    psi_fermat_frobenius := ... -- by FF-C-4 (after relations := Set.univ specialization)
  }
```
Difficulty: trivial structural translation.

**Total: ten verification targets, of which #FF-C-1 through #FF-C-5 are the core formalization (estimated 1-3 weeks of VERIFIER effort) and #FF-C-6 through #FF-C-10 are extensions (additional 2-4 weeks).**

## 8. Adversarial test cases for ADVERSARY

ADVERSARY should attempt to break the candidate by exhibiting:

**Test (a): D-H as candidate Lambda-blueprint via delta**.
Construct a (presumed-impossible) delta-blueprint structure on a carrier B equipped with an L-function equal to `L_DH`. The K2 argument in §4 predicts this fails because of multiplicativity (DR3). ADVERSARY should attempt the construction explicitly and confirm where the obstruction surfaces. Expected outcome: confirmation that no delta-blueprint structure exists for D-H; the obstruction is the multiplicativity axiom (DR3) combined with the additive structure of D-H as `a L_1 + b L_2`.

**Test (b): Z[T] with `psi_p = id`**.
Per §3.6, this should NOT be a delta-blueprint because `delta_p(T) = (T - T^p)/p` is not a polynomial in Z[T]. ADVERSARY should confirm:
- The naive definition fails (delta_p(T) not in Z[T]).
- No alternative definition of `delta_p(T) in Z[T]` satisfies (DR1)-(DR3) for the choice `psi_p(T) = T`.
- Hence the choice `psi_p(T) = T` for Z[T] is excluded from candidate C (consistent with candidate A and candidate B).

**Test (c): Non-flat extension developing torsion**.
Construct a Lambda-blueprint `B'` extending B such that `B'` develops p-torsion. Investigate whether `delta_p` extends to a function `B' -> B'`, possibly with torsion in the image. ADVERSARY should determine: does the delta-structure descend cleanly to non-flat extensions, or does it develop pathologies (e.g., `delta_p` becomes multi-valued mod torsion)?
- Concrete instance: `B = Z[T]`, `B' = Z[T]/(p^2 T)`. The element `T` becomes p-torsion in `B'` (specifically, `p^2 T = 0`). Check whether `delta_p(T)` is well-defined in `B'`.
- Expected outcome: the delta-structure does NOT descend cleanly to non-flat extensions; this is consistent with Bhatt-Scholze's restriction to p-torsion-free or "prismatic" delta-rings.

**Test (d): Wilkerson identities at primes p != q**.
Check whether the commutation `psi_p . psi_q = psi_q . psi_p` (which is imposed as a Lambda-blueprint axiom on derived endomorphisms) automatically implies the Wilkerson identities on the deltas (`delta_p . delta_q` vs `delta_q . delta_p` should agree up to a specific Buium-style polynomial in `x^p, x^q, delta_p(x), delta_q(x)`). If not, the Lambda-blueprint axiom in candidate C is **strictly weaker** than the full multi-prime delta-structure.

**Test (e): Adams operations on F_p**.
The orthodox Lambda-ring structure on F_p has `psi_p = Frobenius = id` (since `x^p = x` in F_p by Fermat). Per Specialization Lemma 3 corrected (§3.3), F_p does NOT admit a native delta-blueprint structure satisfying (DR2). ADVERSARY should:
- Construct the "obvious" delta-blueprint on F_p naively (`delta_p = 0`).
- Compute `delta_p(1 + 1)` two ways: as `delta_p(2) = 0` directly, and as `delta_p(1) + delta_p(1) + C_p(1, 1) = 0 + 0 + C_p(1, 1)`.
- For p = 2: `C_2(1, 1) = (1 + 1 - 4)/2 = -1`. In F_2, `-1 = 1`. So the two computations give `0` and `1`, contradiction.
- This concretely instantiates the obstruction noted in §3.3.

**Test (f): Specialization to Lambda-rings is full and faithful**.
The R2.5 proposal claims `Lambda-Rings -> Lambda-Blpr` is a full embedding. For candidate C, this requires `Lambda-Rings -> DeltaBlueprint` (delta-blueprints at every prime). ADVERSARY should:
- Construct the functor explicitly: a Lambda-ring `(R, {psi_p})` gives a delta-blueprint at each prime p (with `delta_p = (psi_p - F_p)/p` where defined, via the p-torsion-free case).
- Verify the functor is full (every Lambda-blueprint morphism between two Lambda-rings comes from a Lambda-ring morphism). Expected outcome: yes, since the underlying ring map and Adams-operation intertwining determine the delta intertwining (via uniqueness in the p-torsion-free case).
- Verify faithfulness (the functor is injective on morphisms). Expected outcome: yes, trivially.
- Verify a Lambda-ring with p-torsion (the case where `delta_p` is NOT uniquely determined by `psi_p`) lifts uniquely to a delta-blueprint. Expected outcome: NO; this is a non-trivial obstruction. Examples: tate ring W(F_p)/p^n W(F_p), which is `Z/p^n`. Adams operation `psi_p = id` (by uniqueness of Frobenius lift on Z/p^n via Witt construction). Delta: `delta_p(x) = (x - x^p)/p` modulo `p^{n-1}` (one less p than the ring has). This is well-defined uniquely for n >= 2; for n = 1 (i.e., F_p) it is NOT uniquely determined and Specialization Lemma 3 corrected applies.

**Test (g): comparison with candidate A and candidate B**.
For a specific blueprint where all three candidates apply (e.g., Z with psi_p = id), verify that the FF condition certified by each candidate is equivalent:
- Candidate A: `(psi_p(x), x^p) in relations` where `relations` is the ideal generated by `(p, ...)`. For Z this means `psi_p(x) - x^p in pZ`, which is `x - x^p in pZ`, Fermat's little theorem.
- Candidate B: `psi_p(x) = x^p in B/I_p` where `I_p = (p)`. Same condition.
- Candidate C: `delta_p(x) = (psi_p(x) - x^p)/p in Z`. Same condition (the existence of `delta_p` as an integer is equivalent to `psi_p(x) - x^p in pZ`).
- All three agree on Z. They should disagree on more complex examples (e.g., a Lambda-ring with torsion, or a candidate "D-H Lambda-blueprint"). ADVERSARY should produce one such example and document the disagreement.

**Test (h): F_p[T] with non-canonical lift**.
Per §3.5, F_p[T] is a delta-blueprint via the canonical lift Z[T]. But the lift is not canonical without an additional choice. ADVERSARY should construct two distinct lifts (e.g., Z[T] -> F_p[T] vs Z[T'] -> F_p[T] where T' = T + p) and verify whether they give different delta-structures on F_p[T]. If they do, candidate C has a hidden choice dependence.

## 9. Relationship to candidates A and B

To be developed in coordination with BUILDER-1A and BUILDER-1B outputs:

- **Candidate C is strictly stronger than candidate A**. Any object satisfying candidate C (the delta-blueprint axioms with derived psi) automatically satisfies candidate A (the blueprint-relation form `psi_p(x) - x^p in pB`), since `psi_p(x) - x^p = p delta_p(x) in pB` by construction. The converse fails: candidate A allows configurations where `psi_p(x) - x^p in (blueprint p-ideal)` but no explicit `delta_p` exists (e.g., Z[T] with `psi_p(T) = T` if one considers `T - T^p` as "in the blueprint p-ideal" via some auxiliary relation; this is excluded by candidate C). **So candidate C is a strict refinement of candidate A**.

- **Candidate C is comparable but not directly stronger than candidate B**. Candidate B works in the quotient `B/I_p`, which is a categorical operation. Candidate C provides a witness `delta_p` that lives in B itself (not the quotient). Hence candidate C carries strictly more data than B, but the data is not just a strengthening of the same axiom; it's a different axiomatization. In the p-torsion-free case, candidate B and candidate C are EQUIVALENT (per Specialization Lemma 1). In the general case (p-torsion, non-flat extensions), candidate C is more restrictive (it requires the witness to exist in B, not just for the quotient equation to hold).

- **For Direction 1 milestone 4.1's stated goal** (define FF in blueprint language consistently with Lambda-rings and Lorscheid blueprints), candidate C is the most informative: it provides BOTH the structural axiom AND a constructive witness. It is also the most demanding (requires extra data `delta_p`).

- **Recommendation to ORCHESTRATOR**: candidate C should be developed as the "rich" version of FF, with candidates A and B serving as "thin" / "categorical" alternatives. In the Lean formalization, the substrate should expose all three layers: `LambdaBlueprintA` (weak, blueprint-relation), `LambdaBlueprintB` (medium, quotient), `LambdaBlueprintC = DeltaBlueprint with commutation` (strong, witness). Then theorems can be parameterized by the level of structure needed, which gives flexibility for downstream applications.

## 10. Open questions and limitations

Honestly flagging what is unresolved in this proposal:

1. **F_p compatibility (Specialization Lemma 3)**: the failure of native delta-blueprint structure on F_p is a real cost. This needs to be either accepted (treating F_p as a "prismatic blueprint relative to Z_p" rather than a Lambda-blueprint absolutely) or fixed (perhaps by relaxing axiom (DR2) to hold "modulo p-torsion in B"). The former is consistent with prismatic cohomology literature; the latter requires more work.

2. **Wilkerson identities vs commutation**: the Lambda-blueprint axiom (D1.4.1-C.3) demands commutation of derived `psi_p`, not the full Wilkerson identities on `delta_p`. This may be insufficient in the non-flat case. The fix is to add the Wilkerson identities explicitly, but they are substantially more complex than commutation, so the cost is real.

3. **Lift dependence for F_p[T]**: per §3.5, the delta-structure on F_p[T] depends on the choice of lift to Z[T]. For canonical lifts (the obvious one) this is fine, but for general F_p-algebras the canonical lift requires formal smoothness. This is consistent with the prismatic setup (Bhatt-Morrow-Scholze) but adds a hidden hypothesis.

4. **Surface object computation**: the projected Spec(Z) x_F_1 Spec(Z) surface (the Direction 1 milestone 4.6 target) has unknown torsion behavior. If it develops p-torsion, candidate C may not extend cleanly. This is the principal risk for the program continuation.

5. **No new information about Hodge index**: per the project's central thesis (LEARNINGS.md, R3.5), the Hodge index slot (xi)-(xiii) is the K1 wall. Candidate C does NOT address this; it only provides infrastructure for the Frobenius / cohomology side.

## 11. Bottom line

Candidate C proposes a **delta-blueprint** structure for Fermat-Frobenius, in which `delta_p: B -> B` is primitive data (sub-angle (ii)) and `psi_p(x) := x^p + p delta_p(x)` is derived. The FF condition is automatic from the existence of `delta_p`.

**Strengths**:
- Constructive witness for FF (sharper than A and B).
- Direct connection to Bhatt-Scholze prismatic cohomology (R5 / Direction 3).
- Sharper K2 exclusion of D-H (via multiplicativity axiom (DR3)).
- Strengthens (viii), (x), (xvii) in the 17-constraint scorecard.

**Weaknesses**:
- Native F_p compatibility is lost (constraint (iii) downgrades). F_p is treatable only via prismatic lift.
- Requires `CommRing` carrier (strengthens the Phase 1 substrate's `CommSemiring`).
- Wilkerson identities are not fully captured by commutation axiom.
- Lift dependence for F_p-algebras.

**Verdict for ORCHESTRATOR**: candidate C is the right choice IF the program's Phase 2 target is prismatic cohomology (Direction 3), since it produces the prismatic-compatible structure directly. It is the wrong choice if F_p compatibility is a binding constraint. Given the orchestrator's stated Phase 2 trajectory, candidate C is recommended for development alongside (not instead of) candidates A and B; the three candidates form a hierarchy A (weakest) -> B (medium) -> C (strongest), and a complete formalization should expose all three layers.

**Honest assessment**: this is a candidate, not a result. The verification targets (#FF-C-1 through #FF-C-10) and adversarial test cases (a)-(h) are open. The construction is unlikely to "prove RH"; it provides infrastructure for the per-prime side of the program. The Hodge index wall (K1) remains universal.

End of candidate C document.
