# Direction 8B: Geometricizing the M3 Bound via Bhatt-Lurie's `WCart`

> **Parent doc**: [`08_hodge_index_surface.md`](08_hodge_index_surface.md) and [`08A_rosati_standard_conjecture.md`](08A_rosati_standard_conjecture.md).
> Written 2026-06-01 after the M3 Analytic Domination breakthrough.

## 1. The Analytic Target ($M_{\mathrm{euler}}$ Positivity)

The M3 experiment (`e3m_analytic_domination.py`) sharpened the trace-side goal of the proof program. It found a numerical discriminator: across the three controls (zeta, D-H, Epstein), the false positivity of Davenport-Heilbronn (the stealth window) tracks the composite prime support ($P_{\mathrm{comp}}$), which compensates a failure in the prime-power block.

> **Status caveat (read before building on this).** $M_{\mathrm{euler}}$ is formed by *deleting* the composite block $P_{\mathrm{comp}}$ from the Weil-form Gram matrix $M$. For an Euler product that deletion is automatic ($P_{\mathrm{comp}} = 0$); for a non-Euler $L$ (D-H, Epstein) it is imposed by hand, and is logically the same as assuming an Euler-product geometry. So the statement below is a **conjecture**, the target of this direction, not an established equivalence. The M3 experiment shows $M_{\mathrm{euler}}$ is a working discriminator (it passes the D-H discipline); it does NOT prove $M_{\mathrm{euler}} \ge 0 \Leftrightarrow$ RH, and it does not prove that $M_{\mathrm{euler}}$ is the canonical geometric trace.

The conjectured non-circular positivity statement (to be proved, not assumed) is:
$$ M_{\mathrm{euler}} = A_{\mathrm{arch}} + P_{\mathrm{pp}} + B_{\mathrm{pole}} \ge 0 \quad \overset{?}{\Longleftrightarrow} \quad \mathrm{RH} $$
where $A_{\mathrm{arch}}$ is the geometric archimedean polarization (the Green's function / Petersson norm), $P_{\mathrm{pp}}$ is the strictly prime-power supported von Mangoldt trace, and $B_{\mathrm{pole}}$ is the rank-1 hyperbolic direction. 

Direction 8 requires us to construct an intersection pairing $\langle -, - \rangle$ on the cohomological substrate of the product surface $\mathrm{Spec}(\mathbb{Z}) \times \mathrm{Spec}(\mathbb{Z})$ whose signature exactly reproduces $M_{\mathrm{euler}}$.

## 2. The Prismatic Substrate (`WCart`)

Bhatt and Lurie's **Cartier-Witt stack** ($\mathrm{WCart}$) provides the exact algebraic skeleton required for the finite-places side of this surface.
- **The absolute base point:** $\mathrm{WCart}$ geometrizes the category of *all* bounded prisms. It acts as "de Rham cohomology relative to $\mathbb{F}_1$".
- **The dimension count:** It has cohomological dimension 1, but its Nygaard/conjugate filtration is infinite-dimensional, mirroring the arithmetic surface requirement (dimension 1 + infinite flow dimension).

## 3. The Sen Operator $\Theta$ as the Flow

To realize $P_{\mathrm{pp}}$ as an intersection number, we need the Frobenius correspondence $\Gamma_S$. 
- Bhatt-Lurie construct a global Frobenius endomorphism $F$ on $\mathrm{WCart}$ that **contracts** the Hodge-Tate divisor $\mathrm{WCart}^{\mathrm{HT}}$ to the de Rham point.
- On $\mathrm{WCart}^{\mathrm{HT}}$, there is a **Sen operator $\Theta$**.
- $\Theta$ is the infinitesimal generator of the cyclotomic flow: $\gamma_u = \exp(\log(u) \Theta)$. 
- $\Theta$ acts on the $n$-th conjugate-graded piece of the diffracted Hodge complex by multiplication by $-n$.

This $\Theta$ is the literal Deninger $R$-flow generator realized in $p$-adic/prismatic geometry. 

## 4. Defining the Cup Product (The Missing Signature)

The final gap is the intersection signature. We must define a cup product $\smile$ on the absolute prismatic cohomology $H_{\mathrm{prism}}(X)$ such that the Hodge-Riemann bilinear relations hold.

**The Mapping:**
1. The test functions $\Phi_b$ from M3 map to states in the Nygaard filtration of the diffracted Hodge complex.
2. The archimedean block $A_{\mathrm{arch}}$ corresponds to the pairing at the de Rham point (the "trivial" fixed point of the $F$-contraction).
3. The prime-power block $P_{\mathrm{pp}}$ is the action of $F$ on the transversal (the Hodge-Tate divisor), governed entirely by the spectrum of $\Theta$.
4. The composite obstruction $P_{\mathrm{comp}} = 0$ would be forced geometrically IF the absolute prismatic complex is built prime-by-prime (the $p$-adic completion stricture), so that cross-prime composite terms vanish in the canonical filtration. This vanishing is the load-bearing CONJECTURE of this direction: it is what would make the hand-deletion of $P_{\mathrm{comp}}$ in M3 a geometric fact rather than an assumption. It is not proved here.

The theoretical task is therefore twofold and OPEN: (a) prove that the canonical prismatic filtration kills the composite cross-terms ($P_{\mathrm{comp}} = 0$ geometrically), and (b) prove that the Sen operator $\Theta$, acting as the connecting map between the Nygaard graded pieces, forces the alternating sum of traces (the Lefschetz trace) to be positive-definite on the primitive cohomology, recovering $M_{\mathrm{euler}} \ge 0$.