# Riemann Zeta Function — Deep Study Repo

A multi-level exploration of the Riemann Zeta Function and the Riemann Hypothesis: from intuitive visual understanding through graduate-level analysis to the frontier of current research. Includes a computational experimental thread organized around testing the four candidate RH proof architectures.

**Operational substrate**: this repo is also structured as the substrate for an AI-augmented (and, speculatively, AI-only) proof program for RH. See [`STATE_OF_THE_PROGRAM.md`](STATE_OF_THE_PROGRAM.md) for a one-page repo-wide strategic snapshot (where every architecture stands and the single most-leveraged next move), [`OPERATIONS.md`](OPERATIONS.md) for how to operate it, [`PHASE_STATE.md`](PHASE_STATE.md) for current state, [`docs/03_research/proof_program.md`](docs/03_research/proof_program.md) for the AI-augmented plan, and [`docs/03_research/proof_program_ai_only.md`](docs/03_research/proof_program_ai_only.md) for the AI-only speculative variant. The repo is a handoff artifact: ~50-70% of Phase 0 is done; Phases 1-5 require expert collaborators and multi-year compute.

## What's Here

This repo is structured so you can enter at any level and go as deep as you want.

```
zeta-function/
├── docs/                        # All written explanations
│   ├── 00_intuitive/            # No math required: visual, conceptual
│   ├── 01_undergraduate/        # Calculus, complex numbers, series
│   ├── 02_graduate/             # Analytic continuation, functional equation,
│   │                            #   log-correlated fields, four-level RH framing
│   ├── 03_research/             # Current approaches, extreme values, PROOF PROGRAMS
│   │   ├── proof_program.md     # ★ AI-augmented (human-led) proof program
│   │   ├── proof_program_ai_only.md  # ★ AI-only speculative variant
│   │   └── research_directions/ # ★ 8 research-grade directions with operational specs
│   │   └── reading_notes/       # ★ Full-depth notes on all 26 reference-library sources
│   ├── implications/            # Why it matters (primes, physics, crypto)
│   ├── solutions/               # Known approaches to the Riemann Hypothesis
│   └── research_atlas/          # Master research map: all attempts, failures, ML directions
├── experiments/                 # ★ Computational thread; proof-architecture tests
│   ├── PROOF_ARCHITECTURES_PLAN.md    # Test plan + AI-centric methodology
│   ├── LEARNINGS.md             # 26 cross-architecture findings
│   ├── _shared/                 # LFunction interface, zeta, Davenport-Heilbronn control
│   ├── positivity/              # Arch 3 (Li coefficients, Weil quadratic form, 3B.3 rigorous)
│   ├── spectral/                # Arch 1 (Berry-Keating discretization)
│   ├── zero_free/               # Arch 4 (LP/SDP family through 4E.8)
│   ├── arithmetic_geometric/    # Arch 2 (2A diff, R1-R5, R3.6, R3.6.3, 2C, 2D, 2E)
│   └── multifractal/            # Log-correlated field experiments (pre-existing)
├── references/                  # ★ Reference library (26 sources, gitignored PDFs) + tracked index
├── lean/                        # ★ Lean 4 / Mathlib formal verification (skeleton)
│   ├── lakefile.lean
│   ├── ZetaRH.lean              # Main module
│   └── ZetaRH/                  # R3.5, LineRestriction, LambdaBlueprints, HodgeIndex, ...
├── .claude/agents/              # ★ AI agent role specifications for AI-only execution
│   ├── surveyor.md              # Literature survey + scorecard maintenance
│   ├── builder.md               # Propose constructions
│   ├── verifier.md              # Formalize in Lean 4
│   ├── adversary.md             # K1-K4 attack; D-H discipline
│   ├── synthesizer.md           # Integrate outputs into project dossier
│   └── orchestrator.md          # Schedule work, manage compute budget
├── sources/                     # Original PDFs and their converted text
├── visualizations/              # manim animation scripts
├── OPERATIONS.md                # ★ How to operate this repo as the proof-program substrate
├── PHASE_STATE.md               # ★ Current operational state (read by ORCHESTRATOR)
└── CLAUDE.md                    # Project + owner context for AI assistants (merged successor of LLM_ONBOARDING.md)
```

