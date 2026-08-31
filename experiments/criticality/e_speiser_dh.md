# E_SPEISER: Speiser's criterion run against the Davenport-Heilbronn control

**Status:** DONE 2026-08-31. Probe [`e_speiser_dh.py`](e_speiser_dh.py), 11/11 full, 9/9 quick.
**Question source:** the Wikipedia gap sweep, Tier 1 item 4.4
([`wikipedia_rh_gap_sweep_2026-08-31.md`](../../docs/03_research/reading_notes/wikipedia_rh_gap_sweep_2026-08-31.md)).
**Ledger:** LEARNINGS #214. Standing-lane probe under the #213 frameless-window guard: no frame
grading; it FILES an existing reformulation, minting nothing.

## 1. The question

Speiser (1935): RH is equivalent to $\zeta'(s) \ne 0$ in the open left half-strip
$0 < \operatorname{Re}(s) < 1/2$; Levinson-Montgomery (1974) is the counting form ($\zeta$ and
$\zeta'$ have, up to $O(\log T)$, equally many zeros left of the line). This is an exact
reformulation of RH. The question the sweep filed: is its mechanism FE-only? The house test is
Davenport-Heilbronn: a functional equation, no Euler product, its own RH false, first off-line
pair $\beta = 0.8085$ and $0.1915$ at $\gamma = 85.699$.

**Pre-registered expectation:** the mechanism transplants: D-H's derivative acquires a zero left
of the line near the off-line pair, filing Speiser in the FE-only RH-blind bin. The probe was
built so that either outcome is a determinate measurement (the winding number is the headline;
hard checks are integrality, stability, and instrument validation).

## 2. Method

- **Analytic derivatives, no finite differences.** Through the Hurwitz representation
  $f(s) = 5^{-s} \sum_a c_a\, \zeta(s, a/5)$:
  $f'(s) = 5^{-s}(\sum_a c_a\, \zeta'(s, a/5) - \log 5 \cdot \sum_a c_a\, \zeta(s, a/5))$, and
  $f''$ likewise; $\zeta'(s)$ via mpmath's `derivative=1`. Validated against central differences
  to relative error $5 \times 10^{-21}$.
- **Winding numbers by adaptive phase continuation** around rectangles: subdivide until every
  consecutive phase step is below $0.8$ rad (no step can alias a turn), integrality within
  $0.02$ required everywhere. $f$ and $f'$ are entire, so a winding IS a zero count.
- **Instrument positive control:** a known $f'$ zero at $1.24169186141 + 87.428004197i$ is
  counted exactly once by both a small circle and a box.
- **Independent cross-check:** a coarse $|f'|$ grid feeding Newton iteration with the analytic
  $f''$ (muller's error metric stalls near $3 \times 10^{-16}$ on $f'$ roots, so root polishing
  is plain Newton with residuals verified directly) must reproduce the winding count.
- **Stability:** the headline box re-run at dps $30 \to 40$ with $2\times$ sampling.

## 3. Results

| window | function | zero count |
|---|---|---|
| $[0.06, 0.44] \times [10.1, 100.2]$ | $\zeta'$ | 0 |
| $[0.06, 0.44] \times [80.2, 90.1]$ | $\zeta'$ | 0 |
| $[0.06, 0.44] \times [80.2, 90.1]$ (off-line height) | D-H $f'$ | **1** |
| $[0.06, 0.48] \times [83.0, 88.0]$ (squeezed to the line) | D-H $f'$ | 1 (the same zero) |
| $[0.06, 0.44] \times [10.1, 80.2]$ (below the pair) | D-H $f'$ | 0 |

The left-strip derivative zero: $s^* = 0.405371527228556 + 85.7051360266508\,i$, with
$|f(s^*)| = 0.396$ (a genuine $f'$ zero, not a zero of $f$), at distance $0.214$ from the left
off-line zero $1 - \bar\rho$; the off-line zero itself refines to
$\rho = 0.808517182457 + 85.6993484854\,i$ (both members of the pair verified simple,
$|f| < 10^{-25}$, $|f'| \approx 1.256$).

## 4. Verdict

**The Speiser mechanism transplants, and it is local.** Exactly one left-of-line derivative
zero, exactly at the off-line height, none below it, while $\zeta'$ (RH-true world in the
checked range) shows none anywhere. The off-line-pair $\leftrightarrow$ left-derivative-zero
correspondence fires identically for the known counterexample, so the criterion consumes only
the functional-equation half of the adelic package. Speiser files in the FE-only RH-blind bin,
on the same shelf as automorphic scattering unimodularity
([`local_quantum_gravity_and_primes.md`](../../docs/03_research/local_quantum_gravity_and_primes.md)
section 4.2; the #170 law that free structure is free exactly where it is information-free).
As a proof route, "show $\zeta' \ne 0$ left of the line" inherits the whole wall: its detector
cannot tell $\zeta$ from D-H.

**The bracket, honestly.** The D-H column is the kill, above. The Beurling column is
inapplicable BY CONSTRUCTION: a form-side criterion cannot even be posed without the functional
equation, which the Beurling control lacks on purpose. That inapplicability is itself the
diagnosis: Speiser's statement is made of exactly the FE half.

## 5. Instrument lesson (banked)

The reconnaissance grid ($\sigma \le 0.42$, $t$-step $0.6$) saw a minimum $|f'| = 2.77$ and
missed $s^*$ entirely, and muller root searches started in the left strip escaped to
$\sigma \approx 1.2$-$2.8$. Winding numbers, not grid minima or root-finder trajectories, are
the reliable zero counter. Same lesson class as the #199/#202 instrument-blindness catches.

## 6. Scope

One function, one window ($t \le 100.2$ for $\zeta'$, $t \le 90.1$ for D-H), numerical at
30-40 dps with integrality margins of $0.02$. The Levinson-Montgomery counting theorem is not
re-proved; nothing here bears on Speiser's truth for $\zeta$, only on its discriminating
content. Box boundaries were chosen off zeros; a zero on a contour aborts loudly (none did).
No cached artifacts: the outputs are integer counts and two localized points, reproduced by

```
python -m experiments.criticality.e_speiser_dh          # 11 checks, ~10 min
python -m experiments.criticality.e_speiser_dh --quick  # 9 checks, skips the two long contours
```
