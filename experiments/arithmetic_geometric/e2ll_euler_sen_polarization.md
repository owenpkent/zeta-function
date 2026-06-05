# 2LL: finite Euler-Sen polarization probe

> Companion for [`e2ll_euler_sen_polarization.py`](e2ll_euler_sen_polarization.py).
> Run: `python -m experiments.arithmetic_geometric.e2ll_euler_sen_polarization`.
> Result artifacts: [`e2ll_euler_sen_polarization.npz`](e2ll_euler_sen_polarization.npz).
> Plotting is optional with `--plot`; it is disabled by default because the current
> local `matplotlib` binary is incompatible with NumPy 2.4.2.

## Question

The proposed new math in
[`../../docs/03_research/euler_sen_polarization_attempt.md`](../../docs/03_research/euler_sen_polarization_attempt.md)
says: do not diagonalize away Petrov non-semisimplicity. Treat it as monodromy,
then polarize primitive pieces using

```text
Q_N(x,y) = Omega(x, N y)
```

or, in the full conjectural package, `Omega(x, N^k C_E y)`.

2LL asks whether this idea dies immediately in the same way 2KK died. The cheap
kill criteria are:

- a genuine defective Sen/Jordan block must exist;
- the cup equation into `C(-1)` must be exact, not approximate;
- the primitive monodromy form must not be the rigid hyperbolic diagonal-star
  form from 2KK;
- in the function-field specialization, positivity must flip exactly at the
  Hasse-Weil/Rosati bound;
- no-Euler-product inputs must fail at formation, not by object name.

## Model

The model is deliberately function-field shaped. Given genus `g`, field size `q`,
and Frobenius trace `t`, define the positive Rosati matrix

```text
B_E(g,q,t) = [[2g, t],
              [t, 2gq]].
```

This is `-G_prim` from the 2G Hodge-index matrix. It is positive definite iff

```text
t^2 < 4 g^2 q.
```

Build a finite Euler-Sen package on

```text
H = P_top plus N(P_top)
```

with basis `top_i, lower_i`, and set

```text
N(top_i) = lower_i,      N(lower_i) = 0,
Omega(top_i, lower_j) = B_E[i,j],
Theta = -1/2 I + N.
```

Then `Theta` is genuinely defective: `N != 0`, `N^2 = 0`, and the geometric
multiplicity of the single eigenvalue `-1/2` is smaller than its algebraic
multiplicity. The Tate-center placement is the point: because both generalized
eigenvalues are `-1/2`, the cup target has weight `-1`, so the derivation equation

```text
Theta^T Omega + Omega Theta = -Omega
```

is exact.

The primitive monodromy form on top vectors is

```text
Q_N = top^T Omega N top = B_E.
```

The 2KK-style diagonal-star baseline is also computed:

```text
Q_star = Hermitian(Omega diag(+1 on top, -1 on lower)).
```

This has signature `(r,r)` whenever `B_E` is nonsingular, so it remains the
wrong-polarity hyperbolic form.

## Results

Sweep: `g = 1`, `q in {5,7,11}`, integer traces around the Hasse-Weil window.

Representative `q = 5` cases:

| case | trace `t` | cup residual | Jordan diagnostics | primitive `Q_N` | diagonal-star |
|---|---:|---:|---|---|---|
| inside Hasse-Weil | `+4` | `0.000e+00` | `rank N=2`, `rank N^2=0`, geom/alg `2/4`, defective | `(2,0,0)` positive | `(2,2,0)` indefinite |
| outside Hasse-Weil | `+5` | `0.000e+00` | same | `(1,1,0)` indefinite | `(2,2,0)` indefinite |

Full sweep:

| check | result |
|---|---|
| `Q_N` positivity matches `t^2 < 4 g^2 q` | `True` |
| mismatches | `0` |
| diagonal-star form rigidly hyperbolic on every row | `True` |
| no-Euler-product guard blocks package formation | `True` |

## Verdict

**Survives the cheap kill, as formalism.**

The monodromy primitive form is not the 2KK Hodge-star form. With a genuine
defective block centered at the Tate weight `-1/2`, the exact cup equation forms,
and `Omega(x,N y)` recovers the Euler/Rosati matrix. In the function-field model,
its positivity flips exactly at the Hasse-Weil bound. This is the correct polarity
in the only finite specialization where the right answer is known.

The diagonal-star form remains hyperbolic throughout, confirming the 2KK negative:
the diagonal star is the wrong operation. The new operation is the monodromy
primitive form.

## What this does not prove

This does **not** prove RH or construct the arithmetic polarization. The decisive
input `B_E` is supplied by hand. In the real `Spec(Z)` problem, the missing theorem
is exactly:

```text
construct B_E geometrically from Euler/Frobenius data and the archimedean metric,
then prove the corresponding primitive Euler-Sen forms are positive.
```

So 2LL moves the proposal from "probably killed by the 2KK hyperbolic trap" to
"a coherent formalism with the right function-field specialization." The gap is
now sharper, not smaller.

## Adversarial status

**K1 circularity risk.** Serious. If `B_E` is defined as the Weil form or by
zero-side positivity, the proposal is circular. A future construction must define
`B_E` as a geometric trace/Rosati form from Euler-Sen data.

**K2 D-H discipline.** Passed only at the formation-spec level: the constructor
takes `has_euler_product : bool` and refuses to form without it. This is better
than 2KK's name guard, but still a toy version of the Lean
`FrobeniusAlgebra.CanFormCupTarget` guard.

**Petrov non-semisimplicity.** Actually exercised here. `Theta = -1/2 I + N` has
a genuine nilpotent part and is not diagonalizable. Unlike 2KK, the defective
block does not destroy the cup target because it is placed at the Tate center
where two generalized eigenvalues can cup to weight `-1`.

**Function-field specialization.** Passed in the genus-1 matrix model:
`Q_N = B_E`, so positivity is exactly `t^2 < 4g^2q`, matching
[`../../lean/ZetaRH/HodgeIndex.lean`](../../lean/ZetaRH/HodgeIndex.lean)'s
`IntersectionSignature.negDef_iff_hasseWeil` after the sign flip.

## Next theorem to formalize

Formalize the pure linear algebra:

> Given a symmetric form `B`, define `H = P plus NP`, `Omega = [[0,B],[-B,0]]`,
> `N = [[0,0],[I,0]]`, and `Theta = -1/2 I + N`. Then
> `Theta^T Omega + Omega Theta = -Omega`, `N^2=0`, `Theta` is non-semisimple if
> `dim P > 0`, and the primitive monodromy form on `P` is exactly `B`.

Then specialize `B = [[2g,t],[t,2gq]]` and reuse the existing HodgeIndex proof to
obtain positivity iff `t^2 < 4g^2q`.
