# E1W: the literal Burnol bilinear extension vs the negative-square ansatz

> BUILDER dossier, 2026-08-09. Executes PHASE_STATE next-step 1, third clause: "verify the
> negative-square kernel ansatz against Burnol's LITERAL bilinear extension." The ansatz under audit
> is LEARNINGS #168(iii) ([`la_negative_square_check.md`](../../docs/03_research/reading_notes/la_negative_square_check.md)):
> at candidate tier, the pole pair $s = 0, 1$ of the zeta-loaded Sonine space $L_a$ was computed to
> cost exactly ONE negative square ($\kappa = 1$) via a mirror-pole mechanism giving a 2x2 evaluator
> block $[[0, -\rho], [-\bar\rho, 0]]$ of signature $(1,1)$. Its recorded honest limit, closed here:
> "this used a LOCAL ADDITIVE KERNEL ANSATZ, not Burnol's literal bilinear extension."
>
> **STATUS: the pre-registered outcome CORRECTED fired.** The literal extension from $K_a$ to $L_a$
> has signature $(2,0)$: ZERO negative squares, $\kappa = 0$, at every $a$ tested and every
> discretization, with two independent computational routes agreeing to worst-case relative
> discrepancy $3.54 \times 10^{-36}$. The mirror-pole telescoping (off-diagonal-only block) does NOT
> survive the literal form: the literal diagonal is $N = \|Y_1^a\|^2 > 0$, which the ansatz predicted
> to vanish. The exact step where the ansatz diverged is named in Section 5. #168(iii) DOWNGRADES
> from "REALIZABLE-CANDIDATE $\kappa = 1$" to "CORRECTED AT SOURCE: $\kappa = 0$"; the $(1,1)$ block
> survives only as a fact about an auxiliary $\mathcal{F}_+$-twisted pairing that is not the space's
> inner product (Section 6). Tests: 24/24 full, 18/18 quick
> ([`e1w_burnol_bilinear.py`](e1w_burnol_bilinear.py); record [`e1w_burnol_bilinear.npz`](e1w_burnol_bilinear.npz)).
>
> Method discipline: every load-bearing quote below is [FETCHED] this session from the ar5iv full
> text of arXiv:math/0203120 (converted locally with math alt-text preserved; conversion bug for
> `<` inside formulas found and fixed before extraction). Claims tagged as this note's own
> derivation are so flagged. No em dashes.

## 1. Source correction first

The tasking described math/0203120 as "Des équations de Dirac et de Sommerfeld" (French). That is a
mislabel: **arXiv math/0203120 is Burnol, "Two complete and minimal systems associated with the
zeros of the Riemann zeta function," J. Théor. Nombres Bordeaux 16 (2004) 65-94, in English**
(fetched abstract page + full text this session). The repo's own citations of Prop. 2.2 and
Prop. 4.5 to this arXiv number are correct; only the title/language gloss in the tasking was wrong.
"Des équations de Dirac et de Sommerfeld" is a different Burnol paper and was not needed.

## 2. What Burnol literally defines (verbatim, with equation numbers)

**The ambient space and transform** [FETCHED, Note 2 of Section 1]:

> "In all the following we deal only with even functions on the real line. The square integrable
> among them will be assigned squared-norm $\int_0^\infty |f(t)|^2\,dt$. We let
> $K = L^2(0, \infty; dt)$, and we let $\mathcal{F}_+$ be the cosine transform on $K$:
> $\mathcal{F}_+(f)(u) = 2\int_0^\infty \cos(2\pi t u) f(t)\,dt$."

**The spaces** [FETCHED, Section 2]:

> "So we are led to associate to each $a > 0$ the **sub-Hilbert space $L_a$ of $K$** consisting of
> functions which are constant in $(0,a)$ and with their cosine transform again constant in
> $(0,a)$." ... "The Sonine space $K_a$ consists of the functions in $K$ which are vanishing
> identically, as well as their Fourier (cosine) transforms, in $(0,a)$."

