# 2P+: do recent constructions supply a global signed trace pairing carrying t?

> Literature-grounded Direction 8 audit, 2026-06-05. Companion to the
> [Spec(Z) cohomology landscape](../../docs/03_research/spec_z_cohomology_landscape.md).
> No new finite model, no min-eigenvalue panel, no Hodge-star run: this memo only
> asks whether an actually-constructed 2024-2026 object supplies the one missing
> datum that 2LN (#69) and 2LO (#70) isolated.

## The question

2LN reduced the WCart direct-polarization route to the SIGN of the primitive
monodromy form, and 2LO showed the local polar Weil operator
`C_E = A_E(-A_E^2)^{-1/2}` recovers the function-field Rosati sign exactly but
cannot construct `B_E` from the `(1,p)` bidegrees plus archimedean data: the
`(1,q)` bidegree is shared by all curves over `F_q`, while the Frobenius trace
`t = q + 1 - #E(F_q)` is strictly finer. The one open datum is the **global
Frobenius/Lefschetz signed trace pairing carrying `t`**, equivalently the
product-surface / global-prismatic correspondence `Gamma_S` (Direction 8).

This memo scores three of the strongest recent constructions against exactly that
column: does the object produce a **signed (polarization-shaped) pairing** on a
global `H^1` over `Spec(Z)` whose value sees the trace `t`, not merely the
bidegree? Perfectness is free (the functional equation gives a perfect pairing
even for Davenport-Heilbronn, 2HH/#61); POSITIVITY carrying `t` is the gap.

The D-H discipline is applied as a real-time classifier: a construction is
RH-relevant precisely when it CANNOT be built for D-H (no Euler product => no
Frobenius => no `t`).

## Candidates and verdicts

| Candidate | What it supplies | Where it stops |
|---|---|---|
| **Tang**, *Syntomic cycle classes and prismatic Poincare duality* ([arXiv:2210.14279](https://arxiv.org/abs/2210.14279), Compositio) | perfect prismatic / F-gauge Poincare duality `RGamma(X)^vee ~= RGamma(X){d}[2d]`, a diagonal copairing, and trace maps | **perfectness, not the Hodge-Riemann / Rosati sign** |
| **Gurney**, *Prismatization over Z* ([arXiv:2301.12392](https://arxiv.org/abs/2301.12392)) | a global integral prismatization substrate over `Spec(Z)`; perfect cohomology under proper smooth hypotheses | **global construction / perfectness, not a cup / sign / `t`** |
| **Connes-Consani**, *On the Jacobian of $\overline{\mathrm{Spec}\,\mathbb{Z}}$* ([arXiv:2602.15941](https://arxiv.org/abs/2602.15941), Feb 2026) | Picard / Jacobian monoids, spectral realization, Weil's explicit formula reinterpreted as a trace formula | **trace / realization, not a signed product-surface pairing** |

### Tang: the strongest DUALITY input

Tang constructs F-gauges over a prism, syntomic cycle classes, and proves
prismatic Poincare duality for proper smooth schemes: for `X/A/I` proper smooth
of dimension `d`, a canonical isomorphism of F-gauges
`RGamma(X/A)^vee ~= RGamma(X/A){d}[2d]`, with a trace map from the diagonal
(Grothendieck duality / the conjugate-filtered trace). This is exactly ingredient
(ii) of the product-surface program (a perfect cup into a fundamental class) at
the level of complexes, with **no positivity**. The duality is perfect; it is not
a polarization. A polarization is a duality compatible with a positive Hermitian /
Rosati structure (Hodge-Riemann), and the prismatic duality carries no such
positive structure. So Tang supplies the perfect-pairing half of M4 organ (a) and
leaves the SIGN, which is the entire gap (2HH/#61, 2LN/#69, 2LO/#70).

### Gurney: the strongest GLOBAL SUBSTRATE input

Gurney extends the p-adic Drinfeld / Bhatt-Lurie prismatizations to a global
integral prismatization functor over `Spec(Z)`, compares it to p-adic
prismatization and filtered de Rham cohomology, and proves perfection of the
cohomology under proper smooth hypotheses. This is the global stack in which a
future Frobenius correspondence `Gamma_S` and its cup pairing could live, but the
construction itself produces no cup form, no signed pairing, and no trace formula
carrying `t`. It supplies the SUBSTRATE, not the theorem.

### Connes-Consani 2026: the strongest TRACE-REALIZATION input

The 2026 Jacobian paper interprets the Riemann sector of the adele class space as
a monoidal extension of the Picard group and builds Picard / Jacobian monoids
incorporating singular strata for spectral realization, with framed/rooted divisor
duality, and explicitly reinterprets Weil's explicit formula as a trace formula.
The paper itself contrasts the function-field mechanism (Frobenius on the
Jacobian) with the number-field mechanism (the Picard-monoid / idele-class
action). This is a trace-side realization, the same place every NCG framework
lands (R3.5: trace positivity <=> RH, the K1 wall, #65). It is not a
Hodge-Riemann / Rosati signed product pairing.

## Net

**Negative coordinate, but sharp.** None of the three constructions supplies the
signed `t`-carrying pairing. They stop at three DIFFERENT adjacent inputs:

- Tang supplies **perfectness** (the duality), not the sign.
- Gurney supplies the **global substrate**, not the cup / sign / `t`.
- Connes-Consani supplies the **trace / realization**, not the signed pairing.

The post-2LO gap is therefore unchanged and is the SAME theorem for all three:
construct the product-surface or global-prismatic Frobenius correspondence
`Gamma_S`, form the primitive cup / intersection pairing into the Euler-pole
`H^2`, and prove the Hodge-Riemann / Rosati sign without RH input. The three
candidates are not three different gaps; they are three different two-thirds of
the SAME construction, each missing the sign that carries `t`.

This is consistent with the universal-gap reading of
[spec_z_cohomology_landscape.md](../../docs/03_research/spec_z_cohomology_landscape.md):
every candidate realizes the trace or a perfect pairing; none carries the
polarization. Supplying the polarization IS RH.

**Bracket update (2026-06-27, [2L](2L_arakelov_face_probe.md) §4).** The three
candidates above are the realization-side near-misses (perfect pairing / global
substrate / trace). The 2L Arakelov-face probe surveyed the *other* near-miss
bracket, the single-scheme generalized arithmetic Hodge index (`NODE-fh-too-local`),
and added three corpus nodes there: Moriwaki (higher-dimensional arithmetic Hodge
index on a fixed variety), Cantat-Gao-Habegger-Xie (which *uses* the single-variety
index for the geometric Bogomolov conjecture), and Bost theta-invariants
(infinite-dimensional Arakelov over the arithmetic curve, but a Diophantine
$h^0_\theta$ scalar = the wrong signature class). All certify a *fixed* scheme's own
data and never reach zeta's zeros, so they do not enter this memo's global-signed-
pairing column; they bracket the gap from the polarization-proven-but-too-local side
while Tang/Gurney/Connes-Consani bracket it from the realization side.

## Honest scope and discipline

- Structural classification, web-confirmed for Tang (F-gauge perfect duality +
  trace map, no polarization language) and consistent with the repo-verified
  landscape entries for Gurney and Connes-Consani (verified against the originals,
  arXiv:2301.12392 and arXiv:2602.15941). The specific theorem/remark loci in Tang
  (the diagonal copairing and the trace-map remark) are cited from the paper; the
  load-bearing claim is the structural one (perfect, not signed), independently
  corroborated by the absence of `polarization` / `Rosati` / `Hodge-Riemann` /
  `signed` terminology in the inspected text.
- D-H discipline: all three would fail to carry `t` for a non-Euler L, because `t`
  is the Frobenius point count and D-H has no Frobenius. The discriminating datum
  rides the Euler/Frobenius side, never the shared FE/archimedean side.
- Proves nothing about RH. The deliverable is a per-candidate coordinate on
  Direction 8: each construction's specific missing third, and that they are the
  same theorem.
