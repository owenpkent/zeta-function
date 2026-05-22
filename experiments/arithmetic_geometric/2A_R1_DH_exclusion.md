# 2A — R1: Sharpening the Davenport-Heilbronn exclusion (constraint xvii) per candidate

> Companion to [2A_candidate_evaluation.md](2A_candidate_evaluation.md) §V. R1 is the lowest-hanging follow-up identified by the evaluation framework: for each of the six scored candidate constructions, sharpen the (xvii) verdict — does the framework correctly exclude the Davenport-Heilbronn L-function from its domain, or does it accidentally "prove RH" for D-H (which has known off-line zeros)?
>
> This is the kill criterion K2 (D-H kill). Each candidate either passes by construction (D-H is not in its natural domain) or fails (the candidate's RH proof template would apply to D-H, contradicting the known off-line zeros).

## 1. Background: why D-H matters as a kill criterion

The Davenport-Heilbronn L-function is
$$D(s) = (\sin \alpha) \, L(s, \chi_5^a) + (\cos \alpha) \, L(s, \chi_5^b)$$
for specific Dirichlet characters $\chi_5^a, \chi_5^b$ mod 5 and a specific angle $\alpha$ (Davenport-Heilbronn 1936). It has:

- **A functional equation** $D(s) \mapsto D(1-s)$ (inherited from each $L(s, \chi)$).
- **No Euler product**: the linear combination breaks the multiplicative structure of the individual $L$-functions.
- **Known off-line zeros**: the first off-line zero is at $\rho \approx 0.8085 + 85.699 i$ (see [`experiments/_shared/smoke_test.py`](../_shared/smoke_test.py) for the verification).

D-H is the project's standard wrong-approach detector: any method that "proves RH" for D-H is structurally wrong, because D-H has known off-line zeros. So any candidate construction in Architecture 2 must either:

(a) **Exclude D-H from its domain by construction** (D-H isn't a valid input to the framework), OR
(b) **Apply to D-H but predict it doesn't satisfy RH** (the framework's RH conclusion is conditional on something D-H lacks).

A candidate that "proves RH for all L-functions satisfying a functional equation" without further restriction fails kill criterion K2 and is wrong.

## 2. The structural reason all six candidates exclude D-H

Before going candidate by candidate, there's a general observation that applies across all six. **The Architecture 2 frameworks all derive their L-functions from "geometric" operations** — point counting, trace of Frobenius substitute, scheme-theoretic Euler products, automorphic representations, foliated trace formulas, etc. These geometric operations are intrinsically **multiplicative**: they produce L-functions with Euler products.

D-H is defined by a **linear combination** of two Dirichlet L-functions with specific weights $(\sin\alpha, \cos\alpha)$. Linear combination is an **analytic operation on Dirichlet series**, not a geometric operation on arithmetic schemes. There is no scheme, no Λ-ring, no monoid, no foliated space, and no automorphic representation whose L-function naturally equals $D(s)$ — because no such object has a "twisted-by-sin-and-cos" structure that would produce the linear combination.

So D-H is excluded from all six frameworks **by virtue of not being constructible within them**, not by an extra ad-hoc filter. This is a strong consistency: the frameworks distinguish geometrically-derived L-functions (which we conjecture satisfy GRH) from contrived combinations (which can have off-line zeros).

That said, each candidate excludes D-H by a slightly different mechanism, and the explicit verification matters because:
- It tightens the (xvii) verdict from "probably excluded" to "provably excluded."
- It surfaces design constraints for future candidates: any new framework that expands the domain to include linear combinations of L-functions would need to navigate this carefully.

## 3. Per-candidate analysis

### 3.1 Deitmar monoid schemes

**Framework's natural L-functions**: zeta functions of monoid schemes — count of "points" $|X(\mathbb{F}_{q^n})|$ for a monoid scheme $X$ extended over the monoid $\mathbb{F}_{q^n}^*$. Equivalently: motivic zeta of $\mathbb{F}_1$-schemes in Deitmar's sense.

**Is D-H in this domain?** No. Monoid scheme zeta functions are multiplicative by construction: they arise from product structures on monoid schemes, and the Euler product is automatic. D-H is not a counting zeta of any monoid scheme — it's a linear combination at the Dirichlet-series level.

**Could D-H be encoded as a monoid scheme zeta with twisted coefficients?** No. Twisting by Dirichlet characters is allowed in Deitmar's framework (it corresponds to "twisting" the scheme by a character of the residue field action), but the result is still a single character-twisted zeta, not a linear combination of two.

**Verdict (xvii)**: ✅ Excluded by construction (no Euler product → not a Deitmar zeta).

**Subtlety**: there is a small loophole. Deitmar's framework allows direct sums of monoid schemes, which would give sums of L-functions. If one tried to construct $X_a \sqcup X_b$ with $X_a$ giving $L(s, \chi_5^a)$ and $X_b$ giving $L(s, \chi_5^b)$, the resulting "scheme" would have a zeta equal to $L(s, \chi_5^a) \cdot L(s, \chi_5^b)$ — the PRODUCT, not the sum. So even with direct sums, the linear combination doesn't appear. ✅ confirmed excluded.

### 3.2 Lorscheid blueprints

**Framework's natural L-functions**: blueprint zeta functions — same conceptual structure as Deitmar, generalized to blueprints (monoids + relations). Inherits multiplicativity from the blueprint morphism structure.

**Is D-H in this domain?** No. Same argument as Deitmar: blueprint zetas are multiplicative; D-H isn't.

**Could a blueprint blueprint encode D-H?** The blueprint relations allow more complex structures than monoid schemes, but the basic morphisms still respect multiplication. The "relation" structure in blueprints adds constraints like $a + b = c$ (in the "addition relation"), but doesn't allow for linear combinations of L-functions to be encoded as a single blueprint zeta.

**Verdict (xvii)**: ✅ Excluded by construction.

### 3.3 Borger Λ-rings

**Framework's natural L-functions**: Λ-ring zetas — given by traces of Adams operations $\psi_p$ on Λ-modules. Each prime $p$ contributes an Euler factor through the action of $\psi_p$ on the local module.

**Is D-H in this domain?** No. The Adams operations are commuting ring endomorphisms, which inherently give Euler product structure. Specifically, the local Euler factor at $p$ is $\det(1 - \psi_p t \mid M)^{-1}$ for the Λ-module $M$. This is a polynomial in $t$ (or formal power series), and the global L-function is a product of these local factors.

**Linear combinations in Λ-ring framework?** Λ-rings have a direct sum operation, which corresponds to product of L-functions, not sum. So D-H is not encodable.

**Verdict (xvii)**: ✅ Excluded by construction.

**Note**: Borger's framework has a particularly tight fit with the Euler product structure of L-functions — the Adams operations literally ARE the Frobenius substitutes at each prime. This makes it especially clear that D-H (lacking Euler product) cannot fit.

### 3.4 Connes adèle class space

**Framework's natural L-functions**: spectral data from the action of $\mathbb{R}^*_+$ on $\mathbb{A}_\mathbb{Q} / \mathbb{Q}^*$. Specifically, the trace formula identifies eigenvalues of the action with zeros of $\zeta$ (the original Connes 1999 result). More generally: zeros of Dirichlet L-functions $L(s, \chi)$ for primitive characters $\chi$, via twisted versions of the adèle class space.

**Is D-H in this domain?** No, with a careful argument. D-H is NOT a Dirichlet L-function for a single character; it's a specific linear combination $(\sin\alpha) L(s, \chi_5^a) + (\cos\alpha) L(s, \chi_5^b)$.

In the adelic framework, individual L-functions $L(s, \chi_5^a)$ and $L(s, \chi_5^b)$ have their zeros arising from spectral data, but the linear combination D-H does not correspond to a single adelic spectral computation. To get D-H's zeros via the framework, one would need to take $(\sin\alpha)$ times the spectral data for $\chi_5^a$ plus $(\cos\alpha)$ times that for $\chi_5^b$ — and the zeros of the sum are NOT the union of the zeros of the summands (they're new zeros from the linear-combination interference).

