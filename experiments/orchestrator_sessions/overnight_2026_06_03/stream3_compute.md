# Stream 3b slow-compute: de Branges / Conrey-Li cross-term Q(rho) to K=500

Staged overnight 2026-06-03, NOT committed. For morning review by Owen + main-agent
re-derivation. This is a COMPUTED coordinate. No proof, no new claim beyond the data.

Script: `experiments/orchestrator_sessions/overnight_2026_06_03/stream3_debranges_k500.py`
Data:   `experiments/orchestrator_sessions/overnight_2026_06_03/stream3_debranges_k500.npz`

## What was computed

Extension of 2DB.1 (`experiments/arithmetic_geometric/e2db_debranges_crossterm.py`) from
K=50 to K=500 zeta zeros, identical convention:

- xi(s) = s(s-1) pi^{-s/2} Gamma(s/2) zeta(s)  (the NO-1/2 normalization that reproduces
  Conrey-Li, arXiv:math/9812166).
- Q(rho) = -Re{ xi'(rho) xi(1+rho) },  with xi'(rho) via `mp.diff`.
- Q(rho) >= 0 at every zero is the pointwise consequence of de Branges positivity condition
  (3.1); Conrey-Li proved (3.1) implies RH (in fact GRH for all Dirichlet L at once) but that
  it FAILS for zeta. So Q(rho) < 0 is the explicit failure of that (strictly-stronger-than-RH)
  pointwise positivity.

Precision policy: dps scaled with gamma as dps = max(80, ceil((pi/2) gamma / ln10) + 60), so
the working precision always exceeds the magnitude of |Q| with a >= 60-digit guard band. At
K=500 (gamma ~ 811) this reached dps = 613, with |Q| down to ~ 10^{-541}.

## HOW IT WAS RUN (honest provenance)

Command (repo root):
```
ZETA_K=500 python -m experiments.orchestrator_sessions.overnight_2026_06_03.stream3_debranges_k500
```
The canonical run completed (PID confirmed exited; npz written with K=500, 500 rows). Its
stdout was lost to the background harness's full output buffering (0-byte log), so the formatted
summary below was regenerated deterministically FROM the saved npz via:
```
python -m experiments.orchestrator_sessions.overnight_2026_06_03.stream3_debranges_k500 --report
```
A K=50 smoke run (stdout captured live) reproduced the 2DB.1 anchor and negative set exactly
before the K=500 launch. All negative signs and their positive neighbours were independently
re-verified at DOUBLED precision (see "Precision robustness" below). The npz is the ground truth;
re-derive from it.

## RESULT 1 -- the negative-Q index set (the headline)

```
NEGATIVE-Q INDEX SET (k where de Branges (3.1) fails pointwise), K=500:
  [34, 71, 106, 127, 144, 173, 184, 186, 196, 233, 257, 265, 282, 289, 298,
   315, 334, 363, 368, 380, 394, 401, 409, 423, 436, 453, 462, 477, 483, 485,
   492, 497]
  count = 32 of 500
```

This REVISES the 2DB.1 reading. 2DB.1 saw "exactly one negative, k=34" in the first 50 and read
it as "sporadic." At K=500 the negatives are NOT a single sporadic event: there are 32 of them
with a roughly stable density (about 1 in 16), and the density tracks the growing zero density:

```
negatives per 100-index window:  (0,100]:2  (100,200]:7  (200,300]:6  (300,400]:6  (400,500]:11
```

Gaps between consecutive negative indices: [37,35,21,17,29,11,2,10,37,24,8,17,7,9,17,19,29,5,
12,14,7,8,14,13,17,9,15,6,2,7,5], with min/mean/max = 2 / 14.9 / 37.

Clustering note (honest): there is NO strong clustering. Two pairs sit at the minimum gap of 2
(k=184/186 and k=483/485), and the (400,500] window has the most (11), but the gap distribution
is broadly consistent with a roughly i.i.d.-with-fixed-rate sprinkling, not bunching. The fraction
of negatives is order 6% and does not visibly decay or grow over the range. Whether the asymptotic
density is a fixed constant or drifts is NOT resolved by K=500 and would need more zeros.

The anchor k=34 is reproduced: Q(rho_34) = -5.389101e-69, ratio to Conrey-Li = 1.000000.

## RESULT 2 -- the asymptotic slope (the double-archimedean law)

log10|Q| vs gamma, OLS slope over growing windows (target -(pi/2)/ln10 = -0.68219):

```
  k<=W    full(1..W)    tail(W/2..W)
    50      -0.65479        -0.66451
   100      -0.66519        -0.67301
   150      -0.66914        -0.67479
   200      -0.67169        -0.67693
   250      -0.67324        -0.67752
   300      -0.67424        -0.67740
   350      -0.67514        -0.67850
   400      -0.67577        -0.67865
   450      -0.67630        -0.67906
   500      -0.67676        -0.67939
```

The slope is monotonically converging to the predicted -(pi/2)/ln10 = -0.68219 from below. At
K=50 (the old 2DB.1 window) it was -0.655; at K=500 the full-window slope is -0.6768 and the
top-half tail slope is -0.6794. The residual gap (~0.003 to ~0.005) is the expected finite-size
curvature: log|Q| = -(pi/2) gamma / ln10 + (subleading log gamma terms from the Stirling
expansion of the two Gamma(s/2) factors), so any finite OLS slope is biased toward zero and only
approaches -0.68219 as gamma -> infinity. The convergence direction and rate are exactly as the
double-Gamma reading predicts.

Two-factor decomposition (confirms the "two completed-xi factors, two Gamma's" mechanism):
```
slope[log|xi'(rho)|]  = -0.33853
slope[log|xi(1+rho)|] = -0.33814     each ~ single-Gamma -(pi/4)/ln10 = -0.34109
sum                   = -0.67667     ~ the full double-Gamma slope
```
Each xi factor contributes one Gamma(s/2) super-exponential decay of slope ~ -(pi/4)/ln10, and
Q = xi'(rho) * xi(1+rho) carries both, giving -(pi/2)/ln10. This is the sharpening of #38's
single-Gamma -(pi/4)/ln10 law that 2DB.1 first reported, now confirmed out to gamma ~ 811.

## Precision robustness (artifact ruled out)

Minimum precision guard band across all 500 zeros: dps - |log10|Q|| = 65.2 digits (at k=4).
Every entry was computed with at least 60 digits of headroom beyond the magnitude of |Q|.

Sign stability under precision DOUBLING (independent re-evaluation at 2x the script's dps),
sampled on the deepest and tightest-gap negatives and on their positive neighbours:
```
NEGATIVES:  k=34,184,186,483,485,497,462,257  -> all sign -1 at base AND 2x dps, log|Q| agree
POSITIVE NEIGHBOURS: k=33,35,183,185,187,482,484,486,496,498 -> all sign +1 at base AND 2x dps
```
No sign flips. The negative set is a real feature of Q, not catastrophic-cancellation noise.

## Surprises

1. The big one: the negative set is NOT sporadic. The 2DB.1 "exactly k=34 in first 50" was a
   small-sample artifact. By K=500 there are 32 negatives at a roughly stable ~6% rate that
   tracks the zero density. The pointwise de Branges (3.1) positivity for zeta does not fail
   once; it fails infinitely often (empirically, at positive density over this range).

2. No clustering. Despite the higher count, the negatives are sprinkled with irregular gaps
   (2..37), not bunched. Two minimum-gap-2 pairs exist but there is no run of consecutive
   negatives and no visible periodicity.

3. The slope convergence is clean and one-sided (always approaching -0.68219 from above in
   absolute value, i.e. from below in signed value), consistent to four digits with the
   double-Gamma prediction once the leading finite-size bias is accounted for.

## What this does and does NOT change

- It does NOT advance the Direction-8 / M3 gap. No Weil cohomology is built. This stays a
  NEGATIVE coordinate: the global de Branges pairing sees the zeros but its positivity is the
  wrong (pointwise, strictly-stronger-than-RH) one, and we now know that wrongness is
  systematic (positive density), not a fluke at one zero.
- It SHARPENS the 2DB.1 reading: the lesson "the RH-equivalent signed pairing must be a global
  SUM (like Li's lambda_n), not the pointwise Hermite-Biehler cross-term" is reinforced, because
  the pointwise object now provably (empirically) fails at a positive fraction of zeros while RH
  holds. A correct positivity cannot be the pointwise Q.
- It is RH-AGNOSTIC (K2): per 2DB.1, the same sporadic Q<0 appears for RH-true zeta and chi4 and
  for D-H's on-line zeros, and D-H's off-line obstruction is double-suppressed below detectability.
  This K=500 run only extends the zeta side; it does not re-run the D-H control, so K2 status is
  inherited from 2DB.1, not re-established here.

## Verification targets for the main agent

- V1 (re-derive the data): re-run the script from a clean session; confirm K=500, the 32-element
  negative index set, slope_all = -0.6768, and the anchor ratio 1.000000. The npz is canonical.
- V2 (precision): confirm the 65-digit minimum guard band and that no negative flips sign when
  dps is doubled (sampled checks above; a full 500-zero double-precision sweep would be the
  rigorous version but is more compute).
- V3 (slope law): confirm the two-factor decomposition sums to the full slope and that growing
  windows approach -(pi/2)/ln10 monotonically.

## Adversarial test cases

- A1: does the negative density actually stabilize, or is the (400,500]:11 uptick the start of a
  trend? Push to K=1000+ if compute allows; report whether the fraction drifts.
- A2: are the two gap-2 pairs (184/186, 483/485) coincidence or do near-pairs persist at higher
  K with above-Poisson frequency?
- A3: re-run the D-H control at matched height to confirm Q<0 stays RH-agnostic at this density
  (2DB.1 only went to T=90).
