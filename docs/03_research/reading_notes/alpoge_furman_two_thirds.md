# Alpöge-Furman (arXiv:2608.13637): two thirds of the zeta zeros simple and on the line, by inertia bookkeeping on a compressed Weil form

> SURVEYOR deep-read note, 2026-08-25. Executes the top-slot assignment from
> [`watch_sweep_2026-08-25.md`](watch_sweep_2026-08-25.md) (grade CANDIDATE, urgent) and
> adjudicates its discrepancy-log item 2 (the e1s/#169 wording). Sources: the arXiv abstract
> page and the v2 HTML full text, fetched 2026-08-25; quotes below are from those fetches.
> ADVERSARY pass: run same-day on this note's claims (Section 5); post-adversary state is
> authoritative. No em dashes anywhere.

## 1. The result and the mechanism, precisely

**Theorem A (unconditional).** At least $2/3$ of the nontrivial zeros of $\zeta$, counted
with multiplicity, are simple and on the critical line; at least $5/6$ are distinct. With
the Montgomery-Taylor window the constants are $0.6725$ and $0.8362$. Prior unconditional
records, as credited in-paper: $5/12$ (simple-and-on-line, PRZZ20; PRZZ's own abstract
claims on-line, the simple-and-on-line pairing is the AF record bookkeeping) and $0.6603$
(distinct, Wu15; verified at source, Quart. J. Math. 66(2) 2015). Extends to
primitive Dirichlet L-functions (Theorem B). Formally verified in Lean 4.

**The mechanism.** Build the $d \times d$ real symmetric matrix
$\tilde G = \frac{1}{aL^2}\sum_{\mathrm{Re}\,\gamma_\rho \in I'} m_\rho v_\rho v_\rho^T$,
$d \approx N(T, 2T)$, where $v_\rho$ packs a zero's evaluations against a Gabor system of
modulated windows at equispaced points: a finite COMPRESSION of Weil's Hermitian form.
Then:

1. **The prime side computes the spectral statistics unconditionally.** $\mathrm{tr}\,
   \tilde G$ and $\|\tilde G\|_{HS}^2$ are evaluated by the explicit formula plus
   Montgomery's classical prime-side mean values (the inputs of Aryan and of
   Baluyot-Goldston-Suriajaya-Turnage-Butterbaugh), valid at Fourier support $\le 1$
   ($X \le T$): $\|\tilde G\|_{HS}^2 = (R(\psi) + o(1))N$ with $R(\psi)$ a window constant
   independent of the zero configuration.
2. **Sylvester inertia types the zero side.** Every distinct on-line zero contributes a
   rank-one PSD block; every off-line pair $\{\rho, 1-\bar\rho\}$ contributes, via
   $m_\rho(v_\rho v_\rho^T + \bar v_\rho \bar v_\rho^T) = 2m_\rho(aa^T - bb^T)$, the
   pullback of $\mathrm{diag}(1, -1)$: signature $(1,1)$, exactly one unit of positive
   index per pair, whatever its magnitude ($n_+(A^*Q_0A) \le n_+(Q_0)$).
3. **A rank-trace inequality closes it.** Lemma 3.2: $\mathrm{rank}\,P_1 \ge
   2\,\mathrm{tr}\,P_1 + 4\,\mathrm{tr}\,Q' - 4b - \|P_1 + Q'\|_{HS}^2$ (the scalar shadow
   is $m^2 \ge 2m - 1$; multiplicity pays a flat charge 4 via $m^2 \ge 3m - 2$). With
   rank and index bounded by the on-line/off-line bookkeeping and trace/HS supplied by the
   primes: $N_0^s \ge (2 - R(\psi) - o(1))N$; $R(\psi_0) = 4/3$ gives $2/3$.

**The ceiling, in the paper's own words.** The support restriction is structural: past
$X \asymp T$ "the off-diagonal prime sum is no longer dominated by the diagonal" and one
needs Hardy-Littlewood / pair correlation beyond support 1. Unconditionally "higher
moments add nothing" (Rudnick-Sarnak diagonal range: only $k = 1$ at $X \asymp T$).
Conditionally, HL*(4) would give $13/18$ and full HL* would give proportion 1 OF SIMPLE
ZEROS; and, verbatim: "RH itself is out of reach of the mechanism." The paper places
itself as complementary to GLSS25, "where the pair correlation conjecture with full
support yields 100% simple zeros on the line." (Support-1 data is pair-correlation data;
the reading of RH as individual-zero information beyond it is this note's gloss, not a
quotation: adversary catch A4.)

