# Law-novelty pass: the Fourier-optimization school vs the two P12 closed-form laws

**Date**: 2026-08-21. **Purpose**: the pre-registered LAW-NOVELTY PASS gating publication P12
(PUBLICATIONS.md, Gate 3 and Gate 6: "the one thing that has to happen next"). The nine-paper
Weil-positivity sweep of 2026-08-20
([`weil_positivity_prior_art_sweep.md`](../../../docs/03_research/reading_notes/weil_positivity_prior_art_sweep.md):
Yoshida 1992, Bombieri 2000, Connes-Consani-Moscovici arXiv:2511.22755, Suzuki arXiv:2606.09096,
plus five supporting PDFs) did not surface either law and flagged exactly this complementary
corpus: the Fourier optimization / extremal functions school, plus numerical studies of
truncated-Weil-form spectra. **Corpus swept here**: (i) the Beurling-Selberg extremal school
(Vaaler; Graham-Vaaler; Littmann; Carneiro-Littmann; Carneiro-Littmann-Vaaler Gaussian
subordination); (ii) its zeta/L-function applications (Chandee-Soundararajan;
Carneiro-Chandee-Littmann-Milinovich; Carneiro-Chirre-Milinovich; Chirre-Goncalves;
Carneiro-Milinovich-Soundararajan; Carneiro-Milinovich-Ramos; Quesada-Herrera;
Das-Ismoilov-Ramos); (iii) the Fourier-optimization / LP / sign-uncertainty frame (Cohn-Elkies;
Cohn-Goncalves; Bourgain-Clozel-Kahane; Goncalves-Oliveira e Silva-Steinerberger; Fourier
interpolation and uniqueness: Bondarenko-Radchenko-Seip, Kulikov); (iv) numerical
Weil-positivity / margin studies (the 2026 Groskin-Silva-Andrews cluster around the
Connes-van Suijlekom Galerkin matrix; Connes arXiv:2602.04022 Sections 5-6; classical Li-coefficient
numerics). Method: web search (arXiv, journals, Zenodo) plus full or targeted reads of the
closest items; every query and every document opened is listed in the search log (Section 4)
with its read depth.

**Verdict summary.**

| Law | Verdict | One line |
|---|---|---|
| Law 1 (single-mode margin law) | **NOT SURFACED** | No paper states the closed form $4\sqrt{\pi}\,\sigma\,e^{-\gamma_1^2\sigma^2}$ or any Gaussian-width margin law for the zero-side form; the one in-print closed-form margin-decay law (Connes 2026, Section 6.4) is for a different object, in a different variable, by a different mechanism. |
| Law 2 (graded annihilation frontier) | **PARTIAL** | The node-on-zero locking component now has in-print empirical siblings on the arithmetic-side truncated form (Connes 2026 Section 5; Groskin arXiv:2605.20224, to 307-329 digits); the frontier law proper (the $\sigma$-slope $-(\gamma_{\mathrm{frontier}}-\Omega)^2$ selecting the first unannihilatable zero, the two-plus-zero overshoot, the $\sim$6 decades/zero grading) is NOT SURFACED anywhere. |

---

## 1. Law 1: the single-mode margin law

