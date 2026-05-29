# 2Q: the place-dependent bidegree obstruction -- what `Gamma_S` must be

> Experiment [e2q_frobenius_bidegree.py](e2q_frobenius_bidegree.py). Direction 8 /
> the product surface. Companion to [2K](2K_spec_z_squared_dictionary.md) (the
> dictionary) and [2J](2J_arakelov_adjunction.md) (the adjunction). 2K established
> that every intersection NUMBER of the would-be surface `S = Spec(Z) x Spec(Z)`
> is computable and validated on a single arithmetic surface, and that the one
> missing object is the product surface and its Frobenius correspondence `Gamma_S`.
> 2Q asks the next sharp question: granting the dictionary, what must `Gamma_S`
> actually BE, and where exactly does the function-field rigidity break?

## 1. The rigidity that breaks (recalled from 2G)

On `C x C` the Frobenius graph `Gamma` is a **`(1, q)` correspondence**:
`e.Gamma = 1`, `f.Gamma = q`. The single number `q` is the residue-field
cardinality, **constant over the whole curve**. Everything downstream rides on
that one scale:

```
Gamma^2 = q (2 - 2g)              the scale multiplies the adjunction self-int
G_prim  = [[-2g, -t], [-t, -2gq]]
neg.def <=> 4 g^2 q - t^2 > 0 <=> |t| < 2g sqrt(q)        (Hasse-Weil / RH)
```

RH for the curve is an **algebraic inequality in two integers** (`t` and the
single scale `q`), because the surface is finite-type and `H^1` is
`2g`-dimensional. The experiment reconfirms this across the genus-1 family: each
curve sits at exactly one scale `q`, and `4 g^2 q - t^2 > 0` for every one.

## 2. Where it breaks over Spec(Z)

`Spec(Z)` has no single residue cardinality: the fibre over the prime `p` is
`Spec(F_p)`, of cardinality `p`. The arithmetic Frobenius correspondence `Gamma_S`
therefore **cannot be a `(1, q)` correspondence for any single `q`**. Its second
bidegree is **place-dependent**: locally at `p` it is a `(1, p)` correspondence
(the geometric Frobenius of `F_p`). Equivalently, the prime side of the explicit
formula carries the weights `{log p}`, which are unbounded with no single value.
The experiment quantifies the obstruction directly: over the first 40 primes the
spread of required scales `max(p)/min(p)` is already `86.5` and diverges. No
single `q` fits all places.

Three consequences, each a structural fact (not numerology):

1. **No single scale `q`.** A 2G-style finite primitive Gram with one scale
   cannot exist; the would-be Gram is **block-graded over the places**, with scale
   `p` in the `p`-block. Any single effective `q` is overdetermined and
   inconsistent.
2. **Infinite genus.** With one place-block per prime power, `H^1` is
   **infinite-dimensional**: the signature statement is a genuine
   infinite-dimensional **index theorem**, not a `2x2` determinant. This is
   exactly Deninger's "the `H^i` are infinite-dimensional," now derived from the
   bidegree rather than posited.
3. **`Z`-action becomes `R`-flow.** A single Frobenius `x |-> x^q` generates a
   `Z`-action with one log-scale `log q`. Place-dependent log-scales `{log p}`
   that must act simultaneously and commensurably **force a continuous `R`-action**:
   the flow `Phi_t = prod_p U_{log p}^{t/log p}` of Directions 2/4. The flow is
   not an aesthetic choice; it is the only object that carries a continuum of
   commensurable local scales. 2Q makes that necessity explicit.

## 3. The reverse-engineered constraint on `Gamma_S^2`

In the function field, `Gamma^2 = q * Delta^2` (the single scale times the
adjunction self-intersection). Over `Spec(Z)`, with no single `q` and with the
adjunction self-intersection now **computed** (2J/2L: `omega-bar^2 = 12 h_Fal` per
elliptic fibre, the arithmetic `2 - 2g`), the analogue cannot be a single product.
It must be the **regularized prime-weighted sum** the explicit formula already
supplies:

```
"Gamma_S^2"  =  reg-sum_p (log p) * (local self-intersection at p)
             =  the von Mangoldt prime side P_fin (2K), read as the regularized
                self-pairing of the correspondence
             =  det_zeta(s - Phi_t | H^*_{F,pr})   (the Direction 4.6 determinant)
```

So `Gamma_S` is pinned to a sharper, falsifiable target than "a Frobenius graph on
`S`": a correspondence with **place-dependent bidegree `(1, p)`** whose
**regularized self-intersection is the von Mangoldt prime sum**, with per-fibre
adjunction input `12 h_Fal` already in hand.

