# Verifying the Alpöge-Furman prime-side funding inputs at source (Aryan; BGSTB)

> SURVEYOR verification note, 2026-08-26. Frame session F1 of the funding-boundary frame,
> survey half (ii): the adversary-mandated verify-at-source item from
> [`../successor_frame_deliberation.md`](../successor_frame_deliberation.md) Section 7 (F1)
> and its A1 fix. Companion to the deep read
> [`alpoge_furman_two_thirds.md`](alpoge_furman_two_thirds.md) (#202). Purpose: resolve the
> "Aryan" and "BGSTB" abbreviations from the AF bibliography at source; record the credited
> mean-value statements, their scope, unconditionality, and stated barriers; cross-check the
> AF paper's use against them; and record the Lean-hypothesis boundary as the AF paper
> itself states it.
>
> Evidence rules used. Every load-bearing quotation was fetched on TWO independent routes
> before being written: the AF paper via its arXiv LaTeXML HTML (v1 and v2) AND its LaTeX
> e-print source (`paper-v5-draft18.tex`); Aryan via the arXiv e-print LaTeX AND the ar5iv
> HTML build; BGSTB via the arXiv e-print LaTeX AND the ar5iv HTML build (plus the
> independent restatement in GS26's source). Tags: [FETCHED] = seen in raw fetched source
> text by this surveyor; [SECONDARY] = mediated by a fetch-summarizer (used only for
> abstract-page metadata). Quotes are verbatim except that source en/em dashes are
> transcribed as hyphens per house style, and LaTeX macros are expanded to their displayed
> meaning. No em dashes anywhere.

## 0. The abbreviations resolved at source

From the AF bibliography (arXiv:2608.13637, v2 HTML References section, confirmed in the
LaTeX source) [FETCHED]:

- **[Ary22] = "Aryan"**: F. Aryan, *On an extension of the Landau-Gonek formula*, J.
  Number Theory 233 (2022), 389-404. arXiv id resolved by arXiv API title+author search:
  **arXiv:1902.05473** (single version, v1, 2019-02-14; author Farzad Aryan; abstract
  matches the e-print source) [FETCHED via API + e-print; abs metadata SECONDARY].
- **[BGSTB24] = "BGSTB"**: S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya, C. L.
  Turnage-Butterbaugh, *An unconditional Montgomery theorem for pair correlation of zeros
  of the Riemann zeta-function*, Acta Arith. 214 (2024), 357-376. arXiv id resolved by API
  title search: **arXiv:2306.04799** (v1, 2023-06-07; journal ref and DOI
  10.4064/aa230612-20-3 on the abs page) [FETCHED via API + e-print; abs metadata
  SECONDARY].

Where the AF paper credits them, at source [FETCHED, both routes]:

- Abstract: "The analytic inputs are those of Aryan and of Baluyot, Goldston, Suriajaya
  and Turnage-Butterbaugh."
- The (P) box, §1.2: "$\|\widetilde G\|_{\mathrm{HS}}^2 = (R(\psi)+o(1))N$, where
  $R(\psi)$ depends only on the window (Lemma 5.6): $R(\psi_0) = \tfrac43$ for the
  indicator, $R(\psi_{\mathrm{MT}}) = c_{\mathrm{MT}}^{-1}$ for Montgomery-Taylor. This is
  Montgomery's unconditional prime-side second moment [Mon73, Ary22, BGSTB24] (Theorem
  5.7)."
- §1.3: "Aryan [Ary22] made this explicit for the Fejér-kernel second moment, and Baluyot,
  Goldston, Suriajaya and Turnage-Butterbaugh [BGSTB24] then showed that Montgomery's form
  factor itself holds for the sum over all complex zeros."
- Acknowledgments: "the unconditional second-moment identity underlying input (P) was
  first proved by F. Aryan [Ary22] and extended to the pointwise form factor in [BGSTB24]."

The AF §7.1 display co-cites a third source for the exact smoothed statement: "([Ary22,
Cor. 1.4]; [BGSTB24, Theorem 1]; [GS26, Lemma 2])", with [GS26] = D. A. Goldston, A. I.
Suriajaya, *Zeta zeros in a narrow vertical box*, arXiv:2603.28104 (2026) [FETCHED].
Section 3 below records that statement too, since the triple is how AF cites the identity
it names.

