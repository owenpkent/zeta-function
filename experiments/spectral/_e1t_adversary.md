# ADVERSARY report: e1t compactness trojan

> ADVERSARY attack on `experiments/spectral/e1t_compact_class_limit.py` /
> `.md` / `.npz`, 2026-07-22, same day as the BUILDER pass. Target: the
> compactness-trojan probe (can M4's uniform det-class limit be traded for
> compact-class certification + Carleman determinacy + the #160 Hamburger
> pin). Grading style follows [`_e1q_adversary.md`](_e1q_adversary.md) /
> [`_e1p_adversary.md`](_e1p_adversary.md) (PASS_WITH_FIXES format, attack
> axes, every catch banked). All attacks were RUN, not reasoned in the
> abstract; scratch scripts lived in the session scratchpad, outside the
> repo. Context consumed: e1k (build_float), e1m (#160, zero_grid_count,
> winding), e1n (#161, the T5 Abel-summation gate consumer), the Beurling
> and D-H disciplines.

## (a) One-paragraph verdict

The headline verdict `trojan_trades_M4_away = NO` **survives**: links (ii)
and (iii) hold all the content after every attack, the harness is clean
(bit-identity now verified EXACTLY at a real mixed-family config, not just
the toy point), K1 guards genuinely guard, the npz is byte-reproducible,
quick mode saves nothing, and the DMV screen fires as designed (confirmed
down to matching eps = 0.01). But three of the four Q-verdicts were stated
more broadly than what was measured, and the round's sharpest instrument
found the one thing the BUILDER's own handed-forward list predicted it
might: the FE-gated ghost-quotient gauge makes the ZETA measure face
near-positive AND tight family-wide (dressed builds 0.0002/0.0005 negative
mass, the CLEANEST of all builds), while D-H stays at 0.05-0.12 and the
fake at 0.24-0.39, so T1e's "no family-uniform positive-measure
certificate" was a raw-gauge statement presented as a face statement, and
the "all discrimination is input-typed at the pin" theme has one measured
output-level exception (now check T1f, with its caveats priced: in-sample
trend, gauge-forced tightness component, un-normalized mass collapse to
0.0017 on the deep-dressed branch). Second, the load-bearing Q3 "RH-blind"
claim is face-scoped, not absolute: the eps trajectory (max consecutive
gap 3.4e-4 vs 8.6e-3, a 25x zeta-first separation on the full
pre-registered grid, flipping 7x the other way if lam = 2.2 is dropped)
and the T1f gauge-positivity face order zeta above D-H, and the
gauged-measure Kolmogorov face is mixed; what survives is the correct,
narrower claim that the function/germ coherence faces (the ones link (ii)
actually needs) are D-H-cleanest and that NO face certifies zeta
coincidence. Third, the close-pair anecdote justifying the winding
instrument ("ZETA 3.0: 13 zeros vs 11 crossings") is false as an
observation: both the plain phi/16 grid and the e1m offset grid count 13
crossings (the pair 40.86/41.03 has separation 0.178 > the step 0.131),
and the strip count itself is dps-branch-dependent (18/13/12 at dps
15/25/35, all reality-certified, none hiding a complex pair in |Im| in
(0.02, 0.05]). Smaller catches: the T2b Euler gate has no downstream
positivity consumer in this probe (gate-stripped, the signed D-H comb
passes the lattice clause exactly and fails only the truncation-sensitive
convergence clause at 0.098 vs the pinned 0.05, so UNPOSABLE is honest as
input typing only, the genuine consumer being e1n T5); the #160
"EQUIVALENT" citation dropped e1m's own conditionality (restored); the
tau_lambda relocation wording contradicted T4a's family-blind type ratio
(content is in the rate control, not the scalar); and the lattice-clause
threshold provenance was off by 2x ("half the spacing at n = 50" for what
is the full spacing). On the BUILDER's side of the ledger: the eps
question resolved in the builder's favor (the fake's O(1) Weil
indefiniteness scales to -0.132/-0.025 at eps 0.05/0.01: matching
coarseness, not lattice structure, vindicating the exclusion from the
certification vector, with the bonus finding that the alternation ~0.31 at
eps = 0.01 is the quantity that does NOT scale, i.e. the lattice-sensitive
residue), and the T1d dichotomy survived its designated attack (the
sin-quotient fourth normalization is type-free and non-constant but has no
in-sample limit: it fails at link (ii), not link (i)). Verdict:
**PASS_WITH_FIXES**.

