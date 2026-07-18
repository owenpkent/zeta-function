# The two cheap S4 frame falsifiers: Carneiro-Littmann well-posedness in the Sonin space, and the interpolation-identity check

> SURVEYOR dossier, 2026-07-17. Runs falsifiers 2 and 4 named in
> [`ccm_corridor_frame_audit.md`](ccm_corridor_frame_audit.md) Section 3, handed forward as the
> named SURVEYOR fetches in [`s4_carrier_audit.md`](s4_carrier_audit.md) Section 7 and in
> [`../../TODO.md`](../../TODO.md)'s live-corridor section. Both are gate checks: per the frame
> audit's Section 4 exit rule, they run before the expensive Sonin-projector BUILDER round, and a
> trip on falsifier 2 alone is pre-registered to close the corridor as a proof home.
>
> **Question 1 verdict (falsifier 2):** ILL-POSED on the one branch of Burnol's Sonine-space
> corpus that would actually carry the corridor's counting-side content. Burnol's own *extended*
> Sonine space, the one built to host the Riemann zeta zeros as spectral data, requires functions
> with simple poles at $s=0$ and $s=1$ (Burnol, arXiv:math/0203120, Proposition 2.2), which falls
> outside the entire-Hermite-Biehler axiom that Carneiro-Littmann's own Theorem 1 opens by assuming
> (arXiv:1406.5456: "Let $E$ be a Hermite-Biehler function satisfying properties (P1)-(P4)").
> The *generic* (non-zeta-loaded) branch of the same corpus is well-posed by the same axioms, but
> it is exactly the branch the corridor's own e1o probe already measured content-free ("the generic
> trig space," majorant-nil). One adjacent literature (meromorphic model-space majorant theory,
> Baranov-Borichev-Havin) is named but not excluded; see Section 1.3.
>
> **Question 2 verdict (falsifier 4):** MIXED. Every explicit, named-author interpolation or
> summation identity found in this search (Radchenko-Viazovska; the Cohn-Elkies linear-programming
> bound realized by the Viazovska/CKMRV magic functions; Bondarenko-Radchenko-Seip) is lattice-,
> modular-, or functional-equation-tied, and the one perturbation theorem in print (Ramos-Sousa)
> only *shrinks* the tie asymptotically, it never escapes to genuine incommensurability.
> Kulikov-Nazarov-Sodin (arXiv:2306.14013) proves an abstract density-only sufficient condition for
> a uniqueness-and-interpolation pair that is explicitly stated to be independent of rational
> commensurability, a real mechanism-class escape, but its fit to the corridor's actual node set
> $\{k \log p\}$ is unverified, and a first-pass growth-rate check (done in this survey, not sourced
> from any paper) suggests a mismatch. See Section 2.3.
>
> **Consequence for the corridor exit rule:** falsifier 2 trips, against the specific machinery the
> corridor's own docs point to, on the only branch that matters to the corridor's question. Full
> reasoning and recommendation in Section 4.
>
> Method discipline followed throughout: every load-bearing claim is tagged [FETCHED] (read at
> source this session, including via arXiv abstract pages and ar5iv HTML renderings),
> [SECONDARY] (read via a citing paper or search snippet, not the primary source directly), or
> flagged as this survey's own unsourced derivation. No claim is promoted across tiers. No em
> dashes.
>
> **Adversary verification (same day, second independent pass):** the two load-bearing citations
> were re-fetched at source by the session's main loop after this dossier landed. Carneiro-Littmann
> arXiv:1406.5456 confirms the framework requires an ENTIRE Hermite-Biehler $E$ ("an entire function
> that satisfies $|E^*(z)| < |E(z)|$", properties (P1)-(P4); no meromorphic extension anywhere in
> the paper). Burnol arXiv:math/0203120 confirms Prop. 2.2 (completed Mellin transforms of $L_a$
> are "meromorphic ... with at most poles at 0 and at 1"), Thm. 2.1 ($K_a$ entire, classical
> axioms), and Prop. 4.5 ($\dim(L_a/K_a) = 2$, the two residue-evaluators at $s = 0, 1$). The
> Question 1 verdict is upheld as stated; the closure remains conditional on the two named
> residuals (Sections 1.3 and 4). Recorded as LEARNINGS #164.

## 1. Question 1: does Carneiro-Littmann/Holt-Vaaler pose in Burnol's Sonine spaces?

