# E2AU: the turnaround hunt: certified NO TURNAROUND through a = 4, recorded through a = 5

**Date**: 2026-08-20/21 (overnight runs). **Status**: BUILDER round, executed twice (T = 600 exploratory, T = 1500 certified; 3225 s final run; the recorded 3/4 check suite includes the designed scope-catch at a = 5, see section 2). **Code**: [`e2au_turnaround_ladder.py`](e2au_turnaround_ladder.py). **Data**: `e2au_turnaround_ladder.npz` (tracked; incremental); zero caches `zeros_dps110_T600.json` (341) and `zeros_dps110_T1500.json` (1069), regenerable. **Executes**: B2c-deep2 with the #187 mission (locate the turnaround window $a^*$ implied by composing our certified narrowing with CCM's proven kernel limit, or show the proximity must fail).

## 0. The verdict

**There is no turnaround in the accessible range.** Across $a = 2.5, 3.0, 3.5, 4.0, 4.5, 5.0$ (dps-110 solves, per-rung convergence gates, J up to 274):

| a | gate | mixing (T = 1500) | r(z=2) | r(z=4) | r(z=6) | scope |
|---|------|-------------------|--------|--------|--------|-------|
| 2.5 | 0.040 conv | 2e-11 | +0.725 | +0.256 | +0.030 | CERTIFIED |
| 3.0 | 0.019 conv | 6e-09 | +0.583 | +0.093 | -0.001 | CERTIFIED |
| 3.5 | 0.020 conv | 9e-07 | +0.438 | +0.021 | 0.000 | CERTIFIED |
| 4.0 | 0.006 conv | 4e-05 | +0.325 | +0.003 | 0.000 | CERTIFIED |
| 4.5 | 0.134 NOT conv | 4e-03 | +0.240 | 0.000 | 0.000 | recorded (basis gate) |
| 5.0 | 0.029 conv | ~1 | +0.075 | 0.000 | 0.000 | recorded (mixing) |

The (1.2) object's Fourier transform collapses monotonically toward a spike at the origin: $r(z{=}6)$ pinned at zero from $a = 3$; $r(z{=}4)$ dead by $a = 4$; $r(z{=}2)$ down to $0.075$ by $a = 5$. Margins fall smoothly ($10^{-48.7}$ to $10^{-60.3}$) with healthy gaps throughout.

## 1. The certification story (three cross-validations in one run)

