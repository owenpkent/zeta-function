# Mapping the recent Riemann-Hypothesis literature (2021–2026)

*A structured map of recent arXiv work on the Riemann zeta function and the Riemann Hypothesis, organized around the candidate proof architectures your repo is built to test. Built from **303 arXiv papers** (2021–Jul 2026) retrieved through the scholarly-literature connector, deduplicated and triaged; 279 in the six research threads below, with 24 `math.GM` items segregated as unrefereed/claimed-proof.*

![Overview: RH literature by thread and over time]({{artifact:f752dec3-37f8-4d19-9a0a-cdfc2d08716a}})

## The one-paragraph picture

Two developments dominate the period. First, in the **empirical/analytic** direction, the **Guth–Maynard large-value estimate for Dirichlet polynomials** (2024) is the most consequential single result — the first improvement to the Ingham-type zero-density exponent in decades, feeding directly into primes-in-short-intervals and the density hypothesis. It has pulled a whole cluster of zero-density and large-value work behind it. Second, in the **structural/spectral** direction, **Alain Connes and collaborators** have kept the noncommutative-geometry / Weil-positivity program in continuous motion (prolate operator, zeta-cycles, heat expansion, and a 2026 commissioned RH survey). These are the two poles of the current field: sharpen the quantitative bounds vs. build the spectral object. Between them, **random-matrix theory & moments** remains the largest thread by volume (a mature "recipe" for predicting zeta statistics), while **log-correlated / extreme-value** work — though smaller — is where a genuine conjecture-to-theorem transition happened (the Fyodorov–Hiary–Keating maximum).

## Thread sizes (2021–2026, excl. `math.GM`)

| Thread | Papers |
|---|---|
| B — Random matrix theory & moments | 71 |
| F — General RH / critical line / large values | 59 |
| E — Zeros: density, zero-free regions, pair correlation | 57 |
| A — Spectral / Hilbert–Pólya / operator | 53 |
| D — Positivity & explicit-formula criteria | 22 |
| C — Log-correlated fields / extreme values | 17 |

---

## Thread B — Random matrix theory & moments  (71 papers)

The largest thread. A mature machinery (Keating–Snaith / CFKRS 'recipe') predicts moments and value distributions of ζ from characteristic polynomials of random unitary matrices; recent work pushes toward *proving* the predictions and extending them to families of L-functions.

**Trend, 2021–2026:** The dominant trend is the maturation of a rigorous random-matrix "recipe" (Keating–Conrey/Baluyot–Conrey) for predicting and proving sharp moment asymptotics and bounds for zeta and its derivatives.

**Notable recent papers:**

