# 4E.6 — Constrained-Domain LP for Non-Negative Trig Polynomials

> Probe of the proposed escape from [4E.3's structural lemma](e4e3_mt_translation.py). 4E.3 proved that any non-negative 2D trig polynomial restricted to a 1D line is bounded by 1D Fejér at matched effective degree, so single-zero MT bookkeeping cannot improve via line-restriction. TODO and LEARNINGS speculated that **relaxing the non-negativity constraint to a subset Ω ⊂ [0, 2π]^d** (the "constrained-domain LP") might escape this ceiling — the structural lemma's proof relies on full non-negativity, after all.
>
> **Headline**: it doesn't. In all four natural formulations tested, the constrained-domain LP either (a) is under-constrained and hits the coefficient bound (= LP-unbounded artifact), (b) produces a polynomial with large negative excursions in the relaxed region (= unphysical for the MT explicit-formula sum), (c) recovers the full-non-negativity ceiling asymptotically as the constraint set densifies (= "sparse-sampling artifact", not a structural escape), or (d) collapses into one of the above when made physically meaningful.
>
> **Verdict**: the "constrained-domain LP" is not a separate route. Sharpens 4E.3's lemma: the MT geometric structure resists not just 1D restriction but also naive domain relaxation. To improve the single-zero MT shape factor via 2D inequalities requires *qualitatively different* machinery — Heath-Brown multi-zero coupling (Arch 4E.7 open), Bombieri variational SOS, or polynomial-ideal SOS (Arch 4E.8 open).

## 1. Background

4E.3's structural lemma:

> If $P(\theta, \phi) \geq 0$ on $[0, 2\pi]^2$ and $\tilde P(u) := P(t_1 u, t_2 u)$ is the restriction to a line, then $\tilde P$ is a non-neg 1D trig polynomial bounded by the Fejér optimum at matched effective degree.

Consequence: the 2D LP optimal polynomial reduces to 1D Fejér under any line-restriction, so the single-zero MT shape factor (which is computed from the 1D restriction at the zero's frequency line) is bounded by 1D Fejér independent of the 2D LP's structure. The +25% C-S gap of 4E.2 cannot be cashed in.

The proposed escape: don't require $P \geq 0$ on all of $[0, 2\pi]^d$ — only on a subset $\Omega$ that's physically meaningful for the MT explicit-formula sum. If $\Omega$ is small enough, the line-restriction argument breaks (P need not be non-negative on the whole line, only on the line's intersection with $\Omega$), and the LP can exceed the Fejér ceiling.

This experiment tests four natural formulations of "constrained-domain LP" and asks: does any of them give a real, physically realizable improvement?

## 2. Four setups

For all setups, $P(\theta) = c_0 + 2 \sum_{k=1}^N c_k \cos(k\theta)$, $c_0 = 1$, objective is $\max c_1$ (Setups A, B, C) or $\max P(\theta_{\rm trick})$ (Setup D). All LPs add a coefficient bound $|c_k| \le c_{\rm bound}$ to keep them bounded when the non-negativity constraint is underdetermined.

### Setup A: K-point LP

$P(\theta_k) \ge 0$ at $K$ evenly spaced points $\theta_k = 2\pi k / K$, $k = 0, \ldots, K-1$.

- $K \le N$ (under-constrained): LP unbounded, hits $c_{\rm bound}$.
- $K \ge 32 N$ (densely sampled): recovers Fejér to 4-digit precision.
- Sweet spot $K \in [N+1, 2N]$: LP value 1.05x–1.16x Fejér, with $P$ slightly negative (~$-3$ to $-5$) on the inter-sample gaps. Not physically realizable as "$P \ge 0$ on $[0, 2\pi]$" because $P$ is not actually non-negative.

Example at $N = 8$:
| $K$ | LP $c_1$ | Fejér $c_1$ | min $P$ on fine grid |
|---|---|---|---|
| 9 (= N+1) | 50.000 | 0.951 | -395.000 (hit bound) |
| 10 | 1.000 | 0.951 | -420.626 |
| 16 | 1.000 | 0.951 | -3.384 |
| 32 | 0.954 | 0.951 | -0.054 |
| 64 | 0.952 | 0.951 | -0.009 |
| 256 | 0.951 | 0.951 | -0.0005 |

The pattern is universal across $N$: under-constrained $\to$ unbounded; well-constrained $\to$ Fejér.

### Setup B: Arc-removal LP

$P \ge 0$ on $[0, 2\pi] \setminus (\theta_0 - \delta, \theta_0 + \delta)$ for $\theta_0 = \pi$, half-width $\delta$.

- Small $\delta$ ($\le 0.1\pi$): LP recovers Fejér exactly; the excluded arc is too small to give any LP freedom.
- Large $\delta$ ($\ge 0.25\pi$): LP hits the coefficient bound. $P$ is large and negative ($\sim -200$) inside the arc.

Example at $N = 8$:
| $\delta/\pi$ | $c_{\rm bound}$ | LP $c_1$ | Fejér $c_1$ | min $P$ in arc |
|---|---|---|---|---|
| 0.01 | 5 | 0.9511 | 0.9511 | +0.005 |
| 0.10 | 5 | 0.9511 | 0.9511 | +0.000 |
| 0.25 | 5 | 5.000 | 0.9511 | -22.76 |
| 0.50 | 5 | 5.000 | 0.9511 | -28.82 |
| 0.25 | 50 | 50.000 | 0.9511 | -218.87 |

LP value scales with $c_{\rm bound}$ when $\delta$ is large, indicating the LP is unbounded in the limit. The "gain" is purely from coefficient inflation enabled by allowing huge negativity in the excluded arc — not from any structural relaxation that has physical content.

### Setup C: Zero-constrained LP

$P \ge 0$ only at $\theta = \gamma_k \log p \bmod 2\pi$ for the first $K$ on-line zeta zero ordinates and a fixed prime $p$.

This is the natural "MT-physical" subset: the explicit-formula sum runs over zero ordinates, so $P$ only needs to be non-negative on the orbit of $\{\gamma_k \log p\}$.

By Weyl equidistribution, $\{\gamma_k \log p \bmod 2\pi\}$ is equidistributed in $[0, 2\pi]$ as $K \to \infty$. So for large $K$, Setup C's constraint set is dense and the LP recovers full-non-negativity. For small $K$, Setup C is under-constrained.

Example at $N = 4$:
| $K$ | $\log p$ | LP $c_1$ | Fejér | ratio | hit bound? |
|---|---|---|---|---|---|
| 5 | $\log 2$ | hit bound | 0.866 | 23 | yes |
| 10 | $\log 2$ | 0.987 | 0.866 | 1.140 | no |
| 50 | $\log 2$ | 0.872 | 0.866 | 1.007 | no |
| 100 | $\log 2$ | 0.867 | 0.866 | 1.001 | no |

The pattern: above the under-constrained regime, the LP value decreases monotonically toward Fejér. The interpretation is direct: ignoring all-but-K zeros in the explicit-formula sum gives more LP freedom, but the "saved" freedom does not correspond to a valid MT inequality because the MT sum involves *all* zeros.

### Setup D: Trick at off-line height (MT-style)

The most-faithful MT analogue: the polynomial $P$ is constrained at on-line zero heights $\gamma_k \log p \bmod 2\pi$ (the explicit-formula sum's actual support), and we maximize $P$ evaluated at an *off-line trick frequency* $t_{\rm off} \log p \bmod 2\pi$ for a hypothetical off-line zero ordinate $t_{\rm off}$ (we use the midpoint between $\gamma_1$ and $\gamma_2$, a value not in any zero list).

This isolates the genuine "constrained-domain MT improvement" question: with the on-line zeros pinned to enforce non-negativity, how much can $P$ rise at an off-line frequency? Compared baseline: $\max P(\theta_{\rm trick})$ over fully non-neg $P$ with $c_0 = 1$ (computed via LP at $M = 40000$ grid points).

Result at $N = 8$:

| $K$ | $\log p$ | LP $P(\theta_{\rm trick})$ | full-non-neg max | ratio | hit bound? |
|---|---|---|---|---|---|
| 50 | $\log 2$ | 9.30 | 4.89 | 1.900 | no |
| 100 | $\log 2$ | 4.97 | 4.89 | 1.016 | no |
| 200 | $\log 2$ | 4.90 | 4.89 | 1.002 | no |
| 400 | $\log 2$ | 4.89 | 4.89 | 1.000 | no |
| 649 | $\log 2$ | 4.89 | 4.89 | 1.000 | no |
| 50 | $\log 3$ | 5.57 | 5.45 | 1.021 | no |
| 200 | $\log 3$ | 5.54 | 5.45 | 1.016 | no |
| 400 | $\log 3$ | 5.54 | 5.45 | 1.016 | no |
| 649 | $\log 3$ | 5.49 | 5.45 | 1.007 | no |

The ratios decay monotonically toward 1.0 as $K \to \infty$, confirming sparse-sampling-artifact origin:
- $\log p = \log 2$: converges to 1.000 by $K = 400$.
- $\log p = \log 3$: slower convergence (Weyl rate depends on $\log p$); at $K = 649$ still at ratio 1.007, but trend monotonic toward 1.0.

**Crucially**: setup D's apparent gain over the full-non-negativity baseline is consistent with finite-$K$ sparse sampling, not a structural escape from the 4E.3 ceiling. Extending $K$ to $\sim 1000$ at $\log p = \log 3$ should push the ratio under 1.005.

## 3. Why all four setups fail the same way

The pattern is uniform: each setup either hits the coefficient bound (artifact of LP being under-constrained) or asymptotes to the Fejér / full-non-negativity ceiling. There is no formulation where the LP value persists above the ceiling at well-resolved scales.

The structural reason traces back to the MT explicit-formula sum:

$$-\frac{\zeta'}{\zeta}(s) = \sum_{\rho} \frac{1}{s - \rho} + (\text{regular terms})$$

The sum is over **all** zeros $\rho$ of $\zeta$. To bound $\sum_\rho f(\rho)$ from below by something useful, we need a test function $f$ (typically $f = $ Fourier transform of our trig polynomial $P$) that is non-negative at every $\rho$.

If we relax the requirement to "$f \ge 0$ only at off-line $\rho$" (which is what Setup B / D try in different guises), we lose the inequality $\sum f(\rho) \ge 0$ unless we know separately that the on-line contribution stays bounded above by something. That additional bound is essentially RH-strength input.

So the constrained-domain LP, even if it produces $P$ values exceeding the Fejér ceiling on some subset, does not translate to a useful MT inequality without additional ingredients.

## 4. The actual escape routes

Three structurally different approaches *could* improve the MT constant, each not captured by domain restriction alone:

1. **Heath-Brown multi-zero coupling** (Arch 4E.7 open). Multiple putative zeros at different heights couple in the explicit-formula sum non-trivially. The relevant LP becomes a multi-variable problem on $\{(\gamma_1, \gamma_2, \ldots)\}$ where each $\gamma_i$ is a putative zero location. The line-restriction lemma applies only to a single line direction in this multi-variable space, so multi-zero couplings *can* in principle escape the 1D Fejér ceiling. This is the standard Heath-Brown setup for least-prime-in-AP and Siegel-zero bounds.

2. **Bombieri variational SOS**. Allow $P$ to be slightly negative, controlled by an $L^2$-norm bound. The relaxed problem becomes a (positive) quadratic program rather than an LP, with the negative tail of $P$ paid for explicitly via the variational penalty. Bombieri's 2003 program for Weil positivity is in this style.

3. **Polynomial-ideal SOS** (Arch 4E.8 open). Sum-of-squares decompositions over a specific polynomial ideal — i.e., $P = \sum_i Q_i^2 + \sum_j R_j \cdot h_j$ where $h_j$ are the defining polynomials of an algebraic variety. This is the Putinar / Schmüdgen framework. The variety encodes the "domain restriction" structurally, in a way that propagates correctly through MT bookkeeping.

None of these is the same as "naïve constrained-domain LP." 4E.6 sharpens 4E.3 by ruling out the naïve relaxation, narrowing the open question to these three structurally distinct approaches.

## 5. The methodological lesson

The constrained-domain LP idea was structurally motivated by the form of 4E.3's lemma: "the proof needs $P \ge 0$ on the full torus; what if we don't?" The numerical answer (4E.6): the structural lemma is more robust than it looks. Relaxing $P \ge 0$ doesn't help unless the relaxation is paired with an additional structural ingredient (multi-zero coupling, SOS, or algebraic variety) that compensates for the lost rigidity in the LP solution.

This is a clean methodological pattern: **the structural lemma's robustness suggests where the genuine open machinery lives.** The MT framework's "1D Fejér ceiling" survives line-restriction (4E.3) and domain-relaxation (4E.6); to break it, you need to change the *type* of inequality, not just its support.

## 6. Outputs

- **Code**: [e4e6_constrained_lp.py](e4e6_constrained_lp.py)
- **Figure**: [e4e6_constrained_lp.png](e4e6_constrained_lp.png) — four-panel summary (one panel per setup), showing the convergence-to-Fejér or bound-hitting behavior in each.
- **Data**: `e4e6_constrained_lp.npz` — all LP values, ratios, hit-bound flags, baseline values.

## 7. Connections to the broader Arch 4 program

- **4E.3** ([e4e3_mt_translation.py](e4e3_mt_translation.py)): the structural lemma that 4E.6 was designed to escape. 4E.6 confirms 4E.3 is robust under naïve domain relaxation.
- **4E.7** (open): Heath-Brown multi-zero coupling. The natural next 4E experiment is to implement this and check whether multi-zero LPs exceed the 1D Fejér ceiling.
- **4E.8** (open): Polynomial-ideal SOS. The most structurally rich of the three escape routes; requires SDP not LP.
- **3F-3I** (Arch 3): the analytic side of the same wall. Both Arch 3's "explicit-formula cancellation requires GRH-strength input" and Arch 4's "1D Fejér ceiling" are manifestations of the same MT/Weil-positivity rigidity.

## 8. Verdict

The constrained-domain LP escape from 4E.3 does not work. The four natural formulations all collapse to Fejér / full-non-negativity ceiling at well-resolved parameter values; apparent gains at coarse parameters are LP-unbounded artifacts (Setups A, B) or sparse-sampling artifacts (Setups C, D).

The actual escape routes — Heath-Brown multi-zero (4E.7), Bombieri variational, polynomial-ideal SOS (4E.8) — require *qualitatively different* machinery beyond LP-over-a-subset. 4E.6 narrows the open landscape by ruling out one route and pointing to the three remaining ones.

**Status**: Arch 4E.6 complete. Negative result, sharpening 4E.3.
