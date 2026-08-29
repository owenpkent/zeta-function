# F2b: the visibility-floor law over the certificate class

> **Status: BUILDER deliverable, frame session F2b (2026-08-28), the funding-boundary
> frame's fourth session, executed under exit 2's binding deadline
> ([`successor_frame_deliberation.md`](successor_frame_deliberation.md) Section 6;
> [`funding_boundary_audit_1.md`](funding_boundary_audit_1.md) Q3). Foundation: the
> DELTA-CHECKED class definition [`f2a_certificate_class.md`](f2a_certificate_class.md)
> (PASS_WITH_EDITS, edits 1-7 applied;
> [`_f2a_delta_check.md`](_f2a_delta_check.md)), frozen for this document.** This is the
> re-aimed target (a) of LEARNINGS #211(iv), with target (b) carried as the endpoint
> corollary: the QUANTITATIVE visibility-floor law, stated at both co-primary registers
> per delta-check edit 6. The bar it must meet (exit 2 / the Section 5 bar as repaired
> by the deliberation's adversary A1): proven modulo NAMED analytic hypotheses, finite
> skeleton VERIFIER-drafted with the hypothesis load priced, and the derivability check
> run on the contrapositive. Companion artifacts: the calibration build
> [`../../experiments/spectral/e1ag_visibility_curve.py`](../../experiments/spectral/e1ag_visibility_curve.py)
> and the Lean statement skeleton
> [`../../lean/ZetaRH/F2bSkeleton.lean`](../../lean/ZetaRH/F2bSkeleton.lean). The
> same-session ADVERSARY report grading this document:
> [`_f2b_adversary.md`](_f2b_adversary.md). **Post-adversary status (2026-08-28):
> verdict PASS_WITH_FIXES; all ten blocking fixes (F1-F10) applied in-session by the
> bounded fix pass, each tagged "session adversary F$N$" in place (F1 the STANDARD
> hypothesis with the $G^{\sharp}$ boundary case; F2 the (P-M) hypothesis with the
> wild-$M$ construction; F3 the complex-read convention; F4 the regime condition plus
> the unconditional $k = O(1)$ sub-case; F5 the batch-selection form of L4; F6 the
> unit-resolution count in L5; F7/F8/F9 the Lean repairs, re-typechecked clean with
> exactly one sorry; F10 the $N$ correction). Grade per the #206 wiring:
> non-UNMOVED, carried by M2 (the two-sided resolution frontier) at its narrowed
> scope; exit 2 does NOT fire (outcome (a) as scoped, per the report's Section 7).**
> No em dashes anywhere.

**One sentence.** Over the certificate class $\mathcal{C}$, granted correlation data
buys exactly two things, at two separate prices: its absolute SLACK $\varepsilon(T)\,TL$
sets the certifiable defect floor (the $E$ and $N_{\mathrm{off}}$ counts, linearly,
sharp on both sides), and its link SUPPORT $\Theta(T)$ sets the location-resolution
frontier ($\delta^* = (1+o(1))\log(TL)/\Theta$, two-sided, with a thin priced band);
the two purchases decouple to first order, the absolute register ($E < 2$,
$N_{\mathrm{off}} \equiv 0$) sits below every floor at every granted profile, and the
theorem is the CURVE, not that endpoint.

---

## 0. Conventions, fixed once (per the class definition, Section 7 item 7(b))

GLSS conventions throughout
([`reading_notes/glss_full_funding_boundary.md`](reading_notes/glss_full_funding_boundary.md)
Section 1.1): zeros as a multiset; $L = \frac{1}{2\pi}\log T$; $N(T)$ counts
$0 < \gamma \le T$ with multiplicity, $N(T) = TL + o(TL)$ under the C0 frame;
$N(\lambda)$ counts ordered pairs at positive rescaled gap $0 < (\gamma'-\gamma)L \le
\lambda$ (equal ordinates excluded); $N^{\circledast}(T)$ counts ordered pairs with
$\gamma = \gamma'$ including self-pairs, so $N^{\circledast} = \sum_{\text{lines}} h^2$
and $E(T) := N^{\circledast}(T) - N(T) = \sum_{\text{lines}} h(h-1)$; windowing $[0,T]$.
Strip closed $0 \le \beta \le 1$ (C0's convention; the delta-check's note-only flag on
open vs closed is accepted and this document holds the closed convention). "Rescaled
gap" always means $(\gamma'-\gamma)L$. For link families, $\Theta$ denotes the
exponential type of $g(z) := f_T(\tfrac12 + iz)$ (equivalently the log-support: the
support-$\Delta$ profile has $\Theta = \Delta \log T$), and every link family is
sup-normalized $\sup_{t \in \mathbb{R}}|f_T(\tfrac12+it)| \le 1$ with $o(TL)$ absolute
slack (delta-check edits 1-3, load-bearing below).

## 1. The granted profile of a grant set (the curve's coordinates)

Fix a jointly satisfiable grant set $G \subset \mathcal{P}$ (the class quantifier,
re-pose fix 3), with the proven core always riding. The curve is stated against three
profile scalars, each read off $G$'s own stated clauses:

- **D1 (slack).** Each family $i \in G \cup \mathrm{core}$ carries an absolute error
  profile $\epsilon_i(T) \cdot (\text{normalization}_i)$: conjectural grants at
  $\varepsilon_i(T)\,TL$ with $\varepsilon_i \to 0$ (unquantified allowed; then
  $\varepsilon_i$ is a symbol and the curve's statements are o-statements), proven core
  members at their proven classes (Fujii $O(T\sqrt{\log(2+\lambda)})$ per window, MV
  budgets, BGSTB $O(1/\sqrt{\log T})$ at its normalization).
- **D2 (exchange constants; the STANDARD hypothesis).** Each family prices one MERGE
  EVENT (Section 2): its per-event cost $c_i$ under the moves of D3. The family's
  slack in $E$-units is $2\varepsilon_i TL / c_i$. Define the grant set's **slack
  floor** $\varepsilon_G(T)\,TL := \min_i\, \varepsilon_i(T)\,TL / c_i$ over all
  granted and core families. A battery is **STANDARD** if it has finitely many
  granted families with per-event costs $c_i = O(1)$ uniformly; then
  $\varepsilon_G \asymp \min_i \varepsilon_i$. Standardness is a NAMED HYPOTHESIS of
  Theorem 1, not a reassurance (session adversary F1): the graded boundary case
  $G^{\sharp} = \{\sum_{\mathrm{lines}} h^n = N + o(TL) : n \ge 2\}$ is admissible
  (each member has fixed arity and sup-normalized kernel) but not standard (countably
  many families with $c_n = 2^n - 2$ unbounded), has $\varepsilon_G = 0$, and marks
  honestly where the curve's floor range closes.
- **D3 (support).** $\Theta_G(T) :=$ the largest exponential type among $G$'s link
  families ($0$ if none beyond the core; the proven core's link members sit at support
  $\le 1$, i.e. $\Theta \le \log T$, per the e1af Section 2 wall and the BGSTB row).
  The prime channel's role is exactly the FUNDING of $\Theta_G$: support $1+\delta$
  link evaluations consume the shift family $\{B_X(h) : h \le T^{\delta}\}$ at weight
  $\log(H/h)$
  ([`../../experiments/spectral/e1af_funding_wall.md`](../../experiments/spectral/e1af_funding_wall.md)
  Section 2), so the curve's support axis is priced in prime-grant currency and the
  slack axis in error-class currency: the F1 funding wall and the F2 information wall
  are the two AXES of one object.

**The moves (the in-class counterexample family, inherited from F2a and here made
quantitative).** All three perturb a $G$-matching base $Z_0$ and inherit core plus $G$
whenever their total cost stays below every family's slack (the adversary's seeding
trick, [`_f2a_class_adversary.md`](_f2a_class_adversary.md) A4(ii)).

- **(M) merge**: $k$ disjoint on-line pairs at rescaled gap $s$, each moved to its
  common midpoint ordinate: $E \mathrel{+}= 2k$, $N_{\mathrm{off}}$ unchanged, $N$
  unchanged.
- **(S) split**: an on-line double at $\tfrac12 + i\gamma$ replaced by the FE pair
  $\{\tfrac12 \pm \delta + i\gamma\}$: every marginal functional EXACTLY invariant,
  $N_{\mathrm{off}} \mathrel{+}= 2$, $E$ unchanged.
- **(I) inject**: FE-paired points added at rate $k(T) \ll \log T$ inside the $S$
  budget ($o(\sqrt{\log\log T})$ if Selberg-class moments ride the core). Not needed
  for the floors below ((M)+(S) suffice on any base with $\gg k$ on-line zeros, and a
  base violating that has $E \ge cN$ already); kept for the record.

## 2. The cost lemmas (finite; the exact envelope; the one genuinely new lemma)

**L1 (register lemmas).** V-F2a-1 through V-F2a-4 of the class definition Section 8:
parity ($E < 2 \iff E = 0$), monotonicity, the conversion
$\#\{\text{simple critical}\} \ge 2N - N^{\circledast}$, the domination
$N_{\mathrm{off}} + N_{\mathrm{mult}} \le E$. Checked by the F2a adversary (A5) and
re-checked by the delta-check Section 4; drafted in the Lean skeleton.

**L2 (per-event costs, by channel).** Let one (M) event act on a pair at rescaled gap
$s$, and one (S) event act at displacement $\delta$ under a link family of type
$\Theta$.

- **L2a (marginal, decaying kernels).** For a 2-point family with kernel $K$,
  $\sup|K| \le 1$, of bounded local mass $\mu_K := \sup_x \sum_{j}
  \mathrm{osc}_{[x+j, x+j+1]} K < \infty$: one (M) event changes the read by at most
  $C\mu_K$ (the moved zeros' gap set shifts by $\le s/2$ rescaled; boundary crossings
  $O(1)$ at unit density). For the canonical pair count $N(\lambda)$, $\lambda > s$:
  the change is EXACTLY $-1$ plus boundary crossings (the merged pair leaves the
  equal-excluded count). Fixed arity $n$: the same with $C(n)$.
- **L2b (link, on-line second difference; named input: Bernstein).** $g$ entire of
  exponential type $\Theta$, $\sup_{\mathbb{R}}|g| \le 1$; the (M) event's link cost is
  the second difference at half-spacing $s/(2L)$:
  $|g(\gamma_1) + g(\gamma_2) - 2g(\gamma_m)| \le \min\big((s\Theta/(2L))^2,\, 4\big)
  = \min\big((\pi \Delta s)^2,\, 4\big)$, the first branch by Bernstein's inequality
  ($\sup|g''| \le \Theta^2 \sup|g|$), the second the trivial sup-norm cap, which is
  what the delta-check's sup-normalization pin (edits 1-3) buys: EVERY link cost is
  $\le 4$ per event at every support, and merges at gap $s \le 1/(\pi\Delta)$ cost
  $\le 1$ even at the largest granted support.
- **L2c (link, split cost; the EXACT envelope).** By Paley-Wiener,
  $g(\gamma - i\delta) + g(\gamma + i\delta) - 2g(\gamma) = \int \hat g(u)\,
  e^{i\gamma u}\, 2(\cosh(\delta u) - 1)\, du$; the type/Phragmen-Lindelof bound gives,
  with no Fourier-mass hypothesis,
  $|{\cdot}| \le \min\big( (\delta\Theta)^2 e^{\delta\Theta},\ 2(e^{\delta\Theta}+1)
  \big)$. For the height-windowed exponential family ($f_x(s) = x^{s - 1/2}$,
  $\Theta = \log x$) the per-event cost is EXACTLY
  $2(\cosh(\delta \log x) - 1)\,|\phi\cos|$-weighted: the e2ax measured envelope
  $4(\cosh(\delta u) - 1)$ (LEARNINGS #192) is this identity's zeta instance, and its
  measured detector curve $U^*(\delta) = 1.41/\delta$ back-solves to a detection
  threshold $2(\cosh(1.41) - 1) \approx 2.35$: the class curve's constant, measured in
  2026-08 before this document existed.
- **L2d (marginal split cost).** Exactly $0$: the (S) invariance (the marginal sees
  defect mass, never its location split; the delta-check edit 6 register clause).
- **L2e (core costs).** Fujii's functional: one (M) event changes $S(t)$ by $\pm 1$ on
  two intervals of total measure $s/L$, so
  $\Delta \int_0^T (\Delta_U S)^2\,dt \ll (s/L)\sqrt{\log(2+UL)}$ per event: the core
  never binds before the granted slack (the change lives on the MOVED measure, not the
  window measure).

**L3 (slack bootstrap: positioning is the only cost).** Given matching $Z_0$ and any
$k \le c_1 \varepsilon_G TL$: first POSITION $k$ disjoint adjacent on-line pairs at gap
$s(T) \to 0$ (cost per event per family $\le C_{\mathrm{bat}}$: by L2a for decaying
marginal kernels and by L2b's sup-norm cap $\le 4$ for link families: total
$\le C_{\mathrm{bat}} k \le$ half of every slack for $c_1 = 1/(2 C_{\mathrm{bat}})$),
then MERGE at gap $s(T)$: the merge step costs $|K(s) - K(0)|$ per marginal read
(continuity: $\to 0$) and $(\pi\Delta s)^2 \to 0$ per link read. The floor's engine is
exactly the #172 obstruction (continuous functionals cannot see a dense-in-gaps
degeneration) promoted from a pointwise statement to the class's counterexample
calculus: arithmetic-free, granted-law-free, paid once in positioning. Non-decaying
resonance families are the one exception to the $O(1)$ accounting and are L4's
subject.

**L4 (site selection under resonance families; the new lemma this theorem needs and
proves).** L2a covers decaying kernels. The discipline's syntax also admits bounded
NON-decaying kernels (e.g. $K(x) = \cos(u_0 x)$: sup-normalized, arity 2), whose reads
are resonance functionals $\sum_{\gamma,\gamma'} \cos(u_0(\gamma-\gamma')L)
= |\Sigma(u_0)|^2$ with $\Sigma(u) := \sum_\gamma m_\gamma e^{i u \gamma L}$. The
quadratic shape AMPLIFIES: one (M) event changes $\Sigma$ by
$v_e = e^{iu_0 c_e}\big(2 - 2\cos(u_0 s_e/2)\big)$ ($c_e$ the midpoint phase, $s_e$
the gap; an exact identity), and the read by
$2\,\mathrm{Re}(\bar\Sigma\,\Delta\Sigma) + |\Delta\Sigma|^2$, so naive site placement
costs $\asymp |\Sigma| \cdot |{\textstyle\sum_e v_e}|$: on RIGID bases
($|\Sigma(u_0)| \asymp N$: quasi-lattices, the satisfiers of AH-shaped laws) this is
$\asymp N$ per coherent event, and even on generic bases
($|\Sigma| \asymp \sqrt{N}$-fluctuation scale) coherent placement overruns the slack.
The O(1)-per-event bookkeeping of the F2a adversary's (M) is therefore FALSE as
stated for this family class on both base types (the build's gate C0 measured the
generic-base block at 106x the slack, and its stage E the rigid-base block at 6393x),
and the floor needs repair exactly here. The lemma:

> **Lemma (site selection).** Let $G$ (plus core) be jointly satisfiable under the
> T-uniformity discipline, with countably many granted families per compact support
> window, $Z_0$ matching, and let the regime condition hold:
> $\varepsilon_G(T)\, TL \;\ge\; C \big( R(T) + \sup_{u \in \mathrm{granted}}
> |\Sigma_{Z_0}(u)| \cdot \bar v \big)$, where $R(T)$ is the resonance budget below
> and $\bar v := C(R) \cdot \max_e |v_e|$ the batch-selection residual (the constant
> depends on the resonance count $R$; session adversary F5(a)). Then for every
> $k \le c_1 \varepsilon_G TL$ there exist $k$ disjoint on-line pairs whose
> positioning-and-merge changes every granted read by at most half its family
> slack.

Proof route, by base type, each step finite. (i) RIGID bases: at a resonant frequency
the resonance's own alignment provides EXACTLY free sites: a merge whose two
endpoints and midpoint are all phase-aligned has $v_e = 2 - 1 - 1 = 0$ identically
(on a lattice, gap-2 merges land the midpoint ON-lattice; on an AH half-integer
quasi-lattice, gap-1 merges land on the half-lattice), so rigidity is blind to moves
that respect it: the build's stage E measures the dichotomy (naive anti-aligned
sites: 6393x slack; aligned sites: 0.0000x, exact). (ii) GENERIC bases: the selection runs
over the TOTAL position-plus-merge cost vectors
$v_e = 2e^{iu m_e} - e^{iu\gamma_1} - e^{iu\gamma_2}$ with the midpoint $m_e$
MOVER-CHOSEN (free phase; the build's `select_sites` computes exactly this object),
which also covers repulsion-law batteries where small gaps must be created rather
than found (session adversary F5(b)); small-gap or aligned choices make $|v_e|$
small ($|v_e| = 2(1 - \cos(u_0 s_e/2))$ exactly for a symmetric in-place merge;
candidates funded by the L3 positioning budget), and BATCH SELECTION across all
granted resonance frequencies simultaneously keeps the total
$\le C(R)\,\max_e |v_e|$ (the batch bound with constant depending on the resonance
count; the naive per-step "partial sums $\le \max_e|v_e|$" invariant of this
document's first draft is FALSE and was refuted by the session adversary, F5(a)),
so the read change is $\le 2|\Sigma|\, C(R)\max_e|v_e| + (C(R)\max_e|v_e|)^2$:
below slack under the regime condition. The build's stage C implements this
selection and measures the block resolved (106x naive to 0.60x selected, full
scale); its gates probe benign phase pools only (F5(c)), which is part of why the
regime condition is carried as a hypothesis rather than absorbed. (iii) The
finitely-many-resonances condition making the balancing well-posed is the resonance
budget: $R(T) :=$ the number of granted frequencies with $|\Sigma(u)|^2 \ge c N^2$
satisfies $R(T) \le C \cdot (\text{support window length})/L \cdot A(T)$ with $A$
the L5 constant: $O(\Delta\,\mathrm{polylog})$. The delta-check independently
derived the same mechanism ("weighted site-averaging",
[`_f2a_delta_check.md`](_f2a_delta_check.md) new-channel finding (b)); the build then
forced the small-gap-plus-balancing form stated here (its first-draft
equidistribution route measured INSUFFICIENT on generic bases: gate C0's catch, kept
on the record). The regime condition is honest scope, not decoration: at
$\varepsilon_G TL$ below the base's resonance-fluctuation scale the floor is OPEN
(Section 8).

**L5 (resonance budget; named input: Montgomery-Vaughan).** Over any C0-configuration,
$\int_W |\Sigma(u)|^2 du \le C\,|W|\,\big(N^{\circledast} + N(T, O(1))\big) \cdot A$
for unit windows $W$: the UNIT-RESOLUTION pair count, not the exact-coincidence count
alone, is what MV's spacing input prices (session adversary F6: clustered-but-distinct
lines at spacing $2^{-T}$ with $h \equiv 1$ have $\int_W |\Sigma|^2 \asymp |W| m N \gg
|W| N^{\circledast}$, so the first draft's $N^{\circledast}$-only display was false).
The unit-resolution count is core-capped at $C\,TL$ by the same Fujii argument that
caps $N^{\circledast}$ (Section 4's unconditional cap), so the budget and everything
downstream are unchanged. MV is the named input (in-print MV 1974; the zeta-23-lean
repository proves its needed instance in-house with constant 13, per the AF Lean
skim: cite, do not re-prove). A resonance of height $cN^2$ and width $\asymp 1/T$
therefore costs $cN^2/T$ of a budget $C\,TL\,A$ per unit window: at most
$C A / (c L) \cdot$ (window length) resonances, the $R(T)$ of L4.

## 3. Theorem 1 (the completeness branch): the sharp linear exchange

**Theorem 1.** Let $G$ be jointly satisfiable and STANDARD (D2), with slack floor
$\varepsilon_G(T)\,TL$. Then, with $c_1, C_1$ explicit in the battery constants:

- **(i) FLOOR (no certificate beats the slack).** For every target
  $g(T) \to \infty$ with $C R(T) \le g(T) \le c_1\, \varepsilon_G(T)\, TL$, under
  L4's regime condition, the
  $G$-matching class contains configurations with $E(T) \ge g(T)$ and
  $N_{\mathrm{off}} \equiv 0$ (merge only), AND configurations with
  $N_{\mathrm{off}}(T) \ge g(T)$ at any sub-resolution displacement profile (merge
  then split; the co-primary register, delta-check edit 6). Hence no member of
  $\mathcal{C}$ sound over $G$-matching configurations certifies
  "$E(T) \le g(T)$ eventually" or "$N_{\mathrm{off}}(T) \le g(T)$ eventually" for any
  such $g$. Proof: L3 positioning + L4 site selection + L2 costs; the (S) step is free
  at the marginal (L2d) and sub-slack at the link for
  $\delta \le s$-scale displacements (L2c small-argument branch).
- **(ii) CEILING (the slack is achievable).** If $G$ contains a pair law at a moving
  window profile ($\lambda(T) \to \infty$ per GLSS Remark 1, slack
  $\varepsilon(T) TL$), the quantitative second-moment engine is an in-class member
  certifying, over all $G$-matching configurations,
  $$E(T) \;\le\; C_1 \Big( \varepsilon(T)\, TL \;+\; \frac{TL}{\lambda(T)}
  \sqrt{\log(2+\lambda(T))} \Big),$$
  by the GLSS subtraction (the combinatorial identity
  $\int_0^T (\Delta_U N)^2 = U N^{\circledast} + 2\int_0^U N(T,u)\,du + O(L^2)$
  against the analytic side with Fujii's unconditional budget; the granted law
  evaluates the integral term; two lines, at the granted slack). The second term is
  this engine's Fujii floor; whenever $\lambda(T) \ge \sqrt{\log}/\varepsilon$-scale
  the bound is $C_1 \varepsilon TL$, and with the bare unquantified $o(TL)$ grant the
  output is exactly $E = o(TL)$: **GLSS I/II recovered as the curve's
  $\varepsilon$-endpoint**, and the GS25 $\mathbf{C}$-ladder's linear exchange
  recovered at the density register.
- **(iii) Consequently**, over STANDARD batteries, the exchange between granted slack
  and certifiable defect is LINEAR and sharp up to the constant ratio $C_1/c_1$: the
  certifiable-against region is exactly $\{ g : g \gtrsim \varepsilon_G TL \}$, at
  both co-primary registers (the $N_{\mathrm{off}}$ ceiling inherited through
  $N_{\mathrm{off}} \le E$, V-F2a-4; the (S)-move floor showing the marginal cannot
  improve on that inheritance). Outside standardness the sharpness is FALSE as posed
  ($G^{\sharp}$ closes the floor range to empty: D2's boundary case, recorded per
  the session adversary's F1), so the curve's completeness branch is a statement
  about standard batteries by hypothesis, not by oversight.

**Remarks.** (1) The floor is semantic (a counterexample configuration), so it binds
EVERY sound certificate regardless of ingenuity: positivity tricks, compressions, SDP
post-processing change nothing (the class's too-broad guard, working as designed).
(2) The lower cutoff $R(T)$ is the site-selection lemma's honest scope; between
$O(\Delta\,\mathrm{polylog})$ and the slack floor nothing is claimed, and below $R(T)$
the floor question is OPEN (stated, not hidden). (3) At $\varepsilon$ unquantified the
theorem's content is the o-statement pair: certifiable $= o(TL)$, non-certifiable $=$
every prescribed sub-slack growth: the two-error-class gap of the GLSS synthesis
($o(TL)$ certified vs $< 2$ needed) is re-derived as the two ENDS of a priced curve.

## 4. Theorem 2 (the location branch): the resolution frontier

The unconditional cap first: from the core alone (Fujii plus the combinatorial
identity at $U = 1/L$), every C0-configuration in the matching class satisfies
$N^{\circledast}(T) \le C_0\, TL$ with explicit $C_0$: the mean-square capacity that
the exclusion engine consumes, granted-law-free.

**Theorem 2.** Let $G$ contain a sup-normalized height-windowed link family of type
$\Theta_G(T) = \Delta_G \log T$ at absolute slack $\varepsilon(T)TL$ whose main-term
profile obeys the NAMED hypothesis **(P-M)**: $|M| \le C\,TL$ across the support
window. (P-M) cannot be derived from satisfiability (session adversary F2, recorded
as this theorem's honest boundary): a satisfiable link law whose main term itself
encodes an off-line pair at $\delta_0$ has $|M| \asymp e^{\delta_0 \Theta_G} \gg TL$,
and exclusion at $\delta_0$ is unsound over its matching class, because the law
PREDICTS the pair. Every standard EF-prediction profile satisfies (P-M), which is why
it is a named hypothesis and not a loss. Then:

- **(i) FLOOR (sub-resolution invisibility).** Under L4's regime condition: for
  every $k(T) \le c_1 \varepsilon_G TL$ and every displacement profile $\delta(T)$
  with
  $$k(T) \cdot \big(\cosh(\delta(T)\,\Theta_G(T)) - 1\big) \;\le\; c_2\,
  \varepsilon_G(T)\, TL,$$
  the matching class contains configurations with $N_{\mathrm{off}} \ge k$ at
  displacement $\delta$ (merge-then-split, costs L2c/L2d). In particular no member
  certifies "no off-line zeros at displacement $\ge \delta(T)$" for
  $\delta(T) \le (1-o(1)) \log(\varepsilon_G TL / k)/\Theta_G$. UNCONDITIONAL
  sub-case (no regime condition; session adversary F4): at $k = O(1)$, in particular
  the C4-loc endpoint $k = 1$, no balancing is needed on generic bases (total cost
  $O(1)$ per family, below every slack) and only L4(i)-alignment on rigid ones, so
  no member certifies $N_{\mathrm{off}} \equiv 0$ at ANY jointly satisfiable grant
  set, regime-condition-free.
- **(ii) CEILING (super-resolution exclusion).** An explicit in-class member excludes,
  over all $G$-matching configurations, any off-line FE pair at displacement
  $$\delta \;\ge\; (1+o(1)) \, \frac{\log(C\,TL)}{\Theta_G(T)}
  \;=\; \frac{1+o(1)}{\Delta_G(T)},$$
  by the pointwise capacity argument with COMPLEX reads (the convention pinned per
  session adversary F3, which refuted the real-read cosine step for near-real
  ordinates): the FE pair at shared ordinate $\gamma_0$ contributes modulus
  $(x^{\delta} + x^{-\delta})\,\phi \ge x^{\delta}\phi$ at every granted $x$, since
  both members carry the SAME phase $e^{i\gamma_0 \log x}$ and cannot cancel each
  other, while the on-line part is $\le N \le C_0 TL$ pointwise and the read is
  pinned to $M \pm \varepsilon TL$ with $|M| \le CTL$ by (P-M): contradiction once
  $x^\delta \phi > C' TL$. For $m$ simultaneous
  off-line pairs with pairwise ordinate separation $\ge \eta$, the same at threshold
  $\delta^* + O(\log(m/\eta)/\Theta_G)$ via the mean-square (MV/L5) version in place
  of the pointwise bound; the fully clustered case is priced by the same formula with
  $\eta$ at the multiplicity resolution (same-ordinate anomalies add coherently and
  need no separation at all).
- **(iii) The band is THIN.** Floor and ceiling pin the visibility frontier to
  $$\delta^*(T) \;=\; (1+o(1))\, \frac{\log TL}{\Theta_G(T)},$$
  with relative band width $\log(k/\varepsilon_G)/\log(TL)$: SHARP whenever
  $\log(1/\varepsilon_G) = o(\log T)$, i.e. for every slack profile coarser than
  power-saving, which is the pool's entire conjectural range (the power-saving
  sub-pool is excluded by C2; the frontier's sharpness is thus universal over the
  default pool's (P-M) profiles, the conditioning inherited from (ii) per session
  adversary F2). Sharpness note (adversary-recommended): the two-sided pinning is
  stated for the bounded-count clause; for clustered multi-pair families the ceiling
  constant degrades per (ii)'s separation clause and the band widens accordingly.
- **(iv) Endpoints.** At the proven-core support ($\Theta \le \log T$, the e1af wall):
  $\delta^* \ge 1 + o(1) > \tfrac12$: NO off-line zero in the strip is in-class
  excludable from proven funding alone: the AF information-wall sentence ("budgets
  bound HOW MANY, never WHERE") derived as the curve's support-1 endpoint, and the
  reason zero-density technology must (and does) live outside this interface. At every
  finite or growing support profile, $\delta^*(T) > 0$ and the sub-resolution region
  is inhabited (i): C4-loc is uncertifiable at every granted profile: the endpoint
  again, quantified.
- **(v) Orthogonality.** The Theorem 1 floor is $\Theta_G$-independent (merges at gap
  $s \le 1/(\pi\Delta_G)$ are support-blind, L2b; positioning is slack-priced only),
  and the Theorem 2 frontier is $\varepsilon_G$-independent to first order
  ($\varepsilon$ enters only the band's log). Slack buys completeness counting;
  support buys location resolution; the purchases do not trade against each other.
  This is the two-wall typing of the frame registration (FUNDING vs INFORMATION)
  recovered as the two coordinates of one measured object.

## 5. Corollary (the scope-honesty no-go, endpoint only) and its pricing

**Corollary.** For every jointly satisfiable grant set $G$: the matching class
contains configurations with $E$ unbounded and configurations with $N_{\mathrm{off}}$
unbounded (Theorems 1(i) and 2(i) at any admissible $g, k \to \infty$), so no member
of $\mathcal{C}$ certifies C4 or C4-loc. This is the naive no-go, decided SOFT-TRUE at
F2a and NOT minted here; its value is exhausted by being the curve's endpoint. The
scope sentence, carried verbatim per re-pose fix 6:

> A no-go over $\mathcal{C}$ says: no certificate architecture that is sound uniformly
> over all FE-symmetric, RvM-class strip configurations matching its granted o-class
> correlation data can certify location-completeness; equivalently, the granted data
> underdetermines the configuration at the completeness register. It does NOT say that
> no correlation-flavored argument can prove RH for zeta: any argument consuming an
> exact zeta identity (the explicit formula as an identity, the Euler product, the
> Hadamard factorization of $\xi$) is outside $\mathcal{C}$ and untouched. The no-go's
> contribution is to certify that every in-class route's missing ingredient is
> exact-class (uniform-in-cutoff) contact with $\zeta$ itself rather than more
> correlation data, at any support, under any law. It neither implies nor is implied
> by RH, and it constrains programs, not the truth value.

**Pricing (the blindness species this generalizes; ancestry stated per the #201
rule).** The curve is the class-level statement whose zeta-geometry instances the repo
and the literature already hold: #199/e2bd (certified line-window floors are
zero-distance geometry: Theorem 2's frontier at the zeta window, with the D-H
landmark's invisibility its measured extreme); e2ax/#192 (the exact
$4(\cosh(\delta u)-1)$ envelope and the $U^* = 1.41/\delta$ detector curve: L2c's
identity measured on zeta data); the primes-thread GUE RH-blindness theorem (the (S)
move is its configuration-space avatar: ordinate statistics bit-identical as zeros
move off-line); BGSTB's $\beta$-sensitivity at support $\le 1$ (the visibility
mechanism below the frontier); AF's in-mechanism ceiling (Theorem 2(iv)'s endpoint).
What is NEW at the class register is the TWO-SIDEDNESS and the decoupling: the floor
constructions and the ceiling engines meet at matching rates on both axes, so these
are not merely lower bounds on ignorance but the exact exchange law of the interface.

## 6. The discipline bracket, run on the theorems

**Davenport-Heilbronn.** The class over D-H runs zero-side only (the prime and link
channels are empty by type refusal, per the vacuity restated at the link). So Theorem
2's ceiling is EMPTY over D-H: no in-class exclusion engine exists at any support, and
D-H's actual off-line pair ($\delta = 0.3085$, $\gamma = 85.699$) is in-class
invisible at EVERY jointly satisfiable zero-side grant set for its strip multiset
(Theorem 2(i) with $\Theta_G = 0$: the invisibility region is the whole strip). The
theorems NAME their D-H refusal, as Section 4 of the class definition demands: the
exclusion engine consumes $\mathcal{P}_{\mathrm{link}}$, which D-H refuses to pose.
This is #199's certified 700x invisibility generalized to the class register, and the
reason the generalization is honest rather than automatic: which zero-side laws D-H's
marginal satisfies is largely unmeasured, so the floor over D-H is stated over
satisfiable $G$ for its strip multiset, exactly as the harness clause prescribes.

**Beurling.** No zero side poses (no FE, no distinguished line, no RvM frame), so
neither theorem is statable over a Beurling system: the curve lives entirely on the
zero-plus-link side. The prime channel's role in the curve is the FUNDING of
$\Theta_G$ (D3), and THAT is where the Beurling discipline bites: the funding data is
L1-congruence-rich (e1af), not density data, so no step of the exclusion engine runs
on a generic Beurling prime side. Any future variant of Theorem 2 that WOULD run
identically there is consuming only the density shadow and is wrong about what the
pool contains (the class definition's Section 4 duty, discharged).

## 7. What is new against the ledger, and what is deliberately not minted

Run in advance of the session adversary's derivability check, per the Section 5 bar.

- **NOT minted: the no-go.** Soft-true, decided at F2a, endpoint status only
  (Section 5 above). Its contrapositive ("completeness must consume exact-class
  contact") remains the COMPASS it already was (#148/#194/#201's wall statement):
  minting it from the soft no-go would fail the derivability check, and this document
  does not.
- **What the curve adds to the compass is the PRICE, not the direction.** The wall
  statement says the missing ingredient is uniform-in-cutoff contact; the curve says
  HOW FAR every in-class route stops short: linearly in slack on the counting axis,
  hyperbolically ($1/\Delta$) in support on the location axis, with the two axes
  decoupled, and with the frontier THIN (iii). None of the ledger clauses
  (#148/#160/#194) words an exchange rate, a resolution frontier, or their
  decoupling; the four candidate mints below are graded by the adversary, not here.
- **Candidate mints for the adversary's derivability run** (each with ancestry):
  (M1) the sharp linear $E$/$N_{\mathrm{off}}$ exchange, two-sided (ancestry: GS25
  ladder ceiling-side at density register; F2a adversary (M) floor-side, here repaired
  and quantified); (M2) the resolution frontier $\delta^* = (1+o(1))\log(TL)/\Theta$,
  two-sided and thin (ancestry: e2ax/#192 measured instance; #199 certified instance;
  zero-detection folklore ceiling-side, here made an in-class theorem against an
  in-class floor); (M3) the orthogonality law (axes decouple; ancestry: the #206
  two-wall typing, here derived rather than typed); (M4) the site-selection lemma
  (ancestry: the F2a adversary's (M) bookkeeping, FALSE as stated for non-decaying
  kernels on rigid bases, here repaired; independently derived by the delta-check).
- **Honesty about (M2)'s ceiling half**: length-vs-displacement detection exchange is
  classical in SHAPE (zero-density technology); the claim here is only its two-sided
  IN-CLASS form: the ceiling from granted (not proven) support with the floor
  matching it. Nothing about actual zeta zero-density is claimed, improved, or
  consumed.

## 8. Hypothesis load, priced (the Section 5 bar's requirement)

- **Conjectural hypotheses: NONE.** The theorems quantify over granted profiles; the
  grants are the theorem's OBJECTS, not its assumptions. Both floors are unconditional
  constructions over C0; both ceilings are conditional exactly on the certificate's
  own granted laws, which is the class's semantics, not a hypothesis of this document.
- **Named classical inputs** (each finite and in-print): Bernstein's inequality for
  exponential type (L2b); the Paley-Wiener representation and the type bound on
  horizontal strips (L2c); Montgomery-Vaughan's mean value theorem (L5; the
  zeta-23-lean repository carries a machine-checked in-house instance, constant 13:
  cite, do not re-prove); Fujii's unconditional pair second moment (Theorem 1(ii),
  the $N^{\circledast}$ cap); the GLSS combinatorial identity (Prop 1 shape; two-line
  derivation reproduced in-class).
- **The frozen foundation**: the delta-checked class definition (C0 frame, the
  three-channel pool under the T-uniformity discipline with the link class pinned at
  $o(TL)$ absolute sup-normalized: delta-check edits 1-3 are load-bearing for Theorem
  2(i)'s cost accounting and for the collapse-safety the floors rely on).
- **Effectivity**: floor constants ($c_1, c_2, C_{\mathrm{bat}}$) explicit per
  battery; ceiling constants explicit modulo the granted profiles' own ineffectivity
  (inherited and stated; nothing else is ineffective).
- **Open scope, stated**: (a) the region below L4's regime condition (targets under
  the resonance budget $R(T)$, or slack under the base's resonance-fluctuation
  scale $\sup_u |\Sigma_{Z_0}(u)| \cdot \bar v$); (b) the clustered multi-pair
  constant in Theorem 2(ii); (c) worst-case grant batteries beyond
  countable-per-window (the discipline's syntax as written admits them; L4 is proven
  for the stated scope). Each is a named attack surface for the session adversary,
  not a hidden gap.

## 9. Verification hand-off and the calibration build

**Lean skeleton**
([`../../lean/ZetaRH/F2bSkeleton.lean`](../../lean/ZetaRH/F2bSkeleton.lean),
deliberately unimported, VerifierQueue pattern; typechecks standalone against the
repo pin with zero errors): the register lemmas are PROVED sorry-free over the
h-profile model (V-F2b-1 parity and the $E < 2 \iff E = 0$ collapse; V-F2b-2 the
conversion $\#\{\text{simple critical}\} \ge 2N - N^{\circledast}$; V-F2b-3 the
PROFILE domination, i.e. defective-line mass $\le E$, the h-profile surrogate of
V-F2a-4 whose sum-register form $N_{\mathrm{off}} + N_{\mathrm{mult}} \le E$ needs
the $\beta$-data extraction and is carried extraction-side like the conversion's
hypothesis boundary, per session adversary F9; V-F2b-4 monotonicity; V-F2b-5 the
cosh envelope identity with its nonnegativity). Exactly ONE statement is
sorry-bodied with its load priced in-file: V-F2b-6 (the second-difference kernel,
Bernstein carried as `hbound`, both derivatives explicit per session adversary F7);
and V-F2b-7 is carried as a NAMED PROP target (a def, deliberately not asserted:
the sorry-bodied theorem form was refutable at degenerate instantiations, session
adversary F8; its load: the moves, L2, L4's batch form, L5's MV input at the
unit-resolution count, the regime condition and standardness, an on-line-mass
hypothesis). **Numerical instance**
([`../../experiments/spectral/e1ag_visibility_curve.py`](../../experiments/spectral/e1ag_visibility_curve.py)
plus dossier): the cost identities to machine precision, the merge floor and rigidity
block with the site-selection rescue measured on synthetic configurations, the
two-sided frontier located at three supports against the $1/\Delta$ law, and the
D-H/Beurling bracket cells. Pre-registered gates in the module docstring; results in
the dossier.

## 10. Session-adversary checklist (pre-registered attack surfaces)

1. L4's proof at its stated scope: construct a jointly satisfiable battery defeating
   equidistribution-plus-anti-phase site selection, or a rigid base whose resonance
   budget escapes L5.
2. The bootstrap L3's joint satisfiability: a granted family whose slack does NOT
   tolerate $c_1 \varepsilon_G TL$ near-coincident pairs (the absolute-vs-relative
   reading is load-bearing here; attack the definition's fix-4 seam).
3. Theorem 2(ii)'s satisfiability-derived main-term bound: a satisfiable link law
   with $|M| \gg TL$ (would break the pointwise capacity argument).
4. The thin-band claim (iii): a granted profile where the band is NOT thin under the
   default pool's classes.
5. The orthogonality claim (v): a coupling channel between slack and support the cost
   lemmas miss.
6. The derivability run on the contrapositive and on mints M1-M4, per the Section 5
   bar; and the D-H cells' honesty (Section 6).
7. The build's gates and the Lean skeleton's statements against this document's
   claims (drift check).