- **The tail arithmetic predicted its own cure, twice.** The a = 2.5 mixing certificate failed at $T = 350$ (9.0), cleaned at $T = 600$ (9e-5), and the whole ladder cleaned through $a = 4$ at $T = 1500$ (2e-11 to 4e-5), exactly as the sinc-tail scaling said it would. The a = 5 rung still fails mixing (~1) and stays recorded; one more depth doubling would certify it.
- **The ratios are bit-stable across zero depths**: the T = 600 and T = 1500 runs agree to every printed digit on every rung: a third cross-depth reproduction (after #185's a = 2.5 anchor and e2as's a = 1 protocol check).
- **The remaining scope holes are typed**: a = 4.5 fails the BASIS gate (0.134: resolution, not certificates: its values sit on the trend and are recorded); a = 5.0 fails mixing only. The recorded 3/4 in the final log is the aggregate certificate check catching a = 5 by design; the claimed set is the four certified rungs.

## 2. What this means for (1.2), worded with maximal care

The certified data now says: the unconstrained localized Weil-form ground state: which #187 settled at source as the object of Suzuki's conjecture (1.2): passes through the xi shape near $a = 1$ (#184) and then collapses monotonically away from it, certified through $a = 4$ ($\lambda = e^4 \approx 55$) and recorded through $a = 5$ ($\lambda \approx 148$), with no sign of the return that (1.2) requires. Since CCM's Lemma 7.3 PROVES their kernel $\hat k_\lambda \to \Xi$ interior-uniformly, the two facts can only coexist if the kernel-groundstate proximity CCM observed at $\lambda \le 6$ fails at larger $\lambda$: or if the conjectured limit needs restating (no normalization $c_a$ rescues pointwise convergence once fixed-$z$ ratios sit at zero across 2.5 decades of window growth). The decisive instrument is therefore **B2c-prox**: build $k_\lambda$ ourselves and measure the proximity directly; whichever side gives way is the fact the corpus needs. Until then this dossier claims exactly: certified no-turnaround through $a = 4$ for the unconstrained bottom, and nothing about the kernel.

## 3. Infrastructure notes

The parallel algorithms round (LEARNINGS #188) landed two tools this ladder's successors should adopt: `experiments/_shared/zero_polish.py` (bulk Newton polishing: the T = 600 cache reproduced 7x faster; makes the next depth doubling cheap) and `experiments/_shared/certified_eig.py` (Rump-certified pencil eigenpairs with a precision-starvation detector: the #184/#185 dps-failure class made self-announcing; B2c-prox should run on it).

## 4. Hand-off

(i) **B2c-prox** (HIGH, the decisive test: spec in the backlog); (ii) optional: one depth doubling ($T \sim 3000$ via zero_polish) to certify $a = 4.5$-$5$; (iii) P12 Section 6 now has its content: draft after the law-novelty pass; the note's headline is the certified collapse plus the proximity dichotomy.

## 5. Addendum 2026-09-01: the depth doubling executed, a = 5.0 CERTIFIED (hand-off (ii) discharged)

Driver [`e2au_depth3000.py`](e2au_depth3000.py) (thin by construction: imports this
instrument unmodified and retargets only T2 = 3000 / DPS2 = 110; zero supply from
`zero_polish` exactly as Section 3 prescribed, 2469 zeros to T = 3000 at 110 digits,
count-checked against `mp.nzeros(3000)`); overnight run 2026-08-31, **6/6 checks passed**,
8982 s; tracked archive [`e2au_depth3000.npz`](e2au_depth3000.npz), log in `_cache/`.

| rung | J (base/ref) | lg lam0 | gap | mixing | basis gate | verdict |
|---|---|---|---|---|---|---|
| a = 4.0 (control) | 106/218 | -55.17 | 6433 | 4e-12 | 0.0062 | CERTIFIED (as at T = 1500) |
| a = 4.5 | 120/246 | -56.79 | 3192 | 4e-10 | 0.1341 | recorded (basis gate, unchanged) |
| a = 5.0 | 134/274 | -60.29 | 51270 | 9e-08 | 0.0294 | **CERTIFIED (new)** |

Three facts land:

1. **The overlap control is bit-stable.** Every rung's refined ratios agree with the stored
   T = 1500 values to max |dr| <= 2.78e-16: the T-doubling changes NOTHING in the readout,
   only in the certificates, exactly the #185/#189 bit-stability pattern one deeper.
2. **The #189 tail-arithmetic prediction FIRED.** The a = 5.0 mixing certificate went from
   ~1 (uncertifiable) at T = 1500 to 9e-08 at T = 3000: one depth doubling cured it, as the
   dossier's tail estimate predicted. The certified no-turnaround ladder now runs through
   a = 5.0 (r(z=2): +0.3254 -> +0.2405 -> +0.0752, monotone collapse, no turnaround).
3. **a = 4.5's failure is typed, not cured: it is basis starvation, not tail mixing.** Its
   mixing improved 4e-03 -> 4e-10 with depth while the basis gate sat at 0.134 in both runs:
   depth buys tail control, only more knots buy basis convergence. The rung stays recorded
   with its ratios (bit-stable, collapse-consistent); certifying it is a knot-count question
   (J beyond 120/246), not a zero-data question.

P12 impact: the paper's certified range extends from a = 4 to a = 5 with the a = 4.5 gap
typed; the horizon-verdict wording ("recorded to 5") can now say "certified to 5, with the
a = 4.5 interior point basis-limited". Hand-off (ii) above is discharged.
