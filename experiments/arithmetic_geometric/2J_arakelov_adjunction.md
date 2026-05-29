# 2J: arithmetic adjunction and the archimedean self-intersection

> Companion to [2K](2K_spec_z_squared_dictionary.md). 2K maps the trace-formula
> data to the would-be intersection NUMBERS on `Spec(Z) x Spec(Z)`. This note
> covers the distinct ingredient 2K does not: the arithmetic ADJUNCTION /
> SELF-intersection (`Delta^2`, the dualizing sheaf), the analogue of the
> function-field `Delta^2 = 2 - 2g`, and pins where the archimedean Green's
> function enters the self-intersection number.

## The function-field ingredient to lift

In 2G the self-intersections `Delta^2 = 2 - 2g` and `Gamma^2 = q(2 - 2g)` come from
ADJUNCTION on `C x C`: `Delta^2 = deg(N_{Delta}) = deg(T_C) = 2 - 2g`, i.e. the
self-intersection of a section equals the degree of its normal bundle, governed by
the canonical class `K`. These self-intersections are what make 2G's primitive Gram
matrix non-degenerate; without `Delta^2 = -2g` (after projecting out the fibres) the
Hasse-Weil bound `4 g^2 q - t^2 > 0` would have nothing to bound.

## The arithmetic analogue (Arakelov / Faltings-Hriljac)

For a single arithmetic surface (the minimal regular model `E -> Spec(Z)` of an
elliptic curve), arithmetic intersection theory (Arakelov, Faltings, Gillet-Soule)
DOES give self-intersections. The key one is the arithmetic self-intersection of the
relative dualizing sheaf `omega-bar^2` (with its Arakelov metric), the arithmetic
adjunction. For an elliptic curve this is essentially `12 h_Fal(E)` (up to a fixed
normalization), where `h_Fal` is the (stable) Faltings height. And `h_Fal` splits,
exactly as everything in this session has split, into a finite and an ARCHIMEDEAN
piece:

```
12 h_Fal(E) = log |Delta_min|              -  log || Delta ||_Pet (tau)   +  const
              (finite: minimal              (archimedean: Petersson norm
               discriminant, the             of the weight-12 discriminant
               product of bad-prime          modular form at the period
               contributions)                point tau)
```

with the Petersson norm `|| Delta ||_Pet(tau) = (Im tau)^6 |Delta(tau)|`,
`Delta(tau) = (2 pi)^{12} eta(tau)^{24}`, and `tau` the period point of `E`. The
archimedean term is a Green's-function / Petersson-metric quantity on `E(C)` --
exactly the kind of transcendental archimedean contribution that 2I already
exhibited at the level of point-heights (`lambda_inf`), now at the level of the
SELF-intersection of the canonical class.

## The bridge this completes

Putting 2J with 2K and 2I:

| C x C ingredient (2G) | arithmetic analogue | where the archimedean piece lives |
|---|---|---|
| `Gamma . Delta = N_n` | prime side `P_fin` (2K) | -- (finite) |
| `Delta . O` (section meets section) | Neron local height (2I) | `lambda_inf` = Arakelov Green's `g(P,O)` |
| `Delta^2 = 2-2g` (adjunction) | `omega-bar^2 = 12 h_Fal` (this note) | Petersson norm `||Delta||_Pet(tau)` |
| fibre plane `{e,f}` (hyperbolic) | pole block `B_pole` (2K) | -- |

So every structural ingredient of the 2G Hodge-index computation has an identified
arithmetic analogue, and in every case the archimedean place enters through a
transcendental metric quantity (Green's function for incidences `lambda_inf`;
Petersson norm for self-incidence `omega-bar^2`). The arithmetic Hodge index theorem
(Faltings-Hriljac, 2H) shows the resulting pairing on a SINGLE arithmetic surface
has the right signature. What is still missing is only the PRODUCT surface
`Spec(Z) x Spec(Z)` (2K section 4).

## Status and the concrete numerical follow-up

- This note is a rigorous structural bridge (no new numerics shipped, deliberately,
  to avoid a period-computation normalization slog of the kind 2I's factor-of-2
  warned about).
- The clean, validatable numerical next step: compute the period point `tau` of each
  curve (via the AGM / complete elliptic integrals in mpmath), evaluate the
  Petersson norm `||Delta||_Pet(tau)` and hence the archimedean part of
  `12 h_Fal`, and VALIDATE: (i) SL_2(Z)-invariance of `||Delta||_Pet` (an internal
  check), and (ii) the assembled `h_Fal(E)` against known Faltings heights. This is
  the `omega-bar^2` companion to 2I's validated `lambda_inf`, and the literal
  computation of "the archimedean Green's function entering the self-intersection
  number."

## References

- Faltings, *Calculus on arithmetic surfaces* (1984); Hriljac (1985).
- Arithmetic adjunction / `omega-bar^2`: Gillet-Soule; Bost.
- Faltings height & Petersson norm of `Delta`: standard (e.g. Silverman ATAEC,
  Deligne "Preuve des conjectures de Tate et Shafarevitch").
