# 4A + 4C: Vinogradov-Korobov and the Conditional Improvement Landscape (Literature)

> The unconditional zero-free region for $\zeta(s)$ has been stuck at the **Vinogradov-Korobov** form
>
> $$\sigma \geq 1 - \frac{c}{(\log|t|)^{2/3}\, (\log\log|t|)^{1/3}}$$
>
> since 1958. RH is the limit $\sigma \geq 1/2$: the exponent on $\log|t|$ would have to drop from $2/3$ to $\infty$ (the region would have to extend a *positive* width all the way to the critical line). No method has improved the $2/3$ exponent in 67 years. This document covers two pending TODOs together:
>
> - **4A** (Vinogradov-Korobov reproduction): what the V-K method does, why the $2/3$ exponent is structurally hard, where the bottleneck lives.
> - **4C** (conditional improvements: Heath-Brown / Pintz / Ford / Bourgain): which conditional results, if made unconditional, would push the exponent.
>
> Pairing them mirrors how [3E](../positivity/3e_li_de_bruijn_newman.md) covered Li + de Bruijn-Newman together: both 4A and 4C concern the **classical analytic route** to a zero-free region. They share the same explicit-formula machinery and the same bottleneck (the prime sum), and the conditional landscape only makes sense as deltas off the V-K baseline.
>
> **Cross-cut to the project's experimental thread.** Arch 4B-4E.7 explored the *auxiliary inequality* end of this architecture (non-negative trigonometric polynomials and multivariate generalizations). The auxiliary inequality is one of three inputs to a V-K-style zero-free region. The other two inputs (exponential sum bounds and explicit formula bookkeeping) are what 4A and 4C are about. **The conclusion below**: 4B's saturation of Fejér means the auxiliary-inequality input is essentially closed; the V-K bottleneck lives in the exponential sum estimate, which 4B-4E.7 don't touch. Pushing the $2/3$ exponent requires new exponential-sum machinery, not new trig polynomials.

## 1. The Vinogradov-Korobov result (1958)

**Statement (Korobov 1958, Vinogradov 1958, independent).** There exists an effective constant $c > 0$ such that $\zeta(s) \neq 0$ in the region

$$\sigma \geq 1 - \frac{c}{(\log|t|)^{2/3}\, (\log\log|t|)^{1/3}}, \qquad |t| \geq 3.$$

**Best current constant.** Mossinghoff-Trudgian (2015) and follow-ups give explicit values of $c$, typically $c \approx 0.05$ in the standard normalization. The constant has been gradually refined over decades but the exponent $2/3$ has not moved.

**The picture in context.** Compare three landmarks:

| Result | Year | Region | Exponent on $\log|t|$ |
|---|---|---|---|
| Hadamard / de la Vallée Poussin | 1896 | $\sigma > 1$ | (boundary only) |
| de la Vallée Poussin | 1899 | $\sigma \geq 1 - c/\log|t|$ | $1$ |
| Littlewood | 1922 | $\sigma \geq 1 - c \log\log|t|/\log|t|$ | $1$ (with extra $\log\log$) |
| **Vinogradov-Korobov** | **1958** | $\sigma \geq 1 - c / (\log|t|)^{2/3}(\log\log|t|)^{1/3}$ | $\mathbf{2/3}$ |
| RH | (any) | $\sigma \geq 1/2$ | $\infty$ (no decay) |

The V-K improvement from exponent $1$ to exponent $2/3$ was the last qualitative shift. Subsequent work (Heath-Brown 1992, Ford 2002, others) has refined constants and lower-order terms but not the leading exponent.

**What "$2/3$" means concretely.** At height $|t| = 10^{12}$ (roughly the scale of the largest computed zeros), $(\log 10^{12})^{2/3} \approx (27.6)^{2/3} \approx 9.2$, giving a zero-free strip of width $\sim 0.05/9.2 \approx 5 \times 10^{-3}$. At $|t| = 10^{100}$, width is $\sim 4 \times 10^{-4}$. RH would give width $1/2$, three to four orders of magnitude more.

## 2. The method: classical zero-free region via explicit formula

All zero-free regions of this style follow the same three-input recipe.

**Input 1 (Hadamard product → log derivative bound).** Write $\zeta(s) = e^{A + Bs} \prod_\rho (1 - s/\rho) e^{s/\rho} / (s - 1)$ and take logarithmic derivative:

$$-\frac{\zeta'}{\zeta}(s) = \frac{1}{s - 1} + \text{(constants)} + \sum_\rho \frac{1}{s - \rho}$$

(with appropriate convergence/regularization). The Dirichlet-series expansion gives

$$-\frac{\zeta'}{\zeta}(s) = \sum_{n \geq 1} \Lambda(n)\, n^{-s}$$

for $\sigma > 1$, with $\Lambda(n)$ the von Mangoldt function (= $\log p$ if $n = p^k$, else 0).

**Input 2 (auxiliary non-negative trigonometric polynomial).** A polynomial $P(\theta) = \sum_{k=0}^K a_k \cos(k\theta) \geq 0$ with $a_0, a_1 > 0$. The classical choice is the **de la Vallée Poussin polynomial**

$$3 + 4\cos\theta + \cos 2\theta = 2(1 + \cos\theta)^2 \geq 0,$$

with $a_0 = 3, a_1 = 4$. Combine with the log-derivative identity: for $\sigma > 1$, $t$ real, and a putative zero $\rho_0 = \beta + i t$,

$$0 \leq -\sum_{k=0}^K a_k\, \Re\!\left[\frac{\zeta'}{\zeta}(\sigma + i k t)\right] = \sum_n \frac{\Lambda(n)}{n^\sigma} \underbrace{\sum_{k=0}^K a_k \cos(k t \log n)}_{\geq 0 \text{ by trig poly}} - (\text{pole}) - (\text{zero terms}).$$

Rearranged, this gives a *bound* on how close to $\sigma = 1$ a zero can be: a zero too close to $\sigma = 1$ would make the sum too negative.

**Input 3 (exponential sum bound on $\zeta$ in the critical strip).** To make Input 2 work for $\sigma$ slightly less than 1 (not just $\sigma > 1$), we need to control $\zeta(\sigma + it)$ on a region inside the critical strip. The classical de la Vallée Poussin bound gives $|\zeta(\sigma + it)| = O(\log|t|)$ on $\sigma \geq 1 - c/\log|t|$, yielding the exponent-1 zero-free region.

To get to exponent $2/3$, one needs a much sharper bound:

$$|\zeta(\sigma + it)| \ll \exp\!\left(C (1-\sigma)^{3/2} (\log|t|) + \ldots\right) \quad \text{for } \sigma \text{ slightly} < 1.$$

This is the **Vinogradov-Korobov bound on $\zeta$ in the critical strip**, and it is the bottleneck. The bound itself rests on Vinogradov's mean value theorem for exponential sums, a deep result about

$$\sum_{n \leq N} e^{2\pi i (a_1 n + a_2 n^2 + \ldots + a_k n^k)}.$$

The $2/3$ exponent in the final zero-free region traces directly back to the $k$-th moment exponent in Vinogradov's mean value theorem.

**The composition.** The three inputs combine as: trig polynomial gives a linear-functional positivity statement; explicit formula converts the linear functional to a sum over primes (controllable by PNT-style estimates) plus a sum over zeros (the unknown to bound) plus a contribution from $\zeta$ on the critical-strip edge (the V-K bound). Working through the algebra, the size of the zero-free region is **proportional to the strength of the Input-3 bound**.

## 3. Where the $2/3$ exponent appears

The exponent $2/3$ is not a property of the trig polynomial (4B), nor of the explicit formula (which is just an identity). It is a property of **Vinogradov's mean value theorem**:

$$J_{s,k}(N) := \int_{[0,1]^k}\left|\sum_{n \leq N} e^{2\pi i (\alpha_1 n + \ldots + \alpha_k n^k)}\right|^{2s} d\alpha_1 \cdots d\alpha_k.$$

**The Main Conjecture for V-MVT** (resolved by Bourgain-Demeter-Guth 2016 via decoupling): for $s \geq k(k+1)/2$,

$$J_{s,k}(N) \ll_\epsilon N^{2s - k(k+1)/2 + \epsilon}.$$

This Main Conjecture is what Vinogradov needed at the time but only obtained partially (using his own mean value theorem with weaker exponents). Korobov, working simultaneously, sharpened the application slightly. Bourgain-Demeter-Guth (2016) gave the optimal V-MVT bound, which sharpened the constants in V-K but **did not improve the exponent** $2/3 \to$ smaller.

**Why the exponent is $2/3$ specifically.** Schematically: bound $|\zeta(\sigma + it)|$ via $\sum_{n \leq T} n^{-\sigma - it}$ truncated near $n \sim T$; this becomes an exponential sum $\sum_n n^{-\sigma} e^{-it \log n}$; partition into $n \sim N$ blocks and use V-MVT on each block; the optimal degree of polynomial approximation (deciding $k$ in V-MVT) trades off against the per-block size, and optimization gives $k \sim (\log T)^{1/3}$, yielding the final exponent

$$\text{exponent on } 1 - \sigma = \frac{2}{3}, \quad \text{multiplicative } \log\log\text{-loss exponent} = \frac{1}{3}.$$

This is sharp: any improvement requires either (a) breaking the V-MVT main conjecture (impossible, it's sharp), or (b) using a different method entirely (not an exponential-sum optimization).

## 4. Why the $2/3$ exponent has been saturated for 67 years

The standard recipe (Inputs 1+2+3) has the V-MVT bound at its analytic heart, and V-MVT has been pushed to its sharp form. So the exponent on $\log|t|$ in the zero-free region cannot be improved within the recipe. Improving the exponent requires changing the recipe.

**Three structural barriers**:

**(i) The auxiliary inequality input is saturated.** The 4B experiment confirms numerically what Fejér proved analytically: the LP for $\max c_1 / c_0$ over non-negative trig polynomials of degree $\leq N$ saturates at $\cos(\pi/(N+2))$, asymptoting to 1. The classical $3 + 4\cos\theta + \cos 2\theta$ is sub-optimal already at degree 2 (4B finding); the Mossinghoff-Trudgian (2015) work uses degree 23 to extract every available factor. There is no further room here. **The auxiliary inequality cannot push the exponent.**

**(ii) The multivariate auxiliary inequality input also can't escape.** Experiments 4D / 4D.2 / 4E / 4E.2 / 4E.3 / 4E.4 / 4E.5 / 4E.6 / 4E.7 explored every natural extension to multivariate trig polynomials (single-coefficient, balanced-diagonal-sum, constrained-domain, multi-zero coupling, dimensions $d = 2, 3, 4$). The verdict (4E.3 structural lemma): any $d$-variate non-negative polynomial restricted to a line through the origin is a 1D non-negative polynomial bounded by 1D Fejér at matched effective degree. The multi-zero LP (4E.7) gives a real shape-factor improvement at finite height but is bounded by Riemann-von Mangoldt density for asymptotic RH on zeta. **The multivariate route does not push the exponent either.**

**(iii) The exponential sum bound is sharp under V-MVT main conjecture.** As noted in §3 above, the $2/3$ exponent comes directly from V-MVT, which is now optimal. Pushing the exponent requires a fundamentally different approach to bounding $\zeta(\sigma + it)$ in the critical strip, for instance a deep arithmetic-geometry input (à la Deligne's solution of the Weil conjectures, which in turn was a deep exponential sum estimate over finite fields).

**The synthesis.** All three inputs are individually near-optimal within their current frameworks. Improving the V-K exponent requires either (a) a fundamentally new input class (e.g., the Connes / Deninger trace formula in Architecture 2, providing exponential sums of a new kind), or (b) bypassing the explicit-formula recipe entirely (e.g., the spectral approach in Architecture 1, producing zero locations directly from operator theory). Neither has materialized.

## 5. The conditional improvement landscape

Several conditional improvements to V-K exist, each assuming an open conjecture. They form a useful taxonomy of "what would push the exponent if we had it." Each line represents an open conjecture; below it is what the conjecture would buy.

### 5.1 Riemann Hypothesis itself

The strongest assumption. Under RH, the V-K-style zero-free region is irrelevant: every zero is on $\sigma = 1/2$, so the entire critical strip $1/2 < \sigma < 1$ is zero-free. The "width" of the zero-free region is exactly $1/2$ regardless of $|t|$.

### 5.2 Density hypothesis (Lindelöf-type)

Let $N(\sigma, T)$ be the number of zeros of $\zeta$ with real part $\geq \sigma$ and imaginary part in $[0, T]$. The **density hypothesis** is

$$N(\sigma, T) \ll T^{2(1-\sigma) + \epsilon} \quad \text{for all } \sigma \geq 1/2.$$

Currently known: $N(\sigma, T) \ll T^{12(1-\sigma)/5 + \epsilon}$ (Huxley, refined by Heath-Brown). The exponent $12/5$ is the Bourgain-Heath-Brown range; reaching $2$ (= density hypothesis) is open.

**What density hypothesis would buy**: a Vinogradov-Korobov-style zero-free region with *exponent unchanged at $2/3$* but with smaller multiplicative constants. So density hypothesis is a sharpening within the V-K family, not a qualitative escape from $2/3$.

### 5.3 Lindelöf Hypothesis (LH)

LH is $|\zeta(1/2 + it)| \ll |t|^\epsilon$ for all $\epsilon > 0$. Under LH, the V-K input-3 bound on $\zeta$ in the critical strip becomes very sharp, and the zero-free region improves to:

$$\sigma \geq 1 - \frac{c}{\log|t|} \quad \text{(under LH, exponent jumps from $2/3$ back to $1$)}.$$

Note that this is *worse* than the unconditional V-K exponent on $\log|t|$. The explanation: LH is asymptotic in $|t|$ but doesn't directly control $\zeta$ for $\sigma$ near 1 in a way that improves V-K. The V-K exponent $2/3$ comes from a finer balance than LH provides.

In fact, LH is a statement about $\zeta$ on the critical line, while zero-free-region exponents need control of $\zeta$ near $\sigma = 1$. The two are not directly comparable. **LH does not directly improve the V-K exponent.** What LH gives is control of zero density and zero distribution, sharpening Input-3 bounds in specific contexts but not the leading exponent.

### 5.4 Heath-Brown conditional improvements

Heath-Brown (1992) "Zero-free regions of Dirichlet L-functions" obtained improvements conditional on **the absence of Siegel zeros** for Dirichlet $L$-functions. The improvement is for $L(s, \chi)$ rather than $\zeta(s)$ directly, but the technique transfers.

**The result**: assuming no Siegel zero for any real character of modulus $\leq q$, one gets a zero-free region for $L(s, \chi)$ with $q$-independent exponent slightly better than V-K. The improvement is in the *uniformity in $q$*, not in the leading $\log|t|$ exponent.

**Project relevance**: the Heath-Brown framework underlies the multi-zero MT inequalities tested in 4E.7. The multi-zero LP gives a real shape-factor gain at finite height (4E.7 Finding 1, $\lambda_{1,1} > \lambda_1^2$). Under "no Siegel zero" the gain transfers to a zero-free region constant; for $\zeta$ specifically, Riemann-von Mangoldt density limits this to constant-factor improvements at finite height, not asymptotic exponent improvements.

### 5.5 Pintz conditional improvements

Pintz (1976, 2017) obtained zero-free regions conditional on bounds for $L(s, \chi)$ at specific points. The conditional improvements push the exponent of $\log|t|$ closer to 1 from above for *specific* $|t|$ ranges, but don't break the $2/3$ exponent in general.

**Pintz's "Siegel zero implies zero-free region for $\zeta$" theorem**: a remarkable result. If $L(s, \chi)$ has a Siegel zero (which is widely believed not to exist), then $\zeta(s)$ has a zero-free region BETTER than V-K: the existence of an unwanted object for one $L$-function would force good behavior for another. **The result is a partial trade-off**: we don't know whether Siegel zeros exist, but we know that if they do, $\zeta$ becomes easier. This is a Deuring-type result.

### 5.6 Ford conditional improvements

Ford (2002) sharpened the multiplicative constants in V-K and gave explicit numerical values. The work is on explicit constants in the $2/3$-exponent framework, not on the exponent itself.

### 5.7 Bourgain-Demeter-Guth (BDG, 2016)

BDG resolved the Main Conjecture in Vinogradov's mean value theorem via $\ell^2$-decoupling. This sharpened the multiplicative constants in V-K (since the V-MVT input is now optimal) but **did not change the exponent**. As noted in §3, the $2/3$ exponent comes from the optimization combining V-MVT with the explicit formula; once V-MVT is at its sharp form, this optimization gives $2/3$ as a true ceiling.

### 5.8 The Bombieri-Vinogradov / GRH-on-average direction

"On average over moduli $q$" results (Bombieri-Vinogradov, Elliott-Halberstam, Friedlander-Iwaniec) give analogs of GRH for many primes simultaneously. These are non-trivial inputs for arithmetic applications (Goldbach, primes in AP) but do not directly improve the zero-free region for individual $\zeta$ or $L(s, \chi)$.

### 5.9 Summary table

| Conditional input | What it would buy for the V-K zero-free region |
|---|---|
| RH | $\zeta \neq 0$ for $\sigma > 1/2$ (trivially) |
| Density hypothesis ($N(\sigma, T) \ll T^{2(1-\sigma)}$) | Sharper constants in V-K, same exponent $2/3$ |
| Lindelöf hypothesis | Sharper control of $\zeta$ on critical line; does not change V-K exponent directly |
| No Siegel zero (uniform in $q$) | Heath-Brown improvement: $q$-uniform, not exponent-improving |
| BDG / V-MVT main conjecture (done 2016) | Sharper multiplicative constants in V-K, same exponent $2/3$ |
| Pintz-style "Siegel ⇒ ZFR" | Conditional on existence of Siegel zero (likely false) |
| Connes / Deninger trace formula | Would give new input class (speculative) |

**The cluster reveals the structure**: every named conditional improvement either (a) sharpens constants within the V-K framework, (b) gives uniformity in arithmetic parameters $q$, or (c) is a Deuring-type "if-then" with a hypothetical hypothesis. **None of the listed conditionals would push the exponent from $2/3$ down**.

## 6. Connection to the project's experimental thread

The 4B-4E.7 experiments explore exactly **Input 2** (the auxiliary inequality) and its multivariate generalizations. The findings can be retold in V-K terms:

| Experiment | What it tested | What it found | Effect on the V-K exponent |
|---|---|---|---|
| 4B | 1D non-neg trig polys: $\max c_1$ at degree $N$ | LP saturates Fejér $\cos(\pi/(N+2))$ exactly | Sub-optimal classical poly: $3 + 4\cos + \cos 2$ is beaten by Fejér optimum at degree 2 by $\sim$6%. Improves constants, not exponent. |
| 4D, 4D.2 | $d$-variate, max single coefficient $c_{1,\ldots,1}$ | LP decomposes to tensor of 1D Fejér optima | No new inequality; no effect on exponent. |
| 4E, 4E.2 | $d$-variate, balanced diagonal sum $c_{1,1} + \alpha c_{2,2}$ | LP gap to tensor bound +25% at $\alpha = 3, N = 2$ | Real new 2D inequality at C-S level. |
| 4E.3 | Translation of 4E.2 gap to MT zero-free region | **Does not translate**: structural lemma proves 1D restriction of any 2D non-neg poly bounded by 1D Fejér | No effect on V-K exponent. |
| 4E.4, 4E.5 | Higher-$d$ gap pattern | Gap grows sub-linearly ($+25\%, +51\%, +62\%$ at $d = 2, 3, 4$) | Same structural lemma applies; no effect on exponent. |
| 4E.6 | Constrained-domain LP escape from 4E.3 | Collapses to Fejér ceiling | No effect on exponent. |
| 4E.7 | Multi-zero LP escape from 4E.3 | Real shape-factor gain $\lambda_{1,1} > \lambda_1^2$ (55-137×) but rank-1 LP at naive objectives | At asymptotic infinity, bounded by Riemann-von Mangoldt density (consecutive zeros at spacing $\sim 2\pi/\log T$); no asymptotic exponent improvement. Constant-factor improvements possible for finite-range arithmetic problems. |

**The lesson**: the 4B-4E.7 thread thoroughly explored what Input 2 can give and confirmed it cannot push the V-K exponent. The structural reason (best summarized in 4E.3) is that the explicit-formula machinery extracts a 1D linear functional from any multivariate polynomial, and the strength of the 1D linear functional is bounded by the 1D Fejér optimum. **No amount of cleverness in the auxiliary inequality can compensate for the V-K bottleneck in Input 3**.

**Implication for further Arch 4 experimental work**. The natural-LP / auxiliary-inequality direction is closed. The remaining computational frontier:

- **4E.8** (open): polynomial-ideal SOS via Putinar/Schmüdgen Positivstellensatz. Different machinery (SDP, not LP), could give structurally different bounds. **This is the only remaining LP-style escape route from 4E.3** per the LEARNINGS finding-12 taxonomy.
- **Direct exponential-sum experiments**. Numerical evidence on $\sum_{n \leq N} n^{-it}$ at large $N$ and $t$: where does V-K beat the trivial $O(N^{1-\sigma})$ bound? Could a numerical sweep reveal regimes where current bounds are demonstrably loose?
- **Density-hypothesis numerics**. Test $N(\sigma, T) \ll T^{2(1-\sigma)}$ numerically by counting zeros at progressively higher $T$; check whether the empirical exponent matches the density hypothesis or the (currently best) $12/5$.

None of these would close RH, but they would map the architecture more thoroughly.

## 7. Where this leaves Architecture 4

**The architecture's structural ceiling**: the classical analytic route, using non-negative trig polynomials + explicit formula + exponential sum bounds, cannot reach RH because:

- The auxiliary inequality input has been saturated (4B's Fejér ceiling, confirmed numerically by the LP solver).
- The multivariate generalization cannot escape via line-restriction (4E.3 structural lemma, robust under naïve domain relaxation by 4E.6 and naïve multi-zero coupling by 4E.7).
- The exponential sum input is at the V-MVT main conjecture (done 2016 by BDG); no further improvement possible within the V-MVT framework.

**What would change the picture**:

1. A fundamentally new exponential sum bound (e.g., from arithmetic geometry á la Weil/Deligne, applied to $\zeta(s)$ rather than $L$-functions over finite fields). This is essentially what the **Architecture 2** (arithmetic-geometric) route would deliver if it produced a Lefschetz-style spectral identification.

2. A direct positivity certificate that bypasses the explicit formula (Architecture 3 direction). Would require Weil positivity to be provable without RH-strength input, the analytic obstruction documented in Arch 3F-3I.

3. A spectral identification on the operator side (Architecture 1 direction). Would produce zero locations directly, making the V-K route obsolete. Connes' adèle class space is the natural target ([1D dossier](../spectral/1d_connes_adele_literature.md)).

**The verdict**: Architecture 4 is a *constraint mapping* architecture. The 4B-4E.7 thread quantifies what the architecture cannot do; it does not provide a route to RH on its own. Other architectures (2 arithmetic-geometric, 3 positivity) must provide the structural input that breaks the V-K bottleneck. **Architecture 4 is the "tightest current unconditional bound" architecture, not the "proof of RH" architecture**, and the 67-year stagnation is consistent with this structural reading.

**This is the same diagnosis as the** [marginal-positivity thesis](../../README.md) (memory cross-cut): RH is "just barely true" in five distinct senses, including the V-K ceiling being just barely loose enough to allow off-line zeros. The classical analytic route gives the tightest currently-provable wall, and the gap from this wall to RH is structural rather than incidental.

## 8. References

- Vinogradov, I. M. (1958). "A new estimate of the function $\zeta(1 + it)$." *Izv. Akad. Nauk SSSR* 22.
- Korobov, N. M. (1958). "Estimates of trigonometric sums and their applications." *Uspekhi Mat. Nauk* 13.
- Heath-Brown, D. R. (1992). "Zero-free regions of Dirichlet $L$-functions." *Proc. London Math. Soc.* 64.
- Ford, K. (2002). "Vinogradov's integral and bounds for the Riemann zeta-function." *Proc. London Math. Soc.* 85.
- Mossinghoff, M. J. and Trudgian, T. S. (2015). "Nonnegative trigonometric polynomials and a zero-free region for the Riemann zeta-function." *J. Number Theory* 157. (The current state-of-the-art constant.)
- Bourgain, J., Demeter, C., and Guth, L. (2016). "Proof of the main conjecture in Vinogradov's mean value theorem for degrees higher than three." *Ann. Math.* 184.
- Pintz, J. (1976). "Elementary methods in the theory of $L$-functions, II. On the greatest real zero of a real $L$-function." *Acta Arith.* 31.
- Pintz, J. (2017). "Cramér vs. Cramér. On Cramér's probabilistic model for primes." *Funct. Approx.* 37.
- Titchmarsh, E. C. *The Theory of the Riemann Zeta-Function*, 2nd ed., revised by D. R. Heath-Brown. Oxford, 1986. (Standard reference for the classical analytic route; chapters V-VI cover zero-free regions.)
- Iwaniec, H. and Kowalski, E. *Analytic Number Theory*. AMS Colloquium Publications 53. (Chapter 5 on exponential sums; chapter 8 on zero-free regions.)
