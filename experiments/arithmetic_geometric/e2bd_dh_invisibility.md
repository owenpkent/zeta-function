# E2BD: the D-H invisibility certificate (backlog B4)

**Date**: 2026-08-25. **Status**: BUILDER round, executed; 21/21 checks full and `--quick` (full 7 s). **Code**: [`e2bd_dh_invisibility.py`](e2bd_dh_invisibility.py). **Data**: `e2bd_dh_invisibility.npz` (tracked; full-mode run). **Provenance**: hardens LEARNINGS #179 (its handed-forward item 2); backlog spec in [`construction_backlog.md`](../../docs/03_research/construction_backlog.md) Family B. **Joint**: C1's completeness face (SP2), certified from the control side.

## 0. What this is

#179's scorecard MEASURED the assembled SP-object's completeness failure on the form-side control: the meter $|m_{DH}|$ stays at 0.242 on the critical line at the off-line pair's height while zeta's detected zeros dip to $4\times10^{-4}$. This build turns that measurement into a theorem with constants, computed in ball arithmetic (python-flint / arb) from the period-5 coefficient lattice $(1, \kappa, -\kappa, -1, 0)$:

$$|f_{DH}(\tfrac12 + it)| \;\ge\; c_{DH} \;=\; 0.33032\ldots \quad \text{(certified, enclosure radius } \sim 10^{-96}\text{)} \quad \text{for ALL } t \in W = [85.2,\, 86.2],$$

a window containing the off-line pair's height $85.699$ and on-line-zero-free with margin (cached D-H on-line neighbors: 83.109 below, 89.439 above; the pair sits inside a 6.3-wide on-line gap, consistent with the pair replacing two on-line zeros in the count). The floor's argmin is $t \approx 85.709$: the meter is at its lowest essentially AT the off-line height, and still bounded below by 0.33.

**The any-circumference corollary.** A circumference-$L$ carrier samples the line on the grid $\tau_k = 2\pi k/L$, and the e2an assembly extracts $f(\tfrac12+i\tau)$ from the lattice to its certified truncation residual ($7.7\times10^{-14}$ at its scale). The continuum bound therefore covers every grid point of every circumference at once: for any detection threshold $\theta < c_{DH} - \varepsilon_L$, no cokernel dip can open inside $W$ at any $L$ (each $L$ in the e2ao ladder places 1-3 grid points inside $W$; gated). The completeness failure is structural, not a resolution artifact.

## 1. The certified table

| Scan | window | grid | certified result |
|---|---|---|---|
| **THE CERTIFICATE**: $|f_{DH}|$ floor | $[85.2, 86.2] \ni 85.699$ (off-line height) | 1024 covering balls, $h = 2^{-10}$ | $c_{DH} = 0.33032\ldots \ge 0.05$; argmin $\approx 85.709$ |
| landmark point | $t = 85.6993$ | exact point | $|f_{DH}| = 0.356869\ldots$ (radius $6\times10^{-93}$) |
| bracket: zeta, same window | $[85.2, 86.2]$ (zeta-zero-free) | same covering | $c_\zeta = 0.97841\ldots$; ratio 2.96 |
| dip contrast: zeta | $[84.5, 85.0] \ni \gamma_{23} = 84.7355$ | point scan, $h = 2^{-12}$ | $\exists t:\ |\zeta| \le 2.2\times10^{-4}$ at $t \approx 84.7356$ |
| dip contrast: D-H's own ON-line zero | $[82.9, 83.3] \ni 83.109$ | point scan, $h = 2^{-12}$ | $\exists t:\ |f_{DH}| \le 4.7\times10^{-4}$ at $t \approx 83.1087$ |

All three pre-registrations FIRED (P1 floor $> 0.05$; P2 same-window bracket within 30x; P3 both dips below $c_{DH}/50$). Reading the table: the same certified meter that is floored at $0.33$ across a window containing an actual zero of the function (the off-line pair) drives three orders lower at on-line zeros of either function. The invisibility is selective, and it is exactly off-line-ness (the pair sits at distance $0.3085$ from the line) that buys it. #179's measured 600x is now a certified $\sim$700x ($0.330$ vs $4.7\times10^{-4}$), uniform over the window.

## 2. The instrument finding (named negative control, banked)

The backlog's method sketch said "smoothed AFE with explicit tails". Built literally, the $x = 1$-split incomplete-gamma AFE

$$\Lambda(s) = \sum_n a_n n \left[ w_n^{-z_1}\Gamma(z_1, w_n) + w_n^{-z_2}\Gamma(z_2, w_n) \right], \quad w_n = \pi n^2/5,\ z_1 = \tfrac{s+1}{2},\ z_2 = \tfrac{2-s}{2},$$

