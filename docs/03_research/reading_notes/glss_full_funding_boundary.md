# GLSS I/II at full funding: the information wall's boundary pair, deep-read

> SURVEYOR deep-read note, 2026-08-26. The bounded GLSS prep block of frame session F2a,
> ruled to ride INSIDE F2a by the frame's first audit (LEARNINGS #209 scope ruling); boundary
> data for the certificate-class definition F2a will pose
> ([`../successor_frame_deliberation.md`](../successor_frame_deliberation.md) Sections 4 and 7).
> Sibling: [`proportion_support_landscape.md`](proportion_support_landscape.md) rows D3/D4
> graded these papers; this note deep-reads what that note only graded and does not duplicate
> its landscape. Two papers only: **GLSS I** = arXiv:2503.15449 (v4, 2026-03-30) and
> **GLSS II** = arXiv:2507.06823 (v1, 2025-07-09). GLSS = Goldston, Lee, Schettler,
> Suriajaya. No em dashes anywhere.
>
> **Rules of evidence.** Both papers were read in full, first-party: PDFs downloaded from
> arXiv and text extracted locally with pdftotext (no summarizer in the loop), then every
> load-bearing quote re-verified on an independent second route by grepping the papers'
> own LaTeX sources pulled from the arXiv e-print endpoint (`1-PCC1-260330.tex`,
> `2-PCC2-250709.tex`). Metadata came from the raw export-API Atom feed, read directly.
> Tag **[FETCHED-P]** = verified on both routes; **[FETCHED]** = single first-party route;
> **[SECONDARY]** = from a citing source or background knowledge, original not read;
> **[REPO]** = an existing repo dossier's adversarially re-fetched content. One extraction
> artifact was caught by the two-route discipline: pdftotext drops the conjugation bar, so
> the symmetric partner rendered as "$1-\rho$" where the source has $1-\bar\rho$
> (GLSS I Section 2, line 135 of the .tex). No summarizer paraphrase is quoted anywhere in
> this note; the month's five fabrication catches (#202/#207/#208) motivated the protocol.

## 1. The exact statements

### 1.1 GLSS I (arXiv:2503.15449v4): PCC gives 100 percent simple-and-on-line, no RH

**Conventions.** Zeros are taken from the multiset $\mathcal{Z}$ (a zero of multiplicity
$m_\rho$ appears $m_\rho$ times); $\rho = \beta + i\gamma$, $0 < \beta < 1$; $N(T)$ counts
$0 < \gamma \le T$ with multiplicity; $L := \frac{1}{2\pi}\log T$, so $N(T) = TL + o(TL)$.
By the reflection principle and the functional equation, zeros with $\gamma > 0$ split into
two disjoint classes: "1) zeros on the critical line with $\beta = 1/2$, and 2) symmetric
pairs of zeros $\rho = \beta + i\gamma$ and $1-\bar\rho = 1-\beta+i\gamma$, with
$\beta \ne 1/2$. This classification will be important later." [FETCHED-P, Section 2]

**The hypothesis class.** With $N(\lambda) := \#\{(\rho,\rho') : 0<\gamma,\gamma'\le T,\
0 < (\gamma'-\gamma)L \le \lambda\}$ (pairs of multiset ordinates at positive gap; equal
ordinates excluded):

> **Pair Correlation Conjecture (PCC).** For $UL = \lambda > 0$, then
> $N(\lambda) = TL \int_0^\lambda \big(1 - (\tfrac{\sin\pi\alpha}{\pi\alpha})^2\big)\,d\alpha
> + o(TL)$, as $T \to \infty$, uniformly in each interval
> $0 < \lambda_0 = U_0L \le \lambda = UL \le \lambda_1 = U_1L < \infty$. [FETCHED-P, Section 4]

