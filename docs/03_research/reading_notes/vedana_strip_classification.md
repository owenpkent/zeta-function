# Vedana (arXiv:2608.10121): Fourier summation formulas with strip frequencies, classified by almost periodic meromorphic Nevanlinna functions

> SURVEYOR deep-read note, 2026-08-25 (fetches executed 2026-08-26 UTC). Executes the second
> deep-read assignment from [`watch_sweep_2026-08-25.md`](watch_sweep_2026-08-25.md) (grade
> CANDIDATE): "what the correspondence says about the pin slot and whether the Nevanlinna class
> parameterizes the glue space." Sources: the arXiv abstract page and the v1 HTML full text
> (`arxiv.org/html/2608.10121v1`), read via five targeted summarizing fetches plus one
> verification web search; quotes below are as returned by the fetch instrument over the HTML,
> displays re-set in LaTeX from those returns. Two instrument-flagged uncertainties are carried
> in the discrepancy log. Adversary pass: self-run, three attacks, Section 5; this was not an
> independent agent pass and ADVERSARY may re-run. Per the #201 derivability rule, no numbered
> coordinate is minted here: Section 3 states explicitly which findings are restatements or
> enrichments of #160/#152 clauses. No em dashes anywhere.

## 1. What the paper proves, precisely

**The object.** A *Fourier summation pair on a strip* (Definition 1): a locally summable
$a: \mathbb{R} \to \mathbb{C}$ and an admissible strongly tempered measure $\mu$ supported on
$\{z : |\mathrm{Im}\, z| < \sigma_\mu\}$ such that

$$\sum_{n \ge 0} a(\lambda_n)\,\varphi(\lambda_n) \;=\; \int_{\mathbb{R}} \hat\varphi(t)\,d\nu(t) \;+\; \sum_{\gamma \in A} b(\gamma)\,\hat\varphi(\gamma) \qquad \text{(eq. (1))}$$

for every $\varphi \in C_c^\infty(\mathbb{R})$. The nodes $\lambda_n$ are real (test-function
side); the frequencies split as $\mu = \nu + \eta$ with $\nu$ a Borel measure on $\mathbb{R}$
and $\eta = \sum_{\gamma \in A} b(\gamma)\delta_\gamma$ discrete in the open strip. The split
convention is load-bearing: "all atoms of $\mu$ supported on $\mathbb{R}$ are included in
$\nu$, whereas $\eta$ consists only of the atoms outside $\mathbb{R}$" (Definition 1, fetched
verbatim), so $A \cap \mathbb{R} = \emptyset$. *Real-antipodal*: $\mu$ real-valued and
$\overline{a(\lambda)} = a(-\lambda)$. *$\mathbb{R}$-symmetric*: $\gamma \in A$ iff
$\bar\gamma \in A$ with $b(\bar\gamma) = \overline{b(\gamma)}$. *Strongly tempered / ord*:
$\int (1+|z|^2)^{-k/2} d|\mu| < \infty$ over the strip, $\mathrm{ord}(\mu)$ = the least such
$k$ (fetched paraphrase of the displayed definitions).

**The function class.** $\mathfrak{N}_{\le k}$ = holomorphic $F: \mathbb{C}^+ \to \mathbb{C}$
such that for any $z_1, \dots, z_N \in \mathbb{C}^+$ the Hermitian matrix
$\big[\,i\,(F(z_n) + \overline{F(z_m)})/(z_n - \bar z_m)\,\big]$ has at most $k$ negative
eigenvalues (fetched verbatim; this is a Krein-Langer negative-squares condition, stated in a
rotated convention: the kernel is the standard Nevanlinna kernel of $iF$, so $k = 0$ is
Herglotz up to that rotation). $\mathcal{AP}(\mathbb{C}^+)$ = holomorphic maps bounded on
horizontal substrips whose restrictions $x \mapsto F(x+iy)$ are Bohr almost periodic for each
$y > 0$ (fetched verbatim in paraphrased order).

**Theorem 1 (formula $\Rightarrow$ function).** For a real-antipodal, $\mathbb{R}$-symmetric
FS-pair with $\mathrm{ord}(\mu) \le 2(k+1)$ and $a$ of finite exponential growth, the
generating function

$$F(z) := \tfrac{1}{2}a(0) + \sum_{\lambda > 0} a(\lambda)\, e^{2\pi i \lambda z}$$