### 1.1 Sources

| Source | arXiv / DOI | Tier | What it gives |
|---|---|---|---|
| Carneiro, Littmann, Vaaler, "Gaussian Subordination for the Beurling-Selberg Extremal Problem" | arXiv:1008.4969, Trans. Amer. Math. Soc. 365 (2013) 3493-3534 | FETCHED (abstract) | Founding Gaussian-subordination method for one-sided majorants of exponential type |
| Carneiro, Littmann, "Extremal functions in de Branges and Euclidean spaces" | arXiv:1406.5456, Adv. Math. 260 (2014) 281-349 | FETCHED (abstract + Theorem 1 hypotheses, via ar5iv) | The general hypotheses (P1)-(P4) on the structure function $E$; the homogeneous/Bessel worked example $E_\nu$ |
| Carneiro, Littmann, "Extremal functions in de Branges and Euclidean spaces II" | arXiv:1508.02436, Amer. J. Math. 139 (2017) 525-566 | SECONDARY (search snippet only, not fetched) | Multidimensional radial extension of the same $E_\nu$ family |
| Holt, Vaaler, "The Beurling-Selberg extremal functions for a ball in Euclidean space" | Duke Math. J. 83 (1996) 203-248 (pre-arXiv, no preprint found) | SECONDARY (via Carneiro-Littmann's own citing description plus independent search snippets) | Originating reformulation of the ball/sign-function extremal problem inside de Branges' Hilbert-space-of-entire-functions theory |
| Burnol, "Sur les espaces de Sonine associés par de Branges à la transformation de Fourier" | arXiv:math/0208121, C. R. Acad. Sci. Paris Sér. I 335 (2002) | FETCHED (ar5iv HTML) | Explicit structure function $\mathcal E_\lambda(w)$ (Theorem 8) for the *generic* prolate/Sonine space; no zeta-zero loading |
| Burnol, "Two complete and minimal systems associated with the zeros of the Riemann zeta function" | arXiv:math/0203120, J. Théor. Nombres Bordeaux 16 (2004) 65-94 | FETCHED (ar5iv HTML) | The *extended* Sonine space $L_a$ that hosts the zeta zeros: Prop. 2.2 (poles), Thm 2.1 (classical axioms hold for the un-extended $K_a$), Prop. 4.5 (codimension 2) |
| Suzuki, "A canonical system of differential equations arising from the Riemann zeta-function" | arXiv:1204.1827 | SECONDARY (search snippet) | Independent confirmation: the zeta-loaded canonical system needs Burnol's method and is unconditional only for a restricted parameter range ($\omega > 1$) |
| Baranov, Borichev, Havin, "Majorants of meromorphic functions with fixed poles" | arXiv:math/0605052, Indiana Univ. Math. J. 56 (2007) 1595-1628 | FETCHED (abstract) | Adjacent *model-space* (Blaschke-product $K_B$) admissible-majorant theory, built for exactly the fixed-poles case; not connected to Burnol's $L_a$ or a CCM-type carrier in any source found |

### 1.2 Findings

**The Carneiro-Littmann/Holt-Vaaler hypotheses on $E$, named precisely.** Carneiro-Littmann's
Theorem 1 [FETCHED, arXiv:1406.5456] opens: "Let $E$ be a Hermite-Biehler function satisfying
properties (P1)-(P4)," with

- (P1) $E$ has bounded type in $\mathcal U$ (the upper half-plane),
- (P2) $E$ has no real zeros,
- (P3) $z \mapsto E(iz)$ is a real entire function,
- (P4) $A, B \notin \mathcal H(E)$ (where $E = A - iB$),

plus, for the Gaussian-subordination theorem specifically, the integrability condition
$\int_{-\infty}^{\infty} e^{-\lambda|x|}\,|E(x)|^{-2}\,dx < \infty$. By Krein's theorem, (P1) forces
$E$ to have exponential type. "Hermite-Biehler function" is by definition an *entire* function with
$|E(z)| > |E(\bar z)|$ for $\mathrm{Im}(z) > 0$: entireness is not one of the four numbered
properties because it is baked into the term itself, the whole theory is built for $E$ with no
poles anywhere in $\mathbb C$. The paper's own worked example is the *homogeneous* de Branges space
$E_\nu(z) = A_\nu(z) - iB_\nu(z)$ with $A_\nu(z) = \Gamma(\nu+1)(z/2)^{-\nu}J_\nu(z)$,
$B_\nu(z) = \Gamma(\nu+1)(z/2)^{-\nu}J_{\nu+1}(z)$: a concrete, entire, Bessel-built Hermite-Biehler
function. Carneiro-Littmann do not state a "chain" (nested-family) requirement across the parameter
$\nu$; each homogeneous space is treated as a fixed-parameter object, not as a family varying
uniformly with $\nu$. This matters directly for the corridor: even on the well-posed branch, no
published version of this machinery already addresses uniformity across a family parameter (the
corridor's own $\lambda$), that would be an additional, unaddressed requirement layered on top.
Holt-Vaaler's 1996 paper [SECONDARY, via Carneiro-Littmann's own citations and independent search]
is the originating instance of this same move: reformulating the ball/sign-function extremal
problem inside de Branges' Hilbert-space-of-entire-functions theory, again for an entire structure
function.

**Burnol's Sonine-space corpus splits into two branches, and only one of them is the one the
corridor wants.**

*Branch A, generic (no zeta loading).* Burnol's arXiv:math/0208121 [FETCHED, ar5iv] constructs an
explicit structure function via Theorem 8:
$$\mathcal E_\lambda(w) = \pi^{-w/2}\Gamma(w/2)\left(\lambda^{1/2-w} + \frac{\sqrt\lambda}{2}\int_\lambda^\infty \big(\psi_+^\lambda(t) - \psi_-^\lambda(t)\big)\,t^{-w}\,dt\right),$$
entire, satisfying the de Branges positivity inequality $|\mathcal E_\lambda(w)| > |\mathcal
E_\lambda(1-\bar w)|$ on the half-plane $\mathrm{Re}(w) > 1/2$ (the natural coordinate system here
puts the "upper half-plane" at $\mathrm{Re}(w) > 1/2$ and the "real axis" at the critical line
$\mathrm{Re}(w) = 1/2$, a Cayley-type recoordinatization, not a departure from the classical setup).
The companion functions $\mathcal A_\lambda, \mathcal B_\lambda$ have all their zeros exactly on
$\mathrm{Re}(w) = 1/2$, the P2/P3-analogue, satisfied unconditionally (this is a structural
consequence of $\mathcal E_\lambda$ being genuinely Hermite-Biehler, not a zeta-dependent claim).
The construction is built from Fourier-invariant distributions and the eigenfunctions $e_{2n}$ of
the classical time-and-band-limiting operator on $(-\lambda, \lambda)$: this is the Landau-Pollak-
Slepian prolate spheroidal picture, parametrized by the bandwidth $\lambda$, the same shape
parameter the CCM $D_{\log}$ carrier itself carries. The paper reports no explicit connection to
the Riemann zeta zeros; the $\pi^{-w/2}\Gamma(w/2)$ factor is present because it is the natural
archimedean weight for a Mellin-type construction on $(0,\infty)$, not because zeta zeros are
loaded into it.

*Branch B, extended (zeta-loaded).* Burnol's arXiv:math/0203120 [FETCHED, ar5iv] builds the
Sonine space $K_a$: functions in $L^2(0,\infty)$ vanishing, together with their Fourier cosine
transform, on $(0,a)$, with completed Mellin transform $M(f)(s) = \pi^{-s/2}\Gamma(s/2)\hat f(s)$.
Theorem 2.1 states plainly: "the space of functions $M(f)(s)$, $f \in K_a$ satisfies all axioms of
[de Branges'] general theory of Hilbert spaces of entire functions." $K_a$ itself is therefore a
bona fide, well-posed de Branges space, entire, no poles. But $K_a$ alone does not host the zeta
zeros as a complete or minimal system; for that, Burnol builds the *extended* space $L_a \supset
K_a$, tied to the spectral multiplier $\chi(s) = \zeta(s)/\zeta(1-s)$ (the zeta functional
equation), and this is where "the quotient contains vectors intrinsically attached to the
non-trivial zeros and their multiplicities" (per the paper's own abstract). Proposition 2.2 states
that $L_a$'s associated functions have "at most poles at 0 and at 1." Proposition 4.5 gives
$\dim(L_a / K_a) = 2$, exactly matching two simple poles, one at each of $s = 0$ and $s = 1$ (the
Gamma-factor pole and the zeta pole respectively). $L_a$ is $K_a$ extended by a two-real-dimensional
space of functions with prescribed poles, and it is $L_a$, not $K_a$, that carries the arithmetic
content the S4/R1 program wants: the actual location of the zeta zeros.

**The violated hypothesis, named.** Carneiro-Littmann's Theorem 1 requires $E$ Hermite-Biehler,
i.e. entire. Burnol's own Proposition 2.2 gives $L_a$'s structure function simple poles at $s = 0,
1$. $L_a$ is therefore not $\mathcal H(E)$ for an entire Hermite-Biehler $E$ in the classical sense
Carneiro-Littmann's and Holt-Vaaler's machinery assumes from their first line. Posing the
Beurling-Selberg/Gaussian-subordination one-sided extremal problem on $L_a$, the one Sonine space
in this corpus that actually encodes the zeta zeros, is a category error against the named theory
as published: the entireness hypothesis is exactly what fails, and it fails for a structural reason
(the pole is forced by the zeta functional equation entering through $\chi(s) = \zeta(s)/\zeta(1-s)$),
not an incidental gap in Burnol's construction.

**Cross-check against the repo's own prior measurement.** Branch A (entire, well-posed, content-
free) is consistent with, and explains, [`s4_carrier_audit.md`](s4_carrier_audit.md)'s own finding
that the CCM $D_{\log}$ carrier's function space at fixed type "is the generic trig space"
(majorant-nil, structural). If the CCM carrier's natural home is a Branch-A-type generic prolate de
Branges space, posing Carneiro-Littmann machinery there would be well-posed but would supply no new
counting content, exactly the null result already measured. This literature-side finding and the
prior experiment-side finding independently point at the same conclusion from opposite directions.

**The one unexcluded escape.** Baranov-Borichev-Havin [FETCHED, abstract, arXiv:math/0605052]
study $K_B$, model subspaces of the Hardy space $H^2$ associated to a meromorphic Blaschke product
$B$ with zeros $z_n$ (so $K_B$ consists of meromorphic functions with poles at $\bar z_n$), and
"admissible majorants" $w \ge 0$ on $\mathbb R$ for which some nonzero $f \in K_B$ satisfies $|f|
\le w$ a.e. This is a Hardy-space/model-space formulation of a one-sided bound question that is, by
construction, built for exactly the fixed-poles case Burnol's $L_a$ presents. It is not, in
anything fetched this session, connected to Burnol's Sonine-zeta construction or to any CCM-type
carrier; whether the two theories are even asking the same question (Baranov-Borichev-Havin ask for
existence of *some* admissible majorant for the whole space, not the sharp extremal one-sided
approximant of one target function the way Carneiro-Littmann do) was not established at this
search depth.

### 1.3 Verdict

**ILL-POSED**, for the named machinery (Carneiro-Littmann's Gaussian subordination and Holt-Vaaler's
originating construction), on the branch of Burnol's Sonine-space corpus that would carry the
corridor's counting-side content. The violated hypothesis: $E$ must be an entire Hermite-Biehler
function; Burnol's extended, zeta-hosting Sonine space $L_a$ requires functions with simple poles
at $s = 0$ and $s = 1$ (Burnol, arXiv:math/0203120, Proposition 2.2), which is not entire.

This is chosen over OPEN-NEEDS-EXPERT because the finding is specific and load-bearing, not a
report of absence: a named proposition in the primary source gives the exact obstruction. It is
qualified, not absolute: the *generic* branch of the same corpus (Burnol's $\mathcal E_\lambda$,
arXiv:math/0208121 Theorem 8, and the un-extended $K_a$, arXiv:math/0203120 Theorem 2.1) is
genuinely well-posed under (P1)-(P4), and one adjacent literature (Baranov-Borichev-Havin's
meromorphic model-space majorant theory) is a plausible, unexcluded escape route that a follow-up
SURVEYOR pass could check cheaply against $L_a$ specifically, this residual is carried forward
explicitly into Section 4 rather than absorbed into the headline verdict.

## 2. Question 2: does any node-tied identity exist at incommensurate nodes?

### 2.1 Sources

| Source | arXiv / DOI | Tier | What it gives |
|---|---|---|---|
| Radchenko, Viazovska, "Fourier interpolation on the real line" | arXiv:1701.00265, Publ. Math. IHES 129 (2019) 51-81 | FETCHED (exact abstract) | Interpolation at $\{0, \pm\sqrt 1, \pm\sqrt 2, \dots\}$ via weakly holomorphic modular forms for the Hecke theta group |
| Cohn, Elkies, "New upper bounds on sphere packings I" | arXiv:math/0110009, Ann. of Math. 157 (2003) 689-714 | FETCHED (abstract) | The linear-programming bound framework; conjectures sharpness in dimensions 8 and 24 |
| Viazovska, "The sphere packing problem in dimension 8" | arXiv:1603.04246, Ann. of Math. 185 (2017) 991-1015 | SECONDARY (search) | Proves the $E_8$ lattice optimal, via a modular-form-sourced magic function |
| Cohn, Kumar, Miller, Radchenko, Viazovska, "The sphere packing problem in dimension 24" | arXiv:1603.06518, Ann. of Math. 185 (2017) 1017-1033 | SECONDARY (search) | Proves the Leech lattice optimal and the unique optimal periodic packing |
| Cohn, Kumar, Miller, Radchenko, Viazovska, "Universal optimality of the $E_8$ and Leech lattices and interpolation formulas" | arXiv:1902.05438 | SECONDARY (search, not fetched in full) | Direct Fourier interpolation formulas tied to $E_8$/Leech lattice vectors |
| Ramos, Sousa, "Perturbed interpolation formulae and applications" | arXiv:2005.10337 | FETCHED (Theorem 1.4, via ar5iv) | Kadec-$1/4$-type theorem: shrinking perturbation of $\sqrt n$, rate $(1+k)^{-5/4}$ |
| Ramos, Sousa, "Perturbed Fourier uniqueness and interpolation results in higher dimensions" | arXiv:2103.12015 | FETCHED (abstract) | Extends the perturbation result to higher-dimensional spheres of radius $\sqrt n$ |
| Kulikov, Nazarov, Sodin, "Fourier uniqueness and non-uniqueness pairs" | arXiv:2306.14013 | FETCHED (Theorem 1, Corollary 2, via ar5iv) | Density-gap-only sufficient condition for a uniqueness pair, upgraded to an interpolation formula, stated independent of rational commensurability |
| Bondarenko, Radchenko, Seip, "Fourier interpolation with zeros of zeta and $L$-functions" | arXiv:2005.02996, Constr. Approx. 57 (2023) 405-461 | FETCHED (abstract) | General Dirichlet-series-kernel interpolation family; explicitly requires a functional equation |

### 2.2 Findings

**The celebrated constructions are lattice-, modular-, or functional-equation-tied, without
exception.** Radchenko-Viazovska's own abstract [FETCHED]: "We use weakly holomorphic modular
forms for the Hecke theta group to construct an explicit interpolation formula... on the set $\{0,
\pm\sqrt 1, \pm\sqrt 2, \pm\sqrt 3, \dots\}$." The node set $\sqrt n$ is not itself a lattice, but
the construction consumes the theta group's modular structure directly, and $\sqrt n$ is the
support of the theta series' own coefficients: a lattice-adjacent, arithmetic set by construction,
not a generic sequence. Cohn-Elkies's linear-programming bound [FETCHED, abstract] is realized
sharply exactly in dimensions 8 and 24 by the $E_8$ and Leech lattices (Viazovska arXiv:1603.04246;
Cohn-Kumar-Miller-Radchenko-Viazovska arXiv:1603.06518 [SECONDARY]), and the follow-up "Universal
optimality" paper (arXiv:1902.05438 [SECONDARY]) produces interpolation formulas keyed to $E_8$/
Leech lattice vector norms directly: sphere-packing-sourced interpolation is definitionally
lattice-tied. Bondarenko-Radchenko-Seip generalize the mechanism to a "large family of Fourier
interpolation bases," with interesting examples using nontrivial zeros of $\zeta$ and other
$L$-functions as nodes, but their own abstract [FETCHED] states the load-bearing requirement
directly: "kernels of general Dirichlet series with variable coefficients... admit meromorphic
continuation, with poles at a sequence dual to the sequence of frequencies of the Dirichlet series,
and they satisfy a functional equation," and the construction of concrete bases "relies on a
strengthening of Knopp's abundance principle for Dirichlet series with functional equations." Every
concrete basis in their family, including the zeta-zero one, is built from a Dirichlet series that
has a functional equation. This is the strongest rigidity-flavored statement found: not a proven
impossibility theorem (Bondarenko-Radchenko-Seip do not claim no interpolation basis can exist
without a functional equation), but a totalizing methodological fact, every known construction
method in this family consumes one.

**Ramos-Sousa's perturbation preserves the lattice-tie asymptotically; it does not escape it.**
Theorem 1.4 [FETCHED, via ar5iv]: perturbed nodes $\sqrt{k + \varepsilon_k}$ still admit a
Radchenko-Viazovska-type interpolation formula provided $\sup_{k \ge 0} |\varepsilon_k|\,(1+k)^{5/4}
< \delta$ for a fixed $\delta > 0$, i.e. $|\varepsilon_k| \le \delta\,(1+k)^{-5/4}$. This bound is
not a fixed tolerance, it must *shrink* polynomially in $k$. A perturbation that stays this close to
$\sqrt k$ for all $k$ is, by construction, asymptotically density-matched to the original lattice-
adjacent sequence: the perturbed set inherits the same counting-function asymptotics as $\sqrt n$ to
within a summable correction. This answers the falsifier's own posed sub-question directly: the
Ramos-Sousa perturbation result does **not** break the lattice-tie claim, it reinforces it, since
the only perturbations proven to preserve interpolation are ones that stay asymptotically tied to
the reference lattice-like sequence. A set like $\{k \log p\}$, whose deviation from any single
reference arithmetic progression does not shrink (primes are not asymptotically close to any fixed
lattice on the log line), is categorically outside what this theorem covers, not a large instance
of it.

**Kulikov-Nazarov-Sodin: the one genuine abstract escape, unverified against the corridor's actual
node set.** Their Theorem 1 [FETCHED, via ar5iv] gives, for a pair of sequences $(\Lambda, M)$ in a
Sobolev-type Hilbert space $\mathcal H_{s,p,q}$ ($1/p + 1/q = 1$), a purely density-based sufficient
condition: "any supercritical pair $(\Lambda, M)$ is a uniqueness pair," where supercriticality
means $\limsup_{|j| \to \infty} |\lambda_j|^{p-1}(\lambda_{j+1} - \lambda_j) < 1/2$, with the
matching subcritical condition (with $> 1/2$) giving a *non*-uniqueness pair. Corollary 2 upgrades
supercritical uniqueness to an actual interpolation formula, $f = \sum_{\lambda \in \Lambda}
f(\lambda) a_\lambda + \sum_{\mu \in M} \hat f(\mu) b_\mu$, for $f \in \mathcal H_{s,p,q}$. Per the
fetched extraction, this condition is stated to be met "independent of rational commensurateness":
it is a gap/density statement about the sequence's own asymptotic spacing, not an arithmetic
compatibility condition between $\Lambda$ and any lattice. This is a genuine, proven mechanism-class
escape from the pattern in the paragraph above: a categorical claim that "band-limited interpolation
always needs commensurate structure" would be false, because Kulikov-Nazarov-Sodin's condition is
provably sufficient without it. The paper itself flags an important caveat: the interpolating
functions $a_\lambda, b_\mu$ "depend on $s$ and... we do not know whether... convergence holds in
the topology of the Schwartz space $\mathcal S$," i.e. even a successful instance of this theorem
does not automatically hand back a clean Schwartz-space or Paley-Wiener-type identity, the setting
the corridor's Beurling-Selberg-style machinery lives in.

**Growth-rate check against $\{k \log p\}$ (this survey's own estimate, unsourced, not read from
any paper).** Whether Kulikov-Nazarov-Sodin's condition is even the right tool to point at the
corridor's node set is a separate question from whether the condition is met. Take $\Lambda$ to be
$\{\log p : p \text{ prime}\}$ (or, equivalently at leading order, $\{\log n : n \text{ a prime
power}\}$, since higher prime powers are $O(\sqrt X)$ against $\pi(X) \sim X/\log X$), sorted
increasingly as $\lambda_1 < \lambda_2 < \dots$. By the prime number theorem, the counting function
on the log scale is $N(x) = \#\{j : \lambda_j \le x\} = \pi(e^x) \sim e^x / x$. Inverting,
$\lambda_j \sim \log j$: the sequence grows only logarithmically in its own index, far slower than
any fixed polynomial rate $j^{1/p}$ ($p > 1$). Consecutive gaps scale as $\lambda_{j+1} - \lambda_j
\sim 1/N'(\lambda_j) \sim \lambda_j e^{-\lambda_j} \sim (\log j)/j \to 0$. Plugging into the
supercritical quantity for any fixed $p$: $|\lambda_j|^{p-1}(\lambda_{j+1}-\lambda_j) \sim (\log
j)^{p-1} \cdot (\log j)/j = (\log j)^p / j \to 0$, trivially below the $1/2$ threshold. This looks,
naively, like an easy pass, but the polynomial-growth regime $\lambda_j \sim j^{1/p}$ is exactly
what ties Kulikov-Nazarov-Sodin's (and Radchenko-Viazovska's $\sqrt n$, $p=2$) construction to a
specific, non-degenerate function space $\mathcal H_{s,p,q}$ in the first place; a sequence growing
only like $\log j$ is far sparser, in the classical Beurling-density sense relevant to bandlimited
sampling, than the polynomial rate the space's own definition (not extracted in this pass) is
presumably calibrated to. The trivial pass of the numerical inequality is likely a symptom of the
theorem's intended regime not matching this node set's shape, not evidence the theorem's conclusion
(a genuine interpolation formula) actually applies. This is flagged as an open technical question,
not resolved either way here: confirming or excluding applicability needs the precise definition of
$\mathcal H_{s,p,q}$ and is BUILDER/VERIFIER-depth work, not a SURVEYOR-tier closure.

