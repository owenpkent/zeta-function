# E1AD: sum rules on the prime log-lattice. Does the sequence level see Q-linear independence?

**Date**: 2026-08-20. **Role**: BUILDER, executing the sequence-level half of PHASE_STATE next-step 3 (the Christoffel-corpus sweep, SPLIT by LEARNINGS #172 / adversary case 3: the pointwise half is dead in principle, the surviving register is Killip-Simon type sum rules). **Status**: built and measured in one session; 21/21 self-tests full and quick; no adversary round yet; no second party has read this rung.

**Artifacts**: [`e1ad_sum_rules.py`](e1ad_sum_rules.py) (21/21 full, 296.5 s; 21/21 quick, 7.4 s, saves nothing), `e1ad_sum_rules.npz` (full mode only; profiles, rate/kill/horizon/audit tables, the recorded pre-registration resolution).

**Verdict in one line**: `sequence_level_sees_arithmetic = NO BELOW THE COLLISION HORIZON`. The pre-registered [P1] is refuted at the letter (the four-class rate spread is 1.53-1.76x on the diagonal rate and 2.14-4.00x on the mid-profile rate, far outside seed noise), [P2] fires at the letter and is then KILLED by its own pre-registered sanity check: the lattice-destroyed twin GPERM (exact local gap multiset, no arithmetic) reproduces 95.6-99.9% of the spread and stands 0.97-1.00x of TRUE's own distance from the Beurling fake, so the gap is **spacing statistics, not arithmetic**. The Q-linear-independence axis itself is NULL below the horizon: snapping the true configuration onto $(1/D)\mathbb{Z}$ at $D = 10^6$ moves the per-atom diagonal rate by $\le 1.1\cdot 10^{-6}$ and the whole profile response sits inside the matched-amplitude jitter band. What survives is a measured **horizon law**: the sequence-level functional sees the lattice exactly when $\mathbb{Q}$-dependence collapses the atom count (termination at $n = M_d - 1$, exact on all five collision rungs), and is blind at every rung without collisions. #172's pointwise obstruction extends to the sequence level below the horizon.

## The object

For a finite atomic probability measure on the unit circle (atoms at angles $t_j/L \bmod 1$, $t_j$ the configuration, unit weights), the truncated Szego sum

$$S_n \;=\; -\sum_{j\le n}\log\bigl(1-|\alpha_j|^2\bigr) \;=\; -\log\|\Phi_{n+1}\|_{L^2(\mu)}^2 \;=\; -\log\,\min\{\|P\|^2_{L^2(\mu)} : P \text{ monic, } \deg P = n+1\}$$

is exactly minus the log of the extremal monic-polynomial norm: the OPUC twin of e1v's reciprocal Christoffel function (point-normalized there, leading-coefficient-normalized here). For purely atomic $\mu$ with $M$ atoms the sum diverges at $n = M-1$ ($|\alpha_{M-1}| = 1$); the finite-$n$ **rate** of that divergence, along the diagonal $n \to M-2$ with the measure growing, is the sequence-level observable, mirroring #171's Christoffel growth. Calibration point: $M$ equally spaced atoms have $S_n = 0$ for all $n < M-1$ (verified to machine zero, S1a), so the profile is a pure microstructure meter. The Killip-Simon coefficient side $\sum_{j \le n}|\alpha_j|^2$ is computed alongside and stored.

## The classes (mandatory band equalization) and the pre-registration

| class | content | equalization |
|---|---|---|
| (i) TRUE | $\{k\log p \le \log N\}$, the von Mangoldt support; generators $\mathbb{Q}$-linearly independent | reference |
| (ii) SNAP | TRUE snapped onto $(1/D)\mathbb{Z}$, $D = 10^6$ (rationally dependent; pointwise-indistinguishable by #172) | exact count/support |
| (iii) RAND | iid resample from TRUE's empirical CDF | exact count/support, matched profile |
| (iv) BEUR | the shared Beurling control's $\{k \log b\}$ (Euler product, no additive lattice), by import | count within 2.6%, matched density |
| STRAT | stratified resample (matched coarse regularity, no arithmetic) | typing surrogate |
| GPERM | local gap shuffle of TRUE's wrapped angles (exact gap multiset in blocks of 16) | typing surrogate |
| JIT | TRUE + uniform noise at the snap amplitude $1/(2D)$ | the #172 V5 control |

Sizes $N = 300, 1000, 3000$ ($M = 78, 192, 465$ atoms), wrap $L = 1$ primary with a golden-mean gauge face. Certificates: surrogate counts match TRUE exactly, angular-histogram $L^1$ distance to TRUE within $1.07\times$ the sampling-fluctuation scale $\sqrt{\text{bins}/M}$, min wrapped gap $> 3\cdot 10^{-6}$ (S3a-S3c).

Pre-registered readings, from the task specification and frozen in the module's `PREREG` dict: **[P1]** all four classes agree within the #172 family-blind spread ($\le 1.35\times$ on both the per-atom diagonal rate $r_{\rm diag} = S_{M-2}/M$ and the mid-profile rate $r_{\rm mid} = S_{\lfloor (M-1)/2\rfloor}/M$) at every size; **[P2]** a stable rate gap outside seed bands; **SANITY KILL** armed: any (i)-vs-(iv) separation must fail on density-matched lattice-destroyed data or the functional reads density/spacing only; **Q-AXIS** registered expectation: null below the horizon. **Prototype disclosure** (recorded in the module): an $N = 1000$ sizing prototype preceded the freeze and exposed the one-size ordering TRUE < STRAT < BEUR < RAND and one snap-vs-jitter pair; those are calibration facts, not predictions. Check thresholds are pinned from the calibration run and labeled pinned.

## Methods

- **Two independent routes**: the Szego recursion on atom values ($\overline{\alpha_n} = \langle z\Phi_n, 1\rangle/\|\Phi_n\|^2$, values carried on the atoms, no moment matrix) and an own complex-Hermitian Cholesky of the Toeplitz moment matrix ($S_n = -2\log L_{n+1,n+1}$). Agreement $6.5\cdot 10^{-100}$ worst case over TRUE and RAND at $n \le 40$ (S2a). Analytic controls: equal spacing gives $S \equiv 0$ with termination exactly at $n = M-1$; the two-atom closed form $S_0 = -\log(1-|w_1z_1+w_2z_2|^2)$ is exact (S1).
- **Termination detection is a relative cliff** ($1-|\alpha_n|^2$ dropping $10^{10}$ below the running median), not an absolute threshold: the numeric floor sits at $10^{-(\mathrm{dps} - S/\ln 10)}$ and an absolute test silently misses once conditioning eats the margin (measured in calibration at $D = 2000$).
- **Conditioning rule (declared, then measured)**: naive loss model $= S_n/\ln 10$ digits (determinant-ratio range); measured loss coefficient 0.40-0.50 at $M=78$, 0.88-1.63 at $M=192$, 1.51-1.83 at $M=465$ (it grows with $M$; step accumulation). Escalation enforces $\mathrm{dps} \ge 2.3\,S_{\rm final}/\ln 10 + 30$; verified by the internal orthogonality certificate (every run retains $\ge 63$ digits) and by full dps+40 re-runs of the whole pipeline, positions included (worst relative drift $3.3\cdot 10^{-51}$: every reported value carries far more than the 10 required digits) (S8).
- **Exactness hygiene**: TRUE positions are recomputed at working precision at every dps (the audit re-derives the pipeline from $k\log p$); SNAP is exact rationals $m/D$; stochastic classes are exact float64 rationals (their own lattice scale $2^{-52}$ is part of the honest scope; see limits).
- **No L-function zero list anywhere** (source-scanned with a teeth-verified scanner); the Beurling control enters by import from `experiments/_shared/beurling.py`.

## Results

### R1. The rate table ([P1] refuted at the letter)

Medians over seeds; RAND seed band in brackets.

| $N$ | $M$ | | TRUE | SNAP | GPERM | STRAT | BEUR | RAND | four-class spread |
|---|---|---|---|---|---|---|---|---|---|
| 300 | 78 | $r_{\rm diag}$ | 0.3284 | 0.3284 | 0.3505 | 0.3638 | 0.5780 | 0.5609 [band 0.758] | **1.760x** |
| | | $r_{\rm mid}$ | 0.0098 | 0.0098 | 0.0098 | 0.0157 | 0.0243 | 0.0365 | **3.739x** |
| 1000 | 192 | $r_{\rm diag}$ | 0.2941 | 0.2941 | 0.2649 | 0.2927 | 0.4649 | 0.3634 [0.316] | **1.581x** |
| | | $r_{\rm mid}$ | 0.0039 | 0.0039 | 0.0042 | 0.0049 | 0.0154 | 0.0121 | **3.997x** |
| 3000 | 465 | $r_{\rm diag}$ | 0.3269 | 0.3269 | 0.3412 | 0.3318 | 0.3204 | 0.4912 [0.180] | **1.533x** |
| | | $r_{\rm mid}$ | 0.0025 | 0.0025 | 0.0026 | 0.0027 | 0.0054 | 0.0054 | **2.144x** |

Significance is read on the self-averaging observable $r_{\rm mid}$ (the diagonal rate of an iid configuration is heavy-tailed: one tight pair adds $O(-\log d)$ nats; seed bands above): every one of the 8 RAND seed-size pairs exceeds TRUE's $r_{\rm mid}$ by at least **1.91x** (S4a). So [P1]'s 1.35x band is decisively exceeded: the truncated Szego rate is NOT family-blind at matched (count, support, density).

### R2. The kill fires: the spread is spacing statistics ([P2] typed away)

On $r_{\rm mid}$: $|{\rm TRUE}-{\rm BEUR}| = 0.0146 / 0.0116 / 0.0029$ at the three sizes, all significant; the lattice-free GPERM twin's distance $|{\rm GPERM}-{\rm BEUR}| = 0.0145 / 0.0112 / 0.0029$: **lattice-free fractions 1.00 / 0.97 / 0.99**. GPERM sits 99.9% / 95.6% / 98.9% of the way from RAND back to TRUE. A surrogate that keeps only the local gap multiset (in blocks of 16 wrapped gaps) and destroys every arithmetic correlation reproduces essentially the entire class structure. The pre-registered kill condition (lattice-destroyed twin separates from BEUR at $\ge 70\%$ of TRUE's distance) fires at every size: **the functional reads local spacing statistics, and no arithmetic claim survives** (S4b). The gauge face (wrap $L$ = golden mean) preserves the ordering: TRUE 0.2811, GPERM 0.3059, BEUR 0.3872, RAND 0.4719 (S7a).

What the meter actually measures, in plain terms: the wrapped prime log-lattice is **more rigid than Poisson** at matched density (smooth local density means near-regular local spacing; iid resampling is Poisson at all scales), and the Beurling fake interpolates: its $\pm 0.25$ generator perturbation makes it Poisson below scale 0.25 and number-rigid above, which is visibly why its diagonal rate converges to TRUE's at $N = 3000$ (0.3204 vs 0.3269) while its mid rate stays at RAND's level (0.0054): the two observables read different scale mixtures. All of this is PNT-level (density and gap-distribution) data, Level 2-3 in the four-level framing, not Level 4.

### R3. The Q-axis is null below the horizon (the #172 control at sequence level)

| $N$ | $\max_n|S^{\rm SNAP}_n - S^{\rm TRUE}_n|$ | jitter band (matched amplitude) | per-atom diag displacement |
|---|---|---|---|
| 300 | 3.82e-2 | [5.96e-3, 1.52e-2] | 1.08e-6 |
| 1000 | 1.99e-2 | [5.68e-3, 2.52e-2] | 4.44e-8 |
| 3000 | 8.30e-2 | [2.13e-2, 2.70e-2] | 2.59e-7 |

The snap's whole-profile response sits within the pinned 4x of the jitter band top at every size (ratios 2.5 / 0.8 / 3.1), and the rate displacement is $10^{-6}$-scale: snapping onto a rational lattice at $D = 10^6$ is, to this functional, a **generic** perturbation of amplitude $1/(2D)$, indistinguishable in kind from noise (S5). Rationality is invisible. This is #172's V5 result transported to the sequence level, below the horizon.

### R4. The horizon law (the one place the sequence level DOES see the lattice)

D-ladder at $N = 1000$ ($M = 192$), $L = 1$: snapping onto $(1/D)\mathbb{Z}$ wraps onto $D$ angular sites; exact angular collisions merge atoms ($M_d$ distinct sites).

| $D$ | $M_d$ | collisions | $n_{\rm term}$ (theory $M_d-1$) | detection $n^*$ |
|---|---|---|---|---|
| 40 | 40 | 152 | **39** | 39 |
| 100 | 94 | 98 | **93** | 90 |
| 400 | 163 | 29 | **162** | 116 |
| 2000 | 188 | 4 | **187** | 153 |
| $10^4$ | 191 | 1 | **190** | 159 |
| $10^5$ | 192 | 0 | 191 (= generic $M-1$) | none |
| $10^6$ | 192 | 0 | 191 (= generic $M-1$) | none |

The termination law is **exact on every collision rung**: the Verblunsky recursion hits $|\alpha| = 1$ at $n = M_d - 1$, i.e. the functional sees $\mathbb{Q}$-dependence precisely when it collapses the measure's rank, and detection ($n^*$: first 0.5-nat departure from TRUE's profile) fires at or before it (S6a). With zero collisions the ladder is blind (S6b), and $M_d(D)$ is monotone (S6c). Since collisions among $M$ atoms on $\sim DL$ sites appear at the birthday scale $M \gtrsim \sqrt{2DL}$, the measured law prices the register: **certifying non-membership in the scale-$D$ lattice costs $\sim \sqrt{2DL}$ atoms and a comparable sequence depth; genuine $\mathbb{Q}$-linear independence is the $D \to \infty$ limit and costs infinite data.** This CONFIRMS the adversary's #172 correction (the limit is arithmetic-sensitive: the mechanism exists and is exactly rank collapse) while extending the obstruction quantitatively below the horizon.

