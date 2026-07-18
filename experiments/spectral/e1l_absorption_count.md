# E1L: the E-absorption count `1+nu(lambda^2)` as the W6-vs-#143 numerical shadow

> Companion to `e1l_absorption_count.py` / `.npz`. Reuses the e1k D_log operator
> (`build_float`, `operator_spectrum`, `ZETA_CFG`/`DH_CFG`; arXiv:2511.22755
> Thm 5.10) and the e1g genuine concentration operator (`concentration_spectrum`;
> the validated Slepian harness) to measure the CCM archimedean absorption count
> `1 + nu(lambda^2)` and test where it lands on the W6-vs-#143 discriminator
> (LEARNINGS #148/#154; `deligne_weil1_engine_audit.md` W6;
> `ccm_semilocal_prolate.md` lines 349/356-357). It proves nothing about RH. It
> measures one of the four named upgrade-spec ingredients and reports the verdict.

> **BANNER (read before quoting any number).** The absorption count follows the
> lattice law `~2 lambda^2 log lambda`, but `n_win = Twin / phi` is a **lattice
> IDENTITY forced by the window** (`phi * N* = Twin` exactly), not a symmetry-
> computed quantity; the fit confirms the lattice spacing, it cannot discriminate
> "computed" from "installed". The same-lattice-law is family-uniform only in the
> weak sense (D-H clean, zeta pole/ghost-perturbed). It is the **blind
> archimedean/geometry count** (the Slepian/RvM circle-lattice), **installed by
> the two-meter truncation window**, and it is **D-H-blind**. It is NOT a W6 Betti
> count computed by the operator's own symmetry. The exact integer counts
> (`n_win`, `n_neg`) are O(1)-fragile to precision; only the leading law and slope
> verdict are robust. The finite spectrum is NOT perfectly real (O(1) complex
> ghosts, STEP 5). The net verdict is **#143 shell (spectrum budget installed, not
> computed)**, the numerical shadow of the #154 ledger. Do not cite the plateau as
> a W6 hit.

## One-line result

Two counts live in the D_log spectrum. The **raw** count of physical
determinant zeros TRACKS the truncation dimension N (large-N slope
`d/dN = +0.94` for zeta, `+1.00` for D-H) because Thm 5.10(iii) makes the
finite-cutoff zeros real up to an **O(1) complex-ghost residual** (the faithful
e1k build realizes reality only approximately: D-H `65/65` at dps=15, both twins
`63/65` at dps=25 with re~0 ghosts; see STEP 5), so "number of real physical
modes" `= matrix dimension - O(1)`.
The **windowed** count (zeros below the two-meter height `T = 2 pi lambda^2`)
PLATEAUS at an N-independent value (slope `~0` once `N >= N*`), and that plateau
is a stable computed function of lambda: `1+nu(lambda^2) ~ 0.8..0.94 x 2 lambda^2
log lambda = 0.8..0.94 x (T/2pi) log(T/2pi)`, the leading Riemann-von Mangoldt
= circle-lattice count. BUT `N*(lambda) ~ 2 lambda^2 log lambda ~` the count
itself, so the plateau barely separates from N, and the plateau value equals the
CIRCLE-GEOMETRY lattice count (the density-gate two-meter coincidence e1f/e1g
already validated), not an arithmetic invariant. **Zeta and D-H give the same law
and the same verdict (blind).** Verdict: **#143 installed shell, confirmed.**

## The three observables (why three)

The spec names two proxies, "Sonin count" `n_neg` and "physical determinant
zeros" `n_phys`. On this testbed they measure different objects, so we report
three, all from the same faithful e1k `build_float` (mpmath dps=25):

