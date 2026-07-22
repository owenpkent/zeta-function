# The compactness trojan: compact/closed positivity classes + moment determinacy vs the M4 uniform limit

> SURVEYOR dossier, 2026-07-22. Task: map every candidate compact or closed positivity class that
> could let the project trade M4's uniform determinant-class limit (where uniform convergence must be
> PROVEN) for three links: (i) certification of the finite-cutoff objects into a positivity class that
> is CLOSED and COMPACT after normalization, so subsequential limits exist for free; (ii) a determinacy
> statement (moment determinacy: Carleman or Krein growth conditions, not positivity) forcing all
> subsequential limits to coincide; (iii) identification of the unique limit as $\Xi$ via the corrected
> Hamburger pin (already reformulated positivity-free in-repo, LEARNINGS #160 / e1m).
>
> Internal state read first: [`ccm_semilocal_prolate.md`](../ccm_semilocal_prolate.md) (with the
> 2026-07-11 and 2026-07-12 addenda), [`landau_one_sided.md`](../landau_one_sided.md),
> [`la_negative_square_check.md`](la_negative_square_check.md) (the #168 HB$_1$ question),
> [`../../../experiments/spectral/e1m_hamburger_pin.md`](../../../experiments/spectral/e1m_hamburger_pin.md).
>
> Method discipline (LEARNINGS #157 process flag): every load-bearing citation is tagged
> **[FETCH-VERIFIED]** (fetched and read at source this session: arXiv abstract page, ar5iv/native
> HTML full text, or an in-repo note whose own fetch discipline is documented) or **[SECONDARY]**
> (search-snippet, textbook-classical, or converged-but-unpinned). No tag is promoted. Discrepancies
> with prior repo readings are logged in Section 6, not silently resolved. This is a SURVEYOR
> document: it maps and prices; it builds nothing. No em dashes.
>
> ADVERSARY citation-verification pass 2026-07-22: every load-bearing tag re-fetched at source,
> the two incomplete scans completed (2511.23257 full text via PDF extraction; Killip-Simon at
> theorem level), the GORZ discrepancy resolved, and the Section-5 clause-(b) risk adjudicated.
> Working report: [`_compact_class_survey_adversary.md`](_compact_class_survey_adversary.md).

## 0. The framing, and one structural constraint that governs every class

**The wall being traded against.** The CCM Section-7 statement is: the finite-cutoff determinants
$\hat\xi_\lambda$ (real-rooted unconditionally, Thm 5.10(iii) of the D$_{\log}$ family, re-verified
at source this round: "all its zeros are on the real line and coincide with the spectrum of
$D_{\log}^{(\lambda,N)}$", 2511.22755) converge to $\Xi$ uniformly on compacts (CCM's own statement
is the stronger closed-substrip form: "converge uniformly on closed substrips of the open strip
$\Im(z) < 1/2$"; discrepancy 6), whence RH by Hurwitz. The authors' own frame is exactly this, with no
alternative: "This convergence would entail RH using Hurwitz theorem on the zeros of limits of
holomorphic functions," and "Justifying rigorously this step is the main remaining obstacle to our
approach to RH" [FETCH-VERIFIED, arXiv:2511.22755, Section 7; see Section 3.1 below for the exact
attachment point of that quote]. The repo has priced this limit as M4 (uniform ground-state /
det-class control, RH-equivalent positivity with a rate; LEARNINGS #154).

**The trojan.** Uniform convergence is expensive because it is a two-sided, quantitative,
family-uniform statement. The proposed trade: pay instead for (i) class-membership of the finite
objects (often FREE: finite-cutoff reality is unconditional), let a compactness theorem supply
subsequential limits, (ii) let a determinacy theorem (growth conditions, not positivity) force all
subsequential limits to coincide, and (iii) pin the unique limit as $c\,\Xi$ by the corrected
Hamburger pin (#160), whose engine is the lattice (Poisson/theta), not positivity.

**The tariff question, per class.** Where does the RH content relocate, and does the certification /
glue consume the Euler product (nonnegative comb) or the additive lattice (theta FE / Poisson), or
only density data? If a leg consumes only density data it is DMV-screened: the Beurling control
(`experiments/_shared/beurling.py`) shows everything provable from density/counting data alone is
FE- and lattice-agnostic, so a density-only leg can carry no discrimination. (A density-only leg is
still permitted where it carries no discrimination weight, e.g. as pure uniqueness glue; the screen
kills classes whose DISCRIMINATING leg is density-only.)

**The constraint that governs everything: type divergence.** The finite objects have exponential
type $\approx \log\lambda$ (measured $0.93$-$0.98 \times \log\lambda$ across builds, e1m T3), and
the types DIVERGE. The limit $\Xi$ is not of exponential type at all: it is order 1 of maximal
type ($\log|\Xi|$ grows like $|z|\log|z|$, equivalently the zero density $\sim \log T$ grows without
bound, while an exponential-type function has bounded zero density on $\mathbb{R}$)
[SECONDARY-CLASSICAL, Titchmarsh Ch. X / Boas]. Consequences, before any class is examined:

1. **No fixed-type ball works.** Any class whose compactness theorem fixes an exponential-type bound
   excludes the family cofinally AND excludes the limit. Every candidate must absorb the diverging
   type through a normalization (projectivization, trace-norming, rescaling, parameter
   normalization), and **the normalization is where the tariff hides**: it either discards the
   diverging data (and with it, typically, the arithmetic) or converts the divergence into a
   mass/length coordinate that can escape in the limit (and "no escape" is a uniform statement
   again).
2. **The e1m growth-face finding is the local form of this.** e1m already recorded that the limit's
   growth/entirety package "belongs to the open package too" precisely because the finite types
   diverge. The trojan does not evade this; each class below is scored on how its normalization
   handles it.

The six classes surveyed: (1) Polya frequency sequences / Edrei-Thoma; (2) Laguerre-Polya;
(3) Hermite-Biehler, de Branges chains, canonical systems, Krein strings; (4) determinate moment
problems as glue; (5) Lorentzian polynomials; (6) normal families of bounded type.

---

## 1. The per-class map

### 1.1 Polya frequency sequences and Edrei-Thoma

**The class and its theorems.** A one-sided sequence $(a_n)$ is totally positive (a Polya frequency
sequence) iff its generating function has the AESW form. Statement fetched at source
[FETCH-VERIFIED, arXiv:2512.06468, "Theorem ASWE", quoting]: "A function $f$ belongs to
$\widetilde{TP}_\infty$ if and only if $f(z) = C z^q e^{\gamma z} \prod_{k=1}^\infty
(1+\alpha_k z)/(1-\beta_k z)$, where $C \ge 0$, $q \in \mathbb{Z}$, $\gamma \ge 0$, $\alpha_k \ge 0$,
$\beta_k \ge 0$, and $\sum_k (\alpha_k + \beta_k) < \infty$" (refs there: Aissen-Edrei-Schoenberg-
Whitney, J. Anal. Math. 2 (1952) 93-109; Karlin, Total Positivity I, p. 412). Thoma's theorem
classifies the extreme characters of $S(\infty)$ by exactly these parameter pairs with
$\sum_i \alpha_i + \sum_j \beta_j \le 1$, and the Thoma set $\Omega$ **is compact in the product
topology** [FETCH-VERIFIED, Olshanski arXiv:math/0311369, Sections 3.2-3.3: the constraint
inequality and the extreme-character formula $\chi^{(\omega)}(\sigma) = \prod_{k\ge2}
p_k(\alpha,\beta)^{m_k(\sigma)}$ fetched; the compactness sentence "$\Omega$ is a compact space"
fetched, with one fetch-artifact caveat logged in Section 6]. The Edrei-Thoma equivalence (Thoma's
classification = Edrei's solution of Schoenberg's totally-positive-sequence problem) is
[SECONDARY, converged across search sources].

**Is Thoma-simplex compactness usable for entire-function limits of zeta-shaped data?** Structurally
yes, and this is the only class in the survey whose compactness is free in a topology genuinely
weaker than locally uniform convergence. The chart: in the variable $w = z^2$ (using evenness),
$\Xi$ is order $1/2$, genus 0, with Hadamard product $\Xi(0)\prod_k (1 - w/\gamma_k^2)$ and
$\sum_k \gamma_k^{-2} < \infty$ [SECONDARY-CLASSICAL]. Under RH all $\gamma_k^2 > 0$, so the
coefficient sequence of $\prod_k(1 + w/\gamma_k^2)$ is a Polya frequency sequence with
$\beta = 0$, $\gamma$-parameter $0$; conversely AESW forces all zeros of a PF generating function
onto the real axis (in $-w$). So **class membership of the LIMIT is verbatim RH**, exactly as with
Laguerre-Polya below; the trojan's content is whether the finite-to-limit passage can be run on the
parameter simplex instead of on functions. The finite objects certify for free: $\hat\xi_\lambda$ is
real-rooted unconditionally (CF reality, Thm 5.10(iii)), so its $w$-chart parameter list
$\{1/t_k(\lambda)^2\}$ is a legal PF parameter point after normalization.

**Where the compactness actually pays and where it leaks.** Normalize $\alpha_k(\lambda) =
t_k(\lambda)^{-2} / \sum_j t_j(\lambda)^{-2}$; the normalized lists live in the compact simplex, so
subsequential parameter limits exist FOR FREE in product topology, with no type bound and no local
boundedness certificate. The leak is the two escape channels the Thoma normalization itself names:
mass can escape to the exponential parameter $\gamma$ (zeros marching to infinity too fast:
pointwise parameter convergence with $\sum \lim < \lim \sum$), and the normalizing constant
$\sum_j t_j(\lambda)^{-2}$ can drift. "No mass escape" is exactly the statement
$\sum_k t_k(\lambda)^{-2} \to \sum_\rho$ (weighted, over ALL zeros of the limit), i.e. a
**two-sided weighted trace equality**. That is the C1 joint (the two-sided trace formula, the B1
rung wall) in parameter clothing. An off-line zero pair of the true $\Xi$ hides in the limit
precisely as a mass defect: the on-simplex limit point would carry less total mass than the
Hadamard mass of $\Xi$, and nothing in the product topology notices.

**Tariff.** Leg (i) free (CF reality). Leg (ii) cheap on the simplex: the moment coordinates
$p_k(\alpha,\beta)$ ARE the coordinates, so limit uniqueness given convergence of the $p_k$ is
definitional; but convergence of the $p_k(\lambda) = \sum_k t_k(\lambda)^{-2m}$ is a family of
weighted spectral-sum convergences = explicit-formula / trace data = **Euler-consuming (the correct
site)**. Leg (iii) = the Hamburger pin, lattice-consuming, unchanged. The RH content relocates into
**mass conservation** (= C1, the two-sided trace formula), not away from the project's map.
Known certification routes for zeta-shaped data into total-positivity-adjacent conditions consume
the LATTICE: the Turán and higher Turán inequalities for $\Xi$ are proven through the theta kernel
$\Phi$ (Csordas-Norfolk-Varga 1986 and successors) [SECONDARY], and the Jensen-polynomial
certification (Griffin-Ono-Rolen-Zagier) proves hyperbolicity for "a density 1 subset of the Jensen
polynomials of each degree" and "for all $d \le 8$" [FETCH-VERIFIED abstract, arXiv:1902.07321;
Polya 1927 equivalence "RH iff hyperbolicity of Jensen polynomials for $\zeta$ at its point of
symmetry" fetched verbatim; the published PNAS version proves the stronger cofinite form
("hyperbolic for all sufficiently large $n$", each $d$): discrepancy RESOLVED in Section 6]. Note what GORZ certifies: the RH-free corners (large-shift
asymptotic regime, where the limiting objects are Hermite polynomials = the universal/GUE-flavored
regime); the RH-bearing corner (small shift, every degree) is exactly what stays open. That is this
class's honest pattern: certifications exist, consume the right things, and cover everything except
the corner where RH lives.

**Verdict: ADJACENT-WATCH.** The one class with genuinely free compactness in a weaker topology;
the relocation is clean and lands on named repo coordinates (mass conservation = C1; moment
convergence = Euler site; pin = lattice site). Not NEW-LOAD-BEARING because the mass-conservation
clause is M4/C1-shaped and no literature route supplies it (Section 3.5).

### 1.2 Laguerre-Polya

**The class and its closure.** $\mathcal{LP}$ = real entire functions that are locally uniform
limits of real polynomials with only real zeros; equivalently the Hadamard form
$c z^m e^{-az^2+bz}\prod (1 - z/x_j)e^{z/x_j}$, $a \ge 0$, $x_j \in \mathbb{R}$,
$\sum x_j^{-2} < \infty$ [SECONDARY, converged across multiple sources incl. the Polya-Schur 1914
lineage; textbook home Levin, Distribution of Zeros of Entire Functions, Ch. VIII]. The class is
CLOSED under locally uniform limits (limits of $\mathcal{LP}$ are $\mathcal{LP}$ or vanish
identically); this is the Hurwitz/normal-family fact.

**Why this alone is exactly the frame the repo already has.** Plainly: $\mathcal{LP}$-closure under
locally uniform limits is the SAME topology whose convergence is the open problem. CCM's published
architecture already IS this class run in this topology: step (5) of arXiv:2511.23257 is "applying
Hurwitz's theorem on zeros of uniform limits of holomorphic functions" [FETCH-VERIFIED abstract],
and e1k's discipline result (real-zero entire functions cannot converge uniformly to $\Xi_{DH}$
near $\gamma \approx 85.7$; the Hurwitz contrapositive) is the repo's own working form. Membership
of the finite objects is free (CF reality); membership of the limit is RH (Polya); and the class
being closed-but-NOT-compact means subsequential limits are not free: pre-compactness in this
topology is local uniform boundedness (Montel), which for this family is precisely the uniform
control M4 must prove. **Zero gain unless the topology is weakened**, and the two available
weakenings both lose the theorem: pointwise limits of $\mathcal{LP}$ functions need not be entire
(no Hurwitz), and zero-measure (empirical-distribution) limits lose the function entirely (see 1.1
and 4 for what survives that loss: only the mass-conservation question). The de Bruijn-Newman
boundary sharpens the warning: $\Lambda \ge 0$ (Rodgers-Tao) says $\zeta$ sits on the boundary of
the $\mathcal{LP}$-certifiable heat-flow family, with zero margin [SECONDARY].

**Tariff.** Not applicable: the class adds no leg the repo does not already price. The RH content
does not relocate; it stays at uniform convergence.

**Verdict: KNOWN-TO-REPO.** It is the Hurwitz frame verbatim (the repo's #158/#160 wall
vocabulary); named here so nobody re-buys it under the class's name.

### 1.3 Hermite-Biehler, de Branges chains, canonical systems, Krein strings

**The class.** $E \in HB$ iff $|E(z)| > |E^\#(z)|$ on $\mathbb{C}^+$; each $E$ generates a de
Branges space $\mathcal{H}(E)$, and de Branges' ordering theorem organizes the regular subspaces
into a totally ordered CHAIN [SECONDARY-CLASSICAL, de Branges 1968, Thm 35 lineage]. Chains are
equivalent to canonical systems $J u' = -z H u$ with $H(t) \ge 0$ locally integrable (Hamiltonians);
Krein strings are the diagonal sub-case, regular vs singular according to finite vs infinite
length/mass [SECONDARY-CLASSICAL, Kac-Krein; Kasahara 1975 for the continuity of the
string-to-spectral-measure correspondence].

**The compactness theorem, at source.** This class carries the one load-bearing compactness
statement in the survey that is both free and limit-compatible: "The space of trace normed
canonical systems becomes a compact metric space when endowed with a natural metric" and "the
one-to-one correspondence $H \mapsto (m_-, m_+)$ between canonical systems and pairs of generalized
Herglotz functions becomes a homeomorphism if we equip the space of Herglotz functions with the
metric $d(F,G) = \max_{|z-2i|\le 1} \delta(F(z), G(z))$," where "convergence in $d$ is equivalent
to locally uniform convergence with respect to the spherical metric" [FETCH-VERIFIED,
Forester-Remling, "Topological properties of reflectionless canonical systems," arXiv:2409.04862,
quoting, re-verified this round; cited there to Remling, Spectral Theory of Canonical Systems
(de Gruyter 2018): the compactness discussion to Section 5.2, the homeomorphism to Corollary 5.8].

**Adversary re-fetch addendum (2026-07-22), pinning what the theorem needs.** (i) In 2409.04862 the
two sentences are quoted BACKGROUND (that paper's own new compactness results concern the
reflectionless subclasses $\mathcal{R}_0(C)$), so the load rests on Remling's book; an independent
published corroboration exists: Hur, arXiv:1501.01268, proves at source that
$V_+ = \{H : \mathrm{Tr}\,H(x) = 1 \text{ a.e. on } (0,\infty)\}$ "is a compact metric space"
(argument credited to Remling 2007, Section 2) and that the de Branges/Winkler bijection
$H \mapsto m_H$ is a homeomorphism onto $\overline{\mathcal{H}} = \mathcal{H} \cup \mathbb{R} \cup
\{\infty\}$ [FETCH-VERIFIED, full-text passages]. (ii) The exact setup: $H(x) \in
\mathbb{R}^{2\times2}$, $H \ge 0$, entries locally integrable, $\mathrm{Tr}\,H = 1$ a.e.; the
half-line correspondence carries the boundary condition $u_1(0) = 0$, and half-line trace-normed
systems are automatically limit point at $\infty$, so no boundary choice at infinity hides in the
statement. (iii) The homeomorphism's TARGET includes the degenerate elements (real constants and
$\infty$): the compact space genuinely contains degenerate limits, which is exactly where clause
(b) below lives; the compactness costs nothing and excludes nothing. (iv) The finite-cutoff
objects are finite chains; they enter the compact space only after extension to the half-line
(the standard indivisible-interval tail), and that embedding choice is a normalization the
BUILDER rung must fix and report.

