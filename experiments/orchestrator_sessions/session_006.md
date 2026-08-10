# Session 006: the modular/Hecke rung (PHASE_STATE next-step 1), executed as three parallel builds + two adversary passes + synthesis

> 2026-08-09. Angle A chosen by Owen: execute next-step 1 (the modular/Hecke rung named
> by BOTH pivot walls, #166/#167, and by #168(iii)'s sharp question) in one night, as
> three parallel tracks under two adversary rounds, then synthesize. This file records
> the plan as executed, agent by agent, the recommended next deployment, and the open
> items. Finding-level record: LEARNINGS #173. Navigation: PHASE_STATE.md (Current
> state paragraph "The modular/Hecke rung executed").

## The plan as executed

Next-step 1 had three clauses; each became a track:

| Track | Clause | Agent | Artifact | Verdict |
|---|---|---|---|---|
| T1 | sweep Cohn-Elkies / Viazovska / Radchenko-Viazovska vs the S4 spec | SURVEYOR | [`viazovska_s4_sweep.md`](../../docs/03_research/reading_notes/viazovska_s4_sweep.md) | FITS-IN-PART |
| T2 | pose the $HB_1$ one-sided extremal-theorem question | SURVEYOR | [`hb1_one_sided_extremal.md`](../../docs/03_research/reading_notes/hb1_one_sided_extremal.md) | NO-IN-PRINT / OPEN |
| T3 | verify the negative-square ansatz against Burnol's literal bilinear extension | BUILDER | [`e1w_burnol_bilinear.md`](../spectral/e1w_burnol_bilinear.md) (+ `.py`, `.npz`) | CORRECTED: $\kappa(L_a) = 0$ |

Two adversary rounds, both completed the same night:

- [`_modular_rung_adversary.md`](../../docs/03_research/reading_notes/_modular_rung_adversary.md)
  (T1/T2 + cross-consistency with e1w): T1 **PASS_WITH_FIXES**, T2 **PASS_WITH_FIXES**;
  five attacks B1-B5, none LANDED (two GLANCED). Adjudicated the BRS conditionality
  discrepancy in T1's favor at source; independently replicated the whole K-W sweep with
  a second toolchain (pypdf vs pdftotext) including an evasion-vocabulary probe; found
  the three-way Euler-product agreement (the contraction/loading joint) instead of the
  contradiction it hunted; proposed six exact annotations, all applied at synthesis.
- [`_e1w_adversary.md`](../spectral/_e1w_adversary.md): **PASS**, all six pre-registered
  attacks MISSED. Reproduction exact (24/24 full, 18/18 quick, npz md5 unchanged);
  source fidelity verbatim (the paper defines no indefinite pairing anywhere); the
  residue dictionary re-derived independently with signature invariant under every
  convention perturbation; beyond-grid probes to $a = 2.5$ hold at margin
  $\ge 2.7 \times 10^{14}$; the twisted-pairing Krein escape NARROWED (non-Pontryagin,
  $\kappa = \infty$; only the 2-dim quotient carries the $(1,1)$).

## Agent-by-agent outcomes

**SURVEYOR (T1).** The last named unswept corner of the frame audit is closed. Positive
half: the banked S4 spec's mechanism class is NON-EMPTY IN NATURE (the Viazovska magic
function: infinitely many prescribed double zeros at $O(1)$ dimension cost, sourced by
modular rigidity = finite-dimensional coefficient spaces of bounded-pole-order forms).
Negative half, the disqualifier named: at log nodes the mechanism class IS the
Riemann-Weil explicit formula (BRS 2005.02996, unconditional at source, dual nodes = the
zeta zero multiset) and its one-sided version IS M4. Frame-vs-collapse typed: the
interpolation organ is exactly-critical (the KNS-frame / S4-collapse boundary); the
$o(M)$ economy lives only in the magic-function/LP organ.

**SURVEYOR (T2).** The K-W six-part series is CLOSED as a search target (zero one-sided
extremal content, adversary-replicated); the obstruction named at the exact step
(quadrature-weight and spectral-measure positivity both destroyed at a finite located
set); the fork finding (posed-but-blind vs data-sensitive-but-unposed) is a
conservation-law echo and a reusable screen. #164's corridor closure is triple-hardened
by this dossier, quadruple with T3.

