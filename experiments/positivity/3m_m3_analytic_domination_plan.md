# M3: The Analytic Domination (Plan and Strategy)

> **Objective:** Prove the archimedean block $A_{\mathrm{arch}}$ dominates the prime block $P_{\mathrm{fin}} + B_{\mathrm{pole}}$ on the truncated arithmetic Frobenius algebra $\mathcal{A}_P$, engaging the exact off-line structure (Euler product) to break the Davenport-Heilbronn stealth window.

> **Status (2026-06-01).** What was DELIVERED (`e3m_analytic_domination.py`) is the *numerical* half of this plan, not the analytic proof. Splitting $P_{\mathrm{fin}}$ into prime-power $P_{\mathrm{pp}}$ and composite $P_{\mathrm{comp}}$ and deleting $P_{\mathrm{comp}}$ gives a discriminator $M_{\mathrm{euler}} = A_{\mathrm{arch}} + P_{\mathrm{pp}} + B_{\mathrm{pole}}$ that separates all three controls correctly (zeta $+0.035$, D-H $-0.929$, Epstein $+0.676$), passing the D-H discipline where the full $M$ did not. That is genuine progress: it locates the obstruction in the composite delocalization. But the analytic domination bound (Step B below) is NOT proved, and $M_{\mathrm{euler}}$ is not yet an intrinsic invariant: for a non-Euler $L$ the deletion of $P_{\mathrm{comp}}$ is imposed by hand, and equals the Euler-product assumption. The claim that it is geometrically forced is the [Direction 8B/8C](../../docs/03_research/research_directions/08C_cohomological_signature.md) conjecture. M3 is therefore PARTIAL: numerical isolation done, analytic proof open.

## 1. The Bottleneck: The D-H Stealth Window
In M2.6, we showed that the non-circular Rosati trace form $M = A_{\mathrm{arch}} + P_{\mathrm{fin}} + B_{\mathrm{pole}}$ computed via the Bombieri archimedean kernel reads spuriously positive for Davenport-Heilbronn (D-H). The reason is that D-H's off-line obstruction ($\gamma \approx 85.7$) is tiny (~2.6% of the raw spectrum) and sits below the reconstruction-residual floor at reachable truncation scales $b$.

**Conclusion:** Finer numerics will not separate $\zeta$ from D-H. The proof must be analytic. We need an exact structural reason why $A_{\mathrm{arch}}$ dominates for Euler products but fails to dominate for non-Euler products.

## 2. The Polarization: Arakelov Green's Function
Over a function field, the positivity of the Rosati involution comes from the canonical polarization (the Hodge-Riemann bilinear relations). Over $\mathbb{Z}$, the candidate polarization is the Arakelov/archimedean Green's-function pairing:
- $h_{\mathrm{Fal}}$ (the Faltings height from `e2l_faltings_petersson.py`), representing $\overline{\omega}^2 / 12$.
- $\lambda_\infty$ (the genuine Neron local height from `e2i_archimedean_local_height.py`), which carries the arithmetic Hodge index regulator.

We must formulate the trace form $B(x, y) = \mathrm{Tr}(x \, y^\dagger)$ on $\mathcal{A}_P \otimes \mathbb{R}$ using this geometric polarization.

## 3. Formulating the M3 Experiment
We will construct an experiment `e3m_analytic_domination.py` with the following objectives:

### Step A: Assemble the Geometric Polarization
1. Map the basis of $\mathcal{A}_P$ (indexed by $b_i$, corresponding to $\log p_i$) to the geometric Arakelov data.
2. Define the operator $\dagger$ (the arithmetic Rosati adjoint) geometrically.
3. Compute the polarization matrix $A_{\mathrm{geom}}$, where the entries are derived from the Faltings height and the Neron local heights, effectively "globalizing" the transcendental archimedean piece.

### Step B: The Analytic Domination Bound
1. Formulate the analytic bound for $x^T A_{\mathrm{geom}} x$ against the prime obstruction $x^T (P_{\mathrm{fin}} + B_{\mathrm{pole}}) x$.
2. For $\zeta$ (which has an exact Euler product), the prime support is strictly on prime powers. Use the explicit geometry of the Green's function to bound the prime power contributions.
3. For D-H (no Euler product), the prime support delocalizes onto composites. Show analytically (and verify numerically in the script) that the composite contributions break the Green's function bound, causing the polarization to fail to dominate.

### Step C: Numerical Bridge
1. Build $\mathcal{A}_P$ for a small truncation (e.g., $P \le 50$).
2. Compare the algebraic archimedean block $A_{\mathrm{arch}}$ (from the Bombieri integral) with the geometric polarization matrix $A_{\mathrm{geom}}$ to confirm they are structurally equivalent or bounds of each other.
3. Demonstrate that $A_{\mathrm{geom}}$ successfully isolates the off-line obstruction of D-H without requiring extreme $T_{\max}$ limit expansions.

## 4. Next Steps for Implementation
1. Extract the exact Arakelov height pairing matrices computed in `e2i` and `e2l`.
2. Define the mapping between the test functions $\Phi_{b_i}$ (the boxcar basis of $\mathcal{A}_P$) and the points/divisors on the Arakelov surface.
3. Implement `e3m_analytic_domination.py` to numerically test this geometric polarization matrix against $\zeta$ and D-H.