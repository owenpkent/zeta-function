# 2A — R3.5: A No-Shortcut Theorem for NCG Approaches to RH

> Companion to [2A_R3_connes_positivity.md](2A_R3_connes_positivity.md). R3 found that specific Connes-Consani positivity conjectures fall into three buckets: C1 (RH-equivalent), C2 (RH-equivalent), C3 (K1-uncertain). The deeper question that R3 raised: does ANY noncommutative-geometric (NCG) framework escape K1? This document attempts to prove a "no-shortcut" theorem clarifying the answer.
>
> **Disclosure upfront**: the theorem proven here is essentially **folklore in noncommutative geometry circles** — Connes and others have stated versions of this argument across the literature. The contribution of R3.5 is to **make it explicit** in the language of the 17-constraint evaluation framework, and to identify what this means for the path forward (positivity must come from geometry, not from operator theory).
>
> **Outcome**: R3.5 proves that any "trace-formula NCG framework for ζ" that proves RH via a positivity statement P necessarily has P ⟺ RH. This is a K1 "no-shortcut" theorem. **It does NOT mean NCG approaches are useless** — they could still prove the positivity P (= RH) via techniques unavailable to classical analysis. But they can't reduce RH to a strictly weaker statement.

## 1. The claim, precisely stated

**Informal**: every "noncommutative-geometric framework that reduces RH to a positivity statement P" has P equivalent to RH.

To make this precise, we need to define what counts as a "trace-formula NCG framework."

### 1.1 Definition of a trace-formula NCG framework

A **trace-formula NCG framework for ζ** is a 4-tuple $\mathcal{F} = (H, F, \mu, T)$ where:

- $H$ is a separable Hilbert space (or appropriate topological vector space).
- $F: H \to H$ is a closed, normal, possibly unbounded operator. (The "Frobenius substitute" of the framework — its spectrum is the candidate analogue of zeta zeros.)
- $\mu$ is a (possibly densely-defined) trace functional on the algebra of bounded operators on $H$ (or appropriate subalgebra). Different frameworks use different traces: ordinary trace class, Dixmier trace, Connes-Dixmier trace, etc.
- $T$ is a class of test functions on which the trace formula is well-defined.

The framework **satisfies the trace identity** if, for every test function $\phi \in T$:

$$\mu\bigl(\phi(F)\bigr) = \text{[explicit formula side: archimedean term} + \sum_p \log p \int \phi \cdot (\text{local kernel at } p)]$$

This is what makes the framework a "trace-formula NCG framework for ζ": the trace of test functions of $F$ reproduces the prime side of Riemann's explicit formula.

### 1.2 Definition of "proves RH via positivity"

A **positivity property** in $\mathcal{F}$ is a property $P$ of $\mathcal{F}$ that can be stated as one of:

- (P-SA) "$F$ is self-adjoint" (or more weakly, "$F$ has real spectrum"), OR
- (P-Q) "A specific quadratic form $Q$ on $T$ is positive semi-definite", OR
- (P-OP) "A specific operator $D$ on $H$ has non-negative eigenvalues"

