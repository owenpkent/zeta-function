# Stream 2 ADVERSARY probe -- 2CCM.1 (CCM "det -> Xi" self-adjointness obstruction)

> STAGED overnight 2026-06-03. NOT committed. ADVERSARY report on the BUILDER coordinate
> staged at `stream2_ccm_selfadjoint_obstruction.{py,md}`. Read by ORCHESTRATOR, BUILDER,
> VERIFIER in the morning. Every number below was re-run by ADVERSARY from the repo root;
> the main agent must still independently re-derive before anything enters LEARNINGS.

## 0. What was attacked

The coordinate claims: the Connes-Consani-Moscovici 2025 "det_reg -> Xi" route
(arXiv:2511.22755) is RH-EQUIVALENT (not RH-reducing), and the mechanism is
SELF-ADJOINTNESS: a self-adjoint generator H = 1/2 + iA forces every zero of det(s - H)
onto Re(s) = 1/2 (Hilbert-Polya tautology), so "det -> Xi for self-adjoint H" already
asserts RH. The carrier of RH is the DEFINITENESS of the metric (the polarization, 08A M4),
demonstrated by a Krein-space probe (indefinite metric -> off-line zeros). Five PARTs,
all in-file assertions PASS.

## 1. Reproduction (ADVERSARY re-ran the script)

Command: `python -m experiments.orchestrator_sessions.overnight_2026_06_03.stream2_ccm_selfadjoint_obstruction`

All five PARTs reproduce the claimed numbers exactly:
- PART 1: max |Im(eig A)| = 8.182e-16, max |Re(zero)-1/2| = 8.327e-16 (200 draws, 8x8). PASS.
- PART 2: required eigenvalue 85.699 - 0.3085i (non-real); min ||A-A^*|| = 0.6170. PASS.
- PART 5: indefinite-metric max |Re(zero)-1/2| = 3.669, 84.13% complex; definite control 6.661e-16. PASS.
- PART 3: prime side -4.01, -4.78, -7.00, -3.86, +0.31 (x=50..20000), no limit. PASS.
- PART 4: D-H off-line zero 0.8085171825 + 85.69934849i (|f|=6.88e-40); von Mangoldt leaks
  n=6:1.94, n=14:2.85, n=21:3.29 off prime powers. PASS.

Infrastructure cross-check: `python -m experiments._shared.smoke_test` = 8/8 (D-H off-line
zero regression at 0.8085 + 85.70i confirmed). The D-H control is sound.