## Discipline outcomes

- **Beurling (counting side)**: enters by import, passes every construction step identically, and the one functional that separated it from zeta was typed by the kill as a spacing-statistics reading (its gap distribution genuinely differs at scales below its $\varepsilon = 0.25$ scrambling). Nothing here consumes the additive lattice; nothing here pretends to. The conservation law is respected, not dodged.
- **D-H (form side)**: out of scope by construction (this is a counting-side object built from prime data; no functional equation and no L-function zeros are consumed; source scan with verified teeth, S0b).
- **K1**: does not arise; no truth value about zeta's zeros is asserted or consumed.

## Honest limits

1. **Finite window, three sizes** ($M = 78/192/465$), one weight scheme (unit), wrap $L = 1$ primary plus one gauge point. Class orderings are measured levels, not laws; the BEUR diagonal convergence at $N = 3000$ is a one-size observation with a proposed (unproven) scale-mixture mechanism.
2. **All finite data is rational.** The stochastic classes are float64 configurations, i.e. themselves lattices at scale $2^{-52}$; TRUE at working precision is a lattice at scale $10^{-\rm dps}$. The experiment therefore grades lattice SCALE, and the horizon law is exactly the formalization of that: the (i)-vs-(ii) distinction at any finite budget is a distinction between horizons $\sqrt{2D}$ and $\sqrt{2\cdot 10^{\rm dps}}$, not between "rational" and "irrational" as completed totalities.
3. **The horizon mechanism is gauge-rational.** Exact collisions require the snap lattice to be commensurate with the wrap ($DL$ integer here). At irrational $L$ the snapped orbit is dense and never collides exactly; the corresponding mechanism would be three-gap/near-collision structure, and it was NOT measured. The gauge face only checked ordering robustness.
4. **The scope of "sequence-level" here is Szego-type rate functionals** of the Verblunsky/moment data. The claim "blind below the collision horizon" is measured for $S_n$ profiles and rates; a super-resolution register (recovering atom positions from $n$ moments needs $n \sim 1/\delta$ at separation $\delta$) is priced by the same information-theoretic wall but was not built.
5. **The conditioning coefficient grows with $M$** (0.4 to 1.8 over the grid); the 2.3x escalation rule covers the measured window only and would need re-measurement beyond $M \sim 500$.
6. **Prototype disclosure**: the $N=1000$ ordering and one snap/jitter pair were seen before the pre-registration froze (recorded in the module). The size scaling, seed bands, kill resolution, horizon table, and gauge face were not.
7. **No adversary round has run on this rung**, and no second party has read it.

