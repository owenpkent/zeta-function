# ADVERSARY report: the F3 allow-poles survey (debranges_allow_poles_survey.md, 2026-08-26)

> Target: [`debranges_allow_poles_survey.md`](debranges_allow_poles_survey.md) (SURVEYOR, frame
> session F3), verdict NO-IN-PRINT servicing the corridor's last live reopen trigger. A
> NO-IN-PRINT that retires a live trigger is load-bearing; this round tries to overturn it and
> then grades the session under the #206 verdict wiring (the grade is the adversary's call).
> Toolchain disclosure (the second-toolchain rule): all fetches this round are my own: arXiv
> export API via `curl` (the decisive queries and all abstract re-fetches), arXiv abs HTML pages
> (a route the survey did not use for abstracts), crossref REST API (an engine the survey did not
> use at all), fresh downloads of the BBH and Burnol PDFs from arXiv AND numdam, extracted with
> `pypdf` 6.16.2 and ghostscript `txtwrite` (the survey used `pdftotext`; `pypdf` was installed
> this session, closing the survey's honest limit 6). Ten evasion probes of my own devising were
> run beyond Q1-Q17. Every quote below is from my own fetch. No em dashes.
>
> **VERDICT: PASS_WITH_FIXES.** The NO-IN-PRINT verdict replicates exactly on a second toolchain
> and two additional engines; no counterexample exists in anything found; quote fidelity is
> verbatim at every point checked (zero drift, zero fabrication); the discrepancy log is accurate
> and at one point under-claims in the dossier's own favor. Three fixable findings: the 2024-2026
> window enumeration missed three in-window extremal papers (all FITS-IN-PART, all
> verdict-CONFIRMING), Section 9 item 2 carries one overstated sentence that propagates into
> Section 10, and the Section 10 screen's clause (ii) is over-tight as a discussability gate.
> **B6 session grade: UNMOVED** (the structural finding fails the #201 derivability check;
> justification in B6).

## B1. Replication on a second toolchain + new evasion probes: GLANCED

(The attack's aim was a verdict flip; it did not land one. It landed a bounded coverage hole.)

**The decisive queries, replicated via `curl` against `export.arxiv.org/api/query` (my own
fetches, independent of the survey's WebSearch/WebFetch routes):**

| Survey claim | My replication | Match |
|---|---|---|
| `ti:"Majorants of meromorphic functions"` = math/0605052, abstract's "In other words" sentence | 1 result, math/0605052v1; abstract verbatim: "In other words, $K_B$ is the space of square summable meromorphic functions with the poles at the points $\bar z_n$." | EXACT |
| `abs:"admissible majorant"` newest-first = four entries, no allow-poles member | Exactly 4: 2410.19581 (absence result, "we demonstrate the absence of unif[orm]..."), 0906.2943 (dB spaces of entire functions), 0901.4946 (structural), math/0605052 | EXACT |
| `au:Littmann AND abs:"de Branges"` = five entries, all entire | Exactly 5 (2011.09910, 1510.08383, 1508.02436, 1406.5456, 1311.1157); zero occurrences of pole/meromorphic across all five summaries; five "entire" hits | EXACT |

Bonus corroboration the survey did not have: 0901.4946's own abstract states "the map that takes
f to f/E is an isometry of the de Branges space H(E) onto S(F_E), the orthogonal complement of
F_E H^2": an independent in-print statement of the codim-0 identification on which the whole
clause-(a) grading of the model-space corpus rests.

**My evasion probes (ten, none in Q1-Q17; arXiv API + crossref):** E1 `abs:"de Branges" AND
abs:"spectral gap"`: 0 hits. E2 `abs:"canonical system" AND abs:extremal`: 2, both irrelevant
(reflectionless operators; SUSY QM). E3 coinvariant + majorant/meromorphic: 11, all algebraic
combinatorics (wrong field). E4 `all:"Krein string" AND abs:extremal`: 0. E5 `abs:"Beurling-
Selberg" AND abs:meromorphic`: 2, graded below. E6 `abs:"one-sided approximation" AND
abs:meromorphic`: 0. E7 `abs:"de Branges" AND abs:poles`: 3, graded below. E8
`abs:"Cauchy-de Branges"`: 1 (Baranov 2206.02175: the widest meromorphic-flavored dB
generalization in print, and its own abstract keeps the class ENTIRE: "Cauchy-de Branges spaces
are Hilbert spaces of entire functions defined in terms of Cauchy transforms of discrete
measures"; content = Riesz bases + multiplication-domain density: structural, no extremal
statement). E9 Cauchy transforms + majorant/extremal/one-sided: 6, nothing new. E10
`abs:"Hermite-Biehler" AND abs:meromorphic`: 3, graded below. Crossref sweeps (C1-C3) added the
Khabibullin "theorem on the least majorant... entire and meromorphic functions" line (Izvestiya
1994 I/II): least-majorant ENVELOPE theory in growth/potential-theoretic classes, no $H(E)$, no
extension structure, no coupling data: OFF-TARGET; and the Ukrainian free-pole conformal
extremal school (nonoverlapping domains): geometric function theory, OFF-TARGET.

**The three in-window papers the sweep missed (the landed part of this attack):**

1. **Bergman, "Hörmander's Inequality and Point Evaluations in de Branges Space"
   (arXiv:2411.02226, Rev. Mat. Iberoam. 2025).** Own abstract: "We apply this result to study
   the point evaluation functional and associated extremal functions in de Branges spaces
   (equivalently in model spaces generated by meromorphic inner functions)". Genuine one-sided
   extremal content on $\mathcal H(E)$ / $K_\Theta$: clauses (b)+(c) YES, clause (a) NO (the
   meromorphic-inner referent is exactly the Section 5 codim-0 trap, and this abstract is an
   independent in-print confirmation of that referent). Grade: FITS-IN-PART. Q14's phrasing
   should have surfaced it.
2. **Chirre, Helfgott, "Optimal bounds for sums of bounded arithmetic functions"
   (arXiv:2511.14736) and "... non-negative arithmetic functions" (arXiv:2512.15709)
   (Nov/Dec 2025).** The Beurling-Selberg lineage's actual 2025 frontier, with maximally
   pole-flavored DATA: "we know the location of the poles of $A(s)$... and their residues", and
   an "explicit formula with the contribution of each pole clearly stated". But the extremal
   CLASS is the classical entire one by their own words: "optimal approximants of
   Beurling--Selberg type found in (Graham--Vaaler, 1981)" / "(Carneiro--Littmann, 2013)...
   (Vaaler, 1985)". Poles live on the target/value side, never as directions of the
   optimization space: clause (a) NO. Grade: FITS-IN-PART. Q6's shape should have surfaced them.

All three CONFIRM the verdict (the newest lineage members keep poles strictly on the data side
even when the data is nothing but poles), so the dossier's Section 5 sentence "the whole
Beurling-Selberg / Carneiro-Littmann lineage through its 2024 sign-uncertainty frontier" and
Section 1's "(ii) the 2024-2026 literature window is newly swept... nothing moved" are TRUE in
verdict and INCOMPLETE in enumeration. Also cleared by my probes, for the next WATCH screen's
inventory: the meromorphic-Hermite-Biehler corner exists in print and is zero-location/stability
theory, not extremal (1706.08552: "h(s) a meromorphic function... the only zeros of
$h(s)\pm h(1-s)$ are on the critical line"; 0712.1266 Velásquez Castañón, same family); the
Cauchy-de Branges corner (2206.02175) is structural.

**Required fix 1:** add the three papers as graded rows (FITS-IN-PART) and amend the two window
sentences; optionally log E8/E10/C1's cleared corners in Section 6.

## B2. The BBH nearest-miss grading: MISSED

Verified at source with my own arXiv fetch + `pypdf` (a route and extractor the survey did not
use). The abstract defines the class: "$K_B = H^2 \ominus BH^2$... In other words, $K_B$ is the
space of square summable meromorphic functions with the poles at the points $\bar z_n$", with
"$B$ a meromorphic Blaschke product in the upper half-plane with zeros $z_n$": so the poles sit
at the conjugates, lower half-plane, none on the axis, no mirror pair, and $K_B$ is BY
DEFINITION the model space itself (codimension zero relative to it). The body sentence is
verbatim as quoted: "the mapping $F \mapsto F/E$ is a unitary operator from $H(E)$ onto
$K_{\Theta_E}$, where $\Theta_E = E^*/E$, that is, $K_{\Theta_E} = H(E)/E$". My full-text token
scan: zero occurrences of "extension"/"enlarg"; the single "extends" is analytic continuation of
one auxiliary function, not space language. Theorem 2.6 verbatim matches the dossier's
compressed dichotomy: "either a) $1/E \in L^2(\mathbb R)$ and $1/|E|$ is (the unique up to
equivalence) positive and continuous minimal majorant for $K_{\Theta_E}$; b) $1/E \notin L^2$
and there is no positive and continuous minimal majorant". The clause-(a) reading (poles = the
$E$-normalization, codim 0, unitarily $\mathcal H(E)$, no new directions, no structural-side
pole) is confirmed three independent ways (BBH abstract, BBH body, 0901.4946's abstract). The
verdict is safe at this joint.

## B3. The structural finding (Section 9): GLANCED

**The inclusion and its direction: verified from the fetched definition.** BBH's own abstract
defines admissibility existentially: "A nonnegative function $w$ on the real line is said to be
an admissible majorant for $K_B$ if there is a non-zero function $f \in K_B$ such that
$|f| \le w$ a.e." Under any definition of this shape, $K_a \subset L_a$ (set inclusion inside
the same ambient $L^2$, $\dim L_a/K_a = 2$ by Prop. 4.5, re-fetched) gives
$\mathrm{Adm}(K_a) \subseteq \mathrm{Adm}(L_a)$ by transporting the witness. The dossier's
direction is correct, and item 1's inference is sound: a criterion for the set
$\mathrm{Adm}(L_a)$ alone is always satisfiable by base-space witnesses, so a theory that does
not isolate the quotient certifies nothing about the pole directions. The own-synthesis flag is
clean (Section 9's header says "this dossier's own derivation... not a claim found in any
source"; Section 10 and the handoff repeat the reading/proof distinction).

**The overstated sentence (the landed part).** Item 2 asserts "There is no infinite-dimensional
theory left for the literature to have missed: at this class the 'theory' reduces to finite
positive-definite linear algebra plus the coupling of the quotient to the base." The second
half of the sentence contradicts the first: the QUOTIENT DATA is finite (the measured
$B(a) = [[N, \beta], [\beta, N]]$, e1w), but membership in
$\mathrm{Adm}(L_a) \setminus \mathrm{Adm}(K_a)$ constrains $f = g + c_0 Y_0 + c_1 Y_1$
pointwise with $g$ ranging over the infinite-dimensional $K_a$, and depends on the pointwise
profiles of $Y_0, Y_1$, not only on their Gram block. Two extensions with identical $(N, \beta)$
and different evaluator profiles can have different admissibility sets. The base-coupling term
is exactly where a hypothetical extension-specific majorant theory would live, and it is not
finite-dimensional; the dossier's own handoff item 3 ("the measured $B(a)$ plus a base-coupling
term") states this correctly, so the fix is local. The overstatement propagates once: Section
10's "what would exist is finite-dimensional and already measured."

**Required fix 2:** reword item 2's flourish to scope finite-dimensionality to the quotient data
(e.g. "no infinite-dimensional POLE DATA left to miss; the surviving unknown is the
base-coupling term, which is a function-theory question, not linear algebra") and mirror the fix
in Section 10. The verdict does not rest on Section 9, so this is wording, not structure.

## B4. Quote fidelity, third fetch: MISSED

Both load-bearing quotes were re-fetched by a route neither prior reader used (fresh arXiv AND
numdam PDFs, `pypdf` extraction; the survey used numdam + `pdftotext`, e1w used ar5iv):

- BBH: "In other words, $K_B$ is the space of square summable meromorphic functions with the
  poles at the points $\bar z_n$": verbatim in my export-API fetch and in my PDF extraction.
- Burnol, in BOTH the numdam and arXiv versions, verbatim: "It appears to be useful not to
  focus exclusively on entire functions, and to allow poles, perhaps only finitely many."
  Position confirmed: directly above "Proposition 2.2 ([7, 6.10])", in Burnol's own voice.

Additional attributions spot-checked at source (arXiv abs HTML pages, a third abstract route),
all verbatim: Makarov-Poltoratski math/0702497 ("the family of Toeplitz operators
$T_{J\bar S^a}$ acting in the Hardy space $H^2$ in the upper halfplane"; note the kernel is a
subspace of $H^2$, so "kernels are $H^2$-internal" is faithful); Conrey-Li math/9812166 ("L. de
Branges proposed an approach to the Riemann hypothesis using certain positivity conditions. In
this paper, the authors examine this approach and indicate its difficulty."); Suzuki 2012.11121
("a conditional but richly general solution to the inverse problem of recovering the structure
Hamiltonian"); Carneiro-Ismoilov-Ramos 2408.01186 ("the theory of de Branges spaces of entire
functions"); Vasilyev 2203.16674 and Dellepiane-Seco 2603.03093 consistent with their table
rows. Burnol's Section 1 phrase re-fetched verbatim: "the de Branges spaces, and their
extensions allowing poles". Zero drift anywhere. Given the program's #202(v) fabricated-quote
lesson, this dossier's quotation discipline is exemplary.

## B5. The discrepancy log and the Section 10 screen: log MISSED, screen GLANCED

**Discrepancy 1 (attribution split): verified at source, and the log under-claims.** My numdam
fetch of the JTNB bibliography: "[2] L. DE BRANGES, Self-reciprocal functions, J. Math. Anal.
Appl. 9 (1964) 433-457"; "[4] L. DE BRANGES, The convergence of Euler products, J. Funct. Anal.
107 (1992)"; "[5] L. DE BRANGES, A conjecture which implies the Riemann hypothesis, J. Funct.
Anal. 121 (1994)"; and decisively "[7] J.-F. BURNOL, On Fourier and Zeta(s), 50 p.,
Habilitationsschrift (2001-2002), Forum Mathematicum, to appear (2004)". So the dossier's two
glosses of "[7, 6.10]" (Section 2: "Burnol's own Habilitationsschrift"; Section 4: "from 'On
Fourier and Zeta(s)' 6.10"), which I set out to expose as an internal inconsistency, are BOTH
correct simultaneously: the bibliography entry itself identifies the two documents. "Theorem 2.1
(De Branges [2])" and the Section 8 sentence "De Branges [4, 5] uses in his constructions the
other Sonine spaces, even 'double-Sonine' spaces" both re-fetched verbatim. The corrected
attribution (class introduced by Burnol on de Branges' Sonine spaces) is right.

**Discrepancy 2 (the caught summarizer error):** the underlying source facts are as the log
states (my three routes concur: the class IS the model space, codim 0); the caught error was in
the direction that would have flipped the verdict had it been promoted, i.e. the re-fetch
discipline demonstrably did its job. Discrepancy 3 (line counts): confirmed cosmetic (my
extractions differ again: gs 3084 lines, pypdf 66502 chars; content identical everywhere
checked). Honest limit 3 (Lagarias UNREACHED) corroborated: the session scratchpad's
`lagarias_debranges.pdf` is in fact a "ResearchGate - Temporarily Unavailable" HTML page, and my
own two additional routes (UMich pages: Cloudflare-gated; Wayback CDX: timeout, zero archived
snapshots of the guessed path) also failed. Seven failed routes total are now on record.

**The screen (Section 10), attacked both ways.** Against BBH and this round's three new
FITS-IN-PART papers the screen fires correctly: all fail (i) (no strict containment by pole
directions; Chirre-Helfgott's poles are data of the TARGET, not directions of the class). It is
falsifiable: hb1 Section 9's missing theorem transposed to the positive block would satisfy
(i)+(ii)+(iii), so a genuine theory can pass. The over-tightness: clause (ii) demands the
coupling data in the criterion or value formula, and the coda declares "anything that fails (ii)
is base-space theory in disguise." False as a classification: a paper could pose an
admissibility theory on genuine finite-pole extensions whose criterion consumes only pole
LOCATIONS and orders (the analogue of the lineage's winding criteria). That would be coupling
-blind (for $L_a$, blind to $B(a)$ and to the $|\beta|/N \to 1$ degeneration, hence not itself a
reopen), but it would be the FIRST in-print extremal theory posed on the extension class: the
event class the trigger exists to watch, and a mandatory deep read. As written, the screen
labels it non-discussable.

**Required fix 3:** split clause (ii): (ii-a) the criterion or value depends on the extension
data beyond the base space at all (locations, orders, or coupling): if yes, the paper is
DISCUSSABLE and gets a deep read; (ii-b) a REOPEN additionally requires the coupling data (for
$L_a$: $B(a)$, equivalently $(N, \beta)$) in the criterion or value formula. Only failures of
(ii-a) are "base-space theory in disguise."

## B6. The session grade under the #206 verdict wiring (the adversary's call): UNMOVED

Candidate metric items, against Section 5 of the deliberation: (a) theorem-shape at the stated
bar: NONE (a survey; Section 9 self-describes as "a structural explanation... not a proof"; no
VERIFIER draft). (d) frontier movement: NONE (the dossier says so itself). (b)/(c) turn on the
one candidate, the Section 9 structural finding ("inherited majorant theories are pole-blind;
extension-specific content is governed by the finite measured block plus base-coupling"), so I
ran the #201 derivability check on it explicitly. Decomposition: (1) the pole-blindness of
inherited theories is the positive-space instantiation of hb1 Section 7's fork, branch 1
("posed but blind": optimize against the part that ignores the extension data), which the
dossier itself cross-references as "the positive-space twin of the fork hb1 Section 7 recorded";
(2) the finite quotient and its measured Gram block are e1w verbatim (Prop. 4.5,
$\dim(L_a/K_a) = 2$; the measured $B(a)$, $|\beta|/N \to 1$); (3) the joint-pricing clause is
quoted from the trojan ledger. The composed claim is therefore WORDABLE from the entry's own
cross-refs (hb1 + e1w + the ledger) with no residue: it fails the derivability check. (Contrast
the standing PASS example, #205's "the horizon is register-relative," which was not derivable
from #172/#188.) The single genuinely new atom, the exact-form Adm-monotonicity lemma read off
the fetched Havin-Mashreghi definition, is a one-line instantiation, not a constraint. So no
metric item passes and the session grades **UNMOVED** for tripwire purposes (count: one, first
frame session). Stated for the record, per the deliberation's own wiring: this is F3's
expected-success branch ("a serviced-and-hardened trigger is frontier UNMOVED... the frame's
expected cadence, not a failure"); the serviced trigger, the fifth hardening, and the screen are
real work either way. The grade is bookkeeping, and the bookkeeping says: the corridor stays
closed, and nothing here moved the frontier.

## Required fixes (for the SYNTHESIZER; no edits applied to the dossier by this round)

1. **Window completeness (B1):** add graded rows for Bergman arXiv:2411.02226 (FITS-IN-PART:
   (a) NO, model-space referent; (b) YES; (c) YES) and Chirre-Helfgott arXiv:2511.14736 +
   arXiv:2512.15709 (FITS-IN-PART: extremal class entire per their own citations of
   Graham-Vaaler / Vaaler / Carneiro-Littmann; pole data enters the value side only); amend
   Section 1(ii)'s "nothing moved" enumeration and Section 5's "through its 2024 sign-
   uncertainty frontier" to the 2025 frontier. All three strengthen the verdict; none is a
   reopen candidate. Optionally add the cleared corners (Cauchy-de Branges 2206.02175;
   meromorphic-HB zero-location 1706.08552 / 0712.1266; Khabibullin least-majorant envelopes)
   to Section 6's probe inventory.
2. **Section 9 item 2 (B3):** replace "There is no infinite-dimensional theory left for the
   literature to have missed" with a version scoping finiteness to the quotient data and naming
   the base-coupling term as the surviving, possibly infinite-dimensional, component; mirror in
   Section 10 ("what would exist is finite-dimensional and already measured" overstates the
   same way).
3. **Section 10 screen (B5):** split clause (ii) into (ii-a) extension-data dependence =
   discussable (deep read), (ii-b) coupling-data dependence = reopen; re-scope the "base-space
   theory in disguise" coda to failures of (ii-a).
4. Cosmetic: the dossier may cite this round as closing honest limit 6 (a `pypdf` second
   toolchain now exists on this host) and extending honest limit 3's failed-route count to
   seven.

## Overall verdict on the dossier: PASS_WITH_FIXES

The load-bearing claim (NO-IN-PRINT on the joint (a)+(b)+(c), hence no reopen, fifth hardening)
survives replication on an independent toolchain, two additional engines, and ten fresh evasion
probes, including the two strongest corners the survey never named (Cauchy-de Branges spaces;
the meromorphic-Hermite-Biehler zero-location family): every candidate found keeps either the
extremal class entire, the space codimension-zero, or the content structural. The fixes are an
enumeration completion, one sentence of scoping, and one screen-clause split; none touches the
verdict. The trigger is correctly SERVICED; the session grade is UNMOVED per B6.