- **Twisted moments of characteristic polynomials of random matrices in the unitary group** — Baluyot, Conrey (2025-03, [2503.21682](https://arxiv.org/abs/2503.21682))  
  Baluyot–Conrey give a rigorous random matrix analogue of the Keating–Conrey moment recipe, a major structural advance.
- **Moments of zeta and correlations of divisor-sums: stratification and Vandermonde integrals** — Baluyot, Conrey (2022-06, [2206.04821](https://arxiv.org/abs/2206.04821))  
  Introduces Vandermonde/Rodgers–Soundararajan-style integral expression underpinning the moment conjectures program.
- **Exchangeable arrays and integrable systems for characteristic polynomials of random matrices** — Assiotis, Gunes, Keating, Wei (2024-07, [2407.19233](https://arxiv.org/abs/2407.19233))  
  Fully settles moments of derivatives/real characteristic polynomials via exchangeable arrays, resolving a 25-year problem.
- **Negative moments of the Riemann zeta-function** — Bui, Florea (2023-02, [2302.07226](https://arxiv.org/abs/2302.07226))  
  Bui–Florea establish negative moments of zeta, a genuinely new and technically hard direction under RH.
- **Sharp bounds for joint moments of the Riemann zeta function** — Curran, Heycock (2024-03, [2403.00902](https://arxiv.org/abs/2403.00902))  
  Curran–Heycock extend sharp joint moment bounds unconditionally across the full conjectured range, key benchmark result.
- **A survey of moment bounds for $ζ(s)$: from Heath Brown's work to the present** — Florea (2025-09, [2509.20335](https://arxiv.org/abs/2509.20335))  
  Florea's survey synthesizes Heath-Brown's legacy and the current moment-bounds landscape, valuable field overview.
- **Lower bounds for the large deviations and moments of the Riemann zeta function on the critical line** — Arguin, Creighton (2026-03, [2603.01711](https://arxiv.org/abs/2603.01711))  
  Arguin–Creighton give unconditional large-deviation/moment lower bounds on the critical line advancing the log-correlated program.
- **Amplified moments of the Riemann zeta function** — Durkan, Page (2026-06, [2606.27323](https://arxiv.org/abs/2606.27323))  
  Amplified moments yield unconditional sixth-moment lower bounds matching Keating–Snaith predictions, a strong new advance.
- **Currently there are no reasons to doubt the Riemann Hypothesis: The zeta function beyond the realm of computation** — Farmer (2022-11, [2211.11671](https://arxiv.org/abs/2211.11671))  
  Farmer's widely-discussed rebuttal of RH-doubting arguments, blending RMT evidence, shapes community consensus.
- **Bulk asymptotics of the Gaussian $β$-ensemble characteristic polynomial** — Lambert, Paquette (2025-08, [2508.01458](https://arxiv.org/abs/2508.01458))  
  Lambert–Paquette's rigorous bulk asymptotics of Gβε characteristic polynomials deepen the RMT-zeta analogy foundations.


## Thread E — Zeros: computation, density, zero-free regions  (57 papers)

The quantitative backbone: how many zeros lie off the line (zero-density), how close to Re(s)=1 they can be (zero-free regions), and how they correlate (pair correlation). **This is where Guth–Maynard landed**, and it triggered a wave of explicit re-optimizations.

**Trend, 2021–2026:** Recent arXiv work advances zero-free regions, zero-density estimates, and pair correlation theory for zeta/L-functions through explicit bounds, large-value estimates, and Fourier-analytic techniques.

**Notable recent papers:**

- **New large value estimates for Dirichlet polynomials** — Guth, Maynard (2024-05, [2405.20552](https://arxiv.org/abs/2405.20552))  
  Guth–Maynard breakthrough large-value estimates for Dirichlet polynomials, major input to zero-density theory.
- **Half-isolated zeros and zero-density estimates** — Maynard, Pratt (2022-06, [2206.11729](https://arxiv.org/abs/2206.11729))  
  Maynard–Pratt introduce half-isolated zeros method improving classical Ingham–Huxley zero-density estimate.
- **New exponent pairs, zero density estimates, and zero additive energy estimates: a systematic approach** — Tao, Trudgian, Yang (2025-01, [2501.16779](https://arxiv.org/abs/2501.16779))  
  Tao–Trudgian–Yang systematic exponent pairs and zero-density estimates via new ANTEDB database.
- **Explicit zero-free regions for the Riemann zeta-function** — Mossinghoff, Trudgian, Yang (2022-12, [2212.06867](https://arxiv.org/abs/2212.06867))  
  Mossinghoff–Trudgian–Yang give widely-cited explicit zero-free region improvements for zeta.
- **Zero-free regions inspired by work of Heath-Brown** — Bellotti, Trudgian, Yang (2026-03, [2603.21490](https://arxiv.org/abs/2603.21490))  
  Bellotti–Trudgian–Yang extend Heath-Brown's Linnik-constant ideas to sharpen explicit zero-free region.
- **Zeta Zeros on the Critical Line** — Goldston, Suriajaya (2025-11, [2511.20059](https://arxiv.org/abs/2511.20059))  
  Goldston–Suriajaya survey fifty years of pair correlation method and its applications.
- **Fourier optimization and Montgomery's pair correlation conjecture** — Carneiro, Milinovich, Ramos (2023-10, [2310.01913](https://arxiv.org/abs/2310.01913))  
  Carneiro–Milinovich–Ramos apply Fourier optimization framework to sharpen Montgomery's pair correlation bounds.
- **An unconditional Montgomery Theorem for Pair Correlation of Zeros of the Riemann Zeta Function** — Baluyot, Goldston, Suriajaya, Turnage-Butterbaugh (2023-06, [2306.04799](https://arxiv.org/abs/2306.04799)) · *published*  
  Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh prove unconditional analogue of Montgomery's pair correlation theorem.


## Thread A — Spectral / Hilbert–Pólya / operator  (53 papers)

The Hilbert–Pólya dream — realize the zeros as the spectrum of a self-adjoint operator. In this period it is essentially **Connes' noncommutative-geometry program** plus the **Berry–Keating** semiclassical strand, with careful reviews clarifying what is and isn't rigorous.

**Trend, 2021–2026:** Recent arXiv work continues probing Hilbert–Pólya-style operator/spectral realizations of Riemann zeros, dominated by Connes and collaborators' noncommutative-geometric program alongside rigorous transfer-operator and L-function spectral analysis.

**Notable recent papers:**

- **The Riemann Hypothesis: Past, Present and a Letter Through Time** — Connes (2026-02, [2602.04022](https://arxiv.org/abs/2602.04022))  
  Connes' major survey of RH history plus new spectral/operator perspective from a leading researcher.
- **Prolate spheroidal operator and Zeta** — Connes, Moscovici (2021-12, [2112.05500](https://arxiv.org/abs/2112.05500))  
  Connes-Moscovici uncover new spectral property of prolate spheroidal operator tied to zeta.
- **Spectral Triples and Zeta-Cycles** — Connes, Consani (2021-06, [2106.01715](https://arxiv.org/abs/2106.01715))  
  Connes-Consani exhibit eigenvalues of Weil explicit-formula quadratic form via zeta-cycles.
- **Heat Expansion and Zeta** — Connes (2024-02, [2402.13082](https://arxiv.org/abs/2402.13082))  
  Connes computes full heat-kernel trace expansion for the conjectural RH self-adjoint operator.
- **Knots, primes and class field theory** — Connes, Consani (2025-01, [2501.06560](https://arxiv.org/abs/2501.06560))  
  Connes-Consani extend adelic/class field theory framework underlying spectral realization of L-function zeros.
- **Hilbert spaces and low-lying zeros of L-functions** — Carneiro, Chirre, Milinovich (2021-09, [2109.10844](https://arxiv.org/abs/2109.10844))  
  Carneiro-Chirre-Milinovich unify Fourier optimization for low-lying zero density, rigorous analytic number theory.
- **On the Ruelle-Mayer Transfer Operators for Hölder Continuous Functions** — Baumgartner (2025-11, [2511.06513](https://arxiv.org/abs/2511.06513))  
  Baumgartner extends Ruelle-Mayer transfer operator spectral theory linked to Maass forms and zeta zeros.
- **On the Berry-Keating Operator** — Bagarello, Kużel (2026-06, [2606.24405](https://arxiv.org/abs/2606.24405))  
  Careful review clarifying rigorous status of the Berry-Keating operator's connection to RH.
- **High-Precision Approximation of Riemann Zeros via the Truncated Weil Form** — Groskin (2026-05, [2605.20224](https://arxiv.org/abs/2605.20224))  
  Numerical study testing convergence of Connes-van Suijlekom truncated Weil form zeros to Riemann zeros.


## Thread C — Log-correlated fields / extreme values  (17 papers)

Smallest but conceptually sharp: model log|ζ| on the critical line as a **log-correlated field**. This is the thread where a physics conjecture (Fyodorov–Hiary–Keating, on the maximum of ζ in short intervals) became rigorous theorem via branching-random-walk / multiplicative-chaos technology.

**Trend, 2021–2026:** The period is defined by the rigorous proof (via Arguin–Bourgade–Radziwiłł and related work) that the maximum of zeta on short intervals matches the Fyodorov–Hiary–Keating log-correlated/random-matrix prediction, with subsequent work extending this multiplicative-chaos framework to mesoscopic scales, moments of moments, and other L-functions.

**Notable recent papers:**

- **The Fyodorov-Hiary-Keating Conjecture. II** — Arguin, Bourgade, Radziwiłł (2023-07, [2307.00982](https://arxiv.org/abs/2307.00982))  
  Completes the FHK conjecture lower bound, establishing tightness of zeta's maximum on short intervals—a landmark result in the field.
- **Maxima of a Random Model of the Riemann Zeta Function over Intervals of Varying Length** — Arguin, Dubach, Hartung (2021-03, [2103.04817](https://arxiv.org/abs/2103.04817))  
  Introduces the foundational random model interpolating log-correlated and IID extreme-value regimes, seeding much subsequent work.
- **The Fyodorov--Hiary--Keating Conjecture on Mesoscopic Intervals** — Arguin, Hamdan (2024-05, [2405.06474](https://arxiv.org/abs/2405.06474))  
  Extends FHK-type sharp bounds to mesoscopic intervals, advancing the program beyond the original fixed-length regime.
- **Maxima of log-correlated fields: some recent developments** — Bailey, Keating (2021-06, [2106.15141](https://arxiv.org/abs/2106.15141))  
  Authoritative survey synthesizing log-correlated field theory and its connections to zeta/L-function extreme values.
- **Large Deviation Estimates of Selberg's Central Limit Theorem and Applications** — Arguin, Bailey (2022-02, [2202.06799](https://arxiv.org/abs/2202.06799))  
  Sharp unconditional large-deviation bound for Selberg's CLT, improving Soundararajan/Harper and feeding into maximum estimates.
- **Freezing transition and moments of moments of the Riemann zeta function** — Curran (2023-01, [2301.10634](https://arxiv.org/abs/2301.10634))  
  Establishes the freezing transition for moments of moments of zeta, confirming Fyodorov-Keating predictions rigorously.
- **A model problem for multiplicative chaos in number theory** — Soundararajan, Zaman (2021-08, [2108.07264](https://arxiv.org/abs/2108.07264)) · *published*  
  Soundararajan-Zaman model problem links random multiplicative functions to multiplicative chaos, clarifying the probabilistic mechanism behind FHK-type phenomena.
- **A dichotomy for extreme values of zeta and Dirichlet L-functions** — Bondarenko, Darbar, Hagen, Heap et al. (2023-02, [2302.08285](https://arxiv.org/abs/2302.08285)) · *published*  
  Establishes a dichotomy linking Dedekind zeta large values to improved zeta maxima bounds, connecting distinct extreme-value programs.
- **Dirichlet $L$-functions on the critical line and multiplicative chaos** — Vihko (2025-06, [2506.16115](https://arxiv.org/abs/2506.16115))  
  Proves convergence of random Dirichlet L-functions to Gaussian multiplicative chaos, extending the log-correlated framework beyond zeta itself.


## Thread D — Positivity & explicit-formula criteria  (22 papers)

RH restated as a positivity statement — Li's criterion, Weil's explicit-formula positivity, the de Bruijn–Newman constant Λ, Nyman–Beurling. Steady rather than explosive; the interest is in extending criteria to general L-functions and to explicit/quantitative forms.

**Notable recent papers:**

- **On the Pólya Frequency Order of the de Bruijn Newman Kernel. Certified Failure at Order Five and the Toeplitz Threshold Phenomenon** — Michałowski (2026-02, [2602.20313](https://arxiv.org/abs/2602.20313))  
  Rigorous computational disproof that the de Bruijn–Newman kernel is PF5, refining structural understanding of the Λ constant program.
- **Note on the positivity of the real part of the log-derivative of the Riemann $ξ$-function near the critical line** — Grigutis, Turčinskas (2025-09, [2509.18963](https://arxiv.org/abs/2509.18963))  
  Establishes explicit positivity bounds for the log-derivative of ξ near the critical line, refining zero-free region heuristics.
- **Equivalent criteria for the Riemann hypothesis for a general class of $L$-functions** — Garg, Maji (2024-09, [2409.17708](https://arxiv.org/abs/2409.17708))  
  Extends Riesz/Hardy-Littlewood-type equivalent criteria for RH to a general class of L-functions, broadening the positivity-criterion framework.
- **An explicit formula for the zeros of the Riemann zeta function** — Balanzario, Romero (2023-11, [2312.00108](https://arxiv.org/abs/2312.00108))  
  Gives an explicit Hermite-weighted formula linking zeta zeros directly to primes, a genuine explicit-formula advance.
- **A smooth version of Landaus explicit formula** — Balanzario, Romero, Serna (2023-11, [2311.04347](https://arxiv.org/abs/2311.04347))  
  Produces a smoothed Landau explicit formula and links zero-location resolution to prime detection via an uncertainty-principle argument.
- **A Prime Power Equation** — Redmond, Ryavec (2022-09, [2209.10522](https://arxiv.org/abs/2209.10522))  
  Constructs an entire Fourier-transform function vanishing at zeta zeros, yielding a zero-free prime power ident


## Thread F — General RH / critical line / large values  (59 papers)

The connective tissue — critical-line zero-proportion (Levinson/Conrey method), subconvexity, and the **large-values problem** that Guth's survey reframes as a shared object across number theory, harmonic analysis, and CS.

**Notable recent papers:**

- **Pair Correlation of Zeros of the Riemann Zeta Function I: Proportions of Simple Zeros and Critical Zeros** — Baluyot, Goldston, Suriajaya, Turnage-Butterbaugh (2025-01, [2501.14545](https://arxiv.org/abs/2501.14545))  
  Extends Montgomery's pair correlation method to new horizontal-distribution results on zeta zeros, by leading researchers in the area.
- **Zeta Zeros in a Narrow Vertical Box** — Goldston, Suriajaya (2026-03, [2603.28104](https://arxiv.org/abs/2603.28104))  
  Companion advance replacing RH with an explicit double-sum estimate to control simple critical-line zeros.
- **Short mollifiers of the Riemann zeta-function** — Conrey, Farmer, Kwan, Lin et al. (2025-08, [2508.11108](https://arxiv.org/abs/2508.11108))  
  Conrey-Farmer et al. improve Levinson's method via calculus of variations, strengthening critical-line zero-proportion results.
- **Large value estimates in number theory, harmonic analysis, and computer science** — Guth (2025-03, [2503.07410](https://arxiv.org/abs/2503.07410))  
  Guth's survey unifies large value problems across analytic number theory, harmonic analysis, and CS, framing open directions.

---

## Cross-cutting observations

1. **The field's center of gravity in 2024–2025 shifted toward zero-density and large values**, driven by Guth–Maynard and the subsequent explicit re-optimizations (Tao–Trudgian–Yang's exponent-pair database, Bellotti–Trudgian–Yang zero-free regions, Maynard–Pratt half-isolated zeros). If you are tracking "movement," this is the live front.

2. **The spectral/Connes program is the most active *structural* attack** but proceeds by building machinery (operators, trace formulas, cyclic homology) rather than closing bounds — a different tempo from thread E.

3. **RMT/moments (thread B) is the largest by volume but the most incremental** — a well-understood recipe being applied to ever more families; the open frontier is *proving* the moment conjectures unconditionally, not predicting them.

4. **Log-correlated/extreme-value work (thread C) is small but high-yield** — the FHK maximum conjecture moving to theorem is arguably the cleanest conjecture→proof story of the decade in this area, even though it does not attack RH directly.

5. **24 `math.GM` submissions** claiming elementary proofs/disproofs were filtered out. They are catalogued in the corpus CSV (`flagged_math_GM=True`) but excluded from the analysis; none carry journal references or recognized-author signals.

## Method & caveats

- **Source:** arXiv metadata via the scholarly-literature connector, 22 architecture-targeted queries + 6 follow-ups, window 2021-01-01 → 2026-07 (2026 is partial). 342 raw hits → 303 after removing Riemannian-geometry / Riemann-solver false positives → 279 in-thread.
- **Thread assignment** is by keyword scoring on title+abstract (a paper can touch several threads; it is filed under its dominant one). **Landmark selection** is an LLM curation pass (reasoning model) over each thread's full list, prioritizing recognized researchers, program-advancing results, and surveys.
- **Citation weighting was not applied:** OpenAlex requires an API key that isn't configured in this workspace, so I could not rank by citation impact — the "notable" calls rest on venue/publication status, author recognition, and abstract content. Adding an OpenAlex key (Customize → Credentials) would let me re-rank the whole corpus by citation velocity.
- **Full data:** `rh_full_corpus.csv` (all 303, with thread, category, publication status, GM flag) and `rh_selected_papers.csv` (the 46 highlighted here).
