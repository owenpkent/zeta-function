# Wikipedia "Riemann hypothesis" article vs. repo coverage: gap analysis

Source: full pdftotext dump of the Wikipedia "Riemann hypothesis" article (~15.5k words), read completely.
Repo: /home/owen/dev/zeta-function. Search surfaces: docs/ (all .md), experiments/ (.md + .py docstrings),
lean/ (.lean + README), README.md, PUBLICATIONS.md, TODO.md, references/README.md, plus whole-repo rg for recall.

No em dashes used anywhere in this report.

## Special note: the article's "2026 Claude proof" paragraph is not a gap, it is a name mismatch

The article (in its "Zeros on the critical line" section, Notes 44-45) describes an August 2026 unconditional proof
that two-thirds of zeta zeros lie on the critical line, attributed to "an unreleased research version of
Anthropic's Claude," using Weil's explicit formula reframed as a finite-dimensional Hermitian matrix (a Gabor
system), Sylvester's law of inertia, a rank-trace inequality from von Neumann's trace inequality, and Lean 4
verification.

This exact mathematical content (Sylvester's law of inertia + von Neumann trace inequality + Gabor-system test
family + Lean-verified linear algebra bounding off-line zero pairs) is one of the most heavily worked threads in
this repo's recent history, but under a different name: "AF" (Alpoge-Furman). It is not attributed to Claude or
Anthropic anywhere in the repo. Coverage is extensive and adversarial, not credulous:

- `experiments/LEARNINGS.md` entries #211, #212, #213 (the frame session arc: F2a poses the certificate class,
  the adversary FAILS the AF record-holder out of the pool over a beta-sensitive funding read, F2b re-aims)
- `docs/03_research/reading_notes/af_lean_repository_skim.md`, `af_funding_inputs_verification.md`,
  `alpoge_furman_two_thirds.md`
- `docs/03_research/f2a_certificate_class.md`, `f2b_visibility_floor.md`
- `lean/ZetaRH/F2bSkeleton.lean`
- `experiments/arithmetic_geometric/e2bh_forced_polarization.md`, `experiments/spectral/e1s_rank_one_interlacing.md`

Net: the repo's own adversary process independently found a structural problem with the AF construction (it falls
out of the posed certificate class over a beta-sensitive funding read, A1 in LEARNINGS #211) that the Wikipedia
paragraph does not mention. This is the single deepest, most current thread in the whole repository, filed under a
different name than the one a naive keyword search on "Claude" or "Anthropic" would find.

---

## 1. ABSENT items (the gaps)

### 1a. Equivalent criteria / reformulations

- **Speiser's theorem** (Speiser 1934): RH is equivalent to zeta'(s) having no zeros in the strip 0 < Re(s) < 1/2.
  Zero hits anywhere in the repo.
- **Franel-Landau / Farey sequence criterion** (1924): RH is equivalent to a regularity statement about how evenly
  spaced the terms of the Farey sequence are. Only occurrence is the raw OCR text dump in `sources/riemann_full.txt`
  (a source PDF conversion), outside every authored surface.
- **Redheffer matrix criterion**: the determinant of the order-n Redheffer matrix equals the Mertens function M(n),
  restating RH as a growth condition on these determinants. Zero hits anywhere.
- **Björner's criterion** (2011): RH is equivalent to a statement about the Euler characteristic of the simplicial
  complex from the divisibility lattice of integers. Zero hits anywhere.
- **Landau's function / symmetric-group criterion** (Massias, Nicolas & Robin 1988): RH equivalent to a bound on
  g(n), the maximal order of an element of the symmetric group S_n. Zero genuine hits.
- **Turán's criterion and its refutation** (Turán 1948; disproved as a workable route by Haselgrove 1958, Spira
  1968, Borwein-Ferguson-Mossinghoff 2008, and shown vacuous by Montgomery 1983): a zero-free condition on finite
  Dirichlet polynomials built from the Liouville function was hoped to imply RH. The repo's many "Turán" hits are
  all a different Turán topic (Turán inequalities for the Xi function / Jensen-polynomial hyperbolicity); none of
  Haselgrove, Spira's counterexample, or Montgomery's vacuity result appear anywhere.
- **Denjoy's probabilistic argument**: treating the Mobius function as a random +-1 sequence gives a heuristic
  restatement of RH as a random-walk-type law for Mertens-function partial sums. Only occurrence is the raw source
  text dump, outside authored surfaces. (This is the same gap as arguments-for-against item below; the article
  presents it in both places.)

### 1b. Consequences of RH / GRH

- **Dudek (2014)**: RH implies an explicit short interval `(n - (4/pi)*sqrt(n)*log n, n)` always contains a prime.
  Zero hits for "Dudek" anywhere.
