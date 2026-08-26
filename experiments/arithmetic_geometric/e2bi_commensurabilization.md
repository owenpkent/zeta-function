> Filed 2026-08-26 as regression infrastructure under the #201 closed-bank clause (salvaged from PR #8; LEARNINGS #210): a re-measurement instrument, not a finding; no frame session grading.

# e2bi: the function-field costume (commensurabilization)

**Date**: 2026-08-26. **Status**: EXECUTED, 7/7 full and quick; all three pre-registrations FIRED. **Gallery**: G3 of [`construct_gallery.md`](../../docs/03_research/construct_gallery.md).
**Label (per the #201 derivability check)**: re-measurement of the wall (the commensurability face of #162/#172/#188), with one new closed-form constant ($\pi$) for the trade. No new coordinate claimed.

## What was built (deliberately wrong)

The F_q import done literally: quantize $b_p = \exp(\mathrm{round}(D\log p)/D)$ so every $\log b_p \in \tfrac1D\mathbb{Z}$, making the system fully commensurable (a generalized-prime system with "$q$" $= e^{1/D}$), on the ladder $D \in \{2,4,\dots,128\}$ over the 1229 primes to $10^4$, substrate = the shared `BeurlingSystem` class with the log table overwritten.

## Results

1. **The Frobenius costume is real.** The snapped truncated Euler product is EXACTLY periodic in $t$ with period $2\pi D$ (measured $\le 1.1\times10^{-14}$ at every $D$; the true primes differ by $\ge 0.19$ at the same offsets). Commensurability literally buys the function-field structure: a one-parameter Frobenius, zeros on progressions, the whole Weil-side geometry.
2. **The trade law, exact.** Max snap jitter is $\le \tfrac1{2D}$ (attained up to sampling: measured products $3.140$-$3.142$ across the ladder), and the imported structure lives at height $H(D) = 2\pi D$, so $(\text{max jitter}) \times (\text{structure height}) = \pi$ **independent of $D$**. Corollary measured as the height-budget gate: seeing the imported periodicity below zeta's first zero ($\gamma_1 = 14.13$) forces $D \le 2.25$, where the jitter bound is $0.22$: the scale of the default Beurling fake's $\varepsilon = 0.25$ (e2ak). Full arithmetic fidelity pushes the F_q structure above every fixed height; the F_q proof does not transfer for a priced reason.
3. **The lattice cost rides along.** The e2ak drift meter on the snapped systems: drift $1061$ at $D = 2$ down to $10.3$ at $D = 128$ (ratio 103), true integers at $0.524$: the #198 continuity of finite meters, here along the quantization axis. Collisions (distinct primes snapping to one atom) fall monotonically ($1211 \to 799$) but persist at $D = 128$ because prime log-spacings at $p \sim 10^4$ are below $\tfrac1{256}$.

## Reading

Both wrong-approach detectors are one parameter family away from zeta in opposite directions: jitter OFF the integers gives the Beurling fake (e2ak/e2bc), quantization ONTO a coarser common lattice gives the function-field costume, and the trade $\tfrac1{2D} \cdot 2\pi D = \pi$ says you cannot have arithmetic fidelity and low-lying commensurable structure at once. This is the $\mathbb{Q}$-linear-independence wall (#162, #172's density obstruction, #188's horizon law) with the price displayed as one constant.

## Pre-registrations

- P1 FIRED: measured jitter $\times\ 2\pi D \in [0.85\pi, \pi]$ for all $D \ge 4$.
- P2 FIRED: exact $2\pi D$-periodicity for the snapped product, aperiodicity for the true primes.
- P3 FIRED: drift(2) $> 3\times$ drift(128) (measured 103x), integer control $< 1$.

## Artifacts

[`e2bi_commensurabilization.py`](e2bi_commensurabilization.py) (7/7), tracked npz alongside.