(These are not exhaustive but cover the main NCG positivity types I'm aware of.)

The framework **proves RH via P** if (P holds in $\mathcal{F}$) $\implies$ (RH holds for $\zeta$).

### 1.3 The theorem

**Theorem (R3.5, "No-Shortcut for NCG")**: Let $\mathcal{F} = (H, F, \mu, T)$ be a trace-formula NCG framework for $\zeta$ that proves RH via positivity property $P$. Then:

$$P \iff \mathrm{RH}.$$

(I.e., $P$ is logically equivalent to RH within the framework's working axioms.)

**Corollary**: No trace-formula NCG framework for $\zeta$ can reduce RH to a positivity statement strictly weaker than RH. Equivalently: every such framework's positivity statement fails kill criterion K1.

## 2. Proof

### 2.1 Setup

Fix $\mathcal{F} = (H, F, \mu, T)$ satisfying the trace identity. Assume $\mathcal{F}$ proves RH via positivity property $P$.

We want to show $P \iff \mathrm{RH}$. The direction $P \implies \mathrm{RH}$ is by hypothesis. We need to prove $\mathrm{RH} \implies P$.

### 2.2 The spectral identification

The trace identity, by Riemann's classical explicit formula, can be re-expressed as:

$$\mu(\phi(F)) = \sum_\rho \phi(\rho_*) + \text{(boundary terms)}$$

where the sum runs over non-trivial zeros $\rho$ of $\zeta$, and $\rho_*$ is the spectral image of $\rho$ in $F$'s spectrum (which we'll specify below).

The **spectral identification** in NCG frameworks is typically:

$$\mathrm{spec}(F) = \{\gamma_n : \rho_n = \tfrac{1}{2} + i\gamma_n \text{ is a non-trivial zero of } \zeta\} \cup \{-\gamma_n\} \cup \{0\}$$

i.e., the spectrum of $F$ is the set of imaginary parts of zeta's non-trivial zeros (with conjugate pairs and possibly multiplicities).

(Note: this is the spectrum AS PREDICTED by the framework. Whether $F$ actually has this spectrum requires proof.)

### 2.3 Direction 1: $P \implies \mathrm{RH}$

This is by hypothesis (the framework "proves RH via P"). No work to do here.

### 2.4 Direction 2: $\mathrm{RH} \implies P$

This is the substantive direction. The argument depends on which type of positivity $P$ is.

**Case (P-SA): "F is self-adjoint" (or "F has real spectrum").**

Suppose RH holds: all non-trivial zeros $\rho_n = \frac{1}{2} + i\gamma_n$ have $\gamma_n \in \mathbb{R}$ (which is automatic) and the real part is exactly $1/2$ (this is RH).

The spectral identification (2.2) says $\mathrm{spec}(F) = \{\gamma_n\}$ (plus conjugates). If all $\gamma_n \in \mathbb{R}$, then $\mathrm{spec}(F) \subseteq \mathbb{R}$.

A normal operator with real spectrum is self-adjoint. So RH $\implies$ F is self-adjoint $\implies$ P-SA. ✓

**Case (P-Q): "Quadratic form Q is PSD".**

The relevant quadratic form is $Q(f) = \mu(f^*(F) f(F))$ or a variant — essentially, a Hilbert-space inner product realized via the trace and $F$'s spectrum.

Suppose RH holds. Then $F$'s spectrum is real, so $f(F)$ is well-defined as a self-adjoint operator for real-valued $f$. The quadratic form $Q(f) = \mu(f(F)^2)$ is then automatically $\geq 0$ (square of a self-adjoint operator has non-negative spectrum, and the trace of such is $\geq 0$).

For complex-valued $f$, $Q(f) = \mu(f^*(F) f(F))$ is the trace of $|f(F)|^2$ which is again non-negative.

So RH $\implies$ Q ≥ 0 $\implies$ P-Q. ✓

**Case (P-OP): "Operator D has non-negative eigenvalues".**

The operator $D$ in NCG frameworks is typically a Laplacian-like or Dirac-like operator whose eigenvalues are related to $\gamma_n^2$ (or similar). If RH holds, $\gamma_n \in \mathbb{R}$, so $\gamma_n^2 \geq 0$, so $D$'s eigenvalues are non-negative.

So RH $\implies$ P-OP. ✓

In all three cases, RH implies the positivity property. Combined with the hypothesis $P \implies \mathrm{RH}$, we get $P \iff \mathrm{RH}$. $\square$

### 2.5 The structural insight

The proof's content is: **the trace identity, combined with the framework's standard spectral identification, makes RH and P logically equivalent**.

The reason this happens: the framework encodes information about ζ zeros into $F$'s spectrum. Asking "is $F$ self-adjoint?" is just asking "do all zeros lie on the critical line?" via the spectral identification. The two questions are not just analogous — they're logically the same after fixing the spectral correspondence.

To break this equivalence, one would need a framework where the spectral identification is NOT bijective between zeros and operator spectrum — but then the framework doesn't actually reproduce the explicit formula correctly, contradicting the trace identity assumption.

## 3. Where the proof could fail

The theorem is robust but not absolute. Possible escape routes:

### 3.1 Framework without a trace identity

The theorem assumes the framework satisfies the trace identity. A NCG framework that proves RH WITHOUT reducing to a trace formula might escape.

However: most NCG approaches to RH in the literature (Connes, Connes-Consani, Bost-Connes, Bost, Meyer) DO use trace identities. The trace formula is the structural feature that ties the framework to ζ. Without it, the framework isn't obviously about ζ at all.

So this escape route is theoretical. No actual NCG framework I'm aware of avoids the trace identity while still being about ζ.

### 3.2 Framework with a different spectral identification

The proof uses the standard spectral identification ($F$'s spectrum = imaginary parts of zeta zeros). A framework with a different identification might escape.

But: if the spectral identification is different, the framework's positivity statement might no longer track ζ zeros directly, in which case it's unclear how P would imply RH (the framework wouldn't "prove RH via positivity" in the sense the theorem requires).

### 3.3 Framework that proves a stronger statement than RH

If $P$ implies "RH + something extra" (e.g., GRH, or a quantitative refinement), then $P$ is strictly stronger than RH, and the theorem says $P \iff \text{RH+extra}$. This is still K1 territory — proving $P$ is at least as hard as RH.

### 3.4 Framework that proves a weaker statement

If $P$ implies a zero-free region but not full RH, then the framework doesn't "prove RH" in the theorem's sense. Such frameworks exist (Beurling-Nyman, etc., for the zero-free region in vertical strips) and they don't fall under the theorem.

### 3.5 The proof's main assumption: NCG = trace formula + spectral identification

The theorem characterizes "NCG frameworks for ζ" by these two structural features. A more exotic NCG approach (e.g., one based on cyclic cohomology without an explicit trace identity, or one that bypasses spectra entirely) might not fit the theorem's hypotheses.

I'm not aware of any such exotic framework in the published literature. But the theorem doesn't rule them out — it only applies to the trace-identity + spectral-identification class.

## 4. Cross-check against R3 candidates

R3 identified three positivity conjectures in the Connes-Consani framework: C1, C2, C3. Let's check each against the theorem.

### 4.1 Conjecture C1 (Weil-Bombieri positivity)

C1 is $Q(f) \geq 0$ where $Q(f) = \sum_\rho |\hat f(\rho)|^2$. This is case (P-Q) of the theorem.

**Theorem application**: C1 ⟺ RH. ✓ Consistent with R3's verdict (C1 fails K1).

### 4.2 Conjecture C2 (Hamiltonian self-adjointness)

C2 is "$D$ is self-adjoint with real spectrum." This is case (P-SA) of the theorem.

**Theorem application**: C2 ⟺ RH. ✓ Consistent with R3's verdict.

### 4.3 Conjecture C3 (Arithmetic-site / hyperring refinements)

C3 is more subtle. The arithmetic site refinements REPACKAGE positivity in a categorical setting; the precise positivity statement varies across papers.

**Theorem application**: depends on which formulation. Most formulations I've seen still fit case (P-Q) or (P-OP), in which case the theorem applies and C3 ⟺ RH.

A formulation that escapes the theorem would have to either (a) not use a trace identity, OR (b) use a non-standard spectral identification. I don't see evidence either of these is happening in the Connes-Consani published work — though the conjecture remains stated at a level of generality where it's hard to be definitive.

**Tentative conclusion**: C3 is also probably K1-equivalent (the theorem applies), making my R3 verdict of "🟡 uncertain" perhaps too generous. R3.5 suggests C3 should be ❌ (K1 fail) as well — but the technical details require expert verification.

If R3.5 applies to C3, then ALL Connes-Consani positivity conjectures fail K1 universally. This sharpens the R3 verdict.

## 5. Implications for Architecture 2

### 5.1 What this rules out

R3.5 rules out a class of "easy" Arch 2 solutions: ANY approach that says "build a NCG framework with a trace identity and a positivity statement, prove the positivity, done." The theorem says the positivity is RH-equivalent, so proving it IS proving RH.

This is consistent with the empirical observation: 25+ years of work on NCG approaches has not produced a proof of RH. The theorem explains why: the positivity statements in these frameworks are RH-equivalent by structure, so they don't provide a shortcut.

### 5.2 What this does NOT rule out

The theorem says the POSITIVITY is RH-equivalent. It does NOT say:
- The framework is useless.
- The positivity is unprovable.
- New techniques cannot prove RH via the framework.

A NCG framework could STILL prove RH by:
- Developing operator-theoretic techniques (e.g., trace inequalities, modular operators, K-theoretic invariants) that prove the positivity directly — even though the positivity is RH-equivalent, the proof technique might be genuinely new.
- Combining NCG with other inputs (geometric, motivic, etc.) to circumvent the analytic obstacles in classical approaches.

The theorem clarifies that any such proof is "proving P which equals RH" rather than "proving P which is strictly easier than RH." But proving RH is the goal, so this is fine — the theorem is about the LOGICAL STRUCTURE of the proof, not its DIFFICULTY.

### 5.3 The geometric route as the only escape

R3.5 strongly suggests that for an Arch 2 candidate to potentially provide a "different kind of proof" of RH, it must go BEYOND trace-formula NCG. The most plausible such route is:

**The geometric route**: build a surface Spec(ℤ) ×_{𝔽₁} Spec(ℤ), develop intersection theory on it, prove a Hodge index theorem.

The Hodge index theorem is NOT a positivity statement of the trace-formula NCG type (P-SA, P-Q, P-OP). It's a signature theorem on an intersection pairing — a structurally different kind of positivity.

Crucially, in the function-field case (Weil 1948), the Hodge index theorem for C × C is proved by INTERSECTION THEORY on the surface, not by trace formulas or operator-theoretic positivity. The proof uses the projective geometry of the surface and the Castelnuovo-Severi inequality, both of which are essentially algebraic and not "trace-formula NCG" in nature.

So the geometric route ESCAPES the R3.5 no-shortcut theorem — not because it provides a weaker positivity statement, but because it provides a DIFFERENT KIND of positivity (geometric/intersection-theoretic rather than operator-theoretic).

This is consistent with the conclusion of 2A_R2_5: the most promising hybrid (Λ-blueprints + intersection theory on the surface) is the one that introduces geometric positivity, not just better trace formulas.

## 6. Restated R3.5: the "free lunch" question

R3.5 can be restated as: **"Is there a free lunch in NCG?"**

A "free lunch" would be: prove RH by a NCG positivity statement that's strictly easier than RH.

R3.5 says: **no**, within the class of trace-formula NCG frameworks with standard spectral identifications.

The deeper meaning: NCG repackages RH but doesn't bypass it. To bypass requires escaping the trace-formula + spectral-identification structure.

The only known way to escape: GEOMETRY. Intersection theory on a constructed surface provides positivity that's structurally different from trace-formula positivity. If such intersection theory can be built on Spec(ℤ) ×_{𝔽₁} Spec(ℤ), and a Hodge index theorem proven, RH falls out without going through the K1 wall.

## 7. The 17-constraint reading

Translating R3.5 into the 17-constraint framework:

- **Constraint (xi)** "Hodge index theorem" is precisely the geometric-positivity input that R3.5 identifies as the escape route. The theorem clarifies why (xi) is so important: it's the only known way to get positivity that isn't RH-equivalent.

- **Constraint (xii)** "Provable without RH input" is what R3.5 makes precise. For positivity statements in trace-formula NCG frameworks, (xii) is provably violated (the positivity IS RH). For positivity from intersection theory, (xii) is not violated (because the kind of positivity is different).

- **Constraint (xiii)** "Castelnuovo-Severi-style applicability" is what makes the geometric positivity USEFUL for RH. The fact that Castelnuovo-Severi can give "|α|² = q" via positive intersection numbers is what closes Weil's proof in the function-field case.

So R3.5 says: **constraints (xi)-(xiii) are not just "another open problem" but specifically THE escape route**. Every other candidate constraint can be addressed within NCG-style methods; (xi)-(xiii) requires geometric methods that NCG alone doesn't provide.

This is a sharper conclusion than R3's "(xi)-(xiii) universally open." R3.5 says: NCG-only approaches CANNOT close (xi)-(xiii) without falling into K1; only a geometric approach can.

## 8. Limitations of R3.5

The theorem has its own caveats:

1. **The hypotheses are restrictive.** "Trace-formula NCG framework with standard spectral identification" is a class. Frameworks outside this class might escape — but no significant example is known.
2. **The proof is sketch-level.** A fully rigorous version requires:
   - Precise category of frameworks
   - Precise spectral identification
   - Careful handling of unbounded operators and traces
3. **The theorem is folklore.** Connes himself has stated versions; the contribution of R3.5 is to make it explicit in the 17-constraint language. If someone published a rigorous formal version of this theorem, it would be useful but not surprising.
4. **The "different kind of positivity" claim for geometry is informal.** A skeptic could argue that intersection theory on the surface, when fully formalized, eventually reduces to some trace-formula or operator-theoretic statement. The Hodge index theorem is proved by classical projective geometry over $\mathbb{F}_q$; whether the analogous proof on a hypothetical surface over $\mathrm{Spec}(\mathbb{Z}) \times_{\mathbb{F}_1} \mathrm{Spec}(\mathbb{Z})$ would similarly be "purely geometric" is unclear.

A future R3.6 could attempt to formalize R3.5 rigorously and verify the geometric escape route claim.

## 9. Summary

**R3.5 theorem (informal)**: Every trace-formula NCG framework that proves RH via positivity has a positivity statement equivalent to RH.

**Consequence**: NCG by itself cannot reduce RH to a strictly weaker problem. The "K1 wall" is universal across NCG approaches.

**Escape route**: only geometric positivity (intersection theory + Hodge index theorem on a constructed surface) is structurally different from trace-formula NCG positivity. The Hodge index slot (xi)-(xiii) is therefore not just "open" but **specifically the door through which any RH proof via Architecture 2 must go**.

**Verdict on the broader question**: yes, R3.5 supports the conjecture that NCG-only approaches universally fail K1. This sharpens the diagnosis of where Architecture 2's path forward must lie.

## 10. Connection to the project's findings

R3.5 ties together several threads in the project:

- **2A diagnosis**: the obstruction is constructive, not analytic. R3.5 says specifically that the obstruction is the missing GEOMETRIC positivity; analytic and noncommutative-geometric positivities are blocked by K1.
- **Arch 3 finding 7** (3F-3I, Weil-form duality): the analytic positivity hits a circularity wall. R3.5 explains why: the analytic positivity is RH-equivalent by the same theorem.
- **R3** (Connes-Consani analysis): all three Connes-Consani positivity conjectures fall under R3.5's hypothesis, so all are K1-equivalent (sharpening R3's verdict on C3).
- **R2.5** (Λ-blueprints proposal): the proposed hybrid still doesn't address the Hodge index slot. R3.5 says this slot is the universally critical one, and only intersection theory can address it.

**Consistent picture**: Architecture 2's path forward, if there is one, requires constructing intersection theory on a surface over Spec(ℤ) ×_{𝔽₁} Spec(ℤ) AND proving a Hodge index theorem on it. R2 identified the candidate surfaces (Spec(W(ℤ)), blueprint (ℤ × ℤ)). R2.5 proposed the natural hybrid for surface construction (Λ-blueprints). R3.5 identifies the geometric-positivity step as the necessary and uniquely-positioned next move — neither analytical nor noncommutative-geometric methods can replace it.

## References

- Connes, A. (1999). *Trace formula in noncommutative geometry...* Selecta Math. 5(1). [The reformulation that R3.5 generalizes.]
- Meyer, R. (2005). *On a representation of the idele class group related to primes and zeros of L-functions*. Duke Math. J. 127. [Technical analysis of Connes' positivity.]
- Bombieri, E. (2000). *The Riemann Hypothesis - official problem description*. Clay Mathematics Institute. [Explicit statement of Weil-Bombieri positivity = RH.]
- Weil, A. (1952). *Sur les "formules explicites" de la théorie des nombres premiers*. Comm. Sém. Math. Univ. Lund. [The original positivity equivalence.]
- Burnol, J.-F. (2002). *On Fourier and zeta(s)*. Forum Math. 14, 379-395. [Discussion of positivity in adelic Fourier setting.]
- Cartier, P. (2000). *Mathemagics (a tribute to L. Euler and R. Feynman)*. Sém. Lothar. Combin. 44. [Survey including NCG approaches to ζ.]

Future work that would tighten R3.5:
- A rigorous categorical formulation of "trace-formula NCG framework."
- Verification that all published NCG approaches fall within the framework's scope.
- A detailed analysis of whether the geometric escape route can actually be made to work for Spec(ℤ).
