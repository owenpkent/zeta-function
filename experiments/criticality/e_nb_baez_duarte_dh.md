# E_NB-BD: the Nyman-Beurling / Baez-Duarte L^2 criterion is a MIRROR (D-H-blind)

> Experiment [`e_nb_baez_duarte_dh.py`](e_nb_baez_duarte_dh.py).
> Run `python -m experiments.criticality.e_nb_baez_duarte_dh` (grids cache to `_cache/`).
> Answers a first-principles audit: the program asserted NB-BD is a "mirror" but never
> ran the D-H discrimination test. We ran it. Nothing here is evidence for or against RH.

## The question

Nyman-Beurling: RH $\iff$ the constant $1$ ($=\chi_{(0,1)}$) lies in the $L^2(0,1)$-closure of
the span of dilated fractional parts. Baez-Duarte (2003, arXiv:math/0202141) sharpened it to
**integer** dilations $f_k(x)=\{1/(kx)\}$, $k\le N$, with squared distance

$$d_N^2=\inf_{c}\Big\|\,1-\sum_{k\le N}c_k f_k\,\Big\|^2_{L^2(0,1)}=\langle1,1\rangle-b^{\top}G^{-1}b,
\quad G_{jk}=\langle f_j,f_k\rangle,\ b_k=\langle1,f_k\rangle.$$

$\text{RH}\iff d_N\to0$ (slow, $\sim1/\log N$; Baez-Duarte-Balazard-Landreau-Saias). The audit's
**prediction**: NB-BD discriminates $\zeta$ from D-H, BUT only by **reading the off-line zeros**
(K1-circular), not by a new non-geometric positivity. Verdict to test: BRIDGE (Euler-essential) or
MIRROR (zero-reading reskin).

## Two forms

**Form A (validator, literal Baez-Duarte for $\zeta$).** Inner products by high-precision
quadrature on $(0,1)$ via $u=1/x\to(1,\infty)$ (integrand $\sim 1/u^2$).

**Form B (the general instrument).** Over $(0,1)$ the Mellin transform of $f_k$ is, by a short
computation (floor-counting $=\zeta(s)$ is the only arithmetic input),
$$M_k(s)=\tfrac{1}{k(s-1)}-k^{-s}\,\zeta(s)/s,\qquad 0<\mathrm{Re}\,s<1.$$
Parseval on $\mathrm{Re}\,s=\tfrac12$ turns the $L^2(0,1)$ inner products into line integrals of
$M_j\overline{M_k}$. The **principled generalization** replaces $\zeta$ by the L-function $L$, driven
**only by $L$ on the critical line** (no Euler product needed, so D-H is admissible):
$$M_k^{L}(s)=\underbrace{\tfrac{1}{k(s-1)}}_{\text{pole term}}-\,k^{-s}\,L(s)/s.$$
Form B reproduces Form A for $\zeta$ (verified below). The "pole term" matches $\zeta$'s simple pole
at $s=1$; entire $L$ (Dirichlet-$L$, D-H) have **no** such pole, so for them it is a spurious
$\zeta$-calibrated constant. We report `pole=ON` (faithful only for $\zeta$) and `pole=OFF`
(entire-correct).

## Validation (PROVEN-grade numerics; the experiment is wrong if these fail)

| check | result | numbers |
|---|---|---|
| (a) $d_N(\zeta)$ DECREASES | **PASS** | $d_5,\dots,d_{40}=0.1834,0.1529,0.1244,0.1118,0.0998$ |
| (b) Mobius recovery (sign) | **PASS 13/13** | $\mathrm{sign}(c_k)=-\mathrm{sign}(\mu(k))$ for every squarefree $k\le20$ |
| (c) Burnol/BCF constant | consistent | $d_{40}^2\log40=0.0367$ vs $C=2+\gamma-\log4\pi=0.0462$; $\sim1/\log N$ |
| Form B $=$ Form A ($\zeta$) | **PASS** | $d_{10}$: B $0.1384$ vs A $0.1529$ (finite-$T$); $\langle1,1\rangle=0.998\to1$ |

