# E1Q: rank-one interlacing on the CCM D_log family (LEARNINGS #154 item 2)

> Companion to `e1s_rank_one_interlacing.py` / `.npz`. Executes item 2 of the
> #154 W6 upgrade spec: "rank-one interlacing (count moves by <= 1: the count
> is already nearly independent, the gap is the height-dependence, not the
> count)". Reuses the e1k `build_float` / `operator_spectrum` harness
> (arXiv:2511.22755 Thm 5.10; ZETA_CFG/DH_CFG) at dps=25. No operator is
> rebuilt from scratch; only counting and rank bookkeeping are added. It
> proves nothing about RH. It measures one upgrade-spec ingredient and reports
> a clean split of the W6 pole-budget clause. All numbers from the default
> full run (14/14 self-tests, ~3 min).

> **BANNER (read before quoting any number).** Two matrices, two interlacing
> stories, and the whole reconciliation is not to conflate them. (1) The Weil
> form `Q` is Hermitian and zeta's `Q = (entire part) + P` with `rank(P) = 2`
> (measured); WEYL interlacing on `Q` is RIGOROUS: the eigenvalue count moves
> by `<= 2` (measured max move 1). (2) The operator `M` (whose eigenvalues are
> the physical determinant zeros) is a RANK-1 perturbation of the diagonal
> lattice `D_log`; the pole-off count `n_win = floor(T/phi)` EXACTLY (= D-H =
> the geometric lattice count), and the pole's effect splits into `<= 2`
> eigenvalue DISPLACEMENT (the interlacing-governed count, respects rank(P))
> plus a GHOST reality-breaking artifact (filtered out, NON-interlacing). So
> the tasking's "shift of 4 exceeds rank 2" is RESOLVED: the interlacing count
> moves by `<= 2`; the extra drop is the ghost filter. HONEST CAVEAT: the
> secular residues are NOT sign-definite, so the clean "one eigenvalue per
> lattice gap" interlacing does NOT hold; the count pinning rests on the
> rank-1 displacement + reality + the measured pole-free lattice exactness.
> All integer counts are O(1)-dps-fragile (e1l STEP 5); the ghost mechanism IS
> the dps-dependent part. Net: the COUNT half of the W6 budget goes structure-
> cheap (rigorously via Weyl-on-`Q`, and the pole-free count equals the lattice
> count up to `O(1)`); the LOCATION half (= M4) is untouched.
>
> **ADVERSARY (2026-07-12), grid extension DEMOTES two empirical claims (the
> rigorous backbone survives).** (i) "`D-H n_win = floor(T/phi)` EXACTLY at
> EVERY lambda" is FALSE: D-H undercounts the lattice by 1-2 (GHOST-FREE, i.e.
> genuine, `unfiltered = filtered = lattice - 2`, not a `|Im|`-filter artifact)
> at `lam` in {3.3, 3.6, 4.0, 4.5}. Exactness holds only at the tested
> `lam <= 3` (and `lam = 5`); at `lam = sqrt13` it is zeta-OFF (33, exact), NOT
> D-H (31), that hits the lattice, so the "D-H = the clean ghost-free entire-
> part count" framing is backwards there. `Zoff` itself deviates -1 at
> `lam = 3.3, N = 32`. (ii) "unfiltered `M` displacement `<= rank(P) = 2`" is
> GHOST-FRAGILE: it reads 3 at `lam = sqrt13, N = 34` under this probe's own
> `cell()` machinery (a rank-1 NON-normal `M` perturbation, `rank(M_on-M_off)=1`,
> carries NO interlacing bound; a second equally-valid build reads 2). The ONLY
> rigorous count-cheap statement is Weyl-on-`Q` (`|N_Qon-N_Qoff| <= rank(P)=2`,
> robustly held at EVERY extension cell); the `M`-count "exactness" is a fragile
> non-normal shadow, not a bound. The W6 count/location split survives in the
> "count = lattice up to `O(1)`" form; the "EXACTLY / deviation 0 at every
> lambda" wording does not.

## One-line result