| observable | definition | what it is |
|---|---|---|
| `n_neg` | `#{eigenvalues of the truncated Weil form Q < 0}` | the positivity-margin / Sonin block of `Q` (NOT the bare prolate `W_lambda`); small (0-2), razor-thin-margin-sensitive |
| `n_raw` | `#{real zeros of xihat, re>1}`, **no height cap** | the raw operator spectrum; = ~D/2, TRACKS N |
| `n_win` | `#{real zeros of xihat, 1 < re < T}`, `T = 2 pi lambda^2` | the physically resolved absorption count `1+nu` |

Note `n_neg` and `n_phys` do NOT "agree up to O(1)" here (`n_neg ~ 0-2` vs
`n_win ~ 29-31` at lambda=sqrt13): `Q` is the Weil form, not the prolate operator,
so its negative-eigenvalue block is the positivity margin, not the Shannon block.
The genuine Slepian/Sonin absorption count `2c/pi = 4 lambda^2` is recovered
separately by the e1g concentration operator (STEP 3 below).

## STEP 1 (TEST A) -- family-uniformity: PLATEAU (windowed) vs TRACKS-N (raw)

`lambda = sqrt(13)` (`Twin = 81.68`, `N* = 33.3`):

| N | D | ZETA n_neg | n_raw | n_win | D-H n_neg | n_raw | n_win |
|---|---|---|---|---|---|---|---|
| 8 | 17 | 0 | 4 | 4 | 0 | 7 | 7 |
| 16 | 33 | 0 | 15 | 15 | 0 | 15 | 15 |
| 24 | 49 | 2 | 23 | 22 | 0 | 23 | 23 |
| 32 | 65 | 2 | 31 | 30 | 0 | 31 | 30 |
| 40 | 81 | 2 | 38 | **29** | 0 | 39 | **31** |
| 48 | 97 | 2 | 46 | **29** | 0 | 47 | **31** |

Large-N slopes: ZETA `n_raw = +0.937`, `n_win = -0.063`; D-H `n_raw = +1.000`,
`n_win = +0.062`. The windowed count is flat past `N* ~ 33`; the raw count keeps
tracking N. Same picture at `lambda = 3.0` (`N* = 19.8`): `n_win` plateaus at 13
(zeta) / 19 (D-H), `n_raw` slope `+1.0` for both.

**The single decisive number:** the RAW physical-zero count has `d(nu)/dN ~ +1`
(TRACKS N = installed). The plateau only appears once the external two-meter
window `T = 2 pi lambda^2` is imposed, and `N*(lambda) ~ count`, so the plateau
barely separates from the truncation dimension. That is exactly the #143 signature
"count fixed by the truncation/window, RvM only at the edge".

## STEP 2 (TEST B) -- the lambda-law of the plateau `1+nu(lambda^2)`

Plateau values (`n_win` at `N >= N*`) fit against the two computed laws:

| lambda | 2.2 | 2.6 | 3.0 | 3.606 |
|---|---|---|---|---|
| ZETA `1+nu` | 3 | 11 | 13 | 29 |
| D-H `1+nu` | 7 | 12 | 19 | 31 |

| twin | Shannon `a(4 lam^2)` | RvM/lattice `a(2 lam^2 log lam)` | power `C lam^b` |
|---|---|---|---|
| D-H | a=0.540, rms **0.152** | a=**0.936**, rms **0.016** | b=**3.024**, rms 0.027 |
| ZETA | a=0.457, rms 0.310 | a=0.804, rms **0.173** | b=4.309, rms 0.219 |

