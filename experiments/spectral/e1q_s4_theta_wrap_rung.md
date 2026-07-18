# E1Q: the theta/Poisson wrap-collapse rung (form-side S4 probe, post-corridor pivot)

> Companion to `e1q_s4_theta_wrap_rung.py` / `.npz`. Executes
> [`theta_s4_build_spec.md`](../../docs/03_research/theta_s4_build_spec.md)
> in full: the form-side half of the post-corridor pivot named by
> [`ccm_corridor_frame_audit.md`](../../docs/03_research/ccm_corridor_frame_audit.md)
> Sections 4-5 (e1m's Poisson/theta engine, generalized to period L(lambda)
> and tested for a genuine rank collapse at the log-prime comb with e1o's
> own rank/cost-ratio instrument). Reuses e1m's theta/Poisson identities and
> `consume()`/K1-guard conventions, and e1o's rank-threshold + conditioning-
> pair discipline, verbatim in spirit; no operator is rebuilt, no CCM Sonin
> object is reused. It proves nothing about RH. All numbers from the
> default full run (25/25 self-tests post-ADVERSARY, ~1.6 s; `--quick`
> reduced grids, 23/23, ~0.0 s). ADVERSARY round 2026-07-17: verdict
> **PASS_WITH_FIXES**, full report [`_e1q_adversary.md`](_e1q_adversary.md).
> The BUILDER pass's original numbers were 16/16 full (~0.1 s) / 14/14
> quick; every added check and every second is new ADVERSARY territory (a
> lambda extension to M ~ 100+, a twin-fairness conditioning check, a
> mirage-shape audit, two periodization-invariant guards), not a
> correction to any BUILDER-computed number, all of which reproduced
> exactly on re-verification.

> **STATUS BANNER (read before quoting any number).** Predicted-wall outcome
> **CONFIRMED, tier 3 (MIRAGE), as pre-registered, and HARDENED by the
> ADVERSARY round's lambda extension (below).** Phase 0 (the anchor)
> PASSES cleanly: the period-L dual/Poisson identity re-verifies to relative
> defect ~1e-36 at every tested lambda, the same class e1m measured at
> L=1 ([ADVERSARY: this figure is the dps=35 working-precision floor, not a
> ceiling on the identity's true accuracy, which the Nwrap=Kwrap=80
> truncation alone bounds far tighter, ~1e-8952; see Phase 0 below]).
> Phase 1 (the collapse test) finds Delta_rho = 0.000 at 33 of 36
> tested (lambda, t) cells; the remaining 3 cells (the two largest lambda,
> at the top of the t-sweep) show a raw Delta_rho up to 0.182, but every one
> of them **fails the conditioning gate outright** (sig_r ~ 1e-6 to 1e-8,
> three to six orders of magnitude below the required 1e-3). [ADVERSARY,
> corrected: a ratio audit at all three flagged cells (not just the one
> shown below) finds a disproportionate step exactly at the declared-rank
> boundary in all three, not "smooth monotone decay, no clean gap" as
> originally stated -- but the step is between two already-negligible
> values, so it is the absolute scale of sig_r, not the local shape, that
> is and always was the correct rejection criterion; see Phase 1 below.]
> This is the same conditioning mirage e1o's own
> adversary round already caught once in a near-commensurate decimation
> family, reproduced here in a structurally different (genuinely
> lattice-consuming) construction, and now shown to HARDEN, not weaken, at
> M ~ 100+: **[ADVERSARY, lambda extension] the identical Phase 1 battery
> re-run at lambda in {10, 14, 20, 30} (M = 25, 44, 78, 154, an order of
> magnitude past the original grid's M=11 ceiling) finds the same wall,
> with the per-lambda maximum raw Delta_rho SHRINKING monotonically
> (0.120 -> 0.068 -> 0.038 -> 0.020) and never exceeding the original
> grid's own 0.182 ceiling; at lambda>=14 (M>=44) the raw fluctuation does
> not even reach the spec's own 0.1 magnitude bar; no cell anywhere clears
> the conditioning gate.** Phase 2 reinforces rather than
> complicates this: the Beurling twin shows a comparably sized (if
> anything slightly larger, 0.231 vs 0.182) raw fluctuation at matched
> cells [ADVERSARY: now directly confirmed, not just asserted, to be itself
> mirage-graded by the identical sig_r/sig_r1 gate -- max sig_r among the
> twin's own raw-gap cells is 1.1e-05, and the same holds at the twin's
> extended-grid cells], and the fake's own dual identity breaks at relative
> defect 0.368,
> reproducing e1m's T5a number (0.37) almost exactly. D-H unposable
> (cited); K1 guards never tripped (the source-scan exemption marker was
> also hardened this round; see `_e1q_adversary.md`).

## One-line result

The simplest genuinely lattice-consuming kernel (a periodized Gaussian,
Poisson-summed on the honest integers) was built, its rescaled dual
identity re-verified to e1m's own precision class, and tested for a
lambda-uniform well-conditioned rank collapse at the log-prime comb with
e1o's own instrument: no genuine collapse was found anywhere on the tested
grid, only a small number of conditioning-mirage fluctuations that also
appear (at comparable or greater size) on the density-matched Beurling
twin, confirming they are generic SVD-tail noise rather than an
arithmetic effect. The S4 spec's condition (2) is not met by this
construction; the wall is narrowed one notch, per the spec's own
pre-registered reading. **[ADVERSARY, lambda extension]** the wall was
re-tested at M ~ 100+ (an order of magnitude past the original grid's
M=11) and not only holds but hardens: the maximum raw fluctuation shrinks
monotonically as M grows, and the Beurling twin's own raw-gap cells are
now directly confirmed (not just asserted) to fail the identical
conditioning gate. See the Phase 1-EXT and Phase 2 sections below, and the
full attack record in [`_e1q_adversary.md`](_e1q_adversary.md).

## Phase 0: the anchor (PASS)

The rescaled dual/Poisson identity
$$\Theta_t^{(L)}(y) = \sum_{n=-80}^{80} e^{-\pi(y-nL)^2/t}
\;\overset{?}{=}\; \frac{\sqrt t}{L}\sum_{k=-80}^{80} e^{-\pi k^2 t/L^2}\cos(2\pi ky/L)$$
was checked at all four tested lambda, at 4 (y,t) pairs per lambda rescaled
directly from e1m's own T1b-tested $(x,t)$ pairs ($(0.3,1.1)$, $(0.45,0.6)$,
$(0.1,0.31)$, $(0.2,2.0)$, mapped to $y=x\cdot L$, $t = t_{\rm frac}\cdot
L^2$), at 35 decimal digits, Nwrap=Kwrap=80 fixed (matching e1m's own
truncation).