### 2.3 Verdict

**MIXED.** Every explicit, named-author construction found (Radchenko-Viazovska; Cohn-Elkies
realized by Viazovska/CKMRV; Bondarenko-Radchenko-Seip) consumes lattice, modular, or
functional-equation structure, and the strongest rigidity-flavored statement is
Bondarenko-Radchenko-Seip's own account of their method: every concrete basis in their general
family, including the zeta-zero one, is built from a Dirichlet series kernel that "satisf[ies] a
functional equation." The one perturbation result in print (Ramos-Sousa, Theorem 1.4) requires the
perturbation to shrink like $(1+k)^{-5/4}$, which preserves rather than breaks the asymptotic
lattice-tie. Against this, Kulikov-Nazarov-Sodin (Theorem 1, Corollary 2) proves a genuinely
commensurability-free, density-only sufficient condition for a full uniqueness-and-interpolation
pair, a real ESCAPE-EXISTS-shaped citation, but its concrete fit to $\{k \log p\}$ is unverified,
and this survey's own growth-rate check (Section 2.2, last paragraph) raises a specific, unresolved
doubt about whether the theorem's intended regime even covers a sequence this slow-growing.

## 3. Where the two questions interact

Carneiro-Littmann's own machinery is itself interpolation-based: their abstract for
arXiv:1406.5456 [FETCHED] states they "develop new interpolation tools to solve an associated
extremal problem," and the classical Beurling-Selberg construction generally builds a majorant by
interpolating the target function at a specific discrete node set (the zeros of the companion
function $B$), forcing the majorant-minus-target sign by the interpolation structure itself. For
the homogeneous, well-posed branch (Section 1.2's Branch A, $E_\nu$ built from Bessel functions
$J_\nu$), that node set is the sequence of Bessel zeros $j_{\nu,k}$, which are asymptotically
equally spaced ($j_{\nu,k} = k\pi + O(1)$ as $k \to \infty$, the standard McMahon-expansion fact
[UNVERIFIED-MEMORY, standard special-function asymptotic, not fetched this session]), i.e.
asymptotically lattice-like in exactly the sense Section 2's constructions need. So the one branch
of Question 1's machinery that is genuinely well-posed interpolates at a node set that is itself
asymptotically regular, the same structural requirement Question 2 finds governing every working
interpolation identity. Both mechanism classes, from opposite directions (a one-sided majorant
theory and a two-sided interpolation-formula theory), agree on the same diagnosis: constructions
that work sample at asymptotically regular, density-matched node sets, and the corridor's own
target set, $\{\log p\}$ or $\{k \log p\}$, with gaps shrinking like $(\log j)/j \to 0$ rather than
staying asymptotically constant or lattice-matched, is not of this shape by either theory's own
internal logic. This is independent corroboration, not a shared citation: Section 1's finding comes
from the de Branges/Hermite-Biehler axiom structure, Section 2's from the Fourier-uniqueness-pair
literature, and they land on the same structural requirement without either literature citing the
other.