## Handed forward

1. **The horizon question (the sharpest residue)**: is the birthday scale $M \sim \sqrt{2DL}$ optimal among ALL functionals of the first $n$ moments, or can a super-resolution-type functional detect the scale-$D$ lattice at $M \ll \sqrt{D}$? Prony/ESPRIT lower bounds suggest the collision horizon is beatable down to $n \sim D L / \pi$-ish but no further; if that holds, the sequence-level door closes in principle for this gauge: certifying $\mathbb{Q}$-linear independence costs unbounded data in every register, which would make #172's obstruction a two-level theorem (pointwise: continuity vs density; sequence: information vs scale).
2. **The rigidity meter**: $r_{\rm mid}({\rm TRUE})$ is a clean number-rigidity observable of the wrapped prime log-lattice, and its excess over the equal-spacing zero is exactly wrapped-discrepancy data that the explicit formula ties to zeros at PNT precision. Relating the measured 0.0025-0.0098 to an explicit-formula prediction would type the residual arithmetic content of this register exactly (expected: Level 2-3, zero-density not zero-location).
3. **The BEUR scale-mixture mechanism** (R2): vary $\varepsilon$ and watch the diagonal-vs-mid crossover; a cheap follow-up that would confirm or kill the proposed mechanism.
4. The Killip-Simon $\ell^2$ partials are computed and stored in the npz but unexploited.

