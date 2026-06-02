# 2CC — The tropical shadow of the Hodge index on the Connes-Consani square loses the trace t

> Direction 8 (the product surface), first numerical probe of the Connes-Consani square.
> Code: [`e2cc_tropical_shadow.py`](e2cc_tropical_shadow.py). Companions: [2Q](e2q_frobenius_bidegree.md)
> (the (1,p) bidegree), [2G](e2g_intersection_signature.md) (the function-field Hodge index),
> reading note [Connes-Consani-2015](../../docs/03_research/reading_notes/Connes-Consani-2015-Geometry-Arithmetic-Site.md).
> **Adversary-checked (PASS with softening); claims below are the softened, honest versions.**

## The setup

Connes-Consani (arXiv:1502.05580) build the arithmetic-site **square** as the topos `N^×²`
with structure sheaf `Conv_≥(ℤ×ℤ)` = convex Newton polygons under (convex-hull-union,
Minkowski-sum), carrying Frobenius correspondences `Ψ(λ)` of real slope λ, with
`Fr_{n,m} = diag(n,m)` on the quadrant. This **is** the `Spec(ℤ)×Spec(ℤ)` product surface
Direction 8 chases. The reading note isolates the gap precisely: the characteristic-1
operations are **idempotent** (no subtraction), so there is **no signed intersection
number**, hence **no Hodge-index signature**. That missing signed pairing is the whole gap.

## The idea, and what is and isn't rigorous

The Minkowski-sum structure carries a canonical bilinear form, the **mixed area**
`V(A,B) = (Area(A+B) − Area(A) − Area(B))/2` (the 2D mixed volume). By the
**Alexandrov-Fenchel / Teissier-Khovanskii mixed Hodge index theorem**, the Gram of mixed
volumes of convex bodies is **Lorentzian** (≤ 1 positive eigenvalue) — a Hodge-index
signature `(1,k)`.

**Honest framing (the load-bearing caveat).** Mixed-volume = intersection-number is a
**toric** theorem (BKK / Khovanskii-Teissier) about the toric variety of a fan, where
Newton polytopes are divisor classes. The C-C square is a **characteristic-1 topos**, not a
toric variety; its polygons are structure-sheaf sections, not divisors. So the mixed-area
form is **not a constructed intersection theory of the C-C topos** — it is a **proposed
shadow** of the missing pairing, by analogy with toric BKK. What is rigorous: (i) the form
is canonical on the Minkowski structure; (ii) it is Lorentzian by AF; (iii) it is
arithmetic-blind. The decisive question: can *any* such form carry the Frobenius **trace t**
that carries RH on the function-field template (`|t| < 2g√q ⟺ RH-for-C`)?

## Results

