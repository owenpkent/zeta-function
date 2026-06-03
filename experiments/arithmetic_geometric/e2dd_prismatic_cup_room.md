# 2DD: Candidate-A kill probe (does the prismatic cup product have room for a Hodge-index signature?)

> Companion writeup for [`e2dd_prismatic_cup_room.py`](e2dd_prismatic_cup_room.py). Executes probe 1 of [`docs/03_research/backwards_from_2050.md`](../../docs/03_research/backwards_from_2050.md) §6: the kill probe for candidate A (prismatic Hodge-Riemann). Run: `python -m experiments.arithmetic_geometric.e2dd_prismatic_cup_room`.

## The question

The retrocausal exercise localized the one missing organ of any 2050 RH proof as the **polarization** (step 3 of the five-beat skeleton): the realization (Frobenius/flow, the trace) is supplied by many frameworks, and RH is the **signature** of a signed pairing on $H^1$. Candidate A names that pairing as the **prismatic Poincare duality cup product** (Bhatt-Lurie Sen operator $\Theta_p$ as the per-prime "$q$"), with the archimedean place carrying the continuation (C4). Its kill condition: *if the cup product on prismatic $H^1$ is forced degenerate or indefinite with no room for a $(1,k)$ primitive signature, candidate A dies.*

## What was computed (and the honesty boundary)

Genuine prismatic cohomology of $\mathrm{Spec}(\mathbb{Z})$ with a Poincare-duality cup product is **the open problem**; it is not computed here. The experiment has two cleanly separated parts.

### Part 1: REAL crystalline cup-product polarization (the K3 anchor)

For curves $C/\mathbb{F}_q$, $H^1$ is computable from the L-polynomial. The cup product $J$ is a perfect alternating form; Frobenius $\phi$ satisfies $\phi^T J \phi = q J$ (the cup product is a **polarization of scale $q$**, the crystalline shadow of the $(1,q)$ correspondence and the source of $|\alpha_i| = \sqrt q$). The primitive polarization entries $q - |\alpha_i|^2$ vanish exactly at RH.

**Result.** Across the elliptic and genus-2 family, the primitive polarization signature is $(0,0,2g)$: every entry sits at $q - |\alpha_i|^2 = 0$ to machine precision (max deviation $10^{-8}$ to $10^{-16}$). This is the **cup-product face of marginal positivity**: at RH the form sits exactly at the boundary of the definite cone. The **planted-violation control** (scale one $|\alpha|$ by $1.15$) opens a negative eigenvalue, signature $(1,1,0)$: the cup product genuinely *sees* off-line eigenvalues, so the room for a $(1,k)$ signature is real and non-vacuous. This reproduces 2T/2G in explicit cup-product language.

### Part 2: STRUCTURAL graded model (explicitly NOT real Spec(Z) cohomology)

The arithmetic obstruction (#25): no single $q$; $H^1$ is graded over places with bidegree $(1,p)$. We assemble a transparent block model (one symplectic $(1,p)$ block per prime, von Mangoldt diagonal $\log p$, #26) and answer the kill probe's three questions.

- **(a) Room.** On-line the model has signature $(0,0,20)$: every primitive entry $p - |\mathrm{root}|^2 = 0$, the same marginal-positivity boundary as Part 1. This is the boundary of a genuine definite cone (not a forced/bad degeneracy); a signed direction opens under perturbation (see (c)). A $(1,k)$ primitive signature **has room**, poised at the RH boundary exactly as the marginal-positivity thesis predicts.
- **(b) D-H discipline (K2).** Davenport-Heilbronn has no Euler factor at $p$, hence no $(1,p)$ block (2Q), hence no $\Theta_p$: the graded model **does not form** for D-H. The object is unbuildable for the counterexample, the clean C2 face of candidate A. (We literally cannot assemble a D-H Gram; that is the point.)
- **(c) Blindness (#42 local-to-global test).** Planting an off-line root in one $(1,p)$ block changes the *local* signature ($(0,0,20) \to (0,2,18)$), so the local block sees a local violation. But a local off-line block is **not** a zeta zero: the true zeros live in the analytic continuation ($\mathrm{Re}(s)=1/2 < 1$), assembled globally across all primes plus the archimedean place. A purely local cup product is blind to that continuation (#42/2CC.3). So local visibility does **not** close RH; it confirms the archimedean fiber (C4 / candidate B) is the required missing block.

## Verdict

**Candidate A is NOT killed.** The cup product is the real carrier of the signature over $\mathbb{F}_q$; the $(1,p)$-graded model has room for a definite primitive signature and is unbuildable for D-H; and the local cup product is blind to the global continuation, so candidate A *requires* the archimedean gluing. The probe **sharpens** candidate A to its irreducible content: (i) genuine prismatic Poincare duality for $\mathrm{Spec}(\mathbb{Z})$ (not computed here, the open problem) plus (ii) the archimedean continuation block (= candidate B). That conjunction is exactly milestone M4.

The "room exists, not killed" outcome is itself a coordinate: it keeps candidate A on the front and tells us the next brick is not "is there room?" (yes) but "build the archimedean continuation block and glue it to the local prismatic pieces" (the C4 / candidate-B gluing). It also re-confirms, in a third independent basis (cup-product/prismatic), that the signature sits exactly at the marginal-positivity boundary.

## Honest scope

Part 1 is rigorous and reproduces the established 2T/2G result in cup-product form. Part 2 is an **illustrative structural model**: it constructs no prismatic cohomology of $\mathrm{Spec}(\mathbb{Z})$ and proves nothing about RH. Its only job is to answer the room/discrimination/blindness questions the kill probe posed, which it does honestly for the model. No new theorem; a sharpening coordinate that keeps candidate A alive and names its next dependency.

## Pointers

- Parent: [`docs/03_research/backwards_from_2050.md`](../../docs/03_research/backwards_from_2050.md) (candidate A, §3; probe 1, §6).
- Reproduces in cup-product language: [`e2t_rosati_positivity.py`](e2t_rosati_positivity.py) (2T), [`e2g_intersection_signature.py`](e2g_intersection_signature.py) (2G).
- Findings leaned on: LEARNINGS #25 (bidegree), #26 (von Mangoldt diagonal), #42 (local-to-global blindness), #18-#20 (marginal positivity).
