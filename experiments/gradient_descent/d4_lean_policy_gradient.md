# D4: meta-level gradient descent on the search for the RH proof (function-field rehearsal)

> Experiment [`d4_lean_policy_gradient.py`](d4_lean_policy_gradient.py).
> Run `python -m experiments.gradient_descent.d4_lean_policy_gradient` (curves cache to `_cache/`).
> Answers the conversation request "help figure out how to turn this into a gradient descent
> problem." Companion to the design study (5 framings surveyed + scored) and
> [`../../docs/03_research/optimizing_rh_for_ai.md`](../../docs/03_research/optimizing_rh_for_ai.md).

## The question

Every object-level variational form of RH is already a gradient-descent problem and already
built in this repo: Nyman-Beurling / Baez-Duarte is least-squares ([`../criticality/e_nb_baez_duarte_dh.md`](../criticality/e_nb_baez_duarte_dh.md)),
de Bruijn-Newman is a heat/log-gas flow ([`../criticality/e_dbn_flow_dh.md`](../criticality/e_dbn_flow_dh.md)),
the Weil-Gram $\lambda_{\min}$ is an SDP ([`../positivity/`](../positivity/)). Descent on all of
them converges and none cracks RH, for two reasons that together ARE the marginal-positivity
thesis in optimization language:

1. **Zero-margin optimum.** $d_N \to 0$ only as $1/\log N$; $\lambda_{\min}(M^\zeta)\to 0^+$;
   the moment matrix is positive *semi*-definite, singular at the RH point. The gradient
   vanishes at the answer with no certificate of which side you are on.
2. **D-H-blind data.** The gradient only ever sees $L$ on the critical line, where an off-line
   zero is archimedean-suppressed ($\exp(-\tfrac{\pi}{4}\gamma)\approx 6\times10^{-30}$). Descent
   on $\zeta$ and on Davenport-Heilbronn is observably identical.

D4 is the one framing that moves the gradient **off the analytic data**. The optimization
variable is a policy $\pi_\theta$ over proof/construction proposals; the gradient is
$\nabla_\theta \log \pi_\theta$ (informative throughout, regardless of marginal positivity);
the terminal reward is the one non-circular value function in the program: **does it typecheck
in Lean.**

## The rehearsal (route A) and the two-tier reward

The policy proposes a Frobenius (integer trace $t$, prime degree $q = p$). The hard reward is
whether [`functionfield_RH_elliptic_of_matrix`](../../lean/ZetaRH/FunctionFieldRH.lean)
(sorry-free) typechecks at the **companion matrix** of $X^2 - tX + p$. Instantiated there, the
theorem has exactly two numeric proof obligations: `Nat.Prime p` and `t^2 ≤ 4p`; everything else
is a fixed lemma application (`companion_det`, `companion_degForm_nonneg`, the eigenvalue
extraction). Hence

$$\text{the Lean file typechecks} \iff \text{isprime}(p)\ \text{and}\ t^2 \le 4p \quad(\text{the Hasse circle}).$$

This equivalence makes `hasse_valid(t, p)` a **faithful, non-circular** Python proxy of the Lean
typecheck. A single `lake env lean` check is ~111 s (Mathlib olean load), so Lean cannot be the
per-episode oracle. The design is two-tier:

- **In the loop:** the proxy `hasse_valid` (a re-derivation of the exact predicate Lean checks).
- **At the end:** `write_lean_validation_file` emits one Lean file instantiating the theorem at
  every converged witness; `lake env lean` validates them in a single run.

## Results

### F1: the loop works (PROVEN-grade; the policy gradient is real)

REINFORCE on the policy logits (tabular softmax over traces, one row per prime; per-prime
running baseline) climbs from chance to a 0.99 trailing hard-reward hit-rate and a 100% greedy
accuracy over 10 primes, learning the prime-dependent Hasse boundary $|t| \le \lfloor 2\sqrt p\rfloor$.

| | ep250 | ep7750 | ep15250 | ep22750 | ep30000 |
|---|---|---|---|---|---|
| hit-rate (trailing 500) | 0.66 | 0.97 | 0.99 | 0.99 | 0.99 |

The gradient is $\nabla_\theta \log \pi_\theta$: a finite, sign-definite advantage whenever a
sampled proposal beats the baseline. It does not vanish because the target signature has zero
margin, because it does not live on the analytic data at all. This is the structural escape from
the marginal-positivity flatness, paid for with reward sparsity rather than gradient flatness.

### F2: D-H by exclusion (the discrimination is structural, not resolution) = MIRROR

The identical loop with a Davenport-Heilbronn target has a hard-reward hit-rate that stays flat
at **0.00**. D-H has no Euler product, hence no Frobenius endomorphism, hence no integer matrix
$A$ with $\det A = p$ and $\deg = \det$. The Lean theorem cannot be instantiated (the action
space is empty) and the `euler_gated` firewall fails. The loop refuses D-H, but by the **easy
half** (absence of an Euler product), exactly the gap that is already closed; it earns no new bit
toward separating $\zeta$ from a hypothetical Euler-product D-H, and never reads the off-line
zero. MIRROR-grade discrimination, as the design study predicted.

