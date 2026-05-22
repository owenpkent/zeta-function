# Architecture 1: Spectral (Hilbert-Polya)

> Per the [project plan](../PROOF_ARCHITECTURES_PLAN.md): construct an operator whose spectrum is the imaginary parts of zeta zeros. Self-adjointness then forces all zeros onto the critical line. The flagship candidate is the Berry-Keating Hamiltonian $H = (xp + px)/2$.

## 1A: Berry-Keating discretization

**Status:** complete; density-mismatch obstruction quantified.

**Method:** [e1a_berry_keating.py](e1a_berry_keating.py). In log coordinate $u = \log x$, the symmetrized Berry-Keating Hamiltonian becomes
$$H = -i\left(\partial_u + \tfrac{1}{2}\right).$$
We discretize on a uniform $u$-grid with $N$ points on $[-L/2, L/2]$, build $H$ via central finite differences, and diagonalize for three boundary conditions: Dirichlet, periodic, open.

**Findings ($N = 200$, $L = 10$):**

| BC | $\max |\Im E|$ | $\Re E$ range |
|---|---|---|
| Dirichlet | $0.500$ | $[0.16, 19.90]$ |
| Periodic | $0.500$ | $[0, 19.90]$ |
| Open | $0.500$ | $[0, 19.90]$ |

- All eigenvalues sit on the line $\Im E = -1/2$, the constant shift from the $+1/2$ term in $-i(\partial_u + 1/2)$. The operator is symmetric but not self-adjoint on $L^2(\mathbb{R})$ with $dx$ measure; the imaginary shift is intrinsic.
- $\Re E$ density of eigenvalues $\approx L/(2\pi) = 1.59$ per unit, matching the Bohr-Sommerfeld prediction $\rho_{BK}(E) = \log(L/\ell)/(2\pi)$ at our chosen $L/\ell = e^{L}$.

**Structural obstruction.** The Riemann-von Mangoldt density of zeta zeros at height $T$ is
$$\rho_\zeta(T) = \frac{\log(T/(2\pi))}{2\pi},$$
which **grows logarithmically with $T$**. The Berry-Keating density at fixed $L$ is **constant** in energy. Matching them at a single energy $T$ requires $L = \log(T/(2\pi))$, which forces $L$ to depend on $E$. No fixed-domain discretization can reproduce the zeta density globally; only locally at one scale.

This is the well-known "soft cutoff" or "renormalization" issue: a literal Hilbert-Polya operator with $H = xp$ on a fixed domain cannot have the zeta spectrum. Resolutions (Berry-Keating original proposal, Sierra's prescription, Connes' adèle class space) involve either an energy-dependent regulator or moving to a fundamentally different functional-analytic setup.

**Individual zero matching.** None of the BCs produces eigenvalues at the zeta zero heights. The eigenvalue spectrum is roughly uniform on the bandwidth-limited interval, while zeta zeros are at specific values $\gamma_1 = 14.13, \gamma_2 = 21.02, \ldots$ This is consistent with the density mismatch: even if density were right on average, the discrete spectrum wouldn't align with the zeros at fixed grid resolution.

**D-H wrong-approach test (per the project discipline).** Not applied here because the operator construction is generic and doesn't depend on the L-function: $H = xp + px$ is the same operator regardless of which L-function we're trying to match. The relevant question is whether SOME L-function has a spectral realization, not whether THIS operator separates zeta from D-H. (D-H wrong-approach detection becomes meaningful for operator constructions that DEPEND on the L-function's structure, e.g., Connes' adèle setup.)

## 1B: Sierra-Townsend modifications of BK

**Status:** complete; three position-dependent corrections tested, all fail individual zero match; one (modular log-$x$) bends the density in the right direction but overshoots.

**Method:** [e1b_sierra_townsend.py](e1b_sierra_townsend.py). The Sierra-Townsend program (Sierra arXiv:0712.0427 / 1601.01797, Sierra-Townsend arXiv:0805.4847) augments bare Berry-Keating $H_{BK} = (xp + px)/2$ with a slowly varying potential $V(x)$ that, after LLL projection from the hyperbolic upper half plane, is supposed to imprint the Riemann-von Mangoldt log-density on the spectrum. We discretize three representative forms on the same log-grid as 1A, restricted to $x \in [1, e^L]$ (i.e., $u = \log x \in [0, L]$) so the $1/x$ corrections stay regular:

| ID | $V(x)$ | Origin |
|---|---|---|
| ST-A | $+a/(2x^2)$ | Centrifugal: magnetic field on hyperbolic plane |
| ST-B | $-a/(2x)$ | Coulomb-like, attractive |
| ST-C | $+a \log x$ | "Modular" linear-in-$u$ potential |

For each variant we sweep $a \in \{0, 0.5, 1, 2\}$. Periodic boundary condition (same as 1A periodic), $N = 200$, $L = 15$.

**Findings:**

| Variant | $a$ | # positive eigs | $E$ range | $\rho(E=30)$ | RMS vs first 50 $\gamma_n^\zeta$ |
|---|---|---|---|---|---|
| ST-A | 2.0 | 101 | $[0.03, 13.65]$ | $0.00$ | $89.26$ |
| ST-B | 2.0 | 99 | $[0.35, 13.26]$ | $0.00$ | $89.02$ |
| ST-C | 0.0 (= BK) | 101 | $[0, 13.27]$ | $0.00$ | $89.29$ |
| ST-C | 1.0 | 144 | $[0.01, 27.58]$ | $0.33$ | $90.05$ |
| ST-C | 2.0 | 172 | $[0.05, 42.20]$ | $3.33$ | $87.78$ |

Reference: $\rho_\zeta(E = 30) = \log(30/(2\pi))/(2\pi) \approx 0.249$.

**Three takeaways:**

1. **ST-A and ST-B (centrifugal, Coulomb) barely move the spectrum.** Both stay within the BK bandwidth $[0, 13.3]$; the density at $E = 30$ remains zero across all $a$. These short-range corrections do not extend the spectral range beyond the bare BK cutoff.

2. **ST-C (modular) does bend the density.** With $a > 0$ the number of positive eigenvalues grows from 101 to 172 and the energy range extends to 42, so the density genuinely acquires $E$-dependence. But at $a = 2$ the density at $E = 30$ is $3.33$, *thirteen times* zeta's target $0.249$, overshooting in the opposite direction from BK. Tuning $a$ to match the zeta density at one energy will mismatch at any other (the log profile cannot be reproduced by a linear $V$).

3. **No variant matches individual zeta zeros.** RMS deviation from the first 50 $\gamma_n^\zeta$ stays at $\sim 88$ across all variants and couplings, identical in scale to bare BK. The construction has no arithmetic input and cannot reproduce the specific zero locations.

**L-function discrimination test.** The Hamiltonian $H = H_{BK} + V(x)$ has zero L-function input. The same predicted spectrum is "compared to" zeta gammas and to D-H on-line gammas; no variant can prefer one over the other by construction. Zeta's first 10 gammas $\{14.13, 21.02, 25.01, 30.42, \ldots\}$ and D-H's first 10 on-line gammas $\{5.09, 8.94, 12.13, 14.40, \ldots\}$ both differ from any Sierra-Townsend spectrum by RMS $\gtrsim 80$; the construction sees the same picture either way.

**Architectural conclusion (1A + 1B).** Two generations of spectral constructions (bare BK and ST-modified BK) have been tested. Neither reproduces zeta zeros individually, neither reproduces the Riemann-von Mangoldt density, and neither has any mechanism to distinguish zeta from D-H. Any genuine Hilbert-Pólya proof must inject arithmetic information into the operator. This restricts the search to constructions like Connes' adèle class space (1D), where the L-function structure enters via the geometry of $\mathrm{Spec}(\mathbb{Z})$, not via the choice of potential on a fixed manifold.

## 1C: L-function discrimination test ([e1c_lfunction_discrimination.py](e1c_lfunction_discrimination.py))

**Status:** complete; no construction discriminates zeta from D-H beyond factor-3 noise.

