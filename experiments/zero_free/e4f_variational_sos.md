# e4f: Bombieri variational SOS does NOT escape the 4E.3 Fejer wall

> Experiment [`e4f_variational_sos.py`](e4f_variational_sos.py).
> Run `python -m experiments.zero_free.e4f_variational_sos` (cache to `_cache/`).
> First computation of Direction 6 ([`../../docs/03_research/research_directions/06_bombieri_variational_sos.md`](../../docs/03_research/research_directions/06_bombieri_variational_sos.md)),
> previously "research-grade, beyond project scope, no code."

## The question

The 4E.3 line-restriction lemma: a NON-NEGATIVE bivariate trig polynomial $P(x,y)$, restricted to
$\phi = 2\theta$, gives a 1D non-negative polynomial $Q(\theta) = P(\theta, 2\theta)$ whose $c_1/c_0$
is capped by the 1D Fejer ceiling at the matched effective degree. For bidegree $(2,2)$ the restriction
has effective degree 6 and the ceiling is $2\cos(\pi/8) = 1.84776$. Every LP/SDP relaxation of the
non-negative cone saturates this and cannot exceed it (e4e6-e4e8, ratio 1.0000).

The Bombieri variational SOS RELAXES non-negativity: allow $P$ slightly negative, penalized by
$\|P_-\|^2 = \int \max(0,-P)^2$. The feasible set is strictly larger than the non-negative cone, so it
is OUTSIDE the LP/SDP family and might escape 4E.3. The decisive test (Direction 6 sec 5.5): for each
target ratio $r$,

$$\min_{c}\ \|P_-\|^2 \quad\text{s.t.}\quad c_1(Q)=r,\ c_0(Q)=1,\qquad P(x,y)=\sum_{j,k\le 2} c_{jk}\cos(jx)\cos(ky).$$

If $\min\|P_-\|^2 = 0$ for $r \le 1.8478$ and becomes positive exactly as $r$ crosses it, Fejer is the
non-negative-cone boundary and super-Fejer ratios REQUIRE genuine negativity (no escape). If $\|P_-\|^2$
stays $\approx 0$ past Fejer, the variational SOS escapes 4E.3 (a real Architecture-4 advance).

## Result: no escape (prediction holds), the boundary is razor-sharp at Fejer

| target $c_1/c_0$ | $\min\|P_-\|^2$ | vs Fejer |
|---|---|---|
| 1.70 - 1.84 | **0.000** | $\le$ Fejer |
| 1.86 | 2.7e-6 | > Fejer |
| 1.88 | 3.2e-5 | > Fejer |
| 1.90 | 1.1e-4 | > Fejer |
| 1.92 | 2.4e-4 | > Fejer |
| 1.94 | 4.2e-4 | > Fejer |
| 1.96 | 6.7e-4 | > Fejer |

$\|P_-\|^2$ is exactly 0 up to the Fejer ceiling (a genuinely non-negative $P$ realizes every $r \le
1.8478$) and turns positive precisely as the target crosses it, growing smoothly. So the variational
relaxation buys super-Fejer $c_1/c_0$ only by paying L^2-negativity, and the cost rises continuously
from exactly the cone boundary. The 4E.3 line-restriction lemma EXTENDS to the Bombieri variational
setting, sharpening the LP/SDP saturation (e4e6-e4e8) one rung further: the wall is not an artifact of
the non-negative-cone relaxation, it survives the one relaxation built to escape it.

This is the marginal-positivity thesis on the Architecture-4 side: the figure of merit is pinned at the
cone boundary, with no soft slack to exploit. Per Direction 6 sec 5.6 the next milestone (whether the
small negativity translates to a better zero-free-region constant) is predicted negative by sec 6; the
sec 5.5 test settled here is the decisive one and it is no-escape.

## What is PROVEN vs numerical

- **NUMERICAL (this experiment):** the $\|P_-\|^2$-vs-$r$ table, via multi-start SLSQP on a 64x64 grid
  for the penalty and a 1024-point grid for the linear restriction coefficients $c_0(Q), c_1(Q)$. The
  exact-0 below Fejer means the minimizer found genuinely non-negative $P$; the positive values above
  are small but monotone and clearly bounded away from 0.
- **IMPORTED:** the Fejer ceiling $2\cos(\pi/8)$ at effective degree 6 (4B/4E.8); the 4E.3 lemma and the
  LP/SDP saturation (e4e6-e4e8).
- **CONJECTURAL / scope:** bidegree $(2,2)$ only (matching 4E.8); the sec 5.6 translation to a zero-free
  constant is not run here (predicted negative). Higher bidegree could be swept, but 4E.3 is degree-
  matched so the expectation is the same wall at each matched effective degree.

## Cross-refs

[`../../docs/03_research/research_directions/06_bombieri_variational_sos.md`](../../docs/03_research/research_directions/06_bombieri_variational_sos.md)
(the direction); [`e4e8_sos_sdp.py`](e4e8_sos_sdp.py) (the SOS-SDP that saturates Fejer, 4E.3 Phase D);
[`e4e3_mt_translation.py`](e4e3_mt_translation.py) (the line-restriction lemma); LEARNINGS #12/#15 (the
4E.3 robustness pattern, now extended to the variational relaxation). MEMORY: marginal-positivity thesis.
