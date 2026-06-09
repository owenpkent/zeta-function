# First-principles conjecture program: nine new RH attack shapes, adversarially filtered

> A synthesis dossier written 2026-06-09 (session 019). It records a single
> multi-agent run that answered one question: **be creative, use first
> principles, and propose genuinely new conjectural routes to RH, then kill the
> ones that do not survive the project's own discipline.** Nine builder lenses
> each produced one named, precise conjecture; an adversary attacked each against
> the D-H discipline, the four-level framing, K1 non-circularity, and the
> dead-branch list. Five survive as research directions, two are reshaped, two are
> killed and logged here as negative coordinates.
>
> Companion to [`soft_detector_wall.md`](soft_detector_wall.md) (the frozen index
> of what cannot work), [`all_roads_to_the_signature.md`](all_roads_to_the_signature.md)
> (the realization-vs-signature ledger), and
> [`rh_solved_by_accident.md`](rh_solved_by_accident.md) (the accident-channel
> landscape). PROVEN and CONJECTURAL are distinguished throughout. Nothing here
> crosses the gap; every builder-assigned confidence is below $0.35$. The
> deliverable is a set of new PROOF SHAPES, each with a cheap falsification test.

## 1. Why this run, and the honest frame

The project has converged its frontal assault to one object: $\mathrm{AX\text{-}POL}$,
the positivity of the Rosati trace form $B(x,y)=\mathrm{Tr}(x\,y^\dagger)$ on the
arithmetic Frobenius algebra of $\mathrm{Spec}(\mathbb{Z})$, equivalently M4 organ
(a), equivalently the arithmetic Hodge standard conjecture. The marginal-positivity
results (the $+0.035$ minimum eigenvalue, the $e^{-4\pi x}$ collapse, the $370\times$
cancellation) prove that this positivity has **no soft margin**: a frontal inequality
attack cannot win, because the quantity it would bound is the residue of a near-total
cancellation invisible to any reachable truncation.

The bet of this run is the dual move. Rather than fight the positivity head-on,
**change the statement type** so that "barely true" becomes structurally necessary
rather than suspicious. The nine lenses were chosen to span the spaces where
zero-margin statements live naturally: extremal/rigidity theory, convex-cone face
classification, dynamical fixed points, certificate self-reduction, and signature
topology. Each lens was required to (i) state a conjecture precise enough to be
wrong, (ii) be Level 4 or carry an explicit route to it, and (iii) name exactly
where the Euler product enters so Davenport-Heilbronn cannot instantiate it.