**This fit is not a discriminating test.** Because `phi * N* = Twin` holds
EXACTLY by construction (`phi = pi / log lambda`, `N* = 2 lambda^2 log lambda`,
`Twin = 2 pi lambda^2`; verified independently, `81.68 = 81.68`), the windowed
count `n_win = #{grid points phi*n in (1, Twin)} ~ Twin / phi = 2 lambda^2 log
lambda` is a **lattice-counting IDENTITY forced by the window choice**, not a
quantity the operator computes by its own symmetry. So the RvM-vs-Shannon fit can
only confirm the fixed lattice spacing `phi = pi / log lambda`; it CANNOT
discriminate "computed by symmetry" from "installed by the window", because here
the two coincide. With that caveat: the count tracks the lattice law `2 lambda^2
log lambda`, not the flat Shannon `4 lambda^2`. **D-H** (the pure archimedean
lattice, no pole) fits the lattice law cleanly (`a ~ 0.94`, 1.6% residual,
effective exponent `b ~ 3` because the `log lambda` factor amplifies the apparent
power over this range). **Zeta** is a `~2x` low-lambda outlier (`3` vs predicted
`~6`) and noisier overall (`a ~ 0.80`, 17% rms) because the rank-2 pole term and
the ghost artifact perturb the low-lambda counts. By the two-meter law
`2 lambda^2 log lambda = (T/2pi) log(T/2pi) = N(T)` at `T = 2 pi lambda^2`, this
leading-RvM law and the geometric circle-lattice count `Twin * L / (2 pi)` are the
SAME number. So the law is family-uniform in the weak sense of "same fixed lattice
spacing" (D-H clean, zeta pole/ghost-perturbed), and it is the BLIND geometry
coincidence installed by the window, not an arithmetic invariant the operator
computes.

## STEP 3 -- genuine Slepian plunge (e1g concentration operator)

Symmetric time-bandwidth `U0 = S0 = sqrt(c)`, `c = 2 pi lambda^2`:

| lambda | c | n>1/2 (absorbed) | `2c/pi = 4 lam^2` | plunge in (0.1,0.9) | `(2/pi^2) log c log 9` |
|---|---|---|---|---|---|
| 3.606 | 81.7 | **52** | 52.00 | 4 | 1.96 |
| 3.000 | 56.5 | **36** | 36.00 | 4 | 1.80 |
| 4.000 | 100.5 | **64** | 64.00 | 4 | 2.05 |
| 5.000 | 157.1 | **100** | 100.00 | 4 | 2.25 |

The count near 1 is **exactly** the Shannon number `2c/pi = 4 lambda^2`, and the
plunge width is `O(log c)` (measured 4, vs the Landau-Widom leading `~2`; the
factor ~2 is the known finite-c correction, and 4 is not tracking `c`). So the
log-circle IS a genuine time-bandwidth concentration machine: the absorbed count
is family-uniform and COMPUTED. But e1g already showed it is **reweighting-blind**
(a random non-arithmetic multiplier gives the identical spectrum), so this
computed count is BLIND: it cannot carry the prime signature. This is the
geometric floor the D_log determinant-zero count sits on.

## STEP 4 -- D-H control: BLIND (identical law, identical verdict)

`1+nu` across the grid: ZETA `[3, 11, 13, 29]`, D-H `[7, 12, 19, 31]`. The
per-point differences are O(1). They are NOT a clean archimedean-density signal:
a substantial part of the gap (`29 vs 31` at `lambda=sqrt13`; part of `13 vs 19`
at `lambda=3`) is the **complex-ghost / conditioning artifact** described in
STEP 5. The `|Im|` filter drops the 2-4 zeta eigenvalues that the non-normal,
`~1e-4` G-self-adjoint zeta operator throws off the real axis, depressing zeta's
real windowed count below D-H's clean grid count (D-H `n_raw = N` exactly, real to
`~1e-12` at dps=15). The rest of the gap is the zeta-only rank-2 pole term, which
makes the low-lambda counts irregular (the `3 -> 11` jump). D-H fits the RvM law
CLEANER than zeta for the same reason (no pole, and its O(1) ghosts stay in the
central band out of the physical window at both precisions). Crucially, the artifact
does NOT threaten the blind verdict: the *true* zeta grid count is closer to D-H's,
so removing the ghost artifact makes the twins MORE blindly identical, not less.
Both twins: same plateau-vs-tracks-N slope verdict (STEP 1), same Shannon
`4 lambda^2` in STEP 3, same leading law in STEP 2. The count law does NOT
discriminate zeta from D-H: they share the Gamma-factor archimedean density and the
two-meter law. The only place a genuine difference could hide (D-H's off-line zero
at `gamma ~ 85.7`) is quarantined to the Section-7 uniform limit (needs
`lambda^2 >~ 5e11`, archimedean stealth suppression `~1e-30`), INVISIBLE at finite
cutoff. Same finding as #158 (finite reality is information-free) and #148 (the
archimedean fragment is K2-blind).

