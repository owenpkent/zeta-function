# ADVERSARY report: e1ad (sum rules on the prime log-lattice)

**Date**: 2026-08-25. **Scope**: external adversary round clearing the posed-but-unrun debt on this rung (LEARNINGS #201 portfolio item 5), run as a second party on the host that produced the tracked npz. Covers adversarial test cases 1, 2, 4, 5, 6 of [`e1ad_sum_rules.md`](e1ad_sum_rules.md) plus e1v's open case 7 (the replication item [`_e1v_adversary.md`](_e1v_adversary.md) left open). **Case 3 (super-resolution vs the horizon's completeness) is EXCLUDED here: it is being executed separately as a build (`e1ae_prony_horizon`, in flight in this tree).** Executable probe: [`_e1ad_adversary.py`](_e1ad_adversary.py) (`.venv/bin/python -m experiments.spectral._e1ad_adversary`; 294.7 s end to end, dominated by the 249 s full e1ad re-run of case 6d; every case is seeded and deterministic and reproduced identically across two runs of the probe), which consumes e1ad by import and adds attack harnesses only; nothing tracked is written or modified (planted-source copies and the redirected full-run npz live in a tempfile dir; tracked npz md5-verified untouched after every subprocess).

**Verdict: cases 1 and 2 MISSED (with quantifications that sharpen the record); case 4 LANDED (the BEUR scale-mixture mechanism fails in its monotone form; the typing of the BEUR-TRUE separation is reopened as a mechanism, the kill itself untouched); case 5 LANDED (the horizon mechanism is NOT gauge-rational: t-space collisions survive the irrational wrap, the rank law holds there exactly, and honest limit 3's commensurability claim is refuted while the theorem is strengthened); case 6 and e1v case 7 replications ran clean. Two wording-level corrections and one mechanism downgrade are required in e1ad_sum_rules.md / LEARNINGS #188; no measured table and no verdict-line claim of the rung is overturned.**

## Case 1 (the kill surrogate): GPERM on coarse-D snapped configurations. MISSED, with a scope correction

The R2 kill rests on GPERM being lattice-destroying. But GPERM permutes the wrapped gap multiset blockwise, and zero gaps (exact angular collisions, i.e. realized $\mathbb{Q}$-dependences) are elements of that multiset: collision-level structure survives any gap permutation by construction. The attack applies GPERM to the unmerged coarse-$D$ snapped multiset at $N = 300$ ($M = 78$) and quantifies retention vs destruction as a function of $D$ (3 shuffle seeds per rung; duplicate-vs-merged representation control agrees to $\le 1.9\times 10^{-14}$).

| $D$ | $M_d$ | collisions (= zero gaps) | SNAP $n_{\rm term}$ (theory $M_d-1$) | GPERM(SNAP) distinct sites | GPERM(SNAP) $n_{\rm term}$, 3 seeds | $\max_n\|S^{\rm GPERM}-S^{\rm SNAP}\|$ | $\max_n\|S^{\rm SNAP}-S^{\rm TRUE}\|$ |
|---|---|---|---|---|---|---|---|
| 40 | 39 | 39 | **38** | 39 / 39 / 39 | **38 / 38 / 38** | 0.08-0.12 | 0.35 |
| 100 | 60 | 18 | **59** | 60 / 60 / 60 | **59 / 59 / 59** | 1.7-3.6 | 6.1 |
| 400 | 74 | 4 | **73** | 74 / 74 / 74 | **73 / 73 / 73** | 7.0-10.2 | 7.6 |

**Retention is total and exact**: at every $D$ and every seed the distinct-site count and the termination index are invariant under the shuffle, so GPERM carries the entire rank-collapse signature (the one register the rung itself proves is arithmetic-sensitive, R4). At $D = 40$ the profile never even departs 0.5 nats before dying (max 0.35), so detection is carried entirely by the early termination ($n^* = n_{\rm term} = 38$ under e1ad's own S6 fallback convention), identically for SNAP and for every shuffle of it. What GPERM destroys is the ordering above the gap scale: the profile drifts from SNAP's by up to 10 nats at $D = 400$ while the detection indices stay in the same range ($n^* = 45$-$55$ vs SNAP's 53 at $D = 100$).

**Why this does not undermine R2**: the kill ran on the main grid, where the collision channel is empty by the rung's own S3c certificate (min wrapped gap $> 3\times10^{-6}$; measured at $N = 300$: TRUE $1.03\times10^{-5}$, BEUR $2.8\times10^{-5}$, RAND seeds $3.1$-$6.8\times10^{-5}$). On collision-free data GPERM is exactly the lattice-destroyed twin the kill needs, and the typing verdict stands. What does not survive is the dossier's phrasing: R2's "destroys every arithmetic correlation" (and the class table's "no arithmetic") is true only above the local gap scale; at and below the collision scale GPERM retains arithmetic exactly. The tight-pair tail is part of the same picture: TRUE's minimum wrapped gap is 3-6.6x tighter than every surrogate's at $N = 300$, and GPERM retains that datum by design; that is consistent with (indeed it is) R2's own conclusion that the whole spread lives in the gap multiset. **Correction required: scope the sentence, not the verdict.**

## Case 2 (the pinned 4x band): SNAP against a 12-seed jitter ensemble. MISSED, and S5a comes out stronger

S5a's 4.0x factor was pinned post hoc against a 3-seed jitter band. The attack widens the ensemble to 12 seeds (41-52, containing the original 41-43) at $N = 300$ and $N = 1000$ and reads SNAP's whole-profile response as an empirical percentile of the jitter distribution rather than against a small-sample envelope.

| $N$ | SNAP $\max_n\|dS\|$ | jitter min / median / max (12 seeds) | seeds $\ge$ SNAP | SNAP / ensemble max |
|---|---|---|---|---|
| 300 | 3.82e-2 | 2.04e-3 / 1.69e-2 / 9.39e-2 | **3 / 12** | 0.41 |
| 1000 | 1.99e-2 | 2.05e-3 / 2.09e-2 / 5.45e-2 | **7 / 12** | 0.37 |

SNAP sits at the 75th percentile at $N = 300$ and at the median at $N = 1000$: **not an outlier in either case**. The R3 ratios that motivated this attack (2.5x / 3.1x of the band top) were small-sample artifacts of a heavy-tailed statistic: the 12-seed maximum is 2.4-2.7x larger than the 3-seed top, and the pinned 4x envelope is loose but conservative. The generic-perturbation reading of S5a survives the widened ensemble outright.

One observation for the record: on the (heavy-tailed) diagonal-rate displacement SNAP sits BELOW all 12 jitter seeds at both sizes ($1.08\times10^{-6}$ vs $[2.61\times10^{-6}, 1.94\times10^{-5}]$ at $N=300$; $4.44\times10^{-8}$ vs $[7.62\times10^{-7}, 1.04\times10^{-5}]$ at $N=1000$), i.e. a low-side anomaly (snapping is if anything anomalously gentle on the diagonal). At $p \sim 1/13$ per size, sizes sharing the same underlying lattice, this is not significant at this ensemble size; a plausible mechanism (snap displacements of prime powers of one prime are deterministically correlated, $\mathrm{frac}(kDt)$ vs iid jitter) is logged as a cheap follow-up, not a claim. The mid-rate displacement percentile is unremarkable (5/12 and 4/12).

## Case 4 (the BEUR reading): the epsilon ladder. LANDED

R2 proposes the mechanism "BEUR is Poisson below its scrambling scale $\varepsilon$ and number-rigid above; smaller $\varepsilon$ = closer to TRUE at more scales", offered as "visibly why" the diagonal converges at $N = 3000$ while the mid rate stays Poisson; Handed forward 3 asked for exactly this ladder as a confirm-or-kill. Ladder: $\varepsilon \in \{0.05, 0.25, 0.5\}$, seeds 149/150/151 at $N = 300$, seed 149 at $N = 1000$ (anchor: $\varepsilon = 0.25$/seed 149 reproduces `e1ad.beurling_t` exactly, and its rates reproduce the dossier's R1 row to all printed digits). Distances are to TRUE, medians over seeds:

| $N$ | observable | $\varepsilon = 0.05$ | $\varepsilon = 0.25$ | $\varepsilon = 0.5$ | monotone? |
|---|---|---|---|---|---|
| 300 | $\|d_{\rm diag}\|$ | 0.017 | 0.250 | 0.093 | **NO** |
| 300 | $\|d_{\rm mid}\|$ | 0.0086 | 0.0103 | 0.0076 | **NO** |
| 1000 | $\|d_{\rm diag}\|$ | 0.024 | 0.171 | 0.220 | yes |
| 1000 | $\|d_{\rm mid}\|$ | 0.0042 | 0.0116 | 0.0039 | **NO** |

The $0.05 \to 0.25$ leg confirms the predicted direction on both observables at both sizes. The $0.25 \to 0.5$ leg REVERSES it: at $\varepsilon = 0.5$ BEUR's mid rate comes back toward TRUE at both sizes (0.0076/0.0039 vs 0.0103/0.0116 at 0.25) and the diagonal comes back at $N = 300$. Honest confound, stated: count equalization degrades at $\varepsilon = 0.5$ (deviation up to 15.4%, well above the rung's own 6% S3a pin), because the $e^{\varepsilon}$-extended generator bound makes the in-band count noisy. But the count-clean seed carries the same reversal: seed 150 at $N = 300$ has count deviation 2.6% and still gives $|d_{\rm mid}| = 0.0075 < 0.0102$ and $|d_{\rm diag}| = 0.094 < 0.293$ vs its own $\varepsilon = 0.25$ values. So the failure is not the confound.

**Outcome**: the monotone scale-mixture mechanism is refuted; "smaller $\varepsilon$ = closer to TRUE at more scales" is false past $\varepsilon = 0.25$, plausibly because a Beurling system at any $\varepsilon$ retains the arithmetic-progression rigidity of its own generators ($\{k \log b\}$ per generator), which is not a monotone function of the scrambling scale. What this reopens is the MECHANISM typing of the BEUR-TRUE separation (R2's "visibly why" clause and Handed forward 3: the answer is kill, not confirm). What it does NOT reopen: the kill itself (GPERM-based, mechanism-free) and the Level 2-3 reading; BEUR's separation still collapses under lattice destruction at every size (R2's measured lattice-free fractions are untouched).

## Case 5 (the gauge scope): the D-ladder at L = golden mean. LANDED

Honest limit 3 claims "exact collisions require the snap lattice to be commensurate with the wrap ($DL$ integer here); at irrational $L$ the snapped orbit is dense and never collides exactly", and the posed case predicts blindness at ALL $D$. The attack runs the ladder at $L = \varphi^{-1}$ with the snap done correctly for an irrational wrap: $t \mapsto m/D$ with UNREDUCED $m = \mathrm{nint}(Dk\log p)$ (the mod-$D$ reduction is a no-op on the measure only when $DL$ is an integer). A matched-amplitude jitter control ($\pm\tfrac{1}{2D}$ in $t$-space) runs at every rung to separate lattice-specific detection from generic large-amplitude response. $N = 300$, $M = 78$:

| $D$ | $t$-collisions (vs L=1 total incl. folding) | $M_d$ | $n_{\rm term}$ (rank theory $M_d-1$) | $n^*$ | $\max\|dS\|$ | jitter control $n_{\rm term}$ / $n^*$ / $\max\|dS\|$ |
|---|---|---|---|---|---|---|
| 40 | **11** (39) | 67 | **66** | 55 | 6.4 | 77 / 41 / 4.6 |
| 100 | **2** (18) | 76 | **75** | 60 | 4.4 | 77 / 60 / 6.2 |
| 400 | 0 (4) | 78 | 77 (generic) | 69 | 3.4 | 77 / 67 / 17.3 |
| 2000 | 0 (1) | 78 | 77 (generic) | 64 | 3.3 | 77 / 73 / 2.5 |

**The prediction is refuted at the letter: collision rungs EXIST at irrational $L$.** Collisions have two channels the dossier conflated: (i) $t$-space rounding collisions (two prime powers with the same $\mathrm{nint}(Dk\log p)$), which are wrap-INDEPENDENT (11 of the 39 at $D = 40$; 2 of 18 at $D = 100$), and (ii) the mod-$D$ folding channel, which alone requires $DL$ commensurate (the other 28 and 16). On every collision rung at golden the rank law holds EXACTLY ($n_{\rm term} = M_d - 1$ with early termination = detection): the horizon mechanism is gauge-independent through channel (i), which STRENGTHENS the rung's central theorem beyond its claimed scope. The no-collision rungs never terminate early, and their 3.3-3.4 nat profile departures are amplitude-generic (the jitter control departs comparably or worse, 17.3 at $D = 400$): no lattice-specific detection, so no three-gap mechanism surfaced at this scale, and no new detection mechanism exists in this window beyond rank collapse. Pricing note: at irrational $L$ the birthday count runs against the unreduced site count $\sim D\cdot(t_{\max}-t_{\min})$ rather than $DL$; commensurate wraps LOWER the horizon by folding sites together. **Correction required to honest limit 3 and the #188(v) scope sentence; the theorem itself comes out stronger.**

## Case 6 (second-party replication of e1ad): CLEAN

Same host that produced the tracked npz (commit 17f00bc, 2026-08-20), so this is second-party fresh-process replication, not cross-machine replication (which remains open, as it was for e1v).

- **(a) Determinism**: two identical `szego_profile` runs on TRUE ($N=300$, dps 71) and on the RAND0 config agree mpf-EXACTLY at every index, and their 60-digit serializations byte-match (md5-equal).
- **(b) Source-scan teeth**: the tracked source scans clean; planted copies (under a tempfile dir, tracked file untouched) with `mp.zetazero(1)`, a `davenport_heilbronn` import, and a `.zeros(` call are each caught by `scan_lines`. The `SCAN-ALLOW` bypass exists by design (a planted call carrying the token evades); acceptable for a self-scan, noted for the record.
- **(c) Quick mode**: 21/21 passed, rc 0, and the tracked npz md5 is unchanged after the run (quick saves nothing, as documented).
- **(d) Full re-run**: `main()` re-executed with `OUT` redirected to scratch: **21/21 passed (249 s)**, and the freshly produced npz agrees with the tracked one on the identical 90-key set with **all 90 arrays EXACTLY equal** (profiles, $\ell^2$ partials, rate/kill/q-axis/horizon/gauge/audit tables, object arrays and the prereg-resolution string included; equality is array-level, the right register since the zip container embeds timestamps). The dossier's determinism and npz-stability claims replicate without remainder on this host.

**MISSED** (replication is the attack; it found nothing).

## Case 7 (e1v, the open replication item): CLEAN

[`_e1v_adversary.md`](_e1v_adversary.md) left case 7 open: "independent re-verification of K1 guards, the planted-call scan, npz byte-reproducibility and quick/full parity". Run here as a second party:

- `e1v --quick`: **24/24 passed**, rc 0, in 37 s on a COLD e1t build cache (this host had no `_cache/`; the quick grid built its four configs into the gitignored cache in-run; warm re-run 0.6 s, consistent with the dossier's ~0.3 s claim). The tracked `e1v_christoffel_gauge.npz` md5 is unchanged (quick saves nothing, as documented).
- The V6b (guards installed, never tripped) and V6c (source scan) checks are present and PASS in the quick output.
- Independent scanner (e1v's token list reimplemented in the probe, not imported): the tracked e1v source is clean off the `K1-ALLOW`/`K1-SCANNER` lines; a planted `mp.zetazero(3)` in a scratch copy is caught (line 1307, both matching tokens reported).
- The guard-install pattern itself trips: assigning the `_forbid` raiser to `mp.zetazero` and calling it raises `RuntimeError` before any zero is computed (restored immediately; K1-clean).

**Separate finding, for the record (documentation, not correctness)**: [`e1v_christoffel_gauge.md`](e1v_christoffel_gauge.md)'s status line reads "26/26 self-tests full, extended and quick". The module has 26 `check(` sites, but quick mode executes 24 of them (24/24 passed here); two checks are full-mode-gated. Every executed check passes, so nothing substantive is wrong; the quick count in the md is off by two. Flagged for Owen rather than edited (adversary-verified artifact; the `_e1v_adversary.md` F-section precedent).

**NOT replicated, stated honestly**: e1v full-mode npz byte-reproducibility and quick/full parity beyond the quick side (the full grid on a cold cache costs ~5.5 min of builds and was not mandated; the tracked e1v npz was left untouched), and cross-machine replication for either rung. e1v case 7 closes for this host at the quick/guards/teeth level.

## Net, and what must be corrected

Five posed attacks and one replication item were run. Cases 1 and 2 did not land and each sharpened the record (case 1 measured exactly what the kill surrogate retains; case 2 showed the pinned band was conservative and SNAP is mid-distribution). Cases 4 and 5 landed, both at the interpretive layer: no measured table, no self-test, and no verdict-line claim of e1ad breaks. Replications (6, 7) were clean, closing e1v's open case 7 for this host.

Corrections required in [`e1ad_sum_rules.md`](e1ad_sum_rules.md):

1. **Honest limit 3** (case 5): replace the claim that exact collisions require $DL$ commensurate. Correct statement: the snap has two collision channels; $t$-space rounding collisions are wrap-independent and the rank law $n_{\rm term} = M_d - 1$ holds at irrational $L$ exactly (measured at golden, $D = 40/100$); only the mod-$D$ folding channel needs commensurability; blindness at irrational $L$ holds only at $D$ large enough that the $t$-snap is injective, with the birthday price read against $\sim D\cdot(t\text{-range})$ sites instead of $DL$. The gauge face's scope shrinks; the theorem's scope grows.
2. **R2's GPERM phrasing** (case 1): "destroys every arithmetic correlation" needs the scale scope "above the local gap scale; collision-level structure (zero and near-zero gaps) is retained exactly". The kill's verdict is unaffected because the main grid is collision-free by S3c.
3. **R2's mechanism clause and Handed forward 3** (case 4): downgrade "its $\pm0.25$ generator perturbation makes it Poisson below scale 0.25 and number-rigid above, which is visibly why..." from an explanation to a refuted candidate: the $\varepsilon$-ladder shows the distance to TRUE is not monotone in $\varepsilon$ (reversal at $\varepsilon = 0.5$ on $r_{\rm mid}$ at both sizes, count-clean seed included). Handed forward 3 is EXECUTED with answer "kill".

Corrections required in LEARNINGS **#188**: in (v), the "the horizon mechanism is gauge-rational (exact collisions need $DL$ commensurate...)" sentence, per item 1 (and (iv) may note the gauge-independence strengthening); in (ii), the "visibly why its diagonal rate converges" clause, per item 3. The rung's headline (blind below the collision horizon, $\sqrt{2DL}$ price at commensurate wrap, rank-collapse mechanism) survives all six attacks and is strictly stronger after case 5.

Open after this round: case 3 (the horizon-optimality attack, running separately as `e1ae_prony_horizon`); the $N = 3000$ widened-ensemble and $\varepsilon$-ladder points (cost); cross-machine replication of both rungs; the case-2 diagonal low-side observation (cheap seed sweep if anyone cares).