ADVERSARY independently extended PART 3 to x = 200000 (partial sums -6.99, -15.84, +2.67,
-23.46, -4.94): magnitude does not decay, so the "no convergence on the critical line" reading
is a genuine non-convergence, not a slow-convergence artifact. This is a correct classical fact
(-zeta'/zeta is the convergent prime series only for Re(s) > 1).

So: every "PROVED-IN-FILE" number is real and was re-derived. The arithmetic and linear
algebra are correct.

## 2. K1 -- circularity check

VERDICT: PASS, with a sharpening the BUILDER should adopt.

The proposal does NOT claim to prove RH and does NOT assert an intermediate claim that both
implies RH and is implied by RH in a hidden loop. It asserts the OPPOSITE of a shortcut: that
"det -> Xi for self-adjoint H" is RH-EQUIVALENT, which is the honest, R3.5-family reading. As a
no-shortcut statement this is the correct, non-circular content.

BUT there is a load-bearing gap in the MECHANISM as stated, which ADVERSARY found and which the
BUILDER must soften. The proposal's PART 1 establishes "self-adjoint => on-line zeros" only under
the hard-coded structure `zeros = {1/2 + i*lambda(A)}` for a FIXED finite matrix A, i.e. it
ASSUMES zeros = spectrum(fixed self-adjoint operator). That assumption IS Hilbert-Polya; it is not
a consequence of "the operator is self-adjoint."

CCM's det_reg is a zeta-regularized / Fredholm determinant of a family, and in the actual prolate
construction the Xi-zeros correspond to an eigenvalue-CROSSING CONDITION of an s-dependent family,
not literally to the spectrum of one fixed H. ADVERSARY breaking case (concrete):

  K(s) = diag(s, s^2 - c) is HERMITIAN at every real s. det(I - K(s)) = (1-s)(1-(s^2-c)).
  With c = -2, the factor 1 - (s^2 - c) = 0 has roots s = +/- i: OFF the real axis,
  even though K(s) is self-adjoint at every real s.

So "the operator is self-adjoint at real argument" does NOT by itself force the determinant's
zeros to be real. The on-line-ness in PART 1 comes specifically from `zeros = spec(fixed H)`. The
correct statement is therefore narrower than "self-adjointness => RH": it is "IF the construction
realizes the zeros as the spectrum of a single fixed self-adjoint operator, THEN RH." That "IF" is
exactly the Hilbert-Polya hypothesis and is the load-bearing import, alongside V1.

This does not break the coordinate (it is still a correct no-shortcut reading), but it relocates the
load: the circular-looking move is the identification `Xi-zeros = spec(fixed self-adjoint H)`, which
is Hilbert-Polya, not "self-adjointness." The Krein PART 5 is then about a different thing
(J-self-adjoint *fixed* operators), so it does not by itself rescue the "self-adjointness IS the
signature" slogan for the family-determinant case. REQUIRED SOFTENING S1 below.

## 3. K2 -- Davenport-Heilbronn discipline

VERDICT: PASS (strongest part of the coordinate).

Two stacked, correct obstructions:
- K2-a CATEGORICAL: D-H has no Euler product, the von Mangoldt coefficients delocalize off prime
  powers (re-derived: n=6,14,21 leaks), so there is no orbit-length spectrum {log p}, so the CCM
  operator is unbuildable. Reproduces #41/#20 faithfully.
- K2-b SPECTRAL: even force-fed, a self-adjoint H cannot host D-H's off-line zero (eigenvalue
  85.699 - 0.3085i is non-real). Correct arithmetic.

This is L-function-discriminating in the correct direction: the route lives on the Euler/Frobenius
half where K2 has teeth, and the off-line zero is correctly diagnosed as a self-adjointness
(signature) failure rather than a trace failure. No D-H-blindness. PASS cleanly.

One caveat (not a failure): K2-b's "self-adjoint H cannot host the off-line zero" again rides on
the fixed-operator `zeros = spec(H)` framing (see K1). It is correct under that framing. The
categorical K2-a does not depend on the framing and is unconditionally clean.

## 4. K3 -- function-field specialization

VERDICT: PASS, and it is the most useful structural content the coordinate could surface.

Over a curve C/F_q, Weil's 1948 proof produces the relevant positivity (Rosati positivity of the
Frobenius on H^1, equivalently the Riemann-Roch / Hodge-index signature) GENUINELY, as a theorem,
not by numerical fiat. The eigenvalues of Frobenius have |alpha| = sqrt(q), i.e. they sit on the
"critical circle," which is exactly the function-field analogue of "spec on the critical line."

So the coordinate's reading specializes correctly: in the FF case the self-adjointness /
polarization IS proved (Rosati), and that is precisely the structure CCM supply by fitting to low
zeros rather than deriving. This is the right diagnosis of the gap and matches the 08A spine
(RH = arithmetic Rosati positivity). The coordinate does NOT recover Weil's construction (it builds
no cohomology), but it correctly LOCATES what is missing on the Spec(Z) side: a non-circular proof
that the global generator is self-adjoint / the metric is definite = M4. Honest and consistent.

## 5. New-vs-restating

VERDICT: MOSTLY RESTATING. This is the coordinate's real weakness.

- The "self-adjoint => real spectrum => on-line zeros" tautology (PART 1) is textbook
  Hilbert-Polya; not new.
- The Krein / J-self-adjoint => complex spectrum fact (PART 5) is standard Krein-space theory
  (J-self-adjoint operators have spectrum symmetric about R and generically complex); not new.
