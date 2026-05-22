# Plan: Testing the Four RH Proof Architectures

> Companion to [`docs/solutions/README.md`](../docs/solutions/README.md) and the four-level framing in [`docs/02_graduate/log_correlated_fields_intro.md`](../docs/02_graduate/log_correlated_fields_intro.md) §6. This document is the test plan; the code lives in [`experiments/_shared/`](_shared/) plus per-architecture subdirectories.

## Current status (snapshot)

| Item | Status | Detail |
|---|---|---|
| Phase 0 shared infrastructure | ✅ | [`_shared/`](_shared/): LFunction interface, zeta, Davenport-Heilbronn, smoke test 5/5 |
| Arch 3A (zeta Li coefficients) | ✅ | Positivity confirmed for $n = 1, \ldots, 500$; truncation-limited at zero-sum |
| Arch 3B (D-H Li per-zero diagnostic) | ✅ | Central negative result: small-n Li positivity does NOT distinguish zeta from D-H |
| Arch 3C (Weil quadratic form + Gram) | ✅ | Wrong-approach detector witness: $M^{DH}$ has negative eigenvalues, $W_{DH}(\vec c) < 0 < W_\zeta(\vec c)$ |
| Arch 3D (witness scaling) | ✅ | Witness deepens with K, stable in T_max once first off-line zero is included |
| Arch 3B.2 (Li at large $n$ via off-line correction) | ✅ | Witnesses $\lambda_n^{DH} < 0$ at $n = 4 \times 10^5$ (off-line correction $-2.0 \times 10^7$ dwarfs asymptotic $+2.4 \times 10^6$) and $n = 10^6$ ($-3 \times 10^{18}$). Uses Bombieri-Lagarias asymptotic for on-line part + exact off-line correction; crossover predicted at $n \sim 320{,}000$, witnessed at $n = 400{,}000$. Sign oscillates with $|w_{\rm off}|^n$ amplitude. |
| Arch 3F (Weil-form duality, $\zeta$) | ✅ | Bombieri's explicit formula implemented and verified. Zero side = prime side to $<2\%$ at $T_{\max} = 1000$, $b \geq 14$. Decomposition: boundary $+144$, prime sum $-120$, constant $-19$, gamma $-5$ at $b=20$, cancelling to $W \sim 0.1$. Three orders of magnitude of cancellation — the analytic obstruction to RH lives here. |
| Arch 3G (Weil-form duality, D-H) | ✅ | D-H has no Euler product, so analog "prime sum" becomes a Dirichlet sum with oscillating coefficients $b_n^{DH}$ (recursion $\sum_{d \mid n} b_d c_{n/d} = c_n \log n$). Fourier-form gamma kernel with $\psi(3/4 + it/2)$. Zero side = prime side to sign + 10-30% at $T_{\max} = 200$. D-H components 100× smaller than $\zeta$'s; cancellation 100× looser. |
| Arch 3H (Weil-form duality, $\chi_3$) | ✅ | Refines 3G: tight cancellation is **not** a generic feature of Euler-product L-functions. It's specifically $\zeta$'s pole at $s=1$. $\chi_3$ (Euler product, no pole, GRH believed): mild cancellation $\sim 4\%$, intermediate between $\zeta$ ($0.1\%$) and D-H ($13\%$). Zero side = prime side to $<4\%$. |
| Arch 3I (unconditional Siegel-Walfisz bound for $\chi_3$) | ✅ | The "use $\chi_3$'s milder cancellation for unconditional proof" path is **blocked**. S-W bound on $|\psi(x, \chi_3)|$ applied via partial summation is too loose by 33× at $b=10$, 122× at $b=100$. Partial summation kills the cancellation. Same circularity wall as $\zeta$. |
| Arch 3E (Li / de Bruijn-Newman) | ⏳ | Pending; literature-and-analysis |
| Arch 1A (Berry-Keating discretization) | ✅ | All eigenvalues at $\Im E = -1/2$; density mismatch with zeta documented |
| Arch 1B (Sierra-Townsend) | ✅ | Three position-dependent corrections to $H_{BK}$ tested (centrifugal, Coulomb, modular log $x$). RMS vs first 50 $\gamma_n^\zeta$ stays $\sim 88$ across all variants. Modular form bends density but overshoots. Same H matrix predicts same spectrum for zeta and D-H comparison: L-function-agnostic by construction. |
| Arch 1C (operators on D-H) | ✅ | Best-affine fits of six 1A+1B spectra to first 40 $\gamma_n^\zeta$ and $\gamma_n^{DH}$: discrimination ratio $r := \mathrm{RMS}_\zeta / \mathrm{RMS}_{DH}$ spans $[0.50, 1.67]$, factor-3 spread, consistent with random alignment of similar-density sequences. No construction predicts off-line D-H gammas; the one apparent "match" (ST-C, min 0.11) is a spectral-density artifact. |
| Arch 1D (Connes literature) | ⏳ | Pending |
| Arch 4A (Vinogradov-Korobov) | ⏳ | Pending; literature |
| Arch 4B (non-negative trig polys) | ✅ | LP saturates Fejér bound $\cos(\pi/(n+2))$; classical $3+4\cos+\cos 2$ is sub-optimal at degree 2 |
| Arch 4C (conditional improvements) | ⏳ | Pending; literature |
| Arch 4D (new auxiliary inequalities) | ✅ | The d-variate LP for $\max c_{1, \ldots, 1}$ at uniform degree $(N, \ldots, N)$ saturates the tensor-product witness $P = Q(\theta_1)\cdots Q(\theta_d)$ where $Q$ is the 1D Fejér optimum. Confirmed at $d = 2$ (rank-1 coefficient matrix, exact to FP precision) and $d = 3$ (LP bracket contains tensor value at $N \leq 3$). The d-variate problem **decomposes** for single-coefficient objectives; no new inequality at this LP family. An earlier "factor-of-$2^d$ advantage" was a convention error. |
| Arch 4E (off-diagonal & balanced-sum LPs) | ✅ | Single-coefficient LPs decompose universally (Test A: max $c_{j,k}$ for any $(j,k)$ is rank-1 and matches asymmetric tensor product). **Balanced-diagonal-sum LP does NOT decompose:** max $c_{1,1} + c_{2,2}$ at bidegree $(N,N)$ exceeds the Cauchy-Schwarz tensor bound by **+12.1% at $N=2$** (LP = 2.562, tensor = 16/7 = 2.286), with full-rank optimal $c_{j,k}$ matrix. Improvement decays at higher $N$: 0.2%/1.4%/0.1% at $N = 3/4/5$. Off-diagonal-sum $c_{1,2}+c_{2,1}$ does NOT exceed tensor bound. **First genuinely 2D auxiliary inequality found in this thread.** |
| Arch 4E.2 (alpha sweep + extended diagonal) | ✅ | **Peak LP-vs-tensor gap is +25.00% at $\alpha = 3, N = 2$**, much larger than 4E's +12.1% at $\alpha = 1$. LP-optimal $P$ has clean rational coefficients ($c_{1,1} = 8/5, c_{2,2} = c_{0,2} = c_{2,0} = 4/5$) and genuine 2D structure ($\cos 2u, \cos 2v$ without tensor partners in $(u, v) = (\theta + \phi, \theta - \phi)$ coordinates). **3-term diagonal sum at $N = 3$ gives +1.98% (8.66x the 2-term gap)**. The non-decomposition is weight-sensitive and benefits from larger diagonal-sum objective families. |
| Arch 4E.3 (MT translation of 4E.2 gap) | ✅ | **The +25% C-S gap does NOT translate to an improved Mossinghoff-Trudgian zero-free region constant.** At the 4E.2 peak, best shape/$P(0)$ is **12.6x WORSE** than 1D Fejér at matched effective degree (3). Across $\alpha \in [0, 10]$, the BEST 2D polynomial (tensor product at $\alpha = 0$) gives ratio $0.958$ to 1D Fejér; no $\alpha$ exceeds the 1D bound. **Structural lemma:** any $P(\theta, \phi) \geq 0$ on $[0, 2\pi]^2$ restricted to a line gives a 1D non-neg trig poly, so 2D restriction CANNOT beat the 1D Fejér ceiling at matched degree. The C-S and MT figures of merit are structurally distinct. Improving the ZFR constant via 2D would require multi-zero coupling (Heath-Brown's AP / Siegel setup), constrained-domain LP, or polynomial-ideal SOS. |
| Arch 4E.4 (trivariate balanced-sum LP) | ✅ | **The LP-vs-tensor gap roughly DOUBLES from d=2 to d=3.** Trivariate LP $\max c_{1,1,1} + \alpha c_{2,2,2}$ at tridegree $(2, 2, 2)$ has peak gap **+51.29% at $\alpha = 3.25$** (M-corrected: in $[+50.0\%, +51.3\%]$), vs 4E.2's +25.00% at $\alpha = 3$. Peak LP value 5.09 vs symmetric tensor bound 3.36. The d-variate non-decomposition strengthens with dimension. Per 4E.3 structural lemma, this still does NOT improve the single-zero MT zero-free region constant. |
| Arch 4E.5 (d=4 balanced-sum LP) | ✅ | **The $(d-1) \times 25\%$ scaling pattern DOES NOT continue cleanly at d=4.** Quadvariate LP $\max c_{1,1,1,1} + \alpha c_{2,2,2,2}$ at quad-degree $(2,2,2,2)$ has peak at $\alpha = 4.5$ with gap interval **$[+54.5\%, +69.8\%]$** (M-converged at $M_{4D} = 35$, 1.5M constraints, $P_{\min} \sim -0.1$). Midpoint $\sim +62\%$, BELOW the $(d-1) \times 25\% = +75\%$ prediction. The peak $\alpha$ shifts upward: $3.0 \to 3.25 \to 4.5$ for $d = 2, 3, 4$. Increment per dimension: $\Delta_{2\to3} \approx 25$pp, $\Delta_{3\to4} \approx 15$pp — the gap grows SUB-LINEARLY in $d$, suggesting saturation at some limit below 100% as $d \to \infty$. |
| Arch 2A (Weil-proof diff table) | ✅ | [`2A_weil_proof_diff.md`](arithmetic_geometric/2A_weil_proof_diff.md): step-by-step diff between Weil's proof for curves over $\mathbb{F}_q$ (Lefschetz + Poincaré + Hodge index) and the missing structure over $\mathrm{Spec}(\mathbb{Z})$. **Conclusion: Architecture 2's obstruction is constructive, not analytic.** §4 expands: the analytic shadow (Arch 3's circularity wall) and the geometric obstruction are two views of the same missing positivity. §5 lists 17 specific constraints the missing mathematics must satisfy. Companion [`2A_candidate_evaluation.md`](arithmetic_geometric/2A_candidate_evaluation.md) operationalizes the constraints: checkable predicates, submission template, current scorecards for six candidates (Deitmar, Lorscheid, Borger, Connes, Deninger, Connes-Consani), kill criteria. **Universal finding from the scorecards: no candidate has even a partial ✅ on (xi-xiii) — Hodge index positivity provable without RH input. This is the central open construction problem.** |
| Arch 2A R1 (D-H exclusion sharpening) | ✅ | [`2A_R1_DH_exclusion.md`](arithmetic_geometric/2A_R1_DH_exclusion.md): per-candidate verification that D-H is excluded from each framework's natural domain. **All six candidates pass kill criterion K2 by construction.** The structural reason: D-H is defined by a linear combination of Dirichlet L-functions, which is an analytic operation on Dirichlet series rather than a geometric operation on the underlying objects. Linear combinations are not constructible within any of the six frameworks; therefore none of them accidentally "proves RH" for D-H. K2 safety is conditional on the Selberg conjecture (no Euler-product L-function with off-line zeros). Updates the (xvii) column in the scorecard from a mix of ⏳/🟡 to uniform ✅. |
| Arch 2A R2 (fiber product computation) | ✅ | [`2A_R2_fiber_product.md`](arithmetic_geometric/2A_R2_fiber_product.md): explicit computation of Spec(ℤ) ×_{𝔽₁} Spec(ℤ) in Borger's Λ-rings and Lorscheid's blueprints. **Borger** gives Spec(W(ℤ)) via the big Witt vector functor (right adjoint to forgetful U: Λ-Rings → Rings); W(ℤ) is isomorphic to 1 + tℤ[[t]] as multiplicative monoid, with Krull dimension 2 in truncated cases W_n(ℤ). **Lorscheid** gives the blueprint (ℤ × ℤ, doubled relations), which is 2-dimensional in Lorscheid's blueprint dimension theory. Both candidates **produce non-trivial 2-dim-ish surface objects**; constraint (ii) verdict upgrades to 🟡 for both. Companion dossiers [`2A_borger_dossier.md`](arithmetic_geometric/2A_borger_dossier.md) and [`2A_lorscheid_dossier.md`](arithmetic_geometric/2A_lorscheid_dossier.md) go deep on each framework: K-theory origins of Λ-rings, Tits-Weyl origins of blueprints, per-candidate strengths/limitations, per-constraint roadmaps. **Key insight from comparison**: Borger is strong on Frobenius (viii) but weak on surface (ii); Lorscheid is strong on surface (i-iii) but weak on Frobenius. |
| Arch 2A R2.5 (Λ-blueprints proposal) | 📋 proposed | [`2A_R2_5_lambda_blueprints.md`](arithmetic_geometric/2A_R2_5_lambda_blueprints.md): proposes a hybrid framework combining Borger's Adams operations with Lorscheid's blueprints. A **Λ-blueprint** is (B, B^•, {ψ_p}) where (B, B^•) is a blueprint and the ψ_p are commuting blueprint endomorphisms satisfying ψ_p(x) ≡ x^p modulo the appropriate blueprint relations. The category Λ-Blpr would have 𝔽₁ as initial object, ℤ as the canonical next level (with ψ_p = identity by Fermat's little theorem), and inherit both Λ-Rings and Blpr as subcategories. **Predicted scorecard if developed**: 8 ✅ / 4 🟡 / 5 ⏳ — substantial advance over either parent. The Hodge index slot (xi-xiii) remains universally open. **R2.5 is a research proposal, not established mathematics**: precise definitions, categorical properties, and fiber product computations need verification. Estimated effort: thesis-level project. |
| Arch 2A R3 (Connes-Consani K1 analysis) | ✅ | [`2A_R3_connes_positivity.md`](arithmetic_geometric/2A_R3_connes_positivity.md): per-conjecture analysis of whether Connes' (and Connes-Consani's) positivity conjectures are kill-criterion K1 (RH-equivalent) or independent. **C1 (Weil-Bombieri positivity, naive form)** fails K1: provably equivalent to RH. **C2 (Hamiltonian self-adjointness)** also fails K1: Hilbert-Pólya in Connes' setting. **C3 (arithmetic-site / hyperring refinements, post-2008)** is K1-uncertain: not provably equivalent, no independent proof. Scorecard update: Connes / Connes-Consani (xi)-(xiii) moves from ❌ to 🟡. **Cross-architecture concordance**: R3 aligns with Arch 3's 3F-3I finding — both confirm Weil positivity is hard to derive without RH-strength input. **The geometric route (Arch 2's intersection-theory Hodge index)** remains the only direction where positivity could emerge for free. Caveats: my reading of post-2014 Connes-Consani literature is partial; expert consultation would refine the analysis. |
| Arch 2A R3.5 (no-shortcut theorem for NCG) | ✅ | [`2A_R3_5_K1_universality.md`](arithmetic_geometric/2A_R3_5_K1_universality.md): proves that every trace-formula NCG framework with standard spectral identification has positivity P ⟺ RH. **Three positivity types covered**: self-adjointness (P-SA), quadratic form PSD (P-Q), operator non-negative eigenvalues (P-OP). **Proof**: the trace identity is reversible — given the spectral identification (F's spectrum = imaginary parts of ζ zeros), P forces RH AND RH forces P. **Consequence**: NCG-only approaches universally fail K1 by structure. **The unique escape route is geometric** — intersection theory + Hodge index theorem on a constructed surface provides positivity from the SIGNATURE of an intersection form, structurally different from trace-formula NCG positivity. Sharpens R3's verdict on C3 from 🟡 toward ❌. **Crystallizes the central insight**: constraints (xi)-(xiii) are not "another open problem" — they are specifically THE escape route through which any RH proof via Architecture 2 must go. The theorem is folklore in NCG circles; the contribution is making it explicit and tying it to the 17-constraint framework. |
| Arch 2A R3.6 (arithmetic-site C3 deep dive) | ✅ | [`2A_R3_6_arithmetic_site.md`](arithmetic_geometric/2A_R3_6_arithmetic_site.md): focused analysis of Connes-Consani's most aggressive refinements — the arithmetic site 𝒜 (a topos with hyperring-valued structure sheaf and Frobenius-like endomorphism Frob_ar), hyperrings (multivalued-addition algebras), and characteristic-one geometry (tropical / idempotent structures modeling the q → 1 limit). **Findings**: hosts at least four C3 formulations (C3a intersection-pairing, C3b étale cohomology spectral, C3c motivic, C3d sheaf-theoretic). All four either fit R3.5's hypothesis (P-SA / P-Q / P-OP) and fail K1, or aren't strong enough to imply RH alone. **Net effect**: Connes / Connes-Consani (xi)-(xiii) sharpened from 🟡 to ❌ in the summary scorecard. **Silver lining**: Connes-Consani's categorical machinery (topos, hyperrings) might serve as INFRASTRUCTURE for the geometric route even though it doesn't directly provide K1-escaping positivity. R3.6.3 queued as a follow-up. |
| Arch 2A R4 (Borger + Connes hybrid) | ✅ | [`2A_R4_borger_connes_hybrid.md`](arithmetic_geometric/2A_R4_borger_connes_hybrid.md): structural analysis of the natural hybrid combining Borger's Adams operations with Connes' adèle class space. **Bridge proposal**: U_t = ∏_p U_{log p}^{t/log p} — Borger's discrete ψ_p generates Connes' continuous ℝ*_+-action via the multiplicative completion. **Candidate Hilbert space**: H = L²(W(ℤ), μ) for an appropriate measure μ. **Predicted scorecard**: ~8 ✅ / 5 🟡 / 3 ❌ — similar to Λ-blueprints (R2.5) but with trace formula explicit rather than implicit. **K1 verdict**: fails K1 by R3.5 (inherits Connes' trace identity). **Value**: infrastructure for the geometric route — gives a concrete Hilbert space realization where Borger's surface side and Connes' trace formula side coexist. **Five open technical questions** (R4.1-R4.5): right measure μ, multiplicative completion convergence, Connes-side isomorphism, trace formula recovery, cohomology development. **Status**: research proposal, not published — no known explicit Borger + Connes hybrid in the literature. |
| Arch 2A R5 (prismatic cohomology) | ✅ | [`2A_R5_prismatic_cohomology.md`](arithmetic_geometric/2A_R5_prismatic_cohomology.md): investigates Bhatt-Morrow-Scholze prismatic cohomology (2018-) as the cohomology theory for Spec(W(ℤ)) in Borger's framework. **Connection**: δ-rings (the foundation of prismatic cohomology) are essentially "Λ-rings at one prime p" — Borger's Λ-structure on W(ℤ) gives δ-structures at every prime. So prismatic cohomology naturally applies. **Predicted impact**: closes constraints (iv)-(vii) (finite cohomology, Poincaré duality, cycle class map, Künneth) in one move for Borger's framework. **K1 status**: still fails (prismatic cohomology adds a trace formula structure that falls under R3.5's hypothesis). **Value**: infrastructure progress, not K1 escape. **Five open R5 questions** for verification. |
| Arch 2A path forward synthesis | 📋 strategic | [`2A_path_forward.md`](arithmetic_geometric/2A_path_forward.md): synthesis of R1-R5 into a strategic plan. **Develop BOTH hybrid candidates** (Λ-blueprints / Borger + Connes) **in parallel**; use prismatic cohomology for both; attack Hodge index on whichever track reaches it first. **5-10 year multi-paper research program**, success probability < 50%. Project-level vs beyond-project work distinguished. **Final conclusion**: Architecture 2 is the right place to look for an RH proof (per R3.5), but the construction problem is hard enough that even existing categorical machinery doesn't close it. New mathematics needed along the hybrid + geometric lines identified. |
| Arch 2B (worked example, E/F_5) | ✅ | $\alpha = -1.5 \pm i\sqrt{11}/2$, $|\alpha|^2 = 5$; point counts match Weil formula at $k = 1, \ldots, 6$ |
| Arch 2C (F_1 / Arakelov survey) | ⏳ | Pending; literature |
| Arch 2D (Deninger micro-target) | ⏳ | Pending |
| Cross-cut: Selberg-class comparison | ✅ | Fixed K: $M^{\chi_3}$ PSD (min eig $+1.08\times 10^{-2}$); same witness gives $W_{DH}(c^*) < 0 < W_\zeta(c^*), W_{\chi_3}(c^*)$. K scaling: $\chi_3, \chi_4$ PSD across $K \in [10, 100]$ (redundancy pattern), D-H deepens monotonically to $-3.7\times 10^{-1}$. |
| Arch 3D.3 (K-scaling extended to K=1000) | ✅ | **The detector signal saturates structurally.** Across $K \in [100, 1000]$: D-H's relative min eigenvalue converges to a constant $\boldsymbol{-2.62\%}$ (asymptotic, dimension-independent). **Negative eigenvalue count is FIXED at $4$** = number of off-line zero pairs (8 off-line zeros forming 4 conjugate pairs in UHP). Each off-line pair contributes exactly 1 negative eigenvalue. Selberg-class L-functions ($\zeta, \chi_3, \chi_4$) stay PSD to floating-point noise at $K = 1000$. The detector is effectively counting off-line zero pairs via its eigenvalue spectrum. Closes LEARNINGS open #5. |
| Arch 3D.4 (T_max scaling) | ✅ | **Validates the structural prediction $n_{\rm neg}$ = # off-line $\gamma$'s in UHP up to $T_{\max}$.** Three data points: $T_{\max} = 200$ (4 off-$\gamma$'s → 4 neg eigs), $T_{\max} = 300$ (5 → 5, new pair at $\gamma \approx 240.4$), **$T_{\max} = 350$ (7 → 7, non-trivial double increment, new pairs at $\gamma \approx 320.9, 331.0$)**. Relative min eigenvalue identical to 4 sig figs across all three: $-2.599 \times 10^{-2}$. Selberg-class L-functions stay PSD at all $T_{\max}$. **The detector is structurally counting off-line zero pairs** with universal per-pair signal strength. Strongest validation of the wrong-approach detector's architectural picture. |

---

## Premise

We cannot test "does this approach prove RH". We can test the **intermediate claims** each architecture must produce, and we can build **kill criteria** that would falsify the approach. Two non-negotiable disciplines:

1. **Positivity, not just spectral match.** A method that derives only from log-correlated structure, Selberg CLT, GUE statistics, or moments lives at Level 3 and is provably insufficient: those statements are compatible with worlds where RH fails for a single zero at $\beta = 0.51$.
2. **The Davenport-Heilbronn discipline.** Any architecture-1, -3, or -4 method must distinguish $\zeta$ from Davenport-Heilbronn (functional equation, no Euler product, known off-line zeros). Anything that "proves RH" for D-H is wrong.

The four architectures from `docs/solutions/README.md` §8, with concrete test programs below.

---

## Phase 0: Shared infrastructure

Before any architecture-specific work, everything depends on:

1. **Zero data pipeline.** mpmath-derived $\zeta$ zeros at 30+ digit precision, with disk caching; downloads of Odlyzko's high-precision tables for zeros up to height $10^{22}$; LMFDB low-lying zeros for selected L-functions. Uniform API: `LFunction.zeros(T_max, prec)`.
2. **Control L-functions.**
   - **Davenport-Heilbronn** (1936): functional equation, no Euler product, off-line zeros known. The "wrong-approach detector".
   - Selected Dirichlet L-functions for $\chi$ mod small $q$ (Euler product + functional equation, GRH believed).
   - A "fake" Selberg-class object built by hand (Euler product but contrived functional equation) for sanity testing.
3. **Precision pipeline.** mpmath at $\geq 50$ digits, validated against known constants.

Deliverable: [`experiments/_shared/`](_shared/) with documented API.

---

## Architecture 1: Spectral (Hilbert-Pólya)

**Object to test:** does any candidate operator reproduce the zero spectrum *and* fail on D-H (proving it's using something arithmetic)?

| ID | Experiment | Kill criterion |
|---|---|---|
| 1A | Numerical Berry-Keating: discretize $H = xp + px$ on various domains and boundary conditions; compare spectral density to $\tfrac{1}{2\pi}\log(T/2\pi)$ | No boundary condition matches density at scale $\Rightarrow$ heuristic does not survive discretization |
| 1B | Sierra-Townsend hyperbolic-half-plane model: reproduce reported low-eigenvalue match against first 100 zeros | Reproduction fails $\Rightarrow$ this line is weaker than claimed |
| 1C | Same construction applied to D-H; confirm it does *not* spuriously give D-H "on-line" zeros | A candidate $H$ that would predict on-line zeros for D-H is structurally insufficient |
| 1D | Literature: Connes adele-class space. Pin down the smallest missing positivity claim and a toy version we could probe | None (literature) |

**Where a proof would come from:** a self-adjointness theorem with verified domain. Numerical 1A-1C give confidence or rule a candidate out.

---

## Architecture 2: Arithmetic-geometric (Deninger, $\mathbb{F}_1$)

Mostly literature and notation; the proof is a construction. Preparatory work:

| ID | Task | Output |
|---|---|---|
| 2A | Read the Weil proof for curves over $\mathbb{F}_q$ in full detail. Identify each step's analogue (or missing analogue) over $\mathbb{Z}$ | A "diff table": what Weil uses vs what we have over $\mathbb{Z}$, with the gap highlighted |
| 2B | Worked example: a genus-1 curve over $\mathbb{F}_5$. Compute its zeta, its zeros, verify Weil bound. Make the cohomology explicit | Reference notebook other architectures can compare against |
| 2C | Survey state of $\mathbb{F}_1$ and Arakelov-cohomology programs as of 2025 | Status document in `docs/03_research/` |
| 2D | Identify the smallest open conjecture in Deninger's program that would, if proved, be a meaningful step | A target |

**Where a proof would come from:** the missing cohomology construction. We probably can't construct it here, but we can clarify the target.

---

## Architecture 3: Direct positivity (Weil / Li)

**Most computationally tractable architecture.**

| ID | Experiment | Kill criterion |
|---|---|---|
| 3A | Compute Li coefficients $\lambda_n = \sum_\rho \big(1 - (1 - 1/\rho)^n\big)$ for $n = 1, \ldots, 10^4$ at $\geq 30$-digit precision. Check positivity. Fit asymptotic $\lambda_n \sim \tfrac{n}{2}\log n + cn + \ldots$ | A reproducibly negative $\lambda_n$ would refute RH (will not happen). An anomalous growth pattern shapes conjectures |
| 3B | Same for Davenport-Heilbronn. **Expect** $\lambda_n$ to go negative at some computable $n$. Establish where | Positive control: if our setup cannot see D-H going negative, it is broken |
| 3C | Weil quadratic form $Q(f) = \sum_\rho \hat f(\rho)\overline{\hat f(\bar\rho)}$ on parameterized test-function families; track minimum eigenvalue | $Q(f) < 0$ would refute RH. Quantifies how close to zero the minimum gets |
| 3D | ML / gradient-based search for adversarial $f$ minimizing $Q(f)$ over a neural-net-parameterized Schwartz space | Adversarial $f$ found with $Q(f) < 0$ $\Rightarrow$ refutes RH. Tight $Q \geq \varepsilon > 0$ on a wide family $\Rightarrow$ progress |
| 3E | Bombieri-Lagarias structure: relation between Li coefficients and the de Bruijn-Newman constant | Sharpens what positive results would mean |

**Where a proof would come from:** an analytic argument showing $\lambda_n \geq 0$ uniformly, or $Q(f) \geq 0$ on a dense subspace.

---

## Architecture 4: Analytic (zero-free regions)

| ID | Experiment | Kill criterion |
|---|---|---|
| 4A | Reproduce Vinogradov-Korobov; identify where the $2/3$ exponent appears. Probe with numerical exponential sums | Confirms literature; localizes the bottleneck |
| 4B | Non-negative trigonometric polynomial search: $\sum c_k \cos(k\theta) \geq 0$ with $c_0 > 0$ and $c_1$ as large as possible. Improves zero-free-region constants | A better polynomial at small degree shifts constants. Does not break the exponent but is a clean micro-target |
| 4C | Literature: Heath-Brown, Pintz, Ford on conditional improvements; identify which conditional results, unconditionalized, would push the exponent | Map the conditional landscape |
| 4D | Numerical search for "auxiliary inequalities" beyond non-negative trig polynomials: multivariate, weighted, non-classical test functions | A structurally new inequality becomes an active program |

**Where a proof would come from:** a new auxiliary inequality replacing $3 + 4\cos\theta + \cos 2\theta \geq 0$.

---

## Cross-cutting

- **Selberg class as test bed.** Every "Euler product + functional equation gives positivity" claim should be tested across Selberg-class members. Claims that distinguish $\zeta$ from a generic Selberg L-function are the ones with proof potential. Status: positive control via $\chi_3$ now in place ([`e3c3_selberg_cross_cut.py`](positivity/e3c3_selberg_cross_cut.py)): the Gram-matrix detector returns PSD for $\zeta$ and $\chi_3$, indefinite only for D-H.
- **D-H unit test.** Codify "this method does not falsely confirm RH for Davenport-Heilbronn" as an explicit unit test in `experiments/_shared/tests/`.
- **Atlas integration.** Each architecture gets a status row in [`docs/research_atlas/README.md`](../docs/research_atlas/README.md), updated as work proceeds.

---

## Execution order

1. **Phase 0 (shared infrastructure)** — prerequisite for everything.
2. **Architecture 3 (positivity)** — most computationally tractable; immediately produces verifiable artifacts (Li coefficients, Weil form). Highest learning rate per unit effort.
3. **Architecture 1 (spectral)** — rich numerical playground; partial machinery already from multifractal work.
4. **Architecture 4 (zero-free)** — sharp computational micro-target (trig polynomials), small but well-defined.
5. **Architecture 2 (arithmetic-geometric)** — mostly literature, longest arc. Save for when other work has clarified what we need.

Per-architecture work lives in `experiments/positivity/`, `experiments/spectral/`, `experiments/zero_free/`, `experiments/arithmetic_geometric/`. The task list is tracked in this repo's TODO and the harness's todo state.
