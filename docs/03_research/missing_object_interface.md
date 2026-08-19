# The missing object as an interface: subproblem decomposition and build targets

**Date**: 2026-07-02. **Status**: synthesis (no new mathematics; every cell below cites a verified finding).
**Sources**: the 7-property M4 spec ([`math_iteration_engines.md`](math_iteration_engines.md) §3), the two-clause law and four faces ([`all_roads_to_the_signature.md`](all_roads_to_the_signature.md), #145-#148), the two-facet sourcing gap (#130), the three-front conjunction measurement (#128), the Arakelov base probe (#131/#132), the landscape scorecard ([`spec_z_cohomology_landscape.md`](spec_z_cohomology_landscape.md)).

## 0. What this document is

The project's specs for the missing object are scattered: the 7-property list (form face), the M1-M5 ladder (polarization face), R1 (operator face), W6 (trace-formula face), the diagonal rider (base face). This document types them as **one interface with five components**, states the required characteristics of each component, records which existing objects satisfy which components, and identifies the minimal *conjunctions* that remain open. The punchline is structural: every individual component is already satisfied by something; the entire content of RH lives in two specific conjunctions, and the four famous faces are consequences of one generator pair.

## 1. The interface: five components

The missing object is a single datum $X = (H, \mathrm{Fr}, (B, \Delta), \mathrm{TF}, \mathrm{pol})$. Anything inhabiting all five components proves RH. Anything inhabiting a proper subset is a known kind of partial object, and every such subset is already inhabited (§3).

### SP1. Carrier
A global cohomological carrier $H^\bullet(\overline{\mathrm{Spec}(\mathbb{Z})})$.
Required characteristics:
- (a) defined at **all** places including the archimedean one (rules out per-prime and per-surface objects as-is);
- (b) finite-dimensional graded pieces, or a trace-class substitute for the infinite-dimensional (Deninger-style) regime;
- (c) the functional equation realized as Poincaré duality on the carrier;
- (d) $\zeta$ realized as an alternating trace / regularized determinant (the realization half).

**Status: over-satisfied.** All 15 landscape candidates supply (d); most supply (a)-(c). D-H also passes a carrier-level test, so SP1 separates nothing. This is the component the field keeps rebuilding because it is the easy one.

### SP2. Endomorphism (the operator face; R1)
An actual endomorphism or flow $\mathrm{Fr}: H \to H$, not a trace formula asserted about one.
Required characteristics:
- (a) **Euler-sourced**: exists because of the Euler product, unstateable for D-H (AX-FORM: no Euler product, no Frobenius algebra);
- (b) its eigenvalue/characteristic data are the zeros as **discrete** spectrum (Connes shows self-adjointness with continuous spectrum makes zeros resonances and is silent on $\mathrm{Re}(\rho)$, #128 front 3);
- (c) the purity of its weights ($|\alpha| = \sqrt{q}$ analogue) is the R1 sourcing facet, on all evidence variety-gated (#130);
- (d) specializes to literal Frobenius over $\mathbb{F}_q$ (the shadow discipline).

**Status: partially satisfied, never globally.** Prismatic/WCart has a real Frobenius one prime at a time (p-complete); Connes has a global flow with continuous spectrum; Deninger postulates the flow. No candidate has a global endomorphism with the zeros as discrete spectral data whose purity is proved rather than assumed.

### SP3. Base and diagonal (the fixed-point geometry)
A self-product on which fixed-point counting can happen.
Required characteristics:
- (a) a product $\overline{\mathrm{Spec}(\mathbb{Z})} \times \overline{\mathrm{Spec}(\mathbb{Z})}$ **strictly bigger** than $\overline{\mathrm{Spec}(\mathbb{Z})}$ (over $\mathbb{Z}$ the tensor collapses: the absolute-base problem);
- (b) a diagonal class $\Delta$ and graph classes $\Gamma$ with an intersection calculus in which $\Gamma_{\mathrm{Fr}} \cdot \Delta$ equals the prime side of the explicit formula;
- (c) a one-parameter degree family $\deg \Gamma_t = e^t$ replacing $q^n$ (the archimedean flow face; Deninger's $\mathbb{R}$-action);
- (d) hosts either the Hodge-index form on divisors of the product (form roads) or the auxiliary-function section count (counting roads).

**Status (refined by the e2ai base battery, 2026-07-02, LEARNINGS #150): SP3 splits.** SP3a (non-collapse) and SP3b (a prime-aware diagonal: $\Lambda$ recoverable from the diagonal's own data with no zeta input) are **both satisfiable over $\mathbb{Z}$** by the Witt/derived base (ghost-lattice $F/V$ calculus; Bökstedt torsion $|\mathrm{THH}_{2i-1}(\mathbb{Z})| = i$, one mechanism in two costumes since $\mathrm{TR} \cong W$). What is empty is SP3c: a **two-sided fixed-point formula** on that self-product ($\mathrm{tr}\,F_k = 0$ for $k \ge 2$ on the ghost lattice; cyclotomic Frobenii and Hesselholt's TP trace formula are per-prime only). SP3c is the W6/R1 face again: the base *relocates* (in the #131 sense) rather than walls. The old kills stand where they were: $\mathbb{F}_1$-monoid products don't collapse but their Frobenii are prime-blind (the Adams kill's base face); the absolute base $\mathbb{Z}$ collapses at every finite level; Arakelov dies at this component (#131/#132); van Frankenhuijsen names it as the wall of the one published counting transfer (#147). This is the shared base rider of **both** clauses of the two-clause law.

### SP4. Trace formula (the W6 face)
A Lefschetz fixed-point formula tying SP2's action to prime counts.
Required characteristics:
- (a) rationality of $\zeta$ as an alternating trace over the carrier, with a **computed** pole budget (invariant-theoretic, not read off the zeros: K1);
- (b) bounded degrees uniform in twists and Künneth self-powers (what the Deligne amplification road consumes, #148);
- (c) never references zero locations.

**Status: a consequence, not an input, over $\mathbb{F}_q$** (Grothendieck trace formula = a Frobenius consequence). Over $\mathbb{Z}$ its measured absence is exactly the Lindelöf-RH gap (#148).

### SP5. Polarization (the M4 face)
The pairing with the Hodge-index signature, positive on the primitive part. Required characteristics are the 7-property spec verbatim ([`math_iteration_engines.md`](math_iteration_engines.md) §3), with the load-bearing ones:
- positivity **from a polarization**, not read off the zeros (K1, the only non-negotiable methodological constraint);
- indefinite $(1, n-1)$ Hodge-index signature, not all-positive (the Lee-Yang lesson, #95);
- the breadth-program polarity fingerprint: contingent, complex-root, line-axis, output-indefinite-with-sign-flip, prohibitive-on-a-fixed-locus (#119-#121);
- property 7.5: pins the pole-sourced continuous archimedean component to a point (Bost-Connes technology; Curto-Fialkow falls short there).

**Status: proven wherever a variety supplies it, never globally-arithmetically.** Faltings-Hriljac per surface; Hodge-Riemann in char 0; Alexandrov-Fenchel in convex geometry. The entire form-road wall.

## 2. The dependency structure: why "satisfy each, then conjoin" is the problem itself

The five components are **not independent constraints** on a search space. Over $\mathbb{F}_q$ the variety supplies SP3 for free, SP2 is functorial Frobenius, and then SP4 is a theorem (Grothendieck) and SP5 is a theorem (Castelnuovo/Hodge index). The generator is the pair **(SP2, SP3)**: the endomorphism and the place for its fixed points to live. SP4 and SP5 are downstream faces. This is the "one object, four names" reading of #145-#148, typed.

The conjunction costs are not guesses; each has been measured by a dedicated session:

| Conjunction | Verdict | Where measured |
|---|---|---|
| SP1 alone (trace realization) | satisfied by everything, separates nothing (D-H passes) | landscape scorecard |
| SP2 $\wedge$ SP5 without SP3 | walls: Euler trace lives at $\mathrm{Re}(s)>1$, signature at $\mathrm{Re}(s)=\tfrac12$; the continuation across the line IS the missing cohomology | #128, three fronts |
| SP1 $\wedge$ SP5 per-place without SP3 | walls at the base (no self-product, no $\Gamma_S$) | #131/#132, Arakelov |
| SP2 $\wedge$ SP3 without SP5 (counting route) | would prove RH via a one-sided bound plus Landau oscillation; walls at R1, variety-gated | #130, #145 |
| SP4 alone, quantified | its absence over $\mathbb{Z}$ has measured size: the Lindelöf-RH gap | #148 |
| SP5's shape without arithmetic | fully mapped and insufficient (fixed-indefinite-form space outside arithmetic geometry) | #119-#121 |

Corollary. The two **minimal open conjunctions** are:

- **C1 = SP2 $\wedge$ SP3** (counting side). If inhabited, RH follows with *no positivity requirement at all*: SP4 falls out as a fixed-point theorem, and $\psi(x) \le x + O(x^{1/2+\epsilon})$ forces RH by Landau. This is the 2026-07-01 rebalance (R1 co-equal target), reached here from the interface direction.
- **C2 = SP5 global** (form side). The arithmetic Hodge standard conjecture; the M1-M5 ladder's M4.

Everything else, every single component and every other pairwise conjunction, is either inhabited or measured. That is an unusual amount of negative-space information: the object is specified up to exactly two joints.

## 3. The satisfiability matrix

Compressed from the landscape scorecard and LEARNINGS. "part" = satisfies some required characteristics of the component.

| Candidate | SP1 carrier | SP2 endo | SP3 base+$\Delta$ | SP4 trace fmla | SP5 polarization | One-word wall |
|---|---|---|---|---|---|---|
| Function field (curve/$\mathbb{F}_q$) | yes | yes | yes | yes | yes | none (the shadow) |
| Connes adelic | yes | part (flow, cont. spectrum) | no | no (= RH there) | no | diagonal |
| Deninger | postulated | postulated | postulated | postulated | no | existence |
| Prismatic / WCart | part (per-$p$) | part (per-$p$ Frobenius) | no | no | no | globalization |
| Arakelov | yes | no | no | no | per-surface (F-H) | base |
| $\mathbb{F}_1$ geometries | degenerates | no | attempted, collapses | no | no | collapse |
| THH/TC over $\mathbb{S}$ | part | part (cyclotomic Fr) | SP3a/b yes, SP3c no (e2ai) | no | no | globalization |
| Bost-Connes | part (state, not carrier) | yes (semigroup) | no | no | no (pins a state) | not cohomological |
| de Branges | yes | part | no | no | wrong positivity (#43) | sign |
| Moment matrix $G_m$ (e2vv) | genus-faithful | part | no | no | dissolves over $\mathbb{Z}$ (#128 f.2) | log-concavity |
| **SP-object v0, built here (e2an)** | yes (finite, lattice-sourced) | part (spectrum emergent; completeness = RH) | diagonal yes; glue finite-scale | finite residual, measured | empirical, margin zero-at-resolution | the limit |
| D-H control | yes | **must be no** | must be no | must be no | must be no | (by design) |

Reading the columns: SP1 is dense, SP2 is half-dense, and SP3 looked like the emptiest column until the e2ai battery split it: SP3a/SP3b (non-collapse, prime-awareness) are satisfiable in the derived direction, and **the genuinely empty sub-column is SP3c, the two-sided fixed-point formula**, which is the same cell as SP4 restricted to the base. That is the interface-level restatement of the two-clause law, one cell sharper: the missing object is not the self-product but the Lefschetz closure on it.

## 4. Build targets

"Build something that satisfies all conditions" is, literally, RH: the interface is designed so that a full instance is a proof. What the decomposition licenses is the maximal-subset build with the residual pinned to one typed hole, and there are exactly two honest versions, one per open conjunction:

- **B1 (C1 probe, counting side). EXECUTED 2026-07-02** ([`../../experiments/arithmetic_geometric/e2ai_base_battery.py`](../../experiments/arithmetic_geometric/e2ai_base_battery.py), 15/15; LEARNINGS #150). Five bases against four pre-registered checks, function-field control all-green. Result: the minimal-base problem is **solved in shape** by the Witt/derived base (non-collapsed, prime-aware diagonal, $\Lambda$ integer-exact from the diagonal's own data), and the residual is SP3c: no operator on that self-product has a two-sided fixed-point formula ($\mathrm{tr}\,F_k = 0$; per-prime trace formulas only). The next B1 rung is therefore *the formula, not the diagonal*: what added structure on the ghost/THH self-product would make $\mathrm{tr}$ of a Frobenius-like correspondence equal a prime count with an eigenvalue side. That is the W6 spec restricted to a base that now exists.
- **B1 rung 2 (the W6 gluing spec). EXECUTED 2026-07-02** ([`../../experiments/arithmetic_geometric/e2aj_w6_gluing.py`](../../experiments/arithmetic_geometric/e2aj_w6_gluing.py), 7/7; LEARNINGS #151). The answer to the rung-1 question factors into three inputs, two of them now measured. **(A) Periodicity: already supplied, per prime.** In log coordinates each prime carries a circle $\mathbb{R}/(\log p)\mathbb{Z}$ (the cyclotomic structure is the orbit closing at $p$), and per-prime W6 **exists exactly**: the trace of the translation flow on that circle is two-sided by Poisson summation, geometric side $= \log p \sum_k \delta_{k \log p}$ (the $p$-branch of the prime side), spectral side $=$ the poles of the local Euler factor at $s = 2\pi i n/\log p$; the cohomological costume of this identity is Hesselholt's per-$p$ TP determinant formula. **The function-field magic is commensurability**: over $\mathbb{F}_q$ every place's circumference is a multiple of $\log q$ (one common circle), and the control curve's zero set is verified to be an arithmetic progression of step $2\pi/\log q$; over $\mathbb{Q}$ the $\{\log p\}$ are $\mathbb{Q}$-linearly independent and the zero set has no progression structure. **(B) The gluing: open, and now shaped.** The naive direct sum of the prime circles overcounts eigenvalues by 45x already at $T = 100$; density-matching against Riemann-von Mangoldt forces $\theta(P) \approx \log(T/2\pi e)$, i.e. **height $T$ can only see primes up to $\sim \log T$** (measured: $P^* = 7, 11, 13, 17$ at $T = 10^3..10^6$). So the glue must be scale-coupled and determinant-class: finitely many places per scale, more at higher scale, which is exactly the CCM semilocal prolate shape (#111/#114/#118) with the archimedean place entering as the e2ff two-clock organ *(mechanism corrected at rung 4: in the realized door the budget lives on one circle and the primes enter as form data; the two-meter law)*. **(C) Duality forcing the equality (K1): open**, the PROP-global rider, untouched. Net: the B1 ladder lands on the already-identified live door rather than opening a new one. C1 now reads: per-prime circles (have) $+$ semilocal determinant-class glue (open, shaped, $=$ CCM) $+$ duality (open).
- **B1 rung 3 (the Beurling discipline). EXECUTED 2026-07-02** ([`../../experiments/arithmetic_geometric/e2ak_beurling_discipline.py`](../../experiments/arithmetic_geometric/e2ak_beurling_discipline.py), 7/7; control module [`../../experiments/_shared/beurling.py`](../../experiments/_shared/beurling.py); LEARNINGS #152). The adversary move against rung 2: a density-matched Beurling fake ($b_p = p\,e^{\varepsilon_p}$, 12159 perturbed primes) **passes every #151 clause**: matched $\theta$, exact per-prime Poisson W6 on its circles, the same $P^* = \Theta(\log T)$ scale-coupling, and even the #150 divisor-lattice $\Lambda$ recovery (SP3b is Beurling-insensitive). So the rung-2 clause set is system-generic and cannot force zeta's conclusion. The separator is the **additive lattice**: no linear fit makes the fake's integer count $x + O(1)$ (best-fit error grows $5 \to 193$ over $10^2..10^5$, vs $< 1$ for $\mathbb{Z}$), and the fake's theta has a 37% functional-equation defect vs machine-zero for Jacobi. **Fourth clause of the W6 glue spec: LATTICE-CONSUMING**: the glue must consume the fact that the *same set* is multiplicatively free (Euler, the circles) and additively a perfect lattice (Poisson, the theta FE, the source of zeta's FE). The two-sided detector this institutes: D-H (FE without Euler) kills form-side methods; Beurling (Euler without FE) kills counting-side glues; zeta is the intersection, whose adelic package is Tate's thesis and whose geometric face is the diagonal $\mathbb{Q}^*$ in the adeles. SP3 closes on itself: the diagonal is not just the fixed-point locus, it is the gluing datum.
- **B1 rung 4 (the CCM survey against both gates). EXECUTED 2026-07-02** ([`reading_notes/ccm_zeta_cycle_density_gate.md`](reading_notes/ccm_zeta_cycle_density_gate.md); LEARNINGS #153). Verdict: **the door passes the density gate by reframe and pays the Beurling clause explicitly.** The realized construction is not a direct sum of prime circles: **one** spectral circle of circumference $\log x$ carries the whole budget, with $\log x = \log(T/2\pi)$ at the matched edge, confirming rung 2's measured budget exactly while superseding its per-prime-circles interpretation (correction applied above and in #151). The **two-meter law**: spectral meter $=$ circumference $\sim \log(T/2\pi)$; data meter $=$ Euler coefficients $\Lambda(n)$ down to $n \sim T/2\pi$; the exponential mismatch is absorbed by the lattice map $\mathcal{E}(f)(x) = x^{1/2}\sum_{n>0} f(nx)$, whose image defines the zeta cycles and eats the $\sim x$ surplus states. That is precisely where the fourth clause (lattice-consuming, rung 3) is paid: a Beurling fake's $\mathcal{E}_B$ exists but has no Poisson/FE property. Determinant-class status: exact and unconditional at finite cutoff ($\det_{reg} = -i\lambda^{-iz}\hat\xi(z)$, self-adjoint, real zeros, arXiv 2511.22755), open exactly at the uniform limit $\hat\xi_\lambda \to \Xi$, which the authors call their main remaining obstacle: #148's determinant-class clause, i.e. M4 in its trace-formula name. Handed forward: re-run the R3.5/K1 audit on the 2511 operator family (its perturbation vector is the ground state of the truncated Weil form, whose global positivity is RH-equivalent), and pose the W6-vs-#143 gate question to the $D_{\log}$ family.
- **B1 rung 5 (the assembly). EXECUTED 2026-08-19** ([`../../experiments/arithmetic_geometric/e2an_sp_object_v0.py`](../../experiments/arithmetic_geometric/e2an_sp_object_v0.py), 27/27; dossier [`e2an_sp_object_v0.md`](../../experiments/arithmetic_geometric/e2an_sp_object_v0.md); LEARNINGS #179). The five components assembled into ONE runnable object at finite scale, K1-clean (Muntz's formula extracts the multiplier from the integer lattice; an oracle counter proves no L-value or zero is consumed). Zeta fills the whole column (emergent spectrum 29/29 to $T = 100$ from integer data; descent identity 3.3e-10; trace formula two-sided to 1.0e-7 on the object's own spectrum; prime-side Weil Gram = zero-side to 2.7e-5 with window margin $-1.9\times10^{-16}$, zero at machine precision); the controls fail componentwise per the bracket (D-H: off-line pair invisible at 600x contrast, $b_6 = 1.936$ Euler leak; Beurling: truncation drift 0.505, duality defect 0.665, residue = its own density). The wrongness localizes at exactly C1 (SP4's residual: the finite shadow of Connes 1998 Theorem 5) and C2 (SP5's margin: uniform-in-scale positivity = M4). The matrix in §3 gains its first BUILT row, and any future candidate drops into the pipeline for a cell-by-cell score. Handed forward: the scaling ladder ($L = 8..14$: decay law of the SP4 residual and SP5 margin), the D-H invisibility certificate, and B2 with this object as the four-of-five inhabitant.
- **B2 (interface formalization, both sides).** A Lean structure `ArithmeticFrobeniusInterface` packaging the five components, with the four faces (endomorphism, derivation, trace formula, polarization) as *derived* lemmas from the generator pair; prove the function-field instance inhabits it sorry-free (extending `ToyModel.lean` / `FunctionFieldRH.lean` / `ArithmeticPolarization.lean`), so that each $\mathbb{Z}$-candidate's failure becomes a typed missing field. Value: the matrix in §3 becomes a machine-checked regression gate, and "the missing object" becomes a first-class term rather than a metaphor.

Posture check: B1 respects the no-fourth-form-front posture (#132) because it is a counting-side probe with no positivity claim. B2 is formalization of proven content only.

## 5. Honest close

The decomposition does not make RH additive, and that is its finding. Five components; every one individually inhabited; every conjunction short of the two minimal open ones measured and walled; four famous faces revealed as consequences of one generator pair (the endomorphism and its base). The search space is not "objects satisfying seven properties." It is: **two joints, C1 and C2, and one of them (C1) needs no positivity at all.** The first build at a joint (the e2ai base battery) already narrowed C1 by one component: the self-product and its prime-aware diagonal exist in the derived direction, so C1 reduces to the two-sided fixed-point formula on a base that is no longer missing. That the interface analysis lands on the same rebalance the counting-roads audit reached from the engine direction (#145-#148) is convergent evidence the frame is right. The coordinate system is stable; the next move is a build at a joint, not another survey of the components.

## Pointers

- Component specs in full: [`math_iteration_engines.md`](math_iteration_engines.md) §3 (SP5's seven properties), [`research_directions/08A_rosati_standard_conjecture.md`](research_directions/08A_rosati_standard_conjecture.md) (M1-M5 for C2), [`sourcing_gap_r1.md`](sourcing_gap_r1.md) (SP2's R1 facet), [`all_roads_to_the_signature.md`](all_roads_to_the_signature.md) (the two-clause law, W6, the four faces).
- The measured conjunctions: LEARNINGS #128 (three fronts), #130 (two facets), #131/#132 (Arakelov base), #145-#148 (counting roads and Lindelöf gap), #119-#121 (polarity fingerprint).
- Matrix source: [`spec_z_cohomology_landscape.md`](spec_z_cohomology_landscape.md).