Remark 1 upgrades the compact-interval uniformity to windows moving with $T$:
$\lambda_0(T) \to 0$ and $\lambda_1(T) \to \infty$ are allowed, and the proof of Theorem 1
uses exactly that ("we take $\lambda \to \infty$ appropriately as $T\to\infty$ as in Remark
1"). Three typings of this hypothesis matter for F2a. (i) It is the GUE-shape law (Fejér
kernel $1 - (\sin\pi\alpha/\pi\alpha)^2$), asserted at every gap scale: in the repo's
Fourier vocabulary this is the full-support pair register, though the papers never use
Montgomery's $F(\alpha)$ (GLSS I does not mention it at all). (ii) It is asserted of the
**vertical marginal only**: ordinates of all strip zeros, wherever $\beta$ sits. The
abstract makes this the paper's stated clarification: "We clarify this result by
explicitly not assuming RH and considering PCC as a conjecture only concerning the
vertical distribution of zeros." [FETCHED-P] And the introduction: "In this paper we do
not assume the Riemann Hypothesis (RH) is true or make use of results that depend on RH."
[FETCHED-P] (iii) Its error class is an unquantified $o(TL)$ at the density normalization;
every downstream statement inherits exactly this class.

**The conclusion.**

> **Theorem 1.** "Assuming the pair correlation conjecture PCC, then asymptotically 100% of
> the zeros of $\zeta(s)$ are simple and on the critical line." [FETCHED-P]

Density sense, from the proof of Theorem 2: $\#\{\rho :\ 0<\gamma\le T,\ \rho \text{ simple},\
\beta = \tfrac12\} \ge (1+o(1))\,N(T)$, hence (with the trivial upper bound) the proportion
tends to $1$ in the limit (not merely liminf), with an ineffective $o(N(T))$ residual: no
rate is or can be stated, since PCC's own error is an unquantified $o(TL)$.

**The mechanism, one paragraph.** The second moment of zero counts in short intervals,
$\int_0^T (\Delta_U N(t))^2 dt$ with $\Delta_U F(t) = F(t+U)-F(t)$, is computed two ways.
Analytically (Proposition 1 + Proposition 2): via the Riemann-von Mangoldt decomposition
$N = M + 7/8 + S + O(1/t)$ and Fujii's unconditional
$\int_0^T (\Delta_U S)^2 dt = \frac{T}{\pi^2}\log(2+UL) + O(T\sqrt{\log(2+UL)})$, giving
$T(UL)^2 + \frac{T}{\pi^2}\log(2+\lambda)$ plus errors, with **no hypothesis**.
Combinatorially (Proposition 1): the same moment is
$U N^{\circledast}(T) + 2\int_0^U N(T,u)\,du + O(L^2)$, where
$N^{\circledast}(T) := \#\{(\rho,\rho') : \gamma = \gamma'\}$ is the equal-ordinate pair
count. PCC evaluates the integral term; subtracting yields the Horizontal Multiplicity
Hypothesis **HMH**: $N^{\circledast}(T) = \sum_{0<\gamma\le T} H(\gamma) = (1+o(1))TL$,
where $H(\gamma)$ counts (with multiplicity) all zeros on the horizontal line $t=\gamma$.
The location step is then pure functional-equation combinatorics (Section 7, the
"horizontal multiplicity" idea credited to a suggestion of Soundararajan): an off-line zero
forces its symmetric partner $1-\bar\rho$ onto the **same horizontal line**, so
$H(\gamma) \ge 2$ for every off-line zero and every multiple zero, while $H(\gamma)=1$
means exactly one zero on that line, necessarily simple and critical. Since
$N^{\circledast} = \sum_{\text{distinct lines}} h^2$ against $N = \sum h$, HMH forces
$h = 1$ almost always:
$\#\{\text{simple critical}\} \ge \sum_{0<\gamma\le T}(2 - H(\gamma)) = 2N(T) - N^{\circledast}(T) = (1+o(1))N(T)$.
The correlation input is converted into location density by the FE symmetry and nothing else.

### 1.2 GLSS II (arXiv:2507.06823v1): the Alternative Hypothesis gives the same conclusion

