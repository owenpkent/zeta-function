# ADVERSARY report: compact_class_determinacy_survey.md (citation-verification round)

> ADVERSARY pass, 2026-07-22. Target: the SURVEYOR compactness-trojan dossier
> [`compact_class_determinacy_survey.md`](compact_class_determinacy_survey.md). Mandate: re-fetch
> every load-bearing citation (LEARNINGS #157 discipline: a load-bearing [FETCH]-tag was once
> INVERTED and caught only by adversary re-fetch), resolve the two incomplete scans and the GORZ
> discrepancy, attack the novelty claim, and adjudicate the pre-registered clause-(b) equivalence
> question. All unambiguous fixes applied in place in the note; this file is the working record.

## Verdict: PASS_WITH_FIXES

No inverted attribution found anywhere. Every load-bearing quote re-fetched this round came back
verbatim or stronger than the note's use of it. The fixes are precision and promotion fixes
(citation anchors, one convergence-mode gloss, two scan completions, one discrepancy resolution,
one risk-paragraph adjudication), none of which changes a verdict in the note's Section 4 table.
The NEW-LOAD-BEARING verdict on class 1.3 survives attack and is now better sourced than when the
note was filed.

## 1. Re-fetch results, per citation

| Citation | Claim in note | Result |
|---|---|---|
| arXiv:2409.04862 Forester-Remling | trace-normed canonical systems compact metric space; $H \mapsto m$ homeomorphism, metric $d(F,G) = \max_{\|z-2i\|\le1} \delta(F(z),G(z))$, spherical; both from Remling's book | **VERBATIM CONFIRMED** (both sentences). Precision: the compactness discussion is cited there to Remling Sec. 5.2, the homeomorphism to Remling Cor. 5.8; both sentences are quoted BACKGROUND in 2409.04862 (its own new results concern the reflectionless subclasses $\mathcal{R}_0(C)$). Fixed in note. |
| arXiv:1501.01268 Hur (new, corroboration) | (not in note before) | **INDEPENDENT CORROBORATION of the pillar found and added**: proves at source $V_+ = \{\mathrm{Tr}\,H = 1 \text{ a.e.}\}$ "is a compact metric space" (argument from Remling 2007 Sec. 2) and the de Branges/Winkler $H \mapsto m_H$ bijection is a homeomorphism onto $\mathcal{H} \cup \mathbb{R} \cup \{\infty\}$. Also pins the setup the note omitted: boundary condition $u_1(0)=0$; half-line trace-normed systems automatically limit point at $\infty$; the compact space's target INCLUDES degenerate elements (real constants, $\infty$). |
| arXiv:1703.01027 Lin | Carleman (h7)/(s6), Krein both forms, sufficiency-not-necessity, "weakest checkable" | **VERBATIM CONFIRMED**, all five statements, including Lin's "Carleman's (1926) condition" label (discrepancy 5 re-confirmed at source). One hardening applied: Krein's condition is stated for distributions with a positive density $f$ and all moments finite; note now says so. |
| arXiv:1902.03719 Branden-Huh | definition-as-limits; Thm 2.25 closure via Nuij homotopy; Thm 2.28 $\mathbb{P}L^n_d$ compact contractible; fixed $(n,d)$; no cross-degree theorem | **CONFIRMED on all five points** (definition sentence verbatim; 2.28 verbatim; 2.25 confirmed at introduction level + Nuij-type homotopy; explicitly no cross-degree limit theorem in the paper). |
| arXiv:math/0311369 Olshanski | Thoma set definition, "$\Omega$ is a compact space", product topology, extreme-character formula | **VERBATIM CONFIRMED** ("It is readily seen that $\Omega$ is a compact space"; topology induced from $\mathbb{R}^\infty \times \mathbb{R}^\infty$; agrees with pointwise convergence of characters). Discrepancy 4 CONFIRMED as logged: "space of virtual permutations" names the projective-limit space $\mathfrak{S}$ of the $S(n)$, not $\Omega$; the note's flag was correct. |
| arXiv:2511.22755 CCM quotes | "This convergence would entail RH using Hurwitz theorem..."; "Justifying rigorously this step is the main remaining obstacle..."; attachment to the prolate-ansatz formula (7.6); keyword-scan zero hits | **VERBATIM CONFIRMED including the attachment point** ("this step" = justifying that the educated-guess prolate formula (7.6) approximates the minimal eigenvector $\xi_\lambda$; refs their [4] Sec. 3). Discrepancy 3 confirmed as logged. One precision catch: CCM state the convergence "uniformly on closed substrips of the open strip $\Im(z) < 1/2$", stronger than the note's "uniformly on compacts" gloss; gloss was safe (weaker), not inverted; fixed in Section 0 + new discrepancy 6. Thm 5.10(iii) also re-verified at source ("all its zeros are on the real line and coincide with the spectrum"). |
| arXiv:2512.06468 (spot) | Theorem ASWE verbatim + refs | **VERBATIM CONFIRMED** including both references (AESW J. Anal. Math. 2 (1952) 93-109; Karlin p. 412). Paper is Katkova-Vishnyakova. |
| arXiv:math/9812166 Conrey-Li (spot) | abstract verbatim | **VERBATIM CONFIRMED.** |
| arXiv:2301.00421 Suzuki (spot) | abstract verbatim; v3 merges 2209.04658 | **VERBATIM CONFIRMED including the v3 merge note.** |
| arXiv:1801.07415 McPhedran (spot) | Lehmer/Keiper power-sum classification | **CONFIRMED** ("connect these coefficients with sums of powers of reciprocals of the zeros, in the form of sum rules"). |

