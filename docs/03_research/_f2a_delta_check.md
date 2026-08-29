# ADVERSARY delta-check: the re-posed F2a certificate class (bounded, pre-F2b)

> ADVERSARY deliverable, 2026-08-28. Mandate: the re-posed definition's own Section 8
> ("The re-posed definition returns to the adversary for a bounded delta-check") and
> PHASE_STATE's exit-2 bullet ("exit 2 BINDING at F2b = frame session four, the re-posed
> definition's bounded delta-check first on its critical path") prescribe this check
> before any F2b theorem-shape work. Target: [`f2a_certificate_class.md`](f2a_certificate_class.md)
> (RE-POSED 2026-08-26). Prior report: [`_f2a_class_adversary.md`](_f2a_class_adversary.md).
> Sources for the re-run: [`reading_notes/glss_full_funding_boundary.md`](reading_notes/glss_full_funding_boundary.md)
> Sections 1-3, [`reading_notes/alpoge_furman_two_thirds.md`](reading_notes/alpoge_furman_two_thirds.md).
> Scope discipline observed: this is the re-pose delta only, not a fresh adversary round,
> and it does not grade F2b. Nothing was edited by this check. No em dashes anywhere.
>
> **Verdict up front: PASS_WITH_EDITS.** All seven fixes DISCHARGED as prescribed; the
> clause-by-clause re-run passes for AF and GLSS I/II; ONE new hole found, in wording my
> own fix-1 prescription supplied (the link channel's self-stated error class admits an
> exactness smuggler that breaks the collapse-safety certificate as stated); repair is
> three wording edits, no design re-open. Edits 1-3 are blocking before F2b builds.

---

## 1. Fix discharge (required fixes 1-7 of the prior report)

1. **$\mathcal{P}_{\mathrm{link}}$ added: DISCHARGED.** C2 defines the channel with the
   prescribed two-sided read display, named $T$-uniform bandlimited test classes with
   stated support profiles, exact identity still excluded; prime grants fund
   $W_{\mathrm{prime}}$ past support 1 (the e1af family at weight $\log(H/h)$), curing
   A3(iv)'s inertness; the BGSTB $x^{\rho-\rho'}$ functional re-enters the proven core as
   link-shaped ($|\mathrm{EF\ read}|^2$ evaluated by proven prime mathematics, which is
   how it is proven; the $|{\cdot}|^2$ identity uses exactly C0's FE closure:
   $\sum_{\rho'} x^{\bar\rho'} = \sum_{\rho'} x^{1-\rho'}$, checked); the AF row's grant
   column is corrected and re-verified (Section 2 below); the Section 3(a) "verified by
   inspection" sentence is withdrawn with the re-run assigned to this check; D-H vacuity
   restated at the link per #202(iv). The optional $\mathcal{P}_{\mathrm{zero}}$
   widening was not taken (it was an either/or; the better branch was taken). The D1
   exchange-rate row carries the prescribed refactoring note ($N^{\circledast}$
   register). Residue: the "o(stated class)" wording, from my own fix-1 text, is the
   Section 3(a)-finding of this check (edit 1).