## 1. Input 1 at source: Aryan, arXiv:1902.05473 ([Ary22])

**The statement the AF credit points at (Corollary 1.4; compiled numbering identical on
both routes: the e-print label is literally `1--4`, and the ar5iv build prints "Corollary
1.4")** [FETCHED x2]:

> Corollary 1.4. Let $0 < \alpha < 1$, and consider the Sine function as a complex valued
> function. We have that
> $$\sum_{\zeta(\rho)=0}\omega(\rho)\sum_{\zeta(\rho')=0}\Bigl(\frac{\sin(\tfrac{\alpha}{2}(\rho-\rho')\log T)}{\tfrac{\alpha}{2}(\rho-\rho')\log T}\Bigr)^2 = \frac{\log T}{2\pi}\Bigl(\frac{1}{\alpha}+\frac{\alpha}{3}\Bigr) + O\Bigl(\frac{1}{\log^2 T}\Bigr).$$

Here $\omega(s) = \frac{1}{\sqrt\pi\Delta}e^{(s-(1/2+iT))^2/\Delta^2}$ is a Gaussian
window centered at $\tfrac12+iT$ of width $\Delta = T(\log T)^{-1}$ (his Theorem 1.1/1.3
setup) [FETCHED]. Both zero sums run over ALL nontrivial zeros as complex numbers; no RH.
This is the unconditional version of Montgomery's RH-conditional Fejér-kernel second
moment, which Aryan displays first and attributes to Montgomery (his (1.2)): on RH,
$\sum_{0<\gamma,\gamma'<T}\bigl(\frac{\sin(\frac{\alpha}{2}(\gamma-\gamma')\log T)}{\frac{\alpha}{2}(\gamma-\gamma')\log T}\bigr)^2 \sim (\frac1\alpha+\frac\alpha3)\frac{T}{2\pi}\log T$.
At $\alpha \to 1$ the constant is $\tfrac43$.

**The engine behind it (his Theorem 1.3)** [FETCHED]: an extension of the Landau-Gonek
formula. With the Fejér-type kernel $W_\rho(s) = \bigl(\frac{T^{\alpha(s-\rho)/2}-T^{-\alpha(s-\rho)/2}}{s-\rho}\bigr)^2$
and $x = r/s$ a ratio of integers with $r, s < T^{1-\alpha}\log^{-5}T$, the double zero
sum $\sum_\rho \omega(\rho)x^\rho\sum_{\rho'}W_\rho(\rho')$ evaluates in closed form,
supported on $x = p^iq^j$, $p^i$, $p^iq^{-j}$ (products of two prime powers); the $x = 1$
case is
$\sum_\rho\omega(\rho)\sum_{\rho'}W_\rho(\rho') = \frac{1}{6\pi}(\alpha\log T)^3 + \frac{\alpha}{2\pi}\log^3 T + O(1)$,
which rescales to Corollary 1.4.

**Scope and uniformity** [FETCHED]: $0<\alpha<1$ strict; window average at height $T$
(width $T/\log T$), i.e. a per-unit-density normalization $\frac{\log T}{2\pi}(\cdot)$
rather than a $[0,T]$ count; the ratio restriction $r, s < T^{1-\alpha}\log^{-5}T$ in the
general-$x$ theorem; error $O(1/\log^2 T)$ in the $x=1$ corollary.

**Unconditionality** [FETCHED]: Theorem 1.3 and Corollary 1.4 carry no RH/GRH/pair
correlation hypothesis. The abstract: "we recover unconditionally some of the consequences
of a pair correlation estimate that previously was known under the Riemann hypothesis."
The proof inputs are a smoothed Landau formula (his Lemma 2.1), the functional equation,
and classical prime sums; no zero-density input for the identity itself.

**The conditional companion AF also cites (Corollary 1.5; both routes print "Corollary
1.5")** [FETCHED x2]:

> Corollary 1.5. For $\sigma > 1/2$, assume the zero density hypothesis
> $N(\sigma,T) \ll T^{2(1-\sigma)}\log^{-B}$, with $B > 4$. Then at least two-third of the
> zeros are simple.

(sic "two-third"). AF's §7.1 parenthetical "(Aryan [Ary22, Cor. 1.5] had earlier obtained
$\ge\tfrac23$ simple zeros under a zero-density hypothesis)" matches this exactly.

**Barrier remarks in Aryan's own text** [FETCHED]:

- The off-diagonal collapse is purchased by the LENGTH restriction: in the proof, "since
  we assumed $r < T^{1-\alpha}\log^{-5}T$ we get $sn < T\log^{-5}T$, and because of this
  the off-diagonal contribution is negligible." Past that length nothing is claimed.
- Weight-class remark: "Rudnick and Sarnak [RS] also proved pair correlation results
  unconditionally, assuming the weight satisfy certain conditions including exponential
  decay. The Fejer Kernel dose not satisfy the exponential decay." (sic). So his result is
  not subsumed by Rudnick-Sarnak.
- The alternative to the zero-density hypothesis in Cor 1.5 is an explicit non-clustering
  hypothesis on off-line zeros (real parts $|\beta-\tfrac12| > \frac{\log\log T}{\log T}$,
  imaginary gaps $> 4$), which he flags as "somehow a troublesome condition."
- No statement about support/length beyond $T$ appears; the paper simply stops at its
  restriction.

**Numbering caveat, stated honestly.** The arXiv posting has only v1 (2019); the published
2022 J. Number Theory version was not fetched (paywall). The citation numbering "Cor.
1.4/1.5" is corroborated three ways: the e-print's own label `1--4`, the ar5iv compiled
numbers, and GS26's independent attribution of exactly this identity to [Ary22] (Section 3
below). Residual risk that the JOURNAL version renumbered is small and would not change
any content above.

## 2. Input 2 at source: Baluyot-Goldston-Suriajaya-Turnage-Butterbaugh, arXiv:2306.04799 ([BGSTB24])

**Definitions** [FETCHED x2]: for $x > 0$, $T \ge 3$,
$$F(x,T) := \sum_{\substack{\rho,\rho' \\ 0<\gamma,\gamma'\le T}} x^{\rho-\rho'}\,w(\rho-\rho'), \qquad w(u) := \frac{4}{4-u^2},$$
zeros counted with multiplicity, over ALL nontrivial zeros (no RH; "if RH holds then
[this] agrees with" Montgomery's $\sum x^{i(\gamma-\gamma')}\frac{4}{4+(\gamma-\gamma')^2}$),
and $F(\alpha) := (\frac{T}{2\pi}\log T)^{-1}F(T^\alpha,T)$.

**Theorem 1 (the credited statement), verbatim** [FETCHED x2]:

> Theorem 1. The function $F(\alpha)$ is real, even, and nonnegative. Moreover, as
> $T \to \infty$, we have
> $$F(\alpha) = T^{-2\alpha}(\log T + O(1)) + \alpha + O\Bigl(\frac{1}{\sqrt{\log T}}\Bigr)$$
> uniformly for $0 \le \alpha \le 1$.

Their own gloss: "Theorem 1 is nearly identical to Montgomery's theorem in
[Montgomery73] and [GM87, Lemma 8] except it does not assume RH, and it includes the
improvements from [GM87, Lemma 8] where [the asymptotic] holds up to $\alpha = 1$ with
explicit error terms. The proof is also nearly identical."

**Scope and uniformity** [FETCHED]: uniform on the closed interval $0 \le \alpha \le 1$,
i.e. Dirichlet-polynomial length $x = T^\alpha$ up to $x = T$ inclusive; window $[0,T]$ in
ordinates. The $[T,2T]$ variant AF needs is not in this paper; per GS26 (Section 3) it is
proved in [BGSTB25] (arXiv:2501.14545): "The theorem also holds if we replace
$0<\gamma,\gamma'\le T$ with $T<\gamma,\gamma'\le 2T$", "the proof ... is in [BGST-CL]"
[FETCHED in GS26 source].

**Proof structure (what funds what)** [FETCHED]: Montgomery's explicit-formula identity
(their Lemma 1, attributed to Montgomery): for $\rho = \tfrac12+\delta+i\gamma$, $x\ge1$,
all $t$,
$$\sum_\rho \frac{2x^{\delta+i(\gamma-t)}}{1+((t-\gamma)+i\delta)^2} = -\sum_{n=1}^\infty \frac{\Lambda(n)}{n^{1/2+it}}\min\Bigl(\frac nx,\frac xn\Bigr) + x^{-1}(\log(|t|+2)+O(1)) + O\Bigl(\frac{x^{1/2}}{1+t^2}\Bigr) + O\Bigl(\frac{x^{-5/2}}{|t|+2}\Bigr).$$
Squaring and integrating over $t \in [0,T]$: $L(x,T) = R(x,T)$; the zero side gives
$F(x,T)$ via their Lemma 4, and the arithmetic side is evaluated unconditionally
(Montgomery, improved by [GM87]) as
$R(x,T) = x^{-2}T\log T(\log T + O(1)) + T(\log x + O(\sqrt{\log T}))$ for $0 \le x \le T$:
the $x^{-2}T\log^2T$ term is the archimedean/density part, the $T\log x$ term is the prime
DIAGONAL $\sum_n \Lambda(n)^2 n^{-1}\min(n/x,x/n)^2$, and the off-diagonals are absorbed
into the error by the mean-value theorem for Dirichlet polynomials (the length restriction
$x \le T$ is what keeps them there, surfacing as the $O(x)$ term in their (Lfinal)).

**Unconditionality, stated precisely** [FETCHED]: no RH, no GRH, no pair-correlation or
Hardy-Littlewood hypothesis. One non-elementary classical input IS consumed: the passage
from $L(x,T)$ to $F(x,T)$ (their Lemma 4) uses the Korobov-Vinogradov zero-free region.
Their own text: "The current widest known zero-free region $\sigma \ge 1-\eta(t)$ was
obtained independently by Korobov and Vinogradov with
$\eta(t) = c/((\log t)^{2/3}(\log\log t)^{1/3})$", used to bound the
$O(x^{1-2\eta(T\log^2T)}\log^3T)$ term. This matters for the cross-check (Section 4,
finding 2): AF's in-house proof of the same species of statement avoids even this.

**Barrier remarks in BGSTB's own text** [FETCHED]:

- The scope claim simply stops at $\alpha = 1$; the paper contains no analysis of
  $\alpha > 1$ (the equivalence of that range with Hardy-Littlewood-type prime-pair data
  is in the literature they and AF both cite, [Mon73, GM87], not re-proved here).
- The location-blindness remark, in print, their own words: "The pair correlation method
  developed in this paper neither requires nor provides any information as to whether or
  not the nontrivial zeros of $\zeta(s)$ satisfy $\beta = 1/2$." (Remark after their
  Theorem 2.) This is exactly the species of the repo's #199 line-meter certificate and
  the primes-thread GUE blindness datum, from the mechanism class's own authors.
- Their conditional companions: Theorem 2 (thin box $|\beta-\tfrac12| < \frac{1}{2\log T}$
  for $T^{3/8} < \gamma \le T$ gives at least $61.7\%$ simple) and Theorem 3 (a strong
  zero-density hypothesis $N(\sigma,T) = o(T^{2(1-\sigma)})$ on
  $\tfrac12+\tfrac{1}{2\log T} \le \sigma \le \tfrac{25}{32}+\eta$ gives the same), with
  the Selberg-conjecture discussion crediting Aryan's Cor 1.5 device: "In a recent paper,
  Aryan [Ary22] used this type of conjecture as a replacement of RH to obtain Montgomery's
  result on simple zeros."

## 3. The co-cited composite statement: GS26 Lemma 2 (arXiv:2603.28104)

AF's §7.1 cites the exact display "([Ary22, Cor. 1.4]; [BGSTB24, Theorem 1]; [GS26,
Lemma 2])". At the GS26 source [FETCHED]: the lemma counter is independent of the theorem
counter, so the first-appearing lemma (the close-pairs bound, source label `lem2`)
compiles as Lemma 1 and the second (source label `lem1`, headed "Lemma (Aryan)") compiles
as **Lemma 2**, which reads:

