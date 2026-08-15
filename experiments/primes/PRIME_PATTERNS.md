# Prime patterns: digits, bases, twins, and the singularity that runs it all

**Date:** 2026-08-13, deepened 2026-08-14. **Modules:** `e5a_digit_patterns.py`, `e5b_twin_primes.py`, `e5c_explicit_formula.py`, `e5d_riemann_spectrum.py`, `e5e_zero_statistics.py`; engines in `primestream.py` (segmented sieve) and `rsz.py` (Riemann-Siegel bulk zero finder); checks in `test_primes.py` (26/26). **Scale:** every number below is measured in this repo. Default pass $N = 10^8$ (seconds); deep pass $N = 10^{12}$, all **37,607,912,018** primes streamed in 9.7 hours on the research box.

**Predictions registered before the deep pass finished, and how they came out.** Six for six, exact:

| quantity | predicted | measured |
|---|---|---|
| $\pi(10^{12})$ | 37,607,912,018 | 37,607,912,018 |
| twin pairs below $10^{12}$ | 1,870,585,220 | 1,870,585,220 |
| first mod-3 race flip | 608,981,813,029 | 608,981,813,029 |
| first mod-4 race flip | 26,861 | 26,861 |
| $\operatorname{li}(x) - \pi(x)$ at $10^{12}$ | 38,263 | 38,263 |
| base-10 repeat share, decade $10^{11}$ | 0.1951 | 0.1951 |

The last row is the one that was a genuine extrapolation rather than a table lookup: fitting $a + b\log\log x/\log x$ to the seven decades measured at $10^{11}$ predicted 0.1951 for the eighth, and the eighth came in at 0.1951. That is the Lemke Oliver-Soundararajan decay law confirmed quantitatively across nine decades, not merely observed.

The prompt for this thread: investigate properties of primes directly. What patterns appear in different bases; why primes do not repeat their last digit; twin primes; universality; and "the singularity theorem", which we read as the singularity of $\zeta(s)$ at $s = 1$, the pole that runs the prime number theorem. Each section answers one question with measurements first, mechanism second.

## 1. What the last digit of a prime can be, in any base

A number ending in digit $d$ (base $b$) is $\equiv d \pmod b$, so $\gcd(d, b) > 1$ forces a common factor with $b$. Hence every prime $p > b$ ends in one of the $\varphi(b)$ digits coprime to $b$. Base 10: $\{1, 3, 7, 9\}$ (evens are divisible by 2, a trailing 0 or 5 by 5). Base 2 is degenerate: every odd prime ends in 1, the digit carries no information. Base 30: eight legal digits $\{1,7,11,13,17,19,23,29\}$.

Within the legal digits, primes equidistribute (Dirichlet 1837, made quantitative by the prime number theorem in arithmetic progressions). Measured at $10^{12}$: every share in every tested base $b \in \{3,4,10,12,30\}$ is within $9.6 \times 10^{-7}$ of $1/\varphi(b)$ (base 10: within $5.1 \times 10^{-7}$ of exactly $1/4$). There is no favored last digit in any base, asymptotically.

## 2. Why primes do not repeat their last digit (the Lemke Oliver-Soundararajan bias)

Consecutive primes avoid sharing a last digit, by a lot. Measured transition matrix at $10^{12}$, base 10 (row = this prime's digit, column = next prime's):

|      | 1 | 3 | 7 | 9 |
|------|------|------|------|------|
| **1** | 0.1965 | 0.2878 | 0.2876 | 0.2281 |
| **3** | 0.2448 | 0.1926 | 0.2750 | 0.2876 |
| **7** | 0.2538 | 0.2658 | 0.1926 | 0.2878 |
| **9** | 0.3049 | 0.2538 | 0.2448 | 0.1965 |

A memoryless process would put 0.25 everywhere. Even after 37.6 billion primes the diagonal sits at 0.193-0.197: a repeat is still about 22% less likely than chance (31% at $10^8$: the deficit shrinks, slowly). The bias is in every base (repeat share vs naive $1/\varphi(b)$ at $10^{12}$): base 3, 0.4574 vs 0.5; base 4, 0.4602 vs 0.5; base 10, 0.1946 vs 0.25; base 12, 0.1959 vs 0.25; base 30, 0.0671 vs 0.125 (still a 46% deficit at this depth, 65% at $10^8$). More legal digits, stronger avoidance.

The mechanism is not mystical. (i) The cheap first-order reason: after a prime ending in 1, the candidates ending in 3, 7, 9 come **before** the next candidate ending in 1; since the average gap near $10^8$ is $\log 10^8 \approx 18.4$, comparable to one decade, the in-between digits get first shot. (ii) The precise reason (Lemke Oliver-Soundararajan 2016): the Hardy-Littlewood $k$-tuple conjecture predicts the full matrix, with the diagonal deficit decaying like $\log\log x / \log x$, one of the slowest decays in analysis. Measured repeat share by decade $[10^k, 10^{k+1})$, base 10: 0.1206 ($10^3$), 0.1422, 0.1555, 0.1643, 0.1730, 0.1802, 0.1861, 0.1910, 0.1951 ($10^{11}$). Nine decades of crawl and it is still a fifth short of 0.25; at any scale a machine will ever compute, it visibly has not arrived. The fit $a + b\log\log x/\log x$ over the first eight decades predicted the ninth to four decimals (see the prediction table above), with intercept $a = 0.2564$ against the theoretical limit $0.25$. So: not a law, a bias; the asymptotic limit is uniform $1/\varphi(b)$, approached logarithmically slowly.