is holomorphic almost periodic on $\mathrm{Im}\, z > c$ and extends meromorphically to
$\mathbb{C}^+$ as $F = N + S$ with $N \in \mathfrak{N}_{\le k} - \mathfrak{N}_{\le k}$ (a
*difference* of two generalized Nevanlinna functions) and $S$ the explicit strip-pole part
(eq. (17)): $S(z) = \frac{(z^2+\rho^2)^k}{2\pi i} \sum_{\gamma \in A}
\frac{\rho^2 + \gamma z}{\gamma - z} \cdot \frac{b(\gamma)}{(\rho^2+\gamma^2)^{k+1}}$
(fetched; regularization constants per the paper).

**Theorem 2 (function $\Rightarrow$ formula, with uniqueness).** Conversely, if $F$ is
meromorphic on $\mathbb{C}^+$ with $z \mapsto F(z+ic) \in \mathcal{AP}(\mathbb{C}^+)$ for some
$c > 0$, $\lambda \mapsto \mathbb{E}F(\lambda)$ locally summable (where
$\mathbb{E}F(\lambda) = \lim_T \frac{1}{2T}\int_{-T+iy}^{T+iy} F(z) e^{-2\pi i \lambda z} dz$
is the Bohr coefficient), all singularities simple poles $\gamma_n$ with residues
$-b(\gamma_n)/(2\pi i)$ satisfying $\sum |b(\gamma_n)|(1+|\gamma_n|^2)^{-(m+1)/2} < \infty$,
and $F - S \in \mathfrak{N}_{\le j} - \mathfrak{N}_{\le j}$, then $(\nu + \eta, a)$ is an
$\mathbb{R}$-symmetric FS-pair, with $a(\lambda) := \mathbb{E}F(\lambda)$ for $\lambda > 0$
(antipodal reflection for $\lambda < 0$), the node set $\mathrm{spec}(F) := \{\lambda :
\mathbb{E}F(\lambda) \neq 0\}$, $\eta$ read off the residues, and $\nu$ "the (unique)
real-valued measure from the Herglotz-Nevanlinna factorization of $F - S$" (fetched verbatim).
Uniqueness therefore means: *each admissible $F$ determines exactly one FS-pair*, every
ingredient extracted canonically (Bohr coefficients, residues, Herglotz boundary measure); and
the pair determines $F$ back through the defining series. The abstract's phrasing: "every
function in this class gives rise to a unique Fourier summation formula of the above type"
(abstract, verbatim).

**Lineage.** The paper "extend[s] the classification of Fourier summation pairs (FS-pairs for
short) developed in [18, 19]" ... "by allowing the measure $\mu$ to be supported on a strip of
finite width in $\mathbb{C}$, rather than requiring it to be supported on $\mathbb{R}$", and
"These examples were not covered by [18, 19]" (introduction, fetched verbatim; the "examples"
are the Guinand-Weil explicit formulas). Per an arXiv search cross-check, the real-line
lineage is Goncalves arXiv:2312.11185 (2023, "A classification of Fourier summation formulas
and crystalline measures", using almost periodic functions, Hermite-Biehler functions, de
Branges spaces, Poisson representation per its abstract) and Goncalves-Vedana arXiv:2504.02741
(2025, "A Complete Classification of Fourier Summation Formulas on the real line"); see the
discrepancy log for an instrument-level authorship wobble on [18]/[19]. Prior-work frame:
crystalline measures (Lev-Olevskii, Meyer, Olevskii-Ulanovskii, Kurasov-Sarnak cited), and the
Radchenko-Viazovska [39], Bondarenko-Radchenko-Seip [7], Kulikov-Nazarov-Sodin [23] summation
formulas; the de Branges/Krein vocabulary of the lineage is the repo's #171 corridor language,
as the watch sweep row anticipated.

**The Selberg-class instance (Section 3): genuinely an instance.** For $L$ in the Selberg
class, $F_L(z) = \frac{1}{2\pi}\sum_{n \ge 2} \Lambda_L(n)\, n^{-1/2+iz} =
-\frac{1}{2\pi}\frac{L'}{L}(\tfrac12 - iz)$, initially on $\mathrm{Im}\, z > 1/2$ (fetched
verbatim). The resulting identity (eqs. (24)-(25), fetched):

$$\frac{1}{2\pi}\sum_{n \ge 2} \frac{1}{\sqrt n}\Big\{\Lambda_L(n)\varphi\big(\tfrac{\log n}{2\pi}\big) + \overline{\Lambda_L(n)}\varphi\big(-\tfrac{\log n}{2\pi}\big)\Big\} = \frac{1}{2\pi}\int_{\mathbb{R}} \hat\varphi(t) W_L(t)\, dt + m_L\big\{\hat\varphi(\tfrac i2) + \hat\varphi(-\tfrac i2)\big\} - \sum_\rho \hat\varphi(\gamma_\rho)$$

