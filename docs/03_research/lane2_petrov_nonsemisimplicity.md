# Lane 2: Petrov non-semisimplicity is not fatal to WCart, but it kills the naive Sen-eigenspace polarization branch

> Lane 2 writeup, 2026-06-05. The structural/theory companion to the computational
> coordinates 2LN (#69), 2LO (#70), and 2P+ (#71). Parent directions:
> [`research_directions/08B_bhatt_lurie_wcart_signature.md`](research_directions/08B_bhatt_lurie_wcart_signature.md)
> and [`08A_rosati_standard_conjecture.md`](research_directions/08A_rosati_standard_conjecture.md);
> proposal thread [`euler_sen_polarization_attempt.md`](euler_sen_polarization_attempt.md).

The M4 target is fixed: the desired object is not another trace or
functional-equation pairing, but a geometric cup-product polarization on the
infinite-dimensional arithmetic $H^1$.

## Claim

Petrov's non-semisimplicity result is **not** fatal to WCart / prismatic
cohomology as the substrate. It is, however, fatal to a specific and tempting
proof branch.

> **Dead branch.** Construct the M4 polarization by passing to the Hodge-Tate
> divisor $\mathrm{WCart}^{\mathrm{HT}}$, decomposing the arithmetic $H^1$ into
> honest Sen eigenspaces, and proving Hodge-Riemann positivity weight-by-weight
> from that diagonal decomposition.

That branch is dead because WCart's Sen operator is not formally semisimple, and
Petrov gives geometric examples where it is genuinely non-semisimple. Therefore
semisimplicity cannot be treated as a free structural property of prismatic
geometry. It would have to be proved as an additional arithmetic theorem for the
specific $\mathrm{Spec}(\mathbb{Z})$ object, or the polarization must be
formulated on a filtered / derived object that explicitly handles the nilpotent
part.

## The substrate (what WCart does supply)

Bhatt-Lurie identify perfect complexes on $\mathrm{WCart}$ with perfect prismatic
crystals, and the prismatic cohomology sheaf of a smooth proper $p$-adic formal
scheme is one such perfect complex on $\mathrm{WCart}$
([arXiv:2201.06120](https://arxiv.org/abs/2201.06120)). The Hodge-Tate divisor
$\mathrm{WCart}^{\mathrm{HT}}$ is controlled by pairs $(M, \Theta)$, where
$\Theta$ is the Sen operator satisfying an integrality / local-nilpotence
condition, **not** a semisimplicity condition. Bhatt-Lurie also construct a
Frobenius endomorphism $F$, so the full WCart substrate contains arithmetic
Frobenius structure that is absent from a bare functional-equation object. This
is the same two-operator picture recorded in 2PR.1 (#44): $F$ supplies the finite
Euler factors and $\Theta$ supplies the archimedean Hodge-Tate weights $\{-n\}$.

Petrov then shows the non-semisimplicity is not merely a formal possibility
([arXiv:2302.11389](https://arxiv.org/abs/2302.11389), Annals of Mathematics).
For a smooth lift $X_1$, the Sen operator acts by $-n$ on the $n$-th Hodge
cohomology sheaf, but the generalized eigenspaces can carry a genuine nilpotent
operator $N$. The obstruction is explicitly tied to Frobenius-lifting data: the
de Rham complex is formal as an $E_\infty$-algebra if and only if the variety
lifts to $W_2(k)$ **together with its Frobenius endomorphism**, and the
obstruction class has the schematic shape

$$ c_{X_1, p} \;=\; \mathrm{ob}_{F, X_1} \cdot \alpha(\Omega^1_{X_0/k}), $$

the Frobenius-lift obstruction $\mathrm{ob}_{F}$ cupped with an Atiyah-type class
on $\Omega^1$. The non-semisimplicity lives on the Frobenius-lift side, not on
the archimedean / Hodge side.

## The linear-algebra obstruction

Let $E$ be the putative arithmetic $H^1$ object after restriction to
$\mathrm{WCart}^{\mathrm{HT}}$, and suppose a candidate cup product gives a
pairing into a Tate twist,

$$ Q : E \otimes E \longrightarrow \mathcal{O}\{w\}, $$

compatible with the Sen operator (the derivation / Griffiths-transversality
relation, the same equation solved finitely in 2KK/2LL/2LN):

$$ Q(\Theta x, y) + Q(x, \Theta y) \;=\; w\, Q(x, y). $$

Restrict to a generalized Sen-weight piece and write $\Theta = \lambda I + N$ with
$N$ nilpotent. On the paired generalized-weight pieces the scalar part saturates
the weight $w$, leaving

$$ Q(N x, y) + Q(x, N y) \;=\; 0. $$

So the nilpotent part $N$ is **$Q$-skew-adjoint** on the paired generalized-weight
pieces. (This is exactly the finite relation $N^{\mathsf T}\Omega + \Omega N = 0$
that 2LN solved with residual $0$.)

Now suppose the proposed Hodge-Riemann form is obtained from the Sen-weight
decomposition by a Weil-operator-type correction that uses **only** the
semisimple part,

$$ h(x, y) \;=\; Q\!\left(C(\Theta_{\mathrm{ss}})\, x, \ \overline{y}\right). $$

Positivity of $h$ on the eigenspaces forces the nilpotent to vanish:

$$ \boxed{\ \text{positive eigenspace HR form from }\Theta_{\mathrm{ss}}\ \Longrightarrow\ N = 0.\ } $$

Any nonzero Petrov-type nilpotent block is incompatible with a polarization
obtained purely by diagonalizing $\Theta$ and applying signs / Weil phases on
eigenspaces.

## What is killed

The dead strategy, step by step:

1. Restrict the arithmetic prismatic $H^1$ to $\mathrm{WCart}^{\mathrm{HT}}$.
2. Treat $\Theta$ as giving a genuine Hodge-Tate eigenspace decomposition.
3. Define the primitive pairing on those eigenspaces.
4. Read positivity from the eigenspace signs.

This is not a theorem of WCart. Petrov's examples show the Sen operator can have
genuine nilpotent Jordan components in geometric prismatic situations, so an
"eigenspace polarization" is not a free geometric construction. It smuggles in a
semisimplicity hypothesis.

This does **not** prove the specific arithmetic $H^1$ over $\mathrm{Spec}(\mathbb{Z})$
has nonzero nilpotent Sen part. It proves something narrower and useful: the proof
cannot rely on formal WCart geometry to supply a semisimple Hodge-Tate
decomposition. Either one proves $N = 0$ for the arithmetic object from exact
arithmetic (Euler/Frobenius) structure, or one builds a polarization that is
intrinsically filtered / derived and $N$-aware.

## What remains routable

The WCart substrate stays viable if the M4 polarization is constructed **before**
passing to a diagonal Sen decomposition. The surviving shape is a derived cup into
the Euler-pole fundamental class,

$$ Q : \mathcal{H}^1_{\Delta} \otimes^{\mathbf{L}} \mathcal{H}^1_{\Delta} \longrightarrow \mathcal{H}^2_{\Delta,\,\mathrm{Euler}}, $$

with $\Theta = \Theta_{\mathrm{ss}} + N$ handled as monodromy, not diagonalized
away. A routable signature theorem is then a **mixed primitive** statement on the
monodromy weight filtration $W(N)$: the forms

$$ Q_r(x, y) \;=\; Q(x, N^r y) $$

are the candidate polarizations on the primitive pieces
$P_r = \ker(N^{r+1} : \mathrm{Gr}^W_r \to \mathrm{Gr}^W_{-r-2})$. This is the
classical Hodge-Riemann cure for a non-semisimple degeneration: the nilpotent
operator supplies the missing primitive direction, rather than being an
obstruction to be diagonalized.

## Relation to the computational coordinates

This writeup is the geometric statement of the finding that 2LN (#69) exhibited as
finite linear algebra, and it is consistent with 2LO (#70) and 2P+ (#71):

- **2LN** confirmed both halves of this argument computationally. The naive
  diagonal Sen-eigenspace metric (the direct Hermitian Rosati/Lyapunov form
  $\Theta^* H + H\Theta = -H$, $H > 0$) does **not** exist on a genuine defective
  block, which is the $N = 0$ obstruction above. But by Jacobson-Morozov the
  monodromy weight filtration makes $N$ a pure Lefschetz lowering operator (the
  zero endomorphism on each primitive graded quotient), so the $N$-aware forms
  $Q_r$ survive. The Petrov nilpotent is routable, not fatal.
- **2LO** showed the surviving polarization, once its sign datum $B_E$ is
  supplied, recovers the function-field Rosati sign exactly via the polar Weil
  operator $C_E = A_E(-A_E^2)^{-1/2}$, but cannot construct $B_E$ from the $(1,p)$
  bidegrees plus archimedean data: the missing piece is the global Frobenius trace
  $t$.
- **2P+** confirmed that no recent construction (Tang, Gurney, Connes-Consani)
  supplies that global signed $t$-carrying pairing; they stop at perfectness, the
  substrate, and the trace respectively.

So Lane 2 prunes the branch (no eigenspace polarization), 2LN/2LO build the
$N$-aware local formalism, and 2P+ shows the residual datum (the global trace) is
the same open product-surface theorem.

## Davenport-Heilbronn discipline

This obstruction is **D-H-aware by type, not by sign**.

Davenport-Heilbronn has a functional equation but no Euler product, and a valid M4
object must not fire on D-H merely from the shared functional-equation /
archimedean data. The Petrov/WCart obstruction lives in a category of prismatic
crystals, Frobenius lifts, Cartier-Witt geometry, and Frobenius-lifting
obstruction classes. Petrov's class $c_{X_1, p}$ is not defined for D-H, because
D-H supplies no underlying Frobenius / Euler-product geometry to lift or obstruct.

So this result does not separate zeta from D-H by a numerical sign. It says that
any attempted positivity proof using only the Hodge-Tate / Sen fiber is
structurally too soft: if it can be abstracted to a functional-equation object, it
has lost the Frobenius / Euler half and is back in the D-H trap.

## Kill criteria

| Criterion | Status |
|---|---|
| K1 non-circularity | Passes as an obstruction: no zero locations are used. |
| K2 D-H awareness | Passes by type: the relevant WCart / Frobenius objects are not defined for D-H. |
| Produces a polarization | No. This is a branch-pruning result, not a signature theorem. |
| Separates zeta from D-H at reachable truncation | No. It is not a numerical discriminator. |
| Avoids trace / statistic restatement | Yes. It kills a structural branch, not a Level-3 statistic. |
| M4 relevance | Direct: it constrains how the $H^1$ cup-product polarization may be built. |

## Milestone placement

This lands inside M4 as **branch pruning**. It rules out the coordinate "WCart
polarization via semisimple Sen eigenspace decomposition." The proof must instead
live in one of two places:

$$ \boxed{\ \text{either prove } N = 0 \text{ for the arithmetic } \mathrm{Spec}(\mathbb{Z}) \text{ object by Euler/Frobenius geometry,}\ } $$

or

$$ \boxed{\ \text{construct an } N\text{-aware filtered/derived Hodge-Riemann polarization.}\ } $$

Nothing here upgrades trace to signature. The concrete advance is negative and
directional: Petrov non-semisimplicity makes the naive eigenspace-polarization
route unavailable, so the M4 proof must use the full WCart / Frobenius geometry
rather than the Hodge-Tate / Sen fiber alone. That is a coordinate, not a wall:
it tells the construction exactly which fiber is too soft and which structure
(the monodromy-aware cup into the Euler-pole $H^2$) it must carry.

## References

- A. Petrov, *Non-decomposability of the de Rham complex and non-semisimplicity
  of the Sen operator* ([arXiv:2302.11389](https://arxiv.org/abs/2302.11389),
  Annals of Mathematics). The de Rham complex is formal as an $E_\infty$-algebra
  iff the variety lifts to $W_2(k)$ together with its Frobenius; examples of
  non-semisimple Sen operators.
- B. Bhatt, J. Lurie, *Absolute prismatic cohomology*
  ([arXiv:2201.06120](https://arxiv.org/abs/2201.06120)). The Cartier-Witt stack
  $\mathrm{WCart}$, perfect prismatic crystals, the Sen operator on
  $\mathrm{WCart}^{\mathrm{HT}}$, and the Frobenius endomorphism $F$.
- Project coordinates: 2LN (#69), 2LO (#70), 2P+ (#71) in
  [`../../experiments/LEARNINGS.md`](../../experiments/LEARNINGS.md); the Euler-Sen
  proposal in [`euler_sen_polarization_attempt.md`](euler_sen_polarization_attempt.md);
  the consolidating [`spec_z_cohomology_landscape.md`](spec_z_cohomology_landscape.md).