with explicit tail $(25/\pi^2)N^{-2}e^{-\pi N^2/5}$ ($< 10^{-69}$ at $N = 16$) is EXACT at points (enclosure radius $\sim 10^{-43}$ on the line) and provably the wrong sweep instrument: on the line $|\Lambda| \sim e^{-\pi t/4} \sim 10^{-30}$ emerges by cancellation between the conjugate halves of $O(1)$ terms, so a $t$-ball of width $h$ inflates the enclosure by $\sim h\,e^{+\pi t/4}$ and the certified lower bound collapses to 0 at any feasible $h$. Measured as a gate: on one $1/128$-width ball the AFE route's lower bound is exactly 0 while the balanced route certifies 0.97.

The sweep therefore runs on the balanced certified route: $f_{DH}(s) = 5^{-s}\sum_{a=1}^{4} c_a\, \zeta(s, a/5)$ with arb's rigorous Euler-Maclaurin Hurwitz zeta, which needs no functional equation and stays $O(1)$-conditioned on the line. The AFE is kept in the build as the independent FE-consuming route: theta self-duality certified at sample points ($10^{-95}$), $\Lambda(s) = \Lambda(1-s)$ certified off-line, and the two routes agree at line points to $< 10^{-43}$ (independent mathematics: theta/FE vs EM; plus a counted 5-call mpmath implementation check). The general lesson, worth its own line: **completed-object ($\Lambda$-side) representations are point instruments; line sweeps need the balanced side.** The e2an/e2ao assemblies always evaluated at grid points, so nothing upstream is affected; anyone building interval certificates on completed forms will hit this wall.

## 3. What the certificate says structurally

1. **The completeness failure is now a theorem about the control.** SP2's mechanism (zeros = cokernel dips of $|m|$ on the carrier) provably cannot see the off-line pair, at any circumference, for any threshold below $c_{DH}$. This was the one cell of #179's scorecard that was a measurement rather than a structural statement; it is now closed.
2. **The floor is zero-distance geometry, not arithmetic.** Zeta's same-window floor (0.98) and D-H's (0.33) are the same order; both are set by how far the nearest zero is from the scanned segment (for D-H: the off-line pair's $0.3085$ horizontal distance IS what keeps the line value up). No Euler-side quantity enters a line-window floor. That is the D-H discipline doing its job inside a certificate: a method that produced floors only for zeta would have been suspicious.
3. **The template (what a zeta completeness statement must supply).** The certificate's proof shape: line-window floors are purchasable from FE-side data plus zero geometry, for any coefficient lattice with a functional equation. Contrapositive: no line-restricted meter can certify completeness (visibility of ALL zeros): for zeta, SP2-completeness IS RH, and this build shows the line-restriction is structurally indifferent to off-line zeros at bounded distance. Whatever supplies zeta's completeness must therefore act off the line restriction: the #194 coordinate (the Euler side funding positivity through uniformity exactly where its transform vanishes) restated from the control side. C1's completeness face is now bracketed by a theorem on the fake.

## 4. Honest scope

The certificate is a statement about the CONTROL, not about zeta: it proves the instrument's blindness where blindness was measured, with constants. The epistemic chain: the classical D-H functional equation (Titchmarsh sec. 10.25; re-verified here as certified theta self-duality at sample points) + arb's certified special functions (Hurwitz zeta by Euler-Maclaurin, upper incomplete gamma) + the explicit AFE tails derived in the module docstring. Ball-arithmetic containment is machine-checked; the two independent evaluation routes agree at every tested point. Nothing here moves the frontier: the value is that a scorecard cell that read "measured" now reads "theorem", and the proof's shape says where zeta's completeness cannot come from. Frontier verdict: UNMOVED, by design.

## 5. Handed forward

1. **B3 (the certification-cost theorem) is the natural sibling**: the same explicit-constants treatment applied to the e2ao margin assembly ($\sigma^*(\varepsilon)$ with the $e^{\gamma_1^2\sigma^2}$ price as a theorem about the instrument). The ball-arithmetic idioms here (covering balls for floors, point scans for existence, route-pair validation) are directly reusable.
2. **A Lean shadow is cheap**: the certificate's skeleton (finite covering + per-ball rational bounds) is a finite conjunction; the VERIFIER queue can take "the floor constant exists and exceeds $1/20$" as a statement-level target with the npz as witness data (same pattern as #197's measured-column witnesses).
3. **The off-line distance as the floor's currency**: $c_{DH} \approx 0.33$ at horizontal zero-distance $0.3085$ invites the quantitative version (floor $\asymp$ distance $\times$ local slope scale) across several windows and both controls; one cheap sweep would make point 2 of Section 3 a measured law rather than an observation.