## (b) Reproduction

| run | expected | observed (before any ADVERSARY change) |
|---|---|---|
| full | 21/21, ~79 s cold / ~7 s warm | **21/21, 7.1-7.3 s warm** |
| npz reproduced | tracked npz regenerated identically | **196/196 keys, max abs diff 0.0, byte-identical md5** (`a814874d...`) |
| quick | 21/21, no npz | **21/21, 6.6-6.8 s, npz md5 unchanged** |
| T0a/T0b | max dQ = 0.0 claimed | **max dQ = 0.0e+00 both**, at the toy config (N = 4, lam = 1.8, dps 25) only |

Post-ADVERSARY: full **23/23** (~15 s warm; +T0d, +T1f), quick **22/22**
(T0d is full-only because it verifies the e1n cache mixing, which quick
does not exercise; no quick-only check exists). npz re-saved with the 44
new T1f gauge keys + t0_dxi_dh26; quick still saves nothing (md5-verified).

## (c) Attack axes

### Attack 1: harness bit-identity beyond the toy config. DID NOT LAND (claim strengthened)

The .md claimed bit-identity from a single N = 4, lam = 1.8 test while the
actual grid mixes e1n `build_float` caches with fresh `build_comb` builds
INSIDE the D-H family (2.6/sqrt13 cached vs 2.2/3.0 fresh), so a
builder-dependent difference would contaminate the D-H gap sequence that
carries the Q3 coherence claim. Rebuilt D-H 2.6/16 from scratch with
`build_comb` (7.9 s) and compared to the e1n cache: ground eps agrees to
**0.0e+00**, phase-aligned ground state to **max|dxi| = 0.0e+00**. Exact.
Folded in as full-mode check T0d (skips, with a printed reason, when no
e1n cache exists, because then no mixing happens).

### Attack 2: Q1, a fourth normalization (break T1d). DID NOT LAND (dichotomy sharpened)

