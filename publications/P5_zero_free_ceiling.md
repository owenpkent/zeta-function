# Draft skeleton (P5): no higher-dimensional / SDP / SOS escape for the single-zero zero-free constant

> Status: **outline / skeleton**, 2026-06-16. Registry entry: [`../PUBLICATIONS.md`](../PUBLICATIONS.md) P5.
> Reframed after the lit-check. This file exists to make the go/no-go decision explicit: is there a
> standalone paper in the negative residue, or does it fold into the survey (P4)? Read the
> "Go/no-go" section at the bottom first.

## Working title

"A line-restriction obstruction: higher-dimensional, multi-zero, and sum-of-squares generalizations of
the cosine-polynomial method do not improve the single-zero zero-free-region constant."

## One-paragraph thesis

The classical de la Vallée Poussin / Mossinghoff-Trudgian zero-free region for $\zeta$ is driven by a
nonnegative cosine polynomial $P(\theta) = \sum_k c_k \cos k\theta \ge 0$ through a shape factor whose
1D optimum is governed by the Fejér constraint $c_1 \le 2\cos\frac{\pi}{n+2}$. It is natural to ask
whether a *higher-dimensional* inequality, evaluated at several heights at once, can beat the 1D
optimum. We show it cannot, for the asymptotic single-zero constant: every nonnegative multivariate
trigonometric polynomial restricted to a line through the origin is a 1D nonnegative trigonometric
polynomial of matched effective degree, so its shape factor is bounded by the 1D optimum. We
corroborate the obstruction by exhibiting, across the natural escape routes (balanced-sum LPs in
dimension up to four, constrained-domain LPs, naive multi-zero couplings, a Heath-Brown multi-zero
semidefinite program, and a Putinar/Schmüdgen sum-of-squares relaxation), that a genuine
Cauchy-Schwarz-level improvement of up to $+62\%$ exists at the auxiliary-inequality level yet
collapses to no improvement once restricted to the single-zero figure of merit.

## What is NOT claimed (positioning against prior work)

This is load-bearing and goes near the front of the paper. The 1D theory is established and must be
cited, not re-claimed:

- The nonnegative-cosine-polynomial method for the zero-free region is classical (de la Vallée
  Poussin 1899; the $3 + 4\cos\theta + \cos 2\theta$ polynomial).