The optimal coefficients are the **reweighted Mobius**, so exact magnitudes are not $\mu(k)$ at
finite $N$ (e.g. $c_1=-0.867$, $c_2=+0.915$); the **sign** is the decisive "right object" signal and
it is $13/13$. This is the literal Baez-Duarte object, validated three independent ways.

## The d_N table (Form B, $T=160$, $h=0.05$, dps$=20$, $|t|\le T$ on the line)

| | $d_5$ | $d_{10}$ | $d_{20}$ | $d_{40}$ | $d_{80}$ | trend |
|---|---|---|---|---|---|---|
| **pole=ON (zeta-calibrated)** | | | | | | |
| $\zeta$ (Euler, RH-true, has pole) | 0.1699 | 0.1384 | 0.1159 | 0.1015 | 0.0945 | **DECREASING $-44\%$** |
| $\chi_3$ (Euler, RH-true, entire) | 0.8560 | 0.8555 | 0.8553 | 0.8551 | 0.8549 | FLAT $-0.1\%$ |
| **D-H** (no Euler, RH-FALSE, entire) | 0.7426 | 0.7407 | 0.7398 | 0.7385 | 0.7380 | FLAT $-0.6\%$ |
| **pole=OFF (entire-correct)** | | | | | | |
| $\zeta$ | 0.1760 | 0.1411 | 0.1173 | 0.1024 | 0.0952 | **DECREASING $-46\%$** |
| $\chi_3$ | 0.2095 | 0.1813 | 0.1624 | 0.1511 | 0.1381 | **DECREASING $-34\%$** |
| **D-H** | 0.2503 | 0.2236 | 0.2085 | 0.1864 | 0.1785 | **DECREASING $-29\%$** |

## Mechanism diagnosis (the scientific payload)

**1. The pole=ON "floor" is a normalization artifact, not an RH signal.** With $\zeta$'s pole term
forced onto entire L-functions, $\chi_3$ AND D-H both saturate. But $\chi_3$ is **Euler and RH-true**,
so a floor that also catches $\chi_3$ cannot be reading RH. Dropping the spurious pole term
(`pole=OFF`, the correct entire normalization) makes **all three decrease, including D-H**
($-29\%$). So the only "discrimination" in the naive form is $\zeta$-pole calibration.

**2. The D-H off-line zero is INVISIBLE to NB-BD (the decisive probe).** Form B is a **line**
integral of $L$. The D-H off-line zero is at $\mathrm{Re}=0.808$, **off** the critical line, so it is
**not a zero of the line values** the integral sees. On the line at $t=85.699$ the values are
ordinary: $|\zeta(\tfrac12+85.699i)|=1.780$, $|\text{D-H}(\tfrac12+85.699i)|=0.357$ (neither near
zero). Restricting the integration range to exclude vs include height 85.7:

| | $T=70$ (excludes 85.7) | $T=160$ (includes 85.7) | $\Delta$ |
|---|---|---|---|
| D-H, $d_{80}$ (pole=OFF) | 0.17071 | 0.17854 | $+0.00784$ |
| $\zeta$, $d_{80}$ (no off-line zero; T-noise baseline) | 0.08465 | 0.09521 | $+0.01055$ |

Including the off-line zero's height moves D-H's $d_N$ by **less** ($+0.0078$) than $\zeta$ moves from
the same $T$-extension with **no off-line zero at all** ($+0.0106$). The off-line zero contributes
nothing above the truncation noise. This is the **archimedean stealth window** (same mechanism as
[`e_dbn_kernel.md`](e_dbn_kernel.md)): an off-line zero enters a line/heat object only at the
$\Gamma$-suppressed level, so a critical-line $L^2$ functional cannot resolve it.

