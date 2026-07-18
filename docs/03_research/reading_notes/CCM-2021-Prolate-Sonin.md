# Reading note: CCM 2021 prolate/Sonin as the C3 archimedean-injection object

> SURVEYOR reading note, 2026-07-10. Commissioned to characterize the ARCHIMEDEAN INJECTION object
> that the Connes-Moscovici prolate paper (arXiv:2112.05500) supplies, and to test whether the
> Section-7 uniform limit of the later $D_{\log}$ family is literally the C3 archimedean-injection-uniformity
> statement.
>
> Scope note. The repo already carries the prolate operator mechanics at theorem/equation level in
> [`../ccm_semilocal_prolate.md`](../ccm_semilocal_prolate.md) (the $W_{\lambda,S}$ dossier, the $-2$ jump,
> the e1f-e1j surrogate ladder) and the density-gate + $D_{\log}$ analysis in
> [`ccm_zeta_cycle_density_gate.md`](ccm_zeta_cycle_density_gate.md). This note does NOT re-derive those.
> It focuses on the C3 angle: what the prolate/Sonin/$E$/$W_\infty$ object IS as an archimedean-injection
> carrier, and how the Section-7 uniform limit relates to it. The C3 finding it grounds against lives in
> `scratchpad/tameness_trade/04_survivor_screen.md` (BUILDER, 2026-07-10) and
> [`../tameness_trade.md`](../tameness_trade.md).
>
> Rigor labels: **KNOWN** (published/repo-established, cited), **MECHANISM** (precise structural statement,
> no known counterexample, not reduced to a theorem), **HEURISTIC** (directional reading), **OPEN**.
> No em dashes anywhere.

## Sources and verification depth

