# Repairing the majorant machinery past Burnol's codim-2 pole pair: the first #164 reopen-condition rung

> SURVEYOR dossier, 2026-07-17. Runs pivot rung (i) named in
> [`../../../TODO.md`](../../../TODO.md) ("Open, the corridor and its pivot" section) and in
> [`PHASE_STATE.md`](../../../PHASE_STATE.md)'s falsifiability triggers: the first of the two named
> #164 reopen conditions, "a meromorphic majorant theory that poses on $L_a$." Parent document:
> [`../s4_cheap_falsifiers_survey.md`](../s4_cheap_falsifiers_survey.md) Sections 1.2-1.3 and 4, whose
> falsifier-2 finding (ILL-POSED: Carneiro-Littmann's machinery requires an entire Hermite-Biehler
> structure function; Burnol's zeta-loaded Sonine space $L_a$ is meromorphic with simple poles at
> $s=0,1$, Burnol arXiv:math/0203120 Prop. 2.2, $\dim(L_a/K_a)=2$, Prop. 4.5) closed the corridor
> conditional on two residuals. This dossier resolves residual 1 only. Residual 2 (the
> Kulikov-Nazarov-Sodin space definition pinned against $\{k\log p\}$'s growth) is rung (ii), out of
> scope here.
>
> **STATUS.** Date 2026-07-17. Verdict: **NOT-REPAIRABLE-AS-SEARCHED**. No framework was found, in
> either the admissible-majorant/model-space literature or the Kaltenbäck-Woracek Pontryagin-space
> de Branges literature, that poses (let alone solves) a one-sided extremal or admissible-majorant
> problem on Burnol's $L_a$ or on any entire (or genuinely indefinite) companion object built from it.
> Two precise nearest misses are named in Section 7, each with a specific, structural reason it does
> not reach the target, not a bare absence. **Consequence: this HARDENS the #164 closure.** Reopen
> condition (i) does not fire. The corridor stays closed as a proof home on this rung; reopen
> condition (ii) (the KNS pin) remains the only live escape, unresolved by this dossier.
>
> Method discipline: every load-bearing claim is tagged [FETCHED] (read at source this session, via
> ar5iv HTML or via direct PDF-to-text extraction of a downloaded primary source, both cross-checked
> against each other where both were available), [SECONDARY] (read via a citing paper's bibliography,
> a publisher abstract page, or a search-engine snippet, not the primary text directly), or flagged
> explicitly as this survey's own unsourced derivation. No claim is promoted across tiers. No em
> dashes.

## 1. The question

Section 4 of [`../s4_cheap_falsifiers_survey.md`](../s4_cheap_falsifiers_survey.md) named two cheap
residuals rather than treating falsifier 2's ILL-POSED verdict as unconditional. Residual 1, restated
precisely: is there a known mathematical framework, anywhere in the admissible-majorant literature or
the indefinite/Pontryagin-space de Branges literature, that poses a genuine one-sided extremal
(Beurling-Selberg / Carneiro-Littmann-type) problem on a Hilbert space of the exact shape Burnol's
$L_a$ has, namely a classical (entire, Hermite-Biehler) de Branges space $K_a$ extended by a
finite-dimensional (here 2-dimensional) space of functions whose natural transform-side
representation is meromorphic with fixed poles (here at $s=0,1$)? Four sub-threads were searched, as
specified by the parent task: (1) the Havin-Mashreghi / Baranov-Havin / Baranov-Borichev-Havin (BBH)
admissible-majorant lineage; (2) Kaltenbäck-Woracek's Pontryagin-space de Branges theory and adjacent
finite-rank-extension frameworks; (3) whether anyone, including Burnol himself, executes the
"multiply by $s(1-s)$" pole-clearing trick and tracks what happens to a majorant/extremal problem
under it; (4) whether Lagarias or Burnol, in a survey-level piece, flags the pole pair as a named
obstruction with a citable repair.

## 2. Sources

| Source | arXiv / DOI | Tier | What it gives |
|---|---|---|---|
| Baranov, Borichev, Havin, "Majorants of meromorphic functions with fixed poles" | arXiv:math/0605052, Indiana Univ. Math. J. 56(4) (2007) 1595-1628 | [FETCHED] (ar5iv HTML + full local pdftotext extraction of the downloaded arXiv PDF, cross-checked) | The meromorphic-model-space admissible-majorant theory; built for $\Theta = \exp(iaz)B(z)$ with $B$ a Blaschke product with zeros tending to infinity; the whole theory is organized around the asymptotic growth rate (the "winding") of $\arg\Theta$ |
| Havin, Mashreghi, "Admissible majorants for model subspaces of $H^2$, Part I: slow winding of the generating inner function" | Canad. J. Math. 55(6) (2003) 1231-1263 | [FETCHED] (title and full citation read directly from Woracek 2011's own bibliography, ref [17]; internal theorem content is [SECONDARY], via search snippets and via BBH/Baranov-Woracek's own descriptions of it) | Founding admissible-majorant theory for model subspaces; the "slow winding" half |
| Havin, Mashreghi, "Admissible majorants for model subspaces of $H^2$, Part II: fast winding of the generating inner function" | Canad. J. Math. 55(6) (2003) 1264-1301 | [FETCHED] (citation, as above); internal content [SECONDARY] | The "fast winding" half; both papers' own titles are the load-bearing fact used here |
| Baranov, Havin, "Admissible majorants for model subspaces, and arguments of inner functions" | Funct. Anal. Appl. 40(4) (2006) 249-263 | [FETCHED] (citation read from Woracek 2011's bibliography, ref [3]); internal content [SECONDARY] | Extends Havin-Mashreghi; majorants expressed via the argument (winding) of the inner function |
| Baranov, Woracek, "Subspaces of de Branges spaces generated by majorants" | Canad. J. Math. 61(3) (2009) 503-517 | [FETCHED] (abstract read at source via publisher page; cited in full, ref [BW], inside the companion paper below, whose full text was read) | Classical entire $E$ only; defines $\mathcal R_\omega(E)$, the de Branges subspace cut out by a majorant condition |
| Baranov, Woracek, "Finite-dimensional de Branges subspaces generated by majorants" | Oper. Theory Adv. Appl. 188 (2009) 37-48 | [FETCHED] (full text, downloaded PDF converted locally with `pdftotext` and read directly) | "Finite-dimensional" modifies the majorant-*generated subspace* $\mathcal R_\omega(E)$, not the ambient space; $E\in HB$ (classical Hermite-Biehler) throughout; zero occurrences of "Pontryagin," "meromorphic," "indefinite," "negative square," or "pole" anywhere in the paper |
| Kaltenbäck, Woracek, "Pontryagin spaces of entire functions I-VI" | I: Integral Equations Operator Theory 33(1) (1999) 34-97; II: ibid. 33(3) (1999) 305-380; III: Acta Sci. Math. (Szeged) 69(1-2) (2003) 241-310; IV: ibid. 72(3-4) (2006) 709-835; V, VI: ibid. 76, 77 | Part IV [FETCHED] (full text, downloaded PDF converted locally, read in full, 6776 lines); I, II, III, V, VI [SECONDARY] (search snippets and the series' own cross-citations only, not read at source) | Generalizes de Branges' theory to a Pontryagin-space (finite negative index) setting; Part IV specifically is about indefinite canonical systems / Hamiltonians, not directly about majorants |
| Woracek, "Existence of zerofree functions $N$-associated to a de Branges Pontryagin space" | Monatsh. Math. 162 (2011) 453-506 (ASC Preprint 21/2009) | [FETCHED] (full text, downloaded PDF converted locally, read in full, including Section 6.2 verbatim) | The one paper found in this whole search where "Pontryagin space" and "admissible majorant" substantively co-occur; Definition 6.6 / Proposition 6.8 (the actual majorant criterion) is stated for $E \in HB_0$, the classical class, not the indefinite class $HB_{<\infty}$ used elsewhere in the same paper |
| Burnol, "Two complete and minimal systems associated with the zeros of the Riemann zeta function" | arXiv:math/0203120, J. Théor. Nombres Bordeaux 16 (2004) 65-94 | [FETCHED] (ar5iv HTML, plus full text of the *published* JTNB PDF downloaded and converted locally with `pdftotext`, read in full, 1798 lines) | Prop. 2.2 (poles at $s=0,1$), Thm. 2.1 ($K_a$ entire), Prop. 4.5 ($\dim(L_a/K_a)=2$); Burnol's own methodological remark about stepping outside the entire-function axioms; full bibliography read |
| Burnol, "On Fourier and Zeta(s)" | arXiv:math/0112254, Forum Math. 16(6) (2004) 789-840 | [FETCHED] (full text, downloaded PDF converted locally, read in full, 2853 lines) | The longer "Habilitationsschrift" that Prop. 2.2 of the JTNB paper cites as its origin (as "[7, 6.10]"); the master reference for $L_a$'s construction |
| Suzuki, "A canonical system of differential equations arising from the Riemann zeta-function" | arXiv:1204.1827 | [FETCHED] (ar5iv HTML) | Independent author's engagement with Burnol's Sonine spaces; identifies a *different* obstruction (RH itself is needed to build classical de Branges spaces for $\omega<1/2$), not the pole pair |
| Suzuki, "The screw line of the Riemann zeta-function and its applications" | arXiv:2209.04658, J. reine angew. Math / preprint | [FETCHED] (ar5iv HTML) | A different, unrelated de Branges-adjacent framework (screw functions / positive-definite kernels); no discussion of poles, majorants, or Pontryagin spaces |
| Lagarias, "Hilbert spaces of entire functions and Dirichlet $L$-functions" | in *Frontiers in Number Theory, Physics, and Geometry I*, Springer (2006), 365-377 | **UNREACHED.** Four independent fetch attempts failed: a ResearchGate-hosted PDF mirror (HTTP 403), the same PDF via a text-extraction proxy (CAPTCHA-blocked), the Springer/`idp.springer.com` authentication redirect chain (no anonymous route), and the author's own talk-slides PDF on this material (local extraction failure). No claim is made about this source's content in either direction. | N/A: not read |

## 3. Thread 1: the admissible-majorant / model-space literature

**The whole lineage is calibrated to an asymptotic quantity that a 2-point pole set cannot have.**
BBH [FETCHED] states its own scope precisely: $\Theta(z) = \exp(iaz)B(z)$ with $a\ge 0$ and $B$ "a
Blaschke product with zeros tending to infinity," and "there is a well-defined branch of the argument
of $\Theta$ on $\mathbb R$," an increasing function $\theta$ with

$$\theta'(t) = a + \sum_n \frac{\mathrm{Im}\,z_n}{|t-z_n|^2},\qquad t\in\mathbb R.$$

Every theorem in this paper, and in its two direct ancestors (Havin-Mashreghi's "slow winding" and
"fast winding" papers, whose own titles name the governing quantity), is phrased as a hypothesis on
the growth rate of $\theta$: linear growth ($C_1\le\theta'\le C_2$) recovers the Paley-Wiener answer;
"sufficiently sparse" zeros give a minimal positive majorant by a different mechanism; BBH's own
stated goal is "to fill in this gap" between these two regimes for zero sequences with power growth
in a strip. Baranov-Havin's title, "arguments of inner functions," names the same governing object.
None of this has content for a finite pole set: $\theta'$ for a Blaschke factor with finitely many
zeros is, by the same formula, a bounded, compactly-concentrated, integrable perturbation of whatever
the infinite part contributes, with no asymptotic growth rate of its own. [FETCHED, BBH abstract and
Section 1]: the paper's own abstract restricts to a single meromorphic Blaschke product $B$ with the
admissible-majorant question posed for the *whole* zero sequence's distribution; nothing in the paper
addresses, as a distinguished case, a $B$ that is itself a product of an infinite part and an
isolated finite part. A direct text search of the full downloaded paper for "Burnol," "Sonine,"
"zeta," or "Riemann" returns zero hits [FETCHED, confirmed by direct grep of the extracted text]:
this literature was built independently of, and has not been connected to, the zeta-loaded Sonine
space in any source found.

**The nearest terminological match is a different problem.** Baranov and Woracek's two 2009 papers,
"Subspaces of de Branges spaces generated by majorants" and its companion "Finite-dimensional de
Branges subspaces generated by majorants," combine "finite-dimensional," "de Branges," and
"majorant" in one title, closer to the target vocabulary than anything else found. [FETCHED, full
text of the finite-dimensional companion]: the setup fixes a single *classical* $E\in HB$ (entire,
Hermite-Biehler) once and for all, and studies $\mathcal R_\omega(E) := \mathrm{Clos}_{H(E)}\{F\in
H(E): \exists C>0,\ |E^{-1}F|\le C\omega \text{ on } \mathbb R\}$, the subspace of $H(E)$ cut out by a
majorant condition on $\omega$; the paper's main theorem (Theorem 3.8) characterizes exactly when
this generated subspace $\mathcal R_\omega(E)$ is finite-dimensional, via the auxiliary family
$\omega_{[k]}(x) := (1+|x|)^k\omega(x)$. This is a different object from what the corridor needs:
"finite-dimensional" here is a property of a *sub*space carved out of an already-classical,
already-entire ambient space by a majorant inequality, not a property of extending the ambient space
itself by finitely many meromorphic (pole-bearing) directions. A direct grep of the full extracted
text confirms zero occurrences of "Pontryagin," "meromorphic," "indefinite," "negative square," or
"pole" anywhere in the paper [FETCHED]. The companion "Subspaces..." paper (2009, Canad. J. Math.)
is described the same way in its own abstract [FETCHED, publisher page]: $E$ is again a classical de
Branges-Hermite-Biehler entire function throughout.

**This survey's own derivation (unsourced, not read from any paper).** Read literally, BBH's own
stated scope, $\Theta=\exp(iaz)B(z)$ with $B$ "a Blaschke product with zeros tending to infinity,"
does technically cover $L_a$'s realization: if $K_a\cong K_B$ for Burnol's own (infinite) inner
function $B$, and $b$ is the finite (degree-2) Blaschke factor accounting for the two poles at
$s=0,1$, then the classical model-space decomposition $K_{B\cdot b} = K_B \oplus B\cdot K_b$ matches
Burnol's own $\dim(L_a/K_a)=2$ on the nose, and $B\cdot b$ still has "zeros tending to infinity" (a
finite correction cannot violate that). So the objects are not categorically outside BBH's stated
scope, as the first pass of this search suggested; the finite pole set is a bounded, localized
correction, not a foreign kind of thing. But by the formula for $\theta'$ above, this finite
correction changes $\theta$ only by an $O(1)$ (bounded) shift in the limit $t\to\pm\infty$, so it
cannot change the asymptotic growth-rate CLASS of $\arg(B\cdot b)$ relative to $\arg B$: every
theorem in this lineage, being stated purely in terms of that asymptotic class (linear/slow/fast/
power growth), would classify $K_{B\cdot b}$ identically to $K_B=K_a$. Concretely, this predicts
that *even if* one carried out the (currently unattempted, see Section 5) work of verifying $L_a$'s
inner function literally has this product form and checking BBH's precise hypotheses, the qualitative
admissible-majorant answer recovered would be the one already measured for the entire, non-zeta-
loaded branch (Branch A of the parent survey, majorant-nil, content-free per
[`../s4_carrier_audit.md`](../s4_carrier_audit.md)). That is: this literature is not walled off from
$L_a$ by a category error the way Carneiro-Littmann's entireness axiom is (Section 1.3 of the parent
survey), but it is, by its own defining mechanism, blind to exactly the finite-rank data that makes
$L_a$ different from $K_a$. A repair through this door would not be a category error; it would be
informationally empty by construction.

## 4. Thread 2: Kaltenbäck-Woracek Pontryagin-space de Branges theory

**The structure function stays entire.** [FETCHED, Woracek 2011, read at source]: the indefinite
generalization is built by relaxing the *inequality*, not by admitting poles. Classical: "An entire
function $E(z)$ which has no zeros on the real line is said to belong to the Hermite-Biehler class
$HB_0$, if it satisfies $|E(\bar z)|<|E(z)|$" throughout the upper half-plane. Indefinite: "An entire
function $E$ is said to belong to the indefinite Hermite-Biehler class $HB_{<\infty}$" if the same
positivity inequality is allowed to fail at finitely many points (full technical condition involving
no real zeros and no conjugate pairs of a certain kind). $E$ is still, in every place this was
checked, required entire. The "meromorphic" content in this literature lives one level removed, in
an auxiliary generalized Nevanlinna function $q$ (meromorphic in $\mathbb C\setminus\mathbb R$, with
finitely many "negative squares" of its Nevanlinna kernel $K_q(w,z) = \frac{q(z)-\overline{q(w)}}
{z-\bar w}$), which the classical de Branges / Krein correspondence then converts into a genuinely
entire (indefinite) structure function via a Cayley-type construction. [FETCHED, Kaltenbäck-Woracek
Part IV, read in full]: this is exactly the machinery on display there too, but aimed at canonical
systems and Hamiltonians ("we define an indefinite analogue of canonical systems, construct an
operator model which now acts in a Pontryagin space"), not at de Branges structure functions or
majorant problems directly; the paper's own bibliographic keywords are "canonical system, indefinite
inner product, operator model." A direct grep of the full 6776-line extraction returns zero
occurrences of "majorant" anywhere in Part IV [FETCHED].

**The one genuine co-occurrence, and where it stops short.** Woracek's 2011 paper is the single
source found in this entire search where "de Branges Pontryagin space" and "admissible majorant"
substantively meet, in Section 6.2, "Polynomials in de Branges Pontryagin spaces." [FETCHED, exact
text]:

> "We obtain a criterion for the existence of minimal (positive) admissible majorants. Let us recall
> this notion... **Definition 6.6.** Let $E\in HB_0$ and $m:\mathbb R\to(0,\infty)$. Then $m$ is
> called a (positive) admissible majorant for $H(E)$, if there exists a function $F\in H(E)\setminus
> \{0\}$ such that $|F(x)|\le m(x)$, $x\in\mathbb R$... **Proposition 6.8.** Let $E\in HB_0$. Then
> there exists a minimal (positive) admissible majorant for $H(E)$ if and only if for one (and hence
> for all) $\alpha\in\mathbb R$ the function $q_\alpha$ satisfies (I), (II), and (III$_0$)."

The class restriction is explicit and load-bearing: both the definition of admissible majorant
(Def. 6.6) and the criterion for its existence (Prop. 6.8) are stated for $E\in HB_0$, the *classical*
Hermite-Biehler class, even though the section title promises "Pontryagin spaces" and the surrounding
machinery (Theorem 3.2, the conditions (I)/(II)/(III) on a generalized Nevanlinna function $q$) is
genuinely indefinite. Reading the section as a whole, the indefinite apparatus is used as a
computational *tool* to derive a majorant criterion whose object of study, $H(E)$ for $E\in HB_0$,
never leaves the classical, positive-definite world. No admissible-majorant definition or theorem
anywhere in this paper is stated for $E\in HB_{<\infty}$ itself (the genuinely indefinite class used
two sections earlier in the same paper, Corollary 6.4). This is the precise sense in which the
"vehicle exists, the cargo does not": Kaltenbäck-Woracek's program supplies a working
reproducing-kernel theory for spaces with finite negative index (this is the entire point of the
six-part series), but an extremal/majorant theorem posed *inside* that indefinite setting was not
found anywhere in this search, including in the one paper that gets closest to combining the two
ideas.

**Is $L_a$ a known instance of this framework at all?** Not as searched. $L_a$'s own completed Mellin
transform has actual poles at $s=0,1$ (Burnol, Prop. 2.2), so $L_a$ itself is not an $H(E)$ for
$E\in HB_{<\infty}$ in the Kaltenbäck-Woracek sense (their $E$ is always entire). Reaching their
framework from $L_a$ would require a translation step: repackaging the pole/residue data of $L_a$'s
Mellin transform as a genuine generalized Nevanlinna function $q$ (meromorphic, finitely many
negative squares of its own reproducing kernel), then running the Krein-Langer / Kaltenbäck-Woracek
machine to produce a genuinely entire indefinite structure function $E\in HB_{<\infty}$. **No source
found in this search performs this translation for $L_a$, for Burnol's Sonine spaces generally, or
for any zeta-loaded object.** Burnol's own two papers were read in full for exactly this and contain
zero occurrences of "Pontryagin," "Kaltenbäck," "Woracek," "Krein-Langer," "indefinite," or "negative
square" [FETCHED, confirmed by direct grep of both extracted texts, math/0203120 and math/0112254];
Burnol cites Krein only for the classical 1947 theorem on entire functions of exponential type
(refs [17],[19] of the JTNB paper), never for the generalized-Nevanlinna-function / Pontryagin-space
line. Whether the translation would even succeed (does $L_a$'s pole data satisfy the negative-square
condition required to be a bona fide $q\in N_\kappa$ for finite $\kappa$?) is consequently an open
computation nobody has attempted, not a settled fact in either direction.

## 5. Thread 3: the pole-clearing trick, executed or not

**Not executed, anywhere found, including by Burnol.** Both of Burnol's papers were searched in full
(not just the propositions the parent survey had already extracted) for a construction that
multiplies the completed Mellin transform by $s(s-1)$ or an equivalent polynomial to clear the two
poles and produce an entire companion object, and for any subsequent discussion of what happens to a
norm, reproducing kernel, or extremal/majorant question under that operation. Direct text search of
both full extractions (1798 lines for the JTNB paper, 2853 lines for the Habilitationsschrift) for
"$s(1-s)$," "$s(s-1)$," "clear... pole," "majorant," or "admissible" returns zero hits in every case
[FETCHED].

**What Burnol does say, verbatim, and where.** Immediately after Theorem 2.1 (which states that
$K_a$'s completed Mellin transform is entire and that the space of such transforms "satisfies all
axioms of [de Branges'] general theory of Hilbert spaces of entire functions") and immediately before
Proposition 2.2 (the poles at $s=0,1$), the JTNB paper reads, verbatim and in full [FETCHED,
math/0203120, Section 2]:

> "It appears to be useful not to focus exclusively on entire functions, and to allow poles, perhaps
> only finitely many."

This sentence carries no citation of its own. The two citations that flank it, "[6]" (Burnol's own
2001 CRAS note giving "an elementary proof" of Theorem 2.1, i.e. that $K_a$, not $L_a$, is entire) and
"[8, Théorème 1]" (Burnol's own 2002 CRAS note, arXiv:math/0208121, for "a useful extension" of the
*same* entire-function statement), both concern the classical, non-zeta-loaded branch the parent
survey already catalogued as Branch A ([`../s4_cheap_falsifiers_survey.md`](../s4_cheap_falsifiers_survey.md)
Section 1.2). Neither is a repair of $L_a$'s pole structure. The sentence reads, in context, as
Burnol's own candid, undeveloped methodological aside: a recognition that he is stepping outside
de Branges' classical entire-function axioms, called "useful" for the purpose at hand (hosting the
zeta zeros as residue-evaluator data), with no claim that an existing theory already covers the step
and no indication he searched for one. Nothing downstream in either paper returns to this question;
Proposition 2.2 simply states the pole locations as a fact about $L_a$ and moves on to completeness
and minimality questions (the paper's actual subject), never to majorization.

## 6. Thread 4: does any Lagarias or Burnol survey flag the pole pair as a known obstruction?

**Lagarias's named paper: unreached, not checked-negative.** "Hilbert spaces of entire functions and
Dirichlet $L$-functions" (2006 book chapter) could not be fetched at source in this session despite
four independent routes (see Section 2's sources table). No claim is made about whether it discusses
the pole obstruction; this sub-question is left explicitly open rather than folded into the verdict
as an absence.

**Two adjacent, fetchable sources checked directly, both negative.** Suzuki's "A canonical system of
differential equations arising from the Riemann zeta-function" (arXiv:1204.1827) [FETCHED, ar5iv]
engages Burnol's Sonine-space program directly (it builds a canonical system from the same de Branges
data) but names a *different* obstruction: constructing the relevant classical de Branges space is
only unconditional for $\omega>1$, and needs RH itself for $0<\omega<1/2$. It does not discuss the
$s=0,1$ pole pair, does not cite Pontryagin-space or Krein-Langer theory, and does not discuss
majorants. Suzuki's later "The screw line of the Riemann zeta-function and its applications"
(arXiv:2209.04658) [FETCHED, ar5iv] works in an entirely different framework (screw functions and
positive-definite kernels) with no discussion of poles, de Branges structure functions, or majorants.

**Burnol himself is the closest thing to a "flag" found in this search**, and it is a weak one: the
Section-5 quote above documents that he noticed the departure from classical axioms and called it
useful, but he does not name it as a problem against any specific target theory (Carneiro-Littmann's
1406.5456 postdates Burnol's papers by roughly a decade) and does not cite the admissible-majorant or
Pontryagin-space literatures anywhere in either paper read. No survey-level source found in this
search states, as the parent dossier's own falsifier-2 finding does, that the pole pair is *the*
obstruction to running one-sided de Branges-space positivity theory on the zeta-loaded Sonine space.
That specific framing appears to be this repo's own synthesis (built by combining Burnol's
propositions with Carneiro-Littmann's hypotheses directly), not a citation of a prior survey's
diagnosis.

## 7. Verdict

**NOT-REPAIRABLE-AS-SEARCHED.** No source found poses a one-sided extremal or admissible-majorant
problem on $L_a$, on a $s(s-1)$-cleared entire companion to $L_a$, or on a genuinely indefinite
(Pontryagin, finite negative index) realization of $L_a$'s pole data. This is chosen over
OPEN-NEEDS-EXPERT because the finding is not a bare absence: two nearest-miss frameworks were
identified, each with a specific, named, structural reason it does not reach the target, mirroring
the rigor of the parent survey's own ILL-POSED verdict on falsifier 2.

**Nearest miss 1 (Section 3): the BBH/Havin-Mashreghi/Baranov lineage.** Genuinely a majorant theory
for meromorphic model spaces with fixed poles, and, on reflection, not categorically excluded from
covering $L_a$'s shape (a finite Blaschke correction to an infinite one is within its literal stated
scope). What it lacks: sensitivity to exactly the data that distinguishes $L_a$ from $K_a$. Every
theorem in this lineage is organized around the asymptotic growth rate of the generating inner
function's argument (Havin-Mashreghi's own "slow winding" / "fast winding" titles are the clearest
evidence of this), and a fixed 2-point pole correction is, by the paper's own defining formula for
that growth rate (equation (2) of BBH), an $O(1)$ perturbation invisible to every asymptotic regime
the theory distinguishes between. Even a successful, currently-unattempted formal application would
be predicted (this survey's own derivation, Section 3) to return exactly the answer already measured
for the entire branch $K_a$ alone, i.e. no new content.

**Nearest miss 2 (Section 4): Kaltenbäck-Woracek Pontryagin-space de Branges theory.** Genuinely a
reproducing-kernel theory for spaces with finite negative index, built exactly to handle finitely
many failures of classical positivity. What it lacks, twice over: (a) no source found ever translates
$L_a$'s pole/residue data into the generalized-Nevanlinna-function input this machinery needs, so
whether $L_a$ even instantiates the framework is an open computation, not a known fact; and (b) even
where "Pontryagin space" and "admissible majorant" are treated in the same paper (Woracek 2011,
Section 6.2), the majorant theorem itself is stated for the classical subclass $HB_0$, not the
indefinite class $HB_{<\infty}$ that gives the paper its title. The indefinite machinery is a
computational tool for a classical-space answer in the one instance found, not the site of an
indefinite extremal theorem.

**Residuals honestly named, for whoever picks this up next**, in the same spirit as the parent
survey's own practice:

1. Kaltenbäck-Woracek Parts I, II, III, V, and VI were not read in full in this pass (only Part IV,
   plus the related 2011 $N$-associated paper); a majorant theorem stated literally for
   $E\in HB_{<\infty}$ could in principle live in one of the unread parts. Cheap to check directly
   (all are listed with PDF links on Woracek's own publications page).
2. Lagarias's "Hilbert spaces of entire functions and Dirichlet $L$-functions" was unreached at this
   search depth on every route tried; it might independently confirm, extend, or contradict this
   dossier's finding.
3. Whether $L_a$'s pole data actually satisfies the negative-square condition needed to realize it as
   a generalized Nevanlinna function (the prerequisite for nearest miss 2 to even apply) has never
   been checked by anyone, in either direction.

## 8. Consequence for the #164 reopen condition

Per [`PHASE_STATE.md`](../../../PHASE_STATE.md)'s falsifiability triggers, the #164 reopen conditions
are "exactly those residuals resolving in the machinery's favor (a meromorphic majorant theory that
poses on $L_a$, or a KNS-class identity at log-growth nodes)." This dossier searched specifically and
directly for the first of those two and did not find it; it found, instead, two well-characterized
frameworks that come close in vocabulary but not in substance, each for a nameable structural reason.
**Reopen condition (i) does not fire. This finding hardens the #164 closure**, adding a
literature-side "no repair found, and here is why not" to the frame audit's original category-error
diagnosis. The corridor remains closed as a proof home on this rung, reclassified (per #163/#164) as
the project's measurement instrument and discipline-sharpener rather than a live proof route. Reopen
condition (ii), the Kulikov-Nazarov-Sodin space definition pinned against $\{k\log p\}$'s actual
$\lambda_j\sim\log j$ growth, is untouched by this dossier and remains the only unresolved escape,
rung (ii) for a separate SURVEYOR pass.

## 9. Handoff to BUILDER

1. **Do not attempt to resurrect a Carneiro-Littmann-style one-sided extremal construction directly on
   Burnol's $L_a$.** This dossier is the second independent finding (after the parent survey's
   entireness-axiom category error) that this specific door is closed, now for two further,
   independent reasons on the repair side specifically.
2. **If a structurally similar situation recurs on the theta/modular-interpolation pivot** (per
   [`PHASE_STATE.md`](../../../PHASE_STATE.md)'s "next steps," the project's live target), for
   instance if a weakly holomorphic modular form or a theta-kernel construction produces its own
   finite-pole defect relative to an otherwise-entire ideal object, the two tools to reach for, and
   their known gaps, are exactly Sections 3 and 4 above: (a) BBH-style meromorphic-model-space
   majorant theory, which is mechanically ready for a finite-pole defect on top of an infinite carrier
   but is asymptotically blind to that defect by construction, so it can only ever recover what the
   infinite carrier alone already gives; and (b) the Krein-Langer / Kaltenbäck-Woracek generalized-
   Nevanlinna-function route into Pontryagin-space de Branges theory, which supplies genuine
   reproducing-kernel structure for an indefinite object but has no extremal/majorant theorem built
   for that indefinite object anywhere found, and whose translation step (repackaging pole/residue
   data as a bona fide generalized Nevanlinna function) is itself unautomated and would need to be
   built from scratch.
3. **The theta/modular pivot does not obviously inherit this obstruction.** Per Section 3 of the
   parent survey, that mechanism class (lattice-consuming modular interpolation identities, Radchenko-
   Viazovska / Cohn-Elkies / Bondarenko-Radchenko-Seip style) is a genuinely different tool from
   band-limited majorant theory; this dossier's negative finding is a closed door behind the pivot,
   not a constraint in front of it.
4. **This survey's Section 3 derivation (the $O(1)$-invisibility argument) is a reusable pattern, not
   just a one-off negative result:** any time a finite-rank correction is layered on an infinite,
   asymptotically-governed carrier, check whether the target theory's hypotheses are stated in terms
   of an asymptotic quantity before investing in a formal verification that the correction is
   technically "in scope." If they are, the correction is very likely informationally invisible to
   that theory regardless of scope, and the honest move is to look for a theory calibrated to exact
   (not asymptotic) finite data instead, as this dossier tried, and failed to find, on the Pontryagin
   side.
