# 2RR: the finite-prime modular structure is euler-gated (milestone MC.3, K2)

> Experiment [`e2rr_modular_euler_gating.py`](e2rr_modular_euler_gating.py). Milestone MC.3 of [`../../docs/03_research/modular_polarization_carrier.md`](../../docs/03_research/modular_polarization_carrier.md). Result recorded as LEARNINGS #102. Follows MC.1/MC.2 (e2pp #100, e2qq #101).

## The question

The modular-carrier dictionary (#100/#101) splits into a finite-prime part (Frobenius / Euler factors) and an archimedean part (Sen / $\Gamma$-factor). For the carrier to respect the Davenport-Heilbronn discipline (K2), the discriminator must live in the **finite-prime** part: D-H has a functional equation (so it shares the archimedean piece) but no Euler product. MC.3 checks that the finite-prime modular structure is euler-gated, present for $\zeta$ and structurally absent for D-H (#44: K2 lives on $F$, not on $\Theta_{\mathrm{Sen}}$).

## The structure

The finite-prime modular structure is the Bost-Connes Gibbs/KMS structure: the BC Hamiltonian has eigenvalues $\{\log n\}$, partition function $Z(\beta)=\mathrm{Tr}\,e^{-\beta H}=\sum_n n^{-\beta}=\zeta(\beta)=\prod_p(1-p^{-\beta})^{-1}$ with a pole at $\beta=1$ (the type III$_1$ phase transition, #81). The "interaction" is the von Mangoldt comb $-f'/f(s)=\sum_n\Lambda_f(n)n^{-s}$, computed from the Dirichlet coefficients by $\Lambda_f(n)=a_n\log n-\sum_{d\mid n,\,d<n}a_{n/d}\Lambda_f(d)$. The Euler product is exactly the statement that this comb is non-negative and supported on prime powers (passivity, #90/#37).

## The result (each asserted)

1. **$\zeta$'s comb is non-negative.** $\min_n\Lambda(n)=0$ over $n\le60$, zero negatives, supported exactly on the prime powers (the von Mangoldt comb). The positive Gibbs weights exist, so the finite-prime modular structure forms.
2. **D-H's comb goes negative.** $\Lambda_{\mathrm{DH}}(3)=-0.3121$, matching the closed form $-\kappa\log3$ ($\kappa$ the D-H constant); the first negative is at $n=3$ (the first prime $\equiv3\bmod5$), with 21 negatives among $n\le60$. No positive Gibbs state, so the finite-prime modular structure does **not** form for D-H. This reproduces #90 from the modular side.
3. **$\zeta$'s partition function is the Euler product with a pole; the archimedean factor is shared.** $\prod_{p<5000}(1-p^{-2})^{-1}=\zeta(2)$ to residual $\sim2\times10^{-5}$ (a truncation tail $\to0$); $Z(1.02)=50.6$ (the type III$_1$ pole). $\zeta$ has an Euler product, D-H does not, but **both** have a functional equation (the archimedean $\Gamma$-factor), so the archimedean half cannot discriminate. The discriminator is purely the finite-prime comb.

## Reading

The finite-prime modular (Bost-Connes) structure is **euler-gated**: the positive von Mangoldt comb $\to$ the Gibbs/KMS state $\to$ the type III$_1$ factor exists for $\zeta$ and structurally fails for D-H (indefinite comb, no Euler product). So the modular polarization carrier, built on the finite-prime modular flow, passes the K2 firewall **by construction** (D-H cannot even form it), exactly as the oracle's `NoEulerProduct` and the Lean `no_dh_cupTarget` do for the cup target. The archimedean half is shared and inert for K2; the arithmetic that RH needs lives in the euler-gated finite-prime modular structure (#44).

This completes the cheap milestones of the modular-carrier program: MC.1 (the modular structure supplies the weight ladder + duality the trace lacks), MC.2 (it factors the gap: $C_E$ and $N$ are extra data beyond the modular Hamiltonian), MC.3 (the finite-prime modular structure is euler-gated). The open kernel MC.4 is unchanged: prove the $C_E$-twisted form on the finite-prime modular carrier is positive, carrying $t$, without RH input. That is M4.

## Cross-refs

- LEARNINGS #102 (this), #101 (MC.2), #100 (MC.1), #90 (the passivity comb, reproduced here from the modular side), #81 (BC type III$_1$), #44 ($F$ vs $\Theta_{\mathrm{Sen}}$, the finite/archimedean split), #37 (the prime-side discriminator).
- Docs: [`../../docs/03_research/modular_polarization_carrier.md`](../../docs/03_research/modular_polarization_carrier.md) (MC.3), [`../../docs/03_research/acoustic_passive_lossless.md`](../../docs/03_research/acoustic_passive_lossless.md) (#90).