## 4. Consequence for the Sonin-projector round

The frame audit's pre-registered exit rule ([`ccm_corridor_frame_audit.md`](ccm_corridor_frame_audit.md)
Section 4): "if the Sonin projector lands blind, OR the extremal problem is ill-posed in the Sonin
space, the corridor closes as a proof home." Falsifier 2's own statement of the check
([`ccm_corridor_frame_audit.md`](ccm_corridor_frame_audit.md) Section 3, item 2): "If the Sonine/de
Branges chain lacks the structure the one-sided extremal theory needs, the corridor's question is a
category error, not an open problem."

**Falsifier 2 trips.** Section 1's finding is precisely this category error, named with a
proposition number: the one Sonine space in Burnol's corpus that would carry the corridor's
counting-side content, the extended space $L_a$ hosting the zeta zeros, requires poles that put it
outside the entire-Hermite-Biehler axiom the named machinery (Carneiro-Littmann, Holt-Vaaler) is
built on. This is not an absence-at-search-depth finding like the two already-banked in
[`s4_carrier_audit.md`](s4_carrier_audit.md) Section 2 ("no literature collision found"); it is a
structural incompatibility with a named cause. Per the exit rule's own literal wording, this is
sufficient to fire it.

**What this changes about the pre-registered round.** The round as scoped
([`ccm_corridor_frame_audit.md`](ccm_corridor_frame_audit.md) Section 4) was to run falsifiers 1 and
2 together, "the Sonin-projector probe with a Beurling twin, and the Carneiro-Littmann
well-posedness check," with 3 and 4 riding along cheaply. This survey completes falsifier 2 (and 4)
*before* any new code is written, which was exactly the point of sequencing them as the cheap gate.
The most valuable thing the expensive half of the round (building a new Sonin-projector eigenbasis
and testing whether the one-sided extremal problem can even be posed on it) would have established
is now already answered in the negative for the content-bearing branch, and answered as
already-known-empty for the content-free branch (Section 1.2's cross-check against the existing
"generic trig space" measurement). Building the projector to re-ask "is the one-sided extremal
problem well-posed here" would be re-deriving Section 1's literature-side answer at BUILDER cost
instead of SURVEYOR cost.