Spot-checks performed: 4 (2512.06468, math/9812166, 2301.00421, 1801.07415), above the 3-minimum.
Em dashes: zero (checked before and after edits). Inverted attributions: none found.

## 2. Incomplete scans and the discrepancy, resolved

1. **2511.23257 full text: COMPLETED.** ar5iv is still broken, but the arXiv PDF was fetched and
   text-extracted locally (26 pp, ~15k words). Keyword scan: ZERO hits for normal family, Montel,
   Vitali, Helly, subsequential, moment problem, determinate, Carleman, Krein (single "subsequent"
   hit = "subsequent rows in T", a matrix-induction step). "compact" appears 3 times: compact
   selfadjoint operator, and twice as "compact subsets" inside uniform-convergence-plus-Hurwitz
   proofs. Step (5) confirmed verbatim in abstract and introduction. The note's SECONDARY absence
   claim is PROMOTED to FETCH-VERIFIED. Note: in 23257, 5.10 is a Proposition (polynomial
   real-rootedness); the load-bearing "Thm 5.10(iii)" of the survey belongs to 2511.22755 and was
   verified there; the in-repo `CCM-2025-Dlog-family.md` covers both papers under one label, so
   no misattribution.
2. **Killip-Simon at theorem level: COMPLETED** (arXiv:math-ph/0112008). Theorem 1 fetched: $J -
   J_0$ Hilbert-Schmidt iff Blumenthal-Weyl support + quasi-Szego integral + Lieb-Thirring
   eigenvalue sum + normalization. Method confirmed at source: Section 5 "Entropy and lower
   semicontinuity of the Szego and quasi-Szego terms"; the entropy map "weakly lower
   semicontinuous". Tag upgraded SECONDARY -> FETCH-VERIFIED. Precision added to the note's
   "line as INPUT" catch: the $\sigma_{ess} = [-2,2]$ OUTPUT direction of Theorem 1 is Weyl-soft
   (compact perturbation); the sign-structured sum rule is anchored to the $[-2,2]$ reference
   operator, so the disqualifier reading survives.
3. **GORZ statement strength: RESOLVED.** arXiv abstract (as served) = density-1 per degree + all
   $d \le 8$; published PNAS version (10.1073/pnas.1902572116) = "all but finitely many of the
   Jensen polynomials of each degree", Theorem 1 "hyperbolic for all sufficiently large $n$".
   Different versions, both real; the published cofinite form subsumes density-1 and is the one
   to quote. Discrepancy log entry 1 rewritten as RESOLVED; body of 1.1 updated.

## 3. Novelty-claim attack: outcome NOT KILLED, scope widened

Searched beyond the note's four corpora: canonical systems + zeta/RH; de Branges + zeta +
normal-family/compactness; Hilbert-Polya + Helly/Montel/subsequential; moment-determinacy + Xi;
sum-rule + zeta; the RMT canonical-systems school. **No prior poses compactness + determinacy in
place of uniform convergence for zeta's Section-7-style limits.** The UNPOSED verdict stands.

