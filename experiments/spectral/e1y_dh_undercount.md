# E1Y: why does D-H undercount the lattice? The #169 handed-forward look

> Companion to `e1y_dh_undercount.py` / `.npz`. Answers the one open
> mechanism question LEARNINGS #169 (e1s) handed forward, and the TODO item
> "the D-H undercount look (one look)". Reuses e1k's `build_float` /
> `operator_spectrum` verbatim; no operator is rebuilt, no zero list is read
> (K1 guards installed on `mp.zetazero` and the D-H scanner, never tripped).
> **21/21 checks pass in full mode** (4669 s at dps 25 on a contended box).
> ADVERSARY round self-run 2026-08-17/18, [`_e1y_adversary.md`](_e1y_adversary.md):
> **PASS_WITH_FIXES**, one claim demoted (see the dps bullet under Caveats)
> and the mechanism confirmed causally.
> It proves nothing about RH.

## The question

The e1s adversary round (2026-07-12) extended the count grid past `lam = 3`
and demoted an empirical claim: D-H does **not** hit the geometric lattice
count `floor(T/phi)` exactly at every `lam`. It undercounts by 1-2, ghost-free
(`unfiltered = filtered`), at `lam` in {3.3, 3.6, 4.0, 4.5}, and at
`lam = sqrt13` it is zeta-OFF (33, exact) rather than D-H (31) that anchors
the lattice. The catch was banked with its mechanism uncharacterized, and the
script that found it lived in the gitignored `scratchpad/` and is absent on
this machine, so this rebuilds the measurement and asks WHY.

## One-line result

**It is not arithmetic. It is where this reconstruction stops being defined.**
On every D-H build at `lam >= 3.3` the Weil form has a near-null ground state,
so the selected even ground state `xi` is nearly orthogonal to `delta` and the
secular normalization `xi_n = xi/(delta . xi)` -- the quantity
`operator_spectrum` literally divides by -- is inflated by three orders of
magnitude. Every residue `r_k = L^{-1/2} phi k (xi_n)_k` inflates with it,
roots leave their lattice anchors, and the count falls short. Above
`lam = 3.3` the same builds also violate the paper's evenness assumption
outright (`even_assumption_ok = False`, the flag `build_float` records rather
than silently uses, Remark 2.3). Stripping D-H's coefficient signs, or moving
its comb under zeta's archimedean density, repairs both the ground state and
the count; scrambling zeta's comb, flattening it to `Lambda = 1`, or flipping
half its signs breaks neither. So the deviation reads a conditioning property
of one build, never a zero location: the #158/#161 blind class.

## The measurement (pole OFF, `N >= n_hi + 7` so truncation never binds)

`dev` = window count minus lattice count; `sweep` = the range of `dev` as the
window edge `T` slides across the whole top lattice gap; `adm` = the build is
admissible (`even_assumption_ok` and `|delta.xi| > 1e-2`).

| lam | case | latt | dev | sweep | adm | eps | delta.xi | \|r_(n_hi)\| |
|---|---|---|---|---|---|---|---|---|
| 3.0 | Zoff | 19 | +0 | [+0,+0] | yes | -4.83 | 5.85e-01 | 1.77e-02 |
| 3.0 | DH | 19 | +0 | [-1,+0] | no | **8.05e-05** | **-2.09e-03** | 4.70e-01 |
| 3.3 | Zoff | 26 | -1 | [-1,+0] | yes | -5.34 | -5.59e-01 | 1.28e-01 |
| 3.3 | DH | 26 | -2 | [-2,-1] | no | **7.60e-05** | **7.17e-04** | 2.52e-01 |
| 3.6 | Zoff | 33 | +0 | [-1,+0] | yes | -5.84 | -5.68e-01 | 4.48e-02 |
| 3.6 | DH | 33 | -2 | [-2,-1] | no | **2.65e-05** | **-9.38e-04** | 6.59e-01 |
| sqrt13 | Zoff | 33 | +0 | [+0,+0] | yes | -5.85 | -5.65e-01 | 1.48e-02 |
| sqrt13 | DH | 33 | -2 | [-2,-1] | no | **3.34e-05** | **-9.82e-04** | 6.38e-01 |
| 4.0 | Zoff | 44 | +0 | [+0,+0] | yes | -6.49 | 5.60e-01 | 5.45e-03 |
| 4.0 | DH | 44 | -2 | [-2,-1] | no | **1.71e-06** | **9.47e-05** | 4.23e-01 |
| 4.5 | Zoff | 60 | +0 | [+0,+0] | yes | -7.26 | 5.89e-01 | 8.66e-02 |
| 4.5 | DH | 60 | -2 | [-3,-2] | no | **5.42e-06** | **1.78e-06** | 6.11e-01 |