| lambda | L | max rel defect |
|---|---|---|
| 2.2000 | 1.5769 | 1.46e-36 |
| 3.0000 | 2.1972 | 1.06e-36 |
| 3.6056 | 2.5649 | 1.46e-36 |
| 6.0000 | 3.5835 | 1.06e-36 |

Every cell clears the 1e-25 bar by 11 orders of magnitude; this is the
same "already machine-verified as a genuine lattice identity" property the
build spec cited as the reason to choose this construction over a
re-entry into the closed CCM Sonin space.

**[ADVERSARY, precision-floor note].** The ~1e-36 figures above are the
`mp.mp.dps=35` WORKING-PRECISION rounding floor, not a ceiling on the
identity's true mathematical tightness. Re-running the identical check at
dps = 50 / 80 / 120 (same lambda, same (y,t) pairs) drops the measured
defect to ~1e-51 / ~1e-81 / ~1e-121, scaling almost exactly linearly with
dps, i.e. the number is measuring the arbitrary-precision library's own
rounding noise at the chosen working precision, not a fixed mathematical
gap. The TRUNCATION error alone (Nwrap=Kwrap=80, independent of working
precision) is separately bounded at ~2e-8952 (`exp(-pi*81^2)`, directly
computed; the module's original docstring comment mis-stated this as
"~1e-2800", a hand-arithmetic slip, corrected in place). Both readings
clear the spec's 1e-25 bar by an enormous margin either way, so the Phase
0 PASS verdict is unaffected; only the epistemic status of the specific
quoted digits changes (a precision-budget choice matching e1m's own
dps=35, not the identity's actual accuracy ceiling).

**Why the tested $(y,t)$ pairs are anchored at $t/L^2 \sim O(0.3\text{-}2)$
rather than at Phase 1's most extreme small-$t$ cells (a deliberate,
documented choice, not an oversight).** The primal (position-space) sum
and the dual (frequency-space) sum trade off convergence rate: the primal
converges fast for small $t$ and the dual converges fast for large $t$
(their decay rates are exactly reciprocal in $t/L^2$), so both converge
comfortably at Nwrap=Kwrap=80 only near the "self-dual" point $t/L^2\sim1$,
which is exactly where e1m's own T1b pairs live. At Phase 1's smallest
tested $t$ (the minimum pairwise gap squared in $X_\lambda$, e.g.
$t\approx0.0044$ at $\lambda=6$), the DUAL sum alone would need
$K_{\rm wrap}$ in the hundreds to hit relative defect $<10^{-25}$ (a direct
estimate: $K+1 > \sqrt{57.6\,L^2/(\pi t)} \approx 230$ at that cell),
breaking the spec's own $\le 80$ cap. The spec's Phase 0 pass criterion
requires *both* defect $<10^{-25}$ *and* $N_{\rm wrap},K_{\rm wrap}\le 80$
simultaneously; these two requirements are jointly satisfiable at the
$O(1)$ $t/L^2$ scale e1m already validated and are NOT jointly satisfiable
at Phase 1's extreme cells, so Phase 0 tests the former. This does not
weaken Phase 1's own construction: the Gram matrices $G(t)$ there are built
from the float64 PRIMAL form only, which stays safe at Nwrap=80 across the
*entire* Phase-1 range because $t\le L^2$ always holds there (worst-case
dropped-tail exponent $-\pi n^2$, e.g. $n=81$ gives $\sim 2\times10^{-8952}$
[ADVERSARY: corrected from an erroneous "$\sim10^{-2800}$"; independently
verified, `exp(-pi*81^2)` at mpmath dps=50]), and
the rank threshold (1e-8 relative) is far coarser than double precision
regardless.