**Why this evades the type-divergence constraint.** The normalization is trace-norming, a
REPARAMETRIZATION of the independent variable, not a growth bound: the diverging type of
$\hat\xi_\lambda$ is absorbed into the length coordinate of the Hamiltonian ($\Xi$ itself, order 1
maximal type, corresponds to an infinite/singular chain; finite-cutoff objects to finite chains).
So the whole family AND the limit candidate live in one compact space. Subsequential limits of the
finite chains exist for free, the limit is again a genuine positive Hamiltonian, and its Weyl
function is Herglotz, i.e. **the reality/line structure survives the limit BY CLASS**, with no
uniform certificate. This is the trojan's leg (i) + free-limits step, actually available. The
repo's own e1s finding is the finite germ of the chain structure: $D_{\log}^{(N)}$ is the exact
central block of $D_{\log}^{(N+1)}$ (Cauchy compression interlacing) = the finite chain nesting,
already measured.

**Where the RH content relocates (all of it, into two named clauses).**
1. **Identification**: the subsequential-limit canonical system must be identified as ZETA's
   (its $m$-function / spectral measure = the $\Xi$ data). Conditional on the limit existing, this
   is EQUIVALENT to the identification clause the corrected Hamburger pin already isolated (#160:
   reformulated, not reduced); the pin is the right tool for exactly this leg, and its engine is
   the lattice (the correct tariff site).
