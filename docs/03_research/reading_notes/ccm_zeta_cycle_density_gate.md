# Reading note: the Connes-Consani(-Moscovici) zeta-cycle / prolate line vs the density gate

> SURVEYOR reading note, 2026-07-02. Commissioned by LEARNINGS #151 / `e2aj_w6_gluing.py`.
> **Question.** The e2aj probe measured a DENSITY GATE on any global gluing of the per-prime
> trace circles: matching the eigenvalue count to Riemann-von Mangoldt $N(T) \sim
> \frac{T}{2\pi}\log\frac{T}{2\pi e}$ forces $\theta(P) = \sum_{p \le P} \log p \approx
> \log\frac{T}{2\pi e}$, i.e. a direct-sum gluing at height $T$ only has budget for primes up
> to $\sim \log T$ (measured $P^* = 7, 11, 13, 17$ at $T = 10^3..10^6$). Does the CCM
> zeta-cycle / semilocal-prolate line pass, fail, or reframe this gate, and where does the
> rational lattice enter their constructions?

## Sources and verification depth

| Source | What it is | Depth |
|---|---|---|
| arXiv:2106.01715, Connes-Consani, *Spectral Triples and Zeta-Cycles* (Enseign. Math. 69 (2023) no. 1-2, 93-148) | the zeta-cycle criterion + IR numerics | sections-read (ar5iv HTML, 3 targeted extraction passes: Def 1.1, Thm 1.1, Prop 2.1 / eq. (2.11), numerics window, map $\mathcal{E}$) |
| arXiv:2112.05500, Connes-Moscovici, *Prolate spheroidal operator and zeta* | the archimedean prolate operator, detailed | sections-read (ar5iv HTML, 1 pass) |
| PNAS 119 (22) e2123174119 (2022), Connes-Moscovici, *The UV prolate spectrum matches the zeros of zeta* | the UV announcement | sections-read (PMC full text, 1 pass). NOTE: authors are Connes-Moscovici, **not** CCM (task brief said CCM; corrected) |
| arXiv:2310.18423, Connes-Consani-Moscovici, *Zeta zeros and prolate wave operators* (Ann. Funct. Anal. 15 (2024) art. 87; v1 2023-10-27, v2 2024-05-04) | the semilocal integration | sections-read (arXiv HTML, 1 pass) + prior theorem-level dossier (`docs/03_research/ccm_semilocal_prolate.md`) |
| arXiv:2511.22755, Connes-Consani-Moscovici, *Zeta Spectral Triples* (2025-11-27; to appear, EMS Lect. Notes in Math.) | **the key source**: the operator whose spectrum matches zeros, built from Euler data $p \le \lambda^2$ | sections-read (arXiv HTML, 3 targeted passes) |
| arXiv:2511.23257, Connes-van Suijlekom, *Quadratic Forms, Real Zeros and Echoes of the Spectral Action* (Commun. Math. Phys. 2025) | the Caratheodory-Fejer self-adjointness engine used by 2511.22755 | abstract-only |
| arXiv:math/9811068, Connes 1998 trace formula | the semilocal baseline ($X_S$, cutoff counting) | repo reading note (`Connes-1998-Trace-Formula-NCG-Zeros.md`), previously read in full |
| arXiv:2006.13771, Connes-Consani, *Weil positivity and trace formula, the archimedean place* (Selecta Math 2021) | the archimedean positivity template | 1 weak pass this session + prior theorem-level dossier |

**Fidelity caveat.** All web reads are LLM extractions from ar5iv / arXiv HTML, not
line-by-line LaTeX reads. Theorem and equation numbers quoted below are high-confidence but
individually tagged; anything single-sourced from one extraction pass is marked. Numbers I
computed myself (zero heights via `mpmath.zetazero`, $2\pi x$ values, $\theta(P)$) are exact.

---

## Q1. The prime-activation law

**Which places are active at cutoff $\lambda$.** The activation is by SUPPORT, not by an
adelic choice. Test functions live on the interval $[\lambda^{-1}, \lambda] \subset
\mathbb{R}_+^*$; then $f * g^\sharp$ has support in $[\lambda^{-2}, \lambda^2]$, so the Weil
quadratic form truncates itself to prime powers $n \le \lambda^2$:

> "$Q W_\lambda(f,f) = \int_{\mathbb{R}} |\hat f(t)|^2 \,\frac{2\partial_t\theta(t)}{2\pi}\,dt
> + 2\Re(\hat f(i/2)\overline{\hat f}(-i/2)) - \sum_{1<n\le\lambda^2} \Lambda(n)\langle f
> \mid T(n) f\rangle$" (2511.22755 eq. (3.19); same formula as 2106.01715 Prop. 2.1 /
> eq. (2.11), there with $V(n)$; $\theta$ = the Riemann-Siegel theta)

> "the Riemann-Weil explicit formulas give a concrete and finite expression of the semi-local
> Weil quadratic form... which only involves primes less than, say, $\lambda^2$"
> (2106.01715, Section 2 intro; single extraction pass)

> "The construction only involves the Euler products over the primes $p \le x = \lambda^2$"
> (2511.22755, abstract, verbatim)

So $S(\lambda) = \{\infty\} \cup \{p \le \lambda^2\}$. By contrast, in the semilocal paper
proper the set is free: "Let $S$ be a finite set of places with $\infty \in S$"
(2310.18423, throughout; decoupled from $\lambda$).

**Up to what height are zeros matched.** No paper states a $P(T)$ law explicitly
(UNVERIFIED as a stated claim; I searched three passes). What the texts give:

- 2106.01715 (IR numerics): "by varying $L$ in the interval $5 \le \lambda^2 \le 16.5$ ...
  one produces 31 numbers in amazing agreement with the full collection of values of the
  first 31 zeros" and "reproducing the first thirty one zeros of the Riemann zeta function
  from our spectral side... the probability of having obtained this agreement at random...
  a very small number whose first fifty decimal places are all zero."
- 2511.22755 (Section 6 numerics, $N = 120$, $\lambda^2 = 12, 13, 14$): "using only the
  primes $\le 13$ one obtains for the first 50 zeros an extraordinary accuracy, with errors
  ranging from $2.5\times 10^{-55}$ for the first zero to approximately $10^{-3}$ for the
  fiftieth."
- Exact theorem (knife-edge version): "Let $s>0$ be such that $\zeta(1/2+is)=0$, then any
  circle of length an integral multiple of $2\pi/s$ is a $\zeta$-cycle, and the spectrum of
  the action of $\mathbb{R}_+^*$ on $(\Sigma_\mu\mathcal{E}(\mathcal{S}_0^{ev}))^\perp$
  contains $s$" (2106.01715, Thm 1.1(ii) verbatim).

**The implied $P(T)$ (my inference, labeled as such).** The 2106 window edge sits at
$2\pi\lambda^2$: $2\pi \cdot 16.5 = 103.67$ vs $\gamma_{31} = 103.7255$ (agreement to 5
parts in $10^4$), and the window bottom $2\pi \cdot 5 = 31.4$ vs $\gamma_4 = 30.42$. So the
high-precision matched height at cutoff $x = \lambda^2$ is $T_{\text{edge}} \approx 2\pi x$,
i.e. $P(T) \approx$ largest prime $\le T/2\pi$: **linear in $T$**. The 2511 numerics extend
past this edge ($\gamma_{50} = 143.1 > 2\pi\cdot 13 = 81.7$) but with error degrading
smoothly and exponentially in the zero index ($10^{-55} \to 10^{-3}$ over 50 zeros, roughly
one decade per zero; intermediate table rows single-sourced from one extraction pass, the
two endpoints double-confirmed). No sharp knee at the edge is visible in their table
(moderate confidence).

## Q2. Density-gate comparison

**Their prime consumption vastly exceeds the gate's direct-sum budget.** At $T \approx 104$
the gate needs $\theta(P^*) \approx \log(T/2\pi e) \approx 1.8$, i.e. $P^* = 3$; CCM
activate $p \le 16.5$, $\theta(13) = 10.31$, about $5.8\times$ over budget in $\theta$ and
$P \sim T/2\pi$ instead of $P \sim \log T$. Taken as a direct sum of prime circles this
would overcount massively. It does not, for a structural reason visible in the construction:

**The glue is not a direct sum. One interval carries the whole budget.** The operator
$D_{\log}^{(\lambda,N)}$ (2511.22755, Thm 1.1) is a rank-one perturbation of the scaling
Dirac on $L^2([\lambda^{-1},\lambda], d^*u)$, a single circle of circumference
$L = 2\log\lambda = \log x$. Its unperturbed eigenvalue spacing is $\pi/\log\lambda = 2\pi/L$
("the $2N{+}1$ eigenvalues of smallest absolute value (i.e. $\le N\pi/\log\lambda$)",
2511.22755 Section 5), so its density is $\log(x)/2\pi$ per unit height, constant. This
equals the Riemann-von Mangoldt density $\log(T/2\pi)/2\pi$ exactly at $T = 2\pi x$, which
is the observed high-precision edge: measured, $\log 16.5 = 2.8034$ vs
$\log(\gamma_{31}/2\pi) = 2.8036$. The primes $p \le x$ enter only as COEFFICIENTS of the
quadratic form (the $\Lambda(n)$ sum in eq. (3.19)) perturbing that one circle; they
contribute **no additional circumference**.

**Two meters, not one.** The e2aj gate conflated two roles that coincide only in the
direct-sum gluing:

1. **Circumference (eigenvalue budget):** CCM comply exactly. Total circumference
   $L = \log x \approx \log(T/2\pi)$ at the matched edge, which is the gate's budget (up to
   the additive 1 from $\log(T/2\pi e)$ vs $\log(T/2\pi)$, i.e. count-matching vs
   edge-density-matching).
2. **Euler-data depth (form coefficients):** CCM consume $\Lambda(n)$ to $n \le x \approx
   T/2\pi$, exponentially deeper than the gate's $P^* \sim \log T$. In a direct sum each
   data-prime drags its own circle ($\theta(P)$ circumference); in the CCM gluing data depth
   and circumference are decoupled.

**Do they say why the surplus does not overcount?** Not explicitly; no discussion of
overcounting or of eigenvalue density vs RvM appears in 2511.22755 (searched; the paper
"does not provide... density per unit height", extraction pass 1) and none in 2106.01715.
Their own framing is the mirror image: fewness of DATA, "the zeros of this function give
high-precision approximations to the first non-trivial zeros... using remarkably few terms
of the Euler product" (2511.22755). But the structural answer is in the exact theorem:

> "The spectrum of the action of the multiplicative group $\mathbb{R}_+^*$ on the orthogonal
> of $\Sigma_\mu\mathcal{E}(\mathcal{S}_0^{ev})$ in $L^2(C)$ is formed by imaginary parts of
> zeros of the Riemann zeta function on the critical line." (2106.01715, Thm 1.1(i), verbatim)

The circle of length $\log x$ carries $\frac{T}{2\pi}\log\frac{T}{2\pi}$ states up to the
edge, an excess of $\approx T/2\pi = x$ states over $N(T)$; the zeros are realized only on
the ORTHOGONAL COMPLEMENT of the lattice-periodization image $\Sigma_\mu\mathcal{E}$, which
absorbs the surplus (my synthesis, labeled). Two corroborating quoted anchors: the prolate
subspace dimension "$1+\nu(\lambda^2) \sim 2\lambda^2$ of extremely small non zero
eigenvalues" (2106.01715), and the PNAS counting "$\sigma(E,\lambda) \approx
\frac{E}{2\pi}(\log\frac{E}{2\pi}-1+\log 4-2\log\lambda) + \lambda^2 + o(1)$" (PNAS Prop.
3.2; note the $+\lambda^2$ bookkeeping term). This is Connes 1998's absorption picture
(zeros as missing lines) relocated to a compact circle: the "white light" density is
$\log(x)/2\pi$ and the lattice eats all of it except the zeros.

## Q3. Where the lattice enters

The construction is NOT built from $\{\log p\}$ alone; the rational lattice enters at three
identified points.

