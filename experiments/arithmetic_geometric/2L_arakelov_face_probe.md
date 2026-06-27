# 2L: the Arakelov face probe (mirror of the AHK failure mode)

> Direction 8 follow-up. AHK (the combinatorial-Hodge route to P3) was closed in
> LEARNINGS #129/#130: it has the base (it attacks `Spec(Z)`-as-curve-over-`F_1`
> directly) but cannot source a weight-1 `sqrt(q)` carrier (matroid Chow rings are
> purely Tate). This probe asks the mirror question: does the Arakelov face (single
> arithmetic surface + Faltings-Hriljac positivity + the archimedean Green's /
> Petersson data of 2I/2J) ESCAPE that failure mode, or RELOCATE the universal gap?
> Five verified dimensions: four analyses (frontier-lit, structural-equivalence,
> mirror-of-AHK, D-H-discipline) and one computation (e2ae, the `omega-bar^2`
> numerics 2J deferred). Companion to [2K](2K_spec_z_squared_dictionary.md),
> [2J](2J_arakelov_adjunction.md), [sourcing_gap_r1](../../docs/03_research/sourcing_gap_r1.md).

## 1. Headline verdict

The Arakelov face does NOT escape the AHK failure mode: it RELOCATES the universal
gap to the mirror side. AHK has the base but cannot source the carrier; the Arakelov
face has a genuine carrier and a genuine PROVEN polarization (Faltings-Hriljac /
Yuan-Zhang arithmetic Hodge index), but only on a single arithmetic surface, for one
motive's L-function, never for zeta. It dies not at facet A (R1, sourcing/purity) and
not at facet B (M4-positivity, which is a theorem there per surface), but at the
BASE: the nonexistent product surface `Spec(Z) x Spec(Z)` and its Frobenius
correspondence `Gamma_S` that would let per-motive positivity reach zeta's actual
zeros. The two routes fail at opposite ends of the same two-facet gap (AHK lacks the
carrier, Arakelov lacks the zeta-base), and the 2026 literature frontier confirms the
verdict is unmoved: every generalized arithmetic Hodge index theorem (Faltings-Hriljac,
Moriwaki, Yuan-Zhang, Cantat-Gao-Habegger-Xie) proves positivity on a fixed scheme
certifying that scheme's own height/unit/dynamics data, and every 2025-2026 structure
that reaches zeta's zeros (Morishita's Deninger/Connes-Consani bridge, the new
Connes-Consani Jacobian of compactified `Spec(Z)`) supplies only a trace/explicit-
formula, never an intersection pairing or polarization. The K2 / D-H discipline holds
but is substantively DEFERRED: all of the Arakelov face's zeta-vs-D-H discriminating
power is delegated to the unbuilt `Gamma_S`, so no current Arakelov positivity
statement has yet even entered the discipline's domain.

## 2. Mirror-of-AHK synthesis

The two routes occupy distinct, already-recorded scorecard nodes
(`spec_z_cohomology_landscape.md`): AHK = NODE-ahk-too-blind (PROVEN signature, no
variety, arithmetic-blind), Faltings-Hriljac = NODE-fh-too-local (PROVEN polarization,
single surface, no Frobenius reaching zeta). So the polarity contrast is real, not
artificial.

| facet | AHK (combinatorial) | Arakelov (Faltings-Hriljac) |
|---|---|---|
| base `Spec(Z)`-direct? | YES (attacks `Spec(Z)`/`F_1` as a curve directly) | NO (lives on a single arithmetic surface = a curve OVER `Spec(Z)`, relative dim 1; lacks the self-product) |
| R1 purity-source (weight-1 `sqrt(q)` carrier)? | NO (matroid Chow ring is purely even/Tate, no `H^1` at all) | YES per motive (Deligne purity of the generic fiber's motive) |
| M4 polarization-source (indefinite Hodge-index signature)? | PROVEN-but-blind (Hodge-Riemann holds, arithmetic-blind) | PROVEN per surface (Faltings-Hriljac / Yuan-Zhang, validated 2H ranks 1-3) |
| where it dies | facet A (R1): no carrier to even ask purity of | the BASE: no `Spec(Z) x Spec(Z)` + `Gamma_S` to globalize per-motive theorems into zeta |

Conclusion: AHK has the base but not the polarization-SOURCE (it has the signature
abstractly but no arithmetic carrier on which it means anything about zeros). The
Arakelov face has the polarization-source (a real proven index theorem on a real
carrier) but not the BASE (the self-product / Frobenius correspondence on which that
positivity would attach to zeta's zeros rather than to one motive's regulator). Both
are the SAME two-facet variety-gated gap (R1 sourcing + M4 polarization, per
`sourcing_gap_r1.md`) seen from opposite sides. The honest sharpening the mirror
forces: the two-facet model (A=R1, B=M4) presumes a variety on which to STATE weight
and signature; the Arakelov face shows that the missing thing for zeta is neither A
nor B individually (both are theorems per surface) but the BASE-for-zeta. In the
project's existing 4-property M4 decomposition this is PROP-global (lives on the global
`H^1` of the PRODUCT, reaches the actual zeros via `Gamma_S`, not a single surface);
it is co-dependent with the carrier/trace for the literal target object, not a free
third vertex. So this is a re-localization onto the already-named PROP-global conjunct,
not a new fourth facet.

