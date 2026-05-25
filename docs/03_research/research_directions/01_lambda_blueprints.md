# Direction 1: Lambda-blueprints, developed rigorously

> **Parent doc**: [`2A_R2_5_lambda_blueprints.md`](../../../experiments/arithmetic_geometric/2A_R2_5_lambda_blueprints.md) (the original R2.5 proposal). This document is the operational execution roadmap.
>
> **Phase in proof_program.md**: Phase 1 (years 1-2).
>
> **Headline**: develop the hybrid framework combining Lorscheid's blueprints with Borger's Adams operations into a full categorical and computational theory of "Lambda-blueprints" sufficient to host an arithmetic intersection theory on Spec(Z) x_F1 Spec(Z).

## 1. Problem statement

A Lambda-blueprint is proposed (R2.5) as a triple (B, B-bullet, {psi_p}_p prime) where:
- (B, B-bullet) is a Lorscheid blueprint: B is a semiring, B-bullet is a multiplicative monoid generating B, and the blueprint structure encodes which addition relations hold.
- {psi_p} is a family of commuting endomorphisms psi_p: B -> B satisfying:
  - psi_p preserves B-bullet (the multiplicative structure).
  - psi_p(x) ≡ x^p modulo the blueprint relations (Fermat-Frobenius compatibility).
  - psi_p ∘ psi_q = psi_q ∘ psi_p for all primes p, q.

The category Lambda-Blpr should:
- Have F_1 (the trivial blueprint) as initial object.
- Contain Lambda-Rings as a full subcategory (a ring R is a blueprint with B = B-bullet, so a Lambda-ring becomes a Lambda-blueprint with the same structure).
- Contain Blpr as a full subcategory (a blueprint without Lambda-action is a Lambda-blueprint with trivial psi_p).
- Admit fiber products in particular Spec(Z) x_F1 Spec(Z) should compute to a non-trivial 2-dimensional Lambda-blueprint.

The first task is to make this rigorous.

## 2. What "done" looks like

A 30-50 page paper containing:

1. The precise definition of Lambda-blueprint, including the Fermat-Frobenius condition in blueprint language.
2. Proof that Lambda-Blpr forms a well-defined category: morphisms preserve the Lambda-structure, composition is well-defined, identity exists.
3. Embedding theorems: Lambda-Rings -> Lambda-Blpr and Blpr -> Lambda-Blpr are full faithful functors.
4. Fiber product existence theorem for Lambda-Blpr (or a precise characterization of when fiber products exist).
5. Explicit computation of Spec(Z) x_F1 Spec(Z) as a Lambda-blueprint.
6. The 17-constraint scorecard verified for Lambda-Blpr (predicted: 8 yes / 4 partial / 5 open).
7. D-H exclusion (K2) verified.

The paper should be publishable in Compositio Mathematica or Journal of the AMS.

## 3. Prerequisites

- Working knowledge of Lorscheid's blueprint geometry (Lorscheid 2010-2012; "The geometry of blueprints" Adv. Math. 229).
- Working knowledge of Borger's Lambda-algebraic geometry (Borger 2009 arXiv:0906.3146; Joyal's original Lambda-ring papers).
- Familiarity with Tits buildings, Weyl groups, and the classical F_1-geometry context.
- Comfort with categorical machinery: limits, colimits, adjunctions, fibered categories.

A strong PhD-level mathematician working through these prerequisites can begin Direction 1 after 3-6 months of literature study.

## 4. Sub-problems and milestones

### 4.1 Define Fermat-Frobenius in blueprint language

The key new structural ingredient. In Lambda-Rings, psi_p(x) ≡ x^p (mod p) is a relation in the ring. In blueprints, addition is replaced by a multivalued / relation structure. The Fermat-Frobenius condition must be stated as a blueprint-relation: roughly, psi_p(x) - x^p should be in the "blueprint ideal" associated to p.

**Milestone**: precise definition with verification that it specializes correctly to Lambda-Rings (when the blueprint is a ring) and to Tits/Deitmar (when there is no Lambda-action).

### 4.2 Verify the category structure

Check: composition of Lambda-blueprint morphisms is well-defined, identity is a Lambda-blueprint morphism, the category satisfies the basic axioms.

**Milestone**: lemma + proof, ~5 pages.

### 4.3 Embedding from Lambda-Rings

Show U: Lambda-Rings -> Lambda-Blpr is full and faithful. This is straightforward if 4.1 is correct.