| Source | What it is | Depth this pass |
|---|---|---|
| arXiv:2112.05500, Connes-Moscovici, *Prolate spheroidal operator and Zeta* (Dec 2021) | the archimedean prolate operator + Sonin space | ar5iv HTML, 3 targeted extraction passes (section list, eq. (1) operator, Section 1 Weil-positivity link) |
| arXiv:2006.13771, Connes-Consani, *Weil positivity and trace formula, the archimedean place* (Selecta 2021) | the $W_\infty$ + Sonin-compression positivity template (paper's ref [4]) | prior theorem-level dossier (`ccm_semilocal_prolate.md` Section A); not re-read here |
| arXiv:2106.01715, Connes-Consani, *Spectral triples and zeta-cycles* (Enseign. Math. 2023) | the periodization map $\mathcal{E}$ + the zeta-cycle criterion | prior reading note (`ccm_zeta_cycle_density_gate.md` Q3) |
| arXiv:2511.22755, Connes-Consani-Moscovici, *Zeta spectral triples* (2025) | the $D_{\log}^{(\lambda,N)}$ family + the Section-7 uniform limit | prior reading note (`ccm_zeta_cycle_density_gate.md` Q1-Q4) |
| `scratchpad/tameness_trade/04_survivor_screen.md`, `../tameness_trade.md` | the C3 definition + survivor-screen verdict | read in full this pass |

**Fidelity caveat.** All web reads are LLM extractions from ar5iv HTML, not line-by-line LaTeX. The eq. (1)
prolate operator and the section list are this-pass extractions; the $W_\infty = \mathrm{Tr}(\vartheta(f)\mathbf{S}) - \int f\varepsilon$
bridge, the $-2$ jump, and the $D_{\log}$ determinant identity are imported from the two prior repo notes,
themselves theorem-level extractions. Anything single-sourced is tagged.

---

## 1. What 2112.05500 supplies (the second-order archimedean realization)

**Bottom line.** 2112.05500 is the archimedean spectral realization: a self-adjoint operator on the real
line whose negative eigenvalues, in the ultraviolet, reproduce the SQUARES of the zeros of $\zeta$. It is
the second-order (square, "$W \sim D^2$") face of the program. It does not itself carry positivity or a
uniform limit; it supplies the operator whose Sonin-compression the archimedean Weil positivity (ref [4] =
2006.13771) runs on. (KNOWN.)

**Section structure** (extraction): 1. Introduction; 2. The selfadjoint prolate wave operator; 3. Sonin
space and negative eigenvalues; 4. Semiclassical approximation and counting function; 5. Dirac operators;
6. Ultraviolet behavior of spectrum of Dirac, case $\lambda=\sqrt2$; 7. Final remarks.

**The operator** (eq. (1), verbatim extraction):
$$(W_\lambda\,\xi)(x) \;=\; -\partial_x(\lambda^2-x^2)\partial_x\,\xi(x) \;+\; (2\pi\lambda)^2 x^2\,\xi(x).$$
Sturm-Liouville, coefficient $p(x)=\lambda^2-x^2$, potential $q(x)=(2\pi\lambda)^2x^2$; interval $J=[-\lambda,\lambda]$.
This is the classical Connes-Moscovici prolate operator (matches `ccm_semilocal_prolate.md` e1h, where the
same $PW_\lambda$ is diagonalized and shown positive-definite). (KNOWN.)

**The scaling link.** Section 1 states the operator is tied to the **scaling operator $S := x\partial_x$**;
the correspondence with zeta zeros is driven by "the link between the operator and the square of the
scaling operator $S$" (extraction). So $W_\lambda$ is the archimedean object read in the multiplicative /
log variable: after $u=e^x$ (or $x\mapsto \log u$), $S$ is the generator of the scaling action
$\vartheta(g)$, and $W$ is the second-order (square) object. This is why the eigenvalues match the SQUARES
of the $\gamma_j$, not the $\gamma_j$ themselves. (MECHANISM: the square/Dirac split; the first-order
"$\gamma_j$ not $\gamma_j^2$" object is the Dirac of Sections 5-6 and the later $D_{\log}$.)

**The self-dual scales.** Values $\lambda=1$ and $\lambda=\sqrt2$; Section 6 specializes the Dirac UV
analysis to $\lambda=\sqrt2$. The self-dual phase-space radius (where the $-2$ jump of 2006.13771 sits) is
$\Lambda=1$. (KNOWN; note the density-gate note flagged a two-pass disagreement $\lambda=2$ vs $\sqrt2$;
this pass's extraction says $\sqrt2$, consistent with the 2112 Section-6 heading.)

**Sonin space + Weil positivity link** (the load-bearing sentence, Section 1, verbatim extraction):
> "This feature fits with the proof [4] of Weil's positivity at the archimedean place, which uses the
> compression of the scaling action to the Sonin space."

So 2112.05500 explicitly locates the archimedean Weil positivity as a **compression of the scaling action
to the Sonin space**. The Sonin space is the phase-space-cutoff complement (functions vanishing on
$[-\lambda,\lambda]$ together with their Fourier transform); it is the negative eigenspace of $W$ restricted
to the complement of $J$. (KNOWN; the exact "$f$ and $\hat f$ both vanish on the interval" definition is not
quoted verbatim in the 2112 Sections 2-3 excerpt but is the standard 2006.13771 definition and is stated in
`ccm_semilocal_prolate.md` Section A.)

**Section 7 caveat (naming hazard).** The 2112.05500 *own* Section 7 is titled "Final remarks" and is
speculative (a two-dimensional black-hole geometry attached to the operator $2\,D\!\!\!/$); it is NOT the
RH-relevant uniform limit. The "Section-7 uniform limit" that the C3 finding and this note care about is the
Section 7 of the LATER paper 2511.22755 (the $D_{\log}$ family). Do not conflate the two Section 7s.
(MECHANISM; discrepancy D-P1 below.)

---

## 2. The archimedean-injection object, characterized precisely

C3 (`04_survivor_screen.md` Section 0) is the criterion: within the tame survivor class, any construction
that realizes the summed explicit-formula functional
$$S(f) \;=\; \sum_p\sum_{k\ge1}(\log p)\,f(k\log p) \;=\; \sum_{n\ge1}\Lambda(n)\,f(\log n)$$
does so by coupling its discrete prime carrier to an **external archimedean object $O$** (a real line / a
scaling flow / an $L^2$ of the log variable) that supplies the archimedean ingredient ($n\mapsto\log n$ and
the summation into $\mathbb{R}$). It cannot define $S(f)$ internally (the tameness trade forbids it). CCM is
one of three survivors that carry $S(f)$; its $O$ is the prolate/Sonin object on the log-line.

**The CCM injection object is a three-part archimedean carrier, all on the real log-line $\mathbb{R}$**
(MECHANISM; the identification is `04_survivor_screen.md` Section 2.2):

1. **The periodization / lattice map $\mathcal{E}(f)(u)=u^{1/2}\sum_{n>0} f(nu)$** (2106.01715 eq. (1.3)).
   Lives on the multiplicative log-line. Carries the sum over $n$, hence (via $\Lambda=\mu\ast\log$) the
   primes. Its range is the "zeta cycles"; the zeros of $\zeta$ are the scaling-action spectrum on its
   ORTHOGONAL COMPLEMENT. This is the lattice-consuming glue (the $\mathbb{Q}^\ast$ / idele-class shadow).

2. **The prolate/Sonin operator + the Sonin projection $\mathbf{S}$** on $L^2(\mathbb{R})_{ev}$
   (2112.05500 eq. (1); 2006.13771). The operator whose negative eigenspace is the Sonin space and whose
   Sonin-compression carries the positivity. The geometric $-2$ jump at the self-dual scale $\rho=1$ lives
   here, on the real line.

3. **The archimedean Weil functional $W_\infty$** (2006.13771 Thm 4.7): the archimedean term of the Weil
   explicit formula, realized as a trace on the compressed scaling action,
   $$W_\infty(f) \;=\; \mathrm{Tr}\big(\vartheta(f)\,\mathbf{S}\big) \;-\; \int f\,\varepsilon, \qquad \varepsilon = -2\,\mathrm{Id} + K \ (K \text{ Hilbert-Schmidt}).$$
   This is the archimedean piece of $S(f)$ (the $\Gamma$-factor / Riemann-Siegel-$\theta$ density term),
   carried on $L^2(\mathbb{R})_{ev}$ by the compressed scaling.

**How $\log p$ enters the object** (MECHANISM). Two archimedean routes, no internal definable sum:
(i) as the frequency $\log p$ in the L-factor measure $dm_S=|\prod_{v\in S}L_v(\tfrac12-is)|^2\,ds$ (the
L-factor phases); (ii) as the lattice support of $\mathcal{E}$. The summation is realized as the archimedean
trace $W_\infty$ / a periodization over $\mathbb{R}$, never as a first-order-definable sum in a finite-place
carrier. The e1j three-channel closure (`ccm_semilocal_prolate.md`) is the corroborating computation: every
finite/local channel (geometry / measure / sign) is blind; the entire prolate-spreading sign-source is
archimedean.

**Net.** The archimedean-injection object is the FAMILY $\{\,\mathbb{R}\text{-log-line} + \text{scaling
action} + \mathcal{E} + \text{prolate/Sonin} + W_\infty\,\}$. 2112.05500 supplies its prolate/Sonin core
(the operator whose compression is the positivity); 2006.13771 supplies $W_\infty$; 2106.01715 supplies
$\mathcal{E}$. All three sit on the same real log-line. (MECHANISM.)

---

## 3. How the prolate/Sonin space relates to the $D_{\log}$ Section-7 limit

**The two operators are the square and the Dirac-square-root of the same archimedean object.** (MECHANISM.)

- **Prolate $W_\lambda$ (2112.05500):** second-order, $W\sim (2\pi\, S)^2$-type; its UV negative eigenvalues
  reproduce the **squares** $\gamma_j^2$. The Dirac of its Sections 5-6 is the first-order square-root whose
  eigenvalues are the $\gamma_j$ (case $\lambda=\sqrt2$).
- **$D_{\log}^{(\lambda,N)}$ (2511.22755, Thm 1.1 / 5.10):** the later, simpler first-order realization. A
  rank-one perturbation of the scaling Dirac on $L^2([\lambda^{-1},\lambda],d^\ast u)$, i.e. on ONE circle of
  circumference $L=2\log\lambda=\log x$ on the log-line. Its regularized determinant is the finite-cutoff
  xi-function,
  $$\det{}_{\!reg}\big(D_{\log}^{(\lambda,N)}-z\big) \;=\; -i\,\lambda^{-iz}\,\hat\xi(z), \qquad \text{all zeros real (unconditional, finite cutoff).}$$
  The rank-one perturbation vector is the ground state $\xi$ of the TRUNCATED WEIL FORM
  $Q_{W_\lambda}(f,f)=\int|\hat f|^2\tfrac{2\partial_t\theta}{2\pi} + 2\Re(\hat f(i/2)\overline{\hat f}(-i/2)) - \sum_{1<n\le\lambda^2}\Lambda(n)\langle f\mid T(n)f\rangle$
  (2511.22755 eq. (3.19)). The prime sum $S(f)$ enters here, as the $-\sum\Lambda(n)\langle f\mid T(n)f\rangle$
  coefficients, on the archimedean test space.

**The Section-7 limit** (2511.22755 Section 7, verbatim extraction from the density-gate note):
> "When $\lambda\to\infty$ the functions $\hat\xi_\lambda(z)$ multiplied by suitable constants, converge
> uniformly on closed substrips of the open strip $\Im(z)<1/2$ towards the $\Xi$-function of Riemann,"
> and "A rigorous proof of this convergence would establish the Riemann Hypothesis"; "Justifying rigorously
> this step is the main remaining obstacle to our approach to RH" (after Lemma 7.2).

**The relation, stated.** The prolate/Sonin space is the archimedean carrier on which the truncated Weil
form and its ground state $\xi$ are defined; $D_{\log}$ is the Dirac built from that ground state on the same
log-line; and the Section-7 limit is the statement that pushing the truncation $\lambda\to\infty$ (which, by
the support-activation law $S(\lambda)=\{\infty\}\cup\{p\le\lambda^2\}$, injects ALL primes into the
truncated Weil form) makes the finite-cutoff $\hat\xi_\lambda$ converge to the true $\Xi$. So the
prolate/Sonin object is WHERE the prime sum is injected, and Section 7 is the assertion that the injection,
carried to all primes, reproduces $\Xi$. (MECHANISM; the object identity is verbatim, the activation-law
coincidence is from `ccm_zeta_cycle_density_gate.md` Q1.)

**One caveat on object drift** (KNOWN; discrepancy D1 of the density-gate note): the deferred metaplectic
$W_{\lambda,S}$ of `ccm_semilocal_prolate.md` is BYPASSED by the $D_{\log}$ family. So "the prolate/Sonin
operator" (2112.05500 / 2310.18423) and "the $D_{\log}$ operator" (2511.22755) are DIFFERENT specific
operators. They share the log-line, the scaling action, the $\mathcal{E}$/Sonin structure, and the truncated
Weil form, but $D_{\log}$ is a rank-one-perturbation determinant-class realization, not the Sturm-Liouville
$W_\lambda$. The archimedean-injection OBJECT (the family) is stable across the drift; the specific carrier
operator changed.

---

## 4. Is Section-7 uniformity literally C3 archimedean-injection-uniformity?

**Short answer: YES as an object-and-location identity; NO as a logical equivalence. C3 pins WHERE and WHY
the uniformity is archimedean; it is structurally silent on WHETHER it holds.** Three tiers, honestly
separated.

**Tier 1 (object identity) = YES, verbatim (MECHANISM).** Every object in the Section-7 statement
($\hat\xi_\lambda$, $D_{\log}^{(\lambda,N)}$, the truncated Weil form, the prolate/Sonin space, the map
$\mathcal{E}$) is supported on the real log-line $\mathbb{R}$, which is exactly C3's archimedean-injection
object for CCM. There is NO non-archimedean carrier anywhere in the Section-7 statement. The survivor screen
already established this (Section 5, "the Section-7 objects ARE that archimedean object"). This tier is a
straight object-identity check and it passes.

**Tier 2 (statement-shape identity) = YES, up to a limit-coincidence (MECHANISM/HEURISTIC).** The Section-7
uniform limit IS the statement "the archimedean injection of $S(f)$ (the truncated Weil form on the
prolate/Sonin log-line), taken to all primes, converges uniformly to the true completed zeta $\Xi$." C3's
description of the CCM wall (`04_survivor_screen.md` Section 5.2): "the Section-7 difficulty is making the
injection uniform as $S\to$ all primes... assembling all of them at once is exactly the $S\to\infty$ limit of
the archimedean operators." So the two descriptions coincide: Section-7 uniform convergence = uniformity of
the archimedean injection over all primes. The coincidence rests on the support-activation law
$S(\lambda)=\{\infty\}\cup\{p\le\lambda^2\}$ that makes "$S\to$ all primes" and "$\lambda\to\infty$" the same
limit; this holds for the 2511 $D_{\log}$ family (activation by support) but is looser in the abstract
semilocal framing of 2310.18423 (where $S$ is a free finite set decoupled from $\lambda$). Hedge logged.

**Tier 3 (logical equivalence) = NO (the honest limit).** C3 is a structural / definability statement about
WHERE $S(f)$ must enter and WHY the last step must be an archimedean all-primes limit. It is **silent on
whether the uniform limit holds**: it does not contain, imply, or predict the analytic convergence
$\hat\xi_\lambda\to\Xi$. The Section-7 statement, by contrast, is a specific analytic-convergence assertion
whose truth is RH-equivalent (the authors say proving it establishes RH). So:
- C3 correctly predicts the wall's LOCATION (archimedean, at the injection object, in the $\lambda\to\infty$
  / all-primes limit) and gives a structural REASON it must be there (the summation can only be reached by
  injecting an archimedean object, so the last hard step is necessarily an archimedean-limit step).
