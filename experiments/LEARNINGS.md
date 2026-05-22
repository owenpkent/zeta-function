# Learnings from the proof-architecture experimental thread

> Companion to [PROOF_ARCHITECTURES_PLAN.md](PROOF_ARCHITECTURES_PLAN.md) (test plan and status table) and the per-architecture READMEs. This document synthesizes what the experiments collectively **teach** about the four candidate proof architectures and the RH landscape, organized by finding rather than by architecture. Updated as new experiments complete.

The companion documents answer "what did each experiment do?". This one answers "what do they collectively tell us?". When a new experiment lands, look here for the cross-cutting interpretation.

---

## Cross-cutting findings

### 10. The wrong-approach detector's signal saturates: relative min eigenvalue converges and negative count equals off-line zero pairs.

3D.3 extended the Gram-matrix K-scaling from K=100 (3D, 3D.2) up to K=1000, with three structural findings:

- **Relative min eigenvalue ($\lambda_{\min}/\lambda_{\max}$) converges to $-2.62\%$** for D-H across $K \in [300, 1000]$. The signal strength is dimension-independent: it's a fixed property of the off-line zero structure.
- **Number of negative eigenvalues is FIXED at $4$** = number of off-line zero PAIRS in the upper half plane (D-H at $T_{\max} = 200$ has $8$ off-line zeros, forming $4$ functional-equation pairs). Each off-line conjugate pair $(\rho_{\rm off}, \bar\rho_{\rm off})$ introduces exactly $1$ negative eigenvalue. This is a structural finding: the detector's "signal dimension" exactly counts off-line zero pairs.
- **Selberg-class L-functions stay PSD to floating-point noise** even at $K = 1000$. For $\zeta$, $\chi_3$, $\chi_4$: worst rel min $\sim 10^{-16}$, indistinguishable from numerical zero, despite the matrix having $K - n_{\rm zeros} \sim 900$ near-zero eigenvalues (genuine rank deficiency from Gram-of-real-vectors structure for on-line zeros).

This closes LEARNINGS open question #5. The detector is robust at large K, and the architectural interpretation (one negative eigenvalue per off-line zero pair) gives a clean structural picture: **the Gram-matrix detector is effectively counting off-line zero pairs via its negative-eigenvalue spectrum**.

**K-doubling deepening rate.** The absolute min eig grows from $-0.37$ at $K = 100$ to $-4.04$ at $K = 1000$: factor $10.9 \approx K^{1/2}$ in absolute terms. Per K-doubling step: $\{2.06, 1.57, 1.68, 1.50, 1.33\}$. This is consistent with $|\lambda_{\min}| \sim K \cdot |\text{rel min}|$ (since $\lambda_{\max}$ grows linearly with $K$ and rel min is constant).

**Architectural implication.** The detector's signal structure is finite-dimensional and combinatorial: one negative eigenvalue per off-line pair, with fixed signal strength. This raises a natural next question: if one ran D-H at higher $T_{\max}$ (revealing more off-line zero pairs), would the negative-eigenvalue count grow accordingly?

**3D.4 confirms YES** (T_max scaling). At $T_{\max} = 200$ D-H has 4 distinct off-line $\gamma$'s in UHP (at heights $\sim 85.7, 114.2, 166.5, 176.7$); at $T_{\max} = 300$ a 5th off-line pair appears at $\gamma \approx 240.4$; at $T_{\max} = 350$ two more pairs appear at $\gamma \approx 320.9$ and $331.0$. The negative eigenvalue count of $M^{DH}$ tracks exactly:

| $T_{\max}$ | # distinct off-line $\gamma$'s | $n_{\rm neg}$ (measured) | rel min eig | increment |
|---|---|---|---|---|
| $200$ | $4$ | $4$ (MATCH) | $-2.599 \times 10^{-2}$ | baseline |
| $300$ | $5$ | $5$ (MATCH) | $-2.599 \times 10^{-2}$ | +1 |
| $350$ | $7$ | $7$ (MATCH) | $-2.599 \times 10^{-2}$ | **+2 (non-trivial)** |

The double-increment between $T_{\max} = 300$ and $350$ is a non-trivial test: the prediction must hit exactly $n_{\rm neg} = 7$, not just "monotonically larger." It does. **The structural prediction is sharply validated.**

Additionally, the relative min eigenvalue is **identical to 4 sig figs at all three $T_{\max}$ values**: $-2.599 \times 10^{-2}$. Combined with 3D.3's $K$-invariance (3D.3 found rel min $\sim -2.62\%$ across $K \in [300, 1000]$ at fixed $T_{\max} = 200$), the asymptotic constant is universal: invariant under both $K$ and $T_{\max}$ extensions. Selberg-class L-functions ($\zeta, \chi_3, \chi_4$) stay PSD to floating-point noise at all tested $T_{\max}$. This closes the architectural picture of the wrong-approach detector:

**The Gram-matrix detector is structurally counting off-line zero pairs**, with fixed per-pair signal strength of $\sim 2.6\%$ of $\lambda_{\max}$.

Extension to $T_{\max} > 350$ is bottlenecked by the D-H zero finder (uncached zeros at $T_{\max} = 500$ exceeded 10 min runtime); the prediction is expected to hold trivially given the structural picture.

### 1. Level 4 (positivity) is the only level that's been shown to actually discriminate $\zeta$ from D-H computationally.

The four-level framing in [docs/02_graduate/log_correlated_fields_intro.md](../docs/02_graduate/log_correlated_fields_intro.md) §6 says: RH lives at Level 4 (Weil positivity), not Level 3 (spectral / statistical). The experiments have now produced a concrete computational instance of this claim:

- **Arch 3 (positivity) at the Gram-matrix level (3C.2, 3D, 3C.3, 3D.2):** the Weil quadratic form via Gram-matrix eigenvalue analysis returns PSD for $\zeta, \chi_3, \chi_4$ (all Selberg-class, GRH-believed) and **indefinite** for D-H, with the witness deepening monotonically as the basis size grows ($-2.4 \times 10^{-2} \to -3.7 \times 10^{-1}$ for $K = 20 \to 100$). The same witness vector $c^*$ that flags D-H gives $W_\zeta(c^*), W_{\chi_3}(c^*) \geq 0$: the detector is direction-selective, not L-function-blind.
- **Arch 1 (spectral) at every level we tested:** bare Berry-Keating (1A), three Sierra-Townsend variants (1B), and the explicit L-function discrimination test (1C) all produce H matrices with no L-function input. After best affine rescaling, RMS deviations from first 40 $\gamma_n^\zeta$ and from first 40 $\gamma_n^{DH}$ are both in $[2.4, 5.1]$; the discrimination ratio $\mathrm{RMS}_\zeta / \mathrm{RMS}_{DH}$ spans a factor of 3.35 around 1, consistent with random alignment of similar-density sequences.

