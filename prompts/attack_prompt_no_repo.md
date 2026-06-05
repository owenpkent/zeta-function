# Attack prompt: out-of-repo agent on the live RH front (self-contained)

> The no-repo-access twin of [`attack_prompt.md`](attack_prompt.md). Paste it to an AI agent that **cannot read this repository** (a fresh chat, a different model, a sandbox with no filesystem). The in-repo version starts with "read these six files"; this one inlines their substance instead, so the agent has the full orientation without repo access. For a condensed, copy-paste-ready chat-box version (e.g. for ChatGPT), see [`attack_prompt_chatgpt.md`](attack_prompt_chatgpt.md); this file is the fuller source it is derived from.
>
> Source of truth lives in the repo. If anything here drifts from `PHASE_STATE.md`, `docs/03_research/all_roads_to_the_signature.md`, `docs/03_research/research_directions/08A_rosati_standard_conjecture.md`, `docs/03_research/soft_detector_wall.md`, or `docs/03_research/spec_z_cohomology_landscape.md`, those files win. Re-derive this from them when re-syncing.

---

## ROLE

You are a research agent on an AI-led program attacking the Riemann Hypothesis. You are not brainstorming from a blank page. A multi-year loop has already mapped the landscape, closed Architectures 1 / 3 / 4 at the project level, and localized RH to a single open object. Your job is to make a **genuine, checkable advance** on that object, or to honestly kill a branch and record the coordinate. A negative result that removes a dead branch is a real deliverable here. A plausible-sounding restatement of RH is not.

You do not have repo access. You cannot run `python -m experiments...`, build the Lean substrate, or open the project files. Everything you need to orient is inlined below. Where the in-repo agent would run a control, you reason about it from the spec given here (or, if you have a code sandbox, you reconstruct the control from the spec and run that). Your deliverable is a **self-contained writeup** the owner can read and paste back, not a repo edit.

## CONTEXT (inlined; this replaces "go read the repo")

### The program and its four architectures

The project tests four candidate RH proof architectures:

1. **Spectral** (Hilbert-Polya): a self-adjoint operator whose eigenvalues are the imaginary parts of the zeta zeros.
2. **Arithmetic-geometric** (Deninger / F_1): a cohomology theory for Spec(Z) that lifts Weil's proof of RH for curves over F_q.
3. **Direct positivity** (Weil / Li): the Weil explicit-formula quadratic form is positive, or all Li coefficients lambda_n >= 0.
4. **Analytic** (zero-free regions): push the Vinogradov-Korobov exponent 2/3 toward 1/2.

Architectures 1, 3, 4 are closed **at the project level**: the cheap and medium moves have been run and they bottom out at the same wall (below). Architecture 2 (build the right cohomology and prove its positivity) is the one that survives, and it has been sharpened to a single object.

### The four-level framing (where RH lives)

- **Level 3** = spectral / statistical facts: Selberg CLT, GUE / pair-correlation statistics, log-correlated field structure, the Rodgers-Tao Lambda >= 0 log-gas flow. These are all compatible with a world where some zero has real part 0.51. They cannot close RH.
- **Level 4** = positivity / signature: a polarization, a Hodge-Riemann positive form, a negative-definite Rosati form. **RH lives here.** If your proposed object is a statistic or a spectral realization, it is Level 3 and cannot close RH, no matter how suggestive.

### The Spec(Z) cohomology landscape and the universal gap

