# The CCM semilocal prolate operator: the one door still ajar, precisely mapped

> Deep-read + build + adversarial verification, 2026-06-24 (SURVEYOR deep-read -> BUILDER -> ADVERSARY).
> Target: the Connes-Consani-Moscovici semilocal prolate operator (arXiv:2310.18423), the only
> quantum-mechanics object the project's QM survey (`experiments/spectral/quantum_mechanics_signature_dossier.md`,
> LEARNINGS #111) flagged as a *live* thread rather than a closed one. Question: is its open positivity
> step identical to M4, or does the operator-algebra framing isolate a genuinely different,
> separately-attackable sub-problem? Raw artifacts: `scratchpad/ccm_prolate/{01_deepread,02_builder,03_adversary}.md`.

## Bottom line

> **Update (2026-06-30, e1j): the metaplectic front is now EXECUTED and closed as a local construction.**
> The metaplectic route decomposes into three local channels (geometry / measure / sign); each was folded
> with its genuine arithmetic and shown locally blind (geometry = a modulus-blind ultrametric ladder;
> measure = reads magnitude $\sim 1/m$ and is reweighting-invisible; sign = cancels in $g^*g$). No local
> channel carries the zeta-vs-D-H discrimination; it is pinned at the global $S\to\infty$ assembly = M4.
> Adversary-verified (PASS). See "The metaplectic front, executed (e1j)" below. The rest of this dossier
> is the map that led there.

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

## The metaplectic front, executed (e1j): the route decomposes into three local channels, all blind

[`e1j_semilocal_metaplectic.py`](../../experiments/spectral/e1j_semilocal_metaplectic.py) executed the
one door e1f-e1i left un-attacked -- CCM's actual metaplectic construction -- and, after an adversary
round, delivered the honest closure: **the metaplectic route has no local channel that carries the
zeta-vs-D-H discrimination.** BUILDER $\to$ ADVERSARY (`experiments/spectral/_e1j_adversary.md`, six axes)
$\to$ faithful rebuild $\to$ ADVERSARY re-verification (**PASS**).

**The adversary round mattered.** A first build claimed to construct $W_{\lambda,S}$ and close the front
via a "cross-modulus blindness" test. The ADVERSARY broke it: the decider read only the rank-1 overlap of
a self-dual subgroup with its Fourier dual (modulus-independent for **every** integer by elementary
harmonic analysis, so the test could only return "blind"), and -- the sharpest finding -- the one object
that could carry arithmetic, the Tate depth/valuation number operator $N_p$ with $L_p$ as generating
function, was **dead code** (defined, printed as a passing gate, never connected to the verdict). The
load-bearing test was never run. The rebuild runs it.

**The three-channel decomposition (each folded with its genuine arithmetic; each locally blind).** CCM's
$W_{\lambda,S}$ combines exactly three ingredients, which the four surrogates isolated:

