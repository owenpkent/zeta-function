# 2KK: a finite WCart / diffracted-Hodge model of M4 organ (a), and the Petrov non-semisimplicity crux

> Companion for [`e2kk_wcart_finite_model.py`](e2kk_wcart_finite_model.py). Builds a small finite truncation of milestone M4 organ (a) (the cup pairing on the Bhatt-Lurie Cartier-Witt / diffracted-Hodge substrate of [Direction 8B](../../docs/03_research/research_directions/08B_bhatt_lurie_wcart_signature.md)) and runs it through the two mandatory gates: the D-H discipline and the Petrov non-semisimplicity obstruction. Run: `python -m experiments.arithmetic_geometric.e2kk_wcart_finite_model`.

## Why this experiment exists

[Direction 8B](../../docs/03_research/research_directions/08B_bhatt_lurie_wcart_signature.md) proposes that the Hodge-index signature whose positivity is RH is carried by absolute prismatic cohomology on the Cartier-Witt stack $\mathrm{WCart}$, with the cyclotomic **Sen operator** $\Theta$ acting on the $n$-th conjugate-graded piece of the diffracted Hodge complex by multiplication by $-n$ (Bhatt-Lurie, *Absolute prismatic cohomology*, Example 3.5.6 / 3.5.8). Milestone **M4 organ (a)** is the construction of the cup pairing on this substrate:

$$ \smile : H^1 \times H^1 \longrightarrow H^2 = \mathbb{C}(-1), \qquad \Theta(\langle x,y\rangle) = \langle \Theta x, y\rangle + \langle x, \Theta y\rangle \quad(\Theta\text{ a derivation, BL Remark 3.5.5}), $$

together with a trial Hodge-star polarization $Q(x,y) = \langle x, \ast y\rangle$ whose signature one reads off.

The prior WCart probes ([2PR.1](e2pr_sen_archimedean.py), 2DD) located zeta's two trace-halves on WCart as regularized determinants but explicitly reported "no intersection form / Hodge index / polarization" (the M3 signature gap). **2KK is the first probe that actually forms the cup pairing as a matrix and reads its signature**, and the first to confront the one published theorem that bears directly on this construction:

> **Petrov** (Annals, [arXiv:2302.11389](https://arxiv.org/abs/2302.11389)): the Sen operator on the diffracted Hodge complex is **not semisimple**. It carries genuine Jordan blocks; the conjugate filtration does not split.

The crux of M4 organ (a) is therefore: **can an intrinsic (basis-free) positive cup polarization survive on a non-semisimple Sen module?**

## What the model is

Finite truncation, graded weights $n = 0, 1, \dots, K$ (default $K=8$), so $H^1$ is the $(K{+}1)$-dimensional graded space and $\Theta$ is a $(K{+}1)\times(K{+}1)$ matrix.

The cup form is built by **solving the derivation condition as a linear equation**. With $H^2 = \mathbb{C}(-1)$ on which $\Theta$ acts by the Tate weight $w = -1$, a bilinear cup form with matrix $B$ ($\langle x, y\rangle = x^\top B y$) is $\Theta$-compatible iff

$$ \Theta^\top B + B\,\Theta = w\,B = -B \qquad\text{(a Sylvester / Lie equation).} $$

We solve this in the **antisymmetric** subspace (alternating cup product on $H^1$) by taking the null space of the vectorized operator $\mathrm{kron}(I,\Theta^\top) + \mathrm{kron}(\Theta^\top, I) + I$. The trial polarization is $Q = B^{H}\,\ast$ with the Hodge-star modeled as the Weil-operator phase $\ast = i^{\,w}$ along the weight grading, then Hermitized.

## Gate 1: the D-H discipline (clean K2 non-formation)

The cup target $H^2 = \mathbb{C}(-1)$ **is** the Frobenius Tate twist (the $(1,p)$ bidegree). The twist exists iff the L-function has an Euler product, i.e. a Frobenius correspondence $F$ at each finite place. The constructor carries an explicit guard: no Euler product $\Rightarrow$ no $F$ $\Rightarrow$ no $\mathbb{C}(-1)$ $\Rightarrow$ the pairing target does not exist $\Rightarrow$ **the model does not form**.

| target | Euler product | model forms? | semisimple-$\Theta$ signature $(+,-,0)$ |
|---|---|---|---|
| $\zeta$ | yes | **yes** | $(1, 1, 7)$ |
| Davenport-Heilbronn | **no** | **NO (constructor raises)** | n/a |

**Verdict: GATE 1 PASS (as a design statement, NOT as a demonstrated structural non-formation).** D-H carries no Euler product, so the Frobenius Tate twist $\mathbb{C}(-1)$ that is the cup target genuinely does not exist for it; that part is mathematically real and is why Architecture 2 sits outside the D-H discipline by design.

> **ADVERSARY correction (2026-06-04).** The *code's* enforcement of Gate 1 is **not** a structural non-formation. The guard `has_frobenius_twist(L)` is a **string match on `L.name`** (`if "davenport" in name: return False`); it reads no Euler-product data off the object. Renaming the same D-H object to `mystery_L` makes the guard pass and the model build identically (verified). More to the point, `cup_pairing_matrix` and `hodge_star_polarization` take **only the `Theta` matrix**, which is built from `K` alone; the L-function object never enters the matrix construction, so zeta and D-H would produce the *identical* cup form and signature `(1,1,7)` if both reached the solver. The non-formation is therefore a **hand-imposed deletion**, not a property the construction discovers. This is the honest K2 status: D-H is excluded by fiat (correctly motivated, but not by the model fielding it). Treat Gate 1 as "Arch-2-by-design, outside D-H," not as "the probe fires for zeta and structurally fails to form for D-H."

## Gate 2: the Petrov non-semisimplicity crux

### The cup form is essentially unique and lives on one weight pair

Solving the derivation equation reveals the antisymmetric solution space is **1-dimensional** (verified at $K=4$ and $K=8$: null dimension 2, antisymmetric rank 1). For diagonal $\Theta = \mathrm{diag}(-n)$ the equation reads $(n_i + n_j - 1)B_{ij} = 0$, so $B_{ij}$ is nonzero only when $n_i + n_j = 1$, i.e. the pair $\{0, 1\}$. **The compatible alternating cup form is a single hyperbolic $2\times2$ block pairing the weight-0 and weight-1 pieces**; every other weight is unpaired (the $K{-}1$ zero eigenvalues). This is geometrically sensible: weight-0 and weight-1 are exactly the pieces that cup to $\mathbb{C}(-1)$.

### Signature per $\Theta$ construction

We build $\Theta$ four ways and read the trial polarization signature each time:

| $\Theta$ construction | cup form? | signature $(+,-,0)$ | verdict |
|---|---|---|---|
| (i) semisimple $\mathrm{diag}(-n)$ | yes (exact, residual 0) | $(1,1,7)$ | INDEFINITE |
| (ii-a) "Jordan nilpotent on $(-1,-1)$" | yes (exact) BUT see note | $(1,1,7)$ | INDEFINITE |
| (ii-b) "non-split extension $(-1,-2)$" | yes (exact) BUT see note | $(1,1,7)$ | INDEFINITE |
| (iii) Jordan + off-line eigenvalue | **NO (residual 1.82)** | $(1,1,7)$ of a non-cup-form | INDEFINITE (invalid test) |

> **ADVERSARY correction (2026-06-04): the Petrov crux is NOT actually exercised.** Neither "Jordan" construction is non-semisimple, and the off-line probe does not produce a cup form.
>
> - **(ii-a) is a relabeled diagonal, not a Jordan block.** `theta_jordan(K, ((1,1),))` runs `T[a,a]=-a; T[b,b]=-b; T[a,b]=nilp` with `a=b=1`, so the three writes collapse and `nilp=1.0` lands on the **diagonal** $T[1,1]$. The result is $\mathrm{diag}(0,+1,-2,-3,\dots)$: all eigenvalues distinct, fully **semisimple**, no off-diagonal coupling. (Its cup support even moves to $(1,2)$ because weight $+1$ is now present.) The "true non-diagonalizable Jordan cell" claimed here does not exist in the code.
> - **(ii-b) is semisimple too.** The block $\begin{psmallmatrix}-1&1\\0&-2\end{psmallmatrix}$ has **distinct** eigenvalues $-1,-2$, hence is diagonalizable. A genuine Petrov-type defective block needs **equal** eigenvalues, e.g. $\begin{psmallmatrix}-1&1\\0&-1\end{psmallmatrix}$; that case is **never built**. So "non-semisimplicity does not change the verdict" is not demonstrated, because no non-semisimple $\Theta$ was tested.
> - **A genuinely defective $\Theta$ on the load-bearing pair kills the cup form.** Building a true nilpotent block with equal eigenvalues on weights $(0,0)$ yields **no exact cup form** ($B=0$); the derivation equation $w_i+w_j=-1$ then has no admissible integer-weight solution. The honest Petrov finding is thus the opposite of "definiteness survives": genuine non-semisimplicity tends to **destroy the cup target**, which the experiment never reaches because it mislabels semisimple operators as Jordan.

**Does non-semisimplicity change the verdict?** The experiment cannot answer this, because it never tests a non-semisimple $\Theta$ (see correction above). What *is* robustly true is the linear-algebra fact below, which holds for the genuine semisimple cup forms and forces the demotion independently of Petrov.

**The load-bearing fact (robust):** the trial Hodge-star polarization of an *alternating* form on its rank-2 support $(0,1)$ is **always hyperbolic** (signature $(1,1)$), for every nonzero diagonal Hodge-star phase and for all $K$ (verified $K=2\dots32$; support is always the single $(0,1)$ block). This hyperbolicity is what demotes the trial Hodge-star, and it is forced by the truncation collapsing all primitive cohomology onto one weight pair, *before* any non-semisimplicity question arises.

### Polarity check (the AHK pattern, LEARNINGS #48)

The off-line probe (iii) injects a complex eigenvalue tied to the first Davenport-Heilbronn off-line zero $\rho \approx 0.8085 + 85.699\,i$, encoded as a shift $(\beta - \tfrac12) + i\,(\gamma/100)$ on the load-bearing $(0,1)$ block (chosen on purpose so the off-line value lands **on** the cup-form support; injecting it elsewhere would be an unfair test).

| comparison | on-line (semisimple, exact cup form) | off-line ("Jordan" on $(0,1)$) |
|---|---|---|
| derivation residual | $0$ (exact) | **$1.82$ (NOT a cup form)** |
| signature $(+,-,0)$ | $(1,1,7)$ | $(1,1,7)$ of a non-compatible matrix |
| extreme $\lvert$eig$\rvert$ | $0.5000$ | $0.6752$ |

> **ADVERSARY correction (2026-06-04): the off-line "polarity test" is invalid as run.** The off-line $\Theta$ shifts the load-bearing weights by $(\beta-\tfrac12)+i\gamma/100$ on *both* diagonal slots, so $T_{00}+T_{11} = -1 + 2(\beta-\tfrac12) = -0.384 \neq -1$. The derivation equation $\Theta^\top B + B\Theta = -B$ then has **zero exact null vectors** (smallest singular value $0.296 \gg$ tolerance), so `cup_pairing_matrix` silently falls through to its approximate "smallest-SV direction" branch and returns a $B$ with derivation residual $\mathbf{1.82}$. That object is **not a $\Theta$-compatible cup form**; its signature $(1,1,7)$ is meaningless as a polarity readout. The honest statement is the opposite of "the signature does not move": **injecting an off-line eigenvalue on the load-bearing pair destroys the exact cup form entirely** (the compatible-form null space empties). One can argue that *is* a response to off-line-ness, but it is hidden by the silent approximate fallback, and the "$0.500 \to 0.675$ magnitude move" is an artifact of a garbage matrix, not a detector signal.

**Verdict: WRONG POLARITY (conclusion stands, but for a cleaner reason than the off-line probe).** The demotion does **not** rest on the (broken) off-line comparison. It rests on the robust linear-algebra fact: the trial Hodge-star polarization of the *exact* alternating cup form is unconditionally hyperbolic $(1,1)$ on its rank-2 support, for every Hodge-star phase and every $K$. An unconditionally-signed form cannot be definite-iff-RH, so its signature is not the RH signature. This is the AHK convex-Hodge pattern (LEARNINGS #48): the Hodge-Riemann package gives a signature that is fixed for all admissible inputs, so it can never flip to flag an off-line zero. The Weil form has the *right* polarity (PSD $\to$ indefinite when a zero leaves the line); this trial cup form does not. The construction is **demoted as an RH detector**. The off-line probe should be repaired (inject the off-line shift in a way that preserves the derivation constraint, or report the residual and read the null-space collapse as the signal) before any "signature does not move" language is used.

## What this shows and does not show

**Shows (positive structural content):**
- M4 organ (a)'s cup pairing $H^1 \times H^1 \to \mathbb{C}(-1)$ with $\Theta$ a derivation can be written down and **solved** as a Sylvester/Lie equation on a finite truncation, for semisimple $\Theta$ (exact, residual 0).
- The $\Theta$-compatible alternating cup form is **essentially unique** (1-dimensional antisymmetric solution space) and is canonically supported on the single $(\text{weight-}0, \text{weight-}1)$ pair that cups to $\mathbb{C}(-1)$, for all $K$ tested ($2\dots32$).

**Does not show (honest negatives, this is exploratory):**
- No RH-relevant discrimination. The trial Hodge-star polarization of the *exact* cup form is **unconditionally hyperbolic** $(1,1)$ on its rank-2 support (every Hodge-star phase, every $K$), so it has the wrong polarity for an RH detector (the AHK/#48 verdict). This **demotes the trial Hodge-star on WCart** as a candidate signature. This is the solid conclusion.
- **The Petrov non-semisimplicity crux was NOT actually tested** (ADVERSARY correction): both "Jordan" $\Theta$'s in the code are semisimple (one is a relabeled diagonal, the other a $2\times2$ with distinct eigenvalues). A genuine defective block on the load-bearing pair instead *destroys* the cup form. So the experiment's claim that "definiteness survives the Jordan block" is not supported; the question Petrov poses remains open here.
- **The off-line polarity probe is invalid as run** (ADVERSARY correction): the off-line $\Theta$ admits no exact cup form (residual 1.82), so the "signature does not move" comparison is between a real cup form and a non-cup-form artifact. The wrong-polarity conclusion above does not depend on it and stands on the unconditional-hyperbolicity fact alone.
- **Gate 1 (D-H) is a string guard on `L.name`, not a structural non-formation** (ADVERSARY correction): the cup form is built from $\Theta(K)$ alone and never sees the L-function, so D-H and zeta would coincide if both reached the solver. D-H is excluded by fiat (Arch-2-by-design), not discovered to be un-buildable by the model.
- It inherits the marginal-positivity stealth window (no claim past the cutoff $x \sim 3$).

**The coordinate this adds.** Direction 8B's open task (b) was "prove $\Theta$ forces the alternating trace to be positive-definite on primitive cohomology." 2KK shows that the **naive realization of (b) via a Hodge-star on the alternating cup form gives the wrong polarity**: an alternating $\smile$ valued in a 1-dimensional $\mathbb{C}(-1)$ produces a hyperbolic pairing whose signature is rigid. A genuine RH-relevant polarization must therefore come from a **higher-rank** primitive cohomology (the cup form cannot live on a single weight pair) or from a **non-Hodge-star** positivity (the Frobenius-weighted trace, not the Weil-operator phase). The cheap Hodge-star route on the truncated diffracted-Hodge complex is closed; like AHK on the Connes-Consani square (#40/#48), WCart supplies the trace but the signature needs a genuinely new theorem, not a Hodge-star applied to the obvious cup form.

## Verification targets (for VERIFIER)

1. **Cup-form uniqueness.** For $\Theta = \mathrm{diag}(0,-1,\dots,-K)$, the space of antisymmetric $B$ with $\Theta^\top B + B\Theta = -B$ is 1-dimensional and supported on the $(0,1)$ entry. (Formalize the Sylvester equation $(n_i + n_j - 1)B_{ij} = 0$ over the weight grading.)
2. **Hyperbolicity is unconditional.** Any Hermitian form $B^H \ast$ built from a nonzero antisymmetric $2\times2$ $B$ and a diagonal phase $\ast$ has signature $(1,1)$. (Pure linear algebra; the polarity-blindness lemma.)
3. **Gate-1 is a mathematical statement, not a code property.** The cup target $\mathbb{C}(-1)$ (Tate twist) is genuinely absent for an $L$ without an Euler product, AS MATHEMATICS. But the *code* does not verify this: `has_frobenius_twist` is a string match on `L.name`, and the cup form is built from $\Theta(K)$ alone (the L-function never enters). Do not formalize "the constructor's precondition fails for D-H" as if it were structural; it is a hand-coded exclusion. A faithful version would build $\mathbb{C}(-1)$ from actual Euler-product / Frobenius data and let it fail to exist for D-H.

## Adversarial test cases (for ADVERSARY) -- RESOLVED 2026-06-04

ADVERSARY ran all four plus three new ones. Results:

1. **Off-line slot fairness.** PARTIALLY MOOT. The off-line $\Theta$ on $(0,1)$ admits **no exact cup form** (derivation residual 1.82), so the "signature does not move" framing was never a valid test. Repair needed before this case means anything.
2. **Higher truncation $K$.** PASS. Signature stays $(1,1,K{-}1)$ for $K=2,3,4,8,16,32$; support is always the single $(0,1)$ block. Uniqueness/hyperbolicity is robust.
3. **Alternate Hodge-star phase.** PASS. $i^w$, $i^{K-w}$, $\mathrm{sign}(w)$, and random phases all give $(1,1)$. (The $\ast=\mathrm{id}$ case gives $(0,0,9)$ because $B^H\cdot I$ is anti-Hermitian, a degenerate artifact, not a definite counterexample.) The hyperbolic verdict is invariant.
4. **Symmetric (non-alternating) cup.** PASS. The symmetric null vectors are also supported on $(0,1)$ and also give $(1,1,7)$. The obstruction is rank-2-on-one-weight-pair, not the alternating constraint.
5. **(NEW) String-guard attack on Gate 1.** FAIL. Renaming the D-H object to `mystery_L` makes the guard pass and the model build. Gate 1 is not structural.
6. **(NEW) Are the "Jordan" $\Theta$'s actually non-semisimple?** FAIL. `nil(1,1)` is a relabeled diagonal (distinct eigenvalues); `ext(1,2)` has distinct eigenvalues $-1,-2$ (diagonalizable). No defective block is tested.
7. **(NEW) Genuine defective block.** A true nilpotent block with equal eigenvalues on the load-bearing pair returns **no cup form** ($B=0$); the cup target is destroyed, not preserved.

## Self-assessment against the 17-constraint framework

- **K1 (circularity):** passes. No zero location is used; $\Theta$, the cup form, and the polarization are built from the weight grading alone. The construction does not "prove RH easily" (it gives the wrong polarity), which is the expected K1-safe behavior.
- **K2 (D-H discipline):** passes **only as a design statement**, NOT as a demonstrated structural non-formation (ADVERSARY correction). The code's Gate 1 is a string match on `L.name`; the cup form never sees the L-function. D-H is excluded by fiat. Honest status: Arch-2-by-design, outside the D-H discipline.
- **K3 (matches known structure):** the Sen-weight action $-n$, the Tate twist $\mathbb{C}(-1)$, and the derivation condition are the Bhatt-Lurie objects, and the cup-form support on $\{0,1\}$ is consistent. BUT the one published obstruction that bears on this object, Petrov's non-semisimplicity, is **not actually instantiated** (both "Jordan" $\Theta$'s are semisimple). So K3 is only partially exercised; the Petrov-faithful case remains untested here.
- **K4 (right polarity / signature flips with RH):** **FAILS** (the trial Hodge-star polarization of the exact cup form is unconditionally hyperbolic $(1,1)$ for every phase and every $K$; the signature is rigid). This is the load-bearing open constraint and the reason the construction is a demoted candidate. NOTE: the original off-line "polarity test" that purported to show this was invalid (no exact cup form for off-line $\Theta$); the K4 failure is established instead by the unconditional-hyperbolicity fact, which is solid.
