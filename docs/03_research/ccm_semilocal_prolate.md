# The CCM semilocal prolate operator: the one door still ajar, precisely mapped

> Deep-read + build + adversarial verification, 2026-06-24 (SURVEYOR deep-read -> BUILDER -> ADVERSARY).
> Target: the Connes-Consani-Moscovici semilocal prolate operator (arXiv:2310.18423), the only
> quantum-mechanics object the project's QM survey (`experiments/spectral/quantum_mechanics_signature_dossier.md`,
> LEARNINGS #111) flagged as a *live* thread rather than a closed one. Question: is its open positivity
> step identical to M4, or does the operator-algebra framing isolate a genuinely different,
> separately-attackable sub-problem? Raw artifacts: `scratchpad/ccm_prolate/{01_deepread,02_builder,03_adversary}.md`.

## Bottom line

**The door is ajar and now precisely mapped.** The *terminal* object of the CCM strategy is M4
verbatim (the authors call it "the sought for Weil cohomology" -- the polarization on the
Frobenius side of $\mathrm{Spec}(\mathbb{Z})$). But the operator-algebra framing **factors** the road
to it into earlier, genuinely-different, separately-attackable sub-problems that the project did not
previously isolate. The R3.5 status is sharper than "K1 risk": it is **conditionally escaping**. And a
cheap numerical surrogate **cannot** settle it -- a faithful answer requires CCM's actual deferred
operator.

Three precise refinements over the project's prior "CCM semilocal = M4 in operator clothing" read:

1. **The open step factors.** It is not (yet) "prove a hard positivity inequality." The immediate open
   step in 2310.18423, in the authors' own words, is to **construct the operator**: a self-adjoint
   semilocal prolate operator $W_{\lambda,S}$ with an explicit $S$-dependent Jacobi matrix (deferred to
   a forthcoming paper, routed through the metaplectic representation of $\widetilde{SL(2,\mathbb{A}_S)}$),
   whose negative eigenspace is the semilocal Sonin space. Steps (1) construct $W_{\lambda,S}$ and (2)
   identify its negative eigenspace = Sonin are **operator-theory / orthogonal-polynomial** problems,
   not visibly the arithmetic Hodge index, and are separately attackable. Only step (4) -- the trace
   comparison surviving the $S\to\infty$ limit -- **is** M4.
2. **R3.5 status = conditionally escaping**, not a generic K1 risk. The archimedean fragment
   (2006.13771) *proves* the sign can be **geometric** (sourced from the $\rho=1$ derivative jump + the
   Sonin projection, never from the zeros), so it demonstrably walks R3.5's geometric-positivity escape
   clause. The semilocal escape vs K1 collapse turns on a single bit: **can $W_{\lambda,S}$ be
   constructed without inputting the zeros of $\zeta$?** If yes, it escapes R3.5; if the only
   construction routes through the zero locations, it is K1.