## Verification targets (for VERIFIER)

1. **The extremal identity** $S_n = -\log\|\Phi_{n+1}\|^2 = -\log\min\{\|P\|^2 : P \text{ monic, } \deg = n+1\}$ and $\|\Phi_{n+1}\|^2 = \prod_{j\le n}(1-|\alpha_j|^2)$: finite linear algebra over an atomic measure.
2. **The rank/termination law**: for an $M$-atom circle measure, $\alpha_n$ is defined for $n < M$ with $|\alpha_n| < 1$ for $n < M-1$ and $|\alpha_{M-1}| = 1$; hence for a snapped configuration with $M_d$ distinct sites, termination at exactly $n = M_d - 1$. This is the theorem form of the horizon mechanism (Gram determinant positivity vs atom count).
3. **Equal-spacing nullity**: atoms at the $M$-th roots of unity with equal weights have $\alpha_n = 0$ for $n < M - 1$ ($\Phi_n = z^n$).
4. **The sequence-level continuity extension of #172**: each $S_n$ is continuous (real-analytic off the collision locus) in the atom positions, so for every fixed $n$ the #172 argument applies verbatim: no fixed-index functional detects $\mathbb{Q}$-linear independence. (The horizon law is the measured quantitative complement.)

## Adversarial test cases (for ADVERSARY)