**Theorem 2.1 (De Branges)** [FETCHED]:

> "Let $0 < a < \infty$. Let $f(t)$ belong to $K_a$. Then its completed right Mellin transform
> $M(f)(s) = \pi^{-s/2}\Gamma(\frac{s}{2})\widehat{f}(s)$ is an entire function. The evaluations at
> complex numbers $w \in \mathbb{C}$ are continuous linear forms on $K_a$."

with $\widehat{f}(s) = \int_0^\infty f(t) t^{-s}\,dt$ the right Mellin transform (Section 1), and,
directly under Theorem 2.1: "It appears to be useful not to focus exclusively on entire functions,
and to **allow poles**, perhaps only finitely many."

**Proposition 2.2** [FETCHED]:

> "Let $f(t)$ belong to $L_a$. Then its completed right Mellin transform
> $M(f)(s) = \pi^{-s/2}\Gamma(\frac{s}{2})\widehat{f}(s)$ is a meromorphic function in the entire
> complex plane, with at most poles at $0$ and at $1$. The evaluations $f \mapsto M(f)^{(k)}(w)$ for
> $w \neq 0$, $w \neq 1$, or $f \mapsto \mathrm{Res}_{s=0}(M(f))$, $f \mapsto \mathrm{Res}_{s=1}(M(f))$
> are continuous linear forms on $L_a$. One has the functional equations
> $M(\mathcal{F}_+(f))(s) = M(f)(1-s)$."

**The evaluators and the bilinear form** [FETCHED, unnumbered display directly after Prop. 2.2]:

> "We will write $Y^a_{w,k}$ for the vector in $L_a$ with
> $$\forall f \in L_a \quad \int_0^\infty f(t)\, Y^a_{w,k}(t)\,dt = M(f)^{(k)}(w).$$
> This is for $w \neq 0, 1$. For $w = 0$ we have $Y^a_0$ which computes the residue at $0$, and
> similarly $Y^a_1$ for the residue at $1$. We are using the bilinear forms
> $[f,g] = \int_0^\infty f(t) g(t)\,dt$ and not the Hermitian scalar product
> $(f,g) = \int_0^\infty f(t)\overline{g(t)}\,dt$ in order to ensure that the dependency of
> $Y^a_{w,k}$ with respect to $w$ is analytic and not anti-analytic."

**The functional-equation multiplier** [FETCHED, eqs (7)-(8)]:
$\widehat{\mathcal{F}_+(f)}(s) = \chi(s)\widehat{f}(1-s)$ with
$\chi(s) = \pi^{s-1/2}\Gamma(\frac{1-s}{2})/\Gamma(\frac{s}{2})$, "hence also
$\chi(s) = \zeta(s)/\zeta(1-s)$".

**Proposition 4.5, with its second proof** [FETCHED, the structural key of this whole computation]:

> "One has $\dim(L_a/K_a) = 2$." ... "For the second proof we go back to the argument of [6] which
> identifies the perpendicular complement to $K_a$ in $L^2(0,\infty;dt)$ to be the closed space
> $L^2(0,a) + \mathcal{F}_+(L^2(0,a))$. It is clear that $L_a$ is the perpendicular complement to
> the (two dimensions) smaller space
> $(L^2(0,a) \cap \mathbf{1}_{0<t<a}^\perp) + \mathcal{F}_+(L^2(0,a) \cap \mathbf{1}_{0<t<a}^\perp)$
> and this proves 4.5."

**Proposition 4.1** [FETCHED, the $s$-picture]: $\widehat{L_a}$ consists of the $F(s)$ on the
critical line in $\frac{s}{s-1}A^s\mathbb{H}^2$ with $\chi(s)F(1-s)$ also in
$\frac{s}{s-1}A^s\mathbb{H}^2$; such $F$ is "meromorphic in the entire complex plane with at most a
pole at $s = 1$" (the pole at $0$ of $M(f)$ coming from the $\Gamma(\frac{s}{2})$ factor).

