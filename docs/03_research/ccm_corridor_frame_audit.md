# The CCM corridor frame audit: choices stated as law, the verification loop's blind spots, and a pre-registered exit

> Dossier, 2026-07-17. A frame audit of the CCM corridor (LEARNINGS #154-#162; experiments
> e1k-e1o) per the #133 precedent: audit the frame, not the findings. Two independent agent
> lenses ran the same day: a frame-assumption audit (Appendix A: what in the corridor's
> conclusions is THEOREM, what is MEASURED, and what is a CHOICE quietly stated as law, plus
> where the verification loop cannot see its own axioms) and a portfolio/opportunity-cost audit
> (Appendix B: what elsewhere in the repo has been decaying while the corridor ran). One-line
> verdict: TIME-BOX. One more round, with the exit rule pre-registered before the round is run.
> Integrated as LEARNINGS #163.
>
> Cross-links: [`ccm_semilocal_prolate.md`](ccm_semilocal_prolate.md) (the corridor's own
> ledger, audited here), [`s4_carrier_audit.md`](s4_carrier_audit.md) and
> [`landau_one_sided.md`](landau_one_sided.md) (the two arcs most of Section 1's choices sit
> on), [`missing_object_interface.md`](missing_object_interface.md) (the pivot target in
> Section 4), [`LEARNINGS.md`](../../experiments/LEARNINGS.md) (#154-#163). No em dashes
> anywhere.

## 1. Choices stated as law

A frame audit's job is to sort a corridor's conclusions by what actually holds them up, not by how confidently they read. Seven claims the CCM corridor's dossiers lean on turn out, on inspection, to split across three tiers: proven theorem, a measured result quietly generalized past what was measured, and outright choice presented with a theorem's confidence. Tiers and citations preserved from the audit:

**A. "Uniform Section-7 convergence implies RH" is THEOREM, but only in one direction.** The forward implication is a THEOREM (the Hurwitz contrapositive; [`ccm_semilocal_prolate.md`](ccm_semilocal_prolate.md), Addendum 2026-07-02 (second), item 1). The converse, "RH implies convergence," is flagged UNPROVEN in the same paragraph. So "the Section-7 limit is the RH wall" is a half-theorem: RH-hard, not RH-equivalent.

**B. "The Section-7 limit IS M4 (a polarization)" is a CHOICE.** It rests on two legs, both soft. First, "the only identified sufficient input is uniform ground-state control of the truncated Weil form" (#154) is a search summary, not a necessity proof; the dossier itself installs escape condition (++), "a zero-free geometry-sourced proof of the uniform control not routed through Weil positivity" ([`ccm_semilocal_prolate.md`](ccm_semilocal_prolate.md), Addendum 2026-07-02 (second)), which concedes the positivity route is not known to be forced. Second, the "RH-equivalent positivity step" wording is the repo's Bombieri-Weil gloss: the banked e1m surveyor D2 flag records fetched-absence, "CCM's own Section 7 never says positivity" ([`ccm_semilocal_prolate.md`](ccm_semilocal_prolate.md), Addendum 2026-07-11, gloss note). This is the exact move #133 retracted globally ("Level 4 = positivity" was a choice stated as a law), reinstated locally: every corridor probe that finds a non-positivity clause (H4-existence, window growth, inheritance) is re-described as "the Section-7 identification in another costume" (#160 A1, #161), which enforces convergence-on-M4 by re-description: the #133 artifact pattern, verbatim.

**C. "Finite-cutoff reality is information-free" is THEOREM, but its totalization is CHOICE at the margin.** The theorem itself is proven (Theorem 5.10(iii); #154, #158). But "ALL finite-lambda content lives in the uniform limit" is MEASURED per tested observable (spectrum e1k, count e1l, four faces e1m, comb face e1n) and then generalized: CHOICE at the margin. The corridor's own data carries a counter-signal: branches of one $(\lambda, N)$ point differ 100x in $\Xi$-proximity, the dressing is unexplained, and "part of the observed cap is removable dressing" (#161), i.e. finite-lambda structure exists that the information-free framing gives no reason to study, and the corridor accordingly did not pursue it.

**D. "The det-class limit clause equals the M4 polarization" (#148's clause) is MEASURED-IDENTICAL at one family, promoted to a corridor-wide law.** This is a MEASURED-IDENTICAL finding at this one family (#154's coincidence finding, explicitly "open in general"), promoted to load-bearing shorthand corridor-wide. As a law it inherits choice B's gloss.

**E. "The CCM $D_{\log}$ carrier is the right home to pose S4/Spec(Z)-Stepanov" is a CHOICE, and a convenience-loaded one.** The reroute was born inside the corridor itself ([`landau_one_sided.md`](landau_one_sided.md), Sections 3.4-3.6), and e1o reuses the e1k caches, "no operator rebuilt" ([`e1o_s4_carrier.md`](../../experiments/spectral/e1o_s4_carrier.md), header). The probe then measured the premise away where it could actually test it: at fixed type the carrier's function space "is the generic trig space" (majorant-nil, structural; [`e1o_s4_carrier.md`](../../experiments/spectral/e1o_s4_carrier.md), banner (3)); horizon consonance is graded observation-tier consonance, not evidence of home-rightness ([`s4_carrier_audit.md`](s4_carrier_audit.md), 4.1); and the one carrier-distinctive family (the true eigenbasis, the Sonin projector) was "untestable from cache" (#162). The carrier premise is verified only where the carrier is generic, and unverified exactly where it is distinctive.

**F. "S4 equals well-conditioned rank collapse at $\{k \log p\}$ inside a band-limited majorant skeleton" is a CHOICE of formalization.** ([`e1o_s4_carrier.md`](../../experiments/spectral/e1o_s4_carrier.md), Q1, "the formalization chosen"). The $\mathbb{F}_q$ Stepanov engine is an auxiliary-function-plus-derivation argument, not a majorant pairing; the divergence and horizon theorems are theorems about the chosen skeleton. The spec is honestly banked at conjecture tier, but downstream claims ("the slot is measured empty") quietly inherit the formalization.

**G. "Frontier: UNMOVED" as the grade is a bookkeeping CHOICE.** The frontier is defined as M4/BRIDGE-H, which the corridor's own theorems (A, C above) place at an unreachable limit; K1-clean finite probes on this family are then structurally guaranteed to grade UNMOVED. Five UNMOVED verdicts across five arcs are partly the frame grading itself, not five independent misses.

## 2. The verification loop's blind spots

The choices in Section 1 persist because the loop that checks them cannot see past its own setup. Four structural blind spots, not incidental gaps:

**One implementation, verified against itself.** Every e1l-e1o number descends from the single e1k `build_float` harness; adversary rounds reproduce within the same code and branch family. e1n's catch 3 proved the measured object is `dps`-branch-dependent (fill counts "branch-specific, not intrinsic to lambda," #161), so the dressing, fill, and comb-error findings are properties of one reimplementation's branch structure, not settled properties of the mathematics. The out-of-frame null this never ran: an independent build (a different basis, a different precision path, or the paper's exact operator).

**Controls are input twins, never carrier twins.** D-H and Beurling enter as coefficient streams through the same carrier; "Beurling runs IDENTICALLY" is proven on exact comb functions, with the caveat "not a Beurling CCM build (none exists)" (#161 caveats; #162). No probe ever built a rival carrier. Consequently "the S4 slot on the CCM carrier is measured empty" ([`s4_carrier_audit.md`](s4_carrier_audit.md), 4.4) cannot be distinguished from "the slot on every band-limited carrier is empty"; e1o's own generic-space note predicts they are the same measurement. The out-of-frame null: e1o's T4 battery run verbatim on a non-CCM carrier (a plain Paley-Wiener space, a matched-density random-frequency comb, a de Branges space with a different $E$).

**Absence claims verified in corridor vocabulary only.** The two VERIFIED-ABSENT findings ([`s4_carrier_audit.md`](s4_carrier_audit.md), 2.1-2.2) were searched under Stepanov, majorant, and Sonin terms. A repo-wide grep returns ZERO mentions of Cohn-Elkies, Viazovska, or sphere packing. This is the audit's sharpest catch: the one field where a one-sided band-limited extremal problem was closed sharply by a lattice-consuming modular identity (the Cohn-Elkies/Viazovska LP bounds; Radchenko-Viazovska Fourier interpolation at $\sqrt{n}$ nodes) is precisely the mechanism class of the banked S4 spec ("sourced by an identity that FAILS for perturbed logs"), and it was never swept. The absences are true in the searched vocabulary and untested in the nearest adjacent one.

**Who grades movement.** The same session set poses the question, defines the nulls, and grades UNMOVED. #133's lesson was that this loop cannot see its own axiom; the corridor rebuilt the loop with better hygiene, but the same topology.

## 3. Frame falsifiers

Five checks. Each would overturn a load-bearing choice from Section 1 rather than merely narrow a constant, so each is a genuine falsifier of the corridor's frame, not another measurement inside it. Cheapest tripping check named for each:

1. **The Sonin projector lands blind.** Build the projector (the named BUILDER item, [`s4_carrier_audit.md`](s4_carrier_audit.md), Section 7) with a Beurling twin and pre-registered criteria. If its rank behavior at $\{k \log p\}$ matches the generic families or the fake at the accessible window, the carrier has no distinctive structure anywhere, tested or untested; "S4 on the CCM carrier" reduces to "S4 anywhere," and choice E (the home claim) is dead. Cheapest check: one probe, the existing caches plus a new eigenbasis build.
2. **Carneiro-Littmann is ill-posed in the Sonin space.** If the Sonine/de Branges chain lacks the structure the one-sided extremal theory needs, the corridor's question is a category error, not an open problem. Cheapest check: the already-named SURVEYOR fetch (Burnol's Sonine-as-$H(E)$ structure against the Carneiro-Littmann hypotheses).
3. **Generic-carrier replication.** Run e1o's multiplicity battery on a matched non-CCM carrier (a code-reuse day, not a new build). Identical output falsifies "on the CCM carrier" as adding any content beyond "on a band-limited carrier."
4. **The interpolation-identity check.** A WebFetch pass on Fourier uniqueness/interpolation pairs (Radchenko-Viazovska; Ramos-Sousa; Kulikov-Nazarov-Sodin): does any node-tied band-limited identity exist at a $\mathbb{Q}$-linearly independent set like $\{k \log p\}$, or are all known constructions lattice-commensurate? If provably lattice-tied, the spec's identity clause cannot be filled on the log-line at all, and the mechanism lives on the theta/functional-equation side, off this carrier. Either branch moves the question.
5. **The $\theta \le 1/2$ Beurling corner** (the screen's one [UNVERIFIED-MEMORY] escape, [`s4_carrier_audit.md`](s4_carrier_audit.md), Section 3). If sub-$\sqrt{x}$ density regularity turns out to force the RH-analogue, the corridor's central reading, that the lattice is the only glue, is wrong. Cheapest check: the named SURVEYOR fetch (Zhang; Debruyne-Vindas; Revesz).

## 4. Verdict and the pre-registered exit rule

Time-box: one more round, trigger named in advance, then pivot. The round runs falsifiers 1 and 2 (the Sonin-projector probe with a Beurling twin, and the Carneiro-Littmann well-posedness check), with falsifiers 3 and 4 riding along cheaply on the same session.

Exit rule, pre-registered before the round runs: if the Sonin projector lands blind, OR the extremal problem is ill-posed in the Sonin space, the corridor closes as a proof home and is reclassified as what it has demonstrably been since e1k: the project's best measurement instrument and discipline-sharpener.

Pivot target, named now rather than found later: the lattice side the corridor's own results keep pointing at. e1m proved the pin's engine IS Poisson/theta duality, and that the #152 clause is paid by construction there, so the S4 spec's identity clause should next be attempted on the theta/modular-interpolation side. The counting-side joint, C1 = SP2 AND SP3 (needs no positivity, and is not carrier-bound), is the standing alternative ([`missing_object_interface.md`](missing_object_interface.md), Section 2; its own Section 5 already instructs: "the next move is a build at a joint, not another survey").

Reasons, no hedging. Continuing as-is is wrong: choice G above (Section 1) shows the frame guarantees UNMOVED verdicts on this family, so more runs in place would only manufacture further instances of the same non-finding. Pivoting immediately is also wrong: one carrier-distinctive object remains untested, and abandoning the corridor now would leave the "wrong home" conclusion itself unverified, which the project's mindset does not permit ([`researcher_mindset.md`](../researcher_mindset.md)).

The corridor was not wasted. It produced carrier-independent screens, the DMV kill, the divergence theorem, the incommensurability measurement, the Landau translator, that any future S4 candidate must pass. Those are coordinates. The remaining question is one probe wide, and the honest move is to run it with the exit already written.

## 5. Opportunity cost and decay

While the corridor ran, the audit's second lens (Appendix B) checked the rest of the portfolio for decay. Full inventory in Appendix B Section 1; the load-bearing rows:

**HIGH stale-risk: the Mathlib pipeline.** P1/P2 ([`PUBLICATIONS.md`](../../PUBLICATIONS.md)): Owen owed round-1 replies, and a 2026-07-10 flag that P1 might have closed was never polled. Open PRs decay by reviewer goodwill and silent close; this was, in the audit's words, "the single most decayed item in the repo: 7 days on an unconfirmed possible closure, 14 days since last PR action." Resolved same-day; see Section 6.

**MEDIUM stale-risk:** P10 (the rational-root floor, CLEAR-TO-PR since 2026-07-02; every week of master drift raises the port cost) and the WATCH sweep (four analytic shapes of R1 plus the named submission watches, two weeks stale, where a missed R1 event is the inventory's one unbounded cost).

**Everything else reads LOW or NONE stale-risk:** P9, P11, P4, P5/P6/P7, the C1 counting-joint/SP3c-W6 rung, the toy sandbox, the Lean/VERIFIER backlog, the M4/C2 construction coordinates, small experiments, and the docs/viz backlog are conjecture-stable, human-gated, or exposed only to scoop risk, not to decay.

**State drift caught in the same pass:** TODO 190 was stale (marked "READY: submit" when P1/P2 had already been submitted with round-1 review addressed); TODO 195 (the P8 lit-check) was done but still showed as an open checkbox; TODO 194's portfolio decision listed a standalone set {P1, P2, P6} the registry had already outgrown (P9, P10, P11 added since, P11 pre-decided standalone inside its own dossier); [`PUBLICATIONS.md`](../../PUBLICATIONS.md)'s P9 entry still ended "Then draft" after the draft was already written and gate-checked; and the citation-check target #5 RE-RUN had no open checkbox of its own, only a closed one and prose in [`PHASE_STATE.md`](../../PHASE_STATE.md), meaning it could have been silently lost.

**Portfolio split recommended for the next three sessions:** roughly 40% corridor completion (the Sonin-projector probe plus rank-one interlacing, then pause), 25% non-corridor (the WATCH sweep and the SP3c/W6 derived-base rung, the counting joint's non-CCM half), and 35% shipping (poll and reply on P1/P2, open the P10 PR, package P9). The decay gradient points entirely at the Mathlib/arXiv pipeline, where finished mathematics was sitting idle past the two-week line.

## 6. Same-day resolutions and actions (2026-07-17)

The following happened the same day as the audit, in direct response to it.

**(a) The P1 flag resolved.** A direct GitHub API poll resolved the stale P1 flag from Section 5: [mathlib4#41133](https://github.com/leanprover-community/mathlib4/pull/41133) (`riemannZeta_conj`) was MERGED BY BORS on 2026-07-07. GitHub shows `state=closed`, `merged=false`, with the "[Merged by Bors]" title prefix, which is Mathlib's merge signature, not a closure; the 2026-07-10 spot check misread it as one. This is the project's first Mathlib-merged contribution. P2 ([mathlib4#41132](https://github.com/leanprover-community/mathlib4/pull/41132)) is OPEN with fresh reviewer activity dated 2026-07-17; replies are still owed.

**(b) The evidence rule.** The repo-level `scratchpad/` directory is confirmed ABSENT on the current machine, so any tracked file's citation into it, including the P10 novelty passes, is a dangling pointer here. An evidence rule was added to [`CLAUDE.md`](../../CLAUDE.md): anything cited as evidence from a tracked file must itself be tracked at write time.

**(c) Housekeeping.** [`PHASE_STATE.md`](../../PHASE_STATE.md) and [`TODO.md`](../../TODO.md) were compacted, with the removed history preserved in [`PHASE_STATE_ARCHIVE.md`](../../PHASE_STATE_ARCHIVE.md) and [`TODO_ARCHIVE.md`](../../TODO_ARCHIVE.md). [`experiments/run_all_tests.py`](../../experiments/run_all_tests.py) was added as a test aggregator and runs green at 9/9 modules; the repo has no CI, so this is the regression net.

**(d) Provenance.** This dossier synthesizes the two agent reports named in the STATUS line above; the reports themselves are reproduced verbatim in Appendix A and Appendix B below.

---

## Appendix A: Report 1, the frame-assumption audit (verbatim)

*Reproduced verbatim from the agent report supplied for this audit (2026-07-17). Section headers renumbered one level down to nest under this appendix.*

### 1. CHOICES-STATED-AS-LAW

**A. "Uniform Section-7 convergence => RH."** THEOREM (Hurwitz contrapositive; `ccm_semilocal_prolate.md`:Addendum 2026-07-02 (second), item 1). The converse "RH => convergence" is flagged UNPROVEN in the same paragraph. So "the Section-7 limit is the RH wall" is a half-theorem: RH-hard, not RH-equivalent.

**B. "The Section-7 limit IS M4 (a polarization)."** CHOICE. It rests on two legs, both soft. (i) "The only identified sufficient input is uniform ground-state control of the truncated Weil form" (#154) is a search summary, not a necessity proof; the dossier itself installs escape condition (++), "a zero-free geometry-sourced proof of the uniform control not routed through Weil positivity" (`ccm_semilocal_prolate.md`:Addendum 2026-07-02 (second)), which concedes the positivity route is not known to be forced. (ii) The "RH-equivalent positivity step" wording is the repo's Bombieri-Weil gloss: the banked e1m surveyor D2 flag records fetched-absence, "CCM's own Section 7 never says positivity" (`ccm_semilocal_prolate.md`:Addendum 2026-07-11, gloss note). This is the exact move #133 retracted globally ("Level 4 = positivity" was a choice stated as a law), reinstated locally: every corridor probe that finds a non-positivity clause (H4-existence, window growth, inheritance) is re-described as "the Section-7 identification in another costume" (#160 A1, #161), which enforces convergence-on-M4 by re-description, the #133 artifact pattern verbatim.

**C. "Finite-cutoff reality is information-free."** THEOREM (Thm 5.10(iii); #154/#158). But the totalization "ALL finite-lambda content lives in the uniform limit" is MEASURED per tested observable (spectrum e1k, count e1l, four faces e1m, comb face e1n) and then generalized: CHOICE at the margin. The corridor's own data carries a counter-signal: branches of one (lambda, N) point differ 100x in Xi-proximity, the dressing is unexplained, and "part of the observed cap is removable dressing" (#161), i.e. finite-lambda structure exists that the information-free framing gives no reason to study and the corridor accordingly did not pursue.

**D. "The det-class limit clause equals the M4 polarization" (#148's clause).** MEASURED-IDENTICAL at this one family (#154's coincidence finding, explicitly "open in general"), promoted to load-bearing shorthand corridor-wide. As a law it inherits B's gloss.

**E. "The CCM D_log carrier is the right home to pose S4/Spec(Z)-Stepanov."** CHOICE, and convenience-loaded: the reroute was born inside the corridor (`landau_one_sided.md`:3.4-3.6) and e1o reuses the e1k caches, "no operator rebuilt" (`e1o_s4_carrier.md`:header). The probe then measured the premise away where it could test it: at fixed type the carrier's function space "is the generic trig space" (majorant-nil, structural; `e1o_s4_carrier.md`:banner (3)), horizon consonance is graded observation-tier consonance, not evidence of home-rightness (`s4_carrier_audit.md`:4.1), and the ONE carrier-distinctive family (true eigenbasis / Sonin projector) was "untestable from cache" (#162). The carrier premise is verified only where the carrier is generic and unverified exactly where it is distinctive.

**F. "S4 = well-conditioned rank collapse at {k log p} inside a band-limited majorant skeleton."** CHOICE of formalization (`e1o_s4_carrier.md`:Q1, "the formalization chosen"). The F_q Stepanov engine is an auxiliary-function-plus-derivation argument, not a majorant pairing; the divergence and horizon theorems are theorems about the chosen skeleton. The spec is honestly banked at conjecture tier, but downstream claims ("the slot is measured empty") quietly inherit the formalization.

**G. "Frontier: UNMOVED" as the grade.** Bookkeeping CHOICE. The frontier is defined as M4/BRIDGE-H, which the corridor's own theorems (A, C) place at an unreachable limit; K1-clean finite probes on this family are then structurally guaranteed to grade UNMOVED. Five UNMOVED verdicts are partly the frame grading itself, not five independent misses.

### 2. VERIFICATION-LOOP BLIND SPOT

**One implementation, verified against itself.** Every e1l-e1o number descends from the single e1k `build_float` harness; adversary rounds reproduce within the same code and branch family. e1n's catch 3 proved the measured object is dps-branch-dependent (fill counts "branch-specific, not intrinsic to lambda", #161), so the dressing/fill/comb-error findings are properties of one reimplementation's branch structure. Out-of-frame null: an independent build (different basis, different precision path, or the paper's exact operator).

**Controls are input twins, never carrier twins.** D-H and Beurling enter as coefficient streams through the same carrier; "Beurling runs IDENTICALLY" is proven on exact comb functions, with the caveat "not a Beurling CCM build (none exists)" (#161 caveats; #162). No probe ever built a rival carrier. Consequently "the S4 slot on the CCM carrier is measured empty" (`s4_carrier_audit.md`:4.4) cannot be distinguished from "the slot on every band-limited carrier is empty"; e1o's own generic-space note predicts they are the same measurement. Out-of-frame null: e1o's T4 battery run verbatim on a non-CCM carrier (plain PW space, matched-density random-frequency comb, a de Branges space with a different E).

**Absence claims verified in corridor vocabulary.** The two VERIFIED-ABSENT findings (`s4_carrier_audit.md`:2.1-2.2) were searched under Stepanov/majorant/Sonin terms. A repo-wide grep returns ZERO mentions of Cohn-Elkies, Viazovska, or sphere packing: the one field where a one-sided band-limited extremal problem was closed sharply by a lattice-consuming modular identity (the LP bounds; Radchenko-Viazovska Fourier interpolation at sqrt(n) nodes) is precisely the mechanism class of the banked S4 spec ("sourced by an identity that FAILS for perturbed logs") and was never swept. The absences are true in the searched vocabulary and untested in the nearest adjacent one.

**Who grades movement.** The same session set poses the question, defines the nulls, and grades UNMOVED. #133's lesson was that this loop cannot see its own axiom; the corridor rebuilt the loop with better hygiene but the same topology.

### 3. FRAME FALSIFIERS (wrong home, not hard)

1. **The Sonin projector lands blind.** Build the projector (the named BUILDER item, `s4_carrier_audit.md`:7) with a Beurling twin and pre-registered criteria. If its rank behavior at {k log p} matches the generic families or the fake at the accessible window, the carrier has no distinctive structure anywhere, tested or untested; "S4 on the CCM carrier" reduces to "S4 anywhere" and the home claim is dead. Cheapest: one probe, the caches plus a new eigenbasis build.
2. **Carneiro-Littmann is ill-posed in the Sonin space.** If the Sonine de Branges chain lacks the structure the one-sided extremal theory needs, the corridor's question is a category error, not an open problem. Cheapest: the already-named SURVEYOR fetch (Burnol's Sonine-as-H(E) structure vs the Carneiro-Littmann hypotheses).
3. **Generic-carrier replication.** Run e1o's multiplicity battery on a matched non-CCM carrier (a code-reuse day). Identical output falsifies "on the CCM carrier" as adding content.
4. **The interpolation-identity check.** WebFetch pass on Fourier uniqueness/interpolation pairs (Radchenko-Viazovska; Ramos-Sousa; Kulikov-Nazarov-Sodin): does any node-tied band-limited identity exist at a Q-linearly independent set like {k log p}, or are all known constructions lattice-commensurate? If provably lattice-tied, the spec's identity clause cannot be filled on the log-line at all and the mechanism lives on the theta/FE side, off this carrier. Either branch moves the question.
5. **The theta <= 1/2 Beurling corner** (the screen's one [UNVERIFIED-MEMORY] escape, `s4_carrier_audit.md`:3). If sub-sqrt density regularity turns out to force the RH-analogue, the corridor's central "the lattice is the only glue" reading is wrong. Cheapest: the named SURVEYOR fetch (Zhang, Debruyne-Vindas, Revesz).

### 4. VERDICT

**Time-box: one more round, trigger named, then pivot.** Run falsifiers 1 and 2 (the Sonin-projector probe with a Beurling twin, and the Carneiro-Littmann well-posedness check), with 3 and 4 as cheap riders. Exit rule, pre-registered: if the Sonin projector lands blind OR the extremal problem is ill-posed in the Sonin space, the corridor is closed as a proof home and reclassified as what it has demonstrably been since e1k: the project's best measurement instrument and discipline-sharpener. Pivot target: the lattice side the corridor's own results keep pointing at. e1m proved the pin's engine IS Poisson/theta duality and that the #152 clause is paid by construction there, and the S4 spec's identity clause should be attempted on the theta/modular-interpolation side, and the counting-side joint C1 = SP2 AND SP3, which needs no positivity and is not carrier-bound, is the standing alternative (`missing_object_interface.md`:2, and Section 5's own instruction: "the next move is a build at a joint, not another survey"). Reasons, no hedging: continuing as-is is wrong because Section 1G shows the frame guarantees UNMOVED verdicts on this family; pivoting immediately is wrong because one carrier-distinctive object remains untested, and abandoning it now would leave the "wrong home" conclusion itself unverified, which the mindset doc does not permit. The corridor was not wasted: it produced carrier-independent screens (the DMV kill, the divergence theorem, the incommensurability measurement, the Landau translator) that any future S4 candidate must pass. Those are coordinates. The remaining question is one probe wide, and the honest move is to run it with the exit already written.

## Appendix B: Report 2, the portfolio and opportunity-cost audit (verbatim)

*Reproduced verbatim from the agent report supplied for this audit (2026-07-17). Section headers renumbered one level down to nest under this appendix.*

### 1. INVENTORY: open non-corridor coordinates with zero attention since 2026-07-10

| Item | Source | Cost | Stale-risk |
|---|---|---|---|
| P1/P2 Mathlib PRs: Owen posts round-1 replies; confirm P1 #41133 merged vs CLOSED (flag raised 2026-07-10, never polled) | PUBLICATIONS.md P1/P2; TODO 190 | Cheap (human minutes + one agent poll) | HIGH: open PRs decay (reviewer goodwill, master conflicts, silent close) |
| P10 rational-root floor: open the mathlib4 PR (CLEAR-TO-PR since 2026-07-02; #RR-1/#RR-2 machine-checked; port to master) | PUBLICATIONS.md P10 | Cheap-medium (one session) | MEDIUM: master drifts, naming churn, scoop risk |
| P9 paired-subtorus note: MathSciNet session, citation pins, author/ack calls, arXiv package (draft compiles since 2026-07-01) | PUBLICATIONS.md P9; TODO 235 | Cheap (human-gated) | LOW-MEDIUM: scoop risk only |
| P11 tameness-trade gates: expert model-theorist reader, verify remaining FETCH-tagged attributions, keystone-stays-open watch | PUBLICATIONS.md P11 | Medium | LOW (but keystone watch is an external-event risk) |
| P4 survey: expert reader for the (iii) polarization column, (HIGH-1) Deninger + prismatic/THH read | PUBLICATIONS.md P4; TODO 200, 211 | Expensive (multi-session) | NONE (sequenced after P1/P2 anyway) |
| P5/P6/P7 portfolio decisions (fold vs standalone; P6 multi-month Hasse route) | TODO 192, 194, 204 | Cheap decisions / expensive P6 | LOW; P6 has mild external coupling (FLT may supply Tate-module infra) |
| C1 counting joint, derived-base half: the SP3c/W6 rung on the ghost/THH self-product (the interface doc's own directive: "build at a joint, not another survey"); B2 Lean interface | missing_object_interface.md section 4 | Expensive (BUILDER) | NONE (conjecture-stable) |
| WATCH list (now 4 analytic shapes of R1): variety-free purity, sieve bilinear power-saving trigger, det-class trace formula w/ pole budget, S4-carrier shape; plus Dor-Hrushovski, CCM-axis polarization, dBN PF-order line, Connes/Consani/Moscovici/van Suijlekom submissions | sourcing_gap_r1.md; PHASE_STATE #155 | Cheap (SURVEYOR sweep) | MEDIUM: last full sweep 2026-07-03; missing an R1 event is the one unbounded cost |
| Toy sandbox: H2 mesh-min-monotonicity conjecture (possible small proof), VT-PS1..4 Lean targets, SC rung (genus-2 cohn_criterion instantiation and/or its Mathlib PR) | TODO 236, 238 | Cheap (session each) | NONE |
| Lean/VERIFIER backlog: V4 G_log rigidity + slope-1/flat-comb pair; #MTF-2 CompatibleRing transport (multi-day); ADVERSARY residual A3; citation-check target #5 RE-RUN | TODO 179, 219, 222; PHASE_STATE #156/#157 | Cheap-medium each | LOW (Mathlib version drift only) |
| M4/C2 construction coordinates: local-to-global Weil cohomology (TODO 258), 9A AHK lattice target (261), MC.4 coupling (271), q-lift (253), R3.6.3 infra (297) | TODO | Expensive (research-grade) | NONE |
| Small experiments: e3x rung 7 LP protocol (175), ECC e1x spectral-leakage (164), 12.4' Gaussian-smoothed EF route (260) | TODO | Cheap compute | NONE |
| Docs/viz backlog: intuitive + undergrad docs, implications, 6 manim scenes, PDF conversions, glossary, notebooks; ML/data pipeline items | TODO 332-357 | Cheap-medium | NONE |

Corridor-adjacent residues (not crowded out, named by the corridor itself): Sonin-projector family, rank-one interlacing, von Koch/Schoenfeld citation pin, theta <= 1/2 Beurling corner, Carneiro-Littmann well-posedness, complex ghost class + sqrt13, e1n/e1o classical Lean targets (TODO 325-328).

### 2. STATE DRIFT

- TODO 190 is stale: P1+P2 marked "READY: submit" but both were SUBMITTED 2026-06-28 with round-1 review addressed 2026-07-03. The real open action is Owen's reply plus the unresolved 2026-07-10 flag that P1 may be CLOSED (registry still shows SUBMITTED; GitHub never polled). This is the single most decayed item in the repo: 7 days on an unconfirmed possible closure, 14 days since last PR action.
- TODO 195 (P8 lit-check) is actually done: line 212 records (LOW-8) DONE 2026-06-16 with verdict "no standalone novelty, fold into P4 Pillar 3". The open checkbox at 195 should be closed.
- TODO 194 (portfolio decision) is outdated: it lists the standalone set as {P1, P2, P6}, but PUBLICATIONS has since added P9, P10, P11 as standalone rows and pre-decided P11 "standalone, not fold-into-P4" inside the dossier. The decision item and the registry disagree.
- PUBLICATIONS P9 internal drift: the dossier body still ends "Then draft," but the registry row and TODO 234 record the draft as written and gate-checked 2026-07-01.
- Citation-check target #5 RE-RUN (the inverted Kaplan-Shelah FETCH catch) lives only inside a checked [x] item (TODO 223) and PHASE_STATE prose; it has no open checkbox of its own and could be silently lost.
- Idle 2+ weeks on named next steps: P9 (16 days), P10 (15 days), P1/P2 (14 days), P4 expert-reader and P5/P6/P7 decisions (a month, Owen-gated). P11 is only ~7 days idle.

### 3. PORTFOLIO RECOMMENDATION (next 3 sessions)

(a) CCM corridor named next steps: ~40%. One full session: the Sonin-projector probe (the one untested corner, BUILDER-sized, both literature slots verified empty) plus rank-one interlacing (the last #154 upgrade-spec ingredient; closing it retires the whole #154 ledger). These are bounded completion moves. After them, pause the corridor: five consecutive arcs ended "frontier UNMOVED," the S4 forcing spec is banked, and further measurement of proven ceilings has visibly diminishing returns.

(b) Non-corridor research: ~25%. First a cheap SURVEYOR watch sweep (WATCH quadruple + the named submission watches; two weeks stale, and a missed R1 event is the only unbounded cost in the inventory). Then the SP3c/W6 derived-base rung: it is the counting joint's non-CCM half, untouched since 2026-07-02, needs no positivity, and the interface doc explicitly says the next move there is a build. Toy items (mesh-min proof, SC genus-2 rung) as small-slot filler.

(c) Shipping/publications: ~35%. Front-loaded, because these are the only decaying assets: (1) poll P1 merged-vs-closed and prep Owen's round-1 replies (minutes; blocks P4 sequencing); (2) open the P10 Mathlib PR (one agent session, already CLEAR-TO-PR; every week of master drift raises the port cost); (3) package P9 for Owen's MathSciNet pass. Close the two stale TODO checkboxes (195, 190 rewording) and give the citation-check #5 RE-RUN its own checkbox in the same pass.

Justification: the corridor is healthy but self-similar; its marginal session now buys a measured coordinate, not wall movement. The decay gradient points entirely at the Mathlib/arXiv pipeline, where finished mathematics is sitting idle past the 2-week line, and the one cheap unbounded-upside action (the literature watch) also lives outside the corridor.