- "The signature is the self-adjointness / metric definiteness = the polarization" overlaps very
  heavily with #44 ("det blind to the signature"), #30 ("all roads to the signature"), and the
  08A spine (RH = Rosati positivity). The proposal frames itself as "the mechanism #44 omitted,"
  but #44 already concluded the non-trivial zeros are the SIGNATURE of how F and Theta combine and
  that the determinant/trace cannot carry it. Saying "the signature = self-adjointness = metric
  definiteness" is a re-vocabulary of the same gap, not a new theorem or a new numerical anchor.
- The genuinely incremental content is thin but real: (i) it tests the Nov-2025 CCM frontier object
  against the project's K2 detector, which #40-#44 predate (CCM postdates them); (ii) it packages
  the "no shortcut" reading specifically for a determinant route (vs #43's pairing route); (iii) the
  Krein probe is an executable illustration of "definiteness carries the conclusion."

Net: the coordinate is a CONNECTING / re-vocabulary coordinate in the #40-#44 family, with one new
data point (CCM vs K2). It is not a new mechanism in the strong sense it claims.

## 6. Overclaim check

Two overclaims to correct:

- OC1 (the headline). "The precise mechanism is SELF-ADJOINTNESS: a self-adjoint generator forces
  every determinant zero onto Re=1/2." As shown in K1, self-adjointness of the operator forces this
  ONLY when the zeros are the spectrum of a single fixed operator (Hilbert-Polya). For a Fredholm
  family-determinant (which is what det_reg is), a family self-adjoint at real argument can have
  off-real determinant roots. So the mechanism is "Hilbert-Polya hypothesis (zeros = spec of a fixed
  self-adjoint H)," not "self-adjointness" per se. The slogan "the signature is the self-adjointness"
  should become "the signature is the realization-of-zeros-as-fixed-self-adjoint-spectrum (= the
  polarization), which is Hilbert-Polya."

- OC2 (the CCM import). The whole edifice rests on "CCM's H is self-adjoint" CITED from the abstract.
  The proposal honestly flags this as V1 and concedes falsification to #44 if H is non-self-adjoint.
  ADVERSARY adds: the project's OWN survey (`docs/03_research/spec_z_cohomology_landscape.md` line
  165) describes CCM as the "prolate / zeta spectral triples" program. In the prolate setting the
  natural operator is the prolate-spheroidal / Connes "W_H" operator, which IS self-adjoint, but the
  Xi-realization is via a DETERMINANT-RATIO / scattering condition, NOT zeros = spec of that operator.
  This makes OC1 the more likely failure mode than OC2: H may well be self-adjoint, yet the route to
  Xi may not be "zeros = spec(H)," in which case PART 1's tautology does not apply as stated and the
  coordinate weakens toward #44 anyway. So the falsification condition the proposal names (H
  non-self-adjoint => #44) is too narrow: the coordinate ALSO weakens if H is self-adjoint but the
  Xi-link is a family/scattering determinant rather than a fixed-spectrum determinant.

Everything labeled PROVED-IN-FILE is genuinely proved in-file (linear algebra, arithmetic, Krein
probe, prime oscillation, D-H delocalization). Everything labeled CITED / STRUCTURAL-READING is
correctly labeled. No claim to prove RH, advance M3/M4, or construct cohomology. The honesty
discipline is well kept; the overclaims are in the framing slogan, not the scope section.

## 7. Smallest concrete breaking case

K(s) = diag(s, s^2 + 2). Hermitian at every real s. det(I - K(s)) has a factor with roots
s = +/- i (off the real axis). Demonstrates that "self-adjoint at real argument" does not force
on-line determinant zeros without the extra `zeros = spec(fixed H)` hypothesis. (Re-run by
ADVERSARY; roots = 0 +/- 1i.) This is the single fact that converts OC1 from a theorem-sounding
slogan into a flagged hypothesis.

## 8. Verdict

ADVANCE-AS-NEGATIVE-COORDINATE (with required softenings).

