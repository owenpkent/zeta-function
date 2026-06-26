# 2AC: chasing the H^1 -- the Spec(Z) odd operators are weight operators, not the Frobenius circle

> Experiment [`e2ac_weight_vs_frobenius.py`](e2ac_weight_vs_frobenius.py). Follow-up to #124
> (the user's pick: chase the H^1 the Tate-type matroid lacks). A **synthesis** of
> #123 + #124 + #44 + #42 + #119 + #30, **not** a new theorem. **Adversary-corrected**
> (`scratchpad/higher_rank_faces/02_adversary_e2ac.md`, PASS-WITH-CORRECTIONS). Recorded as
> LEARNINGS #126. M3/#25 untouched.

## The question

#124 (e2yy) showed a matroid Chow ring is purely **even/Tate** and has no $H^1$ where the
modulus-$\sqrt q$ Frobenius eigenvalues live. The prismatic / Sen / Deninger world is the standard
home for **odd** cohomology over $\mathrm{Spec}(\mathbb{Z})$ -- does it supply the $H^1$ with a
$\sqrt q$-Frobenius whose moment matrix (e2xx) is RH?

## The discriminator (e2xx's moment lens: circle vs line) -- = #119

e2xx (#123): RH-for-the-curve = positivity of the trigonometric **moment matrix** of the Frobenius
spectrum, which requires that spectrum on a **circle** $|\alpha|=\sqrt q$ (pure weight 1, the
functional-equation pairing $\alpha\leftrightarrow q/\alpha$). The run illustrates it: an on-circle
Frobenius spectrum gives a PSD moment matrix $(4,0)$; an off-circle (still $q$-symmetric, RH-violating)
one gives an indefinite $(2,2)$. **This is just the #119 discriminator (circle/complex vs line/real),
which e2xx already states -- not new.**

## The audit (the odd operators are weight operators, not Frobenius spectra)

| odd operator | spectrum | a $q$-symmetric Frobenius spectrum? |
|---|---|---|
| matroid grading (Lefschetz Cartan, #124) | degrees $\{0,1,\dots,r\}$ | **no** (contains 0; not FE-closed) |
| prismatic **Sen $\Theta$** (#44) | Hodge-Tate weights $\{-n\}$ | **no** (contains 0; not FE-closed) |
| prismatic **Frobenius $F$** / flow (#26/#44) | $\{\log p\}$ | **no** (orbit lengths, not FE-closed) |

These are **weights** and **orbit-lengths** (real exponents), **not** $q$-symmetric Frobenius
eigenvalues: they are not closed under $\alpha\leftrightarrow q/\alpha$, and the grading spectra even
contain $0$. So they **cannot enter the circle-Frobenius moment object at all** -- a category
mismatch (the moment formula errors on the $0$). The matroid grading and the Sen $\Theta$ are the
**same kind** of object (a real-line weight operator).

## The correction (do not flatten unequal positions)

The first pass said #124 and #44 are "one finding." The adversary corrected this: they are the same
**kind** of weight operator but **unequal positions** on the all-roads map.

- **#124 (matroid):** has no $H^1$ and does **not** even realize $\zeta$ as a trace -- the *less
  advanced* position.
- **#44 (prismatic):** carries $\Theta$ and $F$ and **does** realize $\zeta$ as a trace (both
  halves), lacking **only** the signature -- the **live M4 target**.

So **chasing the $H^1$ lands on the prismatic candidate's missing signature** = the circle-Frobenius
moment positivity = M4, viewed from the odd-cohomology side. The $H^1$-with-circle-Frobenius is *not*
a new place to look; it is the same live M4 signature gap (#25/#30), in the analytic continuation
invisible to the local line data (#42).

## Honest scope

This is a **synthesis**, not a new theorem, and -- as the project notes -- more all-roads
convergences (#30) are not where the leverage is. The Part 1 computation is an **illustration** of
#119 (a marginal-positivity caveat applies: a near-circle pair can pass at small $m$). The Part 2
"audit" is the categorical fact that weights/orbit-lengths are not Frobenius spectra. The **one
small organizing increment** is the circle-vs-line moment vocabulary applied to the odd operators,
plus the (corrected) reading that the $H^1$ chase confirms the **prismatic candidate as the live
M4 target** rather than finding a new object. M3/#25 is untouched.

K1-clean (textbook spectra; no zeros input). K2: the moment/Frobenius object needs the Euler product
D-H lacks; the $\Theta$/weight side is the D-H-shared $\Gamma$-factor (#38/#44).

## Cross-refs

LEARNINGS #126 (this), #123/e2xx (the circle requirement), #124/e2yy (matroid Tate/no-$H^1$),
#44 (prismatic $F$, $\Theta$ realize $\zeta$, lack the signature), #42 (zeros in the continuation),
#119 (circle vs line), #30 (all-roads to the signature), #25 (M3). Docs:
[`spec_z_cohomology_landscape.md`](../../docs/03_research/spec_z_cohomology_landscape.md),
[`09A_ahk_arithmetic_lattice.md`](../../docs/03_research/research_directions/09A_ahk_arithmetic_lattice.md)
Section 5. Adversary: `scratchpad/higher_rank_faces/02_adversary_e2ac.md`.