**The hypothesis class.** Two hypotheses, both about the vertical marginal, both RH-free
("Throughout this paper we do not assume RH; any results we mention that depend on RH are
only used as a model to formulate conjectures." [FETCHED-P, Section 1]).

> **AH-Pairs** (from [BGSTB25a]). For any $M > 0$, with
> $\mathcal{P}(T,M) := \{(\gamma,\gamma') : \tfrac{T}{\log^2 T} < \gamma,\gamma' \le T,\
> |(\gamma-\gamma')L| \le M\}$: for every $(\gamma,\gamma') \in \mathcal{P}(T,M)$ there is an
> integer $k$ with $(\gamma-\gamma')L = \tfrac{k}{2} + O\big((|k|+1)R(T)\big)$, for a positive
> decreasing $R(T) \to 0$. [FETCHED-P, (AH0)]

That is the rigid quasi-lattice law: every near-diagonal gap sits near a half-integer
multiple of the mean spacing. Binning by nearest half-integer defines densities
$P_{k/2}(T) := (TL)^{-1}|B_{k/2}(T)|$ with $p_{k/2} := \lim_T P_{k/2}(T)$ when it exists.
The paper's origin paragraph: "a sequence of Landau-Siegel zeros forces the existence of
infinitely many extremely long intervals $(a,b]$ where zeros $\rho = \beta+i\gamma$ with
$a < \gamma \le b$ all satisfy $\beta = 1/2$, are simple, and are spaced at nearly integer
multiples of half the average spacing" [FETCHED-P], and "experimental evidence [MO84,
Odl87] on the vertical distribution of zeros supports PCC and contradicts AH" [FETCHED-P]:
the two laws are competing, mutually contradictory candidates.

> **AH-Weak Density.** (AH1): for each positive integer $j$,
> $P_{j-1/2}(T) + P_j(T) = 1 - \tfrac{2}{\pi^2(2j-1)^2} + O(R_P(T))$, $R_P(T) \to 0$,
> $j$-uniform. (AH2): for any large even $M$,
> $\sum_{j=1}^{M} P_{j-1/2}(T) = \tfrac{M}{2} - \tfrac14 + O(\tfrac1M) + O(M R_P(T))$,
> uniform on compacta in $M$. [FETCHED-P, Section 1]

Crucially, the model's stated scope: "(AH1) is obtained immediately from (1.15). Our model
for (AH1) is that we know the densities $P_{j-1/2}(T)+P_j(T)$ ... but make no assumption on
$P_0(T)$." [FETCHED-P] The diagonal bin, the one carrying simplicity and location, is
deliberately NOT assumed: it is what the theorems derive. ((1.15) is the RH-conditional
density theorem of [BGSTB25a] quoted in the paper; see Section 7 below.)

**The conclusions.**

> **Theorem 1.** "Assuming AH-Pairs, we have that $p_0 = 1$ is equivalent to ESH." [FETCHED-P]

where ESH (Essential Simplicity Hypothesis, adapted from Mueller [Mue83] to the no-RH
setting in GLSS I) is (ES1) $N^{\circledast}(T) = TL + o(TL)$ plus (ES2)
$N(T,\lambda_0) = o(TL)$ for $\lambda_0 \to 0$, jointly equivalent to
$N^{\circledast}(T) + 2N(T,\lambda_0) = TL + o(TL)$.

> **Theorem 4.** "Assuming AH-Pairs and AH-Weak Density, we have $p_0 = 1$ and
> asymptotically 100% of the zeros of $\zeta(s)$ are simple and on the critical line."
> [FETCHED-P]

Same density sense as GLSS I (limit, ineffective $o(N(T))$ residual). The engine is
Theorem 2, an identity equating the AH-binned Fejér-weighted sums with the unconditional
Fujii budget, and the paper is explicit about what it reads off the law: "The method only
obtains asymptotic formulas when we take long averages over the densities from AH-Pairs."
[FETCHED-P] The partial-funding rung, with (AH1) but not (AH2):

> **Corollary 2.** "$\limsup_{T\to\infty} P_0(T) \le 3/2$ and asymptotically at least 50% of
> the zeros of $\zeta(s)$ are simple and at least 50% are on the critical line." [FETCHED-P]

**Why AH is run through Gallagher-Mueller rather than $F(\alpha)$.** "Our use of RH in
(1.15) and (1.17) is required because we have obtained these results by applying
Montgomery's theorem for his function $F(\alpha)$." [FETCHED-P] The form-factor route
costs RH; the second-moment route does not. This is load-bearing for the input typing
(Section 3): at full funding without RH, the papers fund from the zero side directly, not
through any prime-side dictionary.

## 2. The escape clause, precisely

**The negative finding first: there is no escape-clause sentence in either paper.** A
sweep of both LaTeX sources for "cannot", "out of reach", "does not imply / not imply",
"does not follow / give / yield", "fails to", "no information", "still open", "remains
open" returns **zero hits referring to RH** [FETCHED-P, both sources]. The only "cannot"
in GLSS II is about limiting densities ("Without using (AH2), we cannot determine if the
limiting densities in Theorem 2 exist."). Every RH mention in GLSS I (15 instances) is
either historical framing, the no-RH declaration, the definition, Remark 2, or the
$H(\gamma) = m_\rho$ comparison; same character in GLSS II (17 instances). Unlike AF ("RH
itself is out of reach of the mechanism" [REPO, #202]) and BGSTB (the method "neither
requires nor provides any information as to whether or not the nontrivial zeros satisfy
$\beta = 1/2$" [REPO, #208]), the GLSS pair is **silent**: the completeness question is
not posed, disclaimed, or discussed. The escape is carried entirely by the formalism, in
four in-print places:

1. **The conclusions' own formulation.** "Asymptotically 100%" (Theorem 1 of I, Theorem 4
   of II): a density-1 limit statement, tolerating an unlocalized $o(N(T))$ exceptional
   multiset by construction.
2. **The error classes of the hypotheses.** PCC carries $o(TL)$; AH carries $R(T) \to 0$
   and $R_P(T) \to 0$ with no rates. The engine is linear in these errors, so the residual
   is exactly the hypothesis's slack, re-expressed: the proofs end at
   $N^{\circledast}(T) = TL + o(TL)$ and can end nowhere sharper.
3. **The ladder is linear and completeness is at no rung.** GLSS I Remark 4: "In place of
   HMH, we can apply this method with $N^{\circledast}(T) \le (\mathbf{C}+o(1))TL$, where
   $1 \le \mathbf{C} < 2$. This will give us weaker proportions of the zeros depending on
   the size of the constant $\mathbf{C}$, see [GS25, Theorem 3 and Section 7]." [FETCHED-P]
   The [GS25] ladder (arXiv:2511.20059, targeted-fetched on two routes for this note) is
   linear: hypothesis $\mathbf{C}$ buys simple-and-critical proportion $\ge 2-\mathbf{C}$
   [FETCHED-P, GS25 Theorem 3]. Even the best possible correlation input,
   $\mathbf{C} = 1$ exactly, lands at density 1, not at all zeros: completeness does not
   correspond to any value of the input parameter.
4. **RH-orthogonality of the engine.** GLSS I Remark 2: "Assuming RH, the error term in
   (5.6) can be improved to $O(T)$, but this does not improve any results we obtain from
   Proposition 1." [FETCHED-P] Even assuming the target's conclusion, the mechanism's
   output does not sharpen: the binding slack is the funded input's error class, not the
   unconditional budget's.

**The structural anatomy of the residual (own synthesis, assembled from displayed
equations; not a claim of the papers).** Write $h(\gamma)$ for the multiplicity mass on
the line $t = \gamma$ and $E(T) := N^{\circledast}(T) - N(T) = \sum_{\text{lines}} h(h-1)$.
Every off-line zero and every multiple zero lies on a line with $h \ge 2$, and
$\sum_{h\ge2 \text{ lines}} h \le E(T)$, so

$$\#\{\text{off-line zeros up to } T\} + \#\{\text{non-simple zeros up to } T\} \ \ll\ E(T).$$

The theorems certify $E(T) = o(TL)$; RH-plus-simplicity is the statement $E(T) = 0$ (and
since each $h(h-1)$ is even, $E < 2 \iff E = 0$: completeness is an exact-zero statement
about the same observable). So the certified quantity and the completeness quantity are
literally the SAME functional at two error classes: $o(TL)$ versus $< 2$. The residual has
no further structure: no $\beta$-localization (a pair at $\beta = 0.99$ and a pair at
$\beta = \tfrac12 + \varepsilon$ cost the identical one unit of excess $H$), no
$\gamma$-localization, no rate. And the gap is doubly floored in print: even granting the
correlation law exactly (no $o(TL)$ slack), the exchange identities carry
$O(T\sqrt{\log(2+\lambda)})$ (Fujii, unconditional) or $O(T)$ (on RH, Remark 2), so the
engine's output precision on $E(T)$ is never better than $O(T)$ while completeness needs
$< 2$. The input class and the engine are both density-normalized; the completeness clause
lives at absolute count. This is the frame's Wall 2 (#206, #208) in the papers' own
variables, and it is the exact anatomy F2a's class definition must capture.

## 3. The input-class typing

**What the hypotheses consume.** Both hypothesis classes are **zero-side vertical-marginal
correlation data**: counting functions of ordinate gaps of the full strip-zero multiset,
at the $TL$ normalization, with vanishing relative error. No prime-side data appears in
any hypothesis. Prime data enters each proof at exactly one place: Fujii's unconditional
second moment, of which GLSS I says "This result depends on an unconditional explicit
formula of Selberg for $S(t)$ [Sel46, Theorem 2] and to the authors' knowledge, there is
no easy proof for that." [FETCHED-P] The funding ledger of the mechanism is therefore:
the counting frame is funded by FE + argument principle (Riemann-von Mangoldt); the
quadratic budget is funded by primes (Selberg's explicit formula through Fujii); the bulk
pair mass is funded by the conjecture; and the certificate ($N^{\circledast}$, hence
location density) is the **residue** of budget minus bulk. Structurally parallel to AF's
ledger as corrected at #208 (trace funded zero-side, primes fund only the HS budget): in
both record-holding mechanisms the primes fund a second-moment budget and the certified
quantity is a residue. The prime-side parametrization of the LAW itself (the
Goldston-Montgomery $F(\alpha) \leftrightarrow$ short-interval-variance dictionary) is
avoided BECAUSE it costs RH (GLSS II's own sentence, Section 1.2 above); at this register
the conjectural bridge from Hardy-Littlewood prime-pair data to PCC is heuristic only.
So: GLSS-class certificates are funded by **correlation data of the zero side**, with
primes appearing once, below the hypothesis, in the budget's proof.

**(a) Would the mechanism pose for D-H?** Checkable from the papers' step inventory. The
structure-side steps pose verbatim: D-H has real Dirichlet coefficients and the
$s \mapsto 1-s$ functional equation, so the reflection + FE four-fold symmetry, the
multiset counting conventions, the Riemann-von Mangoldt frame with $S \ll \log T$, and
Proposition 1 (pure Lebesgue-measure bookkeeping) all carry over; a "D-H PCC" or "D-H
AH-Pairs" is a well-posed statement about D-H ordinates, and the horizontal-multiplicity
conversion (off-line zero $\Rightarrow$ partner on the same line) holds for D-H exactly as
for zeta. What does NOT carry is the one prime-funded step: Fujii's budget is proven
through Selberg's explicit formula for $S(t)$, i.e. through the prime parametrization of
$-\zeta'/\zeta$, and for D-H that funding channel is vacuous at the same joint #202(iv)
names for AF: $-f'/f$ has poles in $\sigma > 1$ (D-H's convergence-half-plane zeros), no
Euler product, no prime sum [REPO, #202(iv); the papers themselves say nothing about D-H].
So a D-H version of Theorem 1 would need BOTH the pair law AND the second-moment budget as
hypotheses; for zeta the budget is bought from primes. Two consequences for F2a, honestly
graded. First, the discipline verdict matches the deliberation's expectation exactly: the
zero-side certificate poses for D-H; the prime-side funding fails by vacuity. Second, and
sharper: the CONCLUSION-shape is D-H-consistent. D-H's off-line zeros are believed and
partially known to be a density-zero family ($O(T)$ against $N(T) \asymp T\log T$ for
zeros off fixed strips [SECONDARY, classical density bounds; not verified at source this
session]), and [GS25]'s own text points at the in-print instance: "We mention that Selberg
[Sel92] and Bombieri and Hejhal [BH95] have both made use of ES in their work on linear
combinations of $L$-functions" [FETCHED-P, GS25], where Bombieri-Hejhal (Duke 1995) prove,
under GRH for the components plus spacing hypotheses, that almost all zeros of such
combinations (the D-H class) are simple and on the critical line [SECONDARY, statement
shape not verified at source]. A D-H-class function can SATISFY "asymptotically 100 percent
simple and on the critical line" while violating its own RH. So no theorem with this
conclusion-shape can separate zeta from D-H; at this register the D-H discipline can bite
only at the funding joint, never at the conclusion. That is the vacuity clause of the F2a
scope, with its reason now visible in print.

**(b) Would the mechanism pose for a Beurling system?** No, and the breaks are locatable
from the papers alone, because every location inference routes through named FE steps. A
Beurling generalized zeta (Euler product over generalized primes, no functional equation,
no additive lattice: [`experiments/_shared/beurling.py`](../../../experiments/_shared/beurling.py))
loses three steps. (i) The conclusion's predicate: with no FE there is no distinguished
symmetry axis, so "on the critical line" is not even a well-formed target; the paper's
Section 2 classification (on-line zeros versus symmetric pairs) presupposes the FE. (ii)
The conversion: the four-fold symmetry is what makes $H(\gamma) = 1$ carry location
content; without it an off-line zero forces no partner at its own ordinate, and
PCC + the second-moment engine would deliver at most a simplicity-flavored statement
(one zero per occupied height), with zero horizontal information. The entire horizontal-
multiplicity idea, the paper's self-declared new content, evaporates. (iii) The frame and
the budget: the Riemann-von Mangoldt formula with main term $M(T)$ and $S \ll \log T$ is
proven through the completed function (FE), and Fujii's asymptotic with the specific
$\frac{T}{\pi^2}\log(2+UL)$ has no in-print Beurling analogue (the sibling landscape's gap
4 already recorded that no Beurling comparator exists at this register). Note the Beurling
PRIME side never enters at all: the hypotheses are zero-side. This is consistent with the
deliberation's scope ruling that Beurling enters F2a prime-side only: a GLSS-shaped
certificate is not posable for Beurling, so the Beurling discipline constrains only the
prime-side parametrization of funding (the HL class), which these theorems do not use.

## 4. The law-indifference face (what GLSS II adds)

**What varies between the two funded laws: essentially everything about the law.** PCC is
absolutely continuous with the GUE Fejér shape and quadratic repulsion at $0$; AH is a
singular quasi-lattice law concentrated near half-integer multiples of the mean spacing.
They are mutually contradictory as descriptions of the gap distribution, and the papers
say so: the evidence "supports PCC and contradicts AH" [FETCHED-P]. In Fourier terms one
is the form-factor of GUE and the other the periodized AH form factor [SECONDARY framing;
the papers work in gap space and never use $F(\alpha)$].

**What is invariant: the long-average, equivalently the diagonal mass.** The mechanism
never reads the law's shape. It reads one scalar: after paying the unconditionally-known
Fujii budget, the Fejér-weighted long-average of the law determines the equal-ordinate
residue $N^{\circledast}$. GLSS II states the interface exactly ("The method only obtains
asymptotic formulas when we take long averages over the densities from AH-Pairs"
[FETCHED-P]) and Theorem 1 pins the consumed invariant with an equivalence: given
AH-Pairs, $p_0 = 1 \iff$ ESH. Both laws force the same value of that scalar: PCC because
$\int_0^\infty (\tfrac{\sin\pi\alpha}{\pi\alpha})^2 d\alpha = \tfrac12$ makes the
correlation deficit exactly one zero's worth (GLSS I (8.1)-(8.2)); AH-Weak Density because
the binned densities average to the same deficit ((1.19)-(1.21) and Theorem 3). [GS25]'s
own summary sentence: "correlation conjectures besides PCC also imply ES" [FETCHED-P,
GS25]. And the dependence of the output on the consumed scalar is linear with slope $-1$
(the $\mathbf{C}$-ladder: proportion $\ge 2 - \mathbf{C}$; Corollary 2's partial funding,
AH-Pairs + (AH1) alone, certifies only $\mathbf{C} \le 3/2$ and lands at the 50/50 rung).

**What this says about the funding clause.** The mechanism consumes strictly less than
the full law: one linear functional of the correlation measure (the near-diagonal mass
after the unconditional exchange), constant across the entire "essentially simple" class
of laws that both competitors inhabit. Full-support funding of EITHER contradictory law
therefore yields the identical conclusion, and the conclusion would survive under any
other law with unit deficit. For F2a this cuts precisely: the class definition's "funded
by prime-correlation data" clause should be typed by the FUNCTIONALS THE CERTIFICATE
READS (which linear reads of the correlation measure, at which error class), not by which
law is assumed; a definition typed by law would misdescribe the boundary pair, since the
boundary theorems are law-indifferent. It also strengthens the wall's in-print motivation
exactly as #208 banked it: at maximal funding the pair register cannot even distinguish
which of two contradictory laws is feeding it, let alone resolve the $o(TL) \to O(1)$ gap
that completeness requires.

## 5. Feed to F2a (the class definition)

1. The class must contain finite-precision certificates whose inputs are correlation
   functionals of the zero multiset (vertical-marginal counting functionals at the $TL$
   normalization with $o(TL)$-class error, any gap-scale support), with prime-side
   HL-class families admitted as an alternative parametrization of the same currency,
   because the actual boundary theorems (GLSS I/II) are funded zero-side and reach the
   prime side only through the RH-priced Goldston-Montgomery dictionary they explicitly
   avoid.
2. "Certify location-completeness in the limit" must be defined at the absolute-count
   register ($E(T) = N^{\circledast}(T) - N(T) < 2$, equivalently $= 0$, for all large
   $T$), NOT as density-1 on-line, else GLSS I/II already certify it and the class
   question closes trivially at the wrong register.
3. With those two choices GLSS I/II land inside the class as its full-funding boundary
   cases: they consume a single law-indifferent linear functional of the correlation
   measure and saturate the class's terminal conclusion (density 1, ineffective), with
   the residual equal to the input class's own error slot.
4. To avoid the too-broad failure mode, the definition must NOT bake in "inputs that
   cannot resolve individual zeros" or any M4-consuming clause as a hypothesis: input
   admissibility must be syntactic (which functionals, which normalization, which error
   class), so that the no-go, if provable, is a theorem about a resolution floor rather
   than a restatement of K1.
5. To avoid the too-narrow failure mode, the class must be strictly larger than the
   already-proven blindness instances (#199's line meter, the GUE RH-blindness theorem):
   it must include the GM second-moment engine and the AF rank-trace engine as member
   mechanisms, both of which DO extract location density from correlation input, so that
   the no-go's content is "density is purchasable, the last $o(N(T))$ is not", not
   "correlations see nothing".

## 6. Discrepancy log (reported, not resolved; SURVEYOR does not adjudicate)

1. **#208's GLSS sentence, an attribution nuance.** #208 banks the datum as "full-support
   pair correlation of EITHER competing law ... yields 100 percent simple-and-on-line
   WITHOUT RH, and NEITHER yields RH". The first clause is verified at source. The second
   clause is true as a statement about what the theorems prove, but it is nowhere claimed
   in the papers: the sweep (Section 2) shows the GLSS pair contains no RH-reach
   disclaimer at all. Future citations should not put "RH is out of reach" in GLSS's
   mouth; that quote is AF's [REPO, #202]. The papers are silent, and the silence is
   itself a datum: the boundary papers do not pose the completeness question.
2. **Landscape row D4's "J. Number Theory (2026)".** Corroborated: a ScienceDirect
   article page exists for GLSS II in J. Number Theory (S0022314X26001101) [SECONDARY,
   search-surfaced, paywalled]. But the arXiv record carries no journal_ref and no v2
   (raw export-API check, 2026-08-26), so any journal-version deltas against the v1 read
   here are unchecked.
3. **Row D4 compresses two hypotheses.** The ladder row "full-support AH-PCC, no RH
   $\to$ 100%" is Theorem 4, which needs AH-Pairs AND AH-Weak Density ((AH1) + (AH2)).
   With AH-Pairs + (AH1) only, the in-print conclusion is Corollary 2's 50/50 rung. The
   headline is right; the class definition should carry the two-hypothesis structure,
   since the diagonal bin $P_0$ is deliberately not assumed ("make no assumption on
   $P_0(T)$" [FETCHED-P]).
4. **[BGSTB25a] now has a number.** GLSS II cites "The alternative hypothesis for zeros
   of the Riemann zeta-function, preprint, 2025"; a search surfaces it as
   arXiv:2508.10857 [SECONDARY, not deep-read]. Its RH-conditional Theorem 1 is quoted
   inside GLSS II as (1.14)-(1.15): $1 + o(1) \le P_0(T) \le \tfrac32 - \tfrac{2}{\pi^2}
   + o(1) = 1.29735\ldots$, with the odd/even $P_{k/2}$ asymptotics [FETCHED-P via GLSS
   II's own display].
5. **Instrument note.** pdftotext silently drops overlines: "$1-\bar\rho$" extracted as
   "$1-\rho$" (GLSS I Section 2). Caught by the two-route discipline; trivial here, but
   the same artifact on a load-bearing conjugation would invert a statement. Two-route
   verification of displayed math should compare against the .tex, not a second PDF
   renderer.

## 7. References to follow (not read this session unless stated)

- **[GS25]** Goldston-Suriajaya, "Zeta zeros on the critical line", arXiv:2511.20059
  (targeted-fetched, two routes, Theorem 3 + Section 7 + the BH/ES sentence only): the
  $\mathbf{C}$-ladder's proofs, including the three-output form (simple-and-critical
  $\ge 2-\mathbf{C}$; average of the two proportions $\ge (3-\mathbf{C})/2$;
  simple-or-critical $\ge (4-\mathbf{C})/3$). The quantitative rung structure F2a's class
  should reproduce internally.
- **[Mue83]** Mueller, "Arithmetic equivalent of essential simplicity of zeta zeros",
  Trans. AMS 275 (1983) [SECONDARY]. Flagged as the single most F2a-relevant pointer in
  the citation graph: an ARITHMETIC (prime-side) equivalent of exactly the invariant
  scalar the mechanism consumes (ES). If it holds up, it is the in-print bridge that
  re-parametrizes the GLSS boundary cases' funding in prime-correlation currency without
  the RH-priced dictionary, which is what clause 1 of Section 5 needs.
- **[BGSTB25a]** arXiv:2508.10857, the AH-Pairs formulation source and the RH-conditional
  density theorem.
- **[GM87]** Goldston-Montgomery, whose Lemma 9 is GLSS II's unconditional near-diagonal
  bound (1.12) [FETCHED-P as used in GLSS II].
- **[BH95]** Bombieri-Hejhal, Duke 80 (1995), and **[Sel92]** Selberg's Amalfi paper
  [both SECONDARY]: essential simplicity consumed for linear combinations of
  L-functions: the D-H-class face of Section 3(a).
- **[Fuj74, Fuj81, Tsa84/86]** the budget's unconditional source (Selberg's explicit
  formula for $S(t)$): where the primes actually sit in the GLSS mechanism.

## 8. What this enables / what remains open

**Enables.** (i) F2a can now write the class definition against exact boundary
statements: the two hypothesis classes of Section 1 (with displayed functionals, error
classes, and uniformity clauses), the consumed invariant (one law-indifferent linear
functional; Section 4), and the completeness register ($E(T) < 2$ versus the certified
$E(T) = o(TL)$; Section 2): the definition's "full-funding boundary" clause can cite this
note rather than re-derive. (ii) The discipline scope of the F2a definition is now
evidenced, not just ruled: D-H vacuity is located at the one prime-funded step (Fujii via
Selberg), and the conclusion-shape's D-H-consistency (BH95 via GS25's pointer) shows the
discipline can only ever bite at the funding joint at this register. (iii) The
theorem-shape target for F2b inherits two in-print floors to formalize: the input class's
$o(TL)$ slack and the exchange identity's $O(T)$-class error, both below which no
GM-engine certificate can see. (iv) The discrepancy log gives SYNTHESIZER the #208
attribution nuance before it fossilizes.

**Open.** (a) Whether Mueller 1983's arithmetic equivalent of ES actually delivers a
prime-side parametrization of the GLSS boundary cases (deep read not done; if yes, the
F2a class can be posed purely prime-side without tautology; if no, the class definition
must admit zero-side functionals as first-class funding, and the D-H vacuity clause needs
the two-sided wording of Section 5, item 1). (b) The journal version of GLSS II is
unchecked against v1. (c) The D-H off-line zero-density facts used in Section 3(a) are
[SECONDARY]; a VERIFIER-grade use would need Bombieri-Hejhal and a density bound for D-H
verified at source. (d) Nothing in this note touches whether the $o(TL) \to O(1)$ gap can
be crossed by a NON-GM-engine certificate consuming correlation data at growing support:
that is exactly F2b's question, and this note's content is the evidence that the two
record-holding engines in print (GM/GLSS and AF) both sit on the same side of it.
