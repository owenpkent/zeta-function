# 2A: The Weil RH proof for curves over $\mathbb{F}_q$ vs the missing structure over $\mathbb{Z}$

> Companion to [2B](e2b_elliptic_curve_fp.py) (worked example). This document is the "diff table" promised in [PROOF_ARCHITECTURES_PLAN.md](../PROOF_ARCHITECTURES_PLAN.md): a step-by-step trace of how Weil proves the Riemann hypothesis for curves $C/\mathbb{F}_q$, paired with what the analogous structure would have to look like over $\mathrm{Spec}(\mathbb{Z})$, and which pieces are missing.

The Architecture-2 conjecture is that RH for $\zeta$ is closeable by a *construction*: build the right cohomology / dynamical system on $\mathrm{Spec}(\mathbb{Z})$ (or a compactification of it) and Weil's strategy will go through verbatim. 2A maps out what that construction has to deliver.

This is mostly literature; the references at the end point to the primary sources for each step.

---

## 1. Background: what RH means in the function field case

For a smooth projective curve $C$ of genus $g$ over $\mathbb{F}_q$, the zeta function is

$$Z(C, T) = \exp\left( \sum_{k \geq 1} \frac{|C(\mathbb{F}_{q^k})|}{k} T^k \right).$$

Weil (1948) proved three structural facts about $Z(C, T)$:

1. **Rationality:** $Z(C, T) = \dfrac{P(T)}{(1 - T)(1 - qT)}$ where $P(T) \in \mathbb{Z}[T]$ has degree $2g$.
2. **Functional equation:** $Z(C, 1/qT) = q^{1 - g} T^{2 - 2g} Z(C, T)$.
3. **Riemann hypothesis:** all reciprocal roots $\alpha_i$ of $P(T)$ satisfy $|\alpha_i| = \sqrt{q}$.

The change of variables $T = q^{-s}$ turns "$|\alpha_i| = \sqrt q$" into "$\Re(s) = 1/2$ for all zeros of $Z(C, q^{-s})$." This is the function-field analogue of RH for $\zeta(s)$.

For our worked example (2B): $C : y^2 = x^3 + x + 1$ over $\mathbb{F}_5$, $g = 1$, $P(T) = 1 + 3T + 5T^2$, with roots $\alpha = -3/2 \pm i\sqrt{11}/2$ and $|\alpha|^2 = 5 = q$. ✓

---

## 2. Weil's proof in 5 steps

The full proof (1948, in the modern $\ell$-adic formulation due to Grothendieck and others) proceeds as follows.

### Step A: Lefschetz fixed-point formula on $C$

For each $k \geq 1$, $|C(\mathbb{F}_{q^k})|$ counts fixed points of the $k$-th iterate of geometric Frobenius $F_q$ acting on $C(\overline{\mathbb{F}_q})$. The Lefschetz formula in $\ell$-adic étale cohomology gives

$$|C(\mathbb{F}_{q^k})| = \sum_{i = 0}^{2} (-1)^i \operatorname{tr}(F_q^k \mid H^i(C, \mathbb{Q}_\ell)).$$

For a smooth projective curve, $H^0 = \mathbb{Q}_\ell$ (trace $= 1$ for $F_q^k$), $H^2 = \mathbb{Q}_\ell(-1)$ (trace $= q^k$), and $H^1$ has dimension $2g$.

So $|C(\mathbb{F}_{q^k})| = 1 + q^k - \operatorname{tr}(F_q^k \mid H^1)$, and the eigenvalues of $F_q$ on $H^1$ are exactly the reciprocal roots $\alpha_i$ of $P(T)$.

### Step B: Rationality and dimension of $H^1$

Because $H^1(C, \mathbb{Q}_\ell)$ is finite-dimensional (dimension $2g$), the trace expansion gives $Z(C, T)$ as a rational function of degree $\leq 2g$ in the numerator.

### Step C: Poincaré duality on $C \times C$

The cup product

$$H^1(C, \mathbb{Q}_\ell) \otimes H^1(C, \mathbb{Q}_\ell) \to H^2(C, \mathbb{Q}_\ell) \cong \mathbb{Q}_\ell(-1)$$

is a non-degenerate pairing. This compatibility with Frobenius forces:

- If $\alpha$ is an eigenvalue of $F_q$ on $H^1$, then so is $q/\alpha$ (the Frobenius-dual eigenvalue).