1. **The zeta-cycle criterion itself (theorem level).** The map
   > "$\mathcal{E}(f)(x) := x^{1/2}\sum_{n>0} f(nx), \quad \forall f \in
   > \mathcal{S}_0^{ev}$" (2106.01715, eq. (1.3), verbatim)
   is a sum over the integer lattice (the idele-class shadow of $\mathbb{Q}^*$: compare
   Connes 1998 $E(f)(g) = |g|^{1/2}\sum_{q\in k^*} f(qg)$, repo note). The very definition
   "A $\zeta$-cycle is a circle $C$ of length $L = \log\mu$ such that the subspace
   $\Sigma_\mu\mathcal{E}(\mathcal{S}_0^{ev})$ is not dense in the Hilbert space $L^2(C)$"
   (Def. 1.1, verbatim) and the spectral realization Thm 1.1(i) both consume $\mathcal{E}$.
   In 2310.18423 the semilocal $\mathcal{E}$ "agrees with the canonical identification of
   the semilocal functions with functions on idele classes" (Section 3.6, single pass); in
   2006.13771 the radical of the Weil form is the range of $\mathcal{E}$ (prior dossier
   depth). The lattice is the mechanism that carves the zeros out of the circle spectrum.
2. **The Weil-form coefficients (operator level).** The operator inputs of 2511.22755 are
   only: the Riemann-Siegel density $2\partial_t\theta(t)/2\pi$ (archimedean), the pole term
   $2\Re(\hat f(i/2)\overline{\hat f}(-i/2))$, and $\Lambda(n)$ for $n \le \lambda^2$
   (eq. (3.19)). No sum over $\mathbb{Q}^*$ appears in the operator, and "No zeta zeros are
   input" (extraction pass; the ground state $\xi$ of the truncated form $Q_{W_\lambda}^N$
   is the perturbation vector, "normalized by $\delta_N(\xi) = 1$", Thm 1.1). But the pole
   term and the $\theta$-density are the explicit formula's $s = 0, 1$ and $\Gamma$-factor
   entries, i.e. the trace the lattice leaves after Poisson/theta; the lattice is consumed
   upstream, in the DERIVATION of the explicit formula, not in the operator assembly.
3. **The unproven step (where the lattice must be consumed again).** In the outlook the
   bridge from the constructed determinant to $\Xi$ runs through prolate approximation of
   $\xi_\lambda$ (built via $\mathcal{E}$ and the prolate wave operator), and
   > "Justifying rigorously this step is the main remaining obstacle to our approach to RH"
   > (2511.22755, Section 7, after Lemma 7.2, verbatim extraction).
   So the Euler data builds the operator; the lattice certifies (would certify) its limit.

## Q4. Determinant-class status

**Archimedean prolate operator (proven core).** Connes-Moscovici prove the self-adjoint
extension and discreteness: "$\mathbf{W}_{sa}$ is the only self-adjoint extension of
$\mathbf{W}_{min}$ commuting with $P_\lambda$ and $P^\lambda$" (PNAS Thm 1.6(iii)); "The
spectrum of $\mathbf{W}_{sa}$ is discrete and unbounded on both sides; its negative
eigenvalues are simple" (PNAS Thm 1.6(iv) / 2112.05500 Thm 2.6(iv)). The counting function
is proven to RvM shape: PNAS Prop. 3.2 (the $\sigma(E,\lambda)$ formula above) and PNAS Thm
5.1 / eq. (33): "$N(E) \approx \frac{E}{2\pi}(\log\frac{E}{2\pi}-1) - \log\frac{E}{2\pi} +
O(1)$". CAUTION: my two extraction passes disagree on the special value ($\lambda = 2$ in
the PNAS pass vs $\lambda = \sqrt 2$ in the 2112.05500 pass) and on the $-\log$ term;
UNVERIFIED at digit level, but both passes agree the RvM LEADING term is a theorem with
$O(1)$ error. The match of INDIVIDUAL eigenvalues to squares of zeros is numerical only:
"numerical evidence for the ultraviolet spectral similarity" (first ~100 eigenvalues,
figures). No trace-class claim; discreteness via Sturm-Liouville.