1. **Attack the kill surrogate**: GPERM preserves the wrapped gap multiset blockwise; check it does not covertly preserve arithmetic (e.g. apply GPERM to a coarse-$D$ snapped configuration: zero gaps survive the shuffle, so collision-level structure is retained; quantify what GPERM destroys vs retains as a function of $D$).
2. **Attack the pinned band factor** (S5a, 4.0x, pinned post hoc): widen the jitter ensemble (10+ seeds) and test whether SNAP's response is an outlier of the jitter distribution at any size rather than within a 4x envelope.
3. **Attack the horizon's completeness**: run a super-resolution functional (Prony / matrix-pencil on the same $n$ moments) against the $D$-ladder and measure ITS detection horizon; the claim to break is that no moment functional beats the information-theoretic scale.
4. **Attack the BEUR reading**: vary the Beurling $\varepsilon$ (0.05, 0.5) and the seed; the R2 mechanism predicts the diagonal convergence point moves with $\varepsilon$; a failure of that prediction reopens the typing of the BEUR-TRUE separation.
5. **Attack the gauge scope**: run the D-ladder at irrational $L$ (golden); the prediction from limit 3 is blindness at ALL $D$ (no exact collisions); a detection there would be a new mechanism outside the collision law.
6. **Independent re-verification** of determinism (S9), the npz byte-stability across runs, and the teeth of the source scan, on a second machine (the e1v case-7 pattern; not run here).

## Addendum 2026-08-25 (LEARNINGS #205): the adversary round ran, case 3 became e1ae, and three corrections land