| Part | What | Result |
|---|---|---|
| **A** | mixed-area Gram of 6 lattice polygons | signature **(1, 1, 4)** — exactly one positive eigenvalue; 0 Minkowski violations; ADVERSARY confirmed ≤1 positive across **2000 random collections**. The Lorentzian signature is real and robust. |
| **B** | divisor shadow {e=(1,0), f=(0,1), Δ=(1,1), Γ=Fr_{1,p}(Δ)=(1,p)} via edge-segment mixed areas | `{Γ·e, Γ·f} = {p, 1}`, `Δ·Γ = p−1`. The shadow Gram **equals the function-field Gram `ff_gram(p, t=2, g=1)` with e↔f swapped** (verified). |
| **C** | genuine function-field Gram (2G), `Δ·Γ = q+1−t` | signature **(1,3) ⟺ |t| < 2g√q** for every t tested = Hasse-Weil = RH-for-C. The Hodge index **requires t**. |
| **D** | K2 (Davenport-Heilbronn) | no Euler product ⇒ no (1,p) bidegree (2Q/#25) ⇒ no Γ_p polygon ⇒ **no shadow** at all. Clean. |

## The finding (sharpened, honest)

**A canonical Lorentzian convex-geometry form exists for free on the C-C square** (the
mixed-volume / AF mixed Hodge index). **But it takes no arithmetic input, so it is
RH-agnostic — vacuously.** Concretely:

- The shadow is **t-blind**: the mixed-area form has *no free real parameter t*. Whatever
  representatives you choose (edge segments give the value at t=2; full 2D polygons give
  other constants), you get a single number, never the continuum `q+1−t`. The "t=2" is the
  edge-segment representative's value, **not** a structural constant — only the *blindness*
  is robust (ADVERSARY caveat).
- It does **not** independently recover the (1,p) bidegree: it produces `{p,1}` (e↔f
  swapped) and the signature agreement is that relabeling — it *is* the FF Gram at the
  single frozen point t=2, genus 1 only.
- The shadow's `(1,3)` signature is therefore **unconditional**: it would read `(1,3)` for a
  curve with t=2 *and* for one with t=100 (RH violated). **Passing the shadow's Hodge index
  does not imply RH.**

This is the **same RH-agnostic-soft-positivity pattern** as this session's other two
findings — E_DBN1 (#38, the dBN kernel positivity) and #39 (the Rodgers-Tao functional) —
now on the product surface. The 2CC form is the *trivial extreme*: #38/#39 take ζ as input
and are still RH-agnostic; 2CC takes **no arithmetic input** and is RH-agnostic for free.

**It reconciles with the reading note's "the signed pairing does not exist":** the
RH-agnostic *convex-geometry* shadow exists for free; the **arithmetic** signed pairing
carrying the trace t does **not**. So the Direction-8 gap is **sharpened, not closed**: the
RH content is the Frobenius trace t, lost in the idempotent/tropical structure, and the
missing object is the **arithmetic q-lift that restores t** — the "suitable Weil cohomology"
Connes-Consani name as open (end of their §4). The **(1,p) bidegree (2Q) is the locus where
that lift must inject t.**

## Why this is a coordinate (not a wall, not a breakthrough)

It is the **first numerical probe of the Connes-Consani square** (the reading note's
actionable #1), and it does three things:

1. **Realizes attack angle 4.A (tropical/AHK Hodge) on the specific Direction-8 surface** and
   shows *exactly* why it is insufficient. The 08-doc listed 4.A's obstacle as "tropical
   varieties live in ℝⁿ, not over Spec(ℤ)." The C-C square *resolves* that (the arithmetic
   objects live as polygons in ℝ²) — but the mixed-volume Hodge index that results is
   arithmetic-blind. So 4.A's real obstruction is not "no tropical model" but "the tropical
   model's signature is RH-agnostic; the trace t needs the q-lift."
2. **Locates the gap precisely on the (1,p) bidegree**: the shadow gets the bidegree (degree
   data) but not the point-count refinement `q+1−t` (the trace). The arithmetic must enter
   exactly there.
3. **Triangulates the marginal-positivity thesis a third way this session**: soft/free
   positivities (heat kernel #38, zero-dynamics #39, product-surface tropical shadow #40)
   are RH-agnostic; RH lives in the exact arithmetic (Euler product / trace t / Frobenius),
   which every soft structure loses.

## Honest scope / caveats (ADVERSARY-flagged)

- The mixed-area form is a **proposed** shadow (toric-BKK analogy), not a constructed
  intersection theory of the C-C topos. The "free" Lorentzian signature is pure convex
  geometry, RH-agnostic; this is **not progress toward RH**, only a sharpening of where the
  arithmetic must enter.
- The Part-B shadow matches the FF Gram only at **genus 1, the single point t=2, e↔f
  swapped** (`Δ·Δ = 0` for segments coincides with `2−2g` only at g=1). So K3 (Weil
  specialization) holds only as a frozen specialization, consistent with the thesis.
- The AF global `(1,k)` is the Teissier-Khovanskii theorem (confirmed numerically), not the
  pairwise Minkowski inequality (which is necessary-not-sufficient).

## Next (the sharpened target)

The arithmetic q-lift: find a deformation of the mixed-volume form on the C-C square (or a
Weil cohomology of it) whose `Δ·Γ` is the **point count `q+1−t`** rather than the
combinatorial `p−1`, restoring the trace. Candidate routes: (a) the q-deformation of the
characteristic-1 operations (un-idempotent-ize: a `q→1` family whose `q≠1` members carry
subtraction and the trace); (b) the `Ψ(λ)∘Ψ(λ⁻¹) = Id_eps` tangential-deformation
self-intersection (Connes-Consani Thm 7.7) as the carrier of the von Mangoldt / `−ζ'/ζ`
data (2R), checked against the prime-orbit spectrum. Both are research-grade; this
experiment pins them as the **only** places the trace can re-enter.

## Pointers
- LEARNINGS #40 (this finding); #38 (dBN kernel), #39 (Rodgers-Tao), #18-20/#25-26 (bidegree, marginal positivity).
- Direction 8: [`../../docs/03_research/research_directions/08_hodge_index_surface.md`](../../docs/03_research/research_directions/08_hodge_index_surface.md) (attack angle 4.A).
- Connes-Consani square: reading note as above; 2Q (bidegree), 2R (Γ_S²), 2G (FF Hodge index).
- References: Connes-Consani, *Geometry of the arithmetic site*, arXiv:1502.05580 (2015); Khovanskii-Teissier mixed Hodge index; Alexandrov-Fenchel; Adiprasito-Huh-Katz, *Hodge theory for combinatorial geometries*, Ann. Math. 188 (2018).