### F3: the kernel cliff (the deliverable even on a mirror verdict)

Extending the dense reward to the full Spec($\mathbb{Z}$) shadow battery: coverage climbs to 1.0
(the genuine-m4 shape) while the terminal Lean reward for the actual **open** object stays 0.

| checkpoint added | cumulative $R_{\text{dense}}$ | $R_{\text{hard}}$ (Lean floor, Spec($\mathbb{Z}$) polarization) |
|---|---|---|
| +CP-fq | 0.20 | 0.00 |
| +CP-hodge | 0.40 | 0.00 |
| +CP-ahk | 0.60 | 0.00 |
| +CP-fh | 0.80 | 0.00 |
| +CP-af | 1.00 | 0.00 |

The dense gradient saturates on proven shadows; the hard reward for the Spec($\mathbb{Z}$)
arithmetic polarization (M4/P5) never fires, because that Lean theorem does not exist
([`ArithmeticPolarization.lean`](../../lean/ZetaRH/ArithmeticPolarization.lean) carries the
functional-equation pairing but NOT positivity). The loop produces **zero positive hard examples
on the only open sub-problem.** This is the FLT-shaped cliff named in `optimizing_rh_for_ai.md`,
now measured: $R_{\text{hard}}$ fires only on the closed function-field analogue.

## Tier-two Lean validation

The 10 converged witnesses were written to `_cache/d4_validation_witnesses.lean` and checked with
`lake env lean`: **all 10 typecheck clean** (exit 0, empty output, 21 s warm). The policy's
proposals are genuine, machine-checked function-field RH witnesses, not just proxy-passing.

Negative controls (off-Hasse $t=5, p=5$; non-prime $p=9$) in `_cache/d4_negatives.lean` confirm
the oracle **discriminates** (exit 1): the off-Hasse case errors at the `hHasse` line (`norm_num`
reduces $25 \le 20$ to `False`), the non-prime case errors at the `hp` line (`Nat.Prime 9` to
`False`). So Lean fails exactly where the proxy says it must, empirically confirming
$\text{typechecks} \iff \text{isprime}(p)\ \text{and}\ t^2 \le 4p$.

## What is PROVEN vs numerical

- **PROVEN (theorem, in Lean):** `functionfield_RH_elliptic_of_matrix` is sorry-free; instantiated
  at the companion matrix it typechecks iff `Nat.Prime p` and `t^2 ≤ 4p`. The proxy
  `hasse_valid` is therefore exact, not heuristic. (The single open input of the Lean chain is
  the *existence* of the Frobenius matrix over Spec($\mathbb{Z}$), `FrobeniusMatrixExists`, O1+O2.)
- **NUMERICAL (this experiment):** the learning curve, the 100% greedy accuracy, the D-H flat-zero
  curve, the coverage-climb/hard-flat cliff table. Deterministic (seeded `np.random.default_rng`).
- **CONJECTURAL / scope:** this is a REHEARSAL on the closed function-field case. It trains the
  M4 *move* and measures where the open Spec($\mathbb{Z}$) kernel begins. It does not touch P5
  (the indefinite polarization over Spec($\mathbb{Z}$)), by construction: no checkpoint and no
  Lean theorem reaches that locus.

## Verdict

The meta-level framing is the only one of the five design candidates whose gradient is not the
zero-margin analytic slope and whose discrimination is grounded in non-circular truth (the Lean
floor) rather than a hand-set boolean. It **cracks the closed function-field case** (machine-
validated) and **measures the exact location of the open kernel** (the cliff at the
function-field / Spec($\mathbb{Z}$) boundary). What it does not do, and cannot with the current
Lean floor, is supply a positive hard example on the open arithmetic polarization. The honest
net matches the design prediction: a real, climbable, verifier-grounded loop on the rehearsal; a
sharp measurement of where it stops; no contact with P5.

## Cross-refs

The design study (5 framings: D1 continuous shadow-battery, D2 PSD-cone-distance, D3 adversarial
minimax, D4 this, D5 test-function discriminator); [`../../docs/03_research/optimizing_rh_for_ai.md`](../../docs/03_research/optimizing_rh_for_ai.md)
(lever A shadow battery, lever B Lean floor, "no gradient at the goal"); [`../lemma_db/shadow_battery.py`](../lemma_db/shadow_battery.py)
(the dense reward); [`../../lean/ZetaRH/FunctionFieldRH.lean`](../../lean/ZetaRH/FunctionFieldRH.lean)
(the hard reward); the D-H discipline ([`../_shared/davenport_heilbronn.py`](../_shared/davenport_heilbronn.py)).
MEMORY: marginal-positivity thesis, optimizing-rh-for-ai, lever-b-m1-done.
