# E1AG: the visibility-floor curve, measured

> Frame session F2b's calibration build (2026-08-28), companion to
> [`f2b_visibility_floor.md`](../../docs/03_research/f2b_visibility_floor.md).
> Module: [`e1ag_visibility_curve.py`](e1ag_visibility_curve.py); npz tracked next to
> the script. **Full 16/16, quick 15/15 (the D-H cell is full-mode); all four
> pre-registrations SURVIVED.** Runtime 6 s full. Nothing here proves the theorems;
> each gate is an instance whose failure would falsify a named lemma at the measured
> scale. No em dashes.

## 1. Headline numbers (full mode, N = 14659, T = 1e4, seed 212)

| What | Measured | Theorem anchor |
|---|---|---|
| Split envelope exactness | rel err $6.9 \times 10^{-15}$ | L2c's exact identity |
| Merge cost vs Bernstein | $0.185 \le (\pi \Delta s)^2 = 0.253$ | L2b |
| NAIVE-site merge, res family, jitter base | 106x slack: BLOCKED | L4's necessity (generic base) |
| L3+L4-selected merge, full battery | worst 0.60x slack, $E = 44 = 2k$ | Theorem 1(i) floor |
| Exchange two-sided | floor $E = 44$ vs certified 147: ratio 0.30 | Theorem 1(i)+(ii), $[c_1, C_1]$ |
| Second slack rung ($\varepsilon = 3 \times 10^{-3}$) | worst 0.32x slack, $E = 2k$ | linearity |
| Lattice naive gap-1 merges | 6393x slack: BLOCKED | L4 rigid-base block |
| Lattice gap-2 (aligned) merges | 0.0000x slack, $E = 48$ | L4(i): rigidity blind to aligned moves |
| Frontier $\delta^* \times \Theta$ at $\Delta = 4, 8, 16$ | $[5.29, 5.29, 5.29]$, spread 1.000 | Theorem 2(iii): the $1/\Theta$ law |
| The band ($\varepsilon$: $10^{-2} \to 10^{-4}$) | $3.98$ vs $\log 100 = 4.61$ | Theorem 2(iii): thin band |
| Sub-resolution splits | $N_{\mathrm{off}} = 40$ at $\delta = 0.011$, link shift 0.23x slack, $E$ unchanged | Theorem 2(i) floor |
| D-H cell | landmark $\gamma = 85.699$, $\beta = 0.8085$, FE-paired, $E(\mathrm{strip}) = 2$ | Section 6 bracket |
| Beurling cell | no zeros interface: type refusal | Section 6 bracket |

## 2. What the numbers say, briefly

**The cost calculus is exact, not approximate.** The split cost of one event against
a link family is the closed-form envelope to machine precision (the e2aw/e2ax lineage
of exact identities continues), and the merge cost sits inside Bernstein's bound with
27 percent headroom at the tested point.

**The floor is real and the exchange is linear at matched constants.** At granted
absolute slack $\varepsilon N$ the selected merge configuration carries
$E = 2k = 0.3 \times$ slack while every granted family (three Fejér windows, the
HMH-shaped $N^{\circledast}$ family, two resonance frequencies, three link supports)
moves by at most 0.60x its slack; the in-class HMH engine certifies $E \le$ slack
over matching configurations; the merged configuration itself matches the grant. The
bracket $[0.30, 1.0]$ is the measured face of Theorem 1's $[c_1, C_1]$.

**The frontier is hyperbolic in support, with the predicted band.** The measured
detection frontier satisfies $\delta^* \Theta = 5.29$ IDENTICALLY across the
three-octave support ladder (spread 1.000: the binary search resolves the same
constant each time because the anomaly is the exact envelope), and dropping the
slack two orders moves $\delta^* \Theta$ by 3.98 against the predicted
$\log 100 = 4.61$ (the discrepancy is the $\cosh$-vs-$e^{\delta\theta}$ small-argument
correction at the lower rung, visible and understood).

**Both invisibility floors and both blocks are measured.** Forty off-line zeros at
sub-resolution displacement move the link battery 0.23x slack with the marginal
exactly unchanged; the naive-placement blocks (generic 106x, rigid 6393x) and their
selection rescues (0.60x, 0.0000x) bracket L4 from both sides.

## 3. The build-phase catch, kept on the record (gate C0)

The module's first draft placed merge sites at random and FAILED its own battery on
the resonance family, on the GENERIC base (7.9x slack at quick scale): the
$|\Sigma|^2$ shape amplifies a coherent $\Delta\Sigma$ through the cross term
$2|\Sigma||\Delta\Sigma|$ even when $|\Sigma|$ is only at fluctuation scale. This is
the same phenomenon the F2a adversary's (M) bookkeeping ("every bounded-kernel gap
functional changes by O(1) per event") misses, discovered independently by the
theorem draft (rigid case) and by this build (generic case). The repair implemented
and measured here is the theorem's L4 in its corrected form: small-gap candidates
(per-event resonance cost $2(1 - \cos(us/2))$, exact) greedily vector-balanced
across all granted resonance frequencies simultaneously, and on rigid bases the
resonance-aligned sites that are exactly free. The theorem document's L4 was
REWRITTEN to this form after the build (its first-draft equidistribution route was
insufficient); the build is the reason the lemma is now stated with its regime
condition. This is the intended direction of information flow: the instrument
corrected the proof sketch before the adversary saw either.

## 4. Honest limits

- The model is synthetic: unit-density jittered-lattice and lattice bases at
  $N = 14659$, not zeta ordinates; C0's RvM frame is respected by construction
  (jitter half-width 1/2) but no arithmetic is present anywhere. That is by design:
  the theorems are configuration-space statements and the build instantiates their
  quantifiers. The zeta-geometry instances of the same laws are already in the
  ledger (#192's measured envelope, #199's certified window floors).
- The D-H cell consumes the shared control at the cached tuple (T_max = 100); its
  marginal-invariance clause is structural (marginal reads are functions of the
  ordinate multiset alone) and is stated as such, not gated as a measurement.
- The frontier is measured through the exact single-pair anomaly formula (binary
  search on the closed form), not through re-summing the full configuration per
  $\delta$; gate C2 pins the delta-computation to the full recompute at
  $1.6 \times 10^{-13}$.
- Gate thresholds (0.75x slack, ratio window $[0.25, 1.0]$, spread 1.35, band factor
  2) are pre-registered instrument tolerances, not theorem constants.
