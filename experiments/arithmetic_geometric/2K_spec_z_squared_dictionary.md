# 2K: reverse-engineering the Spec(Z) x Spec(Z) intersection form

> Direction 8 centerpiece. Unifies the three session-004 threads -- 3M (the Weil
> quadratic form, trace side), 2G (the C x C intersection form, signature side),
> 2I (the archimedean Neron local height) -- into one dictionary, and reads off
> what the missing arithmetic surface `S = Spec(Z) x Spec(Z)` would have to be, and
> what is and is not supplied by the data we can already compute.

## 1. The function-field anchor (2G), recalled

On `S_FF = C x C` the Weil/Lefschetz machinery gives, for the divisor classes
`e, f` (fibres), `Delta` (diagonal), `Gamma` (Frobenius graph):

```
intersection numbers           Lefschetz / zeta meaning
e.f = 1, e^2=f^2=0             the hyperbolic "fibre" plane (signature (1,1))
Gamma.Delta = N_1              point count = sum over Frobenius eigenvalues (zeros)
Gamma.e=1, Gamma.f=q           Frobenius is a (1,q) correspondence
Delta^2 = 2-2g, Gamma^2=q(2-2g)
```

RH <=> the primitive form (orthogonal complement of `{e,f}`) is negative definite
<=> Hodge index signature `(1, rho-1)` <=> `|t| < 2g sqrt(q)`. The point counts
`N_n` (intersection numbers `Gamma_n.Delta`) ARE the data of the zeta function via
the Lefschetz trace formula `sum_i alpha_i^n = q^n + 1 - N_n`.

## 2. The arithmetic side: what the explicit formula already gives us

For zeta, Weil's explicit formula (the object 3M decomposed) is the EXACT analogue
of the Lefschetz trace formula. Schematically, for a test function:

```
sum_rho  f-hat(rho)   =   A_arch(f)        +   P_fin(f)            +   B_pole(f)
   (zeros)                 (Gamma factor)      (sum_p log p ...)       (pole at s=1)
```

The dictionary to the function-field intersection numbers is forced:

| function-field (C x C) | arithmetic (S = "Spec(Z) x Spec(Z)") | supplied by |
|---|---|---|
| Lefschetz `sum alpha^n = q^n+1-N_n` | explicit formula `sum_rho f-hat(rho) = ...` | **yes** (classical) |
| `Gamma_n . Delta = N_n` (point counts) | the **prime side** `P_fin`: `sum_p (log p) ...` (von Mangoldt) | **yes** (3M, input-side) |
| fibre plane `{e,f}`, the `(1,1)` hyperbolic block | the **pole block** `B_pole` (pole of zeta at s=1), rank-1 positive | **yes** (3M) |
| intersection at the archimedean fibre | the **archimedean block** `A_arch` (Gamma factor); concretely the Neron local height `lambda_inf` | **yes** (2I, validated) |
| Hodge index: primitive form negative definite | Weil positivity: `M = A_arch + P_fin + B_pole >= 0` | **<=> RH** |

