# Does a one-sided extremal theorem exist for the indefinite Hermite-Biehler class $HB_1$? The #168(iii) sharp question answered

> SURVEYOR dossier, 2026-08-09. Answers the question posed by LEARNINGS #168(iii) and
> [`PHASE_STATE.md`](../../../PHASE_STATE.md) next-step 1: now that Burnol's $L_a$ is a
> candidate-tier instance of the Kaltenbäck-Woracek indefinite framework in the mildest class
> $HB_1$ (one negative square, the mirror-pole mechanism of
> [`la_negative_square_check.md`](la_negative_square_check.md)), does a one-sided
> extremal/majorant theorem exist for $HB_1$ specifically? Parent documents:
> [`la_negative_square_check.md`](la_negative_square_check.md) (the $\kappa=1$ computation),
> [`bbh_majorant_repair_rung.md`](bbh_majorant_repair_rung.md) (the majorant-lineage
> NOT-REPAIRABLE finding, whose residual 1 named K-W Parts II/III/V/VI as unread),
> [`../s4_cheap_falsifiers_survey.md`](../s4_cheap_falsifiers_survey.md) (falsifier 2, the #164
> corridor closure this dossier does NOT reopen).
>
> **STATUS.** Date 2026-08-09. Three-way verdict: **NO-IN-PRINT, with the missing theorem now
> well-posed (so: NO for the literature, OPEN as a forcing question).** All six parts of
> Kaltenbäck-Woracek "Pontryagin spaces of entire functions" are now read or full-text-grepped
> (Parts II, III, V, VI newly fetched this session; Parts I, IV previously): **zero
> majorant/extremal/one-sided content anywhere in the series.** The downstream
> Baranov-Woracek majorization line and the Beurling-Selberg extremal lineage are classical
> ($E \in HB_0$, entire, positive kernel) at every instance checked. The indefinite corner
> (Krein-Langer, indefinite strings, $N_1$ structure theory) contains only TWO-SIDED results
> (moment problems, Padé, inverse spectral), pre-excluded by guard (i). The structural
> obstruction is named at the exact step (Section 7): every classical one-sided proof passes
> through positivity of quadrature weights $K(t,t)^{-1}$ and positivity of the spectral
> measure, and one negative square destroys both at a finite, located set. Per guard (iii),
> the well-posedness finding is recorded: unlike #164's kill (ill-posedness), in $HB_1$ the
> extremal problem FORKS into a posed-but-blind version and a data-sensitive-but-unposed
> version (Section 7), and the sharpest well-posed missing theorem is stated in Section 9.
> **The #164 reopen condition does NOT fire** (Section 10).
>
> **e1w cross-fact (2026-08-09, landed after this dossier; ADVERSARY
> [`_modular_rung_adversary.md`](_modular_rung_adversary.md) B4):** $\kappa(L_a) = 0$ at
> source tier ([`e1w_burnol_bilinear.md`](../../../experiments/spectral/e1w_burnol_bilinear.md)),
> so the motivating instance evaporates exactly as honest limit 5 anticipated. The verdict
> NO-IN-PRINT / OPEN stands unchanged (it is a statement about the literature). The Section 9
> missing theorem is downgraded from "the corridor's sharpened question" to "a standalone
> literature gap with no known RH-side instance"; handed-forward item 1's additive-ansatz
> verification is DISCHARGED by e1w with outcome CORRECTED; the live successor question is
> e1w Section 11's positive meromorphic "allow poles" extremal question.
>
> Method discipline: every load-bearing claim tagged [FETCHED] (read at source this session,
> PDF downloaded and converted with `pdftotext`, or ar5iv/abstract read directly), [SECONDARY]
> (search snippet, citing source, or abstract-level fetch summary), [REPO] (carried by an
> existing repo dossier), or flagged as this note's own derivation. No em dashes.

## 1. The question, restated precisely