The visible asymmetries off the diagonal are real too (9 rolls over to 1 at 0.310 because $+2$ from a 9 lands on a 1; 1 feeds 3 and 7 at 0.291): the wrap-around geometry of the residue circle, again quantified by the same $k$-tuple series.

## 3. The race version: which legal digit is ahead (Chebyshev bias)

Equidistribution is an asymptotic statement. At any finite $x$ someone is ahead, and it is systematically the quadratic **nonresidue** classes (Chebyshev 1853).

**Mod 4** (base-4 last digit 3 vs 1), measured to $10^{12}$: the 3-side leads at 99.93% of prime steps, peaking at +68,375. The 1-side takes the lead only in narrow windows, first at exactly $x = 26{,}861$ (Leech 1957, reproduced by the stream) and deepest at $x = 1.87 \times 10^{10}$, where it gets 2,719 primes ahead before the 3-side recovers. Our log-density estimate of "3 ahead" is 0.9987, against the Rubinstein-Sarnak value 0.9959 (1994, under GRH plus linear independence of zeros).

**Mod 3, and the headline of the deep pass.** Chebyshev's bias held without a single exception for the first 23 billion primes, the lead climbing to +63,309. Then the stream found the first sign change at

$$x = 608{,}981{,}813{,}029$$

which is **exactly** the published Bays-Hudson value, located independently with that number appearing nowhere in the code. Getting it required every prime below $6\times10^{11}$ counted once, residues assigned correctly across ~1,220 segment boundaries, the cumulative lead carried exactly through all of them, and our convention matching the literature's ($p = 2$ counted in class 2, $p = 3$ excluded). One dropped prime anywhere in 23 billion moves the answer.

The shape of the excursion is the interesting part. It does not merely graze zero: the lead plunges to $-1{,}538$ at $x = 609{,}224{,}663{,}413$, some 240 million past the crossing, then repairs itself. And the scales are exactly what the theory orders. At the flip, $\sqrt{x}/\log x = 28{,}759$, which is simultaneously the size of the systematic bias (the prime squares $p^2 \equiv 1$ that class 1 is "credited" with, $\tfrac12\pi(\sqrt x) = 31{,}296$) and the size of the fluctuation the L-function zeros supply. Drift and noise are the same order, which is why the bias is persistent, why it is not permanent, and why Littlewood could prove the sign changes infinitely often. Measured against that scale, the peak lead is $1.64\sqrt{x}/\log x$ and the deepest dip only $0.053$ of it. In relative terms the whole race lives in the eighth digit: 1,538 out of 23 billion is an imbalance of $6.7\times10^{-8}$.

Why nonresidues: $\psi(x; q, a)$ is even-handed, but $\pi$ counts only primes, and the prime **squares** all land in quadratic-residue classes, depressing the prime count there by $\sim \sqrt{x}/\log x$: exactly the size of the fluctuation the L-function zeros produce. The race is a zero-driven oscillation around a square-root-size systematic offset, and Littlewood proved the lead flips infinitely often. This is the first place the side quest touches the main program: the finite-$x$ arithmetic of last digits is controlled by the zeros of Dirichlet L-functions, i.e. by GRH-grade information.

**And unlike the GUE statistics of §5c, this observable is not RH-blind.** The race amplitude comes from terms $x^\rho/\rho$ summed over the zeros of the relevant L-function, so its size is governed by their **real parts**, not merely their heights. A single zero with $\beta = 0.6$ would contribute a term fifteen times the whole on-line contribution; the bias would have been swamped long before $6\times10^{11}$ and the race would look violent and early instead of clean and late. What we measured is a long unbroken bias at exactly the $\sqrt x$ scale with one shallow dip, which is a fingerprint of the zeros sitting on the line. That is weak evidence, since a zero at $\beta = 0.5001$ would be invisible at this height, and it is consistency rather than proof. But it is a genuine contrast with §5c, where every statistic is a function of heights alone and is provably unchanged when zeros are moved off the line. §5d works out exactly how much purchase this family of observables has, and the answer is sobering enough to explain why nobody tests RH with primes.

## 4. Twin primes, and the one framework behind sections 2-4

The twin prime conjecture (infinitely many $p$ with $p + 2$ prime) is open. What is not open is how twins are **distributed**, conjecturally to extraordinary accuracy. Hardy-Littlewood: $\pi_2(x) \sim 2 C_2 \int_2^x dt/\log^2 t$ with $C_2 = \prod_{p > 2} (1 - (p-1)^{-2}) = 0.6601618\ldots$ (we compute $C_2$ to $10^{-8}$ from a sieve). Measured at $10^{12}$:

| constellation | measured | HL predicted | ratio |
|---|---|---|---|
| $(p, p+2)$ twins | 1,870,585,220 | 1,870,559,878 | 1.000014 |
| $(p, p+4)$ cousins | 1,870,585,459 | 1,870,559,878 | 1.000014 |
| $(p, p+6)$ sexy | 3,741,217,498 | 3,741,119,756 | 1.000026 |
| $(p, p{+}2, p{+}6)$ triplets | 152,850,135 | | |
| $(p, p{+}4, p{+}6)$ triplets | 152,839,134 | | |
| $(p, p{+}2, p{+}6, p{+}8)$ quadruplets | 8,398,278 | | |

Three parameter-free predictions, three hits at the $3 \times 10^{-5}$ level, including that $d = 6$ pairs are exactly **twice** as common as twins (singular series factor $(3-1)/(3-2) = 2$; measured ratio 2.000025). The convergence is visible decade by decade: the twin ratio walks 0.957 ($10^4$) $\to$ 0.9904 ($10^6$) $\to$ 0.99987 ($10^8$) $\to$ 1.000032 ($10^{11}$) $\to$ 1.000014 ($10^{12}$).

Two things worth noticing in that table. **Cousins tie twins to nine digits**: 1,870,585,459 against 1,870,585,220, a difference of 239 in 1.87 billion, because their singular series is not approximately equal but *identical*. And the two admissible triplet shapes also tie (152,850,135 vs 152,839,134), for the same reason. Nothing in the primes distinguishes $\{0,2\}$ from $\{0,4\}$, or $\{0,2,6\}$ from $\{0,4,6\}$: only the local obstructions matter, and those agree. The same series makes 6 the most common gap between consecutive primes from $x \approx 10^3$ on (measured champion in every decade; at $10^{12}$ the leaderboard runs 6 (3.44e9) > 12 > 18 > 10 > 4 > 2, the primorial-flavored gaps rising; conjectured to hand over to 30 near $10^{35}$, then 210: Odlyzko-Rubinstein-Wolf 1999).

The two famous sums, measured: $\sum_{p \le 10^{12}} 1/p = 3.580436$ vs Mertens $\log\log x + M = 3.580436$ (agreement to every printed digit; divergent, glacially); Brun's twin sum partial $\sum (1/p + 1/(p+2)) = 1.806592$ at $10^{12}$, against the extrapolated full value $B_2 \approx 1.902161$ (convergent: Brun 1919, which is why the twin conjecture cannot be settled by the series alone).

**A new one from the adjacent-gap accumulator: gaps remember their predecessor, and one transition is outright forbidden.** Comparing the joint law of consecutive gaps $(g_n, g_{n+1})$ against the independent product at $10^{12}$: a gap of 2 followed by another gap of 2 has observed/independent ratio **exactly 0.0000**, because $p, p+2, p+4$ always contains a multiple of 3, so no twin gap can ever be immediately followed by another. A gap of 2 followed by 4 is **1.64x** more likely than independence (that is the admissible triplet $\{0,2,6\}$ asserting itself), and 6 followed by 6 is suppressed to 0.82x. The consecutive-gap sequence is not a renewal process: the same admissibility bookkeeping that prices the constellations also prices the transitions between gaps. Current infinitude state of the art: some gap $\le 246$ occurs infinitely often (Zhang 2013; Maynard-Tao; Polymath8b), 6 under the generalized Elliott-Halberstam conjecture.

The unifying point: sections 2, 3, 4 are one phenomenon. The singular series is **Euler-product data applied to an additive question**: for each prime $p$, a local correction for how a pattern sits mod $p$, multiplied over all $p$, governing patterns in $p, p+2$, in consecutive-prime digits, in races. Multiplicative structure crossed with the additive lattice of the integers.

## 5. The singularity: the pole of $\zeta$ at $s = 1$ is the prime number theorem

We read "the singularity theorem" as the one singularity $\zeta$ has: the simple pole at $s = 1$. (If the Penrose-Hawking general-relativity singularity theorems were meant instead, that is a different subject; say so and we chase it.) The chain of custody:

- **The pole knows there are infinitely many primes.** $\log \zeta(s) = \sum_p \sum_k p^{-ks}/k$; as $s \to 1^+$ the left side blows up, forcing $\sum_p 1/p = \infty$ (Euler). Our Mertens measurement in §4 is this divergence, watched in real time.
- **The pole is the main term.** Riemann-von Mangoldt explicit formula: $\psi(x) = x - \sum_\rho x^\rho/\rho - \log 2\pi - \tfrac12 \log(1 - x^{-2})$. The $x$ is the residue at the pole; each nontrivial zero $\rho = \beta + i\gamma$ contributes an oscillation of amplitude $x^\beta/|\rho|$. PNT ($\psi(x) \sim x$) is **equivalent** to no zeros on $\operatorname{Re} s = 1$ (Hadamard, de la Vallée Poussin 1896, via a Tauberian step). The primes are as regular as the pole and as noisy as the zeros.
- **Measured.** With the first 108 zeros ($T \le 250$) the truncated formula tracks the exact $\psi$ staircase on $[2, 1000]$ with mean error 1.31 (max 6.66 at the big jumps), improving monotonically with the number of zeros (mean 2.39 at 5 zeros, 1.86 at 25, 1.31 at 108). Watching that staircase assemble out of $x^{1/2 + i\gamma}$ waves is the whole subject in one picture: the zeros literally rebuild the primes.
- **RH is the error bar.** Every $\gamma$ we use has $\beta = 1/2$, so every oscillation has amplitude $\sqrt{x}/|\rho|$: square-root cancellation, the smallest the fluctuations can possibly be (a zero pair at $\beta$ forces error $\gg x^\beta$). Scoreboard: at $10^8$, $\pi(x) = 5{,}761{,}455$, the crude $x/\log x$ overshoots by 6.1% (the ratio decays like $1/\log x$, which is why $\operatorname{li}(x)$ is the right main term), and $\operatorname{li}(x) - \pi(x) = 754.4$ sits far inside the Schoenfeld RH band $\sqrt{x}\log x / 8\pi = 7329$. At $10^{12}$: $\pi(x) = 37{,}607{,}912{,}018$ (matching the published count exactly), $\operatorname{li} - \pi = 38{,}263$, RH band 1,099,403, and the crude $x/\log x$ still overshoots by 3.9%. The gap stays positive throughout our range, but Littlewood proved it flips sign infinitely often; the first flip is expected near $10^{316}$ (Skewes, Bays-Hudson). Moral: at machine scales the zeros' oscillations have not yet had room to swing; trusting small-$x$ monotonicity would have you conjecture a falsehood. The same lesson the project's four-level framing encodes: finite data lives at Level 3; RH is a Level 4 statement.

## 5b. The dual direction: the primes locate the zeros (e5d)

§5 ran the explicit formula forwards (zeros rebuild $\psi$). It runs backwards too. Since $-\zeta'/\zeta(s) = \sum_n \Lambda(n) n^{-s}$ is built from prime powers alone and has a pole of residue $-1$ at every nontrivial zero, the Fejér-regularized transform

$$\Phi_X(t) = -\sum_{n \le X} \Lambda(n)\, n^{-1/2} \cos(t \log n)\left(1 - \frac{\log n}{\log X}\right)$$

peaks at each $\gamma$. Input: a list of primes and their logarithms. No zeta values, no functional equation, nothing analytic. Measured: **all 29 zeros with $t < 100$ recovered at every cutoff** $X \in \{10^3, 10^4, 10^5, 10^6\}$, median error $4.6\times10^{-3} \to 2.7\times10^{-3} \to 1.2\times10^{-3} \to 1.6\times10^{-3}$.

Two things stated precisely, both measured:

- **Accurate, not convergent.** The error falls with $X$ then flattens. This is consistent with (and sharpens) the repo's earlier CCM probe (`orchestrator_sessions/overnight_2026_06_03/stream2_ccm_selfadjoint_obstruction.py`), which showed the *raw* sum at fixed $t = \gamma_1$ oscillates without a limit. The zero is encoded in where the resonance sits, not in the value of any one sum: the peak *position* is a good estimator, and it is not a convergent one.
- **The Beurling control kills the obvious over-reading.** The construction consumes exactly one structural fact: $\Lambda$ is supported on prime powers, i.e. the Euler product. So it must work for a Beurling generalized-prime system (Euler product, no additive lattice), and it does: 66 peaks of its own in the same window, median distance $0.456$ from a zeta $\gamma$ (zeta's own: $0.0016$, i.e. 280x closer). **Having a spectrum is a property of any Euler product. Where the spectrum lies is what no Euler product determines, and that is RH.** This is the counting-side twin of what `positivity/e3s_connes_eta.py` found on the form side (its Connes-style recovery reproduces D-H's on-line zeros just as well).

## 5c. The zeros repel like random-matrix eigenvalues, and that is Level 3 (e5e)

