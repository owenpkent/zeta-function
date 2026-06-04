# The logical status of RH: can we prove it undecidable? (Gödel)

> Written 2026-06-04. Answers a recurring question: "Can we prove RH has no
> solution, or that it is undecidable (Gödel)?" Short answer: **no, undecidability
> is not an escape from RH being true.** Because RH is a $\Pi^0_1$ arithmetic
> sentence, a proof that it is independent of ZFC would *itself* prove RH true.
> The only logically live undecidability scenario is "true but unprovable in $T$,"
> which is a back door to truth, not a third option beside true/false. And no
> currently known technique can establish even that.
>
> Every assertion below is tagged **PROVEN** / **FOLKLORE** / **OPEN**. The
> $\Pi^0_1$ classification and the "independence implies truth" lever were
> adversarially verified (a panel of skeptics tried to break each load-bearing
> claim); the surviving caveats are folded in. This doc fills the gap left by the
> one-line pointer in [`connes_2602_letter_to_riemann.md`](connes_2602_letter_to_riemann.md)
> ("a Godel/Chaitin digression on RH's logical status") and connects to the
> [marginal-positivity thesis](all_roads_to_the_signature.md) and the
> Davenport-Heilbronn discipline.

## 1. RH is $\Pi^0_1$, and what that forces

**PROVEN.** RH is (provably equivalent to) a $\Pi^0_1$ arithmetic sentence: a single
universal quantifier over $\mathbb{N}$, "$\forall n\, P(n)$," with $P$ a decidable
(primitive-recursive) predicate. Its negation is therefore $\Sigma^0_1$
(recursively enumerable): **if RH is false, a counterexample is mechanically
findable in finite time.**

**The $\Pi^0_1$ status is a theorem, not a definition.** The textbook statement
("every nontrivial zero of $\zeta$ has real part $1/2$") quantifies over the
complex continuum and is, on its face, $\Pi^1_1$ / second-order, or at best
$\Pi_2$ once you account for locating zeros. The drop to $\Pi^0_1$ is *earned* by
a specific arithmetization. Three routes:

- **Lagarias 2002 (PROVEN, the cleanest face).** RH $\iff$ for all $n \geq 1$,
  $\sigma(n) \leq H_n + \exp(H_n)\ln(H_n)$, where $\sigma$ is sum-of-divisors and
  $H_n = \sum_{k\leq n} 1/k$. No threshold; equality only at $n = 1$.
- **Robin 1984 (PROVEN).** RH $\iff$ for all $n \geq 5041$,
  $\sigma(n) < e^\gamma\, n \ln\ln n$. The finite set of violators $\leq 5040$ is
  itself a theorem. (This is the inequality already in
  [`docs/research_atlas/README.md`](../research_atlas/README.md).)
- **Davis-Putnam-Robinson-Matiyasevich (DPRM) (PROVEN, the rigorous backbone).**
  RH $\iff$ a single Diophantine equation $D(x, a_1,\ldots,a_k) = 0$ has no
  natural-number solution, i.e. "$\forall x\, \neg\exists\bar a\,[D = 0]$." The
  matrix is manifestly recursive with **no transcendentals**. An explicit (huge,
  multi-page) such polynomial has been written down.

**The decidability of the matrix is earned, not read off (unanimous adversarial
correction).** Taken literally, "$\sigma(n) < e^\gamma n \ln\ln n$" compares a
rational to a transcendental real, which is not prima facie a decidable predicate
of $n$. Decidability is rescued by two facts the bare inequality hides:

1. **Effective approximability.** $e, \gamma, \ln, \exp$ are computable reals with
   primitive-recursive Cauchy sequences and effective moduli of convergence, so the
   right-hand side is computable to any precision with a known rate.
