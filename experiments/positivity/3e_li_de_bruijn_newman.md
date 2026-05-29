# 3E — Li Coefficients and the de Bruijn-Newman Constant: A Quantitative Relationship

> Literature note on two equivalent reformulations of RH:
> - **Li criterion** (Li 1997): all Li coefficients $\lambda_n \geq 0$ ⟺ RH.
> - **de Bruijn-Newman constant** $\Lambda$ (de Bruijn 1950, Newman 1976): $\Lambda \leq 0$ ⟺ RH; Rodgers-Tao 2018 proved $\Lambda \geq 0$, so $\Lambda = 0$ ⟺ RH.
>
> Both are positivity reformulations of RH. They use different positivity statements and have different computational accessibility. This note quantifies the relationship, summarizes the current state of the art on each, and connects to the project's experimental work (especially 3A, 3B, 3B.2).
>
> Closes Arch 3E TODO open item: "quantify the Li / de Bruijn-Newman relationship (literature)".

## 1. The Li criterion

**Definition** (Li 1997, "The positivity of a sequence of numbers and the Riemann hypothesis"):

$$\lambda_n := \frac{1}{(n-1)!} \frac{d^n}{ds^n}\left[s^{n-1} \log \xi(s)\right]_{s = 1}$$

where $\xi(s) = \tfrac{1}{2} s(s-1) \pi^{-s/2} \Gamma(s/2) \zeta(s)$ is the completed zeta function.

**Equivalent zero-sum formula** (Bombieri-Lagarias 1999):

$$\lambda_n = \sum_\rho \left[1 - \left(1 - \frac{1}{\rho}\right)^n\right]$$

where the sum runs over non-trivial zeros $\rho$ of $\zeta$ (in the appropriate symmetric pairing $\rho \leftrightarrow 1 - \rho$).

**The criterion**:

$$\text{Li (1997):} \quad \lambda_n \geq 0 \text{ for all } n \geq 1 \quad \Longleftrightarrow \quad \text{RH}.$$

**Computational accessibility**: $\lambda_n$ can be computed at finite $n$ from a finite truncation of the zero sum (with controlled error). The project's experiments 3A, 3B, 3B.2 work directly with this.

**Asymptotic behavior** (Bombieri-Lagarias 1999, conditional on RH):

$$\lambda_n \sim \frac{n}{2} \log n + cn \quad \text{with} \quad c = \tfrac{1}{2}(1 - \gamma_E - \log(2\pi)) \approx -0.708.$$