This gives the functional equation Step 2 and pairs up the roots of $P(T)$.

### Step D: Positivity via Hodge index / Castelnuovo-Severi

The Hodge index theorem on the surface $S = C \times C$ says the intersection form on $\operatorname{NS}(S) \otimes \mathbb{R}$ has signature $(1, \rho - 1)$ where $\rho$ is the Picard number.

Equivalently: for a divisor $D$ on $S$ with $D \cdot H > 0$ for an ample $H$, one has $D^2 \leq (D \cdot H)^2 / H^2$ (reverse Cauchy-Schwarz). This is the Castelnuovo-Severi inequality.

Apply this to the divisor $D = F_q^* - \alpha \cdot \mathrm{id}^*$ (Frobenius graph minus a scalar) for the eigenvalue $\alpha$. Castelnuovo-Severi gives $|\alpha|^2 \leq q$. Doing this for $q/\alpha$ as well gives $|q/\alpha|^2 \leq q$, i.e., $|\alpha|^2 \geq q$. Combined: $|\alpha|^2 = q$, i.e., $|\alpha| = \sqrt q$.

This is the RH step. The key ingredient is **positivity of intersection numbers** on the surface $C \times C$, which is Hodge-theoretic.

### Step E: Lift to higher dimensions (Deligne, 1974)

For varieties $V$ of higher dimension, Weil's argument generalizes after extensive cohomological work culminating in Deligne's proof of the full Weil conjectures (Deligne, "La conjecture de Weil I", 1974, and "II", 1980). The structural shape — Lefschetz + Poincaré + Hodge index — is preserved.

---

## 3. The diff table: $\mathbb{F}_q$ vs $\mathbb{Z}$

For each step above, we list (i) what Weil uses, (ii) what the analogue over $\mathrm{Spec}(\mathbb{Z})$ would have to be, (iii) what we actually have, and (iv) the gap.

### Step A: Lefschetz fixed-point formula

| Aspect | $C / \mathbb{F}_q$ | $\mathrm{Spec}(\mathbb{Z})$ analogue |
|---|---|---|
| What is the "scheme" | Smooth projective curve, dim $1$ over $\mathbb{F}_q$. Spec is a $1$-dim variety. | $\mathrm{Spec}(\mathbb{Z})$, an arithmetic scheme of (Krull) dim $1$. |
| What is "Frobenius" | $F_q: x \mapsto x^q$, an endomorphism of $C(\overline{\mathbb{F}_q})$. | **MISSING.** $\mathrm{Spec}(\mathbb{Z})$ has no geometric Frobenius. The absolute Frobenius $a \mapsto a^p$ acts on residue fields $\mathbb{F}_p = \mathbb{Z}/p$ but doesn't lift to a single endomorphism of $\mathrm{Spec}(\mathbb{Z})$. |
| Substitute for Frobenius | — | Deninger conjectures: a flow $\Phi_t$ on a hypothetical space $\bar{X} \supset \mathrm{Spec}(\mathbb{Z})$ whose "fixed points" at time $t = \log p$ are exactly the prime $p$, and whose action on a cohomology $H^*(\bar X)$ has eigenvalues at $s = $ zeros of $\zeta$. |
| What is "counting points" | $\|C(\mathbb{F}_{q^k})\|$ — a finite integer. | Counting primes via $\psi(x) = \sum_{p^k \leq x} \log p$ — connected to $-\zeta'/\zeta$. Connection between $\psi$ and Frobenius eigenvalues is the explicit formula, but the cohomological side is missing. |

**Gap:** there is no endomorphism on $\mathrm{Spec}(\mathbb{Z})$ playing the role of geometric Frobenius. Programs that propose substitutes:
- **Deninger**: a real-time flow on a (yet-unconstructed) space.
- **Connes**: action of $\mathbb{R}^*_+$ (or $\widehat{\mathbb{Z}^*}$) on the adèle class space $\mathbb{A}_\mathbb{Q} / \mathbb{Q}^*$, with a trace formula.
- **$\mathbb{F}_1$ (Soulé, Manin, et al.)**: treat $\mathbb{Z}$ as a "curve over the field with one element $\mathbb{F}_1$", then $\mathrm{Spec}(\mathbb{Z}) \times_{\mathbb{F}_1} \mathrm{Spec}(\mathbb{Z})$ is the missing surface — but $\mathbb{F}_1$ has no rigorous definition.

