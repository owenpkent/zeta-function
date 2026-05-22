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

## 4. Why the obstruction is constructive, not analytic

Mathematical obstructions come in two flavors. **Analytic obstructions** are about bounds and inequalities: certain estimates aren't tight enough, certain sums aren't bounded by what we'd like. They yield to clever computation, new exponential sum techniques, or new auxiliary inequalities. The Vinogradov-Korobov exponent $2/3$ is an analytic obstruction; so is the de Bruijn-Newman constant being $\leq 0$ rather than $< 0$.

**Constructive obstructions** are about *objects* — categories, schemes, sheaves, cohomology theories that don't yet exist. They don't yield to better bookkeeping; they require inventing the missing mathematics. Grothendieck's invention of étale cohomology to settle the Weil conjectures was the resolution of a constructive obstruction. Before étale cohomology existed, the Weil conjectures had no plausible proof outline; after it existed, the proof was nearly mechanical.

Architecture 2 sits squarely on a constructive obstruction. Weil's proof for curves over $\mathbb{F}_q$ is a machine with three input slots:

- **Slot 1 (Frobenius)**: an endomorphism of the underlying scheme whose action on cohomology has eigenvalues equal to the L-function's roots. Over $\mathbb{F}_q$, this is the geometric Frobenius $F_q: x \mapsto x^q$. Its existence is automatic from the $\mathbb{F}_q$-structure.
- **Slot 2 (compactified surface)**: a 2-dimensional proper scheme (the surface $C \times C$) on which divisors and intersection numbers live. Over $\mathbb{F}_q$ this is constructed directly as a fiber product over $\mathrm{Spec}(\mathbb{F}_q)$.
- **Slot 3 (Hodge index positivity)**: a signature theorem on the intersection pairing of the surface. Over $\mathbb{F}_q$ this is proved by intersection theory on $C \times C$, using projectivity and properness.

The machine outputs RH for $L(C, T)$. Plug in the three $\mathbb{F}_q$-side inputs, turn the crank, you get $|\alpha_i| = \sqrt q$.

Over $\mathrm{Spec}(\mathbb{Z})$, each input slot needs to be filled by an object that doesn't exist. The "Frobenius slot" needs an endomorphism of $\mathrm{Spec}(\mathbb{Z})$ (or a compactification thereof) whose action on a cohomology has eigenvalues equal to the zeros of $\zeta$. $\mathrm{Spec}(\mathbb{Z})$ has no such endomorphism — the absolute Frobenius $x \mapsto x^p$ exists on residue fields $\mathbb{F}_p$ individually, but doesn't lift to a single endomorphism of $\mathrm{Spec}(\mathbb{Z})$ that varies the prime continuously. Connes substitutes an action of $\mathbb{R}^*_+$ on the adèle class space $\mathbb{A}_\mathbb{Q} / \mathbb{Q}^*$; Deninger substitutes a real-time flow on a hypothetical foliated space. Each proposal is conceptually clean but neither has been built rigorously enough to plug into Weil's machine.

The "surface slot" needs a 2-dimensional object replacing $C \times C$. The natural candidate is $\mathrm{Spec}(\mathbb{Z}) \times_{\text{base}} \mathrm{Spec}(\mathbb{Z})$, but to make this a 2-dimensional scheme we need a base below $\mathbb{Z}$. The fiber product $\mathrm{Spec}(\mathbb{Z}) \times_{\mathrm{Spec}(\mathbb{Z})} \mathrm{Spec}(\mathbb{Z})$ collapses to $\mathrm{Spec}(\mathbb{Z})$ itself (the diagonal), giving a 1-dimensional object, not a surface. To get a surface we need a hypothetical $\mathrm{Spec}(\mathbb{F}_1)$ sitting below $\mathrm{Spec}(\mathbb{Z})$ — this is what the $\mathbb{F}_1$ program tries to build. Several partial definitions of $\mathbb{F}_1$ exist (monoid schemes per Deitmar, blueprints per Lorscheid, $\Lambda$-rings per Borger), but none has been pushed through to the point where $\mathrm{Spec}(\mathbb{Z}) \times_{\mathbb{F}_1} \mathrm{Spec}(\mathbb{Z})$ carries enough structure to support intersection theory.