[`la_negative_square_check.md`](la_negative_square_check.md) computed (candidate tier) that
Burnol's zeta-loaded Sonine space $L_a$ (poles of the completed Mellin transform at exactly
$s=0,1$, a mirror pair about the critical line, Burnol arXiv:math/0203120 Prop. 2.2) costs
exactly one negative square: the $2\times 2$ evaluator block is
$\begin{pmatrix}0&-\rho\\-\bar\rho&0\end{pmatrix}$, signature $(1,1)$ for every nonzero
coupling. So if $L_a$ enters the Kaltenbäck-Woracek framework at all, it enters through
Theorem 5.3 of Part I in the mildest indefinite class $HB_1$. The question this dossier
answers: does any one-sided extremal theorem (Beurling-Selberg majorant/minorant,
Carneiro-Littmann-type $L^1(|E|^{-2}dx)$ optimization, admissible-majorant existence) exist
in print for $E \in HB_1$, or for any $HB_\kappa$ with $\kappa \ge 1$? Pre-registered guards:
(i) two-sided results (interpolation, moment problems, inverse spectral) do not count as YES;
(ii) density-only results are pre-killed by the DMV screen
([`../s4_carrier_audit.md`](../s4_carrier_audit.md) Section 3); (iii) well-posedness in
$HB_1$ is itself a finding worth recording; (iv) #164 reopens only if a majorant theory
literally poses on $L_a$.

## 2. Sources