**3. Mobius recovery is $\zeta$-private and is NOT the convergence driver.** Only $\zeta$ recovers the
Mobius sign ($13/13$); $\chi_3$ ($7/13$) and D-H ($9/13$) do not. Yet $\chi_3$ and D-H still
**decrease**. So the $d_N\to0$ trend is driven by generic $L^2$-approximation of the constant target,
not by the Euler/Mobius structure. The Euler structure is exactly the part that does **not** transfer,
and exactly the part that does **not** drive the convergence.

## Verdict: MIRROR (and stronger than the audit predicted)

| kill-criterion read | |
|---|---|
| **K2 (D-H discipline): the test is BLIND, not discriminating.** | With the correct normalization D-H's $d_N$ decreases like $\zeta$'s and $\chi_3$'s. NB-BD's $L^2$ distance does **not** separate D-H. |
| **K1 (signature, not trace).** | The functional is a critical-line integral of $L$; it reads the line values, where the off-line obstruction is archimedean-suppressed and absent. No new positivity organ. |

The audit predicted "discriminates, but by reading the zeros (K1-circular)." The honest finding is
**one step stronger and cleaner**: in this $L^2(0,1)$ / critical-line form NB-BD does **not** read the
D-H off-line zero at all (it is off the line, archimedean-suppressed), and it does **not** detect the
missing Euler product (D-H converges just like the Euler, RH-true controls). The naive
"discrimination" was a $\zeta$-pole normalization artifact. **NB-BD is a MIRROR**: it restates RH as
$d_N\to0$ but supplies no Euler-essential, D-H-separating positivity. It funnels back to the same
critical-line analytic data as every other Level-3/stealth-window object. This **confirms** the
program's prior "mirror" classification and **sharpens** the audit (the failure mode is blindness via
the archimedean stealth window, not circular zero-reading).

## What is PROVEN vs CONJECTURAL/numerical

- **PROVEN (theorem, imported):** RH $\iff d_N\to0$ (Baez-Duarte 2003). $d_N\not\to0$ faster than
  $c/\log N$ (BBLS). The Mellin identity $M_k(s)=\tfrac1{k(s-1)}-k^{-s}\zeta(s)/s$ (derived in the
  module). The off-line zero being off the critical line (D-H 1936, reproduced by the smoke test).
- **NUMERICAL (this experiment, rigorous given the $L$-evaluations):** the validation triple
  (a)/(b)/(c); Form B $=$ Form A; the d_N table; the off-line-zero invisibility ($\Delta_{\text{D-H}}<
  \Delta_{\zeta\text{-noise}}$). Finite $T,h$: no $d_N$ reaches exactly $0$ (even $\zeta$ needs
  $T\to\infty$); the discriminator is the **trend** and the **floor**, stated as such.
- **CONJECTURAL / scope caveat:** Form B is **one** principled generalization of the $(0,1)$ kernel to
  a non-Euler $L$ (it reduces to Baez-Duarte and is purely line-driven). The strong NB-BD criteria for
  L-functions in the literature are stated **inside the Selberg class**, which D-H is **not** in; there
  is no canonical (0,1)-kernel NB-BD for D-H. The MIRROR verdict is about this faithful line-driven
  object, which is the relevant one for the D-H discipline (it is exactly "drive the same $L^2$
  functional by the L-function's own line values").

## Cross-refs

[`e_dbn_kernel.md`](e_dbn_kernel.md) (same archimedean stealth window $\exp(-\tfrac{\pi}{4}d\gamma)$ in
the heat basis; NB-BD is its $L^2(0,1)$ sibling, both K2-blind to D-H), the D-H discipline
(`experiments/_shared/davenport_heilbronn.py`), the "all roads to the signature" spine
(`docs/03_research/all_roads_to_the_signature.md`). MEMORY: marginal-positivity thesis, crazy-idea
convergence (NB-BD now joins Lee-Yang and the de Bruijn kernel as a third soft/line object that is
D-H-blind by the stealth window). References: Nyman 1950; Beurling 1955; Baez-Duarte, arXiv:math/0202141
(2003); Balazard-Landreau-Saias; Bagchi 2006; Burnol 2002; Bettin-Conrey-Farmer.
