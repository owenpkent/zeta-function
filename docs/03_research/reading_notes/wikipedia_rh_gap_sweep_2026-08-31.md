# Wikipedia RH article vs this repo: coverage sweep, gaps, and pulled sources

> Sweep executed 2026-08-30/31 against the live Wikipedia "Riemann hypothesis" article
> (32-page print of 2026-08-30). Method: full inventory of the article's named criteria,
> consequences, approaches, zeta-analogues, numerics, and references, then a spelling-variant
> grep sweep of docs/, experiments/, lean/, and the top-level ledgers, with the high-stakes
> classifications re-verified by hand against the ledger. Full item-by-item table:
> [`_evidence/wikipedia_rh_gap_table_2026-08-31.md`](_evidence/wikipedia_rh_gap_table_2026-08-31.md).
> Companion acquisitions this round: datasets (DATASETS.md sections 18 to 21, commit d6bfd37)
> and seventeen papers filed as [`references/README.md`](../../../references/README.md) section 11.
> No em dashes anywhere.

## 1. Verdict

The repo covers every load-bearing section of the article, and on several topics it is
substantially ahead of the article's own depth: Epstein zeta functions are not just cited but
built as a second wrong-approach detector ([`e3l_epstein_control.py`](../../../experiments/positivity/e3l_epstein_control.py),
off-line zero confirmed at $d = 47$); Ihara zeta / Ramanujan graphs are a whole toy subsystem
(LEARNINGS #116); Dyson's quasicrystal suggestion is graded through the Kurasov-Sarnak
correction (#210); Kurokawa's multiple zeta functions are a scored framework row; and the
article's headline 2026 development (section 3 below) is one of the repo's most heavily
adversarially-worked threads. The gaps that remain are real but peripheral to the spine:
none of them names a proof route the four-level framing has not already placed.

## 2. Correction to the evidence file

The automated pass's "Special Note" claims the repo "found a structural problem" with the
2026 two-thirds result. That phrasing is wrong and the evidence table carries it verbatim;
this dossier is the corrected record. What the ledger actually shows: the repo VERIFIED the
result's Lean artifact (zeta-23-lean tag v1.0, five checklist items, inspection tier,
[`af_lean_repository_skim.md`](af_lean_repository_skim.md)) and then CLASSIFIED the method
relative to its own certificate frames (out-of-pool under the original F2a posing via the
funding read, in-class after the prescribed re-pose; LEARNINGS #211-#213). Classification
relative to our frames is not a defect in the theorem.

## 3. The 2026 record, article vs repo

The article's "Zeros on the critical line" section records the August 2026 unconditional
result: more than two thirds of the zeros lie on the critical line ($N_0^*(T,2T)/N(T,2T) \ge 2/3$,
distinct zeros), obtained by an unreleased research version of Claude working with human
researchers, abandoning Levinson mollification for a pair-correlation route through Weil's
explicit formula, with an improved constant from an optimized test family. This is the same
event the repo engages as AF (Alpoge-Furman, arXiv:2608.13637; deep read in
[`alpoge_furman_two_thirds.md`](alpoge_furman_two_thirds.md), constants 0.6725 / 0.8362 under
the Montgomery-Taylor window). No discrepancy between the article's claims and the repo's
assessment was found. New this round: the primary PDF itself is now filed
(`references/11_surveys_and_proven_analogues/anthropic_2026_two_thirds_zeros.pdf`).

## 4. Confirmed gaps, tiered

Recorded as candidate specs only. Nothing here is scheduled: per the PHASE_STATE
frameless-window guard, scheduling belongs to the successor-frame deliberation. Each Tier 1
item is a door with a named question whose either answer is a coordinate.

### Tier 1: candidate work items

**4.1 Goss zeta functions (Sheats 1998; Diaz-Vargas / Polanco-Chi).** A proven RH-analogue
absent from the repo. The proof mechanism is Newton-polygon combinatorics of power sums in
characteristic $p$: no positivity, no cohomology, no spectral pairing anywhere in it. The
question with teeth for [`all_roads_to_the_signature.md`](../all_roads_to_the_signature.md):
is this a genuinely sign-free road to an RH statement, or is the Goss "critical line" analogy
too weak for the convergence to claim jurisdiction? The expected resolution is the second,
and making it precise (place the Goss setting against the S1-S7 skeleton and the disqualifier
battery of [`breadth_program.md`](../breadth_program.md)) would sharpen the boundary of the
all-roads claim instead of leaving it implicit. Sources pulled (references section 11).

**4.2 The Fesenko-Suzuki two-dimensional adelic road.** Fesenko's 2D Tate's thesis on a
regular model of an elliptic curve produces a zeta integral whose boundary term is the
Laplace transform of a K-Bessel series; NON-positivity of that series' fourth log-derivative
suffices for the Hasse-Weil RH of the curve, and Suzuki (arXiv:math/0703052) proves it
necessary under technical assumptions. So this is a second concrete sign-condition-implies-RH
reduction outside the Weil quadratic form, aimed at a degree-2 sibling (exactly the
instrument class #210 built). The question: does the boundary term consume the Euler product
and the additive lattice at one joint (the conservation law of
[`trojan_horse_m4.md`](../trojan_horse_m4.md)), or is it FE-side structure? A D-H / Beurling
read of the construction is the test, and Suzuki is already a live interlocutor of the xi arc
(#179-#191), which makes this the most connected of the gaps. Sources pulled.

**4.3 An $S(T)$ measurement probe (candidate id e5g).** The article's strongest
numerics-skepticism argument is quantitative: $S(T)$ has average size about
$(\log\log T)^{1/2}$, is unbounded, jumps by at least 2 at any RH counterexample, and has
never been observed much above 3. The repo has the data to measure this properly and the
theorem the measurement would illustrate (no prime-side or statistics-side observable can see
RH; PRIME_PATTERNS). Spec: compute $S(T)$ across the certified range to $5 \times 10^7$ and
inside the three new Platt windows at heights $3.7 \times 10^8$, $3.3 \times 10^9$,
$3.06 \times 10^{10}$ (DATASETS.md section 18); report max $|S|$ per window and the growth of
the second moment against the Selberg / Ghosh $\log\log T$ scale; write the jump-by-2
mechanism as the quantitative companion of the existing hiding law (an off-line zero needs
$S(T)$ excursions no computation has approached). Pre-registration at probe time: expect
max $|S| < 3$ in every window.

**4.4 A Speiser probe on the D-H control (cheap).** Speiser's theorem: RH is equivalent to
$\zeta'(s) \ne 0$ in $0 < \operatorname{Re}(s) < 1/2$. Question: is the equivalence FE-only?
Test: compute zeros of the Davenport-Heilbronn derivative near its known off-line zeros
($\rho \approx 0.8085 + 85.699i$). If left-of-line derivative zeros appear (expected), the
Speiser coordinate is another FE-consequence the D-H discipline files as RH-blind in the same
bin as scattering unimodularity; if they do not, Speiser engages more than the functional
equation and earns a deeper look. Either way it is a new measured row in the reformulation
ledger, at the cost of one `_shared` probe.

### Tier 2: ledger paragraphs, no new machinery

- **False positivities adjacent to RH.** The Polya and Turan positivity conjectures, each of
  which would have implied RH, are both false (Haselgrove 1958; first sign changes located
  computationally by Borwein-Ferguson-Mossinghoff 2008, pulled). Conrey-Li 2000 (pulled)
  calibrates from the other side: natural Li-orbit positivity conditions exist that do not
  imply RH/GRH. Together they belong in the trojan-horse ledger's orbit as the two-sided
  caution: near-RH positivity is neither automatically true nor automatically sufficient.
  The disciplines already enforce this structurally; these are the classical citations.
- **Denjoy's probabilistic heuristic plus the Maier caveat** (probabilistic arguments in
  number theory sometimes fail): one paragraph for PRIME_PATTERNS' framing of why
  $M(x) = O(x^{1/2+\epsilon})$ randomness-talk is heuristic only.

### Tier 3: catalogued, no action

Named in the article, absent or thin here, judged not proof-route-relevant now (full list and
one-line statements in the evidence table): Franel-Landau / Farey, Redheffer matrix, Bjorner's
lattice criterion, Landau's function (Massias-Nicolas-Robin), totient thresholds and Nicolas
1983, the Hecke-Deuring-Mordell-Heilbronn excluded-middle chain and Siegel 1935, Dudek's
explicit gap bound, $\zeta(1+it)$ growth within a factor of 2, Gronwall, Weinberger's idoneal
numbers, Odlyzko 1990 discriminant bounds, Ono-Soundararajan, Dunn-Radziwill / Patterson,
Zagier 1981 (pulled; flagged as adjacent to the repo's Eisenstein / scattering thread),
Karatsuba's short-interval theorems and the Selberg zeta conjecture literature, Bohr-Landau,
the Hardy-Littlewood real-zero conjectures, Littlewood's zero-gap theorem, the pre-1953
verification lineage (Gram, Backlund, Hutchinson, Titchmarsh, Turing), Lehmer's phenomenon as
a doubt argument with Odlyzko's rebuttal, and the Cartier bug anecdote.

## 5. Fixes applied this round

- [`../README.md`](../README.md): the least-prime-in-progression bound was labelled
  "Linnik's theorem with sharp constant"; it is the GRH-conditional sharpening, Linnik's
  theorem being the unconditional $q^{O(1)}$ statement. Reworded.
- [`references/README.md`](../../../references/README.md) section 11: seventeen sources filed
  (the two Clay statements, Conrey / Sarnak / Dyson / Ivic surveys and counter-brief, Sheats
  and Diaz-Vargas-Polanco-Chi, Suzuki and Fesenko, Conrey-Li, Lagarias, Hejhal-Odlyzko on
  Turing's method, Odlyzko-te Riele, Borwein-Ferguson-Mossinghoff, Matiyasevich's register
  machine, Zagier 1981, and the Anthropic record paper).
- Attribution noted but not changed: DATASETS.md section 13 references the Mertens
  conjecture's failure without naming Odlyzko-te Riele 1985; the primary source is now in
  references section 11 either way.