**Milestone**: theorem + proof, ~3 pages.

### 4.4 Embedding from Blpr

Show V: Blpr -> Lambda-Blpr (with trivial psi_p) is full and faithful. Straightforward.

**Milestone**: theorem + proof, ~2 pages.

### 4.5 Fiber products

The MAIN technical task. Fiber products in Blpr exist in some cases (Lorscheid 2012); fiber products in Lambda-Rings exist via the big Witt ring functor. Combining: fiber products in Lambda-Blpr should exist when the underlying blueprint fiber product exists AND the Lambda-structures are compatible.

**Milestone**: theorem characterizing when fiber products exist, with explicit construction in the affirmative case. ~10-15 pages.

### 4.6 Compute Spec(Z) x_F1 Spec(Z)

Apply 4.5 to the specific case Z over F_1 (the initial Lambda-blueprint). Compare to:
- Borger's Spec(W(Z)) via the big Witt ring functor.
- Lorscheid's (Z x Z, doubled relations).

**Milestone**: explicit description of the Lambda-blueprint Spec(Z) x_F1 Spec(Z). Show it has dimension 2 in an appropriate sense. Compare structurally to Borger and Lorscheid candidates. ~5-10 pages.

### 4.7 Scorecard verification

Apply the 2A 17-constraint framework to Lambda-Blpr. Verify or revise the R2.5 predicted scorecard (8 yes / 4 partial / 5 open).

**Milestone**: scorecard with detailed analysis of each constraint, ~5-10 pages.

### 4.8 D-H exclusion

Show that D-H is excluded from Lambda-Blpr by construction (K2). This should follow from R1's structural reason (linear combinations of Dirichlet series not constructible) applied to the new framework.

**Milestone**: lemma + proof, ~2 pages.

## 5. Falsifiability

The direction is FALSIFIED (and the framework should be abandoned) if:

- 4.1 fails: no consistent definition of Fermat-Frobenius in blueprint language. The Lambda-structure does not compatibly mesh with the blueprint structure.
- 4.5 fails: fiber products do not exist for the natural Z over F_1 case. The framework is too rigid.
- 4.7 reveals fewer than 6 yes scores in the scorecard. The hybrid is no better than its parents and offers no progress.
- 4.6 produces Spec(Z) x_F1 Spec(Z) = Spec(Z) (a collapse). Same as Deitmar's failure mode.

In any of these cases, the program should pivot to direction 2 (Borger+Connes hybrid) or abandon the hybrid approach in favor of one of the parent frameworks.

## 6. Estimated effort

3-6 postdoc-years for the rigorous development. Calendar time: 1-2 years for a small research group (2-3 people).

The paper is publishable as a standalone contribution to F_1-geometry even if the broader proof program doesn't reach its target.

## 7. Connections

- **Direction 2** (Borger+Connes hybrid): parallel hybrid framework. R2.5 and R4 are complementary; success of either OR both is useful.
- **Direction 3** (prismatic cohomology): the next step is to apply prismatic cohomology to the Lambda-blueprint analog of Spec(W(Z)).
- **Direction 8** (Hodge index theorem): the surface produced in 4.6 is the surface on which direction 8 must construct intersection theory and Hodge index.
- **R1** ([`2A_R1_DH_exclusion.md`](../../../experiments/arithmetic_geometric/2A_R1_DH_exclusion.md)): D-H exclusion at K2 for the new framework follows the same structural argument.

## 8. References

- Lorscheid, O. (2012). *The geometry of blueprints*. Adv. Math. 229(3).
- Borger, J. (2009). *Lambda-rings and the field with one element*. arXiv:0906.3146.
- Joyal, A. (1985). *Lambda-anneaux et vecteurs de Witt*. CR Math. Rep. Acad. Sci. Canada 7.
- Cartier, P. (1956). *Une nouvelle opération sur les formes différentielles*. CR Acad. Sci. Paris 244.
- Toen, B.; Vaquie, M. (2009). *Au-dessous de Spec Z*. J. K-Theory 3(3).

## 9. Status

This direction is **research-grade, beyond project scope**. The 2A R2.5 dossier provides the proposal; this document provides the operational specification. Execution requires a research mathematician at the postdoc-or-faculty level operating over 1-2 years.

Independently publishable as a major contribution to F_1-geometry regardless of whether the broader proof program reaches its target.
