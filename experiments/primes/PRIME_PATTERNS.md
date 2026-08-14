# Prime patterns: digits, bases, twins, and the singularity that runs it all

**Date:** 2026-08-13. **Modules:** `e5a_digit_patterns.py`, `e5b_twin_primes.py`, `e5c_explicit_formula.py`, engine in `primestream.py`, checks in `test_primes.py` (12/12). **Scale:** every number below is measured in this repo, default pass $N = 10^8$ (seconds), deep pass $N = 10^{11}$ (4,118,054,813 primes, streamed on the research box in 44 minutes).

The prompt for this thread: investigate properties of primes directly. What patterns appear in different bases; why primes do not repeat their last digit; twin primes; universality; and "the singularity theorem", which we read as the singularity of $\zeta(s)$ at $s = 1$, the pole that runs the prime number theorem. Each section answers one question with measurements first, mechanism second.

## 1. What the last digit of a prime can be, in any base

A number ending in digit $d$ (base $b$) is $\equiv d \pmod b$, so $\gcd(d, b) > 1$ forces a common factor with $b$. Hence every prime $p > b$ ends in one of the $\varphi(b)$ digits coprime to $b$. Base 10: $\{1, 3, 7, 9\}$ (evens are divisible by 2, a trailing 0 or 5 by 5). Base 2 is degenerate: every odd prime ends in 1, the digit carries no information. Base 30: eight legal digits $\{1,7,11,13,17,19,23,29\}$.

Within the legal digits, primes equidistribute (Dirichlet 1837, made quantitative by the prime number theorem in arithmetic progressions). Measured at $10^{11}$: every share in every tested base $b \in \{3,4,10,12,30\}$ is within $2.1 \times 10^{-6}$ of $1/\varphi(b)$ (base 10: within $1.2 \times 10^{-6}$ of exactly $1/4$). There is no favored last digit in any base, asymptotically.

## 2. Why primes do not repeat their last digit (the Lemke Oliver-Soundararajan bias)

Consecutive primes avoid sharing a last digit, by a lot. Measured transition matrix at $10^{11}$, base 10 (row = this prime's digit, column = next prime's):

|      | 1 | 3 | 7 | 9 |
|------|------|------|------|------|
| **1** | 0.1927 | 0.2908 | 0.2914 | 0.2251 |
| **3** | 0.2435 | 0.1879 | 0.2772 | 0.2914 |
| **7** | 0.2541 | 0.2672 | 0.1879 | 0.2908 |
| **9** | 0.3096 | 0.2541 | 0.2436 | 0.1927 |

A memoryless process would put 0.25 everywhere. Even after 4.1 billion primes the diagonal sits at 0.188-0.193: a repeat is still about 24% less likely than chance (31% at $10^8$: the deficit shrinks, slowly). The bias is in every base (repeat share vs naive $1/\varphi(b)$ at $10^{11}$): base 3, 0.4540 vs 0.5; base 4, 0.4571 vs 0.5; base 10, 0.1903 vs 0.25; base 12, 0.1919 vs 0.25; base 30, 0.0627 vs 0.125 (still a 50% deficit at this depth, 65% at $10^8$). More legal digits, stronger avoidance.

The mechanism is not mystical. (i) The cheap first-order reason: after a prime ending in 1, the candidates ending in 3, 7, 9 come **before** the next candidate ending in 1; since the average gap near $10^8$ is $\log 10^8 \approx 18.4$, comparable to one decade, the in-between digits get first shot. (ii) The precise reason (Lemke Oliver-Soundararajan 2016): the Hardy-Littlewood $k$-tuple conjecture predicts the full matrix, with the diagonal deficit decaying like $\log\log x / \log x$, one of the slowest decays in analysis. Measured repeat share by decade $[10^k, 10^{k+1})$, base 10: 0.1206 ($10^3$), 0.1422, 0.1555, 0.1643, 0.1730, 0.1802, 0.1861, 0.1910 ($10^{10}$). Seven decades of crawl and it is still a fifth short of 0.25; at any scale a machine will ever compute, it visibly has not arrived. So: not a law, a bias; the asymptotic limit is uniform $1/\varphi(b)$, approached logarithmically slowly.

The visible asymmetries off the diagonal are real too (9 rolls over to 1 at 0.310 because $+2$ from a 9 lands on a 1; 1 feeds 3 and 7 at 0.291): the wrap-around geometry of the residue circle, again quantified by the same $k$-tuple series.

## 3. The race version: which legal digit is ahead (Chebyshev bias)

