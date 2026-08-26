# WATCH sweep: arXiv 2026-07-18 through 2026-08-26

> SURVEYOR reading note. Executes the overdue WATCH cadence item: last full graded sweep
> 2026-07-18 ([`watch_sweep_2026-07-18.md`](watch_sweep_2026-07-18.md)), cadence due ~2026-08-01.
> Trigger: the frame audit's decay finding ([`sp_backlog_frame_audit.md`](../sp_backlog_frame_audit.md),
> LEARNINGS #201, Appendix B): the WATCH graded sweep was the portfolio's HIGH stale-risk item at
> 24 days overdue, "the inventory's one unbounded cost (a missed R1 event)," and session 1 of the
> audit's adopted order is "hygiene + the overdue WATCH graded sweep." Partial mitigation
> acknowledged: the `lit_watch` watcher ran 2026-08-20 at listing level (22 tracked papers, 7
> keyword windows) but graded nothing; its in-window harvest (two arXiv IDs under "Weil explicit
> formula") is part of this sweep's corpus and is graded below. A --check re-run 2026-08-26 00:38
> UTC confirmed the baseline (22 tracked papers unchanged, no new keyword listings). Grading
> convention verbatim from the 303-paper corpus build
> ([`rh_corpus_2021-2026_vs_frontier.md`](rh_corpus_2021-2026_vs_frontier.md), LEARNINGS #155):
> grades NEW-LOAD-BEARING / CANDIDATE / KNOWN-TO-REPO / ADJACENT-WATCH / OFF-TARGET /
> LEVEL-3-MIRROR. Screens: the four analytic shapes of the R1 WATCH slot
> ([`sourcing_gap_r1.md`](../sourcing_gap_r1.md): (i) a variety-free purity/Ramanujan theorem;
> (ii) unconditional power-saving bilinear Mobius/von Mangoldt cancellation near $\sqrt x$ for a
> non-algebraic sequence without finite-field geometry; (iii) a determinant-class trace formula
> for $\zeta$ with an independently computable pole budget; (iv) a $\lambda$-uniform
> operator-theoretic one-sided upper-bound mechanism on a determinant-class carrier, the
> S4/Stepanov shape), plus the named-author watches, with anything claiming RH progress screened
> by description against the D-H discipline, the Beurling discipline, and the DMV kill (#162).

## STATUS

- **Date:** 2026-08-25 (queries executed 2026-08-26 UTC). Window swept: 2026-07-18 through
  2026-08-26 (submission date, arXiv API `submittedDate`).
- **Verdict histogram (33 in-window papers graded):** CANDIDATE 2, ADJACENT-WATCH 7,
  KNOWN-TO-REPO 2, LEVEL-3-MIRROR 10, OFF-TARGET 12, NEW-LOAD-BEARING 0.
- **Net:** The loudest window since the sweeps began, and the noise is concentrated in this
  project's exact objects. Two CANDIDATE hits. First, Alpöge-Furman (2608.13637): an
  unconditional record (at least $2/3$ of zeta zeros simple AND on the critical line, at least
  $5/6$ distinct; previous unconditional records $5/12$ and $0.6603$) obtained by replacing RH in
  Montgomery's 1973 deduction with a rank-trace inequality on a FINITE COMPRESSION OF WEIL'S
  HERMITIAN FORM, Sylvester's law of inertia handling off-line pairs, formally verified in Lean 4,
  and, per the arXiv comments field, "discovered autonomously by Claude (Anthropic); verified and
  communicated by the listed authors." That is bounded-rank inertia bookkeeping on the truncated
  Weil form: the e1s corner (#169) made to buy a positive PROPORTION of zero location
  unconditionally. It does not touch the four-level analysis (a proportion survives a
  $\beta = 0.51$ world, thread F), but the mechanism and its $2/3$ ceiling are a live question for
  the marginal-positivity compass, and the Lean artifact is a VERIFIER resource. Second, Vedana
  (2608.10121): a classification-with-uniqueness of Fourier summation formulas with strip-supported
  frequency measures, explicitly encompassing Guinand-Weil explicit formulas for the Selberg
  class, in bijection with almost periodic meromorphic Nevanlinna functions: a structure theorem
  for the space where the SP4/Hamburger-pin clause (#160) lives. Meanwhile the R1 slot itself is
  confirmed silent again: none of the four shapes fired. The nearest miss is deliberate-watch
  territory, not a trigger: Maynard-Pandey-Radziwiłł (2608.14777) improved Vinogradov's 1937
  exponential-sums-over-primes exponent ($N^{4/5} \to N^{19/24}$, unconditional), the watched
  bilinear school's first exponent move, still far above the near-$\sqrt x$ trigger. The
  CCM/Suzuki ecosystem produced no new core-author submissions but is visibly crowding: an AI
  meta-agent paper (Eureka, 2608.19047) advertises a positivity certificate for Suzuki's localized
  Weil form to $a \le 69/200 = 0.345$, which sits strictly below the first-prime threshold
  $(\log 2)/2 \approx 0.3466$ (the archimedean-only fragment the landscape scorecard prices as
  RH-agnostic via the CC 2006.13771 theorem), and an independent six-author group (2607.24830)
  numerically implements Suzuki's Weil-quadratic-form operator including off-line-zero blow-up
  diagnostics: P12's window is narrowing, in-window and measurably. Process signal for the
  proof program: two of the window's notable items are AI-agent-produced mathematics, one of them
  a Lean-verified record on zeta zeros.

## Table (ordered by grade, most to least relevant; date within grade)

| arXiv ID | Authors | One-line claim | Grade | Screen applied |
|---|---|---|---|---|
| [2608.13637](https://arxiv.org/abs/2608.13637) | Alpöge, Furman | Unconditionally, at least $2/3$ of zeta zeros (with multiplicity) are simple and on the critical line and at least $5/6$ are distinct ($0.6725$/$0.8362$ with the Montgomery-Taylor window; prior records $5/12$, $0.6603$): Montgomery's 1973 RH-conditional deduction made unconditional via a rank-trace inequality on a finite compression of Weil's Hermitian form, Sylvester inertia handling off-line pairs; extends to primitive Dirichlet L-functions; formally verified in Lean 4; comments field: proof discovered autonomously by Claude (Anthropic), verified and communicated by the listed authors | CANDIDATE | D-H: unposable (consumes the explicit formula's prime side plus the FE; D-H has no Euler product), the expected pass for an Euler-consuming method; DMV: escapes via the FE/lattice clause (its analytic inputs, Aryan and Baluyot-Goldston-Suriajaya-Turnage-Butterbaugh, are zeta-lattice-specific). Level check: a proportion statement stays thread-F in REACH (compatible with off-line zeros in the residual third), so the standing four-level analysis is unmoved. CANDIDATE for the MECHANISM: bounded-rank inertia bookkeeping on the compressed Weil form is exactly the e1s corner (#169: count structure-cheap up to $O(1)$, location = M4), here shown to buy a positive proportion of LOCATION unconditionally. Deep read assigned (ceiling analysis + Lean artifact as VERIFIER resource + provenance section). |
| [2608.10121](https://arxiv.org/abs/2608.10121) | Vedana | Classifies Fourier summation formulas $\sum a(\lambda_n)\varphi(\lambda_n) = \int \hat\varphi\,d\nu + \sum_{\gamma \in A} b(\gamma)\hat\varphi(\gamma)$ with the discrete frequency measure supported on a finite-width strip in $\mathbb{C}$ (explicitly encompassing Guinand-Weil explicit formulas for the Selberg class, beyond the prior classification's scope): a bijective correspondence with almost periodic meromorphic Nevanlinna functions, each such function giving a UNIQUE formula | CANDIDATE | No RH claim to screen. Beurling-discipline read: this is a structure theorem for exactly the identity class the counting-side disciplines police (which node sets and strip measures admit Poisson/Guinand-Weil-type formulas, with a rigidity clause), i.e. the space where the SP4 glue and the Hamburger pin (#160: the identifying clause is the additive lattice) live, in the Krein/de Branges-adjacent language of the #171 corridor. Deep read assigned: what the correspondence says about the pin slot and whether the Nevanlinna class parameterizes the glue space. Caught by the "Weil explicit formula" lit_watch window (harvested 2026-08-20, graded here). |
| [2607.24830](https://arxiv.org/abs/2607.24830) | Kim, Hong, Kim, Choi, Jang, Kim | Numerical realization of Suzuki's Weil-quadratic-form operator (Hilbert-Pólya frame): high-precision spectral law at the archimedean place, universality claims, an operator form of Weil's positivity criterion, and a measured exponential residual blow-up under off-line-zero perturbations; abstract states it does not prove RH | ADJACENT-WATCH | Suzuki-operator axis (the exact object of this project's #179-#191 xi arc and P12). math.GM-listed, numerics-only, no new theorem; notable for being discrimination-aware (they test off-line perturbations, a D-H-flavored diagnostic). SCOOP-RELEVANT: in-window confirmation of the frame audit's "external groups" pressure on P12; the courtesy communication should not wait another cycle. |
| [2608.19047](https://arxiv.org/abs/2608.19047) | Wong, Cui, Tan, Zhan, Lin, Guo, Dai, Zeng, Li | Eureka, a task-conditioned meta-agent architecture (cs.AI cross math.NT); its Math/Conjecture Agent "identifies bottlenecks in Riemann Hypothesis research and advances a positivity certificate for Suzuki's localized Weil quadratic form to $0 < a \le 69/200 = 0.345$, reaching ~99.55% of $(\log 2)/2$" | ADJACENT-WATCH | CCM/Suzuki axis + AI-process signal. Screen by region: $69/200 = 0.345 < (\log 2)/2 \approx 0.34657$, so the certified window's autocorrelation support stays below $\log 2$, the first prime power: the Weil form there is the archimedean-plus-pole fragment, the region the landscape scorecard prices as RH-agnostic (CC arXiv:2006.13771 proved archimedean positivity; it is the $\Gamma$-half D-H shares, so a certificate confined there is D-H-blind by construction and consumes no Euler data: the #174 axiom-census "free region"). The math content as abstracted is therefore infrastructure, not territory; the notable part is the process claim (an agent system aiming at, and correctly identifying, the localization program's threshold). Certificate details unverified beyond the abstract (62 pp., not deep-read). |
| [2608.14777](https://arxiv.org/abs/2608.14777) | Maynard, Pandey, Radziwiłł | Unconditional: $|\sum_{n<N}\Lambda(n)e(n\alpha)| \le N^{o(1)}(N/B^{1/2} + N^{19/24})$ for $\alpha = a/q + \epsilon$, $q \le N^{1/2}$, $|\epsilon| \le 1/(qN^{1/2})$, $B = \max(q, qN|\epsilon|)$: improves Vinogradov's 1937 exponent $4/5$ for exponential sums over primes | ADJACENT-WATCH | R1 shape (ii) school watch (the #146 sieve-side trigger). The watched school's first genuine exponent move in the bilinear von Mangoldt engine, and unconditional; but $19/24 \approx 0.792$ is nowhere near the near-$\sqrt x$ critical-range trigger, and the gain is in the classical minor-arc range, not the narrow range. Trigger NOT fired; school upgraded from "qualitative $o(1)$ tier" to "moving exponents": re-check every cycle. |
| [2607.16795](https://arxiv.org/abs/2607.16795) | Michalowski | Explicit uniform cubic wedge for consecutive Toeplitz minors of the Riemann $\xi$ coefficients in a tail regime, with certified numerics; abstract states verbatim it "makes no progress on the Riemann Hypothesis" | ADJACENT-WATCH | Named-author watch hit (the dBN PF-order line, 2602.20313; same Toeplitz-minor toolbox as this project's `e_dbn_kernel`). Complementary-region positivity only; no zero-location force; explicit disclaimer, the Groskin-style honest-infrastructure pattern. |
| [2608.08682](https://arxiv.org/abs/2608.08682) | Holland | A new hyperbolicity wedge for Jensen polynomials of $\xi$ (degree-derivative parameter region) plus a joint semicircle limit; notes RH is equivalent to hyperbolicity of ALL Jensen polynomials, proves it only in a restricted region | ADJACENT-WATCH | GORZ/Jensen axis (hyperbolicity = the dBN-adjacent RH-equivalent family). A restricted-region hyperbolicity is compatible with an off-line world (the residual region), and this project measured the Jensen/Turán observables' D-H stealth window (#27): partial wedges are structurally Level-3-reaching. Watched for wedge-growth follow-ups. |
| [2608.13468](https://arxiv.org/abs/2608.13468) | Bondarenko, Seip | Constructs nonzero continuous Fourier self-dual functions with dense zero sets, settling a question of Radchenko-Viazovska, via reproducing-kernel spaces of Fourier-invariant Hermite expansions and universal interpolating sequences | ADJACENT-WATCH | Named-school watch hit (Fourier-uniqueness / irregular nodes). A rigidity-FAILURE result: maps where self-duality plus a large zero set does NOT force vanishing, i.e. the negative boundary of the uniqueness-pair landscape this project watches for additive-lattice mechanisms. No arithmetic content; keeps the KNS-school first-read item warm. |
| [2608.22198](https://arxiv.org/abs/2608.22198) | Gonçalves, Radchenko, Ramos | Hörmander-Bernhardsson extremal problem (point-evaluation norm in Paley-Wiener space) in all dimensions: radial extremals satisfy a third-order linear ODE with polynomial coefficients | ADJACENT-WATCH | Extremal-function toolbox community (the 2502.05106 Carneiro-school watch for the #181(ii) band-ceiling question). Pure PW-extremal machinery, no arithmetic contact; tracked because the band-limited one-sided toolbox is the S4-shape's raw material. |
| [2607.25002](https://arxiv.org/abs/2607.25002) | Verjovsky | Expository-plus-observations: smoothed Mertens criteria; RH identified with an $L^p$ condition on the discrete Laplace transform of the Mobius function | KNOWN-TO-REPO | Same species as the precedent sweep's Liflandsky 2607.09797 (this object exactly): the catalogued one-sided-bound-forces-RH (S7) restatement class, thread D of #155. Built from $1/\zeta$'s coefficients so D-H cannot pose it (trivial pass for an Euler-consuming criterion); supplies no mechanism for the bound. |
| [2607.26114](https://arxiv.org/abs/2607.26114) | Gaber | Necessary-and-sufficient RH criteria via summatory asymptotics of generalized Euler $\ell$-totients (math.GM); no proof claim | KNOWN-TO-REPO | Nicolas-Robin totient-criterion family: the known-criteria class already catalogued in the atlas. No mechanism for the required bound; no discrimination content to screen. |
| [2608.16034](https://arxiv.org/abs/2608.16034) | Hua, Yang | Unconditional proportions of simple and distinct zeros on the critical line in a prime-modulus Dirichlet family, near-microscopic to polylogarithmic heights; "no form of GRH is assumed" | LEVEL-3-MIRROR | Proportion-on-the-line result (thread F, #155): compatible with isolated off-line zeros elsewhere. Two days after 2608.13637; whether it uses the compression mechanism is a deep-read question deferred to the Alpöge-Furman read. |
| [2608.15773](https://arxiv.org/abs/2608.15773) | Dong, Wang, Wang, Zhang, Zhao | Large values of quadratic character sums under GRH | LEVEL-3-MIRROR | Extreme-value/resonance class (thread C, #155): size statistics, not zero location; GRH consumed. |
| [2608.15063](https://arxiv.org/abs/2608.15063) | Chen, Housholder, Khan, Miller, Pradhan | Bounds on zeros near the central point in families of cuspidal newforms under GRH (one-level-density regime) | LEVEL-3-MIRROR | Low-lying-zero family statistics (thread B/E): height-averaged observables survive a $\beta = 0.51$ world; GRH consumed. |
| [2608.07399](https://arxiv.org/abs/2608.07399) | Bondarenko, Heap | Assuming RH, Siegel zeros force gaps between zeta zeros smaller than half the average spacing | LEVEL-3-MIRROR | Gap/pair-correlation statistics conditional on RH (thread B): addresses spacing, not location; the Siegel-zero coupling is the interesting part but runs strictly downstream of RH as hypothesis. |
| [2608.06286](https://arxiv.org/abs/2608.06286) | David, Devin, Fazzari, Waxman | Average analytic rank for $y^2 = x^3 - dx$ twist L-functions under GRH | LEVEL-3-MIRROR | One-level-density family statistics; GRH consumed as input (thread B/E). |
| [2608.05961](https://arxiv.org/abs/2608.05961) | Gao, Zhao | Sharp moment bounds for twisted quadratic characters of prime modulus under GRH | LEVEL-3-MIRROR | Moments class (thread B, #155): moment asymptotics hold whether or not RH is true. |
| [2607.28931](https://arxiv.org/abs/2607.28931) | Koyama | Under the Deep Riemann Hypothesis, a fine-structure hierarchy of prime biases in APs (mollified Weil explicit formula; special L-values rank residue classes beyond quadratic-residue status; universal dominance of $-1 \bmod N$) | LEVEL-3-MIRROR | Chebyshev-race statistics under DRH: the primes-thread observable class (races read zeros' real parts statistically, PRIME_PATTERNS), assumption-side not mechanism-side. Caught by the "Weil explicit formula" lit_watch window (harvested 2026-08-20, graded here). |
| [2607.23150](https://arxiv.org/abs/2607.23150) | Hayani | Chebyshev bias from higher roots in prime ideal races: conditional characterization plus unconditional special cases | LEVEL-3-MIRROR | Race statistics (primes-thread observable class); no zero-location forcing. |
| [2607.21532](https://arxiv.org/abs/2607.21532) | Bui, Florea, Milinovich | Weighted CLT for joint central values of Dirichlet L-functions under GRH; simultaneous large/small central values in positive proportion | LEVEL-3-MIRROR | Central-value distribution statistics (thread B); GRH consumed. |
| [2607.20853](https://arxiv.org/abs/2607.20853) | Gao, Zhao | Murmuration density for quadratic Hecke L-functions of the Gaussian field under GRH | LEVEL-3-MIRROR | Family-correlation (murmuration) statistics; GRH consumed; no location content. |
| [2608.11943](https://arxiv.org/abs/2608.11943) | Nikzad, Deninger | Invariant functions on $p$-divisible groups and the $p$-adic corona problem II (removes dimension restrictions from part I) | OFF-TARGET | Named-author watch hit (Deninger). $p$-adic function theory, no contact with the foliated/dynamical trace-formula program or the W6 determinant-class spec (R1 shape (iii) did NOT fire; recorded because the author is on the direct watch list). |
| [2608.19525](https://arxiv.org/abs/2608.19525) | Krause, Mousavi, Tao, Teräväinen | Quantitative Szemerédi-type bounds for polynomial progressions with shifted-prime differences (Gowers uniformity for primes) | OFF-TARGET | Bilinear-school author watch hit: additive-combinatorial, no exponent move toward the #146 near-$\sqrt x$ trigger. |
| [2607.28091](https://arxiv.org/abs/2607.28091) | Grimmelt, Teräväinen | Random linear configurations in polylog-dense sets and primes (generalized von Neumann + densification) | OFF-TARGET | Bilinear-school author watch hit: transference machinery, no cancellation-exponent content. |
| [2608.12709](https://arxiv.org/abs/2608.12709) | Kim | Removes GRH from Allen-Genao uniform bounds on prime levels of abelian division fields of elliptic curves | OFF-TARGET | Arithmetic application; GRH removed by algebraic means, no contact with the five open coordinates. |
| [2607.21259](https://arxiv.org/abs/2607.21259) | Guo, Lin, Xu | Distribution of fractional parts of polynomials mod $p$ via finite Fourier analysis and Weil bounds | OFF-TARGET | Consumes finite-field purity (Weil bounds) as input: the R1-facet-A consumer pattern (#146), supplies nothing. |
| [2607.17731](https://arxiv.org/abs/2607.17731) | Moser | Jacob's-ladders zeta-functionals and $\zeta$-equivalents of Fermat-Wiles from elementary $\zeta$-pulses (long-running series; RH as working assumption) | OFF-TARGET | No mechanism, no discrimination; RH consumed as input. |
| [2607.24370](https://arxiv.org/abs/2607.24370) | Yoo | Multiplicative irreducibility of shifted multiplicative subgroups in prime fields, extremal case resolved via a Stepanov bound | OFF-TARGET | R1 shape (iv) keyword hit: Stepanov method used where it lives (finite fields, Frobenius present). Confirms #162's finding by silhouette: no archimedean Stepanov carrier appeared; the S4 slot stays verified-empty. |
| [2608.02180](https://arxiv.org/abs/2608.02180) | Ben-Moshe | Chromatic redshift bound for algebraic K-theory from Quillen-Lichtenbaum descent | OFF-TARGET | Keyword false positive on "Lichtenbaum" (R1 shape (iii) query): homotopy theory, no zeta trace formula. |
| [2607.26685](https://arxiv.org/abs/2607.26685) | Komiya | K-equivalence of arithmetically equivalent number fields via higher K-groups; connects to zeta SPECIAL VALUES (Rost-Voevodsky) | OFF-TARGET | R1 shape (iii) query hit: Lichtenbaum-conjecture-adjacent special-value arithmetic (values at integers), not a determinant-class trace formula with a pole budget for the ZEROS. |
| [2608.12094](https://arxiv.org/abs/2608.12094) | Zhang, Yang | Resolves the 196560 auxiliary-function conjecture for the Leech lattice (radial Fourier-interpolation basis, positivity constraints, dim 24) | OFF-TARGET | Viazovska-school watch hit: LP-certificate sphere-packing world, the fixed-sign-form space the Breadth Program mapped as insufficient for M4's polarity (#119-#121); interpolation nodes are lattice-derived, not the non-lattice-node event watched for. |
| [2607.22032](https://arxiv.org/abs/2607.22032) | Arman, Bondarenko, Prymak, Radchenko | Grünbaum-type covering problem for symmetric configurations (rate-distortion methods) | OFF-TARGET | Named-school hit (Radchenko): discrete geometry, no Fourier-uniqueness or arithmetic content. |
| [2608.11614](https://arxiv.org/abs/2608.11614) | Hiranouchi, Sugiyama | Injectivity of Galois symbol maps for Jacobians and multiplicative groups (Chow-group techniques) | OFF-TARGET | R1 shape (iii) query hit (Lichtenbaum-adjacent K-theory vocabulary): variety-based Galois cohomology; no contact. |

The 2-deep-read budget is ASSIGNED rather than spent in-session: both CANDIDATE papers were read
to full-abstract-plus-metadata depth here (screens applied by description) and need full-text
reads next session; everything else needed nothing beyond its abstract.

## In-window version bumps on tracked papers (harvested at listing level 2026-08-20; graded here, not counted in the histogram)

Four `lit_watch` tracked papers re-versioned inside the window (these are version events on known
papers, not new submissions, so they are recorded here rather than in the table):

- **2602.20313 v2 (Michalowski, dBN kernel PF order; 2026-07-20): a PARTIAL WITHDRAWAL.** v2
  "withdraws the asymptotic-threshold theorem of v1 because its derivative-tail certificate was
  unsound"; the central certified PF$_5$ counterexample is unchanged, and eight further
  configurations are now double-certified (Leibniz + independent interval determinant). See the
  discrepancy log below: the repo's citations were checked and cite only the surviving claims.
- **2606.09096 v2 (Suzuki, Weil's quadratic form via the screw function; 2026-08-17): minor.**
  35 KB to 37 KB, 32 pages, no stated content changes; the abstract's conjecture (self-adjoint
  operator with eigenvalues $\mathrm{Im}\,\rho$ as the $a \to \infty$ limit of nonlocal
  realizations of the first-order differential operator on $[-a,a]$) is unchanged. MANDATORY
  watch per the watchlist; a text diff belongs to the P12 completion session, since P12 engages
  this paper's (1.2) directly.
- **2605.20224 v4 (Groskin, truncated Weil form zero approximation; 2026-08-14): maintenance
  with one claim correction.** v4 "corrects the claim that T=1200 removes the c=100
  negative-sign block (it rearranges; the cutoff-free certificate is unaffected), records
  M. Osman's odd-sector probe, updates two Connes references. No measured value changes."
- **2607.02828 v3 (Groskin, finite Guinand-Weil dictionary; 2026-08-14): maintenance.** Updates
  two Connes references to journal versions and corrects ancillary $h_+'$ values at
  $t = 50, 100, 1000$ (unconverged series acceleration); "every row still meets the Lemma 3.1
  envelope; no bound changes." The no-RH-claim disclaimer is intact verbatim.

## Discrepancy log (SURVEYOR reports; ADVERSARY/VERIFIER decide)

1. **Michalowski v1's withdrawn theorem vs repo citations: VERIFIED UNAFFECTED.** The three repo
   files citing 2602.20313 ([`e_dbn_kernel.md`](../../../experiments/criticality/e_dbn_kernel.md),
   [`3e_li_de_bruijn_newman.md`](../../../experiments/positivity/3e_li_de_bruijn_newman.md),
   [`12_debruijn_newman_criticality.md`](../research_directions/12_debruijn_newman_criticality.md))
   cite only the PF$_5$ counterexample and the "orthogonal to $\Lambda$" scoping quote, both of
   which v2 preserves. No edit required; recorded so the check is on file.
2. **Alpöge-Furman vs the e1s reading: a sharpening to adjudicate, not a contradiction.** The
   repo's standing dichotomy (#169: on the compressed Weil form the eigenvalue COUNT is
   structure-cheap up to $O(1)$; the LOCATION half is M4) is not contradicted by 2608.13637, but
   the paper shows finite-compression inertia buys a positive PROPORTION of location
   unconditionally. If the deep read confirms the mechanism as described, the e1s wording should
   be refined (count cheap; full location = M4; proportion-location purchasable by rank-trace
   inertia) and the interesting object becomes the mechanism's ceiling. Flagged for ADVERSARY;
   not resolved here.
3. **Groskin v4's corrected claim vs the C3/e2ba audit (#195): CHECK ITEM.** e2ba engaged the
   Groskin lineage's numbers (horizon pricing at $\lambda = 10$); v4 corrects a T=1200/c=100
   negative-sign-block claim (rearranged, not removed) and ancillary $h_+'$ values, with "no
   measured value changes" claimed. A one-pass cross-check that e2ba consumed none of the
   corrected rows is cheap and belongs to the next maintenance session; nothing in the v4
   comment suggests a bound this project used has moved.
4. **The Eureka abstract's framing invites over-reading.** "Advances a positivity certificate
   ... to $0.345$" reads like new territory; by the repo's scorecard the entire sub-$(\log 2)/2$
   window is the archimedean fragment (CC 2006.13771, RH-agnostic, D-H-shared $\Gamma$-half).
   Recorded so the project's own citations of the window never inherit the framing; a one-section
   check of the 62-page paper would settle whether anything crosses the threshold (nothing in the
   abstract claims it does).

## Swept, no hits in-window

Every query below was executed against the arXiv API 2026-08-26 UTC with
`submittedDate:[20260718000000 TO 20260826235959]`; no query failed; totals are the API's
`totalResults`. Hits already graded above are cross-referenced, not re-listed.

**The four R1 WATCH shapes ([`sourcing_gap_r1.md`](../sourcing_gap_r1.md)):**
- (i) Variety-free purity/Ramanujan: `abs:"Ramanujan conjecture" AND abs:purity` (all
  categories): 0 results. The van Frankenhuijsen anchor remains descendant-free (19+ months per
  #155's baseline).
- (ii) Near-$\sqrt x$ bilinear cancellation: `cat:math.NT AND abs:bilinear AND (abs:Mobius OR
  abs:"von Mangoldt")`: 0 results. School query `cat:math.NT AND (au:Matomaki OR au:Radziwill OR
  au:Teravainen)`: 3 results, all graded above (2608.14777 ADJACENT-WATCH: the school's first
  exponent move, $4/5 \to 19/24$, classical range; 2608.19525 and 2607.28091 OFF-TARGET).
  Trigger NOT fired.
- (iii) Determinant-class trace formula (Weil-etale / Deninger-adjacent): `abs:"Weil-etale" OR
  abs:Lichtenbaum OR au:Deninger OR au:Flach`: 5 results, none a trace formula for $\zeta$
  (2608.11943 Deninger OFF-TARGET; 2608.02180, 2607.26685, 2608.11614 OFF-TARGET keyword hits;
  2607.16753 discarded, see false positives). The `"determinant class zeta"` keyword window: 0
  results. Shape empty.
- (iv) S4-carrier (one-sided extremal / Stepanov-like archimedean mechanism): `abs:Stepanov OR
  (abs:prolate AND abs:zeta)`: 1 result (2607.24370, finite-field Stepanov, OFF-TARGET above).
  No archimedean carrier appeared; consistent with #162's verified-empty finding and #169's
  closure of every buildable family. The 2310.18423 metaplectic Sonin projector remains the sole
  unbuilt variant; no paper constructing it appeared.

**Named-author watches:**
- Connes / Consani / Moscovici / van Suijlekom / Groskin: `au:` query returned 0 new in-window
  submissions. Groskin activity is version-maintenance only (v3/v4 bumps above). Consani's
  listing shows nothing past the tracked 2602.15941 and 2606.06604.
- Suzuki (math.NT): 0 new submissions; the 2606.09096 v2 bump is recorded above.
- The de Bruijn-Newman line: `abs:"de Bruijn-Newman"` (all categories): 0 results. Michalowski's
  new in-window paper (2607.16795, ADJACENT-WATCH above) surfaced via the broad RH query instead
  (its abstract does not use the phrase). No $\Lambda \le 0$-side result appeared.
- Dor-Hrushovski model-theoretic Frobenius: `au:Hrushovski`: 0 results; no follow-up to
  2212.05366.
- Kulikov-Nazarov-Sodin (as the trio): no new joint submission. School activity via
  `abs:"Fourier uniqueness" OR abs:"Fourier interpolation" OR au:Radchenko OR au:Viazovska`:
  6 results: 2608.13468 (Bondarenko-Seip, ADJACENT-WATCH above), 2608.22198 (ADJACENT-WATCH
  above), 2608.12094 and 2607.22032 (OFF-TARGET above), 2 discarded author collisions (below).
- Burnol / Sonine spaces: `au:Burnol OR abs:"Sonine spaces"`: 0 results.

**M4 axis (co-equal frontier target, checked for completeness):** `abs:"Hodge standard
conjecture" OR abs:"Rosati involution"`: 0 results.

**The seven lit_watch keyword windows (full-window re-run, superset of the 2026-08-20/2026-08-26
harvest windows):** "Weil positivity" + "Weil explicit formula" combined: 2 results, exactly the
harvest's two IDs (2608.10121 CANDIDATE, 2607.28931 LEVEL-3-MIRROR above): the graded sweep and
the listing-level watcher agree. "Li coefficients" + "Nyman-Beurling" + "Riemann hypothesis
positivity" combined: 0 results. "de Branges space" + "determinant class zeta" combined: 0
results. Net: 6 of 7 windows empty over the full 39-day window, confirming the watcher baseline.

**Broad catch-alls (the screen-coverage sweeps):** `cat:math.NT AND abs:"Riemann hypothesis"`:
18 results, all graded above. `cat:math.GM AND abs:"Riemann hypothesis"`: 2 results, both graded
above (2607.24830, 2607.26114). NOTABLE NEGATIVE: zero claimed full proofs or disproofs of RH
in-window in either category (the precedent window had one, self-withdrawn); the D-H/Beurling/DMV
kill battery had no proof-claim to execute on this cycle and was applied only as the descriptive
screens recorded in the table.

**Author-collision / query-mechanics false positives (returned, inspected, discarded; recorded
for integrity, not graded):** 2608.05401 (K. Radchenko Serdula, Higgs phenomenology software),
2607.22374 (V. Radchenko, stochastic heat equations), 2607.16753 (Abo-Ranestad-Schreyer,
surfaces in $\mathbb{P}^4$; returned by the shape-(iii) author query, match cause unclear,
presumed fuzzy author matching).

## NEXT

Cadence: next graded sweep due ~2026-09-08 (two-week rhythm restored; the audit's repaired
tripwire counts this sweep as the decay-item clear). Carry-forward, in priority order:

1. **Deep read + ADVERSARY pass on 2608.13637 (Alpöge-Furman), urgent.** Audit the rank-trace
   inequality and the Sylvester-inertia handling of off-line pairs against the e1s corner (#169)
   and the trojan-ledger inertia bookkeeping; locate the structural cause of the $2/3$ ceiling
   (the marginal-positivity compass predicts the mechanism starves exactly where the exact
   structure of $\zeta$ must be consumed; verify or refute against their Section 1 provenance and
   the Lean artifact, which is also a direct VERIFIER resource and a process precedent for the
   AI-only program). Watch for follow-ups pushing the proportion or transferring the compression
   trick.
2. **Deep read on 2608.10121 (Vedana)** against the Hamburger pin (#160) and the #171
   canonical-system corridor: does the almost-periodic-Nevanlinna correspondence parameterize the
   SP4 glue space, and where does the additive lattice enter its uniqueness clause? Note the
   thematic echo: the precedent sweep's NEXT watched Groskin's Guinand-Weil DICTIONARY for
   follow-ups; the dictionary theme moved this window, but from the classification side and a
   different school.
3. **P12 must not wait another cycle.** Two independent in-window Suzuki-operator artifacts
   (2607.24830 numerics; 2608.19047's agent certificate) on top of the frame audit's
   "three external groups" note: the courtesy communication and finishing items (figures, length
   pass, Owen's decisions) are now scoop-exposed on a measured, shortening clock.
4. **Version-bump follow-ups:** diff Suzuki 2606.09096 v2 at the P12 session; run the cheap
   e2ba-vs-Groskin-v4 cross-check (discrepancy log item 3).
5. **Standing items:** the KNS first-read pair (2509.17600, 2509.14953) remains unread, third
   cycle running: fold into the Vedana read (same school vocabulary). Re-run all four R1 shape
   queries plus the full named-author list at next cadence; the missed-R1-event risk is unchanged
   in kind, and this window's two-CANDIDATE yield is the concrete argument for never letting the
   cadence slip to 38 days again.
