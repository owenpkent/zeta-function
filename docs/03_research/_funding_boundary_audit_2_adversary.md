# ADVERSARY report: the funding-boundary frame's closing audit (draft under attack)

> INDEPENDENT ADVERSARY lens, 2026-08-30, mandated per the #206 precedent (adversary on
> the decision itself, before any state file is touched). Target:
> [`funding_boundary_audit_2.md`](funding_boundary_audit_2.md) (the ORCHESTRATOR draft).
> Registration read in full: [`successor_frame_deliberation.md`](successor_frame_deliberation.md)
> Sections 5-7 (metric items (a)-(d), verdict wiring, exits 1-5 verbatim, expiry,
> standing lanes, the ceiling-as-output trap paragraph). First audit read in full:
> [`funding_boundary_audit_1.md`](funding_boundary_audit_1.md). Evidence verified at
> source: LEARNINGS #207-#212; [`_f2b_adversary.md`](_f2b_adversary.md) (verdict block +
> Section 7); [`f2b_visibility_floor.md`](f2b_visibility_floor.md) (header + Sections
> 7-8); [`f2a_certificate_class.md`](f2a_certificate_class.md) (Sections 6-7);
> [`../../experiments/spectral/e1af_funding_wall.md`](../../experiments/spectral/e1af_funding_wall.md)
> (Sections 2, 6, 7); [`../../PHASE_STATE.md`](../../PHASE_STATE.md) (top);
> [`../../TODO.md`](../../TODO.md) (WATCH item); [`../../PUBLICATIONS.md`](../../PUBLICATIONS.md)
> (Evaluation gate); [`reading_notes/proportion_support_landscape.md`](reading_notes/proportion_support_landscape.md)
> and [`reading_notes/af_funding_inputs_verification.md`](reading_notes/af_funding_inputs_verification.md)
> (the fabrication-catch count);
> [`../../experiments/spectral/e1ag_visibility_curve.md`](../../experiments/spectral/e1ag_visibility_curve.md)
> (header); `../../lean/ZetaRH/F2bSkeleton.lean` (the `MergeFloorTarget` name).
> The known risk under attack: a closing audit grading its own frame's life generously.
> This report edits nothing; the orchestrator applies the numbered fixes. No em dashes
> anywhere.
>
> **Verdict up front: CONCUR_WITH_FIXES** (twelve required fixes, none touching the
> disposition; the disposition itself survives every steelman I ran).

---

## Attack A. Arithmetic: sessions, tripwire, exits. LANDED (three findings; the count, the exit states, and the exit-2 reading otherwise verify)