2. **Non-degeneracy / no escape**: the limit chain must not degenerate (indivisible-interval
   collapse, mass escaping to the boundary of the compact space, the limit being a proper
   truncation of zeta's chain). This is the same mass-conservation clause as 1.1, in Hamiltonian
   coordinates; a two-sided trace statement (C1-shaped).

**The known program on this class, and its known failure point.** De Branges' own RH approach
lives here; Conrey-Li examined it: "L. de Branges proposed an approach to the Riemann hypothesis
using certain positivity conditions. In this paper, the authors examine this approach and indicate
its difficulty" [FETCH-VERIFIED abstract, arXiv:math/9812166; the specific content, that the
relevant positivity conditions fail numerically for $\zeta$'s $E$-functions, is SECONDARY].
Lagarias showed that ASSUMING RH the natural de Branges space for an L-function exists with the
norm essentially the Weil form [SECONDARY, Lagarias 2006]. Suzuki's current program is the nearest
live neighbor: "We study the Hilbert space obtained by completing ... with respect to the hermitian
form arising from the Weil distribution under the Riemann hypothesis. It turns out that this
Hilbert space is isomorphic to a de Branges space ... applied to state a new equivalence condition
for the Riemann hypothesis" [FETCH-VERIFIED abstract, arXiv:2301.00421, Suzuki; merged with his
2209.04658 screw-line paper]. Note the direction in ALL of these: they certify the LIMIT object
into the class conditionally on RH (or fail to, as Conrey-Li indicate). None runs the trojan's
direction: certify the FINITE objects (free), take the free compactness limit, and pay at
identification + non-degeneracy. The class's compactness leg has never been the failure point in
this literature; the failure point has always been certifying zeta's own object, which the trojan
deliberately does not attempt.