## STEP 5 -- anti-fooling

- **(i) Window removal flips the verdict.** Dropping the `T = 2 pi lambda^2` cut
  turns `n_win` (plateau) into `n_raw` (tracks N): ZETA `N=32 -> n_raw=31`,
  `N=48 -> n_raw=46`. The window does the plateau work; the raw count is installed
  (= matrix dimension).
- **(ii) The finite spectrum is NOT perfectly real; the `|Im|` filter is not
  universally inert.** Thm 5.10(iii) reality is only APPROXIMATELY realized by the
  faithful e1k build (non-normal, `~1e-4` G-self-adjoint), so the twins carry O(1)
  complex "ghost" eigenvalues. Independently reproduced (`build_float` /
  `operator_spectrum`, `N=32`, `lambda=sqrt13`):
  - **dps=25** (e1l's actual run precision, forced by e1g's module-load
    `mp.mp.dps = 25`): BOTH twins `n_real_total = 63/65` (2 ghosts each), and the
    ghosts sit in the central `|re|<1` band (excluded by `RE_CUT`), so
    `n_win = n_win_nofilter = 30` for both. The equality is **ghost PLACEMENT**,
    not total reality. e1l previously read this as "no complex modes to filter" and
    concluded reality was total: that was a coincidence, not a fact.
  - **dps=15** (mpmath default): zeta's ghosts move into the PHYSICAL band,
    `n_real_total = 61/65`, 4 ghosts at `re = +-26.63`, `|Im| = 0.55`, landing
    INSIDE the window. The filter then DOES change `n_win`: `29` (filtered) vs `31`
    (unfiltered). D-H stays `65/65` real at dps=15.
  This is e1k caveat-2 (imperfect pole realization) surfacing, and the earlier
  STEP 5 hardcoded assertion `n_real_total = D (all zeros real)` was FALSE
  (computed value is `61-63` of `65`). STEP 5 now prints the computed
  `n_real_total` and ghost counts instead of asserting them away.
- **(iii) Razor-thin margin.** Ground-state `eps = -3.7e-5` (zeta) / `+3.3e-5`
  (D-H); G-self-adjointness residual `1.2e-5`; `even_assumption_ok = True` at the
  reported cutoffs. Precision-robustness is coarser than earlier stated: the
  **leading law** (`~2 lambda^2 log lambda`) and the **slope verdict** (`d/dN`, to
  `+-1`) are robust, but the **exact integer `n_win` is O(1)-fragile** to precision
  and window-edge placement, in the same class as `n_neg`. At `lambda=sqrt13`,
  `N=32`: `n_win` (zeta) `= 29` at dps=15, `= 30` at dps=25; `n_win` (D-H) `= 31`
  at dps=15, `= 30` at dps=25. Report `n_win` as leading-order `+- O(1)`, not an
  exact operator output.

## Verdict (W6 vs #143)

**#143 shell CONFIRMED (spectrum budget installed, not computed).** The decisive
slope `d(nu)/dN` for the raw physical count is `+0.94` (zeta) / `+1.00` (D-H):
the count is the matrix dimension (up to O(1) ghosts), manufactured by finite
self-adjointness. The honest nuance is that the WINDOWED count follows the lattice
law `~2 lambda^2 log lambda` (the leading RvM = circle-lattice; and the e1g
Shannon `4 lambda^2`) - but `n_win = Twin/phi` is a lattice IDENTITY forced by
`phi*N* = Twin`, not a symmetry-computed quantity. So the apparent "W6-shaped
observable" is really the **blind archimedean/geometry Slepian count** (the
two-meter density coincidence, reweighting-invariant per e1g), installed BY the
truncation window with `N* ~ count`, NOT a Betti count the operator computes by
its own symmetry.
D-H gives the identical law and the identical verdict: **blind**. This matches the
#154 ledger reading that the D_log family is a determinant-class shell around a
#143 self-adjointness core, and it is the numerical shadow of that verdict.

