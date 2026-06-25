# The breadth corpus: positivity / signature / polarization phenomena across mathematics

> The operational atlas for [`docs/03_research/breadth_program.md`](../../docs/03_research/breadth_program.md).
> One row per phenomenon, indexed by the field-agnostic M4 skeleton so it is queryable by STRUCTURE, not by
> field name. Append-only and deduplicated: every breadth sweep adds rows and never re-derives one. The
> machine-readable corpus + the skeleton query extend
> [`transfer_search.py`](transfer_search.py) (Generative Engine 6b); this file is the human-readable index.

## The skeleton (the query keys)

S1 Lefschetz operator | S2 primitive decomposition | S3 duality/pairing | S4 trace datum $t$-slot |
S5 primitive-definite signature (polarization) | S6 **right polarity** (contingent on $t$, flips) vs
unconditional | S7 non-circular. **The master discriminator is S6 (polarity).** Almost everything is
S1-S5 with *wrong* (unconditional) polarity; M4 needs contingent polarity. The first question to any row:
**does your signature flip, and on what?**

`produces`: realization (a trace/number) / perfectness (a duality, no sign) / signature (the polarization).
`regime`: all-heights signature (RH) / central L-value (BSD) / Level-3 statistical (compatible with $\beta=0.51$).

## Verdict legend

TRANSFER-CANDIDATE (right polarity, a $t$-slot, worth a transfer attempt) | COMPONENT (supplies a piece of
the M4 assembly) | WATCH (infrastructure or gated on a prerequisite) | DISQUALIFIED (with the rule that
kills it) | TARGET (an actual standing M4 construction target).

## The atlas (seeded from the eight-angle + four-area sweeps, the cohomology landscape, the transfer shortlist)