**The indefinite wrinkle (the #168 adjacency).** The honest finite objects carry $O(1)$ ghost
eigenvalues (the imperfect pole realization, e1k), so unquotiented they may certify only into the
indefinite classes $HB_\kappa$ (Kaltenback-Woracek; Part I read in full in-repo, entry theorem =
Thm 5.3 [FETCH-VERIFIED in-repo, `la_negative_square_check.md` Section 3]). Two facts matter.
First, the mirror-pair mechanism prices the rank-2 pole block at $\kappa = 1$ (in-repo candidate
computation, same note, Sections 5-6). Second, negative squares are lower semicontinuous in the
right sense (limits of kernels with $\le \kappa$ negative squares have $\le \kappa$)
[SECONDARY-CLASSICAL, Pontryagin-space theory]. The direction is right for compactness but WRONG
for exclusion: a $\kappa \le 1$ limit class does NOT forbid one non-real mirror zero pair, so the
trojan on this class needs the ghost-quotient (e1n's move) or a proof that the physical part
certifies into $HB_0$ strictly; otherwise the class admits exactly the failure mode it was hired
to exclude. And the one-sided extremal theory for $HB_1$ that would control this does not exist
in print (fresh search this session found only the classical $HB_0$ Beurling-Selberg school:
Carneiro-Littmann, Gaussian subordination arXiv:1008.4969 lineage [SECONDARY]; matches the
in-repo NOT-REPAIRABLE-AS-SEARCHED finding of `bbh_majorant_repair_rung.md` and the zero-hit grep
of K-W Part I).

**Tariff.** Leg (i) free after ghost handling ($HB_0$ for the quotiented objects; $\kappa \le 1$
raw). Compactness free (trace-norming). Leg (ii): on this class determinacy is not Carleman but
the Weyl limit-point/limit-circle dichotomy and the homeomorphism itself: uniqueness of the limit
given convergence of $m$-data on ONE disk ($|z - 2i| \le 1$); the $m$-data convergence is
spectral-sum / explicit-formula data = **Euler-consuming (correct site)**. Leg (iii) = the pin =
lattice (correct site). Relocation: identification (= #160's clause, no dodge) + non-degeneracy
(C1-shaped, NEW in this clothing: the repo has not previously isolated "no indivisible-interval
collapse of the limit chain" as the residue).

**Verdict: NEW-LOAD-BEARING (the single class worth a BUILDER rung).** Reasons in one line: the
only class where compactness is free, normalization-only, limit-compatible with $\Xi$'s maximal
type, and reality-preserving by class; and where both pay-sites land on the project's named
correct tariffs (Euler at $m$-convergence, lattice at the pin). The honest price is stated in
Section 5.

### 1.4 Determinate moment problems (Carleman, Krein; Stieltjes vs Hamburger)

**The theorems, at source** [FETCH-VERIFIED, Lin, "Recent developments on the moment problem,"
arXiv:1703.01027]: Carleman (Hamburger form, condition (h7) of Theorem 1):
$\sum_{k\ge1} m_{2k}^{-1/(2k)} = \infty$ implies determinacy ("the weakest checkable condition for
$X$ to be M-det on $\mathbb{R}$"); Stieltjes form (condition (s6) of Theorem 2):
$\sum_k m_k^{-1/(2k)} = \infty$; Krein (Hamburger): $\int_{-\infty}^{\infty}
\frac{-\log f(x)}{1+x^2}\,dx < \infty$ implies INdeterminacy (stated for distributions with a
positive density $f$ and all moments finite); Stieltjes variant (Graffi-Grecchi /
Slud): $\int_0^\infty \frac{-\log f(x^2)}{1+x^2}\,dx < \infty$ implies indeterminacy on
$\mathbb{R}_+$. Carleman is sufficient, not necessary [FETCH-VERIFIED, same source]. The
determinacy-equals-essential-self-adjointness frame (Jacobi-matrix form) is Simon's survey
[SECONDARY at the theorem level this session: only the abstract page of arXiv:math-ph/9906008 was
reachable; the frame statement "convergence of Pade approximants appears as strong resolvent
convergence of finite matrix approximations to a Jacobi matrix" is on the fetched abstract].

**What this class actually is in the trojan: the GLUE, not the carrier.** Compactness (Helly /
Prokhorov selection) plus determinacy of the limit moment sequence plus moment convergence is the
classical method of moments [SECONDARY-CLASSICAL]: it is the probability-theory avatar of exactly
the composite move this survey prices, and it is standard THERE because the objects are measures.
For the zeta trade the honest accounting is:

- The zero-counting measures have infinite mass; the natural finite-mass weighting
  $\sum_k \delta_{\gamma_k}/(\tfrac14+\gamma_k^2)$ has DIVERGENT higher moments, so Carleman does
  not apply to it directly. The usable determinacy lives one level up, on the spectral measure of
  the limit canonical system (class 1.3), where the dichotomy is Weyl limit-point vs limit-circle.
- Carleman/Krein inputs are moment/density growth = **density-only data**. By the DMV screen this
  leg can carry NO discrimination, and that is acceptable: uniqueness glue is allowed to be
  density-only. The discrimination must sit in the moment-CONVERGENCE input (weighted spectral
  sums = explicit-formula = Euler) and in the identification (lattice). A trojan whose ONLY
  novel leg is determinacy has relocated nothing.

**Tariff.** As glue for 1.1 or 1.3: determinacy free-and-empty (density-only, correctly so);
moment convergence = Euler site; identification = lattice site. Standalone: nothing to certify,
no carrier.

**Verdict: ADJACENT-WATCH (as leg-(ii) glue for 1.1/1.3); OFF-TARGET standalone.**

### 1.5 Lorentzian polynomials (Branden-Huh)

**The theorems, at source** [FETCH-VERIFIED, arXiv:1902.03719, full text via ar5iv]: Lorentzian
polynomials are DEFINED as limits: "the polynomials in $\mathring{L}^n_d$ are called strictly
Lorentzian, and the limits of strictly Lorentzian polynomials are called Lorentzian." Theorem 2.25:
$L^n_d$ equals the closure of $\mathring{L}^n_d$ in the space of degree-$d$ homogeneous
polynomials (via a Nuij-type homotopy); Theorem 2.28: the projectivization $\mathbb{P}L^n_d$ is "a
compact contractible set with contractible interior $\mathbb{P}\mathring{L}^n_d$."

**The degree-growth obstruction, priced.** The compactness is at FIXED $(n, d)$. The finite-cutoff
objects have effective degree $N^* = \lfloor T/\phi \rfloor \to \infty$ (the lattice ceiling,
e1l/e1s), so the family never sits in one $\mathbb{P}L^n_d$; there is no cross-degree compactness
theorem, and the degree-$\infty$ locally-uniform closure of the (bivariate homogenized) real-rooted
world is the Laguerre-Polya/stable closure again, inheriting 1.2's verdict wholesale. The class's
celebrated wins (Adiprasito-Huh-Katz, Alexandrov-Fenchel transfers) are fixed-degree INEQUALITY
transfers, not limit theorems: exactly the pattern the Breadth Program already priced (the
fixed-indefinite-form space outside arithmetic geometry is mapped and insufficient, LEARNINGS
#119-#121). No certification route from zeta-shaped data into Lorentzian structure at growing
degree exists in the literature searched; the natural finite sections (Jensen polynomials) revert
to classes 1.1/1.2.

**Verdict: OFF-TARGET.** Compactness real but degree-pinned; the trojan needs the degree to grow,
and at growing degree the class collapses into 1.2.

### 1.6 Normal families with bounded type (Montel for HB with a uniform type bound)

**The classical statement.** A family of entire functions of exponential type $\le \sigma$,
uniformly bounded on $\mathbb{R}$, is normal (Bernstein's inequality plus Montel); the HB property
passes to locally uniform limits (limits are HB or degenerate) [SECONDARY-CLASSICAL, Boas, Entire
Functions; Levin, Lectures on Entire Functions; no single arXiv source fetched this session, tagged
honestly].

**Both ways to run it fail, for named reasons.**
- **Fixed $\sigma$:** excludes the family cofinally (types $\approx \log\lambda \to \infty$, e1m
  measured) and excludes $\Xi$ (maximal type; bounded real-axis zero density at finite type vs
  $\zeta$'s growing $\log T$ density). The class is simply the wrong ambient space for the limit.
- **Rescaled ($z = (\log\lambda) w$, type normalized to 1):** subsequential limits then exist, but
  they are the LOCAL scaling limits, and what survives the rescaling is spacing/density data only:
  precisely the "installed lattice line" the e1m/e1l budget face measured (mean spacing $\phi$ to
  2-3 percent; the exact $\sin(zL/2)$ far-budget tail). A density-matched Beurling fake has the
  SAME rescaled limits, so the rescaled route is DMV-killed by type: its discriminating leg is
  density-only. This is the type-divergence constraint of Section 0 in its sharpest form: the
  normalization this class forces discards exactly the arithmetic.

**Verdict: OFF-TARGET**, with the mechanism named (bounded-type normalization = density-only
regime).

---

## 2. The tariff table (where the RH content relocates, per class)

| Class | Compactness / closure theorem | Free for this family? | Certification of finite objects | Where the RH content relocates | Euler/lattice consumed at the right site? |
|---|---|---|---|---|---|
| 1.1 PF / Edrei-Thoma | Thoma simplex compact (product topology) [F-V math/0311369]; AESW form [F-V 2512.06468] | YES (parameter normalization; no type bound) | free (CF reality; parameters legal after normalization) | mass conservation on the simplex = two-sided weighted trace equality (C1) + pin | moment convergence = Euler; pin = lattice; determinacy-on-simplex free |
| 1.2 Laguerre-Polya | closed under locally uniform limits (Hurwitz frame) [SECONDARY-CLASSICAL] | NO (closed, not compact; Montel bound = the open uniform control) | free (CF reality) | does not relocate; stays at uniform convergence = M4 | n/a (no new leg) |
| 1.3 HB / dB chains / canonical systems | trace-normed Hamiltonians compact; $H \mapsto m$ homeomorphism [F-V 2409.04862, citing Remling 5.2] | YES (trace-norming absorbs diverging type; reality preserved by class) | free after ghost handling ($HB_0$ quotiented; $\kappa \le 1$ raw) | identification of the limit chain (= #160's clause) + non-degeneracy/no-escape (C1-shaped, newly isolated) | $m$-convergence = Euler; pin = lattice; both correct |
| 1.4 Determinate moments | Helly/Prokhorov + Carleman (h7)/(s6), Krein [F-V 1703.01027] | glue only (no carrier) | n/a | nothing relocated standalone; as glue, discrimination correctly pushed to moment convergence | determinacy density-only (allowed: carries no weight) |
| 1.5 Lorentzian | $L^n_d$ closed, $\mathbb{P}L^n_d$ compact at fixed degree [F-V 1902.03719 Thm 2.25/2.28] | NO (degree grows; no cross-degree theorem) | no known route at growing degree | collapses to 1.2 | no |
| 1.6 Bounded-type normal families | Montel + Bernstein [SECONDARY-CLASSICAL] | NO (fixed type excludes limit) / YES-but-empty (rescaled) | free at fixed $\lambda$ | rescaled limit retains density only; DMV-killed | no (density-only) |

---

## 3. The composite move in the literature: has anyone posed "compactness + determinacy instead of uniform convergence" for these limits?

Short answer: **no, nowhere found**, across all four checked corpora, and the ADVERSARY re-sweep
(the RMT canonical-systems school, the moment-determinacy literature, a Hilbert-Polya
normal-family search) found no prior either; the closest miss is named in 3.5. The move's two avatars in
neighboring fields (method of moments in probability; Killip-Simon sum rules in spectral theory)
are standard, which makes the absence a genuine gap rather than a known dead end; but in both
avatars the sign/support structure is an INPUT, and that is the disqualifier-shaped catch (3.4).

### 3.1 The CCM semilocal corpus (2511.22755, 2511.23257, 2602.04022, 2606.06604)

- **arXiv:2511.22755, "Zeta Spectral Triples," Connes-Consani-Moscovici** [FETCH-VERIFIED, full
  text via ar5iv + abstract page]. The convergence goal: spectra/determinants "converge towards
  the zeros of $\zeta(1/2+is)$ as the parameters $N, \lambda \to \infty$"; "This convergence would
  entail RH using Hurwitz theorem on the zeros of limits of holomorphic functions." The remaining
  open step is described in Section 7 (Outlook): "Justifying rigorously this step is the main
  remaining obstacle to our approach to RH," where "this step" attaches to justifying that the
  eigenfunctions $\xi_\lambda$ are well-approximated by the prolate ansatz of their educated-guess
  formula (7.6). **Keyword scan of the full text: zero hits** for normal family, Montel, Vitali,
  Helly, subsequence(-tial), moment (problem), determinate, Carleman, Krein; "compact" occurs only
  in the compact-resolvent sense (Prop. 3.5). The architecture is uniform-convergence-plus-Hurwitz
  by design.
- **arXiv:2511.23257, "Quadratic Forms, Real Zeros and Echoes of the Spectral Action,"
  Connes-van Suijlekom** [FETCH-VERIFIED: abstract page + full text, completed by ADVERSARY
  2026-07-22 via PDF text extraction after the broken ar5iv conversion]. The abstract lists the
  five-step architecture ending with "(5) Finally, we apply a classical theorem of Hurwitz
  concerning the zeros of uniform limits of holomorphic functions"; the same step-(5) sentence
  recurs in the introduction. **Keyword scan of the full text: zero hits** for normal family,
  Montel, Vitali, Helly, subsequential, moment problem, determinate, Carleman, Krein (the single
  "subsequent" hit is "subsequent rows in T", a matrix-induction step); "compact" occurs only as
  compact selfadjoint operator and as "compact subsets" inside the uniform-convergence-plus-
  Hurwitz proofs. The uniform-limit frame is the whole architecture, at source; consistent with
  the in-repo read `reading_notes/CCM-2025-Dlog-family.md`.
- **arXiv:2602.04022, Connes, "The Riemann Hypothesis: Past, Present and a Letter Through Time"**
  [FETCH-VERIFIED, full text via ar5iv]. "While the numerical evidence in support of this is
  overwhelming, evidence alone is not a proof." **Keyword scan: zero hits** on the same list
  (Hadamard factorization, Jensen's formula, Nevanlinna characteristic appear; no compactness-based
  existence argument anywhere). No strategy other than uniform convergence + Hurwitz is proposed.
- **arXiv:2606.06604, Connes-Consani, "On the Absolute Geometry of Spec Z"** [abstract
  FETCH-VERIFIED]. Substrate/trace-side only ($\mathbb{F}_1$-structure sheaf, perfectoid untilts,
  Tate curve, Fargues-Fontaine real analogue); the abstract carries no positivity, polarization,
  Hodge-index, or limit/convergence clause. Confirms the repo's existing trace-side-only read
  (`reading_notes/Connes-Consani-2026-Absolute-Geometry-SpecZ.md`); not a composite-move site.

### 3.2 De Branges's own attempts and their refutation

De Branges's RH program lives on class 1.3 and consumed axiomatic POSITIVITY hypotheses, not
compactness: the known examination is Conrey-Li, "A note on some positivity conditions related to
zeta- and L-functions" [FETCH-VERIFIED abstract, arXiv:math/9812166]: "L. de Branges proposed an
approach to the Riemann hypothesis using certain positivity conditions. In this paper, the authors
examine this approach and indicate its difficulty." (The sharper folklore reading, that the
positivity conditions demonstrably FAIL for $\zeta$, is [SECONDARY] this session.) Structurally
decisive for this survey: de Branges's failure point is the CERTIFICATION of zeta's limit object
into the positive class, i.e. the leg the trojan deliberately does not attempt; no de Branges text
found poses free-compactness-plus-determinacy on the finite objects. The compactness resources of
his own theory (the ordering theorem, the chain structure) sat unused for that purpose.

### 3.3 Kaltenback-Woracek indefinite $HB_\kappa$ theory (the #168 adjacency)

In-repo, Part I is read in full with the entry theorem pinned (Thm 5.3; converse direction
hypothesis-free beyond $E \in HB_\kappa$) and a zero-hit grep for majorant/extremal content
[FETCH-VERIFIED in-repo, `la_negative_square_check.md`]. Fresh search this session for a one-sided
extremal / admissible-majorant theorem in any indefinite class: **still nothing**; every hit is the
classical $HB_0$ Beurling-Selberg school (Carneiro-Littmann line, Gaussian subordination
arXiv:1008.4969 lineage) [SECONDARY]. So the #168 HB$_1$ question (does a one-sided extremal
theorem exist for $HB_1$) remains open-and-unclaimed in print, and the trojan's indefinite wrinkle
(1.3 above) has no off-the-shelf control: if the finite objects are run unquotiented (raw
$\kappa \le 1$), the class itself cannot exclude a mirror pair of non-real zeros in the limit.
Parts II, III, V, VI of K-W remain unread (standing residual of `bbh_majorant_repair_rung.md`).

### 3.4 The Killip-Simon sum-rule school (the mechanism that proves the pattern CAN work)

Killip-Simon (Ann. of Math. 158 (2003) 253-321 = arXiv:math-ph/0112008) [FETCH-VERIFIED at theorem
level, ADVERSARY 2026-07-22: abstract, Theorem 1, and the Section-5 method statements fetched] is,
in its proof pattern, EXACTLY the trojan executed in a neighboring field: a sum rule (a
trace-formula identity whose two sides are sign-structured) plus Helly compactness of spectral
measures plus one-sided SEMICONTINUITY of an entropy functional under weak convergence replaces
uniform operator control, and delivers a complete spectral classification (Hilbert-Schmidt
perturbations of the free Jacobi matrix) with no uniform convergence anywhere. At source: Theorem 1
characterizes $J - J_0$ Hilbert-Schmidt by four measure-side properties (Blumenthal-Weyl support,
quasi-Szego integral, Lieb-Thirring eigenvalue sum, normalization), and the method section is
literally titled "Entropy and lower semicontinuity of the Szego and quasi-Szego terms" (the
entropy map is "weakly lower semicontinuous"). The pedagogical account of the
semicontinuity-based proof is the Gamboa-Nagel-Rouault large-deviations line (arXiv:1608.01467)
[SECONDARY, search-located].

**Is a zeta analogue posed anywhere? NO** (search-verified absence this session). The existing
"sum rules for zeta" literature is a different animal: power-sum identities over zeros in the
Lehmer-Keiper lineage, e.g. McPhedran, "Sum Rules for Functions of the Riemann Zeta Type"
[FETCH-VERIFIED abstract, arXiv:1801.07415: connects Taylor coefficients "with sums of powers of
reciprocals of the zeros, in the form of sum rules," explicitly Lehmer/Keiper-style], and
"A sum rule for the critical zeros of $\zeta$" (arXiv:1309.7040) [SECONDARY]: identities, with no
compactness leg, no semicontinuity leg, no classification.

**The catch, stated as a disqualifier.** In Killip-Simon the essential support $[-2,2]$ (the
"line") is an INPUT to the sum rule (one direction of Theorem 1 does output $\sigma_{ess} =
[-2,2]$, but that direction is Weyl-soft: essential-spectrum preservation under a compact
perturbation; the sign-structured sum rule itself is anchored to the $[-2,2]$ reference operator),
and the sign structure of both sides is supplied by the class
(the entropy is $\le 0$, the eigenvalue term is $\ge 0$). The zeta transfer would need the line as
an OUTPUT, and a zeta sum rule with two sign-definite sides IS a Weil-positivity statement: the
trade exploits an existing sign, it does not create one. What survives honestly: the K-S pattern
shows that a ONE-SIDED, lower-semicontinuous functional inequality at finite cutoff can survive
weak limits without uniformity. That is BRIDGE-H's shape (one-sided, positivity-free), so this row
feeds the S4/R1 coordinate (`landau_one_sided.md` Section 3.4), not M4 directly. A zeta sum rule
in the K-S sense, if one existed with a nameable Euler-consuming side, would be the first genuinely
new mechanism this survey found room for; none is in print.

### 3.5 The nearest live neighbors, for completeness

- **Suzuki** (arXiv:2301.00421 [FETCH-VERIFIED abstract], merging the 2209.04658 screw-line paper):
  the Weil-form Hilbert space is a de Branges space UNDER RH, with a new RH equivalence. Direction:
  limit-object certification, conditional; not the trojan.
- **Suzuki's earlier canonical-system program** (arXiv:1204.1827, "A canonical system of
  differential equations arising from the Riemann zeta-function") [FETCH-VERIFIED abstract,
  ADVERSARY round]: the canonical system attached to $\Theta_\omega$ is "constructed explicitly
  and unconditionally under the restriction of the parameter $\omega > 1$", and extending to all
  $\omega > 0$ would give a criterion that "explains the validity of the Riemann hypothesis as
  positive semidefiniteness of the corresponding family of Hamiltonian matrices". The nearest
  canonical-system-native RH statement in print; direction is still inverse-construction /
  limit-object certification, with no compactness leg and no determinacy leg.
- **The RMT canonical-systems school (the closest miss to the composite move)** [ADVERSARY round]:
  Valko-Virag's stochastic zeta function (arXiv:2009.04670, GAFA 2022) and successors (e.g.
  Painchaud arXiv:2510.06120, hard-edge-to-bulk operator limits via canonical systems, convergence
  in the vague topology; Hur arXiv:1501.01268, which uses the $V_+$ compactness itself) run the
  COMPACTNESS HALF of the composite move as standard technology: operator-level limits of
  $\beta$-ensembles through canonical systems with Weyl-data convergence in weak topologies, no
  uniform operator control. But the targets are random universality-class operators (Sine$_\beta$,
  Bessel: Level 3 in the repo's framing), the limits are identified probabilistically, and no
  determinacy pin to a deterministic arithmetic limit appears; no $\Xi$, no RH claim. The
  composite move for zeta-shaped Section-7 limits remains unposed.
- **The classical Polya/approximates program** (component functions of $\Xi$ approximants,
  expanding-subregion arguments) [SECONDARY, search-located]: uniform-convergence-based throughout;
  no compactness+determinacy variant found.
- **GORZ Jensen certification** (1.1 above): finite certification into hyperbolicity classes,
  covering the RH-free corners only; no limit mechanism.

---

## 4. Verdict table

| Class | Verdict | One-line reason |
|---|---|---|
| Polya frequency / Edrei-Thoma | **ADJACENT-WATCH** | The one free weak-topology compactness; relocation lands cleanly on C1 (mass conservation) + Euler (moments) + lattice (pin); no literature route to the mass clause |
| Laguerre-Polya | **KNOWN-TO-REPO** | Verbatim the Hurwitz frame (CCM step 5); closed, not compact; the Montel bound IS the open uniform control |
| HB / de Branges chains / canonical systems / Krein strings | **NEW-LOAD-BEARING** | Free trace-normed compactness [F-V Remling 5.2 via 2409.04862], type-divergence-proof, reality preserved by class; RH content relocates to identification (= #160 pin clause) + a newly isolated non-degeneracy clause |
| Determinate moment problems (Carleman/Krein) | **ADJACENT-WATCH** (glue) / OFF-TARGET standalone | Determinacy is density-only and correctly weightless; the discrimination must sit in moment convergence (Euler) and the pin (lattice) |
| Lorentzian polynomials | **OFF-TARGET** | Compactness degree-pinned (Thm 2.28 at fixed $d$); the family's degree grows; at growing degree the class collapses into Laguerre-Polya |
| Bounded-type normal families | **OFF-TARGET** | Fixed type excludes $\Xi$ (maximal type) and the family (types $\log\lambda$ diverge); rescaling retains density only = DMV-killed |
| Composite move itself (all corpora) | **UNPOSED** | Zero hits in CCM corpus / de Branges / K-W / sum-rule school + ADVERSARY sweep; closest miss = RMT canonical-systems school (compactness half only, Level 3 targets); its avatars (method of moments, Killip-Simon) are standard elsewhere with sign/support as INPUT |

## 5. The honest close: which single class, and where the content goes in the best case

**The single class worth a BUILDER rung is 1.3 (canonical systems / de Branges chains under trace
normalization).** It is the only candidate that passes all four structural gates at once: the
compactness is proven and free [FETCH-VERIFIED, Forester-Remling 2409.04862 quoting Remling,
Spectral Theory of Canonical Systems, Sec. 5.2]; the normalization absorbs the measured type
divergence instead of fighting it; the finite objects certify essentially for free (with the ghost
caveat); and the class preserves the reality/line structure through the limit, which is the one
thing uniform convergence was being paid to protect.

**Where the RH content relocates in the best case.** Not away. It splits into exactly two clauses:
(a) **identification** of the subsequential-limit chain as zeta's, which conditional on the limit
existing is EQUIVALENT to the corrected Hamburger pin's inheritance clause (#160: reformulated,
not reduced), payable only by the lattice; and (b) **non-degeneracy / no mass escape** of the limit
(no indivisible-interval collapse, no proper-truncation limit), a two-sided trace statement, i.e.
C1-shaped, payable only by an Euler-consuming convergence of $m$-function / weighted-spectral-sum
data. The trojan therefore does NOT reduce the problem; what it genuinely buys, if built, is
(i) elimination of the UNIFORMITY layer as a separate cost (subsequential existence and limit
reality become free), and (ii) the isolation of clause (b), "no chain degeneration," as a new,
precisely shaped residual the repo has not previously named as such. The realistic risk, attacked this
round (adversary report, 2026-07-22): at STATEMENT level clause (b) is NOT the uniform det-class
control; it is a strictly weaker-topology statement (tightness / trace-equality of the weighted
spectral data, with no rate and no locally uniform determinant convergence), M4 implies it, and no
converse is visible, so the trade genuinely weakens what must be proven. The surviving risk is at
PRICE level: the only known routes to two-sided trace equalities of this shape are the same
explicit-formula inputs M4 consumes, so the cost may be conserved even though the statement is
weaker. Two sharpenings from the attack: clause (b) ALONE is Beurling-satisfiable at density level
(the fake's chains non-collapse and conserve density mass identically), so all discrimination must
sit in the exact Euler-weighted equality inside the (a)+(b) joint; and an off-line zero pair of
the true $\Xi$ manifests in these coordinates not as escape at real infinity but as a LOCAL mass
defect of the limit measure against zeta's global data, i.e. clauses (a) and (b) are entangled and
the RH weight sits in their conjunction (the exact-mass identification). If the price does
conserve, the rung's value reduces to (ii) alone, a reformulation with a new proof surface (Weyl
theory, limit-point/limit-circle, the $m$-homeomorphism) rather than a strength reduction. Given the project's experience with #160 (reformulated-not-reduced was still judged
worth having, for the positivity-free surface), that is the honest expected value here too: a
THIRD proof surface for the same residue (variational / lattice-Hamburger / now Weyl-spectral),
not a smaller residue.

## 6. Discrepancy log (reported, not resolved)

1. **GORZ statement strength: RESOLVED (ADVERSARY 2026-07-22).** The arXiv abstract of 1902.07321
   (as served) states "hyperbolicity of a density 1 subset of the Jensen polynomials of each
   degree" plus "all $d \le 8$"; the published PNAS version (10.1073/pnas.1902572116, re-fetched
   at source) states the stronger cofinite form: abstract "prove the hyperbolicity of all but
   finitely many of the Jensen polynomials of each degree", Theorem 1 "$J_\gamma^{d,n}(X)$ is
   hyperbolic for all sufficiently large $n$". Both statements are real, from different versions;
   quote the published cofinite form, which subsumes density-1.
2. **2511.22755's title.** The paper is titled "Zeta Spectral Triples" [FETCH-VERIFIED, abstract
   page]; the repo reading note carries it under the working label "CCM-2025-Dlog-family". No
   contradiction, but the record should carry the real title.
3. **The "main remaining obstacle" attachment point.** This session's full-text fetch attaches the
   2511.22755 quote to justifying the prolate-ansatz approximation of the eigenfunctions (their
   eq. 7.6), consistent with e1m's D2 gloss note (CCM's own Section-7 wording is
   eigenvector-identification, not "positivity"). The repo's shorthand "Section-7 uniform
   convergence is the obstacle" remains a fair gloss (the convergence sentence and the obstacle
   sentence are adjacent and coupled), but the verbatim attachment is the ansatz-justification
   step.
4. **Olshanski fetch artifact.** The fetched summary of arXiv:math/0311369 attached the phrase
   "space of virtual permutations" to the Thoma set $\Omega$; in Olshanski's text that name
   belongs to a different object (the projective-limit space of the $S(n)$). The compactness
   sentence for $\Omega$ itself is taken as fetched; the naming conflation is flagged as a
   fetch-model artifact, not repeated in the body above.
5. **Carleman dating.** Lin's survey (as fetched) labels (h7) "Carleman's 1926 condition";
   secondary sources commonly date it 1922 (or 1923, Les fonctions quasi-analytiques). Lin's own
   label re-confirmed at source this round (the survey does print "Carleman's (1926) condition");
   the 1922/1923 question concerns Carleman's original publication, not Lin's text. Cosmetic;
   unresolved.
6. **CCM convergence-mode precision (ADVERSARY 2026-07-22).** 2511.22755 Section 7 states the
   target convergence "uniformly on closed substrips of the open strip $\Im(z) < 1/2$", which is
   stronger than this note's original Section-0 gloss "uniformly on compacts" (the weaker form is
   all Hurwitz needs, so the gloss was safe, not inverted). Section 0 now carries the verbatim
   form alongside the gloss.

## 7. Reference list with verification tags

Fetched at source this session:
- arXiv:2511.22755, Connes-Consani-Moscovici, "Zeta Spectral Triples" [FETCH-VERIFIED: abstract
  page + ar5iv full text; Section-7 quotes + keyword scan].
- arXiv:2511.23257, Connes-van Suijlekom, "Quadratic Forms, Real Zeros and Echoes of the Spectral
  Action" [FETCH-VERIFIED: abstract page + full text (ADVERSARY 2026-07-22, PDF extraction after
  the broken ar5iv conversion); keyword scan zero hits, step-(5) Hurwitz verbatim; consistent
  with the in-repo read `reading_notes/CCM-2025-Dlog-family.md`].
