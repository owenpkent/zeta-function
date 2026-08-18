# ADVERSARY round on e1z (self-run, 2026-08-17)

Attacks written down before execution. Four posed, **two landed**, and the
one that could have made the whole finding an artifact of a single family did
not.

**VERDICT: PASS_WITH_FIXES.** No claim demoted. Two overreaches in the
dossier's wording corrected, one unverified attribution removed, and the
central result strengthened by a third family that e1z had computed but never
checked.

## The attacks, as posed

| | attack | pre-registered kill condition |
|---|---|---|
| B2 | **An unchecked explanation.** e1z attributes the equilibrium excess `rho - 1` to "the `log M / M` weight term". That is a gesture, and the magnitudes look wrong on inspection (excess 2.69 at M = 100 against `log M / M` = 0.046). | the excess is not `log(2M)/(2 M Gamma)` to within a factor of ~3 |
| B3 | **Does `rho` overshoot?** e1z stops at M = 6400 with `rho` still 0.016 short of `Gamma/G` and calls `Gamma/G` the limit. Pushed further it might cross. | `rho > Gamma/G` beyond what the contraction predicts |
| B5 | **Is `sqrt(gT)` universal?** e1z phrases the maximizer as a property of the band. | the zeta density maximizes elsewhere |
| B6 | **The one that matters.** e1z verifies `rho -> Gamma/G` for EQUILIBRIUM and UNIFORM only. It computes `Gamma` for the zeta density and never checks that `rho` goes there. | `rho_zeta` does not approach `Gamma_zeta/G`, which would make the whole `Gamma` story uniform-specific |

## B6: DOES NOT LAND, and is the strongest confirmation in the round

`Gamma_zeta/G = 8.3521` at `g = 13.6, T = 1000`, three times the uniform
value of 2.6817. If `Gamma` only predicted equal spacing, e1z's headline
overreached. It does not:

| M | 200 | 400 | 800 | 1600 | 3200 | 6400 | 12800 |
|---|---|---|---|---|---|---|---|
| `rho`, zeta | 10.741 | 9.322 | 8.780 | 8.547 | 8.442 | 8.393 | 8.370 |
| gap | -2.389 | -0.970 | -0.427 | -0.195 | -0.090 | -0.041 | -0.018 |

converging from ABOVE where uniform converges from below, gap contracting
2.2x per doubling. Three distributions spanning a factor of eight in
`Gamma/G`, each landing on its own `Gamma`. **Promoted to a tracked check,
Z9**, since the module should have carried it in the first place.

## B3: DOES NOT LAND

Pushed two doublings past e1z's grid:

| M | 3200 | 6400 | 12800 | 25600 |
|---|---|---|---|---|
| `rho`, uniform | 2.654271 | 2.666022 | 2.672890 | 2.676818 |
| gap to `Gamma/G` | +0.027465 | +0.015714 | +0.008846 | +0.004918 |

Monotone, always positive, contracting 1.77x per doubling. No overshoot.

## B2: LANDS

The excess is not the claimed quantity:

| M | 100 | 200 | 400 | 800 | 1600 | 3200 | 6400 |
|---|---|---|---|---|---|---|---|
| excess `rho - 1` | 2.6908 | 0.9154 | 0.3847 | 0.1787 | 0.0863 | 0.0424 | 0.0210 |
| `log(2M)/(2 M G)` | 1.9478 | 1.1013 | 0.6144 | 0.3390 | 0.1854 | 0.1007 | 0.0543 |
| ratio | 1.381 | 0.831 | 0.626 | 0.527 | 0.465 | 0.421 | 0.387 |

The ratio drifts steadily from 1.38 to 0.39 rather than settling, because the
excess halves exactly per doubling of M (decay `1/M`) while the predicted
quantity carries an extra slowly-growing `log M`. **Fix: the attribution is
removed.** The dossier now states the measured `1/M` decay and leaves the
subleading structure unidentified rather than guessed at. Nothing else
depended on it.

## B5: LANDS

`sqrt(gT)` is a fact about the uniform family, not about the band:

| family | argmax of `U^sigma` on E | `sqrt(gT)` | ratio |
|---|---|---|---|
| uniform | 115.93 | 116.62 | 0.994 |
| zeta density | **383.95** | 116.62 | **3.292** |

(The uniform row is the empirical-`sigma` check at 30,000 atoms; the
closed-form scan e1z uses gives 1.00000, so the 0.994 is discretization, not
disagreement.) **Fix:** the claim is rescoped to the corollary in the
dossier, and Z7's check name now says uniform-specific and quotes the 3.29.

## Fixes applied to e1z

1. B2's attribution removed, measured `1/M` decay stated instead, with the
   drifting ratio recorded so nobody re-derives the wrong explanation.
2. B5's `sqrt(gT)` rescoped to the uniform corollary in both the dossier and
   the Z7 check name.
3. B6 promoted to a tracked check (Z9); the module is now 12 checks, not 11.
4. B3's extension to M = 25600 recorded in the dossier's Z3/Z4 section.

## What did not move

Every headline claim stands: the rate is `2 Gamma(sigma)`; Theorem V2 is the
`sigma = equilibrium` case and is asymptotically sharp exactly there;
`Gamma > G` strictly otherwise; the missing factor is `(1/2) log T` for equal
spacing; and the typing is unchanged, since `Gamma` is a functional of
`sigma` alone. B6 in particular converts "verified on two families" into
"verified on three spanning 8x in the predicted rate", which is the
difference between a coincidence and a law.