- C3 does NOT deliver the wall's RESOLUTION. The residual "does the uniform archimedean injection survive to
  all primes" is M4 / the arithmetic Hodge standard conjecture / global Weil positivity with a rate, on which
  C3 has nothing to say.

**Therefore: "Section-7 uniformity = C3 archimedean-injection-uniformity" is TRUE as an identity of objects
and of where-the-uniformity-must-live, and FALSE if read as "C3 predicts or is equivalent to the Section-7
convergence."** The precise honest sentence: the Section-7 uniform limit is the uniformity-of-the-archimedean-injection
step that C3 says must exist and must be archimedean; C3 locates and names it, RH-hardness (M4) owns its
truth-value. (This matches `04_survivor_screen.md` Section 5's own labeling: object-coincidence = MECHANISM,
"C3 explains why the wall is archimedean" = HEURISTIC, "does not predict whether the limit holds" = explicit
non-claim.)

**A second honest hedge (the naming hazard, promoted).** The task's "Section-7 uniform limit" is 2511.22755's
Section 7, NOT 2112.05500's Section 7 ("Final remarks", the 2D black hole). The prolate paper 2112.05500 has
no uniform-limit statement at all; it supplies the archimedean operator, and the uniform limit is stated four
years later on the $D_{\log}$ descendant. So C3's "the object that carries $S(f)$ has a Section 7 wall" is a
statement about the ANALYTIC-THREAD lineage 2006.13771 -> 2112.05500 -> 2310.18423 -> 2511.22755 taken as one
object, not about the 2021 paper in isolation.

