# ADVERSARY report: the F2a certificate-class definition (same-session, mandated)

> ADVERSARY deliverable, 2026-08-26, frame session F2a of the funding-boundary frame.
> Target: [`f2a_certificate_class.md`](f2a_certificate_class.md) (status PROPOSED,
> pre-adversary). Charter: [`successor_frame_deliberation.md`](successor_frame_deliberation.md)
> Sections 4-7 (the class question, the two failure modes, the Section 5 bar, the Section 6
> verdict wiring) and the #209 scope rulings. Sources read at full length: the target; the
> deliberation; [`reading_notes/glss_full_funding_boundary.md`](reading_notes/glss_full_funding_boundary.md);
> [`reading_notes/alpoge_furman_two_thirds.md`](reading_notes/alpoge_furman_two_thirds.md)
> Section 1; [`../../experiments/spectral/e1af_funding_wall.md`](../../experiments/spectral/e1af_funding_wall.md)
> Sections 2 and 5; [`reading_notes/proportion_support_landscape.md`](reading_notes/proportion_support_landscape.md);
> [`reading_notes/af_lean_repository_skim.md`](reading_notes/af_lean_repository_skim.md);
> LEARNINGS #201-#209. This report does not edit the definition; it lists required fixes
> for the synthesizer. No em dashes anywhere.
>
> **Verdict up front.** A1 LANDED, A2 LANDED, A3 LANDED, A4 LANDED (the crux), A5 GLANCED,
> A6 GLANCED. F2b-readiness: **FAIL AS POSED** (three definition-breaking counterexamples,
> each explicit below; the complete fix list makes the re-pose one bounded synthesizer
> pass, not a new research session). Session grade (A7): **UNMOVED**; tripwire count
> **1/3** post-#209 reset. The failure is the productive kind: two of the constructions
> below effectively answer the class question as posed, which is precisely why the posed
> version must change before F2b spends a session on it.

---

## A1. In-class verification of the boundary engines, independent: LANDED

Charge: verify clause by clause that both purchasing engines are in the class as defined.
Result: **GLSS I/II are in-class** (modulo the error-normalization ambiguity logged under
A3); **the AF compression, the class's record holder, is NOT in-class as posed**, and the
definition's own guard sentence, "every Section 2 in-class row must satisfy every clause
of Section 1 (verified above by inspection, clause by clause, for AF and GLSS)"
(Section 3(a)), is false at exactly one clause, C2.