### Step B: Rationality / finite-dim cohomology

| Aspect | $C / \mathbb{F}_q$ | $\mathrm{Spec}(\mathbb{Z})$ analogue |
|---|---|---|
| What is finite | $H^1(C, \mathbb{Q}_\ell)$ has dim $2g$. | **PARTIAL.** Various motivic cohomologies of $\mathrm{Spec}(\mathbb{Z})$ are finite-dimensional, but none has dimension matching what's needed. |
| Why finite | $C$ is proper (compact) and smooth. | $\mathrm{Spec}(\mathbb{Z})$ is not proper (there's an "archimedean place at infinity" missing). |
| Substitute compactification | — | Arakelov geometry: add the archimedean place $\infty$ to get a "compactified" $\overline{\mathrm{Spec}(\mathbb{Z})}$. But the Arakelov compactification gives only a partial analogue — the topological structure is real, not $\ell$-adic, and the cohomology theory is incomplete for RH purposes. |
| Eigenvalue spectrum on the cohomology | Frobenius eigenvalues on $H^1$ = $\{\alpha_i\}_{i=1..2g}$. | The desired "spectrum" = $\{\frac{1}{2} + i\gamma\}$ for $\gamma$ over zeta zeros. But there are infinitely many zeros, so the cohomology must be infinite-dimensional. |

**Gap:** the analogue cohomology over $\mathrm{Spec}(\mathbb{Z})$ would need to be infinite-dimensional (matching the infinitely many zeros of $\zeta$) but still have a Frobenius-like operator with a well-defined trace at each "time step." This is the key technical difficulty: such an infinite-dimensional cohomology with controllable trace structure has not been constructed.

### Step C: Poincaré duality

| Aspect | $C \times C / \mathbb{F}_q$ | $\mathrm{Spec}(\mathbb{Z}) \times \mathrm{Spec}(\mathbb{Z})$ analogue |
|---|---|---|
| The "surface" | $C \times C$ is a smooth projective surface over $\mathbb{F}_q$. | $\mathrm{Spec}(\mathbb{Z}) \times_? \mathrm{Spec}(\mathbb{Z})$. The fibered product over $\mathrm{Spec}(\mathbb{Z})$ gives just $\mathrm{Spec}(\mathbb{Z})$ (the diagonal) — wrong dimension. |
| Substitute base | $\mathbb{F}_q$ | **MISSING.** Want $\mathrm{Spec}(\mathbb{Z}) \times_{\mathbb{F}_1} \mathrm{Spec}(\mathbb{Z})$ to be a "surface," but $\mathbb{F}_1$ is not yet a scheme. |
| Duality pairing | $H^1 \otimes H^1 \to H^2 = \mathbb{Q}_\ell(-1)$ non-degenerate. | The functional equation $\xi(s) = \xi(1-s)$ for $\zeta$ provides a *form* of duality — pairing $s$ with $1-s$ — but it's at the level of L-functions, not at the level of an underlying cohomology. |
| Operative consequence | Eigenvalues of $F$ on $H^1$ pair as $\{\alpha, q/\alpha\}$. | The functional equation pairs zeros as $\{\rho, 1 - \rho\}$. ✓ (We have this; we just don't have the underlying cohomological pairing.) |

**Gap:** we have the *consequence* (the functional equation $\xi(s) = \xi(1-s)$) but not the *underlying duality pairing* on a cohomology theory. Without the underlying pairing, we cannot use it as an ingredient in a Hodge-index-style positivity argument.

### Step D: Positivity (the RH step)

| Aspect | $C \times C / \mathbb{F}_q$ | $\mathrm{Spec}(\mathbb{Z})$ analogue |
|---|---|---|
| Positivity tool | Hodge index theorem on $C \times C$: intersection form has signature $(1, \rho - 1)$. | **MISSING.** No Hodge index theorem because there is no surface $\mathrm{Spec}(\mathbb{Z}) \times \mathrm{Spec}(\mathbb{Z})$ in the right sense. |
| Equivalent statement | Castelnuovo-Severi inequality: for divisors $D, H$ on the surface with $H$ ample, $D^2 \cdot H^2 \leq (D \cdot H)^2$. | What positivity statement on $\zeta$ would play the role? Weil positivity: $\sum_\rho \hat f(\rho) \overline{\hat f(\bar\rho)} \geq 0$ for Schwartz $f$. This is a positivity, but proving it from below requires (essentially) RH. |
| How positivity gives RH | Apply Castelnuovo-Severi to $D = F^* - \alpha \cdot \mathrm{id}^*$ to get $\|\alpha\|^2 \leq q$. Symmetrize for $q/\alpha$ to get $\|\alpha\|^2 = q$. | Weil positivity, if established unconditionally (without using RH), would give RH. But all known proofs of Weil positivity require RH-strength input. |

**Gap:** the most direct positivity we'd need (Weil positivity unconditionally) is essentially equivalent to RH. This is the fundamental circularity. The function-field case escapes the circularity because the Hodge index theorem is proved by direct intersection theory on the surface $C \times C$, which is a *finite-dimensional* geometric construction over a field.

### Step E: Higher dimensions

| Aspect | Deligne 1974 | $\mathrm{Spec}(\mathbb{Z})$ |
|---|---|---|
| Setting | Varieties $V$ of any dimension over $\mathbb{F}_q$. | Just $\mathrm{Spec}(\mathbb{Z})$ (dim 1). |
| Method | Bootstrap from curves: Lefschetz pencils, étale monodromy. | N/A — we don't have the dim-1 case yet. |

Higher dimensions are not directly relevant for proving RH for $\zeta$, but Deligne's strategy (bootstrap from curves) does suggest that any analogue over $\mathbb{Z}$ would first need a "$\mathrm{Spec}(\mathbb{Z})$-curve" cohomology to work.

---

## 4. The structural gap, in one paragraph

Weil's proof for curves over $\mathbb{F}_q$ uses (a) a finite-dimensional $\ell$-adic cohomology with a Frobenius endomorphism whose eigenvalues are the L-function's roots, (b) a Poincaré duality on the square $C \times C$, and (c) the Hodge index theorem on $C \times C$ as a positivity ingredient. Translating to $\mathrm{Spec}(\mathbb{Z})$ requires (a') an *infinite-dimensional* cohomology with a Frobenius-like operator whose eigenvalues are the (infinitely many) zeros of $\zeta$, (b') a duality on $\mathrm{Spec}(\mathbb{Z}) \times \mathrm{Spec}(\mathbb{Z})$ as a "surface" (which requires a base field below $\mathbb{Z}$, traditionally called $\mathbb{F}_1$), and (c') a positivity statement on this surface that does not already encode RH. None of (a'), (b'), (c') has been constructed; each of the major programs (Deninger, Connes, $\mathbb{F}_1$) addresses a different subset of these pieces but none has assembled all three.

---

## 5. The three programs as they sit at this gap

### Connes' adèle class space

Connes builds the "Frobenius" substitute (a') using an action of $\mathbb{R}^*_+$ on the noncommutative quotient $\mathbb{A}_\mathbb{Q} / \mathbb{Q}^*$. The trace of this action is the explicit-formula side of RH. What's missing: a *positivity statement* (c') analogous to the Hodge index theorem. Connes-Consani-Marcolli's work over the past ~20 years pushes the trace formula toward such positivity, but the positivity itself remains conjectural and (in some formulations) provably implies RH directly (i.e., the program reduces RH to a different conjecture rather than proving it).

### Deninger's dynamical cohomology

Deninger conjectures (a') as an actual flow $\Phi_t$ on a hypothetical foliated space $\bar X$, with leaves of the foliation corresponding to closed points of $\mathrm{Spec}(\mathbb{Z})$. The cohomology $H^*(\bar X)$ would have a real-valued infinitesimal generator whose spectrum gives the zeros of $\zeta$ on the critical line. What's missing: the *construction* of $\bar X$ itself. The cohomology theory is mostly conjectural; no candidate $\bar X$ has been explicitly built.

### $\mathbb{F}_1$ geometry (Soulé, Tits, Manin, Borger, Lorscheid, et al.)

The $\mathbb{F}_1$ program aims at (b') by making $\mathbb{F}_1$ — the "field with one element" — into an actual scheme-like object, so that $\mathrm{Spec}(\mathbb{Z}) \times_{\mathbb{F}_1} \mathrm{Spec}(\mathbb{Z})$ becomes a genuine surface and inherits enough structure for a Hodge-index-style positivity argument. What's missing: a working definition of $\mathbb{F}_1$ that simultaneously (i) makes the fiber product of arithmetic schemes meaningful, (ii) carries enough sheaf theory to support an analogue of Poincaré duality, and (iii) connects to L-functions of arithmetic objects. Several partial definitions exist (monoid schemes, blueprints, $\Lambda$-schemes) but none has been pushed through to a Weil-style proof.

### Why none has closed

Each program addresses one corner of the (a')-(b')-(c') triangle but is silent on or conjectural about the others. The Weil proof works in the function-field case precisely because all three pieces exist on the SAME object (the surface $C \times C$). Any analogue over $\mathbb{Z}$ has to build all three on the same underlying object — that's the open construction problem.

---

## 6. What this means for the experimental thread

**2A confirms** that Architecture 2's obstruction is *constructive*, not analytic: the proof template (Lefschetz + Poincaré + Hodge index) is well-understood; what's missing is the underlying object. The experimental thread cannot construct this object numerically; it can only verify that the function-field analogue works (2B) and clarify what the missing pieces are (this document).

**2D (Deninger micro-target)** is the natural follow-up: identify the smallest open conjecture in Deninger's program — one whose proof would be a meaningful step toward closing the gap without being equivalent to RH itself. Likely candidates: a positivity statement for a specific class of operators on conjectural foliated cohomologies, or a uniqueness/existence statement for the foliated space $\bar X$ in some restricted setting (e.g., for a specific local component).

**2C ($\mathbb{F}_1$ / Arakelov survey)** would map the current state of these programs as of $\sim 2025$: which definitions of $\mathbb{F}_1$ are most live, what concrete partial results have been proven, where the obstacles lie.

**Cross-reference to Architecture 3 (positivity).** The Weil-positivity statement on the zeta side (used in Arch 3) is the (c') ingredient — but encoded analytically rather than geometrically. The Arch 3 experiments (3C-3F, especially 3F-3I on the Weil-form duality) probe whether this analytic positivity can be obtained without the geometric machinery. The Arch 3 finding is that the unconditional analytic route hits a circularity wall (proving Weil positivity requires GRH-strength input). This is consistent with 2A's diagnosis: the missing piece is geometric, not analytic.

---

## References

**Primary sources for the Weil proof:**

- Weil, A. (1948). *Sur les courbes algébriques et les variétés qui s'en déduisent*. Hermann. (The original 1948 proof.)
- Deligne, P. (1974). *La conjecture de Weil. I.* Publications mathématiques de l'IHÉS, 43, 273–307.
- Hartshorne, R. (1977). *Algebraic Geometry*, Ch. V (intersection theory on surfaces, gives Castelnuovo-Severi).
- Milne, J. S. *Lectures on Étale Cohomology* (Sec. VI, the Weil conjectures for curves).
- Tate, J. (1965). *Algebraic cycles and poles of zeta functions.* In: Arithmetical Algebraic Geometry, 93–110.

**Deninger's program:**

- Deninger, C. (1998). *Some analogies between number theory and dynamical systems on foliated spaces.* Documenta Mathematica, Extra Vol. ICM 1998, 163–186.
- Deninger, C. (2002). *A note on arithmetic topology and dynamical systems.* In: Algebraic Number Theory and Algebraic Geometry, AMS Contemp. Math. 300.

**Connes' adèle class space:**

- Connes, A. (1999). *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function.* Selecta Math. (N.S.), 5(1), 29–106.
- Connes, A.; Consani, C. (2014). *The hyperring of adèle classes and the Riemann zeta function.* J. Number Theory, 135, 281–311.

**$\mathbb{F}_1$:**

- Tits, J. (1957). *Sur les analogues algébriques des groupes semi-simples complexes.* (The first appearance of "$\mathbb{F}_1$".)
- Soulé, C. (2004). *Les variétés sur le corps à un élément.* Mosc. Math. J., 4, 217–244.
- Manin, Y. (1995). *Lectures on zeta functions and motives.* Astérisque 228.
- Lorscheid, O. (2018). *$\mathbb{F}_1$ for everyone.* Jahresber. Dtsch. Math.-Ver. 120, 83–116.

**Bridging:**

- Conrad, B. (n.d.). *The Weil conjectures: an introduction to étale cohomology.* (Unpublished lecture notes; widely available.)
- Bombieri, E. (2000). *Problems of the Millennium: The Riemann Hypothesis.* Clay Mathematics Institute. (Section 4 sketches the function-field case as motivation.)
