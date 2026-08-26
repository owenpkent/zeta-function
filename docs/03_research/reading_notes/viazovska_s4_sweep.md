# Reading note: the Cohn-Elkies / Viazovska / Radchenko-Viazovska corpus swept against the banked S4 spec

> SURVEYOR reading note, 2026-08-09. Executes the modular/Hecke rung's sweep half named in
> PHASE_STATE.md next-step 1 and in LEARNINGS #167's own closing pointer ("the
> Cohn-Elkies/Viazovska/Radchenko-Viazovska corpus the frame audit found at ZERO repo mentions
> is now the named next rung from BOTH sides of the pivot"). The corpus had zero repo mentions
> before the 2026-07-17 frame audit
> ([`ccm_corridor_frame_audit.md`](../ccm_corridor_frame_audit.md) Section 2, "Absence claims
> verified in corridor vocabulary only") flagged it as the one field where a one-sided
> band-limited extremal problem WAS closed sharply by a lattice-consuming modular identity.
> Spec swept against: [`s4_carrier_audit.md`](../s4_carrier_audit.md) Section 4 item 5 (the
> banked forcing spec) in its Q4 four-condition form
> ([`theta_s4_build_spec.md`](../theta_s4_build_spec.md) Section 1). Screens applied: the DMV
> kill ([`s4_carrier_audit.md`](../s4_carrier_audit.md) Section 3), the Beurling discipline,
> the frame-vs-collapse discriminator of
> [`kns_log_growth_pin.md`](kns_log_growth_pin.md) Section 5.

## STATUS

- **Date:** 2026-08-09.
- **Verdict: FITS-IN-PART.** Conditions (1) ONE-SIDEDNESS and (4) LATTICE CLAUSE fit fully
  and exactly. Condition (2) CHEAP MULTIPLICITY fits **as a mechanism class at its native
  nodes**: the Viazovska magic function is the first and only known non-arithmetic-progression
  instance of the S4 economy (infinitely many prescribed double zeros paid for by an
  $O(1)$-dimensional modular family), which upgrades the banked S4 spec from "no published
  relative" ([`s4_carrier_audit.md`](../s4_carrier_audit.md) Section 2.5) to "instantiated in
  nature, at quadratic nodes." The **blocking condition is (2) at the log nodes**: the
  identity consumes the integer support of $q$-expansions (the node set $\{\sqrt{n}\}$ is the
  preimage of the integer exponent lattice under $x \mapsto x^2$), and the corpus's own unique
  log-node realization (Bondarenko-Radchenko-Seip, arXiv:2005.02996) shows what the transfer
  produces: an exactly-critical interpolation identity at $\{\log n/(4\pi)\}$ whose **dual node
  set is forced onto the zeta zero multiset**. The mechanism transfers INTO the wall, not
  around it: the S4 device at log nodes sourced by this mechanism class IS the Riemann-Weil
  explicit formula, and its one-sided version IS Weil positivity = M4.
- **Frame-vs-collapse typing (the sweep's sharpest question): the corpus splits into two
  organs.** The interpolation theorems (Radchenko-Viazovska, CKMRV with derivatives) are
  EXACTLY-CRITICAL BASES: free data modulo exactly one linear relation (classical Poisson
  summation), one basis function per node, formula destroyed by removing any single node.
  That is neither a KNS-style oversampled frame nor an S4-style rank collapse: it is the
  boundary case between them. The S4-relevant collapse economy lives exclusively in the
  OTHER organ, the magic-function / LP-sharpness half. Section 4 below.
- **Consequence for #167's "modular forms ARE the tie" reading: a load-bearing caveat.** The
  sphere-packing identities consume $\Gamma_\theta \subset SL_2$ (the additive lattice via
  the translation generator, plus inversion $\tau \mapsto -1/\tau$ = the theta FE). They do
  NOT consume Hecke operators or any multiplicative structure. The Hecke/Euler layer is
  exactly what the log-node transfer adds, and exactly where the zeros appear on the dual
  side. Section 6 (discrepancy log).
- **Verdict calibration (ADVERSARY 2026-08-09,
  [`_modular_rung_adversary.md`](_modular_rung_adversary.md) B2):** read FITS-IN-PART as
  "FITS as mechanism class at native quadratic nodes / M4-EQUIVALENT as a transfer to
  $\{k\log p\}$"; strictly at the spec's node set no Q4 condition is met, so this corpus is
  an existence proof for the S4 economy, not a candidate route around M4.

## 1. Sources

Process rule (#157): every load-bearing statement tagged. All full-text extractions are LLM
summarizations of ar5iv HTML renders (same fidelity caveat as
[`kns_log_growth_pin.md`](kns_log_growth_pin.md) Section 1.1), cross-checked across passes
where load-bearing; not character-by-character reads.

| Source | Tier | What it gives |
|---|---|---|
| Cohn-Elkies, "New upper bounds on sphere packings I," arXiv:math/0110009, Ann. Math. 157 (2003) | FETCHED (abstract; the LP criterion itself fetched via Viazovska's restatement below) | The LP framework; conjectured sharpness in dims 8 and 24 |
| Viazovska, "The sphere packing problem in dimension 8," arXiv:1603.04246, Ann. Math. (2017) | FETCHED (ar5iv, one structured pass) | Theorem 2 (the LP criterion with signs), the magic-function construction ($E_2, E_4, E_6$ quasimodular + $M_2(\Gamma(2))$ halves, Laplace transforms), the forced double zeros at $\sqrt{2n}$, the $\tau \mapsto -1/\tau$ eigenfunction mechanism, integer $q$-support |
| Cohn-Kumar-Miller-Radchenko-Viazovska, "The sphere packing problem in dimension 24," arXiv:1603.06518, Ann. Math. (2017) | FETCHED (abstract) | Leech optimality + uniqueness among periodic packings; same method |
| CKMRV, "Universal optimality of the E8 and Leech lattices and interpolation formulas," arXiv:1902.05438 | FETCHED (abstract only; ar5iv fetch exceeded size limits) | Universal optimality for completely monotone potentials of squared distance; interpolation from $f, f', \hat f, \hat f'$ at radii $\sqrt{2n}$; "integral transforms of quasimodular forms" |
| Radchenko-Viazovska, "Fourier interpolation on the real line," arXiv:1701.00265, Publ. IHES (2018) | FETCHED (ar5iv, two passes incl. one targeted at Theorem 2) | Theorem 1 (interpolation at $\{\pm\sqrt n\}$), Theorem 2 (image $=\ker L$, ONE relation), Theorem 3 (weight-$3/2$ $\Gamma_\theta$ generating identity) |
| Bondarenko-Radchenko-Seip, "Fourier interpolation with zeros of zeta and L-functions," arXiv:2005.02996 | FETCHED (ar5iv, one structured pass; upgrades the SECONDARY tier it held in [`kns_log_growth_pin.md`](kns_log_growth_pin.md)) | Theorem 1.1: nodes $\{\log n/(4\pi)\}$ paired with the zeta zero multiset; unconditional per this fetch; exact criticality; Riemann-Weil recovered as a consequence |
| Ramos-Sousa, "Perturbed interpolation formulae and applications," arXiv:2005.10337, Anal. PDE (2023) | FETCHED (abstract) | Perturbations of the RV and CKMRV formulas by functional-analytic (Kadec-type) methods, not by new modular identities |
| Ramos-Sousa, "Fourier uniqueness pairs of powers of integers," arXiv:1910.04276 | FETCHED (abstract) | Uniqueness (no formula) at power nodes $\{\pm n^\alpha\}, \{\pm n^\beta\}$ under unspecified-in-abstract $(\alpha,\beta)$ conditions |
| Radchenko-Stoller, "Fourier non-uniqueness sets from totally real number fields," arXiv:2108.11828 | FETCHED (abstract) | The mechanism's arithmetic boundary: extends to number-field lattices (Hilbert-modular-type input), with both existence AND failure of formulas decided by arithmetic structure, not density |
| Cohn-Triantafillou, "Dual linear programming bounds for sphere packing via modular forms," arXiv:1909.04772, Math. Comp. (2021) | SECONDARY (search-result summaries, two independent hits) | LP bound "nowhere near" the best packings in dims 12, 16, 20, 28, 32; dual certificates themselves built from modular forms |
| de Courcy-Ireland-Dostert-Viazovska, "Six-dimensional sphere packing and linear programming," arXiv:2211.09044 | SECONDARY (search-result summaries) | LP bound proven NOT sharp in dim 6 (dual modular-form certificate vs the Cohn-de Laat-Salmon SDP bound) |
| Kulikov-Nazarov-Sodin, arXiv:2306.14013 | REPO ([`kns_log_growth_pin.md`](kns_log_growth_pin.md), FETCHED there) | The density-only frame counterpoint |

Not read this session (named in Honest limits): CKMRV 1902.05438 full text, Stoller
arXiv:2002.11627 (interpolation from spheres), Cohn's ICM laudatio arXiv:2207.06913, the
2026 dim-36 dual bound arXiv:2607.11319, arXiv:2503.15733 (regularity of interpolation
bases).

## 2. What each pillar contributes structurally

**Cohn-Elkies (math/0110009), as restated in Viazovska 1603.04246 Theorem 2.** If
$f:\mathbb R^d \to \mathbb R$ is admissible, not identically zero, with $f(x) \le 0$ for
$\|x\| \ge r$ and $\hat f \ge 0$ everywhere, then every sphere packing has density
$\le \frac{f(0)}{\hat f(0)}\,\mathrm{Vol}\,B_d(0, r/2)$. Proof shape: Poisson summation over
the packing lattice; the two sign cones squeeze $\sum_{\ell} f(\ell)$ between $f(0)$ and
$\hat f(0)\cdot(\text{density factor})$. This is a genuine one-sided band-limited extremal
problem: structurally the Beurling-Selberg/majorant shape, but with the inequality run
against a LATTICE sum instead of a sieve axiom.

**Viazovska (1603.04246).** The sharp $d=8$ function: built as Laplace transforms of
modular objects, the $+1$ Fourier eigenfunction from quasimodular combinations of
$E_2, E_4, E_6$ (her $\varphi_0, \varphi_{-2}, \varphi_{-4}$), the $-1$ eigenfunction from
$M_2(\Gamma(2))$ theta-quotients. The eigenfunction property is the modular inversion
$\tau \mapsto -1/\tau$ pushed through the Gaussian kernel $e^{i\pi\|x\|^2\tau}$ (fetched:
identity (29) plus contour rotation $w = -1/z$ proves $\hat a = a$): i.e. theta
inversion/Poisson IS the Fourier-eigenfunction engine, the same engine e1m verified as T1
(LEARNINGS #160). Sharpness forces $g(\ell) = \hat g(\ell) = 0$ at every nonzero
$\ell \in \Lambda_8$ (lengths $\sqrt{2n}$), with double zeros; these infinitely many
conditions are paid by the integer support of the $q$-expansions (fetched: the relevant
expansion "starts at $q^1$, rational coefficients"), i.e. by the additive lattice in the
exponent, not condition-by-condition.

**CKMRV dim 24 (1603.06518).** Same mechanism at the Leech lattice; uniqueness among
periodic packings. Confirms the mechanism is not a dim-8 accident but is exceptional-lattice
indexed.

**Radchenko-Viazovska (1701.00265).** Theorem 1: every even Schwartz $f$ satisfies
$f(x) = \sum_{n\ge0} a_n(x) f(\sqrt n) + \sum_{n\ge0} \tilde a_n(x) \hat f(\sqrt n)$.
Theorem 2 (the load-bearing structural fact): the map
$\Psi(f) = (f(\sqrt n))_n \oplus (\hat f(\sqrt n))_n$ is an isomorphism onto
$\ker L \subset \mathfrak s \oplus \mathfrak s$ (rapidly decaying sequences), where
$L((x_n),(y_n)) = \sum_{n\in\mathbb Z} x_{n^2} - \sum_{n\in\mathbb Z} y_{n^2}$: the
perfect-square-index samples are $f$ at the integers, so **the unique linear relation on the
interpolation data is the classical Poisson summation formula
$\sum_{n\in\mathbb Z} f(n) = \sum_{n\in\mathbb Z} \hat f(n)$, and there are no others**
(fidelity note: subscript $x_{n^2}$ vs $x_n^2$ read from the render across two passes; the
targeted pass confirmed the perfect-square-index / deformation-of-Poisson reading). Theorem
3: the basis is generated by weight-$3/2$ weakly holomorphic modular forms for
$\Gamma_\theta$, via $\sum_{n\ge0} g_n^+(z) e^{i\pi n\tau} = $ (an explicit
$\theta, \lambda, J$ kernel), and $b_m^\varepsilon(x) = \frac12\int_{-1}^1 g_m^\varepsilon(z)
e^{i\pi x^2 z}\,dz$ with $\hat b_m^\varepsilon = \varepsilon\, b_m^\varepsilon$. The nodes
$\sqrt n$ appear because $e^{i\pi x^2 z}$ evaluated at $x = \sqrt n$ is $q^{n/2}$: **the node
set is the preimage of the integer $q$-exponent lattice under the squared-radius character.**

**CKMRV universal optimality (1902.05438, abstract only).** E8 and Leech minimize energy for
every completely monotone potential of squared distance; the engine is an interpolation
theorem reconstructing radial Schwartz functions from $f, f', \hat f, \hat f'$ at radii
$\sqrt{2n}$, from integral transforms of quasimodular forms. This is family-uniformity over
the POTENTIAL, at one fixed node geometry, in two fixed dimensions.

**Bondarenko-Radchenko-Seip (2005.02996).** The corpus's own log-node object. Theorem 1.1
builds an interpolation basis for even functions in a strip: Fourier-side nodes
$\{\log n/(4\pi)\}_{n\ge1}$ (ALL integers $n$, not primes), function-side nodes
$(\rho - 1/2)/i$ over the nontrivial zeta zero multiset (multiplicities handled; the fetched
text presents the theorem as unconditional in its space $\mathcal H_1$, see discrepancy log).
Mechanism: a Dirichlet-series kernel $D(w,s)$ with the zeta functional equation
($H(1-w,s) = -H(w,s)$ for $H = (\zeta(s)/\zeta(w))D$), Mellin transforms of
$\Gamma_\theta$ modular integrals, contour integration. Two fetched structural facts:
(i) **exact criticality**: "the formula breaks down if one removes any single point" from
either node set; (ii) **Riemann-Weil is recovered as a consequence** when the $\log n$ side
is contracted against von Mangoldt weights: the explicit formula is the shadow of this basis
on the prime-power sublattice. [Retagged FETCHED-PLUS-GLOSS, ADVERSARY 2026-08-09
([`_modular_rung_adversary.md`](_modular_rung_adversary.md) B1): the paper's own wording is
"we may think of (1.1) as arising from (1.2)" via functional representation, framed as
complementary multiplicative and additive duality relations; the von-Mangoldt-contraction
mechanism is this repo's interpretive gloss, not the paper's sentence. Section 5's pricing
logic is unaffected, needing only that the RW pairing and the BRS basis live on the same
node duality, which is confirmed.]

**The boundary literature.** Ramos-Sousa 2005.10337: the RV/CKMRV formulas survive small node
perturbations, but by operator inversion anchored on the unperturbed modular identity (a
functional-analytic correction, not an autonomous identity for the perturbed set).
Ramos-Sousa 1910.04276: power nodes $n^\alpha$ give uniqueness only (no formula), by
uncertainty/density arguments. Radchenko-Stoller 2108.11828: the modular mechanism extends
to totally real number fields (component-wise square roots of inverse-different lattices,
Poincare series for Hecke groups), and DECIDES both existence and failure of formulas by
arithmetic structure; density does not decide. Cohn-Triantafillou 1909.04772 and
de Courcy-Ireland-Dostert-Viazovska 2211.09044: the LP bound is provably not sharp in dim 6
and nowhere near sharp in 12, 16, 20, 28, 32, with the dual (impossibility) certificates
themselves built from modular forms.

## 3. The Q4 scorecard

Format per [`theta_s4_build_spec.md`](../theta_s4_build_spec.md) Section 1 (the four-condition
form of [`s4_carrier_audit.md`](../s4_carrier_audit.md) Section 4 item 5). The 17-constraint
Arch-2 framework is not applicable to this sweep (this is a mechanism-class sweep against the
S4/Q4 spec, not a Spec(Z)-cohomology candidate); the Q4 conditions are the operative
scorecard.

### (1) ONE-SIDEDNESS: FITS

The LP corpus is genuinely one-sided, and the sign conditions enter exactly where the S4
spec wants them: a pointwise cone constraint on the function beyond a radius
($f(x) \le 0$ for $\|x\| \ge r$) and a positivity cone on the transform side
($\hat f \ge 0$), squeezed against a lattice summation identity (Poisson), with sharpness =
simultaneous saturation of both cones on the lattice's distance spectrum. This is the only
known setting where that majorant-shaped pairing was closed SHARPLY rather than walling at a
factor-2/parity ceiling ([`s4_carrier_audit.md`](../s4_carrier_audit.md) Sections 2.3-2.4):
the decisive difference from the sieve embedding is that the inequality is run against the
lattice identity directly, with no axiom-relative intermediary.

### (2) CHEAP MULTIPLICITY: FITS as mechanism class at native nodes; MISFIT at $\{k\log p\}$, with the misfit mechanism NAMED

**What the modular identity actually consumes: neither the specific node set nor bare
summation structure, but the integer support of the exponent lattice.** The nodes
$\{\sqrt n\}$ / $\{\sqrt{2n}\}$ are not an input; they are the OUTPUT of pairing the
squared-radius character $e^{i\pi x^2 z}$ with $q$-expansions supported on
$\mathbb Z_{\ge0}$. The translation generator of $\Gamma_\theta$ ($\tau \mapsto \tau + 2$)
forces integer exponent support; the inversion generator ($\tau \mapsto -1/\tau$) is the
FE/Poisson engine. The cheapness itself is sourced by RIGIDITY: spaces of (weakly
holomorphic) modular forms with bounded pole order are finite-dimensional, so infinitely
many vanishing/coefficient conditions are enforced wholesale by an $O(1)$-dimensional
family. In S4 language: total order $M = \infty$ of vanishing conditions at the node set,
dimension cost $O(1)$, well-conditioned, sourced by an identity that fails for perturbed
nodes. **This is the banked S4 economy, realized.** It is the first known instance outside
commensurate AP combs (e1o's $\mathbb F_q$ avatar), which answers
[`s4_carrier_audit.md`](../s4_carrier_audit.md) Section 2.5's "no published relative": a
relative exists, at quadratic nodes.

**Is there any interpolation or LP-sharpness result at nodes neither AP nor
$\sqrt n$-type?** At search depth, exactly three families, each classified: (i) density-only
nodes (KNS 2306.14013; Ramos-Sousa 1910.04276 power nodes): frames/uniqueness with slack,
no exact identity, no collapse, pre-killed by the DMV screen
([`kns_log_growth_pin.md`](kns_log_growth_pin.md)); (ii) perturbed-$\sqrt n$ nodes
(Ramos-Sousa 2005.10337): exact formulas exist but are functional-analytic corrections
anchored on the modular identity, still asymptotically quadratic nodes; (iii) **log nodes
(BRS 2005.02996): the one exact, critical, FE-sourced identity at $\{\log n/(4\pi)\}$, and
its dual node set is the zeta zero multiset.** No known exact identity exists at any node
set that is not (a) an exponent-lattice preimage under a power character (integer or
number-field), (b) a perturbation thereof, or (c) log-type with the zero set dual. The
misfit at $\{k\log p\}$ is therefore nameable: **at log nodes the role of the Gaussian
character is played by $n^{-s}$, the role of modular inversion by the zeta FE $s \mapsto
1-s$, and the resulting identity's dual vanishing locus is the zero set itself.** Using it
is K1-circular; proving one-sidedness against it is M4. The transfer reproduces the wall
exactly (Section 5).

### (3) LAMBDA-UNIFORMITY: split verdict; the informative half is negative

On its native nodes the mechanism is horizon-free: one identity covers the entire infinite
node set at once with controlled basis growth, which is stronger than lambda-uniformity.
Across the transfer parameter (which node geometry / which dimension), the constructions
are rigidly single-shot: sharp in dims 8 and 24 only, PROVEN not sharp in dim 6
(2211.09044) and nowhere near in 12, 16, 20, 28, 32 (1909.04772), with dim 2 open
(math/0110009's own conjecture list is 8 and 24; sharpness elsewhere is not conjectured).
Universal optimality (1902.05438) is uniformity over potentials, not over node geometries.
The mechanism exists exactly where an exceptional lattice does; there is no family knob.
For S4 this means: a transferred device would have to be re-sourced at the log-node
geometry from scratch; nothing in the corpus supplies a deformation path.

### (4) LATTICE CLAUSE: FITS, rigidly

The lattice enters at three named sites: (i) the $\pm1$ eigenfunction property = theta
inversion = Poisson over $\mathbb Z$ (e1m's T1 engine, verbatim); (ii) the vanishing
locations = integer $q$-exponent support (the translation generator); (iii) the sign
control on $\hat f$ = nonnegative $q$-coefficients of the constructed forms. **Beurling
screen:** the mechanism cannot be built on a density-matched fake node set, with the failing
clause nameable at the construction step: a "modular form" whose exponents are Beurling
generalized integers has no group ($\tau \mapsto \tau+2$ presupposes $\mathbb Z$-support;
no discrete group, no finite-dimensionality, no rigidity, no wholesale vanishing). This is
the same failure e1m measured as T5's $0.37$ theta-FE defect and e1q reproduced at $0.368$
(LEARNINGS #160, #167). Radchenko-Stoller 2108.11828 confirms the boundary from the
positive side: the mechanism extends exactly as far as arithmetic (number-field lattices)
and not one step into bare density; and even some arithmetic sets provably fail, so density
never decides. **DMV screen:** passes; no load-bearing part of the magic-function mechanism
consumes only density. (The parts of the wider literature that ARE density-only, KNS and
the power-node uniqueness results, carry no S4 content and are already pre-killed, per
[`kns_log_growth_pin.md`](kns_log_growth_pin.md).) **D-H screen:** the mechanism is
unposable on Davenport-Heilbronn for the same two reasons as e1q's kernel
([`theta_s4_build_spec.md`](../theta_s4_build_spec.md) Section (c)): no Euler product means
no privileged prime-power locus for a log-node transfer, and the conductor-1 theta
inversion is the wrong FE type; additionally the BRS construction consumes
$\zeta(s)/\zeta(w)$ (Dirichlet series with FE AND product structure in its intended
contraction), which D-H lacks.

## 4. Frame vs collapse: the typed answer

The discriminator from [`kns_log_growth_pin.md`](kns_log_growth_pin.md) Section 5 (frame =
evaluation map bounded below = full price; collapse = rank-deficient evaluation = cheap
multiplicity) applied to this corpus gives a sharper picture than either label: **the corpus
contains both organs, cleanly separated.**

- **The interpolation organ (RV Theorems 1-2, CKMRV interpolation, BRS) is EXACTLY
  CRITICAL.** The data is free modulo exactly ONE linear relation (classical Poisson
  summation, RV Theorem 2; for BRS, the explicit-formula pairing plays the analogous role),
  one basis function per node, and removal of any single node destroys the formula (BRS,
  fetched; for RV the same is implied by Theorem 2's isomorphism onto a codimension-1
  kernel). This is NOT a KNS frame: arXiv:2512.18677 (REPO tier, via
  [`kns_log_growth_pin.md`](kns_log_growth_pin.md) Section 6) shows the RV basis fails to be
  a Riesz basis in KNS's own space, and the node density $\sqrt n$ sits exactly at KNS's
  critical exponent $\alpha = 1/2 = 1/p_0$ for the self-dual case, the boundary KNS's
  strict-inequality dichotomy cannot reach. **What modularity buys over density is exactly
  the critical case**: density-only methods give frames with slack; the modular identity
  closes the boundary with zero oversampling. But in S4's accounting, an exactly-critical
  basis is still FULL PRICE: one function per condition, $M$ conditions cost $M$
  dimensions. The interpolation organ, as such, has no $o(M)$ content.
- **The collapse organ is the magic function.** The S4 economy (M conditions at $o(M)$,
  indeed $O(1)$, cost) lives in the LP-sharpness half: the existence of a nonzero one-sided
  function with prescribed double zeros along the entire lattice distance spectrum, inside
  an $O(1)$-dimensional modular family. In evaluation-matrix language: restricted to the
  modular-sourced subspace, the vanishing conditions at $\{\sqrt{2n}\}$ are rank-collapsed
  to $O(1)$; the rigidity of modular forms is the collapse mechanism.

**Answer to the pre-registered question:** RV interpolation per se is neither the KNS
structural opposite nor the S4 collapse; it is the critical boundary between them, and its
sharp node economy is a criticality statement, not a rank deficiency. The rank-collapse-like
economy S4 wants is real in this corpus but lives one theorem over, in the magic-function
existence, and THAT is the object whose log-node analogue must be priced (Section 5).

## 5. The transfer, priced

Transplant the mechanism to the S4 setting ($\{k\log p\}$, one-sided device, dim budget
$\le 4\lambda^2$):

1. The exponent-lattice character at log nodes is $e^{-s\log n} = n^{-s}$; the generating
   object is a Dirichlet series; the inversion is the zeta FE. The corpus's own realization
   is BRS 2005.02996, and it is forced to pair $\{\log n/(4\pi)\}$ with the zeta zero
   multiset as dual nodes. This is not an accident of their method: the FE's "dual lattice"
   to the $\log n$ comb IS the zero set (the explicit formula's two sides), exactly as
   $\Lambda_8$'s dual vanishing locus is $\Lambda_8$.
2. Therefore the transferred magic-function question reads: build, at $O(1)$ modular-type
   cost from the FE alone, a ONE-SIDED function with prescribed vanishing at the log comb,
   without evaluating the dual (zero-side) conditions. But one-sidedness against the
   explicit-formula pairing with the zero side left symbolic is verbatim the Weil-positivity
   / Landau-threshold statement: M4, the repo's known wall
   ([`landau_one_sided.md`](../landau_one_sided.md); [`all_roads_to_the_signature.md`](../all_roads_to_the_signature.md)).
   Evaluating the zero side instead is a K1 violation.
3. The node-set granularity confirms the pricing: BRS needs ALL of $\{\log n\}$, and the
   prime-power sublattice $\{k\log p\}$ with von Mangoldt weights appears exactly when the
   Euler product is contracted in, recovering Riemann-Weil (fetched, Section 2). So the
   restriction from $\log n$ to $k\log p$ costs precisely the Euler product, and the
   one-sided use of the result costs precisely M4: **the two payments of the trojan-horse
   conservation law ([`trojan_horse_m4.md`](../trojan_horse_m4.md)), made separately
   visible by this corpus.**

Net: the Viazovska mechanism class does transfer structurally, and the transferred object
already exists in the literature (BRS); what it produces at log nodes is the explicit
formula in interpolation costume, exactly critical, with the S4-relevant one-sided/collapse
question mapping onto M4 unchanged. The corpus bypasses nothing; it independently
re-derives the wall from the sharpest known positive instance of the S4 economy. As a
coordinate: this is the strongest external validation yet that the banked S4 spec is the
right shape (its mechanism class is non-empty in nature), and simultaneously a proof that
filling it at $\{k\log p\}$ by THIS route is not a detour around M4 but a restatement of it.

## 6. Discrepancy log

1. **BRS conditionality.** [`kns_log_growth_pin.md`](kns_log_growth_pin.md) Section 1.3
   (quoting KNS's related-work section) describes the BRS formula as "assuming the Riemann
   hypothesis and simplicity of zeroes." This session's direct fetch of 2005.02996 presents
   Theorem 1.1 as unconditional, with zero multiplicities $m(\rho)$ handled explicitly.
   Plausible reconciliation (NOT adjudicated here): KNS described a cleaner conditional
   variant while the paper's main theorem is the unconditional multiset form. Flagged for
   ADVERSARY/VERIFIER; a full-text read of BRS Section 1 settles it.
2. **The "modular forms ARE the tie" reading in LEARNINGS #167.** #167 motivates this sweep
   with "the additive lattice BOUND TO the multiplicative structure ... is what modular
   forms ARE (Hecke operators on q-expansions with a functional equation)." The fetched
   record shows the sphere-packing magic functions consume NO Hecke/multiplicative
   structure: $\Gamma_\theta$/$\Gamma(2)$/quasimodular $SL_2(\mathbb Z)$ input only
   (additive lattice + inversion). The multiplicative layer enters this corpus exactly once,
   in BRS's $\zeta(s)/\zeta(w)$ kernel, and its price is the zero-set dual. The #167 hope,
   read strictly, is therefore not falsified but relocated: the lattice-times-multiplicative
   binding is not a free property of modularity; in this corpus it is purchased only at the
   explicit-formula joint. Reported, not resolved.
3. **The frame audit's mechanism-class identification
   ([`ccm_corridor_frame_audit.md`](../ccm_corridor_frame_audit.md) Section 2).** Confirmed
   with one refinement: "Radchenko-Viazovska Fourier interpolation at $\sqrt n$ nodes" is
   the critical-basis organ (full price, no collapse); the S4-mechanism-class member is the
   magic-function/LP-sharpness organ. The audit's sentence conflated the two halves;
   harmless for its purpose (naming the unswept field) but load-bearing for any BUILDER
   follow-up.

## 7. Verdict

**FITS-IN-PART.** Conditions (1) and (4): FITS, fully and exactly (the corpus is the only
known sharp closure of a one-sided band-limited extremal problem, and its identity is
rigidly lattice-consuming with the Beurling failure nameable at the construction step).
Condition (3): split (horizon-free on native nodes; provably single-shot across geometries).
**Blocking condition: (2) at $\{k\log p\}$**: the cheap-multiplicity economy is real and
instantiated (magic function, $O(1)$ cost for infinitely many conditions) but is sourced by
exponent-lattice integrality, and its unique log-node realization (BRS) forces the zeta
zero multiset onto the dual side, mapping the S4 question onto M4 verbatim. Not a MISFIT of
the mechanism class (the class fits; that is the sweep's positive finding); a MISFIT of the
transfer, with the disqualifier named: **at log nodes, this mechanism class IS the explicit
formula, and its one-sided version IS the M4 positivity.**

## Honest limits

- CKMRV 1902.05438 was read at abstract level only (the ar5iv render exceeded fetch
  limits); the statement that Poisson summation over E8/Leech furnishes the ONLY relations
  on its derivative-interpolation data is plausible by analogy with RV Theorem 2 but was
  NOT verified at source this session and is deliberately not asserted above. UNSOURCED if
  quoted.
- Ramos-Sousa 2005.10337's quantitative perturbation threshold (the Kadec-type smallness
  condition on node perturbations) was not pinned; only the method class (operator
  inversion anchored on the modular identity) is asserted.
- Ramos-Sousa 1910.04276's exact $(\alpha,\beta)$ uniqueness region was not pinned.
- Cohn-Triantafillou 1909.04772 and de Courcy-Ireland-Dostert-Viazovska 2211.09044 are
  SECONDARY (consistent search-result summaries, two independent hits each), not fetched at
  source.
- All full-text extractions are LLM summarizations of ar5iv renders; the RV Theorem 2
  subscript reading ($x_{n^2}$, perfect-square indices) was cross-checked by a targeted
  second pass but not read character-by-character.
- Not read at all: Stoller 2002.11627, Cohn 2207.06913, arXiv:2607.11319, arXiv:2503.15733,
  and the entire Fourier-interpolation-on-lattice-cross / Heisenberg-uniqueness-pair
  literature (a known adjacent family, left out of scope as density/PDE-sourced rather than
  modular-identity-sourced; unverified classification).

## What this enables / handed forward

- **For SYNTHESIZER:** the banked S4 spec gains its first external instance (the mechanism
  class is non-empty: quadratic nodes, magic functions), and the sweep closes the last
  named unswept corner of [`ccm_corridor_frame_audit.md`](../ccm_corridor_frame_audit.md)
  Section 2's absence-vocabulary catch. The spec's realization at $\{k\log p\}$ is now
  triangulated to be M4-equivalent from a third independent side (after the majorant
  closure and the density/frame closure): rigidity-sourced collapse exists in nature, and
  its log-node price is the explicit formula's positivity.
- **For ADVERSARY:** discrepancy-log items 1 and 2 are decision-ready; item 1 is a one-fetch
  check.
- **For BUILDER, the sharpest handed-forward question:** the corpus locates the S4 economy's
  source in FINITE-DIMENSIONALITY (rigidity) of the identity's coefficient space. The
  log-node analogue of "weakly holomorphic modular forms of bounded pole order" would be a
  space of FE-symmetric Dirichlet-type objects with controlled polar data, finite-dimensional
  WITHOUT zero-location input. Does any such rigidity theorem exist, or is
  finite-dimensionality there itself zero-location-equivalent? Concretely executable rung:
  pose e1o's rank/cost-ratio instrument on the BRS skeleton at finite horizon (nodes
  $\{\log n/(4\pi)\}_{n \le N}$ and the prime sublattice, the zero side carried symbolically,
  K1-guarded, Beurling twin = no FE), and measure whether the FE buys ANY conditioned
  economy at $\{k\log p\}$ beyond the all-$n$ baseline; pre-registered wall: the economy
  prices as the explicit formula's zero side, i.e. M4, which would make the third coordinate
  system's wall (LEARNINGS #171's chain) and this corpus's wall provably the same joint.

## Adversary note (2026-08-09)

Full report: [`_modular_rung_adversary.md`](_modular_rung_adversary.md). Verdict
**PASS_WITH_FIXES**. Findings:

1. **Discrepancy-log item 1 ADJUDICATED IN THIS DOSSIER'S FAVOR.** Direct source fetch of
   arXiv:2005.02996: Theorem 1.1 is unconditional, multiplicities $m(\rho)$ handled by
   derivative terms $\sum_{j=0}^{m(\rho)-1} f^{(j)}((\rho-1/2)/i)V_{\rho,j}$; the
   exact-criticality sentence ("break down if one removes any single point") is verbatim.
   The "assuming RH + simplicity" wording in [`kns_log_growth_pin.md`](kns_log_growth_pin.md)
   Section 1.3 is KNS's citing description, not BRS's theorem; annotation belongs there.
2. **Two further citations verified at source.** RV 1701.00265 Theorem 2 ($\ker L$,
   perfect-square indices $x_{n^2}$, unique relation = classical Poisson summation) and
   2211.09044 (LP bound "not sharp in dimension 6," dual modular-form certificate,
   de Courcy-Ireland-Dostert-Viazovska) both confirmed verbatim; the latter can be upgraded
   from SECONDARY to FETCHED-abstract.
3. **One fidelity fix.** Section 2's "Riemann-Weil is recovered as a consequence when the
   $\log n$ side is contracted against von Mangoldt weights" overstates the fetch: the
   paper's wording is "we may think of (1.1) as arising from (1.2)" (LHS of (1.1) = a
   linear functional on $\mathcal H_1$, RHS = its representation in the Theorem 1.1 basis),
   framed as complementary duality relations. The von-Mangoldt-contraction mechanism is
   this dossier's interpretive gloss and should be tagged as such. Section 5's pricing
   logic is unaffected.
4. **Verdict calibration (B2).** Strictly at the spec's own node set $\{k\log p\}$, no Q4
   condition is met (conditions (1)/(4) fit at NATIVE quadratic nodes). Read FITS-IN-PART
   as "FITS as mechanism class at native nodes / M4-EQUIVALENT as a transfer": an existence
   proof for the S4 economy, not a candidate route around M4. The dossier's own Sections
   5 and 7 already say this; the annotation guards against verdict-vocabulary drift.
5. **DMV and Beurling screens confirmed applied with mechanisms** (density-only parts
   partitioned out and pre-killed; the Beurling failure named at the construction step with
   e1m/e1q quantitative anchors), not merely cited.

Addendum (salvaged from PR #7, 2026-08-26; LEARNINGS #210): two further non-uniformity
citations for the family-parameter verdict: Mallows-Odlyzko-Sloane, J. Algebra 36 (1975)
68-76 (the prescribed-vanishing extremal modular form develops a negative coefficient at
large weight) and Zhou, arXiv:2604.10914 ($\dim S_{d/2}(\mathrm{SL}_2(\mathbb{Z})) \le 1$
rules out LP sharpness for all $d \ge 48$).