## The Question

The **Riemann Hypothesis** states:

> All non-trivial zeros of the Riemann zeta function have real part equal to 1/2.

It has been open since 1859. It is one of the Millennium Prize Problems (worth $1,000,000). It governs the distribution of prime numbers, and its implications ripple through number theory, physics, cryptography, and beyond.

## Stance

We are trying to solve this. That is the posture of the whole repo.

It is hard. The odds against any single program are long, and 166 years of effort by the best mathematicians alive is the honest baseline. But "hard" is not "impossible," and this project treats RH as a target, not a monument.

Read every negative result here in that spirit. When an experiment shows that a method fails (Level 3 statistics cannot pin a single zero, the classical analytic ceiling sits at the $2/3$ exponent, NCG alone hits the K1 wall, soft positivity has zero margin), that is **progress**: it removes a dead branch and sharpens where the real proof must live. Each "this won't work" is a coordinate that narrows the search, not a verdict that the search is hopeless.

The dominant finding (RH is true only at the margin, so the proof must engage the **exact** structure of $\zeta$) is a compass, not a wall. It tells us where to dig. The job is to keep digging there.

## Levels

| Level | Folder | Prerequisites |
|-------|--------|---------------|
| Intuitive | `docs/00_intuitive/` | None — curiosity only |
| Undergraduate | `docs/01_undergraduate/` | Calculus, basic complex numbers |
| Graduate | `docs/02_graduate/` | Complex analysis, real analysis |
| Research | `docs/03_research/` | Graduate mathematics |
| **Research Atlas** | `docs/research_atlas/` | **Start here for ML research** — full catalog of approaches, failures, obstructions, and ML directions |

## Visualizations (manim)