The coordinate is honest, its numbers are real and reproduced, its K2 is clean and its K3
specialization is correct and useful. It is a legitimate no-shortcut / connecting coordinate that
(a) tests the newest CCM frontier object against the project's K2 detector and (b) re-localizes the
Spec(Z) gap as "prove the global generator self-adjoint / the metric definite, non-circularly = M4."
It does NOT prove RH, advance M3/M4, or contain a new mechanism; it is largely a re-vocabulary of
#44/#30/#43 plus one new data point. It must NOT be recorded as "the mechanism #44 omitted" without
the softenings below, because the headline mechanism (OC1) is imprecise: the load-bearing object is
the Hilbert-Polya hypothesis "zeros = spectrum of a fixed self-adjoint operator," not
self-adjointness alone.

Score: 4 / 10. (Honest, clean K2/K3, reproducible; but mostly restating #44/#30, with a headline
overclaim that needs the OC1 softening, and a CITED load-bearing import with a falsification
condition that is too narrow.)

## 9. Required softenings (exact)

- S1 (fixes OC1, load-bearing). Replace the headline "the mechanism is self-adjointness" with:
  "the mechanism is the Hilbert-Polya hypothesis -- the realization of the Xi-zeros as the spectrum
  of a SINGLE FIXED self-adjoint operator. Self-adjointness alone is not sufficient: a Fredholm
  family-determinant whose operator is self-adjoint at every real argument can still have off-line
  zeros (ADVERSARY breaking case, section 7). The on-line conclusion needs zeros = spec(fixed H),
  which is exactly Hilbert-Polya / the polarization, not a corollary of self-adjointness."

- S2 (fixes OC2 / widens falsification). Add to the falsification condition: "the coordinate also
  weakens to #44 if CCM's H is self-adjoint BUT the Xi-realization is a determinant-RATIO /
  scattering / family condition (as is typical in the prolate setting) rather than literally
  zeros = spec(H). VERIFIER V1 must confirm BOTH (a) H self-adjoint AND (b) Xi-zeros = spec(H) as a
  fixed-operator determinant, not just (a)."

- S3 (new-vs-restating honesty). Downgrade "sharpens #44 with the mechanism #44 omitted" to
  "re-vocabulary of #44/#30/#43 onto the CCM determinant route, plus the new data point of testing
  the Nov-2025 CCM object against K2." State explicitly that PART 1 (Hilbert-Polya) and PART 5
  (Krein-space complex spectrum) are textbook facts, used illustratively, not new results.

- S4 (PART 5 scope). State that PART 5 demonstrates "indefinite metric => off-line zeros" for FIXED
  J-self-adjoint operators only; it does not address the family-determinant case (S1) and so does
  not by itself establish "definiteness is THE carrier" for the CCM route. It supports the 08A-M4
  reading by analogy, not by proof.

- S5 (claim wording). The strapline "The signature is the self-adjointness, not the trace" should
  read "The signature is the polarization (metric definiteness / fixed-self-adjoint-spectrum
  realization), which is what #30/#44 already named; this coordinate relocates it onto the CCM
  determinant and confirms K2 has teeth there."

## 10. Handoff notes

- ORCHESTRATOR: keep as a negative/connecting coordinate in the #40-#44 cluster. Low new content
  (score 4); its value is the CCM-vs-K2 data point and the M4 relocation, not a mechanism. Do not
  promote to an e2*-numbered experiment unless V1 (with the S2 widening) confirms the fixed-operator
  determinant structure; if V1 finds a family/scattering determinant, fold into #44 and drop the
  "self-adjointness mechanism" framing entirely.
- BUILDER: apply S1-S5 verbatim before any LEARNINGS entry. The breaking case in section 7 should be
  added to the script as PART 6 (a family Hermitian-at-real-s with off-line determinant roots) so the
  file itself carries the caveat that defeats its own headline.
- VERIFIER: V1 must be split into V1a (H self-adjoint) and V1b (Xi-zeros = spec of that fixed H, vs a
  determinant ratio). V2 (Lean: A=A^* => spec real => zeros on Re=1/2) is fine as a finite tautology
  but should be annotated that it formalizes ONLY the fixed-operator case, not the family case.