The posed cases were executed ([`_e1ad_adversary.md`](_e1ad_adversary.md), probe
[`_e1ad_adversary.py`](_e1ad_adversary.py); cases 1, 2, 4, 5, 6 plus e1v case 7;
case 3 executed separately as the build [`e1ae_prony_horizon`](e1ae_prony_horizon.md)).
Verdicts: cases 1, 2 MISSED (with S5a's pinned 4x band exposed as a 3-seed
small-sample artifact: SNAP sits at the 75th percentile of a 12-seed jitter
ensemble, unremarkable); case 4 LANDED; case 5 LANDED; case 6 and e1v case 7
CLEAN (this-host replication; cross-machine remains open). Corrections applied
to this dossier's record:

1. **Honest limit 3 is corrected.** "At irrational L the snapped orbit never
   collides exactly" is FALSE: there are TWO collision channels, and the
   t-space rounding channel (m = nint(D k log p) coinciding) is
   wrap-independent: collision rungs exist at L = golden (11 at D = 40, 2 at
   D = 100), and the rank law n_term = M_d - 1 held EXACTLY there. The
   horizon law is therefore GAUGE-INDEPENDENT through the t-channel, a
   strictly stronger statement than the original claim.
2. **R2's GPERM clause gains a scale scope.** GPERM retains the collision
   channel exactly (zero gaps survive the shuffle; termination invariant at
   every coarse D): "destroys every arithmetic correlation" holds at scales
   ABOVE the collision channel; the R2 kill itself stands (the main grid is
   collision-free).
3. **R2's BEUR scale-mixture mechanism is REFUTED** (handed-forward item 3
   executed with answer "kill"): the distance to TRUE is not monotone in the
   Beurling epsilon (d_mid reverses at eps = 0.5 at both sizes); the
   BEUR-TRUE separation keeps its typing via GPERM, but the proposed
   mechanism paragraph is downgraded to a refuted candidate.

**The horizon law is re-scoped by e1ae** (this dossier's handed-forward item 1
and case 3): the birthday-scale pricing is REGISTER-RELATIVE: the Prony
register detects the scale-D lattice at M = 78 atoms and 14 digits where this
rung's register needs sqrt(2D) = 1414 atoms (D = 1e6, zero collisions). The
termination law, the measured tables, and the D-to-infinity obstruction stand;
the totalized atom pricing does not. See e1ae for the falsifier-4 disposition.

## Citation appendix (salvaged from PR #7, 2026-08-26; LEARNINGS #210)

An in-print "why" for the closed register, extracted from the PR #7 branch's
Christoffel corpus sweep (`christoffel_corpus_sweep_2026-07-30.md`, branch
`overnight-wave-172-173`, Section 3; extract carried here because that sweep is
not tracked on main): every boundedness theorem in the Widom-factor /
Szego-Widom strand is conditioned on the support being THICK (positive Lebesgue
measure, locally quantified: homogeneous, Parreau-Widom, regular with positive
a.c. density), while the chain's spectrum at finite $\lambda$ and in the limit
is discrete and Lebesgue-null, so the Totik-Widom apparatus is structurally
inapplicable, not merely silent. The corpus knows the failure mode is real:
Widom factors are UNBOUNDED for the Julia set of $(z-\lambda)^2$ with
$\lambda > 2$, can grow subexponentially of any prescribed order on thin
Cantor-type sets (Goncharov-Hatinoglu), and the best general bound for a
uniformly perfect set is only $W_n(e) = O(n^c)$ (Andrievskii).

The sharpest single citation: Christiansen-Simon-Zinchenko, "Widom Factors and
Szego-Widom Asymptotics, a Review" (arXiv:2112.06450), whose Open Problem 2.2
asks whether ANY Lebesgue-null set has bounded Widom factors. The prefactor
uniformity this register would have needed is an open problem of that corpus
itself, on the side of the thickness dichotomy where it has no positive results
at all.

Criticality thread (one-line pointer, filed here because
`experiments/criticality/` carries no notes file): Romik, orthogonal-polynomial
expansions of $\Xi$, arXiv:1902.06330 (86pp; zero prior repo mentions), a
salvaged pointer from PR #7.