- arXiv:2602.04022, Connes, "The Riemann Hypothesis: Past, Present and a Letter Through Time"
  [FETCH-VERIFIED: ar5iv full text; keyword scan zero hits].
- arXiv:2606.06604, Connes-Consani, "On the Absolute Geometry of Spec Z" [FETCH-VERIFIED:
  abstract verbatim].
- arXiv:1703.01027, Lin, "Recent developments on the moment problem" [FETCH-VERIFIED: Carleman
  (h7)/(s6), Krein Hamburger + Stieltjes forms, sufficiency-not-necessity, via ar5iv].
- arXiv:math/0311369, Olshanski, "An introduction to harmonic analysis on the infinite symmetric
  group" [FETCH-VERIFIED: Thoma's theorem Sections 3.2-3.3, simplex compactness; see discrepancy 4].
- arXiv:2512.06468 (convolution operators preserving totally positive sequences) [FETCH-VERIFIED:
  Theorem ASWE verbatim with references].
- arXiv:1902.03719, Branden-Huh, "Lorentzian polynomials" [FETCH-VERIFIED: definition-as-limits,
  Thm 2.25 closure, Thm 2.28 projective compactness, via ar5iv].
- arXiv:1902.07321, Griffin-Ono-Rolen-Zagier [FETCH-VERIFIED: abstract; see discrepancy 1].
- arXiv:2409.04862, Forester-Remling, "Topological properties of reflectionless canonical systems"
  [FETCH-VERIFIED: compactness of trace-normed canonical systems + $H \mapsto m$ homeomorphism,
  quoting; both citing Remling, Spectral Theory of Canonical Systems, Sec. 5.2].
