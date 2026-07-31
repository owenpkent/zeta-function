# Reading note: the Christoffel-function / orthogonal-polynomial growth corpus against the #160 growth clause

> SURVEYOR sweep, 2026-07-30. Executes the TODO.md item "The Christoffel-corpus sweep (NEW from
> #171)" and step 2 of PHASE_STATE.md "Next steps". Posed by the LEARNINGS #171 price answer: a
> discriminating $\lambda$-uniform rate clause in the trace-normed canonical-chain gauge equals
> **uniform Christoffel / orthonormal-polynomial growth control at the footpoint**, which IS the
> #160 growth clause in Jacobi coordinates
> ([`e1u_canonical_chain.md`](../../../experiments/spectral/e1u_canonical_chain.md), price table,
> row "the U3c rate clause, priced"; [`trojan_horse_m4.md`](../trojan_horse_m4.md) Section 8, final
> paragraph).
>
> **The sweep question, verbatim from #171:** is there ANY known mechanism giving $\lambda$-uniform
> Christoffel control at a point, against measures whose atoms sit at $\mathbb{Q}$-linearly
> independent positions, for a STRUCTURAL reason (Euler product + additive lattice)?
>
> **This note proves nothing about RH.** It is a literature map with a scorecard.

---

## STATUS (written after the sweep; criteria in Section 0 were fixed before it)

- **Date:** 2026-07-30. **Role:** SURVEYOR.
- **Verdict: NO HIT. Three NEAR-MISSES, four OBSTRUCTIONS, and the rest MIRAGE.**
  Nothing in the Christoffel-function / orthogonal-polynomial growth corpus supplies the
  growth clause with a structural (Euler + lattice) source. The clause is **exactly as open
  as #160 left it**, and the sweep upgrades the "why" from "not found" to a
  **structural incompatibility with a named shape**: every uniformity theorem in this corpus
  is conditioned on the spectrum being THICK (positive Lebesgue measure locally: a.c. weight,
  doubling, Carleson-homogeneous, Parreau-Widom), and the chain's spectrum is a
  **discrete, Lebesgue-null set**. The corpus's uniformity apparatus is on the wrong side of
  a thickness dichotomy, not merely silent.