3. **The cheap operator-side experiment confirms a faithful build is required.** A
   multiplication-by-density surrogate ([`e1f`](../../experiments/spectral/e1f_ccm_semilocal_prolate.py))
   reproduces the archimedean sign-source faithfully (the $-2$ jump, the Slepian/PSWF spectrum) but
   **cannot** settle the semilocal question: its "projection" is not idempotent, so its eigenvalues are
   not spectral invariants. The real operator (CCM's deferred metaplectic Jacobi matrix) is the
   load-bearing object.

## The two-layer picture (do not conflate)

- **The archimedean theorem (2006.13771, Selecta Math. 2021).** A genuinely PROVEN Weil-positivity
  fragment, at the single archimedean place. It is the **template**. It is **K2-blind**: D-H shares the
  $\Gamma$-factor, so it cannot distinguish $\zeta$ from Davenport-Heilbronn. Its proof is also partly
  **computer-assisted** (a Toeplitz eigenvalue separation).
- **The semilocal program (2310.18423, Ann. Funct. Anal. 2024).** NOT a positivity theorem. It builds
  the Hilbert-space stage on the Euler/Frobenius side (the measure carries $\prod_v L_v$), proves two
  structural lemmas (Sonin-space stability under enlarging $S$; the Hardy-Titchmarsh canonical form),
  and writes a **strategy** to replicate the archimedean proof with primes added. The positivity is an
  **expectation**; the operator it needs is a **candidate to be constructed**.

## A. The archimedean sign source (the proven, non-circular template)

On $L^2(\mathbb{R})_{ev}$, with $\vartheta(g)$ the scaling action, $W_\infty$ the archimedean Weil
functional, and $\mathbf{S}$ the projection onto the **Sonin space** ($\{f : f|_{[-1,1]} = 0$ and
$\hat f|_{[-1,1]} = 0\}$, the orthogonal complement of the phase-space cutoff at the self-dual radius
$\Lambda=1$), the main theorem is (eq. 4): $W_\infty(g * g^*) \ge \mathrm{Tr}(\vartheta(g)\,\mathbf{S}\,\vartheta(g)^*)$
for $g$ supported in $[2^{-1/2}, 2^{1/2}]$ with $\hat g(i/2)=0$.

**Where the sign comes from** (and why it is non-circular):
- **(i) The RHS is manifestly $\ge 0$.** $\mathrm{Tr}(\vartheta(g)\mathbf{S}\vartheta(g)^*) = \mathrm{Tr}(AA^*)$
  with $A = \vartheta(g)\mathbf{S}^{1/2}$ -- a trace of a positive operator, from unitarity of scaling +
  the projection $\mathbf{S}$. **It does not reference the zeros.** This is the non-circular sign source.
- **(ii) The bridge to $W_\infty$** (Thm 4.7): $\mathrm{Tr}(\vartheta(f)\mathbf{S}) = W_\infty(f) + \int f\,\varepsilon$,
  with $\varepsilon$ an explicit prolate-spheroidal correction.
- **(iii) The correction is $-2\,\mathrm{Id} + K$** (Thm 3.6, $K$ Hilbert-Schmidt). The **$-2$ is
  geometric**, not fitted: the jump in $\delta'(\rho)$ from $-1$ to $+1$ at the self-dual scale
  $\rho=1$. Forced by the cutoff geometry, independent of $\zeta$.
- **(iv) The closure is numerical.** $K$ has a single eigenvalue $>1$; imposing finitely many linear
  constraints ($\hat g(\pm i/2)=0$, orthogonality to the bad eigenvector) gives $\mathrm{Id}-K>0$. The
  separation is established by a **Hermitian Toeplitz matrix computation** ($13 < c < 17$ in the refined
  Thm 6.11).

So the archimedean positivity is non-circular (sign from unitarity + the $\rho=1$ jump + a
numerically-separated eigenvalue, none mentioning zeros), but **K2-blind** (it is the $\Gamma$-factor
term D-H shares verbatim) and **partly computer-assisted** (the Toeplitz step).

## B. The radical-conditioning, concretely

The **radical** of the Weil form is the range of the periodization map $\mathcal{E}(f)(u) = u^{1/2}\sum_n f(nu)$ --
the **pole / trivial directions** of the explicit formula (the $s=0,1$ contributions), **not the zeros**.
"Conditioning by the radical" = projecting the test space onto the orthogonal complement of the radical.

| | Archimedean (PROVEN) | Semilocal (EXPECTED) |
|---|---|---|
| Radical-conditioning is a... | hand-built orthogonal **projection** (Gram-Schmidt off range $\mathcal{E}$) + finite linear constraints | **spectral splitting** (orthogonality of positive vs negative eigenspaces of $W_{\lambda,S}$) |
| Implemented... | manually, with a numerical Toeplitz step | "automatically" by the operator's own spectral decomposition -- *if it exists and its negative eigenspace is Sonin* |

## C. Where the prime side breaks

The free trace $\mathrm{Tr}(\vartheta(g)\mathbf{S}_S\vartheta(g)^*) \ge 0$ **survives** adding primes
(semilocal Sonin stability is proven; the measure $dm_S = |\prod_{v\in S} L_v(\tfrac12-is)|^2 ds$ carries
the Euler factors, unbuildable for D-H). What breaks is **everything downstream of "let $\psi_n$ be the
prolate eigenfunctions"**: semilocally **there is no prolate operator yet** (the Jacobi matrix is
explicitly deferred; the operator is a "candidate" via the metaplectic route). So there are no
eigenfunctions to build the correction $\varepsilon_S$ from, no computed jump to source the $-2$, no
Toeplitz computation to separate the bad eigenvalue -- and even granting all that, the separation would
have to hold **uniformly as $S \to$ all primes**, exactly where the Euler product (the $\zeta$-vs-D-H
distinction) lives.

