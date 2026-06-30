# e2w2: the loglog-coefficient on the archimedean block (the one unexecuted probe toward P5)

> Experiment [`e2w2_loglog_arch_coupling.py`](e2w2_loglog_arch_coupling.py).
> Run `python -m experiments.arithmetic_geometric.e2w2_loglog_arch_coupling`.
> Executes the one named, marginally-live, not-yet-foreclosed probe toward P5 (the missing
> arithmetic-Rosati polarization) from [`../../docs/03_research/building_the_missing_positivity.md`](../../docs/03_research/building_the_missing_positivity.md)
> ("Smallest next step to test the only marginally-live thread").

## The probe

P5 = the arithmetic Hodge standard conjecture = the missing RH-closing polarization (RH-equivalent,
the open kernel). The four-mechanism first-principles sweep showed every construction of it collapses
at the same seam: the Euler product fixes the object's existence / block structure (a clean,
non-circular, RH-INDEPENDENT discriminator) while the off-line zeros live in the SHARED archimedean
continuation the Euler product does not touch. The sweep named exactly one unforeclosed test: promote
the Rankin loglog-coefficient

$$c_F = \lim_{X\to\infty} \frac{\sum_{p\le X} |a_F(p)|^2/p}{\log\log X}\quad(\,=1\ \text{primitive Euler},\ <1\ \text{else}\,)$$

from a scalar discriminator (experiment 3W) into the NORMALIZATION of the archimedean block of the
non-circular Weil/Rosati form $M = A_{\mathrm{arch}} + P_{\mathrm{fin}} + B_{\mathrm{pole}}$ (e2w /
M2.6). Does making multiplicativity act ON the continuation ($M_c = c_F\cdot A_{\mathrm{arch}} +
P_{\mathrm{fin}} + B_{\mathrm{pole}}$) inject the Euler structure into the GLOBAL signature and break
the M2.6 stealth window (where the unscaled $M$ reads D-H spuriously positive)?

Controls: zeta (Euler, RH-true), Epstein-d47-principal (NON-Euler, RH-true), Davenport-Heilbronn
(non-Euler, RH-false). The Epstein control is decisive: it is non-Euler ($c_F<1$) but RH-true.

## Result: no separation, deeper than predicted

| target | Euler | RH | $c_F$ | min eig $M$ | min eig $M_c$ |
|---|---|---|---|---|---|
| zeta | yes | true | 1.105 | **+0.0346** (POS) | **−4.57** (NEG) |
| Eps47-principal | no | true | 0.635 | +0.126 (POS) | −0.703 (NEG) |
| D-H | no | false | 0.369 | +0.094 (POS) | −0.515 (NEG) |

Baseline reproduces M2.6 exactly: all three POS, no separation (D-H reads spuriously positive = the
stealth window). The probe $M_c$ sends **all three NEG, including RH-true Euler zeta** whose
$c_F=1.105>1$ scales $A_{\mathrm{arch}}$ UP.

The block-magnitude diagnostic shows the mechanism, and it is **deeper than the predicted #20
non-Euler trap**:

| target | $\|A_{\mathrm{arch}}\|$ | $\|P+B\|$ | min eig $M$ |
|---|---|---|---|
| zeta | 44.32 | 44.38 | +0.0346 |
| Eps47-principal | 19.42 | 64.66 | +0.126 |
| D-H | 4.89 | 4.98 | +0.094 |

The unscaled positivity is a **razor-thin exact cancellation of LARGE blocks**: for zeta a block of
norm 44.3 cancels a block of norm 44.4 down to a +0.035 margin. Rescaling $A_{\mathrm{arch}}$ by
$c_F$ perturbs the form by $\sim 0.1\times 44 \approx 4.6$, which dwarfs the +0.035 margin and flips
the sign for **everyone, regardless of RH** (zeta with $c_F>1$ scaled up, Epstein and D-H with
$c_F<1$ scaled down). So multiplicativity cannot "normalize the archimedean coupling" to inject Euler
structure into the signature: the signature has **zero slack** — it IS the exact $A$-vs-$(P+B)$
cancellation. The $c_F$ idea fails not because $c_F$ is a non-Euler detector (the #20 trap I
predicted) but because there is no margin to rescale into. The marginal-positivity thesis, localized
onto this probe and made quantitative (a 44-vs-44 cancellation).

## Verdict

This closes the one marginally-live thread the construction sweep left open. P5 is unreached. The
missing math IS the polarization (the arithmetic Hodge standard conjecture), not a route to it: the
positivity is so marginal that the multiplicative coefficient, applied to the one block where the
zeros enter, destroys it rather than reading it. A clean negative coordinate that sharpens, not a
foothold. It also gives the marginal-positivity thesis its most concrete face yet: the RH-compatible
positivity of the non-circular Rosati form is a +0.035 cancellation of two norm-44 blocks.

## What is PROVEN vs numerical

- **NUMERICAL (this experiment):** the min-eig table, the block magnitudes, the $c_F$ values
  (recomputed via `rankin_loglog_partial`). The baseline reproduces e2w/M2.6 (zeta +0.035). The
  blocks $A,P,B$ need no zeros, so the min-eig verdict is exact given the L-evaluations; the M2.6
  zero-side validation (that these blocks equal the zero-side Gram) is the prior e2w result, not
  re-run here.
- **IMPORTED:** $c_F=1$ iff primitive Euler product (Selberg orthonormality / Rankin-Selberg); the
  M2.6 form construction; the D-H off-line zero and Epstein-d47 RH-truth (<=120).
- **CONJECTURAL / scope:** "$M_c$ separation" was the falsifiable target; it failed, decisively. The
  result is about the faithful single-basis operationalization ($c_F$ scaling the archimedean
  contribution); a genuinely separable arch-to-finite off-diagonal does not exist in this summed
  form, which is itself part of the finding (there is no coupling to renormalize independently).

## Cross-refs

[`../../docs/03_research/building_the_missing_positivity.md`](../../docs/03_research/building_the_missing_positivity.md)
(the four-mechanism sweep + the named "smallest next step"); [`e2w_rosati_fourway_M2_6.py`](e2w_rosati_fourway_M2_6.py)
(the M2.6 form + the stealth-window finding); [`../positivity/e3w_rankin_loglog.py`](../positivity/e3w_rankin_loglog.py)
(the $c_F$ scalar discriminator + the #20 non-Euler trap); [`../../lean/ZetaRH/ArithmeticPolarization.lean`](../../lean/ZetaRH/ArithmeticPolarization.lean)
(P5 as a Lean Prop: RH iff the FE pairing is conjugation). MEMORY: marginal-positivity thesis,
first-principles-audit, gradient-descent-d4-thread.