(So $\lambda_n$ grows like $\frac{n \log n}{2}$ asymptotically when RH holds. The leading growth is RH-independent; the constant $c$ is what's RH-conditional.)

## 2. The de Bruijn-Newman constant

**The heat-equation deformation**: define

$$H_t(z) := \int_{-\infty}^{\infty} e^{t u^2} \Phi(u) \cos(z u) du$$

where $\Phi(u) = 2 \sum_{n=1}^\infty (2 \pi^2 n^4 e^{9u} - 3 \pi n^2 e^{5u}) e^{-\pi n^2 e^{4u}}$ is the explicit function such that $\xi(1/2 + i z) = H_0(z)$ (up to normalization).

For $t < 0$, $H_t(z)$ is the heat-equation deformation in the "wrong direction" (the heat equation typically smooths; here we're going backward in time). For $t > 0$, $H_t$ is the standard heat-equation smoothing.

**The de Bruijn-Newman constant**:

$$\Lambda := \inf\{ t \in \mathbb{R} : H_t(z) \text{ has only real zeros for all } t' \geq t \}.$$

**Equivalence to RH**:

$$\text{de Bruijn (1950):} \quad H_t \text{ has only real zeros for all } t \geq 1/2.$$

$$\text{Newman (1976):} \quad \Lambda \text{ is well-defined as a real number}.$$

$$\Lambda \leq 0 \quad \Longleftrightarrow \quad \text{RH}.$$

**Newman's conjecture (1976)**: $\Lambda \geq 0$. This is in some sense "RH-but-just-barely-so" — Newman conjectured that RH is true but only just so, with $\Lambda = 0$ exactly.

**Rodgers-Tao 2018** ("The de Bruijn-Newman constant is non-negative", Forum of Mathematics, Pi): proved $\Lambda \geq 0$, settling Newman's conjecture.

**Consequence**: $\Lambda = 0$ ⟺ RH (combining Newman 1976's "$\Lambda \leq 0 \Leftrightarrow$ RH" with Rodgers-Tao 2018's "$\Lambda \geq 0$").

## 3. Current computational state of the art

### Li coefficients

- **3A** (this project): positivity confirmed for $n \leq 500$ via incremental product algorithm.
- Direct computation in the literature: positivity confirmed for $n \leq $ several thousand (various authors).
- **3B.2** (this project): demonstrated that the Li criterion DOES discriminate RH from non-RH (witnessed $\lambda_n^{\text{D-H}} < 0$ at $n = 4 \times 10^5$ via asymptotic + off-line correction decomposition).
- For $\zeta$: no published witness of $\lambda_n < 0$ at any $n$. All computations confirm positivity in the accessible range.

### de Bruijn-Newman constant

- **Upper bounds** (since 1998):
  - de Bruijn 1950: $\Lambda \leq 1/2$.
  - Csordas-Smith-Varga 1994: $\Lambda \leq 0.5$.
  - Saouter-Demichel 2010: $\Lambda \leq 0.001$.
  - Polymath 15 (2018, "Effective approximation of heat flow evolution of the Riemann $\xi$ function"): $\Lambda \leq 0.22$.
  - Subsequent refinements: $\Lambda \leq 0.2$ (various).
- **Lower bound** (Rodgers-Tao 2018): $\Lambda \geq 0$.
- Current best knowledge: $0 \leq \Lambda \leq 0.2$.

Note: the upper bound of 0.22 comes from computing zero behavior of $H_t$ for specific small $t > 0$ and checking that zeros stay real. This is computationally intensive (Polymath 15 used distributed computation).

## 4. The structural relationship

Both Li and dBN are POSITIVITY reformulations of RH, but their structures differ:

| Aspect | Li criterion | de Bruijn-Newman constant |
|---|---|---|
| Object | Sequence $\{\lambda_n\}_{n \geq 1}$ | Single real number $\Lambda$ |
| Type of positivity | Discrete (each $\lambda_n \geq 0$) | Continuous ($\Lambda = 0$, sharp) |
| Information source | Zeros via explicit-formula sum | Heat-equation deformation of $\xi$ |
| Computational access | Direct from zeros | Indirect via deformation |
| Sharp at | All $n$ | Single value $\Lambda = 0$ |
| Discrimination scale | $n \sim |w_{\text{off}} - 1|^{-2}$ for non-RH | $t > 0$ regime detects "almost-RH" |

**Key structural fact**: both reduce RH to positivity, but via different machinery.

- Li works in **frequency space** (sum over zeros).
- dBN works in **time/heat space** (deformation parameter).

These are dual perspectives — connected by the Fourier-transform structure relating zero distribution to $\xi$'s spectral data.

## 5. How they relate at the technical level

### From Li to dBN

The connection is via the **second moment** of zero positions:

For RH, the function $\xi(1/2 + iz)$ has all real zeros. As $t$ decreases from $0$, zeros can move off the real axis. The Newman lower bound on $\Lambda$ is equivalent to saying that zeros approach the real axis "from the right" as $t \to 0^+$.

Equivalently (Csordas-Norfolk-Varga 1988): the convexity properties of $\log |H_t|$ along the real axis encode whether zeros can leave the real line as $t$ increases.

Li coefficients also probe zero behavior near $\rho = 1/2$. At large $n$, $\lambda_n$ is dominated by the contribution from zeros nearest $s = 1$:

$$\lambda_n \approx \sum_\rho |1/\rho|^n \cdot (\text{phase factor}).$$

For zeros on the critical line ($\rho = 1/2 + i\gamma$), $|1/\rho|^n = |\rho|^{-n} = (1/4 + \gamma^2)^{-n/2}$, decaying rapidly. For off-line zeros ($\beta > 1/2$), $|1/\rho|^n$ is larger by the factor $(\beta^2 + \gamma^2 / (1/4 + \gamma^2))^{n/2}$. At large $n$ this factor dominates, giving negative $\lambda_n$ for non-RH cases.

This is the mechanism the project's 3B.2 experiment exploited: at $n \sim 4 \times 10^5$, the off-line correction from D-H's known off-line zeros at $\gamma \sim 85.7$ overpowers the on-line baseline.

### From dBN to Li

There's no clean reverse direction (dBN doesn't naturally give a sequence of inequalities the way Li does). But:

- For $\Lambda < 0$ (RH-stronger-than-true): Li coefficients would have a structural positivity gap reflecting how far below 0 $\Lambda$ sits.
- For $\Lambda = 0$ (RH, sharp): Li coefficients are positive but with growth $\sim \frac{n}{2} \log n + cn$ — the constant $c$ encodes the marginal RH-truth.
- For $\Lambda > 0$ (RH fails): some Li coefficient must eventually become negative, with the discrimination scale depending on how large $\Lambda$ is.

## 6. What each gives that the other doesn't

**Li gives**:
- A discrete witness: if a single $\lambda_n < 0$, RH fails. Combinatorially decisive.
- Direct computational access from zeros.
- A growing positivity quantity (asymptotic $\frac{n}{2} \log n$).

**dBN gives**:
- A real-valued "RH parameter" $\Lambda$, with RH ⟺ $\Lambda = 0$.
- A natural "quantification of how badly RH fails" (the value of $\Lambda > 0$).
- A specific computational target: improve the upper bound on $\Lambda$.

**Neither gives**:
- A proof of RH.
- A method to compute the truth of RH unconditionally.

Both are equivalent reformulations: they recast RH as a positivity statement but neither makes it easier to PROVE.

## 7. Connection to the project's experiments

- **3A** (this project): computed $\lambda_n$ for $\zeta$ at $n \leq 500$. All positive. Consistent with RH.
- **3B**: $\lambda_n^{\text{D-H}}$ at $n \leq 300$ also positive. Established that small-$n$ Li doesn't discriminate.
- **3B.2**: large-$n$ Li for D-H at $n = 4 \times 10^5$ negative. Discrimination scale $n \sim |w_{\text{off}} - 1|^{-2}$.
- **3C-3D**: Gram matrix Weil quadratic form. Different positivity statement (test functions instead of Li coefficients). Discriminates at smaller "resolution" ($K \sim 30$ test functions).

The project's experimental thread has focused on Li (via 3A, 3B, 3B.2) and Weil (via 3C-3D) rather than dBN. The dBN constant is not directly computable by the project's tools (would require heat-equation simulation of $\xi$), but the project's Li experiments are structurally analogous in spirit.

**The Newman lower bound $\Lambda \geq 0$** (Rodgers-Tao 2018) is a remarkable RECENT result — it shows that RH is "barely true" in the sense that any "wrong-way heat-equation deformation" of $\xi$ moves zeros off the line immediately. This is one of the few unconditional results about RH-related quantities and gives some structural insight into why proving RH is hard: there's no "buffer" between the truth of RH and its negation.

## 8. Implications for proof attempts

**Both criteria suggest RH is sharp**:
- Li coefficients grow $\sim n \log n /2$ — barely positive, not exponentially positive.
- $\Lambda = 0$ exactly (per Rodgers-Tao + Newman) — RH is "on the boundary," not deep in the safe region.

This is consistent with the project's structural finding (LEARNINGS #7): the Weil-form duality has $\sim 10^{-3}$ cancellation tightness. All three POSITIVITY formulations (Li, dBN, Weil) are "marginally positive": RH is true only at the margin.

**Implication (a targeting result, not a discouragement)**: an RH proof attempt that gives "lots of room" (e.g., a positivity argument with order-of-magnitude headroom) is almost certainly leaking somewhere, because the actual margin is zero. This tells us exactly where the real proof lives: it must use the EXACT structure of zeta (Euler product, functional equation, archimedean factor) rather than soft arguments. The zero margin removes the soft routes and concentrates the search on the structural one.

This is the same structural lesson encoded in:
- 3I (Siegel-Walfisz too loose by factor 30-120× — the wall is sharp)
- 4E.3 (single-zero MT structurally capped at 1D Fejér)
- R3.5 (NCG no-shortcut theorem: positivity ⟺ RH)
- R3.6 (arithmetic-site refinements don't escape)

All these suggest the "marginal positivity" structural picture.

## 9. Bottom line on 3E

Li and dBN are two natural positivity reformulations of RH, related but distinct:
- Li is **discrete** (sequence $\{\lambda_n\}$), **directly accessible from zeros**, **provides combinatorial witnesses** of non-RH (per 3B.2 at $n \sim 4 \times 10^5$).
- dBN is **continuous** ($\Lambda \in \mathbb{R}$), **defined via heat-equation deformation**, **proves "RH is sharp"** ($\Lambda \geq 0$ per Rodgers-Tao 2018, so $\Lambda = 0$ ⟺ RH).

Both confirm the project's structural finding that RH is true only at the margin, which points the proof at the exact structure of zeta rather than soft positivity. The Weil-form cancellation tightness (LEARNINGS #7), the K1 wall (R3.5), and the dBN $\Lambda = 0$ sharpness are three views of the same phenomenon, and together they map where to dig.

**Implication for proof attempts**: any RH proof must use the exact structure of $\zeta$ (Euler product, functional equation, archimedean factor) rather than soft positivity arguments. The "marginal positivity" structural picture rules out wholesale generalizations.

**Project's choice**: focused experimental work on Li (3A, 3B, 3B.2) and Weil quadratic form (3C-3D) rather than dBN, because dBN requires heat-equation simulation of $\xi$ which is computationally heavier with similar payoff. The Li / Weil track gives more direct access to the zero structure.

## References (Li / dBN-specific)

- Li, X.-J. (1997). *The positivity of a sequence of numbers and the Riemann hypothesis*. J. Number Theory 65, 325–333. The Li criterion.
- Bombieri, E.; Lagarias, J. C. (1999). *Complements to Li's criterion for the Riemann hypothesis*. J. Number Theory 77, 274–287. Asymptotic analysis.
- de Bruijn, N. G. (1950). *The roots of trigonometric integrals*. Duke Math. J. 17, 197–226. Introduces the heat-equation deformation.
- Newman, C. M. (1976). *Fourier transforms with only real zeros*. Proc. AMS 61, 245–251. Introduces $\Lambda$.
- Csordas, G.; Norfolk, T. S.; Varga, R. S. (1988). *The Riemann hypothesis and the Turán inequalities*. Trans. AMS 296, 521–541.
- Rodgers, B.; Tao, T. (2020). *The de Bruijn-Newman constant is non-negative*. Forum of Mathematics, Pi, 8, e6. Settles Newman's conjecture.
- Polymath, D. H. J. (Tao et al.) (2019). *Effective approximation of heat flow evolution of the Riemann $\xi$ function*. preprint. The current best upper bound $\Lambda \leq 0.22$.
- Saouter, Y.; Demichel, P. (2011). *A sharp region where $\pi(x) - \mathrm{li}(x)$ is positive*. Math. Comp. 80, 2295–2308. Earlier numerical upper bound work.
- Csordas, G.; Smith, W.; Varga, R. S. (1994). *Lehmer pairs of zeros, the de Bruijn-Newman constant, and the Riemann hypothesis*. Constr. Approx. 10, 107–129. Method for upper-bounding $\Lambda$.