- **Growth of zeta(1+it) up to a factor of 2**: RH implies the growth rates of zeta(1+it) and its reciprocal are
  known up to a factor of 2. Absent; the repo only has the unrelated classical fact that zeta(1+it) != 0 implies PNT.
- **Grönwall (1913)**: GRH implies Gauss's list of class-number-1 imaginary quadratic fields is complete. Zero hits.
- **Weinberger (1973), idoneal numbers**: GRH implies Euler's list of idoneal numbers is complete. Zero hits.
- **Weinberger (1973), Euclidean number fields**: GRH for all number-field zeta functions implies any
  class-number-1 field is Euclidean or one of 4 named imaginary quadratic fields. Zero hits.
- **Odlyzko (1990)**: GRH gives sharper discriminant/class-number estimates. Absent as this specific paper; every
  "Odlyzko" hit in the repo is his zero-computation tables or GUE statistics work, a name collision.
- **Ono & Soundararajan (1997)**: GRH implies Ramanujan's ternary quadratic form x^2+y^2+10z^2 represents all
  locally-represented integers with exactly 18 exceptions. Absent; "Soundararajan" hits are Lemke Oliver-
  Soundararajan (last-digit bias) and Radziwill-Soundararajan (Selberg CLT), a name collision.
- **Dunn & Radziwill (2021)**: proved Patterson's conjecture on cubic Gauss sums under GRH. Absent; "Radziwill"
  hits are Matomaki-Radziwill (multiplicative functions), a name collision.
- **Gauss's class number conjecture / excluded middle** (Hecke 1918, Deuring 1933, Mordell 1934, Heilbronn 1934;
  made unconditional by Siegel 1935): the theorem chain where both RH-true and RH-false cases separately force
  h(D) -> infinity. Absent as this specific chain; every relevant name is a collision ("Deuring" = isogenies,
  "Mordell" = Mordell-Weil groups, "Siegel" = Siegel zeros/Siegel's lemma, "Heilbronn" = this repo's own
  Davenport-Heilbronn L-function). The phrase "excluded middle" itself never appears.

### 1c. Attempted-proof approaches

- **Zagier (1981)**: a natural invariant-function space on the upper half-plane whose Laplacian eigenvalues match
  zeta zeros; a positive-definite inner product on it would prove RH. Absent; "Zagier" hits are the unrelated 2019
  Griffin-Ono-Rolen-Zagier Jensen-polynomial paper, a name collision.
- **Cartier (1982)**: the anecdote of a computer-program bug that listed zeta zeros as Laplacian eigenvalues.
  Absent; "Cartier" hits are all the unrelated Cartier isomorphism / Cartier-Witt stack in the prismatic
  cohomology thread, a name collision.
- **Fesenko's program**: a two-dimensional generalization of Tate's thesis for arithmetic zeta functions of
  elliptic-curve models over number fields, plus a positivity conjecture on a boundary function whose partial
  resolution is due to Suzuki (2011). Absent; zero hits for "Fesenko," and the repo's many "Suzuki" hits are a
  different, unrelated Masatoshi Suzuki paper on canonical systems / the Weil-positivity screw-function program
  (2022/2026), a name collision.

### 1d. Zeta-analogue families

- **Goss zeta functions of function fields**, RH analogue proved by Sheats (1998). Neither "Goss zeta" nor
  "Sheats" appears anywhere in the repo. This is a clean, uncomplicated absence (no name collision involved).

### 1e. Numerical-verification phenomena

- **Karatsuba (1996)**: every interval (T, T+H] contains at least a certain number of sign changes of S(t).
  Absent; the repo's "Karatsuba" hits are a different Karatsuba (Stepanov-method character-sum estimates), a name
  collision.
- **Selberg (1946) / Ghosh (1983)**: average moments of even powers of S(T); S(T)/(loglogT)^(1/2) behaves like a
  Gaussian with variance 2*pi^2 (Ghosh proved this); the known upper/lower bounds on the true order of growth of
  S(T). Absent; "Ghosh" hits resolve to unrelated Conrey-Ghosh papers, a name collision.