The count half of #154's W6 pole-budget clause is discharged by interlacing up
to `O(1)`: the number of eigenvalues below the two-meter edge is the geometric
lattice count `floor(T/phi)` (exactly at the tested `lam <= 3` for D-H and
zeta-with-pole-off, and up to a genuine `O(1)` deviation at larger lambda,
ADVERSARY 2026-07-12), the RIGOROUS content being Weyl-on-`Q` (`<= rank(P) = 2`,
robust); the apparent extra "pull toward RvM" is the approximate-self-adjointness
ghost artifact, not an interlacing violation (and the unfiltered `M`-count is a
non-normal shadow with no interlacing bound, ghost-fragile at `O(1)`); the
residual open piece is WHERE the eigenvalues sit inside that count (the
density/height-dependence = M4), cleanly isolated from the now-cheap count.

## The two operators (WHERE each perturbation enters)

The whole of question (a) turns on keeping two matrices apart.

| matrix | type | perturbation | interlacing |
|---|---|---|---|
| `Q` (Weil form) | Hermitian, `D x D` | zeta = entire + `P`, `rank(P) = 2` | WEYL, rigorous: count moves `<= 2` |
| `M = D_log - (D_log xi) delta^T` | non-Hermitian | rank-1 from the lattice `D_log = diag(phi n)`; pole on/off and zeta/D-H each change only `xi` | rank-1, but non-normal + ghosts: count moves measured, not `<= 1` |

Measured ranks (`lam = 3.0`, `N = 20`): `rank(P) = 2` (svals `[1, 0.07, 0, ..]`);
`rank(M_on - M_off) = 1`; `rank(M_zeta - M_DH) = 1`. The naive worry "a shift
of 4 exceeds rank 2" applies the rank-2 Weyl bound of `Q` to a count of `M`'s
eigenvalues: different objects.

## T1 (a): the pole-term reconciliation

The rigorous backbone (RIGOROUS, verifier-ready): for all thresholds `t`,
`|#{eig(Q_on) < t} - #{eig(Q_off) < t}| <= rank(P) = 2`. Measured max move
over a 400-point grid: **1** (well within 2). Weyl on the Hermitian Weil form.

The `n_win` decomposition (pole-off = lattice; pole = displacement + ghost),
full run `N = 20`, and the truncated-regime `sqrt13` anchor:

| lam | floor(T/phi) | Zoff n_win | Zon unfiltered | Zon filtered | displ (off->uf) | ghost (uf->filt) |
|---|---|---|---|---|---|---|
| 2.2 | 7 | 7 | 5 | 3 | +2 (<= 2) | +2 |
| 2.6 | 12 | 12 | 11 | 11 | +1 (<= 2) | +0 |
| 3.0 | 19 | 19 | 17 | 13 | +2 (<= 2) | +4 |
| sqrt13, N=24 | 33 (= N*) | 24 | 22 | 22 | +2 (<= 2) | +0 |

Two SEPARATE mechanisms, neither a rank violation:

1. **Eigenvalue displacement (a non-normal shadow, NOT a rigorous bound).** The
   UNFILTERED window count (eigenvalues with `1 < re < T`, `|Im|` ignored) moves
   `Zoff -> Zon_uf` by `2, 1, 2, 2` on these four base cells (`<= rank(P) = 2`),
   suggestively tracking the rank-2 pole. But this is the shadow of the Weyl-
   on-`Q` bound in the NON-normal `M`, NOT a theorem: ADVERSARY (2026-07-12)
   found it reads `+3` at `lam=sqrt13, N=34` (ghost-fragile; a second build
   reads `+2`). The rigorous statement is Weyl-on-`Q` only.
2. **Reality-breaking (the ghost artifact, NOT interlacing).** The pole is
   only approximately G-self-adjoint (e1k caveat 2), so it throws `O(1)`
   eigenvalues off the real axis; in-window ghosts (`gin = 2, 0, 4`) are
   removed by the `|Im|` filter, dropping the FILTERED `n_win` further
   (`5->3`, `17->13`). A numerical non-normality effect (e1l STEP 5),
   dps-dependent, with NO interlacing content.

