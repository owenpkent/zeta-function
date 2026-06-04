# The soft-detector wall: a frozen consolidation

> Written 2026-06-04 as the honesty-consolidation move from the "where do we go from here" roadmap (a map / strategize / adversarial-stress-test / synthesize workflow, 32 agents). This doc does not delete anything from [`experiments/LEARNINGS.md`](../../experiments/LEARNINGS.md); it indexes one recurring class of result so the single genuinely-open object stays unmissable. Companion to [`all_roads_to_the_signature.md`](all_roads_to_the_signature.md), [`state_of_candidate_ABF.md`](state_of_candidate_ABF.md), and [`research_directions/08A_rosati_standard_conjecture.md`](research_directions/08A_rosati_standard_conjecture.md).

## FROZEN

**The soft-detector thread is confirmed closed along 6+ independent bases. Do not add new soft or realization detectors.** A new proposal is dead on arrival unless it does one of exactly two things:

1. **Separates $\zeta$ from Davenport-Heilbronn at reachable truncation** (below $e^{\gamma}$ primes for the off-line zero at $\gamma\approx 85.7$), which would overturn the marginal-positivity thesis and is itself the result that reshapes everything; or
2. **Is a genuine signature theorem** (a polarization / Hodge-Riemann positivity / negative-definite Rosati form), not another trace, realization, duality, or statistic.

Anything that prices in soft positivity, fires the same for D-H, recovers only the sign (not the analytic margin), or re-encodes the polarization as an operator identity / split lemma / Lefschetz decomposition is a **restatement of RH**, not a step toward it. Treat it as such and do not spend loop cycles on it.

## What a "soft detector" is, and why they all hit one wall

A soft detector is any quantity built from the archimedean data, the zero statistics, or a non-circular reconstruction of the explicit formula that is *hoped* to be positive exactly when RH holds. Every one the project has built falls into the same trap: it is either

- **orthogonal to RH** (positive for both $\zeta$ and the RH-false D-H), or
- **necessary-not-sufficient** (it detects the absence of the Euler product, which D-H and the RH-true Epstein control both lack, so it fires on non-Euler-ness rather than on RH-failure), or
- **wrong-polarity** (unconditionally definite, so it can never flip to flag an off-line zero), or
- **stealth-blinded** (the off-line obstruction sits below the reconstruction floor at any reachable resolution).

The structural reason is the **marginal-positivity thesis**: RH is just barely true, with zero slack. The off-line obstruction for D-H is real but doubly-exponentially suppressed in any reachable basis, so no soft object can see it without already knowing the zero location. This is a compass, not a wall: it says the proof must engage the exact arithmetic structure (the Euler-product $H^2$, the transcendence of $\{\log p\}$), which is precisely where the spine ([08A](research_directions/08A_rosati_standard_conjecture.md)) puts the work.

## The five load-bearing facts (keep these; they carry the thesis)