Built with [manim](https://github.com/3b1b/manim) (3Blue1Brown's animation engine).

See `visualizations/README.md` for setup and how to render each scene.

## Source PDFs

Original source PDFs and their converted text versions live in `sources/`.

## Experimental thread

See [`experiments/PROOF_ARCHITECTURES_PLAN.md`](experiments/PROOF_ARCHITECTURES_PLAN.md) for the test plan. Four candidate RH proof architectures (spectral, arithmetic-geometric, direct positivity, analytic) with the Davenport-Heilbronn L-function as a structural wrong-approach detector throughout. ~25 experiments + literature reviews implemented across the four architectures, plus full dossier coverage for 5 of 6 major Arch 2 candidates (Borger, Lorscheid, Connes, Deninger, Deitmar). Arch 3 (positivity) has the deepest experimental thread, including a Gram-matrix wrong-approach detector validated at four T_max values (`n_neg` exactly equals number of off-line zero pairs in upper half plane at T_max ∈ {200, 300, 350, 500}).

Smoke test:
```powershell
python -m experiments._shared.smoke_test
```

## Cross-cutting findings

Synthesis of structural insights across architectures lives in [`experiments/LEARNINGS.md`](experiments/LEARNINGS.md). The dominant meta-finding from the experimental thread: **RH is true only at the margin**. Every positivity reformulation (Weil-form, Li, de Bruijn-Newman, MT shape factor) is sharp at zero margin. Five independent reinforcing directions (LEARNINGS findings #7, #11, #12, #13 + Arch 3E literature review) point the same way. This is the project's most useful piece of map: it tells us a winning proof must use the EXACT structure of $\zeta$ (Euler product, functional equation, archimedean factor) rather than generic positivity arguments. The margin result rules out the soft routes so that effort concentrates on the structural one.

The 17-constraint framework for Architecture 2 candidates (see [`experiments/arithmetic_geometric/2A_candidate_evaluation.md`](experiments/arithmetic_geometric/2A_candidate_evaluation.md)) operationalizes the comparison of $\mathbb{F}_1$ programs and identifies the geometric route (intersection theory + Hodge index theorem on a constructed surface) as the unique remaining direction for breaking the K1 wall on positivity. The path forward strategic synthesis is in [`experiments/arithmetic_geometric/2A_path_forward.md`](experiments/arithmetic_geometric/2A_path_forward.md).

## Status

| Area | Status |
|------|--------|
| Repo structure | ✅ Complete |
| Solutions / approach catalog | ✅ `docs/solutions/` |
| Research atlas | ✅ `docs/research_atlas/` |
| Graduate docs (incl. log-correlated, four-level framing) | ✅ Substantial |
| Experiments — Phase 0 infrastructure | ✅ Complete |
| Experiments — Arch 3 (positivity) | ✅ 3A-3D, 3B.2, 3D.2-3D.4, 3E (literature), 3F-3I, 3J (Schur complement against on-line cushion gives ~30x sharper detector than raw spectrum, rel min asymptote -78.7%), 3K (hypothetical off-line zero perturbation, disproof path closed in Gram-matrix family) complete; **3L (Epstein zeta second control): the Schur detector obeys the same counting law (schur_neg = #off-line heights) on a structurally independent off-line construction, generalising the wrong-approach discipline beyond D-H; 3B.4: second Li-criterion off-line witness (Epstein) + rigorous Selberg discrimination** |
| Experiments — Arch 1 (spectral) | ✅ 1A, 1B, 1C, 1D complete (1D as literature review of Connes adèle class space) |
| Experiments — Arch 4 (zero-free regions) | ✅ 4B, 4D, 4D.2, 4E, 4E.2-4E.8 complete; 4A+4C unified literature dossier (V-K $2/3$ exponent is a structural ceiling after BDG 2016; Arch 4 is constraint-mapping, not a route to RH); **4E.9 (Heath-Brown multi-zero MT SDP, Direction 7): the multi-zero MT shape factor does not exceed the 1D Fejér ceiling (best ratio ≤ 1, rank-2 certificate). The LP/SDP/SOS family is now fully closed** |
| Experiments — Arch 2 (arithmetic-geometric) | ✅ 2A, 2B, 2E complete (2A includes R1-R5 evaluation framework with hybrid proposals AND 5 of 6 candidate dossiers: Borger, Lorscheid, Connes, Deninger, Deitmar; 2E confirms bare $\psi_p$ on concrete Λ-rings has no zeta-zero-like spectrum, validating R5's cohomology-must-lift framing); **2F (Hodge-index sweep): the function-field RH bound $|\alpha_i| = \sqrt{q}$ holds exactly across a family of curves over finite fields, exhibiting the positivity target a Spec($\mathbb{Z}$) lift must reproduce**; 2C (F_1/Arakelov survey) and 2D (Deninger micro-target → Direction 4) complete. **Direction 8 opened (session 004): 2G — the Hodge index as a SIGNATURE on $C\times C$ (primitive form negative definite $=$ Hasse-Weil, machine-proved in Lean); 2H/2M — the Faltings-Hriljac height pairing over Spec($\mathbb{Z}$) is positive definite at ranks 1-4 (regulators match LMFDB); 2I/2L/2P — the complete Silverman local-height decomposition (archimedean + every finite prime) validated $h_\infty+\sum_p h_p = \hat h$ by the authoritative algorithm; 2K — the dictionary mapping all of this to the would-be $\mathrm{Spec}(\mathbb{Z})\times\mathrm{Spec}(\mathbb{Z})$ intersection form. The single-arithmetic-surface side is complete and validated; the remaining gap is the product surface + Frobenius. **Session 005: 2Q — the place-dependent bidegree obstruction (the arithmetic Frobenius correspondence $\Gamma_S$ must carry a $(1,p)$ bidegree per prime, not a single scale $q$; forces infinite-dim $H^i$ + the Deninger $\mathbb{R}$-flow, pins $\Gamma_S^2$ to the von Mangoldt prime sum); 2R — realizes that $\Gamma_S^2$ concretely as a Ruelle dynamical-zeta log-derivative ($-\zeta'/\zeta$, orbit lengths $\{\log p\}$), with the D-H control showing no such orbit spectrum exists.** |
| Research spine + framing (session 007, 2026-05-30) | ✅ **All roads lead to the signature.** Five new directions proposed (9-13, each attacking the #25 bidegree obstruction); two cheap D-H falsifications (Li log-concavity = non-Euler detector not RH; Jensen/Turán = stealth window; LEARNINGS #27); **Direction 10 (THH/TC over the sphere spectrum)** pushed to Hesselholt's proven $\zeta = \det_\infty(s-\Theta\mid\mathrm{TP})$ template (#28-29). **Synthesis** ([`docs/03_research/all_roads_to_the_signature.md`](docs/03_research/all_roads_to_the_signature.md), #30): every framework realizes $\zeta$ (a determinant/trace), but RH is the SIGNATURE, the same positivity everywhere. **Sharpened** to the standard form ([`08A_rosati_standard_conjecture.md`](docs/03_research/research_directions/08A_rosati_standard_conjecture.md)): **RH = arithmetic Rosati positivity = the arithmetic Hodge standard conjecture**, with an M1-M5 milestone ladder. M1 done (2T: function-field Rosati positivity, four equivalent faces, #31); M2 assembled (2U, #32); M2.5 done (2V, #33: $A_{\mathrm{arch}}$ fixed + $T_{\max}$-validated, diagnostic corrected to $\min\mathrm{eig}$, non-circular Weil form for $\zeta$ POSITIVE $+0.035$, necessary-not-sufficient). **M2.6 done (2W, #34): general-$\mu$ archimedean constant fixed ($C_\mu = \log\pi - \psi((1+\mu)/2)$; D-H block residual $5.58\to0.12$, validated), but the four-way verdict hits the STEALTH WINDOW: D-H reads spuriously positive ($+0.094$) because its off-line obstruction ($\gamma\approx85.7$, $\sim$2.6%) is below the residual floor (#18/#19/#27 on the Rosati side). CONSEQUENCE: M3 must be ANALYTIC** (prove archimedean-dominates-prime domination via the exact off-line structure), not a finer numerical truncation. The non-circular Weil-form infrastructure (any $\Gamma$ factor) is complete + validated; the open problem is the analytic domination. Framing recast to a research-program stance; operating philosophy in [`docs/researcher_mindset.md`](docs/researcher_mindset.md). |
| M3 + stress tests (session 008, 2026-06-01) | 🟡 **M3 is a validated numerical discriminator, not geometric progress.** The attempt (e3m) split $P_{\mathrm{fin}}$ into prime-power $P_{\mathrm{pp}}$ + composite $P_{\mathrm{comp}}$ and formed $M_{\mathrm{euler}} = A_{\mathrm{arch}}+P_{\mathrm{pp}}+B_{\mathrm{pole}}$ by deleting $P_{\mathrm{comp}}$: separates the controls (zeta $+0.035$, D-H $-0.929$). Stress-tested in three threads: **(#35, e3m2)** survives the false-negative probe -- independent Euler products $\chi_3,\chi_4$ stay positive with $P_{\mathrm{comp}}=0$ exactly; **(#36, e3m3)** fires negative on a second, independently-constructed and FE-verified off-line control at conductor 7 ($\rho = 1.0616+28.44i$, $|f(\rho)|\sim$2e-50), removing the single-example fragility (both witnesses still Davenport-Heilbronn-type); **(#37)** the geometric conjecture "absolute prismatic cohomology forces $P_{\mathrm{comp}}=0$" is VACUOUS for $\zeta$ ($P_{\mathrm{comp}}=0$ is the Euler product, a theorem, so $M_{\mathrm{euler}}=M$ already) and INAPPLICABLE to D-H (no Euler product $\Rightarrow$ no surface), so it is struck from the Direction 8 ladder. Net: M3 reorganized bookkeeping; the genuine gap (construct the surface for $\zeta$ + prove its cup-product signature) is unchanged. Earlier "breakthrough / stealth window broken" framing corrected throughout. |
| Direction 12 (de Bruijn-Newman) heat side (session 009, 2026-06-02) | ✅ **Kernel positivity is orthogonal to RH** (E_DBN1, LEARNINGS #38). First heat-side experiment, closing the gap `3e` deferred. A Bochner/Toeplitz + max-modulus test (project idiom) for the Pólya kernel positivity $\Phi\ge0$, validated on $\zeta$ vs Pólya's closed form to 4.4e-16. Finding: $\Phi\ge0$ is **K2-failing** -- the RH-false Davenport-Heilbronn passes it identically to $\zeta$ (clean degree-1), because off-line zeros are archimedean-suppressed in the kernel to $\exp(-\tfrac\pi4 d\gamma)$ ($|\Xi_{DH}(85.7)|=1.5\mathrm{e}{-}29$; measured rates $0.73\!\sim\!\pi/4$ deg-1, $1.59\!\sim\!\pi/2$ deg-2) -- the **stealth window in the heat basis**, the softest detector yet. Verified by a 4-agent workflow (independent re-implementation reproduced every number; D-H off-line zero refined to $0.80852+85.6993i$). **Honest framing: the conclusion is correct but PRE-EMPTED** (Dobner 2020 -- extended Selberg class $S^\#$ incl. D-H; Newman-Wu 2019; convergent Michalowski 2026), so a confirmed coordinate importing 3 corroborating references, not new mathematics. Isolated then **RESOLVED** Level-4 sub-target 12.4 (LEARNINGS #39): the Rodgers-Tao $\Lambda\ge0$ functional $\leftrightarrow$ Weil/Hodge positivity bridge is **FALSE**. An equation-level survey shows Rodgers-Tao's functional is the log-gas Hamiltonian $\sum\log\frac1{|x_j-x_k|}$ on the zeros — RH-agnostic in sign ($dH/dt=-4E\le0$ always), a Level-3 statistical object — not the Weil quadratic form; its input (Montgomery pair correlation) is consumed as Level-3 statistics. So $\Lambda\ge0$ is the Level-3 half and $\mathrm{RH}{=}(\Lambda\le0)$ the Level-4 signature; the flow does not short-circuit to the signature. Confirms the four-level framing and re-isolates Direction 8 (the product surface) as the irreducible target. |
| Direction 8 (product surface) first probe (session 009, 2026-06-02) | 🟡 **The Connes-Consani square's tropical Hodge index is free but arithmetic-blind** (2CC, LEARNINGS #40). First numerical probe of the product object (C-C arithmetic-site square = Newton polygons under convex-hull-union + Minkowski-sum). Its canonical mixed-volume form is Lorentzian by **Alexandrov-Fenchel** -- a Hodge-index signature $(1,k)$ exists FOR FREE (verified, robust over 2000 random collections). BUT it is the **characteristic-1 shadow**: arithmetic-blind, it freezes the Frobenius trace $t$ ($\Delta\cdot\Gamma = p{-}1$, not the point count $q{+}1{-}t$), so its $(1,3)$ signature is UNCONDITIONAL / RH-agnostic -- the trivial extreme of the #38/#39 soft-positivity pattern. Reconciles with the gap's "no signed pairing": the RH-agnostic convex-geometry shadow exists; the **arithmetic** pairing carrying $t$ does not. **Gap sharpened to the arithmetic $q$-lift that restores $t$**, with the $(1,p)$ bidegree (2Q) its locus. Realizes attack angle 4.A (tropical/AHK) on the specific surface and shows why it is insufficient. ADVERSARY-checked (PASS, softened): a *proposed* shadow (toric-BKK analogy), not a constructed intersection theory of the topos. **2CC.2 (#41)** then probed the diagonal: the self-composition $\Psi(\lambda)\circ\Psi(\lambda^{-1})=\mathrm{Id}_\epsilon$ (C-C Thm 7.7) **does** carry the von Mangoldt $-\zeta'/\zeta$ (its tangent $=$ the Deninger-Hesselholt flow generator $\Theta$; $-d/ds\log\det_\infty(s-\Theta)=-\zeta'/\zeta$), refining 2CC -- the diagonal self-intersection is trace-rich where the off-diagonal point-count froze. But it is the TRACE, not the signature; the q-lift gap is unchanged. Connects C-C $\leftrightarrow$ 2R $\leftrightarrow$ Deninger/Hesselholt. **2CC.3 (#42)** then *tried* the q-lift (probe a): it DECOMPOSES into un-idempotent-ization (formal -- the soft-max restores subtraction, so a signed pairing becomes possible; the 2CC idempotency obstruction is removable) + per-prime lift (the known finite-q FF Hodge index, carries t) + the GLOBAL local-to-global assembly = the gap. The attempt crosses the first two and LOCALIZES the third: the zeros live in the analytic continuation Re(s)<1, invisible to the local Euler/orbit data (converges only Re(s)>1; on the critical line $\prod_p(1-p^{-s})^{-1}$ does not converge). The irreducible step is realizing the continuation as a signed pairing on the global $H^1$ = the missing Weil cohomology (M3/#25), unchanged. Not crossed -- localized. |
| Direction 8 (product surface) continued (session 009, 2026-06-02) | 🟡 **Two more coordinates + a consolidated map; the polarization is the universal gap.** **2DB.1 (#43):** the de Branges / Conrey-Li per-zero cross-term $Q(\rho) = -\mathrm{Re}\{\xi'(\rho)\xi(1+\rho)\}$ is the exact CONVERSE of #42 -- the global de Branges pairing DOES see the zeros, but its positivity is strictly-stronger-than-RH and FAILS for $\zeta$ (only $k{=}34$ negative of the first 50; reproduced Conrey-Li's $-5.389\mathrm{e}{-}69$ to 12 sig figs). RH-agnostic / third soft detector after #38/#39; double-archimedean suppression slope $-(\pi/2)/\ln 10$. **2PR.1 (#44):** Bhatt-Lurie's WCart carries TWO operators -- the Frobenius $F$ ($\to$ finite Euler factors) and the Sen $\Theta$ (Hodge-Tate weights $\{-n\}$ $\to$ the archimedean $\Gamma$-factor DIVISOR via Lerch, ratio 1.0); both TRACES, neither contains the non-trivial zeros ($|\det_\infty(\rho-\Theta_{\mathrm{Sen}})|=4.39\mathrm{e}9\ne0$). Real-but-only-heuristic (spectral coincidence; supplies the divisor not $\Gamma_\mathbb{R}/\pi$), RH-agnostic. **Consolidated map** ([`docs/03_research/spec_z_cohomology_landscape.md`](docs/03_research/spec_z_cohomology_landscape.md)): a 15-candidate scorecard against the (i)-trace/(ii)-FE-duality/(iii)-polarization template. Every candidate realizes $\zeta$ as a TRACE; NONE carries the polarization (the universal gap $=$ RH $=$ 08A M4), bracketed by Faltings-Hriljac (proven, too local), AHK (proven signature, arithmetic-blind), de Branges (too strong). Verified 2024-2026 literature: Deninger's foliated space is now CONSTRUCTED (arXiv:1807.06400; corrects the dossier caveat), Petrov's Sen operator is NOT semisimple (Annals, arXiv:2302.11389; blocks eigenspace polarization), Connes-Consani's Feb-2026 Jacobian (arXiv:2602.15941) builds realization structure with no RH-positivity. |
| Lean 4 / Mathlib formalization | ✅ Phase 1 substrate green (2026-05-25). **Session 008: six sorry-free digamma identities in `ExplicitFormula.lean` (#EF-arch), all upstreamable to Mathlib (which has no `digamma`): recurrence $\psi(s+1)=\psi(s)+1/s$, reflection $\psi(1-s)-\psi(s)=\pi\cot\pi s$, iterated recurrence $\psi(s+n)=\psi(s)+\sum_{k<n}1/(s+k)$, duplication $\psi(2s)=\tfrac12(\psi(s)+\psi(s+\tfrac12))+\log 2$, and the special values $\psi(1)=-\gamma$ and $\psi(\tfrac12)=-\gamma-2\log 2$. The half-integer values are the arguments in $\zeta$'s archimedean kernel.** **Session 005: `ExplicitFormula.lean` — the Weil explicit formula + Weil positivity criterion scaffold (the highest-leverage target, LEARNINGS #17); prime side concrete via Mathlib `vonMangoldt`. Discharged #MB-1/#MB-2/#MB-6 (ζ pole, nonvanishing, functional equation) to real proofs, and proved the digamma recurrence $\psi(s+1)=\psi(s)+1/s$ (Mathlib has no digamma). Build green; project sorry count 26 → 23.** Full proof closure remains multi-year |
| Intuitive / undergraduate docs | 🔄 In progress |
| PDF text conversions | 🔄 In progress |
| manim visualizations | 🔄 In progress |

## Quick Start

```powershell
# Set up environment
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Smoke test the experimental framework
python -m experiments._shared.smoke_test

# manim scene
manim -pql visualizations/01_series_intro/series_intro.py ZetaSeriesIntro
```