## D. The factoring (M4 at the core, wrapped in non-M4 operator problems)

The open step decomposes, in increasing order of how-much-it-is-M4:
1. **(Construction)** Does $W_{\lambda,S}$ exist as a concrete self-adjoint operator with an explicit
   $S$-dependent Jacobi matrix? -- *Operator-theory / orthogonal-polynomial. NOT M4. Separately attackable.*
2. **(Identification)** Is its negative eigenspace exactly the semilocal Sonin space? -- *Index / spectral-subspace. NOT M4. Separately attackable.*
3. **(Automatic conditioning)** Does the positive/negative spectral orthogonality reproduce the
   Gram-Schmidt-off-$\mathcal{E}$ projection? -- *Borderline.*
4. **(Positivity / $S\to\infty$)** Does the comparison $W_S(g*g^*) \ge \mathrm{Tr}(\vartheta(g)\mathbf{S}_S\vartheta(g)^*)$
   hold with the bad-eigenvalue separation uniform up to $S\to\infty$? -- ***This is M4*** (the #20/3M
   archimedean-dominates-the-growing-Euler-product balance = the arithmetic Hodge standard conjecture).

So the thread is genuinely "ajar," not "open" and not "closed": the terminal positivity is M4, but the
path is factored through a concrete operator-construction problem (steps 1-2) that is well-posed,
non-circular in principle, and not isolated anywhere else in the project.

## E. R3.5 verdict: conditionally escaping

R3.5 (`lean/ZetaRH/R3_5.lean`): a trace-formula NCG with standard spectral identification has positivity
$\iff$ RH (K1-circular), **unless** an independent geometric/intersection input enters (the
geometric-positivity clause is the open escape). The CCM strategy is a trace-positivity argument, so the
risk is K1 -- but the archimedean fragment **demonstrably walks the escape clause**: its sign is geometric
(the $\rho=1$ jump + the Sonin projection), not "spectrum = zeros." For the semilocal case to escape:

> **(†) There exists a self-adjoint semilocal prolate operator $W_{\lambda,S}$, constructed without
> reference to the zeros of $\zeta$, whose negative eigenspace equals the semilocal Sonin space, and
> whose positive/negative spectral orthogonality implements the radical-conditioning.**

If (†) holds with a zero-free construction, the positivity injects an independent spectral-geometric
input and **escapes R3.5** (it would be the operator-algebra realization of the M4 polarization). If the
only available construction inputs $\zeta$, it collapses to K1. **Status: undetermined; the deciding bit
is exactly the open construction (steps 1-2).**

## The experiment (e1f): what it establishes and what it cannot

[`e1f_ccm_semilocal_prolate.py`](../../experiments/spectral/e1f_ccm_semilocal_prolate.py) attempted the
buildable sub-problem with a multiplication-by-density surrogate for the deferred operator.

- **VALIDATED (Tier-1, the anti-vacuity gate).** The harness faithfully reproduces CCM's archimedean
  sign-source: the $-2$ geometric jump is exact (a genuine distributional derivative-jump, verified by
  perturbing the kernel), and the prolate spectrum matches the classical Slepian/PSWF value
  ($\lambda_0 \approx 0.56$ vs $\sim 0.57$) at the self-dual band-limit $c=1$. The construction is
  **K1-clean** (never inputs the zeros) and **D-H is unbuildable by type** (no Euler factors $\Rightarrow$
  no $L_p$ $\Rightarrow$ no measure).
- **DOES NOT SETTLE (Tier-2).** The cheap surrogate **cannot** decide whether the eigenvalue separation
  survives the addition of primes, for three diagnosed reasons (adversary, re-derived): (i) the
  surrogate's "projection" $P_{\text{freq}}$ (multiplication by a smooth density) is **not idempotent**,
  so its "eigenvalues" are not concentration/prolate eigenvalues and are **not spectral invariants** (the
  same place set gives $\lambda_0 = 0.04 / 0.15 / 242$ across normalizations); (ii) any candidate
  inter-prime signal is **below grid noise** ($\sim$30x smaller than the grid wobble); (iii) it is
  **signature-blind** (arithmetic-free bumps reproduce the same effect). Settling the semilocal separation
  requires CCM's **actual deferred operator** (the metaplectic Jacobi matrix of $dm_S$), not a
  multiplication surrogate.

