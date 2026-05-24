# 1D — Connes' Adèle Class Space (Literature Review)

> The natural follow-up to [1A-1C](README.md): all bare and Sierra-Townsend-modified Berry-Keating Hamiltonians failed to discriminate $\zeta$ from D-H (factor-3 ratio around 1, consistent with random alignment). The fundamental obstruction (LEARNINGS finding #4): no fixed-domain discretization of a position-momentum operator can produce a spectrum that genuinely depends on the L-function, because the operator construction is L-function-agnostic.
>
> Connes' adèle-class-space program (Connes 1995, 1999) is the natural exception: the construction is INTRINSICALLY arithmetic because the adèle ring $\mathbb{A}_\mathbb{Q}$ encodes the local $p$-adic structure at every prime. This is the closest existing approach to a "Hilbert-Pólya construction with arithmetic content."
>
> This document is a literature review summarizing what Connes' framework adds beyond the operators tested in 1A-1C, and what would be needed for it to produce a rigorous spectral identification with $\{\gamma_n\}$.
>
> **Cross-cut**: deep dive on Connes' framework from the Architecture 2 (geometric) angle is in [2A_connes_dossier.md](../arithmetic_geometric/2A_connes_dossier.md). This 1D doc is the Architecture 1 (spectral / Hilbert-Pólya) angle.

## 1. What 1A-1C established (recap)

- **1A**: Bare Berry-Keating $H = (xp + px)/2$, discretized on a uniform log-grid. All eigenvalues collapse to $\Im E = -1/2$ (a constant shift from the symmetrization). Density $\rho_{BK} = L/(2\pi)$ is constant in energy; zeta density $\log(T/(2\pi))/(2\pi)$ grows logarithmically. **No fixed-domain discretization of $H$ can reproduce zeta density.**

- **1B**: Three Sierra-Townsend modifications (centrifugal $+a/x^2$, Coulomb $-a/x$, modular log $+a \log x$). RMS vs first 50 $\gamma_n^\zeta$ stays $\sim 88$ across all variants — none discriminates against bare BK. Modular log bends the density in the right direction but overshoots.

- **1C**: L-function discrimination test on six 1A+1B variants. RMS vs $\zeta$ in $[2.4, 4.7]$, RMS vs D-H in $[2.8, 5.1]$, ratio $\in [0.5, 1.67]$. Factor-3 spread consistent with random alignment of similar-density sequences. **No variant has L-function content.**

**The structural diagnosis** (from LEARNINGS #4): the operators $H = (xp + px)/2 + V(x)$ depend only on the potential $V(x)$. They have no input from the Euler product or any L-function-specific data. Hence the spectrum cannot depend on which L-function we want to match.

## 2. Why Connes' adèle class space is structurally different

The adèle ring of $\mathbb{Q}$:
$$\mathbb{A}_\mathbb{Q} = \mathbb{R} \times {\prod_{p \text{ prime}}}' \mathbb{Q}_p$$
where the prime ($\prod'$) denotes the restricted product (almost all components in $\mathbb{Z}_p$). The adèle class space:
$$S_\mathbb{Q} = \mathbb{A}_\mathbb{Q} / \mathbb{Q}^*.$$

**Why this has arithmetic content**: every prime $p$ enters explicitly as the $\mathbb{Q}_p$ factor in $\mathbb{A}_\mathbb{Q}$. The $\mathbb{Q}^*$-action by multiplication mixes the local components in a way that encodes the multiplicative structure of $\mathbb{Q}$. The Euler product of $\zeta$ emerges from the per-place structure of $\mathbb{A}_\mathbb{Q}$.

**Contrast with 1A-1C**: position-momentum Hamiltonians on $\mathbb{R}$ have no notion of "prime $p$"; they only see real-valued operators. The arithmetic information is absent by construction.

**The Connes Hilbert space**:
$$\mathcal{H} = L^2(\mathbb{A}_\mathbb{Q}^*) / (\mathbb{Q}^* \text{-action})$$
(more precisely, certain subspaces / quotients respecting the noncommutative structure). The natural operator on $\mathcal{H}$ is the generator $H$ of the $\mathbb{R}_+^*$-action via the modulus map $|\cdot|: \mathbb{A}_\mathbb{Q}^* \to \mathbb{R}_+^*$, which descends to $S_\mathbb{Q}$.

**The Connes conjecture**: the spectrum of $H$ consists exactly of the imaginary parts $\{\gamma_n\}$ of $\zeta$ zeros.

## 3. What the trace formula provides

Connes (1999) "Trace formula in noncommutative geometry and the zeros of the Riemann zeta function" gives a regularized trace formula for the $\mathbb{R}_+^*$-action $U_t = e^{itH}$:

$$\mathrm{Tr}_\Lambda(U(h)) = 2 h(1) \log' \Lambda - \sum_v \int_{\mathbb{Q}_v^*}' \frac{h(u^{-1})}{|1 - u|} d^* u + o(1)$$

where $\sum_v$ runs over places of $\mathbb{Q}$ (= primes + archimedean place), and $\mathrm{Tr}_\Lambda$ is a regularized trace at cutoff $\Lambda \to \infty$.

**The structural achievement**: this formula has the same shape as the explicit formula for $\zeta$ zeros — the spectral side $\mathrm{Tr}_\Lambda(U(h))$ "should be" $\sum_\rho \hat h(\rho)$ if the spectral identification holds. The geometric side is exactly the sum over primes that the explicit formula produces.

**The gap**: the rigorous proof of $\mathrm{Tr}_\Lambda(U(h)) = \sum_\rho \hat h(\rho)$ requires the spectral identification (eigenvalues of $H$ = imaginary parts of $\gamma_n$), which is the central RH-equivalent conjecture.

## 4. Why this is still conjectural

The Connes program does NOT yet prove that $H$'s spectrum is $\{\gamma_n\}$. What it does provide:
- A rigorous noncommutative space $S_\mathbb{Q}$ with an $\mathbb{R}_+^*$-action.
- A trace formula structure parallel to the explicit formula.
- A POSITIVITY conjecture (Weil-Bombieri positivity in $S_\mathbb{Q}$) equivalent to RH.

What it does NOT provide:
- A proof that $H$ has the right spectrum.
- A proof of the positivity conjecture without assuming RH.

Per [2A_R3](../arithmetic_geometric/2A_R3_connes_positivity.md), [2A_R3.5](../arithmetic_geometric/2A_R3_5_K1_universality.md), and the Connes dossier ([2A_connes_dossier.md](../arithmetic_geometric/2A_connes_dossier.md)), the positivity is K1-equivalent — falls under the no-shortcut theorem. So Connes' framework gives the right STRUCTURE for a Hilbert-Pólya proof but doesn't close the spectral identification or the positivity.

## 5. What is needed to make 1D a rigorous experiment

For our experimental project, a "1D experiment" in the spirit of 1A-1C would need:

**A discretization of Connes' adèle class space**. This requires:
- Truncating to finitely many primes $\{p_1, p_2, \ldots, p_K\}$.
- Truncating each $\mathbb{Q}_{p_i}$ to a finite $\mathbb{Z}/p_i^N$ for some $N$.
- Constructing the corresponding finite Hilbert space and the $\mathbb{R}_+^*$-action.

**The technical issues**:
- The $\mathbb{Q}^*$-action mixes all primes simultaneously. Truncating to finitely many primes breaks this; the resulting "truncated" operator has spectrum that depends on the truncation rather than approaching $\{\gamma_n\}$.
- The continuous $\mathbb{R}_+^*$-action discretizes awkwardly; natural step sizes don't match the logarithmic scale of $\{\gamma_n\}$.
- The regularization (cutoff $\Lambda$) is delicate; numerical truncation may not converge to the right limit.

**Conclusion**: a finite-rank approximation of Connes' construction is non-trivial. Existing work (Connes-Marcolli on Bost-Connes systems) provides operator-algebraic models but these are infinite-dim by construction; finite-dim approximations have not been systematically explored numerically.

## 6. What 1D would add beyond 1A-1C

A rigorous 1D experiment, if executable, would:
1. **Demonstrate L-function content in the operator**: the operator's matrix elements WOULD depend on the L-function (Euler product enters explicitly via prime structure of $\mathbb{A}_\mathbb{Q}$).
2. **Test discrimination against D-H**: D-H has no Euler product so it doesn't fit naturally into the adèle framework — this is the structural reason Connes' approach excludes D-H (per [2A_R1](../arithmetic_geometric/2A_R1_DH_exclusion.md)).
3. **Probe the spectral identification numerically**: if a finite-rank approximation of $H$ has eigenvalues converging toward $\{\gamma_n\}$ as the truncation grows, that's circumstantial evidence for the spectral identification.

**My honest assessment**: a rigorous numerical 1D experiment is research-grade work (months, not weeks). The path is:
- Choose a specific discretization (e.g., Bost-Connes-style with finite Hecke algebra).
- Implement the $\mathbb{R}_+^*$-action's generator $H$ as a matrix.
- Compute eigenvalues; compare to $\{\gamma_n\}$.
- Sweep truncation parameter; check convergence.

Without such an implementation, the structural understanding is: Connes' construction IS the natural Hilbert-Pólya construction with arithmetic content, but the spectral identification remains conjectural and the K1 wall (R3.5) applies to the positivity formulation.

## 7. Cross-architecture connection

The Connes framework sits at the interface of three architectures:

- **Arch 1 (spectral / Hilbert-Pólya)**: provides the operator and Hilbert space; closes the "no arithmetic content" obstruction from 1A-1C; remains conjectural on spectral identification.
- **Arch 2 (arithmetic-geometric)**: provides the geometric setting ($S_\mathbb{Q}$ as a noncommutative space); covered in detail in [2A_connes_dossier.md](../arithmetic_geometric/2A_connes_dossier.md).
- **Arch 3 (positivity)**: the positivity conjecture is K1-equivalent per R3.5; cannot break the wall without geometric input.

**The structural unification**: Connes' framework is the most-developed candidate that connects all three architectures in a single construction. Per [2A_path_forward.md](../arithmetic_geometric/2A_path_forward.md), the most promising hybrid direction is Connes + Borger + prismatic cohomology, which would give the spectral / geometric / cohomological ingredients on a unified structure.

## 8. Bottom line on 1D

**Status of 1D as a numerical experiment**: not pursued. A rigorous finite-rank approximation of Connes' adèle class space is research-grade work and the central conjecture (spectral identification) is not within reach of finite-dim numerics.

**Status of 1D as a literature review**: this document. Summarizes what Connes' framework adds beyond 1A-1C, why the spectral identification is conjectural, and how the construction integrates with Arch 2's geometric program.

**Key references** (see also [Connes dossier](../arithmetic_geometric/2A_connes_dossier.md) for fuller list):
- Connes, A. (1995). *Formule de trace en géométrie non-commutative et hypothèse de Riemann*. C. R. Acad. Sci. Paris 323.
- Connes, A. (1999). *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*. Selecta Math. 5.
- Bost, J.-B.; Connes, A. (1995). *Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory*. Selecta Math. 1.
- Meyer, R. (2005). *On a representation of the idèle class group related to primes and zeros of L-functions*. Duke Math. J. 127.
- Connes, A. (2019). *An essay on the Riemann Hypothesis*. Open Problems in Mathematics, Springer.

**The takeaway for the experimental program**: 1A-1C exhausted the "naïve spectral discretization" direction within Arch 1. Connes' adèle program is the natural "second-level" Hilbert-Pólya approach, but it requires the noncommutative-geometric machinery covered in Arch 2 (and is K1-blocked on positivity per R3.5). The Arch 1 thread is effectively complete from the experimental side; further progress requires the deeper Arch 2 + NCG infrastructure.
