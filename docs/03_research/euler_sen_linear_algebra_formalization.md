# Euler-Sen Linear Algebra Formalization

Status: formal core added in `lean/ZetaRH/EulerSenLinearAlgebra.lean`.

This is the reusable finite linear algebra package behind experiment 2LL.  For
an arbitrary real matrix `B` on a finite primitive index type `P`, the Lean file
defines

- `omega B = [[0, B], [-B, 0]]` on `P plus P`,
- `monodromy P = [[0, 0], [I, 0]]`,
- `theta P = -1/2 I + monodromy P`,
- `primitiveForm B`, the top-left block of `omega B * monodromy P`.

The formal theorems prove:

- `monodromy_sq_zero`: `N * N = 0`.
- `theta_sub_scalar`: `Theta - (-1/2) I = N`.
- `theta_nilpotent_part_sq_zero` and `theta_nilpotent_part_ne_zero`: the
  nilpotent part is square-zero and nonzero when `P` is nonempty.  This is the
  finite Jordan-block witness; the file does not attempt to formalize a full
  semisimplicity API.
- `theta_cup_derivation`: `Theta^T * omega B + omega B * Theta = -omega B`.
- `primitiveForm_eq`: the primitive monodromy form is exactly `B`.

The function-field specialization defines

```text
B_E(g,q,t) = [[2g, t], [t, 2gq]]
```

and proves `B_E = -Gprim`, where `Gprim` is the existing primitive
intersection matrix in `HodgeIndex`.  It then proves
`rosatiPos_iff_hasseWeil`, reusing
`HodgeIndex.IntersectionSignature.negDef_iff_hasseWeil` after the sign flip.

What this does not prove: it does not construct the arithmetic `B_E` over
`Spec Z`, and it does not claim RH progress.  The formal result isolates the
next real gap sharply: construct the Euler/Frobenius plus archimedean-metric
matrix `B_E` geometrically, without importing zero-side positivity or a Weil
form by definition.