## The faithful build (e1g): the e1f bug fixed; the band-in-$s$ route eliminated by control

[`e1g_ccm_faithful_prolate.py`](../../experiments/spectral/e1g_ccm_faithful_prolate.py) rebuilds the
operator from **genuine** orthogonal projections (the explicit e1f fix), so the eigenvalues are TRUE
spectral invariants this time. On $L^2(\mathbb{R}, du)$ (scaling = translation), with $D(s) = \prod_{v\in S}
L_v(\tfrac12 - is)$ and the Hardy-Titchmarsh isometry $M_S = D^{-1}\cdot F$, the cutoffs are
$P_T = \mathbf{1}_{|u|\le U_0}$ and $P_W^{(S)} = M_S^{-1}\mathbf{1}_{|s|\le S_0} M_S$ (a genuine
projection, $(\text{isometry})^{-1}\cdot(\text{indicator})\cdot(\text{isometry})$), and
$T_S = P_W^{(S)} P_T P_W^{(S)}$.

- **TIER 1 VALIDATES (the reusable result).** The Slepian/PSWF eigenvalues are reproduced at $c = U_0 S_0$
  ($\lambda_0 = 0.567, 0.875, 0.995$ at $c = 1, 2, 4$ vs the sinc-kernel reference $0.573, 0.881, 0.996$);
  $P_T^2 = P_T$ exactly, $P_W^2 = P_W$ to $\sim 10^{-16}$; and **the eigenvalues are normalization-INVARIANT**
  (rescaling $dm_S$ by $\alpha \in \{0.01, 3.7, 10^6\}$ moves them by $\sim 10^{-15}$). The e1f
  non-invariance bug is provably fixed.
- **TIER 2 = a GENUINE NEGATIVE (both parts adversary-confirmed by control, run in-code).**
  - **(A) The band-in-$s$ concentration route is REWEIGHTING-BLIND.** $T_S$ is unitarily equivalent (via
    $M_S$) to the **bare archimedean** concentration operator for **any** nonvanishing multiplier $D$, not
    just the L-factors: since the band indicator $\mathbf{1}_{|s|\le S_0}$ commutes with multiplication-by-$D$,
    $M_S^{-1} P_W^{(S)} M_S = F^{-1}\mathbf{1}_s F$, a diagonal-similarity fact. **Control:** a random
    non-arithmetic multiplier gives the **identical** spectrum ($\sim 10^{-16}$), exactly like the primes.
    So the route is **L-function-blind / D-H-blind by type** (D-H factors would give the identical
    archimedean spectrum) and is **ruled out by elimination**. This is NOT a "prime cancellation" -- the
    whole multiplier is invisible, the phase of $D$ carries no content.
  - **(B) The $dm_S$ orthogonal-polynomial / Jacobi band cutoff is SIGNATURE-BLIND.** Its spectrum DOES move
    under reweighting (the Jacobi $\beta_0$ shrinks $0.61 \to 0.38$ for prime-2), but **control:** a
    non-arithmetic periodic factor ($\omega = 1.37$, not log of a prime) of matched amplitude reproduces the
    same shrink ($\beta_0 \to 0.30$) and the same OP spectrum-drift. So the OP motion is the generic "a
    positive factor shifts a measure's orthogonal polynomials" effect (the e1f-K3 / NP-1 decorative mode),
    **not** an arithmetic signal. The earlier "primes survive here" reading is withdrawn.

**Upshot.** The faithful build validates the archimedean harness and **rules out the band-in-$s$
concentration route** (reweighting-blind) and the degree/Jacobi surrogate (signature-blind) as ways to read
the prime signature. It does **not** touch CCM's actual open step -- the deferred metaplectic /
Hardy-Titchmarsh Jacobi matrix of $dm_S$ -- which remains genuinely open. Full writeup:
`scratchpad/ccm_faithful/01_builder.md`.

## The faithful degree-domain build (e1h): the third cheap route, also signature-blind

