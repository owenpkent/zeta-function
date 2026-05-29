# Reading notes: Cohen, *A Course in Computational Algebraic Number Theory* (GTM 138, 1993)

> Computational-authority ROLE-note. Folder
> [`references/07_elliptic_curve_heights/`](../../../references/README.md) (single-surface
> height machinery for Architecture 2, Direction 8). This is a 556-page reference
> textbook, NOT read cover to cover: I read the table of contents and the §7.5
> elliptic-curve height algorithms (Alg. 7.5.6 finite part, Alg. 7.5.7 archimedean
> part, plus the surrounding BSD/regulator framing pp. 386, 404-405). This note points
> the program at the exact algorithms used in experiment 2P. Pages refer to the PDF.
> Read: TOC + PDF pp. 386, 404-405 (the two height algorithms).

## One-line takeaway

Cohen §7.5 gives the two textbook algorithms that decompose the canonical height of a
point on `E/Q` into local pieces: Algorithm 7.5.6 computes the FINITE (non-archimedean)
contribution by the `A, B, C, M` valuation case-split, and Algorithm 7.5.7 computes the
ARCHIMEDEAN contribution by a theta-function / `q`-expansion series built from the real
and imaginary periods (`omega1, omega2`) and the elliptic logarithm. Their sum is
`h_hat(P)`. This is the authoritative source experiment 2P implements verbatim, and it
is the per-place decomposition whose archimedean block is the `A_arch` of Direction 8.

## The points that matter, mapped to the project

1. **Algorithm 7.5.6 (finite part of the height), PDF p. 404.** Given the global minimal
   model coefficients and a rational `P = (x, y)`, set `z = (1/2) log(den x)`,
   `A = num(3x^2 + 2a2 x + a4 - a1 y)`, `B = num(2y + a1 x + a3)`,
   `C = num(3x^4 + b2 x^3 + 3 b4 x^2 + 3 b6 x + b8)`, `N = ord_p(Delta)`, `M = min(B, N/2)`.
   The case-split (good reduction `min(A,B)<=0`; multiplicative `ord_p(c4)=0`; additive
   `C>=3B` vs else) returns the per-prime local height as a rational multiple of `log p`.
   This is exactly the FINITE block of the local decomposition `h_inf + sum_p h_p = h_hat`.
   -> This is the algorithm cited in the 2P script header ("Cohen Alg. 7.5.6/7.5.7") and
   implemented as the finite local height in
   [`e2p_silverman_local_heights.py`](../../../experiments/arithmetic_geometric/e2p_silverman_local_heights.py).
   2P's corrected attribution (the `-0.347` on the I_2 curve coming from `p=2`, not `p=11`)
   is this case-split applied prime by prime.

2. **Algorithm 7.5.7 (archimedean height at infinity), PDF p. 405.** Uses Algorithm
   7.4.7 for the periods `omega1, omega2`, Algorithm 7.4.8 for the elliptic logarithm `z`
   of `P`, then sets `lambda = 2*pi/omega1`, `t = lambda*Re(z)`, `q = e^(2*i*pi*omega2/omega1)`,
   computes the theta series `theta = sum_{n>=0} sin((2n+1)t)(-1)^n q^(n(n+1)/2)`, and
   outputs the archimedean local height from it. Cohen flags that this `q`-expansion form
   "has a faster rate of convergence" than the geometrically-converging Tate/Silverman
   series and "should be preferred for high-precision calculations" (p. 405).
   -> This is the AGM/theta archimedean height. Silverman 1997 cites it by this exact ID
   ("[3, Algorithm 7.5.7]") as the fast alternative to the Tate series. 2P's archimedean
   block (`h_inf`) and 2I's `lambda_inf` both compute this quantity; 2P validated it to
   `~1e-8` against the independent limit `h_hat`. This is the analytic `A_arch` diagonal.

3. **Algorithm 7.5.7 is built on the period lattice (Alg. 7.4.7) and the Weierstrass
   theory.** The archimedean height is a TRANSCENDENTAL object: a theta value at the
   point's elliptic logarithm, not an algebraic intersection number. The finite heights
   (7.5.6) are rational multiples of `log p`; the archimedean one (7.5.7) is genuinely
   analytic.
   -> This is the structural fact 2I made central: the archimedean place carries the
   transcendental bulk of the regulator (100% of the diagonal for integral generators),
   while the finite places are arithmetic corrections. The split `algebraic vs analytic`
   here IS the `finite vs archimedean` split of the Hodge-index decomposition.

4. **Framing: the regulator IS the height-pairing determinant (p. 386, Conj. 7.3.9).**
   Cohen states the BSD conjecture and notes the regulator `R(E/Q)` is the determinant of
   the canonical height pairing `<Pi, Pj> = h(Pi+Pj) - h(Pi) - h(Pj)` on a basis of the
   torsion-free part; he records that this pairing is "positive definite" (p. 404).
   -> This is the Faltings-Hriljac positive-definiteness the project validated in 2H/2M.
   Cohen is the computational statement of it: `det(<Pi,Pj>) = 0` iff the points are
   dependent, so positive-definiteness on the independent generators is exactly the
   signature condition Direction 8 reads off the arithmetic surface.

## What this changes for the program

- **2P is grounded in the authoritative source.** The finite case-split (7.5.6) and the
  theta archimedean series (7.5.7) are the textbook algorithms; the program can cite
  Cohen GTM 138 §7.5 as the reference implementation behind the validated
  `h_inf + sum_p h_p = h_hat` decomposition. No re-derivation needed.
- **The fast archimedean route is theta/AGM, not the Tate switch-series.** For
  high-precision archimedean local heights (the `A_arch` diagonal at large rank or large
  height), 7.5.7's `q`-expansion is the preferred algorithm. Cremona §3.4 and Silverman
  1988 give the slower geometric switch-series; Cohen/7.5.7 (= Silverman 1997's "[3]")
  is the faster one. Worth knowing if `A_arch` precision ever becomes the bottleneck.
- **Positive-definiteness of the pairing is the computational form of the signature.**
  Cohen's regulator-determinant statement is the single-surface positivity 2H/2M
  validated; the Direction-8 task is to make that determinant's sign emerge from an
  intersection form, not just from the analytic height.

## Status

- **ROLE-note, honest depth:** read the TOC and the two height algorithms (§7.5, PDF
  pp. 386, 404-405) plus the BSD/regulator framing; did NOT read the other 550 pages
  (number-field algorithms, factoring, lattice reduction) -- not relevant to the height
  decomposition. The two algorithms are transcribed accurately above and match the 2P
  implementation.
- **Used by:** experiment 2P (both algorithms, verbatim), 2I (the archimedean part,
  cross-check reference). Cited in the 2P script header and the 2I status block.
- **Direction 8 bearing:** the per-place height decomposition is the Arakelov-style
  local picture on a single arithmetic surface; the archimedean block (7.5.7) is the
  `A_arch` diagonal, the finite blocks (7.5.6) the off-diagonal arithmetic glue, and
  the positive-definiteness of their sum is the validated single-surface signature.