The designated candidate inside the harness is the sin-quotient
T(z) = xihat(z)/sin(zL/2): by the structural split it carries ZERO
exponential type, is non-constant, object-computable, truth-free, and is
not in {a, b, c}. Measured its projective gaps on [1,10]+1.5i (ghost-
quotiented): zeta {0.46, 0.56, 0.54}, D-H {0.21, 0.18, 0.27}, BEUR
{0.70, 0.42}. No in-sample Cauchy trend for any family: the candidate
bounds the type WITHOUT collapsing to a constant but produces no certified
limit, so it dies at link (ii), not link (i). The pre-registered Q1
dichotomy survives in sharpened form: bounded type is purchasable
(rescale: constant limit; sin-quotient: no limit); a certified
non-constant limit is not. (Consistent with T3e: T'/T was already flat;
this closes the "maybe T itself is Cauchy even if its log-derivative is
not" loophole, which the BUILDER had not tested.)

### Attack 3: Q1/T1e, the gauge sweep. LANDED (the round's main find, now T1f)

Target: fneg < 0.05 on the DRESSED builds via a sign-fixed, invertible,
object-computable weighting. First, the posed criterion "any weighting
computable from the object alone" is ill-posed: the trivial sign gauge
w_n = sign(a_n) is object-computable and makes ANY measure positive
(demonstrated; criterion re-scoped in the .md). Second, the structured
sweep: exponential damps order D-H first (e^-|x| gives D-H 0.000 but zeta
dressed only 0.063/0.146) but the **FE-gated ghost-quotient gauge**
aq_n = a_n / q(phi n), built from the BUILDER's own normalization-(b)
machinery, gives:

| build | fneg_alt (raw) | fneg_q (quotient gauge) | r95 raw -> gauged | esc12 raw -> gauged |
|---|---|---|---|---|
| ZETA 2.2 (clean) | 0.026 | 0.026 | 12.0 -> 12.0 | 0.027 -> 0.027 |
| ZETA 2.6 (dressed) | 0.598 | **0.0002** | 29.6 -> 6.6 | 0.567 -> 0.002 |
| ZETA 3.0 (clean) | 0.028 | 0.028 | 11.4 -> 11.4 | 0.031 -> 0.031 |
| ZETA sqrt13 (dressed) | 0.283 | **0.0005** | 51.4 -> 7.3 | 0.999 -> 0.005 |
| D-H (all four) | 0.052-0.122 | 0.052-0.122 (no ghosts) | ~6-16 | <= 0.063 |
| BEUR (all three) | 0.24-0.39 | same (no ghosts) | 36-40 | 0.36-0.96 |

The dressed alternation is EXACTLY the ghost polynomial's sign pattern
(99.9+ percent of the negative mass vanishes under division), i.e. e1n's
dressing-migration finding measured on the measure face. Consequences:
(1) T1e was a raw-gauge statement, re-scoped; (2) the Helly positivity
clause revives for zeta, gauge-conditionally; (3) fneg_q is an
OUTPUT-level family separator (zeta cleanest at every grid point),
the one measured exception to "all discrimination is input-typed".
Caveats I priced before promoting it: the D-H sequence decreases along
the grid (in-sample separation, may close); the tightness gain is partly
gauge-forced (degree-2g polynomial damping); the un-normalized gauged
mass collapses on the deep-dressed branch (sum|aq| = {2.39, 1.38, 2.86,
0.0017}), so Helly without renormalization can converge to the zero
measure and the clean framing is Prokhorov on normalized measures; and
the normalized gauged-measure Kolmogorov gaps are family-MIXED (zeta
{0.257, 0.142, 0.256}, D-H {0.162, 0.214, 0.212}, BEUR {0.302, 0.171}),
so the gauge buys positivity, not coincidence: link (ii) stays open,
and the headline NO stands.

### Attack 4: Q3, the RH-blind claim (find ANY zeta-first surrogate). LANDED (scoping kill)

Systematic hunt over the computed data. D-H-first faces confirmed:
function-face projective gaps (also RAW, without the quotient: zeta
{1.34, 1.20, 1.13}, worse than quotiented), a2/a4 relative scatter
(D-H rel max-gap 0.12/0.35 vs zeta 1.65/3.02), m-proxy gaps, raw
mass-escape, r95/esc stability. Zeta-first faces found: **the eps
trajectory** (zeta {+3.1e-5, -3.1e-4, +3.2e-5, -3.8e-5}, max gap 3.4e-4;
D-H {+8.7e-3, +1.0e-4, +8.1e-5, +3.3e-5}, max gap 8.6e-3: zeta 25x more
coherent on the full pre-registered grid, FLIPPING to D-H 7x if lam = 2.2
is dropped, so it is margin data, honestly fragile) and **the T1f
gauge-positivity face** (zeta below D-H at all four cutoffs). Mixed face:
gauged-measure Kolmogorov. Also noted: zeta's supG1 has a smaller absolute
max-gap (0.209 vs 0.264) but that is a scale artifact (zeta's values are
all small; relative, D-H wins) and was not counted. Net: the absolutist
"NONE exists at finite lambda" phrasing (the .md's own kill condition for
the RH-blind wording) is dead by its own criterion; the face-scoped claim
survives and is now what both files say.

### Attack 5: Q2, the Euler gate (structural refusal or coded refusal?). LANDED (scoping)

Gate-stripped bypass: fed the signed D-H comb directly to the downstream
clauses. Result: lattice displacement exactly 0.0 (passes; D-H lives on
{log n}), convergence defect 0.098 vs the pinned 0.05 (fails, but this is
truncation-sensitive at n <= 79, not structural); the |comb| rearrangement
gives the same shape (conv 0.113, disp 0.0). So NOTHING downstream of the
gate consumes nonnegativity; the UNPOSABLE verdict is a type-level refusal
whose mathematical justification lives in e1n T5 (the Abel-summation
one-sided upgrade, where Lambda >= 0 is genuinely consumed), not in this
probe. This does not break Q2's verdict (the gate is honest as input
typing, and the .md said "by construction"), but "consumed as an explicit
hypothesis" overstated: CHECKED, not consumed. Scoped in both files.
Bonus consistency finding: the lattice-clause threshold's provenance
phrase ("half the spacing at n = 50") is arithmetically wrong: log 51 -
log 50 = 0.0198, half = 0.0099, and the code uses 0.02 = the FULL spacing.
Fixed in the .md.

### Attack 6: the close-pair diagnosis + dps branches. LANDED (anecdote falsified; certificate robust)

