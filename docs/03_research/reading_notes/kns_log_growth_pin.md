# Reading note: pinning Kulikov-Nazarov-Sodin against the corridor's actual node sets

> SURVEYOR reading note, 2026-07-17. Executes TODO.md's pivot rung (ii) ("pin the
> Kulikov-Nazarov-Sodin space definition against the actual growth $\lambda_j \sim \log j$ of
> $\{k \log p\}$"), the second of the two named **#164 reopen conditions**
> ([`s4_cheap_falsifiers_survey.md`](../s4_cheap_falsifiers_survey.md) Section 4, "Two cheap
> residuals named for whoever picks this up next," item 2). LEARNINGS #164 flagged
> Kulikov-Nazarov-Sodin (KNS), arXiv:2306.14013, as "the ONE possible mechanism-class escape
> from the lattice-tie diagnosis," with an unverified fit to the corridor's node set and a
> survey-internal growth check suggesting mismatch. This note pins it at source.

## STATUS

- **Date:** 2026-07-17.
- **Verdict: FITS-IN-PART.** KNS's raw density hypothesis (Definition 2, "supercritical pair")
  is genuinely SATISFIED by the full prime-power log set $\{k \log p\}$ (node set (b) below),
  confirming, not just leaving open, the survey's original doubt in the opposite direction than
  expected: the set is not borderline, it is trivially/deeply supercritical for every admissible
  exponent. But the single-prime lattice (node set (a)) is DEEPLY SUBCRITICAL, landing on the
  wrong (non-uniqueness) side of KNS's own dichotomy, for every admissible exponent and every
  prime. And even the (b)-side "fits" carries **zero S4 content**: what KNS proves there is a
  full-rank Fourier **frame** (a system with no near-kernel), which is the structural opposite of
  the rank-deficient, cost-$o(M)$ collapse the S4 spec actually needs.
- **Consequence for the #164 reopen condition:** DISCHARGED. No genuine mechanism-class escape
  materializes. Combined with falsifier 2's ILL-POSED verdict
  ([`s4_cheap_falsifiers_survey.md`](../s4_cheap_falsifiers_survey.md) Section 1.3), only reopen
  condition (i) (Baranov-Borichev-Havin vs. Burnol's $L_a$) remains open from that survey's
  Section 4.
- **Consequence for the theta-side S4 attempt:** REINFORCED. This note adds a third, independently
  computed reason (after the ill-posedness finding and the lattice-tie diagnosis) to expect no
  density-only escape from the counting side, sharpening the corridor's already-declared pivot
  toward the theta/modular-interpolation side and the C1 = SP2-and-SP3 counting joint
  (TODO.md, "THE POST-CORRIDOR PIVOT").

**Notation warning.** KNS's own Hölder-dual exponents are named $p, q$ in their paper, which
collides with "the prime $p$" central to the corridor's node sets. Throughout this note, KNS's
exponents are renamed $p_0, q_0 \in (1,\infty)$, $1/p_0+1/q_0=1$; the letter $p$ is reserved for
an arithmetic prime.

## 1. KNS 2306.14013 at source

### 1.1 Sources

| Source | Tier | What it gives |
|---|---|---|
| Kulikov, Nazarov, Sodin, "Fourier uniqueness and non-uniqueness pairs," arXiv:2306.14013 | FETCHED (ar5iv, three targeted extraction passes) | Definition of $\mathcal H_{s,p_0,q_0}$; Definition 2 (super/subcritical pair); Theorem 1 (uniqueness/non-uniqueness dichotomy); Theorem 2 (quantitative frame bound); Claim 1 (separation reduction); Corollary 2 (interpolation formula); Section 2.4 Related Work (Bondarenko-Radchenko-Seip citation) |
| Bondarenko, Radchenko, Seip, "Fourier interpolation with zeros of zeta and $L$-functions," arXiv:2005.02996 | SECONDARY (via KNS's own citing description, cross-checked against [`s4_cheap_falsifiers_survey.md`](../s4_cheap_falsifiers_survey.md) Section 2.1, itself FETCHED there) | The $\Lambda=\{(4\pi)^{-1}\log n\}$, $M=\{i(\rho-1/2)\}$ (zeta zeros) pairing, built from a Dirichlet-series functional equation |
| [Author(s) unconfirmed this session], "Critical and asymmetric Fourier uniqueness pairs," arXiv:2509.17600 | FETCHED (ar5iv, one extraction pass) | 2025 follow-up explicitly motivated by KNS; still two-sided-$\mathbb Z$-indexed; Remark 3 on zeta-zero spacing |
| [Author(s) unconfirmed this session], "The basis functions of Fourier Interpolation," arXiv:2512.18677 | FETCHED (abstract, one extraction pass) | Shows the Radchenko-Viazovska basis functions themselves fail to be a Riesz basis in KNS's own Hilbert space |
| WebSearch, "Kulikov Nazarov Sodin ... citing prime numbers arithmetic sequence" | FETCHED (search result list) | Citation-graph scan for arithmetic node-set treatment among citing papers |

**Fidelity caveat**, same practice as the repo's other reading notes (e.g.
[`ccm_zeta_cycle_density_gate.md`](ccm_zeta_cycle_density_gate.md)): all KNS extractions this
session are LLM summarizations of the ar5iv HTML render, not a line-by-line LaTeX read by hand.
Theorem/definition numbers and the quoted sentences are high-confidence (cross-checked across
three independent fetch passes that agree with each other) but not independently verified
character-by-character against the source. Where two passes disagreed (Theorem 1(ii)'s function
space; see Section 1.3), both readings are reported rather than silently resolved.

### 1.2 The apparatus, exactly as extracted

**Function space (Definition 3).** For $1 < p_0, q_0 < \infty$ with $1/p_0+1/q_0=1$, and $s>0$:
$$\mathcal H_{s,p_0,q_0} = \{f : f \in H_{q_0 s},\ \hat f \in H_{p_0 s}\},\qquad \|f\|^2_{\mathcal H_{s,p_0,q_0}} = \|f\|^2_{H_{p_0 s}} + \|\hat f\|^2_{H_{q_0 s}},$$
where $\|f\|^2_{H_t} = \int_{\mathbb R}(1+|\xi|^{2t})|\hat f(\xi)|^2\,d\xi$. An extra constraint,
$s\min(p_0,q_0)\ge 1$, is imposed wherever $\mathcal H_{s,p_0,q_0}$ itself is the ambient space
(Theorem 2, Corollary 2); Theorem 1's own conclusion is stated for the Schwartz space $\mathcal
S$ directly, not for $\mathcal H_{s,p_0,q_0}$.

**Definition 2 (supercritical / subcritical pair).** Sequences $\Lambda=(\lambda_j)_{j\in\mathbb
Z}$, $M=(\mu_j)_{j\in\mathbb Z}$ must be **two-sided**: strictly increasing,
$\lim_{j\to\pm\infty}\lambda_j=\pm\infty$ (and likewise for $M$). A pair $(\Lambda,M)$ is
**supercritical** if
$$\limsup_{|j|\to\infty}|\lambda_j|^{p_0-1}(\lambda_{j+1}-\lambda_j) < \tfrac12, \qquad \limsup_{|j|\to\infty}|\mu_j|^{q_0-1}(\mu_{j+1}-\mu_j) < \tfrac12,$$
**subcritical** if the same two quantities have $\liminf > 1/2$ instead.

**Theorem 1.** "Suppose that $1<p_0,q_0<\infty$, $1/p_0+1/q_0=1$. Then (i) any supercritical
pair $(\Lambda,M)$ is a uniqueness pair for the Schwartz space $\mathcal S$; (ii) any subcritical
pair $(\Lambda,M)$ is a non-uniqueness pair for the Schwartz space $\mathcal S$."

**Theorem 2 (quantitative, needs separated pairs).** For separated supercritical pairs, there
exist $c,C>0$ with
$$c\|f\|^2_{\mathcal H_{s,p_0,q_0}} \le \sum_{\lambda\in\Lambda}(1+|\lambda|)^{(2s-1)p_0+1}|f(\lambda)|^2 + \sum_{\mu\in M}(1+|\mu|)^{(2s-1)q_0+1}|\hat f(\mu)|^2 \le C\|f\|^2_{\mathcal H_{s,p_0,q_0}}.$$
This is a two-sided **frame bound**: both a ceiling and a floor on the evaluation map's norm,
i.e. a statement that the map is bounded *below* (no near-kernel), not merely bounded above.

**Corollary 2 (interpolation formula).** For a supercritical pair with $s\min(p_0,q_0)\ge1$,
there exist $(a_\lambda)_{\lambda\in\Lambda}$, $(b_\mu)_{\mu\in M}$ in $\mathcal H_{s,p_0,q_0}$
such that for every $f\in\mathcal H_{s,p_0,q_0}$,
$$f = \sum_{\lambda\in\Lambda} f(\lambda)\,a_\lambda + \sum_{\mu\in M} \hat f(\mu)\,b_\mu,$$
convergent in $\mathcal H_{s,p_0,q_0}$, with $\|a_\lambda\| \le C(1+|\lambda|)^{(s-1/2)p_0+1/2}$
(similarly for $b_\mu$). **One interpolating function per point of $\Lambda$ (and per point of
$M$)**: the formula's index set is the full, unthinned $\Lambda$, and no smaller subset of
$\Lambda$ is claimed sufficient by this statement.

**Claim 1 (the separation reduction, proof-internal).** "For any supercritical pair
$(\Lambda,M)$, there exists a supercritical pair $(\Lambda',M')$ such that $\Lambda'\subset
\Lambda$, $M'\subset M$, and $\Lambda'$ is $p_0$-separated while $M'$ is $q_0$-separated," where
$p_0$-separated means $\lambda_{j+1}-\lambda_j \ge c(1+\min(|\lambda_j|,|\lambda_{j+1}|))^{1-p_0}$.
This is a **sufficiency reduction used inside the proofs** of Theorem 2 and Corollary 2 (monotone:
vanishing on a subset is a weaker constraint, so uniqueness for the thinned pair implies
uniqueness for the full pair). **Neither Theorem 1 nor Corollary 2 states separation as an
explicit hypothesis of its own conclusion**; only Theorem 2's stated hypothesis names "separated"
directly. This matters below (Section 4): the corridor's actual node sets are *not*
$p_0$-separated in this technical sense, but that does not by itself block Theorem 1(i)/Corollary
2, because the reduction is designed to route around exactly that.

**Non-uniqueness (subcritical) side.** Two extraction passes gave slightly different framings of
Theorem 1(ii)'s target space: one returned "non-uniqueness pair for the Schwartz space
$\mathcal S$" verbatim as the theorem statement; the other, on a more targeted follow-up pass,
confirmed the theorem literally reads "for the Schwartz space $\mathcal S$" but that the
surrounding text immediately strengthens it: "the non-uniqueness part of Theorem 1 requires less
stringent assumptions on the pair $(\Lambda,M)$ and holds for a much smaller Gelfand-Shilov space
$\mathcal S(p_0,q_0)$." Both readings are consistent (a counterexample in the smaller
Gelfand-Shilov space is automatically one in the larger Schwartz space), so this does not affect
anything below; it is recorded as a residual because it was not independently re-verified
character-for-character. **No explicit closed-form counterexample function is exhibited** in the
extracted material; the construction is via complex-analytic / entire-function methods (the
paper's Section 7), an existence argument, not a formula.

### 1.3 Related work: does KNS itself touch an arithmetic node set?

Yes, once, in Related Work (Section 2.4), and explicitly **not** as an instance of its own
mechanism:

> "Bondarenko, Radchenko and Seip revealed a collection of similar interpolation formulas, the
> most curious one corresponding to $\Lambda=\{(4\pi)^{-1}\log n : n\in\mathbb N\}$ and
> $M=\{i(\rho-1/2)\}$, where $\rho$ runs through all non-trivial zeroes of the Riemann zeta
> function with positive imaginary part (assuming the Riemann hypothesis and simplicity of
> zeroes). Similarly to [19], they used an arithmetic approach based on the theory of modular
> forms and Dirichlet series."

This is presented as a *different, contrasting* method (functional-equation-consuming, per
[`s4_cheap_falsifiers_survey.md`](../s4_cheap_falsifiers_survey.md) Section 2.2's own reading of
Bondarenko-Radchenko-Seip's abstract), not as a special case KNS's density-only theorem is claimed
to reach. **No paper in this search treats primes or prime powers specifically** ($\log n$ over
all $n\in\mathbb N$ is a different, denser set than $\log p$ over primes only or $\{k\log p\}$
over prime powers; see Section 3 below for how close these actually are asymptotically).

> Adjudicated 2026-08-09 (ADVERSARY, [`_modular_rung_adversary.md`](_modular_rung_adversary.md)
> B1): BRS 2005.02996 Theorem 1.1 is unconditional with multiplicities $m(\rho)$ handled by
> derivative terms, per direct source fetch; the "assuming RH and simplicity" wording is KNS's
> citing description and does not match the printed theorem. This pin's quote of KNS is
> accurate; KNS's characterization of BRS is not.

## 2. The corridor's node sets, defined precisely, with the counting-function arithmetic

Three distinct objects are in play; conflating them is the main risk in this whole question, so
they are kept separate throughout.

### 2.1 Node set (a): the single-prime lattice

Fix a prime $p$. Define $\Lambda_p = \{k\log p : k\in\mathbb Z\}$, indexed naturally by
$k\in\mathbb Z$ (already two-sided, matching KNS's convention with no symmetrization needed):
$\lambda_k = k\log p$. This is an **exact arithmetic progression**, spacing $\log p$, not merely
asymptotic:
$$\lambda_{k+1}-\lambda_k = \log p \quad \text{for every } k \text{ (constant, exact)}.$$

### 2.2 Node set (b): the full prime-power log set

$$\Lambda^* = \{k\log p : p \text{ prime}, k\ge 1\} = \{\log n : n = p^k,\ p \text{ prime},\ k\ge1\},$$
sorted increasingly. As literally defined this is **one-sided** ($\log n > 0$ for all $n\ge2$);
symmetrizing to fit KNS's two-sided convention means setting $\lambda_{-j} := -\lambda_j$ for
$j>0$, a choice not part of the corridor's own definition of the set, though a standard move in
this literature (Radchenko-Viazovska symmetrize $\sqrt n$ the same way, to $\{0,\pm\sqrt n\}$).

**Counting function** (this note's own derivation). For $T>0$:
$$N(T) := \#\{n=p^k \le e^T\} = \sum_{k\ge1}\pi(e^{T/k}).$$
The $k=1$ term is $\pi(e^T)$. The $k\ge2$ terms are dominated by $k=2$: $\pi(e^{T/2}) =
O(e^{T/2}/T)$, and higher $k$ contribute even less. By the prime number theorem $\pi(x)\sim
x/\log x$, so
$$N(T) = \pi(e^T) + O(e^{T/2}) \sim \frac{e^T}{T} \qquad (T\to\infty).$$
This matches [`s4_cheap_falsifiers_survey.md`](../s4_cheap_falsifiers_survey.md) Section 2.2's
stated counting function exactly, independently re-derived here.

### 2.3 The e1o instrument's actual node sets (not the same objects)

Reading [`e1o_s4_carrier.md`](../../../experiments/spectral/e1o_s4_carrier.md) Section "Q3: the
carrier delta" (item (c), the multiplicity heart) precisely, the CCM-carrier probe actually tests
**three** different, more restrictive objects, none of which is the raw infinite-line $\Lambda_p$
or $\Lambda^*$ above:

1. **"log-prime comb $\{\log p : p \le \lambda^2\}$"**: primes only ($k=1$), truncated to a
   FINITE window by the carrier's horizon $\lambda^2$, and evaluated against DECIMATED
   finite-dimensional subspaces $V_K$ of the carrier's own trig space (dimension budget $\le
   4\lambda^2$). Measured: cost ratio $1.000$ (full price, no collapse) at every tested
   $(\lambda, K)$ cell.
2. **AP comb at "kernel spacing"**: a genuine arithmetic progression of spacing $L/K$, matched to
   the decimation period. Measured: cost ratio down to $1/K$ (cheap collapse).
3. **"Per-prime circle"**: the orbit $\{k\log p\}$ reduced onto the **compact circle**
   $\mathbb R/(\log p)\mathbb Z$, i.e. a quotient/periodic structure, not the raw line. Measured:
   cost ratio $0.20$ (cheap).

The S4 spec itself
([`e1o_s4_carrier.md`](../../../experiments/spectral/e1o_s4_carrier.md) Q4, item 2, "CHEAP
MULTIPLICITY") is phrased generically over "$\{k\log p\}$" (i.e. node set (b)'s shape), but asks
for a **lambda-uniform rank collapse of a fixed-dimension ($\le4\lambda^2$) evaluation matrix**,
which is a finite-dimensional linear-algebra object. This is a structurally different question
from a Fourier-transform uniqueness pair on the infinite real line (Section 5 returns to this).

## 3. Reconciling the two growth-rate readings

The task is to state, unambiguously, both ways of describing $\Lambda^*$'s size, since KNS's
Definition 2 is phrased in the "index" convention ($\lambda_j$ as a function of $j$) while the
natural arithmetic statement (prime number theorem) is phrased in the "height" convention
($N(T)$ as a function of $T$).

**Reading 1 (height/density).** $N(T) \sim e^T/T$: **exponential** growth in $T$. Below any
height $T$, the node count multiplies by $\approx e$ per unit increase in $T$ (up to the slowly
varying $1/T$ correction). The nodes become dense at an exponential rate as $T\to\infty$.

**Reading 2 (index).** Invert $N(\lambda_j)=j$. Using the standard PNT corollary for the $j$-th
prime, $p_j \sim j\log j$ (prime powers with $k\ge2$ do not affect this to leading order), and
$\lambda_j = \log p_j$ (dropping the negligible $k\ge2$ correction):
$$\lambda_j = \log p_j \sim \log(j\log j) = \log j + \log\log j \sim \log j \qquad (j\to\infty).$$

**These are the same fact, viewed two ways**, exactly as the task requires making explicit: $N$
and $j\mapsto\lambda_j$ are (to leading order) mutual inverse functions, so "$N$ grows
exponentially fast in $T$" and "$\lambda_j$ grows logarithmically slowly in $j$" are automatically
equivalent statements about the same object (a fast forward map has a slow inverse map; this is a
general fact about inverse functions, not special to primes). This confirms
[`s4_cheap_falsifiers_survey.md`](../s4_cheap_falsifiers_survey.md) Section 2.2's "$\lambda_j \sim
\log j$" reading is the correct inversion of its own "$N(x)\sim e^x/x$" computation.

**A small arithmetic refinement to the survey's gap estimate (does not change the conclusion).**
The survey states "$\lambda_{j+1}-\lambda_j \sim 1/N'(\lambda_j) \sim \lambda_j e^{-\lambda_j}
\sim (\log j)/j$." Redoing this using the *exact* relation $e^{\lambda_j}=p_j$ (rather than the
looser approximation $e^{\lambda_j}\sim j$) and $p_j\sim j\log j$:
$$\lambda_{j+1}-\lambda_j \;\sim\; \frac{\lambda_j}{e^{\lambda_j}} \;=\; \frac{\log p_j}{p_j} \;\sim\; \frac{\log j}{j\log j} \;=\; \frac1j,$$
i.e. this note's route gives average gap $\sim 1/j$, one factor of $\log j$ smaller than the
survey's $(\log j)/j$. This is traceable exactly to whether $e^{\lambda_j}$ is approximated as
$\sim j$ or (more precisely) as $\sim j\log j = j\lambda_j$ before taking the reciprocal; both are
legitimate leading-order statements depending on how many terms of the asymptotic expansion are
kept, and **the discrepancy does not matter for the verdict** (Section 4): both $1/j$ and $(\log
j)/j$ decay polynomially in $j$, both are annihilated by any fixed power of $\log j$ multiplying
them. Individual-gap fluctuation (twin primes give occasional tiny gaps; the largest
unconditionally known prime gaps are $O(p_j^{1-\delta})$ for some fixed small $\delta>0$, a
classical fact after Hoheisel 1930 [UNVERIFIED-MEMORY for the modern best exponent, not needed
here]) does not change this either: even the worst unconditionally known individual gap gives
$\lambda_{j+1}-\lambda_j = O(p_j^{-\delta})$, still a fixed negative power of $j$, still beaten by
any $(\log j)^{p_0-1}$ prefactor.

## 4. Running KNS's hypothesis against the corridor's sets

**The unifying lens (this note's own derivation, elementary asymptotic calculus).** If
$\lambda_j$ is regularly varying of index $\alpha \ge 0$ (i.e. $\lambda_j \sim Cj^\alpha$), then
gap $\lambda_{j+1}-\lambda_j \sim C\alpha j^{\alpha-1}$, so
$$Q_{p_0}(j) := |\lambda_j|^{p_0-1}(\lambda_{j+1}-\lambda_j) \sim C^{p_0}\alpha\, j^{\alpha p_0 - 1}.$$
This $\to 0$ (supercritical) iff $\alpha < 1/p_0$; $\to\infty$ (subcritical) iff $\alpha>1/p_0$;
stays order-1 (the genuinely critical regime) iff $\alpha = 1/p_0$ exactly, which is precisely
KNS's own example family $\lambda_j \sim j^{1/p_0}$ (Section 1.2's extracted "general asymptotic
form"). This single computation explains both verdicts below.

### 4.1 Node set (a): FAILS, in the wrong direction

$\Lambda_p$ is an exact lattice: regular variation index $\alpha=1$ (exactly, not just
asymptotically). Since $1 > 1/p_0$ for **every** $p_0\in(1,\infty)$ (as $1/p_0<1$ always),
$\Lambda_p$ is subcritical for every admissible exponent. Directly:
$$Q_{p_0}(k) = (|k|\log p)^{p_0-1}\log p = (\log p)^{p_0}\,|k|^{p_0-1} \xrightarrow{|k|\to\infty} +\infty \quad \text{for every } p_0\in(1,\infty),\ \text{every prime } p.$$
Not a marginal failure of the $1/2$ threshold: the quantity diverges. If paired with any $M$ that
is *also* subcritical for the dual $q_0$ (which by the same lens includes $M=\Lambda_p$ itself,
any other lattice, or indeed anything growing at most linearly), **Theorem 1(ii) fires: $(\Lambda_p, M)$ is a non-uniqueness pair.** The corridor's single-prime lattice, tested directly against
KNS's own criterion, lands squarely on the escape theorem's *failure* side. (This is consistent
with, and a fresh independent confirmation of, the classical fact that a lattice paired with its
own dual is not in general a Fourier-Schwartz uniqueness pair without extra structure beyond bare
density, the same phenomenon the Heisenberg-uniqueness-pair literature for the hyperbola
addresses by other means.)

### 4.2 Node set (b): the hypothesis genuinely holds

$\Lambda^*$ has $\lambda_j \sim \log j$: slower than $j^\alpha$ for *every* $\alpha>0$ (a slowly
varying sequence, "$\alpha=0$" in the lens above). Since $0 < 1/p_0$ for every finite
$p_0\in(1,\infty)$, $\Lambda^*$ is supercritical for **every** admissible exponent, and not
marginally: $Q_{p_0}(j) \sim (\log j)^{p_0-1}/j \to 0$ (using either this note's $1/j$ gap or the
survey's $(\log j)/j$ gap, Section 3). This **confirms and sharpens**
[`s4_cheap_falsifiers_survey.md`](../s4_cheap_falsifiers_survey.md) Section 2.2's flagged doubt:
the growth-rate check is not an inconclusive numerical curiosity, it is a rigorous demonstration
that $\Lambda^*$ sits deep inside supercritical territory, arbitrarily far from the $1/2$
threshold, for every choice of exponent. Self-paired ($M=\Lambda^*$, by the same computation via
symmetry) or paired with any comparably dense partner, **Theorem 1(i) genuinely fires**: this is
a real, literal instance of a KNS uniqueness pair, and Corollary 2's interpolation formula applies
too (any $s \ge \max(1/p_0,1/q_0)$ satisfies $s\min(p_0,q_0)\ge1$).

**Cross-check (this note's own derivation): why the zeta zeros specifically do not work as a
partner.** If instead one tries the Bondarenko-Radchenko-Seip-style pairing ($M=$ imaginary parts
of nontrivial zeta zeros), the Riemann-von Mangoldt counting law $N(T)\sim(T/2\pi)\log(T/2\pi)$
inverts to $\mu_j \sim 2\pi j/\log j$: regular variation index $\to 1^-$ (almost linear), strictly
above $1/q_0$ for every finite $q_0\in(1,\infty)$. Directly, $Q_{q_0}(j) \sim j^{q_0-1}/(\log
j)^{q_0} \to \infty$: the zeta-zero sequence is **subcritical**, for every admissible exponent,
by the same lens as the lattice case. So pairing $\Lambda^*$ against the zeta zeros fails
Theorem 1(i)'s hypothesis on the $M$-side, regardless of $\Lambda^*$'s own supercriticality. This
independently reproduces, by direct computation, exactly what the 2025 follow-up paper states in
words (Section 6 below): "the spacing behavior of zeta zeros does not satisfy the paper's
sufficient conditions." Two unrelated routes (this note's arithmetic; a 2025 paper's own stated
remark) land on the same fact.

## 5. S4 content, even in the best case

This is the sharpest part of the verdict, and holds *even granting* Section 4.2's positive
finding at face value.

**A uniqueness pair, let alone a frame, is a full-rank statement.** Theorem 2's conclusion is a
**two-sided** bound: $c\|f\|^2 \le \sum(\ldots) \le C\|f\|^2$. The lower bound $c\|f\|^2 \le
\sum(\ldots)$ says the evaluation map $f \mapsto (f(\lambda))_\lambda, (\hat f(\mu))_\mu$ is
bounded *below*: injective, with no near-kernel, no small singular values. This is, by
definition, a **frame** condition, and a frame is the *opposite* structure from a rank collapse.
Corollary 2 makes the same point concretely: it hands back **one interpolating function $a_\lambda$
per point of $\Lambda$**, with no claim that any proper subset of $\Lambda$ would already
suffice. Full price, not cheap multiplicity.

**The S4 spec wants exactly the opposite.**
[`s4_carrier_audit.md`](../s4_carrier_audit.md) Section 4 item 5 and
[`e1o_s4_carrier.md`](../../../experiments/spectral/e1o_s4_carrier.md) Q4 item 2 define "CHEAP
MULTIPLICITY" as: vanishing/interpolation conditions of total order $M$ costing only $o(M)$
**dimensions**, in a FIXED finite budget ($\le 4\lambda^2$), lambda-uniformly. That is a
**rank-deficient** (collapsing) evaluation map, the precise negation of a frame's lower bound. The
e1o probe's own numbers make this concrete: a genuine collapse (AP comb, per-prime circle) shows
up as cost ratio $\ll 1$; the log-prime comb shows cost ratio exactly $1.000$ (full rank,
i.e. frame-like, not collapse-like) at every tested cell. **A KNS uniqueness/frame result, even
where its hypothesis is met, is a source-level explanation of *why* the corridor already measures
full price, not a route to the collapse it wants.**

**Grading against the S4 spec's four conditions**
([`e1o_s4_carrier.md`](../../../experiments/spectral/e1o_s4_carrier.md) Q4), even in the
best-case (b)-side reading:

1. **ONE-SIDEDNESS** (a device $F_\lambda \ge \chi_{[0,L]}$ on a fixed finite window): KNS builds
   no such device; its objects are infinite-tail interpolating functions on the whole line, not a
   one-sided bound at a finite type. Not supplied.
2. **CHEAP MULTIPLICITY**: actively the opposite, as argued above. Not supplied; ruled out in
   this direction.
3. **UNIFORMITY in $\lambda$**: not applicable. KNS has no analogue of the carrier's family
   parameter $\lambda$; its asymptotics are all in the sequence index $j\to\pm\infty$ at one fixed
   pair $(\Lambda,M)$, not a family of finite-window problems indexed by a growing cutoff. Not
   supplied.
4. **LATTICE CLAUSE** (the mechanism must nameably consume the additive lattice / functional
   equation): KNS's mechanism is explicitly **density-only**, and per
   [`s4_cheap_falsifiers_survey.md`](../s4_cheap_falsifiers_survey.md) Section 2.2, its entire
   distinguishing feature (the reason it was flagged as a possible escape at all) is being
   "independent of rational commensurability." That is definitionally the opposite of consuming a
   lattice. Not supplied, by the mechanism's own advertised design.

**Cross-reference to the repo's own DMV-kill discipline**
([`s4_carrier_audit.md`](../s4_carrier_audit.md) Section 3). The repo has already proven,
independently of this note, that *any* mechanism whose inputs are density-only (no lattice, no
functional equation, no sub-square-root density irregularity) is provably incapable of any
exponent gain below error-exponent 1: the Diamond-Montgomery-Vorhauer / Broucke-Vindas fake
system possesses every density-only input a mechanism of this shape could read, and provably
violates the one-sided Landau bound at every exponent below 1 (the corollary derived and
adversary-verified in that dossier). KNS's Fourier-uniqueness-pair machinery is a different formal
object from a Beurling generalized-number system (this note does not claim a formal reduction of
one to the other), but the *qualitative* lesson, density-only mechanisms do not carry
lattice-consuming content, is exactly what KNS's own self-description confirms about itself, and
exactly what Section 5's frame-vs-collapse argument confirms independently at the level of what
the theorem's conclusion actually is. Three separate arguments (direct hypothesis computation on
the corridor's own sets, the frame/collapse structural opposition, the repo's prior DMV-kill
closure of the density-only input class) converge on the same verdict.

## 6. Citing literature check

Per the task's step 4: does KNS, or its citing literature, treat any arithmetic node set
explicitly?

| Source | Tier | Finding |
|---|---|---|
| KNS 2306.14013 itself | FETCHED | Cites Bondarenko-Radchenko-Seip's $\log n$ / zeta-zero pairing once, in Related Work, attributed explicitly to "an arithmetic approach based on the theory of modular forms and Dirichlet series," contrasted with KNS's own analytic method. No claim their own theorem reaches it. No mention of primes or prime powers specifically anywhere found. |
| "Critical and asymmetric Fourier uniqueness pairs," arXiv:2509.17600 (Sept 2025) | FETCHED (ar5iv) | Explicitly "motivated by the recent work of Kulikov, Nazarov, and Sodin." Still requires two-sided $\mathbb Z$-indexed sequences (its own Definition C, unchanged from KNS). Cites the same $\log n$/zeta-zero example purely as motivation; constructs no arithmetic sequences in its own theorems. Its "frame and interpolation" result remains a full-rank/bounded-below system, not a collapse mechanism. **Its own Remark 3 states the spacing behavior of the actual zeta zeros does NOT satisfy this paper's (more general, weaker-than-KNS) sufficient conditions** either, independently corroborating this note's Section 4.2 cross-check computation. |
| "The basis functions of Fourier Interpolation," arXiv:2512.18677 (Dec 2025) | FETCHED (abstract) | Cites KNS; shows the celebrated Radchenko-Viazovska basis functions themselves "fail to yield a Riesz basis in the Hilbert space used by Kulikov, Nazarov, and Sodin." No arithmetic node-set treatment. Notable as a second independent data point that even this literature's own flagship examples sit in friction with the KNS frame apparatus. |
| WebSearch citation scan | FETCHED (search results) | No paper found, at this search depth, constructing or analyzing primes, log-primes, or prime powers as a KNS-style node set. Absence-at-search-depth, correctly tiered, not a proof of non-existence. |

**Reading.** The one real number-theoretic exemplar in this entire literature line (the
Bondarenko-Radchenko-Seip zeta-zero pairing) is (i) built from a functional equation, not
density alone, and (ii) shown, by the most recent (Sept 2025) paper actually descended from KNS,
to fail even a *generalized, weakened* version of the density criterion when tested against the
real zeta zeros. Nothing in this citation graph treats primes or prime powers at all. This is
consistent, not coincidental, with Section 4's direct computation.

## 7. Verdict

**FITS-IN-PART**, with the practical consequence of a hardened closure.

- Node set (a) (single-prime lattice, the corridor's most literal arithmetic-progression object):
  MISMATCH, computed exactly: KNS's own criterion places it in the non-uniqueness (failure)
  regime, for every admissible exponent and every prime.
- Node set (b) (full prime-power log set, symmetrized): the letter of Theorem 1(i)/Corollary 2
  genuinely FITS (confirmed rigorously, not left as a doubt), but carries no S4 content in the
  best case: what is proven there is a full-rank Fourier frame, structurally the opposite of the
  rank-deficient, lattice-consuming, finite-budget, family-uniform device the S4 spec requires,
  and the mechanism is density-only by design, exactly the input class the repo's own DMV-kill
  screen has already shown insufficient for any S4-shaped exponent gain.
- The e1o instrument that actually measures the corridor's "full price at $\{\log p\}$" finding
  tests a different mathematical object (finite trig-Vandermonde rank on a truncated window or
  compact circle) than KNS's theorem (infinite two-sided sequences under the line Fourier
  transform); there is no established bridge between the two, and building one is unstarted,
  non-trivial work, not something this literature line hands over.

**#164 reopen condition (ii): DISCHARGED.** No genuine mechanism-class escape from the
lattice-tie diagnosis materializes. Combined with reopen condition (i) remaining open
(Baranov-Borichev-Havin vs. Burnol's $L_a$, not addressed by this note), the corridor's counting
side has now had both of its named cheap residuals checked; one is closed negative here, one
remains open and is SURVEYOR-cheap future work.

**Consequence for the theta-side S4 attempt:** the corridor's already-declared pivot
([`s4_cheap_falsifiers_survey.md`](../s4_cheap_falsifiers_survey.md) Section 4: "redirect BUILDER
budget at the pivot target"; TODO.md's "POST-CORRIDOR PIVOT" item) is reinforced by a third,
independently computed and triangulated reason, layered on top of the ill-posedness finding
(Section 1 of the survey) and the lattice-tie diagnosis (the e1o probe's own T4c/T4d measurements):
every density-only mechanism checked against the corridor's arithmetic node sets, across three
unrelated formal frameworks now (Beurling generalized-number systems / DMV; finite trig-Vandermonde
rank / e1o; Fourier-uniqueness pairs / KNS), converges on the same diagnosis. The missing glue
remains what [`e1o_s4_carrier.md`](../../../experiments/spectral/e1o_s4_carrier.md) Q4 item 4
already named: something that nameably consumes the additive lattice ($N(x)=x+O(1)$ / theta
functional equation), which is precisely what the theta/modular-interpolation side pays by
construction and what KNS's density-only apparatus, even where its hypothesis is met, does not.

## Handoff to BUILDER

1. **Do not pursue a KNS-based S4 construction.** This mechanism class is now closed by three
   independent arguments (Sections 4.1, 5, and the DMV-kill cross-reference), not just an
   unverified doubt. Any future candidate in this exact shape (a density-only Fourier-uniqueness
   or interpolation-pair criterion, with no lattice/FE input) should be screened against the same
   three arguments before any code is written: (i) does it apply to the corridor's actual node
   set with the right sign (Section 4's regular-variation lens is reusable: compute $\alpha$,
   compare to $1/p_0$); (ii) does its conclusion have frame/full-rank shape (then it is
   automatically not a collapse witness); (iii) is its input class density-only (then the DMV-kill
   screen already excludes it from any exponent gain below 1).
2. **The critical-regime literature (arXiv:2509.17600) is also checked and also closed.** It
   generalizes KNS toward the boundary case and toward asymmetric pairs, which looked like the
   most promising still-open direction in this exact line; its own Remark 3 shows even the zeta
   zeros fail its weakened conditions, and its own scope is still two-sided-line, still
   frame-shaped, not collapse-shaped. No further mileage expected here without new ideas beyond
   what this whole citation graph currently contains.
3. **Redirect to the theta/modular-interpolation side** and the C1 = SP2-and-SP3 counting joint,
   per TODO.md's "THE POST-CORRIDOR PIVOT" item: the lattice clause is paid by construction there
   (per LEARNINGS #160's engine reading), which is the property this whole note shows the
   density-only literature line cannot supply.
4. **Residual (i) remains genuinely open** and is the one item left from
   [`s4_cheap_falsifiers_survey.md`](../s4_cheap_falsifiers_survey.md) Section 4's named
   residuals: whether Baranov-Borichev-Havin's meromorphic model-space majorant theory
   (arXiv:math/0605052) can be run directly against Burnol's pole-carrying $L_a$ to repair
   falsifier 2's ILL-POSED verdict. Not addressed by this note; SURVEYOR-cheap next step if the
   counting side is revisited at all.