## Overclaim guard (what this does NOT show)

- It does **not** close the W6 upgrade or produce a W6 hit. The family-uniform
  count is the blind geometry one, installed by the window, not computed by
  symmetry.
- It does **not** move any wall. The spectrum budget is measured to be installed,
  exactly the #143 status the finite-cutoff reality theorem already had.
- It does **not** discriminate zeta from D-H. The count law is D-H-blind; the
  discrimination stays quarantined to the unreachable Section-7 / M4 limit.
- It is **one of the four named upgrade-spec ingredients, MEASURED** (the
  absorption-count law), not a proof step. The other ingredients are untouched.
- The testbed inherits e1k's caveats (faithful reimplementation, not the paper's
  exact operator; razor-thin positivity margin; zeta pole term only approximately
  G-self-adjoint; the finite spectrum is not perfectly real, see STEP 5). Robust
  to precision: the LEADING law `~2 lambda^2 log lambda` and the slope verdict
  (`d/dN` to `+-1`). NOT robust: the exact integers `n_neg` AND `n_win`, both of
  which shift by O(1) between dps=15 and dps=25 (ghost contamination and window-
  edge placement move `n_win`). Treat all reported counts as leading-order `+- O(1)`.

## Verification targets (for VERIFIER)

1. **Slope law.** For the raw physical-zero count, `d(nu)/dN -> 1` as `N -> inf`
   at fixed lambda. Thm 5.10(iii) predicts total reality (`n_real_total = 2N+1`),
   but the faithful e1k build realizes it only up to an O(1) ghost residual
   (`n_real_total = 2N+1 - O(1)`, empirically `61-63` of `65` at `N=32`), so the
   formalizable statement is the weaker: the count of positive real eigenvalues is
   `N + O(1)`, driven by the matrix dimension (installed).
2. **Two-meter identity.** `Twin * L / (2 pi) = (T/2pi) log(T/2pi)` at
   `T = 2 pi lambda^2`, `L = 2 log lambda`: the circle-lattice count equals the
   leading RvM count. Pure algebra.
3. **Shannon count.** For the e1g concentration operator at `c = 2 pi lambda^2`,
   `#{eigenvalues > 1/2} = 2c/pi + o(c)` (Landau-Pollak-Slepian). Reproduced
   exactly (52/36/64/100 = 4 lambda^2).

## Adversarial test cases (for ADVERSARY)

1. Push N far past `N*` at fixed lambda (`N = 120+` if compute allows): confirm
   `n_win` stays flat while `n_raw` keeps climbing (no hidden late plateau in
   `n_raw`).
2. Vary the window definition (`T = alpha * 2 pi lambda^2`, `alpha in {0.5, 2}`):
   the plateau value should scale with `alpha`-set `T` as `(T/2pi) log(T/2pi)`,
   confirming the count is set by the window, not by arithmetic.
3. Feed a non-arithmetic coefficient stream (random `Lambda(n)` of matched
   support) into `build_float`: the windowed count law should be UNCHANGED
   (blind), matching e1g's reweighting-blindness control. A stream that moved the
   count law would be a red flag that the probe measures an artifact.

## Reproduce

```
python3 -m experiments.spectral.e1l_absorption_count          # full (~8 min)
python3 -m experiments.spectral.e1l_absorption_count --quick   # smaller sweeps
```
Outputs `e1l_absorption_count.npz` (test-A sweeps + slopes, test-B law fits,
Slepian plunge, D-H control, anti-fooling).