| Source | Reference | Tier | What it gives |
|---|---|---|---|
| Kaltenbäck, Woracek, "Pontryagin spaces of entire functions II" | Integral Equations Operator Theory 33(3) (1999) 305-380; author PDF `Downloads/JournalPapers/1999/18.pdf` | [FETCHED] (full download, `pdftotext`, 4274 lines; abstract + Sections 1-2 + Prop. 4.6 read; full-text greps) | Isometric embedding of dB-Pontryagin spaces into $L^2(\phi)$ "in a distributional sense"; the indefinite inverse spectral theorem for Nevanlinna functions; Definitions 2.1-2.2 (the structure of the indefinite spectral data, load-bearing for Section 7) |
| Kaltenbäck, Woracek, "... III" | Acta Sci. Math. (Szeged) 69 (2003) 241-310; `2003/22.pdf` | [FETCHED] (full download, 3542 lines; abstract + intro read; greps) | Degenerate dB-subspaces, singularities of maximal chains of matrix functions, continuity of intermediate Weyl coefficients |
| Kaltenbäck, Woracek, "... V" | Acta Sci. Math. (Szeged) 77 (2011) 223-336; `2011/51.pdf` | [FETCHED] (full download, 5980 lines; abstract + intro read; greps) | Monodromy matrix, Weyl coefficient, and Fourier transform for indefinite canonical systems |
| Kaltenbäck, Woracek, "... VI" | Acta Sci. Math. (Szeged) 76 (2010) 511-560; `2010/48.pdf` | [FETCHED] (full download, 2605 lines; abstract + intro read; greps) | The indefinite Inverse Spectral Theorem (de Branges' theorem, Pontryagin version) |
| Kaltenbäck, Woracek, "... I" | Integral Equations Operator Theory 33 (1999) 34-97; `1999/17.pdf` | [FETCHED] (re-downloaded this session; Def. 5.1, Thm. 5.3 proof environment, Lemma 5.4 read directly) | $HB_\kappa$ definition; the kernel-diagonal sign behavior and the real-zero divisor Lemma 5.4 (load-bearing for Section 7) |
| Baranov, Woracek, "Majorization in de Branges spaces II. Banach spaces generated by majorants" | Collect. Math. 62 (2011) 27-55; `2011/54.pdf`; arXiv:0906.2943 | [FETCHED] (full download, 1960 lines; abstract + axioms read; greps) | The majorization series' setting: classical Hilbert dB space, $E \in HB$ with the strict inequality on all of $\mathbb C^+$ (line 36 of the extraction); zero occurrences of Pontryagin/indefinite/negative-square/meromorphic/pole |
| Baranov, Woracek, "Majorization in de Branges spaces I. Representability of subspaces" | arXiv:0906.2939 | [SECONDARY] (arXiv listing; same-series setting) | Part I of the same classical series |
| Baranov, Woracek, "Majorization in de Branges spaces III. Division by Blaschke products" | Algebra i Analiz 21(6) (2009) 3-46; St. Petersburg Math. J. 21(6) (2010) 843-875 | [SECONDARY] (search-level; series context) | Blaschke division INSIDE the classical Banach-space setting; not a pole-tolerant or indefinite extension |
| Baranov, Woracek, "De Branges' theorem on approximation problems of Bernstein type" | J. Inst. Math. Jussieu 12(4) (2013) 879-899; `2013/58.pdf` | [FETCHED] (full download, 1358 lines; abstract read; greps) | Weighted sup-norm DENSITY characterization (Krein-class entire function); density-type, pre-killed by guard (ii) even if it had been indefinite, which it is not |
| Woracek, "De Branges spaces and growth aspects" | Springer Reference, Oper. Theory chapter; `2015/71.pdf` | [FETCHED] (full download, 2049 lines; all Pontryagin/indefinite hits inspected) | Survey; ZERO majorant mentions; every Pontryagin mention is a citation of two-sided results (Krein-Langer indefinite Hamburger/Stieltjes moment problems, Langer-Woracek indefinite Hamiltonians) |
| Woracek, "Existence of zerofree functions $N$-associated to a de Branges Pontryagin space" | Monatsh. Math. 162 (2011) 453-506 | [REPO] ([`bbh_majorant_repair_rung.md`](bbh_majorant_repair_rung.md) Section 4, read at source 2026-07-17) | The single known co-occurrence of "Pontryagin" and "admissible majorant": Def. 6.6 / Prop. 6.8 stated for $E \in HB_0$ only |
| de Snoo, Winkler, Wojtylak, "Zeros of nonpositive type of generalized Nevanlinna functions with one negative square" | arXiv:1011.2081 | [FETCHED] (abstract at source) | $N_1$ structure: exactly ONE generalized zero of nonpositive type (GZNT) in the closed extended upper half-plane; no extremal content. Load-bearing for Section 9's missing-theorem statement |
| Littmann, Spanier, "Extremal functions with vanishing condition" | Constr. Approx. 42 (2015) 209-237; arXiv:1311.1157 | [SECONDARY] (abstract-level fetch) | Classical $\mathcal H(E)$ extremal problem WITH a prescribed vanishing at a non-real point $\alpha = ia$; the value formula $\int_{\mathbb R}(M^+-M^-)\,|E(x)|^{-2}dx = 1/(a^2 K(0,0))$; the nearest classical template for Section 9 |
| Carneiro, Littmann (, Vaaler), extremal series | arXiv:1008.4969, 1406.5456, 1508.02436, 1412.1050 | [REPO] + [SECONDARY] (hypotheses pinned at source in [`../s4_cheap_falsifiers_survey.md`](../s4_cheap_falsifiers_survey.md); 1412.1050 confirmed same lineage by search) | Entire Hermite-Biehler structure function required throughout (Theorem 1 hypotheses (P1)-(P4)); no meromorphic or indefinite variant anywhere in the series |
| Gonçalves (et al.), "The Beurling-Selberg box minorant problem" and adjacent | arXiv:1702.04579 etc. | [SECONDARY] (search-level) | Multidimensional classical Beurling-Selberg; Paley-Wiener / entire type classes; no indefinite variant |
| Eckhardt, Kostenko (indefinite strings); Krein, Langer (indefinite moment problems); Dijksma school | e.g. "The classical moment problem and generalized indefinite strings," Integral Equations Operator Theory (2018); Krein-Langer Beiträge Anal. 14/15 (1979/80); arXiv:2002.07456 (indefinite Stieltjes + Padé) | [SECONDARY] (search-level, abstracts) | The indefinite corner's entire output is two-sided: moment problems, continued fractions / Padé approximants, inverse spectral theorems. Guard (i) excludes all of it from YES |
| Woracek publications index | `haraldworacek.github.io/homepage/Content/publications.html` | [FETCHED] | The complete series PDF paths and the majorant/extremal-titled sublist swept above |

## 3. The Kaltenbäck-Woracek series is now CLOSED as a search target

The named unread residual (BBH dossier Section 7 residual 1, narrowed by
[`la_negative_square_check.md`](la_negative_square_check.md) to "$HB_1$ specifically") is
fully discharged. All four remaining parts were downloaded from the author's own page and
grepped in full [FETCHED]:

| Part | Content (from its own abstract) | "majorant" | "extremal" | "one-sided" | "minorant" |
|---|---|---|---|---|---|
| II | isometric embeddings into distributional $L^2(\phi)$; indefinite inverse spectral theorem | 0 | 0 | 0 | 0 |
| III | degenerate dB-subspaces; singularities of maximal chains; intermediate Weyl coefficients | 0 | 0 | 0 | 0 |
| V | monodromy matrix / Weyl coefficient / Fourier transform for indefinite canonical systems | 0 | 0 | 0 | 0 |
| VI | the indefinite Inverse Spectral Theorem | 0 | 0 | 0 | 0 |

(The two "admissible" hits in Part V and one in Part VI were inspected directly: "admissible
partition" of a Hamiltonian's domain and "admissible values of $r_-, r_+$", unrelated to
majorants [FETCHED].) Also: zero occurrences of "Beurling," "Selberg," "Burnol," or "Sonine"
in any of the six parts [FETCHED, direct grep, Parts I-III, V, VI this session; Part IV's
zero-majorant grep was banked by [`bbh_majorant_repair_rung.md`](bbh_majorant_repair_rung.md)].
Combined with the Part I and Part IV zero-hit greps already on record, **the entire six-part
series contains no one-sided extremal or majorant theorem of any kind.** The series' output
is spectral: existence/uniqueness of the operator model (I, IV), the indefinite inverse
spectral theorem (II, VI), singularity structure (III), and the transform theory (V). All of
it is two-sided in the sense of guard (i).

## 4. The downstream Woracek/Baranov majorization line: classical at every instance

The complete majorant-titled sublist of Woracek's own publications page was swept:

- **Majorization in de Branges spaces I/II/III** (2009-2011): Part II read at source
  [FETCHED]; its axioms are the classical Hilbert (dB1)-(dB3) and its $HB$ definition
  carries the strict classical inequality $|E(\bar z)| < |E(z)|$ on all of $\mathbb C^+$
  (i.e. $HB_0$; extraction line 36). Zero indefinite vocabulary in the full text. Parts I
  and III are the same series in the same setting [SECONDARY]. Part III's "division by
  Blaschke products" is an operation on the majorant-generated Banach space inside a
  classical $H(E)$, not a pole-tolerant ambient extension.
- **Subspaces of / Finite-dimensional de Branges subspaces generated by majorants** (2009):
  already read for the BBH dossier [REPO]; classical $E$, zero indefinite vocabulary.
- **De Branges' theorem on approximation problems of Bernstein type** (2013) [FETCHED]:
  weighted sup-norm density characterization. Not one-sided, and density-type: guard (ii)
  pre-kills this shape regardless.
- **De Branges spaces and growth aspects** (Springer survey) [FETCHED]: zero majorant
  mentions; all six indefinite/Pontryagin mentions are citations of two-sided theory
  (Krein-Langer indefinite Hamburger/Stieltjes moment problems; Langer-Woracek indefinite
  Hamiltonians; Kaltenbäck-Winkler-Woracek generalized strings).
- **Woracek 2011 ($N$-associated zerofree functions)** [REPO]: the one genuine co-occurrence
  of "Pontryagin" and "admissible majorant" in the literature, and its majorant criterion
  (Def. 6.6 / Prop. 6.8) is stated for $E \in HB_0$ only. This dossier re-confirms (by
  completing the series sweep) that nothing later in the same school upgrades it to
  $HB_\kappa$.

## 5. The Beurling-Selberg extremal lineage: entire Hermite-Biehler throughout

Nothing on the extremal side has moved past the entireness axiom that #164 identified:
Carneiro-Littmann-Vaaler Gaussian subordination (1008.4969), Carneiro-Littmann de
Branges-space extremal theory I/II (1406.5456 Theorem 1 hypotheses, pinned at source in
[`../s4_cheap_falsifiers_survey.md`](../s4_cheap_falsifiers_survey.md); 1508.02436), the
truncated/odd-function paper (1412.1050), Gonçalves' box-minorant line (1702.04579), and
Littmann-Spanier's vanishing-condition paper (1311.1157) all pose on classical
$\mathcal H(E)$, $E$ entire Hermite-Biehler, positive reproducing kernel [REPO + SECONDARY].
The single structurally interesting item is Littmann-Spanier: it solves a classical extremal
problem with an EXTRA interpolation-type constraint at a non-real point, and its value
formula degrades gracefully ($1/(a^2 K(0,0))$, the constraint node entering through the
kernel). That is the classical template closest in shape to what an $HB_1$ theorem would
need (Section 9); it is not itself such a theorem.

## 6. The indefinite corner: everything is two-sided (guard (i))

The genuinely indefinite literature adjacent to $N_1$/$HB_1$ was swept for a one-sided
statement: Krein-Langer's indefinite Hamburger and Stieltjes moment problems (Beiträge Anal.
1979/80), the indefinite Stieltjes moment problem with Padé approximants (arXiv:2002.07456),
Eckhardt-Kostenko's generalized indefinite strings and their moment-problem correspondence,
Langer-Winkler generalized strings, and de Snoo-Winkler-Wojtylak's $N_1$ structure theory
(arXiv:1011.2081) [all SECONDARY at abstract/search level, 1011.2081 abstract FETCHED].
Every result found is interpolation-type or inverse-spectral-type: given data, reconstruct
or parametrize the object. **No source poses an optimization over a pointwise-inequality
cone.** Per guard (i), none of this counts toward YES, and none of it was promoted.