Three things fall out of that table and none of them is about arithmetic.

**(i) The catch reproduces, and zeta-off is not perfect either.** D-H deviates
at five of six `lam`; zeta-OFF deviates by -1 at `lam = 3.3`. That single
zeta-off deviation is fully explained by the window geometry: at `lam = 3.3`,
`2 lam^2 log lam = 26.003`, so the top lattice point sits **0.4%** of a gap
below the two-meter height `T`, and the root that would be counted there falls
just above it. Slide `T` anywhere else in that gap and the count is exact
(`sweep = [-1,+0]`, exact for 96% of placements). Nothing to explain.

**(ii) The T-sweep separates two different things.** A deviation is
RECOVERABLE if some placement of `T` inside the top gap restores the lattice
count, and STRUCTURAL if none does. Every zeta-side build in the probe is
recoverable. Five of six D-H builds are structural. That is the real
distinction, and it is threshold-free: it asks whether `0` lies in the swept
range, nothing more.

**(iii) The conservation law also breaks, in the same cells, but for a
DIFFERENT reason.** By the negation symmetry of `spec(M)` (e1p's derivation: `J M J^-1 =
-M` for even `xi`), the `2N+1` eigenvalues must split N-positive / one zero /
N-negative, so `#{Re > 0} = N` and a window deficit can only be an eigenvalue
that left the window. That identity holds in every zeta-side cell and fails in
exactly the five structural D-H cells (`n_pos` short by 1, and by 2 at
`lam = 4.5`): eigenvalues are collapsing toward the origin. This is a
count-free symptom, measured independently of any window, and it agrees cell
for cell with the `delta.xi` diagnostic. **It is not, however, the same
phenomenon as the count deficit**, which this file originally implied. The
adversary round's A6 inflates a healthy build's residues by hand and finds
`n_pos = N` preserved at every scale factor, up to 3000x, while the count
deficit appears at 10x. So residue inflation causes the deficit and does not
cause the conservation failure. Nor does the evenness violation: `lam = 3.3`
has `even_assumption_ok = True` at every precision and still breaks
conservation. **The cause of the conservation failure is an open residual.**

## The mechanism

`M = D_log - |D_log xi_n><delta|` with `xi_n = xi/(delta . xi)`, and its real
eigenvalues are the zeros of the secular function
`s(z) = 1 - sum_k r_k/(phi k - z)` with `r_k = L^{-1/2} phi k (xi_n)_k`. The
normalization sits in front of every residue, so `delta . xi -> 0` inflates
the whole secular equation at once. Measured across the grid, the median
`|delta.xi|` is **788x smaller** on the deficient builds (7.17e-04 vs
5.65e-01) and the median top-mode residue `|r_(n_hi)|` correspondingly
**13.7x larger** (6.11e-01 vs 4.48e-02). That is the entire story: a rank-one
perturbation whose strength has been multiplied by a thousand does not leave
the spectrum near its unperturbed lattice.

**Shown causally, not just by correlation (ADVERSARY A6).** The two repairs
below each change the comb, so each changes everything at once. The direct
intervention keeps the build fixed and scales `xi_n -> c xi_n`, which is
exactly `delta.xi` shrunk by `1/c` with nothing else touched. On a healthy
zeta-off build at `lam = sqrt13`: `dev` is 0 at `c = 1` and `c = 3`, turns
**-2 and structural at `c = 10`** (effective `|delta.xi| ~ 5.6e-2`), and
saturates at -9 beyond. `lam = 4.0` behaves identically. So residue inflation
alone breaks a sound build's count, and the construction is MORE sensitive
than the 788x median ratio quoted above suggests: the threshold is about 10x.

The verdict does not rest on where the admissibility cut was placed. The
probe re-runs the classification across 25 cuts spanning two decades of
`|delta.xi|` (3e-3 to 3e-1) and requires the same answer at every one. What
makes that work is the separation between the two *builds*, not between
"deficient" and "sound" counts: every zeta-side cell has `|delta.xi| >= 0.46`
and every D-H cell has `|delta.xi| <= 2.1e-3`, a factor of at least 220, so
any cut in that range puts the same cells on the same sides. Worth stating
plainly because the naive version of the claim is false: the largest
`|delta.xi|` among structurally deficient cells (9.8e-4) is only 2.1x below
the smallest among recoverable ones (2.1e-3, which is D-H at `lam = 3.0` --
an equally sick build whose count happens to still be recoverable). Sickness
is not a step function; the classification is stable anyway.

## The controls

**Repair (U5), both without touching the arithmetic content class.**

| intervention | eps | delta.xi | sweep | verdict |
|---|---|---|---|---|
| `DH` (native) | ~1e-5 | ~1e-3 | [-2,-1] | structural deficit |
| `DH-abs` = \|Lambda_DH\| | -1.8 .. -2.8 | 0.57 .. 0.64 | [-1,+0] | repaired |
| `DH-inZ` = D-H comb, zeta density | -2.6 .. -2.8 | 0.21 .. 0.32 | [-1,+1] | repaired |

Both interventions restore a sound ground state and remove the structural
deficit. Note what `DH-inZ` isolates: D-H's comb is fine under zeta's
archimedean density. The near-null ground state needs the *combination* of
D-H's dense period-5 coefficient stream with D-H's own density
(`dens_a = 3/4`, conductor 5), which is a statement about this finite build,
not about the L-function.

**Blindness (U6), the converse direction.** Permuting zeta's comb values
across the same support (arithmetic destroyed, magnitudes kept), replacing it
with the flat non-arithmetic comb `Lambda(n) = 1`, and flipping the signs of
half its support all leave `eps` sound (-1.95 to -8.05), `delta.xi` sound
(0.46 to 0.63) and the count exactly matching zeta-off's at every `lam`. So
zeta's exactness is not the Euler product and not the sign pattern; it is
genericity of a well-conditioned build. In particular the tempting reading
"D-H undercounts because its `Lambda` changes sign" is **refuted by its own
converse**: signs flipped into zeta do not manufacture the deficit.

## What this does to the record

- #169's ADVERSARY catch (i) stands as a statement about the numbers: D-H is
  not `floor(T/phi)` exactly at every `lam`, and the "EXACTLY / deviation 0 at
  every lambda" wording was correctly demoted.
- Its **type** changes. The right reading is not "a genuine `O(1)` deviation
  at larger lambda" but "the D-H cells at `lam >= 3.3` are outside this
  harness's validity domain", flagged by the harness's own instrument. On
  admissible pole-off builds the count is the geometric lattice count up to
  where the window edge falls.
- The RIGOROUS backbone is untouched either way. It was always Weyl-on-`Q`
  (`|N_Qon(t) - N_Qoff(t)| <= rank(P) = 2`), which uses the Hermitian form and
  never the ground state's evenness or the secular normalization. See the
  companion reconciliation note added to `e1p_rank_one_interlacing.md` and
  `e1s_rank_one_interlacing.md` the same day.
- The frontier is UNMOVED. This retires a handed-forward puzzle and slightly
  tightens the count half of the W6 clause. M4 is untouched.

## Caveats

- **dps sensitivity is worse than a caveat, and the ADVERSARY round
  (`_e1y_adversary.md`, attack A2) demoted this file's first defence of it.**
  An earlier version of this bullet said the *classification* was what the
  probe rests on rather than the individual integers. That is FALSE: the
  structural/recoverable class flips with working precision at two of three
  D-H cells (`lam = sqrt13` reads recoverable at dps 15 and structural at
  25/35; `lam = 4.0` reads structural at 15/25 and recoverable at 35, where
  D-H's count is exact). What actually carries the finding is that the
  instability is **one-sided**: over dps {15, 25, 35}, zeta-off is class-stable
  at 3/3 cells with `eps` reproducing to four digits and `|delta.xi|` to
  three, while D-H is stable at 1/3 with `eps` wandering by factors of 4 to 50
  *including sign changes*, `|delta.xi|` by factors of 20 to 130 *including
  sign changes*, and `even_assumption_ok` itself flipping. That is the
  signature of a quantity that is zero being reported as noise, so the honest
  statement is stronger than the one this file made: on those builds
  `delta.xi` is numerically indistinguishable from zero at every reachable
  precision, `xi` is the eigenvector of a numerically degenerate eigenvalue
  and rotates freely as precision changes, and `xi_n = xi/(delta.xi)` is
  **undefined** rather than merely ill-conditioned. The count's
  precision-dependence is a consequence of that, not a rival explanation.
- **Protocol robustness (A1) held**: the class is stable across `N` margins
  {3, 7, 12, 20} at every `lam`, so `n_hi + 7` is not driving anything.
- **The "lattice pinning" reading is false and was dropped.** An earlier
  version of this analysis claimed zeta's top root is glued to the top lattice
  point. It is not: at `lam = 4.0` zeta-off's next root sits 0.99 of a gap
  above it and the count is still exact for every placement of `T`. Where
  individual roots sit is not what the count tracks.
- `N >= n_hi + 7` is a protocol choice this reconstruction had to make,
  because the absent adversary script did not record its own. It is chosen so
  the operator's mode truncation never binds
  (`min(N, floor(T/phi)) = floor(T/phi)`), which is what makes the question
  well-posed; with a smaller `N` the "undercount" would be trivially forced.
- Every e1k/e1l caveat is inherited (float harness, razor-thin eps margins,
  the ghost mechanism is the dps-dependent part). Beurling is not buildable as
  an operator here (comb-side only, per e1s).

## Verdict fields

| field | value |
|---|---|
| `undercount_reproduced` | YES. Five of six D-H cells deviate; the #169 catch was right about the numbers |
| `mechanism` | GROUND-STATE CONDITIONING. Near-null `eps` (~1e-5 vs zeta's -5) makes `xi` nearly orthogonal to `delta`; the secular normalization `xi/(delta.xi)` inflates every residue (median 788x on `delta.xi`, 13.7x on `\|r_(n_hi)\|`) |
| `arithmetic_sensitive` | NO, in both directions. `\|Lambda_DH\|` or zeta's density REPAIRS it; scrambling, flattening or sign-flipping zeta's comb does not BREAK it |
| `harness_self_flagged` | YES. `even_assumption_ok = False` on every D-H cell at `lam >= 3.3`, and `\|delta.xi\|` is 2-3 orders below the zeta-side population at every `lam` |
| `count_law_on_admissible_builds` | the pole-free count equals the geometric lattice count up to the window-edge placement, on every admissible build measured |
| `rigorous_backbone_affected` | NO. Weyl-on-`Q` never uses the ground state |
| `rh_content` | NONE. A coefficient/conditioning property, never a zero location (#158/#161 class) |
| `k1_clean` | YES (guards installed, never tripped; only combs and geometry read) |
| `frontier_delta` | ZERO. Retires a handed-forward puzzle; M4 untouched |
