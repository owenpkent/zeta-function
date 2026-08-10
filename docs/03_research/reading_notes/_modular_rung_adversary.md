# Adversary report: the 2026-08-09 modular/Hecke rung (T1 Viazovska S4 sweep, T2 $HB_1$ one-sided extremal) plus cross-consistency with e1w

> ADVERSARY report, 2026-08-09. Targets:
> T1 = [`viazovska_s4_sweep.md`](viazovska_s4_sweep.md) (verdict FITS-IN-PART),
> T2 = [`hb1_one_sided_extremal.md`](hb1_one_sided_extremal.md) (verdict NO-IN-PRINT / OPEN),
> cross-fact = [`e1w_burnol_bilinear.md`](../../../experiments/spectral/e1w_burnol_bilinear.md)
> ($\kappa(L_a) = 0$, signature $(2,0)$, #168(iii) CORRECTED). Five pre-registered attacks
> (B1-B5), each reported LANDED / GLANCED / MISSED with evidence. Web verification done at
> source this session (arXiv abstracts, ar5iv full texts, and an independent re-download of
> Kaltenbäck-Woracek Parts V and VI from the author's page with a re-run vocabulary grep).

## Summary of verdicts

| Attack | Verdict | One-line evidence |
|---|---|---|
| B1 citation spot-check (T1) | MISSED | BRS 2005.02996 Theorem 1.1 confirmed UNCONDITIONAL at source, multiplicities handled; RV 1701.00265 Theorem 2 and 2211.09044 dim-6 non-sharpness both verified verbatim |
| B2 verdict discipline (T1) | GLANCED | FITS-IN-PART is defensible and internally honest, but strictly at $\{k\log p\}$ no Q4 condition is met; calibration annotation recommended |
| B3 citation spot-check (T2) | MISSED | Independent re-download + re-grep of K-W Parts V and VI replicates every zero-hit claim; no vocabulary-evasion content found |
| B4 cross-consistency (e1w) | GLANCED | No contradiction on where the Euler product enters (three-way agreement); T2's forcing question needs rescoping annotations, which its own honest-limits block anticipated |
| B5 style/evidence gates | MISSED | Zero em dashes in T1/T2/e1w; tags and honest-limits blocks present; no machine-local citations in either target |

| Target | Overall verdict |
|---|---|
| T1 `viazovska_s4_sweep.md` | **PASS_WITH_FIXES** (two annotation-level fixes: the "Riemann-Weil recovered as a consequence" tag downgrade, the verdict-calibration line; no substantive error found) |
| T2 `hb1_one_sided_extremal.md` | **PASS_WITH_FIXES** (content verified; fixes are the e1w rescoping annotations, all in the direction T2's own honest limit 5 pre-registered) |

## B1: citation spot-check on T1. MISSED

**Main check, the flagged discrepancy (BRS conditionality).** Fetched arXiv:2005.02996 at
source (abstract page + ar5iv full text). Adjudication:

- Theorem 1.1 is stated **unconditionally**. The full text explicitly associates with each
  zero $\rho$ "the multiplicity $m(\rho)$ of the zero of $\zeta(s)$ at $\rho$" and the
  formula carries derivative terms $\sum_{j=0}^{m(\rho)-1} f^{(j)}((\rho-1/2)/i)\,V_{\rho,j}(z)$.
  No RH or simplicity hypothesis appears in the theorem.
- The exact-criticality sentence T1 cites is verbatim in the paper: "both Theorem 1.1 and
  the above corollary are rather sensitive to the choice of interpolation points and break
  down if one removes any single point."
- Therefore T1's fetch is CORRECT and the discrepancy resolves in T1's favor:
  [`kns_log_growth_pin.md`](kns_log_growth_pin.md) Section 1.3's "assuming the Riemann
  hypothesis and simplicity of zeroes" is Kulikov-Nazarov-Sodin's own citing description
  (accurately quoted by the pin), and that description does not match BRS Theorem 1.1 as
  printed; it plausibly describes a cleaner simple-zeros variant. The annotation belongs in
  the pin, not in T1 (proposed line below).

**Second check (RV 1701.00265 Theorem 2).** Verified at ar5iv source: $\Psi(f) =
(f(\sqrt n))_{n\ge0} \oplus (\hat f(\sqrt n))_{n\ge0}$ is "an isomorphism of the space of
even Schwartz functions onto the vector space $\ker L \subset \mathfrak s \oplus \mathfrak s$"
with $L((x_n),(y_n)) = \sum_{n\in\mathbb Z} x_{n^2} - \sum_{n\in\mathbb Z} y_{n^2}$.
Perfect-square indices confirmed at source; the unique relation is classical Poisson
summation $\sum f(n) = \sum \hat f(n)$. T1's reading, including the subscript fidelity note
it flagged about itself, is correct.

**Third check (LP non-sharp in dim 6).** Verified at arXiv:2211.09044 abstract, verbatim:
"We prove that the Cohn-Elkies linear programming bound for sphere packing is not sharp in
dimension 6. The proof uses duality and optimization over a space of modular forms,
generalizing a construction of Cohn-Triantafillou..." Authors: de Courcy-Ireland, Dostert,
Viazovska. T1's SECONDARY-tier claim is confirmed and could be upgraded to FETCHED-abstract.

**One fidelity nuance (sub-LANDED, folded into T1's fix list).** T1 Section 2 asserts as
fetched: "Riemann-Weil is recovered as a consequence when the $\log n$ side is contracted
against von Mangoldt weights." The paper's own wording is softer and does not mention von
Mangoldt weights at that point: "we may think of (1.1) as arising from (1.2) in the
following way: The left-hand side of (1.1) defines a linear functional on $\mathcal H_1$,
while the right-hand side gives the representation of this functional with respect to the
basis functions of Theorem 1.1," framed as complementary "multiplicative and additive
duality relations." The substance (RW is tied to the basis as a functional representation)
survives; the von-Mangoldt-contraction mechanism is T1's interpretive gloss and should be
tagged as gloss, not fetch. This does not touch the verdict or the Section 5 pricing
argument, whose logic needs only "the RW pairing and the BRS basis live on the same node
duality," which is confirmed.

## B2: verdict discipline on T1. GLANCED

**Does FITS-IN-PART follow from the four-condition scoring as written?** Strictly at the
spec's own node set $\{k\log p\}$ ([`../theta_s4_build_spec.md`](../theta_s4_build_spec.md)
Section 1), NO condition is met by the corpus: (1) and (4) fit at the corpus's NATIVE
quadratic nodes, (3) is split with the informative half negative, and (2) at log nodes is
shown by T1's own Section 5 to be M4 verbatim. A stricter scorer could therefore return
"MISFIT at the spec's node set; mechanism-class existence proof at foreign nodes." T1 is
not hiding this: its verdict line itself says the transfer "IS the Riemann-Weil explicit
formula, and its one-sided version IS Weil positivity = M4," and Section 7 distinguishes
mechanism-class fit from transfer misfit explicitly. The risk is downstream
verdict-vocabulary drift (a future reader taking "FITS-IN-PART" as "partially viable
route"). Calibration annotation proposed below; not LANDED because no evidence contradicts
the dossier's own account, which is complete and honest.

**Was the DMV screen actually applied?** Yes, mechanically: Section 3 condition (4)
partitions the corpus into density-only parts (KNS, power-node uniqueness: pre-killed,
carrying no S4 content) and the magic-function mechanism, whose lattice consumption is
localized at three named sites (eigenfunction property = Poisson over $\mathbb Z$; vanishing
locations = integer $q$-exponent support; sign control = $q$-coefficients). That is an
application, not a citation.

**Is the Beurling screen answered with a mechanism?** Yes: the named failing clause is at
the construction step ($\tau \mapsto \tau + 2$ presupposes $\mathbb Z$-support; no discrete
group, no finite-dimensionality, no rigidity, no wholesale vanishing), quantitatively
anchored to e1m's T5 defect $0.37$ and e1q's $0.368$, and boundary-confirmed from the
positive side by Radchenko-Stoller 2108.11828 (arithmetic decides, density never does).
This is a mechanism, not an assertion.

## B3: citation spot-check on T2. MISSED

**Independent replication of the K-W sweep.** Parts V and VI were re-downloaded this
session from the author's own page (`haraldworacek.github.io/homepage/Downloads/JournalPapers/2011/51.pdf`,
93 pages, and `.../2010/48.pdf`, 40 pages; both URLs resolve, confirming T2's path
fragments are live site paths, not dead local links), text-extracted independently (pypdf,
not T2's pdftotext), and grepped. Results, matching T2's Section 3 table exactly:

| Token | Part V | Part VI |
|---|---|---|
| majorant / majoriz / extremal / one-sided / minorant | 0 / 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 / 0 |
| Beurling / Selberg / Burnol / Sonine / Malliavin | 0 / 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 / 0 |
| admissible | 2 (+1 bibliography) | 1 |

The admissible hits are exactly what T2 reported: Part V "admissible partition" (of a
Hamiltonian's domain; the third hit is a bibliography title on "admissibility"), Part VI
"for all admissible values of $r_-, r_+$" (a commuting-diagram condition). **Vocabulary
evasion probe:** additional greps for one-sided content under nonstandard tokens
(dominat*, subharmonic, superharmonic, envelope, "best approximation", "upper bound for",
pointwise) returned ZERO hits in both parts. No extremal content found under any
vocabulary; the papers are purely spectral (monodromy/Weyl/Fourier transform theory and
the indefinite inverse spectral theorem), as their abstracts say.

**Downstream claim (Baranov-Woracek majorization strictly classical).** arXiv:0906.2943
abstract fetched: "subspaces of de Branges spaces of entire function generated by
majorization... Banach spaces generated by admissible majorants." Entire-function setting,
no Pontryagin/indefinite/negative-square vocabulary anywhere in the abstract. Consistent
with T2's full-text finding (strict $HB_0$ inequality at its extraction line 36); nothing
contradicts "strictly $HB_0$."

## B4: cross-consistency with e1w. GLANCED (annotations required, no contradiction)

**T2's verdict stability.** NO-IN-PRINT / OPEN is a statement about the literature (does a
one-sided extremal theorem for $HB_\kappa$, $\kappa \ge 1$ exist in print). It is
logically independent of whether $L_a$ inhabits $HB_1$, so e1w's $\kappa(L_a) = 0$ does
not touch the verdict. T2's honest limit 5 pre-registered exactly this exposure ("$L_a$'s
realization in $HB_1$ is itself still candidate tier... Everything here about '$L_a$ in
$HB_1$' inherits that caveat"). VERDICT STANDS.

**What does need rescoping in T2** (all annotation-level, none verdict-touching):

1. The framing (title block, Section 1) presents the question as sharpened by $L_a$'s
   candidate-tier $\kappa = 1$; e1w corrects that to $\kappa = 0$ at source tier, so the
   $HB_1$ question loses its only named RH-side instance and drops from "THE sharpened
   question of this corridor" to "a standalone literature gap" (e1w Section 9.2's words).
2. Section 7(b)'s illustration ("For the $L_a$-shaped instance the mirror-pole pair
   $\{s=0,1\}$... is precisely a candidate one-pair complex part") is now counterfactual
   for $L_a$ itself: the literal extension block is a positive Gram block, not indefinite
   spectral data. The illustration survives only as an abstract $HB_1$ shape.
3. Handed-forward item 1 lists "the additive-ansatz verification" as one of two live
   BUILDER moves; e1w IS that verification and it fired CORRECTED, so the item is
   discharged (outcome: negative for the ansatz) and the Section 9 forcing question, while
   still well-posed, is now unmotivated by any known object. Its blindness dichotomy
   remains a good screen if an $HB_1$ instance ever appears.
4. Section 10's "TRIPLE-hardened" corridor closure is consistent with e1w and in fact
   strengthens: e1w closes the indefinite repair route AT SOURCE (Section 9.3), a fourth
   hardening.

**T1's handed-forward question vs e1w.** No conflict. T1's BRS-skeleton rank/cost probe
targets the FE-sourced economy at $\{\log n\}$ vs $\{k\log p\}$ with the zero side
symbolic; e1w's "no arithmetic discrimination" finding concerns Burnol's pole-coupling
block (FE + interval-constancy data only, no Euler product), a different object. The probe
design is if anything REINFORCED by e1w: e1w demonstrates concretely that FE-plus-pole
structure alone carries no zeta-vs-fake discrimination, which is the same null hypothesis
T1's probe pre-registers ("the economy prices as the explicit formula's zero side").

**Where the Euler product enters: the three documents AGREE.** This was the pre-registered
contradiction hunt; it found a three-way agreement instead. T1 Section 5.3: restricting
$\{\log n\} \to \{k\log p\}$ costs precisely the Euler product (von Mangoldt contraction),
one-sidedness costs precisely M4. T2 handed-forward item 3: a construction equally happy on
the D-H mirror pair "has consumed only the mirror geometry, not the Euler product." e1w
Section 8: the block consumes FE + constancy data, NO Euler product ($\zeta$-loading enters
$L_a$ only through the co-Poisson subspace, unused). All three place the Euler product at
the contraction/loading joint, never in the FE/pole geometry, consistent with the
trojan-ledger conservation law. No contradiction = attack does not land; the agreement
itself is worth one LEARNINGS line.

## B5: style and evidence gates. MISSED (both targets pass)

- **Em dashes:** zero occurrences of the character in T1, T2 (grep over the whole
  `reading_notes/` directory) and in e1w's dossier.
- **Sourcing:** T1 tags every source with an arXiv ID and tier, and its honest-limits
  block explicitly marks the one at-risk claim "UNSOURCED if quoted" (CKMRV relations
  uniqueness). T2 tags [FETCHED]/[SECONDARY]/[REPO] per claim; the K-W parts carry journal
  references plus live author-page paths (no arXiv versions exist for them; acceptable).
- **Honest-limits blocks:** present and substantive in both.
- **Evidence rule:** neither T1 nor T2 cites scratchpad or machine-local paths. T2's
  `Downloads/JournalPapers/...` fragments are live paths on the cited author page
  (verified by successful re-download); a portability fix (prefix the full
  `haraldworacek.github.io/homepage/` base once in the sources table) is suggested but not
  required. OUT-OF-SCOPE OBSERVATION for SYNTHESIZER: the parent dossier
  [`la_negative_square_check.md`](la_negative_square_check.md) (lines 258-259) DOES cite a
  machine-local scratchpad path (`C:\Users\owenp\AppData\...\la_negative_square_numerics.py`),
  a violation of the CLAUDE.md evidence rule on a different-machine profile; since e1w has
  now superseded that computation at source tier, the cheapest cure is an annotation there
  pointing to e1w rather than recovering the script.

## Proposed SYNTHESIZER annotations (exact lines; verdicts untouched)

1. **[`kns_log_growth_pin.md`](kns_log_growth_pin.md) Section 1.3**, append:
   "Adjudicated 2026-08-09 (ADVERSARY, [`_modular_rung_adversary.md`](_modular_rung_adversary.md) B1):
   BRS 2005.02996 Theorem 1.1 is unconditional with multiplicities $m(\rho)$ handled by
   derivative terms, per direct source fetch; the 'assuming RH and simplicity' wording is
   KNS's citing description and does not match the printed theorem. This pin's quote of KNS
   is accurate; KNS's characterization of BRS is not."
2. **T1 STATUS block**, append: "Verdict calibration (ADVERSARY 2026-08-09): read
   FITS-IN-PART as 'FITS as mechanism class at native quadratic nodes / M4-EQUIVALENT as a
   transfer to $\{k\log p\}$'; strictly at the spec's node set no Q4 condition is met, so
   this corpus is an existence proof for the S4 economy, not a candidate route around M4."
3. **T1 Section 2 (BRS paragraph)**: retag the "Riemann-Weil is recovered as a consequence"
   sentence as fetched-plus-gloss; the paper's wording is "we may think of (1.1) as arising
   from (1.2)" via functional representation, and the von Mangoldt contraction is this
   repo's interpretive mechanism, not the paper's sentence.
4. **T2 STATUS block**, append: "e1w cross-fact (2026-08-09, landed after this dossier):
   $\kappa(L_a) = 0$ at source tier, so the motivating instance evaporates exactly as
   honest limit 5 anticipated. The verdict NO-IN-PRINT / OPEN stands unchanged (it is a
   statement about the literature). The Section 9 missing theorem is downgraded from 'the
   corridor's sharpened question' to 'a standalone literature gap with no known RH-side
   instance'; handed-forward item 1's additive-ansatz verification is DISCHARGED by e1w
   with outcome CORRECTED; the live successor question is e1w Section 11's positive
   meromorphic 'allow poles' extremal question."
5. **LEARNINGS** (when the #168 downgrade annotation e1w requested is written), add the
   B4 agreement line: "The 2026-08-09 rung's three documents independently place the Euler
   product at the same joint (the contraction/loading step: von Mangoldt contraction in
   BRS, co-Poisson loading in Burnol, the D-H mirror-pair tariff), never in the FE/pole
   geometry: a three-way confirmation of the trojan-ledger conservation law from the
   modular, de Branges, and adversarial sides."
6. **[`la_negative_square_check.md`](la_negative_square_check.md)** (out of scope but
   cheap): annotate the machine-local script citation as superseded by
   [`e1w_burnol_bilinear.py`](../../../experiments/spectral/e1w_burnol_bilinear.py)
   (tracked), curing the evidence-rule violation without recovery.

## Final verdicts

- **T1 [`viazovska_s4_sweep.md`](viazovska_s4_sweep.md): PASS_WITH_FIXES.** All spot-checked
  citations verified at source (BRS unconditionality adjudicated in its favor; RV Theorem 2
  and dim-6 non-sharpness verbatim-confirmed). Fixes: annotations 2 and 3 above.
- **T2 [`hb1_one_sided_extremal.md`](hb1_one_sided_extremal.md): PASS_WITH_FIXES.** The
  K-W sweep replicated independently including an evasion-vocabulary probe; verdict stable
  under e1w. Fixes: annotation 4 above (rescoping, pre-registered by its own honest
  limits).
- PASS means survives these attacks; ADVERSARY can only falsify, not confirm.
