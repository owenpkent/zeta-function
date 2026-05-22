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

## 2A: The Weil-proof diff table ([2A_weil_proof_diff.md](2A_weil_proof_diff.md))

**Status:** complete. Companion to 2B.

A step-by-step trace of Weil's RH proof for curves over $\mathbb{F}_q$, paired with what the analogous structure would need to be over $\mathrm{Spec}(\mathbb{Z})$ and which pieces are missing. The proof's structural shape is **Lefschetz + Poincaré duality + Hodge index theorem**; over $\mathbb{Z}$, all three pieces are either missing or have only partial analogues:

| Step | Over $\mathbb{F}_q$ | Over $\mathrm{Spec}(\mathbb{Z})$ |
|---|---|---|
| Lefschetz fixed-point | Geometric Frobenius $F_q$ on $C$; eigenvalues on $H^1$ give zeros of $Z(C, T)$ | **No geometric Frobenius** on $\mathrm{Spec}(\mathbb{Z})$. Connes/Deninger propose substitutes (flow on adèle class space / foliated space) but none has been built. |
| Finite-dim cohomology | $H^1(C, \mathbb{Q}_\ell)$, dim $2g$, $\ell$-adic | Cohomology with the right spectrum (infinite-dim, matching infinitely many zeta zeros) is conjectural |
| Poincaré duality | Non-degenerate pairing on $C \times C$ | We have the consequence ($\xi(s) = \xi(1-s)$) but no underlying cohomology pairing |
| Hodge index theorem | Intersection-theoretic positivity on $C \times C$ | **MISSING.** No "surface" $\mathrm{Spec}(\mathbb{Z}) \times_{\mathbb{F}_1} \mathrm{Spec}(\mathbb{Z})$ in any rigorous sense, hence no Hodge index analogue. Weil positivity on the analytic side gives the right shape but is essentially equivalent to RH (the Arch 3 circularity wall). |

**Conclusion**: Architecture 2's obstruction is *constructive*, not analytic. Weil's strategy (Lefschetz + Poincaré + Hodge index) is well understood; what's missing is the underlying object on which to instantiate it. Three programs (Connes, Deninger, $\mathbb{F}_1$) each address one corner of the obstruction triangle; none has assembled all three.

**§4-5 in the document**: expanded analysis of why the obstruction is constructive (with cross-cut to Arch 3's analytic circularity wall — the analytic and geometric obstructions are two views of the same missing positivity), and a list of 17 specific characteristics that the missing mathematics would have to deliver: a base scheme below $\mathbb{Z}$ (i-iii), a cohomology theory on the surface $\mathrm{Spec}(\mathbb{Z}) \times_{\mathbb{F}_1} \mathrm{Spec}(\mathbb{Z})$ with Poincaré duality and Künneth (iv-vii), a Frobenius substitute with spectrum at zeta zeros (viii-x), a Hodge index positivity certificate provable without RH input (xi-xiii), and four test cases the construction must pass (xiv-xvii, including correctly excluding Davenport-Heilbronn).

## 2A: Candidate evaluation methodology ([2A_candidate_evaluation.md](2A_candidate_evaluation.md))

**Status:** complete (living document).

Operationalizes the 17-constraint list from `2A_weil_proof_diff.md §5` into a workable evaluation framework: precise checkable predicates for each constraint, a standardized submission template for proposing new candidate constructions, current scorecards for the six major candidates (Deitmar, Lorscheid, Borger, Connes, Deninger, Connes-Consani), and methodology notes on weighting, combinability of candidates, and four sharpened kill criteria.

**Key finding from current scoring**: no existing candidate has even a partial ✅ on (xi-xiii) — the Hodge index positivity provable without RH input. This is universally open across all six candidates and is the central construction problem.

**Next steps** (per §V of the evaluation doc):
- ~~**R1**: Sharpen the D-H exclusion check (xvii) for each candidate.~~ ✅ **Complete** ([2A_R1_DH_exclusion.md](2A_R1_DH_exclusion.md)). All six candidates pass kill criterion K2: D-H is excluded by construction (linear combinations are not geometric operations). K2 safety is conditional on the Selberg conjecture.
- ~~**R2**: Explicitly compute the fiber product $\mathrm{Spec}(\mathbb{Z}) \times_{\mathbb{F}_1} \mathrm{Spec}(\mathbb{Z})$ in Borger / Lorscheid frameworks.~~ ✅ **Complete** ([2A_R2_fiber_product.md](2A_R2_fiber_product.md)). Borger gives Spec(W(ℤ)) via the big Witt ring; Lorscheid gives the blueprint (ℤ × ℤ, doubled relations). Both produce non-trivial surface-like objects (constraint (ii) → 🟡 for both, sharpened from ⏳). Neither has developed intersection theory on the resulting surface — the deeper constraints (vi, xi) remain open.
- **R3**: Identify whether Connes-Consani's positivity conjecture is RH-equivalent (kill criterion K1) or has an independent constructive proof candidate
- **R4**: Explore hybrid candidates — the "Borger Frobenius + Connes trace formula" hybrid is the most promising on paper

## 2C, 2D

- **2C** (state of $\mathbb{F}_1$ / Arakelov programs as of 2025): literature review; deferred.
- **2D** (smallest open conjecture in Deninger's program to target): planned after 2C.
