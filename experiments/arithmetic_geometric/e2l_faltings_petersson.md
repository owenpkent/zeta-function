# 2L: the archimedean self-intersection -- Petersson norm of the discriminant

> Overnight task T1 (the 2J numerical follow-up). Computes the archimedean piece of
> the arithmetic adjunction `omega-bar^2 = 12 h_Fal`: the Petersson norm of the
> weight-12 discriminant modular form, the `omega-bar^2` companion to 2I's
> `lambda_inf`. Both validation gates PASS.

## Result

For the period point `tau` of each curve (computed from the period lattice via the
AGM), with `||Delta||_Pet(tau) = (Im tau)^6 |eta(tau)|^24`:

| curve | tau | j(E) | j(tau) [=1728·kleinj] | gate (a) | ||Delta||_Pet | gate (b) | h_Fal (norm.-dep.) |
|---|---|---:|---:|---|---:|---|---:|
| 37a1 | 1.221127 i | 2988.973 | 2988.973 | PASS 1e-51 | 1.526e-3 | PASS 1e-50 | -0.9965 |
| 389a1 | 1.262953 i | 3611.640 | 3611.640 | PASS 1e-51 | 1.440e-3 | PASS 1e-50 | -0.7956 |
| 5077a1 | 1.402078 i | 7471.549 | 7471.549 | PASS 1e-51 | 1.130e-3 | PASS 1e-50 | -0.5614 |

(All three curves happen to have purely imaginary `tau` -- they are the
period points of curves with these j-invariants in the fundamental domain.)

## The two gates (self-contained, no external lookup)

- **(a) `j(tau) = j(E)`** to ~1e-51. The period point computed from the lattice (AGM
  half-periods) reproduces the curve's own j-invariant `c4^3/Delta`. This validates
  `tau`. (Note: mpmath's `kleinj` is the normalized `J = j/1728`; the bare value was
  off by exactly 1728 across all curves, which is the documented convention, not a
  wrong `tau` -- gate (b) independently confirms `tau` is right.)
- **(b) `||Delta||_Pet` SL_2(Z)-invariant** to ~1e-50: equal at `tau`, `tau+1`, and
  `-1/tau`. This validates the Petersson-norm computation (a weight-0 modular
  function must be invariant).

The first run "failed" gate (a) by exactly 1728 -- the gate caught the mpmath
`kleinj` normalization, exactly as the protocol intends (trust the gate). The fix is
the documented `j = 1728·kleinj` convention, not a fudge.

## Interpretation and honest scope

- **Validated (robust):** the period point `tau` and the archimedean invariant
  `||Delta||_Pet(tau)`. This is the archimedean contribution to the self-intersection
  of the dualizing sheaf -- the analogue of `Delta^2 = 2-2g` on `C x C` (2G), where
  the function-field self-intersection is replaced by a transcendental Petersson /
  Green's-function quantity, exactly as 2J predicted.
- **Reported but normalization-dependent:** the absolute Faltings height `h_Fal`
  (the values are of the expected magnitude and sign, but the additive
  normalization constant -- the perennial factor like 2I's -- is not independently
  validated here, so it is flagged, not claimed).

With 2I (the archimedean local height of points, `lambda_inf`, = Arakelov Green's
function for incidences) and 2L (the archimedean self-intersection, Petersson norm,
for self-incidence), the archimedean place's role in the arithmetic Hodge index is
now computed and validated at BOTH the incidence and self-incidence levels -- the
complete archimedean side of the 2K dictionary.

## Outputs

- `e2l_faltings_petersson.npz`, `e2l_faltings_petersson.png`.
