# Quantum chaos and the Riemann zeros: the spectral stage, not the polarization

> **Status: expository synthesis for Architecture 1 (spectral / Hilbert-Pólya).** Written 2026-06-30 as the graduate-level bridge between classical chaos, quantum chaos, and the project's spectral thread.
>
> **Headline.** The Riemann zeros behave, statistically, exactly like the energy levels of a quantized classically chaotic system with broken time-reversal symmetry (GUE). The Berry-Keating dictionary makes this concrete: the Gutzwiller trace formula and the Riemann-Weil explicit formula are the same equation read twice, with **primes as the primitive periodic orbits** and $\log p$ as their periods. This is the strongest heuristic argument for a self-adjoint operator behind the zeros. It is also, by the project's own discipline, a **Level-3** fact: it supplies the spectral stage on which RH would be proved, but it cannot separate $\zeta$ from Davenport-Heilbronn, and so it cannot close RH. The missing ingredient is a genuine positivity (the polarization, the M4 object), restated here in spectral language.

## 0. Where this sits

This is the quantum-chaos face of the same object the rest of the project chases from the arithmetic-geometry side. The spine documents ([`all_roads_to_the_signature.md`](all_roads_to_the_signature.md), [`research_directions/08A_rosati_standard_conjecture.md`](research_directions/08A_rosati_standard_conjecture.md)) argue that every direction converges on one positivity. This document explains why the **spectral** direction, which historically looked like the most direct route (find the operator, diagonalize it, done), lands on the same wall. The four-level framing of [`../02_graduate/log_correlated_fields_intro.md`](../02_graduate/log_correlated_fields_intro.md) §6 is used throughout: statistics of the zeros live at Level 3, RH lives at Level 4.

## 1. Quantum chaos: the Bohigas-Giannoni-Schmit conjecture

Take a classical Hamiltonian system and quantize it. The eigenvalues $E_1 \le E_2 \le \dots$ of the quantum Hamiltonian form a spectrum, and after unfolding (rescaling so the mean level spacing is $1$) one asks about the statistics of the gaps and correlations. The **Bohigas-Giannoni-Schmit (BGS) conjecture** (1984) is the organizing empirical law of quantum chaos:

- If the classical dynamics is **integrable** (as many conserved quantities as degrees of freedom, motion on invariant tori), the unfolded levels are **uncorrelated**: they follow **Poisson** statistics. Levels do not repel; small gaps are common; you can find near-degeneracies freely.
- If the classical dynamics is **chaotic** (positive Lyapunov exponents, ergodic on the energy shell), the unfolded levels follow **random-matrix theory (RMT)**. Which ensemble depends on symmetry:
  - time-reversal symmetry present: **GOE** (Gaussian Orthogonal Ensemble), level-repulsion exponent $\beta = 1$,
  - time-reversal symmetry broken: **GUE** (Gaussian Unitary Ensemble), level-repulsion exponent $\beta = 2$,
  - with spin and time reversal: **GSE**, $\beta = 4$.

The physical fingerprint is **level repulsion**. In a chaotic spectrum the probability of a gap $s$ vanishes as $s^\beta$ for small $s$: the levels avoid each other. In an integrable spectrum the gap distribution is $e^{-s}$, peaked at zero: the levels ignore each other. Repulsion is the spectral shadow of the classical instability. Chaotic orbits are exponentially sensitive, the corresponding eigenstates are spread and generic, and generic Hermitian matrices repel their eigenvalues.

The relevant statistic for us is the **pair correlation** $R_2(u)$, the density of pairs of levels at unfolded separation $u$. For the GUE,
$$R_2(u) = 1 - \left(\frac{\sin \pi u}{\pi u}\right)^2 .$$
The dip near $u = 0$ (it vanishes quadratically, $R_2(u) \sim \tfrac{\pi^2}{3} u^2$) is the analytic statement of level repulsion for broken time-reversal symmetry.

## 2. The zeros match GUE: Montgomery and Odlyzko

Write the nontrivial zeros as $\rho = \tfrac12 + i\gamma$ (assuming RH for the statement, though the pair-correlation work does not need it). Unfold the ordinates by the local density
$$\tilde\gamma = \frac{\gamma}{2\pi}\log\frac{\gamma}{2\pi},$$
which uses the Riemann-von Mangoldt count $N(T) \sim \tfrac{T}{2\pi}\log\tfrac{T}{2\pi} - \tfrac{T}{2\pi}$. Montgomery (1973) computed the pair correlation of the unfolded zeros and found, for test functions with Fourier support in $(-1,1)$,
$$R_2^{\zeta}(u) = 1 - \left(\frac{\sin \pi u}{\pi u}\right)^2 .$$
This is **identical to the GUE pair correlation**. The zeros repel exactly like the levels of a quantized chaotic system with broken time-reversal symmetry. Dyson recognized the form on sight in the famous tea-time conversation with Montgomery.