The "Hodge index slot" is the deepest gap. Even with a constructed surface and a constructed Frobenius, a positivity statement on the intersection form has to be PROVED, not just postulated. Over $\mathbb{F}_q$, positivity comes from projectivity of $C \times C$ plus standard Hodge-theoretic input (or, more elementarily, from Castelnuovo-Severi). Over $\mathbb{Z}$, even granting the existence of a "surface," we'd need to prove a Hodge index theorem on that surface — and this is where the Arch 3 finding becomes load-bearing.

### The analytic and geometric obstructions are the same obstruction

Arch 3F-3I computed Weil's positivity quadratic form $W(b) = \sum_\rho \Phi_b(\rho)^2$ for $\zeta$ and three other Selberg-class L-functions. The Weil form is the analytic analogue of the Hodge-index-style intersection pairing: in the function-field case, the intersection number of a divisor with itself on $C \times C$ is non-negative under the right conditions (Castelnuovo-Severi). Over $\mathbb{Z}$, the analogous quantity is $W(b)$, a sum over the zeros of $\zeta$. Both quantities are quadratic forms; both are supposed to be $\geq 0$ as a consequence of RH (or, equivalently in the function-field case, as a consequence of the surface's geometric structure).

Bombieri's explicit formula expresses $W(b)$ for $\zeta$ via four components: a boundary term $\sim 8(b^{1/2} - b^{-1/2})^2$, a prime sum $-2 \sum_{p^k < b^2} (\log p / p^{k/2})(2 \log b - k \log p)$, a constant $-(\log 4\pi + \gamma_E) \cdot 2 \log b$, and a gamma-integral term. Each component is large — at $b = 20$, they sit at $+144, -120, -19, -5$ — and they cancel to give $W \approx 0.1$. Three orders of magnitude of cancellation.

This cancellation is the analytic version of the Hodge index theorem. In the function-field setting, the corresponding cancellation is "free": it's a consequence of the surface $C \times C$ being projective, plus the intersection-theoretic inputs (Picard group structure, ample divisors, the Hodge index signature). You don't have to prove anything about prime sums; the geometry supplies the positivity directly.

Over $\mathbb{Z}$, without a surface and without intersection theory, we have to derive the cancellation analytically. And here's the wall: any unconditional bound on the prime sum tight enough to match the boundary's cancellation requires controlling the zeros of $\zeta$ at near-RH precision. The best unconditional PNT (Vinogradov-Korobov) gives $\psi(x) - x = O(x \exp(-c (\log x)^{3/5}))$, an error of order $x$. The cancellation we observed is at the $0.1\%$ level relative to the component magnitudes. The PNT error is too loose by a factor of roughly $10^3$. Improving it to a power-saving error term $\psi(x) - x = O(x^\theta)$ for $\theta < 1$ is *equivalent* (up to bookkeeping) to a zero-free region with that exponent — i.e., progress on RH itself. Arch 3I tested whether the milder cancellation for $\chi_3$ (Euler product, no pole, $\sim 4\%$ cancellation tightness) gives an unconditional opening via Siegel-Walfisz, and found it doesn't: partial summation kills the cancellation and the bound is too loose by factor 30-120. The same circularity wall, just at a slightly different magnitude.

The structural reading: **the analytic positivity needed for the Weil-form route over $\mathbb{Z}$ is the same positivity that the Hodge index theorem supplies for free over $\mathbb{F}_q$**. Over $\mathbb{F}_q$, the geometric structure of the surface delivers it. Over $\mathbb{Z}$, with no surface, we have to prove it from prime sums alone, and any tight enough bound on prime sums is itself a near-RH statement. The analytic obstruction (Arch 3's circularity wall) and the geometric obstruction (Arch 2's missing Hodge index) are two views of the same missing positivity. The Connes / Deninger / $\mathbb{F}_1$ programs are each trying to construct the geometric side so that positivity becomes free again, rather than fighting the analytic circularity directly.