**Semilocal prolate operator (2310.18423): formal.** Proven: stability of the semilocal
Sonin space, "the map $\theta_S$ induces a hilbertian isomorphism of the Sonin spaces"
(Thm 2), and the relation to de Branges spaces of entire functions. The semilocal prolate
operator itself is handled "ignoring the delicate domain definition needed to obtain a
selfadjoint operator" (single pass); no trace-class or determinant-class control; the
concrete candidate was deferred to a forthcoming metaplectic paper.

**Zeta spectral triple (2511.22755): determinant-class at finite truncation, exactly.**
Proven, unconditionally: (i) self-adjointness of $D_{\log}^{(\lambda,N)}$ (Thm 1.1 /
5.10(i)), supplied by the Caratheodory-Fejer extension of 2511.23257 (abstract-only read:
a PSD Toeplitz matrix of rank $n-1$ with kernel vector has associated polynomial with all
zeros on the unit circle); (ii) the exact determinant identity
$\det_{reg}(D_{\log}^{(\lambda,N)} - z) = -i\lambda^{-iz}\hat\xi(z)$ (Thm 5.10(ii)), with
$\det_{reg}(D - s) = \exp(-\zeta_D'(0; s))$ via the spectral zeta function (eq. (5.16));
(iii) "all its zeros are on the real line" (Thm 5.10(iii)). Numerical: "the spectra of the
operators converge towards the zeros of $\zeta(1/2+is)$ as the parameters $N, \lambda \to
\infty$" (abstract). Conjectural: "When $\lambda\to\infty$ the functions
$\hat\xi_\lambda(z)$ multiplied by suitable constants, converge uniformly on closed
substrips of the open strip $\Im(z) < 1/2$ towards the $\Xi$-function of Riemann" (Section
7), and "A rigorous proof of this convergence would establish the Riemann Hypothesis"
(abstract, verbatim). **Net:** determinant-class control exists PRE-LIMIT only; the
uniform $(N,\lambda) \to \infty$ control (the project's #148 determinant-class clause) is
exactly the named open obstacle.

---

## VERDICT: the CCM door REFRAMES the density gate (neither pass nor fail)

1. **Against the gate as measured (direct-sum circumference $= \theta(P)$), CCM "fail"
   spectacularly:** they activate $P \sim T/2\pi$ (linear in $T$), not $P \sim \log T$.
2. **But their gluing never claims the direct-sum shape.** One interval of length
   $\log x$ carries the entire eigenvalue budget, and $\log x = \log(T/2\pi)$ at the
   matched edge, so the gate's circumference budget is satisfied EXACTLY. The primes enter
   as quadratic-form coefficients, contributing data, not circumference.
3. **The corrected gate (two-meter law), which e2aj should adopt:** at spectral height
   $T$, a W6-style gluing needs (a) total circumference $\approx \log(T/2\pi)$ AND (b)
   Euler data $\Lambda(n)$ to depth $n \approx T/2\pi$ if the CCM numerics are the guide.
   The e2aj direct-sum reading conflated (a) and (b) because a direct sum pays
   circumference for every data prime. The semilocal "scale-coupled glue" of #151 is
   therefore NOT "more circles at higher scale" but "one longer circle + exponentially
   deeper form data at higher scale."
4. **Where the lattice enters:** as the carving/absorption mechanism. The circle of length
   $\log x$ has $\sim x$ surplus states over $N(T)$ up to the edge; the zeros are the
   spectrum on the orthogonal complement of the lattice-periodization image
   $\Sigma_\mu\mathcal{E}$ (Thm 1.1(i)), so the lattice absorbs the overcount. The Euler
   data alone builds the operator (K1-clean at the assembly level); the lattice is consumed
   in the explicit-formula coefficients upstream and in the unproven Section-7 convergence
   downstream.
5. **Determinant-class:** exact and proven at finite $(N, \lambda)$
   ($\det_{reg} = -i\lambda^{-iz}\hat\xi(z)$); open exactly at the uniform limit, which is
   where CCM themselves locate "the main remaining obstacle to our approach to RH."

## Discrepancy log (report, not resolve)

- **D1.** The repo dossier `ccm_semilocal_prolate.md` (2026-06-24) states the CCM open step
  as "construct the deferred metaplectic Jacobi-matrix operator $W_{\lambda,S}$". The Nov
  2025 paper (2511.22755) bypasses that route: the new operator $D_{\log}^{(\lambda,N)}$ is
  a different family (rank-one perturbation + Caratheodory-Fejer self-adjointness via
  2511.23257), and the open front has moved to the Section-7 convergence
  ($\hat\xi_\lambda \to \Xi$). The dossier's "precise open statement" is stale.
- **D2.** The dossier's deciding bit ("can the operator be constructed without inputting
  the zeros of $\zeta$?") is answered YES for the new family by inspection of its inputs
  ($\theta'$, pole term, $\Lambda(n \le x)$). But the R3.5/K1 question relocates rather
  than closes: the perturbation vector is the ground state of the truncated WEIL FORM,
  whose global positivity is RH-equivalent. ADVERSARY should re-run R3.5 on the 2511 shape.
- **D3.** LEARNINGS #151 describes the CCM shape as "semilocal: finitely many places per
  scale, more at higher scale." Confirmed in spirit, corrected in mechanism: more DATA
  places per scale ($p \le \lambda^2$), constant ONE spectral circle whose length grows as
  $\log$ of the data cutoff. The W6 glue spec should carry the two-meter law of the verdict.
- **D4.** The task brief attributed the PNAS UV paper to Connes-Consani-Moscovici; it is
  Connes-Moscovici (PMC author list). The three-author papers are 2310.18423 and 2511.22755.
- **D5.** My two extraction passes disagree on the PNAS/2112 special lambda value ($2$ vs
  $\sqrt 2$) and a $-\log(E/2\pi)$ term in the proven counting law. Flagged UNVERIFIED;
  does not affect the verdict (leading RvM term proven either way).

## References to follow up

- arXiv:2511.23257 (Connes-van Suijlekom, CMP 2025): the self-adjointness engine; should be
  read in full before any BUILDER reimplementation of $D_{\log}^{(\lambda,N)}$.
- arXiv:2605.20224 "High-Precision Approximation of Riemann Zeros via the Truncated Weil
  Form" (surfaced in search, not read; possibly an independent replication of the 2511
  numerics; abstract-only candidate for the next survey pass).
- The EMS volume "Applications of Noncommutative Geometry to Gauge Theories, Field
  Theories, and Quantum Space-Time" (where 2511.22755 will appear) and the companion
  Carmin.tv lecture "Extremal eigenvectors, the spectral action, and the zeta spectral
  triple" (not watched).
- Connes 1999 semilocal trace formula (already in repo notes): the $2h(1)\log'\Lambda$
  cutoff term is the ancestor of the "one circle of length $2\log\lambda$" budget.

## What this enables / what remains open

- **For BUILDER (e2aj rung 3):** rebuild the e2aj density check under the CCM assignment
  (one circle of length $\log x$, Weil-form coefficients to depth $x$) and verify the
  two-meter law numerically: circumference meter compliant, data meter at $x \approx
  T/2\pi$. Testable prediction from this note: the high-precision match window ends near
  $T = 2\pi\lambda^2$; on our own reimplementation the error-vs-index curve should bend
  there (CCM's published table shows smooth exponential degradation, no sharp knee;
  reconciling these is a concrete falsifiable check).
- **For ADVERSARY:** (i) D-H discipline on the 2511 machine: the inputs are
  explicit-formula coefficients ($\theta'$, pole, $\Lambda$); D-H has a functional equation
  but no Euler product, so the $\Lambda(n)$ stream does not exist for it, but a
  coefficient-stream analogue does; test whether the Caratheodory-Fejer even-simple
  condition (the self-adjointness gate) fails for the D-H stream. (ii) R3.5 re-run per D2.
- **Open (theirs and ours):** the Section-7 convergence $\hat\xi_\lambda \to \Xi$ is
  simultaneously CCM's "main remaining obstacle," the determinant-class clause of #148, and
  the place where the lattice ($\mathcal{E}$, prolate approximation) re-enters. On the
  project's map this is the M4 positivity in yet another costume: the truncated Weil form's
  ground-state control uniform in the cutoff. The door remains ajar, now with a sharper
  hinge: the eigenvalue budget is not the obstruction; the uniform-limit control is.
