# 2G: positivity from a SIGNATURE -- the Weil template for Direction 8

> Experiment [e2g_intersection_signature.py](e2g_intersection_signature.py). Opens
> [Direction 8](../../docs/03_research/research_directions/08_hodge_index_surface.md),
> the project's central open problem (the Hodge index theorem on a constructed
> arithmetic surface below Spec(Z)). This experiment makes the **function-field
> template** computational and exact: it builds the intersection form whose
> SIGNATURE is the Hodge index theorem, and shows that signature *is* the
> Hasse-Weil bound. It realizes Direction 8 milestones 5.1 (state the Hodge index
> precisely) and 5.5 (Weil specialization / K3) in verifiable form.

## Why this, and why now

2F exhibited the function-field RH bound `|alpha_i| = sqrt(q)` from point counts.
But that bound is the *consequence*; the *mechanism* is the Hodge index theorem on
the surface `C x C`, which 2F never builds. Direction 8's entire bet is that
RH-positivity must come from the SIGNATURE of an intersection form (the unique K1
escape route, per R3.5). So the right first move is to make that signature
concrete in the one world where it is a theorem, giving an exact target the
Spec(Z) lift must reproduce.

This also closes a loop with the session's earlier work (3M). 3M decomposed the
Weil quadratic form -- the **trace / explicit-formula side** (Architecture 3) --
and found its positivity is circular as a proof route (R3.5 / K1: a trace
identity cannot found RH). 2G is the **signature side** (Architecture 2) of the
*same* positivity. In the function-field world both exist and agree; the signature
side is non-circular. That contrast is the whole reason Direction 8 is the target.

## The construction (Weil 1948, computational)

On `S = C x C` for `C` of genus `g` over `F_q`, take
`e = {P} x C`, `f = C x {P}`, the diagonal `Delta`, and `Gamma` = graph of the
q-power Frobenius. Classical intersection numbers:

```
e^2 = f^2 = 0,   e.f = 1,
e.Delta = f.Delta = 1,   Delta^2 = 2 - 2g          (adjunction),
e.Gamma = 1,   f.Gamma = q   (Frobenius is a (1, q) correspondence),
Delta.Gamma = N_1 = #C(F_q)  (Lefschetz),   Gamma^2 = q(2 - 2g).
```

`{e, f}` is a hyperbolic plane (signature (1,1)). Project out:
`Delta_0 = Delta - e - f`, `Gamma_0 = Gamma - q e - f`. Using
`D_0.E_0 = D.E - (D.e)(E.f) - (D.f)(E.e)`:

```
G_prim = [[ Delta_0^2 , Delta_0.Gamma_0 ]   =  [[ -2g , -t  ],     t = q + 1 - N_1
          [ .         , Gamma_0^2       ]]      [ -t  , -2gq ]]    (Frobenius trace)
```

## Result (exact, across the curve family)

Genus-1 (q in {5,7,11,13}) and genus-2 (q in {5,7,11}) curves, all checks pass:

| check | outcome |
|---|---|
| full Gram `{e,f,Delta,Gamma}` signature | **(1, 3)** for every curve (Hodge index: exactly one positive eigenvalue) |
| primitive Gram `{Delta_0, Gamma_0}` | **negative definite (0, 2)** for every curve |
| Hasse-Weil `\|t\| < 2g sqrt(q)` | holds for every curve |
| signature condition `<=>` Hasse-Weil | consistent for every curve |

**The headline identity.** The primitive form is negative definite
`<=> det(G_prim) > 0 and trace < 0 <=> 4 g^2 q - t^2 > 0 <=> |t| < 2g sqrt(q)`.
The Hasse-Weil / Riemann bound is *literally* the negative-definite signature
condition. Iterating over Frobenius powers `phi^n` (with `t_n = q^n + 1 - N_n`)
gives `|sum alpha_i^n| <= 2g q^{n/2}` for all `n`, which forces
`|alpha_i| = sqrt(q)`. **Positivity from a signature, not from a trace identity.**

## K1 / K2 / K3

- **K3 (Weil specialization):** this experiment *is* the function-field case,
  exact. The Direction 8 proof must restrict to exactly this.
- **K1 (no-shortcut escape):** the load-bearing step is the *sign* of the
  eigenvalues of an intersection Gram matrix, not a trace identity. This is the
  structural feature R3.5 demands; the bound fails the instant the primitive form
  acquires a non-negative eigenvalue. (Contrast 3M: the explicit-formula
  positivity is a trace identity, hence circular.)
- **K2 (D-H discipline):** the construction is *unbuildable* for
  Davenport-Heilbronn. No Euler product => no Frobenius endomorphism => no graph
  `Gamma`, no surface, no `Delta^2 = 2 - 2g`. The geometric face of the 3M
  finding: no Euler product `<=>` the von Mangoldt weight delocalizes off prime
  powers `<=>` no Frobenius correspondence to place on the surface.

## What the Spec(Z) lift must reproduce (the precise gap)

The template names exactly what is missing over `Spec(Z)`. Each ingredient has a
known obstruction:

| function-field ingredient | Spec(Z) analogue | status |
|---|---|---|
| the surface `C x C` | `Spec(Z) x_{F_1} Spec(Z)` | does not exist as a classical scheme (Direction 1/2) |
| Frobenius graph `Gamma` | an "arithmetic Frobenius" flow (Deninger) | no construction (Direction 3/4) |
| `Delta^2 = 2 - 2g`, `Gamma^2 = q(2-2g)` | self-intersections via an arithmetic intersection theory | Arakelov/Faltings give a *partial* pairing; the relevant surface is absent |
| hyperbolic `{e, f}` + negative-definite primitive part | a `(1, k)` signature on the arithmetic NS | **the central open problem** |
| the archimedean place | the "point at infinity" compactifying `Spec(Z)` | candidate for the missing second hyperbolic direction (Arakelov) |

The honest reading: the *template* is completely clear and now exact in code; the
*lift* is the open problem, and it is open at the very first ingredient (the
surface itself). The arithmetic Hodge index theorem of Faltings-Hriljac *does*
hold for a single arithmetic surface (a curve over `Spec(O_K)`), with signature
`(1, rho-1)` -- the encouraging precedent. What is missing is the surface
`Spec(Z) x Spec(Z)` and a Frobenius correspondence on it; that, not the index
theorem per se, is where Direction 8 is stuck.

## Status and next step

- **Solid:** the function-field signature template is exact and verified across
  genus 1-2; the Hasse-Weil bound is exhibited as the negative-definite signature
  condition; K1/K2/K3 readings are explicit.
- **Next (Direction 8 proper):** the arithmetic-surface lift. The most tractable
  sub-question to make computational next is the **Arakelov / Faltings-Hriljac
  arithmetic Hodge index on a single arithmetic surface** (which is a theorem),
  to see how the archimedean place enters the signature -- the closest existing
  object to the missing `Spec(Z) x Spec(Z)` pairing, and the natural bridge from
  this template toward the central problem.

## Outputs

- `e2g_intersection_signature.npz`: per-curve Gram matrices, signatures, margins.
- `e2g_intersection_signature.png`: primitive eigenvalues + Hasse-Weil margin across the family.
