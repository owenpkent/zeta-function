# Night Findings (2026-05-30)

Running findings log for branch overnight/night-2026-05-30.
Appended in real time; read this for blocked tasks and diagnosis.

## Session status

Initiated 2026-05-30. All tasks COMPLETE. No tasks blocked.

---

## T3 - Green's function cross-check PASSED

All 6 generators (37a1, 389a1, 5077a1) agree to < 1e-5 between
Method 1 (h_hat via iterative doubling) and Method 2 (Arakelov
Green's function formula). No fitted constant.

### Formula correction required

The naive derivation of the Green's function formula misses two corrections.

**Correction 1: Silverman vs Cremona normalization (factor of 2)**

The Weierstrass sigma-based Neron function computes:
  lambda_inf^{Silverman}(P) = log(2pi/omega1) + 3*log|eta| - log|theta1| + correction

which corresponds to h_hat_Silverman = lim (1/2)*log max(|a|,b) / 4^n.

Our e2h.py uses the Cremona normalization h_naive = log max(|a|,b), so:
  lambda_inf^{Cremona} = 2 * lambda_inf^{Silverman}

Without this factor: formula gives h_hat/2 for the unbounded component.

**Correction 2: Im(z_P)^2 term for bounded-oval points**

For points on the bounded oval of E(R) (the second real component),
z_P = a + bi where b = Im(omega2)/2 = Im(tau)*omega1/2 (constant for all
bounded-oval points of a given curve). The formula needs:

  pi * Im(z_P)^2 / (Im(tau) * omega1^2) = pi * Im(tau) / 4

added to the Silverman base formula. For 37a1: correction = pi*0.8189/4 = 0.644.

Without this correction the formula is off by order 1 for bounded-oval points.

**Final correct formula:**
  lambda_inf^{Cremona}(P) = 2 * [log(2pi/omega1) + 3*log|eta(tau)|
                                  - log|theta1(pi*z_P/omega1, q0)|
                                  + pi*Im(z_P)^2 / (Im(tau)*omega1^2)]

For unbounded component: Im(z_P)=0, correction term vanishes.
For bounded oval: correction = pi*Im(tau)/4, a curve constant.

### T3 results

| Curve | P | Method1 | Method2 | Diff |
|-------|---|---------|---------|------|
| 37a1  | (0,0)  | 0.0511106 | 0.0511114 | 7.6e-7 |
| 389a1 | (-1,1) | 0.6866626 | 0.6866671 | 4.5e-6 |
| 389a1 | (0,0)  | 0.3269967 | 0.3270008 | 4.1e-6 |
| 5077a1| (-2,3) | 1.3685725 | 1.3685725 | 6.4e-9 |
| 5077a1| (-1,3) | 1.2050807 | 1.2050811 | 4.5e-7 |
| 5077a1| (0,2)  | 0.9909051 | 0.9909063 | 1.2e-6 |

---

## T2(a) - 234446a1 rank-4 pairing matrix PASSED

The 4x4 canonical height pairing matrix for 234446a1 generators
(6,-1),(4,3),(5,-2),(8,7) is positive definite.

Matrix (n_iter=6):
  [ 0.983711,  0.216649,  0.055036, -0.426240]
  [ 0.216649,  1.176553, -0.167635,  0.000074]
  [ 0.055036, -0.167635,  1.202626, -0.475898]
  [-0.426240,  0.000074, -0.475898,  1.512779]

Positive definite: True. Leading minor determinants all positive.

---

## T2(b) - Local height decomposition PASSED

For all test curves (I_1 reduction at all bad primes):
  lambda_p(P) = 0 for all P (only one Neron model component)
  residual = |lambda_inf + 0 - h_hat| = 0 exactly

Gate passes trivially. The infrastructure (neron_local_height_mult_reduction)
is in place and handles the I_1 case correctly. For curves with I_n (n>=2)
reduction, the formula lambda_p = c*(n-c)/(2n)*log(p) is implemented but
not exercised in this session.

---

## Note on canonical height expected values

The expected values cited in NIGHT_PLAN_004.md for 389a1 and 5077a1
generators were incorrect (possibly from a different normalization or
wrong generators). The Cremona h_naive = log max(|a|,b) normalization
gives:
  389a1 gen (-1,1): h_hat ~ 0.6867 (not ~0.1524)
  389a1 gen (0,0):  h_hat ~ 0.3270 (not ~0.4248)
  5077a1 gen (-2,3): h_hat ~ 1.3686 (not ~0.4109)
  5077a1 gen (0,2):  h_hat ~ 0.9909 (not ~0.0238)

These are the converged values from iterative x-doubling, consistent
with the Green's function.
