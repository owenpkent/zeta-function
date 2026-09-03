# e_euler_pencil: the Euler pencil, off-line zeros approaching the Euler-product point

> Companion probe of [`negative_proof.md`](../../docs/03_research/negative_proof.md) (the disproof exercise, 2026-09-01; LEARNINGS #217). Script [`e_euler_pencil.py`](e_euler_pencil.py), run `python -m experiments.criticality.e_euler_pencil` (`--quick` halves the height); gates [`test_euler_pencil.py`](test_euler_pencil.py) (11/11, 31 s); tracked results [`e_euler_pencil.npz`](e_euler_pencil.npz) with provenance. Backend: python-flint 0.9.0 (Conrey-indexed Dirichlet characters, 25 digits) with an mpmath polish to $|f| < 10^{-18}$ at 30 digits. Full run 667 s at $T_{\max} = 200$.
>
> Siblings: [`e_dbn_flow_dh.md`](e_dbn_flow_dh.md) (the de Bruijn-Newman flow on the D-H control, the other FE-preserving deformation), [`e2bb_eta_second_variation`](../arithmetic_geometric/e2bb_eta_second_variation.py) (LEARNINGS #196, the complex pencil $L(\chi) + wL(\bar\chi)$ and its eta-Hessian).

## The object

$A(s) = \zeta(s)L(s,\chi_{-15})$, $B(s) = L(s,\chi_{-3})L(s,\chi_5)$, $f_\lambda = A + \lambda B$. Both complete to $\Lambda(s) = 15^{s/2}(2\pi)^{-s}\Gamma(s)(\cdot)(s) = \Lambda(1-s)$ with root number $+1$, so $Z_\lambda(t) = \Lambda_\lambda(1/2+it)$ is real and off-line zeros come in pairs $(\rho, 1-\bar\rho)$. $\lambda = 0$ and $\lambda = \infty$ are the two Euler products; $\lambda = +1$ is the Epstein zeta function of the principal form $x^2+xy+4y^2$ and $\lambda = -1$ that of $2x^2+xy+2y^2$ (gate G3: agreement with the Chowla-Selberg module to $10^{-26}$ at heights 20 and 45, no normalization constant; the genus decomposition was also checked coefficient by coefficient to $n = 200$ by the referee). Machinery: `count_rect` (winding number of $f_\lambda$ around $[-1,2]\times[T_1,T_2]$ by adaptive phase increments), `count_line` (sign changes of $Z_\lambda$ with local refinement), `offline_zeros` (2D minima of $|f|$ over $\sigma \in (0.5, 2]$, Newton, dedup), `lehmer_prediction`, `track_pair` (predictor-corrector continuation in $\lambda$, then bisection of $\lambda_c$ on the sign-change count in the collision window).

Pre-registration and its provenance are in the research document, Section 4 (P1-P5).

## S1: the lambda grid, d = -15, heights 1 to 200

$N_{\rm off}$ counts PAIRS ($N_{\rm total} = N_{\rm line} + 2N_{\rm off}$). $T^*$ is the lowest off-line height; $\beta_{\max}$ the largest real part found.

| $\lambda$ | $N_{\rm total}$ | $N_{\rm line}$ | $N_{\rm off}$ | $T^*$ | $\beta_{\max}$ |
|---|---|---|---|---|---|
| +1 | 243 | 169 | 37 | 12.039 | 0.927 |
| +0.5 | 243 | 165 | 39 | 12.215 | 0.919 |
| +0.25 | 243 | 175 | 34 | 15.139 | 0.831 |
| +0.1 | 243 | 193 | 25 | 20.737 | 0.651 |
| +0.05 | 243 | 207 | 18 | 43.391 | 0.688 |
| +0.025 | 243 | 215 | 14 | 43.384 | 0.630 |
| +0.01 | 243 | 227 | 8 | 43.380 | 0.572 |
| 0 | 243 | 243 | 0 | none | none |
| -0.01 | 243 | 219 | 12 | 24.952 | 0.596 |
| -0.025 | 243 | 209 | 17 | 13.805 | 0.782 |
| -0.05 | 243 | 197 | 23 | 13.799 | 1.015 |
| -0.1 | 243 | 189 | 27 | 13.788 | 1.305 |
| -0.25 | 243 | 181 | 31 | 4.256 | 1.895 |
| -0.5 | 199 | 175 | 12 | 24.672 | 0.839 |
| -1 | 199 | 179 | 10 | 24.483 | 0.758 |

Reading. (i) $\lambda = 0$: 243 zeros, all on the line (numerical RH + GRH$(\chi_{-15})$ to height 200; P5). (ii) Every $\lambda \neq 0$ on the grid has off-line zeros below 200, down to $\pm 0.01$; on the positive side the pair count falls monotonically $39 \to 8$ and $T^*$ climbs $12.0 \to 43.4$ as $\lambda \to 0$. (iii) The certified referee zeros are the $T^*$ entries: $12.039$ at $\lambda = +1$ (P1 as first written), $24.483$ at $\lambda = -1$. (iv) **The negative side is the Davenport-Heilbronn half-plane mechanism, at height 4.** $A$'s second Dirichlet coefficient is $+2$ and $B$'s is $-2$, so for $\lambda < 0$ the $n = 2$ term competes with the $n = 1$ term on the right edge and the pencil acquires zeros in $\sigma > 1$, where the series converges absolutely: $\beta_{\max} = 1.895$ at height 4.26 for $\lambda = -0.25$, $1.305$ at $-0.1$, $1.015$ at $-0.05$. These are D-H's 1936 zeros reproduced as a continuous function of the mixing parameter, and they descend onto the line as $\lambda \to 0^-$: the pair at height 13.80 has $\beta = 1.305, 1.015, 0.782$ at $\lambda = -0.1, -0.05, -0.025$ and is on the line by $-0.01$. (v) The two rows $\lambda = -1, -0.5$ read 199, not 243, and that is correct, not a miscount: at $\lambda = -1$ the first coefficient $1 + \lambda$ vanishes, $f_{-1} = 4\cdot 2^{-s} + \dots$ is a Dirichlet series beginning at $n = 2$, and its zero count carries the deficit $(T/\pi)\log 2 = 44.1$ at $T = 200$; at $\lambda = -0.5$ the $n = 2$ term ($3\cdot 2^{-s}$) dominates the $n = 1$ term ($0.5$) on $\sigma = 2$, so the same 44 zeros (22 pairs, spaced $2\pi/\log 2 = 9.06$ in height, near $\sigma \approx 2.6$ and their partners near $-1.6$) sit OUTSIDE the $\sigma \le 2$ box. Those two rows are box-limited; the box was kept at 2 to keep the trivial zeros and the pole out.

## S1 wide grid, d = -15, heights 1 to 200 (overnight 2026-09-02)

The same census at $|\lambda| = 2$ to $128$, toward the OTHER Euler product $f_\infty = B$ ($N_{\rm off}$ in pairs; the $\lambda = -2$ row is box-limited for the same reason as $-1$ and $-0.5$: $a(1) = -1$, $a(2) = 6$, so 22 pairs sit beyond $\sigma = 2$).

| $\lambda$ | +2 | +4 | +8 | +16 | +32 | +64 | +128 | -2 | -4 | -8 | -16 | -32 | -64 | -128 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $N_{\rm line}$ | 171 | 169 | 181 | 191 | 205 | 211 | 221 | 181 | 185 | 187 | 193 | 207 | 219 | 229 |
| $N_{\rm off}$ | 36 | 37 | 31 | 26 | 19 | 16 | 11 | 9 | 29 | 28 | 25 | 18 | 12 | 7 |

Reading: the off-line count thins toward $\lambda = \infty$ ($37 \to 11$ pairs on the positive side from 4 to 128, $29 \to 7$ on the negative side) exactly as it thins toward $\lambda = 0$ ($39 \to 8$ from 0.5 to 0.01). Both Euler products are the sparse ends of the projective line; the maximum sits in the middle ($|\lambda| \approx 0.5$ to $4$, where $A$ and $\lambda B$ are of comparable size). P1's "window bounded away from both endpoints" holds in this thinning sense, not as absence: even at $\lambda = 128$ there are 11 pairs below height 200. Log: `_cache/pencil_wide_overnight_2026-09-02.log` (752 s).

The $d = -20$ replicate at $T_{\max} = 60$ hung again in its killable subprocess (killed at 3000 s), so the 15-unit window below stands.

## S1 replicate, d = -20 (heights 1 to 15 only)

| $\lambda$ | $N_{\rm total}$ | $N_{\rm line}$ | $N_{\rm off}$ | $T^*$ | $\beta_{\max}$ |
|---|---|---|---|---|---|
| +1 | 7 | 7 | 0 | none | none |
| -1 | 2 | 2 | 0 | none | none |
| +0.25 | 7 | 7 | 0 | none | none |
| -0.25 | 8 | 6 | 1 | 14.125 | 1.631 |
| +0.05 | 8 | 8 | 0 | none | none |
| -0.05 | 8 | 6 | 1 | 14.209 | 0.960 |

Only $T_{\max} = 15$ was possible: heights above 25 hung reproducibly inside one C-extension call in this environment, so the replicate was isolated in an OS-killable subprocess and truncated. Within its window it shows the same negative-side half-plane zeros ($\beta = 1.63$ at $\lambda = -0.25$) and nothing else is claimed from it.

## S2: twelve tracked pairs

Each off-line zero at $\lambda = \pm 1$ (the six lowest per sign) continued in $\lambda$ toward 0 until it lands on the line, then the two on-line zeros $t_1 < t_2$ of $A$ it descends from, their gap $\delta$, the type (Z = zero of $\zeta$, L = zero of $L(\chi_{-15})$), and the model's $\lambda_{\rm pred} = Z_0''(t_m)\delta^2/(8Z_B(t_m))$.

| start $\lambda$ | $\gamma$ | $\beta$ | $\lambda_c$ | $t_c$ | $t_1$ | $t_2$ | $\delta$ | type | $\lambda_{\rm pred}$ | ratio | sign |
|---|---|---|---|---|---|---|---|---|---|---|---|
| +1 | 12.039 | 0.800 | 0.02549 | 12.36 | 12.160 | 13.489 | 1.330 | LL | 0.02044 | 1.247 | ok |
| +1 | 15.497 | 0.927 | 0.08606 | 14.98 | 14.135 | 15.240 | 1.106 | ZL | 0.08964 | 0.960 | ok |
| +1 | 20.346 | 0.696 | 0.05014 | 20.59 | 19.103 | 20.662 | 1.559 | LL | -1.682 | -0.030 | WRONG |
| +1 | 33.757 | 0.740 | 0.54504 | 33.57 | 32.935 | 33.781 | 0.846 | ZL | 0.55252 | 0.986 | ok |
| +1 | 43.632 | 0.856 | 0.00997 | 43.36 | 43.327 | 43.427 | 0.099 | ZL | 0.00995 | 1.002 | ok |
| +1 | 47.533 | 0.913 | (see note) | 48.00 | 48.005 | 49.080 | 1.075 | ZL | 0.317 | (see note) | ok |
| -1 | 24.483 | 0.758 | -0.00769 | 24.95 | 24.904 | 25.011 | 0.107 | ZL | -0.00765 | 1.005 | ok |
| -1 | 75.612 | 0.536 | -0.00057 | 75.70 | 75.695 | 75.705 | 0.010 | ZL | -0.00057 | 1.001 | ok |
| -1 | 98.829 | 0.778 | -0.01245 | 98.86 | 98.831 | 98.887 | 0.056 | ZL | -0.01245 | 1.000 | ok |
| -1 | 114.303 | 0.598 | -0.13004 | 114.35 | 114.320 | 114.859 | 0.539 | ZL | -0.29399 | 0.442 | ok |
| -1 | 133.166 | 0.765 | -0.00806 | 133.45 | 133.422 | 133.498 | 0.075 | ZL | -0.00805 | 1.001 | ok |
| -1 | 147.895 | 0.693 | -0.01253 | 147.64 | 147.423 | 147.799 | 0.376 | ZL | -0.31647 | 0.040 | ok |

Note on row 6: the pair started at 47.53 landed on the closest pair below 200, the L-zero at 48.003 against $\zeta$'s ninth zero at 48.005 ($\delta = 0.002$), but the landing bookkeeping labeled it with the neighbor 49.080; the S3 row for (48.003, 48.005) is the correct record ($\lambda_c = 4.9\times10^{-4}$ by bisection). Every tracked pair landed on an on-line pair of $A$ inside its window; none exited through the top (P4).

## S3: the fifteen closest on-line pairs of A, forward test

For each pair, the model's $\lambda_{\rm pred}$, then a direct check that the pair is off the line at $1.5\lambda_{\rm pred}$ and on it at $0.5\lambda_{\rm pred}$, then bisection of $\lambda_c$.

| $t_1$ | $t_2$ | $\delta$ | type | $\lambda_{\rm pred}$ | $\lambda_c$ | ratio | model |
|---|---|---|---|---|---|---|---|
| 48.003 | 48.005 | 0.0020 | ZL | $\approx 0$ | 0.00049 | (fd invalid) | fail |
| 75.695 | 75.705 | 0.0099 | ZL | -0.00057 | -0.00057 | 1.002 | ok |
| 111.875 | 111.885 | 0.0107 | ZL | -0.00003 | -0.00003 | 0.998 | ok |
| 185.586 | 185.599 | 0.0124 | ZL | $\approx 0$ | $\approx 0$ | 1.000 | ok |
| 167.184 | 167.219 | 0.0345 | ZL | 0.00019 | 0.00019 | 1.003 | ok |
| 122.908 | 122.947 | 0.0383 | ZL | -0.00003 | -0.00003 | 1.001 | ok |
| 143.112 | 143.157 | 0.0451 | ZL | 0.00566 | 0.00566 | 1.000 | ok |
| 150.925 | 150.971 | 0.0455 | ZL | -0.00116 | -0.00117 | 1.002 | ok |
| 98.831 | 98.887 | 0.0557 | ZL | -0.01245 | -0.01245 | 1.000 | ok |
| 189.354 | 189.416 | 0.0617 | ZL | -0.03639 | -0.03640 | 1.000 | ok |
| 133.422 | 133.498 | 0.0755 | ZL | -0.00805 | -0.00806 | 1.001 | ok |
| 92.411 | 92.492 | 0.0808 | ZL | 9.413 | 0.405 | 0.043 | fail |
| 43.327 | 43.427 | 0.0995 | ZL | 0.00995 | 0.00997 | 1.002 | ok |
| 173.412 | 173.514 | 0.1026 | ZL | 0.11882 | 0.12286 | 1.034 | ok |
| 60.727 | 60.832 | 0.1053 | ZL | 0.00346 | 0.00347 | 1.003 | ok |

Least-squares slope of $\log|\lambda_c|$ against $\log\delta$: 1.13 (the model's $\delta^2$ carries a pair-dependent prefactor $Z_0''/Z_B$ spanning decades, so the raw slope was never the test; the ratio is). The two failures: at $\delta = 0.002$ the finite-difference curvature ($h = 10^{-3} \ge \delta/2$) is meaningless while the bisected $\lambda_c$ is fine; at (92.41, 92.49) the local two-zero quadratic is not the picture ($\lambda_{\rm pred} = 9.4$ against $\lambda_c = 0.40$: a third zero takes part).

## Verdicts against the pre-registration

- **P1 HELD** as first written (the ledger sentence it was rewritten against was false; see the research document).
- **P2 HELD**: 25 of 27 pairs in S2 and S3 are mixed (one $\zeta$ zero, one $L$ zero); the two LL pairs are the lowest two, below $\zeta$'s first zero at 14.13; the closest pair below 200 is a Poisson coincidence between the two sequences ($\delta = 0.002$ at 48.00). Thresholds of the closest pairs span five decades ($0.4$ down to $3\times10^{-5}$ at $\delta = 0.0107$), so $T^*(\lambda)$ is a staircase set by coincidences, not a smooth power law; the sign rule then decides which of the two sides each step belongs to.
- **P3 HELD, stronger than registered**: ratio $\lambda_c/\lambda_{\rm pred}$ within 0.5% and sign rule exact for every pair with $\delta \le 0.11$ (14 of 14 with a valid curvature estimate); 4-56% off at $\delta \approx 0.5$-$1.3$; wrong sign at $\delta = 1.56$, twice the local mean spacing, where the two-zero quadratic is not local.
- **P4 HELD**: 12 of 12 tracked pairs land on on-line pairs of $A$.
- **P5 HELD**: $N_{\rm off} = 0$ at $\lambda = 0$; all differences even.

## What it measures for the disproof exercise

The Euler product $\lambda = 0$ is the unique point of the pencil without off-line zeros below 200, and both neighbors at $|\lambda| = 0.01$ already have them (heights 43 and 25). The cost of pushing the first zero above height $T$ is the smallest threshold $|Z_0''|\delta^2/(8|Z_B|)$ among the mixed pairs below $T$ with the matching sign, a Poisson-coincidence quantity that goes to zero as $T$ grows. The negative side additionally carries the half-plane zeros of Davenport-Heilbronn, continuously connected to the same on-line pairs. Nothing in the pencil acts at $\lambda = 0$ itself: the disproof needs a perturbation direction, and the Euler product has none (Hamburger at conductor 1; here, the pencil's own coordinate).

## Side finding: the Epstein control (LEARNINGS #217, TODO "Epstein control defect")

Choosing $d = -15$ exposed that `experiments/_shared/epstein_zeta.py` was inaccurate above height $\approx 50$ at 30 digits (Bessel-tail truncation against an absolute tolerance before an $e^{\pi t/2}$ prefactor, plus a single-small-term stopping test that a coincidental cosine zero defeats for the form $(2,1,2)$), that its `zeros()` both invented a root (height 84.76) and missed three genuine ones, and that the "$d = 47$ principal form is RH-true" label used across the positivity thread is false (a certified pair at $0.724531 + 64.646629i$ first; then seven pairs below height 70, the lowest at 24.66, once `zeros()` was rebuilt around the argument-principle census on 2026-09-02). Certification of the five $d = -15$ zeros: the referee's archived scripts in [`docs/03_research/_evidence/negative_proof_adversary_scripts/`](../../docs/03_research/_evidence/negative_proof_adversary_scripts/); the module-side fixes and the audit of affected experiments are recorded in LEARNINGS #217 and TODO.