Odlyzko's high-precision computations (the "Odlyzko-Schönhage" era, zeros near height $10^{20}$ and beyond) confirmed not just the pair correlation but the full suite of GUE statistics: nearest-neighbor spacings, higher correlations, the number variance. The agreement is among the most precise unproven correspondences in mathematics. Rudnick and Sarnak later extended the pair-correlation agreement to the $n$-level correlations of a broad class of $L$-functions (again within restricted support), so this is a property of the family, not an accident of $\zeta$.

The reading is unavoidable: **the zeros look like a spectrum, and specifically like a chaotic quantum spectrum.**

## 3. Hilbert-Pólya, and its chaos interpretation

The **Hilbert-Pólya conjecture** is the oldest form of the spectral idea: the ordinates $\gamma$ are the eigenvalues of a self-adjoint operator $\hat H$ on some Hilbert space,
$$\hat H \,\psi_n = \gamma_n \,\psi_n , \qquad \hat H = \hat H^\dagger .$$
If such an $\hat H$ exists, its eigenvalues are real, so every $\gamma$ is real, so every zero has $\mathrm{Re}\,\rho = \tfrac12$: RH follows immediately. Self-adjointness **is** RH in this language.

Quantum chaos sharpens the conjecture. If $\hat H$ exists and its spectrum has GUE statistics, then by the BGS heuristic $\hat H$ should be the **quantization of a classical Hamiltonian whose flow is chaotic**, and the broken-time-reversal-symmetry (GUE, not GOE) tells us the classical system has no time-reversal symmetry. So the search for Hilbert-Pólya becomes the search for a specific classical chaotic dynamical system whose quantization has the zeros as its energy levels. This is where Berry-Keating enters.

## 4. Berry-Keating: the classical Hamiltonian $H = xp$

Berry and Keating (1999) proposed that the relevant classical Hamiltonian is the dilation generator
$$H = x\,p ,$$
the product of position and momentum on the phase-plane $(x,p)$. The motivation is direct. The smooth (Weyl) counting of quantum states below energy $E$ for a Hamiltonian $H(x,p)$ is the phase-space area $\{H(x,p) \le E\}/(2\pi\hbar)$. For $H = xp$ the level sets are hyperbolas $xp = E$, and regularizing the area (cut off at $x \ge l_x$, $p \ge l_p$ with $l_x l_p = 2\pi\hbar$) gives a counting function
$$N_{\text{smooth}}(E) = \frac{E}{2\pi}\log\frac{E}{2\pi} - \frac{E}{2\pi} + \dots ,$$
which is **exactly the Riemann-von Mangoldt smooth term** $N(T)$ with $E \leftrightarrow T$. The Hamiltonian $H = xp$ reproduces the average density of the zeros from pure semiclassics. That is a strong hint that $xp$, suitably regularized and confined, is the classical skeleton behind the zeros.

Two features make $xp$ both attractive and hard:

- **It is not bounded below.** The classical orbits $x(t) = x_0 e^{t}$, $p(t) = p_0 e^{-t}$ are hyperbolic: they stretch in $x$ and contract in $p$ with rate $1$. This is the signature of an **unstable (chaotic) fixed point**: the flow near $xp = 0$ has a positive Lyapunov exponent. The unboundedness is exactly why the spectrum can be a dense set of real numbers rather than a bounded or discrete-from-below tower. It is also why making $\hat H = \tfrac12(xp + px)$ genuinely self-adjoint (choosing a domain, a boundary condition, a confinement) is subtle: the naive operator is only symmetric, and different self-adjoint extensions give different spectra.
- **It requires a confinement / boundary.** Berry-Keating and, from a different direction, Connes (1999) supply the missing structure by hand. Connes' trace formula realizes the zeros as an **absorption spectrum** (missing lines in a continuum) via an action of the idele class group on a space of adeles, with the primes entering through the local factors at each place. Sierra and Townsend, and others, have built explicit $xp$-type models (the "$H = x(p + \ell^2/p)$" Sierra Hamiltonian, Landau-model realizations) that put a genuine self-adjoint operator on the table and get the smooth counting right.

The project's spectral experiments live exactly here: [`../../experiments/spectral/`](../../experiments/spectral/) contains the Berry-Keating ($xp$) and Sierra-Townsend probes, and the 1D Connes adele literature review. The consistent finding there is the same as the one this document is building toward: these models reproduce the **average** density and the **statistics**, but none of them supplies the arithmetic input that would force the eigenvalues to be real. They match Level 3 and stop.