The lesson is concrete: a structural test that lives at Level 3 (spectral signature, density) cannot tell us which L-function we're looking at, because the input quantities (eigenvalues, densities) don't see the Euler product. The same construction "matches" zeta and D-H equally well, even though one satisfies RH and the other doesn't. Positivity-based tests that take in the actual zeros (Gram matrix of $\Phi_b(\rho)$ values) do see the difference.

### 2. Small-$n$ Li-positivity does not distinguish; large-$n$ Li does. The discrimination scale is $n \sim 320{,}000$ for D-H.

The Li criterion $\lambda_n \geq 0 \iff$ RH is unconditional, so D-H must have negative $\lambda_n$ at some $n$. 3B computed $\lambda_n$ at $n \leq 300$ and found **both $\zeta$ and D-H are strictly positive** in that range. The reason: for the first D-H off-line zero ($\rho \approx 0.8085 + 85.7i$, FE partner $0.192 + 85.7i$), $|w_{\rm off}| - 1 \approx 4.2 \times 10^{-5}$, so the off-line contribution becomes order 1 only at $n \approx 24{,}000$, and exceeds the on-line $(n/2)\log(qn/(2\pi))$ asymptotic only at $n \gtrsim 320{,}000$.

3B.2 computed $\lambda_n^{DH}$ at large $n$ via the decomposition $\lambda_n^{DH} = \lambda_n^{DH, \rm asymp} + \sum_{\rho_{\rm off}} 2\,\Re(w_{\rm on}^n - w_{\rm off}^n)$ and **directly witnessed $\lambda_n^{DH} < 0$ at $n = 400{,}000$** (off-line correction $-2.0 \times 10^7$ vs asymptotic $+2.4 \times 10^6$) and **at $n = 10^6$** ($-3 \times 10^{18}$). The sign oscillates as $\cos(n \arg(w_{\rm off}))$ with amplitude growing as $|w_{\rm off}|^n$, so not every $n$ past the crossover gives negative $\lambda_n^{DH}$ (e.g., $n = 500{,}000$ landed on a positive phase).

This is a non-trivial structural result. **The Li criterion does correctly distinguish RH from non-RH; the discrimination scale is just large**, roughly $n \sim 1/|w_{\rm off} - 1|^2$ rather than $n \sim 1/|w_{\rm off} - 1|$. Any proof attempt that argues $\lambda_n \geq 0$ via methods that work uniformly out to $n = O(10^3)$ is structurally insufficient: the same arguments would conclude the same for D-H. To use the Li criterion as a discriminator computationally, you need $n \gtrsim 10^5$ scale or you need a different positivity test entirely.

The methodologically correct upgrade was the Weil quadratic form (3C-3D, 3C.3, 3D.2): same positivity principle, but evaluated via test functions (the $\Phi_b$ family) where the phase of $\hat f(\rho)$ at off-line $\rho$ shows up immediately. The Gram-matrix detector discriminates D-H at $K = 30$ test functions and $T_{\max} = 200$, vastly cheaper than the $n \sim 4 \times 10^5$ needed for Li.

### 3. The Davenport-Heilbronn discipline has been operationally validated.

D-H was introduced as a structural counter-example: any Arch 1/3/4 method that does not distinguish $\zeta$ from D-H is wrong. After the session's experiments, this discipline has now done concrete work twice:

- **It killed a plausible approach** (small-$n$ Li, 3B). Without the D-H control, Li-positivity at $n \leq 300$ looked like a clean positive signal for $\zeta$. With it, we recognized the signal as not actually testing RH.
- **It validated the right approach** (Gram-matrix Weil form, 3C.2 + 3D.2). The detector flags D-H indefinite (correct) and the Selberg-class L-functions PSD (correct). The cross-cut with $\chi_3, \chi_4$ then confirmed the detector is not just "different from $\zeta$" but specifically responding to off-line zeros.

Architecturally: D-H is the project's "false-positive filter." Any method that survives the D-H test deserves further investigation; any method that fails it (passes for D-H as well as $\zeta$) is structurally wrong even if it looks correct on $\zeta$ alone.

### 4. Spectral constructions without arithmetic input are uniformly bounded in their L-function discrimination.

The full Arch 1 result (1A + 1B + 1C) provides a quantitative version of "Hilbert-Pólya needs arithmetic input": across six H matrices we tested (three boundary conditions in 1A, three Sierra-Townsend variants in 1B), the discrimination ratio after best affine rescaling spans $[0.50, 1.67]$ — factor 3.35 spread. A genuine Hilbert-Pólya construction whose eigenvalues are exactly $\{\gamma_n^\zeta\}$ would give RMS$_\zeta = 0$ and RMS$_{DH} \sim 10$, giving ratio $0$. The factor-3 spread we see is consistent with random alignment between two similar-density gamma sequences, not with arithmetic content.

What this rules out is **strong**: no fixed-domain discretization of any operator of the form $H = (xp + px)/2 + V(x)$ (for any $V$) can prove RH, because the same H matrix is L-function-agnostic. The only viable spectral directions are constructions whose H matrix encodes the Euler product (or equivalent arithmetic input), like Connes' adèle class space (1D), which is the deferred-literature task.

### 5. Single-coefficient multivariate Fejér LPs decompose; balanced-sum LPs do not. (REFINED via 4E.)

4D-ii and 4D.2 established the *single-coefficient* decomposition: max $c_{1, \ldots, 1}$ at $d$-degree $(N, \ldots, N)$ saturates the tensor product. 4E (e4e_offdiag_lp.py) generalizes the question and finds the picture is family-dependent.

**Single-coefficient family decomposes.** For 4D/4D.2 and 4E Test A combined:
$$\max c_{j_1, \ldots, j_d} = \prod_{i=1}^d (\max_Q q_{j_i}) = \prod_i q_{j_i}^{1D}(N)$$
at $d$-degree $(N, \ldots, N)$, for any $(j_1, \ldots, j_d)$. The LP-optimal coefficient tensor is rank 1, and the LP value equals the asymmetric tensor product of independently chosen 1D optima. For $d = 2$, $j = k = 1$: $q_1^{1D}(N) = 2\cos(\pi/(N+2))$ (Fejér).

**Balanced-sum-of-diagonal family does NOT decompose, and the gap is weight-dependent.** For the objective $c_{1,1} + \alpha c_{2,2}$ at bidegree $(N, N) = (2, 2)$, 4E (at $\alpha = 1$) and 4E.2 (alpha sweep) together establish that the LP value strictly exceeds the Cauchy-Schwarz tensor bound $16/(8 - \alpha)$ over the range $\alpha \in (0, 8]$, with relative gap peaking at $+25.00\%$ for $\alpha = 3$:

$$\max\, c_{1,1} + 3 c_{2,2}\,(\text{LP}) = 4.0000 \quad > \quad \max_Q (q_1^2 + 3 q_2^2) = \tfrac{16}{5} = 3.2000.$$