This is also why partial analytic results (positive proportion of zeros on the critical line, Levinson-Conrey for $\zeta$ and $\chi_3$ alike, Riemann's Selberg-class density estimates) don't close the gap: they all live downstream of the analytic positivity, none constructs the missing geometric object that would make the positivity automatic. The path that actually closes RH, if there is one, goes through the construction problem — the analytic route is structurally walled off.

---

## 5. Characteristics of the missing mathematics: what would it have to do?

Granting the diagnosis in §4, the natural follow-up is: if there exists a body of mathematics that fills the three slots over $\mathrm{Spec}(\mathbb{Z})$, what would it have to look like? This section lists the constraints — what the missing mathematics must *deliver*, regardless of how it's constructed. Each constraint comes from a specific structural requirement of Weil's proof or from a specific known partial result that the new mathematics would have to subsume.

### 5.1 A base scheme below $\mathbb{Z}$

The new mathematics must contain an object $S$ (call it "$\mathrm{Spec}(\mathbb{F}_1)$" or whatever the right name turns out to be) with:

- **(i) A canonical morphism $\mathrm{Spec}(\mathbb{Z}) \to S$**, so that $\mathrm{Spec}(\mathbb{Z})$ is a "scheme over $S$." This is the analogue of $C$ being a curve over $\mathbb{F}_q$.
- **(ii) A meaningful fiber product**: $\mathrm{Spec}(\mathbb{Z}) \times_S \mathrm{Spec}(\mathbb{Z})$ must be a 2-dimensional object, not collapse to the diagonal. (Recall that $\mathrm{Spec}(\mathbb{Z}) \times_{\mathrm{Spec}(\mathbb{Z})} \mathrm{Spec}(\mathbb{Z}) = \mathrm{Spec}(\mathbb{Z})$ trivially. The new base $S$ must be properly "below" $\mathbb{Z}$.)
- **(iii) Compatibility with $\mathbb{F}_q$**: when restricted to function-field arithmetic schemes (e.g., curves over $\mathbb{F}_q$), the new framework should reduce to standard scheme theory over $\mathbb{F}_q$. Equivalently: there should be a morphism $\mathrm{Spec}(\mathbb{F}_q) \to S$ for each $q$, recovering the existing theory.

The various $\mathbb{F}_1$ programs (Deitmar's monoid schemes, Lorscheid's blueprints, Borger's $\Lambda$-rings, Toën-Vaquié's brave new schemes) each provide (i) and (iii) in some form; none has yet pushed through to a satisfactory (ii) that supports the next requirements.

### 5.2 A cohomology theory on the surface $\mathrm{Spec}(\mathbb{Z}) \times_S \mathrm{Spec}(\mathbb{Z})$

Once the surface exists, we need a cohomology functor with:

- **(iv) Finite-dimensional cohomology groups in each degree** — or, more honestly given the infinite spectrum of $\zeta$, a topological / Hilbert-space structure with a well-defined trace class.
- **(v) Poincaré duality**: a non-degenerate pairing $H^i \otimes H^{2-i} \to H^2$ giving the functional equation $\xi(s) = \xi(1-s)$ as its consequence at the L-function level.
- **(vi) A cycle class map and intersection pairing on $H^2$**: divisors on the surface should have well-defined intersection numbers, with bilinear and symmetric structure.
- **(vii) The Künneth formula**: $H^*(\mathrm{Spec}(\mathbb{Z}) \times_S \mathrm{Spec}(\mathbb{Z})) \cong H^*(\mathrm{Spec}(\mathbb{Z})) \otimes H^*(\mathrm{Spec}(\mathbb{Z}))$, so that the structure of the surface decomposes into the structure of $\mathrm{Spec}(\mathbb{Z})$.

The Künneth requirement is non-trivial: it pins down the cohomology of the base $\mathrm{Spec}(\mathbb{Z})$ as having the right number of "degrees of freedom" to recover the surface's structure via tensor product.

### 5.3 A Frobenius-like endomorphism

The new mathematics must produce an endomorphism (or flow) acting on the cohomology with:

- **(viii) Spectrum matching the zeros of $\zeta$**: the eigenvalues of the Frobenius-substitute on $H^1$ (or the relevant cohomology group) should be in bijection with the imaginary parts $\{\gamma_n\}$ of zeta's non-trivial zeros.
- **(ix) Lefschetz fixed-point formula**: a trace formula of the shape
  $$|\text{fixed points of }F^k| = \sum_i (-1)^i \mathrm{tr}(F^k \mid H^i)$$
  must reproduce, on the LHS, prime counting data (some function of the primes), and on the RHS, sums over the zeros. The explicit formula for $\zeta$ should fall out as a special case.
- **(x) Compatibility with local data at each prime**: at each prime $p$, the Frobenius substitute should produce an "Euler factor" $(1 - p^{-s})^{-1}$ for $\zeta$, matching the Euler product. More generally, for L-functions of arithmetic objects, the Euler factors at each prime should be recovered from the local action of the Frobenius substitute.

Constraint (x) is what ties this back to the L-function: the Euler product structure of $\zeta$ is the "local-global" decomposition that any candidate Frobenius substitute must respect.

### 5.4 A positivity certificate (the Hodge index slot)

The deepest requirement:

- **(xi) A Hodge index theorem on the surface**: the intersection form on the Picard group (or appropriate Néron-Severi-like quotient) of $\mathrm{Spec}(\mathbb{Z}) \times_S \mathrm{Spec}(\mathbb{Z})$ must have signature $(1, \rho - 1)$ where $\rho$ is the Picard number.
- **(xii) Provable within the new mathematics**, not requiring RH (or anything equivalent to RH) as input. This is the key point: in the function-field case, the Hodge index theorem is proved by direct intersection theory, before any L-function input. The analogue over $\mathbb{Z}$ must be similarly self-contained.
- **(xiii) Castelnuovo-Severi-style applicability**: the positivity must be in a form that applies to divisors of the type "Frobenius graph minus scalar diagonal," so that the standard Weil argument ($|\alpha|^2 \leq q$ and $|q/\alpha|^2 \leq q$ together yield $|\alpha|^2 = q$) ports over.

This is where the partial programs (Connes, Deninger) currently get stuck: the trace formula side is mature, but the positivity statement either remains conjectural or, in some formulations, is provably equivalent to RH itself (which would just shift the difficulty without resolving it).

### 5.5 Test cases the new mathematics should pass

The new mathematics should also reproduce results we already have, both as a sanity check and as a way to constrain the construction. Specifically:

- **(xiv) Recovery of the function-field case**: for $C / \mathbb{F}_q$, the new framework should give exactly Weil's RH (already proved) — i.e., reduce to standard étale cohomology when the base is $\mathbb{F}_q$.
- **(xv) Compatibility with Dirichlet L-functions**: for Dirichlet characters $\chi$, the new framework should produce $L(s, \chi)$ from a twisted version of the cohomology, with Frobenius-substitute eigenvalues at zeros of $L(s, \chi)$.
- **(xvi) The Selberg class as a natural domain**: more generally, the new framework should accommodate L-functions in the Selberg class (Euler product + functional equation + Ramanujan-on-average), with the structure varying continuously with the L-function's analytic conductor.
- **(xvii) Davenport-Heilbronn falls outside the framework**: the D-H L-function (functional equation but no Euler product) lacks the Euler product local-global decomposition required by (x), so the framework should NOT predict RH for it. (And indeed, D-H has off-line zeros — see 3B, 3C, 3D.)

Constraint (xvii) is a sharp consistency check: any new framework that "proves RH" without distinguishing Euler-product L-functions from non-Euler-product L-functions is wrong, because it would also "prove RH" for D-H.

### 5.6 What's not on the list

The list above is striking for what it doesn't ask for. The new mathematics does **not** need:

- New analytic bounds. Per the diagnosis (§4), the obstruction is constructive. Better PNT error terms, better trig polynomial inequalities, sharper exponential sums — none of these would help close the gap if the underlying geometric object isn't there.
- New foundations. ZFC set theory is presumed sufficient; the construction lives within ordinary mathematics, not in a new logical framework. (One could imagine alternative foundations — homotopy type theory, condensed mathematics — being convenient packaging for the construction, but the mathematical content is independent of foundations.)
- New combinatorial structures unrelated to arithmetic. The construction is constrained to fit with primes, L-functions, and intersection theory; it's not a free invention.

What it does need is **a new geometric / cohomological object** that simultaneously satisfies (i)-(xiii), with the test cases (xiv)-(xvii) as consistency checks.

### 5.7 Companion document: candidate evaluation methodology

[2A_candidate_evaluation.md](2A_candidate_evaluation.md) operationalizes this 17-constraint list into a workable scoring framework: checkable predicates for each constraint, a standardized submission template, current scorecards for the six major candidates (Deitmar, Lorscheid, Borger, Connes, Deninger, Connes-Consani), kill criteria for ruling out bad candidates, and methodology notes on candidate combinability. **Universal current finding**: no candidate has even a partial ✅ on (xi-xiii), the Hodge index positivity. This is the central open construction problem.

### 5.8 The shape of the solution, if there is one

Putting the constraints together, the missing mathematics — whatever its eventual form — has to be a single object (call it the "arithmetic surface" or whatever) that:

1. Sits over a base $S$ "smaller than $\mathbb{Z}$" (probably some version of $\mathbb{F}_1$, monoid schemes, or $\Lambda$-rings).
2. Carries a Frobenius-substitute (a discrete endomorphism per prime, or a continuous flow as Deninger conjectures).
3. Has a finite-or-trace-class cohomology with Poincaré duality.
4. Has a Hodge index theorem provable from the geometry of the surface, not from L-function bounds.
5. Reduces to known cases (function fields, Dirichlet L-functions) on appropriate subcategories.
6. Correctly excludes non-Euler-product L-functions like Davenport-Heilbronn.

Constraints 1-3 are addressed (partially) by current programs. Constraint 4 — the geometric positivity — is the deepest open problem and the central obstacle.

The reason this hasn't been built in 70+ years is that constraints 1-6 are tightly coupled: a construction satisfying 1 must also support 4, which means the choice of base $S$ has to be made in a way that the intersection theory on $\mathrm{Spec}(\mathbb{Z}) \times_S \mathrm{Spec}(\mathbb{Z})$ has the right signature. Most of the partial $\mathbb{F}_1$ definitions on the market satisfy 1 and 3 but leave 4 untouched. Conversely, the Connes / Deninger programs go after 2 and 4 but defer 1. Closing all six simultaneously is the open construction problem.

If the construction exists, it will likely look like a "Grothendieck of the arithmetic surface" — someone who builds the right base $S$, the right cohomology, the right Frobenius substitute, and proves the Hodge index theorem within that framework, all in one coherent package. The fact that no such package has emerged in 70+ years, despite many talented attempts, suggests the right base $S$ is mathematically more exotic than the existing $\mathbb{F}_1$ candidates — perhaps closer to a homotopical or noncommutative object than a classical scheme.

---

## 6. The three programs as they sit at this gap

### Connes' adèle class space

Connes builds the "Frobenius" substitute (a') using an action of $\mathbb{R}^*_+$ on the noncommutative quotient $\mathbb{A}_\mathbb{Q} / \mathbb{Q}^*$. The trace of this action is the explicit-formula side of RH. What's missing: a *positivity statement* (c') analogous to the Hodge index theorem. Connes-Consani-Marcolli's work over the past ~20 years pushes the trace formula toward such positivity, but the positivity itself remains conjectural and (in some formulations) provably implies RH directly (i.e., the program reduces RH to a different conjecture rather than proving it).

### Deninger's dynamical cohomology

Deninger conjectures (a') as an actual flow $\Phi_t$ on a hypothetical foliated space $\bar X$, with leaves of the foliation corresponding to closed points of $\mathrm{Spec}(\mathbb{Z})$. The cohomology $H^*(\bar X)$ would have a real-valued infinitesimal generator whose spectrum gives the zeros of $\zeta$ on the critical line. What's missing: the *construction* of $\bar X$ itself. The cohomology theory is mostly conjectural; no candidate $\bar X$ has been explicitly built.

### $\mathbb{F}_1$ geometry (Soulé, Tits, Manin, Borger, Lorscheid, et al.)

The $\mathbb{F}_1$ program aims at (b') by making $\mathbb{F}_1$ — the "field with one element" — into an actual scheme-like object, so that $\mathrm{Spec}(\mathbb{Z}) \times_{\mathbb{F}_1} \mathrm{Spec}(\mathbb{Z})$ becomes a genuine surface and inherits enough structure for a Hodge-index-style positivity argument. What's missing: a working definition of $\mathbb{F}_1$ that simultaneously (i) makes the fiber product of arithmetic schemes meaningful, (ii) carries enough sheaf theory to support an analogue of Poincaré duality, and (iii) connects to L-functions of arithmetic objects. Several partial definitions exist (monoid schemes, blueprints, $\Lambda$-schemes) but none has been pushed through to a Weil-style proof.

### Why none has closed

Each program addresses one corner of the (a')-(b')-(c') triangle but is silent on or conjectural about the others. The Weil proof works in the function-field case precisely because all three pieces exist on the SAME object (the surface $C \times C$). Any analogue over $\mathbb{Z}$ has to build all three on the same underlying object — that's the open construction problem.

---

## 7. What this means for the experimental thread

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