**Recommendation.** Do not run the Sonin-projector eigenbasis build as originally scoped for the
well-posedness question. Falsifiers 1 and 3 (rank behavior at $\{k \log p\}$ against a Beurling
twin; generic-carrier replication) remain independently informative as *measurement* moves, since
they test rank collapse rather than well-posedness, but their premise should be updated: they would
be testing the branch this survey now shows was already expected to be content-free by the
literature, not an open question. This lowers, but does not zero out, their marginal value; if run
at all, run them as bounded confirmation, not as the load-bearing test the round was originally
built around. Question 2's MIXED verdict does not on its own trip an exit rule (falsifier 4 has no
pre-registered binary trigger), but it reinforces, from an independent literature line, the
corridor's own already-declared pivot target: the lattice/theta side
([`ccm_corridor_frame_audit.md`](ccm_corridor_frame_audit.md) Section 4: "the lattice side the
corridor's own results keep pointing at"; [`missing_object_interface.md`](missing_object_interface.md)
Section 2's counting joint C1 = SP2 AND SP3). Both falsifiers point the same direction as the
portfolio argument already in Section 5 of the frame audit: reclassify the corridor as the project's
measurement instrument and discipline-sharpener, and redirect BUILDER budget at the pivot target,
now with a specific literature-sourced reason (Section 1 of this survey) added to the timing/
portfolio reason already on record.

**Two cheap residuals named for whoever picks this up next**, in the same spirit as the corridor's
own practice of naming escape conditions rather than treating a closure as unconditional:

1. Check Baranov-Borichev-Havin's meromorphic model-space majorant theory (arXiv:math/0605052, and
   its citing literature) directly against Burnol's $L_a$: is $L_a$'s pole structure literally a
   $K_B$ for some meromorphic Blaschke product $B$ with zeros at $0, 1$, and if so, does an
   admissible-majorant theorem there answer the same extremal question Carneiro-Littmann ask for
   entire $E$? Unresolved at this search depth.
2. Pin the precise definition of Kulikov-Nazarov-Sodin's $\mathcal H_{s,p,q}$ space and check
   whether $\{\log p\}$'s actual growth rate ($\lambda_j \sim \log j$, Section 2.2) places it inside
   or outside the theorem's intended scope, resolving the doubt this survey raises but does not
   settle.