One structure fact from this corner is banked for Section 9 [FETCHED, 1011.2081 abstract]:
a $q \in N_1$ has **exactly one generalized zero of nonpositive type (GZNT)** in the closed
extended upper half-plane. The indefinite data of an $HB_1$ space is concentrated at one
located point.

## 7. The structural obstruction, named at the exact step (this note's own synthesis)

Why is the slot empty? Not by accident. Two independent positivity inputs of every classical
one-sided proof fail at $\kappa = 1$, both at a finite, located set. Flagged as this note's
own derivation, assembled from [FETCHED] statements:

**(a) The quadrature-weight step.** Classical Beurling-Selberg/Carneiro-Littmann proofs
convert the objective into a quadrature: $\int_{\mathbb R} (F-f)\,|E(x)|^{-2}dx =
\sum_t (F-f)(t)\,K(t,t)^{-1}$ over interpolation nodes $t$, and one-sidedness enters ONLY
through "all weights $K(t,t)^{-1} > 0$, so $F \ge f$ pointwise implies the integral bound."
In a dB-Pontryagin space the diagonal $K(z,z)$ is NOT of one sign: the proof of Part I's
own Theorem 5.3 must explicitly choose a point $w_0$ with $K(w_0,w_0)\,\mathrm{Im}\,w_0 > 0$
[FETCHED, Part I, proof of Thm. 5.3], because the choice is not free in the indefinite case;
and real zeros of $E$ (forbidden in $HB_0$, allowed in $HB_\kappa$ with
$\mathrm{Ord}_x E = d(P)(x)$, Lemma 5.4 [FETCHED]) can destroy the node set itself. One
negative square means at least one node can carry a negative weight, and the pointwise cone
no longer maps into the objective's positive cone. This is the "specific step" the task's NO
branch asked for.

