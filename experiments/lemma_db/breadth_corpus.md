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
| **Riemann-Hilbert / equilibrium-measure transitions** (acq1) | integrable systems / RMT | contingent but **curative** | realization | no | Level-3 | DISQUALIFIED (curative-flip #120) | the locus relocates and zeros track it; K1 made concrete |
| **Transfer operator / Ruelle / Selberg dynamical zeta** (acq1) | thermodynamic formalism | contingent, **strip-width** axis | realization | yes (closed orbits) | all-heights | DISQUALIFIED (spectral-gap=zero-free-region #120, K1) | gap = a strip not the line; zeta's zeros are scattering resonances off the self-adjoint axis |
| **Berry-Tabor / GUE level statistics** (acq1) | quantum chaos | contingent, **spacing** axis | realization | no | Level-3 | DISQUALIFIED (wrong-axis #120) | repels in the height direction, orthogonal to Re=1/2 |
| **Katz-Sarnak symmetry type** (acq1) | automorphic / RMT | contingent, **central-rank** axis | realization | yes (monodromy) | L-value | DISQUALIFIED (wrong-axis #120 + #113 + circular) | governs the central point (rank), corollary of RH where proven |
| **Bridgeland stability + support-property form** (acq2) | derived categories | unconditional (**selection**, not sign) | realization | no | n/a | DISQUALIFIED (selection-not-sign #121 + curative #120) | the closest non-AG near-miss: a FIXED indefinite Q (weight-2 Mukai), but membership flips not the sign; off by one Hodge weight |
| **Frobenius manifolds / Dubrovin connection** (acq2) | GW theory | static skeleton, no contingent polarity | realization | no | n/a | DISQUALIFIED (curative #120) | fixed indefinite $\eta$ + spectral connection, but the contingency is semisimplicity (eigenvalue collision), curative |
| **Gamma conjecture / Apery constants** (acq2) | GW theory / Hodge | n/a | realization | no | special-value | DISQUALIFIED (special-value/period #121) | zeta VALUES $\zeta(k)$, $k\ge2$, in the convergent half-plane (no zeros); one tier beyond #113 |
| **Scattering / Eisenstein resonance sign** (acq2) | automorphic spectral | unconditional, **line** axis | realization | yes (carries $\xi$) | all-heights | DISQUALIFIED (K1 + de Branges #43) | F3 line-axis HIT, but a half-plane dissipativity bound not a line signature; closes onto Connes/CCM/de Branges |
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
| **Sieve parity barrier / bilinear parity-breakers** (Vinogradov Type I/II, Bombieri-Vinogradov, Friedlander-Iwaniec $x^2{+}y^4$, Zhang Type III, Sawin-Shusterman /$\mathbb{F}_q[T]$) | analytic number theory (sieve) | n/a (the $\mu$-sign is input-side, #120 split) | realization | no | Levels 2-3 (survives EH/GRH) | DISQUALIFIED (**modulus-only-consumer #146**, machine-enforced 2026-07-02; wrong-axis: **level of distribution**, the fourth shadow axis) | parity = the consumer-side shadow of R1, not M4: every power-saving break consumes Weil/Deligne purity through sign-free corollaries (moduli, or the FKM/Sawin-Shusterman angle/monodromy tier) and discards the S5 sign at the border; yields the sharpened R1 WATCH trigger (variety-free power-saving bilinear $\mu$ cancellation near $\sqrt x$) |

**Battery additions (2026-07-01, #146; ADVERSARY-passed and machine-enforced in `breadth_corpus.py`
2026-07-02, suite 23/23; the "stays at 16/16" note previously here was stale, the suite was already 19/19
after #143):** the **modulus-only-consumer screen**, upheld with a corrected antecedent: a polarization
consumed only through **sign-free corollaries** (the modulus tier $|S| \le 2\sqrt p$ OR the angle/monodromy
tier: weights in all degrees, monodromy classifications, equidistribution laws) cannot be re-emitted as a
signature, because every imported statement is invariant under $Q \mapsto -Q$ and no geometric carrier
crosses the border; retires the exponential-sum-import family (Kloostermania, trace-function machinery) as
M4 **sources** while leaving it alive as a purity consumer and as an ingredient in operator-signed
assemblies (#143 branch). "Sign" is pinned to the S5 signature, not eigenvalue phases (Gauss-sum signs, root
numbers = S3 data) and not proof-internal oscillation (Kloostermania's sign changes are Kuznetsov-sourced).
And the **level-of-distribution** wrong-axis flavor (the sieve frame's native $\theta$ axis,
`axis="level"`), joining spacing / central-rank / strip-width. Encoding: the `weil_consumption` skeleton
dimension ('sign-free' fires; 'signature'/'producer' do not; Katz-Sarnak tagged 'sign-free', the
Ihara/Ramanujan row stays 'na' by the tagging discipline: tag the claimed route to a signature, not the
historical constructions). Resolution: the ADVERSARY-pass section of
[`parity_vs_polarization.md`](../../docs/03_research/parity_vs_polarization.md).

## Open acquisition queue (Pillar 5 of the program: where to look next)

**Disqualifier-complement aim (5.5; the sharpest, from the #119 discriminant screen) -- DONE (acq1, #120).**
RH lives on the **complex-root / contingent** half; the four complement fields (Riemann-Hilbert, Lee-Yang
failure, transfer-operator/Selberg, Berry-Tabor/GUE) were swept and ALL CLOSE. The complement is occupied,
but by four flavors of "contingent but still wrong", each a new screen (curative-flip, wrong-axis,
spectral-gap=strip, input/output). **Result: the M4 polarity FINGERPRINT** -- a transfer candidate must be
*contingent + complex-root + line-axis + output-indefinite + prohibitive-on-a-fixed-locus*, which IS a
polarization. So contingent + complex-root was necessary, not sufficient; the four acq1 fields are the gap.
The refined aim (next draws): the **scattering-resonance sign** (the modular-surface absorption sign as the
spectral avatar of the polarization sign; a VERIFIER target on `R3_5.lean`) and **Bridgeland stability** (a
$(1,n{-}1)$ central charge on a FIXED heart, the rare fixed-locus + output-indefinite combination outside
algebraic geometry).

**Orbit-map aim (5.2) -- partly DONE (acq2, #121); the search has CONVERGED.** Bridgeland stability and
quantum cohomology / Frobenius manifolds were drawn (acq2) and both CLOSE: they supply the rare ingredient
(a FIXED indefinite form), but the **sign never flips** (selection-not-sign #121) and there is **no
Frobenius $t$-slot**. acq2 sharpened the fingerprint (F4: the SIGN must flip, not class-membership) and
showed the fixed-indefinite-form space outside arithmetic geometry is mapped and **insufficient** -- the
residual profile IS M4 (Bridgeland is off by exactly one Hodge weight: its weight-2 $(2,n{-}2)$ vs Weil's
weight-1 $(1,n{-}1)$). **PIVOT (engine `aim()` = CONVERGED):** the productive work is now the M4
construction (09A AHK lattice, Faltings-Hriljac + $\Gamma_S$, lever B) and the `R3_5.lean` VERIFIER target
(a discrete-vs-continuous spectrum predicate), not more breadth draws until a genuinely new orbit point
appears. Remaining unvisited orbit points (only if a new structural reason emerges): Schur / cluster-algebra
positivity; the Weil-Petersson / Hodge-metric positivity; the limiting-MHS / Sen degeneration (08D, likely
on file).

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