2. **Strictness (the load-bearing edge case).** You must never have to decide an
   exact equality of a rational against a transcendental. Robin is strict for all
   $n > 5040$; Lagarias's $\leq$ is equality only at $n = 1$ and strict for
   $n \geq 2$. So a finite-precision computation always separates the two sides and
   terminates with the correct verdict.

For the airtight version, cite DPRM (recursive matrix, no transcendentals) as the
backbone and present Robin/Lagarias as the elementary face. The threshold constant
$5040$ and the value $e^\gamma$ are irrelevant to the complexity class; they affect
only truth.

**What $\Pi^0_1$ forces (all PROVEN):**

- **Refutability asymmetry.** A false $\Pi^0_1$ sentence has a finite,
  weak-arithmetic-checkable counterexample. So numerical zero verification
  (Turing's method, Platt-style rigorous interval arithmetic) is genuine *partial*
  verification: it can only ever **refute** RH, never confirm it. $\Pi^0_1$ truth
  is refutable by one witness, not verifiable by any finite number.
- **Same complexity class as $\mathrm{Con}(T)$.** Consistency statements are the
  canonical $\Pi^0_1$ independent sentences (Gödel). The analogy "RH could be
  true-but-unprovable like a consistency statement" is logically apt, not loose.
- **The Gödel lever.** See §2.

**Not clean $\Pi^0_1$ witnesses:** the Riesz (1916) and Hardy-Littlewood (1918)
growth-rate criteria are PROVEN RH equivalences but in their natural form carry an
$O(\cdot)$-with-constant existential plus a universal, a $\Sigma^0_2/\Pi^0_2$ shape.
Cite them as equivalences; do not use them for the complexity claim.

## 2. The Gödel lever, stated exactly

This is where the loose folklore ("if RH is independent it's true") needs surgical
hypotheses.

**THEOREM (false $\Pi^0_1$ $\Rightarrow$ refutable). PROVEN, hypothesis-light.**
Let $T$ be any recursively axiomatized theory extending Robinson arithmetic $Q$
(PA and ZFC qualify). Let $S = \forall x\, \varphi(x)$ be $\Pi^0_1$ with $\varphi$
decidable. If $S$ is false in the standard model $\mathbb{N}$, then $T \vdash \neg S$.

*Proof.* $\mathbb{N} \models \neg S$ gives a standard numeral $n_0$ with
$\mathbb{N} \models \neg\varphi(n_0)$. The sentence $\neg\varphi(n_0)$ is a true
$\Delta_0$ (hence $\Sigma_1$) sentence. By the **$\Sigma_1$-completeness of $Q$**
($Q$ proves every true $\Sigma_1$ sentence) and $T \supseteq Q$, $T \vdash
\neg\varphi(n_0)$, hence $T \vdash \exists x\, \neg\varphi(x) = \neg S$. $\square$

**The engine is $\Sigma_1$-COMPLETENESS, not $\Sigma_1$-soundness (key adversarial
correction).** This direction uses no consistency, no soundness, no
$\omega$-consistency. $\Sigma_1$-completeness is a free, unconditional property of
any extension of $Q$.

**COROLLARY (irrefutability $\Rightarrow$ truth). PROVEN.** If $T \nvdash \neg S$
and $S$ is $\Pi^0_1$ and $T \supseteq Q$, then $\mathbb{N} \models S$.

**Applied to RH.** If $T \nvdash \neg\text{RH}$, then RH is true in $\mathbb{N}$.
Precisely what is and is not needed:

- The "unprovable" half of "independent" ($T \nvdash \text{RH}$) is **unused** for
  the truth conclusion. Only **irrefutability** ($T \nvdash \neg\text{RH}$) does
  the work.
- **$\Sigma_1$-soundness of $T$ is superfluous** to the bare implication
  "irrefutable $\Rightarrow$ true." It is sufficient but strictly stronger than
  necessary (its honest role is non-vacuity: $\Sigma_1$-soundness $\Rightarrow$
  consistency).

**Where soundness genuinely is load-bearing (name it, do not skip it):**

- To read "$T$ proves RH $\Rightarrow$ RH is true," you need **$\Pi_1$-soundness**
  of $T$. Note $\Sigma_1$-soundness $\neq \Pi_1$-soundness; name the right one.
- To trust that an actual *independence proof* reflects reality (that ZFC's silence
  means no genuine counterexample exists), you need ZFC to be **$\Sigma_1$-sound**.
  If ZFC were $\Sigma_1$-unsound it could fail to refute a false RH (a nonstandard
  "view" in which the counterexample is invisible), and the lever breaks. A genuine,
  named, universally accepted (but not free) assumption.

**THE DUAL (no "false but unprovable"). PROVEN, with a wording fix.** RH cannot be
false-in-$\mathbb{N}$ yet irrefutable. The slogan "false but unprovable" is
literally wrong: a false RH being unprovable *as the positive sentence* is the
ordinary situation. The correct statement is **"false but NOT REFUTABLE" is
impossible**. A false $\Pi^0_1$ sentence is always refutable, already in $Q$.

Two wording anchors:

- **"False" means false in the standard model $\mathbb{N}$.** A $\Pi^0_1$ sentence
  can fail in a *nonstandard* model via a nonstandard pseudo-witness while being
  true in $\mathbb{N}$. So "RH true but independent" is exactly compatibility with
  nonstandard pseudo-counterexamples.
- **The verified witness is to the arithmetized surrogate** (an integer inequality
  / Diophantine matrix), not a literal transcendental zero off the line.

## 3. The punchline: undecidability is a back door to truth, not an escape hatch

The naive picture imagines three outcomes: RH true, RH false, or RH "undecidable"
(a way to sidestep both). **For $\Pi^0_1$ sentences that third option collapses
into the first.** The three exhaustive cases relative to a $\Sigma_1$-sound
$T \supseteq Q$ (PROVEN):

1. $T$ proves RH $\Rightarrow$ RH true (needs $T$ $\Pi_1$-sound).
2. $T$ refutes RH $\Rightarrow$ RH false, with an actual counterexample (needs $T$
   $\Sigma_1$-sound).
3. RH independent of $T$ $\Rightarrow$ since $T \nvdash \neg\text{RH}$ and RH is
   $\Pi^0_1$ over $Q$, **RH is true**.

So a proof that RH is independent of ZFC would *itself* be a proof that RH is true.
**Independence is a (strange, nonstandard) back door to proving RH, not a way around
proving it.** Anyone hoping "maybe RH is just undecidable, so we never have to settle
it" has the logic backwards: succeeding at the independence route *is* settling it
(the truth half), and it is at least as hard as a direct proof, because it
additionally requires showing non-provability.

**The single live undecidability scenario: "true but unprovable in $T$."** This is
a real logical possibility (the way $\mathrm{Con}(\text{PA})$, Goodstein, and
Paris-Harrington are true-but-PA-unprovable). RH being $\Pi^0_1$ does **not** make
it decidable; it only excludes the "false but unrefutable" corner.

**A deeper structural cost (PROVEN).** A proof that ZFC $\nvdash \neg\text{RH}$
entails $\mathrm{Con}(\text{ZFC})$ (an inconsistent theory refutes everything). By
Gödel's second incompleteness theorem, ZFC $\nvdash \mathrm{Con}(\text{ZFC})$.
Therefore:

- ZFC cannot prove "RH is independent of ZFC" unless ZFC already settles RH.
- Any genuine independence proof for RH must be carried out in a metatheory $M$
  **strictly stronger than ZFC** (one proving $\mathrm{Con}(\text{ZFC})$). You never
  get a ZFC-internal proof of RH this way; you get an $M$-proof, only as trustworthy
  as $M$'s $\Pi_1$-soundness.

So "modulo soundness of the metatheory" is not a footnote: the required metatheory
is provably non-conservative over ZFC.

**The Chaitin / Calude / busy-beaver demystification.** A common confusion is that
these results "show RH is near the undecidability frontier." They do not:

- Chaitin's $\Omega$ incompleteness bounds how many bits of $\Omega$ a theory can
  determine. RH's truth is encoded in finitely many bits because RH $\iff$ a
  specific program never halts. A **reformulation/encoding**, not an independence
  result. Chaitin's "RH might be true for no reason" is explicit **philosophical
  speculation** (FOLKLORE), no theorem behind it.
- Calude-Calude(-Dinneen) measured the program-size complexity of "halts iff RH
  false" ($\approx 7780$ bits, ranking RH above Goldbach). A "how hard to state as a
  halting question" metric, **orthogonal to provability/independence**.
- Yedidia-Aaronson and successors built a Turing machine that halts iff RH is false
  (originally $5372$ states, informally reduced toward $\approx 744$).
  **Critical distinction:** the *separate* $\approx 7918$-state ($7910$ in one
  version) ZFC-independence machine (built on a Friedman statement) has provably
  ZFC-independent behavior; the RH machine is **NOT known to be independent of
  anything**. The small state count is an engineering fact about encoding
  efficiency, carrying zero metamathematical force about RH's decidability.

Every $\Pi^0_1$ conjecture trivially has a halting-machine and a Diophantine avatar.
That is reformulation, not metamathematical progress, and not evidence of
independence.

## 4. Reality check: why no known technique can prove RH independent

**EMPIRICAL / FOLKLORE (current literature status, not a theorem): there is no known
technique that proves RH independent of ZFC or PA.** The two clauses below ARE
theorems.

**Forcing provably cannot do it (PROVEN).** A set-forcing extension $V[G]$ adds no
new naturals: $\omega^V = \omega^{V[G]}$. Hence $V$ and $V[G]$ satisfy exactly the
same arithmetic sentences (all $\Sigma^0_n / \Pi^0_n$). So forcing cannot change
RH's truth value and cannot witness its independence.

- *Citation precision:* the operative fact is the elementary one (same $\omega$
  $\Rightarrow$ same arithmetic truth, $\Delta_0$/Levy absoluteness for transitive
  models). Shoenfield's $\Sigma^1_2/\Pi^1_2$ absoluteness theorem (1961) is correct
  but a sledgehammer: RH ($\Pi^0_1 \subset$ arithmetic $\subset \Sigma^1_2$) is far
  below its level. Shoenfield earns its keep only if you refuse the $\Pi^0_1$
  reduction and bound RH at the analytic level.

**Large cardinals are a DIFFERENT case (unanimous adversarial correction).**
Absoluteness fixes RH's truth value across models; it does **not** bound provability
strength. Large-cardinal axioms demonstrably *do* prove new $\Pi^0_1$ theorems that
ZFC cannot: the canonical example is $\mathrm{Con}(\text{ZFC})$, a $\Pi^0_1$ sentence
provable from "there exists an inaccessible cardinal" but not in ZFC. So:

- It is **OPEN** (not excluded by any absoluteness theorem) that some large-cardinal
  axiom **proves RH** where ZFC does not. Such a proof would be a perfectly good
  proof of RH.
- What large cardinals **cannot** do is exhibit RH as *independent*: consistency
  strength can settle a $\Pi^0_1$ statement only affirmatively, never reveal it as
  two-sided independent. They extend absoluteness *upward*, the opposite of helpful
  for an undecidability program.

**Why this is a category difference from CH (PROVEN).** CH lives at the level of
$\mathcal{P}(\omega)$ / the reals, exactly where forcing operates and where
Cohen/Gödel established two-sided independence. RH is arithmetic ($\Pi^0_1$),
beneath the entire CH/Souslin/Whitehead independence toolkit. "Maybe RH is
independent like CH" is a level confusion: CH-independence is forcing-independence
over the reals; RH-independence (if it existed) would have to be
$\mathrm{Con}(\text{ZFC})$-strength proof-theoretic independence over arithmetic.

**PA vs ZFC.** The forcing/large-cardinal argument is about set-theoretic
independence (ZFC). PA-independence is a separate proof-theoretic question (the
Paris-Harrington / Goodstein / Kirby-Paris family shows true $\Pi^0_1$-ish
statements *can* be PA-independent). Being $\Pi^0_1$ does **not** make RH
PA-decidable. RH being PA-independent-but-true is more plausible a priori than
ZFC-independence, and neither is anywhere near demonstrable today.

**Reverse-mathematics strength of RH (OPEN / thin literature).** There is no
established reverse-math classification ($\text{RCA}_0$, $\text{WKL}_0$,
$\text{ACA}_0$, ...) of RH's *proof* strength, because RH is open and you cannot
calibrate a proof that does not exist. What is known: RH is *statable* in very weak
systems ($\Pi^0_1$ needs no set-existence; expressible even at EFA/PRA level). The
expectation that a proof of RH, if found, would formalize in a relatively weak
system (Friedman's "grand conjecture") is **SPECULATION**. Whether the equivalence
"RH(analytic) $\iff$ Robin/Lagarias" is provable in $\text{RCA}_0/\text{WKL}_0$
specifically is a real **OPEN** reverse-math question. Safe claim: the equivalence is
provable in PA (and ZFC). Do not assert PRA/RCA$_0$ as certain.

## 5. Connection to the marginal-positivity thesis

The logical picture reinforces the project's working thesis that RH is "just barely
true" and that any proof must engage the exact structure of $\zeta$, not soft
generalities. The Davenport-Heilbronn discipline is the cleanest bridge: D-H has
off-line zeros, so the D-H analogue of the $\Pi^0_1$ statement is **false and (in
principle) finitely refutable**, exactly the $\Sigma^0_1$ falsity-certificate the
logic predicts. That is *why* D-H is a clean wrong-approach detector and why the
marginal-positivity finding (zero margin, the K1 wall, the analytic $2/3$ ceiling,
the soft-positivity $370\times$ cancellation residue) is a compass rather than a
wall: a soft method that proves "RH" for both $\zeta$ and D-H is proving a
$\Sigma^0_1$-refutable falsehood for D-H, so it must be wrong. The logic and the
experiments agree on the same coordinate.

RH's $\Pi^0_1$ form says any genuine proof distinguishes $\zeta$ from its
functional-equation-only neighbors at the level of the **Euler product** (the exact
arithmetic structure), and the four-architecture framing localizes where that
distinction can live: not at Level 3 (statistics, GUE, log-correlated structure, all
compatible with a $\beta = 0.51$ zero), but at Level 4 (positivity / the arithmetic
signature). The Gödel lever adds nothing to the *difficulty* (it does not make RH
easier), but it sharpens the *target*: there is no escape into "undecidable," so the
only outcomes are a direct proof, a stronger-axiom proof, or a true-but-unprovable
verdict that would itself be a proof of truth. Architecture 2 (Deninger / $\mathbb{F}_1$)
sits outside the D-H discipline precisely because it engages the Euler product that
D-H lacks, consistent with the $\Pi^0_1$ reading that the arithmetic structure is
load-bearing.

## 6. Tag summary

- **PROVEN:** RH is $\Pi^0_1$ (Lagarias/Robin/DPRM); decidability of the matrix via
  effective approximability + strictness; false $\Pi^0_1$ $\Rightarrow$ refutable in
  $Q$ ($\Sigma_1$-completeness, hypothesis-light); irrefutable $\Pi^0_1$
  $\Rightarrow$ true in $\mathbb{N}$; "false but not-refutable" impossible;
  independence-of-ZFC proof $\Rightarrow$ RH true; independence proof requires a
  $\mathrm{Con}(\text{ZFC})$-strength metatheory (Gödel II); forcing cannot change
  arithmetic truth; large cardinals can prove new $\Pi^0_1$ truths
  ($\mathrm{Con}(\text{ZFC})$ from an inaccessible); Shoenfield absoluteness; CH is
  forcing-independent over the reals.
- **FOLKLORE / attribution-only:** Kreisel "RH is $\Pi^0_1$" (mathematically solid,
  exact published locus unverified); the slogan "if RH is independent then it's true"
  (correct once hypotheses are fixed as above); "no known technique proves RH
  independent" (true as current literature status, not a theorem); Chaitin's "RH
  might be true for no reason" (explicitly philosophical).
- **OPEN / thin literature:** exact weak-theory (RCA$_0$/WKL$_0$/PRA) provability of
  the analytic $\iff$ elementary equivalence; reverse-math proof-theoretic strength
  of RH (cannot be calibrated without a proof); whether any large-cardinal axiom
  actually settles RH; whether RH is independent of PA or ZFC at all (no evidence
  either way).

## 7. Open research: what is genuinely open (and what only looks open)

A web-grounded survey across six clusters (reverse math, bounded arithmetic,
Diophantine/busy-beaver, the independence program, algorithmic randomness,
formalization), each adversarially stress-tested for "is this actually open, or
already closed?" The honest bottom line: the logical-status excursion has exactly
**one genuinely open technical core**, a handful of write-down-not-research items,
and a large set of dead corners. **None of it supplies the project's missing
positivity.** Its value is diagnostic (a sharper target and a wrong-approach filter),
not constructive.

### Ranked open questions

1. **Reverse-math strength of the zero-counting step $N(T) = \tfrac{T}{2\pi}\log\tfrac{T}{2\pi} - \tfrac{T}{2\pi} + O(\log T)$ via the argument principle.** OPEN, the single uncalibrated technical core. No paper places the argument principle / Rouché / $N(T)$ in the reverse-math hierarchy. Honest bracket: $\text{WKL}_0$-up-to-$\text{ACA}_0$ (the adjacent Riemann mapping theorem reverses to $\text{ACA}_0$ over $\text{WKL}_0$, Yokoyama 2007, so "downstream of Cauchy" does **not** force "WKL$_0$"). Status dormant; hard but well-posed (clean attack: test the $\text{ACA}_0$ lower bound first); project-relevance low-to-medium.
2. **Minimal fragment proving "analytic RH $\iff$ Robin/Lagarias."** OPEN. The asymmetry is real: the elementary face is EFA-level ($\text{EFA} = I\Delta_0 + \exp$ is the statability floor, Parikh 1971, since the witnesses reference $\exp/\log$), the analytic bridge is uncalibrated (= #1). Tractable to BRACKET, not to pin to a least subsystem by bookkeeping alone. Project-relevance medium (the Lean substrate can put the first data point on it).
3. Lower-ranked / low-relevance: $\Pi$-form status of twin-prime / Elliott-Halberstam (Nayebi 2023); infinitude of primes in $I\Delta_0$ alone (open since Paris-Wilkie-Woods 1988, a famous 37-year frontier but the wrong mountain, DO NOT ATTEMPT); the master "PA/EFA vs beyond-ZFC for an RH proof" meta-question (unresolvable without an actual proof); GRH-Diophantine via the Booker/Turing-method strand; AI autoformalization closing the analytic-NT gap (a forecast, not a question).

### Dead corners (look open, are empty: zero build effort)

- **"Is RH independent of ZFC?"** Structurally foreclosed: $\Pi^0_1$ $\Rightarrow$ independence implies truth; forcing-immune; needs a $\mathrm{Con}(\text{ZFC})$-strength metatheory. No mechanism to answer affirmatively without over-settling RH.
- **"RH proved via ZFC-independence"** papers (Nielsen-Semita 2025, the withdrawn Feinstein 2003): the canonical circular fallacy.
- **Chaitin-$\Omega$ "true for no reason."** Settled-in-the-negative; Chaitin himself disclaims applicability (math/0306042). No theorem.
- **Smallest TM halting iff RH false.** Stuck at $744$ states since 2016; all post-2016 busy-beaver motion is the ZFC machine or $\mathrm{BB}(5)$, not RH. Code golf, metamathematically empty.
- **Program-size bit-counts** ($\approx 7780$ bits, CCD 2006) and **minimizing the RH-Diophantine equation** (existence proven, $\approx 166$ variables Moroz-Norkin 2020): the minimization is the same trade-off open for *all* r.e. sets, no RH-specific content.
- **"RH not provable in weak system $T$"** for any $T$: a true vacuum (non-refutability already implies truth, so it is at least as hard as proving RH).

### Concrete tractable entry points for this repo's Lean substrate

- **(A) `lean/ZetaRH/RHEquivalences.lean`, the equivalence hub. LANDED 2026-06-04 (build green).** Defines `robinInequality`, `lagariasInequality`, `mertensBound` as concrete `Prop`s over Mathlib (`ArithmeticFunction.sigma`, `harmonic`, `Real.eulerMascheroniConstant`, `ArithmeticFunction.moebius`), plus `li_criterion` and `nymanBeurling_criterion` bundling the analytic data Mathlib lacks. Each carries an `iff`-to-`RiemannHypothesis` theorem (deep directions documented `sorry`s: #RB-1, #LG-1, #MT-1, #LI-1, #NB-1). Three sorry-free anchors proved: the definitional reformulation, the Mathlib-bridge re-export, and `lagarias_holds_at_one` (the $n = 1$ equality case, `#print axioms` clean). **Load-bearing correction (applied):** `lagariasInequality` uses $\sigma(n) \le H_n + e^{H_n}\log H_n$ with equality at $n = 1$, NOT strict `<`, or the $n=1$ check is false. The Weil-form positivity face (#EF-2) stays in `ExplicitFormula.lean`; this hub does not duplicate it.
- **(B) Prove the elementary decidable half. PARTIALLY LANDED 2026-06-04.** Sorry-free results in `RHEquivalences.lean` (all with clean `#print axioms`, no `sorryAx`, no `ofReduceBool`): `rh_arith_refutable` (the $\Sigma^0_1$ structure: $\neg$ `RH_arith` $\iff$ a single $n$ violating Lagarias, the formal core of §2's "no false-but-unrefutable"); concrete $\sigma$ computations (`sigma_one_six`, `sigma_one_twelve`) witnessing the matrix's arithmetic side is kernel-computable; `lagarias_holds_at_three` ($\sigma(3) = 4 \le 11/6 + e^{11/6}\log(11/6) \approx 4.08$, by order-1 effective bounds: $e^{11/6} = e\cdot e^{5/6} \ge e\cdot(11/6) \ge (27/10)(11/6)$ via `add_one_le_exp` + `exp_one_gt_d9`, and $\log(11/6) \ge 5/11$ via `log_le_sub_one_of_pos`); and `lagarias_holds_at_two`, the HARDEST small case (smallest margin, exact RHS only $\approx 3.32$ vs $\sigma(2)=3$), which the order-1 bounds cannot reach and which needs SHARP bounds from comparing integer powers of $e$ to rational powers ($e^{3/2} \ge 4$ because $(e^{3/2})^2 = e^3 = (e^1)^3 \ge (27/10)^3 \ge 16$; $\log(3/2) \ge 2/5$ because $(e^{2/5})^5 = e^2 = (e^1)^2 \le (68/25)^2 \le (3/2)^5$, via `le_of_pow_le_pow_left` and `le_log_iff_exp_le`). Together these concretely realize the §1 claim that the matrix is decidable by effective approximation, not as a literal `Decidable` real predicate. The margins are NON-monotone in $n$ (exact RHS minus $\sigma(n)$: $0$ at $n=1$, $0.32$ at $n=2$, $1.62$ at $n=3$, $0.98$ at $n=4$, $4.38$ at $n=5$): $n=2$ needs sharper bounds than $n=3$ because its margin is smaller, not because of any trend with $n$. The genuinely tight cases are highly composite $n$ (e.g. $n=12$, margin $\approx 0.01$), where $\sigma(n)$ is large relative to the bound. The real formalization-layer trace of marginal positivity is that no *uniform* soft bound can cover all $n$: that would be proving RH. The analytic forward direction stays deferred (#LG-1).
- **(C) State the $\Pi^0_1$ witness as a kernel object. LANDED 2026-06-04 (with A).** `RH_arith := lagariasInequality` with `RH_arith_iff_RiemannHypothesis` reusing #LG-1 (no new sorry). Turns the "false $\Pi^0_1$ $\Rightarrow$ refutable" lever from prose into a formal object: its negation is a $\Sigma^0_1$ existence of one refuting $n$. (Entry point B, the finite elementary half, has only its $n=1$ anchor proved so far; the general $n < 5041$ verification remains open.)
- **(D) The D-H refutation lever, two layers.** Logical: D-H has no Euler product, hence no $\sigma$-style multiplicative inequality, so its Robin-type $\Pi^0_1$ analogue is **false and $\Sigma^0_1$-refutable**, with the single witness corresponding to the off-line zero $\rho \approx 0.8085 + 85.699\,i$ (location: Spira 1994). Formalization: an ADVERSARY test that any candidate `robinInequality`$\iff$RH proof **cannot** be instantiated for a D-H-shaped object (if it goes through, the proof is wrong).

Blocked (not repo-sized): a kernel-checked D-H off-line-zero *certificate* needs verified argument-principle zero-counting for meromorphic functions plus rigorous-numerics Hurwitz-zeta evaluation, a multi-person Mathlib effort.

## References

- J. C. Lagarias, "An elementary problem equivalent to the Riemann hypothesis,"
  *Amer. Math. Monthly* 109 (2002), 534-543.
- G. Robin, "Grandes valeurs de la fonction somme des diviseurs et hypothèse de
  Riemann," *J. Math. Pures Appl.* 63 (1984), 187-213.
- M. Davis, Yu. Matiyasevich, J. Robinson, "Hilbert's tenth problem. Diophantine
  equations: positive aspects of a negative solution," *Proc. Sympos. Pure Math.* 28
  (1976) (the DPRM theorem; RH as a Diophantine $\Pi^0_1$ statement).
- G. Kreisel, on the arithmetical ($\Pi^0_1$) form of RH (folklore attribution).
- J. Shoenfield, "The problem of predicativity" / Shoenfield absoluteness (1961).
- C. S. Calude, E. Calude, M. J. Dinneen, "A new measure of the difficulty of
  problems," *J. Mult.-Valued Logic Soft Comput.* (RH program-size complexity).
- A. Yedidia, S. Aaronson, "A relatively small Turing machine whose behavior is
  independent of set theory," *Complex Systems* 25 (2016) (the $\approx 7918$-state
  ZFC-independence machine; the *separate* $5372$-state RH machine is not known
  independent).
- Yu. Matiyasevich, "Diophantine flavor of Kolmogorov complexity" / the
  $\psi(n) = \ln\mathrm{lcm}(1,\ldots,n)$ reformulation, *Chebyshevskii Sb.* (2018)
  and the 130-instruction register machine, *Theoret. Comput. Sci.* 807 (2020),
  257-265 (single author).
- B. Z. Moroz, A. A. Norkin, "On a theorem of Yu. V. Matiyasevich," *Math. Notes*
  108 (2020) (an explicit RH-equivalent Diophantine system in $\approx 166$
  variables).
