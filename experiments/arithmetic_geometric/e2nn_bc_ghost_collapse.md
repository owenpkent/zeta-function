# e2nn: Finite-window Bost-Connes ghost-room collapse

**Date:** 2026-06-10. **Status:** complete, 6/6 checks pass. **Script:** [`e2nn_bc_ghost_collapse.py`](e2nn_bc_ghost_collapse.py). **Data:** `e2nn_bc_ghost_collapse.npz`.

## Why this experiment exists (the #79 -> #80 gap)

LEARNINGS #79 ([e2ll_ff_crystal_cone.py](e2ll_ff_crystal_cone.py)) confirmed the program's named target, composite pinching, over $\mathbb{F}_q$, and identified its mechanism: **flat-extension uniqueness** of the truncated trigonometric moment problem (Curto-Fialkow). The Frobenius measure is $2g$ atoms, the moment Toeplitz goes flat, the representing measure is unique. #80 ([e3gg_zeta_moment_mirror.py](../positivity/e3gg_zeta_moment_mirror.py)) showed that this mechanism has **no purchase on zeta**: the pole-sourced continuous archimedean spectrum keeps the moment matrix full rank forever, leaving ~15 orders of magnitude of ghost room. The named open core became:

> a moment-uniqueness theorem for a measure with a continuous (archimedean) component PLUS the Euler structure that singles zeta out.

This experiment imports the one place in mathematics where a theorem of exactly that shape is already **proven, unconditional, and Euler-powered**: the Bost-Connes phase transition.

## The import

**Bost-Connes (1995).** For the BC system (the Hecke $C^*$-algebra of $\mathbb{Q}$, whose partition function is $\zeta(\beta)$ and whose symmetry is $\hat{\mathbb{Z}}^*$), the simplex of KMS$_\beta$ states:

- $\beta > 1$: a huge simplex, extreme points indexed by $x_0 \in \hat{\mathbb{Z}}^*$ (atomic, type I, Gibbs $\mu = \zeta(\beta)^{-1}\sum_n n^{-\beta}\delta_{n x_0}$).
- $0 < \beta \le 1$: **the simplex is a single point**, of type III$_1$, whose spectral realization is **continuous**.