2. **T-uniformity discipline: DISCHARGED.** Clauses (a)-(e) verbatim as prescribed;
   amplifier and growing-arity constructions quoted in place with the amplitude-vs-phase
   distinction at (c); no-fixed-height and joint-satisfiability carried as consequences;
   collapse-safety certificate recorded in Section 3(b) with its cost. Re-attack in
   Section 3(b) below: the discipline as worded does block both prior constructions on
   the zero channel; its cross-channel amplitude wording is marginal-specific ("rescaled
   gap vectors"), which is where edit 3 lands.
3. **"Consistent" replaced by joint satisfiability: DISCHARGED.** Membership ("selects a
   grant set $G$ ... satisfied, jointly with C0 and the proven core, by at least one
   configuration") and quantifier ("quantifies over all jointly satisfiable $G$") both
   repaired; C4's definition and Section 5's naive no-go carry the same quantifier; the
   Lean sketch has the $\exists Z_0$ side condition. Grep confirms the only remaining
   "consistent" (C2 bullet) is the intentional historical quote of the posed wording.
4. **Error cap scoped to conjectural grants: DISCHARGED.** Cap scoped; the false
   relative-error parenthetical deleted with the Fujii counterexample and the
   shrinking-window smuggler recorded; absolute reading chosen with per-family window
   profiles; proven statements enter at proven classes (Fujii, MV, BGSTB named); E5
   square-root exclusion kept with the Section 6 item 6 quarantine.
5. **C4-loc co-primary: DISCHARGED.** Co-primary definition at C4-LIM with (M) and (S)
   quoted as the reason; C4-fin demoted to bookkeeping with its soft refutation
   recorded; the register-choice paragraph corrects the posed "covered-by-courtesy"
   accounting; Sections 3(a), 5 (naive no-go and Lean sketch), and 8 carry both
   registers. Two minor wording residues (edits 5, 6) in Section 3(b)'s K1 sentence and
   re-aim target (a).
6. **Scope sentence + re-aim + contrapositive: DISCHARGED.** The scope sentence is
   VERBATIM the prior report's blockquote (compared word for word). The "mathematical
   heart" sentence is corrected to decided-not-open (pinning power nil at o-class); the
   naive no-go retained for the record as soft-true with the (M)/(S)/(I) constructions
   quoted; re-aims (a)/(b) stated as prescribed; the #148 contrapositive explicitly
   demoted to compass with the mint prohibition and the #201 derivability reason.
7. **Smaller items: DISCHARGED.** D-H strip-multiset wording repaired at C0(iii) and
   Section 4 (exterior-to-exterior closure of the pairing: checked, $\beta \mapsto
   1-\beta$ maps $\sigma > 1$ to $\sigma < 0$); closed/open strip convention flagged
   with the F2b pick-one instruction; L-R row re-labeled ancestor-of-shape with the
   correlation-statistics-only caveat and superseded by (M)/(S)/(I); Lean sketch
   grant-set-indexed (`G : Set LawFamily`, `Satisfies`, satisfiability side condition,
   `reads : FiniteReadsFrom G`, link constructor, co-primary conjunction) with the
   instructive deleted-field-is-EF note kept.

## 2. The clause-by-clause re-run (load-bearing; replaces the withdrawn inspection claim)

| Clause | AF Theorem A | GLSS I | GLSS II |
|---|---|---|---|
| C0-FRAME | PASS: `ZeroConfig` = FE-paired strip multiset with multiplicities; RvM count sizes $d \asymp N(T,2T)$; $\Gamma$-facts in `PaperInputs`; all C0-provided | PASS: Section 2 classification + Prop. 1 are FE + Lebesgue bookkeeping; RvM decomposition $N = M + 7/8 + S$, $S \ll \log T$ IS the C0 frame | PASS: same frame; AH binning consumes only the marginal + FE combinatorics |
| C1-OBJ | PASS: rank-$d$ Gabor compression of Weil's form, $d \asymp N(T,2T)$; the named C1 archetype | PASS: Fejér-weighted second-moment kernel, bandlimited, finite-rank realizable at rank $\asymp TL \cdot \mathrm{supp}$ per C1(ii) | PASS: same engine (Theorem 2 identity on binned Fejér sums) |
| C2-FUND | PASS under the repaired pool: conjectural $G = \emptyset$; funding all proven: trace = C0-structural (RvM + Gabor frame, #208); HS budget = BGSTB via $\mathcal{P}_{\mathrm{link}}$ at proven class $O(1/\sqrt{\log T})$, prime side by MV at support $\le 1$; joint satisfiability of $\emptyset$ + core witnessed by zeta's own configuration | PASS: $G = \{$PCC$\}$: arity 2, Fejér amplitude $\le 1$ $T$-independent, moving windows exactly clause (c)'s named Remark-1 style, error $o(TL)$ absolute; satisfiability with core taken as met (sine-kernel-class satisfier; presupposition noted in Section 4 below); core reads: Fujii (marginal-shaped), MV (proven) | PASS: $G = \{$AH-Pairs, AH-Weak Density$\}$ (Corollary 2 rung: AH-Pairs + AH1 only): binned densities $P_{k/2}(T)$ in-pool by name, indicator amplitude, $j$/$M$-uniformity clauses stated per family, $R(T), R_P(T) \to 0$ read absolutely; satisfiable per the L-R near-witness with its carried caveat; PCC excluded from the SAME $G$ by joint satisfiability, per-certificate selection working as designed |
| C3-OUT | PASS: $N_0^s \ge (2 - R(\psi) - o(1))N$; the named AF shape | PASS: HMH derived, $E(T) = o(TL)$, $\#\{\mathrm{simple\ critical}\} \ge 2N - N^{\circledast}$; the named GLSS shape | PASS: $p_0 = 1$, density-1 simple-and-on-line; 50/50 at the AH1 rung |
| C4-LIM | Member does NOT certify C4/C4-loc ("RH itself is out of reach of the mechanism"); density register, as the table states | Does NOT certify C4/C4-loc: $o(TL)$ vs $< 2$ is the class gap; the ceiling inhabitant | Same; law-indifferent co-inhabitant of the ceiling |

Also re-verified: the GGOS row (granted marginal-$F$ lower bound on $[1, 3/2)$: arity 2,
bounded kernel, fixed support window, o-class; satisfiable by the PCC-class satisfier,
whose $F = \min(\alpha, 1)$ meets $F \ge 3/2 - \alpha - \epsilon$ there) and the AF
HL\*($k$) rungs (prime grants now non-vacuous through the link; see Section 4(c) for the
satisfiability-degenerates-to-truth note). The withdrawn Section 3(a) inspection claim
is hereby replaced by this re-run: both engines are in-class by name under the repaired
pool.

## 3. New-collapse hunt on the re-pose's own additions

**(a) The link fine-class smuggler: FOUND (the one real hole; edits 1-3 repair it).**
The error cap reads "$o(X)$ per shift on the prime side, $o$(stated class) at the link":
the link channel's class is SELF-STATED, while zero and prime channels are pinned.
Construction: for a fixed bandlimited decaying $g$, grant the link family
$f_T := g \cdot (\text{smooth cutoff at height } T)$, stated class $o(1)$ (or
$o(2^{-T})$). Syntax: $T$-dependence confined to a window parameter, so clause (c)
conforms; amplitude bounded; arity is not in question (link reads are linear); the
no-fixed-height clause does not unambiguously bite (the windowed variant IS a law in the
running variable; the constant variant $f_T := g$ is the degenerate case the wording
"pinned at a fixed height" does not literally cover). Satisfiability: zeta's
configuration satisfies the exact EF with error zero, hence every stated class: the
grant set is jointly satisfiable with C0 + core. Semantics: since the read tends to the
$T$-independent number $\sum_Z g$, the law forces the EXACT identity
$\sum_Z g = W_{\mathrm{prime}}(g) + W_\infty(g)$ in the limit; ranging $g$ over a
determining family pins $Z$ to zeta's actual multiset by the A4(i) uniqueness anchor
(Guinand-Weil/Vedana). Consequences: the matching class for this $G^*$ collapses to one
configuration, the counterexample-configuration method dies there, the collapse-safety
certificate's universal statement ("for every jointly satisfiable grant set the matching
class contains non-RH configurations") is FALSIFIED at $G^*$ (its truth at $G^*$ equals
not-RH), and the A4(i) frame collapse (no-go = unprovability statement about zeta)
re-enters in-pool. I verified the perturbations do fail against $G^*$: a merge at gap
$g$ costs $\asymp (\Delta L)^2 g^2$ per event in a bandwidth-$\Delta$ read, which no
$k(T) \to \infty$ schedule keeps below a $2^{-T}$ floor. Attribution, plainly: the
"o(stated class)" wording is from my own fix-1 prescription; the re-pose applied it
faithfully; the collapse-hunt sentence in Section 3(b) ("re-ran ... at o-class with
$T$-uniform test classes") is accurate about what was hunted, and the hole is the gap
between the hunted syntax and the written syntax. The repair pins the link class at
$o(TL)$ absolute for sup-normalized families (then the windowed-$g$ law carries
$TL$-scale slack and is harmless, and near-line splits cost $O(1)$ per event as the
certificate already computes): edits 1-3. Not a design re-open: the design sentence
"every link read carries its stated o-class slack, so C0(ii)'s exclusion stands"
already asserts the intent; the syntax under-enforced it.

**(b) The T-uniformity discipline as worded, re-attacked: HOLDS on the zero channel.**
The amplifier $\Phi_T = TL \cdot E(T)$ dies at (b); the growing-arity family dies at
(a). New attempts, all blocked: the fixed-$n$ coincidence ladder $\{\sum_{\mathrm{lines}}
h^n\}_{n \ge 2}$ granted for every $n$ (each family passes (a)-(d), but a single $h=2$
line costs the fixed constant $2^n - 2$ per event, so the merge at slow $k(T)$ stays
below every family's absolute $o(TL)$ slack simultaneously: no exactness forced; growing
arity was the only amplification route and it is syntactically closed); min-gap and
distinct-defective-line functionals (not fixed-kernel $n$-point shapes: out of pool);
amplitude-down rescaling (vacuous); read differences (slacks add, never cancel). I also
re-derived collapse-safety for COUNTABLE grant sets with non-decaying bounded kernels
(the worst admissible case: adding a zero can cost $O(N)$ on a cos-kernel read at an
adversarial site): a weighted averaging argument over injection/merge sites gives, for
any weights $w_u$ summing to 1, sites where family $u$'s per-event cost is
$O(1/w_u)$, so per fixed family the total perturbation cost is $O(k(T)/w_u) = o(TL)$:
the certificate's universal claim survives on the zero and prime channels; on the link
channel it survives exactly when edits 1-3 are applied (per (a)).

**(c) Joint satisfiability: no vacuity, no over-restriction; one semantic note.** Empty
$G$ is satisfiable (zeta witnesses the core), so AF is in-class unconditionally; PCC and
AH are each satisfiable with the core in the intended-model sense (satisfier existence
is a presupposition the (M)/(S)/(I) constructions consume: "perturb ANY satisfier"; the
in-print near-witness is L-R on the AH side, with the carried caveat; F2b's bookkeeping
should state the presupposition once); mutually contradictory laws are separated by
per-certificate $G$-selection as designed; the A3(ii) vacuous-certifier is excluded.
The note: prime-channel laws mention no configuration, so for them joint satisfiability
DEGENERATES TO TRUTH about the actual primes (a false prime grant makes $G$
unsatisfiable and its certificates vacuously out-of-quantifier; an HL\*-granting
certificate's class membership is contingent on HL\* exactly as its theorem is). This is
coherent and arguably the honest semantics; optional edit 7 records it. Core growth over
time (Section 7 item 5) implicitly time-indexes the collapse-safety certificate to the
current core; noted, no edit.

**(d) C4/C4-loc co-primary wording: consistent, two residues.** Section 1 (definition,
register choice), Section 3(a), Section 5 (naive no-go, Lean sketch), Section 7 item 1
annotation, and Section 8 all carry co-primacy correctly. Residues: Section 3(b)'s K1
sentence describes the counterexample form with "$E$ unbounded" only (edit 5); re-aim
target (a) words the curve in $E$-growth only, while C4-LIM requires every F2b statement
to cover both registers explicitly (edit 6; the (S) move is exactly why the
$N_{\mathrm{off}}$ reading needs stating: the marginal never sees the split, and the
domination $N_{\mathrm{off}} \le E$ is the transfer).

## 4. Convention spot-checks (Section 7 item 7(b), GLSS conventions)

- $N^{\circledast}$ as ordered pairs including self-pairs ($\sum_{\mathrm{lines}} h^2$,
  per the boundary note's Section 1.1) is FORCED by $E = N^{\circledast} - N =
  \sum h(h-1)$: consistent, and it gives $N^{\circledast} \ge N$, which the
  satisfiability example uses correctly.
- Parity: each $h(h-1)$ is a product of consecutive integers, even; $E$ even-valued
  nonnegative integer; $E < 2 \iff E = 0$: CHECK. Monotone: a line's full mass enters
  when $\gamma \le T$; terms nonnegative: CHECK.
- Conversion: $\sum_{\rho: \gamma \le T} (2 - H(\gamma)) = 2N - N^{\circledast}$, and
  $H(\gamma) = 1$ forces simple-and-critical (an off-line zero's FE partner shares its
  line, needing the strip closure C0 provides): $\#\{\mathrm{simple\ critical}\} \ge
  2N - N^{\circledast}$: CHECK. The "$(1+o(1))N$" with signed $o(1)$ is the papers' own
  notation: fine.
- Domination $N_{\mathrm{off}} + N_{\mathrm{mult}} \le E$ with the both-defective
  corner: on an $h = 2$ line no element can be both off-line and multiple (an off-line
  $m \ge 2$ zero forces $h \ge 4$ via its partner), so $h = 2$ gives $\le 2 = h(h-1)$
  with equality at an off-line simple pair or a critical double; for $h \ge 3$ even
  double-counted defectives give $\le 2h \le h(h-1)$: CHECK, matching the prior A5 note.
  C4-LIM's $\ll$ vs V-F2a-4's $\le$: the $\le$ is the lemma, $\ll$ follows: consistent.
- Equal-ordinate exclusion in $N(\lambda)$ ($0 < (\gamma'-\gamma)L \le \lambda$) vs
  inclusion in $N^{\circledast}$: used consistently everywhere it matters, including the
  (M)-move invisibility argument (merges create equal-ordinate mass invisible to
  $N(\lambda)$) and the C2 special-case list.
- Small flags, note only: "Fujii's $O(T\sqrt{\log T})$" is shorthand for the proven
  $O(T\sqrt{\log(2+UL)})$ (weaker-than-proven citation of a proven statement: cannot
  smuggle); closed vs open strip carried as flagged (boundary zeros in C0-closed cost
  $E$ through $h \ge 2$ lines like any FE pair: the identities are $\beta$-indifferent,
  so genuinely harmless).

## 5. Verdict

**PASS_WITH_EDITS.** The re-pose is faithful to the prescription, the record holder and
both ceiling engines are in-class by the formal re-run, the prior attacks stay closed,
and the definition is sound to build F2b on ONCE the link-channel class floor is pinned.
Edits (apply verbatim; 1-3 blocking, 4-6 recommended, 7 optional):

1. C2 error-class paragraph. OLD: "$o(X)$ per shift on the prime side, $o$(stated
   class) at the link." NEW: "$o(X)$ per shift on the prime side; at the link, $o(TL)$
   absolute per sup-normalized family ($\sup|f_T| \le 1$; the grant's stated class names
   its support/window profile, never a rate finer than $o(TL)$), with constant-in-$T$
   link members not grantable (the no-fixed-height clause applies at the link: a fixed
   test function's read is $T$-independent, so any vanishing stated class forces the
   exact identity, C0(ii)'s excluded object)."
2. $\mathcal{P}_{\mathrm{link}}$ paragraph. OLD: "with the exact identity still
   excluded: every link read carries its stated o-class slack, so C0(ii)'s exclusion
   stands." NEW: "with the exact identity still excluded: every link family is
   sup-normalized and carries $o(TL)$ absolute slack under the T-uniformity discipline
   (clause (b) read as $\sup|f_T| \le 1$), so C0(ii)'s exclusion stands."
3. T-uniformity clause (b). OLD: "(b) kernel applied to rescaled gap vectors with
   $T$-independent bounded amplitude (normalize $\sup|K| \le 1$);" NEW: "(b)
   $T$-independent bounded amplitude in every channel (gap kernels normalized
   $\sup|K| \le 1$; link test families $\sup|f_T| \le 1$);"
4. Section 3(b) collapse-safety. OLD: "so the three-channel pool remains
   collapse-safe." NEW: "so the three-channel pool remains collapse-safe; the
   delta-check's link fine-class smuggler (a windowed fixed test function at a
   self-stated vanishing class, which would have re-pinned the matching class to zeta's
   multiset per A4(i)) is closed by the link clauses of the error cap and discipline
   (b)."
5. Section 3(b) K1 check. OLD: "matching a grant set with $E$ unbounded (an existence"
   NEW: "matching a grant set with $E$ unbounded, and for the C4-loc register with
   $N_{\mathrm{off}}$ unbounded (an existence"
6. Section 5 re-aim (a). OLD: "which $E$-growth rates are certifiable-against at which
   granted classes;" NEW: "which $E$-growth rates are certifiable-against at which
   granted classes, stated at both co-primary registers (the $E$-curve primary, its
   $N_{\mathrm{off}}$ reading via the domination $N_{\mathrm{off}} \le E$ and the
   (S)-move floor showing the marginal cannot improve on it);"
7. Optional, C2 joint-satisfiability bullet, append after "made precise
   simultaneously).": "Channel asymmetry, noted: prime-channel laws mention no
   configuration, so for them joint satisfiability degenerates to truth about the
   actual primes; an HL\*-granting certificate's class membership is contingent on
   HL\* exactly as its theorem is."

With edits 1-3 applied, the collapse-safety certificate's statement is true as written
on all three channels, and F2b may proceed on this definition.
