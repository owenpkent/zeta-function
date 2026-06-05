# 2MM: Euler-Sen K1 audit

> Companion for [`e2mm_euler_sen_k1_audit.py`](e2mm_euler_sen_k1_audit.py).
> Run: `python -m experiments.arithmetic_geometric.e2mm_euler_sen_k1_audit`.
> Result artifact: [`e2mm_euler_sen_k1_audit.npz`](e2mm_euler_sen_k1_audit.npz).

## Question

2LL showed that the Euler-Sen monodromy primitive form avoids the 2KK
diagonal-star trap:

```text
Q_N(x,y) = Omega(x, N y)
```

In the function-field model this recovers the Rosati matrix

```text
B_E(g,q,t) = [[2g, t],
              [t, 2gq]]
```

and flips exactly at the Hasse-Weil bound. The obvious K1 risk is that this is
only transport: if `B_E` is supplied as input, then `Q_N` inherits whatever
signature `B_E` already had and creates no positivity.

2MM tests that risk directly.

## Method

The experiment builds the same finite Euler-Sen package as 2LL:

```text
Omega = [[0, B], [-B, 0]]
N     = [[0, 0], [I, 0]]
Theta = -1/2 I + N
Q_N   = top^T Omega N top
```

It then sweeps arbitrary real symmetric matrices `B` with every nondegenerate
signature in dimensions `1..6`, plus one singular row per dimension. For each
row it checks:

- `Theta^T Omega + Omega Theta = -Omega` has zero residual;
- `signature(Q_N) = signature(B)`;
- the 2KK diagonal-star baseline has the expected hyperbolic signature
  `(rank B, rank B, 2 nullity B)`.

It also runs a formation guard against zeta, `chi3`, `chi4`, Davenport-Heilbronn,
and a renamed Davenport-Heilbronn wrapper. The guard reads
`L.has_euler_product`, not `L.name`, so the renamed D-H object still fails before
the cup package forms.

## Results

Signature transport sweep:

| check | result |
|---|---:|
| dimensions checked | `1..6` |
| rows checked | `32` |
| `Q_N` signature equals input `B` signature | `True` |
| transport mismatches | `0` |
| diagonal-star expected hyperbolic signature | `True` |
| diagonal-star mismatches | `0` |

Function-field anchors:

| case | input `B` signature | `Q_N` signature | diagonal-star signature | cup residual |
|---|---|---|---|---:|
| `q=5, t=4` inside Hasse-Weil | `(2,0,0)` | `(2,0,0)` | `(2,2,0)` | `0.0e+00` |
| `q=5, t=5` outside Hasse-Weil | `(1,1,0)` | `(1,1,0)` | `(2,2,0)` | `0.0e+00` |

Formation guard:

| target | forms? | expected |
|---|---:|---:|
| zeta | `True` | `True` |
| chi3 | `True` | `True` |
| chi4 | `True` | `True` |
| Davenport-Heilbronn | `False` | `False` |
| renamed Davenport-Heilbronn | `False` | `False` |

## Verdict

**K1 audit passes as a negative coordinate.**

The finite Euler-Sen primitive form is a transport formalism:

```text
signature(Q_N) = signature(B)
```

for arbitrary symmetric input `B`. It does not manufacture positivity, improve a
bad signature, or turn an indefinite form into a polarized one.

This does **not** kill the Euler-Sen proposal. It sharpens the burden:

```text
construct B geometrically from Euler/Frobenius data plus the archimedean metric,
then prove B is positive on primitive pieces without zero-side or RH input.
```

That construction and positivity theorem is exactly M4 organ (a). 2LL remains a
survival result for the monodromy formalism; 2MM prevents over-reading it as a
positivity theorem.

## Discipline Status

**K1.** The finite algebra alone does not discharge K1. If `B` is imported from
the Weil form or from known zero locations, the route is circular. A future
proof must define `B` as a geometric Euler/Rosati trace form.

**K2.** The Python guard is now data-based at the toy level: no Euler product
means no Frobenius Tate target. The renamed D-H object fails for the same reason
as D-H itself, not because of its name. This mirrors the Lean
`FrobeniusAlgebra.CanFormCupTarget` guard, but it is still a formation guard, not
an analytic proof.

**Petrov.** The defective block is retained from 2LL. Petrov non-semisimplicity
is routable in the finite Tate-centered model, but only because `B` is supplied.

**Scope.** No RH progress is claimed. The result is a structural audit of the
finite model: Euler-Sen gives the right slot for the missing polarization, but
not the polarization itself.
