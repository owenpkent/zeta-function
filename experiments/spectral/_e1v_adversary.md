# ADVERSARY report: e1v (the Christoffel gauge)

**Date**: 2026-08-08. **Scope**: self-run, in the absence of an external ADVERSARY round. Executable probe: [`_e1v_adversary.py`](_e1v_adversary.py) (`python -m experiments.spectral._e1v_adversary`), which consumes e1v / e1u / e1t by import and adds no new build. **Verdict: PASS on all five attacks run (A-E); the two attacks NOT run are named at the end and remain open.**

This report covers adversarial test cases 1, 2, 4, 5, 6 of [`e1v_christoffel_gauge.md`](e1v_christoffel_gauge.md). Cases 3 (scope of the continuity obstruction) and 7 (independent re-verification of K1/determinism) are prose/replication tasks and were not run here.

## A (case 5): does V2d's family-blindness survive other equalization bands?

The V2d family comparison equalizes the low band at $|t| \ge 13.6$ (zeta's own gate boundary, inherited from e1u U2c). If the 1.27x family spread were an artefact of that particular threshold, the reading would be worthless.

| band | BEUR | D-H | ZETA | spread | verdict |
|---|---|---|---|---|---|
| 13.6 | 1.206 | 1.309 | 1.534 | 1.27x | family-blind |
| 16.0 | 1.206 | 1.254 | 1.496 | 1.24x | family-blind |
| 20.0 | 1.245 | 1.221 | 1.478 | 1.21x | family-blind |
| 25.0 | 1.141 | 1.196 | 1.488 | 1.30x | family-blind |

**ATTACK DID NOT LAND.** The spread is $1.21$ to $1.30$ across every band tested, and the family ordering is not even stable (D-H is above BEUR at 13.6 and 16.0, below it at 20.0). ZETA's mean is consistently the highest, but that mean contains the single V7-flagged build ($\rho_{\text{eq}} = 2.204$); with it removed zeta's mean is $1.31$, numerically equal to D-H's. Recorded in the dossier as such.

## B (case 4): is the V7 audit stable in DEGEN_RATIO, and does the ZETA 3.0 residual survive a different repair?

DEGEN_RATIO $=0.25$ was chosen after seeing the grid, which is exactly the kind of choice an adversary should attack.

| DEGEN_RATIO | flagged | unflagged $\rho_{\text{eq}}$ band |
|---|---|---|
| 0.15 | ZETA 3.00 | [1.083, 1.607] |
| 0.25 | ZETA 3.00, ZETA 3.61 | [1.083, 1.538] |
| 0.40 | ZETA 3.00, ZETA 3.61 | [1.083, 1.538] |

The flag set is stable on $[0.25, 0.40]$ and only loses the weaker of the two builds at $0.15$; in every case ZETA 3.0 is flagged, which is the one the audit's conclusion rests on.

Two different surgeries on ZETA 3.0 (band-equalized, raw $\rho_{\text{eq}} = 2.204$, unflagged band top $1.538$):

- **separate** the sub-threshold pairs to the median spacing: $\to 1.736$ (70 percent of the excess removed, $+0.199$ residual);
- **remove** the tight pair outright, recomputing the bound for the smaller configuration: $\to 1.440$, **inside the unflagged band**.

**ATTACK DID NOT LAND, and it resolved an open item.** The $+0.199$ residual reported as open in the dossier's honest limit 4 is **repair-dependent**: it survives the separation surgery and vanishes under the removal surgery. So it is a property of the chosen surgery (separating a pair to the median leaves the configuration locally denser than a typical one, which the bound does not see), not a stable family signal. Honest limit 4 is downgraded accordingly.

## C (case 1): theorem sanity

- **Brute force**: 400 random even configurations with **non-uniform random weights**, $M$ up to 24, $g/T$ from $0.005$ to $0.9$: **0 violations**, worst $(\text{bound} - \text{measured}) = 0.0$.
- **Small $M$**: $M=2$ gives $n=0$ and the trivial bound $0 \le 0$; $M=4$ ($n=1$) gives $0.160 \le 0.776$; $M=6$ ($n=2$) gives $0.596 \le 1.444$. The $2n \le M-1$ bookkeeping is correct at the edge.
- **$g \to 0$**: $G$ and the log-bound go to 0 like $g$ ($g = 5, 1, 0.1, 0.01, 0.001$ give log-bounds $3.05, 0.188, 0.0019, 1.9\text{e-}5, 0$), i.e. the bound degrades to the trivial $1/\lambda \ge 1$ exactly as a gapless configuration requires.

**ATTACK DID NOT LAND.** The theorem is correct as stated, including for non-uniform weights (which the e1v grid only exercises on Face B).

## D (case 2): does $\rho$ grow without bound at fixed gap fraction?

The dossier reads $\rho = O(1)$ off a grid where $M$ and the gap fraction move together. The sharp test holds $g/T = 0.25$ fixed and grows $M$ on equally spaced atoms:

| M | 8 | 12 | 16 | 24 | 32 | 48 | 64 | 96 |
|---|---|---|---|---|---|---|---|---|
| $\rho$ | 1.450 | 1.299 | 1.298 | 1.330 | 1.355 | 1.384 | 1.401 | 1.419 |

$\rho$ grows $0.98$x while $M$ grows 12x; the trend from $M=12$ upward is a slow creep from $1.30$ to $1.42$ that is visibly saturating.

**ATTACK DID NOT LAND, and this strengthens V2b.** At fixed gap fraction $\rho$ is bounded and close to $4/3$ over a 12-fold range of $M$, so "the proved geometric rate is the leading order" is structural rather than grid-local. It also isolates what the observed $\lambda$-drift of $\rho_{\text{eq}}$ in the real families is: not an $M$ effect, but the gap fraction $g/T$ shrinking as the window grows at fixed $g$.

## E (case 6): does a spacing-distribution-preserving surrogate change V3a's answer?

The block surrogate preserves macroscopic density and destroys microstructure. The complementary surrogate randomly permutes the multiset of gaps: the spacing **distribution** is exactly preserved and the density **profile** is destroyed (5 seeded permutations, averaged).

| build | M | block $K{=}1$ | shuffled gaps | flag |
|---|---|---|---|---|
| BEUR 2.2 / 2.6 / 3.0 | 14 / 22 / 38 | 0.0095 / 0.0026 / 0.0001 | 0.0129 / 0.0154 / 0.0056 | |
| D-H 2.2 / 2.6 / 3.0 / $\sqrt{13}$ | 14 / 24 / 38 / 64 | 0.0052 / 0.0249 / 0.0359 / 0.0605 | 0.0050 / 0.0255 / 0.0260 / 0.0516 | |
| ZETA 2.6 | 16 | 0.0268 | 0.0489 | |
| ZETA 3.0 | 26 | 0.3633 | 0.2244 | DEGENERATE |
| ZETA $\sqrt{13}$ | 48 | 0.0417 | 0.0220 | DEGENERATE |

All builds: worst block $0.363$, worst shuffled $0.224$. V7-unflagged only: worst block $0.061$, worst shuffled $0.052$.

**ATTACK DID NOT LAND.** On every build the declared V7 rule does not flag, the two structurally different surrogates agree: the per-atom rate displacement stays under $0.06$ in both. The two flagged builds move more under **both** surrogates, which is the V7 conditioning story again rather than a surrogate artefact. (Applying the V7 flag here is the same rule V3a already applies, not a new exclusion invented for this probe; the unflagged and all-build numbers are both reported above.)

## Net

Five attacks run, five failed to land, and one of them (B) closed an item the dossier had left open. Nothing in the e1v verdict was weakened. Specifically:

- the theorem is correct, including at the edges and for non-uniform weights (C);
- its order-tightness is structural, not grid luck (D);
- the family-blindness of the tightness residual is not an artefact of the equalization band (A);
- the near-degeneracy audit is not an artefact of its own threshold, and its one residual is an artefact of the surgery (B);
- the density-versus-microstructure answer does not depend on which surrogate destroys the microstructure (E).

## F (added, not posed in the dossier): are the atom sets the ones e1u actually used?

Every number in e1v is a functional of the Face-A/Face-B atom sets, which are re-derived here by importing e1u's `face_A` / `face_B` rather than read from e1u's artifact. If the re-derivation drifted, the whole rung would be measuring a different object than the one e1u certified. Checked against the tracked `e1u_canonical_chain.npz` (`u1_*_M`, `u1_*_lens[0]`), all 22 build-faces:

- **Every atom COUNT $M$ reproduces exactly, 22/22.** The zero extraction is robust across machines.
- **Every germ length $X$ reproduces to $\le 1.6\cdot10^{-8}$ relative, with exactly one exception: ZETA 3.0 Face A, at $3.7\cdot10^{-4}$**, four to five orders worse than every other build-face.

**This is an independent confirmation of V7 that the rung did not ask for.** The single build whose germ length fails to reproduce across machines at the build-noise level is precisely the one the declared near-degeneracy rule flags, for precisely the stated reason: a pair at separation $0.124$ makes the Lagrange sum hypersensitive, so a $3\cdot10^{-11}$ difference in the build amplifies to $4\cdot10^{-4}$ in $X$. The conditioning story is therefore not a post-hoc rationalization; it predicts which build breaks under an independent perturbation, and that prediction holds.

**Separate finding, for the record (documentation, not reproducibility):** e1u's dossier conditioning table gives BEUR 3.0 Face A as `36 / 41.0`, while e1u's own tracked npz gives $M = 38$, $X = 43.4631$, which this machine reproduces to $3\cdot10^{-12}$. The Face-B row for the same build matches the npz exactly. The npz and the recomputation agree; the one md row does not. Flagged for Owen rather than edited, since [`e1u_canonical_chain.md`](e1u_canonical_chain.md) is an adversary-verified artifact.

## Attacks NOT run (open)

1. **Case 3**: verify that the continuity obstruction is scoped correctly, i.e. that it kills pointwise detection **without** quietly claiming to kill sequence-level (sum-rule) statements. This is a prose-level check on the verdict line and the strongest place for an independent reader to catch overclaiming.
2. **Case 7**: independent re-verification of K1 guards, the planted-call scan, npz byte-reproducibility and quick/full parity. All were verified in-session (including a planted `mp.zetazero(1)` call being caught, and only it), but not by a second party.