**Provenance.** The paper's own §1.5/Appendix B: "The mathematical argument in this paper
was discovered and written by Claude, an AI developed by Anthropic"; found over two
interactive sessions; "checked by repeated adversarial review by independent model
instances"; problem posed and guided by Jarred Sumner; Lean formalization orchestrated by
Eric Easley; the listed authors verified and take responsibility. The Lean artifact
covers Theorems A and B on the three standard axioms. **CORRECTED AT SOURCE 2026-08-26**
(F1 survey, [`af_funding_inputs_verification.md`](af_funding_inputs_verification.md)):
this note's earlier clause "with the analytic prime-side inputs (their §5.1-5.4, the
Aryan/BGSTB evaluations) carried as hypotheses rather than formalized" is NOT in the
paper and is contradicted by its Appendix A in BOTH versions ("their types carry no
hypotheses... the analytic inputs of §2 appear in the repository as theorems in their own
right rather than as hypotheses of the main theorems... no sorry"): a fetch-summarizer
confabulation (the month's third caught instance), likely blending §7.2's real
hvalid/EnclOK hypothesis pair, which belongs to the bandwidth-one ceiling certificate
only. The paper's SELF-REPORT is full coverage; the repository itself is unaudited by
this repo, and the F2a Lean skim carries the audit checklist (the five named
declarations, `#print axioms`, the EnclOK externality).

## 2. What it changes on this project's map

**(a) The e1s/#169 sharpening: ADJUDICATED, wording adopted.** The repo's dichotomy read
"on the compressed Weil form the eigenvalue COUNT is structure-cheap up to $O(1)$; the
LOCATION half is M4." Alpöge-Furman does not contradict it and does refine it. Adopted
wording (addendum placed on [`e1s_rank_one_interlacing.md`](../../experiments/spectral/e1s_rank_one_interlacing.md)):
COUNT is structure-cheap up to $O(1)$ (Weyl-on-Q, #169); a positive PROPORTION of
LOCATION is purchasable unconditionally from the compressed form by rank-trace-inertia
bookkeeping at Fourier support 1 (2608.13637: $2/3$ at $\psi_0$, $0.6725$ at $\psi_{MT}$);
FULL location (proportion 1, completeness) remains M4 (the paper's ceiling statement
concurs for its own mechanism). The interesting object the discrepancy log predicted, the
mechanism's ceiling, is answered in-paper: the ceiling is the Fourier-support-1 wall, i.e.
exactly the pair-correlation information boundary.

**(b) An in-print, machine-verified instance of the four-level compass.** The paper
proves, about its own method, an instance of the statement this repo has been defending
as a finding:
proportion results are purchasable below the polarization requirement, and the uniform
statement is different in kind ("RH itself is out of reach of the mechanism"; even full
HL* tops out at 100 percent SIMPLE, which still is not RH). Scope kept honest: the paper's
ceiling claim covers rank/index arguments at bounded Fourier support, not every
sub-polarization method; it is an INSTANCE of the compass, not a proof of it. But it is
the first external instance that is simultaneously unconditional, record-setting, and
Lean-verified, and it lands exactly on the compressed-Weil-form object this repo probes.

**(c) The mechanism datum (candidate coordinate; derivability check run in Section 5).**
The repo's polarization frame ([`ArithmeticPolarization.lean`](../../lean/ZetaRH/ArithmeticPolarization.lean):
perfectness is free, positivity is the gap; RH iff the FE pairing is conjugation) has a
quantitative contrapositive in print: each positivity violation (off-line pair) costs
EXACTLY ONE unit of positive index in the compressed form, and the prime side bounds the
total index budget unconditionally. In one line: **indefiniteness is countable at finite
rank from prime data; positivity is not certifiable there.** Ancestry stated honestly
(adversary A2): the countability has a conditional ancestor the paper itself credits,
Montgomery 1973's multiplicity budget under RH (rowed in the atlas); the NEW content is
that off-line pairs enter the same finite-rank budget at unit weight WITHOUT RH, via
inertia. The first half is NOT derivable from the #148/#160/#194 funding clause (it
counts index, it does not fund positivity), nor from #169's Weyl-on-Q count (no index
budget, no prime funding there), nor from the repo's prior inertia usages (#72, #78:
polarity bookkeeping on candidate forms, not defect counting from prime data): it passes
the #201 derivability check as a genuinely new mechanism datum. The second half is the
same SPECIES as the repo's #199/#200 certificates (different instruments: the line meter,
the assembly family) and, at the exact register, the primes-thread pair-correlation
blindness finding (GUE data provably RH-blind). Complementarity with #199, precisely:
#199 says the line-restricted meter is blind to WHERE off-line zeros are; 2608.13637 says
the prime side nonetheless bounds HOW MANY there can be, in aggregate, with
multiplicity-and-off-line defects together at most $1/3$ of zeros at support 1.

