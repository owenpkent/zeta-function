# E2AZ: the wrong polarization, built anyway: three metrics, one measured trilemma, and M4 as a vanishing-locus statement

**Date**: 2026-08-23. **Status**: BUILDER round, executed; 12/12 checks (2.2 s). **Code**: [`e2az_wrong_polarization.py`](e2az_wrong_polarization.py). **Data**: `e2az_wrong_polarization.npz` (tracked). **Executes**: backlog B2. **Joint**: C2 (SP5). **K1 posture**: build phase 0 oracle calls; zeros only in validation; each metric's own data consumption is the measured content.

## 0. The setting and the demands

On the e2an v0 object (multiplier $m(\tau)$ extracted from integers, cokernel = the dip modes, flow = $\mathrm{diag}(\tau)$ compressed there), SP5 asks for a polarization. Since every candidate metric here is diagonal, self-adjointness-with-the-right-spectrum is FREE ([B2-1]): the discriminating content lives in three demands distilled from the 7-property spec:

- **D1** (P6/P7 face): positive metric mass on the primitive (dip) part;
- **D2** (P3/K1): no zero locations consumed, neither as weights nor as support selection;
- **D3** (P4): Euler-sourced: the construction separates zeta from D-H.

## 1. The three candidates, cell by cell (all measured)

**FLAT (L$^2$ restricted to the dip modes) $= (D1, \neg D2, \neg D3)$.** Its Gram on the e2an test family equals the PRIME-SIDE-ASSEMBLED Weil Gram to $2.5\times10^{-5}$: the flat metric on the cokernel IS the Weil form: positivity by restatement, with the zero locations consumed at the support-selection step. And the identical construction passes on D-H (on-line hit rate $1.00$) while D-H's RH is false: the P4 firewall catches the whole class. Its eigenvalues reproduce e2an's SP5 cell ($[-3.6\times10^{-16}, 1.27]$: the marginal bottom).

**PULLBACK ($\langle f,g\rangle_{\mathcal E} = \langle \mathcal E f, \mathcal E g\rangle$, weights $|m(\tau)|^2$) $= (\neg D1, D2, D3)$.** K1-clean (m is integer-extracted) and Euler-sourced, and its mass sits EXACTLY off the primitive part: median dip weight $1.16\times10^{-7}$ against bulk $1.54$: ratio $7.5\times10^{-8}$. The #170 law measured inside the object: the GNS/state costume is free exactly where it is information-free. It does see completeness structurally: at D-H's off-line landmark the weight FAILS to vanish ($0.058$ relative, against zeta's $7.5\times10^{-8}$ at true dips): it detects the D-H pathology without certifying anything positive about it.

**CHRISTOFFEL (CD-kernel weights of the emergent atomic measure) $= (D1, \neg D2, \neg D3)$.** Concentration on the atoms onsets exactly when the degree reaches the atom count (midgap/atom $K$ ratio $0.98 \to 1.04 \to 22.1$ at $M = 10, 20, 28$ with 29 atoms: the resolution threshold, #172's physics) and the off-atom blowup of $K_M$ is the uniform growth clause (#160/#171) surfacing inside the object. Its defining data ARE the dip locations (the K1 ledger line), and the D-H twin concentrates on ITS dips identically (311x at full resolution): the D1-satisfiers are firewall-blind. The K1-CLEAN SURROGATE (the same construction on the location-free measure $|m|^2 d\tau$) puts LESS Christoffel weight on the dips ($K$ ratio $1.269$: a 21 percent weight deficit at $M = 28$): removing the location input restores the #170 law.

## 2. The trilemma, and coordinate system #4

| metric | D1 primitive-positive | D2 K1-clean | D3 Euler contact |
|---|---|---|---|
| flat | yes | no (support) | no (D-H hit 1.00) |
| pullback | no ($7.5\times10^{-8}$) | yes | yes (landmark 0.058) |
| christoffel | yes | no (weights) | no (D-H 311x) |

No candidate solves all three (the pre-registered kill did not fire), and the structure is sharper than a trilemma: **within this family, D1 implies both failures.** Primitive positivity is purchasable only from the dip set; the dip set is FE-side data shared with D-H; and the Euler-side data, the multiplier values, VANISH exactly on it.

**Coordinate system #4 for M4** (after variational / lattice-Hamburger / Weyl-spectral-chain, #171): in the assembled object's own coordinates, M4 is the demand that **the Euler side fund positivity precisely on the locus where its own transform vanishes.** The conservation law (#148/#170: Euler product $\wedge$ additive lattice consumed at one joint) becomes a vanishing-locus statement: the K1-clean data $|m|^2$ is identically zero where the positivity is needed, so any funding must come through a limit/uniformity structure (the derivative $|m'|^2$ at the dips, the growth clause across scales) rather than through values: which is exactly where #160's growth clause and the CCM determinant-class clause (#148) already live. Resonance with #191, noted: the e2aw kernel whose full-line transform vanishes at every zero is the same vanishing-locus geometry seen from the trial-state side: there it makes the kernel an exponentially good state; here it makes the Euler values unable to pay at the dips. Two faces of one locus.

## 3. Scope and caveats

Finite scale throughout (dips to $\tau = 100$ at $1.3\times10^{-4}$ localization; assembly errors at the e2an protocol's $10^{-4}$-$10^{-5}$); the trilemma's D-entries are measured for THESE three constructions plus the surrogate, not proven for all metrics (the family is the backlog's named candidates; the D1-implies claim is a measured pattern with a structural reason, not a theorem); diagonality makes self-adjointness free, so nothing here tests non-diagonal (genuinely operator-theoretic) polarizations: that is the CCM Section-7/C3 territory, deliberately untouched. Frontier verdict: UNMOVED (a typing round; the deliverable is the coordinate system).

## 4. Hand-off

(i) The vanishing-locus coordinate is the sharpest one-sentence M4 statement the object owns; candidates for **C3** (the CCM Section-7 determinant-family audit) should be scored against it first (does the determinant class fund the dips through values or through uniformity?). (ii) The pullback's completeness sensitivity (vanishing-set = on-line zeros only) is a cheap standing diagnostic: any candidate metric can be screened by where its degeneracy locus sits on the D-H column. (iii) A VERIFIER-shaped nugget: "no nonnegative diagonal metric with weights from $|m|^2$-values has mass on the zero set of $m$" is trivially formal; the useful target is the finite-scale quantitative version with the derivative funding (the $|m'|^2$ channel), left named. (iv) B2 is struck; the remaining backlog: hardening tier (B1/B3/B4/B2d), heavy tier (C2/C3/C4).
