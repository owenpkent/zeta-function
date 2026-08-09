# E1V: the Christoffel gauge. Is the germ-length blowup arithmetic or geometry?

**Date**: 2026-08-08. **Role**: BUILDER (this probe), executing the LEARNINGS #171 handed-forward item 2 / [`PHASE_STATE.md`](../../PHASE_STATE.md) "Next steps" item 2 (the Christoffel-corpus rung) as a **local build** rather than a literature sweep, and discharging [`e1u`](e1u_canonical_chain.md) VERIFIER target 6. **Status**: built and adversarially probed in one session; 23/23 self-tests full and quick; ADVERSARY round **self-run** ([`_e1v_adversary.md`](_e1v_adversary.md), 5 attacks run + 1 unposed, none landed, one closed an open item, one independently confirmed V7), with cases 3 and 7 **not run and open**. No second party has read this rung.

**Artifacts**: [`e1v_christoffel_gauge.py`](e1v_christoffel_gauge.py) (23/23 full, ~5 s warm; 23/23 quick, ~0.3 s, saves nothing and does not clobber the npz, md5-verified), `e1v_christoffel_gauge.npz` (full mode only; byte-reproducible across consecutive runs, md5-verified), shared build cache `_cache/e1t_build_*.npz` (gitignored; a cold machine pays ~5.5 min for the 12-build grid, measured).

**Verdict in one line**: `christoffel_gauge_carries_arithmetic = NO, POINTWISE`. The germ-length blowup that e1u measured is now a **theorem with an explicit potential-theoretic rate** that depends only on $(g, T, M)$, the tightness residual is **family-blind once the gap is equalized** (means 1.21 / 1.31 / 1.53, spread 1.27x), and the whole functional is **provably unable to see $\mathbb{Q}$-linear independence** because it is continuous in the atom positions while lattices are dense (demonstrated: snapping the true zero set onto $(1/D)\mathbb{Z}$ moves the per-atom rate by $\le 2.4\cdot 10^{-8}$ at $D = 10^6$, uniformly in $M$). The corpus question as posed ("any mechanism giving $\lambda$-uniform Christoffel control at a point, for an Euler + lattice reason") is therefore **closed at the pointwise/finite-$\lambda$ level** and must be re-aimed at limit-level instruments (sum rules), which is where Killip-Simon already lives.

## What this rung adds (in decreasing order of durability)

### 1. An exact identity, then a theorem

The e1u footprint chain's total trace-length is not merely "like" a reciprocal Christoffel function. It **is** one, plus a second-kind twin:

$$X_{\text{total}} = \sum_k |u_k|^2 = \sum_k p_k(0)^2 + \sum_k q_k(0)^2 = \frac{1}{\lambda_M(0)} + Q_M(0),$$

with $p_k, q_k$ the first/second-kind orthonormal polynomials at the footpoint and $\lambda_M$ the Christoffel function of the normalized input measure. Since $Q_M \ge 0$, $X_{\text{total}} \ge 1/\lambda_M(0)$ exactly. A second, **independent** route (pure Lagrange interpolation, no Lanczos and no recurrence anywhere) evaluates the same number as

$$\frac{1}{\lambda_M(0)} = \sum_j \frac{\ell_j(0)^2}{w_j}, \qquad \ell_j = \text{Lagrange basis at the atoms},$$

exact at full degree $M-1$: with $M$ atoms the degree-$\le M-1$ polynomials exhaust all functions on the atoms, so the Christoffel extremal problem **is** an interpolation problem. The two routes agree to $7\cdot 10^{-50}$ on every build-face (V1b). Neither is a fit.