**Closest miss (named, now in the note's 3.5):** the RMT canonical-systems school. Valko-Virag's
stochastic zeta function (arXiv:2009.04670, GAFA 2022) and successors (Painchaud arXiv:2510.06120;
Hur arXiv:1501.01268, which uses the $V_+$ compactness itself) run the COMPACTNESS HALF of the
composite move as standard technology (operator-level limits via canonical systems, Weyl-data
convergence in weak/vague topologies, no uniform operator control). But every target is a random
universality-class operator (Sine$_\beta$, Bessel: Level 3), the limit is identified
probabilistically, and no determinacy pin to a deterministic arithmetic limit appears; no $\Xi$,
no RH. Second nearest: Suzuki arXiv:1204.1827 (canonical system built FROM zeta, unconditional
only for $\omega > 1$; RH restated as positive semidefiniteness of the Hamiltonian family):
canonical-system-native RH, but inverse-construction direction, no compactness or determinacy leg.

## 4. The clause-(b) equivalence attack (pre-registered): outcome

Question: is clause (b) (non-degeneracy / no-mass-escape of the limit Hamiltonian) EQUIVALENT to
the uniform det-class control (M4) in Hamiltonian coordinates?

**Outcome: no statement-level equivalence; risk relocated to price level; hedging in the note was
adequate in substance but overstated the identity risk, and is now fixed.**

- **Statement level:** M4 (uniform det-class control, locally uniform determinant convergence)
  implies (b) trivially. The converse has no visible route: (b) is a tightness / trace-equality
  statement about weighted spectral data, with no rate and no locally uniform determinant
  convergence; the compact-space framework (Remling/Hur) hands over locally-uniform-spherical
  $m$-convergence along subsequences for FREE, so what (b) adds is measure-level, strictly weaker
  in topology than what M4 pays for. Note also that (a)+(b)+compactness would give RH but not
  obviously M4's convergence statement itself, so the two are not even conditionally
  interchangeable as statements.
- **Price level (the surviving risk):** the only known routes to two-sided trace equalities of
  this shape are the explicit-formula inputs M4 consumes, so the COST may be conserved. This is
  now what the note says.
- **Two sharpenings banked into the note:** (i) clause (b) ALONE is Beurling-satisfiable at
  density level (the fake's chains embed in the same compact space, non-collapse, and conserve
  density-mass identically), so (b) by itself carries zero discrimination; all discriminating
  weight sits in the exact Euler-weighted equality inside the (a)+(b) joint. (ii) An off-line
  zero pair of the true $\Xi$ manifests in Hamiltonian coordinates not as mass escaping to real
  infinity but as a LOCAL mass defect of the limit measure against zeta's global data: clauses
  (a) and (b) are entangled, and the RH weight lives in their conjunction (the exact-mass
  identification), which is C1 in yet another set of clothes. Consistent with the project's
  all-roads pattern; the rung's honest value remains the third proof surface, as the note
  already priced.

## 5. Catches banked (numbered)

1. **F-R citation anchor split**: homeomorphism is cited to Remling Cor. 5.8, not Sec. 5.2 (note
   said "both ... Section 5.2"). Fixed.
2. **F-R statements are quoted background**, not that paper's own theorem (its new compactness is
   for reflectionless subclasses $\mathcal{R}_0(C)$); load rests on Remling's book. Independent
   corroboration (Hur 1501.01268, at source) found and added, with the exact normalization,
   boundary condition, automatic limit-point, and the degenerate elements inside the compact
   target. Fixed (adversary addendum in 1.3).
3. **CCM convergence-mode gloss**: "uniformly on compacts" vs CCM's stronger "closed substrips of
   $\Im(z) < 1/2$". Safe direction, not an inversion. Fixed + logged (discrepancy 6).
4. **Krein condition hypotheses**: positive density + all moments finite, omitted. Fixed.
5. **GORZ discrepancy resolved** (arXiv density-1 vs published cofinite: version difference; quote
   the published form). Fixed in 1.1 + log entry 1.
6. **2511.23257 absence claim promoted** SECONDARY -> FETCH-VERIFIED via local PDF extraction
   (zero keyword hits, step-(5) verbatim). Fixed in 3.1 + Section 7.
7. **Killip-Simon promoted** to theorem-level FETCH-VERIFIED; Weyl-soft precision added to the
   "$[-2,2]$ as input" disqualifier so it cannot be attacked as an inversion later. Fixed in 3.4.
8. **Survey coverage gap**: Suzuki's earlier canonical-system program (1204.1827) missing from the
   1.3/3.5 neighbor map despite being the nearest canonical-system-native RH statement in print.
   Added.
9. **Novelty scope**: "unposed everywhere checked" was true but under-scoped; the RMT
   canonical-systems school runs the compactness half as standard technology and had to be named
   as the closest miss for the claim to survive future adversarial rounds. Added (3.5 + table).
10. **Clause-(b) risk wording**: "may simply BE the uniform det-class control" overstated the
    identity risk; adjudicated to statement-level NO / price-level OPEN, with the
    Beurling-satisfiability and mass-defect entanglement sharpenings. Fixed in Section 5 and
    Section 8.
11. **Finite-chain embedding choice** (indivisible-interval tail extension to the half-line) is a
    normalization the BUILDER rung must fix and report; previously implicit. Fixed (addendum item
    iv).

## 6. What was NOT changed

- All six class verdicts (Section 4 table) stand as filed; no re-grading was warranted.
- The NEW-LOAD-BEARING call on 1.3 stands, now double-sourced.
- The tariff table stands (the 1.3 row's "[F-V 2409.04862, citing Remling 5.2]" is still accurate
  for the compactness half).
- Remaining honest gap, recorded in Section 8: a source read of Remling's book Sec. 5.2 itself is
  the one hardening step left on the pillar (currently: F-R quoting it + Hur proving the same
  statement by the 2007 argument).