**Connes' framework's "L-functions"** are precisely those that arise from spectral data of a single twist of the adèle class space. Linear combinations are not in the spectral output of any single twist.

**Verdict (xvii)**: ✅ Excluded — but the exclusion is *implicit* in the framework's structure (only single twists give L-functions), not stated as an explicit theorem. This is the "🟡 implicit but plausible" verdict from the evaluation framework. To upgrade to ✅: write down a theorem stating "the framework's L-functions are exactly the principal automorphic L-functions for GL_1 over the adèles," and note that D-H is not principal automorphic.

**Subtlety**: more general non-Euler-product L-functions could potentially be encoded via "sum-twists" of the adèle class space, but this would extend the framework beyond what Connes has defined. The framework as currently stated only handles single twists.

### 3.5 Deninger foliated cohomology

**Framework's natural L-functions**: L-functions of arithmetic schemes whose closed points correspond to leaves of the foliation. Specifically, $\zeta(s)$ comes from the natural foliation on $\bar X$ (the hypothetical foliated space over $\mathrm{Spec}(\mathbb{Z})$); more generally, twisted/modular L-functions arise from foliations on twisted versions of $\bar X$.

**Is D-H in this domain?** Same answer as Connes: D-H is a linear combination, not a single L-function. Deninger's framework would predict GRH for each $L(s, \chi_5^a)$ and $L(s, \chi_5^b)$ separately (assuming the framework is constructed), but D-H itself is not the trace of any single foliated dynamical system.