---

## 5. Discrepancy log (report, not resolve)

- **D-P1 (two Section 7s).** The 2112.05500 own Section 7 ("Final remarks", 2D black hole, operator
  $2D\!\!\!/$) is not the RH uniform limit. The RH-relevant Section 7 is 2511.22755's. Any downstream agent
  citing "the CCM Section-7 wall" must mean the $D_{\log}$ paper's Section 7. (This note fixes the reference;
  the C3 survivor screen already used it correctly but did not flag the collision.)
- **D-P2 (object drift, inherited from density-gate D1).** The archimedean-injection object's SPECIFIC
  carrier operator changed across the lineage: prolate $W_\lambda$ (2112) / deferred metaplectic $W_{\lambda,S}$
  (2310, `ccm_semilocal_prolate.md`) vs rank-one $D_{\log}^{(\lambda,N)}$ (2511). C3's injection-object
  identification is stable at the FAMILY level (log-line + scaling + $\mathcal{E}$ + Sonin) but names the
  prolate/Sonin operator specifically; the operative object today is $D_{\log}$. `ccm_semilocal_prolate.md`'s
  "precise open statement" (construct $W_{\lambda,S}$) is stale per that note's own 2026-07-02 addenda.
- **D-P3 (square vs Dirac).** 2112.05500 reproduces the SQUARES $\gamma_j^2$ (second-order $W$); $D_{\log}$
  reproduces the $\gamma_j$ (first-order Dirac). When cross-citing "reproduces the zeros" between the papers,
  keep the square/root distinction: the prolate operator's negative eigenvalues are $-\gamma_j^2$, the Dirac's
  are $\gamma_j$.