New infrastructure: `rsz.py`, a vectorized float64 Riemann-Siegel $Z$ with sign-change bracketing and vectorized bisection, at ~600 zeros/second (mpmath's `zetazero` is ~1 zero/second at index 5000, so bulk statistics were previously out of reach in this repo). Validated three ways: zero counts match Odlyzko's published table exactly in every window tested; positions agree to $4.9\times10^{-5}$ at $t \approx 5000$ (accuracy improves with height as the $O(t^{-3/4})$ remainder demands); and counts match Riemann-von Mangoldt to under one zero.

Statistics on five heights, all cut to a common 9,999 spacings so the columns compare like for like (heights $10^{12}$, $10^{21}$, $10^{22}$ come from Odlyzko's tables; $10^6$ is 40,066 zeros computed here):

| zeros near | distance to GUE | distance to Poisson | spacings under 0.1 |
|---|---|---|---|
| the 10,000th | 0.0275 | 0.3066 | 0.050% |
| height $10^6$ (ours) | 0.0146 | 0.2941 | 0.080% |
| the $10^{12}$th | 0.0056 | 0.2828 | 0.060% |
| the $10^{21}$st | 0.0077 | 0.2781 | 0.100% |
| the $10^{22}$nd | 0.0074 | 0.2827 | 0.070% |
| Poisson control | 0.2830 | 0.0055 | 9.551% |
| **GUE theory** | 0 | 0.283 | 0.107% |

Montgomery's pair correlation is reproduced directly: at $u = 0.5$ the sine kernel $1 - (\sin \pi u/\pi u)^2$ says $0.595$, and the measurements walk $0.548 \to 0.551 \to 0.589 \to 0.606 \to 0.583$ up the height ladder. Level repulsion is unmistakable: 0.05-0.1% of spacings fall below a tenth of the mean, against 9.5% for uncorrelated points. The zeros avoid each other exactly as GUE eigenvalues do, and the agreement sharpens with height (Montgomery-Odlyzko, confirmed here on our own data at $10^6$ and on Odlyzko's at $10^{22}$).

**And it buys nothing for RH, which is the point.** Every statistic above is a function of the heights $\gamma$. RH is a claim about real parts. The module demonstrates this literally: take our 40,066 computed zeros, move 400 of them to $\mathrm{Re}\,\rho = 0.8085$ (where D-H's off-line zeros genuinely sit), and RH is false for that set while every statistic is unchanged **bit for bit** ($\max|\mathrm{Re}\,\rho - 1/2|$ goes $0 \to 0.3085$; KS-vs-GUE stays $0.012684$). This is the four-level framing's Level 3 made quantitative, and it agrees with `docs/03_research/quantum_chaos_and_the_zeros.md` (which argued it in prose) and with the screen formalized in `positivity/offline_flip_test.py`. GUE agreement is a compass pointing at a spectral proof; it is not evidence that the statement is true.

**The D-H control was attempted and refused, which is itself a finding about our infrastructure.** The natural empirical control is to run the same battery on Davenport-Heilbronn, which genuinely has off-line zeros. Our scan to $T = 200$ found 65 distinct heights and, usefully, **four off-line conjugate pairs**: $\beta = 0.8085, 0.6508, 0.5744, 0.7243$ (with partners $1-\beta$) at heights $85.699$, $114.163$, $166.479$, $176.702$. But the functional equation (degree 1, conductor 5) predicts about 128 zeros below that height, so the list is only ~51% complete: `_shared/davenport_heilbronn.py` is a coarse grid search, not a bracketing zero finder. Run anyway, the battery reports "D-H is not GUE" (KS 0.22 vs 0.15), and that is an **artifact**: deleting points at random from a repulsive sequence makes it look Poisson. So no D-H spacing statistic is reported. Closing this properly needs a Hardy-function analogue of $Z(t)$ for D-H, giving sign-change bracketing plus a Riemann-von Mangoldt completeness check, exactly the two properties that make the zeta rows above trustworthy. That is a well-scoped piece of future infrastructure.

One detail from the scan does survive and sharpens §5c: each off-line pair shares **one height exactly** (the functional equation puts $\beta$ and $1-\beta$ at the same $\gamma$). A height-only statistic therefore sees a spacing of exactly zero there and cannot tell that anything is off the line. The blindness is not subtle.

## 5d. What actually tests RH, and verifying it ourselves to height $10^7$ (e5f)

§5c ends on a negative: zero statistics are RH-blind. §3 ends on a positive: the Chebyshev races *do* see real parts. The obvious next move is to build a prime-side race observable with real teeth. That move is dead on arrival, and the reason is quantitative rather than a failure of imagination.

**The detection threshold.** Every prime-side statistic factors through the zeros as a sum of $x^\rho/\rho$, so a hypothetical off-line zero contributes with amplitude $x^\beta/\gamma$. RH is already verified below height $3\times10^{12}$, so any off-line zero must hide above that and arrives pre-suppressed by that $1/\gamma$. For its term to clear the ordinary on-line noise $\sqrt{x}\log x$ one needs $x^{\beta-1/2} > \gamma$, giving:

| $\beta$ | $x$ needed to see it |
|---|---|
| 0.90 | $10^{36}$ |
| 0.75 | $10^{58}$ |
| 0.60 | $10^{150}$ |
| 0.55 | $10^{307}$ |
| 0.51 | beyond double precision |

We just spent ten hours reaching $10^{12}$. No engineering closes a gap of 138 orders of magnitude. The refinements fail too: subtracting the known zeros and testing the residual has sensitivity set by how many zeros you use, but the truncation error $\sim (x/T)\log^2 x$ forces $T \gtrsim x$, so you would compute $10^{12}$ zeros to test $10^{12}$ primes and it collapses into direct zero verification; Weil-type test functions concentrated near a suspicious height are "look for a zero there" in disguise. The pattern is structural: **length in $x$ buys $x^{\beta-1/2}$, height in $T$ buys the zeros themselves.** Searching height is exponentially cheaper, which is exactly why every RH verification on record (Platt to $3\times10^{12}$, Gourdon to $10^{13}$) counts zeros and none counts primes.

**So we counted zeros.** `e5f_rh_verification.py` walks Gram points $g_n$ (where $\theta(g_n) = n\pi$), which costs about one evaluation of $Z$ per zero instead of the eighty-odd that bisection costs. Since $N(t) = \theta(t)/\pi + 1 + S(t)$ counts *all* zeros of $\zeta$ in the strip up to $t$, while every sign change of the Hardy function $Z$ is a zero *on* the line, finding exactly $n+1$ sign changes below $g_n$ pins $S(g_n) = 0$ and leaves no room for an off-line zero. Gram's law fails infinitely often, so the count is organized by Gram blocks with Rosser's rule, and blocks that come up short are subdivided until the missing sign changes appear.

**Result:**

> Every one of the **21,136,125** zeros of $\zeta$ with $0 < \operatorname{Im}\rho \le 10^7$ is simple and lies exactly on the critical line, and (by the Turing closure below) there are no others.

17,946,647 Gram blocks, Gram's law failing on 14.85% of them (longest block 7), one boundary merge, zero unresolved blocks, 1h54m.

**The failure that came first, because it is the useful part.** The initial run came up *exactly 2 zeros short* and flagged one Gram block, rather than quietly declaring success. Diagnosis: near $t = 6{,}820{,}052$ two zeros sit $0.19$ of a mean spacing apart, both inside one Gram interval, so they contribute no *net* sign change at Gram resolution; a zero also lands essentially on the block boundary ($|Z| = 0.0045$ against a local scale of 50), pushing the pair into the neighbouring block whose surplus was invisible. Recounting a wider window found all 60 zeros present, confirming the shortfall was accounting rather than arithmetic and certainly not RH. The fix absorbs neighbouring blocks until the merged region balances. A second bug surfaced in the same pass: near the top of a range the window can hold fewer than two good Gram points, and the widening logic was capped at the target, so it looped forever. Both are fixed and both are covered by tests. **A genuine counterexample would look different: a Gram block that stays short at every refinement depth**, which is why unresolved blocks are reported individually rather than folded into a total.

**Turing's method: the count is now pinned from both sides.** Counting sign changes gives only half the argument. At a Gram point, $S(g_m) = N(g_m) - m - 1$ is an *integer*, and finding $m+1$ zeros on the line gives $S(g_m) \ge 0$; what was missing was $S(g_m) \le 0$, which is exactly what Turing's method supplies. Since $N$ is non-decreasing and every zero we locate above $g_m$ is genuine,

$$S(t) \ge S(g_m) + \big(F(t) - F(g_m)\big) - \frac{\theta(t) - \theta(g_m)}{\pi},$$

and integrating over a stretch of $k$ Gram intervals, then combining with an explicit bound $B$ on $\left|\int S\right|$, gives $S(g_m) \le (B + C - A)/L$ where $L$ is the stretch length, $A = \sum_i (g_{m+k} - \gamma_i)$ over the zeros found in it, and $C = \frac1\pi\int(\theta(t) - \theta(g_m))\,dt$. If that falls below 1, the integer $S(g_m)$ is $\le 0$, hence exactly 0.

We use **Trudgian 2014** (*Improvements to Turing's Method II*, Thm 1): $\left|\int_{t_1}^{t_2} S\right| \le 1.698 + 0.183\log\log t_2 + 0.049\log t_2$ for $t_2 > t_1 > 10^5$. At the top of our range ($B = 2.997$) an 80-interval stretch gives

$$S(g_m) \le 0.0883 < 1 \implies S(g_m) = 0.$$

So the verification is not merely "the count came out right": **no zero below height $10^7$ is missing, therefore none can be sitting off the critical line.** The convergence is fast (S bound $0.93$ at $k=10$, $0.37$ at $k=20$, $0.19$ at $k=40$, $0.088$ at $k=80$), so the closing argument costs seconds on top of a two-hour count.

**Certified signs: the last gap closed.** The argument above is a chain of theorems fed by floating-point numbers, so the remaining risk was a wrong *sign* near a very close pair. Certified mode removes it. Every sign the count rests on is accepted only when $|Z|$ exceeds a rigorous error bound

$$\varepsilon(t) = \underbrace{0.127\,t^{-3/4}}_{\text{Gabcke, } t \ge 200} + \underbrace{4\sqrt{\nu}\,(4u(|\theta| + t\log\nu) + u) + 2\nu u}_{\text{float64 rounding, } u = 2^{-53}},$$

and anything closer is recomputed in exact arithmetic. The first term is **Gabcke (1979)**, whose bound on the discarded Riemann-Siegel tail is $|R_K| < c_K t^{-(2K+3)/4}$ for $t \ge 200$ with $c_0 = 0.127$ (Odlyzko calls these essentially optimal for $K \le 4$); we keep $C_0$ only, so $K = 0$. The second term is an explicit and deliberately generous accounting of rounding: the phase $\theta(t) - t\log n$ is formed from quantities of size $t\log t$, cosine is 1-Lipschitz, and the weights $n^{-1/2}$ sum to at most $2\sqrt{\nu}$.

The budget is checked against reality rather than trusted: measured error versus bound is $1.15\times10^{-4}$ vs $1.27\times10^{-4}$ at $t = 10^4$, $1.9\times10^{-6}$ vs $4.4\times10^{-6}$ at $10^6$, $1.3\times10^{-7}$ vs $9.4\times10^{-6}$ at $10^7$, and $9.7\times10^{-7}$ vs $1.8\times10^{-4}$ at $10^8$. The crossover is visible: truncation dominates up to about $10^7$, rounding beyond it. At the top of our range a typical Gram point has $|Z| \approx 0.98$ against $\varepsilon \approx 9.4\times10^{-6}$, a margin of five orders of magnitude, so escalation is rare: 349 points in the 1.75 million zeros below $10^6$, at an 18% cost over the uncertified run.

**So the chain is complete.** Certified sign changes give a rigorous lower bound on the zero count; Turing's method with Trudgian's bound closes it from above; the two meet at $S(g_m) = 0$. Every zero below the verified height is simple, on the critical line, and none is missing. The result is long known ($10^7$ sits far below Platt's $3\times10^{12}$) and this is not a formal proof artifact: it is ordinary code, so it rests on the correctness of numpy, mpmath and the implementation, not on a proof assistant. What is ours is the whole pipeline, from the Riemann-Siegel formula through the Gram-block bookkeeping and the Turing closure to the certified signs, cross-checked against Odlyzko's published table at every height we can reach.

## 6. Universality, both meanings

**Base-universality of everything above.** Nothing in §§1-4 is about ten fingers: legal digits are the units mod $b$, shares go to $1/\varphi(b)$, the repeat deficit appears in every base with strength increasing in $\varphi(b)$, the races run in every modulus with the nonresidues ahead. The decimal system is a viewing window, not a mechanism. Any claimed "pattern in the digits of primes" that does not survive a change of base is a property of the base, not of the primes.

**Voronin universality of $\zeta$.** The word "universality" has a precise, startling meaning for zeta (Voronin 1975): vertical shifts $\zeta(s + i\tau)$ approximate, uniformly and to any accuracy, **every** non-vanishing analytic function on any disc in the strip $1/2 < \operatorname{Re} s < 1$, for a positive-density set of shifts $\tau$. Zeta contains every possible analytic behavior in its critical strip. The RH hook (Bagchi 1981): RH is equivalent to $\zeta$ being able to approximate **itself** in this sense (strong recurrence). So universality is not decoration; it is one more RH-equivalent lens, and it lives on the value-distribution side rather than the zero side.

## 7. Repdigit primes: the other sense of "nonrepeating digits"

Can a prime have **all** digits equal (base 10: $dd\ldots d$)? Almost never, for two stacked reasons: $dd\ldots d = d \times \underbrace{11\ldots1}_{n}$, so $d > 1$ is composite on its face; and the repunit $R_n = (10^n - 1)/9$ satisfies $R_m \mid R_{mn}$, so $R_n$ can be prime only for prime $n$. Survivors are rare: base-10 repunit primes are proven for $n = 2, 19, 23, 317, 1031, 49081$, with larger known candidates (86453, 109297, 270343) established as probable primes. Base 2 repunits are the Mersenne numbers $2^n - 1$: 52 known Mersenne primes as of the October 2024 discovery of $2^{136279841} - 1$. Same structure, every base: repetition is multiplicative structure, and multiplicative structure is what primes refuse.

## 8. Why this side quest feeds the main program

Every phenomenon measured here is the **interaction of the Euler product with the additive lattice $\mathbb{Z}$**: singular series (multiplicative local data) governing additive patterns (§§2-4), theta/Poisson summation standing behind the explicit formula that turns zeros into the $\psi$ staircase (§5). That pairing is precisely the two-sidedness the missing-object interface calls the additive-lattice clause, and the Beurling control (`experiments/_shared/beurling.py`) is its photographic negative: a generalized-prime system with an Euler product but **no digits at all** (no integer lattice, hence no residue classes, no last-digit bias, no Hardy-Littlewood series, no theta identity). Seen from this thread, the Beurling discipline's fourth clause is just: a real proof must consume the structure that makes §§2-5 true, not merely the circle circumferences. The D-H control is silent here by design (no Euler product means no primes to count).

## 9. Files, commands, tests

```powershell
python -m experiments.primes.e5a_digit_patterns          # digits, bases, races (1e8, seconds)
python -m experiments.primes.e5b_twin_primes             # constellations vs HL, Brun, Mertens, gaps
python -m experiments.primes.e5c_explicit_formula        # zeros rebuild psi; PNT scoreboard
python -m experiments.primes.e5d_riemann_spectrum        # primes locate the zeros; Beurling control
python -m experiments.primes.e5e_zero_statistics         # GUE statistics to the 10^22nd zero
python -m experiments.primes.e5f_rh_verification 1e7               # verify RH to height 10^7 (~2 h)
python -m experiments.primes.e5f_rh_verification 1e6 certified     # ... with every sign certified
python -m experiments.primes.e5a_digit_patterns 1e12     # deep pass (overnight, checkpointed)
python -m experiments.primes.test_primes                 # 31/31; auto-discovered by run_all_tests
```

**External datasets.** `e5e` uses A. M. Odlyzko's published tables of zeta zeros, which reach heights no machine here can compute: `zeros1` (first $10^5$ zeros), `zeros3` (zeros $10^{12}{+}1$ through $10^{12}{+}10^4$), `zeros4` ($10^{21}$), `zeros5` ($10^{22}$), from `https://www-users.cse.umn.edu/~odlyzko/zeta_tables/`. They are fetched on demand into the gitignored `_cache/odlyzko/` (about 2 MB total); the module prints the exact `curl` line if they are absent, and `test_primes.py` skips rather than fails the cross-check when they are. Everything else on this page is computed in-repo. The tables are also used as an independent check on `rsz.py`: our own zero positions agree with Odlyzko's to $10^{-4}$ at $t \approx 5000$, and the counts agree exactly.

Engines: `primestream.py`, a segmented sieve streaming all primes to $N$ in $O(\text{segment})$ memory, one pass feeding e5a and e5b, cached per $N$ under `_cache/`; and `rsz.py` for bulk zeros. The sieve's accumulators are checked for **segment-size invariance** (every integer accumulator is bit-identical across three segment sizes, including a prime-sized one), which is what makes the overnight deep passes trustworthy, and the constellation counts are checked against a brute-force scan rather than pinned to remembered values. External anchors reproduced, every one exactly: $\pi(10^8) = 5{,}761{,}455$ and $\pi_2(10^8) = 440{,}312$; $\pi(10^{12}) = 37{,}607{,}912{,}018$ and $\pi_2(10^{12}) = 1{,}870{,}585{,}220$ (deep pass, 9.7 hours); the first mod-4 race flip at 26,861 and the first mod-3 flip at 608,981,813,029; $\operatorname{li} - \pi = 754$ at $10^8$ and 38,263 at $10^{12}$.

## References

- R. J. Lemke Oliver, K. Soundararajan, *Unexpected biases in the distribution of consecutive primes*, PNAS 113 (2016).
- M. Rubinstein, P. Sarnak, *Chebyshev's bias*, Experiment. Math. 3 (1994).
- G. H. Hardy, J. E. Littlewood, *Some problems of 'Partitio Numerorum' III*, Acta Math. 44 (1923).
- A. Odlyzko, M. Rubinstein, M. Wolf, *Jumping champions*, Experiment. Math. 8 (1999).
- Y. Zhang, *Bounded gaps between primes*, Ann. of Math. 179 (2014); J. Maynard, *Small gaps between primes*, Ann. of Math. 181 (2015); Polymath8b.
- S. M. Voronin, *Theorem on the "universality" of the Riemann zeta-function* (1975); B. Bagchi, thesis and *Recurrence in topological dynamics and the Riemann hypothesis* (1981/87).
- C. Bays, R. Hudson, *A new bound for the smallest x with pi(x) > li(x)* (2000); J. E. Littlewood (1914); S. Skewes (1933/1955).
- T. Nicely, computations of Brun's constant; L. Schoenfeld, *Sharper bounds for the Chebyshev functions* (1976).
- H. L. Montgomery, *The pair correlation of zeros of the zeta function* (1973); F. J. Dyson (the tea, 1972).
- J. B. Rosser, J. M. Yohe, L. Schoenfeld, *Rigorous computation and the zeros of the Riemann zeta-function* (1969), for Gram blocks and Rosser's rule; A. M. Turing, *Some calculations of the Riemann zeta-function* (1953), corrected by R. S. Lehman (1970), for the closing argument; **T. S. Trudgian, *Improvements to Turing's Method II*, arXiv:1406.3416 (2014), Theorem 1**, for the explicit bound on $\int S$ used here; **W. Gabcke, *Neue Herleitung und explizite Restabschätzung der Riemann-Siegel-Formel*, thesis, Göttingen (1979)**, for the rigorous remainder bounds behind certified mode; D. J. Platt (RH to $3\times10^{12}$), X. Gourdon (to $10^{13}$).
- A. M. Odlyzko, *On the distribution of spacings between zeros of the zeta function*, Math. Comp. 48 (1987), and the published zero tables used here.
- E. C. Titchmarsh / C. L. Siegel, the Riemann-Siegel formula; H. Riesel, *Prime Numbers and Computer Methods* (the $C_0$ remainder used in `rsz.py`).
