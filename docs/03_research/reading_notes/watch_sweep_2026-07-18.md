# WATCH sweep: arXiv 2026-07-01 through 2026-07-18

> SURVEYOR reading note. Executes TODO.md's open SURVEYOR item (iv), "refresh the WATCH
> sweep ([`sourcing_gap_r1.md`](../sourcing_gap_r1.md) quadruple + Connes/Consani/Moscovici/van
> Suijlekom submissions + the bilinear-Mobius school + the dBN PF-order line; last full sweep
> 2026-07-03)." That 2026-07-03 pass was the full 303-paper 2021-2026 corpus build
> ([`rh_corpus_2021-2026_vs_frontier.md`](rh_corpus_2021-2026_vs_frontier.md), LEARNINGS #155,
> grading convention adopted verbatim below). This is the cheap, narrow, two-week refresh: arXiv
> listings and abstracts only, swept against the four analytic shapes of the R1 WATCH slot
> ([`sourcing_gap_r1.md`](../sourcing_gap_r1.md), cont. 2 through cont. 3-later-still) plus the
> named-author watches, with anything claiming RH progress screened by description against the
> D-H discipline, the Beurling discipline, and the DMV kill.

## STATUS

- **Date:** 2026-07-18. Window swept: 2026-07-01 through 2026-07-18 (submission date, arXiv API
  `submittedDate`).
- **Verdict histogram (14 in-window papers graded):** KNOWN-TO-REPO 1, ADJACENT-WATCH 2,
  OFF-TARGET 7, LEVEL-3-MIRROR 4, NEW-LOAD-BEARING 0.
- **Net:** Two weeks of arXiv produced one CCM-axis infrastructure paper (Groskin, explicitly
  disclaiming any RH claim) and thirteen off-target or Level-3-mirror papers plus one restatement
  already in the repo's known-criteria class; every one of the four R1 WATCH shapes and every
  named-author watch except the Groskin/CCM lineage is confirmed silent in-window. Zero CANDIDATE.
  The standing finding is unmoved: no variety-free purity theorem, no unconditional near-sqrt(x)
  power-saving bilinear cancellation, no determinant-class trace formula with an independently
  computable pole budget, and no S4/Stepanov-like archimedean mechanism appeared anywhere in the
  window.

## Table (ordered by grade, most to least relevant; date within grade)

