# 2A: Methodology for Proposing and Evaluating Candidate Constructions

> Companion to [2A_weil_proof_diff.md](2A_weil_proof_diff.md), specifically the 17-constraint list in §5. This document operationalizes that list into a workable evaluation framework: precise predicates for each constraint, a standardized submission template for new candidates, current scorecards for the major candidates, and methodology notes on weighting, combinability, and kill criteria.
>
> The point is to make the Arch 2 construction problem **legible and tractable** rather than vague. If someone proposes a new construction tomorrow, we should be able to score it against the same checklist that scores Connes, Deninger, Borger, etc.

## I. Refined constraint checklist (checkable predicates)

For each constraint from [2A §5](2A_weil_proof_diff.md#5-characteristics-of-the-missing-mathematics-what-would-it-have-to-do), here is a checkable predicate (what would constitute evidence that the constraint is satisfied), plus dependency notes (which other constraints this one builds on).

### §5.1 — Base scheme below $\mathbb{Z}$

**(i) Canonical morphism $\mathrm{Spec}(\mathbb{Z}) \to S$.**

- *Predicate*: The candidate defines an object $S$ (in some category of "generalized schemes" or analogous) and exhibits a morphism $\mathrm{Spec}(\mathbb{Z}) \to S$. The morphism is canonical: it does not depend on auxiliary choices.
- *Evidence form*: A published definition of $S$ as a category-theoretic / scheme-theoretic object, plus a construction of the morphism with a uniqueness statement.
- *Dependencies*: none (foundational).
- *Status verdicts*: ✅ if definition + morphism + canonicity proof exists; 🟡 if definition exists but canonicity is informal; ❌ if no plausible $S$ has been defined.

**(ii) Non-trivial fiber product $\mathrm{Spec}(\mathbb{Z}) \times_S \mathrm{Spec}(\mathbb{Z})$.**

- *Predicate*: The fiber product, computed within the candidate's category, is a 2-dimensional object (in some meaningful sense: Krull dim, cohomological dim, or topological dim, consistent with how the candidate measures dimension).
- *Evidence form*: An explicit computation of the fiber product within the candidate's framework, plus a dimension calculation.
- *Dependencies*: (i).
- *Status verdicts*: ✅ if computation + dim = 2 proof; 🟡 if dim is computed but the candidate's notion of "dimension" doesn't match what Weil's proof needs; ❌ if fiber product collapses to a 1-dim object.

**(iii) Compatibility with $\mathbb{F}_q$.**

- *Predicate*: There is a morphism $\mathrm{Spec}(\mathbb{F}_q) \to S$ for each $q$, and the candidate's structure on $\mathrm{Spec}(\mathbb{F}_q) \times_S \mathrm{Spec}(\mathbb{F}_q)$ recovers standard scheme theory.
- *Evidence form*: A reduction theorem showing the candidate framework, restricted to function-field arithmetic, gives the same answers as ordinary $\mathbb{F}_q$-scheme theory.
- *Dependencies*: (i), (ii).
- *Status verdicts*: ✅ if reduction theorem proved; 🟡 if reduction is plausible but informal; ❌ if the candidate is incompatible with function-field schemes.

### §5.2 — Cohomology

**(iv) Finite-dimensional cohomology (or trace class).**

- *Predicate*: There is a cohomology functor $H^*$ from the candidate's category to vector spaces / Hilbert spaces such that $H^i(\mathrm{Spec}(\mathbb{Z}) \times_S \mathrm{Spec}(\mathbb{Z}))$ is either finite-dimensional or trace-class.
- *Evidence form*: A definition of the cohomology functor plus a finiteness theorem for the surface.
- *Dependencies*: (i)-(iii).
- *Status verdicts*: ✅ if cohomology defined + finiteness proved; 🟡 if cohomology defined but finiteness is conjectural; ❌ if cohomology is undefined or known to be ill-behaved.

**(v) Poincaré duality.**

- *Predicate*: A non-degenerate pairing $H^i \otimes H^{2-i} \to H^2$ that, at the L-function level, produces the functional equation $\xi(s) = \xi(1-s)$ as a corollary.
- *Evidence form*: A proof of the pairing's non-degeneracy plus a derivation of the functional equation from it.
- *Dependencies*: (iv).
- *Status verdicts*: ✅ if pairing constructed + non-degeneracy proved + functional equation derived; 🟡 if pairing is partial or functional equation is added separately; ❌ if no pairing or the pairing degenerates.

**(vi) Cycle class map and intersection pairing on $H^2$.**

- *Predicate*: Divisors on the surface have well-defined cycle classes in $H^2$, with a symmetric bilinear pairing $D_1 \cdot D_2$ that agrees with ordinary intersection theory in the $\mathbb{F}_q$-case.
- *Evidence form*: Definition of the cycle class map, proof of bilinearity, comparison theorem with $\mathbb{F}_q$-intersection theory.
- *Dependencies*: (iv), (v).
- *Status verdicts*: ✅ if all three; 🟡 if defined but comparison is informal; ❌ if no cycle class theory available.

**(vii) Künneth formula.**

- *Predicate*: $H^*(\mathrm{Spec}(\mathbb{Z}) \times_S \mathrm{Spec}(\mathbb{Z})) \cong H^*(\mathrm{Spec}(\mathbb{Z})) \otimes H^*(\mathrm{Spec}(\mathbb{Z}))$.
- *Evidence form*: A proof of the Künneth isomorphism in the candidate framework.
- *Dependencies*: (iv).
- *Status verdicts*: ✅ if proved; 🟡 if proved in a restricted setting; ❌ if the cohomology fails Künneth.

### §5.3 — Frobenius substitute

**(viii) Spectrum matches $\zeta$ zeros.**

- *Predicate*: An endomorphism (or flow) $F$ on $H^1(\mathrm{Spec}(\mathbb{Z}))$ (or the cohomology of the appropriate object) whose spectrum is in bijection with $\{\gamma_n\}$ (imaginary parts of zeta zeros), with $|F|$ acting as multiplication by $\sqrt q$-analogue on relevant subspaces.
- *Evidence form*: Construction of $F$ + spectral theorem identifying the spectrum.
- *Dependencies*: (iv).
- *Status verdicts*: ✅ if construction + spectral identification; 🟡 if the operator is defined but the spectral identification is conjectural; ❌ if no such operator can exist.

**(ix) Lefschetz trace formula reproducing the explicit formula.**

- *Predicate*: A formula $|\text{Fix}(F^k)| = \sum_i (-1)^i \mathrm{tr}(F^k \mid H^i)$ that, when unpacked, reproduces Riemann's / Weil's explicit formula for $\zeta$.
- *Evidence form*: Statement of trace formula + derivation of explicit formula from it.
- *Dependencies*: (iv), (viii).
- *Status verdicts*: ✅ if trace formula proved and explicit formula recovered; 🟡 if trace formula is conjectural but plausible; ❌ if no candidate trace formula matches.

**(x) Euler-factor compatibility at each prime.**

- *Predicate*: At each prime $p$, the local action of $F$ on a localized version of the cohomology produces $(1 - p^{-s})^{-1}$ for $\zeta$, and analogous local Euler factors for L-functions of arithmetic objects (Dirichlet, Hecke, etc.).
- *Evidence form*: Local-global decomposition of the cohomology + computation of local Euler factors.
- *Dependencies*: (i), (iv), (viii).
- *Status verdicts*: ✅ if local-global structure built and Euler factors computed; 🟡 if Euler factors are recovered for $\zeta$ but not for general L-functions; ❌ if no Euler product structure emerges.

### §5.4 — Hodge index positivity

**(xi) Hodge index theorem on the surface.**

- *Predicate*: The intersection form on Pic (or Néron-Severi-analog) of $\mathrm{Spec}(\mathbb{Z}) \times_S \mathrm{Spec}(\mathbb{Z})$ has signature $(1, \rho - 1)$.
- *Evidence form*: Statement of the theorem + proof within the candidate's framework + computation of $\rho$.
- *Dependencies*: (vi), (vii).
- *Status verdicts*: ✅ if theorem stated + proved + signature computed; 🟡 if stated but proof requires RH-strength input; ❌ if the signature is wrong or the form is degenerate.

**(xii) Provable without RH input.**

- *Predicate*: The proof of (xi) does NOT use, as input, RH (or any statement equivalent to RH, including: Weil positivity for $\zeta$, the Riemann hypothesis for any specific L-function in the Selberg class, GRH, etc.).
- *Evidence form*: The proof of (xi) is examined for its input hypotheses. The hypothesis list does not include any RH-equivalent.
- *Dependencies*: (xi).
- *Status verdicts*: ✅ if independent proof; 🟡 if proof reduces RH to a different conjecture that is "morally easier" but unproven; ❌ if proof uses RH or RH-equivalent.

This is the deepest constraint and currently the hardest to satisfy. Most "RH proofs" in the literature reduce to (xii) and fail it: they prove some positivity that is morally equivalent to RH.

**(xiii) Castelnuovo-Severi-style applicability.**

- *Predicate*: The Hodge index theorem from (xi) can be applied to divisors of the type "Frobenius graph minus scalar diagonal" to yield $|\alpha|^2 = $ (analogue of $\sqrt q$ for the $\mathbb{Z}$-case, which is the critical line $\Re(s) = 1/2$).
- *Evidence form*: Explicit construction of the relevant divisors + application of (xi) + derivation of $\Re(s) = 1/2$.
- *Dependencies*: (xi), (xii).
- *Status verdicts*: ✅ if RH derived; 🟡 if derivation requires extra inputs; ❌ if the divisors don't have the right intersection signature.

### §5.5 — Test cases

**(xiv) Recovery of function-field RH.**

- *Predicate*: When restricted to a curve $C / \mathbb{F}_q$, the candidate framework recovers Weil's RH for $L(C, T)$, with the same Frobenius eigenvalues and the same positivity argument.
- *Evidence form*: A reduction theorem from the candidate framework to Weil/Deligne.
- *Dependencies*: (iii), (xiii).
- *Status verdicts*: ✅ if reduction proved; 🟡 if reduction plausible but informal; ❌ if the candidate framework gives different (or incompatible) answers in the function-field case.

**(xv) Dirichlet L-functions.**

- *Predicate*: For Dirichlet character $\chi$, the candidate produces $L(s, \chi)$ from a twisted version of its cohomology, with Frobenius-substitute eigenvalues at the zeros of $L(s, \chi)$.
- *Evidence form*: Construction of the twisted cohomology + identification of its spectrum with $L(s, \chi)$ zeros.
- *Dependencies*: (viii), (x).
- *Status verdicts*: ✅ if construction + spectrum identification; 🟡 if construction exists but spectrum is conjectural; ❌ if Dirichlet L-functions don't fit the framework.

**(xvi) Selberg class as natural domain.**

- *Predicate*: L-functions in the Selberg class (Euler product + functional equation + Ramanujan-on-average) are naturally parameterized by appropriate twists in the candidate framework, with the analytic conductor varying continuously with the framework's parameters.
- *Evidence form*: An equivalence (or near-equivalence) between Selberg-class L-functions and a subcategory of "objects in the candidate framework."
- *Dependencies*: (xv).
- *Status verdicts*: ✅ if equivalence proved; 🟡 if equivalence sketched; ❌ if Selberg class doesn't fit.

**(xvii) Davenport-Heilbronn falls OUTSIDE the framework.**

- *Predicate*: The Davenport-Heilbronn L-function (functional equation but no Euler product, known to have off-line zeros) is NOT predicted to satisfy RH by the framework. Specifically: D-H lacks the local-global decomposition (x), so the framework's RH conclusion does not apply.
- *Evidence form*: Demonstration that D-H is not in the framework's domain + verification that the framework's RH proof does not "accidentally" prove RH for D-H.
- *Dependencies*: (x), (xv), (xvi).
- *Status verdicts*: ✅ if D-H is explicitly excluded; 🟡 if exclusion is implicit but plausible; ❌ if the framework would prove RH for D-H (which is known false), thereby invalidating the framework.

**This is the sharpest kill criterion.** Any candidate that "proves RH" without distinguishing Euler-product from non-Euler-product L-functions is wrong. D-H is the wrong-approach detector for Arch 2 just as it was for Arch 1, 3, 4.

## II. Candidate submission template

To propose a new candidate construction, fill out the following template and post it (e.g., as a new markdown file in this directory or as a pull request).

```markdown
# Candidate: <name>

**Authors / sources**: <published papers, lecture notes, or proposer if novel>
**One-sentence summary**: <what is the candidate, in one sentence>
**Year of first formulation**: <year>
**Most mature reference**: <link or citation to the most complete write-up>

## Description (1-2 paragraphs)

<What is the underlying object? What is the base $S$? How is the cohomology
defined? What is the Frobenius substitute? Is there a known partial positivity?>

## Per-constraint scorecard

| Constraint | Status | Justification |
|---|---|---|
| (i) Canonical Spec(Z) → S | ✅ / 🟡 / ⏳ / ❌ | <brief>  |
| (ii) Non-trivial fiber product | ✅ / 🟡 / ⏳ / ❌ | <brief>  |
| (iii) F_q compatibility | ✅ / 🟡 / ⏳ / ❌ | <brief>  |
| (iv) Finite-dim cohomology | ✅ / 🟡 / ⏳ / ❌ | <brief>  |
| (v) Poincaré duality | ✅ / 🟡 / ⏳ / ❌ | <brief>  |
| (vi) Cycle class / intersection | ✅ / 🟡 / ⏳ / ❌ | <brief>  |
| (vii) Künneth | ✅ / 🟡 / ⏳ / ❌ | <brief>  |
| (viii) Frobenius spectrum = ζ zeros | ✅ / 🟡 / ⏳ / ❌ | <brief>  |
| (ix) Lefschetz / explicit formula | ✅ / 🟡 / ⏳ / ❌ | <brief>  |
| (x) Euler-factor compatibility | ✅ / 🟡 / ⏳ / ❌ | <brief>  |
| (xi) Hodge index theorem | ✅ / 🟡 / ⏳ / ❌ | <brief>  |
| (xii) Provable without RH input | ✅ / 🟡 / ⏳ / ❌ | <brief>  |
| (xiii) Castelnuovo-Severi applicability | ✅ / 🟡 / ⏳ / ❌ | <brief>  |
| (xiv) Function-field RH recovery | ✅ / 🟡 / ⏳ / ❌ | <brief>  |
| (xv) Dirichlet L-functions | ✅ / 🟡 / ⏳ / ❌ | <brief>  |
| (xvi) Selberg class domain | ✅ / 🟡 / ⏳ / ❌ | <brief>  |
| (xvii) D-H excluded (kill criterion) | ✅ / 🟡 / ⏳ / ❌ | <brief>  |

Status legend:
- ✅ Satisfied: published proof or rigorous construction
- 🟡 Partial: defined but incomplete, restricted setting, or informal
- ⏳ Open: not yet addressed but no known obstruction
- ❌ Fails: known obstruction OR proof of impossibility OR known incompatible result

## Known gaps and open questions

<What's missing? What would have to be proven next to close the candidate?>

## Combinability

<Does this candidate combine cleanly with others? E.g., can it provide
the Frobenius substitute while another provides the base?>

## Kill-criterion check

<Does the candidate accidentally prove RH for Davenport-Heilbronn?
If unclear, what is the argument for why it doesn't?>
```

## III. Current candidate scorecard

Below, the major candidates as of $\sim$2025. Scoring is a working draft and reflects my current reading; corrections welcome.

### III.1 — Deitmar monoid schemes (2005)

**One-line**: $\mathbb{F}_1$ defined as the category of commutative monoids; schemes over $\mathbb{F}_1$ glue local pieces with monoid-valued sheaves.

| Constraint | Status | Note |
|---|---|---|
| (i) Spec(Z) → S | ✅ | $\mathbb{Z}$ is an "$\mathbb{F}_1$-algebra" in Deitmar's sense; morphism is canonical |
| (ii) Non-trivial fiber product | 🟡 | Defined, but the fiber product yields a 1-dim object in monoid-scheme dimension; intersection theory underdeveloped |
| (iii) $\mathbb{F}_q$ compatibility | ✅ | $\mathbb{F}_q$-schemes embed as monoid schemes with $\mathbb{F}_q^*$-monoid structure |
| (iv) Finite-dim cohomology | ❌ | No cohomology theory matching the infinite zeta spectrum; "cohomology" of monoid schemes is too rigid |
| (v)-(x) | ❌ | All inherited from (iv) being unaddressed |
| (xi)-(xiii) | ❌ | No Hodge index because no surface intersection theory |
| (xiv) | ✅ | Function-field case reduces correctly |
| (xv) | ❌ | Dirichlet L-functions not naturally encoded |
| (xvi) | ❌ | No |
| (xvii) | ⏳ | Vacuous since the framework doesn't prove RH for anything |

**Verdict**: Deitmar provides a clean (i)-(iii) but the cohomology slot (iv) is essentially empty. This is the early-2000s baseline that subsequent programs try to upgrade.

### III.2 — Lorscheid blueprints (2012)

**One-line**: A blueprint generalizes a commutative monoid by adding "relations" between sums of elements, giving a category that contains both monoid schemes and ordinary schemes.

| Constraint | Status | Note |
|---|---|---|
| (i) Spec(Z) → S | ✅ | $\mathbb{Z}$ is a blueprint |
| (ii) Non-trivial fiber product | 🟡 | Improved over Deitmar; fiber product is closer to a 2-dim object but the dimension is not unambiguously 2 |
| (iii) $\mathbb{F}_q$ compatibility | ✅ | Standard |
| (iv) Finite-dim cohomology | 🟡 | Some cohomology theories defined for blueprint schemes (Lorscheid-Pena), but not yet matching infinite zeta spectrum |
| (v)-(x) | ⏳ | Open; framework is mature enough to ask the questions |
| (xi)-(xiii) | ❌ | Same as Deitmar — no Hodge index |
| (xiv) | ✅ | |
| (xv), (xvi) | ⏳ | Open |
| (xvii) | ⏳ | Vacuous |

**Verdict**: Lorscheid improves on Deitmar in the fiber product slot but doesn't yet deliver the positivity (xi-xiii). Active development area.

### III.3 — Borger $\Lambda$-rings (2009)

**One-line**: $\mathbb{F}_1$ is reinterpreted via $\Lambda$-ring structure: a ring with commuting Adams operations $\{\psi_p\}$ that play the role of Frobenius at each prime.

| Constraint | Status | Note |
|---|---|---|
| (i) Spec(Z) → S | ✅ | $\mathbb{Z}$ has a canonical $\Lambda$-ring structure |
| (ii) Non-trivial fiber product | ⏳ | Fiber product in $\Lambda$-schemes; dimension question is open |
| (iii) $\mathbb{F}_q$ compatibility | ✅ | $\mathbb{F}_q^*$ has natural $\Lambda$ structure |
| (iv) Finite-dim cohomology | 🟡 | Witt-vector-style cohomologies under development |
| (v) Poincaré duality | ⏳ | Open |
| (vi) Cycle class | ⏳ | Open |
| (vii) Künneth | ⏳ | Open |
| **(viii) Frobenius spectrum** | 🟡 | **The Adams operations $\psi_p$ ARE candidate Frobenius substitutes, by design.** Most attractive feature. |
| (ix) Lefschetz | ⏳ | Open |
| (x) Euler factors | 🟡 | Adams operations give per-prime structure naturally |
| (xi)-(xiii) | ⏳ | Open |
| (xiv) | ✅ | |
| (xv), (xvi) | ⏳ | Open |
| (xvii) | ⏳ | Vacuous |

**Verdict**: Borger's $\Lambda$-ring approach is the most attractive on the Frobenius axis (viii, x): Adams operations are a natural arithmetic analogue. But the cohomological development (iv-vii) is incomplete, and the positivity slot (xi-xiii) is untouched.

### III.4 — Connes adèle class space (1999-)

**One-line**: The noncommutative quotient $\mathbb{A}_\mathbb{Q} / \mathbb{Q}^*$ with an action of $\mathbb{R}^*_+$; trace formula reproduces the explicit formula.

| Constraint | Status | Note |
|---|---|---|
| (i) Spec(Z) → S | 🟡 | The "base" is implicit (the noncommutative structure of $\mathbb{A}_\mathbb{Q}$); not in scheme form |
| (ii) Non-trivial fiber product | ❌ | The framework is noncommutative; standard fiber product not applicable |
| (iii) $\mathbb{F}_q$ compatibility | 🟡 | Connes-Consani have adelic analogues for function fields; reduction informal |
| (iv) Trace-class cohomology | ✅ | Trace-class operators on Hilbert space; well-defined |
| (v) Poincaré duality | 🟡 | Functional equation follows from a "scaling" symmetry, not a cohomological pairing |
| (vi) Cycle class | 🟡 | Substitute via noncommutative cycles, but the intersection theory is partial |
| (vii) Künneth | ❌ | Standard Künneth doesn't apply to noncommutative spaces |
| **(viii) Frobenius spectrum** | ✅ | **The $\mathbb{R}^*_+$ action has spectrum at $\zeta$ zeros (Connes' main result).** Most mature feature. |
| **(ix) Lefschetz** | ✅ | **Trace formula = explicit formula, derived in Connes 1999.** |
| (x) Euler factors | ✅ | Local factors at each prime via local components of $\mathbb{A}_\mathbb{Q}$ |
| **(xi)-(xiii) Hodge index positivity** | ❌ | **The deepest gap. Connes-Consani's positivity conjecture is either RH-equivalent or unproven.** |
| (xiv) | 🟡 | Function-field analogue works but the cohomological structure is different |
| (xv) Dirichlet L | ✅ | Adelic framework naturally accommodates Dirichlet L-functions |
| (xvi) Selberg class | 🟡 | Selberg-class L-functions parameterized by automorphic data; full domain unclear |
| (xvii) D-H excluded | 🟡 | **Probably**: D-H is non-automorphic, falls outside the adelic framework's natural domain. But the exclusion has not been rigorously argued in the literature I've seen. |

**Verdict**: Connes covers (i, iv, viii, ix, x) very well — the trace formula side is the most developed in any candidate. The framework's weakness is (vii) Künneth, the cycle class structure (vi), and especially (xi-xiii): no Hodge index theorem analogue, and the positivity conjecture remains open or RH-equivalent. The kill criterion (xvii) needs sharpening.

### III.5 — Deninger foliated cohomology (1998-)

**One-line**: A hypothetical foliated dynamical system $\bar X$ on which a flow $\Phi_t$ at $t = \log p$ has fixed points = closed points of $\mathrm{Spec}(\mathbb{Z})$.

| Constraint | Status | Note |
|---|---|---|
| (i) Spec(Z) → S | 🟡 | $\bar X$ would compactify $\mathrm{Spec}(\mathbb{Z})$, but $\bar X$ itself is not constructed |
| (ii) Non-trivial fiber product | ⏳ | Would follow from $\bar X$ being constructed |
| (iii) $\mathbb{F}_q$ compatibility | ✅ | Deninger's framework is consciously modeled on the function-field case |
| (iv) Finite-dim cohomology | 🟡 | Conjectural; leafwise cohomology proposed |
| (v) Poincaré duality | 🟡 | Conjectural via foliated structure |
| (vi) Cycle class | ⏳ | Open |
| (vii) Künneth | ⏳ | Open |
| **(viii) Frobenius spectrum** | 🟡 | **Flow $\Phi_t$ would have spectrum at $\zeta$ zeros, by design.** But $\Phi_t$ is not constructed. |
| (ix) Lefschetz | 🟡 | Conjectural |
| (x) Euler factors | 🟡 | Inherited from the flow's per-prime structure |
| (xi)-(xiii) | ⏳ | Conjectural |
| (xiv) | ✅ | |
| (xv)-(xvii) | ⏳ | Open |

**Verdict**: Deninger is the most ambitious candidate (full Weil-style picture) but everything is conjectural pending the construction of $\bar X$. The framework is more of a research program than a finished product.

### III.6 — Connes-Consani hyperring / characteristic-one geometry (2008-)

**One-line**: Combines Connes' adelic approach with a hyperring (multivalued addition) structure to build an arithmetic site $\mathcal{A}$ with a self-map analogous to Frobenius.

| Constraint | Status | Note |
|---|---|---|
| (i)-(iii) | 🟡 | $\mathcal{A}$ is constructed but the relationship to $\mathrm{Spec}(\mathbb{Z})$ is via the noncommutative-side rather than via base change |
| (iv) | 🟡 | Site cohomology defined |
| (v)-(vii) | ⏳ | Various partial results |
| (viii)-(x) | ✅ | Inherited from Connes' framework |
| (xi)-(xiii) | ❌ | Still no Hodge index analogue |
| (xiv) | 🟡 | |
| (xv)-(xvi) | 🟡 | |
| (xvii) | ⏳ | |

**Verdict**: Hybrid of Connes and $\mathbb{F}_1$ approaches. Inherits Connes' strengths on the Frobenius/trace formula side and the $\mathbb{F}_1$ weaknesses on the surface/Hodge index side.

### III.7 — Summary scorecard

| Candidate | (i)-(iii) Base | (iv)-(vii) Cohomology | (viii)-(x) Frobenius | (xi)-(xiii) Positivity | (xiv)-(xvii) Tests |
|---|---|---|---|---|---|
| Deitmar | ✅ ✅ ✅ | ❌ — — — | — — — | — — — | ✅ ❌ ❌ ✅ |
| Lorscheid | ✅ 🟡 ✅ | 🟡 ⏳ ⏳ ⏳ | ⏳ ⏳ ⏳ | ❌ ❌ ❌ | ✅ ⏳ ⏳ ✅ |
| Borger | ✅ ⏳ ✅ | 🟡 ⏳ ⏳ ⏳ | 🟡 ⏳ 🟡 | ⏳ ⏳ ⏳ | ✅ ⏳ ⏳ ✅ |
| Connes | 🟡 ❌ 🟡 | ✅ 🟡 🟡 ❌ | ✅ ✅ ✅ | ❌ ❌ ❌ | 🟡 ✅ 🟡 ✅ |
| Deninger | 🟡 ⏳ ✅ | 🟡 🟡 ⏳ ⏳ | 🟡 🟡 🟡 | ⏳ ⏳ ⏳ | ✅ ⏳ ⏳ ✅ |
| Connes-Consani | 🟡 🟡 🟡 | 🟡 ⏳ ⏳ ⏳ | ✅ ✅ ✅ | ❌ ❌ ❌ | 🟡 🟡 🟡 ✅ |

No candidate has even a partial ✅ on (xi-xiii) — the Hodge index positivity. This is the universally open constraint.

**The (xvii) column** was sharpened by R1 (see [2A_R1_DH_exclusion.md](2A_R1_DH_exclusion.md)): all six candidates now ✅ on D-H exclusion, with the underlying reason being that D-H's defining feature (linear combination → no Euler product) is not constructible within any geometric framework. Linear combinations are analytic operations on Dirichlet series, not geometric operations on schemes / Λ-rings / foliated spaces / adelic spaces. The candidates pass K2 by construction.

## IV. Methodology notes

### IV.1 — Weighting of constraints

Not all constraints are equally load-bearing. A working candidate could be partial on some and still useful; failing others is fatal.

**Fatal-if-failing** (any one rules out the candidate):
- **(xii)** Provability without RH input. A candidate that "proves RH" using RH-equivalent input is RH-trivial; it does no work.
- **(xvii)** D-H exclusion. A candidate that "proves RH" for D-H is wrong (since D-H is a known counterexample).
- **(xiv)** Function-field recovery. A candidate that gives the wrong answer for $C / \mathbb{F}_q$ is incompatible with established mathematics.

**Load-bearing** (essential but partially satisfying is OK in the near term):
- (xi) Hodge index theorem (depth)
- (ix) Lefschetz / explicit formula (depth)
- (viii) Frobenius spectrum (depth)

**Lightweight** (deferrable; failing these is recoverable):
- (xvi) Selberg class compatibility (could be argued post hoc)
- (xv) Dirichlet L-functions (analogous)
- (vii) Künneth (could be replaced by a different decomposition)

### IV.2 — Combinability of candidates

The framework is *modular*: different candidates can contribute different slots. A successful construction might be a hybrid:

- **Connes (viii-x) + Borger (i-iii, viii alternative)**: use Adams operations as the Frobenius substitute and the adelic trace formula side; combine via comparing the two Frobenius substitutes' spectra.
- **Lorscheid (i-iii) + Deninger (viii-x)**: use blueprints for the base and Deninger's flow for the Frobenius; the open task becomes constructing Deninger's $\bar X$ within the blueprint framework.
- **Connes (viii-xi) + Connes-Consani (i-vii)**: combine the trace formula apparatus with the hyperring structure.

The point of breaking down into 17 constraints is precisely to make these combinations EVALUABLE. A hybrid that solves all 17 (even if no single program does) is just as much a solution as a unified construction.

### IV.3 — What evidence counts

Different types of evidence are appropriate at different maturity stages:

- **Definition exists in a published paper** → at least 🟡 for definitional constraints (i, ii, iv).
- **Theorem stated + sketch of proof** → 🟡 if independent verification is plausible; ✅ if peer-reviewed.
- **Theorem stated but proof requires RH** → 🟡 (the constraint is met conditionally) or 🔴 for (xii) specifically.
- **Numerical verification in restricted setting** → 🟡 for constraints (xiv-xvii); insufficient for the construction constraints (i-xiii).
- **Computer-checked proof** → ✅ if the formal verification covers the constraint.

For all candidates currently on the scorecard, the evidence is "published mathematics papers in peer-reviewed journals" except where conjectural (marked ⏳).

### IV.4 — Kill criteria, sharpened

The framework should be able to RULE OUT bad candidates, not just rank good ones. Kill criteria so far:

- **K1 (RH-equivalence kill)**: if the candidate's proof of (xi) reduces RH to an equivalent statement, it fails (xii) and is RH-trivial.
- **K2 (D-H kill)**: if the candidate "proves RH" for an L-function that's known to have off-line zeros (D-H or Selberg-class counterexamples), it's wrong.
- **K3 (function-field kill)**: if the candidate gives different answers than Weil/Deligne for $C / \mathbb{F}_q$, it's incompatible.
- **K4 (Selberg-class blind kill)**: if the candidate "proves RH" without any L-function-specific input (i.e., for any L-function whatsoever, including those with no Euler product), it's wrong by K2.

K1 is the subtlest. Many proposed "proofs of RH" reduce RH to a different positivity statement that's not obviously easier; without an independent proof of that statement, the work is just shuffling rather than progressing. Distinguishing genuine progress from K1-style shuffling requires checking that the new positivity statement has a CONSTRUCTIVE / GEOMETRIC proof candidate, not just an analytic restatement.

### IV.5 — Reading new candidates

When a new paper claims progress on Architecture 2, evaluate it as follows:

1. **Identify which constraints (i-xvii) the paper addresses.** Most papers contribute to 1-3 constraints, rarely the full set.
2. **For each addressed constraint, ask: what's the predicate evidence?** Definition / theorem / numerical computation / etc.
3. **Check the kill criteria.** Does the paper accidentally also "prove RH" for D-H or other off-line-zero objects? Does its main theorem reduce RH to an RH-equivalent statement?
4. **Locate combinability**: does the paper's contribution fit with others' contributions to fill in slots they leave open?
5. **Update the scorecard** for the relevant candidate.

This process should be doable in $\sim$1 hour for a typical paper. The scorecard then becomes a living document of where the field stands.

## V. Where the gaps are, concretely

Putting the scorecard together, the open gaps are:

1. **(xi)-(xiii) Hodge index positivity**: **universally open across all candidates**. This is the central construction problem.
2. **(ii) Non-trivial fiber product**: open in most $\mathbb{F}_1$ programs; the candidates that satisfy (i) often have a trivial-or-collapsed fiber product. Resolving this requires a working definition of $\mathbb{F}_1$ that survives base-change.
3. **(vii) Künneth formula**: not addressed in the noncommutative candidates (Connes, Connes-Consani); fundamental obstruction since the surface has to decompose into the base.
4. **(xvii) D-H exclusion** (sharpening): the kill criterion has not been rigorously verified for Connes / Deninger / Borger. Tightening this would also tighten what each candidate predicts about which L-functions satisfy RH.

The natural next-step research directions, ranked by tractability:

- ~~**R1**: Sharpen (xvii) for each candidate.~~ **Complete** ([2A_R1_DH_exclusion.md](2A_R1_DH_exclusion.md)). All six candidates pass K2 (D-H exclusion). The structural reason: D-H's defining feature (linear combination of $L(s, \chi)$'s without Euler product) is not constructible within any geometric framework. Linear combination is an analytic operation on Dirichlet series, not a geometric operation on the underlying objects. The candidates are K2-safe under the Selberg conjecture; if Selberg fails (i.e., some Euler-product L-function has off-line zeros), K2 becomes a live concern, but no such counterexample is known.
- ~~**R2**: Compute (ii) explicitly for one of the $\mathbb{F}_1$ candidates.~~ **Complete** ([2A_R2_fiber_product.md](2A_R2_fiber_product.md), with per-candidate dossiers [2A_borger_dossier.md](2A_borger_dossier.md) and [2A_lorscheid_dossier.md](2A_lorscheid_dossier.md)). Findings: Borger's framework gives $\mathrm{Spec}(\mathbb{Z}) \times_{\mathbb{F}_1} \mathrm{Spec}(\mathbb{Z}) \simeq \mathrm{Spec}(W(\mathbb{Z}))$ via the big Witt ring functor (the right adjoint to the forgetful functor U: Λ-Rings → Rings). Lorscheid's framework gives the blueprint $(\mathbb{Z} \times \mathbb{Z}, \text{doubled relations})$ which is 2-dimensional in Lorscheid's blueprint dimension theory. **Both candidates produce non-trivial surface-like objects** (constraint (ii) upgraded from ⏳/🟡 to 🟡 for both, with sharper picture). **Neither has developed intersection theory** on the resulting surface — the next downstream constraints (vi) and (xi) remain open. **The dossier comparison surfaces a natural hybrid**: Borger is strong on Frobenius (viii) but weak on surface (ii); Lorscheid is strong on surface (i-iii) but weak on Frobenius.
- ~~**R2.5**: Sketch the Λ-blueprint hybrid.~~ **Proposed** ([2A_R2_5_lambda_blueprints.md](2A_R2_5_lambda_blueprints.md)). A Λ-blueprint is a blueprint (B, B^•) enriched with commuting Adams operations {ψ_p}_p satisfying the Fermat-Frobenius condition modulo the blueprint relations B^•. The category Λ-Blpr would have 𝔽₁ as initial object, ℤ as the canonical "next level" (with ψ_p = identity), and inherit ordinary Λ-Rings and ordinary Blpr as subcategories. Predicted scorecard: **8 ✅ / 4 🟡 / 5 ⏳** — constraints (i, ii, iii, viii, x, xiv, xvii) inherited from one or both parents at ✅, with (vi) and (ix) improved by the hybrid structure but still 🟡, and (xi-xiii) Hodge index positivity still ⏳. **Status: research proposal, not established mathematics.** Estimated effort to develop rigorously: thesis-level project. Whether this is the right hybrid (vs Borger + prismatic cohomology, vs Lorscheid + hyperrings) remains an open question.
- **R3**: For Connes-Consani, identify whether the noncommutative positivity conjecture is K1 (RH-equivalent) or whether it has an independent constructive proof candidate. This is the hardest but most important.
- **R4**: Explore hybrid candidates (per IV.2). The "Borger Frobenius + Connes trace formula" hybrid is the most promising on paper.

### V.1 — A specific 2D target (potential 2D companion experiment)

The 17-constraint framework also suggests a concrete numerical micro-target that the experimental thread could pursue. Recall constraint (viii): the Frobenius substitute's spectrum should match $\zeta$ zeros. For Borger's $\Lambda$-ring framework, the Adams operations $\psi_p$ give one operator per prime. A numerical question: at small $p$ and small-rank $\Lambda$-modules, do the eigenvalues of $\psi_p$ on those modules concentrate near the imaginary parts of $\zeta$ zeros?

This is a "test case" experiment: it wouldn't prove anything but would either provide circumstantial support for Borger's Frobenius identification or rule it out. The infrastructure (mpmath for $\zeta$ zeros, sympy for $\Lambda$-ring algebra) is already in place.

Queued as **2E (numerical Adams-operation spectrum probe)** — not pursued in 2A but mentioned here for the experimental follow-up.

## VI. Future updates to this scorecard

This is a living document. When a new candidate is proposed or an existing candidate makes progress:

1. Fork the submission template (§II), fill it in, and add it to a new section in §III.
2. Update the summary scorecard (§III.7) accordingly.
3. Re-evaluate the gaps in §V and update the next-step research directions.

The goal is for this document to give a snapshot, at any time, of "where the Architecture 2 construction problem stands and what's worth working on next."

## References

See [2A_weil_proof_diff.md §6 references](2A_weil_proof_diff.md#references) for primary literature. Additional methodology / philosophy references:

- Bombieri, E. (2000). *Problems of the Millennium: The Riemann Hypothesis* (Clay Mathematics Institute). The Clay description is itself an early version of an Arch-2-style diff: it explicitly compares the function-field case to the integer case.
- Connes, A.; Consani, C.; Marcolli, M. (2007). *Noncommutative geometry and motives: the thermodynamics of endomotives*. Adv. Math. 214(2). Provides Connes-Consani's most developed view of the Frobenius / trace formula correspondence.
- Borger, J. (2009). *$\Lambda$-rings and the field with one element*. arXiv:0906.3146. The Borger framework's foundational paper.
- Lorscheid, O. (2012). *Blueprints — Towards Absolute Arithmetic?* J. Number Theory 144. Lorscheid's most complete blueprint development.
- Manin, Y. (2008). *Cyclotomy and analytic geometry over $\mathbb{F}_1$.* arXiv:0809.1564. Manin's view of the $\mathbb{F}_1$ landscape.
- Deninger, C. (2008). *Analogies between analysis on foliated spaces and arithmetic geometry.* Groups and Analysis: The Legacy of Hermann Weyl, 174–190. Deninger's mature program statement.

## Suggested editorial workflow

When evaluating a new claim or paper:

1. Read the paper twice. First for overall picture, second tracking specific contributions to constraints (i)-(xvii).
2. Note which constraints the paper attempts (don't infer from absence: if a paper doesn't mention constraint $X$, mark it ⏳ rather than ❌).
3. Score the addressed constraints conservatively. ✅ requires unambiguous published proof; 🟡 is the default for "looks promising but I'm not certain."
4. Cross-check against kill criteria K1-K4 (§IV.4). Most papers that claim "RH progress" fail K1 because their main theorem reduces RH to an RH-equivalent statement.
5. Add the result to §III as a new subsection; update §III.7 summary.
6. Update §V (gaps and next steps) if the scoring changes the picture.

The whole loop should take a few hours per paper. Doing this systematically across the recent literature would produce a substantial body of evaluation data and likely surface combinability opportunities (per §IV.2) that haven't been noticed.
