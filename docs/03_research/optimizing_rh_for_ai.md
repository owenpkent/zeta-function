# Optimizing RH for an AI to attack

> Posted 2026-06-14. The strategic answer to "how do we optimize this problem for AI?", with the first three levers executed in-session: a built value-function battery (A), a scoped Lean keystone (B), and a run frame-audit (C). Companion to [`math_iteration_engines.md`](math_iteration_engines.md) (the engine arc this continues) and the spine ([`all_roads_to_the_signature.md`](all_roads_to_the_signature.md), [`research_directions/09A_ahk_arithmetic_lattice.md`](research_directions/09A_ahk_arithmetic_lattice.md)).

## The binding constraint: there is no gradient at the goal

Every other difficulty is downstream of one fact the project has now confirmed five times (#90-94, #95, #96, #97, and the frame-audit below): **marginal positivity means there is no cheap value signal at M4.** You cannot hill-climb toward "proved the arithmetic Hodge standard conjecture," because nothing returns a partial score until you are done. That is the FLT-shape risk, and it is exactly why an AI's usual strengths (breadth, search, fast iteration) keep bouncing off and merely re-confirming convergence.

So "optimize this problem for AI" is not "search harder." Breadth-over-frameworks is now a convergence detector, not a discovery engine. The real optimization is two moves: **manufacture gradients where positivity removed them, and shrink the gradient-free kernel until what remains is small enough to brute-force or formalize.** Everything below does one of those two.

## The levers, in order of leverage

1. **Turn the function-field shadow into a proven-case battery.** (Built, lever A below.) Convert "no gradient" into "k of N proven cases reproduced."
2. **Make Lean the hard value function.** (Scoped, lever B below.) The one non-circular oracle is "does it typecheck."
3. **Maximize the machine-checkable surface of 09A, shrink P6.** The 09A spec already isolates the kernel to one open property; execute the finite milestones (9A.1-9A.3) that are brute-forceable.
4. **The one real discovery bet: the regime-two frame-audit.** (Run, lever C below.)
5. **Upgrade the engines from hand-tagged to learned.** Learned premise selection, an AlphaProof-style generate-verify-RL loop trained against the Lean floor (B), conjecture-mining near M4. This is where more compute buys something, because the signal is real and the loop is tight.

## Lever A (built): the proven-case shadow battery

[`experiments/lemma_db/shadow_battery.py`](../../experiments/lemma_db/shadow_battery.py) generalizes the single function-field shadow ([`fq_shadow.py`](../../experiments/lemma_db/fq_shadow.py)) into a graded battery of proven cases, each a checkpoint a genuine M4 construction must reproduce:

| Checkpoint | Domain | Proven anchor | Facet it tests |
|---|---|---|---|
| CP-fq | function field | Weil/Hasse: $\lvert\alpha\rvert=\sqrt q$ | carries the Frobenius trace $t$ |
| CP-hodge | algebraic surface | Hodge index: signature $(1,\rho-1)$ on NS | indefinite $(1,n-1)$ signature |
| CP-ahk | matroid Chow ring | AHK: Whitney numbers log-concave | Hodge-Riemann with no variety (K1-clean) |
| CP-fh | arithmetic surface | Faltings-Hriljac: Neron-Tate height PD | a real proven polarization |
| CP-af | convex bodies | Alexandrov-Fenchel: Lorentzian $(1,n-1)$ | the convex signature (free, arithmetic-blind) |

A candidate supplies the structural object it specializes to in each domain; the checkpoint asks whether that object HAS the proven property (signature, log-concavity, positive-definiteness, on-circle). The score is `coverage` = (checkpoints reproduced) / 5, with the Davenport-Heilbronn firewall (euler-gated) as a hard side condition. The battery is self-validating (each checkpoint passes its own canonical witness) and it is the positive mirror of [`oracle.py`](../../experiments/lemma_db/oracle.py) (the negative D-H filter); together they are the value function. `test_shadow_battery.py` 6/6.

**The result: a real graded gradient that discriminates along the project's three axes.**

- `genuine-m4` (reproduces all five, euler-gated): **FULL, coverage 1.00.**
- `convex-only` (the convex/combinatorial signatures only, no Euler product): **PARTIAL, coverage 0.60, firewall FAILS.** The clean middle: it breaks nothing yet reproduces only three of five.
- `arithmetic-blind` (the #40 trap: convex signatures free, but $t$-blind so its $F_q$ modulus is wrong, and no Euler product): **BROKEN at CP-fq.** It is seductive on three checkpoints and breaks the one that carries $t$.
- `too-strong` (de Branges: forces a positive-definite form where the Hodge index must be indefinite): **BROKEN at CP-hodge** (wrong signature).
- `off-line-forgery` (the $F_q$ analogue of D-H): **BROKEN at CP-fq, coverage 0.00.**

The point is not the toy candidates; it is that "no gradient at M4" has become "k of N proven cases plus the firewall," a signal a generate-evaluate loop can climb, and that the gradient already separates the three known failure modes (t-blind / wrong-signature / non-euler) without ever reading the zeros. FULL is necessary, never sufficient: only Lean validates.

## Lever B (scoped): Lean as the non-circular value function

The deepest real value signal is "does it typecheck against a proof skeleton that does not assume RH." The plan is to formalize Weil's function-field proof end-to-end, then pose the Spec($\mathbb{Z}$) lift as a proof-transport task with Lean rejecting every circular or wrong step. A survey of `lean/ZetaRH/` against this goal:

**Already sorry-free (the non-circular formal core):**
- The keystone `negDef_iff_hasseWeil` ([`HodgeIndex.lean`](../../lean/ZetaRH/HodgeIndex.lean), target #2G-1): the primitive intersection form $G_{\mathrm{prim}}=\begin{psmallmatrix}-2g&-t\\-t&-2gq\end{psmallmatrix}$ is negative-definite $\iff t^2<4g^2q$. This IS the function-field Hodge-index signature, machine-proved.
- The Euler-Sen matrix algebra ([`EulerSenLinearAlgebra.lean`](../../lean/ZetaRH/EulerSenLinearAlgebra.lean)): the cup/derivation equation, the Tate-weight nilpotent, and `rosatiPos_iff_hasseWeil` (Rosati positivity $\iff$ the Hasse-Weil bound).
- The two no-go guards ([`SenDefiniteObstruction.lean`](../../lean/ZetaRH/SenDefiniteObstruction.lean) Class A; [`TraceBlindObstruction.lean`](../../lean/ZetaRH/TraceBlindObstruction.lean) Class C: `no_trace_blind_signature`, the formal statement of the CP-fq facet, that no $t$-blind predicate decides Hasse-Weil).
- The Frobenius cup formation guard ([`FrobeniusAlgebra.lean`](../../lean/ZetaRH/FrobeniusAlgebra.lean)): `no_dh_cupTarget` (D-H cannot even form the object: the K2 firewall as a type constraint).
- The archimedean digamma kernel ([`ExplicitFormula.lean`](../../lean/ZetaRH/ExplicitFormula.lean), #EF-arch): recurrence, reflection, duplication, special values.

**The gap to an end-to-end function-field RH.** The ALGEBRAIC core (the signature equivalence) is done; the GEOMETRY is absent, in the repo and in Mathlib:
- curve / divisor / Chow-group framework and the intersection product on $C\times C$ (Large; not in Mathlib);
- the Frobenius correspondence (its graph $\Gamma$, $\Gamma\cdot\Delta=q+1-t$) (Large, given the framework);
- the Hodge index theorem for $C\times C$ delivering $G_{\mathrm{prim}}$ on the primitive part (Medium);
- the eigenvalue extraction $\alpha+\bar\alpha=t$, $\alpha\bar\alpha=q$, hence $\lvert\alpha\rvert^2=q$ from the bound (Small).

Effort to a complete function-field RH in Lean: roughly 2-3 weeks of formalization, almost all of it the geometric scaffolding around the keystone, not the keystone. `negDef_iff_hasseWeil` is the necessary bridge and, with the geometry filled in, RH-for-the-curve is a two-line corollary; but it is one link, not the chain. The three transportable theorems (the signature equivalence, the Rosati link, the Class-A guard) are the non-circular core an AI could grow the lift against.

**Reading for the AI-optimization plan:** B is the highest-value structural investment because it is the only lever that makes lever-5 (a verifier-trained loop) possible. The bottleneck is that Mathlib has no algebraic-curve intersection theory, so a real chunk of the work is upstreamable infrastructure that also benefits the wider community.

**Lever B, first step BUILT (2026-06-14).** [`lean/ZetaRH/FunctionFieldRH.lean`](../../lean/ZetaRH/FunctionFieldRH.lean) (build green, 3147 jobs, Lean v4.30.0) makes the genus-1 function-field RH chain explicit and proves the eigenvalue-extraction end sorry-free: `eigenvalue_modulus` (a non-real root of $X^2-tX+q$ has $|\alpha|^2=q$, via Vieta on the conjugate root), `root_nonreal` ($t^2<4q\Rightarrow$ the roots are non-real), and the implication `functionfield_RH_elliptic_of_hodge` (the Hodge-index input $\Rightarrow|\alpha|=\sqrt q$, wiring the existing keystone `negDef_iff_hasseWeil` #2G-1). The chain is now **fully sorry-free** (2026-06-14 follow-up): the geometric step (Castelnuovo-Severi, $t^2<4q$) is carried as an explicit hypothesis field `hodge_index` of an `EllipticFrobeniusData` structure, from which `negDef_of_curve` and `functionfield_RH_elliptic` derive RH-for-the-curve sorry-free. So the function-field RH skeleton is a sorry-free **conditional** theorem whose single assumption is the curve-intersection geometry Mathlib lacks (VERIFIER targets #FF-1 and #FF-geom, both no longer `sorry`). This also repaired a latent defect: the previous `hodge_index_curve_elliptic` admitted a false proposition (`NegDef 1 q t` for all $q,t$) behind a vacuous hypothesis. An AI/human grows the Spec($\mathbb{Z}$) lift against this non-circular scaffold by discharging the explicit geometric hypothesis.

## Lever C (run): the regime-two frame-audit

The one unspent discovery axis: does a single distant frame collapse two of the M4 conjuncts into one statement, the way the acoustic frame made "carries-trace" (P1) and "euler-gated/passive" (P4) the same statement? Run as a structured multi-agent workflow over all ten pairs of the five M4 properties (P1 carries-trace, P2 global, P3 noncircular, P4 euler-gated, P5 = the blind-spot indefinite polarization), each pair searched for a co-extensive frame, each genuine claim adversarially verified.

**Result: the fifth independent convergence, plus one new structural datum.**

- Of ten pairs, nine returned NONE; one (P3-P4) returned CORRELATED; **zero new genuine collapses survived verification.** The audit found no new lever.
- **P5 is an isolated vertex.** Every pair containing the blind spot (P1-P5, P2-P5, P3-P5, P4-P5) returned NONE, examined in the strongest available frames (Connes/Tomita-Takesaki KMS with de Branges as its analytic face; the Bombieri-Weil explicit-formula positivity on the adele class space; the Hodge-Riemann/AHK indefinite frame; Bost-Connes KMS thermodynamics). No cheap property is co-extensive with P5. The sharpest sub-result: the AHK Hodge-Riemann frame, the only R3.5-escaping (P3-clean) frame even capable of touching P5, was examined and found NOT to deliver the iff unconditionally. The one frame that could have produced a jackpot is exactly the one whose verdict is "not unconditional": the marginal-positivity wall restated as an audit.
- **The new datum: the M4 property graph has exactly two edges, both at the cheap layer, sharing the Euler-product vertex.** P1-P4 (acoustic, known) and P3-P4 (Rosati/Frobenius-algebra, CORRELATED). The "easy four" are not five independent asks; they are coalescing around P4, while P5 stays a lone island. This is the marginal-positivity thesis re-derived from the connectivity of the property graph.

**The single highest-value next probe it surfaced:** attack the one live edge, not the dead island. Can the P3-P4 CORRELATED edge be upgraded to GENUINE by the minimal extra hypothesis that forces existence-of-a-positive-dagger from existence-of-the-algebra? Concretely: in the polarized-Frobenius frame, does requiring $\mathcal{A}$ to be a finite von Neumann algebra with a faithful normal positive trace state (not a bare $\ast$-algebra) make "$\mathcal{A}$ exists and is euler-gated" co-extensive with "$\mathcal{A}$ carries an intrinsic positive Rosati involution"? If yes, it converts the correlation into an iff and names the residual to P5 as a single concrete operator-algebra deficiency. It is also cheap to falsify: the Bost-Connes / KMS thread already built the von Neumann / KMS machinery, so the probe is "does the BC trace state induce a Rosati dagger on the arithmetic Frobenius algebra, and is its positivity equivalent to euler-gating," runnable against the existing lemma DB and the D-H control. Expected outcome is still NONE-or-CORRELATED (the polarization will not come for free), but it interrogates new structure rather than re-screening the island.

## The honest ceiling (a coordinate, not a wall)

The project's own findings predict where this stops: nothing cheap touches P5, and the construction-grade synthesis at the kernel is genuinely research-grade. The realistic AI contribution is to make the kernel as small, as crisp, and as surrounded-by-gradients as possible (levers A, C, and the 09A decomposition), build the verification scaffold (lever B), and only then run a verifier-trained loop (lever 5) that has a real signal to climb. That is not pessimism; it is the same compass logic the project runs on. Each lever narrows where the proof must live: A gives the search a gradient, B gives it a non-circular floor, C confirms the gradient cannot be cheated into the kernel and isolates the one live edge to push.

## Pointers

- Built: [`experiments/lemma_db/shadow_battery.py`](../../experiments/lemma_db/shadow_battery.py) + [`test_shadow_battery.py`](../../experiments/lemma_db/test_shadow_battery.py) (6/6).
- Scoped: `lean/ZetaRH/` (keystone `HodgeIndex.lean` #2G-1; the sorry-free core; the geometry gap).
- Run: the regime-two frame-audit workflow (11 agents); finding recorded as LEARNINGS #98.
- Spine: [`all_roads_to_the_signature.md`](all_roads_to_the_signature.md), [`research_directions/09A_ahk_arithmetic_lattice.md`](research_directions/09A_ahk_arithmetic_lattice.md), [`research_directions/08A_rosati_standard_conjecture.md`](research_directions/08A_rosati_standard_conjecture.md) (the M1-M5 ladder the P3-P4 probe lives in).
