# Architecture 2: Arithmetic-geometric (Deninger / $\mathbb{F}_1$)

> The Weil conjectures (Weil 1948 for curves, Deligne 1974 in general) prove RH for L-functions of varieties over finite fields. The Architecture-2 question: can these techniques lift to classical zeta over $\mathbb{Z}$?

## 2B: Weil's RH for an elliptic curve over $\mathbb{F}_p$, worked example

**Status:** complete. The prototype proof verified to compute exactly the values predicted by Weil's theorem.

**Method:** [e2b_elliptic_curve_fp.py](e2b_elliptic_curve_fp.py). Pick the elliptic curve
$$E: y^2 = x^3 + x + 1 \quad \text{over } \mathbb{F}_5$$
(nonsingular, genus 1). Brute-force count $|C(\mathbb{F}_{5^k})|$ for $k = 1, \ldots, 6$ by constructing $\mathbb{F}_{5^k}$ as $\mathbb{F}_5[t]/(g_k)$ for an irreducible $g_k$ and enumerating $(x, y)$.

**Findings:**

| $k$ | brute-force $|C(\mathbb{F}_{5^k})|$ | $5^k + 1 - 2\,\mathrm{Re}(\alpha^k)$ | agree |
|---|---|---|---|
| 1 | 9 | 9 | ✓ |
| 2 | 27 | 27 | ✓ |
| 3 | 108 | 108 | ✓ |
| 4 | 675 | 675 | ✓ |
| 5 | 3069 | 3069 | ✓ |
| 6 | 15552 | 15552 | ✓ |

Extracted from $k=1$: $a_5 = 5 + 1 - 9 = -3$. The Frobenius polynomial is $T^2 + 3T + 5$, with eigenvalues
$$\alpha = -\tfrac{3}{2} + \tfrac{\sqrt{11}}{2}\,i, \quad \bar\alpha = -\tfrac{3}{2} - \tfrac{\sqrt{11}}{2}\,i.$$

**Riemann hypothesis for $C/\mathbb{F}_5$:** $|\alpha|^2 = \alpha \bar\alpha = 5 = p$, so $|\alpha| = \sqrt 5$. ✓ Both Frobenius eigenvalues lie on the Weil circle $|z| = \sqrt p$.

**Why this proof works for curves but not for $\mathbb{Z}$.** Weil's proof of RH for $C/\mathbb{F}_p$ uses three structural facts:

1. **$\ell$-adic étale cohomology** of $C$ is finite-dimensional. Specifically $H^1(C, \mathbb{Q}_\ell)$ has dimension $2g$ ($g$ the genus). The reciprocal roots of the zeta polynomial $P(T)$ are exactly the Frobenius eigenvalues on $H^1$.

2. **Poincaré duality** on $C \times C$ pairs $H^1 \otimes H^1 \to H^2 = \mathbb{Q}_\ell(-1)$ non-degenerately, forcing the eigenvalues to come in pairs $\{\alpha_i, p/\alpha_i\}$.

3. **Hodge index theorem** on the surface $C \times C$ (or equivalently the Castelnuovo-Severi inequality) provides the positivity that forces $|\alpha_i| = \sqrt p$. This is essentially intersection theory: a divisor's self-intersection sign is controlled.

The corresponding facts that we do NOT have for $\mathrm{Spec}(\mathbb{Z})$:

- No analogue of $H^1(\mathrm{Spec}(\mathbb{Z}), \cdot)$ with a Frobenius-like endomorphism whose eigenvalues are the imaginary parts of $\zeta$'s zeros (this is what Deninger's conjectural cohomology would provide).
- No proper smooth compactification: Arakelov geometry gives a partial compactification but doesn't deliver Poincaré duality of the right shape.
- No analogue of the Hodge index theorem.

This is the gap that Arch 2 must cross. The reason it remains stuck for 70+ years is precisely that constructing any one of these three pieces in a way that also makes the others work requires fundamentally new mathematics.

**Output:**
- `e2b_elliptic_curve_fp.npz`: point counts, $a_p$, Frobenius eigenvalues
- `e2b_elliptic_curve_fp.png`: two panels (eigenvalues on Weil circle, point-count deviation vs Weil bound)

## 2A, 2C, 2D

- **2A** (Weil-proof step-by-step diff table over $\mathbb{F}_q$ vs $\mathbb{Z}$): substantial literature work; planned next.
- **2C** (state of $\mathbb{F}_1$ / Arakelov programs as of 2025): literature review; deferred.
- **2D** (smallest open conjecture in Deninger's program to target): planned after 2A.
