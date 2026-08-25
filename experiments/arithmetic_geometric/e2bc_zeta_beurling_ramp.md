# E2BC: the zeta-to-Beurling ramp: the meters are linear in the jitter, the knee is set by the data, and the Euler clause never breaks

**Date**: 2026-08-24. **Status**: BUILDER round, executed; 8/8 checks (13 s). **Code**: [`e2bc_zeta_beurling_ramp.py`](e2bc_zeta_beurling_ramp.py). **Data**: `e2bc_zeta_beurling_ramp.npz` (tracked). **Executes**: backlog A4 (the last Family-A item: Family A COMPLETE). **K1 posture**: FULLY CLEAN (zero oracle calls at any phase: the meters are lattice-side functionals only). **Bracket**: the $t = 1$ endpoint IS the counting-side control; D-H (form-side) does not pose on an Euler-side ramp (typed).

## 0. The instrument

$b_p(t) = p\,e^{t\varepsilon_p}$ with the standard fake's jitter directions ($\varepsilon = 0.25$, seed 149), base = ALL primes up to the data depth, so $t = 0$ is EXACTLY the integer lattice and $t = 1$ a full Beurling fake; every intermediate $t$ is a free semigroup. Three e2an meters per rung: truncation drift, duality defect (zeta's own completion), von Mangoldt defect.

## 1. The measured ramp ($X = 60000$)

| $t$ | 0 | $10^{-3}$ | $3\times10^{-3}$ | $10^{-2}$ | $3\times10^{-2}$ | $0.1$ | $0.3$ | $1.0$ |
|---|---|---|---|---|---|---|---|---|
| drift | $2.2\times10^{-12}$ | $1.1\times10^{-3}$ | $2.8\times10^{-3}$ | $8.9\times10^{-3}$ | $2.6\times10^{-2}$ | $0.127$ | $0.225$ | $0.521$ |
| duality | $2.4\times10^{-11}$ | $3.4\times10^{-3}$ | $1.0\times10^{-2}$ | $3.4\times10^{-2}$ | $0.104$ | $0.315$ | $0.587$ | $0.666$ |
| vM | $8.9\times10^{-16}$ | $1.8\times10^{-15}$ | $1.8\times10^{-15}$ | $1.8\times10^{-15}$ | $1.8\times10^{-15}$ | $1.8\times10^{-15}$ | $1.8\times10^{-15}$ | $2.7\times10^{-15}$ |
| $A$ | $1.0000$ | $1.0003$ | $1.0012$ | $1.0037$ | $1.0115$ | $1.0393$ | $1.1251$ | $1.5864$ |

Endpoints: the $t = 0$ column is the e2an zeta class; $t = 1$ reproduces the e2an Beurling class to two digits (drift $0.521$ vs $0.51$; duality $0.666$ vs $0.665$; $A = 1.5864$ vs $1.5856$) despite a different prime base: the classes are configuration-robust.

## 2. The three pre-registered laws, all landed

**[P1] No cliff: the meters are LINEAR in the jitter.** Log-log slopes over two decades: drift $0.974$, duality $0.926$; monotone throughout. A $0.1$-percent log-jitter already lifts the drift NINE orders above the integer floor: the integers are not a distinguished point of any finite meter except through its precision floor. The pre-registered kill (a cliff at $t = 0$, which would have meant a finite instrument sees the arithmetic 0/1) did NOT fire.

**[P2] The knee is set by the data meter.** The integer floor is depth-dependent (drift floor $3.95\times10^{-8}$ at $X = 15000$ vs $2.21\times10^{-12}$ at $X = 60000$), so the departure point $t^*(X) = 3\,\mathrm{floor}/\mathrm{slope}$ moves four-plus orders with depth ($\sim2.2\times10^{-7}$ vs $\sim1.3\times10^{-11}$): where "arithmetic becomes visible" is a property of the DATA BUDGET, not of the lattice.

**[P3] The Euler clause never breaks.** The von Mangoldt identity is exact ($\le 2.7\times10^{-15}$) at every $t$ including $1$: the ramp is a pure lattice-clause instrument, the clean complement of the D-H side (FE without Euler).

## 3. The typing (the round's coordinate)

This completes the counting-side continuity trilogy: **pointwise** (#172: no continuous Christoffel functional of atom positions sees $\mathbb{Q}$-linear independence, since lattices are dense), **sequence-level** (#188: the Szego register is arithmetic-blind below its collision horizon, priced at $\sqrt{2DL}$), and now **instrument-level** (A4: the assembled descent/duality meters are LINEAR in the prime positions, with the visibility threshold set by the data meter). At every register, finite-scale functionals are continuous in the lattice while the arithmetic distinction is a 0/1 at the limit: arithmetic enters finite instruments only through floors and limits: the S4/R1 coordinate (#162) confirmed on the assembled object's own meters, and the counting-side face of the week's uniform message (#191's horizon, #195's priced discrimination).

## 4. Scope and caveats

One jitter realization (seed 149: the standing control's directions: the slopes are jitter-scale laws, not direction-specific, but a second seed was not swept); the duality floor at $t = 0$ ($2.4\times10^{-11}$) reflects the shared quadrature of the completed multiplier, not an arithmetic statement; $t^*$ is a linear-model estimate from (floor, endpoint), not a measured crossing (the grid brackets it consistently). Frontier verdict: UNMOVED (a controls/typing round; Family A closes with all four corners plus the ramp between them measured through one pipeline).

## 5. Hand-off

(i) Family A is COMPLETE (A1 Cramer / A2 S-finite / A3 implant / A4 ramp); the backlog's remaining open items are the hardening tier (B1/B3/B4/B2d). (ii) The ramp instrument is reusable as a calibration axis: any future counting-side detector claim should quote its $t$-sensitivity and floor. (iii) Optional cheap extension if ever needed: a second seed and a per-prime-subset ramp (jitter only $p > P_0$) to type WHICH primes carry the meters' sensitivity.