**(d) The discipline verdict, worked (rewritten per adversary A3; sharper than the sweep
screen).** D-H: the ZERO-SIDE inertia bookkeeping poses VERBATIM (the FE pairing
$\rho \leftrightarrow 1 - \bar\rho$ plus $m_\rho \ge 1$ are all it consumes; and Theorem
B runs the mechanism on complex $\Lambda(n)\chi(n)$ coefficients, so nonnegativity is not
consumed either: the mean values consume SIZES). What fails is the PRIME-SIDE FUNDING:
$\mathrm{tr}\,\tilde G$ and the HS budget need $-f'/f$ to be a Dirichlet series in
$\sigma > 1$ with von-Mangoldt-size coefficients, and Davenport-Heilbronn's zeros in the
half-plane of absolute convergence (Titchmarsh sec. 10.25) are POLES of $-f'/f$ there, so
no such series exists; right of the zeros' abscissa the coefficients inherit
$n^{\beta - 1}$ terms from each $\sigma = \beta > 1$ zero, the $R(\psi)$ analogue
diverges, and the certificate $2 - R$ is vacuous. UNPOSABLE at the funding joint. The
split lands exactly on the conservation law's two clauses: D-H keeps the zero side and
loses the prime side; Beurling keeps a prime side and loses the FE/zero side (no pairing,
no Gabor compression of a completed form). A proportion method whose zero side D-H
SHARES and whose funding it cannot pay is a sharper discipline datum than "no Euler
product": the tariff is levied at the funding joint, precisely where the trojan ledger
says it must be.

**(e) Practical assets.** (i) The window optimization $R(\psi)$ (indicator $4/3$ vs
Montgomery-Taylor) is the repo's extremal-function genre (e4b LP family, Carneiro-Littmann
corner). Adversary-corrected scope: Montgomery-Taylor is optimal AMONG WINDOWS (CCLM17,
as the paper credits), and the paper itself prices the ceiling over ALL bandwidth-one
certificates at about $0.682$ via Chebyshev-Markov-Stieltjes moment bounds: about one
point of in-class headroom above $0.6725$ is named in-paper. The structural wall is the
support, not the constant; the functional is a named transfer target for the zero_free
tooling either way. (ii) The Lean
artifact is a VERIFIER resource: it formalizes compressed-Weil-form inertia bookkeeping
(per its Appendix A self-report, full coverage on the three standard axioms; the
hypothesis-style comparison to #S4C-2 was retired with the 2026-08-26 correction above;
audit checklist queued for the F2a skim), and is the natural
pattern library for any future SPInterface module on finite compressions. (iii) The
provenance appendix is a dated external datum for
[`proof_program_ai_only.md`](../proof_program_ai_only.md): an autonomous-model discovery,
adversarially reviewed by model instances, human-verified and Lean-formalized, at
research-record grade, in this exact problem area.

