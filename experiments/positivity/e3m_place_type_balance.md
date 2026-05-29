# 3M: the input-side place-type decomposition of Weil's quadratic form

> Experiment [e3m_place_type_balance.py](e3m_place_type_balance.py). Attacks RH
> from the framing of [`docs/03_research/new_mathematics.md`](../../docs/03_research/new_mathematics.md)
> sections 2.2 and 4.2: the positivity that proves RH must come from treating the
> archimedean place and the finite primes uniformly, and from input the proof is
> allowed to use. This experiment builds the place-type split of the Weil form and
> reports what is solid, what is provisional, and what the remaining gap is.

## Motivation: answer-side vs input-side

The project's sharpest positivity result, the Schur two-clock decomposition
([LEARNINGS](LEARNINGS.md) #18), splits the Weil Gram matrix as

```
M = M_on + M_off
```

by sorting each zero's contribution by WHERE the zero sits (on the critical line
or off it). This is **answer-side**: it uses the location of the zeros. As a route
to a *proof* it is circular, since one may not use the conclusion (zeros on the
line) as an input. [LEARNINGS](LEARNINGS.md) #19 recorded the consequence: the
disproof angle in the Gram-matrix family has "no leverage point", and a productive
attack needs a fundamentally different, non-circular diagnostic.

This experiment supplies the non-circular alternative. The **same** quadratic form

```
M_ij = sum_rho  Phi_{b_i}(rho) Phi_{b_j}(rho)        (zero side)
```

decomposes a second way, by **place type**, via Weil's explicit formula:

```
M  =  A_arch   +   P_fin    +   B_pole
      |             |             |
      Gamma factor  Dirichlet     poles of the completed L
      (digamma      coefficients  (zeta & Epstein have them;
       kernel)      (Euler/prime  D-H is entire -> 0)
                     side)
```

Every block is computable **from the Gamma factor and the Dirichlet coefficients
alone, without locating a single zero**. That is the whole point: an input-side
decomposition is legitimate for a proof. The Weil criterion `M >= 0` (<=> RH)
becomes "the archimedean and prime blocks together stay positive semidefinite",
checkable input-side.

Test family: `Phi_b(s) = 2 sinh((s-1/2) log b)/(s-1/2)`, the same Mellin-symmetric
boxcar family used in 3C-3J. On the line, `Phi_b(1/2+it) = 2 sin(t log b)/t` is the
Fourier transform of the additive indicator `h_b = 1_{[-log b, log b]}`, so the
finite block uses the cross-correlation overlap of two such indicators, and the
prime sum truncates automatically at `n <= b_i b_j`.

## What is solid (validated)

### The finite block P_fin and pole block B_pole reproduce 3F exactly

The von-Mangoldt analogue `Lambda_L(n)` (coefficients of `-L'/L = sum Lambda_L(n) n^{-s}`)
is built from the Dirichlet coefficients by the standard recursion
`a_n log n = sum_{d|n} Lambda_L(d) a_{n/d}`. The diagonal of `P_fin` then matches
3F's independently-derived prime sum, and `B_pole` matches 3F's boundary term
`8(sqrt(b) - 1/sqrt(b))^2`, to floating point. These two blocks are correct.

### The Euler-product fingerprint (cancellation-free, the headline result)

`Lambda_L(n)` makes the missing Euler product **visible and quantitative**. Computed
input-side from the periodic / representation-number coefficients (n <= 200, prec 30):

| L | a_1 | # n with Lambda_L(n) != 0 | # supported on **composite** n | first composite n |
|---|---:|---:|---:|---:|
| zeta | 1 | 60 | **0** | none |
| Davenport-Heilbronn | 1 | 121 | **64** | **6** |
| Epstein d=47 (non-principal) | **0** | n/a | n/a | n/a |
| Epstein d=47 (principal) | 2 | (computable) | (computable) | - |

For zeta, `Lambda_zeta(n)` lives **only on prime powers** with `Lambda(p^k) = log p > 0`:
the Euler product, exactly. For Davenport-Heilbronn there is no Euler product, so
`Lambda_DH(n)` spills onto composite integers, starting at `n = 6 = 2*3` (a non-prime
power), with 64 such terms below 200 and magnitude up to ~6.8.

This is the precise input-side mechanism the framing document
([`new_mathematics.md`](../../docs/03_research/new_mathematics.md) section 2.2)
points at: the finite block of the Weil form receives contributions from composite
`n` for D-H that are simply absent for any Euler product. It localizes WHERE in the
explicit formula a non-Euler L-function's off-line obstruction originates: the
composite-`n` terms of the prime block. It is cancellation-free (no large-number
subtraction), so it is the robust part of the place-type decomposition.

