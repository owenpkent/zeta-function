# 2ZZ: the archimedean/global face -- marginal positivity IS the boundary-kernel analogue

> Experiment [`e2zz_archimedean_moment_bridge.py`](e2zz_archimedean_moment_bridge.py). Option C
> of the 2026-06-26 next-steps menu, the Arakelov/archimedean side of 09A Section 5. Bridges
> the finite function-field moment problem (e2xx, #123) to the archimedean one.
> **ADVERSARY-corrected** (`scratchpad/higher_rank_faces/01_adversary.md`): the first-pass
> "disanalogy" was measured on the wrong axis and is **withdrawn and inverted**. Recorded as
> LEARNINGS #125. A reframing of #48/#96/#123/#25, not new content; P6/M4 untouched.

## The correction (what was wrong, and the right answer)

The first pass claimed a **disanalogy**: "the $\mathbb{F}_q$ on-circle moment matrix has an exact
kernel, but the archimedean Weil-form min eig **grows** with the number of zeros, so it is *not* at
a boundary." The adversary showed this is measured on the **wrong axis** and the conclusion is
**backwards**:

- **[A]** $\mathbb{F}_q$ grows the matrix **dimension** $m=1..2g+1$; the kernel appears at dim
  $2g+1$ because the Frobenius spectrum has **finite support** $2g$.
- **[B]** the first pass held the Weil-Gram **dimension fixed** at $K=\#\text{test-functions}$ and
  grew the **number of summed zeros** $n$. On-line, each zero adds a rank-1 PSD outer product to
  the fixed $K\times K$ Gram, so by Weyl the min eig is monotone non-decreasing in $n$
  **automatically** -- zero information about a kernel (AXIS 1 in the run).

On the **faithful** axis -- grow the test-function **dimension** $K$ (the analogue of
$\mathbb{F}_q$'s $m$) at a fixed large zero set -- the archimedean min eig **collapses toward 0**
($3.4\mathrm{e}{-}2 \to 3.7\mathrm{e}{-}3$, condition number $3.7\to138$; AXIS 2), and a
**truncated** zero set even gives an **exact kernel** once $K>n_{\text{zeros}}$ (min eig
$\approx-1.3\mathrm{e}{-}17$). So:

> **Marginal positivity over $\mathbb{Z}$ (the #18/#19 "no buffer" wall) IS the infinite-support
> analogue of the $\mathbb{F}_q$ boundary kernel.**

Both are the moment/Gram form sitting at the **edge of positivity** as its dimension grows. The
only (mild) difference: $\mathbb{F}_q$ reaches min eig $=0$ **exactly** at the fixed small dimension
$2g+1$ (finite support $2g$); the archimedean form approaches min eig $\to0$ **asymptotically** as
the test family is enriched (the infinite $\zeta$ spectrum, accumulation at $0$). The earlier
"disanalogy" is withdrawn.

## The surviving frame (a reframing, not new content)

- **Connection:** e2xx's finite $\mathbb{F}_q$ moment matrix is the **finite model** of the
  archimedean Weil/Li positivity. Both are **conditional** forms that **flip** off the symmetry
  locus (Level-4, e3r/#48; offline_flip_test/#96).
- **Polarity:** **Faltings-Hriljac** is **unconditionally** positive-definite, and is not
  parameterized by a zero configuration at all, so it cannot flip, so it cannot detect RH -- the
  wrong polarity (09A Section 5's "wrong signature", #22-24). This is structural, not a toy
  computation.
- **What $\Gamma_S$ adds:** the archimedean place makes the form **infinite-dimensional** (#25, the
  $(1,p)$ bidegree, the Deninger $\mathbb{R}$-flow) -- which is exactly why its boundary is
  **asymptotic** (no fixed finite kernel), not reached at a fixed small dimension like
  $\mathbb{F}_q$. The **global assembly** is the archimedean+finite balance (#23/#24, two-clock
  3M); **M4** is the open certificate that this infinite, marginal balance is a *conditional*
  (flipping) positivity.

## Honest scope

The connection and polarity taxonomy restate #48/#96/#123. The corrected **unification** (marginal
positivity = the boundary-kernel analogue) is the right reading -- recovered after the adversary
inverted the flawed first pass -- but it is a *reframing* of #18/#19 + e2xx + #25, not a new
theorem. The value is twofold: it ties the project's recurring marginal-positivity wall to the
*proven* $\mathbb{F}_q$ boundary (so "no buffer" is the correct, expected shape of the RH object,
whose function-field avatar is a theorem -- a compass reading, per the project's mindset), and it
records the wrong-axis trap (a methodological coordinate). P6/M4 (certifying the infinite
conditional positivity) is untouched.

## Cross-refs

LEARNINGS #125 (this), #123/e2xx (the finite model), #18/#19 (the marginal-positivity wall = the
asymptotic boundary, AXIS 2), #96/offline_flip_test (the flip), #48/e3r (conditional-vs-unconditional
polarity), #22-24 (Faltings-Hriljac unconditionally definite + the global balance), #25 (the $(1,p)$
bidegree = $\Gamma_S$ infinite-dim). Docs:
[`09A_ahk_arithmetic_lattice.md`](../../docs/03_research/research_directions/09A_ahk_arithmetic_lattice.md)
Section 5 (the two faces). Adversary: `scratchpad/higher_rank_faces/01_adversary.md`.