**Reconciliation of "29 vs 33".** The tasking's "29 vs 33 without pole" is:
`33 = floor(T/phi) = N*` (the geometric lattice ceiling, hit EXACTLY by
zeta-off and D-H), and `29 = 33 - rank(P) - ghost` (the pole's `<= 2`
displacement plus the `O(1)` ghost). The "33 without pole" was `N*` (a budget
quantity), NOT a genuine pole-off `n_win` moving by 4. The interlacing-
governed count (the unfiltered `M` count, empirically `<= rank(P) = 2`; its
rigorous parent is the Weyl-on-`Q` bound, also `<= rank(P)`) moves by `<= 2`;
no rank bookkeeping is violated. `pole_interlacing_consistent = YES`.

## T2: the rank-1 secular structure (and an honest failure)

`det(M - z) = det(D_log - z)(1 - sum_k r_k/(phi k - z))`,
`r_k = L^{-1/2} phi k (xi_n)_k`. Eigenvalues of `M` = zeros of
`s(z) = 1 - sum r_k/(phi k - z)`. Verified: `max |s(eig)|` over the first
physical eigenvalues `= O(1e-13)`, so the secular representation is exact.

HONEST FINDING: the residues `r_k` are NOT sign-definite even for `k >= 1`
(the even ground state of the INDEFINITE truncated Weil form, razor-thin
margin, has many sign changes; measured `>= 5` sign changes for `n = 1..N`).
So the clean "one eigenvalue per lattice gap" interlacing (which needs all
`r_k > 0`, giving `s' < 0` monotone between poles) DOES NOT hold. The count
pinning rests instead on the rank-1 displacement + reality + the measured
exactness below, NOT on a monotone secular equation. Stated up front so it is
not mistaken for a clean interlacing theorem.

What DOES hold (measured every cell): the pole-free `n_win` equals the
truncated lattice count `min(N, floor(T/phi))` EXACTLY.

## T3 (b, N-direction): compression interlacing proves the e1l plateau

Increasing `N` at fixed `lambda`: `D_log^(N)` is the principal compression of
`D_log^(N+1)` (add one `+`mode at `phi(N+1)`, one `-`mode). Cauchy
interlacing: a bordered row+column moves any interior window count by `<= 2`,
and for the DIAGONAL the interior count in `(1, T)` with `T < phi(N+1)` is
EXACTLY stable (the new modes sit outside the window). This PROVES the e1l
plateau structurally. Measured (`lam = 2.2`, `N* = 7`):

| N | D | min(N, N*) | DH n_win | Zoff n_win |
|---|---|---|---|---|
| 4 | 9 | 4 | 4 | 4 |
| 6 | 13 | 6 | 6 | 6 |
| 8 | 17 | 7 | 7 | 7 |
| 12 | 25 | 7 | 7 | 7 |
| 20 | 41 | 7 | 7 | 7 |

`n_win = min(N, floor(T/phi))` EXACTLY; exact stability past `N = 8 = N*`. The
e1l "plateaus at an N-independent value" is now a Cauchy-interlacing theorem,
not just an observation.

## T4 (b, lambda-direction): NOT low-rank, but count = geometry

Stepping `lambda` at fixed `N` changes `phi = pi/log lambda` (lattice
SPACING) AND `kmax = floor(lambda^2)` (number of prime terms) AND `L`: the
matrix is NOT a compression or low-rank update of the previous `lambda`, so
plain/compression interlacing does NOT bound the step. What IS true: the
pole-free count `= floor(T/phi)` up to `O(1)` (measured `7, 12, 19` EXACTLY at
`lam = 2.2, 2.6, 3.0`; ADVERSARY 2026-07-12: a genuine 1-2 deviation appears at
`lam` in {3.3-4.5}, so the exact match is a small-lambda phenomenon). So the
step-to-step move of `n_win` TRACKS the geometric lattice count
`floor(2 lambda^2 log lambda)` up to `O(1)`, a pure-geometry quantity, not an
interlacing-bounded small move. "Family-stable for free" means "the count IS the
geometry up to `O(1)`", not "the count barely moves".
`lambda_step_interlacing = SPLIT` (N-step compression-proven; lambda-
step not interlacing-governed but geometry-pinned).

## T5 (d): the D-H twin calibration + Beurling scope

`M_zeta - M_DH = rank 1` (same `D_log`, only `xi` differs). D-H has no pole
term, so it IS the pole-free "entire part" for the count. Measured:

| lam | floor | DH n_win | \|Zon_filt - DH\| |
|---|---|---|---|
| 2.2 | 7 | 7 | 4 |
| 2.6 | 12 | 12 | 1 |
| 3.0 | 19 | 19 | 6 |

D-H `n_win = floor(T/phi)` EXACTLY at the tested `lam <= 3` (and `lam = 5`).
**ADVERSARY (2026-07-12): this is NOT universal.** D-H undercounts the lattice
by 1-2 (ghost-free / genuine: `unfiltered = filtered = lattice - 2`) at `lam` in
{3.3, 3.6, 4.0, 4.5} (measured DH_f = 19/19/19/18 vs floor 26/33/44/60 at N=20,
and 31 vs floor 33 at `lam=sqrt13, N=34-36` plateau). At `lam = sqrt13` it is
zeta-OFF (33 = exact lattice) that is clean, NOT D-H (31), so the "D-H is THE
clean ghost-free entire-part count" reading is backwards at larger lambda; the
robust pole-free lattice anchor is zeta-OFF, and both agree with the lattice
only up to an `O(1)` genuine deviation. With that correction, zeta
`= D-H-structure + pole (<= 2 on Q) + ghost`, and the
count law does NOT discriminate zeta from D-H (the twins agree up to the
pole/ghost `O(1)`): identical structure, matching #158 information-free
finiteness and the e1l blind verdict. `dh_twin_consistent = YES`.

**Beurling scope.** NOT buildable as an operator here: e1k has no Beurling
`D_log` (the `_shared/beurling.py` control is comb-side only). The count
comparison is form-side; the Beurling fake enters only at the comb/density
level, which this probe does not pair. Recorded as scope, NOT forced (the
same operator-absence limitation as e1n/e1o).

## T6 (c): the K1 reading and the W6 budget split

`k1_clean = YES`. Every observable is a matrix eigenvalue count or lattice
geometry (`phi`, `T`, `N`). No zero list, zero scan, or zero-location datum is
consumed. Guards on `mp.zetazero` and the D-H scanner installed, never
tripped; the input ledger is printed (all comb / geometry).

**THE W6 BUDGET SPLIT (the conceptual deliverable).** The W6 "independently
computable pole budget" clause splits into:

- **COUNT half (DISCHARGED, interlacing-cheap).** The number of eigenvalues
  below the two-meter edge `= floor(T/phi) = geometry` up to `O(1)`: exactly at
  the tested `lam <= 3` (D-H and zeta-off), and up to a genuine `O(1)` (1-2)
  deviation at larger lambda (ADVERSARY 2026-07-12). The RIGOROUS structure-
  cheap content is Weyl-on-`Q` (`<= rank(P) = 2`, robustly held everywhere),
  NOT the exact-lattice match; the exact match is a small-lambda phenomenon.
  Proven zeta-input-free (the pole-free anchor is zeta-off, exact where tested).
  This is #154's "the count is already nearly independent", read as `up to O(1)`.
- **LOCATION half (REMAINS).** WHERE the eigenvalues sit inside the count (the
  density profile, RvM `log`-growth vs flat, reality in the limit, the
  critical line) is untouched by any interlacing bound. This is M4 / the
  uniformity joint. Interlacing gives "how many", never "where".

`count_half_discharged = YES`.

## Verdict fields

