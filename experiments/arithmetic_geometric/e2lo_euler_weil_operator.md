# 2LO: the Euler Weil operator C_E, built or not built from geometric data

> Companion for [`e2lo_euler_weil_operator.py`](e2lo_euler_weil_operator.py).
> Run: `python -m experiments.arithmetic_geometric.e2lo_euler_weil_operator`.
> Result artifact: [`e2lo_euler_weil_operator.npz`](e2lo_euler_weil_operator.npz).

## Question

2LN (#69) showed Petrov non-semisimplicity is routable but unhelpful: the
nilpotent dies on the primitive quotient, and the positivity gap relocates to the
SIGN of the primitive monodromy form, fixed by the archimedean Weil operator
`C_E`. 2LN Part 4 isolated the missing datum as the geometric Frobenius/Lefschetz
operator.

2LO tests the construction target from
[`euler_sen_polarization_attempt.md`](../../../docs/03_research/euler_sen_polarization_attempt.md)
literally:

```text
A_E := Omega^{-1} B_E
C_E := A_E (-A_E^2)^{-1/2}     (polar / functional-calculus complex structure)
```

The danger, sharpened by the 2MM K1 audit (#68): `B_E` must be built geometrically
from Euler/Frobenius data (the `(1,p)` bidegrees, #25) plus the archimedean metric,
NOT imported from the Weil form or from zero locations. If `B_E` is supplied, the
polar formula only transports its signature.

## Method

Four kill conditions from the proposal, plus a basis-invariance audit.

- **Part 1 (function-field specialization).** With `B_E = [[2g,t],[t,2gq]]` and
  `Omega` symplectic, `A_E^2 = (t^2 - 4 g^2 q) I`, so `-A_E^2` is positive
  definite iff `t^2 < 4 g^2 q`. Then `C_E = A_E (-A_E^2)^{-1/2}` is an
  `Omega`-compatible complex structure (`C_E^2 = -I`) and `Q(x,y) = Omega(x, C_E y)`
  is the Rosati polarization, positive definite exactly in the Hasse-Weil window.
  Swept over `g in {1,2}`, `q in {5,7,11,13}`.
- **Part 2 (K1 audit, the crux).** The `(1,q)` bidegree is shared by every curve
  over `F_q`; the trace `t = q + 1 - #E(F_q)` is strictly finer. We exhibit the
  admissible traces inside the window, all with the identical bidegree, and check
  whether `C_E` differs across them.
- **Part 3 (archimedean/FE-only bypass = kill condition 2).** A `C_E` built from
  functional-equation / archimedean data alone forms for any object with an FE,
  including D-H, hence is D-H-blind and dead.
- **Part 4 (K2 / D-H discipline).** Data-based `has_euler_product` formation guard
  (not a name match); injected off-line zero defect `|1 - 2 beta| ~ 0.617`.
- **Audit (basis invariance).** Symplectic-compatible random conjugation.

## Results

| check | result |
|---|---:|
| Part 1: rows swept (`g in 1..2`, `q in 5,7,11,13`) | `206` |
| Part 1: `C_E` polarization positive iff `t^2 < 4 g^2 q` | `True` (0 mismatches) |
| Part 1: worst `C_E^2 + I` residual | `7.2e-15` |
| Part 1: `q=5,t=4` inside | `C_E` exists, `Q` sig `(2,0,0)` POS |
| Part 1: `q=5,t=5` outside | `C_E` does not exist (`-A_E^2` min eig `-5.0`) |
| Part 2: bidegree `(1,5)` admissible traces | `9` |
| Part 2: distinct `C_E` across those traces | `9` |
| Part 2: bidegree + archimedean determines `t`/`B_E` | `False` (K1 fails) |
| Part 3: FE-only `C_E` forms for D-H | `True` (D-H-blind, dead) |
| Part 4: D-H and renamed D-H form | `False` / `False` |
| Part 4: injected off-line zero defect | `0.617` |
| Audit: basis invariance | `True`, max residual `2.6e-13` |

## Verdict

**2LO is a NEGATIVE coordinate, sharply.**

The polar formula `C_E = A_E (-A_E^2)^{-1/2}` works perfectly AFTER `B_E` is
supplied: it forms a genuine complex structure (`C_E^2 = -I` to `1e-15`) and
recovers the finite-field Rosati sign exactly, positive iff `t^2 < 4 g^2 q`
(Part 1, the kill-condition-4 reduction to `HodgeIndex.negDef_iff_hasseWeil`).

But finite Euler-Sen linear algebra does NOT construct `B_E` from the `(1,p)`
bidegrees plus archimedean data (Part 2). The bidegree `(1,q)` is shared by every
curve over `F_q`, while the trace `t = q + 1 - #E(F_q)` is strictly finer: nine
admissible traces over `F_5` give nine distinct `C_E`. The trace is the global
Frobenius point count, not a local bidegree, so the only non-circular way to fill
it is the global Frobenius/Lefschetz signed trace pairing, equivalently the
product-surface / prismatic Poincare-duality assembly (Direction 8). That is
exactly the open step.

This matches the standing K1 burden after 2MM (#68): the finite Euler-Sen
formalism transports a supplied `B`, but does not prove positivity or construct
the arithmetic `B` geometrically. 2LO adds the precise reason: the missing piece
is the trace `t`, the global object the bidegree cannot see.

## Discipline Status

**K1.** Fails CONSTRUCTIVELY and that is the deliverable: `B_E` (specifically the
Frobenius trace `t`) cannot be built from the non-circular inputs. Importing `t`
from a Weil form or known zeros would be circular; supplying it geometrically is
the product surface.

**K2.** Two layers. The geometric construction is blocked for D-H and a renamed
D-H by the data-based `has_euler_product` guard. The FE-only bypass forms for D-H
(it has a functional equation), which is precisely why an FE/archimedean-only
`C_E` is dead: D-H-blind. The discriminating content must ride the Euler/Frobenius
side, never the shared FE/archimedean side.

**Petrov.** Inherited from 2LN: the construction is on the primitive quotient
where the nilpotent has already died; 2LO is about the SIGN, not the nilpotent.

**Scope.** Finite linear algebra plus a degree-of-freedom count, not absolute
prismatic cohomology. Proves nothing about RH. The value: the polar `C_E`
construction is sound and reduces to the proved function-field signature, but the
sign over `Spec(Z)` is the global Frobenius/Lefschetz trace pairing, the same gap
as the product surface.
