# E1P: the Sonin projector family, the last untested corner of the S4/R1 coordinate

> Companion to `e1r_sonin_projector.py` / `.npz`. Executes the ONE subspace
> family the e1o adversary round could not build (no full eigenbasis in any
> cache): the carrier's OWN spectral data. Four channels of it (the Weil-form
> energy eigenbasis, the D_log operator eigenbasis, the Sonin-space projection,
> and the E-map pullback) are tested for the S4 mechanism: a lambda-uniform,
> well-conditioned rank collapse of the log-prime evaluation matrix that is
> present for the true prime lattice and ABSENT for perturbed logs. Reuses e1k's
> archimedean quadrature (build_float) and the `_shared/beurling.py` control; no
> new operator physics. It proves nothing about RH. All numbers from the default
> full run (10/10 self-tests, ~40 s; `--quick` reduced grid, 10/10, does NOT
> save the npz). Builder derivations: `scratchpad/sonin_projector/01`
> (gitignored). Arc provenance: LEARNINGS #162 / e1o Q4 forcing question, the
> Sonin-projector item handed to BUILDER.

> **BANNER (read before quoting any number).** Three headline facts.
> (1) THE CARRIER'S OWN EIGENBASIS DOES NOT COLLAPSE. Because the Weil form Q is
> Hermitian its eigenbasis is UNITARY, so evaluation on the full eigenbasis is
> unitarily equivalent to the standard basis (identical singular values, verified
> to 1e-15): the eigenbasis can only matter through SELECTION or through the
> non-orthogonal D_log operator. Neither collapses: the leading-J low-energy
> subspace is FULL PRICE at {log p} in all 12 (lambda, J) cells (rank = M
> everywhere), and the non-orthogonal D_log operator eigenbasis is full price too.
> (2) THE ONE RANK DROP IS A WINDOW MIRAGE. The Sonin projection (low-concentration
> eigenspace of the central-window prolate) does drop rank, but the drop TRACKS the
> number of comb points that land inside the Sonin-vanishing window W (drop 4 =
> n_inW 4 at lam=6; drop <= n_inW in general; min_cos ~ 1e-13), it PERSISTS under
> perturbed logs (fails the S4 lattice clause), and the comb restricted to points
> OUTSIDE W is full rank. It is a spatial-support artifact carrying zero counting
> information,
> not a commensurability mechanism. (3) THE INCOMMENSURABILITY READING EXTENDS TO
> THE EIGENBASIS. Every apparent drop survives perturbation; the E-map shift-sum
> proxy is full price; D-H (dense sign-changing comb) and the Beurling fake are
> both full price. The S4 spec is answered NEGATIVE and the last corner of the
> coordinate closes FOR EVERY BUILDABLE FAMILY (the faithful metaplectic self-dual
> Sonin projector of arXiv:2310.18423 remains the sole unbuilt variant, tiered
> claim 12): no lattice-sourced cheap multiplicity lives in the carrier's own
> buildable spectral data. Frontier: UNMOVED; the corner is now measured, not just
> untested.

## One-line result

The carrier's own spectral data supplies no S4 mechanism: the Hermitian
eigenbasis is unitarily equivalent to the standard basis (so full-eigenbasis
collapse is impossible in principle), the leading-J low-energy selection and the
non-orthogonal D_log eigenbasis are full price at {log p}, the Sonin projection's
only rank drop is a spatial-window mirage that fails the perturbed-log control,
and the E-map/D-H/Beurling screens all read full price, so the last untested
corner of the S4/R1 coordinate closes negative with the lattice clause visible.

## The load-bearing structural fact (stated first, so no number is over-read)

Q is Hermitian, so its eigenbasis V is UNITARY. The M comb evaluation functionals
are the columns of a D x M matrix C (g_p[n] = exp(-i phi n u_p), so f_v(u_p) =
<g_p, v>). The cost of forcing an eigen-subspace E_J to vanish at all M comb
points = rank of the cross-Gram E_J^H C; collapse = rank < M = a comb functional
escaping E_J; min singular value = cos(largest principal angle), collapse-adjacent
iff near 0. Because V is unitary, evaluation on the FULL eigenbasis has the same
singular values as the raw comb-Vandermonde (self-test: maxdiff 3.6e-15), so the
full eigenbasis CANNOT manufacture collapse. Only three things can: (a) SELECTION
of the leading-J low-energy subspace (T1), (b) the non-orthogonal D_log operator
eigenbasis (T2, the one basis not unitarily equivalent to the standard basis),
(c) the Sonin projection (T2) or an E-map reweighting (T3). All are measured
below against a random-orthobasis null and the perturbed-log control.