Reproduction at cached ZETA 3.0/32: winding at bands 0.4/0.05/0.02 all
give **13**; sign-change crossings at phi/16 give **13**, on both the
plain [0.6, Twin+0.4] grid and e1m's own offset `zero_grid_count` grid
(zeros at 14.05, 21.02, 24.95, 30.49, 32.99, 37.64, **40.86, 41.03**,
43.36, 48.01, 49.79, 53.01, 56.41). The claimed "11 crossings" does not
reproduce anywhere: the close pair's separation 0.178 exceeds the phi/16
step 0.131 and is resolved. Localized the pair by per-box winding
(box [40.85, 42.86] holds exactly 2 zeros). The .md's instrument
justification was therefore false as an observation (kept as an
in-principle preference). The untested dps branches, now tested: full
N = 32 rebuilds at dps 15 (13 s) and dps 35 (62 s) give **18** and **12**
strip zeros respectively (vs 13 at dps 25): the count itself is
dps-branch-dependent, e1n's branch caveat biting hard on this face. At
every branch, winding at 0.05 equals winding at 0.02 equals the crossing
count: reality-certified everywhere, and NO zero sits at |Im| in
(0.02, 0.05] on any branch. So T2a's certificate is robust across
branches; only the anecdote and the branch-independence of the count die.

### Attack 7: the Beurling eps question. DID NOT LAND (builder vindicated, with a bonus split)

Rebuilt the fake at lam 2.2 / N 12 with matching eps = 0.05 and 0.01
(same seed 149, same pipeline): ground eps = **-0.132** and **-0.025**
(from -0.879 at eps = 0.25): the Weil-form indefiniteness scales with
matching coarseness, so it is density data, exactly as the BUILDER
claimed when excluding it from the certification vector; both finer
fakes still certify REAL (strip = thin = 6), extending T2a's
family-blindness. The bonus: fneg_alt does NOT scale (0.309/0.313 at
eps 0.05/0.01 vs zeta's 0.026 at the same config), so the measure-face
alternation is the lattice-sensitive quantity at hair-trigger sensitivity
(a 1 percent log-displacement flips a third of the alternating mass).
Recorded in the .md as the answered honest-limit 4.

### Attack 8: K1 / discipline audit. DID NOT LAND

(i) Guard trip test: installed the guards exactly as `main()` does, then
called `mp.zetazero(1)` and `davenport_heilbronn.zeros(20)`: both raise
`RuntimeError` and set the tripped flag. (ii) Import-graph side channel:
e1k carries hard-coded landmark literals (ZETA_ZEROS/DH_ZEROS) at module
level, but e1t imports only builders/configs and never touches them; e1n/
e1m module levels are function/class definitions only; no `np.load` of any
zero cache exists in e1t's paths. (iii) Identical-code-path claim: T0a/
T0b/T0d now cover toy and real scale; D-H and BEUR flow through the same
`build_comb`/`XihatD`/`winding_count` instruments with family differences
only in the comb input and the FE-typed gates (`ghost_gate` returns
UNPOSABLE for BEUR by type, which is the documented design, and the two
gates that special-case labels do so on input-typed grounds stated in
their docstrings). (iv) Pre-registration consistency: the .md's
expectation table matches the outcomes; thresholds are disclosed as
pinned-not-pre-registered (they are regression pins, which is the honest
reading of all 21 original checks); the one self-fulfilling expectation
found is Q2's "D-H must be UNPOSABLE" (the gate is CODED to return that;
see Attack 5, scoped). (v) npz/quick discipline: byte-identical
regeneration, no clobber. (vi) Em dashes: zero in .py/.md before and
after all edits.

### Attack 9: the relocation table row audit. PARTIALLY LANDED (two wording fixes)

Row (i): "content moves into control of tau_lambda" contradicted T4a's own
finding that the type RATIO is part of the family-blind vector (diff
0.034): a family-blind scalar cannot carry identification content. What
the measurements support: the content is in the lambda-uniform control of
the collapse RATE (what the rescale discards), which is the #160 growth
clause. Fixed in both files. Row (iii): "by #160 the pin's open clause is
EQUIVALENT to the identification" dropped e1m's explicit conditionality
("conditionally EQUIVALENT... given the limit + growth package",
e1m_hamburger_pin.md rung table + banner). Restored in both files. Row
(ii) survives as written (all three cited measurements are real; the
RH-blind phrase inside it now reads face-scoped per Attack 4). Rows (i)
and (iii) otherwise carry measured content (T1a/T1b/T1d/T1e/T1f and
T2b/T2c/T2d respectively).