- **D-P4 ($\lambda=\sqrt2$ vs $2$).** The density-gate note (D5) logged a two-pass disagreement on the
  special value. This pass's 2112.05500 extraction says $\lambda=\sqrt2$ (Section 6 heading). Still not
  digit-verified against LaTeX; does not affect any verdict here.

## 6. References to follow up

- arXiv:2006.13771 (Connes-Consani, archimedean Weil positivity, paper's ref [4]): the $W_\infty=\mathrm{Tr}(\vartheta(f)\mathbf{S})-\int f\varepsilon$
  bridge and the $-2$ jump; already at theorem level in `ccm_semilocal_prolate.md` Section A, but a full read
  of Thm 4.7 + the Toeplitz separation (Thm 6.11) would firm up the $W_\infty$ half of the injection object.
- arXiv:2511.23257 (Connes-van Suijlekom, CMP 2025): the Caratheodory-Fejer self-adjointness engine behind
  $D_{\log}$; still abstract-only in the repo. Read before any BUILDER touches the Section-7 limit.
- 2112.05500 Section 7 itself (the 2D black hole, $2D\!\!\!/$): unread beyond the intro pointer; likely
  orthogonal to the C3 question but should be skimmed once to confirm it carries no hidden uniform-limit claim.
- The full-text 2112.05500 LaTeX (ar5iv truncated Sections 3 and 7 in this pass): the verbatim Sonin
  definition and the exact $W\leftrightarrow S^2$ relation are extraction-inferred, not quoted; a source read
  would settle D-P3 and D-P4.

## 7. What this enables / what remains open

**Enables (for BUILDER/ADVERSARY/SYNTHESIZER):**
- **The archimedean-injection object is now pinned as a named three-part family** (log-line + scaling +
  $\mathcal{E}$ + prolate/Sonin + $W_\infty$), with 2112.05500 identified as the supplier of its
  prolate/Sonin core. Downstream work that says "inject $S(f)$ archimedeanly" now has a concrete object list
  and its three source papers.
- **The Section-7 wall is object-identical to C3's injection uniformity** (Tier 1/2). A BUILDER attacking the
  uniform limit is attacking exactly the archimedean-injection-uniformity C3 names; there is no separate
  non-archimedean route to try (consistent with e1j's all-local-channels-blind closure).
- **A clean falsifiable coordinate for ADVERSARY:** if any finite-place or geometric-descent obstruction
  (not the $\lambda\to\infty$ archimedean limit) independently blocks the program, C3's "the wall is
  archimedean by necessity" reading is incomplete (A-C3-3 in the survivor screen). Expected consistent with
  e1j, but not proven.

**Remains open:**
- The Section-7 uniform limit $\hat\xi_\lambda\to\Xi$ itself: RH-equivalent, the authors' own "main remaining
  obstacle." C3 locates it (archimedean, all-primes limit, on the prolate/Sonin log-line) but is silent on
  its truth. On the project map this is M4 / global Weil positivity with a rate, in the $D_{\log}$ costume.
- Whether "$S\to$ all primes" and "$\lambda\to\infty$" are the SAME limit in the abstract semilocal framing
  (2310.18423) as they are in the support-activated $D_{\log}$ family (2511.22755). Tier-2 identity leans on
  this coincidence; it is clean for $D_{\log}$, looser for free-$S$ semilocal.
- The verbatim 2112.05500 Sonin definition and $W\leftrightarrow S^2$ relation (D-P3): extraction-inferred,
  not source-verified. Cheap to close with a LaTeX read.