[`e1h_ccm_degree_prolate.py`](../../experiments/spectral/e1h_ccm_degree_prolate.py) attacks the *degree*
domain -- the place the `e1g` band-in-$s$ cancellation does not reach -- with the genuine operator
$W_{\lambda,S} = (H+\tfrac12)^2 + \lambda^2 N_S$ ($H$ = the Jacobi matrix of $dm_S$; $N_S$ = the diagonal
degree number-operator). BUILDER -> ADVERSARY, two framings corrected.

- **Archimedean gate VALIDATES exactly (a clean new identity).** The Jacobi matrix of
  $dm_\infty = \pi^{-1/2}|\Gamma(\tfrac14-\tfrac{is}{2})|^2 ds$ **is the Meixner-Pollaczek orthogonal
  polynomials** ($\lambda_{MP}=\tfrac14$, $\phi=\tfrac{\pi}{2}$: $\alpha_k=0$, $\beta_k^2=k(k-\tfrac12)$),
  re-derived independently in 60-digit exact arithmetic to $5\times10^{-60}$. So $H=J_\infty$ is genuinely
  the proven Hardy-Titchmarsh scaling operator -- a citable special-function fact.
- **$W$ is genuine and correctly POSITIVE.** Its spectrum is normalization-invariant ($3\times10^{-13}$,
  the `e1f` gate). It is positive-definite ($n_{\text{neg}}=0$) -- and this is *right*: the actual
  Connes-Moscovici prolate operator $PW_\lambda = -\tfrac{d}{dx}[(\lambda^2-x^2)\tfrac{d}{dx}]+(2\pi\lambda x)^2$
  is itself positive (diagonalized, $n_{\text{neg}}=0$). There is **no** "negative eigenspace = Sonin"
  tension at the prolate operator; that splitting lives in *different* objects -- the concentration
  operator $T$ (the `e1g` $[0,1]$ object, reweighting-blind) and the IR Dirac $D^2$ -- which `e1h` does not
  build. (The first-pass "needs a metaplectic sign-structure" caveat was mis-framed and is withdrawn.)
- **SIGNATURE-BLIND (genuine, hardened).** $W$ is a deterministic function of the moments (the Jacobi
  matrix), so it distinguishes *any* two measures equally and reads moments, not arithmetic. It escapes
  `e1g`'s *specific* failure (it is not reproduced by the $\omega=1.37$ control), but the discrimination is
  **generic**: prime-2's distances to non-arithmetic controls overlap the non-arith-vs-non-arith spread,
  prime-2 is never an outlier. The adversary steelmanned the positive (the inverse risk) with four
  arithmetic-keyed observables and **killed its own $z=+2.29$ false positive** -- a non-arithmetic
  Lorentzian at the identical frequency $\log 2$ scores equally, because a single prime's factor
  $|L_p(\tfrac12-is)|^2$ carries no arithmetic content beyond its frequency $\log p$; the joint
  $\{2,3,5\}$ Mahalanobis test lands in the cloud body (52nd percentile in-code, 18th in the adversary's
  panel), not the tail.

**Upshot.** All **three** cheap orthogonal-polynomial-data routes are signature-blind by three distinct
mechanisms -- `e1f` (non-idempotent, not a spectral invariant), `e1g` (reweighting-blind, L-function-blind),
`e1h` (reads moments, not arithmetic). `e1h` does **not** prove the metaplectic route necessary; it
reinforces it **by elimination** as the one route none of the cheap OP-data surrogates captures. The
deferred metaplectic operator stays the open step. Full writeup: `scratchpad/ccm_degree/01_builder.md`.

## The finite-local metaplectic build (e1i): the deferred route's sign-structure, attacked directly

[`e1i_metaplectic_weil_index.py`](../../experiments/spectral/e1i_metaplectic_weil_index.py) attacks the
route the three OP-data surrogates left un-eliminated. Since e1f/g/h are blind because they build from the
modulus-squared measure $dm_S$, and the metaplectic arithmetic (the Weil index, the quadratic character)
is a **phase/sign**, e1i builds the **finite Weil representation over $\mathbb{F}_p$** as a computable
model of that sign-structure and tests whether it survives the positivity compression. Builder ->
self-corrected false positive -> ADVERSARY (five corrections applied; `scratchpad/ccm_metaplectic/03_adversary.md`).