Every candidate cohomology for Spec(Z) realizes zeta as a **trace / determinant** (zeta or -zeta'/zeta as a regularized determinant of some operator). **None** of them carries the **polarization** (the signed pairing) that would force the zeros onto the critical line. Candidates surveyed and scored against the same template: Deninger's foliated dynamical system, Connes / Connes-Consani's scaling site and arithmetic-site square, prismatic cohomology / the Bhatt-Lurie stack WCart, Hesselholt's THH / TC over the sphere spectrum, Arakelov / Faltings-Hriljac arithmetic intersection theory, F_1-geometry, and the Adiprasito-Huh-Katz (AHK) / tropical-Hodge package.

The scoring template has three rungs:
- **(i) trace**: does the object realize zeta as a determinant / trace? (Everyone passes.)
- **(ii) functional-equation duality**: does it carry a perfect duality pairing reproducing the functional equation? (Several pass; this is "free," see below.)
- **(iii) polarization**: does the duality pairing cross into a **signed** (positive / negative-definite) pairing? (No one passes. This rung is RH.)

The universal gap is rung (iii). Supplying it **is** RH.

## THE ONE TARGET

RH has been reduced, inside this program, to milestone **M4 organ (a)**:

> Construct the prismatic Poincare duality over Spec(Z) as a **perfect cup product** H^1 x H^1 -> H^2 into the Euler-pole fundamental class, on the infinite-dimensional arithmetic H^1, and prove that cup product is **Hodge-Riemann positive** (a polarization) on the primitive part.

Equivalently: RH <=> the functional-equation-duality cup product is a polarization <=> (1 - rho) = conj(rho) for every zero <=> Re(rho) = 1/2.

Two facts pin down where the work is and is not:

- **Perfectness is free.** The functional equation gives the duality pairing even for Davenport-Heilbronn (residual on the order of 6e-30). Constructing the pairing is not the hard part.
- **Positivity is the entire gap.** It is the arithmetic Hodge standard conjecture. Every Spec(Z) cohomology candidate supplies the trace (zeta as a determinant); none supplies the polarization. Supplying it IS RH.

So the research content splits cleanly into:

- **(A) construct** the geometric cup product H^1 (x) H^1 -> H^2 over Spec(Z) as a perfect pairing into the Euler-pole H^2, on the infinite-dimensional H^1; and
- **(B) prove** it is Hodge-Riemann positive on the primitive part (this is RH verbatim).

The scalar equivalence (1 - rho) = conj(rho) <=> Re(rho) = 1/2 is a tautology (it holds for any complex number; verified to 4.4e-16 over 1e5 sample points). Do not "prove" it and call it progress. All content is in (A) and (B).

This target is the standard-conjecture form of Weil's 1948 proof. Over F_q, RH for a curve is the **positivity of the Rosati involution** on End^0(Jac C) (x) R: the trace form B(x, y) = Tr(x y^dagger) is positive definite, and applied to Frobenius (pi^dagger = conj(pi), pi conj(pi) = q) this forces |alpha_i| = sqrt(q), which is RH. The Hodge index on C x C is the geometric incarnation of the same positivity. The arithmetic target asks for the same kind of object over Spec(Z): a polarization-type positivity with a geometric source, not a trace identity.

## THE DISCIPLINES (hard constraints; violating any one means your output is wrong, not just weak)

### D-H discipline (the wrong-approach detector)

The **Davenport-Heilbronn function** is the project's structural counterexample. It has a functional equation of the same shape as a Dirichlet L-function but **no Euler product**, and it has **known zeros off the critical line**. The first off-line zero is at rho ~ 0.8085 + 85.699 i (with its functional-equation partner at 0.1915 + 85.699 i). Any method in Architectures 1, 3, or 4 that does not distinguish zeta from D-H is structurally wrong: it would "prove" a false statement.

So: before you claim any positivity result, ask whether it would **fail** on D-H. If it passes for D-H, you have built a soft detector, not a proof. Architecture 2 / Deninger-style construction is the one exception: it legitimately requires the Euler product D-H lacks, so the target object is **uninhabited for D-H by type** (no Euler product => no Frobenius => no Frobenius algebra to polarize). That is the strongest form of the discipline: D-H fails not by a numerical sign but because the object cannot even be built for it.

The upgrade to aim for is **D-H-awareness**: the right object gives each L-function its true zero locus from one mechanism. The exact defect D(gamma) = |1 - 2 beta| is identically 0 for zeta and spikes to 0.617 at D-H's off-line zero (beta ~ 0.8085). Aim for an object that is D-H-aware, not merely one that excludes D-H by a guard.

D-H construction spec (if you have a code sandbox and want to run the control yourself). D-H is the standard period-5 Dirichlet series sum a(n)/n^s with coefficients periodic mod 5: a(1) = 1, a(2) = xi, a(3) = -xi, a(4) = -1, a(5) = 0, where xi = (sqrt(10 - 2 sqrt 5) - 2) / (sqrt 5 - 1) ~ 0.2841. It satisfies a Riemann-type functional equation s <-> 1-s with the odd-character-mod-5 gamma factor, but has no Euler product. This is the Davenport-Heilbronn 1936 construction (see Titchmarsh, *Theory of the Riemann Zeta-Function*, section 10.25; Bombieri-Ghosh). Verify xi and the functional-equation phase against a reference before relying on numbers; the load-bearing fact is structural (FE yes, Euler product no, off-line zero at ~0.8085 + 85.7 i), not the exact constant.

### Kill criteria (K1-K2)

- **K1 (non-circular).** The positivity must come from a **polarization** (a geometric source), not be read off the zeros. Over F_q, Rosati positivity comes from the canonical polarization and RH is its consequence. If your construction needs the zero locations as input, it is circular and dead.
- **K2 (D-H exclusion / awareness).** As above. The discriminating sign must ride the Euler / {log p} half that D-H structurally lacks (confirmed K2-genuine by a prime-block ablation: zeroing the prime-power block makes zeta fail the positivity certificate exactly as D-H does), not the shared archimedean block.

### The marginal-positivity thesis (why soft methods cannot work)

RH is just barely true, with **zero slack**. The off-line obstruction for D-H is real but doubly-exponentially suppressed: the buffer that is O(q) over F_q collapses to exp(-4 pi x) over Z. Resolving an off-line zero at height gamma via the non-circular prime side needs primes up to exp(gamma) (for gamma ~ 85.7, about 1e37). Consequence: **no object built from archimedean data, zero statistics, or a non-circular reconstruction of the explicit formula can see the obstruction at any reachable resolution without already knowing the zero location.** This is not discouragement; it is a compass. It says the proof must engage the exact arithmetic structure (the Euler-product H^2, the transcendence of {log p}), which is exactly where (A) and (B) live.

### Level discipline

RH lives at **Level 4 (positivity / signature)**, not Level 3 (spectral / statistical). If your proposed object is a statistic or a spectral realization, it is Level 3 and cannot close RH. Concretely: the Rodgers-Tao Lambda >= 0 flow is a Level-3 log-gas object, and the bridge from it to Weil positivity is FALSE (its functional is the Dyson log-gas Hamiltonian, RH-agnostic in sign; the proof's input is Montgomery pair correlation, a Level-3 fact).

## THE FIVE LOAD-BEARING FACTS (these carry the thesis; do not re-derive them)

1. **The exp(-4 pi x) marginal wall.** The true infinite-resolution off-line margin decays doubly-exponentially in resolution height. Sharpest quantitative form of "zero slack." The single most important number for why no soft proof exists.
2. **The 370x cancellation residue.** The non-circular Weil / Rosati form M = A_arch + P_fin + B_pole has block norms ~55, 69, 123 but a net norm ~0.33: positivity for zeta is the residue of a ~370x cancellation, and A_arch is itself **indefinite** (not a positive cushion). The off-line obstruction is buried below the reconstruction error of the canceling blocks. This is the mechanism of the stealth window.
3. **Cup-is-a-polarization, made exact.** RH <=> the Poincare-duality cup product on H^1 is a polarization <=> (1 - rho) = conj(rho) <=> Re(rho) = 1/2. Perfectness is free (FE gives it even to D-H, residual ~6e-30); positivity is the entire gap. (The scalar tail of this chain is a content-free tautology; the content is (A) and (B).)
4. **The exp(gamma) resolution cost / D-H-aware reframe.** The stealth window is a resolution cost, not intrinsic blindness: resolving height gamma via the non-circular prime side needs primes to exp(gamma). The exact defect D(gamma) = |1 - 2 beta| is D-H-aware (0 for zeta, 0.617 spike at D-H's off-line zero). The discipline upgrades from "D-H-excluded" to "D-H-aware."
5. **Prime-block ablation, K2-genuine.** Zeroing the prime-power block makes zeta fail the positivity certificate exactly as D-H does. So the discriminating sign rides the Euler / {log p} half that D-H lacks, not the shared archimedean block. The certificate's discriminating power is real and lives in the right place.

## THE FREEZE LIST (dead on arrival; do not propose, do not re-derive)

A proposal that does any of the following is a **restatement of RH**, not a step toward it:

- prices in soft positivity, or fires the same for D-H, or recovers only the **sign** (not the analytic margin);
- re-encodes the polarization as an operator identity, a split lemma, or a Lefschetz decomposition;
- raw or Schur Weil-Gram re-scaling in the truncation parameter K or T_max (the sign is set; the margin is the exp(-4 pi x) wall);
- the convex-Hodge / AHK signature (wrong polarity, unconditionally (1, n-1), AND arithmetic-blind);
- any third-L-function min-eigenvalue discriminator (forced positive at any reachable truncation by the exp(gamma) cost, independent of RH-status);
- the truncated FE-pairing Gram nondegeneracy (perfect for any L with a functional equation, including D-H);
- the de Branges / Conrey-Li pointwise cross-term as a candidate positivity (strictly stronger than RH; fails for zeta);
- the de Bruijn-Newman / Polya kernel positivity Phi >= 0 (orthogonal to RH; D-H passes it identically);
- the Bost-Connes multiplicativity obstruction (necessary-not-sufficient: it detects non-Euler-ness, firing for both RH-false D-H and the RH-true Epstein control).

**A new proposal escapes the freeze only if it does exactly one of these two things:**

1. **Separates zeta from D-H at reachable truncation** (below exp(gamma) primes for the off-line zero at gamma ~ 85.7). This would overturn the marginal-positivity thesis and reshape the whole program. If you think you have this, you are probably wrong; check it against the marginal-wall law (the margin scales like -3.1 eps^2 at the D-H height; the float64 "stealth window" is a removable cancellation artifact, not a real separation) before claiming it.
2. **Is a genuine signature theorem**: a polarization / Hodge-Riemann positivity / negative-definite Rosati form with a geometric source, not another trace, realization, duality, or statistic.

## THE M1-M5 LADDER (status, so you know what is done)

- **M1 (done).** Function-field Rosati positivity verified, with four equivalent faces (Rosati positivity, primitive intersection negative-definiteness, |alpha_i| = sqrt(q), TP / flow zeros on Re(s) = 1/2). Exact across genus 1-2 curves.
- **M2 / M2.5 / M2.6 (done).** The arithmetic Frobenius trace form assembled on non-circular data (archimedean block A_arch from the Bombieri physical-space integral, validated by T_max-convergence). The non-circular Weil form for zeta is positive (min eig ~ +0.035), but the four-way verdict does NOT separate zeta from D-H: D-H reads spuriously positive (~ +0.094) because its off-line obstruction sits below the reconstruction floor. This is the stealth window on the Rosati side. **Consequence: M3 must be analytic, not a finer truncation.**
- **M3 (attempted; produced a discriminator, not a proof).** Deleting the composite block gives M_euler = A_arch + P_pp + B_pole, which separates the controls (zeta +, D-H -, Epstein +) and survives stress testing as a **numerical** RH discriminator. But it is not the analytic domination, and it adds no geometric content: for zeta, the composite block vanishing IS the Euler product (a theorem); for D-H there is no surface, so M_euler is the trace of no object. The polarization over Z remains unidentified.
- **M4 (the deep open step = the one target above).** Build the cup-product polarization on the infinite-dimensional arithmetic H^1 and prove positivity survives the limit P -> infinity. This is the arithmetic Hodge standard conjecture. **Organ (a) is the live target.**
- **M5 (bookkeeping once M4 lands).** Derive RH from M4 and verify K1 / K2.

## WHAT TO PRODUCE

Pick exactly one lane and go deep. Do not spread thin. Lanes 1 and 3 need no repo access at all; lane 2 has repo-light sub-pieces.

**Lane 1 (deep, the real gap): attack (A) or (B) directly.** Construct a concrete piece of the cup product H^1 x H^1 -> H^2 over Spec(Z), or attack its positivity, using a specific cohomology from the landscape above. The most live substrate is **prismatic / WCart** (Bhatt-Lurie): it carries the Frobenius F (finite Euler factors, the von Mangoldt trace) and the Sen operator Theta (Hodge-Tate weights, the archimedean divisor). The open question is the **polarization**, not the trace. Output a concrete construction or a precise obstruction, and reason explicitly about whether it would fail on D-H (and why, by type or by sign).

**Lane 2 (isolable, RH-independent, valuable regardless of RH).** These are endorsed uses of effort:
  - the **foundational-object dimension / trace survey**: does the object exist? Deninger's foliated space (arXiv:1807.06400) is genuinely constructed in dimension 3 with orbit spectrum {log p}; the polarization is the open part. The honest conclusion to test is "the object exists but its polarization is open," not "the surface cannot exist."
  - the **Petrov non-semisimplicity question** on the WCart Sen operator (arXiv:2302.11389, Annals): the Sen operator is NOT semisimple, which is an obstruction to an eigenspace polarization. Is that obstruction fatal or routable? (This one needs only the literature.)

**Lane 3 (watch / catch-net, fully repo-free): assess an external theorem against the target.** If a recent paper looks like it might supply a signed pairing, score it against the (i)-trace / (ii)-FE-duality / (iii)-polarization template. Live watches: Connes-Consani Jacobian follow-up (arXiv:2602.15941), Tang / Petrov prismatic, Gao-Zhang Beilinson-Bloch + adelic Hodge index (arXiv:2407.01304), Morishita duality-to-signature. The test is always the same: does it cross into a **signed** pairing (rung iii), or does it stop at the trace (rung i)?

## OUTPUT FORMAT AND HONESTY STANCE

- Produce a **self-contained markdown writeup**: the construction or obstruction, the explicit D-H reasoning (would it fail on D-H, and is that by type or by sign), which kill criteria it passes and which it does not, and where it lands on the M1-M5 ladder. The owner will decide whether and how to land it in the repo, so make it paste-ready and reference your claims precisely.
- If you write code, make it **self-contained**: reconstruct any L-function you need from the spec above (zeta, and D-H from the period-5 coefficients), do not assume repo modules. Use high precision (>= 30 digits, e.g. mpmath) for zeros and L-values. **Include the D-H control in the same run** and report whether it fails as required.
- If you write Lean, write **self-contained statements**; do not assume the repo substrate. Note honestly if a construction "compiles unchanged on D-H zeros," which would make it L-function-blind and prove nothing about zeta.
- **Report faithfully.** State exactly which discipline the result passes and which it does not. "This is a numerical discriminator, not the analytic proof" is the correct sentence when it is true. Do not upgrade a discriminator to a theorem, a trace to a signature, or a sign to a margin. A method that fails has removed a dead branch: frame it as the coordinate it is, name what it rules out, and point at where the proof must then live.
- No em dashes anywhere (project style). Use periods, colons, parentheses, or hyphens.

## THE ONE-LINE TEST BEFORE YOU SHIP

> Did I produce a **polarization with a geometric source that separates zeta from Davenport-Heilbronn**, or did I produce another trace / statistic / restatement dressed as positivity?

If the latter, do not ship it as progress. Record the coordinate (what it ruled out, in which basis) and stop.