Equidistribution is an asymptotic statement. At any finite $x$ someone is ahead, and it is systematically the quadratic **nonresidue** classes (Chebyshev 1853). Measured to $10^{11}$: in the mod-4 race (base-4 last digit 3 vs 1), the 3-side leads at 99.39% of prime steps. The 1-side takes the lead only in narrow windows: first at exactly $x = 26{,}861$ (Leech 1957, reproduced by the stream), then near $6.23 \times 10^5$, near $1.23 \times 10^7$, near $6.4 \times 10^9$, and in the deep zone near $1.9 \times 10^{10}$ where it briefly gets 2,719 primes ahead before the 3-side recovers. Our log-density estimate of "3 ahead" is 0.9972, closing on the Rubinstein-Sarnak value 0.9959 (1994, under GRH plus linear independence of zeros). The mod-3 race never flips in the entire run; the first flip is known to sit near $6.09 \times 10^{11}$ (Bays-Hudson), just past this pass's horizon.

Why nonresidues: $\psi(x; q, a)$ is even-handed, but $\pi$ counts only primes, and the prime **squares** all land in quadratic-residue classes, depressing the prime count there by $\sim \sqrt{x}/\log x$: exactly the size of the fluctuation the L-function zeros produce. The race is a zero-driven oscillation around a square-root-size systematic offset, and Littlewood proved the lead flips infinitely often. This is the first place the side quest touches the main program: the finite-$x$ arithmetic of last digits is controlled by the zeros of Dirichlet L-functions, i.e. by GRH-grade information.

## 4. Twin primes, and the one framework behind sections 2-4

The twin prime conjecture (infinitely many $p$ with $p + 2$ prime) is open. What is not open is how twins are **distributed**, conjecturally to extraordinary accuracy. Hardy-Littlewood: $\pi_2(x) \sim 2 C_2 \int_2^x dt/\log^2 t$ with $C_2 = \prod_{p > 2} (1 - (p-1)^{-2}) = 0.6601618\ldots$ (we compute $C_2$ to $10^{-8}$ from a sieve). Measured at $10^{11}$:

| pairs $(p, p+d)$ | measured | HL predicted | ratio |
|---|---|---|---|
| $d = 2$ (twins) | 224,376,048 | 224,368,866 | 1.000032 |
| $d = 4$ (cousins) | 224,373,161 | 224,368,866 | 1.000019 |
| $d = 6$ (sexy) | 448,725,003 | 448,737,732 | 0.999972 |

Three predictions, three hits at the $3 \times 10^{-5}$ level, including the parameter-free prediction that $d = 6$ pairs are exactly **twice** as common as twins (singular series factor $(3-1)/(3-2) = 2$; measured ratio 1.999879). The convergence is visible decade by decade: the twin ratio walks 0.957 ($10^4$) $\to$ 0.9904 ($10^6$) $\to$ 0.99987 ($10^8$) $\to$ 1.000032 ($10^{11}$). The same series makes 6 the most common gap between consecutive primes from $x \approx 10^3$ on (measured champion in every decade; at $10^{11}$ the leaderboard runs 6 > 12 > 18 > 10 > 2, the primorial-flavored gaps rising; conjectured to hand over to 30 near $10^{35}$, then 210: Odlyzko-Rubinstein-Wolf 1999).

The two famous sums, measured: $\sum_{p \le 10^{10}} 1/p = 3.398115$ vs Mertens $\log\log x + M = 3.398115$ (agreement to the printed digit; divergent, glacially); Brun's twin sum partial $\sum (1/p + 1/(p+2)) = 1.797904$ at $10^{11}$, against the extrapolated full value $B_2 \approx 1.902161$ (convergent: Brun 1919, which is why the twin conjecture cannot be settled by the series alone). Current infinitude state of the art: some gap $\le 246$ occurs infinitely often (Zhang 2013; Maynard-Tao; Polymath8b), 6 under the generalized Elliott-Halberstam conjecture.

The unifying point: sections 2, 3, 4 are one phenomenon. The singular series is **Euler-product data applied to an additive question**: for each prime $p$, a local correction for how a pattern sits mod $p$, multiplied over all $p$, governing patterns in $p, p+2$, in consecutive-prime digits, in races. Multiplicative structure crossed with the additive lattice of the integers.

## 5. The singularity: the pole of $\zeta$ at $s = 1$ is the prime number theorem

We read "the singularity theorem" as the one singularity $\zeta$ has: the simple pole at $s = 1$. (If the Penrose-Hawking general-relativity singularity theorems were meant instead, that is a different subject; say so and we chase it.) The chain of custody:

- **The pole knows there are infinitely many primes.** $\log \zeta(s) = \sum_p \sum_k p^{-ks}/k$; as $s \to 1^+$ the left side blows up, forcing $\sum_p 1/p = \infty$ (Euler). Our Mertens measurement in §4 is this divergence, watched in real time.
- **The pole is the main term.** Riemann-von Mangoldt explicit formula: $\psi(x) = x - \sum_\rho x^\rho/\rho - \log 2\pi - \tfrac12 \log(1 - x^{-2})$. The $x$ is the residue at the pole; each nontrivial zero $\rho = \beta + i\gamma$ contributes an oscillation of amplitude $x^\beta/|\rho|$. PNT ($\psi(x) \sim x$) is **equivalent** to no zeros on $\operatorname{Re} s = 1$ (Hadamard, de la Vallée Poussin 1896, via a Tauberian step). The primes are as regular as the pole and as noisy as the zeros.
- **Measured.** With the first 108 zeros ($T \le 250$) the truncated formula tracks the exact $\psi$ staircase on $[2, 1000]$ with mean error 1.31 (max 6.66 at the big jumps), improving monotonically with the number of zeros (mean 2.39 at 5 zeros, 1.86 at 25, 1.31 at 108). Watching that staircase assemble out of $x^{1/2 + i\gamma}$ waves is the whole subject in one picture: the zeros literally rebuild the primes.
- **RH is the error bar.** Every $\gamma$ we use has $\beta = 1/2$, so every oscillation has amplitude $\sqrt{x}/|\rho|$: square-root cancellation, the smallest the fluctuations can possibly be (a zero pair at $\beta$ forces error $\gg x^\beta$). Scoreboard: at $10^8$, $\pi(x) = 5{,}761{,}455$, the crude $x/\log x$ overshoots by 6.1% (the ratio decays like $1/\log x$, which is why $\operatorname{li}(x)$ is the right main term), and $\operatorname{li}(x) - \pi(x) = 754.4$ sits far inside the Schoenfeld RH band $\sqrt{x}\log x / 8\pi = 7329$. At $10^{11}$: $\pi(x) = 4{,}118{,}054{,}813$ (matching the published count exactly), $\operatorname{li} - \pi = 11{,}588$, RH band 318,690. The gap stays positive throughout our range, but Littlewood proved it flips sign infinitely often; the first flip is expected near $10^{316}$ (Skewes, Bays-Hudson). Moral: at machine scales the zeros' oscillations have not yet had room to swing; trusting small-$x$ monotonicity would have you conjecture a falsehood. The same lesson the project's four-level framing encodes: finite data lives at Level 3; RH is a Level 4 statement.

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
python -m experiments.primes.e5b_twin_primes             # pairs vs HL, Brun, Mertens, gaps
python -m experiments.primes.e5c_explicit_formula        # zeros rebuild psi; PNT scoreboard
python -m experiments.primes.e5a_digit_patterns 1e11     # deep pass (hour-class, checkpointed)
python -m experiments.primes.test_primes                 # 12/12; auto-discovered by run_all_tests
```

Engine: `primestream.py`, a segmented sieve streaming all primes to $N$ in $O(\text{segment})$ memory, one pass feeding e5a and e5b, cached per $N$ under `_cache/`. External anchors reproduced: $\pi(10^8) = 5{,}761{,}455$; $\pi_2(10^8) = 440{,}312$; $\pi(10^{11}) = 4{,}118{,}054{,}813$ and $\pi_2(10^{11}) = 224{,}376{,}048$ (deep pass, 44 minutes on the box, both matching published tables exactly); first mod-4 race flip at 26,861; $\operatorname{li} - \pi = 754$ at $10^8$.

## References

- R. J. Lemke Oliver, K. Soundararajan, *Unexpected biases in the distribution of consecutive primes*, PNAS 113 (2016).
- M. Rubinstein, P. Sarnak, *Chebyshev's bias*, Experiment. Math. 3 (1994).
- G. H. Hardy, J. E. Littlewood, *Some problems of 'Partitio Numerorum' III*, Acta Math. 44 (1923).
- A. Odlyzko, M. Rubinstein, M. Wolf, *Jumping champions*, Experiment. Math. 8 (1999).
- Y. Zhang, *Bounded gaps between primes*, Ann. of Math. 179 (2014); J. Maynard, *Small gaps between primes*, Ann. of Math. 181 (2015); Polymath8b.
- S. M. Voronin, *Theorem on the "universality" of the Riemann zeta-function* (1975); B. Bagchi, thesis and *Recurrence in topological dynamics and the Riemann hypothesis* (1981/87).
- C. Bays, R. Hudson, *A new bound for the smallest x with pi(x) > li(x)* (2000); J. E. Littlewood (1914); S. Skewes (1933/1955).
- T. Nicely, computations of Brun's constant; L. Schoenfeld, *Sharper bounds for the Chebyshev functions* (1976).