- arXiv:math/9812166, Conrey-Li, "A note on some positivity conditions related to zeta- and
  L-functions" [FETCH-VERIFIED: abstract verbatim].
- arXiv:2301.00421, Suzuki, "On the Hilbert space derived from the Weil distribution"
  [FETCH-VERIFIED: abstract verbatim; v3 merges 2209.04658].
- arXiv:1801.07415, McPhedran, "Sum Rules for Functions of the Riemann Zeta Type" [FETCH-VERIFIED:
  abstract; classified Lehmer/Keiper power-sum, not Killip-Simon-type].
- arXiv:math-ph/9906008, Simon, "The Classical Moment Problem as a Self-Adjoint Finite Difference
  Operator" [abstract page fetched; theorem-level content SECONDARY].

Fetched at source by the ADVERSARY pass (2026-07-22):
- arXiv:math-ph/0112008, Killip-Simon, "Sum Rules for Jacobi Matrices and Their Applications to
  Spectral Theory" (= Ann. of Math. 158 (2003) 253-321) [FETCH-VERIFIED: abstract, Theorem 1,
  Section-5 semicontinuity statements].
- arXiv:1501.01268, Hur, "Density of Schrodinger Weyl-Titchmarsh m functions on Herglotz
  functions" [FETCH-VERIFIED: full-text passages; $V_+$ compactness + homeomorphism onto
  $\mathcal{H} \cup \mathbb{R} \cup \{\infty\}$; independent corroboration of the Remling-book
  pillar].