- The Fejér constraint $|c_1| \le 2\cos\frac{\pi}{n+2}$ is classical (Fejér).
- The modern optimization of the constant $V = \inf_n V_n$ over degree-$n$ cosine polynomials is the
  Mossinghoff-Trudgian program: Mossinghoff-Trudgian, *Nonnegative trigonometric polynomials and a
  zero-free region for the Riemann zeta-function* ([arXiv:1410.3926](https://arxiv.org/abs/1410.3926),
  J. Number Theory 2015); Mossinghoff-Trudgian-Yang
  ([arXiv:2212.06867](https://arxiv.org/abs/2212.06867)); and *Optimal Cosine Polynomials for the
  Riemann Zeta Zero-Free Region* ([arXiv:2411.01385](https://arxiv.org/abs/2411.01385)), which
  computes $V_7, V_8$ exactly and narrows $34.468 < V < 34.504$.
- Our experiment 4B (the 1D LP saturating $\cos\frac{\pi}{n+2}$) **reproduces** this framework. It is
  used here only as the base case, not as a new result.

The contribution is the **negative** statement about the *generalizations*, which I did not find in the
published record.

## Main result (the centerpiece)

**Lemma (line restriction).** Let $P(\theta_1, \dots, \theta_d)$ be a nonnegative real trigonometric
polynomial on the torus $[0, 2\pi]^d$ of multidegree $(N, \dots, N)$. For any heights
$(t_1, \dots, t_d) \in \mathbb{R}^d$, the univariate restriction
$$\tilde P(u) := P(t_1 u, \dots, t_d u)$$
is a nonnegative trigonometric polynomial on $[0, 2\pi]$ whose frequencies are integer combinations
$\sum_i j_i t_i$. Consequently the family of effective 1D polynomials obtained by line restriction is a
*subset* of all 1D nonnegative trigonometric polynomials of the matched effective degree, and the
maximum of the de la Vallée Poussin shape factor over this subset is bounded by the unconstrained 1D
optimum (the Fejér/Mossinghoff-Trudgian value).

*Proof sketch.* Nonnegativity is preserved under restriction to any line because $(t_1 u, \dots, t_d
u)$ is a point of the torus for every $u$. The shape factor in the single-zero argument depends only on
the restricted 1D polynomial, hence is bounded by the 1D optimum. $\square$

This is elementary. The paper's value (if any) is in **assembling it as a systematic no-go** and
verifying that every natural attempt to evade it does evade the lemma's hypotheses yet still fails to
improve the constant.

## Corroborating computations (the escape routes that fail)

| Route | Experiment | Auxiliary-level gain | Single-zero gain | Why it fails |
|-------|-----------|----------------------|------------------|--------------|
| Multivariate balanced-sum LP, $d=2,3,4$ | 4E, 4E.2, 4E.4, 4E.5 | $+25\%$ / $+51\%$ / $\sim{+}62\%$ Cauchy-Schwarz | none | the gain lives in $c_{2,2}$-type modes that land at frequency $2\gamma_0$ in the MT bookkeeping |
| Constrained-domain LP | 4E.6 | apparent, finite-sample | none | recovers the Fejér ceiling as the constraint set densifies (sparse-sampling artifact) |
| Naive multi-zero coupling | 4E.7 | rank-1 optima | none | first-harmonic objectives decompose to tensor products |
| Heath-Brown multi-zero SDP | 4E.9 | best ratio $\le 1$, rank-2 certificate | none | the multi-zero shape factor does not exceed the 1D Fejér ceiling |
| Putinar/Schmüdgen SOS | 4E.8 | saturates, does not exceed | none | SOS confirms but does not escape the line-restriction bound |

All LP/SDP/SOS values carry optimality certificates (cvxpy + CLARABEL/SCS). The auxiliary-level gains
are *genuine* (the bivariate optimum at $\alpha = 3$, $N = 2$ has clean rational coefficients and
provably exceeds the Cauchy-Schwarz tensor bound by exactly $25\%$); the point is precisely that a real
gain at the wrong figure of merit transfers to zero gain at the right one.

## Scope and honest caveats (a dedicated section, not a footnote)

1. **The no-go is about the asymptotic single-zero constant only.** The multi-zero machinery of
   Heath-Brown and Pintz genuinely improves *finite-range* problems (least prime in an arithmetic
   progression, Siegel-zero couplings for specific moduli), where multiple zeros at controlled heights
   are postulated by the problem. The lemma does not contradict that; it constrains the single putative
   off-line zero used for the asymptotic zero-free region.
2. **The line-restriction lemma is elementary.** A referee may regard it as folklore. The defensible
   value is the assembly + the certificates showing the natural evasions all collapse.
3. **The Vinogradov-Korobov $2/3$ exponent** (4A/4C) is a separate input. That it is a ceiling of the
   V-K recipe after Bourgain-Demeter-Guth (2016, sharp Vinogradov mean value theorem) is an expository
   synthesis, not a new theorem, and should be presented as context, not as a result.

## Proposed structure

1. Introduction: the cosine-polynomial method, the question "can higher dimension help?", the answer.
2. Background and prior work (the "what is NOT claimed" section, expanded with the constant $V$).
3. The line-restriction lemma + proof.
4. The escape routes and their certificates (the table, expanded; figures from `experiments/zero_free/`).
5. Scope: single-zero vs finite-range; the V-K context.
6. Conclusion: the soft polynomial method maps its own ceiling; the RH-closing content lives elsewhere.

## Source material in-repo

- `experiments/zero_free/README.md` (now covers 4B-4E.9 + 4A/4C). **Refreshed 2026-06-16** (was stale,
  adversary HIGH-2): the 4E.8 (SOS) and 4E.9 (Heath-Brown SDP) sections are added and the "4E.8 is the
  remaining open direction" line is corrected to "the LP/SDP/SOS family is fully closed." Safe to cite.
- Experiments (cite escape routes by experiment ID): `e4b_nonneg_trig.py`, `e4e_offdiag_lp.py`,
  `e4e2_sum_sweep.py`, `e4e3_mt_translation.py` (the lemma), `e4e4..e4e6`, `e4e7_multi_zero_lp.py`,
  `e4e8_sos_sdp.py` (SOS), `e4e9_heath_brown_sdp.py` (Heath-Brown SDP; ratio = 1.0000 in the `.npz`),
  `4a_4c_vinogradov_korobov.md`.
- LEARNINGS #8, #9, #12, #13, #14, #15. **Do NOT cite LEARNINGS #21 for the Heath-Brown SDP**
  (adversary HIGH-2): under the canonical numbering `### 21.` is the function-field Hodge index (e2g);
  LEARNINGS.md has a #21 collision (an embedded "Finding #21" at ~line 1256). Cite 4E.9 by experiment ID.

## Go/no-go

**Honest read.** After the lit-check, the publishable surface is thin. The 1D headline is pre-empted;
the residue is an elementary lemma plus computational corroboration, scoped to a negative statement
about the asymptotic single-zero constant. Two viable outcomes:

- **(A) Fold into P4.** Make this the "Architecture 4 maps its own ceiling" section of the survey. This
  is the recommended default: the material is strongest as one honest coordinate in the larger
  marginal-positivity / all-roads narrative, where "the soft polynomial method provably cannot close
  RH" is exactly the kind of level-3-vs-level-4 evidence the survey is built on.
- **(B) Standalone short note**, only if a referee-facing expert confirms the multivariate/SDP/SOS
  negative closure is genuinely absent from the literature AND the framing as a clean obstruction
  (not just "we tried and it did not work") lands. Lower probability; needs the line-restriction lemma
  developed into a sharper statement (e.g. an exact matched-effective-degree bound) to carry a paper.

Decision owner: Owen. My recommendation: **(A)**, and treat this skeleton as the seed of P4's
Architecture-4 section rather than a separate submission.
