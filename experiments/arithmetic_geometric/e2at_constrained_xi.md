# E2AT: the pole-constrained ladder refutes the naive reconciliation, and the boundary fact reframes the whole (1.2) comparison

**Date**: 2026-08-20. **Status**: BUILDER round, executed; 4/4 checks after retyping to the measured outcome (241 s). **Code**: [`e2at_constrained_xi.py`](e2at_constrained_xi.py). **Data**: `e2at_constrained_xi.npz` (tracked). **Trigger**: B2c-lit: pulling CCM "Zeta spectral triples" (arXiv:2511.22755, Suzuki's [4]) revealed their kernel construction imposes the vanishing-integral (pole) condition, which our #185 instrument did not: the candidate explanation for the measured narrowing.

## 0. What happened, in order

1. **The hypothesis**: #185's narrowing (the unconstrained hard-window bottom concentrating toward the origin) might be an artifact of omitting the pole condition $\hat v(i/2) = 0$ that CCM impose; the constrained bottom might stay on $\Xi$, reconciling everything.
2. **The run refuted it**: with the constraint imposed exactly (closed form $b_k = \hat\psi_k(i/2)$, residuals $10^{-81}$), the constrained bottom's $z{=}0$-normalized ratios EXPLODE (17 to 319 at $a = 1$): the constrained minimizer suppresses $\hat v(0)$ and moves its lobe off-center; nothing passes the convergence gate at matched resolution.
3. **The diagnosis found the structural fact** (mp-verified in the checks): $\Xi(i/2) = \xi(0) = 1/2 \neq 0$. **The xi function itself violates the pole constraint.** So (1.2)'s conjectured limit lives OUTSIDE the constrained space, and CCM's own convergence (their Lemma 7.3: $\hat k_\lambda \to \Xi$) is stated uniformly on closed substrips of the OPEN strip $|\Im z| < 1/2$: interior-only, with the constraint's pinch squeezed to the boundary as $\lambda \to \infty$. At our small windows the pinch contaminates the whole real axis, which is exactly what the exploded ratios show.

## 1. The three-object split (the round's real yield)

The (1.2) circle involves at least three distinct finite-$a$ objects our instruments have now separated experimentally:

- **The unconstrained bottom** (Suzuki's $A_a$ as literally defined on $C_c^\infty(-a,a)$; #184/#185): certified, basis-converged, and it NARROWS through the xi shape near $a \approx 1$.
- **The pole-constrained bottom** (the space CCM's kernel construction lives in; this round): measured, basis-unconverged at matched resolution, $z{=}0$-normalization meaningless for it; its honest comparison to $\Xi$ must be an INTERIOR fit (away from the boundary pinch), which is not yet built.
- **CCM's explicit kernel $k_\lambda$** (constrained by construction, with $\hat k_\lambda \to \Xi$ interior-uniformly per their Lemma 7.3, and their numerical evidence that $k_\lambda$ approximates their ground state).

Which object (1.2)'s $v_a$ IS: Suzuki's text defines $A_a$ from $Q_W^a$ on the unconstrained window space, while attributing (1.2) to CCM whose analysis is constraint-side. The literature's two presentations are not obviously the same variational problem at finite $a$, and our measurements show the two bottoms differ grossly at accessible windows. That identification question, plus the interior-fit comparison for the constrained object, is the successor (B2c-obj); the expensive $a = 3$-$5$ ladder (B2c-deep2) is BLOCKED behind it, since it must be run on the right object.

## 2. Amendment to #185's wording

#185 stands as a measurement of the UNCONSTRAINED bottom with its certificates. Its framing sentence "the approach to Suzuki (1.2) is non-monotone" now carries the qualifier: for the unconstrained object. Whether that object is (1.2)'s $v_a$ is exactly the open identification above. The novelty caveat is also updated: CCM [4] is now in the library; it contains numerics (their Section 6: $D_{\log}$ spectra vs zeros; Section 7: $e_n(\mu)$ curves and kernel-vs-ground-state proximity) but no direct measurement of the unconstrained bottom's shape, so #185's "first certified probe" claim survives re-scoped to the unconstrained object.

## 3. Hand-off

(i) **B2c-obj**: settle the object identification (read CCM's Section 3/5 definitions of $Q_{W\lambda}$'s domain at source; determine whether Suzuki's $A_a$ and CCM's $\xi_\lambda$ solve the same problem) and build the interior-fit comparison for the constrained bottom (fit against $\Xi$ on $z \in [4, 10]$ with the basis-convergence gate; the constrained problem needs higher resolution than matched-$m$); (ii) then B2c-deep2 on the settled object; (iii) the P12 packaging now includes this round: the arc's story is stronger for having caught its own naive reconciliation.