A standing honesty caveat, inherited from the project discipline (#73): several
survivors are, like every prior reformulation, RH-EQUIVALENT in one of their
clauses (an attainment step, a cone-membership step). The contribution is NOT a
reduction in difficulty. It is a new proof TOPOLOGY with an unconditional,
non-circular half that is genuinely separable from the RH-equivalent half. Where a
clause is RH-equivalent it is marked as such below.

## 2. The method

Nine BUILDER agents (one per lens) each returned a structured conjecture: name,
precise statement, first-principles motivation, RH link with named bridge theorems,
Euler-dependence (the D-H firewall), level, smallest decisive test, kill criterion,
novelty against the dead-branch list, and a self-assigned confidence. One ADVERSARY
pass then judged each against six attacks: D-H instantiability, the four-level check,
K1 circularity, dead-branch overlap, internal mathematical coherence, and test
feasibility. The adversary was calibrated to kill only for structural flaws, not for
ambition or strangeness.

The run was paused and resumed in a token-optimized configuration (the creative
builder core at full model; the adversarial pass batched onto a cheaper model with
repo reading disabled). The optimization is orthogonal to the mathematics and is
not relevant to the findings.

### 2.1 The full slate (scorecard)

| Conjecture | Lens | Core idea in one line | Verdict | Priority |
|---|---|---|---|---|
| Lonely Crystal (LCC) | extremal rigidity | RH = the cone of positive quadratures for the explicit-formula source contains exactly one point, and zeta is it | PURSUE | 8 |
| Eratosthenes Descent (EDC) | certificate induction | RH as induction on prime octaves: a prime-free base case already a theorem, plus one uniform step, the sieve as the certificate-generation rule | PURSUE | 7 |
| Euler Crystal (ECC) | boundary anomaly | The primes as a physical crystal of scatterers; the Berry-Keating boundary condition derived from the adelic product formula; RH = the crystal is spectrally complete | PURSUE | 7 |
| Euler Facet Rigidity (EFR) | boundary of the cone | The primes are literally the extreme rays of the Weil cone's saturated face; RH falls out of the classification | PURSUE | 7 |
| Euler Decimation Flow (EDF) | renormalization | Zeta is a center fixed point of a coefficient flow; marginal positivity is structurally necessary, not mysterious | PURSUE | 7 |
| Habiro Ladder (HLP) | q-deformation | Prove positivity rung by rung at roots of unity, then force the $q\to1$ limit by Galois integrality (a Liouville move) | RESHAPE | 6 |
| Arithmetic Seifert Flow (ASF) | wildcard | Fill the empty signature row of the knots-and-primes dictionary; RH = the prime link is fibered like a torus knot, not the figure-8 | RESHAPE | 4 |
| Semicircular Polarization | archimedean prism | Unique factorization as free independence; positivity via free probability | KILLED | 2 |
| Adelic Ferromagnet (AFC) | Lee-Yang | p-adic Teichmuller spins with the Euler product as ferromagnetism | KILLED | 2 |

Priority is the adversary's 0-10 score (10 = drop everything and test). Builder-assigned
confidences ran $0.04$ to $0.35$; the two highest ($0.35$, LCC and ECC) are also the two
with the cleanest separable unconditional half.

## 3. The five survivors (PURSUE)

All five share one structural move, arrived at independently from five different
starting points: **convert RH from an inequality into a statement type where zero
margin is the signature of the answer, not an obstacle.**

### 3.1 Lonely Crystal (LCC), extremal rigidity, priority 8

**Statement.** RH is recast as: the cone of positive "log-crystals" (positive
tempered measures $\mu$ paired with a nonnegative comb $C=(c_n)$) compatible with
zeta's explicit-formula source contains EXACTLY ONE point, and that point is the
von Mangoldt crystal. Two clauses: **(i) rigidity** (unconditional, no RH assumed):
every log-crystal for the source has $c_n=\Lambda(n)/\sqrt{n}$, so $\mu$ is unique;
**(ii) attainment**: at least one log-crystal exists. Together (i)+(ii) give Weil
positivity, hence RH.

**Why it survives.** The D-H firewall is a PROVABLE lemma, not a numeric: the D-H
source has archimedean density $\approx -0.099$ at $r=0$ and no pole term, so a
Fejer-test pairing certifies no positive crystal exists for it (stealth-window
independent). The cleanest separation of all nine: a proven D-H exclusion, an
unconditional open core (rigidity), and an RH-equivalent attainment cleanly marked.

**The open core.** The composite-pinching mechanism (sign-richness of the near-null
cone forces $c_n=0$ at non-prime-powers) is the genuine unproven content; the
"ghost crystal" (a second feasible signed comb) is the precise kill. The cited
Olevskii-Ulanovskii / Bondarenko-Radchenko-Seip uniqueness technology covers
uniformly-discrete spectra; the pole-sourced non-uniformly-discrete case here is
outside it and needs a transfer theorem.

### 3.2 Eratosthenes Descent (EDC), certificate induction, priority 7

**Statement.** Slice the Weil form by support octaves $a_k=2^k a_0$. The nested Gram
matrices $G_k$ make $G_k$ a principal block of $G_{k+1}$, and Haynsworth inertia
additivity gives the EXACT identity $\mathrm{In}(G_{k+1})=\mathrm{In}(G_k)+\mathrm{In}(S_k)$,
$S_k$ the octave Schur complement. Conjecture: (i) every $S_k$ is positive
semidefinite; (ii) the certificate margins decay at worst exponentially in the
level, so the Cholesky chain is a self-reducing $\Pi^0_1$ certificate; (iii) a single
$k$-uniform mechanism (Selberg symmetry plus the sieve) certifies $S_k\succeq0$ for
all large $k$. The base case (prime-free window, support $<\log 2$) is a claimed
theorem (Yoshida + Connes-Consani).

**Why it survives.** Level 4, K1-clean (entries built from primes only, no zeros),
D-H-aware (no sieve-formation rule exists for D-H, so the chain cannot be FORMED).
The Haynsworth telescoping is an exact identity, not an estimate; clause (i) plus
the base case suffices for RH via finite-section exhaustion, so clause (iii) is
bonus structure rather than load-bearing. Distinct from 3J/3K: the Schur complement
is across SUPPORT OCTAVES (prime data), not across the on-line zero cushion (zero
data).

**The open core.** Whether octave positivity holds at every $k$, and whether the
margins collapse super-exponentially (which would void the certificate advantage).
Both are directly testable.

### 3.3 Euler Crystal (ECC), boundary anomaly, priority 7

**Statement.** Build a literal crystal of scatterers on the Berry-Keating half-line,
one Blaschke-Potapov factor per prime with reflection coefficient $p^{-1/2}$, whose
on-shell scattering phase reproduces the local Euler factor. The boundary condition
is DERIVED from the adelic product-formula anomaly $\sigma_\infty\prod_p\sigma_p=1$
rather than postulated. Three clauses: (E1) each truncation is $J$-contractive (a
PSD canonical system); (E2) the truncations converge to a unique limit-point system
(opacity $\prod_p(1-1/p)^{1/2}\to0$, the Euler pole, is the confinement); (E3) the
limit Weyl $m$-function equals $i\,\xi'/\xi(1/2-iz)$. Then $\mathrm{Im}\,\Phi>0$ on
$\mathbb{C}_+$ gives $\mathrm{Re}(\xi'/\xi)>0$ on $\mathrm{Re}\,s>1/2$, hence RH
(Lagarias positivity equivalence).

**Why it survives.** Double-locked D-H firewall: D-H has no real-positive prime-power
reflection coefficients (formation fails) AND $\Phi_{DH}$ is provably not Herglotz
(the off-line zero forces $\mathrm{Re}(\xi'/\xi)<0$ on the right strip). Crucially
distinct from the killed Berry-Keating Hamiltonians (experiment 1C): ECC does not
postulate the operator, it CONSTRUCTS it from the Euler product. Highest builder
confidence (0.35) tied with LCC.

**The open core, and a K1 risk.** E3 is the hard conjectural identification. The
adversary flags a genuine K1 question: the Krein-de Branges uniqueness that pins the
limit $m$-function must run from the accelerant/coefficient function (built from
primes, K1-clean) and NOT from the spectral measure (which would import the zero
locus). Builder must specify which.

### 3.4 Euler Facet Rigidity (EFR), boundary of the cone, priority 7

**Statement.** Make the ARITHMETIC DATA the variable. In von Mangoldt coefficient
space, the Weil-cone slice $K=\{\lambda:\,Q_\lambda\succeq0\}$ is convex and compact.
Conjecture: its fully-saturated face $\mathrm{Sat}(K)$ is the SINGLETON $\{\Lambda\}$,
with the extreme rays being the primes (the free generators of the support monoid
$\{\log n\}$) and each per-prime moment sequence forced Herglotz (unitary Satake,
$|\alpha_p|=1$, an Euler product reconstructed from cone geometry). RH is then a
corollary of the classification plus Kaczorowski-Perelli degree-1 uniqueness.

**Why it survives.** Dual to LCC: LCC classifies the measure (spectral side), EFR
classifies the coefficients (arithmetic side). Theorem-grade D-H exclusion on three
independent layers (off-line zeros via Weil's converse; $\lambda_{DH}(6)\neq0$
violates the prime-power face; zeros in $\mathrm{Re}\,s>1$ push D-H out of the box).
The variable flip from the dead LP/SDP/SOS family is structural: that family fixed
the L-function and optimized over test functions; EFR fixes the test cone and varies
the arithmetic.

**The open core, and a K1 risk.** The composite-pinching mechanism is unproven
(same shape as LCC's). The Krein assembly step (reconstruct an entire function with
functional equation from per-prime Herglotz data) must not verify the functional
equation against zero data, or K1 fails.

### 3.5 Euler Decimation Flow (EDF), renormalization, priority 7

**Statement.** A flow on L-coefficients that decimates non-prime-power log-coefficients
while a functional-equation backreaction redistributes. Conjecture: (A) the zero-defect
fixed points are exactly the degree-1 Selberg-class Euler products (zeta for its data;
the D-H class is fixed-point-free by a parity obstruction, no odd real character mod 5);
(B) zeta is a CENTER fixed point (the angular mean of $(1-1/p)R_p$ is exactly 1, so the
linearized margin beta-function vanishes), and the Weil margin $\mu(t)\geq0$ with
subexponential convergence, which explains WHY RH is barely true; (C) under-decimated
truncations $Q_{t,e^{\theta t}}$ ($\theta<1$) are NEGATIVE (positivity is a fixed-point
property, not perturbative); (D) D-H's off-line zeros are the unstable manifold with
Lyapunov exponent exactly $2\beta_1-1=0.617$; (E) a Mobius-dressing SOS witness in the
prime-translation algebra.

**Why it survives.** The most falsifiable specific predictions of all nine (the center
identity, the critical-window exponent 1, the D-H exponent 0.617) and the cheapest
targeted test. K1-clean by architecture (witness from prime translations, no zeros).
The "exactness lemma" connecting $Q_t$ to the Weil sum is a verifiable algebraic
identity. Not De Bruijn-Newman / Rodgers-Tao: EDF flows COEFFICIENTS toward
multiplicativity (Level 4 target), not zeros under heat (Level 3).

**The open core.** Flow well-posedness (the FE backreaction may be underdetermined),
the clause-E witness mechanism, and the clause-C sign, all testable.

## 4. The two kills (negative coordinates, do not re-propose)

### 4.1 Semicircular Polarization (free probability), KILLED by a constant

The conjecture was: unique factorization makes the local Frobenius blocks freely
independent in the Gamma-curvature state, so the Weil prime-side spectral edge is
$\ell^2$ (square-root cancelled) and is dominated by the archimedean curvature; free
probability's Helton-McCullough Positivstellensatz then gives an exact SOS certificate
escaping the commutative Fejer ceiling.

**The kill (PROVEN, on the spot).** The free-convolution edge grows as
$2\sqrt{\sum_{p\le X}\mathrm{Var}_c(X_p)}$ with
$\sum_{p\le X}2(\log p)^2/(p-1)\sim2(\log X)^2$ by Mertens, hence
$\approx 2\sqrt{2}\,\log X$. The archimedean curvature grows as $(1/2\pi)\log T$ at
the matched scale $T=X$. The ratio is $\approx 4\pi\sqrt{2}\approx 17.8\gg1$, so the
free edge OVERWHELMS the curvature and the central inequality (clause C4) is FALSE as
stated. The builder anticipated only a "$\sqrt2$-flavored tension"; the real mismatch
is a factor of $\sim18$, far beyond any normalization fix. Salvage collapses C4 to
exact Weil positivity, i.e. RH itself, so the framework becomes a restatement.

**The coordinate.** Free independence from unique factorization is real and may be a
useful structural lens, but the spectral-edge-domination form of the archimedean-prism
idea is quantitatively dead. Any revival must compute variances in the curvature inner
product (not $L^2$) and produce an edge constant below 1.

### 4.2 Adelic Ferromagnet (Lee-Yang), KILLED as a #42 restatement

The conjecture was: a p-adic spin system with Teichmuller-character single-site
measures on $\mathbb{Z}_p^\times$ and Euler-factor couplings, whose Lee-Yang property
forces partition-function zeros onto the critical line, with ferromagnetism = Euler
product so D-H fails coupling positivity.

**The kill (structural).** The partition function is a PRODUCT of independent local
$\mathbb{Z}_p$ averages. Integrating out each site replaces the Euler factor by its
modulus-squared LOCAL AVERAGE, which destroys the cross-place phase coherence needed
to reproduce $|\zeta(s)|^2$ as a function in the critical strip. The local Euler data
converges only for $\mathrm{Re}\,s>1$; the zeros live in the continuation
$\mathrm{Re}\,s<1$ that a factored product measure cannot reach. This is exactly the
LEARNINGS #42 wall (the local-to-global continuation is the gap; local data cannot
reach $\mathrm{Re}\,s=1/2$) in probabilistic clothing, so the conjecture partially
RESTATES a known dead branch. Newman's classical no-go for naive Lee-Yang
approaches to zeta is the shadow of the same obstruction.

**The coordinate.** A genuine Lee-Yang route would need couplings that are NOT a
factored product measure (so the continuation survives), which is precisely the
global signed pairing the whole program already seeks. The p-adic spin dressing adds
nothing past #42.

## 5. The two reshapes (RESHAPE, lower priority)

- **Habiro Ladder (HLP), q-deformation, priority 6.** Prove rung-by-rung Hodge-index
  positivity at roots of unity, then force the $q\to1$ limit by a Galois-Liouville move
  (the obstruction lies in an integral $\mathbb{Z}[\zeta_N]$-lattice and is too small to
  be a nonzero algebraic integer, hence vanishes). Genuinely novel substrate (Habiro
  cohomology, Garoufalidis-Scholze-Wheeler, appears nowhere in the corpus). The
  load-bearing gap is the covolume-vs-decay arithmetic: the lattice covolume scales as
  $\phi(N)^{1/2}\sim N^{1/2}$ while the stealth decay is $\sim N^{-c}$, so the Liouville
  vanishing needs $c>1/2$, and that exponent is not established. Reshape: pin the
  exponent or move to a p-adic height with a better quantization gap.

- **Arithmetic Seifert Flow (ASF), wildcard, priority 4.** Fill the empty "signature"
  row of the Mazur-Morishita knots-and-primes dictionary: RH as "the prime link is
  algebraically fibered" (definite monotone Tristram-Levine signature flow), giving an
  INTEGER identity (signature flow $=-2N(T)$) that cannot be marginally true. Most
  speculative (confidence 0.04). Underspecified at its two load-bearing clauses (the
  off-diagonal Frobenius linking blocks, and the Fredholm-determinant-equals-$|\xi|^2$
  claim), with an unresolved amphichirality risk from the functional equation. Reshape:
  specify the linking blocks and give a structural (not analogical) argument for the
  determinant identity before any test.

## 6. The pattern, and the two merges worth more than their parts

Every survivor performs the same reinterpretation of the marginal-positivity thesis:
the $+0.035$ residue and the $370\times$ cancellation stop being a mystery and become
the **predicted fingerprint of extremality**. An extreme point of a cone is barely
feasible by definition (LCC, EFR). A center fixed point has exactly zero linearized
margin (EDF). A unique crystal is rigid (LCC). A signature jump is an integer and
cannot be marginally true (ASF). A self-reducing certificate telescopes a healthy
per-octave positivity into a globally marginal one (EDC). "Barely true" stops being a
wall and becomes a classification target.

Two pairs could merge into something stronger than either:

- **LCC + EFR** are dual faces of one classification program. LCC classifies the
  positive measures (spectral side), EFR classifies the coefficient data (arithmetic
  side), and both assert the boundary of the Weil cone is exactly arithmetic (the
  extreme rays are the primes). The shared open core is the same composite-pinching
  mechanism; proving it once serves both. This is the highest-value merge.

- **EDC + EDF** are the discrete and continuous scale-gradings of Weil positivity.
  EDC's Haynsworth telescoping is an EXACT identity; EDF's flow has the richer
  predictions but currently lacks a rigorous skeleton. EDC could supply the skeleton
  EDF needs, and EDF could supply the mechanism (center-stability) that explains why
  EDC's octave margins should stay positive.

## 7. The three cheapest decisive experiments

All three run on existing repo infrastructure (mpmath / numpy / cvxpy-CLARABEL, the
validated Bombieri kernel and Gram builders in `experiments/positivity/`, the D-H
control in `experiments/_shared/davenport_heilbronn.py`). Per the soft-detector
freeze, these are FALSIFICATION instruments, not certificates: a clean negative kills
a mechanism; a clean positive supports a conjecture without proving anything.

1. **LCC LP triple** (`experiments/positivity/e3x_lonely_crystal_lp.py`). Three runs:
   (a) blind crystal recovery with the von Mangoldt comb fixed and NO zero data in the
   solver (does the recovered mass localize at $\gamma_1,\gamma_2,\dots$?); (b)
   composite-node rigidity (free $c_6\geq0$, maximize, check it shrinks to 0 under
   refinement); (c) the D-H infeasibility certificate (the Fejer triangle dual).
   Outcome: a persistent $c_6$ floor kills LCC clause (i); D-H feasibility breaks the
   firewall and the whole lens.

2. **EDF under-decimation discriminator** (extends `experiments/positivity/e3c2_weil_gram.py`).
   Minimum eigenvalue of the half-matched form $Q_{t,e^{t/2}}$ at $t=8,9,10$, plus the
   single-prime $p=2$ dip at the $\xi=2\pi/\log2$ packet. Outcome: if these forms come
   out nonnegative (against the predicted clear negativity), the critical-window
   mechanism is dead in one run, independent of RH.

3. **ECC spectral-leakage test** (`experiments/spectral/e1x_euler_crystal.py`). Build
   the truncated prime crystal as a transfer recursion and compute $m_X(i)$ for
   $X=10^2,\dots,10^5$. Outcome: convergence to $i\,\xi'/\xi(3/2)\approx0.0461\,i$
   supports E3; convergence to any other Herglotz value (Montel guarantees it converges
   to something) is spectral leakage and kills E3.

## 8. How I would go about finding a solution

Directly, integrating the survivors with the existing spine. I would accept the
project's hard-won localization (RH $=\mathrm{AX\text{-}POL}$, one positivity on one
primitive space, with no soft margin available), and then REFUSE to fight that
positivity head-on, because the marginal-positivity results prove head-on loses: the
quantity a frontal inequality would bound is the residue of a near-total cancellation
invisible to any reachable truncation. Instead I would attack the STATEMENT TYPE,
along the two axes the survivors define.

**Axis 1, classification.** Prove unconditionally that anything sitting on the boundary
of the Weil cone must be an Euler product (EFR's saturated-face rigidity, LCC's lonely
crystal), so that zeta's membership in the positive cone follows from WHAT IT IS rather
than from an estimate. This is the move that turns marginality from a liability into the
hypothesis: an extreme point is barely feasible by definition, so "zeta is barely
positive" becomes "zeta is the extreme point," and extreme points are exactly what
rigidity theorems classify. The unconditional, non-circular half here is real (the
provable D-H firewall, the composite-pinching target); the RH-equivalent half (attainment
/ membership) is cleanly separated and attacked last.

**Axis 2, induction and quantization.** Replace the single global inequality with a
structure that survives a zero-margin world. Two currencies survive there: a SELF-REDUCING
certificate (EDC's prime octaves, where the Haynsworth identity
$\mathrm{In}(G_{k+1})=\mathrm{In}(G_k)+\mathrm{In}(S_k)$ is exact and the base case is
already a theorem) and an INTEGER-VALUED invariant (ASF's signature flow, which cannot be
marginally true because it counts). A global inequality with zero margin is fragile; an
exact telescoping identity and an integer equality are not.

**The discipline that makes it tractable.** At every step, run the cheapest kill test
first. A conjecture that dies in an afternoon of computation is a contribution: it is a
coordinate that narrows the search, in exactly the sense this project already runs on.
The three tests in Section 7 are the immediate instance: each can falsify a mechanism
cheaply and independently of RH, and the survivors of that pruning are the ones worth the
years.

The two axes are not independent. The highest-value object is the LCC+EFR merge (one
classification with a spectral face and an arithmetic face), and EDC's exact identity is
the rigorous skeleton that EDF's center-stability flow needs. If I had to name a single
target, it would be the composite-pinching lemma shared by LCC and EFR: prove that a
fully-saturated point of the Weil cone has no mass off the prime powers. That one lemma,
if it holds, is the unconditional engine both classification routes are missing, and it
is the cleanest thing in the whole slate that is NOT itself a restatement of RH.

## 9. Honest scope

This run produced no theorem and crossed no gap. It produced nine precise, falsifiable
conjectures, filtered to five viable new proof shapes, two clean kills, and two
reshapes, each with a named open core and a cheap test. The five survivors are new
TOPOLOGIES on the same RH-equivalent positivity, not reductions of its difficulty;
their value is the separable unconditional half (a provable D-H firewall in LCC and
EFR, an exact Haynsworth identity in EDC, an algebraic exactness lemma in EDF, a
constructed-not-postulated operator in ECC) and the reinterpretation of marginality as
extremality. The two kills are coordinates: the archimedean-prism idea is
quantitatively dead in its spectral-edge form (factor $\sim18$), and the Lee-Yang
route adds nothing past the #42 continuation wall. Next move is to run the three tests
above, cheapest-first, and let the negatives prune.

Cross-refs: 08A M4 / $\mathrm{AX\text{-}POL}$ (the target every survivor reformulates),
#52 / #56 / #63 (the marginal-positivity facts reread as extremality), #42 (the
continuation wall that kills the Adelic Ferromagnet), #43 (the de Branges
stronger-than-RH precedent the Semicircular C4 echoed), 1C (the postulated-Hamiltonian
kill that ECC routes around by construction), #71 (the universal gap the survivors
each propose a different shape for).
