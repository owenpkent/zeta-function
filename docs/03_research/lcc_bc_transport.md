# The LCC/BC transport: the log-crystal cone as a KMS-weight simplex

**Status: BUILDER candidate (2026-06-11), the e2nn/#81 follow-on (TODO line 162). ADVERSARY-verified same day: UPHELD-WITH-REVISIONS (report appended at the end of this file; kill switch A2 settled in the construction's favor, P1 closed unconditionally, the conjecture relabeled a restatement of #76 clause (i)). Synthesized as LEARNINGS #82.**

**Task.** Formulate the Lonely Crystal (LCC, [first_principles_conjecture_program.md](first_principles_conjecture_program.md) section 3.1, LEARNINGS #76) cone of positive log-crystals as the KMS-type simplex of a scaling $\mathbb{N}^\times$-action, so the Bost-Connes uniqueness template (#81: pole = normalization-killer, prime-rotation density = uniformizer) can run the ghost-crystal kill on the source-side cone.

**Verdict in one sentence.** (B) with a repaired form: the literal BC axiom, KMS quasi-invariance of the crystal functional itself, PROVABLY fails (its solution set is the flat ray $c_n = c_1 n^{-\beta}$, the comb of $\zeta(s)$, not of $-\zeta'/\zeta$), and the correct transported object is one twist away: the von Mangoldt crystal is the energy 1-cumulant of the unique quasi-invariant ray, equivalently its integrated comb satisfies the additive cocycle identity $B(pn) - B(n) = \log p$. The repaired statement is precise, K1-clean, and its open core is exactly composite pinching, now carrying a new structural name: vanishing of mixed cumulants = independence across prime sites.

---

## 1. Object

### 1.1 The cone (restating LCC precisely)

Test class: even $g \in C_c^\infty(\mathbb{R})$, with $\hat g(r) = \int_{\mathbb{R}} g(x) e^{irx}\,dx$ (entire, Paley-Wiener). Archimedean density (project convention, e3m/e3aa): $\Omega(r) = \mathrm{Re}\,\psi(\tfrac14 + \tfrac{ir}{2}) - \log\pi$.

**Definition 1 (comb space).** A comb is a sequence $c = (c_n)_{n\ge1}$ with $c_n \ge 0$. Its unnormalized form is $b_n := c_n\sqrt{n} \ge 0$. No growth condition is imposed: for compactly supported $g$ only finitely many $n$ contribute below.

**Definition 2 (log-crystal, the LCC cone).** A log-crystal for the zeta source is a pair $(\mu, c)$: $\mu$ a positive tempered measure on $\mathbb{R}$, $c$ a comb, satisfying the explicit-formula identity for ALL even $g \in C_c^\infty(\mathbb{R})$:

$$\int_{\mathbb{R}} \hat g(r)\,d\mu(r) \;=\; \hat g(\tfrac{i}{2}) + \hat g(-\tfrac{i}{2}) \;-\; 2\sum_{n\ge1} c_n\, g(\log n) \;+\; \frac{1}{2\pi}\int_{\mathbb{R}} \hat g(r)\,\Omega(r)\,dr. \tag{EF}$$

Write $\mathcal{W}_\zeta$ for the set of log-crystals. Since (EF) determines the distribution $\mu$ from $c$ (Fourier uniqueness), $\mathcal{W}_\zeta$ is parameterized by the combs $c \ge 0$ whose induced $\mu_c$ is a positive measure. LCC clause (i) (rigidity, unconditional target): $\mathcal{W}_\zeta \subseteq \{(\mu_*, \Lambda(n)/\sqrt n)\}$. Clause (ii) (attainment, RH-equivalent): $\mathcal{W}_\zeta \neq \emptyset$.

### 1.2 The scaling system

**Definition 3 (crystal Toeplitz system).** On $\ell^2(\mathbb{N})$ with basis $\{e_n\}$, isometries $V_m e_n = e_{mn}$ ($m \in \mathbb{N}^\times$), generating the multiplicative Toeplitz algebra $\mathcal{T}_{\mathbb{N}^\times} \cong \bigotimes_p \mathcal{T}_p$ (one classical Toeplitz factor per prime: the free generators of $\mathbb{N}^\times$). Time evolution $\sigma_t = \mathrm{Ad}(N^{it})$, $N e_n = n\,e_n$, so $\sigma_t(V_m) = m^{it} V_m$ and $H = \log N$ has spectrum $\{\log n\}$, which is exactly the crystal support. Everything is built from $\mathbb{N}$ alone: no L-function data, no zeros.

A comb defines a diagonal weight $w_c(f) = \sum_n c_n f(n)$ on $c_0(\mathbb{N}) \subset \mathcal{T}_{\mathbb{N}^\times}$, manifestly $\sigma$-invariant.

**Definition 4 (the literal BC axiom: KMS$_\beta$ quasi-invariance).** $w(V_m\, a\, V_m^*) = m^{-\beta}\, w(a)$ for all $m \in \mathbb{N}^\times$. On diagonal weights this reads $c_{mn} = m^{-\beta} c_n$ for all $m, n$, i.e. the scaling map $T_p : c(n) \mapsto c(pn)$ acts with exact cocycle $p^{-\beta}$ everywhere.

**Definition 5 (integrated comb and the cocycle identity).** $B := \mathbf{1} * b$, i.e. $B(n) = \sum_{d \mid n} b_d$ (Dirichlet convolution; $B$ is the comb of $\zeta(s)\,C(s)$ where $C(s) = \sum_n b_n n^{-s}$). The increment $\Delta_p B(n) := B(pn) - B(n)$ satisfies $\Delta_p B(n) \ge 0$ automatically whenever $b \ge 0$ (the new divisors of $pn$ contribute nonnegatively). The **KMS-cocycle condition** is

$$\Delta_p B(n) = \log p \quad \text{for all primes } p \text{ and all } n \ge 1, \tag{C}$$

i.e. the multiplicative integral of the crystal reproduces the additive Radon-Nikodym cocycle $\log(pn) = \log p + \log n$ of the scaling action, with the cocycle VALUE equal to the position increment of the support set $\{\log n\}$.

### 1.3 Two lemmas (proven here; one-line proofs, machine-checked identities)

**Lemma 1 (quasi-invariance collapse; the O2 computation).** The solution set of Definition 4 is exactly the flat ray $c_n = c_1 n^{-\beta}$. Proof: induct along factorization, $c_n = c_{n\cdot1} = n^{-\beta} c_1$. At $\beta = \tfrac12$ this is $b_n \equiv c_1$, the comb of $c_1\,\zeta(s)$: a divisor-type comb with full support, NOT the von Mangoldt comb. Explicit witness: at $n = 6$ the flat ray gives $c_1 \cdot 6^{-1/2} = 0.408248\,c_1 \neq 0 = \Lambda(6)/\sqrt6$.

**Lemma 2 (cocycle rigidity equivalence).** For $b \ge 0$ with $B = \mathbf{1} * b$: the increments $\Delta_p B(n) = \kappa_p$ are constant in $n$ for every $p$ **iff** $b(p^k) = \kappa_p$ for all $k \ge 1$, $b(n) = 0$ for every $n \ge 2$ that is not a prime power, and $b(1) = B(1)$ free. In particular, condition (C) ($\kappa_p = \log p$) holds **iff** $c_n = \Lambda(n)/\sqrt n$ for all $n \ge 2$.

Proof. ($\Leftarrow$) $B(n) = b_1 + \log n$, increments $\log p$. ($\Rightarrow$) Constancy gives $B(n) = B(1) + \sum_p \kappa_p v_p(n)$. Mobius-invert: $v_p = \mathbf{1} * e_p$ where $e_p(m) = 1$ iff $m = p^k$, $k \ge 1$; hence $\mu * v_p = e_p$ and $b = \mu * B = B(1)\,\delta_1 + \sum_p \kappa_p e_p$. $\square$

Machine check (exact to $1.8 \times 10^{-15}$, $n \le 5000$, all $p < 50$; and the converse with random $\kappa_p$, $n \le 2000$, error $2.7 \times 10^{-15}$): identity checks only, freeze-compliant.

**Dictionary (the cumulant reading).** The divisor lattice of $n$ is the product of chains $\prod_p \{0, \dots, v_p(n)\}$, and Mobius inversion on it is the moment-to-cumulant map. The flat ray of Lemma 1 is the product weight $\bigotimes_p (\text{geometric}_p(\beta))$ whose energy density is the Leibniz sum $\log n = \sum_p v_p(n) \log p$ (one term per site). Its site-$p$ primitive (connected, single-site) part is $(\log p)\,e_p$, and $\Lambda = \mu * \log$ is precisely the extraction of that connected part. So:

> **The von Mangoldt crystal is the first energy cumulant of the unique KMS-quasi-invariant ray, and composite pinching ($c_n = 0$ off prime powers) is the statement that mixed cumulants of an independent product vanish. Pinching = independence across the free prime generators = the Euler product, in cumulant form.**

This is the structural payload of the transport: the open core acquires a target shape (force independence), not just a target value (force $\Lambda$).

### 1.4 Disposition of the steering observations

- **O1 (shell-wise KMS at $\beta = 1/2$): REFRAMED, half costume.** The shell cocycle $c(p^{k+1}) = p^{-1/2} c(p^k)$ does hold for $k \ge 1$ ($c(8) = 0.245064 = 2^{-1/2} c(4) = 0.245064$), but FAILS at the bottom rung: $c(p) = \log p/\sqrt p \neq p^{-1/2} c(1) = 0$ ($c(2) = 0.490129$ vs $0$), and fails across shells ($c(6) = 0$ vs $2^{-1/2} c(3) = 0.448487$). The load-bearing structure is the additive cocycle (C) on the integrated comb; the exponent $1/2$ is supplied by the explicit formula's unitary normalization, not by the KMS condition. What survives of O1 and matters: the construction sits at scaling exponent $\tfrac12$, strictly inside the BC uniqueness range $\beta \le 1$ (regime separation from the killed Mechanism 2, section 4).
- **O2 (naive transport fails informatively): CONFIRMED and promoted to the central lemma pair.** Lemma 1 is the failure (named axiom, section 3); Lemma 2 is the Mobius-twisted repair the TODO predicted, made exact.
- **O3 (weights, not states): CONFIRMED, load-bearing.** $\sum_n \Lambda(n)/n = \infty$, so the crystal cannot be a normalized state at the KMS edge; it is a weight. The pole organ transports from "kills atomic states by normalization failure" to "pins the scale of the non-normalizable weight" (row (c) below). Whether BC uniqueness has a citable weights version is a real gap (P0).
- **O4 (atomicity tension): RESOLVED via O3.** The BC kill applies to NORMALIZED atomic states. The comb survives as the weight component whose scale the pole pins, coupled by (EF) to the spectral component $\mu$, mirroring BC's one-state decomposition into orbit part plus boundary part. The template, correctly transported, PREDICTS the LCC rigidity shape (atomic source comb with pinned values, spectral side carrying the rest) rather than contradicting it. This resolution is structural, not a theorem; the uniqueness engine itself is still the open core.

---

## 2. Axiom-by-axiom transport check

BC organ anatomy from #81/e2nn; one row per organ.

| BC organ | LCC counterpart | Status |
|---|---|---|
| (a) scaling action exists | $V_m$, $T_p$, $\sigma_t$ on $\mathcal{T}_{\mathbb{N}^\times}$, built from $\mathbb{N}$ alone | **HOLDS** |
| (b) quasi-invariance cocycle | literal form FAILS (Lemma 1: flat ray, wrong ray); repaired form = cocycle identity (C) on $B = \mathbf{1}*b$ | **FAILS literally / repaired precisely** |
| (c) pole = normalization-killer | pole term in (EF) = non-normalizability of the crystal; kills the dilation freedom (pins Chebyshev scale, residue 1) instead of killing the comb | **HOLDS in modified form (GAP: Tauberian lemma P1)** |
| (d) rotation density = uniformizer | $\{\log p\}$ Q-linearly independent, generating a dense subgroup of $\mathbb{R}$; forcing role unproven | **GAP (P2; K1 tripwire: Nyman-Beurling)** |
| (e) ergodicity / type III$_1$ | ratio set $\{m/n\}$ dense in $\mathbb{R}_+$: true; but the boundary is non-compact ($\mathbb{R}$, no Haar), so BC's ergodicity step has no off-the-shelf analogue | **GAP (P3)** |
| (f) uniqueness lands on the right ray | literal: lands on $\zeta$'s own comb (wrong); repaired: lands exactly on $\Lambda$ (Lemma 2), scale pinned by (c) | **HOLDS for the repaired form, conditional on (b),(c),(d)** |

**(a) HOLDS.** The action and time evolution exist canonically and are L-function-independent. $H = \log N$ encodes the crystal support positions; the cocycle value $\log p$ in (C) is the position increment, the same data BC feeds in through $\sigma_t(\mu_p) = p^{it}\mu_p$. No zero data (K1-clean).

**(b) FAILS literally, and the failure is the named negative coordinate.** BC's equilibrium object is itself quasi-invariant; the LCC target object is NOT (Lemma 1: quasi-invariant diagonal weights form exactly the flat ray; the bottom-rung witness $c(2) = 0.490129 \neq 0$ shows $\Lambda/\sqrt{n}$ violates the axiom at every prime). The repair is one Mobius twist: the crystal is the 1-cumulant OF the quasi-invariant ray, and the transported condition is (C). Note the division of labor this creates: BC uniqueness (trivial in this commutative corner: Lemma 1) pins the flat ray; the genuinely open step is that (EF)-positivity forces the crystal's multiplicative integral onto that ray's energy comb.

**(c) HOLDS in modified form.** In BC, $\sum_n n^{-\beta} = \infty$ for $\beta \le 1$ makes atomic candidates unnormalizable: the kill. Here $C(s) = \sum b_n n^{-s}$ is forced by (EF) to carry the EXACT pole of the source: the pole term $\hat g(\pm i/2)$ is fixed data, so any crystal has Chebyshev scale $\psi_b(x) = \sum_{n\le x} b_n \asymp x$ with slope pinned to the residue 1. Consequence: $\mathcal{W}_\zeta$ is an affine slice, not a cone through the origin; the pole kills the SCALING degree of freedom (in BC it killed the atomic states; in the weight world it kills the one-parameter family of rescaled ghosts). Proof obligation P1: derive the two-sided Chebyshev pinning from $b \ge 0$ plus (EF) with Fejer-type tests (the upper bound is the classical Weil-cone argument; the exact slope may need (C) first: order-of-battle is open).

**(d) GAP, with the uniformizer identified but its forcing role unproven.** BC: primes are dense in $\hat{\mathbb{Z}}^*$ (Dirichlet), forcing unit-shell uniformity on a COMPACT group with a unique invariant (Haar) measure. LCC: the counterpart ingredients are the Q-linear independence of $\{\log p\}$ (unique factorization) and density of $\sum_p \mathbb{Z}\log p$ in $\mathbb{R}$; the counterpart of "Haar is the unique invariant measure" would be a completeness/spanning statement for the dilation system $\{g(x - \log p)\}$ against the spectral side. K1 tripwire, flagged hard: FULL completeness of the dilation system is Nyman-Beurling, which is RH-equivalent; only unconditional fragments are admissible in a rigidity proof. The transported rotation organ is therefore a genuine gap, not a free import.

**(e) GAP, the structural difference named.** BC's uniqueness proof runs ergodicity of $\mathbb{N}^\times$ on $(\hat{\mathbb{Z}}, \text{Haar})$: compact boundary, unique invariant measure, type III$_1$ via ratio set $\overline{\{m/n\}} = \mathbb{R}_+$. The ratio-set ingredient transports (density of $\{\log n - \log m\}$ in $\mathbb{R}$, unconditionally true), but the boundary does not: the LCC spectral side lives on non-compact $\mathbb{R}$ with no Haar normalization, constrained only by (EF). The right replacement technology is Neshveyev-style: uniqueness of KMS states/weights = uniqueness of measures quasi-invariant under a groupoid with prescribed Radon-Nikodym cocycle (Neshveyev 2013, J. Operator Theory 70; Laca-Larsen-Neshveyev for phase transitions; Thomsen for KMS weights). The precise question to pose there: which groupoid has the property that its cocycle-quasi-invariant pairs are exactly the log-crystals? Unanswered (P3).

**(f) HOLDS for the repaired form.** Lemma 2 is exact: condition (C) lands on $c_n = \Lambda(n)/\sqrt n$ for $n \ge 2$, with two calibration leftovers, the shell values ($\kappa_p = \log p$, P2b) and the unit atom ($c_1 = 0$, P4), both enumerated below. The literal form lands on the wrong ray, which is row (b)'s failure restated.

---

## 3. Verdict

**(B), the failing axiom in one sentence: BC's quasi-invariance axiom, applied to the crystal functional itself, fails: the $T_p$-quasi-invariant rays are exactly the flat combs $c_n = c_1 n^{-\beta}$ (the comb of $\zeta(s)$, full support, wrong ray), not the positive log-crystals.**

The failure is sharp (Lemma 1, three numeric witnesses) and the replacement structure is exact (Lemma 2): the transport must run on the INTEGRATED comb through the additive cocycle identity (C), equivalently on the cumulant twist. This yields:

**LCC-KMS Transport Conjecture.** Let $(\mu, c) \in \mathcal{W}_\zeta$ (Definition 2) and $b_n = c_n \sqrt n$, $B = \mathbf{1} * b$. Then:

- **(T1) scale pinning (pole organ):** $\psi_b(x)/x \to 1$ (slope = pole residue).
- **(T2) cocycle rigidity (composite pinching, the open core):** $\Delta_p B(n) = \log p$ for all $p, n$; equivalently $c_n = \Lambda(n)/\sqrt n$ for $n \ge 2$ and $c_1 = 0$.

Consequently $\mathcal{W}_\zeta$ contains at most the von Mangoldt crystal (rigidity, LCC clause (i)), and $\mathcal{W}_\zeta \neq \emptyset \iff$ RH (attainment, clause (ii), NOT claimed here).

**Proof obligations** (each a separately attackable piece; none claimed):

- **P0 (literature gap, from O3).** A weights version of BC uniqueness at $\beta \le 1$: does "the KMS simplex is a point" extend from states to lower-semicontinuous weights normalized on a residue slice? Check against Combes/Kustermans weight theory, Thomsen's KMS-weight papers, Laca-Larsen-Neshveyev. If yes, the template is exact; if no, the residue-slice substitute in row (c) is the fallback and must be proven directly.
- **P1 (Tauberian).** $b \ge 0$ + (EF) $\Rightarrow$ two-sided Chebyshev pinning $\psi_b(x) \asymp x$ with slope exactly 1. Upper bound: classical Fejer pairing against the source. Exact slope: open; may require T2 first (order-of-battle ambiguity stated honestly).
- **P2a (the core: mixed-cumulant kill).** $b_{mn} = 0$ for coprime $m, n \ge 2$. Minimal instance: $b_6 = 0$. This IS composite pinching (#76), now with target structure: prove (EF)-positivity forces independence across prime sites. Candidate uniformizer: unconditional fragments of dilation-system density plus Q-linear independence of $\{\log p\}$; the Nyman-Beurling tripwire from row (d) applies.
- **P2b (shell calibration).** $\kappa_p = \log p$ individually. NOT implied by P1 (the slope is insensitive to perturbing finitely many $\kappa_p$); needs positivity against tests localized at $x = \log p$ coupled to the archimedean term. Open.
- **P3 (ergodicity import).** Formulate the groupoid whose cocycle-quasi-invariant pairs are the log-crystals and run a Neshveyev-type uniqueness criterion on it; this is the precise "what replaces Haar on the non-compact boundary" question.
- **P4 (unit atom).** $c_1 = 0$ forced by positivity of $\mu_c$ (a $c_1 > 0$ shifts $\mu$ by $-(c_1/\pi)\,\mathrm{Leb}$; killing it requires a local density floor argument that must not use zero locations). Small, open, LP-probeable.

**What is actually proven in this dossier:** Lemmas 1 and 2 (elementary, machine-checked, Lean-ready) and the organ mapping. The conjecture itself inherits #76's open core; the contribution is the precise transported FORM (weights, residue slice, cocycle identity, cumulant target) and the named failure of the literal axiom.

### Worked example (explicit values)

$n$: 1, 2, 3, 4, 5, 6, 8, 9, 12. $\;b_n = \Lambda(n)$: 0, 0.693147, 1.098612, 0.693147, 1.609438, 0, 0.693147, 1.098612, 0. $\;B(n) = \log n$: 0, 0.693147, 1.098612, 1.386294, 1.609438, 1.791759, 2.079442, 2.197225, 2.484907. Cocycle checks: $B(6) - B(3) = 0.693147 = \log 2$; $B(12) - B(6) = 0.693147 = \log 2$; $B(9) - B(3) = 1.098612 = \log 3$. Comb values $c_n = \Lambda(n)/\sqrt n$: $c_2 = 0.490129$, $c_3 = 0.634257$, $c_4 = 0.346574$, $c_6 = 0$, $c_8 = 0.245064$. Shell cocycle (O1, interior): $c_8 = 2^{-1/2} c_4$ exact. Bottom-rung anomaly: $c_2 = 0.490129 \neq 2^{-1/2} c_1 = 0$. Cross-shell failure: $c_6 = 0 \neq 2^{-1/2} c_3 = 0.448487$. Flat-ray contrast at 6: $6^{-1/2} = 0.408248 \neq 0$.

### Function-field anchor (K3 sanity)

Over $\mathbb{F}_q$ the same divisor-lattice structure is the point-count identity $N_k = \sum_{d \mid k} d\,a_d$: the integrated comb is the point count, Mobius inversion extracts the closed-point ("prime") data, and e2ll (#79) proved both the exactness (all $a_d$ nonnegative integers) and the cone uniqueness (flat extension). The cumulant reading (pinching = independence across places) is consistent with the proven FF case; the analogy is an anchor, not a proof.

---

## 4. Honesty block

- **K1 (no zero data): CLEAN.** Every defined object (comb space, $\mathcal{T}_{\mathbb{N}^\times}$, $V_m$, $\sigma_t$, $B$, condition (C), the pole residue, $\Omega(r)$) is source-side. $\mu$ is a variable of the cone, never instantiated with zeros. Zeros appear only in the STATEMENT "attainment $\iff$ RH". The rigidity conjecture is not RH-equivalent by itself: rigidity plus an empty cone is consistent with RH-false (#76's clause separation preserved). One K1 tripwire is live and flagged in rows (d)/P2a: importing FULL dilation completeness would smuggle in Nyman-Beurling = RH.
- **D-H discipline: SAFE, with the precise behavior stated.** The ambient machinery (Definitions 1, 3, 5) is built from $\mathbb{N}$ and runs for any source. For the Davenport-Heilbronn source the analogue of (EF) has NO pole term and archimedean density $\approx -0.099$ at $r = 0$, and the Fejer-test pairing of #76 certifies the D-H crystal cone is EMPTY (a provable lemma, stealth-window independent). So the construction does not produce a false D-H-RH proof: the transported uniqueness statement degrades to "cone = $\emptyset$" for D-H versus "cone = $\{\Lambda\}$" for zeta, and the KMS/cocycle layer never engages because there is no crystal to act on. The Euler-specific organs (free prime generators, product/cumulant structure) additionally have no D-H counterpart (no Euler semigroup: the #55 firewall class), matching e2nn's "constructionally undefined" status for the BC mechanism itself.
- **Distinction from the killed Mechanism 2** ([building_the_missing_positivity.md](building_the_missing_positivity.md)), on all three demanded axes. (1) Regime: Mechanism 2 lived at $\beta > 1$ (normalizable Gibbs states, $\zeta(\beta) < \infty$); this construction lives at scaling exponent $\tfrac12$, strictly inside the non-normalizable uniqueness range $\beta \le 1$, in the WEIGHT category (O3). (2) Object: Mechanism 2 used the modular operator $\Delta^{1/2}$ of the product state as a zero-side POLARIZATION; here the object is the source-side cone $\mathcal{W}_\zeta$ and the claim shape is "simplex is a point", with no polarization and no signature claim. (3) Claim type: Mechanism 2's content was "$Q_b \ge 0$ iff RH" (adversary verdict: RH-restated, all content in the archimedean counterterm); here the conjectured conclusion is $c = \Lambda$ (rigidity), unconditional if proven, with the RH-equivalent attainment clause explicitly fenced off and NOT claimed.
- **Soft-detector freeze: respected.** No positivity margins are cited as evidence anywhere. The only numerics are exact identity checks of Lemmas 1-2 ($\le 2.7 \times 10^{-15}$) and the worked-example values.
- **What this does NOT do.** It does not prove composite pinching (P2a is the same open core as #76, reorganized); it does not touch the zero side (the #42 continuation wall stands; nothing here reaches $\mathrm{Re}\,s \le 1$); it does not establish the weights version of BC uniqueness (P0 is a literature gap); it does not show the flat comb is infeasible (if the flat comb WERE in $\mathcal{W}_\zeta$, LCC rigidity would be falsified: that is adversarial target A2); and it does not advance M4/AX-POL directly. [SYNTHESIZER update 2026-06-11: A2 is no longer live; the ADVERSARY report block 3 proves the flat comb infeasible for every $c_1 > 0$, see e3hh.]

---

## 5. Next step

**The single highest-value follow-on: extend the queued LCC LP (e3x, TODO line 155) with the two probes this dossier makes available, before any literature work.**

- **(d) flat-comb ghost probe (the cheapest kill of LCC itself):** test truncation-feasibility of the Lemma 1 ray $c_n = n^{-1/2}$ (scale set by the pole residue). Persistent feasibility under refinement = a ghost crystal = LCC rigidity dead, and this transport with it. Persistent infeasibility = the first evidence that (EF)-positivity rejects the quasi-invariant ray, i.e. that the cumulant twist is forced, exactly what P2 needs. [SUPERSEDED 2026-06-11: settled analytically by the ADVERSARY report block 3 and `e3hh_flat_comb_ghost.py`; the flat comb is provably infeasible, do not run this probe.]
- **(e) calibration probes for P2b/P4:** maximize $|\kappa_2 - \log 2|$ and $c_1$ over the truncated cone; shrinking margins under refinement localize whether shell calibration and the unit atom are LP-visible or need the archimedean coupling.

Second priority (literature, P0/P3): the KMS-weight uniqueness question for BC at $\beta \le 1$ (Thomsen; Laca-Larsen-Neshveyev; Neshveyev's groupoid criterion), posed as: which groupoid has the log-crystals as its cocycle-quasi-invariant pairs?

## 6. Handoff: verification targets and adversarial test cases

**VERIFIER (Lean 4 / Mathlib targets, in order of feasibility):**

- **V1 (Lemma 2).** For `b : ArithmeticFunction ℝ`, `B = zeta * b`: `(∀ p n, p.Prime → B (p*n) - B n = Real.log p) ↔ (∀ n ≥ 2, b n = Λ n)` with `b 1` free. Mathlib has `ArithmeticFunction.vonMangoldt`, `moebius`, and `vonMangoldt_mul_zeta` (i.e. $\Lambda * \zeta = \log$); the new content is the converse via $\mu * v_p = e_p$.
- **V2 (Lemma 1).** `(∀ p n, c (p*n) = p^(-β) * c n) → ∀ n, c n = c 1 * n^(-β)`. Induction on factorization.
- **V3.** `b ≥ 0 → ∀ p n, B (p*n) ≥ B n` (increment nonnegativity).

**ADVERSARY (configurations to attack):**

- **A1.** The $c_6$ floor (e3x run (b)): a persistent floor kills T2/P2a and the conjecture.
- **A2.** The flat-comb ghost (section 5(d)): feasibility of $c_n = n^{-1/2}$ kills LCC rigidity outright. Highest-value single attack.
- **A3.** $\kappa_2$ perturbation: a feasible comb with $\kappa_2 \neq \log 2$ at all truncations breaks P2b and shows the conjecture over-claims shell calibration.
- **A4.** D-H regression: confirm the Fejer-dual emptiness certificate (#76) runs; if any positive D-H crystal is exhibited, the firewall and this transport both fall.
- **A5.** Unit-atom probe: a truncation-stable crystal with $c_1 > 0$ breaks P4 and Lemma 2's calibration to the exact von Mangoldt crystal.

**Cross-references.** #76 (LCC definition, D-H firewall lemma, composite-pinching core), #79/#80 (the transfer gap this targets), #81/e2nn (the BC template and organ anatomy), #55 (firewall class), #42 (continuation wall, respected), #63 (the $e^\gamma$ marginality rate at the pole, expected to reappear as the convergence rate of any proof of P1). Literature: Bost-Connes 1995 (Selecta Math 1); Laca-Raeburn 2010 (Adv. Math 225, phase transition on $\mathcal{T}(\mathbb{N} \rtimes \mathbb{N}^\times)$); Neshveyev 2013 (J. Operator Theory 70, KMS states via quasi-invariant measures with prescribed cocycle); Laca-Larsen-Neshveyev (JFA 2011, Hecke/semigroup phase transitions); Combes 1971 / Kustermans-Vaes (weight theory); Thomsen (KMS weights, J. Operator Theory / ETDS); Rota (Mobius functions and the foundations of combinatorial theory, for the lattice-cumulant reading).

---

## ADVERSARY report (2026-06-11)

**VERDICT: UPHELD-WITH-REVISIONS.** No false mathematical statement found; Lemmas 1-2 verified independently; the D-H story and the Mechanism-2 separation are honest. Three revisions are mandatory: (1) the "LCC-KMS Transport Conjecture" must be labeled a restatement of #76 LCC clause (i), not a new conjecture; (2) kill switch A2 is now SETTLED ANALYTICALLY in the construction's favor (the flat comb is provably infeasible for every $c_1 > 0$; see block 3 and [`e3hh_flat_comb_ghost.py`](../../experiments/positivity/e3hh_flat_comb_ghost.py)), so section 5(d) and adversarial target A2 are superseded by a theorem; (3) P1's status is overstated as open: its smoothed form follows unconditionally from temperedness of $\mu$ via translate-bump pairing, and P1 does NOT need T2 first.

### 1. Vacuity / renaming attack: the conjecture IS clause (i); the residual value is real but smaller than the framing

**Finding: the "transport conjecture" is mathematically identical to #76 LCC rigidity.** T2 says every crystal satisfies (C); Lemma 2 says (C) $\iff c_n = \Lambda(n)/\sqrt n$ ($n \ge 2$); Definition 2 says $c$ determines $\mu$. Composing: T2 $\iff$ LCC clause (i) plus the $c_1 = 0$ calibration. The conjecture adds zero mathematical content over #76. Item by item:

- **Renamed:** (C) $\iff \Lambda$ is the classical inversion pair $\Lambda * \mathbf{1} = \log$, $\mu * \log = \Lambda$ (Lemma 2's converse is mildly less standard but elementary). The cumulant dictionary is Rota-classical (Mobius inversion on a product of chains = moment-to-cumulant). "Pinching = independence" renames "$\Lambda$ supported on prime powers = Euler product"; no theorem class with a proof engine is identified that takes "(EF)-positivity" as input and outputs "mixed cumulants vanish". It is a target shape, not a handle.
- **Idle costume:** the operator-algebra layer (Definitions 3-4, $\mathcal{T}_{\mathbb{N}^\times}$, $\sigma_t$) does no work in anything proven. Lemma 1 kills the only genuinely C*-algebraic statement (quasi-invariance of $w_c$), and the repaired condition (C) is pure Dirichlet convolution, never re-expressed as a KMS or groupoid condition. The title's "the log-crystal cone as a KMS-weight simplex" is NOT delivered; per TODO line 162 the dossier delivers the second branch ("a precise statement of which BC axiom fails"), which is legitimate, but the framing should say so.
- **Genuinely new:** (a) Lemma 1 as a sharp negative coordinate (the quasi-invariant rays are flat, so any BC-templated uniqueness must act on $B = \mathbf{1}*b$); (b) the identification of the flat comb as the canonical ghost candidate, now settled (block 3): the first unconditional exclusion of a ghost family from the zeta cone; (c) the P0-P4 decomposition as separable obligations, with P1 essentially closable now (block 2 end); (d) the Neshveyev/Thomsen pointers (P0/P3), real but unexecuted.

### 2. Math check: Lemmas verified; machine check was unarchived, now reproduced; P1 status corrected

- **Lemma 1: correct.** $n = 1$ specialization gives $c_m = m^{-\beta} c_1$; the flat ray conversely satisfies $c_{mn} = m^{-\beta} c_n$. The Definition 4 reading on diagonal weights ($c_{mn} = m^{-\beta} c_n$) was re-derived and is right.
- **Lemma 2: correct, quantifiers correct** ((C) over ALL $p$ and ALL $n \ge 1$ is exactly what the $\Rightarrow$ proof uses). Independently re-verified in [`e3hh_flat_comb_ghost.py`](../../experiments/positivity/e3hh_flat_comb_ghost.py) part [1]: forward ($\mu * \log = \Lambda$, $n \le 10^4$) max error $4.4 \times 10^{-15}$; converse (random $\kappa_p$ for all $p \le 10^4$) max error $3.8 \times 10^{-15}$, $b(1)$ recovered free. Consistent with the dossier's claimed $1.8/2.7 \times 10^{-15}$, which had NO script in the repo; that check is now archived. Minor nit: the hypothesis $b \ge 0$ in Lemma 2 is unnecessary (the equivalence is sign-free; positivity is only needed for the $\Delta_p B \ge 0$ remark).
- **Unit atom (P4): consistent.** Lemma 2 leaves $b(1)$ free, T2 adds $c_1 = 0$ through P4, and P4's claim that a unit atom shifts $\mu$ by $-(c_1/\pi)\,\mathrm{Leb}$ checks out ($-2c_1 g(0) = -(c_1/\pi)\int \hat g\,dr$).
- **Worked example: all values verified** (including the O1 interior/bottom-rung/cross-shell numbers).
- **Correction to P1's status.** The dossier marks P1 open with "the exact slope may need (C) first". False: pair (EF) with $g_T(x) = \varphi(x-T) + \varphi(x+T)$, $\varphi \in C_c^\infty$ even. For any crystal, $|\int \hat g_T\,d\mu| \le 2\int |\hat\varphi|\,d\mu < \infty$ uniformly in $T$ ($\mu$ tempered), the archimedean term is $O(1)$, and the pole term is exactly $\hat g_T(i/2) + \hat g_T(-i/2) = 4\cosh(T/2)\int\varphi(u)\cosh(u/2)\,du$; so the windowed comb mass obeys $2\sum_n c_n\,\varphi(\log n - T) = 4\cosh(T/2)\int\varphi(u)\cosh(u/2)\,du + O(1)$, i.e. smoothed two-sided Chebyshev pinning with slope exactly the residue 1, unconditionally. With $b \ge 0$ the standard monotonicity sandwich upgrades smoothed to sharp $\psi_b(x) \sim x$. P1 does not need T2; the order-of-battle ambiguity is resolved. (Numerical shadow: e3hh part [5], where the translate-bump pairing matches the predicted pole atom to relative $5 \times 10^{-5}$ at $T = 10, 14$.) Note this does NOT trivialize PNT: it is a statement about cone members, and membership of the von Mangoldt crystal (attainment) is the RH-equivalent clause.

### 3. Kill switch A2: DEFUSED by derivation. The flat comb is infeasible for every $c_1 > 0$

This settles the dossier's "highest-value single attack" analytically, replacing the proposed LP probe (section 5(d)) with a proof. Perron contour shift (residue of $\zeta$ at $s = 1$) gives, for even $g \in C_c^\infty$:

$$\sum_{n\ge1} n^{-1/2} g(\log n) \;=\; \hat g(-i/2) + \frac{1}{2\pi}\int_{\mathbb{R}} \hat g(r)\,\zeta(\tfrac12 + ir)\,dr,$$

(machine-verified to $4 \times 10^{-16}$, e3hh part [2]). Substituting the flat comb $c_n = c_1 n^{-1/2}$ into (EF), the right side decomposes as

$$\mathrm{RHS}(g) \;=\; 2(1 - c_1)\,\hat g(i/2) \;+\; \frac{1}{2\pi}\int_{\mathbb{R}} \hat g(r)\,\big[\Omega(r) - 2 c_1 \mathrm{Re}\,\zeta(\tfrac12 + ir)\big]\,dr.$$

- **Case $c_1 \ne 1$ (scale not pinned): infeasible.** On translate bumps $g_T = \varphi(\cdot - T) + \varphi(\cdot + T)$ the residual atom grows like $4(1-c_1)\cosh(T/2)\int\varphi\cosh(u/2)$, while $\int \hat g_T\,d\mu$ is bounded uniformly in $T$ for ANY positive tempered $\mu$ and the archimedean term is $O(1)$. Equality fails for large $T$. (e3hh part [5]: computed RHS $151.531$ and $1119.671$ at $T = 10, 14$ against predicted atoms $151.538$ and $1119.672$; growth ratio $7.389 = e^2$ exactly.) This is also the flat-family instance of T1: the pole pins $c_1 = 1$.
- **Case $c_1 = 1$ (the dossier's probe value): infeasible.** The atom cancels and the induced spectral density is $\frac{1}{2\pi}[\Omega(r) - 2\mathrm{Re}\,\zeta(\tfrac12 + ir)]$, whose value at $r = 0$ is $\frac{1}{2\pi}(\Omega(0) - 2\zeta(\tfrac12)) = \frac{1}{2\pi}(-5.3721834 + 2.9207090) = \frac{-2.4514744}{2\pi} < 0$. Mollified Fejer tests $g_X$ ($\hat g_X \ge 0$ on $\mathbb{R}$) concentrate at $r = 0$, forcing $\int \hat g_X\,d\mu < 0$: contradiction with positivity. Direct (EF) witnesses computed WITHOUT the Perron identity (pure pole-comb-archimedean balance, e3hh part [4]): $\mathrm{RHS}(g_X) = -2.397, -2.415, -2.424$ at $X = 8, 12, 16$, against limit $-2.4515$, with the pole cancellation running through $1.5 \times 10^3$ at $X = 16$; cross-checked against the spectral form at $X = 8$ ($-2.3968$ vs $-2.3976$).
- **Mechanism, stated structurally:** the pole organ pins the flat ray's scale to $c_1 = 1$ (exactly the BC normalization-killer in weight form, row (c)), and then the archimedean trough $\Omega(0) \approx -5.372$ rejects it: the flat comb supplies only $2|\zeta(\tfrac12)| \approx 2.921$ of density at $r = 0$, short by $2.451$. This is the SAME Fejer-trough mechanism as the #76 D-H emptiness lemma, now firing inside the zeta cone against the wrong comb. The von Mangoldt comb must (and, by exactness of the explicit formula, does) cancel the trough to exactly $0$ at $r = 0$, since $\mu_*$ has no mass below $\gamma_1$: marginal positivity at its sharpest.
- **Scope guard:** this excludes the one-parameter quasi-invariant family, NOT the whole cone. It is the first unconditional ghost-kill in $\mathcal{W}_\zeta$ and the first concrete instance of "(EF)-positivity rejects the quasi-invariant ray" (what P2 needs), but it is not composite pinching: $b_6 = 0$ (P2a) remains open. K1-clean: no zero locations used anywhere ($\zeta(\tfrac12 + ir)$ is source-side continuation data, same status as $\Omega(r)$; the density's first sign change at $r \approx 13.14$ is NOT $\gamma_1 = 14.13$ and no zero entered the computation).

### 4. D-H discipline: SAFE as claimed, with one structural warning made explicit

The walk-through confirms the dossier. (i) The D-H (EF) analogue has no pole term and archimedean trough $\approx -0.099$ at $r = 0$ (#76), so the same Fejer pairing as block 3 (with pole $= 0$ and comb contribution $\le 0$ for $c \ge 0$, $g \ge 0$) certifies the D-H cone is empty; the KMS/cocycle layer never engages. (ii) Imposing the repaired axiom (C) on a "D-H comb" is syntactically possible and lands on $\Lambda$ regardless: (C) is L-FUNCTION-BLIND (built from $\mathbb{N}$ alone, like the whole Definition 3-5 layer). This is not a kill, because rigidity-over-an-empty-cone is vacuous and the attainment clause (the only RH-bearing clause) fails for D-H; no false D-H-RH is derivable. But it sharpens a discipline rule for the follow-on work: **any future proof of T2 must consume the (EF) data (pole term and $\Omega$) somewhere essential, because the scaling-action formalism and condition (C) are identical for every source; a T2 "proof" that never touches the pole or the archimedean density is structurally wrong by construction.** Block 3's mechanism (pole pins, trough rejects) is the existence proof that the (EF) data suffices to do real work.

### 5. Killed-costume check: the Mechanism 2 separation is real on all three axes

Verified against [building_the_missing_positivity.md](building_the_missing_positivity.md): Mechanism 2 lived at $\beta > 1$ (normalizable Gibbs, $\zeta(\beta) < \infty$), used the Tomita modular operator of the product state as a zero-side polarization, and claimed an RH-iff ($Q_b \ge 0$), dying because $\Delta$ is strictly PSD and all content sat in the archimedean counterterm. This dossier: exponent $\tfrac12$ in the weight regime $\beta \le 1$, source-side cone, claim shape "simplex is a point", no polarization, RH-equivalence fenced into attainment and not claimed. All three demanded axes check. Note the instructive inversion: in Mechanism 2 the archimedean term was where circularity hid; in block 3 the archimedean trough does unconditional REJECTING work. Soft-detector freeze: respected by the dossier (identity checks only) and by e3hh (infeasibility certificates, the falsification direction; the limit value $\Omega(0) - 2\zeta(\tfrac12)$ is exact analytic data, not a float margin). K1: clean throughout (block 3 scope guard).

### 6. Style gate: PASS

No em dashes (U+2014) or en dashes (U+2013) found in the dossier; nothing to fix.

### Disposition for ORCHESTRATOR

- Section 5(d) and adversarial target A2 are superseded: replace the e3x flat-comb LP probe with the e3hh theorem; keep e3x runs (b) (the $c_6$ floor, P2a) and (e) (calibration probes, P2b/P4), which remain open and are now the only live LP targets.
- BUILDER follow-on with the best ratio of effort to payoff: write up block 3 + the P1 closure as a short unconditional lemma pair ("every crystal has slope 1; the flat ray is not a crystal"), Lean targets alongside V1-V3. The genuinely open core is unchanged: P2a ($b_6 = 0$), now with one proven instance of the rejection mechanism to imitate.

---

## SYNTHESIZER update (2026-06-11, post-survey and post-stress-round)

The same-day follow-ons settled four of the open items above; see [kms_weights_p0_p3_survey.md](kms_weights_p0_p3_survey.md) (LEARNINGS #85) and the e3x/e3x2 instrument thread (LEARNINGS #83/#84).

- **P0 is CLOSED.** Christensen (arXiv:2005.01792, JNCG 2023): on unital C*-algebras every KMS weight is a scalar multiple of a KMS state; with Bost-Connes 1995 the KMS-$\beta$ weight ray at $\beta \le 1$ is unique. Stronger: Neshveyev-Stammeier (arXiv:1912.03141, Thm 4.5) prove the ambient $\mathcal{T}_{\mathbb{N}^\times}$ of Definition 3 has a ONE-POINT KMS simplex at every $\beta > 0$, and their Prop 3.8 independently re-derives Lemma 1's flat ray.
- **P3 is CLOSED NEGATIVELY, and row (e)'s GAP is resolved by reclassification.** No etale groupoid has the log-crystals as its cocycle-quasi-invariant data: (EF) is INHOMOGENEOUS (the pole term makes $\mathcal{W}_\zeta$ an affine slice; quasi-invariance cuts a homogeneous cone) and FOURIER-NONLOCAL (atom-to-continuum coupling; quasi-invariance is orbit-local transport). So $\mathcal{W}_\zeta$ = (groupoid KMS cone) $\cap$ (EF slice) and ALL rigidity lives in the slice. The "find the LCC groupoid" search is killed as a category error. Constructive residue: BUILDER B1, the dense-translate rigidity lemma on $G_{\log} = \mathbb{R} \rtimes \mathbb{Q}^*_+$ (queued in TODO).
- **Row (c)'s P1 was closed unconditionally by the ADVERSARY report block 2** (translate-bump pairing; slope = residue 1).
- **The e3x instrument data on P2a/P2b/P4** (#83, corrected by #84): the kappa_2 squeeze onto $\log 2$ (P2b) is the strongest LP survivor; P2a ceilings are tolerance-proportional ($c_6 \approx 3\varepsilon$, intercept $\sim$0.01-0.02, kill not armed); P4 is tolerance-bound, undecided. New discipline rule from the stress round: signed test families are D-H-blind, so any LP family must contain $\hat g \ge 0$ tests.
- **Bottom line after one day of follow-ons:** the operator-algebra leg is fully priced (it delivers flat-ray uniqueness three independent ways and cannot reach the slice); the open core P2a/P2b/P4 is wholly an explicit-formula positivity problem.