## 4. The sharper K2 (Davenport-Heilbronn)

This refines 2G's K2 reading from "D-H has no Frobenius, no `Gamma`" to a statement
about **bidegree**: a `(1, p)` local bidegree at each prime *is* the Euler factor
`(1 - p^{-s})^{-1}`. D-H has a functional equation (hence a zero/genus structure)
but **no Euler product**, so its von Mangoldt analogue delocalizes off prime powers
(the 3M finding, #20): there are no clean per-place local degrees to assemble into
`Gamma_S`. The place-dependent-bidegree correspondence **requires** the Euler
product:

```
no Euler product  <=>  no local (1, p) bidegrees  <=>  no Gamma_S  <=>  no surface.
```

The wrong-approach discipline is now a statement about the correspondence's
bidegree, the most geometric form of it yet.

## 5. Why this is progress, not reformulation

2K was a dictionary (which block plays which role). 2Q adds three things the
dictionary did not contain:

1. It identifies the **precise rigidity that breaks** (single scale `q` -> a
   place-dependent spectrum `{p}`), and shows quantitatively that no single scale
   survives. This is *why* the surface cannot be a finite-type scheme, derived
   rather than asserted.
2. It **derives** the two headline features of Deninger's program (infinite-
   dimensional `H^i`; the `R`-flow rather than a `Z`-action) from the bidegree,
   turning them from inputs into consequences.
3. It **pins `Gamma_S^2`** to a computed object (the von Mangoldt prime sum / the
   Direction 4.6 regularized determinant), and recasts the D-H discipline as a
   bidegree statement.

Together these convert "build the surface" one notch further: the correspondence
`Gamma_S` now has a specified bidegree structure `(1, p)` per place and a specified
regularized self-intersection, and the only freedom left is the realization of
these as honest intersection numbers on a 2-dimensional object. That realization
is Direction 4 (the foliation carrying the flow) feeding Direction 8 (the index
theorem). The falsification: if no correspondence can carry a place-dependent
bidegree on a single 2-dimensional arithmetic object, the classical-scheme route
is dead and only the foliated/flow route survives -- which is exactly Deninger's
claim, now with a reason.

## 6. Status

- **Illustration, not proof** (by design). The script reconfirms the FF single
  scale across the genus-1 family and exhibits the unbounded arithmetic place
  spectrum `{log p}` with its diverging scale spread. The deliverable is the
  sharpened specification, recorded here and folded into 2K section 4.
- **Next.** Direction 4.6: construct the regularized determinant
  `det_zeta(s - Phi_t | H^*_{F,pr})` and verify it reproduces the Euler product,
  i.e. realize the `Gamma_S^2` constraint of section 3 on an actual leafwise
  prismatic cohomology. That is the first place the place-dependent bidegree would
  become an honest (regularized) intersection number. **Partially done ([2R](e2r_dynamical_zeta.md)):**
  the DYNAMICAL side of this is now concrete -- `Gamma_S^2 = -zeta'/zeta` is the
  log-derivative of a Ruelle dynamical zeta with primitive orbit lengths `{log p}`,
  and D-H has no such orbit spectrum. What remains is the COHOMOLOGY the flow acts
  on (the signature, not just the spectrum).

## 7. Connections

- 2G ([e2g](e2g_intersection_signature.md)): the `(1, q)` correspondence and the single-scale Hasse-Weil signature.
- 2J ([2J](2J_arakelov_adjunction.md)): the adjunction `omega-bar^2 = 12 h_Fal`, the per-fibre input to `Gamma_S^2`.
- 2K ([2K](2K_spec_z_squared_dictionary.md)): the dictionary; 2Q sharpens its section 4 (the one missing object).
- 3M ([e3m](../positivity/e3m_place_type_balance.md)): the von Mangoldt delocalization that grounds the sharper K2.
- Direction 4 ([04_prismatic_foliation.md](../../docs/03_research/research_directions/04_prismatic_foliation.md)): milestone 4.6 is where `Gamma_S^2` becomes a regularized intersection number.
- Direction 8 ([08_hodge_index_surface.md](../../docs/03_research/research_directions/08_hodge_index_surface.md)): the index theorem on the surface carrying `Gamma_S`.

## Outputs

- `e2q_frobenius_bidegree.npz`: FF single-scale data (q, t, margin) + arithmetic place spectrum (`p`, `log p`, scale spread).
- `e2q_frobenius_bidegree.png`: the single scale `q` (FF, one point per curve) vs the unbounded `{log p}` place spectrum (Spec(Z)).
