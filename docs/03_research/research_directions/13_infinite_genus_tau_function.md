# Direction 13: Infinite-genus periods (RH as Riemann's bilinear relations on a Sato-Grassmannian point)

> **Status: speculative, proposed 2026-05-30.** Embraces the obstruction of LEARNINGS #25 instead of fighting it.
>
> **Headline.** Finding #25 says the obstruction is that $\mathrm{Spec}(\mathbb{Z})$ has no finite genus. Embrace infinite genus. In the Krichever / Segal-Wilson dictionary, the **Riemann bilinear relations are a Hodge index** (the period matrix has positive-definite imaginary part). Build an infinite-genus spectral curve / KP tau-function whose tau-function is the completed $\xi(s)$, and RH becomes positive-definiteness of an infinite-dimensional period form. This is Architecture 2 made transcendental via integrable systems.

## 1. The idea in one paragraph

The classical Riemann bilinear relations on a genus-$g$ curve assert that the imaginary part of the period matrix is positive definite, a $(g,g)$ Hodge-index signature on $H^1$. The integrable-systems dictionary (Sato; Segal-Wilson; Krichever) attaches to each point $W$ of the Sato Grassmannian a (possibly infinite-genus) curve and a **tau-function** $\tau$. Direction 13 seeks to realize the completed $\xi(s)$ (or its Hadamard product) as such a tau-function, so that the zeros of $\xi$ become the curve's spectral/branch data, and "all zeros on the critical line" becomes "the infinite-dimensional period form is positive definite" (Riemann's relation in the Feldman-Knorrer-Trubowitz infinite-genus framework). No algebraic surface is built; the Hodge index lives on an integrable-system curve where it already exists classically and only needs its infinite-dimensional extension.

## 2. Formal kernel

- **Tau-function.** Realize $\Xi(z) = \xi(1/2 + iz)$ (even, real, order 1) as a KP tau-function $\tau(t_1, t_2, \dots)$ under a chosen embedding of the spectral parameter into the KP times, or as a Toda/Hankel tau-function of its Taylor moments.
- **Constraint.** A tau-function must satisfy the **Hirota bilinear equations** (equivalently the Plücker relations on its Schur expansion), e.g. the first KP equation $(D_1^4 + 3 D_2^2 - 4 D_1 D_3)\,\tau\cdot\tau = 0$. Not every entire function is a tau-function; the Euler product is conjecturally what makes $\xi$ one.
- **Period positivity.** RH $\Leftrightarrow$ the infinite-genus period form $\mathrm{Im}\,\Omega \succ 0$. This is the Hodge index in infinite genus.
- **Bridge to Direction 9.** The simplest necessary conditions are the **Turan inequalities** / **Jensen-polynomial hyperbolicity** for the $\Xi$ Taylor coefficients (Pólya; Csordas-Norfolk-Varga; Griffin-Ono-Rolen-Zagier 2019). These are exactly the degree-1 Hodge-Riemann / log-concavity content of Direction 9. Directions 9 and 13 meet here.

## 3. Why it could break Davenport-Heilbronn (K2)

A tau-function satisfies the Hirota/Plücker bilinear identities; a generic entire function does not. The Euler product is conjecturally the multiplicative structure that makes $\xi$ integrable (a tau-function). D-H, lacking the Euler product, should **fail** the Hirota relations, equivalently its Jensen polynomials should fail hyperbolicity / its Taylor coefficients should violate the Turan inequalities. Crucially this is **checkable now**: the off-line zeros of D-H give $\Xi_{DH}$ genuinely complex zeros, so a finite Jensen polynomial / Turan test at a sufficiently sensitive index must detect non-real roots.

## 4. Kill-criteria status

- **K1 (signature not trace):** clean. The Riemann bilinear relations are a Hodge-index signature, and the Turan inequalities are log-concavity (degree-1 Hodge-Riemann), neither a trace identity.
- **K2:** clean and *testable today* (Hirota/Turan failure for D-H).
- **K3:** for a curve over $\mathbb{F}_q$, the finite-genus tau-function recovers the classical Riemann bilinear relations and Weil's Hodge index. Milestone 13.3.

## 5. First step (cheap, decisive: landed alongside this doc)

Experiment [`e_jensen_turan.py`](../../../experiments/integrable/e_jensen_turan.py):

1. Compute the Taylor coefficients of $\Xi(z) = \xi(1/2+iz)$ and of the completed D-H function $\Xi_{DH}(z)$ to high precision.
2. Test the **Turan inequalities** (degree-2 Jensen hyperbolicity) and the hyperbolicity of higher Jensen polynomials $J^{d,n}$.
3. Ask whether $\zeta$ satisfies them (GORZ 2019 proved eventual hyperbolicity) and whether D-H **violates** them, and at what index / precision (the stealth-window analysis, cf. LEARNINGS #18/#19).

**Decision rule.** If D-H violates Turan/hyperbolicity at a reachable index while $\zeta$ satisfies it, Direction 13 yields a new integrable-systems D-H discriminator and earns the tau-function construction effort. If the off-line perturbation is below the detection floor at reachable indices (likely, given the off-line zeros sit at height $85.7$), the finding is the stealth-window wall in the Jensen basis: a compass reading consistent with marginal positivity.

## 6. Honest assessment

Probability of closing RH: low, but the bridge to the Jensen/Turan framework is rigorous and active (GORZ 2019), and the tau-function hypothesis for $\xi$ connects RH to a vast, well-developed machine (KP/Toda hierarchies, Sato Grassmannian, isomonodromy). The realistic payoff is a sharp computable D-H discriminator and a precise statement of "what integrable structure $\xi$ would need to have."

## 7. References

- Segal, G.; Wilson, G. (1985). *Loop groups and equations of KdV type*. Publ. Math. IHES 61.
- Sato, M.; Sato, Y. (1983). *Soliton equations as dynamical systems on infinite-dimensional Grassmann manifold*.
- Krichever, I. M. (1977). *Methods of algebraic geometry in the theory of nonlinear equations*. Russian Math. Surveys 32.
- Feldman, J.; Knorrer, H.; Trubowitz, E. (2003). *Riemann surfaces of infinite genus*. CRM Monograph 20.
- Griffin, M.; Ono, K.; Rolen, L.; Zagier, D. (2019). *Jensen polynomials for the Riemann zeta function and other sequences*. PNAS 116(23).
- Csordas, G.; Norfolk, T. S.; Varga, R. S. (1986). *The Riemann hypothesis and the Turan inequalities*. Trans. AMS 296.