## T1: eigenbasis collapse (eigenbasis_collapse = NONE)

The leading-J eigenvectors of the Weil form Q (energy ordered, K1-clean: the
ordering is variational, not by any zero-approximating eigenvalue), evaluated at
{log q : q prime power <= lambda^2}. Result: FULL PRICE (rank = M) in all 12
cells, lambda in {3, sqrt13, 5, 6}, J in {M, ~2M, D}.

| lambda | D | M | J=M rank/M | min_cos (true) | null p5 / med | pert-op rank/M |
|---|---|---|---|---|---|---|
| 3.0 | 33 | 7 | 7/7 | 0.007 | 0.023 / 0.062 | 7/7 |
| sqrt13 | 33 | 8 | 8/8 | 0.168 | 0.016 / 0.059 | 8/8 |
| 5.0 | 41 | 14 | 14/14 | 0.002 | 0.010 / 0.042 | 14/14 |
| 6.0 | 49 | 18 | 18/18 | 0.029 | 0.011 / 0.034 | 18/18 |

The leading-J min_cos is small (the generic small-angle effect for a J=M subspace
against an M-dim comb space in D dimensions) but the RANK is always exactly M:
every comb functional is resolved. The mild alignment (min_cos at/above the null
in several cells) has the WRONG SIGN for S4: cheap multiplicity needs a comb
direction ESCAPING (rank < M, min_cos -> 0), whereas the low-energy space RESOLVES
the comb (the prime term T(n) is a shift CORRELATION, not a vanishing). The
perturbed-OPERATOR control (teeth at log n + iid eps, evaluated at its own
perturbed comb) gives identical full rank and comparable min_cos: the alignment is
generic to 'an operator built from a comb resolves that comb', NOT lattice-specific.

## T2: Sonin projection (sonin_alignment = window-artifact only) + D_log operator

The Sonin space in CCM is the negative/low eigenspace of the prolate operator
(functions vanishing near the self-dual radius rho = 1, i.e. u = 0). The finite
proxy: the low-concentration eigenspace of the central-window prolate B_W,
W = [-a, a] with a = (1/2) log 2 (the archimedean cutoff [2^{-1/2}, 2^{1/2}]).

**The one rank drop in the whole probe, and why it is a mirage.** At J = M the
Sonin subspace drops rank by exactly the number of comb points inside W:

| lambda | M | comb pts in W | Sonin drop (true) | drop (perturbed logs) | out-of-W comb full rank | min_cos |
|---|---|---|---|---|---|---|
| 3.0 | 7 | 3 | 2 | 2 | yes | 9.8e-11 |
| sqrt13 | 8 | 1 | 1 | 1 | yes | 9.9e-11 |
| 5.0 | 14 | 3 | 3 | 3 | yes | 3.5e-12 |
| 6.0 | 18 | 4 | 4 | 3 | yes | 2.7e-13 |

The drop TRACKS #comb-in-W (self-test asserts 1 <= drop <= n_inW; the drop equals
n_inW when the in-window points are deep enough in W, and is one less when an
in-window point sits near the window edge and is only partially suppressed at
finite N, e.g. lam=3 log7 = 1.946 just inside the edge at 1.85). Sonin functions
vanish inside W, so any comb point landing there (near u=0 or the wrap at u=L,
where the largest prime powers sit) gives a vanishing evaluation. This is a
spatial-support artifact,
NOT a lattice/commensurability mechanism, proven three ways: (i) the drop equals
the geometric in-window count, not anything prime-specific; (ii) it PERSISTS under
perturbed logs (drop_pert = drop_true; a lattice-sourced collapse would be restored
to full rank by perturbation); (iii) the comb restricted to points OUTSIDE W is
FULL RANK. It conveys zero counting information (vanishing where the subspace is
already ~0) and fails the S4 lattice clause. At J = 2M the window artifact vanishes
too (the larger Sonin space spans the in-window directions).

**The D_log operator eigenbasis (non-orthogonal, the one basis not unitarily
equivalent).** Energy-ordered leading-M eigenvectors of M = Dlog - |Dlog xi><delta|
(K1-clean: ordered by Weil energy, the eigenVALUES = zeros of xihat are never used
to select), orthonormalized. FULL PRICE (rank = M) in every cell (min_cos
0.001-0.539, above the null): the non-normal carrier basis behaves exactly like the
Hermitian one. No collapse.