- **Exact gate (genuine metaplectic structure).** (i) the trace of the normalized metaplectic Fourier is
  the Weil index, $\mathrm{Tr}(F_p)=\varepsilon_p$ ($1$ or $i$ by $p\bmod4$, the Gauss-sum sign theorem,
  to $\sim10^{-15}$, reproduced for all primes $3..59$); (ii) the metaplectic **2-cocycle** $F^2$ vs
  $\rho(m(-1))=(-1|p)\cdot\text{parity}$ is non-trivial exactly for $p\equiv3\bmod4$ (the double-cover
  obstruction). The metaplectic analogue of e1h's Meixner-Pollaczek identity. (The torus
  character-multiplicativity alone would pass with the trivial sign, so the cocycle is the real test.)
- **The result: finite-local signature-blindness.** The scalar Weil index **cancels** in $g^*g$
  ($|\varepsilon_p|^2=1$), and a **concentration-matched, shear-free Arbiter** (a cloud of smooth
  quadratic chirps) places the genuine chirp's Sonin-concentration spectrum in the body for all five
  tested primes (false-negative-probed: a planted outlier reads 100% tail, the genuine reads deep body).
  So the finite-local quadratic sign-structure does **not** survive the finite Sonin positivity
  compression as arithmetic discrimination.
- **Scope (does NOT close this dossier's open step).** This is the finite-local quadratic (Gauss-sum)
  sign-structure at one place, **not** CCM's actual semilocal $W_{\lambda,S}$ (the metaplectic rep of
  $\widetilde{SL(2,\mathbb{A}_S)}$ from the degree-1 Euler factors, with the global $S$-dependent
  coupling). e1i does **not** eliminate the metaplectic route; it sharpens the map: the metaplectic
  arithmetic is genuine, but the place it survives positivity (if anywhere) is the global $S\to\infty$
  assembly, which **is** M4 (steps 1-2 below stay the open BUILDER target). Full writeup: LEARNINGS #118.

## The precise open statement (and the BUILDER target)

> Construct a self-adjoint semilocal prolate operator $W_{\lambda,S}$ (for finite $S \ni \infty$ and at
> least one prime), **without inputting the zeros of $\zeta$**, whose negative eigenspace equals the
> semilocal Sonin space, and whose positive/negative spectral orthogonality implements the conditioning
> by the radical (range of $\mathcal{E}(f)(u) = u^{1/2}\sum_n f(nu)$); then prove the trace comparison
> $W_S(g*g^*) \ge \mathrm{Tr}(\vartheta(g)\mathbf{S}_S\vartheta(g)^*)$ with the bad-eigenvalue separation
> uniform as $S \to$ all primes.

The **first half** (construct $W_{\lambda,S}$ + identify the negative eigenspace) is the
separately-attackable, non-M4, operator-theory sub-problem -- the genuine new BUILDER target, and the one
the cheap surrogate showed needs a *faithful* operator (the metaplectic Jacobi matrix, computed from the
proven Hardy-Titchmarsh canonical form), not a density surrogate. The **second half** (the $S\to\infty$
uniform domination) **is** M4 / the arithmetic Hodge standard conjecture, restated as a uniform
spectral-gap problem, and the operator-algebra dress does not remove it.

## Provenance and fidelity caveats

The deep-read read 2006.13771 and 2310.18423 at theorem/equation level via ar5iv HTML (2112.05500 at
abstract level). Internal operator identities ($-2\,\mathrm{Id}+K$, $\varepsilon(\rho)$, Thm 3.6/4.7) are
high-confidence LLM reads of the HTML, not a line-by-line LaTeX read; the theorem numbers and headline
inequalities (eq. 4/5, Thm 6.11) are double-confirmed against the published abstract. The CCM papers state
"semilocal Weil positivity **implies** RH" (the direction their program would deliver); Weil's criterion
is classically an equivalence. The $13 < c < 17$ archimedean Toeplitz separation is a computer-assisted
step in the *template* -- a non-trivial extra burden for any semilocal replication (the separation must
hold uniformly as $S \to \infty$, a concrete place a stealth window could hide). Cross-refs: `#111`
(the QM run), `#114` (this dig), `#20`/`#34`/M2.6 (the archimedean-dominates-prime balance = the M4 core),
`R3_5.lean` (the no-shortcut wall + the geometric-positivity escape clause),
`research_directions/08A_rosati_standard_conjecture.md` (M4), `spec_z_cohomology_landscape.md` (the
universal gap).
