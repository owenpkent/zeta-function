# 2CC.4 — The soft-max de-idempotentization does NOT restore the Frobenius trace t (the Connes-Consani signed-pairing handle is closed)

> Direction 8 (the product surface), adversarial follow-up to [2CC](e2cc_tropical_shadow.md)
> (#40, the tropical shadow is t-blind) and [2CC.3 / LEARNINGS #42](../LEARNINGS.md)
> (soft-max removes the characteristic-1 idempotency). Code:
> [`e2cc4_adversary_probe.py`](e2cc4_adversary_probe.py). Generated and run by an ADVERSARY
> agent during the "where could we move the needle" workflow (2026-06-04), then reviewed and
> re-run by hand. Companion: reading note
> [Connes-Consani-2015](../../docs/03_research/reading_notes/Connes-Consani-2015-Geometry-Arithmetic-Site.md).

## The move under test

#42 found that the characteristic-1 operations on the Connes-Consani square are idempotent
(no subtraction, hence no signed intersection pairing, hence no Hodge index), but that a
finite-β **soft-max** `a (+)_β b = (1/β) log(e^{βa}+e^{βb})` removes the idempotency (the
scalar defect `log2/β ≠ 0`). The candidate move (Tier-2 handle in the needle-map) **speculated**
that carrying that deformation into the bilinear form might **restore the Frobenius trace t** —
the curve-dependent quantity the β=∞ mixed-volume form froze at `Δ·Γ = p − 1`, where the
function-field target is `Δ·Γ = q + 1 − t` with t roaming the Hasse-Weil window
`(√q − 1)² .. (√q + 1)²`.

## Method (three honest readings, because "soft-deform the pairing" is ambiguous)

On the divisor shadow `{e=(1,0), f=(0,1), Δ=(1,1), Γ=(1,p)}`:

- **R1** — de-idempotentize the SCALAR pairing: replace `|det(u,v)|` by `soft|x| = (1/β)log(e^{βx}+e^{-βx})` in every Gram entry.
- **R2** — smooth the POLYGON corners: thicken each divisor segment by a radius `~1/β` disk (Minkowski sum) and recompute the EXACT Euclidean mixed area `2·V(A,B)`.
- **R3** — the structural test: at FIXED p, can any function of β make `Δ·Γ` roam the Hasse-Weil window, i.e. is there a second free knob detached from p?

## Results (p = 5, q = 5 target; reproduced by hand-run)

- Both R1 and R2 recover the frozen `Δ·Γ = p − 1 = 4` at β = ∞ (sanity).
- At finite β, `Δ·Γ(β, p)` is a SINGLE deterministic number per (β, p). The deviations from `p − 1` are a fixed function of (β, p) with NO independent parameter:
  - R1: deviations at β=0.5 for p=3,5,7 are `+0.254, +0.036, +0.005` (vanish as p grows; pure scalar-softening, lattice-independent).
  - R2: deviations at β=0.5 for p=3,5,7 are `+43.4, +51.1, +59.0` (this is the perimeter/area inflation of the thickening, monotone in p, NOT a free t).
- No reading ever leaves the single-point value to roam the Hasse-Weil window `(1.53, 10.47)` at fixed p.

## Verdict

**The trace t is NOT restored; the soft-max handle on the Connes-Consani square is closed.**
The soft-max genuinely de-idempotentizes the scalar semiring (defect `log2/β`, real), but the
combinatorial area pairing is a determinant `|det(u,v)|` of the lattice direction vectors,
which **has no t to begin with**: t is a point count `q + 1 − t`, strictly finer than the
`(1,p)` bidegree (#25), and four distinct genus-1 curves over `F_5` share the identical slope
data. Smoothing corners (R2) perturbs entries by `O(1/β)` lattice-independent amounts, not a
curve-dependent t. Soft-max cannot refine a bidegree into a point count.

## Consequence for the program

This closes the soft-max route to the missing signed pairing for the whole C-C-square family.
In the needle-map (2026-06-04), it is why the most attackable handle on milestone M4 (the
arithmetic Hodge standard conjecture) is the **Bhatt-Lurie WCart substrate** (Frobenius F +
Sen Θ on one stack, prismatic Poincaré duality via Tang), **not** the Connes-Consani signed
pairing. A negative coordinate that prunes a Tier-2 handle.

## Honest scope

R1/R2 are decisive computations on the divisor shadow (the same `e2cc_tropical_shadow`
machinery), not a constructed intersection theory of the topos; R3 is a degree-of-freedom
count, not a no-go theorem about every conceivable de-idempotentization. It falsifies the
SPECIFIC soft-max mechanism the move proposed. Proves nothing about RH; closes one candidate
route, which is how this project measures progress.