## 3. Structural-equivalence result: weaker sufficient object, and the BSD severance

Does the Arakelov gap reduce STRICTLY to "build `Spec(Z) x Spec(Z)` + `Gamma_S`"? The
weaker sufficient object is a SINGLE arithmetic carrier (a relative surface over an
auxiliary curve, or an arithmetic 3-fold) hosting `H`-odd with a Frobenius/flow cycle
class `Gamma` of place-dependent `(1, p)` bidegree, plus the arithmetic Hodge standard
positivity on its primitive part. Yuan-Zhang's adelic-line-bundle index theorem
(Math. Ann. 367, 2017) is the natural index machinery on such a carrier directly: one
does not need the literal self-product, only a single carrier whose Frobenius spectrum
on `H`-odd equals zeta's zeros and whose primitive cup form is definite.

Honest deflation (per the e2ad caution, and confirmed by the adversary): this is
weaker than 2K only in CONSTRUCTION (no literal self-product), NOT in DIFFICULTY. A
self-correspondence `Gamma` on `Y` is by definition a cycle on `Y x Y`, so "a
Frobenius correspondence on a single `Y`" already lives on a self-product at the level
where it matters; the genuinely distinct move (host `H`-odd by a Weil cohomology and
an endomorphism of it directly) is exactly the Deninger / prismatic / Hesselholt route
already cataloged in `spec_z_cohomology_landscape.md` (Deninger `X x X` flow,
Bhatt-Lurie Rosati form on global prismatic `H^1`, Hesselholt negative-definite cup on
`TP`-odd), each carrying the SAME missing polarization. So the "strictly weaker object"
is an equivalent re-localization onto the cohomology rather than the self-product, not
a new object. It still inherits BOTH variety-gated facets R1 (sourcing the pure
carrier = Deligne over `F_q`) and M4 (the polarization = Weil/Rosati over `F_q`). It
reduces the construction wording, not the open kernel.

