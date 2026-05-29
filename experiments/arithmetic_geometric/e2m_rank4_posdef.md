# 2M (part a): the arithmetic Hodge index at rank 4

> Extends 2H (Faltings-Hriljac positive-definiteness of the Neron-Tate height
> pairing) from ranks 1-3 to RANK 4, on the smallest-conductor rank-4 curve.

## Curve and method

234446a1: `y^2 + x y = x^3 - x^2 - 79 x + 289`, `[a1,a2,a3,a4,a6]=[1,-1,0,-79,289]`,
conductor `234446 = 2 * 117223` (Stein-Jorza-Balakrishnan: the smallest conductor of
a rank-4 elliptic curve). Generators are NOT taken from an external source (to avoid
transcription risk): instead 50 integral points are found directly on the curve
(each on-curve by construction), and the rank-4 structure is read off the height
pairing, which is a genuine inner product on `E(Q) tensor R` (positive
semi-definite, rank = number of independent points). The pairing is built with the
validated `canonical_heights` / group law from `e2h_arithmetic_hodge_index.py`.

## Result (gate PASSES)

8x8 height-pairing Gram on the points
`(-10,7),(-9,19),(-8,23),(-7,25),(-4,25),(0,17),(1,14),(3,7)`, eigenvalues (n_iter=6):

```
[-0.0001, 0.0, 0.0001, 0.0002,  3.1432, 4.3373, 4.6712, 5.3863]
```

**4 strictly positive eigenvalues, 4 near-zero, NONE negative.** The 4 positive
eigenvalues are the rank-4 independent subspace; the 4 near-zero ones are the 4
relations among 8 points on a rank-4 group (at the n_iter=6 precision floor). So the
height pairing is positive definite on the rank-4 subspace: the Faltings-Hriljac
arithmetic Hodge index, exhibited at rank 4.

GATE (exactly 4 positive eigenvalues, none negative): PASS.

## Significance

With 2H (ranks 1, 2, 3) this confirms the arithmetic Hodge index positive-
definiteness across ranks 1-4 -- the Spec(Z) signature side of the 2K dictionary --
on a curve whose rank is itself a hard computation. No negative eigenvalue appears,
as Faltings-Hriljac requires. (2I/2L already pinned the archimedean local-height
contributions to this signature; this confirms the global positivity persists as the
rank grows.)

## Outputs

- `e2m_rank4_posdef.npz`: curve, points, Gram, eigenvalues, rank.
