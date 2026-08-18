# ADVERSARY round on e1y (self-run, 2026-08-17/18)

Precedent: `_e1v_adversary.md` (#172) was self-run too. Attacks were written
down before any of them was executed; the record below reports what each one
did, including the two that landed on e1y's own text.

**VERDICT: PASS_WITH_FIXES.** One stated claim is FALSE and is demoted. The
central conclusion survives and is better supported than it was, because the
attack that killed the claim also supplied a sharper replacement. Nothing in
the RH-facing reading changes: the D-H undercount still carries no arithmetic
information.

## The attacks, as posed

| | attack | pre-registered kill condition |
|---|---|---|
| A1 | **Protocol dependence.** e1y fixes `N = n_hi + 7`, a reconstruction choice, since the adversary script that found the original numbers is absent from this machine. | any D-H cell changing class over margins {3, 7, 12, 20} |
| A2 | **Precision dependence.** e1y itself reports `dev` moving between dps 15 and 25, and defends itself by resting on the CLASSIFICATION rather than the integers. That defence had better hold. | any cell changing class over dps {15, 25, 35} |
| A6 | **Is the mechanism causal?** e1y shows a correlation (small `delta.xi`, deficit) plus two repairs, and a repair changes the comb, so it changes everything at once. Direct intervention instead: take a HEALTHY build and inflate its residues by hand, `xi_n -> c xi_n`, which is exactly "`delta.xi` shrunk by `1/c`" with nothing else touched. | the count stays exact however large `c` grows, which would demote e1y's mechanism to a correlation |

## A1: DOES NOT LAND

The class is stable at every margin, at all three `lam`:

| lam | m=3 | m=7 | m=12 | m=20 |
|---|---|---|---|---|
| 3.3 | -2 STR | -2 STR | -2 STR | -2 STR |
| sqrt13 | -2 STR | -2 STR | -2 STR | -2 STR |
| 4.0 | -2 STR | -2 STR | -1 STR | -1 STR |

The integer `dev` does move at `lam = 4.0` (-2 to -1 at the wider margins),
which is worth knowing, but the class does not. The protocol choice is not
driving the finding.

## A2: LANDS

The class flips with working precision at two of three cells:

| lam | dps 15 | dps 25 | dps 35 |
|---|---|---|---|
| 3.3 | -2 STR | -2 STR | -1 STR |
| sqrt13 | **-1 REC** | -2 STR | -2 STR |
| 4.0 | -2 STR | -2 STR | **+0 REC** |

At `lam = 4.0`, dps 35, D-H's count is EXACT. So e1y's sentence

> "The *classification* (which cells are structural, and its agreement with
> the conditioning diagnostics) is what this probe rests on, not the
> individual integers."

is **false as written** and is demoted on the record. The classification is
not dps-stable either.

### The follow-up that decides what survives

The flip is compatible with two very different readings: (a) the probe is
precision noise and the finding is worthless, or (b) an ill-conditioned build
has a precision-dependent count, which is itself the symptom, and a
well-conditioned one does not. (b) predicts a ONE-SIDED instability. Measured
(18 builds, both twins, three precisions):

| lam | case | dps 15 | dps 25 | dps 35 | class stable |
|---|---|---|---|---|---|
| 3.3 | Zoff | eps -5.340, \|dxi\| 0.5588 | -5.340, 0.5593 | -5.341, 0.5608 | yes |
| 3.3 | DH | 8.19e-5, 7.71e-4 | 7.61e-5, 7.17e-4 | 2.02e-5, **5.76e-6** | yes |
| sqrt13 | Zoff | -5.850, 0.5657 | -5.849, 0.5648 | -5.850, 0.5675 | yes |
| sqrt13 | DH | -1.52e-5, 1.13e-2 | 3.34e-5, 9.82e-4 | 4.64e-6, 3.78e-4 | **no** |
| 4.0 | Zoff | -6.489, 0.5446 | -6.492, 0.5598 | -6.492, 0.5584 | yes |
| 4.0 | DH | 8.88e-5, 6.33e-5 | 1.71e-6, 9.47e-5 | -2.59e-6, 1.28e-3 | **no** |