**(b) The spectral-measure step.** Part II's Definitions 2.1-2.2 [FETCHED] describe exactly
what replaces the positive measure $|E(x)|^{-2}dx$ in the indefinite setting: a distribution
$\phi$ that is a positive (possibly unbounded) measure OFF a finite singular set $s(\phi)$,
plus a "complex part" supported on a finite $\mathbb R$-symmetric set $B \subset \mathbb C
\setminus \mathbb R$ of conjugate pairs. For the $L_a$-shaped instance the mirror-pole pair
$\{s=0, s=1\}$ (conjugate about the structural axis) is precisely a candidate one-pair
complex part. The indefinite Parseval identity therefore decomposes the objective into
(positive integral) + (signed finite-rank functional at the mirror pair), and a pointwise
inequality on the structural axis says nothing about the finite-rank term.

**The well-posedness fork (the guard (iii) finding).** Unlike #164's kill, which was an
ill-posedness (the machinery's hypotheses literally exclude the object), in $HB_1$ the
extremal problem CAN be posed, in two inequivalent ways, and the fork is the finding:

1. **Posed but blind.** Optimize only against the positive part ($\int (F-f)\,d\phi_+$,
   the measure off $s(\phi)$, ignoring the complex part). Well-posed; but the objective is
   then invisible to exactly the finite-rank data that distinguishes $L_a$ from $K_a$. This
   is the Pontryagin-side twin of the BBH blindness already on record
   ([`bbh_majorant_repair_rung.md`](bbh_majorant_repair_rung.md) Section 3: the winding-rate
   theory is in scope but $O(1)$-blind to the pole pair).
2. **Data-sensitive but unposed.** Optimize the full indefinite pairing. Then the objective
   is not bounded below on the constraint cone a priori (the negative direction is in the
   space), and one-sidedness does not couple to it: no minimum exists to be a theorem about,
   unless an extra constraint controls the finite-rank part.

This fork is a conservation-law echo of the trojan ledger
([`../trojan_horse_m4.md`](../trojan_horse_m4.md)): positivity of the objective and
sensitivity to the pole data can be had separately for free; having both at once is exactly
the priced joint. The classical literature sits entirely in the first branch's degenerate
case ($s(\phi) = \emptyset$, $B = \emptyset$).

## 8. Is $L_a$ in scope of anything found?

No. Every extremal theorem found requires $E$ entire and classical ($HB_0$); every
indefinite framework found proves two-sided theorems only. $L_a$'s candidate entry point
into the indefinite framework remains Theorem 5.3 of Part I (converse direction, no
hypotheses beyond $E \in HB_\kappa$), via the unverified additive-ansatz realization of
[`la_negative_square_check.md`](la_negative_square_check.md); but there is no extremal
theorem waiting on the other side of that door. No source found cites Burnol together with
any majorant/extremal vocabulary (re-confirmed by search this session; and the six K-W parts
contain no Burnol/Sonine mention [FETCHED]).

## 9. The missing theorem, sharpest well-posed form (candidate-tier forcing question)

The survey's product: the empty slot can now be stated as a precise target rather than an
absence. Combining the $N_1$ GZNT uniqueness [FETCHED, 1011.2081] with the Littmann-Spanier
vanishing-condition template [SECONDARY, 1311.1157]:

> **Missing theorem ($HB_1$ one-sided extremal, not in print anywhere found).** Let
> $E \in HB_1$ with no real zeros, $P(E)$ its dB-Pontryagin space (Part I Thm. 5.3), and let
> the indefinite spectral data of $P(E)$ (Part II Defs. 2.1-2.2) consist of a positive
> measure $\mu$ on $\mathbb R$ plus a complex part concentrated at the single conjugate pair
> $\{w_1, \bar w_1\}$ associated with the one negative square (equivalently, at the unique
> GZNT of $q = E^\#/E \in S_1$-data). Let $f$ be a target in the truncation/signum family.
> **Claim to prove or refute:** among entire $F$ of the growth class of $P(E)^2$ with
> $F \ge f$ on $\mathbb R$ AND the interpolation side-condition $F - f$ vanishing to order
> $\ge 2$ at $w_1$ (the constraint that annihilates the finite-rank signed term), there is a
> unique minimizer of $\int_{\mathbb R}(F - f)\,d\mu$, given by interpolation at the shifted
> node set, with the extremal value carrying the coupling $\rho$ of the negative square
> explicitly.
>
> Inputs: $E \in HB_1$, its spectral data $(\mu, w_1, \rho)$, target $f$. Outputs: extremal
> $F$, value formula in which $\rho$ appears (the non-blindness certificate). Failure mode
> to check first: whether the vanishing side-condition collapses the problem back to a
> classical one for the pole-cleared companion $s(1-s)M(f)$, in which case the theorem would
> be true but content-free, the third blindness in the series (BBH winding, KNS frame, and
> then this).

Two honest notes on this statement. First, the side-condition is exactly the trojan tariff
in miniature: it buys back positivity by spending the pole data at a named joint, so the
value formula either carries $\rho$ (content) or does not (blindness); which one is a sharp,
checkable dichotomy and the real question. Second, this is a FORCING QUESTION for a future
BUILDER/ADVERSARY round, not a conjecture this dossier asserts; the Littmann-Spanier
template makes the classical half of the construction look mechanical, and the indefinite
half (does the quadrature survive one negative weight when the constraint kills the node?)
is precisely where it would live or die.

## 10. Consequence for #164: the reopen condition does NOT fire

Guard (iv) is discharged in the expected direction. The reopen condition is "a majorant
theory that poses on $L_a$" literally. This dossier's finding is the opposite: the last
unread corners of the only candidate framework (K-W Parts II, III, V, VI) contain no such
theory, the downstream school never poses one, and the extremal lineage never leaves
$HB_0$. The corridor closure is now TRIPLE-hardened on the majorant side (the #164
category-error kill, the BBH NOT-REPAIRABLE rung, and this series-complete zero). The one
new thing is directional, not a reopening: the missing theorem is now well-posed (Section
9), so any future firing of the reopen condition has a precise shape to be checked against.

## Discrepancy log

1. **Journal-volume order of K-W Parts V and VI.**
   [`bbh_majorant_repair_rung.md`](bbh_majorant_repair_rung.md)'s sources table lists
   "V, VI: ibid. 76, 77", implying Part V in vol. 76 and VI in 77. The author's own
   publications page [FETCHED] has the reverse: Part VI in Acta Sci. Math. (Szeged) 76
   (2010) 511-560, Part V in 77 (2011) 223-336 (Part VI appeared in print before Part V).
   Cosmetic, no verdict touched; flagged for the record, not silently fixed there.
2. No substantive disagreement found between this sub-corpus and the repo's existing
   analyses; every prior claim re-encountered ([`bbh_majorant_repair_rung.md`](bbh_majorant_repair_rung.md)'s
   Woracek-2011 $HB_0$-only reading, [`la_negative_square_check.md`](la_negative_square_check.md)'s
   Part I zero-majorant grep) re-verified in this session's independent fetches.

## Honest limits

1. Parts II, III, V, VI were read at abstract/introduction depth plus targeted passages
   (Part II Defs. 2.1-2.2 and Prop. 4.6 directly) and FULL-TEXT grepped for the extremal
   vocabulary; they were not read line by line. A one-sided theorem hiding under
   nonstandard vocabulary (no "majorant"/"extremal"/"one-sided"/"minorant"/"admissible"
   token) would evade the grep. Judged unlikely (the abstracts describe purely spectral
   content) but not excluded.
2. The Beurling-Selberg sweep leaned on the repo's prior at-source pinning of
   Carneiro-Littmann's hypotheses plus abstract-level checks of the newer papers
   (1412.1050, 1702.04579, 1311.1157 [SECONDARY]); none of the newer ones was read in full.
   Their titles, abstracts, and citing descriptions all place them in classical
   $\mathcal H(E)$.
3. Section 7 (the obstruction) and Section 9 (the missing theorem) are this note's own
   synthesis from [FETCHED] ingredients; no source states either. In particular, whether
   the GZNT of the $L_a$-shaped $q$ coincides with the mirror-pole location $w_1$ is
   plausible but UNVERIFIED (it is the natural reading of the de Snoo-Winkler-Wojtylak
   abstract against the Section 5 model of
   [`la_negative_square_check.md`](la_negative_square_check.md), not a computed fact).
4. The Lagarias book chapter ("Hilbert spaces of entire functions and Dirichlet
   $L$-functions") remains UNREACHED (not re-attempted this session; four failed routes on
   record from 2026-07-17). Still open as a possible independent commentary.
5. $L_a$'s realization in $HB_1$ is itself still candidate tier (the additive-ansatz gap,
   [`la_negative_square_check.md`](la_negative_square_check.md) Section 7 gap 1). Everything
   here about "$L_a$ in $HB_1$" inherits that caveat.

## Handed forward

**Verdict for the #168(iii) question: NO-IN-PRINT / OPEN.** No one-sided extremal theorem
exists for $HB_1$ (or any $HB_\kappa$, $\kappa \ge 1$) anywhere found, the whole K-W series
now being swept; the obstruction is the positivity of quadrature weights and of the spectral
measure, both destroyed at a finite located set by one negative square (Section 7); the
problem is nevertheless well-posable, and the sharpest missing theorem is stated in Section
9 with its content-vs-blindness dichotomy pre-registered.

1. **For ORCHESTRATOR/SYNTHESIZER:** the $HB_1$ literature question is CLOSED as a survey
   target. The residual ladder (BBH residual 1, narrowed by #168(iii)) is fully discharged;
   #164 stays closed; no reopen fires. What remains on this thread is not reading, it is
   building: the Section 9 forcing question and the additive-ansatz verification
   ([`la_negative_square_check.md`](la_negative_square_check.md) handoff item 2) are the
   only live moves, and both are BUILDER-shaped.
2. **For BUILDER (if the Section 9 question is ever picked up):** run the blindness check
   FIRST. Before constructing the extremal function, test whether the vanishing
   side-condition at $w_1$ makes the problem equivalent to a classical extremal problem for
   the pole-cleared companion. If it does, the theorem is content-free and the round should
   close in one page; only if $\rho$ survives into the value formula is the construction
   worth building. The Littmann-Spanier value formula ($1/(a^2K(0,0))$) is the template for
   what "carrying the data" looks like.
3. **For ADVERSARY:** the D-H/Beurling discipline applies to any future $HB_1$ extremal
   construction in the standard way: D-H's off-line zero pair is ALSO a mirror pair about
   the critical line, so a construction that produces a "one-sided theorem" equally happy on
   the D-H analogue has consumed only the mirror geometry, not the Euler product, and is
   structurally wrong for RH purposes. The mirror-pair mechanism is FE-side data; this is
   the same tariff line item as always.
4. **The reusable pattern:** the well-posedness fork of Section 7 (posed-but-blind vs
   data-sensitive-but-unposed) is a general-purpose screen for any future "extend a
   positive-cone optimization into an indefinite setting" proposal in this program: ask
   which branch the proposal lives on before reading further. Three instances are now on
   record (BBH winding-blindness, KNS frame-vs-collapse, this fork), all the same shape:
   the classical machinery either excludes the indefinite data or cannot see it.

## Adversary note (2026-08-09)

Full report: [`_modular_rung_adversary.md`](_modular_rung_adversary.md). Verdict
**PASS_WITH_FIXES**. Findings:

1. **The K-W sweep replicated independently (B3).** Parts V and VI were re-downloaded from
   the author's page (both path fragments in the sources table resolve live) and re-grepped
   with an independent toolchain (pypdf, not pdftotext): zero hits for
   majorant/majoriz/extremal/one-sided/minorant and for Beurling/Selberg/Burnol/Sonine/
   Malliavin in both parts, matching Section 3's table exactly. The admissible hits are as
   described ("admissible partition", Part V; "admissible values of $r_-, r_+$", Part VI).
   An evasion-vocabulary probe (dominat*, subharmonic, superharmonic, envelope, "best
   approximation", "upper bound for", pointwise) returned zero hits: no one-sided content
   hides under nonstandard vocabulary. Baranov-Woracek 0906.2943's abstract confirms the
   entire-function classical setting.
2. **Cross-fact from e1w ([`e1w_burnol_bilinear.md`](../../../experiments/spectral/e1w_burnol_bilinear.md)),
   landed after this dossier: $\kappa(L_a) = 0$, signature $(2,0)$, at source tier.** The
   verdict NO-IN-PRINT / OPEN STANDS unchanged (it is a statement about the literature,
   independent of $L_a$), and honest limit 5 pre-registered exactly this exposure. Rescoping
   required, not reversal: (i) the Section 9 missing theorem loses its only named RH-side
   instance and downgrades from "the corridor's sharpened question" to a standalone
   literature gap; (ii) Section 7(b)'s "$L_a$-shaped instance" illustration is now
   counterfactual for $L_a$ itself (the literal extension block is a positive Gram block),
   surviving only as an abstract $HB_1$ shape; (iii) handed-forward item 1's
   "additive-ansatz verification" is DISCHARGED by e1w with outcome CORRECTED; the live
   successor is e1w Section 11's positive meromorphic "allow poles" extremal question;
   (iv) Section 10's closure is consistent with e1w and further hardened by it (the
   indefinite repair route is now closed at source, a fourth hardening).
3. **No Euler-product contradiction (B4).** This dossier's handed-forward item 3, T1's
   Section 5.3 pricing, and e1w's Section 8 typing all place the Euler product at the
   contraction/loading joint (von Mangoldt contraction, co-Poisson loading, the D-H
   mirror-pair tariff respectively), never in the FE/pole geometry: a three-way agreement
   consistent with the trojan-ledger conservation law.