**The co-Poisson formula** [FETCHED, eq (9), used as the end-to-end convention anchor]:
$$\mathcal{F}_+\Big(\sum_{m\geq 1}\tfrac{g(m/t)}{|t|} - \widehat{g}(0)\Big) = \sum_{n\geq 1}\tfrac{g(t/n)}{n} - \widehat{g}(1).$$

**The decisive reading.** $L_a$ is, verbatim, a **sub-Hilbert space of $K = L^2(0,\infty;dt)$**.
Burnol defines no indefinite inner product anywhere. The bilinear form $[f,g]$ is an analyticity
device on top of the same Hilbert space (his stated reason, quoted above), and for the residue
evaluators, which turn out to be real-valued functions (Section 4), the bilinear pairing and the
Hermitian scalar product literally coincide. So "the literal bilinear extension from $K_a$ to
$L_a$" is a two-dimensional enlargement INSIDE a Hilbert space, and the only question is what its
2x2 block is and how it sits against the ansatz's kernel model. That is what the computation
measures.

## 3. The residue dictionary (this note's derivation, verified numerically)

For $f \in L_a$ write $f(0^+)$ for its constant value on $(0,a)$. Splitting
$\widehat{f}(s) = f(0^+)\frac{a^{1-s}}{1-s} + \int_a^\infty f\,t^{-s}dt$ (the second term analytic
for $\mathrm{Re}(s) > 1/2$) and using $\pi^{-1/2}\Gamma(\frac12) = 1$ at $s=1$, then transporting
through the functional equation $M(\mathcal{F}_+ f)(s) = M(f)(1-s)$ for the pole at $0$:

$$\mathrm{Res}_{s=1} M(f) = -f(0^+), \qquad \mathrm{Res}_{s=0} M(f) = +(\mathcal{F}_+ f)(0^+).$$

Both functionals are means over $(0,a)$ ($f(0^+) = \frac1a\int_0^a f$), so the evaluators are
orthogonal projections onto $L_a$ of explicit elementary functions:

$$Y_1^a = P_{L_a}(u_1), \quad u_1 = -\tfrac1a \mathbf{1}_{(0,a)}; \qquad
Y_0^a = P_{L_a}(u_0), \quad u_0 = \tfrac1a \mathcal{F}_+\mathbf{1}_{(0,a)} = \tfrac{\sin(2\pi a t)}{\pi a t}.$$