**The AF funding read is not pool-shaped under the marginal-only syntax.** The
$\mathcal{P}_{\mathrm{zero}}$ pool is defined as "Correlation functionals of the
configuration's **vertical marginal** (the ordinate multiset $\{\gamma\}$, with
multiplicity, of all strip points, wherever $\beta$ sits)". The AF certificate's one
non-structural funding input is the HS budget $\|\tilde G\|_{HS}^2 = (R(\psi)+o(1))N$
(the trace is zero-side structural per the #208 correction: RvM count plus Gabor frame
facts, in-class as C0 + proven math). On the configuration side the HS budget is the pair
functional $\sum_{\rho,\rho'} m_\rho m_{\rho'} |\langle v_\rho, v_{\rho'}\rangle|^2$,
whose entries evaluate modulated windows AT the complex points $\rho$. This functional is
$\beta$-sensitive in an essential way: an off-line zero's Gabor evaluations differ from
their on-line projections by factors up to $T^{O(|\beta - 1/2|)}$ (window frequencies run
to $L$, so the strip offset is not a bounded distortion; this is exactly how the inertia
step sees off-line pairs at all). No functional of the ordinate multiset determines or
usefully bounds it. Its proven evaluation is the Montgomery/BGSTB mean-value computation,
and the landscape note is explicit that this object lives on the full 2D configuration:
"the unconditional variant of BGSTB replacing $T^{i\alpha(\gamma-\gamma')}$ by
$x^{\rho-\rho'}$ over full complex zeros" (landscape Section 1); "Their $F$ is built from
full complex zeros ($x^{\rho-\rho'}$ ...), so the asymptotic itself needs NO location
input" (row note A1). The asymptotic needs no location input; the FUNCTIONAL is a
location-sensitive object, and that is what pool-shape admission is about.

**The definition's own proven core violates its own pool syntax.** C2's proven-core list:
"Pool-shaped statements that are proven (Fujii's second moment, BGSTB's unconditional
$F(\alpha)$ on $[0,1]$, the Montgomery-Vaughan-funded diagonal budgets, Gallagher's ...)
are free." Fujii's second moment is a marginal functional (a second moment of $S(t)$,
determined by the ordinate multiset): genuinely pool-shaped. BGSTB's unconditional
$F(\alpha)$ is the $x^{\rho-\rho'}$ functional: NOT a marginal functional under the C2
syntax as written. So the core's second item is out of the pool the core claims to
inhabit, and the AF row's grant column, "EMPTY (proven pool-shaped funding at support
$\le 1$ only)" (Section 2), is wrong as posed.

**Why no in-frame repair exists without a new clause.** In the real world AF's HS
evaluation routes through the explicit formula (zero-side sum equals prime-side sum,
exactly), then MV evaluates the prime side. C0(ii) excludes the exact EF; C2 contains no
EF-mediated read shape (see A3/A4: the promised channel was never built); and marginal
data cannot bound the $\beta$-sensitive HS value within $o(1)$ relative accuracy (the
$T^{\beta - \beta'}$ distortion is polynomial). So over abstract C0-configurations the AF
derivation has no admissible funding route: the record holder is out of class, the
too-narrow guard fails, and by the definition's own falsifiability standard this forces a
re-pose.

**The other rows.** GLSS I: PCC is a marginal law (admissible grant); Proposition 1 is
Lebesgue bookkeeping (C0-structural); the RvM decomposition is the C0 frame; Fujii is
proven-core and marginal-shaped; the horizontal-multiplicity step is C0 combinatorics.
In-class. GLSS II: AH-Pairs + AH-Weak Density are marginal laws; same engine; in-class,
including the Corollary 2 rung. The $\mathbf{C}$-ladder: $N^{\circledast} \le
(\mathbf{C}+o(1))TL$ is a marginal law; the exchange is C0-structural; in-class. The
conditional exchange-rate ladder (landscape D1, $RH + F \sim 1$ on $[1,\lambda]$ buys
$N_s \ge (1 - \frac{1}{3\lambda^2})N$): out-of-class AS PRINTED (RH is a $\beta$-resolved
hypothesis, exactly like the Montgomery row the table already handles); its in-class
refactoring is "grant the marginal-$F$ law on $[0,\lambda]$", which lands at the
$N^{\circledast}$ register (the GS25 ladder's shape), not at $N^*$: if the definition ever
cites D1 as an in-class calibration it must do so in that form. GGOS shadow row: fine as
stated (the granted object is a marginal-$F$ lower bound; the GRH pricing is correctly
marked out-of-pool).

**Required fixes (A1).** (i) Add the missing read channel: either widen
$\mathcal{P}_{\mathrm{zero}}$ to pair-difference correlation functionals of the full
configuration (kernels in $\rho - \rho'$, the $x^{\rho-\rho'}$ class, which by the FE
pairing see $\beta$ only through difference terms $x^{\pm(2\beta-1)}$), or, better, add
the EF-read family of A3/A4 fix 1, from which the BGSTB law is derivable in-class as
$|{\rm EF\ read}|^2$ evaluated by proven prime mathematics (that is literally how it is
proven). Re-verify the AF row under the repaired pool. (ii) Correct the Section 3(a)
guard sentence: the clause-by-clause verification claim is withdrawn until re-run.
(iii) Correct the proven-core list's self-description or the pool syntax so they agree.

---

## A2. The register (C4 at $E(T) < 2$): LANDED

Charge: attack the choice of $E$ as primary register; construct the cheap evasions.

**(i) A cardinality argument against C4-fin exists, and I construct it.** The builder's
own risk 1(b) asked whether "C4-fin ... [is] perhaps ALREADY excludable by a soft
cardinality argument that would make the theorem cheap and its derivability suspect". It
is. **The merge move (M):** take any C0-configuration $Z_0$ satisfying a grant set $G$
plus the proven core; choose $k(T) \to \infty$ arbitrarily slowly; move $k(T)$ disjoint
pairs of on-line zeros, each pair to its common midpoint ordinate (displacement at most
the pair's gap). Bookkeeping: $N(T)$ unchanged; the FE pairing and multiplicity closure
hold (merged double at $\beta = 1/2$ is self-paired, $m = 2$); $S$-corrections change by
$O(1)$ on a vanishing-measure set (C0 frame intact; Fujii/Selberg-class core functionals
change by $o$ of their errors); every bounded-kernel gap functional changes by $O(1)$ per
event, so by $O(k(T)) = o(TL)$, invisible to every admissible o-class law, INCLUDING
full-window pair counts (equal-ordinate pairs are excluded from $N(\lambda)$, and
$N^{\circledast}$-type reads carry $o(TL)$ slack); and $E(T) = 2k(T) \to \infty$. So for
every satisfiable $G$ there is a matching configuration with $E$ unbounded: no in-class
certificate certifies C4-fin (hence C4). Two lines of measure-and-parity bookkeeping,
consuming nothing about primes or zeta. The register's strong target is softly refutable
in-frame; the no-go's VALUE cannot live at C4-fin.

**(ii) The all-on-line, wildly multiple configuration exists in-frame and decouples the
registers.** The merge construction IS that configuration: $E \to \infty$ with
$N_{\mathrm{off}} \equiv 0$, location perfect. Consequence: a C4-only no-go can be true
for pure simplicity reasons while saying nothing about location, so the frame question's
word "location" is unearned by C4 alone. And the converse contamination is exact, not
partial: **the split move (S)** replaces an on-line double zero $m = 2$ at
$\frac12 + i\gamma$ by an FE pair $\{\beta + i\gamma,\ 1 - \beta + i\gamma\}$, both
simple. The ordinate multiset is LITERALLY UNCHANGED ($\gamma$ carries mass 2 either
way), $N$, $N^{\circledast}$, $E$, and every marginal functional are exactly invariant,
and $N_{\mathrm{off}}$ jumps by 2. Composing (M) then (S): configurations with
$N_{\mathrm{off}} \to \infty$ matching every marginal law exactly up to the (M) step's
$o$-costs. So under the marginal-only pool the C4-loc no-go is also soft; and under the
A1-widened pool ($x^{\rho-\rho'}$ or EF reads at supports up to $\Delta(T)$), near-line
splits at $\beta - \frac12 = 1/(\Delta(T) L)$ cost $O(1)$ per event in every granted
read, so slow-growing off-line families remain invisible at any $\omega(1)$ error class.
This also corrects the optimism of Section 3(a)'s guard sentence, "off-line-ness is
visible to the marginal as equal-ordinate mass": off-line-ness created from an on-line
double adds NO equal-ordinate mass; the marginal sees defect mass $E$, never the
multiplicity/location split of it. The engines purchase non-defect density, not location
density.

**(iii) The quantifier.** "There exists $T_0$ such that $E(T) < 2$ for all $T \ge T_0$"
is not vacuous and not unfalsifiable: by monotonicity plus parity (V-F2a-1, checked
correct), eventual $< 2$ collapses to $E \equiv 0$, so the "eventually" adds and
subtracts nothing. The grants' ineffectivity does not undermine the register; the
ineffectivity that matters is the o-slack itself, which is where the counterexamples of
(i)/(ii) live.

**Verdict on the register question.** $E$ remains the right BOOKKEEPING register (it is
the engines' certified observable; the definition's reasoning there is sound), but C4
cannot be the sole primary: **C4-loc must be co-primary** (risk 1(a) confirmed: a
location-only certificate with $E$ unbounded would evade a C4-only no-go, and my (M)
construction shows the dual gap is real). Deeper: the register question is SUBORDINATE to
the frame repair (A4), because as posed every register's no-go is either false (A3's
amplifiers) or free ((i)/(ii) above); until the pool syntax and scope are fixed, choosing
among C4/C4-loc/C4-fin is choosing which trivial statement to prove.

---

## A3. The RH-adjacency channel (the crux attack on C2): LANDED

Charge: hunt for a consistent grant set inside the pool whose conjunction is
RH-equivalent or RH-implying; check the o-cap against the engines; check the
Lagarias-Rodgers usage.

**(i) The pool as written admits an RH-forcing grant: the amplifier family.** C2 admits
"weighted $n$-point gap-counting functionals at the $TL$ normalization ..., with
arbitrary weights and arbitrary gap-scale support", law-blind. Take the 2-point
equal-ordinate family with $T$-dependent weight: $\Phi_T := TL \cdot E(T)$ (equivalently,
weight $TL$ on the gap-zero diagonal, excluding self-pairs). Grant the law
"$\Phi_T = 0 + o(TL)$". This is syntactically a law in the running variable (the
no-fixed-height clause does not bite), with error class $o(TL)$ (the cap's letter is
satisfied), of the marginal (admission is law-blind). Semantically it asserts
$E(T) = o(1)$, hence by integrality $E \equiv 0$ eventually: every matching configuration
has all zeros simple and on the line, and a certificate granting it certifies C4 in one
line. The G-LAW guard "an exact statement like $N^{\circledast} - N = 0$ is not
grantable; only its $o(TL)$ shadow is" (Section 7 item 3) is defeated by amplitude
rescaling: o-class SYNTAX can encode exact-class INFORMATION. Note the defense "weights
may not depend on $T$" is not available as written: the pool's own named special cases
are $T$-dependent kernels ($F(\alpha)$'s kernel $T^{i\alpha u}$; $N(\lambda)$ with moving
$\lambda$), so the text cannot distinguish $T$-dependent phase/support (harmless, needed)
from $T$-dependent amplitude (the smuggler) without a new clause. A second smuggler of
the same species, in case the first is patched narrowly: the growing-arity coincidence
family $\Phi_T := \sum_{\mathrm{lines}} h^{n(T)}$ with $n(T) = L^2$; granting
"$\Phi_T = TL + o(TL)$" forbids any line with $h \ge 2$ outright (one $h = 2$ line at any
height contributes $2^{L^2} \gg TL$), again forcing $E \equiv 0$. This answers the
builder's probe (ii): the fixed-height diagonalization leak is REOPENED by composite
reads exactly as feared, through amplitude and arity rather than height.

**The restriction that closes it, named as demanded.** **T-uniformity of granted
families:** each admissible family has (a) fixed finite arity $n$; (b) a kernel applied
to rescaled gap vectors whose amplitude is $T$-independent and bounded (normalize
$\sup |K| \le 1$); (c) $T$-dependence confined to a support/window parameter with a
per-family uniformity clause in the GLSS Remark 1 style; (d) error $o(TL)$ absolute per
family; plus (e) the satisfiability clause of fix 3 below. Under (a)-(e) the collapse is
not merely plausible but PROVEN impossible: the A2/A4 sub-slack constructions show that
for every satisfiable grant set the matching class contains non-RH configurations, so no
restricted-pool conjunction is RH-forcing over the class. (That proof is a positive yield
of this run: the repaired pool comes with its collapse-safety certificate. Its cost is
recorded under A4: the same constructions make the no-go itself cheap.)

**(ii) A consistency bug adjacent to the hunt: "consistent" must become "satisfiable".**
"Granted subsets must be consistent" (C2) and C4's "as theorems over C0 + proven core +
its grant set $G$" interact badly: a grant set consistent as a theory but jointly
UNSATISFIABLE with C0 + core (example: grant "$N^{\circledast}(T) = \frac12 TL + o(TL)$",
impossible since $N^{\circledast} \ge N = TL + o(TL)$ under the C0 frame) makes every
implication vacuously true, so a certificate granting it "certifies" C4 for free, and the
Section 5 no-go as quantified ("for every member ... and every consistent grant set $G$")
is FALSE for trivial reasons. Replace "consistent" everywhere by "jointly satisfiable
with C0 + proven core by at least one configuration" (or quantify the no-go over
satisfiable $G$ only).

**(iii) Does the o-cap exclude a legitimate engine? No; but the cap's letter conflicts
with the proven core.** GLSS I/II grants are $o(TL)$-class: in-cap. AF consumes no
conjectural grants, and its OUTPUT o(1)-proportion error is C3's business (unrestricted:
fine). But the cap's blanket wording, "Error classes admitted: **o-class only** ...
Power-saving and square-root error classes are excluded from the default pool", applies
as written to the whole pool including the proven core, whose members carry sharper
classes (Fujii's $O(T\sqrt{\log})$; MV diagonal budgets with $1/\log$-relative errors;
and if the A1 fix admits it, BGSTB's $O(1/\sqrt{\log T})$). Proven statements cannot
smuggle; the exclusion's purpose (row E5's $k = 1$ member is RH) is about conjectural
grants. Fix: scope the error cap to conjectural grants; proven statements enter at their
proven classes. Also strike or correct the parenthetical "(equivalently vanishing
relative error)" attached to the $o(TL)$ cap: the equivalence is false for families whose
main term is not $\asymp TL$ (Fujii at bounded $\lambda$ has main $\asymp T$), and the
two readings are load-bearing in opposite directions: absolute $o(TL)$ slack is what
makes the A2/A4 constructions invisible, while per-family RELATIVE $o$(main) on
shrinking-mass windows would re-admit an exactness smuggler (grant the small-gap family
$N(T, \lambda_0(T))$ at relative error with $\lambda_0(T) \to 0$ fast and the law forces
zero coincidences: E $\equiv 0$ again). The definition must choose the absolute reading
per family and say so, with the window-profile uniformity stated per family (at very
large windows the absolute-$o(TL)$ pair law entangles $N^{\circledast}$ with the count
fluctuation $S$ and approaches unsatisfiability; the F2b bookkeeping will turn on exactly
these clauses).

**(iv) The prime side of the hunt is moot as posed, which is itself a finding.** A
laundering route through the GM dictionary is correctly priced (RH-priced bridge, noted
in-definition; Mueller 1983 correctly left open). But as posed nothing needs laundering:
$\mathcal{P}_{\mathrm{prime}}$ grants are statements about the rational primes, the
frame contains no link between the primes and the abstract configuration (the EF is
excluded and no read family replaces it), and C1 restricts derivations to touch the
configuration "ONLY through (a) and (b)". So a prime read can never contribute
non-vacuously to a C3 output about the configuration: **the entire prime parametrization
is logically inert in-class**. C0(ii)'s own sentence promises the channel ("EF-derived
information enters only through C2's finite, error-carrying reads") and C2 never
delivers a read shape that touches both sides. The frame question's verbatim words,
"certificates whose inputs are prime-correlation data", are unsatisfiable by any
non-vacuous member of $\mathcal{C}$ as posed. Fix (the same one A1 needs): add the
EF-read family $\mathcal{P}_{\mathrm{link}}$: for $f$ in named $T$-uniform bandlimited
classes with stated support profiles, the two-sided read
"$\sum_\rho f(\rho) = W_{\mathrm{prime}}(f) + W_\infty(f) + o(\text{stated class})$",
with the exact identity still excluded. Then prime grants fund $W_{\mathrm{prime}}$
evaluations past support 1 (the e1af Section 2 family $\{B_X(h)\}$ at weight
$\log(H/h)$ enters exactly here), AF's HS read becomes in-class, and the D-H scope
clause of Section 4 survives verbatim at the link (for D-H the prime side of the link is
unposable per #202(iv): the family is empty by type refusal). I re-ran the collapse hunt
over $\mathcal{P}_{\mathrm{link}}$ at o-class with $T$-uniform test classes: near-line
splits at $\beta - \frac12 = 1/(\Delta L)$ cost $O(1)$ per event in every link read up to
support $\Delta$, so the widened pool remains collapse-safe (and remains softly
no-go-able; A4).

**(v) Lagarias-Rodgers usage: in scope, one caveat.** The definition uses the row as
"the no-go's natural proof shape ... in-print ancestor at a smaller pool" and as the
non-implication anchor at the currently-known sub-pool. That matches the landscape's
verbatim abstract ("show by construction of an explicit counterexample point process
that it is not [ruled out]") and does not overstate (no claim that L-R covers the full
o-class pool). One caveat to carry: the L-R process matches "all statistics which are
currently known about zeros" in the CORRELATION family; whether it matches the full
proven marginal core the class grants for free (Selberg/Fujii $S(t)$-moment statements)
is not checked in print, so cite it as ancestor-of-shape, not as a member of the
repaired class's counterexample family. (The A2/A4 constructions, which perturb a
satisfier rather than build from scratch, do not have this gap; they are the sharper
ancestor and are free.)

---

## A4. Frame well-posedness (the K1-adjacent scope question): LANDED, the crux

**(i) With the exact EF in-frame the question does collapse; confirmed with a sharper
wording.** An exact-EF read family pins the matching class to zeta's actual zero multiset
(uniqueness of the Guinand-Weil-type correspondence per function; the Vedana
classification is the in-repo external anchor that formula-existence plus the data pins
the measure). With exactly one matching configuration, the counterexample-configuration
method is unavailable, soundness-over-matching-configurations equals truth-about-zeta,
and a "no-go" would have to be "RH is not a theorem of [pool + EF + all proven
mathematics]", i.e. an unprovability statement about zeta: unconditional metamathematical
strength, out of scope. The exclusion is justified; keep it, with this wording available
to F2b.

**(ii) Without the EF the frame is too floppy, and this is now a construction, not a
worry.** The A2 moves (M), (S), plus the injection move (I) (add FE-paired near-line
pairs at rate $k(T) \ll \log T$, consuming the C0 frame's $S \ll \log T$ budget and, if
Selberg-class moment statements are in the core, slowing to $k(T) = o(\sqrt{\log\log T})$)
show: **for every satisfiable grant set $G$, the matching class contains configurations
with $E$ and $N_{\mathrm{off}}$ unbounded, obtained by perturbing any satisfier below
every granted slack floor.** Seeding at a satisfier is the decisive trick: the perturbed
configuration inherits the ENTIRE proven core and all of $G$ automatically, because every
perturbation cost is below every admitted error class by construction. Consequence for
Section 5's self-declared "mathematical heart": the sentence "the configuration must also
match the proven prime-side core through every pool-shaped consequence of the explicit
formula at all supports ... how much of the EF's pinning power survives the o-class floor
is the mathematical heart of F2b" is ALREADY DECIDED, negatively and cheaply: at o-class,
the EF's pinning power against sub-slack perturbations is nil, because the pinning enters
only through reads that carry $\omega(1)$ slack while the defect events cost $O(1)$ each.
The heart question is real only at exact/uniform class, which is #148's clause by
inspection rather than by theorem. As posed, F2b's no-go is therefore soft-true at every
register, and its contrapositive ("completeness must consume exact-class contact") is a
restatement of the pool's own design (the slack was put in by fiat; the no-go harvests
it): it would fail the #201 derivability check at mint time. The definition's Section 3(b)
falsifiability clause fires early: this is the design-level tautology, caught at F2a
instead of F2b.

**What the no-go, if proven in this frame, would and would not say.** The scope sentence
F2b needs verbatim:

> A no-go over $\mathcal{C}$ says: no certificate architecture that is sound uniformly
> over all FE-symmetric, RvM-class strip configurations matching its granted o-class
> correlation data can certify location-completeness; equivalently, the granted data
> underdetermines the configuration at the completeness register. It does NOT say that no
> correlation-flavored argument can prove RH for zeta: any argument consuming an exact
> zeta identity (the explicit formula as an identity, the Euler product, the Hadamard
> factorization of $\xi$) is outside $\mathcal{C}$ and untouched. The no-go's
> contribution is to certify that every in-class route's missing ingredient is
> exact-class (uniform-in-cutoff) contact with $\zeta$ itself rather than more
> correlation data, at any support, under any law. It neither implies nor is implied by
> RH, and it constrains programs, not the truth value.

**Where the non-trivial question actually lives after this attack.** Two honest re-aims,
for the re-pose to choose between (both syntactic, preserving the 3(b) discipline):
(a) the QUANTITATIVE visibility-floor law: for a granted family set with stated window
and error profiles, the certified exchange rate between defect growth and slack (which
$E$-growth rates are certifiable-against at which granted classes; my constructions give
the lower bulk of the curve, the GLSS $o(TL)$ ceiling the upper; the theorem is the
curve, not the endpoint); (b) the zeta-scope honesty theorem: the no-go stated WITH the
scope sentence above as its content, priced as a class-level generalization of the
#199/BGSTB blindness species (the definition's too-narrow guard concedes this is the
low-value outcome; if it is the only provable outcome, the frame's exit 2 language should
say so rather than let F2b relabel it). The builder's probe (i) (a $\beta$-sensitive
functional passing C2's syntax) resolves as: the marginal syntax is genuinely
$\beta$-tight, no smuggle exists THROUGH it; the two real breaches are from the other
side (the record holder's $\beta$-sensitive read is wrongly excluded, A1) and from
normalization (exactness smuggled without $\beta$, A3).

---

## A5. Fidelity: GLANCED

Verified faithful against the cited sources: the GLSS conventions and multiset
classification; PCC/AH statements and their two-hypothesis structure (Theorem 4 = AH-Pairs
plus AH-Weak Density; the 50/50 rung at (AH1) only); $E(T) = N^{\circledast} - N =
\sum h(h-1)$, evenness, monotonicity, $E < 2 \iff E = 0$; V-F2a-1 through V-F2a-4 all
check (including the both-defective double-counting corner: $N_{\mathrm{off}} +
N_{\mathrm{mult}} \le E$ holds with equality at $h = 2$); the $\mathbf{C}$-ladder
completeness-at-no-rung reading; "does not improve any results" (GLSS I Remark 2); the AF
constants $2/3$, $5/6$, $0.6725/0.8362$, $13/18$, "RH itself is out of reach of the
mechanism"; the e1af $H(\delta) \asymp X/T$ and $\log(H/h)$ weights; the GM-dictionary
RH-pricing; row E5's $k = 1$ clause and its use; the Bolanz row E2 use in Section 6 item
6; the "certified unoccupied" citation (landscape Section 7 gap 5); the BH95 [SECONDARY]
tag correctly carried. Montgomery's marginal $F(\alpha)$ correctly listed as a marginal
special case (it is the BGSTB variant that is not; A1).

Three precision flags, descending:

1. **"The Davenport-Heilbronn configuration satisfies C0 verbatim" is false for the full
   D-H zero set**: D-H has zeros in $\sigma > 1$ (and FE partners in $\sigma < 0$),
   outside C0's strip. The STRIP multiset satisfies C0 (and is closed under the pairing,
   since the pairing maps the exterior to the exterior), and the certified off-line pair
   at $0.8085 + 85.699i$ is in-strip, so Section 4's test-harness use survives; but the
   sentence and the "plus zeros in $\sigma > 1$" clause two paragraphs later must be
   reconciled (the $\sigma > 1$ zeros are not C0-configuration points and the D-H C4
   statement concerns the strip multiset only).
2. **The "(equivalently vanishing relative error)" parenthetical is false in general**
   and load-bearing (A3(iii) carries the fix).
3. **"verified above by inspection, clause by clause, for AF and GLSS"**: overclaim
   (A1). Pedantry, logged not graded: C0's closed strip $0 \le \beta \le 1$ vs GLSS's
   open strip; harmless but the formal layer should pick one.

---

## A6. The Lean sketch: GLANCED (one real mismatch)

Conformance to the prose: the fields are the pool and the output clause, the no-go is a
statement over inhabitants, and the comment "deliberately NO field mentions any $\beta$,
any single $\rho$, or an exact identity" matches C0(ii)/C2. Faithful, and instructively
so: `prime : PrimePairLaws` mentions `Z` nowhere, which is the A3(iv) inertness displayed
in types (compare AF's actual `PaperInputs`, whose five fields are `EF, RvM, cheb, MV,
Gamma`: the field the sketch deletes relative to the record holder's own trust boundary
is exactly `EF`, and with it the primes' only route to the configuration). Keep the
sketch; state this.

The real mismatch: the prose's class "quantifies over all consistent $G$" with law-blind
admission of mutually contradictory laws, but `CorrelationPool` is a single Prop
structure; as a conjunction it is unsatisfiable the moment `vert` bundles PCC-shaped and
AH-shaped laws, and the target line `∀ Z G C, SoundOver Z G C → ¬ CertifiesLimit C`
binds a `G` that no structure introduces. The quarantine must be grant-set-indexed:
`G : Set LawFamily`, `Satisfies Z G`, a satisfiability side condition (A3(ii)), and
`reads : FiniteReadsFrom G`. P2 conformance is otherwise half by design (bundle yes;
discharge ladder inapplicable to conjectural grants, which is the right shape); graded
conforming once `G` is bound.

---

## A7. Session grade (mandatory) and F2b-readiness

**Derivability check on the session's candidate mints, per the Section 6 wiring.**
(1) The class definition itself: a definition, not a theorem-shape; under the Section 5
bar ((a) theorem-shape proven modulo named hypotheses, (b) located obstruction with
mechanism, (c) constraint passing derivability, (d) frontier movement) it is none of the
four, and this report finds it not yet F2b-ready besides. (2) The GLSS escape-clause
synthesis (the $E(T)$ two-error-class anatomy): the boundary note's own label is "own
synthesis, assembled from displayed equations; not a claim of the papers"; as a datum it
sharpens #208(iii)'s already-banked GLSS sentence (density-1 at full funding,
law-indifferent, completeness untouched) and is wordable from it plus the papers'
displays: enrichment, not a coordinate. (3) The law-indifference datum (the mechanism
consumes one linear functional of the correlation measure): same status; #208 banked the
law-indifference headline, the note prices the consumed scalar: enrichment.
(4) The Lean-skim conformance verdict (the AF self-report verified at skim tier, the #208
renamed surface discharged to one `lake build`): genuine diligence with a real
trust-boundary yield, but not a Section 5 (a)-(d) item. No metric item lands.

**Grade: UNMOVED.** One-paragraph justification: F2a is a pose-and-prep session by
charter, and it executed its spec (two prep riders plus the posed definition, all
delivered, all first-party-sourced); but the Section 5 bar was raised precisely so that
statements and definitions are cheap, and nothing minted this session is a theorem-shape,
a located obstruction with a mechanism, or a derivability-passing constraint. The posed
definition moreover fails its own Section 3 guards under this report's attacks, so the
session's central artifact is a re-pose input rather than a settled interface. Under the
#206 wiring (non-UNMOVED iff a metric item lands AND passes derivability, graded by the
session's adversary) the grade is UNMOVED. **Tripwire: the #209 audit reset the counter
to 0/3; F2a is a registered session executing its spec, so exit 3a does not apply; no
label inflation occurred (the definition self-filed as PROPOSED-attacking-nothing, the
notes self-filed their syntheses as readings), so 3b does not advance. New count: 1/3.**
Exit 2 is unchanged and binding: F2b is frame session four, and by exit 2's letter the
frame must produce a theorem-shape at the bar or an evading family there. Consequence
the ORCHESTRATOR should schedule around: the required fixes below are on F2b's critical
path; run the re-pose as F2b's opening block (a bounded synthesizer pass against this
report), not as a separate session, which would be a 3a event.

**F2b-readiness of the definition: FAIL as posed.** Three definition-breaking
counterexamples: the record holder is out of class (A1: the marginal-only pool refuses
AF's $\beta$-sensitive proven funding read, and the proven core's own BGSTB item violates
the pool syntax); the pool admits amplifier grants that certify C4 outright (A3(i):
"$TL \cdot E(T) = o(TL)$", and the growing-arity variant), so the no-go as stated is
false; and the frame without any EF-class channel is simultaneously inert on the prime
side (A3(iv)) and floppy on the zero side (A4(ii): sub-slack perturbations decide the
declared "mathematical heart" trivially at every register). Each fix is stated and
bounded; none requires new mathematics beyond what this report supplies; but they change
load-bearing clauses (C2's shape and syntax, the satisfiability quantifier, C4's
primacy, Section 5's target and value story), which is a re-pose, not a patch list a
theorem session should absorb silently.

---

## Required fixes (consolidated; the synthesizer applies, the re-posed definition
returns for a bounded delta-check)

1. **Add the EF-read channel $\mathcal{P}_{\mathrm{link}}$** (A1, A3(iv)): $T$-uniform
   bandlimited test classes, stated support profiles, two-sided reads
   $\sum_\rho f(\rho) = W_{\mathrm{prime}}(f) + W_\infty(f) + o(\text{stated class})$;
   exact identity still excluded; D-H vacuity restated at the link (prime side unposable,
   #202(iv)). Optionally also widen $\mathcal{P}_{\mathrm{zero}}$ to pair-difference
   kernels in $\rho - \rho'$ (the $x^{\rho-\rho'}$ class). Re-verify the AF and GGOS rows
   and the proven-core list under the repaired pool; withdraw the Section 3(a)
   "verified by inspection" sentence until re-run.
2. **T-uniformity discipline on granted families** (A3(i)): fixed arity; bounded
   $T$-independent kernel amplitude; $T$-dependence only through support/window
   parameters with per-family uniformity clauses; error $o(TL)$ absolute per family.
   State that this closes the amplifier and growing-arity smugglers and re-closes the
   fixed-height leak; carry the collapse-safety proof (A3's positive yield) into the
   definition's Section 3(b).
3. **Replace "consistent" by "jointly satisfiable with C0 + proven core"** in C2, C4,
   and Section 5's quantifiers (A3(ii)).
4. **Scope the o-class error cap to conjectural grants**; proven statements enter at
   their proven classes; delete or correct "(equivalently vanishing relative error)" and
   state the absolute reading per family with window-profile uniformity (A3(iii)).
5. **Make C4-loc co-primary with C4** (A2): the no-go must cover
   $N_{\mathrm{off}} \equiv 0$ certification explicitly; record that C4-fin is softly
   refutable in-frame (the (M) construction) so the no-go's value cannot be sited there.
6. **Adopt the A4 scope sentence verbatim into Section 5** and re-aim F2b's value claim:
   correct the "mathematical heart" sentence (at o-class the EF's pinning power against
   sub-slack perturbations is nil; decided, not open); the surviving non-trivial targets
   are the quantitative visibility-floor law and/or the scope-honest class blindness
   theorem, and the Section 5 contrapositive ("the residue is #148's clause") must not be
   minted as a theorem on the back of the soft no-go (it would fail the derivability
   check; it remains the compass reading it already was).
7. **Smaller** (A5, A6, A3(v)): D-H strip-multiset wording; the closed/open strip
   convention; the L-R ancestor caveat (correlation statistics only; the perturbation
   construction supersedes it as the in-class counterexample family); Lean sketch:
   grant-set-index the pool, bind $G$, add the satisfiability side condition, and keep
   the instructive absence note (the deleted field relative to AF's `PaperInputs` is
   `EF`).

---

## Overall verdict

**FAIL as posed; re-pose required before F2b; all fixes bounded and listed.** The
definition's architecture choices that survive attack, and should be kept through the
re-pose: the abstract-configuration semantics with the exact-EF exclusion (A4(i) confirms
the collapse direction), the absolute-count register with the density-register refusal,
law-blind admission with the law-indifference rationale, the syntactic-only discipline of
Section 3(b), the named leave-outs (family averaging, moment class, $\beta$-resolved
facts; the Hadamard-factorization probe of Section 7 item 6 resolves as principled:
mean values reach the configuration only through an exact-identity channel of the kind
C0(ii) excludes), and the V-F2a-1..4 verification targets (all check, and V-F2a-1's
parity/monotonicity lemma is what makes the A2 register analysis clean). What fails is
the funding clause's two-sided seal: as posed it is too tight for the class's own record
holder and too loose for normalization smugglers, and the missing EF-class channel makes
the prime parametrization decorative while leaving the abstract frame soft enough that
the declared theorem target is decided by a perturbation argument. Session grade UNMOVED,
tripwire 1/3, exit 2 unchanged at F2b; fold the re-pose into F2b's opening block.
