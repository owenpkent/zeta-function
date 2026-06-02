# State of the proof program (repo-wide)

> A one-page strategic snapshot of the whole project: where every architecture
> stands, what wall each hit, where the live work is, and the single most-leveraged
> next move. Companion to the operational [`PHASE_STATE.md`](PHASE_STATE.md) (current
> sub-task, falsifiability triggers) and the synthesis surface
> [`experiments/LEARNINGS.md`](experiments/LEARNINGS.md) (26 cross-architecture
> findings). Last updated: 2026-05-29 (after session 005).

## The thesis in one paragraph

The program does not have a proof of RH and is not close to one. What it has is a
**sharp map of where the proof cannot live and a precise specification of the one
place it can**. Three of the four candidate architectures are closed as routes to RH
(not because they are wrong, but because each provably reaches a ceiling). The fourth
(arithmetic-geometric, Architecture 2) is open, and the project has converted its
central problem from a slogan ("build new mathematics for $\mathrm{Spec}(\mathbb{Z})$")
into a **computed specification** of the single missing object. The dominant
meta-finding, validated five independent ways, is the **marginal-positivity thesis**:
RH is true only at the margin, so any proof must engage the *exact* structure of
$\zeta$ (Euler product, functional equation, archimedean factor), not generic
positivity. That is a compass, not a verdict.

## The four architectures

| Arch | What it is | Status | The wall (what we learned) |
|---|---|---|---|
| **1. Spectral** (Hilbert-Pólya) | self-adjoint operator with eigenvalues = zero heights | **Closed at project level** (1A-1D) | Candidate operators (Berry-Keating, Sierra-Townsend) are L-function-*agnostic*; they match statistics but cannot prove self-adjointness or distinguish $\zeta$ from controls. A Level-3 statement. |
| **2. Arithmetic-geometric** (Deninger / $\mathbb{F}_1$) | cohomology + Frobenius + Hodge index on a surface below $\mathrm{Spec}(\mathbb{Z})$ | **LIVE** (Direction 8) | The single-arithmetic-surface side is complete and validated; the gap is the *product* surface and its Frobenius. See below. |
| **3. Direct positivity** (Weil / Li) | a quadratic form / sequence is $\ge 0$ iff RH | **Closed as a soft route** (3A-3L) | Every positivity reformulation is sharp at **zero margin**. Trace-identity positivity is circular (the K1 wall, R3.5). The Gram-matrix detector counts off-line zeros exactly (wrong-approach control). |
| **4. Analytic** (zero-free regions) | push the Vinogradov-Korobov $2/3$ exponent to $1/2$ | **Closed as a route to RH** (4A-4E.9) | The $2/3$ ceiling is structural (auxiliary inequality saturated, V-MVT sharp post-BDG 2016). The entire LP/SDP/SOS family is closed. Arch 4 is constraint-mapping, not a route. |

Each "closed" is a coordinate: it tells us the proof is **not** a soft/statistical/
analytic argument, so effort concentrates on Architecture 2's structural route.

## The live front: Architecture 2 / Direction 8

The bet (the same one that worked for the function-field RH via Weil/Grothendieck/
Deligne): build a surface whose **intersection-form signature** forces the zeros onto
the line. What is in hand vs. missing:

**In hand (computed and validated):**
- **2G** the function-field template: on $C \times C$ the primitive intersection form is negative definite, and that signature *is* the Hasse-Weil bound (machine-proved in Lean).
- **2H/2M** over $\mathrm{Spec}(\mathbb{Z})$: the Néron-Tate height pairing is positive definite, ranks 1-4 (Faltings-Hriljac; regulators match LMFDB).
- **2I/2L/2O/2P** the complete local-height decomposition (archimedean Green/Petersson + every finite prime) summing to $\hat h$ by the authoritative algorithm.
- **2K** the dictionary: the explicit-formula place-decomposition $M = A_{\mathrm{arch}} + P_{\mathrm{fin}} + B_{\mathrm{pole}}$ maps to the would-be intersection numbers, with the pole at $s=1$ as the hyperbolic $(+1)$ direction.
- **2Q** (session 005): the missing correspondence $\Gamma_S$ must carry a **place-dependent $(1,p)$ bidegree** (not the function field's single scale $q$); this *forces* infinite-dimensional $H^i$ and the Deninger $\mathbb{R}$-flow, and pins $\Gamma_S^2$ to the von Mangoldt prime sum.
- **2R** (session 005): that $\Gamma_S^2$ realized concretely as a Ruelle dynamical-zeta log-derivative (orbit lengths $\{\log p\}$, $-\zeta'/\zeta = \sum_n \Lambda(n) n^{-s}$); D-H has no such orbit spectrum.
- **M3 Analytic Domination** (session 008, PARTIAL): a *numerical* discriminator, not yet a proof. Splitting $P_{\mathrm{fin}}$ into prime-power $P_{\mathrm{pp}}$ and composite $P_{\mathrm{comp}}$ and deleting $P_{\mathrm{comp}}$ gives $M_{\mathrm{euler}} = A_{\mathrm{arch}} + P_{\mathrm{pp}} + B_{\mathrm{pole}}$, which separates the three controls correctly (zeta $+0.035$, D-H $-0.929$, Epstein $+0.676$) and passes the D-H discipline where the full $M$ did not. Caveat: for a non-Euler $L$ the deletion of $P_{\mathrm{comp}}$ is imposed by hand and equals the Euler-product assumption; that $M_{\mathrm{euler}} \ge 0 \Leftrightarrow$ RH, and that $M_{\mathrm{euler}}$ is the canonical geometric trace, is the [Direction 8B/8C](docs/03_research/research_directions/08C_cohomological_signature.md) conjecture, not a result. The analytic domination proof remains open.

**The one missing object:** the product surface $\mathrm{Spec}(\mathbb{Z}) \times \mathrm{Spec}(\mathbb{Z})$ with a genuine intersection pairing realizing these numbers, and a cohomology carrying the **signature** (not just the spectrum, which 2R supplies). This is Direction 4.6 (leafwise prismatic cohomology with a trace formula) feeding Direction 8 (the Hodge index theorem on the surface). Untouched at the construction level; multi-year, multi-person.

## The cross-cutting compass

- **Marginal positivity** (LEARNINGS #7, #11-#13): no buffer for soft proofs. Dig at the exact structure of $\zeta$.
- **Four-level framing**: RH is Level 4 (positivity/signature). Level 3 (statistics, GUE, spectral) is compatible with a world where some zero has $\beta = 0.51$, so it cannot close RH.
- **Davenport-Heilbronn discipline**: the wrong-approach detector. Now sharpened to a **bidegree statement** (2Q): no Euler product $\Rightarrow$ no $(1,p)$ local bidegrees $\Rightarrow$ no $\Gamma_S$ $\Rightarrow$ no surface. Any method that "works" for D-H is wrong.

## Lean substrate

Phase 1 green (Lean 4.13.0 + Mathlib v4.13.0, all modules compile). Real machine-proved
content: `RiemannHypothesisMathlib_iff_RiemannHypothesis_zeta`; `negDef_iff_hasseWeil`
(2G); and session 005's additions in `ExplicitFormula.lean` (the Weil explicit formula +
positivity criterion scaffold, #EF-1/#EF-2), three discharged bridge lemmas
(#MB-1/#MB-2/#MB-6: $\zeta$ pole, nonvanishing, functional equation), and (session 008)
six sorry-free digamma identities discharging the kernel part of #EF-arch: the recurrence
$\psi(s+1)=\psi(s)+1/s$, reflection $\psi(1-s)-\psi(s)=\pi\cot\pi s$, iterated recurrence
$\psi(s+n)=\psi(s)+\sum_{k<n}1/(s+k)$, duplication $\psi(2s)=\tfrac12(\psi(s)+\psi(s+\tfrac12))+\log 2$,
and the special values $\psi(1)=-\gamma$, $\psi(\tfrac12)=-\gamma-2\log 2$ (the half-integer
arguments of $\zeta$'s archimedean kernel); all upstreamable to Mathlib. Project sorry count 23
(the digamma additions are all sorry-free). The highest-leverage remaining target is the Weil
explicit formula itself (LEARNINGS #17), which needs a sum-over-zeros theory Mathlib lacks, and
the remaining #EF-class integral pairing. See [`lean/README.md`](lean/README.md).

## The single most-leveraged next move

**Test the conjecture M3 leans on, then construct the Product Surface Intersection Signature (Direction 8):**
M3 supplied a trace-side discriminator ($M_{\mathrm{euler}}$) but it rests on an unproven step: that prismatic geometry forces $P_{\mathrm{comp}} = 0$, making the hand-deletion of the composite block canonical rather than the Euler-product assumption in disguise. The cheapest high-value move is to stress that step. If it survives, build the geometric framework that realizes $M_{\mathrm{euler}} \ge 0$ on $\mathrm{Spec}(\mathbb{Z}) \times \mathrm{Spec}(\mathbb{Z})$ (the Hodge index signature on the Bhatt-Lurie or Connes-Consani spaces). If it fails, M3 is the Euler-product assumption restated and Direction 8B/8C needs rethinking.

Honest odds (per the direction docs): Direction 8 unconditional success is under 1%; its
value is that any outcome (proof, or a refutation showing the natural intersection form
has the wrong signature) would be a top-tier result, and the partial results
(arithmetic intersection theory, the surface frameworks) are contributions in their own
right.

**Two concrete leads from the reference-library read-through** (26 sources, deep notes in
[`docs/03_research/reading_notes/`](docs/03_research/reading_notes/)). The literature
independently confirms the 2Q/2R reduction and locates the gap identically (the signature,
not the trace formula, is the open step). It also surfaces the two most concrete objects to
push on:

1. **Bhatt-Lurie's Cartier-Witt stack `WCart`.** Absolute prismatic cohomology is "de Rham
   relative to $\mathbb{F}_1$" (a candidate for 2K's missing base point), it carries a global
   Frobenius that is a contraction collapsing `WCart^HT` to the de Rham point, and a **Sen
   operator $\Theta$** that is the literal generator of the cyclotomic flow ($\gamma_u =
   u^\Theta$). That is the closest existing object to Deninger's eigenvalue generator / the
   Direction-4.6 flow, on the finite-places (p-adic transversal) substrate Leichtnam 2006 uses.
2. **Connes-Consani's square $\widehat{\mathbb{N}^2}$.** They already build the product object
   (Newton polygons in $\mathbb{Z}\times\mathbb{Z}$) with one-parameter Frobenius correspondences
   $\Psi(\lambda)$ and a composition law. The gap is isolated and sharp: the characteristic-1
   operations are idempotent, so there is **no signed intersection pairing / Hodge index yet**.
   Putting a signature on this square is Direction 8 in its most concrete current form.

## Canonical pointers

- Operational state / next sub-task: [`PHASE_STATE.md`](PHASE_STATE.md)
- Cross-architecture findings (26): [`experiments/LEARNINGS.md`](experiments/LEARNINGS.md)
- Test plan + per-architecture status: [`experiments/PROOF_ARCHITECTURES_PLAN.md`](experiments/PROOF_ARCHITECTURES_PLAN.md)
- Master research map (all approaches, obstructions): [`docs/research_atlas/README.md`](docs/research_atlas/README.md)
- What new mathematics must look like: [`docs/03_research/new_mathematics.md`](docs/03_research/new_mathematics.md)
- The eight research directions: [`docs/03_research/research_directions/`](docs/03_research/research_directions/)
- Reference library (26 sources) + deep reading notes: [`references/README.md`](references/README.md), [`docs/03_research/reading_notes/`](docs/03_research/reading_notes/)
- Latest session narrative: [`experiments/orchestrator_sessions/session_005.md`](experiments/orchestrator_sessions/session_005.md)
- Lean substrate + VERIFIER targets: [`lean/README.md`](lean/README.md)