| phenomenon | field | polarity | produces | t-slot | regime | verdict / disqualifier | yield |
|---|---|---|---|---|---|---|---|
| **Weil/Rosati form on a surface /$\mathbb{F}_q$** | algebraic geometry | **contingent** | signature | yes | all-heights | **TRANSFER-CANDIDATE (the master column)** | the function-field RH = lever B; the template all transfers aim at |
| **Hodge-Riemann (Kähler)** | complex geometry | unconditional | signature | no | n/a | DISQUALIFIED (e3r polarity #48) | the canonical wrong-polarity source |
| **Adiprasito-Huh-Katz (matroids)** | combinatorics | unconditional | signature | partial | n/a | COMPONENT / TARGET (09A AHK lattice) | proven $(1,n{-}1)$ with no variety; needs a $t$-carrying Lefschetz element |
| **Alexandrov-Fenchel / mixed volumes** | convex geometry | unconditional | signature | no | n/a | DISQUALIFIED (e3r #48; discriminant #119) | transfer-shortlist entry, wrong polarity |
| **Lorentzian / completely log-concave polynomials** | combinatorics/optimization | unconditional | signature | no | n/a | DISQUALIFIED (#119 discriminant: real-rooted) | **the discriminant screen** (real-root half) |
| **Tropical / Berkovich Hodge-Riemann** | tropical geometry | unconditional | signature | no | n/a | DISQUALIFIED (#119; #97 Boucksom-Jonsson) | same family, real-root half |
| **Lee-Yang circle theorem** | statistical mechanics | unconditional (real/circle) | signature | no | n/a | DISQUALIFIED (#95; #119 discriminant) | retired by the discriminant screen |
| **Boucksom-Jonsson NA Monge-Ampere** | non-arch geometry | unconditional (convex one-sided) | signature | no | n/a | DISQUALIFIED (#97) | valuative single place, archimedean-blind |
| **Connes 1999 adele trace formula** | NCG / operator algebras | n/a (K1) | realization | on $F$ | all-heights | DISQUALIFIED (R3.5 K1 wall) | the paradigm K1 case |
| **Connes-Consani archimedean Weil positivity** | NCG | contingent (proved at $\infty$) | signature (at $\infty$) | no | all-heights | COMPONENT (K2-blind, $\Gamma$-factor half) | proves the sign can be GEOMETRIC (the $\rho{=}1$ jump) |
| **CCM semilocal prolate $W_{\lambda,S}$** | NCG / metaplectic | contingent (strategy) | signature (strategy) | yes (Euler $dm_S$) | all-heights | TARGET (door ajar, = M4 at core) | the un-eliminated metaplectic route |
| **Metaplectic / Weil rep over $\mathbb{F}_p$ (e1i)** | rep theory / harmonic analysis | n/a (sign cancels) | realization (Gauss sum) | no | n/a | DISQUALIFIED finite-locally (#118) | the Weil index is a phase the measure discards; cancels in $g^*g$ |
| **Bost-Connes / KMS, type III$_1$** | NCG / operator algebras | n/a | realization (trace) | no | Re$(s)>1$ | DISQUALIFIED (K1, blind to strip; Buchholz-Longo #119) | graded-KMS modulus $\propto$ ungraded; no sign from grading |
| **de Branges / Conrey-Li pairing** | analysis | contingent but strictly-stronger | signature | no | all-heights | DISQUALIFIED (#43, fails for $\zeta$ at $k{=}34$) | the pairing must be RH-EQUIVALENT, not stronger |
| **Bhatt-Lurie prismatic / WCart** | $p$-adic Hodge | n/a (perfectness) | perfectness | on $F$ | n/a | COMPONENT (substrate, no sign) | duality proven, polarization absent |
| **Tang prismatic Poincare duality** | $p$-adic Hodge | n/a | perfectness | no | n/a | DISQUALIFIED as polarization (#71) | perfectness not the sign |
| **Hesselholt THH/TP/TC** | algebraic K-theory | n/a | realization (det) | no | n/a | COMPONENT (realization /$\mathbb{F}_q$, no $\mathbb{Z}$-flow) | $\zeta=\det_\infty$, needs negative-definite cup |
| **SUSY Witten index $\mathrm{Tr}(-1)^F$** | physics / index theory | n/a (Euler char) | realization | no | order-of-vanishing | DISQUALIFIED (#119: supertrace = Euler char; #113) | the signature grading is a DIFFERENT index theorem = M4 |
| **Hirzebruch signature operator** | index theory | n/a (presupposes HR) | realization (integer $\sigma$) | no | all-heights but global int | DISQUALIFIED (#119: grading = the polarization) | the convergence: signature-operator grading = M4 |
| **Eta-invariant / APS signature defect** | index theory | n/a | realization | no | central L-value | DISQUALIFIED (#119: eta = Shimizu L-value, #113) | the eta bridge retired |
| **Gillet-Soule arithmetic Riemann-Roch** | Arakelov | n/a | realization | no | heights / L-deriv | DISQUALIFIED (#113 BSD regime) | outputs heights, not the signature |
| **Faltings-Hriljac arithmetic Hodge index** | Arakelov | contingent (proven, single surface) | signature | no (wrong dim) | all-heights | TARGET | needs the PRODUCT Spec(Z)$^2$ + Frobenius $\Gamma_S$ |
| **Condensed/analytic six functors + norm-stack** | condensed math | n/a (perfectness) | perfectness | no | n/a | WATCH (substrate, #119) | best archimedean-inclusive base; gated on archimedean Deligne-Illusie |
| **Kudla arithmetic theta lift** | automorphic | contingent | central L-deriv | yes | central L-value | DISQUALIFIED (#113 BSD regime) | the L-value/derivative rule |
| **Epstein zeta (non-Euler)** | analytic NT | n/a | realization | no | n/a | DISQUALIFIED (the K2 control: off-line zeros) | a D-H-class wrong-approach detector |
| **Ihara zeta / Ramanujan graphs** | spectral graph theory | contingent | signature (graph-RH) | yes (Frobenius=adjacency) | all-heights | COMPONENT (= function-field shadow) | the proven-case signature in graph clothing |

## Open acquisition queue (Pillar 5 of the program: where to look next)

**Disqualifier-complement aim (5.5; the sharpest, from the #119 discriminant screen).** RH lives on the
**complex-root / negative-discriminant / contingent** half. Sweep fields that produce CONTINGENT,
complex-root, spectral-gap positivity (the complement of the convex/log-concave engine):
- Riemann-Hilbert / Plancherel-Rotach transitions (where real roots become complex; the edge of the spectrum)
- the Lee-Yang **failure** regime (where zeros leave the circle: the contingent side of #95)
- transfer-operator / Ruelle spectral-gap positivity (contingent on the gap)
- the Berry-Tabor $\to$ GUE transition (integrable vs chaotic, the contingency of level repulsion)

**Orbit-map aim (5.2).** Under-visited points in the Hodge-Riemann orbit and the "functional-equation-as-
duality" orbit:
- Bridgeland stability conditions on triangulated categories (a $(1,n{-}1)$-flavored central charge)
- Schur / cluster-algebra positivity; the Hodge theory of cluster varieties
- quantum cohomology / Frobenius-manifold flatness; the Dubrovin connection
- the Weil-Petersson / Hodge-metric positivity

**Distant-field queue (5.4; blind sampling, lower priority than the aimed draws).** quantum information
(entanglement monogamy, relative-entropy positivity); integrable systems (tau-functions, Riemann-Hilbert);
free probability (subordination, the Brown measure); optimal transport (displacement convexity); topological
recursion (the spectral curve); the c-/a-theorem monotonicity; persistent homology (signature stability);
coding theory (MacWilliams duality as a functional equation).

## How to use this corpus

1. **Query by skeleton, not field** (Section 3 of the program): "return contingent-polarity rows with a
   $t$-slot and a duality."
2. **Score a new candidate** before recording: run the full disqualifier battery (Section 4) + a D-H and
   polarity control. Add a row only after the builder $\to$ adversary loop.
3. **Mine the corpus** (Pillar 5.6): periodically ask "what do the contingent rows share that the
   unconditional ones lack?" The discriminant screen was found this way. Each pattern is a candidate new
   disqualifier.