> **THEOREM V2.** Let $\mu = \sum_j w_j \delta_{y_j}$ be a probability measure with $M$ atoms, all with $g \le |y_j| \le T$, $0 < g < T$. Put $n = \lfloor (M-1)/2 \rfloor$ and
> $$G \;=\; \tfrac12 \operatorname{arccosh}\frac{T^2+g^2}{T^2-g^2}$$
> (the Green's function of $\mathbb{C} \setminus (\pm[g,T])$ at $0$, pole at $\infty$). Then
> $$\lambda_M(0) \;\le\; \cosh(2nG)^{-2}, \qquad\text{hence}\qquad X_{\text{total}} \;\ge\; \frac{1}{\lambda_M(0)} \;\ge\; \cosh(2nG)^2 \;\ge\; \tfrac14 e^{4nG}.$$
> **Proof.** $\pi(z) = T_n(\ell(z^2))/T_n(\ell(0))$ with $\ell(w) = (2w - g^2 - T^2)/(T^2-g^2)$ has degree $2n \le M-1$, $\pi(0) = 1$, and $|\pi| \le 1/|T_n(\ell(0))|$ on $\pm[g,T]$ (because $\ell(y^2) \in [-1,1]$ there). Since $\ell(0) = -(g^2+T^2)/(T^2-g^2) < -1$, $|T_n(\ell(0))| = \cosh(n \operatorname{arccosh}\frac{g^2+T^2}{T^2-g^2}) = \cosh(2nG)$. So $\lambda_M(0) \le \int |\pi|^2 d\mu \le \cosh(2nG)^{-2}$; the identity above supplies the rest. $\square$

This turns e1u VERIFIER target 6 ("a clean statement would make *the type divergence relocates into the length coordinate* a theorem in this gauge") from a numerical shadow into a **proved statement with an explicit rate**, and the rate is a function of $(g, T, M)$ only. The bound is never violated across 22 build-faces (V2a), as it must not be.

### 2. The typing verdict, measured

Because the rate depends only on the gap geometry, the **exponential order** of the blowup is geometry, not arithmetic. What is left for arithmetic is the tightness residual $\rho = \log(1/\lambda) / (2\log\cosh 2nG)$. Measured (V2, V2d, V3): $\rho$ is $O(1)$, does not scale with $M$, and once the gap is equalized across families it does not separate them.

### 3. The continuity obstruction (the sharpening the corpus sweep needs)

$1/\lambda_M(0) = \sum_j \ell_j(0)^2/w_j$ is a **rational, hence continuous** function of the atom positions. $\mathbb{Q}$-linear independence of the positions is a totally-disconnected condition whose complement (rationals with a common denominator, i.e. lattices) is **dense**. No continuous functional of finitely many atom positions can detect it. V5 demonstrates this by snapping the true zero set onto $(1/D)\mathbb{Z}$ (maximally $\mathbb{Q}$-dependent: an honest lattice) for growing $D$ and measuring the response, in the per-atom rate coordinate, uniformly in $M$.

## Pre-registered expectations and exits (stated before results were read)

| Q | Pre-registered expectation | Pre-registered exit | Outcome |
|---|---|---|---|
| Q1 | The identity holds to chain precision on every build-face through two independent routes | Any failure is an encoding bug, reported not tuned | **CONFIRMED** (V1b: $7\cdot10^{-50}$) |
| Q2 | The proved bound holds and is order-tight: $\rho = O(1)$, not $O(M)$ | $\rho$ growing with $M$ would mean the geometric law is not the leading order and would REOPEN the pointwise route | **CONFIRMED** ($\rho \in [1.15, 3.32]$, corr$(\rho, M) = +0.55$) |
| Q3 | Destroying microstructure at fixed density moves $\log(1/\lambda)$ by a small, $M$-stable, family-uniform amount | A margin the density-matched fake does not reproduce = a genuine arithmetic signal, and the rung reverses | **CONFIRMED** (V3a $\le 0.061$ per atom unflagged; V6a screen fired) |
| Q4 | The defect moves the Christoffel data only through the atom COUNT | A location-dependent response "would say the Christoffel gauge sees defect POSITION, which would be new" | **EXIT FIRED**: response is location-dependent beyond the gap. Typed non-arithmetic by V4b/V5 |
| Q5 | The lattice snap converges, with the per-atom rate response bounded uniformly in $M$ | Non-convergence, or blowup with $M$ surviving normalization, leaves the pointwise route open | **CONFIRMED** ($\le 2.4\cdot10^{-8}$ at $D=10^6$, corr with $M$ $= -0.24$) |
| Q6 | The DMV screen MUST fire; K1 guards installed and never tripped | Failure of the screen to fire is an ALARM, not a discovery | **FIRED** (V6a, on the clean configs) |

Threshold provenance (the e1t/e1u discipline): the check SHAPES above were pre-registered in the module docstring before any result was read; the numerical thresholds in the self-tests were pinned from a calibration run of this same deterministic code and are labeled **pinned**, not pre-registered. Two instruments were **replaced after the full grid** and both replacements are marked in place with the reason (V4b, V7); see "Instruments that were wrong" below.

## Methods

- **Harness by import, not reimplementation**: `get_build`, `ghost_gate`, `qpoly` come from e1t; `Chain`, `face_A`, `face_B`, `build_chain` come from e1u (module identity asserted in V0a/V0b). Zeta, D-H and the Beurling fake flow through literally the code e1t verified bit-identical to e1k and e1u certified by round trips at $10^{-49}$.
- **Grid**: the e1t/e1u 11-build grid (ZETA / D-H at $\lambda = 2.2, 2.6, 3.0, \sqrt{13}$; BEUR at $2.2, 2.6, 3.0$), both faces, 22 build-faces total. Builds on the dps-25 branch; Christoffel work at dps 80 (all Lagrange terms are positive squares, so there is no cancellation; the precision sweep 40/80/120 agrees exactly, V6d).
- **Surrogates**: block-equalized (split the sorted positive atoms into $K$ contiguous blocks, replace each block's interior by equally spaced points between its endpoints: a one-parameter family from pure geometry at $K=1$ to the truth at $K = n-1$, preserving $(g, T, M)$); jitter ($t_j \to t_j + \varepsilon d_j u_j$ with $d_j$ the min neighbour spacing, seeded, order-preserving); rational snap onto $(1/D)\mathbb{Z}$.
- **Gap equalization (mandatory)**: every cross-family Face-A read is made on $|t| \ge 13.6$ symmetrically, exactly the e1u U2c control. $\rho$ is a function of the gap by Theorem V2 and the three families have different low bands, so an unequalized family comparison is a comparison of first-zero positions. This rule caught two would-be findings in this rung (see below).
- **K1**: runtime guards on `mp.zetazero` and the D-H scanner (installed, never tripped); a source scan that was **verified to have teeth** (a planted `mp.zetazero(1)` call is caught, and only it). No zero list of any L-function is consumed anywhere; 13.6 / 4.9 enter only as inherited scan-window landmarks.

## Results

### V1 (Q1) The identity, two routes

Every build-face of all three families: the chain's own trace-length is reproduced by $1/\lambda_M(0) + Q_M(0)$ (float-floored at $2\cdot10^{-16}$ because e1u stores interval lengths as float64), and the mpmath-exact comparison of the two **independent** routes agrees to $7\cdot 10^{-50}$ worst case. The first-kind (Christoffel) share of the germ length is $0.844$ to $1.000$, i.e. on Face A the germ length **is** the reciprocal Christoffel function to five decimal places ($\ge 0.99988$ at every Face-A build), and even on the gauged Face B it is the dominant term.

### V2 (Q2) The theorem and its tightness

| build | face | M | gap $g$ | $T$ | $G$ | bound | measured | $\rho$ |
|---|---|---|---|---|---|---|---|---|
| ZETA 2.2 | A | 8 | 14.135 | 30.44 | 0.50291 | 4.653 | 5.355 | 1.151 |
| ZETA 2.6 | A | 16 | 14.135 | 40.91 | 0.36029 | 8.702 | 10.207 | 1.173 |
| ZETA 3.0 | A | 26 | 14.135 | 56.46 | 0.25578 | 10.891 | 24.006 | 2.204 |
| ZETA $\sqrt{13}$ | A | 48 | 14.135 | 79.33 | 0.18009 | 15.182 | 24.402 | 1.607 |
| D-H 2.2 | A | 14 | 5.164 | 28.40 | 0.18386 | 3.051 | 4.322 | 1.417 |
| D-H 2.6 | A | 24 | 5.096 | 40.44 | 0.12667 | 4.195 | 7.108 | 1.694 |
| D-H 3.0 | A | 38 | 5.094 | 55.25 | 0.09247 | 5.274 | 10.189 | 1.932 |
| D-H $\sqrt{13}$ | A | 64 | 5.094 | 81.83 | 0.06233 | 6.344 | 15.569 | 2.454 |
| BEUR 2.2 | A | 14 | 2.311 | 29.15 | 0.07944 | 0.797 | 2.587 | 3.245 |
| BEUR 2.6 | A | 22 | 2.842 | 41.04 | 0.06937 | 1.509 | 3.439 | 2.278 |
| BEUR 3.0 | A | 38 | 1.846 | 56.89 | 0.03247 | 1.136 | 3.771 | 3.320 |

Bound never violated (22/22 build-faces including Face B). Face-A $\rho \in [1.15, 3.32]$, mean 1.92, corr$(\rho, M) = +0.55$: **the proved geometric rate is the leading order**, capturing 30 to 87 percent of $\log(1/\lambda)$ raw. The raw ordering (zeta tightest, fake loosest) is **not** a family ordering: it tracks the gap exactly as the theorem says it must.

**V2d, gap-equalized ($|t| \ge 13.6$ for all three families, the U2c control):**

| build | M | gap $g$ | bound | measured | $\rho_{\text{eq}}$ |
|---|---|---|---|---|---|
| BEUR 2.2 / 2.6 / 3.0 | 8 / 16 / 30 | 16.42 / 16.24 / 16.01 | 6.265 / 10.331 / 14.810 | 7.232 / 12.633 / 18.389 | 1.154 / 1.223 / 1.242 |
| D-H 2.2 / 2.6 / 3.0 / $\sqrt{13}$ | 8 / 18 / 32 / 58 | 17.19 / 14.89 / 14.44 / 14.41 | 7.028 / 10.977 / 14.665 / 18.537 | 7.611 / 13.873 / 19.804 / 28.507 | 1.083 / 1.264 / 1.350 / 1.538 |
| ZETA 2.2 / 2.6 / 3.0 / $\sqrt{13}$ | 8 / 16 / 26 / 48 | 14.135 | 4.653 / 8.702 / 10.891 / 15.182 | 5.355 / 10.207 / 24.006 / 24.402 | 1.151 / 1.173 / **2.204** / 1.607 |

Family means: BEUR 1.206, D-H 1.309, ZETA 1.534, **spread 1.27x**. The single bold entry is the V7 near-degenerate build; excluding it, zeta's mean is 1.31, i.e. numerically equal to D-H's.

**The $\lambda$ trend (the coordinate the uniformity clause actually lives in)**: BEUR 1.154, 1.223, 1.242; D-H 1.083, 1.264, 1.350, 1.538; ZETA 1.151, 1.173, (2.204), 1.607. $\rho_{\text{eq}}$ **drifts upward with $\lambda$ for every family, at a comparable rate**. That drift is exactly what a $\lambda$-uniform rate clause would have to control, and it is family-blind: the residual above the geometric law grows the same way for zeta, for the RH-false twin, and for the Euler-product-only fake.

### V3 (Q3) Density versus microstructure

Destroying **all** microstructure at fixed $(g, T, M)$ (block surrogate at $K=1$) moves the per-atom rate $|\Delta\log(1/\lambda)|/M$ by at most $0.061$ on every build the V7 rule does not flag (BEUR $\le 0.010$, D-H $\le 0.061$, ZETA 2.6 $0.027$); the surrogate family recovers the truth monotonically in $K$ (V3b), and by $K = 32$ every build is reproduced to five decimals. Position jitter at fixed count moves the rate by $\le 0.028$ even at $\varepsilon = 0.5$, and the modulus **decreases** with $M$ (corr $= -0.675$). The Christoffel value at the footpoint is, to this resolution, a functional of the macroscopic density and the gap.

### V4 (Q4) The off-line defect: the exit fired

Sweeping the e1u U4a collision (remove an adjacent pair) over **all** 12 pair locations at ZETA 3.0: $\Delta\log(1/\lambda)$ ranges $[-11.71, +5.89]$ and **changes sign** (3 of 12 positive). The pre-registered "same-signed" instrument was simply wrong, and the pre-registered Q4 exit fired: the response is location-dependent beyond the count.

The mechanism for the sign flip is Theorem V2's own content: removing the **lowest** pair widens the central gap $g$, which **raises** the proved bound. The bound's own response over the same sweep is $[-2.05, +6.76]$, and corr(measured, bound) $= +0.59$ (held-out) and $+0.59$ on a gap-equalized non-degenerate replication (D-H $\sqrt{13}$, 28 locations). So the gap geometry explains $r^2 \approx 0.35$ of the location variance and **a genuine local-position sensitivity is the rest**.

Is that residual sensitivity arithmetic? No. The identical gap-equalized sweep on the density-matched Beurling fake gives $r^2 = 0.44$: the fake shows the same mixture. **Position sensitivity is not arithmetic sensitivity.** (Before gap equalization this comparison read $r^2 = 0.92$ for the fake versus $0.50$ for D-H, which would have been a spurious "the fake is more geometric" finding. It was the gap confound; see "Instruments that were wrong".)

### V5 (Q5) The continuity obstruction

Per-atom rate displacement after snapping the zero set onto $(1/D)\mathbb{Z}$:

| build | $D=10$ | $10^2$ | $10^3$ | $10^4$ | $10^5$ | $10^6$ |
|---|---|---|---|---|---|---|
| ZETA 2.6 | 1.9e-3 | 2.1e-4 | 2.9e-5 | 6e-7 | 3e-7 | <1e-8 |
| ZETA 3.0 | 1.6e-2 | 2.6e-3 | 1.4e-4 | 1.2e-5 | 3.0e-6 | <1e-8 |
| ZETA $\sqrt{13}$ | 2.6e-3 | 2.8e-4 | 2.9e-5 | 5.9e-6 | 7e-7 | <1e-8 |
| D-H $\sqrt{13}$ | 1.1e-3 | 1.6e-5 | 4.0e-6 | 3e-7 | <1e-8 | <1e-8 |
| BEUR 3.0 | 1.2e-3 | 1.1e-4 | 1.2e-5 | 6e-7 | <1e-8 | <1e-8 |

Worst at $D = 10^6$: $2.4\cdot10^{-8}$, over 10 builds with $M$ from 14 to 64, corr with $M$ $= -0.24$. Every snapped configuration is a genuine lattice. The obstruction does not weaken as the configuration grows over the measured range. And the coarse snap ($D = 10^2$, worst $2.6\cdot10^{-3}$) is already a **weaker** perturbation than density-preserving microstructure destruction (V3a, up to $6\cdot10^{-2}$): lattice-ness is a smaller change to this functional than re-spacing the zeros at fixed density.

### V7 The near-degeneracy audit (post-hoc, declared)

Added after the full grid showed one build carrying every anomaly at once. Rule declared before application: flag a build if its minimal adjacent zero separation is below $1/4$ of its median.

| build | min sep | med sep | ratio | top term share | $K{=}1$ displacement | $\rho_{\text{eq}}$ | flag |
|---|---|---|---|---|---|---|---|
| BEUR 2.2 / 2.6 / 3.0 | 3.10 / 2.25 / 1.66 | 3.93 / 3.55 / 2.78 | 0.79 / 0.63 / 0.60 | 0.46 / 0.39 / 0.41 | 0.010 / 0.003 / 0.000 | 1.154 / 1.223 / 1.242 | |
| D-H 2.2 / 2.6 / 3.0 / $\sqrt{13}$ | 3.37 / 2.38 / 2.08 / 1.35 | 3.94 / 3.26 / 2.81 / 2.42 | 0.86 / 0.73 / 0.74 / 0.56 | 0.22 / 0.18 / 0.15 / 0.16 | 0.005 / 0.025 / 0.036 / 0.061 | 1.083 / 1.264 / 1.350 / 1.538 | |
| ZETA 2.6 | 2.51 | 3.98 | 0.63 | 0.20 | 0.027 | 1.173 | |
| ZETA 3.0 | **0.124** | 3.40 | **0.036** | 0.25 | **0.363** | **2.204** | DEGENERATE |
| ZETA $\sqrt{13}$ | 0.485 | 2.52 | **0.192** | 0.26 | 0.042 | 1.607 | DEGENERATE |

corr(separation ratio, $K{=}1$ displacement) $= -0.768$: tighter configurations are more microstructure-sensitive, i.e. the sensitivity is **conditioning**, not family structure. Surgical control (separate only the sub-threshold pairs to the median spacing, touch nothing else): ZETA $\sqrt{13}$ goes $1.607 \to 1.498$, **100 percent** of its excess over the unflagged band removed, inside the band. ZETA 3.0 goes $2.204 \to 1.736$, **70 percent** removed, with a **residual $+0.199$ that the declared rule does not explain and that is recorded as an open item, not absorbed**.

The near-degenerate pair at ZETA 3.0 is the $(40.91, 41.03)$ pair, separation $0.124$: e1u's own U4a minimal-separation choice. It is a property of that finite build.

### V6 (Q6) Disciplines

- **DMV screen FIRED** on the gap-equalized certification vector ($\Delta\rho_{\text{eq}}$, block modulus, jitter modulus, snap modulus) at both non-degenerate matched configs: $\Delta\rho_{\text{eq}} \le 0.050$, $\Delta$block $\le 0.024$, $\Delta$jitter $\le 0.0011$, $\Delta$snap $\le 1.9\cdot10^{-8}$. The $\lambda = 3.0$ config is the V7 near-degenerate build and is reported with that label rather than dropped.
- **K1 clean**: guards installed, never tripped; source scan verified to have teeth.
- **Precision**: the Lagrange route is exact across dps 40/80/120 (spread 0.0).
- **Input typing**: the identity and the theorem consume atom positions and count only, i.e. **pure geometry, no arithmetic input at all**. The tightness residual is geometry plus configuration, DMV-screened. Nothing in this rung is Euler-typed or lattice-typed. That is the finding, not an omission.

## Instruments that were wrong, and how they were caught

Recorded because the corrections are the load-bearing part of the round.

1. **V4b's pre-registered "same-signed at every location"** was the wrong instrument: the response genuinely changes sign. Replaced in place (with the reason marked) by a test of *why* it varies, i.e. whether it tracks the proved bound. The pre-registered exit was then honestly recorded as FIRED rather than reinterpreted away.
2. **The first V6a screen compared raw rates across families**, which re-imports precisely the gap confound V2d exists to remove. Fixed to compare per-atom **displacements**, gap-equalized.
3. **The first V4 fake comparison was not gap-equalized** and produced an apparent "the fake is far more geometry-explained" separation ($r^2$ 0.92 vs 0.50). Equalizing the band collapsed it to 0.44 vs 0.35. This is the third time in the e1t/e1u/e1v arc that an unequalized Face-A family read produced a mirage; the U2c rule should be treated as a standing precondition for any Face-A cross-family claim, not a control to be remembered.
4. **V1a/V1b's first thresholds** ($10^{-30}$, $10^{-20}$) were below the float64 floor of the inherited container; the identity check is float-floored by construction and the mpmath-exact certificate is V1b.
5. **V6c's first source scan was a tautology** (it passed unconditionally). Rewritten and then verified to catch a planted `mp.zetazero(1)` call.

## Discipline outcomes

- **D-H (form-side control)**: enters through identical code at all four cutoffs. Certifies into the theorem exactly like zeta (bound never violated), gap-equalized $\rho_{\text{eq}}$ within 1.2x of zeta's non-degenerate values, supplies the clean non-degenerate replication for V4b. Nothing in the Christoffel gauge separates zeta from the RH-false twin.
- **Beurling (counting-side control)**: builds and certifies identically; the DMV screen fires on the full certification vector; its gap-equalized defect-sweep geometry share (0.44) brackets the gated families' (0.35). The fake fails nothing on any Christoffel face, which is the expected and required outcome: the compactness/growth leg is density-typed by construction.
- **K1**: no truth values or zero lists of any L-function consumed; guards armed throughout.

## Honest limits

1. **Finite objects only.** This rung decides whether the **pointwise** Christoffel functional at finite $\lambda$ carries arithmetic. It cannot prove that no limit-level mechanism exists, and does not claim to. The continuity obstruction is an obstruction to finite-$M$ detection; V5b measures that its modulus does not degrade over $M \in [14, 64]$, which is evidence, not a theorem about all $M$.
2. **The degree regime is not the corpus's.** Totik / Nevai / Lubinsky / Mate-Nevai-Totik study $\lambda_n(\mu)$ for a **fixed** measure as $n \to \infty$. Our object is the **diagonal** $n = M(\lambda) - 1$ with the measure itself moving with $\lambda$, where the extremal problem degenerates to pure interpolation. This is a real scoping gap in the transfer, and it cuts both ways: the corpus's asymptotic uniformity mechanisms do not directly apply to the object the clause is about. Stated as a limit, and as a reason the sweep target needs re-aiming rather than more reading.
3. **In-sample, small grids** (4 + 4 + 3 cutoffs, $N$ and $\lambda$ co-varying, dps-25 build branch). Every family reading is a finite-grid level, not a law. The DMV screen ran on two clean matched configs, which is thin.
4. **The ZETA 3.0 residual, DOWNGRADED by the adversary round.** The declared degeneracy rule removes 70 percent of its excess under the separation surgery, leaving $+0.199$. Probe B showed the residual is **repair-dependent**: removing the tight pair outright (rather than separating it) lands at $1.440$, inside the unflagged band $[1.083, 1.538]$. So the residual is a property of the chosen surgery, not a stable family signal. It is no longer an open item, but the build remains flagged and excluded from family readings.
5. **Theorem V2 is one-sided.** It lower-bounds $1/\lambda_M(0)$; no matching upper bound is proved here, so "the geometric law is the leading order" is a measured statement, not a theorem. Probe D strengthens it: at **fixed** gap fraction $g/T = 0.25$, $\rho$ stays in $[1.30, 1.42]$ while $M$ grows 12-fold ($8 \to 96$), visibly saturating, so the $O(1)$ reading is structural rather than grid-local. Probe D also identifies what the observed $\lambda$-drift of $\rho_{\text{eq}}$ actually is: not an $M$ effect but the gap fraction $g/T$ shrinking as the window grows at fixed $g$.
6. **The ADVERSARY round was self-run.** [`_e1v_adversary.md`](_e1v_adversary.md): five attacks run (dossier cases 1, 2, 4, 5, 6), five failed to land, one (B) closed an open item, and one unposed attack (F, verifying the atom sets against e1u's tracked npz) **independently confirmed V7**: all 22 atom counts reproduce exactly and every germ length reproduces to $\le 1.6\cdot10^{-8}$ except ZETA 3.0 Face A at $3.7\cdot10^{-4}$, i.e. the one build the degeneracy rule flags is the one that fails to reproduce across machines, for the stated reason. Cases 3 (scope of the continuity obstruction) and 7 (independent K1/determinism re-verification) were **not** run and remain the open attack surface.
7. **A documentation discrepancy in e1u was surfaced and left alone.** e1u's dossier conditioning table gives BEUR 3.0 Face A as `36 / 41.0`; e1u's own npz gives $M = 38$, $X = 43.4631$, reproduced here to $3\cdot10^{-12}$. Not edited, since that dossier is adversary-verified; flagged for Owen.

## Handed forward

1. **The corpus sweep should be re-aimed, not run as written.** PHASE_STATE next-step 2 asks for "ANY mechanism giving $\lambda$-uniform Christoffel control at a point against measures with atoms at $\mathbb{Q}$-linearly independent positions, for an Euler + lattice reason". This rung says the pointwise version of that request is unsatisfiable in principle (continuity versus a dense complement), so a literature sweep for it would return either nothing or a mirage. The surviving version of the question is **limit-level**: a sum-rule statement about the sequence of chains, which is exactly the Killip-Simon register the #170 survey already named as the proven neighbouring template. The four-level caution the TODO attached to this sweep stands and is sharpened: Lubinsky-type universality is bulk-asymptotic, and now we also know the pointwise growth functional is arithmetic-blind, so the whole "growth bound" family is out and only the sum-rule family survives.
2. **The $\lambda$-drift of $\rho_{\text{eq}}$ is the measurable form of the uniformity clause.** It drifts upward for all three families at a comparable rate over $\lambda \in [2.2, 3.6]$. Whether that drift is bounded is the finite-grid shadow of the #160 growth clause. A larger grid (more $\lambda$, held-fixed $N/\lambda$ ratio) would say whether the drift saturates. This is the cheapest genuinely new measurement in the coordinate.
3. **Theorem V2 is Lean-ready** and subsumes e1u VERIFIER target 6; see below.
4. **The ZETA 3.0 residual** (limit 4) is a concrete, cheap open question.

## Verification targets (for VERIFIER)

1. **Theorem V2 itself** (finite, elementary): the Chebyshev construction, $|T_n(x)| = \cosh(n \operatorname{arccosh} x)$ for $x > 1$, and the conclusion $\lambda_M(0) \le \cosh(2nG)^{-2}$. Mathlib has Chebyshev polynomials (`Polynomial.Chebyshev.T`); the analytic step is the $\cosh$ representation off $[-1,1]$.
2. **The Christoffel identity** $\sum_{k<M} p_k(0)^2 = 1/\lambda_M(0)$ for an $M$-atom probability measure (the reproducing-kernel/Christoffel-Darboux statement at full degree), and its Lagrange form $\sum_j \ell_j(0)^2/w_j$. Both are finite linear algebra; the Lagrange form is a Cauchy-Schwarz equality case.
3. **The germ-length split** $X_{\text{total}} = 1/\lambda_M(0) + Q_M(0)$, which together with 1 and 2 **supersedes e1u VERIFIER target 6** by proving it with an explicit rate rather than conjecturing the shape.
4. **Continuity/rationality of $1/\lambda_M(0)$ in the atom positions** away from collisions (needed to state the obstruction formally): the functional is a rational function with poles only on the collision locus.

## Adversarial test cases (posed, with the round's outcomes)

Full record: [`_e1v_adversary.md`](_e1v_adversary.md), executable as `python -m experiments.spectral._e1v_adversary`.

1. **Attack the theorem.** Is $2n \le M-1$ used correctly at small $M$? Is the $z \mapsto z^2$ Green's-function factor $1/2$ right, and does the bound degrade correctly as $g \to 0$? [OUTCOME: **did not land.** 400 random even configurations with non-uniform random weights, $M$ up to 24, $g/T$ from $0.005$ to $0.9$: **0 violations**. Small-$M$ edges correct ($M=2 \Rightarrow n=0 \Rightarrow$ trivial bound). $g \to 0$ sends the log-bound to 0 as required.]
2. **Attack the "leading order" reading.** Construct a family where $\rho$ grows without bound at fixed gap fraction. [OUTCOME: **did not land, and V2b is strengthened.** At $g/T = 0.25$ fixed, $\rho$ runs $1.30 \to 1.42$ while $M$ goes $8 \to 96$, saturating. The $\lambda$-drift in the real families is the gap fraction shrinking, not an $M$ effect.]
3. **Attack the continuity obstruction as stated.** Does it also kill every *sequence-level* statement a sum rule could make? It should not. [**NOT RUN. Open**, and the strongest place for an independent reader to catch overclaiming in the verdict line.]
4. **Attack V7's declared rule.** DEGEN_RATIO was chosen after seeing the grid. [OUTCOME: **did not land, and it closed an open item.** The flag set is stable on $[0.25, 0.40]$ and keeps ZETA 3.0 at $0.15$; the $+0.199$ residual is repair-dependent (removal surgery lands at $1.440$, inside the band), so it is a property of the surgery.]
5. **Attack the gap-equalization threshold.** [OUTCOME: **did not land.** Bands 13.6 / 16 / 20 / 25 give spreads 1.27x / 1.24x / 1.21x / 1.30x, and the family ordering is not even stable across them.]
6. **Attack the surrogate design.** [OUTCOME: **did not land.** A spacing-**distribution**-preserving surrogate (permuted gap multiset) agrees with the block-density surrogate on every unflagged build (worst 0.052 vs 0.061 per atom); the two flagged builds move more under both.]
7. **K1 and determinism**: guards, planted-call scan, npz byte-reproducibility, quick/full parity. [Verified in-session (the scan was confirmed to catch a planted `mp.zetazero(1)` call, and only it); **independent re-verification NOT RUN. Open.**]
8. **(Unposed, added by the round) Are the atom sets e1u's?** [OUTCOME: **confirmed, and it independently validated V7.** All 22 atom counts match e1u's tracked npz exactly; every germ length matches to $\le 1.6\cdot10^{-8}$ except ZETA 3.0 Face A at $3.7\cdot10^{-4}$, i.e. the flagged build is the one that fails to reproduce across machines, for the stated conditioning reason.]