**[ADVERSARY, small-t validity, Attack 3].** Directly verified, not just
argued: Nwrap=80 vs Nwrap=400 in the ACTUAL float64 `theta_wrap_np` code
path agree to 0 (exact double-precision equality) at both the smallest and
largest tested Phase-1 $t$ at $\lambda=6$; the mpmath primal wrap sum
(dps=50) agrees with Nwrap=400 to below $10^{-50}$ relative at every
$(\lambda, t, \text{node-diff})$ triple across the whole Phase-1 grid, both
extremes of $t$, using the actual node differences $x_j-x_k$ (not just
$y=0$). The spec's own $10^{-12}$ bar is cleared by 38+ orders of magnitude
at every tested cell; Nwrap=80 is not merely "safe," it is safe by a
margin that leaves no realistic doubt.

## Phase 1: the collapse test, zeta side (WALL, tier 3 MIRAGE)

Grid: $\lambda\in\{2.2, 3.0, \sqrt{13}, 6.0\}$ ($M(\lambda) = \pi(\lambda^2)
\in\{2,4,6,11\}$, e1o's own log-prime comb, identical numbers), $t$
geometric, 9 points, from the minimum pairwise gap$^2$ in $X_\lambda$ up to
$L(\lambda)^2$. 36 (lambda, t) cells total.

**33 of 36 cells: $\Delta\rho = 0.000$ exactly.** $G(t)$ and $G_0(t)$ track
full rank together throughout the small-to-mid $t$ range; the wrap
correction is Gaussian-suppressed wherever the wrap-free control is still
well-conditioned, exactly the pre-registered first branch of the wall
statement.

**3 of 36 cells: a nonzero raw $\Delta\rho$, but a conditioning mirage.**

| lambda | t | M | rank(G) | rank(G0) | Delta_rho | sig_r | sig_r+1 |
|---|---|---|---|---|---|---|---|
| 3.6056 | 6.579 | 6 | 5 | 6 | 0.167 | 1.7e-06 | 4.3e-13 |
| 6.0000 | 4.743 | 11 | 7 | 9 | 0.182 | 9.9e-06 | 5.3e-09 |
| 6.0000 | 12.84 | 11 | 5 | 7 | 0.182 | 1.9e-06 | 5.7e-13 |

All three sit at the *top* of their lambda's $t$-sweep (near or above
$L^2/2$), and all three fail the conditioning gate outright: `sig_r`
(the smallest *kept* singular value at the declared rank, relative to the
top one) is itself only $10^{-6}$ to $10^{-8}$, three to six orders of
magnitude below the spec's own $10^{-3}$ bar for a "genuine spectral gap."
Direct inspection of the full singular-value spectrum at the worst cell
(lambda=6, t=4.743) confirms why:

```
sv(G)/sv0  : 1.00e+00 3.00e-01 2.13e-01 1.03e-02 4.98e-03 2.96e-05 9.89e-06 5.32e-09 4.01e-10 1.12e-14 3.13e-16
sv(G0)/sv0 : 1.00e+00 4.30e-01 1.60e-01 4.12e-02 6.17e-03 9.21e-04 5.66e-05 3.71e-06 7.33e-08 1.46e-09 4.58e-12
```

Both are smooth-ish monotone decays overall; the 1e-8 rank
threshold simply lands at a slightly different step of the two curves.