**Epstein subtlety.** The reduced non-principal form `2m^2 + mn + 6n^2` never equals
1, so `r_Q(1) = a_1 = 0`: the Epstein zeta of a non-principal form is not a standard
`a_1 = 1` Dirichlet series, and the `-L'/L` recursion (which inverts `a_1`) does not
apply directly. This is a genuine structural wrinkle for porting the place-type
split to Epstein, recorded here for the next pass.

## What is provisional (the diagnosed gap)

### The archimedean block A_arch has an isolated normalization error

`A_arch` is computed in frequency space as
`A_ij = (1/2pi) int Phi_{b_i}(1/2+it) Phi_{b_j}(1/2+it) Omega_L(t) dt` with the
uniform digamma kernel `Omega_L(t) = 2 log Q + sum_j [Re psi(1/4 + mu_j/2 + it/2) - log pi]`.
Compared against 3F's independently-validated Bombieri-form archimedean integral
(`const + gamma_int`), this block:

- matches to **0.2%** at the upper end of the b range (b ~ 6), but
- carries a **converged ~0.06 absolute offset** at small b (verified stable as the
  integration cap t_cap -> 20000, so it is NOT a truncation tail; it is a genuine
  normalization discrepancy isolated to A_arch).

Because the full Weil form `M ~ 0.08` is a tiny cancellation residue of blocks of
size ~60 (the archimedean cushion and the prime obstruction nearly cancel, as 3F
already observed), a ~0.06 error in A_arch swamps M. So the **input-side minimum-
eigenvalue detection of D-H's off-line failure is not yet trustworthy** and is
reported as provisional. The concrete fix is to compute A_arch from the bilinear
generalization of 3F's validated Bombieri-form integral, per L-function's own Gamma
factor (zeta: `mu = {0}`, Q = 1; D-H: `mu = {1}`, Q = sqrt 5; Epstein: `mu = {0,1}`),
rather than from the frequency kernel.

### The zero side is a poor validator

The zero-side `M` converges only as ~1/T_max (the tail of `sum_rho Phi^2`), so the
self-check `||A+P+B - M|| / ||M||` is dominated by zero truncation unless T_max is
very large. Validation should instead go through 3F-style input-side methods, which
have no truncation. (At T_max = 200 the apparent residual plateaus near 14% purely
from zero truncation; this is not a statement about the blocks.)

## The structural finding (marginal positivity, sharpened)

The cancellation budget is itself the result. D-H's raw off-line obstruction is
about **-2.6%** of the largest eigenvalue ([LEARNINGS](LEARNINGS.md) #10), which is
the **same order as the archimedean-minus-prime cancellation residue** in the
explicit formula. So the off-line obstruction is buried at exactly the scale of the
cancellation: it is invisible to a soft input-side reconstruction (which must
subtract two ~60-sized blocks to ~0.08) and becomes visible only with either exact
(rational) arithmetic on the explicit-formula blocks or the answer-side projection
of 3J (which manufactures the 30x sharpening, asymptote -78.7%, by projecting onto
`range(M_off)` -- an answer-side move).

This is a new, sharp instance of the marginal-positivity thesis and explains
**why** [LEARNINGS](LEARNINGS.md) #19's "fundamentally different diagnostic" is hard
to build: any input-side positivity certificate for the Weil form must resolve a
signal sitting beneath the archimedean-prime cancellation floor. A working proof
must therefore engage the exact arithmetic of the blocks (the Euler product made
the prime block supported on prime powers; the off-line obstruction lives in the
composite-`n` terms that an Euler product forbids), not their floating-point
difference.

## Status and next step

- **Solid:** the place-type machinery; the validated `P_fin` and `B_pole` blocks;
  the cancellation-free `Lambda_L` composite-support fingerprint (zeta 0, D-H 64,
  first at n=6); the cancellation-budget finding.
- **Provisional:** the input-side minimum-eigenvalue detector, pending a correctly
  normalized archimedean block.
- **Next:** replace the frequency-form `A_arch` with the bilinear Bombieri-form
  archimedean integral derived per L-function Gamma factor; handle the Epstein
  `a_1 = 0` normalization; then test whether the input-side reconstruction resolves
  D-H's `-2.6%` below a `< 1%` self-consistency floor. This is a contained
  derivation-plus-numerics task (BUILDER/VERIFIER-scale).

## Outputs

- `e3m_place_type_balance.npz`: per-L blocks, residuals, eigenvalue summaries.
- `e3m_place_type_balance.png`: input-side vs zero-side min eigenvalue; self-check residual.