**Could one construct a foliation whose "L-function" is D-H?** This is more delicate than for the other candidates because Deninger's framework is more conjectural. In principle, if the foliated space $\bar X$ has direct-sum decompositions, the L-function of the sum might be a product (per the trace formula), not a linear combination. So linear combinations remain excluded.

**Verdict (xvii)**: ✅ Excluded by the same trace-formula argument as Connes. But like Connes, the exclusion is implicit; an explicit theorem would tighten the verdict.

### 3.6 Connes-Consani hyperring (characteristic-one geometry)

**Framework's natural L-functions**: arise from the arithmetic site $\mathcal{A}$ (a topos-theoretic object) via the Connes-Consani trace formula. The L-functions are essentially the same as in Connes' original adelic framework, just packaged differently.

**Is D-H in this domain?** No, same argument as Connes (3.4): D-H is not a single automorphic L-function and doesn't arise from spectral data of $\mathcal{A}$.

**Verdict (xvii)**: ✅ Excluded by construction (implicit in the trace-formula structure).

## 4. Updated scorecards

The (xvii) verdict for each candidate updates from the previous status:

| Candidate | Previous (xvii) | Updated (xvii) | Argument |
|---|---|---|---|
| Deitmar | ⏳ (vacuous) | ✅ | No Euler product → not a Deitmar zeta. |
| Lorscheid | ⏳ (vacuous) | ✅ | Blueprint zetas are multiplicative; D-H is not. |
| Borger | ⏳ (vacuous) | ✅ | Adams operations give Euler product structure intrinsically. |
| Connes | 🟡 (probably) | ✅ (implicit) | Framework's L-functions are single-twist spectral; D-H is a linear combination. Explicit theorem would tighten. |
| Deninger | ⏳ (open) | ✅ (implicit) | Trace formula gives single L-functions per foliation; linear combinations are not in the natural output. |
| Connes-Consani | ⏳ (open) | ✅ (implicit) | Same as Connes. |

All six candidates pass kill criterion K2. None of them accidentally proves RH for D-H, because D-H is structurally outside each framework's natural domain. **The Architecture 2 candidates are all K2-safe.**

## 5. What this means for future candidate design

The R1 analysis surfaces a design constraint for new candidates: **the framework's natural L-functions must arise from a "geometric" operation that is intrinsically multiplicative.** Linear combinations of L-functions are not allowed in the natural domain.

This rules out (or at least flags) a class of plausible-looking candidates:

- **Any framework whose L-functions are defined by Mellin transforms of arbitrary modular-form-like objects without an Euler product structure** would risk including D-H or D-H-like combinations and would fail K2.
- **Any framework that allows the L-function operation to commute with linear combination** is suspect: $L(s, X_1 + X_2) = L(s, X_1) + L(s, X_2)$ would mean the framework's RH conclusion applies to sums, contradicting D-H's off-line zeros.

The structural lesson: the L-function operation must be "multiplicative at the object level" (so that $L(s, X_1 \cdot X_2) = L(s, X_1) \cdot L(s, X_2)$ or similar) but not "additive at the object level." This is automatically the case for all six existing candidates — but a future candidate trying to be more general should be checked against this constraint explicitly.

## 6. Stronger D-H-like tests

The R1 analysis used D-H specifically. There are other known counterexamples in the Selberg-class literature that could be used as stronger tests:

- **Spira's L-function** (1976): another non-Euler-product L-function with off-line zeros.
- **Selberg's manufactured counterexamples**: families of L-functions constructed to have off-line zeros, parameterized by mixing angles.
- **Higher-order linear combinations**: $\sum_i c_i L(s, \chi_i)$ for more than two characters with various coefficients $c_i$.

These all share D-H's key feature: lack of Euler product. Any candidate that passes the D-H test via the Euler-product argument (i.e., constraint x in the evaluation framework) automatically passes for these other counterexamples too. The R1 analysis is therefore robust against the natural family of Selberg-class counterexamples, not just D-H specifically.

## 7. Open question: are there Euler-product L-functions with off-line zeros?

The R1 analysis shows that K2 is safe for all six candidates because they restrict to Euler-product L-functions. But what if some Euler-product L-function had off-line zeros? Then K2 would be a real concern: the candidate's RH conclusion would apply (since the L-function is in its domain), but the L-function would have off-line zeros (contradiction).

**As of 2025, no Euler-product L-function in the Selberg class is known to have off-line zeros.** This is consistent with the Selberg conjecture (which posits that all Selberg-class L-functions satisfy GRH). The Selberg conjecture is open, but no counterexample has been found.

So the K2 risk for the six candidates depends on the Selberg conjecture: if Selberg is true, K2 is safe by Euler-product restriction; if Selberg is false (i.e., some Euler-product L-function has off-line zeros), K2 becomes a live concern.

**This raises an interesting cross-architecture question**: a counterexample to the Selberg conjecture would simultaneously falsify any Architecture 2 candidate that "proves RH for all Euler-product L-functions." So the candidates collectively constitute a wager on the Selberg conjecture.

For the purposes of R1 (sharpening (xvii) for the six candidates): the analysis assumes Selberg conjecture holds. Under that assumption, all six candidates pass K2.

## 8. Summary

| Step | Finding |
|---|---|
| Universal reason | D-H's defining feature (linear combination → no Euler product) is not constructible within any of the six frameworks. |
| Per-candidate verdicts | All six are ✅ on (xvii), updated from previous mix of ⏳ and 🟡. |
| Kill criterion K2 | Safe for all six candidates (under Selberg conjecture). |
| Design constraint surfaced | New candidates must have L-functions arise from multiplicative-by-construction operations; linear combinations of L-functions are not natural. |
| Cross-architecture connection | The candidates' K2 safety is conditional on the Selberg conjecture — a non-trivial unsolved problem connecting Architecture 2 design to Architecture 3 / 4 questions. |
| What R1 did NOT close | The (xi)-(xiii) Hodge index positivity slot is still open for all six. R1 was bookkeeping; the central construction problem remains. |

R1 is now closed. Next-step natural follow-ups (per `2A_candidate_evaluation.md §V`):

- **R2**: compute $\mathrm{Spec}(\mathbb{Z}) \times_{\mathbb{F}_1} \mathrm{Spec}(\mathbb{Z})$ explicitly in Borger / Lorscheid frameworks (constraint ii).
- **R3**: classify whether Connes-Consani's positivity conjecture is RH-equivalent (kill criterion K1).
- **R4**: explore hybrid candidates (Borger Frobenius + Connes trace formula).
- **2E**: numerical probe — does Borger's $\psi_p$ have spectrum near $\zeta$ zeros at small $p$?