> $$\sum_{\substack{\rho,\rho'\in\mathcal Z \\ 0<\gamma,\gamma'\le T}}\Bigl(\frac{\sin(\frac12 i(\rho-\rho')\log T)}{\frac12 i(\rho-\rho')\log T}\Bigr)^2 W(\rho-\rho') = \Bigl(\frac43+o(1)\Bigr)\frac{T}{2\pi}\log T,$$
> $W(u) = \frac{4}{4-u^2}$, unconditional, all complex zeros with multiplicity; "In both
> results, we can also replace $0<\gamma,\gamma'\le T$ with $T<\gamma,\gamma'\le 2T$."

Its proof, in full view at source, is the Fejér identity
$\int_{-1}^1 e^{z\alpha}(1-|\alpha|)d\alpha = \bigl(\frac{\sin\frac12 iz}{\frac12 iz}\bigr)^2$
applied under $\int_{-1}^1 \mathcal F(\alpha,T)(1-|\alpha|)d\alpha$ with
$\mathcal F$ = BGSTB24's unconditional form factor (restated as "Montgomery Theorem (MT)"
with "The proof of this theorem is in [BGST-PC]" = BGSTB24). GS26 attributes the lemma "a
form of" it to Aryan: "More recently, Aryan [Ary22] obtained a form of the unconditional
part of this lemma." So the composite is: Aryan proved the smoothed local version at
$\alpha < 1$ first; BGSTB24 proved the pointwise form factor uniformly to the endpoint;
GS26 Lemma 2 is the endpoint Fejér statement AF's display transcribes, obtained by
integrating BGSTB24. AF's phrase "up to the choice of smoothing" is carrying exactly this
difference. (GS26's Theorem 1, also sighted at source, is the [BGSTB25] box theorem: all
zeros in a box of width $b/\log T$, $b \to 0$, between $T$ and $2T$ implies asymptotically
at least $2/3$ simple and on the line; context for AF's §7.1 comparison, not a funding
input.)

## 4. Cross-check: AF's use against the credited statements

**Finding 1 (structural; the main answer to the daylight question). The AF paper does not
import either credited theorem. It re-proves the needed evaluation in-house, and the
credits are priority/lineage credits.** At source, input (P) is AF's own Theorem 5.7,
$\|\widetilde G\|_{\mathrm{HS}}^2 = (R(\psi) + O_\chi(L^{-1}))N(T,2T)$ [FETCHED x2],
proved in §§5.1-5.4 from: the Poisson-Gabor frame identity (Lemma 2.1, proved in-paper),
the explicit formula (2.2) in the [BGSTB24]-compatible normalization ("our normalisation
agrees with [BGSTB24]"), Chebyshev-Mertens estimates (Lemma 5.1, cited to [MV07, §2.2] and
[IK04, Theorem 2.7]), and the Montgomery-Vaughan weighted Hilbert inequality (Lemma 2.2,
cited to [MV74, Theorem 2]). The in-text sentence at (P), "This is Montgomery's
unconditional prime-side second moment [Mon73, Ary22, BGSTB24] (Theorem 5.7)", names the
identity's class and its ancestry, and the acknowledgments assign priority ("first proved
by F. Aryan [Ary22] and extended to the pointwise form factor in [BGSTB24]"); the proof
chain of Theorems A/B cites the two papers nowhere as a consumed step. Consequence for
F1: there is NO imported-statement scope to mismatch; the correctness surface is AF's own
§5 (plus §2 and §4), not the credited papers' theorems. The deliberation's phrase "the
Aryan/BGSTB support-1 mean values [are] the AF Lean formalization's carried hypotheses"
is wrong in both halves at source (see Section 5 for the second half).

**Finding 2 (input strength; daylight in AF's favor).** BGSTB24's own unconditional proof
consumes the Korobov-Vinogradov zero-free region (their Lemma 4, quoted in Section 2). AF
§1.1 states, of its whole argument: "The arithmetic inputs are Weil's explicit formula,
the Riemann-von Mangoldt formula and the bound $N(t,t+1) \ll \log t$, Stirling's estimate
for $\Gamma'/\Gamma$, Chebyshev-Mertens estimates for $\sum_{n\le X}\Lambda(n)^2$ and
$\sum_{n\le X}\Lambda(n)^2/n$, and the Montgomery-Vaughan inequality for the frequencies
$\{\log n : n \le X\}$, $X \le T$. No mollifier, zero-density estimate, or zero-free
region is used." [FETCHED x2]. So AF's in-house (P) is proved from strictly weaker inputs
than the credited BGSTB24 route: the compression-plus-$C^2$-window tail bound (their Prop
4.3 and Remark 4.4) does the work BGSTB24's zero-free region does in the $L \to F$
passage. This is a genuine difference between the funded object and its credited
ancestors, and it strengthens, not weakens, the unconditionality claim.

**Finding 3 (the §7.1 display is a composite, accurately assembled).** Aryan's Cor 1.4 at
source is stated for $0 < \alpha < 1$ strict, in the Gaussian-window per-unit-density
normalization; AF's §7.1 display is the $\alpha = 1$ endpoint statement for the full
ordinate count with the weight $W$. That endpoint statement is exactly GS26's compiled
Lemma 2, which exists because BGSTB24's Theorem 1 is uniform on the CLOSED interval
$0 \le \alpha \le 1$. Read singly, either credit would over- or under-state ([Ary22] alone
lacks the endpoint and the count normalization; [BGSTB24] alone lacks the Fejér
smoothing); read as the cited triple with AF's own qualifier "up to the choice of
smoothing," the attribution is exact. Verdict: no daylight, conditional on reading the
citation as the triple it is.

**Finding 4 (support arithmetic).** AF fixes $L := \log(T/2\pi)$ and $X := e^L = T/(2\pi)$
[FETCHED x2]: polynomial length exactly at the support-1 endpoint (in Montgomery's
normalization $x = T^\alpha$, $\alpha = 1$ up to the $2\pi$), matching the credited
statements' validity edge ($0 \le \alpha \le 1$ for BGSTB24; $\alpha \to 1$ limiting value
$\tfrac43$ in Aryan). The reading note's "valid at Fourier support $\le 1$ ($X \le T$)" is
accurate.

**Finding 5 (repo-side imprecision, minor, for the discrepancy log).** The reading note's
mechanism summary says "$\mathrm{tr}\,\widetilde G$ and $\|\widetilde G\|_{HS}^2$ are
evaluated by the explicit formula plus Montgomery's classical prime-side mean values." At
source the two budgets are funded differently: $\mathrm{tr}\,\widetilde G = N(I') +
O_\chi(T^{1/2}L^2)$ is Proposition 4.2, proved zero-by-zero from the Gabor frame identity
plus the Riemann-von Mangoldt count and $N(t,t+1) \ll \log t$; no prime sum enters the
trace. The prime side funds ONLY the Hilbert-Schmidt budget (and would fund higher traces
$\mathrm{tr}\,\widetilde G^k$ only in the Rudnick-Sarnak range $X^k \le T^{2-\varepsilon}$,
which at $X \asymp T$ "allows only $k = 1$", §7.2(e) [FETCHED x2]). Also (P)'s error at
source is $O_\chi(L^{-1})$, sharper than the $o(1)$ carried in the summary box.

## 5. The Lean-hypothesis boundary, as the AF paper itself states it

What the paper claims, verbatim, Appendix A (identical in v1 and v2; both HTML and LaTeX
routes) [FETCHED x2]:

> "The top-level declarations for Theorem A, in `Zeta23/Unconditional.lean` and
> `Zeta23/FinalMult.lean`, are reproduced below; their types carry no hypotheses. ... The
> counting functions of §1.1 are defined directly against Mathlib's `riemannZeta`, and the
> analytic inputs of §2 appear in the repository as theorems in their own right rather
> than as hypotheses of the main theorems; several are ported, with attribution, from the
> PrimeNumberTheoremAnd project [PNT+]. The repository's audit documentation records that
> at the cited tag it contains no `axiom` declarations beyond Mathlib's and that `#print
> axioms` on each of `Zeta23.two_thirds_on_critical_line`, `Zeta23.thmB0_mult`,
> `Zeta23.thmC0_mult`, and the corresponding declarations for the Montgomery-Taylor
> constants and for Theorem B, returns only the three standard axioms `propext`,
> `Classical.choice`, `Quot.sound`, with no `sorry`."

The hypothesis-carrying and kernel-external pieces the paper DOES declare are confined to
§7.2's bandwidth-one ceiling and Remark 7.2, not to Theorems A/B [FETCHED x2]:

- The ceiling theorem `Zeta23.PairCeiling.ceiling_law256` holds "under two hypotheses:
  `hvalid` ... and `EnclOK`, certifying the form-factor enclosures"; "the enclosures
  `EnclOK` are certified by interval arithmetic and are not checked by the Lean kernel";
  the expectation-averaging step "is carried out here, not in Lean"; and "This is the only
  place in the paper where a numerical certification enters; the formalisation of Theorems
  A and B is independent of it and depends only on the three standard axioms (§1.5)."
- Remark 7.2 (the Dirichlet family average, $0.811/0.905$): "checked by independent
  derivations but is not included in the Lean formalisation of Appendix A."

**DISCREPANCY (a finding; flagged, not resolved).** The repo's deep-read note
([`alpoge_furman_two_thirds.md`](alpoge_furman_two_thirds.md) §1 and §2(e)) states: "the
analytic prime-side inputs (their §5.1-5.4, the Aryan/BGSTB evaluations) carried as
hypotheses rather than formalized." That sentence does not appear in, and is contradicted
by, the paper text at source in BOTH arXiv versions (v1 2026-08-13, v2 2026-08-19; the
Appendix A sentences above are identical in both). The most likely mechanism, given the
month's two prior catches, is a fetch-summarizer confabulation blending the real §7.2
hypothesis pair (`hvalid`/`EnclOK`) and the real kernel-external enclosures into a
statement about §5; the note's same-day adversary (A4) reports having verified "the
Lean-appendix claim" against its own fetch, so either both fetches hit the same truncated
or summarizer-mediated surface, or a source that has since changed (no evidence of the
latter: both arXiv versions predate the note). Downstream propagation: the successor-frame
deliberation Section 5 ("the prime-side inputs are carried as hypotheses, not formalized,
and that is exactly F1's surface") and this session's own tasking inherit the error.
Adjudication and any correction of #202's note text belong to an ADVERSARY/SYNTHESIZER
pass, not to this note. Two things survive the correction unchanged: (i) F1's
verify-at-source item was worth running regardless (this note is it), and (ii) the
project has still only verified the PAPER'S CLAIM about its repository, not the repository
itself; the queued F2a Lean skim (github.com/anthropics/zeta-23-lean, tag v1.0, toolchain
v4.33.0-rc2, Mathlib revision 51e6992efd06 [FETCHED]) is the confirmation path for the
audit-documentation claims, and is now also the check on `#print axioms` for the five
listed declarations.

## 6. Surface map: exactly which sums the funded budget consists of, as the sources state them

For the frame's F1 build, the unconditionally funded budget of the AF certificate consists
of precisely two evaluated quantities and one family of bounded remainders. (1) The trace:
$\mathrm{tr}\,\widetilde G = N(I') + O_\chi(T^{1/2}L^2)$, funded by the Gabor frame
normalization plus the Riemann-von Mangoldt count; it contains no prime sum at all. (2)
The Hilbert-Schmidt budget: after the reduction (Prop 5.2) it is the double integral of
$\widehat{\phi^2}(\tau-\tau')^2$ against $\nu_X(\tau)\nu_X(\tau')$ over $[T,2T]^2$ with
$\nu_X = \mu + \Pi_X + P_X$ and $P_X(\tau) = -\frac1\pi\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}\cos(\tau\log n)$,
$X = T/(2\pi)$; its two main terms are the archimedean square $\mathcal M[\mu,\mu] =
2\pi bL\int_T^{2T}\mu^2 + O(l^2\log L)$ (contributing $\int\psi^2$ to $R(\psi)$; this is
the diagonal $\rho = \rho'$ of the zero-side reading) and the prime DIAGONAL $n = m$ over
prime powers $n \le X$ at weight $a_n^2 = \Lambda(n)^2/n$ against the window
autocorrelation, $\mathcal D = \frac{T}{\pi}\sum_{n\le X}\frac{\Lambda(n)^2}{n}g(\log n) +
O(L^2\log L)$ with $g = \phi^2 * \phi^2$, evaluated by
$\sum_{n\le x}\Lambda(n)^2/n = \frac12\log^2x + O(\log x)$ (contributing
$\iint|u-v|\psi(u)\psi(v)\,du\,dv$, the $\alpha$-part of the form factor). Everything else
is BOUNDED, not evaluated: the same-sign prime off-diagonal
$\mathcal O_1 = \sum_{n\ne m}$ (four bilinear sums $\sum_{n\ne m}x_n\bar z_m/(\log n - \log m)$)
is $\ll L^2X$ by Montgomery-Vaughan with the separation $\delta_n^{-1} \le 2n$, which the
paper derives from "consecutive prime powers satisfy $\log\frac{n'}{n} \ge \frac1{2n}$"
(unit spacing of integers, i.e. the crudest additive-lattice datum); the opposite-sign sum
$\mathcal O_2 \ll XL$ trivially via $1/\log(nm)$; and the archimedean-prime cross terms
$\ll_\chi L^2\sqrt X$. The balance that defines the funding wall: the evaluated main terms
are of order $TL^3$ while the MV bound on $\mathcal O_1$ is $L^2X$, so domination holds
exactly while $X \lesssim T$; in the paper's own words the restriction "comes from
Proposition 5.4: for $X \gg T$ the off-diagonal prime sum is no longer dominated by the
diagonal, and its evaluation would require information on prime pairs (the
Hardy-Littlewood conjectures, or equivalently Montgomery's pair correlation conjecture for
support $> 1$ [Mon73, GM87])" [FETCHED x2]. In the credited papers the same split appears
as: prime side $-\sum_n\frac{\Lambda(n)}{n^{1/2+it}}\min(\frac nx,\frac xn)$ (effective
weight the tent at scale $x$), mean square over $[0,T]$ giving archimedean
$x^{-2}T\log T(\log T + O(1))$ plus diagonal $T(\log x + O(\sqrt{\log T}))$ for
$0 \le x \le T$ (BGSTB24), and off-diagonal negligibility purchased by the length
restriction $r,s < T^{1-\alpha}\log^{-5}T$ (Aryan). So the F1a/F1b build should treat, at
support $1+\delta$, the newly needed object as the EVALUATION (with sign) of
$\sum_{n\ne m,\,n,m\le X}\frac{\Lambda(n)\Lambda(m)}{\sqrt{nm}}\,K(\log n - \log m)$ for
frame kernels $K$ concentrated at shifts $|\log(n/m)| \lesssim 1/T$ with $X > T$, which is
prime-pair count data at integer shifts $n - m = h$ weighted by the singular-series class;
below support 1 the sources bound it by separation alone and never evaluate it.

## 7. What this enables / what remains open

**Enables.**

- F1's build half can start from a verified surface: the funded budget is exactly the
  Section 6 map (trace = count; HS = archimedean square + prime diagonal; off-diagonals
  bounded by MV separation from unit integer spacing). The typing question F1a ("does the
  data class past support 1 exist only over an additive lattice") now has its
  support-$\le 1$ baseline pinned at source, including where the crude lattice datum
  already enters below the wall (the $\delta_n^{-1} \le 2n$ separation).
- The competitor-typing input the deliberation pre-registered (minor-arc / short-interval
  variance, architecture 4) gains a concrete datum: BGSTB24's unconditional proof consumes
  the Korobov-Vinogradov zero-free region (an architecture-4 object) while AF's in-house
  version eliminates it; at support $\le 1$ the architecture-4 input is thus REMOVABLE.
  Whether it re-enters obligatorily past support 1 is exactly F1's discrimination.
- The discrepancy in Section 5 gives the F2a Lean skim a sharpened checklist: confirm the
  repository audit claims (`#print axioms` on the five named declarations; no `sorry`; no
  extra `axiom`), locate the §5 analytic lemmas as proved theorems, and confirm the only
  hypothesis-carrying declaration is `PairCeiling.ceiling_law256` with `EnclOK` external.
- Two in-print blindness statements from the mechanism's own authors (BGSTB24's
  "neither requires nor provides any information" remark; AF §1.4's "insensitive to $o(N)$
  off-line zeros and hold for Davenport-Heilbronn and Epstein zeta functions") are now
  available verbatim for F2a's class definition and its D-H vacuity clause.

**Open.**

- The repository-level confirmation of the paper's Lean claims (F2a; only the paper's
  self-report is verified here).
- The correction pass on #202's reading-note sentence and the deliberation's Section 5
  wording (ADVERSARY/SYNTHESIZER authority; this note only flags).
- The published (journal) version of [Ary22] was not fetched; corollary numbering is
  corroborated but not journal-confirmed.
- Survey half (i) of F1 (the proportion-vs-support conditional landscape: GS25's Theorems
  2-4, BGSTB25's quantitative box constants, GLSS25 under full pair correlation) is a
  separate task and is not covered by this note beyond the statements incidentally
  verified in Section 3.
