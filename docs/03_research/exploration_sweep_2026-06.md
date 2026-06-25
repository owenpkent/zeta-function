# Session synthesis: the four-area exploration sweep (June 2026)

> Consolidation of a single research session that swept four further areas of math/physics for a tool
> that could supply M4 (the arithmetic Hodge standard conjecture / the indefinite polarization on the
> Frobenius side of Spec(Z)). All four CLOSE. Companion to
> [`eight_angle_sweep_2026-06.md`](eight_angle_sweep_2026-06.md) (the prior eight-angle sweep),
> [`all_roads_to_the_signature.md`](all_roads_to_the_signature.md) (the convergence ledger), and
> [`spec_z_cohomology_landscape.md`](spec_z_cohomology_landscape.md) (the scorecard). Raw dossiers:
> `scratchpad/explore_2026-06/{lorentzian_polynomials,susy_witten_index,index_theory,condensed_analytic}.md`.

## The one-paragraph finding

The sweep deliberately did **not** look for another framework that realizes $\zeta$ as a trace (those
are abundant and all stop at the same wall). It looked for a **proven indefinite-positivity tool of the
right polarity**, or a substrate that could carry the polarization. Four areas were assessed against the
project's disciplines (Davenport-Heilbronn, the e3r wrong-polarity test, the L-value/order-of-vanishing
disqualifier, the R3.5/K1 wall): **Lorentzian polynomials / Alexandrov-Fenchel** (the modern Hodge-Riemann
engine), **supersymmetric QM / the Witten index** $\mathrm{Tr}(-1)^F$, **index theory** (Atiyah-Singer /
Lefschetz / eta / Hirzebruch signature), and **condensed/analytic geometry** (Clausen-Scholze, the
six-functor formalism over an analytic Spec(Z)). All four CLOSE, and they close in the same shape:
each supplies a **realization** (a trace, an index, a perfect duality) and **not** the **signature** (the
$(1,n{-}1)$ polarization carrying the trace $t$). The signature is, in every case, the Hodge-Riemann/Rosati
input the tool *presupposes*, not an output. This is the marginal-positivity thesis confirmed from four
more independent bases (twelve total with the eight-angle sweep), and it sharpened the map: it produced
three reusable disqualifiers, one cross-area convergence, and one strictly-better archimedean-inclusive
substrate to watch.

## The four-area ledger

| Area | Verdict | Reduces to | Durable yield |
|---|---|---|---|
| **Lorentzian polynomials / Alexandrov-Fenchel** (Branden-Huh; tropical HR) | CLOSE (wrong polarity) | e3r/#48 (convex Hodge unconditional) + #97 (Boucksom-Jonsson) | **The discriminant-complementarity screen** |
| **SUSY QM / Witten index** $\mathrm{Tr}(-1)^F$ | CLOSE (realization / Level 3) | #113 (xp/SYK Level 3); #101 ($J$ vs $C_E$); the CCM #114 target | **Supertrace = Euler char, not signature; + Buchholz-Longo** |
| **Index theory** (Atiyah-Singer / Lefschetz / eta / Hirzebruch) | CLOSE (realization / K1) | R3.5 K1 wall (Connes); Faltings-Hriljac too-local; #113 | **eta-invariant = Shimizu L-value (the eta bridge retired)** |
| **Condensed/analytic geometry** (Clausen-Scholze, six functors) | CLOSE as polarization; **WATCH** as infrastructure | #71 (perfectness not sign), at maximal generality | **The norm-stack: a better archimedean-inclusive substrate** |

## The three reusable disqualifiers (the sweep's genuine yield)

1. **The discriminant-complementarity screen (Lorentzian).** The genus-1 Weil/RH bound is
   $|t_p| < 2\sqrt p \iff t_p^2 - 4p < 0$, the **negative-discriminant / complex-root** condition.
   Lorentzian / real-stable / log-concave polynomials are **real-rooted**: $t_p^2 - 4p \ge 0$, the
   *negation* of the Weil bound. RH lives on the complex-root half of the discriminant; the entire
   convex / log-concave / Lee-Yang engine lives on the real-root half. Both read "one positive eigenvalue"
   numerically, but from opposite root-geometries, which is exactly why one signature is unconditional
   (wrong polarity, cannot flag an off-line zero) and the other is contingent. The single inequality
   $\mathrm{sign}(t^2-4q)$ vs real-rootedness retires the **whole real-stability / Lee-Yang / Lorentzian /
   log-concave family** in one line, unifying #95 (Lee-Yang), #27 (log-concavity), #48 (convex Hodge).

