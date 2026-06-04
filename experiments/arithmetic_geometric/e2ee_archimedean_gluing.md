# 2EE: the archimedean continuation block and the gluing (probe B)

> Companion for [`e2ee_archimedean_gluing.py`](e2ee_archimedean_gluing.py). Executes probe B of [`docs/03_research/backwards_from_2050.md`](../../docs/03_research/backwards_from_2050.md): build candidate A's named dependency (the archimedean continuation block, = candidate B's fiber) and attempt the gluing to the local finite/prismatic blocks. Run: `python -m experiments.arithmetic_geometric.e2ee_archimedean_gluing`.

## The setup

Probe 1 (2DD, LEARNINGS #43) sharpened candidate A to: the local $(1,p)$ prismatic blocks have room for a signature but are blind to the global continuation, so candidate A needs the **archimedean continuation block** (C4 / candidate B) glued to the finite blocks. Probe B prototypes that gluing on the project's already-validated non-circular Weil form $M = A_{\mathrm{arch}} + P_{\mathrm{fin}} + B_{\mathrm{pole}}$ (#33/#34).

**The structural observation that makes this worth running:** the pole block is, by construction, $B_{\mathrm{pole}} = \mathrm{residue}\cdot 2\cdot \phi_1\phi_1^{\!\top}$, a **rank-1** form. For $\zeta$ the residue is $1$ (rank-1 positive); for Davenport-Heilbronn the residue is $0$ (it is entire, so $B_{\mathrm{pole}} = 0$). That is exactly the silhouette of a Hodge-index / Lefschetz decomposition: the pole direction $\phi_1$ is the **ample / fundamental-class "+1"** (present for $\zeta$ via the Euler-product residue, absent for D-H), and the **primitive part** is $M$ restricted to $\phi_1^{\perp}$, the $H^1$ where the nontrivial zeros and RH live. This is the arithmetic image of the function-field $(1,\rho-1)$ signature on $C\times C$ (2G), and it is non-circular (the residue is elementary).

## Results

### (1) The archimedean fiber in isolation (the Connes-match check)

Candidate B claims the archimedean fiber's polarization is Connes-Consani's *proven* archimedean Weil positivity (the Sonin-space trace, arXiv:2006.13771). Test: is the validated $A_{\mathrm{arch}}$ positive on the pole-orthogonal complement $\phi_1^{\perp}$ (a naive Sonin condition)?

| target | sig($A_{\mathrm{arch}}$) | min eig | sig($A$ on $\phi_1^{\perp}$) | min eig\|perp |
|---|---|---|---|---|
| zeta | (7,3,0) | $-55.2$ | (7,2,0) | $-2.52$ |
| DH | (9,1,0) | $-5.79$ | no pole dir | n/a |

**Finding (honest negative): the naive Connes-match is NOT confirmed.** $A_{\mathrm{arch}}$ is indefinite for $\zeta$ even after removing the pole direction (still 2 negatives). So pole-removal in the Bombieri $b$-basis is *not* Connes' Sonin space, and the archimedean fiber is not positive in isolation. This does not refute Connes (his theorem holds in its own functional-analytic space, with both endpoint conditions and the prolate structure, not a single rank-1 projection in this basis); it says **the naive prototype is too coarse to see his positivity**. The robust content: positivity is **global**, not a property of the archimedean fiber alone (the two-clock balance, #23). The archimedean block must be glued to the finite block before any positivity appears, which is precisely why candidate B needs a single interpolating period.

### (2) The gluing as a Hodge-index (the stealth-window check)

| target | min eig($M$) | min eig(primitive) | has ample? |
|---|---|---|---|
| zeta | $+0.0262$ (POS) | $+0.0262$ (POS) | yes |
| DH | $+0.0840$ (POS) | $+0.0840$ (POS) | NO (no pole) |

**Finding: the stealth window persists, exactly as #34 predicted.** Projecting out the ample/pole direction (a non-circular move) does **not** manufacture the RH-vs-off-line discrimination: both $\zeta$ and D-H read positive (D-H spuriously, since it fails RH). D-H's off-line obstruction ($\gamma\approx 85.7$, $\sim 2.6\%$ of the spectrum) stays below the reconstruction floor at reachable truncation. So the gluing-as-**trace** (the explicit formula) is built and carries the right Hodge-index **silhouette** (a rank-1 ample pole plus a primitive part), but the gluing-as-**signature** (the genuine duality whose positivity is RH) is the analytic M4 gap, unchanged. A finer numerical truncation will not close it.

**K2 in the gluing language (a clean new face):** D-H has residue $0$, hence no pole, hence **no ample fundamental class** at all. $\zeta$'s ample "+1" is the Euler-product residue at $s=1$. So the fundamental class is exactly the object D-H lacks. This is the C2 (D-H-unbuildable) discipline expressed inside the gluing: the missing organ for D-H is the very direction that anchors the Hodge index for $\zeta$.

### (3) The named obstruction

The gluing assembles archimedean + finite + pole as a trace (the explicit formula). To be a Hodge-index **signature** over $\mathrm{Spec}(\mathbb{Z})$ it needs two organs, now pinned by name:

- **A fundamental class $H^2$** (a trace map $H^1\otimes H^1 \to H^2 = \text{unit}$). The ample/pole direction is its rank-1 shadow here, but a genuine $H^2$ with Poincare duality is the open prismatic-duality step (candidate A's dependency (i)).
- **A single interpolating period** reconciling the two clocks: the archimedean place runs on the additive/log scale (the $\Gamma$-factor), the finite places on the multiplicative scale $p$ (the $(1,p)$ bidegree, #25). Candidate B's archimedean Fargues-Fontaine would supply one curve carrying both; the missing number is the period that glues additive to multiplicative (candidate A's dependency (ii) = candidate B).

These two together **are** milestone M4.

## Verdict

Probe B confirms the gluing's silhouette is a Hodge index (rank-1 ample pole + primitive part, with the ample class present for $\zeta$ and absent for D-H), reproduces the stealth window (M4 is analytic, unchanged), and returns one honest negative (the naive pole-removal is not Connes' Sonin space, so the archimedean fiber is not positive in isolation: positivity is global). Net: candidate A+B's missing organs are now named precisely (the $H^2$ fundamental class and the two-clock interpolating period), and the front is unchanged in location but sharper in description.

## Honest scope

The blocks $A_{\mathrm{arch}}, P_{\mathrm{fin}}, B_{\mathrm{pole}}$ are the project's validated non-circular Weil form (#33/#34); real, reproducing the explicit formula. The Hodge-index **reading** (pole = ample +1, complement = primitive) is a structural proposal, the arithmetic image of 2G; it is not a constructed prismatic Poincare duality and proves nothing about RH. The Connes-match negative is about the naive prototype, not Connes' theorem. No new theorem; a sharpening coordinate that names the two missing organs.

## Pointers

- Parent: [`docs/03_research/backwards_from_2050.md`](../../docs/03_research/backwards_from_2050.md) (candidates A and B; probe B).
- Builds on: [`e2dd_prismatic_cup_room.py`](e2dd_prismatic_cup_room.py) (2DD / #43), [`e2w_rosati_fourway_M2_6.py`](e2w_rosati_fourway_M2_6.py) (M2.6 / #34), [`e2v_rosati_balance_M2_5.py`](e2v_rosati_balance_M2_5.py) ($A_{\mathrm{arch}}$ / #33), [`../positivity/e3m_place_type_balance.py`](../positivity/e3m_place_type_balance.py) (the blocks).
- Findings leaned on: #33/#34 (the Weil form, the stealth window), #23 (two-clock balance), #25 (bidegree), #42 (local-to-global blindness).