with $W_L(t) = 2\log Q_L + 2\,\mathrm{Re}\sum_j \lambda_j \frac{\Gamma'}{\Gamma}(\lambda_j(\tfrac12+it)+\mu_j)$,
$m_L$ the pole order at $s = 1$ ($m_\zeta = 1$), and "The functional equation implies that the
multiset $\{\gamma_\rho\}$ is symmetric with respect to $\mathbb{R}$" (fetched verbatim). The
verification sentence: "The Selberg-class axioms imply that $\nu$ and $\eta$ are strongly
tempered of order at most 2, while $a(\cdot)$ has finite exponential growth. Hence Theorem 1
applies with $k = 0$" (fetched verbatim). The measures, as displayed for this example:

$$d\nu(t) = \frac{W_L(t)}{2\pi}\,dt - \sum_{\mathrm{Re}\,\rho = 1/2} \delta_{\gamma_\rho}, \qquad \eta = m_L\big(\delta_{i/2} + \delta_{-i/2}\big) - \sum_{\mathrm{Re}\,\rho \neq 1/2} \delta_{\gamma_\rho}$$

where $\gamma_\rho = -\gamma + i(\beta - \tfrac12)$ for $\rho = \beta + i\gamma$: on-line
zeros are *real* frequencies (atoms of $\nu$, negative sign), off-line zeros and the
$s = 0, 1$ pole terms are the strip atoms $\eta$, on $|\mathrm{Im}\, z| \le 1/2$. The paper
states no RH-conditional sentence anywhere in the section (fetch-checked); the formula is
unconditional by construction.

## 2. What it says for the repo's map

**(a) The Hamburger-pin slot (#160): the ambient space is now charted, the pin is untouched.**
The pin's landscape claim (LEARNINGS #160, T4 + the Knopp lesson) was: FE data + growth +
counting budget admit an infinite-dimensional solution family, witnessed by an explicit
relocation pair; the identifying clause is H4, the Dirichlet series absolutely convergent for
$\mathrm{Re}\, s > 1$, i.e. the additive lattice through the abscissa. Vedana's theorem is a
*structure theorem for exactly that ambient space*: everything with a Guinand-Weil-shaped
two-sided identity with strip frequencies is one point of a classical function class
($\mathcal{AP}$ meromorphic, Nevanlinna-difference modulo the explicit pole part), and the
class is parameterized, not merely witnessed large. In the paper's coordinates the H4 clause
of #160 is precisely the almost-periodicity-above-a-height clause with zeta's particular Bohr
spectrum: $F_\zeta$ is the AP function with $\mathrm{spec} = \{\log n / 2\pi\}$ and
coefficients $\Lambda(n)/2\pi\sqrt n$. Nothing in the classification privileges that spectrum.
Per the #201 derivability rule: the negative content here ("existence of an explicit-formula
identity cannot identify zeta; the solution space is a whole function class") is a
**restatement of #160's verdict with an enriched witness** (a full parameterization by an
external school, replacing #160's hand-built relocation family as evidence of size); the
positive content (the bijection itself, the $\nu/\eta$ extraction mechanics) is new structure
*on the map*, not a new constraint, and no coordinate is minted.

**(b) The sweep's NEXT question, "where does the additive lattice enter its uniqueness
clause": it does not.** Uniqueness in Theorem 2 is per-function and functional-analytic (Bohr
coefficient extraction, residue reading, uniqueness of the Herglotz factorization). It is a
statement that the correspondence is well-defined, not that any member is rigid or that
arithmetic node sets are forced. In every fetched definition, theorem, and example, the node
set enters only as $\mathrm{spec}(F)$, "constrained to the Bohr spectrum of $F$, not
arbitrary" (fetch summary), with local summability and growth the only conditions. The
additive lattice / log-prime structure appears nowhere as a constraint; it falls out as data,
exactly the #152 pattern (clauses stated in circumference-type data are system-generic; the
lattice is the separator that such clause sets do not see). This answers the assignment's
question (5) negatively and cleanly.

**(c) Does the Nevanlinna class parameterize the SP4 glue space? Yes for the
formula-existence layer, with a genuine construction recipe; no for the layers that matter to
M4.** Theorem 2 is a recipe: pick any admissible $F$, read off nodes, weights, $\nu$, $\eta$.
So the space of strip summation formulas (the space where SP4's two-sided identities live, the
home of the B1 rung-2 glue question) is not just characterized but constructed. Three scope
limits, stated honestly:

1. *Membership is an FE-side gate, not a lattice gate.* Belonging to the class requires
   meromorphic continuation of the generating Dirichlet-type series to $\mathbb{C}^+$ with AP
   structure and controlled poles. That is the continuation/growth package, the D-H side of
   the #152 bracket. A generic Beurling system (natural boundary at its abscissa, no
   continuation) has no member $F$, so its "formula" does not exist in this class at all
   (SURVEYOR inference from the definitions, not a sentence of the paper); a matched fake
   *with* continuation would be a member on equal footing with zeta. Membership therefore
   cannot serve as a counting-side separator, and the classification confirms by its
   generality that formula-existence is a shared-structure clause in #152's sense.
2. *The polarity layer is invisible.* The class is differences
   $\mathfrak{N}_{\le k} - \mathfrak{N}_{\le k}$: signed boundary measures. For zeta, $\nu$
   contains the on-line zeros with negative sign against a positive archimedean density; the
   parameterization is indifferent to the sign structure that Weil positivity (SP5, M4) is
   about. Nothing here touches the polarization gap.
3. *The repo's glue question is narrower than the classified space.* B1 rung 2 asks which
   formulas arise from Euler systems with lattice compatibility and a two-sided determinant-
   class assembly; Vedana classifies the far larger space of all strip formulas. The
   classification is the ambient chart, not the glue.

**(d) One clean observation read off the displayed measures (the note's observation, derived
from the paper's own $\nu/\eta$ split, not a sentence of the paper).** Because Definition 1
forces real atoms into $\nu$ and reserves $\eta$ for strictly-off-axis atoms, RH for $L$ is
exactly the statement that $\eta = m_L(\delta_{i/2} + \delta_{-i/2})$: *the strip part of the
frequency measure is the pole part alone*. The off-line locus and the arithmetic pole occupy
the same slot of the classification, and even under RH zeta's formula needs the strip (the
pole atoms sit at $\pm i/2$ unconditionally), which is precisely why the explicit formula
"lie[s] beyond the scope of the previous classification" (abstract) on $\mathbb{R}$. This
gives the repo a tidy coordinate for saying where an off-line zero would live in the
classified family: as an $\eta$-atom next to the pole, a legal member of the space. D-H's
off-line pairs would sit there too, if D-H's generating function is admissible; that
membership is plausible (its $\mathrm{Re}\, s > 1$ zeros are confined to a bounded substrip,
so $F(z+ic)$ should be AP for large $c$) but is *not verified here and not claimed by the
paper*, whose example section is scoped to the Selberg class. Flagged for ADVERSARY if anyone
wants to lean on it.

**(e) Rigidity (assignment question 3).** There is no crystalline-type rigidity theorem in
the paper, no uniqueness-of-node-set clause, and no "perturb and die" statement
(fetch-checked: no concluding/remarks/open-problems section exists; the narrative ends with
the proof of Theorem 2 in Section 5). What the classification supports is the split verdict:
perturbing zeta's nodes generically exits the class (the perturbed series generically loses
AP meromorphic continuation; inference as in (c)1), but among members nothing pins zeta. The
Beurling-discipline question "does the formula die under perturbation" thus factors into
"dies as a member" (yes, generically, for a named function-theoretic reason) and "dies as
zeta" (the classification is silent; identification is not its business). That is #160's "the
pin reformulates, it does not reduce," now visible from the outside.

## 3. What it does NOT change

- **No new constraint, no minted coordinate.** Under #201: the survey content is a
  restatement/enrichment of #160 (ambient-space size and the location of the H4 clause) and
  #152 (formula-existence clauses are system-generic; the lattice is data, not constraint).
- **The Hamburger pin's open clause is exactly where it was**: Dirichlet-face inheritance /
  identification, #160's residual. The classification adds a chart, not a pin.
- **No positivity content**: SP5/M4, the polarization gap, and the marginal-positivity
  compass are untouched (signed difference class throughout).
- **No counting-side leverage**: the strip classification consumes continuation + growth, not
  zero counts; the #160 budget verdict (counting can never supply locations) is unaffected.
- **The frontier is unmoved.** This is infrastructure of the map: the SP4 formula-existence
  layer now has an external, citable parameterization, in the de Branges/Krein-adjacent
  vocabulary the #171 corridor already speaks.

## 4. Discrepancy log (SURVEYOR reports; ADVERSARY/VERIFIER decide)

1. **[18]/[19] authorship, instrument-level wobble.** The bibliography fetch returned both
   entries as solo Vedana ("Fourier summation formulas and crystalline measures", 2024;
   "Classification of Fourier summation pairs", 2025) with an explicit instrument caveat that
   exact citations were not visible. The arXiv search record shows the real-line lineage as
   Goncalves arXiv:2312.11185 (solo, 2023) and Goncalves-Vedana arXiv:2504.02741 (2025).
   Titles and numbering in the note's Section 1 follow the search-verified record; the PDF
   bibliography should be checked before any external citation of [18]/[19] by number.
