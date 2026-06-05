# Frobenius cup target formation spec

> Written 2026-06-04 as the concrete execution of the "state the main conjecture
> as a standard-conjecture problem" move. Companion to
> [`research_directions/08A_rosati_standard_conjecture.md`](research_directions/08A_rosati_standard_conjecture.md),
> [`spec_z_cohomology_landscape.md`](spec_z_cohomology_landscape.md), and the Lean
> artifact [`../../lean/ZetaRH/FrobeniusAlgebra.lean`](../../lean/ZetaRH/FrobeniusAlgebra.lean).

## Purpose

The Direction 8 target should be stated as a formation problem before it is stated
as a positivity theorem:

> Euler product data -> local Frobenius bidegrees `(1,p)` -> Tate-twist `H^2`
> fundamental class -> cup target `H^1 x H^1 -> H^2` -> Hodge-Riemann positivity.

The final arrow is RH. The earlier arrows are the structural formation rules that
keep the route K2-safe. Davenport-Heilbronn has a functional equation and trace
formula data, but no Euler product; therefore it should fail before positivity is
even discussed. The failure must be structural, not a string guard and not a
manual deletion of a composite block.

## The data

**1. Euler product data.** For an L-function `L`, the first datum is not the
functional equation. It is a proof/object witnessing that `L` has an Euler product,
with local factors indexed by primes. In the future full definition this should
include convergence on `Re(s) > 1`, uniqueness of local factors, and the
log-derivative/von-Mangoldt expansion. The minimal Lean formation object is
`EulerProductData L`, whose first field has type `L.has_euler_product`.

**2. Local Frobenius bidegrees.** Direction 8's specific arithmetic content is that
the Frobenius correspondence has place-dependent bidegree `(1,p)`, not a single
function-field bidegree `(1,q)`. This is the trace column D-H lacks. In Lean this is
recorded by the field

```lean
bidegree_eq : forall p : Nat.Primes, bidegree p = (1, p.val)
```

This is only the formation-level fingerprint, not the future cycle-class theorem.

**3. The Frobenius Tate twist.** The cup product must land in the Euler-pole target
`H^2`, the arithmetic analogue of `C(-1)`. This target is not supplied by the
functional equation alone. It is formed from Euler/Frobenius data:

```lean
structure FrobeniusTateTwist (L : LFunction) where
  euler : EulerProductData L
  carrier : Type
  fundamentalClass : carrier
```

The `fundamentalClass` field is a placeholder for the future residue/pole
identification. The point now is formation: if `EulerProductData L` cannot exist,
then neither can the `H^2` target.

**4. The cup target.** The M4 organ (a) target is then

```lean
structure FrobeniusCupTarget (L : LFunction) where
  twist : FrobeniusTateTwist L
  H1 H2 : Type
  cup : H1 -> H1 -> H2
  trace : H2 -> twist.carrier
  trace_hits_fundamental : exists h : H2, trace h = twist.fundamentalClass
```

This deliberately omits the hard parts: bilinearity, perfectness, the flow
derivation law, primitive decomposition, and positivity. Those are M4. The current
structure only states when the target is allowed to form.

## Formation rules

**Rule A: FE is not enough.** A functional equation can give the shadow of
duality, and D-H has that. It does not supply the Euler-pole `H^2` target or the
local `(1,p)` Frobenius bidegrees.

**Rule B: no Euler product means no cup target.** In Lean:

```lean
theorem cupTarget_requires_eulerProduct {L : LFunction} :
    CanFormCupTarget L -> L.has_euler_product
```

For Davenport-Heilbronn this specializes to:

```lean
theorem no_dh_cupTarget :
    not (CanFormCupTarget davenport_heilbronn)
```

This is the clean replacement for the 2KK string guard. D-H is excluded because
the target contains Euler-product data as a field, and D-H's field is `False`.

**Rule C: zeta formation is not zeta positivity.** The Lean file includes toy
formation witnesses for zeta because the current substrate sets
`zeta_function.has_euler_product := True`. These witnesses prove only that the
target is formable in the present abstract model. They do not prove a cup product
law, a polarization, or RH.

**Rule D: deleting `P_comp` is not a formation theorem.** For zeta,
`P_comp = 0` is just the Euler product. For a non-Euler object, forcing
`P_comp = 0` is imposing the geometry by hand. The formation spec avoids this by
making Euler/Frobenius data a prerequisite, rather than taking a matrix and
projecting away the offending support.

## What remains open

The spec moves no RH mass by itself. It only pins down where the mass is:

- construct the real global arithmetic `H^1`, not the toy `Unit`;
- identify the Frobenius Tate twist with the Euler-pole fundamental class;
- prove Poincare duality and the flow derivation law;
- build an intrinsic polarization that survives the Petrov non-semisimplicity
  obstruction;
- prove Hodge-Riemann positivity on the primitive part without RH input.

That last item is the arithmetic Hodge standard conjecture. The formation spec is
the guardrail that keeps false positives from reaching it.