The BSD-vs-Gamma-factor severance (why FH positivity stays off zeta's zeros). The
only proven height-to-L channel is Gross-Zagier / BSD, which equates the Neron-Tate
height of a Heegner point (an FH-positive quantity) to the CENTRAL derivative
`L'(E, 1)` up to nonzero period/Tamagawa factors. This is a single Taylor coefficient
at the one point `s = 1`: the order-of-vanishing / rank datum, severed from where the
OTHER zeros sit. A function can have positive central derivative and off-line zeros
elsewhere. Hence FH positivity is logically compatible with off-line zeros, and the
project's disqualifier #113 retires the whole Gross-Zagier / Beilinson-Bloch family as
"central L-value / order-of-vanishing regime, not the signature across all heights."
The severance is in the L-LINK, not in the signature object: the Beilinson-Bloch /
Yuan-Zhang height PAIRING positivity is itself a genuine signature (negative-definite
primitive, global, arithmetically loaded, D-H-unbuildable), proven generically by Gao
in the higher-codimension regime FH cannot reach. So the right reading is two-part: the
L-link (Gross-Zagier / the Beilinson-Bloch conjecture) is order-of-vanishing and
useless for zero-location, while the signature object is exactly the right KIND of tool
and is what the weaker carrier in section 3 should host. It still lacks the
self-product `Gamma_S` and SHARP (not generic) positivity, which is M4.

(Correction recorded against the prompt's clean two-facet split: M4 is NOT what the
Arakelov face is missing. The single-surface analogue of M4 is a theorem there; what
is missing is the base. The two-facet model was never a complete model of the gap, the
project already names PROP-global, PROP-rh-equivalent, PROP-noncircular alongside
R1/M4.)

## 4. The 2026 literature frontier

Verdict: NO. As of 2026 no generalized arithmetic Hodge index theorem applies to an
object carrying zeta's (or any degree >= 2 L-function's) ZEROS without the nonexistent
product `Spec(Z) x Spec(Z)`. The 2K section-4 verdict ("the gap = the product
surface") is unmoved. Reliance: WebSearch + arXiv/Springer abstracts for the survey,
cross-checked against in-repo records (`spec_z_cohomology_landscape.md`, 2P) and
background knowledge; two arXiv facts independently confirmed by author + date.

What was found, each classified by which side of the wall it sits on:

| object | reaches zeta's zeros? | carries a polarization? | side of the wall |
|---|---|---|---|
| Yuan-Zhang adelic-line-bundle index (Math. Ann. 367, 2017) | no (fixed scheme; certifies non-arch Calabi + preperiodic-point rigidity) | yes, single scheme, codim-1 | NODE-fh-too-local |
| Moriwaki higher-dim arithmetic Hodge index (alg-geom/9403011; arXiv:1010.1599) | no (certifies a Dirichlet-unit-theorem analogue on a fixed variety) | yes, single scheme | NODE-fh-too-local |
| Bost theta-invariants / pro-Hermitian Arakelov (Prog. Math. 334, 2020; arXiv:1512.08946) | no (Diophantine `h^0_theta`, a non-negative scalar) | NO (wrong signature class: an arithmetic `h^0`, not an indefinite `(1, n-1)` form) | D-H-blind / arithmetic-`h^0` side |
| Cantat-Gao-Habegger-Xie (Duke 170(2), 2021) | no (USES the existing single-variety index for the geometric Bogomolov conjecture) | uses, does not extend | same side as FH |
| Morishita, Deninger <-> Connes-Consani adelic-spaces bridge (arXiv:2508.15971, 2025) | trace-side only (orbits <-> primes correspondence) | NO (no intersection pairing, no bilinear form, no positivity) | D-H-shared trace side |
| Connes-Consani, "On the Jacobian of (Spec Z)bar" (arXiv:2602.15941, 2026) | trace-side only (explicit formula AS Lefschetz trace; no eigenvalue correspondence proven) | NO (no intersection pairing, no polarization, no Rosati positivity) | D-H-shared trace side |

The frontier has advanced the REALIZATION (trace) side and added structure to the
arithmetic-curve geometry (the new Connes-Consani arithmetic Picard monoid,
Abel-Jacobi map `Theta`, and explicit-formula-as-Lefschetz-trace are the single most
relevant 2026 development), but the polarization facet (M4) and the product-surface
self-intersection are exactly as open in 2026 as the project recorded. Bost's
infinite-dimensional Arakelov geometry is genuinely over the arithmetic curve and
infinite-dimensional, but produces a Diophantine `h^0_theta`, the wrong signature
class (a positive scalar, not a quadratic form whose negative-definiteness on a
primitive part forces `|alpha| = sqrt(q)`). It is the arithmetic-`h^0` / D-H-blind
side, not the polarization.

Repo correction emitted by this probe (verified internal inconsistency):
`2K_spec_z_squared_dictionary.md` section 6b (lines 156-165) attributes
arXiv:2508.15971 to "NEW (Oct 2024)" and frames it as a Connes-Consani-authored
"Deninger <-> Connes-Consani bridge." The paper is by Masanori Morishita, first
submitted 2025-08-21 (v4 2025-12-19), a knots-and-primes / adelic-spaces
correspondence. The substance 2K drew from it (links the two frameworks, no product
surface, no intersection form) is correct; only the date and authorship are wrong. The
companion `spec_z_cohomology_landscape.md` already has the correct Morishita-2025
attribution, so 2K is the stale file. Recommended fix: update 2K section 6b to
"Morishita 2025 (arXiv:2508.15971), a Deninger <-> Connes-Consani adelic-spaces
correspondence."

## 5. D-H discipline result

Partition of the Arakelov face into D-H-SHARED and zeta-ONLY layers, confirmed
numerically at dps=40 (re-run independently by the verifier):

- D-H-SHARED (any FE-bearing L has these): the archimedean Gamma-factor block
  `A_arch`, the completed `Lambda`, and the functional equation. Both zeta and D-H
  reduce to the SAME special-function kind, `-1/2 log(conductor) + 1/2 psi(linear in
  s)` (digamma/Gamma), confirmed at `t = 5, 20, 50`. Precision note: the archimedean
  DATUM differs (zeta uses the even-character factor `Gamma(s/2)`; D-H the
  odd-character-mod-5 factor `Gamma((s+1)/2)`, a parity shift plus conductor 5). The
  FE holds to 1e-40 only with the odd-character factor. Same KIND, different datum.
- zeta-ONLY: the Euler-product-supplied Frobenius correspondence `Gamma_S` with
  place-dependent `(1, p)` bidegree; the prime-power-supported `P_fin` block (von
  Mangoldt); the pole block `B_pole` at `s = 1` (D-H is entire across `s = 1`:
  `DH(0.9999) = DH(1.0001) = 0.9228`, finite, so `B_pole` is genuinely zeta-only).
  Confirmed: zeta's `-L'/L` is von Mangoldt (`log p` on prime powers, exactly 0 on
  composites, `Lam(6) = 0`); D-H's is composite-supported and non-multiplicative
  (`Lam(6) = 1.936`, `c(6) != c(2) c(3)`).

Where D-H falls out: at the FIRST step of the Weil template. `Gamma_S . Delta_S = N_n`
(point counts) requires the prime-power data that only an Euler product supplies. D-H
(an FE-forced linear combination of two Dirichlet L-functions with a non-algebraic
phase) is the L-function of no motive: no motive `V`, no `Frob_p`, no Tate module, no
arithmetic surface, no Neron-Tate height to be positive. So there is NO D-H
Faltings-Hriljac analogue to even ask positivity for. This is the opposite of a kill:
D-H cannot mimic the construction, so the Arakelov face SURVIVES this attack by
non-mimicry, failing at the motive, not at the positivity.

K2-clean status: the Arakelov face is K2-clean by structure. But the survival is
hollow in exactly the marginal-positivity sense. The built Arakelov positivity
theorems (Faltings-Hriljac, `omega-bar^2 = 12 h_Fal`, `lambda_inf`) are NOT
D-H-discriminating because they are not zeta-discriminating: they certify a fixed
curve's Mordell-Weil regulator and connect to L-values only through BSD (a conjecture,
the central derivative at `s = 1`), never through the FE Gamma-join that touches zeros.
The entire zeta-vs-D-H discriminating content is delegated to the unbuilt `Gamma_S`
(= R1 sourcing + M4 polarization). So the K2 pass is necessary but provides ZERO
evidence the face can close RH: a face whose only discriminator is an unbuilt object
has not yet entered the discipline's domain. The control passes 9/9 (smoke test, incl.
Test 9: the Li detector is blind to D-H while D-H's off-line zero at
`0.8085 + 85.699 i` is detectable). No positivity claim in this probe would "work" for
D-H.

## 6. The computed artifact (e2ae: Petersson / Faltings-height)

`python -m experiments.arithmetic_geometric.e2ae_petersson_faltings` (mpmath, 50 dps)
computes the archimedean self-intersection `omega-bar^2 = 12 h_Fal` that 2J specified
but deliberately did not compute, for the three e2h curves. Verified by independent
re-derivation (eta via a 400-term direct product, 60 dps; agreement to 1e-50+).

```
curve    Delta_min   ||Delta||_Pet(tau)   12 h_Fal       h_Fal          arch share
37a1        37        5777169.4392        -0.93124409    -0.07760367     81.17%
389a1       389       5450834.0692         1.47956255     0.12329688     72.23%
5077a1      5077      4278690.3275         4.29058069     0.35754839     64.15%
```

Three-term split `12 h_Fal = log|Delta_min| - log||Delta||_Pet(tau) + 6 log(2 pi)`:
the archimedean term `-log||Delta||_Pet` is remarkably STABLE across the ladder
(-15.57, -15.51, -15.27) while the finite term `log|Delta_min|` grows with the
discriminant (3.61, 5.96, 8.53). The archimedean (Petersson) term dominates the finite
term for all three and its dominance grows as the conductor shrinks (parallel to 2H's
"the regulator is archimedean").

- SL2(Z)-invariance of `||Delta||_Pet`: PASS for all three to ~1e-50, verified against
  `S`, `T`, `TS`, and (adversary-added) `Tinv`, `ST`, two random hyperbolics, and a
  GENERIC off-imaginary-axis `tau = 0.3 + 1.4 i`. The test has teeth: two WRONG
  normalizations (`(Im tau)^5 |eta|^24` and `(Im tau)^6 |eta|^22`) break at rel err
  1.05 and 0.30 off-axis. So the weight-(-12) `(Im tau)^6` genuinely cancels the
  weight-12 `|eta|^24`; this is a discriminating check, not a free identity.
- Archimedean share: 81.17% / 72.23% / 64.15%, defined as
  `|log||Delta||_Pet| / (|log||Delta||_Pet| + |log|Delta_min||)` with the additive
  `6 log(2 pi)` constant set aside. NORMALIZATION CAVEAT: this is a DESCRIPTIVE
  magnitude reading, not a curve invariant, and carries no proof weight.
- Normalization pinned without external import: two independent routes to `h_Fal` agree
  to 1e-52 (route A: eta + disc + `6 log(2 pi)`; route B: `h_Fal = -(1/2) log(A/2pi)`
  from the bare Neron covolume `A = Im(tau) |omega_1|^2`, which never touches eta or
  the discriminant). The internal pin `Delta(L) = (2pi/omega_1)^12 eta^24 = Delta_min`
  recovers 37 / 389 / 5077 to ~1e-50. A scan over candidate constants shows ONLY
  `+6 log(2 pi) = 11.0272623985` matches LMFDB; slip variants (2pi->pi, factor-2,
  half-slip, no const) all miss by 0.04 to 0.92. So the factor-of-2 / 2pi slog that 2J
  flagged is sidestepped: the constant is derived internally, then confirmed against
  LMFDB.
- LMFDB cross-check (extended by the adversary, closing the experiment's caveat b):
  37a1 to ~7e-8 (limited by recorded reference digits; route A vs route B agree to
  1e-52 internally, far stronger than the single external digit string, the residual
  is a likely transposition in the reference), 389a1 to 1e-11, 5077a1 to 1e-11. All
  three match published values.

Experiment: `experiments/arithmetic_geometric/e2ae_petersson_faltings.py`; writeup
`e2ae_petersson_faltings.md`; artifacts `e2ae_petersson_faltings.npz` and `.png`. Not
committed to git.

## 7. New-vs-re-cataloging self-assessment (per the e2ad caution)

GENUINELY NEW (and verified):

- The computational artifact e2ae. The explicit `omega-bar^2 = 12 h_Fal` values, their
  archimedean/finite split, and the exact pinning of the 2J normalization constant to
  `+6 log(2 pi)`. 2J deliberately shipped no numerics; e2ae closes the one
  specified-but-uncomputed entry of the Arakelov dictionary, with a discriminating
  SL2(Z)-invariance check and a two-independent-route normalization pin. This is a new,
  correct artifact.
- One verified repo correction: the 2K section-6b date/authorship error on
  arXiv:2508.15971 (Morishita 2025, not Connes-Consani Oct 2024).
- Three corpus additions to the survey, each correctly classified on the wrong side of
  the wall: Bost theta-invariants (wrong signature class), Moriwaki (Dirichlet-unit on
  a fixed variety), Cantat-Gao-Habegger-Xie (uses, does not extend, the single-variety
  index). These widen the survey without moving the verdict.
- One genuine localization the mirror sharpens: AHK and the Arakelov face fail at
  OPPOSITE ends of the two-facet gap (AHK lacks the carrier, Arakelov lacks the
  zeta-base), which makes precise that the universal gap is symmetric and that
  "Arakelov has a variety" is reconciled with "FLT-adjacent inherited gap" by
  DIMENSION (the variety it has is relative dim 1, not the self-product).

MERELY RE-CATALOGING (the universal gap is UNCHANGED):

- The frontier-lit verdict is mostly a faithful restatement of records already in the
  repo, often verbatim: 2P (2026-06-05) already scored the Connes-Consani 2026 Jacobian
  as trace/realization not a signed product-surface pairing; `spec_z_cohomology_landscape.md`
  already records Yuan-Zhang as fixed-scheme, the FH "too local" bracket, and the
  master thesis "every candidate realizes zeta as a trace; none carries the
  polarization." The self-label "mixed" is honest; "mostly recataloging with one
  correction and three additions" is more accurate.
- The structural-equivalence "strictly weaker sufficient object" is a re-localization
  onto the already-cataloged cohomological alternative (Deninger / prismatic /
  Hesselholt), not a new object; it inherits both variety-gated facets. RE-CATALOGING.
- The D-H "distinguishing-power-is-unbuilt / survival-is-hollow" finding is correct but
  RE-CATALOGING of the spec_z FH scorecard row and the 2K section-4 verdict; the
  "more damning than a clean pass" framing over-dramatizes a faithful restatement. The
  one sharpest D-H item (D-H is the L-function of no motive, so no FH analogue exists =
  survival by non-mimicry) is the closest to load-bearing.
- `omega-bar^2 = 12 h_Fal` itself is the single-surface SELF-intersection (the
  Arakelov analogue of the function-field diagonal `Delta^2 = 2 - 2g`), NOT the
  polarization (M4, facet B) and NOT sourcing/purity (R1, facet A). It is computed
  entirely from each curve's own arithmetic and says nothing about zeta's zeros.
  K1-clean (only Weierstrass coefficients, minimal discriminant, complex period enter;
  zeta's zeros never appear).

Net honest accounting: the probe produced one new correct artifact (e2ae), one repo
correction, three survey additions, and one genuine symmetry localization (the
opposite-ends mirror). Its structural conclusion is a consolidation of the
already-established universal-gap verdict, not new leverage. This is consistent with
e2ad's own caution that more all-roads re-cataloging is not where the leverage is.

## 8. Recommended next step

The Arakelov face is now the best-instrumented mirror of the gap: it HAS a proven
polarization and a proven, computed archimedean self-intersection on each single
surface, and it lacks exactly one thing, the product base `Spec(Z) x Spec(Z)` + the
Frobenius correspondence `Gamma_S` with place-dependent `(1, p)` bidegree (= PROP-global
= R1 + M4 bundled for the literal object). Two concrete moves, in priority order:

1. (Construction, the real target.) Attack the BASE, not another survey. The sharpest
   buildable target is the strictly-construction-weaker object of section 3: a single
   arithmetic carrier (relative surface over an auxiliary curve, or an arithmetic
   3-fold) hosting `H`-odd with a Frobenius/flow cycle class of bidegree `(1, p)`, on
   which Yuan-Zhang's adelic index applies directly, with the OPEN step being SHARP (not
   generic) Hodge-standard positivity on the primitive part. Hand this to BUILDER as the
   Arakelov-side restatement of M4, explicitly noting it inherits R1 (Deligne-purity
   sourcing of the `sqrt(p)`-pure carrier) and the `(1, p)` archimedean assembly
   obstruction (#25).

2. (Cheap, do first.) Apply the verified repo correction: fix `2K_spec_z_squared_dictionary.md`
   section 6b to "Morishita 2025 (arXiv:2508.15971)," matching the landscape doc, and
   add the new Connes-Consani Jacobian (arXiv:2602.15941) to the spec_z landscape /
   2P scorecard as a trace-side 2026 datapoint (Picard monoid + Abel-Jacobi +
   explicit-formula-as-Lefschetz-trace, no pairing / no polarization / no eigenvalue
   correspondence). Add Bost theta, Moriwaki, and CGHX as corpus nodes.

The honest frame for ORCHESTRATOR: this probe confirms the Arakelov face is the
mirror, not the escape. It does not move the open kernel. The remaining work is
construction-grade (build the base), the same place every all-roads convergence has
left the program.

## Connections

- AHK closure: LEARNINGS #129/#130; `sourcing_gap_r1.md` (the two variety-gated facets).
- 2K ([2K](2K_spec_z_squared_dictionary.md)): the would-be intersection numbers and the gap = product surface.
- 2J ([2J](2J_arakelov_adjunction.md)): the arithmetic adjunction `omega-bar^2 = 12 h_Fal`; e2ae computes it.
- 2H ([e2h](e2h_arithmetic_hodge_index.md)): Faltings-Hriljac is a theorem on one arithmetic surface (ranks 1-3 validated).
- 2P ([2P](2P_recent_global_signed_trace_pairing_probe.md)): the 2026 trace-vs-pairing scorecard (Connes-Consani Jacobian = trace not pairing).
- e2ad ([e2ad](e2ad_fh_gamma_certificate.md)): the height-to-L link is BSD (central derivative at s=1), NOT the FE Gamma-factor (the two withdrawn moves).
- e2ae ([e2ae](e2ae_petersson_faltings.md)): the computed archimedean self-intersection (this probe's artifact).
- `spec_z_cohomology_landscape.md`: NODE-ahk-too-blind vs NODE-fh-too-local; the 4-property M4 decomposition (PROP-global = the base).
- Direction 8 ([08_hodge_index_surface.md](../../docs/03_research/research_directions/08_hodge_index_surface.md)): the surface to build.