## (d) Fixes applied

All in place, marked `[ADVERSARY]`, in `e1t_compact_class_limit.py` / `.md`:

1. **`.py`**: new check **T0d** (bit-identity at the real mixed-family
   config D-H 2.6/16 against the e1n cache; full mode, skip-with-reason
   when no cache). (Attack 1)
2. **`.py`**: new check **T1f** + per-build gauge line + 44 new npz keys
   (fneg_q, r95q, escq, tvq per build): the FE-gated ghost-quotient gauge
   revival, with all caveats in the check text and comment. T1e's check
   name re-scoped to "RAW/ALTERNATING gauges only". Q1 verdict print
   re-scoped. (Attack 3)
3. **`.py`**: T2a's WHY comment corrected (close-pair anecdote replaced by
   the measured 13 = 13 + dps-branch table + in-principle justification).
   (Attack 6)
4. **`.py`**: `euler_gated_certificate` docstring gains the ADVERSARY note
   with the measured bypass numbers (no downstream positivity consumer;
   the consumer is e1n T5). (Attack 5)
5. **`.py`**: T4a check text now names the T1f exception and makes the
   exclusion choice explicit; T4c row (iii) and the main verdict print
   restore #160's conditionality; main verdict print carries the
   face-scoped blindness wording. (Attacks 4, 9)
6. **`.py`**: module docstring gains the ADVERSARY ROUND summary block.
7. **`.md`**: header/status/artifacts updated (23/23 full, 22/22 quick);
   one-line verdict carries the T1f exception; methods harness bullet
   scoped to toy config + T0d; T1e re-scoped + new T1f bullet with the
   full gauge table numbers, mass-collapse and Kolmogorov caveats; Q1/Q2/
   Q3 verdict lines re-scoped; T3b addendum (the surrogate-hunt outcome);
   T3e mass-escape gauge-artifact note; T4a exception note; relocation
   table rows (i)/(iii) fixed; T1c/T1d tau_lambda precision note; lattice
   threshold provenance corrected (full spacing, not half); D-H and
   Beurling discipline paragraphs scoped/extended with the eps = 0.05/0.01
   measurements; honest limits 4 and 7 marked ANSWERED; handed-forward 2,
   3, 5 updated (5 corrected); adversarial test cases annotated with
   outcomes; new "ADVERSARY round summary" section.

Not fixed (not unambiguous, recorded for the next rung): whether the T1f
separation persists at larger lambda (e1u question); the Forester-Remling
arXiv citation in the surveyor fold-in was not independently verifiable
from this offline session (flagged, not altered); the shared bare-substring
"K1-ALLOW" scanner weakness documented in `_e1q_adversary.md` applies to
this file's scanner too and remains a cross-file cleanup item (the runtime
guard, which is the load-bearing layer, was verified to trip).

## (e) Post-fix re-verification

```
full:  23/23 passed, ~15 s warm (T0d adds ~8 s); npz re-saved with the
       new keys; three consecutive runs stable
quick: 22/22 passed, ~7 s; npz md5-identical before/after (no clobber)
em dashes: 0 across .py, .md, and this report (rg scan)
```

## Verdict: PASS_WITH_FIXES

The trojan probe's headline (`trojan_trades_M4_away = NO`, all three links
measured, content relocating to the gauge / the uniformity joint / the
pin) survives every attack, and two designated attacks strengthened it
(bit-identity exact at scale; the eps exclusion vindicated down to
eps = 0.01). The fixes are scope corrections, one falsified anecdote, and
one genuine new instrument: the FE-gated quotient gauge (T1f), which
converts the BUILDER's "no positive gauge exists" into the sharper and
more useful "the dressed alternation is exactly ghost dressing; positivity
is gauge-relative and, in the FE-gated gauge, family-separating in-sample":
simultaneously the round's biggest catch against the .md's wording and the
most promising lead it hands to e1u (pose the trace-normed chain on the
QUOTIENTED, near-positive measure face, and ask whether the zeta/D-H
separation persists or closes with lambda).