**BUILDER (T3, e1w).** The pre-registered outcome CORRECTED fired: the literal extension
is a positive Gram block, signature $(2,0)$, at every $a$; #168(iii)'s $\kappa = 1$ was
correct algebra applied to the wrong pairing (the $(1,1)$ belongs to the
$\mathcal{F}_+$-twisted form only). Durable products: the residue dictionary
($\mathrm{Res}_1 M(f) = -f(0^+)$, $Y_0 = -\mathcal{F}_+Y_1$, closing #168's largest
named gap) and the measured coupling profile ($N, -\beta$ super-exponentially decaying,
$|\beta|/N \to 1$). Three Lean-friendly VERIFIER targets named in its Section 11.

**ADVERSARY (both rounds).** No verdict overturned; one banked finding removed
(#168(iii)); the structural downgrade shown FORCED, not merely measured (Gram + Prop 4.5
means no resolution failure or larger $a$ can flip it); and the round's one genuinely
new cross-cutting fact is the adversary's (the three-way Euler-product placement at the
contraction/loading joint, never in FE/pole geometry).

**SYNTHESIZER (this session).** Applied all six proposed annotations (the kns pin BRS
adjudication; T1 verdict calibration + the Riemann-Weil gloss retag; T2's e1w rescoping
block; the `la_negative_square_check.md` scratchpad-citation cure, superseded by tracked
e1w); wrote LEARNINGS #173 and the #168 downgrade note; updated PHASE_STATE (new
Current-state paragraph, Next steps rewritten around the BRS-skeleton probe, rotation of
#163/#164/#166-#170 paragraphs and the older last-verified blocks into the archive);
added the Arch 1G (e1w) row to PROOF_ARCHITECTURES_PLAN; updated TODO (pivot rungs (a)
and (b) checked with outcomes; three new open items). Regression at synthesis:
`run_all_tests` GREEN 9/9 (e1w is NOT auto-discovered, by the `test_*`/`smoke_test`
naming pattern); e1w quick 18/18.

## Honest frontier accounting

UNMOVED. No attack on M4 advanced; one candidate mechanism (the $\kappa = 1$ indefinite
route) was removed, and the strongest external validation yet of the S4 spec's shape was
banked (the mechanism class exists in nature; its log-node price is exactly the wall).
The round produced coordinates, not progress on the sign itself, and says so.

## Recommended next deployment (session 007)

1. **BUILDER round: the BRS-skeleton probe, build spec first** (the
   [`theta_s4_build_spec.md`](../../docs/03_research/theta_s4_build_spec.md) precedent:
   spec with pre-registered exits and screens BEFORE code). Content: e1o's
   rank/cost-ratio instrument on the BRS skeleton at finite horizon (nodes
   $\{\log n/(4\pi)\}_{n \le N}$ + the prime sublattice, zero side SYMBOLIC, K1-guarded,
   Beurling twin = no FE). Pre-registered wall: the economy prices as M4, which would
   identify this corpus's wall with #171's chain wall as provably the same joint. That
   identification, if it lands, is itself a keeper (a fourth coordinate system tied to
   the third).
2. **SURVEYOR riders (cheap, parallel):** the positive allow-poles extremal question
   (search key "finite-dimensional extensions of $\mathcal{H}(E)$ / de Branges spaces of
   meromorphic functions, extremal problems"); T2's rescoped missing-theorem statement
   stays banked as a screen, not a search target. The WATCH sweep is overdue
   (~2026-08-01 cadence).
3. **Optional VERIFIER:** e1w's V1-V3 (residue dictionary; $Y_0 = -\mathcal{F}_+Y_1$;
   the PSD-kernel-with-off-axis-poles incompatibility lemma), all elementary.

## Open items

- **The round is UNCOMMITTED** pending Owen's per-action authorization. Per the evidence
  rule, `e1w_burnol_bilinear.npz` must land in the SAME commit as the citing dossier
  (adversary bookkeeping note; all three e1w files plus the two reading notes, two
  adversary reports, and the synthesis edits belong in one commit).
- The `la_negative_square_check.md` evidence-rule cure is APPLIED (annotation, not
  recovery; the machine-local script stays lost, its computation superseded at source
  tier by tracked e1w).
- e1w adversary case A2's narrowed escape (a Krein-space reading of the twisted pairing
  on the 2-dim quotient only) stays OPEN at low priority; nobody has posed a use for it.
- e1v adversary cases 3 (scope) and 7 (independent K1 re-verification) remain NOT RUN
  (inherited from #172).