**[ADVERSARY, mirage grading, Attack 2 -- corrected characterization].**
The original text generalized "smooth monotone decay, no clean gap
anywhere" from this one shown spectrum to all three flagged cells. A
direct, plot-free consecutive-singular-value-ratio audit at ALL THREE
cells (not just this one), now run as Check P1g every time the module
executes, finds that is not quite accurate: the ratio $\sigma_{r+1}/\sigma_r$
AT the declared-rank boundary is 3+ orders of magnitude below the MEDIAN
consecutive ratio elsewhere in the same spectrum at every one of the three
cells (this one included: boundary ratio $5.4\times10^{-4}$ vs. median
$7.5\times10^{-2}$ elsewhere). There IS a disproportionate step exactly at
the boundary in all three cases, not "no clean gap anywhere." What does
NOT change is the verdict: the step is between two already-negligible
values ($\sigma_r$ itself is only $1.7\times10^{-6}$ to $9.9\times10^{-6}$,
still three to six orders of magnitude below the $10^{-3}$ floor), so it
is a boundary between noise and deeper noise, not signal falling off a
cliff into noise. This is exactly the behavior expected of a Gaussian/RBF
kernel's well-known super-exponential eigenvalue decay, which can produce
a locally sharp RATIO step at essentially any index purely from
smoothness, with no arithmetic content at all -- which is precisely why
`is_discovery_candidate` gates on the ABSOLUTE scale of $\sigma_r$ and not
on local spectral shape: shape alone cannot distinguish a genuine
structural collapse from generic smooth-kernel tail behavior. The full
per-cell spectra and ratio audit print on every run (Check P1g); see
[`_e1q_adversary.md`](_e1q_adversary.md) Attack 2 for the complete
independent derivation.

This is exactly the conditioning-mirage failure mode
[`e1o_s4_carrier.md`](e1o_s4_carrier.md)'s adversary round caught once
already (Adversarial test case 2b, the near-commensurate decimation
family): a nonzero rank-count difference driven by threshold placement in
a smooth-ish tail, not a structural rank drop. Because no cell clears the
conditioning gate, the S4 discovery bar (Delta_rho>=0.1 AND a genuine sv
gap) is never met, and lambda-uniformity is moot (nothing to be uniform
about): the largest two lambda's max raw Delta_rho (0.167, 0.182) are
comparable, not shrinking, but the underlying signal is noise at both.

**[ADVERSARY, lambda extension, Attack 1].** The M=11 ceiling above is
statistically thin (one rank unit is $\Delta\rho\approx0.09$, right at the
0.1 discovery threshold). Re-running the IDENTICAL Phase 1 machinery
(same `node_set_zeta`/`gram_matrices`/`numeric_rank`/
`is_discovery_candidate` helpers, no reimplementation; new Checks P1e/
P1f/P1e2, "Phase 1-EXT") at $\lambda\in\{10, 14, 20, 30\}$
($M=\pi(\lambda^2)\in\{25,44,78,154\}$, M ~ 100+, an order of magnitude
past the original ceiling) finds the SAME wall, and it HARDENS:

| lambda | M | max raw Delta_rho (any cell) | sig_r at that cell | crosses the 0.1 raw-gap bar? |
|---|---|---|---|---|
| 6.0 (original grid) | 11 | 0.182 | 9.9e-06 | yes (2 cells) |
| 10 | 25 | 0.120 | 2.3e-06 | yes (1 cell) |
| 14 | 44 | 0.068 | 1.9e-06 | **no** |
| 20 | 78 | 0.038 | 1.7e-06 | **no** |
| 30 | 154 | 0.020 | 1.3e-06 | **no** |

The maximum raw fluctuation shrinks monotonically as $M$ grows (0.120 ->
0.068 -> 0.038 -> 0.020) and never once exceeds the original grid's own
0.182 ceiling; at $\lambda\ge14$ ($M\ge44$) the raw fluctuation does not
even reach the spec's own $\Delta\rho\ge0.1$ magnitude bar at all, let
alone the conditioning gate on top of it -- the "wall" is not merely
well-conditioned at large $M$, the raw signal itself is vanishing. `sig_r`
at the max-drho cell stays flat at the $10^{-6}$ noise-floor scale
throughout (never approaching the required $10^{-3}$), consistent with it
being a generic feature of the kernel's numerical conditioning rather than
a quantity that tracks $\Delta\rho$'s own decline. The periodization
invariant
($\Delta\rho\ge0$ at every cell) also holds throughout the extended grid
(Check P1e2). The verdict hardens decisively at $M\sim100+$: this is not a
small-sample artifact of an $11\times11$ measurement.

## Phase 2: the disciplines (Beurling twin, D-H cited, K1 clean)