## 3. What it does NOT change

The frontier. The result is compatible with a $\beta = 0.51$ zero (the residual third is
unconstrained in location), so Level 4 is untouched; M4/R1 stand as the open kernel. The
#199/#200 certificates are about different instruments (the SP-object's line meter; the
e2ao assembly family) and are unaffected. No repo claim is contradicted; one repo wording
(#169's dichotomy) is refined as in 2(a). The four-level framing gains corroboration, not
proof.

## 4. Actions (landed with this note's integration commit)

- e1s dossier addendum (the 2(a) wording), LEARNINGS #202 entry, PHASE_STATE update:
  same commit as this note (adversary A4 flag 3: the earlier draft's "same session"
  tense corrected to this).
- QUEUED: fetch the Lean repository (URL in the paper's Appendix A; not captured by the
  HTML fetches) and skim its statement architecture for the SPInterface pattern library;
  one-line PUBLICATIONS note that PRZZ20/Wu15 citations in any future P-item should now
  cite 2608.13637 as the standing record.
- NOT queued: chasing the in-class $\approx 0.682$ ceiling (one point above
  Montgomery-Taylor, priced in-paper; the structural wall is the support, and the repo's
  effort belongs on the wall, not the point).

## 5. Adversary pass (same-day; post-adversary state, authoritative)

Five attacks were posed on the draft before integration; a general-purpose ADVERSARY
agent ran them against its own independent fetches of the paper. Outcomes, all fixes
applied above:

- **A1 (over-claim): LANDED.** The draft's 2(b) let "instance" slide into "the
  statement"; one sentence fixed, plus the 2(a) "remains M4" attribution rescoped to the
  paper's own mechanism.
- **A2 (derivability, #201 rule): the datum SURVIVES; two attributions LANDED.** The
  mechanism datum is not derivable from #148/#160/#194, #169, #199/#200, or the repo's
  prior inertia usages (#72, #78): it stands as new. Fixed: the Montgomery-1973
  conditional ancestry is now stated, and the "second half" attribution was corrected
  from "the #199/#200 bank" to "same species, different instruments; the exact register
  is the primes-thread pair-correlation blindness."
- **A3 (D-H unposability): LANDED, verdict survives, reason rewritten.** The draft
  imported "nonnegative coefficients" from the repo's S4 Euler-gate (a different route;
  Theorem B's complex $\Lambda\chi$ disproves it here) and mislocated the obstruction.
  Correct statement now in 2(d): the zero-side inertia poses for D-H; the prime-side
  FUNDING fails ($-f'/f$ has poles in $\sigma > 1$; $R(\psi)$ analogue diverges).
- **A4 (fidelity): core verbatim-faithful; one serious catch LANDED.** Every inequality
  shape, constant, ceiling quote, provenance quote, and Lean-appendix claim checked out
  against the adversary's own fetch, EXCEPT one fabricated quotation ("RH is a statement
  about individual zero locations": a summarizer gloss, not in the paper): unquoted and
  replaced with the paper's GLSS25 complementarity sentence. Also landed: the
  $\approx 0.682$ bandwidth-one-certificate ceiling the draft had waved off, and the
  Section 4 tense.
- **A5 (records): MISSED** (attributions correct as credited in-paper); optional
  precision on PRZZ20's abstract wording adopted in Section 1.