The original 4E finding ($\alpha = 1$, +12.1%) is a single point on this curve. Other findings: gap peaks smoothly at $\alpha = 3$ then decays; **3-term diagonal sum** $c_{1,1} + c_{2,2} + c_{3,3}$ at bidegree $(3,3)$ gives gap +1.98%, an **8.66x increase** over the 2-term sum at the same bidegree (+0.23%). The LP-optimal coefficient matrix is full rank $N+1$ with $\sigma_2/\sigma_1 \in [0.43, 0.78]$, robust across grid resolutions.

**Closed-form structure at the peak.** At $\alpha = 3$, $N = 2$, the LP-optimal coefficient matrix has clean rational entries: $c_{1,1} = 8/5, c_{2,2} = c_{0,2} = c_{2,0} = 4/5$, parity structure $c_{j,k} = 0$ for $j + k$ odd. In $(u, v) = (\theta + \phi, \theta - \phi)$ coordinates, $5 P = 5 + 4\cos u + 4 \cos v + 8 \cos u \cos v + 2 \cos 2u + 2 \cos 2v$, which contains $\cos 2u, \cos 2v$ without their tensor partners $\cos 2u \cos v, \cos u \cos 2v$ — algebraically ruling out factorization. The clean rationals suggest a closed-form derivation of this optimum is possible.

**Off-diagonal-sum family does NOT exceed tensor either.** For $c_{1,2} + c_{2,1}$ at bidegree $(N, N)$ (Test C), the LP value is **strictly less than** the Cauchy-Schwarz tensor bound. The LP-optimal $c_{j,k}$ matrix has rank $> 1$ but this is an LP-vertex degeneracy: a tensor product witness achieves the same LP value.