## 5. The central dictionary: Gutzwiller = Riemann-Weil

Here is the mechanism that makes the primes-as-orbits picture more than an analogy. Both quantum chaos and analytic number theory have a **trace formula** that expresses a spectral density as a smooth part plus an oscillating sum, and the two formulas have the same shape.

### 5a. The Gutzwiller trace formula

For a quantized chaotic Hamiltonian, Gutzwiller's semiclassical trace formula expresses the density of states $d(E) = \sum_n \delta(E - E_n)$ as
$$d(E) \;=\; \bar d(E) \;+\; \frac{1}{\pi\hbar}\sum_{p}\sum_{k=1}^{\infty} \frac{T_p}{\sqrt{\left|\det\!\left(M_p^{\,k} - I\right)\right|}}\,\cos\!\left(\frac{k\,S_p(E)}{\hbar} - \frac{k\,\mu_p\,\pi}{2}\right).$$
Reading the pieces:

- $\bar d(E)$ is the smooth **Weyl term**, the average density from phase-space volume (this is the $H = xp$ counting of §4).
- The double sum runs over **primitive periodic orbits** $p$ of the classical flow and their **repetitions** $k = 1, 2, 3, \dots$ (going around orbit $p$ a total of $k$ times).
- $T_p$ is the **period** of the primitive orbit and $S_p(E)$ its **action**.
- $M_p$ is the **monodromy (stability) matrix** of the orbit. For an unstable (chaotic) orbit with Lyapunov exponent $\lambda_p$, $\left|\det(M_p^k - I)\right| \approx e^{k\lambda_p T_p}$ for large $k$, so the amplitude decays like $e^{-k \lambda_p T_p / 2}$. **The instability of the orbit is the size of its contribution.**
- $\mu_p$ is the **Maslov index**, a topological phase counting focal points along the orbit.

### 5b. The Riemann-Weil explicit formula

The explicit formula writes the density of zeros $\sum_\gamma \delta(t - \gamma)$ (equivalently, tests it against a smooth $h$) as a smooth archimedean term plus a sum over primes and prime powers. In the density form,
$$\sum_{\gamma}\delta(t - \gamma) \;=\; \bar d(t) \;-\; \frac{1}{2\pi}\sum_{p}\sum_{k=1}^{\infty} \frac{\log p}{p^{k/2}}\,\Big(e^{\,i k t \log p} + e^{-\,i k t \log p}\Big),$$
where $\bar d(t) = \tfrac{1}{2\pi}\log\tfrac{t}{2\pi}$ is the smooth zero density (the derivative of $N(T)$), and the prime side is the von Mangoldt weight $\Lambda(n) = \log p$ for $n = p^k$, normalized by $n^{-1/2} = p^{-k/2}$. The cosine form is $\sum_{p,k} \tfrac{\log p}{p^{k/2}}\cos(k t \log p)$, up to normalization and the archimedean pieces.

### 5c. Lining them up

Set $\hbar = 1$ and match term by term. The correspondence is forced:

| Gutzwiller (quantum chaos) | Riemann-Weil (number theory) |
|---|---|
| energy $E$ / time conjugate | height $t$ on the critical line |
| smooth Weyl term $\bar d(E)$ | smooth zero density $\tfrac{1}{2\pi}\log\tfrac{t}{2\pi}$ |
| primitive periodic orbit $p$ | prime $p$ |
| orbit period $T_p$ | $\log p$ |
| repetition $k$ (go around $k$ times) | prime power $p^k$ |
| action phase $e^{i k S_p}$ | $e^{i k t \log p} = (p^k)^{it}$ |
| stability amplitude $1/\sqrt{|\det(M_p^k - I)|} \approx e^{-k\lambda_p T_p/2}$ | $1/p^{k/2}$ |
| Maslov index $\mu_p$ | archimedean / functional-equation phase |

The reading that number theory has been telling us all along: **the primes are the primitive periodic orbits of the hypothetical dynamical system whose energy levels are the zeros.** Their periods are $\log p$. Prime powers are the repetitions of an orbit. And the amplitude $p^{-k/2}$ is the stability weight of an orbit with Lyapunov exponent $\lambda_p$ and period $T_p = \log p$ such that $e^{-\lambda_p T_p /2} = p^{-1/2}$, i.e. $\lambda_p = 1$ for every prime. Every prime orbit is unstable with the **same** Lyapunov exponent $\lambda = 1$: a uniformly hyperbolic system. The multiplicity of primes with $\log p \le X$ (there are $\sim e^X / X$ of them by the prime number theorem) matches the exponential proliferation of periodic orbits in a chaotic flow with topological entropy $1$.

