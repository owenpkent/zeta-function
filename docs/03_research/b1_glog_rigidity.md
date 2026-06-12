# B1: the G_log dense-translate rigidity lemma

**Status: BUILDER deliverable (2026-06-11), the constructive residue of the P0/P3 survey ([kms_weights_p0_p3_survey.md](kms_weights_p0_p3_survey.md), LEARNINGS #85). Proven here in full; elementary, Lean-ready.**

## Statement

**Lemma (G_log rigidity).** Fix $\beta \in \mathbb{R}$. Let $\nu$ be a positive Radon measure on $\mathbb{R}$ satisfying the prime-translation quasi-invariance with exact cocycle

$$\nu(A + \log p) = p^{-\beta}\,\nu(A) \qquad \text{for every prime } p \text{ and every Borel } A \subset \mathbb{R}. \tag{QI}$$

Then $\nu = c\,e^{-\beta x}\,dx$ for some constant $c \ge 0$. In particular the (QI)-solutions form a single ray, non-normalizable for every $\beta$ (infinite total mass), i.e. a weight ray, never a state.

This is the continuum (non-compact unit space) closure of the discrete Lemma 1 of [lcc_bc_transport.md](lcc_bc_transport.md): under $x = \log n$ the ray restricts to the flat comb $c_n = c_1 n^{-\beta}$ (check: $\int_{A+\log p} e^{-\beta x} dx = p^{-\beta} \int_A e^{-\beta y} dy$).

## Proof (five steps)

1. **Twist.** Define $dm(x) := e^{\beta x}\,d\nu(x)$. Since $e^{\beta x}$ is locally bounded and $\nu$ is Radon, $m$ is Radon.

2. **(QI) becomes invariance.** For any Borel $f \ge 0$ and $s = \log p$, the set identity (QI) gives, by simple-function approximation, the change-of-variables $\int f(x)\,d\nu(x) = e^{-\beta s} \int f(y + s)\,d\nu(y)$. Apply it to $f(x) = \mathbf{1}_{A+s}(x)\,e^{\beta x}$:
$$m(A + s) = e^{-\beta s} \int \mathbf{1}_A(y)\,e^{\beta(y+s)}\,d\nu(y) = \int_A e^{\beta y}\,d\nu(y) = m(A).$$
So $m$ is invariant under translation by $\log p$ for every prime $p$, hence under the subgroup $G_{\log} = \{\sum_p k_p \log p : k_p \in \mathbb{Z}, \text{ finitely many nonzero}\}$.

3. **Density.** $G_{\log}$ is dense in $\mathbb{R}$: a subgroup of $\mathbb{R}$ is either cyclic or dense, and $\log 2 / \log 3 \notin \mathbb{Q}$ (else $2^a = 3^b$ with $a, b$ positive integers, contradicting unique factorization). Two primes suffice; the remaining primes add nothing at this step.

4. **Vague continuity upgrades dense invariance to full invariance.** For $f \in C_c(\mathbb{R})$ the map $t \mapsto \int f(x - t)\,dm(x)$ is continuous: for $t_n \to t$ the supports of $f(\cdot - t_n)$ lie in a common compact $K$, $f$ is uniformly continuous, and $\left| \int (f(x - t_n) - f(x - t))\,dm \right| \le \|f(\cdot - t_n) - f(\cdot - t)\|_\infty\, m(K) \to 0$. Invariance on the dense set $G_{\log}$ plus continuity gives $\int f(x - t)\,dm = \int f\,dm$ for all $t \in \mathbb{R}$, i.e. $m$ is translation-invariant.

5. **Haar uniqueness.** A translation-invariant Radon measure on $\mathbb{R}$ is a multiple of Lebesgue: $m = c\,\mathrm{Leb}$. Hence $\nu = c\,e^{-\beta x}\,dx$. $\square$

## Remarks (what the proof teaches)

- **Organ accounting.** Rotation density (step 3-4, the dense translates) does ALL the uniqueness work; the pole/normalization organ does NONE (the conclusion is a non-normalizable weight ray; no normalization is ever invoked). This is the cleanest possible exhibit of the #81 organ separation in the weights category, on a NON-COMPACT unit space, which compact-$\hat{\mathbb{Z}}$ Bost-Connes could not display.
- **Two primes suffice.** Uniqueness here needs only $\log 2/\log 3 \notin \mathbb{Q}$. Contrast the BC organ A, where Dirichlet density in $\hat{\mathbb{Z}}^*$ uses the full prime set. The full set matters for the EF slice, not for the homogeneous cone.
- **Position in the program.** Per #85, $\mathcal{W}_\zeta = (\text{homogeneous KMS cone}) \cap (\text{EF slice})$. This lemma settles the CONE leg on the line by direct proof (matching Neshveyev-Stammeier Thm 4.5 on the Toeplitz side and Lemma 1 on the discrete side: three independent derivations of the same flat ray). The slice rigidity (P2a/P2b/P4) is untouched and remains the open core; e3hh already proved the flat ray is NOT in the slice.
- **D-H / K1 / freeze.** No L-function appears anywhere (the lemma is about $\mathbb{R}$ and the primes' logarithms only): K1 trivially clean, D-H constructionally out of scope (no semigroup, the #55 firewall class), nothing numerical claimed (the proof is exact).
- **Lean target (V4).** Steps 1-5 use: pushforward measures, density of non-cyclic subgroups of $\mathbb{R}$ (`Real.subgroup_dense_or_cyclic` exists in Mathlib in some form), vague continuity of translation, and Haar uniqueness (`MeasureTheory.Measure.isHaarMeasure` machinery). A clean medium-size formalization alongside V1-V3 of the transport dossier.

## Cross-references

#85 (the survey that posed B1), #82 (Lemma 1, the discrete shadow), #81 (organ anatomy), e3hh (the flat ray's exclusion from the slice), #76 (LCC). The lemma's role is structural closure: it finishes the operator-algebra/measure-rigidity leg so that all remaining effort points at the explicit-formula slice.
