# E2BF: the frontier-capacity function (backlog B2d): the node schedule is universal, and the margin face is attainment-limited with certificates

**Date**: 2026-08-25. **Status**: BUILDER round, executed; final full run 8/12 with the four FAILing gates being the finding (the margin face's attainment limit, recorded with certificates; the node-schedule face is green). **Code**: [`e2bf_frontier_capacity.py`](e2bf_frontier_capacity.py). **Data**: `e2bf_frontier_capacity.npz` (tracked; full run). **Provenance**: backlog B2d, reclassified BANK MAINTENANCE by the #201 frame audit; hardens the #183 frontier law's capacity axis.

## 0. What survived and what the instrument confessed

Two faces were measured. The NODE-SCHEDULE face is solid and delivers B2d's content; the MARGIN face is not measurable by this solver family beyond the #183 regime, and the build proves that about itself with certificates. Both are deliverables.

**The node-schedule face (green):**

- **P2 FIRED: the per-zero precision schedule is UNIVERSAL.** Across all five configurations (capacity axis $J = 18, 35, 53$ at $\Omega = 34$; ceiling axis $\Omega = 27, 34, 41$ at unit grid), the graded profile costs **5.1-6.9 decades of node precision per zero (spread 1.34x)**: the #183 "about six decades per zero" is a capacity-independent law of the family.
- **The frontier is ceiling-monotone**: dead cut at $\gamma_9$ / $\gamma_{12}$ / $\gamma_{14}$ for $\Omega = 27/34/41$ (gated).
- **#183 reconciled by a sharper typing.** #183's "frontier $\gamma_8$" is SLOPE-SELECTED (the zero whose leak carries the margin; its node is still $10^{-23}$-alive); the graded profile's DEAD cut ($> 10^{-12}$) sits at $\gamma_9$, exactly #183's own table. Both are level-set readings of one graded object; the sweep's reference gates reproduce #183's table at its own working precision.
- **Node depths are working-precision-relative; the selection is not** (gated): at dps 50 the dead cut is $\gamma_9$, at dps 80 it is $\gamma_{12}$ with $\gamma_6, \gamma_7$ at $10^{-42}$: annihilation depth is an artifact of the arithmetic register; which zero carries the margin is not.

**The margin face (the confession, with certificates):**

- The nested-capacity control (P3) fired at dps 50, fired AGAIN at dps 80 in the opposite direction with the reference margin moving 14 orders between precisions, and, decisive, fired on **certified Rayleigh quotients** (each returned vector evaluated directly against fresh $Q, G$ at dps 140): attained lg margins $-83.8 \to -70.4 \to -55.4$ along $J = 18 \subset 35 \subset 53$. Since the certificates are true upper bounds, the $J = 18$ attainment proves every larger space's true bottom is $\le 10^{-83.8}$, so the larger solves are simply NOT FINDING it: **Cholesky-whitened eigsy attainment degrades with $J$ under the mode Gram's conditioning**, and eigsy's reported value disagrees with its own vector's certified quotient by up to 12.3 decades. Every margin-derived quantity of this family (slopes included) is therefore solver-attainment, not spectrum, outside the #183 corner; #183's own five-point law keeps its independent internal evidence (2 percent mechanism match) and is neither reproduced nor refuted here: flagged ATTAINMENT-LIMITED.
- **P1 (overshoot nondecreasing in spare capacity) is ATTAINMENT-CONFOUNDED**: monotone $4 \to 5 \to 6 \to 6$ over $S = 13..35$, then 5 at $S = 48$, where the certified margin shows the solver 15+ orders short of optimal: the outlier's node profile belongs to a non-optimal vector. The spare-capacity law stands on the attained range and is open beyond it; recorded, not iterated (the bank is closed to new probes).

## 1. Placement

B2d's deliverable was the capacity function and the per-zero cost schedule. Delivered: the schedule (universal, 5-7 decades/zero), the ceiling-monotone frontier, the level-set/slope-selection typing that reconciles #183, and the dps-relativity of annihilation depth. The margin face's attainment no-go is the build's instrument finding, of direct use to any future SP5 numerics: **certified-vector Rayleigh evaluation is mandatory; eigenvalue readouts of near-degenerate localized families are not data**. This is the #184/#185 precision-starvation class promoted to a certified statement about the solver pipeline itself.

## 2. Honest scope

Zero-side instrument by design (the zero list is the counted input, as in e2aq); nothing here feeds a construction cell or touches the frontier. The five FAILing/refuted items in the final run's own table are the record of the confession, kept deliberately (the harness pattern: a fired control is a result). Frontier UNMOVED.