**Method:** for each H matrix from 1A (three boundary conditions) and 1B (three Sierra-Townsend variants, $a = 1$), extract the lowest 40 positive eigenvalues. Fit a best AFFINE map $E \mapsto \alpha E + \beta$ to minimize RMS deviation from the first 40 $\gamma_n^\zeta$; separately fit the same spectrum to the first 40 on-line $\gamma_n^{DH}$. The discrimination ratio
$$r := \mathrm{RMS}_\zeta / \mathrm{RMS}_{DH}$$
measures whether the spectrum prefers one target over the other.

**Findings:**

| Variant | RMS to zeta | RMS to D-H on-line | $r$ |
|---|---|---|---|
| 1A-Dirichlet | $2.40$ | $4.80$ | $0.50$ |
| 1A-periodic | $2.77$ | $5.14$ | $0.54$ |
| 1A-open | $2.56$ | $4.73$ | $0.54$ |
| 1B-ST-A | $2.82$ | $5.05$ | $0.56$ |
| 1B-ST-B | $2.76$ | $5.13$ | $0.54$ |
| 1B-ST-C | $4.71$ | $2.82$ | $1.67$ |

Ratios span $[0.50, 1.67]$, spread by factor $3.35$.

**Interpretation:**

1. **Bare BK (1A) and short-range corrections (1B-ST-A, 1B-ST-B) fit zeta slightly better than D-H** ($r \approx 0.5$). The reason is not arithmetic content but zero-distribution variance: D-H gammas have larger variance at low height than zeta gammas (D-H conductor $q = 5$ increases zero density slightly, and the spacing is less regular), so a roughly evenly-spaced BK spectrum is geometrically closer to zeta.

2. **The modular ST-C variant flips the ratio to $r = 1.67$**, mildly favoring D-H. This is the dense-spectrum variant with $a = 1$, whose 144 positive eigenvalues spread up to $E = 27.58$; the higher density gives a marginally better D-H fit.

3. **No variant achieves the discrimination a genuine arithmetic construction would give.** A Hamiltonian whose spectrum is exactly $\{\gamma_n^\zeta\}$ would have RMS_zeta $= 0$ and RMS_DH $\sim 10$ (the inter-L-function gamma spacing variance), giving $r = 0$. The factor-3 spread we observe is consistent with random alignment to two similar-density sequences, not with structural L-function content.

**Off-line D-H gamma matching test:**

| Variant | min $|E - \gamma_{\mathrm{off}}|$ | mean |
|---|---|---|
| 1A-Dirichlet | $0.37$ | $8.34$ |
| 1A-periodic | $0.46$ | $9.10$ |
| 1A-open | $0.32$ | $8.20$ |
| 1B-ST-A | $0.43$ | $8.09$ |
| 1B-ST-B | $0.42$ | $8.99$ |
| 1B-ST-C | $0.11$ | $0.56$ |

1B-ST-C's small mean is an artifact of its dense spectrum (144 eigenvalues over the relevant range, giving an expected nearest-neighbor distance $\sim 1.5$), not a real prediction of off-line zero locations. The 1A and other 1B variants have means $\sim 8\text{--}9$, far from any off-line gamma. No variant "predicts" the off-line zeros in any meaningful sense.

**Architectural conclusion (1A + 1B + 1C).** Three spectral constructions have been tested across six total variants. All produce spectra whose first 40 eigenvalues fit zeta gammas with RMS $2.4\text{--}4.7$ and D-H gammas with RMS $2.8\text{--}5.1$ after best affine rescaling. The discrimination ratio is bounded to a factor of $\sim 3$ around 1, consistent with random alignment, not arithmetic content. A genuine Hilbert-Pólya proof would require either:

  - A construction whose H matrix encodes the Euler product (or equivalent arithmetic input) so the spectrum genuinely depends on whether the target is $\zeta$ or $\chi_3$ or D-H, **or**
  - A theorem that some specific operator's spectrum coincides with $\{\gamma_n^\zeta\}$ via deeper structure (Connes adèle class space, 1D).

The numerical experiments in 1A-1C do not produce such a construction. They confirm the Connes-style structural obstruction at a quantitative level.

## 1D

Connes adèle class space (literature task): deferred.