**The law under test** (e2ao_scaling_ladder.md; LEARNINGS #180). For a single unmodulated Gaussian
window mode of width $\sigma$, the smallest eigenvalue (margin) of the zero-side Weil form
$Q(f) = 2\sum_{\gamma>0}|\hat f(\gamma)|^2$ on the window family obeys

$$\mathrm{margin}(\sigma) = 4\sqrt{\pi}\,\sigma\,e^{-\gamma_1^2\sigma^2}\,\bigl(1 + O(e^{-\sigma^2(\gamma_2^2-\gamma_1^2)})\bigr),\qquad \gamma_1 = 14.134725\ldots$$

Measured: log-slope $-199.79$ vs $-\gamma_1^2 = -199.79$, intercept $1.959$ vs
$\ln(4\sqrt{\pi}) = 1.959$, $R^2 = 1.000000$, over 38 orders of magnitude ($4.8\times10^{-4}$ at
$\sigma = 0.2$ down to $1.5\times10^{-42}$ at $\sigma = 0.7$). Mechanism: the explicit formula
cancels the pole term, so the worst single mode is the UNMODULATED bump ($\omega^* = 0$), and the
exponential rate is the central spectral hole of radius $\gamma_1$. Corollary: prime-side assembly
at accuracy $\varepsilon$ certifies positivity only for $\sigma^2 < \ln(c/\varepsilon)/\gamma_1^2$.

### Verdict: NOT SURFACED

No paper in the swept corpus states this closed form, the equivalent decay statement
$\mathrm{margin} \asymp \sigma e^{-\gamma_1^2\sigma^2}$ for Gaussian windows against the zero-side
form, the $\omega^* = 0$ worst-mode identification, or the certification-cost corollary in the
$\sigma$ variable.

### Nearest neighbors (why each is not the law)

1. **Connes, "The Riemann Hypothesis: Past, Present and a Letter Through Time" (arXiv:2602.04022,
   Feb 2026), Section 6.4.** The one in-print closed-form decay law with an explicit prefactor for
   a localized-Weil-form smallest eigenvalue. For the FULL truncated form $QW_\lambda$ (prime,
   pole, and archimedean terms, support $[\lambda^{-1},\lambda]$), the smallest eigenvalue
   $\epsilon(\lambda)$ goes to $0$ exponentially in $\mu = \lambda^2$, and his Figure 1 shows
   $\epsilon(\sqrt{x})$ tracks the prolate eigenvalue defect $1-\chi_2$ with the asymptotic
   $1-\chi_2 \sim \frac{2^{14}}{3}\sqrt{2\pi^5}\,e^{-4\pi e^{L}}\,L^{9/2}$, $L = 2\log\lambda$.
   This is a margin-decay law of the same GENRE, and any P12 related-work section must cite it.
   It is not Law 1 on three counts: different object (the assembled arithmetic-side form, not the
   zero-side form on a window family), different variable (the window scale $\lambda$, exp-of-exp
   in $L$, not the Gaussian width $\sigma$ at fixed window), and different mechanism (the
   prolate/Sonin phase-space near-intersection, not the zero-free hole of radius $\gamma_1$; no
   $\gamma_1$ appears in his formula). Read depth: theorem-level via the repo's reading note
   [`Connes-2026-RH-Past-Present-Letter.md`](../../../docs/03_research/reading_notes/Connes-2026-RH-Past-Present-Letter.md)
   (Section 6.4 lines), corroborated by Groskin's out-of-sample test against it (below).
2. **The 2026 numerical cluster on the Connes-van Suijlekom Galerkin matrix.**
   - Groskin, "A finite Guinand-Weil dictionary and archimedean tail order for the truncated Weil
     quadratic form" (arXiv:2607.02828, v3 Aug 2026; read in full). Two exact theorems about the
     CvS/CCM truncation: every Galerkin vector transports to a band-limited test function whose
     zero sum equals the quadratic value exactly (Thm 2.5), and the omitted archimedean tail is a
     totally positive increment with budget $B_T = \frac{(2N+1)\rho}{\pi^2 T}(\log\frac{T}{2\pi}+1)(1+o(1))$
     (Thm 3.2, Cor 3.3). Its certification arithmetic (resolving a $10^{-59}$-scale eigenvalue at
     $c = 100$ would need $T \approx 8\times10^{62}$ through the cutoff) is a structural cousin of
     our certification-cost corollary, in the $T$ direction rather than the $\sigma$ direction. No
     eigenvalue decay law, no Gaussian family, no $\gamma_1$-rate statement anywhere in it.
   - Groskin, "High-Precision Approximation of Riemann Zeros via the Truncated Weil Form"
     (arXiv:2605.20224, v4 Aug 2026; pp. 1-8 read plus abstract). Measures
     $\lambda_{\min}^{\mathrm{even}} = 2.865\times10^{-59}$ at $c=13, N=100$, and depth ladders to
     $\sim 10^{-334}$ at $c=100, N=250$. Its only decay-law content is empirical in the $c$
     variable: the fit $|\log_{10}\lambda_{\min}| \approx 13.24\,c^{0.634}$, explicitly falsified
     out-of-sample by 49 orders, and an Aitken extrapolation ($\approx 10^{-536.8}$) tested against
     Connes' Section 6.4 heuristic ($\approx 10^{-530.4}$). No $\sigma$-law, no closed form, no
     first-zero mechanism.
   - Silva, Zenodo 20671635 and 20650146 (June 2026; record descriptions read): corrected deep
     spectra of the truncated form ("descending in a clean geometric ladder"), quadrature noise
     floors; explicitly no rate formula. Andrews, Zenodo 20427500 (June 2026; record description
     read): independent reproduction; reports the Weil eigenvalue ceiling $\epsilon_N$ "decays
     super-exponentially with prime count"; qualitative, $c$-direction, no closed form.
3. **The mechanism's classical home: the highest lowest zero.** Miller's positivity argument
   (placed via Bober-Conrey-Farmer-Fujii-Koutsoliotas-Lemurell-Rubinstein-Yoshida, "The highest
   lowest zero of general L-functions", arXiv:1211.5996, J. Number Theory; abstract read) uses
   explicit-formula positivity to prove every entire L-function of real archimedean type has a
   zero below $t_0 \approx 14.13$; the 2012 paper constructs a degree-4 counterexample at 14.496
   and a conditional bound 22.661. This is the "central spectral hole of radius $\gamma_1$" used
   as an extremal mechanism, and it is why the hole radius is a celebrated constant; there is no
   margin-decay law in it (the hole bounds where zeros must exist, it is not priced in a window
   width).
4. **The school's own minima are reproducing-kernel quotients, not window-margin laws.**
   Carneiro-Chirre-Milinovich, "Hilbert spaces and low-lying zeros of L-functions"
   (arXiv:2109.10844, Adv. Math. 410 (2022); pp. 1-5 read): the extremal answers are kernel
   evaluations, average vanishing order $\le 1/K(0,0)$ at the central point and
   $\le 1/(K(t,t)+|K(t,-t)|)$ at low-lying height (Thm 2), via de Branges/Paley-Wiener
   reproducing kernels; the one-delta and two-delta problems generalize Iwaniec-Luo-Sarnak's
   Fredholm treatment. Structurally the school's closest quantity to a "smallest quadratic-form
   value on a band-limited family", and nothing in it is a decay law in a Gaussian width or an
   exponent set by $\gamma_1$. Likewise Chandee-Soundararajan (arXiv:0908.2008: optimal minorants
   of $\log((4+x^2)/x^2)$, the $(\log 2)/2$ constant) and Carneiro-Chirre-Milinovich
   (arXiv:1710.10362: $L^1$-optimal band-limited majorants for bounding $\zeta$ and $S(t)$
   objects) optimize approximation errors of fixed target functions, never a zero-side margin.
5. **Gaussian subordination is about Gaussians as targets, not as margin probes.**
   Carneiro-Littmann-Vaaler, "Gaussian subordination for the Beurling-Selberg extremal problem"
   (arXiv:1008.4969, Trans. AMS 365 (2013) 3493-3534; abstract read): solves majorant/minorant/
   best-approximation problems FOR the Gaussian $e^{-\pi\lambda x^2}$ by exponential-type
   functions, then subordinates a large class of even functions to it. The Gaussian enters as the
   generating target of the extremal problem; no Weil form, no margin, no first-zero rate.

**Honesty caveat (carried into P12).** The mechanism of Law 1 is elementary: for a single
unmodulated Gaussian the zero-side sum is dominated by the first zero pair, so a rate
$e^{-\gamma_1^2\sigma^2}$ is a one-line consequence that any explicit-formula practitioner could
derive, and the 2026-08-20 sweep already recorded this ("elementary once $\omega^* = 0$ is
known"). The pass claim is only the literal one: the stated closed form (prefactor
$4\sqrt{\pi}\sigma$ from the $L^2$ normalization, the $\omega^* = 0$ worst-mode identification via
pole cancellation, the 38-order verification, and the certification-cost reading) does not appear
in the swept corpus. P12 should present the law as a measured-then-derived calibration of the
instrument, with Connes Section 6.4 cited as the in-print margin-decay law for the sibling object.

---

## 2. Law 2: the graded annihilation frontier

**The law under test** (e2aq_xi_convergence.md; LEARNINGS #181/#183 as corrected). For a
multi-mode family ($J$ modulated Gaussian modes on a frequency grid with ceiling $\Omega$): the
ground state places spectral nodes ON every reachable zero to working precision
($10^{-38}$-$10^{-41}$); with the grid held fixed, the $\sigma$-slope of the log-margin equals
$-(\gamma_{\mathrm{frontier}}-\Omega)^2$ where $\gamma_{\mathrm{frontier}}$ is the first zero the
family cannot annihilate (measured: $-85.2$ vs $-(\gamma_8-34)^2 = -87.0$, 2 percent), and the
frontier sits TWO OR MORE zeros past the naive ceiling (the $\Omega = 34$ family kills
$\gamma_6 = 37.59$ and $\gamma_7 = 40.92$ with its spare dimensions); node precision degrades
geometrically across the frontier ($2\times10^{-35}$ at $\gamma_6$, $5\times10^{-29}$ at
$\gamma_7$, $1\times10^{-23}$ at $\gamma_8$, $2\times10^{-10}$ at $\gamma_9$: about six decades
per zero).

### Verdict: PARTIAL

Split by component, because the components have sharply different in-print status.

**(a) Node-on-zero locking of the ground state: in-print empirical siblings exist (this is the
PARTIAL).** The 2026-08-20 sweep placed locking as "known in conjectural/theorem form, empirically
ours". That placement is now superseded on the empirical side for the SIBLING object, the
arithmetic-side truncated Weil form:

- Connes (arXiv:2602.04022, Feb 2026), Section 5: with primes $\le 13$ only, the Mellin transform
  of the minimizer of the truncated quadratic form matches the first 50 zeta zeros, first-zero
  error $2.6\times10^{-55}$, degrading to $\approx 2\times10^{-3}$ at the 50th; he prices the
  chance probability at $\approx 10^{-1235}$.
- Connes-Consani-Moscovici (arXiv:2511.22755), Section 6: the same datum at $\lambda = \sqrt{13}$,
  $N = 120$: first-zero error $2.44\times10^{-55}$ (covered in the 2026-08-20 sweep library).
- Groskin (arXiv:2605.20224, May 2026, v4 Aug 2026): the first independent public implementation;
  fifteen cutoffs $c = 13..67$ with the first-zero error shrinking $2\times10^{-55} \to
  1.5\times10^{-168}$, and at $c = 100$, $N = 250$, dps 500 the smallest-positive even-sector
  eigenvector recovers $\gamma_1,\ldots,\gamma_{10}$ to 307-329 matching digits: by its own
  accurate description the deepest such Galerkin-truncation recovery in the public CvS/CCM
  literature.
- Connes-van Suijlekom (arXiv:2511.23257, CMP 406 (2025)): the criticality theorem behind all of
  this (the finite-truncation ground state's Fourier-Mellin zeros are REAL for every finite
  cutoff), which is why the open question is convergence, not criticality.

Distinction that keeps our measurement standing but bounds the claim: those are all measurements
of the ARITHMETIC-SIDE form (prime cutoff $c$, trigonometric Galerkin basis), where node-on-zero
is the conjectured convergence to $\Xi$ (CCM Section 7; Suzuki (1.2)). Our locking is measured on
the ZERO-SIDE instrument (the PSD form $2\sum|\hat f(\gamma_k)|^2$ on windowed Gaussian-mode
families), where it is the best-avoidance/complementary-slackness face of the same phenomenon, on
a different matrix, with the frontier structure attached. P12 must not phrase locking as a
first observation of the phenomenon; it should phrase it as the zero-side instrument's locking,
measured with the frontier law that the arithmetic-side literature does not have. See discrepancy
D1.

**(b) Graded degradation across the capacity edge: empirical precursors, no law.** Connes' own
Section 5 table IS a graded profile (55 orders of error growth across 50 zeros at $c = 13$,
roughly a decade per zero on average), reported as data with no rate statement, no frontier
selection rule, and no tie to a frequency ceiling. Groskin's Table 11 gives per-zero
matching-digit counts (307-329 across ten zeros at $c=100$: a nearly flat profile deep inside his
family's capacity) and notes "multi-zero convergence universality" (rates within 3.8 percent);
again no per-zero cost law. The abstract mechanism has a rigorous home in the localization-operator
literature: the eigenvalue plunge of time-frequency localization (Landau-Widom asymptotics;
Bonami-Jaming-Karoui; Kulikov, arXiv:2306.12430, proving $\lambda_n(c) > 1-\delta^c$ for
$n = \lfloor(1-\varepsilon)c\rfloor$, exponential closeness to 1 before the plunge). These prove
geometric transitions for the prolate spectrum, which is CCM's own comparison object; none states
a per-zeta-zero cost or a frontier selection law.

**(c) The frontier law proper: NOT SURFACED.** No paper found states (i) that the margin's
$\sigma$-slope at fixed grid selects the first unannihilatable zero via
$-(\gamma_{\mathrm{frontier}}-\Omega)^2$, (ii) that the annihilation frontier overshoots the naive
frequency ceiling by two or more zeros, or (iii) a per-zero geometric node-precision cost for zeta
zeros. Nearest structural relatives, each checked and each short of the law:

- **Superoscillation energy laws.** Ferreira-Kempf ("Superoscillations: faster than the Nyquist
  rate", IEEE Trans. Signal Processing 54 (2006); placed via the topical review literature): a
  band-limited family CAN place oscillations/nodes beyond its ceiling, at an energy cost
  exponential in the NUMBER of superoscillatory features and polynomial in their speed. This is
  the qualitative twin of the overshoot-plus-geometric-cost structure (our "spare dimensions"
  buying $\gamma_6,\gamma_7$ at $\sim$6 decades per zero), never applied to zeta zeros and with
  no selection law.
- **The capacity accounting: Fourier uniqueness densities.** Kulikov ("Fourier interpolation and
  time-frequency localization", arXiv:2005.12836, JFAA 27 (2021)), as used in
  Bondarenko-Radchenko-Seip Section 2.4: any interpolation/uniqueness pair obeys
  $N_\Lambda(T) + N_{\Lambda^*}(W) \ge 4WT - C\log^{2+\eta}(4WT)$, and the zeta-zero plus
  $\log$-lattice node system saturates it via Riemann-von Mangoldt. This is the in-print counting
  constraint on how many nodes a time-frequency-constrained family can control: the frontier's
  existence in the large, with no finite-family selection rule and no rate.
- **The infinite-capacity endpoint.** Bondarenko-Radchenko-Seip ("Fourier interpolation with zeros
  of zeta and L-functions", arXiv:2005.02996, Constr. Approx. 57 (2023) 405-461; targeted
  full-text extraction): Theorem 1.1 reconstructs an even $f$ in their strip class from
  $\hat f(\frac{\log n}{4\pi})$ and the values at the zeta zeros; Corollary 1.1(i) is the
  uniqueness statement (vanishing on all of both sequences forces $f = 0$), and the basis breaks
  if a single node is removed. This is the abstract, all-zeros face of e2aq's synthesis ("every
  zero is eventually paid for exactly once"); it contains no finite-truncation frontier and no
  precision profile.
- **Node placement as complementary slackness.** In the LP frame the school itself uses
  (Cohn-Elkies class $\mathcal{A}_\Delta$ as axiomatized in Das-Ismoilov-Ramos, arXiv:2502.05106,
  EP1: minimize $\Phi_\nu(g)/g(0)$; and the sphere-packing magic functions vanishing on the
  optimal configuration), optimizers put roots on the active obstruction set. Sign-uncertainty
  extremizers likewise carry forced root structure (Goncalves-Oliveira e Silva-Steinerberger,
  arXiv:1602.03366, JMAA 451 (2017): Bourgain-Clozel-Kahane root constant pinned to
  $0.45 \le c \le 0.594$, extremizers have infinitely many double roots; Cohn-Goncalves'
  $+1$-eigenfunction solution in dimension 12). This is the right general reason ground states
  lock nodes onto the spectrum they must avoid; none of it is quantitative about zeta zeros or
  about a truncated family's frontier.

**Net for Law 2.** The locking component alone would be PARTIAL (measured elsewhere on the sibling
object, at greater depth, before us); the frontier law, the $\sigma$-slope selection rule, the
two-plus-zero overshoot, and the six-decades-per-zero grading are not in the corpus. P12 should
claim the FRONTIER LAW as the new content and present zero-locking as the (independently measured)
zero-side face of a phenomenon now well documented on the arithmetic side.

---

## 3. Discrepancy log (reported, not resolved)

- **D1 (supersedes part of the 2026-08-20 sweep, item 3, and P12 claim (iii) framing).** The
  sweep's "zero-locking ... empirically ours" was written before this pass found Groskin
  arXiv:2605.20224 (submitted May 2026, i.e. before our #181/e2aq measurements of 2026-08-19/20)
  and before weighing Connes 2602.04022 Section 5's fifty-zero error table as an empirical locking
  measurement. Empirical node-on-zero recovery from truncated-Weil-form ground states is in print,
  independently reproduced, and deeper (307-329 digits) than our working precision, on the
  arithmetic-side object. Our zero-side-instrument locking and everything frontier-shaped remains
  unclaimed elsewhere. ACTION for SYNTHESIZER/drafter: reword P12 claim (iii) from "exact
  zero-locking" as a standalone novelty to "exact zero-locking of the zero-side window family
  (cf. the arithmetic-side recoveries of Connes 2026 Section 5, CCM Section 6, Groskin
  2605.20224), with the graded frontier structure that those measurements do not resolve".
- **D2 (sharpens the sweep's item 2).** "No decay law surfaced in the corpus" remains true for the
  Gaussian-window law, but the repo's own reading note on Connes 2602.04022 already carried the
  Section 6.4 exp-of-exp law $1-\chi_2 \sim \frac{2^{14}}{3}\sqrt{2\pi^5}\,e^{-4\pi e^L}L^{9/2}$
  for the arithmetic-side $\epsilon(\lambda)$; the 2026-08-20 sweep's nine-PDF library simply did
  not include that paper. P12's related-work section should cite it explicitly (with the
  object/variable/mechanism distinction of Section 1 above) to preempt "Connes already has a
  margin law".
- **D3 (library mislabel).** `references/10_weil_positivity/Das-Ismoilov-Ramos-2025-Fourier-Optimization-Pair-Correlation.pdf`
  is Das-Ismoilov-Ramos, "Fourier optimization and pair correlation problems", arXiv:2502.05106
  (Feb 2025). The Carneiro-school attribution in the filename is wrong (the paper is by Ramos and
  coauthors, building on Carneiro-Milinovich-Ramos arXiv:2310.01913). Rename or note in the
  references README.
- **D4 (live parallel cluster; WATCH).** There is an active 2026 numerical cluster on exactly the
  truncated-Weil-form spectrum with certification-style instruments: Groskin (arXiv:2605.20224,
  2607.02828, both revised 2026-08-14), Silva (six Zenodo notes, June 2026, incl. 20671635,
  20650146: closed-form archimedean entries, quadrature-sensitivity two-$T$ rule, a parity sign
  law, Herglotz/Loewner structure), Andrews (Zenodo 20427500, independent Rust reproduction).
  Their instruments (archimedean tail budget $B_T$, cutoff-free $LDL^{\mathsf{T}}$ certificates,
  backward-error floors) are the arithmetic-side complements of our e2an-e2av certificate suite,
  and 2607.02828's budget theorem belongs next to our certification-cost corollary in P12's
  related work. Add arXiv:2605.20224 and 2607.02828 (and the Zenodo authors) to the WATCH list
  alongside 2606.09096 and the CCM line.

---

## 4. Search log (auditability)

Queries run (web search, 2026-08-21):

1. `Carneiro Littmann Vaaler "Gaussian subordination" Beurling-Selberg extremal functions`
2. `Carneiro "Fourier optimization" survey Riemann hypothesis explicit formula lecture notes`
3. `"Weil explicit formula" positivity numerical smallest eigenvalue quadratic form test functions`
4. `Fourier interpolation with zeros of the Riemann zeta function Bondarenko Radchenko Seip`
5. `Carneiro Chandee Littmann Milinovich "pair correlation" zeros Hilbert spaces entire functions`
6. `Carneiro Chirre Milinovich "low-lying zeros" Hilbert spaces de Branges L-functions arXiv`
7. `Chandee Soundararajan bounding |zeta(1/2+it)| Riemann hypothesis Beurling-Selberg majorant arXiv`
8. `superoscillation energy cost exponential number of oscillations band-limited Kempf Ferreira`
9. `Li coefficients numerical computation Maslanka Coffey "Riemann hypothesis" Gram matrix smallest eigenvalue positivity`
10. `arXiv 2411.05095 "Fourier optimization and consequences of the generalized Riemann hypothesis" authors`
11. `Bourgain Clozel Kahane "sign uncertainty" principle eigenfunctions Fourier transform first sign change`
12. `Vaaler 1985 "Some extremal functions in Fourier analysis" Beurling Selberg majorant survey`
13. `Kulikov "Fourier interpolation" density theorem "time-frequency localization" arXiv`
14. `Chirre Goncalves arXiv extremal functions zeta "Pair correlation" OR "log-derivative" OR "bandlimited"`
15. `Goncalves "Oliveira e Silva" Steinerberger Hermite polynomials uncertainty sign changes arXiv`
16. `"explicit formula" Gaussian test function "exponentially small" sum over zeros "first zero" zeta 14.13`
17. `test function "annihilates" OR "vanishing at" low zeros zeta explicit formula positivity margin band-limited frontier`

Documents opened, with read depth:

| Document | Depth |
|---|---|
| Groskin, arXiv:2607.02828 v3 (Guinand-Weil dictionary + tail order) | FULL (all 15 pp. incl. bibliography) |
| Groskin, arXiv:2605.20224 v4 (high-precision zeros via truncated Weil form) | pp. 1-8 + abstract + revision notes |
| Connes, arXiv:2602.04022, Sections 5-6.6 | theorem-level via the repo reading note (prior full extraction) |
| Silva, Zenodo 20671635 and 20650146 | record descriptions |
| Andrews, Zenodo 20427500 | record description |
| Carneiro-Chirre-Milinovich, arXiv:2109.10844 (Adv. Math. 410 (2022)) | pp. 1-5 |
| Das-Ismoilov-Ramos, arXiv:2502.05106 (in-library PDF) | pp. 1-4 |
| Bondarenko-Radchenko-Seip, arXiv:2005.02996 (Constr. Approx. 57 (2023)) | targeted full-text extraction (Thm 1.1, Cor 1.1, Sec 2.4) |
| Bober-Conrey-Farmer-Fujii-Koutsoliotas-Lemurell-Rubinstein-Yoshida, arXiv:1211.5996 (J. Number Theory) | abstract |
| Kulikov, arXiv:2306.12430 | abstract |
| Carneiro-Milinovich-Soundararajan, arXiv:1708.04122 (Comment. Math. Helv. 94 (2019)) | abstract |
| Quesada-Herrera, arXiv:2411.05095 (survey of the school's GRH consequences) | abstract + author metadata |
| Carneiro-Littmann-Vaaler, arXiv:1008.4969 (Trans. AMS 365 (2013)) | abstract + secondary descriptions |
| Chandee-Soundararajan, arXiv:0908.2008 (Bull. LMS 43 (2011)) | abstract + result statement |
| Carneiro-Chandee-Littmann-Milinovich, arXiv:1406.5462 (J. reine angew. Math. 725 (2017)) | abstract + secondary descriptions |
| Carneiro-Chirre-Milinovich, arXiv:1710.10362 (Publ. Mat. 63 (2019)) | abstract |
| Goncalves-Oliveira e Silva-Steinerberger, arXiv:1602.03366 (JMAA 451 (2017)) | abstract + result statements |
| Kulikov, arXiv:2005.12836 (JFAA 27 (2021)) | via BRS Sec. 2.4 + search-level statement of the density theorem |
| Vaaler, "Some extremal functions in Fourier analysis", Bull. AMS 12 (1985) 183-216 | metadata + secondary descriptions (school foundation; content classical) |
| Ferreira-Kempf superoscillation energy law (IEEE TSP 54 (2006)) | via the topical-review literature (energy exponential in the number of superoscillations) |
| Maslanka, "Li's criterion ... numerical approach" (Opuscula Math. 24 (2004)); Coffey's Li-coefficient verifications | metadata + secondary descriptions |
| Chirre-Goncalves, arXiv:2103.06237 (Math. Z. 2021); Chirre-Goncalves-de Laat, arXiv:1810.08843 (SDP pair-correlation) | metadata |
| Goncalves-Oliveira e Silva-Ramos, "New sign uncertainty principles" (Discrete Analysis 2023:9, arXiv:2003.10771); Cohn-Goncalves 12-dimensional $+1$-eigenfunction result | metadata + search-level statements |
| Graham-Vaaler (Trans. AMS 1981); Littmann's extremal-function papers; Carneiro-Littmann "Extremal functions with vanishing condition" (arXiv:1311.1157) | NOT opened this pass; placed via Vaaler's survey and search listings only |
| Bourgain-Clozel-Kahane (Ann. Inst. Fourier 60 (2010)) | NOT opened; placed via GOSS and the sign-uncertainty literature |
| Cohn-Elkies (Ann. of Math. 157 (2003)) | NOT opened this pass; class and mechanism placed via Das-Ismoilov-Ramos Sec. 1.3 |

Already covered by the 2026-08-20 sweep and not re-read here: Yoshida 1992, Bombieri 2000, CCM
arXiv:2511.22755, Suzuki arXiv:2606.09096 and 2022 screw-line, Connes-Consani arXiv:2006.13771,
Gonek 2007, GHK 2005, Broucke-Debruyne-Vindas 2020, the 2024 Hilbert-Schmidt/Weil-distribution
paper (all in `references/10_weil_positivity/`). Connes-van Suijlekom arXiv:2511.23257 remains
abstract-level in the repo (flagged in the CCM reading notes); its Theorem 6.1 role here is taken
from Connes 2602.04022 and Groskin's Section 2, both of which state it.

Scope caveats. Zenodo notes were read at record-description level only; Silva's six notes could in
principle contain an unadvertised rate law, though the two deep-spectra descriptions explicitly
disclaim one. Yoshida 1992 remains not freely available (held via Suzuki's and Bombieri's
accounts, per the prior sweep). Classical school papers marked "NOT opened" above are cited only
for corpus coverage, not for content claims beyond their standard descriptions.

---

## 5. What this enables / what remains open

**Enables (for the P12 drafter and ADVERSARY):**
- The gate is PASSED in the operative sense: neither closed form is in print. Law 1 can be claimed
  as stated (with the elementarity caveat and the Connes Section 6.4 citation). Law 2's FRONTIER
  content (selection rule, overshoot, grading) can be claimed as new; its LOCKING content must be
  reframed per D1 before drafting.
- A ready-made related-work paragraph: Yoshida-Bombieri-CCM-Suzuki (the program), Connes Section
  6.4 (the arithmetic-side margin law), Groskin-Silva-Andrews (the arithmetic-side numerics and
  certification instruments), Miller/Bober et al. (the $\gamma_1$ hole as extremal mechanism),
  BRS-Kulikov (the capacity accounting), Ferreira-Kempf (the overshoot cost mechanism), and the
  Carneiro school (the extremal-function frame in which none of this is a margin law).
- Two citation-hygiene actions: fix the D3 filename; add the D4 items to the WATCH list.

**Remains open (not blocking, worth one line each in P12 or a follow-up):**
- Whether Silva's remaining four Zenodo notes (20710075 parity sign law, 20682834 Perron
  structure, 20694588 Herglotz criterion, 20737111 Loewner framework) contain eigenvector node
  statements beyond their descriptions: a 30-minute read would close it.
- Whether the frontier overshoot ("two or more zeros past the ceiling") admits a clean derivation
  from the superoscillation energy law plus the local zero density, which would upgrade Law 2 from
  measured law to small proposition, matching Gate 2's "upgradeable" note.
- A direct test of the analogy in (b): whether the per-zero six-decade cost maps quantitatively
  onto the prolate plunge width (Landau-Widom $\log$-width) under CCM's dictionary; if yes, the
  frontier law connects our zero-side instrument to the Connes Section 6.4 mechanism, which would
  be a finding, not just related work.
