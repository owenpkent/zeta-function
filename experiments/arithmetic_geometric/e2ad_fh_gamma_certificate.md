# 2AD: the Arakelov-face certificate, re-cataloged through the moment lens

> Experiment [`e2ad_fh_gamma_certificate.py`](e2ad_fh_gamma_certificate.py). The Arakelov face of
> M4 (the #125 follow-up, the user's pick). **ADVERSARY-corrected**
> (`scratchpad/higher_rank_faces/03_adversary_e2ad.md`, PASS-WITH-CORRECTIONS): two cute first-pass
> identifications are **withdrawn**. Recorded as LEARNINGS #127. A **re-cataloging** of
> #25/#44/#125/#30, **not** a new theorem; M4/#25 untouched. The weakest of the 2026-06-26 probes.

## What this is (and is not)

The first pass tried to make the "Faltings-Hriljac + $\Gamma_S$ global-assembly certificate" precise
by splitting the e2xx moment Gram into a "height entry" (= FH) and a "Frobenius off-diagonal", and
claiming $\Gamma_S$ assembles them. The adversary showed **two of those moves are unsound** and they
are withdrawn. What remains is one correct computation and one weak-form refinement of #125.

## What survives

1. **The per-prime Frobenius computation is correct.** For the real curve 389a1 (rank 2),
   $a_p=p+1-\#E(\mathbb{F}_p)$ is Hasse-bounded for every $p$, with $a_p^2-4p<0$ (complex roots = the
   per-prime circle $|\alpha|=\sqrt p$, the per-prime RH, Hasse 1933). The circle radius $\sqrt p$
   changes with $p$ -- 11 distinct scales across the first 11 primes -- the $(1,p)$ place-dependent
   bidegree (#25).

2. **One weak-form refinement of #125.** In the e2xx **normalized** moment matrix $[c_{|j-k|}]$, the
   **diagonal** is the uniform **norm** $c_0=2g$ (unconditional) and the RH-detecting **flip** lives
   entirely in the **off-diagonal** Frobenius coupling $c_1=t/\sqrt q$ (conditional). So
   Faltings-Hriljac being **unconditionally positive-definite** (#22-24, #125) is "the right shape
   for a **norm**", **not** "the wrong shape": it is the arithmetic analogue of the moment matrix's
   unconditional norm structure, and the RH content is the off-diagonal Frobenius coupling. (This is
   the Arakelov-side analogue of e2yy's wrinkle.)

## What is withdrawn (the adversary's kills)

- **"FH = the $(0,0)$ entry $\Delta_0^2=-2g$" -- type mismatch.** FH is an $r\times r$
  **positive-definite** regulator (389a1: rank 2, regulator $\approx0.1525$); $\Delta_0^2=-2g$ is one
  **negative** number on a product surface. FH is the analogue of the **whole** normalized PD moment
  structure, not a single entry. And the un-normalized asymmetry $\Delta_0^2=-2g$ vs
  $\Gamma_0^2=-2gq$ is just the un-divided $q$-scale (the $(1,q)$ bidegree), **not** a
  height-vs-Frobenius decomposition -- after normalization the diagonal is uniformly $2g$.
- **"$\Gamma_S$ assembles the FH height" -- misattribution.** $\Lambda(E,s)=N^{s/2}(2\pi)^{-s}
  \Gamma(s)L(E,s)$ joins the **finite primes** (the Euler product, the $a_p$) with the
  **archimedean** place ($\Gamma_S$) -- i.e. the **Frobenius** side -- as a **trace**. It does
  **not** contain the Néron-Tate **height**; the height-to-$L$ link is **BSD** (the central
  value/derivative at $s=1$, a conjecture), **not** the functional-equation $\Gamma$-factor.

## The gap (= #25, restated)

Assembling the per-prime Frobenius couplings (scale $\sqrt p$ each) into **one signed pairing** at a
single compatible scale is the place-dependent $(1,p)$ bidegree obstruction (#25), re-narrated as
"the signed-pairing assembly across per-prime scales." It adds **no localization** beyond #25/#44.
The analytic join ($\Gamma_S$/$\Lambda$) exists; the signed-pairing join (the Weil cohomology / the
moment positivity over $\mathrm{Spec}(\mathbb{Z})$) is **M4/#25, untouched.**

## Honest scope

This is the weakest of the four 2026-06-26 probes: a re-cataloging of #25/#44/#125/#30 in
moment-Gram vocabulary, with **no new theorem, object, or localization**. The genuine content is the
correct $a_p$ computation and the weak-form #125 refinement (FH unconditionally PD = the right shape
for a norm; the flip is off-diagonal). It confirms the project's own caution that more all-roads
re-cataloging is not where the leverage is. M4/#25 is untouched.

K1-clean ($a_p$ intrinsic; no zeros input). K2: the Frobenius/Euler part is what D-H lacks; the
$\Gamma_S$/archimedean part is D-H-shared (#38/#44).

## Cross-refs

LEARNINGS #127 (this), #125 (the archimedean face this weakly refines), #22-24 (FH height PD), #25
(the $(1,p)$ bidegree = the scale mismatch), #30 (trace vs signature), #44 ($\Gamma_S$ / the
prismatic operators), #123/e2xx (the moment Gram), Hasse 1933 (the per-prime bound). Adversary:
`scratchpad/higher_rank_faces/03_adversary_e2ad.md`. Docs:
[`09A_ahk_arithmetic_lattice.md`](../../docs/03_research/research_directions/09A_ahk_arithmetic_lattice.md)
Section 5.
