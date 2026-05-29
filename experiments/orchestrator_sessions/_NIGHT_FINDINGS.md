# Night findings (BLOCKED tasks -- not committed as correct)

## T3 (2N) -- theta/Green's-function cross-check of 2I: BLOCKED (gate failed)

Attempted an independent recomputation of 2I's archimedean local height lambda_inf
via the elliptic logarithm z_P + Jacobi theta_1 Green's function on E(C)=C/Lambda
(experiment e2n_greens_function_crosscheck.py).

GATE: lambda_2I(P) - lambda_theta(P) should be CONSTANT across points P per curve
(constant => the theta route reproduces 2I's z-dependence up to the per-curve metric
constant). RESULT: NOT constant.

| curve | per-point diffs lambda_2I - lambda_theta | spread |
|---|---|---|
| 389a1 | -0.3146, -0.0547 | 0.26 |
| 5077a1 | +0.1525, -0.0839, -0.0536 | 0.24 |

The theta values ARE in the right ballpark (0.5-1.5, comparable to lambda_2I), so the
construction is close, but the z-dependence does not match. Most likely cause (one
honest attempt, not resolved): an elliptic-log branch issue (z_{2P} vs 2 z_P mod
period) or a theta_1-argument convention factor (pi u vs 2 pi u), or the real-period
normalization 2*omega1. Diagnosing requires iterating on these normalization
choices, which is the "thrash" the protocol forbids on a single attempt.

IMPORTANT: this does NOT undermine 2I. 2I's lambda_inf was already validated
INDEPENDENTLY against the canonical height h_hat (the 4^{-n} limit definition), to
1e-5, via lambda_inf + sum_p lambda_p = h_hat. T3 was a SECOND, confirmatory check;
its failure is a failure of THIS theta implementation's normalization, not of 2I.

STATUS: BLOCKED. The blocked attempt is preserved (e2n_greens_function_crosscheck.py,
clearly marked) for a future resumption that fixes the elliptic-log/theta
normalization (gate: difference constant, then derive the constant C(tau) for a
no-fit absolute match).