"The simplex is a point" is the exact statement shape of the LCC/EFR composite-pinching target (#76: *the cone of positive log-crystals is the singleton $\{\Lambda\}$*; the ghost-crystal kill). And the BC proof runs on exactly two organs:

1. **The pole.** $\sum_n n^{-\beta}$ diverges for $\beta \le 1$, so the atomic ghost states cannot normalize. The pole is the atom-killer.
2. **Rotation density.** The primes generate a dense subgroup of $\hat{\mathbb{Z}}^*$ (Dirichlet), so any surviving state is forced to be uniform on the unit shells. The Euler structure is the uniformizer.

Note what this is **not**: the killed Mechanism 2 of [building_the_missing_positivity.md](../../docs/03_research/building_the_missing_positivity.md) tried to use the $\beta > 1$ Gibbs state's Tomita modular operator *as the polarization* (dead: type-incompatible, $\Delta$ strictly PSD, no Hodge sign). The present import uses the $\beta \le 1$ **uniqueness theorem as a template for the cone-is-a-singleton statement**. No polarization, margin, or positivity is claimed here.

## Finite-window formulation

KMS$_\beta$ states correspond to measures $\mu$ on $\hat{\mathbb{Z}}$ with the scaling property $\mu(nE) = n^{-\beta}\mu(E)$ for all $n \in \mathbb{N}^\times$. Truncate the semigroup to $N_S$ ($S$ = first $m$ primes) and observe through a finite window $(\mathbb{Z}/M)^*$ ($M$ a product of small prime powers). The candidate states ("ghosts") restrict to marginals supported on cosets of

$$H_m = \langle q \bmod M : q \in S_m,\ \gcd(q, M) = 1\rangle \subseteq (\mathbb{Z}/M)^*,$$

with within-coset shape the normalized geometric-orbit convolution $\nu = \circledast_{p} w_p$, where $w_p(p^j \bmod M) \propto p^{-j\beta}$. Both organs become exact finite computations:

- **Organ A (rotation density, integer-exact):** the ghost-component count $g(m) = [(\mathbb{Z}/M)^* : H_m]$.
- **Organ B (pole, finite Euler products):** the within-coset ghost diameter $u(\beta, m) = \mathrm{TV}(\nu, \mathrm{uniform\ on\ } H_m)$, and the system-wide atom budget $A(\beta, m) = \prod_{p \le p_m}(1 - p^{-\beta})$ (the largest point mass any normalized scaling state can carry).

On the Fourier side $\hat\nu(\chi) = \prod_p \frac{1 - p^{-\beta}}{1 - \chi(p) p^{-\beta}}$, a ratio of finite Euler products, so the collapse rate is governed by $\sum_p (1 - \mathrm{Re}\,\chi(p)) p^{-\beta}$: divergent for $\beta \le 1$ (Mertens for $L(1,\chi) \ne 0$), convergent for $\beta > 1$. The prediction is a phase transition at the pole with **log-slow collapse exactly at criticality**.

## Results (first 10,453 primes, $p_{\max} = 109{,}987$)

**Organ A collapses fast and unconditionally.** $g(m) = 1$ by $m^* \le 5$ for all windows tested ($M = 5, 7, 8, 9, 16, 21, 40$); over all prime windows $p < 300$ the median $m^*$ is 2, max 4 (at $p = 71$). The collapse time is a least-prime-in-subgroup statistic (Linnik-flavored, unconditional).

**Organ B exhibits the phase transition at the pole.** Within-coset ghost diameter $u(\beta, m)$:

| window | $\beta = 0.70$ | $\beta = 1.00$ | $\beta = 1.50$ |
|---|---|---|---|
| $M = 5$ | $2.8\mathrm{e}{-2} \to 3.2\mathrm{e}{-7}$ (stretched-exp) | $1.0\mathrm{e}{-1} \to 3.3\mathrm{e}{-2}$ (log-slow) | $2.7\mathrm{e}{-1} \to 2.56\mathrm{e}{-1}$ (**plateau**) |
| $M = 8$ | $7.3\mathrm{e}{-2} \to 6.6\mathrm{e}{-7}$ | $2.1\mathrm{e}{-1} \to 6.1\mathrm{e}{-2}$ | $4.4\mathrm{e}{-1} \to 4.05\mathrm{e}{-1}$ (**plateau**) |
| $M = 21$ | $1.5\mathrm{e}{-1} \to 1.4\mathrm{e}{-6}$ | $3.3\mathrm{e}{-1} \to 9.9\mathrm{e}{-2}$ | $5.8\mathrm{e}{-1} \to 5.38\mathrm{e}{-1}$ (**plateau**) |

At $\beta = 1$ exactly, $u \cdot \log p_m$ stabilizes to a constant (0.379 / 0.707 / 1.146 for $M = 5/8/21$): the collapse at the pole is **exactly log-slow**, $u \sim C/\log p_m$.

**Both organs are load-bearing (amputation tests, #77 style).**

- *Pole removed* ($\beta = 1.5$): $u(10{,}000)/u(1{,}000) = 0.9984$ at every window. The ghost survives; the atom budget stalls at $A \to 1/\zeta(1.5) = 0.382793$ (computed: 0.382971).
- *Rotations removed* (stream only primes $\equiv 1 \bmod 5$, window $M = 5$): the index stays 4 forever even though $\sum 1/p$ over the stream diverges (0.404 at $p < 110$k and growing). Ghost components persist despite a fully intact pole organ.

**The marginality fingerprint.** At criticality the atomic ghost budget obeys Mertens: $-\log(A(1,m)\log p_m) \to 0.5775$ against $\gamma = 0.5772$. The constant $e^{\gamma}$, which #63 met as the resolution cost of the soft-detector wall, reappears here as **the rate constant of uniqueness at the pole**: the simplex collapses to a point, but log-slowly, i.e. *barely*. The program's marginal-positivity fingerprint shows up in this costume as criticality of the collapse rate, exactly at the pole.

## What this changes

#80 left the transfer gap as "we need a uniqueness theorem for a positive functional with continuous spectrum, pinned by Euler structure, and the moment-problem toolbox cannot supply it." This experiment exhibits that **such a theorem exists, is unconditional, and its engine is precisely the program's organ pair**: the pole kills the atomic ghosts (B_pole's job) and prime multiplicativity forces uniformity (P_pp's job). The technology is not flat extension (rank rigidity) but **scaling-quasi-invariance + ergodicity** (group-measure rigidity). That is a different, and proven, route to "the cone is a singleton."

**The open BUILDER target (the transport).** Formulate the LCC log-crystal cone as the KMS-type simplex of a scaling action: find the action of $\mathbb{N}^\times$ on the crystal space (candidate: $T_p: c(n) \mapsto c(pn)$, under which $\Lambda$'s prime-power support is the shell structure and $\Lambda = \mu * \log$ encodes the quasi-invariance cocycle) such that positive crystals = scaling-quasi-invariant functionals, the pole plays the normalization-killer, and prime-rotation density forces the von Mangoldt ray. If that formulation exists, the BC uniqueness proof is the template for the ghost-crystal kill. The known wall to respect: BC's Gibbs side lives at $\beta > 1$ and the #42 continuation wall stands between the semigroup side and the zeros; the transport targets the **source-side cone** (LCC), not the zero side, which is exactly where #76 placed the open core.

## Honesty block

- **No zeros are computed or used anywhere.** The experiment is pure unconditional number theory (subgroup closures, finite Euler products). K1-clean by construction.
- **No positivity margin is claimed.** Soft-detector freeze respected; nothing here is a detector.
- **D-H status:** the mechanism is constructionally **undefined** for Davenport-Heilbronn (no Euler product, hence no multiplicative semigroup, hence no scaling action: the #55 firewall class, like Arch 2). This is a structural firewall, not a numerical separation.
- **What is genuinely new here vs. known:** the BC uniqueness theorem is 1995 mathematics; the contribution is (i) recognizing it as the exact statement shape of the #79/#80 transfer gap, (ii) the finite-window formulation making both organs exactly computable, (iii) the quantified phase transition + log-slow criticality + Mertens rate constant, and (iv) the named transport target.
- **What this does not do:** it does not supply the Weil-cone uniqueness theorem, does not touch the critical strip, and does not advance M4 directly. It is a technology-existence proof plus a precise transport question.

## Cross-references

#79 (the F_q mechanism this complements), #80 (the obstruction this answers in shape), #76 (LCC/EFR, whose singleton-cone target is the BC statement shape), #55 (the BC product-state K2 firewall this builds on), #63 ($e^\gamma$, reappearing as the criticality rate constant), #42 (the continuation wall the transport must respect), [building_the_missing_positivity.md](../../docs/03_research/building_the_missing_positivity.md) Mechanism 2 (the killed BC costume this is distinct from). References: Bost-Connes, *Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory* (Selecta Math. 1995); Laca-Neshveyev for the KMS classification; Mertens' third theorem.