### 5d. The sign problem: where the analogy breaks

The dictionary is not a proof, and the exact point where it fails is diagnostic. Gutzwiller's sum is a sum of **cosines with positive amplitudes** $1/\sqrt{|\det(M-I)|} > 0$: it comes from tracing $e^{-i\hat H t/\hbar}$ for a **self-adjoint** $\hat H$, so positivity of the amplitudes is automatic. The Riemann-Weil prime sum carries a definite **sign** (the minus sign in front of the prime sum above), and controlling that sign against the archimedean term is exactly the **Weil explicit-formula positivity**: RH is equivalent to $\sum_\rho \hat f(\rho)\overline{\hat f(\bar\rho)} \ge 0$ for all suitable $f$ (Architecture 3). A naive Gutzwiller reading gives you the oscillating sum but **not** the positivity, because there is no actual self-adjoint operator underneath yet, only a formula that has the shape of one. Producing the operator (Hilbert-Pólya) would make the positivity automatic; matching the formula does not. This is the spectral-language statement of the project's central gap: **the trace formula is the trace (Level 3); the missing thing is the polarization that makes it a spectrum of a self-adjoint operator (Level 4).** See the K1 kill-criterion ("signature not trace") throughout the research directions.

## 6. The honest caveat: this is Level 3, and it cannot see Davenport-Heilbronn

Everything above is real and is strong evidence. It is also, by the project's discipline, insufficient, and it is worth being exact about why.

**GUE statistics live at Level 3.** The four-level framing ([`../02_graduate/log_correlated_fields_intro.md`](../02_graduate/log_correlated_fields_intro.md) §6) places pair correlation, spacing distributions, and the whole RMT correspondence at Level 3 (spectral / statistical). RH is a Level-4 statement. The gap is not rhetorical. Pair correlation is an **averaged, asymptotic** statement about the bulk of the zeros. A single zero at $\beta = 0.51$, or even a positive-density-zero set of off-line zeros consistent with the known zero-density estimates, perturbs the pair correlation by an amount below what any statistical test at finite height can resolve. Matching GUE constrains where the operator would live and how its spectrum is distributed; it does not force any individual eigenvalue to be real.

**The Davenport-Heilbronn discipline makes this concrete.** The project's structural sanity check (see [`../../CLAUDE.md`](../../CLAUDE.md) and [`../../experiments/_shared/davenport_heilbronn.py`](../../experiments/_shared/davenport_heilbronn.py)) is the Davenport-Heilbronn function: it has a functional equation and a Riemann-von Mangoldt density, its zeros are known to obey the same GUE-type statistics in the bulk, and yet it has **zeros off the critical line** (the first near $\rho \approx 0.8085 + 85.699\,i$). D-H has no Euler product, hence no prime sum, hence no Gutzwiller-style periodic-orbit expansion, but it has the same spectral **statistics**. Therefore any argument that proves RH using only spectral statistics (pair correlation, level repulsion, GUE) would prove the false analogue for D-H, and is structurally wrong. Quantum chaos, taken as a statement about statistics, is D-H-blind.

This is the same wall the arithmetic-geometry directions hit, restated. The statistics are the **trace** (they see $\sum p^{-it}$-type data, which D-H shares in distribution). The thing that separates $\zeta$ from D-H is the **Euler product**, which is what the Gutzwiller dictionary uses to name the primes as orbits with a specific uniform Lyapunov exponent. The Euler product is necessary for the periodic-orbit structure to exist at all, but having the structure is not the same as proving the positivity it would imply. The closing ingredient is the Level-4 polarization: the M4 object of [`all_roads_to_the_signature.md`](all_roads_to_the_signature.md) and [`research_directions/08A_rosati_standard_conjecture.md`](research_directions/08A_rosati_standard_conjecture.md).

## 7. What would actually help

Framed positively, quantum chaos tells us precisely what is missing and hands the search a sharp target.

1. **A genuine self-adjoint operator, not matching statistics.** The prize is not another model whose spectrum has GUE statistics (we have several, and they are all Level 3). The prize is an operator $\hat H$ with a proven self-adjointness on a specified domain **whose reality of spectrum uses the Euler product**. In the Gutzwiller language: an actual quantum system, not just a formula with the shape of a trace, so that positivity of the amplitudes (hence RH) is a theorem about the operator rather than an input. Supplying that self-adjointness **is** supplying the polarization. The spectral route does not avoid the M4 object; it renames it. This is the honest content of the K1 criterion applied to Hilbert-Pólya.

