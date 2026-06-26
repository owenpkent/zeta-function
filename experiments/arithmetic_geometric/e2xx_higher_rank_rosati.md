# 2XX: the higher-rank AHK/Rosati object -- where genus 1 stops being elementary

> Experiment [`e2xx_higher_rank_rosati.py`](e2xx_higher_rank_rosati.py). Builds the
> higher-rank generalization of the genus-1 primitive intersection form (e2uu/e2g),
> the object the [#122 faithfulness caveat](../../docs/03_research/research_directions/09A_ahk_arithmetic_lattice.md#6B)
> named as missing. Recorded as LEARNINGS #123. A genuine construction on the
> function-field side; it sharpens the M4 target, it does not solve M4.

## Why this experiment exists (the #122 caveat, made concrete)

The 09A AHK program localized the construction gap to **P3** (a degree map carrying
the Frobenius trace) on the genus-1 function-field shadow, where the primitive
intersection form is the 2x2 binary Gram

```
Q = [[-2g, -t], [-t, -2gq]],   negative-definite  <=>  |t| < 2 sqrt q   (the Weil bound).
```

The ADVERSARY's load-bearing correction (`scratchpad/ahk_tslot/03_adversary.md`,
LEARNINGS #122): **genus 1 is the easiest Weil case.** A 2x2 binary quadratic form is
definite iff its determinant is positive, and Hasse proved exactly this bound in 1933
from norm-form positivity, *before* Weil, with **no Hodge index theorem**. So in the
genus-1 shadow the M4 positivity (P6) looks automatic the instant P3 is supplied,
which is an **artifact**. The genuine M4 difficulty is **higher-rank Rosati positivity
(Hodge-Riemann on a >2-dimensional primitive part)**, and that is exactly what the 2x2
throws away.

Nobody in this repo had built that higher-rank object. Even
[e2g](e2g_intersection_signature.md)'s "genus-2" check uses the *same* 2x2 trace-bound
form `[[-2g,-t],[-t,-2gq]]`: it bounds only the trace `t = Tr(Frob | H^1)`, never the
higher Frobenius moments. This experiment fills that hole.

## The object (the honest higher-rank generalization of e2uu)

On `S = C x C` take the Frobenius-**power** correspondences
`c_k = Gamma_{q^k} = graph(Frob^k)`, `k = 0,...,m` (`c_0 = Delta`). On `H^1` they act
as `pi^k` (`pi` = Frobenius, Rosati involution `pi^dagger = q pi^{-1}`, `pi pi^dagger = q`).
Project out the hyperbolic plane `<e,f>` exactly as in e2g. The primitive intersection
Gram is

```
G^prim_{jk} = - M_{jk},    M_{jk} = q^k t_{j-k},   t_n = Tr(pi^n) = sum_i (alpha_i^n + (q/alpha_i)^n),
```

and the Hodge index theorem says `G^prim` is **negative-definite**, i.e. `M` is
positive-definite. Writing `alpha_i = sqrt(q) u_i` and normalizing the basis by
`q^{k/2}`, `M` is congruent to the real symmetric **Toeplitz moment matrix**

```
G_m = [ c_{|j-k|} ]_{0<=j,k<=m},    c_n = sum_{i=1}^g (u_i^n + u_i^{-n}) = (q^n + 1 - #C(F_{q^n})) / q^{n/2}.
```

Two faces, one object:

- **m = 1 is EXACTLY e2uu/e2g.** `G_1 = [[2g, c_1],[c_1, 2g]]`, `det = 4g^2 - c_1^2`,
  PD iff `|c_1| < 2g` iff `|t| < 2g sqrt q`: the trace bound, Hasse's binary form.
  **Genus 1 has nothing else** (one Frobenius pair gives only `c_0, c_1`).
- **m >= 2 is a genuine moment problem.** By the **Caratheodory-Toeplitz theorem**,
  `{ G_m PSD for all m }` iff `{ c_n are the Fourier coefficients of a positive measure
  on the unit circle }` iff `{ every u_i lies on |u| = 1 }` iff **RH for the curve**.

So the higher-rank primitive Hodge form **is** the trigonometric moment matrix of the
symmetrized Frobenius spectrum, and its definiteness is RH for the curve -- not as a
single determinant, but as a positive-definite (Toeplitz) moment sequence. That is the
">2-dimensional primitive part" the caveat named, now explicit and computable.

## What the experiment shows

1. **Genus-1 reduction (exact).** `m=1` reproduces `[[-2,-6],[-6,-50]] = [[-2g,-t],[-t,-2gq]]`
   exactly: the higher-rank object contains the old 2x2 trace-bound form as its
   degenerate rank-2 corner.

2. **The higher-rank polarization.** On RH-respecting genus-2/3 spectra (all `|u_i|=1`),
   `G_m` is PSD at every order. The form is positive semi-definite and becomes singular
   at size `2g+1` (the spectrum is a measure on `2g` points), never going negative: it
   *is* the polarization.

3. **THE HEADLINE (adversary-corrected) -- an integer genus-2 Davenport-Heilbronn
   analogue.** Take the integer "fake zeta"

   ```
   P(T) = T^4 - 4 T^3 + 15 T^2 - 20 T + 25   over q = 5
   ```

   It has integer coefficients and the **exact curve functional equation**
   (`e_3 = q e_1`, `e_4 = q^2`), but its roots are off the circle
   (`|alpha| in {1.749, 2.859}`, not `sqrt 5 = 2.236`), because the trace polynomial
   `s^2 - 4s + 5` has complex roots `2 +- i`. So **RH is false** and `P` is not the zeta
   of any curve -- the higher-genus analogue of a Davenport-Heilbronn off-line zero.
   From its first two point-count moments `c_1 = 1.789`, `c_2 = -2.800` (the data a
   genus-2 curve's `N_1, N_2` supply), the **joint** rank-3 moment form `G_2` (built from
   exactly `{c_0, c_1, c_2}`) has signature `(2,1)`, **indefinite** -- while **every 2x2
   principal sub-minor of `G_2` is positive-definite** (dets `12.8, 8.16, 12.8 > 0`; both
   the `n=1` and `n=2` trace bounds hold). So the indefiniteness is caught **only by the
   full 3x3 determinant**, by no 2x2 restriction: `G_2` is the smallest matrix exhibiting
   the genuine higher-rank Hodge-Riemann structure (indefinite, all 2x2 restrictions
   definite), invisible to the genus-1 binary form. Its **positivity** over `Z` is M4.

   **Three honest caveats (the adversary's, applied).** (i) This is **not** "higher rank
   is needed to *see* a violation": the 2x2 trace-bound **family** `{|c_n| <= 2g : all n}`
   is *also* equivalent to RH (an off-circle pair makes `c_n ~ r^n` unbounded), and it
   catches **this** violation at `n = 3` (`|c_3| = 5.01 > 2g`, needing the further point
   count `N_3`). The joint form is the **data-efficient** detector (catches at rank 3 from
   `(N_1, N_2)`), not the only one. (ii) The genuine higher-rank **difficulty is PROVING
   positivity** (= the Hodge index theorem = M4/P6), which is **untouched** and bites
   already at `(g=2, n=1)`: even the trace bound `|t| < 2g sqrt q` is no longer Hasse's
   elementary binary norm form once `g >= 2`. (iii) Control: the genuine Weil polynomial
   `T^4 - 5T^3 + 20T^2 - 35T + 49` over `q=7` (RH true) gives a PSD joint form. The object
   is correct; the discriminator is the joint **positivity**, left open.

4. **Real genus-2 curves.** Four hyperelliptic curves `y^2 = f(x)`, point-counted by
   brute force over `F_p` and `F_{p^2}`: Weil's theorem holds (`|alpha_i| = sqrt p`
   exactly), and the higher-rank moment form is the PSD polarization at every order.

5. **The higher-rank off-line flip (adversary-corrected).** Push one pair off the circle.
   The RH form is PSD with a kernel at rank `2g+1` (the spectrum is a measure on `2g`
   points); an off-line pair pushes that borderline zero negative. The corrected reading:
   the flip **rank is FLAT at the kernel size `2g+1`** across the whole near-circle range
   (`r = 1.001 .. 1.6` all flip at size 7, `g=3`), dropping below `2g+1` only when far off
   (`r=2.5` -> size 5). It does **not** climb as `r -> 1` (that earlier framing was
   withdrawn). What vanishes as `r -> 1` is the **margin** (the flipping min-eigenvalue:
   `-8.65e-06` at `r=1.001`) -- the ordinary marginal-positivity wall (#18/#19/#3J), now
   in a `(2g+1) x (2g+1)` instead of a 2x2: a **magnitude** stealth, not a rank stealth.
   The point in favour of the joint form: it detects a barely-off pair at the **fixed
   small size `2g+1`**, far sooner in point-count data than the 2x2 trace-bound family
   (which needs `n ~ 1/log r`: `n = 377` at `r=1.001`, vs the joint form's size 7).

## Honest reading: what is classical, what is the content, what is gained

- **Classical (the easy half).** `on-circle (RH) => moment matrix PSD` is one direction
  of Caratheodory-Toeplitz: a positive measure on the circle has a PSD moment matrix.
  It is a **restatement of RH-for-the-curve, not a proof.** The experiment is explicit
  about this.
- **The content (= M4).** The *other* direction -- a proof that the moment matrix **is**
  PSD **without** assuming the spectrum is on the circle -- is the Hodge index theorem
  on `C x C` = Weil's theorem = **M4 / P6**. Over `F_q` it is a theorem (geometry);
  over `Z` (the AHK lattice) it is the **open kernel**. This experiment does **not**
  prove it.
- **What is gained.**
  1. The higher-rank object the caveat *named in prose* is now **built and identified**
     (the primitive form on the Frobenius powers = the trigonometric moment matrix,
     `RH <=> all G_m PSD`, verified via Weil's intersection formula not just the genus-1
     match), and genus 1 is exhibited as its degenerate rank-2 corner.
  2. The genuine higher-rank Hodge-Riemann structure is exhibited integer-exactly: a rank-3
     form that is indefinite while all its 2x2 minors are PD (the smallest such), whose
     **positivity** is the M4 content. This is a structural fact about the object, **not**
     a claim that higher rank is needed to *see* violations (it is not -- see caveat (i)
     under the headline); the genuine difficulty is *proving* positivity, untouched.
  3. **P3 is sharpened (modestly).** The genus-1 "the degree map carries `t = t_1`" (#105)
     is too weak. The higher-rank Hodge index needs the curve's **zeta numerator `P(T)`**,
     i.e. `t_1, ..., t_g` (the first `g` point counts `#C(F_{q^n})`; the rest are
     determined by the functional equation), and P6 becomes the **joint moment-positivity
     of that `2g`-dimensional form**, not a single determinant. (For `g=1` it reduces to
     #105.) The Frobenius powers saturate at rank `2g` (Cayley-Hamilton), so "higher rank"
     here means up to `2g`; the object does not reach the full rank `rho-2` of the
     primitive part of `NS(C x C)`.

## K1 / K2 / K3

- **K1 (no zeros as input): clean.** The form is built from intersection numbers and a
  free q-symmetric spectrum; eigenvalue locations are never an input. The off-line flip
  is a hypothetical sweep of the spectrum (as in
  [`offline_flip_test.py`](../positivity/offline_flip_test.py), #96), and the headline
  witness is a fixed integer polynomial, not read off any zeros.
- **K2 (Davenport-Heilbronn): clean by construction.** D-H has no Euler product => no
  Frobenius `pi` => no q-Weil spectrum `{alpha_i, q/alpha_i}` => no Frobenius-power
  correspondences and no `NS(C x C)`: D-H instantiates **none** of the moment matrix.
  The integer fake-zeta `P` above is the *form-level* analogue of a D-H off-line zero
  (a functional equation with RH false), and the higher-rank form rejects it.
- **K3 (function-field shadow): this experiment is it, exact.** The construction lives
  entirely in the function-field world where Weil's theorem holds; the genus-1 corner
  recovers e2uu/e2g and the genus-2 corner recovers the Hasse-Weil bound plus the new
  higher-moment content.

## Scope and probability

This is construction-grade work on the AHK face of M4 (Direction
[9A](../../docs/03_research/research_directions/09A_ahk_arithmetic_lattice.md)). It builds
and identifies the higher-rank object (the trigonometric moment matrix), exhibits the
genus-1 form as its degenerate rank-2 corner, and sharpens P3 from one number (`t_1`) to
the curve's zeta `P(T)` (`t_1..t_g`). It does **not** prove the higher-rank positivity
(P6 / M4), which is open over `Z` and carries the same single-digit probability as the rest
of the 9A program; per the adversary, that positivity is the genuine difficulty and is
non-elementary already at genus 2. The durable yield is a sharper, computable, integer-exact
statement of the M4 *object*: the joint moment-positivity of the `2g`-dimensional Frobenius
form, the genuine higher-rank Hodge-Riemann problem that the genus-1 binary form (Hasse 1933)
cannot express. (BUILDER -> ADVERSARY loop: `scratchpad/higher_rank_rosati/01_adversary.md`;
verdict PASS-WITH-CORRECTIONS, all corrections applied.)

## Cross-refs

LEARNINGS #123 (this), #122 (the faithfulness caveat this answers), #105 (e2uu, the P3
localization this sharpens), #48 (the free `(1,n-1)`), #40 (`t`-blindness), #21/e2g (the
function-field Hodge-index template, genus 1-2 trace bound). Docs:
[`09A_ahk_arithmetic_lattice.md`](../../docs/03_research/research_directions/09A_ahk_arithmetic_lattice.md)
(Section 6C), [`08A_rosati_standard_conjecture.md`](../../docs/03_research/research_directions/08A_rosati_standard_conjecture.md)
(M4). Adversary report: `scratchpad/higher_rank_rosati/01_adversary.md`.

## Outputs

- `e2xx_higher_rank_rosati.npz`: the genus-1 reduction Gram, the headline witness
  moments and flip size, the real-curve point counts, and the off-line flip sizes.