Both are REAL functions ($L_a$, $L_a^\perp$, and the $u_i$ are conjugation-stable). Moreover, since
$\mathcal{F}_+ u_1 = -u_0$ and $\mathcal{F}_+$ commutes with $P_{L_a}$ (both $L_a$ and $L_a^\perp$
are $\mathcal{F}_+$-stable, by Prop. 4.5's second proof):

$$\boxed{\;Y_0^a = -\mathcal{F}_+(Y_1^a)\;}$$

This closed-form relation between the two residue evaluators is NEW relative to #168, whose dossier
recorded exactly this item as "not extracted... the single largest concrete gap." It is an
immediate consequence of $\mathrm{Res}_{s=0}M(f) = -\mathrm{Res}_{s=1}M(\mathcal{F}_+f)$ (change of
variable $s \mapsto 1-s$ flips the residue sign) and forces $\|Y_0\| = \|Y_1\|$.

## 4. The literal extension block, in all three of its guises

Let $N := \|Y_1^a\|^2$ and $\beta := (Y_0^a, Y_1^a)$ (real). The 2x2 object the ansatz modeled is,
under the literal construction, the SAME real symmetric matrix in three readings:

1. **The bilinear evaluator block** $B_{pq} = [Y_p^a, Y_q^a]$, $p,q \in \{0,1\}$: by Prop. 2.2,
   $[f, Y_1] = \mathrm{Res}_1 M(f)$, so $B_{11} = \mathrm{Res}_1 M(Y_1) = -Y_1(0^+)$, etc. Since
   the $Y$'s are real, $[Y_p, Y_q] = (Y_p, Y_q)$, giving $B = \begin{pmatrix} N & \beta \\ \beta & N \end{pmatrix}$
   (diagonal equality $B_{00} = B_{11}$ forced by $Y_0 = -\mathcal{F}_+Y_1$ and unitarity).
2. **The Hermitian extension Gram.** By Prop. 4.5's proof, $K_a = \{f \in L_a: [f,Y_0] = [f,Y_1] = 0\}$,
   so the orthogonal complement of $K_a$ inside $L_a$ is $\mathrm{span}\{Y_0, Y_1\}$ (real vectors,
   conjugation immaterial), with Gram matrix $B$. This is "the extension from $K_a$ to $L_a$."
3. **The doubly-singular coefficient block of the literal reproducing kernel.** The kernel
   $K_L(w,z) := M(Y_w)(z) = [Y_w, Y_z]$ (analytic in both variables, Burnol's stated reason for the
   bilinear convention) has vector-valued simple poles $Y_w \sim Y_p/(w-p)$ at $w = p \in \{0,1\}$,
   so $K_L(w,z) = \sum_{p,q} B_{pq}\frac{1}{w-p}\frac{1}{z-q} + (\text{lower-order poles + regular})$.
   In the Hermitian convention ($K_H(w,z) = \overline{K_L(w,\bar z)}$, positive definite because
   $L_a$ is a Hilbert space) the doubly-singular block is again $B$. This is the literal counterpart
   of the ansatz's coefficient matrix $C$ in the Cauchy-vector basis $\{\frac1s, \frac1{s-1}\}$,
   which the ansatz computed as $[[0,-\rho],[-\bar\rho,0]]$.

Since $B$ is the Gram matrix of two vectors in a Hilbert space, it is positive semidefinite a
priori, and positive DEFINITE exactly by Prop. 4.5 (linear independence of $Y_0, Y_1$). Signature
$(2,0)$, $\kappa = 0$. The computation below measures $N$, $\beta$, the eigenvalues
$N \pm \beta$, and the resolution margins, rather than resting on the structural argument alone.

## 5. Where the ansatz diverged (the named step)

The #168 dossier's Section 5 "Setup" posited $K_L = K_{K_a} + K_{\rm sing}$ with $K_{\rm sing}$ the
**Nevanlinna difference-quotient kernel** of a scalar singular part
$Q_{\rm sing}(\tau) = \frac{\rho}{\tau - i/2} + \frac{\bar\rho}{\tau + i/2}$ (critical-line
coordinates $\tau = i(s - \frac12)$). That difference-quotient shape is precisely what produced the
telescoping (each pole's contribution landing on the OTHER pole's off-diagonal slot, zero diagonal,
signature $(1,1)$ for any $\rho \neq 0$). The literal kernel correction is not of difference-quotient
form: it is the rank-2 POSITIVE Gram block of the two evaluator directions, with diagonal
$N = \|Y_1\|^2 > 0$. No scalar $Q$ can reproduce it: a generalized Nevanlinna function of class
$N_0$ (Herglotz) has no poles off the real axis (here: off the critical line, and $s = 0,1$ ARE off
it), while $N_\kappa$ with $\kappa \geq 1$ forces at least one negative square in the kernel,
contradicting positivity [standard Krein-Langer background, same tier as #168's own Section 3
definitions; not re-fetched today]. So the divergence is exactly at the additive-ansatz Setup step:
**modeling a positive two-dimensional Hilbert-space enlargement as a scalar generalized-Nevanlinna
singular perturbation.** The mirror-pole algebra downstream of that step was correct (and is
re-confirmed below in its corrected home); the step itself does not match Burnol's construction.

## 6. The corrected home of the $(1,1)$ block

The ansatz's structure is not noise; it lives one pairing away. Define the
$\mathcal{F}_+$-twisted pairing $\langle f, g\rangle_\times := [f, \mathcal{F}_+ g]$ on $L_a$
(equivalently $(f, \mathcal{F}_+\bar g)$; this is the natural pairing of the involution
$F^\#(s) = \overline{F(1-\bar s)}$, i.e. ordinary complex conjugation in the critical-line
coordinate $\tau$, which is exactly the conjugation the ansatz's model used). Using
$\mathcal{F}_+ Y_1 = -Y_0$ and $\mathcal{F}_+ Y_0 = -Y_1$, the twisted evaluator block is

$$X = \begin{pmatrix} -\beta & -N \\ -N & -\beta \end{pmatrix}, \qquad
\text{eigenvalues } -\beta \mp N, \text{ signature } (1,1) \text{ whenever } |\beta| < N,$$

with dominant OFF-diagonal $-N$: for small $|\beta|/N$ this is literally the ansatz's
$[[0,-\rho],[-\bar\rho,0]]$ with $\rho = N$. The computation verifies signature $(1,1)$ of $X$ at
every grid point (test T16). But $\langle\cdot,\cdot\rangle_\times$ is NOT the inner product of
$L_a$; it is the indefinite quadratic form whose diagonalization is the $\mathcal{F}_+$-eigenspace
splitting: the eigendirections of $B$ are $(Y_1 \pm Y_0)/\sqrt2$, i.e. the
$\mathcal{F}_+$-anti-invariant and invariant combinations, with
$N + \beta = \frac12\|(1 - \mathcal{F}_+)Y_1\|^2$ and $N - \beta = \frac12\|(1 + \mathcal{F}_+)Y_1\|^2$,
and the same two directions diagonalize $X$ with MIXED signs, which is where the one negative
square lives. The ansatz, by conjugating in $\tau$, computed the
negative-square count of THIS form, not of the space. That is the precise sense in which the
mirror-pole mechanism was "correct algebra applied to the wrong pairing."

## 7. THE COMPUTATION

Module: [`e1w_burnol_bilinear.py`](e1w_burnol_bilinear.py), standalone, mpmath at 44 dps (full) /
34 dps (quick), record in [`e1w_burnol_bilinear.npz`](e1w_burnol_bilinear.npz).

**Discretization.** $L_a^\perp = \overline{\Phi_0 + \mathcal{F}_+\Phi_0}$ with $\Phi_0$ = mean-zero
$L^2(0,a)$ (Prop. 4.5's second proof, verbatim above). Galerkin over mean-zero polynomial bases of
degree $\leq K$; all needed inner products reduce to integrals over $(0,a)$ (the cross-Gram
$(\phi_j, \mathcal{F}_+\phi_k)$ is a smooth double integral over $(0,a)^2$; self-adjointness and
unitarity of $\mathcal{F}_+$ close the rest). $B$ is then the Schur complement
$B_{ij} = (u_i, u_j) - b_i^T G^{-1} b_j$, with $(u_1,u_1) = (u_0,u_0) = \frac1a$ and
$(u_0,u_1) = -\mathrm{Si}(2\pi a^2)/(\pi a^2)$ in closed form.

**Route A**: orthonormal shifted-Legendre basis, Gauss-Legendre quadrature ($n = 96$, nodes by
Newton at working precision), LU solve. **Route B**: mean-zero shifted-Chebyshev basis
(non-orthogonal Gram), Clenshaw-Curtis quadrature ($n = 88$). At matched $K$ the two are
exact-arithmetic-equal, so their discrepancy measures the numerical error of both code paths.
**Route R** (residue reading): $B$ re-read off the pointwise constant values of the computed
projections ($\mathrm{Res}_1 = -\text{constant}$, Section 3's dictionary), at five spread points of
$(0,a)$; converges with $K$ independently of the Gram algebra.

**Convention anchors** (pinning the implementation to the paper): the completed-Mellin functional
equation on the Gaussian (T01, worst error $1.6 \times 10^{-45}$); $\chi(s)$ Gamma-form vs
$\zeta(s)/\zeta(1-s)$, eqs (7)-(8) (T02, $3.8 \times 10^{-45}$); the indicator Mellin identity
(T03, $3.6 \times 10^{-45}$); and the co-Poisson formula (9) verified END TO END numerically
($\mathcal{F}_+$ of a co-Poisson sum of an explicit $g$ on $[0.6, 1.5]$, evaluated inside $(0,a)$,
against $-\widehat{g}(1)$: relative error $6.8 \times 10^{-4}$, truncation-limited, T18).

### The measured block (route A, $K = 24$, full mode)

| $a$ | $N = \|Y_1\|^2$ | $\beta = (Y_0, Y_1)$ | $\mathrm{eig}_{\min} = N + \beta$ | $\mathrm{eig}_{\max} = N - \beta$ | $|\beta|/N$ | K-increment |
|---|---|---|---|---|---|---|
| 0.3 | 3.33303852235 | $-1.96480596558$ | $1.368$ | $5.298$ | 0.5895 | 0.0 |
| 0.5 | 1.97544305632 | $-1.74299523449$ | $2.324\times10^{-1}$ | $3.718$ | 0.8823 | 0.0 |
| 0.8 | 0.600906523845 | $-0.597902321164$ | $3.004\times10^{-3}$ | $1.199$ | 0.9950 | $1.3\times10^{-41}$ |
| 1.0 | 0.0377811234767 | $-0.0377391668145$ | $4.196\times10^{-5}$ | $7.552\times10^{-2}$ | 0.99889 | $2.3\times10^{-35}$ |
| 1.25 | $1.17219023646\times10^{-4}$ | $-1.17173616754\times10^{-4}$ | $4.541\times10^{-8}$ | $2.344\times10^{-4}$ | 0.99961 | $2.9\times10^{-27}$ |
| 1.6 | $1.58155949166\times10^{-9}$ | $-1.58134806353\times10^{-9}$ | $2.114\times10^{-13}$ | $3.163\times10^{-9}$ | 0.99987 | $1.7\times10^{-21}$ |

Every eigenvalue positive: **signature $(2,0)$ at every $a$**, with the sign of the small
eigenvalue resolved by margin (the K-increment column is the measured $|N^{(24)} - N^{(20)}|$
convergence residual; since the Galerkin block converges to $B$ monotonically from above in the
PSD order, the small eigenvalue is certified positive whenever the increment is far below it,
which it is: worst ratio $8 \times 10^{-9}$ at $a = 1.6$). Convergence in $K$ is superexponential
(measured, tests T08/T09), quadrature-node stability at the $10^{-34}$ level (T14).

### Two-route agreement and robustness

- Route A vs route B, worst relative discrepancy over the grid at matched $K$:
  $\mathbf{3.54 \times 10^{-36}}$ (T12).
- Residue reading vs Gram reading, worst relative: $2.1 \times 10^{-6}$, with pointwise constancy
  spread of the computed $Y$'s at $2.0 \times 10^{-5}$ relative (both truncation-limited at
  $a = 1.6$ where $N \sim 10^{-9}$; at $a \leq 1$ agreement is $\sim 10^{-10}$) (T13).
- Grid: 6 values of $a$ x 5 values of $K$ x 2 routes = 60 solved configurations (vs #168's 24),
  all signature $(2,0)$; quick mode reruns 18 of them.
- Small-$a$ closed-form anchor (T17): $N \to 1/a$ and $\beta \to (u_0, u_1) = -\mathrm{Si}(2\pi a^2)/(\pi a^2) \to -2$;
  measured at $a = 0.3$: $|N - 1/a| = 3 \times 10^{-4}$, $|\beta - (u_0,u_1)| = 2.5 \times 10^{-6}$.
- Structural identities at $10^{-39}$: $B_{00} = B_{11}$, $B_{01} = B_{10}$, and the coefficient
  swap encoding $Y_0 = -\mathcal{F}_+ Y_1$ (T10).

**Measured shape worth recording.** As $a$ grows, $N$ and $|\beta|$ decay together
super-exponentially and $|\beta|/N \to 1$: the block approaches the rank-one degenerate direction,
i.e. $Y_1$ becomes asymptotically $\mathcal{F}_+$-invariant, and the $\mathcal{F}_+$-odd evaluator
combination carries vanishing norm ($\mathrm{eig}_{\min} = N + \beta$). The extension stays
strictly positive (Prop. 4.5 at every $a$) but with collapsing margin. This measured profile
$(N(a), \beta(a))$ is precisely "the coupling constant $\rho(a)$" whose absence #168 flagged as its
largest gap, now with the corrected sign structure: the coupling is positive-definite, not
indefinite.

## 8. Beurling / D-H typing (what this mechanism consumes)

Facts, not guesses: the computation of $B$ consumes (i) the $\Gamma$-factor / functional-equation
pole structure ($\chi(s)$, the completed Mellin $M$), and (ii) the additive-interval constancy
conditions defining $L_a$. It consumes NO Euler product anywhere: $\zeta$ appears only in the
convention check $\chi = \zeta(s)/\zeta(1-s)$ and in the co-Poisson anchor; the pole of $M(f)$ at
$s = 1$ for $f \in L_a$ is the CONSTANCY pole ($\mathrm{Res}_1 = -f(0^+)$), not the arithmetic pole
of $\zeta$ (zeta-loading enters $L_a$ only through the co-Poisson subspace $P_a$, which this
computation never uses). Consequently the same construction over any functional equation of
$s \leftrightarrow 1-s$ type with a Gamma-type factor (a Davenport-Heilbronn analogue included;
note D-H's function is entire, so its analogue pole data would again come from the Gamma factor and
the test-function constancy) yields the identical $(2,0)$ verdict. Typing: this rung is
FORM-SIDE / STRUCTURAL; it makes and can make no zeta-vs-fake discrimination claim, which is
correct for its role: it audits a claimed structural property of a named space, it does not propose
an RH mechanism. The D-H and Beurling screens therefore apply to any future attempt to LOAD this
structure into a positivity argument, not to the audit itself.

## 9. Consequences

1. **#168(iii) DOWNGRADES.** The candidate-tier $\kappa = 1$ does not survive the literal form:
   $\kappa(L_a) = 0$, signature $(2,0)$, source tier ("source" = the construction as defined in
   math/0203120, computed, not modeled). The mirror-pole mechanism survives only as the signature
   $(1,1)$ of the $\mathcal{F}_+$-twisted pairing (Section 6), which carries no reproducing-kernel
   or Pontryagin-space meaning for $L_a$.
2. **The $HB_1$ question loses its $L_a$ motivation.** PHASE_STATE next-step 1's second clause
   ("pose the $HB_1$ one-sided extremal-theorem question, $\kappa = 1$, candidate tier") was
   premised on $L_a$ instantiating the mildest indefinite class. It does not: $L_a$ is a POSITIVE
   de Branges-type space with poles allowed (Burnol's own "allow poles" sentence, quoted in
   Section 2). The Kaltenbäck-Woracek entry theorem is not needed and does not apply (elements are
   non-entire; the space is not $\mathcal{H}(E)$ for entire $E$, and its negative index is $0$).
   The $HB_1$ extremal question may retain independent interest for other constructions, but it is
   no longer THE sharpened question of this corridor.
3. **#164 stays closed and hardens.** The #164 reopen residual (a meromorphic majorant theory that
   poses on $L_a$) must now be sought in POSITIVE meromorphic de Branges theory (BBH-adjacent),
   not in indefinite (Pontryagin/$N_\kappa$) machinery; the indefinite route to a repair is now
   closed at source, not merely unattempted.

## 10. Honest limits

1. The residue dictionary, the projector formulas for $Y_0, Y_1$, and the identification of $B$
   with the doubly-singular kernel block (Sections 3-4) are this note's own derivations from the
   quoted propositions: elementary, numerically verified here (constancy of the computed
   projections at $2\times10^{-5}$, the swap identity at $10^{-39}$, the co-Poisson anchor at
   $6.8\times10^{-4}$), but not quoted theorems of the paper.
2. The "no scalar $Q$" step in Section 5 cites standard Krein-Langer facts at the same SECONDARY
   tier as #168's own background section; those sources were not re-fetched today.
3. The $a$-grid stops at $1.6$: beyond it the block is numerically near-degenerate
   ($1 - |\beta|/N \sim 10^{-4}$ and shrinking) and resolving $\mathrm{eig}_{\min} > 0$ costs
   rapidly growing $K$. Positivity for ALL $a$ rests on the structural argument (Gram matrix +
   Prop. 4.5), which is airtight but is an argument, not a measurement, for $a > 1.6$.
4. Routes A and B share the abstract Galerkin variational principle and the mpmath arithmetic;
   independence is at the level of basis family, quadrature theory, and code path. The residue
   reading (route R) is the check of the principle itself, and the convention anchors check the
   paper-matching of $M$, $\mathcal{F}_+$, $\chi$ end to end.
5. The co-Poisson end-to-end check is truncation-limited at $6.8\times10^{-4}$ relative; it
   validates conventions only, and contributes nothing to $B$.
6. Nothing here touches the OTHER #164 residual (the absence of a majorant/extremal theorem for
   any indefinite class): that absence simply becomes moot for $L_a$.

## 11. Handoff

- **Handed-forward question (the replacement for the $HB_1$ clause).** $L_a$ is a positive
  meromorphic de Branges extension whose pole coupling is now MEASURED:
  $B(a) = [[N, \beta], [\beta, N]]$ with $N, -\beta$ super-exponentially decaying and
  $|\beta|/N \to 1$. The question that inherits the corridor's load: **does the positive
  "allow poles" extension class (de Branges' own, per Burnol) admit an extremal/majorant theory in
  which the two pole directions with near-degenerate positive coupling play the role the
  #163/#164 corridor wanted the indefinite $\kappa = 1$ structure to play?** Concretely: BBH-type
  admissible-majorant theory is organized around winding/asymptotics and was found blind to
  finite-rank pole data (#168(i)); the finite-rank data is now positive and quantified, so the
  right search key is "de Branges spaces of meromorphic functions / finite-dimensional extensions
  of $\mathcal{H}(E)$, extremal problems," not "$HB_\kappa$."
- **For SYNTHESIZER**: LEARNINGS #168(iii) needs the downgrade annotation ($\kappa = 0$ at source
  tier, this dossier); PHASE_STATE next-step 1's second and third clauses collapse into the
  handed-forward question above.
- **VERIFIER targets**: (V1) the residue dictionary $\mathrm{Res}_{s=1}M(f) = -f(0^+)$ for
  $f \in L_a$ (elementary Mellin split, Lean-friendly); (V2) $Y_0 = -\mathcal{F}_+ Y_1$ from the
  functional equation; (V3) the two-line incompatibility lemma (PSD kernel with off-axis poles is
  not a Nevanlinna kernel of any $N_\kappa$).
- **ADVERSARY cases**: (A1) probe $a \in (1.6, 2.5]$ at higher $K$/dps for a signature flip (none
  is possible if the structural argument is right; a flip would falsify the discretization, not
  the theorem); (A2) attempt to complete $L_a$ against the twisted pairing
  $\langle f, g\rangle_\times$ into a genuine Krein-space realization in which the ansatz's
  $(1,1)$ IS the space structure, and check whether de Branges axiom (i)
  ($[F^\#, G^\#] = [G, F]$) survives; if some completion exists, #168(iii) could be partially
  rehabilitated in a different category: this is the one named escape and it is OPEN; (A3) check
  the $B(a)$ profile against Burnol's later explicit-kernel papers (the $E_a$ structure-function
  notes [8],[9] cited in the paper) for an independent closed form.
