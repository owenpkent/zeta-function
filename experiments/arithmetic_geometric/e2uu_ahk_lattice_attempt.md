# 2UU: the AHK arithmetic lattice, smallest case (9A.1-9A.3) -- the gap narrows to P3

> Experiment [`e2uu_ahk_lattice_attempt.py`](e2uu_ahk_lattice_attempt.py). A genuine instantiation attempt at milestones 9A.1-9A.3 of [`../../docs/03_research/research_directions/09A_ahk_arithmetic_lattice.md`](../../docs/03_research/research_directions/09A_ahk_arithmetic_lattice.md). Result recorded as LEARNINGS #105. This is construction-grade work on the AHK face of M4; it sharpens the target, it does not solve M4.

## The attempt

The 09A spec asks for a finite graded prime-lattice with six properties (P1 local product structure, P2 Poincare duality, P3 degree map = q+1-t, P4 t-carrying submodular Lefschetz, P5 indefinite (1,n-1), P6 [open] Hodge-Riemann positivity). This run instantiates the smallest case and checks which properties actually hold.

**Part 1 (9A.3, the function-field specialization, decisive).** On NS(C×C) for a genus-1 curve, the degree/intersection map gives $\Gamma\cdot\Delta = \#C(\mathbb{F}_q) = q+1-t$ (carries $t$, P3 holds), and the primitive form $G_{\mathrm{prim}}$ is negative-definite iff $|t|<2\sqrt q$ (the t-dependent polarization P6). Verified for $(q,t)\in\{(5,1),(5,3),(7,2),(13,4)\}$: the degree carries $t$, and primitive-neg-def $\Leftrightarrow$ Weil-bound matches in every case. So the FF model satisfies the spec, with P6 = the Weil bound (a theorem there).

**Part 2 (9A.1-9A.2, the abstract lattice).** The smallest combinatorial graded lattice on the primes $\{2,3\}$ is the Boolean lattice $B_2$. It has **P1** (the rank-generating polynomial $(1+x)^2$ factors over the atoms = $(1+x)^n$, the product-star structure) and **P2** (Whitney numbers $(1,2,1)$ are rank-symmetric, Poincare duality). **P4** (submodular hard Lefschetz) and **P5** (the convex-Hodge/AHK form is $(1,n-1)$) hold by AHK 2018 + #48/e3r -- but P5 is **unconditional**, i.e. t-blind (the same $(1,n-1)$ for every weighting, #48). The degree map (number of maximal chains $=2$) is a combinatorial integer with **no t-slot**: **P3 FAILS**.

## The result: the gap is P3

Of the six properties, the bare combinatorial lattice already supplies P1, P2, P4, and P5 (the latter two by AHK + #48). The **single missing property is P3** -- the t-carrying degree map ($=q+1-t$ on the FF shadow). And P3 is exactly what makes P6 (the primitive polarization) t-dependent and RH-meaningful: P5's $(1,n-1)$ signature is **free and t-blind** (#48), so the content is entirely in P3 $\Rightarrow$ P6.

**So the AHK BUILDER target narrows from "build a 6-property object" to "build a graded prime-lattice whose degree map yields $q+1-t$."** Everything else (the product structure, Poincare duality, the submodular Lefschetz, the $(1,n-1)$ signature) is already combinatorial. The t-carrying degree map is the AHK face of the e2tt coupling (#104): supplying it is M4.

## Spec refinement (fed back into 09A)

This run sharpens the 09A spec in two ways:
- **P5 is demoted.** "The form is indefinite $(1,n-1)$" is free and t-blind (AHK gives it unconditionally, #48); it is not a real requirement and not the discriminator. The earlier P5 wording ("the *primitive* form is indefinite $(1,n-1)$") was also imprecise: the $(1,n-1)$ is the *full* form; the *primitive* part is negative-definite and IS the polarization (the e2qq/#101 carries-t-not-definite-vs-indefinite refinement).
- **P3 is elevated.** The single gap is the t-carrying degree map; P3 $\Rightarrow$ P6. The BUILDER should put all effort into P3 (over $\mathbb{Z}$: an arithmetic intersection theory whose Lefschetz numbers are the local Frobenius traces), not into the combinatorial P1/P2/P4/P5.

## Honest scope

A genuine construction run, with a real (and useful) outcome: the AHK face of M4 reduces to one property, P3. This is not a solve -- P3 over $\mathbb{Z}$ (a degree map carrying $t$) is the t-carrying arithmetic structure, i.e. the missing cohomology -- but it is a sharp narrowing of the target and a clean division of labour (the combinatorics is free; the arithmetic decoration is everything). Same place the coupling (e2tt), the modular carrier (MC.4), and the product surface all land, now stated inside the AHK spec.

## Cross-refs

LEARNINGS #105 (this), #104 (the coupling's four faces; this is the AHK face), #48/e3r (the convex-Hodge form is unconditionally (1,n-1) = P5 free + t-blind), #40 (the t-blindness), #101/e2qq (carries-t not definite-vs-indefinite), #97 (the sharpened AHK target). Docs: [`../../docs/03_research/research_directions/09A_ahk_arithmetic_lattice.md`](../../docs/03_research/research_directions/09A_ahk_arithmetic_lattice.md), 2G ([`e2g_intersection_signature.md`](e2g_intersection_signature.md)).
