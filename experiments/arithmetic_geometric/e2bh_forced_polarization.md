# e2bh: the surgery costume (forced polarization)

**Date**: 2026-08-26. **Status**: EXECUTED, 13/13 full and quick; all three pre-registrations FIRED. **Gallery**: G1 of [`construct_gallery.md`](../../docs/03_research/construct_gallery.md).
**Label (per the #201 derivability check)**: re-measurement of the wall (the K1 face), new costume. No new coordinate claimed.

## What was built (deliberately wrong)

The zero-side compressed Weil Hermitian form $B[j,k] = \sum_\rho F_j(\rho)\,\overline{F_k(1-\bar\rho)}$ on a 21-member window family (modulated Gaussians, centers $\tau \in [80, 90]$ step $0.5$, $\sigma = 3$), zeros to $T = 100$ at dps 30, followed by the surgery: $P = B_+$ (delete the negative eigenspace) and the declaration "P is the polarization". The build commits the K1 sin at line one (the form is assembled FROM the zeros) and then doubles down; the experiment measures exactly what the sin buys and where it localizes.

## Results

| Measurement | zeta | D-H |
|---|---|---|
| min eigenvalue / scale | $-3.7\times10^{-16}$ (PSD at floor) | $-0.63$ (genuine) |
| negative eigenvalue count | 0 | **exactly 1** |
| surgery removal $\|P-B\|/\|B\|$ | $9.3\times10^{-16}$ (no-op) | $O(1)$ |
| deleted-mode line profile peak | (none) | $t = 86.11$, within $0.5$ of the landmark $85.699$ |
| forced $P$ PSD | yes | **yes** (the disqualification) |

1. **Free where information-free.** On zeta the window form is already PSD at the numerical floor and the surgery removes nothing: the #170 clause (compactness/forcing is free exactly where it is information-free) in matrix coordinates.
2. **Unit index weight.** The D-H window form has exactly one negative eigenvalue, i.e. the off-line pair enters the compressed form at one unit of index: the Alpöge-Furman Sylvester-inertia mechanism (LEARNINGS #202(iii)) reproduced in a 21-dim window family, from the FE-paired rank-2 hyperbolic block.
3. **The K1 audit.** The deleted eigenvector's critical-line profile peaks at $t = 86.11$: the surgery data IS the off-line zero location. The forced polarization cannot be written down without reading the zeros; that is K1 quantified, not just asserted.
4. **The disqualification, stated as a passing gate.** The surgery outputs a PSD form for D-H too, i.e. the route "proves RH" for the counterexample; the D-H discipline rejects it structurally. Beurling cannot even be posed (no zeros): the counting-side refusal. The pipeline consumes no prime data anywhere (Euler-blindness gate): by e2az's trilemma the route fails D3 (Euler contact) as well as D2 (K1).

## Pre-registrations

- P1 FIRED: zeta window form PSD at the floor.
- P2 FIRED: exactly one negative D-H eigenvalue (unit index weight).
- P3 FIRED: deleted-mode peak within $1.0$ of $85.699$ (measured $86.11$).

## Artifacts

[`e2bh_forced_polarization.py`](e2bh_forced_polarization.py) (13/13), tracked npz alongside. Controls: shared zeta / D-H / Beurling via `experiments._shared`.
