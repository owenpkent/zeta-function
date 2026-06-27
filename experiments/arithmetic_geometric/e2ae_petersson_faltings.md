# 2AE: the archimedean self-intersection omega-bar^2 = 12 h_Fal, computed

> Experiment [e2ae_petersson_faltings.py](e2ae_petersson_faltings.py). Executes the
> deferred numerical follow-up flagged in
> [2J_arakelov_adjunction.md](2J_arakelov_adjunction.md) (section "Status and the
> concrete numerical follow-up"): the one piece of the Arakelov dictionary that 2J
> specified but did not compute, the archimedean part of the arithmetic
> self-intersection of the dualizing sheaf, omega-bar^2 = 12 h_Fal(E), via the
> Petersson norm of the weight-12 discriminant modular form. This is the
> omega-bar^2 companion to 2H/2I's validated point-height work.

## The object

On the function-field side (2G) the canonical self-intersection Delta^2 = 2 - 2g
comes from adjunction on C x C, and that self-intersection is exactly what makes
the primitive Gram matrix non-degenerate (without Delta^2 the Hasse-Weil bound
has nothing to bound). For the minimal regular model E -> Spec(Z) of an elliptic
curve, the arithmetic analogue is the arithmetic self-intersection of the relative
dualizing sheaf with its Arakelov metric, omega-bar^2, and (Faltings adjunction,
fixed normalization) omega-bar^2 = 12 h_Fal(E). The stable Faltings height splits,
as everything in this session has split, into a finite piece and an archimedean
piece:

```
12 h_Fal(E) = log|Delta_min|  -  log ||Delta||_Pet(tau)  +  6 log(2 pi)
              (finite:            (archimedean:              (normalization
               minimal             Petersson norm of         constant)
               discriminant)       weight-12 Delta at tau)
```

with the Petersson norm `||Delta||_Pet(tau) = (2 pi)^12 (Im tau)^6 |eta(tau)|^24`,
`Delta(tau) = (2 pi)^12 eta(tau)^24`, eta the Dedekind eta function, and tau the
period point of E reduced to the SL_2(Z) fundamental domain.

## Method

Per curve (the e2h ladder: 37a1 rank 1, 389a1 rank 2, 5077a1 rank 3):

1. Period lattice via AGM. Pass to y^2 = 4x^3 - g2 x - g3 (g2 = c4/12,
   g3 = c6/216); for disc > 0 the roots e1 > e2 > e3 are real, and
   `omega_1 = pi / AGM(sqrt(e1-e3), sqrt(e1-e2))`,
   `omega_2 = i pi / AGM(sqrt(e1-e3), sqrt(e2-e3))`. mpmath at 50 decimal digits.
2. `tau = omega_2 / omega_1`, reduced to `|Re| <= 1/2, |tau| >= 1` by the standard
   translate-and-invert loop.
3. eta via the q-Pochhammer `(q;q)_inf` (full precision), then
   `||Delta||_Pet(tau)` and the assembled `12 h_Fal`.

## The normalization, pinned exactly (the factor-of-2 / 2pi slog)

The documented headache (Silverman's paper vs his books; Deligne vs LMFDB) is the
(2 pi) and factor-of-2 conventions. We pin them by an UNAMBIGUOUS internal
identity, not by citation. For the minimal Neron lattice
`L = Z omega_1 + Z omega_2`, the lattice discriminant is

```
Delta(L) = (2 pi / omega_1)^12 eta(tau)^24  =  Delta_min   (the integer)
```

and the experiment verifies this recovers 37, 389, 5077 to relative error ~1e-50.
That single check fixes the differential's normalization with no external input.
The covolume `A = Im(tau) |omega_1|^2` then gives the Deligne / LMFDB stable
Faltings height as `h_Fal(E) = -(1/2) log(A / (2 pi))`, and one verifies (the
constant is the SAME `6 log(2 pi) = 11.0272623985` for all three curves) that

```
12 h_Fal(E) = log|Delta_min| - log ||Delta||_Pet(tau) + 6 log(2 pi).
```

So the constant in the 2J display is `+ 6 log(2 pi)`. We use the Deligne / LMFDB
normalization throughout; for 37a1 it gives `h_Fal = -0.0776037`, the LMFDB value
for curve 37.a1.

## Results (actual numbers)

| curve | Delta_min | tau (reduced) | \|\|Delta\|\|_Pet(tau) | 12 h_Fal | h_Fal | archimedean share |
|---|---:|---|---:|---:|---:|---:|
| 37a1   | 37   | 1.221127i | 5777169.44 | -0.931244 | -0.077604 | 81.17% |
| 389a1  | 389  | 1.262953i | 5450834.07 |  1.479563 |  0.123297 | 72.23% |
| 5077a1 | 5077 | 1.402078i | 4278690.33 |  4.290581 |  0.357548 | 64.15% |

The three terms of `12 h_Fal` for each curve (finite, archimedean, constant):

| curve | log\|Delta_min\| (finite) | -log\|\|Delta\|\|_Pet (archimedean) | 6 log(2 pi) (const) |
|---|---:|---:|---:|
| 37a1   | 3.610918 | -15.569424 | 11.027262 |
| 389a1  | 5.963579 | -15.511279 | 11.027262 |
| 5077a1 | 8.532476 | -15.269158 | 11.027262 |

"Archimedean share" is `|log_arch| / (|log_arch| + |log_finite|)`: the fraction of
the term magnitude carried by the Petersson (archimedean) term versus the finite
(minimal-discriminant) term, with the normalization constant set aside.

## Validations

- **(i) SL_2(Z)-invariance of `||Delta||_Pet`: PASS, all three curves, relative
  error ~1e-50.** Checked against S = (0 -1; 1 0), T = (1 1; 0 1), and the
  nontrivial word TS = (1 1; -1 0). This is the SOLID internal check, and it is a
  genuine modular-symmetry fact: `(Im tau)^6 |eta|^24` is weight 0 (|eta|^24 is
  weight 12, `(Im tau)^6` is weight -12). It passes exactly to working precision.
- **(ii) Faltings-height match: MATCH for 37a1.** `h_Fal(37a1) = -0.0776037`,
  agreeing with the LMFDB value for 37.a1 to ~1e-8 (limited only by the precision
  of the recorded reference value, not the computation). The convention is pinned
  by the Delta(L) = Delta_min identity above, so this is a real cross-check of the
  normalization, not a fit. The same pinned formula gives `h_Fal(389a1) = 0.12330`
  and `h_Fal(5077a1) = 0.35755`.

## What is NEW versus a RE-CATALOGING (honest flag)

- **NEW (computational, not previously in the repo):** the explicit archimedean
  self-intersection numbers omega-bar^2 = 12 h_Fal for the three e2h curves, the
  archimedean/finite split of each, and the exact pinning of the 2J normalization
  constant to `+ 6 log(2 pi)`. 2J deliberately shipped no numerics; this closes
  that one specified-but-uncomputed entry of the Arakelov dictionary. The
  finding that the archimedean (Petersson) term carries 64-81% of the term
  magnitude (and grows in dominance as the conductor shrinks) is a new, concrete
  reading of "the archimedean place carries the self-intersection," parallel to
  2H's finding that the integral generators' good-finite local heights vanish and
  the regulator is archimedean.
- **RE-CATALOGING (the gap is unchanged):** none of this touches the universal
  gap. omega-bar^2 = 12 h_Fal is a single-arithmetic-surface SELF-intersection. It
  is the analogue of Delta^2 = 2 - 2g, a DIAGONAL entry of the would-be
  intersection form, not the polarization (M4) and not the sourcing/purity facet
  (R1). It certifies a Faltings height of a FIXED curve, computed entirely from
  that curve's own arithmetic; it says nothing about zeta's zeros. The
  height-to-L-value link is BSD (a conjecture, the central derivative at s=1), NOT
  the functional-equation Gamma-factor: per the e2ad correction, Faltings-Hriljac
  / Arakelov positivity does not connect to zeta's zeros via the analytic
  Gamma/Lambda join. So this is the "realizes a trace / Arakelov number, does not
  carry the polarization" row of the spec_z landscape, now filled in numerically
  on its archimedean side.

## Davenport-Heilbronn discipline

The D-H discipline applies vacuously here and is respected. This is an
Architecture-2 object: it intentionally requires the curve's geometry (its period
lattice, its minimal model), the exact structure D-H lacks. No positivity claim is
made that could "work" for D-H. The only positivity-adjacent statement, the
SL_2(Z)-invariance of `||Delta||_Pet`, is a modular-symmetry identity for eta, not
an RH-type inequality, so it is not a D-H-blind detector. There is no Euler-product
positivity asserted, hence nothing for D-H to falsify.

## Honest caveats

- The archimedean share (64-81%) is a magnitude reading of the two log-terms with
  the additive `6 log(2 pi)` constant set aside; it is descriptive, not an
  invariant of the curve. Reported as such. The unambiguous, citation-free anchor
  is the Delta(L) = Delta_min identity and the SL_2(Z)-invariance, both at ~1e-50.
- Validation (ii) is anchored on 37a1 (the published LMFDB value to the digits
  recorded). The 389a1 / 5077a1 Faltings heights are emitted by the SAME pinned
  formula but were not separately cross-checked against an external table here; the
  shared `6 log(2 pi)` constant across all three (verified internally) is the
  argument that the same convention holds for all three. If a future pass wants an
  independent external check, PARI `ellheight` / a Faltings-height routine would
  cross-validate 389a1, 5077a1 the way 37a1 is anchored now.
- This is the omega-bar^2 (self-incidence) diagonal. The off-diagonal incidence
  archimedean term lambda_inf (the Neron / Green's-function point-height, 2I's
  deferred next step) remains the separate uncomputed transcendental piece; 2H
  flagged it and it is not addressed here.

## Status

- **Solid:** the archimedean self-intersection omega-bar^2 = 12 h_Fal computed for
  the three curves, with the 2J normalization constant pinned to `+ 6 log(2 pi)`;
  SL_2(Z)-invariance of `||Delta||_Pet` at ~1e-50 (the solid internal check); the
  37a1 Faltings height matched to LMFDB. With 2H/2I this completes the Arakelov
  dictionary's archimedean entries on the e2h curves: incidence (lambda_inf,
  2I, deferred) and self-incidence (omega-bar^2, here, done).