- arXiv:1204.1827, Suzuki, "A canonical system of differential equations arising from the Riemann
  zeta-function" [FETCH-VERIFIED: abstract].
- arXiv:2009.04670 (Valko-Virag, stochastic zeta function) and arXiv:2510.06120 (Painchaud,
  hard-edge-to-bulk via canonical systems) [abstract-level: the RMT canonical-systems school,
  closest miss to the composite move].
- PNAS 10.1073/pnas.1902572116 (GORZ published version) [FETCH-VERIFIED: abstract + Theorem 1,
  cofinite form; resolves discrepancy 1].

Secondary (not read at source this session; used for statements marked [SECONDARY]):
- Gamboa-Nagel-Rouault arXiv:1608.01467 (pedagogical large-deviations account of the sum-rule
  semicontinuity method; Killip-Simon itself is now source-verified, see the ADVERSARY block
  above).
- de Branges, Hilbert Spaces of Entire Functions (1968); ordering theorem.
- Levin (Distribution of Zeros; Lectures), Boas (Entire Functions): LP definition/closure,
  Bernstein-Montel, maximal-type facts.
- Kac-Krein string theory; Kasahara 1975 continuity of the string correspondence.
- Csordas-Norfolk-Varga 1986 (Turán inequalities for $\Xi$); Rodgers-Tao $\Lambda \ge 0$;
  Lagarias 2006 (dB spaces for L-functions under RH); Aissen-Edrei-Schoenberg-Whitney originals
  (PNAS 37 (1951) 303-307; J. Anal. Math. 2 (1952) 93-109); arXiv:1309.7040; Carneiro-Littmann /
  arXiv:1008.4969 (classical HB$_0$ extremal school).