2. **The archimedean place as the confinement.** The one piece of structure that the Berry-Keating $xp$ picture must add by hand (the boundary / confinement that turns the unbounded hyperbolic flow into a discrete real spectrum) is, on the arithmetic side, the **archimedean local factor** $\Gamma_\mathbb{R}(s) = \pi^{-s/2}\Gamma(s/2)$. In Connes' formula it is the place at infinity. The project's repeated finding that off-line obstructions are "archimedean-suppressed" (the stealth window of [`research_directions/12_debruijn_newman_criticality.md`](research_directions/12_debruijn_newman_criticality.md), LEARNINGS #38) says the same thing from the analytic side: the discriminating information sits at the archimedean place, exactly where the $xp$ confinement is unspecified. A correct self-adjoint extension is a correct archimedean boundary condition.

3. **The statistical-mechanics face is already in the repo.** The multifractal / log-correlated thread ([`../../experiments/multifractal/`](../../experiments/multifractal/), E0-E3) studies $\log|\zeta(\tfrac12 + it)|$ as a log-correlated Gaussian field (Fyodorov-Hiary-Keating). That is the **wave-intensity** face of the same spectrum whose **level statistics** are the GUE face here: both are Level-3 observables of the hypothetical chaotic quantum system, one describing the eigenvalue correlations, the other the eigenfunction / value-distribution fluctuations. They are consistent with each other and with GUE, and neither closes RH, for the same reason. Direction 12 ([`research_directions/12_debruijn_newman_criticality.md`](research_directions/12_debruijn_newman_criticality.md)) is the current attempt to promote this Level-3 machinery to a Level-4 criticality statement; its honest status (the flow, not the kernel, carries the RH content, and the discriminating step is unbuilt) is the same lesson as this document.

**Net.** Quantum chaos gives the most vivid and most predictive picture of the zeros available: they are the spectrum of a uniformly hyperbolic quantum system with the primes as its periodic orbits. It reproduces the smooth counting, the pair correlation, and the whole trace-formula structure. What it does not do, and provably cannot do at the level of statistics alone, is separate $\zeta$ from Davenport-Heilbronn. That negative is a coordinate: it says the operator we are looking for is not distinguished by its statistics but by its **positivity**, and it locates the missing structure at the archimedean place. The spectral route and the arithmetic-geometry route are looking for the same object from opposite sides.

## References

- Montgomery, H. L. (1973). *The pair correlation of zeros of the zeta function.* Proc. Sympos. Pure Math. 24, 181-193.
- Odlyzko, A. M. (1987, and later). *On the distribution of spacings between zeros of the zeta function.* Math. Comp. 48; and the high-height computations near $10^{20}$.
- Berry, M. V.; Keating, J. P. (1999). *H = xp and the Riemann zeros.* In Supersymmetry and Trace Formulae, ed. Lerner et al., 355-367.
- Berry, M. V.; Keating, J. P. (1999). *The Riemann zeros and eigenvalue asymptotics.* SIAM Review 41, 236-266.
- Bohigas, O.; Giannoni, M.-J.; Schmit, C. (1984). *Characterization of chaotic quantum spectra and universality of level fluctuation laws.* Phys. Rev. Lett. 52, 1-4.
- Gutzwiller, M. C. (1990). *Chaos in Classical and Quantum Mechanics.* Springer. (The trace formula and the periodic-orbit theory.)
- Connes, A. (1999). *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function.* Selecta Math. 5, 29-106.
- Rudnick, Z.; Sarnak, P. (1996). *Zeros of principal L-functions and random matrix theory.* Duke Math. J. 81, 269-322.
- Fyodorov, Y. V.; Hiary, G. A.; Keating, J. P. (2012). *Freezing transition, characteristic polynomials of random matrices, and the Riemann zeta function.* Phys. Rev. Lett. 108, 170601. arXiv:1202.4713.
- Sierra, G.; Townsend, P. K. (2008). *Landau levels and Riemann zeros.* Phys. Rev. Lett. 101, 110201.
- Project: [`all_roads_to_the_signature.md`](all_roads_to_the_signature.md), [`research_directions/08A_rosati_standard_conjecture.md`](research_directions/08A_rosati_standard_conjecture.md), [`../02_graduate/log_correlated_fields_intro.md`](../02_graduate/log_correlated_fields_intro.md) §6 (four-level framing), [`research_directions/12_debruijn_newman_criticality.md`](research_directions/12_debruijn_newman_criticality.md), [`../../experiments/spectral/`](../../experiments/spectral/), [`../../experiments/multifractal/`](../../experiments/multifractal/).
