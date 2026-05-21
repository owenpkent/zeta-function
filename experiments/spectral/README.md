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

## 1B, 1C, 1D

- **1B** (Sierra-Townsend hyperbolic model): proposed for next session.
- **1C** (apply candidate operators to D-H): activates only when 1A or 1B is L-function-specific.
- **1D** (Connes adèle class space, literature): deferred.