**zeta-off stable at 3/3, D-H at 1/3.** And the diagnostics themselves split
the same way. Zeta's `eps` reproduces to four digits and `|delta.xi|` to
three across a twenty-digit change in working precision. D-H's `eps` wanders
by factors of 4 to 50 **and changes sign**; `|delta.xi|` wanders by factors
of 20 to 130 **and changes sign**; and `even_assumption_ok` itself flips
(False at `lam = sqrt13` dps 15, True at 25 and 35).

(Sign changes in `delta.xi` alone are meaningless: `xi` is an eigenvector,
fixed only up to sign, and zeta's own sign flips harmlessly between dps 15
and 25 at `lam = 4.0` while its magnitude holds to three digits. What is
diagnostic is the MAGNITUDE moving by two orders.)

That is the signature of a quantity that is zero being reported as noise. So
the honest statement is **stronger** than e1y's, not weaker:

> For D-H at `lam >= 3.3` the ground-state eigenvalue and the normalization
> `delta.xi` are numerically indistinguishable from zero at every precision
> this harness can reach. `xi` is the eigenvector of a numerically degenerate
> eigenvalue, so it rotates freely inside that subspace as precision changes,
> and `xi_n = xi/(delta.xi)` is not merely ill-conditioned but **undefined**
> on those builds. The count's precision-dependence is a consequence of that,
> not a competing explanation for it.

## A6: DOES NOT LAND, and confirms the mechanism causally

Take a healthy zeta-off build and scale `xi_n -> c xi_n`, changing nothing
else. No rebuild, no comb change, no density change.

`lam = sqrt13`, N = 40, lattice 33, healthy `delta.xi` = -0.5648:

| c | 1 | 3 | 10 | 30 | 100 | 570 | 3000 |
|---|---|---|---|---|---|---|---|
| effective `delta.xi` | -5.6e-1 | -1.9e-1 | -5.6e-2 | -1.9e-2 | -5.6e-3 | -9.9e-4 | -1.9e-4 |
| dev | +0 | +0 | **-2** | -9 | -9 | -9 | -9 |
| class | REC | REC | **STR** | STR | STR | STR | STR |
| n_pos | 40 | 40 | 40 | 40 | 40 | 40 | 40 |

`lam = 4.0` behaves the same way (REC at c = 1, 3; STR from c = 10 on).

Residue inflation alone breaks a perfectly sound build's count, which is what
e1y claimed and had only shown by correlation. The threshold is `c ~ 10`,
i.e. `|delta.xi| ~ 5e-2`, so the construction is MORE sensitive than e1y
implied when it pointed at the 788x median ratio.

### What A6 also found, which e1y had conflated

`n_pos = N` at **every** `c`. So residue inflation causes the count deficit
but does **not** cause the conservation failure `#{Re > 0} != N`. e1y's U2-3
check reported the two coinciding cell-for-cell and read them as one
symptom of one cause. They are two symptoms, and only the first is explained.
Nor is the second explained by the evenness violation: `lam = 3.3` has
`even_assumption_ok = True` at every dps and still breaks conservation.

**Open residual, recorded rather than papered over: the cause of the
conservation failure is uncharacterized.**

## Fixes applied to e1y

1. The "classification, not the integers" defence is **removed** and replaced
   by the measured one-sided instability above (zeta 3/3, D-H 1/3) plus the
   `delta.xi`-is-numerically-zero statement, which is what actually carries
   the finding.
2. The mechanism paragraph now cites A6's direct intervention rather than
   resting on correlation plus repairs, and quotes the `c ~ 10` threshold.
3. U2-3's claim that the conservation failures and the count deficits are one
   phenomenon is **split**: the count deficit is causally explained, the
   conservation failure is listed as an open residual.
4. The `dev <= -2` cut inside U2-3 is replaced by the threshold-free
   structural criterion, since the cut was arbitrary.

## What did not move

The RH-facing reading is unchanged and better supported. The D-H undercount
is a fact about where this reconstruction stops being defined, not about
Davenport-Heilbronn zeros; #169's catch still stands as a statement about the
numbers and still re-types as a validity-domain statement; and the rigorous
Weyl-on-`Q` backbone never used the ground state, so it is untouched by any
of this. K1 is clean throughout (the guards were installed in every attack
build and never tripped).