So the explicit-formula place-decomposition `M = A_arch + P_fin + B_pole` (3M) is
the **exact arithmetic analogue** of the C x C divisor decomposition
`{Delta, Gamma}` against the hyperbolic `{e, f}` (2G). The pole block plays the
role of the fibre plane (the "+1" hyperbolic direction); the prime block plays the
role of the Frobenius correspondence (`Gamma.Delta = N`); the archimedean block
(2I's `lambda_inf`) plays the role of the intersection at the place at infinity.

## 3. The reframing of RH this produces

Reading the dictionary right-to-left, RH becomes EXACTLY a Hodge-index signature
statement on the arithmetic Weil-form Gram matrix:

> **RH (zeta) <=> the intersection Gram matrix `M = A_arch + P_fin + B_pole` is
> positive semidefinite on the test-function basis, with the pole block supplying
> the single positive (hyperbolic) direction and the archimedean + prime blocks
> supplying a negative-(semi)definite primitive part.**

This is the same shape as 2G's theorem (`(1, rho-1)` signature), now over Spec(Z).
The session's two-clock findings pin the quantitative content:

- 3M (#20): the prime block delocalizes off prime powers exactly when there is no
  Euler product (zeta: prime-power-supported; D-H: composite-supported). So the
  arithmetic "Frobenius correspondence" `Gamma_S` exists (prime-power-supported
  `Gamma_S . Delta_S`) precisely for Euler-product L-functions -- the K2 face: D-H
  has no `Gamma_S`, hence no surface, hence the Weil template cannot be set up.
- 2I (#23): the archimedean block is NOT positive-definite by itself (rank-3
  example), so positivity is GLOBAL -- the archimedean "fibre at infinity" and the
  finite places must combine. This says the would-be Hodge index on `S` is not a
  product of a finite and an archimedean index; it is a single global signature, as
  on a genuine surface.

## 4. What is supplied, and the one thing that is not

Everything on the RIGHT side of the trace formula is computable today: the
intersection NUMBERS (`P_fin` from von Mangoldt, `B_pole` from the pole, `A_arch`
from the Gamma factor / `lambda_inf`) are all in hand and validated (3M, 2I). What
is missing is the **scheme that realizes them as actual intersection numbers**: a
2-dimensional arithmetic object `S` with

- a genuine intersection pairing whose values are these numbers,
- a self-map `Gamma_S` (arithmetic Frobenius / Deninger flow) with
  `Gamma_S . Delta_S = ` the prime side,
- a `Delta_S^2` (arithmetic adjunction; the analogue of `2-2g`),
- and a compactification carrying the archimedean fibre (where 2I's `lambda_inf`
  lives).

The gap is therefore NOT "find the intersection numbers" (the explicit formula and
2I give them) and NOT "prove an index theorem in the abstract" (Faltings-Hriljac
shows the arithmetic Hodge index is a theorem for a single arithmetic surface, 2H).
The gap is the **product surface `Spec(Z) x Spec(Z)` and its Frobenius
correspondence** -- the object on which "these numbers are intersection numbers"
and on which a global signature theorem could be proved. This is exactly the
F_1 / Lambda-blueprint / prismatic program (Directions 1-4), now with a sharp,
computed target: produce `S` whose intersection form is the Weil-form Gram matrix
`A_arch + P_fin + B_pole`, with the pole block as the hyperbolic direction.

## 5. Why this is progress, not just reformulation

A bare "RH <=> Weil form positive" reformulation would be failure mode #5
(reformulation without new tools). This is more, in three concrete ways:

1. It identifies WHICH block is the hyperbolic `(+1)` direction (the pole at s=1),
   matching the fibre class on C x C -- a structural correspondence, not a slogan.
2. It pins, via 3M (#20), that the arithmetic Frobenius correspondence is exactly
   what the Euler product supplies, giving the K2 wrong-approach discipline a
   geometric statement (no Euler product => no `Gamma_S` => no surface).
3. It locates the archimedean place precisely (2I): it is one of the intersection
   contributions, not positive-definite alone, so the surface must be GLOBAL
   (compactified, with the archimedean fibre genuinely intersecting), ruling out
   any "finite-places-only" or "archimedean-only" shortcut.

Together these convert "build the surface" from a vague aspiration into a
specification: the target intersection form, its hyperbolic direction, the
correspondence's defining property, and the archimedean fibre's role are all now
fixed by computed data. That specification is the deliverable Direction 8 milestones
5.1 and 5.6 (state the index precisely; verify the K1 signature-not-trace escape).

## 6b. State of the art on actually building S (2026 literature)

A literature pass (overnight task T4) on where the construction of an arithmetic
surface below `Spec(Z)` actually stands, to keep section 4's "the gap is the product
surface" statement honest:

- **F_1 / blueprint framework (Lorscheid, Connes-Consani).** The organizing idea is
  unchanged: `Spec(Z)` should be a "curve over `F_1`" with a completion
  `\overline{Spec Z}` analogous to a curve over a finite field, and intersection
  theory on `\overline{Spec Z} x \overline{Spec Z}` is the explicit hope for
  mimicking Weil's proof ([Lorscheid, "Blueprints -- towards absolute arithmetic?",
  arXiv:1204.3129]). This is exactly the surface 2K specifies. Status: framework,
  no surface with the needed intersection form.
- **The Arithmetic Site (Connes-Consani, 2014-).** The adele class space quotient
  yields the complete Riemann zeta as a Hasse-Weil zeta ([arXiv:1502.05580]); this
  is the "right arena" (the 3M / R3.5 NCG side), still missing the positivity, as
  the project's R3.x analyses recorded.
- **NEW (Oct 2024): Deninger <-> Connes-Consani bridge** ([arXiv:2508.15971]). A
  correspondence is established between Deninger's foliated dynamical systems
  attached to abelian number fields and Connes-Consani's adelic spaces:
  Galois-equivariant, flow-anti-equivariant, with closed orbits <-> primes matching
  on both sides. This is the most relevant recent progress: it links the two
  leading candidate frameworks for the "arithmetic Frobenius flow" (Deninger's
  `R`-action, new_mathematics.md sec 4.1) on the very spaces that would carry the
  surface. It does NOT yet build the product surface or its intersection form, but
  it unifies the two programs that each supply half of the 2K dictionary (Deninger:
  the flow `Gamma_S`; Connes-Consani: the arithmetic site / archimedean place).

**Net for 2K:** the dictionary's two structural halves -- the Frobenius
correspondence (Deninger flow) and the arithmetic-site geometry (Connes-Consani) --
were bridged in 2024, but the object that would make `A_arch + P_fin + B_pole` an
honest intersection form on a 2-dimensional `S` (with `B_pole` the hyperbolic
direction) is still unbuilt. The 2026 frontier is therefore: put a genuine
intersection pairing on the Deninger-Connes-Consani space, with the signature 2K
specifies. That is a sharper, literature-current statement of Direction 8's gap.

## 6. Connections

- 3M ([e3m](../positivity/e3m_place_type_balance.md)): the place decomposition `M = A+P+B` (the arithmetic Weil form).
- 2G ([e2g](e2g_intersection_signature.md)): the C x C template (the hyperbolic-fibre + negative-primitive signature).
- 2H ([e2h](e2h_arithmetic_hodge_index.md)): Faltings-Hriljac (the index is a theorem for one arithmetic surface).
- 2I ([e2i](e2i_archimedean_local_height.md)): the archimedean intersection contribution (lambda_inf), and positivity-is-global.
- Direction 8 ([08_hodge_index_surface.md](../../docs/03_research/research_directions/08_hodge_index_surface.md)): the surface to build.
- R3.5 (K1): positivity from a SIGNATURE (this dictionary) escapes the trace-identity circularity; the pole-as-hyperbolic-direction is the signature anchor.