- **Unchanged:** the universal gap. This is a self-intersection diagonal of a
  single arithmetic surface, the Arakelov-face analogue of the function-field
  Delta^2, computed from one curve's arithmetic and disconnected from zeta's zeros
  (the height-L link is BSD, not the Gamma-factor). It fills the "realizes the
  Arakelov number, does not carry the polarization" row numerically; it does not
  supply M4 (the polarization / signature) or R1 (sourcing / purity).

## Outputs

- `e2ae_petersson_faltings.npz`: per-curve tau, Petersson norm, 12 h_Fal, term
  split, archimedean share, invariance error.
- `e2ae_petersson_faltings.png`: the three terms of 12 h_Fal per curve, and the
  archimedean share.

## References

- Faltings, *Calculus on arithmetic surfaces* (1984); Hriljac (1985).
- Deligne, *Preuve des conjectures de Tate et Shafarevitch* (the Petersson-norm /
  Faltings-height relation and the (2 pi) normalization).
- Silverman, *Advanced Topics in the Arithmetic of Elliptic Curves* (ATAEC); the
  documented factor-of-2 caveat between his paper and books.
- Companion notes: [2J](2J_arakelov_adjunction.md) (the structural bridge this
  computes), [2H](e2h_arithmetic_hodge_index.md) (the height-pairing signature,
  archimedean point side), [2K](2K_spec_z_squared_dictionary.md) (the would-be
  product-surface dictionary), [e2ad](e2ad_fh_gamma_certificate.md) (the
  height-to-L link is BSD not the Gamma-factor).