**Re-derived from the primary records.** Frame sessions: F3 (#207), F1 (#208), F2a
(#211), F2b (#212) = 4 of 6. Audits: #209 (session two, exit 3's letter) and this one
(#213 pending) = two, neither a frame session per the #209 counter rule. #210 is a
hygiene/synthesis round, not frame-graded, by its own entry. The draft's Q1 count
("4 of 6; two audits; one non-frame hygiene round") is CORRECT. Every graded session
matches its registered spec; the one in-session addition (the Mueller rider at F2b) was
itself pre-registered in the frozen class definition (Section 6 item 5: "A bounded
fetch rides F2b"), so "nothing was added, repeated, or substituted" survives at both
the session and the rider granularity. Dates verify (#207/#208/#209/#210/#211 =
2026-08-26; #212 = 2026-08-28).

**Finding A1 (tripwire history is incomplete as printed).** The actual sequence is 1/3
(F3, #207) then **2/3 (F1, #208: "UNMOVED, tripwire 2/3")** then reset 0/3 (#209) then
1/3 (F2a, #211) then broken 0/3 (F2b, #212, with the adversary's dual-reading note:
1/3 on a no-reset reading, advancing on neither). The draft's line "Tripwire history
1/3, reset 0/3, 1/3, broken 0/3" omits the 2/3 state, and the Q1 table's F1 grade cell
omits it too (the F3 cell carries its count; the F1 cell does not). The conclusion
("never reached its firing count") is right: max 2/3. Fix 1.

**Finding A2 (the header overstates exit 3a's letter).** 3a fires on an unscheduled
session only if it ALSO "produces no Section 5 metric item passing the derivability
check" (registration Section 6, verbatim). The draft's header asserts any further
session "would be an unscheduled measurement session," converting 3a's conditional into
a certainty. PHASE_STATE's own #212 wording is the careful form ("any further frame
session would be exit 3a's subject"). The practical conclusion (the frame cannot
honestly continue without audit or re-registration) stands, since continuing on the
gamble of a passing mint is the bank pattern; but the audit should not quote 3a as
saying more than it says. Fix 2.

**Finding A3 (exit 1's "W1 ... lane-assigned" is unsupported by the record).** The
e1af dossier, Section 2: "The W1 computation on the actual AF window is open, not run
here (Section 7)"; Section 6: "open, not excluded by this probe, named as the standing
kill." The only lane assignment in the record is W2's: the ~2026-09-08 WATCH sweep
carries "the frame's W2 screen" (TODO, SURVEYOR item (iv)). No file assigns W1's
computation to any lane. The draft asserts "open and lane-assigned": false as written,
and it matters because W1 alone kills F1a's typing (the frame's Q3 item 3 yield). The
honest close either assigns it now (inventory it in the door list) or says plainly it
is unassigned. Fix 3, coupled to fix 8.

**Verified honest (no fix).** (i) Exit 2 "DISCHARGED, not fired": the registered
firing condition is "produces neither a theorem-shape (at the Section 5 bar) nor an
evading family" by F2b = frame session four (the two deadline clauses coincide, as
audit 1 recorded). The session adversary's verdict block states "Exit 2 does not
fire," classifies the outcome "(a) as scoped," explicitly rules out the #211(iv)(b)
relabeling case, and made the grade conditional on the fix pass, whose discharge #212
records as verified (Lean re-typecheck, build re-run, sweep). On the strictest reading
I can construct (the bar = proven modulo NAMED hypotheses), the narrowed scope carries
its L4-generic obligations as named per the adversary's own Section 7 fork; the grade
is the adversary's to give under the #206 wiring, and the draft adds nothing to it.
(ii) Exit 3b: audit 1 confirmed F3/F1 "filed their mints modestly"; #211 filed a
definition as a definition; #212 filed M4 AS a candidate. Never advanced. (iii) Exit 4:
GLSS I/II are 2503.15449/2507.06823, pre-frame, conditional-on-granted-law, entered as
boundary data at #208; no in-window record event. (iv) Exit 5: P2 polled 2026-08-25
and blocked upstream; P12 LaTeX+PDF 2026-08-26 with the remainder Owen's; WATCH due
~09-08 (not due at close); VERIFIER batch dated ~09-02 at audit 1 and enriched at
#212. All verified at source.

## Attack B. Yield inflation. LANDED (four findings; the mint grades themselves verify clean)

**Verified NOT inflated.** Q2(i) states the mint ledger exactly as graded: one
coordinate (M2), M1 ENRICHMENT, M3 CORROBORATION, M4 candidate-not-landed, the no-go
and contrapositive refused as mints by the document itself before the adversary ran
(f2b Section 7 pre-labels; adversary Section 6 "label checked: HOLDS"). The Q1 table
carries "NON-UNMOVED (M2 NEW-COORDINATE as scoped)" verbatim. The "method yield"
framing of F2a's FAIL round (Q3 item 2) is EARNED, not spin: the fail was real (four
landed attacks), the re-pose was per the adversary's own prescription, the delta-check
validated it clause-by-clause, and the adversary's perturbation constructions became
Theorem 1(i)/2(i)'s floors, which is exactly what the draft claims and no more. The
Q1 F2a row grades the session UNMOVED (A7) with no upgrade anywhere.

**Finding B1 (M2's narrowed scope is not carried everywhere; the (P-M) hypothesis is
absent from the entire draft).** #212(ii) summarizes the frontier's ceiling as
"complex-read pointwise capacity under the NAMED hypothesis (P-M) $|M| \le CTL$, which
the adversary proved UNDERIVABLE from satisfiability via the wild-$M$ construction,"
and the floors as regime-conditioned with the unconditional $k = O(1)$/C4-loc endpoint.
The draft's Q3 item 1 states the frontier two-sided-with-thin-band and then "no
conjectural hypotheses" with neither qualifier; the string "$|M|$" appears nowhere in
the draft. "No conjectural hypotheses" is accurate to the document (the (P-M)
hypothesis restricts the granted profile; it is named, not conjectural), but summarizing
the ceiling without it is precisely the softening the mandate told me to hunt. The
grade's own words are "NEW-COORDINATE **as scoped**"; the inventory must carry the
scope. Fix 4.

**Finding B2 (F1a's scope qualifier dropped in Q3 item 3).** #208's verdict is "F1a
SUPPORTED AS SCOPED," with the scope doing real work: the discriminating content is L1
congruence data "in the FINITE-DATA sense," the completed-totality clause
meter-invisible by the #172/#198 continuity law, and the competitor CO-LANDED at the
provability register (the pre-registered conjunction). Q3 item 3 keeps the price list
and the four-corner matrix but drops the AS-SCOPED tag and the conjunction (the Q1
table has them; the inventory item, which is what a successor will quote, does not).
Fix 5.

**Finding B3 (the confabulation count is wrong: three should be four).** In-frame
catches: the BBH abstract fabrication at F3 (#207(iv), "the #202 lesson's second
banked instance"); the AF "carried as hypotheses" clause at F1 (#208(ii), "the month's
THIRD"); and TWO more at F1's landscape sweep (#208(iii) "Two more summarizer
fabrications caught (FIVE this month)"; the landscape note's own header: "Two
summarizer fabrications were caught during THIS sweep"; the AF verification note calls
the clause catch "the month's two prior catches" + itself). Five for the month, of
which instance one (#202) is pre-frame: FOUR in the frame's span. The draft's "THREE"
undercounts the very discipline it is crediting. Fix 6.

**Finding B4 (Q3 item 7, "what did NOT land," omits three open items the frame's own
records carry).** (i) The Mueller thread: the ES-equivalence sourcing is tagged
[SINGLE-SOURCE] (Ivic math/0312097 p. 12; the 1983 paper itself paywalled), with the
removability question explicitly "unknown" (#212(i); class definition Section 6 item
5). The draft's item 6 cites the note's conclusion and drops its open thread. (ii) The
AF Lean repository's kernel tier: "honestly NOT-DETERMINABLE-WITHOUT-BUILD (priced
out)" (#211(i)); the skim discharged the #208 surface at inspection tier only, and
nothing schedules the build. (iii) The class definition's own Section 6 names two
in-print certificate families the theorem deliberately does NOT constrain: the
family-averaged pool (Özlük/CLLR, 91 percent at support 2 under GRH; "a named
OUT-OF-CLASS evading candidate") and the moment-class pool (Levinson/Conrey/PRZZ, BHB
$19/27$; "the F2b no-go will NOT constrain moment-funded certificates"), with Section
7 item 6 (is the moment exclusion principled or notational?) carried OPEN by the
executed checklist ("items 5-7 carry"). These are the frame's honest leftovers and
successor-relevant; item 7 and Q5's "untouched region" sentence must not reduce the
untouched set to the exact-identity register alone. Fix 7 (and the door-list half in
fix 8). Checked and NOT omissions: the f2b Section 8 open-scope triple (L4 regime
region, clustered constant, non-countable batteries) is in item 1; the e1af Section 7
limits are subsumed by the AS-SCOPED tag once fix 5 lands plus open W1 (fix 3); the
cross-machine sliver is in Q6; e1z is closed (#175(vi)(1), re-confirmed #210); the
#210 D3 tension and the Owen-gated standing-positive-control proposal belong to the
hygiene round's ledger entry, not to this frame's yield table (no fix, noted here for
the deliberation's benefit).

## Attack C. The disposition. PARTIAL (CLOSE survives every steelman; the door list and the gap governance do not survive as drafted)

**Steelman 1: re-register a continuation frame to land M4 or close the band.** Fails
against the draft, and the draft's argument does NOT prove too much. The remaining
work items (the L4 batch bound, V-F2b-6, the open band, `MergeFloorTarget` instances,
the V-F2a extractions) are finite proof/instrument work on the frame's own theorem,
already scheduled in the ~09-02 VERIFIER batch; a frame wrapper around lane-scheduled
work would re-create exactly the #201 signature (instrument output filed as frame
progress). The argument does not generalize to forbidding honest INSTRUMENT frames
(the repaired rule provides for them, and #206 Section 8 uses that provision for the
recovery register); the draft just fails to NAME that option in the inventory, which
is a door-list gap, not a disposition error. Fix 8(h).

**Steelman 2: attack the exact-identity register now as F2c.** Fails: the scope
sentence types that register as outside this class ("a different frame"), the
registered session order is complete, and the re-pose analysis for EF-in-frame (the
F2a adversary's A4, LANDED as the crux) is already written and handed over. Routing
through a deliberation with its own adversary is the #206 pattern and strictly
dominates a same-audit registration. CONCUR with CLOSE-AS-ATTACK-LANDED.

**Finding C1 (the door list is incomplete; four omissions, one of them slanted).**
(i) W1's open computation: the standing kill on the frame's OWN F1a yield, unassigned
anywhere (attack A3); an inventory that lists the frame's yields but not the named
kill against one of them is slanted toward the yield surviving. (ii) The two
out-of-class certificate families (B4(iii)): in-print, alive, and explicitly
unconstrained by the curve; the deliberation should see them next to door (a).
(iii) The instrument-frame option on the curve's own completion list, if the VERIFIER
batch leaves one (the repaired rule's honest-instrument provision); omitting it makes
"continuation = bank pattern" read as a theorem when it is a default. (iv) Status
notes: the ACS WATCH trigger stands unchanged (#206 disposed it; nothing since touched
it); the recovery register's registered frame-reopen condition (#206 Section 8: F1a
lands AND F1b grows a finite completion list) is now HALF-MET (F1a landed as scoped;
F1b posed, never executed), which the draft's door (b) should say; and G4/G15's parked
custody ("under the old exit 3a's custody") must transfer explicitly, since 3a dies
with the frame. Fix 8.

**Finding C2 (the close opens a governance gap the draft does not guard).** At close
the tripwire and exits die; the successor arms its own at registration, which the
draft schedules AFTER two dated lanes (~09-02, ~09-08). In the window between, NOTHING
polices probe-species work: 3a is dead, the successor's 3a-equivalent not yet armed.
This is exactly the unguarded-window species the #201 audit existed to catch. One
sentence closes it: only standing-lane work runs in the gap. Fix 9.

**Scheduling the deliberation after the VERIFIER batch and WATCH sweep: CONCUR,
justified rather than convenient.** The batch materially changes the M4 candidate's
status (batch bound proven or not) and the P13 package's completeness item; the sweep
services exit-4-species events, the Hilberdink screen, and the Suzuki-crowding
pressure; both are dated standing lanes needing no frame. Deliberating before them
would deliberate on information known to be about to change. With fix 9's guard, the
ordering is sound.

## Attack D. The publication flag (Q4). GLANCED (proper under the gate; one numbering front-run)

PUBLICATIONS.md's gate is six items (completeness; verification status; novelty; D-H
soundness; K1 circularity; honest framing; then venue/effort), run "for every candidate
before it earns a tier," with registry rows added only "if it survives" (How-to-add,
step 2). Raising a candidate inside a closing audit is proper: the audit tiers
nothing, venues nothing, quotes the registration's own "registry-grade mathematics
with an external audience either way" sentence WITH attribution, and says the gate "is
its OWN process and is not run inside this audit." Two checks pass on the package's
face: K1 (the scope sentence's "neither implies nor is implied by RH" is the gate-4b
answer) and honest framing (the no-go stays unminted). ONE front-run: "(a P13 slot)"
and same-day action 3's "the P13 flag recorded" assign the next registry number to a
candidate the gate has not seen; P-numbers are the registry's, post-gate. Cheap fix,
worth making because the whole Q4 paragraph is otherwise a model of not front-running.
Fix 10.

## Attack E. The wiring meta-check (Q6). GLANCED (honest; one unsupported credential)

The conditional-grade write-up is accurate to the record: the grade was conditional on
the M2-touching fixes (F2/F3/F4/F7/F8) landing in-session (adversary verdict block),
the fixes were the adversary's own supplied repairs ("none requires new mathematics
beyond what this report supplies"), discharge was verified by mechanical anchors
(re-typecheck, re-run, sweep; #212(v)), and the draft flags it as one more
same-session judgment needing advance wiring next time: that is the honest reading,
neither credit-grabbing nor false modesty. The delta-check credit is process, not
luck: #211(v) mandated it in advance on the critical path, and it caught the link
fine-class smuggler before theorem work (the smuggler being a hole in the checker's
OWN prior prescription is stated in #212(i) and the draft does not hide it). The
F2a-kill-becomes-floor-content claim verifies (A2's constructions are Theorem 1(i)'s
floor). ONE unsupported credential: "a fresh-context adversary." No cited record
documents the F2b adversary's context freshness; the records say "same-session
ADVERSARY" (#212) with bit-exact reproduction as the independence anchor. The draft
should use the record's own terms, especially in the paragraph rebutting verdict
inflation. Fix 11. The standing-blind-spot list (same-day grading; audit self-grading,
mitigated by this lens; the e1ad/e1v cross-machine sliver) matches the ledger.

## Attack F. Euphemism, drift, hygiene. GLANCED (two label nits; the rest clean)

Swept: zero em dashes in the draft (grep clean). Links resolve
(`successor_frame_deliberation.md`, `funding_boundary_audit_1.md`,
`f2b_visibility_floor.md`, `f2a_certificate_class.md`,
`../../experiments/spectral/e1af_funding_wall.md`). Numbers verified against sources:
$N = 14659$, e1ag 16/16 full / 15/15 quick, seed 212, envelope $6.9 \times 10^{-15}$
(cited as $7 \times 10^{-15}$ nowhere in the draft, no conflict), frame sessions 4/6,
battery 15/15 (2026-08-28), $\delta^{\ast} = (1+o(1))\log(TL)/\Theta_G$, the
$\Theta(\varepsilon_G TL)$ floor, D-H landmark $0.8085 + 85.699i$, e1ag header
self-describes as calibration ("Nothing here proves the theorems"), `MergeFloorTarget`
exists at `F2bSkeleton.lean` line 244. Two label findings: (i) the confabulation
count (fix 6, filed under B); (ii) "the four-report audit chain" (Q3 item 5) names
four of the frame's seven adversary/audit artifacts as if they were the chain,
omitting `_debranges_allow_poles_adversary`, `_e1af_adversary`, and audit 1; either
scope the label to F2 or enumerate. Fix 12. No other euphemism found: the draft's
exit-2, grade, and kernel-unchanged sentences track their sources word-for-word where
it matters ("the frame priced the information wall, it did not breach it, and it never
claimed otherwise" is exactly #212's posture).

---

## Required fixes (the orchestrator applies; old $\to$ new exact where wording)

1. **(Q1, arithmetic line + table.)** OLD: "Tripwire history 1/3, reset 0/3, 1/3,
   broken 0/3: it never reached its firing count." NEW: "Tripwire history 1/3, 2/3,
   reset 0/3, 1/3, broken 0/3 (the #212 adversary's dual-reading note: 1/3 on a
   no-reset reading, advancing on neither; moot at close): it never reached its firing
   count." AND in the Q1 table, F1 row grade cell, OLD: "UNMOVED (A8), letter of exit
   3 met" NEW: "UNMOVED (A8), tripwire 2/3; letter of exit 3 met".
2. **(Header.)** OLD: "any further session graded under this frame's wiring would be
   an unscheduled measurement session, so the frame cannot continue" NEW: "any further
   session graded under this frame's wiring would be exit 3a's subject (unscheduled;
   it fires the audit unless the session lands a derivability-passing metric item), so
   the frame cannot honestly continue".
3. **(Exit 1, last clause.)** OLD: "where it remains: W1's computation on the actual
   AF window is open and lane-assigned." NEW: "where it remains: W2's literature half
   is WATCH-screened (the ~09-08 sweep's named screen); W1's computation on the actual
   AF window is OPEN and UNASSIGNED, inventoried for the successor deliberation (door
   (f))."
4. **(Q3 item 1.)** OLD: "location frontier $\delta^{\ast} = (1+o(1))\log(TL)/\Theta_G$
   two-sided with thin band; the axes decouple;" NEW: "location frontier
   $\delta^{\ast} = (1+o(1))\log(TL)/\Theta_G$ two-sided with thin band (ceiling under
   the named (P-M) main-term hypothesis $|M| \le C\,TL$, proved underivable from
   satisfiability by the wild-$M$ construction; floors under L4's regime condition,
   with the $k = O(1)$/C4-loc endpoint unconditional); the axes decouple;".
5. **(Q3 item 3.)** OLD: "the price list is the L1-congruence-structured shift family
   at stated weights; the four-corner matrix; the competitor kill decidable (W1/W2)."
   NEW: "the price list is the L1-congruence-structured shift family at stated
   weights, SUPPORTED AS SCOPED (the finite-data L1 reading; the meter reads neither
   L2 direction); the four-corner matrix; the competitor co-landed at the provability
   register (the pre-registered conjunction), its outright win decidable (W1/W2)."
6. **(Q3 item 6.)** OLD: "THREE fetch-summarizer confabulation catches across the
   frame's span" NEW: "FOUR fetch-summarizer confabulation catches across the frame's
   span (BBH at F3; the AF hypotheses clause plus two landscape-sweep fabrications at
   F1: instances two through five of the month's five)".
7. **(Q3 item 7, append.)** Add: "Also open, from the frame's own records: the Mueller
   ES-equivalence sourcing is [SINGLE-SOURCE] (Ivic p. 12; the 1983 paper paywalled)
   with the removability thread flagged unknown; the AF Lean repository's kernel tier
   is NOT-DETERMINABLE-WITHOUT-BUILD (priced out at the skim, unscheduled); and the
   class definition's Section 6 names two in-print certificate families the curve
   deliberately does not constrain (family-averaged: Özlük/CLLR support-2 under GRH;
   moment-funded: Levinson/Conrey/PRZZ, BHB $19/27$ under RH), carried to the door
   list."
8. **(Q5 door list.)** Extend to: "(f) W1's computation on the actual AF kernel (the
   standing kill on F1a's typing; open, previously unassigned); (g) the two
   out-of-class input families the class definition names (family-averaged;
   moment-funded), untouched by the curve and un-posed as a class question (the
   definition's Section 7 item 6 carries the principled-vs-notational probe OPEN);
   (h) an honestly-registered INSTRUMENT frame on the curve's finite completion list
   (the L4 batch bound, the open band, `MergeFloorTarget` instances) if the ~09-02
   VERIFIER batch leaves one, per the repaired rule's instrument-frame provision."
   AND annotate door (b): "(its #206 Section 8 frame-reopen condition is HALF-MET:
   F1a landed as scoped, F1b never executed)"; door (c): custody of the G4/G15 parks
   transfers from the dead exit 3a to the successor registration's equivalent clause;
   door (d): "(the ACS positivity trigger and the Hilberdink screen stand unchanged
   among the sweep's standing screens)".
9. **(Q5 counter state, append.)** Add: "Between this close and the successor
   registration, only standing-lane work runs (VERIFIER ~09-02, WATCH ~09-08, P2/P10,
   P12 with Owen); probe-species work in the frameless window is out of order and
   becomes the deliberation's first agenda item."
10. **(Q4 + same-day action 3.)** OLD: "is a PUBLICATIONS.md gate candidate (a P13
    slot)" NEW: "is a PUBLICATIONS.md gate candidate (the next registry slot, P13, if
    it survives the gate)". OLD: "the P13 flag recorded" NEW: "the P13 candidate flag
    recorded (gate not yet run)".
11. **(Q2(iii).)** OLD: "the F2b grade was assigned by a fresh-context adversary that
    returned TEN blocking fixes" NEW: "the F2b grade was assigned by the same-session
    ADVERSARY (the #206 wiring; independence anchored by bit-exact reproduction at
    seed 212 and the standalone Lean re-typecheck) which returned TEN blocking fixes".
12. **(Q3 item 5.)** OLD: "the four-report audit chain (`_f2a_class_adversary`,
    `_f2a_delta_check`, `_f2b_adversary`, this file) as a methods record." NEW: "the
    frame's adversary/audit record (`_debranges_allow_poles_adversary`,
    `_e1af_adversary`, `_f2a_class_adversary`, `_f2a_delta_check`, `_f2b_adversary`,
    audit 1, this file) as a methods record."

Recommended, non-blocking: in Q1, cite the Mueller rider's pre-registration home
(class definition Section 6 item 5) inside the "nothing was added" sentence, so the
claim carries its own evidence; note in Q3 item 6 or Q5 that the #210 round's
Owen-gated standing-positive-control proposal remains flagged (hygiene-round custody,
not frame yield).

## Verdict block

- **Verdict: CONCUR_WITH_FIXES.** The audit may finalize once fixes 1-12 are applied
  in place. Nothing found touches the disposition: the session count, exit states,
  and grade citations verify against the primary records; the failures are an
  incomplete tripwire history, one overquoted exit letter, one false lane-assignment
  claim, scope qualifiers dropped from two inventory items, one undercounted
  discipline statistic, three omitted open items, four door-list omissions (one
  slanted: the named kill against a listed yield), an unguarded frameless window, a
  registry-number front-run, one unsupported process credential, and one label nit.
- **(i) CLOSE-AS-ATTACK-LANDED: CONCUR.** The registered question is answered at the
  honest register (soft NO decided at F2a and correctly unminted; the quantitative
  content is the two-axis law; the missing ingredient PRICED, not proven, as
  exact-class contact, and the draft claims no more); both continuation steelmen fail;
  the remaining work is lane-scheduled instrument work, which is the bank pattern's
  signature if wrapped in a frame.
- **(ii) The door list: DIVERGE AS DRAFTED; CONCUR once fixes 3, 7, 8 land.** As
  drafted it lists the frame's yields but omits the named kill against one of them
  (W1), the two out-of-class families the class definition itself names as
  unconstrained, the instrument-frame option, and three custody/status notes.
- **(iii) The deliberation's scheduling: CONCUR** (after the ~09-02 VERIFIER batch and
  ~09-08 WATCH sweep is justified by information, not convenience), conditional on
  fix 9's standing-lanes-only guard for the frameless window.
- **(iv) The P13 flag: CONCUR** as raised-not-adjudicated under the PUBLICATIONS.md
  gate, with fix 10 removing the registry-number front-run.