**The corrected structural statement.** The 4D claim "the d-variate LP decomposes; no new auxiliary inequality" is true for *single-coefficient* objectives at uniform degree, and even for *some* sum objectives (like Test C's $c_{1,2} + c_{2,1}$). It is **false** for the balanced-diagonal-sum objective $c_{1,1} + c_{2,2}$: the LP value at $N = 2$ exceeds the tensor bound by 12%, and the optimal polynomial is genuinely 2D.

**Earlier convention error remains.** The original 4D-ii narrative had a separate convention bug (comparing $(c_1^{4B})^d$ vs $(2 c_1^{4B})^d = (q_1^{1D})^d$); that bug is fixed in [4D's writeup](../zero_free/README.md#4D). 4E's finding is independent of the convention question: it's about which LP objectives produce rank-1 vs full-rank solutions and whether the LP exceeds the tensor bound.

**Methodological lesson.** "Does the LP decompose?" is answered by two diagnostics combined: (1) rank of the LP-optimal coefficient matrix via SVD, and (2) comparison of the LP value to a Cauchy-Schwarz-derived tensor product bound. Rank $> 1$ alone is not sufficient (Test C has rank $> 1$ but LP value matches tensor bound, so the LP has a rank-1 optimal solution that the solver missed). The pair "rank $> 1$ AND LP > tensor bound" is the right test for genuine new content.

**What this leaves open.** The 12% improvement at $N = 2$ is on the auxiliary inequality, not yet on the zero-free region constant. **(Resolved by 4E.3:** see finding 8 below.) The other open directions from the original 4D remain: constrained-domain LP (e.g., $P \geq 0$ only on a submanifold corresponding to a hypothetical off-line zero), and Heath-Brown-style cross-prime coupling.

### 8. The C-S figure of merit and the MT figure of merit are structurally distinct: 4E.2's +25% LP gap does NOT translate into a zero-free region improvement.

4E.2 produced a +25% gap to the Cauchy-Schwarz tensor bound on $\max c_{1,1} + 3 c_{2,2}$ at bidegree $(2, 2)$. The natural next question (open #3 in the LEARNINGS earlier version): does this gap improve the Mossinghoff-Trudgian zero-free region constant $C$ in $\beta < 1 - C/\log|t|$? 4E.3 (e4e3_mt_translation.py) answers no, with both numerical evidence and a structural lemma.

**Numerical evidence.** Take the 4E.2 peak polynomial at $(\alpha, N) = (3, 2)$: $c_{0,0} = 1, c_{1,1} = 8/5, c_{2,0} = c_{0,2} = c_{2,2} = 4/5$. Restrict to 1D via various heights $(t_1, t_2)$. The MT shape factor (divided by $P(0)$ as a proxy for the boundary $R(P)$) is computed for each reduction and compared to the 1D Fejér optimum at the same effective degree:

| Reduction | shape/$P(0)$ | eff deg | Fejér shape/$P(0)$ at same deg | ratio |
|---|---|---|---|---|
| $t_1 = t_2 = \gamma_0/2$ | $0.000909$ | $2$ | $0.01472$ | $0.062$ |
| $t_1 = \gamma_0, t_2 = \gamma_0/2$ | $0.002000$ | $3$ | $0.02520$ | $0.079$ |
| $t_1 = t_2 = \gamma_0$ | $0$ | $4$ | $0.02885$ | $0$ |

Best 2D-derived shape/$P(0)$ is 12.6x worse than 1D Fejér at matched degree. Across the $\alpha \in [0, 10]$ sweep, no choice produces a 2D polynomial whose 1D restriction beats 1D Fejér; the maximum ratio (0.958) is achieved by the trivial tensor product at $\alpha = 0$.

**Structural lemma.** For any non-negative bivariate trig polynomial $P(\theta, \phi) \geq 0$ on $[0, 2\pi]^2$, the restriction $\tilde P(u) := P(t_1 u, t_2 u)$ is a non-negative 1D trig polynomial on $[0, 2\pi]$. The argument is one line: $(t_1 u, t_2 u)$ is a point of $[0, 2\pi]^2$ (modulo periodicity), so $P \geq 0$ everywhere implies $\tilde P(u) \geq 0$.

Hence the family of effective 1D polynomials from 2D restriction is a SUBSET of all 1D non-neg trig polynomials at matched effective degree. The MT figure of merit, which involves $\max c_1$ over the non-neg cone, is therefore bounded above by 1D Fejér. **No 2D bivariate restriction can break the 1D Fejér ceiling on the single-zero MT zero-free region constant.**

**The two figures of merit see different things.** The 4E.2 +25% gap is a real structural finding: the LP $\max c_{1,1} + 3 c_{2,2}$ over 2D non-neg polynomials at bidegree $(2, 2)$ exceeds the Cauchy-Schwarz tensor bound, and the LP-optimal polynomial has genuinely 2D coupling (clean rational coefficients with $\cos 2u, \cos 2v$ appearing without their tensor partners in $(u, v) = (\theta + \phi, \theta - \phi)$ coordinates). But the C-S figure of merit (max linear combination of $c_{j,k}$) and the MT figure of merit (max $c_1$ after 1D restriction) optimize different functionals. The 4E.2 LP shifts mass to $c_{2,2}, c_{2,0}, c_{0,2}$ to gain on the C-S objective; in MT bookkeeping this mass lands at the pole frequency (inflating $c_0$) or at $h = 2\gamma_0$ (which doesn't probe the trick zero at $\gamma_0$).

**What this rules out.** Any "shortcut" from the bivariate LP framework to the de la Vallée Poussin / Mossinghoff-Trudgian single-zero zero-free region constant via simple 1D restriction. This includes the natural family $\max c_{1,1} + \alpha c_{2,2}$ across all $\alpha$, all reductions $(t_1, t_2) \in \mathbb{R}^2$, and all bidegrees.

**What this does NOT rule out.**

- Constrained-domain LP: $P \geq 0$ only on a submanifold corresponding to a hypothetical off-line zero (e.g., $\phi = 2\theta$ for a zero probed at heights $\gamma$ and $2\gamma$). The submanifold-constrained polynomial is NOT bounded by the unrestricted 1D Fejér.
- Polynomial-ideal sum-of-squares decompositions modulo prime-coupling relations.
- Multi-zero or multi-character setups (Heath-Brown's actual use of bivariate inequalities in the least-prime-in-AP and Siegel-zero problems).
- Higher-rank LP families: $d$-variate at $d \geq 3$ with non-degenerate weights, where the structural lemma still applies but the matching becomes more delicate.

These are queued as 4E.4 follow-ups; none are pursued in 4E.3.

**Lesson.** A real structural improvement on one figure of merit does not automatically transfer to a different figure of merit even when both involve the same family of polynomials. The 4E ↔ 4E.2 ↔ 4E.3 progression illustrates how a "+25% gap" finding can be both real and computationally beneficial somewhere AND irrelevant to the headline RH-style application. Future LP-based architecture-4 work should specify the figure of merit explicitly and target it directly, not target a proxy and hope it transfers.

### 9. The d-variate balanced-sum LP gap grows sub-linearly with $d$: +25% (d=2), +51% (d=3), $\sim$+62% (d=4).

4E.4 and 4E.5 extend the bivariate balanced-sum LP of 4E / 4E.2 to higher dimensions: max $c_{1, \ldots, 1} + \alpha c_{2, \ldots, 2}$ at uniform degree $(N, \ldots, N)$ for $N = 2$. The peak gaps to the symmetric tensor bound:

| $d$ | LP variables | peak $\alpha$ | peak gap (M-corrected) |
|---|---|---|---|
| $2$ (4E.2) | $3^2 = 9$ | $3.00$ | $+25.00\%$ |
| $3$ (4E.4) | $3^3 = 27$ | $3.25$ | $\sim +50\%$ (interval $[47\%, 51\%]$) |
| $4$ (4E.5) | $3^4 = 81$ | $4.50$ | $\sim +62\%$ (interval $[55\%, 70\%]$) |

The d=2 → d=3 jump nearly doubles the gap (25 pp); the d=3 → d=4 jump adds less (15 pp). The increment per dimension shrinks. A naive linear prediction $(d-1) \times 25\%$ would give 75% at d=4, above the observed range. The pattern is sub-linear and likely saturates at some limit below $100\%$ as $d \to \infty$.

**Peak $\alpha$ grows with $d$.** The optimal weight on the higher-order term $c_{2, \ldots, 2}$ rises ($3.0 \to 3.25 \to 4.5$), consistent with higher-dimensional structure putting more emphasis on higher-order coupling.

**M-convergence at d=3.** At $\alpha = 3$ exactly, LP values across $M_{3D} \in \{40, 70, 100\}$ are $\{4.95, 4.89, 4.87\}$ with $P_{\min}$ approaching 0. The M=100 LP value 4.8665 with $P_{\min} = -2.9 \times 10^{-4}$ gives a tight lower-bracket of 4.865, so the true LP value at $\alpha = 3$ is in $[4.865, 4.867]$, gap $[+47.0\%, +47.1\%]$. The M=60 sweep at $\alpha = 3.25$ gives +51.3% (slight overestimate).

**M-convergence at d=4.** Heavier: $M^4$ constraints. At $\alpha = 4.5, M = 35$ (1.5M constraints): LP = 7.64, $P_{\min} = -0.099$, lower bracket = 6.95, gap in $[+54.5\%, +69.8\%]$. Larger $M$ would narrow this further but requires $\geq 10^7$ constraints.

**Peak coefficient tensors.** $d = 2$ had clean rationals ($1, 8/5, 4/5, 4/5, 4/5$). $d = 3$ at $M = 60$ gave $c_{1,1,1} = 2.637, c_{2,2,2} = 0.754$, lower-order entries $\sim 0.6$, without an obvious clean-rational form (some asymmetry consistent with LP noise). $d = 4$ similarly lacks an evident clean structure at the M values reached.

**What this does NOT mean for RH.** Per finding 8 (4E.3 structural lemma), any d-variate non-neg polynomial restricted to a line is a 1D non-neg trig polynomial bounded by 1D Fejér at matched effective degree, FOR ANY $d$. The +62% trivariate-or-higher gap still does NOT translate into a better single-zero MT zero-free region constant. The growth-with-dimension result characterizes the structure of multivariate auxiliary inequalities themselves, independent of the RH application.

**What this MIGHT mean for the broader picture.** The sub-linear growth of the LP-vs-tensor gap with $d$ suggests that the bivariate LP (4E.2) already captures most of the available LP-vs-tensor gap. Going to higher dimensions yields diminishing returns. If a future application uses d-variate non-negativity in a context where the structural lemma does NOT apply (multi-zero coupling, constrained domain, polynomial-ideal SOS), the d-variate gap is the relevant figure of merit, but the d=2 result already captures more than half of what's achievable.

### 6. The arithmetic-geometric architecture is the only one that has produced an actual RH theorem in our experiments — and 2A pins down precisely why.

Arch 2B verified the Weil RH for the elliptic curve $E: y^2 = x^3 + x + 1$ over $\mathbb{F}_5$ exactly: Frobenius eigenvalues $\alpha = -3/2 \pm i\sqrt{11}/2$, $|\alpha|^2 = 5$, and $|C(\mathbb{F}_{5^k})|$ matches the Weil formula at $k = 1, \ldots, 6$ by brute-force point counting. This is not "evidence for RH"; it is RH for that curve, proved.

**2A** traces the proof step by step against $\mathrm{Spec}(\mathbb{Z})$. The two companion docs:
- [2A_weil_proof_diff.md](../experiments/arithmetic_geometric/2A_weil_proof_diff.md): the diff itself + §4 expansion + §5 list of 17 constraints the missing mathematics must satisfy
- [2A_candidate_evaluation.md](../experiments/arithmetic_geometric/2A_candidate_evaluation.md): checkable predicates for each constraint + submission template for new candidates + scorecards for the six major existing candidates (Deitmar, Lorscheid, Borger, Connes, Deninger, Connes-Consani) + kill criteria

The proof's structural shape — **Lefschetz fixed-point + Poincaré duality + Hodge index theorem** — works for curves over $\mathbb{F}_q$ because all three pieces exist on the SAME object (the surface $C \times C$). Over $\mathrm{Spec}(\mathbb{Z})$, each piece is either missing entirely or available only in a partial form:

- **Lefschetz**: requires a geometric Frobenius endomorphism. $\mathrm{Spec}(\mathbb{Z})$ has none; Connes proposes the $\mathbb{R}^*_+$-action on the adèle class space and Deninger proposes a real-time flow on a hypothetical foliated space, but neither object has been built.
- **Poincaré duality**: requires a non-degenerate cohomological pairing on $\mathrm{Spec}(\mathbb{Z}) \times \mathrm{Spec}(\mathbb{Z})$, which in turn requires a "base below $\mathbb{Z}$" (traditionally called $\mathbb{F}_1$). The functional equation $\xi(s) = \xi(1-s)$ gives the consequence at the L-function level but not the underlying cohomology pairing.
- **Hodge index theorem**: requires a 2-dimensional geometric object (the surface $C \times C$ in the function-field case). Without the surface $\mathrm{Spec}(\mathbb{Z}) \times_{\mathbb{F}_1} \mathrm{Spec}(\mathbb{Z})$, no analogue. The Arch 3 finding (#7, the Weil-form duality circularity) is the analytic shadow of this missing geometric positivity.

**The single-sentence diagnosis**: Architecture 2's obstruction is constructive, not analytic — the proof template is well-understood, but the underlying object on which to instantiate it has not been built. The three programs (Connes, Deninger, $\mathbb{F}_1$) each address one corner of the obstruction triangle (Frobenius / surface / positivity respectively), but no single program has assembled all three.

**The universal scorecard finding** (from `2A_candidate_evaluation.md`): scored against the 17 specific constraints, the six major candidates collectively cover the Frobenius slot (constraints viii-x, especially Connes and Borger) and the base slot (i-iii, especially Deitmar and Lorscheid), but **no candidate has even a partial ✅ on the Hodge index positivity slot (xi-xiii)**. The deepest open problem is constructing a positivity certificate on the (hypothetical) surface $\mathrm{Spec}(\mathbb{Z}) \times_{\mathbb{F}_1} \mathrm{Spec}(\mathbb{Z})$ that is provable WITHIN the new framework, not requiring RH as input. Most "RH proofs" in the literature fail kill criterion K1: they reduce RH to a different positivity statement that is morally RH-equivalent rather than providing an independent constructive proof.

**Cross-cut to Arch 3 (positivity).** Arch 3 probes the (c) Hodge-index slot analytically rather than geometrically (Weil positivity on test functions). Arch 3F-3I (the Weil-form duality experiments) found that the analytic version hits a circularity wall: any unconditional proof requires GRH-strength input. This is consistent with 2A's diagnosis — the analytic shadow inherits the circularity of the missing geometric positivity. **The analytic and geometric obstructions are the same obstruction, viewed from two sides.**

2B is the only architecture in our set where the proof template actually closes; the other three architectures' obstructions all reduce, in different ways, to "we don't have the cohomology over $\mathbb{Z}$ that we have over $\mathbb{F}_q$."

### 7. The Weil-form duality is computable, and the cancellation structure on the prime side reveals where the analytic obstruction lives.

For $\zeta$, Weil positivity $W(b) = \sum_\rho \Phi_b(\rho)^2 \geq 0$ can be computed from either the zero side (the sum over $\rho$) or from the prime side via Bombieri's explicit formula:
$$W(b) = \underbrace{8(b^{1/2} - b^{-1/2})^2}_{\text{boundary}} - 2\sum_{p^k < b^2} \tfrac{\log p}{p^{k/2}}(2\log b - k\log p) - (\log 4\pi + \gamma_E)\cdot 2\log b - \int_1^\infty \tfrac{f(x) + f(1/x)/x - 2f(1)/x}{x - 1/x}dx.$$

3F verifies the two sides agree to $<2\%$ at $T_{\max} = 1000$, $b \geq 14$, with the residual error matching the expected $O((\log T)/(\pi T))$ truncation. The framework is correctly implemented.

**The cancellation structure.** At $b = 20$, the four prime-side components are $+144, -120, -19, -5$, summing to $\sim 0.1$. The prime sum cancels 83% of the boundary; the constant and gamma integral together cancel most of the remainder. Each component is $O(10^2)$ relative to $W$ of $O(10^{-1})$ — three orders of magnitude of cancellation.

**Why this is the analytic obstruction.** A proof of Weil positivity from the prime side requires bounding $\sum \Lambda(n) n^{-1/2} (2 \log b - \log n)_+$ from above by the boundary $+$ constants $+$ gamma integral, *without using zero locations*. The best unconditional PNT (Vinogradov-Korobov) gives $\psi(x) - x = O(x \exp(-c (\log x)^{3/5}))$, an error of order $x$. The cancellation we observed has margin $\sim 0.1\%$ of the component magnitudes. The PNT error is far too loose. Improving it to a power-saving error term ($\psi(x) - x = O(x^\theta)$ for $\theta < 1$) is *equivalent* (up to bookkeeping) to a zero-free region with that exponent. To break Weil positivity's analytic obstruction one needs a fundamentally new way to bound the prime sum — Bombieri's "variational approach" (2003), Connes' trace-formula construction, and Deninger's motivic cohomology are three ongoing programs aimed at this.

**Three L-functions tested (3G, 3H).** The cross-comparison sharpens the picture:

| L-function | Pole at $s = 1$ | Coefficient sign | Largest comp ($b=20$) | $\lvert W \rvert$ | Cancellation ratio |
|---|---|---|---|---|---|
| $\zeta$ | YES | $\Lambda(n) \geq 0$ all positive | $144$ (boundary) | $0.1$ | $\sim 10^{-3}$ |
| $\chi_3$ | no | $\Lambda(n) \chi_3(n) \in \{\pm 1, 0\}$ | $5.77$ (prime sum) | $0.24$ | $\sim 4 \times 10^{-2}$ |
| D-H | no | $b_n^{DH}$ oscillating, no $\Lambda$ structure | $2.83$ (Dirichlet sum) | $0.31$ | $\sim 1.3 \times 10^{-1}$ |

**The tight cancellation is specifically a feature of $\zeta$'s pole at $s = 1$, not of Euler products in general.** $\chi_3$ also has an Euler product but no pole and shows mild cancellation comparable to D-H, not tight cancellation like $\zeta$. The mechanism: $\zeta$'s pole forces a large positive boundary $\sim b^{1/2}$; $\Lambda(n) \geq 0$ forces a large positive prime sum; the tight cancellation between these two is what we observe at $\sim 10^{-3}$. For all other Selberg-class L-functions (which are entire), no pole means no boundary, and the prime sum has internal cancellation from the character.

**The χ_3 unconditional path tested (3I): blocked by the same wall.** I conjectured in 3H that χ_3's mild cancellation might be unconditionally achievable via Siegel-Walfisz-strength estimates. **3I verifies this is wrong.** The Siegel-Walfisz bound on $|\psi(x, \chi_3)|$, applied via partial summation against the boxcar test kernel, is too loose by factor 33× at $b = 10$, growing to 122× at $b = 100$. The ratio gets *worse* as $b$ grows.

**Why:** partial summation kills the cancellation that makes the weighted prime sum small. To get a tight bound on the weighted prime sum, you'd need to control the *zeros* of $L(s, \chi_3)$ — which is GRH for $\chi_3$, what we're trying to prove. Same circularity as ζ.

**The wall isn't ζ-specific; it's a feature of all Selberg-class L-functions.** Even with mild cancellation, the gap between current unconditional bounds and required margin is factor 30-100 for χ_3 (vs factor ~5-10 for ζ). Both are blocked by the same circularity: you need GRH-strength input to bound prime sums tightly enough.

**Implication for the RH route.** Among Selberg-class L-functions, **ζ is exceptionally hard for the Weil-form route** at the level of cancellation tightness. But for ALL of them (ζ, Dirichlet L's, modular L's), the unconditional path through Weil positivity hits the same fundamental wall — getting tighter control on $\psi(x, \chi)$ unconditionally than current Siegel-Walfisz-strength bounds. This is consistent with the historical pattern: many partial results (positive proportion of zeros on line, Levinson-Conrey for ζ and χ_3 alike), but no path through full Weil positivity for any non-trivial L-function. The Weil-form route is structurally blocked across the Selberg class.

**The path forward must avoid the partial-summation step entirely.** Either work directly with the L-function (Connes' adèle class space, Deninger's cohomology) without going through the prime sum, OR find a positivity certificate that doesn't require the prime sum to be bounded *tightly* (sum-of-squares decomposition for the Weil form, as in Bombieri's variational approach).

---

## Per-architecture summary of what is open

### Arch 1 (spectral): no further computational lift expected; the door is now Connes-style.

1A + 1B + 1C closed the door on the BK family and ST-style modifications. The remaining direction (1D, Connes adèle class space) is a literature/theory task, not numerical. No further Arch 1 numerical experiment is expected to produce new structural information.

### Arch 2 (arithmetic-geometric): the open frontier is literature-and-construction work; 2A has now mapped it and provided an evaluation framework.

2B (worked example over $\mathbb{F}_5$) is one of the strongest results we have, but it doesn't move toward $\mathrm{Spec}(\mathbb{Z})$. **2A** is complete and consists of two companion documents:

- [2A_weil_proof_diff.md](../experiments/arithmetic_geometric/2A_weil_proof_diff.md) — the diff itself, the constructive-obstruction analysis (§4), and the 17-constraint specification of what the missing mathematics must deliver (§5).
- [2A_candidate_evaluation.md](../experiments/arithmetic_geometric/2A_candidate_evaluation.md) — the methodology: checkable predicates per constraint, submission template for new candidates, scorecards for six major candidates, kill criteria.

Diagnosis: Architecture 2's obstruction is *constructive* — the proof template is well-understood, but the underlying object hasn't been built. The three programs (Connes, Deninger, $\mathbb{F}_1$ variants) each address one corner of the obstruction triangle but none has assembled all three on a single object. The universal scorecard finding: no candidate has even a partial ✅ on the Hodge index positivity slot (xi-xiii). This is the central open construction problem.

Remaining literature tasks (informed by the evaluation framework):
- ~~**R1** (lowest-hanging fruit per 2A_candidate_evaluation §V): sharpen the D-H exclusion check (xvii) for each candidate.~~ **Complete** ([2A_R1_DH_exclusion.md](../experiments/arithmetic_geometric/2A_R1_DH_exclusion.md)): all six candidates pass K2 by construction. **The structural reason**: D-H is defined by a linear combination of Dirichlet L-functions, which is an analytic operation on Dirichlet series rather than a geometric operation. None of the six frameworks (Deitmar, Lorscheid, Borger, Connes, Deninger, Connes-Consani) can construct linear combinations of L-functions as their natural output. K2 safety is conditional on the Selberg conjecture — if some Euler-product L-function were found to have off-line zeros (no known examples), K2 would become a live concern. This finding also surfaces a design constraint for future candidates: any framework whose L-function operation commutes with linear combination would fail K2 immediately.
- ~~**R2**: explicitly compute the fiber product $\mathrm{Spec}(\mathbb{Z}) \times_{\mathbb{F}_1} \mathrm{Spec}(\mathbb{Z})$ in Borger / Lorscheid.~~ **Complete** ([2A_R2_fiber_product.md](../experiments/arithmetic_geometric/2A_R2_fiber_product.md)). Borger gives Spec(W(ℤ)) via the big Witt ring functor (right adjoint to U: Λ-Rings → Rings); Lorscheid gives the blueprint (ℤ × ℤ, doubled relations). Both candidates produce non-trivial surface-like objects (constraint (ii) upgraded from ⏳/🟡 to 🟡 for both, with sharper picture). **Critical gap surfaced**: neither has developed intersection theory or Hodge index on the resulting surface — the constraints downstream of (ii) (specifically vi, vii, xi) remain open. R2 sharpened what the candidates ARE on the surface side; the central positivity construction problem is unchanged.
- **R3** (hardest): identify whether Connes-Consani's positivity conjecture is kill-criterion K1 (RH-equivalent) or has an independent constructive proof candidate.
- **R4**: explore hybrid candidates — the "Borger Frobenius + Connes trace formula" hybrid is most promising on paper.
- **2C** (state of the $\mathbb{F}_1$ / Arakelov programs as of 2025): the framework supports this naturally — write up the survey using the scorecard structure.
- **2D** (smallest open conjecture in Deninger's program): identify a meaningful target shorter than full RH.

These are not "experiments" in the numerical sense, but they now have a defined methodology and evaluation criteria.

### Arch 3 (positivity): the framework is robust; an open computational frontier exists (the $n \sim 350{,}000$ Li negativity).

The Gram-matrix detector works as a wrong-approach detector and survives Selberg-class cross-cuts. The framework has been validated. The remaining open computational task is: actually exhibit $\lambda_n^{DH} < 0$ for some $n$ around $350{,}000$ via the xi-derivative formula (3B-extension). This is heavy ($\geq 100$-digit precision and careful cancellation control) but would close the loop on the small-$n$ Li result. It is **not** required to validate Arch 3 — the Gram-matrix detector already does that — but it would be a direct demonstration of where the Li criterion goes negative for D-H.

### Arch 4 (analytic): the d-variate LP gap is real and grows with d, but does not improve the MT zero-free region constant under restriction (4E.3, 4E.4).

4B closed the 1D Fejér question. 4D-ii and 4D.2 confirmed that single-coefficient $d$-variate LPs decompose. 4E and 4E.2 found that balanced-diagonal-sum LPs $\max c_{1,1} + \alpha c_{2,2}$ do NOT decompose: LP value exceeds the C-S tensor bound by up to +25% at $\alpha = 3, N = 2$. **4E.4 extended to d=3** and found the gap nearly DOUBLES: +51% at $\alpha = 3.25, N = 2$, fitting the pattern $\sim (d-1) \times 25\%$.

**4E.3 closes the natural RH-application follow-up:** does the +25% (or +51%) gap improve the Mossinghoff-Trudgian zero-free region constant? Answer: NO. Both numerically (across all $\alpha$ and reductions) and structurally (any $d$-variate non-neg polynomial restricted to a line gives a 1D non-neg polynomial, bounded by 1D Fejér at matched effective degree). The C-S and MT figures of merit are incompatible; the $d$-variate restriction approach to MT is structurally capped by 1D.

So the architecture-4 numerical thread has converged: the bivariate / multivariate LP families are computationally well-understood (gap pattern with $d$ is known), but none of them produces a better zero-free region constant via the standard de la Vallée Poussin route.

Remaining open directions (NOT closed by 4E.3, NOT in the restriction route):
- **Constrained-domain LP** (4E.5): impose $P \geq 0$ only on a submanifold corresponding to a hypothetical off-line zero. The submanifold-constrained polynomial is NOT bounded by 1D Fejér.
- **Polynomial-ideal SOS** (4E.6): sum-of-squares decompositions modulo prime-coupling relations.
- **Multi-zero / multi-character coupling** (4E.7): Heath-Brown's actual use of bivariate inequalities in least-prime-in-AP / Siegel-zero problems (these involve multiple putative zeros, where 2D structure genuinely couples them).
- **4-variate or higher d** for the balanced-sum LP gap pattern: does the $(d-1) \times 25\%$ scaling continue?

4A (Vinogradov-Korobov reproduction) and 4C (conditional improvements) remain literature tasks.

---

## Methodological notes

### What test designs have worked

- **The PSD-of-Gram-matrix construction:** evaluating a sum $\sum_\rho \Phi(\rho_j) \Phi(\rho_k)$ at on-line zeros gives a real Gram matrix (automatically PSD); at off-line zeros it doesn't. Reduces the abstract positivity question to a finite-dimensional eigenvalue computation. This is the cleanest concrete realization of "Level 4 positivity" we have.

- **The L-function-class cross-cut:** running the same test on $\zeta$ (RH believed), $\chi_3, \chi_4$ (GRH believed; Selberg-class positive control), and D-H (RH known false; non-Selberg negative control) gives three calibration points. A test that distinguishes all three correctly is direction-selective.

- **Best-affine rescaling for spectral discrimination:** instead of comparing raw eigenvalues to zeta gammas (which forces a scale match), fit $E \mapsto \alpha E + \beta$ first and report residual RMS. Eliminates trivial scale mismatch as a confound.

- **High-precision arithmetic for slow-convergent sums:** mpmath at $\geq 30$ digits for any zero sum, Hurwitz zeta for Dirichlet L-functions, $Z_\chi$ sign-change scan for L-zeros. The smoke test catches regressions at 8/8 tests.

### What test designs did not work, or required correction

- **LP for nonneg multivariate trig polys at coarse grid:** at $M_{2D} = 50$, the 2D LP returned solutions with $P_{\min} \sim -10^{-2}$, i.e., genuinely infeasible on the continuum. Required $M_{2D} = 200$ for $P_{\min}$ to drop to floating-point noise. Lesson: pointwise constraints on continuous functions require fine sampling.

- **Comparison convention mismatch in the 4D multivariate LP:** an earlier version of the 4D / 4D.2 narrative claimed a "factor-of-$2^d$ advantage" of the LP over a "factorized witness." This was a convention error. The 1D Fejér theorem statement "max $c_1 = \cos(\pi/(n+2))$" uses the 4B convention $P = c_0 + 2\sum c_k \cos$, in which the raw coefficient of $\cos(\alpha)$ in the optimum $Q$ is $q_1 = 2 c_1$, not $c_1$. The tensor product $Q(\theta_1) \cdots Q(\theta_d)$ has raw $c_{1,\ldots,1} = q_1^d = (2 c_1)^d$, which equals the LP optimum. The "$2^d$ advantage" came from comparing the LP value to $c_1^d$ instead of $(2 c_1)^d = q_1^d$. Once the conventions are aligned, no advantage remains: the d-variate LP just finds the tensor product. **Lesson: whenever comparing an LP value to an analytic witness, write both in the same convention (raw coefficients of $\cos$ in the polynomial, not "doubled" or "Fourier-symmetric" conventions). Verify the rank of the LP-optimal coefficient tensor: if rank 1, the problem decomposes.**

- **Lowest-eigenvalue-of-real-Hamiltonian comparison without rescaling:** raw eigenvalues from a discretized $H_{BK}$ (range $[0, 20]$) compared to zeta gammas (range $[14, 143]$) gave RMS $\sim 88$, which obscured the actual L-function-blindness question. Best-affine rescaling (1C) made the structural comparison clean.

- **Compact-support test function for Li (e.g., truncating the explicit-formula sum at $T_{\max} = 200$):** the truncation error in Li coefficients at $n = 500$ is $\sim 17\%$, dominated by the $\sim n^2 \log T / (2\pi T)$ tail. To reach truncation accuracy 1% we'd need $T_{\max} \gtrsim 10^4$, requiring $\sim 12{,}000$ zeros. Feasible but not pursued; the qualitative result was already in hand.

### What machinery should be reusable across future experiments

- **The `LFunction` interface** in `experiments/_shared/lfunction.py`: every L-function (zeta, D-H, Dirichlet) implements `evaluate(s)` and `zeros(T_max, prec)` with disk caching. New L-functions can be added by subclassing and the existing experiments run on them unchanged.

- **The Gram-matrix scaling experiment template** (e3d2): pick a test family, an L-function set, a basis-size sweep, and report min eigenvalue. Generalizes to any "Level 4 positivity" test.

- **The discrimination-ratio test** (e1c): for any candidate $\zeta$-targeting construction, apply it to D-H (and ideally $\chi_3, \chi_4$) and compute best-affine RMS to each. A construction whose ratio is bounded by a factor of $\sim 3$ is L-function-blind.

---

## Open questions identified by the experiments

1. ~~**Does the 4D 2D-LP factor-of-4 result generalize to higher dimensions?**~~ ~~**Resolved (4D.2):** confirmed at $d = 3$.~~ **Resolved differently:** the "factor-of-$2^d$ advantage" was a convention error. The d-variate LP for max $c_{1,\ldots,1}$ at uniform degree $(N,\ldots,N)$ decomposes: the optimum is the tensor product $Q(\theta_1) \cdots Q(\theta_d)$ where $Q$ is the 1D Fejér optimum, giving $\max c_{1,\ldots,1} = (2\cos(\pi/(N+2)))^d = (q_1^{1D})^d$. No new inequality.

2. ~~**What LP family WOULD produce a genuinely new multivariate auxiliary inequality?**~~ **Resolved (4E + 4E.2):** the balanced-diagonal-sum family $c_{1,1} + \alpha c_{2,2}$ at bidegree $(2, 2)$ produces 2D inequalities not derivable from tensor products, with relative gap to the C-S tensor bound varying as $\alpha$ varies and peaking at +25.00% for $\alpha = 3$. Extension to higher bidegree with more diagonal terms (4E.2.b: $c_{1,1} + c_{2,2} + c_{3,3}$ at $N = 3$) increases the gap by 8.66x relative to the 2-term version at the same bidegree. The off-diagonal-sum $c_{1,2} + c_{2,1}$ does NOT exceed tensor bound. Remaining sub-directions: (a) constrained-domain LPs; (b) Heath-Brown cross-prime coupling; (c) closed-form derivation of the $\alpha = 3$ peak optimum.

3. ~~**Does the Mossinghoff-Trudgian zero-free constant improve when the 4E/4E.2 2D inequality is plugged in?**~~ **Resolved (4E.3): NO.** The +25% C-S gap does not translate to an MT improvement. Both numerically (the 4E.2 peak gives 12.6x WORSE shape/$P(0)$ than 1D Fejér at matched effective degree, and across $\alpha \in [0, 10]$ no 2D polynomial beats 1D Fejér) and structurally (any 2D non-neg polynomial restricted to a line is bounded by the 1D Fejér optimum). The C-S and MT figures of merit are incompatible; future LP-based zero-free-region work must target MT directly (via constrained-domain LP, multi-zero coupling, or polynomial-ideal SOS).

4. ~~**At what $n$ does $\lambda_n^{DH}$ first go negative?**~~ **Resolved (3B.2):** witnessed at $n = 400{,}000$ via the asymptotic-plus-off-line-correction decomposition. Off-line correction $-2.0 \times 10^7$ vs on-line asymptotic $+2.4 \times 10^6$. Crossover predicted at $n \sim 320{,}000$; phase determines sign past that. Refinement: a fully rigorous certificate (exact xi-derivative formula, ~100 digit precision, more off-line zeros) would replace the asymptotic with the exact value; the structural conclusion is robust.

5. ~~**Does the Gram-matrix wrong-approach detector remain a clean test in the limit $K \to \infty$ where $M^\zeta$ becomes singular but $M^{DH}$ continues to deepen?**~~ **Resolved (3D.3): YES, and the structural picture is cleaner than expected.** At $K \in [100, 1000]$ with $T_{\max} = 200$ (D-H has 8 off-line zeros, i.e., 4 conjugate pairs): the relative min eigenvalue $\lambda_{\min}/\lambda_{\max}$ for D-H converges to an asymptotic constant of $-2.62\%$. The number of negative eigenvalues stays FIXED at $4 =$ number of off-line zero pairs. Selberg-class L-functions ($\zeta, \chi_3, \chi_4$) remain PSD to floating-point noise. The detector is essentially counting off-line zero pairs via the negative-eigenvalue count, and the relative-min depth is dimension-independent.

6. **Is there an Arch-2-style "lift to $\mathbb{Z}$" that the experiments could probe, even partially?** 2B gave us RH for one curve over $\mathbb{F}_5$. An analogous "RH for a single object in $\mathrm{Spec}(\mathbb{Z})$" doesn't exist yet, but $\mathbb{F}_1$ literature gestures at it.

---

## Synthesis: where does the project stand?

Of the four architectures:

- **Arch 1 (spectral)** is closed at the numerical-experiment level. We've shown the simple constructions are L-function-blind; further progress requires Connes-style theory.
- **Arch 2 (arithmetic-geometric)** has produced the strongest individual result (Weil RH for one curve over $\mathbb{F}_5$, proved). 2A completes the diff-table analysis: the obstruction over $\mathrm{Spec}(\mathbb{Z})$ is *constructive*, not analytic — Weil's proof template needs a Frobenius substitute, a surface $\mathrm{Spec}(\mathbb{Z}) \times_{\mathbb{F}_1} \mathrm{Spec}(\mathbb{Z})$, and a Hodge index positivity on that surface; the three corresponding programs (Connes, Deninger, $\mathbb{F}_1$) each address one corner but no single program has assembled all three. The path forward is construction work.
- **Arch 3 (positivity)** has the most extensive experimental support: small-$n$ Li-positivity confirmed for $\zeta$ (but not a discrimination test); Weil-form-via-Gram-matrix works as a wrong-approach detector; Selberg-class cross-cut validates direction-selectivity. The next experimental step (xi-derivative Li at $n \sim 350{,}000$) is heavy but well-defined.
- **Arch 4 (analytic)** has a refined picture from 4D/4D.2 + 4E + 4E.2 + 4E.3 + 4E.4: single-coefficient multivariate Fejér LPs decompose to tensor products, but the balanced-diagonal-sum LP $\max c_{1,1} + \alpha c_{2,2}$ at bidegree $(2, 2)$ does NOT — peak gap +25.00% at $\alpha = 3$. The trivariate extension (4E.4) DOUBLES the gap to +51.29% at $\alpha = 3.25, N = 2, d = 3$, fitting the pattern $\sim (d-1) \times 25\%$. **However (4E.3)**: the d-variate C-S gap does NOT improve the Mossinghoff-Trudgian zero-free region constant for any $d$, neither numerically nor structurally. The C-S and MT figures of merit are incompatible: any d-variate non-neg polynomial restricted to a line is bounded by 1D Fejér at matched effective degree, so the d-variate restriction approach to MT is structurally capped. To actually improve the zero-free region via multivariate inequalities requires constrained-domain LP, multi-zero coupling, or polynomial-ideal SOS (queued as 4E.5-4E.7).

The structural message of the experiments: **only Arch 2 has the cohomology/positivity coupling that closes RH-style arguments in the function-field case; only Arch 3 has a positivity test that distinguishes Selberg-class L-functions from non-Euler-product look-alikes computationally; Arch 1 and Arch 4, on the numerical evidence here, do not close RH by themselves.**

This is consistent with the project's structural commitment (RH lives at Level 4 positivity, not Level 3 spectral signature) and with the strategic landscape in [docs/research_atlas/](../docs/research_atlas/).