| Channel | What it is | Folded-in test (e1j) | Verdict |
|---|---|---|---|
| **Geometry** (Weyl/Fourier + ultrametric balls) | the adelic phase space $\prod_v L^2(\mathbb{Q}_v)$, $p$-adic balls = subgroups | the ball concentration $P_T(p^a)P_W(p^b)P_T$ is rank-1 with eigenvalue **exactly $p^{a+b}$** (or perfectly localized); the spectrum is **always** exact powers of $1/p$, **never** a continuous plunge (verified over all radii) | **BLIND** -- modulus-blind (powers of $1/m$ for any $m$) = geometry, not arithmetic. *e1j's genuine NEW content.* |
| **Measure** ($dm_S = |\prod_v L_v|^2$) | the L-factor spectral weight (the Euler/arithmetic content) | B1: $N_p$ **wired in**, depth-weighted top eigenvalue $= 1/m$ exactly (same for prime $m$ and composite $m'$) $\Rightarrow$ reads magnitude, not primality (= e1h). B2: band-in-$s$ concentration with genuine $L_p$ $\equiv$ non-arith control $\equiv$ bare, to $\sim10^{-15}$ (the e1g diagonal-similarity fact, genuine $L_p$) | **BLIND** -- reproduces e1g/e1h with the genuine $L_p$ folded in |
| **Sign** (Weil index, quadratic unipotent) | the metaplectic phase $\varepsilon_p$ | the scalar Weil index cancels in $g^*g$ ($|\varepsilon_p|^2=1$) | **BLIND** (= e1i) |

**The new structural fact (geometry channel).** The $p$-adic ball concentration operator has spectrum
**always in $\{$exact powers of $1/p\} \cup \{1\}$, never a continuous boundary layer** -- the sharp
ultrametric uncertainty, the exact opposite of the archimedean continuous Slepian plunge (where the $-2$
jump and the Sonin correction live). At a finite place there is no prolate boundary layer at all; the
entire prolate-spreading sign-source is archimedean. This ladder is modulus-blind, so it carries geometry,
not arithmetic.

**The closure.** These three channels are the local content of the metaplectic route (the standard
Weil-representation factorization); each is locally blind, and no fourth blind-breaking local channel was
found. So the zeta-vs-D-H discrimination is carried by **no** local or finite-semilocal channel -- it is
the global $S\to\infty$ uniform assembly = **M4** / the arithmetic Hodge standard conjecture. The
construction is **K1-clean** (zero-free), and **D-H is unbuildable by type** for the measure channel (no
Euler product $\Rightarrow$ no $L_p$). This is the honest closure of the front: *not* "e1j built
$W_{\lambda,S}$ and it is blind," *but* "the metaplectic route has no local channel beyond
$\{$geometry, measure, sign$\}$, and every one is locally blind, so the content is global = M4." Two honest
footnotes: the "no fourth channel" completeness is empirical, not proven; the measure channel reproduces
the prior e1g/e1h findings faithfully (with genuine $L_p$), it does not discover a new escape. Full
writeups: `scratchpad/ccm_semilocal/01_builder.md`, `experiments/spectral/_e1j_adversary.md`, LEARNINGS #135.

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

## Addendum 2026-07-02: the open statement above is superseded (survey, LEARNINGS #153)

A SURVEYOR pass against the Nov 2025 papers ([`reading_notes/ccm_zeta_cycle_density_gate.md`](reading_notes/ccm_zeta_cycle_density_gate.md); arXiv 2511.22755 + 2511.23257, with 2106.01715 / 2310.18423 / the Connes-Moscovici PNAS paper) found this dossier's "precise open statement" stale in two places:

- **The deferred metaplectic Jacobi-matrix operator $W_{\lambda,S}$ is bypassed.** The new family $D^{(\lambda,N)}_{\log}$ (rank-one perturbation, Caratheodory-Fejer self-adjointness) carries an exact, unconditional determinant formula $\det_{reg}(D^{(\lambda,N)}_{\log} - z) = -i\lambda^{-iz}\hat\xi(z)$ with real zeros. The open front has moved to the Section-7 uniform convergence $\hat\xi_\lambda \to \Xi$, which the authors call "the main remaining obstacle to our approach to RH".
- **The deciding bit ("built without inputting the zeros?") is YES at the assembly level** (inputs: $\theta'$, the pole term, $\Lambda(n \le x)$), but the R3.5/K1 question RELOCATES rather than closes: the perturbation vector is the ground state of the truncated Weil form, whose global positivity is RH-equivalent. ADVERSARY should re-run R3.5 on the 2511 shape.

Density-gate context from the same session (#151-#153): the door satisfies the eigenvalue budget with ONE spectral circle of circumference $\log x = \log(T/2\pi)$ while consuming Euler data to $n \le x = T/2\pi$ (the two-meter law); the lattice map $\mathcal{E}$ absorbs the surplus, which is where the Beurling discipline's fourth clause (lattice-consuming, #152) is paid.

## Addendum 2026-07-02 (second): the two #153 handed-forward audits executed (ADVERSARY)

Full note: `scratchpad/ccm_dlog_adversary/01_adversary.md` (untracked); draft LEARNINGS #154 there. Two verdicts on the $D^{(\lambda,N)}_{\log}$ family:

1. **R3.5/K1 re-run: the wall is MET, not escaped, at exactly the Section-7 step.** The discrimination geography is three-level: input level real (D-H lacks the $\Lambda$ stream; the Beurling fake lacks the $\theta'$-density AND the $\mathcal{E}$-bridge, so #152's fourth clause is paid at TWO sites); finite-spectrum level none (Thm 5.10(iii) makes all finite-cutoff determinant zeros real unconditionally, so finite reality carries zero bits about RH: information-free finiteness, the TOTAL form of the stealth window; an off-line zero would show only as convergence non-uniformity, needing $\lambda^2 \approx \gamma_0/2\pi > 5\times 10^{11}$ by Platt-Trudgian); limit level all of it (the Section-7 identification instantiates `TraceFormulaNCG` and `r3_5_no_shortcut_theorem` applies by `rfl`). K1: convergence $\Rightarrow$ RH proven (Hurwitz), converse unproven: not circular, but RH-hard, and the only identified sufficient input (uniform ground-state control of the truncated Weil form) is an RH-equivalent positivity with a rate. The escape clause is NOT walked: the perturbation vector is the Weil form's own variational vector, not an external geometric sign source. **Section E's condition (†) is RETIRED** (the metaplectic operator is bypassed); the new escape condition is **(††): a zero-free, geometry-sourced proof of the uniform $(N,\lambda)\to\infty$ control not routed through global Weil positivity.** Door status: wall-met-at-one-step (was: conditionally escaping).

2. **W6-vs-#143 gate: NOT a W6 hit; a determinant-class SHELL around a #143 core.** Determinant-class: yes, exact at finite cutoff (first such object in the ledger). Pole budget: half-independent (the $s=0,1$ + $\Gamma$ side is imported from the proven explicit formula). Spectrum budget: installed, not computed (count and density fixed by the truncation choice; RvM only at the edge), and the spectral side runs through the argmin of the truncated Weil form: a variational, positivity-sourced step where a genuine W6 computes by symmetry. So the finite determinant formula presupposes CF self-adjointness (#143 branch) and the third WATCH item does not ring. **Coincidence finding:** at this family the W6 upgrade (variational vector replaced by the symmetry-computed $\mathcal{E}$-direction, the global Weil form's radical) and the M4 statement (uniform ground-state control) are the SAME statement, verbatim the Section-7 bridge: the trace-formula and polarization faces of #148's four-face map coincide at one published open step. Upgrade spec (all zero-free): the trivial circle budget + rank-one interlacing ($\pm 1$) + the $\mathcal{E}$-absorption count proven family-uniform (the Slepian/prolate "$1+\nu(\lambda^2)$" count, the Betti-number analogue) + a Hamburger-type converse pin **(DONE 2026-07-11: e1m, LEARNINGS #160, addendum below; the bare budget form is proven FALSE, the corrected form is classical Hamburger with the abscissa clause, net = reformulated not reduced; e1m also proves the trivial circle budget in-build, so three of the four ingredients are executed and rank-one interlacing is the one untouched)** **(UPDATE 2026-07-17: ingredient (2) DONE, [`e1p_rank_one_interlacing.md`](../../experiments/spectral/e1p_rank_one_interlacing.md), LEARNINGS #165, adversary PASS_WITH_FIXES; the ledger is fully retired: interlacing holds as a measured family-uniform profile ($\le 2$, one $\sqrt{13}$ point at 3), lands on the #143 side, and the rank-$\le 2$ pole block is the one genuine Weyl/Cauchy instance, input-faithful but RH-blind)**; even then the residual open step is the uniform det-class limit = M4, cleanly isolated.

Handed forward (cheap): ~~the CF-on-D-H probe (does Caratheodory-Fejer run on the D-H coefficient stream; read 2511.23257 in full first), the D-H twin as a Section-7 convergence-failure testbed at $\gamma \approx 85.7$~~ **DONE 2026-07-10 (e1k, LEARNINGS #158, below)**, ~~and the absorption-count numerical shadow (still open)~~ **DONE 2026-07-10 (e1l, LEARNINGS #159, below)**. All three #154 handed-forward probes are now discharged.

## Addendum 2026-07-10: the CF-on-D-H probe + the Section-7 D-H testbed EXECUTED (e1k, LEARNINGS #158)

Full record: [`experiments/spectral/e1k_dh_dlog_testbed.md`](../../experiments/spectral/e1k_dh_dlog_testbed.md) (+ `.py` / `.npz`); reading notes [`reading_notes/CCM-2025-Dlog-family.md`](reading_notes/CCM-2025-Dlog-family.md) + [`reading_notes/CCM-2021-Prolate-Sonin.md`](reading_notes/CCM-2021-Prolate-Sonin.md). BUILDER + ADVERSARY (verdict PASS_WITH_FIXES; genuine, `discrimination_real = FALSE by design`). Two of the three #154 handed-forward probes are now discharged; the frontier is UNMOVED.

- **CF-on-D-H: it RUNS (NOT a non-mimicry exemption).** The Caratheodory-Fejer self-adjointness gate (2511.23257 Thm 1.2/6.1) needs only real + even + lower-bounded + simple-lowest-eigenvalue; none references an Euler product. D-H supplies a genuine log-derivative stream $\Lambda_{DH}(n)$ via the Dirichlet recursion $\sum_{d\mid n}\Lambda(d)c_{n/d} = c_n\log n$ with the period-5 comb $c_n = (1,\kappa,-\kappa,-1,0)$: dense (all $n\ge2$), non-multiplicative, sign-changing. D-H and $\zeta$ enter through IDENTICAL code, differing only in the comb and the rank-$\le2$ pole (present for $\zeta$, absent for entire D-H). So $W_{\lambda,S}$'s finite-cutoff descendant is buildable for D-H by type.
- **Finite reality is INFORMATION-FREE, confirmed on the D-H twin.** The D-H operator is G-self-adjoint to residual $4.1\times10^{-6}$ and its physical eigenvalues are real to $7.8\times10^{-30}$ (N=6, dps=30), matching D-H's ON-LINE zeros. The same Thm 5.10(iii) manufactures reality for both twins with no arithmetic input = the TOTAL form of the stealth window (#153/#154). Even AT the height of D-H's genuine off-line zero ($s=0.808+85.699i$, i.e. $z=85.699-0.308i$, COMPLEX) the finite operator returns a REAL eigenvalue ($85.7828$, $\mathrm{Im}\sim-2\times10^{-12}$), never the complex zero (the sharpest form of the discipline reached to date).
- **The discrimination is quarantined to the Section-7 uniform limit = M4.** The off-line zero can only emerge as a $\lambda\to\infty$ convergence non-uniformity (Hurwitz contrapositive: real-zero entire functions cannot converge uniformly to $\Xi_{DH}$ near $\gamma\approx85.7$); the direct test needs $\lambda^2\gtrsim5\times10^{11}$ (Platt-Trudgian), out of reach, and the archimedean stealth suppression $e^{-(\pi/4)d\gamma}\sim10^{-30}$ keeps finite reality exact by design. This is exactly the #148/#154 wall (Section-7 uniformity = uniform truncated-Weil ground-state control = global Weil positivity with a rate), now confirmed even after pushing the spectral range PAST the off-line height.
- **C3 grounded (#157).** Every Section-7 object lives on the real log-line = C3's archimedean-injection object; the $\lambda\to\infty$ limit injects all primes via $\{p\le\lambda^2\}$, so Section-7 uniformity IS archimedean-injection uniformity (C3 Tiers 1-2 confirmed with numerical grounding; Tier 3 = logical equivalence stays open = M4).
- **Honest limitations (not claims).** The $\zeta$ pole-term realization is imperfect (G-self-adjoint residual $2.5\times10^{-2}$, ghost complex eigenvalues at 30 digits) so D-H reconstructs cleaner only because it is entire; the archimedean factor was corrected to D-H's own $\Gamma((s+1)/2)$ (the reading note's "shares $\zeta$'s $\Gamma$ factor" is imprecise); the ground state sits on a near-degenerate zero-margin cluster where the "even + simple" CF hypothesis is marginal (global min is ODD at several cutoffs = the Remark 2.3 caveat, surfaced).

## Addendum 2026-07-10 (third): the absorption-count numerical shadow EXECUTED (e1l, LEARNINGS #159)

Full record: [`experiments/spectral/e1l_absorption_count.md`](../../experiments/spectral/e1l_absorption_count.md) (+ `.py` / `.npz`). BUILDER + ADVERSARY (verdict PASS_WITH_FIXES; `count_genuine = FALSE`, `w6_143_read_sound = TRUE`). This discharges the **third and last** of the #154 handed-forward probes; all three are now DONE and the frontier is UNMOVED.

- **The upgrade spec's absorption ingredient is now MEASURED, and it lands on the #143 side.** The #154 upgrade spec (line 357) named four zero-free ingredients that would make W6 ring; ingredient (3), the $\mathcal{E}$-absorption count proven family-uniform (the Slepian/prolate "$1+\nu(\lambda^2)$" count, the Betti-number analogue), is the one measured here. It IS a real, family-uniform, computed asymptotic in $\lambda$: the windowed physical-zero count $1+\nu(\lambda^2)$ tracks the RvM / circle-lattice law $2\lambda^2\log\lambda = (T/2\pi)\log(T/2\pi)$ at $T = 2\pi\lambda^2$ (D-H fits it cleanly, $a=0.936$, rms 1.6%; $\zeta$ noisier, $a=0.804$, the rank-2 pole perturbs the low-$\lambda$ counts), and the genuine Slepian concentration operator (e1g, $c = 2\pi\lambda^2$) reproduces the Shannon count $2c/\pi = 4\lambda^2$ EXACTLY ($52/36/64/100$). So the W6-shaped observable (a family-uniform count) exists numerically.
- **But it is the BLIND count, installed by the window, not computed by symmetry.** The RAW un-windowed physical count TRACKS the truncation dimension $N$ (slope $d\nu/dN = +0.94$ zeta / $+1.00$ D-H, because Thm 5.10(iii) makes the finite-cutoff zeros real up to an O(1) complex-ghost residual). The plateau appears only once the external two-meter window $T = 2\pi\lambda^2$ is imposed, and $n_{\rm win} = T_{\rm win}/\phi$ is a lattice IDENTITY forced by $\phi\,N^* = T_{\rm win}$ exactly ($\phi = \pi/\log\lambda$), so the RvM-vs-Shannon fit confirms the fixed lattice spacing but CANNOT discriminate computed-by-symmetry from installed-by-window; e1g's reweighting-blindness (a random non-arithmetic multiplier gives the identical spectrum) confirms it is the blind archimedean/geometry count. This is exactly the #143-shell reading of line 357: **spectrum budget INSTALLED, not computed**; the count is the geometric Slepian/RvM floor, not a Betti count the operator computes by its own symmetry, and it carries zero bits about RH.
- **D-H blind; the residual is unchanged.** The count law does not discriminate $\zeta$ from D-H (same law, same slope verdict, same Shannon $4\lambda^2$; D-H fits the RvM law CLEANER because it carries no pole). Measuring ingredient (3) does NOT close the W6 upgrade and does NOT move any wall: the residual open step is exactly what it was, the **uniform det-class limit = M4** (Section-7), cleanly isolated. The other three upgrade-spec ingredients are untouched.
- **Caveats inherited from e1k.** Faithful reimplementation not the paper's exact operator; razor-thin positivity margin $\varepsilon\approx3\times10^{-5}$; imperfect $\zeta$ pole term (O(1) complex ghosts, spectrum not perfectly real). Robust: the leading law and the slope verdict; NOT robust: the exact integers $n_{\rm neg}$, $n_{\rm win}$ (O(1)-fragile between dps 15 and 25).

## Addendum 2026-07-11: the Hamburger-type converse pin EXECUTED (e1m, LEARNINGS #160)

Full record: [`experiments/spectral/e1m_hamburger_pin.md`](../../experiments/spectral/e1m_hamburger_pin.md) (+ `.py` / `.npz`). SURVEYOR + BUILDER + ADVERSARY (verdict PASS_WITH_FIXES). This executes upgrade-spec ingredient (4) from the 2026-07-02 addendum above; the same probe proves ingredient (1) (the trivial circle budget) in-build via the exact lattice tail $\hat\xi(\phi m) = 0$ for $|m| > N$, so THREE of the four zero-free ingredients are now executed and **rank-one interlacing (2) is the one untouched item** (DONE 2026-07-17: [`e1p_rank_one_interlacing.md`](../../experiments/spectral/e1p_rank_one_interlacing.md), LEARNINGS #165; the #154 ledger is fully retired). The frontier is UNMOVED.

- **The bare pin is FALSE, proven.** FE + order 1 + the full-plane RvM budget do NOT pin $\Xi$: an explicit K1-clean relocation pair on the smooth-inverted RvM comb (gamma data only, no zero consumed) is even/real/order-1 with identical counting functions to O(1) yet pointwise distinct, and the solution family is infinite-dimensional. The budget has real teeth (it kills FE-preserving multiplicative perturbations, measured excess 18 vs predicted 18.1, and must be stated full-plane), but uniqueness needs zero LOCATIONS, which counting can never supply. The "budget-forced identification" reading of ingredient (4) is dead as stated.
- **The corrected pin is classical Hamburger (1921), abscissa included.** H4 = the unpacked $f(s)$ is a Dirichlet series absolutely convergent for $\mathrm{Re}\,s > 1$ (K-P survey arXiv:1605.02354 Thm 2.1); the ADVERSARY fixed a real bug where H4 was stated "on a half-plane", exactly the Knopp-insufficient form (Invent. Math. 117 (1994)). No budget-substitution converse theorem exists in the literature (surveyor-verified absence); the nearest relatives (Ki, Adv. Math. 231 (2012); Hu-Li arXiv:1610.01583) consume zero SETS plus a $\sigma\to+\infty$ normalization the finite object fails.
- **The A1 net: REFORMULATED, NOT REDUCED.** The corrected pin's one open clause (Dirichlet-face inheritance: the limit carries H4 with its growth package) is, conditional on the limit existing, EQUIVALENT to the identification $F = c\,\Xi$ it replaces (forward Hamburger; backward via $\zeta$'s own series). Zero net logical reduction of the Section-7 statement. The genuine gain is a POSITIVITY-FREE proof surface for the identification half: attack via $\det_{reg}(D^{(\lambda,N)}_{\log} - z) = -i\lambda^{-iz}\hat\xi(z)$ + the prime comb, zero-free, instead of the variational ground state; the bare counting route into the identification is proven closed.
- **Finite-$\lambda$ inheritance is FE-only, and the FE face is information-free.** The e1k harness ENFORCES evenness by selecting the lowest even eigenvector (`even_frac = 1.00000` at all six builds), so the tiny FE defects are an even-simplicity/numerics monitor (a Remark 2.3 odd-minimum event would fail the face at O(1)); the finite types $\approx\log\lambda$ DIVERGE, so the LIMIT's growth/entirety belongs to the open package too; the budget face is two-regime and type-aware (own-conductor RvM core below $\sim T_{\rm win}/5$, lattice spacing above; pole-ablation surprise: the low-band fill is the lattice floor, and the pole term pulls the edge count toward RvM); the Dirichlet face is blocked at every finite cutoff by Paley-Wiener (tracking window $t \sim 6..7$, escape rate $\to \pi/4$: e1k's stealth window quantified from the modulus side).
- **Disciplines.** Beurling fails NAMEABLY: no additive lattice $\Rightarrow$ no Poisson $\Rightarrow$ no theta FE (defect 0.37) $\Rightarrow$ the budget is underivable and the Hamburger engine unfueled; the pin's proof engine IS lattice duality, so the #152 fourth clause is paid by construction. D-H is excluded by TYPE (own conductor-5 FE exact to $1.7\times10^{-30}$ vs Riemann-type defect 1.72; budget surplus 20.7 zeros at $T = 85.699$).
- **Gloss note (e1m surveyor D2, banked here because this dossier carries the gloss).** CCM's own Section 7 wording is "identify the true minimal eigenvector with the prolate ansatz"; the words "positivity" / "Weil positivity" do not appear there (fetched-absence). This dossier's "RH-equivalent positivity" reading of that step is the repo's gloss via the Bombieri-Weil equivalence: well-argued, but not attributable to CCM verbatim.
- **Frontier: UNMOVED.** The residual is (a) the uniform det-class limit = M4 and (b) the inheritance clause = the identification restated in lattice vocabulary. New watch/attack coordinate: can the determinant identity + the prime comb produce H4 for the limit without passing through Weil positivity?

## Addendum 2026-07-11 (later): the prime-comb face measured + the one-sided reroute (e1n + the Landau dossier, LEARNINGS #161)

Full records: [`experiments/spectral/e1n_prime_comb.md`](../../experiments/spectral/e1n_prime_comb.md) (+ `.py` / `.npz`, 31/31, adversary-reproduced) and [`landau_one_sided.md`](landau_one_sided.md). One ADVERSARY round over both, PASS_WITH_FIXES twice. This executes the "determinant identity + prime comb" attack coordinate the addendum above named; the frontier is UNMOVED, sharpened at four points that annotate THIS dossier.

- **The escape law is DERIVED (the e1m soft spot closed).** The $t_{\rm dir} \sim 6..7$ constancy flagged above as "observed, not derived" now has a mechanism, and it SPLITS: on the clean builds it is a plateau crossing (the signal $|c\,\Xi(2+it)|$ decays at the exact completed-factor rate, closed form $\mathrm{Im}[d\log\mathrm{Fac}(2+it)] = \pi/4 - 5/(2t) + O(1/t^2)$, adversary re-derived; the crossing with the object's own Paley-Wiener plateau is predicted from object-only data to 0.25-0.5, non-circular); on the fill-dressed builds the corridor trips on the dressing polynomial BY ARTIFACT, and the ghost-quotiented $\lambda = 2.6$ object tracks PAST $t = 14$ at floor $2.1\times10^{-4}$. So $t_{\rm dir}$ grows without bound iff the floor $\to 0$ = the Section-7 identification on the line, in window clothing, and part of the observed cap is REMOVABLE dressing, not convergence failure.
- **The fill counts are dps-branch-specific (annotates the e1m/e1l readings above).** The lam 2.6 fill (+3) supports a `c Xi x (three real zero factors)` structure to 2-3e-4, N-robust at dps 25 (N = 14/16/18), but at dps 15/35 the SAME $(\lambda, N)$ point builds fill-free at the ordinary 3-5e-2 floor: the fill (and e1m's 0/3/0/5 counts) is a property of the dps-25 BRANCH of the near-degenerate ground-state family (e1l's O(1) integer fragility acts as a branch selector), not of $\lambda$. Branches of one point differ 100x in $\Xi$-proximity; if dressed branches are generally `dressing x Xi`, Section-7 convergence becomes a dressing-migration statement (handed forward).
- **The comb face is RH-blind at finite lambda (the #158 class, confirmed on a new face).** The D-H twin's comb face has identical fidelity ($|D|$ 0.030/0.034 = zeta's clean class), is input-faithful (6.2x cross-comb contrast), and reads back its own input comb: nothing at finite $\lambda$ knows which twin satisfies RH. The Beurling control is two-regime: nameable failure at long windows (clause = the integer lattice), BLIND at the archimedean-capped accessible window (the fake sits within ~2x of the object's own comb error): the #152 fourth clause is payable only in the limit, i.e. the C3 stealth window measured from the comb side.
- **The S4/R1 reroute reading (the Landau interlock).** The #145 one-sided residue is a PROVEN classical translator (one-sided $\psi(x) \le x + C_\epsilon x^{1/2+\epsilon}$ for all $\epsilon$ forces RH; Euler-gated at comb nonnegativity, so D-H cannot pose it and Beurling runs it vacuously). Its bridge to THIS family is layer-dependent (the adversary's L1 reconciliation): at the input layer the below-horizon transfer is exact and VACUOUS (the injected stream IS the true comb below $\lambda^2$); at the built-object layer it is FALSE without an error term (comb-mass errors +4-9 percent; ~3 percent floor not shrinking over $\lambda \in [2.2, 3.6]$). What survives is the proof-engine reading: whether the $D_{\log}$ carrier can PROVE the $\lambda$-uniform one-sided bound operator-theoretically = a Spec(Z)-Stepanov / S4 on this carrier, rerouting the finite-$\lambda$ wall from M4 (polarization) to R1's S4 face, POSED not answered. The measured mixed-sign comb error (+, +, +, - across builds) locates the obstruction at exactly the $\lambda$-uniformity joint. Tracked in [`sourcing_gap_r1.md`](sourcing_gap_r1.md) as the fourth analytic shape of the R1 slot.

## Addendum 2026-07-11 (later still): the S4 skeleton posed on the carrier and the slot measured empty (e1o, LEARNINGS #162)

Full records: [`experiments/spectral/e1o_s4_carrier.md`](../../experiments/spectral/e1o_s4_carrier.md) (+ `.py` / `.npz`, 19/19 full and quick, adversary-reproduced) and the promoted arc dossier [`s4_carrier_audit.md`](s4_carrier_audit.md) (survey + DMV kill + spec). One ADVERSARY round, PASS_WITH_FIXES twice, several claims upgraded. This executes the first round of the S4/R1 question the addendum above rerouted to; the frontier is UNMOVED. Four points that annotate THIS dossier:

- **Horizon consonance (structural tier).** The classical Beurling-Selberg majorant pairing against the full von Mangoldt comb DIVERGES at every exponential type, and family-universally: no band-limited majorant of ANY family evades it (Krein factorization + the Cartwright log-integral cap real-axis decay strictly below $e^{-u}$, against the $e^u$ comb density). A horizon device is therefore MANDATORY for any band-limited one-sided pairing, and the carrier's injection horizon $p \le \lambda^2$ is exactly such a device: the CCM structure is FORCED by the counting skeleton it would have to serve. An observation about shape, not progress on the bound.
- **The budget is not the wall.** The dimension needed to push the majorant excess to $x^{1/2}$ resolution is $x^{1/2}\log x$ against the carrier's Shannon budget $4x$ at its horizon window (e1g/e1l's $4\lambda^2$): ratio $3.5\times10^{-3}$ at $x = 10^6$, scaling to 0. Unlike over $\mathbb{F}_q$, where the degree budget binds and Frobenius relaxes it, the binding constraint here is that the smoothed prime sum at that type is unconditionally UNEVALUABLE (the explicit-formula zero side IS location data). The S4 absence is a mechanism shortfall, not a budget shortfall.
- **The S4 absence on this carrier = the incommensurability of $\{\log p\}$ (mechanism tier).** Multiplicity is FULL PRICE at the log-prime comb for every decimation subspace at every $\lambda$ (cost ratio 1.000, well-conditioned) and for the adversary's five smarter families, while commensurate AP combs collapse EXACTLY (ratio $1/J$, $10^{-14}$ exact) and the per-prime orbit $\{k \log p\}$ on $\mathbb{R}/(\log p)\mathbb{Z}$ is cheap at the ideal rate (0.20 = the multiplicity avatar of #153's per-prime W6 exactness). Frobenius = commensurability of the value group; the missing glue across incommensurable circles is the additive lattice, the same clause #62/#152/#153/#156 met from four other sides. The forcing spec is banked in the dossier (a lattice-consuming $\lambda$-uniform rank collapse at $\{k \log p\}$ at cost $o(M)$, restoring the linear Stepanov pairing). [AMENDED 2026-07-31, LEARNINGS #172: read "the missing glue" here as "the missing glue of the required class", not as a uniqueness claim. There are exactly TWO known glues across incommensurable circles, the additive lattice and Lee-Yang stability of a multivariate polynomial (Kurasov-Sarnak arXiv:2004.05678 Thm 1, arbitrary reals $b_j > 1$; classified by Alon-Cohen-Vinzant arXiv:2303.03201 Cor. 1.4). The second consumes no lattice and takes an arbitrary multiplicative generator set as input, so it is Beurling-generic by its own hypotheses and the DMV screen kills it BY NAME: the lattice-consuming clause is CONFIRMED with a better reason, not weakened. Tension D3 (Lee-Yang polarity) logged open.]
- **Handed forward: the Sonin projector.** The ONE candidate family the probe could not test is the true operator eigenbasis / Sonin-space projector (no Sonin projector exists in the e1k/e1n caches; building one is a new experiment). The surveyor's parallel finding: the one-sided extremal literature (Carneiro-Littmann, solved in de Branges spaces) and the Sonine-zeta literature (Burnol, Connes-Moscovici) are both alive and DISJOINT in print, so posing the one-sided extremal problem in the CCM Sonin space is unclaimed territory, with its well-posedness itself open.

## Addendum 2026-07-12: the Sonin corner closed for buildable families + the W6 count/location split + the #154 probe list COMPLETE (e1r + e1s, LEARNINGS #169 (parallel line, merged 2026-07-22; IDs renamed e1p->e1r, e1q->e1s))

Full records: [`experiments/spectral/e1r_sonin_projector.md`](../../experiments/spectral/e1r_sonin_projector.md) (+ `.py` / `.npz`, 10/10 full and quick) and [`experiments/spectral/e1s_rank_one_interlacing.md`](../../experiments/spectral/e1s_rank_one_interlacing.md) (+ `.py` / `.npz`, 14/14 full), plus the Lean floor [`lean/ZetaRH/S4Carrier.lean`](../../lean/ZetaRH/S4Carrier.lean). Three parallel tracks, one ADVERSARY round (e1r/e1s PASS_WITH_FIXES, Lean PASS). This discharges the two frontier NEXT items the addendum above handed forward (the Sonin projector; rank-one interlacing = the last #154 upgrade-spec item); the frontier is UNMOVED.

- **The Sonin corner is CLOSED for every buildable family (e1r).** The one family e1o could not build is the carrier's OWN spectral data, and it supplies no S4 mechanism. Structural preemption: the Weil form Q is Hermitian, so its full eigenbasis is UNITARY and evaluation on it is unitarily equivalent to the standard basis (singular values match to 3.6e-15); the full eigenbasis cannot manufacture collapse in principle, and only selection or a non-orthogonal basis can differ. Neither does: the leading-J Weil energy eigenbasis is FULL PRICE at $\{\log p\}$ in all 12 cells (with the mild low-energy alignment having the WRONG SIGN for S4, resolving the comb rather than escaping it, and not lattice-specific), the non-orthogonal $D_{\log}$ operator eigenbasis is full price, and the E-map shift-sum diagonal proxy (the partial-zeta multiplier $S_m$, the lattice-carrying half) is full price with drop(perturbed) $= 0$; the aperiodic $x^{1/2}$ E-map weight is honestly recorded UNBUILDABLE on the compact log-circle (the faithful $\mathcal{E}$ lives on the non-compact line). The ONE rank drop (the Sonin projection, the low-concentration eigenspace of the central-window prolate) is a SPATIAL-WINDOW MIRAGE: it tracks the number of comb points inside the vanishing window W, PERSISTS under perturbed logs, and the out-of-W comb is full rank. The ADVERSARY's three window constructions confirmed the diagnosis by execution (empty comb-free window -> drop 0; perturbing only the in-window logs while keeping them in-window -> drop persists exactly, so the drop is spatial not arithmetic; top-k window -> drop tracks $\#$comb-in-W). `s4_spec_answer = NEGATIVE, closed for every buildable family`; the SOLE unbuilt variant is the faithful metaplectic self-dual Sonin projector of arXiv:2310.18423 (the discrete central-window prolate is its finite proxy; the phase-space cutoff is not in the e1k machinery). The incommensurability reading of e1o extends to the carrier's own eigenbasis.
- **The W6 pole-budget clause splits into a structure-cheap COUNT and the LOCATION half = M4 (e1s), and #154 item 2 is DONE.** Rank-one interlacing keeps two matrices apart. The Hermitian Weil form $Q$ ($Q_\zeta = Q_{\rm entire} + P$, $\mathrm{rank}(P) = 2$ measured) obeys WEYL interlacing rigorously ($|N_{Q_{\rm on}}(t) - N_{Q_{\rm off}}(t)| \le \mathrm{rank}(P) = 2$ for all $t$, measured max move 1, robust at every extension cell). The non-normal operator $M = D_{\log} - (D_{\log}\xi)\delta^T$ (rank-1 differences pole-on/off and zeta/D-H) has a count that is $Q$'s NON-NORMAL SHADOW, ghost-fragile: the adversary broke the empirical "unfiltered displacement $\le \mathrm{rank}(P) = 2$" at $\lambda = \sqrt{13}, N = 34$ (reading $+3$; a second build reads $+2$), so there is NO provable interlacing bound for $M$ (rank-1, non-normal). The e1l 29-vs-33 tension is RESOLVED: $33 = N^* = \lfloor T/\phi\rfloor$ is the geometric lattice ceiling (a BUDGET quantity), not a pole-off count; $29 = 33 - \mathrm{rank}(P) - \text{ghost}$; no interlacing is violated. The N-direction lambda-plateau is PROVEN by Cauchy compression interlacing ($D_{\log}^{(N)}$ is the exact central block of $D_{\log}^{(N+1)}$; $n_{\rm win} = \min(N, \lfloor T/\phi\rfloor)$ at the tested plateau). The pole-free count $= \lfloor T/\phi\rfloor$ EXACTLY at the tested $\lambda \le 3$ (and $\lambda = 5$), with GENUINE $O(1)$ deviations at larger $\lambda$: D-H undercounts the lattice by 1-2 ghost-free at $\lambda$ in $\{3.3, 3.6, 4.0, 4.5\}$, and at $\lambda = \sqrt{13}$ it is zeta-OFF (33, exact), NOT D-H (31), that anchors the lattice (the "D-H is THE clean entire-part count" reading is BACKWARDS there, restoring consistency with e1l's recorded D-H 30-31). Net: the W6 COUNT half is STRUCTURE-CHEAP UP TO $O(1)$ (the rigorous content is Weyl-on-$Q$, $\le 2$, K1-clean and zeta-input-free), and the residual is pinned to LOCATION (the density profile / height-dependence / reality in the limit / the critical line $=$ M4 / the uniformity joint). #154's literal "count moves by $\le 1$" is CORRECTED on the record to a rigorous $\le 2$ on $Q$; the non-normal $M$-shadow has no provable bound, and the secular residues are sign-indefinite so no clean per-gap interlacing exists. With this, the #154 upgrade-spec probe list is COMPLETE (all four ingredients executed: (1) the lattice tail in-build, (2) this rank-one interlacing, (3) the absorption count = e1l #159, (4) the Hamburger pin).
- **The classical floor is machine-checked (Lean #S4C-1..#S4C-5).** The five deliberately classical e1o VERIFIER targets landed sorry-free, axioms exactly `[propext, Classical.choice, Quot.sound]`, build green 3762 jobs: the Euler-gate inequality (corrected #161 nonnegativity form; `vonMangoldt_nonneg` discharges it, sign-changing $\Lambda_{DH}$ fails it), the tail-divergence KERNEL (the one classical Chebyshev input $\psi(x) \ge c\,x$ carried as an honest EXTERNAL hypothesis $=$ a named Mathlib gap and upstream-PR candidate), the structural-nil span atom, the decimation rank-1 collapse (the $\mathbb{F}_q$ Frobenius avatar), the trig-Vandermonde nonsingularity.
- **Frontier: UNMOVED.** The S4/R1 coordinate is now closed at every buildable corner with its classical floor machine-checked, and the W6 clause of #154 stands fully dissected (count half structure-cheap up to $O(1)$, location half $=$ M4). Handed forward: the faithful metaplectic self-dual Sonin projector (the sole unbuilt variant); the D-H undercount mechanism (worth one look); the Mathlib Chebyshev $\psi$-bound (an upstream-PR target); the $\theta \le 1/2$ Beurling corner and Carneiro-Littmann well-posedness remain the standing SURVEYOR items.