2. **The supertrace/signature grading split (SUSY + index theory, convergent).** $\mathrm{Tr}(-1)^F$ is a
   supertrace $=$ the Lefschetz number $=$ the **Euler characteristic** (an alternating count); the Weil
   explicit formula *is* a Lefschetz-supertrace, so this is the realization side, free. The **signature**
   $\sigma = b^+ - b^-$ is a *different* index theorem (Hirzebruch's), and its grading is the Hodge-$\star$
   / Weil **C-operator** ($C_E^2 = -1$, $t$-carrying), not $(-1)^F$ ($J$, square $+1$, $t$-blind). The
   index theorem realizes the *integer* $\sigma$ but **presupposes Hodge-Riemann to define the grading
   operator**. So the grading that turns the supertrace into the signature **is M4**. Reinforced by
   **Buchholz-Longo (1999)**: the modulus of any graded/super-KMS functional is proportional to an
   ordinary ungraded KMS state (the twist is weakly inner), so a $\mathbb{Z}_2$-graded supertrace over the
   type-III$_1$ modular carrier produces **no new sign** beyond the plain (definite, D-H-blind) trace
   (#99/#102). Sign-from-grading is dead as a free lunch.

3. **The eta-invariant = L-value bridge (index theory).** Atiyah-Donnelly-Singer (1983) proves the
   eta-invariant signature-defect of a Hilbert-modular cusp $=$ the **value at $s=0,1$ of a Shimizu
   L-function**. So *both* faces of arithmetic index theory fall to the #113 L-value/order-of-vanishing
   disqualifier: analytic torsion $\to$ heights (Kudla, already #113), eta $\to$ L-values (new). Arithmetic
   index theory is special-value regime, not the zero-location-across-all-heights signature RH needs.

## The convergence (worth recording)

Two independent surveys (SUSY and index theory) landed on the **same object** from different directions:
the **signature operator's grading is the polarization**. The signature is realizable as the index of the
Hirzebruch signature operator, a genuine non-circular geometric integer that *formally* fits R3.5's
geometric-positivity escape shape, **but it is not a Hodge index theorem**: it presupposes the
self-dual/anti-self-dual splitting (the Hodge-$\star$, the C-operator) that *is* M4. This pins the
universal gap to a single operator: realization $=$ the index (free); the signature $=$ the grading that
defines the signature operator $=$ the polarization $=$ M4. (Recommended VERIFIER/ADVERSARY follow-up:
tighten the Lean `GeometricPositivity` placeholder in `R3_5.lean` so "realizes the signature integer"
cannot be mistaken for "proves the primitive-part definiteness.")

## The one thing to WATCH (infrastructure, not polarization)

Condensed/analytic geometry (Clausen-Scholze) closes as a polarization route for the same reason as
everything in the #71 trio (it gives perfect Poincare-Verdier duality, no sign), but it upgrades the
**substrate** coordinate. Wagner's **stack of norms** $\mathcal{N}/\mathbb{R}_{>0}$ (analytic stacks,
Strasbourg workshop May 2025) surjects onto the extended Berkovich spectrum $\mathcal{M}(\mathbb{Z})^{\mathrm{ext}}$
with the **archimedean place as a first-class branch** alongside the prime branches, glued by the
$!$-topology rather than by hand-built Green's functions. This is a strictly better archimedean-inclusive
substrate than Gurney's prismatization (which is $p$-adic, no $\infty$) for the M4 core, the
archimedean-dominates-the-growing-Euler-product balance (#20/3M). It carries **only** the perfect duality
plus classical (imported, wrong-regime) Arakelov positivity; the prerequisite for any native polarization
is an **"archimedean Deligne-Illusie"** (Hodge-de-Rham degeneration at $\infty$), which is conjectural and
is the workshop's own closing open problem. **WATCH trigger:** if the archimedean Deligne-Illusie is
proven, re-survey, it is the gate to a polarization on this substrate.

## The deepest structural statement (what the sweep sharpened)

The perfectness/sign cut is now **structural**, not an artifact of any one cohomology. The four areas span
the modern toolkit for the two halves: the six-functor formalism is **duality-without-sign made universal**
(realization/perfectness, free), and Hodge-Riemann/Rosati positivity is **the sign** (M4). The signature
is the difference between a six-functor formalism and a Hodge-theoretic polarization. Realization is the
universal, axiomatizable half; the signature is the non-formal, metric/Hodge-theoretic half. That is the
universal gap, restated at the level of the formalisms themselves: **every framework that can be
axiomatized gives realization; the signature is exactly the part no axiomatization supplies.**

## Where the front stands

Unchanged in location (M4), sharper in description. The sweep added three disqualifiers that keep future
search off the real-stability, sign-from-grading, and eta/L-value dead branches; one convergence that pins
the gap to the grading of the signature operator; and one substrate to watch (the norm-stack, gated on the
archimedean Deligne-Illusie). The standing construction-grade M4 targets are unchanged: the AHK arithmetic
lattice ([`research_directions/09A_ahk_arithmetic_lattice.md`](research_directions/09A_ahk_arithmetic_lattice.md)),
the Faltings-Hriljac product + $\Gamma_S$, the function-field lever B Spec(Z) lift
([`lever_b_function_field_plan.md`](lever_b_function_field_plan.md)), and the modular $C_E$-cup (#104).
Nothing here lowered the difficulty of M4; it confirmed, from four more directions, that M4 *is* the
difficulty, and handed back three disqualifiers and a better substrate.

## Provenance

Single session, 2026-06-25. Four areas, four SURVEYOR agents, each builder/surveyor-adversarial with the
D-H + e3r-polarity + L-value disciplines applied. Dossiers:
`scratchpad/explore_2026-06/{lorentzian_polynomials,susy_witten_index,index_theory,condensed_analytic}.md`.
Recorded in LEARNINGS #119. Follows the metaplectic-operator finding (#118, `e1i`) and the eight-angle
sweep (#111-#117). Cross-refs: #48/#95/#27 (the convex/log-concave kills the discriminant screen unifies),
#71 (perfectness-not-sign, which the condensed survey generalizes), #99/#101/#102/#104 (the modular
carrier the Buchholz-Longo result neuters), #113 (the L-value disqualifier the eta bridge obeys),
R3.5/K1 (the wall index theory re-derives), `spec_z_cohomology_landscape.md` (the scorecard the
norm-stack row slots into).
