# 2FF: the two-clock interpolating period, quantitative (organ (b) of M4)

> Companion for [`e2ff_two_clock_period.py`](e2ff_two_clock_period.py). Attacks organ (b) of milestone M4, named by probe B (2EE / #44): the single interpolating period reconciling the additive archimedean clock with the multiplicative prime clock. Run: `python -m experiments.arithmetic_geometric.e2ff_two_clock_period`.

## The question

Probe B left M4 needing two organs: (a) a fundamental class $H^2$, and (b) a single period gluing the archimedean clock (additive, the $\Gamma$-factor) to the finite clock (multiplicative, the $(1,p)$ bidegree). Candidate B's intuition was a single transcendental "global $q$". This experiment asks, honestly: **can a single number play that role?** It cannot construct the period (that would be a chunk of RH); it determines whether a single number is even the right *kind* of object, and names the replacement if not.

## What was computed

### Function-field anchor (a single clock exists)

Over $\mathbb{F}_q$, $\zeta_C(s)$ is a rational function of $q^{-s}$, hence periodic in $\mathrm{Im}(s)$ with period $2\pi/\log q$; the zeros lie on a vertical lattice of that spacing, and the Frobenius closed-orbit lengths are $\{k\log q\}$, all multiples of the one period $\log q$. **Verified:** the period-defect $D(L) = \mathrm{mean}_i\,\mathrm{dist}(\ell_i/L, \mathbb{Z}_{\geq 1})^2$ of the $\mathbb{F}_5$ orbits hits its minimum $2.2\times 10^{-5}$ (essentially zero) at $L = 1.609 = \log 5$. Additive and multiplicative scales are locked by one number.

### (1) Incommensurability: no single multiplicative period over Spec(Z)

The arithmetic closed-orbit lengths are $\{\log p\}$ (2R/#26), and they are rationally independent ($\log p_i/\log p_j$ irrational, since distinct primes share no common power). **Verified:** the prime period-defect stays at $0.055$ across the entire valid range $L \le \min_p \log p = \log 2$, bounded away from zero by a factor $\sim 2500$ relative to the $\mathbb{F}_q$ case. The simplest explicit obstruction: $\log 3/\log 2 = 1.58496\ldots$ is irrational, so no $L$ makes both $\log 2$ and $\log 3$ integer multiples. **There is no single multiplicative period.**

*(Metric note: the naive $(\ell/L \bmod 1)$ defect vanishes spuriously as $L\to\infty$, where every length rounds to the 0th multiple. The fix used here forbids the 0th multiple and restricts to the genuine range $L \le \min(\ell)$, so the reported defect is a real obstruction, not a grid artifact.)*

### (2) The running archimedean clock

The $\zeta$ zeros are not on a lattice: their mean spacing near height $T$ is $2\pi/\log(T/2\pi)$ (Riemann-von Mangoldt). Define the effective clock $\log q_{\mathrm{eff}}(T) := 2\pi/(\text{mean spacing}) = \log(T/2\pi)$. **Verified** against 79 actual $\zeta$ zeros up to $T=200$: the smoothed measured clock tracks $\log(T/2\pi)$ (mean relative error $0.15$, the residual being the strong per-gap GUE fluctuations around the mean density), running from $\approx 1.03$ at $T\approx 18$ to $\approx 3.45$ at $T\approx 197$. For $\mathbb{F}_q$ this clock is the constant $\log q$; for $\zeta$ it runs, and its running rate is set by the archimedean $\Gamma$-factor (the density formula is the archimedean argument).

## Conclusion on organ (b)

The interpolating "period" is **not a single transcendental number**. Over $\mathbb{F}_q$ one number $\log q$ locks the two clocks (commensurable orbits, a zero lattice). Over $\mathrm{Spec}(\mathbb{Z})$: (1) the prime orbit lengths $\{\log p\}$ are rationally independent (no common period), and (2) the archimedean clock runs as $\log(T/2\pi)$. So organ (b) must be the **scaling flow $\mathbb{R}_+$** (Deninger's $\mathbb{R}$-flow, not a $\mathbb{Z}$-action) with the incommensurable spectrum $\{\log p\}$, and **the obstruction to collapsing it to one number is exactly the transcendence / rational-independence of $\{\log p\}$** — which links organ (b) directly to candidate F (the transcendence shadow) of the brainstorm. The universal transcendental constant that *does* survive is $2\pi$ (the Mellin-Fourier period relating $s$ to $q^{-s} = e^{-s\log q}$); what dissolves into the flow is the clock $\log q$.

**The $q\to 1$ picture.** As $q\to 1^+$ the FF period $2\pi/\log q \to \infty$: the zero lattice spacing diverges and the discrete lattice opens into the continuum. $\zeta$ is the "$q=1$" limit (Connes-Consani scaling site, Deninger flow), with a height-running effective clock instead of a fixed one.

**K2.** Davenport-Heilbronn has no Euler product, hence no closed-orbit spectrum $\{\log p\}$ (2R/#26: $\Lambda_{\mathrm{DH}}$ delocalizes off prime powers), hence no scaling flow and no clock. The two-clock object does not even form for the counterexample, the clean C2 face of organ (b).

## Why this is a coordinate

It converts organ (b) from "find a transcendental period" into a sharper, truer target: **build the scaling flow $\mathbb{R}_+$ with orbit spectrum $\{\log p\}$ and prove the additive (archimedean, running) and multiplicative (prime, incommensurable) clocks balance at every height** (RH). It also reveals organ (b) and candidate F are the same problem from two sides: the period cannot be a number *because* $\{\log p\}$ is transcendentally independent, so the geometric gluing (b) and the transcendence statement (F) are dual descriptions of the one missing input. This is a genuine bridge between two of the brainstorm's six candidates.

## Honest scope

The FF lattice period, the incommensurability of $\{\log p\}$, and the running density $\log(T/2\pi)$ are all known/rigorous facts. This experiment makes the two-clock structure quantitative and draws the structural conclusion (period = flow, obstruction = incommensurability). It constructs no arithmetic cohomology and proves nothing about RH. No new theorem; a sharpening coordinate that fixes the *kind* of object organ (b) must be and bridges it to candidate F.

## Pointers

- Parent: [`docs/03_research/backwards_from_2050.md`](../../docs/03_research/backwards_from_2050.md) (organ (b); candidate F, the transcendence shadow).
- Builds on: [`e2ee_archimedean_gluing.py`](e2ee_archimedean_gluing.py) (2EE / #44, named the two organs), [`e2r_dynamical_zeta.md`](e2r_dynamical_zeta.md) (2R / #26, the orbit spectrum $\{\log p\}$).
- Findings leaned on: #23 (two-clock balance), #25 (the $(1,p)$ bidegree), #26 (von Mangoldt orbit lengths).
