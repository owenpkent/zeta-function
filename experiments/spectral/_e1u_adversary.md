# ADVERSARY report: e1u canonical-chain rung

> ADVERSARY attack on `experiments/spectral/e1u_canonical_chain.py` /
> `.md` / `.npz`, 2026-07-22, same day as the BUILDER pass. Target: the
> trace-normed canonical-system rung of the compactness-trojan arc
> (LEARNINGS #170 Section-6 spec, `trojan_horse_m4.md`), with the
> SURVEYOR hardening (`remling_suzuki_canonical_pin.md`) as context.
> Grading style follows [`_e1t_adversary.md`](_e1t_adversary.md)
> (PASS_WITH_FIXES format, attack axes, every catch banked). All attacks
> were RUN, not reasoned in the abstract; scratch scripts lived in the
> session scratchpad, outside the repo. Context consumed: e1t (harness,
> T1f, the eps protocol), e1n/e1k (build branch caveats), the Beurling
> and D-H disciplines.

## (a) One-paragraph verdict

The mechanics are clean end to end (exact round trips, byte-reproducible
npz, quick saves nothing, module-identity import with zero copy drift,
K1 guards that genuinely trip, a cold-cache `get_build` that rebuilds
bit-identically at dps 25 with guards armed, and a sane D-H 3.7/36
build), the U4 entanglement measurements SURVIVE attack and come out
sharpened (the 243x asymmetry is pair-specific, 9.7x-490x, and TRACKS
the defect location, which is exactly what the localization reading
predicts), and the U5/T1f admission price reproduces e1t's tracked
record to 0.0. But the rung's two headline claims, the ONLY two new
zeta-first output faces in the whole compactness arc, are both DEAD,
and both died under the probe's own pre-registered controls. (1) The mA
flip is low-band geometry: with the compared band equalized (all three
families restricted to $|t| \ge 13.6$) D-H is first again (0.0012 vs
zeta's 0.0015) and BEUR reaches exact parity (0.0015); at $|t| \ge 20$
all three means agree within 1.3x; a disk beside each family's first
zero puts zeta LAST (0.0342 vs D-H 0.0191); the eps = 0.01 fake reaches
D-H parity (0.0070 vs 0.0068). "Cleanest family on a mid-gap disk" just
means "deepest central gap relative to the disk", which is first-zero-
position data, FE/density-adjacent, the exact residual U3a itself had
named; the builder's kill criterion ("the flip dies if any control
restores D-H-first or BEUR-parity") fired twice over. (2) The U3c
stabilization is a UGRID-floor artifact: the headline "u_half constant
0.025" was the FIRST grid step; on a grid resolving $u < 0.025$ zeta's
u_half collapses (0.0048 then 0.0002), the sup-gaps become ZETA
{0.99, 0.11, 0.0}, D-H {0.85, 0.86, 0.45} (non-stabilizing), BEUR
{0.28, 0.11} (the SMALLEST first gap: the ordering inverts), and after
band equalization the fake reproduces zeta's degenerate pattern exactly
({0.997, 0.016}); the fake's profile behavior is eps-INsensitive
(0.32/0.39 at eps 0.05/0.01), so it was never coarseness either. The
structural reason both faces broke the same way: the gated chains'
giant near-indivisible stretch (the U1 length blowup, i.e. the
relocated #160 type divergence) dominates both instruments, so both
"separations" re-measured the central gap. Three more catches: the
"Weyl profile tail-invariant by construction" claim is FALSE (measured
normalized-profile shifts to 0.283 face A / 0.216 face B under the tail
swap; the profile is germ-supported, not tail-free; VERIFIER target 4
was wrong as stated), the U3a family-blindness is a linear-scale
boundary-saturation read (deltaK spans 1.0e-2 down to 9.2e-14, ZETA
nearest the degenerate boundary by 8-12 orders, and neither deltaK nor
dispersion responds to genuine spectral escape at all: flat 0.64/0.40
with half the mass escaping), and the U3c "information Suzuki's gauge
does not have in print" sentence died with U3c. Net: the pre-registered
Q2 exit FIRES post-round ("no improvement AND (b) family-blind on every
measured face" once geometry is equalized), the rung closes as the
THIRD reformulation (after e1m and e1t), the price-table question is
answered YES-in-disguise (the rate clause's discriminating margin is
the #160 growth clause in Jacobi/Christoffel coordinates), and the
durable products are the exact embedding, the U1 conditioning panel,
the U4 entanglement numbers, and two new tracked negative controls
(U2c, U3d). Verdict: **PASS_WITH_FIXES** on the construction and
mechanics; **FAIL** for the two headline zeta-first faces, both
withdrawn in place.

## (b) Reproduction

| run | expected | observed (before any ADVERSARY change) |
|---|---|---|
| full | 19/19, ~8 s warm | **19/19, 7.9 s warm** |
| npz reproduced | tracked npz regenerated identically | **byte-identical md5 `6c93eb8f...` after rerun** |
| quick | 18/18, ~2 s, no npz | **18/18, 2.2 s, npz md5 unchanged** |
| round trips | worst 1.6e-49 | **1.55e-49 (npz max over all `_rt` keys)** |
| 243x | dm_high/dm_low = 243x | **243.4x (u4_synth), reproduced independently in the sweep** |

Post-ADVERSARY: full **21/21** (~10.6 s warm; +U2c, +U3d), quick
**18/18** (both new checks are full-only: they need the full grid).
npz re-saved with the new keys (u2c_ex136/ex200 per family, u3d_gapsF/
gapsX per family, u6_prof_tailshift), byte-reproducible across
consecutive full runs (md5 `9e67caff...`); quick still saves nothing
(md5-verified).

## (c) Attack axes

### Attack 1: the mA flip (the load-bearing novelty). LANDED (the flip is dead)

The pre-registered kill (adversarial test case 2): the flip dies if a
family-relative disk, symmetric band exclusion, or a finer fake
restores D-H-first or BEUR-parity. Ran all three plus leave-one-out:

- **Symmetric low-band exclusion** (all families compared on
  $|t| \ge T_0$, chains rebuilt from the truncated measures, same
  instruments): at $T_0 = 13.6$ (zeta loses nothing: its first zero is
  14.13) the means become ZETA 0.0015 / **D-H 0.0012** / BEUR 0.0015:
  D-H-first restored AND BEUR parity, on the 2i disk and the 6i disk
  both. At $T_0 = 20$: 0.0010 / 0.0011 / 0.0013, all within 1.3x.
  Excluded-mass fractions printed per family (D-H 9-43 percent, BEUR
  21-43 percent of atoms), so the "admission-price selection" angle is
  quantified at the same time: equalizing what the gate/window admits
  removes the whole flip. Folded in as tracked check **U2c**.
- **Family-relative disks**: center $i t_1$, radius $0.45 t_1$
  (mid-gap-anchored, the scale-relative analogue of 2i/0.9): zeta-first
  SURVIVES but the margin shrinks 3.4x -> 1.6x. Center $t_1 + 2i$,
  radius 0.9 (beside each family's first zero): ordering becomes
  **D-H 0.0191 < BEUR 0.0324 < ZETA 0.0342**: zeta LAST. Any disk deep
  in a family's own gap flatters the family with the deepest gap; any
  disk beside actual spectral mass restores the e1t ordering.
- **Finer fake** (eps = 0.05 / 0.01, seed 149, the e1t protocol,
  builds cached in the scratchpad): BEUR's 2.2->2.6 mA gap scales
  0.0222 -> 0.0073 -> 0.0070 = D-H parity (0.0068). The BEUR-vs-D-H
  part of the deficit was matching coarseness; the residual vs zeta is
  the band geometry killed above.
- **Leave-one-out lambda** (the e1t eps-trajectory lesson): dropping
  any one of the four lambdas keeps zeta first (z/d margins 2.9x-3.5x);
  zeta-only drops vs full D-H likewise. This attack did NOT land: the
  flip was grid-stable geometry, not branch luck, which makes the
  geometry kill cleaner (nothing about it was noise).

Interpretation, typed: the mA face measures the depth of the central
gap relative to the evaluation disk = first-zero position = the same
FE/density-adjacent residual U3a named. The .md's "clean gated-vs-gated
zeta-vs-D-H comparison" was never gap-matched: D-H's zeros in
[4.9, 13.6) are inside its own FE budget (its gate correctly leaves
them), so gate parity did not imply geometry parity.

### Attack 2: U3c, the Suzuki-analogue Weyl tail-mass rate. LANDED (grid-floor artifact + gap geometry)

The builder's own named control (adversarial case 3): is zeta's
stability an artifact of u_half saturating at the UGRID floor
(0.025 = one step)? Ran a grid with step 2e-4 below u = 0.05:

- **u_half**: ZETA {0.0048, 0.0002, 0.0002, 0.0002} (the "constant
  0.025" was the grid floor; the true values COLLAPSE), D-H {0.036,
  0.0022, 0.0002, 0.0002}, BEUR {0.25, 0.18, 0.15} (genuine values,
  well above resolution).
- **Fine-grid sup-gaps**: ZETA {0.992, 0.114, 0.0}, D-H {0.845, 0.857,
  0.445} (NON-stabilizing), BEUR {0.282, 0.112}: the fake now has the
  SMALLEST first-pair gap. The coarse-grid "stabilization" was the
  step of a degenerate profile moving below the grid's resolution; the
  in-sample ordering inverts when the instrument can see.
- **Structural cause** (measured): the longest interval covers
  0.60-0.9999 of X for the gated families and starts at u as low as
  0.00012; all Weyl mass sits in the tiny head before it. The
  u-normalized profile of a gated build is a step at $u = 0^+$, i.e.
  the U1 germ-length blowup (the relocated type divergence) in another
  costume. BEUR's X stays 13-43 (no central gap), so its profile is a
  bona fide function that genuinely moves: the "separation" was gap
  geometry, again.
- **Band-equalization control**: excluding $|t| < 13.6$ for everyone,
  D-H {0.999, 0.005, 0.0} and BEUR {0.997, 0.016}: the fake reproduces
  zeta's degenerate pattern exactly. eps-control: the eps = 0.05/0.01
  fakes keep profile gaps 0.32/0.39 (eps-INsensitive): not coarseness.
- Folded in as tracked check **U3d**; U3c's check text re-scoped (the
  coarse numbers stand as pins; the stabilization reading is dead);
  the "information his gauge does not have in print" sentence removed.

### Attack 3: the 243x conditioning asymmetry (U4a). DID NOT LAND (refined, reading confirmed)

Swept the collided pair over adjacent pairs at ZETA 3.0/32 and D-H
3.0/32 (every 3rd pair + lowest + minimal-sep + highest), same removal
rule, same disks:

| base | pair location $t_{mid}$ | ratio dm_beside/dm_low |
|---|---|---|
| ZETA 3.0 | 17.6 (lowest) | **9.7x** (dm_low largest here, 1.3e-3) |
| ZETA 3.0 | 31.7 | **490x** |
| ZETA 3.0 | 40.97 (builder's minimal-sep pair) | **243x** |
| ZETA 3.0 | 48.9 / 54.7 | 114x / 59x |
| D-H 3.0 | 7.0 (lowest, beside the 2i disk) | **2.9x** |
| D-H 3.0 | 15.8 .. 54.0 | 159x .. 17x |

The asymmetry TRACKS the defect location (low defects are low-disk-
visible; the builder's check threshold `dm_high > 3 dm_low` would
itself fail for a defect at $t_{mid} = 7$, which is the localization
reading working, not failing). A location-independent 243x would have
falsified the reading; instead 243x is one point on a location curve.
Fix applied: the .md and check text now quote the asymmetry as
pair-specific (10x-490x), and the handed-forward item no longer uses
243x as a constant.

### Attack 4: clause-(b) indicator saturation. LANDED (as a sharpening)

- **Measured values** (npz): Face-A deltaK = ZETA {4.7e-5, 2.9e-7,
  1.7e-13, 9.2e-14}, D-H {4.8e-4 .. 1.8e-9}, BEUR {1.0e-2 .. 1.9e-3}.
  The U3a "agreement to < 0.05" is a linear-scale read of numbers that
  differ by 8-12 ORDERS, with ZETA the closest to the degenerate
  boundary. The log-scale "separation" is the central-gap length
  blowup (density data), so the density-typing verdict stands, but the
  honest wording is "all pinned near the boundary the gap geometry
  chose", now in the check text.
- **Genuine-escape control**: a family with half its spectral mass
  escaping to infinity (atoms $\pm 1, \pm T$, $T \to 320$; also a
  9-atom core + heavy escaping pair) leaves deltaK/dispersion FLAT
  (0.64/0.40 and 0.027/0.014 respectively); only min_len moves. The
  indicators are chain-geometry (indivisibility) reads, not escape
  detectors; `indicators()` docstring corrected. This confirms rather
  than contradicts U3b's own scoping ("the clause lives on H, not on
  the measure"), but the pre-fix docstring name ("no-mass-escape
  indicators") overpromised.
- **Non-saturated variant** (the builder's suggested head-window
  deltaK at $x = \min(5, 0.9X)$): separates weakly (BEUR 0.012 > D-H
  0.004 > ZETA 0.0015 at lam 2.2, converging along the grid); input =
  low-band mass near the footpoint = the central gap = density data.
  Typed and recorded; no discrimination beyond geometry here either.

### Attack 5: tail-gauge integrity. LANDED (one false claim; demotion consistent)

- **The false claim**: encoding item 6, the U6d comment/check, and
  VERIFIER target 4 all asserted the Weyl-mass profile is
  tail-invariant by construction ("the artificial tail carries zero
  Weyl H-mass, so the profile is a pure germ observable"). The
  zero-tail-mass fact is true (tail annihilation forces
  $u(X) \propto J e_\beta$), but the Weyl solution on the germ DEPENDS
  on the tail direction, so the normalized profile is tail-COVARIANT:
  measured max shifts 0.283 (Face A, TAIL-N vs TAIL-0; N = D
  structurally on Face A) and 0.216 (Face B). Fixed in all four places
  (.py docstring, U6d comment + check text + npz key
  `u6_prof_tailshift`, .md encoding item 6, VERIFIER target 4 restated
  as the correct pair: germ-data invariance + per-tail annihilation).
  U3d's fine-grid conclusions were re-checked under TAIL-0: same
  pattern (zeta {0.988, 0.117, 0.0}, D-H {0.83, 0.86, 0.45}), so no
  downstream verdict flips, but the claim as written was false.
- **The mB demotion**: consistently applied everywhere mB appears
  (Q2 table = data only; Q5 and U6d carry the demotion; the .py
  verdict print never leans on mB). No catch.

### Attack 6: mechanics. DID NOT LAND

(i) Module identity: U0a verifies the imported functions ARE e1t's
(module check) and e1u defines no shadowing builders; confirmed by
source grep. (ii) Round trips: npz worst 1.55e-49 as claimed; U1d
winding counts 4/8/13/24, 7/12/19/32, 7/11/19 reproduced in the sweep
harness. (iii) npz/quick discipline: full-mode npz byte-identical
across consecutive runs before AND after the fixes; quick saves
nothing (md5 unchanged, three checks). (iv) K1: guards trip correctly
(both raise RuntimeError and set the flag); COLD-cache `get_build`
(cache file removed, D-H 2.2/12 rebuilt from scratch with guards
armed, ambient dps 25 as `main()` sets): no trip, rebuild
BIT-IDENTICAL to the tracked cache (|deps| = 0.0, max|dxi| = 0.0),
original cache bytes restored after the test. At ambient dps 15 the
rebuild differs at 5e-4: the known e1n dps-branch caveat, re-observed,
not a leak; anyone rebuilding caches outside `main()` must set dps 25.
(v) D-H 3.7/36: window 86.02 > 85.699, winding wide = thin = 34,
M = 68 = 2x34, local counts 1/2/1, rt 2.5e-52. (vi) The K1-ALLOW
bare-substring scanner weakness documented in `_e1q_adversary.md`
applies here too; the runtime guard layer is the load-bearing one and
was verified; remains the standing cross-file cleanup item. (vii) Em
dashes: zero in .py/.md before and after all edits.

### Attack 7: narrative integrity. PARTIALLY LANDED

- **Pre-registered exits**: the exits were stated before results and
  not moved; the check SHAPES match the tasking; thresholds disclosed
  as pinned. The pre-round verdict line said the Q2 closing exit "does
  NOT fire: its first conjunct is false". Both conjuncts' measured
  values, post-round: conjunct 1 ("zeta shows NO improvement") was
  false only in the shared-compression + geometry sense (all families
  compress 30-500x; zeta's EXTRA cleanliness is the gap geometry killed
  by U2c); conjunct 2 ("(b) family-blind on every measured face") was
  false pre-round only through U3c, which is now dead. Post-adversary
  both conjuncts hold in the sense the pre-registration intended, so
  the exit FIRES and the rung closes as the THIRD reformulation. The
  .md verdict line and price-table net were rewritten accordingly
  (the pre-round "three zeta-first faces / new surface" reading is
  withdrawn; fneg_q is e1t's face carried over, not chain output).
- **Suzuki scoping**: correctly worded throughout (transverse cousin,
  cited for the clause shape, not as prior for the compactness trade);
  the one overreach ("information his gauge does not have in print",
  contingent on U3c being real) removed with U3c.
- **Price table**: no row asserted relocation without a measurement;
  the U3c-dependent cells were re-scoped and the pre-registered
  question now has an explicit answered row (below).

## (d) The price-level reformulation question (pre-registered), answered

Is a lambda-uniform U3c rate claim the #160 growth clause in disguise?
**YES at its discriminating margin; and the "actual reduction" branch
is refuted by measurement.** Decomposition, now in the price table:
the part of the profile behavior purchasable from density + gate
inputs alone (the u-collapse pattern and the family ordering) is
exactly the part measured to carry ZERO discrimination (U3d: fake
identical after band equalization; eps-insensitive). What a
discriminating rate claim would have to control, posed in the only
coordinate where it is not vacuous (unnormalized trace-length x, since
the u-coordinate is broken by the length blowup), is the Weyl
solution's mass distribution uniformly in lambda = uniform
Christoffel/orthonormal-polynomial growth control at the footpoint for
the window zero-counting measures = a lambda-uniform growth statement
about $\hat\xi_\lambda$: the #160 growth clause in Jacobi/Christoffel
coordinates. No cheaper fuel appears anywhere in the measurements; the
conservation law holds; the rung ends where e1m and e1t ended:
REFORMULATED, NOT REDUCED.

## (e) Fixes applied

All in place, marked `[ADVERSARY]`, in `e1u_canonical_chain.py` / `.md`:

1. **`.py`**: new check **U2c** (band-equalization control; the mA
   flip's tracked kill; npz keys u2c_ex136/ex200 per family). U2a
   check text re-scoped (numbers stand as pinned; flip is geometry).
2. **`.py`**: new check **U3d** (fine-grid + band-equalized profile
   control; the U3c kill; npz keys u3d_gapsF/gapsX per family). U3c
   check text re-scoped (coarse numbers are pins, reading dead).
3. **`.py`**: `weyl_tail_mass` and `indicators` docstrings corrected
   (germ-supported vs tail-invariant; degeneration vs escape); U6d
   comment/check text corrected + profile tail-shift measured in-run
   (npz key u6_prof_tailshift); U3a check text gains the saturation
   caveat; U4a gains the pair-sweep comment + check-text scope; U6c
   typing table updated; module docstring gains the ADVERSARY ROUND
   block; verdict print rewritten (NO-BEYOND-GEOMETRY + Q2 exit fires).
4. **`.md`**: header/status/artifacts (21/21 full, 18/18 quick);
   verdict-in-one-line replaced (NO-BEYOND-GEOMETRY, exit FIRES, rung
   closes as third reformulation); encoding item 6 tail claim
   corrected; U2a bullet rewritten with all four controls; deflation
   bullet (iv) extended (gated-vs-gated was never gap-matched); U3a
   sharpened (saturation + escape-blindness); U3c bullet rewritten
   (artifact + structure + controls); U4a sweep folded in; U6c/U6d
   updated; price table: two cells re-scoped + the answered
   pre-registered row added + net corrected; discipline outcomes
   (D-H and Beurling paragraphs) corrected (both new fake-failing
   reads withdrawn); honest limits 1-3, 5, 6 updated/resolved; handed
   forward 1 (closed), 2 (re-posed in unnormalized x), 3 (243x ->
   location-dependent); VERIFIER target 4 restated; adversarial test
   cases annotated with outcomes; ADVERSARY round summary appended.

Not fixed (recorded): the K1-ALLOW substring scanner weakness
(cross-file item, runtime layer verified); the dps-sensitivity of
`build_comb` outside `main()` (documented here, inherent to the
branch); whether fneg_q survives lambda beyond the grid (open, carried
from e1t, now the rung's only zeta-first face).

## (f) Post-fix re-verification

```
full:  21/21 passed, ~10.6 s warm; npz re-saved with the new keys and
       byte-reproducible across consecutive runs (md5 9e67caff...)
quick: 18/18 passed, ~2 s; saves nothing; npz md5 unchanged
em dashes: 0 across .py, .md, and this report (rg scan)
```

## Verdict: PASS_WITH_FIXES (mechanics and measurements) / FAIL (the two headline zeta-first faces, withdrawn)

The construction is real and exactly what it claims mechanically: the
embedding is exact, the compact-space entry is free, the conditioning
panel is the honest shape of the relocated type divergence, and the
entanglement quantification (U4) survives attack sharpened. What did
not survive is the round's narrative: the chain coordinate did NOT
produce a zeta-first face. Both claimed novel faces measured the
central spectral gap through different instruments, and both died
under controls the BUILDER itself pre-registered, which is the
discipline working as designed. The rung closes as the third
reformulation with its own exit's words; the compactness-trojan arc's
conservation law (D-H catches form dodges, Beurling catches counting
dodges, DMV pre-kills density mechanisms) has now killed the canonical-
chain costume's output faces too, and the surviving lead remains where
e1t left it: the gauge-conditional T1f admission price and the pin.