- **The one genuinely new structural product** (Section 1, evidence-checked): in Christoffel
  coordinates the growth clause splits cleanly into two layers, and the layers have different
  discipline verdicts. The **RATE layer** (the exponential growth of $K_M$ at the footpoint) is
  a logarithmic-potential functional of the atom-counting measure, hence density-typed and
  Beurling-shared, measured here at **30x** the size of the fine-structure effect. The
  **PREFACTOR layer** (the Widom-factor layer) is where atom fine structure lives, and it is
  the only layer where an arithmetic input (Baker-type lower bounds on
  $|k\log p - k'\log p'|$) has any purchase at all. Since the discriminating content of RH is
  a zero-location statement and the rate layer is location-blind, this **re-derives the e1u U2c
  verdict from the Christoffel side and independently reconfirms `e2ii`** (LEARNINGS #62, "the
  candidate-F bridge is WEAKER than hoped"): the Diophantine input sits an order of magnitude
  below where the discrimination lives.
- **Consequence for the clause:** a $\lambda$-uniform Christoffel statement that could
  discriminate must be posed in the PREFACTOR (Widom-factor) layer, after dividing out the
  density-forced rate. That is a sharper posing than #171 had, and it is stated as a follow-on
  rung (Section 10, BUILDER items 1-2), not as a result.
- **Repo-absent items surfaced:** Romik arXiv:1902.06330 (86pp, OP expansions of $\Xi$;
  ZERO repo mentions), the Bessonov-Denisov Krein-string Szegő theory (ZERO repo mentions),
  Eichinger-Lukic Stahl-Totik regularity for continuum operators (ZERO repo mentions), and the
  Widom-factor corpus (ZERO repo mentions). Plus one incidental ADJACENT-WATCH item found off
  the sweep's own axis (arXiv:2607.24830, 2026-07-23; Section 10, SURVEYOR item 11).
- **Evidence:** [`_evidence/christoffel_gap_growth_check.py`](_evidence/christoffel_gap_growth_check.py),
  11/11, tracked output alongside. Run:
  `python docs/03_research/reading_notes/_evidence/christoffel_gap_growth_check.py`.

## SECTION 0. PRE-REGISTERED CRITERIA

**Written before any search was run.** (Process note, honestly stated: this section was composed
and saved to disk as the first action of the sweep, before the first WebSearch/WebFetch call of
the session. The orientation reading listed in Section 0.1 happened first; no external literature
was consulted before these criteria were fixed. Criteria were NOT amended afterwards; where a
finding sat awkwardly against a criterion, the awkwardness is recorded in Section 6 rather than
resolved by moving the line.)

### 0.1 What was read first (orientation, repo-internal only)

`CLAUDE.md`; `PHASE_STATE.md`; `experiments/spectral/e1u_canonical_chain.md` (full);
`docs/03_research/trojan_horse_m4.md` Section 8; `experiments/LEARNINGS.md` #160, #170, #171;
`TODO.md`; `docs/03_research/s4_carrier_audit.md` Section 4 item 5 (the S4 spec);
`docs/03_research/reading_notes/kns_log_growth_pin.md` Sections 2-4 (the S4-spec restatement and
the $\{k\log p\}$ growth reading).

### 0.2 The clause being tested, stated precisely

Let $\hat\xi_\lambda$ be the ghost-quotiented finite CCM object at cutoff $\lambda$ (the e1k/e1t/e1u
harness). Two measures are in scope, because the sweep question conjoins two conditions that live
on two different objects in the repo's own coordinates:

- **(T-A) the chain measure.** $\mu_\lambda$ = the Prokhorov-normalized counting measure on the
  real strip zeros $\{\pm t_j\}_{j\le M(\lambda)}$ of $\hat\xi_\lambda$ (e1u Face A). Footpoint
  $x_0 = 0$, which lies in a **central spectral gap** ($\zeta$: no atoms below 13.6; D-H: below
  4.9). The e1u germ trace-length is
  $$X(\lambda) \;=\; \sum_{k=0}^{M-1}\big(q_k(0)^2 + p_k(0)^2\big), \qquad
    \sum_{k=0}^{M-1} p_k(0)^2 \;=\; K_M(0,0) \;=\; \frac{1}{\lambda_M(\mu_\lambda,\,0)},$$
  i.e. **the reciprocal Christoffel function of $\mu_\lambda$ at the footpoint**, plus its
  second-kind twin. Measured (e1u U1): $X$ reaches $3.96\times10^{10}$ for $\zeta$ at
  $\lambda=\sqrt{13}$ ($M=48$), $5.78\times 10^{6}$ for D-H, and stays at $13$-$41$ for the
  density-matched Beurling fake (which has no central gap).
- **(T-B) the S4 carrier measure.** The log-prime comb: atoms at $\{k\log p\}$, whose positions
  are $\mathbb{Q}$-linearly independent across primes (unique factorization). This is where the
  sweep question's "$\mathbb{Q}$-linearly independent positions" clause actually bites, and it is
  where LEARNINGS #162 localized the S4 absence.

**The clause (the target).** A statement of the form: there exist $C$, and a rate $r(\cdot)$,
independent of $\lambda$, such that
$$\frac{1}{\lambda_{M(\lambda)}(\mu_\lambda,\,0)} \;\le\; C\, r\!\left(M(\lambda)\right)
\qquad\text{for all }\lambda,$$
(or the corresponding two-sided/normalized form in **unnormalized trace-length**, per e1u U3d: the
$u$-normalized profile is a measured-broken instrument), whose proof consumes the Euler product AND
the additive lattice at the same joint, and which is therefore FALSE or UNPOSABLE for D-H and for
the Beurling control.

### 0.3 HIT criteria (all four required)

A mechanism counts as a **HIT** only if it supplies a bound with all of:

- **H1 POINTWISE.** At a single fixed footpoint $x_0$. Not "for a.e. $x$" (Lebesgue or $\mu$),
  not "in measure", not after averaging over an interval, not "for all $x$ outside an exceptional
  set of capacity zero". The clause needs the value AT the footpoint.
- **H2 FAMILY-UNIFORM.** A single constant/rate valid for the whole family $\{\mu_\lambda\}$ with
  $M(\lambda)\to\infty$. A theorem of the form "for FIXED $\mu$, as $n\to\infty$, ..." is not
  family-uniform: it gives one constant per measure with no control on how the constant varies
  along the family. (This is the exact defect #160 named: the finite types diverge, so the limit
  object is not reachable from per-$\lambda$ statements.)
- **H3 STRUCTURAL SOURCE.** The hypothesis that buys the uniformity must be arithmetic:
  a multiplicative/Euler-product input AND an additive-lattice/Poisson input, at the same joint
  (the #170 tariff / conservation law). Explicitly NOT sufficient as a source:
  (a) a density/counting hypothesis on the atoms alone; (b) a potential-theoretic hypothesis on
  the SUPPORT alone (capacity, Green's function, equilibrium measure, regularity in the
  Stahl-Totik sense); (c) an absolutely-continuous-part hypothesis ($\mu' > 0$, Szegő condition,
  doubling weight, $A_\infty$), since the target measures are **purely atomic**;
  (d) a smoothness hypothesis on a varying external field.
- **H4 DISCIPLINE-FALSIFIABLE.** The mechanism must be shown to FAIL, for a nameable reason, for
  BOTH controls: Davenport-Heilbronn (functional equation, no Euler product) and the density-matched
  Beurling control (Euler product, no additive lattice). Per the task framing, the
  atoms-at-$\mathbb{Q}$-linearly-independent-positions condition is precisely where the lattice
  enters, so the Beurling gate is sharp here and is NOT a formality.

**Partial hit (recorded as NEAR-MISS, not HIT):** H1 + H2 satisfied but the source is (a)-(d).
A NEAR-MISS is upgraded only if a named, checkable route from an Euler+lattice input to the
mechanism's own hypothesis is exhibited. "Could conceivably be arithmetised" is not a route.

### 0.4 MIRAGE criteria (the Level-3 trap, pre-named)

A result is a **MIRAGE** for this clause if its content is a BULK ASYMPTOTIC: a limit statement
about local/rescaled behaviour that is compatible with off-line worlds. Pre-named instances (the
caution in TODO.md and #171, written down in advance so it cannot be softened later):

- Universality of the rescaled Christoffel-Darboux kernel (sine kernel in the bulk, Airy/Bessel at
  edges): Lubinsky-type theorems.
- Christoffel-function asymptotics valid for a.e. $x$ (Máté-Nevai-Totik; Totik's regular-measure
  extension).
- Ratio asymptotics, Rakhmanov/Denisov-type theorems, Nevai-class membership.
- Clock behaviour / fine spacing of zeros of orthogonal polynomials.
- Random-matrix canonical-systems statements (Valkó-Virág and descendants), already graded
  Level 3 in #170.

The reason, stated once: all of these are statements about the LOCAL STATISTICS of a spectrum at a
fixed measure, and the repo's four-level framing (`CLAUDE.md`, "Core conceptual framework") places
such statements at Level 3. A world in which one zero sits at $\beta = 0.51$ is compatible with
every one of them. **A mirage does not become a hit by being sharp, quantitative, or hard.**

### 0.5 OBSTRUCTION criteria

A finding is an **OBSTRUCTION** if it does one of:

- **O1** proves the desired uniform control FALSE (a counterexample family);
- **O2** shows a hypothesis incompatibility that is STRUCTURAL, not technical: every theorem in a
  class requires an input the target measures provably lack (e.g. $\mu' > 0$ near $x_0$ for purely
  atomic $\mu$ with $x_0$ in a gap), so the class is inapplicable by hypothesis;
- **O3** shows that the quantity the mechanism controls is provably shared by a control (D-H or
  Beurling), hence weightless: a **conservation-law confirmation** in the #170 sense;
- **O4** shows the mechanism class does not extend past a proven ceiling (a no-go for
  higher-order/finer versions).

### 0.6 Reporting rules bound in advance

1. Every cited paper is tagged **FETCHED** (read at source this session, with what was extracted),
   **SECONDARY** (known only through another source read this session, named), or
   **UNVERIFIED-MEMORY** (recalled, not confirmed this session: to be treated as a pointer, never
   as evidence).
2. Every mechanism gets a four-level call (Level 1-4 per `CLAUDE.md`).
3. Every mechanism gets a D-H line and a Beurling line, even when the answer is "unposable".
4. Discrepancies with existing repo analyses are logged in Section 6, not silently resolved.
5. If everything found is bulk-asymptotic, that is stated plainly as the finding, with what it
   rules out.

### 0.7 The pre-registered exit

If the sweep produces no HIT and no NEAR-MISS with a named upgrade route, the verdict is:
**the growth clause is exactly as open as #160 left it, and the Christoffel costume is a
coordinate change, not a reduction** (the #160 / #171 "reformulated, not reduced" pattern, fourth
instance). That outcome is banked as a coordinate, not as a defeat: it narrows where the mechanism
can live.

---

## SECTION 1. THE CLAUSE IN CHRISTOFFEL COORDINATES, EXACTLY

### 1.1 The identification (elementary, and now checked)

e1u's chain carries, on interval $k$, the vector $u_k = (q_k(0), -p_k(0))$ of first- and
second-kind orthonormal polynomial values at the footpoint, with trace-length
$l_k = |u_k|^2$ (e1u encoding item 4). So the germ trace-length is

$$X(\lambda) \;=\; \sum_{k=0}^{M-1} l_k \;=\; \underbrace{\sum_{k=0}^{M-1} p_k(0)^2}_{=\;K_M(0,0)\;=\;1/\lambda_M(\mu_\lambda,0)} \;+\; \sum_{k=0}^{M-1} q_k(0)^2 .$$

The first sum is exactly the Christoffel-Darboux kernel diagonal, i.e. the **reciprocal
Christoffel function at the footpoint** (Christoffel variational principle: Simon,
arXiv:0806.1528, Theorem 9.2 [FETCHED, full text]). This is what makes e1u's
VERIFIER target 6 ("total trace-length grows like the reciprocal Christoffel function at the
footpoint") the right statement, and it is why the whole rate clause is a Christoffel question.

For an $M$-atom measure $\mu = \sum_j w_j \delta_{x_j}$ and a non-atom footpoint $x_0$, the
reproducing property of $K_M$ on $L^2(\mu)$ (which for $M$ atoms is the FULL space of
polynomials of degree $\le M-1$) gives $K_M(x, x_j) = L_j(x)/w_j$ with $L_j$ the Lagrange basis
polynomial at the nodes, hence the exact identity

$$K_M(x_0,x_0) \;=\; \sum_{j=1}^{M} \frac{|L_j(x_0)|^2}{w_j}
 \;=\; \sum_j \frac{1}{w_j}\prod_{i\ne j}\frac{(x_0-x_i)^2}{(x_j-x_i)^2}.$$

This is classical (it is the Gauss-quadrature / Cotes-number picture of Simon's Sections 6-7),
not new here; it is written out because it makes the arithmetic content of the clause visible:
**the numerators are atom POSITIONS and the denominators are atom GAPS.** The clause is a
small-denominators object, which is exactly why "atoms at $\mathbb{Q}$-linearly independent
positions" is the right thing to ask about.

**Checked**: [`_evidence/christoffel_gap_growth_check.py`](_evidence/christoffel_gap_growth_check.py)
(11/11, output tracked at
[`_evidence/christoffel_gap_growth_check.out.txt`](_evidence/christoffel_gap_growth_check.out.txt)),
check C1, against an independent Gram-Schmidt build, relative deviation $\le 2.5\times10^{-58}$
at mp.dps 60.

### 1.2 The two-layer split (the sweep's own structural product)

Write $\log K_M(0,0) = 2M\,r_M + (\text{prefactor})$. The literature fixes the RATE layer:

- **Compact case.** For measures regular in the Stahl-Totik sense, $|p_n(z)|^{1/n} \to e^{G_e(z)}$
  off the support, with $G_e$ the Green's function of $\mathbb{C}\setminus e$, and
  $G(z) = -\log C(e) + \int\log|z-x|\,d\rho_e(x)$ (Christiansen-Simon-Zinchenko,
  arXiv:2112.06450, eq. (1.1), (1.5) [FETCHED, full text]). The rate depends on the SUPPORT only.
- **Unbounded case (this is e1u's case: the spectrum runs to infinity).** Eichinger-Lukic,
  arXiv:2001.00875 [FETCHED, full text], replace the Green's function by the **Martin function**
  $M_E$ of the Denjoy domain $\mathbb{C}\setminus E$ and prove:
  - **Theorem 1.3 (free, no regularity hypothesis):**
    $M_E(z) \le \liminf_{x\to\infty}\frac1x\log|u(x,z)|$ for all
    $z \in \mathbb{C}\setminus[\min E,\infty)$. A universal LOWER bound on the growth: you cannot
    avoid at least Martin-rate growth at an off-spectrum point.
  - **Theorem 1.5, (i) $\Leftrightarrow$ (vi):** the potential is regular **iff**
    $\lim_{x\to\infty}\frac1x\log|u(x,z)| = M_E(z)$ uniformly on compacts of
    $\mathbb{C}\setminus[\min E,\infty)$.

  So the rate at an off-spectrum footpoint is EXACTLY a potential-theoretic functional of
  $E = \sigma_{\mathrm{ess}}$.
- **Ergodic case.** The Thouless formula $\gamma(E) = \int\log|E-E'|\,dN(E')$ says the same thing
  in the density-of-states language: the exponential growth rate is the logarithmic potential of
  the counting measure (Avron-Simon / Craig-Simon; [UNVERIFIED-MEMORY], stated in the standard
  form, source not read line-by-line this session).

**Finite-$M$ shadow, measured** (evidence check, C2 and C3; all numeric thresholds PINNED from a
calibration run and labelled as such in the script):

| what is varied | $\lvert\Delta \log K_M\rvert$ at $M=48$ | at $M=96$ | at $M=192$ | per-atom trend | layer |
|---|---|---|---|---|---|
| relocation of every atom by 0.10 of its local gap | 0.216 | 0.151 | 0.124 | 0.0045 to 0.0006, decaying | PREFACTOR |
| relocation by 0.30 of its local gap | 1.330 | 1.179 | 1.117 | 0.0277 to 0.0058, decaying | PREFACTOR |
| **gap half-width 13.6 to 4.9** (zeta-shaped to D-H-shaped) | 6.62 | 16.12 | **33.37** | 0.138 to 0.174, NOT decaying | **RATE** |

and the dichotomy itself: with the window top fixed at 160, the gapped family's per-atom
$\log K$ RISES along the grid (0.187 to 0.291 as $M$ goes 24 to 192) while the density-matched
gapless family's FALLS (0.124 to 0.027), with the ratio going 1.50 to 10.73.

**Reading.** The relocation family is exactly the #160 / e1m non-uniqueness family (counting
function preserved to $O(1)$, object pointwise different, adjacent atoms pushed toward
collision, i.e. the small-denominator direction). It moves $\log K$ by a BOUNDED amount as $M$
grows: a prefactor effect. Changing the gap geometry moves $\log K$ proportionally to $M$: a
rate effect. At $M=192$ the gap effect is **30x** the relocation effect.

This is the Christoffel-coordinate restatement of e1u's U2c control (symmetric band exclusion
kills every apparent zeta-first face, because what the faces measure is central-gap depth) and
of e1u's U1 conditioning panel (the germ-length blowup IS the gap-driven rate). It also
independently reconfirms
[`e2ii_transcendence_bridge.md`](../../../experiments/arithmetic_geometric/e2ii_transcendence_bridge.md)
(LEARNINGS #62): there the Weil margin (0.035) sat a factor ~25 ABOVE the effective Diophantine gap scale
(0.0013); here the density-driven rate effect sits a factor ~30 above the fine-structure
effect. Two different gauges, the same order-of-magnitude verdict about where the arithmetic
fine structure lives relative to the discriminating signal.

### 1.3 What this does to the sweep question

The sweep question ("$\lambda$-uniform Christoffel control at a point, against
$\mathbb{Q}$-linearly-independent atoms, for an Euler+lattice reason") splits:

- against the RATE layer: **already answered NO by structure**, since the rate is a functional
  of the counting measure, which the density-matched Beurling control shares by construction.
  No mechanism, arithmetic or otherwise, can make the rate layer discriminate. (This is
  OBSTRUCTION O3 and it is the sweep's firmest finding.)
- against the PREFACTOR layer: the question is live in principle, and the corpus's name for it
  is **Widom-factor boundedness**. That is where Section 3 goes, and where the corpus's answer
  turns out to be a thickness hypothesis the chain's spectrum cannot satisfy.

---

## SECTION 2. THE CORPUS: BULK CHRISTOFFEL ASYMPTOTICS (STRAND A)

### 2.1 Máté-Nevai-Totik, and Totik's general-measure extension

| source | tier | what it gives |
|---|---|---|
| Simon, "The Christoffel-Darboux Kernel", arXiv:0806.1528, Proc. Sympos. Pure Math. 79 (2008), 295-336 | FETCHED (full PDF text; Sections 7, 9, 12, 13, 14, 17, 18, 20, 24 read verbatim) | The master survey; Theorems 9.2, 12.1, 12.2, 14.1, 14.2, 17.1, 17.2, 17.3, 20.1, 20.3, 24.1 |
| Máté, Nevai, Totik, "Szegő's extremum problem on the unit circle", Ann. of Math. 134 (1991), 433-453 | SECONDARY (statement pinned verbatim through Simon's survey Theorems 17.1-17.2) | $\lim n\lambda_n(\theta_\infty) = w(\theta_\infty)$ for a.e. $\theta_\infty$, under the Szegő condition |
| Totik, "Asymptotics for Christoffel functions for general measures on the real line", J. Anal. Math. 81 (2000), 283-303 (DOI 10.1007/BF02788993) | SECONDARY (statement pinned verbatim through Simon's survey Theorem 17.3; journal abstract fetched) | $\lim \frac1n K_n(x_\infty,x_\infty) = \rho_e(x_\infty)/w(x_\infty)$ for a.e. $x_\infty \in I$ |
| Nevai, "Géza Freud, orthogonal polynomials and Christoffel functions. A case study", J. Approx. Theory 48 (1986), 3-167 | UNVERIFIED-MEMORY / bibliographic pin only (existence and full citation confirmed by search; text NOT read this session) | The field's foundational survey; treated here as a pointer, never as evidence |

**Hypotheses, verbatim from Simon's survey Theorem 17.3** (Totik): "Let $e$ be a compact subset
of $\mathbb{R}$. Let $I \subset e$ be an **interval**. Let $d\mu$ have $\sigma_{ess}(d\mu) = e$ be
**regular** for $e$ with $\int_I \log(w)\,dx > -\infty$. Then for **a.e.** $x_\infty \in I$,
$\lim \frac1n K_n(x_\infty,x_\infty) = \rho_e(x_\infty)/w(x_\infty)$."

Máté-Nevai upper bound (Theorem 14.1): "for any **Lebesgue point** $x$ in $I$,
$\liminf \frac1n K_n(x,x) \ge \rho_e(x)/w(x)$", with $I \subset e$ a closed interval.

**Verdict: MIRAGE, and additionally OBSTRUCTION O2.**

- **H1 fails**: the conclusions are a.e. statements on an interval, not statements at a chosen
  footpoint. (Uniformity is available only when $w$ is continuous and nonvanishing on $I$.)
- **H2 fails**: fixed $\mu$, $n \to \infty$. No control of the constant along a family.
- **H3 fails structurally, twice**: the footpoint must lie in an **interval contained in the
  support**, and the measure must have $w > 0$ with $\log w$ locally integrable. Our $\mu_\lambda$
  is **purely atomic** ($w \equiv 0$, so $\int_I\log w = -\infty$) and the footpoint sits in a
  **gap** (no interval of $e$ contains it). Both hypotheses fail by construction, not by
  technical shortfall.
- **Four-level call: Level 3.** These are statements about local spectral statistics at a fixed
  measure; nothing in them constrains the location of any individual atom.

### 2.2 The continuum / canonical-system analogue (the closest paper to e1u's gauge)

| source | tier | what it gives |
|---|---|---|
| Eichinger, "Asymptotics for Christoffel functions associated to continuum Schrödinger operators", arXiv:2204.05633, J. Anal. Math. (2024) | FETCHED (full PDF text) | Theorem 1.1, 1.2, 1.3; the Martin-measure formulation |

**Theorem 1.1 verbatim**: "Let $V$ be a **Stahl-Totik regular** potential such that
$E = \sigma_{ess}(H_V)$ is Dirichlet regular and $\mu$ the corresponding spectral measure. Let
$I \subset \mathrm{int}(E)$ be a closed interval such that $\mu$ is **absolutely continuous in a
neighborhood of $I$** and its density $f_\mu$ is **positive and continuous** at every point of
$I$. Then $\lim_{L\to\infty} L\lambda_L(\xi) = f_\mu(\xi)/f_E(\xi)$, uniformly for $\xi \in I$."

This is the sharpest possible pin for the sweep, because it is stated in the CONTINUUM /
canonical-system gauge that e1u works in, with $\lambda_L(z) = (\int_0^L|v(x,z)|^2dx)^{-1}$
(his eq. (1.3)), i.e. literally the Weyl-solution mass that e1u's U3 profile measures.

**Verdict: OBSTRUCTION O2, cleanly.** The theorem is uniform (H2 satisfied on $I$) and its
conclusion is the polynomial regime $\lambda_L \asymp 1/L$. It requires $\xi$ in the INTERIOR of
the essential spectrum with a positive continuous a.c. density nearby. e1u's footpoint is in a
gap and e1u's measure is purely atomic. The measured e1u behaviour is exponential blowup, which
is the OTHER branch of the dichotomy, and this theorem says nothing about that branch.
**Four-level call: Level 3** (its conclusion feeds bulk universality and clock spacing, his
Theorems 1.2, 1.3).

### 2.3 Universality (Lubinsky and descendants)

| source | tier | what it gives |
|---|---|---|
| Lubinsky, "A new approach to universality limits involving orthogonal polynomials", Ann. of Math. 170 (2009), 915-939 | SECONDARY (statement pinned verbatim through Simon's survey Theorems 20.1 and 20.3; arXiv math/0701307 located, not read) | Lubinsky's inequality (Thm 20.1) and bulk sine-kernel universality (Thm 20.3) |
| Lubinsky, "Universality limits for random matrices and de Branges spaces of entire functions", J. Funct. Anal. 256 (2009), 3688-3729 | SECONDARY (abstract via search result; full text not read) | Universality limits are reproducing kernels of de Branges spaces equal to Paley-Wiener spaces |
| Danka-Totik, "Christoffel functions with power type weights", JEMS 20 (2018), 747-796 | SECONDARY (EMS abstract level) | Asymptotics for power-type weights on unions of curves/arcs; the limit again involves the equilibrium measure |

**Theorem 20.3 verbatim** (Simon's survey): "Under the hypotheses of Theorem 17.3, for **a.e.**
$x_\infty$ in $I$, we have uniformly for $|a|,|b| < A$,
$\lim K_n(x_\infty+\frac an, x_\infty+\frac bn)/K_n(x_\infty,x_\infty) = \frac{\sin(\pi\rho_e(x_\infty)(b-a))}{\pi\rho_e(x_\infty)(b-a)}$."

**Verdict: MIRAGE, exactly as the TODO caution pre-registered.** Universality inherits Totik's
Theorem 17.3 hypotheses wholesale and delivers a rescaled local limit at a.e. point of an
interval of the support. It is the canonical Level-3 statement: the sine kernel is the same for
zeta's zeros, for D-H's zeros, and for a density-matched Beurling comb. The de Branges variant
(JFA 2009) is the same content in the gauge e1u lives in, which is precisely why it must be
named and refused rather than mistaken for a chain-side gain.
**Four-level call: Level 3.**

---

## SECTION 3. THE UNIFORMITY MACHINERY: WIDOM FACTORS AND THICKNESS (STRAND B)

This is the strand that actually answers "when is a growth quantity uniformly controlled",
which is what the clause needs. It is therefore the strand where the sweep's structural verdict
is decided.

| source | tier | what it gives |
|---|---|---|
| Christiansen, Simon, Zinchenko, "Widom Factors and Szegő-Widom Asymptotics, a Review", arXiv:2112.06450 | FETCHED (full PDF text; Sections 1-2 read verbatim) | Widom factor definition (1.6); Schiefermayr bound $W_n \ge 2$; Parreau-Widom definition (2.11); **Theorem 2.1**; Totik-Widom bounds; Open Problem 2.2; the unboundedness examples |
| Eichinger, arXiv:2204.05633 (as above) | FETCHED | The Carleson-homogeneity definition verbatim, and the Widom criterion route to regularity |

**The controlling condition, verbatim** (arXiv:2112.06450, eq. (2.11) and Theorem 2.1): a
regular compact $e \subset \mathbb{R}$ is **Parreau-Widom** if
$\mathrm{PW}(e) := \sum_j G(c_j) < \infty$ over the critical points $c_j$ of the Green's function
in the gaps; and "**Theorem 2.1** If $e \subset \mathbb{R}$ is a PW set, then the Widom factors
are bounded. Explicitly, $\|T_n\|_e \le 2\exp(\mathrm{PW}(e))\,C(e)^n$." Remark (ii) of that
theorem: "Examples of PW sets include finite gap sets but also sets that are homogeneous in the
sense of Carleson, e.g., fat Cantor sets." And PW sets "are known to have **positive Lebesgue
measure**."

**Carleson homogeneity, verbatim** (Eichinger, arXiv:2204.05633, p. 4): "$E$ for which there
exists $\tau > 0$ so that $|E \cap [\xi_0-\varepsilon, \xi_0+\varepsilon]| \ge \tau\varepsilon$,
$\forall \xi_0 \in E$, $\forall \varepsilon \in (0,1]$", with $|\cdot|$ Lebesgue measure.

**The obstruction, stated sharply (this is the sweep's headline structural finding).**
Every boundedness theorem in this strand is conditioned on the support being **THICK**:
positive Lebesgue measure, locally quantified (homogeneous, Parreau-Widom,
regular-with-positive-a.c.-density). The chain's spectrum, at finite $\lambda$ AND in the limit,
is a **discrete set** (finitely many atoms at finite $\lambda$; the zero set of $\Xi$ in the
limit). A discrete set is Lebesgue-null, so it is neither homogeneous nor Parreau-Widom, and the
Totik-Widom apparatus does not apply. (A precision note, stated conservatively: the strand's
hypotheses are on $E = \sigma_{\mathrm{ess}}$, and for a spectrum that is discrete with no finite
accumulation point $\sigma_{\mathrm{ess}}$ is empty outright, which would degenerate the Martin /
Parreau-Widom apparatus a fortiori. This note does NOT claim to settle what
$\sigma_{\mathrm{ess}}$ of the limit chain is, only that on either reading, empty or
Lebesgue-null, the thickness hypotheses fail.) Moreover the corpus knows the failure mode is real, not
just unproven: Widom factors are UNBOUNDED for the Julia set of $(z-\lambda)^2$ with
$\lambda>2$ (their [9]) and can grow subexponentially of any prescribed order on thin
Cantor-type sets (Goncharov-Hatinoğlu, their [24]); the best general result for uniformly
perfect $e$ is only $W_n(e) = O(n^c)$ (Andrievskii, their [6]); and their **Open Problem 2.2**
asks whether ANY measure-zero set has bounded Widom factors. The clause's prefactor layer is
therefore an OPEN PROBLEM of the corpus itself, on the side of the dichotomy where the corpus
has no positive results at all.

**Verdict: OBSTRUCTION O2 (structural inapplicability) reinforced by O4 (no extension past the
thickness ceiling; the corpus's own open problem).**
**Four-level call: Level 3 in content** (a statement about the metric thickness of a spectrum,
shared by any density-matched comb of the same support geometry), **but the right SHAPE for
Level 4** in the sense that a genuine Widom-factor theorem for a Lebesgue-null arithmetic
support would be a new kind of theorem. That is the follow-on rung, not a finding.

**D-H gate**: unposable as a discriminator. D-H's zero set is also discrete and also
Lebesgue-null; both fail the same hypothesis. Nothing here separates them.
**Beurling gate**: the density-matched Beurling comb has a discrete atom set of matched
density; it fails the same hypothesis identically. Nothing here separates them.

---

## SECTION 4. THE SUM-RULE / RIGIDITY STRAND (STRAND C)

This is #170's named "proven neighboring template". The sweep sharpens why it is a template and
not a tool.

| source | tier | what it gives |
|---|---|---|
| Killip, Simon, "Sum rules for Jacobi matrices and their applications to spectral theory", Ann. of Math. 158 (2003), 253-321 | FETCHED (full PDF text; Introduction read verbatim) | **Theorem 1** (the Hilbert-Schmidt classification), the **P2 sum rule** (1.23), Theorems 2, 5, 6 |
| Bessonov, Denisov, "A spectral Szegő theorem on the real line", Adv. Math. (2020), arXiv:1711.05671 | FETCHED (full PDF text; Theorems 1 and 2 read verbatim) | Exact two-sided characterization of the Szegő class in terms of the Hamiltonian of the canonical system, and its Krein-string form |
| Bessonov, Denisov, "Szegő condition, scattering, and vibration of Krein strings", Invent. Math. 234 (2023), 291-373, arXiv:2203.07132 | SECONDARY (located, abstract level) | The dynamical characterization; the same Szegő-side conditioning |
| Nazarov, Peherstorfer, Volberg, Yuditskii, "On generalized sum rules for Jacobi matrices", IMRN (2005) | SECONDARY (located via citing descriptions only; NOT read) | The higher-order sum-rule programme; cited only as a pointer |

**Killip-Simon Theorem 1 verbatim (conditions (0)-(3)):** $J - J_0$ Hilbert-Schmidt iff
(0) Blumenthal-Weyl (essential spectrum $[-2,2]$ plus eigenvalues accumulating only at $\pm2$),
(1) **quasi-Szegő** $\int_{-2}^{2}\log[f(E)]\sqrt{4-E^2}\,dE > -\infty$ with
$\mu_{ac} = f\,dE$, (2) Lieb-Thirring $\sum|E_j^{\pm}\mp2|^{3/2} < \infty$, (3) normalization.
The engine is the P2 sum rule (their (1.23)), every term of which is nonnegative:
$$\frac{1}{2\pi}\int_{-\pi}^{\pi}\log\Big(\frac{\sin\theta}{\mathrm{Im}\,M(\theta)}\Big)\sin^2\theta\,d\theta \;+\; \sum_j\big[F(E_j^+)+F(E_j^-)\big] \;=\; \tfrac14\sum_j b_j^2 + \tfrac12\sum_j G(a_j).$$

**Bessonov-Denisov Theorem 1 verbatim:** "An even measure $\mu \in \Pi(\mathbb{R})$ belongs to
the Szegő class $Sz(\mathbb{R})$ **if and only if** some (and then every) Hamiltonian
$H = \mathrm{diag}(h_1,h_2)$ generated by $\mu$ is such that
$\sqrt{\det H} \notin L^1(\mathbb{R}_+)$ and
$\widetilde K(H) = \sum_{n\ge0}\big(\int_{\eta_n}^{\eta_{n+2}}h_1 \cdot \int_{\eta_n}^{\eta_{n+2}}h_2 - 4\big) < \infty$",
with $\eta_n$ the $\sqrt{\det H}$-arclength partition (their (1.5)), and the Krein-string form as
their Theorem 2.

**Verdict: OBSTRUCTION O2, and it is worth stating precisely because this strand LOOKS like
exactly what the clause wants.** Bessonov-Denisov is a genuine, two-sided, quantitative
Hamiltonian-side characterization of a spectral condition: the right SHAPE for a
$\lambda$-uniform chain statement. But the spectral condition it characterizes is the **Szegő
condition on the a.c. part**, $\int \log w(t)/(1+t^2)\,dt > -\infty$. The chain's spectral
measure is purely singular (finitely atomic at each $\lambda$; discrete in the limit), so
$w \equiv 0$, the entropy $K(\mu) = +\infty$, and the measure is on the non-Szegő side. The
theorem is TRUE and VACUOUS for our object: it says $\widetilde K(H) = \infty$, i.e. the
det-defect sum diverges, which is exactly e1u's measured degenerate-boundary behaviour
($\delta_K$ spanning $10^{-2}$ down to $9.2\times10^{-14}$) and carries no zero-location
content. Killip-Simon has the same shape of conditioning: its quasi-Szegő clause (1) is a
statement about $f = d\mu_{ac}/dE$, and its clause (0) takes the essential spectrum as INPUT
(which is #170's "support/sign as inputs", here sharpened: it is not only that the support is an
input, it is that the OUTPUT term is a functional of an a.c. part our object does not have).

**A structural corollary worth recording** (with its caveat): Bessonov-Denisov's necessary
condition $\sqrt{\det H} \notin L^1$ fails immediately for any Hamiltonian built entirely of
**indivisible intervals** ($H_k = u_ku_k^\top$ rank one, so $\det H \equiv 0$ pointwise), which is
exactly e1u's Kac-Krein footprint chain. So "a chain of indivisible intervals is never in the
Szegő class" reads off their theorem in one line. CAVEAT, not resolved here: their theorem is
stated for DIAGONAL Hamiltonians generated by $\mu$, and e1u's chain is rank-one-projection
valued, not diagonal; the one-line reading is legitimate for the diagonal Hamiltonian a purely
discrete even measure generates (its indivisible pieces alternate $h_1 = 0$ and $h_2 = 0$, so
$h_1h_2 = 0$ a.e.), and the gauge dictionary between the two forms is NOT checked here. Flagged
as a VERIFIER-adjacent item in Section 10.

**Four-level call: Level 3 in effect.** A statement about the a.c. part is exactly a statement
about the part of the spectrum that carries no individual-zero information.
**D-H gate**: unposable/identical. D-H's completed object also has purely discrete spectrum;
same side of the dichotomy.
**Beurling gate**: identical. Nothing separates.

---

## SECTION 5. STRANDS THAT HAVE THE RIGHT SHAPE (THE THREE NEAR-MISSES)

Pre-registered definition: H1 and H2 satisfied, source in the excluded list (a)-(d); recorded as
NEAR-MISS and upgraded only if a named checkable route from Euler+lattice to the mechanism's
hypothesis is exhibited. None of the three upgrades.

### NEAR-MISS 1. The Steklov extremal problem (family-uniform pointwise growth, done properly)

| source | tier | what it gives |
|---|---|---|
| Aptekarev, Denisov, Tulyakov, "On a problem by Steklov", arXiv:1402.1145 (v2, 2015) | FETCHED (full PDF text; abstract and Introduction read verbatim) | The Steklov class $S_\delta$; the extremal quantity $M_{n,\delta}$; the sharp two-sided bound |

**Verbatim:** "Given any $\delta\in(0,1)$, we define the Steklov class $S_\delta$ to be the set of
probability measures $\sigma$ on the unit circle $\mathbb{T}$, such that
$\sigma'(\theta) \ge \delta/(2\pi) > 0$ at every Lebesgue point of $\sigma$. ... Fix $n$ and define
$M_{n,\delta} = \sup_{\sigma\in S_\delta}\|\varphi_n\|_{L^\infty(\mathbb{T})}$. Then we prove
$C(\delta)\sqrt n < M_{n,\delta} \le \sqrt{(n+1)/\delta}$." The paper records Rakhmanov's 1979
disproof of Steklov's conjecture ($\limsup|P_n(0)| = \infty$ for a weight in the class).

**Why this is the sweep's best structural match**: it is a genuine **uniform-over-a-CLASS,
pointwise** growth theorem, i.e. H1 and H2 both satisfied, with the constant depending only on
the class parameter $\delta$. That is exactly the logical shape the clause needs, and it is the
only place in the OP corpus proper where that shape is realized.
**Why it does not upgrade**: the class is defined by $\sigma' \ge \delta > 0$, excluded source (c).
It is an a.c.-density hypothesis, maximally far from a purely atomic measure. And what it buys is
a polynomial ($\sqrt n$) bound INSIDE the support, not a bound at a gap point. There is no route
from an Euler-product/lattice input to a lower bound on an a.c. density our object does not have.
**Four-level call: Level 3.** **D-H and Beurling gates: unposable for both** (neither control has
an a.c. spectral density either), so H4 cannot even be run: an independent disqualification.

### NEAR-MISS 2. Diophantine uniformity in quasi-periodic spectral theory

| source | tier | what it gives |
|---|---|---|
| Bourgain, Goldstein, "On nonperturbative localization with quasi-periodic potential", Ann. of Math. 152 (2000), 835-879 | SECONDARY (bibliographic and descriptive; NOT read this session) | The archetype: a Diophantine condition on the frequency buys nonperturbative localization / uniform large-deviation control of transfer matrices |
| Eichinger-Lukic, arXiv:2001.00875, Theorems 1.15, 1.16 | FETCHED (full text) | Ergodic-family regularity iff density of states equals Martin measure; positive Lyapunov exponent forces zero-Hausdorff-dimension spectral type |

**Why it is a near-miss**: this is the one place in the neighbouring literature where an
**arithmetic (Diophantine) hypothesis on positions/frequencies genuinely buys uniformity** over a
parameter family. The shape "$\mathbb{Q}$-linear independence, quantified, implies uniform
control" is realized there and nowhere in the Christoffel corpus proper.
**Why it does not upgrade**: (i) the Diophantine condition constrains the frequency of the
COEFFICIENTS (a quasi-periodic potential), not the positions of the spectral atoms, which is the
opposite side of the inverse-spectral correspondence from the clause; (ii) the uniformity bought
is a LOWER bound on Lyapunov exponents (localization), i.e. MORE growth, while the clause needs
an upper bound on growth; (iii) the target family $\{\mu_\lambda\}$ is not ergodic and has no
frequency to be Diophantine about. No named route exists from Euler+lattice to this hypothesis.
**Four-level call: Level 3.** **D-H gate**: unposable (no quasi-periodic structure to posit).
**Beurling gate**: unposable for the same reason, so the gate is unrunnable, which under H4 is an
independent disqualification.

### NEAR-MISS 3. Baker-type lower bounds on log-prime gaps (the only ARITHMETIC source found)

This is the S4-side half of the sweep question, and it is the only mechanism the sweep found
whose source is genuinely Euler-side.

**The observation** (elementary, stated here because it is what the Section 1.1 identity forces):
the denominators in $K_M(x_0,x_0) = \sum_j w_j^{-1}\prod_{i\ne j}(x_0-x_i)^2/(x_j-x_i)^2$ at the
log-prime comb are $|k\log p - k'\log p'| = |\log(p^k/p'^{k'})|$, i.e. **linear forms in
logarithms of primes**. Baker-type effective lower bounds therefore control the
small-denominator layer of the log-prime comb's Christoffel function; and they FAIL, for a
nameable reason, for a Beurling generalized-prime system (a Beurling system's generators are
arbitrary positive reals with no unique-factorization constraint, so by Dirichlet's approximation
theorem one can arrange near-coincidences $|k\log q_i - k'\log q_j|$ as small as desired at
bounded height). That is a real Euler-gated discriminator with a real Beurling failure.

**Why it does not upgrade to a HIT**: the layer is wrong. Section 1.2's measurement shows the
small-denominator/relocation layer is a BOUNDED prefactor effect, dominated 30x by the
density-forced rate layer at $M = 192$. Controlling it therefore cannot supply the
$\lambda$-uniform statement the clause needs, because the clause's uniformity bill is charged in
the rate layer first. And this is not a new verdict for the repo: it independently reproduces
[`e2ii_transcendence_bridge.md`](../../../experiments/arithmetic_geometric/e2ii_transcendence_bridge.md)'s
finding (LEARNINGS #62) that the Weil positivity margin sits a factor ~25 ABOVE the effective Diophantine gap
scale, so that "positivity does not obviously live at the transcendence (Baker) scale". Two
gauges, one verdict. That note also records the deflating fact that the QUALITATIVE
$\mathbb{Q}$-independence of $\{\log p\}$ is elementary (unique factorization), so only the
EFFECTIVE version is a real import, and only into the prefactor layer.
**Four-level call: Level 4 in TYPE** (an effective transcendence statement is not a statistical
statement), **but off-target in OBJECT.**
**D-H gate: PASSES (unposable).** D-H has no Euler product, so it has no log-prime comb at all;
the mechanism cannot be stated for it. This is a type refusal in the e1n/e1o sense.
**Beurling gate: PASSES (nameable failure).** As above.
**Honest scope**: the Baker route is recorded as a NEAR-MISS on the strength of its DISCIPLINE
behaviour, which is the best of anything in the sweep. It fails on target, not on discipline.

---

## SECTION 6. THE HYPOTHESIS-FREE RESIDUE, AND THE RH-ADJACENT OP CORPUS

### 6.1 What the corpus proves with NO thickness or regularity hypothesis

Three items, all from Simon's survey [FETCHED]:

1. **The atom limit** (Section 9): $K_n(x_0,x_0) \uparrow \mu(\{x_0\})^{-1}$, infinite if
   $\mu(\{x_0\}) = 0$ (his lines around (9.22)-(9.26)). So at a non-atom footpoint the Christoffel
   function goes to zero unconditionally, and the entire clause is about the RATE, never the
   limit.
2. **Markov-Stieltjes inequalities** (Section 7, Lemma 7.1 and its consequences): universal
   two-sided bounds sandwiching partial sums of Christoffel numbers between $\mu$-measures of
   intervals. Hypothesis-free, and **purely density data**.
3. **Regularity's exponential bound** (Theorem 12.1): for $e$ Dirichlet-regular and $\mu$ regular
   for $e$, $\sup_{\mathrm{dist}(z,e)<\delta}|p_n(z)| \le C_\varepsilon e^{\varepsilon|n|}$; and
   (Theorem 12.2) the zero-counting measures converge weakly to the equilibrium measure $\rho_e$.

**Verdict: OBSTRUCTION O3, the conservation-law confirmation.** Everything the corpus gives
without a thickness hypothesis is a functional of the counting measure or of the support. That is
the DMV-screened, density-typed part: exactly the part the e1u round measured to be family-blind
after band equalization (U3d), and exactly the part the Beurling control is built to share.

### 6.2 The RH-adjacent orthogonal-polynomial corpus (repo-absent, and honestly graded)

| source | tier | repo status | grade |
|---|---|---|---|
| Romik, "Orthogonal polynomial expansions for the Riemann xi function", arXiv:1902.06330 (86 pp.) | FETCHED (full PDF text; Introduction, concluding open problems, section headers read) | **ZERO repo mentions** (ripgrep, whole tree) | NEW POINTER, not a mechanism |
| Griffin, Ono, Rolen, Zagier, "Jensen polynomials for the Riemann zeta function and other sequences", PNAS 116 (2019), arXiv:1902.07321 | SECONDARY (abstract and description; the repo already carries a GORZ scoping note, LEARNINGS #170) | present (as the "GORZ discrepancy") | MIRAGE exemplar |
| Suzuki, arXiv:1204.1827 / arXiv:1606.05726 | already pinned in [`remling_suzuki_canonical_pin.md`](remling_suzuki_canonical_pin.md) | present | unchanged |

**Romik.** Expands $\Xi(t)$ in three orthogonal-polynomial families: Hermite (Turán's 1950s
programme), symmetric Meixner-Pollaczek, and continuous Hahn (both new), with coefficient
formulas, sign alternation, and asymptotics; the author's own framing is that "the theory of
orthogonal polynomials may have a more central role to play in the study of the zeta function
... than had been previously suspected", and the RH connection runs through hyperbolicity of
expansions and the de Bruijn-Newman flow (his Section 3.5 and open problems 1-4). **Grade: a
genuine repo gap in the OP direction, but NOT a Christoffel mechanism** (the string "Christoffel"
does not occur in the extracted text; checked by ripgrep). It belongs to the repo's
`experiments/criticality/` de Bruijn-Newman thread, not to this clause. Recorded so it is not
lost; see Section 10.

**GORZ, as the pre-registered mirage exemplar with a real RH pedigree.** The Pólya-Jensen
criterion is RH-equivalent (hyperbolicity of the Jensen polynomials $J^{d,n}$ for all $d$ and all
$n$); GORZ prove it **for each fixed $d$ and all sufficiently large $n$**, via Hermite-polynomial
approximation, plus all $d \le 8$. That is precisely the shape Section 0.4 pre-named: a sharp,
quantitative, hard theorem whose logical form (asymptotic in one index at fixed other index)
leaves the RH-equivalent conjunction untouched. It is the clearest available demonstration that
"asymptotic in $n$ at fixed $d$" is not "uniform", which is the exact failure mode the growth
clause is about. **Four-level call: Level 3 as a criterion-closer**, notwithstanding that its
object is Level 4.

---

## SECTION 7. SCORECARD

Grades: **HIT** / **NEAR-MISS** / **MIRAGE** / **OBSTRUCTION**, against Section 0's criteria.

| # | Mechanism | H1 pointwise | H2 family-uniform | H3 structural source | H4 D-H fails | H4 Beurling fails | Level | Grade |
|---|---|---|---|---|---|---|---|---|
| A1 | Máté-Nevai-Totik Christoffel asymptotics | NO (a.e.) | NO (fixed $\mu$) | NO (c: Szegő/a.c.) | no | no | 3 | MIRAGE + O2 |
| A2 | Totik general-measure extension (Thm 17.3) | NO (a.e.) | NO | NO (b+c: Reg + local Szegő) | no | no | 3 | MIRAGE + O2 |
| A3 | Eichinger continuum Christoffel (Thm 1.1) | YES on $I$ | YES on $I$ | NO (b+c; needs $\xi\in\mathrm{int}\,E$) | no | no | 3 | OBSTRUCTION O2 |
| A4 | Lubinsky bulk universality (Thm 20.3) | NO (a.e.) | NO | NO (inherits A2) | no | no | 3 | MIRAGE |
| A5 | Lubinsky de Branges universality (JFA 2009) | NO | NO | NO | no | no | 3 | MIRAGE |
| A6 | Danka-Totik power-type weights | partial | partial | NO (c: power-type a.c. weight) | no | no | 3 | MIRAGE |
| B1 | Widom factors / Totik-Widom bound (Thm 2.1) | YES | YES | NO (b: Parreau-Widom thickness) | no | no | 3 | OBSTRUCTION O2 + O4 |
| B2 | Carleson homogeneity | YES | YES | NO (b: positive Lebesgue measure) | no | no | 3 | OBSTRUCTION O2 |
| B3 | Stahl-Totik root asymptotics (E-L Thm 1.5(vi)) | YES | n/a (asymptotic) | NO (b: support only) | no | no | 3 | OBSTRUCTION O3 |
| B4 | Eichinger-Lukic universal lower bound (Thm 1.3) | YES | YES | NO (b: support only) | no | no | 3 | OBSTRUCTION O3 |
| B5 | Thouless formula | YES | n/a | NO (a: density of states) | no | no | 3 | OBSTRUCTION O3 |
| C1 | Killip-Simon P2 sum rule / Thm 1 | n/a | n/a | NO (c: quasi-Szegő; support as input) | no | no | 3 | OBSTRUCTION O2 |
| C2 | Bessonov-Denisov canonical-system Szegő (Thms 1, 2) | n/a | YES (quantitative) | NO (c: finite log integral) | no | no | 3 | OBSTRUCTION O2 |
| C3 | Higher-order sum rules (NPVY, Denisov-Kupin) | n/a | n/a | NO (c) | no | no | 3 | pointer only, NOT READ |
| D1 | Steklov extremal problem (ADT sharp $\sqrt n$) | YES | YES | NO (c: $\sigma'\ge\delta$) | unposable | unposable | 3 | NEAR-MISS |
| D2 | Diophantine/quasi-periodic uniformity (BG) | YES | YES | arithmetic but WRONG OBJECT | unposable | gate unrunnable | 3 | NEAR-MISS |
| D3 | Baker bounds on $\lvert k\log p - k'\log p'\rvert$ | YES | YES | **YES (Euler side)** | **YES (unposable)** | **YES (nameable)** | 4 in type | **NEAR-MISS** (wrong layer) |
| E1 | Markov-Stieltjes inequalities | YES | YES | NO (a: density) | no | no | 3 | OBSTRUCTION O3 |
| E2 | $K_n(x_0,x_0)\uparrow\mu(\{x_0\})^{-1}$ | YES | YES | NO (trivial) | no | no | 3 | OBSTRUCTION O3 |
| F1 | GORZ Jensen polynomials | n/a | **NO** (fixed $d$, large $n$) | RH-equivalent object | n/a | n/a | 3 | MIRAGE exemplar |
| F2 | Romik OP expansions of $\Xi$ | n/a | n/a | n/a (not a growth mechanism) | n/a | n/a | 4 in object | NEW POINTER |

**Count: 0 HIT, 3 NEAR-MISS, 6 MIRAGE, 11 OBSTRUCTION-or-pointer.**

---

## SECTION 8. DISCIPLINE GATES, RUN EXPLICITLY

### 8.1 Davenport-Heilbronn

The D-H gate is run mechanism by mechanism in the Section 7 table. The aggregate result is the
important one, and it is negative in an informative way:

> Of the 20 mechanisms scored, exactly ONE (D3, the Baker layer) is unposable for D-H, and it is
> unposable for the standard reason (no Euler product, hence no log-prime comb). **Every single
> mechanism in the Christoffel corpus proper runs identically for D-H.** Its zero set is
> discrete, Lebesgue-null, has a central gap (at 4.9 rather than 13.6), and has the same
> Riemann-von-Mangoldt-shaped counting law up to conductor rescaling. Every hypothesis in
> Sections 2-4 and 6.1 is satisfied or violated identically by both objects.

This is a re-derivation of the e1u U2c verdict from the literature side, and it is the sharpest
form of the finding: the Christoffel corpus is not a wrong-approach detector's near-miss, it is
**structurally blind to the D-H / zeta distinction**, because everything it controls is a
functional of the support geometry and the a.c. part, and the two objects agree on the first and
both have none of the second. Section 1.2's measurement quantifies the one place they DO differ
under a corpus-native instrument (the gap half-width, 13.6 vs 4.9, moving the rate by 0.17 per
atom), and that difference is first-zero-position data, which e1u already typed as
density-adjacent and gate-confounded.

### 8.2 Beurling

The Beurling gate is sharp here exactly as the tasking said, because the
atoms-at-$\mathbb{Q}$-linearly-independent-positions condition is where the lattice enters.

> The density-matched Beurling control shares, by construction, the counting measure of the
> comb. Therefore it shares the **entire rate layer** (Section 1.2; Sections 3 and 6.1: Martin
> function, Green's function, Thouless potential, equilibrium measure, Markov-Stieltjes bounds,
> regularity). **Every mechanism graded OBSTRUCTION O3 in the scorecard is Beurling-satisfiable
> by construction, i.e. weightless in the #152 sense.** Every mechanism graded OBSTRUCTION O2
> fails identically for both (both spectra are discrete and Lebesgue-null, both spectral measures
> are purely singular).
>
> The single exception, and the only place in the whole sweep where the Beurling control can be
> made to fail for a nameable reason, is D3: Baker-type lower bounds on
> $|k\log p - k'\log p'|$ have no Beurling analogue, because Beurling generators carry no
> unique-factorization constraint and admit arbitrarily good near-coincidences at bounded
> height. That is a genuine lattice/Euler discrimination, and it lives entirely in the
> **prefactor** layer, which the same section measures at 30x smaller than the rate layer.

**Net for the Beurling discipline**: the sweep confirms the #152 fourth clause in a new corpus.
A Christoffel-side mechanism that consumes only support/density data is exactly what the fake
satisfies, and that is 19 of the 20 mechanisms surveyed.

### 8.3 Four-level framing

Every mechanism's level is in the Section 7 table. Summary: **19 of 20 are Level 3**; the one
Level-4-in-type item (D3, Baker) is off-target in object; the one Level-4-in-object item (F2,
Romik) is not a growth mechanism. This is the four-level framing doing exactly the job
`CLAUDE.md` describes: separating "sharp and hard" from "RH-closing". The Christoffel corpus is
uniformly the former.

---

## SECTION 9. VERDICT, DISCREPANCY LOG, AND VERIFIED ABSENCES

### 9.1 The direct answer to the sweep question

> **Does anything in this corpus give the growth clause a structural (Euler + lattice) source, or
> is the clause still exactly as open as #160 left it?**

**The clause is exactly as open as #160 left it.** Nothing in the Christoffel-function /
orthogonal-polynomial growth corpus supplies a $\lambda$-uniform pointwise control at a footpoint
with an arithmetic source. The pre-registered exit (Section 0.7) therefore FIRES: the Christoffel
costume is a **coordinate change, not a reduction**, which is the #160 / #171 pattern for the
fourth time. The corridor's conservation law holds again, in a corpus it had never been tested
against.

**The sweep does not return empty-handed, and the gain is a sharpening of the "why".** Before
this sweep the status was "no mechanism found". After it, the status is:

1. The clause **splits into two layers** with different discipline verdicts (Section 1.2,
   evidence-checked 11/11): a RATE layer that is provably density-typed and therefore
   Beurling-satisfiable and D-H-blind, and a PREFACTOR (Widom-factor) layer that is 30x smaller
   at $M=192$ and is where any arithmetic input would have to act.
2. The corpus's uniformity machinery is not silent about our object, it is **structurally
   inapplicable to it**, along a single named axis: **thickness**. Every uniformity theorem
   (Widom-factor boundedness, Carleson homogeneity, Parreau-Widom, doubling, Steklov, the
   Christoffel asymptotics, the sum rules) is conditioned on a spectrum with positive Lebesgue
   measure and/or a positive a.c. density. The chain's spectrum is discrete and Lebesgue-null.
   Whether ANY Lebesgue-null set has bounded Widom factors is **the corpus's own Open Problem
   2.2** (arXiv:2112.06450). So the clause is not merely unproven here; the corpus has no
   positive results at all on the side of the dichotomy the clause lives on.
3. The only arithmetic mechanism the sweep found (D3, Baker) **passes both discipline gates** and
   fails on target rather than on discipline, which is a new and unusually clean data point: it
   is the first item in this corridor that is D-H-unposable AND Beurling-failing AND
   quantitatively bounded in its effect.

That is a narrowing, not a wall: it says where a Christoffel-side mechanism would have to live
(the prefactor layer, at a Lebesgue-null arithmetic support) and it says that spot is empty in
the literature rather than occupied by an obstruction theorem.

### 9.2 Discrepancy log (flagged, not resolved: SURVEYOR reports, ADVERSARY / VERIFIER decide)

- **D-LOG-1 (a sharpening, arguably a correction, of #170's Killip-Simon gloss).** LEARNINGS #170
  records Killip-Simon as "the PROVEN neighboring template (sum rule + Helly + semicontinuity,
  but with support/sign as INPUTS)". That is right as far as it goes, but the sweep finds a
  stronger reason the template cannot be instantiated: the OUTPUT term of the sum rule is a
  functional of the a.c. part ($\int\log f$), and our object has none. Support-as-input is a
  fixable-looking defect; a vacuous output term is not. The same applies to Bessonov-Denisov.
  Recommend an ADVERSARY or SYNTHESIZER decide whether #170's phrasing should be amended.
- **D-LOG-2 (a scope question on e1u VERIFIER target 6).** e1u names as a target: "for an even
  atomic probability measure with no atoms in $(-g,g)$, the footprint chain's total trace-length
  grows like the reciprocal Christoffel function at 0 (exponential in $M$ at fixed gap
  fraction)". Section 1.1 shows the first half is an IDENTITY (trace-length = reciprocal
  Christoffel + second-kind twin, exactly), not an asymptotic; the substantive half is the
  exponential growth, which is the finite shadow of Eichinger-Lukic Theorems 1.3/1.5(vi). This
  note's C2 measures it at FIXED window top rather than at fixed gap fraction and finds the
  per-atom rate RISING (0.187 to 0.291), which is consistent but is not the normalization e1u
  stated. Flagged: the target's exact hypothesis should be pinned before formalization, and the
  identity half should be split off as a separate (much easier) Lean target.
- **D-LOG-3 (no discrepancy; an independent reconfirmation worth logging).** Section 5's
  NEAR-MISS 3 reaches, from the Christoffel side, the same verdict
  `e2ii_transcendence_bridge.md` reached from the Weil-form side: the Baker/Diophantine layer
  sits an order of magnitude below the discriminating signal (25x there, 30x here). Logged so the
  SYNTHESIZER can decide whether this counts as a second independent confirmation of that
  finding, and whether the "candidate F is shallow" verdict should be upgraded in confidence.
- **D-LOG-4 (process, self-reported).** The first run of this note's evidence script scored 6/9.
  Two of the three failures were my own thresholds conflating the rate layer with the prefactor
  layer (a 2% drift criterion applied to a quantity that legitimately drifts 11% at fixed $M$ for
  a 0.45 relocation), and one was a stale absolute threshold carried over from a different grid.
  The criteria were re-specified to test the two layers separately (bounded vs
  proportional-to-$M$ drift), which is a strictly better test, and the script now scores 11/11.
  The Section 0 HIT/MIRAGE/OBSTRUCTION criteria were NOT touched at any point. Recorded rather
  than hidden, per the repo's threshold-provenance discipline.

### 9.3 Verified absences (search-level, with the caveat stated)

Each of these was searched this session with targeted queries and returned nothing on point.
These are **search-level absences**, not proofs of non-existence, and should be read the way
[`kns_log_growth_pin.md`](kns_log_growth_pin.md) reads its own fidelity caveat.

1. **"Christoffel function" plus arithmetic.** No paper found connecting Christoffel functions or
   orthogonal-polynomial growth to Euler products, primes, or L-functions. (Queries run against
   "Christoffel function" with "Euler product", "prime numbers", "L-function", "arithmetic
   measure".)
2. **"Christoffel function" plus Diophantine / $\mathbb{Q}$-linear independence.** No paper found
   treating Christoffel functions for measures whose atoms are constrained by a Diophantine or
   rational-independence hypothesis. The searches return quasi-conformal Jacobi-measure papers
   and exceptional-OP papers, none on point.
3. **Christoffel functions at gap points of purely atomic measures.** No dedicated treatment
   found. The corpus treats gap points only through root asymptotics (Martin / Green function),
   and treats atomic measures only through point-mass insertion formulas (Geronimus / Uvarov;
   Simon's Section 24, Theorems 24.1-24.3).
4. **Family-uniform Christoffel bounds without a thickness hypothesis.** None found. Every
   uniformity result located is conditioned on a.c. density, doubling, homogeneity,
   Parreau-Widom, or varying-weight smoothness.
5. **A Widom-factor-type theorem for a Lebesgue-null arithmetic support.** None found, and the
   corresponding general question is the corpus's own stated Open Problem 2.2.

### 9.4 Honest limits of this sweep

- Nevai's 1986 memoir (167 pp.) is the field's foundational Christoffel-function survey and was
  NOT read; it is cited as a bibliographic pointer only. If any mechanism hides anywhere, that is
  the likeliest place, and a targeted read of its at-a-point sections is the cheapest residual.
- Totik (2000) and Máté-Nevai-Totik (1991) were pinned through Simon's survey, which quotes them
  with theorem numbers and hypotheses; the original papers were not opened (both paywalled).
  Simon's renderings are the authority used and are labelled SECONDARY throughout.
- The higher-order sum-rule strand (NPVY 2005, Denisov-Kupin, Simon-Zlatoš) was located but not
  read; it is graded "pointer only" in the scorecard and no weight rests on it.
- All PDF extractions this session are pymupdf text dumps read by an LLM, not line-by-line LaTeX
  reads. Theorem numbers and quoted hypotheses are high-confidence (each load-bearing quote was
  read in its own context in the extracted text) but not verified character-by-character against
  the published typeset source.
- The evidence script uses idealized equally-spaced atom families, not the e1u builds. It
  measures the STRUCTURE of the two-layer split, not the e1u objects themselves. Reproducing it
  against the actual e1u Face-A measures is a cheap BUILDER rider (Section 10, item 2).
- The dossier does not attempt to decide whether the LIMIT chain exists or what its spectral
  measure is; it works with "the limit spectral measure is discrete" as the natural reading of
  the Suzuki/CCM picture, which is the reading e1u and #170 already use. If that reading is
  wrong, Sections 3 and 4's obstructions would need re-examination.

---

## SECTION 10. WHAT THIS ENABLES / WHAT REMAINS OPEN

### For BUILDER

1. **The re-posed clause (the sweep's main handoff).** Do not ask for a $\lambda$-uniform bound on
   $K_{M(\lambda)}(0,0)$. That quantity's leading behaviour is forced by the counting measure and
   is provably Beurling-satisfiable. Ask instead for a $\lambda$-uniform bound on the
   **normalized Widom-type residual**
   $$W_\lambda \;:=\; \log K_{M(\lambda)}(0,0) \;-\; 2M(\lambda)\!\int\!\log|t|\,d\nu_\lambda(t)$$
   (or the correct Martin-function normalization for the unbounded support), i.e. what is left
   after the potential-theoretic rate is divided out. That is the only layer where an arithmetic
   input can act, and it is the layer where the corpus has an open problem rather than a theorem.
2. **A cheap rider on e1u** (hours; reuses the tracked harness): recompute Section 1.2's two-layer
   split on the ACTUAL e1u Face-A measures at the 11-build grid, i.e. report $\log X(\lambda)$,
   the potential term $2M\int\log|t|\,d\nu$, and their difference, for ZETA / D-H / BEUR.
   **Prediction, stated in advance** (so it can falsify): the difference (the Widom layer) is
   small, family-mixed, and does not order the families. If it DOES order them, that is the first
   chain-side face the U2c/U3d controls have not already killed, and it is worth a full round.
3. **Do not build a Christoffel-side S4 device.** The S4 spec wants an anomalously LARGE
   Christoffel function at the log-prime nodes (a rank deficiency, cost $o(M)$), and e1o already
   measured full rank with cost ratio 1.000 across all 12 $(\lambda,K)$ cells. Section 1.1's
   identity explains why in one line: distinct nodes give a nonsingular Lagrange/Vandermonde
   system, and the only way to make $K$ anomalous is to make gaps anomalously small, which Baker
   forbids at the log-prime comb. The e1o measurement and the Christoffel identity are the same
   fact seen twice.

### For ADVERSARY

4. **Attack the two-layer split itself.** The claim that the discriminating content cannot live in
   the rate layer rests on "the density-matched Beurling comb shares the counting measure, hence
   the log-potential at the footpoint". Is `experiments/_shared/beurling.py` density-matched
   sharply enough that $\int\log|t|\,d\nu$ agrees to the precision the claim needs? Section 1.2
   assumes it does; that is checkable and was NOT checked here.
5. **Attack D-LOG-1.** Is the "vacuous output term" reading of Killip-Simon / Bessonov-Denisov
   right, or is there a singular-measure analogue of the sum rule (an entropy relative to
   something other than Lebesgue) that restores content? The Bessonov-Denisov $\widetilde K(H)$
   functional is defined on the Hamiltonian side and is dichotomously finite/infinite; is there a
   REGULARIZED version whose finite part carries information on the non-Szegő side? A yes would
   be a genuine reopen of the sum-rule template.
6. **Attack the Section 4 corollary's gauge caveat**: does "a chain of indivisible intervals is
   never in the Szegő class" survive the diagonal-vs-rank-one Hamiltonian dictionary? Stated with
   its caveat in Section 4; not resolved here.
7. **Attack the thickness obstruction from the other side.** Is there a reformulation in which the
   relevant "support" is NOT the discrete zero set but something thick (for example the support of
   a smoothed or averaged version of the chain's spectral measure)? If such a reformulation exists
   and is faithful, Sections 3 and 4 reopen. If it exists but is unfaithful, that is itself worth
   recording as the reason it cannot be used.

### For VERIFIER

8. Two Lean-friendly items fall out of Section 1.1, both finite and algebraic, and both cleaner
   than e1u's VERIFIER target 6 as currently stated (see D-LOG-2):
   - **the atomic reproducing-kernel identity**: for an $M$-atom measure with weights $w_j$ and a
     non-atom point $x_0$, $K_M(x_0,x_0) = \sum_j |L_j(x_0)|^2/w_j$ (a finite rational-function
     identity per $M$; checked here to $2.5\times10^{-58}$ relative deviation);
   - **the trace-length identification**: $X = \sum_k l_k = K_M(0,0) + \sum_k q_k(0)^2$ for the
     Kac-Krein footprint chain, which is e1u target 6's identity half, separated from its
     asymptotic half.

### For SURVEYOR (residuals from this sweep)

9. **Nevai 1986** (the one unread foundational source; Section 9.4).
10. **Romik arXiv:1902.06330** deserves its own reading note in the `criticality/` (de
    Bruijn-Newman) thread, not this one: 86 pages, three OP expansions of $\Xi$, four open
    problems, ZERO repo mentions. It is not a Christoffel mechanism, but it is the OP-side RH
    literature the repo has never mapped, and its Poisson-flow / hyperbolicity questions sit next
    to the repo's existing dBN probes.
11. **ADJACENT-WATCH, found off-axis and handed to the WATCH cadence (next ~2026-08-01):**
    arXiv:2607.24830 (Kim, Hong, Kim, Choi, Jang, Kim; v1 2026-07-23, v2 2026-07-29), "A Numerical
    Realization of Suzuki's Weil-Quadratic-Form Operator: The Archimedean Spectral Law, its
    Universality, and an Operator Form of Weil's Positivity Criterion". [FETCHED, abstract only.]
    The authors state explicitly that "this work does not prove RH"; it is a numerical realization
    of Suzuki's screw-function operator, with a claimed "archimedean spectral law"
    $A_k(a) = \log(1/a) + \log(k-2) + B_0 + O(a)$ whose constant depends only on the conductor,
    and an operator form of Weil positivity in which "an injected off-line zero causes exponential
    blow-up". Relevance flag: that last phrase has the same shape as e1u's U4 entanglement finding
    and as this note's rate-layer blowup, and the archimedean-only scoping is exactly the K2-blind
    half the repo has flagged since LEARNINGS #111. NOT assessed beyond the abstract; no weight
    rests on it.

### For SYNTHESIZER

12. The frontier is **UNMOVED**. The clause is unchanged; what changed is its coordinates and the
    reason for its openness. If this is integrated, the two load-bearing sentences are:
    (i) the growth clause splits into a density-forced RATE layer and a Widom-factor PREFACTOR
    layer, and only the second can carry arithmetic;
    (ii) the entire Christoffel corpus's uniformity machinery is conditioned on spectral
    THICKNESS, and the chain's spectrum is Lebesgue-null, so the corpus sits on the wrong side of
    a dichotomy rather than being merely silent.
    Both are coordinates that narrow the search. Neither is a wall.

---

## SOURCES, BY TIER

**FETCHED at source this session (full PDF text extracted and read in context):**
Simon, arXiv:0806.1528 (CD kernel survey);
Killip-Simon, Ann. of Math. 158 (2003), 253-321;
Christiansen-Simon-Zinchenko, arXiv:2112.06450 (Widom factors review);
Eichinger, arXiv:2204.05633 (continuum Christoffel asymptotics);
Eichinger-Lukic, arXiv:2001.00875 (Stahl-Totik regularity, continuum);
Bessonov-Denisov, arXiv:1711.05671 (spectral Szegő on the line);
Aptekarev-Denisov-Tulyakov, arXiv:1402.1145 (Steklov);
Romik, arXiv:1902.06330 (OP expansions of $\Xi$).

**FETCHED at abstract level only:**
Lasserre, arXiv:2301.11072; Beckermann-Putinar-Saff-Stylianopoulos, arXiv:1812.06560;
Bessonov-Denisov, arXiv:2203.07132; Kim et al., arXiv:2607.24830;
Totik, J. Anal. Math. 81 (2000) via the Springer abstract page.

**SECONDARY (pinned through a source read this session, or through search descriptions):**
Máté-Nevai-Totik, Ann. of Math. 134 (1991), 433-453 (via Simon Thms 17.1-17.2);
Totik, J. Anal. Math. 81 (2000), 283-303 (via Simon Thm 17.3);
Máté-Nevai, Ann. of Math. 111 (1980), 145-154 (via Simon Thm 14.1);
Stahl-Totik, *General Orthogonal Polynomials*, CUP 1992 (via Simon Sections 12-13 and
Eichinger-Lukic Section 1);
Lubinsky, Ann. of Math. 170 (2009), 915-939 (via Simon Thms 20.1, 20.3);
Lubinsky, J. Funct. Anal. 256 (2009), 3688-3729;
Danka-Totik, JEMS 20 (2018), 747-796;
Griffin-Ono-Rolen-Zagier, PNAS 116 (2019) / arXiv:1902.07321;
Remling, Ann. of Math. 174 (2011), 125-171 / arXiv:0706.1101;
Schiefermayr, Goncharov-Hatinoğlu, Andrievskii, Totik, Faber, Szegő (via the Widom review's
numbered bibliography).

**UNVERIFIED-MEMORY / bibliographic pointer only (NOT read this session; no weight rests on
them):**
Nevai, J. Approx. Theory 48 (1986), 3-167;
Nazarov-Peherstorfer-Volberg-Yuditskii, IMRN (2005);
Bourgain-Goldstein, Ann. of Math. 152 (2000), 835-879;
Avron-Simon / Craig-Simon (Thouless formula; log-Hölder IDS);
Levin-Lubinsky, *Christoffel Functions and Orthogonal Polynomials for Exponential Weights*,
Mem. Amer. Math. Soc. 111 (1994), no. 535;
Mastroianni-Totik (doubling and $A_\infty$ weights).

**Repo-internal, cited as evidence:**
[`e1u_canonical_chain.md`](../../../experiments/spectral/e1u_canonical_chain.md) (U1, U2c, U3d,
U4, the price table, VERIFIER target 6);
[`trojan_horse_m4.md`](../trojan_horse_m4.md) Section 8;
`experiments/LEARNINGS.md` #152, #160, #162, #170, #171;
[`e2ii_transcendence_bridge.md`](../../../experiments/arithmetic_geometric/e2ii_transcendence_bridge.md);
[`s4_carrier_audit.md`](../s4_carrier_audit.md) Section 4;
[`kns_log_growth_pin.md`](kns_log_growth_pin.md);
[`remling_suzuki_canonical_pin.md`](remling_suzuki_canonical_pin.md);
[`_evidence/christoffel_gap_growth_check.py`](_evidence/christoffel_gap_growth_check.py) (11/11)
and its tracked output
[`_evidence/christoffel_gap_growth_check.out.txt`](_evidence/christoffel_gap_growth_check.out.txt).
