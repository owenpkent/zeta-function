# The proportion-vs-support landscape: what prime-side inputs buy about zeta zeros, in print

> SURVEYOR landscape note, 2026-08-26. Frame session F1, survey half (i), per the
> funding-boundary frame spec ([`../successor_frame_deliberation.md`](../successor_frame_deliberation.md)
> Sections 4 and 7): the map of what conditional and unconditional inputs between Fourier
> support $1$ and full Hardy-Littlewood buy about the zeros of $\zeta$, so the frame never
> re-derives a known conditional result. Companion to
> [`alpoge_furman_two_thirds.md`](alpoge_furman_two_thirds.md) (the record holder, deep-read
> post-adversary at #202). The Aryan and BGSTB support-1 mean values are cited here but
> deliberately not deep-read: a sibling session verifies them at source (F1 survey half (ii)).
> No em dashes anywhere.
>
> **Rules of evidence.** Every load-bearing row is pinned at source. Tiers:
> **[FETCHED-P]** = first-party text extraction from the paper's own PDF (pdftotext on the
> downloaded file; no summarizer in the loop); **[FETCHED]** = arXiv abstract or HTML
> fetched this session AND confirmed on an independent second route (a different endpoint,
> search-index copy, or a repo dossier's prior adversary re-fetch); **[SECONDARY]** = the
> statement is taken from a fetched citing source (the original was not read);
> **[REPO]** = carried by an existing repo dossier whose quotes were adversarially
> re-fetched (#202 standard). Quotations are used sparingly and only at tier [FETCHED-P]
> or double-routed [FETCHED]. Two summarizer fabrications were caught during THIS sweep
> and discarded (Section 8, item 5), consistent with the #202/#207 instrument lesson.

## 1. Conventions: the axes of the table

**Support.** Montgomery's form factor, in the normalization of his 1973 paper and of
Goldston's Newton Institute notes (math/0412313, first-party):

$$F(\alpha) = \Big(\tfrac{T}{2\pi}\log T\Big)^{-1} \sum_{0<\gamma,\gamma'\le T} T^{i\alpha(\gamma-\gamma')} w(\gamma-\gamma'), \qquad w(u) = \tfrac{4}{4+u^2},$$

with the unconditional variant of BGSTB replacing $T^{i\alpha(\gamma-\gamma')}$ by
$x^{\rho-\rho'}$ over full complex zeros. "Support $\le 1$" means $|\alpha| \le 1$, i.e.
prime sums of length $X \le T$: the range where the diagonal dominates. A test/window
$\psi$ with $\hat\psi$ supported in $[-1,1]$ ("bandwidth one") consumes only this data.
In Rudnick-Sarnak's $n$-level normalization the analogous boundary is
$\sum_j |\xi_j| < 2$, which for the pair case is the same wall.

**Proportion.** Four distinct quantities recur and must not be conflated (the AF
bookkeeping made one conflation route load-bearing; see the discrepancy log):
$N_s(T)$ = zeros that are simple; $N_0^s(T)$ = simple AND on the critical line;
$N_d(T)$ = distinct zeros; $N^*(T) = \sum m_\rho$ = the multiplicity-weighted count whose
upper bounds generate the first three via $N_s \ge 2N - N^*$, $N_d \ge N - \tfrac12(N^*-N)$
style inequalities.

**Two directions of the dictionary.** Zeros $\to$ primes (Heath-Brown 1982, Section 5)
and primes $\to$ zeros (Hardy-Littlewood inputs funding $F$ beyond support 1). The
Goldston-Montgomery equivalence is the exact exchange rate between them (row E1).

## 2. The table

| # | Input consumed | Cond.? | What it buys about zeta zeros, in print | Record constant | Source | Tier |
|---|---|---|---|---|---|---|
| **A. Unconditional, Fourier support $\le 1$** | | | | | | |
| A1 | Prime-side mean values at $X \le T$ (Montgomery's classical inputs, unconditional form) | NO | The full Montgomery asymptotic $F(\alpha) = T^{-2\alpha}(\log T + O(1)) + \alpha + O(1/\sqrt{\log T})$ uniformly $0\le\alpha\le 1$, with zeros NOT assumed on the line ($x^{\rho-\rho'}$ form) | asymptotic, closed endpoint $\alpha=1$ | BGSTB, arXiv:2306.04799, Acta Arith. 214 (2024) 357-376 | [FETCHED] |
| A2 | A1 + thin-box hypothesis $\lvert\beta-\tfrac12\rvert < \tfrac{1}{2\log T}$ for $T^{3/8}<\gamma\le T$ (or a strong zero-density hypothesis) | box hyp. | Proportion of simple zeros; "neither requires nor provides" on-line information | $61.7\%$ simple | same | [FETCHED] |
| A3 | Extended Landau-Gonek formula (unconditional pair-correlation-type estimates) | zero-density hyp. | $2/3$ of zeros simple under a zero-density hypothesis weaker than RH | $2/3$ simple | Aryan, arXiv:1902.05473, J. Number Theory | [FETCHED] |
| A4 | A1 + A3 inputs, plus rank-trace inequality + Sylvester inertia on a finite compression of Weil's Hermitian form (NO hypothesis on zeros) | NO | Simple-and-on-line and distinct proportions, fully unconditional; extends to primitive Dirichlet L-functions; Lean 4 verified | $2/3$ simple+on-line, $5/6$ distinct; $0.6725$/$0.8362$ at the Montgomery-Taylor window | Alpöge-Furman, arXiv:2608.13637 | [FETCHED]+[REPO] |
| A5 | $n$-level prime sums in the diagonal range, $\sum_j\lvert\xi_j\rvert < 2$ | NO (smoothed); RH (sharp) | $n$-level correlations agree with GUE on restricted test classes; diagonal saturation past the boundary; for $\zeta$, $n=2$ "coincides with the result of Montgomery" | correlations only, no new proportion (AF: "higher moments add nothing" at this register) | Rudnick-Sarnak, Duke Math. J. 81 (1996) 269-322 | [FETCHED-P] |
| A6 | Mollified moments of $\zeta$, $\zeta'$ (Levinson-Conrey method; a DIFFERENT input class from $F(\alpha)$: long Dirichlet-polynomial mollifiers, Kloosterman-sum estimates) | NO | Zeros ON the critical line (and simple-on-line variants) | on-line: $1/3$ (Levinson 1974) $\to$ $2/5$ (Conrey 1989) $\to$ $0.4105$ (BCY 2011) $\to$ $>5/12 \approx 0.4173$ (PRZZ); simple+on-line $0.4058$ (BCY), $\approx 0.4075$ (PRZZ) | PRZZ, arXiv:1802.10521, Res. Math. Sci. 7:2 (2020); BCY, arXiv:1002.4127, Acta Arith. 150 (2011) 35-64 | [FETCHED] (PRZZ abs), [SECONDARY] (lineage constants) |
| A7 | Combination method on moment inputs (Farmer's method + refinements) | NO | Distinct zeros | $0.639$ (Farmer 1995) $\to$ $66.036\%$ (Wu) | Wu, Quart. J. Math. 66(2) (2015) 759-771 | [SECONDARY]+[REPO] |
| **B. Conditional on RH, support still $\le 1$** | | | | | | |
| B1 | RH + support-1 mean values (the original) | RH | $F(\alpha) = \alpha + o(1) + (1+o(1))T^{-2\alpha}\log T$ for $0\le\alpha\le 1-\epsilon$ (endpoint $\alpha = 1$ via a sieve bound for prime twins); $N^* \le (\tfrac43+\epsilon)N$; $N_s \ge (\tfrac23 - o(1))N$ | $2/3$ simple | Montgomery 1973, Proc. Sympos. Pure Math. XXIV; statements pinned first-party via Goldston math/0412313 | [FETCHED-P] |
| B2 | RH + optimal window in the bandwidth-one class | RH | Improved multiplicity budget via the Montgomery-Taylor window | $N^*\le 1.3275 N$, $N_s \ge 0.6725 N$ | Montgomery ICM 1974 (with Taylor); constants as credited in CGdL | [SECONDARY] |
| B3 | RH + refined kernel constraints | RH | Simple zeros | $0.6727$ (Cheer-Goldston 1993) | Proc. AMS-era record, credited in CGdL intro | [SECONDARY] |
| B4 | RH + semidefinite programming over the Cohn-Elkies function class (beyond bandlimited windows) | RH | Multiplicity, simple, distinct, small-gap budgets, all from support-1 data | $N^*\le 1.3208N$, $N_s\ge 0.6792N$, $N_d\ge 0.8477N$ (prev. $0.8051$ Farmer-Gonek-Lee); small gaps $N(0.6039,T)\gg N(T)$ | Chirre-Gonçalves-de Laat, arXiv:1810.08843, Adv. Math. 361 (2020) | [FETCHED] |
| B5 | RH + complete solution of the $N(T,\beta)$ extremal problem (reproducing-kernel Hilbert spaces of entire functions of exponential type) | RH | Sharp upper/lower pair-count bounds for ALL $\beta>0$; the window-optimality machinery AF credits for Montgomery-Taylor | extremal machinery (the in-class optimum) | CCLM, arXiv:1406.5462, Crelle 725 (2017) 143-182 | [FETCHED] |
| B6 | RH + mollified discrete moments of $\zeta'(\rho)$ (generalized Vaughan identity; NOT the $F(\alpha)$ class) | RH | Simple zeros, beating every pair-correlation bound at the same hypothesis | $19/27 \approx 0.7037$ simple (CGG98 needed RH+GLH; BHB removed GLH) | Bui-Heath-Brown, arXiv:1302.5018, Bull. LMS 45 (2013); Conrey-Ghosh-Gonek, Proc. LMS 76 (1998) 497-522 | [FETCHED] (BHB), [SECONDARY] (CGG) |
| **C. Conditional on GRH: the first purchased support beyond 1** | | | | | | |
| C1 | GRH for Dirichlet L-functions (primes in APs via long-Dirichlet-polynomial mean values) | GRH | The first lower bound past the wall: $F(\alpha) \ge \tfrac32 - \lvert\alpha\rvert - \epsilon$ uniformly for $1\le\lvert\alpha\rvert\le\tfrac32-2\epsilon$ | $N_s \ge 0.6738N$, $N^*\le 1.3262N$ (GGOS); improved to $N_s\ge 0.6845N$, $N_d\ge 0.8486N$ by SDP | GGOS, Proc. LMS 80 (2000) 31-49; CGdL arXiv:1810.08843 | [FETCHED] (the $F$ bound), [SECONDARY] (consequences) |
| C2 | GRH + $q$-family averaging (all characters) | GRH | $q$-analogue of $F(\alpha)$ for $\lvert\alpha\rvert<2$: support 2 purchasable ON AVERAGE over the family | $\le 86\%$ simple (family aggregate) | Özlük, J. Number Theory 59 (1996) | [SECONDARY] |
| C3 | GRH + asymptotic large sieve (primitive characters) | GRH | $q$-averaged $F(\alpha)$, $\lvert\alpha\rvert<2$, over primitive L-functions; family-aggregate simplicity | $91\%$ of zeros of primitive Dirichlet L-functions simple | CLLR, arXiv:1211.6725 | [FETCHED] |
| **D. Full-support and Hardy-Littlewood ladders (the conditional ceiling)** | | | | | | |
| D1 | RH + $F(\alpha) = 1+o(1)$ on $[1,\lambda]$ (SPC at finite bandwidth) | RH+SPC$[1,\lambda]$ | $N^* \le (1 + \tfrac{1}{3\lambda^2} + o(1))N$, hence $N_s \ge (1 - \tfrac{1}{3\lambda^2} - o(1))N$: the explicit proportion-vs-support exchange rate (display (6.13) of math/0412313; the finite-$\lambda$ reading is immediate from the in-print display, flagged as such) | $1-\tfrac{1}{3\lambda^2}$ simple | Goldston math/0412313, Section 6 | [FETCHED-P] |
| D2 | RH + PCC (full support) | RH+PCC | $100\%$ of zeros simple (Gallagher-Mueller 1978; per GLSS the method "does not depend on RH") | $100\%$ simple | Gallagher-Mueller 1978, as stated in GLSS I abstract | [FETCHED] |
| D3 | PCC alone, as a statement about VERTICAL distribution only (no RH anywhere) | PCC | $100\%$ simple AND on the critical line ("horizontal multiplicity" idea); Remark 4 partial ladder: $N^{\circledast}\le(\mathbf{C}+o(1))TL$ with $1\le\mathbf{C}<2$ gives weaker proportions depending on $\mathbf{C}$ | $100\%$ simple+on-line | GLSS I, arXiv:2503.15449 (v4 2026-03-30) | [FETCHED] |
| D4 | The Alternative-Hypothesis-shaped PCC (the competing full-support pair law), no RH | AH-PCC | ALSO $100\%$ simple and on the critical line: full-support pair data of either competing shape saturates at the same conclusion | $100\%$ simple+on-line | GLSS II, arXiv:2507.06823, J. Number Theory (2026) | [FETCHED] |
| D5 | Narrow-box hypotheses (all zeros in a box of width $b/\log T$, $b\to 0$) | box hyp. | $2/3$ simple, $2/3$ on-line, $1/3$ simple+on-line (2501.14545); $2/3$ simple AND on-line (2603.28104, heights $[T,2T]$) | $2/3$ | BGSTB, arXiv:2501.14545; Goldston-Suriajaya, arXiv:2511.20059 + arXiv:2603.28104 | [FETCHED] |
| D6 | Hardy-Littlewood prime-pair data at integer shifts, graded (HL*($k$) ladders inside the AF mechanism) | HL* | HL*(4) gives $13/18$; full HL* gives proportion $1$ OF SIMPLE ZEROS; in-paper verbatim: "RH itself is out of reach of the mechanism"; all bandwidth-one certificates priced at $\approx 0.682$ | $13/18$; then $100\%$ simple, never RH | AF arXiv:2608.13637, in-paper conditional table | [REPO] |
| **E. The prime-side dictionary (what support $>1$ IS, in prime currency)** | | | | | | |
| E1 | Second moment of primes in short intervals | RH (for the equivalence) | $F(x,T)\sim\tfrac{T}{2\pi}\log T$ for $T\in[X^{B_1}(\log x)^{-3}, X^{B_2}(\log x)^3]$ $\iff$ $\int_1^X(\psi((1{+}\delta)x)-\psi(x)-\delta x)^2dx \sim \tfrac12\delta X^2\log\tfrac1\delta$ for $\delta\in[X^{-B_2},X^{-B_1}]$; in particular SPC $\iff$ $\int_1^X(\psi(x{+}h)-\psi(x)-h)^2dx\sim hX\log\tfrac{X}{h}$, $1\le h\le X^{1-\epsilon}$ | exact equivalence, both directions, uniform ranges | Goldston-Montgomery 1987; Theorem 7 of math/0412313 | [FETCHED-P] |
| E2 | HL prime-pair conjecture with strong error, $\sum_{n\le N}\Lambda(n)\Lambda(n{+}k)=\mathfrak{S}(k)N+O(N^{1/2+\epsilon})$ | HL+error | SPC on $1\le\alpha\le 2-\epsilon$ (Bolanz 1987, 131 pages; simplified via smoothing); the second-moment hypothesis is "considerably weaker... and gives the full range" | support $[1,2-\epsilon]$ from HL | math/0412313 Sections 6, 9 | [FETCHED-P] |
| E3 | Bounds on $F$ in $[1,M]$, fed BACK to primes | RH+$F$ data | $F=o(\log T)$ on $[1,M]$ $\Rightarrow$ $\psi(x)=x+o(x^{1/2}\log^2x)$; $F\ll 1$ near $\alpha=2$ $\Rightarrow$ $p_{n+1}-p_n\ll\sqrt{p_n\log p_n}$; $F\sim1$ near $\alpha=1$ $\Rightarrow$ $\liminf\frac{p_{n+1}-p_n}{\log p_n}=0$, and bounded gaps under log-savings in the error | the zeros$\to$primes direction | Heath-Brown 1982, as Section 8 of math/0412313 | [FETCHED-P] |
| E4 | Sums of the singular series itself (NO hypothesis: theorems about $\mathfrak{S}$) | NO | $R_2(h) = -h\log h + (2-C_0-\log 2\pi)h + O(h^{1/2+\epsilon})$; equivalently $\sum_{d_1\ne d_2\le h}\mathfrak{S}(D) = h^2 - h\log h + (1-C_0-\log2\pi)h + O(h^{1/2+\epsilon})$: the SECOND-ORDER singular-series term, the register F1a is aimed at | second-order constants explicit | Montgomery-Soundararajan, arXiv:math/0409258, Theorem 2 + eq. (17), Comm. Math. Phys. 252 (2004) | [FETCHED-P] |
| E5 | HL with square-root error UNIFORM over shift sets ($E_k(x;D)\ll N^{1/2+\epsilon}$) | HL uniform | Gaussian moments of $\psi(x{+}H)-\psi(x)-H$ with variance carrying $B = 1-C_0-\log2\pi$ (i.e. $\sim H(\log\tfrac{x}{H}-C_0-\log2\pi)$ after the $x$-average); for $k=1$ the hypothesis "is equivalent to the Riemann Hypothesis" | conditional CLT; the $k{=}1$ clause IS RH | same, Theorem 3 + Corollary 1 | [FETCHED-P] |
| E6 | PCC as a variance statement; higher analogues | RH | $F(\alpha)\sim1$ (SPC) $\iff$ the $K{=}2$ case of the MS moment conjecture (Goldston-Montgomery); MS Conjecture 1 $\iff$ Gaussian moments of $\sum_{0<\gamma\le T}\cos(\gamma\log x)$ (Chan); HL $\to$ $n$-level correlations heuristically (Bogomolny-Keating) | the full dictionary at every level | math/0409258 intro, first-party | [FETCHED-P] |
| **F. Consistency certificates (what support-$\le1$ data can NEVER decide)** | | | | | | |
| F1 | Everything currently known about pair AND higher correlations (restricted support) | NO | An explicit point process, and by the ergodic theorem a deterministic set in $\tfrac12\mathbb{Z}$, satisfying the Alternative Hypothesis spacings while matching "all statistics which are currently known about zeros": known correlation data cannot rule AH out (Tao independently) | in-print non-decidability certificate | Lagarias-Rodgers, arXiv:1905.12123, Quart. J. Math. 71 (2020) 257-280 | [FETCHED] |
| F2 | RH + AH (half-integer spacing formulation, multiple zeros allowed) | RH+AH | Density constraints on pairs at $k/2$ spacings; strong AH implies Essential Simplicity; "AH-Pairs is consistent with MT, however it determines a completely different behavior of $F(\alpha)$ when $\lvert\alpha\rvert>1$" | AH lives exactly at the support-1 boundary | BGSTB, arXiv:2508.10857; Baluyot, J. Number Theory (2016); Heath-Brown 1996 (origin, Landau-Siegel) | [FETCHED] |

$N$ throughout means $N(T)$, counts with multiplicity; $C_0 = \gamma$ is Euler's constant.

## 3. Row notes (what was verified, and how)

- **A1/A2 (BGSTB).** Abstract transcribed verbatim from the abs page and cross-checked
  against the search-index copy. Their $F$ is built from full complex zeros
  ($x^{\rho-\rho'}$, $w(u)=4/(4-u^2)$ in their normalization), so the asymptotic itself
  needs NO location input; the location cost re-enters only in the simplicity
  deduction (the thin box). The 67.9 percent their abstract cites as the RH benchmark is
  CGdL's 0.6792 (their intro credits it explicitly: "Recently Chirre, Gonçalves, and de
  Laat [CGdL20] obtained by this method 67.9%"). Deep verification of their mean-value
  inputs is the sibling session's charge, not this note's.
- **A4 (AF).** Abstract re-fetched this session, identical in content to the #202
  deep-read note (which had every quote adversarially re-fetched). The mechanism note:
  what AF add on top of A1-A3 is exactly the removal of the box/zero-density hypotheses
  by inertia bookkeeping: the landscape's cleanest illustration that the LOCATION premium
  at support 1 was a bookkeeping cost, not a data cost.
- **A5 (Rudnick-Sarnak).** First-party (pdftotext of the Duke paper from Rudnick's
  page). Their Theorem 1.1 (smoothed $n$-level, GUE agreement) needs no RH for $m\le3$
  (so for $\zeta$); the sharp Theorem 1.2 assumes RH for $L(s,\pi)$. Remark 1, verbatim:
  the restriction is "exactly the region in which the asymptotic behaviour... is
  dominated by the contributions from all the multidiagonals... Beyond this region, a
  saturation takes effect and the diagonals no longer dominate. For $\zeta(s)$, this
  region is also distinguished by being the range in which the pole at $s=1$ contributes
  only terms of lower order." This is the higher-correlation face of the same wall, and
  the in-print ground for AF's "higher moments add nothing" at the support-1 register.
- **A6 (the critical-line lineage).** PRZZ's abstract (verbatim) claims only the on-line
  record ("slightly over five-twelfths"); the simple-and-on-line $\approx 0.4075$ is
  body-level and carried here at [SECONDARY]. This class consumes a genuinely different
  input (mollified moments, Kloosterman technology) and is the reason the on-line and
  simple ledgers were decoupled before AF.
- **B1 (Montgomery).** All statements taken first-party from Goldston's notes, including
  the two details that matter to F1: the closed endpoint $\alpha=1$ already consumes "a
  sieve bound for prime twins" (notes, after Theorem 1), and the deduction machinery is
  the Fejér pair at $\lambda=1$ giving $\sum m_\rho \le (\tfrac43+\epsilon)\tfrac{T}{2\pi}\log T$.
  Goldston, on the ceiling: "It is possible to make very small improvements in the value
  $\tfrac23$... It would be a major advance to be able to prove that almost all the zeros
  are simple, even on RH."
- **B4/B5 (the window-class optimization).** CGdL's numbers transcribed from their
  intro (ar5iv). CCLM17 is the complete extremal solution in the exponential-type class;
  CGdL then exit the bandlimited class (Cohn-Elkies functions, SDP) and still gain only
  $0.6725 \to 0.6792$ under RH: the in-class headroom above the Montgomery-Taylor window
  is small, consistent with AF's own $\approx 0.682$ pricing of ALL bandwidth-one
  certificates ([REPO], in-paper via Chebyshev-Markov-Stieltjes).
- **B6 (the moment-method premium).** Under the SAME hypothesis (RH), the
  non-pair-correlation method holds the simplicity record: $19/27 \approx 0.7037$
  (BHB13, verbatim abstract). Landscape datum for F2: the pair-correlation input class
  is not the only certificate family even below the wall.
- **C1 (GGOS).** The only in-print theorem funding $F$ past support 1 from an
  unconditional-adjacent hypothesis (GRH): a LOWER bound, linear in $\lvert\alpha\rvert$,
  on $[1, \tfrac32-2\epsilon]$, via primes in arithmetic progressions. Note the shape:
  GRH buys one-sided information only; no asymptotic.
- **C2/C3 (the family evasion).** Averaging over the $q$-family purchases support 2
  (Özlük all characters; CLLR primitive characters via the asymptotic large sieve,
  abstract verbatim: "91% of the zeros of primitive Dirichlet $L$-functions are simple...
  improves on earlier work of Özlük which gives a proportion of at most 86%"). The wall
  is per-L-function; family aggregation is the one in-print mechanism that crosses it,
  and it crosses it by changing the question (aggregate statistics, not $\zeta$'s zeros).
- **D1 (the exchange rate).** The display (6.13) in Goldston's notes is in print with
  full proof (RH + SPC on $[1,\lambda]$ evaluated against the Fejér pair); the
  finite-$\lambda$ corollary $N_s \ge (1-\tfrac{1}{3\lambda^2})N$ is an immediate
  read-off stated here explicitly BECAUSE no source states it as a standalone theorem
  (see Section 7, gap 3). Checked against endpoints: $\lambda=1$ gives $2/3$
  (Montgomery); $\lambda\to\infty$ gives SZC (Theorem 4 of the notes: "SPC implies PCC
  and SZC").
- **D3/D4 (GLSS).** Abstracts verbatim, both. The pair: full-support pair correlation of
  the GUE shape gives 100 percent simple-and-on-line WITHOUT RH; and the AH shape (the
  only named competitor law) gives the SAME conclusion. So at full funding the pair
  register is conclusion-insensitive to which law holds, and neither yields RH. GLSS I
  Remark 4 is the only in-print partial-funding ladder posed without RH.
- **E4/E5 (Montgomery-Soundararajan).** First-party. Their Theorem 2 and eq. (17) are
  unconditional theorems about the singular series; Theorem 3 is where the HL hypothesis
  enters, with the uniformity clause and the flat statement that its $k=1$ case "is
  equivalent to the Riemann Hypothesis (RH)". The second-order register (the
  $-h\log h$ and $(1-C_0-\log2\pi)h$ terms) is exactly where the deliberation pre-stated
  F1a's typing lives, and it is inhabited in print ONLY on the variance side.
- **F1 (Lagarias-Rodgers).** Abstract verbatim: "It is known that the Alternative
  Hypothesis is compatible with what is known about the pair correlation function of
  zeta zeros. We ask whether what is currently known about higher correlation functions
  of the zeros is sufficient to rule out the Alternative Hypothesis and show by
  construction of an explicit counterexample point process that it is not."

## 4. The ladder, assembled: proportion as a function of funded support

Reading the table as one curve (simple zeros unless stated; all $-o(1)$ suppressed):

| Funded input | Simple proportion | Simple+on-line |
|---|---|---|
| support 1, unconditional, pre-inertia | $0.617$ (box hyp., BGSTB) | none |
| support 1, unconditional, inertia | $2/3$; $0.6725$ (MT window) | SAME (AF: the two ledgers fuse) |
| support 1 + RH, window class | $0.6725 \to 0.6792$ (SDP) | trivially on-line |
| support 1 + RH, moment class | $19/27 \approx 0.7037$ | |
| $[1,\tfrac32)$ + GRH (one-sided $F$) | $0.6845$ (SDP-improved GGOS) | |
| $[1,\lambda]$ + RH, $F\sim1$ | $1 - \tfrac{1}{3\lambda^2}$ | |
| HL*(4) (AF mechanism) | $13/18 \approx 0.722$ | |
| full-support PCC, no RH | $100\%$ | $100\%$ (GLSS I) |
| full-support AH-PCC, no RH | $100\%$ | $100\%$ (GLSS II) |
| full HL* (AF mechanism) | $100\%$ | still NOT RH (in-paper) |

Three structural readings, each with an in-print anchor. (1) The curve is CONTINUOUS in
the support parameter (D1's $1-\tfrac{1}{3\lambda^2}$) but the FUNDING is not: nothing
between support 1 (unconditional) and support $\tfrac32$ (GRH) is purchasable from any
proven input; the gap in the input column is the funding wall itself. (2) Every rung
past support 1 tops out at proportion statements; the terminal rung is 100 percent
SIMPLE-and-on-line, and both AF ("RH itself is out of reach of the mechanism", [REPO])
and the GLSS pair (same conclusion from contradictory full-support laws) mark the
information wall in print. (3) The unconditional record equals the OLD conditional
record at the same window ($0.6725$): RH's entire contribution at bandwidth one has
been re-derived from primes; what RH still buys in-class is $0.0067$ (window class) or
$\approx 0.031$ (moment class).

## 5. The provability boundary, in the papers' own words

What the surveyed literature ITSELF blames for the support-1 wall. This feeds the
frame's pre-registered competitor typing (deliberation Section 4: minor-arc /
short-interval-variance species vs lattice-data availability), so the sourcing
discipline matters: every item below is [FETCHED-P] unless marked.

1. **The off-diagonal cancellation requirement (Goldston, first-party).** From
   math/0412313, Section 6: since trivially $F(x,T) \le F(0,T) \sim \tfrac{T}{2\pi}\log^2T$,
   "$F(x,T)$ never gets as large as $x$ for $x \gg T(\log T)^2$, and therefore the
   off-diagonal terms in the sum over primes must almost perfectly cancel the expected
   value term." And the input that would deliver it: "For the off-diagonal terms, one
   needs to assume the Hardy-Littlewood k-tuple conjecture [20] for 2-tuples (or prime
   pairs) with a strong error term", i.e. eq. (6.3), $\sum_{n\le N}\Lambda(n)\Lambda(n+k)
   = \mathfrak{S}(k)N + O(N^{1/2+\epsilon})$. The obstruction as named is a
   CANCELLATION statement about integer-shift prime pairs; the singular series (the
   $\mathbb{Z}$-congruence data) is what the cancellation must resolve to.
2. **Diagonal saturation (Rudnick-Sarnak, first-party).** Remark 1 and the Section 3
   remark: past the support boundary "a saturation takes effect and the diagonals no
   longer dominate", and for $\zeta$ the boundary is "precisely that which renders [the
   polar term] smaller than the main term $T\log T$." Two independent structural
   descriptions (off-diagonal prime sums; the $s=1$ pole) of one wall.
3. **The hypothesis-is-RH degeneracy (Montgomery-Soundararajan, first-party).** The
   uniform HL error hypothesis (20) has as its $k=1$ case a statement "equivalent to the
   Riemann Hypothesis". So the prime-side input class that funds support $>1$ CONTAINS
   RH as its simplest member: the ladder cannot be climbed from below without paying at
   least RH-grade cancellation somewhere in the input column.
4. **The exchange rate makes the wall a variance wall (Goldston-Montgomery, Theorem 7,
   first-party).** Support $[1,A]$ asymptotics for $F$ are EQUIVALENT (on RH) to
   short-interval variance asymptotics $\int_1^X(\psi(x+h)-\psi(x)-h)^2dx \sim hX\log(X/h)$
   down to $h = X^{1/A}$. What is provable there: Selberg's RH-conditional
   UPPER bound $\ll$ (notes, Section 10), never an asymptotic; and the notes record that
   replacing Selberg's bound (10.7) by an asymptotic "is equivalent to the PCC". The
   support wall and the short-interval variance barrier are one object, in print.
5. **Non-decidability at current funding (Lagarias-Rodgers, [FETCHED]).** Everything
   currently known about pair AND higher correlations is satisfied by an AH-spaced point
   set: so no argument consuming only currently-proven correlation data can decide the
   fine spacing structure, independent of ingenuity. GLSS II sharpens the other side:
   even FULL pair funding cannot separate the two laws' conclusions at the
   simplicity/location register.
6. **What is conspicuously NOT blamed.** None of the fetched sources invokes the parity
   problem by name at this joint, and none frames the wall as availability of additive
   lattice data. The in-print blame is uniformly the off-diagonal cancellation /
   variance species (items 1-4): exactly the deliberation's pre-registered COMPETITOR
   typing. F1a's discrimination duty is therefore live, not decorative: the literature's
   own language sides with the competitor, and the typing probe must find something the
   density-alone comparator fails to reproduce (the second-order register, E4) or F1a
   grades against it.

## 6. Discrepancy log (reported, not resolved; SURVEYOR does not adjudicate)

1. **AF's "previous unconditional records are 5/12 and 0.6603" (abstract).** PRZZ's own
   abstract claims $>5/12$ ON-LINE; their simple-and-on-line constant is
   $\approx 0.4075$ (body-level, [SECONDARY]), and BCY's is $0.4058$. So AF's stated
   prior for the simple-and-on-line ledger uses the stronger on-line number. The #202
   note's A5 adjudication ("the simple-and-on-line pairing is the AF record
   bookkeeping") is confirmed at source; the comparison is generous to the prior record
   and AF's margin over the strict prior is larger than stated.
2. **The deliberation's RH benchmark.** #206 carries Montgomery-Taylor $0.6725$ as the
   conditional ancestor constant. In print, the RH-conditional pair-correlation record
   is $0.6792$ (CGdL, credited by BGSTB as "67.9%"), and the overall RH-conditional
   simplicity record is $19/27$ (BHB13, a different input class). No repo claim is
   contradicted (the #202 note's records paragraph is about unconditional bookkeeping),
   but frame documents comparing AF's $0.6725$ to "the conditional record" should name
   which class.
3. **"Higher moments add nothing" (Rudnick-Sarnak range).** Confirmed as the right
   reading of RS at the support-1 register, with one refinement: RS's sharp Theorem 1.2
   assumes RH; the unconditional statement for $\zeta$ is the smoothed Theorem 1.1. AF's
   unconditional usage is therefore of the smoothed species; the repo's wording ("the
   Rudnick-Sarnak diagonal range") stays correct.
4. **BGSTB vs AF on what "unconditional" bought.** BGSTB's own simplicity consequence
   (61.7 percent) carries a thin-box location hypothesis, and their 2025-2026 sequels
   (2501.14545, 2603.28104) still price location via box hypotheses. AF's inertia step
   is the specific removal of that hypothesis. This confirms #202(iii)'s "NEW content"
   clause at source and dates the residual gap AF closed to within its own citation
   list.
5. **Instrument catches (two, banked per the #202/#207 lesson).** (a) The 2306.04799
   HTML summarizer INVENTED a mechanism for the support limitation ("poles of
   $w(u)=4/(4-u^2)$ at $u=\pm2$ limit the effective range"): no such claim exists in the
   sources; discarded, and the obstruction language in this note is taken only from
   first-party text. (b) An arXiv id offered by a search summary for Lagarias-Rodgers
   (1902.05382) resolved to a materials-science paper; content-checked, correct id
   1905.12123 located and fetched. Neither fabrication reached any row.
6. **GLSS II vs the AH's advertised role.** The repo's frame documents treat AH as the
   support-1 conspiracy that pair-correlation methods cannot exclude (true, F1/F2 rows).
   GLSS II adds a twist not yet in any repo document: at FULL support the AH-shaped law
   yields the same 100 percent simple-and-on-line conclusion as PCC. The two-wall
   picture survives, but "AH vs GUE" is not the axis the information wall turns on; the
   wall is indifferent to which law is funded.

## 7. What is NOT in print (the gaps this landscape shows)

1. **No unconditional statement consuming $F(\alpha)$ data for any $\alpha > 1$.** The
   unconditional edge is exactly the closed interval $[0,1]$ (BGSTB). On RH there are
   upper bounds ($\int_B^{B+1}F \le 3$, notes Lemma 1); on GRH a one-sided lower bound
   on $[1,\tfrac32)$ (GGOS); asymptotics only under HL-with-strong-error (Bolanz range
   $[1,2-\epsilon]$) or by fiat (SPC). Nothing unconditional touches $\alpha=1+\delta$
   for any $\delta>0$, for any functional of $F$.
2. **No zero-proportion argument consuming the singular-series SECOND-ORDER term.**
   MS eq. (17) prices $\sum\mathfrak{S}$ to second order unconditionally, and Chan (per
   the notes: "A detailed analysis... with all second order terms obtained") carries
   second-order terms through Montgomery's $F$ heuristic. But every proportion theorem
   in the table consumes correlation inputs at LEADING order only ($F\sim1$, or linear
   lower bounds). A budget line in a simplicity/location argument that is sensitive to
   the $-h\log h$ / $(1-C_0-\log2\pi)h$ register does not exist in the surveyed corpus.
   That register is exactly where F1a's typing was pre-stated to live: it is unoccupied.
3. **No standalone partial-support theorem "unconditional $F$ on $[1,1+\delta]$ would
   buy $X$".** The exchange rate exists implicitly (D1's display; GLSS I Remark 4's
   $\mathbf{C}$-ladder), but no source states the marginal value of the FIRST
   $\delta$ of support past 1, in any currency. The frame's build half (F1's
   "off-diagonal funding need explicit at support $1+\delta$") has no in-print
   competitor to re-derive.
4. **No in-print Beurling-side comparator at this register.** This sweep found no
   pair-correlation or short-interval-variance second-order analysis for Beurling
   generalized primes playing the density-alone role F1a needs. Scope caveat: Beurling
   variance literature (Hilberdink and others) was NOT systematically searched here;
   F1a should run that check before treating the comparator as unclaimed.
5. **No certificate-class ceiling theorem.** AF prices the bandwidth-one class
   ($\approx0.682$) and its own mechanism ("RH out of reach"); GLSS prices full pair
   funding (100 percent simple-and-on-line, silent on RH); Lagarias-Rodgers certify
   non-decidability at CURRENT funding. Nobody has posed, let alone proven, the class
   question F2a is chartered to pose: whether ANY finite-rank certificate family funded
   by prime-correlation data at arbitrary support can certify location-completeness in
   the limit. The nearest in-print objects are the three just listed; none quantifies
   over the class.

## 8. Feed to F1a

Aim the typing probe at the Montgomery-Soundararajan second-order register (E4: the
$-h\log h + (1-C_0-\log2\pi)h$ term of $\sum_{d_1\ne d_2\le h}\mathfrak{S}(D)$), because
every in-print zero-proportion pipeline consumes correlation data at leading order only,
so a measurement there cannot be a re-derivation (Section 7, gap 2). The probe must
discriminate against the literature's OWN typing of the wall, which is uniformly
off-diagonal cancellation / short-interval variance (Section 5, items 1-4 and 6), i.e.
the deliberation's pre-registered competitor, not lattice-data availability. Concretely:
the density-alone comparator (Beurling prime side) must fail to reproduce the
second-order term for a reason the probe can name, and gap 4's scope caveat (Hilberdink
check) must be cleared first.

## 9. What this enables / what remains open

**Enables.** (i) F1's build half can start from row E2's exact funding statement (which
prime-pair sums, at what error, buy which support) with the marginal-$\delta$ question
certified unoccupied (gap 3). (ii) F2a's class definition can be posed against the three
nearest in-print objects (AF's in-mechanism ceiling, GLSS's full-funding saturation,
Lagarias-Rodgers' non-decidability certificate) with confidence nothing closer exists
(gap 5); the GLSS II datum (competing laws, same conclusion) is a free strengthening of
the information-wall intuition and should enter F2a's motivation. (iii) Any future
record-watch has the current constants table in one place, with the conditional
benchmarks straightened (discrepancy 2). (iv) The A-ladder $1-\tfrac{1}{3\lambda^2}$ and
the GLSS $\mathbf{C}$-ladder give the frame two in-print exchange rates to calibrate any
new pricing against.

**Open.** (a) The Aryan and BGSTB mean values remain to be verified at source (sibling
session; they are the AF Lean formalization's carried hypotheses). (b) Whether the
second-order singular-series register can be made a funding line in any proportion
budget is exactly F1a, unanswered in print. (c) The Beurling comparator's in-print
status (gap 4's caveat). (d) Whether the moment-method premium (B6: $19/27$ under RH by
non-correlation inputs) survives unconditionalization by an inertia-style argument is a
question this survey surfaces but no source poses; it sits outside the frame's charge
and is left as a WATCH item.