1. **The $e^{-4\pi x}$ marginal wall (#52, `e3v`).** The true infinite-resolution off-line margin decays doubly-exponentially in the resolution height. This is the sharpest quantitative form of "zero slack": the buffer that is $O(q)$ over $\mathbb{F}_q$ collapses to $e^{-4\pi x}$ over $\mathbb{Z}$. The single most important number for why no soft proof exists.

2. **The $370\times$ cancellation residue (#56, `e3y`).** The non-circular Weil/Rosati form $M = A_{\mathrm{arch}} + P_{\mathrm{fin}} + B_{\mathrm{pole}}$ has block norms $55, 69, 123$ but a net norm $0.33$: positivity for $\zeta$ is the residue of a $\sim 370\times$ cancellation, and $A_{\mathrm{arch}}$ is itself **indefinite** (not a positive cushion, correcting the old `e3m` docstring). The off-line obstruction is buried below the reconstruction error of the canceling blocks, which is the mechanism of the stealth window.

3. **Cup-is-a-polarization, made exact (#61, `2HH`).** RH $\iff$ the Poincare-duality cup product on $H^1$ is a polarization $\iff$ the FE-partner $(1-\rho)$ equals the conjugate $\bar\rho$ for every zero $\iff \mathrm{Re}(\rho)=1/2$. Perfectness of the pairing is free (the functional equation gives it even to D-H, residual $6\times10^{-30}$); **positivity is the entire gap**. See the demotion note below for what is and is not research-content here.

4. **The $e^{\gamma}$ resolution cost / D-H-aware reframe (#63, `2JJ`).** The stealth window (#34) is a *resolution cost*, not intrinsic blindness: resolving height $\gamma$ via the non-circular prime side needs primes to $e^{\gamma}$ (for $\gamma\approx 85.7$, that is $\sim 10^{37}$). The exact defect $D(\gamma)=|1-2\beta|$ is **D-H-aware** (identically $0$ for $\zeta$, a $0.617$ spike at D-H's off-line zero). So the discipline upgrades from "D-H-excluded" to "D-H-aware": the right object gives each $L$ its true zero locus from one mechanism.

5. **Prime-block ablation, K2-genuine (#46, `3P`).** Zeroing the prime-power block makes $\zeta$ fail the positivity certificate exactly as D-H does (no sign separation). So the discriminating sign rides the Euler / $\{\log p\}$ half that D-H structurally lacks, not the shared archimedean block. This is the positive counterpart to the soft-detector negatives: it confirms the certificate's discriminating power is real and lives in the right place.

## Demotion note: #61's scalar core is write-down-not-research

The chain $(1-\rho)=\bar\rho \iff \mathrm{Re}(\rho)=1/2$ is the scalar identity $|1-2\,\mathrm{Re}(\rho)|=0$. It is **$\zeta$-content-free**: a tautology that holds for any complex number, verified to $4.4\times10^{-16}$ over $10^5$ sample points, carrying no information about zeta specifically. All the research content of organ (a) is in the two steps the identity does *not* touch:

- **(A) construct** the geometric cup product $H^1\otimes H^1\to H^2$ over $\mathrm{Spec}(\mathbb{Z})$ as a perfect pairing into the Euler-pole fundamental class, on the infinite-dimensional arithmetic $H^1$; and
- **(B) prove** that cup product is Hodge-Riemann positive on the primitive part, which is RH verbatim (the arithmetic Hodge standard conjecture).

Stating the equivalence is bookkeeping; (A) and (B) are the mathematics. The Lean targets `Q3a`/`Q3b` in [`PrismaticCohomology.lean`](../../lean/ZetaRH/PrismaticCohomology.lean) are the machine-checked record of *where the content is not*, not a step toward RH (a naive compiled version is L-function-blind: it compiles unchanged on D-H zeros).

## Index of the soft / necessary-not-sufficient detectors

| # | Module | What it tested | Verdict |
|---|---|---|---|
| 18/19 | 3D.3 / `e3j` | Schur-complement two-clock detector | stealth window; answer-side Schur sharper than input-side, but certificate is downstream of zero location |
| 27 | `e3n`, `e_jensen_turan` | Li log-concavity; Xi-moment Jensen/Turan | two new bases, same stealth wall; Li log-concavity is a non-Euler detector |
| 34 | `e2w` (M2.6) | non-circular Rosati form, four-way | D-H reads spuriously positive ($+0.094$); stealth window on the Rosati side |
| 38 | `e_dbn_kernel` | de Bruijn-Newman / Polya kernel positivity $\Phi\ge 0$ | orthogonal to RH; D-H passes identically; suppression $\exp(-(\pi/4)d\gamma)$ |
| 39 | (survey) | Rodgers-Tao $\Lambda\ge 0$ as a fragment of Weil positivity | bridge FALSE; $\Lambda\ge 0$ is a Level-3 log-gas object, RH-agnostic in sign |
| 43 | `2DB.1` | de Branges / Conrey-Li per-zero cross-term $Q(\rho)$ | third soft detector; the global pairing sees zeros but its positivity is strictly-stronger-than-RH and fails for $\zeta$ |
| 45 | `3O` | PSLQ numerical-stumble accident slot | K2-blind by computability; PSLQ-accessible quantities are the shared archimedean half |
| 47 | `3Q` | sharp-margin recovery at the D-H height | clean $-3.1\varepsilon^2$ law; float64 stealth is a removable cancellation artifact, but moot for certification |
| 48 | `3R` | convex-Hodge (Kahler/HR/AHK) mixed-area signature | **wrong polarity**: unconditionally $(1,n-1)$ for every weighting, can never flip |
| 49 | `AccidentAudit.lean` | Lean de-smuggling / non-circularity audit | kernel-checked non-circularity certificate (a positive structural fact, not a detector) |
| 53 | `e3w` | loglog-coefficient seam | analytic twin of the multiplicativity obstruction |
| 55 | `e3z` | Bost-Connes multiplicativity obstruction $d(L)$ | necessary-not-sufficient: $d>0$ for both RH-false D-H and RH-true Epstein, so it detects non-Euler-ness |
| 65 | `2CC.4` | soft-max de-idempotentization of the C-C square | does NOT restore the Frobenius trace $t$; closes the soft-max route to the signed pairing |

The five load-bearing facts (#46, #52, #56, #61, #63) are listed above and are not duplicated in this table.

## Do-not-re-run guard

Confirmed dead; do not spend cycles re-deriving:

- raw or Schur Weil-Gram re-scaling in $K$ or $T_{\max}$ (the sign is set; the margin is the $e^{-4\pi x}$ wall);
- the convex-Hodge / AHK signature (wrong polarity AND arithmetic-blind, #40 + #48);
- any third-$L$-function $\min$-eig discriminator (the sign is forced positive at any reachable truncation by the $e^{\gamma}$ resolution cost, independent of RH-status);
- the truncated FE-pairing Gram nondegeneracy (perfect for any $L$ with a functional equation, including D-H);
- the de Branges pointwise cross-term as a candidate positivity (strictly stronger than RH).

## Where the live work is

Not here. The open object is milestone M4 organ (a): construct the prismatic Poincare duality over $\mathrm{Spec}(\mathbb{Z})$ as a perfect cup product into the Euler-pole $H^2$, and prove it is Hodge-Riemann positive on the infinite-dimensional $H^1$. The isolable, RH-independent sub-pieces worth the loop are the foundational-object dimension/trace survey, the Petrov non-semisimplicity question on the WCart substrate, and the digamma Mathlib contribution. See [`research_directions/08A_rosati_standard_conjecture.md`](research_directions/08A_rosati_standard_conjecture.md) and [`spec_z_cohomology_landscape.md`](spec_z_cohomology_landscape.md).