## T3: the E-map channel (emap_channel = shift-sum proxy full-price; weight UNBUILDABLE)

E(f)(x) = x^{1/2} sum_{n>0} f(nx) is the lattice-consuming organ (#153). In log
coordinates u = log x, f(nx) -> f(u + log n): a sum of multiplicative shifts. On a
mode exp(i phi m u) the shift-sum part acts as a DIAGONAL multiplier by
S_m = sum_{n=1}^{K} n^{i phi m} (a partial zeta value on the imaginary axis,
K = lambda^2). This is the one channel where a positive result would be
lattice-SOURCED (S_m is built from the integer lattice 1..K). Measured: reweighting
the leading-J eigenvectors by S (|S| in [0.5, K]) gives FULL PRICE (rank = M) at
{log p} in all four cells, drop under perturbed logs = 0: no lattice-sourced
collapse. HONEST SCOPE: the aperiodic weight x^{1/2} = e^{u/2} breaks periodicity
on the compact log-circle; the faithful E lives on the non-compact line R+ and is
only PARTIALLY buildable here. The weight channel is recorded UNBUILDABLE (per the
e1o discipline: honest UNBUILDABLE beats a fake test); the shift-sum channel, which
IS the lattice-carrying half, is tested and negative. S_0 = K exactly (self-test).

## T4: disciplines

- **D-H calibration (dh_calibration = full price).** The D-H operator's eigenbasis
  at its OWN dense sign-changing comb {log n : 2 <= n <= lambda^2}: FULL PRICE
  (rank = M) across all lambda (min_cos 0.001-0.208). Calibration: 'operator knows
  its comb' = full price even when the comb is not the prime lattice and is
  sign-changing. Consistent with the D-H discipline (the finite machine is
  D-H-blind, #158). The dense comb can exceed the trig dimension D; the test caps
  the eval comb at D-6 points so a DIMENSION shortfall (Vandermonde with more
  points than frequencies) is not miscounted as an eigenbasis collapse.
- **Beurling screen (beurling_screen = full price).** An operator built with the
  repo fake's comb {k log b_p} (b_p = p exp(eps_p), eps=0.25, seed 149),
  evaluated at {k log b_p}: FULL PRICE in every cell. There is no zeta-only
  collapse for the fake to lack; the system-generic full-price is consistent, and
  any future positive S4 finding must (by the DMV kill) be ABSENT here.
- **K1 (k1_clean = TRUE).** Source scan clean (np.zeros swapped to np.full to
  avoid the '.zeros(' token; docstring reworded to avoid 'zetazero'); runtime
  guards on the mpmath zero routine and the D-H scanner installed, never tripped;
  input ledger printed. Eigenvalues come OUT of the operator; no zero list, zero
  scan, or zero-location datum enters. Energy ordering is manifestly
  zero-independent; the D_log operator's eigenvectors are computed from the
  operator, not from any external zero data.

## Verdict fields

| field | verdict |
|---|---|
| `eigenbasis_collapse` | NONE. Full eigenbasis unitarily equivalent to the standard basis (sv match to 3.6e-15, so collapse impossible in principle); leading-J low-energy SELECTION is full price (rank = M in all 12 cells); the non-orthogonal D_log operator eigenbasis is full price too. The mild low-energy alignment has the wrong sign for S4 (resolves, does not escape) and is not lattice-specific (perturbed operator identical) |
| `sonin_alignment` | WINDOW-ARTIFACT ONLY. The Sonin (low-concentration prolate) subspace drops rank tracking the number of comb points inside the vanishing window W (drop 2/1/3/4 vs in-W 3/1/3/4; drop 4 = n_inW 4 at lam=6, min_cos ~1e-13); the drop PERSISTS under perturbed logs and the out-of-W comb is full rank, so it is a spatial-support mirage carrying zero counting information, not a commensurability mechanism. Lattice-sourced = FALSE |
| `emap_channel` | shift-sum diagonal proxy (partial-zeta multiplier S_m) FULL PRICE, drop(perturbed) = 0, lattice-sourced = FALSE. The aperiodic x^{1/2} weight is UNBUILDABLE on the compact circle (recorded, not faked); the lattice-carrying shift-sum half is tested and negative |
| `perturbed_log_control` | every apparent drop PERSISTS under perturbed logs (T1 pert-operator full rank; T2 Sonin drop_pert = drop_true; T3 drop_pert = 0): nothing measured is lattice-sourced, so the S4 lattice clause is failed by all four channels |
| `dh_calibration` | full price at the dense sign-changing D-H comb (rank = M, all lambda): operator-knows-its-comb is full price regardless of comb sign; consistent with the D-H discipline (finite machine D-H-blind) |
| `beurling_screen` | full price (fake operator at fake comb); no zeta-only collapse exists to be absent for the fake; system-generic full-price, DMV-consistent |
| `k1_clean` | TRUE (source scan clean; guards installed, never tripped; ledger printed; eigenvalues out, no zero data in) |
| `s4_spec_answer` | NEGATIVE and CLOSED FOR EVERY BUILDABLE FAMILY. The carrier's own buildable spectral data (Weil-form energy eigenbasis, D_log operator eigenbasis, discrete central-window Sonin projection, E-map shift-sum pullback) supplies no lambda-uniform, well-conditioned, lattice-sourced rank collapse at the log-prime comb. The incommensurability reading of e1o extends to the carrier's own eigenbasis; the last corner of the S4/R1 coordinate is measured empty for every family that can be built here. SOLE UNBUILT VARIANT: the faithful metaplectic self-dual Sonin projector of arXiv:2310.18423 (tiered claim 12); the discrete central-window prolate is its finite proxy, but the faithful phase-space cutoff is not in the e1k machinery and its behaviour is not measured |
| `frontier_delta` | UNMOVED. The corner e1o left untested (no full eigenbasis in cache) is now measured with the same negative verdict as the five external families, plus a subtle mirage (the Sonin window drop) caught and explained. Nothing here moves M4 or BRIDGE-H |

## Tiered claims

**PROVEN (linear algebra, instantiated here):**
1. The full Hermitian eigenbasis is unitarily equivalent to the standard basis:
   sv(F V) = sv(F) for unitary V (verified to 3.6e-15). So full-eigenbasis
   collapse is impossible; only selection or a non-orthogonal basis can differ.
2. The comb functional identity <g_p, v> = f_v(u_p) (verified to 1e-12).
3. The assembler A+P = Q_e1k + herm(Ts_true) reconstructs e1k's build_float Q to
   1e-17 (the factorization reusing e1k's archimedean quadrature is exact).
4. Distinct comb points give a nonsingular trig Vandermonde (rank = M whenever
   M <= D and points distinct), so full-price at {log p} is the generic case;
   the measured 1.000 rank is that generic case, not an accident (same core as
   e1o's incommensurability finding).

**NUMERICAL (measured on this implementation):**
5. T1 leading-J full price at {log p}: rank = M in all 12 (lambda, J) cells;
   min_cos 0.002-0.63; perturbed operator identical rank.
6. T2 Sonin drop tracks #comb-in-window (drop 2/1/3/4 vs in-W 3/1/3/4 at
   lam=3/sqrt13/5/6; equal when in-window points are deep, one less near the
   window edge at finite N), min_cos ~1e-11 to 1e-13, drop persists under
   perturbed logs, out-of-window comb full rank; window artifact confirmed.
7. T2 D_log operator (non-orthogonal) eigenbasis full price (rank = M) all cells.
8. T3 E-map shift-sum proxy full price, drop(perturbed) = 0; S_0 = K exactly.
9. T4 D-H full price at the dense sign-changing comb (rank = M, all lambda).
10. T4 Beurling fake full price (fake operator at fake comb).

**STRUCTURAL / SCOPE:**
11. The Sonin window artifact reading (spatial support, not commensurability) is
    an interpretation supported by three controls, not a theorem; the specific
    window half-width a = (1/2) log 2 is the archimedean cutoff (a
    lambda-dependent / metaplectic self-dual radius is untested).
12. The faithful phase-space Sonin projector (the metaplectic self-dual cutoff of
    arXiv:2310.18423) is UNBUILT here; the discrete central-window prolate is a
    faithful finite proxy, and CCM's own definition (low eigenspace of the
    prolate operator) is the leading-J space of T1.
13. The E-map weight channel (x^{1/2}) is UNBUILDABLE on the compact circle.

## Named residual

The S4 slot on the CCM carrier is now measured empty in the carrier's OWN spectral
data too, closing the corner e1o could not reach. What survives of the S4/R1 route
is exactly the e1o Q4 spec, now hardened by a sixth family (the eigenbasis) and by
the observation that even the one apparent collapse (Sonin) is a spatial mirage:
any winner must still consume the additive lattice, sourced by an identity that
fails for perturbed logs, and no channel of the carrier's spectral data supplies
one. Nothing here moves M4 or BRIDGE-H; the probe converts 'the eigenbasis is the
one untested family' from an open item into a measured, control-calibrated negative.

## Handed forward

- **To ADVERSARY**: the sharpest attack surface is the T2 Sonin window drop. It IS
  a genuine well-conditioned rank drop (min_cos ~1e-13), and I diagnose it as a
  spatial-window artifact via three controls (drop = #in-W; persistence under
  perturbed logs; out-of-W comb full rank). The attack: find a Sonin/window
  configuration where the drop is NOT purely spatial, e.g. a window excluding all
  comb points that still drops, or an in-window comb whose lattice placement makes
  perturbation RESTORE rank. Also fair game: the window half-width a = (1/2) log 2
  is a fixed choice; a lambda-dependent self-dual radius or the true metaplectic
  Sonin projector (unbuilt here) could behave differently. Secondary: the T1
  min_cos being above the null in some cells is a mild low-energy alignment; verify
  it never turns into rank < M at larger lambda (I tested to lambda = 6, M = 18).
- **To VERIFIER**: three Lean-sized targets below.
- **To SURVEYOR**: whether the metaplectic self-dual Sonin projector of
  arXiv:2310.18423 (unbuilt here) admits a finite model on this carrier; and the
  theta <= 1/2 Beurling corner (the one open escape in the DMV screen, inherited
  from e1o).
- **To SYNTHESIZER**: one line: "e1r tested the carrier's OWN spectral data (Weil
  energy eigenbasis, D_log operator eigenbasis, Sonin projection, E-map pullback),
  the one S4 family e1o could not build, and measured the log-prime slot empty in
  all four channels; the only rank drop (Sonin) is a spatial-window mirage failing
  the perturbed-log control; the last corner of the S4/R1 coordinate closes
  negative, the incommensurability reading extended to the eigenbasis."

## Verification targets (for VERIFIER)

1. **Unitary invariance of evaluation singular values**: for unitary V, the
   singular values of F V equal those of F (Mathlib has the SVD / unitary
   invariance of operator norm; the full singular spectrum is the target). This
   is why the full eigenbasis cannot collapse.
2. **Comb functional = evaluation**: f_v(u_p) = <g_p, v> with
   g_p[n] = exp(-i phi n u_p) (definition-level).
3. **Window-artifact rank drop**: if J basis functions all vanish on a set
   W and k of the M evaluation points lie in W, the evaluation matrix drops
   rank by at least k (elementary: k zero columns). Formalizes the T2 mirage:
   the drop is spatial, independent of the arithmetic of the points.

## Adversarial test cases (configurations for ADVERSARY)

1. **Sonin window not purely spatial**: choose W disjoint from all comb points and
   check the Sonin subspace is full rank at the comb (predicted: yes, full rank);
   then choose W covering the top-k prime powers and check drop = k exactly
   (predicted: yes). A drop with W disjoint from the comb would break the reading.
2. **Perturbation restoring rank**: for the Sonin in-window drop, sweep the
   perturbation eps and confirm the drop tracks the NEW in-window count (spatial),
   never returning to a prime-specific pattern.
3. **Larger lambda / higher N**: push lambda beyond 6 (M > 18) and N toward the
   full Shannon budget 2 lambda^2; confirm T1 rank stays = M and no min_cos ->
   0 emerges (the corner's uniformity claim).
4. **D_log operator ordering**: the D_log-M test orders by Weil energy; re-order by
   |Im eigenvalue| or a random selection and confirm full price is order-robust
   (predicted: yes; selection cannot beat the Vandermonde at distinct points).
5. **Beurling eps / seed sweep**: vary the fake's eps and seed; confirm full price
   is fake-robust (nothing zeta-specific to be absent).

## Reproduce

```
python3 -m experiments.spectral.e1r_sonin_projector           # full (~40 s)
python3 -m experiments.spectral.e1r_sonin_projector --quick   # reduced grid
```
Outputs `e1r_sonin_projector.npz` (T1 alignment table, T2 Sonin drops + D_log-M,
T3 E-map, T4 D-H + Beurling, verdict flags). `--quick` does NOT write the npz
(the e1o adversary fix: a quick run must never clobber the tracked full-run
artifact). Reuses e1k's build_float (archimedean quadrature) and
`_shared/beurling.py`; no operator physics is rebuilt and no cache is written.