- **Numerical |S(T)| bounds**: |S(T)| < 1 for T < 280, < 2 for T < 6,800,000, largest found so far not much more
  than 3. Absent; the repo only has a bound on the *integral* of S (Trudgian's), never this pointwise-value history.
- **Littlewood's zero-gap theorem**: the gaps between consecutive zeros' imaginary parts tend to 0. Absent; every
  "Littlewood" hit in the repo is his unrelated pi(x)-li(x) sign-change/Skewes theorem, a name collision.
- **Hardy-Littlewood conjectures 1 and 2**: about the spacing of real zeros of a Z(t)-type function and the
  density of odd-order zeros on long intervals. Absent; the repo's Hardy-Littlewood hits are all the unrelated
  twin-prime k-tuple conjecture, a name collision. The phrase "odd order zero" gets zero hits.
- **Selberg's zeta-function conjecture and Karatsuba's 1992 confirmation** (the "supershort intervals" result).
  Absent, no hits at all.

### Cross-cutting meta-finding: the name-collision pattern

At least ten absences above are not clean gaps but **name collisions**: the repo cites the same mathematician for
different, unrelated work (Zagier, Cartier, Suzuki/Fesenko, Odlyzko 1990, Ono-Soundararajan, Dunn-Radziwill,
Karatsuba 1996, Ghosh, Littlewood's zero-gap theorem, Hardy-Littlewood conjectures 1/2, and the Chowla/Linnik and
Nicolas-1983 misattributions noted under PARTIAL below). A keyword search for an author's surname alone would
over-report coverage; the actual paper being cited matters and was checked for each item above.

---

## 2. PARTIAL items (mentioned but not engaged)

### Equivalent criteria
- **Salem's criterion** (1953): only a single bibliography-CSV row (`docs/03_research/literature_survey/rh_full_corpus.csv`)
  citing a paper on "the Salem integral equation"; absent from every curated equivalence catalog
  (research_atlas, solutions/README).
- **Mertens conjecture** (the stronger, false |M(x)| < sqrt(x) bound, disproved by Odlyzko & te Riele 1985):
  `docs/research_atlas/README.md` and `experiments/primes/DATASETS.md` state the bound as a fact / discuss how far
  its failure has been pushed numerically, but never name Odlyzko-te Riele's 1985 disproof; the repo's "te Riele"
  hits are the unrelated 1988 de Bruijn-Newman bound paper.
- **Totient growth criterion** (n/phi(n) inequality for n >= 120569#): catalogued only in its general classical
  "Nicolas' inequality" form in `docs/research_atlas/README.md` and `docs/solutions/README.md`; the specific
  120569# (product of first 120569 primes) threshold is never spelled out.

### Consequences of RH / GRH
- **Chowla (1934), least prime in an arithmetic progression**: `docs/implications/README.md` and
  `docs/03_research/README.md` state the correct GRH-conditional bound but attribute it to "Linnik's theorem"
  rather than Chowla; Linnik's actual theorem is a different, unconditional result. Worth a citation fix if the
  project ever tightens this section.
- **Growth of Euler's totient, excluded-middle version** (Nicolas 1983): `docs/solutions/README.md` and
  `docs/research_atlas/README.md` cite a different 1983 Nicolas result (the primorial inequality
  prod(p/(p-1)) > e^gamma * ln(theta(p_k))), not the excluded-middle phi(n) theorem the Wikipedia article means.

### Attempted-proof approaches
- **Operator-theory analogy triple** (Frobenius/etale cohomology, Selberg-zeta/Laplacian, p-adic-zeta/Galois-action
  on ideal class groups): two of the three legs are genuinely deep (Frobenius/etale is core to Architecture 2;
  Selberg/Laplacian appears in `experiments/toy/README.md`); the p-adic-zeta/Galois/ideal-class-group leg is
  essentially absent beyond unrelated Iwasawa mentions.
- **Berry-Connes proposal** (half-derivative of the potential; functional determinant proportional to the Riemann
  Xi function): `experiments/spectral/e1d_arithmetic_spectral_dh.py` and
  `quantum_mechanics_signature_dossier.md` build a Berry-Keating + Connes-adele hybrid operator but never name
  "Berry-Connes" or engage the specific half-derivative/functional-determinant mechanism.
- **Schumayer & Hutchinson (2011) survey**: only a one-line bibliography annotation in `references/README.md`
  ("useful map, no new leverage"), never engaged further.
- **Turán's approach as a failed proof avenue** (as opposed to the criterion itself, listed under ABSENT above):
  same gap, the repo's Turán content is a different topic entirely.

### Zeta-analogue families
- **Dedekind zeta functions / extended Riemann hypothesis (ERH)**: only definitional one-liners in
  `docs/03_research/README.md` §6, `docs/implications/README.md`, `docs/research_atlas/README.md`; "ERH" itself
  appears only inside a surveyed external paper's abstract, never engaged as a target.
- **Grand Riemann Hypothesis / automorphic L-functions**: stated definitionally in the same doc-6 section; the
  literal term "grand Riemann hypothesis" never appears in the repo, and it is not a research target.
- **Multiple zeros of Dedekind zeta / elliptic-curve L-functions and the BSD link**: BSD's regulator/rank is
  mentioned only in passing in computational reading notes (`Cohen-1993...md`, `Cremona-...Ch3.md`); the
  central-point-multiplicity-equals-rank link and the Dedekind-zeta-as-Artin-L-function-product factorization are
  never engaged.

### Numerical-verification phenomena
- **Bohr & Landau (1914)** density estimate (almost all zeros within epsilon of the critical line): one-line
  namedrop in `docs/03_research/reading_notes/Connes-2026-RH-Past-Present-Letter.md`, no engagement with the
  o(T)-density claim itself.
- **Ivić (1985) zero-density estimates**: every "Ivić" hit in the repo cites a different, unrelated 2003 Ivić
  paper (on an ES-equivalence question); zero-density estimates are discussed generally via other authors
  (Maynard-Pratt, Guth-Maynard, Tao-Trudgian-Yang) but never attributed to Ivić's 1985 book.
- **Historical zero-computation table**: the modern lineage (Turing 1953, Lehman 1970, Rosser-Yohe-Schoenfeld 1969,
  Gabcke 1979, Odlyzko 1987, Platt, Gourdon) is cited with real cross-checked data in `experiments/primes/`; the
  pre-1953 hand-computation names (Riemann's own 1859 estimate, Gram 1903, Backlund 1914, Hutchinson 1925,
  Titchmarsh 1935, Comrie 1936) and several later ones (Lehmer's exact 1956 count, Meller, Brent, van de Lune,
  Wedeniwski/ZetaGrid, the "Odlyzko-Schönhage algorithm" by name) are absent.

### Arguments for and against
- **Lehmer's phenomenon as a doubt-argument**: the term "Lehmer pairs" is used technically (de Bruijn-Newman
  bounding, close-pair resolution in zero-counting: `experiments/positivity/3e_li_de_bruijn_newman.md`,
  `e3k_hypothetical_offline.py`), but the specific disbelief-argument and its Montgomery/Odlyzko rebuttal (that
  close pairs occur exactly as often as the pair-correlation conjecture predicts) is never discussed.
- **Survey consensus vs. skepticism** (Bombieri 2000 / Conrey 2003 / Sarnak 2005's "strong but not overwhelming"
  verdict, against Littlewood's flat disbelief and Ivić's 2008 skepticism): these are bibliography-list entries
  only (`docs/research_atlas/README.md`); their actual content is never engaged. Littlewood is cited elsewhere
  only for his 1914 oscillation theorem, never for his stated belief that RH is false. "Ivić" produces zero
  genuine hits (repo-wide grep hits are false positives on "motivic"). CLAUDE.md's Stance section and
  `docs/researcher_mindset.md` state a generic "target not monument" position and do not cite any of these
  historical figures' skeptical content by name.

---

## 3. COVERED items (compact table)

### Equivalent criteria / reformulations

| Item | File(s) | Depth |
|---|---|---|
| Riesz criterion | `docs/03_research/rh_logical_status.md`; `docs/03_research/literature_survey/rh_literature_map.md` | named as a proven equivalence, one paragraph |
| Hardy-Littlewood criterion | `docs/03_research/rh_logical_status.md` | same paragraph as Riesz, shallow |
| Nyman-Beurling criterion | `experiments/criticality/e_nb_baez_duarte_dh.py`/`.md`; `lean/ZetaRH/RHEquivalences.lean` (`nymanBeurling_criterion`) | full experiment (Gram-matrix computation) + Lean Prop |
| Baez-Duarte strengthening | same files as above | implemented as the integer-dilation restriction f_k(x) = {1/(kx)} |
| Weil's criterion | `lean/ZetaRH/ExplicitFormula.lean`; `experiments/positivity/e3c2_weil_gram.py`; `publications/weil_ground_state/`; `references/README.md` sec 10 | deepest item in this whole search: Lean theorem + experiment + publication draft (P12) + curated reference library |
| Li's criterion | `lean/ZetaRH/RHEquivalences.lean` (`li_criterion`); `experiments/positivity/e3s_li_hankel_dissolves.py`, `e3b3_rigorous.py` | Lean Prop + multiple experiments (Hankel non-PSD no-go, D-H witness at n=336,000) |
| Speiser-adjacent: (not applicable, see ABSENT) | | |
| Weak Mertens conjecture (Littlewood 1912) | `lean/ZetaRH/RHEquivalences.lean` (`mertensBound`, `mertens_criterion`); `docs/03_research/rh_logical_status.md` | formalized in Lean as M(x)=O(x^(1/2+eps)) iff RH |
| Robin's criterion | `lean/ZetaRH/RHEquivalences.lean` (`robin_criterion`); `docs/research_atlas/README.md`; `docs/solutions/README.md`; `experiments/LEARNINGS.md` #441 | Lean Prop + catalog rows + colossally-abundant-number / marginal-positivity analysis |
| Lagarias's criterion | `lean/ZetaRH/RHEquivalences.lean` (`lagarias_criterion`, `RH_arith`) | the project's own chosen Pi-0-1 arithmetic surrogate for RH; n=1,2,3 cases proved sorry-free |
| de Bruijn-Newman constant | `docs/03_research/research_directions/12_debruijn_newman_criticality.md`; `experiments/criticality/e_dbn_kernel.py`/`.md`, `e_dbn_flow_dh.py`/`.md` | dedicated dossier on Rodgers-Tao 2020 (Lambda >= 0) plus two full experiments |

### Consequences of RH / GRH

| Item | File(s) | Depth |
|---|---|---|
| von Koch's theorem | `docs/03_research/landau_one_sided.md`; `docs/01_undergraduate/README.md`; `docs/implications/README.md` | cited as load-bearing classical fact (flagged for source re-verification) |
| Schoenfeld (1976) explicit bounds | `experiments/primes/e5c_explicit_formula.py`; `experiments/primes/PRIME_PATTERNS.md`; `landau_one_sided.md` | the explicit constant is an actual computational checkpoint, not just cited |
| Lindelöf hypothesis | `docs/02_graduate/README.md` sec 7; `docs/research_atlas/README.md`; `docs/03_research/missing_object_interface.md` | deep: a named load-bearing quantity in the project's own SP-interface framework |
| Cramér / large prime gap | `docs/implications/README.md` | states the exact O((log x)^2) vs. RH-conditional O(sqrt(x) log x) contrast |
| Chebyshev's bias (Hardy-Littlewood 1917) | `experiments/primes/PRIME_PATTERNS.md` sec 3; `e5g_race_from_zeros.py`; `e5h_multichar_races.py` | computed to 10^13, quotes Rubinstein-Sarnak's GRH-conditional density against measured value |
| Weak / ternary Goldbach | `docs/implications/README.md`; `docs/03_research/parity_vs_polarization.md` | states the GRH-vs-Helfgott-unconditional distinction; Vinogradov's method separately dissected in depth |
| Hooley (1967) / Artin's conjecture | `docs/implications/README.md`; `docs/03_research/README.md` | states GRH implies Artin's primitive-root conjecture explicitly |
| Miller (1976) / AKS primality | `docs/implications/README.md`; `docs/03_research/cryptography_rh.md`; `experiments/LEARNINGS.md` #116 | substantial: Bach's bound, deterministic Miller-Rabin under GRH, AKS contrast |
| Littlewood's theorem / Skewes' number | `experiments/primes/e5c_explicit_formula.py`; `PRIME_PATTERNS.md`; `docs/implications/README.md` | explicit sign-change claim plus the ~10^316 estimate in code comments (Knapowski's follow-up not named) |

### Attempted-proof approaches

| Item | File(s) | Depth |
|---|---|---|
| Hilbert-Polya conjecture | `experiments/spectral/README.md`; `e1a_berry_keating.py`; `experiments/toy/selberg.py` | dedicated Architecture-1 thread plus a toy training ground |
| Operator-theory analogy (2 of 3 legs) | `docs/research_atlas/README.md`; `experiments/toy/README.md` | Frobenius/etale and Selberg/Laplacian legs present; p-adic/Galois leg thin (see PARTIAL) |
| Odlyzko (1987) GUE support | `docs/03_research/quantum_chaos_and_the_zeros.md`; `docs/research_atlas/README.md` | dedicated section citing height-10^20 numerics |
| Berry-Keating H=xp | `experiments/spectral/e1a_berry_keating.py`; `README.md`; `1d_connes_adele_literature.md` | full computational architecture (bare + Sierra-Townsend variants) run against the D-H discipline |
| Deninger's program | `experiments/arithmetic_geometric/2A_deninger_dossier.md`; 5 Deninger reading notes under `docs/03_research/reading_notes/` | one of the project's four core architectures, dozens of dossiers |
| Lee-Yang theorem | `docs/03_research/reading_notes/modular_hecke_sweep_2026-07-30.md`; `experiments/lemma_db/breadth_corpus.py` | engaged as the sourcing mechanism for Kurasov-Sarnak quasicrystals |
| Connes / noncommutative geometry trace formula | `docs/03_research/reading_notes/Connes-1998-Trace-Formula-NCG-Zeros.md`; `2A_R3_connes_positivity.md`; `docs/research_atlas/README.md` | the repo's single deepest classical thread; central to Architecture 2 (the "K1 wall") |
| Lapidus (2008) | `docs/03_research/reading_notes/vanFrankenhuijsen-2008-Nevanlinna-RH.md` | engaged via a citation-network read, secondary depth |
| de Branges | `experiments/arithmetic_geometric/e2db_debranges_crossterm.py`; `docs/03_research/spec_z_cohomology_landscape.md` | reproduces Conrey-Li's negative result to 12 significant figures |
| Quasicrystals / Dyson | `docs/03_research/reading_notes/modular_hecke_sweep_2026-07-30.md`; `experiments/positivity/offline_flip_test.py`; `experiments/LEARNINGS.md` #96 | graded explicitly, extensive Kurasov-Sarnak / Alon-Cohen-Vinzant engagement |
| Kurokawa (1992) multiple zeta functions | `docs/03_research/spec_z_cohomology_landscape.md`; `Deninger-I-regularized-determinants.md` | tracked as a graded candidate framework |
| Random matrix theory / quantum chaos | `docs/03_research/quantum_chaos_and_the_zeros.md`; `docs/02_graduate/log_correlated_fields_intro.md`; `deligne_weil1_engine_audit.md` | Montgomery, Katz-Sarnak, Keating-Snaith all treated under an explicit Level-3-vs-Level-4 framework |
| "2026 two-thirds of zeros" claim | see Special Note above (filed as "AF" / Alpoge-Furman) | extremely deep, multi-session, adversarially contested |

### Zeta-analogue families

| Item | File(s) | Depth |
|---|---|---|
| Dirichlet L-functions / GRH | `experiments/_shared/dirichlet_l.py`; `docs/03_research/README.md` sec 5 | full LFunction implementation (chi3/chi4), used as a positive control across dozens of experiments |
| Siegel zeros | `docs/03_research/research_directions/07_heath_brown_multi_zero_mt.md`; `experiments/LEARNINGS.md` #162 | load-bearing fact behind a sieve factor-2 ceiling result |
| Hecke L-functions | `experiments/arithmetic_geometric/e2an_sp_object_v0.md`; `LEARNINGS.md` #179 | Connes's Thm 5 (trace formula iff RH for all Hecke L-functions) is an explicit measurement target |
| Selberg class | `lean/ZetaRH/Basic.lean`; `docs/03_research/README.md` sec 6 | actual Lean membership definition plus use as a scoping discipline |
| Function field zeta / Artin-Hasse-Weil | `experiments/arithmetic_geometric/e2b_elliptic_curve_fp.py`; `e1i_metaplectic_weil_index.py` | Hasse's genus-1 case computed directly and cited by name in ~6 files |
| Weil conjectures (Deligne) | `e2b_elliptic_curve_fp.py`; `2A_weil_proof_diff.md`; `docs/solutions/README.md` | core Architecture 2; worked F_5 example, extended in `e2xx_higher_rank_rosati.py` |
| Arithmetic zeta functions of schemes | `docs/03_research/spec_z_cohomology_landscape.md` | a START HERE doc organized entirely around this generalization |
| Selberg zeta function (geodesics, genuine sense) | `docs/research_atlas/multifractal_and_log_correlated_methods.md`; `experiments/toy/README.md`; `c4_prime_orbit_spectrum.py` | dedicated trace-formula / Patterson-Sullivan section |
| Ihara zeta functions / Ramanujan graphs | `experiments/toy/ihara.py`, `ihara_grader.py`, `alon_boppana.py`; `docs/03_research/cryptography_rh.md` | whole toy-model subsystem, named "the proven function-field RH shadow" (LEARNINGS #116) |
| Iwasawa main conjecture / p-adic L-functions | `docs/03_research/rh_solved_by_accident.md` | scored table row with a specific named defect |
| Epstein zeta functions (counterexample family) | `experiments/_shared/epstein_zeta.py`; `experiments/positivity/e3l_epstein_control.py`; `experiments/LEARNINGS.md` (50+ references) | a full second independent wrong-approach detector alongside D-H, matching the Wikipedia description exactly (FE, no Euler product at class number > 1, off-line zero confirmed at d=47) |

### Numerical-verification phenomena

| Item | File(s) | Depth |
|---|---|---|
| N(T) zero-counting formula / Trudgian (2014) | `experiments/primes/e5f_rh_verification.py`, `rsz.py`, `test_primes.py` | implements N(t) formula and codes Trudgian's explicit bound, used live in the repo's own RH verification |
| Hadamard / de la Vallée-Poussin (1896) | `docs/01_undergraduate/README.md`; `docs/solutions/README.md`; `docs/02_graduate/README.md`; `PRIME_PATTERNS.md` | stated as theorem, tied to the PNT equivalence |
| Zero-free region history | `experiments/zero_free/4a_4c_vinogradov_korobov.md`; `lean/ZetaRH/LineRestriction.lean`; literature-survey docs | de la Vallee-Poussin, Vinogradov MVT, Ford 2002, Mossinghoff-Trudgian-Yang all discussed with real depth (Pace Nielsen's 2022 improvement not named by name) |
| Platt & Trudgian (2021) verification height | `experiments/primes/platt_reader.py`; `DATASETS.md`; `PRIME_PATTERNS.md` | the actual LMFDB/Platt zero archive downloaded, parsed, and cross-checked |
| Classical proportion-of-zeros chain (Hardy, Selberg, Levinson, Conrey, PRZZ) | `docs/03_research/reading_notes/proportion_support_landscape.md` | sourced table: Levinson 1/3, Conrey 2/5, BCY 0.4105, PRZZ 5/12 |
| Hardy's Z(t) / Riemann-Siegel theta(t) | `experiments/primes/rsz.py`; `experiments/_shared/zero_polish.py`, `dirichlet_l.py`, `davenport_heilbronn.py` | implemented across the whole LFunction interface |
| Turing's method | `experiments/primes/e5f_rh_verification.py`, `test_primes.py`, `PRIME_PATTERNS.md` | fully implemented as the closing half of the repo's own RH-verification pipeline |
| Gram points / Gram's law / Gram blocks / Rosser's rule | `experiments/primes/rsz.py` (`gram_point`); `e5f_rh_verification.py`; `test_primes.py`; `PRIME_PATTERNS.md` | genuine critical-line sense confirmed (not the Gram-matrix false positive); Rosser's rule implemented and cited |
| Lehmer's phenomenon (the numerical fact) | `experiments/primes/e5f_rh_verification.py`; `e3k_hypothetical_offline.py`; `3e_li_de_bruijn_newman.md`; `visualizations/research/make_figs.py` | verification code explicitly engineered around it; the exact t=7005.0-7005.2 window is plotted |

### Arguments for and against

| Item | File(s) | Depth |
|---|---|---|
| Deligne's proof as the strongest theoretical reason | `docs/research_atlas/README.md`; `deligne_weil1_engine_audit.md`; `all_roads_to_the_signature.md` | the organizing analogy for Architecture 2, audited move by move |
| Epstein zeta as the counterexample / over-generalization caution | `experiments/_shared/epstein_zeta.py`; `e3l_epstein_control.py` | built explicitly as a second wrong-approach detector, motivated the same way Wikipedia frames it |
| Numerical verification is weak evidence | `docs/implications/README.md`; `PRIME_PATTERNS.md` | explicit Littlewood-oscillation and Skewes ~10^316 citation |
| Odlyzko's GUE support tempered by "all attempts have failed" | `docs/research_atlas/README.md` sec 2.1, 2.3; `experiments/spectral/README.md` | matches the Wikipedia framing closely, including the explicit unmet-requirement language |
| GRH predictions later proved unconditional (weak Goldbach) | `docs/implications/README.md` | names the Helfgott (2013) unconditional result explicitly against the GRH-conditional predecessor |

---

## 4. References cross-check against references/README.md

`references/README.md` is a narrow, curated reading list built for specific deep-dive threads (prismatic
cohomology, the Deninger program, NCG/Connes, arithmetic topology, Hodge/intersection theory, elliptic-curve
heights, quantum gravity, Weil positivity). It is not a general RH bibliography, so the large majority of the
Wikipedia article's ~120 citations (almost all of the classical analytic-number-theory literature: Selberg,
Titchmarsh, Odlyzko's computational papers, Robin, Lagarias, Nyman, Beurling, Riesz, Speiser, Franel-Landau, Gram,
Rosser, Karatsuba, Ivic, Hardy-Littlewood, Turan, etc.) fall outside its scope by design. That is an expected
finding, not a search failure.

### Already indexed (found in references/README.md)

| Wikipedia citation | Repo file | Note |
|---|---|---|
| Connes, Alain (1999), "Trace formula in noncommutative geometry..." | `Connes-1998-Trace-Formula-in-NCG-and-Zeros-of-Riemann-Zeta.pdf` (sec 04) | same paper (arXiv math/9811068, published Selecta 1999); filename uses the arXiv year |
| Connes, Alain (2016), "An Essay on the Riemann Hypothesis" | `arxiv_1509.05576.pdf` (sec 09) | exact match |
| Connes, Alain (2026), "The Riemann Hypothesis: Past, Present and a Letter Through Time" | `Connes-2026-RH-Past-Present-and-a-Letter-Through-Time.pdf` (sec 04) | exact match, with dedicated reading notes and an assessment doc |
| Deninger, Christopher (1998), "Some analogies between number theory and dynamical systems on foliated spaces" | `Deninger-1998-ICM-...-Foliated-Spaces.pdf` (sec 02) | exact match (ICM Berlin 1998) |
| Schumayer, D.; Hutchinson, D. A. W. (2011), "Physics of the Riemann Hypothesis" | `arxiv_1101.3116.pdf` (sec 09) | exact match |

### Near misses (same author, different paper, worth flagging precisely)

- **Bombieri, Enrico (2000)**, "The Riemann Hypothesis: official problem description" (the Clay Millennium Problem
  statement) is cited by Wikipedia. The repo has `Bombieri-2000-Remarks-on-Weils-Quadratic-Functional-I.pdf`
  (sec 10), a *different* Bombieri 2000 paper (Rend. Lincei technical paper on Weil's quadratic functional). Same
  author and year, not the same work; the Clay problem statement itself is not indexed.
- **Leichtnam, Eric (2005)**, "An invitation to Deninger's work on arithmetic zeta functions" is cited by
  Wikipedia. The repo has `Leichtnam-2006-Scaling-Group-Flow-and-Lefschetz-Trace-Formula-Laminated-Spaces.pdf`
  (sec 03), a different (2006) Leichtnam paper. The 2005 survey itself is not indexed.
- **Suzuki, Masatoshi (2011)**, "Positivity of certain functions associated with analysis on elliptic surfaces"
  (the Fesenko-boundary-function paper) is cited by Wikipedia. The repo has two *other* Suzuki papers indexed,
  `Suzuki-2022-Screw-Line-of-the-Riemann-Zeta-Function.pdf` and
  `Suzuki-2026-Weils-Quadratic-Form-via-the-Screw-Function.pdf` (sec 10), on a related but distinct Weil-positivity
  program. The specific 2011 paper is not indexed. (This is the same collision noted under ABSENT for "Fesenko's
  program.")

### Also worth noting

- **Riemann, Bernhard (1859)**, the founding paper: not in `references/README.md`, but the primary source itself
  is present elsewhere in the repo, in `sources/` (`Riemann.pdf`, `Wilkins-translation.pdf`, `riemann_full.txt`,
  `riemann_original_notes.txt`). Different index, same material, genuinely present.

### Not indexed (the great majority; ~110 of ~120 citations)

Grouped, not exhaustively re-verified line by line beyond the checks above, since the negative result is uniform:
none of these appear in `references/README.md`.

Equivalence/criteria authors: Riesz (1916), Nyman (1950), Beurling (1955), Baez-Duarte (2005), Salem (1953),
Speiser (1934), Franel & Landau (1924), Robin (1984), Lagarias (2002), Massias/Nicolas/Robin (1988), Bjorner
(2011), Rodgers & Tao (2020), Newman (1976).

Consequences authors: von Koch (1901), Schoenfeld (1976), Dudek (2014), Nicely (1999), Chowla-era sources,
Weinberger (1973), Ono & Soundararajan (1997), Dunn & Radziwill (2021), Goldfeld (1985), Siegel (1935), Ireland &
Rosen (1990), Ribenboim (1996).

Attempted-proof authors: Berry & Keating (1999), Zagier (1981, 1977), Cartier (1982), Lapidus (2008), de Branges
(1992), Conrey & Li (2000), Dyson (2009), Fesenko (2010), Suzuki (2011, the specific paper), Kurokawa (1992),
Knauf (1999).

Zeta-analogue-family authors: Artin (1924), Deligne (1974, 1980), Serre (1969-1970), Weil (1948, 1949), Sheats
(1998), Wiles (2000), Radziejewski (2007), Katz & Sarnak (1999a, 1999b), Keating & Snaith (2000a, 2000b).

Numerical/zero-location authors: Backlund (1914), Gram (1903), Hutchinson (1925), Titchmarsh (1935, 1936, 1986),
Turing (1953), Lehmer (1956), Haselgrove (1958), Haselgrove & Miller (1960), van de Lune/te Riele/Winter (1986),
Rosser/Yohe/Schoenfeld (1969), Odlyzko (1987, 1990, 1992, 1998), Odlyzko & te Riele (1985), Gourdon (2004), Platt &
Trudgian (2021), Karatsuba (1984a, 1984b, 1985, 1992), Karatsuba & Voronin (1992), Ghosh (1983), Hadamard (1896),
de la Vallee-Poussin (1896, 1899-1900), Bohr & Landau (1914), Ivic (1985, 2008), Trudgian (2011, 2014), Ford
(2002), Mossinghoff/Trudgian/Yang (2022), Hanga (2020), Selberg (1942, 1946, 1956), Levinson (1974), Conrey
(1989), Pratt/Robles/Zaharescu/Zeindler (2020), Hardy (1914), Hardy & Littlewood (1921), Knapowski (1962), Spira
(1968), Borwein/Ferguson/Mossinghoff (2008), Turan (1948).

General surveys and popular expositions: Bombieri (2000, Clay version), Conrey (2003), Sarnak (2005), Littlewood
(1962), Burton (2006), Edwards (1974), Broughan (2017), Patterson (1988), Ingham (1932), Montgomery (1973, 1983),
Montgomery & Vaughan (2007), Rudin (1973), Mazur & Stein (2015), Lavrik (2001), all six "Popular expositions"
titles (Sabbagh x2, du Sautoy, Rockmore, Derbyshire, Watkins 2015, Frenkel, Nahin).

Notes-only extras (never in the References section at all): Euler (1744), Landau (1924), Titchmarsh (1927), Maier
& Montgomery (2009), Soundararajan (2009), Yu & Matiyasevich (2020), Johnston (2022), the Anthropic (2026) blog
post and Claude (2026) paper cited in Notes 44-45 (this specific pair is not in `references/README.md`, though the
underlying mathematical content is deeply covered elsewhere under "AF," see the Special Note above).