**Beurling twin, the node-set swap (Section (c)(ii)).** The identical true
kernel run on $X_\lambda^{\mathrm B}$ (`BeurlingSystem(eps=0.25, seed=149)`,
density-matched, $M_{\mathrm B}\in\{3,4,5,13\}$ vs zeta's $\{2,4,6,11\}$) at
the exact same $(\lambda,t)$ cells zeta was tested at. Since Phase 1 never
clears the discovery bar, the spec's own comparison row applies ("twin
tracks zeta if Phase 1 walls, both nil") rather than the stricter
half-separation bound: the twin's raw fluctuations are comparable to or
larger than zeta's at the same mirage-prone cells (twin max 0.231 at
lambda=6, t=12.84, vs zeta's 0.182 at the same cell), which *reinforces*
the mirage reading directly: the effect is a generic property of
smooth-kernel SVD tails at large $t/L^2$ on a finite scattered point set of
comparable size, not something specific to the arithmetic of true primes.

**[ADVERSARY, twin fairness, Attack 4].** Three checks the BUILDER text
asserted in prose but never actually computed, now directly verified
(new Checks P2a2/P2a3, and P2h/P2h2 at the extended grid):
(i) *matched density*: $M_{\mathrm B}/M_{\mathrm{zeta}}$ at the tested
lambda is $\{1.5, 1.0, 0.83, 1.18\}$, noisy at these tiny counts as
expected of a Poisson-type process, but tightens to $\{1.04, 0.96, 0.97,
0.97\}$ at the extended grid's larger $M$ -- density-matched by
construction, confirmed rather than assumed. (ii) *identical t-grid and
threshold*: confirmed by direct code read, the twin loop consumes
`t_grid_by_lambda[lam]` (Phase 1's own computed grid) verbatim and calls
`numeric_rank` with the same global `RANK_THRESH`; no independent
recomputation, no separate threshold. (iii) *the sharp one*: is the twin's
own larger raw fluctuation (0.231) itself mirage-graded by the SAME
`sig_r`/`sig_r1` gate zeta's cells are held to, or is the "generic noise"
reading merely asserted? Previously merely asserted: the twin loop called
`numeric_rank` and discarded the singular values (`rG, _ = numeric_rank(G)`).
Now captured and checked (Check P2a2): the twin's own raw-gap cells
(lambda=6, t=4.743 and t=12.84) have `sig_r` = 1.1e-05 and 1.6e-06
respectively, both far below the $10^{-3}$ bar -- the "mirage, not
arithmetic" reading is verified by the identical numeric criterion, not
just argued by analogy. The same holds at the extended grid (Check P2h).

**Beurling twin, the fake's own construction (Section (c)(i)).** Rather
than inventing a novel L-rescaled hybrid periodization on the fake's
generalized integers (no such construction reduces cleanly to the true
wrap sum when unperturbed, so any such hybrid would be an arbitrary,
underdetermined choice), this rung reproduces e1m's own T5a construction
verbatim: $\theta_{\mathrm B}(u) = 1 + 2\sum_{\ell\in\mathrm{gen\_ints}(B),\,
\ell>0} e^{-\pi e^{2\ell} u}$ (`BeurlingSystem(prime_bound=15000, eps=0.25,
seed=149)`, `gen_integers(40)`), tested against its own would-be FE
$\theta_{\mathrm B}(1/t) \overset{?}{=} \sqrt t\,\theta_{\mathrm B}(t)$ at
$t\in\{0.7,1.3,2.0\}$. **Measured relative defect: 0.368**, against a true-Z
defect $<10^{-25}$ and e1m's own T5a citation of 0.37: the reproduction is
essentially exact, both confirming the port and satisfying the clause (Z
replaced by the fake's generalized integers breaks the dual identity by a
nameable, O(1) amount, independent of Phase 1's own outcome).

**D-H (cited, not recomputed).** Two independent arguments, per the
spec's Section (c): AX-FORM (the node set $X_\lambda$ exists only because
zeta has an Euler product; D-H's coefficient comb is dense and
sign-changing, 25 sign changes below $n=60$, negative excess exhibit
$-0.288$ at $(x{=}10,\delta{=}2)$, [`e1o_s4_carrier.md`](e1o_s4_carrier.md)
T5a) and type exclusion (the kernel's conductor-1 theta sum matches
zeta's own gamma factor; D-H's own FE is exact to $1.7\times10^{-30}$ but a
Riemann-type reconstruction fails at $O(1)$, defect 1.72, budget surplus
$\sim$20.7 zeros at $T=85.699$, [`e1m_hamburger_pin.md`](e1m_hamburger_pin.md)
T2). Both hold regardless of Phase 1's outcome; no D-H numeric rerun.

**K1.** Source scan clean (no zero-list/zero-scanner token in the
theta-wrap path); runtime guards on `mp.zetazero` and the D-H zero scanner
installed, never tripped; `consume()` ledger printed per phase (primes,
$\mathbb Z$/window geometry, Beurling logs/gen-integers, D-H citation
numbers only -- no zero of any L-function, at any step).

**[ADVERSARY, K1 scanner hardening].** An injection test (a scratch copy,
outside the repo, with an unguarded `mp.zetazero(1)` call added) found the
source scan's exemption check was a bare substring test for `"K1-ALLOW"`
anywhere in a line, which a crafted comment *discussing* K1-ALLOW without
actually marking one (e.g. "...no K1-ALLOW") could slip past. The RUNTIME
guard caught the same injection immediately regardless (defense in depth
held), but the static scan's exemption was tightened to require the
marker as an actual trailing-comment token, `"# K1-ALLOW"`, matching the
two real guard-install lines verbatim; re-verified the two legitimate
exemptions still pass and the crafted injection is now caught. This is a
heuristic hardening, not a proof: a comment engineered to contain the
literal substring `"# K1-ALLOW"` without being a genuine exemption would
still slip past any purely textual scan, which is exactly why the runtime
guard, not the source scan, is the load-bearing K1 enforcement.

## Grading (spec Section (d))

**Tier 3, MIRAGE.** No cell clears the conjunction of wrap-attributable
($\Delta\rho\ge0.1$) and well-conditioned (a genuine singular-value gap);
the three cells that clear the magnitude bar alone fail conditioning by
three to six orders of magnitude, confirmed by direct spectrum inspection
to be noise-floor-scale threshold artifacts (ADVERSARY-audited: a genuine
ratio-sense step exists at the boundary in all three cases, but strictly
between two already-negligible values, so it is the absolute scale, not
the local shape, that correctly identifies it as noise, not a structural
rank drop). This is the
"MIRAGE" sub-case of tier 3, not its plainer "BLIND" sub-case (33 of 36
cells never even raise a raw signal) -- a distinction the build spec's own
grading scheme (Section (d), item 3) anticipated and separately named.
**[ADVERSARY, lambda extension]** confirmed to persist and harden at
M ~ 100+ (an order of magnitude past this grid's own M=11 ceiling); see
the Phase 1 section above and [`_e1q_adversary.md`](_e1q_adversary.md).

| field | verdict |
|---|---|
| `phase0_anchor` | PASS: rel defect ~1e-36 (dps=35 precision floor; the true, precision-independent bound is far tighter) at every tested lambda, 11+ orders of magnitude inside the 1e-25 bar |
| `phase1_collapse` | WALL: Delta_rho=0.000 at 33/36 cells; 3/36 cells show raw Delta_rho up to 0.182 but ALL fail the conditioning gate (sig_r 1e-6 to 1e-8 vs required >1e-3): confirmed mirage by direct sv-spectrum + ratio-audit inspection (ADVERSARY, Attack 2) |
| `phase1_ext` **[ADVERSARY]** | HARDENS: identical battery at M in {25,44,78,154} (M ~ 100+) finds the same wall, max raw Delta_rho shrinking monotonically (0.120->0.068->0.038->0.020), never exceeding the original grid's 0.182 ceiling, not even reaching the 0.1 raw-gap bar at all for M>=44, no cell clearing the conditioning gate |
| `phase2_beurling_twin` | Twin's raw fluctuations at matched cells are comparable to or larger than zeta's (0.231 vs 0.182 at the worst cell): reinforces the mirage reading, not a genuine arithmetic effect; **[ADVERSARY]** now directly confirmed (not just asserted) mirage-graded by the identical sig_r/sig_r1 gate, at both the original and extended grids |
| `phase2_beurling_construction` | The fake's own dual identity breaks at relative defect 0.368 (true Z: <1e-25), reproducing e1m's T5a citation (0.37) almost exactly |
| `dh_unposable` | TRUE (cited: AX-FORM + type exclusion, e1o T5a / e1m T2) |
| `k1_clean` | TRUE (guards never tripped; source scan clean, exemption marker hardened by ADVERSARY after an injection test; ledger printed; no zero of any L-function consumed) |
| `grade` | tier 3 (MIRAGE): the S4 spec's condition (2) is NOT met by this construction |
| `frontier` | UNMOVED, narrowed one notch, and the narrowing is now hardened at M ~ 100+: a construction that PROVABLY consumes the additive lattice (unlike KNS's density criterion, unlike raw trig decimation, unlike the closed majorant route) still cannot produce a well-conditioned collapse at {k log p} with the simplest such device, at any tested scale from M=2 to M=154. Per the build spec's own pre-registered reading, this points at the one genuinely unexplored corner named in the frame audit: Cohn-Elkies/Viazovska/Radchenko-Viazovska modular interpolation (genuine modular forms and Hecke structure, not a bare theta function) |

## Tiered claims

**PROVEN (classical mathematics, instantiated here):**
1. The period-$L$ dual/Poisson identity itself (a direct rescaling of the
   classical Jacobi theta transformation), re-verified to $10^{-36}$-class
   precision at four lambda (Phase 0).
2. $G_0$ (the wrap-free control) is a Gaussian/RBF kernel, PSD for
   distinct nodes at any bandwidth in exact arithmetic; the observed
   numerical rank deficiency at large $t$ is a threshold artifact of a
   smooth eigenvalue decay, not a violation of positive-definiteness
   (confirmed by the printed spectra, both PROVEN and NUMERICAL).

**NUMERICAL (measured on this implementation):**
3. Delta_rho = 0.000 at 33/36 (lambda,t) cells (Phase 1).
4. The 3 nonzero raw Delta_rho cells and their conditioning-pair numbers
   (table above); the full sv spectra at the worst cell.
5. The Beurling twin's matched-cell fluctuations (table in Phase 2),
   comparable to or larger than zeta's own mirage-level numbers.
6. The fake's own dual-identity defect, 0.368 (Phase 2b), reproducing
   e1m's T5a citation.
7. D-H's cited numbers (25 sign changes, -0.288 excess, 1.72/20.7 type
   exclusion): unchanged from e1o/e1m, not recomputed here.

**STRUCTURAL / CONJECTURE:**
8. The reading that the missing mechanism must tie the additive lattice
   to the multiplicative (Euler-product) structure nontrivially (the
   build spec's own closing paragraph); this probe's contribution is
   narrowing that claim by elimination (a bare theta kernel does not do
   it), not establishing the positive claim itself.

## Deviations from the spec (one line each, per the tasking's own discipline)

- **Phase 0's tested $(y,t)$ pairs are anchored near $t/L^2\sim O(1)$
  (e1m's own T1b range), not at Phase 1's extreme small-$t$ cells.**
  Reason: the spec's own Phase 0 pass bar requires both defect $<10^{-25}$
  and $N_{\rm wrap},K_{\rm wrap}\le80$ simultaneously; at Phase 1's smallest
  tested $t$ the dual sum alone needs $K_{\rm wrap}$ in the hundreds to hit
  $10^{-25}$, so the two conditions are jointly satisfiable only at the
  $O(1)$ $t/L^2$ scale, which is exactly where e1m's own tested pairs live
  (see the "why" paragraph under Phase 0 above). Phase 1's own Gram
  matrices are unaffected: they use the float64 primal form, safe at
  Nwrap=80 across the *entire* Phase-1 range.
- **Phase 2(c)(i) ("Z replaced by BeurlingSystem's generalized integers in
  the wrap sum") is implemented as a verbatim reproduction of e1m's own
  T5a construction** (the un-rescaled theta_B FE check) rather than a novel
  L-dependent hybrid periodization. Reason: no L-rescaled construction
  substitutes generalized integers for $\mathbb Z$ in the periodization sum
  without an arbitrary, spec-underdetermined rescaling choice; the spec's
  own phrase "by direct analogy to T5's measured 0.37 for the un-rescaled
  case" anchors this reading, and the reproduction (0.368) matches the
  citation almost exactly, both validating the port and satisfying the
  clause (a nameable, O(1) construction-level failure).
- **The `sig_r`/`sig_{r+1}` conditioning gate is applied as a strict
  precondition for treating any raw Delta_rho as meaningful (P1c, P2a,
  and the grading function all share one helper, `is_discovery_candidate`)**,
  rather than reporting raw Delta_rho>=0.1 as a naive pass/fail signal.
  Reason: an early draft of this module treated raw Delta_rho>=0.1 alone
  as the bar and the three mirage cells then registered as spurious
  self-test FAILures; the spec's own Phase 1 text makes the conditioning
  requirement part of the *definition* of a positive discovery, not a
  separate downstream filter, so the checks were corrected to match the
  spec's own bar exactly (documented in the module's `is_discovery_candidate`
  docstring).
- **[ADVERSARY, lambda extension]** The build spec's own lambda grid is
  $\{2.2, 3.0, \sqrt{13}, 6.0\}$ (chosen for exact numeric comparability
  with e1o's baseline); the ADVERSARY round extended it to
  $\{10, 14, 20, 30\}$ (M ~ 100+) to close the small-M-triviality attack
  surface. This is an addition beyond the spec's literal grid, not a
  deviation from it: the extension reuses the spec's own construction and
  thresholds verbatim (new Checks P1e/P1f/P1e2/P2h/P2h2, "Phase 1-EXT"/
  "Phase 2-EXT"), and the original grid's own numbers are unchanged and
  still separately checked.

## Limitations

- The ORIGINAL node sets are small ($M\in\{2,4,6,11\}$): the SVD/rank
  measurements at $\lambda=2.2$ (a $2\times2$ matrix) carry limited
  statistical weight; this is inherited directly from e1o's own carrier
  convention (chosen for direct numeric comparability with e1o's
  baseline), not a new choice. **[ADVERSARY]** this limitation is now
  substantially addressed, not merely noted: the lambda extension
  (M up to 154) reproduces the identical wall with the raw fluctuation
  shrinking as M grows, so the tier-3 verdict does not rest on small-M
  statistics alone.
- The kernel tested is the simplest possible lattice-consuming device (a
  bare periodized Gaussian). The build spec's own closing section
  anticipated a wall at this rung and named genuine modular forms
  (Cohn-Elkies/Viazovska/Radchenko-Viazovska) as the next, structurally
  different candidate; this probe does not attempt that construction.
- Phase 2(a)'s twin comparison is only informative at cells where zeta
  itself shows a signal; since Phase 1 never clears the discovery bar, the
  comparison is necessarily a "both near-nil, comparably noisy" reading
  rather than a sharp separation, exactly as the spec's own summary table
  anticipates for a walled Phase 1. **[ADVERSARY]** the twin's own
  "near-nil, comparably noisy" cells are now directly confirmed
  mirage-graded by the same numeric gate (Check P2a2), not merely
  asserted noisy by eyeball comparison of raw Delta_rho.
- An ADVERSARY round has now been run on this rung (2026-07-17, verdict
  PASS_WITH_FIXES; full record [`_e1q_adversary.md`](_e1q_adversary.md)):
  the small-M attack surface, the twin-fairness gap, the mirage-shape
  overgeneralization, a K1 scanner robustness gap, and a periodization-
  invariant blind spot were all found and fixed or closed. What remains
  genuinely untested: a systematic search for a smarter node-set/kernel
  family that might collapse well-conditionedly (analogous to e1o's own
  five-family adversary sweep) has still not been attempted on THIS
  (theta-wrap) construction specifically.

## Handed forward

- **ADVERSARY round complete** (2026-07-17, verdict PASS_WITH_FIXES; full
  record [`_e1q_adversary.md`](_e1q_adversary.md)): the small-M attack
  (resolved: wall hardens through M ~ 100+), the twin-fairness gap
  (resolved: twin's own cells now directly confirmed mirage-graded), the
  mirage-shape overgeneralization (corrected: absolute scale, not local
  shape, is the load-bearing criterion), a K1 scanner robustness gap
  (hardened, with the residual text-marker limitation named honestly), a
  periodization-invariant blind spot (closed with new guard checks), and a
  precision-floor / hand-arithmetic-slip pair of minor numeric corrections
  (Phase 0's ~1e-36 figure; the dropped-tail exponent estimate).
- **To a future ADVERSARY or BUILDER round**: (i) the conditioning-gate
  thresholds themselves (1e-3 / 1e-6) are e1o's own convention, reused
  verbatim; stress-testing whether a different threshold pair changes the
  tier-3 verdict at the flagged cells (original or extended grid) would be
  a cheap, valuable check, not yet done; (ii) the Phase 0 anchoring
  deviation (documented above) is a judgment call, not a forced move; a
  smarter precision/truncation scheme that reaches Phase 1's extreme
  small-$t$ cells at the full 1e-25 bar without breaking the
  Nwrap/Kwrap<=80 cap is still open (though Attack 3 shows the current
  choice is safe by a vast margin regardless); (iii) a systematic search
  for a smarter node-set/kernel family that might collapse
  well-conditionedly (analogous to e1o's own five-family adversary sweep)
  has still not been attempted on this construction.
- **To SURVEYOR (next round)**: the Cohn-Elkies/Viazovska/Radchenko-Viazovska
  modular-interpolation corpus, named by the build spec's own closing
  section as the next rung and confirmed by the frame audit as having zero
  prior repo mentions.
- **To BUILDER (next executable)**: a genuine modular-form interpolation
  kernel (not a bare theta function) tested with the identical
  rank/cost-ratio instrument this rung reused, per the build spec's own
  forward pointer.
- **To SYNTHESIZER**: one line: "e1q built the theta/Poisson wrap-collapse
  kernel (the form-side S4 rung), re-verified the period-L dual identity
  to machine precision, and measured NO well-conditioned rank collapse at
  the log-prime comb anywhere on the tested grid from M=2 to M=154 (ADVERSARY-
  extended, hardening as M grows): the only nonzero signal
  is a conditioning mirage (confirmed by direct spectrum inspection and a
  plot-free ratio audit) that
  also appears, and is itself independently confirmed mirage-graded, on the
  Beurling twin, at comparable or larger size; the
  simplest lattice-consuming kernel is not the missing S4 mechanism, which
  narrows the search toward genuine modular-form/Hecke structure."

## Reproduce

```
python -m experiments.spectral.e1q_s4_theta_wrap_rung           # full (~1.6 s)
python -m experiments.spectral.e1q_s4_theta_wrap_rung --quick   # reduced grids (~0.0 s)
```

Outputs `e1q_s4_theta_wrap_rung.npz` (Phase 0 per-lambda defects; Phase 1
per-cell lam/t/M/rho/rho0/drho/sig_r/sig_r+1 arrays; Phase 1-EXT and
Phase 2-EXT arrays at the extended lambda grid; Phase 2 twin arrays
and the fake's dual-identity defect). `--quick` does NOT write the npz
(matching e1o's own convention: the tracked artifact is the full run's;
filesystem-verified byte-identical and mtime-identical after a `--quick`
run, ADVERSARY round 2026-07-17). No external cache is read or written;
all inputs are primes up to
$\lambda^2\le900$ (the ADVERSARY-extended grid's largest lambda=30), the
integers/window geometry, and the Beurling fake's
generator (`_shared/beurling.py`, `eps=0.25, seed=149`). The full attack
record, including checks and numbers not repeated here, is
[`_e1q_adversary.md`](_e1q_adversary.md).