2. **A stray arXiv ID in the search layer.** The verification search's synthesis attributed
   the strip paper to "arXiv:2608.10253"; the direct abstract fetch of 2608.10121 returned
   this exact title, author, and abstract, so 2608.10121 is the verified ID and 10253 is
   presumed search-synthesis noise. Recorded so nobody chases it.
3. **Watch-sweep row accuracy: confirmed.** The row's claims (strip-supported frequency
   measure, Selberg-class Guinand-Weil explicitly encompassed, bijection with almost periodic
   meromorphic Nevanlinna functions, unique formula per function) all check against the
   fetched text verbatim. No correction needed.

## 5. Adversary pass (self-run, three attacks; not an independent agent pass)

- **A1 (over-claim): LANDED, wording fixed.** Draft phrasing had the classification
  "confirming #160's T4." Attack: T4 is specifically about the RvM *budget* clause failing to
  pin, and Vedana never mentions zero-counting budgets; membership does not even see them.
  Fix applied in 2(a): the theorem charts the ambient space in which #160's non-uniqueness
  witnesses live and enriches the size claim; it does not re-prove or touch T4's mechanism.
  Whether #160's specific $G_1/G_2$ relocation pair are themselves members (are their
  log-derivative generating functions AP meromorphic?) was NOT verified and is stated
  nowhere in this note as fact.
- **A2 (unlicensed generalization to D-H and Beurling): LANDED, scope flags added.** Attack:
  the paper's example section covers the Selberg class only; both "D-H fits" and "generic
  Beurling systems do not fit" are the note's inferences from Definition 1 + Theorem 2
  hypotheses, not the paper's claims. Fixes: 2(c)1 and 2(d) now carry explicit
  inference/plausibility markers, with the D-H membership additionally flagged for ADVERSARY
  before any load-bearing use. The D-H confinement fact used (zeros with
  $\mathrm{Re}\, s > 1$ lie in a bounded substrip) is classical background, not fetched, and
  is marked accordingly.
- **A3 (absence claims proved only by absence of fetch hits): LANDED, scoping added.** Attack:
  "the lattice appears nowhere as a constraint" and "no RH-conditional sentence" rest on five
  summarizing fetches, not a line-by-line read; a summarizer can miss a remark. Fixes: both
  claims are now scoped as fetch-verified absence (each was probed by a direct question to
  the full text and returned negative, including a dedicated flexibility/rigidity-language
  probe), and one residual convention wrinkle is recorded rather than resolved: the
  Selberg-class pair is called "an FS-pair on $|\mathrm{Im}\, z| \le 1/2$" while Definition 1
  uses an open strip $|\mathrm{Im}\, z| < \sigma_\mu$, reconciled in-paper by "our convention
  for admissible measures" (fetched fragment); the exact convention was not chased and
  nothing in this note depends on it.

## 6. What this enables / what remains open

**Enables.**
- A citable external parameterization of the SP4 formula-existence layer: any future glue
  candidate or trace-formula costume can be located as a point of Vedana's class (its $F$,
  its $\mathrm{spec}$, its $\nu/\eta$ split), and the $\eta$-slot gives a standard coordinate
  for off-line-zero bookkeeping (the pole-only $\eta$ reading of RH in 2(d)).
- A sharpened statement for the missing-object file if wanted (as enrichment, not new
  coordinate): the B1 glue question in Vedana coordinates reads "which members of the AP
  Nevanlinna class have lattice Bohr spectrum," and the classification proves that question
  is invisible to formula-existence structure.
- BUILDER: the explicit Theorem 2 recipe is a legal generator of two-sided identities for
  probe families (e.g. building controlled fake explicit formulas with prescribed
  $\eta$-atoms as D-H-style stress tests), cheaper than hand-deriving each identity.
- VERIFIER: nothing here is Lean-ready; the classical Herglotz-factorization uniqueness
  inside Theorem 2 is the only self-contained candidate if the corridor ever needs it.

**Remains open.**
- The KNS first-read pair (2509.17600, 2509.14953), third cycle unread; Vedana's [23]
  confirms the school adjacency but this note did not read them. The sweep's fold-in item
  stays open.
- The D-H membership check (A2) if anyone wants the "off-line pair as $\eta$-atoms" picture
  as more than a plausibility.
- Whether #160's relocation family embeds in the class (A1), a small check that would tie the
  two witnesses of ambient-space size together.
- The [18]/[19] PDF bibliography check (discrepancy log 1) before external citation.
