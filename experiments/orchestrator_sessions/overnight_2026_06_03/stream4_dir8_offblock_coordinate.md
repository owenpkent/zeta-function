# Stream 4 (coordinate factory) -- Direction 8 candidate coordinate

> STAGED, NOT COMMITTED. Overnight run 2026-06-03. For morning review by Owen +
> main-agent verification. Nothing here is final; the numbers below must be
> independently re-derived before anything is recorded in LEARNINGS.

## The single most tractable sub-step (proposed)

**Title.** The block-diagonal-trace / off-block-signature obstruction for the
arithmetic Rosati Gram on the self-product.

**One-line claim.** When the function-field Rosati Gram is assembled over
`Spec(Z)` as a place-graded (per-prime) object, the only realizable arithmetic
datum that the project already has in hand, `Gamma_S^2 = -zeta'/zeta(s) =
sum_n Lambda(n) n^{-s}` (#26/2R/#41), is **exactly diagonal in the prime
grading** (`Lambda(n) = 0` whenever `n` has two or more distinct prime factors),
so it populates **only the within-block (diagonal-prime) entries** of the Gram and
supplies **zero cross-prime (off-block) coupling**. But the global signature
(RH) is carried precisely by the **off-block** entries. So the missing
polarization is pinned to a concrete, finite locus: the off-block bilinear
coupling between the `p`-block and the `p'`-block, which no Euler-product trace
object can reach.

This is a sharpening of the #40-#42 q-lift gap from a new, fully finite and
exactly-computable angle: it does not require the analytic continuation to
*state* the obstruction (unlike 2CC.3, which had to invoke the divergent Euler
product on `Re(s)=1/2`). It is a statement about which matrix entries are
populated by the data we already have.

## Why this is the right framing of the self-product pairing

Over `F_q`, Weil's whole proof runs on a **single** Frobenius `pi` at **one**
scale `q`. The Rosati Gram `G[a][b] = q^{min(a,b)} a_{|a-b|}` on the basis
`{1, pi, ..., pi^{2g-1}}` is built from one scale; positivity is RH-for-C (2T/#row).

Over `Spec(Z)` there is no single `q` (#25/2Q). The arithmetic Frobenius algebra
`A` is **place-graded**: scale `p` in the `p`-block (08A M2). The natural
assembly is therefore a **block-structured** Gram, blocks indexed by primes:

- the `p`-block carries the local Frobenius at scale `p` (the `(1,p)` bidegree);
- the off-block `(p, p')` entry would carry a coupling between the two local
  Frobenii.

The decisive observation: a **direct sum** `(+)_p G_p` of per-prime blocks is
**trivially positive** whenever each block is, and carries **no global
information** (no `Re(rho)=1/2` content) -- it is just `prod_p` of local
conditions, which is RH-agnostic (each local block can be made critical
independently). Therefore **all** the global / RH content must live in the
**off-block coupling**. This localizes the polarization gap to a specific set of
matrix entries.

## What to compute or obstruct (and what I already computed tonight)

COMPUTED (mpmath dps=30; commands + outputs below; MUST be re-derived before recording):

1. **Per-prime blocks are trivially positive (carry no global content).**
   Genus-1 block at scale `p` with critical trace `t=0` is `[[2,0],[0,2p]]`,
   PD. The block-diagonal sum over `p in {2,3,5,7,11,13}` has `min eig = 2.0`,
   signature `(12,0,0)`. A direct sum of local-critical blocks is PD and
   RH-agnostic: it encodes no coupling.

2. **The trace object is exactly prime-grading-diagonal.**
   `max |Lambda(n)|` over **all** `n < 2000` with `>= 2` distinct prime factors
   is `0.0` exactly. So `-zeta'/zeta = sum Lambda(n) n^{-s}` has **no** Dirichlet
   coefficient at any `n = p^a q^b` (both `a,b >= 1`). In the prime grading this
   is a strictly **block-diagonal** object. `Gamma_S^2` lives entirely on the
   diagonal-prime locus; it cannot populate the off-block entries.

3. **Anchor for the trace object.** `-zeta'/zeta(2) = 0.569960993095`
   (mpmath derivative of `log zeta`); the prime-power-supported von Mangoldt sum
   `sum_{n<40000} Lambda(n) n^{-2} = 0.569936002912`, rel err `4.4e-5`
   (converging). So the diagonal object is correctly the full `-zeta'/zeta` and
   nothing is hidden off the prime powers for zeta.

THE OBSTRUCTION (the coordinate proper). Combining (1)+(2): the only arithmetic
bilinear datum the program currently realizes (the Frobenius self-intersection
`Gamma_S^2`, = the von Mangoldt sum) is block-diagonal, hence supplies the
within-block Gram entries but **identically zero** off-block coupling. The
off-block entries are exactly where a global signature (the cross-prime
correlation that the zeros encode) must sit. So the missing polarization is not
"a number we have not computed"; it is a coupling **structurally absent** from
the Euler-product / Frobenius trace data, and must come from the
zeros/continuation (the archimedean carrier, #34/#42/2PR.1).

NEXT COMPUTE STEP (for a depth pass, not done tonight): take the explicit-formula
/ Hadamard resolvent `sum_rho 1/(s-rho)` (which IS a global functional of all
primes simultaneously) and ask whether its restriction to the `(p, p')` off-block
locus is (a) nonzero and (b) sign-definite. That is the candidate carrier of the
off-block coupling. Prediction (low confidence): it is nonzero (the zeros couple
all primes) but **not** sign-definite from the data alone -- the sign-definiteness
IS the open polarization (M4). This would be the depth follow-up.

## D-H control (K2)

For an L-function **without** an Euler product, the von Mangoldt analogue
`Lambda_L(n)` (coefficients of `-L'/L`) is **delocalized**: supported on all `n`,
including `n` with `>= 2` distinct prime factors (#20/#41; the project's
3M/2R/2CC.2 delocalization finding). So:

- **zeta** (Euler): trace object `-zeta'/zeta` is strictly prime-grading-diagonal
  (computed: `0.0` off-block, item 2).
- **D-H** (no Euler product, RH FALSE): `-L_DH'/L_DH` has **nonzero off-block
  (cross-prime) coefficients** (delocalized, #20).

This makes **prime-grading diagonality of the trace object itself a K2
discriminator at the trace level**: it is a clean, finite, exactly-checkable
property that zeta has and D-H lacks. (Honest caveat below: this discriminates at
the level of the *trace's support structure*, which is just the Euler product
restated; it does NOT by itself discriminate RH, since RH lives in the
off-block *signature*, which is open for both. The discriminator content here is
"has an Euler product," consistent with #37: a structural prerequisite, not RH.)

Note the **inversion** relative to the usual stealth-window story: here zeta is
the *clean/diagonal* case and D-H is the *messy/off-block* case, but D-H's
off-block coefficients are NOT a polarization (they are delocalized von Mangoldt
noise, mixed-sign, RH-agnostic). The point is that the off-block locus is where
the discrimination lives; supplying the *right* (sign-definite, RH-equivalent)
off-block coupling for zeta is the open problem, and D-H structurally cannot host
it (no Frobenius correspondence to couple).

## Honest scope (PROVED / COMPUTED / CITED / STRUCTURAL-READING)

- **COMPUTED (re-derive before recording):** items 1-3 above. All are elementary
  (block-diagonal eigenvalues; `Lambda(n)=0` off prime powers; the `-zeta'/zeta(2)`
  anchor). None is new mathematics; they are exact facts assembled into a new
  *localization* of the gap.
- **CITED (statement-level):** the per-prime Rosati Gram form `G[a][b] =
  q^{min(a,b)} a_{|a-b|}` and its positivity = RH-for-C (Weil 1948; project 2T).
  The `(1,p)` bidegree and `Gamma_S^2 = -zeta'/zeta` (Deninger; project #25/#26/2Q/2R).
  The D-H delocalization (#20/#41).
- **STRUCTURAL READING (the proposed coordinate):** "the polarization gap is the
  **off-block** coupling, structurally absent from the Euler-product trace data,
  and the trace object's prime-grading diagonality proves the local data cannot
  supply it." This is a reading of computed facts, NOT a theorem. It does NOT
  construct the off-block coupling, does NOT prove RH, and does NOT discriminate
  RH (only the Euler-product prerequisite).
- **What is genuinely fresh vs prior coordinates:** 2CC.3 (#42) localized the gap
  to the local-to-global *continuation* using the divergence of the Euler product
  on `Re(s)=1/2` (an analytic statement). THIS coordinate localizes the same gap
  to a **finite, exactly-computable, algebraic** statement: the trace object is
  block-diagonal in the prime grading, so the missing coupling is off-block. It
  is the *matrix-entry* form of the same gap, which is more directly
  Lean-formalizable (a support statement about `Lambda(n)`) and gives a sharper
  target for a depth pass (the resolvent restricted to the off-block locus).

## Verification targets (for VERIFIER)

- **V1 (finite, formalizable).** `forall n, (number of distinct prime factors of
  n >= 2) -> vonMangoldt n = 0`. This is the "trace object is prime-grading
  diagonal" fact. Mathlib has `ArithmeticFunction.vonMangoldt`; the support
  statement should be close to existing lemmas (`vonMangoldt_apply`,
  `isPrimePow` characterization). This is the load-bearing exact fact.
- **V2 (linear algebra).** A finite block-diagonal real symmetric matrix is
  positive (semi)definite iff each block is. (Direct sum of forms; standard.)
  Establishes that the per-prime direct sum carries no global content.
- **V3 (definitional).** State the place-graded Gram assembly: `G = (diagonal
  blocks G_p from local Frobenius) + (off-block coupling C_{p,p'})`, and record
  `C` as the open object (the polarization). This is a definition + an
  `open`/`sorry` for `C`, wiring to `LambdaBlueprints.lean` /
  `HodgeIndex.lean`.

## Adversarial test cases (for ADVERSARY)

- **A1 (circularity, K1).** Check that the claim does not secretly assume RH: the
  diagonality of `Lambda` is the Euler product (a theorem, no RH input); the
  "off-block carries the signature" is a structural reading, not derived from
  zero locations. Confirm no zero data enters.
- **A2 (D-H, K2).** Verify D-H's `-L'/L` has nonzero off-block coefficients
  (delocalization, #20). Then check the honest caveat holds: this discriminates
  "has Euler product," NOT RH (D-H's off-block coeffs are mixed-sign von Mangoldt
  noise, not a failed polarization). Do NOT let the coordinate overclaim K2
  discrimination of RH.
- **A3 (is the off-block locus really empty for the trace?).** Stress the item-2
  computation to larger `n` and to the second log-derivative `(-zeta'/zeta)' =
  sum Lambda(n) log(n) n^{-s}` (still prime-power supported -> still diagonal).
  Confirm no realizable Euler-product trace object populates the off-block locus.
- **A4 (does the resolvent actually couple primes?).** The depth claim is that
  `sum_rho 1/(s-rho)` couples all primes (via the explicit formula). Stress
  whether its off-block restriction is nonzero and whether it is sign-definite
  (predicted nonzero, NOT sign-definite from data alone -- the open M4). This is
  the test that would either promote or kill the depth follow-up.

## Commands run tonight (for independent re-derivation)

```
# FACT 1 + FACT 2 (block positivity + prime-grading diagonality of vonMangoldt)
python -c "<block-diag eigvalsh of g1_block(p,0) over p in {2,3,5,7,11,13};
            max|vonMangoldt(n)| over n<2000 with >=2 distinct prime factors>"
#   -> min eig 2.0, sig (12,0,0);  max off-block |Lambda| = 0.0

# ANCHOR (-zeta'/zeta(2) vs von Mangoldt sum)
python -c "<-mp.diff(log zeta, 2) vs sum_{n<40000} Lambda(n) n^-2>"
#   -> 0.569960993095 vs 0.569936002912, rel err 4.4e-5
```

(The exact inline scripts are reproduced in the Stream-4 transcript; they are
elementary and self-contained, using only mpmath and numpy/scipy.)