| arXiv ID | Authors | One-line claim | Grade | Screen applied |
|---|---|---|---|---|
| [2607.02828](https://arxiv.org/abs/2607.02828) | Groskin | Two finite theorems on the Connes-van Suijlekom / CCM truncated Weil quadratic form: a Guinand-Weil dictionary at prime cutoff and an archimedean-tail positivity certification (budget $B_T \sim (2N{+}1)\rho\log(T)/(\pi^2 T)$), verified on the first 512 zeros | ADJACENT-WATCH | CCM axis (Groskin lineage, already tracked at 2605.20224). No RH-progress claim to screen: abstract states verbatim "the paper makes no Riemann Hypothesis, prime-counting, next-prime, or factoring claim." |
| [2607.09797](https://arxiv.org/abs/2607.09797) | Liflandsky | Explicit formula for the discrete Laplace transform of the Mobius function; shows an $O(x^{-1/2})$ decay bound on it would imply RH unconditionally (the converse needs extra hypotheses) | KNOWN-TO-REPO | D-H: unposable by construction (built from the Mobius function, i.e. $1/\zeta$'s Dirichlet coefficients; D-H has no Euler product to invert), so it passes trivially, the expected behavior for a genuinely Euler-consuming object. Supplies no mechanism to prove the bound itself: same species as the repo's already-catalogued one-sided-bound-forces-RH (S7) restatement class (thread D, LEARNINGS #155). |
| [2607.04632](https://arxiv.org/abs/2607.04632) | Turnage-Butterbaugh | Survey of a recent zero-density-estimate / primes-in-short-intervals advance | ADJACENT-WATCH | SP-C1/D-H firewall infrastructure (thread E, #155): zero-density bounds do not force zeros onto the line and survive a beta=0.51 world, but are the watched class for any future density-matching move. |
| [2607.14515](https://arxiv.org/abs/2607.14515) | Kandhil, Languasco, Moree | Pair-correlation approach to the least prime in an AP and the smallest quadratic non-residue, going beyond GRH-conditional bounds | LEVEL-3-MIRROR | Pair correlation is the named GUE/Level-3 tool (thread B, #155); addresses consequences of zero location statistically, not location itself. |
| [2607.04316](https://arxiv.org/abs/2607.04316) | Moriya | A "Gaussian-Perron prime-force defect" comparing a smoothed prime-side force to $\zeta'/\zeta$: a local diagnostic for zero geometry | LEVEL-3-MIRROR | Diagnostic, not a forcing or discriminating argument; by its own framing it profiles zero geometry locally and is compatible with any configuration away from its own measured points. |
| [2607.03654](https://arxiv.org/abs/2607.03654) | Yang, Zhao | Lower bounds for extreme values of $\mathrm{Re}\,\zeta$ on the critical line via the Bondarenko-Seip resonance method | LEVEL-3-MIRROR | Extreme-value statistics, the named Level-3 mirror class (thread C, #155); addresses size of $\zeta$ on the line, not zero location. |
| [2607.00282](https://arxiv.org/abs/2607.00282) | Conrey, Kwan, Lin, Turnage-Butterbaugh | Levinson's-method proportion-of-critical-zeros plus unconditional mean-value theorems for twisted PGL(2)/PGL(3) L-functions | LEVEL-3-MIRROR | Proportion-on-the-line result (thread F, #155); compatible with isolated off-line zeros elsewhere; classical technique, no purity/Ramanujan content despite the automorphic setting. |
| [2607.09110](https://arxiv.org/abs/2607.09110) | Cantarini | Weighted-average (Sobolev / Holder-Zygmund) variants of the Elliott-Halberstam-twisted-by-Mobius problem, Goldbach-adjacent | OFF-TARGET | Conditional on GRH plus a weak Gonek-Hejhal conjecture; sieve/function-space technique, not the R1 shape's required unconditional near-sqrt(x) bilinear cancellation. |
| [2607.04338](https://arxiv.org/abs/2607.04338) | Micheas | Claimed full proof of RH via Hadamard-Weierstrass factorization of $\xi$ | OFF-TARGET | D-H: fails by description. A variety-free, arithmetic-free Hadamard-factorization argument on $\xi$ would run identically on D-H's completed L-function (which has a known off-line zero at $\rho \approx 0.8085 + 85.699i$), so any such argument is structurally wrong. Consistent with outcome: self-withdrawn by the author 2026-07-08, comment "Mistakes in main approach. Withdrawn." |
| [2607.12381](https://arxiv.org/abs/2607.12381) | Jeong, Park | Reduction-type probabilities for genus-$g$ hyperelliptic curves with a Weierstrass point | OFF-TARGET | Arithmetic statistics; no contact with any of the five open coordinates (R1/M4/CCM/SP-C1/LEVEL). |
| [2607.01126](https://arxiv.org/abs/2607.01126) | Keliher, Park | Selmer-rank distribution in prime cyclic extensions, assuming ERH | OFF-TARGET | ERH consumed as an input hypothesis, not addressed or advanced. |
| [2607.01458](https://arxiv.org/abs/2607.01458) | Goncalves, Radchenko | Sharp lower bounds for sumsets in hypercubes | OFF-TARGET | Named-author watch hit (Radchenko-Viazovska school). Topic is additive combinatorics; no interpolation or Fourier-uniqueness content at non-lattice nodes. |
| [2607.05542](https://arxiv.org/abs/2607.05542) | Slutsky, Sodin, Wennman | Measurable equivariant Weierstrass theorem for entire-function divisors (a prequel to equivariant Borel liftings work) | OFF-TARGET | Named-author watch hit (Kulikov-Nazarov-Sodin's Sodin). Pure complex-analysis / descriptive-set-theory result; no Fourier-uniqueness or number-theoretic content. |
| [2607.13159](https://arxiv.org/abs/2607.13159) | Alfes, Ono, Swaminathan | Elliptic corrections for higher Dyson ranks (mock modularity, harmonic Maass forms) | OFF-TARGET | Keyword false positive on "Maass forms." Partition theory; no Ramanujan-conjecture or purity content. |

No CANDIDATE. Nothing above required a deep read beyond its full abstract; the 2-deep-read budget
was not spent.

## Swept, no hits in-window

**The four R1 WATCH shapes ([`sourcing_gap_r1.md`](../sourcing_gap_r1.md)):**
- (i) A variety-free purity/Ramanujan theorem: empty. (Broadened the check to all of 2026
  year-to-date for "Ramanujan conjecture" AND "purity" jointly: still empty, 18+ months running
  zero descendants of the van Frankenhuijsen anchor per #155.)
- (ii) Unconditional power-saving bilinear Mobius/von Mangoldt cancellation near $\sqrt x$,
  non-algebraic: empty in-window. The one nearby hit under a broader search, 2606.15900
  ("Square-root cancellation for sums of coefficients of GL(m)-automorphic forms over values of
  random polynomials"), is finite-field-geometry-side (the wrong side of the R1 escape) and
  outside the window (June 2026) regardless.
- (iii) A determinant-class trace formula for zeta with an independently computable pole budget
  (Weil-etale / Deninger-adjacent): empty. Direct author checks on Deninger and Flach, and phrase
  checks on "Weil-etale" and "Lichtenbaum," returned nothing in-window and only one unrelated 2026
  hit outside it.
- (iv) The S4-carrier shape (one-sided extremal or Stepanov-like mechanism on an archimedean
  carrier): empty. Phrase checks on "Stepanov method" and "prolate spheroidal" + zeta both empty
  in-window, consistent with #162's verified-empty literature finding.

**Named-author watches:**
- Connes / Consani / Moscovici / van Suijlekom: no new submission in-window (direct author-field
  query empty). The one hit surfaced by general web search, "Quadratic Forms, Real Zeros and
  Echoes of the Spectral Action," is arXiv:2511.23257, already tracked as part of the CCM D_log
  line in `sourcing_gap_r1.md`; it has only newly appeared in print at Communications in
  Mathematical Physics, no new arXiv content. Consani's own 2026 listing likewise shows nothing
  past the already-tracked 2602.15941 and 2606.06604.
- The de Bruijn-Newman PF-order line: no new submission; the most recent remains the
  already-tracked Michalowski 2602.20313 (Lambda <= 0.22 upper bound side, not a Lambda <= 0
  result).
- Dor-Hrushovski model-theoretic Frobenius: no follow-up to arXiv:2212.05366 found.
- Kulikov-Nazarov-Sodin (as the trio, on Fourier uniqueness / irregular nodes): no new submission
  in-window; Sodin's one July hit (2607.05542, above) is off-topic.
- Radchenko-Viazovska-school interpolation at non-lattice nodes: no new submission in-window;
  Radchenko's one July hit (2607.01458, above) is off-topic.
- Anything citing Burnol's Sonine spaces: no new Burnol submission in-window (direct author-field
  query empty); no third-party citation surfaced by web search either.

**M4 axis (co-equal frontier target per PHASE_STATE, not one of the four R1 shapes but checked for
completeness):** "Hodge standard conjecture" / "Rosati involution": empty in-window.

## NEXT

CCM core authors are quiet this cycle apart from the Groskin/CCM-lineage infrastructure paper
(2607.02828): watch whether its Guinand-Weil dictionary or archimedean-tail-order technique gets
turned toward the Section-7 uniform-limit question (M4) in a follow-up, since Groskin's prior
paper (2605.20224) is the same lineage. Re-run all four R1 shape queries plus the full
named-author watch list at the next cadence (roughly two weeks, next due around 2026-08-01), since
every one of them is confirmed silent through 2026-07-18 and the standing risk is unchanged: a
missed R1 event is the one unbounded-cost gap. One adjacent thread outside this window worth a
first-read check next cycle if still repo-untracked: Kulikov-Nazarov-Sodin's own 2025 follow-ups
on Fourier uniqueness pairs (arXiv:2509.17600, "Critical and asymmetric Fourier uniqueness pairs";
arXiv:2509.14953, "Spectral Criteria for Uniqueness Pairs of Unitary Transforms"), both from
September 2025 and both surfaced only incidentally by this sweep.