In-repo verified state relied on: `ccm_semilocal_prolate.md` (+ addenda through 2026-07-22),
`landau_one_sided.md`, `la_negative_square_check.md`, `bbh_majorant_repair_rung.md`,
`e1m_hamburger_pin.md`, `e1k/e1l/e1n/e1s` records, `_shared/beurling.py` (DMV screen),
LEARNINGS #152-#169.

## 8. What this enables / what remains open

**Enables (for BUILDER).** One rung, precisely shaped: encode the (ghost-quotiented) finite
objects $\hat\xi_\lambda$ as structure functions of finite trace-normed canonical systems (the
e1s Cauchy-compression nesting is the finite germ), embed in Remling's compact space, and measure
the two relocated clauses: does the subsequential-limit Hamiltonian degenerate (indivisible
intervals, mass escape), and what $m$-function data would identify it (feeding the #160 pin)?
Cheap first probe: numerically compute the finite Hamiltonians for the existing e1k builds and
watch the limit behavior of the trace-normed length. The Beurling and D-H controls must run: the
fake's finite chains embed in the SAME compact space (compactness is density-blind, as expected);
the discrimination must appear, nameably, in the $m$-convergence data and nowhere else.

**Enables (for ADVERSARY).** Three attack surfaces, in order: (1) EXECUTED at reasoning level
(2026-07-22 pass; Section 5 and the adversary report): no statement-level equivalence (clause (b)
is strictly weaker-topology; M4 implies it, no converse visible); the remaining open half is
price-level (whether proving (b) consumes the same explicit-formula inputs), a BUILDER-measurable
question; (2) the indefinite wrinkle: with
raw $\kappa \le 1$ finite objects, exhibit the mirror-pair limit mode the class fails to exclude
(the la_negative_square mechanism run in reverse); (3) the DMV screen on any proposed
identification step: if the limit chain is identified through counting/density data alone, it is
pre-killed (e1m's P3 already proved counting cannot pin).

**Remains open (SURVEYOR items).** (1) The zeta sum rule in the Killip-Simon sense: no such
object is in print; whether one can even be POSED with an Euler-consuming sign-definite side is
unasked in the literature, and it connects to the S4/R1 (one-sided, semicontinuity) coordinate
rather than M4. (2) K-W Parts II/III/V/VI remain unread; the HB$_1$ one-sided extremal question
(#168) remains unclaimed in print. (3) The mass-conservation clause on the Thoma simplex (1.1)
has no literature; if the canonical-system rung stalls, the parameter-simplex frame is the
fallback carrier for the same two clauses. (4) DONE (ADVERSARY 2026-07-22): the GORZ published-version check (discrepancy 1
resolved, cofinite form) and the source-level Killip-Simon read (Theorem 1 + semicontinuity
method) are banked; the remaining hardening item is a source read of Remling's book Section 5.2
itself (the pillar currently rests on 2409.04862 quoting it, independently corroborated by Hur
arXiv:1501.01268).