| field | verdict |
|---|---|
| `pole_interlacing_consistent` | YES (rigorous backbone), with the empirical `M`-count claim DEMOTED (ADVERSARY 2026-07-12). `rank(P) = 2` (measured, sv2/s0 = 0.09, genuine); `rank(M_on - M_off) = rank(M_zeta - M_DH) = 1`. RIGOROUS: Weyl on `Q` gives `|#eig(Q_on)<t - #eig(Q_off)<t| <= 2` (measured max move 1, robust at every extension cell). The `n_win` "pull" decomposes into eigenvalue displacement (unfiltered) + ghost artifact (filtered out). CAVEAT: the unfiltered `M` displacement is a NON-normal shadow with NO interlacing bound (the `M` perturbation is rank 1); it measured `+2,+1,+2,+2` on the base cells but reads `+3` at `lam=sqrt13, N=34` under this probe's own machinery (ghost-fragile: a second build reads `+2`). So "displacement `<= rank(P)`" is NOT a bound; only Weyl-on-`Q` is. The tasking's "29 vs 33" reconciliation (`29 = 33 - rank(P) - ghost`, reproduced at dps=25: Zon = 29 filt / 31 unfilt / 2 ghost) holds via Weyl-on-`Q`; the "33" is `N*`, a budget quantity, not a genuine pole-off count |
| `lambda_step_interlacing` | SPLIT. N-direction IS a compression: Cauchy interlacing on `D_log` is EXACT (verified `||D_log^(N) - central-block(D_log^(N+1))|| = 0`) and proves the e1l plateau (`n_win = min(N, floor(T/phi))` at the tested small-lambda cells). lambda-direction is NOT low-rank (phi AND kmax AND L change), so plain interlacing does not bound the step; the pole-free count tracks `floor(T/phi)` (measured `7/12/19` exactly at `lam <= 3`), so the count is the geometric lattice count up to `O(1)`. ADVERSARY: the exact match is a small-lambda phenomenon; at `lam` in {3.3-4.5} the pole-free count (D-H, and Zoff at `N=32`) deviates by a genuine `O(1)` (1-2), so read "count = geometry" as "up to `O(1)`" |
| `count_half_discharged` | YES up to `O(1)`. RIGOROUS structure-cheap content: Weyl-on-`Q` (`<= rank(P) = 2`, robust everywhere). The pole-free count = `floor(T/phi)` = geometry EXACTLY at the tested `lam <= 3` (zeta-off and D-H), and up to a genuine `O(1)` (1-2) deviation at `lam` in {3.3-4.5} (ADVERSARY 2026-07-12). Zeta-input-free (the exact pole-free anchor is zeta-off). REMAINS: the location/height-dependence (density profile, RvM growth, reality in the limit, critical line) = M4 / the uniformity joint, untouched by any interlacing bound |
| `dh_twin_consistent` | YES (structure), with the D-H exactness claim CORRECTED (ADVERSARY 2026-07-12). `M_zeta - M_DH = rank 1`; the twins are `O(1)`-blind in the count (#158). CORRECTION: D-H is NOT the exact lattice count "at every lambda": it undercounts by 1-2 (ghost-free / genuine) at `lam` in {3.3, 3.6, 4.0, 4.5}, and at `lam = sqrt13` it is zeta-OFF (33 = exact), NOT D-H (31), that hits the lattice, so "D-H is THE clean ghost-free entire part" is backwards there. Both pole-free operators agree with the lattice only up to a genuine `O(1)`. Beurling NOT buildable as an operator here (comb-side only; scope recorded, not forced) |
| `k1_clean` | YES. Only matrix eigenvalue counts and lattice geometry (phi, T, N) consumed; no zero list / scan / location; guards installed and never tripped; input ledger printed |
| `frontier_delta` | The COUNT half of the W6 pole-budget goes STRUCTURE-CHEAP up to `O(1)` (rigorously via Weyl-`<=2` on `Q` and the exact Cauchy-compression on `D_log`; the pole-free `floor(T/phi)` match is exact at `lam <= 3` and up to a genuine `O(1)` at larger lambda, ADVERSARY 2026-07-12). What moved: "count" is removed from the open list of #154's W6 upgrade in the "cheap up to `O(1)`" sense. What did NOT move: the residual is pinned to WHERE the eigenvalues sit (density / height-dependence = the uniformity/M4 joint), exactly #154's "the gap is the height-dependence, not the count". The frontier is UNMOVED on M4; the count clause is now cheap |

## Tiered claims

**PROVEN (classical linear algebra, instantiated here):**
1. `rank(P) <= 2`: `P = 2 Re(conj(a) a^T)` is a sum of two rank-1 Hermitian
   matrices (measured rank exactly 2).
2. Weyl interlacing on `Q`: `A' = A + P`, `rank(P) = r` implies
   `|N_{A'}(t) - N_A(t)| <= r` for all `t` (Mathlib-reachable; the rigorous
   backbone of question (a)).
3. Cauchy compression interlacing on `D_log`: adding modes `+-phi(N+1)` outside
   the window `(1, T)` leaves the interior count exactly invariant (the e1l
   plateau, structurally).
4. The truncated lattice count `min(N, floor(T/phi))` is pure geometry (phi, T,
   N), independent of the coefficient stream.
5. The rank-1 secular representation `det(M - z) = det(D_log - z) s(z)`
   (matrix determinant lemma), verified to `O(1e-13)`.

**NUMERICAL (measured on the faithful e1k build, dps=25):**
6. `rank(M_on - M_off) = rank(M_zeta - M_DH) = 1` (robust across every cell).
7. Weyl max move on `Q` = 1 (`<= rank(P) = 2`), robust at every extension cell
   (this is the only RIGOROUS count-cheap statement).
8. The `n_win` decomposition: displacement `+2/+1/+2/+2` on the base cells, but
   `+3` at `lam=sqrt13, N=34` (ADVERSARY 2026-07-12, ghost-fragile: the
   unfiltered `M` count is a non-normal shadow with NO interlacing bound; a
   second build reads `+2`) + ghost `+2/0/+4` (filtered, non-interlacing).
9. Pole-free `n_win = min(N, floor(T/phi))` EXACTLY only at the tested
   `lam <= 3` cells; at `lam` in {3.3-4.5} D-H deviates by 1-2 (genuine,
   ghost-free) and Zoff deviates -1 at `lam=3.3, N=32` (ADVERSARY 2026-07-12).
10. The N-plateau: `4,6,7,7,7,7,7` at `lam=2.2`, exact past `N* = 8`.
11. The lambda-family at `lam <= 3`: pole-free count `7/12/19` = `floor(T/phi)`
    (deviation 0); at larger lambda the match is only up to a genuine `O(1)`.
12. The twins `O(1)`-blind: `|Zon_filt - DH| = 4/1/6`.

**STRUCTURAL / CONJECTURE:**
13. The residue sign-indefiniteness kills clean per-gap interlacing; the count
    pinning is empirical (rank-1 displacement + reality), not a proven `<= 1`
    for the non-Hermitian `M`.
14. The W6 budget split (count cheap / location = M4) is the conceptual
    reading, not a theorem about the limit.

## Named residual

The count half of the W6 pole-budget is now measured structure-cheap up to
`O(1)`: the eigenvalue count below the two-meter edge is the geometric lattice
count `floor(T/phi)` up to a rank-`<=2` (Weyl-on-`Q`, rigorous) plus a genuine
`O(1)` deviation of the pole-free operators themselves (exact at `lam <= 3`,
1-2 off at larger lambda; ADVERSARY 2026-07-12). What survives is precisely the
location half: the
height-dependence of WHERE the eigenvalues sit, which is the uniform det-class
limit = M4. This converts #154's item 2 from a spec line into a measured,
control-calibrated split, with the residual cleanly isolated as M4.

## Overclaim guard (what this does NOT show)

- It does **not** produce a W6 hit or move M4. Only the count clause of the
  budget is discharged; the location/uniformity clause (the actual wall) is
  untouched.
- The `<= 1` in #154's wording is NOT literally true for the non-Hermitian
  `M`: the filtered count moves by up to 4-6 (ghost-inflated), and the
  unfiltered count moves by `<= 2 = rank(P)` on the base cells but reads `+3` at
  `lam=sqrt13, N=34` (ADVERSARY 2026-07-12). Even `<= 2` is NOT a bound for the
  `M`-count: the `M` perturbation is rank 1, `M` is non-normal, so there is NO
  interlacing theorem for it, and the reading is ghost-fragile. The RIGOROUS
  `<=` bound lives ONLY on the Hermitian `Q` (Weyl, `<= rank(P) = 2`, robust).
- "Pole-free `n_win = floor(T/phi)` EXACTLY at every lambda" is FALSE (ADVERSARY
  2026-07-12): D-H undercounts by 1-2 (genuine, ghost-free) at `lam` in
  {3.3-4.5}, and Zoff by -1 at `lam=3.3, N=32`. Exactness is a `lam <= 3`
  phenomenon; elsewhere the pole-free count = lattice only up to `O(1)`.
- The clean per-gap interlacing does NOT hold (residues sign-indefinite); the
  count pinning is empirical + reality-dependent, not a monotone secular proof.
- All integer counts are `O(1)`-dps-fragile (e1l STEP 5). Reported at dps=25;
  the ghost mechanism is exactly the dps-dependent part.
- It does **not** discriminate zeta from D-H: the count law is D-H-blind
  (twins `O(1)`-agree), matching #158.
- Beurling is not tested (no operator here); the lattice clause of #152 is not
  engaged by a count-only probe.

## Verification targets (for VERIFIER)

1. **Weyl interlacing (the backbone).** For Hermitian `A` and `A' = A + P`
   with `rank(P) = r`: `|#{eig(A') < t} - #{eig(A) < t}| <= r` for all `t`.
   (Mathlib has `Matrix.IsHermitian` spectral theory; the min-max / rank
   inequality is the target. This is the rigorous content of question (a).)
2. **`rank(P) <= 2`.** `P = c (conj(a) a^T + a conj(a)^T)` is a sum of two
   rank-1 matrices, hence rank `<= 2`. (Definition-level.)
3. **Compression interlacing / the plateau.** For a real diagonal `D` and its
   principal submatrix (compression) `D'` obtained by deleting rows/cols
   indexed outside `(1, T)/phi`: the count of eigenvalues in `(1, T)` is equal.
   (The e1l plateau as a Cauchy-interlacing corollary; Mathlib
   `Matrix.vandermonde`/eigenvalue infrastructure.)
4. **Matrix determinant lemma.** `det(D - z - u v^T) = det(D - z)(1 - v^T (D -
   z)^{-1} u)`. (Standard; anchors the secular representation.)
5. **The truncated lattice count.** `#{n : 1 <= n <= N, 1 < phi n < T} =
   min(N, floor(T/phi))` for `phi > 1` (the geometric count; pure arithmetic).

## Adversarial test cases (for ADVERSARY)

1. **Push the displacement bound.** RUN (ADVERSARY 2026-07-12), `lam` in
   {3.3, 3.6, 4.0, 4.5, 5.0} and `N` = 20, plus `lam <= 3.6` pushed past `N*`.
   OUTCOME: the unfiltered `M` move reads `+3` at `lam=sqrt13, N=34` (`Zoff_uf`
   33 -> `Zon_uf` 30, ghost 0) under the probe's own `cell()`, EXCEEDING
   `rank(P) = 2`. A second build (make_streams(15) vs (40)) reads `+2`
   (`Zon_uf` 31, ghost 2): the excursion is ghost-fragile. Since `M` is
   non-normal and rank-1-perturbed, there is no interlacing bound to break;
   the finding is reported and the "unfiltered `<= rank(P)`" claim is demoted
   to "only Weyl-on-`Q` is rigorous". Weyl-on-`Q` stayed `<= 2` at every cell.
2. **The ghost autopsy.** RUN (partial): two dps=25 builds of `lam=sqrt13` give
   DIFFERENT zeta-ON ghost counts (0 vs 2) and hence different unfiltered/
   filtered `n_win`, confirming the ghost count is build/dps-fragile (as the
   e1l STEP 5 caveat states). The a-priori criterion (`IMTOL = 1e-4`, fixed,
   not tuned per cell) is sound; the fragility is in WHERE the ghosts land.
3. **Residue-sign stress.** Not re-run; the sign-indefiniteness (5 sign changes
   at `lam=sqrt13, N=20`) reproduced in the full run.
4. **The lattice-count exactness.** RUN (ADVERSARY 2026-07-12), BROKEN. D-H
   deviates from `floor(T/phi)` by -1 to -2 (GHOST-FREE / genuine:
   `unfiltered = filtered = lattice - 2`) at `lam` in {3.3, 3.6, 4.0, 4.5},
   including the PLATEAU cell `lam=sqrt13, N=34-36` (D-H 31 vs floor 33). Zoff
   deviates -1 at `lam=3.3, N=32`. So "pole-free = floor EXACTLY at every
   lambda" is FALSE; it is a `lam <= 3` phenomenon. Notably `Zoff` (not D-H) is
   the robust exact-lattice anchor at `lam=sqrt13`.
5. **The Weyl vs M gap.** CONFIRMED (case 1): the `M` unfiltered move (`+3`)
   exceeds the `Q` Weyl move (`1`) at `lam=sqrt13, N=34`; the `M` count is
   bounded via `Q` only up to the (unbounded, ghost-fragile) non-normal slack,
   exactly as this case anticipated. `Q` is verified exactly Hermitian
   (`||Q-Q^H|| = 0`), so the Weyl backbone is sound.

## Reproduce

```
python3 -m experiments.spectral.e1s_rank_one_interlacing          # full (~3 min)
python3 -m experiments.spectral.e1s_rank_one_interlacing --quick   # reduced grids
```
Outputs `e1s_rank_one_interlacing.npz` (rank(P), Weyl max, the `n_win`
decomposition, secular residual, N-step and lambda-step tables, twin table).
`--quick` does NOT write the npz (the tracked artifact is the full run's). No
cache is written; the e1k harness is imported read-only (comb streams and the
`build_float`/`operator_spectrum` functions; no zero lists).

## ADVERSARY reconciliation (2026-07-30): e1s vs #165/e1p, resolved -- NO CONFLICT

**VERDICT: NO CONFLICT.** The twisted-inner-product caveat in #165/e1p bites
only the non-normal operator-level object (e1p's `D = D_0+P_1`, this
dossier's `M`); it does not touch, and neither dossier ever claimed it
touches, the Hermitian form-level `Q`. Read past their one-line headlines,
#165/e1p and this dossier make the *identical* two-object split internally
(e1p: Q1 operator-level "measurement, not theorem" vs Q3 form-level
"provable, verified... hypotheses actually met"; here: `M` "non-normal
shadow, NO interlacing bound" vs `Q` "RIGOROUS, Weyl, robust"), and they
agree on every disputed number: the shift-3 anomaly both flag at
`lam=sqrt(13)` is, in BOTH dossiers, an operator-level (`D`/`M`) reading
(e1p Q3: `D_noPole->D_full` shift = 3 at `N=24`, graded "no theorem backing
a bound there"; this dossier's ADVERSARY entry: unfiltered `M` move = +3 at
`N=34`, graded "ghost-fragile... NOT a bound"), while the Hermitian-`Q`
Weyl bound stays `<=2` at every cell tested by either dossier, including
sqrt(13) (e1p Q3 form-level max shift 1/2; this dossier's own ADVERSARY
push case 1: "Weyl-on-`Q` stayed `<=2` at every cell"). Verified directly
against the shared source (`e1k_dh_dlog_testbed.py`): `Q` is forced
Hermitian by an explicit `0.5*(Q+Q.conj().T)` symmetrization w.r.t. the
STANDARD inner product and diagonalized by `np.linalg.eigh` (lines
244-246); the pole term, named `P` in the shared source (line 220,
`P = 2.0*np.real(np.outer(np.conj(av), av))` with `av_n = Vhat(n,i/2)`)
and relabelled `P_pole` in e1p, equals
`2(pp^T+qq^T)` and is manifestly PSD, rank `<=2`,
machine-exact -- the classical Weyl/Cauchy hypotheses are met by
construction, not by luck. `M`/`D`, by contrast, is a rank-1 update
`-w u^T` for two DIFFERENT vectors (not `w w^T`), self-adjoint only w.r.t.
the twisted form `G = Q - eps*I` per `operator_spectrum`'s own docstring,
so the ambient-inner-product hypothesis the counting theorem needs is not
manifestly met there -- exactly, and only, the twisted-inner-product
caveat's scope.

**Downstream: nothing moves.** #165's retirement of the #154 ledger and its
"the rank<=2 pole block is the ONE genuine Weyl/Cauchy instance,
input-faithful, RH-blind" claim is CONFIRMED (doubly-independently
verified: two separate implementations of the counting/shift harness, same
conclusion), not contradicted. This dossier's own Weyl-on-`Q` rigor claim
also stands unchanged. The frontier stays UNMOVED: the count-half of the W6
budget was already graded structure-cheap by both dossiers; the
location-half (= M4) was never touched by either. This is a cross-reference
resolution of a wording collision, not a new result or a correction to any
prior verdict. Full reasoning, matching-number tables, and adversarial
stress tests attempting to break this reading:
[`_e1s_interlacing_reconciliation.md`](_e1s_interlacing_reconciliation.md).

